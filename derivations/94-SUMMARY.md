# Phase 94 (v34.0) — BASE-SAKHAROV ON THE VARIETY: gate-by-gate SUMMARY

> **DERIVED VERDICT: CLOSES-CONDITIONAL** (G1–G3 PASS, G4 = NOT-YET-FORCED). The INDUCE route does
> NOT die on the variety the way it died on the v21 fiber (the rank wall is cleared, ε=20), and it
> does NOT force a gravitational law either: the frozen FS geometry IS self-consistent under its own
> matter loop and closes on the v33 source, so the entire gravity gap collapses to the single
> state-fp ⟹ metric-fp clamp (Paper 5), which is NOT-YET-FORCED. Exact over Q/Q(i) on every decisive
> path; mpmath used only as explicit cross-checks. Completes the Block-C gravity confrontation — both
> ways to manufacture a law (EXTREMIZE = v33 FORCES-NOTHING; INDUCE = this) now run.

**Driver:** `code/sakharov_variety.py` (one foreground `python3 -u` invocation, ~0.1 s for G1–G4;
G0 re-confirmed via the certified `gate0_v33.py` + `lichnerowicz_response_fingerprint.py`). The
`verdict()` ladder is DERIVED from the gate booleans (non-hardwired) with 7 self-tests.

---

## Gate table

| Gate | PASS | Result (exact over Q) |
|---|---|---|
| **G0** foundation + machinery freeze | **PASS** | ε = λ_L − 2Λ = 32 − 12 = **20** (rank-compatible, Trap #26 cleared); v32 fingerprints T1/T2/all 5 norms/the 5:4 split reproduce |
| **G1** the heat kernel (core) | **PASS** | E = 0 minimal scalar (3 contamination checks); Gilkey a₁ = A₂ = tr(E+R/6) = **R/6 = 4**; attractive 3-way; κ_ind = (1/(12π²))Λ_f², G_ind = (3π/4)/Λ_f² > 0 |
| **G2** self-consistency (the FORK) | **PASS** (not over-determined) | ζ(0) = **−89/120**; Gilkey tie A₄/(4π)² = **31/120**; A₂/A₀ = R/6 = 4, A₀ = π²/2 = Vol; **Λ_cc = (3/2)Λ_f²** (N cancels); FS critical ⟺ **Λ_f² = 4**; over-determined = **False** (NOT the rank wall). Two readings emitted; REC = PASS-conditional, **FLAGGED for human ratification** |
| **G3** closure on the source | **PASS** | Besse 4.60: TT Hess(a₁) = (Δ_L − 2Λ); reuse ε = 20 ⇒ h = κ_ind·TT(B3)/20, well-defined; **κ_ind FREE** (no negative-weight h₃(O) invariant) |
| **G4** the clamp audit | classify | computation NATIVE (ζ′(0) of the program's own spectrum); principle = state-fp ⟹ metric-fp bridge **NOT-YET-FORCED** (no Paper-5 proof; Trap #28 seam kept typed-distinct) |

**verdict() inputs:** G1_clean_attractive = True, G2_not_over_determined = True, G3_closes = True,
G4 = NOT-YET-FORCED ⇒ **CLOSES-CONDITIONAL**. All 7 self-tests pass (wrong-sign G1 ⇒ DOESN'T-CLOSE;
over-determined G2 ⇒ DOESN'T-CLOSE; G3 no-closure ⇒ DOESN'T-CLOSE; CLOSES-FORCED only on G4=FIT;
NOT-YET-FORCED ⇒ CONDITIONAL; IMPORT ⇒ IMPORTS-QFT; Trap #25 guard NOT-YET-FORCED ≠ FORCED).

---

## G0 — foundation + machinery freeze (re-confirmed)

ε is the rank-compatibility input that distinguishes this run from the dead v21 fiber (Trap #26).
Re-confirmed (both certified drivers run PASS, exit 0):

- `gate0_v33.py` → controls C1/C2a/C2b/REG **all PASS**; Δ_L r = 32·r EXACT on **every** Kähler block
  (H20, H11, H02) for all four directions s01, a01, d1, GEN=d2 (detM = −2 ≠ 0). ⇒ λ_L = 32,
  **ε = λ_L − 2Λ = 32 − 12 = 20.**
- `lichnerowicz_response_fingerprint.py` → **T1 PASS, T2 PASS**, all 5 norm directions exact
  (‖TT(B3)‖² = (1/30)(TrM²)²), the **5:4 split** exact (‖r₁₁‖²:‖r_anti‖² = (1/54):(2/135) of (TrM²)²,
  ratio 5/4) on s01 and a01 (and the remaining directions). The slow T3 Gram (rank 6, ~40 min) is the
  structural re-confirmation only; the decisive freeze checks reproduced byte-for-byte over Q.

**G0 PASS ⟺ ε = 20 reproduced AND the fingerprints reproduce: True.**

---

## G1 — the heat kernel (the core computation)

### The fluctuation operator is the minimal massless scalar Laplacian (E = 0), confirmed not assumed

Three contamination criteria (Trap #27), all confirmed against the variety matter-field code:

1. **No ξR|φ|² (ξ = 0).** The variety matter action is the free Dirichlet energy ∫|∇φ_M|²√g:
   `variety_sourced_field_equation.py` B1/B3 show the matter equation **(Δ + λ₁)G_M = source is
   LINEAR** ⇒ the action is quadratic ⇒ a free field, no non-minimal coupling. The dialable scalar
   coefficient is (1/6 − ξ); at ξ = 0 it is exactly **+1/6**.
2. **No wave-map target curvature.** The moments φ_a = Tr(M·P) are **LINEAR** in the SU(3)-adjoint
   embedding (`variety_moment_doublet.py` C2: φ_Y(p) = ⟨Y,p⟩ linear) ⇒ flat target ℝ⁸ ⇒ no
   sigma-model target-curvature term injected into E.
3. **No non-associativity leak.** The base field lives on CP² = h₃(C_u), the COMPLEX cut; the scalar
   Laplacian is associative-algebra-clean (the v18/v20 non-associative MM corpse is a FIBER object;
   the background is the torsion-free Levi-Civita FS connection, a clean Laplace-type Δ).

⇒ **E = 0**, Δ = −g^{μν}∇_μ∇_ν, minimal, no mass, no curvature endomorphism, no gauge connection.

### Gilkey / Seeley–DeWitt a₁ = the only-E-and-R structure

`Tr e^{−tΔ} ~ (4πt)^{−2} Σ_n t^n A_{2n}`; the prompt's a₁ = Gilkey's A₂ = tr(E + R/6). At E = 0:

> **a₁ = R/6 = 24/6 = 4** (per real d.o.f.), R-coefficient **+1/6**, background-independent.

The curvature-squared invariants R²/Ric²/Riem²/□R/tr F² are strictly a₂(=A₄)-level, so they
**cannot contaminate a₁** (Gilkey's theorem: a₁ contains ONLY E and R·𝟙).

### The attractive sign — three ways (Trap #27)

1. **Gilkey** a₁ = R/6 = +4 (positive R-coefficient +1/6).
2. **Frolov–Fursaev / Visser spin-weight table**: the minimal-scalar unit is +1/6 (bosonic,
   statistics s = +1 — no two-minus subtlety, unlike the v21 Dirac fermions).
3. **Direct**: E = 0 leaves only the universal +R/6 ⇒ positive.

⇒ 1/(16πG_ind) > 0 ⇒ **G_ind > 0 (attractive)**.

### Induced couplings (coefficient count/scheme-dependent, NOT load-bearing — flagged)

With N = 8 (the adjoint-valued moment field, λ₁ = 8 on CP²):

- **κ_ind = 1/(16πG_ind) = (N·(1/6)/(4π)²)·Λ_f² = (1/(12π²))·Λ_f²** ⇒ G_ind = (3π/4)/Λ_f² > 0.
- **Λ_ind = ρ_Λ,ind ~ Λ_f⁴·N** (magnitude scheme-dependent).

**G1 PASS ⟺ (E = 0 clean, 3 contamination checks) AND (a₁ ∝ R, attractive 3-way): True.**

---

## G2 — the self-consistency test (the GENUINE FORK, real teeth)

### The CP² scalar Laplacian spectrum (exact over Q)

`λ_k = 4k(k+2)`, `d_k = (k+1)³`: [(0,1), (12,8), (32,27), (60,64)]. Assert λ₁ = 12/d₁ = 8 and
λ₂ = 32/d₂ = 27 ✓.

### ζ(0) = −89/120 (exact, the decisive anchor) + the heat-kernel computation shown

ζ(s) = Σ_{k≥1} d_k λ_k^{−s} = Σ_{k≥1}(k+1)³[4k(k+2)]^{−s}. Shift n = k+1 ≥ 2, k(k+2) = n²−1:

> ζ(s) = 4^{−s} Σ_{n≥2} n³(n²−1)^{−s} = 4^{−s} Σ_{j≥0} (s)_j/j! · [ζ_R(2s+2j−3) − 1]

(using (1−x)^{−s} = Σ_j (s)_j/j! x^j with x = n^{−2}). **At s = 0, only j = 0 and j = 2 survive:**

- **j = 0:** (s)₀/0! · [ζ_R(2s−3) − 1] → ζ_R(−3) − 1 = 1/120 − 1 = **−119/120**.
- **j = 2:** (s)₂/2! = s(s+1)/2; [ζ_R(2s+1) − 1] has the pole ζ_R(2s+1) ~ 1/(2s); the product
  → (s+1)/4 → **+1/4** at s = 0 (the −1 part is killed by the explicit s factor).
- **j = 1, j ≥ 3:** O(s) × finite → 0.

> **ζ(0) = −119/120 + 1/4 = −89/120.**

**Gilkey tie:** A₄/(4π)² = ζ(0) + dim ker = −89/120 + 1 = **31/120** ✓.

**mpmath cross-checks (NOT decisive paths):**
- ζ(0) numeric = −0.741666666667 = −89/120 (the j=2 pole ~ 1/(2s) is odd in s, so the +ε/−ε average
  of the continuation series cancels it and exposes the finite value to 12 digits).
- Small-t heat kernel (4πt)²Σ d_k e^{−tλ_k} → A₀ + A₂t + A₄t² (3-pt Richardson): **A₂/A₀ = 3.99983
  → R/6 = 4** and **A₀ = 4.934803 → π²/2 = 4.934802 = Vol(CP², Ric=6g)** — independently confirming
  the spectrum reproduces R = 24.

### The cc-matching (Sakharov/cutoff scheme), exact over Q in Λ_f

Per d.o.f.: 1/(16πG) ∝ (1/6)Λ_f² (quadratic a₁ divergence) and ρ_Λ ∝ (1/2)Λ_f⁴ (quartic a₀
divergence). Writing Γ = (1/16πG)∫(R − 2Λ_cc)√g:

> **Λ_cc = (3/2)Λ_f²** — the field-count N CANCELS in the ratio.

On the Einstein background FS, R_μν = 6g, R = 24 ⇒ R_μν − ½Rg = −6g, so the vacuum equation
R_μν − ½Rg + Λ_cc g = 0 ⟺ **Λ_cc = 6 = Λ_geo** ⟺ **Λ_f² = 4** (the cutoff = the curvature scale).

### The fork — and why it is NOT the rank wall (Trap #26)

The matching is **ONE condition (the scale/volume mode) with ONE knob (Λ_f)** ⇒ ALWAYS solvable
(Λ_f² = 4) ⇒ **over-determined = False**. Contrast the v18/v21 death: 10 OFF-T entries
over-determined ONE scalar to 4 distinct rationals ⇒ EmptySet (an over-determination a scalar κ
cannot repair). There is no such over-determination here — the source is the clean ε = 20
eigentensor (G0), and the cc-matching is a single scalar equation.

### The two readings (emitted; do NOT silently pick — FLAGGED for human ratification)

- **[A] G2 = PASS (field-faithful, conditional) [EXPECTED, RECOMMENDED]:** FS IS a critical point of
  its own induced action at the natural/only scale (Λ_f² = 4); the scale-identification is folded
  into the G4 not-yet-forced clamp ⇒ contributes CLOSES-CONDITIONAL.
- **[B] G2 = soft-FAIL (Λ-mismatch):** if one DEMANDS a content-forced cancellation (Λ_ind = Λ_geo
  without scale-tuning) — 8 bosons, no fermionic partner, ζ(0) ≠ 0 so the anomaly does not vanish —
  then the induce route does not close on its own ⇒ leans DOESN'T-CLOSE.

**The honest content:** FS IS a critical point of its own induced action at the natural scale, but
the match is a **SCALE-IDENTIFICATION (the cosmological-constant problem reframed), NOT a forced
content cancellation.** This is a genuine judgment — **FLAGGED for human ratification.** It is NOT
the hard DOESN'T-CLOSE that an over-determination would force.

**G2 PASS (not over-determined) = the decisive fork fact AND the anchors reproduce: True.**

---

## G3 — closure on the source (follows from a clean G1)

**Besse, *Einstein Manifolds* 4.60:** the TT (transverse-traceless) Hessian of a₁ = ∫R√g on an
Einstein background IS the Lichnerowicz operator **(Δ_L − 2Λ)** (the second variation of the total
scalar curvature). v33 Gate-0 gives (Δ_L − 2Λ) = ε = **20** on r = TT(B3). So the induced field
equation is

> (Δ_L − 2Λ) h = κ_ind·TT(B3) ⇒ **h = κ_ind·TT(B3)/20**, well-defined (ε ≠ 0).

Closure FOLLOWS from G1 producing a clean ∫R (ε = 20 REUSED, not recomputed).

**Is κ_ind forced?** κ_ind = 1/(16πG_ind) ~ Λ_f². The framework grading R[h₃(O)]^{F₄} is free on
POSITIVE-degree generators Tr/Tr²/det₃ with no negative-weight invariant (v20/v21; det₃ ≡ 0 on the
Lorentz block) ⇒ no dimensionful scale ⇒ **κ_ind is a framework ratio set by the cutoff Λ_f, NOT
forced** unless Paper 5 forces Λ_f.

**ASYMMETRY:** the stiffness ε = 20 is a FORCED framework number; the coupling κ_ind is a FREE scale.
This is exactly the "closes on the source but does not force the law" of CLOSES-CONDITIONAL.

**G3 PASS on stiffness (ε = 20 closure), κ_ind FREE: True.**

---

## G4 — the clamp audit (the honest gate, load-bearing)

- **(a) The COMPUTATION is NATIVE.** The one-loop determinant is ζ′(0) of the matter Laplacian whose
  spectrum (λ₁ = 12, λ₂ = 32, …) the program ALREADY uses (v25–v33, Gate-0). The heat-kernel
  coefficients are spectral data of the frozen geometry ⇒ the effective-action MACHINERY is native
  (imports-as-math, like the rest of the program). NOT IMPORTS-QFT.
- **(b) The PRINCIPLE is the clamp.** "The system sits at the extremum of Γ[g]" = the
  **state-fp ⟹ metric-fp** bridge (Paper 5: ρ_J the φ-iteration attractor forces δΓ/δg = 0).
  **SEAM (Trap #28):** state-fp lives on ρ_J ∈ h₃(O) (the algebra); metric-fp lives on g (the
  geometry) — typed-distinct. The bridge is the thing to PROVE, never to assume. No proof exists in
  the corpus ⇒ default **NOT-YET-FORCED.**

**Trap #25 (the big one):** a load-bearing clamp is NOT relabeled "conditional and shipped" as
native — it is FIT (exhibit the forcing) or flagged not-forced. **CLOSES-CONDITIONAL is the honest
CEILING absent the Paper-5 fit; STOP at NOT-YET-FORCED, do NOT glaze to CLOSES-FORCED.**

---

## Deviations from the RESEARCH's expected numbers

**None.** Every load-bearing number reproduced exactly:

| Quantity | RESEARCH expected | Computed | Match |
|---|---|---|---|
| ε (rank compatibility) | 20 | 20 | ✓ |
| E (curvature endomorphism) | 0 | 0 | ✓ |
| a₁ R-coefficient | +1/6 (a₁ = R/6 = 4) | +1/6 (= 4) | ✓ |
| sign | attractive (3-way) | attractive (3-way) | ✓ |
| κ_ind/Λ_f² | (1/(12π²)) [count-dependent] | 1/(12π²) | ✓ |
| ζ(0) | −89/120 | −89/120 | ✓ |
| Gilkey tie A₄/(4π)² | 31/120 | 31/120 | ✓ |
| A₂/A₀ (heat-kernel) | R/6 = 4 | 3.99983 → 4 | ✓ |
| A₀ (heat-kernel) | π²/2 = Vol | 4.934803 = π²/2 | ✓ |
| Λ_cc | (3/2)Λ_f² (N cancels) | (3/2)Λ_f² | ✓ |
| FS-critical Λ_f² | 4 | 4 | ✓ |
| over-determined? | False (not the rank wall) | False | ✓ |
| κ_ind forced? | FREE (no neg-weight invariant) | FREE | ✓ |
| G4 classification | NOT-YET-FORCED | NOT-YET-FORCED | ✓ |
| verdict | CLOSES-CONDITIONAL | CLOSES-CONDITIONAL | ✓ |

---

## Confidence

**[CONFIDENCE: HIGH]** on the spectrum, the heat-kernel coefficients, the attractive sign, ζ(0) =
−89/120 (exact analytic continuation + two independent numerical cross-checks: pole-odd average and
the small-t heat-kernel A₂/A₀ = 4), ε = 20 (v33 Gate-0, control-validated), and the fork being a
scale-identification not a rank-wall over-determination.

**[CONFIDENCE: MEDIUM — flagged for human ratification]** the G2 PASS-vs-soft-FAIL judgment (whether
"FS critical at the only scale" counts as G2-PASS or as a soft Λ-mismatch) and the G4 NOT-YET-FORCED
clamp (the honest default absent a Paper-5 proof of state-fp ⟹ metric-fp). Both are emitted with
both readings; neither is silently picked.

---

## Fences (binding, verbatim)

NO Einstein-equation / G=κT / gravity / Newton / dark-matter / geodesic language as a DERIVED result;
κ is a framework ratio (Λ_f-set), NOT Newton's constant; FS is USED, not derived; signature
Riemannian (Wall 2 unpaid — NOTHING is called gravity, even under CLOSES-FORCED, until signature is
paid); CLOSES-CONDITIONAL is NOT a derivation. v34 does NOT retract v33 (extremize route stays dead)
or v17–v21 (the fiber kills stand). Paper 5 remains the only result in the more-than-nothing column.
Three-path verification standing; milestone HOLD for human ratification; do NOT self-register v35.

---

## Reproducibility

sympy 1.14.0, mpmath 1.3.0, Python 3.14.5, Darwin arm64. Exact rational arithmetic over Q/Q(i) on
every decisive path (no RNG / no seeds in any verdict path); floats illustrative only; the mpmath
numerical evaluations (ζ(0), A₂/A₀, A₀) are explicitly CROSS-CHECKS, not decisive paths. The G0
ε = 20 + fingerprints are the certified `gate0_v33.py` + `lichnerowicz_response_fingerprint.py`
(re-run PASS, exit 0). `code/.p92_basis_images.pkl` disk cache reused for `extract_tt`.

## Artifacts

- `code/sakharov_variety.py` — the driver: G0 (reuse/confirm) … G4, exact over Q, the non-hardwired
  `verdict()` ladder + 7 self-tests, prints the auditable gate table. One foreground
  `python3 -u code/sakharov_variety.py` invocation (exit 0).
- `derivations/94-SUMMARY.md` — this file.
- `derivations/94-VERDICT.md` — the taxonomy verdict with the G2 fork + G4 clamp flagged.
