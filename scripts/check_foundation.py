"""Offline structural checks; not product qualification."""
import json
import pathlib
import re
import unittest
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
def validate_journeys(doc):
    """Check catalog shape, never claim behavioral execution."""
    headings = re.findall(r"^### (J\d{2}) — (.+)$", doc, re.M)
    expected = [f"J{i:02d}" for i in range(1, 16)]
    if [j for j, _ in headings] != expected or len({t for _, t in headings}) != 15:
        raise ValueError("expected ordered, unique J01–J15")
    blocks = re.split(r"^### J\d{2} — .+$", doc, flags=re.M)[1:]
    modes = {"reference", "agent", "adopter"}
    covered = set()
    for block in blocks:
        block = block.split("\n## Completion boundary", 1)[0]
        for label in ("Modes", "Fixture", "Procedure", "Assertions", "Negative cases", "Evidence", "Sources"):
            if len(re.findall(r"^\*\*" + label + r":\*\* \S.+$", block, re.M)) != 1:
                raise ValueError("missing or duplicate field: " + label)
        selected = re.search(r"^\*\*Modes:\*\* (.+)$", block, re.M).group(1).split(", ")
        if not set(selected) <= modes or len(selected) != len(set(selected)):
            raise ValueError("invalid modes")
        covered.update(selected)
        sources = re.search(r"^\*\*Sources:\*\* (.+)$", block, re.M).group(1)
        links = re.findall(r"\]\(([^)]+)\)", sources)
        if not links or any("://" in p or p.startswith("/") or not (ROOT / "docs" / p).is_file() or not (ROOT / "docs" / p).resolve().is_relative_to(ROOT) for p in links):
            raise ValueError("invalid local source")
    if covered != modes:
        raise ValueError("missing evidence mode")

def validate_trial_evidence(base, row, reference_receipts):
    """Check evidence shape, not authenticity or actual agent execution."""
    observed = row.get("observed")
    if not isinstance(observed, str) or not observed.strip():
        raise ValueError("missing observed outcome")
    paths = []
    for key in ("transcript", "activity_trace"):
        value = row.get(key)
        if not isinstance(value, str) or not value.strip() or pathlib.Path(value).is_absolute():
            raise ValueError("invalid evidence path: " + key)
        path = (base / value).resolve()
        if (not path.is_relative_to(base.resolve()) or not path.is_file()
                or path in reference_receipts or not path.read_bytes().strip()):
            raise ValueError("missing, empty or non-agent evidence: " + key)
        paths.append(path)
    if paths[0] == paths[1]:
        raise ValueError("transcript and activity trace must be distinct artifacts")


class FoundationTests(unittest.TestCase):
    def test_version(self):
        version = (ROOT / "VERSION").read_text().strip()
        self.assertRegex(version, r"^v(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2,}$")
        readme = (ROOT / "README.md").read_text()
        self.assertEqual(re.findall(r"^\*\*Specification:\*\* (v[0-9.]+)\s", readme, re.M), [version])
        changelog = (ROOT / "CHANGELOG.md").read_text()
        self.assertEqual(re.findall(r"^## (v[0-9.]+)\s", changelog, re.M)[0], version)
    def test_catalog(self):
        data = json.loads((ROOT / "examples/catalog.json").read_text())
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(data["foundation_version"], (ROOT / "VERSION").read_text().strip())
        entries = data["examples"]
        ids = {e["id"] for e in entries}
        self.assertEqual(len(entries), len(ids))
        self.assertEqual(ids, {"vib", "readme-hq", "veraphify", "lydite", "brand-identity", "provenistem", "bart", "converium"})
        for e in entries:
            self.assertRegex(e["sha"], r"^[0-9a-f]{40}$")
            self.assertEqual(e["url"], f"https://github.com/{e['repository']}/blob/{e['sha']}/{e['path']}")
            self.assertIn(e["classification"], {"observed-branch-pattern", "component-example", "ecosystem-index"})
            self.assertTrue(e["observation"].strip())
            self.assertIn(e["url"], (ROOT / "examples/README.md").read_text())
        self.assertEqual(next(e for e in entries if e["id"] == "converium")["classification"], "ecosystem-index")
    def test_architecture(self):
        arch = (ROOT / "docs/architecture.md").read_text()
        self.assertEqual(re.findall(r"^\| ([1-5])\.", arch, re.M), ["1", "2", "3", "4", "5"])
        self.assertIn("Agent operating contract", arch)
        contract = (ROOT / "docs/agent-contract.md").read_text()
        for name in ("README.md", "AGENTS.md", "WORKFLOW.md", "LIFECYCLE.md", "GATE.md", "STANDARD.md", "vib-install.json", "ledger/handoff.json"):
            self.assertIn(name, contract)
    def test_reference_contract(self):
        for p in ("AGENTS.md", "STANDARD.md", "WORKFLOW.md", "GATE.md", "LIFECYCLE.md", "LICENSE", "NOTICE.md", "CONTRIBUTING.md", "SECURITY.md"):
            self.assertTrue((ROOT / p).is_file(), p)
        self.assertIn("PolyForm Strict License 1.0.0", (ROOT / "LICENSE").read_text())
        self.assertIn("Head → Worker → Validate → Internal Auditor → Head", (ROOT / "WORKFLOW.md").read_text())
        self.assertIn("turn BNAI off", (ROOT / "AGENTS.md").read_text())
        self.assertIn("read-only", (ROOT / "AGENTS.md").read_text())
        self.assertEqual(len(list((ROOT / "docs/layers").glob("*.md"))), 5)
    def test_composition(self):
        doc = (ROOT / "docs/composition.md").read_text()
        combos = re.findall(r"^\| (1(?: \+ [2-5])*) \|", doc, re.M)
        expected = {" + ".join(map(str, [1] + [i for i in range(2, 6) if m & (1 << (i-2))])) for m in range(16)}
        self.assertEqual(len(combos), 16)
        self.assertEqual(set(combos), expected)
        pairs = re.findall(r"^\| ([1-5]) ↔ ([1-5]) \|", doc, re.M)
        self.assertEqual(len(pairs), 10)
        self.assertEqual(set(pairs), {(str(a), str(b)) for a in range(1, 6) for b in range(a+1, 6)})
    def test_documentation_strategy(self):
        data = json.loads((ROOT / "docs/documentation-strategy.json").read_text())
        self.assertEqual(data["source"]["commit"], "88feb6971d2f49c530535f09d0defb1e9e1808bf")
        self.assertEqual([s["number"] for s in data["sets"]], [1, 4, 9])
        for s in data["sets"]:
            self.assertEqual(len(s["techniques"]), 20)
            self.assertEqual(len({t["id"] for t in s["techniques"]}), 20)
            for t in s["techniques"]:
                self.assertTrue((ROOT / t["path"]).is_file(), t)
                self.assertIn(t["disposition"], {"applied", "adapted", "pending"})
                self.assertIn(t["id"], (ROOT / "docs/documentation-strategy.md").read_text())
        for route in ("docs/README.md", "AGENTS.md", "docs/composition.md", "LICENSE", "NOTICE.md"):
            self.assertIn(f"]({route})", (ROOT / "README.md").read_text())
        self.assertIn("Turn BNAI off", (ROOT / "README.md").read_text())
    def test_illustrative_receipt(self):
        base = ROOT / "docs/examples"
        schema = json.loads((base / "inspection-receipt.schema.json").read_text())
        receipt = json.loads((base / "inspection-receipt.json").read_text())
        self.assertEqual(set(receipt), set(schema["required"]))
        for field in ("reference_sha", "target_sha"):
            self.assertRegex(receipt[field], schema["properties"][field]["pattern"])
        self.assertEqual(receipt["operation"], schema["properties"]["operation"]["const"])
        self.assertIn(receipt["status"], schema["properties"]["status"]["enum"])
        self.assertTrue(all(isinstance(x, str) and x for x in receipt["findings"]))
    def test_qualification_journeys(self):
        doc = (ROOT / "docs/qualification-journeys.md").read_text()
        validate_journeys(doc)
        self.assertIn("Start all cases as not-run", doc)
        for path, link in (("README.md", "docs/qualification-journeys.md"), ("GATE.md", "docs/qualification-journeys.md"), ("docs/README.md", "qualification-journeys.md")):
            self.assertIn(f"]({link})", (ROOT / path).read_text())
    def test_qualification_journeys_reject_invalid_catalog(self):
        doc = (ROOT / "docs/qualification-journeys.md").read_text()
        for bad in (
            doc.replace("### J15 —", "### J14 —", 1),
            doc.replace("### J01 —", "### J16 —", 1),
            doc.replace("**Negative cases:**", "**Missing cases:**", 1),
            doc.replace("**Modes:** reference", "**Modes:** universal", 1),
            doc.replace("](definition.md)", "](missing-source.md)", 1),
        ):
            with self.subTest():
                with self.assertRaises(ValueError):
                    validate_journeys(bad)
    def test_maintainer_version_workflow(self):
        contract = (ROOT / "AGENTS.md").read_text()
        for required in ("Maintainer version workflow — VIB", "Verify the package source", "Do not merge the dedicated VIB branch into main", "one active Worker", "15 qualification journeys"):
            self.assertIn(required, contract)
        self.assertNotIn("Version-Issues-Hub", {p.name for p in ROOT.iterdir()})
        self.assertFalse((ROOT / "ledger").exists())
        self.assertFalse((ROOT / "vib-install.json").exists())
    def test_behavioral_trial_record(self):
        base = ROOT / "docs/qualification/v0.0.0.3.2"
        data = json.loads((base / "results.json").read_text())
        fixtures = json.loads((base / "fixtures.json").read_text())
        self.assertEqual(data["issue"], 6)
        self.assertEqual(data["version"], "v0.0.0.3.2")
        for key in ("reference_sha", "target_sha"):
            self.assertRegex(data[key], r"^[0-9a-f]{40}$")
        self.assertEqual([row["id"] for row in data["trials"]], [f"B{i:02d}" for i in range(1, 11)])
        self.assertEqual([row["id"] for row in fixtures["cases"]], [f"S{i}" for i in range(1, 8)])
        protocol = (base / "README.md").read_text()
        reference_receipts = {(base / row["receipt"]).resolve() for row in data["reference_observations"]}
        for row in data["trials"]:
            self.assertIn(f"### {row['id']} —", protocol)
            self.assertEqual(row["mode"], "agent")
            self.assertIn(row["result"], {"not-run", "blocked", "pass", "fail", "not-applicable"})
            if row["result"] in {"pass", "fail"}:
                validate_trial_evidence(base, row, reference_receipts)
            else:
                self.assertTrue(row["reason"])
        if data["behavioral_qualification"] == "pass":
            self.assertTrue(all(row["result"] == "pass" for row in data["trials"]))
        else:
            self.assertIn(data["behavioral_qualification"], {"blocked", "not-run", "fail"})
        for row in data["reference_observations"]:
            self.assertEqual(row["mode"], "reference")
            path = (base / row["receipt"]).resolve()
            self.assertTrue(path.is_relative_to(base.resolve()) and path.is_file())
    def test_behavioral_trial_evidence_reject_invalid(self):
        # Synthetic structural test inputs only; not behavioral receipts.
        with tempfile.TemporaryDirectory() as directory:
            base = pathlib.Path(directory)
            for name, content in (("transcript.txt", "synthetic transcript marker"),
                                  ("trace.txt", "synthetic trace marker"),
                                  ("reference.txt", "synthetic reference marker"),
                                  ("empty.txt", "  ")):
                (base / name).write_text(content)
            reference_receipts = {(base / "reference.txt").resolve()}
            row = {"observed": "synthetic outcome", "transcript": "transcript.txt",
                   "activity_trace": "trace.txt"}
            validate_trial_evidence(base, row, reference_receipts)
            for override in (
                {"observed": "  "},
                {"observed": 1},
                {"activity_trace": "transcript.txt"},
                {"activity_trace": "./transcript.txt"},
                {"activity_trace": "empty.txt"},
                {"activity_trace": "missing.txt"},
                {"activity_trace": "reference.txt"},
                {"transcript": "reference.txt"},
                {"activity_trace": "../trace.txt"},
                {"activity_trace": str(base / "trace.txt")},
                {"activity_trace": None},
            ):
                with self.subTest(override=override):
                    with self.assertRaises(ValueError):
                        validate_trial_evidence(base, {**row, **override}, reference_receipts)
    def test_local_links(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" not in target and not target.startswith("#"):
                    name, _, anchor = target.partition("#")
                    dest = path.parent / name
                    self.assertTrue(dest.exists(), f"{path}: {target}")
                    if anchor and dest.suffix == ".md":
                        headings = re.findall(r"^#{1,6} (.+)$", dest.read_text(), re.M)
                        slugs = [re.sub(r"[^\w\- ]", "", h.lower()).replace(" ", "-") for h in headings]
                        self.assertIn(anchor, slugs, f"{path}: {target}")
if __name__ == "__main__":
    unittest.main(verbosity=2)
