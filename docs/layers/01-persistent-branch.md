# Layer 1 — Persistent branch infrastructure

Purpose: reusable, long-lived project-local engineering workspace. Includes implementation or authorized mechanical procedures, installation metadata, adopter-owned state, tests and durable evidence. The branch is not the product's ordinary feature branch.

## How to create one
1. Define the capability, authorized target, minimal commands or procedures, source version, license/notice and evidence criteria. Separate reusable package from adopter records.
2. Inspect the existing repository and refs. Choose a dedicated long-lived name with owner approval; never overwrite a collision or merge a template workspace wholesale into product source. Create from an approved empty or existing baseline using a safe branch procedure. Do not make unrelated changes to main.
3. Populate reviewed source files only. Initialize empty adopter data rather than copy another project's state. Record source commit/package identity, target repo/branch, schema and compatibility, and where instructions and state live. Provide a minimal discoverable entry point even without a dedicated Layer 2.
4. Define a bounded operation path (authorized repository API, optional CLI, optional MCP, or another approved interface). Validate targets and input, minimize privileges, isolate secrets, and specify errors and recovery. Source and state revisions are distinct.
5. Establish tests and receipts. Pin exact input revision, operation, environment, run/attempt where available, outcome and durable artifact digest. Retain required evidence before ephemeral artifact expiry. Never report execution that did not occur.
6. Qualify in an isolated authorized repository with synthetic fixtures: fresh-session discovery, state recovery, read-only use, authorized write, denied write, stale/concurrent update, interruption, upgrade and recovery. Use public standard GitHub-hosted CI by default for reference qualification; document alternatives.
7. Adopt and maintain only after owner review. Use non-force changes, expected revision guards and serialization or atomic conditional transactions where supported. A check followed by a write is not atomic. Read back actual state after ambiguous results; never retry blindly.
8. Upgrade by comparing package revisions and collision risks, preserving adopter data and prior receipts. Retire by freezing writers, retaining exact Git/archive references and evidence, then separately authorizing any deletion.

## Illustrative layout
```text
dedicated-tool-branch/
  README.md
  install-manifest.json
  implementation/
  state/
  tests/
  evidence/
```
Names are examples, not mandatory. A small installation can use other layouts with equivalent responsibilities. The [VIB branch](https://github.com/vixttha/Version-Issues-Hub/tree/77b8d09d2471b20fe517bea35c6efc0bd047ddeb) is source evidence of a more specialized layout, not a certification.

## Interaction with other layers
With Layer 2, load the operating contract from the pinned branch. With Layer 3, have skills resolve the correct installation. With Layer 4, bind CLI calls to exact target/revision. With Layer 5, expose scoped context and operations via MCP. No additional layer is required merely because Layer 1 exists. See [all pairwise interfaces](../composition.md) and [execution options](../execution.md).

## Acceptance
Verify no unrelated state leaked; source and target identities match; applicable tests prove the actual operations; owner authority is maintained; recovery can identify the last verified state. Record any missing capability as unqualified, not passed.

## Related reference
[Guide index](../README.md) · [Composition and interfaces](../composition.md) · [Lifecycle and recovery](../lifecycle-guide.md) · [Illustrative receipt](../interface-example.md). Apply only the selected layers and qualify the actual product, not this example.
