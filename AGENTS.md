# Repository guidance

Read the [contribution workflow](README.md#contributing) before making changes.

- `openapi.yaml` and `openapi.json` are generated publication artifacts. For endpoint, schema, parameter, or response-header changes, use the upstream authoring guide linked from the README and follow the source repository's instructions. Do not directly author a spec correction in these generated files.
- If the upstream source is inaccessible, prepare an issue through the README's feedback process with the endpoint/method or schema, expected behavior, and a minimal example. Do not invent an internal source path or claim the correction has been applied.
- Edit this repository's README and assets here when the request concerns those files.
- For documentation changes, run `git diff --check`, check affected links and Markdown, and confirm that generated spec files are unchanged. This repository has no local build or test commands.
