# 87 — GATE 2 SUMMARY: D1 (well-posedness/strata) + D2 (the multiplier machinery)

**v27.0 Phase 87. Exact over Q/Q(t). ALL PASS.** Independently checked
(`87-GATE-2-VERIFICATION.md`).

## D2 — the hand anchor (exact over Q(t))

`M₀ = F_12(1) + E_11 − E_33` (rows `[[1,1,0],[1,0,0],[0,0,−1]]`):
- `M₀# = [[0,1,0],[1,−1,0],[0,0,−1]]` (verified two ways: cofactors, and
  `X² − Tr(X)X + σ₂(X)I` with `σ₂ = −2`);
- tuple `(a,c,TrM²,detM) = (1,0,4,1)`;
- against `R(t) =` the real `(1,0)`-family, `E_11` is ON the locus for `t ∉ {0,±1}`, with
  `dG(E_11) = ½F_12(1) ∥ dc_R = cs·F_12(1)`, `λ = 1/(2cs)`, and
  **`4 c_R(1−c_R) λ² = 1`** — the specialization of the law `P` (with `|π_{1/2}M₀|² = 1`,
  `a²−4c = 1`).

## D2 — invariant-rank (the tuple is frozen as-is)

The `M`-tuple map `(a, c, TrM², detM)` has generic Jacobian rank **4** — functionally
independent, NO forced relation among the tuple coordinates. The fork is stated over the
full frozen tuple `(a, c, c_R, TrM², detM)`.

## D1 — strata (excluded from fork evidence, zero verdict weight)

`dc_R = 0` (`p = R` / polar locus); `dG_M = 0` (`G`-critical: diagonal / eigenframe-aligned
`M`, including `E_11`); `λ = 0`. Recorded; carry no verdict weight (the vacuity guard
class, institutionalized).

**Gate 2: ALL PASS.**
