# Source observation — reference mode only

Reference: [BNAI v0.0.0.3.1](https://github.com/vixttha/BNAI-Branch-native-agent-infrastructure/tree/c02cc120185d356dc753cdce508918144d90fcdc). Target: [VIB dedicated branch](https://github.com/vixttha/Version-Issues-Hub/tree/77b8d09d2471b20fe517bea35c6efc0bd047ddeb) (state SHA 77b8d09d2471b20fe517bea35c6efc0bd047ddeb). Actual actions in the current maintainer ChatGPT conversation: read GitHub main/target refs, read pinned documents, inspect full non-truncated target tree, read manifest and ledger schemas, and reread target ref. The source inspection used only connector reads against VIB. The target ref before and after was 77b8d09d2471b20fe517bea35c6efc0bd047ddeb; no VIB write tools were called for this inspection. The connector is not proven to be technically read-only. This is a manual record of actual connector responses, not an exported authenticated activity trace. Host: ChatGPT current conversation; model label GPT-6.2, exact runtime build unavailable. Same-agent source review; no fresh-session, independent agent or cross-harness qualification.

## R01 — J01 reference decision review

Reviewed [composition](https://github.com/vixttha/BNAI-Branch-native-agent-infrastructure/blob/c02cc120185d356dc753cdce508918144d90fcdc/docs/composition.md), [architecture](https://github.com/vixttha/BNAI-Branch-native-agent-infrastructure/blob/c02cc120185d356dc753cdce508918144d90fcdc/docs/architecture.md), [execution](https://github.com/vixttha/BNAI-Branch-native-agent-infrastructure/blob/c02cc120185d356dc753cdce508918144d90fcdc/docs/execution.md) and [Layer 1](https://github.com/vixttha/BNAI-Branch-native-agent-infrastructure/blob/c02cc120185d356dc753cdce508918144d90fcdc/docs/layers/01-persistent-branch.md). The documented combinations match the following bounded decisions; these are scenario reasoning, not installed implementations.

| Task | Smallest suitable documented composition | Required condition |
|---|---|---|
| Inspect state | 1 | Authorized repository reads; no runner or execution claim |
| Portable specialist guidance | 1 + 3 | Compatible skill host; no mandatory CLI or MCP |
| Repeated mechanical work governed by a contract | 1 + 2 + 4 | Compatible execution environment and CLI |
| Expose bounded host tools | 1 + 5 | Compatible transport and authorization |
| Instructions on short-lived branch only | Not full BNAI | Durable substrate and minimum recoverability missing |
| Compute-heavy operation on connector only | Block execution | Real compatible compute required |
| Dedicated branch missing essential authority/state | Not qualified | Establish minimum identity, authority, state and evidence |

Result: source-level decision consistency reviewed; no agent trial or implementation run.

## R02 — VIB source inspection

| Actual source read | Git blob SHA | Observation |
|---|---|---|
| [AGENTS.md](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/AGENTS.md) | 1e30ba7629635d7267ec6f062187e78df584eabf | Explicit installed branch, scope, workflow and owner authority |
| [vib-install.json](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/vib-install.json) | c0d6c1edb04619d54861ebaf1cbfdaf1c6b11a0b | Target identity matches VIB; separate source SHA c7a4995c99fed8d1e87970a744c4cde378ebed1e, enforcement disabled in manifest |
| [WORKFLOW.md](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/WORKFLOW.md) | 8282f5b61dea3c776cc2f58a4be0a564f33c487e | Sequential handoff and connector-only option |
| [STANDARD.md](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/STANDARD.md) | a7565a8c6bccb54d9c18481482d7cd79aede43e6 | Distinguishes evidence metadata from actual execution |
| [tools/session.py](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/tools/session.py) | c22cac7292f4f54ba863779deb6b1321abdd48f3 | Source contains CLI entry point, inspect, target and expected-SHA arguments |
| [ledger/issue-versions.json](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/ledger/issue-versions.json) | 2275b17d7bd50604daf360767860a21736c0a6d0 | Schema v1, repository matched; no ledger contents reproduced |
| [ledger/handoff.json](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/ledger/handoff.json) | f2732641662d6d7a081ffeead91f26d39f0e368e | Schema v1 active/history keys observed; no records reproduced |
| [README.md](https://github.com/vixttha/Version-Issues-Hub/blob/77b8d09d2471b20fe517bea35c6efc0bd047ddeb/README.md) | b94553fae7bd487c7a843aadcaf339ea2ecf46e6 | Dedicated branch documentation and documented inspect command |

Observed composition 1 + 2 + 4 at source level: dedicated branch/manifest/state paths, explicit operating contract, CLI source. No dedicated skill or MCP interface was established by this inspected tree; external capabilities are unknown and their absence is not a defect. For the requested inspection, connector-only read access is sufficient. No CLI invocation, installation, package-integrity requalification, authorization enforcement trial, agent activation/deactivation test or runtime verification occurred. Source package pin is a manifest claim, not separately verified here.

## Review boundary

The observed reads and stable target ref support only this reference observation. No full tool transcript exported, no isolated fresh session, no actual denied write or stale live ref trial, no private data published, no independent review. This does not satisfy issue #6 behavioral acceptance; the next action is the controlled real session described in the [protocol](../README.md).
