---
phase: 78-phase-c-circularity-audit-forced-vs-posited
plan: 01
depth: complex
one-liner: "Decisive forced-vs-posited audit (exact over Q): the MM eps-contraction is NOT forced by the h_3(O) trace form Tr(XoY)/cubic norm det_3 -- bare so(3,1) quad-curvature 4-form space dim=2 (Euler+Pontryagin), Tr supplies the symmetric eta (=> Pontryagin) but eps is reachable only as a non-unique, orientation-ambiguous metric volume form and det_3 vanishes identically on the soldered Lorentz block => fp-imported-action, the high/most-likely outcome, at true strength"
subsystem: [formalism, validation, derivation]
tags: [macdowell-mansouri, invariant-theory, exceptional-jordan, h_3(O), cubic-norm, trace-form, so(3,1), euler-pontryagin, circularity-audit, fp-imported-action, exact-over-Q]

requires:
  - phase: 77-phase-b-full-cartan-curvature-4d-gravity
    provides: "R[omega] genuine Lorentz-block Riemann of g=e.e; G[g] NOT Einstein-form intrinsically; Lambda=0 MEASURED -- so Einstein, if any, only via a posited action (the premise this phase audits)"
  - phase: 75-phase-a-coframe-reduction-kill-gate
    provides: "(E_11,u) FORCES so(3,1) (residual 21 = so(3,1)[6] (+) so(6)[15]); the soldered det_2 (1,3) Lorentzian frame metric eta (NOT the (4,0) bare-trace OP^2 foil)"
  - phase: 64.1
    provides: "det_3 = the UNIQUE F_4-invariant cubic norm (324/324 inner-derivation annihilation); the det SSOT"
provides:
  - "DECISIVE: the MM eps-contraction is NOT forced by Tr(XoY)/det_3 -> fp-imported-action (the decisive input to the 78-02 verdict ladder)"
  - "bare so(3,1)-invariant quad-in-curvature 4-form space dim=2 (Euler + Pontryagin), exact over Q, triple-confirmed (forced gens / canonical so(eta) / textbook boosts+rotations)"
  - "Tr(XoY)|frame: the (4,0) Fubini-Study FOIL vs the soldered (1,3) eta; eta supplies Pontryagin; eps NOT a tensorial fn of symmetric eta"
  - "det_3 == 0 IDENTICALLY on the soldered V_0 Lorentz block [1,2,3,10] (the cubic norm couples x1 to alpha, outside the block) => det_3 supplies no orientation/Pfaffian/normalization"
  - "the decisive triple (dim 1/2; eps-in-span YES only via the metric volume form; normalization free/imported)"
affects: [78-02, v18.0-milestone-closure, paper6-cartan-tetrad]

methods:
  added: ["so(3,1)-invariant quad-in-curvature 4-form nullspace over QQ (21-dim wedge-symmetry parameter space)", "trace-form-invariant subspace reachability (eta-tensorial vs metric-volume-form vs det_3-polarization routes)", "AST + source-string + runtime input-ban guard with string-literal/docstring stripping"]
  patterns: ["exact-over-Q invariant-theory dimension count as the operational forced-vs-posited test", "triple-independent-route confirmation of a decisive integer", "report the dimension+identity at true strength; do NOT structure to 'confirm Einstein'"]

key-files:
  created: ["code/cartan_phaseC_contraction.py", "derivations/78-circularity-audit.tex"]
  modified: []

key-decisions:
  - "The audited object is the LINEAR-in-Riemann EH term eps_{abcd} R^{ab} ^ e^c ^ e^d (the R^e^e cross-term of the eps F^F square), NOT a quadratic-in-F Pontryagin/Maxwell stress (the overturned Phase-76 tautology)."
  - "The invariant count is at the BROKEN so(3,1) level (the Spin(9,1)->SO(3,1) breaking IS the 'by hand' step being audited), using the (E_11,u)-forced so(3,1) generators (Phase 75)."
  - "Two distinct 'trace-form' metrics kept apart: the bare Jordan trace Gram diag(1,1,2,2)=(4,0) (OP^2 Fubini-Study FOIL, transparency only) vs the SOLDERED det_2 (1,3) eta (the physical spacetime frame metric). Pontryagin and the volume-form eps are built from the SOLDERED eta."
  - "Euler/Pontryagin independence certified on a GENERIC algebraic-curvature tensor (rank 2), NOT on the Phase-77 diagonal R[omega] (which gives Pontryagin==0 identically -- the exact, expected diagonal-metric fact). Deviation Rule 4."
  - "Decisive verdict INPUT reported at true strength as fp-imported-action; the FINAL verdict ladder + GST/Singh/Castro contrast + BLOCKING human ratification are 78-02 (NOT rendered here)."

patterns-established:
  - "det_3 vanishing on the soldered Lorentz block is the concrete exact-over-Q witness that the cubic norm supplies no orientation -- the sharpest closure of the eps-from-det_3 route."
  - "The symmetric-data-cannot-single-out-antisymmetric-eps argument is made QUANTITATIVE (rank{eps,Pont}=2, eps total-antisym, det_3|block=0), not asserted as a slogan."

conventions:
  - "natural units (hbar=c=k_B=1); pure algebra -- decisive output is a DIMENSION (integer) + an IDENTITY, dimensionless"
  - "metric mostly-minus (+,-,-,-) timelike-positive; frame eta=diag(+1,-1,-1,-1), signature (1,3)"
  - "EXACT over Q (sympy.Matrix.rank/nullspace over QQ); NEVER numpy.linalg, NEVER float on the decisive dimension/rank/identity"
  - "det SSOT = ring_lemma_verification.py det_3 (cross-term 2Re((x2 x1)x3), x2 BEFORE x1, Phase-64.1 fix); octonion_algebra.py BANNED"
  - "trace form c(X,Y)=Tr(X o Y)=Tr(jordan(X,Y)), jordan=(1/2)(AB+BA), F_4-invariant"
  - "frame indices a,b,c,d=0..3 (so(3,1), FORCED by (E_11,u)); soldered V_0 frame = engine idx [1,2,3,10]; V_{1/2} survivors = [11,18,19,26]"
  - "Lambda=0 at M=0 (Phase 77 MEASURED); at Lambda=0 the eps F^F action is pure Gauss-Bonnet/Euler (topological)"

plan_contract_ref: ".gpd/phases/78-phase-c-circularity-audit-forced-vs-posited/78-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-forced-einstein:
      status: partial
      summary: "DECISIVE computation complete (exact over Q) and the negative branch established: the MM eps-contraction giving Einstein-Hilbert is NOT forced by the h_3(O) trace form / cubic norm. The bare so(3,1)-invariant quad-curvature 4-form space is already 2-dim (Euler + Pontryagin); the trace form supplies the symmetric eta (=> Pontryagin reachable) but the antisymmetric eps is reachable ONLY as the metric volume form sqrt|det eta| eps (a non-unique choice vs Pontryagin, with an orientation NOT fixed by the symmetric data), and det_3 vanishes identically on the soldered Lorentz block so it supplies no orientation and no normalization. The STRONG-WIN comparison (dim==1 AND generator==eps AND det_3-fixed normalization) FAILS on all three counts => the decisive INPUT is fp-imported-action, reported at true strength. status=partial (NOT passed): 78-01 deliberately establishes only the decisive dimension+identity; the milestone-closing FINAL verdict and the BLOCKING human ratification are 78-02 (the claim's other branch, STRONG WIN, is excluded, not confirmed)."
      linked_ids: [deliv-phaseC, deliv-phaseC-code, test-forced-vs-posited, test-bare-space-dim, test-traceform-restriction, ref-mm-1977, ref-wise, ref-ring-lemma-engine, ref-orbit-gate]
      evidence:
        - verifier: gpd-executor
          method: "exact-over-Q nullspace/rank dimension count + reachability + det_3-block-vanishing, triple-independent-route confirmation of the dim=2 anchor"
          confidence: high
          claim_id: claim-forced-einstein
          deliverable_id: deliv-phaseC-code
          acceptance_test_id: test-forced-vs-posited
          reference_id: ref-ring-lemma-engine
          evidence_path: ".gpd/phases/78-phase-c-circularity-audit-forced-vs-posited/78-01-SUMMARY.md"
  deliverables:
    deliv-phaseC:
      status: partial
      path: derivations/78-circularity-audit.tex
      summary: "Phase C derivation STARTED here (completed in 78-02): documents the certified intrinsic toolkit (det_3, Tr|frame soldered eta vs (4,0) foil), the bare dim=2 anchor (Euler+Pontryagin, independent on generic curvature), Proposition det_3==0 on the Lorentz block, the eps-via-volume-form route, and the decisive triple. The verdict-ladder synthesis, GST/Singh/Castro contrast, and Lambda=0 corollary are deferred to 78-02 (per plan). Structurally valid (envs/braces balanced); pdflatex compile BLOCKED -- no LaTeX toolchain in this environment (environment gate; consistent with the carried Phase-77 'compile .tex' notation follow-up)."
      linked_ids: [claim-forced-einstein, test-forced-vs-posited, test-bare-space-dim, test-traceform-restriction]
    deliv-phaseC-code:
      status: passed
      path: code/cartan_phaseC_contraction.py
      summary: "The decisive driver: source guard (octonion_algebra/numpy absent, det SSOT native) + det_3 SSOT re-pass + Tr|frame metrics + input_ban_guard() (AST/source/runtime) + bare_invariant_space() (dim=2 nullspace over QQ, Euler+Pontryagin, generic-curvature independence) + traceform_invariant_subspace() (the decisive dimension + eps/Pontryagin reachability + det_3-fixed-vs-free normalization + the decisive triple). 32/32 PASS, exit 0, exact over Q, fully reproducible across runs. NO octonion_algebra import; NO numpy.linalg on the decisive path."
      linked_ids: [claim-forced-einstein, test-forced-vs-posited, test-bare-space-dim]
  acceptance_tests:
    test-bare-space-dim:
      status: passed
      summary: "The bare so(3,1)-invariant quad-in-curvature 4-form space is EXACTLY 2-dimensional over Q (Euler eps R^R + Pontryagin R^R), via the exact invariance nullspace delta_g T = 0 (21-dim wedge-symmetry parameter space). Euler and Pontryagin both lie in it, rank{Euler,Pontryagin}=2 (they span it), and they are independent invariants on a generic algebraic-curvature tensor (value-matrix rank 2; e.g. Euler=-2528/49, Pontryagin=416/49). TRIPLE-confirmed: forced (E_11,u) gens / canonical so(eta) / textbook boosts+rotations all give dim=2."
      linked_ids: [claim-forced-einstein, deliv-phaseC, deliv-phaseC-code]
    test-traceform-restriction:
      status: passed
      summary: "Tr(XoY) restricted to the soldered V_0 ~ R^{3,1} frame == the det_2 Lorentzian eta=diag(+1,-1,-1,-1) (signature (1,3); the bare Jordan trace Gram diag(1,1,2,2)=(4,0) is the OP^2 Fubini-Study FOIL, reported transparently, NEVER the verdict). det_3 SSOT re-passes (det_3(I)=1, det_3(diag)=abc, polarize_d=6N; Phase-64.1/65 324/324 cited). octonion_algebra.py absent; no numpy.linalg on the decisive path. Frame change-of-basis G_DET2_RAW == T^T eta T verified exact over Q."
      linked_ids: [claim-forced-einstein, deliv-phaseC, deliv-phaseC-code]
    test-forced-vs-posited:
      status: passed
      summary: "The DECISIVE exact-over-Q determination feeding the 78-02 verdict ladder. dim(trace-form-invariant subspace) = 1 (eta-tensorial: span{Pontryagin}, eps unreachable) / 2 (admitting the metric volume form: span{Pontryagin, eps}, eps NON-UNIQUE). eps-in-span = YES only via the metric volume form sqrt|det eta|=1 (orientation a discrete choice NOT fixed by the symmetric eta/det_3); det_3 supplies NO eps (det_3==0 identically on the Lorentz block). Pontryagin-in-span = YES (pure eta product). Normalization = FREE/imported (det_3==0 on the block fixes nothing). STRONG-WIN (dim==1 AND generator==eps AND det_3-fixed norm -- all three) NOT met => fp-imported-action, reported at true strength, NOT relabeled a win. No decisive number on float."
      linked_ids: [claim-forced-einstein, deliv-phaseC, deliv-phaseC-code]
  references:
    ref-mm-1977:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "MacDowell-Mansouri PRL 38 (1977) 739 cited (via 78-RESEARCH.md verbatim; executor has no web) as the SOURCE of the audited construction (the int eps F^F action), NEVER as the source of the Einstein term. The eps-contraction whose forced-vs-posited status is the verdict."
    ref-wise:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Wise gr-qc/0611154 cited for what F's blocks MEAN (A=omega+(1/l)e; F=(R-(Lambda/3)e^e)+d_omega e) and what the eps-contraction IS (the 'broken by hand' SO(4,1)->SO(3,1) locus + the EH+Lambda+GB decomposition, eq:ehexpand), NEVER as the source of the Einstein term."
    ref-gst:
      status: not_applicable
      completed_actions: []
      missing_actions: []
      summary: "GST contrast-class framing (the canonical fp-imported-action precedent) is deferred to 78-02 (the verdict synthesis + contrast plan, per the plan's must_surface:false / required_actions [cite,avoid] and the 78-RESEARCH recommended structure). Not load-bearing for the 78-01 dimension count; their Lagrangian is correctly NOT adopted."
    ref-ring-lemma-engine:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "ring_lemma_verification.py det_3/Tr/c/jordan/polarize_d USED as the ONLY admissible intrinsic invariant-tensor sources. det_3 SSOT re-passed; the forced-vs-posited question IS whether eps is reachable from Tr/det_3 -- answered NO (eps only via the metric volume form; det_3==0 on the block)."
    ref-orbit-gate:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "orbit_dimension_gate.py exact_qq_rank/span_rank_over_QQ USED (imported; __main__ NOT run) for the exact-over-Q rank/nullspace dim counts (the bare dim=2 anchor and the decisive trace-form-invariant subspace dimension)."
  forbidden_proxies:
    fp-imported-action:
      status: rejected
      notes: "REJECTED as a methodology and CONFIRMED as the honest verdict input. The plan COUNTED whether eps is forced; it did NOT posit the eps-action and expand. fp-imported-action is reported at TRUE STRENGTH as the high/most-likely real outcome (an honest partial, same class as GST/Singh/Castro), NOT relabeled a derivation. No load-bearing '\\int eps F^F'/'-1/2'/'16piG'/'MM action'/'SUSY' on the decisive path (input_ban_guard verifies; the '16piG' string in a report message is correctly NOT a code-use, and the guard still catches a genuine load-bearing violation)."
    fp-float-decisive:
      status: rejected
      notes: "Every decisive dimension/rank/identity is sympy.Matrix.rank/nullspace over QQ (exact over Q). No numpy.linalg, no float on the decisive path (source guard + input_ban_guard verify). Fully reproducible across runs."
    fp-octonion-algebra:
      status: rejected
      notes: "octonion_algebra.py NOT imported on the decisive path (source guard: not in sys.modules; det SSOT = native ring_lemma_verification det_3, det_3(diag(2,3,5))==30)."
    fp-reuse-cone-hessian:
      status: rejected
      notes: "The v17.0 symmetric/real cone-Hessian Riemann (Re(QGT)) was NOT used as load-bearing. This is the antisymmetric/Lie sector (the eps-contraction on the connection curvature); the contraction-space count uses only Tr/det_3/eta and the (E_11,u)-forced so(3,1)."
    fp-wrong-object:
      status: rejected
      notes: "The audited Einstein object is the LINEAR-in-Riemann eps_{abcd} R^{ab} ^ e^c ^ e^d (the R^e^e cross-term of eps F^F, eq:ehexpand), NOT a quadratic-in-F Maxwell/Pontryagin stress (the overturned Phase-76 tautology). The count is over the quad-in-curvature invariants whose eps-contraction yields that linear-in-R EH term."
  uncertainty_markers:
    weakest_anchors:
      - "The OUTCOME (FORCED vs POSITED) is MEDIUM by design -- that is what this phase MEASURES. It is resolved to fp-imported-action and now rests on HIGH-confidence exact-over-Q components: bare dim=2 (triple-route), Pontryagin-from-eta (exact eta-product), eps-not-tensorial-from-eta (total-antisymmetry + rank 2), det_3==0-on-block (exact symbolic + structural mechanism: x1 couples to alpha outside the block), volume-form route (det eta=-1 exact)."
    unvalidated_assumptions:
      - "The 'forced' criterion is operationalized at the BROKEN so(3,1) level (the contract/ROADMAP/PITFALLS specify this; the Spin(9,1)->SO(3,1) breaking IS the audited 'by hand' step). A reviewer arguing for the full SO(4,1)/SO(3,2) invariant count could differ -- flagged as the key modeling choice (78-RESEARCH caveat 1)."
      - "Whether the 'admit the metric volume form' reading (dim=2) or the 'eta-tensorial-only' reading (dim=1) is the canonical statement is a presentation choice; BOTH are fp-imported-action (dim=1 WITHOUT eps as the generator, or dim>=2 with eps non-unique). 78-02 renders the canonical statement."
    competing_explanations:
      - "STRONG WIN (the milestone's hopeful hypothesis: h_3(O)'s specific cubic-norm/trace-form structure forces eps where generic MM does not) is EXCLUDED by the exact count -- the exceptional-structure escape hatch does not open: det_3 vanishes on the Lorentz block, and the symmetric Tr cannot single out the antisymmetric eps over Pontryagin."
    disconfirming_observations:
      - "Bare invariant space dim != 2 would mean the so(3,1) setup is BUGGY -- it is dim=2 (triple-confirmed), so the baseline is sound."
      - "If det_3 had supplied a genuine orientation/Pfaffian on the Lorentz block, eps could be singled out -- it does NOT (det_3==0 identically there)."
      - "If the eps normalization were read off det_3, the dim=1 reading could approach a win -- it is FREE/imported (det_3==0 on the block fixes nothing)."

comparison_verdicts:
  - subject_id: claim-forced-einstein
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-ring-lemma-engine
    comparison_kind: baseline
    metric: "subspace dimension + eps-reachability + normalization (exact over Q)"
    threshold: "STRONG WIN iff dim(trace-form-invariant subspace)==1 AND generator==eps AND normalization det_3-fixed"
    verdict: fail
    recommended_action: "Render the FINAL verdict fp-imported-action in 78-02 with the GST/Singh/Castro contrast and the Lambda=0 corollary; obtain the BLOCKING human ratification (the milestone-closing verdict)."
    notes: "'fail' = STRONG-WIN condition fails (the route is NOT forced) => fp-imported-action, the HIGH/most-likely outcome and a full publishable closure (negative-result-is-success). NOT a failure of the computation: the decisive dimension+identity is established cleanly and at true strength."

duration: 33min
completed: 2026-06-02
---

# Phase 78-01: Decisive Forced-vs-Posited Circularity Audit Summary

**The MacDowell-Mansouri eps-contraction (hence the Einstein-Hilbert term) is NOT forced by the h_3(O) trace form Tr(XoY) / cubic norm det_3 -- the symmetric intrinsic data give the symmetric Pontryagin invariant for free but never single out the antisymmetric eps with a fixed coupling, and det_3 vanishes identically on the soldered Lorentz block => fp-imported-action, the high/most-likely outcome, established exact over Q at true strength.**

## Performance

- **Duration:** ~33 min
- **Started:** 2026-06-02T23:58:00Z
- **Completed:** 2026-06-03 (~00:15Z)
- **Tasks:** 3 (all auto; non-interactive plan)
- **Files created:** 2 (driver + derivation)

## Key Results

1. **The bare so(3,1)-invariant quad-in-curvature 4-form space is dim = 2** (Euler `eps R^R` + Pontryagin `R^R`), exact over Q via the invariance nullspace (21-dim wedge-symmetry parameter space). **Triple-confirmed** by three independent generator bases: the (E_11,u)-forced so(3,1) (Phase 75), the canonical so(eta), and textbook boosts+rotations. The two invariants are independent on a generic algebraic-curvature tensor (value-matrix rank 2). **=> eps is NOT unique among quadratic invariants.**
2. **Tr(XoY)|frame supplies the symmetric soldered metric eta = diag(+1,-1,-1,-1)** (signature (1,3); the bare Jordan trace Gram `diag(1,1,2,2)` = (4,0) is the OP^2 Fubini-Study FOIL, transparency only). Hence the **Pontryagin** contraction `eta^{ac}eta^{bd}` is reachable; **eps is NOT a tensorial function of the symmetric eta** (an antisymmetric eps cannot be a polynomial in symmetric eta; rank{eps,Pont}=2, eps totally antisymmetric).
3. **det_3 == 0 IDENTICALLY on the soldered V_0 Lorentz block [1,2,3,10]** (the cubic norm couples x1 to alpha, which lies OUTSIDE the {beta,gamma,p,q} block; verified symbolically `det_3(...)|_{alpha=0, block}=0`, all 64 polarization comps zero). **=> det_3 supplies no metric, no orientation, no Pfaffian, no normalization on the block** -- the eps-from-det_3 route is closed.
4. **eps is reachable ONLY via the metric volume form** `sqrt|det eta| eps` (det eta = -1 => sqrt|det eta| = 1, normalization fixed; but the ORIENTATION eps vs -eps is a discrete choice NOT fixed by the symmetric eta -- the literal "broken by hand" step). Admitting it makes the subspace dim = 2 (Pont + eps): **eps is a NON-UNIQUE choice.**
5. **THE DECISIVE TRIPLE:** `(dim = 1 (eta-tensorial: Pontryagin only) / 2 (with volume form: Pont+eps, eps non-unique); eps-in-span = YES only via the volume form; normalization = free/imported)`. In every reading the **STRONG-WIN condition fails** (dim==1 AND generator==eps AND det_3-fixed normalization -- none hold). **Decisive input = `fp-imported-action`** (the high/most-likely outcome), reported at true strength.

## Task Commits

The driver and derivation form one cohesive, exact-over-Q deliverable in which the three tasks are inseparable (Task 3 consumes Task 2's nullspace basis; Task 2 uses Task 1's forced so(3,1) and soldered eta). Verified as a unit (32/32 PASS, exit 0, reproducible) and committed atomically the moment it passed, per the commit-immediately discipline (project history of socket-timeout kills on multi-task executors):

1. **Tasks 1+2+3: the decisive driver + started derivation** -- `495303e0` (compute)
   - Task 1 (setup): det_3 SSOT re-pass; Tr|frame (4,0) foil + soldered (1,3) eta; input_ban_guard (AST/source/runtime).
   - Task 2 (anchor): bare so(3,1)-invariant quad-curvature 4-form space dim=2 (Euler+Pontryagin), triple-route confirmed, independent on generic curvature.
   - Task 3 (decisive): trace-form-invariant subspace dim + eps/Pontryagin reachability + det_3-fixed-vs-free normalization -> the decisive triple => fp-imported-action.

_Plan metadata commit follows this SUMMARY._

## Files Created/Modified

- `code/cartan_phaseC_contraction.py` - The decisive driver (source guard, det_3 SSOT re-pass, Tr|frame metrics, input_ban_guard, bare_invariant_space, traceform_invariant_subspace). 32/32 PASS, exact over Q, reproducible.
- `derivations/78-circularity-audit.tex` - Phase C derivation, STARTED here (the count, the eps-identity input, the decisive triple); the verdict synthesis + contrast + ratification are 78-02. Structurally valid; pdflatex compile blocked (no LaTeX toolchain -- environment gate).

## Equations Derived

**Eq. (78.1)** -- the MM eps-contraction decomposition (Wise; the audited object is the LINEAR-in-R cross-term):

$$
\varepsilon_{abcd}F^{ab}\wedge F^{cd}
= \underbrace{\varepsilon_{abcd}R^{ab}\wedge R^{cd}}_{\text{Gauss-Bonnet}}
- \tfrac{2\Lambda}{3}\underbrace{\varepsilon_{abcd}R^{ab}\wedge e^c\wedge e^d}_{\text{Einstein-Hilbert (LINEAR in }R)}
+ \tfrac{\Lambda^2}{9}\varepsilon_{abcd}e^a\wedge e^b\wedge e^c\wedge e^d
$$

**Eq. (78.2)** -- the bare invariant space (the sanity anchor):

$$
\dim\bigl\{\,T_{abcd}\ \text{so}(3,1)\text{-invariant, wedge-symmetric}\,\bigr\} = 2
\qquad (\text{Euler}\ \varepsilon_{abcd}\ +\ \text{Pontryagin}\ \eta_{ac}\eta_{bd}-\eta_{ad}\eta_{bc}).
$$

**Eq. (78.3)** -- det_3 on the soldered Lorentz block (the cubic norm couples x1 to alpha, outside the block):

$$
N(X)=\alpha\beta\gamma-\alpha|x_1|^2-\beta|x_2|^2-\gamma|x_3|^2+2\,\mathrm{Re}((x_2x_1)x_3),
\qquad N\big|_{\{\beta,\gamma,p,q\}}\equiv 0 .
$$

**Eq. (78.4)** -- the decisive triple (input to the 78-02 verdict ladder):

$$
\bigl(\ \dim = 1\,/\,2\ ;\quad \varepsilon\text{-in-span} = \text{YES only via }\sqrt{|\det\eta|}\,\varepsilon\ ;\quad \text{normalization} = \text{free/imported}\ \bigr)
\ \Longrightarrow\ \texttt{fp-imported-action}.
$$

## Validations Completed

- **Bare dim=2 anchor:** triple-confirmed -- forced (E_11,u) so(3,1) gens / canonical so(eta) / textbook boosts+rotations all give dim=2 (three independent physical principles, not three steps of one calculation). HIGH confidence.
- **Euler/Pontryagin independence:** rank 2 on a generic algebraic-curvature tensor (Euler=-2528/49, Pont=416/49 on one sample; rank{eps,Pont}=2 in the 21-dim tensor space). eps totally antisymmetric, Pontryagin symmetric-built.
- **det_3==0 on the block:** verified by symbolic det_3 of a general block element (`det_3(a*Ea+b*Eb+g*Eg+s*Ep+r*Eq)=abg-ar^2-as^2`, vanishes at a=0) AND by all-64-zero polarization -- with the structural MECHANISM identified (the |x1|^2 term multiplies alpha, not beta; alpha is outside the block). Cancellation-detection protocol satisfied (the near-total zero has a structural reason).
- **Reproducibility:** the decisive triple is byte-identical across two full runs (exact over Q, deterministic; no RNG, no float on any decisive path).
- **Input-ban guard:** passes on the driver AND still catches a genuine load-bearing violation (a real `numpy.linalg.matrix_rank(...)` call + a real `coupling_16piG` identifier are both flagged) -- not trivially weakened.
- **Self-critique checkpoint:** sign (orientation ambiguity is part of the verdict, not an error), factor (the 1,1,2,2 foil normalization recorded), convention (eta, det SSOT, exact-Q all held), dimension (decisive outputs are dimensionless integers/identities) -- all pass.

## Decisions Made

See `key-decisions` in frontmatter. Headline: the audited object is the LINEAR-in-R EH term (not the quadratic Pontryagin -- anti-tautology); the count is at the broken so(3,1) level (the breaking IS the audited step); the two trace-form metrics (4,0 foil vs soldered 1,3 eta) are kept apart; Euler/Pontryagin independence is certified on generic curvature (Deviation Rule 4); the decisive INPUT is reported at true strength, with the FINAL verdict + ratification deferred to 78-02.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Code bug] input_ban_guard tripped on its own report-message prose**

- **Found during:** Task 1 (input-ban guard), first run.
- **Issue:** The source-string coefficient-ban scan flagged `16piG` and `posited action` inside the `traceform_invariant_subspace` docstring and a `_report(...)` message string -- where the tokens DESCRIBE the ban/finding, not a load-bearing code use. This is the classic "guard trips on its own provenance prose" problem (which `ring_lemma.exact_only_guard` and `cartan_phaseB_einstein.ast_guard_T` explicitly handle: comment/string mentions are NOT code-uses).
- **Fix:** Added `_strip_code_only` (drop the docstring, BLANK all string-literal contents via an AST `_BlankStrings` transform, strip `#` comments) before the token scan -- mirroring the AST-only discipline of the precedent guards. The guard now passes on the driver AND still catches a genuine load-bearing violation (verified: a real numpy.linalg call + a real 16piG identifier are flagged).
- **Files modified:** `code/cartan_phaseC_contraction.py`.
- **Verification:** guard PASS on driver; guard CATCHES the injected-violation snippet `['16piG', 'numpy.linalg']`.
- **Committed in:** `495303e0`.

**2. [Rule 4 - Missing component] Euler/Pontryagin independence test object**

- **Found during:** Task 2.4 (independence on R[omega]), first run.
- **Issue:** The plan said to evaluate Euler & Pontryagin on the Phase-77 R[omega] at a rational basepoint and confirm two distinct rationals. But the Phase-77 reference tetrad `E=diag(1,1+x0^2,1,1)` is curved in a SINGLE 2-plane (4 nonzero comps, plane (0,1) only), so the 4-form `eps^{munurhosig}R^{ab}_{munu}R^{cd}_{rhosig}` -- which needs curvature in complementary planes -- vanishes for BOTH invariants (not because they are equal). This is a deficiency of the special test tetrad (diagonal metrics give Pontryagin == 0 identically), NOT of the invariants.
- **Fix:** Certified Euler/Pontryagin independence on a GENERIC algebraic-curvature tensor (full Riemann pair-symmetries; the correct generic test object) -- value-matrix rank 2 across two generic curvatures. Kept the Phase-77 R[omega] as a documented SECONDARY observation (Euler != 0 in a multi-warp variant, Pontryagin == 0 for the diagonal reference -- the exact, expected diagonal-metric fact). This is a correctness fix (right test object), not a scope change.
- **Files modified:** `code/cartan_phaseC_contraction.py`.
- **Verification:** rank 2 on generic curvature; the bare dim=2 + rank{eps,Pont}=2 in the tensor space (Task 2.3) is the primary independence proof, unaffected.
- **Committed in:** `495303e0`.

---

**Total deviations:** 2 auto-fixed (1 Rule-1 code bug, 1 Rule-4 missing-component/right-test-object). **Impact:** both necessary for correctness; no scope creep. The decisive computation and the verdict input are unchanged by either fix.

## Issues Encountered

- **pdflatex unavailable** (no LaTeX toolchain in this environment) -- an ENVIRONMENT GATE, not a physics issue. The `.tex` is structurally valid (all environments and braces balanced) and is committed for 78-02 to compile, consistent with the carried Phase-77 non-blocking "compile 77 .tex" notation follow-up.
- **Observability `.active-trace` points at a stale 70-02 trace** from a prior session; trace logging is best-effort and not load-bearing. The decisive work, commit, and SUMMARY are unaffected.

## Open Questions

- **(For 78-02, the milestone-closing verdict):** render the FINAL verdict ladder (STRONG WIN xor fp-imported-action) from this decisive triple => fp-imported-action; frame the GST/Singh/Castro contrast class (where each imports its action); note the Lambda=0 corollary (at the measured vacuum even the posited eps-action is the topological Gauss-Bonnet term -- a second, independent fp-imported-action argument); obtain the BLOCKING human ratification.
- **(Presentation choice for 78-02):** whether to state the canonical decisive dimension as 1 (eta-tensorial: Pontryagin only, eps unreachable) or 2 (admitting the metric volume form: eps non-unique) -- BOTH are fp-imported-action; 78-02 picks the canonical phrasing.

## Next Phase Readiness

The decisive exact-over-Q input to the 78-02 verdict ladder is ready and committed: the decisive triple (dim 1/2; eps-in-span YES only via the volume form; normalization free/imported) => **fp-imported-action** at true strength. 78-02 needs only the verdict-ladder synthesis, the GST/Singh/Castro contrast framing, the Lambda=0 corollary, and the BLOCKING human ratification to close milestone v18.0. The driver is fast (~seconds), exact, and reproducible -- the verifier can re-run it byte-for-byte.

## Self-Check: PASSED

- Created files exist: `code/cartan_phaseC_contraction.py`, `derivations/78-circularity-audit.tex`, this SUMMARY -- all FOUND.
- Checkpoint `495303e0` exists in git log.
- Driver reproduces: re-run exit 0, ALL_PASS, decisive verdict input `fp-imported-action` (byte-identical decisive triple across runs).
- SUMMARY frontmatter: valid YAML; `validate summary-contract` and `frontmatter validate --schema summary` both `valid: True`, 0 errors.
- Contract coverage: every PLAN contract ID present and consistent -- 1 claim (partial, the negative branch; STRONG-WIN comparison verdict=fail), 2 deliverables (code passed, derivation partial=tex-started/compile-gated), 3 acceptance tests (all passed), 5 references (4 completed + ref-gst not_applicable/deferred-to-78-02), 5 forbidden proxies (all rejected), 1 decisive comparison_verdict (fail = not-forced => fp-imported-action).
- Domain guard (mathematical physics): integer-valued invariants are integers (bare dim=2; trace-form subspace dim 1/2). PASS.

---

_Phase: 78-phase-c-circularity-audit-forced-vs-posited_
_Completed: 2026-06-02_
