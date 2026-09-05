<div align="center">
  <h1>OpenAI API · OpenAPI specification</h1>

  <p>A machine-readable description of the OpenAI REST API, authored in OpenAPI 3.1.</p>

  <p>
    <a href="./openapi.yaml"><strong>Explore the spec</strong></a>
    ·
    <a href="https://developers.openai.com/api/reference/overview">API reference</a>
    ·
    <a href="https://help.openai.com/">Support</a>
  </p>

</div>

<p align="center">
  <img src="./assets/openai-api-reference.png" alt="OpenAI Developers Responses API reference" width="80%">
</p>

## About

This repository publishes the OpenAPI specification for the OpenAI API. The spec describes the API's endpoints, authentication, parameters, and request and response schemas.

`openapi.yaml` and `openapi.json` are generated artifacts synchronized automatically from upstream source. For specification corrections, follow the [contribution workflow](#contributing).

Use it to generate typed clients, build API explorers, configure testing tools, or work with the OpenAI API in any OpenAPI-compatible workflow.

> [!NOTE]
> Looking for human-readable documentation, guides, and examples? Visit the [OpenAI API docs](https://developers.openai.com/api/docs).

## Get the specification

Browse [`openapi.yaml`](./openapi.yaml) or [`openapi.json`](./openapi.json) directly, or download the latest YAML version:

```sh
curl -L https://raw.githubusercontent.com/openai/openai-openapi/main/openapi.yaml \
  -o openai-openapi.yaml
```

The document uses **OpenAPI 3.1** and can be imported into tools that support the OpenAPI ecosystem.

## Generated SDKs

OpenAI publishes the following official SDKs generated from this specification:

| Language or platform | Repository |
| --- | --- |
| Python | [`openai-python`](https://github.com/openai/openai-python) |
| JavaScript / TypeScript | [`openai-node`](https://github.com/openai/openai-node) |
| .NET | [`openai-dotnet`](https://github.com/openai/openai-dotnet) |
| Go | [`openai-go`](https://github.com/openai/openai-go) |
| Java | [`openai-java`](https://github.com/openai/openai-java) |
| Ruby | [`openai-ruby`](https://github.com/openai/openai-ruby) |

## Contributing

Make specification changes in the upstream source so they persist through the next publication. Direct edits to this repository's generated YAML or JSON do not update that source.

**OpenAI contributors with monorepo access:** Follow the [internal OpenAPI authoring guide](https://github.com/openai/openai/blob/master/lib/js/oai_js_apidocs_data/src/openapi/README.md) and its package guidance to locate the editable definition, generate the specification, and validate the change. The publication workflow updates this repository's spec files automatically.

**Contributors without monorepo access:** Use the [feedback process below](#feedback). Include proposed wording or a schema snippet in the issue when helpful so maintainers can apply the correction upstream.

Changes to this README and repository assets can be submitted as pull requests here.

## Feedback

Found an incorrect schema, a missing field, or another problem with the specification? [Search the existing issues](https://github.com/openai/openai-openapi/issues) and, if it has not already been reported, [open a new issue](https://github.com/openai/openai-openapi/issues/new).

When reporting a problem, include the affected endpoint and HTTP method or schema, the expected behavior, and a minimal example when possible. The OpenAI team will make a best-effort attempt to triage and resolve spec issues.

For immediate help with the OpenAI API, [contact OpenAI Support](https://help.openai.com/en/articles/6614161-how-can-i-contact-support).

## License

This project is licensed under the [MIT License](./LICENSE).
