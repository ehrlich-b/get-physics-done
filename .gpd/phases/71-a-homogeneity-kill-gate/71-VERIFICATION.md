---
phase: 71-a-homogeneity-kill-gate
verified: 2026-05-30T00:00:00Z
status: passed
score: 4/4 decisive contract targets verified (reconciled)
consistency_score: 9/9 decisive physics checks passed
independently_confirmed: 9/9 checks independently confirmed (exact over Q)
confidence: high
reconciled_verdict: "SURVIVES — the inherited h_2(C_u) slice metric is genuinely position-dependent; the three routes AGREE once the 4-dim-sub-slice vs 10-dim-V_0 submanifold conflation is removed."
comparison_verdicts:
  - subject_kind: acceptance_test
    subject_id: test-homogeneity
    subject_role: decisive
    reference_id: ref-totaro
    comparison_kind: cross_method
    metric: exact_inequality_over_Q
    threshold: "R(x),K(x) differ across >=2 distinct generic rational basepoints exact over Q => SURVIVES"
    verdict: pass
    notes: "Independently reproduced: matterless pure-V_0 basepoints give DIFFERENT exact-over-Q Ricci scalars (R=-521269105/154700283, -137053539/48874081, -114049215/37982569 ...). Genuine position-dependence."
  - subject_kind: acceptance_test
    subject_id: test-two-route-agreement
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: cross_method
    metric: same_verdict_all_routes
    threshold: "Route-1 curvature, Route-2 stabilizer transitivity, CALC-02 II all give the SAME verdict"
    verdict: pass
    notes: "RECONCILED to AGREEMENT (all SURVIVES) after correcting the executor's center-only II computation. II(h_2(C_u)) != 0 OFF-center (executor only checked the center, where it is 0). The 71-02 'disagreement => no verdict' was based on a submanifold conflation (II(V_0=10)=0 does NOT constrain the 4-dim h_2(C_u) sub-slice). With the off-center II computed, CALC-02 agrees with Route-1 SURVIVES."
  - subject_kind: acceptance_test
    subject_id: test-single-copy-anchor
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "orbit 24 / Spin(8) 28 / trdeg 3"
    verdict: pass
    notes: "Engine ALL_PASS exit 0; calibration anchors reproduced."
  - subject_kind: acceptance_test
    subject_id: test-e6-dim
    subject_role: decisive
    reference_id: ref-baez-octonions
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "dim e_6 == 78 == 52+26"
    verdict: pass
    notes: "Independently reproduced: dim e_6 = 78, orbit of E_11 = 17, dim Stab_{E_6}(E_11) = 61, dim Stab_{V_0} = 45 = Spin(9,1), V_0 orbit 9 < 10 — all exact over Q."
suggested_contract_checks:
  - check: "Add an OFF-CENTER II(h_2(C_u)) acceptance gate (II of the 4-dim spacetime sub-slice at >=1 generic off-center pure-V_0 basepoint), not only at the center."
    reason: "The 71-02 no-verdict rested on II(h_2(C_u))|_center = 0 and II(V_0=10)=0, but the DECISIVE submanifold (the 4-dim h_2(C_u) spacetime sub-slice) is NOT totally geodesic OFF-center (II != 0). The contract's II gate (test-homogeneity (c)) was satisfied at the center only, which manufactured a spurious 'totally geodesic => homogeneous' KILL signal. An off-center II(h_2(C_u)) gate would have caught the conflation directly."
    suggested_subject_kind: acceptance_test
    suggested_subject_id: test-homogeneity
    evidence_path: "code/bulk_geometry_verification.py second_fundamental_form(H2CU_SLICE_IDX, <off-center sub>)"
  - check: "Pin the genuine basepoint modulus as det_2 (the Stab_{V_0}=Spin(9,1) invariant), not rho_J(X_bg)."
    reason: "rho_J^2 = Tr(X^2)-(Tr X)^2/3 is the EUCLIDEAN traceless norm, which Spin(9,1) does NOT preserve (boosts move it at fixed det_2). The genuine Stab_{V_0}-invariant modulus is det_2 (0/45 generators move it). R = R(det_2) on the matterless family (direction-blind WITHIN a det_2 leaf); the SURVIVES signal is that DIFFERENT det_2 leaves give different R, and different-det_2 basepoints are genuinely inequivalent. rho_J and det_2 coincide for the single-direction perturbations Route-1 sampled, so the verdict is unaffected, but det_2 is the correct invariant to name."
    suggested_subject_kind: claim
    suggested_subject_id: claim-homogeneity
    evidence_path: "code/bulk_geometry_verification.py stab_preserving_V0 + det_2 invariance check"
gaps: []
expert_verification: []
---

# Phase 71 (A) — Homogeneity KILL Gate: Independent Reconciled Verification

**Phase goal (ROADMAP):** With E_11 = diag(1,0,0) fixed, decide whether the inherited slice metric g_mu_nu(x) = eta_mu_nu + h_mu_nu(x) on the V_0 Peirce slice (decisive arena: the dim-4 h_2(C_u) sub-slice) is genuinely POSITION-DEPENDENT (route SURVIVES) or X-INDEPENDENT / HOMOGENEOUS (route DEAD / KILL), via exact-over-Q curvature-scalar invariants, cross-checked by stabilizer transitivity and the totally-geodesic second fundamental form II.

**Status:** `passed`. The two execution waves produced a CONTESTED no-verdict (71-01 SURVIVES vs 71-02 no-verdict-on-disagreement). I independently re-derived the physics exact over Q. **The disagreement was a submanifold conflation in 71-02, not a genuine route conflict.** Corrected, the three routes RECONCILE to a clean **SURVIVES**.

**RECONCILED PHASE-71 VERDICT: SURVIVES.** The inherited h_2(C_u) slice metric is genuinely position-dependent. The position-dependence is matterless and genuine (not a scale/chart/gauge artifact). Phases 72/73 are greenlit.

---

## The one-line reconciliation

> The 4-dim spacetime sub-slice h_2(C_u) is **NOT totally geodesic off-center** (II != 0), even though the 10-dim V_0 = h_2(O) **is** (II = 0 everywhere). The executor computed II(h_2(C_u)) only at the center (where it is 0) and read "II=0 ⇒ homogeneous ⇒ KILL signal," conflating the 4-dim sub-slice with the 10-dim V_0. With II(h_2(C_u)) computed OFF-center (≠ 0, matterless), CALC-02 AGREES with Route-1's SURVIVES via the Gauss equation; Route-2's single non-transitive modulus (det_2, orbit 9 < 10) IS the genuine position-dependence direction. All three routes ⇒ **SURVIVES**.

---

## Decisive checks I independently ran (all exact over Q, foreground `python3 -u`, engine SSOT reused)

### CHECK A — the position-dependence is MATTERLESS and direction-blind (CONFIRMED)

**A(i) matterless pure-V_0 basepoints give VARYING R.** Reproduced the orchestrator's three values EXACTLY (zero matter, indices {4..9} only, common fixed slice point):

| delta (pure V_0-internal, ZERO matter) | rho_J^2 | R (Ricci scalar, exact over Q) |
|---|---|---|
| {4:1/5, 5:1/7} | 148/1225 | **-521269105/154700283** |
| {4:2/5, 6:1/3} | 122/225 | **-137053539/48874081** |
| {7:1/3, 8:1/4, 9:1/5} | 769/1800 | **-114049215/37982569** |

These differ. The position-dependence is present with **zero matter** — which **CONTRADICTS** 71-02's localization that "Route-1's SURVIVES is sourced ENTIRELY by V_1/2/V_1 MATTER." Confidence: **INDEPENDENTLY CONFIRMED**.

**A(ii) matter (in)sensitivity.** Base = pure V_0 {4:1/3}, R = -73041507/21967969.
- Adding V_1 alpha (index 0): R **UNCHANGED** (-73041507/21967969). V_1 is inert to this curvature.
- Adding V_{1/2} (index 11): R changes (-20890467/7656289). dR = 100305755136000/168193119407041.
Confirmed: pure-V_0 geometry already carries the variation; V_1 is inert; V_{1/2} contributes additively. Confidence: **INDEPENDENTLY CONFIRMED**.

**A(iii) direction-blindness at fixed rho_J^2.** Four distinct single-component V_0-internal directions {4},{5},{6},{7} at magnitude 1/3 (all rho_J^2 = 2/9) give the **IDENTICAL** R = **-73041507/21967969**; a different magnitude {4:1/2} (rho_J^2=1/2) gives a different R = -1587747/552049. So R = R(rho_J) (direction-blind). Confidence: **INDEPENDENTLY CONFIRMED**.

### CHECK B — THE LINCHPIN: II of the 4-dim h_2(C_u) sub-slice OFF-CENTER (CONFIRMED ≠ 0)

The executor only computed `second_fundamental_form(H2CU_SLICE_IDX, _center_sub())` = 0. I computed it OFF-center, at positive-cone basepoints (alpha=beta=gamma=1, off-center perturbation = pure V_0-internal {4..9}, ZERO matter):

| basepoint (positive cone, matterless off-center) | det_3 | II(h_2(C_u)) is_zero | n_nonzero | example II value |
|---|---|---|---|---|
| on-center (no transverse) | 1 | **True** | 0 | — |
| off {4:1/7} | 48/49 | **FALSE** | 4 | 343/2400 |
| off {4:1/3} | 8/9 | **FALSE** | 4 | (nonzero) |
| off {5:1/4, 8:1/3} | 119/144 | **FALSE** | 8 | (nonzero) |

**II(h_2(C_u)) = 0 at the center, but ≠ 0 OFF-center** (matterless). This is the executor's exact error. Confidence: **INDEPENDENTLY CONFIRMED**.

**Cross-check (resolves the apparent paradox):** II(V_0 = full 10-dim) = 0 EVERYWHERE I tested (center AND off-center {4:1/3}, {4:1/7,5:1/9}, n_nonzero=0 each). So:
- V_0 = h_2(O) IS genuinely totally geodesic (sub-Jordan-algebra sub-cone, Faraut-Koranyi). The executor's II(V_0)=0 is correct and robust.
- The 4-dim h_2(C_u) is a strict sub-slice of V_0 and is a **curved submanifold of the homogeneous V_0** off-center.
- II=0 for the 10-dim V_0 does **NOT** imply II=0 for the 4-dim h_2(C_u). Different submanifolds. **This is the conflation 71-02 missed.**

Via the Gauss equation R^{slice} = R^{ambient}|_{slice} + (II II - II II): a non-geodesic slice (II ≠ 0) has induced curvature that genuinely varies with the basepoint. This directly explains and AGREES WITH Route-1's varying R. Confidence: **INDEPENDENTLY CONFIRMED**.

### CHECK C — GENUINE vs ARTIFACT: is the variation a slice-preserving-isometry orbit artifact? (GENUINE)

Independently reproduced the stabilizer counts (exact over Q):
- dim e_6 = **78** = 52 + 26; orbit of E_11 = **17**; dim Stab_{E_6}(E_11) = **61** (61 nullspace generators all annihilate E_11).
- dim Stab_{V_0} (slice-preserving) = **45** = dim Spin(9,1); V_0 orbit under Stab_{V_0} = **9** < family 10 (single modulus). All confidence **INDEPENDENTLY CONFIRMED**.

**The genuine modulus is det_2, not rho_J.** The single non-transitive modulus (orbit 9 < 10) is the V_0-block Lorentzian norm det_2 = beta*gamma - |oct-x1|^2:
- **det_2 is moved by 0/45 Stab_{V_0} generators** (exact over Q) — it IS the invariant.
- rho_J^2 (the Euclidean traceless norm) IS moved (9/45 generators) — boosts change rho_J^2 at FIXED det_2. Numeric orbit flow confirms det_2 stays exactly -5 while rho_J^2 runs 15.67 → 19.40 → 31.99.

**R = R(det_2) on the matterless family — and det_2 distinguishes genuinely inequivalent basepoints.** Decisive exact-over-Q test: four matterless pure-V_0 basepoints with the SAME det_2 = -57/1600 (same Σc^2) but DIFFERENT transverse directions ({4:1/2}, {5:1/2}, {4:3/10,5:2/5}, {6:3/10,9:2/5}) ALL give the IDENTICAL R = **-1587747/552049**. So within a det_2 leaf (gauge orbit), R is constant (direction = gauge); the variation is purely a function of the genuine Stab_{V_0} modulus det_2.

The 4 ROUTE1_BASEPOINTS that 71-01 used for SURVIVES have **distinct det_2** (12071/78400, -817/14400, 11/14400, -3013/14400) ⇒ genuinely inequivalent leaves ⇒ the R-variation is **GENUINE position-dependence, not a chart/gauge artifact** ⇒ SURVIVES. Confidence: **INDEPENDENTLY CONFIRMED**.

**Not an overall-scale (det_3=1) artifact.** R is exactly invariant under X → 2X (R = -73041507/21967969 at both X and 2X): Phi = -log det shifts by a constant under uniform scaling, leaving the Hessian metric and hence R unchanged. The variation lives in the traceless/leaf (det_2) direction, transverse to overall scale, so the det_3 = 1 normalization cannot remove it. Confidence: **INDEPENDENTLY CONFIRMED**.

### CHECK D — two-route agreement + no Wick artifact (CONFIRMED, RECONCILED)

- **Route-1 (curvature):** R(x), K(x) differ across distinct basepoints (matterless), exact over Q ⇒ SURVIVES.
- **Route-2 (stabilizer transitivity):** Stab_{V_0} = Spin(9,1), orbit 9 < family 10 ⇒ a genuine modulus (det_2) ⇒ basepoints at different det_2 are NON-isometric ⇒ SURVIVES.
- **CALC-02 (II), corrected:** II(h_2(C_u)) ≠ 0 OFF-center ⇒ the spacetime slice is non-geodesic ⇒ position-dependent induced curvature ⇒ SURVIVES (the executor's center-only II=0 was the conflation).

All three AGREE on **SURVIVES**. The disagreement 71-02 reported was an artifact of (a) computing II(h_2(C_u)) only at the center and (b) reading II(V_0=10)=0 as constraining the 4-dim sub-slice. **No Riemannian-vs-Lorentzian / Phase-70 Wick artifact:** the R-variation is intrinsic, scale-invariant, sign-pinned (R<0 everywhere, R(center)=-3 negative, consistent with the H^3 benchmark K_sections=-1/2 constant), and present on the Riemannian cone-Hessian restriction directly — no Wick rotation enters the decisive comparison. Confidence: **INDEPENDENTLY CONFIRMED**.

---

## Computational oracle evidence (exact over Q, independently executed)

```
# CHECK A(i) — reproduced orchestrator's matterless varying R (engine API):
delta={4:1/5,5:1/7}        rho_J^2=148/1225       R=-521269105/154700283   (detg!=0, real)
delta={4:2/5,6:1/3}        rho_J^2=122/225        R=-137053539/48874081
delta={7:1/3,8:1/4,9:1/5}  rho_J^2=769/1800       R=-114049215/37982569

# CHECK B — THE LINCHPIN, off-center II of the 4-dim spacetime sub-slice:
II(h2Cu) @ on-center                : is_zero=True  n_nonzero=0   det3=1
II(h2Cu) @ off-center {4:1/7}       : is_zero=False n_nonzero=4   det3=48/49   example II=343/2400
II(h2Cu) @ off-center {5:1/4,8:1/3} : is_zero=False n_nonzero=8   det3=119/144
II(V_0=10) @ off-center {4:1/3}     : is_zero=True  n_nonzero=0   (V_0 genuinely tot.geo.)

# CHECK C — genuine modulus + same-det_2 collapse:
det_2 moved by 0/45 Stab_{V_0} gens;  rho_J^2 moved by 9/45  (det_2 is the invariant)
SAME det_2=-57/1600, 4 different directions -> ALL R = -1587747/552049 (direction = gauge)
4 ROUTE1 basepoints have DISTINCT det_2 (12071/78400, -817/14400, 11/14400, -3013/14400)
R(X)=R(2X)=-73041507/21967969  (scale-invariant; not a det_3=1 artifact)

# CHECK D — stabilizer counts (independently reproduced):
dim e_6 = 78 ; orbit(E_11) = 17 ; dim Stab_{E_6}(E_11) = 61 ; dim Stab_{V_0} = 45 = Spin(9,1) ; V_0 orbit 9 < 10

# Engine harness:
python3 code/bulk_geometry_verification.py  ->  OVERALL: ALL_PASS, exit 0
```

VERDICT of the oracle: **SURVIVES** — matterless, genuine, scale-invariant, gauge-invariant (constant on det_2 leaves), with II(h_2(C_u)) ≠ 0 off-center supplying the Gauss-equation mechanism. PASS.

---

## Physics consistency summary

| # | Check | Status | Confidence | Notes |
|---|---|---|---|---|
| 5.2 | Numerical spot-check (R at concrete basepoints) | VERIFIED | INDEPENDENTLY CONFIRMED | Reproduced the orchestrator's 3 matterless R values exactly over Q |
| 5.3 | Limiting case (R at center; H^3 sign) | VERIFIED | INDEPENDENTLY CONFIRMED | R(center) = -3 (negative); H^3 K_sections = -1/2 constant; sign pinned, imag-free |
| 5.4 | Cross-check (II vs curvature via Gauss) | VERIFIED | INDEPENDENTLY CONFIRMED | II(h_2(C_u)) != 0 off-center explains varying R via Gauss; consistent with Route-1 |
| 5.6 | Symmetry (Stab_{V_0} invariance / gauge) | VERIFIED | INDEPENDENTLY CONFIRMED | det_2 = Stab_{V_0} invariant (0/45 move it); R constant on det_2 leaves (gauge-invariant) |
| 5.8 | Math consistency (submanifold conflation) | ERROR_FOUND (in 71-02) | INDEPENDENTLY CONFIRMED | II(V_0=10)=0 does NOT imply II(h_2(C_u)=4)=0; the 4-dim sub-slice is non-geodesic off-center |
| 5.11 | Plausibility (scale, sign, reality) | VERIFIED | INDEPENDENTLY CONFIRMED | R invariant under X->2X (no scale artifact); R<0 everywhere; all R,K real over Q |
| 5.10 | Agreement with structure (orbit/stab counts) | VERIFIED | INDEPENDENTLY CONFIRMED | e_6=78, orbit(E_11)=17, Stab=61, Stab_{V_0}=45=Spin(9,1), V_0 orbit 9<10 |
| — | Two-route agreement (reconciled) | VERIFIED | INDEPENDENTLY CONFIRMED | All three routes => SURVIVES after correcting the off-center II |
| — | Engine regression (SSOT, ALL_PASS) | VERIFIED | INDEPENDENTLY CONFIRMED | python3 code/bulk_geometry_verification.py => ALL_PASS exit 0 |

**Overall physics assessment: SOUND.** Every decisive value independently confirmed exact over Q. One ERROR localized in 71-02's reasoning (submanifold conflation), which does NOT invalidate any 71-02 computation (all its exact-over-Q numbers reproduce) — only its no-verdict CONCLUSION. The reconciled verdict is SURVIVES.

---

## Forbidden-proxy audit

| Proxy | Status | Evidence |
|---|---|---|
| fp-coordinate-curvature | REJECTED | The decisive quantities are scalar invariants R, K (full 4-index contractions) — verified by computing them, not reading metric components; R is constant on det_2 gauge leaves (direction-blind) and scale-invariant. The variation is in the genuine F_4/Stab_{V_0}-invariant modulus det_2, NOT a chart effect. Comparison holds the spacetime point x FIXED. |
| fp-float-decisive | REJECTED | Every decisive value computed exact over Q (sympy.Rational). Float (mpmath) used ONLY as explicitly-labeled non-decisive triage (the orbit-flow visualization of det_2 vs rho_J^2). The verdict numbers are all exact rationals. |
| fp-relabel-homogeneous | REJECTED | I did NOT soften a homogeneous result. The result is genuinely position-dependent (SURVIVES), established by decisive exact-over-Q evidence. I did NOT force SURVIVES either: I tested the KILL hypothesis (is the variation gauge?) head-on (Check C same-det_2 collapse, scale-invariance) and it failed — the variation is genuine. |

---

## What greenlights / what would have killed

- **Greenlights (the SURVIVES branch, now established):** the inherited h_2(C_u) slice metric is genuinely position-dependent across distinct det_2 leaves, matterlessly, with II(h_2(C_u)) != 0 off-center supplying the mechanism. Phases 72 (matter-sourcing) and 73 (Einstein structure) are greenlit. The matter (V_{1/2}) sector ADDS to the curvature (it also changes R at fixed det_2) — so Phase 72's matter-sourcing question is real and well-posed, but it is NOT the origin of the homogeneity-breaking; the pure geometry already breaks homogeneity.
- **Corrected reading of II(V_0)=0:** II(V_0=10-dim) = 0 is a TRUE statement (V_0 = h_2(O) is totally geodesic, a sub-Jordan-algebra sub-cone) — but it is the wrong submanifold. The physical spacetime slice is the 4-dim h_2(C_u) ⊂ V_0, which has II != 0 off-center. "V_0 totally geodesic" does not imply "the spacetime sub-slice is homogeneous."
- **What would have killed:** if the matterless R-variation had collapsed under a slice-preserving isometry (R constant across det_2 leaves), OR if II(h_2(C_u)) had been 0 off-center too, OR if R had been removable by overall scaling. None of these hold — all three were tested and failed.

---

## Honest residual / scope note

- **det_2 vs rho_J labeling:** the orchestrator framed the modulus as rho_J(X_bg). The strictly-correct Stab_{V_0}-invariant modulus is **det_2** (the V_0-block Lorentzian norm); rho_J^2 is the Euclidean traceless norm, which is moved by Spin(9,1) boosts. They coincide on the single-direction perturbations Route-1 and the orchestrator sampled (so the SURVIVES verdict is unaffected), but det_2 is the genuine invariant that distinguishes inequivalent basepoints. Recorded as a suggested_contract_check (non-blocking; sharpens, does not change, the verdict).
- **Phase-72 matter coupling:** whether the position-dependent curvature is sourced by matter via the cubic-norm cross-terms in the Einstein sense is the Phase-72 question and is NOT decided here. The Phase-71 gate (is the geometry homogeneous?) is decisively answered: NO, it is position-dependent (SURVIVES), matterlessly.
- All decisive arithmetic exact over Q; engine SSOT (det_3) reused; 0 octonion_algebra imports; engine ALL_PASS exit 0; deterministic.

---

_Phase: 71-a-homogeneity-kill-gate — independent reconciled verification_
_Verified: 2026-05-30_
