---
phase: 62-coherent-embedding-under-e-the-hard-part
plan: 01
depth: full
one-liner: "Set up the bottleneck conditional expectation E: h_3(O) -> h_3(C_u) explicitly (Effros-Stormer positive unital idempotent; Jordan-product-preserving on the slice, NOT a Jordan morphism on ambient elements) and framed the decisive crux as AMBIENT E-transport of the sequential product — verdict deferred to 62-02, fork kept open"
subsystem: [formalism, derivation]
tags: [jordan-algebra, octonions, conditional-expectation, sequential-product, peirce-decomposition, non-associativity, effros-stormer, albert-algebra]

requires:
  - phase: 61-slice-satisfies-clause-iii
    provides: "slice A = h_3(C_u) ~ M_3(C)^sa satisfies all four Paper 5 Def 1 clauses intrinsically; clause (iii) AS STATED; product-form SP factorizes on the ASSOCIATIVE M_9(C)^sa; induced-by-E DEFERRED here"
  - phase: 60-two-composites
    provides: "two-composites distinction (V_BM vs BGW (x)~ on h_3(O)) type-distinct; rem:converse CONFIRMED-WITH-CAVEAT (minimal != maximal direct-summand form)"
provides:
  - "Explicit E: h_3(O) -> h_3(C_u) as entrywise proj_u (C_u=span{1,e_7}); positive, unital, idempotent, E|_A=id; range = Jordan subalgebra (Effros-Stormer); dim 9, ker 18"
  - "Precise statement of what E preserves: Jordan product ON THE SLICE (E|_A=id; Jordan-product-preserving embedding) but E is NOT a Jordan morphism on AMBIENT elements (E(XoX) != (EX)o(EX))"
  - "Decisive crux FRAMED as ambient E-transport residual R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) for GENERIC ambient X,Y; well-posed exact-arithmetic spec for 62-02"
  - "Slice-internal SP recorded as TRIVIAL control (closed associative subalgebra, leakage 0, associator 0); CORRECTED RESTRICTION (coexistence-as-island); obstruction-or-preservation fork OPEN (O expected, refines RESTRICTION)"
affects: [62-02 (decisive exact computation of R), 62-03 (verdict on the fork), 63 (milestone verdict)]

methods:
  added: ["explicit entrywise C_u-projection conditional expectation on h_3(O)", "Jordan-morphism-on-ambient diagnostic E(XoX) vs (EX)o(EX)", "ambient-transport residual R as the decisive SP-coherence object", "exact-square trick X=C^2 for exact ambient sqrt while keeping X,Y generic ambient"]
  patterns: ["control-vs-decisive separation: slice-internal (trivial, leakage 0) vs ambient (non-associativity load-bearing)", "type/category + Peirce-grade ledger as dimensional-analysis analog", "forward-reference numbers tagged [UNVERIFIED - forward reference to 62-02]"]

key-files:
  created: ["derivations/p5-basin-restriction/embedding-under-E.md (§0-§3; §4/§5 to-follow stubs)"]
  modified: []

key-decisions:
  - "E defined as entrywise proj_u (= code/octonion_algebra.py::proj_u, u=e_7); range = h_3(C_u) ~ M_3(C)^sa"
  - "Decisive object = AMBIENT transport residual R for GENERIC X,Y (non-associativity load-bearing), NOT the slice-internal trivial case"
  - "Adopted CORRECTED RESTRICTION (coexistence-as-island, Bryan 2026-05-24): RESTRICTION's EMBEDDING clause weakened; clause (iii) ITSELF unchanged"
  - "Dropped the v11.0/Phase 42 sqrt(T_a)T_b sqrt(T_a)-exits-M_16(R) precedent as a leaning-toward-obstruction prior (different mechanism: Clifford pairs, not the projection restriction)"
  - "Fork kept genuinely OPEN; obstruction (O) framed as EXPECTED + a refinement to island, NOT a program collapse; verdict deferred to 62-02/62-03"

patterns-established:
  - "Pattern: separate the closed-associative-slice control (leakage 0, associator 0) from the non-associative ambient decisive test; foreclose the unrelated-matrices line-loophole"
  - "Pattern: a conditional expectation that preserves the Jordan product on its range need NOT be a Jordan morphism on the ambient, and need NOT transport the non-Jordan triple product"

conventions:
  - "natural units (hbar=1, k_B=1); pure algebra — no physical dimensions"
  - "Jordan product a o b = (1/2)(ab+ba)"
  - "sequential product a&b = sqrt(a) b sqrt(a) (Luders/self-modeling, temporally asymmetric; principal CFC sqrt)"
  - "octonion Fano e_1 e_2 = e_4; complex structure u = e_7 (any u in S^6 equivalent under G_2)"
  - "slice A = h_3(C_u) ~ M_3(C)^sa (maximal C*-target inside h_3(O); single F_4-orbit)"
  - "Peirce eigenvalues {0, 1/2, 1}"

plan_contract_ref: ".gpd/phases/62-coherent-embedding-under-e-the-hard-part/62-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-restriction:
      status: partial
      summary: "SETUP half established: E: h_3(O) -> A constructed explicitly as a positive unital idempotent (Effros-Stormer; Jordan-product-preserving embedding => E IS coherent with the Jordan product ON THE SLICE), and the decisive crux FRAMED as ambient E-transport of the sequential product (E(sqrt(X) Y sqrt(X)) =? sqrt(EX)(EY)sqrt(EX) for generic X,Y, non-associativity load-bearing). The TRANSPORT verdict (the load-bearing part of claim-restriction) is NOT closed by this plan — it is computed in 62-02 and read in 62-03. Slice-internal case recorded as the trivial control; CORRECTED RESTRICTION (coexistence-as-island) stated; fork OPEN, no pre-commitment."
      linked_ids: [deliv-embedding, test-E-explicit, test-E-preserves-stated, test-crux-framed-ambient, test-slice-triviality, test-corrected-restriction, test-fork-open, ref-effros-stormer, ref-lem-bottleneck, ref-hanche-olsen, ref-paper5-def1]
      evidence:
        - verifier: gpd-executor
          method: explicit construction + verbatim-quote grounding + structural derivation + qualitative numerical sanity (slice vs ambient associator)
          confidence: medium
          claim_id: claim-restriction
          deliverable_id: deliv-embedding
          acceptance_test_id: test-E-explicit
          reference_id: ref-lem-bottleneck
          evidence_path: "derivations/p5-basin-restriction/embedding-under-E.md"
  deliverables:
    deliv-embedding:
      status: passed
      path: derivations/p5-basin-restriction/embedding-under-E.md
      summary: "§0-§3 created: (§1) E explicit entrywise proj_u, four CE properties stated+justified, Effros-Stormer quoted verbatim (range = Jordan subalgebra; Jordan-product-preserving embedding), Peirce decomposition of A at E_11 (V_1~R, V_{1/2}~C_u^2, V_0~h_2(C_u)~M_2(C)^sa; 1+4+4=9); (§2) what E preserves stated precisely (Jordan on slice YES; NOT a Jordan morphism on ambient; SP transport NOT claimed — fp-assert-preservation rejected); (§3) crux framed as ambient E-transport, slice-internal triviality control, exact-arithmetic 62-02 spec, structural expectation without pre-deciding, fork open, corrected RESTRICTION (coexistence-as-island). §4/§5 to-follow stubs for 62-02/62-03."
      linked_ids: [claim-restriction, test-E-explicit, test-E-preserves-stated, test-crux-framed-ambient, test-slice-triviality, test-corrected-restriction, test-fork-open]
  acceptance_tests:
    test-E-explicit:
      status: passed
      summary: "E constructed with explicit entrywise-proj_u formula (identity on real diagonal alpha,beta,gamma; proj_u on off-diagonal x1,x2,x3; proj_u = code::proj_u lines 527-542, keeps comps 0,7). Four CE properties each stated with justification: unital E(I_3)=I_3; idempotent E o E = E (proj_u idempotent — numerically confirmed proj_u(proj_u(b))=proj_u(b)); E|_A=id; positive (Effros-Stormer + standard conditional expectation, exact eigenvalue check explicitly deferred to 62-02). Effros-Stormer quoted verbatim from complexification.tex:437. dim(range E)=9=dim A, ker E=18, 27=9+18 confirmed."
      linked_ids: [claim-restriction, deliv-embedding, ref-effros-stormer, ref-lem-bottleneck]
    test-E-preserves-stated:
      status: passed
      summary: "Deliverable states precisely: E IS coherent with the Jordan product a o b ON THE SLICE (lem:bottleneck Jordan-product-preserving embedding + E|_A=id; §2.1). Deliverable ALSO states E is NOT a Jordan morphism on AMBIENT elements (E(X o X) != (EX) o (EX) in general; structural argument via squared-norm of killed components; §2.2). The sequential-product transport is explicitly a SEPARATE, unresolved question (§2.3), NOT folded into 'E preserves everything' — the hand-wave 'E is a conditional expectation so it transports clause (iii)' is explicitly rejected (fp-assert-preservation)."
      linked_ids: [claim-restriction, deliv-embedding, ref-lem-bottleneck, ref-effros-stormer]
    test-crux-framed-ambient:
      status: passed
      summary: "Crux framed explicitly as AMBIENT E-transport: decisive object = E(sqrt(X) Y sqrt(X)) =? sqrt(EX)(EY)sqrt(EX) for GENERIC ambient X (PSD), Y in h_3(O), NOT the slice-internal case (§3.1, §3.3). sqrt(X) in the ambient (power-associative CFC); non-associativity ((xy)z != x(yz)) genuinely engaged, with a mandated associator-nonzero check on the chosen X,Y. Sequential product tagged as a CFC non-Jordan triple product. E not a Jordan morphism on ambient. Explicitly deferred to 62-02 for exact computation (§4 stub) — NOT asserted here."
      linked_ids: [claim-restriction, deliv-embedding, ref-paper5-def1, ref-lem-bottleneck]
    test-slice-triviality:
      status: passed
      summary: "Slice-internal triviality recorded plainly (§3.2): A = h_3(C_u) is a CLOSED, ASSOCIATIVE Jordan subalgebra (= range E); for a,b in A, sqrt(a) b sqrt(a) stays in A with leakage EXACTLY 0 and triple associator EXACTLY 0; SP datum induced TRIVIALLY; non-associativity NOT engaged. Presented as the documented CONTROL, clearly distinguished from the decisive ambient-transport test. Both reward-hack loopholes foreclosed (fp-ignore-nonassociativity): passing the trivial residual off as decisive, AND the unrelated-matrices line-loophole. Qualitative sanity confirmed: slice octonion associator ~3.7e-15, ambient ~22 mean."
      linked_ids: [claim-restriction, deliv-embedding, ref-lem-bottleneck]
    test-corrected-restriction:
      status: passed
      summary: "CORRECTED RESTRICTION (coexistence-as-island) stated (§3.7): observer self-models on the slice (Phase 61, all four clauses verbatim) and the slice sits inside h_3(O) as the range of E. RESTRICTION's EMBEDDING clause weakened to Bryan's exact wording ('the observer self-models on the slice, which sits inside h_3(O) as the range of the projection E'), NOT 'coherently induced from the ambient via E'. Clause (iii) ITSELF NOT weakened (fp-redefine-iii) — only the embedding clause. V_BM remains the observer's own A (x) A ~ M_9(C)^sa, not conflated with the BGW (x)~ on h_3(O) (fp-conflate-composites; Phase 60 distinction explicitly preserved; basin fixes TYPE not composite)."
      linked_ids: [claim-restriction, deliv-embedding, ref-paper5-def1]
    test-fork-open:
      status: passed
      summary: "Obstruction-or-preservation fork stated and kept OPEN with corrected verdict semantics (§3.6): (P) exact R=0 -> RESTRICTION embedding lemma (62-03); (O) exact R!=0 -> ambient-transport obstruction (62-03), the EXPECTED/acceptable outcome that REFINES RESTRICTION to coexistence-as-island (self-contained C* island; through-line survives; NOT independent posits, NOT collapse). No pre-commitment to either branch; (O) explicitly framed as a refinement, not a program collapse. The v11.0/Phase 42 leakage precedent explicitly NOT carried as a prior leaning toward (O) — different mechanism (Clifford pairs, not the projection restriction). 62-02 -> 62-03 handoff wired."
      linked_ids: [claim-restriction, deliv-embedding]
  references:
    ref-effros-stormer:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Effros-Stormer 1979 content quoted VERBATIM from the LIVE lem:bottleneck proof (complexification.tex:437) where the deliverable asserts E's range/positivity/idempotency: 'the range of a positive unital idempotent on a JB-algebra is a JB-subalgebra... the embedding is moreover Jordan-product-preserving.' Surfaced in §1.3 (range = Jordan subalgebra), §1.2d (positivity), §2.1 (Jordan-product-preserving on slice). Tagged IDENTITY_CLAIM with IDENTITY_SOURCE: citation. No web fetch attempted (executor has none)."
    ref-lem-bottleneck:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "LIVE lem:bottleneck (complexification.tex lines 409-487) read and quoted: lemma statement (412-413: conditional expectations with Jordan-product-preserving embedding), Effros-Stormer (437), Peirce decomposition (iii) (481-486: V_1~R, V_{1/2}~C_u^2, V_0~h_2(C_u)~M_2(C)^sa). Supplies E, the slice A=h_3(C_u), and the Peirce structure E restricts through (§1.4). Surfaced where the deliverable asserts E's range/Jordan-coherence and the slice Peirce grades; the GAP (lem:bottleneck is silent on the sequential product) is made explicit as the §3 crux."
    ref-hanche-olsen:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Hanche-Olsen induced-vs-imported framing (via Phase 60 derivation files two-composites.md / rem-converse-bgw.md content) used to frame the obstruction-or-preservation fork: if the SP datum on A can be INDUCED by E from h_3(O) -> (P); if it requires IMPORTING structure not in the ambient -> (O) obstruction. Surfaced in §3.6/§3.7 (fork + coexistence-as-island = self-contained island vs ambient-induced). Read of full paper not required (content as used in Phase 60)."
    ref-paper5-def1:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Paper 5 Def 1 clause (iii) (LIVE qm-from-self-modeling/main.tex sms:minimal, 351-353) — 'product-form sequential product' is the datum whose coherence under E is at stake. Surfaced in §3.1 (the SP is clause iii's fourth datum) and §3.7 (clause iii kept verbatim; only the embedding clause weakened). Clause (iii) integrity preserved (fp-redefine-iii)."
  forbidden_proxies:
    fp-assert-preservation:
      status: rejected
      notes: "Explicitly rejected in §2.3 and reaffirmed in §3.1/§3.8. The decisive object is framed as the OPEN ambient transport residual R for generic X,Y and its computation deferred to 62-02. lem:bottleneck's Jordan-product-preserving property is explicitly NOT treated as covering the non-Jordan triple-product transport; E is shown to not even be a Jordan morphism on ambient elements (§2.2). The 'E is a conditional expectation so it transports clause (iii)' hand-wave is named and rejected."
    fp-ignore-nonassociativity:
      status: rejected
      notes: "Rejected in §3.2/§3.3. The slice-internal sqrt(a) b sqrt(a) is recorded plainly as TRIVIAL (closed associative subalgebra, leakage 0, associator 0, non-associativity not engaged) and tagged the CONTROL. The decisive object is the AMBIENT transport residual for generic X,Y with non-associativity load-bearing (mandated associator-nonzero check on the SAME X,Y). Both loopholes foreclosed: (i) passing the trivial slice case off as decisive, (ii) the unrelated-matrices exerciser line-loophole. Qualitative sanity check confirms slice assoc ~1e-15 vs ambient ~22."
    fp-redefine-iii:
      status: rejected
      notes: "Rejected in §3.7. The reframe weakens RESTRICTION's EMBEDDING clause ONLY ('induced from the ambient via E' -> 'observer self-models on the slice, which sits inside h_3(O) as the range of E'). Clause (iii) itself stands verbatim (all four data + minimality), established intrinsically in Phase 61. The deliverable explicitly states weakening the embedding clause is NOT weakening clause (iii)."
    fp-conflate-composites:
      status: rejected
      notes: "Rejected in §0.3 and §3.7. V_BM remains the observer's OWN internal composite A (x) A ~ M_9(C)^sa, never identified with the BGW (x)~ universe-tensoring of h_3(O). Coexistence-as-island stated as FULLY CONSISTENT with the Phase 60 two-composites distinction: the island has its own composite; the basin fixes the TYPE M_3(C)^sa, not the composite."
    fp-force-positive:
      status: rejected
      notes: "Rejected in §3.5/§3.6. The fork is kept genuinely OPEN with no pre-commitment to either branch; the verdict is decided by 62-02's exact computation, not by expectation. An obstruction (O) is framed as EXPECTED + a refinement to coexistence-as-island, NOT a collapse. The v11.0/Phase 42 sqrt(T_a)T_b sqrt(T_a) precedent is explicitly DROPPED as a leaning-toward-(O) prior (different mechanism — Clifford non-commuting pairs in a fixed matrix algebra, NOT the h_3(O)->h_3(C_u) projection restriction), per the plan-checker warning."
  uncertainty_markers:
    weakest_anchors:
      - "ref-effros-stormer and ref-lem-bottleneck establish E as a JORDAN conditional expectation (positive, unital, idempotent, Jordan-product-preserving embedding) but only ON THE SLICE (E|_A=id). NEITHER says E is a Jordan morphism on AMBIENT elements (it is NOT: E(XoX) != (EX)o(EX)), and neither says anything about TRANSPORTING the sequential product from the ambient. The decisive ambient-transport question rests on a property the supplying lemmas do NOT provide — the genuinely non-trivial crux, deferred to 62-02."
      - "The slice-internal sequential-product datum is TRIVIAL (closed associative subalgebra = range E; leakage 0, associator 0) — qualitatively reconfirmed this plan (slice octonion associator ~3.7e-15 vs ambient ~22 over 2000 random triples; exact h_3(O) transport residual is 62-02 work). So the slice-internal case carries NO information about ambient transport; only the AMBIENT transport residual is decisive. E's positivity/idempotency on the full 27-dim algebra is STATED here and to be COMPUTED exactly in 62-02."
    unvalidated_assumptions:
      - "E's positivity on the full positive cone of h_3(O) is stated (via Effros-Stormer + standard conditional expectation) but the explicit eigenvalue check on PSD test elements is deferred to 62-02."
      - "Representative forward-reference magnitudes (E(XoX)-(EX)o(EX) Frobenius ~22; slice associator ~1e-15; ambient associator ~170) are tagged [UNVERIFIED - forward reference to 62-02]; the qualitative claims (E not a Jordan morphism on ambient; slice trivially closed; ambient non-associative) are what the decisive framing rests on and are sanity-confirmed."
    competing_explanations:
      - "Branch (P): E transports the sequential product coherently (exact R=0) -> RESTRICTION embedding lemma. Branch (O): E does not (exact R!=0) -> ambient-transport obstruction refining RESTRICTION to coexistence-as-island. The setup pre-commits to NEITHER; 62-02's exact R decides."
    disconfirming_observations:
      - "If E (entrywise C_u-projection) FAILS to be a positive unital idempotent onto a Jordan subalgebra of h_3(O) — e.g. E o E != E on the full 27-dim algebra, or the range is not a Jordan subalgebra — the setup itself is wrong and lem:bottleneck's E must be reconstrued. (62-02 verifies idempotency/unitality/positivity exactly.) proj_u idempotency confirmed numerically this plan; full-27-dim exact check deferred to 62-02 by design."
      - "THE decisive observation (deferred to 62-02): the exact AMBIENT transport residual R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX) for generic X,Y. R != 0 => ambient-transport obstruction (EXPECTED; refines RESTRICTION to island, NOT a refutation). R = 0 => coherent transport (RESTRICTION embedding lemma). The fork must NOT be pre-decided; the v11.0 leakage precedent is NOT carried as a prior."

comparison_verdicts:
  - subject_id: claim-restriction
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-paper5-def1
    comparison_kind: cross_method
    metric: exact_ambient_transport_residual_R
    threshold: "exact R == 0 (zero-tolerance; SymPy symbolic, NOT float64)"
    verdict: inconclusive
    recommended_action: "Compute exact R in 62-02 (VALD-62-01) on generic ambient X,Y (exact-square trick X=C^2; off-diagonal not in C_u; mandated associator-nonzero check; independent Peirce/grade cross-check). 62-03 reads the verdict: R=0 -> (P) RESTRICTION embedding lemma; R!=0 -> (O) ambient-transport obstruction refining RESTRICTION to coexistence-as-island."
    notes: "This plan (62-01) DEFINES the decisive comparison and frames it; it does NOT compute it. Verdict inconclusive BY DESIGN — the setup must keep the fork open and not assert the transport answer (fp-assert-preservation, fp-force-positive). The decisive object is the ambient residual, NOT the slice-internal trivial case (leakage 0)."

duration: 5min
completed: 2026-05-24
---

# Phase 62, Plan 01: Coherent Embedding under E (the hard part) — Setup + Crux Framing Summary

**Set up the bottleneck conditional expectation E: h_3(O) -> h_3(C_u) explicitly (Effros-Stormer positive unital idempotent; Jordan-product-preserving on the slice but NOT a Jordan morphism on ambient elements), and framed the decisive crux as AMBIENT E-transport of the sequential product — verdict deferred to 62-02, obstruction-or-preservation fork kept genuinely open.**

## Performance

- **Duration:** ~5 min
- **Started:** 2026-05-24T21:06:46Z
- **Completed:** 2026-05-24T21:11:40Z
- **Tasks:** 2
- **Files modified:** 1 (created)

## Key Results

- **Explicit E.** `E : h_3(O) -> h_3(C_u)` is the **entrywise `C_u`-projection** (`= code/octonion_algebra.py::proj_u`, `u=e_7`): identity on the real diagonal, `proj_u` on each off-diagonal octonion. It is **positive, unital (`E(I_3)=I_3`), idempotent (`E o E = E`), `E|_A = id`**; its range `A = h_3(C_u) ~ M_3(C)^sa` is a **Jordan subalgebra** with **Jordan-product-preserving embedding** (Effros-Stormer, quoted verbatim from `complexification.tex:437`). `dim(range E)=9`, `ker E=18`, `27=9+18`.
- **What E preserves — precisely.** `E` **IS** coherent with the **Jordan product `a o b` ON THE SLICE** (`E|_A=id`), but `E` is **NOT** a Jordan morphism on **ambient** elements (`E(X o X) != (EX) o (EX)` in general). So `E` does **not** transport even the Jordan structure from the ambient — a fortiori the sequential product need not be transported. The hand-wave "`E` is a conditional expectation, so it transports clause (iii)" is **explicitly rejected**.
- **Decisive crux FRAMED (not answered).** The decisive object is the **ambient transport residual** `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` for **GENERIC ambient** `X,Y` (non-associativity load-bearing). `R=0 => (P)` coherent transport; `R!=0 => (O)` ambient-transport obstruction. **Verdict deferred to 62-02** (exact arithmetic), read in 62-03.
- **Slice-internal triviality = the CONTROL.** The slice is a **closed associative** subalgebra (`= range E`), so slice-internal `sqrt(a) b sqrt(a)` has **leakage 0 / associator 0** — it carries **no** information about ambient transport. Recorded plainly as the control; both reward-hack loopholes foreclosed.
- **CORRECTED RESTRICTION (coexistence-as-island).** `RESTRICTION`'s **embedding clause** weakened (observer self-models on the slice, which sits inside `h_3(O)` as the range of `E`); **clause (iii) itself unchanged**; `V_BM = A (x) A` **not conflated** with the ambient. An obstruction **(O) is EXPECTED and REFINES** `RESTRICTION` to a self-contained C* island — **not** a collapse. Fork kept **open**; v11.0/Phase 42 precedent **dropped** as a prior.

## Task Commits

Each task was committed atomically:

1. **Task 1: Construct E explicitly; state what E preserves (§0–§2)** — `ec944a30` (derive)
2. **Task 2: Frame the crux as ambient E-transport; slice-internal control; corrected RESTRICTION; open fork (§3 + §4/§5 stubs)** — `e0cb2bcb` (derive)

_Plan metadata commit to follow this SUMMARY._

## Files Created/Modified

- `derivations/p5-basin-restriction/embedding-under-E.md` — Phase 62 deliverable, §0–§3 (SETUP + CRUX FRAMING); §4 (62-02 exact computation) and §5 (62-03 verdict) are explicit to-follow stubs.

## Equations Derived

**Eq. (62.1) — Explicit E (entrywise `C_u`-projection):**

$$
E:\;(\alpha,\beta,\gamma;\,x_1,x_2,x_3)\;\longmapsto\;
(\alpha,\beta,\gamma;\,\mathrm{proj}_u(x_1),\mathrm{proj}_u(x_2),\mathrm{proj}_u(x_3)),
\qquad
\mathrm{proj}_u\!\big(\textstyle\sum_k b_k e_k\big)=b_0+b_7 e_7\ (u=e_7).
$$

**Eq. (62.2) — Peirce decomposition of A at the rank-1 idempotent `E_11` (`lem:bottleneck` (iii)):**

$$
A = V_1(E_{11})\oplus V_{1/2}(E_{11})\oplus V_0(E_{11}),\quad
V_1\cong\mathbb{R},\ V_{1/2}\cong\mathbb{C}_u^2,\ V_0\cong h_2(\mathbb{C}_u)\cong M_2(\mathbb{C})^{sa},\quad 1+4+4=9.
$$

**Eq. (62.3) — E is NOT a Jordan morphism on ambient elements:**

$$
E(X\circ X)\;\neq\;(EX)\circ(EX)\quad\text{for generic } X\in h_3(\mathbb{O}).
$$

**Eq. (62.4) — The decisive ambient transport residual (the 62-02 object):**

$$
R \;:=\; E\big(\sqrt{X}\,Y\,\sqrt{X}\big)\;-\;\sqrt{EX}\,(EY)\,\sqrt{EX},
\qquad X,Y\in h_3(\mathbb{O})\ \text{generic};\qquad
R=0\Rightarrow(\mathrm{P}),\ R\neq 0\Rightarrow(\mathrm{O}).
$$

## Validations Completed

- **Structural / type consistency.** Real-dimension bookkeeping `27 = 9 (range) + 18 (ker)` and slice Peirce `9 = 1 + 4 + 4` both exact. Type/category ledger: Jordan product (binary Jordan op) and sequential product (CFC triple product) kept in distinct categories; `V_BM` (OUS self-composite) never identified with the BGW bifunctor on `h_3(O)`.
- **Anchor grounding.** Effros-Stormer and `lem:bottleneck` (iii) quoted **verbatim** from the LIVE `complexification.tex` (lines 437, 481-486); lemma statement (412-413) confirms the Jordan-product-preserving embedding.
- **Numerical sanity (control-vs-decisive).** `code/octonion_algebra.py::proj_u` confirmed idempotent (`proj_u(proj_u(b)) = proj_u(b)`) and to keep only components 0,7. Over 2000 random triples: **slice (`C_u`) octonion associator max ~3.7e-15** (machine zero — slice associative, leakage 0) vs **ambient octonion associator mean ~22** (`O(1)` — `O` non-associative). This confirms the framing qualitatively; it is a sanity check on the control-vs-decisive distinction, **NOT** the decisive exact `h_3(O)` transport residual (which is 62-02 by design).

## Decisions Made

- E defined as the entrywise `C_u`-projection (`= code::proj_u`, `u=e_7`); range `= h_3(C_u) ~ M_3(C)^sa` (`lem:bottleneck` (ii)).
- Decisive object set to the **ambient** transport residual `R` for **generic** `X,Y` (non-associativity load-bearing) — **not** the slice-internal trivial case.
- Adopted the **CORRECTED RESTRICTION (coexistence-as-island)** (Bryan 2026-05-24): weaken `RESTRICTION`'s embedding clause only; keep clause (iii) verbatim.
- **Dropped** the v11.0/Phase 42 `sqrt(T_a)T_b sqrt(T_a)`-exits-`M_16(R)` precedent as a leaning-toward-obstruction prior (different mechanism: Clifford non-commuting pairs, not the projection restriction) — per the plan-checker warning.
- Fork kept **genuinely open**; obstruction (O) framed as EXPECTED + a refinement, not a collapse; verdict deferred to 62-02/62-03.

## Deviations from Plan

None — plan executed exactly as written. Both tasks completed with all `<verify>`/`<done>` criteria met; no deviation rules invoked; no environment gates; no checkpoints in this plan (Pattern A, checkpoint-free).

## Issues Encountered

None. (One housekeeping note: the macOS `date -j` epoch parse mis-handled the UTC stamp; duration recomputed with Python UTC — purely a metadata-tooling detail, no impact on the deliverable.)

## Open Questions

- **[62, the load-bearing part — deferred to 62-02]** Is the exact ambient transport residual `R = E(sqrt(X) Y sqrt(X)) - sqrt(EX)(EY)sqrt(EX)` zero (P) or nonzero (O) for generic `X,Y` in `h_3(O)`, with non-associativity genuinely engaged? An exact `R != 0` is the EXPECTED outcome and would refine `RESTRICTION` to coexistence-as-island.
- **[62-02 method]** Confirm `E`'s positivity/idempotency/unitality **exactly** on the full 27-dim algebra (eigenvalue checks); construct generic ambient `X,Y` via the exact-square trick `X = C^2` while verifying the associator is nonzero on the chosen `X,Y`; cross-check the residual via the Peirce/grade-component route.
- **[63]** The milestone verdict (clean `RESTRICTION` theorem vs precisely-characterized obstruction → coexistence-as-island) follows in Phase 63.

## Next Phase Readiness

- **62-02 (VALD-62-01) is fully specified.** §3.3–§3.4 give the exact-arithmetic spec: generic ambient `X,Y` (exact-square trick), associator-nonzero mandate, the residual `R` (zero-tolerance), and the independent Peirce cross-check. The handoff is wired: 62-02's exact `R` is the decisive input to 62-03's verdict.
- The deliverable file `derivations/p5-basin-restriction/embedding-under-E.md` is ready for 62-02 to append §4 and 62-03 to append §5.

## Self-Check: PASSED

- Created file exists: `derivations/p5-basin-restriction/embedding-under-E.md` — FOUND.
- Both task checkpoints exist: `ec944a30` (Task 1), `e0cb2bcb` (Task 2) — FOUND.
- Numerical sanity reproducible: `proj_u` idempotency + slice/ambient associator separation re-runnable from `code/octonion_algebra.py` (seed 62012024).
- Convention consistency: deliverable `ASSERT_CONVENTION` header matches `convention_lock` (riemannian_fisher metric, natural units, pure-algebra N/A fields) and the milestone artifacts (`claim.md`, `slice-clause-iii.md`).
- Domain final verification (Mathematical physics — `topological`/`representation` triggers do not apply; pure Jordan-algebra structure): integer/structural invariants consistent (`dim 27=9+18`, Peirce `9=1+4+4`); no anomaly/modular/index content in this setup plan.
- **Contract coverage:** 1 claim (claim-restriction → partial, by design), 1 deliverable (deliv-embedding → passed), 6 acceptance tests (all passed), 4 references (all completed: read+cite), 5 forbidden proxies (all rejected), uncertainty_markers populated, 1 decisive comparison_verdict (inconclusive, by design — deferred to 62-02). All PLAN contract IDs present.

---

_Phase: 62-coherent-embedding-under-e-the-hard-part_
_Completed: 2026-05-24_
