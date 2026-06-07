# Phase 81 (v21.0 Sakharov Gate 2): SUPPORT MISMATCH — EXECUTOR SUMMARY

**Executed:** 2026-06-06
**Scope:** Gate 2 ONLY (run after Gate 0 SURVIVED and Gate 1 PASSED). This is the MILESTONE-DECISIVE gate (the ledger's predicted real cause of death). Gate 3 NOT run (FAIL-FAST: Gate 2 is DEAD).
**Driver:** `code/sakharov_gate2_support.py` (exact over Q; `python3 -u` foreground; byte-identical decisive output across runs; exit 0; ALL_PASS=True)
**Derivation:** `derivations/81-sakharov-gate2.tex` (well-formed: environments balanced, braces balanced, all refs resolve; pdflatex unavailable in-env, NOT compiled)
**Upstream:** Gate 0 = SURVIVES (G>0, STr=+8/3); Gate 1 = PASS (a_1=-R/3 clean ∝ R, c_1=1/(6π²), G=3π/(8Λ_f²)>0) — both verifier-hardened HIGH, human-ratified.

---

## VERDICT: DEAD (induced scalar κ does NOT repair the v18 16-vs-6 tensor-support mismatch)

The Sakharov route dies EXACTLY where v18 died. The induced Newton coupling is a **scalar** (κ = 6π²/Λ_f², from Gate 1's c_1 = 1/(6π²), κ⁻¹ = c_1 Λ_f²). A scalar multiplies the matter stress T by a number — it **cannot change which tensor components are nonzero** (cannot change tensor rank/support). So the v18 tensor-support mismatch survives the induced κ. Confirmed exact over Q on **matter-bearing** profiles (ρ>0, R[g]≠0, differentiated — the OPPOSITE of any deflated matter-free check).

This is the **predicted outcome** (the ledger's "most likely actual cause of death"). The constructed-vs-extremized gap is a tensor-RANK fact, invariant under ANY scalar coupling — the conclusion is **Λ_f-independent**.

**[CONFIDENCE: HIGH]** — Three genuinely independent checks: (i) the v18 16-vs-6 support reproduced exact over Q via the verifier-hardened v18 harness; (ii) the decisive off-T over-determination (10 entries where G≠0, T=0, forcing a single scalar Λ to be 4 distinct values, computed exact over Q, κ-free); (iii) the single-global (κ,Λ) solve is EmptySet for the induced κ, for κ free, AND for the v18 frozen rational κ — three independent solves all agree. The scalar-invariance-of-support lemma is elementary (κ≠0 ⇒ κT_{μν}≠0 iff T_{μν}≠0). The one residual risk (a non-generic anchor) is excluded: the family has 18 matter-bearing points and the failure is structural (off-T block) not a single-point accident.

---

## The reproduced (n_G, n_T) and the decisive numbers (exact over Q)

### Support counts at the matter-bearing anchor M_0 (V_{1/2} survivors [11,18,19,26]):
| Quantity | Value (exact Q) | Meaning |
|---|---|---|
| R[g=e.e](M_0) | `14187524733311967018208791837/634906109300195099205387025` ≠ 0 | matter-bearing (ρ>0), NOT M=0 deflated |
| **n_G** | **16** | G[g] supported on ALL 16 entries of the 4×4 lower-index array (the v18 "16") |
| **n_T** | **6** | T[ψ] supported on `{01,10,22,23,32,33}` only — a thin fragment (the v18 "6") |
| ψ (primary scalar) | `11p/50 − 7q/50` (real) | from 2Re((x₂x₁)x₃), AST-guarded (no Ric/R/G) |
| **v18 16-vs-6 reproduced** | **True** | n_G==16, n_T==6, T_support=={01,10,22,23,32,33} — matches verifier-hardened v18 Ph77 |

> **Note on the definition:** "16" and "6" are the counts of **nonzero entries of the 4×4 lower-index array** at the matter-bearing anchor — NOT "10 symmetric slots". This is the v18 PRECISE definition (`cartan_phaseB_einstein.py` lines 589-590), reproduced here, not assumed. The actual reproduced integers are **(n_G, n_T) = (16, 6)**.

### The induced κ (carried from Gate 1, NOT recomputed):
| Quantity | Value | Source |
|---|---|---|
| c_1 | `1/(6π²)` | Gate 1 (on the Gate-0 STr=+8/3) |
| **κ (induced)** | **`6π²/Λ_f²`** (scalar) | κ⁻¹ = c_1 Λ_f² |
| G | `3π/(8Λ_f²)` > 0 | consistent with Gate 0 |
| Λ_f | symbolic (Gate-3 scope) | NOT pinned — and the verdict is Λ_f-INDEPENDENT |

### Scalar-invariance of support (a scalar cannot change tensor rank):
| Check | Result |
|---|---|
| support(induced-κ · T) == support(T) | **True** (6 == 6) — Λ_f-independent |
| support(κ_symbolic · T) == support(T) | **True** (6 == 6) — any nonzero scalar |
| support(κ · T) == support(T), rational panel (8 scalars) | **True** (corroboration, non-decisive) |

### The decisive off-T over-determination (the real kill — NOT naive support coverage):
- g = e.e is **DENSE** (16/16 entries nonzero), so support(κT + Λg) = support(T) ∪ support(g) = the full 16. Adding Λg DOES reach every entry as a support set — naive coverage is NOT the obstruction.
- **off-T entries** (G≠0 but T=0): **10** of them (`{00,02,03,11,12,13,20,21,30,31}`). There κT+Λg = Λg, so **κ drops out entirely**.
- required Λ = G_{μν}/g_{μν} on the off-T block: **4 DISTINCT values** (a single scalar Λ needs exactly 1) → **no scalar (κ,Λ) works**.

### The single-global (κ,Λ) solve over the matter-bearing family (18 pts, 0 dropped):
| Solve | Result | Meaning |
|---|---|---|
| both (κ,Λ) FREE (180 eqs, 2 unknowns) | **EmptySet** | no global linear-in-T Einstein closure at all (strongest test) |
| κ = induced 6π²/Λ_f² (Λ free) | **EmptySet** + every per-point residual ≠ 0 | the induced scalar does NOT close (a RESTRICTION of the free solve) |
| v18 frozen RATIONAL κ_ψ = a₄/[t⁴ tr T] | **EmptySet** | reproduces the verifier-hardened v18 Ph77 negative |
| **Gate-2 == v18 (both inconsistent, both 16-vs-6)** | **True** | the induced scalar REPRODUCES, not REPAIRS, the v18 mismatch |

---

## Non-hardwired verdict + 3 self-tests (pre-empts the v20 hardcoded-boolean bug)

The DEAD/SURVIVES category is DERIVED from the actual `(n_G, n_T)`, the containment `support(G) ⊆ support(κT)`, and the solve consistency — NOT a hardcoded literal:
- **DEAD** iff support(G) ⊄ support(κT) OR the single-global solve is inconsistent.
- **SURVIVES** iff support(G) ⊆ support(κT) AND the solve is consistent (the surprise branch).

| Self-test | Input | Output |
|---|---|---|
| (a) | synthetic matching supports (n_G≤n_T+1) + consistent solve | **SURVIVES** ✓ |
| (b) | the real mismatched supports (16 vs 6) + inconsistent solve | **DEAD** ✓ |
| (c) | literal-detector: two input sets → two categories (SURVIVES vs DEAD) | **not a literal** ✓ |

Source/runtime guards: no numpy.linalg / float / thermodynamic token on any decisive function (AST-checked, docstrings/comments stripped); octonion_algebra.py absent; det SSOT = ring_lemma_verification.det_3 exact-Q. The guard FIRES on an injected numpy.linalg/float violation (proven not a no-op).

---

## Honest framing

**Gate 2 DEAD means the Sakharov route dies exactly where v18 died** — the induced scalar κ cannot repair a tensor-RANK mismatch. A scalar coupling multiplies T by a number; it leaves the off-T block (where the matter stress vanishes but G does not) untouched, and there a single cosmological Λ is over-determined. This was structurally expected (a scalar cannot change rank), and we confirmed it exactly over Q on matter-bearing profiles.

Had the induced κ instead made G = κT + Λg consistent, that would have been a **major surprise** (a scalar repairing a rank mismatch) → the non-hardwired verdict machinery would have reported SURVIVES at true strength and flagged that Gate 3 (CLOSURE) must run. The math says DEAD.

This is a DEAD at true strength of **the third of four gates** — the milestone-decisive one. Gates 0/1 certified the induced coupling has the right sign and a clean ∫R curvature term; Gate 2 shows that is not enough: the induced scalar cannot supply the tensor structure the extremized Einstein equation demands.

---

## What it means for the selection-law ledger

**Route C / kind-4 (induced action) gravity is DEAD for h_3(O).** The Sakharov-induced scalar κ — having survived the sign (Gate 0) and curvature-cleanliness (Gate 1) gates — cannot repair the v18 16-vs-6 tensor-support mismatch (Gate 2), exactly as the ledger predicted. **The six-kind selection-law menu (read-off / intrinsic-curvature / enlarge / induced / constraint / spectral·thermo) is now EXHAUSTED for h_3(O).**

Per `selection-law-ledger.md` §6, the redirect is FORCED by exhaustion (not chosen out of fatigue):
- **(A) Accept the program's real scope** — self-modeling forces the spacetime arena + QM (Paper 5) + the SM matter content (Paper 7), but the gravitational LAW is genuinely **separate** (imported; Penrose/'t Hooft territory). Outcome = "QM + Standard Model on flat KKT spacetime, gravity its own thing" = **incomplete-TOE, not failed-program.** This is the verdict the v17/v18/v19/v20 four-corner triangulation already supports, now sealed by the induced-action close-out.
- **(B) Find a selection-law kind NOT on the six-kind menu** — a high bar (genuinely new physics); must route to a published mechanism the menu missed, not to a story.

Combined gravity verdict across the program: v17 NONE / v18 fp-imported-action / v19 fp-no-intrinsic-orientation / v20 fp-imported-action / **v21 Gate-2 DEAD (induced-action support mismatch)** — every metric-selection kind tried fails. **Gravity is separate.**

---

## One line per gate (the ledger ladder)

| Gate | Status | Result |
|---|---|---|
| **Gate 0 (SIGN)** | DONE | SURVIVES (G>0, STr=+8/3, unforced, circularity=False) |
| **Gate 1 (a_1 ∝ R)** | DONE | PASS (a_1=-R/3 clean ∝ R; c_1=1/(6π²); G=3π/(8Λ_f²)>0) |
| **Gate 2 (SUPPORT MISMATCH)** | **DONE** | **DEAD** (induced scalar κ=6π²/Λ_f² does NOT repair the v18 16-vs-6; n_G=16/n_T=6 reproduced; all 3 single-global solves EmptySet; Λ_f-independent) |
| **Gate 3 (CLOSURE)** | NOT RUN | Gate 2 DEAD ⇒ six-kind menu exhausted; redirect per ledger §6 |

---

## Deviations

- **[Rule 1 — code bug]** First run raised `NameError: name 'G' is not defined` in `scalar_invariance_of_support` (referenced `G[μ,ν]` on the off-T block without pulling `G` from the `rep` dict). Fixed by adding `G = rep["G"]` (the anchor-evaluated Einstein matrix). Verified: re-run clean, exit 0.
- **[Rule 4 — correctness, not scope]** Initial off-T check (2d) naively asserted `support(κT + Λg) does NOT cover support(G)`, which latched a false FAIL because g = e.e is DENSE (fills all 16 entries). Corrected the physics: the decisive obstruction is NOT support-set coverage but the **off-T over-determination** (on the 10 entries where T=0, G=Λg forces one scalar Λ to be 4 distinct values, κ-independent). This is the physically correct, verifier-defensible mechanism and matches the v18 EmptySet solve. The verdict (DEAD) was unchanged; only the supporting argument was corrected to be sound.

---

## Reproducibility

- SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0 (no RNG on any decisive path; one fixed-seed `random.Random(20210606)` rational panel for the NON-decisive scalar-invariance sweep only).
- `code/sakharov_gate2_support.py` runs foreground `python3 -u` (~50s; the heavy calls are the 18-point family build and the v18 cross-check interpolation). Byte-identical decisive output across two runs (verified); exit 0; no float on any decisive path.
- octonion_algebra.py BANNED (buggy float associator); warm v18 harness `cartan_phaseB_einstein.py` + `bulk_geometry_verification.py` + `ring_lemma_verification.py` reused; the independent AST-guarded T[ψ]/T_σ reused verbatim from v18. The surd-laden matter tetrad's symbolic dω hits the >200s watchdog cliff, so R[ω] is delivered via the harness's provably-equal metric-Levi-Civita route exactly as v18-Ph77 did (the symbolic spin connection is NOT brute-forced).

## NOTE

This is the EXECUTOR's reading of the mechanical Gate-2 checks. The ORCHESTRATOR/VERIFIER adjudicates the milestone verdict and any transition.

---

## Self-Check: PASSED

- Created files exist: `code/sakharov_gate2_support.py`, `derivations/81-sakharov-gate2.tex`, `derivations/81-gate2-SUMMARY.md` — all FOUND.
- Driver + tex commits exist: `49d8893f` (driver), `55bea0c0` (tex) — both FOUND.
- Driver re-run reproduces the decisive numbers reported here exactly: n_G=16, n_T=6, v18 16-vs-6 reproduced=True, off-T entries=10, distinct off-T Λ=4, all three single-global solves=EmptySet, Gate-2==v18 agree=True, VERDICT=DEAD, ALL_PASS=True, exit 0.
- LaTeX well-formed: environments balanced, braces balanced, all `\ref` resolve to defined `\label` targets (pdflatex unavailable in-env — NOT compiled).
- Byte-identical decisive output across runs (verified via diff with timing lines stripped); no float on any decisive path.
- Convention consistency: mostly-minus (+,-,-,-), g=e.e (1,3), gravity = R[ω], exact-over-Q — matches the convention_lock and the Gate-0/1 drivers.
- Domain (GR) final checks: the test is on the linear-in-Riemann object G[g]=Ric-(1/2)gR vs an independent T[M] (the RIGHT object — not a quadratic-in-F tautology); matter-bearing (ρ>0), NOT the M=0 deflated check; the negative is structural (off-T rank fact), reported at true strength.
