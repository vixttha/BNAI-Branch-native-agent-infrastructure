# BNAI review workflow

Head → Worker → Validate → Internal Auditor → Head. Use one bounded lane. A role transition is not a separate agent process; disclose whether an independent agent actually reviewed the work.

| Stage | Responsibility | Exit evidence |
|---|---|---|
| 1 Head | Pin reference and target revisions, resolve owner scope, choose read-only or explicitly approved work, define observable criteria | Scope and revision record |
| 2 Worker | Inventory the target; map observed artifacts to layers and interfaces; recommend smallest composition; implement only separately authorized changes | Pinned file/operation observations, findings |
| 3 Validate | Check against layer guides, laws and requested criteria; run tests only within authority and suitable execution environment | Exact checks, commands, results or explicit not-run reason |
| 4 Internal Auditor | Recheck scope, source accuracy, optional-layer assumptions, permissions, stale state, privacy and evidence; distinguish independent review from self-review | Findings, disagreements, evidence limitations |
| 5 Head | Reconcile results; present prioritized findings and decisions, stop or return to Worker on specific failures | Final report, residual limitations, owner decisions |

If target revision moves, re-pin and review affected observations. Never silently promote metadata or documentation to execution evidence. Stop on unclear authority, unsafe execution, missing provenance or ambiguous writes. No automatic follow-up mutations. An advisory report may be produced with no runner at all, as long as untested claims remain untested.

## Report shape

Reference SHA; target repository/ref/SHA; scope and mode; detected layers; requested vs observed composition; execution profile; findings and evidence; recommended changes; test and independent-review status; owner decisions required. Do not include private content in public reports.
