# Requirements: Gravity as the Curvature of the Peirce-Frame (Cartan/MacDowell-Mansouri) Connection on h_3(O)

**Defined:** 2026-06-01
**Milestone:** v18.0 (physics-side; Phases 74–78, continuing from v17.0's Phase 73)
**Core Research Question:** Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself? — _this milestone tests one route to the GR endpoint: is gravity the curvature of the antisymmetric/Lie-sector (Cartan/MM) Peirce-frame connection on h_3(O)?_

> **Framing.** The route mines the **imaginary part of the self-model QGT (Berry curvature)** — the Lie sector — where the dead v17.0 cone-Hessian route was the **real part** (Fubini-Study). A genuinely different tensor, so the v17.0 NONE verdict does NOT bind it. Hard KILL gates first (Phase A coframe reduction, Phase A.5 Berry same-wall) decide survival before the expensive connection machinery. NEGATIVE-RESULT-IS-SUCCESS: a clean KILL/SOFT-KILL is a full, publishable pass; the most likely real outcome is forced-coframe-but-imported-action (B yes, C no), reported as `fp-imported-action`. EXACT over Q on every decisive verdict (Berry sector over Q(i); split Re/Im); det SSOT = `ring_lemma_verification.py` det_3; `octonion_algebra.py` BANNED.

## Primary Requirements

### Phase 0 (→ Phase 74): Engine Recovery, Tangent Identity & Calibration

- [ ] **DERV-01**: Re-pass the det SSOT (`code/ring_lemma_verification.py` det_3) — Cayley-Hamilton + 324/324 inner-derivation annihilation = dim f_4 = 52; confirm `octonion_algebra.py` is NOT imported on any decisive path.
- [ ] **DERV-02**: Verify EXACTLY over Q the load-bearing tangent identity `E_11∘δ = (1/2)δ` for a basis of `δ ∈ V_{1/2}(E_11)`, and that the tangent space to the primitive-idempotent variety at `E_11` is exactly `V_{1/2}(E_11)` (16-dim). _(Peirce-under-E_11 via `bulk_geometry_verification.py:peirce_indices_under_E11` / `embedding_under_E_verification.py` — `peirce_coupling.py` does not exist.)_
- [ ] **VALD-01**: Reproduce the calibration anchors via `code/orbit_dimension_gate.py` (single-copy dim 24 / Spin(8)=28 / trdeg 3; e_6=78=52+26; orbit(E_11)=17; Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1)) AND re-pass the H^3 cone-Hessian sign benchmark K=−1/2, BEFORE any new structure-group count or curvature verdict.

### Phase A (→ Phase 75): Coframe-Reduction Dealbreaker — THE KILL GATE (do first; cheap)

- [ ] **CALC-01**: Compute the EXACT image dimension over Q of `π_u(V_{1/2}(16))` under the C_u/Phase-46 bottleneck (expect 4). **KILL if ≠ 4.**
- [ ] **CALC-02**: Compute the EXACT Gram-eigenvalue signature over Q of the induced coframe pairing (expect Lorentzian (1,3) / mostly-minus). **KILL if not Lorentzian.**
- [ ] **VALD-02**: Decide (forced-vs-arbitrary) whether the residual structure group on the 4-dim coframe contains SO(3,1) and is FORCED by `(E_11,u)` alone, not by an arbitrary extra choice. **KILL (`fp-arbitrary-reduction`) if the 4d reduction requires an arbitrary choice.**

### Phase A.5 (→ Phase 76): Berry-Curvature Same-Wall Gate — SOFT KILL

- [ ] **CALC-03**: Compute the QGT of the idempotent state family `|ψ(x)⟩` at `E(x)` (projector form `Q=Tr(P ∂P ∂P)`, gauge-invariant) and confirm its REAL part reproduces the dead Fubini-Study/cone-Hessian `Hess(−log det)`. **HARD STOP if it does not (the QGT construction is wrong).**
- [ ] **VALD-03**: Well-definedness checkpoint (survey-added) — establish that `Im(QGT) = F_B` is a well-defined, generically-NONZERO 2-form on the 4-dim slice AFTER the C_u breaking (OP^2=F_4/Spin(9) carries no invariant 2-form, so a nonzero Berry 2-form must be born from the breaking), BEFORE testing its shape.
- [ ] **CALC-04**: Classify `F_B` at `M=0` — zero/flat, pure-Λ (`F_B ~ e∧e`), or other (report the vacuum level; expected flat/pure-Λ per CONVENTIONS §6; do NOT reintroduce Λ<0).
- [ ] **VALD-04**: Same-wall test — with `M∈V_{1/2}` on, decide whether the matter-sourced `F_B` (and the ε-contraction of `F_B∧F_B` onto the Lorentz block) is transverse/Einstein-shaped vs EM-shaped (traceless `T^μ_μ=0`, `~F²`, conformal), matching M-power + tensor-structure + support against an independently-frozen `V_{1/2}` stress-energy `T[M]`; use gauge-invariant scalars (the degenerate-bundle Berry curvature is non-abelian/Wilczek-Zee, gauge-COVARIANT not invariant). **SOFT KILL if it reproduces the v17.0 cone-Hessian mismatch (support disjoint from T[M], no order-matching).**

### Phase B (→ Phase 77): Full Cartan Curvature = 4d Gravity (only if A and A.5 survive)

- [ ] **DERV-03**: Confirm `e = π_u(dE)` is a non-degenerate soldering form on the 4-dim slice: `det(e^a_μ) ≠ 0` (exact over Q).
- [ ] **DERV-04**: Extract `ω` = the Lorentz Spin(3,1) part of the ambient Spin(9,1) connection compatible with `e` (metric/torsion condition or the canonical f_4/e_6 reductive split `g=h⊕m`); do NOT use the raw 45-dim Spin(9,1) curvature.
- [ ] **CALC-05**: Assemble `A = ω⊕e` (so(3,2)/so(4,1)/iso(3,1)) and compute `F = dA + A∧A` symbolically; identify the Lorentz block `R(ω)+Λe∧e` with the 4d Riemann tensor (cross-checked against an independent Totaro/Levi-Civita computation on ≥5 components, reusing `bulk_geometry_verification.py`); report the translation/torsion block `de+ω∧e`.
- [ ] **VALD-05**: At `M=0`, test whether the Lorentz block is Einstein/(A)dS (`R_μν ~ Λg_μν`), sign-fixed by the K=−1/2 benchmark (expected flat/pure-Λ, MEASURE Λ); then turn on `M∈V_{1/2}` and characterize the matter-sourced Riemann.

### Phase C (→ Phase 78): Circularity Audit (the GST sin, re-armed)

- [ ] **VALD-06**: Decide whether the MM ε-contraction (the Spin(9,1)→SO(3,1) breaking + ε-tensor that turns `F∧F` into Einstein-Hilbert+Λ) is FORCED by the h_3(O) trace-form/cubic-norm pairing — concretely, whether the space of trace-form-invariant quadratic-in-F contractions is **1-dimensional AND equals the ε-contraction with a cubic-norm-fixed normalization** (**STRONG WIN**) — or appears only because an MM/EH action was posited by hand (**`fp-imported-action`**, honest partial, NOT a derivation). Report at true strength; frame Singh/Castro/GST as the contrast class.

## Follow-up Requirements

Deferred to future work / not in this milestone's roadmap.

- **EXTD-01**: Non-compact `so(3,1)⊂so(9,1)` sub-block extraction transporting the compact F_4/Spin(9) canonical connection to the `e_{6(-26)}` real form (a Phase-B construction detail; deepen only if B reaches it).
- **EXTD-02**: If Phase C reaches STRONG WIN, the write-up (paper6-cartan-tetrad) and the relation to the v12/v13 (Einstein via posited SUSY) and v17.0 (cone-Hessian NONE) routes.
- **EXTD-03**: Dynamics/field equations of the matter M; quantization; cosmology — out of program scope here.

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| The v17.0 cone-Hessian Riemann (symmetric sector / real-part QGT) as load-bearing | This route is the antisymmetric/Lie sector (imaginary part) — a DIFFERENT tensor; cone-Hessian is for the real-part consistency check only |
| Positing an MM/EH action to obtain the Einstein term | That is exactly `fp-imported-action` (the GST sin); Phase C audits it |
| det/GST/Weinberg N=2 supergravity-Lagrangian route (47-*..50-*, 53-*) | CIRCULAR; GST E_{6(-26)}/F_4 geometry citable for orientation only |
| Lattice/Fisher continuum-limit route | ABANDONED |
| Any thermodynamic/modular/ensemble (Jacobson/Verlinde/Vanchurin/Connes-Rovelli) argument | REJECTED as woo (standing constraint) |
| Re-deriving SOLID standard math (OP^2=F_4/Spin(9); QGT real/imag split; MM=broken-Cartan curvature; h_2(C_u)≅R^{3,1}) | Cite, do not re-derive |
| `octonion_algebra.py` on any decisive path | BANNED (buggy associator); det SSOT = ring_lemma_verification.py det_3 |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| DERV-01 | Exact over Q; engine ALL_PASS (exit 0) | CH + 324/324 inner-derivation annihilation; source guard 0 octonion_algebra |
| DERV-02 | Exact over Q | `E_11∘δ=(1/2)δ` for all V_{1/2} basis elements; `dim T_{E_11}OP^2 = 16` |
| CALC-01/02 | Exact over Q (rank/eigenvalues) | `sympy.Matrix.rank` (never numpy); exact Gram eigenvalues / signature |
| VALD-02 | Exact over Q | residual-structure-group generators over Q; forced-vs-arbitrary argument |
| CALC-03 | Exact over Q(i); Re-part exact over Q | `Re(QGT)` byte-matches the cone-Hessian `Hess(−log det)` |
| VALD-04 | Exact over Q(i); gauge-invariant scalar | M-power + tensor-structure + support match vs independently-frozen T[M]; EM-shaped discriminants (traceless, ~F²) |
| CALC-05 | Exact over Q | Lorentz block == independent Totaro/Levi-Civita Riemann on ≥5 components |
| VALD-05 | Exact over Q | K=−1/2 benchmark sign-pin; `R_μν ~ Λg_μν` test |
| VALD-06 | Exact over Q | dim of the trace-form-invariant quadratic-in-F contraction space (== 1 and == ε-contraction ⇒ FORCED) |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ |
| CALC-01/02, VALD-02 (claim-coframe-reduction) | image dim + Gram signature + forced-vs-arbitrary verdict (deliv-phaseA) | V_0→h_2(C_u)≅R^{3,1} precedent (52-kkt); Baez/McCrimmon | `fp-arbitrary-reduction`; relabeling non-4d/non-Lorentzian as "approximately"; `fp-float-decisive` |
| CALC-03/04, VALD-03/04 (claim-berry-same-wall) | F_B = Im(QGT); vacuum level; Einstein-vs-EM shape (deliv-phaseA5) | Provost-Vallée 1980; Re(QGT)=cone-Hessian anchor; v17.0 Ph73 same-wall lesson | `fp-relabel` (EM-shaped as Einstein); non-abelian gauge-covariance mistake |
| DERV-03/04, CALC-05, VALD-05 (claim-cartan-gravity) | F=dA+A∧A; Lorentz block = 4d Riemann (cross-checked); vacuum + matter-sourced Riemann (deliv-phaseB) | Wise gr-qc/0611154; H^3 K=−1/2; in-repo Totaro/Levi-Civita harness | reusing cone-Hessian Riemann; raw 45-dim Spin(9,1) curvature as the 4d connection |
| VALD-06 (claim-forced-einstein) | forced-vs-posited verdict: 1-dim trace-form contraction == ε? (deliv-phaseC) | MM 1977; Wise; GST/Singh/Castro contrast class | `fp-imported-action` (Einstein only via posited action) |

## Traceability

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| DERV-01 | Phase 74 (0: Engine & Calibration) | Pending |
| DERV-02 | Phase 74 (0: Engine & Calibration) | Pending |
| VALD-01 | Phase 74 (0: Engine & Calibration) | Pending |
| CALC-01 | Phase 75 (A: Coframe Reduction — KILL) | Pending |
| CALC-02 | Phase 75 (A: Coframe Reduction — KILL) | Pending |
| VALD-02 | Phase 75 (A: Coframe Reduction — KILL) | Pending |
| CALC-03 | Phase 76 (A.5: Berry Same-Wall — SOFT KILL) | Pending |
| VALD-03 | Phase 76 (A.5: Berry Same-Wall — SOFT KILL) | Pending |
| CALC-04 | Phase 76 (A.5: Berry Same-Wall — SOFT KILL) | Pending |
| VALD-04 | Phase 76 (A.5: Berry Same-Wall — SOFT KILL) | Pending |
| DERV-03 | Phase 77 (B: Full Cartan Curvature) | Pending |
| DERV-04 | Phase 77 (B: Full Cartan Curvature) | Pending |
| CALC-05 | Phase 77 (B: Full Cartan Curvature) | Pending |
| VALD-05 | Phase 77 (B: Full Cartan Curvature) | Pending |
| VALD-06 | Phase 78 (C: Circularity Audit) | Pending |

**Coverage:**

- Primary requirements: 15 total (DERV ×4, CALC ×5, VALD ×6)
- Mapped to phases: 15
- Unmapped: 0

---

_Requirements defined: 2026-06-01_
_Last updated: 2026-06-01 after v18.0 literature survey_
