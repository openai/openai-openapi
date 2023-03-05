import {
  Project,
  Node,
  ts,
  CodeBlockWriter,
  OptionalKind,
  ParameterDeclarationStructure,
  MethodDeclaration,
} from "ts-morph";

function writeBody(writer: CodeBlockWriter, argName: string, body: string) {
  return writer
    .write(`if (${argName}.stream) `)
    .write(
      body
        .replace("createRequestFunction", "createStreamFunction")
        .replace(argName, `{ ...${argName}, stream: true }`)
    )
    .write(" else ")
    .write(body.replace(argName, `{ ...${argName}, stream: false }`));
}

function transformParameters(
  kind: "stream" | "json",
  parameters: OptionalKind<ParameterDeclarationStructure>[] | undefined
) {
  return parameters?.map((param, idx) => {
    return idx === 0
      ? {
          ...param,
          type:
            kind === "json"
              ? `${param.type} & { stream?: false }`
              : `${param.type} & { stream: true }`,
        }
      : param;
  });
}

function extractKeyTypes(method: MethodDeclaration) {
  const requestName = method.getParameters()[0].getName();
  const requestType = method.getParameters()[0].getTypeNodeOrThrow().getText();
  const responseType = requestType.replace("Request", "Response");

  return { requestName, requestType, responseType };
}

function transformObject(methodName: string, sourceNode: Node) {
  const method = sourceNode
    .getDescendantsOfKind(ts.SyntaxKind.MethodDeclaration)
    .filter((declaration) => declaration.getName() === methodName)[0]!;

  const keyTypes = extractKeyTypes(method);
  const body = method
    .getBodyOrThrow()
    .getText({ trimLeadingIndentation: true });

  const docs = method.getJsDocs()[0].getText({ trimLeadingIndentation: true });
  const structure = method.getStructure();
  const returnType = structure.returnType as string;

  method
    .getParent()
    .asKindOrThrow(ts.SyntaxKind.ObjectLiteralExpression)
    .insertPropertyAssignment(method.getChildIndex(), {
      name: methodName,
      leadingTrivia: docs + "\n",
      initializer: (writer) =>
        writer
          .write("(() => {")
          .indent(() => {
            writer
              .setIndentationLevel(writer.getIndentationLevel() - 1)
              .write(`function ${methodName}(): unknown`)
              .inlineBlock(() => writeBody(writer, keyTypes.requestName, body))
              .write(";");

            writer.writeLine(`return ${methodName};`);
          })
          .write("})()"),
    })
    .getFirstDescendantByKindOrThrow(ts.SyntaxKind.FunctionDeclaration)
    .set({
      parameters: structure.parameters,
      isAsync: method.isAsync(),
      overloads: [
        {
          isAsync: method.isAsync(),
          parameters: transformParameters("json", structure.parameters),
          returnType,
        },
        {
          isAsync: method.isAsync(),
          parameters: transformParameters("stream", structure.parameters),
          returnType: returnType.replace(
            keyTypes.responseType,
            "ReadableStream"
          ),
        },
      ],
      returnType: returnType.replace(
        keyTypes.responseType,
        `${keyTypes.responseType} | ReadableStream`
      ),
    });

  method.remove();
}

function transformClass(methodName: string, sourceNode: Node) {
  const method = sourceNode
    .getDescendantsOfKind(ts.SyntaxKind.MethodDeclaration)
    .filter((declaration) => declaration.getName() === methodName)[0]!;

  const keyTypes = extractKeyTypes(method);

  const body = method
    .getBodyOrThrow()
    .getText({ trimLeadingIndentation: true });
  const docs = method.getJsDocs()[0].getText({ trimLeadingIndentation: true });
  const structure = method.getStructure();

  method.set({
    name: methodName,
    scope: structure.scope,
    parameters: structure.parameters,
    docs: [],
    overloads: [
      {
        leadingTrivia: docs + "\n",
        parameters: transformParameters("stream", structure.parameters),
        returnType: `AxiosPromise<ReadableStream>`,
      },
      {
        parameters: transformParameters("json", structure.parameters),
        returnType: `AxiosPromise<${keyTypes.responseType}>`,
      },
    ],
    statements: (writer) =>
      writer.indent(() => {
        writer.withIndentationLevel(writer.getIndentationLevel() - 1, () => {
          writeBody(writer, keyTypes.requestName, body);
        });
      }),
  });
}

const project = new Project();
project.addSourceFilesAtPaths(process.argv[process.argv.length - 1]);

const sourceFile = project.getSourceFileOrThrow("api.ts");
const declarations = sourceFile.getExportedDeclarations();

const methods = new Set(
  sourceFile
    .getInterfaces()
    .filter((declaration) => {
      return declaration
        .getDescendantsOfKind(ts.SyntaxKind.PropertySignature)
        .some((a) => a.getName().includes(`'stream'`));
    })
    .map((decl) =>
      decl
        .findReferencesAsNodes()
        .map((refs) =>
          refs
            .getFirstAncestorByKind(ts.SyntaxKind.MethodDeclaration)
            ?.getName()
        )
    )
    .flat(2)
    .filter((x): x is string => !!x)
);

for (const method of methods) {
  transformObject(method, declarations.get("OpenAIApiFp")![0]);
  transformObject(method, declarations.get("OpenAIApiFactory")![0]);
  transformClass(method, declarations.get("OpenAIApi")![0]);
}

sourceFile.saveSync();
