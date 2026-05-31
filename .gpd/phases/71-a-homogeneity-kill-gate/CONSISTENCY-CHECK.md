# Phase 71 (A) — Homogeneity KILL Gate: Cross-Phase Consistency Check (rapid mode)

**Checked:** 2026-05-30
**Mode:** rapid (post-phase, milestone v17.0)
**Verdict checked:** reconciled SURVIVES (71-VERIFICATION.md, status: passed, HIGH)
**consistency_status: CONSISTENT** (with 1 non-blocking convention-text clarification recommended)

---

## Scope

Phase 71 is the DECISIVE homogeneity KILL gate of v17.0. Two execution waves
(71-01 Route-1 SURVIVES; 71-02 Route-2 + CALC-02 no-verdict-on-disagreement)
produced a contested no-verdict; the verifier (71-VERIFICATION.md) reconciled it to a
clean SURVIVES by correcting a submanifold conflation. This check verifies that the
RECONCILED result is consistent with the full v17.0 conventions ledger (state.json
`convention_lock`, 33 entries / 18 canonical + 15 custom; CONVENTIONS.md) and with the
Phase-70 (A0) and Phase-52 (KKT) producers it consumes.

All decisive numbers were INDEPENDENTLY reproduced exact over Q on the certified engine
`code/bulk_geometry_verification.py` (engine: ALL_PASS exit 0, 41/41 PASS, deterministic
across 2 full re-runs).

---

## 1. Convention compliance (current phase vs FULL ledger)

| # | Convention (v17.0 lock) | Relevant? | Compliant? | Evidence (independently reproduced) |
|---|---|---|---|---|
| metric_signature | mostly-minus (−,+,+,+) slice via det_2; bulk Riemannian g_X=Hess(−log det) | YES | YES | slice eta = Minkowski (1 timelike + 3 spacelike); bulk center metric diag(9,9,18,18) all eigenvalues >0 (Riemannian). Both signatures used in their correct arenas; no mixing. |
| natural_units | ħ=c=k_B=1; decisive EXACT over Q | YES | YES | every decisive value an exact rational (R, K, II, det_2, stab dims); 0 float-rank/float-curvature on decisive path (source guard PASS). |
| cubic_norm_det (det_3 SSOT) | ring_lemma det_3, cross 2Re(x2* x0* x1); NEVER octonion_algebra.py | YES | YES | LOCK 0 byte-identity to ring_lemma_verification reaffirmed; source guard 0 octonion_algebra imports; BP4 octonionic directions give REAL rational R (no associator error). |
| potential / cone_metric | Φ=−log det; g_X=Hess(−log det) positive-definite | YES | YES | center Hess(−log det)|_{I/3}=diag(9,9,18,18) det 26244 (>0 ⇒ convex); Totaro engine uses only f_ijk (det cubic ⇒ f_ijkl=0). |
| covariant_derivative_sign / riemann_ricci_sign | Levi-Civita of g_X; Riemann sign STATED + benchmarked on H^3 | YES | YES (sign) / **see §5 clarification** | sign pinned NEGATIVE & CONSTANT on H^3 (K=−1/2). The text says "constant curvature −1"; the cone-Hessian-slice value is −1/2 (round = −1). Benign metric-normalization factor of 2 — recommend recording. |
| signature_bridge (construction ii) | eta from det_2 + cone-Hessian h; g(center,M=0)=eta EXACTLY; (i)/Wick REJECTED | YES | YES | center regression: h_μν(center)=0, g(center)=eta exactly; verdict computed on Riemannian cone-Hessian restriction, NO Wick rotation on the decisive path (verifier CHECK D; confirmed). |
| state_normalization | center I/3, rho_J(I/3)=0, det(I/3)=1/27 | YES | YES | rho_J^2(center)=0 reproduced; off-center expansion measured from I/3. |
| coordinate_system | slice entries {17,18,19,26}=={x1,x2,x3,x10}=(b,g,p,q) symbolic | YES | YES | engine-native H2CU index set {1,2,3,10}; slice coords held symbolic; off-center perturbation in non-slice directions only. |
| generator_normalization / group | F_4=Aut (52); E_6=Stab(det); Stab_{E_6}(E_11) Levi~Spin(9,1) | YES | YES | dim e_6=78=52+26; orbit(E_11)=17; Stab=61; Stab_{V_0}=45=Spin(9,1) (Levi recovered); single-copy anchor 24/Spin(8)28/trdeg3. |
| commutation / jordan_product | [A,B]=AB−BA; X∘Y=(1/2)(XY+YX) | YES | YES | used in inner-derivation f_4 build and Jordan L-operators. |
| octonion_basis | Fano e1·e2=e4 | YES | YES | consistent (SSOT det_3). |
| complex_structure | u=e7; C_u=span{1,e7}; h_2(C_u)~R^{3,1} | YES | YES | spacetime sub-slice = h_2(C_u). |
| fourier, gauge, regularization, renormalization, time_ordering, levi_civita_sign, spin_basis, gamma_matrix, creation_annihilation | N/A on v17.0 decisive path (intrinsic differential geometry; no field theory) | NO | N/A | correctly inert; Phase 71 introduces no field-theory/QFT objects. |

**Compliant: 13/13 relevant conventions. 9 conventions correctly N/A. 0 violations.**
The 1 flagged item (riemann_ricci_sign text) is a documentation clarification, NOT a
compliance violation — the engine's actual sign convention is correct and the verdict is
sign-convention-independent.

---

## 2. Provides/consumes verification (semantic, test-value)

| Quantity | Producer | Consumer | Meaning✓ | Units✓ | Test value (exact over Q) | Conv✓ | Status |
|---|---|---|---|---|---|---|---|
| center metric diag(9,9,18,18)/det 26244 | Phase 70 (A0) | Phase 71 center regression | YES | YES (dimensionless) | `cone_hessian_at_center()`=diag(9,9,18,18), det=26244 — EXACT MATCH | YES | OK |
| construction-(ii) bridge g=eta+h; g(center)=eta | Phase 70 | Phase 71 off-center metric | YES | YES | h_μν(center)=0, rho_J^2(center)=0 — EXACT | YES | OK |
| h_2(C_u)~R^{3,1}, mostly-minus eta from det_2; H^3=SL(2,C)/SU(2) | Phase 52 (KKT) | Phase 71 H^3 benchmark | YES | YES | slice det_2 = x0²−x1²−x2²−x3² (Minkowski 1,3); H^3 benchmark on {det_2=1} | YES | OK |
| det_3 SSOT (LOCK 0 byte-identity) | Phase 70 | Phase 71 curvature + group | YES | YES | LOCK 0 reaffirmed; 324/324 inner-derivation annihilation; CH-norm match 3 pts | YES | OK |
| Route-1 SURVIVES + R/K evidence | Phase 71-01 | Phase 71-02 cross-check | YES | YES | R_BP1..4 distinct exact rationals; reconciled in 71-VERIFICATION | YES | OK |
| reconciled SURVIVES + greenlight | Phase 71 | Phase 72/73 | YES | YES | position-dependence matterless+genuine; II(h_2(C_u))≠0 off-center | YES | OK |

**6/6 cross-phase transfers: meaning✓ units✓ test-value✓ convention✓. 0 failed transfers.**

---

## 3. Sign / factor spot-checks (the 3 load-bearing equations)

**Eq. (71.1) Totaro Riemann** R_ijkl = −(1/4) g^{pq}(f_jlp f_ikq − f_ilp f_jkq):
sign pinned on H^3 (constant NEGATIVE). Prefactor 1/4 on the numerical-factor watch list —
consistent (Totaro Cor 2.3). Engine asserts Riemann algebraic symmetries + reality. ✓

**Eq. (71.2) H^3 benchmark** K_coneHessian = −1/2; K_round = −1 = 2·K_coneHessian:
independently reproduced `K_sections=[-1/2,-1/2,-1/2]`, `round_K=-1`, `round_R=-6`,
sym_ok=True, imag_free=True. The factor-of-2 (g_slice|_apex=diag(2,2,2)=2·g_round, scaling
law K(c·g)=c⁻¹K(g)) is BENIGN and verified two independent ways. ✓ (see §5)

**Eq. (II) second fundamental form** II^n_{bc}=(1/2) f_{abc} n^a — the LINCHPIN:
independently reproduced exact over Q:
- II(h_2(C_u)) ON-center = 0 (n_nonzero=0)
- II(h_2(C_u)) OFF-center {4:1/7} = NONZERO (n_nonzero=4, det3=48/49)
- II(h_2(C_u)) OFF-center {5:1/4,8:1/3} = NONZERO (n_nonzero=8)
- II(V_0=10-dim) OFF-center {4:1/3} = 0 (n_nonzero=0) — genuinely totally geodesic

This confirms the verifier's reconciliation: II(V_0=10)=0 does NOT imply II(h_2(C_u)=4)=0
(distinct submanifolds). The 4-dim spacetime sub-slice is a curved submanifold of the
homogeneous 10-dim V_0 off-center ⇒ Gauss equation ⇒ varying induced R ⇒ SURVIVES. ✓

**Matterless position-dependence** (verifier CHECK A, reproduced exact over Q):
3 pure-V_0 basepoints give 3 distinct R: −521269105/154700283, −137053539/48874081,
−114049215/37982569. **Matterless and genuine** — this CORRECTS 71-02's localization
("SURVIVES sourced ENTIRELY by matter"), but is exactly what the reconciled SURVIVES needs.
Direction-blind within fixed magnitude ({4},{5},{6},{7}@1/3 all give −73041507/21967969);
scale-invariant (R(X)=R(2X); also {4:1/2}→−1587747/552049 reproduced). ✓

---

## 4. Wick / Riemannian-vs-Lorentzian artifact check (explicitly requested)

**No Wick artifact.** The decisive R-variation is computed on the RIEMANNIAN cone-Hessian
restriction directly (g_X=Hess(−log det), positive-definite). Construction (i) (Wick-rotate
via u) is the REJECTED fallback and is NOT on the decisive path; construction (ii) (eta from
det_2 + cone-Hessian h) is used and reduces to EXACT Minkowski at (M=0, center) (Phase-70
LOCKED, reaffirmed by center regression). The SURVIVES signal is:
- intrinsic (scalar invariants R, K — full contractions, not components),
- scale-invariant (R(X)=R(2X) — not a det_3=1 chart artifact),
- sign-pinned (R<0 everywhere; R(center)=−3; H^3 K=−1/2 constant — consistent),
- gauge-invariant (constant on det_2 leaves).

The 71-02 "disagreement" was a center-only-II + submanifold conflation, NOT a
Riemannian-vs-Lorentzian conflict. The reconciled SURVIVES is consistent with the
construction-(ii) signature bridge. **No return to Phase 70 warranted.** (Matches verifier
CHECK D.)

---

## 5. CONVENTION-TEXT CLARIFICATION (non-blocking, RECOMMENDED)

**Finding:** The `riemann_ricci_sign` custom convention records the H^3 benchmark as
"**constant curvature −1**" in THREE places that should be reconciled:
- state.json `convention_lock.custom_conventions.riemann_ricci_sign.value`:
  "...benchmark on H^3 = SL(2,C)/SU(2) (constant curvature **−1**...) at Phase 70..."
- state.json `convention_lock.conventions.covariant_derivative_sign.value`:
  "...benchmarked on H^3 (constant curvature **−1**) at Phase 70."
- CONVENTIONS.md §1 (Riemann/Ricci sign row), §4 (Riemann/Ricci sign), §8 (cross-convention
  table row "Riemann sign | H^3 benchmark | constant curvature must be **−1**").

**The Phase-71 decisive value is K = −1/2** on the ACTUAL cone-Hessian slice metric
g_ij=Hess(−log det_2); the −1 is the ROUND hyperbolic metric (Totaro −d²/4, d=2). They
differ by the benign metric-normalization factor of 2 (g_slice|_apex=2·g_round). Verified two
independent ways, sign correctly pinned, verdict sign-convention-independent.

**Recommendation (sharpens; does NOT change the verdict):** update the three convention-text
entries to record BOTH values explicitly, e.g.:
> "H^3 cone-Hessian-slice constant sectional curvature K = −1/2 (the literal pullback
> Hess(−log det_2) = 2× the round metric at the apex); round-metric reinforcement K = −1 =
> Totaro −d²/4 (d=2). The SIGN (constant, negative) is the load-bearing convention; the −1/2
> vs −1 is a metric normalization (factor of 2), not a sign error."

This is the SAME factor-of-2 already documented HONESTLY in 71-01-SUMMARY (Deviation 1, Rule
5, benign) and in derivations/71-homogeneity-curvature.tex §2 — the recommendation is only to
propagate that clarification into the convention ledger so a future phase reading "must be −1"
is not tripped.

---

## 6. STATE.md staleness (pre-existing, NOT a Phase-71 regression)

`.gpd/STATE.md` "Convention Lock" block (lines 142–177) still carries v16.0 LATTICE content:
"lattice spacing a=1", "Coupling: J>0 antiferromagnetic", "Spin basis: standard S^z
eigenbasis", "State normalization: density matrices trace 1", "Group: F_4 ... NOT E_6 ... c =
Tr(X∘Y)". This CONTRADICTS the v17.0 lock in state.json `convention_lock` + CONVENTIONS.md
(which correctly carry mostly-minus slice/Riemannian bulk, g_X=Hess(−log det), construction-
(ii) bridge, E_6=Stab(det) used in Phase 71-02). Per CONVENTIONS.md header, **state.json
wins**, and Phase 71's artifacts comply with state.json/CONVENTIONS.md, not the stale
STATE.md block. This is a known issue (memory: project_v17_bulk_geometry — "STATE.md still
carries stale v16.0 content (needs sync-state)") and is a DISPLAY/SSOT-mirror staleness, not a
Phase-71 inconsistency. **Recommend `gpd sync-state` (or notation-coordinator refresh) to
regenerate the STATE.md Convention Lock block from state.json** before Phase 72. Non-blocking
for Phase 71.

---

## 7. Engine / determinism

`python3 code/bulk_geometry_verification.py` → OVERALL: ALL_PASS, exit 0, **41/41 PASS, 0
FAIL**, reproduced across 2 full runs (deterministic). LOCK 0 (det_3 byte-identity), LOCK
7a/7b (F_4 SSOT certificate), exact-only source guard (0 octonion_algebra, 0 float-rank) all
PASS. Center regression diag(9,9,18,18)/26244, H^3 K=−1/2, off-center II linchpin, matterless
R-variation, e_6=78/Stab=61/Stab_{V_0}=45/V_0 orbit 9<10 — ALL independently reproduced exact
over Q.

---

## Summary

- **consistency_status: CONSISTENT.**
- 13/13 relevant conventions compliant; 9 correctly N/A; 0 violations.
- 6/6 provides/consumes transfers verified (meaning, units, test-value, convention).
- 3/3 load-bearing equations sign/factor spot-checked and independently reproduced.
- No Wick / Riemannian-vs-Lorentzian artifact; reconciled SURVIVES consistent with the
  construction-(ii) signature bridge.
- 2 non-blocking documentation items:
  1. **(flagged as requested)** record H^3 K=−1/2 (cone-Hessian slice) alongside the −1 (round)
     in the `riemann_ricci_sign` / `covariant_derivative_sign` convention text (state.json
     custom_conventions + CONVENTIONS.md §1/§4/§8). Benign metric-normalization factor of 2;
     sign correctly pinned; verdict unaffected.
  2. STATE.md "Convention Lock" block is stale v16.0 lattice content (state.json/CONVENTIONS.md
     are the correct v17.0 SSOT and Phase 71 complies with them); run `gpd sync-state`.

_Phase: 71-a-homogeneity-kill-gate — rapid cross-phase consistency check_
_Checked: 2026-05-30_
