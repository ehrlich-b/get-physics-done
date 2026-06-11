# 89 — GATE 0 SUMMARY: machinery regression (fail-fast)

**v29.0 Phase 89. Exact over Q. ALL PASS.** Driver `code/thermal_time_consistency.py`.

- **v26 regression:** `M=diag(2,−1,−1)` ⟹ `G_M(E_22)=−9/4` (the v26 response field intact).
- **The 2×2 parallelism lemma (trap #5):** on a 2-face, `ρ² = Tr(ρ)ρ − det₂(ρ)(1−p)`
  (rank-2 Cayley–Hamilton), so any analytic `f(ρ) ∈ span{1−p, ρ}` and `traceless(f(ρ)) ∥
  traceless(ρ) ∥ traceless(C_pX)` — verified symbolically. (Doubles as the reduction lemma;
  direction-match is therefore VACUOUS and never used as evidence.)

**Gate 0: ALL PASS** — the v26 machinery and the parallelism lemma certified.
