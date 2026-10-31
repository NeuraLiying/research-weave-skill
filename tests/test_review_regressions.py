"""Regression cases derived from the independent review; all study data are fictional."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_evidence import MODULE, ROOT, fixture
from fuzz_evidence import mutate


class ReviewRegressions(unittest.TestCase):
    def detected(self, data, error=True):
        errors, cautions = MODULE.check(data)
        self.assertTrue(errors if error else errors or cautions, (errors, cautions))

    def test_duplicate_source_cannot_be_relabeled_independent(self):
        data = fixture()
        data["papers"][1].update(title=data["papers"][0]["title"], url=data["papers"][0]["url"])
        self.detected(data)

    def test_canonical_doi_duplicates(self):
        data = fixture()
        data["papers"][0]["url"] = "http://dx.doi.org/10.123/ABC#table1"
        data["papers"][1]["url"] = "https://doi.org/10.123/abc?utm_source=test"
        self.detected(data)

    def test_different_versions_preserve_history(self):
        data = fixture()
        data["papers"][1].update(url=data["papers"][0]["url"], version="2")
        self.assertFalse(MODULE.check(data)[0])

    def test_analogy_is_context_not_direct_support(self):
        data = fixture()
        data["claims"][1]["uses"][0]["role"] = "analogy"
        self.detected(data)

    def test_contested_needs_counterevidence(self):
        data = fixture()
        data["propositions"][0]["synthesis"] = "contested"
        self.detected(data)

    def test_convergent_needs_declared_independent_contributions(self):
        for count in [0, 1, None]:
            with self.subTest(count=count):
                data = fixture()
                data["propositions"][0]["independent_evidence_count"] = count
                self.detected(data)

    def test_source_supported_edge_cannot_hide_abstract_endpoint(self):
        data = fixture()
        data["papers"].append(dict(id="P3", title="Abstract-only", url="local:P3", version="1", access="abstract", evidence_family="F3"))
        claim = copy.deepcopy(data["claims"][0]); claim.update(id="C3", paper_id="P3")
        claim["assessment"]["strength"] = "provisional"; data["claims"].append(claim)
        data["edges"].append(dict(id="E2", source="C3", target="C1", relation="supports", status="source_supported", evidence_claims=["C1"], rationale="Test provenance", independence="unknown"))
        self.detected(data)

    def test_conflict_requires_supported_claims(self):
        data = fixture()
        for claim in data["claims"]:
            claim["assessment"]["strength"] = "provisional"
        data["propositions"] = []; data["edges"] = []
        data["tensions"] = [dict(id="T1", claim_ids=["C1", "C2"], classification="comparable_conflict", comparison="Nominally aligned", explanation="Opposing findings", resolution_search="Corpus only", alternatives=["sampling", "implementation"], test=dict(variable="protocol", controls="paired tasks", predictions="different outcomes", gap_killer="bug explains result"))]
        self.detected(data)

    def test_not_opposed_is_not_a_contradiction_frontier(self):
        data = fixture()
        data["tensions"] = [dict(id="T1", claim_ids=["C1", "C2"], classification="not_opposed", comparison="Compatible", explanation="Same finding", resolution_search="Corpus only", frontier_candidate=True, alternatives=["a", "b"], test=dict(variable="v", controls="c", predictions="p", gap_killer="g"))]
        self.detected(data)

    def test_claim_memberships_disjoint(self):
        for field in ["candidate_claim_ids", "uncertain_claim_ids", "context_claim_ids"]:
            data = fixture(); data["propositions"][0][field] = ["C1"]
            self.detected(data)

    def test_superseded_result_not_current_support(self):
        data = fixture()
        data["edges"].append(dict(id="E2", source="C2", target="C1", relation="supersedes", status="source_supported", evidence_claims=["C2"], rationale="Erratum removes gain", source_locator="P2 Erratum", independence="shared"))
        self.detected(data)

    def test_unknown_field_and_unlogged_sources_are_visible(self):
        data = fixture(); data["propositions"][0]["independant_replication_count"] = 3
        data["searches"][0]["kept_ids"] = []
        errors, cautions = MODULE.check(data)
        self.assertFalse(errors); self.assertTrue(any("unknown field" in x for x in cautions))
        self.assertTrue(any("absent from search" in x for x in cautions))

    def test_relationship_needs_its_own_provenance(self):
        data = fixture(); data["edges"][0].pop("source_locator")
        errors, cautions = MODULE.check(data)
        self.assertFalse(errors); self.assertTrue(any("relationship" in x for x in cautions))

    def test_search_not_after_snapshot(self):
        data = fixture(); data["searches"][0]["date"] = "2030-01-01"
        self.detected(data)

    def test_access_type_error_is_reported_in_cli(self):
        for access in [["fulltext"], {"access": "fulltext"}]:
            data = fixture(); data["papers"][0]["access"] = access
            with tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / "bad.json"; path.write_text(json.dumps(data))
                result = subprocess.run([sys.executable, str(ROOT / "skills/research-weave/scripts/check_evidence.py"), str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("ERROR:", result.stdout); self.assertNotIn("Traceback", result.stderr)

    def test_refutation_and_uncertain_interval_are_not_missing_evidence(self):
        for synthesis, field in [("refuted", "counter_claim_ids"), ("uninformative", "uncertain_claim_ids")]:
            data = fixture(); q = data["propositions"][0]
            q.update(synthesis=synthesis, supporting_claim_ids=[], independent_evidence_count=0)
            q[field] = ["C1"]; q["refutation_basis"] = "In-scope observation defeats the exact table-level assertion"
            self.assertFalse(MODULE.check(data)[0])

    def test_inherited_risk_is_visible_without_automatically_rejecting_result(self):
        data = fixture(); data["claims"][1]["inherited_threats"] = ["C1"]
        errors, cautions = MODULE.check(data)
        self.assertFalse(errors); self.assertTrue(any("inherited" in x for x in cautions))

    def test_numeric_interval_preserves_uncertainty_and_rejects_bad_bounds(self):
        data = fixture()
        estimate = dict(effect=2, ci_low=-3, ci_high=7, null_value=0, unit="percent")
        data["claims"][0]["estimate"] = estimate
        self.assertFalse(MODULE.check(data)[0])
        for change in [dict(ci_low=8), dict(effect=float("inf")), dict(null_value=True)]:
            bad = copy.deepcopy(data); bad["claims"][0]["estimate"].update(change)
            self.detected(bad)
        # Arbitrarily large JSON integers are finite and must not crash math.isfinite.
        estimate["effect"] = 10 ** 400
        self.assertFalse(MODULE.check(data)[0])

    def test_opposing_uncertain_points_do_not_silently_establish_conflict(self):
        data = fixture(); data["edges"] = []
        for claim, effect in zip(data["claims"], [2, -1]):
            claim["estimate"] = dict(effect=effect, ci_low=-4, ci_high=7, null_value=0, unit="percent")
        data["tensions"] = [dict(id="T1", claim_ids=["C1", "C2"], classification="comparable_conflict", comparison="Aligned nominal protocol", explanation="Opposing point estimates", resolution_search="No paired comparison supplied", alternatives=["noise", "protocol"], test=dict(variable="paired difference", controls="same tasks", predictions="interval separates effects", gap_killer="no meaningful difference"))]
        errors, cautions = MODULE.check(data)
        self.assertFalse(errors); self.assertTrue(any("point estimates alone" in x for x in cautions))

    def test_shared_metadata_cautions_on_claimed_independence(self):
        data = fixture()
        for paper in data["papers"]:
            paper.update(authors=["Lab A"], datasets=["Shared test"], code_urls=["https://example.org/code"])
        errors, cautions = MODULE.check(data)
        self.assertFalse(errors); self.assertTrue(any("share" in x for x in cautions))

    def test_saturation_requires_real_unchanged_rounds(self):
        data = fixture(); data["context"]["stop_basis"] = "decision_saturation"
        self.detected(data)
        data["searches"][0].update(round=1, changed=[])
        data["searches"].append(dict(data["searches"][0], round=2))
        self.assertFalse(MODULE.check(data)[0])
        data["searches"][-1]["changed"] = ["queue:P1"]
        self.detected(data)

    def test_compact_reference_example_is_usable(self):
        reference = (ROOT / "skills/research-weave/references/scout-format.md").read_text()
        example = reference.split("```json\n", 1)[1].split("```", 1)[0]
        self.assertEqual(MODULE.check(json.loads(example)), ([], []))

    def test_scout_can_omit_full_network(self):
        data = fixture(); data.update(schema_version=2, profile="scout")
        for key in ["propositions", "edges", "tensions", "searches"]:
            data.pop(key)
        for claim in data["claims"]:
            claim["evidence"].pop("authors_interpretation"); claim["evidence"].pop("analyst_inference")
        self.assertEqual(MODULE.check(data), ([], []))

    def test_main_claim_coverage_and_budget(self):
        data = fixture(); data["papers"][0].pop("main_claim_ids")
        self.detected(data, error=False)
        data["context"]["deep_read_budget"] = 0; data["reading_queue"][0]["action"] = "deep_read"
        self.detected(data)

    def test_seeded_json_mutations_do_not_crash(self):
        mutate(fixture(), count=2000, seed=0)
