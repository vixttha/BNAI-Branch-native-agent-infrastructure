# Execution profiles — not a sixth layer

BNAI is independent of where authorized operations run. Standard GitHub-hosted runners on public repositories are the primary reference profile and the only profile used by this reference repository's CI. Never infer that all installations need Actions.

| Profile | What can be done | Cost and safety boundary |
|---|---|---|
| Public standard GitHub-hosted Actions | Automated public builds, tests and batch tasks | Standard public compute free under GitHub terms; do not expose private inputs |
| Private standard GitHub-hosted Actions | Private builds/tests | Included allowance then billed or blocked; verify budget and retention |
| Self-hosted Actions runner (local or remote) | Owner-controlled execution | Own hardware/hosting cost and isolation; do not run untrusted public jobs on persistent hosts |
| Larger/paid hosted runners | Specialized workloads | Explicit approval and cost ceiling |
| Connector/API-only, no runner | Read branch, inspect state, produce advisory reviews; authorized bounded repository updates | No CI compute required; no arbitrary code execution or test proof |
| Browser editor, no runner | Inspect/edit files and commit through authorized UI | github.dev has no build terminal; do not claim tests run |
| Codespaces, no Actions runner | Browser-accessible shell/VM for CLI and tests | Personal included compute/storage allowance; enforce quota, stop idle work |
| Local direct shell, no Actions runner | Git, CLI, local tests, stdio MCP | Requires hardware; isolate credentials; record reproducible environment |
| Alternative cloud sandbox/VM/CI, no GitHub Actions runner | Authorized compatible commands, builds and tests | Verify provider terms, privacy, runtime, costs and access before selection |
| Hosted MCP/API, no Actions runner | Scoped context and service-native operations | Verify host support, authentication, isolation and actual operation limits |

A connector-only host can use Layer 1 + 2 to inspect VIB and its current handoff, Layer 1 + 3 to guide a documentation review, or update authorized metadata through the API with safe concurrency and readback. BART's geometry generation needs real compatible compute; a connector cannot pretend to run Blender. An advisory review can finish with no execution, but tests remain not run.

## Universal safety
Use minimum sufficient privileges, explicit repository and operation scope, trusted source pins and read-only defaults. Do not equate a safe environment with unrestricted permissions. Keep private data, tokens, logs and artifacts out of public jobs. Public/private is separate from paid/free; free quotas and account eligibility vary. Verify current billing and use spending controls before work. Never promise unlimited free private computation or free inference.

Workflow dispatch availability and branch restrictions must be checked; never silently add a default-branch workflow. Retain evidence durably and identify source, actual checkout, environment, commands and outcomes. Distinguish metadata checks from real executed tests.

Official sources: [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions), [runner selection](https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job), [secure use](https://docs.github.com/en/actions/reference/security/secure-use), [Codespaces usage](https://docs.github.com/en/codespaces/troubleshooting/troubleshooting-included-usage), [github.dev](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor), [REST contents](https://docs.github.com/en/rest/repos/contents).
