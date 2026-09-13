# Contribution policy

**We welcome issue reports and suggestions from everyone.** Follow the
[README feedback process](README.md#feedback) to contribute through issues.

**Pull requests are limited to OpenAI team members.** External contributors
should use issues rather than opening pull requests, including for documentation
or asset changes.

`openapi.yaml` and `openapi.json` are generated publication artifacts. Direct
edits here do not change the upstream source and may be overwritten by the next
publication.

## Feedback and security reports

For ordinary specification errors, follow the [README feedback
process](README.md#feedback). Include the affected revision, endpoint and HTTP
method or schema, expected behavior, and a minimal example using synthetic data.
Do not include API keys, authorization headers, cookies, customer data, or private
URLs in issues, logs, or screenshots.

Report suspected vulnerabilities privately using [SECURITY.md](SECURITY.md).
Do not open a public issue or pull request for a security vulnerability.

## Team member guidance

OpenAI team members make specification corrections in the upstream
source using the [internal OpenAPI authoring
guide](https://github.com/openai/openai/blob/master/lib/js/oai_js_apidocs_data/src/openapi/README.md)
and its review and validation requirements. The publisher synchronizes the
generated artifacts. Team members can submit pull requests here for repository
policy, supporting documentation, and assets, subject to required review.

- Use synthetic examples and placeholder credentials; redact sensitive data
  before sharing any diagnostic output.
- Request security review for changes affecting server URLs, authentication,
  publisher access, review rules, CI, or dependencies. Review specification
  corrections and their generated effects upstream.
- If introducing CI or dependencies, review their source and permissions, pin
  Actions to full commit SHAs, and establish dependency updates. Never expose
  credentials to untrusted changes or examples.
- For local documentation or policy maintenance, run `git diff --check`, check
  changed links and Markdown, and confirm the generated specification is
  unchanged. The `Generated files unchanged` CI check rejects PR changes to
  `openapi.yaml` or `openapi.json`, including deletions and renames. There is no
  application build in this repository.
