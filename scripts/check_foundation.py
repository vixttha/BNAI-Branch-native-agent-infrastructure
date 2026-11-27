"""Offline structural checks; not product qualification."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
class FoundationTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "v0.0.0.3")
        for path in ("README.md", "CHANGELOG.md"):
            self.assertIn("v0.0.0.3", (ROOT / path).read_text())
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
