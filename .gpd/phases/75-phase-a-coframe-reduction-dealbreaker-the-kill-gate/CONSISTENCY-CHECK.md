# Phase 75 Cross-Phase Consistency Check (rapid mode)

**Phase:** 75 — Phase A: Coframe-Reduction Dealbreaker (THE KILL GATE), v18.0
**Mode:** rapid (post-phase, against the FULL convention ledger)
**Date:** 2026-06-02
**Verdict:** **WARNING** — 0 Phase-75-introduced issues; 1 PRE-EXISTING non-blocking carried item (metric_signature label/glyph string, carried since Phase 73/74).

Driver `code/cartan_phaseA_coframe.py` independently re-run by the consistency checker: **exit 0, ALL_PASS, 24/24 checks PASS exact over Q** — every decisive number reproduced (image dim 4, V_0-limit 4, soldering target (1,3), foil (4,0), B rank 4, residual 21 = so(3,1)[6]+so(6)[15], anchors 61/45, Killing sig (3,3)).

---

## 1. Convention Compliance vs the Full Ledger (`gpd convention list`, 39 conventions)

| Convention (key) | Relevant? | Compliant? | Evidence in Phase 75 |
|---|---|---|---|
| metric_signature | YES | YES (content); WARNING (ledger glyph string) | Phase 75 uses clean `(+,-,-,-)` mostly-minus, `det_2=x0^2-x1^2-x2^2-x3^2`, `G=diag(+1,-1,-1,-1)`, sig `(1,3)` consistently in PLAN frontmatter, SUMMARY, and .tex. **Matches the convention CONTENT.** The ledger STRING `convention_lock.metric_signature` carries an unbalanced glyph `(+,-,-,-` (closing paren absorbed into the "via h_2(C_u)…" parenthetical) — pre-existing, not from Phase 75. See §5. |
| natural_units (hbar=1, a=1) | YES | YES | PLAN: "natural (hbar=1, dimensionless)"; exact-algebra phase, no dimensionful quantities. |
| arithmetic_field (EXACT over Q; sympy not numpy) | YES | YES | All decisive numbers from `sympy.Matrix.rank/.eigenvals/.nullspace` over QQ. fp-float-decisive explicitly rejected. Driver re-run confirms "[exact Q]" on every PASS line; 0 numpy-rank calls on decisive path. |
| det SSOT = ring_lemma_verification.py det_3; octonion_algebra BANNED | YES | YES | Source guard active; `octonion_algebra` absent from sys.modules on the decisive path (SOURCE GUARD PASS). The single `import det_3 as oa_det_3` in ring_lemma is the sanctioned in-fence oracle, never shadowing the exact primitive. fp-octonion-algebra rejected. |
| jordan_product a o b = (1/2)(ab+ba) | YES | YES | Used in B(d,d')=(d o d')\|_{V_0} and the trace-form foil Tr(jordan(cof_i,cof_j)). |
| octonion_convention (Fano e1 e2 = e4) | YES | YES | PLAN frontmatter; engine-native. |
| complex_structure (u = e_7; C_u=span{1,e_7}) | YES | YES | pi_u keeps octonion comps {0,7}, kills {1..6}; survivors {11,18,19,26}=C_u^2 confirm zero e_1..e_6 leak. |
| peirce_eigenvalues {0,1/2,1} + Peirce layout | YES | YES | V_1={0}, V_0={1..10}, V_{1/2}={11..26}; regression vs Phase 74 re-checked (BG.peirce_indices_under_E11). |
| soldering_form_e (e=pi_u(dE), V_{1/2}-valued, 16-dim) | YES (v18.0 custom, locked Ph74) | YES | e = the V_{1/2}(E_11) soldering form, C_u-reduced to a 4d coframe — exactly the locked definition. |
| pi_u_reduction (C_u/Phase-46 O->C_u bottleneck) | YES (v18.0 custom) | YES | Same mechanism as V_0=h_2(O)->h_2(C_u); V_0-limit cross-check reproduces 10->4. |
| lorentz_connection_omega (Spin(3,1) block of Spin(9,1)) | YES (forward-looking; Ph77) | YES | VALD-02 lands SO(3,1) as the Lorentz block of Spin(9,1) ⊃ Spin(3,1) x Spin(6); so(6) = internal sector. Consistent with the locked omega definition for Phase 77. |
| qgt / berry_curvature_FB (Re=FS, Im=Berry) | Partially (foil only) | YES | The (4,0) trace-form foil is identified as Re(QGT)=Fubini-Study (Provost-Vallee), the v17.0 cone-Hessian sector — correctly the FOIL, not the v18.0 verdict tensor. No conflation with the Im(QGT)/Berry sector that Phase 76/77 will compute. |
| generator_normalization / gamma_matrix (Cl(9,0), T_a=gamma_a/2) | Background | N/A-in-phase | Not directly exercised; Spin(9,1)/Spin(9) structure consistent with Cl convention. |
| group F_4 / rep 27=1+26 / cubic_norm / coupling_generator c | Background | YES | det_2, det_3, F_4 stabilizer machinery used consistently with locked defs. |
| fourier, gauge, regularization, renormalization, coordinate_system, time_ordering, covariant_derivative_sign, creation_annihilation, levi_civita_sign | NO (declared N/A: pure algebra) | N/A | Correctly inapplicable — pure exact linear algebra, no field theory/dynamics/tensors. |

**Compliance tally:** 14 relevant conventions checked → 13 fully compliant; 1 (metric_signature) compliant in content with a pre-existing ledger-string glyph WARNING. 0 violations introduced by Phase 75.

---

## 2. The Two Focus-Item Convention Traps (both PASS)

### 2a. Lorentzian (1,3) soldering target matches the locked metric_signature — PASS
- Phase 75 soldering-target signature `(1,3)` on R^{3,1} (det_2 = x0^2-x1^2-x2^2-x3^2, G=diag(+1,-1,-1,-1), timelike-positive) is **identical** to the locked metric_signature content and to the 52-kkt benchmark (`derivations/52-kkt-spacetime.tex` L204: G=diag(+1,-1,-1,-1), sig (1,3) Eq.46.4).
- Driver re-run: raw {beta,gamma,p,q} Gram → (+1,-3) AND orthonormal G → (+1,-3) — both frames AGREE on (1,3). Test value: n(cof_11) mink=[1/2,0,0,-1/2], det_2=0, x0=1/2 ≥ 0 (forward light cone, not a degeneracy — Pitfall 3 avoided).

### 2b. The Euclidean (4,0) trace-form is the FOIL, NOT relabeled as the spacetime metric — PASS (the most important trap)
- The bare Jordan trace Gram = diag(2,2,2,2), signature (4,0) Euclidean, is **explicitly and consistently** labeled the compact OP^2=F_4/Spin(9) Fubini-Study DIAGNOSTIC FOIL ("NEVER the verdict") in PLAN frontmatter (`bare_trace_gram`), SUMMARY (Eq. 75.4, key-decisions), and .tex (§Clause (b), L108-121).
- **No convention violation:** the (4,0) Euclidean form is NOT a metric_signature change and is NOT presented as the spacetime metric. The verdict metric is the SOLDERED (1,3) form (Sharpe g=e^*eta). Both readings reported transparently. This correctly defeats the Euclidean-trap false-KILL and is the honest framing that blocks fp-relabel.

---

## 3. Provides/Consumes Cross-Phase Transfers (semantic + test-value)

| Quantity | Producer | Consumer (this phase) | Meaning match | Test value | Status |
|---|---|---|---|---|---|
| Peirce layout V_{1/2}={11..26}, E_11∘δ=(1/2)δ | Phase 74 | CALC-01 basis build + regression | YES (same 16-dim half-eigenspace) | BG.peirce_indices_under_E11() == range(11,27) reproduced; kernel/span identity holds | OK |
| Calibration anchors Stab_E6(E_11)=61, Stab_V0=45=Spin(9,1), orbit(E_11)=17 | Phase 74 VALD-01 | VALD-02 (reproduced FIRST) | YES | Driver: orbit 17, Stab_E6 61, Stab_V0 45 — exact over Q | OK |
| V_0=h_2(O)→h_2(C_u)≅R^{3,1}, det_2 (1,3), G=diag(+1,-1,-1,-1) | Phase 52 (52-kkt Eq.46.4) | CALC-02 soldering TARGET + V_0-limit | YES (same Minkowski R^{3,1}) | V_0-limit dim pi_u(V_0)=4 reproduces 10→4; target sig (1,3) matches Eq.46.4 | OK |
| OD3 map V_{1/2}×V_{1/2}→V_0 surjective, rank 4 on pi_u(V_0) | Phase 52 (52-observer-uniqueness L149,L71) | CALC-02 soldering bilinear B | YES (B IS the OD3 map) | rank(B)=4; rank[image(B)\|pi_u(V_0)]=4 — solders to THE spacetime, not a look-alike | OK |
| SO(3,1) boosts B_i=L_{sigma_i}, [B_i,B_j]=-eps_ijk J_k, Killing sig (3,3) | Phase 52 (52-kkt L158) | VALD-02 forced-Lorentz check | YES (same so(3,1) Lorentz block) | Residual Lorentz block dim 6, A^T g + g A = 0, Killing sig (3,3) — matches L158 | OK |
| Spin(9,1) ⊃ Spin(3,1) x Spin(6) split | Phase 48 | VALD-02 residual decomposition | YES | residual 21 = so(3,1)[6] + so(6)[15]; so(6) trivial on spacetime | OK |

All 6 cross-phase transfers: meaning match YES, test value PASS, convention match YES. **No sign/factor/normalization drift at any phase boundary.**

---

## 4. Approximation-Validity Propagation
- Phase 75 introduces NO approximations (PLAN `approximations: []`; exact linear algebra over Q, no small parameter, no truncation). Any "approximately 4d/Lorentzian" would be fp-relabel — explicitly rejected and not present.
- No prior-phase approximation-validity range is at risk (none are numerical-parameter-bounded in a way Phase 75 could violate).

---

## 5. The PRE-EXISTING Carried Item (NOT a Phase-75 issue)

**metric_signature label/glyph reconcile** — WARNING, non-blocking, carried since Phase 73/74.

- `convention_lock.metric_signature` value string begins `"mostly-minus (+,-,-,- via h_2(C_u) det_2 Lorentzian slice; ..."` — the glyph `(+,-,-,-` has its closing paren absorbed into the following parenthetical, so a literal glyph-extraction reads an unbalanced `(+,-,-,-` rather than the clean canonical `(+,-,-,-)`.
- This is a **string/label cosmetic** item: the engine uses `eta = diag(+1,-1,-1,-1)` unchanged, and ALL Phase 75 artifacts (and the 52-kkt benchmark) use the clean `(+,-,-,-)` / `(1,3)` / `G=diag(+1,-1,-1,-1)` form. The convention CONTENT is uniform and correct across all phases.
- **Provenance:** flagged at Phase 73 ("metric_signature label/glyph reconcile (operationally inert)") and Phase 74 ("consistency WARNING — 1 PRE-EXISTING non-blocking metric_signature label/glyph item; 0 Phase-74-introduced"). The recommended fix (gpd-notation-coordinator: reconcile the glyph string to "mostly-minus (+,-,-,-)") was deferred as non-blocking. Phase 75 did not touch it and did not make it worse.
- **Attribution: PRE-EXISTING, carried — NOT introduced by Phase 75.**

---

## 6. Summary

- **Phase-75-introduced consistency issues: 0.**
- **Pre-existing carried items: 1** (metric_signature ledger-string glyph; cosmetic, operationally inert).
- Driver reproduced exact over Q (exit 0 / ALL_PASS / 24-of-24) by the consistency checker independently.
- All convention-sensitive objects in the focus list (metric (1,3), (4,0) foil-not-metric, soldering_form_e/pi_u_reduction/omega, qgt Re/Im split, EXACT-over-Q, V_0-limit + Peirce layout reproductions) are consistent with the locked ledger and with Phases 48/52/74.
- **Nothing blocks the Phase 76/77 greenlight from a consistency standpoint.** The downstream binding convention (spacetime metric = the soldered (1,3) Lorentzian form, NOT the intrinsic Euclidean OP^2 metric; SO(3,1) the FORCED Lorentz structure group for omega) is correctly stated and carried.

**consistency_status: WARNING** (1 pre-existing carried item; 0 Phase-75 issues)
