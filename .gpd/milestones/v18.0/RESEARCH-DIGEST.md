# Research Digest: v18.0 — Gravity as the Curvature of the Peirce-Frame (Cartan/MacDowell-Mansouri) Connection on h_3(O)

Generated: 2026-06-03
Milestone: v18.0
Phases: 74–78 (5 phases, 8 plans)

## Narrative Arc

v18.0 opened a fresh physics-side route to gravity on the *same* endpoint as the dead v17.0 route but a **genuinely different tensor**. Every prior route in the program built the metric from the **symmetric (Jordan) sector** — `Hess(−log det)` is symmetric, and v17.0 read it as the **real part** of the self-model quantum geometric tensor (QGT) and returned NONE. The Provost-Vallée (1980) Re/Im split is the load-bearing justification that NONE binds only `Re(Q)`: the **imaginary part** — the Berry curvature, equivalently the curvature 2-form `F = dA + A∧A` of the antisymmetric/Lie-sector Peirce-frame Cartan/MacDowell-Mansouri connection `A = ω⊕e` — was never touched, so the v17.0 verdict does NOT bind it. The milestone was structured as a hard-gated KILL test (NEGATIVE-RESULT-IS-SUCCESS), cheap gates first, run 74 → 75 → (76) → 77 → 78. **Scope = GR** (the Lorentz Spin(3,1) block) — not the Standard Model.

The work proceeded. **(74, Phase 0)** re-certified the det SSOT (det_3, F_4-invariant, 324/324 inner-derivation annihilation = dim f_4 = 52, byte-identical to the warm v16.0/v17.0 engine; `octonion_algebra.py` confirmed absent on every decisive path) and established the load-bearing geometric fact exactly over Q: the soldering form `dE` is `V_{1/2}`-valued — `E_11∘δ=½δ` for a full `V_{1/2}` basis, and the Zariski tangent space `T_{E_11}OP² = V_{1/2}(E_11)`, dim 16 (Jacobian rank 11, kernel == span{11..26}, 16 = 17−1). All v17.0 calibration anchors (single-copy 24 / Spin(8)=28 / trdeg 3; e_6=78=52+26; orbit(E_11)=17; Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1)) and the K=−1/2 cone-Hessian sign benchmark reproduced byte-for-byte.

**(75, Phase A — THE KILL GATE) SURVIVES.** With `(E_11, u=e_7)` fixed, the Phase-46 `C_u` bottleneck `π_u` reduces the 16-dim `V_{1/2}` soldering form to a 4-dim Lorentzian coframe carrying SO(3,1), FORCED — all three clauses exact over Q. Image dim `π_u(V_{1/2}(16)) = 4` (survivors {11,18,19,26}=C_u², matching the V_0-limit `π_u(V_0)=4`); the soldering-form metric (the Peirce bilinear B into V_0≅R^{3,1}) has signature **(1,3)**, B is rank 4 surjective with a forward null cone and `image(B)==π_u(V_0)` (the bare Jordan trace Gram `diag(2,2,2,2)=(4,0)` is the **Euclidean OP² Fubini-Study foil**, reported for transparency, NOT the verdict). The residual structure group is `21 = so(3,1)[6] ⊕ so(6)[15]`, with **so(3,1) FORCED by (E_11,u)** (Killing signature (3,3), kills det_2) and the so(6) a genuine **ideal** acting trivially on spacetime (`res/so(6)=so(3,1)`) — so `fp-arbitrary-reduction` is averted, "4" is EARNED not assumed. New binding downstream convention: the spacetime metric is the soldered (1,3) Lorentzian form (NOT the Euclidean OP² metric); SO(3,1) is the FORCED Lorentz structure group for `ω`.

**(76, Phase A.5 — Berry curvature) EXECUTED, then RETIRED as a gate.** The canonical Berry curvature `F_B = Im(QGT)` was computed (well-definedness born-from-breaking; M=0 pure-Λ/Kähler vacuum `F_B=−2ω_K`; matter-on shape) — 25/25 + 43/43 PASS exact over Q(i), orchestrator-reproduced. The proposed SOFT KILL was **OVERTURNED (Bryan)**: A.5 tested the **wrong object**. The Maxwell stress and Pontryagin `F_B∧F_B` are *quadratic* in `F_B`, whereas the Einstein-Hilbert object `ε_{abcd}R^{ab}∧e^c∧e^d` is *linear* in the Riemann `R[ω]` and wedged with the tetrad; "a 2-form's Maxwell stress is traceless in 4d" is a universal tautology that *also* kills real GR ⟹ the discriminant is invalid for gravity. Corrected framing: `F_B` is the **internal `so(6)=SU(4)` gauge curvature** (a deferred SM-unification bonus, NOT a v18.0 deliverable); **gravity is the soldering-form Riemann `R[ω]`** = the Lorentz block of `F = dA + A∧A`. The "75 ∧ 76 conjunctive" gate was RETIRED — Phase 75 (SURVIVES) alone greenlit Phase B. A cheap pre-check confirmed `g = e·e` is `(1,3)` Lorentzian = the v17.0 η baseline but a DIFFERENT curvature mechanism (soldering/Cartan `ω(e)` vs cone-Hessian cross-terms) ⟹ Phase B is a genuine, non-redundant test.

**(77, Phase B — Full Cartan Curvature) NEGATIVE / `fp-imported-action` partial.** Phase B opened with a flatness sub-gate (the v18.0 analog of the v17.0 homogeneity dealbreaker): `R[ω(e)] ≠ 0` for `M≠0` (136/256 components nonzero exact over Q, Ricci scalar ≠ 0; M=0 baseline flat) ⟹ **PROCEED** (not rigid/integrable, no trivial death). The coframe `e=π_u(dE)` is invertible (`det(e)=½≠0`, sig (1,3); built via the contract-sanctioned Lagrange-congruence fallback after the `π_u(dE)` symbolic route hit the watchdog cliff — frame-invariant, so the verdict is unaffected); the closed-form torsion-free Levi-Civita `ω(e)` is antisymmetric and sign-pinned to K=−1/2; `R[ω]` matches the metric Levi-Civita Riemann. The full assembly `F=dA+A∧A` has a Lorentz block that **IS** the genuine 4d Riemann tensor of `g=e·e` — independent Levi-Civita cross-check agreeing on 6/6 components exact over Q, torsion = 0 (the guards check MECHANICS, not physics). The M=0 vacuum is **flat with Λ=0 MEASURED** (not the v17.0 dead R×H³). But the decisive Einstein test FAILS on two independent axes: `G[g]` is NOT Einstein-form `κT+Λg` for any single global `(κ,Λ)` vs an AST-guarded, order-matched, independently-frozen `T[M]` — a **global-Λ inconsistency** (per-point Λ varies; the 180-equation solve is inconsistent for both T candidates; the both-(κ,Λ)-free solve returns EmptySet) AND a **tensor-support mismatch** (16 vs 6). The t⁴ order-match is satisfied ⟹ the failure is STRUCTURAL, not a near-miss; n=4 gives S≠0, Weyl≠0; 18 signature-(1,3) family points, 0 dropped. A curved, matter-sourced, position-dependent Lorentzian slice that is NOT Einstein-structured **without a posited action**.

**(78, Phase C — Circularity Audit, the FINAL phase) `fp-imported-action`.** The decisive non-circularity question — is the MM ε-contraction (hence the Einstein term) FORCED by the intrinsic h_3(O) trace form `Tr(X∘Y)` / cubic norm `det_3`, or only posited? — was settled exact over Q. The decisive triple: the bare so(3,1)-invariant quadratic-in-curvature 4-form space is already **dim 2** (Euler + Pontryagin, triple-route confirmed); the trace-form-invariant subspace is dim **1** (η-tensorial → Pontryagin only) / **2** (admitting the metric volume form → +ε); ε is reachable **only** via the orientation-ambiguous metric volume form `√|det η| ε` (not singled out); and `det_3 ≡ 0` **identically** on the soldered Lorentz block [1,2,3,10] (it couples x₁ to α, outside the block) ⇒ the normalization is **free/imported**. A deterministic, non-hardwired `verdict()` ladder maps this to `fp-imported-action` (a hypothetical *forced* triple would map to STRONG WIN; the actual triple fails all three clauses, each independently load-bearing). A second independent argument: at the Phase-77-MEASURED Λ=0 vacuum, `εF∧F → εR∧R` is pure Gauss-Bonnet/Euler — topological, no EOM, no GR. GST/Singh/Castro are the imported-action contrast class (each imports its action; the h_3(O) exceptional-structure escape hatch is CLOSED — `det_3` vanishes on the block, a symmetric `Tr` cannot build the antisymmetric ε).

**Combined milestone verdict (Phase 77 dynamical NEGATIVE + Phase 78 tensor/action NEGATIVE):** the h_3(O) Lie-sector Cartan/MM connection yields a **curved, matter-sourced, position-dependent Lorentzian slice carrying a forced SO(3,1) coframe, but NOT Einstein gravity without a posited action** — the same honest-partial class as Singh / Castro / GST (`fp-imported-action`). Reported at true strength: not inflated to a win (the coframe IS forced, the curvature IS genuine and matter-sourced), not deflated (the action IS imported; the ε is NOT forced). Tested the RIGHT object (linear-in-Riemann `εR∧e∧e`, the corrected Phase-B object, NOT the tautological quadratic-in-F the retired A.5 mistested). INDEPENDENT of v17.0's Ph73 NONE (different tensor ⟹ does NOT bind). Every decisive verdict exact over Q (Berry sector over Q(i)); every phase verified independently HIGH; both decisive verdicts (77, 78) human-ratified and orchestrator-reproduced.

## Key Results (exact over Q; Berry sector over Q(i))

| Phase | Result | Equation / Value | Validity / Regime | Confidence |
| ----- | ------ | ---------------- | ----------------- | ---------- |
| 74 | det SSOT re-certified | 324/324 inner-derivation annihilation = dim f_4 = 52; octonion_algebra.py absent | all of v18.0 | HIGH |
| 74 | Soldering form is V_{1/2}-valued | `E_11∘δ=½δ`; `T_{E_11}OP²=V_{1/2}(16)`, Jacobian rank 11, kernel==span{11..26}, 16=17−1 | tangent at E_11 | HIGH |
| 74 | Calibration anchors + sign benchmark | 24/28/3; 78=52+26; 17; 61; 45=Spin(9,1); K=−1/2 | all of v18.0 | HIGH |
| 75 | **Coframe KILL gate: SURVIVES** | dim π_u(V_{1/2}(16)) = 4 (survivors {11,18,19,26}=C_u²) | 4d slice | HIGH (human-ratified) |
| 75 | Soldering-form metric Lorentzian | signature (1,3); B rank 4 surjective; image(B)==π_u(V_0); forward null cone (bare trace-form diag(2,2,2,2)=(4,0) = OP² FS Euclidean foil) | 4d slice | HIGH |
| 75 | SO(3,1) FORCED, not chosen | residual 21=so(3,1)[6]⊕so(6)[15]; Killing sig (3,3) kills det_2; so(6) a trivial-on-spacetime ideal (res/so(6)=so(3,1)) | structure group | HIGH |
| 76 | Berry curvature reinterpreted | `F_B=Im(QGT)`; M=0 vacuum `F_B=−2ω_K`; F_B = internal so(6)=SU(4) gauge curvature, NOT gravity | — (gate retired) | HIGH (driver 25/25 + 43/43 over Q(i)) |
| 76 (precheck) | Base-metric coincidence ≠ redundancy | `g=e·e`=(1,3) η baseline, DIFFERENT mechanism from the (4,0) cone-Hessian | — | HIGH |
| 77 | Flatness sub-gate: PROCEED | `R[ω(e)]≠0` for M≠0 (136/256 nonzero exact/Q, R_scalar≠0); M=0 baseline flat | M≠0 slice | HIGH |
| 77 | Invertible torsion-free Cartan frame | `det(e)=½≠0` sig (1,3); closed-form `ω(e)` antisymmetric, K=−1/2; torsion=0 | 4d slice | HIGH |
| 77 | Lorentz block IS the 4d Riemann | `F=dA+A∧A` Lorentz block == independent Levi-Civita Riemann of g=e·e on 6/6 components exact over Q | 4d slice | HIGH |
| 77 | M=0 vacuum flat, Λ=0 MEASURED | Λ=0 (NOT R×H³) | M=0 | HIGH |
| 77 | **Einstein structure: NEGATIVE** | no single global (κ,Λ) gives `G[g]=κT+Λg` vs AST-guarded order-matched T[M]; two-axis (per-point Λ varies, 180-eq inconsistent, both-free solve EmptySet; support 16 vs 6); t⁴ order-match satisfied → structural; S≠0/Weyl≠0; 18 pts, 0 dropped | (M,x) family | HIGH (human-ratified; orchestrator-reproduced) |
| 78 | Bare invariant 4-form space dim=2 | so(3,1)-invariant quadratic-in-curvature 4-forms = Euler + Pontryagin (triple-route) | so(3,1) curvature | HIGH |
| 78 | Decisive triple | dim(trace-form-invariant subspace) = 1 (Pontryagin) / 2 (+ε via volume form); ε only via orientation-ambiguous `√|det η|ε`; `det_3≡0` on the Lorentz block [1,2,3,10] ⇒ normalization free | so(3,1) curvature | HIGH |
| 78 | **Forced-vs-posited: `fp-imported-action`** | deterministic non-hardwired `verdict()`; STRONG-WIN fails all 3 clauses; Λ=0 ⇒ εF∧F → εR∧R Gauss-Bonnet topological (2nd argument) | milestone headline | HIGH (human-ratified) |

## Methods Employed

- **Phase 74:** Exact-SymPy h_3(O) cubic-norm engine over Q (det SSOT `code/ring_lemma_verification.py` det_3); Cayley-Hamilton + 324/324 inner-derivation certification; AST/source guard for `octonion_algebra.py` absence; Zariski-tangent / Jacobian-rank computation of `T_{E_11}OP²`; Peirce-under-E_11 via `bulk_geometry_verification.py:peirce_indices_under_E11` / `embedding_under_E_verification.py`; `orbit_dimension_gate.py` calibration anchors. Deliverable `code/cartan_phase0_tangent.py`.
- **Phase 75:** Exact image-dimension over Q of `π_u(V_{1/2}(16))` under the `C_u`/Phase-46 bottleneck (`sympy.Matrix.rank`, never numpy); exact Gram-eigenvalue signature of the Peirce bilinear B into V_0≅R^{3,1}; forced-vs-arbitrary residual-structure-group decomposition over Q (so(3,1) ⊕ so(6) ideal split, verified from a from-scratch octonion algebra in verification). Deliverable `code/cartan_phaseA_coframe.py`.
- **Phase 76:** Gauge-invariant projector-form QGT `Q=Tr(P∂P∂P)` over Q(i), Re/Im split; well-definedness "born-from-breaking" checkpoint (OP²=F_4/Spin(9) carries no invariant 2-form); Wilczek-Zee non-abelian Berry covariance under frame rotation; the corrected-object analysis distinguishing quadratic-in-F (Maxwell stress / Pontryagin) from linear-in-R[ω] (Einstein-Hilbert). Deliverables `code/cartan_phaseA5_berry.py`, `code/cartan_phaseB_metric_precheck.py`.
- **Phase 77:** Flatness sub-gate (`R[ω(e)]≠0` for M≠0, exact over Q); invertible-coframe construction (`π_u(dE)`, Lagrange-congruence fallback at the watchdog cliff, frame-invariant); closed-form torsion-free Levi-Civita `ω(e)` (Wise `A=ω+(1/ℓ)e`, `F=R[ω]−(Λ/3)e∧e+d_ω e`); `F=dA+A∧A` symbolic assembly with Lorentz/torsion split; independent Levi-Civita Riemann cross-check ≥5 (achieved 6/6) components; AST-guarded order-matched independent `T[M]` (no Ric/R/G import) with single-global-(κ,Λ) over-determined solve (180-eq + both-free EmptySet); n=4 Ricci decomposition (S, Weyl); `eig_signature_count` (1,3)-splice gating. Deliverables `code/cartan_phaseB_curvature.py`, `code/cartan_phaseB_einstein.py`.
- **Phase 78:** Trace-form-invariant quadratic-in-curvature 4-form contraction-space dimension count (bare so(3,1) basis Euler+Pontryagin, triple-route); ε-reachability test via the orientation-ambiguous metric volume form; `det_3≡0`-on-the-Lorentz-block identity (two code paths: `X_from_symbols` vs `polarize_d`); deterministic non-hardwired `verdict()` ladder + injected-violation input-ban guard; Λ=0 Gauss-Bonnet corollary. Deliverable `code/cartan_phaseC_contraction.py`.

## Convention Evolution

| Phase | Convention | Description | Status |
| ----- | ---------- | ----------- | ------ |
| 74 (lock, 0d10eeea inherited) | det SSOT | det_3 = `code/ring_lemma_verification.py` (cross-term 2Re((x₂x₁)x₃)); `octonion_algebra.py` BANNED on the decisive path | Active |
| 74 (notation pass, 3e3f3d20) | metric_signature glyph | string set to "mostly-minus (+,−,−,−)" timelike-positive (STRING-ONLY; engine `eta=diag(+1,−1,−1,−1)` unchanged) | Active |
| 74 | Cartan/MM customs | 7 locked customs (soldering form `e=π_u(dE)`; connection `A=ω⊕e`; curvature `F=dA+A∧A`; `ω`=Lorentz Spin(3,1) part; QGT Re/Im split; etc.) | Active |
| 75 | Spacetime metric | the **soldered (1,3) Lorentzian form** (Peirce bilinear B), NOT the Euclidean OP² Fubini-Study metric | Active (binding downstream) |
| 75 | Structure group | SO(3,1) = the FORCED Lorentz structure group for `ω` (residual ideal so(6) acts trivially on spacetime) | Active |
| 76 (CONVENTIONS §11) | Berry curvature object | `F_B=Im(QGT)` = the internal `so(6)=SU(4)` gauge curvature (deferred SM bonus), NOT gravity; gravity = `R[ω]` | Active (reinterpreted) |
| 77 | Vacuum | M=0 flat, Λ=0 MEASURED (not R×H³); inherit CONVENTIONS §6, do NOT reintroduce Λ<0 | Active |
| 77/78 | Arithmetic | EXACT over Q on every decisive verdict (`fp-float-decisive` rejected); ranks via sympy, never numpy | Active |

**Non-blocking notation follow-up (carried, not gating — routed to notation-coordinator):** (1) the state.json `convention_lock.metric_signature` glyph vs label reconcile; (2) CONVENTIONS §1/§3 still show the stale Peirce ledger `{17,18,19,26}` — the live indices are the engine block `[1,2,3,10]` (V_0 sub-slice) and `[11,18,19,26]` (V_{1/2} survivors); (3) record K=−1/2 alongside round −1 in the `riemann_ricci_sign` line; (4) compile the Phase-77 and Phase-78 `.tex` (pdflatex was unavailable in-environment). All operationally inert (every decisive quantity flows from the fixed engine eta and exact-over-Q ranks).

## Figures and Data Registry

| File | Phase | Description | Paper-ready? |
| ---- | ----- | ----------- | ------------ |
| (none) | — | v18.0 produced no figures/plots — it is an exact-symbolic computation milestone; results are exact rationals, dimensions, and signatures | n/a |

Deliverable code (the data, as reproducible exact-over-Q drivers):

| File | Phase | Description |
| ---- | ----- | ----------- |
| `code/cartan_phase0_tangent.py` | 74 | det SSOT re-pass + tangent identity + calibration anchors |
| `code/cartan_phaseA_coframe.py` | 75 | image dim + Gram signature + forced structure group |
| `code/cartan_phaseA5_berry.py` | 76 | `F_B=Im(QGT)` vacuum + matter (Q(i)) |
| `code/cartan_phaseB_metric_precheck.py` | 76 | `g=e·e`=(1,3) vs (4,0) cone-Hessian pre-check |
| `code/cartan_phaseB_curvature.py` | 77 | coframe + `ω(e)` + flatness gate + `F=dA+A∧A` + Levi-Civita cross-check |
| `code/cartan_phaseB_einstein.py` | 77 | M=0 vacuum Λ + matter Einstein test vs independent T[M] |
| `code/cartan_phaseC_contraction.py` | 78 | trace-form-invariant contraction-space dim + ε-reachability + `verdict()` |
| `derivations/{74,75,76,77,78}-*.tex` | 74–78 | per-phase derivations |

## Open Questions (deferred / future work)

1. **(SM-unification bonus, deferred)** The internal `so(6)=SU(4)` Berry/gauge curvature `F_B=Im(QGT)` (Phase 76) — the Pati-Salam block already housed in Paper 7 (Phase 48) — as a *gauge*-sector object, distinct from gravity. A later milestone could test whether it yields the SM gauge dynamics (NOT a v18.0 deliverable; derive→house discipline).
2. **(The imported action)** Whether a posited MM/EH action could be justified *non-circularly* from some structure outside the h_3(O) trace form — the honest-partial boundary. Phase 78 proved the trace form does NOT force it; whether anything else does is open (and would itself need a forced-vs-posited audit).
3. **(Write-up)** Paper write-up of the `fp-imported-action` result (`paper6-cartan-tetrad`), and its honest relation to v12/v13 (Einstein via *posited* SUSY closure — circular by this milestone's lights) and v17.0 (cone-Hessian NONE, the real-part/symmetric-sector route). Two independent intrinsic routes (symmetric v17.0, antisymmetric v18.0) both fall short of forced Einstein.
4. **(Non-blocking notation)** The four carried notation-coordinator items above (glyph, stale Peirce ledger, K=−1/2 in `riemann_ricci_sign`, uncompiled 77/78 `.tex`).
5. **(Interpretation)** What physical content a forced-coframe-but-imported-action route carries — and whether a higher Peirce structure, a different intrinsic contraction, or a non-minimal `T[M]` could change the C verdict without importing a dead route.

## Dependency Graph

    Phase 74 "Phase 0 — Engine, Tangent Identity & Calibration"
      provides: certified det_3 SSOT; V_{1/2}-valued soldering form (E_11∘δ=½δ, T_{E_11}OP²=16); calibration anchors; K=−1/2
    -> Phase 75 "Phase A — Coframe-Reduction KILL Gate"
      requires: 74 soldering form + det SSOT
      provides: VERDICT SURVIVES (dim π_u(V_{1/2})=4, sig (1,3), SO(3,1) FORCED); soldered (1,3) spacetime metric; SO(3,1) structure group
    -> Phase 76 "Phase A.5 — Berry Curvature"  [RETIRED as a gravity gate]
      requires: 74 engine
      provides: F_B=Im(QGT) = internal so(6)=SU(4) gauge curvature (deferred SM bonus, NOT gravity); g=e·e=(1,3) pre-check
    -> Phase 77 "Phase B — Full Cartan Curvature = 4d Gravity"
      requires: 75 SURVIVES (76 retired as a gate); the soldered coframe
      provides: VERDICT NEGATIVE / fp-imported-action partial; flatness PROCEED (R[ω]≠0); invertible torsion-free frame; F=dA+A∧A Lorentz block == Levi-Civita Riemann (6/6); M=0 flat Λ=0; G[g]≠κT+Λg
    -> Phase 78 "Phase C — Circularity Audit (forced vs posited)"
      requires: 77 assembled connection + F∧F structure
      provides: VERDICT fp-imported-action; bare dim=2; decisive triple (det_3≡0 on block, ε via volume form only); Λ=0 Gauss-Bonnet corollary; verdict() ladder

**Critical path:** 74 → 75 → 77 → 78 (the "75 ∧ 76 conjunctive gate" was RETIRED 2026-06-02; Phase 75 alone greenlit Phase B; Phase 76's computation is preserved as an internal-gauge-sector observation). Phase 77 opened with its own flatness sub-gate (PROCEED).

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
| ----------- | ------ | ------------ | ---------- |
| DERV-01 (det SSOT re-pass) | Complete | Phase 74 | 324/324 = dim f_4 52; octonion_algebra.py absent |
| DERV-02 (tangent identity) | Complete | Phase 74 | `E_11∘δ=½δ`; `T_{E_11}OP²=V_{1/2}(16)` |
| VALD-01 (calibration anchors) | Complete | Phase 74 | 24/28/3; 78; 17; 61; 45; K=−1/2 |
| CALC-01 (image dim) | Complete — **SURVIVES** | Phase 75 | dim π_u(V_{1/2}(16)) = 4 |
| CALC-02 (Gram signature) | Complete — **SURVIVES** | Phase 75 | signature (1,3); B rank 4 |
| VALD-02 (forced-vs-arbitrary) | Complete — **SURVIVES** | Phase 75 | SO(3,1) FORCED; so(6) trivial-on-spacetime ideal |
| CALC-03 (Re(QGT) anchor) | Complete (gate retired) | Phase 76 | Re(QGT) sensible FS metric (SOFT sanity check) |
| VALD-03 (F_B well-defined) | Complete (gate retired) | Phase 76 | `Im(QGT)=F_B` born-from-breaking, nonzero |
| CALC-04 (M=0 vacuum) | Complete (gate retired) | Phase 76 | M=0 pure-Λ/Kähler `F_B=−2ω_K` |
| VALD-04 (same-wall) | Executed; SOFT-KILL **OVERTURNED** | Phase 76 | F_B = internal so(6)=SU(4) gauge curvature, NOT gravity |
| DERV-03 (invertible coframe) | Complete | Phase 77 | `det(e)=½≠0` sig (1,3) |
| DERV-04 (ω extraction) | Complete | Phase 77 | closed-form torsion-free `ω(e)`, K=−1/2 |
| CALC-05 (F=dA+A∧A = Riemann) | Complete | Phase 77 | Lorentz block == Levi-Civita Riemann on 6/6 components |
| VALD-05 (Einstein test) | Complete — **NEGATIVE** | Phase 77 | no global (κ,Λ) for G[g]=κT+Λg; two-axis; t⁴ matched (structural) |
| VALD-06 (forced-vs-posited) | Complete — **`fp-imported-action`** | Phase 78 | ε NOT forced; det_3≡0 on block; STRONG-WIN fails all 3 clauses |

**Milestone verdict:** all 15 requirements complete; all 4 contract claims resolved. The route SURVIVED the Phase-75 coframe KILL gate and the Phase-77 flatness sub-gate, then returned a two-axis NEGATIVE (Phase 77 dynamical `G[g]≠κT+Λg` + Phase 78 ε-not-forced) ⟹ **`fp-imported-action`**: a curved, matter-sourced, forced-SO(3,1)-coframe Lorentzian slice that is NOT Einstein gravity without a posited action. A decisive honest partial on the strongest claim, exact over Q, with no thermodynamic/ensemble argument and (Phase 78 audit) no GST/SUSY/−R/2/Weinberg import. NEGATIVE-RESULT-IS-SUCCESS.
