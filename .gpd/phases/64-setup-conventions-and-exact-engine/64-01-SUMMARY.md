---
phase: 64-setup-conventions-and-exact-engine
plan: 01
depth: complex
one-liner: "Ported the verified exact-SymPy h_3(O) engine into code/ring_lemma_verification.py; established all five convention locks EXACTLY over Q (headline polarize_d(X,X,X)=6*det_3(X) over Q for the first time), built the 54-symbol pair layout + seven base invariants, froze R_pt, installed an adversarially-verified exact-only guard, and confirmed the single-state ring R[Tr,Tr^2,det] by citation"
subsystem: formalism
tags: [octonion-algebra, exceptional-jordan-algebra, F4-invariant-theory, cubic-norm, polarization, exact-symbolic, convention-lock]

requires:
  - phase: (v16.0 literature survey + roadmap)
    provides: "Unified Notation (binding conventions); Reconciliation 2 (exact engine = embedding_under_E_verification.py, NOT float64 octonion_algebra.py); FK Ch. V -> II-IV citation correction; frozen R_pt phrasing (Pitfall 7)"
provides:
  - "code/ring_lemma_verification.py: self-contained exact-SymPy assert-harness (exits 0; 25 checks)"
  - "Exact octonion + 3x3 matmul + Jordan(1/2) block (byte-faithful port of the warm engine)"
  - "Standalone Tr / Tr2=Tr(X o X) / det_3 (left-assoc) / c=Tr(X o Y) / polarize_d, exact over Q"
  - "Five convention locks established EXACTLY over Q (headline d(X,X,X)=6*det_3 first time over Q)"
  - "54-symbol pair layout (x0..x26, y0..y26, engine-native) + seven base invariants with correct bidegrees"
  - "FROZEN R_pt verbatim block (six generators; Tr(X)Tr(Y) member; claim (b) stated-not-proven) for Phases 66/67/68 to cite"
  - "Exact-only source guard (adversarially verified: catches real imports/float-rank calls, ignores prose)"
  - "Single-state ring R[Tr,Tr^2,det] confirmed by citation (FK Ch. II-IV; Ch. V correction recorded)"
affects: [65-orbit-dimension-gate, 66-c-independence-spine, 67-sym2-branching, 68-hilbert-molien, 69-reducibility-statement]

methods:
  added: ["exact-SymPy octonion arithmetic over Q", "cubic-norm polarization lock over Q", "sentinel-window exact-only source guard (import-statement + float-rank-call regex, comment-stripped)"]
  patterns: ["copy-verbatim-warm-engine into a self-contained decisive module", "assert-based _report/ALL_PASS/sys.exit harness (no pytest)", "store invariants as unexpanded SymPy expressions (no eager 54-var swell)"]

key-files:
  created: ["code/ring_lemma_verification.py", ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md"]
  modified: []

key-decisions:
  - "COPY (not import) route for the octonion block — self-contained decisive module (engine is import-safe; copy decouples from the Phase-62 file; matches slice_clause_iii precedent)"
  - "Engine-native coordinate basis for the 54 symbols (Peirce-adapted basis DEFERRED to Phase 65; invariants are basis-agnostic)"
  - "Exact-only guard matches real import STATEMENTS + float-rank CALLS (regex, comment-stripped), NOT substrings — so provenance prose does not false-fail and a genuine violation is caught"

patterns-established:
  - "R_PT_FROZEN_DEFINITION: single verbatim source-of-truth block, cited identically by Phases 66/67/68 (anti-Pitfall-7 drift)"
  - "ORACLE-FENCE-BEGIN/END sentinel window: the single sanctioned, non-decisive float touch, mechanically allowlisted by the guard"

conventions:
  - "arithmetic = EXACT over Q (SymPy Rational); NO float64 on any decisive path"
  - "ranks = sympy.Matrix(...).rank() over QQ; numpy.linalg.matrix_rank FORBIDDEN"
  - "Jordan product X o Y = (1/2)(XY + YX)"
  - "octonion Fano e1*e2 = e4; e_i*e_i = -1"
  - "det_3 cross term LEFT-assoc 2*Re((x1*x2)*x3); det_3(diag(a,b,c))=abc; det_3(I)=1"
  - "polarization d(X,X,X) = 6*det_3(X); coupling c = Tr(X o Y), bidegree (1,1)"

plan_contract_ref: ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-engine-locks:
      status: passed
      summary: "Exact octonion engine ported (byte-faithful) + Tr/Tr2/det_3/c/polarize_d lifted/re-ported; all five convention locks hold EXACTLY over Q: polarize_d(X,X,X)==6*det_3(X), c(X,X)==Tr(X^2), e1*e2==e4, det_3(diag(a,b,c))==a*b*c, det_3(I)==1. Float-det oracle confirms port (|delta|=3.55e-15)."
      linked_ids: [deliv-module, deliv-engine-block, deliv-invariant-fns, test-lock-polarize, test-lock-coupling, test-lock-fano, test-lock-diag, test-lock-identity, test-port-oracle, ref-warm-engine, ref-octonion-algebra-spec, ref-springer, ref-blind]
      evidence:
        - verifier: gpd-executor
          method: in-harness exact-over-Q assertion + adversarial float-det oracle
          confidence: high
          claim_id: claim-engine-locks
          deliverable_id: deliv-invariant-fns
          acceptance_test_id: test-lock-polarize
          reference_id: ref-blind
          evidence_path: ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md"
    claim-layout-invariants:
      status: passed
      summary: "Pair (X,Y) coordinatized by 54 SymPy symbols (x0..x26, y0..y26) on the engine-native layout, X and Y identical constructor; seven base invariants built as unexpanded SymPy expressions with verified bidegrees (1,0)/(2,0)/(3,0)/(0,1)/(0,2)/(0,3)/(1,1); round-trip exact; Tr2 distinct from (Tr)^2."
      linked_ids: [deliv-layout, deliv-invariant-fns, deliv-seven-invariants, test-layout-roundtrip, test-invariant-bidegree, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: round-trip + in-harness diagonal-slice degree checks + out-of-harness full-Poly bidegree cross-check
          confidence: high
          claim_id: claim-layout-invariants
          deliverable_id: deliv-seven-invariants
          acceptance_test_id: test-invariant-bidegree
          evidence_path: ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md"
    claim-rpt-frozen:
      status: passed
      summary: "R_pt FROZEN as the R-subalgebra generated by exactly the six single-state generators = R[..X](x)R[..Y]; Tr(X)*Tr(Y) recorded as a MEMBER; claim (b) recorded verbatim as 'c NOT IN R_pt' (STATED, not proven). is_in_Rpt stub references the six-generator definition and raises NotImplementedError (decision procedure = Phase 66)."
      linked_ids: [deliv-rpt-freeze, test-rpt-membership, test-rpt-frozen-text, ref-pitfalls, ref-project-scope]
      evidence:
        - verifier: gpd-executor
          method: in-harness prose-vs-invariants consistency + stub-raises check
          confidence: high
          claim_id: claim-rpt-frozen
          deliverable_id: deliv-rpt-freeze
          acceptance_test_id: test-rpt-membership
          reference_id: ref-pitfalls
          evidence_path: ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md"
    claim-single-state-ring:
      status: passed
      summary: "Single-state ('Observable') ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] (trdeg 3, degrees 1/2/3) confirmed BY CITATION (Faraut-Koranyi Ch. II-IV, Thm IV.2.5 region; Springer 1962/1973). Ch. V -> II-IV correction recorded verbatim. Observable single-frame ring identified with the pointwise single-copy subring. No Reynolds/Jacobian re-derivation."
      linked_ids: [deliv-single-state-doc, test-citation-recorded, ref-faraut-koranyi, ref-springer]
      evidence:
        - verifier: gpd-executor
          method: citation recorded + internal consistency (3 single-copy gens, degrees 1/2/3, trdeg 3)
          confidence: high
          claim_id: claim-single-state-ring
          deliverable_id: deliv-single-state-doc
          acceptance_test_id: test-citation-recorded
          reference_id: ref-faraut-koranyi
          evidence_path: ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md"
    claim-exact-only-guard:
      status: passed
      summary: "code/ring_lemma_verification.py embeds the SymPy octonion block; the exact-only guard confirms no 'from octonion_algebra import' and no numpy/np.linalg.matrix_rank call is reachable on the decisive path (the single aliased oa_det_3 import is fenced/allowlisted). Adversarially verified: catches injected out-of-fence import + float-rank calls, ignores provenance prose. Phases 65-67 inherit a float-free rank guarantee."
      linked_ids: [deliv-exact-guard, deliv-module, test-exact-only-guard, ref-pitfalls, ref-octonion-algebra-spec]
      evidence:
        - verifier: gpd-executor
          method: in-harness sentinel-window source scan + out-of-harness adversarial mutation test
          confidence: high
          claim_id: claim-exact-only-guard
          deliverable_id: deliv-exact-guard
          acceptance_test_id: test-exact-only-guard
          reference_id: ref-octonion-algebra-spec
          evidence_path: ".gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md"
  deliverables:
    deliv-module:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "Self-contained exact-SymPy assert harness; ALL_PASS/_report/sys.exit; exits 0 (25 checks); ASSERT_CONVENTION header present."
      linked_ids: [claim-engine-locks, claim-exact-only-guard]
    deliv-engine-block:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "FANO_TRIPLES/_MUL_TABLE/oct_*/_oct_normsq/h3o_from_coords/h3o_identity/octmat_*/h3o_matmul/jordan/_coord_from_octmat copied verbatim (AST-logic byte-faithful to engine; jordan has Rational(1,2))."
      linked_ids: [claim-engine-locks]
    deliv-invariant-fns:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "Standalone Tr, Tr2=Tr(jordan(X,X)), det_3 (left-assoc, lifted from T3), polarize_d (re-ported onto exact det_3), c=Tr(jordan(X,Y))."
      linked_ids: [claim-engine-locks, claim-layout-invariants]
    deliv-layout:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "xs=symbols('x0:27'), ys=symbols('y0:27'); X_from_symbols on engine-native layout (3 diag + 3 octonions); X and Y identical."
      linked_ids: [claim-layout-invariants]
    deliv-seven-invariants:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "Seven base invariants as unexpanded SymPy expression objects on the 54-symbol layout (Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c); bidegrees verified."
      linked_ids: [claim-layout-invariants]
    deliv-rpt-freeze:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "R_PT_FROZEN_DEFINITION verbatim block: six-generator predicate, R_pt=R[..X](x)R[..Y], Tr(X)*Tr(Y) IN R_pt, claim (b)='c NOT IN R_pt' (stated, not proven). is_in_Rpt stub."
      linked_ids: [claim-rpt-frozen]
    deliv-single-state-doc:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "SINGLE_STATE_RING_NOTE: R[Tr,Tr^2,det], trdeg 3, degrees 1/2/3, FK Ch. II-IV (Thm IV.2.5) + Springer; Ch. V -> II-IV correction recorded; Observable ring identified with the pointwise single-copy subring."
      linked_ids: [claim-single-state-ring]
    deliv-exact-guard:
      status: passed
      path: code/ring_lemma_verification.py
      summary: "exact_only_guard(): sentinel-window source scan (import-statement + float-rank-call regex, comment-stripped) + rank-routing convention; adversarially verified."
      linked_ids: [claim-exact-only-guard, claim-engine-locks]
  acceptance_tests:
    test-lock-polarize:
      status: passed
      summary: "simplify(polarize_d(Xr,Xr,Xr) - 6*det_3(Xr)) == 0 exactly over Q on a generic rational Xr (run FIRST). det_3(Xr)=631276435001/25971865920; polarize_d = exactly 6x. ESTABLISHED EXACTLY OVER Q for the first time (was float 1.4e-13)."
      linked_ids: [claim-engine-locks, deliv-invariant-fns, ref-blind]
    test-lock-coupling:
      status: passed
      summary: "simplify(c(Xr,Xr) - Tr2(Xr)) == 0 exactly over Q."
      linked_ids: [claim-engine-locks, deliv-invariant-fns]
    test-lock-fano:
      status: passed
      summary: "oct_mul(e1,e2) == e4 exactly; FANO_TRIPLES matches the documented orientation (octonion_algebra.py / Paper 7)."
      linked_ids: [claim-engine-locks, deliv-engine-block]
    test-lock-diag:
      status: passed
      summary: "simplify(det_3(diag(a,b,c)) - a*b*c) == 0 exactly over Q (symbolic a,b,c)."
      linked_ids: [claim-engine-locks, deliv-invariant-fns]
    test-lock-identity:
      status: passed
      summary: "det_3(h3o_identity()) == 1 exactly."
      linked_ids: [claim-engine-locks, deliv-invariant-fns]
    test-port-oracle:
      status: passed
      summary: "ONE-TIME non-decisive float-det oracle: float(exact det_3(Xr)) = 24.30616409870177 vs float64 octonion_algebra det_3 = 24.306164098701768; |delta| = 3.55e-15 < 1e-12. Fenced, aliased, isolated from the decisive locks."
      linked_ids: [claim-engine-locks, deliv-invariant-fns, ref-octonion-algebra-spec]
    test-layout-roundtrip:
      status: passed
      summary: "_coord_from_octmat(X_from_symbols(xs)) returns exactly (xs[0],xs[1],xs[2], xs[3:11], xs[11:19], xs[19:27]); same constructor used for ys."
      linked_ids: [claim-layout-invariants, deliv-layout]
    test-invariant-bidegree:
      status: passed
      summary: "Seven invariants exist with documented bidegrees (full-Poly cross-check); Tr2 built from jordan (not squared trace); NOT eagerly expanded (module runtime 0.57s)."
      linked_ids: [claim-layout-invariants, deliv-seven-invariants, deliv-invariant-fns]
    test-rpt-membership:
      status: passed
      summary: "R_pt freeze text contains the six generators, 'Tr(X)*Tr(Y) IN R_pt', and 'c NOT IN R_pt' (claim (b), stated not proven); is_in_Rpt stub references the six-generator definition; six generators == the six base invariants."
      linked_ids: [claim-rpt-frozen, deliv-rpt-freeze]
    test-rpt-frozen-text:
      status: passed
      summary: "R_pt documented as a single verbatim frozen-text block (R_PT_FROZEN_DEFINITION) for Phases 66/67/68 to cite; c-independence NOT asserted/proven (is_in_Rpt raises NotImplementedError); 'pointwise' not redefined."
      linked_ids: [claim-rpt-frozen, deliv-rpt-freeze]
    test-citation-recorded:
      status: passed
      summary: "Module documents R[Tr,Tr^2,det] (trdeg 3, degrees 1/2/3) with FK Ch. II-IV (Thm IV.2.5) + Springer; Ch. V -> II-IV correction recorded; Observable ring identified with the pointwise single-copy subring; no Reynolds/Jacobian re-derivation."
      linked_ids: [claim-single-state-ring, deliv-single-state-doc, ref-faraut-koranyi]
    test-exact-only-guard:
      status: passed
      summary: "Guard finds zero forbidden tokens on the decisive path (1 octonion_algebra import in-fence, 0 outside, 0 float-rank calls); rank-routing convention documented; module exits 0 only when ALL_PASS including the guard. Adversarial mutation test confirms it catches real violations and ignores prose."
      linked_ids: [claim-exact-only-guard, deliv-exact-guard, deliv-module]
  references:
    ref-warm-engine:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "code/embedding_under_E_verification.py — the exact octonion+matmul+jordan block was copied verbatim (byte-faithful), det_3/Tr lifted from its inlined T1/T3; cited in the module provenance header."
    ref-octonion-algebra-spec:
      status: completed
      completed_actions: [read, avoid]
      missing_actions: []
      summary: "code/octonion_algebra.py (float64) — det_3 (2152) / polarize_d (2184) bodies READ as the re-port spec; AVOIDED on the decisive path (exact-only guard forbids it); single sanctioned touch is the fenced one-time det oracle."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Faraut-Koranyi Ch. II-IV (Thm IV.2.5 region) cited for the single-state ring R[Tr,Tr^2,det]; Ch. V -> II-IV correction recorded."
    ref-springer:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Springer 1962/1973 cited as the cubic-norm / F_4=Aut / det-normalization anchor justifying the diagonal and identity locks and the single-state ring."
    ref-blind:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Blind 2011 Sec 3 cited for the polarization normalization d(X,X,X)=6*det X (the headline lock)."
    ref-pitfalls:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "PITFALLS Pitfall 7 + convention-trap table drove the frozen six-generator R_pt phrasing, the exact-only guard, and the Jordan-1/2 / det-left-assoc / sharp-vs-d trap avoidance."
    ref-project-scope:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "PROJECT.md reward-hacking guard honored: 'pointwise'/'reducible' not redefined; c-independence NOT asserted; v16.0 not entangled with v15.0."
  forbidden_proxies:
    fp-float-contamination:
      status: rejected
      notes: "No octonion_algebra function on the decisive path; the only import is the fenced aliased oa_det_3 for the one-time non-decisive oracle. Exact-only guard (adversarially verified) enforces this."
    fp-rpt-drift:
      status: rejected
      notes: "R_pt frozen as exactly the six-generator R-subalgebra = R[..X](x)R[..Y]; 'pointwise'/'reducible' not redefined; is_in_Rpt references the six-generator definition."
    fp-convention-trap:
      status: rejected
      notes: "Jordan 1/2 (jordan w/ Rational(1,2)) used for c & Tr2; det_3 cross term LEFT-assoc oct_mul(oct_mul(x1,x2),x3); polarize_d (NOT _polarized_sharp). All caught by the five locks; engine block reused verbatim."
    fp-clean-algebra-no-eval:
      status: rejected
      notes: "All five locks EVALUATE to exact 0 / exact value over Q in the assert harness (exit 0); no narrative-only claim; the exact-only guard prevents a false pass with a slipped float import."
    fp-overreach-independence:
      status: rejected
      notes: "c-independence (Phase 66), f_4/orbit dimension (Phase 65), Hilbert/Molien (Phase 68), and the Peirce-adapted basis (Phase 65) were NOT done; claim (b) STATED as text only. Grep confirms no such computation present."
  uncertainty_markers:
    weakest_anchors:
      - "Exact FK theorem number IV.2.5 (paywalled): MEDIUM confidence on the precise number; HIGH on the chapter range II-IV and the Ch. V -> II-IV correction. Mitigation: chapter range + Springer is the robust anchor."
      - "Engine inlined T3 == standalone octonion_algebra.py:2152 det_3 assumed exact-equal (verified by inspection): MITIGATED by the one-time float-det oracle (|delta|=3.55e-15)."
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "Any convention lock nonzero over Q (esp. d(X,X,X) != 6*det_3) would indicate a PORT ERROR — NONE occurred; all five locks exact-pass."
      - "ALL_PASS while the exact-only guard finds a forbidden token — guard is adversarially verified to catch this; no such token on the decisive path."

comparison_verdicts:
  - subject_id: test-lock-polarize
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-blind
    comparison_kind: baseline
    metric: exact_equality_over_Q
    threshold: "== 0 exactly (no tolerance)"
    verdict: pass
    recommended_action: "Reuse polarize_d / det_3 verbatim in Phases 65-69; the d=6*det_3 normalization is now exact over Q."
    notes: "Headline convention lock. polarize_d(Xr,Xr,Xr) - 6*det_3(Xr) == 0 exactly; det_3(Xr)=631276435001/25971865920, polarize_d = exactly 6x. First exact-over-Q establishment (was float 1.4e-13)."
  - subject_id: test-port-oracle
    subject_kind: acceptance_test
    subject_role: supporting
    reference_id: ref-octonion-algebra-spec
    comparison_kind: cross_method
    metric: relative_error
    threshold: "<= 1e-12"
    verdict: pass
    recommended_action: "Port-correctness confirmed; no further oracle needed (non-decisive, one-time)."
    notes: "exact float(det_3)=24.30616409870177 vs float64 octonion_algebra det_3=24.306164098701768; |delta|=3.55e-15. Fenced, aliased, off the decisive path."

duration: 13min
completed: 2026-05-25
---

# Phase 64 (BASE-01): Exact-SymPy h_3(O) Foundation Summary

**Ported the verified exact-SymPy h_3(O) engine into a self-contained `code/ring_lemma_verification.py`, established all five convention locks EXACTLY over Q (headline `polarize_d(X,X,X)=6*det_3(X)` over Q for the first time), built the 54-symbol pair layout + seven base invariants, froze R_pt as a verbatim reusable block, installed an adversarially-verified exact-only guard, and confirmed the single-state ring R[Tr,Tr^2,det] by citation.**

## Performance

- **Duration:** ~13 min
- **Started:** 2026-05-25T12:50:31Z
- **Completed:** 2026-05-25T13:04:03Z
- **Tasks:** 6 (all atomic-committed)
- **Files modified:** 2 (`code/ring_lemma_verification.py` created; `64-01-LOG.md` created)

## Key Results

- **Headline convention lock established EXACTLY over Q for the first time:** `polarize_d(X,X,X) - 6*det_3(X) == 0` exactly over Q on a generic rational element. `det_3(Xr) = 631276435001/25971865920`; `polarize_d(Xr,Xr,Xr) = 631276435001/4328644320` = exactly `6 x det_3` (`25971865920/4328644320 = 6`). Previously verified only at float tolerance 1.4e-13. [CONFIDENCE: HIGH]
- **All five convention locks PASS exactly over Q:** d=6*det_3; `c(X,X)=Tr(X^2)`; `e1*e2=e4` (Fano); `det_3(diag(a,b,c))=a*b*c`; `det_3(I)=1`. No tolerances on any decisive lock. [CONFIDENCE: HIGH]
- **Port confirmed by one-time float-det oracle:** exact `det_3 = 24.30616409870177` vs float64 reference `24.306164098701768`, `|delta| = 3.55e-15` (fenced, aliased, non-decisive). [CONFIDENCE: HIGH]
- **Seven base invariants** built on the 54-symbol engine-native layout with verified bidegrees (1,0)/(2,0)/(3,0)/(0,1)/(0,2)/(0,3)/(1,1); `Tr2 = Tr(X o X)` is distinct from `(Tr X)^2`. [CONFIDENCE: HIGH]
- **R_pt FROZEN** as the six-generator R-subalgebra `= R[..X] (x) R[..Y]`; `Tr(X)Tr(Y)` recorded as a member; claim (b) = "c NOT IN R_pt" stated (not proven). [CONFIDENCE: HIGH]
- **Exact-only guard adversarially verified:** catches genuine out-of-fence `from octonion_algebra import` and `np/numpy.linalg.matrix_rank(...)` calls; ignores provenance prose; not allowlist-by-filename. Phases 65-67 inherit a float-free rank guarantee. [CONFIDENCE: HIGH]
- **Single-state ring `R[Tr,Tr^2,det]`** (trdeg 3, degrees 1/2/3) confirmed by citation (FK Ch. II-IV; Ch. V -> II-IV correction recorded). [CONFIDENCE: HIGH on ring/chapter/correction; MEDIUM on exact theorem number IV.2.5 (paywalled)]

## Task Commits

Each task was committed atomically:

1. **Task 1: scaffold + verbatim octonion/matmul/jordan block** - `3da1014d` (setup)
2. **Task 2: lift Tr/det_3, add Tr2/c, re-port polarize_d** - `9289f879` (compute)
3. **Task 3: five convention locks exactly over Q + oracle** - `380a2794` (validate)
4. **Task 4: 54-symbol pair layout + seven base invariants** - `f29e91cc` (compute)
5. **Task 5: freeze R_pt + install exact-only guard** - `e952b05f` (validate)
6. **Task 6: single-state ring by citation** - `43040fec` (document)

## Files Created/Modified

- `code/ring_lemma_verification.py` - The frozen exact-SymPy (RING) foundation: octonion block, standalone invariants, five convention locks, 54-symbol layout + seven invariants, frozen R_pt, exact-only guard, single-state-ring citation. Assert harness, exits 0 (25 checks), runtime 0.57s.
- `.gpd/phases/64-setup-conventions-and-exact-engine/64-01-LOG.md` - Per-task research log with exact lock values, the first-result gate record, and the adversarial guard verification.

## Next Phase Readiness

- **Phase 65 (the orbit-dimension GATE):** the seven invariants, the 54-symbol layout, `jordan`, `det_3`, `polarize_d`, and the exact-only guard are all available verbatim. The engine-native basis is in place; the Peirce-adapted basis is flagged as a deliberate Phase-65 decision. The rank-routing convention (`sympy.Matrix.rank()` over QQ) is documented so the orbit-dim Jacobian rank runs float-free.
- **Phase 66 (the (b) SPINE):** `R_PT_FROZEN_DEFINITION` and the `is_in_Rpt` stub are frozen for verbatim citation; claim (b) "c not in R_pt" is stated and ready to be decided.
- **Phases 67/68:** `inv_c` (bidegree (1,1)), `Tr(X)Tr(Y)` membership in R_pt, and the 27 = 1 (+) 26 rep-decomposition (REP-DECOMP header) are recorded for the Sym^2 branching and Hilbert/Molien work.

## Contract Coverage

- **Claim IDs advanced:** claim-engine-locks -> passed; claim-layout-invariants -> passed; claim-rpt-frozen -> passed; claim-single-state-ring -> passed; claim-exact-only-guard -> passed.
- **Deliverable IDs produced:** all 8 -> passed (deliv-module, deliv-engine-block, deliv-invariant-fns, deliv-layout, deliv-seven-invariants, deliv-rpt-freeze, deliv-single-state-doc, deliv-exact-guard) at `code/ring_lemma_verification.py`.
- **Acceptance test IDs run:** all 12 -> passed (test-lock-polarize, test-lock-coupling, test-lock-fano, test-lock-diag, test-lock-identity, test-port-oracle, test-layout-roundtrip, test-invariant-bidegree, test-rpt-membership, test-rpt-frozen-text, test-citation-recorded, test-exact-only-guard).
- **Reference IDs surfaced:** all 7 -> completed (ref-warm-engine read/used/cited; ref-octonion-algebra-spec read/avoided; ref-faraut-koranyi cited/used; ref-springer cited; ref-blind cited; ref-pitfalls read/used; ref-project-scope used).
- **Forbidden proxies rejected:** all 5 -> rejected (fp-float-contamination, fp-rpt-drift, fp-convention-trap, fp-clean-algebra-no-eval, fp-overreach-independence).
- **Decisive comparison verdicts:** test-lock-polarize -> pass (exact over Q); test-port-oracle -> pass (|delta|=3.55e-15).

## Equations Established

**Eq. (64.1) — Cubic norm (det_3), left-associated cross term:**

$$
\det_3(X) = \alpha\beta\gamma - \alpha\,|x_1|^2 - \beta\,|x_2|^2 - \gamma\,|x_3|^2 + 2\,\mathrm{Re}\big((x_1 x_2)\,x_3\big)
$$

**Eq. (64.2) — Headline polarization lock (now exact over Q):**

$$
d(X,X,X) \equiv N(X+X+X) - 3N(X+X) + 3N(X) = 6\,\det_3(X)
$$

**Eq. (64.3) — Coupling / quadratic-trace lock:**

$$
c(X,Y) = \mathrm{Tr}(X\circ Y),\qquad X\circ Y = \tfrac12(XY+YX),\qquad c(X,X) = \mathrm{Tr}(X^2)
$$

**Eq. (64.4) — Frozen pointwise ring:**

$$
R_{\mathrm{pt}} = R[\mathrm{Tr}\,X,\ \mathrm{Tr}\,X^2,\ \det X]\ \otimes\ R[\mathrm{Tr}\,Y,\ \mathrm{Tr}\,Y^2,\ \det Y]
$$

**Eq. (64.5) — Single-state ("Observable") ring (by citation):**

$$
R[h_3(\mathbb{O})]^{F_4} = R[\mathrm{Tr},\ \mathrm{Tr}^2,\ \det],\qquad \mathrm{trdeg}=3,\ \text{degrees } 1,2,3
$$

## Validations Completed

- Headline lock `polarize_d(X,X,X) - 6*det_3(X) == 0` exact over Q (generic rational X). First exact-over-Q establishment.
- `c(X,X) - Tr(X^2) == 0` exact over Q (Jordan-1/2 confirmation).
- `e1*e2 == e4` exact; FANO_TRIPLES orientation matches the reference table.
- `det_3(diag(a,b,c)) - a*b*c == 0` symbolic; `det_3(I) == 1` (Springer cubic-norm normalization).
- Port-correctness float-det oracle: `|delta| = 3.55e-15 < 1e-12`.
- Layout round-trip `_coord_from_octmat(X_from_symbols(xs)) == xs` exact.
- Seven invariant bidegrees verified (diagonal slice in-harness + full-Poly out-of-harness); `Tr2 != (Tr)^2`.
- Octonion block byte-faithful (AST-logic diff) to the warm engine; `jordan` has `Rational(1,2)`; `_MUL_TABLE`/`FANO_TRIPLES` identical; `e_i*e_i = (-1,0)`.
- Exact-only guard: adversarial mutation test (catches injected import + float-rank calls, ignores prose).

## Approximations Used

None. This phase is exact-symbolic over Q end to end — no small parameter, no truncation, no convergence. Any float64 on the decisive path would be a defect; the single float touch (the port-correctness oracle) is fenced and non-decisive.

## Decisions Made

- **COPY (not import) route** for the octonion block — self-contained decisive module per the plan mandate. The warm engine is import-safe (`if __name__ == "__main__"` guard) but copy decouples the decisive module from the Phase-62 file and matches the `slice_clause_iii_verification.py` precedent. (Routine in-scope decision; balanced autonomy.)
- **Engine-native coordinate basis** for the 54 symbols; Peirce-adapted basis deferred to Phase 65 (the invariants are basis-agnostic functions of the coordinates).
- **Exact-only guard matches real import STATEMENTS + float-rank CALLS** (regex on comment-stripped lines), not substrings — handling the correctness flag that provenance prose ("octonion_algebra.py:2184", and the guard's own token mentions) must not false-fail while a genuine violation is still caught.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - code bug] Missing `expand` import**

- **Found during:** Task 4 (bidegree checks)
- **Issue:** Added `total_degree` to the sympy import but the diagonal-slice degree check also needs `expand`; `NameError` at first run.
- **Fix:** Added `expand` to the sympy import line.
- **Files modified:** `code/ring_lemma_verification.py`
- **Verification:** Re-run exits 0; all Task-4 checks pass.
- **Committed in:** `f29e91cc` (Task 4 commit)

**2. [Rule 1 - code bug] Exact-only guard false-failed on its own doc/regex token mentions**

- **Found during:** Task 5 (exact-only guard)
- **Issue:** The first guard used a raw-substring scan for `numpy.linalg.matrix_rank`, which matched the guard's OWN convention-doc comment, the `RANK_ROUTING_CONVENTION` string, and the regex pattern (3 false hits) — the exact mirror of the import-prose problem flagged by the orchestrator.
- **Fix:** Require a real call-paren `(np|numpy)\.linalg\.matrix_rank\s*\(` and strip trailing comments before scanning; match import STATEMENTS via `re.match`. Verified adversarially (catches real violations, ignores prose).
- **Files modified:** `code/ring_lemma_verification.py`
- **Verification:** Module exits 0; out-of-harness mutation test confirms catch + ignore behavior.
- **Committed in:** `e952b05f` (Task 5 commit)

---

**Total deviations:** 2 auto-fixed (2 code bugs, both correctness-only). **Impact on plan:** Both necessary for correctness; no scope creep. The guard fix hardened the deliverable per the orchestrator's correctness flag.

## Issues Encountered

- The plan deliverable `deliv-rpt-freeze` lists the token `"c not in R_pt"` (lowercase) while the acceptance test `test-rpt-membership` requires `'c NOT IN R_pt'` (uppercase). Resolved by including BOTH phrasings (the uppercase in `R_PT_FROZEN_DEFINITION`, the lowercase in the `is_in_Rpt` docstring) so deliverable and test both pass. (Rule 4 — wording coverage, correctness-only.)

## User Setup Required

None - no external configuration required. SymPy 1.14.0 + Python 3.14.2 present; the float64 `octonion_algebra.py` is touched only by the fenced one-time oracle.

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
| --- | --- | --- |
| Exact `jordan`, `det_3`, `polarize_d`, `Tr`, `Tr2`, `c` + 54-symbol layout + seven invariants | 65 (orbit-dim GATE) | Inputs to the f_4 build and the orbit-derivative / Jacobian rank (float-free via the rank-routing convention) |
| `R_PT_FROZEN_DEFINITION` + `is_in_Rpt` stub | 66 (c-independence SPINE) | Cited verbatim; the predicate against which "c not in R_pt" is decided |
| `inv_c` (bidegree (1,1)), `Tr(X)Tr(Y)` in R_pt, REP-DECOMP 27=1+26 | 67 (Sym^2 branching) | The two bidegree-(1,1) invariants and the irreducible decomposition |
| Exact-only guard + rank-routing convention | 65-67 | Inherited float-free rank guarantee |
| Single-state ring `R[Tr,Tr^2,det]` (citation) | 68 (Hilbert/Molien) | Single-copy Krull dim / Hilbert-series factor |

### Results This Phase Consumed From Earlier Phases

| Result | From | Verified Consistent |
| --- | --- | --- |
| Exact octonion+matmul+jordan engine | code/embedding_under_E_verification.py (v15.0 Phase 62) | Yes — byte-faithful AST-logic diff; jordan 1/2; FANO identical |
| det_3 / polarize_d formula bodies | code/octonion_algebra.py (float64 spec) | Yes — re-ported to exact; oracle |delta|=3.55e-15 |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| --- | --- | --- | --- |
| None — all conventions preserved | — | — | All v16.0-binding conventions from state.json carried verbatim and verified exactly over Q |

## Self-Check: PASSED

- Created files exist: `code/ring_lemma_verification.py`, `64-01-SUMMARY.md`, `64-01-LOG.md`.
- All 6 task checkpoints present (`3da1014d`, `9289f879`, `380a2794`, `f29e91cc`, `e952b05f`, `43040fec`).
- Module reproduces: re-run exits 0, ALL_PASS, 25 checks, runtime 0.57s.
- Convention consistency: single `ASSERT_CONVENTION` line; conventions match state.json `convention_lock` exactly.
- Domain-specific (math_phys): integer/rational-valued algebraic structure verified (det_3(I)=1 integer, det_3(diag)=abc, integer bidegrees); anomaly/modular/index checks N/A for pure invariant theory.
- Contract coverage COMPLETE: 5/5 claims, 8/8 deliverables, 12/12 acceptance tests, 7/7 references, 5/5 forbidden proxies (all valid status); 2 decisive comparison_verdicts (both pass). SUMMARY frontmatter parses as valid YAML.

---

_Phase: 64-setup-conventions-and-exact-engine_
_Completed: 2026-05-25_
