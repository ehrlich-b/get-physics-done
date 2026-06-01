# Research Digest: v17.0 — Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry

Generated: 2026-06-01
Milestone: v17.0
Phases: 70–73 (4 primary; Phase 70 superseded by the inserted decimal Phase 70.1)

## Narrative Arc

v17.0 opened a fresh, intrinsic physics-side route to gravity, explicitly replacing two dead routes — the abandoned lattice/Fisher continuum limit, and the circular det/GST/Weinberg supergravity Lagrangian (where −R/2 is fixed by an assumed SUSY closure). The thesis: the positive cone of h_3(O) is a Riemannian symmetric space with the canonical metric g_X = Hess(−log det X) (Faraut–Korányi); a primitive idempotent E_11 picks the spacetime Peirce slice V_0 ⊇ h_2(C_u) ~ R^{3,1}, and an off-center state picks a basepoint. The milestone was designed as a hard-gated KILL test — a decisive verdict either way is a full pass (NEGATIVE-RESULT-IS-SUCCESS) — run in the order A0 → A (homogeneity, cheap and first) → B (matter-sourcing) → C (Einstein structure).

The work proceeded: **(70/70.1)** certify a single source-of-truth cubic-norm engine (det_3, F_4-invariant, byte-identical to the warm v16.0 engine) and fix the Riemannian-cone → Lorentzian-slice signature bridge (construction (ii): background η from h_2(C_u)'s det_2 + cone-Hessian perturbation), reducing to EXACT Minkowski at (M=0, center). Phase 72's first-result gate then exposed a fork: the cone-Hessian M=0 vacuum is the non-Einstein static product R_time × H³ (Ricci eigenvalues {0,−1,−1,−1}, R=−3), while the η+h bridge is flat there — they disagree about the vacuum. The inserted **Phase 70.1** re-adjudicated this and (human-ratified) selected the **η+h bridge** as the physical spacetime metric: the literal "cone-Hessian IS the metric" thesis is FALSIFIED (a spin-2 field on a fixed non-Einstein background is non-gauge ⇒ not a graviton), but the route is RESTATED not abandoned — the cone-Hessian is the matter source/information structure (its V_0↔V_{1/2} cross-terms 2Re((x₂x₁)x₃) source the perturbation h), and the flat M=0 vacuum is DERIVED from the KKT det_2 form (not an inserted Λ).

With the metric fixed, the gated chain ran to a decisive verdict. **(71, the KILL gate) SURVIVES:** the inherited h_2(C_u) slice metric is genuinely position-dependent — curvature scalar invariants vary exact-over-Q across distinct-det_2 basepoints; the slice-preserving stabilizer Stab_{V_0}=45=Spin(9,1) is non-transitive (orbit 9 < 10), leaving a single genuine modulus (the Spin(9,1)-invariant det_2), and the position-dependence is matterless and direction-blind (not a coordinate artifact). **(72, matter-sourcing) SURVIVES (qualified):** matter in V_{1/2} dominantly (~94%) cross-term-sources the curvature of the flat KKT slice g=η+h (cross-term off-switch R_full≈4008 → R_off≈247, a 16× decisive reduction); M=0 is flat (structurally DERIVED — the difference potential vanishes identically at M=0); curvature →0 as ‖M‖⁴ and carries genuine traceless-Ricci S≠0 and Weyl≠0. A consequential by-product: the linear-in-M metric response h⁽¹⁾=0 identically, so matter perturbs g at O(‖M‖²). **(73, Einstein structure) NONE:** with an independent stress tensor T_μν and intrinsic coupling κ frozen from the V_{1/2} cross-terms BEFORE any curvature was computed, the full nonlinear Einstein tensor G_μν[g] over a 12-point (M,x) family is NOT reproduced by κT+Λg for any single global (κ,Λ), against either frozen T, at finite-M or leading order. The matter-sourced curvature is genuinely curved (S≠0, Weyl≠0) but not of Einstein form.

The verdict is a clean, decisive NEGATIVE on the strongest claim: **the h_3(O) symmetric-cone geometry yields a curved, matter-sourced, position-dependent Lorentzian spacetime slice that is NOT Einstein-structured** — achieved with no lattice, no posited Lagrangian, no SUSY, no observer-ensemble, and (audit-certified) no GST/SUSY/−R/2/Weinberg circularity. The route survived the cheap homogeneity KILL gate and matter-sourcing, then failed cleanly at Einstein structure. Per the milestone's binding discipline, "curved but not Einstein-structured" is an acceptable full result, reported at true strength (not inflated to a leading-order Einstein claim, not deflated into an inserted-Λ circularity).

## Key Results (exact over Q)

| Phase | Result | Equation / Value | Validity / Regime | Confidence |
| ----- | ------ | ---------------- | ----------------- | ---------- |
| 70 | det_3 certified SSOT (F_4-invariant cubic norm) | cross-term 2Re((x₂x₁)x₃); 324/324 inner-derivation annihilation; buggy order rejected off-by-16 | all of v17.0 | HIGH |
| 70 | Signature bridge → exact Minkowski at center | g_μν(center, M=0) = η_μν, sig (1,3); Hess(−log det)\|_{I/3} = diag(9,9,18,18), det 26244 | M=0, center | HIGH |
| 70.1 | Physical metric = η+h bridge; cone-Hessian-is-metric FALSIFIED | cone-Hessian M=0 vacuum = R_time×H³, Ric eig {0,−1,−1,−1}, R=−3, K(p,q)=−1/2 | M=0 | HIGH (human-ratified; independent Levi-Civita re-derivation) |
| 71 | Homogeneity KILL gate: SURVIVES | R(x) varies: e.g. −1047519795/310570129 vs −130237700283/50153154601 at distinct basepoints; dim Stab_{E_6}(E_11)=61, Stab_{V_0}=45=Spin(9,1) non-transitive (orbit 9<10) | off-center, dim-4 h_2(C_u) slice | HIGH |
| 72 | Matter-sourcing: SURVIVES (qualified) | cross-term off-switch R_full≈4008 → R_off≈247 (16× reduction); R[g] ~ a_4‖M‖⁴, a_4 = 395268903/24010000; M=0 flat (R=S=Weyl=0, structural) | small ‖M‖, sig (1,3) splice | HIGH |
| 72 | Linear metric response vanishes | h⁽¹⁾ = 0 identically ⇒ matter enters g at O(‖M‖²); emitted h⁽²⁾ (4×4 rational) | all M | HIGH |
| 73 | Independent RHS frozen (DERV-03) | T[ψ], ψ=2Re((x₂x₁)x₃), T_μν=∂_μψ∂_νψ−½η(∂ψ)²; κ_ψ=32016781143/5929 (t⁴-matched); ALT σ-model T[V_{1/2}], κ_σ (t² order-mismatch); all conserved, no Ric/R/G | flat η | HIGH |
| 73 | **Einstein structure: NONE (curved but not Einstein-structured)** | no single global (κ,Λ) gives G[g]=κT+Λg vs either T, finite-M or t⁴; best-Λ residual ‖·‖≈7209 (T[ψ]) / 7190 (T[σ]); R not ∝ g at even one point; κT ~10³ smaller than G | 12-point (M,x) family | HIGH (human-ratified; orchestrator-reproduced) |
| 73 | Curvature decomposition (n=4) | R≈4008, traceless-Ricci S≠0 (10/16), Weyl≠0 (72/256), trace_S=0, reconstruction exact | anchor M_0 and family | HIGH |

## Methods Employed

- **Phase 70:** Exact-SymPy h_3(O) cubic-norm engine over Q (copy/extend `code/ring_lemma_verification.py` → `code/bulk_geometry_verification.py`); Cayley-Hamilton + multiplicativity + 324/324 inner-derivation certification of det_3; construction-(ii) signature bridge (η from h_2(C_u)'s det_2).
- **Phase 70.1:** Background-agnostic Einstein-condition test (Ricci endomorphism g⁻¹Ric eigenvalues, signature-independent); independent Levi-Civita Christoffel/Riemann cross-check vs the Totaro closed form; linearized-spin-2 gauge-obstruction reasoning on a non-Einstein background.
- **Phase 71:** Totaro's Hessian-curvature formula (R depends only on 3rd derivatives of det; det cubic ⇒ exact, cheap) — hand-rolled Ricci scalar / Kretschmann / sectional curvature; off-center expansion around I/3 (rho_J, not the spacetime coordinate); second fundamental form II via Gauss; exact-over-Q orbit/stabilizer rank (`orbit_dimension_gate.py`); e_6 = f_4 ⊕ L(traceless) = 78.
- **Phase 72:** Difference-potential isolation h(x;M) = H_source(x;bg+M) − H_source(x;bg) (the B1 definition, cancels the matterless background); curvature of g=η+h with indices raised by g⁻¹=(η+h)⁻¹ (NOT the bare cone-Hessian H_bg⁻¹); cross-term ON/OFF off-switch (full det_3 vs block-diagonal det_block); n=4 Ricci decomposition (scalar / traceless-Ricci S / Weyl); amplitude series M = t·M_0 (matter to rationals before any symbolic inverse).
- **Phase 73:** Construction-before-comparison (DERV-03): canonical scalar stress tensor T[ψ]=∂ψ∂ψ−½η(∂ψ)² and a σ-model T[V_{1/2}], frozen with an AST-based no-Ric/R/G guard; intrinsic κ as a leading-order scale ratio at one reference direction (frozen, not −R/2, not per-point); full nonlinear G_μν[g]=Ric−½gR over an (M,x) family with eig_signature_count gating to the (1,3) splice; single-global-(κ,Λ) over-determined fit (no per-point tuning, no LSQ-rounding); the linear box-h̄⁽²⁾ diagnostic (gauge-degenerate, demoted).

## Convention Evolution

| Phase | Convention | Description | Status |
| ----- | ---------- | ----------- | ------ |
| 70 (lock 0d10eeea) | Metric signature | mostly-minus slice (sig (1,3)) via h_2(C_u) det_2; bulk cone Riemannian positive-definite (v16.0 Riemannian-Fisher RETIRED) | Active |
| 70 | det SSOT | det_3 = `code/bulk_geometry_verification.py` (byte-identical to ring_lemma_verification); cross-term 2Re((x₂x₁)x₃); `octonion_algebra.py` BANNED on the decisive path | Active |
| 70 | Potential | g_X = Hess(−log det) (NOT det); index/coordinate map for V_0 sub-slice {17,18,19,26} == engine {x1,x2,x3,x10} | Active |
| 70.1 | Physical metric | the η+h bridge is the spacetime metric; "cone-Hessian IS the metric" FALSIFIED (its M=0 vacuum non-Einstein R×H³). SUPERSEDES the earlier "center is Einstein, Λ<0" text (CONVENTIONS §6) | Active (supersedes) |
| 72 | M=0 baseline | flat (R=S=Weyl=0), DERIVED from KKT det_2 — NOT a pure cosmological constant; Λ=0, no Λ tripwire | Active |
| 73 | eta_bg / box | eta_bg null-aligned constant [[0,½,0,0],[½,0,0,0],[0,0,−1,0],[0,0,0,−1]]; box = 4∂_β∂_γ − ∂_p² − ∂_q² (built from eta_bg⁻¹, never diag) | Active |
| 73 | Arithmetic | EXACT over Q on every decisive verdict (fp-float-decisive rejected); ranks via sympy, never numpy | Active |

**Non-blocking notation follow-up (carried, not gating):** the state.json `convention_lock.metric_signature` string pairs the label "mostly-minus" with the glyph "(-,+,+,+)" (conventionally mostly-plus); operationally inert (every decisive quantity flows from the fixed eta_bg, genuine sig (1,3)). Also record cone-Hessian K=−1/2 alongside round −1 in the riemann_ricci_sign line. A notation-coordinator pass can reconcile both.

## Figures and Data Registry

| File | Phase | Description | Paper-ready? |
| ---- | ----- | ----------- | ------------ |
| (none) | — | v17.0 produced no figures/plots — it is an exact-symbolic computation milestone; results are equations and exact rationals | n/a |

## Open Questions (deferred / future work)

1. **(EXTD-01)** Full dim-10 V_0 = h_2(O) curvature (decisive physics was on the 4-dim h_2(C_u) slice; the dim-10 symbolic inverse times out — high-precision fallback only).
2. **(EXTD-02)** Dynamics: solving/interpreting the matter field equations for M, beyond a fixed background source.
3. **(EXTD-03)** The precise non-compact stabilizer of a primitive idempotent in E_6(-26) (the Spin(9,1) Levi appeared as Stab_{V_0}=45) and its gravitational interpretation.
4. **(EXTD-04)** Paper write-up of the curved-but-not-Einstein result (`paper6-bulk-geometry`).
5. **Interpretation:** what gravitational/physical content (if any) a curved-but-not-Einstein matter-sourced slice carries — and whether a different intrinsic coupling, a non-minimal T, or a higher Peirce structure could change the C verdict without importing the dead routes.
6. **Relation to v12/v13:** the v17.0 intrinsic-curvature route did not reach Einstein form; the v12/v13 det/GST/Weinberg route (which did, via the assumed SUSY closure) stands as an independent — and, by this milestone's lights, circular — alternative. The honest comparison is a write-up question.

## Dependency Graph

    Phase 70 "A0 — Engine & Signature Bridge"  [SUPERSEDED by 70.1]
      provides: certified det_3 SSOT engine; construction-(ii) bridge; exact-Minkowski reduction; H³ benchmark; index map
    -> Phase 70.1 "Revise A0 — physical-metric selection"
      requires: 70 engine + bridge
      provides: VERDICT η+h is the spacetime metric (cone-Hessian-is-metric FALSIFIED); cone-Hessian = matter-source; flat vacuum DERIVED
    -> Phase 71 "A — Homogeneity KILL Gate"
      requires: 70 engine (via 70.1)
      provides: VERDICT SURVIVES (slice metric position-dependent); Stab_{E_6}(E_11)=61, Stab_{V_0}=45=Spin(9,1); II machinery; off-center curvature engine
    -> Phase 72 "B — Matter-Sourcing (matter-on-flat)"
      requires: 71 SURVIVES + the slice metric
      provides: VERDICT SURVIVES (qualified) (~94% cross-term sourcing); curvature-of-g engine (Section 13); h⁽¹⁾=0, emitted h⁽²⁾; a_4; ON/OFF off-switch det_block
    -> Phase 73 "C — Einstein Structure"
      requires: 72 matter-sourced curvature; h⁽²⁾; a_4
      provides: VERDICT NONE (curved but not Einstein-structured); frozen T[ψ]/T[V_{1/2}] + κ; h2_field/box (Section 14); circularity audit (VALD-05)

**Critical path:** 70 → 70.1 → 71 → 72 → 73 (strictly sequential hard-gated chain; each verdict gated the next).

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
| ----------- | ------ | ------------ | ---------- |
| SETU-01 (certified det_3) | Complete | Phase 70 | det_3 SSOT, F_4-invariant, 324/324 |
| SETU-02 (signature bridge) | Complete | Phase 70 → 70.1 | construction (ii); η+h selected as physical metric |
| DERV-01 (slice metric g=η+h) | Complete | Phase 71 | exact-over-Q off-center expansion |
| CALC-01/02 (Stab + II) | Complete | Phase 71 | Stab_{V_0}=Spin(9,1) non-transitive; II(h_2(C_u))≠0 off-center |
| VALD-01 (homogeneity KILL gate) | Complete — **SURVIVES** | Phase 71 | R(x), K(x) vary exact over Q |
| VALD-02/03 (Minkowski + H³) | Complete | Phase 70/71 | exact Minkowski at center; H³ K=−1/2 |
| DERV-02 (Riemann via Totaro) | Complete | Phase 72 | curvature of g=η+h, hand-rolled cross-check |
| CALC-03/04 (cross-term on/off + scaling) | Complete | Phase 72 | 16× off-switch reduction; R~a_4‖M‖⁴ |
| VALD-04 (M=0 baseline) | Complete — **SURVIVES (qualified)** | Phase 72 | M=0 flat structurally DERIVED; S≠0/Weyl≠0 for M≠0 |
| DERV-03 (independent T_μν) | Complete | Phase 73 | T[ψ] + T[V_{1/2}] + κ frozen, no Ric/R/G |
| CALC-05 (Einstein test) | Complete — **NONE** | Phase 73 | no global (κ,Λ) for G[g]=κT+Λg, finite-M or t⁴ |
| VALD-05 (circularity audit) | Complete | Phase 73 | no GST/SUSY/−R/2/Weinberg/Jacobson import |

**Milestone verdict:** all 15 requirements complete; all 4 contract claims resolved. The decisive can-fail Einstein test returned NONE (curved but not Einstein-structured) — a full-pass negative result on the strongest claim, with the route surviving the homogeneity KILL gate and matter-sourcing. NEGATIVE-RESULT-IS-SUCCESS.
