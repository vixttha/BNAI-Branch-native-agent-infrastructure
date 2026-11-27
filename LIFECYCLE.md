# Reference lifecycle

Start and stop BNAI Mode using [AGENTS.md](AGENTS.md). Re-resolve reference main to an exact revision per new review; preserve older references when comparing results. Read target revisions independently. When reference or target changes during a review, identify affected findings and refresh only those.

For adopters, follow the [Layer 1 installation and lifecycle guide](docs/layers/01-persistent-branch.md). Do not install BNAI itself as a prerequisite. This reference maintains a version file, changelog, reviewed main, historical Git commits and pinned source examples; no operational adopter ledger.

Candidate changes live on separate review branches. Merge and release require owner approval. Preserve prior valid license grants, evidence and history; no force updates or silent deletion.
