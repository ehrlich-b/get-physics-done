---
phase: 94-base-sakharov-variety
verified: 2026-06-14T00:00:00Z
status: passed
score: 7/7 load-bearing claims independently confirmed
consistency_score: 11/11 physics checks passed
independently_confirmed: 7/7 load-bearing claims independently confirmed (separate code path + literature)
confidence: high
verdict_agreement: CLOSES-CONDITIONAL — INDEPENDENTLY CONFIRMED (G1-G3 pass, G4 = NOT-YET-FORCED)
comparison_verdicts:
  - subject_kind: acceptance_test
    subject_id: zeta0-cp2-scalar
    reference_id: gilkey-a4-curvature-invariants
    comparison_kind: cross-method
    verdict: pass
    metric: "zeta(0) via Gilkey a_4 from independent real-coordinate Riemann (5R^2-2Ric^2+2Riem^2)"
    threshold: "== -89/120 exact over Q (A_4/(4pi)^2 = 31/120)"
  - subject_kind: acceptance_test
    subject_id: zeta0-cp2-scalar
    reference_id: heatkernel-smallt-continuation-free
    comparison_kind: cross-method
    verdict: pass
    metric: "zeta(0) via heat-kernel small-t constant term (independent of any analytic continuation)"
    threshold: "== -89/120 to 9+ digits; c_-2=1/32, c_-1=1/8 fall out"
  - subject_kind: claim
    subject_id: kretschmann-Riem2-192
    reference_id: cp2-fubini-study-kretschmann-literature
    comparison_kind: literature
    verdict: pass
    metric: "|Riem|^2 of CP^2 (Ric=6g) vs literature K = (16/3)Lambda^2"
    threshold: "== 192 (Lambda=6); independent Riemann == literature Kretschmann"
  - subject_kind: acceptance_test
    subject_id: gate-0-eps-20
    reference_id: independent-real-lichnerowicz-operator
    comparison_kind: cross-method
    verdict: pass
    metric: "Delta_L(Hess R_M) eigenvalue, independent real-coordinate operator (v33 indep_lich.py)"
    threshold: "== 32 on all 16 entries, 2 points, exact/Q => eps = 32-12 = 20"
  - subject_kind: claim
    subject_id: besse-tt-second-variation
    reference_id: einstein-metric-stability-literature
    comparison_kind: literature
    verdict: pass
    metric: "TT second variation of Int R = (1/2)(nabla*nabla - 2Rdot) = (1/2)(Delta_L - 2Lambda)"
    threshold: "Einstein operator Delta_E = Delta_L - 2Lambda confirmed in stability literature"
  - subject_kind: claim
    subject_id: minimal-scalar-attractive-sign
    reference_id: visser-sakharov-modern-perspective
    comparison_kind: literature
    verdict: pass
    metric: "minimal scalar a_2 = R/6 > 0 => 1/(16piG) > 0 => attractive (bosonic)"
    threshold: "positive Newton constant for the bosonic minimal scalar"
suggested_contract_checks: []
---

# Phase 94 (v34.0) — VERIFICATION: BASE-SAKHAROV ON THE VARIETY (the INDUCE route)

**Independent verifier (gpd-verifier, path 2 of 3), separate code path + web literature.** Verdict
**CLOSES-CONDITIONAL — INDEPENDENTLY CONFIRMED.** Every load-bearing claim was re-derived by a
method that shares zero code with the executor's driver, or cross-checked against the published
literature. The DECISIVE anchor ζ(0) = −89/120 is confirmed **three independent ways** (Gilkey a₄
from my own real-coordinate Riemann tensor, a continuation-free heat-kernel small-t fit, and an
analytic pole-subtraction distinct from the executor's ±ε average). The rank-compatibility input
ε = 20 is re-certified by my v33 from-scratch real-coordinate Lichnerowicz operator. Confidence:
**HIGH** on the spectrum, the heat-kernel coefficients, ζ(0), the attractive sign, ε = 20, and the
fork being a scale-identification (not a rank-wall over-determination); **MEDIUM** (correctly
flagged for human ratification, not a verifier call) on the G2 PASS-vs-soft-FAIL judgment and the G4
NOT-YET-FORCED clamp.

---

## 0. Scope, independence, fences carried

- **Riemannian** computation (CP² Fubini–Study, Ric = 6g, positive-definite). Consistent with the
  convention lock (the lock's mostly-minus Lorentzian signature applies to the bulk/slice, not to
  this base-deformation-complex computation). **Wall 2 (signature) is unpaid** and carried as a fence.
- **My independence:** ζ(0) is verified from the **curvature invariants** of my own from-scratch
  real-4D Riemann tensor (the v33 `indep_curv`/`indep_lich` pipeline), NOT from the executor's
  spectral-zeta analytic continuation; the numeric cross-check uses a continuation-free heat-kernel
  fit; ε = 20 is my own real-coordinate Lichnerowicz operator (zero shared code with the complex
  frame); the verdict ladder is independently re-implemented and checked to agree on all input combos.
- **Scripts written this phase:** `code/indep_zeta0_gilkey.py` (ζ(0) via Gilkey a₄ / curvature
  invariants, exact/Q), `code/indep_zeta0_heatkernel.py` (ζ(0) continuation-free numeric),
  `code/indep_sakharov_checks.py` (spectrum, a₁, cc-matching logic, verdict ladder),
  `code/indep_reconcile.py` (minimal-vs-conformal, Besse, Kretschmann literature). Reused warm:
  `code/indep_lich.py`, `code/indep_su3_reps.py` (v33).
- **FENCES (carried, binding):** NO Einstein-equation / G=κT / gravity / Newton / dark-matter /
  geodesic as a DERIVED result; κ is a framework ratio (Λ_f-set), NOT Newton's constant; FS is USED,
  not derived; Riemannian (Wall 2 unpaid); CLOSES-CONDITIONAL is NOT a derivation; v34 does NOT
  retract v33 (extremize stays dead) or v17–v21 (fiber kills stand); **Paper 5 remains the only
  more-than-nothing result.** Verified honored in §8.

---

## 1. The seven load-bearing claims — INDEPENDENT verification table

| # | Claim | My INDEPENDENT method (separate path / literature) | Result | Verdict |
|---|---|---|---|---|
| **1** | **ζ(0) = −89/120** (the DECISIVE G2 anchor) | (a) Gilkey a₄ from MY OWN real-coord Riemann invariants: A₄=(1/360)(5R²−2Ric²+2Riem²)Vol; (b) continuation-free heat-kernel small-t fit; (c) analytic pole-subtraction ≠ executor's ±ε average; (d) literature a₄ formula + Kretschmann | (a) **31/120 − 1 = −89/120 EXACT/Q**; (b) **−89/120 to 9 digits**; (c) **−89/120 exact**; (d) confirmed | **PASS — 3 indep ways** |
| **2** | **λ_k = 4k(k+2), d_k = (k+1)³** | Weyl dim formula SU(3)(k,k) = (k+1)³ for k=0..5; literature CP^n λ_k=4k(k+n) | d_k=(k+1)³ all k; λ₁=12/d₁=8 (adjoint), λ₂=32/d₂=27, λ₃=60/d₃=64 | **PASS** |
| **3** | **G1 minimal scalar a₁ = R/6, attractive** | Gilkey tr(E+R/6) at E=0 = R/6 = 4; contamination = only-E-and-R structure; Visser/FF sign | a₁=R/6=+4, coeff +1/6>0; conformal (E=−R/6) would DIFFER ⇒ minimal is the right object | **PASS** |
| **4** | **ε = 20** (Trap #26 rank compatibility) | My v33 from-scratch real-4D Lichnerowicz operator on Hess(R_M), 2 pts, exact/Q | **Δ_L = 32 on all 16 entries** ⇒ ε = 32 − 12 = **20** | **PASS** |
| **5** | **G2 over-determined = False** | Independent linear-algebra: Λ_cc=(3/2)Λ_f² (1 eqn), Λ_cc=6 ⇒ Λ_f²=4 unique; contrast x=1∧x=2 ⇒ EmptySet | 1 condition / 1 knob ⇒ always solvable; NOT the v18/v21 rank wall | **PASS** |
| **6** | **G3 Besse theorem** | Einstein-metric stability literature: TT second variation of ∫R = (1/2)(∇*∇−2R̊) = (1/2)(Δ_L−2Λ) | Einstein operator Δ_E = Δ_L − 2Λ confirmed ⇒ stiffness = ε = 20 | **PASS** |
| **7** | **verdict() non-hardwired** | Independent re-implementation of the taxonomy ladder; check it flips on each gate; agree with executor on all combos | All 7 flips correct; my ladder == executor verdict() on all 6 combos | **PASS** |

**Computational-oracle evidence (executed, all exact over Q unless noted):**

```
$ python3 -u code/indep_zeta0_gilkey.py          # DIFFERENT method from spectral-zeta
  R (scalar) = 24;  |Ric|^2 = 144;  |Riem|^2 = 192;  Ric == 6g: True   (2 test points, identical)
  5R^2 - 2|Ric|^2 + 2|Riem|^2 = 2976  (constant across points => homogeneous)
  A_4/(4pi)^2 = (1/360)(2976)(pi^2/2)/(16 pi^2) = 31/120
  *** INDEPENDENT zeta(0) = 31/120 - 1 = -89/120  [== -89/120: True] ***   ALL CHECKS PASS: True

$ python3 -u code/indep_zeta0_heatkernel.py      # continuation-free numeric
  c_-2 = 0.03125 (=1/32=Vol/(4pi)^2);  c_-1 = 0.125 (=1/8);  c_0 = -0.74166666664 = zeta(0)
  *** INDEPENDENT (continuation-free) zeta(0) = -89/120 CONFIRMED: True ***

$ python3 -u code/indep_lich.py                  # independent real Lichnerowicz, eps=20
  TEST POINT 1 & 2: Delta_L(Hess R_M) = 32 * h  [lambda==32: True] (proportional, all 16 entries)

$ python3 -u code/indep_reconcile.py             # 8/8 PASS
  minimal (E=0): A_4/(4pi)^2 = 31/120 => zeta(0)=-89/120;  conformal (E=-R/6): 1/120 => -119/120 (DIFFERS)
  Einstein operator Delta_E = Delta_L - 2Lambda = 32 - 12 = 20 = eps
  literature Kretschmann K = (16/3)Lambda^2 = 192 == indep |Riem|^2 = 192

$ python3 -u code/indep_sakharov_checks.py        # 29/30 (the 1 'FAIL' is a check-formula
                                                  # double-subtraction of the zero mode, NOT physics;
                                                  # the c_0 value -89/120 is itself correct — see §2.1)
  C2 spectrum (12/12), C3 a_1=R/6 (4/4), C5 cc-matching (5/5), C7 verdict ladder (8/8) ALL PASS
  C1b: pole-subtraction method = -89/120 PASS; heat-kernel method c_0 = -0.741666 (= zeta(0), correct)

$ python3 -u code/sakharov_variety.py             # executor driver (sanity): exit 0
  >>> DERIVED VERDICT: CLOSES-CONDITIONAL <<<   all 7 self-tests pass
```

---

## 2. Claim-by-claim detail

### 2.1 ζ(0) = −89/120 — THREE independent confirmations (the decisive anchor)

**This is the load-bearing number and I attacked it hardest.** The executor used the binomial/Hurwitz
analytic continuation ζ(s)=4^{−s}Σ_j (s)_j/j!·[ζ_R(2s+2j−3)−1] with a ±ε pole average. I confirmed
−89/120 by **three genuinely different routes**, none reusing that continuation:

**(a) Gilkey a₄ from the curvature invariants (EXACT over Q — the strongest, fully independent).**
For a minimal scalar (E=0, Ω=0) in d=4, A₄ = (1/360)∫(5R²−2Ric²+2Riem²)√g (□R total-derivative=0).
I computed the invariants from **my own from-scratch real-4D Riemann tensor** (the v33 pipeline that
built the real metric → real Christoffels → real Riemann, sharing no code with any spectral path):
- R = 24 (exact), |Ric|² = 144 (exact; = 6²·4 for Ric=6g in d=4), **|Riem|² = 192 (exact)**,
  identical at two rational test points (constant ⇒ homogeneous space, as required).
- 5R² − 2·144 + 2·192 = 2880 − 288 + 384 = **2976**.
- Vol(CP², Ric=6g) = π²/2 (literature πⁿ/n!; also = the executor's heat-kernel A₀).
- A₄/(4π)² = (1/360)(2976)(π²/2)/(16π²) = **31/120**.
- The d=4 Mellin relation gives ζ(0) = A₄/(4π)² − dim ker = 31/120 − 1 = **−89/120**. EXACT.

**(b) Continuation-free heat-kernel small-t fit (numeric, independent).** θ(t)=Σ_{k≥1}d_k e^{−tλ_k}
(zero-mode-excluded) has small-t expansion with t⁰ coefficient = ζ(0) directly (Mellin), using NO
analytic continuation of ζ_R. A 7-point polynomial fit on small t gives c₀ = **−0.74166666664 =
−89/120** to 9 digits — AND the other coefficients fall out as independent validations: c₋₂ = 1/32
(⇒ A₀ = Vol = π²/2) and c₋₁ = 1/8 (⇒ A₂ = (R/6)Vol ⇒ R = 24). Gilkey tie: c₀+1 = 31/120.

**(c) Analytic pole-subtraction (≠ executor's ±ε average).** I removed the j=2 pole ζ_R(2s+1)~1/(2s)
analytically (the rf(s,2)=s(s+1) factor kills it, finite limit +1/4) BEFORE evaluating at s→0,
rather than averaging ±ε. Result: **−89/120** exact.

**(d) Literature.** The Gilkey a₄ formula `(4π)²a₄ = (1/360)tr{60RE+180E²+30Ω²+(5R²+2Riem²−2Ric²)I}`
is confirmed by multiple search hits (Vassilevich hep-th/0306138 §4.3; the b₄ form
`(1/360)(12□R+5R²−2Ric²+2Riem²)`). The CP² **Kretschmann K = (16/3)Λ² = 192** (Ric=Λg, R=4Λ, Λ=6)
is confirmed by the Fubini-Study-geometry literature and matches my independent |Riem|² = 192 EXACTLY.

> **Note on the one `indep_sakharov_checks.py` FAIL (NOT a discrepancy):** my first heat-kernel check
> wrote `zeta(0) = c_0 − 1`, double-subtracting the zero mode (θ already excludes k=0). The computed
> value c₀ = −0.741666 IS itself −89/120 (the correct ζ(0)); the `−1` was a mislabel in my check
> formula. The clean standalone `indep_zeta0_heatkernel.py` confirms c₀ = ζ(0) = −89/120, with the
> Gilkey tie c₀+1 = 31/120. **No physics discrepancy.** The conformal-scalar value −119/120 (R1) is
> exactly the executor's j=0 piece, a pleasing internal consistency.

**⇒ ζ(0) = −89/120 INDEPENDENTLY CONFIRMED (three ways + literature). NO showstopper.** HIGH.

### 2.2 Spectrum λ_k = 4k(k+2), d_k = (k+1)³ — CONFIRMED

- **d_k = (k+1)³** via the Weyl dimension formula for the SU(3) (k,k) irrep:
  dim(p,q)=(p+1)(q+1)(p+q+2)/2; at (k,k) = (k+1)²(2k+2)/2 = (k+1)³. Verified k=0..5 exact/Q.
- **λ_k = 4k(k+n)** with n=2 — **literature-confirmed** (search: "eigenvalues of the scalar Laplacian
  on CP^n are λ_k = 4k(k+n)"; same source gives R=4n(n+1)=24 and Vol=πⁿ/n!=π²/2 for n=2, all
  consistent with the Ric=6g normalization).
- Anchors: λ₁=12 / d₁=8 (= the SU(3) adjoint, the program's moments); λ₂=32 / d₂=27. The "4·2·4=32"
  mnemonic = 4k(k+2) at k=2. **CONFIRMED.** HIGH.

### 2.3 G1 — minimal scalar, a₁ = R/6, attractive — CONFIRMED

- **a₁ = R/6.** Gilkey a₂ density = tr(E + R/6); the free Dirichlet action ⇒ E = 0 ⇒ a₁ = R/6 = 4,
  R-coefficient +1/6. **The contamination argument is structurally sound:** a₂ contains ONLY E and
  R·1 (Gilkey's theorem); curvature-squared invariants (R²/Ric²/Riem²/trF²) are strictly a₄-level, so
  a LINEAR (flat-target, ξ=0) field cannot inject a non-R invariant into a₁. I independently confirmed
  that the conformal coupling (E=−R/6) would give a DIFFERENT a₄ (1/120 vs 31/120) — i.e. the
  ξ-dependence is real and the program's free-Dirichlet ⇒ minimal ⇒ E=0 is the correct object.
- **Attractive sign.** Minimal scalar a₂=R/6 > 0 ⇒ 1/(16πG_ind) > 0 ⇒ **G_ind > 0 (attractive)**,
  bosonic (no two-minus subtlety). **Literature-confirmed:** Visser, "Sakharov's induced gravity: a
  modern perspective" (Mod.Phys.Lett.A 17, 977, 2002) — positive Newton constant ⇔ attractive; the
  scalar contributes with the bosonic sign. The 3-way argument (Gilkey / FF-Visser weight / direct
  E=0) is sound. **CONFIRMED.** HIGH.
- κ_ind = (1/(12π²))Λ_f² (N=8 count-dependent, correctly flagged as NOT load-bearing).

### 2.4 ε = 20 (Trap #26) — CONFIRMED by my independent operator

Re-ran my v33 from-scratch real-4D Lichnerowicz operator Δ_L h = ∇*∇h + 12h − 2R̊h (∇*∇ positive,
R̊h_{ij}=R_{ikjl}h^{kl} textbook sign, built entirely in real coordinates from the real metric,
**zero shared code** with the executor's complex-frame operator). On the provable control Hess(R_M)
[M=s01, a λ₂=32 scalar]: **Δ_L = 32·h, proportional on all 16 entries, at TWO rational test points,
exact over Q.** ⇒ ε = λ_L − 2Λ = 32 − 12 = **20**. The matter source acts invertibly (ε≠0); the rank
wall is genuinely cleared. **CONFIRMED.** HIGH. (This re-certifies the v33 Gate-0 input that
distinguishes the variety from the dead v21 fiber.)

### 2.5 G2 — over-determined = False — CONFIRMED (the fork logic)

Independent linear-algebra check: Λ_cc = (3/2)Λ_f² is **one** linear equation in the **one** knob
Λ_f² (the count N cancels in the ratio — structural); the FS-critical condition Λ_cc = 6 has the
**unique** solution Λ_f² = 4 (sympy solve → [4]). This is ONE condition / ONE knob ⇒ always solvable
⇒ **NOT over-determined.** I contrasted with the genuine over-determination model (x=1 ∧ x=2 ⇒
sympy returns EmptySet) — that is the v18/v21 rank wall (10 OFF-T conditions on 1 scalar ⇒ 4 distinct
rationals ⇒ EmptySet), and it is **absent** here. **The decisive fork fact CONFIRMED.** HIGH on the
*structure*; the PASS-vs-soft-FAIL JUDGMENT is correctly flagged for human ratification (see §3).

### 2.6 G3 — Besse theorem — CONFIRMED by literature + reconciliation

**Literature-confirmed** (Einstein-metric stability literature, e.g. Dai-Wang-Wei; multiple stability
papers): the second variation of the total scalar curvature on TT tensors is
S''(h) = −(1/2)∫⟨h, ∇*∇h − 2R̊h⟩dV, with the **Einstein operator** Δ_E = ∇*∇ − 2R̊. On an Einstein
manifold the Lichnerowicz operator is Δ_L = ∇*∇ + 2Λ − 2R̊, so **Δ_E = Δ_L − 2Λ**. My independent
operator gives Δ_L = 32 with Λ=6, hence Δ_E = 32 − 12 = **20 = ε**. So the induced-a₁ TT stiffness IS
the certified ε = 20, and the response h = κ_ind·TT(B3)/ε is well-defined (ε≠0). The RESEARCH's "Besse
4.60" is the correct reference for this statement. **CONFIRMED.** HIGH.
**κ_ind FREE** (no negative-weight h₃(O) invariant, v20/v21) is consistent with the framework grading —
this is the "closes on the source but does not force the law" asymmetry. CONFIRMED.

### 2.7 verdict() non-hardwired — CONFIRMED

I re-implemented the taxonomy ladder **independently** from the RESEARCH §0 definitions (without
copying the executor's branch order) and checked: (T,T,T,NOT-YET-FORCED) ⇒ CLOSES-CONDITIONAL; and it
**flips** correctly on every perturbation — wrong-sign G1 / over-determined G2 / G3-no-closure ⇒
DOESN'T-CLOSE; G4=FIT ⇒ CLOSES-FORCED; G4=IMPORT ⇒ IMPORTS-QFT; Trap #25 guard (NOT-YET-FORCED ≠
FORCED) holds. My independent ladder **agrees with the executor's `verdict()` on all 6 input combos.**
The executor's 7 self-tests also pass (driver exit 0). NOT a hardwired string (the v20 anti-pattern is
avoided). **CONFIRMED.** HIGH.

---

## 3. The two FLAGGED judgments (verifier does NOT pick — correctly human-ratification items)

- **G2 PASS-vs-soft-FAIL.** Whether "FS critical at the only available scale (Λ_f²=4)" counts as
  G2-PASS (reading [A], folding the scale-identification into the G4 clamp ⇒ CLOSES-CONDITIONAL) or as
  a soft Λ-mismatch (reading [B]: 8 bosons, no fermionic partner, ζ(0)≠0 so the anomaly does not
  vanish ⇒ leans DOESN'T-CLOSE) is a genuine judgment. **The match IS a scale-identification (the
  cosmological-constant problem reframed), NOT a forced content cancellation** — I confirm this
  characterization is accurate (ζ(0)=−89/120≠0, purely bosonic content). Both readings are emitted;
  neither is silently picked. The verifier-relevant FACT (not over-determined ⇒ not the rank-wall
  death) is independently confirmed. **The PASS/soft-FAIL call is Bryan's, not mine.**
- **G4 NOT-YET-FORCED.** The computation (ζ′(0) of the program's own spectrum) is native; the
  PRINCIPLE "the system extremizes Γ[g]" = the state-fp ⟹ metric-fp bridge (Paper 5), which has no
  proof in the corpus ⇒ NOT-YET-FORCED is the honest default. Trap #28 (state-fp on ρ_J∈h₃(O) vs
  metric-fp on g) is kept typed-distinct. Trap #25 (do NOT glaze to CLOSES-FORCED) is honored.
  **CONFIRMED as the honest CEILING.** The classification (vs supplying the Paper-5 fit) is Bryan's.

---

## 4. Literature cross-checks (with sources)

| Quantity | Literature value | This phase | Source |
|---|---|---|---|
| CP^n scalar Laplacian eigenvalues | λ_k = 4k(k+n) | λ_k = 4k(k+2) (n=2) | spectral-geometry refs (search) |
| CP^n degeneracy / Ricci scalar / volume | dim SU(n+1)(k..k); R=4n(n+1); Vol=πⁿ/n! | (k+1)³; R=24; Vol=π²/2 | CP^n Laplacian refs (search) |
| Gilkey a₄ (minimal scalar) | (1/360)(5R²−2Ric²+2Riem²) | 2976/360 · Vol | Vassilevich hep-th/0306138 §4.3 (search) |
| Gilkey a₂ | tr(E + R/6) | R/6 = 4 (E=0) | Vassilevich §4.3 (search) |
| CP² Kretschmann | K=\|Riem\|²=(16/3)Λ²=192 | 192 (exact, indep Riemann) | Fubini-Study-geometry refs (search) |
| Besse / Einstein-op 2nd variation | S''\|_TT = (1/2)(∇*∇−2R̊) = (1/2)(Δ_L−2Λ) | Δ_E = Δ_L−2Λ ⇒ ε=20 | Einstein-stability lit (search; Besse 4.60) |
| Sakharov minimal-scalar sign | positive Newton const ⇔ attractive (bosonic) | attractive, G_ind>0 | Visser MPLA 17,977 (2002) (search) |

(WebFetch of the Vassilevich and Dai-Wang-Wei PDFs returned binary-unreadable streams; the formulas
are nonetheless confirmed by multiple independent search hits quoting them verbatim.)

---

## 5. Universal physics checks

| Check | Status | Confidence | Notes |
|---|---|---|---|
| 5.1 Dimensional/structural | CONSISTENT | INDEPENDENTLY CONFIRMED | ζ(0), a-coeffs dimensionless; A₄/(4π)² pure number 31/120 |
| 5.3 Limiting cases | VERIFIED | INDEPENDENTLY CONFIRMED | Λ_f²=4 from Λ_cc=6; conformal-limit (E=−R/6) ⇒ different a₄ (sanity) |
| 5.6 Symmetry | VERIFIED | INDEPENDENTLY CONFIRMED | SU(3)-equivariance: d_k=(k+1)³ = (k,k) irrep dims; invariants constant (homogeneous) |
| 5.8 Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | 5R²−2Ric²+2Riem²=2976 exact; ε=Δ_L−2Λ=20; sign conventions tracked |
| 5.9 Numerical convergence | CONVERGED | INDEPENDENTLY CONFIRMED | heat-kernel small-t fit: c₀→−89/120 to 9 digits; c₋₂,c₋₁ exact |
| 5.10 Literature agreement | AGREES | INDEPENDENTLY CONFIRMED | λ_k, R, Vol, a₄, Kretschmann, Besse, Visser sign all match (§4) |
| 5.11 Plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | attractive G>0; ε>0 invertible; ζ(0)<0 (anomaly nonzero, as stated) |
| Cross-check (5.4) | VERIFIED | INDEPENDENTLY CONFIRMED | ζ(0) by 3 independent methods; \|Riem\|² by Riemann AND literature |
| verdict ladder (non-hardwired) | VERIFIED | INDEPENDENTLY CONFIRMED | independent re-implementation agrees on all combos; flips correctly |

**Overall physics assessment: SOUND.** 11/11 applicable checks pass, all independently confirmed.

---

## 6. Catastrophic-cancellation / approximation gates

- **Gate A (cancellation):** the decisive numbers are exact rationals over Q (no float cancellation);
  the numeric heat-kernel fit is well-conditioned (the c₋₂,c₋₁ coefficients come out to 1/32, 1/8 to
  6 digits, confirming no catastrophic cancellation in the small-t extraction). PASS.
- **Gate B (analytic↔numeric):** ζ(0) analytic (Gilkey a₄, exact −89/120) vs numeric (heat-kernel
  −0.74166666664) agree to 9 digits. PASS.
- **Gate C (integration measure):** Vol = π²/2 is the matched FS normalization (literature πⁿ/n! AND
  the executor's heat-kernel A₀ extraction AND the c₋₂=1/32 coefficient here). The a₄ integrand is
  constant on the homogeneous CP², so A₄ = (integrand/360)·Vol with no Jacobian subtlety. PASS.
- **Gate D (approximation validity):** the Sakharov leading-order (a₀ quartic, a₁ quadratic, a₄
  log/finite) truncation is the standard induced-gravity expansion; the scale-identification caveat
  (the EH term needs the cutoff Λ_f) is correctly stated and flagged. No uncontrolled approximation.

---

## 7. Discrepancies / gaps

**None affecting the verdict.** Every load-bearing claim was independently reproduced or
literature-confirmed. The single `indep_sakharov_checks.py` "FAIL" is a check-formula
double-subtraction of the zero mode in my own first heat-kernel attempt — the computed value
(−89/120) is itself correct, and the clean `indep_zeta0_heatkernel.py` confirms it (§2.1). No physics
gap; no fence violation; no overclaim.

---

## 8. Fences — COMPLIANT

Scanned `94-VERDICT.md` and `94-SUMMARY.md`: every Einstein/gravity occurrence is a negation, the
fenced import (a₁=∫R√g), the FS-is-Einstein geometric fact (used, not derived), or the Besse book
title / theorem context. NO claim asserts the framework PRODUCES gravity. κ stated as a framework
ratio (Λ_f-set), NOT Newton. FS USED not derived. "Signature Riemannian (Wall 2 unpaid)" stated.
CLOSES-CONDITIONAL explicitly NOT glazed to CLOSES-FORCED (Trap #25). v34 does NOT retract v33
(extremize stays dead) or v17–v21 (fiber kills stand). Paper 5 named as the only more-than-nothing
result. Verdict is consistently CLOSES-CONDITIONAL (never CLOSES-FORCED). **All fences honored.**

---

## 9. Verdict, confidence

### Independent verdict: CLOSES-CONDITIONAL — CONFIRMED
The INDUCE route does NOT die on the variety (rank wall cleared, ε=20 re-certified by an independent
operator) and does NOT force a gravitational law (κ_ind FREE; the clamp NOT-YET-FORCED). G1–G3 pass
(independently confirmed); G4 = NOT-YET-FORCED (the honest default). The entire gravity gap collapses
to the single state-fp ⟹ metric-fp clamp (Paper 5). This COMPLETES the Block-C confrontation: both
ways to manufacture a law — EXTREMIZE (v33: FORCES-NOTHING) and INDUCE (v34: CLOSES-CONDITIONAL) — now
run.

### Confidence: HIGH (on the decision-relevant core)
- **ζ(0) = −89/120: HIGH** — three independent methods (Gilkey a₄ exact/Q, continuation-free
  heat-kernel, analytic pole-subtraction) + literature (Kretschmann 192).
- **Spectrum / a₁ / sign / ε=20 / Besse: HIGH** — literature-confirmed and/or independently
  re-derived (the ε=20 operator shares zero code with the executor).
- **G2 not-over-determined: HIGH** (structure); the **PASS-vs-soft-FAIL judgment: MEDIUM** and
  correctly flagged for Bryan, not auto-resolved.
- **G4 NOT-YET-FORCED: MEDIUM** — the honest classification absent a Paper-5 proof; correctly flagged.

**The verdict is robust under an independent code path and the literature. CLOSES-CONDITIONAL is
INDEPENDENTLY CONFIRMED, with the two flagged judgments left for human ratification.**

---

## 10. Computational oracle evidence (executed, this phase)
- Independent Gilkey a₄ from my own real Riemann: R=24, |Ric|²=144, |Riem|²=192, A₄/(4π)²=31/120,
  ζ(0)=−89/120 (exact/Q, 2 points) — `code/indep_zeta0_gilkey.py`.
- Continuation-free heat-kernel: ζ(0)=−89/120 (9 digits), c₋₂=1/32, c₋₁=1/8 —
  `code/indep_zeta0_heatkernel.py`.
- Independent real Lichnerowicz: Δ_L(Hess R_M)=32·h on all 16 entries, 2 points ⇒ ε=20 —
  `code/indep_lich.py`.
- Spectrum (Weyl dim, k=0..5), a₁=R/6, cc-matching logic, verdict ladder (8/8) —
  `code/indep_sakharov_checks.py`.
- Reconcile (minimal vs conformal a₄; Besse Δ_E=Δ_L−2Λ; Kretschmann literature) 8/8 —
  `code/indep_reconcile.py`.
- Executor driver re-run (sanity): exit 0, verdict CLOSES-CONDITIONAL, 7 self-tests pass.
