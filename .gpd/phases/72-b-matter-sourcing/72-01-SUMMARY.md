---
phase: 72-b-matter-sourcing
plan: 01
depth: complex
one-liner: "Built & confirmed the matter-on-flat curvature engine: g=eta+h(x;M) on the flat KKT-Minkowski background (B1 difference-of-cone-Hessians), M=0 FLAT over a neighbourhood (DERIVED from KKT, NOT R=-3), R[g](M)!=0 with hand-rolled Levi-Civita == Totaro-g^{-1} exact over Q, n=4 decomposition exposing S!=0 & Weyl!=0; verdict deferred to 72-02"

subsystem: [computation, derivation, formalism]
tags: [differential-geometry, hessian-metric, totaro-curvature, ricci-decomposition, octonions, h3o, jordan-algebra, lorentzian-signature, matter-on-flat]

requires:
  - phase: 70.1-revise-a0-select-the-physical-spacetime-metric
    provides: "human-ratified verdict: g=eta+h is the physical spacetime metric (eta=flat KKT, DERIVED from det_2); cone-Hessian = matter SOURCE; cone-Hessian-is-metric FALSIFIED; Lambda tripwire STRUCK"
  - phase: 71-a-homogeneity-kill-gate
    provides: "SURVIVES (position-dependent slice metric); the warm Totaro curvature engine + cone-Hessian SOURCE regression anchors (R{4:1/3}, R{4:1/5,5:1/7}, R(center)=-3)"
provides:
  - "spacetime_curvature_of_g(matter_delta, slice_vals, bg_delta) -- curvature of g=eta+h(x;M), B1 (difference potential, indices raised by g^{-1}=(eta+h)^{-1}), exact over Q"
  - "hand_rolled_riemann_of_g -- independent Levi-Civita Riemann of g=eta+h (validates Totaro applicability; agrees exact over Q)"
  - "ricci_decomposition_n4 -- n=4 scalar/traceless-Ricci/Weyl split (trace_g(S)=0, reconstruction exact over Q)"
  - "eig_signature_count -- exact-over-Q signature via real_roots of charpoly (null-aligned frame, NOT Sylvester)"
  - "the FLAT M=0 baseline (R=S=Weyl=0, DERIVED from KKT det_2) confirmed over a neighbourhood under B1"
  - "the M!=0 curvature is genuinely structured (R[g](M)!=0, S_munu!=0, Weyl!=0); V_1 inert, V_{1/2} active"
affects: [72-02-decisive-cross-term-off-switch-and-verdict, 73-linearized-einstein-test]

methods:
  added: ["B1 difference-of-cone-Hessians operational definition of h(x;M)", "watchdog-safe hand-rolled Riemann (differentiate-symbolically-then-evaluate-then-invert)", "exact-over-Q signature via real_roots(charpoly)"]
  patterns: ["matter-on-flat: g=eta+h, C from the difference potential Phi_{bg+M}-Phi_{bg}, indices raised by g^{-1}=(eta+h)^{-1}", "two-route curvature cross-check (Totaro closed-form vs hand-rolled Levi-Civita) on a genuine Hessian metric to pin sign convention"]

key-files:
  created: []
  modified:
    - "code/bulk_geometry_verification.py (Section 13: B1 rewrite of spacetime_curvature_of_g + hand_rolled_riemann_of_g + _difference_potential_subs; eig_signature_count real_roots fix; offcenter_slice_metric CENTERED-H0-TRAP docstring)"
    - "derivations/72-matter-sourcing.tex (superseded to matter-on-flat B1)"
    - ".gpd/phases/72-b-matter-sourcing/72-01-matter-on-flat.py (driver Tasks 2+3)"
    - ".gpd/phases/72-b-matter-sourcing/72-RESEARCH.md (operational-definition section banner-corrected to B1)"

key-decisions:
  - "B1 (human checkpoint:decision response, pinned by 70.1): h(x;M) := H_source(x;bg+M) - H_source(x;bg-only) [matterless reference AT THE SAME x], V_0 partner retained in both terms => cancels. Supersedes the falsified centered h := H_source - H_center."
  - "Task 2/3 use a SMALL-||M|| Lorentzian representative (V_{1/2} pattern /10, slice at center) -- the Task-1 cross-term M is OUTSIDE the small-||M|| regime under g=eta+h (signature flips to (0,4), the plan's documented perturbative boundary). In-scope parameter choice (balanced autonomy); large-M flip recorded, not a failure."
  - "hand-rolled Levi-Civita Riemann sign FLIPPED to match the engine's pinned Totaro convention (uniform -1 ratio verified across 9 components on a genuine Hessian metric => global convention flip, not a component bug)."

patterns-established:
  - "Matter-on-flat curvature: same difference-potential cubic form C, indices raised by g=eta+h NOT the bare cone-Hessian H_bg."
  - "Watchdog-safe symbolic curvature: differentiate g symbolically, EVALUATE g/dg/ddg at the rational slice point, THEN invert (rational 4x4) -- avoids the >200s all-symbolic Matrix.inv() cliff."

conventions:
  - "natural units (hbar=c=k_B=1); dimensionless differential geometry; EXACT over Q on all decisive verdicts"
  - "metric signature mostly-minus; eta = pullback of diag(+1,-1,-1,-1) via 52-kkt frame into (beta,gamma,p,q); eta_bg=[[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]] (null-aligned beta,gamma => signature by eigenvalue sign)"
  - "spacetime_metric g=eta+h(x;M); M=0 => h=0 => g=eta (R=0, DERIVED from KKT det_2, NOT inserted)"
  - "cone-Hessian g_X=Hess(-log det_3) = matter SOURCE, NOT the spacetime metric"
  - "det_3 Freudenthal cross-term 2Re((x2 x1)x3); SSOT=code/bulk_geometry_verification.py; octonion_algebra.py BANNED"
  - "Totaro Cor 2.3: R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq); Ric_jl=g^{ik}R_ijkl; R=g^{jl}Ric_jl"

plan_contract_ref: ".gpd/phases/72-b-matter-sourcing/72-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-matter-sourcing:
      status: partial
      summary: "BUILD & CONFIRM done: the curvature of g=eta+h(M) is an explicit exact-over-Q function of M (B1: difference-potential C, indices raised by g^{-1}=(eta+h)^{-1}); M=0 gives flat eta (R=S=Weyl=0, DERIVED from KKT det_2) over a NEIGHBOURHOOD; the M!=0 curvature is decomposed (n=4) and carries genuine S_munu!=0 AND Weyl!=0; the Totaro-g^{-1} route is validated against a hand-rolled Levi-Civita Riemann (exact over Q). The DECISIVE cross-term ON/OFF off-switch and the matter-sourcing VERDICT are Plan 72-02 (NOT pronounced here) -- hence partial."
      linked_ids: [deliv-phaseB, test-lambda-vs-matter, test-cross-term-association, ref-70.1-verdict, ref-totaro, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: two-route curvature cross-check + exact-over-Q flat-baseline + n=4 decomposition reconstruction
          confidence: high
          claim_id: claim-matter-sourcing
          deliverable_id: deliv-phaseB
          acceptance_test_id: test-lambda-vs-matter
          evidence_path: ".gpd/phases/72-b-matter-sourcing/72-01-LOG.md"
  deliverables:
    deliv-phaseB:
      status: partial
      path: derivations/72-matter-sourcing.tex
      summary: "Superseded to matter-on-flat (B1). Contains: curvature of g=eta+h raised by g^{-1}=(eta+h)^{-1} (index-raising correction stated); the MANDATORY hand-rolled Levi-Civita cross-check agreeing with Totaro-g^{-1} exact over Q on 3 components; the M=0 FLAT baseline (R=S=Weyl=0, DERIVED from KKT det_2, explicitly NOT R=-3/pure-Lambda/R_time x H^3); the n=4 Ricci decomposition (R, S_munu, Weyl) of the M!=0 curvature (S!=0 & Weyl!=0); signature (1,3) over Q at small M; the Phase-71 cone-Hessian SOURCE regression; the cross-term 2Re((x2 x1)x3) as the unique V_0<->V_{1/2} channel (buggy order excluded). The cross-term off-switch + verdict (CALC-03/04) remain for 72-02 by design -- hence partial."
      linked_ids: [claim-matter-sourcing, test-lambda-vs-matter, test-cross-term-association]
  acceptance_tests:
    test-lambda-vs-matter:
      status: passed
      summary: "M=0 curvature of g=eta+h is FLAT (R=S=Weyl=0) exactly over Q -- confirmed at the center, OFF-center (the neighbourhood test that defeats the disconfirming observation), and with the V_0 background partner ON (cancels in B1). NO Lambda subtraction, NO R=-3 baseline. Re-framed per 70.1: the only 'pure-Lambda' check is the trivial flat one at M=0; only the M-dependent part counts."
      linked_ids: [claim-matter-sourcing, deliv-phaseB, ref-70.1-verdict]
    test-cross-term-association:
      status: passed
      summary: "det_3 minus the block-diagonal norm == 2Re((x2 x1)x3) exactly over Q on the full symbolic X; alpha,beta,gamma absent from the triple; engine det_3 byte-identical to the certified ring_lemma_verification SSOT; buggy (x1 x2)x3 / octonion_algebra.py order excluded. (Reproduced from Task 1, committed 5f477bbf; re-run green.)"
      linked_ids: [claim-matter-sourcing, deliv-phaseB, ref-warm-engine, ref-h3o-tower]
  references:
    ref-70.1-verdict:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "AUTHORITATIVE re-scope read and applied: g=eta+h is the physical metric; M=0 flat DERIVED from KKT; cone-Hessian=source; Lambda tripwire STRUCK. Drove the B1 definition (matterless reference at same x) and the explicit NOT-R=-3 framing of the flat baseline."
    ref-prompt:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Phase-B targets + negative-result-is-success discipline honored: BUILD & CONFIRM only; verdict + off-switch deferred to 72-02; no softening, no Einstein-fitting."
    ref-totaro:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Totaro Cor 2.3 closed form applied to g=eta+h (C from the difference potential, g^{-1}=(eta+h)^{-1}); its applicability to eta+h VALIDATED by the mandatory hand-rolled Levi-Civita cross-check (exact agreement over Q)."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cone-Hessian SOURCE structure g_X = Hess(-log det) grounding the matter source; cited in the .tex conventions."
    ref-warm-engine:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Engine extended IN PLACE (Section 13); det_3 SSOT guard green (0 octonion_algebra imports, 0 float-rank on decisive path); main() ALL_PASS harness untouched (Section-13 functions not called by main())."
    ref-h3o-tower:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Cross-term association 2Re((x2 x1)x3) confirmed (Task 1); buggy order excluded."
  forbidden_proxies:
    fp-lambda-as-sourcing:
      status: rejected
      notes: "The M=0 spacetime baseline is FLAT eta (R=0, DERIVED from KKT det_2). The cone-Hessian R=-3 / {0,-1,-1,-1} / R_time x H^3 is explicitly labeled the SOURCE field's geometry, NOT the spacetime curvature; no R=-3 baseline is subtracted. The disconfirming observation (centered-h gave curved M=0 = this proxy) was DIAGNOSED and corrected to B1."
    fp-coordinate-curvature:
      status: rejected
      notes: "Indices raised with g^{-1}=(eta+h)^{-1}, NOT H_bg^{-1} (verified distinct; index-raising correction non-vacuous). The M!=0 curvature carries traceless-Ricci S_munu!=0 AND Weyl!=0 (exact over Q) -- genuine geometry, not a removable pure-trace/embedding artifact. Hand-rolled Levi-Civita cross-check confirms the intrinsic curvature."
    fp-wrong-cross-term:
      status: rejected
      notes: "SSOT det_3 cross-term 2Re((x2 x1)x3) used throughout; engine det_3 byte-identical to ring_lemma_verification; octonion_algebra.py not imported on the decisive path; buggy (x1 x2)x3 order excluded (Task 1)."
    fp-float-decisive:
      status: rejected
      notes: "All decisive quantities EXACT over Q (sympy Rational/Matrix; real_roots for signature; == comparisons). No numpy float rank/curvature. The signature helper was fixed to use exact real_roots(charpoly) rather than a float fallback."
    fp-assume-einstein:
      status: rejected
      notes: "NO factor inserted to force Ric prop. to g or to force flatness. The flat M=0 baseline is DERIVED (B1 h identically 0 in x at M=0), not fitted. The Einstein test is Phase 73; Phase 72 exposes matter-SOURCING structure only. Verdict NOT pronounced."
  uncertainty_markers:
    weakest_anchors:
      - "The matter-sourcing OUTCOME is NOVEL (no external literature for off-diagonal-Peirce content sourcing a perturbation of a flat Minkowski slice metric); validation is INTERNAL only. This plan builds the machinery; the OUTCOME confidence stays MEDIUM and is decided by the 72-02 off-switch."
      - "Totaro applicability to g=eta+h confirmed by the hand-rolled cross-check on 3 components (R_0202, R_2323, R_0101) at one representative; broader-component confirmation is available on demand but not exhaustively run."
    unvalidated_assumptions:
      - "The small-||M|| representative (pattern /10) is INSIDE the Lorentzian regime; the precise perturbative radius (where signature flips) is bracketed (sig (1,3) at /10..1/5-ish at center; flips at the large Task-1 amplitude) but not mapped exactly -- not needed for build & confirm."
    competing_explanations: []
    disconfirming_observations:
      - "RESOLVED HONESTLY: the literal engine/72-RESEARCH centered-h definition (h := H_source(x;M) - H_center, H_center constant) gave R[g](M=0)=17496 (CURVED) -- the falsified cone-Hessian-is-metric framing (fp-lambda-as-sourcing). This was the Task-2 disconfirming observation (committed e2894163). Corrected to B1 (matterless reference at same x) by human checkpoint:decision, pinned by the 70.1 verdict; B1 gives h(x;M=0)==0 identically in x => flat M=0 over a neighbourhood (exact over Q). The .tex, 72-RESEARCH operational-definition section, and offcenter_slice_metric docstring are all annotated with this trap and the B1 correction."

comparison_verdicts:
  - subject_id: claim-matter-sourcing
    subject_kind: deliverable
    subject_role: decisive
    reference_id: ref-totaro
    comparison_kind: cross_method
    metric: exact_equality_over_Q
    threshold: "R_ijkl[g] (Totaro-g^{-1}) - R_ijkl[g] (hand-rolled Levi-Civita) == 0 over Q"
    verdict: pass
    recommended_action: "Use the validated curvature-of-g engine in 72-02 for the decisive cross-term off-switch."
    notes: "Totaro closed-form (indices raised by g=eta+h) vs independent hand-rolled Levi-Civita Riemann of g=eta+h, on R_0202/R_2323/R_0101 at the small-||M|| representative. Exact agreement => Totaro applicability to eta+h validated (research Open Q1). A global sign-convention flip in the hand-rolled formula was diagnosed (uniform -1 on a genuine Hessian metric) and reconciled to the engine's pinned convention before the comparison."
  - subject_id: test-lambda-vs-matter
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-70.1-verdict
    comparison_kind: baseline
    metric: exact_equality_over_Q
    threshold: "R[g](M=0) == 0, S_munu == 0, Weyl == 0 over Q"
    verdict: pass
    recommended_action: "Treat the flat eta as the matter-on-flat baseline in 72-02; count only the M-dependent curvature."
    notes: "B1 M=0 flat baseline confirmed at center, off-center (neighbourhood test), and bg-on. DERIVED from KKT det_2, NOT an inserted Lambda; explicitly NOT R=-3 / pure-Lambda / R_time x H^3 (which is the cone-Hessian SOURCE)."
  - subject_id: claim-matter-sourcing
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-warm-engine
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "Phase-71 SOURCE anchors R{4:1/3}, R{4:1/5,5:1/7}, R(center) reproduced exactly over Q"
    verdict: pass
    recommended_action: "Proceed; SOURCE engine faithful."
    notes: "R{4:1/3}=-73041507/21967969, R{4:1/5,5:1/7}=-521269105/154700283, R(center)=-3 -- match 71-VERIFICATION. These are the cone-Hessian SOURCE field's curvatures, NOT the spacetime curvature."

duration: ~55min (this resumption segment; build-and-confirm Tasks 2+3 after the human B1 decision)
completed: 2026-06-01
---

# Phase 72-01 (matter-on-flat) Summary

**Built & confirmed the matter-on-flat curvature engine: g=eta+h(x;M) on the flat KKT-Minkowski background (B1 difference-of-cone-Hessians), M=0 FLAT over a neighbourhood (DERIVED from KKT, NOT R=-3), R[g](M)!=0 with a hand-rolled Levi-Civita Riemann agreeing with Totaro-g^{-1} exactly over Q, and an n=4 Ricci decomposition exposing genuine S!=0 & Weyl!=0 structure; the matter-sourcing verdict is deferred to 72-02.**

## Performance

- **Duration:** ~55 min (resumption segment: Tasks 2+3 after the human B1 checkpoint:decision; built on the prior agent's uncommitted `_matterless_reference_hessian` partial)
- **Completed:** 2026-06-01
- **Tasks:** 3 (Task 1 committed earlier; Tasks 2, 3 this segment)
- **Files modified:** 4 (engine, driver, .tex, 72-RESEARCH)

## Key Results

- **B1 operational definition of h (human-ratified, pinned by 70.1):** `h(x;M) := H_source(x; bg+M) - H_source(x; bg-only)` (matterless reference AT THE SAME x, V_0 partner retained in both terms => cancels). At M=0 this is `h(x;0) == 0 IDENTICALLY in x` over Q ⟹ `g=eta_bg` over a NEIGHBOURHOOD ⟹ `R[g](M=0)=0` — the genuine FLAT baseline, DERIVED from KKT det_2. **[CONFIDENCE: HIGH]**
- **Disconfirming observation resolved honestly:** the literal centered definition `h := H_source(x;M) - H_center` (H_center constant) gives `R[g](M=0)=17496` (CURVED) — the falsified cone-Hessian-is-metric framing. Corrected to B1. The .tex / 72-RESEARCH / engine docstring all carry the trap warning.
- **Curvature of g=eta+h(M):** `R[g](M) = 36619289909723558886437397679056/1933049384485442822005843957573 != 0` at the small-||M|| Lorentzian representative (V_{1/2} pattern /10, slice at center). Indices raised with `g^{-1}=(eta+h)^{-1}`, NOT the bare cone-Hessian (verified non-vacuous). **[CONFIDENCE: HIGH — exact over Q]**
- **Mandatory hand-rolled cross-check PASS:** an independent Levi-Civita Christoffel/Riemann of g=eta+h agrees with the Totaro-g^{-1} route EXACTLY over Q on R_0202, R_2323, R_0101 — validating Totaro's applicability to eta+h (research Open Q1 resolved positively). A global sign-convention flip in the hand-rolled formula was diagnosed (uniform -1 on a genuine Hessian metric) and reconciled. **[CONFIDENCE: HIGH]**
- **Lorentzian signature & perturbative boundary:** g has signature (1,3) at the small-||M|| representative (exact `real_roots` sign test); the large Task-1 cross-term amplitude flips it to (0,4) — the documented perturbative boundary, not a failure.
- **n=4 Ricci decomposition of the M!=0 curvature:** trace_g(S)=0, reconstruction R=Scal+E+Weyl=0 exact over Q; the M!=0 curvature has `R[g](M)!=0`, `S_munu!=0` AND `Weyl!=0` — genuine traceless-Ricci + Weyl structure, not a removable pure-trace/coordinate artifact. **[CONFIDENCE: HIGH for structure; the SOURCING VERDICT is 72-02]**
- **V_1-inertness:** V_1(alpha)-only matter leaves `R[g]=0` (flat); V_{1/2}-only gives `R[g]!=0`; alpha is structurally absent from the cross-term triple `2Re((x2 x1)x3)`. V_{1/2} is the active matter channel.
- **Engine faithful:** Phase-71 cone-Hessian SOURCE anchors reproduced exactly over Q (R{4:1/3}=-73041507/21967969, R{4:1/5,5:1/7}=-521269105/154700283, R(center)=-3). These are the SOURCE field's curvatures, NOT the spacetime curvature.

## Task Commits

1. **Task 1: mechanism + index audit + Phase-71 SOURCE regression** — `5f477bbf` (compute) [prior segment]
2. **Task 2 (diagnostic): disconfirming observation diagnosis** — `e2894163` (compute) [prior segment]
3. **Task 2: B1 curvature-of-g=eta+h** — `2827e68e` (compute) [this segment]
4. **Task 3: n=4 Ricci decomp + V_1-inertness + supersede .tex/RESEARCH/docstring** — `dbf228c0` (analyze) [this segment]

## Files Created/Modified

- `code/bulk_geometry_verification.py` — Section 13 B1 rewrite of `spacetime_curvature_of_g` (difference potential, `g^{-1}=(eta+h)^{-1}`) and `hand_rolled_riemann_of_g` (watchdog-safe Levi-Civita, sign reconciled to Totaro); new `_difference_potential_subs`; `eig_signature_count` fixed to exact `real_roots(charpoly)`; `offcenter_slice_metric` docstring annotated with the CENTERED-H0 TRAP.
- `derivations/72-matter-sourcing.tex` — superseded to matter-on-flat (B1): STATUS header + the M=0-obstruction/adjudication/reopened-70 sections rewritten; Task-1 CLEAN sections preserved; all LaTeX environments balanced.
- `.gpd/phases/72-b-matter-sourcing/72-01-matter-on-flat.py` — driver Tasks 2 (flat baseline neighbourhood test, curvature, mandatory cross-check, signature, perturbative-boundary demo) and 3 (decomposition, V_1-inertness, SOURCE anchor).
- `.gpd/phases/72-b-matter-sourcing/72-RESEARCH.md` — operational-definition section banner-corrected from centered-H0 to B1.

## Equations Derived

**Eq. (72.1)** — B1 matter-induced deviation (the operational definition of h):

$$
h_{\mu\nu}(x;M) := H_{\mathrm{source}}(x;\,\mathrm{bg}+M) - H_{\mathrm{source}}(x;\,\mathrm{bg\ only}),
\qquad H_{\mathrm{source}} = \mathrm{Hess}_{\mathrm{slice}}(-\log\det_3)
$$

**Eq. (72.2)** — curvature of the spacetime metric (index-raising correction):

$$
R_{ijkl}[g] = -\tfrac14\,(g^{-1})^{pq}\big(C_{jlp}C_{ikq}-C_{ilp}C_{jkq}\big),
\quad C_{ijk}=(\Phi_{\mathrm{bg}+M}-\Phi_{\mathrm{bg}})_{,ijk},
\quad g^{-1}=(\eta+h)^{-1}
$$

**Eq. (72.3)** — flat M=0 baseline (DERIVED, over a neighbourhood):

$$
h(x;0)\equiv 0 \ \Rightarrow\ g(x;0)=\eta_{\mathrm{bg}} \ \Rightarrow\ R[g](M{=}0)=S_{\mu\nu}=C^{\mathrm{Weyl}}_{ijkl}=0
$$

## Validations Completed

- M=0 flat baseline: confirmed at center, off-center (neighbourhood), and bg-on — `h≡0`, `R=S=Weyl=0` exact over Q.
- Two-route curvature cross-check: Totaro-g^{-1} == hand-rolled Levi-Civita on 3 components, exact over Q.
- Signature (1,3) at small ||M|| (exact real_roots); (0,4) flip at large M (documented boundary).
- n=4 decomposition: trace_g(S)=0 and R=Scal+E+Weyl reconstruction exact over Q.
- Index-raising non-vacuity: g^{-1}-raised R != H_bg^{-1}-raised R.
- Phase-71 SOURCE regression anchors reproduced exactly over Q (engine faithful).
- SSOT det_3 guard green; octonion_algebra.py not on the decisive path; all arithmetic exact over Q.

## Decisions Made

- **B1 (human checkpoint:decision, pinned by 70.1):** matterless reference AT THE SAME x, V_0 partner held fixed. Supersedes the falsified centered h. LOAD-BEARING for the whole 72-02 pipeline.
- **Small-||M|| Lorentzian representative for Task 2/3** (balanced-autonomy in-scope parameter choice): the Task-1 cross-term M is outside the small-||M|| regime under g=eta+h (signature flips); the plan's own `approximations` block declares this regime. Large-M flip recorded as the documented perturbative boundary.
- **Hand-rolled Riemann sign reconciled to the engine's pinned Totaro convention** (uniform -1 verified on a genuine Hessian metric => global flip, not a component bug).

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code bug] `eig_signature_count` failed on opaque radical eigenvalues**

- **Found during:** Task 2 (signature of g at the representative M)
- **Issue:** `M.eigenvals()` returned nested radicals whose `is_positive`/`is_negative` were None; the `float()` fallback raised `TypeError: Cannot convert complex to float`.
- **Fix:** Count signs of `real_roots(charpoly)` (Sturm/Descartes isolation of the exact real algebraic roots, sign-decidable), asserting `#roots == dim`. Exact over Q, no float verdict (fp-float-decisive honored).
- **Files modified:** `code/bulk_geometry_verification.py`
- **Verification:** signature (1,3,0) at small M, (0,4,0) at large M, (1,3,0) for eta_bg alone — all exact over Q.
- **Committed in:** `2827e68e`

**2. [Rule 1 - Convention] hand-rolled Levi-Civita Riemann had the opposite overall sign to the Totaro engine**

- **Found during:** Task 2 (mandatory hand-rolled cross-check initially DISAGREED)
- **Issue:** the bare Levi-Civita lower-index Riemann formula uses the opposite overall sign convention from the engine's pinned Totaro form (benchmarked to K=-1/2 for H^3).
- **Fix:** diagnosed on a genuine Hessian metric (matterless cone-Hessian, where both routes MUST agree) — the ratio hand/Totaro is a UNIFORM -1 across 9 independent components (diag+mixed+off-diag) with zeros agreeing, i.e. a single global sign flip, NOT a component bug. Carried the overall minus so the cross-check is in the engine's convention.
- **Files modified:** `code/bulk_geometry_verification.py`
- **Verification:** after the flip, Totaro-g^{-1} == hand-rolled on R_0202, R_2323, R_0101 exact over Q.
- **Committed in:** `2827e68e`

**3. [Rule 1 - Performance] watchdog stall in the fully-symbolic hand-rolled Riemann**

- **Found during:** Task 2 (first hand-rolled attempt ran >7 min and was killed)
- **Issue:** symbolic `g.inv()` of the dense 4x4 difference-Hessian + symbolic differentiation of the second-kind Christoffels blew up.
- **Fix:** differentiate g symbolically (cheap per-entry), EVALUATE g, dg, ddg at the rational slice point, THEN invert (rational 4x4) and assemble the lower-index Riemann from evaluated quantities. ~35s, exact over Q, watchdog-safe.
- **Files modified:** `code/bulk_geometry_verification.py`
- **Verification:** full driver Tasks 1+2+3 run in ~49s foreground, exit 0.
- **Committed in:** `2827e68e`

---

**Total deviations:** 3 auto-fixed (3 Rule-1: 1 code bug, 1 convention, 1 performance). **Impact:** all necessary for correctness/feasibility; no scope creep. The B1 construction itself was the human checkpoint:decision (not a deviation).

## Issues Encountered

- The Task-1 cross-term representative M (sized for non-vacuity -13/315) is outside the small-||M|| Lorentzian regime under g=eta+h. Resolved by using a small-||M|| representative for the curvature/signature confirmation and recording the large-M signature flip as the documented perturbative boundary (the plan's `approximations` block declares exactly this).

## Open Questions

- The precise perturbative radius (the ||M|| where signature flips from (1,3) to (0,4)) is bracketed but not mapped exactly — not needed for build & confirm; relevant to the 72-02 ||M||->0 controlled limit.
- Whether the M!=0 Weyl piece (now confirmed nonzero) survives the cross-term off-switch is the decisive 72-02 question.

## Next Phase Readiness

**Hands Plan 72-02 a validated curvature-of-g engine and a confirmed flat baseline.** Ready for 72-02: (i) the decisive cross-term ON/OFF off-switch (does zeroing `2Re((x2 x1)x3)` remove the M-sourced curvature of g?); (ii) the `||M||->0` controlled limit; (iii) the curvature scaling vs `||M||` / det_2; (iv) emission of `h^{(1)}` for the Phase-73 linearized-Einstein test; (v) the matter-sourcing VERDICT (SURVIVES/greenlight or honest-NEGATIVE/HALT). **The verdict is NOT pronounced here. Plan 72-02 is NOT unlocked** (downstream stays fanout-locked for the orchestrator's pre-fanout review).

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
| --- | --- | --- |
| `spacetime_curvature_of_g` (B1, validated) | 72-02 | the decisive cross-term off-switch + ||M||->0 limit operate on this exact engine |
| Flat M=0 baseline (R=S=Weyl=0, DERIVED) | 72-02, 73 | the matter-on-flat reference; only M-dependent curvature counts |
| `h(x;M)` (B1) | 73 | linearized-in-M piece h^{(1)} feeds the can-fail linearized-Einstein test |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
| --- | --- | --- |
| g=eta+h is the physical metric; M=0 flat DERIVED from KKT; cone-Hessian=source | 70.1 | Yes — B1 implements this verbatim; flat M=0 confirmed exact over Q |
| Totaro curvature engine + cone-Hessian SOURCE regression anchors | 71 | Yes — anchors reproduced exactly over Q |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| --- | --- | --- | --- |
| operational definition of h | centered: `H_source - H_center` (H_center const) | **B1: `H_source(bg+M) - H_source(bg)`** (same-x) | centered-h gives a CURVED M=0 (falsified cone-Hessian-is-metric framing); B1 gives flat M=0 over a neighbourhood (human-ratified, pinned by 70.1) |

## Self-Check: PASSED

- Files exist: 72-01-SUMMARY.md, 72-01-LOG.md, derivations/72-matter-sourcing.tex, code/bulk_geometry_verification.py — all FOUND.
- Commits exist: 2827e68e (Task 2), dbf228c0 (Task 3), 5f477bbf + e2894163 (prior) — all FOUND.
- Reproducibility: R[g](M) = 36619289909723558886437397679056/1933049384485442822005843957573 reproduced exactly on a fresh run; M=0 flat reproduced; signature (1,3); GR-guard (trace_g(S)=0, R=Scal+E+Weyl reconstruction) exact over Q.
- Convention consistency: ASSERT_CONVENTION header declares g=eta+h with the flat-DERIVED M=0 baseline; matches state.json lock (mostly-minus, det_3 cross-term (x2 x1)x3, exact over Q).
- Contract coverage: ALL PLAN contract IDs present in contract_results (1 claim, 1 deliverable, 2 acceptance tests, 6 references, 5 forbidden proxies); 3 decisive comparison_verdicts recorded.
- Discipline: matter-sourcing VERDICT NOT pronounced; cross-term off-switch NOT run; Plan 72-02 NOT unlocked (downstream stays fanout-locked).

---

_Phase: 72-b-matter-sourcing_
_Completed: 2026-06-01_
