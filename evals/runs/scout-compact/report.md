# Scout: adaptive draft length for T‑7 chat

**Keep a tuned fixed gamma as the default. Spend the two deep reads on P2 and P4 before committing to adaptive-policy development.** The closest supplied result, P2, is +2% tokens/sec with a 95% interval of [−3%, +7%]; it supports uncertainty about a useful gain, not a finding of zero benefit. No supplied excerpt establishes preservation of the exact output distribution.

This is an offline exercise using invented publications. Target: T‑7 chat, batch 1, identical single-GPU resources across arms. P2 uses D‑1/CHAT‑500/G‑A; equivalence to the intended drafter, GPU and traffic is unconfirmed.

| Order | Paper | Action and decision-changing focus |
|---|---|---|
| 1 | **P2, corrected v2** | **deep_read** — Errata and corrected timing/result block: cache rebuilds, comparator selection, interval construction; inspect the algorithm’s exactness argument if available. Determines whether the closest-match benefit survives complete costing. |
| 2 | **P4, When Fixed Is Enough** | **deep_read** — Main result and v1-policy reimplementation: fixed-gamma tuning, acceptance regime, timing parity and correctness. Tests when adaptation adds enough value to justify complexity. |
| 3 | P3, Dynamic Drafting at Scale | targeted_read — Main +11% result, timing code and v2 correction provenance. Could strengthen motivation if the gain transfers to T‑7/G‑A and the inherited timing risk is excluded. |
| 4 | P7, Speculation Under Load | verify_access — Obtain methods/results before using the “up to 2x” claim; baseline, metric and serving conditions are unknown. |
| 5 | P1, original v1 | defer — Historical implementation/correction comparison only; its +9% result is superseded. |
| 6 | P6, sequential testing | defer — Constant-cost sample-count theory offers an analogy; no wall-clock decoding or exactness evidence. |
| 7 | P5, survey | defer — Repeats stale +9% and P3’s +11%; no additional experimental evidence. |

**What the evidence establishes.** P2 replaces P1’s +9%, which omitted adaptive-arm cache rebuild time. Its fixed gamma was selected on the evaluation set; a clean held-out comparison remains necessary. P3’s +11% [6%, 16%] is a real result within the supplied excerpt’s T‑9/G‑B scope, with a dev-tuned baseline, but shares Kappa authorship, code and CHAT‑500 with P1/P2. A carried-over timing defect is possible, not established. P4’s −1% [−4%, +2%] concerns high-acceptance code completion and a reimplementation from v1. It neither proves universal failure nor directly contradicts P2: the settings differ and the intervals overlap. P5 supplies no independent replication. P7 is provisional.

**What would change the decision.** First require an inspected argument that adaptive gamma selection and rejection/verification preserve the target conditional distribution. Output comparisons can detect bugs but cannot establish exactness by themselves. None of this packet supplies that argument.

Then compare adaptive with a dev-tuned fixed gamma on untouched, representative T‑7 chat, using identical drafter/GPU resources and complete wall time, including forecasting and rejection/cache work. Declare a worthwhile relative gain δ before testing; report paired uncertainty with its sampling unit. Advance if the lower interval bound exceeds δ. Drop the target-setting investment if the upper bound falls below δ; otherwise the benefit remains unresolved.

Two explanations remain: adaptation exploits changing acceptance conditions, or bookkeeping/comparator selection explains the apparent advantage. Under the first, adaptive gains should survive corrected timing and held-out selection; a shuffled gamma schedule with matched draft-length frequencies should weaken them. Under the second, the gains disappear after those controls. Acceptance variability is a hypothesis, not an established moderator.

The unsupported step is transfer from bounded, dependent results to a worthwhile, exact T‑7 chat policy. This diagnostic is not a novelty claim. Stop: the supplied packet is exhausted; full proofs, independent chat replication, broader hardware evidence and P7 methods remain unavailable.
