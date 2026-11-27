# Persistent infrastructure lifecycle

This guide applies to adopter installations, not BNAI itself. Source packages, adopter state and this reference have separate identities. Consult [version history](../CHANGELOG.md) and [VERSION](../VERSION); pin the reference and product documentation to the exact applicable commit, not simply latest main. Read [Layer 1](layers/01-persistent-branch.md) for installation and [composition](composition.md) for optional interfaces.

## Upgrade preflight
Confirm owner scope, current source SHA, current adopter state SHA, target branch, incoming package SHA, schema compatibility, license and collision risks. List files and data that change or remain. Preserve a verified recovery reference before writing. If the product has not established compatible saved-data versions or migration behavior, stop and qualify them with synthetic data; BNAI has no universal compatibility guarantee.

## Repeated operations and uncertain writes
Read-only inspection may be repeated against the same revision. Mutations must define whether repetition converges, resumes or creates a new record. For ambiguous responses, read back the actual state and reconcile the request receipt before retrying. Reject stale revisions; do not use a check-then-write sequence as a claim of atomicity. Prefer explicit expected revision guards and serialized or atomic operations where available.

## Restore into an isolated destination
Illustrative protocol, not an executed restore: freeze writers or take a consistent snapshot; record the source revision, manifest and relevant digests; restore to an authorized separate disposable branch or environment; compare state, schema, digests and representative read-only operations. Only then propose owner-approved recovery into the real target. Retain the original until the restore is independently qualified. Never publish private data to obtain a free runner.

## Retirement and archive handoff
Freeze writes and preserve source, adopter records, evidence and recovery instructions. Document what removal affects (branch, credentials, integrations) and what remains (state, backups and receipts); obtain separate authorization before removal. If archived, place a successor link or explicit no-successor notice, last verified revision and unresolved work at the top of its README. This is a recommended handoff pattern, not an assertion that BNAI or an example is archived.

[Layer guides](README.md) · [Authority and acceptance](../GATE.md).
