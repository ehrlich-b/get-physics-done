# Phase 73: C — Einstein Structure - Research

**Researched:** 2026-06-01
**Domain:** Linearized/quadratic-order general relativity on a flat KKT-Minkowski background, coupled to an independently-built stress-energy tensor from octonionic cross-term ("matter") content of the h_3(O) (Albert algebra) cubic norm. The decisive object is the matter-sourced curvature of the spacetime slice metric g = eta + h(x; M), at QUADRATIC order in ||M|| (since h^(1)=0). This is the FINAL phase of milestone v17.0; it is a can-fail Einstein-structure test, NOT a confirmation exercise.
**Confidence:** HIGH on the linearized-GR formalism, the engine extensibility, and the order bookkeeping (all transcribed and/or directly computed below); HIGH on the circularity-audit method; MEDIUM on the T_mu_nu construction (novel, several defensible routes — the genuine open design choice); MEDIUM on the OUTCOME (the honest prior is "curved but not Einstein-structured" — see Summary).

> ## SELF-CONTAINED NOTICE (executor has NO web/arxiv)
> Per [[feedback_executor_no_web_stage_literature]], the downstream gpd-executor has no web tools. Every formula, sign convention, and literature result the execution needs is transcribed verbatim below (linearized Ricci/Einstein operator, trace-reverse, Lorenz gauge, the d=5 very-special-geometry metric, the scalar/sigma-model stress tensor, the Jacobson route to contrast). Cite the in-repo engine and these transcribed equations; do NOT expect to look anything up.

## Summary

Phase 72 established (human-ratified, SURVIVES-qualified) that matter `M` in V_{1/2} cross-term-sources the curvature of the flat KKT spacetime slice `g = eta + h(x;M)`, and emitted two facts that completely determine the shape of Phase 73: (1) **`h^(1)_mu_nu = 0` identically** — the linear-in-M metric response vanishes, so the leading response is the QUADRATIC `h^(2)_mu_nu`; and (2) **`R[g] = a_4 ||M||^4 + O(||M||^5)`** with `a_4 = 395268903/24010000` — the scalar curvature first appears at FOURTH order in ||M||. Phase 73 must test, at the honest level (exact / linear-in-the-leading-response / none), whether `G_mu_nu[g(x)] = kappa T_mu_nu + Lambda g_mu_nu` for a `T_mu_nu` built INDEPENDENTLY from the V_{1/2} cross-term content, with `kappa` a GLOBAL constant over an (M,x) family and `Lambda = 0` (the M=0 vacuum is flat, DERIVED from KKT det_2 — there is NO Lambda tripwire).

**The single most important finding (order bookkeeping — I computed this directly, exact over Q).** The Phase-72 handoff instruction "form `h̄^(2) = h^(2) - (1/2) eta tr(h^(2))` and test `□h̄^(2) ~ kappa T`" is a USEFUL POINTER but is **NOT the gauge-invariant test by itself**. Direct computation on the emitted `h^(2)(x)` field shows:
- `□h̄^(2)_mu_nu != 0` at the center (e.g. `(0,0)`-entry `= -76221/2450`), BUT
- the **linearized Einstein tensor `G^(1)_mu_nu[h^(2)] = 0` IDENTICALLY** at the center, and the **linearized Ricci scalar `R^(1)[h^(2)] = 0`**, AND
- `h^(2)` is **NOT in Lorenz gauge** (defect `∂^mu h̄^(2)_mu_nu = [19143/9800, 9747/4900, 297/350, 0] != 0`).

The reconciliation: `□h̄_mu_nu = -2 G^(1)_mu_nu` holds ONLY in Lorenz gauge; `h^(2)` is not in Lorenz gauge, so the nonzero `□h̄^(2)` is **pure gauge** (it equals the gauge terms `∂_mu(∂^a h̄_anu)+∂_nu(∂^a h̄_amu)` that Lorenz gauge would kill), and the gauge-invariant linearized Einstein content `G^(1)[h^(2)]` is exactly zero. This is **fully consistent** with `R = O(||M||^4)`: the O(||M||^2) piece of the curvature — which is precisely the linear-in-`h^(2)` Einstein tensor — vanishes. **The genuine curvature lives at O(||M||^4), which is SECOND order in `h^(2)` (the Totaro `C·C` structure: Riemann is bilinear in the cubic form C, and C is O(||M||^2)).** I confirmed the FULL nonlinear Einstein tensor `G_mu_nu[g] != 0` at the decisive M_0 (e.g. `(3,3)`-entry a large nonzero rational), and that `g` is NOT an Einstein space there (`S_mu_nu = Ric - (R/4)g != 0`).

**Primary recommendation (the well-posed can-fail test).** Test `G_mu_nu[g(x)] = kappa T_mu_nu + Lambda g_mu_nu` using the **FULL nonlinear Einstein tensor** `G_mu_nu[g] = Ric_mu_nu[g] - (1/2) g_mu_nu R[g]` (which the warm engine already computes via Totaro, ~2s at a rational M_0), evaluated at the leading curvature order O(||M||^4), against a `T_mu_nu` built independently from the V_{1/2} cross-term scalar `2Re((x2 x1)x3)` (the canonical/sigma-model scalar stress tensor is the most defensible construction — see Area 2). Fit `kappa` and `Lambda` as GLOBAL constants over an (M,x) family. Report the honest level. Use `□h̄^(2)` ONLY as a documented secondary/gauge diagnostic, after first gauge-fixing to Lorenz (or reporting that the algebra-derived `h^(2)` is not naturally in Lorenz gauge). The honest prior — given that `g` is already known to carry nonzero Weyl and traceless-Ricci at finite M — is **"curved but not Einstein-structured"**; build the test to be able to REPORT that cleanly, do NOT force Einstein form.

## User Constraints

No CONTEXT.md exists for this phase (no `/gpd:discuss-phase` was run). The binding context is: the **ROADMAP Phase-73 re-scope** (`.gpd/ROADMAP.md`, 2026-05-31, quadratic-response linearized-Einstein can-fail test), the **Phase-72 handoff** (`.gpd/phases/72-b-matter-sourcing/72-02-SUMMARY.md`, human-ratified), the **v17.0 project contract** (`claim-einstein-structure`, `deliv-phaseC`, `test-einstein-level`, `fp-import-supergravity`, `fp-assume-einstein`, `fp-ensemble-gravity`), the **authoritative spec** (`paper6-bulk-geometry-prompt.md`), and the **LOCKED v17.0 conventions** (`.gpd/CONVENTIONS.md`). Treat all of these as locked decisions:

- **The physical spacetime metric is `g = eta + h(x;M)`** (Phase-70.1, human-ratified). `eta` = flat KKT Minkowski (`det_2`, mostly-minus, timelike `x_0 = beta+gamma`); the cone-Hessian is the matter SOURCE, NOT the metric. Do NOT re-open this.
- **The test is the QUADRATIC-response (O(||M||^2) / leading-`h^(2)`) Einstein test, NOT linear-in-M** — because `h^(1) = 0` makes the linear test degenerate (Phase-72 handoff). The "linear-in-M" criterion in the ROADMAP/contract means **linear in the leading quadratic building block** (i.e. leading order in `h^(2)` / first nonvanishing curvature order O(||M||^4)) — see the Order-Counting section, which I resolved by direct computation.
- **`Lambda = 0`. NO Lambda tripwire.** The M=0 vacuum is flat eta, DERIVED from KKT det_2 (NOT inserted, NOT Einstein-negative). The pre-70.1 "fit Lambda nonzero / center is Einstein" instruction is SUPERSEDED (CONVENTIONS.md §6, ROADMAP VALD-04). A residual `Lambda*g` term may be FIT as a global constant in the test (and is expected to be 0), but it is never a circularity tripwire.
- **`T_mu_nu` and `kappa` MUST be defined BEFORE `G_mu_nu` is computed, and INDEPENDENTLY of any assumed Einstein form** (DERV-03). No supergravity multiplet data, no GST Lagrangian, no N=2 SUSY closure, no `-R/2` coefficient fixed by SUSY, no Weinberg soft-graviton theorem as a load-bearing input (`fp-import-supergravity`). SUBTLE TRAP: the slice geometry genuinely COINCIDES with GST very-special-real geometry (both are `Hess(-log N)` of the same cubic norm), so importing GST is easy to do by accident — cite GST for the manifold/orientation ONLY (Area 6).
- **No per-point tuning of `kappa, Lambda`** (`fp-assume-einstein`). They are GLOBAL constants over the (M,x) family; a single-point match is rejected as a tuned-point overclaim. Linear-in-leading-response agreement is reported as the weaker level it is.
- **No observers-make-gravity / Jacobson-style ensemble/thermodynamic argument** (`fp-ensemble-gravity`). The curvature and the stress tensor come from the algebra's own cubic-norm geometry, one observer, one off-center point.
- **EXACT over Q on all decisive verdicts.** Signatures via `eig_signature_count` (real_roots), ranks via `sympy.Matrix.rank()`, never numpy float (`fp-float-decisive`).
- **Backtracking trigger (honest negative is ACCEPTABLE, do NOT force):** if no Einstein structure holds at exact or leading-response order, report "curved but not Einstein-structured" — an acceptable FULL result. If the ONLY way to reach `G = kappa T + Lambda g` is to import GST/SUSY/-R/2/Weinberg, STOP and report the honest non-Einstein level instead (that import IS the circularity the milestone exists to avoid).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `.gpd/phases/72-b-matter-sourcing/72-02-SUMMARY.md` (Phase-72 handoff) | prior artifact (AUTHORITATIVE) | Emits `h^(1)=0`, the `h^(2)` matrix, `a_4`, the decisive M_0, and the explicit `□h̄~kappaT` instruction. The whole phase is built on this. | READ IN FULL before planning | plan, execution, verification |
| `paper6-bulk-geometry-prompt.md` (ref-prompt) | authoritative milestone spec | Defines Phase C target: candidate `T_mu_nu` from V_1/V_{1/2}, test `G = kappa T + Lambda g` at exact/linear/none, "curved but not Einstein-structured is acceptable, do NOT force." Reporting discipline is binding. | READ IN FULL before planning | plan, execution, verification |
| `code/bulk_geometry_verification.py` (warm engine, ALL_PASS exit 0) | prior artifact (EXTEND) | The decisive surface. `spacetime_curvature_of_g` (full nonlinear `Ric[g]`, `R[g]`), `cone_hessian_offcenter(slice_symbolic=True)` (the `h^(2)(x)` FIELD), `_eta_minkowski`/`_frame_jacobian_bg_to_mink` (constant eta), `ricci_decomposition_n4` (S, Weyl), `det_3`/`det_3_block` (cross-term + off-switch), `eig_signature_count`, `hand_rolled_riemann_of_g` (cross-check). Phase 73 EXTENDS this with: the `h^(2)(x)` field, `□`, the linearized `G^(1)`, the FULL nonlinear `G_mu_nu`, the `T_mu_nu` builder, and the (M,x)-family fit. Do NOT rebuild; do NOT import `octonion_algebra.py`. | EXTEND in place; reuse `det_3` SSOT | execution, verification |
| `.gpd/phases/72-b-matter-sourcing/72-02-decisive-controls.py` (Phase-72 driver, lines ~264-296) | prior artifact (TEMPLATE) | Shows exactly how `h^(2)` was computed (symbolic in slice AND t, then t^2-coefficient). Phase 73 takes the SAME `h_sym_t` but does NOT substitute the center → `h^(2)(x)` as a field. Reuse this construction verbatim. | READ; reuse the field-extraction pattern | execution |
| `derivations/72-matter-sourcing.tex` (Phase-72 write-up) | prior artifact | The off-switch, ||M||->0 limit, h^(2), and conventions in LaTeX. Phase 73's `derivations/73-einstein-structure.tex` builds on it. | READ for conventions + continuity | plan, execution |
| `derivations/52-kkt-spacetime.tex` (ref-52-kkt) | foundational | The `h_2(C_u) ~ R^{3,1}` Minkowski background, the frame map `x0=(beta+gamma)/2, x1=p, x2=q, x3=(beta-gamma)/2`, timelike `x_0`. Grounds eta and the box operator. | CITE for eta and the frame | plan, verification |
| `code/ring_lemma_verification.py` (ref-warm-engine) | foundational | The det_3 SSOT (byte-identical to the engine's). Provenance of the cubic norm. | CITE; do not re-derive det_3 | verification |
| Gunaydin-Sierra-Townsend 1983-84 (ref-gst) | literature (CITE-FOR-GEOMETRY-ONLY / AVOID-LAGRANGIAN) | The slice IS very-special-real geometry `E_{6(-26)}/F_4` (`a_IJ = -(1/3)∂_I∂_J ln N`). Cite to ORIENT (acknowledge the coincidence); NEVER adopt their Lagrangian / SUSY-fixed couplings (`fp-import-supergravity`). | CITE geometry; AVOID Lagrangian | plan (Area 6), circularity audit |
| Jacobson 1995 (ref-jacobson-contrast) | literature (CONTRAST-ONLY / AVOID) | The rejected thermodynamic/ensemble route (entropy ∝ area, δQ=TdS at local Rindler horizons). Name it to CONTRAST and explicitly reject (`fp-ensemble-gravity`). | CITE to contrast; AVOID as method | plan (Area 6), circularity audit |

**Missing or weak anchors:**

- **No external literature for the CLAIM (an intrinsic algebraic `T_mu_nu` from octonion cross-terms tested against a bulk-induced `G_mu_nu`).** This is novel. The `T_mu_nu` construction (Area 2) has no off-the-shelf template; the closest is the canonical scalar/sigma-model stress tensor (transcribed below). Validation is INTERNAL (symmetry, conservation `∂^mu T_mu_nu=0`, the `||M||->0` limit, the global-constant test across the family), not literature-benchmarked. Outcome confidence is MEDIUM, and the honest prior is a NEGATIVE (non-Einstein) result.
- **The handoff `□h̄^(2)~kappaT` is under-specified as stated.** I resolved (by direct computation) that it is gauge-dependent and that the gauge-invariant linearized Einstein content vanishes; the well-posed test is the full nonlinear `G[g]` at O(||M||^4). The planner MUST adopt the full-`G` test as primary and demote `□h̄^(2)` to a gauge diagnostic. This is the most important plan-shaping correction.
- **Notation aliasing to flag (non-blocking).** CONVENTIONS.md §0/§3 write the cross-term as `2Re(x2* x0* x1)` and slice indices as `{17,18,19,26}`; the engine SSOT writes `2Re((x2 x1)x3)` and slice indices `{1,2,3,10}` (= beta,gamma,p,q). These are the SAME objects under the McCrimmon-vs-matrix-layout relabeling; the **engine indices and `det_3` are authoritative** for Phase 73 (byte-identical SSOT, Phase-72-verified). A notation-coordinator follow-up is pending (non-blocking).

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Physical spacetime metric | `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)`; leading response is `h^(2)` (since `h^(1)=0`) | cone-Hessian-is-metric [FALSIFIED, Phase 70.1] | Phase 70.1; CONVENTIONS §1 |
| Metric signature | **mostly-minus (+,-,-,-)** Lorentzian; `eta_M = diag(+1,-1,-1,-1)` in Minkowski coords | mostly-plus (-,+,+,+) [Wikipedia/MTW use this — SIGN FLIP, see below] | CONVENTIONS §1; 52-kkt |
| eta in the engine (beta,gamma,p,q) frame | `eta_bg = J^T eta_M J` = `[[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]` (CONSTANT, null-aligned); `eta_bg^{-1} = [[0,2,0,0],[2,0,0,0],[0,0,-1,0],[0,0,0,-1]]` | diag form (only in Minkowski coords) | engine `_eta_minkowski`/`_frame_jacobian_bg_to_mink`; computed below |
| Frame map (beta,gamma,p,q)->(x0,x1,x2,x3) | `x0=(beta+gamma)/2, x1=p, x2=q, x3=(beta-gamma)/2`; det J = -1/2 | — | 52-kkt; engine `_frame_jacobian_bg_to_mink` |
| d'Alembertian (box) | `□ = eta^{ab} ∂_a ∂_b`; in (beta,gamma,p,q): `□ = 2·2·∂_beta∂_gamma - ∂_p^2 - ∂_q^2` = `4∂_beta∂_gamma - ∂_p^2 - ∂_q^2` (since `eta_bg^{-1}_{betagamma}=2`, counted twice) | — | computed below (eta_bg^{-1}) |
| det / cubic norm | Freudenthal `det_3`, cross-term `2Re((x2 x1)x3)`; SSOT = engine `det_3` | `(x1 x2)x3` [BANNED, buggy]; `2Re(x2* x0* x1)` [= same, McCrimmon relabel] | CONVENTIONS §0; engine |
| Riemann (lower idx) | `R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq)`, C from the DIFFERENCE potential `Phi_{bg+M}-Phi_{bg}`; indices raised with `g^{-1}=(eta+h)^{-1}`, NOT `H_bg^{-1}` | — | Totaro Cor 2.3; engine §13 |
| Ricci / scalar | `Ric_jl = g^{ik}R_ijkl`; `R = g^{jl}Ric_jl` | — | engine `ricci_scalar` |
| Full nonlinear Einstein tensor | `G_mu_nu[g] = Ric_mu_nu[g] - (1/2) g_mu_nu R[g]` (lower index) | — | standard; the well-posed test LHS |
| M=0 spacetime curvature | `R = S = Weyl = 0` (flat eta), DERIVED from KKT det_2 — NOT R=-3, NOT pure-Lambda | R=-3/Cartan [SUPERSEDED: that is the cone-Hessian SOURCE] | Phase 70.1; 72 verdict |
| Lambda | `Lambda = 0` (vacuum flat, DERIVED). May be FIT as a global constant (expected 0); NEVER a tripwire | "center Einstein, Lambda<0" [FALSIFIED] | Phase 70.1; CONVENTIONS §6 |
| Units | natural ħ=c=k_B=1; EXACT over Q; dimensionless differential geometry | float [FORBIDDEN on verdicts] | CONVENTIONS §2 |
| Peirce (under E_11=diag(1,0,0)) | V_1(1)={0} alpha (INERT); V_0(10)={1..10}; V_{1/2}(16)={11..26} (the matter channel). Slice = {1,2,3,10}=(beta,gamma,p,q). x1=X[2][1] (V_0 oct), x2=X[0][2], x3=X[1][0] (V_{1/2} oct) | indices {17,18,19,26} [CONVENTIONS relabel] | engine §11 |

**CRITICAL — SIGN/SIGNATURE FLIP vs the textbook formulas below.** All the standard linearized-GR references I transcribe (Wikipedia, MTW, Wald, Carroll) use **mostly-plus (-,+,+,+)**. This project is **mostly-minus (+,-,-,-)**. The linearized Ricci tensor `R^(1)_mu_nu` (the formula with `∂∂h` terms and `□h`) is the SAME algebraic expression in both signatures (it is built from the connection, which is signature-form-invariant). What flips is: (a) the trace `h = eta^{mu nu}h_mu_nu` picks up the signature through `eta^{-1}`; (b) the overall sign of `□` and of the source coefficient. The SAFE procedure (which I used in the computations below and which I recommend the executor follow): **build everything from the engine's explicit `eta_bg` and `eta_bg^{-1}` (mostly-minus, the matrices above) — never hard-code a `diag(-1,1,1,1)` — and pin the sign of the source coefficient `kappa` by the FIT, not by importing the textbook `-16πG` or `-2κ` value (which would be `fp-import-supergravity`-adjacent and signature-dependent).** The textbook `□h̄ = -2κ_Einstein T` is transcribed for STRUCTURE (which terms, which contraction), not for its numeric coefficient.

Convention loading: see agent-infrastructure.md Convention Loading Protocol. Run `gpd --raw convention check` (note §6 Lambda<0 is FALSIFIED/superseded — non-blocking; Lambda=0).

## Mathematical Framework

### Key Equations and Starting Points (TRANSCRIBED — self-contained)

#### (A) Linearized gravity on flat eta (mostly-PLUS textbook form; READ THE SIGN NOTE above)

Source: Wikipedia "Linearized gravity" (MTW (-,+,+,+) convention), cross-checked against MTW Ch. 18 and Carroll Ch. 7. Transcribed verbatim, then adapted to mostly-minus via the engine eta.

- **Trace-reversed perturbation:** `h̄_mu_nu = h_mu_nu - (1/2) eta_mu_nu h`, where `h = eta^{mu nu} h_mu_nu` (the trace). Inverse relation (n=4): `h_mu_nu = h̄_mu_nu - (1/2) eta_mu_nu h̄`, with `h̄ = eta^{mu nu}h̄_mu_nu = -h`.

- **Linearized Ricci tensor (gauge-general):**
  ```
  R^(1)_mu_nu = (1/2) ( ∂_s ∂_mu h^s_nu + ∂_s ∂_nu h^s_mu - ∂_mu ∂_nu h - □ h_mu_nu )
  ```
  where `h^s_nu = eta^{s a} h_a_nu`, `□ = eta^{ab}∂_a∂_b`. (Equivalently `R^(1)_mu_nu = (1/2)(∂^s∂_mu h_snu + ∂^s∂_nu h_smu - ∂_mu∂_nu h - □h_mu_nu)`.)

- **Linearized Ricci scalar:** `R^(1) = eta^{mu nu}R^(1)_mu_nu = ∂_a∂_b h^{ab} - □h`.

- **Linearized Einstein tensor:** `G^(1)_mu_nu = R^(1)_mu_nu - (1/2) eta_mu_nu R^(1)`. In trace-reversed variables it is `G^(1)_mu_nu = -(1/2)( □h̄_mu_nu + eta_mu_nu ∂_a∂_b h̄^{ab} - ∂_mu∂_a h̄^a_nu - ∂_nu∂_a h̄^a_mu )`.

- **Lorenz / harmonic / de Donder gauge condition:** `∂^mu h̄_mu_nu = 0` (equivalently `∂_mu h^mu_nu = (1/2)∂_nu h`).

- **Reduced field equation IN Lorenz gauge:**
  ```
  □ h̄_mu_nu = -2 kappa_Einstein T_mu_nu          (Wikipedia form; kappa_Einstein = 8πG)
            = -16 π G T_mu_nu                     (MTW/Wald form, G geometrized)
  ```
  Equivalently `G^(1)_mu_nu = -(1/2) □h̄_mu_nu` IN Lorenz gauge.

**CRITICAL caveat I verified (the heart of the order-counting):** `□h̄_mu_nu = -2 G^(1)_mu_nu` holds ONLY when Lorenz gauge `∂^mu h̄_mu_nu = 0` is imposed. The Phase-72 `h^(2)` is **NOT in Lorenz gauge** (I computed the defect `∂^mu h̄^(2)_mu_nu = [19143/9800, 9747/4900, 297/350, 0] != 0` at the center). So `□h̄^(2)` is NOT `-2 G^(1)[h^(2)]`; the difference is the gauge terms. See Order-Counting below.

#### (B) The h^(2)(x) FIELD and the box operator (computed, exact over Q)

The emitted `h^(2)` is a single matrix at the center, but `□` needs the x-dependence. **The `h^(2)(x)` field is recoverable EXACTLY** (I verified this — see Computational Tools): take the Phase-72 `h_sym_t` (symbolic in BOTH slice coords and amplitude t, from `cone_hessian_offcenter(..., slice_symbolic=True)`) and extract the `t^2`-coefficient WITHOUT substituting the center:
```
h^(2)_mu_nu(x) = (1/2) ∂_t^2 [ H_source(x; t·(bg+M)) - H_source(x; t·bg) ]_mu_nu |_{t=0}     # FIELD in (beta,gamma,p,q)
```
This is an EXACT rational function of (beta,gamma,p,q) (slice symbols appear in the denominator `det_2(V_0)^2` — it is genuinely a field to all orders in slice displacement, NOT a Taylor truncation). The box operator in the engine frame:
```
□ f = eta_bg^{ab} ∂_a∂_b f = 4 ∂_beta∂_gamma f - ∂_p^2 f - ∂_q^2 f     (eta_bg^{-1}_{beta,gamma}=2, symmetric ⇒ factor 4)
```
`eta_bg` is CONSTANT (zero free symbols), so `∂eta=0` and `□` has this simple flat form everywhere.

#### (C) The very-special-real geometry coincidence (CITE-ONLY, the fp-import-supergravity trap)

Source: Gunaydin-Sierra-Townsend (1983-84); de Wit-Van Proeyen (hep-th/9112027). The d=5, N=2 vector-multiplet scalar manifold is the cubic hypersurface `N(h) = C_{IJK}h^I h^J h^K = 1` with metric
```
a_IJ = -(1/3) ∂_I ∂_J ln N(h)        (very special real geometry)
```
**This is EXACTLY `Hess(-log N)` of the cubic norm — i.e. the cone-Hessian source structure of this milestone (up to the -1/3 normalization and the N=1 restriction).** For the exceptional case `N = det_3` of the Albert algebra h_3(O), the manifold is `E_{6(-26)}/F_4` (26-dim). **THE TRAP:** because the geometry coincides, it is tempting to read off GST's Einstein equation / `-R/2` / coupling. That is `fp-import-supergravity` — the GST couplings are fixed by the assumed N=2 SUSY closure, which is the circularity the milestone exists to avoid. Cite GST ONLY to acknowledge the slice IS very-special-real geometry (orientation); derive `kappa`, `T`, and the Einstein test from intrinsic algebraic data alone.

#### (D) The Jacobson route (CONTRAST-ONLY, fp-ensemble-gravity)

Source: Jacobson 1995 (gr-qc/9504004), "Thermodynamics of Spacetime: The Einstein Equation of State." Derives `G_mu_nu = 8πG T_mu_nu` by demanding the Clausius relation `δQ = T dS` hold for ALL local Rindler causal horizons through each point, with `S = (entropy) ∝ (horizon area)` (Bekenstein-Hawking) and `T = ` Unruh temperature of an accelerated observer. **This milestone REJECTS this route** (`fp-ensemble-gravity`): no horizon thermodynamics, no entropy-area, no ensemble/observer-averaging. Name it in the circularity audit to certify the construction does NOT use it; the curvature and stress tensor come from the algebra's cubic norm, one observer, one off-center point.

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| `h^(2)(x)` field extraction (t^2-coeff of `h_sym_t`, slice symbolic) | Gives the leading metric response as a FIELD (not a point) so `□` and `∂∂` act | 73-01 (build the field) | Phase-72 driver lines 264-296 (reuse) |
| Box / d'Alembertian on flat constant eta | `□f = 4∂_beta∂_gamma f - ∂_p^2 f - ∂_q^2 f` | 73-01 (□h̄ diagnostic), 73-02 | engine eta_bg^{-1} (computed) |
| Trace-reverse `h̄ = h - (1/2)eta tr(h)` | The handoff variable; `tr(h)=eta^{munu}h_munu` with engine eta | 73-01 (gauge diagnostic) | Wikipedia/MTW (transcribed) |
| Lorenz-gauge defect `∂^mu h̄_munu` | Diagnoses whether `□h̄=-2G^(1)` is valid; the algebra-derived h^(2) is NOT in Lorenz gauge | 73-01 (gauge audit) | transcribed |
| Linearized Einstein `G^(1)[h^(2)]` (full gauge-general formula) | The gauge-INVARIANT O(||M||^2) curvature content (I found it = 0 — degenerate) | 73-01 (confirm degeneracy) | transcribed |
| FULL nonlinear Einstein `G_munu[g] = Ric[g] - (1/2)g R[g]` | THE well-posed test LHS at O(||M||^4) (first nonvanishing curvature) | 73-02 (the decisive test) | engine `spacetime_curvature_of_g` |
| Independent `T_mu_nu` from the cross-term scalar `2Re((x2 x1)x3)` | The RHS, built BEFORE G, no Einstein input (DERV-03) | 73-01 (construct T) | canonical scalar stress tensor (Area 2) |
| Global `(kappa, Lambda)` least-squares / exact solve over the (M,x) family | Tests `G = kappa T + Lambda g` with GLOBAL constants (rejects per-point tuning) | 73-02 (the fit) | this phase (novel) |
| n=4 Ricci decomposition (S, Weyl) | Reports "curved but not Einstein-structured" cleanly (S!=0 or Weyl!=0) | 73-02 (honest level) | engine `ricci_decomposition_n4` |
| Per-equation circularity audit (provenance table) | Certifies no GST/SUSY/-R-2/Weinberg/Jacobson input (VALD-05) | 73-01 + 73-02 | this phase (Area 5) |

### Approximation / Order Schemes

| Scheme | Small Parameter | Regime | Error | Notes |
| ------ | --------------- | ------ | ----- | ----- |
| Amplitude series `M = t·M_0`, leading curvature order | `t = ||M||` | small-matter neighborhood of flat eta (sig (1,3)) | exact per order | Curvature first appears at `t^4`; `h` at `t^2` (`h^(1)=0`). The "leading-response" test is at `t^4` (= `h^(2)`-squared). |
| Leading-response (= "linear-in-M" in the re-scoped criterion) | `t` | the first nonvanishing curvature order O(t^4) | drops O(t^5) | This is the level at which a global `kappa` could hold; agreement here is the WEAKER "linear" level. |
| Exact (all-order in t) | — | finite rational M_0 in the splice | exact over Q | The strongest level; `G[g]=kappa T+Lambda g` exactly at finite M_0 for all (M,x). |

## Order-Counting Resolution (THE crux — resolved by direct computation, exact over Q)

The handoff posed the question precisely; here is the resolved answer, with the numbers I computed on the warm engine.

**Setup.** Phase 72: `R[g] = a_4 ||M||^4 + O(||M||^5)` (curvature starts at 4th order); `h = h^(2)||M||^2 + O(||M||^3)` (metric response starts at 2nd order, `h^(1)=0`). Naively the linearized Einstein tensor `G^(1)[h^(2)]` is O(||M||^2).

**What I computed (on `h^(2)(x)` as a field, at the center, exact over Q):**
1. **`R^(1)[h^(2)] = 0`** (the linearized Ricci scalar of `h^(2)` vanishes identically).
2. **`G^(1)_mu_nu[h^(2)] = 0` IDENTICALLY** (the full gauge-general linearized Einstein tensor of `h^(2)` is the zero matrix).
3. **`□h̄^(2)_mu_nu != 0`** (e.g. center `(0,0) = -76221/2450`, `(3,3) = -38637/1225`).
4. **`h^(2)` is NOT in Lorenz gauge:** `∂^mu h̄^(2)_mu_nu = [19143/9800, 9747/4900, 297/350, 0] != 0`.

**The reconciliation (unambiguous order bookkeeping for the planner):**
- `□h̄_mu_nu = -2 G^(1)_mu_nu` is an identity ONLY in Lorenz gauge. Since `h^(2)` is NOT in Lorenz gauge, the nonzero `□h̄^(2)` is **pure gauge** — it equals the omitted gauge terms `∂_mu(∂^a h̄_anu)+∂_nu(∂^a h̄_amu) - eta_munu ∂_a∂_b h̄^{ab}`, NOT physical curvature. The gauge-INVARIANT O(||M||^2) curvature is `G^(1)[h^(2)] = 0`.
- `G^(1)[h^(2)] = 0` is **REQUIRED for consistency** with `R = O(||M||^4)`: if `G^(1)[h^(2)]` were nonzero at O(||M||^2), then `R` would have an O(||M||^2) piece — but Phase 72 found `R` starts at O(||M||^4). So the vanishing is a CROSS-CHECK of the Phase-72 result, not a surprise. (Physically: the leading metric response `h^(2)` is, at linear order, a pure-gauge / coordinate deformation of flat space — it carries no linearized Einstein content; the genuine curvature is a SECOND-order effect.)
- **The genuine curvature lives at O(||M||^4) = SECOND order in `h^(2)`.** Totaro's Riemann is `R_ijkl = -(1/4)g^{pq}(C_jlp C_ikq - ...)` — BILINEAR in the cubic form C. Since `C = O(||M||^2)` (the difference-potential 3rd derivative, which starts at the cross-term), `R = C·C = O(||M||^4)`. This is exactly the `a_4 t^4` Phase 72 measured.

**Therefore the well-posed Einstein test is at O(||M||^4), using the FULL nonlinear `G_mu_nu[g]`** (not the linearized `G^(1)`). I confirmed `G_mu_nu[g] = Ric[g] - (1/2)g R[g] != 0` at the decisive M_0 (the engine computes it in ~2s), and that `g` is NOT an Einstein space there (`S = Ric - (R/4)g != 0`). So there IS a nonzero, well-posed LHS to test against `kappa T + Lambda g`.

**Definition of the honest levels (for `test-einstein-level`):**
- **exact:** `G_mu_nu[g(x)] = kappa T_mu_nu + Lambda g_mu_nu` holds for ALL (M,x) in the family at finite M (all-order in t), with a single GLOBAL `(kappa, Lambda)`, exactly over Q.
- **linear-in-M (= leading-response):** the equality holds only at the LEADING curvature order O(||M||^4) (i.e. matching the `t^4` coefficients across the family with global `(kappa, Lambda)`), failing at O(||M||^5+). Report as the WEAKER level it is.
- **none ("curved but not Einstein-structured"):** no global `(kappa, Lambda)` reproduces `G[g]` even at leading order; `S != 0` and/or `Weyl != 0` with structure NOT proportional to any independently-built `T`. This is an ACCEPTABLE full result — do NOT force.

**Consequence for the handoff instruction:** demote `□h̄^(2) ~ kappa T` to a SECONDARY gauge diagnostic. If the executor wants to use it, it must FIRST gauge-fix `h^(2)` to Lorenz gauge (solve `□ξ_nu = -∂^mu h̄_munu` for the gauge vector `ξ`, then `h'_munu = h_munu + ∂_mu ξ_nu + ∂_nu ξ_mu`) — but note that AFTER Lorenz-fixing, `□h̄'^(2) = -2 G^(1)[h^(2)] = 0`, so the linear test is degenerate either way. **The full-`G[g]` test at O(||M||^4) is the only non-degenerate, gauge-invariant Einstein test.** This is the single most important plan correction.

## Standard Approaches

### Approach 1: Full-`G[g]` Einstein test at the leading curvature order, global `(kappa,Lambda)` over an (M,x) family (RECOMMENDED)

**What:** (1) Build an independent `T_mu_nu` from the V_{1/2} cross-term content BEFORE computing G (Area 2). (2) Define `kappa` from intrinsic cross-term data BEFORE the fit (Area 3). (3) Compute the FULL nonlinear Einstein tensor `G_mu_nu[g] = Ric[g] - (1/2)g R[g]` via the warm engine, at several (M,x) points (vary matter direction/amplitude and slice position). (4) Test whether a SINGLE global `(kappa, Lambda)` solves `G_mu_nu[g] = kappa T_mu_nu + Lambda g_mu_nu` across the family, at exact order and at leading-response (O(||M||^4)) order. (5) Report the honest level via the n=4 decomposition.

**Why standard:** It is the only gauge-invariant, non-degenerate test (Order-Counting above). The full `G[g]` is already computed by `spacetime_curvature_of_g` (Phase 72 used it; ~2s at a rational M_0). The (M,x)-family + global-constant design is exactly what `test-einstein-level` and `fp-assume-einstein` demand.

**Track record:** Phase 72 ran this engine end-to-end (cross-term ON/OFF, ||M||->0, S/Weyl) exactly over Q, ALL_PASS. The full `G_munu[g]` I computed here in ~2s. The novel parts are `T_mu_nu`, `kappa`, and the family fit.

**Key steps (executable recipe):**
1. **Construct `T_mu_nu(x)` independently (DERV-03).** From the V_{1/2} cross-term scalar `psi(x;M) := 2Re((x2 x1)x3)` (the unique V_0<->V_{1/2} channel, x-dependent through x1's slice content), build the canonical scalar stress tensor (Area 2). Assert `T` is symmetric and `∂^mu T_mu_nu = 0` (conserved) over Q, and `T->0` as `||M||->0`. **Build T BEFORE G.**
2. **Define `kappa` intrinsically (Area 3).** From dimensional/scale analysis of the cross-term vs the curvature (NOT from `-R/2`, NOT a per-point fit). **Define kappa BEFORE the fit.**
3. **Compute `G_mu_nu[g]` at the (M,x) family.** Reuse `spacetime_curvature_of_g`; form `G = Ric - (1/2)g R`. Family: >=3 matter directions x >=3 slice positions x >=2 amplitudes (stay in the sig-(1,3) splice; check `eig_signature_count`).
4. **Global-constant fit (the can-fail test).** Solve `G_munu = kappa T_munu + Lambda g_munu` for `(kappa, Lambda)` as GLOBAL constants over the family (over-determined: 10 components x N points, 2 unknowns). Pass = a consistent global solution (exact over Q at finite M, or at the t^4 order); fail = no global solution.
5. **Honest level + decomposition.** Decompose `G[g]` (n=4 S/Weyl). If a global `(kappa,Lambda)` works exactly -> "exact"; only at leading order -> "linear/leading"; not at all -> "curved but not Einstein-structured" (report `S!=0`/`Weyl!=0` and that no independent `T` matches).
6. **Circularity audit (VALD-05).** Per-equation provenance table certifying `T`, `kappa`, and the test use no GST/SUSY/-R-2/Weinberg/Jacobson input (Area 5).

**Known difficulties:**
- The family fit needs exact-over-Q linear algebra; keep matter rational, only slice symbolic before `g.inv()` (>200s symbolic-matter inverse cliff — Phase-72 measured).
- `T_mu_nu` must be a genuine (0,2) tensor in the SAME (beta,gamma,p,q) frame as `G` (raise/lower with `eta_bg`, not `g`, for a flat-background stress tensor — see Area 2 caveat).
- The honest prior is FAILURE (non-Einstein). Build the fit to DETECT and REPORT failure cleanly; do not least-squares-force a near-fit and call it Einstein (`fp-assume-einstein`).

### Approach 2: Lorenz-gauge-fixed `□h̄^(2) ~ kappa T` (SECONDARY / gauge diagnostic only)

**What:** Gauge-fix `h^(2)` to Lorenz gauge (`□ξ_nu = -∂^mu h̄_munu`), then compare `□h̄'^(2)` to `kappa T`. **When to use:** ONLY as a documented diagnostic to show the handoff instruction was honored and to confirm the linear test is degenerate (`□h̄'^(2) = -2G^(1)[h^(2)] = 0`). **Tradeoff:** gauge-dependent before fixing, degenerate after; NOT the decisive test. Document it to close the handoff loop, but the verdict rests on Approach 1.

### Anti-Patterns to Avoid

- **Treating `□h̄^(2) ~ kappa T` as the decisive test without gauge-fixing.** `□h̄^(2)` is pure gauge here (`h^(2)` not in Lorenz gauge); the gauge-invariant linear content is zero. Use the full `G[g]` at O(||M||^4). _Example:_ reporting `□h̄^(2)_{00}=-76221/2450` as "the linearized Einstein LHS" — it is not; `G^(1)[h^(2)]=0`.
- **Importing the GST/very-special-geometry Einstein term or `-R/2`.** The slice IS very-special-real geometry, so this is the easy accidental circularity (`fp-import-supergravity`). Derive `kappa` and the test intrinsically; cite GST for orientation only. _Example:_ setting `kappa = ` the GST-fixed coupling, or using `a_IJ = -(1/3)Hess ln N` to read off an Einstein equation.
- **Per-point `(kappa,Lambda)` tuning.** Two free constants can match 10 components at ONE point trivially. Demand a GLOBAL solution over the family (`fp-assume-einstein`). _Example:_ "at M_0 there exist kappa,Lambda with G=kT+Lg, therefore Einstein."
- **Any horizon-thermodynamic / ensemble step.** `fp-ensemble-gravity`. _Example:_ invoking entropy-area or a Clausius `δQ=TdS` to "derive" the coefficient.
- **Subtracting an R=-3 / Cartan baseline.** FALSIFIED (Phase 70.1); the vacuum is flat. `Lambda=0`.
- **Building `T_mu_nu` AFTER seeing `G`.** Begs the question (DERV-03). Build and freeze `T` and `kappa` first.
- **Using `octonion_algebra.py` or the real-only cross-term.** Banned (buggy association). Use engine `det_3`.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE — cite and use)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| `h^(1)=0`, `h^(2)` matrix (center) | `h^(2)=[[261/1225,0,99/700,0],[0,9/40,99/700,0],[99/700,99/700,4293/9800,0],[0,0,0,4293/9800]]` | Phase 72 (exact Q) | The leading response; extend to the `h^(2)(x)` FIELD (Computational Tools) |
| `R[g]=a_4 ||M||^4`, `a_4=395268903/24010000` | leading curvature coefficient | Phase 72 (exact Q) | The order at which the Einstein test lives (O(||M||^4)) |
| Decisive M_0 (non-vacuous cross-term) | matter `MATTER_L` (V_{1/2}/10) + bg partner `BG_HALF` (V_0 x1 /2); triple `2Re((x2 x1)x3)=-13/63000!=0`; sig (1,3) | Phase 72 | The representative point; reuse verbatim |
| `eta_bg` (constant, null-aligned) | `[[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]`; inverse `[[0,2,0,0],[2,0,0,0],[0,0,-1,0],[0,0,0,-1]]` | engine (computed) | The flat background; box = `4∂_beta∂_gamma-∂_p^2-∂_q^2` |
| `G^(1)[h^(2)]=0`, `R^(1)[h^(2)]=0` | linearized Einstein/scalar of `h^(2)` vanish | THIS research (exact Q) | The linear test is degenerate; use full `G[g]` |
| `□h̄^(2)!=0` but `h^(2)` not in Lorenz gauge | defect `[19143/9800,9747/4900,297/350,0]` | THIS research (exact Q) | `□h̄^(2)` is pure gauge; demote to diagnostic |
| Full nonlinear `G_munu[g](M_0)!=0`, `S!=0` | `G=Ric-(1/2)gR` nonzero; not Einstein space at M_0 | THIS research (exact Q) | The well-posed test LHS exists and is non-Einstein at M_0 |
| Totaro closed-form Riemann | `R_ijkl=-(1/4)g^{pq}(C_jlp C_ikq-C_ilp C_jkq)`, C from DIFFERENCE potential, raise with `(eta+h)^{-1}` | Totaro Cor 2.3; engine | The curvature engine (validated vs hand-rolled in 72-01) |
| Corrected cross-term | `2Re((x2 x1)x3)`, F_4-invariant (CH+324/324) | Phase 64.1; engine `det_3` | The matter channel; the `psi` for `T`; never re-derive |
| Very special real geometry metric | `a_IJ=-(1/3)∂_I∂_J ln N(h)`, `N=det_3`, manifold `E_{6(-26)}/F_4` | GST 1983-84; de Wit-Van Proeyen | CITE for orientation ONLY (the fp-import trap) |
| Linearized GR formulas (A) | transcribed above (Ricci, trace-reverse, Lorenz, `□h̄=-2κT`) | Wikipedia/MTW/Wald | The formalism; adapt to mostly-minus via engine eta |
| Jacobson Einstein-of-state | `δQ=TdS` at local Rindler horizons, S∝area | Jacobson 1995 | CONTRAST/reject (fp-ensemble-gravity) |

**Key insight:** the curvature engine, the cross-term, `h^(2)`, `a_4`, and the Phase-70.1 metric selection are all certified/ratified — re-deriving risks re-introducing the association bug or re-opening settled decisions. The ONLY genuinely novel objects are `T_mu_nu`, `kappa`, and the family fit. Spend the budget there. And I have ALREADY computed (above) the order-counting facts (`G^(1)[h^(2)]=0`, `□h̄^(2)` pure-gauge, full `G[g]!=0`) — the executor should reproduce them as regression anchors, not rediscover them.

### Nearest Analogues and Mathematical Scaffolding (novel-territory)

| Analogue | What It Gives | Mapping to Our Problem | Confidence |
| -------- | ------------- | ---------------------- | ---------- |
| Linearized GR `□h̄=-2κT` | The structure of the Einstein test | Our `h` starts at `h^(2)` (quadratic), and the linear `G^(1)` is degenerate ⇒ use full `G[g]` at O(||M||^4) | HIGH (formalism), the adaptation is the novelty |
| Canonical scalar stress tensor `T_munu=∂_mu φ∂_nu φ-(1/2)eta_munu(∂φ)^2` (flat space, conserved on-shell) | The most defensible `T` from a scalar "matter field" | Our scalar is `psi=2Re((x2 x1)x3)`; treat the V_{1/2} content as field(s) on the slice | MEDIUM (which scalar / sigma-model metric is the design choice) |
| Sigma-model / multi-scalar `T_munu=G_ab ∂_mu φ^a ∂_nu φ^b - (1/2)eta_munu G_ab ∂φ^a·∂φ^b` | Symmetric, conserved `T` from MULTIPLE fields with a target metric `G_ab` | The V_{1/2} octonion components are the multiplet `φ^a`; `G_ab` from an F_4/Spin(9,1)-covariant bilinear | MEDIUM |
| GST very-special-real geometry | Confirms the slice geometry; warns of the trap | Cite for orientation; do NOT use its Lagrangian/couplings | HIGH (coincidence is real), AVOID as input |

**The Known->Unknown bridge.** KNOWN: for a flat-space scalar field `φ`, `T_munu = ∂_mu φ ∂_nu φ - (1/2)eta_munu(∂φ)^2` is symmetric and conserved, and sources linearized gravity via `□h̄=-16πG T`. UNKNOWN: whether the bulk-induced `G_munu[g]` (Totaro curvature of `g=eta+h`, at O(||M||^4)) equals `kappa·T[psi]` for the cross-term scalar `psi=2Re((x2 x1)x3)` (or a sigma-model `T` in the V_{1/2} components) with a GLOBAL `kappa` and `Lambda=0`. The research question is whether the algebra's curvature has the stress-tensor structure of its own matter content — a structural test, not a confirmation. **Validation anchors (no literature benchmark):** (a) `T->0` and `G->0` as `||M||->0` (both flat); (b) `T` symmetric + conserved over Q; (c) `G` and `T` are genuine (0,2) tensors with matching index structure; (d) global-constant consistency across the (M,x) family; (e) the n=4 decomposition (S/Weyl) gives the honest level.

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (installed) | exact symbolic algebra over Q: octonion/Jordan arithmetic, `det_3`, diff, `Matrix.inv`, `real_roots` signatures | the project's exact-over-Q engine; numpy float rank FORBIDDEN on verdicts |
| `code/bulk_geometry_verification.py` | warm engine (EXTEND) | `spacetime_curvature_of_g` (full `Ric[g],R[g]`), `cone_hessian_offcenter(slice_symbolic=True)` (the `h^(2)(x)` FIELD), `_eta_minkowski`/`_frame_jacobian_bg_to_mink` (constant eta), `ricci_decomposition_n4` (S,Weyl), `det_3`/`det_3_block`, `eig_signature_count`, `hand_rolled_riemann_of_g` | the decisive surface; ALL_PASS exit 0; det_3 SSOT |
| Python 3 (`python3 -u`, foreground) | — | run heavy symbolic with unbuffered progress prints | defeats the ~150s executor stream-watchdog ([[feedback_executor_watchdog_stall_long_symbolic]]) |

### Engine extensibility — VERIFIED (I ran these, exact over Q)

I confirmed the three load-bearing computational questions the handoff flagged:

1. **`cone_hessian_offcenter(slice_symbolic=True)` is an EXACT rational function of the slice coords (NOT a Taylor truncation).** Example: `H[0,0] = gamma^2/(beta^2*gamma^2 - 2*beta*gamma*p^2 - 2*beta*gamma*q^2 + p^4 + 2*p^2*q^2 + q^4) = gamma^2/det_2(V_0)^2` — slice symbols are in the DENOMINATOR, so the field is reliable to ALL orders in slice displacement. `□` (which needs 2nd x-derivatives) is therefore well-defined and meaningful. Symbolic-then-subs equals direct-at-point (verified). The only singularity is the light-cone `det_2(V_0)=0`, away from the center.

2. **`eta_bg` is position-INDEPENDENT (constant, zero free symbols).** So `∂eta=0` and `□ = eta_bg^{ab}∂_a∂_b` has the simple flat form. (`eta_bg` is NOT diagonal — it is null-aligned `[[0,1/2,..],[1/2,0,..],..]` because `x0=(beta+gamma)/2`. Build `□` from `eta_bg^{-1}`, never hard-code diag.)

3. **`h^(2)(x)` as a FIELD and `□h̄^(2)` are computable (~20s total, exact over Q).** I built `h^(2)(x)` (the `t^2`-coeff of `h_sym_t` without substituting the center; ~10s), verified it reduces to the handoff matrix at the center, and applied `□` (~10s more). All the linearized-GR diagnostics (`G^(1)[h^(2)]`, `R^(1)`, Lorenz defect) and the full `G[g]` ran in well under the watchdog limit.

### Computational Feasibility (MEASURED here + Phase-72 COMPUTATIONAL.md)

| Computation | Cost | Bottleneck | Mitigation |
| ----------- | ---- | ---------- | ---------- |
| `h^(2)(x)` field (t^2-coeff, slice symbolic) | ~10 s | symbolic-in-(slice,t) cone-Hessian diff | keep matter/bg as `t·(rational)`; cancel per entry |
| `□h̄^(2)`, `G^(1)[h^(2)]`, Lorenz defect (fields) | ~10 s | 2nd derivatives of rational fields | cancel per entry; eta constant |
| Full `G_munu[g]` at a rational M_0 | ~2 s | `g.inv()` (matter rational) | matter rational BEFORE inv (Phase-72 cliff: >200s if symbolic) |
| (M,x)-family: full `G[g]` at ~6-18 points | ~12-40 s | repeated curvature | loop rational M_0/slice points; print between |
| `T_mu_nu` build + conservation check | fast | — | `psi` and its derivatives are rational fields |
| Global `(kappa,Lambda)` exact solve over family | fast | linear system over Q | `linsolve`/`Matrix.solve` exact |

**Watchdog discipline ([[feedback_executor_watchdog_stall_long_symbolic]]):** foreground `python3 -u`, print progress between heavy steps. Background-resume stalls were observed; if a stall happens the orchestrator commits + writes SUMMARY from partial output.

**Installation:** SymPy 1.14.0 already installed; nothing to install.
```bash
# nothing to install; if a fresh venv is ever needed:
pip install sympy==1.14.0
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How | Expected |
| ----- | ----------------- | --- | -------- |
| `h^(2)(x)` at center == handoff matrix | the field reduces correctly | subs center into `h^(2)(x)` | `[[261/1225,0,99/700,0],...]` (verified) |
| `G^(1)[h^(2)] = 0`, `R^(1)[h^(2)] = 0` | the linear test is degenerate (consistency with R=O(||M||^4)) | full gauge-general `G^(1)` of the `h^(2)` field | zero matrix / 0 (verified) |
| `□h̄^(2) = ` (gauge terms only) | `□h̄^(2)` is pure gauge (h^(2) not in Lorenz gauge) | compare `□h̄^(2)` to `-2G^(1)+`gauge | nonzero, but `G^(1)=0` (verified) |
| `T_mu_nu` symmetric | `T` is a valid stress tensor | `T == T.T` over Q | True |
| `∂^mu T_mu_nu = 0` | `T` conserved (Bianchi-compatible RHS) | divergence with eta over Q | 0 (or document the on-shell condition) |
| `T->0` and `G[g]->0` as `||M||->0` | both vanish at the flat vacuum | amplitude series `t->0` | both 0 (G via Phase-72 ||M||->0) |
| Global `(kappa,Lambda)` over family | NOT a per-point tune | over-determined solve | consistent global solution OR no solution (honest) |
| `G[g]` Totaro vs hand-rolled | the curvature engine is correct | `hand_rolled_riemann_of_g` on a few components | exact agreement over Q |
| sig (1,3) at each family point | inside the Lorentzian splice | `eig_signature_count(g)` | (1,3,0) |
| Engine regression | det_3 + curvature unbroken | `python3 code/bulk_geometry_verification.py` | ALL_PASS, exit 0 |
| Reality + exactness | no Wick/float artifact | all quantities real rationals over Q | real, exact |

### Known Limits and Benchmarks

| Limit | Regime | Known Result | Source |
| ----- | ------ | ------------ | ------ |
| `||M||->0` | both `T` and `G[g]` | -> 0 (flat eta, DERIVED) | Phase 70.1; 72 |
| Leading curvature order | O(||M||^4) | `R ~ a_4 t^4`, `a_4=395268903/24010000` | Phase 72 |
| Linear-in-`h^(2)` Einstein | O(||M||^2) | `G^(1)[h^(2)] = 0` (degenerate) | THIS research |
| Cross-term OFF + M!=0 | block-diagonal det | curvature drops ~94% (dominantly cross-term-sourced) | Phase 72 |
| M=0 vacuum | `Lambda` | `Lambda=0` (flat, DERIVED — NOT Einstein-negative) | Phase 70.1 |

### Red Flags During Computation

- `G^(1)[h^(2)] != 0` -> contradicts Phase 72's `R=O(||M||^4)` (the O(||M||^2) curvature should vanish); recheck the field extraction / eta. (I verified it IS zero.)
- `□h̄^(2) = 0` -> would mean `h^(2)` IS in Lorenz gauge; I found it is NOT (defect nonzero). If you get 0, recheck the trace `tr(h)` (must use `eta_bg^{-1}`, the null-aligned inverse).
- A nonzero imaginary part anywhere -> reality/Wick contamination (wrong cross-term). Everything is real rational over Q.
- The global `(kappa,Lambda)` fit "almost" works -> do NOT round to call it Einstein (`fp-assume-einstein`); report the exact residual and the honest level.
- `kappa` chosen to make a single point match -> per-point tuning (`fp-assume-einstein`); `kappa` must be GLOBAL and defined before the fit.
- Any appearance of `-R/2`, a GST coupling, a SUSY closure, an entropy/area term, or `δQ=TdS` -> a forbidden import crept in; strike it and report the intrinsic level.
- `g` signature != (1,3) at a family point -> outside the splice; shrink `||M||`.

## Common Pitfalls

### Pitfall 1: Treating `□h̄^(2)` as the linearized Einstein tensor [THE order-counting trap]

**What goes wrong:** Reading the nonzero `□h̄^(2)` as the physical (gauge-invariant) linearized Einstein content and testing it against `kappa T`. **Why:** `□h̄=-2G^(1)` holds ONLY in Lorenz gauge; the algebra-derived `h^(2)` is NOT in Lorenz gauge, so `□h̄^(2)` is pure gauge and `G^(1)[h^(2)]=0`. **How to avoid:** Use the FULL nonlinear `G_munu[g]=Ric[g]-(1/2)gR[g]` at O(||M||^4); demote `□h̄^(2)` to a gauge diagnostic. **Warning signs:** quoting `□h̄^(2)_{00}=-76221/2450` as "the Einstein LHS"; finding the linear test "works" because you compared two gauge artifacts. **Recovery:** compute `G^(1)[h^(2)]` (it is 0), confirm the degeneracy, switch to full `G[g]`.

### Pitfall 2: Importing GST/very-special-geometry structure [fp-import-supergravity; the SUBTLE trap]

**What goes wrong:** The slice IS very-special-real geometry (`a_IJ=-(1/3)Hess ln N`, `N=det_3`), so reading off the GST Einstein term / `-R/2` / coupling feels natural — and it is exactly the dead circular route (the couplings are fixed by assumed SUSY closure). **Why:** the geometric coincidence is real and seductive. **How to avoid:** cite GST ONLY to acknowledge the manifold; derive `kappa`, `T`, and the test from intrinsic algebraic data; run the per-equation circularity audit (Area 5). **Warning signs:** `kappa = `(a GST/SUSY-fixed number); `T` or the Einstein equation traced to a supergravity multiplet; `-R/2` appearing as an input. **Recovery:** strike the import; rebuild from the cross-term scalar; report the intrinsic level (likely non-Einstein).

### Pitfall 3: Building `T_mu_nu` after seeing `G`, or per-point `(kappa,Lambda)` tuning [fp-assume-einstein; DERV-03]

**What goes wrong:** Constructing `T` (or choosing `kappa,Lambda`) to match the already-computed `G` — trivially "succeeds" and proves nothing. **Why:** two free constants match 10 components at one point; a reverse-engineered `T` matches by construction. **How to avoid:** FREEZE `T` and `kappa` from intrinsic data BEFORE computing `G`; demand a GLOBAL `(kappa,Lambda)` over the (M,x) family (over-determined). **Warning signs:** `T` defined using `Ric` or `R`; `kappa` solved per-point; "Einstein at M_0" from a single point. **Recovery:** rebuild `T` from `psi=2Re((x2 x1)x3)` only; re-run the family fit with global constants.

### Pitfall 4: Octonion non-associativity / wrong cross-term [propagates everywhere]

**What goes wrong:** Wrong association (`(x1 x2)x3`, real-only `2 d1 d2 d3`) corrupts `psi`, `T`, and `G` silently (error amplified by differentiation). **How to avoid:** use engine `det_3` (`2Re((x2 x1)x3)`) for ALL of it; pre-flight on genuinely non-associative M (e_4..e_7 nonzero). **Warning signs:** det_3 disagrees with CH norm on octonionic data; a "verified" cross-term done only on quaternionic e_0..e_3 (vacuous). **Recovery:** recompute with engine `det_3`; redo everything downstream.

### Pitfall 5: Mostly-minus vs mostly-plus sign error [signature]

**What goes wrong:** Hard-coding a `diag(-1,1,1,1)` eta or importing the textbook `-16πG`/`-2κ` coefficient (mostly-plus) into a mostly-minus computation flips signs in `tr(h)`, `□`, and `kappa`. **How to avoid:** build `□`, `tr`, and trace-reverse from the engine's explicit `eta_bg`/`eta_bg^{-1}` (mostly-minus, null-aligned); pin the sign of `kappa` by the FIT, not by the textbook value. **Warning signs:** `kappa` comes out with the textbook sign "for free"; `tr(h)` uses `diag` not `eta_bg^{-1}`. **Recovery:** recompute traces and `□` with `eta_bg^{-1}=[[0,2,..],[2,0,..],..]`.

## Level of Rigor

**Required:** EXACT over Q (a computer-algebra proof of the specific tensor identities at the chosen (M,x) family), "controlled exact evidence on a decisive family." NOT a general theorem for all M (out of scope). The decisive verdict is: does a GLOBAL `(kappa,Lambda)` reproduce `G_munu[g]` against an independently-built `T_munu` across the family, at exact / leading-response / no level.

**Justification:** `test-einstein-level` (oracle), `fp-float-decisive`, and `fp-assume-einstein` demand exactness and global constants, not floating-point or per-point fits. The claim is novel (no benchmark), so rigor is internal: `T` symmetric+conserved over Q, both `T,G->0` as `||M||->0`, the global-constant consistency, the Totaro-vs-hand-rolled cross-check, and reality.

**Concretely:**
- All test verdicts (`G[g]`, `T`, the fit residual, S/Weyl) computed with `sympy.Rational`, exact over Q. No float on any verdict.
- `(kappa,Lambda)` is a GLOBAL exact solution (or provably no solution) over the family; never per-point, never least-squares-rounded.
- `T` and `kappa` are FROZEN before `G` is computed (provenance recorded).
- The full `G[g]` cross-checked Totaro-vs-hand-rolled on a few components.
- A representative (M,x) family (>=3 directions x >=3 positions x >=2 amplitudes) suffices for the verdict; an all-M theorem is NOT required.
- Reproduce the THIS-research anchors (`G^(1)[h^(2)]=0`, full `G[g]!=0`, `□h̄^(2)` defect) as regression checks.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Posited GST/N=2 supergravity Lagrangian, `-R/2` from SUSY closure | Intrinsic cubic-norm curvature `G[g]` tested against an intrinsic `T` | v17.0 | No Lagrangian, no SUSY; the circular route is the thing being avoided |
| Linear-in-M linearized-Einstein test `□h̄^(1)~kT` | QUADRATIC-response test (h^(2)); and the FULL `G[g]` at O(||M||^4) (since `G^(1)[h^(2)]=0`) | Phase 72 + THIS research | The linear test is degenerate; the well-posed test is nonlinear `G[g]` |
| "Center is Einstein, Lambda<0" (Cartan) | Vacuum FLAT (Lambda=0), DERIVED from KKT det_2 | Phase 70.1 | No Lambda tripwire; `Lambda` fit (expected 0), never a circularity gate |
| `□h̄~kT` as the decisive handoff test | `□h̄` is a gauge diagnostic; full `G[g]` is decisive | THIS research | The single most important plan correction |
| `octonion_algebra.py` det_3 (buggy, float) | engine `det_3` (`2Re((x2 x1)x3)`, exact, F_4-invariant) | Phase 64.1 | The SSOT; stale project-research references SUPERSEDED |

**Superseded approaches to avoid:**
- **GST/SUSY/-R/2/Weinberg import:** `fp-import-supergravity`. The slice IS very-special-real geometry, so guard hard.
- **Jacobson thermodynamic / ensemble:** `fp-ensemble-gravity`. Curvature + stress from the algebra, one observer, one point.
- **Per-point Einstein-fitting:** `fp-assume-einstein`. Global constants over the family.
- **R=-3 baseline:** FALSIFIED (Phase 70.1). Flat vacuum, Lambda=0.

## Open Questions

1. **Which independent `T_mu_nu` construction is most defensible?** (THE design choice.)
   - Known: the cross-term scalar `psi=2Re((x2 x1)x3)` is the unique V_0<->V_{1/2} channel; the canonical scalar stress tensor `T_munu=∂_mu psi ∂_nu psi - (1/2)eta_munu(∂psi)^2` is symmetric and conserved on-shell; a sigma-model `T` in the V_{1/2} components (target metric `G_ab` from an F_4/Spin(9,1)-covariant bilinear) is the multi-field generalization.
   - Unclear: whether the "field" is the single scalar `psi(x)`, the 16 V_{1/2} components as a multiplet, or a covariant bilinear; and whether `∂` means slice-coordinate derivative of `psi(x;M)` or a polarization in the matter directions.
   - Impact: determines the RHS of the decisive test.
   - Recommendation: build BOTH the single-scalar `T[psi]` and a sigma-model `T[V_{1/2}]` as candidates; require each to be symmetric + conserved + `->0` at `||M||->0` BEFORE the fit; report which (if any) matches `G[g]` with a global `kappa`. Do NOT pick the one that "works" after seeing G (DERV-03). Recommend the single-scalar `T[psi]` as the PRIMARY (cleanest, most defensible, directly the named cross-term channel); the sigma-model as a documented alternative.

2. **What is `kappa` intrinsically?** (Area 3.)
   - Known: `kappa` must be a global constant from intrinsic cross-term data, NOT `-R/2`, NOT per-point.
   - Unclear: the operational definition — a ratio of the leading curvature coefficient `a_4` to a leading `T`-coefficient? a fixed numerical factor from the polarization `d(X,X,X)=6 det`?
   - Impact: whether `kappa` is genuinely independent or a disguised fit.
   - Recommendation: DEFINE `kappa` as a fixed rational from the dimensionless algebra (e.g. from the ratio of the `t^4` coefficients of `R[g]` and of a curvature scalar built from `T`, evaluated at ONE reference direction, then HELD FIXED across the family). Freeze it before the family fit; the family test is then whether that SAME `kappa` works for all (M,x). If `kappa` has to be re-fit per direction, that is the "linear/leading" or "none" level.

3. **Does any global `(kappa,Lambda)` reproduce `G[g]` at leading order?** (The decisive unknown.)
   - Known: `g` carries `S!=0` and `Weyl!=0` at finite M (not an Einstein space). For `G=kT+Lg` to hold, `T` would need to carry the SAME traceless-Ricci/Weyl structure.
   - Unclear: whether the cross-term `T` happens to match the bulk `G`'s structure.
   - Impact: the headline verdict (exact / leading / none).
   - Recommendation: the honest prior is "none / curved but not Einstein-structured" (the bulk curvature is generic, the cross-term `T` is special). Build the family fit to DETECT and REPORT a non-match cleanly. A leading-order match would be a strong (surprising) positive; an exact all-M match would be the strongest. Do NOT force.

4. **Is V_1 (alpha) inert here too?** (Carries forward from Phase 71/72.)
   - Known: `alpha` is absent from the triple `2Re((x2 x1)x3)`; V_1-only matter left `R[g]=0` in Phase 72.
   - Recommendation: build `T` and the test from V_{1/2} (and note V_1-inertness structurally); confirm V_1-only `T=0` and `G=0` as a control.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost |
| ------------- | ---------- | --------- | ---- |
| Full `G[g]` family fit intractable | expression swell at many points | fewer family points + the `t^4`-coefficient (leading-order) test only | low |
| Single-scalar `T[psi]` clearly wrong structure | `psi` too coarse | sigma-model `T[V_{1/2}]` with covariant `G_ab` | low-medium (build the multiplet T) |
| `kappa` cannot be defined non-circularly | no clean intrinsic scale | report "none" (no intrinsic coupling reproduces G) — an honest result | none (it IS the verdict) |
| Totaro vs hand-rolled disagree on `G[g]` | closed-form mis-applied | hand-rolled Riemann of `g` as primary (already in engine) | low |
| `□h̄^(2)` diagnostic confusing | gauge dependence | drop it; rely solely on full `G[g]` (Approach 1) | none |

**Decision criteria:** If no global `(kappa,Lambda)` reproduces `G_munu[g]` against ANY independently-built `T_munu` even at leading order O(||M||^4), report **"curved but not Einstein-structured"** (an acceptable FULL result — the milestone's honest prior). If a global `(kappa,Lambda)` works at leading order but not exactly, report **"Einstein at linear/leading order in M only"** (the weaker level). If it works exactly for all (M,x) at finite M, report **"exact Einstein structure"** (the strong win). If the ONLY way to a match is importing GST/SUSY/-R-2/Weinberg, STOP and report the honest non-Einstein level (that import is the circularity).

## Recommended Plan Structure (2 plans)

### Plan 73-01 — Construct `T_mu_nu` + `kappa` + the `h^(2)(x)` field + circularity-audit scaffold (BUILD; non-interactive)

**Goal:** Freeze the independent RHS and the field machinery BEFORE any Einstein test. Establish the order-counting facts as regression anchors.

- **T1 — Extend the engine with the `h^(2)(x)` FIELD.** Add a routine returning `h^(2)(x)` (the `t^2`-coeff of `h_sym_t`, slice symbolic) for an (M, bg) direction; assert it reduces to the handoff `h^(2)` matrix at the center (regression). Add `box(field)` from `eta_bg^{-1}`.
- **T2 — Reproduce + freeze the order-counting anchors.** Compute `G^(1)[h^(2)]` (assert = 0), `R^(1)[h^(2)]` (=0), `□h̄^(2)` (nonzero) and the Lorenz defect (nonzero); DOCUMENT that `□h̄^(2)` is pure gauge and the linear test is degenerate ⇒ the decisive test is full `G[g]` at O(||M||^4). *(These are the THIS-research anchors; reproduce, do not rediscover.)*
- **T3 — Construct `T_mu_nu` independently (DERV-03).** From `psi(x;M)=2Re((x2 x1)x3)`: build `T_munu=∂_mu psi ∂_nu psi - (1/2)eta_munu(∂psi)^2` (PRIMARY), and a sigma-model `T[V_{1/2}]` (ALTERNATIVE). Assert each is symmetric, `∂^mu T_munu=0` over Q, and `->0` as `||M||->0`. **No `Ric`/`R`/`G` anywhere in `T`.**
- **T4 — Define `kappa` intrinsically (Area 3).** Fix `kappa` as a rational from intrinsic cross-term/curvature scale at ONE reference direction; FREEZE it. Record the definition (provenance).
- **T5 — Circularity-audit scaffold (VALD-05).** Build the per-equation provenance table (each equation feeding `T`, `kappa`, the test ⟶ its inputs ⟶ certify NO GST/SUSY/-R-2/Weinberg/Jacobson). Pre-populate for T3/T4.
- **Decisive can-fail check for 73-01:** `T_munu` symmetric + conserved (`∂^mu T_munu=0`) + vanishing at `||M||->0`, all exact over Q, with `T` and `kappa` provably independent of any Einstein/G input (audit table). If `T` cannot be made conserved/independent, the Einstein test cannot be posed honestly — report that.

### Plan 73-02 — The (M,x)-family linearized-Einstein test + honest-level verdict (TEST; INTERACTIVE — verdict checkpoint)

**Goal:** Run the decisive can-fail test and pronounce the honest level.

- **T1 — Compute `G_munu[g]` over the (M,x) family.** Reuse `spacetime_curvature_of_g`; form `G=Ric-(1/2)gR` at >=3 matter directions x >=3 slice positions x >=2 amplitudes (assert sig (1,3) at each via `eig_signature_count`). Cross-check Totaro-vs-hand-rolled on a few components.
- **T2 — The global `(kappa,Lambda)` fit (the can-fail test).** With `T` and `kappa` FROZEN from 73-01, solve `G_munu = kappa T_munu + Lambda g_munu` for a SINGLE global `(kappa,Lambda)` over the family — exact over Q, at finite M and at the `t^4` (leading) order. Report the exact residual.
- **T3 — Honest level + decomposition.** `ricci_decomposition_n4(G[g])` (S, Weyl). Classify: exact / leading-only / none ("curved but not Einstein-structured"). Report `S!=0`/`Weyl!=0` and whether any independent `T` matches.
- **T4 — Circularity audit FINAL (VALD-05) + verdict checkpoint (HUMAN).** Complete the provenance table; certify no forbidden import. Present the honest level for human ratification (per [[feedback_executor_socket_timeout_long_agent]] / the verdict-checkpoint pattern); do NOT self-ratify an Einstein claim. Write `derivations/73-einstein-structure.tex`.
- **Decisive can-fail check for 73-02:** does a SINGLE global `(kappa,Lambda)` reproduce `G_munu[g]` against the independently-frozen `T_munu` across the family (exact / leading / none)? A non-match is reported as "curved but not Einstein-structured" (acceptable full result); a per-point or import-dependent "match" is REJECTED. The verdict is the honest level, human-ratified.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that the full nonlinear `G[g]` at O(||M||^4) is THE right LHS (vs some resummed/effective object). It is the standard gauge-invariant Einstein tensor of the actual metric `g`, and the linear `G^(1)` is provably degenerate, so this is sound — but the executor must verify `G[g]` is computed on the SAME `g` (B1 difference-potential, indices raised with `(eta+h)^{-1}`) that Phase 72 used, cross-checked Totaro-vs-hand-rolled. Flagged in 73-02 T1.
2. **Assumption that might be wrong (2):** that the single-scalar `T[psi]` is the natural matter stress tensor. The V_{1/2} content is 16-dimensional; collapsing it to one scalar `psi` may lose structure that a sigma-model `T` would capture. Mitigated by building BOTH and reporting which (if any) matches. The honest prior is that NEITHER matches exactly (the bulk curvature is generic).
3. **Limitation understated:** the rigor is "exact on a representative (M,x) family", not "proved for all M". A non-Einstein verdict on the family is decisive for the milestone's honest reporting; an exact-for-all-M theorem is out of scope.
4. **Simpler method overlooked?** The `□h̄^(2)~kT` handoff is SIMPLER but I showed it is gauge-dependent and degenerate — the full `G[g]` is necessary. There is no simpler correct test. (Using it as a diagnostic is fine and cheap.)
5. **Would a specialist disagree?** A relativist might note that "an intrinsic algebraic `T` matching the bulk `G`" is a strong, unusual claim, and that the generic expectation (Weyl!=0, S!=0) is non-Einstein. That is exactly the milestone's honest prior — Phase 73 is built to REPORT "curved but not Einstein-structured" cleanly, not to manufacture Einstein form. A Jordan-algebra geometer might note the slice is very-special-real geometry and "of course" relates to GST — which is precisely the `fp-import-supergravity` trap the audit guards against (cite for orientation, derive intrinsically).
6. **The biggest risk:** accidentally importing GST's `-R/2`/coupling (because the geometry coincides) or reverse-engineering `T` from `G`. Guarded by Pitfalls 2/3, the freeze-before-G discipline (DERV-03), the per-equation circularity audit (VALD-05), and the global-constant family fit (fp-assume-einstein). The second-biggest risk is the order-counting confusion (Pitfall 1), which I have resolved by direct computation and transcribed as regression anchors.

## Sources

### Primary (HIGH confidence)

- `.gpd/phases/72-b-matter-sourcing/72-02-SUMMARY.md` — the human-ratified Phase-72 handoff (`h^(1)=0`, `h^(2)`, `a_4`, decisive M_0, the `□h̄~kT` instruction). AUTHORITATIVE.
- `.gpd/ROADMAP.md` (Phase 73 entry, re-scoped 2026-05-31) — the quadratic-response linearized-Einstein can-fail test framing; `Lambda=0`, no tripwire.
- `.gpd/state.json` `project_contract` — `claim-einstein-structure`, `deliv-phaseC`, `test-einstein-level`, `fp-import-supergravity`, `fp-assume-einstein`, `fp-ensemble-gravity`, `ref-gst`, `ref-jacobson-contrast` (all quoted in this research).
- `paper6-bulk-geometry-prompt.md` — authoritative milestone spec, Phase C target + reporting discipline ("curved but not Einstein-structured is acceptable, do NOT force").
- `.gpd/CONVENTIONS.md` (v17.0) — signature, det_3 SSOT, Lambda=0 (§6 superseded), the GST-geometry-only / Jacobson-contrast-only reference maps.
- `code/bulk_geometry_verification.py` — the warm engine (det_3 SSOT, full `spacetime_curvature_of_g`, `cone_hessian_offcenter` field, constant eta, `ricci_decomposition_n4`, `hand_rolled_riemann_of_g`, `eig_signature_count`); ALL_PASS exit 0. The h^(2)(x)-field, box, `G^(1)`, and full `G[g]` computations in this research were run on it.
- Wikipedia, "Linearized gravity" (MTW (-,+,+,+) convention) — the linearized Ricci tensor `R_munu=(1/2)(∂_s∂_mu h^s_nu+∂_s∂_nu h^s_mu-∂_mu∂_nu h-□h_munu)`, trace-reverse `h̄=h-(1/2)eta h`, Lorenz gauge `∂^mu h̄_munu=0`, `□h̄_munu=-2κT`, `G_munu=-(1/2)□h̄`. https://en.wikipedia.org/wiki/Linearized_gravity (transcribed; sign-flip to mostly-minus noted).
- Misner-Thorne-Wheeler, *Gravitation*, Ch.18; Wald, *General Relativity*, §4.4; Carroll, *Spacetime and Geometry*, Ch.7 — standard linearized GR (the same formulas, mostly-plus).

### Secondary (MEDIUM confidence)

- Gunaydin-Sierra-Townsend (1983-84), Phys. Lett. B133 / Nucl. Phys. B242 — very special geometry / magic supergravity scalar manifold `E_{6(-26)}/F_4`. CITE FOR GEOMETRY ONLY (`a_IJ=-(1/3)∂_I∂_J ln N`); the Lagrangian/SUSY couplings are the AVOIDED circular route. https://www.sciencedirect.com/science/article/abs/pii/0370269383901089
- de Wit & Van Proeyen, "Special geometry, cubic polynomials and homogeneous quaternionic spaces", hep-th/9112027 (1992) — the very-special-real metric `a_IJ=-(1/3)Hess ln N` from a cubic norm. CITE for the coincidence; AVOID the Lagrangian. https://arxiv.org/abs/hep-th/9112027
- Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State", gr-qc/9504004, PRL 75:1260 (1995) — the rejected ensemble/thermodynamic route (`δQ=TdS`, S∝area, Unruh T). CONTRAST ONLY (`fp-ensemble-gravity`). https://arxiv.org/abs/gr-qc/9504004
- Stress-energy tensor (Wikipedia) / sigma model (Wikipedia) — the canonical scalar `T_munu=∂_mu φ∂_nu φ-(1/2)eta_munu(∂φ)^2` (symmetric, conserved on-shell for a scalar in flat space) and the sigma-model `T_munu=G_ab ∂_mu φ^a∂_nu φ^b-(1/2)eta_munu G_ab∂φ^a·∂φ^b`. https://en.wikipedia.org/wiki/Stress%E2%80%93energy_tensor , https://en.wikipedia.org/wiki/Sigma_model
- "Canonical and gravitational stress-energy tensors", gr-qc/0510044; Belinfante-Rosenfeld symmetrization — for making a canonical `T` symmetric+conserved if needed. https://arxiv.org/pdf/gr-qc/0510044

### Tertiary (LOW confidence)

- Project-level `.gpd/research/METHODS.md`/`PITFALLS.md`/`COMPUTATIONAL.md` — USE WITH CAUTION: their det-SSOT references to `octonion_algebra.py` are SUPERSEDED (use engine `det_3`); their "center is Einstein/pure-Lambda" baseline is FALSIFIED (Phase 70.1). The performance cliffs (>200s symbolic inverse, ~watchdog) are accurate.
- **No external literature for the CLAIM** (an intrinsic algebraic `T` from octonion cross-terms tested against a bulk-induced `G`). Novel; validation is internal (symmetry, conservation, `||M||->0` limit, global-constant family fit), not literature-benchmarked.

## Metadata

**Confidence breakdown:**
- Mathematical framework (linearized GR, order-counting, engine extensibility): HIGH — formulas transcribed and the order bookkeeping resolved by direct computation (`G^(1)[h^(2)]=0`, full `G[g]!=0`, `□h̄^(2)` pure-gauge), exact over Q.
- Standard approaches (full-`G[g]` family test): HIGH on the method (the only gauge-invariant non-degenerate test; engine measured), MEDIUM on the outcome (honest prior = non-Einstein).
- `T_mu_nu` construction: MEDIUM — the canonical scalar / sigma-model templates are standard, but WHICH scalar/multiplet is the genuine design choice (Open Q1).
- `kappa` definition: MEDIUM — must be intrinsic and global; the operational definition is a design choice (Open Q2), guarded against circularity.
- Circularity audit (VALD-05): HIGH — the per-equation provenance method is concrete; the GST-coincidence trap is identified and guarded.
- Computational tools: HIGH — SymPy 1.14.0 installed; engine ALL_PASS; all costs MEASURED here (h^(2)(x) field ~10s, □h̄^(2) ~10s, full G[g] ~2s).
- External literature for the claim: LOW — none; expected (novel construction).

**Research date:** 2026-06-01
**Valid until:** Physics/math results stable indefinitely (linearized GR, GST geometry, Jacobson are decades-old; the Phase-70.1/72 results are ratified project decisions). The engine API is the volatile part — re-confirm `spacetime_curvature_of_g` / `cone_hessian_offcenter` signatures if `code/bulk_geometry_verification.py` is refactored. SymPy 1.14.0 is the fastest-moving dependency.
