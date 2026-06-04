---
artifact: code/cartan_gate0_torsion.py
verified: 2026-06-04
verifier: gpd-verifier (independent re-derivation, HIGH bar)
subject: Gate-0 ("cheap kill") Einstein-Cartan torsion from chiral V_{1/2} spin on h_3(O)
driver_verdict: fp-imported-action
verifier_verdict: fp-imported-action (CONFIRMED)
confidence: HIGH
exact_over_Q: true
octonion_algebra_used: false
checks_total: 33
checks_independently_confirmed: 33
---

# Gate-0 Verification: Einstein-Cartan Torsion on h_3(O)

**Mandate.** Confirm or refute the driver verdict `fp-imported-action` at HIGH bar
by INDEPENDENT re-derivation (not re-running). Two load-bearing issues:
**Issue 1** (the decisive boolean `algebra_weights_nonneg` is hardcoded — is
"no negative-weight invariant" a sound theorem?) and **Issue 2** (does G0c
genuinely FAIL → `fp-imported-action`, or should it PASS → SURVIVE to Gate 1?).

**Verdict.** `fp-imported-action` is **CONFIRMED at HIGH confidence**. Issue 1's
hardcoded boolean is a *theorem* (established below from the invariant-ring
grading, not merely asserted). Issue 2 resolves cleanly to **G0c FAILS**: the
bridge ratio −2/3 (weight 0) and the geometric-torsion coupling (weight −1) are
genuinely different objects by an exact, independently-verified homogeneity
mismatch.

**Computational oracle:** every check below was executed exact-over-Q (SymPy
`Rational`/`Matrix`/symbolic), `octonion_algebra` confirmed absent from
`sys.modules`, no numpy on any decisive path. The driver itself re-ran clean
(`ALL_PASS=True`, exit 0).

---

## A. Driver re-run (confirmation only)

`cd code && python3 -u cartan_gate0_torsion.py` → **ALL_PASS=True, exit 0**.
Headline reading reproduced verbatim:

| Quantity | Value |
|---|---|
| BRIDGE const (algebra-fixed, single) | **−2/3** |
| Def-A S^a at sample [x0,x1,x2,x3] | [39/200, 11/100, −7/100, 29/200] |
| Def-A S^a flipped | [39/200, 11/100, −7/100, **−29/200**] |
| det_3(matter) on Lorentz block | **0** |
| det_2(g) weight under e→λe | λ^8 |
| Cartan coupling c=T/S weight | **λ^{−1}** |
| Gate-0 verdict | **fp-imported-action** |

This is necessary but NOT sufficient (re-running cannot catch a hardcoded
boolean). The independent re-derivations below are the decisive evidence.

---

## B. Independent re-derivations (33/33 INDEPENDENTLY CONFIRMED)

All three scripts under `/tmp/gate0_*` use only the warm SSOT engines
(`ring_lemma_verification`, `embedding_under_E_verification`,
`cartan_phaseA_coframe`, `bulk_geometry_verification`, `cartan_phaseC_contraction`)
and recompute by **different code paths** than the driver.

### B1. BRIDGE const −2/3 at a SECOND matter sample — CONFIRMED

Driver fixes −2/3 over the survivor basis pairs. I recomputed at a fresh, unrelated
rational survivor vector `{11:2/7, 18:5/3, 19:−4/9, 26:7/11}`:

```
S_a (C-contraction, lowered) = [−1662574/1440747, −1646/2079, 332/891, −1083884/1440747]
eta*soldering(Phi2,Phi2)     = [831287/480249, 823/693, −166/297, 541942/480249]
per-component ratios S_C/(eta*sold) = {−2/3}
```

Despite totally different intermediate rationals, the per-component ratio is the
single value **−2/3**, and the full bridge equation `S_a == (−2/3)(η·soldering)_a`
has **zero residual**. The const is matter-INDEPENDENT and algebra-fixed (it is the
det_3-polarization-vs-π_u-soldered-Jordan-product ratio, not an inserted knob).
Reconfirmed over all 16 survivor basis pairs (singleton {−2/3}, no INCONSISTENT
marker).

**Method:** `/tmp/gate0_independent_verify.py` CHECK 1–2. **INDEPENDENTLY CONFIRMED.**

### B2. det_3 == 0 on the Lorentz block via a FRESH generic symbolic survivor — CONFIRMED

Built a fresh generic symbolic survivor element with 4 free rational symbols
`a11,a18,a19,a26` on the C_u-survivor coords (independent of the driver's `Mfull`):
`det_3(generic survivor) = 0` identically. Also confirmed `det_3 == 0` on the
generic soldered C_u V_0 spacetime element (β,γ,p,q free) — the cubic norm
degenerates on the primitive-Peirce (α=0) slice. This independently reproduces the
v18 Phase-78 fact via a different symbolic element.

**Method:** `/tmp/gate0_independent_verify.py` CHECK 3. **INDEPENDENTLY CONFIRMED.**

### B3. Grading weights by DIRECT λ-substitution into the SSOT functions — CONFIRMED

Rather than trust the driver's *asserted* weights, I substituted `X → λX` into the
actual SSOT scalar functions and read the homogeneity degree (zero residual = exact
homogeneity):

| Scalar | f(λX) − λ^k f(X) | weight k |
|---|---|---|
| Tr(X) | 0 | **+1** |
| Tr(X∘X) | 0 | **+2** |
| det_3(X) | 0 | **+3** |
| det_2(g), g→λ²g | 0 | **+8** (since g=e·e is quadratic in e) |
| S = soldering(φ,φ), φ→λφ | [0,0,0,0] | **+2** (quadratic in φ) |

Every SSOT scalar has strictly positive weight. **Method:**
`/tmp/gate0_independent_verify.py` CHECK 4–5. **INDEPENDENTLY CONFIRMED.**

### B4. Single-copy Molien series → generator degrees {1,2,3} — CONFIRMED

`H(s) = 1/((1−s)(1−s²)(1−s³))`; plethystic log = **s + s² + s³** exactly. The
invariant ring `R[h_3(O)]^{F_4}` is a free polynomial ring on generators of degrees
**1, 2, 3 — all positive**. This is the Springer / Faraut-Korányi / Garibaldi-
Guralnick theorem, and it is the project's own certified v16 RING-lemma fact
(`molien_bigraded.py` G1 calibration gate, two-copy bidegrees all ≥ 0 in
`ring_generating_set.py`/`generating_set_certificate.py`).

**Method:** direct SymPy series + plethystic log. **INDEPENDENTLY CONFIRMED.**

### B5. Chirality structure via the independent C-block table — CONFIRMED

`/tmp/gate0_cblock_check.py` (a different construction — diagonal/off-diagonal
C-block tables) gives:

```
b+ (beta+gamma) = x0 :  x2-block=[−1/3]  x3-block=[−1/3]  UNIVERSAL (chirality-EVEN)
b− (beta-gamma) = x3 :  x2-block=[−1/3]  x3-block=[+1/3]  SIGN-SPLIT (chirality-ODD)
```

The timelike x0 direction is chirality-EVEN (universal C_{i,i,17}=−1/6); the
spacelike x3 direction is chirality-ODD (the −1/3 ↔ +1/3 sign split). This is the
structural source of the G0b flip and independently confirms it.

**Generic-symbolic confirmation:** the 16-symbol Def-A current has
`S^0 = ½(p₀²+p₇²+p₈²+p₁₅²)` (survivor amplitudes, symmetric in x2↔x3 → EVEN) and
`S^3 = ½(−p₀²−p₇²+p₈²+p₁₅²)` (x2-survivors minus x3-survivors → ODD). Only the 4
C_u survivors enter; e₁..e₆ drop out. **INDEPENDENTLY CONFIRMED.**

### B6. Forced so(3,1) genuinely closes as so(3,1) — CONFIRMED

Rebuilt the residual structure group (build_e6_basis → stab → nullspace) and
verified independently:

- Stab_{V_0} = 45 = dim Spin(9,1) ✓
- residual dim = **21** = so(3,1)[6] ⊕ so(6)[15] ✓
- Lorentz-block image on the C_u 4-space = **6** = dim so(3,1) ✓
- every block kills the (1,3) metric: `Aᵀg + gA = 0` ✓ (so(3,1), not gl(4))
- **Killing form signature (3,3,0)** → non-compact semisimple = so(3,1) ✓
- the 6 generators are **bracket-closed** (rank doesn't grow adjoining all [Lᵢ,Lⱼ]) ✓
- the so(6) complement (15 gens) acts with **zero image** on spacetime → a
  spacetime-trivial IDEAL, NOT extra Lorentz freedom (averts fp-arbitrary-reduction) ✓

**Method:** `/tmp/gate0_so31_and_headline.py` CHECK 6. **INDEPENDENTLY CONFIRMED.**

### B7. Def-A headline + chirality flip + bridge self-consistency — CONFIRMED

Fully independent recompute at the locked MATTER:
`S^a = [39/200, 11/100, −7/100, 29/200]` (matches); flipped
`[39/200, 11/100, −7/100, −29/200]` (x0,x1,x2 EVEN, x3 ODD — matches);
C-contraction `S_a = [−13/100, 11/150, −7/150, 29/300]` with
`S_a == −2/3·η·S^a` (zero residual). **Method:** `/tmp/gate0_so31_and_headline.py`
CHECK 7. **INDEPENDENTLY CONFIRMED.**

### B8. verdict() ladder non-hardwired (except the flagged Issue-1 boolean) — CONFIRMED

The driver's own non-hardwired demonstration is sound and I reproduced its logic:
all-pass → SURVIVES; T==0 → torsion-free; parity-blind → torsion-free;
coupling-free → fp-imported-action. Each clause is independently load-bearing. The
ONE hardcode is the `coupling_forced` input itself (Issue 1), adjudicated below.

### B9. Source/exactness discipline — CONFIRMED

`octonion_algebra` absent from `sys.modules` on every decisive path (asserted in
all three independent scripts); det SSOT native `ring_lemma_verification`
(det_3(diag(2,3,5))=30 exact integer); no numpy float-rank on decisive paths; AST
guard FIRES on an injected κ=8πG (not a no-op). **CONFIRMED.**

---

## C. ISSUE 1 — is "no negative-weight invariant" ESTABLISHED?

**YES — it is a theorem, not an unproven assertion.** The driver line
`algebra_weights_nonneg = True` is hardcoded, but the underlying mathematical fact
is sound and is established (not merely asserted) by the following argument, every
step of which I verified exact-over-Q:

1. **The single-copy invariant ring is a FREE polynomial ring on positive-degree
   generators.** `R[h_3(O)]^{F_4} = R[Tr, Tr², det_3]` with generator degrees
   {1, 2, 3} (Springer 1962 / Faraut-Korányi / Garibaldi-Guralnick; this project's
   certified v16 RING-lemma). Verified here: Molien series
   `H(s) = 1/((1−s)(1−s²)(1−s³))`, plethystic log = `s + s² + s³` (B4). The
   two-copy ring's 10 generators all sit at non-negative bidegree (B4).

2. **Every invariant is a polynomial in non-negative-weight generators.** Under the
   soldering rescale `e → λe` the algebra coordinates scale as `X → λX`, so each
   generator scales by `λ^(its degree)` with degree ∈ {1,2,3} > 0 (B3, verified by
   direct substitution: Tr~λ, Tr²~λ², det_3~λ³). Any homogeneous invariant of total
   degree d therefore has weight d ≥ 0, with d = 0 only for constants.

3. **Negative weight is unreachable.** A weight−1 scalar would require EITHER a
   negative-degree generator (none exist — the ring is generated in degrees 1,2,3)
   OR a rational quotient (a DENOMINATOR). The polynomial invariant ring contains no
   quotients. The Cartan coupling needs weight −1 (§D), so no algebra invariant can
   supply it.

4. **Even the ratio escape-hatch is closed.** One could try to manufacture weight −1
   by dividing invariants (e.g. Tr/det_3 ~ λ^{−2}). But (i) such a ratio is not a
   polynomial invariant; (ii) it is ill-defined precisely where det_3 = 0 — and
   det_3 ≡ 0 IDENTICALLY on the entire C_u-survivor / Lorentz block (B2); and
   (iii) *which* ratio is an arbitrary choice = exactly the imported normalization.
   So the ratio route is itself `fp-imported-action`.

**Conclusion:** `algebra_weights_nonneg = True` is **mathematically sound**. The
hardcode is a presentational shortcut for a genuine theorem; it does NOT inflate the
verdict. (Recommendation: the driver could derive it from the generating-set grading
rather than asserting it inline, but the boolean's VALUE is correct.) **This does
not lower confidence.**

---

## D. ISSUE 2 — does G0c FAIL (fp-imported-action) or PASS (→ Gate 1)?

**G0c genuinely FAILS → `fp-imported-action`.** The counter-argument (that −2/3 is
read from the algebra, so the coupling is algebra-fixed and the milestone should
SURVIVE) is **refuted by an exact homogeneity mismatch**:

- **The bridge ratio −2/3 is WEIGHT 0 (quadratic/quadratic).** It relates the
  C-block contraction to the η-lowered soldering bilinear. Both objects are
  **quadratic in the V_{1/2} sector** φ: I verified `S = soldering(φ,φ)` scales as
  `λ²` under `φ→λφ` (B3/B5, zero residual). A quad/quad ratio is dimensionless. So
  −2/3 fixes the **SHAPE** of the spin current relative to the soldering bilinear.

- **The geometric-torsion coupling c is WEIGHT −1 (linear/quadratic).** Geometric
  torsion `T^a = d_ω e^a` is **LINEAR in the coframe e** (one factor of e; weight
  +1). The spin current S is **QUADRATIC** in the V_{1/2} sector (weight +2). The
  Cartan equation `T^a = c·S^a` therefore forces `c ~ λ^{1−2} = λ^{−1}` —
  dimensionful (1/length² in physical units). Verified: det_2(g)~λ⁸, S~λ², the
  λ^{−1} coupling weight (B3, A).

- **The homogeneity mismatch is REAL** (the prompt's decisive technical point):
  T is linear-in-e while S is quadratic-in-V_{1/2}. The bridge ratio −2/3
  (weight 0) and the geometric coupling c (weight −1) are therefore **different
  objects of different λ-weight**. −2/3 fixes the spin current's shape but says
  NOTHING about the geometric coupling's scale. By Issue 1, no algebra invariant
  carries weight −1, so the coupling is a FREE parameter — supplied only by a
  POSITED Einstein-Cartan action (kappa = 8πG), exactly the v18 Phase-78 import.

**Why the "froze kappa as a ratio in Ph77" precedent does NOT rescue it:** Ph77's
−2/3-style ratios relate same-weight (quadratic) algebra objects — weight-0 shape
ratios. The geometric coupling is a different beast: it relates a linear-in-e
torsion to a quadratic spin current, so it carries net negative weight and is
dimensionful. A weight-0 ratio cannot fix a weight−1 coupling. The soldering form
`e = π_u(dE)` is scale-free (h_3(O) is a dimensionless graded algebra), so there is
no intrinsic length to set the coupling. **G0c FAILS; the honest call is
`fp-imported-action`, NOT SURVIVE-to-Gate-1.**

---

## E. Universal physics-verification checks

| Check | Result | Confidence |
|---|---|---|
| Dimensional/scaling analysis (the λ-weight argument) | CONSISTENT — every term's weight verified by direct substitution | INDEPENDENTLY CONFIRMED |
| Limiting case (M=0 soldered vacuum) | g(M=0) == G_DET2_RAW, signature (1,3,0) | INDEPENDENTLY CONFIRMED |
| Symmetry (chirality x2↔x3 under the flip) | x0 even / x3 odd, structurally derived | INDEPENDENTLY CONFIRMED |
| Group theory (forced so(3,1)) | dim 6, kills η, Killing (3,3), bracket-closed; so(6) trivial ideal | INDEPENDENTLY CONFIRMED |
| Math consistency (det_3≡0 on block) | fresh generic symbolic → 0 | INDEPENDENTLY CONFIRMED |
| Exact-over-Q discipline / no octonion_algebra / no float | clean on all paths | INDEPENDENTLY CONFIRMED |
| LLM-error scan (class 4 group theory, class 15 dimensional, class 19 DOF) | so(3,1) Casimir/signature correct; weights consistent; 4-dim coframe forced | no errors found |

No catastrophic cancellation (rational arithmetic, exact). No analytical-numerical
disagreement (everything analytical/exact). Integration measures N/A (no integrals).
Approximation validity N/A (exact symbolic, no perturbative expansion).

---

## F. Final confidence

**Verdict: `fp-imported-action` — CONFIDENCE HIGH.**

**True-strength reason.** A nonzero, chirality-tracking, non-circular V_{1/2} spin
current EXISTS (G0a/G0b/G0c.1 all independently confirmed: Def-A & Def-B nonzero
at the sample and generic-symbolic; x3 flips while x0 stays even; every coefficient
is (1/6)polarize_d / soldering with the AST guard firing on injection). The bridge
const −2/3 is genuinely algebra-fixed and matter-independent (reproduced at a second
sample, component-wise). BUT the decisive non-circularity gate G0c.2 FAILS at true
strength: the geometric-torsion coupling has λ-weight −1 (T linear-in-e, S
quadratic-in-V_{1/2}) — a DIFFERENT object from the weight-0 bridge ratio −2/3 —
and **no h_3(O) invariant can carry negative weight** because the invariant ring is
a free polynomial ring on positive-degree generators {Tr, Tr², det_3} (a theorem,
verified via the Molien series and direct λ-substitution; the only negative-weight
escape, a det_3 quotient, is both non-polynomial and identically singular on the
Lorentz block). The Einstein-Cartan coupling kappa = 8πG is therefore supplied only
by a posited action — the same import as v18 Phase-78 — placing this firmly in the
honest-partial GST/Singh/Castro class. Both load-bearing issues resolve in favor of
the driver verdict: Issue 1's hardcoded boolean is sound, and Issue 2's G0c failure
is real.

**Net:** the verdict rests on INDEPENDENTLY CONFIRMED computations (33/33), a sound
grading theorem, and a real homogeneity mismatch — not on the hardcoded boolean
alone. HIGH confidence; ready for human ratification.

### Minor note (non-blocking, for the orchestrator)

The driver's `g0c2_geometric_coupling()` derives `coupling_negative_weight` and
`det2_w8` from substituted weights but then hardcodes the *decisive*
`algebra_weights_nonneg = True` (lines ~581/599) rather than deriving it from the
generating-set grading. The boolean's VALUE is correct (a theorem, §C), so the
verdict is sound, but a future tightening could compute it from
`molien_bigraded`/`ring_generating_set` (degrees {1,2,3} all > 0) to remove the last
hardcode. This is a presentational nit, not a correctness gap.
