"""Offline structural checks; not product qualification."""
import json
import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
class FoundationTests(unittest.TestCase):
    def test_version(self):
        self.assertEqual((ROOT / "VERSION").read_text().strip(), "v0.0.0.2")
        for path in ("README.md", "CHANGELOG.md"):
            self.assertIn("v0.0.0.2", (ROOT / path).read_text())
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
    def test_local_links(self):
        for path in ROOT.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent / target.split("#", 1)[0]).exists(), f"{path}: {target}")
if __name__ == "__main__":
    unittest.main(verbosity=2)
