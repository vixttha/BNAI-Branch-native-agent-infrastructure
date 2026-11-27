# Review and acceptance gates

A BNAI report is complete only when scope and exact target/reference revision are known (or explicitly blocked), findings cite evidence, untested assumptions are marked, optional layers are not treated as mandatory, and permissions/privacy are reviewed. Failed or missing checks return to Worker or are recorded as limitations. Source inspection is not execution proof.

For reference repository changes: review exact candidate, require passing applicable standard public GitHub-hosted structural CI, inspect changed scope, obtain owner approval before merge or formal release, and verify the actual main revision and post-merge checks. Report independent audit only when actually performed. No claim that this advisory document or CI mechanically blocks merges; no new branch protection is required.

Use the [reference qualification journeys](docs/qualification-journeys.md) for applicable scenario coverage. Record specification, agent and adopter results separately; the catalog itself and its structural checks do not establish successful journey execution. No new mandatory runtime or service is required.

For VIB-managed maintenance, require an actual compatible installed-branch assignment and exact handoff evidence; never label a candidate VIB-managed from documentation alone. Until [the version compatibility issue](https://github.com/vixttha/BNAI-Branch-native-agent-infrastructure/issues/5) is resolved, record the blocker and obtain explicit owner direction for any alternate workflow. The current v0.0.0.3.1 candidate is not assigned in VIB.
