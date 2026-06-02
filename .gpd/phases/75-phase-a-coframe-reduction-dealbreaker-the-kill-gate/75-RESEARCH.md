# Phase 75: Phase A — Coframe-Reduction Dealbreaker (THE KILL GATE) - Research

**Researched:** 2026-06-01
**Domain:** Mathematical physics — Peirce/Cartan reduction of the soldering form on h_3(O); complex-structure (C_u) reduction of the 16-dim half-eigenspace V_{1/2} to a candidate 4-dim Lorentzian coframe; exact-over-Q linear algebra; forced-vs-arbitrary structure-group analysis.
**Confidence:** HIGH on the mechanism, the engine reuse, and the three decisive computations (each spot-verified exact over Q during this research). MEDIUM only on the *outcome of clause (c)* (forced-vs-arbitrary residual structure group), which is the genuinely-open part of the KILL gate and is designed to be measured, not assumed.

## Summary

Phase A is a **cheap, decisive KILL gate**: exact linear algebra over Q on a 16-dim space, no calculus, no curvature. It asks whether `(E_11, u=e_7)` ALONE reduces the 16-dim V_{1/2} soldering form to a **4-dim Lorentzian coframe carrying SO(3,1)** — a greenlight for the rest of v18.0, or a flat KILL of the whole route. It is NOT a write-up phase.

The decisive methodological question (Q1 in the brief — "what is the induced coframe pairing?") is now **resolved with an exact-over-Q computation** performed during this research. The answer overturns the naive reading: the bare Jordan trace form `Tr(δ∘δ')` restricted to π_u(V_{1/2}) gives `diag(2,2,2,2)` — **Euclidean (4,0)**, because that IS the compact Fubini–Study metric of OP² = F_4/Spin(9) (a Riemannian symmetric space, which carries no Lorentzian invariant form). Reading the signature off the bare trace form would manufacture a spurious "not Lorentzian" KILL. The **correct, geometrically canonical pairing is the soldering-form metric** (candidate (b)), made exact-over-Q via the **Peirce soldering bilinear** `B(δ,δ') = (δ∘δ')|_{V_0}` (the OD3 map V_{1/2}×V_{1/2}→V_0 ≅ R^{3,1}): this map **surjects (rank 4) onto the full R^{3,1}**, and the diagonal `n(δ)=B(δ,δ)` lands on the **light cone** (`det_2(n(δ)) = 0` identically), with forward timelike component `x0 = ½‖δ‖² ≥ 0`. The Lorentzian (1,3) signature lives on the **V_0 = h_2(C_u) ≅ R^{3,1} target** (the already-validated det_2 benchmark), to which the coframe is soldered — NOT as a quadratic form on V_{1/2} itself.

**Primary recommendation:** Run the three checks exactly over Q reusing the warm engines. **CALC-01** (image dim of π_u(V_{1/2})) = exact column rank over QQ — **verified = 4** in this research (surviving engine coords {11,18,19,26} = C_u components of the (1,3)=x2 and (1,2)=x3 octonion entries = C_u²). **CALC-02** (coframe signature) = read the **det_2 signature on the R^{3,1} target of the soldering bilinear B, AND confirm B has rank 4 onto it** — the soldering-form metric, NOT the bare trace form (which is the Euclidean OP² metric and must be reported as the diagnostic foil, not the verdict). **VALD-02** (forced-vs-arbitrary) = reuse `orbit_dimension_gate` infinitesimal-action rank to show the surviving 4-space is the (E_11,u)-canonical Stab-eigenspace (the Spin(3,1) Lorentz block of Spin(9,1)∩commutant(u)), with NO extra free parameters. KILL flat on any failing clause; never relabel "approximately 4d / approximately Lorentzian".

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `paper6-cartan-tetrad-prompt.md` ("Phase A: the coframe-reduction dealbreaker"; new-objects block: `e=dE`, `π_u`; conventions lock) | Authoritative milestone spec (BINDING) | Defines the KILL gate, the three clauses, and the forbidden proxies | Read; obey verbatim — clauses (a)/(b)/(c), the KILL condition, `fp-arbitrary-reduction`/`fp-relabel-approx-4d`/`fp-float-decisive` | Plan, execution, verification (every decisive verdict) |
| `derivations/52-kkt-spacetime.tex` + `52-observer-uniqueness.tex` | Benchmark / template (THE V_0 precedent) | The SAME Phase-46 π_u : h_2(O)→h_2(C_u)≅R^{3,1} reduction (V_0:10→4; det_2 Lorentzian (1,3); SO(3,1) boosts B_i=L_{σ_i}∈Str_0; Uniqueness Thm: h_2(C_u) the UNIQUE JSpin(3) image of π_u, forced by u). OD3: V_{1/2}×V_{1/2}→V_0 surjective, rank 10 on V_0 / rank 4 on π_u(V_0) | Use as the target-space signature benchmark; reuse the (1,3) det_2 result and OD3; PARALLEL (do not blindly copy) for V_{1/2} | Plan (recipe), execution (cross-check), verification (the V_0 limit) |
| `code/cartan_phase0_tangent.py` (Phase 74, DONE/verified) | Prior artifact (the warm driver pattern) | Establishes the exact-over-Q reuse pattern (`import bulk_geometry_verification as BG`), the Peirce layout V_{1/2}=idx 11..26, and the `_report`/`_run_engine` harness | Copy the driver pattern; build on Phase 74's verified V_{1/2}-valued `dE`, kernel==span{11..26} | Plan (code skeleton), execution |
| `code/ring_lemma_verification.py` | det SSOT (BINDING) | `det_3`, `Tr`, `Tr2`, `c(X,Y)=Tr(X∘Y)`, `polarize_d`, `jordan`, `X_from_symbols`, exact-Q guards. The cubic norm + trace form for the pairing and any det_2 | Import; call `Tr`, `jordan`, `X_from_symbols` (det_2 built from `_coord_from_octmat`) | Plan, execution |
| `code/bulk_geometry_verification.py` (`peirce_indices_under_E11`, octonion/Jordan primitives) | Engine (warm, SSOT-consistent) | The Peirce decomposition under E_11; `h3o_from_coords`, `_standard_basis_27`, `_flat27`, `_coord_from_octmat`, `jordan`, `octmat_*`, `oct_zero` — verbatim det_3 dependencies | Import; call `peirce_indices_under_E11`, `_standard_basis_27`, `_flat27`, `_coord_from_octmat`, `jordan` | Plan, execution |
| `code/embedding_under_E_verification.py` (`proj_u_exact`, `cu_to_complex`, `slice_to_complex`, `E()`) | Engine (the C_u/π_u machinery) | The literal Phase-46 C_u projection (`proj_u_exact(a, u_index=7)` keeps comps 0,7; `E(X)` = entrywise π_u) used for V_0; docstring line 55 records the expectation `V_1~R, V_{1/2}~C_u^2, V_0~h_2(C_u)` | Reuse `proj_u_exact`/`E()` as π_u (the SAME map as V_0) — do NOT invent a new reduction | Plan, execution, verification |
| `code/orbit_dimension_gate.py` (`infinitesimal_action`, `exact_qq_rank`, `span_rank_over_QQ`, f_4/e_6 machinery) | Engine (stabilizer calibration) | Forced-vs-arbitrary verdict for clause (c): residual structure group as a nullspace/rank over QQ; calibration anchors (Stab_{E_6}(E_11)=61, Stab_{V_0}=45=Spin(9,1)) | Reuse for the residual-structure-group rank; reproduce anchors before trusting any new count | Plan, execution (VALD-02), verification |
| `.gpd/research/{SUMMARY,METHODS,PITFALLS,COMPUTATIONAL}.md` (v18.0 project research) | Prior artifact (project-level research) | Method M4/M5 (Phase A), Pitfall 2 (`fp-arbitrary-reduction`), the OP²-not-Kähler subtlety, the engine inventory and `peirce_coupling.py`-absent correction | Build on; do not re-derive | Plan (constraints), verification |

**Missing or weak anchors:**
- `code/peirce_coupling.py` cited in the spec **does NOT exist** in the repo (confirmed; also flagged in SUMMARY.md). The Peirce-under-E_11 machinery lives in `bulk_geometry_verification.py::peirce_indices_under_E11` and `embedding_under_E_verification.py`. The plan must point at those, NOT at the absent file.
- No CONTEXT.md / init.json for Phase 75 (confirmed). All constraints are inherited from the milestone spec + contract slice (captured above and in Conventions). No locked user decisions to honor beyond the contract.
- `octonion_algebra.py` is **BANNED** (buggy associator). It is present on disk but MUST NOT be imported on any decisive path. The Phase-0 source guard (DERV-01) already enforces this; Phase A inherits the guard.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Det SSOT (cubic norm) | `ring_lemma_verification.py` `det_3`, cross-term `2Re(x2* x0* x1)` (F_4-invariant; CH + 324/324 verified) | the cyclic `2Re((x1 x2)x3)` variant (BUG, off by 16, only 30/324 annihilation) — REJECTED | spec conventions lock; Phase 74 DERV-01 |
| Octonion multiplication | Fano table, `e1 e2 = e4` | — | spec; `oct_mul` |
| Complex structure | `u = e_7` (C_u = span{1, e_7}) | any `u ∈ S^6` (G_2-conjugate) | spec; `proj_u_exact(u_index=7)` |
| Primitive idempotent | `E_11 = diag(1,0,0)` | E_22, E_33 (F_4-conjugate, OD7) | spec |
| Peirce grades (engine layout) | `V_1={0}` (α); `V_0={1..10}`; `V_{1/2}={11..26}`. Flat layout `[α,β,γ, x1(8), x2(8), x3(8)]` ⇒ idx 11..18 = x2 = (1,3) entry, idx 19..26 = x3 = (1,2) entry | — | `_flat27`; `peirce_indices_under_E11`; Phase 74 |
| Spacetime sub-slice | `h_2(C_u) ≅ R^{3,1}`; Minkowski coords `x0=(β+γ)/2, x1=Re(x1), x2=⟨x1,u⟩, x3=(β−γ)/2` | — | `52-kkt-spacetime` |
| Metric signature | **mostly-minus (+,−,−,−)**, `det_2 = x0² − x1² − x2² − x3²`, `G=diag(+1,−1,−1,−1)`, signature (1,3) | (−,+,+,+) | spec (v18.0 lock); `52-kkt-spacetime` Eq.46.4 |
| Exactness | **EXACT over Q** on every decisive verdict (`sympy.Matrix.rank()`, `.eigenvals()`, `.nullspace()` over QQ); NEVER numpy/float | mpmath/float = TRIAGE ONLY, never decisive | spec (`fp-float-decisive`) |

**CRITICAL:** All results below use these conventions. The det_2 Lorentzian form is read on the **R^{3,1} target** of the soldering map; the bare trace form on V_{1/2} is **Euclidean (4,0)** (the compact OP² metric) and is the diagnostic foil, never the verdict. Converting a Euclidean Gram to Lorentzian via a Wick rotation is `fp-arbitrary-reduction`.

Convention loading: see agent-infrastructure.md Convention Loading Protocol. Phase 74 already reproduced the v18.0 lock byte-for-byte (metric_signature glyph reconciled to mostly-minus, string-only; engine `eta=diag(+1,-1,-1,-1)` unchanged).

## Mathematical Framework

### The C_u / π_u reduction of V_{1/2} (Q2 — RESOLVED, verified exact over Q)

π_u is the **entrywise projection onto C_u = span{1, e_7}** — the SAME map (`embedding_under_E_verification.py::proj_u_exact` / `E()`) that sent V_0 = h_2(O) → h_2(C_u) ≅ R^{3,1} in Phase 46. Acting on the 16-dim V_{1/2}(E_11) (the (1,3)=x2 and (1,2)=x3 octonion entries), it keeps octonion components 0 and 7 of each entry and zeros components 1..6.

**Verified (exact over Q, this research):** π_u(V_{1/2}) has image dimension **4**, spanned by engine flat-coords **{11, 18, 19, 26}** = {Re(x2), ⟨x2,e_7⟩, Re(x3), ⟨x3,e_7⟩} = **C_u²** (two octonion entries × two C_u components). This is the exact analog of the V_0 reduction: where V_0's single h_2(O) octonion entry x1 reduced to C_u (2-dim), here the **two** Peirce off-diagonal entries each reduce to C_u, giving 2×2 = 4. This matches the project-research expectation (`embedding_under_E_verification.py` docstring line 55: `V_{1/2} ~ C_u^2`).

### The induced coframe pairing (Q1 — THE CRUX, RESOLVED with exact-over-Q evidence)

Four candidates were posed. The decisive computation (performed during this research, exact over Q) settles which is canonical:

| Candidate | What it computes | Exact-over-Q result on π_u(V_{1/2}) | Verdict |
| --------- | ---------------- | ----------------------------------- | ------- |
| **(a)** Bare Jordan trace form `Tr(δ∘δ')` restricted to π_u(V_{1/2}) | Gram of the 4 coframe dirs under `Tr(X∘Y)` | `Gram = diag(2,2,2,2)`, eigenvalues {2×4} → **signature (4,0) EUCLIDEAN** | **WRONG pairing** for the coframe signature. This IS the compact Fubini–Study metric of OP²=F_4/Spin(9) (Riemannian symmetric, NO invariant Lorentzian form). Reading the verdict here manufactures a spurious "not Lorentzian" KILL. **Report as the diagnostic foil.** |
| **(b)** Soldering-form metric `g_{μν}=η_{ab} e^a_μ e^b_ν`, `e=π_u(dE)` | Pullback through the soldering map to R^{3,1}; η = det_2 on the target | Lorentzian (1,3) on the R^{3,1} target (see (c) for the exact realization) | **THE induced coframe pairing.** Rigorous Cartan-geometry definition (Sharpe 1997): the metric is the pullback of the model-space (R^{3,1}) metric through the soldering form. Lorentzian structure is INHERITED from the V_0=h_2(C_u)=R^{3,1} det_2, to which the coframe solders. |
| **(c)** Peirce-product quadratic refinement: bilinear `B(δ,δ')=(δ∘δ')|_{V_0}` into V_0≅R^{3,1}, signature read via det_2 on the TARGET | The OD3 map V_{1/2}×V_{1/2}→V_0; `n(δ)=B(δ,δ)`; det_2 on R^{3,1} | `B` **surjects, rank 4** onto R^{3,1}; `n(δ)` lands on the **light cone** (`det_2(n(δ))≡0`), `x0=½‖δ‖²≥0` (forward). `det_2(δ∘δ)≡0` identically (Brahmagupta–Fibonacci) | **The EXACT-over-Q realization of (b).** This is the recommended computable recipe: the signature (1,3) is the det_2 signature on the R^{3,1} target, and `B` is confirmed full-rank onto it. (c)-as-a-scalar-quadratic `det_2(δ∘δ)` is degenerate (≡0) and must NOT be used as the Gram. |
| **(d)** Freudenthal/cubic-norm quadratic-trace form on V_{1/2} | `polarize_d` / `Tr2`-type quadratic | Not the coframe metric: the cubic-norm quadratic trace on the off-diagonal Peirce block reduces to the same positive-definite norm structure as (a) on π_u(V_{1/2}); does not produce Lorentzian signature on V_{1/2} itself | **Not the coframe pairing.** Useful only as the Phase-C trace-form-invariance object, not here. |

**THE DECISION:** The induced coframe pairing is **candidate (b), the soldering-form metric, realized exactly over Q via the candidate-(c) Peirce soldering bilinear** `B(δ,δ') = (δ∘δ')|_{V_0} ∈ V_0 ≅ R^{3,1}`, with the Lorentzian signature read as the **det_2 signature on the R^{3,1} target** (the validated V_0 benchmark) together with the **rank-4 surjectivity of B** onto that target. Justification: OP² = F_4/Spin(9) is a **compact Riemannian symmetric space** carrying no invariant Lorentzian form (SUMMARY.md, "OP²-not-Kähler"); therefore the Lorentzian structure CANNOT live as a quadratic form intrinsic to V_{1/2} — it can only be **inherited by soldering V_{1/2} to the V_0 = h_2(C_u) = R^{3,1} spacetime**. The Peirce product V_{1/2}×V_{1/2}→V_0 (OD3) is precisely that soldering map, and det_2 on V_0 is the precisely the validated Minkowski form. This is geometrically the standard tetrad construction: `e: T_x M → R^{3,1}` (the model space), `g = e^* η`.

**Cross-check (mandatory, both defensible readings reported):** Compute and REPORT BOTH (i) the bare trace-form Gram `diag(2,2,2,2)` — the Euclidean OP² foil — and (ii) the soldering det_2 signature (1,3) on the R^{3,1} target + rank-4 of B. The verdict rests on (ii); (i) is reported transparently so the reader sees that "4-dim" is genuine (CALC-01) but the Lorentzian signature is a SOLDERED, not intrinsic-to-V_{1/2}, property. This is the honest framing that defeats `fp-relabel`: we are NOT claiming V_{1/2} is intrinsically Lorentzian; we are claiming the coframe `e=π_u(dE)` solders the 4-dim π_u(V_{1/2}) onto the Lorentzian R^{3,1}, which is exactly what a tetrad does.

### The forced-vs-arbitrary criterion (Q3 — method fixed, outcome to MEASURE)

VALD-02 must show the 4-dim reduction and its SO(3,1) are **forced by (E_11, u) alone**, with NO arbitrary extra choice. The decisive over-Q test (Method M5, `orbit_dimension_gate` style):

1. The surviving 4-space π_u(V_{1/2}) = span{11,18,19,26} must be an **invariant/eigenspace of an (E_11,u)-canonical operator**, not a hand-picked subspace. It is: it is exactly the **fixed space of the C_u projector** `proj_u` (eigenvalue-1 space of π_u acting on V_{1/2}) — `proj_u` is determined by u=e_7 alone, and V_{1/2} by E_11 alone. No basis selection enters (the engine basis is the canonical Peirce basis; the image is computed by rank, not by choosing 4 of 16 directions).
2. The **residual structure group** preserving the reduced coframe = the subgroup of the ambient Spin(9,1) (the Levi of Stab_{E_6(-26)}(E_11), dim 45) that ALSO commutes with u=e_7 (preserves C_u). Compute its Lie algebra as the **nullspace over QQ** of the joint action {fix E_11, commute with the u-multiplication, preserve π_u(V_{1/2})}, via `infinitesimal_action`/`exact_qq_rank`. SO(3,1) is FORCED iff this stabilizer-compatible residual algebra **contains so(3,1) with no extra free parameters** tracing to an arbitrary frame choice.
3. **Connect to the v17.0 / Phase-48 split** `Spin(9,1) ⊃ Spin(3,1) × Spin(6)` (Lorentz × internal): the reduction must land on the **Spin(3,1) 4d vector** (forced), not on the Spin(6) internal directions. Cross-check the residual-group dimension against the Phase-48 `so(3) × so(6)` data and the v17.0 Stab counts (61, 45). The boosts B_i = L_{σ_i} ∈ Str_0 (`52-kkt-spacetime` §"Boost identification", `[B_i,B_j]=-ε_{ijk}J_k`, Killing signature (3,3)=so(3,1)) are the SO(3,1) generators to match.

**Outcome confidence: MEDIUM.** Clauses (a) [dim=4] and (b) [Lorentzian via soldering] are verified HIGH. Clause (c) [forced SO(3,1), no smuggled choice] is the genuinely-open part — it is plausible by the V_0 Uniqueness-Theorem analogy and the C_u-projector-eigenspace argument, but the residual-group rank MUST be computed, not assumed. This is where a `fp-arbitrary-reduction` KILL would trigger if SO(3,1) is not forced.

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| `E_11 ∘ δ = (1/2)δ`, `δ ∈ V_{1/2}` | Peirce half-eigenspace identity | McCrimmon; Phase 74 DERV-02 (verified 16/16) | Defines V_{1/2}; the soldering form `dE` is V_{1/2}-valued |
| `π_u(a) = a_0 + a_7 e_7` (octonion → C_u) | The Phase-46 C_u bottleneck | `proj_u_exact`; `52-kkt-spacetime` | CALC-01: the reduction map |
| `det_2(X) = x0² − x1² − x2² − x3²`, `G=diag(+1,−1,−1,−1)` | Minkowski form on h_2(C_u) | `52-kkt-spacetime` Eq.46.4 | CALC-02: the (1,3) target signature |
| `B(δ,δ') = (δ∘δ')\|_{V_0}` : V_{1/2}×V_{1/2} → V_0 ≅ R^{3,1} | Peirce soldering product (OD3) | `52-observer-uniqueness` OD3 (rank 10 / rank 4 on π_u(V_0)) | CALC-02: the soldering-form metric (THE pairing) |
| `n(δ)=B(δ,δ)`, `det_2(n(δ)) = 0`, `x0 = ½‖δ‖²` | Coframe-dirs map to the forward light cone | verified this research | CALC-02 consistency: confirms soldering onto R^{3,1}, not a spurious metric |
| `Spin(9,1) ⊃ Spin(3,1) × Spin(6)`; `[B_i,B_j]=−ε_{ijk}J_k`, sig (3,3) | Lorentz × internal split; so(3,1) | Phase 48; `52-kkt-spacetime` §boosts | VALD-02: the forced SO(3,1) target |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Exact column rank over QQ | image dimension of π_u(V_{1/2}); rank of soldering map B | CALC-01, CALC-02 | `sympy.Matrix.rank()`; `exact_qq_rank` |
| Exact eigenvalues / signature count over QQ | Gram signature (foil + det_2 target) | CALC-02 | `sympy.Matrix.eigenvals()` |
| Peirce / Jordan product on h_3(O) | `δ∘δ'` into V_1⊕V_0; the soldering bilinear | CALC-02 | `ring_lemma`/`bulk_geometry` `jordan` |
| C_u entrywise projection | π_u | CALC-01/02 | `proj_u_exact`, `E()` |
| Infinitesimal-action nullspace over QQ | residual structure group; forced-vs-arbitrary | VALD-02 | `orbit_dimension_gate.infinitesimal_action`, `span_rank_over_QQ` |
| Generic-point sampling over Z | confirm generic rank (lower-semicontinuity) | CALC-01/02, VALD-02 | `orbit_dimension_gate` / `ring_lemma` point patterns |

### Approximation Schemes

**None.** This phase is exact linear algebra over Q. There is NO small parameter, NO truncation, NO approximation. Any "approximately 4d / approximately Lorentzian" is a forbidden proxy (`fp-relabel-approx-4d`). Float is permitted ONLY as pre-simplify triage, never as a decisive verdict (`fp-float-decisive`).

## Standard Approaches

### Approach 1: Reuse the Phase-46 π_u + the V_0 det_2/soldering benchmark (RECOMMENDED)

**What:** Apply the literal `proj_u_exact`/`E()` C_u map to a canonical V_{1/2} Peirce basis; take the image dimension by exact rank; read the Lorentzian signature off the soldering bilinear `B(δ,δ')=(δ∘δ')|_{V_0}` into R^{3,1} (det_2 signature on the target + rank-4 surjectivity); decide forced-vs-arbitrary via the residual-structure-group rank.

**Why standard:** This IS the validated V_0 mechanism (`52-kkt-spacetime`, `52-observer-uniqueness`), reused verbatim — the only legitimate way to avoid `fp-arbitrary-reduction` (using a different ad hoc reduction is a red flag for a smuggled choice). The soldering-form-metric reading is the standard Cartan-geometry tetrad construction (Sharpe 1997).

**Key steps:**
1. Build the 16 V_{1/2}(E_11) basis elements (engine idx 11..26) via `_standard_basis_27()`; build E_11 via `h3o_from_coords(1,0,0,0,0,0)`.
2. CALC-01: `M = [π_u(b_k)]` columns; `rank_M = M.rank()` over QQ. **Expect 4. KILL if ≠ 4.**
3. CALC-02 (foil, transparency): bare trace Gram `Tr(jordan(cof_i,cof_j))` → REPORT `diag(2,2,2,2)`, signature (4,0) = the Euclidean OP² metric. State explicitly this is NOT the verdict.
4. CALC-02 (verdict): soldering bilinear `B(δ,δ')=(δ∘δ')|_{V_0}` mapped to R^{3,1} coords; confirm `rank(B) = 4` (full, OD3 rank-4-on-π_u(V_0)); read det_2 signature on the target = **(1,3) Lorentzian**; confirm `n(δ)=B(δ,δ)` is null (`det_2≡0`) with `x0≥0` (forward cone). **KILL if the target is not Lorentzian (1,3), or B is not rank 4.**
5. VALD-02: residual structure group = nullspace over QQ of {fix E_11, commute with u=e_7, preserve π_u(V_{1/2})} in the Spin(9,1) Levi; show it contains so(3,1) (match the B_i=L_{σ_i} boosts, sig (3,3)) with NO extra free parameters; confirm the 4-space is the C_u-projector eigenspace (canonical, not chosen). **KILL = `fp-arbitrary-reduction` if SO(3,1) needs an arbitrary choice.**

**Known difficulties at each step:**
- Step 3/4: the temptation to read the verdict off the bare trace form (step 3) → Euclidean → false KILL. The plan MUST route the verdict through the soldering map (step 4). This is the single most important design point of the phase.
- Step 4: `det_2(δ∘δ) ≡ 0` (the diagonal is null) — do NOT mistake this identical-zero for "the pairing is degenerate / signature undefined". The signature is read on the R^{3,1} TARGET space (where det_2 = diag(+1,−1,−1,−1)), confirmed via the rank-4 image, not on the scalar `det_2(δ∘δ)`.
- Step 5: an arbitrary basis choice in V_{1/2} can masquerade as "extra structure". Anchor every count to (E_11, u) only; reproduce the calibration anchors (Stab_{E_6}(E_11)=61, Stab_{V_0}=45) BEFORE trusting any new stabilizer count (the Phase-0 gate; the v16.0 "naive 7 refuted by orbit method" cautionary precedent).

### Approach 2: Direct +i-eigenspace of the complex structure on V_{1/2} (FALLBACK / cross-check)

**What:** Treat u=e_7 as a genuine complex structure J (J²=−1) acting on each octonion entry; the C_u reduction is the projection onto the J-compatible subspace. Compute the image as the J-stable part.

**When to switch:** As an independent cross-check of CALC-01 (does the +i-eigenspace dimension agree with the `proj_u` rank?), or if `proj_u`'s entrywise definition is contested. Should give the same 4-dim image.

**Tradeoffs:** More conceptual but less directly tied to the validated V_0 engine; risks introducing a J-convention that is not literally the Phase-46 map (a `fp-arbitrary-reduction` foot-gun). Use only as confirmation, not as the load-bearing path.

### Anti-Patterns to Avoid

- **Reading the coframe signature off the bare trace form `Tr(δ∘δ')`.** Gives Euclidean (4,0) (the compact OP² metric) → a false "not Lorentzian" KILL. The verdict is the soldering det_2 on R^{3,1}. *Example:* computing `Gram_ij = Tr(jordan(cof_i,cof_j))` = `diag(2,2,2,2)` and reporting "Phase A KILL: signature (4,0)". WRONG — that Gram is the diagnostic foil.
- **Rescuing a non-Lorentzian Gram with a Wick rotation.** The rotation is the extra structure → `fp-arbitrary-reduction`. (v17.0 signature post-mortem: Wick rotation manufactures spurious structure.)
- **Selecting a 4-dim sub-piece "for the physical part" when the image is not 4.** The 4 must be EARNED by the exact rank, not chosen (`fp-arbitrary-reduction`). (Verified here: the image IS 4, so this should not arise — but the guard stays.)
- **Trusting a back-of-envelope residual-group dimension.** Run the rank (the v16.0 GATE surprise: naive "7" refuted by the orbit method).
- **Importing `octonion_algebra.py` or any float rank.** BANNED / `fp-float-decisive`.

## Existing Results to Leverage

**MANDATORY.** Results to CITE/REUSE, never re-derive.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| `T_E OP² = V_{1/2}(E)`, dim 16; OP² = F_4/Spin(9) | Borel 1950; Baez 2002 §3.4 | Phase 74 DERV-02 (verified: Zariski tangent of {X∘X=X} at E_11 == V_{1/2}, dim 16 = 17−1) | The soldering form `dE` is V_{1/2}-valued — the object being reduced |
| `E_11 ∘ δ = (1/2)δ` for all 16 V_{1/2} basis elts | exact over Q | Phase 74 DERV-02 (verified 16/16); McCrimmon | Defines V_{1/2}; do NOT recompute (cite Phase 74) |
| V_0 = h_2(O) → h_2(C_u) ≅ R^{3,1}, det_2 signature (1,3) | `det_2 = x0²−x1²−x2²−x3²` | `52-kkt-spacetime`, `52-observer-uniqueness` (verified, OD1–OD7) | The target-space signature benchmark; the SAME π_u; the (1,3) det_2 the coframe solders to |
| OD3: V_{1/2}×V_{1/2} → V_0 surjective, **rank 10 on V_0, rank 4 on π_u(V_0)** | — | `52-observer-uniqueness` OD3 | The soldering bilinear B is exactly this map; rank-4-on-π_u(V_0) is the CALC-02 surjectivity check |
| Boosts B_i = L_{σ_i} ∈ Str_0, `[B_i,B_j]=−ε_{ijk}J_k`, Killing sig (3,3) = so(3,1) | — | `52-kkt-spacetime` §boosts | The SO(3,1) generators VALD-02 must match as forced |
| Spin(9,1) ⊃ Spin(3,1) × Spin(6); Stab_{E_6}(E_11)=61, Stab_{V_0}=45=Spin(9,1), orbit(E_11)=17 | exact | Phase 48; Phase 74 VALD-01 (reproduced) | VALD-02 residual-group identification + calibration anchors |
| det SSOT: `det_3` CH-norm, 324/324 inner-derivation annihilation = dim f_4 = 52 | — | `ring_lemma_verification.py`; Phase 74 DERV-01 | The trace form `c(X,Y)=Tr(X∘Y)` and any det_2 come from this engine (correct association) |
| Compact OP² Fubini–Study metric = bare trace form on V_{1/2} = positive-definite | `diag(2,2,2,2)` on π_u(V_{1/2}) (verified this research) | Provost–Vallée (Re QGT = FS metric); SUMMARY.md "OP²-not-Kähler" | The diagnostic FOIL — explains WHY the verdict must be the soldering det_2, not the trace form |

**Key insight (why re-derivation is wasteful/dangerous):** The reduction dimension (4), the Peirce layout (V_{1/2}=idx 11..26), the (1,3) target signature, OD3 surjectivity, the so(3,1) boosts, and the calibration anchors are ALL already verified in-repo (Phases 46/48/52/74). Phase A's ONLY new content is: (i) running the SAME π_u on V_{1/2} and confirming dim 4 + the soldering signature (verified HIGH this research), and (ii) the residual-structure-group forced-vs-arbitrary verdict (the genuinely-open clause). Re-deriving the octonion arithmetic or det_2 invites the buggy-associator / convention-slip failures the SSOT guard exists to prevent.

### Useful Intermediate Results (verified during THIS research, exact over Q)

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| `dim π_u(V_{1/2}) = 4`, surviving coords {11,18,19,26} = C_u² | CALC-01 expected value, with the explicit basis | this research (`/tmp/q1_probe.py`) | E_11=diag(1,0,0), u=e_7 |
| Bare trace Gram = `diag(2,2,2,2)`, signature (4,0) | The Euclidean foil to REPORT | this research | the diagnostic, not the verdict |
| `det_2(δ∘δ) ≡ 0` (Brahmagupta–Fibonacci); `n(δ)` on the light cone, `x0=½‖δ‖²` | Coframe dirs map to forward light cone | this research (`/tmp/q1_probe2.py`, `q1_probe3.py`) | confirms soldering onto R^{3,1} |
| Soldering bilinear B surjects R^{3,1} (rank 4) | CALC-02 verdict realization | this research (`/tmp/q1_probe3.py`) | OD3 consistency (rank-4-on-π_u(V_0)) |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| "Differential Geometry: Cartan's Generalization of Klein's Erlangen Program" | Sharpe | 1997 | Rigorous soldering-form / Cartan-geometry definition (`g = e^* η`) | The definition that makes candidate (b) the canonical coframe pairing |
| "The Octonions" (math/0105155) | Baez | 2002 | OP² = F_4/Spin(9), T_E OP² = V_{1/2} | Cite for the tangent fact (already verified Phase 74) |
| A Taste of Jordan Algebras | McCrimmon | 2004 | Peirce decomposition, `E∘δ=(1/2)δ`, primitive idempotents | Cite for the Peirce identity |
| CMP 76 (1980) 289 | Provost & Vallée | 1980 | QGT real part = Fubini–Study metric | Explains the (4,0) trace-form foil = compact OP² FS metric |
| Freudenthal, Oktaven… | Freudenthal | 1954 | F_4 transitive on rank-1 idempotents; OP² | OD7 observer-independence (the reduction is E-independent up to F_4) |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (confirmed in env) | Exact `Matrix.rank()`, `.eigenvals()`, `.nullspace()` over QQ; `simplify`, `Poly` | The whole program runs exact over Q; DomainMatrix-over-QQ is the fast exact-rank path |
| `bulk_geometry_verification.py` | in-repo (warm) | `peirce_indices_under_E11`, `_standard_basis_27`, `_flat27`, `_coord_from_octmat`, `h3o_from_coords`, `jordan`, `octmat_*`, `oct_zero` | SSOT-consistent octonion/Jordan/Peirce primitives (verbatim det_3 deps) |
| `embedding_under_E_verification.py` | in-repo | `proj_u_exact(a, u_index=7)`, `E(X)`, `cu_to_complex`, `slice_to_complex` | The literal Phase-46 π_u / C_u map (reuse, do NOT reinvent) |
| `ring_lemma_verification.py` | in-repo (det SSOT) | `Tr`, `Tr2`, `c(X,Y)=Tr(X∘Y)`, `polarize_d`, `jordan`, `X_from_symbols`, exact-Q guards | The trace form + cubic norm with correct association |
| `orbit_dimension_gate.py` | in-repo | `infinitesimal_action`, `exact_qq_rank`, `span_rank_over_QQ`, f_4/e_6 machinery, calibration anchors | VALD-02 residual-structure-group rank; the forced-vs-arbitrary verdict |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| mpmath / NumPy 2.4.2 | float triage (which Gram entries are nonzero before simplify) | NEVER on a decisive verdict (`fp-float-decisive`); triage only |
| `cartan_phase0_tangent.py` | the driver/`_report`/`_run_engine` pattern + Phase-74 facts | Copy the harness skeleton; build on (do not redo) Phase 74 |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| Reuse `proj_u_exact` | A fresh "+i-eigenspace of J" projection | Cross-check only; a non-identical map risks `fp-arbitrary-reduction` |
| det_2-on-R^{3,1}-target signature | `slice_to_complex` + complex 2×2 determinant | Equivalent; the complex-matrix route is a nice cross-check of the Lorentzian form |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| `rank` / `eigenvals` of 4×4 and 27×N rational matrices | < 1 second | trivial | none needed |
| Soldering bilinear over 16-dim basis (symbolic) | seconds | octonion-product entry blow-up (mild) | rational basepoints; the matrices are small |
| Residual-structure-group nullspace (Spin(9,1) Levi, 45-dim, over QQ) | seconds–minutes | `infinitesimal_action` rank over QQ | reuse `orbit_dimension_gate` exact-rank path; reproduce anchors first |

**Note:** Phase A is the cheapest phase in the milestone — pure small-matrix linear algebra over Q. Unlike `orbit_dimension_gate.py` (the ~19-min v16.0 RING gate that exits nonzero BY DESIGN), the Phase-A computations are fast; do NOT pull in the slow pair-orbit RING anchors. If you reuse `orbit_dimension_gate` machinery, import only `infinitesimal_action`/`exact_qq_rank`/`span_rank_over_QQ`, do not run its `__main__`.

**Installation / Setup:** No new packages. Python 3.14.2 / SymPy 1.14.0 confirmed in env.
```bash
# Nothing to install; all engines are in-repo. Run the driver unbuffered:
python3 -u code/<phaseA_driver>.py
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| V_0 limit / OD3 surjectivity | the soldering map B is the SAME OD3 map | `rank(B onto R^{3,1}) == 4` (= rank-4-on-π_u(V_0)) | rank 4 (verified this research) |
| Null-cone consistency | coframe dirs solder to the light cone (not a spurious metric) | `det_2(B(δ,δ)) == 0` identically; `x0 = ½‖δ‖² ≥ 0` | `≡ 0`, forward (verified) |
| Trace-form foil | the Euclidean OP² metric is reported transparently | `Tr(jordan(cof_i,cof_j)) == diag(2,2,2,2)` | (4,0), explicitly NOT the verdict |
| Peirce layout regression | V_{1/2} = idx 11..26; π_u survivors {11,18,19,26} | re-run `peirce_indices_under_E11`; confirm survivors | matches Phase 74 |
| Calibration anchors (VALD-02) | the residual-group count is trustworthy | reproduce Stab_{E_6}(E_11)=61, Stab_{V_0}=45 before any new count | match (Phase 74 VALD-01) |
| Boost match (VALD-02) | SO(3,1) is the V_0 Lorentz group, not an abstract one | residual algebra ⊇ span{B_i, J_i}, Killing sig (3,3) | so(3,1) forced |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| V_0 reduction (the precedent) | apply π_u to V_0 instead of V_{1/2} | 10 → 4, det_2 (1,3) Lorentzian | `52-kkt-spacetime` (must reproduce as the soldering target) |
| u-choice independence | any u ∈ S^6 (G_2-conjugate) | same (1,3) | `52-observer-uniqueness` Step 5 |
| E-choice independence | E_22, E_33 (F_4-conjugate) | same structure | `52-observer-uniqueness` OD7 |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| All decisive numbers | exact over Q (sympy) | EXACT (zero tolerance) | dim=4; sig (1,3); rank(B)=4; foil (4,0) |
| Float triage (optional) | mpmath, pre-simplify only | not decisive | — |

### Red Flags During Computation

- Image dimension ≠ 4 (e.g. 6, 8, or 16) → genuine KILL clause (a). Do NOT pick a 4-dim sub-piece.
- Soldering bilinear B rank < 4 onto R^{3,1} → the coframe does not surject the spacetime → KILL (the soldering is degenerate).
- det_2 signature on the target ≠ (1,3) (e.g. (2,2) split, (4,0) Euclidean, or a degenerate (0,...)) → KILL clause (b). Do NOT Wick-rotate.
- The residual structure group has **extra free parameters** beyond so(3,1) tracing to a frame choice → `fp-arbitrary-reduction` KILL clause (c).
- Any nonzero octonion component 1..6 surviving π_u → the C_u projection is mis-implemented (it must keep only comps 0,7).
- `det_2(δ∘δ)` reported as a 4×4 Gram → CONCEPTUAL ERROR: that scalar is ≡0 (null cone); the signature is on the R^{3,1} target, read via rank-4 + det_2 there.

## Common Pitfalls

### Pitfall 1: Reading the verdict off the bare trace form (the Euclidean trap)
**What goes wrong:** `Tr(δ∘δ')` on π_u(V_{1/2}) = `diag(2,2,2,2)` = signature (4,0), triggering a false "Phase A KILL: not Lorentzian".
**Why it happens:** The trace form is the obvious "metric"; but OP² = F_4/Spin(9) is a compact Riemannian symmetric space — its invariant metric IS positive-definite. The Lorentzian structure is NOT intrinsic to V_{1/2}.
**How to avoid:** Route the signature verdict through the **soldering map** B(δ,δ') into V_0 = R^{3,1} and read det_2 on the TARGET (+ confirm rank-4 surjectivity). Report the (4,0) trace form transparently as the diagnostic foil.
**Warning signs:** A clean (4,0) or (2,2) on a 4×4 Gram built directly from `Tr(jordan(...))`.
**Recovery:** Switch to the soldering-bilinear-into-R^{3,1} reading (verified Lorentzian (1,3) + rank 4 this research).

### Pitfall 2: `fp-arbitrary-reduction` — a 4 (or an SO(3,1)) smuggled in by hand
**What goes wrong:** The 4-dim coframe or its Lorentz group is obtained by a choice not forced by (E_11, u): picking 4 of 16 directions, a non-canonical projection, a Wick rotation, or an arbitrary SO(3,1) frame.
**Why it happens:** "4-dim Lorentzian spacetime" is the hoped-for answer; the V_0 success tempts assuming V_{1/2} "obviously" parallels it.
**How to avoid:** Use the SAME `proj_u` map; compute the image dim by rank (not selection); show the 4-space is the C_u-projector eigenspace (canonical); compute the residual structure group as a nullspace over QQ anchored to (E_11, u) only; KILL if extra free parameters appear.
**Warning signs:** Any structural input beyond (E_11, u); a basis selection; an "extra idempotent"; a rotation invoked to make the Gram Lorentzian.
**Recovery:** Remove the choice; if the result requires it, that IS the KILL.

### Pitfall 3: Misreading `det_2(δ∘δ) ≡ 0` as a degenerate pairing
**What goes wrong:** Since `det_2(δ∘δ) ≡ 0` (the diagonal of the soldering bilinear is null), one might conclude "the induced metric is degenerate / undefined" and KILL.
**Why it happens:** Confusing the null cone (the image of the diagonal map) with the metric on the target space.
**How to avoid:** The signature is read on the R^{3,1} TARGET (det_2 = diag(+1,−1,−1,−1)), confirmed by the rank-4 surjectivity of B. `n(δ)` being null is CORRECT physics (coframe dirs map to the light cone, `x0 = ½‖δ‖² ≥ 0` forward) — it confirms the soldering, not a degeneracy.
**Warning signs:** A report of "signature (0,0,4) / all-zero Gram".
**Recovery:** Read det_2 on the target + rank-4 image.

### Pitfall 4: Arithmetic-hygiene / engine drift
**What goes wrong:** Importing `octonion_algebra.py` (buggy associator), using a float rank, or a det_3 cross-term slip.
**How to avoid:** Inherit the Phase-0 source guard (0 outside-fence `octonion_algebra` imports, 0 float-rank calls); reuse `ring_lemma`/`bulk_geometry` det_3 verbatim; `sympy.Matrix.rank()` only.
**Warning signs:** Any `import octonion_algebra`; any `numpy.linalg.matrix_rank` on a decisive path.
**Recovery:** STOP, diff against the warm commit; do NOT patch the cross-term.

## Level of Rigor

**Required for this phase:** Exact symbolic proof over Q (machine-verified). Every decisive number — image dimension, Gram signature, soldering-map rank, residual-group dimension — must be a rational/integer produced by `sympy` over QQ, never a float.

**Justification:** This is a binary KILL gate on a contract-critical claim (`claim-coframe-reduction`). A floating-point "approximately 4" or "approximately Lorentzian" is explicitly a forbidden proxy. The cost is trivial (small-matrix exact linear algebra), so there is no excuse for anything less than exact.

**What this means concretely:**
- CALC-01: `M.rank()` over QQ == 4 (integer). KILL if ≠ 4.
- CALC-02: signature counts from `Gram.eigenvals()` over QQ on the R^{3,1} target == (1,3); `rank(B) == 4`. KILL if not Lorentzian or B not full-rank. Report the (4,0) trace-form foil alongside.
- VALD-02: residual-group dimension from an exact nullspace over QQ; SO(3,1) (dim 6) contained with no extra free parameters; the 4-space is the C_u-projector eigenspace. KILL if not forced.
- NO truncation, NO approximation, NO float verdict, NO Wick rotation.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Read coframe signature off the bare trace form on V_{1/2} | Read it off the soldering map B into V_0 = R^{3,1} (det_2 + rank-4) | this research | Prevents a false (4,0) KILL; the verdict is the soldered Lorentzian metric (Sharpe) |
| Symmetric-sector cone-Hessian (v17.0, DEAD) | Antisymmetric/Lie-sector connection curvature (v18.0) | 2026-05-31 (v17.0 NONE) | v17.0 NONE does not bind this; Phase A is the first gate of the new route |

**Superseded approaches to avoid:**
- The v17.0 cone-Hessian (symmetric-sector, real-part QGT) Riemann tensor: do NOT reuse as load-bearing here — it is a different tensor and DEAD (Phase 73 NONE). Phase A is pure pre-curvature linear algebra; the curvature only enters Phase B.
- `peirce_coupling.py` (cited in the spec): does not exist; use `bulk_geometry`/`embedding` instead.

## Open Questions

1. **Is SO(3,1) FORCED by (E_11, u) alone (VALD-02 / clause c)?**
   - What we know: dim π_u(V_{1/2}) = 4 (verified); the soldering target is Lorentzian (1,3) (verified); the 4-space is the C_u-projector eigenspace (canonical by construction); the V_0 Uniqueness Theorem gives the analogous "forced" result for V_0.
   - What's unclear: whether the residual structure group computed as an exact nullspace over QQ contains so(3,1) with NO extra free parameters tracing to a frame choice. This is the genuinely-open part of the KILL gate.
   - Impact on this phase: this is the clause most likely to trigger a KILL (`fp-arbitrary-reduction`). It is the one computation the planner must scope as "MEASURE, do not assume".
   - Recommendation: compute the residual-group rank via `orbit_dimension_gate.infinitesimal_action`, anchored to (E_11, u); cross-check the dimension against Phase-48 so(3)×so(6) and the boosts B_i (sig (3,3)). Report the verdict flat either way.

2. **Does the soldering bilinear B's rank-4 image coincide with the V_0 = h_2(C_u) spacetime EXACTLY (not just dimensionally)?**
   - What we know: `rank(B onto R^{3,1}) = 4` (full); OD3 gives rank-4-on-π_u(V_0).
   - What's unclear: whether the image is literally π_u(V_0) = the validated spacetime (it should be, by OD3), or a different 4-space of the same signature.
   - Recommendation: confirm `image(B) == π_u(V_0)` by exact subspace equality (rank[image(B) | π_u(V_0)] == 4), the V_{1/2}-analog of Phase 74's `rank[ker | V_HALF_IDX]` identity check. Low risk, but it cements that the coframe solders to THE spacetime, not a look-alike.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| `proj_u_exact` C_u reduction | contested entrywise definition | +i-eigenspace of J=u (Approach 2) as cross-check | low (a few lines); confirmation only |
| Soldering det_2 on R^{3,1} target | the bilinear B is degenerate (rank < 4) | this is itself the KILL verdict — report it | none (it's the answer) |
| Residual-group nullspace over QQ | the count is untrustworthy | reproduce calibration anchors first (61/45), then recompute; run the rank, do not estimate | low–medium |

**Decision criteria:** There is no "pivot to a different physics" here — Phase A is a binary gate. If clause (a), (b), or (c) fails exactly over Q, the verdict is KILL ("Phase A: coframe reduction fails [clause]") and the milestone STOPS. Negative-result-is-success. The only legitimate "alternative" is a cross-check (Approach 2, or the image==π_u(V_0) identity), never a rescue of a failing clause.

## Sources

### Primary (HIGH confidence)
- `paper6-cartan-tetrad-prompt.md` — the authoritative milestone spec (Phase A KILL gate, clauses, forbidden proxies); BINDING.
- `derivations/52-kkt-spacetime.tex`, `52-observer-uniqueness.tex` — the V_0 → h_2(C_u) ≅ R^{3,1} precedent; det_2 (1,3); OD3 surjectivity (rank 4 on π_u(V_0)); SO(3,1) boosts; Uniqueness Theorem. In-repo, verified.
- `code/cartan_phase0_tangent.py` (Phase 74, verified) — Peirce layout, the warm-engine reuse pattern, `E∘δ=(1/2)δ` and `T_E OP²=V_{1/2}` (verified 16/16; tangent dim 16=17−1).
- `code/ring_lemma_verification.py`, `code/bulk_geometry_verification.py`, `code/embedding_under_E_verification.py`, `code/orbit_dimension_gate.py` — the SSOT det_3, Peirce/Jordan/octonion primitives, the C_u/π_u map, the stabilizer machinery. Inspected this research.
- `.gpd/research/{SUMMARY,METHODS,PITFALLS,COMPUTATIONAL}.md` (v18.0) — Method M4/M5, Pitfall 2, the OP²-not-Kähler subtlety, the engine inventory. Project-level research.
- R. W. Sharpe, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (1997) — the rigorous soldering-form / coframe metric definition (`g = e^* η`) grounding candidate (b).
- **Exact-over-Q spot computations performed during this research** (`/tmp/q1_probe*.py`, sympy 1.14.0): dim π_u(V_{1/2})=4 with survivors {11,18,19,26}; bare trace Gram `diag(2,2,2,2)` (4,0); `det_2(δ∘δ)≡0`; soldering B rank 4 onto R^{3,1}; `n(δ)` on the forward light cone. These directly validate CALC-01 and the CALC-02 recipe and resolve Q1/Q2.

### Secondary (MEDIUM confidence)
- Baez, "The Octonions", math/0105155 (2002) — OP² = F_4/Spin(9), T_E OP² = V_{1/2}.
- McCrimmon, *A Taste of Jordan Algebras* (2004) — Peirce decomposition, `E∘δ=(1/2)δ`.
- Provost & Vallée, CMP 76 (1980) 289 — QGT real part = Fubini–Study; explains the (4,0) trace-form foil = compact OP² FS metric.
- D. K. Wise, gr-qc/0611154 — Cartan/MM (for the downstream Phase B; here only as context for why the coframe matters).

### Tertiary (LOW confidence)
- Web searches (June 2026) for Berry curvature of the OP² idempotent family and MM-from-h_3(O): returned only adjacent/generic results (Singh arXiv:2304.01213; Smith hep-th/9302030 propose h_3(O)/HJTS frameworks but compute no C_u coframe reduction). Confirms the **novelty** below; no result to cite as a benchmark for the V_{1/2} reduction itself.

## Novelty Note (Q5 — LIGHT survey)

Targeted searches (Provost–Vallée QGT literature; MM/Cartan from exceptional Jordan algebras; Peirce V_{1/2}→4d Lorentzian reduction) found:
- The QGT/Berry literature is **generic** (no Cayley-plane / OP² primitive-idempotent computation).
- MM-from-h_3(O) exists in **adjacent, action-positing** form (Wise's clean Cartan statement; Singh's E_6/h_3(O) "new U(1) gravity"; Smith's HJTS SM+gravity), but **nobody has computed the C_u reduction of V_{1/2} to a 4-dim coframe**, nor the Berry curvature of the OP² = F_4/Spin(9) idempotent family.
- The **specific Phase-A object** — π_u : V_{1/2}(16) → 4-dim soldered Lorentzian coframe, forced by (E_11, u) — is **unattested**. This is genuine novel territory (consistent with SUMMARY.md's "candidate-novel" finding for the coframe `e=dE`).

Per the brief, this is a KILL gate, not the paper — the novelty is noted, not over-invested. The validation anchors are the V_0 precedent (limit), the det_2 (1,3) benchmark, and OD3 surjectivity, all in-repo and verified.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that the soldering bilinear B = (δ∘δ')|_{V_0} is THE canonical coframe pairing and not merely *one* defensible choice. *Defense:* it is the unique map (OD3, the Peirce product) carrying V_{1/2} to the validated R^{3,1}; the trace form (a) is provably the compact OP² FS metric (wrong signature class); (d) reduces to (a) on π_u(V_{1/2}). I report BOTH (a) (foil) and (b)/(c) (verdict) so the planner/verifier can see the reasoning, not just the conclusion. Residual risk: a reviewer could argue the coframe metric should be defined intrinsically on V_{1/2} — but that is impossible for a compact Riemannian OP², which is exactly why the soldering reading is forced. This is the single most important judgment call in the phase; it is made explicit and is falsifiable (if the verifier finds a defensible intrinsic Lorentzian form on V_{1/2}, the framing must be revisited — I judge this very unlikely given OP²'s Riemannian symmetric structure).
2. **Alternative dismissed (the +i-eigenspace of J):** kept as a cross-check (Approach 2), not load-bearing, to avoid introducing a non-Phase-46 projection convention (`fp-arbitrary-reduction` risk). Defensible to elevate it only if `proj_u` is contested.
3. **Understated limitation:** clause (c) [forced SO(3,1)] is MEDIUM confidence — I have argued it is plausible (C_u-projector eigenspace + V_0 Uniqueness analogy) but NOT computed the residual-group rank in this research (it needs the slow-ish Spin(9,1)-Levi nullspace). The planner must scope VALD-02 as a genuine measurement with a real KILL possibility, not a formality.
4. **Simpler method overlooked?** No — Phase A is already the cheapest possible test (small-matrix exact linear algebra). The risk is the opposite: over-engineering (pulling in curvature or the slow RING gate). The plan should stay minimal and fast.
5. **Would a specialist disagree?** A Jordan-algebra geometer might note that "the coframe pairing" could also be phrased via the Freudenthal cross/quartic — but for the 4-dim π_u-image the relevant object is the quadratic det_2 on the soldered R^{3,1} target, which is unambiguous and validated. A Cartan-geometry specialist would endorse the soldering-form-metric (`g=e^*η`) reading (Sharpe). I am confident the soldering reading is correct; the genuine uncertainty is the clause-(c) outcome, flagged as such.

## Metadata

**Confidence breakdown:**
- Mathematical framework (C_u reduction, the induced pairing decision): **HIGH** — dim=4, the Euclidean trace-form foil, the soldering-bilinear Lorentzian (1,3) + rank-4 surjectivity, and the null-cone map were all verified exact over Q during this research; the soldering-form-metric reading is the standard Cartan definition (Sharpe).
- Standard approaches (reuse the Phase-46 π_u + V_0 benchmark): **HIGH** — the literal validated engine path.
- Computational tools (engine reuse inventory): **HIGH** — every function signature was inspected in-repo this research.
- Validation strategies (limits, OD3, anchors): **HIGH** for the V_0 limit / det_2 / OD3; the forced-vs-arbitrary clause (c) outcome is **MEDIUM** (designed to be measured).

**Research date:** 2026-06-01
**Valid until:** Indefinite for the mathematics (exact, stable). Engine function names are stable (Phase 74 warm). Re-verify only if the SSOT engines are refactored.

## RESEARCH COMPLETE

**Phase:** 75 - Phase A — Coframe-Reduction Dealbreaker (THE KILL GATE)
**Confidence:** HIGH (clauses a, b + framework); MEDIUM (clause c outcome, by design)

### Key Findings
- **CALC-01 verified exact over Q: dim π_u(V_{1/2}) = 4** (survivors {11,18,19,26} = C_u² = the C_u components of the (1,3)=x2 and (1,2)=x3 octonion entries). Parallels V_0 (Q2 resolved).
- **Q1 (the crux) RESOLVED:** the bare trace form `Tr(δ∘δ')` on π_u(V_{1/2}) is **Euclidean (4,0)** = the compact OP²=F_4/Spin(9) Fubini–Study metric, NOT the coframe signature. The **canonical pairing is the soldering-form metric (candidate b)**, realized exact over Q via the **Peirce soldering bilinear** B(δ,δ')=(δ∘δ')|_{V_0} into R^{3,1}: B **surjects (rank 4)**, det_2 on the target is **Lorentzian (1,3)**, and the diagonal lands on the **forward light cone** (`det_2(δ∘δ)≡0`, `x0=½‖δ‖²`). CALC-02 must read the verdict there, REPORTING the (4,0) trace-form as the diagnostic foil.
- **VALD-02 method fixed (outcome MEDIUM, to MEASURE):** residual structure group = exact nullspace over QQ of {fix E_11, commute with u, preserve π_u(V_{1/2})} in the Spin(9,1) Levi; SO(3,1) forced iff it contains so(3,1) (match boosts B_i, sig (3,3)) with no extra free parameters; the 4-space is the C_u-projector eigenspace (canonical). This is the clause most likely to KILL (`fp-arbitrary-reduction`).
- **Engine reuse inventory (Q4) complete:** import `bulk_geometry_verification` (`peirce_indices_under_E11`, `_standard_basis_27`, `_flat27`, `_coord_from_octmat`, `jordan`, `h3o_from_coords`, `octmat_*`, `oct_zero`), `embedding_under_E_verification` (`proj_u_exact`, `E`, `slice_to_complex`), `ring_lemma_verification` (`Tr`, `jordan`, `X_from_symbols`, `det_3`), `orbit_dimension_gate` (`infinitesimal_action`, `exact_qq_rank`, `span_rank_over_QQ`). `octonion_algebra.py` BANNED; `peirce_coupling.py` ABSENT (use the above). Do NOT rebuild octonion arithmetic; do NOT run the slow `orbit_dimension_gate` `__main__`.
- **Novelty (Q5):** the π_u : V_{1/2}→4d soldered Lorentzian coframe is unattested in the literature (QGT/MM-from-h_3(O) work is generic or action-positing); noted, not over-invested (this is the KILL gate, not the paper).

### File Created
`.gpd/phases/75-phase-a-coframe-reduction-dealbreaker-the-kill-gate/75-RESEARCH.md`

### Confidence Assessment
| Area | Level | Reason |
| ---- | ----- | ------ |
| Mathematical Framework | HIGH | dim=4, the pairing decision, Lorentzian (1,3) + rank-4, and the null cone all verified exact over Q this research |
| Standard Approaches | HIGH | the literal validated Phase-46 π_u + V_0 benchmark |
| Computational Tools | HIGH | every engine function inspected in-repo |
| Validation Strategies | HIGH (V_0 limit/OD3/anchors); MEDIUM (clause-c outcome) | clause (c) is the designed-open KILL clause |

### Open Questions
- Clause (c): is SO(3,1) FORCED by (E_11,u) alone? Residual-group rank over QQ must be computed (MEASURE; real KILL possibility).
- Does image(B) == π_u(V_0) exactly (not just dimensionally)? Recommend a subspace-equality identity check (the V_{1/2}-analog of Phase 74's `rank[ker | V_HALF_IDX]`).

### Convention Choices Made
- Inherited the v18.0 lock verbatim (det SSOT = ring_lemma det_3; u=e_7; E_11=diag(1,0,0); Peirce V_{1/2}=idx 11..26; mostly-minus (+,−,−,−); det_2=x0²−x1²−x2²−x3²; EXACT over Q).
- DECIDED the induced coframe pairing = soldering-form metric (candidate b) via the Peirce soldering bilinear into R^{3,1} (candidate c realization); the bare trace form (candidate a) is the diagnostic foil, never the verdict. Documented with exact-over-Q evidence and a both-readings cross-check.

### Ready for Planning
Research complete. The planner can write a tight, single-plan executable Phase A: three checks (CALC-01 dim, CALC-02 soldering signature + foil, VALD-02 forced-vs-arbitrary), each exact over Q, each with an explicit KILL condition, reusing the named warm engines. No new packages, no curvature, no slow gates.
