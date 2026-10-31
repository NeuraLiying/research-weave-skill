# Run notes

This run followed the revised Research Weave skill for an offline, fictional supplied-corpus Scout. All deliverables are under `.`; the skill and repository were not modified. No network retrieval, other reports, tests, run artifacts or evaluator conclusions were consulted.

Resources opened:

- `../../../skills/research-weave/SKILL.md` — workflow and proportional Scout instructions.
- `../../../skills/research-weave/references/scout-format.md` — required exact saved-Scout field names and enums.
- `../../../evals/fixtures/speculative-decoding.md` — entire supplied primary excerpt/abstract corpus.
- `../../../skills/research-weave/references/contradictions.md` — consulted for the consequential unresolved throughput question, scope/precision alignment, alternative explanations and a separating diagnostic. No rich tension/graph objects were needed.
- `../../../skills/research-weave/scripts/check_evidence.py` — executed once on this run's ledger; checker source and tests were not inspected.
- This run's own `report.md` and `evidence.json` — read for report length, ledger counts and validation. No pre-existing run outputs were read.

Workflow/format friction:

- The compact contract made a seven-record/eight-claim ledger possible without proposition or edge scaffolding. Distinct empirical result families and shared provenance still need explanatory strings; they do not encode statistical independence by themselves.
- The skill says to capture a main claim and decisive result/proof locations, but this packet supplies only excerpts. P6 has a conceptual assertion without its proof; P7 has only a headline. Both are preserved as provisional with inaccessible decisive locations stated explicitly. Other main results are captured before secondary limitations.
- The v1 result remains as a superseded historical observation, while the correction and timing defect are separate claims. `assessment.strength: supported` for the old record means the historical report was inspected; `status: superseded` prevents adopting its old gain as current support.
- P4 is the second deep-read recommendation because it tests a strong fixed comparator and an inconvenient boundary, despite its code/chat scope mismatch. P3 is retained as a targeted near-match, with its main positive result preserved and a possible inherited timing defect explicitly unconfirmed.
- Exactness is a mandatory user condition with no supplied proof; it is treated as a validation gate rather than invented evidence. The worthwhile gain threshold is left as a preregistered decision variable because no engineering cost threshold was provided.

Validation:

`python3 ../../../skills/research-weave/scripts/check_evidence.py ./evidence.json`

Result: `0 error(s), 0 caution(s). Declared provenance checked; source meaning and independence not certified.` The checker was run once, with no subsequent ledger edits. The report has 607 whitespace-delimited words; the ledger has seven source records, eight claims and exactly two deep-read recommendations.

Semantic reread: reopened P2 and P4 behind the decision and top priorities, P3 behind the positive dependent near-match, and P1 as the deferred same-setting near-match. Also reopened P6 and P7 to check analogy/access limits. The earlier +9% remains superseded; P2's interval remains direct uncertain evidence; P4's local negative point estimate and broad author conclusion are separated. P3's timing vulnerability is a specific unconfirmed inherited risk, not a declared defect. No comparable conflict is claimed. No numerical sample count was inferred from dataset names. Unresolved source questions remain the missing exactness proofs, full timing implementations, interval methods, traffic equivalence and independent target-setting replication; structural success does not resolve them.
