# Security policy

## Reporting a vulnerability

Report suspected vulnerabilities privately through [GitHub private vulnerability
reporting](https://github.com/openai/openai-openapi/security/advisories/new).
Do not disclose vulnerabilities, credentials, or sensitive data in public issues
or pull requests. This repository does not accept contributions or public
security-fix pull requests.

Include the affected specification revision, endpoint and HTTP method or schema,
expected behavior, security impact, and a minimal example using synthetic data.
Remove API keys, authorization headers, cookies, customer data, and private URLs
from reports, logs, and screenshots. Never include a live credential as evidence.

For ordinary specification errors without security implications, use the
[README feedback process](README.md#feedback). For account or API support, use
[OpenAI Support](https://help.openai.com/).

## Scope and security expectations

This repository publishes generated `openapi.yaml` and `openapi.json` artifacts
and supporting documentation. The specification is consumed by client generators
and API explorers; its authenticity and integrity matter to those consumers.

- Published specifications must reflect the intended upstream source. Changes to
  server URLs, authentication declarations, schemas, and examples need review for
  their effect on consumers, including credential handling.
- Examples and documentation must contain only synthetic data and placeholder
  credentials suitable for public distribution.
- Repository maintenance requires review by the appropriate owners. The
  automated publisher updates generated artifacts from upstream; review of source
  changes belongs in that source repository.
- Changes to publisher access, review rules, CI, or dependencies require security
  review. Preserve the integrity of the publication path.

The upstream generator, publisher implementation, API service, and client runtimes
are not implemented here. Specification declarations alone do not prove how
those systems enforce authentication or authorization. Report suspected security
issues privately even when the affected component is uncertain; maintainers can
route them to the appropriate owner.
