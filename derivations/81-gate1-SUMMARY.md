# Phase 81 (v21.0 Sakharov Gate 1): a_1 ∝ R — EXECUTOR SUMMARY

**Executed:** 2026-06-06
**Scope:** Gate 1 ONLY (run after Gate 0 SURVIVED). Gates 2/3 NOT run (fail-fast).
**Driver:** `code/sakharov_gate1_a1R.py` (exact over Q; `python -u` foreground; byte-identical across runs; exit 0; ALL_PASS=True)
**Derivation:** `derivations/81-sakharov-gate1.tex` (well-formed: environments balanced, all refs resolve; pdflatex unavailable in-env, NOT compiled)
**Upstream:** Gate 0 = SURVIVES (G>0, STr=+8/3, verifier-hardened HIGH within-scheme, human-ratified)

---

## VERDICT: PASS (a_1 clean ∝ R)

The V_{1/2}=16 Weyl heat-kernel coefficient is `a_1 = tr(E + R/6) = -R/3` per Dirac — a **clean multiple of the spacetime Ricci scalar R[g]**, with **zero** residual in any other curvature invariant. All three contamination channels the research flagged are absent:

1. **Gauge tr(F²) — drops out.** `E = -R/4 - (1/2)γ^{μν}F_{μν}`; the gauge term traces away because `tr(γ^{μν}) = 0` identically. tr(F²) is an a_2 term, not a_1.
2. **Wave-map target curvature — absent.** V_{1/2}=16 of Spin(10) is a LINEAR spinor rep (flat fermionic bundle, NOT a curved-coset sigma-model; the soldering e=π_u(dE) acts linearly), so the target Riemann tensor R^target ≡ 0 and the `E ⊃ -R^target(∂φ̄)²` channel is identically absent.
3. **Non-associativity / torsion — absent (CHECKED, not assumed).** The soldering connection ω(e) is the torsion-free Levi-Civita connection: torsion 2-form residual = 0 exact over Q on a position-dependent tetrad (warm harness `spin_connection_omega → torsion_of`), so the operator is Laplace-type and a_1 has the standard Gilkey form (no associator, no T²).

The verdict is DERIVED non-hardwired from `(has_nonR_residual=False, torsion_is_zero=True, is_linear_rep=True)`, not a literal. The DEAD/PASS mapping is a pure function of these flags; three self-tests prove each DEAD branch fires (synthetic R^target → DEAD, real clean → PASS, synthetic nonzero torsion → DEAD), pre-empting the v20 hardcoded-decisive-boolean bug.

**[CONFIDENCE: HIGH]** — The `a_1 = E + R/6` structure is textbook (Gilkey; Vassilevich §4.3), the F-term drop-out (`tr γ^{μν}=0`) and the residual=0 are exact over Q, the wave-map channel is ruled out by the linearity of the **16**, and the one genuine risk (Laplace-type) is checked exact over Q on the warm harness (the same Phase-77 routines that were verifier-hardened in v18). Three independent checks: (i) structural Gilkey theorem (a_1 carries only E + R), (ii) explicit symbolic residual = 0 with all non-R coefficients vanishing, (iii) harness torsion 2-form = 0 on a genuinely x-dependent tetrad.

---

## The exact-over-Q numbers

### a_1 structure (per Dirac), built from primitives:
| Quantity | Value (exact Q) | Source |
|---|---|---|
| tr(I₄) | `4` | d=4 Dirac bundle, 2^{d/2} |
| tr(γ^{μν}) | `0` | antisymmetric distinct gammas, traceless ⇒ F drops out |
| per-Dirac-COMPONENT a_1 R-coeff | `-1/4 + 1/6 = -1/12` | Lichnerowicz E=-R/4 + universal +R/6 |
| per-Weyl a_1 R-coeff | `-1/6` | half the Dirac bundle |
| **a_1 (per Dirac)** | **`-R/3`** | `4·(-1/12)·R` |
| coeff_R | `-1/3` | ∂a_1/∂R |
| coeff_F | `0` | gauge F traces away |
| coeff_R^target | `0` | flat target (linear rep) |
| **residual `a_1 - coeff_R·R`** | **`0` (exactly)** | a_1 is PURELY (rational)·R |
| degree in R | `1` (≤1) | no R², □R, R_{μν}² (those are a_2) |

### c_1 read-off (built ON the Gate-0 supertrace STr = +8/3):
| Quantity | Value (exact Q·π) |
|---|---|
| STr (from Gate 0, imported) | `+8/3` |
| **c_1 = STr/(4π)²** | **`1/(6π²)`** = (8/3)/(16π²) |
| κ⁻¹ = c_1 Λ_f² | `Λ_f²/(6π²)` |
| **G = 3π/(8 Λ_f²)** | **POSITIVE** (consistent with Gate 0) |

Λ_f (the ρ_J fixed-point scale) is **Gate-3 scope** — carried symbolic, NOT pinned here. Gate 1 delivers the dimensionless `c_1 = 1/(6π²)`.

### R≠0 anchor (warm harness, exact over Q):
- `R[g=e.e] (M≠0)` = `14187524733311967018208791837/634906109300195099205387025` ≠ 0 ⇒ the induced a_1 = c_1·R term is a NONZERO term (the EH coefficient is not vacuous).
- `R[g=e.e] (M=0)` = `0` (flat vacuum reference).

---

## Flags / check statuses

| Flag | Value | Meaning |
|---|---|---|
| `has_nonR_residual` | **False** | the DEAD trigger is NOT set; a_1 IS clean ∝ R |
| `torsion_is_zero` | **True** | soldering ω(e) torsion-free Levi-Civita (exact-Q harness, position-dependent tetrad); Laplace-type |
| `is_linear_rep` | **True** | 16 of Spin(10) linear ⇒ flat target ⇒ R^target=0, wave-map channel absent |
| `coeff_F == 0` | **True** | gauge F traces away (tr γ^{μν}=0) |
| `coeff_R^target == 0` | **True** | no target-curvature term |
| `first_order_in_R` | **True** | no R²/□R/R_{μν}² (those are strictly a_2) |
| Gate-0 consistency (STr=+8/3) | **True** | imported, NOT recomputed; c_1 built ON it |
| source/exactness/thermo guards | **clean** + FIRE on injection | no numpy.linalg/float/thermo on decisive path; octonion_algebra absent |
| 3 required self-tests | **all PASS** | synthetic contaminant→DEAD, clean→PASS, synthetic torsion→DEAD |

---

## What it means for the selection-law ledger

**Gate 1 does NOT kill.** The induced Einstein-Hilbert coefficient is a genuine clean `∫R` (the gauge sector lives in a_2, the target is flat, the background is torsion-free Levi-Civita) with `c_1 = 1/(6π²)`. With a positive sign (Gate 0) and a clean curvature term (Gate 1), the route lives to **Gate 2 = the predicted real death**: the v18 tensor-support mismatch (`G[g]` has 16 independent components, `κT` has 6). A scalar induced `κ` cannot change tensor rank, so it cannot repair the 16-vs-6 mismatch — exactly the ledger's "most likely actual cause of death."

This is a PASS at true strength of **the second of four gates** — NOT "Sakharov induced gravity works." Gate 1 certifies the curvature term is clean ∝ R; it makes no claim about closure `G[g]=κT[M]` (Gates 2-3).

---

## One line per gate (the ledger ladder)

| Gate | Status | Result |
|---|---|---|
| **Gate 0 (SIGN)** | DONE | SURVIVES (G>0, STr=+8/3, unforced, circularity=False) |
| **Gate 1 (a_1 ∝ R)** | **DONE** | **PASS** (a_1 = -R/3 clean ∝ R; c_1 = 1/(6π²); G = 3π/(8Λ_f²)>0) |
| **Gate 2 (support mismatch)** | NOT RUN | the PREDICTED real death — v18 16-vs-6 |
| **Gate 3 (closure)** | NOT RUN | deferred |

---

## Deviations

None. The plan/research-note recipe executed as specified. One implementation refinement (Deviation Rule 4 — correctness, not scope): the torsion check was implemented as a **genuine exact-over-Q harness computation** of the torsion 2-form on a position-dependent tetrad `E(x)=diag(1,1+x0²,1,1)` (mirroring the v18-Ph77 `closed_form_omega_demo` certified frame), rather than a reused assertion — because the harness `torsion_of(W, E, coords)` / `spin_connection_omega(E, coords)` signatures require an explicit tetrad and coords (not a matter dict). This makes torsion==0 a non-trivial computed check (the tetrad has real x-dependence; a non-Levi-Civita connection would give nonzero torsion). The matter-bearing R≠0 verdict is delivered via the provably-equal metric-Riemann route exactly as Phase 77 did (the surd-laden matter tetrad e0 hits the symbolic-d-omega watchdog).

---

## Reproducibility

- SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0 (no random seeds; all decisive values hardcoded exact rationals / Q·π).
- `code/sakharov_gate1_a1R.py` runs foreground `python -u` (~4s total; the only heavy call is the R≠0 anchor, ~3s). Byte-identical decisive output across runs.
- octonion_algebra.py BANNED (buggy float associator); warm harness `bulk_geometry_verification.py` + `cartan_phaseB_curvature.py` reused; Gate-0 primitives imported from `sakharov_gate0_sign.py`.

## NOTE

This is the EXECUTOR's reading of the mechanical Gate-1 checks. The ORCHESTRATOR/VERIFIER adjudicates the milestone verdict and any transition.

---

## Self-Check: PASSED

- Created files exist: `code/sakharov_gate1_a1R.py`, `derivations/81-sakharov-gate1.tex`, `derivations/81-gate1-SUMMARY.md` — all FOUND.
- Driver + tex commits exist: `bd0fc15a` (driver), `f944c6e1` (tex) — both FOUND.
- Driver re-run reproduces the decisive numbers reported here exactly: a_1 coeff_R=-1/3, residual=0, c_1=1/(6π²), G=3π/(8Λ_f²), torsion_is_zero=True, coeff_F=0, VERDICT=PASS, ALL_PASS=True.
- LaTeX well-formed: environments balanced, all `\ref`/`\eqref` resolve to defined labels, braces balanced (pdflatex unavailable in-env — NOT compiled).
- Byte-identical decisive output across runs; exit 0; no float on any decisive path.
- Convention consistency: mostly-minus (+,-,-,-), exact-over-Q, tr 1=4 (d=4) — matches the convention_lock and the Gate-0 driver.
