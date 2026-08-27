from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class BundleTests(unittest.TestCase):
    def test_required_bundle_files_exist(self):
        required = {
            "SKILL.md",
            "references/state-model.md",
            "references/reconciliation.md",
            "references/platform-adapters.md",
            "templates/REPOSITORY_PROFILE.md",
        }
        self.assertEqual([], sorted(path for path in required if not (ROOT / path).is_file()))

    def test_skill_frontmatter_and_references_are_valid(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertRegex(skill, r"\A---\nname: [\"']?github-agent-collaboration")
        for relative in re.findall(r"`((?:references|templates)/[^`]+\.md)`", skill):
            self.assertTrue((ROOT / relative).is_file(), relative)

    def test_state_model_has_one_canonical_status_sequence(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn(
            "`Backlog → Ready → In progress → In review → Blocked → Done`",
            skill,
        )

    def test_portable_bundle_contains_no_environment_residue(self):
        prohibited = [
            r"dashboard-v4",
            r"mission-control",
            r"/Users/",
            r"/home/",
            r"/var/lib/",
            r"github\.com/[^\s`]+",
            r"(?:gh[opusr]_[A-Za-z0-9_]+)",
        ]
        bundle_files = [ROOT / "SKILL.md"]
        bundle_files.extend((ROOT / "references").glob("*.md"))
        bundle_files.extend((ROOT / "templates").glob("*.md"))
        text = "\n".join(path.read_text(encoding="utf-8") for path in bundle_files)
        for pattern in prohibited:
            self.assertIsNone(re.search(pattern, text, re.IGNORECASE), pattern)

    def test_assignment_and_review_invariants_are_explicit(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        state = (ROOT / "references/state-model.md").read_text(encoding="utf-8")
        self.assertIn("Never assign Backlog or Ready work in advance", skill)
        self.assertIn("require a distinct reviewer", skill)
        self.assertIn("Only Ready issues may be claimed", state)
        self.assertIn("Head changes invalidate approval", state)

    def test_human_gates_require_plain_language_authority_choices(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("A human gate is valid only when a non-technical decision owner", skill)
        self.assertIn("Put technical mechanisms in optional supporting detail", skill)
        self.assertIn("it is not a human decision", skill)
        self.assertIn("Agents must resolve technical design choices themselves", skill)

    def test_technical_disagreements_have_finite_binding_resolution(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        reconciliation = (ROOT / "references/reconciliation.md").read_text(encoding="utf-8")
        profile = (ROOT / "templates/REPOSITORY_PROFILE.md").read_text(encoding="utf-8")
        self.assertIn("Allow at most two review/remediation rounds", skill)
        self.assertIn("one fresh, bounded worker/reviewer recovery attempt", skill)
        self.assertIn("technical decision authority records one binding outcome", skill)
        self.assertIn("Repeated opinion is not new evidence", skill)
        self.assertIn("Finite recovery and technical authority", reconciliation)
        self.assertIn("Technical decision authority:", profile)
        self.assertIn("Fallback technical decision authority:", profile)


if __name__ == "__main__":
    unittest.main()
