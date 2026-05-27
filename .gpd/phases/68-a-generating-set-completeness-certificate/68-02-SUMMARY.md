---
phase: 68-a-generating-set-completeness-certificate
plan: 02
depth: complex
one-liner: "CERTIFIED the 10-candidate F_4 two-copy set {6 pointwise, c, Tr(X^2oY), Tr(XoY^2), Tr(X^2oY^2)} as a COMPLETE and MINIMAL generating set of R[27+27]^{F_4} to total degree <=6 by exact-over-Q Hilbert match (d_candidate==d_true at all 28 bidegrees, exact_qq_rank, 44 generic pairs) -- NOT by assuming polarization generates (Schwarz); (2,2) Tr(X^2oY^2) DECIDED a GENERATOR (lower-product rank 8->9); the ring is FREE through degree 6 (NO syzygies; plog all {0,+1}), reported honestly against the Blind non-free expectation"

subsystem: [computation, formalism, validation]
tags: [invariant-theory, hilbert-series, generating-set, plethystic-log, minimal-generators, F4, exceptional-group, jordan-algebra, exact-arithmetic, completeness-certificate]

requires:
  - phase: 68-a-generating-set-completeness-certificate (Plan 01)
    provides: "certified bigraded dimension table d_true {d_(a,b): a+b<=6}, gate-passed + two-route-confirmed; d_(2,2)=9; (1,1)=2; Krull=10"
  - phase: 65.1-corrected-generating-set
    provides: "the 10-candidate set CANDIDATES/NAMES/BIDEGREES/BUILDERS/CANDIDATE_GRADS verbatim; PAIR_POINTS; trdeg-10 field completeness"
  - phase: 65-orbit-dimension-gate
    provides: "exact_qq_rank (DomainMatrix-over-QQ); Krull/trdeg target 10"
  - phase: 67-c-degree-2-uniqueness
    provides: "(1,1)=2 = span{Tr(X)Tr(Y), c}; the genuine-coupling quotient 1 = span{c} (the (1,1) prototype of the generator-vs-product test)"
  - phase: 66-spine
    provides: "c FUNCTIONALLY INDEPENDENT, rank 7 (cross-consistency anchor)"
provides:
  - "CERTIFIED-COMPLETE verdict: the 10-candidate set generates R[27+27]^{F_4} to total degree <=6 (d_candidate(a,b)==d_true(a,b) for ALL 28 bidegrees a+b<=6, exact over Q)"
  - "The MINIMAL generating set: all 10 candidates are genuine generators (in-span-of-lower-products test, each adds exact rank +1) with bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2),(2,2)"
  - "The (2,2) decision: Tr(X^2 o Y^2) is a GENUINE GENERATOR (its value-vector is NOT in the span of the 8 strictly-lower products; rank 8 -> 9 = d_true(2,2))"
  - "Relations catalogue: NO syzygies through total degree 6 (plethystic log all {0,+1}; the ring is FREE through deg 6; first relation, if non-free, is at total degree >= 7)"
affects: [v16.0-RING-lemma, sub-claim-a-closure, phase-69-reducibility]

methods:
  added: ["candidate-product dimension d_candidate(a,b) = exact_qq_rank of the candidate-monomial value-matrix at MANY generic rational octonionic pairs (the value of a product invariant at a point = product of candidate scalar values); points added until the rank SATURATES", "exact bivariate plethystic log plog H(s,t) = sum_k (mu(k)/k) log H(s^k,t^k) via truncated power-series log(1+u)", "in-span-of-lower-products minimality test (exact rank with/without the generator's value-vector)"]
  patterns: ["Hilbert match as the completeness certificate (Schwarz: polarization PRODUCES candidates only, NEVER assumed to generate)", "three-method agreement on the dimension (Molien d_true == monomial-count == exact_qq_rank d_candidate) as the reward-hacking tripwire", "seed-independent decisive ranks (re-run at a second seed) to reject fp-nongeneric-point"]

key-files:
  created: ["code/generating_set_certificate.py"]
  modified: []

key-decisions:
  - "VERDICT = CERTIFIED COMPLETE to total degree <=6: d_candidate(a,b) reaches d_true(a,b) at EVERY bidegree a+b<=6 (exact over Q). The 10-candidate set generates the ring to degree 6; nothing is missing."
  - "The (2,2) diagnostic RESOLVED: Tr(X^2 o Y^2) is a GENUINE GENERATOR, not a product. The 8 strictly-lower candidate products {c^2, Tr(X^2)Tr(Y^2), c*Tr(X)Tr(Y), Tr(X^2oY)*Tr(Y), Tr(XoY^2)*Tr(X), (TrX)^2(TrY)^2, Tr(X^2)(TrY)^2, (TrX)^2 Tr(Y^2)} span exactly an 8-dim space over Q; adding Tr(X^2 o Y^2) raises the rank to 9 = d_true(2,2). Its value-vector is provably NOT in the lower-product span."
  - "HONEST NON-FREE FINDING (against the Blind expectation): the plethystic log has coefficient +1 at exactly the 10 candidate bidegrees and 0 everywhere else through total degree 6, with NO NEGATIVE coefficients. The candidate set is therefore FREE through total degree 6. The plan/Blind contrast EXPECTED relations (negative plog) because the F_4 pair ring is larger than the free E_6 ring; the relations do NOT appear within the contract scope (a+b<=6). Reported honestly: the first relation, IF the ring is genuinely non-free, must occur at total degree >= 7. This is NOT the fp-e6-free-form proxy -- d_true was computed INDEPENDENTLY in Plan 01 (Molien-Weyl) and HAPPENS to match the free product through degree 6; H_free was never substituted for H_true."
  - "Polarization was used ONLY to PRODUCE candidates (the (2,1)/(1,2) mixed cubics via polarize_d are equivalent candidate-producers); the bigraded Hilbert match is the SOLE completeness certificate (Schwarz arXiv:math/0609078). fp-polarization-generates rejected."
  - "All decisive ranks are exact over Q (exact_qq_rank = DomainMatrix-over-QQ); 0 numpy float-rank, 0 octonion_algebra on the decisive path (module-local exact-only guard PASS). The decisive (2,2) generator test and (3,3) rank re-confirmed point-independent at a second random seed (rejects fp-nongeneric-point)."

patterns-established:
  - "Pattern 1: completeness by candidate-product dimension SATURATION -- enumerate ALL candidate monomials per bidegree, evaluate at generic rational octonionic pairs (product invariant value = product of candidate scalars), take exact_qq_rank, add points until the rank stabilizes; d_candidate == d_true everywhere certifies ring generation to that degree."
  - "Pattern 2: minimal-vs-spanning by the in-span-of-lower-products exact test -- a candidate is a GENUINE generator iff appending its value-vector to the strictly-lower-product value-matrix raises the exact rank by 1; this distinguishes a minimal generating set from a Reynolds spanning set (Pitfall 8) and decides generator-vs-product at every bidegree (the (2,2) headline)."

conventions:
  - "jordan(A,B) = (1/2)(AB+BA); c = Tr(X o Y) = Tr(jordan(X,Y)); c(X,X)=Tr(X^2) (NOT (Tr X)^2)"
  - "det_3 cross-term = 2 Re((x2 x1) x3) (Phase 64.1 factor-order fix); polarize_d: d(X,X,X)=6 det_3"
  - "10-candidate set with bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2),(2,2) verbatim from ring_generating_set.py"
  - "R_pt frozen = R-subalgebra gen by the 6 pointwise; Tr(X)Tr(Y) in R_pt; c NOT in R_pt"
  - "gen_func vars s=X-degree, t=Y-degree; H(s,t) bigraded; H_free != H_true assumed a priori (F_4 ring expected non-free; Blind E_6 is the FREE contrast) -- but FOUND free through deg 6 (computed, not assumed)"
  - "arithmetic exact over Q; ranks/nullspace via exact_qq_rank = DomainMatrix-over-QQ; NEVER numpy.linalg.matrix_rank / SVD on the decisive path"
  - "polarization used ONLY to PRODUCE candidates (Schwarz); the Hilbert match is the certificate"
  - "Krull = 10 (Phase 65, the superseded 7 is FORBIDDEN); trdeg 10 (65/65.1); SPINE rank 7 (66); (1,1)=2 (67)"
  - "metric = (+,+,...,+) Riemannian Fisher (pure algebra; no field theory/gauge/Fourier)"

plan_contract_ref: ".gpd/phases/68-a-generating-set-completeness-certificate/68-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-candidate-set:
      status: passed
      summary: "The 10-candidate F_4 two-copy generating set is assembled VERBATIM from ring_generating_set.py with explicit bidegrees (six pointwise (1,0),(2,0),(3,0),(0,1),(0,2),(0,3); c=Tr(XoY) (1,1); mixed trace monomials Tr(X^2oY) (2,1), Tr(XoY^2) (1,2), Tr(X^2oY^2) (2,2)). All 10 re-confirmed F_4-invariant (D_M f=0 for 52/52 generators at a diagonal octonionic point + an independent pair). Polarization (polarize_d) is used ONLY to PRODUCE the equivalent mixed-cubic candidates -- NOWHERE as evidence of completeness (Schwarz guard, stated in-code and at runtime)."
      linked_ids: [deliv-cert-code, deliv-candidate-table, test-candidate-bidegrees, test-no-polarization-assumption, ref-ring-gen-set, ref-iltyakov, ref-schwarz, ref-polarize]
      evidence:
        - verifier: gpd-executor
          method: "verbatim load + bidegree assertion + D_M f=0 invariance re-check (52/52, diagonal + independent pair)"
          confidence: high
          claim_id: claim-candidate-set
          deliverable_id: deliv-candidate-table
          acceptance_test_id: test-candidate-bidegrees
          reference_id: ref-ring-gen-set
          evidence_path: "code/generating_set_certificate.py"
    claim-minimality:
      status: passed
      summary: "Each of the 10 candidates is a GENUINE (minimal) generator: appending its value-vector to the value-matrix of the products of strictly-lower-degree candidates landing at its bidegree raises the exact_qq_rank by exactly 1 (its value-vector is NOT in the lower-product span), evaluated at 44 generic rational octonionic pairs. Increments: Tr X 0->1, Tr X^2 1->2, det X 2->3, Tr Y 0->1, Tr Y^2 1->2, det Y 2->3, c 1->2, Tr(X^2oY) 3->4, Tr(XoY^2) 3->4, Tr(X^2oY^2) 8->9. Spanning is explicitly distinguished from minimal generating (Pitfall 8): no candidate is reducible."
      linked_ids: [deliv-cert-code, deliv-minimality-table, test-minimality, test-spanning-vs-minimal, ref-ring-gen-set, ref-frozen-degree2]
      evidence:
        - verifier: gpd-executor
          method: "in-span-of-lower-products exact_qq_rank test per generator (rank with vs without G's value-vector)"
          confidence: high
          claim_id: claim-minimality
          deliverable_id: deliv-minimality-table
          acceptance_test_id: test-minimality
          reference_id: ref-frozen-degree2
          evidence_path: "code/generating_set_certificate.py"
    claim-22-decision:
      status: passed
      summary: "The (2,2) diagnostic is DECIDED: Tr(X^2 o Y^2) is a GENUINE GENERATOR, not a product. The 8 strictly-lower candidate products at (2,2) {c^2, Tr(X^2)Tr(Y^2), c*Tr(X)Tr(Y), Tr(X^2oY)*Tr(Y), Tr(XoY^2)*Tr(X), (TrX)^2(TrY)^2, Tr(X^2)(TrY)^2, (TrX)^2 Tr(Y^2)} have exact_qq_rank 8; appending Tr(X^2oY^2) raises it to 9 = d_true(2,2) (Plan 01). Its value-vector is provably NOT in the lower-product span. Re-confirmed point-independent at a second random seed. (Field-completeness put Tr(X^2oY^2) in the trdeg-10 set; ring generation is the STRICTER question -- decided here.)"
      linked_ids: [deliv-cert-code, deliv-minimality-table, test-22-decision, ref-ring-gen-set, ref-frozen-degree2, ref-plan01-table]
      evidence:
        - verifier: gpd-executor
          method: "cross-method: exact_qq_rank of the 8 lower products (=8) + the in-span test (8->9) vs d_true(2,2)=9 from Plan 01; seed-independence re-check"
          confidence: high
          claim_id: claim-22-decision
          deliverable_id: deliv-minimality-table
          acceptance_test_id: test-22-decision
          reference_id: ref-plan01-table
          evidence_path: "code/generating_set_certificate.py"
    claim-completeness:
      status: passed
      summary: "CERTIFIED COMPLETE to total degree <=6: the candidate-product dimension d_candidate(a,b) (exact_qq_rank of the candidate-monomial value-matrix, 44 generic pairs, SATURATED) equals d_true(a,b) (Plan 01 Molien) at EVERY one of the 28 bidegrees a+b<=6. The plethystic log plog H(s,t) has coefficient +1 at exactly the 10 candidate bidegrees and 0 elsewhere through degree 6, with NO positive coefficient at a non-candidate bidegree (no missing generator) and NO negative coefficient (no syzygy through degree 6 -- the ring is FREE through total degree 6). Polarization was NOT assumed to generate; the Hilbert match (d_true computed independently in Plan 01) is the certificate (Schwarz). The Blind non-free expectation is reported honestly: the first relation, if any, is at total degree >= 7 (beyond scope). fp-e6-free-form rejected (H_free never substituted for H_true; the independently-computed d_true HAPPENS to match the free product through deg 6)."
      linked_ids: [deliv-cert-code, deliv-verdict, test-hilbert-match, test-plog, test-verdict-honest, ref-plan01-table, ref-derksen-kemper, ref-hanany, ref-schwarz, ref-blind]
      evidence:
        - verifier: gpd-executor
          method: "benchmark: d_true(a,b) (Plan 01) vs d_candidate(a,b) (exact_qq_rank) at all 28 bidegrees + plethystic-log generator/relation separation + independent monomial-count cross-check"
          confidence: high
          claim_id: claim-completeness
          deliverable_id: deliv-verdict
          acceptance_test_id: test-hilbert-match
          reference_id: ref-plan01-table
          evidence_path: "code/generating_set_certificate.py"
  deliverables:
    deliv-cert-code:
      status: passed
      path: code/generating_set_certificate.py
      summary: "The generating-set assembly (10 candidates verbatim + F_4-invariance re-check + Schwarz guard), the candidate-product dimension d_candidate(a,b) via exact_qq_rank at 44 saturated generic pairs, the plethystic log plog H(s,t), the d_true-vs-d_candidate match at every a+b<=6, the in-span-of-lower-products minimality test per generator, the (2,2) generator-vs-product decision, and the honest CERTIFIED-COMPLETE verdict. Consumes the Plan-01 d_true by IMPORTING molien_bigraded (regenerated, NOT hand-typed). Exact over Q; module-local exact-only guard PASS (0 float-rank, 0 octonion_algebra). CLEAN PASS (exit 0)."
      linked_ids: [claim-candidate-set, claim-minimality, claim-22-decision, claim-completeness]
    deliv-candidate-table:
      status: passed
      path: code/generating_set_certificate.py
      summary: "The 10 candidates with bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2),(2,2) and builder expressions (printed), plus d_candidate(a,b) as exact integers for all a+b<=6 (== d_true everywhere)."
      linked_ids: [claim-candidate-set]
    deliv-minimality-table:
      status: passed
      path: code/generating_set_certificate.py
      summary: "Per-generator minimality results: all 10 candidates are GENUINE generators (in-span-of-lower-products exact_qq_rank increases by 1 for each), with the (2,2) Tr(X^2 o Y^2) result called out explicitly (lower-product rank 8 -> 9 = GENERATOR)."
      linked_ids: [claim-minimality, claim-22-decision]
    deliv-verdict:
      status: passed
      path: code/generating_set_certificate.py
      summary: "The honest verdict: CERTIFIED COMPLETE to total degree <=6, with the explicit polarization-NOT-assumed note (Hilbert match is the certificate; Schwarz). Minimal generating set listed (10 generators with bidegrees). Relations: NO syzygies through degree 6 (plog all {0,+1}; FREE through deg 6; first relation at total degree >= 7 if the ring is non-free). Cross-consistent with trdeg 10 / Krull 10 / (1,1)=2."
      linked_ids: [claim-completeness]
    deliv-summary-handoff:
      status: passed
      path: .gpd/phases/68-a-generating-set-completeness-certificate/68-02-SUMMARY.md
      summary: "This SUMMARY: the phase-closing sub-claim (a) result -- the minimal F_4 two-copy generating set (10 generators) + the degree-<=6 completeness certificate (CERTIFIED COMPLETE, no missing generator), cross-consistent with Phases 65 (Krull 10), 65.1 (trdeg-10 set), 66 (rank 7), 67 ((1,1)=2)."
      linked_ids: [claim-completeness]
  acceptance_tests:
    test-candidate-bidegrees:
      status: passed
      summary: "All 10 candidates loaded with correct bidegrees (asserted == the tabulated list) and confirmed F_4-invariant (D_M f=0 for 52/52 generators at a diagonal octonionic point + an independent pair). The mixed cubics are equivalently produced via polarize_d as candidates."
      linked_ids: [claim-candidate-set, deliv-cert-code, deliv-candidate-table, ref-ring-gen-set]
    test-no-polarization-assumption:
      status: passed
      summary: "Code + verdict audited: polarization is used ONLY to construct candidate expressions (the (2,1)/(1,2) mixed cubics), NOWHERE as evidence of completeness. The verdict explicitly states 'polarization was NOT assumed to generate; the bigraded Hilbert match IS the certificate.' (Schwarz guard, fp-polarization-generates.)"
      linked_ids: [claim-candidate-set, deliv-cert-code, deliv-verdict, ref-schwarz]
    test-minimality:
      status: passed
      summary: "For each of the 10 generators, exact_qq_rank of {lower products at its bidegree} + its value-vector increased by exactly 1 over {lower products} alone (proven, not asserted): all 10 are genuine generators; none reducible. Evaluated at 44 generic rational octonionic pairs (saturated)."
      linked_ids: [claim-minimality, deliv-cert-code, deliv-minimality-table]
    test-spanning-vs-minimal:
      status: passed
      summary: "Minimality rests on the in-span-of-lower-products exact test (Pitfall 8), not on membership in a Reynolds spanning set. H_free was never substituted for H_true (d_true computed independently in Plan 01). No candidate counted as a generator merely for appearing in a spanning set."
      linked_ids: [claim-minimality, deliv-cert-code, deliv-minimality-table]
    test-22-decision:
      status: passed
      summary: "At (2,2): the 8 strictly-lower candidate products have exact_qq_rank 8; +Tr(X^2 o Y^2) -> 9 = d_true(2,2) from Plan 01. The in-span test shows Tr(X^2 o Y^2) is NOT in the lower-product span AND d_true(2,2) > rank-without (9 > 8) => GENERATOR. Reported honestly; re-confirmed point-independent at a second seed."
      linked_ids: [claim-22-decision, deliv-cert-code, deliv-minimality-table, ref-plan01-table]
    test-hilbert-match:
      status: passed
      summary: "At every bidegree a+b<=6, d_true(a,b) (Plan 01 Molien) <= d_candidate(a,b) (exact_qq_rank reachable by candidate products); in fact EQUAL at all 28 bidegrees. Candidate products reach the true dimension everywhere => CERTIFIED COMPLETE to degree 6. No bidegree with d_true > d_candidate (no missing generator)."
      linked_ids: [claim-completeness, deliv-cert-code, deliv-verdict, ref-plan01-table]
    test-plog:
      status: passed
      summary: "plog H(s,t) = sum_k (mu(k)/k) log H(s^k,t^k) computed exactly (SymPy mobius, exact rational bivariate series) to total degree <=6. Positive coefficients (all +1) at exactly the 10 candidate bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2),(2,2); NO positive coefficient at a non-candidate bidegree (no missing generator); NO negative coefficient (no syzygy through deg 6). Independent monomial-count cross-check confirms #candidate-monomials == d_true at every bidegree."
      linked_ids: [claim-completeness, deliv-cert-code, deliv-verdict]
    test-verdict-honest:
      status: passed
      summary: "Verdict stated per NEGATIVE-RESULT-IS-SUCCESS: CERTIFIED COMPLETE to total degree <=6 with the explicit polarization-NOT-assumed note (the Hilbert match is the certificate). Cross-consistent with trdeg 10 (65/65.1) >= rank 7 (66) >= quotient 1 (67), Krull 10, (1,1)=2. The non-free EXPECTATION (Blind) was disconfirmed within scope (free through deg 6) and reported honestly. No hand-wave; the positive (complete) outcome is the honest computed result."
      linked_ids: [claim-completeness, deliv-verdict, deliv-summary-handoff, ref-schwarz]
  references:
    ref-plan01-table:
      status: completed
      completed_actions: [read, use, compare]
      missing_actions: []
      summary: "The Plan-01 certified d_true {d_(a,b): a+b<=6} is the decisive INPUT, consumed by IMPORTING molien_bigraded.molien_H (regenerated, NOT hand-typed); the handoff sanity gates (CT=1152, single-copy [1,1,2,3,4,5,7], (1,1)=2, (2,2)=9, symmetry) re-fired and PASSED. The completeness certificate IS the comparison of this table against d_candidate."
    ref-ring-gen-set:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "The 10-candidate set (CANDIDATES/NAMES/BIDEGREES/BUILDERS/CANDIDATE_GRADS) and the PAIR_POINTS + value-matrix exact_qq_rank machinery are imported verbatim from Phase 65.1; this plan upgrades from FIELD-level (trdeg) to RING generation via the Hilbert match."
    ref-frozen-degree2:
      status: completed
      completed_actions: [read, use, compare]
      missing_actions: []
      summary: "Phase 67 (1,1)=2 = span{Tr(X)Tr(Y), c} anchored the (1,1) cell of the analysis (d_true(1,1)=2 re-checked at the handoff); the genuine-coupling quotient 1 mod the reducible product Tr(X)Tr(Y) is the prototype of the generator-vs-product minimality reasoning applied here at every bidegree (c at (1,1): lower-product rank 1 -> 2 = GENERATOR, matching the quotient-1 structure)."
    ref-schwarz:
      status: completed
      completed_actions: [cite, avoid]
      missing_actions: []
      summary: "Schwarz (2-polarization fails generically in char 0) cited as THE reason the bigraded Hilbert match -- not polarization -- is the completeness certificate. Polarization (polarize_d) PRODUCED the mixed-cubic candidates only; it is NOWHERE used as evidence of completeness. Cited in the completeness verdict."
    ref-blind:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "Blind 2011 (C[27+27]^{E_6} FREE on 4 dets) cited as the CONTRAST: the F_4 pair ring is strictly LARGER (contains c) and EXPECTED non-free, so H_free was NOT assumed to equal H_true. FINDING reported honestly: through total degree 6 the F_4 ring is in fact FREE on the 10 candidates (no syzygy); the first relation, if non-free, is at total degree >= 7. The E_6 free answer was NOT imported as the F_4 ring (fp-e6-free-form rejected)."
    ref-iltyakov:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Iltyakov 1998 (F_4 several-copy invariants = trace polynomials + Laplace invariants) cited as the authority that the candidate generators ARE trace polynomials (c, Tr(X^2oY), Tr(XoY^2), Tr(X^2oY^2)) -- the candidate set is the right FORM; a missing generator (had any been found) would be the lowest-degree trace monomial at that bidegree (backtracking guidance; not needed -- the set is complete)."
    ref-derksen-kemper:
      status: completed
      completed_actions: [use, cite]
      missing_actions: []
      summary: "Derksen-Kemper plethystic-log generator/relation extraction and minimal-vs-spanning-via-Hilbert-series used as the method for plog H(s,t) and the in-span minimality test; cited in the module docstring."
    ref-hanany:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "Hanany et al. plethystic-exponential / plethystic-log (PE/plog) formulas followed in practice for reading generators (positive plog) and relations (negative plog) off the Hilbert series."
    ref-polarize:
      status: completed
      completed_actions: [use]
      missing_actions: []
      summary: "polarize_d (frozen engine; d(X,X,X)=6 det_3) PRODUCED the equivalent (2,1) and (1,2) mixed-cubic CANDIDATES f(X,X,Y), f(X,Y,Y). Used ONLY as a candidate-producer (Schwarz guard) -- NEVER assumed to generate; the 10 candidates carried into the Hilbert match are the trace monomials from ring_generating_set.py, and polarize_d's role is the equivalence note in the assembly (fp-polarization-generates rejected)."
  forbidden_proxies:
    fp-polarization-generates:
      status: rejected
      notes: "The completeness claim rests SOLELY on the bigraded Hilbert match (d_true vs d_candidate, both computed exactly and independently). Polarization (polarize_d) PRODUCED the mixed-cubic candidates only; the verdict EXPLICITLY states 'polarization was NOT assumed to generate.' No code path or verdict sentence treats 'we polarized' as proof (Schwarz guard, stated in-code and at runtime)."
    fp-spanning-as-minimal:
      status: rejected
      notes: "Minimality is the in-span-of-lower-products exact_qq_rank test (rank +1 when the generator's value-vector is appended), NOT membership in a Reynolds spanning set. Each candidate proven a genuine generator (none reducible); spanning explicitly distinguished from minimal generating (Pitfall 8). H_free never substituted for H_true."
    fp-float-rank:
      status: rejected
      notes: "ALL value-matrix ranks via exact_qq_rank = DomainMatrix-over-QQ (exact rational); 0 numpy.linalg.matrix_rank / SVD tolerance; 0 octonion_algebra (float64) import. Module-local exact-only guard scans __file__ and asserts both (PASS: 0 float-rank calls, 0 octonion_algebra imports)."
    fp-e6-free-form:
      status: rejected
      notes: "H_true was NOT assumed to have the free-algebra product form. d_true was computed INDEPENDENTLY in Plan 01 (Molien-Weyl iterated residue); the candidate-product dimension d_candidate was computed INDEPENDENTLY here (exact_qq_rank). They HAPPEN to match the free product through total degree 6 -- a COMPUTED finding (the ring is free through deg 6), not an imported E_6 assumption. The plog is reported as it is (all {0,+1}); the honest statement is that the first relation, if non-free, is at degree >= 7."
    fp-suppress-missing:
      status: rejected
      notes: "No bidegree had d_true > d_candidate (no missing generator to suppress). The harness is wired to REPORT any such bidegree (NEGATIVE-RESULT-IS-SUCCESS) and to name the lowest-degree trace monomial there (Iltyakov), never to paper over a gap by appealing to polarization or an assumed syzygy. The CERTIFIED-COMPLETE verdict is the honest computed outcome, not a suppression."
  uncertainty_markers:
    weakest_anchors:
      - "d_candidate(a,b) depends on a COMPLETE enumeration of candidate-monomial products at each bidegree; an incomplete enumeration would falsely UNDER-count d_candidate and could falsely flag a missing generator. Mitigation (executed): the monomial enumeration is by exhaustive bounded recursion over candidate exponents (verified: #monomials == d_true at every bidegree by an independent count); the (1,1) and (2,0) cells match the known Phase-67/65.1 structure (c at (1,1): 1->2; etc.); the decisive ranks re-confirmed point-independent at a second random seed."
      - "Completeness is certified ONLY to total degree <=6 (the contract scope). The genuinely-new generators live at degree <=4 (single-copy <=3, mixed <=4); degrees 5,6 probe for surprise generators and found none (plog 0 there). A generator or relation at total degree >= 7 is OUTSIDE this certificate -- the FREE-through-deg-6 finding does NOT prove the ring is globally free (the Blind E_6 contrast suggests the larger F_4 ring is ultimately non-free; the first relation, if any, is at degree >= 7)."
    unvalidated_assumptions: []
    competing_explanations:
      - "The absence of relations (negative plog) through degree 6 admits two readings, both reported: (i) the F_4 pair ring is genuinely free on these 10 generators through degree 6 (the computed fact); (ii) the ring is ultimately non-free (Blind contrast) with its first syzygy at total degree >= 7, beyond scope. The certificate establishes (i) within scope and is explicit that (ii) is not excluded above degree 6."
    disconfirming_observations:
      - "DISCONFIRMED EXPECTATION (reported honestly): the plan/Blind contrast EXPECTED negative plethystic-log coefficients (relations) because the F_4 pair ring is larger than the free E_6 ring. NO negative coefficient appears through total degree 6 -- the ring is FREE through degree 6. This is a clean honest finding (NOT the fp-e6-free-form proxy): d_true was computed independently and matches the free product through deg 6. A negative plog or a d_true>d_candidate bidegree WITHIN deg 6 would have been a missing-generator/relation report; neither occurred."
      - "No two-method disagreement: Molien d_true == independent monomial count == exact_qq_rank d_candidate at all 28 bidegrees. The (2,2) generator verdict (rank 8->9) and the (3,3) rank (24) are seed-independent. All reward-hacking tripwires clear."

comparison_verdicts:
  - subject_id: claim-completeness
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan01-table
    comparison_kind: benchmark
    metric: exact_integer_equality
    threshold: "d_candidate(a,b) == d_true(a,b) for ALL 28 bidegrees a+b<=6"
    verdict: pass
    recommended_action: "Close sub-claim (a) of the (RING) Lemma: the 10-candidate set is a CERTIFIED COMPLETE minimal generating set to total degree <=6. Proceed to Phase 69 (REDUCIBILITY statement) / v16.0 closeout."
    notes: "d_candidate (exact_qq_rank, 44 saturated generic pairs) == d_true (Plan 01 Molien) as identical exact integers at every bidegree (28/28). Candidate products reach the true dimension everywhere -> COMPLETE."
  - subject_id: claim-22-decision
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-plan01-table
    comparison_kind: cross_method
    metric: exact_integer_equality
    threshold: "lower-product rank (8) + 1 == d_true(2,2) (9) AND in-span test increments"
    verdict: pass
    recommended_action: "Record Tr(X^2 o Y^2) as a GENUINE (2,2) generator in the minimal generating set."
    notes: "The 8 strictly-lower candidate products span exactly 8-dim (exact_qq_rank); +Tr(X^2 o Y^2) -> 9 = d_true(2,2). Its value-vector is NOT in the lower-product span. Seed-independent."
  - subject_id: claim-minimality
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-frozen-degree2
    comparison_kind: cross_method
    metric: rank_increment
    threshold: "each generator's in-span test increments exact_qq_rank by exactly 1"
    verdict: pass
    recommended_action: "Record all 10 candidates as genuine (minimal) generators; none reducible."
    notes: "Increments all +1 (0->1, 1->2, 2->3, 0->1, 1->2, 2->3, 1->2, 3->4, 3->4, 8->9). c at (1,1) reproduces the Phase-67 quotient-1 structure (1->2)."
  - subject_id: claim-completeness
    subject_kind: claim
    subject_role: supporting
    reference_id: ref-blind
    comparison_kind: prior_work
    metric: plethystic_log_relations
    threshold: "negative plog coefficients EXPECTED (non-free); reported as found"
    verdict: tension
    recommended_action: "Report the FREE-through-deg-6 finding honestly; note the first relation (if non-free) is at total degree >= 7, beyond the contract scope. Do NOT over-claim global freeness."
    notes: "The Blind E_6 contrast EXPECTED the larger F_4 ring to be non-free (negative plog). Within total degree <=6 NO relation appears (plog all {0,+1}; free through deg 6). Honest tension: the certificate establishes freeness ONLY through degree 6; global non-freeness is not excluded above degree 6. This is NOT fp-e6-free-form (d_true computed independently)."

duration: 14min
completed: 2026-05-27
---

# Phase 68 Plan 02: (a) Generating-Set Completeness Certificate (CERTIFICATE half) Summary

**CERTIFIED the 10-candidate F_4 two-copy set {6 pointwise, c, Tr(X^2oY), Tr(XoY^2), Tr(X^2oY^2)} as a COMPLETE and MINIMAL generating set of R[27+27]^{F_4} to total degree <=6 by exact-over-Q Hilbert match (d_candidate == d_true at all 28 bidegrees, exact_qq_rank, 44 saturated generic pairs) — NOT by assuming polarization generates (Schwarz). The (2,2) Tr(X^2oY^2) question is DECIDED a GENERATOR (lower-product rank 8 -> 9); the ring is FREE through total degree 6 (no syzygies; plog all {0,+1}), reported honestly against the Blind non-free expectation. This CLOSES sub-claim (a) of the (RING) Lemma.**

## Status: COMPLETE — CLEAN PASS (exit 0)

Both tasks complete, verified, and committed (`39c40ee7`). The harness `code/generating_set_certificate.py` runs CLEAN PASS (exit 0) end-to-end: exact-only guard green, all 10 candidates assembled + F_4-invariance re-confirmed (52/52), d_true regenerated from Plan 01 (handoff gates re-fired and PASSED), d_candidate saturated at 44 generic pairs, plog computed, all 10 minimality tests PASS (genuine generators), (2,2) decided GENERATOR, completeness match d_true==d_candidate at all 28 bidegrees, honest CERTIFIED-COMPLETE verdict cross-consistent with Phases 65/65.1/66/67.

## Performance

- **Duration:** ~14 min (harness ~3 min/run; two full runs + an independent-seed robustness re-check + an independent monomial-count cross-check)
- **Started:** 2026-05-27T18:43:47Z
- **Completed:** 2026-05-27T18:57:53Z
- **Tasks:** 2 of 2 (both `type=auto`)
- **Files modified:** 1 (`code/generating_set_certificate.py`)

## Key Results

- **CERTIFIED COMPLETE to total degree <=6.** The candidate-product dimension `d_candidate(a,b)` (exact_qq_rank of the candidate-monomial value-matrix at 44 saturated generic rational octonionic pairs) **equals `d_true(a,b)` (Plan 01 Molien) at EVERY one of the 28 bidegrees `a+b<=6`** — candidate products reach the true dimension everywhere. The full match grid (T = d_true, C = d_candidate):

  ```
    a\b |    0      1      2      3      4      5      6
    -------------------------------------------------------
      0 |  1/1    1/1    2/2    3/3    4/4    5/5    7/7
      1 |  1/1    2/2    4/4    6/6    9/9  12/12      .
      2 |  2/2    4/4    9/9  14/14  22/22      .      .
      3 |  3/3    6/6  14/14  24/24      .      .      .
      4 |  4/4    9/9  22/22      .      .      .      .
      5 |  5/5  12/12      .      .      .      .      .
      6 |  7/7      .      .      .      .      .      .
  ```

- **The MINIMAL generating set = all 10 candidates** (each a genuine generator by the in-span-of-lower-products exact test; no candidate reducible):

  | # | name | bidegree | in-span test (lower-product rank -> +G) |
  |---|------|----------|------------------------------------------|
  | 1 | Tr X | (1,0) | 0 -> 1 GENERATOR |
  | 2 | Tr X^2 | (2,0) | 1 -> 2 GENERATOR |
  | 3 | det X | (3,0) | 2 -> 3 GENERATOR |
  | 4 | Tr Y | (0,1) | 0 -> 1 GENERATOR |
  | 5 | Tr Y^2 | (0,2) | 1 -> 2 GENERATOR |
  | 6 | det Y | (0,3) | 2 -> 3 GENERATOR |
  | 7 | c = Tr(X o Y) | (1,1) | 1 -> 2 GENERATOR |
  | 8 | Tr(X^2 o Y) | (2,1) | 3 -> 4 GENERATOR |
  | 9 | Tr(X o Y^2) | (1,2) | 3 -> 4 GENERATOR |
  | 10 | Tr(X^2 o Y^2) | (2,2) | **8 -> 9 GENERATOR** |

- **The (2,2) diagnostic DECIDED: `Tr(X^2 o Y^2)` is a GENUINE GENERATOR, not a product.** The 8 strictly-lower candidate products at (2,2) {`c^2`, `Tr(X^2)Tr(Y^2)`, `c*Tr(X)Tr(Y)`, `Tr(X^2oY)*Tr(Y)`, `Tr(XoY^2)*Tr(X)`, `(TrX)^2(TrY)^2`, `Tr(X^2)(TrY)^2`, `(TrX)^2 Tr(Y^2)`} span exactly 8-dim over Q (exact_qq_rank = 8); appending `Tr(X^2 o Y^2)` raises the rank to 9 = `d_true(2,2)`. Its value-vector is provably **not** in the lower-product span. Re-confirmed point-independent at a second random seed.

- **Relations catalogue — HONEST NON-FREE FINDING.** The plethystic log `plog H(s,t)` has coefficient **+1 at exactly the 10 candidate bidegrees** and **0 everywhere else through total degree 6, with NO NEGATIVE coefficient.** The candidate set is therefore **FREE through total degree 6**. The plan/Blind contrast *expected* relations (negative plog) because the F_4 pair ring is larger than the free E_6 ring; they do **not** appear within the contract scope. The first relation, if the ring is genuinely non-free, must occur at **total degree >= 7** (beyond scope). This is **not** the `fp-e6-free-form` proxy: `d_true` was computed *independently* in Plan 01 (Molien-Weyl) and *happens* to match the free product through degree 6; `H_free` was never substituted for `H_true`.

- **Cross-phase consistency confirmed:** trdeg 10 (65/65.1) >= SPINE rank 7 (66) >= quotient 1 (67); Krull 10; (1,1)=2 (67). The minimal generating set (10) equals the Phase-65.1 trdeg-10 field-generating candidate count — every field generator is also a ring generator here.

## Task Commits

The two tasks form one cohesive harness (`code/generating_set_certificate.py`) that does not function in pieces (Task 2's minimality/match reuses Task 1's saturated candidate-value table and the loaded d_true), so they are committed as one working-state atomic unit per the checkpoint discipline (a non-functional partial commit would violate "each checkpoint = working state") — mirroring the Plan-01 precedent.

1. **Tasks 1 + 2 (assembly + d_true + d_candidate + plog + minimality + (2,2) + match + verdict)** — `39c40ee7` (compute)
   - Task 1: candidate assembly (verbatim, F_4-invariance 52/52, Schwarz guard); d_true regenerated from Plan 01 (handoff gates re-fired); d_candidate(a,b) via exact_qq_rank at 44 saturated generic pairs; plethystic log.
   - Task 2: per-generator in-span-of-lower-products minimality (all 10 genuine generators); the (2,2) Tr(X^2 o Y^2) generator-vs-product decision (GENERATOR); d_true-vs-d_candidate completeness match (CERTIFIED COMPLETE); honest verdict + cross-phase consistency.

## Files Created/Modified

- `code/generating_set_certificate.py` — the candidate assembly + F_4-invariance re-check + Schwarz guard, the candidate-product dimension `d_candidate(a,b)` via exact_qq_rank at saturated generic pairs, the plethystic log, the d_true-vs-d_candidate match, the in-span minimality test per generator, the (2,2) decision, and the honest CERTIFIED-COMPLETE verdict. Exact over Q; module-local exact-only guard PASS (0 float-rank, 0 octonion_algebra). CLEAN PASS (exit 0), ~3 min runtime.

## Equations Used

**Eq. (68.4)** — candidate-product dimension (the completeness measure):
$$
d_{\text{candidate}}(a,b) = \operatorname{rank}_{\mathbb{Q}}\Big[\,\big(\textstyle\prod_i g_i(P_p)^{e_i}\big)_{\,\mathbf{e}\in M(a,b),\ p}\,\Big],\quad M(a,b)=\{\mathbf e: \textstyle\sum_i e_i\,\mathrm{bideg}(g_i)=(a,b)\}
$$
where $g_i$ are the 10 candidate invariants, $P_p$ the generic rational octonionic pairs (the value of a product invariant at a point is the product of the candidate scalar values), and the rank is exact over $\mathbb{Q}$.

**Eq. (68.5)** — completeness certificate (Hilbert match):
$$
d_{\text{true}}(a,b) = d_{\text{candidate}}(a,b)\quad\text{for all } a+b\le 6 \;\;\Longrightarrow\;\; \text{the 10 candidates generate } R[27\oplus27]^{F_4} \text{ to total degree } 6.
$$

**Eq. (68.6)** — in-span-of-lower-products minimality (generator vs product):
$$
g\ \text{at}\ (a,b)\ \text{is a GENUINE generator} \iff \operatorname{rank}_{\mathbb{Q}}\big(L_{(a,b)}\cup\{g\}\big) = \operatorname{rank}_{\mathbb{Q}}\big(L_{(a,b)}\big) + 1,
$$
where $L_{(a,b)}$ = value-vectors of all products of strictly-lower-degree candidates landing at $(a,b)$. For $(2,2)$: $8 \to 9 = d_{\text{true}}(2,2)$.

**Eq. (68.7)** — plethystic log (generator/relation separation):
$$
\operatorname{plog} H(s,t) = \sum_{k\ge1}\frac{\mu(k)}{k}\,\log H(s^k,t^k);\quad [\,s^a t^b\,]\operatorname{plog}H = +(\text{generators}) - (\text{relations}).
$$
Found: $+1$ at the 10 candidate bidegrees, $0$ elsewhere, **no negatives** through degree 6.

## Validations Completed

- **Three-method agreement on the dimension (reward-hacking tripwire):** Molien `d_true` == independent monomial count == exact_qq_rank `d_candidate` at ALL 28 bidegrees `a+b<=6`.
- **Plan-01 handoff re-verified:** regenerated d_true by importing `molien_bigraded.molien_H` (NOT hand-typed); CT=1152, single-copy row/col = [1,1,2,3,4,5,7], (1,1)=2, (2,2)=9, symmetry — all re-fired and PASSED.
- **F_4-invariance re-confirmed:** D_M f = 0 for 52/52 generators for all 10 candidates (diagonal octonionic point + independent pair).
- **(2,2) GENERATOR verdict point-independent:** re-ran the decisive ranks at a second random seed (999331): (2,2) 8->9, (3,3)=24, (2,1)=(1,2)=4 reproduced exactly (rejects fp-nongeneric-point).
- **Saturation:** d_candidate stable across two successive point counts (36 -> 44 pairs identical) and `d_candidate <= d_true` everywhere (sane).
- **Exact-only guard:** 0 numpy float-rank calls, 0 octonion_algebra imports on the decisive path (module scans __file__).
- **Cross-phase consistency:** trdeg 10 >= rank 7 >= quotient 1; Krull 10; (1,1)=2.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| (2,2) lower-product dim | — | 8 | exact (0) | exact_qq_rank, 44 pairs | exact over Q |
| (2,2) with Tr(X^2oY^2) | — | 9 (= d_true) | exact (0) | exact_qq_rank | exact over Q |
| # genuine generators | — | 10 | exact (0) | in-span test (all +1) | total degree <= 6 |
| # relations (syzygies) | — | 0 | exact (0) | plog (all {0,+1}) | total degree <= 6 |
| completeness match bidegrees | — | 28/28 | exact (0) | d_true == d_candidate | a+b <= 6 |

All quantities are exact integers over Q (no tolerance; the error budget is exact).

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---|---|---|---|
| total-degree truncation a+b<=6 | the contract scope; genuinely-new generators live at degree <=4 | exact within the truncation | a generator/relation at total degree >= 7 (the FREE-through-deg-6 finding does not certify global freeness) |
| NONE on the decisive path | exact-integer arithmetic over Q | exact (no tolerance) | n/a |

## Decisions Made

- **Verdict = CERTIFIED COMPLETE** (d_candidate == d_true at all 28 bidegrees).
- **(2,2) = GENERATOR** (Tr(X^2 o Y^2) not in the 8-dim lower-product span; rank 8 -> 9).
- **Relations = NONE through degree 6** (free through deg 6; reported honestly against the Blind non-free expectation; first relation at degree >= 7 if non-free).
- **Polarization NOT assumed to generate** (Schwarz; the Hilbert match is the certificate).
- d_true consumed by IMPORTING the Plan-01 engine (regenerated, not hand-typed) so the handoff is re-verified, not trusted blindly.
- Generic pairs drawn from a FIXED seed (68022) and validated genuinely octonionic; decisive ranks re-confirmed at a second seed.

## Deviations from Plan

**None — plan executed exactly as written.** Both tasks ran as specified with exact-over-Q rigor; no deviation rules were triggered. The one notable scientific outcome (the ring being FREE through degree 6, contrary to the Blind non-free *expectation*) is a HONEST FINDING within the contract's NEGATIVE-RESULT-IS-SUCCESS framing, not a deviation — both completeness outcomes (certified-complete OR missing-generator) were full passes, and the relations question was reported as computed (no negatives) rather than forced to match the non-free expectation.

## Issues Encountered

- The executor stream-watchdog backgrounded the first long symbolic run (no token stream during the ~40s candidate-evaluation loops and the Weyl-CT product), as anticipated by the watchdog guidance. All heavy runs were executed with `python -u` and chunked progress prints (one line per saturation round / convolution batch) and monitored to completion via output-file polling. No data loss.

## Open Questions (beyond this certificate's scope)

- **Is R[27+27]^{F_4} globally free, or non-free with its first relation at total degree >= 7?** The certificate establishes freeness through total degree 6; the Blind E_6 contrast suggests the larger F_4 ring is ultimately non-free. Resolving this needs the Hilbert series to higher degree (Plan 01's Molien-Weyl engine extends, but the f_4-kernel cross-check is infeasible past a+b<=4) — outside the v16.0 (RING) sub-claim (a) scope.
- The genuinely-new generators live at degree <=4 (single-copy <=3, mixed <=4); degrees 5,6 found no surprise generators (plog 0 there), as expected.

## Next Phase Readiness

Sub-claim (a) of the (RING) Lemma is **CLOSED**: the minimal F_4 two-copy generating set is the 10 candidates with bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2),(2,2), CERTIFIED COMPLETE to total degree <=6 by the exact bigraded Hilbert match (polarization NOT assumed; Schwarz). Combined with Phase 66 ((b) c FUNCTIONALLY INDEPENDENT, rank 7) and Phase 67 ((c) c the UNIQUE degree-2 coupling generator), the (RING) characterization is complete: **c = Tr(X o Y) is a genuine, minimal, functionally-independent, unique-degree-2 generator of the F_4 two-copy invariant ring.** Phase 69 ((REDUCIBILITY) statement) is unblocked.

## Cross-Phase Dependencies

### Results This Phase Provides To Later Phases

| Result | Used By Phase | How |
|---|---|---|
| CERTIFIED-COMPLETE minimal generating set (10 generators, bidegrees) | v16.0 (RING) closeout | the (a) deliverable; combines with (b)/(c) for the full (RING) characterization |
| (2,2) Tr(X^2 o Y^2) = GENERATOR | (RING) characterization | confirms the mixed-square is a genuine generator, not a product |
| FREE-through-deg-6 (no syzygies) finding | Phase 69 / future | the ring structure to degree 6; the first relation (if any) is at degree >= 7 |

### Results This Phase Consumed From Earlier Phases

| Result | From Phase | Verified Consistent |
|---|---|---|
| Certified d_true table {d_(a,b): a+b<=6} | Phase 68 Plan 01 | Yes — regenerated by import; CT=1152, single-copy [1,1,2,3,4,5,7], (1,1)=2, (2,2)=9, symmetry all re-fired |
| 10-candidate set + bidegrees + PAIR_POINTS | Phase 65.1 | Yes — loaded verbatim; F_4-invariance re-confirmed 52/52 |
| exact_qq_rank (DomainMatrix-over-QQ) | Phase 65 | Yes — used for all decisive ranks; exact-only guard PASS |
| (1,1)=2 = span{Tr(X)Tr(Y), c} | Phase 67 | Yes — c at (1,1) minimality 1->2 reproduces the quotient-1 structure |
| SPINE rank 7 (c independent) | Phase 66 | Yes — trdeg 10 >= rank 7 >= quotient 1 consistent |

### Convention Changes

| Convention | Previous | This Phase | Reason |
|---|---|---|---|
| F_4 pair ring freeness | EXPECTED non-free (Blind E_6 contrast; H_free != H_true a priori) | FOUND FREE through total degree 6 (computed, not assumed) | the independently-computed d_true matches the free product through deg 6; reported honestly with the explicit note that global non-freeness (first relation at deg >= 7) is not excluded |

## Self-Check: PASSED

- Files exist: `code/generating_set_certificate.py`, `68-02-SUMMARY.md` — FOUND.
- Commit exists: `39c40ee7` — FOUND.
- Reproducibility: fresh clean invocation of `generating_set_certificate.py` reproduced OVERALL CLEAN PASS / CERTIFIED COMPLETE (d_candidate == d_true at all 28 bidegrees; (2,2) GENERATOR; 10 minimal generators; no relations through deg 6).
- Exact-only audit: 0 `numpy.linalg.matrix_rank` calls, 0 `octonion_algebra` imports on the decisive path (all such tokens are in comments/strings only).
- Contract coverage: all 4 claims, 5 deliverables, 8 acceptance tests, 9 references, 5 forbidden proxies present and resolved (claims/deliverables/tests all `passed`; proxies all `rejected`); 4 comparison verdicts (3 pass + 1 honest tension for the Blind non-free expectation).
- Convention consistency: exact over Q throughout; c=Tr(X∘Y); 10 verbatim candidates; jordan=(1/2)(AB+BA) — consistent with the convention lock and Phases 64.1/65/65.1/66/67.
- Domain guard (mathematical physics / invariant theory): all dimensions, ranks, plog coefficients are exact integers; three-method agreement (Molien d_true == monomial count == exact_qq_rank d_candidate); decisive ranks point-independent (second seed).

---

_Phase: 68-a-generating-set-completeness-certificate_
_Completed: 2026-05-27_
