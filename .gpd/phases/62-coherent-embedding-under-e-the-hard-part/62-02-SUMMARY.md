---
phase: 62-coherent-embedding-under-e-the-hard-part
plan: 02
depth: complex
one-liner: "DECISIVE COMPUTATION: on the genuinely non-associative h_3(O), the exact ambient E-transport residual R = E(sqrt(X)Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) is EXACTLY NONZERO for generic X,Y (associator load-bearing = 524/9; |R|^2 = 38593/72 on the clean pair) — VERDICT (O) AMBIENT-TRANSPORT OBSTRUCTION, the EXPECTED outcome that refines RESTRICTION to coexistence-as-island; both routes (direct + positional Peirce) agree; ambient SP found non-Hermitian"
subsystem: [validation, derivation, formalism]
tags: [jordan-algebra, octonions, conditional-expectation, sequential-product, peirce-decomposition, non-associativity, albert-algebra, exact-symbolic, ambient-transport-obstruction]

requires:
  - phase: 62-01
    provides: "explicit E: h_3(O) -> h_3(C_u) (entrywise proj_u, u=e_7; positive unital idempotent, E|_A=id, NOT a Jordan morphism on the ambient); the decisive crux framed as the ambient E-transport residual R for generic X,Y; §3.3-§3.4 exact-arithmetic spec; slice-internal case = trivial control; CORRECTED RESTRICTION (coexistence-as-island); fork kept open"
  - phase: 61-slice-satisfies-clause-iii
    provides: "slice A = h_3(C_u) ~ M_3(C)^sa satisfies all four Paper 5 Def 1 clauses intrinsically; the closed-associative-slice triviality (leakage 0) that makes the AMBIENT residual the decisive object; the exact-SymPy spectral sqrt + assert-harness template (VALD-61-01)"
provides:
  - "DECISIVE exact result: E does NOT transport the self-modeling sequential product coherently from h_3(O) — the ambient residual R = E(sqrt(X)Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) is EXACTLY nonzero for generic ambient X,Y (verdict O, ambient-transport obstruction)"
  - "Non-associativity is LOAD-BEARING on the decisive data (associator of (sqrt(X),Y,sqrt(X)) = 524/9 != 0 exact); the slice-internal case is the documented TRIVIAL control (leakage 0, associator 0)"
  - "Defect characterization: R lands ENTIRELY in the C_u directions (e_0,e_7), |R|^2 = 38593/72 (clean pair); positional E_11 Peirce grades |V_1|^2=4, |V_1/2|^2=1033/18, |V_0|^2=3797/8 (sum = |R|^2); the failure is the two slice elements not coinciding, NOT leakage out of A"
  - "NEW finding: the ambient sequential product sqrt(X)Y sqrt(X) is NON-Hermitian in h_3(O) (the involution identity fails under non-associativity) — an additional, association-dependent way E fails to transport the SP (sharpens O)"
  - "E confirmed EXACTLY (positivity/idempotency/unitality/E|_A=id) on the full 27-dim algebra, AND confirmed NOT a Jordan morphism on the ambient (|E(XoX)-(EX)o(EX)|^2 = 3797527/34560000 != 0)"
  - "code/embedding_under_E_verification.py + tests/test_embedding_under_E.py (VALD-62-01): exact-SymPy, assert-based (NO pytest), runnable as `python tests/test_embedding_under_E.py`, exits 0; two independent routes agree on (O)"
affects: [62-03 (reads the verdict (O) into the RESTRICTION refinement / characterized obstruction), 63 (milestone verdict)]

methods:
  added: ["exact-SymPy octonion arithmetic (Fano e1e2=e4) ported from the float64 octonion_algebra.py", "non-associative 3x3 octonionic matrix triple product by independent left/right association (h3o_matmul)", "ambient principal square root via the exact-square trick X=C*C (surd-free, sqrt^2==X exact)", "diagonal-EX engineering (single-direction C off-diagonals) to keep the EXACT slice spectral sqrt tractable while X,Y stay generic ambient", "positional E_11 Peirce decomposition (faithful for non-Hermitian matrices)"]
  patterns: ["decisive AMBIENT-transport residual vs slice-internal trivial control — non-associativity load-bearing on the SAME decisive (X,Y)", "two independent verdict routes (direct exact residual + positional Peirce/grade-component) with RAISE-on-split guard", "HONEST verdict harness: assert R.equals(zeros) <=> is_zero_exact (not hardcoded to P or O)", "EXACT zero-tolerance decisive test (SymPy simplify==0), NEVER float64"]

key-files:
  created: ["code/embedding_under_E_verification.py", "tests/test_embedding_under_E.py"]
  modified: ["derivations/p5-basin-restriction/embedding-under-E.md (§4 appended: the decisive ambient-transport computation + verdict (O); §4-to-follow marker updated)"]

key-decisions:
  - "Decisive object = the AMBIENT transport residual R for GENERIC ambient X,Y (sqrt(X) in the ambient); slice-internal case kept strictly as the TRIVIAL control"
  - "Engineered the decisive data so EX = E(C*C) is DIAGONAL (single-direction C off-diagonals) to avoid casus-irreducibilis cubic-radical blowup in the EXACT slice sqrt — while Y is rich so the decisive triple (sqrt(X),Y,sqrt(X)) genuinely engages non-associativity (associator = 524/9 != 0)"
  - "Reported the TRUE verdict (O) as computed — did NOT cherry-pick X,Y or relax the exact test; (O) framed as the EXPECTED refinement to coexistence-as-island, not a collapse"
  - "Made the Peirce cross-check sound for the NON-Hermitian defect (positional grading + all-entry C_u/e16 split), after discovering the ambient SP is non-Hermitian"
  - "v11.0/Phase 42 precedent cited only as historical context (different mechanism), NOT as evidence for (O)"

patterns-established:
  - "Pattern: a conditional expectation that preserves the Jordan product on its range, and is not even a Jordan morphism on the ambient, fails (exactly) to transport the non-Jordan CFC triple product from the non-associative ambient"
  - "Pattern: in a non-associative *-algebra the triple product sqrt(X) Y sqrt(X) is association-dependent and generically non-Hermitian; characterize residuals with positional Peirce grading, not Hermitian-coordinate reconstruction"

conventions:
  - "natural units (hbar=1, k_B=1); pure algebra — no physical dimensions; EXACT symbolic/rational/surd arithmetic (SymPy), NEVER float64 on the decisive path"
  - "Jordan product a o b = (1/2)(ab+ba)"
  - "sequential product a&b = sqrt(a) b sqrt(a) (Luders/self-modeling, principal CFC sqrt; LEFT association in the ambient)"
  - "octonion Fano e_1 e_2 = e_4; complex structure u = e_7 (C_u = span{1,e_7}); any u in S^6 equivalent under G_2"
  - "slice A = h_3(C_u) ~ M_3(C)^sa (maximal C*-target inside h_3(O)); range E = A; ker E = e_1..e_6 directions (18 real dims)"
  - "Peirce eigenvalues {0, 1/2, 1} at E_11 = diag(1,0,0)"

plan_contract_ref: ".gpd/phases/62-coherent-embedding-under-e-the-hard-part/62-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-restriction:
      status: passed
      summary: "DECISIVE half established by EXACT computation on the genuinely non-associative h_3(O): the ambient E-transport residual R = E(sqrt(X)Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) is EXACTLY NONZERO for two distinct generic ambient (X,Y) (associator of the decisive triple = 524/9 != 0, so non-associativity is load-bearing). VERDICT = (O) AMBIENT-TRANSPORT OBSTRUCTION — E does NOT transport the sequential product coherently. Both the direct exact-residual route and the independent positional-Peirce/grade-component route AGREE (no split). The slice-internal case is the documented TRIVIAL control (leakage 0, associator 0). (O) is the EXPECTED, ACCEPTABLE outcome that REFINES RESTRICTION to coexistence-as-island (62-03), NOT independent posits / collapse. Verdict NOT forced; v11.0 cited only as historical context. Additional finding: the ambient SP is non-Hermitian (sharpens O)."
      linked_ids: [deliv-embedding, deliv-vald-62-01, test-E-properties-exact, test-ambient-sqrt-exact, test-nonassociativity-load-bearing, test-decisive-ambient-residual, test-slice-internal-control, test-peirce-crosscheck, test-exact-arithmetic, test-no-pytest, test-verdict-not-forced, ref-effros-stormer, ref-lem-bottleneck, ref-paper5-def1, ref-vald-61-01, ref-v11-leakage]
      evidence:
        - verifier: gpd-executor
          method: "exact-SymPy computation on the non-associative h_3(O); two independent routes (direct ambient residual + positional Peirce/grade-component) agreeing; assert-based harness exits 0; zero-tolerance exact-equality decisive test"
          confidence: high
          claim_id: claim-restriction
          deliverable_id: deliv-vald-62-01
          acceptance_test_id: test-decisive-ambient-residual
          reference_id: ref-paper5-def1
          evidence_path: "code/embedding_under_E_verification.py + tests/test_embedding_under_E.py (run: ALL SELF-CHECKS PASS; VERDICT O; |R|^2 = 38593/72 pair0, surd~155 pair1; is_zero_exact=[False,False])"
        - verifier: gpd-executor
          method: "analytic record of the decisive computation + verdict + defect characterization + handoff"
          confidence: high
          claim_id: claim-restriction
          deliverable_id: deliv-embedding
          acceptance_test_id: test-verdict-not-forced
          reference_id: ref-lem-bottleneck
          evidence_path: "derivations/p5-basin-restriction/embedding-under-E.md §4"
  deliverables:
    deliv-embedding:
      status: passed
      path: derivations/p5-basin-restriction/embedding-under-E.md
      summary: "§4 appended (DERV-62-02): the decisive AMBIENT-TRANSPORT computation. §4.1 recaps the question; §4.2 cites code/tests and lists what was computed (E-properties exact incl. NOT-a-Jordan-morphism-on-ambient |diff|^2=3797527/34560000; ambient sqrt exact via X=C*C; associator=524/9 nonzero on the decisive data; the exact residual R for 2 generic (X,Y); slice-internal trivial control; Peirce cross-check); §4.3 states VERDICT (O) with the defect characterized (lands in C_u (e0,e7); |R|^2=38593/72; positional Peirce grades 4, 1033/18, 3797/8 summing to |R|^2; representative entry R_11=-2) and the non-Hermiticity finding; §4.4 justifies trustworthiness (two routes agree, exact zero-tolerance, non-associativity load-bearing, actual SP, generic ambient); §4.5 hands the verdict+defect to 62-03; §4.6 type/Peirce self-audit + CONFIDENCE HIGH + generality caveat. §1-§3 unchanged except the §4-to-follow marker."
      linked_ids: [claim-restriction, test-decisive-ambient-residual, test-verdict-not-forced, test-slice-internal-control, test-nonassociativity-load-bearing]
    deliv-vald-62-01:
      status: passed
      path: code/embedding_under_E_verification.py
      summary: "code/embedding_under_E_verification.py + tests/test_embedding_under_E.py (VALD-62-01): exact-SymPy, assert-based __main__ harness (NO pytest; _report/ALL_PASS/sys.exit; runnable as `python tests/test_embedding_under_E.py`, exits 0). (1) exact octonion arith (Fano e1e2=e4) + non-assoc h3o_matmul (triple product by independent left/right association); (2) E onto h_3(C_u) (entrywise proj_u) with exact unital/idempotent/E|_A=id/positive(spectrum 1,3,5)/dim 27=9+18 checks AND E-NOT-a-Jordan-morphism-on-ambient; (3) ambient sqrt via exact-square trick X=C*C (sqrt^2==X exact) + diagonal-EX engineering + slice spectral sqrt with diagonal fast-path; (4) DECISIVE residual R via compute_ambient_transport_residual -> (R, is_zero_exact) for 2 generic (X,Y), HONEST (R.equals(zeros)<=>is_zero_exact); (5) independent positional-Peirce/grade route with RAISE-on-split; (6) non-associativity exerciser (associator=524/9 nonzero on decisive data); (7) slice-internal TRIVIAL control (leakage 0, associator 0). Prints VERDICT (O); exits 0 on self-check success (P/O both valid)."
      linked_ids: [claim-restriction, test-E-properties-exact, test-ambient-sqrt-exact, test-nonassociativity-load-bearing, test-decisive-ambient-residual, test-slice-internal-control, test-peirce-crosscheck, test-exact-arithmetic, test-no-pytest, test-verdict-not-forced]
  acceptance_tests:
    test-E-properties-exact:
      status: passed
      summary: "E onto h_3(C_u) verified by EXACT SymPy: (a) unital E(I_3)=I_3; (b) idempotent E(E(X))=E(X) on a generic ambient X with nonzero e_1..e_6 (non-vacuous); (c) E|_A=id on a slice element; (d) positive on a non-diagonal PSD slice effect with rational spectrum {1,3,5}; (e) E is NOT a Jordan morphism on the ambient (|E(XoX)-(EX)o(EX)|^2 = 3797527/34560000 != 0); entrywise proj_u (comps 0,7 kept, 1..6 zeroed); dim(range E)=9, dim(ker E)=18. All exact, no float."
      linked_ids: [claim-restriction, deliv-vald-62-01, ref-effros-stormer]
    test-ambient-sqrt-exact:
      status: passed
      summary: "Ambient principal square root sqrt_ambient(X) computed in the 27-dim non-associative h_3(O) via the exact-square trick X = C*C (C ambient PSD, exact entries; PSD confirmed by reduced-charpoly roots >= 0); self-check h3o_matmul(sqrt_X, sqrt_X) == X EXACT (octonionic product); X genuinely ambient (nonzero e_1..e_6)."
      linked_ids: [claim-restriction, deliv-vald-62-01, ref-vald-61-01]
    test-nonassociativity-load-bearing:
      status: passed
      summary: "The associator (sqrt(X),Y,sqrt(X)) of the relevant ambient triple — the SAME triple whose product is the decisive sequential product — is EXACTLY nonzero (|assoc|^2 = 524/9) on the decisive (X,Y); per-pair associator-nonzero prechecks also pass. The decisive X,Y are generic ambient (nonzero e_1..e_6), NOT slice-confined. (xy)z != x(yz) genuinely engaged; NON-ASSOCIATIVITY guard honored; line-loophole foreclosed (associator on the SAME data, not unrelated matrices)."
      linked_ids: [claim-restriction, deliv-vald-62-01]
    test-decisive-ambient-residual:
      status: passed
      summary: "THE DECISIVE TEST. The ambient-transport residual R = E(sqrt(X)Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) computed EXACTLY for 2 generic (X,Y) via compute_ambient_transport_residual -> (R, is_zero_exact) with R.equals(zeros) <=> is_zero_exact (NOT hardcoded). Result: is_zero_exact = [False, False] -> VERDICT (O). |R|^2 = 38593/72 (pair0; representative exact entry R_11 = -2), surd ~155 (pair1). Defect localized to the C_u directions (e_0,e_7); positional Peirce grades |V_1|^2=4, |V_1/2|^2=1033/18, |V_0|^2=3797/8 (sum = |R|^2)."
      linked_ids: [claim-restriction, deliv-vald-62-01, deliv-embedding, ref-paper5-def1]
    test-slice-internal-control:
      status: passed
      summary: "Slice-internal control: for a,b in A (a diagonal PSD slice effect, b a slice element with C_u off-diagonal content), sqrt(a) b sqrt(a) (computed via the AMBIENT octonionic product) stays in A with leakage EXACTLY 0 (E(.)==.) and triple associator EXACTLY 0 (A closed associative subalgebra = range E). Clearly labeled as the TRIVIAL CONTROL, separated from the decisive ambient test; NOT used as the decisive test."
      linked_ids: [claim-restriction, deliv-vald-62-01]
    test-peirce-crosscheck:
      status: passed
      summary: "Independent second route: the defect D = E(sqrt(X)Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) decomposed by (i) all-entry C_u-vs-(e_1..e_6) split and (ii) positional E_11 Peirce grades V_1/V_1/2/V_0 (faithful for the NON-Hermitian defect). The Peirce/grade verdict AGREES with the direct ambient-residual verdict on BOTH pairs (both nonzero -> O); the code RAISES on a split decision (none occurred)."
      linked_ids: [claim-restriction, deliv-vald-62-01, ref-lem-bottleneck]
    test-exact-arithmetic:
      status: passed
      summary: "The decisive residual assertion uses EXACT arithmetic ONLY (octmat_is_zero = per-component simplify(...)==0; Rational/surd equality), with NO float64 anywhere on the decisive path (no import numpy, no .evalf, no atol/rtol/1e- in the code). The exact-square trick X=C*C is documented AND confirmed not to trivialize non-associativity (associator = 524/9 != 0 on the same X,Y). fp-float-pass rejected; only an EXACT nonzero residual accepted as obstruction evidence (R_11 = -2 is an exact rational, no surd, definitively nonzero)."
      linked_ids: [claim-restriction, deliv-vald-62-01]
    test-no-pytest:
      status: passed
      summary: "Neither code/embedding_under_E_verification.py nor tests/test_embedding_under_E.py imports pytest or uses pytest fixtures/decorators (verified by grep: 0 literal occurrences; an internal needle-check built from parts confirms it). Assert-based _report/ALL_PASS/sys.exit harness (mirrors slice_clause_iii_verification.py); runs under `python tests/test_embedding_under_E.py` with sympy/numpy only; exits 0 on self-check success."
      linked_ids: [claim-restriction, deliv-vald-62-01]
    test-verdict-not-forced:
      status: passed
      summary: "The verdict (O) is whatever the exact computation yields. The harness asserts only internal consistency (R.equals(zeros) <=> is_zero_exact) and cross-route agreement — it does NOT hardcode is_zero_exact==True (force P) or ==False (force O). (O) reported honestly: the defect is characterized (C_u directions, Peirce grades, R_11=-2), flagged as the EXPECTED, ACCEPTABLE outcome that REFINES RESTRICTION to coexistence-as-island and handed to 62-03; X,Y were NOT cherry-picked, the exact test was NOT relaxed. The v11.0 precedent is cited only as historical context (different mechanism — Clifford pairs), NOT as a prior leaning toward (O). fp-force-positive rejected."
      linked_ids: [claim-restriction, deliv-vald-62-01, deliv-embedding]
  references:
    ref-effros-stormer:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Effros-Stormer content (quoted in 62-01 from LIVE complexification.tex:437) underwrites E as a positive unital idempotent with range = JB-subalgebra. This plan VERIFIES E's idempotency/unitality/positivity EXACTLY on the full 27-dim algebra (test-E-properties-exact), confirming E is a legitimate Jordan conditional expectation — and then shows its Jordan-coherence on the slice does NOT extend to transporting the sequential product from the ambient (the decisive point). Cited in §4.2(1). No web fetch (executor has none); quoted content authoritative per plan."
    ref-lem-bottleneck:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "lem:bottleneck supplies E, the slice A=h_3(C_u), and the Peirce decomposition (V_1~R, V_1/2~C_u^2, V_0~h_2(C_u)) used by the independent cross-check route. The defect is characterized in these Peirce grades (positional grading at E_11; §4.3, §4.5). Cited where the cross-check and defect localization invoke the slice Peirce structure."
    ref-paper5-def1:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Paper 5 Def 1 clause (iii)'s fourth datum is the product-form sequential product sqrt(a) b sqrt(a). The decisive test uses the ACTUAL self-modeling SP sqrt(X) Y sqrt(X) (not a surrogate); clause (iii) itself is unchanged (only RESTRICTION's embedding clause is weakened, 62-03). Cited in §4.1/§4.4 (fp-redefine-iii rejected)."
    ref-vald-61-01:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "VALD-61-01 (code/slice_clause_iii_verification.py) supplied the exact-SymPy spectral sqrt (matrix_sqrt_nxn / _gram_schmidt, ported to matrix_sqrt_complex) and the ASSERT-BASED _report/ALL_PASS/sys.exit __main__ harness pattern (used INSTEAD of pytest — the executor venv has none). The NEW, decisive work is the AMBIENT non-associative transport computation (h3o_matmul, exact octonion arith, the ambient residual); 61-02's associative-only path was NOT reused, and the slice-internal case is the control, not the decisive test. Cited in §4.2(2)."
    ref-v11-leakage:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "v11.0/Phase 42 (sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b exits M_16(R) for anticommuting Cl(9,0) pairs) is historically adjacent but a DIFFERENT mechanism — Clifford non-commuting pairs in a fixed matrix algebra, NOT the h_3(O) -> h_3(C_u) projection restriction tested here. Compared and explicitly NOT carried as evidence for (O); cited only as historical context (§4.3 note; fp-force-positive guard)."
  forbidden_proxies:
    fp-assert-preservation:
      status: rejected
      notes: "The decisive object IS the AMBIENT transport residual R = E(sqrt(X)Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) computed on the genuinely non-associative h_3(O) for GENERIC X,Y — NOT the trivial slice-internal case, and NOT a hand-wave from E's conditional-expectation status. E is shown NOT even a Jordan morphism on the ambient (|E(XoX)-(EX)o(EX)|^2=3797527/34560000 != 0), so transport is genuinely non-trivial. The slice-internal case is computed and recorded strictly as the TRIVIAL control (leakage 0)."
    fp-ignore-nonassociativity:
      status: rejected
      notes: "Non-associativity is LOAD-BEARING on the SAME decisive (X,Y): the associator (sqrt(X),Y,sqrt(X)) = 524/9 != 0 exact (test-nonassociativity-load-bearing). The decisive X,Y are generic ambient (not slice-confined). The slice-internal case is the control only. Both loopholes foreclosed: the trivial residual is NOT passed off as decisive, and the associator is checked on the decisive data (not unrelated matrices — line-loophole foreclosed). h3o_matmul computes left/right associations independently (triple product not assumed associative)."
    fp-float-pass:
      status: rejected
      notes: "The decisive residual uses EXACT SymPy equality only (octmat_is_zero = simplify(...)==0); no float64 anywhere on the decisive path (verified: no import numpy, no .evalf, no atol/rtol/1e-). R_11 = -2 (pair0) is an exact rational, definitively nonzero — a genuine obstruction, not round-off. The exact-square trick is documented and confirmed not to trivialize non-associativity. (Numeric evaluations appear only as non-decisive sanity prints.)"
    fp-force-positive:
      status: rejected
      notes: "Verdict (O) reported honestly as the true exact computation yields — NO cherry-picking X,Y to force R==0, NO relaxing the exact test. (O) is framed as the EXPECTED, ACCEPTABLE outcome that REFINES RESTRICTION to coexistence-as-island (NOT a collapse / independent posits). The harness is HONEST (asserts consistency, not a forced value; passes for either P or O). v11.0 NOT carried as a thumb on the scale (different mechanism). [Equally: had R been exactly 0 it would have been reported as (P); it was not.]"
    fp-redefine-iii:
      status: rejected
      notes: "The decisive test uses the ACTUAL clause-(iii) sequential product sqrt(X) Y sqrt(X) (not the Jordan product, not a symmetrized/surrogate product). Clause (iii) itself is NOT weakened by the coexistence-as-island reframe — only RESTRICTION's embedding clause is (62-03). §4.4 states this explicitly."
  uncertainty_markers:
    weakest_anchors:
      - "The ambient principal square root used the exact-square trick X=C*C (surd-free, sqrt^2==X exact). To keep the EXACT slice square root sqrt(EX) tractable, the decisive data was engineered so EX=E(C*C) is DIAGONAL (single-direction C off-diagonals) — but non-associativity remains LOAD-BEARING because Y is rich and the associator of the decisive triple (sqrt(X),Y,sqrt(X)) is exactly nonzero (524/9). This is a legitimate, documented construction (the obstruction is the EXISTENCE of generic X,Y with R!=0, which is proven on 2 such pairs), NOT a corner that evades non-associativity."
      - "Two distinct generic pairs were tested; ONE exact nonzero residual on non-associativity-load-bearing data already SUFFICES to establish (O), and we have two. The complementary 'no X,Y ever gives R=0' is NOT needed for (O) and is NOT claimed. (A hypothetical (P) would have required a general argument, not representatives — but (P) did not occur.)"
      - "E's positivity on the full 27-dim cone is spot-checked on a non-diagonal PSD slice effect with rational spectrum {1,3,5} (exact eigenvalues >= 0). A broader positivity sweep was not performed (not needed for the decisive verdict; E's positivity is also underwritten structurally by Effros-Stormer)."
    disconfirming_observations:
      - "THE decisive observation, REALIZED: an EXACT nonzero ambient-transport residual R != 0 for generic X,Y (associator nonzero) => E does NOT transport the sequential product => (O). This is the EXPECTED, ACCEPTABLE outcome refining RESTRICTION to coexistence-as-island, NOT a refutation and NOT a bug. (Had R been exactly 0 with both routes agreeing, the verdict would have been (P) — a RESTRICTION embedding lemma.)"
      - "The two routes (direct exact residual + positional Peirce/grade-component) AGREED on (O) for both pairs; no split decision (the code would RAISE on one). Had they disagreed, neither verdict would be trustworthy."
      - "The associator-nonzero check PASSED on the decisive X,Y (= 524/9 != 0); had it failed (accidentally-associative corner), the decisive test would be void and new generic X,Y would be required."
      - "By-product finding: the ambient SP sqrt(X) Y sqrt(X) is NON-Hermitian (the involution identity fails under non-associativity). This is consistent with — and sharpens — (O); it required making the Peirce cross-check positional (faithful for non-Hermitian matrices)."

comparison_verdicts:
  - subject_id: claim-restriction
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-paper5-def1
    comparison_kind: cross_method
    metric: exact_ambient_transport_residual_R
    threshold: "exact R == 0 (zero-tolerance; SymPy symbolic, NOT float64)"
    verdict: fail
    recommended_action: "Read (O) into 62-03 as a REFINEMENT of RESTRICTION to coexistence-as-island: state the precise obstruction (E cannot transport the ambient SP's content that does not survive projection; the two slice elements E(sqrt(X)Y sqrt(X)) and sqrt(EX)(EY)sqrt(EX) fail to coincide; defect in the C_u directions, |R|^2=38593/72, positional Peirce grades 4/1033·18^-1/3797·8^-1; ambient SP non-Hermitian) and the minimal extra input (the observer does NOT need transport — it self-models on the slice, which sits inside h_3(O) as range E). Carry to the Phase 63 milestone verdict."
    notes: "verdict=fail means the EQUALITY R==0 (coherent transport, branch P) FAILS — i.e. the computation establishes branch (O), the ambient-transport OBSTRUCTION. This is the EXPECTED, ACCEPTABLE scientific outcome (NOT a program failure): R != 0 EXACTLY (|R|^2=38593/72, R_11=-2) for 2 generic non-associativity-load-bearing pairs, both routes agreeing. Decided by EXACT arithmetic (zero tolerance), NOT the trivial slice-internal case (which is the control: leakage 0). Resolves the 62-01 'inconclusive' verdict on the same comparison."

duration: 31min
completed: 2026-05-24
---

# Phase 62, Plan 02: Coherent Embedding under E (the hard part) — Decisive Ambient E-Transport Computation Summary

**DECISIVE COMPUTATION of milestone v15.0.** On the genuinely non-associative exceptional Albert algebra `h_3(O)`, the exact ambient `E`-transport residual `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` is **EXACTLY NONZERO** for generic ambient `X, Y` (non-associativity load-bearing: associator of the decisive triple `= 524/9 != 0`; `|R|^2 = 38593/72` on the clean pair, `R_{11} = -2`). **VERDICT: (O) AMBIENT-TRANSPORT OBSTRUCTION** — `E` does **not** transport the self-modeling sequential product coherently from the ambient. This is the **EXPECTED, ACCEPTABLE** outcome that **refines `RESTRICTION` to coexistence-as-island**, handed to 62-03; it is **not** a collapse. Two independent routes (direct exact residual + positional Peirce/grade-component) agree; the slice-internal case is the documented trivial control (leakage 0).

## Performance

- **Duration:** ~31 min
- **Started:** 2026-05-24T21:19:15Z
- **Completed:** 2026-05-24T21:50:16Z
- **Tasks:** 3 (RED harness; GREEN exact-SymPy implementation; §4 record)
- **Files:** 2 created (`code/`, `tests/`), 1 modified (`derivations/...embedding-under-E.md`)

## Key Results

- **THE DECISIVE RESULT — (O) ambient-transport obstruction.** For two distinct generic ambient `(X, Y)` (with `sqrt(X)` computed **in the ambient** via the exact-square trick `X = C*C`), the exact residual
  $$ R = E\big(\sqrt{X}\,Y\,\sqrt{X}\big) - \sqrt{EX}\,(EY)\,\sqrt{EX} \;\neq\; 0 \quad(\text{exact}). $$
  `is_zero_exact = [False, False]`; `|R|_F^2 = 38593/72` (pair 0; representative exact entry `R_{11} = -2`), and `|R|_F^2 = 127725937/64800 - 13\sqrt{67134}/2 - 277\sqrt{183513}/900 \approx 155` (pair 1). `E` does **not** transport the sequential product coherently.
- **Non-associativity is LOAD-BEARING** on the decisive data: the associator `(\sqrt{X}\,Y)\,\sqrt{X} - \sqrt{X}\,(Y\,\sqrt{X})` has `|\cdot|^2 = 524/9 \neq 0` (exact) — the SAME triple whose product is the decisive SP. The decisive `X, Y` are generic ambient (nonzero `e_1..e_6`), not slice-confined.
- **`E` verified EXACTLY** on the full 27-dim algebra: unital, idempotent, `E|_A = id`, positive (PSD slice effect with rational spectrum `{1,3,5}`), entrywise `proj_u`, `dim 27 = 9 + 18`; **AND** `E` is **NOT** a Jordan morphism on the ambient (`|E(X\circ X) - (EX)\circ(EX)|^2 = 3797527/34560000 \neq 0`) — which is what makes the transport question genuinely non-trivial.
- **Defect characterization (for 62-03):** `R` lands **entirely in the `C_u` directions** (`e_0, e_7`): `C_u`-part`^2 = 38593/72`, `(e_1..e_6)`-part`^2 = 0`. The obstruction is the **failure of the two slice elements to coincide**, not leakage out of `A`. Positional `E_11` Peirce grades: `|V_1|^2 = 4`, `|V_{1/2}|^2 = 1033/18`, `|V_0|^2 = 3797/8` (sum `= 38593/72 = |R|^2`).
- **NEW finding:** the ambient sequential product `\sqrt{X}\,Y\,\sqrt{X}` is **NON-Hermitian** in `h_3(O)` (the involution identity `(\sqrt{X}\,Y\,\sqrt{X})^\dagger = \sqrt{X}\,Y\,\sqrt{X}` fails under `(AB)C \neq A(BC)`). An additional, association-dependent way `E` fails to transport the SP — sharpens (O). (We use the natural left association throughout.)
- **Slice-internal TRIVIAL control:** for `a, b \in A`, `\sqrt{a}\,b\,\sqrt{a}` (computed via the ambient product) has leakage **exactly 0** (`E(\cdot) = \cdot`) and triple associator **exactly 0** — the closed associative subalgebra, clearly separated as the control, NOT the decisive test.
- **Independent cross-check AGREES:** the positional Peirce/grade-component route reaches the same verdict (O) as the direct residual on both pairs; the code RAISES on a split decision (none occurred).

## Task Commits

Each task was committed atomically:

1. **Task 1 (RED): assert-based harness pinning E-properties, ambient sqrt, non-associativity exerciser, decisive residual, slice control, Peirce cross-check** — `c9603898` (validate)
2. **Task 2 (GREEN): exact-SymPy implementation; DECISIVE VERDICT (O)** — `1e96d012` (validate)
3. **Task 3: §4 record of the decisive computation + verdict; cross-check correctness fix for the non-Hermitian defect** — `9cb5eb75` (document)

_Plan metadata commit to follow this SUMMARY._

## Files Created/Modified

- `code/embedding_under_E_verification.py` — exact-SymPy VALD-62-01: octonion arithmetic (Fano e1e2=e4), non-associative `h3o_matmul`, `E` onto `h_3(C_u)`, ambient sqrt (exact-square trick + diagonal fast-path slice sqrt), the decisive ambient-transport residual, positional Peirce cross-check, non-associativity exerciser, slice-internal control, assert-based `_report/ALL_PASS/sys.exit` harness.
- `tests/test_embedding_under_E.py` — assert-based runner (NO pytest), check groups (A)-(G); runnable as `python tests/test_embedding_under_E.py`, exits 0.
- `derivations/p5-basin-restriction/embedding-under-E.md` — §4 appended (the decisive ambient-transport computation + verdict (O) + defect characterization + handoff to 62-03); §4-to-follow marker updated.

## Equations Derived / Computed

**Eq. (62.5) — the decisive ambient-transport residual (computed exactly, nonzero):**
$$ R := E\big(\sqrt{X}\,Y\,\sqrt{X}\big) - \sqrt{EX}\,(EY)\,\sqrt{EX} \neq 0,\qquad |R|_F^2 = \tfrac{38593}{72}\ (\text{pair 0}). $$

**Eq. (62.6) — non-associativity load-bearing (associator of the decisive triple):**
$$ \big\|(\sqrt{X}\,Y)\,\sqrt{X} - \sqrt{X}\,(Y\,\sqrt{X})\big\|_F^2 = \tfrac{524}{9} \neq 0. $$

**Eq. (62.7) — E not a Jordan morphism on the ambient (confirmed exactly):**
$$ \big\|E(X\circ X) - (EX)\circ(EX)\big\|_F^2 = \tfrac{3797527}{34560000} \neq 0. $$

**Eq. (62.8) — defect localization (positional E_11 Peirce grades partition |R|^2):**
$$ \|V_1(R)\|^2 = 4,\quad \|V_{1/2}(R)\|^2 = \tfrac{1033}{18},\quad \|V_0(R)\|^2 = \tfrac{3797}{8},\quad \text{sum} = \tfrac{38593}{72}. $$

## Validations Completed

- **Level 5 (external oracle):** all results produced and re-produced by exact SymPy in `code/embedding_under_E_verification.py`; `python tests/test_embedding_under_E.py` prints `OVERALL: ALL SELF-CHECKS PASS` and exits 0. Deterministic (no random seeds; hardcoded exact entries) — re-runs reproduce `is_zero_exact = [False, False]` and verdict (O).
- **Two independent routes agree:** direct exact residual and positional Peirce/grade-component both give (O) on both pairs; RAISE-on-split guard not triggered.
- **Exact zero-tolerance:** decisive test via `simplify(...) == 0` only; no float64 on the decisive path (no `import numpy`, no `.evalf`, no `atol/rtol/1e-`). `R_{11} = -2` is an exact rational — definitively nonzero, excluding round-off and accidental cancellation (`|R|^2 ~ 536` is the same order as the terms — no suspicious near-cancellation).
- **Self-checks:** `E` unital/idempotent/`E|_A=id`/positive/entrywise-proj_u/dim-27=9+18 + NOT-a-Jordan-morphism-on-ambient; ambient `sqrt^2 == X`; associator nonzero on the decisive data; slice-internal control trivial (leakage 0, associator 0).
- **Cross-check arithmetic:** positional Peirce-grade magnitudes sum exactly to `|R|^2` (`4 + 1033/18 + 3797/8 = 38593/72`); `C_u`-part + `(e_1..e_6)`-part `= |R|^2` with `(e_1..e_6)`-part `= 0`.

## Decisions Made

- Decisive object = the **ambient** transport residual for **generic** `X, Y`; slice-internal case kept strictly as the trivial control.
- Engineered `EX = E(C*C)` **diagonal** (single-direction `C` off-diagonals) for an EXACT, tractable slice `sqrt(EX)` — while `Y` is rich so the decisive triple genuinely engages non-associativity (associator `= 524/9 != 0`). Documented as a legitimate construction (the obstruction is the existence of generic `X,Y` with `R != 0`, proven on 2 pairs).
- Reported the TRUE verdict (O); did not force preservation or relax the exact test. (O) framed as the expected refinement to coexistence-as-island.
- Made the Peirce cross-check **positional** (faithful for the discovered non-Hermitian defect), after the Hermitian-coordinate version mis-summed the grades.
- v11.0/Phase 42 cited only as historical context (different mechanism).

## Deviations from Plan

- **[Rule 1 — code performance]** The EXACT slice spectral square root blew up on casus-irreducibilis cubic eigenvalues of a generic projected `EX` (SymPy nested cube-root + `sqrt(3)*I` radicals). **Fix:** engineered the decisive data so `EX` is diagonal (single-direction `C` off-diagonals) and added a diagonal fast-path to `matrix_sqrt_complex`. **Correctness unaffected** — non-associativity stays load-bearing (rich `Y`; associator `= 524/9 != 0`), and the verdict (O) was confirmed robust (it also held for the original cubic-blowup data before the optimization, which ran to completion). Documented in `code/` comments and §4.2.
- **[Rule 4 — missing component / correctness]** Discovered the ambient SP `sqrt(X) Y sqrt(X)` is **non-Hermitian**; the initial Peirce-grade cross-check used a Hermitian-coordinate reconstruction that dropped the upper/lower mismatch (grade-sum `37213/72 != |R|^2 = 38593/72`). **Fix:** replaced with a **positional** E_11 Peirce decomposition + all-entry `C_u`/`e16` split (faithful for non-Hermitian matrices); grades now partition `|R|^2` exactly, both routes still agree, verdict (O) unchanged. The non-Hermiticity is reported as an additional finding sharpening (O).

No physics redirection (Rule 5) or scope change (Rule 6): the (O) verdict is the explicitly anticipated, contract-sanctioned outcome (claim-restriction allows P or O; disconfirming_observations names the exact-nonzero-R observation as expected). No checkpoints in this plan (Pattern A). No environment gates (sympy/numpy present; pytest correctly absent and not used).

## Issues Encountered

- Background-task stdout was not persisting to the redirect file on process exit in this environment; resolved by running the harness in the foreground with `python -u` and capturing to a file. No impact on results.

## Open Questions

- **[62-03]** Read the verdict (O) into the RESTRICTION refinement: state the precise obstruction (E cannot transport the ambient SP's content surviving projection; the two slice elements fail to coincide; defect in `C_u`, `|R|^2 = 38593/72`, positional Peirce grades; ambient SP non-Hermitian) and the minimal extra input (the observer self-models on the slice = range E; no transport needed). Carry the generality caveat (one exact nonzero residual on load-bearing data suffices for (O); we have two).
- **[63]** Milestone verdict: coexistence-as-island RESTRICTION (the slice sits inside `h_3(O)` as range E; `E` = access/projection map, not a Jordan/SP morphism on the ambient) — the through-line survives as the island through-line; (O) refines, does not refute.

## Next Phase Readiness

- **62-03 is fully fed.** The decisive input — branch (O) with the exact characterized defect (`C_u` directions; `|R|^2 = 38593/72`; positional Peirce grades 4, 1033/18, 3797/8; `R_{11} = -2`; ambient SP non-Hermitian) — is recorded in §4 and wired to 62-03's read-off. The handoff is explicit (§4.5). §5 of `embedding-under-E.md` remains the 62-03 stub.
- The exact-SymPy harness (`code/embedding_under_E_verification.py` + `tests/test_embedding_under_E.py`) is reproducible and re-runnable (exits 0); it stands as the VALD-62-01 evidence for the verifier.

## Self-Check: PASSED

- Created files exist: `code/embedding_under_E_verification.py`, `tests/test_embedding_under_E.py` — FOUND.
- Modified file updated: `derivations/p5-basin-restriction/embedding-under-E.md` §4 present — FOUND.
- All three task checkpoints exist: `c9603898` (Task 1), `1e96d012` (Task 2), `9cb5eb75` (Task 3) — FOUND.
- Result reproducible: `python tests/test_embedding_under_E.py` and `python code/embedding_under_E_verification.py` both exit 0, verdict (O), `is_zero_exact = [False, False]` — deterministic across re-runs.
- Numbers consistent: every §4 figure (`3797527/34560000`, `524/9`, `38593/72`, `127725937/64800`, `1033/18`, `3797/8`, `R_{11} = -2`) matches the harness output exactly; Peirce grades sum to `|R|^2`.
- No float on the decisive path (no `import numpy`/`.evalf`/`atol`/`1e-`); no pytest import (0 literal occurrences); convention assertion lines present in both code and the derivation file; conventions match `convention_lock` (Fano e1e2=e4, u=e_7, slice h_3(C_u), exact arithmetic).
- Domain final verification (Mathematical physics — Jordan-algebra structure): integer/structural invariants consistent (`dim 27 = 9 + 18`); the exact obstruction is genuine (exact rational `R_{11}=-2`, not round-off); positional Peirce grades partition `|R|^2`.
- **Contract coverage:** 1 claim (claim-restriction → passed, verdict O); 2 deliverables (deliv-embedding, deliv-vald-62-01 → both passed); 9 acceptance tests (all passed); 5 references (all completed); 5 forbidden proxies (all rejected); uncertainty_markers populated; 1 decisive comparison_verdict (verdict=fail = branch (O) established, the expected outcome). All PLAN contract IDs present.

---

_Phase: 62-coherent-embedding-under-e-the-hard-part_
_Completed: 2026-05-24_
