# Phase 76: Phase A.5 — Berry-Curvature Same-Wall Gate (SOFT KILL) — Research

**Researched:** 2026-06-02
**Domain:** Mathematical physics — the imaginary part of the quantum geometric tensor (canonical/tautological Berry curvature `F_B = Im Tr(P ∂P ∂P)`) of the rank-1 primitive-idempotent family `E(x)` on `OP² = F_4/Spin(9) = h_3(O)` idempotents; exact symbolic computation over `Q(i)`; the Einstein-vs-EM "same-wall" stress-content test against an independently-frozen `V_{1/2}` stress-energy `T[M]`; non-abelian (Wilczek–Zee) vs abelian gauge structure of the eigenbundle.
**Confidence:** HIGH on the QGT/Berry recipe (CP¹ and CP²-over-`C_u` anchored exact over `Q(i)` during this research), the warm-engine reuse, the VALD-03 well-definedness group theory (OP² isotropy-irreducible ⟹ Berry born-from-breaking — confirmed), the gauge-structure resolution (the primitive idempotent is **rank-1 ⟹ abelian** `F_B`; the Wilczek–Zee non-abelian caveat lives in the *frame* bundle, Phase B), and the novelty (no prior computation found). MEDIUM only on the **outcome of VALD-04** (Einstein-shaped vs EM-shaped), which is the genuinely-open SOFT-KILL clause and is designed to be MEASURED, not assumed. This is a SOFT-KILL gate, not a write-up phase.

## User Constraints

There is **no CONTEXT.md / init.json** for Phase 76 (confirmed — the directory is empty). All constraints are inherited from the authoritative milestone spec (`paper6-cartan-tetrad-prompt.md`), the binding conventions (`.gpd/CONVENTIONS.md` §6/§7/§11), the project contract intake (claim `claim-berry-same-wall`), and the partner gate (Phase 75, COMPLETE = SURVIVES). Key binding constraints affecting research scope:

- **The object is the IMAGINARY part of the QGT.** `F_B = Im(QGT)`, the *canonical* (Grassmann/tautological) Berry curvature of the rank-1 idempotent family — it needs NO metric-compatibility equation and NO assembly of `A = ω ⊕ e` (that is Phase B/77). This is what makes A.5 the cheap early gate. (CONVENTIONS §11; spec lines 164–199.)
- **This is a SOFT KILL, not a hard KILL.** A clean EM-shaped same-wall mismatch ⟹ "Lie sector inherits the symmetric-sector mismatch", recommend STOP before Phase B — reported FLAT (negative-result-is-success). Do NOT relabel an EM-shaped result "approximately Einstein". (spec lines 196–199, 248–255.)
- **CONJUNCTIVE GATE.** BOTH Phase 75 (✓ SURVIVES) and Phase 76 must SURVIVE to greenlight Phase B/77.
- **The Re(QGT) = cone-Hessian anchor is a SOFT sanity check ONLY** (FS-pullback ≠ cone-Hessian restriction). A discrepancy is INFORMATIVE (diagnose), NEVER a KILL on this anchor alone. This guards `fp-reuse-cone-hessian`. (CALC-03; §11.)
- **Λ = 0; M=0 vacuum is flat / pure-Λ; do NOT reintroduce Λ<0 / R×H³** (the FALSIFIED v17.0 cone-Hessian source-field geometry). (CONVENTIONS §6.)
- **EXACT over `Q(i)`** on every decisive verdict; the `i` carried SYMBOLICALLY, never as a float. `sympy` ranks/eigenvalues, never numpy. `octonion_algebra.py` BANNED. (CONVENTIONS §7; `fp-float-decisive`, `fp-octonion-algebra`.)
- **Decisive verdicts on gauge-INVARIANT scalars**, tested under a frame rotation (non-abelian-gauge guard / `fp-relabel` guard).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `paper6-cartan-tetrad-prompt.md` (Phase A.5 §, ≈164–199; QGT/Berry def ≈40–115; Pass/Fail; Forbidden proxies ≈257–268) | Authoritative milestone spec (BINDING) | Defines the canonical `F_B`, the (a)/(b)/(c) sub-tests, the SOFT-KILL condition, the reporting discipline, the forbidden proxies | Read; obey verbatim — `F_B = Im(QGT)` canonical, M=0 classification, the same-wall Einstein-vs-EM test, `fp-relabel`/`fp-reuse-cone-hessian`/non-abelian-gauge/`fp-float`/`fp-octonion` | Plan, execution, verification (every decisive verdict) |
| `ref-provost-vallee` — Provost & Vallée, CMP 76 (1980) 289 | Benchmark / method (BINDING) | The QGT split: **real = Fubini–Study metric, imaginary = Berry curvature**; the foundational identity that "the dead route was Re, this route is Im" | Cite; the Re/Im split is the load-bearing convention; confirm `Re(QGT)` = FS pullback (CALC-03) | Plan, execution (CALC-03, VALD-03) |
| `ref-wilczek-zee` — Wilczek & Zee 1984 + npj QI arXiv:1910.13991 + arXiv:2312.01086 (non-abelian QGT) | Benchmark / method (BINDING) | Non-abelian Berry curvature is gauge-COVARIANT `F→UFU⁻¹`; decisive verdicts must be gauge-INVARIANT (traces, Wilson **loops**, not lines) | Cite; apply the gauge-invariance protocol Q7; **resolve rank-1 (abelian) vs rank-r (non-abelian)** | Plan, execution (VALD-04 gauge guard), verification |
| `ref-wise` — Wise gr-qc/0611154; `ref-mm-1977` — MacDowell & Mansouri PRL 38 (1977) 739 | Benchmark / method | The MM ε-contraction `F∧F` → EH+Λ; the `F_B∧F_B` Lorentz-block contraction (the *diagnostic*, A.5(b)); the EM-vs-Einstein distinction lives here | Cite for the contraction *structure* only; the *diagnostic* ε-contraction (whether `F_B∧F_B` can match `T[M]`) is A.5(b) — NOT the forced-vs-posited audit (Phase C) | Plan, execution (VALD-04) |
| **`code/cartan_phaseA_coframe.py`** (Phase 75, DONE/verified SURVIVES) | Prior artifact (THE structural template) | The exact-over-`Q` driver pattern; the soldering bilinear `B`; **the C_u survivors `{11,18,19,26}=C_u²`** (the 4 coframe directions A.5 parametrizes); the foil-vs-verdict design discipline; the source guard; `_report` harness | Mirror the driver structure and rigor; reuse `{11,18,19,26}`, `to_mink`, `G_DET2_RAW`, `_signature`, `_source_guard` | Plan (code skeleton), execution |
| `.gpd/phases/75-…/75-01-SUMMARY.md` (verdict ledger) | Prior artifact (the SURVIVES result) | The soldered (1,3) Lorentz metric + FORCED SO(3,1) is the binding downstream convention; `image(B)==π_u(V_0)`; the trace form is Euclidean (4,0) FOIL | Use as the Lorentzian target for the `F_B∧F_B` Lorentz-block contraction; the SO(3,1) is the frame group for the gauge test | Plan, execution, verification |
| **`code/bulk_geometry_verification.py`** — `cone_hessian_at_center`, `offcenter_slice_metric`, `spacetime_curvature_of_g`, `_matterless_reference_hessian`, `ricci_decomposition_n4`, `h3_constant_curvature` | Engine (warm; the Re-anchor + T[M] pipeline) | CALC-03 Re-anchor (`cone_hessian_at_center`→diag(9,9,18,18); `h3_constant_curvature`→round K=−1; Phase-71 cone-Hessian K=−1/2); the **independently-frozen T[M]** (the v17.0 matter-on-flat + cross-term off-switch pipeline); the trace/traceless/Weyl decomposition for EM-vs-Einstein | Reuse `cone_hessian_at_center` for CALC-03; reuse `spacetime_curvature_of_g`(+`norm_potential=inv_det_X_block` off-switch) + `ricci_decomposition_n4` to build/diagnose `T[M]` for VALD-04 | Plan, execution (CALC-03, VALD-04) |
| `code/embedding_under_E_verification.py` — `E`, `proj_u_exact`, `slice_to_complex`, `cu_to_complex`, `h3o_from_coords`, `jordan` | Engine (the C_u/QGT bridge) | **`slice_to_complex` maps an `h_3(C_u)` element → a 3×3 complex SymPy matrix with `e_7 → i`** — this is THE bridge that makes `Im` the literal SymPy imaginary part and carries the `i` symbolically over `Q(i)` | Reuse `slice_to_complex` to land in the complex-matrix QGT; `proj_u_exact`/`E` for the C_u reduction; `jordan` for any Jordan-product step | Plan, execution (CALC-03/VALD-03/CALC-04/VALD-04) |
| `code/ring_lemma_verification.py` — `det_3` (SSOT), `Tr`, `jordan` | det SSOT (BINDING) | The cubic norm + trace form for `T[M]`, the Re-anchor, and any det_2; correct octonion association | Import; det/trace/Jordan from the SSOT (never `octonion_algebra.py`) | Plan, execution |
| `code/cartan_phase0_tangent.py` + `74-01-SUMMARY.md` | Prior artifact (warm harness) | The `_report`/`_run_engine` harness, `V_HALF_IDX=range(11,27)`, the source guard, the certified tangent identity `T_{E_11}OP²=V_{1/2}` | Copy the harness skeleton; build on Phase 74 (do NOT redo the tangent identity) | Plan (code skeleton), execution |
| `derivations/52-kkt-spacetime.tex`, `52-observer-uniqueness.tex` | Benchmark / template | `h_2(C_u)≅R^{3,1}`, the `π_u` O→C bottleneck, the Lorentz boosts (sig (3,3)) — the soldered target for the `F_B∧F_B` Lorentz-block contraction | Cite; use the (1,3) det_2 target | Plan, execution (VALD-04) |
| `.gpd/research/{METHODS,PITFALLS,SUMMARY,COMPUTATIONAL}.md` (v18.0 project research) | Prior artifact (project-level) | M1 (projector `F_B`), Pitfalls 3/4/5/6/10 (sector / same-wall / gauge / float / vacuum), the EM-shaped discriminants, the engine inventory | Build on; do NOT re-derive | Plan (constraints), verification |

**Missing or weak anchors:**
- `code/peirce_coupling.py` (cited in the spec "Build on") **does NOT exist** (confirmed; also flagged Phase 74/75). The Peirce-under-E_11 machinery is `bulk_geometry_verification.py::peirce_indices_under_E11` + `embedding_under_E_verification.py`. The plan must point at those.
- **The cleanest matrix realization of the *matter-on* family `E(x;M)`** (how `M ∈ V_{1/2}` perturbs the rank-1 idempotent and whether its C_u image stays a clean rank-1 complex projector) is the one MEDIUM-confidence modeling step (see Q6 and Open Risks). The *vacuum* family (M=0) is fully de-risked this research (CP²-over-`C_u`, exact over `Q(i)`); the *matter* family needs an explicit construction in the plan.
- `octonion_algebra.py` is **BANNED** (buggy associator); present on disk but MUST NOT be imported on any decisive path (inherit the Phase-0/75 source guard).

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Metric signature (slice) | mostly-minus `(+,−,−,−)` timelike-positive; `det_2 = x0²−x1²−x2²−x3²`, `G=diag(+1,−1,−1,−1)`, sig (1,3) | `(−,+,+,+)` | CONVENTIONS §1; 52-kkt |
| Bulk OP² metric | Riemannian / positive-definite (the Fubini–Study metric of OP²); bare trace form on `π_u(V_{1/2})` = `diag(2,2,2,2)` = (4,0) | — | Phase 75; Baez |
| Units | natural (ħ=c=1), dimensionless | — | §2 |
| QGT (projector form) | `Q_{μν} = Tr(P ∂_μ P ∂_ν P)`, gauge-invariant for rank-1 `P` | state form `⟨∂ψ|(1−P)|∂ψ⟩` (carries a gauge phase — REJECTED symbolically) | Provost–Vallée; Graf–Piéchon arXiv:2102.09899; METHODS M1 |
| Quantum metric / Berry split | `g_{μν} = Re Q_{μν} = ½Tr(∂_μP ∂_νP)` (FS); `F_{B,μν} = i·Tr(P[∂_μP, ∂_νP]) = −2 Im Q_{μν}` | sign/factor-2 variants — PIN against the CP¹ anchor (below) | Provost–Vallée; this research (CP¹ check) |
| Complex structure / `Q(i)` | `u = e_7`, `C_u = span{1, e_7}`; `slice_to_complex` maps `e_7 → i` (SymPy `I`); the `i` is SYMBOLIC over `Q(i)` | float `i` (BANNED, `fp-float-decisive`) | §3/§11; `embedding_under_E_verification.cu_to_complex` |
| Primitive idempotent / Peirce | `E_11 = diag(1,0,0)`; `V_1={0}`, `V_0={1..10}`, `V_{1/2}={11..26}`; **C_u survivors `{11,18,19,26}=C_u²`** | E_22/E_33 (F_4-conjugate) | §3; Phase 74/75 |
| Det SSOT | `ring_lemma_verification.py det_3`, cross-term `2Re(x2* x0* x1)`, CH + 324/324 | `octonion_algebra.py` (BANNED) | §0/§7 |
| Sign calibration | round H³ `K=−1`; cone-Hessian slice `K=−1/2` (Phase-71 benchmark); factor-2 locked | force −1 (WRONG) | §1/§4; `h3_constant_curvature` |
| Vacuum | M=0 flat / pure-Λ; **Λ=0**; do NOT reintroduce Λ<0 / R×H³ | Λ<0 (FALSIFIED) | §6 |

**CRITICAL:** All results below use these conventions. The Berry curvature is read as the literal `Im` of the complex (`e_7→i`) QGT, exact over `Q(i)`. The Re-anchor (CALC-03) is compared to the cone-Hessian as a SOFT diagnostic, NEVER load-bearing for the Im verdict (`fp-reuse-cone-hessian`). The decisive Einstein-vs-EM verdict (VALD-04) rests on gauge-invariant scalars and on an M-power/tensor-structure/support match to an **independently-frozen** `T[M]` — "some 2-form appears" is forbidden (`fp-relabel`).

Convention loading: see agent-infrastructure.md Convention Loading Protocol. Phases 74/75 already reproduced the v18.0 lock byte-for-byte.

## Mathematical Framework

### The recipe in one line (RESOLVED, anchored exact over Q(i) this research)

```
P(x) = E(x)  =  the rank-1 primitive idempotent at x, projected to C_u  (a 3×3 C_u-Hermitian matrix)
M_C(x) = slice_to_complex(P(x))      # 3×3 SymPy complex matrix, e_7 → i  (carries the i SYMBOLICALLY over Q(i))
Q_{μν}(x) = Tr( M_C  ∂_μ M_C  ∂_ν M_C )                 # the QGT, exact over Q(i)
g_{μν}    = Re Q_{μν}                                    # Fubini–Study metric  (CALC-03 Re-anchor)
F_{B,μν}  = i·Tr( M_C [∂_μ M_C, ∂_ν M_C] ) = −2 Im Q_{μν}   # Berry curvature 2-form  (VALD-03/CALC-04/VALD-04)
```

The four base directions `μ,ν` are the **4 reduced coframe directions** = the C_u² survivors `{11,18,19,26}` from Phase 75 (the `π_u`-image of `V_{1/2}`). `F_B` is a `4×4` antisymmetric matrix of rational functions of the slice coordinates.

### Q1 — The exact QGT recipe over h_3(O)/Q(i) (RESOLVED, HIGH)

**The non-associativity problem dissolves once you project to C_u.** `h_3(O)` is a non-associative Jordan algebra and `OP²` has no genuine octonionic Hilbert space — there is no associative `P ∂P ∂P` on the full octonionic matrices. BUT the **C_u reduction `π_u` (Phase 46/75) lands every entry in `C_u = span{1,e_7} ≅ C`, which IS associative** (it is just the complex numbers). After `slice_to_complex` (`e_7 → i`), `P(x)` is an ordinary `3×3` complex Hermitian rank-1 projector and `Tr(P ∂P ∂P)` is the **standard associative QGT** of complex quantum mechanics. The `i` of `Q(i)` is carried symbolically by SymPy's `I`. This is the single key insight that makes A.5 computable exactly.

Concretely:
- **(a) `P` = the rank-1 primitive idempotent `E(x)`.** Primitive idempotents of a formally-real Jordan algebra ARE rank-1 projectors (METHODS M1; the Veronese/rank-1 elements of `h_3(O)`). The vacuum base point is `E_11 = diag(1,0,0)` (`Tr=1`, rank 1).
- **(b) The product = ordinary complex matrix multiplication** on `slice_to_complex(P)`. NOT the Jordan product `∘`, NOT the Freudenthal triple product. Justification: the QGT is `Tr(P ∂P ∂P)` with `P` a *projector* and the *associative* operator product; the Jordan product would give a different (and wrong) object. The C_u associative realization is exactly the "associative realization" option in Q1(b), and it is forced (not chosen) because `C_u ≅ C` is the unique associative completion the `u=e_7` complex structure provides.
- **(c) The "trace" = ordinary matrix trace** of the `3×3` complex matrix `slice_to_complex(P)`. (This is consistent with the `h_3(O)` trace form `Tr` restricted to the C_u block; `ring_lemma_verification.Tr` agrees on C_u data.)
- **(d) The Re/Im split via `u=e_7`** is the literal SymPy `re`/`im` after `e_7 → i`. `Re(QGT)` = symmetric (FS metric); `Im(QGT)` = `−½ F_B` (antisymmetric Berry curvature). The "e_7-component / C_u-antisymmetric part" extraction the spec mentions IS this `Im`.

**Cross-check against the standard case (DONE this research, exact over Q(i)):** the CP¹ projector `P(θ,φ) = ½[[1+cosθ, sinθ e^{−iφ}],[sinθ e^{iφ}, 1−cosθ]]` gives, exactly:
`Q_θθ = 1/4`, `Q_φφ = sin²θ/4` (the FS metric), `Q_θφ = i sinθ/4`, and `F_B = i Tr(P[∂_θP,∂_φP]) = −sinθ/2` (the standard CP¹ monopole Berry curvature, `∫F_B = −2π`), `g_θθ = Re Q_θθ = 1/4`. The convention (sign, factor) is thereby PINNED. **This anchors the entire recipe.**

### Q2 — The E(x) family parametrization (RESOLVED, HIGH for vacuum; MEDIUM for matter-on)

A 2-form needs ≥2 parameters; we need a 4-real-parameter family over the 4d slice. The clean, computable choice (de-risked this research):

**Vacuum family (M=0) — the rank-1 Veronese/CP² chart over C_u:** a rank-1 idempotent is `P = v v†/(v†v)` with `v` a unit octonionic 3-vector (Veronese). Restricting `v` to **C_u entries** keeps `P` in `h_3(C_u)`, so `slice_to_complex(P)` is a `3×3` complex rank-1 projector. The natural 2-complex-parameter (= 4-real) chart anchored at `E_11`:
```
v(z1,z2) = [1, z1, z2] / sqrt(1+|z1|²+|z2|²),    z1,z2 ∈ C_u ≅ C,   z1=a+i b, z2=c+i d
P = v v†                          # rank-1 idempotent, Tr P = 1, exact over Q(i)
```
**Verified this research (exact over Q(i)):** `P` is a clean rank-1 idempotent (`P²−P=0`); at the base point `a=b=c=d=0` the Berry curvature is **generically NONZERO** with `F_B[a,b] = −2`, `F_B[c,d] = −2`, and `F_B[a,c]=F_B[a,d]=F_B[b,c]=F_B[b,d]=0` (the CP² Kähler form, block-diagonal); the quantum metric is `g = diag(1,1,1,1)` (the FS metric). **This is the most informative single result for the verdict** (see Order-of-Magnitude Expectations).

Equivalently and group-theoretically: `E(x) = g(x)·E_11·g(x)⁻¹` with `g(x)` the transvections moving along the 4 reduced coframe directions `π_u(V_{1/2})={11,18,19,26}` — this is the same orbit, just realized as the CP²-over-`C_u` chart above. Use the chart (it is rational and exact); the conjugation form is the conceptual cross-check.

**Matter-on family (M≠0):** turn on `M ∈ V_{1/2}` as a background perturbation `X_bg = I/3 + M` and let `E(x;M)` be the rank-1 idempotent of the *perturbed* configuration (the off-center basepoint move, parallel to `_offcenter_subs`/`rho_J` in `bulk_geometry_verification.py`). Two routes, in increasing rigor:
1. **Small-M series** to the needed order (the v17.0 lesson: matter entered `g` at `O(‖M‖²)`, curvature at `O(‖M‖⁴)` — power-counting is decisive). Keep `M` symbolic, expand `E(x;M)` and `F_B(x;M)` to leading nonzero order in `M`. This is the recommended decisive path (exact rational coefficients per order).
2. **Rational one-parameter subgroups** (specific rational `M`) as a cross-check / triage.

The leading-order-in-M coefficient of `F_B`'s matter part is the object VALD-04 compares to `T[M]`. (The exact rank-1-idempotent-of-a-perturbed-config construction over C_u is the MEDIUM modeling step — see Open Risks.)

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `Q_{μν} = Tr(P ∂_μP ∂_νP)` | Projector-form QGT (gauge-invariant) | Provost–Vallée; Graf–Piéchon | The master object; CALC-03/VALD-03 |
| `F_{B,μν} = i Tr(P[∂_μP,∂_νP]) = −2 Im Q_{μν}` | Berry curvature 2-form | Provost–Vallée; this research (CP¹: `−sinθ/2`) | VALD-03/CALC-04/VALD-04 |
| `g_{μν} = Re Q_{μν} = ½Tr(∂_μP ∂_νP)` | Fubini–Study metric | Provost–Vallée | CALC-03 Re-anchor |
| `P = vv†/(v†v)`, `v=[1,z1,z2]`, `z_k∈C_u` | Rank-1 Veronese/CP² chart over C_u | this research (verified rank-1 over Q(i)) | CALC-04 vacuum family |
| `M_C = slice_to_complex(P)` (`e_7→i`) | The C_u→C bridge (i symbolic over Q(i)) | `embedding_under_E_verification` | Every clause |
| `R_ijkl = Scal + E + Weyl`, `S_ab = Ric_ab − (R/4)g_ab` (traceless Ricci) | n=4 Ricci decomposition | `ricci_decomposition_n4` | VALD-04 EM-vs-Einstein |
| `T^μ_μ = 0`, `T ~ F²` (traceless, conformal) | EM stress-energy discriminant | Wikipedia EM stress tensor; arXiv:1101.2505 | VALD-04 EM-shaped test |
| `h(x;M) := H_source(x;bg+M) − H_source(x;bg-only)` | Matter-on-flat `T[M]` (B1) | `spacetime_curvature_of_g`; v17.0 Ph72/73 | VALD-04 independently-frozen `T[M]` |
| `cone-Hessian|_{V_0,center} = diag(9,9,18,18)`, `K=−1/2`; round H³ `K=−1` | The Re-anchor + sign calibration | `cone_hessian_at_center`, `h3_constant_curvature` | CALC-03 |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| C_u projection → complex matrix (`e_7→i`) | Turns the non-associative octonionic projector into an associative complex one; carries `i` symbolically | All clauses | `slice_to_complex`; §11 |
| Symbolic differentiation + Re/Im split over Q(i) | `∂_μ M_C`, `Re/Im Q` exact | All clauses | SymPy `diff`, `re`, `im` |
| Rank-1 idempotent (Veronese) construction | The state family `E(x)` | CALC-04 vacuum | METHODS M1; this research |
| Small-M series expansion (exact rational coefficients) | Leading matter order of `F_B`; power-counting vs `T[M]` | VALD-04 | v17.0 Ph73 |
| n=4 trace/traceless-Ricci/Weyl decomposition | EM-shaped (traceless) vs Einstein-shaped (S≠0) | VALD-04 | `ricci_decomposition_n4` |
| Gauge-invariant scalars + frame-rotation test | Verdict invariance (abelian rank-1, but test anyway) | VALD-04 gauge guard | Wilczek–Zee; arXiv:1910.13991 |
| Exact eigenvalue/rank signatures over Q (or Q(i)) | well-definedness, nonzero-ness | VALD-03 | `sympy.Matrix` |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| ------------- | --------------- | ------------------ | -------------- | ----------------------- |
| Small-M series of `F_B`, `T[M]` | `‖M‖` (`rho_J` off-center-ness) | leading matter order (the decisive order; v17.0 used `O(‖M‖²)`/`O(‖M‖⁴)`) | exact rational per order (truncation controlled — compute the next order to confirm leading) | full rational `M` (exact, no truncation) as cross-check |
| Single base point for the vacuum 2-form | none (M=0 is exact) | the vacuum class is homogeneous (OP² symmetric) | exact | symbolic over the chart (preferred) |

**Note:** the M=0 vacuum and the round CP² Berry form are EXACT (no approximation). Only the matter-on comparison uses an M-series, and even that is exact per order. There is no float, no uncontrolled truncation.

## Standard Approaches

### Approach 1: C_u-complex projector QGT, ordered VALD-03 → CALC-03 → CALC-04 → VALD-04 (RECOMMENDED)

**What:** Build the rank-1 idempotent family over C_u, map to a complex matrix (`e_7→i`), compute the QGT exactly over `Q(i)`, split Re/Im. Lead with the **well-definedness checkpoint (VALD-03)**; then the soft Re-anchor (CALC-03); then classify the vacuum (CALC-04); then the decisive same-wall Einstein-vs-EM test (VALD-04).

**Why standard:** This is the projector-form QGT (Provost–Vallée; Graf–Piéchon) — manifestly gauge-invariant for rank-1, no phase fixing, the clean object for exact symbolic evaluation (METHODS M1, point 3). The C_u associative realization is the only way to define `P ∂P ∂P` exactly on `h_3(O)` data. It mirrors the validated Phase-75 driver pattern (warm engines, exact over Q, foil-vs-verdict discipline).

**Key steps (the explicit ordering):**
1. **Source guard + harness** (copy from `cartan_phaseA_coframe.py`): `octonion_algebra` absent on the decisive path; native exact primitives; no numpy; `_report` latch; reproduce the Peirce layout `V_{1/2}={11..26}` and the C_u survivors `{11,18,19,26}`.
2. **Convention pin (CP¹ anchor):** reproduce `F_B(CP¹) = −sinθ/2`, `g_θθ=1/4` exactly over `Q(i)` to lock the sign/factor before any h_3(O) verdict (defeats Pitfall 5 normalization slip).
3. **VALD-03 (FIRST):** establish `F_B` is well-defined and generically NONZERO on the 4d slice after C_u breaking. (i) Group theory: OP²=F_4/Spin(9) isotropy-irreducible ⟹ NO invariant 2-form ⟹ round Berry vanishes ⟹ a nonzero `F_B` is BORN FROM THE BREAKING. (ii) Compute `F_B` on the C_u chart and show it is generically nonzero (not identically 0). **KILL-worse-than-SOFT if `F_B ≡ 0`** (degenerate).
4. **CALC-03 (soft anchor):** compute `Re(QGT)` = FS metric on the chart; compare its *character* (Ricci-eigenvalue pattern / non-Einstein-ness / sign structure) to the cone-Hessian (`cone_hessian_at_center` diag(9,9,18,18); `h3_constant_curvature` K=−1). **A discrepancy is INFORMATIVE, NOT a KILL** (FS-pullback ≠ cone-Hessian restriction; `fp-reuse-cone-hessian`).
5. **CALC-04 (vacuum classification):** classify `F_B` at M=0 — zero/flat, pure-Λ (`F_B ~ e∧e`, the Kähler/cosmological form), or other. Decompose into trace/traceless/Weyl. Expected pure-Λ-shaped (the CP² Kähler form — see Expectations). Do NOT reintroduce Λ<0.
6. **VALD-04 (the decisive SOFT-KILL clause):** turn on `M ∈ V_{1/2}`; compute the matter part of `F_B` and the ε-contraction of `F_B∧F_B` onto the SO(3,1) Lorentz block; build an **independently-frozen `T[M]`** (the v17.0 cross-term pipeline, `spacetime_curvature_of_g`+off-switch, frozen WITHOUT reference to `F_B`); test M-power AND tensor-structure (traceless? `~F²`? — EM-shaped) AND support against `T[M]`, using gauge-invariant scalars tested under a frame rotation. **Einstein-shaped (matchable) → SURVIVES to B; EM-shaped / support-disjoint / no M-power match → SOFT KILL.**

**Known difficulties at each step:**
- Step 3 (VALD-03): the round CP²-over-C_u Berry form is the *Euclidean* Kähler form (the probe gave block-diagonal `F_B` with the Euclidean FS metric). Reconciling this Euclidean Kähler 2-form with the *soldered Lorentzian* (1,3) coframe of Phase 75 is the conceptual subtlety: `F_B` is intrinsically the OP² Berry form, but its verdict-bearing contraction is onto the soldered Lorentz block. State both (the intrinsic Kähler form AND the Lorentz-block contraction) — the Phase-75 foil-vs-verdict discipline applies again.
- Step 6 (VALD-04): the matter-on idempotent construction over C_u (Q6 / Open Risks) is the modeling step most likely to be contested; build it explicitly and cross-check (off-switch, `M→0` limit, multiple `M`).
- Step 6: the "independently frozen" requirement — `T[M]` and `κ` must be built BEFORE/WITHOUT `F_B` (else circular `fp-relabel`).

### Approach 2: Direct octonionic QGT via the trace form on V_{1/2} (FALLBACK / cross-check)

**What:** Compute the QGT directly from the `h_3(O)` trace form `Tr(δ∘δ')` on the soldering form `dE ∈ V_{1/2}`, extracting the C_u-antisymmetric (`e_7`) part as `Im`.

**When to switch:** As an independent cross-check of the C_u-complex result (does the `e_7`-antisymmetric part of the trace-form QGT match the `Im` of the complex QGT?), or if the `slice_to_complex` bridge's faithfulness is contested.

**Tradeoffs:** More directly tied to the octonionic structure but messier (non-associativity must be tracked; the foil/verdict split is less clean). Use only as confirmation, not the load-bearing path. **Risk:** the bare trace form is the Euclidean (4,0) OP² metric (Phase 75), so reading anything off it directly invites the same "Euclidean trap" Phase 75 navigated — route the verdict through the complex QGT, not the bare trace form.

### Anti-Patterns to Avoid

- **Reading "Einstein" off a nonzero `F_B`.** A nonzero antisymmetric 2-form is a *field strength* (EM-shaped lives on the source side), NOT an Einstein structure. Verdict requires the M-power/tensor/support match to a frozen `T[M]` (`fp-relabel`). *Example:* "F_B ≠ 0 and matter turns it on, therefore gravity" — that is the v17.0 same-wall trap on the 2-form.
- **Using the cone-Hessian as load-bearing for the Im verdict.** It is the real-part SOFT check ONLY (`fp-reuse-cone-hessian`). *Example:* importing the v17.0 Riemann tensor and calling its non-Einstein-ness the A.5 verdict — that re-binds to v17.0 NONE (sector confusion, Pitfall 3).
- **Deciding on a frame-dependent `F_B` component.** Even though rank-1 `F_B` is abelian (gauge-invariant), the *Lorentz-block contraction* and any *frame* statement must use gauge-invariant scalars tested under an SO(3,1) frame rotation. *Example:* reading "Einstein-shaped" off one off-diagonal `F_B` component.
- **Using the Jordan product `∘` in `P ∂P ∂P`.** The QGT uses the *associative* operator product (here, complex matrix multiply on C_u), not `∘`. Using `∘` gives a different, wrong object.
- **Float `i` / numpy.** `fp-float-decisive` — the `i` is symbolic over `Q(i)`; ranks/eigenvalues via SymPy.
- **Reintroducing Λ<0 / R×H³ as the expected vacuum.** That is the FALSIFIED dead symmetric-sector object (§6; Pitfall 10).

## Existing Results to Leverage

**MANDATORY.** Results to CITE/REUSE, never re-derive.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| QGT split: Re = Fubini–Study metric, Im = Berry curvature | `g=Re Q`, `F_B=−2 Im Q` | Provost–Vallée CMP 76 (1980) 289 | The load-bearing convention; the Re-anchor and the Im verdict |
| Projector form gauge-invariant for rank-1 | `Q=Tr(P ∂P ∂P)`, no phase fixing | Graf–Piéchon PRB 104 (2021), arXiv:2102.09899; Wikipedia "Quantum geometry" | Use the projector form symbolically (METHODS M1) |
| **OP²=F_4/Spin(9) isotropy-irreducible** (unique rank-1 exceptional symmetric space); isotropy = 16-dim spinor Δ9, the unique irreducible 16-dim Spin(9) rep | — | Baez 2002 §3.4; Berger; arXiv:math/9912112 (weak Spin(9)); this research (web survey) | **VALD-03 core:** irreducible isotropy ⟹ unique invariant symmetric form (FS metric) + NO invariant 2-form ⟹ round Berry = 0 ⟹ `F_B` born from the C_u breaking |
| CP¹ Berry curvature `F_B = −sinθ/2` (`∫=−2π`); FS metric `g_θθ=1/4` | exact | standard; verified this research over Q(i) | The convention-pin anchor (sign/factor) |
| CP² Fubini–Study Kähler form (round); FS metric | block-diagonal, maximally symmetric | standard; verified this research (`F_B[a,b]=F_B[c,d]=−2`, `g=I₄` at base) | The M=0 vacuum *character* (pure-Λ/Kähler expectation, CALC-04) |
| Phase 75 SURVIVES: `dim π_u(V_{1/2})=4`, survivors `{11,18,19,26}=C_u²`; soldered (1,3) Lorentz metric; SO(3,1) FORCED; trace form (4,0) is the FOIL | exact over Q | `75-01-SUMMARY.md` (human-ratified) | The 4 base directions; the soldered Lorentz target for the `F_B∧F_B` contraction; the SO(3,1) frame group; the foil-vs-verdict discipline |
| cone-Hessian|_{center} = diag(9,9,18,18), det 26244; round H³ K=−1; cone-Hessian slice K=−1/2 | exact | `cone_hessian_at_center`, `h3_constant_curvature`; Phase 71 | CALC-03 Re-anchor + sign calibration |
| v17.0 NONE: cone-Hessian curved but NOT Einstein (κT~10³<G, support-disjoint, S≠0/Weyl≠0); matter ~94% cross-term-sourced | exact | v17.0 Ph73; `.gpd/research/archive-v17` | The same-wall *failure pattern* VALD-04 tests for; binds only Re, NOT Im |
| EM stress tensor: traceless `T^μ_μ=0`, `T~F²`, conformal | — | Wikipedia "EM stress-energy tensor"; arXiv:1101.2505 | The EM-shaped discriminant (VALD-04) |
| Non-abelian Berry: gauge-COVARIANT `F→UFU⁻¹`; Wilson **loop** invariant, line not | — | Wilczek–Zee 1984; arXiv:1910.13991; arXiv:2312.01086 | The gauge-invariance protocol (Q7); resolves rank-1=abelian vs rank-r=non-abelian |
| det SSOT: `det_3` CH + 324/324 = dim f_4 = 52 | — | `ring_lemma_verification.py`; Phase 74 | The trace form + cubic norm for `T[M]` |

**Key insight (why re-derivation is wasteful/dangerous):** The QGT split, the projector formula, the OP² isotropy-irreducibility, the CP¹/CP² anchors, the 4 C_u² base directions, the soldered Lorentz target, the cone-Hessian benchmark, the v17.0 same-wall pattern, and the EM/non-abelian discriminants are ALL established (literature or in-repo, several verified this research). Phase A.5's ONLY new content is: (i) the QGT of THIS specific idempotent family (vacuum class de-risked this research; matter-on to compute), and (ii) the VALD-04 Einstein-vs-EM same-wall verdict (the genuinely-open SOFT-KILL clause). Re-deriving the octonion arithmetic or the QGT formula invites the buggy-associator / convention-slip / float failures the SSOT + CP¹-anchor guards exist to prevent.

### Useful Intermediate Results (verified during THIS research, exact over Q(i))

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| CP¹: `Q_θθ=1/4`, `Q_φφ=sin²θ/4`, `Q_θφ=i sinθ/4`, `F_B=−sinθ/2`, `g_θθ=1/4` | The convention pin (sign/factor) + SymPy Re/Im split works exactly | this research (`/tmp` probe, sympy 1.14.0) | the projector form on a 2×2 |
| CP²-over-C_u (`v=[1,z1,z2]`): rank-1 idempotent over Q(i); base `F_B[a,b]=F_B[c,d]=−2`, `F_B[a,c]=…=0`; `g=diag(1,1,1,1)` | The M=0 vacuum **is generically nonzero** and **pure-Kähler/pure-Λ-shaped** (block-diagonal, maximally symmetric) | this research | the C_u rank-1 chart, base point |
| `slice_to_complex` faithfully maps `e_7→i` giving a clean complex projector | The C_u→C bridge carries `i` symbolically (Q(i)) | `embedding_under_E_verification`; this research | C_u entries only |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| "Riemannian structure on manifolds of quantum states" CMP 76, 289 | Provost & Vallée | 1980 | QGT Re=FS / Im=Berry | The split convention (BINDING) |
| "Berry curvature and quantum metric in N-band systems — eigenprojector approach" PRB 104, 085114 | Graf & Piéchon | 2021 | Projector form `Q=Tr(P∂P∂P)`, gauge-invariant | The exact formula to code |
| "MacDowell–Mansouri gravity and Cartan geometry" gr-qc/0611154 | Wise | 2010 | The `F∧F` Lorentz-block contraction structure; EM-vs-Einstein | The *diagnostic* contraction (A.5(b)); NOT the action (Phase C) |
| "The Octonions" math/0105155 §3.4 | Baez | 2002 | OP²=F_4/Spin(9), isotropy = 16-dim spinor | VALD-03 isotropy-irreducibility |
| Non-abelian Berry / Wilson loop, arXiv:1910.13991; non-abelian QGT, arXiv:2312.01086, arXiv:2201.01086 | Sugawa et al.; Chen et al. | 2021/2024 | Gauge-covariance, Wilson-loop invariance, non-abelian QGT (if rank-r) | The gauge-invariance protocol (Q7) |
| "The exceptional Jordan algebra… gravitation and the weak force" arXiv:2304.01213 | Singh | 2023 | h_3(O)→gravity — but via a DIFFERENT construction (NOT the Berry/QGT of the idempotent family) | Contrast only; confirms the *novelty* of the Berry-curvature route |
| EM stress tensor characterization, arXiv:1101.2505 | — | 2011 | Traceless `T^μ_μ=0`, `T~F²` | The EM-shaped discriminant |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (confirmed) | Exact `Q(i)` algebra: `diff`, `re`, `im`, `Matrix.rank/eigenvals`, `cancel`, `simplify` | The whole program runs exact over Q(i); SymPy `I` carries the complex structure symbolically |
| `embedding_under_E_verification.py` | in-repo (warm) | `E`, `proj_u_exact`, **`slice_to_complex`** (e_7→i), `cu_to_complex`, `h3o_from_coords`, `jordan` | The C_u→C bridge (THE key tool); the literal Phase-46 π_u |
| `ring_lemma_verification.py` | in-repo (det SSOT) | `det_3`, `Tr`, `jordan` | Correct octonion association for `T[M]` / Re-anchor |
| `bulk_geometry_verification.py` | in-repo (warm) | `cone_hessian_at_center`, `offcenter_slice_metric`, `spacetime_curvature_of_g`(+`norm_potential=inv_det_X_block`), `_matterless_reference_hessian`, `ricci_decomposition_n4`, `h3_constant_curvature`, `peirce_indices_under_E11`, `_standard_basis_27`, `_flat27` | CALC-03 Re-anchor; the independently-frozen `T[M]` pipeline; the trace/traceless/Weyl decomposition; sign calibration |
| `cartan_phaseA_coframe.py` | in-repo (Phase 75) | The driver template: `_report`, `_source_guard`, `_signature`, `to_mink`, `G_DET2_RAW`, the C_u survivors, foil-vs-verdict | Copy the harness; reuse the Lorentz target + survivors |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| `orbit_dimension_gate.py` (`exact_qq_rank`, import-only) | Exact rank over QQ if a residual/frame-group rank is needed | gauge-invariance frame test (rare); NEVER run its `__main__` (~19-min RING gate) |
| mpmath / NumPy 2.4.2 | float triage (which `F_B` components are nonzero before simplify) | NEVER on a decisive verdict (`fp-float-decisive`); triage only |
| `cartan_phase0_tangent.py` | `_run_engine`/`_report` harness + Phase-74 facts | Copy the skeleton; build on Phase 74 |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| C_u-complex projector QGT (`slice_to_complex`) | Direct octonionic trace-form QGT (Approach 2) | Cross-check only; messier, invites the Euclidean-trace trap |
| Veronese rank-1 chart `v=[1,z1,z2]` | `E(x)=g(x)E_11 g(x)⁻¹` conjugation | Equivalent orbit; the chart is rational/exact (preferred), conjugation is the conceptual cross-check |
| `ricci_decomposition_n4` for trace/traceless | Hand-rolled trace test | The engine is the warm, validated v17.0 harness |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| QGT + `F_B` of the vacuum CP²-over-C_u family (4 real params) | < 5 s (verified this research) | trivial | none |
| `F_B(x;M)` small-M series to leading order | seconds–minutes | symbolic `M`-expansion of the rank-1 idempotent + Re/Im split | keep `M` to leading order; rational coefficients; `cancel` not full `simplify` |
| `T[M]` via `spacetime_curvature_of_g`(+off-switch) + `ricci_decomposition_n4` | seconds–minutes (warm v17.0 path) | the cubic-norm Hessian + n=4 decomposition | reuse the warm engine; the slice is 4d (cheap); the dim-10 V_0 inverse is the cliff (>200s) — stay on the 4d slice |
| Frame-rotation gauge-invariance check | seconds | a generic SO(3,1) rotation of the 4 base directions | small matrices, exact over Q |

**Note:** A.5 is cheap on the vacuum side (verified this research) and moderate on the matter side. The one watchdog risk is a long no-output symbolic `F_B(x;M)` simplify — run foreground with `python3 -u`, commit task-by-task (the v17.0/Phase-75 discipline; see Pitfalls).

**Installation / Setup:** No new packages. Python 3.14.2 / SymPy 1.14.0 confirmed.
```bash
# Nothing to install; all engines in-repo. Run the driver unbuffered:
python3 -u code/<phaseA5_driver>.py
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| CP¹ convention pin | sign/factor of `F_B`, `g`; SymPy Re/Im split | reproduce `F_B=−sinθ/2`, `g_θθ=1/4` over Q(i) | exact match (verified this research) |
| Re(QGT) = FS metric structure | the QGT is the right object; CALC-03 | `Re Q` on the chart = positive-definite FS metric (the round CP² gave `diag(1,1,1,1)`) | positive-definite; SOFT-compare to cone-Hessian character |
| **VALD-03 nonzero-ness** | `F_B ≢ 0` on the slice | `F_B` on the chart generically nonzero (verified: `F_B[a,b]=F_B[c,d]=−2`) | generically nonzero (NOT identically 0) |
| VALD-03 born-from-breaking | the nonzero `F_B` requires the C_u breaking | OP² isotropy-irreducible ⟹ no invariant 2-form ⟹ round Berry=0; the C_u-reduced isotropy DOES admit the Kähler form | consistent (round vanishes; C_u-broken nonzero) |
| `M→0` limit of the matter `F_B` | the matter part vanishes at M=0 | matter `F_B(x;M)` → the vacuum `F_B` as `M→0` | smooth limit; matter part `→0` |
| Off-switch (cross-term OFF) | `T[M]` is genuinely cross-term-sourced (independent of `F_B`) | `spacetime_curvature_of_g(norm_potential=inv_det_X_block)` kills the V_0↔V_{1/2} triple | decisive reduction (the v17.0 ~94% result) |
| Frame-rotation invariance | the verdict scalar is gauge-invariant | apply a generic SO(3,1) rotation to the 4 base dirs; the decisive scalar unchanged | invariant over Q |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| CP¹ / CP² round Berry | rank-1, no breaking | the FS Kähler form (`∫_{CP¹}F_B=−2π`); CP² Kähler form | standard; verified this research |
| Round OP² Berry | no C_u breaking | **vanishes** (isotropy-irreducible, no invariant 2-form) | Baez; arXiv:math/9912112 |
| M=0 vacuum | flat / pure-Λ | NOT R×H³ / Λ<0 (FALSIFIED); pure-Kähler/Λ expected | §6; this research (CP² Kähler) |
| Re(QGT) vs cone-Hessian | the SOFT anchor | same non-Einstein *character* (NOT identity — FS-pullback ≠ cone-Hessian restriction) | CALC-03; §11 |
| sign calibration | round H³ vs cone-Hessian slice | K=−1 (round), K=−1/2 (cone-Hessian slice) | `h3_constant_curvature`; Phase 71 |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| All decisive numbers | exact over Q(i) (sympy) | EXACT (zero tolerance) | `F_B` components, M-power, signatures, `T[M]` match |
| Float triage (optional) | mpmath, pre-simplify only | not decisive | — |

### Red Flags During Computation

- `F_B ≡ 0` on the slice → **degenerate, worse-than-SOFT-KILL** (no antisymmetric content at all). VALD-03 must detect this; report it flat.
- `Re(QGT)` NOT positive-definite / NOT a sensible FS metric → the QGT construction or the family is wrong → STOP and re-examine (before trusting `Im`).
- Matter `F_B` traceless (`T^μ_μ=0` on the contraction) and `~F²` / `~(∂M)²` → **EM-shaped** → SOFT-KILL signal (VALD-04).
- Matter-source support disjoint from `T[M]` support, or magnitude mismatch (the v17.0 ~10³ pattern) → **same-wall mismatch** → SOFT-KILL.
- M-power of the matter `F_B`-source ≠ M-power of `T[M]` at the matched order → EM-shaped, not Einstein → SOFT-KILL.
- A verdict that changes under a frame rotation → gauge artifact (Pitfall 5); switch to an invariant scalar.
- Any nonzero octonion component `e_1..e_6` surviving `π_u` → the C_u projection is mis-implemented.
- `Im(QGT)` nonzero where the family should be real (a coding slip in the `e_7→i` map) → re-check `slice_to_complex`.

## Common Pitfalls

### Pitfall 1: `fp-relabel` / the same-wall trap — calling a nonzero `F_B` "Einstein"
**What goes wrong:** "`F_B ≠ 0` and matter turns it on, therefore gravity/Einstein." A nonzero antisymmetric 2-form is a *field strength* (EM-shaped, source side), not an Einstein structure.
**Why it happens:** after the Phase-75 SURVIVES, "the curvature is nonzero and matter sources it" feels like success; the EM-vs-Einstein distinction blurs because both are "curvature".
**How to avoid:** the decisive verdict is the M-power AND tensor-structure (traceless? `~F²`?) AND support match to an **independently-frozen** `T[M]` (built without `F_B`, `κ` frozen first). Decompose `F_B`'s effective stress into trace/traceless-Ricci/Weyl (`ricci_decomposition_n4`); a traceless `~F²` object sourcing a non-traceless `G[g]` cannot be Einstein.
**Warning signs:** a traceless / `~F²` source declared a metric stress-energy; `T[M]` or `κ` referencing `F_B`; support/magnitude mismatch (the v17.0 ~10³ pattern); M-power mismatch.
**Recovery:** report the SOFT KILL flat ("Lie sector inherits the symmetric-sector mismatch").

### Pitfall 2: `fp-reuse-cone-hessian` — the Re-anchor used as load-bearing for the Im verdict
**What goes wrong:** importing the v17.0 cone-Hessian Riemann (the real-part/symmetric-sector object, verdict NONE) and treating its non-Einstein-ness as the A.5 verdict — re-binding to v17.0 NONE (sector confusion).
**Why it happens:** both routes live on OP², both involve "curvature", the warm v17.0 code is frictionless to import.
**How to avoid:** the cone-Hessian appears ONLY in CALC-03 as a SOFT consistency check on `Re(QGT)`; the verdict-bearing object is `Im(QGT)=F_B`. Type-guard: state in each artifact whether it computes a Re (symmetric) or Im (antisymmetric) quantity; a decisive verdict on a symmetric-sector object is a regression.
**Warning signs:** a v17.0 Riemann import on the decisive path; the verdict echoing "curved but not Einstein" without demonstrating the tensor tested is the Im part.
**Recovery:** excise the symmetric import; recompute `Im(QGT)`; keep CALC-03 separate and soft.

### Pitfall 3: non-abelian-gauge mistake — deciding on a gauge-COVARIANT quantity
**What goes wrong:** treating a frame-dependent `F_B` component (or the connection) as the verdict. For a degenerate subspace the Wilczek–Zee curvature is gauge-COVARIANT (`F→UFU⁻¹`), not invariant.
**Why it happens:** "Berry curvature is gauge-invariant" is true for the *abelian* (single-band) case and is reflexively over-extended.
**RESOLUTION (Q7, this research):** the primitive idempotent `E(x)` is **rank-1 ⟹ the eigenbundle is a LINE bundle ⟹ `F_B` is ABELIAN and `Tr(P ∂P ∂P)` is genuinely gauge-invariant** (the U(1) phase drops out of the projector form — confirmed by the CP¹/CP² probes giving clean invariant numbers). The genuinely non-abelian (Wilczek–Zee, U(r)) structure lives in the *frame* bundle (the SO(3,1) Lorentz freedom and the `V_{1/2}` eigenbundle) — that is **Phase B's** `ω`/`A`, not A.5's canonical `F_B`. **So for A.5, a single gauge-invariant `F_B` suffices; `tr(...)` is not strictly required.** BUT: any statement about the *Lorentz-block contraction* `F_B∧F_B` or any *frame* claim must still be tested under an SO(3,1) frame rotation, and decisive scalars must be invariants (traces, `tr(F_B∧F_B)`, curvature scalars). Distinguish Wilson **loop** (invariant) from Wilson **line** (not).
**How to avoid:** decide on gauge-invariant scalars; verify invariance under a generic frame rotation over Q; pin sign/normalization against the CP¹ anchor.
**Warning signs:** a verdict changing under a frame rotation; a decisive quantity that is a connection component or an open Wilson line.
**Recovery:** switch to an invariant scalar; re-run the frame test.

### Pitfall 4: vacuum mis-read — reintroducing Λ<0 / R×H³, or calling pure-Λ "matter"
**What goes wrong:** (i) expecting Λ<0 / R×H³ at M=0 (the FALSIFIED dead cone-Hessian source-field); (ii) calling a maximally-symmetric `F_B ∝ e∧e` (the Kähler/cosmological form) "matter curvature".
**Why it happens:** the v17.0 framing lingers; a nonzero constant `F_B` looks like "structure".
**How to avoid:** expect flat / pure-Λ (per §6); the round CP²-over-C_u Berry form IS pure-Kähler/pure-Λ-shaped (verified this research) — that is the *vacuum*, not matter. Genuine matter-sourcing must VANISH as M→0 and show structure beyond `∝ e∧e`. Decompose trace/traceless/Weyl; a pure `∝e∧e` constant is Λ, not matter.
**Warning signs:** a report of "matter curvature" that is actually the constant Kähler form; Λ<0 / R×H³ reappearing.
**Recovery:** subtract the vacuum `F_B`; test the *matter part* (M-dependent, vanishing at M=0).

### Pitfall 5: arithmetic hygiene — Jordan product in the QGT, float `i`, octonion_algebra, watchdog stall
**What goes wrong:** using the Jordan product `∘` in `P ∂P ∂P` (wrong object); float `i` (`fp-float-decisive`); importing `octonion_algebra.py` (buggy associator); a long no-output symbolic `F_B(x;M)` simplify killed by the stream watchdog (~600 s).
**How to avoid:** the QGT uses the *associative* complex matrix product on `slice_to_complex(P)` (NOT `∘`); the `i` is symbolic (`sympy.I`) over Q(i); inherit the Phase-0/75 source guard (octonion_algebra absent on the decisive path); run foreground `python3 -u`, commit task-by-task (recover via git log, not re-run).
**Warning signs:** `jordan(...)` inside the QGT; any `import octonion_algebra` on the decisive path; numpy on a decisive rank; a 0-token executor return after a long run.
**Recovery:** swap to the associative complex product; re-run exact over Q(i); recover committed work via git log.

## Level of Rigor

**Required for this phase:** Exact symbolic computation over `Q(i)` (machine-verified), with a controlled small-M series for the matter comparison. Every decisive quantity — `F_B` components, the M-power, the trace/traceless/Weyl split, the `T[M]` match, the signatures — must be a rational/symbolic value from SymPy over Q(i), never a float. The verdict is rendered on **gauge-invariant scalars**.

**Justification:** This is a SOFT-KILL gate on a contract-critical claim (`claim-berry-same-wall`) and a conjunctive partner to Phase 75. A floating-point "approximately Einstein" is explicitly a forbidden proxy (`fp-relabel`, `fp-float-decisive`). The vacuum side is cheap (verified this research); the matter side is moderate; there is no excuse for less than exact.

**What this means concretely:**
- CALC-03: `Re(QGT)` exact over Q(i); the cone-Hessian comparison is a *character* comparison (Ricci-eigenvalue pattern / non-Einstein-ness), explicitly SOFT (a discrepancy is diagnosed, NOT a KILL).
- VALD-03: `F_B` exact over Q(i), shown generically nonzero (NOT identically 0) and born-from-breaking (the isotropy-irreducibility argument). Done FIRST.
- CALC-04: `F_B|_{M=0}` classified exactly (zero/flat / pure-Λ / other) via the trace/traceless/Weyl decomposition; Λ<0 NOT reintroduced.
- VALD-04: the matter `F_B`-source and the `F_B∧F_B` Lorentz-block contraction matched (M-power AND tensor-structure AND support) to an independently-frozen `T[M]`, on gauge-invariant scalars tested under a frame rotation. SURVIVES iff Einstein-shaped; SOFT KILL iff EM-shaped / support-disjoint / M-power mismatch.
- NO float verdict, NO Jordan product in the QGT, NO cone-Hessian as load-bearing, NO Λ<0.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Symmetric-sector cone-Hessian (v17.0 real-part QGT), DEAD = NONE | Antisymmetric/Lie-sector Berry curvature `F_B = Im(QGT)` (v18.0) | 2026-05-31 (v17.0 NONE) | v17.0 NONE binds only Re; A.5 mines the Im half |
| State-form QGT `⟨∂ψ|(1−P)|∂ψ⟩` (gauge phase to fix) | Projector form `Tr(P∂P∂P)` (manifestly invariant) | standard (Graf–Piéchon 2021) | Clean exact symbolic evaluation |
| Octonionic QGT on full h_3(O) (non-associative, ill-defined) | C_u-complex realization (`e_7→i`, associative) | this research | Makes `P∂P∂P` computable exactly over Q(i) |

**Superseded approaches to avoid:**
- The v17.0 cone-Hessian Riemann as load-bearing — a different tensor, DEAD (`fp-reuse-cone-hessian`).
- The bare trace form on V_{1/2} as the verdict metric — Euclidean (4,0) OP² FOIL (Phase 75); route the verdict through the complex QGT.
- `peirce_coupling.py` (cited, absent); use `bulk_geometry`/`embedding`.

## Open Questions

1. **VALD-04: is the matter-sourced `F_B` Einstein-shaped or EM-shaped? (the genuinely-open SOFT-KILL clause)**
   - What we know: the vacuum `F_B` is the pure-Kähler/pure-Λ form (verified); the Re-anchor reproduces the FS metric; the v17.0 symmetric sector was EM-mismatched (NONE). The Lie sector is a *different* tensor (NONE doesn't bind it).
   - What's unclear: whether the matter part of `F_B` (and `F_B∧F_B` on the Lorentz block) matches a frozen `T[M]` in M-power + tensor-structure + support. This is exactly the clause designed to be MEASURED.
   - Impact: this is the clause most likely to trigger the SOFT KILL (the symmetric sector failed the analogous test; the Lie sector may inherit it).
   - Recommendation: compute the matter `F_B` small-M series; build `T[M]` independently (off-switch pipeline); test the three matches on gauge-invariant scalars. Report flat either way.

2. **Q6: the matter-on rank-1 idempotent construction over C_u.**
   - What we know: the vacuum CP²-over-C_u family is clean rank-1 over Q(i) (verified); `_offcenter_subs`/`rho_J` give the off-center basepoint move.
   - What's unclear: whether the rank-1 idempotent of the *perturbed* (`X_bg=I/3+M`) configuration stays a clean rank-1 C_u projector (does `M∈V_{1/2}` keep it in C_u, or does it leak `e_1..e_6` that `π_u` then kills, changing rank?). The C_u-faithfulness of the matter family is the modeling step to pin in the plan.
   - Recommendation: construct `E(x;M)` explicitly to leading order in M; verify rank-1 + C_u-faithfulness (no `e_1..e_6` leak on the decisive path) before trusting the matter `F_B`; cross-check the `M→0` limit.

3. **CALC-03: what exactly does "same non-Einstein CHARACTER" mean, and will it hold?**
   - What we know: `Re(QGT)` is the FS pullback (round CP² gave `diag(1,1,1,1)`); the cone-Hessian is `Hess(−log det)|_{V_0}` (diag(9,9,18,18)). They are DIFFERENT constructions.
   - What's unclear: whether the FS-pullback's Ricci-eigenvalue pattern / non-Einstein-ness matches the cone-Hessian's. A discrepancy is EXPECTED (different constructions) and is INFORMATIVE, NOT a KILL.
   - Recommendation: define "character" operationally as the Ricci-eigenvalue *pattern* / non-Einstein-ness / sign structure (NOT numerical identity); report the comparison as a diagnostic; do NOT KILL/HALT on this anchor alone (`fp-reuse-cone-hessian`).

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| C_u-complex projector QGT | contested `slice_to_complex` faithfulness | direct octonionic trace-form QGT (Approach 2) as cross-check | low (a few lines); confirmation only |
| Matter `F_B` small-M series | symbolic blow-up / watchdog stall | rational-`M` spot evaluations (exact, triage) + commit-per-task | low–medium |
| Einstein-shaped verdict | the match fails (EM-shaped) | this IS the SOFT-KILL verdict — report it flat, recommend STOP before B | none (it's the answer) |
| `Re(QGT)` ≠ cone-Hessian character | different constructions (expected) | report as INFORMATIVE diagnostic; do NOT KILL | none (soft anchor) |

**Decision criteria:** A.5 is a SOFT-KILL gate. If VALD-04 shows EM-shaped / support-disjoint / no M-power match (exactly over Q(i)), the verdict is **SOFT KILL** ("Lie sector inherits the symmetric-sector mismatch"), recommend STOP before Phase B — reported FLAT (negative-result-is-success). If it shows Einstein-shaped (M-power + tensor-structure + support matchable to a frozen `T[M]`), **SURVIVES** to B (conjunctive with Phase 75 ✓). The Re-anchor (CALC-03) and the vacuum classification (CALC-04) are diagnostics, never standalone KILLs. The only legitimate "alternative" is a cross-check (Approach 2, the `M→0` limit, the off-switch), never a rescue of an EM-shaped result.

## Novelty / Prior-Art Survey (Q8)

**Finding: NOVEL.** Targeted web searches (arXiv, Project Euclid, journals) found:
- The QGT Re=Fubini–Study / Im=Berry split (Provost–Vallée) and the projector form (Graf–Piéchon) are **standard and confirmed** across multiple independent sources.
- `OP²=F_4/Spin(9)` (52=36+16), `h_3(O)`, `F_4=Aut(h_3(O))`, and the **isotropy-irreducibility** (the unique rank-1 exceptional symmetric space; isotropy = the unique irreducible 16-dim Spin(9) spinor rep ⟹ no invariant Kähler 2-form) are **established** (Baez; Berger; arXiv:math/9912112). This is the load-bearing VALD-03 fact and it is solid.
- **NO computation of the Berry curvature / imaginary part of the QGT of the OP²=F_4/Spin(9) primitive-idempotent family was found.** The one paper connecting `h_3(O)` to gravity (Singh, arXiv:2304.01213) uses a DIFFERENT construction (a trace dynamics / U(1)-gravity proposal, not the Berry/QGT of the idempotent family) — it does NOT compute `Im Tr(P∂P∂P)` and does NOT use the MacDowell–Mansouri `F∧F` contraction.
- **NO computation of MacDowell–Mansouri gravity from an exceptional Jordan algebra was found.** Wise (gr-qc/0611154) gives the MM/Cartan statement (standard); the exceptional-Jordan-algebra connection to MM is absent from the literature.

So the imaginary-QGT/Berry-curvature route on `OP²=F_4/Spin(9)`, and its MM-style Einstein-vs-EM same-wall test, is **genuinely novel territory**. The recipe rests on standard tools (Provost–Vallée QGT, the CP¹/CP² anchors verified this research, the isotropy-irreducibility theorem) applied to a system no one has computed. Per the Novel Territory protocol: the nearest solved problems are CP¹/CP² (Berry curvature of projective spaces — exactly anchored this research) and the v17.0 cone-Hessian (the real-part analog — the same-wall *failure pattern* to test for). Confidence: HIGH for the base tools, MEDIUM for the VALD-04 outcome, LOW that anyone has done this before (which is the point).

## Order-of-Magnitude / Structural Expectations (per clause)

- **VALD-03 (well-definedness):** `F_B` is generically **NONZERO** (verified: the round CP²-over-C_u Berry form is `F_B[a,b]=F_B[c,d]=−2`, block-diagonal). Born-from-breaking is solid (OP² isotropy-irreducible ⟹ round Berry=0; the C_u-broken isotropy admits the Kähler 2-form). An identically-zero `F_B` (a degenerate, worse-than-SOFT outcome) is UNLIKELY but must be checked. Expected: PASS (well-defined, nonzero).
- **CALC-03 (Re-anchor):** `Re(QGT)` = a positive-definite Fubini–Study metric (round CP² gave `diag(1,1,1,1)`). Its *character* vs the cone-Hessian (diag(9,9,18,18); round H³ K=−1): a discrepancy is EXPECTED (FS-pullback ≠ cone-Hessian restriction) and INFORMATIVE, NOT a KILL. Expected: a sensible FS metric of broadly non-Einstein character; SOFT diagnostic.
- **CALC-04 (M=0 vacuum):** expected **pure-Λ / pure-Kähler-shaped** (`F_B ∝ e∧e`, the maximally-symmetric CP² Kähler form — verified block-diagonal). Λ=0 in the sense of §6 (the M=0 *spacetime* vacuum is flat; the Berry 2-form's vacuum is the Kähler/cosmological form, NOT matter). Do NOT reintroduce Λ<0. Expected: pure-Λ/Kähler.
- **VALD-04 (the decisive clause):** **MEDIUM, genuinely open.** The structural worry: the round Berry form is the *Euclidean* CP² Kähler form (symmetric, block-diagonal, maximally symmetric). For matter to be *Einstein-shaped*, the C_u-breaking + M-dependence must distort `F_B` toward a tensor whose Lorentz-block `F_B∧F_B` contraction matches a frozen `T[M]` in M-power + structure + support. The v17.0 precedent (the symmetric sector FAILED the analogous test, NONE, κT~10³<G, support-disjoint) is the **base rate**: the most likely outcome is that **the Lie sector inherits the same-wall mismatch (SOFT KILL)** — but this is a *different tensor*, so it genuinely might not, which is why it is computed. Expected (honest base rate): SOFT KILL more likely than SURVIVES, but MEASURE it.

## Caveats and Alternatives (pre-submission self-critique)

1. **What assumption might be wrong?** That the C_u-complex realization of `P ∂P ∂P` is THE physically correct QGT (vs an octonionic refinement). Mitigation: Approach 2 (octonionic trace-form QGT) as an independent cross-check; the CP¹ anchor pins the convention. The C_u realization is forced by `u=e_7` (the only associative completion), so this is low risk.
2. **What alternative did I dismiss too quickly?** The state-form QGT `⟨∂ψ|(1−P)|∂ψ⟩` — dismissed because it carries a gauge phase to fix by hand (an `fp-` risk). Correct to dismiss for the decisive path (METHODS M1), but it could serve as a cross-check if the projector form is contested.
3. **What limitation am I understating?** The matter-on idempotent construction over C_u (Q6) — I have de-risked only the *vacuum* family exactly; the matter family's C_u-faithfulness is asserted, not yet verified. The plan MUST build `E(x;M)` explicitly and check rank-1 + no `e_1..e_6` leak before the VALD-04 verdict. This is the single biggest modeling gap.
4. **Is there a simpler method I overlooked?** Possibly: if the matter `F_B` were obviously traceless `~(∂M)²` by a symmetry argument (an EM-shaped no-go), VALD-04 could short-circuit to SOFT KILL without the full `T[M]` build. Worth a quick structural check first (is the matter `F_B` forced traceless by the C_u/Kähler structure?), but the full match is the rigorous verdict.
5. **Would a specialist disagree?** A condensed-matter geometer might insist on the non-abelian (Wilczek–Zee) treatment. RESOLVED (Q7): the *primitive idempotent* is rank-1 ⟹ abelian `F_B` (the projector form is genuinely gauge-invariant); the non-abelian structure is in the *frame* bundle (Phase B). A specialist might also flag that the round CP²-over-C_u Berry form being Kähler (symmetric) sits in tension with the Lorentzian soldered coframe — exactly the foil-vs-verdict subtlety I flag (intrinsic Kähler 2-form vs Lorentz-block contraction); the plan must carry both, as Phase 75 did.

## Sources

### Primary (HIGH confidence)
- `paper6-cartan-tetrad-prompt.md` — authoritative milestone spec (Phase A.5 §, QGT/Berry def, Pass/Fail, Forbidden proxies); BINDING.
- `.gpd/CONVENTIONS.md` §1/§3/§4/§6/§7/**§11** (the v18.0 Cartan/MM Berry layer; the QGT objects, Re/Im split, Q(i), Λ=0); BINDING.
- Provost & Vallée, CMP 76 (1980) 289 — QGT Re=Fubini–Study / Im=Berry. BINDING split convention.
- `code/cartan_phaseA_coframe.py` + `75-01-SUMMARY.md` (Phase 75, human-ratified SURVIVES) — the structural template; the C_u survivors `{11,18,19,26}`; the soldered (1,3) Lorentz target; SO(3,1) FORCED; foil-vs-verdict discipline. In-repo, verified.
- `code/embedding_under_E_verification.py` (`E`, `proj_u_exact`, `slice_to_complex`, `cu_to_complex`), `code/ring_lemma_verification.py` (`det_3`, `Tr`, `jordan`), `code/bulk_geometry_verification.py` (`cone_hessian_at_center`, `spacetime_curvature_of_g`, `ricci_decomposition_n4`, `h3_constant_curvature`, `_matterless_reference_hessian`) — the SSOT engines. Inspected this research.
- `.gpd/research/{METHODS,PITFALLS,SUMMARY,COMPUTATIONAL}.md` (v18.0) — M1 projector `F_B`; Pitfalls 3/4/5/6/10; the EM/non-abelian discriminants; the engine inventory. Project-level research.
- **Exact-over-Q(i) spot computations performed during this research** (sympy 1.14.0): CP¹ (`F_B=−sinθ/2`, `g_θθ=1/4`, full QGT) and CP²-over-C_u (rank-1 idempotent over Q(i); base `F_B[a,b]=F_B[c,d]=−2`, `g=diag(1,1,1,1)`). These pin the convention and de-risk the vacuum recipe (Q1/Q2/VALD-03/CALC-04).

### Secondary (MEDIUM confidence)
- Graf & Piéchon, PRB 104 (2021) 085114, arXiv:2102.09899 — projector-form QGT `Tr(P∂P∂P)`, gauge-invariant. (Also Wikipedia "Quantum geometry (condensed matter)".)
- Wise, gr-qc/0611154; MacDowell & Mansouri, PRL 38 (1977) 739 — the `F∧F` Lorentz-block contraction structure (the *diagnostic* A.5(b); NOT the action — Phase C).
- Baez, "The Octonions", math/0105155 §3.4 — OP²=F_4/Spin(9), isotropy = 16-dim spinor.
- arXiv:math/9912112 (weak Spin(9) structures); Berger's list — OP² isotropy-irreducible / no invariant Kähler form (the VALD-03 born-from-breaking fact).
- Wilczek–Zee 1984; arXiv:1910.13991 (Wilson loop / Wilczek–Zee phase); arXiv:2312.01086, arXiv:2201.01086 (non-abelian QGT) — the gauge-invariance protocol (Q7); rank-1=abelian vs rank-r=non-abelian.
- EM stress tensor: Wikipedia "Electromagnetic stress-energy tensor"; arXiv:1101.2505 — traceless `T^μ_μ=0`, `T~F²`, conformal (the EM-shaped discriminant).
- v17.0 Ph73 NONE post-mortem (`.gpd/research/archive-v17`) — the same-wall *failure pattern* (κT~10³<G, support-disjoint, S≠0/Weyl≠0) VALD-04 tests for; binds only Re.

### Tertiary (LOW confidence)
- Singh, arXiv:2304.01213 ("exceptional Jordan algebra… gravitation and the weak force") — CONTRAST ONLY: confirms the *novelty* (a different h_3(O)→gravity construction, not the Berry/QGT route).
- WebSearch result summaries (the F4/Spin(9) and QGT-split confirmations) — corroborated against the primary sources above.

## Metadata

**Confidence breakdown:**
- Mathematical framework (QGT recipe, Re/Im split, C_u bridge): **HIGH** — anchored exact over Q(i) (CP¹ + CP²-over-C_u) this research; Provost–Vallée + Graf–Piéchon.
- Standard approaches (projector QGT, ordering, warm-engine reuse): **HIGH** — mirrors the validated Phase-75 driver; the engines exist and are inspected.
- VALD-03 well-definedness (born-from-breaking): **HIGH** — OP² isotropy-irreducibility confirmed (literature + the nonzero CP²-over-C_u probe).
- Computational tools: **HIGH** — all in-repo, versions confirmed (SymPy 1.14.0 / Python 3.14.2).
- Validation strategies: **HIGH** — CP¹ anchor, off-switch, frame-rotation test, sign calibration all available.
- CALC-04 vacuum classification: **HIGH/MEDIUM** — pure-Λ/Kähler expectation backed by the CP² probe; exact classification to compute.
- **VALD-04 outcome (Einstein vs EM)**: **MEDIUM** — the genuinely-open SOFT-KILL clause, designed to be MEASURED; the v17.0 base rate suggests SOFT KILL is more likely, but the Lie sector is a different tensor.
- Q6 matter-on idempotent construction: **MEDIUM** — vacuum de-risked; matter family's C_u-faithfulness to verify in the plan.
- Novelty (Q8): **HIGH** — no prior Berry-QGT-of-OP²-idempotents or MM-from-exceptional-Jordan computation found.

**Research date:** 2026-06-02
**Valid until:** Physics/math results stable indefinitely (the QGT split, OP² isotropy-irreducibility, the CP¹/CP² anchors). Tool versions (SymPy 1.14.0) and the in-repo engine API are the faster-moving pieces; re-confirm if the engines are refactored.
