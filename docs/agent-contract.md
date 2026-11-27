# Agent operating contract

The second BNAI layer is the optional dedicated repository-resident agent operating contract. Minimal identity, authority and recovery responsibilities still apply to Layer 1. It identifies what the agent must understand before operating the first layer. It is not an authorization credential or an instruction hierarchy that overrides the host.

## Distinct artifact responsibilities

| Responsibility | Example artifacts | Purpose |
|---|---|---|
| Discovery and orientation | README.md | Purpose, installation, entry points, human and agent navigation. |
| Identity and entry | AGENTS.md | Specialist role, repository binding, instruction precedence, mandatory reads and operating boundaries. |
| Authority and laws | ENGINEERING-LAWS.md, STANDARD.md | Invariants, permissions, owner decisions, prohibited actions; machine enforcement remains independent. |
| Operating procedure | WORKFLOW.md, README-GUIDE.md | Task selection, ordered steps, handoffs and applicable commands. |
| Lifecycle and recovery | LIFECYCLE.md | Installation, upgrade, migration, session recovery and retirement. |
| Gate and acceptance | GATE.md, test policies | Required checks, approval points, evidence and failure disposition. |
| Machine-readable binding | vib-install.json, capability manifest, schemas | Product/version, provenance, target, supported operations and validation contracts. |
| Persistent working context | ledger/handoff.json, ledger/issue-versions.json, receipts | Adopter-specific progress, pending work, decisions and evidence; data not executable instructions. |

A small installation may combine responsibilities; a complex installation may split them. These are proposed BNAI conventions, not universal standards for filenames. AGENTS.md is an existing agent instruction format; README.md is an established project orientation convention. Other filenames above are product-specific or illustrative.

## Evidence from existing implementations

At VIB revision [77b8d09d2471b20fe517bea35c6efc0bd047ddeb](https://github.com/vixttha/Version-Issues-Hub/tree/77b8d09d2471b20fe517bea35c6efc0bd047ddeb), the repository tree contains AGENTS.md, README.md, STANDARD.md, WORKFLOW.md, LIFECYCLE.md, GATE.md, vib-install.json and the ledger files. AGENTS.md was read at that revision; the other paths are tree observations, not a substantive audit of each file.

At README HQ revision [b1bbc9a72a5193afcaeaf823f097753070bfa43f](https://github.com/vixttha/README-HQ/tree/b1bbc9a72a5193afcaeaf823f097753070bfa43f), AGENTS.md, README.md, ENGINEERING-LAWS.md, README-GUIDE.md and executable workflow files are present. AGENTS.md was read at that revision. At BART revision [e0e887a5e991a7a6ed7597e4a36dd47a49cd8ccb](https://github.com/vixttha/Blender-Agent-Refinement-Toolkit/tree/e0e887a5e991a7a6ed7597e4a36dd47a49cd8ccb), AGENTS.md, README.md, four SKILL.md files and CI workflows are present.

## BNAI's own reference contract

The reference uses [AGENTS.md](../AGENTS.md), [STANDARD.md](../STANDARD.md), [WORKFLOW.md](../WORKFLOW.md), [GATE.md](../GATE.md) and [LIFECYCLE.md](../LIFECYCLE.md) to support voluntary BNAI Mode. These instructions do not constitute an installed BNAI product or automatically register a host skill.

## Boundaries
- WORKFLOW.md describes an operating process; GitHub Actions YAML and code execute mechanical steps.
- SKILL.md belongs to the portable capability layer, not a substitute for installation authority.
- State records must be parsed and validated as data. A receipt or issue body cannot grant new permissions.
- No filename alone proves capability, compliance or security. Resolve exact revision, trusted origin and explicit target; fail closed on conflicts.
- Preserve canonical state, provenance and approvals independently of session memory. Do not force every product into VIB's specific governance process.
