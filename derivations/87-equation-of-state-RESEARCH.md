# 87 — RESEARCH: The Constrained Balance — the Equation-of-State Fork

**v27.0 Phase 87 (J5-on-the-variety, step 3). A GENUINE FORK.
Drivers: `code/variety_equation_of_state.py` (executor, 15/15 PASS),
`code/variety_equation_of_state_verify.py` (independent path, 5/5 PASS). Exact over
Q / Q(t). VERDICT: LIVE — the equation-of-state closes into a local balance law.**

This run executes the v26 Gate-5(a) fork: does the two-structure competition between the
second-order entropy-response field `G_M` and the canonical coordinate `c_R` close into a
LOCAL balance law on the idempotent variety? "Equation of state" is Jacobson's phrase used
as a STRUCTURAL analogy only — the question is pure exact algebra (multiplier-locality):
no thermodynamics, no horizons, no `G = κT`. The verdict is genuinely open; the
elimination decides.

---

## 0. Setup: gradients on the variety

At a rank-1 idempotent `p`, the tangent space is the Peirce space `J_{1/2}(p)`,
trace-form-orthogonal to `J_1 ⊕ J_0`. For fixed `Y`, the differential of
`φ_Y(p) = ⟨Y,p⟩` in a tangent direction `v ∈ J_{1/2}(p)` is `⟨Y,v⟩ = ⟨π_{1/2}^{(p)}(Y),v⟩`,
so the covector `dφ_Y` is represented by the Peirce projection `π_{1/2}^{(p)}(Y)`. Hence:
- `dG_M(p) = π_{1/2}( M# − ½⟨M,p⟩·M )` (since `G_M = ⟨M#,p⟩ − ¼⟨M,p⟩²`);
- `dc_R(p) = π_{1/2}( R )`, where `c_R(p) = ⟨R,p⟩` for a reference rank-1 idempotent `R`
  (v24 Gate-3's `c11` with movable `R`).

Verified both ways: the Peirce-projection formula matches `d/dt G_M(p(t)) = ⟨dG_M, ṗ(t)⟩`
along the recorded families (Gate 0).

**The balance condition (METRIC-FREE).** Extremize `G_M` on level sets of `c_R`:
> **π_{1/2}( M# − ½⟨M,p⟩·M ) = λ · π_{1/2}(R)**   (at `p`, as covectors),
proportionality of covectors — no inner product, so `λ` has no hidden normalization.
By F₄-transitivity (Spin(9) = Stab E_11), fix `p = E_11`; `M`, `R` stay symbolic; the
tuple and `λ` are stabilizer-invariant, the locus stabilizer-covariant.

---

## 1. The fork and its reduction

**THE FORK.** On the parallel locus (off trivial strata), is `λ` a state-universal
function of the FROZEN local tuple **`(a, c, c_R, TrM², detM)`**, `a := ⟨M,p⟩`,
`c := ⟨M#,p⟩` — the same function for all `M` and all `R`? The quadratic Peirce data of
`M` is tuple-determined (`|π_{1/2}M|² = ½TrM² − a² + c`, `Tr C_pM = −a`, `det₂C_pM = c`),
so the fork lives at CUBIC order, in the octonion direction data v24 proved the landscape
resolves. The mixed alignment invariants `⟨π_{1/2}M, π_{1/2}R⟩` are NOT in the tuple:
whether the locus FORCES them given the tuple IS the fork.

**Norm convention (stated once, for precision).** Throughout, `|π_{1/2}M|² := ½TrM² − a² + c`
= the sum of the squared `J_{1/2}` octonion-entry magnitudes `|x₂|² + |x₃|²` (the reduced-norm
convention used in the prompt). The trace-form norm `‖π_{1/2}M‖²_tr := Tr((π_{1/2}M)∘(π_{1/2}M))`
is exactly TWICE this, `= 2(½TrM² − a² + c)`. The reduction below (`λ² = |dG|²/|dc_R|²`) uses
the trace-form norm consistently in numerator and denominator, so the factor cancels and the
bookkeeping is internally exact; only the closed-form `|π_{1/2}M|²` label carries the reduced
convention.

**A structural deepening (the alignment invariant is tuple-forced).** The mixed invariant the
fork warned could secretly carry a certificate, `J := ⟨π_{1/2}M, π_{1/2}M#⟩`, is ITSELF
tuple-determined: `J = −2ac + 2·detM` exactly over all 26 parameters (both monomials needed).
The very object that could have hidden a DEAD is forced by the tuple — which is *why* `Q_M`'s
fit is a genuine identity rather than an over-rich fit.

**The reduction (the key move).** The parallel condition makes `dG_M = λ·dc_R` on the
locus, so in ANY metric `|dG_M|² = λ²|dc_R|²`; the metric cancels in the ratio, giving the
metric-free
> **λ² = |dG_M|² / |dc_R|² = Q_M / (2 c_R(1−c_R))**,  `Q_M := |π_{1/2}(M# − ½aM)|²`,

using `|dc_R|² = |π_{1/2}(R)|² = 2c_R(1−c_R)` (exact for every rank-1 idempotent `R = vv*`:
`c_R = |v_0|²`, `|π_{1/2}(R)|² = 2|v_0|²(|v_1|²+|v_2|²) = 2c_R(1−c_R)`). Therefore
> **LIVE ⟺ `Q_M` is a function of `(a, c, TrM², detM)`** (then `λ²` is, given `c_R`);
> **DEAD ⟺ two on-locus configs with the same tuple and different `Q_M`** (a certificate).

The pre-registered marginal dimension count (generic tuple-fiber dim = generic
stabilizer-orbit dim = 4) makes this inconclusive by counting; the elimination decides.

---

## 2. The elimination (Tiers A→B→C) and the law

For traceless `M`, `Q_M = |π_{1/2}(M# − ½aM)|²` is a degree-4 invariant of `M`. The only
tuple monomials of total `M`-degree 4 are `{(TrM²)², c², a·detM, a²TrM², a⁴, a²c, c·TrM²}`.
Fitting `Q_M` to this 7-term ansatz and demanding the residual vanish IDENTICALLY:

| tier | `M` | params | fit | result |
|---|---|---|---|---|
| A (u-complex / cut) | `h₃(C_u)` traceless | 8 | EXACT, residual ≡ 0 | LIVE-in-sector |
| B (one octonion block) | diag + one off-diag octonion | 10 | EXACT, SAME coeffs | — |
| C (full OP²) | full traceless | 26 | EXACT, SAME coeffs | **LIVE globalized** |

All three tiers give the identical coefficients `(A,B,C,D,E,F,G) = (0, −2, 0, ¼, −½, 5/2, −1)`,
with the residual identically zero through the full 26-param symbolic `M`. Since the fit is
an exact polynomial identity (not least-squares), **no certificate pair can exist** — a
symbolic PROOF of LIVE, not a battery. (Confirmed: a `≥44`-instance rational battery and an
adversarial matched-tuple certificate hunt both find `Q_M` always tuple-equal.) The law
factors:
> **`2 Q_M = (½TrM² − a² + c)(a² − 4c) = |π_{1/2}M|²·(a² − 4c)`,**

and since `a² − 4c = (Tr C_pM)² − 4 det₂C_pM = −4 G_M` (the squared face eigengap):
> **`4 c_R(1−c_R) λ² = |π_{1/2}M|²·(a² − 4c) = −4·|π_{1/2}M|²·G_M`**,
> equivalently **`c_R(1−c_R) λ² = −|π_{1/2}M|² · G_M(p)`.**

`detM` does NOT appear (coeff `C = 0`): the law is cubic-norm-blind. The multiplier² is the
J_{1/2}-norm of the matter times the (positive) `−G_M`, divided by the canonical-coordinate
factor — `G_M ≤ 0` (v26 positivity) makes `λ² ≥ 0` automatically. **The v26 second-order
entropy-response field IS the source of the v27 multiplier.**

**Hand anchor (reproduced exactly).** `M₀ = F_12(1) + E_11 − E_33` (rows
`[[1,1,0],[1,0,0],[0,0,−1]]`), `M₀# = [[0,1,0],[1,−1,0],[0,0,−1]]`, tuple `(1,0,4,1)`,
`p = E_11`, `R(t)` the real `(1,0)`-family: `dG(E_11) = ½F_12(1)`, `dc_R = cs·F_12(1)`,
`λ = 1/(2cs)`, `4c_R(1−c_R)λ² = 1` — the law's specialization (`|π_{1/2}M₀|² = 1`,
`a²−4c = 1`, product 1 ✓). **Negative anchor** `M_{e₁} = F_12(e₁) + E_11 − E_33`: same tuple
`(1,0,4,1)`, same `|dG|² = ½`, but `dG = ½F_12(e₁) ∦ cs·F_12(1)` — OFF the locus at `E_11`
against the real family, re-entering against the `e₁`-family with the SAME `λ` (Spin(9)
pair, never a certificate). The magnitude (hence `λ²`) is tuple-fixed; only the direction
rotates — exactly the LIVE mechanism.

---

## 3. Strata, guards, and the D4 reading

**D1 strata (excluded from fork evidence, zero verdict weight):** `dc_R = 0` (`p = R` /
polar locus), `dG_M = 0` (`G`-critical: diagonal/eigenframe-aligned `M`, incl. `E_11`),
`λ = 0`. **D2 tuple-rank:** the `M`-tuple `(a,c,TrM²,detM)` Jacobian has generic rank 4 —
functionally independent, no forced relation, so the tuple is used as-is (frozen).

**Guards (all held):** metric-free verdicts (covector proportionality only); strata
discipline (λ-verdicts only on the open stratum); exactness (Q/Q(t), no float in any verdict);
the tuple is FROZEN `(a,c,c_R,TrM²,detM)` — no mixed invariant added to rescue LIVE, `detM`
not dropped; sector honesty (Tier verdicts are sector verdicts; LIVE globalized only by the
full-26 symbolic identity); the `conj(x₃x₂)` octonion-order trap pinned (independent
implementations agree on an octonionic battery).

**D4 reading (LIVE branch, fenced).** The route's FIRST selection-shaped LOCAL law: on the
parallel locus, the second-order entropy response `G_M` trades against the canonical
coordinate `c_R` at a rate fixed by local field values ALONE. **STILL NOT Einstein, NOT a
metric law; the canonical geometry is FROZEN throughout; `λ` is a Lagrange multiplier, NOT a
coupling; no Newton constant; `λ₁, λ₂` remain spectral data; signature OPEN.** We are in the
LIVE world: the scalar sector closes into a local balance, so the spinor-moment object
`p ↦ π_{1/2}^{(p)}(X)` (v26 Gate-5(b)) is the natural — but, with the scalar law closed,
OPTIONAL, not forced — v28 object. The through-line: v24 found the field; v25 its closed form
and forced operator; v26 its source and MaxEnt theorem; **v27 closes it into a local balance
law whose multiplier is the entropy response itself.**

---

## 4. Citations

- T. Jacobson, "Entanglement Equilibrium and the Einstein Equation," Phys. Rev. Lett. **116** (2016) 201101 — the "equation of state" framing (used here as a STRUCTURAL analogy only; no thermodynamic import).
- K. McCrimmon, *A Taste of Jordan Algebras*, Springer (2004); T. A. Springer & F. D. Veldkamp, *Octonions, Jordan Algebras and Exceptional Groups*, Springer (2000) — the Peirce decomposition `J = J_1 ⊕ J_{1/2} ⊕ J_0`, the sharp/adjugate, `M² = M# + σ₂(M)I`.
- J. Faraut & A. Korányi, *Analysis on Symmetric Cones*, Oxford (1994) — Peirce projections and the trace form on Jordan algebras (the `J_{1/2}` gradient representation).
- A. Borel, C. R. Acad. Sci. Paris **230** (1950) — F₄ transitive on rank-1 idempotents (`OP² = F_4/Spin(9)`), the wlog `p = E_11`.
