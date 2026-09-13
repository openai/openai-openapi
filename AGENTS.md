# Repository guidance

This repository does not accept contributions. Read the
[contribution policy](CONTRIBUTING.md) before working here. The guidance below is
for authorized maintainer work; it is not an invitation to submit pull requests.

- `openapi.yaml` and `openapi.json` are generated publication artifacts. For endpoint, schema, parameter, or response-header changes, use the upstream authoring guide linked from the README and follow the source repository's instructions. Do not directly author a spec correction in these generated files.
- If the upstream source is inaccessible, prepare ordinary, non-security feedback through the README's feedback process with the endpoint/method or schema, expected behavior, and a minimal synthetic example. Route suspected vulnerabilities privately through `SECURITY.md`. Do not invent an internal source path or claim the correction has been applied.
- Only perform local documentation, policy, or asset maintenance when authorized by a maintainer.
- For documentation changes, run `git diff --check`, check affected links and Markdown, and confirm that generated spec files are unchanged. This repository has no local build or test commands.

## Security guidance

- Follow [SECURITY.md](SECURITY.md). Never publish suspected vulnerabilities in public issues or pull requests.
- Use synthetic examples and placeholder credentials. Do not commit, log, or attach API keys, authorization headers, cookies, customer data, private URLs, or unredacted screenshots. Redact diagnostic output before sharing it.
- Review changes to server URLs, authentication declarations, schemas, and examples for their effect on generated clients and credential handling. Make specification corrections and validate their generated effects upstream.
- Request security review before changing publisher access, review rules, CI, or dependencies. Preserve required review and the upstream publication path.
- If CI or dependencies are introduced, use least-privilege job permissions, full-SHA Action pins, and dependency-update automation. Do not run untrusted changes with secrets or write-capable tokens.
