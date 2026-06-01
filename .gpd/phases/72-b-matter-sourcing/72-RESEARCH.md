# Phase 72: B — Matter-Sourcing - Research

**Researched:** 2026-05-30
**Refreshed:** 2026-05-31 (matter-on-flat re-frame after Phase 70.1 metric-selection verdict)
**Domain:** Computational differential geometry on the h_3(O) (Albert algebra) symmetric cone; exact-over-Q curvature of a dim-4 Lorentzian spacetime slice g = eta + h built on a FLAT KKT-Minkowski baseline; matter-sourcing of h via cubic-norm cross-terms.
**Confidence:** HIGH on method/mechanism/decomposition/isolation (engine measured end-to-end; standard GR decomposition); MEDIUM on the matter-sourcing OUTCOME (novel, undecided — this is the phase's open question); LOW on external literature for matter-sourcing (none found — expected).

> ## Re-frame note (Phase 70.1 — READ FIRST)
>
> **What changed and why.** This RESEARCH.md was first written (2026-05-30) when the
> physical-metric question was still open and the curvature was computed *as if the
> cone-Hessian were the spacetime metric*. Phase 70.1 (COMPLETE 2026-05-31,
> human-ratified outcome 2, VERIFIED 5/5 HIGH —
> `.gpd/phases/70.1-revise-a0-select-the-physical-spacetime-metric-cone-hessian-vs-eta-h-bridge/70.1-01-SUMMARY.md`)
> **SELECTED the physical spacetime metric and FALSIFIED the alternative.** The binding
> consequences for Phase 72 are:
>
> 1. **The physical spacetime metric is `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)`** — `eta` is
>    the FLAT KKT Minkowski form of the slice (`h_2(C_u) ~ R^{3,1}`, `det_2` mostly-minus,
>    timelike `x_0 = beta+gamma`), `h` the matter perturbation. **The cone-Hessian curvature
>    is NOT the spacetime metric.**
> 2. **The literal "cone-Hessian IS the metric" thesis is FALSIFIED (NULL).** Its M=0 vacuum
>    is the non-Einstein static product `R_time x H^3` (Ricci-endomorphism `{0,-1,-1,-1}`,
>    `R=-3`, `S != 0`). The cone-Hessian object is now re-cast as the **SOURCE / information
>    structure** (its `V_0<->V_{1/2}` cross-terms `2Re((x2 x1)x3)` source `h`), NOT the
>    gravitational field.
> 3. **M=0 gives FLAT `eta` (`R=0`), and this flatness is DERIVED from the KKT `det_2`
>    Minkowski form (52-kkt), NOT an inserted Lambda.** The "Lambda=0 inserted by
>    center-subtraction / circularity tripwire on the vacuum" framing is **STRUCK**. There is
>    **NO Lambda tripwire** in Phase 72 (or Phase 73).
> 4. **`det_2`/`det_3` splice-consistency = PASS:** `h` is a valid symmetric (0,2) perturbation
>    of the Lorentzian `eta_bg` in the same 4x4 frame; small matter preserves signature (1,3).
>
> **The one substantive correction (matter-on-flat).** Everywhere the prior version computed
> curvature against a curved/cone-Hessian baseline — "M=0 is `R_time x H^3`", "`R(center)=-3`",
> "pure-Lambda at the center", "Lambda-vs-matter against a curved fixed V_0-background", "Cartan
> baseline" — that baseline framing is exactly what 70.1 FALSIFIED. It is corrected throughout
> to: **the M=0 spacetime baseline is FLAT `eta` (`R=0`), DERIVED from KKT `det_2`.** The
> matter-sourced curvature is the curvature of `g = eta + h(x; M)` with matter ON, where `h` is
> sourced by the `V_0<->V_{1/2}` `det_3` cross-terms. (The new operational definition of
> `h_mu_nu(x; M)` is in **§ The h_mu_nu(x; M) operational definition (Phase-72 crux)** below.)
>
> **What is PRESERVED verbatim (correct, hard-won, do NOT re-derive or weaken):** the matter
> channel `2*Re((x2*x1)*x3)` as the unique `V_0<->V_{1/2}` coupling; the SSOT
> `code/bulk_geometry_verification.py det_3` (octonion_algebra.py BANNED); the Peirce index map;
> the cross-term ON/OFF off-switch as the decisive control; the all-three-slots-populated
> non-vacuity requirement; the measured performance cliffs (>200s symbolic-matter inverse; ~19s
> Totaro dim-4; ~150s executor watchdog); the n=4 GR Ricci decomposition (R + traceless-Ricci S +
> Weyl C); EXACT over Q on all verdicts; Totaro Cor 2.3.
>
> **Do NOT re-litigate the metric selection** (70.1 settled it: `eta+h`, human-ratified). **Do NOT
> relabel a homogeneous/flat result to fake survival** (`fp-relabel`). **Do NOT count a pure-Lambda
> or matterless piece as sourcing** (`fp-lambda-as-sourcing`). The superseded `PHASE-RECOVERY.md`
> in this directory predates 70.1 — its "Lambda=0 tripwire / flatness inserted / construction-(ii)
> conditional" language must NOT be carried forward.

## Summary

The computational method is LOCKED and the engine is built (`code/bulk_geometry_verification.py`, 2568 lines, ALL_PASS exit 0). This is NOT a method-selection phase; it is an *isolation* phase. Following the Phase-70.1 verdict, the physical spacetime metric is the construction-(ii) bridge `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)`: `eta` the FLAT KKT-Minkowski background (the slice's own `det_2` causal form, `R=0`, DERIVED — not inserted), and `h_mu_nu(x; M)` the matter perturbation. At `M=0` the perturbation vanishes (`h=0`, `g=eta` exactly over Q) so the baseline spacetime is FLAT. The Phase-72 question is therefore sharp: **does turning on matter `M` in `V_1 ⊕ V_{1/2}` source a NONZERO curvature of `g=eta+h(x;M)` through the `det_3` cross-term `2Re((x2 x1)x3)`, and does switching the cross-term OFF (block-diagonal norm) remove it?**

Two subtleties carry over from Phase 71 and must be respected, but neither is a baseline ambiguity any more (70.1 fixed the baseline as flat `eta`):

1. **The cone-Hessian is the SOURCE structure, not the metric.** Phase 71 found the *cone-Hessian* slice geometry is position-dependent at `M=0` (its `R = R(det_2)` varies across `det_2` leaves). That matterless cone-Hessian variation is **not** the spacetime curvature — the spacetime metric is `g=eta+h`, whose `M=0` value is flat. So "matterless det_2-variation of the cone-Hessian" is no longer a confound for the *spacetime* curvature; it is the behaviour of the source field. The Phase-72 claim is strictly about the **M-dependence of `h` (hence of `g`'s curvature)** generated through the cross-terms.
2. **V_1 (alpha) is inert; V_{1/2} is the active matter channel** — `alpha` (index 0) is absent from the octonion triple `2Re((x2 x1)x3)`, structurally explaining the Phase-71 V_1-inertness.

The matter-sourcing question reduces to four exact-over-Q computations on the dim-4 `h_2(C_u)` sub-slice (engine indices `{1,2,3,10} = (beta,gamma,p,q)`): **(DERV-02)** the curvature of `g=eta+h(x;M)` as an explicit function of `M`; **(VALD-04, re-framed)** the n=4 GR Ricci decomposition (R, traceless-Ricci `S_munu`, Weyl `C_munu`) of `g`, to confirm `M=0` gives flat `g` (`R=0`, `S=0`, `C=0`) and to expose the structure of the `M!=0` curvature — **NO Lambda tripwire, NO pure-Lambda-at-center baseline subtraction**; **(CALC-03)** the cross-term ON/OFF test, feeding the SAME `M!=0` through the full cubic norm and through a block-diagonal norm that zeroes the `V_0<->V_{1/2}` cross-term; **(CALC-04)** the `||M||` / `det_2` scaling law via a series in matter amplitude. Matter enters ONLY through the det cross-term `2*Re((x2*x1)*x3)`, so the cross-term off-switch is a clean, decisive control.

**Primary recommendation:** Extend the existing engine API. Populate the matter indices (`V_1 alpha = {0}`; `V_{1/2} = {11..26}`) in the `delta` argument of `offcenter_slice_metric` / `_offcenter_subs`, **holding the V_0-background at the center** (so `M=0 ⟹ h=0 ⟹ g=eta` exactly — the DERIVED flat KKT vacuum). Keep ONLY the 4 slice coords `{beta,gamma,p,q}` symbolic, **substitute all matter to small rationals BEFORE any `Matrix.inv()`** (the symbolic-matter inverse is the measured >200s cliff), build `g = eta + h(x;M)`, and run Totaro Riemann (~19s exact) on `g`. Decide matter-sourcing by the conjunction: (i) cross-term OFF kills the `M`-curvature of `g`; (ii) the curvature of `g` -> 0 as `||M|| -> 0` (recovering flat `eta`); (iii) the `M!=0` curvature carries traceless-Ricci / Weyl structure (genuine geometry, not a coordinate artifact). Anything weaker — a curvature that survives the off-switch, or that does not vanish as `||M||->0` — means matter does NOT source the spacetime curvature; report "not matter-sourced" (NEGATIVE-RESULT-IS-SUCCESS) and do NOT proceed to Phase 73.

## User Constraints

No CONTEXT.md exists for this phase (no `/gpd:discuss-phase` was run). The binding context is: the **Phase-70.1 human-ratified verdict** (`.gpd/phases/70.1-.../70.1-01-SUMMARY.md` — AUTHORITATIVE re-scope) + the ROADMAP phase spec + the v17.0 project contract (`claim-matter-sourcing`) + the LOCKED v17.0 conventions (`.gpd/CONVENTIONS.md`, 18/18 set, with the §6 "center is Einstein, Lambda<0" item FALSIFIED for the cone-Hessian per 70.1 — see below) + the VERIFIED Phase-71 findings (`.gpd/phases/71-a-homogeneity-kill-gate/71-VERIFICATION.md`). Treat all of these as locked decisions:

- **The physical spacetime metric is `g = eta + h` (Phase-70.1, human-ratified).** `eta` = the FLAT KKT-Minkowski form (`det_2`, mostly-minus, timelike `x_0=beta+gamma`); `h` = the matter perturbation. **The cone-Hessian curvature is the matter SOURCE / information structure, NOT the gravitational field.** Do NOT re-open this selection.
- **The M=0 spacetime baseline is FLAT `eta` (`R=0`), DERIVED from the KKT `det_2` form, NOT inserted.** There is **NO Lambda tripwire, NO "which Lambda reference", NO pure-Lambda-at-center baseline subtraction.** The only thing that counts as matter-sourcing is the M-dependent curvature of `g=eta+h` generated through the cross-terms.
- **Method is LOCKED.** Totaro closed-form curvature on the certified `det_3` SSOT, applied to the spacetime metric `g=eta+h`. Do NOT survey alternative formalisms or alternative curvature engines. (Engine = `code/bulk_geometry_verification.py`.)
- **det SSOT is LOCKED.** `det_3` with cross-term `2*Re((x2*x1)*x3)` (Phase-64.1-corrected, F_4-invariant via CH + 324/324). NEVER `code/octonion_algebra.py` (buggy `(x1 x2) x3` order, float-only, 0.67 associator gap).
- **Signature bridge construction (ii) is LOCKED.** `g_munu(x) = eta_munu + h_munu(x)`; `eta` from `h_2(C_u)`'s `det_2`; `g(center, M=0) = eta` EXACTLY (`h=0`). Construction (i) (Wick via u=e7) is REJECTED.
- **EXACT over Q on all decisive verdicts.** Ranks via `sympy.Matrix.rank()`, never numpy float rank. `fp-float-decisive` is FORBIDDEN.
- **kappa, Lambda are GLOBAL constants for Phase 73, NOT here.** Phase 72 only needs to establish matter-SOURCING (curved-or-not + cross-term-sourced-or-not). The numeric value of any cosmological constant is out of scope; the M=0 vacuum is flat regardless.
- **Phase-71 finding (VERIFIED), re-read through 70.1:** the *cone-Hessian* (source) geometry is position-dependent at `M=0` (`R = R(det_2)`); `V_1` (index 0) is INERT; `V_{1/2}` (indices 11..26) is the active matter channel; the genuine basepoint modulus is **`det_2`** (the `Stab_{V_0}=Spin(9,1)` invariant), not `rho_J` (they coincide for single-direction perturbations). This describes the SOURCE field; the SPACETIME metric `g=eta+h` is flat at `M=0`.
- **FORBIDDEN PROXIES (contract):** `fp-lambda-as-sourcing` (a pure-Lambda / matterless piece is NOT matter-sourcing — and the M=0 flat `eta` is DERIVED, not counted as sourcing); `fp-wrong-cross-term` (wrong octonion association); `fp-float-decisive` (verdicts EXACT over Q); `fp-coordinate-curvature` (a coordinate/embedding artifact is not intrinsic gravity); `fp-assume-einstein` (no factor inserted to force `Ric ∝ g`; this proxy formally belongs to Phase 73 but guard against creeping Einstein-fitting here). `fp-relabel` (do NOT relabel a flat/homogeneous result as survival) and `fp-ensemble-gravity` (NO observers-make-gravity / Jacobson thermodynamic argument) remain in force.
- **Backtracking trigger (honest negative):** if the curvature of `g=eta+h` with `M!=0` (a) survives the cross-term off-switch, or (b) does not vanish as `||M||->0`, or (c) is a pure coordinate/embedding artifact (no traceless-Ricci/Weyl structure), report "not matter-sourced" and do NOT proceed to Phase 73.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| `.gpd/phases/70.1-.../70.1-01-SUMMARY.md` (ref-70.1-verdict) | prior artifact (AUTHORITATIVE re-scope) | The human-ratified verdict that fixes the metric (`g=eta+h`), derives the flat M=0 vacuum from KKT, strikes the Lambda tripwire, and re-casts the cone-Hessian as the source. **Supersedes the pre-70.1 baseline framing of this very file.** | READ IN FULL before planning | plan, execution, verification |
| `~/scratch/get-physics-done/paper6-bulk-geometry-prompt.md` (ref-prompt) | authoritative milestone spec | Defines Phase B targets (a)(b)(c): M=0 flat; cross-term off-switch removes M-curvature; scale vs \|\|M\|\| and rho_J. The negative-result-is-success reporting discipline ("do not soften", "curved-but-not-Einstein is acceptable") is binding. | READ IN FULL before planning | plan, execution, verification |
| Faraut & Koranyi, *Analysis on Symmetric Cones* (1994) (ref-faraut-koranyi) | foundational reference | Cone metric g_X = Hess(-log det); inverse g^{pq} = P(X) (quadratic representation). Grounds the cone-Hessian SOURCE structure and `det_2` modulus. | CITE for g_X, g^{pq}=P(X) | plan (mechanism), verification (g^{pq} cross-check) |
| McCrimmon, *A Taste of Jordan Algebras* (2004) (ref-mccrimmon) | reference | Peirce decomposition under E_11, cubic norm, quadratic representation P(X). Grounds the V_1/V_{1/2}/V_0 split and the cross-term coupling. | CITE for Peirce + cubic norm structure | plan (mechanism) |
| Totaro, arXiv:math/0401381, Cor 2.3 (ref-totaro) | method reference | The Hessian-curvature closed form R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq); pins the Riemann sign. Used for the curvature of `g=eta+h` (see operational note). | CITE for the curvature engine + sign | plan, execution (engine SSOT) |
| `code/bulk_geometry_verification.py` (warm engine, ALL_PASS) | prior artifact (EXTEND) | The decisive computation surface. `_offcenter_subs`/`cone_hessian_offcenter`/`offcenter_slice_metric`/`minkowski_reduction`/`cubic_form_C`/`totaro_riemann`/`ricci_scalar`/`second_fundamental_form` are the API Phase 72 EXTENDS (put **matter** in `delta`; add a block-diagonal-det variant; add a Ricci-decomposition routine; compute curvature of `g=eta+h`). Do NOT rebuild. | EXTEND in place; reuse `det_3` SSOT | execution, verification |
| `.gpd/phases/71-a-homogeneity-kill-gate/71-VERIFICATION.md` | prior artifact (VERIFIED) | V_1 inert; V_{1/2} active; det_2 is the genuine modulus; concrete matterless cone-Hessian R values (now understood as SOURCE-field behaviour, regression anchors for the engine). | READ; use values as engine regression anchors | plan, execution, verification |
| `~/scratch/get-physics-done/rho_directional_derivatives.py` (ref-peirce-coupling) | reference (real-only) | The off-center / rho_J expansion STRUCTURE for CALC-04 (series in matter amplitude). CAUTION: real-only cross-term `2*d1*d2*d3` — use the expansion strategy ONLY, recompute the octonionic cross-term from the engine `det_3`. | REUSE expansion strategy; NOT its det | execution (CALC-04 scaling) |
| `~/scratch/get-physics-done/peirce_coupling.py` (ref-peirce-coupling) | reference (numpy/float) | Peirce decomposition under E_11. Establishes that x1 (V_0) couples to E_11 ONLY through the cubic trilinear, never bilinear — exactly the cross-term mechanism. NOT on the decisive path (float). | READ for intuition; do NOT import on decisive path | plan (mechanism) |
| `~/repos/blog/research/qualia-fixed-point/h3o_tower.py` (ref-h3o-tower) | benchmark | Corrected cubic-norm benchmark (cross-term association). Provenance cross-check for `det_3` if needed. | OPTIONAL cross-check of det_3 | verification |

**Missing or weak anchors:**

- **No external literature anchor for the matter-sourcing CLAIM.** A focused literature pass (Totaro, Faraut-Koranyi, "Curvatures of metric Jordan algebras" arXiv:2309.02682) found precedent ONLY for the matterless cone-Hessian side: every formally real Jordan algebra admits a Jordan-Einstein metric of negative scalar curvature (corroborates the cone-Hessian SOURCE geometry's negative curvature — NOT the spacetime metric, which is flat at M=0). I found NO precedent for off-diagonal-Peirce / non-idempotent ("matter") content SOURCING a perturbation `h` of a flat Minkowski slice metric via the cubic cross-term. This is the novel contribution. Validation must be internal (limiting case `||M||->0 ⟹ flat eta`, cross-term off-switch, exact-over-Q reality), NOT literature-benchmarked. Confidence on the OUTCOME is MEDIUM, not HIGH.
- **STALE-REFERENCE CONFLICT to flag to the planner.** The project-level `.gpd/research/METHODS.md`, `PITFALLS.md`, and `COMPUTATIONAL.md` (written pre-Phase-64.1/70/71) repeatedly name `code/octonion_algebra.py` `det_3` as the SSOT. This is SUPERSEDED: the v17.0 CONVENTIONS lock and the warm engine make `code/octonion_algebra.py` BANNED (buggy order, float, 0.67 gap) and the SSOT is `code/ring_lemma_verification.py det_3` == `code/bulk_geometry_verification.py det_3` (`2*Re((x2*x1)*x3)`). Where the project research and the convention lock disagree, **the convention lock + warm engine win.** Use the engine's `det_3`.
- **FALSIFIED convention to flag (non-blocking, from 70.1).** `.gpd/CONVENTIONS.md §6` and `.gpd/research/METHODS.md` Validation-(a) state "center is Einstein with negative Ricci, Lambda<0" (the Cartan/pure-Lambda reading). Phase 70.1 FALSIFIED this **for the cone-Hessian** (its M=0 center is the non-Einstein `R_time x H^3`, `{0,-1,-1,-1}`). It is moot for the SPACETIME metric `g=eta+h` (flat at M=0). A notation-coordinator follow-up is pending (non-blocking). **Do NOT rely on the "center is Einstein/Cartan" baseline anywhere in Phase 72.**
- **rho_J vs det_2 wording.** The contract/roadmap say "rho_J(X_bg)"; the Phase-71 verifier flagged `det_2` (the `Stab_{V_0}=Spin(9,1)` invariant) as the strictly-correct modulus. They coincide for single-direction perturbations. Phase 72 should report the scaling law against `det_2` and NOTE the coincidence; this sharpens, not changes, CALC-04.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Physical spacetime metric | `g_munu(x) = eta_munu + h_munu(x)` (construction (ii)); `eta` = FLAT KKT-Minkowski; M=0 ⟹ h=0 ⟹ g=eta (R=0, DERIVED) | cone-Hessian-IS-metric [FALSIFIED, Phase 70.1] | Phase 70.1 verdict; CONVENTIONS.md §1 |
| Metric signature (slice/spacetime) | mostly-minus (-,+,+,+) Lorentzian; eta = diag(+1,-1,-1,-1); timelike x_0 = beta+gamma | (+,-,-,-) | CONVENTIONS.md §1; 52-kkt |
| Source structure (cone-Hessian) | Riemannian, positive-definite; g_X = Hess(-log det) — the SOURCE / information structure, NOT the spacetime metric | (used as the metric) [FALSIFIED] | Faraut-Koranyi; Phase 70.1 |
| Potential | Phi = -log det (FIXED; do NOT mix with bare det) | — | CONVENTIONS.md §4 |
| det / cubic norm | Freudenthal `det_3`, cross-term `2*Re((x2*x1)*x3)`; SSOT = engine `det_3` | (x1 x2) x3 [BANNED, buggy] | CONVENTIONS.md §0,§3 |
| Riemann (lower idx) | R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq), C_ijk = Phi_{,ijk} | — | Totaro Cor 2.3 |
| Ricci tensor | Ric_jl = g^{ik} R_ijkl (contract 1st & 3rd slots) | — | engine §12 header |
| Ricci scalar | R = g^{jl} Ric_jl = g^{ik}g^{jl} R_ijkl | — | engine §12 header |
| M=0 spacetime curvature | `R = 0` (flat eta), DERIVED from KKT det_2 — NOT R=-3, NOT pure-Lambda, NOT R_time x H^3 | R=-3 / Cartan [SUPERSEDED: that is the cone-Hessian SOURCE, not the metric] | Phase 70.1 verdict |
| Units | natural ħ=c=k_B=1; EXACT over Q on all verdicts | float [FORBIDDEN on verdicts] | CONVENTIONS.md §2 |
| Center (for the cone-Hessian source) | I/3 (F_4-symmetric, rho_J=0); det(I/3)=1/27 | — | CONVENTIONS.md §3 |
| Peirce (under E_11=diag(1,0,0)) | V_1(1)={0} alpha; V_0(10)={1..10}=h_2(O); V_{1/2}(16)={11..26}. Slice h_2(C_u)(4)={1,2,3,10}=(beta,gamma,p,q) | — | engine §11, CONVENTIONS.md §3 |
| Genuine basepoint modulus (of the source) | **det_2** (Stab_{V_0}=Spin(9,1) invariant); rho_J coincides for single-direction perturbations | rho_J [contract wording] | Phase-71 verifier |

**CRITICAL: All equations below use these conventions.** The spacetime metric is `g=eta+h` (mostly-minus, flat at M=0). The Riemann sign is the Totaro/engine convention. The `det_3` cross-term is the corrected `2*Re((x2*x1)*x3)`. The GR Ricci decomposition below is an algebraic identity in the curvature tensor (signature-agnostic), with indices raised by the slice metric `g_munu`.

Convention loading: see agent-infrastructure.md Convention Loading Protocol. Run `gpd --raw convention check` to confirm 18/18 (note §6 is FALSIFIED for the cone-Hessian — non-blocking, moot for `g=eta+h`).

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| det_3(X) = abg - a\|x1\|^2 - b\|x2\|^2 - g\|x3\|^2 + 2 Re((x2 x1) x3) | Freudenthal cubic norm | engine `det_3` (l.351) | The SOURCE object; matter enters via the cross-term |
| **g_munu(x) = eta_munu + h_munu(x)** | physical spacetime metric (construction (ii)) | Phase 70.1; engine `offcenter_slice_metric` (l.1109) | **THE metric whose curvature is decisive**; flat at M=0 |
| **h_munu(x;M) = [Hess(-log det_3)\|_{V_0,slice}(X_bg+M)] - [same at (M=0, center)]** | the matter perturbation (centered cone-Hessian deviation) | engine `offcenter_slice_metric` (l.1114) | The matter-sourced field; `h=0` at (M=0, center) |
| eta = diag(+1,-1,-1,-1) (52-kkt det_2 Minkowski) | flat KKT background | engine `_eta_minkowski` (l.1144); 52-kkt | The DERIVED flat M=0 vacuum (R=0) |
| Phi = -log det_3(X_bg + x) | cone potential (for the SOURCE Hessian) | Faraut-Koranyi | Supplies h via Hess(Phi) |
| C_ijk = Phi_{,ijk} (totally symmetric) | cubic-form tensor | engine `cubic_form_C` (l.1319) | Totaro Riemann datum (for curvature of g) |
| R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq) | Totaro Riemann | engine `totaro_riemann` (l.1334); Totaro Cor 2.3 | DERV-02 Riemann of the spacetime metric g (see operational note) |
| Ric_jl = g^{ik} R_ijkl; R = g^{jl} Ric_jl | Ricci tensor & scalar | engine `ricci_scalar` (l.1376) | DERV-02 / VALD-04 |
| **Matter cross-term** = 2 Re((x2 x1) x3), x1 in V_0, x2,x3 in V_{1/2} | V_0<->matter coupling | engine `det_3` | the SOLE channel for M; the off-switch target |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Centered cone-Hessian deviation `h := H_bg(X_bg+M) - H_center` | Defines the matter perturbation of flat eta; h=0 at (M=0,center) | h_munu(x;M) operational defn | Phase 70.1; engine `offcenter_slice_metric` |
| Curvature of `g = eta + h(x;M)` (Totaro closed form on the slice) | Riemann of the spacetime metric from its 3rd-derivative cubic form | DERV-02 (R_ijkl of g) | Totaro arXiv:math/0401381 |
| GR Ricci decomposition (scalar + traceless-Ricci + Weyl), n=4 | Confirms M=0 is flat (R=S=C=0); exposes M!=0 structure | VALD-04 (re-framed) | Wikipedia Ricci decomposition; Besse, *Einstein Manifolds* |
| Polarization of the cubic norm `polarize_d`, d(X,X,X)=6 det_3 | Directional derivatives organize the M-expansion of h | CALC-04 | engine `polarize_d` (l.403) |
| Block-diagonal norm construction (zero the cross-term) | Decouples V_0 from matter in det ⟹ removes the M-source of h | CALC-03 off-switch | this phase (novel control) |
| Series in matter amplitude t (M = t·M0, expand to low order) | Scaling law: curvature(t) ~ t^k; avoids symbolic-matter inverse | CALC-04 | rho_directional_derivatives.py (strategy only) |
| `||M||->0` limit recovering flat eta | The decisive limiting case (NOT a Lambda baseline subtraction) | ISOLATION | this phase (Phase-70.1-mandated) |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| ------------- | --------------- | ------------------ | -------------- | ----------------------- |
| Series in matter amplitude t (M = t·M0) | t = \|\|M\|\| | small-matter neighborhood of the flat eta vacuum | EXACT per order (det cubic => finite jet in t) | Carry M rational and compute curvature exactly at several finite M (no truncation) |
| Linear-in-M (leading order of h, hence of curvature) | t | leading scaling law; feeds the Phase-73 linearized-Einstein test | drops O(t^2) | full exact curvature at finite rational M |

**Note (det cubic => no resummation).** `-log det` has a finite-order rational Taylor jet around any interior point in the *matter* directions; the expansion TERMINATES. The smallness is `||M||` (deviation from the flat eta vacuum), NEVER the spacetime coordinate x (which is O(1) and is the wrong expansion variable — Phase-71 lesson).

## The h_mu_nu(x; M) operational definition (Phase-72 crux)

> **!!! CORRECTED in Plan 72-01 execution (2026-06-01) — the CENTERED-H0 definition below was a TRAP; use B1.**
> The centered definition `h := H_source(x;M) - H0` with `H0 = diag(9,9,18,18)` CONSTANT (line 181 below)
> satisfies `h=0` only AT the center POINT — it is NONZERO for `x != center`, so at `M=0` the metric
> `g = eta + h(x;0)` is the matterless CONE-HESSIAN metric, which is CURVED (verified `R[g](M=0)=17496` at
> the center, a large rational off-center). That is exactly the cone-Hessian-is-metric framing **Phase 70.1
> FALSIFIED** (forbidden proxy `fp-lambda-as-sourcing`). A curved `M=0` was the disconfirming observation
> in Task 2. **The human-ratified correction (B1, matter-on-flat), pinned by the 70.1 verdict:** subtract the
> matterless reference cone-Hessian **AT THE SAME x** (V_0 background partner retained in BOTH terms):
> ```
> h(x; M) := H_source(x; bg + M) - H_source(x; bg-only)        # B1: matter-induced deviation
> ```
> Then `h(x; M=0) == 0 IDENTICALLY in x` (verified over Q) ⟹ `g = eta_bg` over a NEIGHBOURHOOD ⟹
> `R[g](M=0) = 0` (the genuine FLAT baseline, DERIVED from KKT `det_2`). The curvature engine
> `spacetime_curvature_of_g` and `hand_rolled_riemann_of_g` (Section 13) now use B1: `h` from the
> difference of cone-Hessians, the cubic form `C` from the **DIFFERENCE potential** `Phi_bgM - Phi_bg`,
> and indices raised by `g^{-1}=(eta+h)^{-1}`. The Totaro-`g^{-1}` route and a hand-rolled Levi-Civita
> Riemann of `g` AGREE EXACTLY over Q (mandatory cross-check PASS). The text below is RETAINED as the
> honest pre-correction record; read `H0` as `H_source(x;bg-only)` (function-of-x), NOT the constant.

**This section answers the one new methodological question the 70.1 re-frame creates: what IS `h_mu_nu(x; M)`, operationally, on the flat `eta` background?** It must satisfy (a) `h = 0` at `M=0` (so `g=eta` flat — and per B1, IDENTICALLY in x, not just at the center point); (b) `h` is sourced by matter `M` in `V_1/V_{1/2}` through the cross-term `2Re((x2 x1)x3)`; (c) it is computable EXACTLY over Q with the warm engine.

### Definition (CORRECTED to B1 — see the banner above)

The engine implements the OLD centered split in `offcenter_slice_metric(delta, ...)` (l.1109–1147) and `minkowski_reduction` (l.1173). Plan 72-01 **does NOT use that centered `h` on the decisive path**; it uses the B1 matter-induced deviation (matterless reference AT THE SAME x). Phase 72's contribution is to **read the `delta`/`matter_delta` argument as the MATTER content** (not a V_0-background move) while **holding the V_0-background partner fixed in BOTH the matter-ON and matter-OFF cone-Hessians (so it cancels)**:

```
X(x; M) = X_bg(x) + M,               X_bg(x) = I/3 + (fixed V_0 partner), slice coords {beta,gamma,p,q} live,
                                       M in V_1(alpha={0}) ⊕ V_{1/2}({11..26})  [matter only]

H_source(x; .) = Hess_{slice}( -log det_3 )  evaluated at .            # cone-Hessian SOURCE, 4x4 over slice coords

h_munu(x; M)  := H_source(x; bg+M) - H_source(x; bg-only)   # B1 (FIXED): matterless reference AT THE SAME x
                                                            #   [TRAP, do NOT use: H_source(x;M) - H0 const]
g_munu(x; M)  := eta_munu + h_munu(x; M)        # physical spacetime metric (eta = KKT Minkowski, l.1152)
```

with, in the `det_3` matrix layout, `x1 = X[2][1]` (V_0 octonion, carries the slice `p,q` and the V_0 internal sector), `x2 = X[0][2]`, `x3 = X[1][0]` (V_{1/2} octonions, carry the matter). **Matter `M` enters `H_source` ONLY through the cross-term `2Re((x2 x1)x3)` of `det_3`** (the unique `V_0<->V_{1/2}` channel); `alpha` (V_1) multiplies the diagonal norms and is absent from the triple ⟹ V_1-inertness (CONFIRMED in 72-01 Task 3: V_1-only matter leaves `R[g]=0`).

### Why this satisfies (a)/(b)/(c)

- **(a) Flat at M=0 (B1: over a NEIGHBOURHOOD, not just the center point).** With `M=0`, `H_source(x;bg+0) == H_source(x;bg)` so `h(x;0) = 0` IDENTICALLY in x ⟹ `g = eta_bg` everywhere ⟹ `R[g](M=0)=0` (confirmed exact over Q at the center, off-center, and with the bg partner ON — 72-01 Task 2.0/2.0b/2.0c). `minkowski_reduction` confirms `g-eta=0` and signature (1,3) at the center (l.1194). **This flatness is DERIVED from the KKT `det_2` Minkowski form, not inserted** (70.1, Correction 3): `eta` IS the slice's own causal form; the B1 subtraction is a deviation-from-matterless bookkeeping carrying NO circularity and NO Lambda tripwire. [The OLD centered `H0`-subtraction gave `h=0` only AT the center point ⟹ a CURVED `M=0` — the falsified framing.]
- **(b) Sourced by matter through the cross-term.** Turning on `M` in `V_{1/2}` makes the cross-term `2Re((x2 x1)x3) != 0`, which feeds `det_3`, hence `Phi=-log det_3`, hence `H_source(bg+M)`, hence `h = H_source(bg+M) - H_source(bg) != 0`. The cross-term OFF-switch (block-diagonal norm) removes exactly this channel ⟹ `h` loses its `M`-source (the decisive off-switch is Plan 72-02).
- **(c) Exact over Q.** Everything is rational once matter is substituted to rationals: `H_source` is `Hess(-log det_3)` with the slice coords symbolic and matter rational (measured ~2s inverse / ~few-s Totaro curvature; the hand-rolled Levi-Civita cross-check ~35s — watchdog-safe with the evaluate-then-invert strategy).

### Which curvature is decisive: curvature of g=eta+h (full nonlinear), with the linearized-in-M piece feeding Phase 73

- **Decisive for Phase 72 (matter-SOURCING):** the **intrinsic curvature of the full spacetime metric `g=eta+h(x;M)`** — `R_ijkl[g]`, `Ric[g]`, `R[g]` via the Totaro engine applied to `g` (not to the bare cone-Hessian). The verdict is the conjunction (off-switch kills it; `||M||->0` recovers flat eta; traceless-Ricci/Weyl structure present). Use the FULL (nonlinear-in-h) curvature here, because matter-sourcing is a statement about `g` being genuinely curved when `M!=0`, and the off-switch/limit controls are cleanest on the exact `g`.
  - **Operational engine note (IMPORTANT for the planner).** The engine's `totaro_riemann` is the Hessian-metric closed form `R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq)`, which is exact **for a Hessian metric** `g = Hess(Phi)`. The spacetime metric `g=eta+h` is a Hessian metric **plus a constant** `eta` (since `eta` is constant, `Hess(eta+h) = Hess(h)`-as-an-additive-constant-shift does NOT change 2nd/3rd derivatives — the cubic form `C_ijk = g_{,ijk} = h_{,ijk} = H_source_{,ijk}` is identical). Concretely: because `eta` is a CONSTANT (coordinate-independent) background, the 3rd-derivative cubic form `C` of `g` equals that of the cone-Hessian source `H_source`; only the INVERSE metric differs (`g^{pq}` raised with `eta+h`, not with `H_source`). So the decisive curvature is computed as `R_ijkl = -(1/4) (g^{-1})^{pq}(C_jlp C_ikq - C_ilp C_jkq)` with **`C` from the cone-Hessian potential** and **`g^{-1} = (eta+h)^{-1}`** — a one-line change to the existing pipeline (raise indices with `g=eta+h`, not with `H_source`). The planner must make this explicit: *the curvature is the curvature of `g=eta+h`, which differs from the bare cone-Hessian curvature precisely through the index-raising metric.* (This is also the cleanest way the prior "cone-Hessian curvature" computation is corrected: same `C`, different `g^{-1}`.)
  - **Caveat to verify (planner: schedule a cross-check).** The Totaro closed form assumes the metric is *exactly* a Hessian metric `g=Hess(Phi)`. `g=eta+h` is `Hess(Phi) + eta` with `eta` constant — for the 3rd-derivative `C` this is identical, but the derivation of the closed form also uses the relation between `g`, `g^{-1}` and `C` (the `f_ijkl=0` cubic property). To be safe, **cross-check a few `R_ijkl[g]` components via the hand-rolled Christoffel/Riemann path** (`h3_constant_curvature`-style, l.1213) computed directly from `g=eta+h` — this is independent of the Totaro shortcut and guards against mis-applying the closed form to `eta+h`. If the two agree exactly over Q, the Totaro-with-`g^{-1}` route is validated; if not, use the hand-rolled Riemann of `g=eta+h` as primary.
- **Feeds Phase 73 (linearized-Einstein test):** the **linearized-in-M piece** `h^{(1)}_munu = ∂_t h(x; t·M0)|_{t=0}` and the linearized curvature `R^{(1)}` are what Phase 73 tests against `box h_bar ~ kappa T`. Phase 72 should EMIT `h(x;M)` (and its leading-order-in-`||M||` part) so Phase 73 can build `h_bar = h - (1/2)eta·tr_eta(h)` and apply the wave operator. Phase 72 does NOT do the Einstein test — it only establishes that `M` sources a genuine curvature of `g`.

### Consistency with the 70.1 splice-consistency PASS

70.1 step 9 confirmed (exact over Q): `h` is a valid symmetric (0,2) perturbation of the Lorentzian `eta_bg` in the same 4x4 frame; small `M` preserves signature (1,3); large `M` eventually flips signature (the perturbative regime boundary). Phase 72 must therefore **stay in the small-`||M||` regime where `g=eta+h` keeps signature (1,3)** (check `g`'s eigenvalue signs over Q at each chosen `M`), and report the curvature there. This is the regime where `g=eta+h` is a bona fide Lorentzian spacetime metric — exactly the splice-consistency PASS condition.

## Standard Approaches

### Approach 1: Matter-on-flat — curvature of g=eta+h(x;M) + cross-term off-switch (RECOMMENDED, LOCKED)

**What:** Extend the warm engine. Hold the V_0-background at the center; put **matter** in `delta` (V_1 alpha={0}, V_{1/2}={11..26}); keep slice coords {beta,gamma,p,q} symbolic; substitute matter to rationals BEFORE inverting; build `g = eta + h(x;M)` via `offcenter_slice_metric`; compute the intrinsic curvature of `g` (Totaro `C` from the cone-Hessian potential, indices raised with `g=eta+h`; cross-checked by hand-rolled Riemann of `g`); decompose; compare full-det vs block-diagonal-det at the SAME M; take `||M||->0` recovering flat eta.

**Why standard:** It is the engine's measured-working path (~19s exact with matter rational, dim-4). It is the only path consistent with the Phase-70.1 verdict (g=eta+h is the metric; M=0 is flat). The four sub-questions map 1:1 onto contract requirements DERV-02/VALD-04/CALC-03/CALC-04.

**Track record:** The matterless cone-Hessian version (Phase 71) ran exactly over Q, ALL_PASS exit 0; the `g=eta+h` split, `h=0`-at-center, and signature (1,3) were reproduced in Phase 70.1 (step 6 + step 9, exact over Q). Matter-on was spot-checked in Phase 71/72-01 (V_1 inert; V_{1/2} sources a nonzero cross-term `-13/315`; all three slots, e_4 content). The block-diagonal-det variant is new but is a one-line change to `det_3` (drop the cross-term).

**Key steps (executable recipe):**

1. **Mechanism + index audit (cheap, do first).** Confirm the Peirce index map (V_1={0}, V_{1/2}={11..26}, V_0={1..10}, slice={1,2,3,10}) and that the cross-term `2*Re((x2*x1)*x3)` is the ONLY det term mixing x1 (V_0) with x2,x3 (V_{1/2}). Re-derive the (V_{1/2},V_{1/2},V_0) polarization block from `polarize_d` on the Peirce basis and confirm it is nonzero on genuinely octonionic M (e_4..e_7 components). [DERV-02 prereq; PITFALLS Pitfall 2.5/2.8]

2. **DERV-02: build g=eta+h(M) and its curvature as an explicit function of M.** Build `delta_M` = chosen V_{1/2} (and optionally V_1) matter (rational), slice symbolic. `MG = offcenter_slice_metric(delta_M)` gives `{g, h, eta_bg, ...}`. Then compute the curvature of `g`: cubic form `C` from the cone-Hessian potential (slice-coord 3rd derivatives), `ginv = g.inv()` (4x4, ~3s with matter rational; raise indices with **g=eta+h**, NOT the bare cone-Hessian), `R = totaro_riemann(ginv, C, 4)`, `Ric`, `Rscalar`. Assert `riemann_symmetry_ok`. **Cross-check a few R_ijkl[g] via hand-rolled Christoffel/Riemann of g** (independent of the Totaro shortcut — see the operational engine note above). ~19–40s total.

3. **VALD-04 (re-framed): flat-baseline confirmation + M-structure.** (a) At `(M=0, center)`: confirm `g=eta`, `R[g]=0`, `S_munu=0`, Weyl`=0` — the FLAT KKT vacuum (DERIVED, **NO Lambda, NO R=-3**). (b) For `M!=0`: compute the Ricci scalar `R[g](M)`, the traceless Ricci `S_munu = R_munu - (R/4) g_munu`, and the Weyl `C_munu` (n=4 formulas below). Genuine M-sourcing of *spacetime* curvature requires `R[g](M) != 0` with `S_munu != 0` and/or Weyl`!= 0` tracking M — i.e. `g` is genuinely curved (not flat, not a pure coordinate change). **There is NO pure-Lambda baseline to subtract; the baseline is flat.**

4. **CALC-03: cross-term ON/OFF (decisive).** Define `det_block(X) = a*b*g - a*|x1|^2 - b*|x2|^2 - g*|x3|^2` (the block-diagonal norm; the `2*Re((x2 x1)x3)` term dropped — the unique V_0<->V_{1/2} channel). Rebuild `h_off`, `g_off = eta + h_off`, and its curvature with `Phi_off = -log det_block` at the SAME M!=0. Decisive: `R[g]_full(M) != 0` but `R[g]_off(M) = 0` (g_off flat, or decisively less curved) => the M-curvature is cross-term-sourced. Place M so ALL THREE off-diagonal octonion slots (x1,x2,x3) are populated (else the triple product is vacuous).

5. **CALC-04: scaling law + `||M||->0` limit.** Series `h(t)`, curvature`(t)` with `M = t·M0` (one V_{1/2} direction with octonionic content + a V_0 `x1` partner). Confirm curvature `-> 0` as `t -> 0` (recovering flat eta — the decisive limiting case), and read the leading power empirically (exact per order). Report the scale vs `det_2` (the genuine modulus) at fixed direction; NOTE the rho_J coincidence. Emit the leading-order `h^{(1)}` for Phase 73.

**Known difficulties at each step:**

- Step 2: carrying matter AND slice coords ALL symbolic through `.inv()` => >200s timeout. **Matter must be rational before inv().** (Measured cliff, COMPUTATIONAL.md.)
- Step 2 (engine subtlety): the curvature of `g=eta+h` is NOT the bare cone-Hessian curvature — raise indices with `g=eta+h`, keep `C` from the cone-Hessian potential (eta is a constant background so `C` is unchanged), and CROSS-CHECK with hand-rolled Riemann of `g`. Do NOT silently re-report the Phase-71 cone-Hessian R as the spacetime R.
- Step 3: **do NOT subtract a pure-Lambda or "center" baseline** — the M=0 spacetime baseline is flat `eta` (R=0). Subtracting an R=-3/Cartan reference is the FALSIFIED cone-Hessian framing (`fp-lambda-as-sourcing` / `fp-assume-einstein`).
- Step 4: single-slot matter makes `2*Re((x2 x1)x3) = 0` identically => off-switch test is HOLLOW. Populate all three slots (need a V_0 `x1` partner — at the bare center `x1=0`, so include a fixed V_0-internal `x1` component, OR populate the slice `p,q` which live in `x1`; verify the cross-term is nonzero before running curvature).
- Step 5: keep `||M||` small enough that `g=eta+h` retains signature (1,3) (70.1 splice-consistency regime); check eigenvalue signs over Q.
- Octonion non-associativity: every Hessian/curvature must be built from the corrected `det_3`; a wrong cross-term silently corrupts everything (PITFALLS Pitfall 2).

### Approach 2: Direct sympy hand-rolled Riemann of g=eta+h on the 4-dim slice (FALLBACK + MANDATORY cross-check)

**What:** Compute Christoffels and Riemann components of `g=eta+h` directly (not the Totaro shortcut), as an INDEPENDENT cross-check of the Totaro-with-`g^{-1}` route — and as the PRIMARY method if the Totaro closed form is found not to apply cleanly to `eta+h` (it should, since `C` is unchanged and only `g^{-1}` differs, but this MUST be verified).

**When to switch:** Always run it for a few components as a cross-check (the operational engine note flags this as mandatory). Use as primary only if the Totaro-`g^{-1}` and hand-rolled results disagree.

**Tradeoffs:** Slower, but independent of the Totaro closed-form assumption (the guard against mis-applying it to `g=eta+h`). The `h3_constant_curvature()` H^3 benchmark already exercises this hand-rolled path; adapt it to the dim-4 `g=eta+h`.

### Anti-Patterns to Avoid

- **Re-reporting the cone-Hessian curvature as the spacetime curvature.** Per Phase 70.1 the cone-Hessian is the SOURCE, not the metric. The decisive curvature is that of `g=eta+h` (indices raised with `g`, cross-checked by hand-rolled Riemann). _Example:_ quoting the Phase-71 `R=-3` / `R(det_2)` cone-Hessian values as the spacetime curvature — those describe the source field; the spacetime metric is flat at M=0.
- **Subtracting a pure-Lambda / "center is Einstein" baseline.** FALSIFIED by 70.1. The M=0 spacetime baseline is flat `eta` (R=0). _Example:_ "Delta R = R(M) - R(center=-3)" — there is no R=-3 spacetime baseline; this is `fp-lambda-as-sourcing`.
- **Single-slot matter for the cross-term test.** `2*Re((x2 x1)x3) = 0` if any slot is empty => the off-switch changes nothing => hollow test. _Example:_ M with only an x2-component and x3=0 gives identically-zero cross-term; the ON/OFF comparison is then trivially equal.
- **Carrying matter symbolic through the inverse.** >200s timeout; will trip the ~150s executor stream-watchdog. Substitute matter to rationals first.
- **Reading a coordinate/embedding artifact as matter-sourcing.** If the `M!=0` "curvature" of `g` is removable by a coordinate change (zero Riemann, or pure-trace with no traceless-Ricci/Weyl), it is not intrinsic gravity. Decompose and check Weyl/traceless-Ricci. (`fp-coordinate-curvature`.)
- **Relabeling a flat/homogeneous M!=0 result as survival.** If `g=eta+h(M)` stays flat (R=0) when matter is on, that is the honest negative result — report it, do NOT relabel. (`fp-relabel`.)
- **Using `octonion_algebra.py` det_3 (or the real-only rho-module cross-term) for octonionic M.** Buggy/association-blind => silently wrong coupling. Use the engine `det_3`.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE — cite and use)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Physical spacetime metric = eta+h (M=0 flat, DERIVED) | g=eta+h; g(center,M=0)=eta; R[g]=0 at M=0 | Phase 70.1 verdict (ratified) | THE metric; cite, do not re-open |
| Cone-Hessian = SOURCE structure (Hess(-log det)) | g_X = Hess(-log det), g^{pq} = P(X) | Faraut-Koranyi (ref); Phase 70.1 | Supplies h via the cross-term; cite, do not re-derive |
| Cone-Hessian M=0 vacuum is non-Einstein R_time x H^3 | g^{-1}Ric eigenvalues {0,-1,-1,-1}, R=-3, S!=0 | Phase 70.1 (exact over Q) | The SOURCE field's geometry (NOT the spacetime metric); explains why eta+h, not cone-Hessian, is the metric |
| Totaro closed-form Riemann (cubic => f_ijkl=0) | R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq) | Totaro Cor 2.3 (ref) | The curvature engine; apply to g=eta+h (C from cone-Hessian potential, g^{-1}=(eta+h)^{-1}) |
| Corrected cubic-norm cross-term | `2*Re((x2*x1)*x3)`, F_4-invariant (CH + 324/324) | Phase 64.1; engine `det_3` | The SSOT; never re-derive the association |
| Minkowski reduction (h=0 at center, signature (1,3)) | g-eta=0 exact at (M=0,center); Sylvester [1,-1,1,-1] | Phase 70/70.1; engine `minkowski_reduction` | The flat baseline (DERIVED); regression anchor |
| Ricci decomposition (n general) | see formulas below | Wikipedia / Besse | M-structure separation; standard, do not re-derive |
| **Phase-71 matterless cone-Hessian R values (engine regression anchors)** | R(center)=-3 [cone-Hessian source]; R{4:1/5,5:1/7}=-521269105/154700283; R{4:1/3}=-73041507/21967969; scale-inv; V_1 inert; one V_{1/2} dR=100305755136000/168193119407041 | 71-VERIFICATION.md | Reproduce to confirm the SOURCE engine is faithful before building g=eta+h |
| 70.1 splice-consistency PASS | h symmetric (0,2); small M preserves sig (1,3) | Phase 70.1 step 9 | The regime where g=eta+h is a valid Lorentzian metric |

**Key insight (why re-derivation is wasteful AND dangerous):** the cone metric (source), the Totaro formula, the corrected cross-term, AND the Phase-70.1 metric selection (g=eta+h, flat M=0) are all SOLID/certified results — re-deriving them risks re-introducing the cross-term association bug Phase 64.1 paid to fix, or re-opening the metric question 70.1 settled. The ONLY genuinely novel object is the *matter-sourced* curvature of `g=eta+h(x;M)` and its cross-term origin; spend the budget there.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| cone_hessian_at_center restricted to slice = diag(9,9,18,18), det 26244 | H0 (the centering reference for h) | engine `cone_hessian_at_center` (l.976); Phase 70 | center, M=0 |
| eta = diag(+1,-1,-1,-1) in Minkowski coords; eta_bg = J^T eta J in (beta,gamma,p,q) | the flat KKT background | engine `_eta_minkowski` (l.1144), `_frame_jacobian_bg_to_mink` (l.1150) | 52-kkt frame |
| Hess(-log det) at diagonal state: off-diag blocks 4·det - 2·w_i·(sig2-1/3) | closed-form 2nd-deriv structure (free analytic check on H_source) | rho_directional_derivatives.py PART 13 | diagonal background |
| x1 (V_0) couples to E_11 ONLY through the cubic trilinear, never bilinear | the cross-term IS the only matter channel | peirce_coupling.py (read, not import) | structural fact |
| Representative non-vacuous M (cross-term -13/315 != 0, all three slots, e_4 content) | a known-good matter point for the cross-term test | 72-01-baseline-probe.py / PHASE-RECOVERY (preserved) | x1,x2,x3 populated |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| The curvature of a Hessian metric (arXiv:math/0401381) | Totaro | 2004 | The exact curvature engine + the -d^2/4 rank-1 slice value | R_ijkl closed form; Cor 2.3; the constant-curvature slice fact |
| Analysis on Symmetric Cones | Faraut & Koranyi | 1994 | g_X=Hess(-log det), g^{pq}=P(X) — the SOURCE structure | the cone metric (source) |
| Curvatures of metric Jordan algebras (arXiv:2309.02682) | (recent) | 2023 | Every formally real Jordan algebra admits a Jordan-Einstein metric of NEGATIVE scalar curvature | Corroborates the cone-Hessian SOURCE geometry (negative curvature). NOTE: source side only — no matter-sourcing-of-a-flat-metric precedent, and NOT the spacetime metric (which is flat at M=0) |
| Ricci decomposition / Einstein four-manifolds (Wikipedia; arXiv:1612.00627, 1903.11817) | various | — | Standard n=4 scalar/traceless-Ricci/Weyl decomposition | the exact formulas in VALD-04 |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14.0 (installed) | exact symbolic algebra over Q: octonion/Jordan arithmetic, det_3, diff, Matrix.inv, Matrix.rank | the project's exact-over-Q engine; FORBIDDEN to use numpy float rank on verdicts |
| `code/bulk_geometry_verification.py` | warm engine (EXTEND) | det_3 SSOT + Totaro curvature + offcenter API + eta+h split (`offcenter_slice_metric`, `minkowski_reduction`) + II | the decisive surface; ALL_PASS exit 0 |
| Python 3 (`python3 -u`, foreground) | — | run heavy symbolic with unbuffered progress prints | defeats the ~150s executor stream-watchdog (print between heavy steps) |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| mpmath | guarded float fallback / triage | ONLY non-decisive triage (e.g. which M to do exactly); NEVER a verdict |
| `rho_directional_derivatives.py` (strategy) | the off-center / amplitude expansion structure | CALC-04 series-in-t; reuse strategy, recompute octonionic cross-term from engine |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| Totaro closed-form with g^{-1}=(eta+h)^{-1} | hand-rolled Christoffel/Riemann of g=eta+h | hand-rolled is the independent cross-check (mandatory); diffgeom blows up at dim-4 with matter |
| Faraut-Koranyi g^{pq} = P(X) closed form (for the SOURCE) | numerically invert finite-difference Hessian | float spot-check only; decisive inverse must be exact (Matrix.inv of the rational 4x4 g=eta+h) |
| Exact curvature at finite rational M | series in amplitude t | series is cheaper for the SCALING LAW and the ||M||->0 limit; finite-M exact is the decisive on/off verdict |

### Computational Feasibility (MEASURED — COMPUTATIONAL.md)

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| Hess(-log det_3) build, dim-4 slice (H_source) | ~35 ms | — | — |
| Evaluate at center / rational point | fast | — | — |
| `Matrix.inv()` of g=eta+h, dim-4, MATTER RATIONAL + 4 slice coords symbolic | ~3 s | expression swell | keep matter rational (this is the working regime) |
| `Matrix.inv()` dim-4, matter+coords ALL symbolic (6+ symbols) | **TIMEOUT >200 s** | symbolic inverse cliff | substitute matter to rationals FIRST |
| `Matrix.inv()` dim-10 V_0 symbolic | **TIMEOUT >200 s** | dim-10 off critical path | stay on dim-4 h_2(C_u); dim-10 is mpmath-only triage |
| Full Christoffel + Riemann of g=eta+h, dim-4, matter rational | **~19 s total** exact over Q | per-entry simplify | `cancel` per entry, not `simplify` in hot loop; print progress between steps (watchdog) |
| Cross-term ON vs OFF (two runs of the above) | ~40 s total | as above | — |
| Series curvature(t) to low order | cheap (finite jet) | — | — |
| Hand-rolled Riemann cross-check (few components) of g=eta+h | ~few s | — | only a handful of components needed |

**Installation / Setup:** SymPy 1.14.0 is already installed; no new packages required.
```bash
# nothing to install; if a fresh venv is ever needed:
pip install sympy==1.14.0
```

**Watchdog discipline (MEMORY [[feedback_executor_watchdog_stall_long_symbolic]]):** the gpd-executor stream-watchdog can kill long no-output symbolic runs (~150s harness, 600s hard). Run heavy steps FOREGROUND with `python -u` and print progress between heavy steps (after Hessian build, after inverse, after Riemann, after each decomposition). Background-resume stalls were observed; if a stall happens the orchestrator can commit + write SUMMARY from partial output.

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| g(center, M=0) = eta exactly; R[g]=0 | the FLAT KKT baseline (DERIVED, no fake Lambda) | `minkowski_reduction` residual=0; curvature of g at M=0 | exact 4x4 zero; R=S=Weyl=0 (flat) |
| Totaro-g^{-1} vs hand-rolled Riemann of g=eta+h | the curvature of g is computed correctly (Totaro closed form applies to eta+h) | compare a few R_ijkl[g] components both ways | exact agreement over Q |
| Riemann algebraic symmetries | engine correctness | `riemann_symmetry_ok(R, 4)` | True (antisym i,j; antisym k,l; pair-swap) |
| Engine regression (SSOT) | det_3 + curvature unbroken | `python3 code/bulk_geometry_verification.py` | OVERALL: ALL_PASS, exit 0 |
| Phase-71 matterless cone-Hessian R reproduced | the SOURCE engine is faithful | recompute the 71 cone-Hessian R anchors | exact match over Q |
| Cross-term off-switch reduces det to block-diagonal | the off-switch is implemented right | `det_block` = det_3 with `2*Re((x2x1)x3)` removed; factorizes on a test point | exact factorization |
| All three octonion slots populated for cross-term test | non-vacuous triple product | evaluate `2*Re((x2 x1)x3)` at the chosen M | NONZERO (else hollow) |
| g=eta+h keeps signature (1,3) at the chosen M | the splice-consistency regime (70.1) | eigenvalue signs of g over Q | (1,3) for small ||M|| |
| Reality + exactness | no Wick/float artifact | R[g], Ric[g], curvature all real rationals over Q | real, exact |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| M -> 0 (any V_0-background at center) | ||M||->0 | g -> eta, R[g] -> 0 (FLAT, DERIVED from KKT — the decisive limiting case) | Phase 70.1; 52-kkt |
| Cross-terms OFF + M!=0 | block-diagonal det | M-sourced curvature of g must VANISH (or change decisively) | ref-prompt Phase B(b); contract test-cross-term-onoff |
| V_1 (alpha) matter alone | M in V_1 only | curvature of g UNCHANGED from flat (V_1 inert; alpha absent from triple) — must be checked/explained | Phase-71 Check A(ii) |
| cone-Hessian SOURCE at M=0 | (source field, not spacetime) | non-Einstein R_time x H^3, {0,-1,-1,-1}, R=-3 | Phase 70.1 (for the SOURCE only) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| Curvature of g reality | exact rational | exact (no tolerance) | imaginary part identically 0 |
| Scaling curvature(t), M=t·M0 | series in t | exact per order | leading power k>=1; curvature(0)=0 (flat); coeff exact rational |
| g^{pq} vs Faraut-Koranyi P(X) (source cross-check) | float spot-check of the symbolic inverse | ~1e-10 (triage only) | agreement (decisive g^{pq} is the exact Matrix.inv of g=eta+h) |

### Red Flags During Computation

- Curvature of `g=eta+h` has a nonzero imaginary part => a unitarity/reality-violating error (wrong cross-term association or a Wick contamination). Reality must hold exactly over Q.
- `2*Re((x2 x1)x3)` evaluates to 0 at the chosen M => the cross-term test is HOLLOW (single-slot or accidentally-associative M); repopulate all three slots with e_4..e_7 content.
- The cross-term off-switch leaves the curvature of `g` UNCHANGED => the curvature is NOT matter-sourced => honest negative (`fp-lambda-as-sourcing` avoided).
- `Matrix.inv()` hangs (>60s) => matter is still symbolic; substitute to rationals.
- The `M!=0` "curvature" of `g` has zero Riemann (or is pure-trace removable by a coordinate change) => coordinate/embedding artifact, not gravity (`fp-coordinate-curvature`); decompose to confirm Weyl/traceless-Ricci.
- Someone subtracts an `R=-3` / "center is Einstein" baseline => the FALSIFIED cone-Hessian framing crept in; the spacetime baseline is FLAT (R=0). Strike it.
- The Totaro-`g^{-1}` curvature disagrees with the hand-rolled Riemann of `g=eta+h` => the closed form was mis-applied to `eta+h`; use the hand-rolled Riemann as primary.

## Common Pitfalls

### Pitfall 1: Cone-Hessian baseline / pure-Lambda mistaken for the spacetime baseline [fp-lambda-as-sourcing; the re-frame pitfall]

**What goes wrong:** The curvature is computed against the CONE-HESSIAN baseline (M=0 = R_time x H^3, R=-3) or a "center is Einstein, pure-Lambda" reference, and the matter effect is read as a Delta against that curved baseline.
**Why it happens:** Carrying forward the pre-70.1 framing (the prior version of THIS file, and the superseded PHASE-RECOVERY.md). 70.1 FALSIFIED the cone-Hessian-as-metric thesis: the SPACETIME metric is `g=eta+h`, flat at M=0.
**How to avoid:** The M=0 spacetime baseline is FLAT `eta` (R=0), DERIVED from the KKT `det_2` form. Compute the curvature of `g=eta+h` directly; the matter claim is that `g` becomes genuinely curved when `M!=0` (and flat when `M->0` or cross-term OFF). **NO Lambda tripwire, NO R=-3 subtraction, NO Cartan baseline.**
**Warning signs:** an `R=-3` or `{0,-1,-1,-1}` value quoted as the spacetime curvature; a "Delta R against the center/pure-Lambda" subtraction; the cone-Hessian curvature reported as the metric's curvature.
**Recovery:** Re-base on flat `eta`; recompute the curvature of `g=eta+h`; if matter does not curve `g`, report "not matter-sourced" (NEGATIVE-RESULT-IS-SUCCESS), do NOT proceed to Phase 73.

### Pitfall 2: Octonion non-associativity in the cross-term silently corrupts everything [Phase B critical]

**What goes wrong:** Using the wrong cross-term association ((x1 x2) x3, or x1(x2 x3), or the real-only `2 d1 d2 d3`) returns a plausible number, but every Hessian/curvature/coupling built on it is wrong — and the error is amplified by differentiation, not averaged out.
**Why it happens:** Three mutually inconsistent det conventions exist in-repo (measured 0.67 associator gap); stale project-research files even point at the banned `octonion_algebra.py`.
**How to avoid:** Use the engine `det_3` (`2*Re((x2*x1)*x3)`) for ALL geometry. Pre-flight on genuinely non-associative M (e_4..e_7 nonzero): confirm `Re((x2 x1) x3) != Re(x1 (x2 x3))` (nonzero gap) and Cayley-Hamilton holds. Re-derive the (V_{1/2},V_{1/2},V_0) polarization block and confirm it matches.
**Warning signs:** det_3 disagrees with the matrix/Sarrus convention on octonionic data; a "verified" cross-term done only on diagonal/quaternionic (e_0..e_3) inputs (vacuous, associative).
**Recovery:** Recompute det_3 with the corrected association; redo ALL Hessians/curvatures downstream (nothing built on the wrong norm survives).

### Pitfall 3: Hollow cross-term test (vacuous triple product) [CALC-03]

**What goes wrong:** With matter in fewer than all three off-diagonal slots, `2*Re((x2 x1)x3) = 0` identically, so the full-det and block-diagonal-det give the SAME curvature — the ON/OFF test is trivially equal and proves nothing.
**Why it happens:** Putting M only in V_{1/2} (x2 or x3) without an x1 (V_0) partner, or only one of x2/x3. At the bare center `x1=0` (no V_0 octonion content) so the triple vanishes.
**How to avoid:** Populate x1 (a V_0 slice direction `p,q` — which live in x1 — or a fixed V_0 internal direction), x2 AND x3 (V_{1/2}) so the triple product is genuinely nonzero. Verify `2*Re((x2 x1)x3) != 0` at the chosen M before running curvature. (The preserved representative M with cross-term `-13/315` is a known-good choice.)
**Warning signs:** cross-term evaluates to 0; ON and OFF curvatures identical for trivial reasons.
**Recovery:** Repopulate all three slots with octonionic (e_4..e_7) content; re-run.

### Pitfall 4: Symbolic-matter inverse cliff / watchdog stall [performance]

**What goes wrong:** Carrying matter parameters AND the 4 slice coords as free symbols through `Matrix.inv()` (of g=eta+h) blows up (>200s), tripping the ~150s executor stream-watchdog; the run is killed with no verdict.
**Why it happens:** Expression swell in the symbolic inverse (the dominant cost).
**How to avoid:** Substitute matter to small RATIONALS before inverting; keep ONLY the 4 slice coords symbolic (~3s inverse, ~19s full curvature). For the scaling law, series-expand in a single amplitude t to low order rather than carrying M symbolic. Run foreground `python -u` with progress prints between heavy steps.
**Warning signs:** `.inv()` runs >60s; harness goes quiet.
**Recovery:** Kill, substitute matter to rationals, re-run; if a stall already happened, orchestrator commits + writes SUMMARY from partial output.

### Pitfall 5: Mistaking the bare cone-Hessian curvature (or an embedding artifact) for the spacetime curvature [conceptual; fp-coordinate-curvature]

**What goes wrong:** Reporting the curvature of the cone-Hessian `H_source` (the SOURCE field), or an extrinsic-embedding (II) term, as the spacetime curvature — when the decisive object is the intrinsic curvature of `g=eta+h`.
**Why it happens:** The engine's `totaro_riemann` was originally fed the cone-Hessian metric (Phase 71); the curvature of `g=eta+h` raises indices with `g`, not `H_source`. The slice is also not totally geodesic off-center (II != 0), but that is the SOURCE-field embedding, not the spacetime metric.
**How to avoid:** The DECISIVE quantity is the INTRINSIC curvature of `g=eta+h(x;M)` — Totaro `C` from the cone-Hessian potential but indices raised with `g=eta+h`, cross-checked by hand-rolled Riemann of `g`. The matter claim is about its M-DEPENDENT part being genuinely curved (traceless-Ricci/Weyl present), vanishing as `||M||->0`.
**Warning signs:** the spacetime R quoted as the Phase-71 cone-Hessian value; II-driven terms quoted as the source; curvature computed with `H_source^{-1}` instead of `(eta+h)^{-1}`.
**Recovery:** Recompute the curvature of `g=eta+h` (raise with g); cross-check hand-rolled; decompose to confirm intrinsic non-flat structure.

## Level of Rigor

**Required for this phase:** EXACT computation over Q (a computer-algebra proof of the specific tensor identities at the chosen backgrounds), at the level of "controlled exact numerical evidence on a decisive sub-slice." NOT a general theorem for all M (that is beyond scope); a decisive exact-over-Q verdict on representative M with the cross-term off-switch and the `||M||->0` limit recovering flat eta.

**Justification:** The contract's acceptance tests (test-cross-term-onoff = consistency, test-lambda-vs-matter = re-framed limiting case: M=0 is flat eta) and FORBIDDEN PROXIES (fp-float-decisive) demand exactness, not floating-point. The matter-sourcing claim is novel (no literature benchmark), so the rigor must come from internal exact-over-Q checks: the off-switch must EXACTLY kill the M-curvature of `g`, `||M||->0` must EXACTLY recover flat `eta` (g->eta, R->0), and reality must hold EXACTLY.

**What this means concretely:**
- All curvature verdicts (R[g], S_munu, Weyl, on/off comparison) computed with `sympy.Rational`, exact over Q. No float on any verdict.
- The curvature of `g=eta+h` cross-checked by two independent routes (Totaro-`g^{-1}` and hand-rolled Riemann of `g`) on a few components.
- Ranks/zeros via `sympy.Matrix.rank()` / exact comparison, never numpy.
- The scaling law may be a low-order series in amplitude t, but each coefficient is an exact rational; `curvature(t=0)=0` (flat) is the decisive boundary value.
- A representative-M result with the off-switch + `||M||->0` limit is sufficient for the SURVIVES/negative verdict; an all-M general proof is NOT required (and is out of scope — Phase C / future).
- Reproduce the Phase-71 matterless cone-Hessian anchors exactly before adding matter (engine regression), and the 70.1 `g=eta` / signature-(1,3) baseline.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| Cone-Hessian IS the spacetime metric (M=0 = R_time x H^3) | `g=eta+h` is the spacetime metric (M=0 = flat eta, DERIVED); cone-Hessian = matter SOURCE | **Phase 70.1 (2026-05-31)** | **The baseline is FLAT, not curved; no Lambda tripwire; curvature computed for g=eta+h** |
| Lattice/Fisher metric (paper6-continuum-limit) | Intrinsic cubic-norm cone-Hessian sourcing of h | v17.0 | No lattice; matter enters via det cross-terms |
| Posited GST/N=2 supergravity Lagrangian with det as prepotential | Intrinsic curvature of g=eta+h sourced by the cone-Hessian cross-terms | v17.0 | No SUSY, no posited action — circular route abandoned |
| `octonion_algebra.py` det_3 ((x1 x2) x3, float) | `det_3` (`2*Re((x2*x1)*x3)`, exact, F_4-invariant) | Phase 64.1 | The SSOT; stale project-research references to octonion_algebra are SUPERSEDED |
| Construction (i) Wick-rotate via u=e7 | Construction (ii) eta + cone-Hessian perturbation | Phase 70 | Wick rejected (manufactures spurious curvature) |
| rho_J as the basepoint modulus | det_2 (Stab_{V_0}=Spin(9,1) invariant) | Phase 71 | det_2 is the genuine modulus (of the source); coincides with rho_J for single-direction perturbations |
| "Center is Einstein, Lambda<0" (Cartan baseline) | Center cone-Hessian is non-Einstein {0,-1,-1,-1}; spacetime metric is flat at M=0 | **Phase 70.1** | CONVENTIONS §6 / METHODS Validation-(a) FALSIFIED for the cone-Hessian (non-blocking flag); moot for g=eta+h |

**Superseded approaches to avoid:**
- **Cone-Hessian-as-metric / R=-3 / pure-Lambda-at-center baseline:** FALSIFIED by Phase 70.1. The spacetime metric is `g=eta+h`, flat at M=0. Do not compute a Delta against an R=-3 baseline.
- `octonion_algebra.py` det_3: buggy association; the project-research METHODS/PITFALLS/COMPUTATIONAL that point at it are PRE-Phase-64.1 and SUPERSEDED — use the engine `det_3`.
- Jacobson 1995 thermodynamic / observers-make-gravity ensemble: explicitly REJECTED (fp-ensemble-gravity). The curvature must come from the algebra's own cubic-norm geometry, one observer, one off-center point.

## Open Questions

1. **Does the Totaro closed form apply cleanly to `g=eta+h` (eta a constant additive background)?**
   - What we know: `eta` is a constant (coordinate-independent) background, so the 3rd-derivative cubic form `C` of `g=eta+h` equals that of the cone-Hessian `H_source`; only the index-raising metric differs (`g^{-1}=(eta+h)^{-1}` vs `H_source^{-1}`). The Totaro closed form is derived for a pure Hessian metric `g=Hess(Phi)`.
   - What's unclear: whether the closed-form derivation's use of the `f_ijkl=0` cubic property survives the additive constant `eta` (it should, since `eta` does not enter `C`), or whether a residual term appears.
   - Impact: determines whether the fast Totaro route or the hand-rolled Riemann is primary.
   - Recommendation: compute a few `R_ijkl[g]` BOTH ways (Totaro-`g^{-1}` and hand-rolled Christoffel/Riemann of `g`) and require exact agreement over Q; if they disagree, use the hand-rolled Riemann of `g=eta+h` as primary. (Mandatory cross-check.)

2. **Is V_1 (alpha) inert to the spacetime curvature, as it is to the cone-Hessian R?**
   - What we know: Phase-71 found adding V_1 alone leaves the cone-Hessian R UNCHANGED; `alpha` (the (0,0) entry) is absent from the octonion cross-term `2*Re((x2 x1)x3)`.
   - What's unclear: whether V_1 can source `h` (hence the curvature of g) indirectly via its effect on the metric normalization.
   - Impact: determines whether "matter" effectively means V_{1/2} only.
   - Recommendation: compute the curvature of `g=eta+h` for (a) V_{1/2} only, (b) V_1 only, (c) V_1+V_{1/2}, at the center background; explain the V_1-inertness structurally (alpha absent from the triple). Likely the decisive matter channel is V_{1/2}.

3. **What is the leading power of the curvature of `g=eta+h` in `||M||`?**
   - What we know: curvature ~ C·C structure (Totaro), C from 3rd derivatives of `-log det_3`; the cross-term is bilinear in (x2,x3) with x1. `h` itself is O(cross-term) in M.
   - What's unclear: whether the leading curvature is O(||M||), O(||M||^2), or higher.
   - Impact: the scaling law (CALC-04) and the linear-in-M piece feeding the Phase-73 linearized-Einstein test.
   - Recommendation: compute the series curvature(t), M=t·M0, read the leading power empirically (exact per order); curvature(0)=0 (flat) is the boundary value; do NOT assume O(||M||^2).

4. **Does the cross-term off-switch cleanly remove the M-source of `h`?**
   - What we know: the only V_0<->matter mixing term is the octonion triple `2*Re((x2 x1)x3)`. Zeroing it leaves abg - a|x1|^2 - b|x2|^2 - g|x3|^2 (block-diagonal).
   - What's unclear: the |x2|^2, |x3|^2 terms (V_{1/2} self-norms) still couple to the diagonal a,b,g, so the off-switch removes the TRIPLE coupling but not the matter norms entirely.
   - Impact: the exact form of `det_block` determines what "cross-terms off" means precisely.
   - Recommendation: define `det_block` operationally as "det_3 with the `2*Re((x2 x1)x3)` term set to 0" (the unique V_0<->V_{1/2} mixing channel), verify it reduces to det(V_0) when matter (x2,x3,alpha)=0, and document that the product wording "det(V_1)·det(V_0)" is schematic.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Totaro `totaro_riemann` mis-applies to g=eta+h | additive eta breaks the closed-form assumption | hand-rolled Christoffel/Riemann of g=eta+h (the mandatory cross-check, promoted to primary) | low — engine has the hand-rolled path (h3_constant_curvature) |
| Symbolic dim-4 curvature too slow even with matter rational | unexpected swell | series in amplitude t to low order (avoid full inverse), or smaller/sparser rational M | low |
| Exact full-M result intractable | expression swell | representative finite rational M + ||M||->0 series; accept "decisive on representative M" rigor | low (already the planned rigor) |
| Cross-term off-switch ambiguous | block structure unclear | operational det_block = "drop the `2*Re((x2 x1)x3)` term"; verify reduction to det(V_0) at M=0 | low |

**Decision criteria:** If, with the V_0-background at the center and all three slots populated, the curvature of `g=eta+h(M)` (i) survives the cross-term off-switch, OR (ii) does not vanish as `||M||->0` (does not recover flat eta), OR (iii) is a coordinate/embedding artifact (no traceless-Ricci/Weyl structure), then matter does NOT source the spacetime curvature: report "not matter-sourced" / "g stays flat (or non-intrinsically-curved) under matter", do NOT proceed to Phase 73 (NEGATIVE-RESULT-IS-SUCCESS). If the curvature of `g=eta+h(M)` vanishes under the off-switch AND vanishes as `||M||->0` AND carries genuine traceless-Ricci/Weyl structure, matter IS cross-term-sourcing the spacetime curvature (SURVIVES; Phase 73 greenlit — emit `h^{(1)}` for the linearized-Einstein test).

## Lambda-vs-Matter Decomposition (n=4) — re-framed: flat-baseline confirmation + M-structure (for VALD-04)

**Re-frame note:** the prior version subtracted a pure-Lambda "center" baseline (R=-3). Per Phase 70.1 there is NO such baseline: the M=0 spacetime metric is FLAT `eta` (R=0). The decomposition below now serves to (1) confirm M=0 gives flat `g` (R=S=Weyl=0) and (2) expose the structure of the `M!=0` curvature of `g=eta+h`. **NO Lambda tripwire; the only "pure-Lambda" check is the trivial flat one at M=0.**

The executor computes these EXACT over Q for `g=eta+h(M)`, with indices raised by the slice metric `g_munu` (mostly-minus; the decomposition is an algebraic identity in the curvature tensor, signature-agnostic). n = 4.

- **Ricci scalar:** R = g^{munu} R_munu = g^{ik} g^{jl} R_ijkl  (engine `ricci_scalar`). At M=0: R=0 (flat). 
- **Traceless Ricci:** S_munu = R_munu - (R / n) g_munu = R_munu - (R/4) g_munu.  At M=0: S=0. Genuine M-sourcing of curvature requires S_munu != 0 (or Weyl != 0) tracking M.
- **Maximally-symmetric (constant-curvature) reference Riemann:** R^{(0)}_{abcd} = (R / (n(n-1))) (g_ac g_bd - g_ad g_bc) = (R/12)(g_ac g_bd - g_ad g_bc) for n=4. At M=0 (R=0) this is zero (flat).
- **Scalar part of Riemann:** S_ijkl = (R/(n(n-1)))(g_il g_jk - g_ik g_jl) = (R/12)(g_il g_jk - g_ik g_jl).
- **Traceless-Ricci part of Riemann:** with Z_jk = S_jk (= R_jk - (R/4)g_jk), E_ijkl = (1/(n-2))(Z_il g_jk - Z_jl g_ik - Z_ik g_jl + Z_jk g_il) = (1/2)(...) for n=4.
- **Weyl tensor (residual):** C_ijkl = R_ijkl - S_ijkl - E_ijkl  (n>=4). Conformally invariant; nonzero Weyl = genuine non-conformally-flat structure.
- **Matter-sourcing criterion (re-framed):** at M=0, R=S=Weyl=0 (flat eta — DERIVED). For M!=0, **genuine M-sourcing requires R[g](M) != 0 with S_munu != 0 and/or C_ijkl != 0 tracking M** (g genuinely curved, not flat, not a coordinate artifact), VANISHING as ||M||->0 and under the cross-term off-switch.

(Source: Wikipedia "Ricci decomposition"; Besse, *Einstein Manifolds*; standard. The maximally-symmetric form R_abcd = (R/(n(n-1)))(g_ac g_bd - g_ad g_bc) is textbook.)

## Cross-term ON/OFF construction — operational recipe for CALC-03

The matter coupling channel is the SINGLE term in `det_3`:
```
cross = oct_mul(oct_mul(x2, x1), x3)   # (x2 x1) x3
det_3(X) = a*b*g - a*|x1|^2 - b*|x2|^2 - g*|x3|^2 + 2*cross[0]
```
with x1 the V_0 octonion (matrix entry X[2][1]), x2,x3 the V_{1/2} octonions (X[0][2], X[1][0]). x1 carries V_0 content (incl. the slice p,q and the internal W-sector); x2,x3 carry the V_{1/2} matter.

- **Cross-terms OFF (block-diagonal norm):** `det_block(X) = a*b*g - a*|x1|^2 - b*|x2|^2 - g*|x3|^2` (the `2*cross[0]` term dropped). This is the unique V_0<->V_{1/2} mixing channel; with it removed, the V_0 sector and the V_{1/2} matter no longer couple through the triple product. At M=0 (x2=x3=alpha-matter=0) det_block reduces to det(V_0) (verify exactly). Implement as a one-line variant of `det_3` (a `cross_off=True` flag, or a separate `det_3_block`).
- **Feed the SAME M!=0 through both** `Phi = -log det_3` and `Phi_off = -log det_block`, build `h`, `h_off`, `g=eta+h`, `g_off=eta+h_off`, compute the curvature of each, and compare. Decisive: curvature of `g_full(M) != 0` (curved), curvature of `g_off(M) = 0` (flat, or decisively less) => cross-term/matter-sourced.
- **Non-vacuity gate (Pitfall 3):** before running, assert `2*cross[0] != 0` at the chosen M — i.e. all three slots x1,x2,x3 populated with octonionic content (include e_4..e_7 components so the test is genuinely non-associative). At the bare center x1=0, so populate the slice p,q (which live in x1) or a fixed V_0 internal x1 component.

Note: the prompt's "det(V_1)·det(V_0)" product is schematic; the operational, unambiguous definition is "det_3 with the `2*Re((x2 x1)x3)` term set to zero" (the only term coupling V_0 to V_{1/2}). Document this and verify the M=0 reduction.

## Isolation Protocol — V_0-background at the center, varying only M (matter-on-flat)

Per the Phase-70.1 verdict, the spacetime baseline is the FLAT KKT vacuum; matter is isolated by varying ONLY M from the center:

1. **Fix the V_0-background at the center.** `X_bg = I/3` (so the M=0 spacetime metric is exactly flat `eta`, the DERIVED KKT vacuum; `h=0`). This is the cleanest baseline and the one the 70.1 verdict singles out (flat, no Lambda). (A fixed off-center V_0-background is also admissible but reintroduces the source-field det_2-variation; the center is preferred for the flat baseline.)
2. **Vary ONLY matter M in V_1 (alpha-matter, index 0) ⊕ V_{1/2} (indices 11..26).** In the engine, populate ONLY these indices in `delta`; do NOT move the V_0-background between the M=0 and M!=0 runs. (To make the cross-term non-vacuous at the center, populate the slice `p,q` — engine indices {3,10}, which live in x1 — alongside the V_{1/2} matter; or add a fixed V_0 internal x1 component.)
3. **Build `g = eta + h(x;M)` and compute its intrinsic curvature.** `h(x;M) = H_source(x;M) - H0`; `g = eta + h`. The matter-sourced spacetime curvature is the curvature of `g` (raise indices with `g`, cross-check hand-rolled). At M=0 this is flat (R=0); the claim is that M!=0 makes it genuinely curved via the cross-term.
4. **M-placement (non-vacuous):** ensure all three off-diagonal octonion slots are populated so `2*Re((x2 x1)x3) != 0` — x1 from the slice `p,q` (or a fixed V_0 internal component), x2,x3 from the V_{1/2} matter, with e_4..e_7 content (genuinely octonionic). Verify the cross-term is nonzero before running curvature.
5. **Limits and controls:** (a) `||M||->0` => `g->eta`, curvature->0 (flat — the decisive limiting case); (b) cross-term OFF => curvature of `g_off` vanishes; (c) V_1-only vs V_{1/2}-only to confirm the V_1-inertness (alpha absent from the triple); (d) keep `||M||` in the signature-(1,3) regime (70.1 splice-consistency).

This protocol is what makes Phase 72 matter-on-flat: the V_0-background is held at the center (flat eta baseline), and ONLY matter is varied, reading off the M-dependent curvature of `g=eta+h` sourced through the cross-terms.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that the Totaro closed form applies unchanged to `g=eta+h` (additive constant `eta`). The argument (eta constant => C unchanged, only g^{-1} differs) is sound but MUST be verified against a hand-rolled Riemann of `g=eta+h` — flagged as Open Question 1 and a mandatory cross-check. If it fails, the hand-rolled Riemann is primary (low switching cost; the engine has the path).
2. **Assumption that might be wrong (2):** that the cross-term `2*Re((x2 x1)x3)` is the ONLY V_0<->matter channel. It is the only OCTONION-mixing term, but the diagonal coefficients (a,b,g multiplying |x1|^2,|x2|^2,|x3|^2) also couple the diagonal content to the matter norms. The off-switch removes only the triple product; the |x2|^2,|x3|^2 terms remain. This is acceptable (the triple product IS the prompt's named channel) but should be stated explicitly — Open Question 4.
3. **Limitation I might be understating:** the rigor is "exact on representative M", not "proved for all M". A matter-sourcing verdict on a few representative M (with off-switch + ||M||->0) is decisive for SURVIVES/negative, but is NOT a general theorem. Phase C (Einstein structure) is where generality would be tested; Phase 72 deliberately stops short. Stated in Level of Rigor.
4. **Simpler method overlooked?** The series-in-amplitude approach (CALC-04) is actually SIMPLER than full finite-M exact curvature for the scaling law and the ||M||->0 limit, and should be the primary tool there; full finite-M exact is reserved for the decisive on/off verdict. Both are in the engine's wheelhouse.
5. **Would a specialist disagree?** A Jordan-algebra geometer might note that "matter sourcing curvature" is unusual framing — the cone is homogeneous under E_6, so all the curvature is "intrinsic to the algebra." That is exactly the milestone's point (the interpretation is what's being tested), and the 70.1 re-frame sharpens it: the SPACETIME metric is the flat `eta` slice, and the V_{1/2} ("matter") content perturbs it via the cubic cross-term — a concrete, interpretation-free, exact-over-Q test (does the curvature of `g=eta+h` turn on with M, off with the cross-term, off as M->0). The math verdict is what Phase 72 decides.
6. **The biggest re-frame risk:** silently re-reporting the Phase-71 cone-Hessian curvature (R=-3, R(det_2)) as the spacetime curvature. Guarded by Pitfall 1 and Pitfall 5, the red-flag list, and `fp-lambda-as-sourcing`/`fp-coordinate-curvature`. The spacetime curvature is that of `g=eta+h` (raise with g), flat at M=0.

## Sources

### Primary (HIGH confidence)

- `.gpd/phases/70.1-.../70.1-01-SUMMARY.md` — the human-ratified Phase-70.1 verdict (g=eta+h is the metric; M=0 flat DERIVED from KKT; cone-Hessian = source; Lambda tripwire struck; splice-consistency PASS). **AUTHORITATIVE re-scope; supersedes the pre-70.1 baseline framing.** [ref-70.1-verdict]
- Faraut & Koranyi, *Analysis on Symmetric Cones* (1994), Oxford — cone metric g_X = Hess(-log det) (the SOURCE structure), g^{pq} = P(X). [ref-faraut-koranyi]
- Totaro, "The curvature of a Hessian metric", arXiv:math/0401381, Cor 2.3 — R_ijkl closed form; the engine's curvature method (applied to g=eta+h). [ref-totaro]
- McCrimmon, *A Taste of Jordan Algebras* (2004) — Peirce decomposition, cubic norm, P(X). [ref-mccrimmon]
- `~/scratch/get-physics-done/paper6-bulk-geometry-prompt.md` — authoritative milestone spec, Phase B targets + reporting discipline. [ref-prompt]
- `.gpd/phases/71-a-homogeneity-kill-gate/71-VERIFICATION.md` — VERIFIED Phase-71 findings (cone-Hessian SOURCE position-dependence, V_1 inert, V_{1/2} active, det_2 modulus, exact R anchors).
- `code/bulk_geometry_verification.py` — the warm engine (det_3 SSOT, Totaro curvature, offcenter API, eta+h split via `offcenter_slice_metric`/`minkowski_reduction`, II); ALL_PASS exit 0. Read l.342-468 (det_3/Tr/polarize_d), l.976-1210 (center/offcenter metric, eta+h split, Minkowski reduction), l.1312-1433 (cubic_form_C/totaro_riemann/ricci_scalar/kretschmann/sectional_curvature), l.1888-1947 (second_fundamental_form).
- `.gpd/CONVENTIONS.md` — v17.0 locked conventions (18/18; §6 "center is Einstein" FALSIFIED for the cone-Hessian per 70.1, non-blocking, moot for g=eta+h).
- Wikipedia, "Ricci decomposition" — exact n=4 scalar/traceless-Ricci/Weyl formulas + Einstein/maximally-symmetric criteria (textbook-standard).

### Secondary (MEDIUM confidence)

- "Curvatures of metric Jordan algebras", arXiv:2309.02682 (2023) — every formally real Jordan algebra admits a Jordan-Einstein metric of NEGATIVE scalar curvature; corroborates the cone-Hessian SOURCE geometry (Lambda<0 for the source). PDF could not be parsed in full; relevance from the search abstract. SOURCE side only — NOT the spacetime metric (flat at M=0).
- Curvature decompositions on Einstein four-manifolds, arXiv:1903.11817; Bochner formulas for Weyl on 4d Einstein manifolds, arXiv:1612.00627 — corroborate the n=4 decomposition.
- `.gpd/research/METHODS.md`, `PITFALLS.md`, `COMPUTATIONAL.md` — project-level research. USE WITH CAUTION: their det-SSOT references to `octonion_algebra.py` are SUPERSEDED by the v17.0 convention lock (use engine `det_3`), and their "center is Einstein / pure-Lambda" baseline is FALSIFIED for the cone-Hessian (Phase 70.1). The performance cliffs (>200s symbolic inverse, ~19s matter-rational, vacuous-triple-product) and the cross-term-off-switch methodology are accurate and directly used here.

### Tertiary (LOW confidence)

- `~/scratch/get-physics-done/rho_directional_derivatives.py` (real-only cross-term — strategy reuse only), `peirce_coupling.py` (numpy/float — intuition only), `~/repos/blog/research/qualia-fixed-point/h3o_tower.py` (cubic-norm benchmark — optional provenance check). NOT on the decisive path.
- `.gpd/phases/72-b-matter-sourcing/PHASE-RECOVERY.md` — **SUPERSEDED by Phase 70.1.** Its "Lambda=0 tripwire / flatness inserted / construction-(ii) conditional / cone-Hessian = spin-2-on-R×H³" framing was the open-question state BEFORE the metric was selected; do NOT carry it forward. Retained only as provenance for the preserved matter pipeline (Peirce map, cross-term channel, representative M, ΔR/Ricci-decomposition machinery).
- **No external literature found for the matter-sourcing CLAIM** (off-diagonal-Peirce content sourcing a perturbation of a flat Minkowski slice metric on a symmetric cone). Novel; validation is internal (exact-over-Q + ||M||->0 flat limit + off-switch), not literature-benchmarked.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH — Totaro curvature, Faraut-Koranyi cone metric, Ricci decomposition, and the Phase-70.1 metric selection (g=eta+h, flat M=0) are all standard/certified/ratified; the engine implements them and passes regression. (One MEDIUM caveat: the Totaro closed form's application to g=eta+h needs the mandatory hand-rolled cross-check — Open Question 1.)
- Standard approaches: HIGH on the method (engine measured end-to-end; metric fixed by 70.1), MEDIUM on the matter-sourcing OUTCOME (novel; that's the phase's open question).
- Computational tools: HIGH — SymPy 1.14.0 installed; engine ALL_PASS; all costs MEASURED (COMPUTATIONAL.md), not assumed.
- Validation strategies: HIGH — limiting case (M->0 => flat eta), cross-term off-switch, reality/exactness, two-route curvature cross-check, Phase-71 regression anchors, 70.1 signature/splice all concrete and exact.
- External literature for matter-sourcing: LOW — none found; expected for this novel construction (Novel Territory — internal validation only).

**Research date:** 2026-05-30 (refreshed 2026-05-31 for the Phase-70.1 matter-on-flat re-frame)
**Valid until:** Physics/math results stable indefinitely (Totaro, Faraut-Koranyi, Ricci decomposition are decades-old textbook; the Phase-70.1 metric selection is a ratified project decision). The engine API is the volatile part — re-confirm function signatures if `code/bulk_geometry_verification.py` is refactored. SymPy version (1.14.0) is the fastest-moving dependency.
