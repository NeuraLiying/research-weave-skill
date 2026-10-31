# Fictional source packet — speculative decoding draft-length policy (offline test)

All works, numbers and identities below are INVENTED test data, not real publications. Treat each as a user-supplied excerpt with `local:` provenance. No live search is available or requested. Do not assume unreported fields.

Researcher's decision: for target model T-7 serving chat traffic on one GPU type, should they invest in an *adaptive draft-length* policy (choose gamma per step) instead of tuning a *fixed* gamma? Success metric: end-to-end wall-clock tokens/sec at batch size 1, output distribution must stay exact. They can deeply read only TWO works.

## P1 — Adaptive Gamma via Acceptance Forecasting (2024), methods/results excerpt
Source: local:P1-v1. Version 1. Target T-7, drafter D-1, dataset CHAT-500, batch 1, GPU type G-A. Table 3: adaptive gamma vs best fixed gamma (gamma=4, chosen on the same CHAT-500 test set) = +9% tokens/sec (mean over 3 seeds, no interval reported). Section 6: the forecasting head adds 3% latency, included in timing. Authors: Lab Kappa.

## P2 — Adaptive Gamma via Acceptance Forecasting, v2 (2025), errata excerpt
Source: local:P2-v2. Version 2 of P1 (same authors). Errata: v1 timing excluded draft-model KV-cache rebuild after rejections for the adaptive arm only. With the fix, adaptive vs best fixed gamma = +2% tokens/sec, 95% interval [-3%, +7%], 5 seeds. All other settings as P1.

## P3 — Dynamic Drafting at Scale (2025), methods/results excerpt
Source: local:P3-v1. Lab Kappa (same group as P1/P2), reuses the P1 codebase and CHAT-500. Target T-9 (larger than T-7), batch 1, GPU G-B. Adaptive vs best fixed gamma (selected on a held-out dev split): +11% tokens/sec, 95% interval [+6%, +16%]. Section 5: "results consistent with P1, confirming adaptive drafting generalises."

## P4 — When Fixed Is Enough (2025), methods/results excerpt
Source: local:P4-v1. Lab Sigma. Target T-7, drafter D-1, dataset CODE-300 (code completion, high acceptance), batch 1, GPU G-A. Best fixed gamma (tuned on dev) vs adaptive policy reimplemented from P1-v1 description: adaptive -1% tokens/sec, 95% interval [-4%, +2%]. Section 4: "adaptive policies provide no benefit."

## P5 — A Survey of Speculative Decoding (2025), survey excerpt
Source: local:P5-v1. Section 7 table lists "adaptive gamma: +9% (P1), +11% (P3)" and states "adaptive drafting is consistently better across models." No new experiments.

## P6 — Adaptive Sampling in Sequential Testing (1998), conceptual excerpt
Source: local:P6-v1. Statistics. Section 3: choosing how many observations to take before deciding, based on running evidence, reduces expected sample count vs a fixed sample size when per-observation cost is constant. No LLM or decoding experiment.

## P7 — Speculation Under Load (2026), abstract only
Source: local:P7-abstract. Abstract: "adaptive draft length gives up to 2x speedup in production serving." Batch size, metric, baseline, model, hardware unspecified.
