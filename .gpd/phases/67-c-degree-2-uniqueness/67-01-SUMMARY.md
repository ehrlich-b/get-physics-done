---
phase: 67-c-degree-2-uniqueness
plan: 01
depth: complex
one-liner: "Proved by exact computation over Q that c = Tr(X∘Y) is the UNIQUE degree-2 coupling generator of R[27⊕27]^{F_4} mod products + pointwise terms: the bidegree-(1,1) trivial part is exactly 2-dim = span{Tr(X)Tr(Y), c} (two-route agreement: Schur End_{F_4}(1⊕26)=2 AND exact f_4-kernel nullspace=2), mod the single reducible product Tr(X)Tr(Y) the genuine-coupling quotient is span{c}"
subsystem: [computation, validation, formalism]
tags: [invariant-theory, F4, exceptional-jordan-algebra, octonions, representation-theory, exact-arithmetic, sylvester-equation, schur-lemma, degree-2-uniqueness]

requires:
  - phase: 64-engine
    provides: "FROZEN exact h_3(O) engine (jordan, Tr, Tr2, c=inv_c, det_3, 54-symbol layout xs/ys, octonionic_points, inner_derivations, is_in_Rpt stub, R_pt frozen definition)"
  - phase: 65-orbit-dimension-gate
    provides: "CERTIFIED 52-independent f_4 basis (_select_independent_basis), exact_qq_rank (DomainMatrix-over-QQ), _flatten_729 row-major (1,1) coordinate order, infinitesimal_action"
  - phase: 65.1-generating-set-count
    provides: "CANDIDATE_GRADS (index 6 = cached gradient of c), check_f4_invariance recipe, PAIR_POINTS; r7=7 preview (c independent of pointwise sextet)"
  - phase: 66-the-spine
    provides: "RING-02: c FUNCTIONALLY INDEPENDENT of R_pt (rank 7); complementary FIELD-level result"
provides:
  - "RING-03: c = Tr(X∘Y) is the UNIQUE degree-2 coupling generator mod scale + products + pointwise terms"
  - "bidegree-(1,1) trivial multiplicity = 2 over Q (the (1,1) Hilbert coefficient Phase 68 must reproduce)"
  - "full degree-2 invariant dim = 6 (blocks (2,0)=2, (1,1)=2, (0,2)=2) over Q"
  - "named basis {Tr(X)Tr(Y), c} SPANS the (1,1) kernel (in-kernel AND linearly independent; witness Tr(I)Tr(I)=9 != c(I,I)=3)"
  - "the Leibniz lift rho(M)=M⊗I+I⊗M realized as the (1,1) Sylvester condition M^T C + C M = 0 (the ONE new component)"
affects: [Phase 68 ring generation (RING-01) -- the (1,1)=2 count is the bidegree-(1,1) Hilbert coefficient; the (RING) lemma writeup]

methods:
  added: ["(1,1)-block f_4-kernel nullspace via the Sylvester/derivation condition M^T C + C M = 0 (the Leibniz lift M⊗I+I⊗M on a bilinear coefficient matrix)", "symmetric-restricted Sylvester nullspace for the (2,0)/(0,2) quadratic blocks", "named-basis identification tying an abstract nullspace dim to NAMED invariants via an exact linear-independence witness"]
  patterns: ["pre-registered two-route adjudicator (verdict ONLY on agreement; disagreement => trust exact nullspace + STOP)", "invariance gate BEFORE any dimension count", "exact-over-Q discipline with module-local source guard (0 numpy float-rank, 0 octonion_algebra)"]

key-files:
  created: ["code/degree2_uniqueness.py"]
  modified: []

key-decisions:
  - "Leibniz lift kept IMPLICIT as the diagonal gradient-contraction for the invariance gate (Task 3) and realized EXPLICITLY as the Sylvester operator C -> M^T C + C M for the (1,1) nullspace (Task 4) -- the SAME derivation rho(M)=M⊗I+I⊗M, never M⊗M (uncertainty_marker: implementation choice, not correctness)"
  - "(1,1) block computed on ALL 27x27 coefficient matrices C (a bilinear form x^T C y has independent X,Y); the (2,0)/(0,2) blocks restricted to SYMMETRIC S (a quadratic form x^T S x sees only the symmetric part)"
  - "degree-2 R_pt membership decided DIRECTLY by the bidegree/identity argument; E.is_in_Rpt (a stub that raises NotImplementedError) NOT called"

patterns-established:
  - "Pattern 1: (1,1) F_4-invariant <=> M^T C + C M = 0 for all 52 generators (the derivation/Sylvester condition); invariant dim = 729 - exact_qq_rank(stacked operator)"
  - "Pattern 2: named-basis identification (in-kernel AND rank-2 via an exact witness) defeats fp-dim-match-only -- an abstract count is tied to the NAMED invariants, not merely matched in dimension"

conventions:
  - "field: exact over Q (SymPy Rational / DomainMatrix over QQ); NEVER float64 / numpy.linalg.matrix_rank"
  - "group: F_4 = Aut(h_3(O)), 52-dim; fixes Tr, trace form, det; c F_4-invariant but NOT E_6-invariant"
  - "rep: 27 = 1 (trivial/Tr direction) ⊕ 26 (trace-free irreducible, self-dual)"
  - "jordan: X∘Y = (1/2)(XY+YX); c = Tr(X∘Y) = Tr(jordan(X,Y)); c(X,X) = Tr X^2 (NOT (Tr X)^2)"
  - "trace normalization: Tr(I) = 3 => Tr(I)Tr(I) = 9 != c(I,I) = 3 (the linear-independence witness)"
  - "Leibniz lift: rho(M) = M⊗I + I⊗M (NOT M⊗M); on a (1,1) coefficient matrix => M^T C + C M = 0"
  - "R_pt FROZEN = subalgebra gen by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}; Tr(X)Tr(Y) in R_pt, c NOT in R_pt at degree 2"
  - "metric: Riemannian Fisher (pure algebra; no field theory / gauge / Fourier)"

plan_contract_ref: ".gpd/phases/67-c-degree-2-uniqueness/67-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-branching:
      status: passed
      summary: "Route A (LITERATURE-anchored corroboration): all integer rep-theory facts hold exactly as runnable asserts -- 27=1⊕26; dim Sym^2(27)=378; dim Sym^2(26)=351=1+26+324; trivial mult in Sym^2(27)=2; bidegree-(1,1) trivial mult in 27_X⊗27_Y = dim End_{F_4}(1⊕26) = 1^2+1^2 = 2 (Schur, 27 self-dual). ROUTE_A_11=2. Dimension bookkeeping (1+26=27; 1+26+324=351; 52+273=325; 351+325=676; 1+26+351=378) self-consistent."
      linked_ids: [deliv-harness, deliv-verdict, test-branching-integers, test-dim-bookkeeping, ref-methods, ref-wikipedia-slansky, ref-garibaldi-guralnick]
      evidence:
        - verifier: gpd-executor
          method: runnable integer asserts (Route A) cross-checked against Route B exact nullspace
          confidence: high
          claim_id: claim-branching
          deliverable_id: deliv-harness
          acceptance_test_id: test-branching-integers
          reference_id: ref-methods
          evidence_path: "code/degree2_uniqueness.py"
    claim-leibniz-lift:
      status: passed
      summary: "The Leibniz lift is rho(M)=M⊗I+I⊗M (the derivation action), realized as the diagonal gradient-contraction D_M f = grad_X(f).(M.x)+grad_Y(f).(M.y) and, on a (1,1) coefficient matrix, as M^T C + C M. CORRECTNESS GUARD passed: the lift annihilates the KNOWN invariant c for ALL 52 generators over Q (52/52) at a genuinely octonionic point -- M⊗M would NOT annihilate c (fp-leibniz-MxM caught)."
      linked_ids: [deliv-harness, test-leibniz-guard, ref-orbit-gate, ref-ring-generating-set, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: annihilate-c guard (D_M c == 0 over Q, 52/52 generators)
          confidence: high
          claim_id: claim-leibniz-lift
          deliverable_id: deliv-harness
          acceptance_test_id: test-leibniz-guard
          reference_id: ref-ring-generating-set
          evidence_path: "code/degree2_uniqueness.py"
    claim-invariance-gate:
      status: passed
      summary: "Invariance gate passed BEFORE any dimension: D_M f = 0 over Q for BOTH named (1,1) candidates {c = Tr(X∘Y) = E.inv_c, Tr(X)Tr(Y) = E.inv_Tr_X*E.inv_Tr_Y} and for ALL 52 f_4 generators, at 3 genuinely octonionic rational points (diagonal) + 2 independent (X=P_i, Y=P_j) pairs (52/52 in every case). Both are genuine F_4 invariants; no candidate survives, so the dimension count is licensed."
      linked_ids: [deliv-harness, test-invariance-gate, ref-orbit-gate, ref-ring-generating-set, ref-warm-engine]
      evidence:
        - verifier: gpd-executor
          method: check_f4_invariance recipe at >=3 octonionic points + 2 independent pairs (52/52)
          confidence: high
          claim_id: claim-invariance-gate
          deliverable_id: deliv-harness
          acceptance_test_id: test-invariance-gate
          reference_id: ref-ring-generating-set
          evidence_path: "code/degree2_uniqueness.py"
    claim-nullspace-11:
      status: passed
      summary: "Route B (the self-certifying proof): the exact f_4-infinitesimal-kernel nullspace over QQ on the bidegree-(1,1) 27_X⊗27_Y monomial space has dimension exactly 2 = 729 - exact_qq_rank(Sylvester operator) = 729 - 727. The named invariants {Tr(X)Tr(Y), c} form a BASIS: both in-kernel (M^T C + C M = 0 for all 52 M) AND linearly independent over Q (rank 2; witness Tr(I)Tr(I)=9 != c(I,I)=Tr(I)=3). Dimension-match alone rejected (fp-dim-match-only); the named basis is tied to the abstract count."
      linked_ids: [deliv-harness, deliv-named-basis, test-nullspace-11-dim, test-named-basis, ref-orbit-gate, ref-warm-engine, ref-iltyakov]
      evidence:
        - verifier: gpd-executor
          method: exact_qq_rank (DomainMatrix-over-QQ) of the 729x(52*729) Sylvester operator => nullspace 2; named-basis in-kernel + rank-2 witness
          confidence: high
          claim_id: claim-nullspace-11
          deliverable_id: deliv-harness
          acceptance_test_id: test-nullspace-11-dim
          reference_id: ref-orbit-gate
          evidence_path: "code/degree2_uniqueness.py"
    claim-total-degree2:
      status: passed
      summary: "Cross-check: the FULL degree-2 invariant space is exactly 6-dimensional over Q, decomposing per-bidegree as (2,0)=2 {(Tr X)^2, Tr X^2}, (1,1)=2 {Tr(X)Tr(Y), c}, (0,2)=2 {(Tr Y)^2, Tr Y^2}. The (2,0)/(0,2) blocks are the symmetric-restricted Sylvester nullspace (378-dim symmetric space, dim 2 each); (1,1) from claim-nullspace-11. Confirms the rep-theory count by direct exact computation."
      linked_ids: [deliv-harness, deliv-verdict, test-total-degree2, ref-methods, ref-orbit-gate]
      evidence:
        - verifier: gpd-executor
          method: exact symmetric (2,0)/(0,2) nullspace (2 each) + (1,1)=2 => total 6
          confidence: high
          claim_id: claim-total-degree2
          deliverable_id: deliv-harness
          acceptance_test_id: test-total-degree2
          reference_id: ref-methods
          evidence_path: "code/degree2_uniqueness.py"
    claim-mod-products-quotient:
      status: passed
      summary: "Mod products + pointwise, c is the UNIQUE new degree-2 coupling generator: the only degree-1 invariants are Tr(X) (1,0) and Tr(Y) (0,1); the only bidegree-(1,1) product of lower-degree invariants is Tr(X)*Tr(Y), so the reducible part of the (1,1) space = span{Tr(X)Tr(Y)} (1-dim); genuine-coupling quotient = 2-1 = 1 = span{c}. 'Mod products' stated precisely: Tr(X)Tr(Y) in R_pt (a product of pointwise generators), c NOT in R_pt at degree 2 (no rational a makes c = a*Tr(X)Tr(Y): forced a=1/3 at X=I vs a=1 at X=diag(2,0,0); c(X,X)=Tr X^2 != (Tr X)^2). c unique up to scale + additive multiples of Tr(X)Tr(Y). E.is_in_Rpt NOT called (stub)."
      linked_ids: [deliv-harness, deliv-quotient-note, test-quotient-1, test-rpt-membership, ref-methods, ref-pitfalls, ref-warm-engine, ref-blind]
      evidence:
        - verifier: gpd-executor
          method: bidegree argument (reducible (1,1) = span{Tr(X)Tr(Y)}) + exact non-proportionality witness (forced a 1/3 vs 1)
          confidence: high
          claim_id: claim-mod-products-quotient
          deliverable_id: deliv-quotient-note
          acceptance_test_id: test-rpt-membership
          reference_id: ref-pitfalls
          evidence_path: "code/degree2_uniqueness.py"
    claim-two-route-agreement:
      status: passed
      summary: "The uniqueness verdict is reported ONLY because Route A (integer count = 2) and Route B (exact nullspace (1,1) = 2) AGREE, with total-degree-2 = 6 and quotient = 1 also holding. The pre-registered adjudicator emits NO verdict + STOP on disagreement (trusting the EXACT NULLSPACE, flagging Route A for re-derivation -- never tuning). On this run the agreement cell fired; the disagreement/anomaly branches are wired and force nonzero exit (not exercised here)."
      linked_ids: [deliv-harness, deliv-verdict, test-two-route-adjudicator, ref-methods, ref-pitfalls, ref-orbit-gate]
      evidence:
        - verifier: gpd-executor
          method: two-route adjudicator (ROUTE_A_11==ROUTE_B_11==2 AND total==6 AND quotient==1) -> VERDICT
          confidence: high
          claim_id: claim-two-route-agreement
          deliverable_id: deliv-verdict
          acceptance_test_id: test-two-route-adjudicator
          reference_id: ref-methods
          evidence_path: "code/degree2_uniqueness.py"
  deliverables:
    deliv-harness:
      status: passed
      path: code/degree2_uniqueness.py
      summary: "Single pre-registered, foreground-runnable (python -u, chatty) exact-over-Q harness: pre-registration block + verdict map (frozen before evaluation); Route A integer branching + bookkeeping; Leibniz lift rho(M)=M⊗I+I⊗M with annihilate-c guard; invariance gate (52 gens, >=3 octonionic points, both candidates); exact (1,1)-block nullspace=2 + named-basis identification; full degree-2 nullspace=6; mod-products quotient=1 + degree-2 R_pt membership; two-route adjudicator; exact-only source guard. main() exits 0 iff all checks pass AND the two routes agree. Runs ~50s foreground; exit 0."
      linked_ids: [claim-branching, claim-leibniz-lift, claim-invariance-gate, claim-nullspace-11, claim-total-degree2, claim-mod-products-quotient, claim-two-route-agreement]
    deliv-verdict:
      status: passed
      path: code/degree2_uniqueness.py
      summary: "Printed verdict: (1,1) trivial multiplicity Route A integer 2 vs Route B exact nullspace 2; total degree-2 dim 6; genuine-coupling quotient 1; two-route agreement line; label 'c = Tr(X o Y) is the UNIQUE degree-2 coupling generator (mod scale, products, and pointwise terms)'."
      linked_ids: [claim-branching, claim-total-degree2, claim-two-route-agreement]
    deliv-named-basis:
      status: passed
      path: code/degree2_uniqueness.py
      summary: "Named-basis identification: coordinate vectors of Tr(X)Tr(Y) and Tr(X∘Y) shown to lie in the (1,1) f_4-kernel AND be linearly independent (rank 2; Tr(I)Tr(I)=9 != c(I,I)=3), hence a BASIS of the 2-dim kernel -- not a bare dimension match."
      linked_ids: [claim-nullspace-11]
    deliv-quotient-note:
      status: passed
      path: code/degree2_uniqueness.py
      summary: "Precise 'mod products' statement + degree-2 R_pt membership decision: the only bidegree (1,1) pointwise product is Tr(X)Tr(Y) in R_pt; c not in R_pt at degree 2; quotient (2-1)=1 => c UNIQUE up to scale + additive multiples of Tr(X)Tr(Y). Records WHY the general is_in_Rpt stub is NOT called (it raises NotImplementedError; the degree-2 bidegree argument decides membership directly)."
      linked_ids: [claim-mod-products-quotient]
    deliv-consistency-note:
      status: passed
      path: code/degree2_uniqueness.py
      summary: "Scope + consistency statement: Phase 67 is the DEGREE-2 uniqueness sub-claim (RING-03), complementary to Phase 66's FIELD-level functional-independence SPINE (RING-02) and distinct from Phase 68 ring generation (RING-01). The (1,1) count 2 is the bidegree-(1,1) Hilbert coefficient Phase 68 must reproduce."
      linked_ids: [claim-two-route-agreement]
  acceptance_tests:
    test-branching-integers:
      status: passed
      summary: "All Route A integer asserts True: Sym^2(27)=378, Sym^2(26)=351=1+26+324, Sym^2(27) trivial mult=2, (1,1) trivial mult via Schur=2. ROUTE_A_11=2 recorded for the adjudicator."
      linked_ids: [claim-branching, deliv-harness, deliv-verdict]
    test-dim-bookkeeping:
      status: passed
      summary: "All five identities True: 1+26=27; 1+26+324=351; 52+273=325; 351+325=676; 1+(1*26)+351=378. Branching arithmetic internally self-consistent."
      linked_ids: [claim-branching, deliv-harness]
    test-leibniz-guard:
      status: passed
      summary: "D_M c == 0 over Q for all 52 generators (52/52) at a genuinely octonionic point -- the lift is a derivation (M⊗I+I⊗M), not M⊗M."
      linked_ids: [claim-leibniz-lift, deliv-harness]
    test-invariance-gate:
      status: passed
      summary: "All 52 generators annihilate BOTH candidates {Tr(X∘Y), Tr(X)Tr(Y)} at 3 octonionic diagonal points + 2 independent pairs (52/52 in every cell). Both are genuine F_4 invariants."
      linked_ids: [claim-invariance-gate, deliv-harness]
    test-nullspace-11-dim:
      status: passed
      summary: "The (1,1)-block invariant dimension is exactly 2 over Q: exact_qq_rank(Sylvester)=727, nullspace = 729-727 = 2. ROUTE_B_11=2 recorded. Exact over QQ (DomainMatrix), not float."
      linked_ids: [claim-nullspace-11, deliv-harness, deliv-named-basis]
    test-named-basis:
      status: passed
      summary: "The two named coordinate vectors {Tr(X)Tr(Y), c} are in the (1,1) kernel AND linearly independent (rank 2; witness Tr(I)Tr(I)=9 != c(I,I)=3) => they SPAN the 2-dim kernel. Named-basis identification, not a bare dim match."
      linked_ids: [claim-nullspace-11, deliv-harness, deliv-named-basis]
    test-total-degree2:
      status: passed
      summary: "Total degree-2 invariant dim == 6 with blocks (2,0)=2, (1,1)=2, (0,2)=2 (symmetric-restricted Sylvester for (2,0)/(0,2); (1,1) from Route B). Matches the named six-element set."
      linked_ids: [claim-total-degree2, deliv-harness, deliv-verdict]
    test-quotient-1:
      status: passed
      summary: "Quotient == 1 = (1,1) dim 2 - reducible-product dim 1. c is the UNIQUE new (irreducible, non-product) degree-2 coupling generator, unique up to scale + additive multiples of Tr(X)Tr(Y). 'Mod products' qualifier stated precisely (NOT 'c is the unique (1,1) invariant')."
      linked_ids: [claim-mod-products-quotient, deliv-harness, deliv-quotient-note]
    test-rpt-membership:
      status: passed
      summary: "Tr(X)Tr(Y) decided IN R_pt (product of frozen pointwise generators Tr X, Tr Y); c decided NOT in R_pt at degree 2 via the explicit non-proportionality witness (forced a=1/3 at X=I vs a=1 at X=diag(2,0,0); c(X,X)=Tr X^2 != (Tr X)^2). Frozen R_pt used as-is; E.is_in_Rpt NOT called (it raises)."
      linked_ids: [claim-mod-products-quotient, deliv-harness, deliv-quotient-note]
    test-two-route-adjudicator:
      status: passed
      summary: "ROUTE_A_11 == ROUTE_B_11 == 2 AND total-degree-2 == 6 AND quotient == 1 -> uniqueness VERDICT emitted. Disagreement/anomaly branches wired (print STOP, force nonzero, trust exact nullspace) but not exercised on this clean-agreement run."
      linked_ids: [claim-two-route-agreement, deliv-harness, deliv-verdict]
  references:
    ref-methods:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "METHODS (c) lines 105-118 cited for the F_4 branching chain and the precise 'mod products' statement; total degree-2 = 6 target (line 114) confirmed by direct exact computation. Conceptual chain cited, not re-derived."
    ref-pitfalls:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Pitfall 9 (26-vs-27) and Pitfall 7 (frozen R_pt anti-drift) read; target integers {2, 6, 351, 378, 1+26+324} encoded as runnable asserts; R_pt used verbatim; 'mod products' qualifier kept (NOT 'c is the unique (1,1) invariant')."
    ref-orbit-gate:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "code/orbit_dimension_gate.py reused verbatim: exact_qq_rank, _select_independent_basis (the 52 f_4 basis), _flatten_729 row-major order, infinitesimal_action. Not re-derived."
    ref-ring-generating-set:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "code/ring_generating_set.py reused: CANDIDATE_GRADS[6] (cached gradient of c), the check_f4_invariance gradient-split contraction recipe, PAIR_POINTS. The invariance-test pattern reused verbatim."
    ref-warm-engine:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "code/ring_lemma_verification.py (module E) used as the exact substrate: jordan, Tr, Tr2, c=inv_c, inv_Tr_X/inv_Tr_Y, xs/ys, octonionic_points, inner_derivations. E.is_in_Rpt (stub) deliberately NOT called. Not modified."
    ref-garibaldi-guralnick:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Garibaldi-Guralnick 2015 cited: F_4 = identity component of Stab(Tr, trace form, det); pins WHY the trace form (= c) is THE F_4-invariant (1,1) pairing (26⊗26->1 contraction) and not E_6-invariant. Grounds Route A."
    ref-wikipedia-slansky:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Wikipedia 'F4 (mathematics)' + Slansky 1981 cited for the F_4 small-irrep dimensions {1,26,52,273,324}; 324 is a genuine irrep; backs the Sym^2(26)=1+26+324 branching asserts."
    ref-iltyakov:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Iltyakov 1998 cited: F_4 several-copy invariants are trace polynomials + Laplace invariants; c = Tr(X∘Y) is a trace monomial -- supports the named-basis identification (the kernel basis is the NAMED trace invariants)."
    ref-blind:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Blind 2011 cited as the CONTRAST/limiting-case control: E_6 does NOT preserve the trace form, so c is NOT an E_6 invariant -- restricting to E_6 loses c (printed as consistency control b). Sharpens that c is genuinely the F_4 (1,1) coupling."
  forbidden_proxies:
    fp-26-vs-27:
      status: rejected
      notes: "27 = 1⊕26 carried explicitly; Sym^2(27)=378 and Sym^2(26)=351 both asserted as distinct runnable integers; trivial multiplicity in Sym^2(27) asserted = 2 (NOT 1). Sym^2(26) never substituted for Sym^2(27)."
    fp-drop-mod-products:
      status: rejected
      notes: "The (1,1) space is reported 2-dim {Tr(X)Tr(Y), c}; uniqueness is stated in the QUOTIENT mod the reducible product Tr(X)Tr(Y). The harness prints 'NOT c is the unique (1,1) invariant -- that is FALSE, Pitfall 9.2'."
    fp-float-rank:
      status: rejected
      notes: "Every decisive rank/nullspace via exact_qq_rank = DomainMatrix-over-QQ. Module-local exact_only_guard asserts 0 numpy.linalg.matrix_rank calls + 0 octonion_algebra imports on the decisive path; adversarially confirmed to FAIL on a planted octonion_algebra import."
    fp-leibniz-MxM:
      status: rejected
      notes: "Lift written as M⊗I+I⊗M (=> Sylvester M^T C + C M / diagonal gradient-contraction), guarded by annihilation of the KNOWN invariant c (52/52); M⊗M would not annihilate c."
    fp-numerical-haar:
      status: rejected
      notes: "No group-sampling / Reynolds averaging anywhere; the decisive (1,1) count is the exact f_4-infinitesimal-kernel nullspace over QQ (the Sylvester operator), not numerical Haar."
    fp-dim-match-only:
      status: rejected
      notes: "The nullspace dim 2 is TIED to the named invariants: {coord(Tr(X)Tr(Y)), coord(c)} shown in-kernel (M^T C + C M = 0 for all 52 M) AND linearly independent (rank 2; exact witness Tr(I)Tr(I)=9 != c(I,I)=3), hence a BASIS -- not a bare dimension match."
    fp-redefine-rpt:
      status: rejected
      notes: "R_pt used verbatim as the frozen subalgebra gen by the six pointwise generators; Tr(X)Tr(Y) in R_pt (a product of pointwise gens), c not in R_pt at degree 2, decided by the bidegree/identity argument. 'reducible'/'pointwise' not redefined."
    fp-assert-without-exact-witness:
      status: rejected
      notes: "The verdict is emitted ONLY on Route-A==Route-B agreement WITH the Route B exact f_4-kernel nullspace witness present; the adjudicator STOPs (no verdict, force nonzero) on disagreement, trusting the exact nullspace -- never the branching count alone, never tuning."
  uncertainty_markers:
    weakest_anchors:
      - "The VERBATIM published plethysm 'Sym^2(26)_{F_4} = 1 ⊕ 26 ⊕ 324' was not retrievable as readable text this session (MEDIUM-confidence literature gap). MITIGATED: the dimension arithmetic is fully internally self-consistent (1+26+324=351; 52+273=325; 351+325=676), the constituent irreps {1,26,52,273,324} are textbook-standard (Wikipedia/Slansky), and the DECISIVE route is the self-certifying exact-QQ nullspace, which proves the (1,1) count = 2 INDEPENDENTLY of any literature table (roadmap: TRUST THE EXACT NULLSPACE). The exact nullspace and the integer count agree."
    unvalidated_assumptions:
      - "The (0,2) block dim is computed as identical to the (2,0) block by the copy-agnostic f_4 action (the same 27x27 generators act on each copy) rather than re-running an independent Y-copy symmetric solve. This is exact (the X and Y copies carry identical 27-dim F_4 reps), not an approximation; an independent Y-only solve would reproduce it."
    competing_explanations: []
    disconfirming_observations:
      - "NONE OBSERVED. All disconfirming conditions checked and absent: (1,1) nullspace == 2 (not 1 or 3); total degree-2 == 6; the lift annihilates c (not M⊗M); the named invariants DO span the kernel (in-kernel + rank 2); Route A and Route B AGREE on (1,1)=2. Had any failed, the adjudicator would emit NO verdict and STOP (trusting the exact nullspace)."

comparison_verdicts:
  - subject_id: claim-two-route-agreement
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-methods
    comparison_kind: cross_method
    metric: integer_equality_of_bidegree_11_trivial_multiplicity
    threshold: "ROUTE_A_11 == ROUTE_B_11 == 2 (exact integer equality)"
    verdict: pass
    recommended_action: "Carry the (1,1)=2 count forward as the bidegree-(1,1) Hilbert coefficient Phase 68 must reproduce; no further action for RING-03."
    notes: "Route A (Schur: dim End_{F_4}(1⊕26) = 1^2+1^2 = 2) and Route B (exact f_4-kernel nullspace over QQ = 729-727 = 2) agree exactly; total degree-2 = 6 and quotient = 1 also hold. Exact integers, zero tolerance."
  - subject_id: claim-nullspace-11
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-iltyakov
    comparison_kind: cross_method
    metric: named_basis_spans_kernel
    threshold: "{coord(Tr(X)Tr(Y)), coord(c)} in-kernel AND rank == 2 == dim"
    verdict: pass
    recommended_action: "None -- the named basis is certified to span the kernel."
    notes: "The abstract 2-dim nullspace is tied to the NAMED trace invariants (in-kernel for all 52 generators AND linearly independent via the exact witness Tr(I)Tr(I)=9 != c(I,I)=3); not a bare dimension match (fp-dim-match-only rejected)."

duration: 11min
completed: 2026-05-27
---

# Phase 67: (c) Degree-2 Uniqueness Summary

**Proved by exact computation over Q that c = Tr(X∘Y) is the UNIQUE degree-2 coupling generator of R[27⊕27]^{F_4} mod products + pointwise terms: the bidegree-(1,1) trivial part is exactly 2-dimensional = span{Tr(X)Tr(Y), c} (two-route agreement: Schur End_{F_4}(1⊕26)=2 AND the exact f_4-kernel nullspace over QQ = 2), and modulo the single reducible product Tr(X)Tr(Y) the genuine-coupling quotient is span{c}.**

## Performance

- **Duration:** ~11 min (harness runtime ~50s foreground)
- **Started:** 2026-05-27T03:04:04Z
- **Completed:** 2026-05-27T03:15:23Z
- **Tasks:** 7 (one cohesive harness; all 7 task verification criteria pass)
- **Files modified:** 1 (`code/degree2_uniqueness.py`, created)

## Key Results

- **(1,1) trivial multiplicity = 2** over Q, established by TWO agreeing routes:
  - Route A (rep theory): dim End_{F_4}(1⊕26) = 1² + 1² = 2 (Schur; 27 = 1⊕26 self-dual).
  - Route B (the proof): exact f_4-kernel nullspace over QQ on the (1,1) block = 729 − exact_qq_rank = 729 − 727 = **2**.
- **Named basis SPANS the kernel:** {Tr(X)Tr(Y), c} are both in the (1,1) f_4-kernel AND linearly independent over Q, with the exact witness **Tr(I)Tr(I) = 9 ≠ c(I,I) = Tr(I) = 3**. (Not a bare dimension match.)
- **Full degree-2 invariant dim = 6** over Q: blocks (2,0)=2 {(Tr X)², Tr X²}, (1,1)=2 {Tr(X)Tr(Y), c}, (0,2)=2 {(Tr Y)², Tr Y²}.
- **Mod-products quotient = 1 = span{c}:** the only reducible (1,1) element is Tr(X)Tr(Y) ∈ R_pt; c ∉ R_pt at degree 2 (no rational a makes c = a·Tr(X)Tr(Y): forced a = 1/3 at X=I vs a = 1 at X=diag(2,0,0), since c(X,X)=Tr X² ≠ (Tr X)²). **c is the UNIQUE new degree-2 coupling generator, unique up to scale + additive multiples of Tr(X)Tr(Y).**

## The Central New Component (the Leibniz lift)

The ONE genuinely new piece beyond the reused engine is the lift of an f_4 generator M (27×27, diagonal action) to the 27⊗27 space: the **derivation** ρ(M) = M⊗I + I⊗M (NOT the group-like M⊗M). On a bidegree-(1,1) polynomial f(x,y) = xᵀ C y (C a 27×27 coefficient matrix):

**Eq. (67.1):** the (1,1) invariance condition

$$
D_M f = \nabla_X f \cdot (M x) + \nabla_Y f \cdot (M y) = x^{\mathsf T}\big(M^{\mathsf T} C + C M\big)\, y
\;\Longrightarrow\; f\ \text{invariant}\ \forall x,y \iff M^{\mathsf T} C + C M = 0\ \ \forall M\in\mathfrak f_4 .
$$

So the (1,1) invariant dimension = dim ker{ C ↦ (MᵀC + CM)_{M∈basis} } over QQ. The correctness guard (the lift annihilates the known invariant c, 52/52) catches the M⊗M error.

## Task Commits

The deliverable is a single cohesive harness (Tasks 2–7 add functions called only by `main()`); it was validated as a whole and committed atomically:

1. **Tasks 1–7: degree-2 uniqueness harness** — `85086874` (compute)

**Plan metadata:** (this SUMMARY + STATE update committed by the orchestrator)

Per-task verification all passed within the single harness run:
- Task 1 (PRE-REGISTER + Route A + bookkeeping): ROUTE_A_11=2; all integer/bookkeeping asserts True.
- Task 2 (Leibniz lift ρ(M)=M⊗I+I⊗M + annihilate-c guard): 52/52.
- Task 3 (invariance gate before any count): both candidates, 52/52 at 3 octonionic points + 2 independent pairs.
- Task 4 (Route B exact (1,1) nullspace + named basis): dim 2; named basis spans.
- Task 5 (full degree-2 cross-check): total 6.
- Task 6 (mod-products quotient + R_pt membership): quotient 1; Tr(X)Tr(Y)∈R_pt, c∉R_pt at degree 2.
- Task 7 (two-route adjudicator + exact-only guard): agreement verdict; guard green (planted-violation discriminated).

## Files Created/Modified

- `code/degree2_uniqueness.py` — pre-registered exact-over-Q harness for the degree-2 uniqueness sub-claim (RING-03). Imports the frozen engine (`ring_lemma_verification as E`), the certified gate machinery (`exact_qq_rank`, `_select_independent_basis`, `_flatten_729`, `infinitesimal_action`), and the Phase-65.1 candidate machinery (`CANDIDATE_GRADS`, `PAIR_POINTS`). Never touches the float64 `octonion_algebra.py`. `main()` exits 0 iff all checks pass AND the two routes agree.

## Equations Derived

**Eq. (67.1):** (1,1) invariance ⟺ Sylvester/derivation condition (above).

**Eq. (67.2):** the decisive count

$$
\dim\big(\,27_X\otimes 27_Y\,\big)^{\mathfrak f_4}_{(1,1)} \;=\; 729 - \operatorname{rank}_{\mathbb Q}\!\big[\,M^{\mathsf T}C+CM\,\big]_{M} \;=\; 729 - 727 \;=\; 2 \;=\; \operatorname{span}\{\,\mathrm{Tr}(X)\mathrm{Tr}(Y),\ \mathrm{Tr}(X\circ Y)\,\}.
$$

**Eq. (67.3):** the genuine-coupling quotient

$$
\dim\Big( (27_X\otimes 27_Y)^{\mathfrak f_4}_{(1,1)} \big/ \operatorname{span}\{\mathrm{Tr}(X)\mathrm{Tr}(Y)\} \Big) = 2 - 1 = 1 = \operatorname{span}\{\,c\,\},\qquad c \notin R_{\mathrm{pt}}\ \text{at degree 2}.
$$

## Validations Completed

- **Two-route agreement (decisive):** Route A integer 2 == Route B exact nullspace 2 == pre-registered target.
- **Named-basis spans (not dim-match):** {Tr(X)Tr(Y), c} in-kernel for all 52 generators AND rank 2 (witness 9 ≠ 3).
- **Total degree-2 = 6** cross-check (per-bidegree (2,0)=2, (1,1)=2, (0,2)=2).
- **Leibniz-lift correctness:** annihilates the known invariant c, 52/52 (rules out M⊗M).
- **Invariance gate before counting:** both (1,1) candidates pass D_M f = 0 over Q, 52/52, at ≥3 octonionic points + 2 independent pairs.
- **Limiting-case control (E_6 contrast, Blind 2011):** c is NOT an E_6 invariant — restricting to E_6 loses c (printed control b).
- **Diagonal collapse control:** X=Y restricts the (1,1) invariants to the (2,0) pointwise quadratics; c(X,X)=Tr X².
- **Exact-only source guard:** 0 numpy float-rank, 0 octonion_algebra on the decisive path; adversarially confirmed to FAIL on a planted violation.

## Decisions Made

- **Leibniz lift dual realization:** kept IMPLICIT (diagonal gradient-contraction) for the invariance gate and EXPLICIT (Sylvester operator MᵀC + CM) for the (1,1) nullspace — the same derivation ρ(M)=M⊗I+I⊗M, never M⊗M. (uncertainty_marker: implementation choice, both exact.)
- **(1,1) on all C, (2,0)/(0,2) on symmetric S:** a (1,1) bilinear form xᵀCy has independent X,Y (general C); a (2,0) quadratic form xᵀSx sees only the symmetric part (378-dim symmetric space). Both give dim 2.
- **Degree-2 R_pt membership by the bidegree/identity argument**, NOT by calling `E.is_in_Rpt` (a stub that raises NotImplementedError) — recorded in code.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing component] Added contract `must_contain` tokens `PRE-REGISTER` and `bidegree (1,1)`**

- **Found during:** post-harness deliverable-token verification (deliv-harness / deliv-quotient-note `must_contain`).
- **Issue:** the harness used `PRE-REGISTRATION` (substring "PRE-REGISTR", not "PRE-REGISTER") and `bidegree-(1,1)` (hyphen, not space) — both failed the exact-substring contract check.
- **Fix:** edited the pre-registration print line to include the literal `PRE-REGISTER`, and the Task-6 reducible-part report to include the literal `bidegree (1,1)`. Documentation/string-only; no physics or computation changed.
- **Files modified:** `code/degree2_uniqueness.py`
- **Verification:** both tokens now present (grep); harness re-run still CLEAN PASS, exit 0.
- **Committed in:** `85086874` (part of the harness commit)

---

**Total deviations:** 1 auto-fixed (1 missing component, contract-token compliance).
**Impact on plan:** documentation-only; no scope creep, no physics change.

## Issues Encountered

- **Watchdog stall risk (flagged in the plan):** Task 3 (52-generator invariance gate) and Task 4 (729-wide Sylvester nullspace) are long symbolic runs. Mitigated exactly as the plan mandated: ran FOREGROUND with `python -u`, with a one-line progress print before/after each route, each candidate, each octonionic point, and every 162 Sylvester rows. The stream never went silent; the whole harness ran ~50s. No stall.

## Open Questions

- None for RING-03. The (1,1)=2 count is now fixed as the bidegree-(1,1) Hilbert coefficient that Phase 68 (ring generation, RING-01) must reproduce.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| (1,1) trivial multiplicity | dim (27_X⊗27_Y)^{F_4}_{(1,1)} | 2 | exact (integer) | exact_qq_rank nullspace over QQ (729−727) + Schur | all of h_3(O)⊕h_3(O) |
| full degree-2 invariant dim | — | 6 | exact (integer) | exact symmetric (2,0)/(0,2) + (1,1) nullspaces | degree-2 part |
| genuine-coupling quotient | — | 1 | exact (integer) | (1,1) dim 2 − reducible product 1 | degree 2, mod R_pt |
| linear-independence witness | c(I,I), Tr(I)Tr(I) | 3, 9 | exact (integer) | xᵀCx at x=I | — |

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
| --- | --- | --- |
| bidegree-(1,1) trivial multiplicity = 2 | Phase 68 (RING-01, ring generation) | the (1,1) Hilbert coefficient the Hilbert-series / minimal-generator analysis must reproduce |
| c the UNIQUE degree-2 coupling generator mod products | (RING) lemma writeup | the (c) sub-claim seal (RING-03) |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
| --- | --- | --- |
| frozen exact engine (jordan, Tr, c, det_3, 54-symbol layout, octonionic_points, inner_derivations, frozen R_pt) | Phase 64 | Yes — imported as E, not modified; conventions match |
| 52-independent f_4 basis, exact_qq_rank, _flatten_729 | Phase 65 | Yes — \|basis\|=52 reconfirmed; exact over QQ |
| CANDIDATE_GRADS[6]=grad(c), check_f4_invariance recipe, PAIR_POINTS | Phase 65.1 | Yes — annihilate-c guard 52/52; same invariance pattern |
| c independent of R_pt (rank 7) | Phase 66 (RING-02) | Yes — complementary FIELD-level result; rank 7 ≤ trdeg 10; this phase is the DEGREE-2 (not field) statement |

### Convention Changes

| Convention | Previous | This Phase | Reason |
| --- | --- | --- | --- |
| None — all conventions preserved | | | exact over Q, 27=1⊕26, jordan 1/2, R_pt frozen, Tr(I)=3 all carried verbatim from the frozen engine |

## Self-Check: PASSED

- Files exist: `code/degree2_uniqueness.py`, `67-01-SUMMARY.md`.
- Commit exists: `85086874`.
- Reproducible: independent re-run reproduces ROUTE_B_11=2, two-route agreement, CLEAN PASS, exit 0.
- Convention consistency: exact-over-Q throughout; 0 `octonion_algebra` import lines; 0 numpy float-rank calls (exact-only guard green, adversarially confirmed to fail on a planted violation).
- Contract coverage: all 7 claims, 5 deliverables, 10 acceptance tests, 9 references, 8 forbidden proxies present in `contract_results`; 2 decisive `comparison_verdicts` (both pass); YAML frontmatter parses.
- Domain guard (mathematical physics): all reported invariants are integers (rep dims 1/26/52/273/324; nullspace dims 2/2/2); no unexplained cancellation (the 729->727 rank deficiency IS the 2-dim invariant kernel, explained by Schur).

---

_Phase: 67-c-degree-2-uniqueness_
_Completed: 2026-05-27_
