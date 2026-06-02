# Phase 74 Cross-Phase Consistency Check (rapid mode)

**Phase:** 74 — Phase 0: Engine Recovery, Tangent Identity & Calibration (v18.0)
**Checked:** 2026-06-02
**Mode:** rapid (post-phase, against full convention ledger)
**Verdict:** WARNING (1 pre-existing, non-blocking, documented notation item; 0 Phase-74-introduced issues)

---

## Summary

Phase 74 is a **re-certification phase that made ZERO convention changes** — all 32 conventions
(18 canonical + 14 custom in state.json `convention_lock`) were inherited from v17.0 verbatim, and
the SUMMARY's `Convention Changes` table correctly reads "None — all v17.0 conventions inherited
verbatim." Every convention Phase 74 actually exercises is compliant and was ASSERT_CONVENTION-checked
in both the driver (`code/cartan_phase0_tangent.py`) and the deliverable
(`derivations/74-phase0-engine-tangent-calibration.tex`).

The verifier already ran a full in-phase consistency pass (14/14 physics checks CONSISTENT, including
"Convention assertions vs state.json lock = VERIFIED / INDEPENDENTLY CONFIRMED"). This cross-phase pass
confirms that result against the **full** ledger and the v17.0 producers, and re-checks the
load-bearing sign/factor benchmarks by independent arithmetic.

**Checks performed:** 11 · **Issues found:** 1 (pre-existing, WARNING)

---

## Convention Compliance Matrix (current phase vs full ledger)

| Convention (key) | Active value | Relevant to Ph74? | Compliant? | Evidence |
|---|---|---|---|---|
| metric_signature | mostly-minus on h_2(C_u) det_2 slice; bulk cone Riemannian | Partial (label only; no slice-index raise on decisive path) | LABEL CLASH (pre-existing) | Inherited verbatim; see Issue 1. Operationally inert here — Ph74 raises/lowers no slice index. |
| jordan_product | X∘Y=(1/2)(XY+YX); Tr(X∘Y)=Re Tr(XY) | YES | YES | E_11∘δ and J=2(E_11∘b)−b use exactly this; from-scratch verifier build reproduced it. |
| octonion_convention | Fano e1·e2=e4 | YES | YES | Verifier from-scratch CONV-CHECK: e1·e2=+e4, e2·e1=−e4, non-assoc. Driver imports SSOT primitives. |
| complex_structure | u=e7 | Cited (slice context) | YES | .tex convention lock Sec 1; not load-bearing for the tangent identity. |
| clifford_signature | Cl(9,0) positive-definite | Background | YES | Inherited; consistent with Spin(9) ⊂ F_4 orbit dims (Spin(8)=28, Stab_V0=45=Spin(9,1)). |
| peirce_eigenvalues | {0, 1/2, 1} | YES (core) | YES | L_E11 diagonal, eigenvalues {1:[0], 0:[1..10], 1/2:[11..26]} reproduced two independent ways. |
| cubic_norm / det SSOT | ring_lemma_verification.py det_3; 2Re(x2* x0* x1) order | YES (DERV-01) | YES | LOCK 7a CH norm + LOCK 7b 324/324=dim f_4=52; off-by-16 buggy order exhibited & rejected. |
| arithmetic_field | EXACT over Q; sympy.Matrix.rank, NEVER numpy | YES | YES | 0 float-rank on any decisive path (both source guards); all verdicts exact integers/rationals. |
| natural_units | ħ=c=k_B=1 | N/A (dimensionless diff-geo) | N/A | No unit factors enter the verdicts; binding requirement is exactness over Q (met). |
| generator_normalization | T_a=(1/2)γ_a; {T_a,T_b}=(1/2)δ_ab I_16 | Background (Spin(9) sector) | YES | Consistent with the dim counts; not directly invoked in DERV-02. |
| gamma_matrix_convention | Cl(9,0): {γ_a,γ_b}=2δ_ab I_16 | Background | YES | Same as above. |
| commutation_convention | [A,B]=AB−BA; {A,B}=AB+BA | YES (inner derivations) | YES | 324/324 inner-derivation [L_a,L_b] annihilation uses this bracket; = dim f_4 = 52. |
| group / rep / coupling_generator | F_4=Aut(h_3(O)) 52-dim; 27=1⊕26; c=Tr(X∘Y) (1,1) | Background | YES | e_6=78=52+26, orbit/stab anchors all consistent with F_4-not-E_6 structure. |
| fourier, gauge, regularization, renormalization, coordinate_system, index_positioning (slice), time_ordering, levi_civita_sign, covariant_derivative_sign, creation_annihilation_order | N/A (pure algebra) | N/A | N/A | Correctly marked N/A in the ledger; Phase 74 introduces no field theory / spacetime dynamics / second quantization. |

**Compliant: 12 relevant conventions · N/A: 19 (correctly inert) · Label clash: 1 (metric_signature, pre-existing).**

---

## Provides/Consumes Consistency

Phase 74 is the **foundational** phase of v18.0 (v17.0 archived). It **consumes** three warm v17.0
engines and **provides** four anchors to Phases 75–78. No numerical value crosses a boundary with a
unit/sign conversion; the transfer is *byte-identical engine re-use* + *exact-over-Q anchors*.

### Consumes (from v16.0/v17.0)

| Quantity | Producer | Meaning match | Test value | Convention match | Status |
|---|---|---|---|---|---|
| det SSOT (ring_lemma_verification.py det_3) | v16.0/v17.0 | Yes — same F_4-invariant cubic norm | re-ran: exit 0, ALL_PASS, **324/324** (not 30), CH 7a | Yes (det SSOT, octonion_algebra banned) | OK |
| single-copy orbit gate (orbit_dimension_gate.py) | v16.0 | Yes — single-copy F_4 orbit on 27 | re-ran: **24/28/3** PASS in-engine (designed nonzero exit on v16.0 RING pair-anchor handled) | Yes | OK |
| bulk geometry / e_6 / stab / K (bulk_geometry_verification.py) | v17.0 Ph71 | Yes — same cone/stabilizer machinery | re-ran: exit 0, ALL_PASS 41/41; e_6=78, orbit 17, Stab 61, Stab_V0 45, **K=−1/2** | Yes | OK |

### Provides (to Phases 75–78)

| Quantity | Consumer | Meaning | Test value | Status |
|---|---|---|---|---|
| T_{E_11}OP^2 = V_{1/2}(E_11), 16-dim (soldering form V_{1/2}-valued) | 75 (coframe reduction) | π_u reduces the 16-dim V_{1/2} to a 4d coframe | rank J=11, ker==span{11..26}, dim 16=17−1 — two independent routes agree | OK |
| det SSOT re-certified | 76, 77 | underlies every downstream curvature | 324/324, octonion_algebra.py absent | OK |
| K=−1/2 cone-Hessian sign benchmark (round_K=−1) | 76, 77 | pins Riemann/Ricci curvature SIGN before any verdict | K<0 constant on 3 slice-tangent 2-planes; round_K=2K | OK (sign load-bearing, not magnitude) |
| calibration anchors (24/28/3; 78; 17; 61; 45) | 75–78 | structure-group counts (Spin(9,1) Levi, e_6, OP^2 cone) | all exact integers, 8 arithmetic cross-checks hold | OK |

All four provided anchors are exactly the v17.0 consistency anchors, reproduced byte-for-byte —
these ARE the cross-phase consistency checks, and all pass.

---

## Load-Bearing Sign/Factor Spot-Checks (independent arithmetic)

Re-evaluated the prioritized downstream-referenced equations (the curvature SIGN and the tangent
DIMENSION are what every Phase 75–78 verdict will read):

| Check | Result | Pass |
|---|---|---|
| C1: K=−1/2, round_K=−1, round_K==2K, sign NEGATIVE | −1/2, −1, True, True | YES |
| C2: dim ker = 27−rankJ = 16 == orbit(E_11)−1 = 17−1 | 16 == 16 | YES |
| C3: Peirce λ=1/2; dim split V_1+V_0+V_{1/2}=1+10+16=27 | 1/2; 27 | YES |
| C4: e6=f4+26; stab_e6=e6−orbit; stab28=f4−24; trdeg3=27−24; stab_v0=45=10·9/2 (so(9,1)) | all True | YES |

The K=−1/2 sign benchmark and the metric signature are the two items the context flagged for
special attention. **The K sign is correct, constant, and negative**, with the documented exact
factor-2 (`g_slice|_apex = 2·g_round ⇒ K_slice = round_K/2 = −1/2`); the load-bearing fact is the
negative SIGN, which Phase 74 reproduces and which is consistent with the CONVENTIONS.md §1
Riemann/Ricci-sign benchmark (H^3 must come out negative) and the Phase 71 resolution.

---

## Approximation Validity

None to check — Phase 74 is exact over Q end-to-end (no small parameters, no truncations, no
validity ranges introduced). It introduces no parameter value that could violate any existing
approximation range in STATE.md (there are no active approximations: STATE.md "Active
Approximations: None yet").

---

## ISSUE 1 (WARNING — pre-existing, non-blocking): metric_signature label/glyph clash

**Category:** convention (notation/labeling) · **Severity:** WARNING (non-blocking) ·
**Origin:** PRE-EXISTING (carried from v17.0 Phases 71/72/73; NOT Phase-74-introduced)

**What it is.** The `metric_signature` convention is stored (in both state.json `convention_lock` and
CONVENTIONS.md §1) as the string **"mostly-minus (−,+,+,+)"**. The glyph `(−,+,+,+)` is, by the usual
reading, the *mostly-plus* sign pattern (one minus, three plus). The **label word** "mostly-minus"
and the **test value** disagree with the glyph:

- CONVENTIONS.md §1 test value: timelike `p^μ=(E,0)` gives `p·p = E² − |p|² > 0`, "one `+`, three `−`"
  → operational signature is `(+,−,−,−)` = **mostly-minus** (timelike-positive).
- The slice `det_2` Minkowski form `b·g/3 − p²/3 − q²/3` (one hyperbolic timelike block, two spacelike)
  confirms mostly-minus.

So the **operational object is unambiguous** (mostly-minus, timelike-positive, pinned by two
independent test values); only the **glyph string** `(−,+,+,+)` is mismatched to its own label and
test value. This is a string-label defect, not a sign error in any computation.

**Why it does not bind Phase 74.** Phase 74 raises/lowers **no slice metric index on any decisive
path**. Its decisive content is (i) the det SSOT (F_4-invariant cubic norm, signature-free), (ii) the
Peirce/tangent identity `T_{E_11}OP^2 = V_{1/2}` (eigenspace structure of the Jordan multiplication
operator, signature-independent), and (iii) dimension/orbit/stabilizer counts (integers). The only
signature-sensitive object it touches — the cone-Hessian sectional curvature — is reported by its
**sign** (K=−1/2 < 0), which is correct under either glyph reading. The verifier's
"Convention assertions vs state.json lock = INDEPENDENTLY CONFIRMED" stands because the driver/.tex
assert the same (self-consistent-modulo-glyph) lock the rest of the project uses.

**Why it MATTERS downstream (the reason it stays a tracked WARNING, not dismissed).** Phases 75–77
build a Lorentzian coframe and a Spin(3,1) connection, then read a curvature VERDICT off the slice
metric. Those phases WILL raise/lower slice indices and WILL test a Gram-matrix signature
((1,3) Lorentzian). The moment a Phase-75 author copies the glyph `(−,+,+,+)` literally into a
mostly-plus index-raising convention while the producer used mostly-minus, a global sign could flip on
a curvature contraction. The risk is latent, not realized in Phase 74.

**Suggested fix (non-blocking, before Phase 75 raises a slice index):** spawn
`gpd-notation-coordinator` to reconcile the `metric_signature` string so the glyph matches the label
and test value — i.e. write it as **"mostly-minus `(+,−,−,−)`"** (timelike-positive), or keep
`(−,+,+,+)` and relabel/retest as mostly-plus, consistently across state.json `convention_lock`,
CONVENTIONS.md §1, and the Phase-74 `.tex`/driver ASSERT lines. This is exactly the documented v17.0
non-blocking follow-up (STATE.md Session Continuity + Phase 70.1 blocker note + Phase 73 verifier
"Cross-Phase Consistency"): "metric_signature label/glyph reconcile (operationally inert)." Phase 74
neither fixed nor worsened it.

---

## Verdict

**WARNING.** Phase 74 introduces **no** consistency issue and **no** convention change. All 12
relevant conventions are compliant; all four downstream anchors reproduce the v17.0 producers
byte-for-byte; the K=−1/2 sign benchmark and the `16 = 17−1` tangent identity — the two items the
milestone's curvature verdicts will read — are sign- and factor-correct by independent arithmetic.

The single open item is the **pre-existing, documented, operationally-inert metric_signature
label/glyph clash** inherited from v17.0. It is a WARNING (a real latent notation hazard for the
index-raising Phases 75–77), NOT an INCONSISTENT (no sign/convention error corrupts any Phase-74
result, because Phase 74 raises no slice index on a decisive path). Confirmed: this is the **only**
consistency item, and it matches the verifier's single flagged non-blocking note.

**Recommended action:** Proceed to Phase 75. Schedule the `gpd-notation-coordinator` glyph
reconcile before Phase 75 first raises/lowers a slice metric index (the first signature-sensitive
contraction), so the latent hazard is closed before it can be realized.
