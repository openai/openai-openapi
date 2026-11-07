# Repository guidance

Read and follow [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md), including contribution eligibility, review, validation, and sensitive-data requirements. PRs are limited to OpenAI team members; external contributors use [feedback](README.md#feedback).

- Never author corrections directly in generated `openapi.yaml` or `openapi.json`. Follow the [upstream authoring guide](README.md#contributing) and source repository instructions for endpoint, schema, parameter, or response-header changes; review generated-client and credential-handling effects upstream.
- If upstream is inaccessible, prepare non-security [feedback](README.md#feedback) with the endpoint/method or schema, expected behavior, and a minimal synthetic example. Report vulnerabilities privately per SECURITY.md. Never invent an internal source path or claim an unapplied correction.
- For local documentation, policy, or asset PRs, preserve required review and upstream publication. Run `git diff --check`, check affected links/Markdown, and confirm generated specs are unchanged (`Generated files unchanged` CI). No application build exists.
- Request security review before changing publisher access, review rules, CI, or dependencies. New CI/dependencies require least-privilege job permissions, full-SHA Action pins, and dependency-update automation; never run untrusted changes with secrets or write-capable tokens.
