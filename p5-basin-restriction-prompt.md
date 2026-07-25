# GPD Milestone: The P5 <-> Basin Restriction Lemma

**The spine of the Radical Relativity program: is "self-modeling -> QM -> h_3(O)" a
through-line, or two independent posits?** Prove or disprove a single algebraic claim.

Written 2026-05-23 after a fresh adversarial pass identified this as the deepest
unproven, load-bearing join in the program. Self-contained: all needed definitions are
inline (do NOT trust the papers/ copies in this repo; they predate the 2026-05-23
reframe - the live sources are in ~/repos/blog/landing/papers/).

---

## The tension (why this is the spine)

- **Paper 5** proves: a finite faithful self-modeling system has state space
  M_n(C)^sa. It reaches the COMPLEX field via clause (iii) below
  (minimal composite / local tomography), which *requires a well-behaved composite to
  exist* - this is exactly the step that excludes the real and quaternionic alternatives.
- **Paper 7** selects h_3(O) (the exceptional Jordan algebra, 27-dim) as the universe
  "basin" precisely BECAUSE it is NON-composable (it is the unique non-special simple
  formally real Jordan algebra; it admits no well-behaved Jordan-tensor composite, in
  the Barnum-Graydon-Wilce sense).
- So: the observer is forced COMPLEX by *having* a composite; the basin is forced
  OCTONIONIC by having *no* composite. The program asserts these coexist - observer = a
  complex C*-subsystem that accesses h_3(O) through a Peirce "bottleneck" slice; basin =
  the non-composable whole; the access is Peirce projection, NOT tensor factorization.
  **But the lemma that makes this coherent has never been proved.**

## The claim to PROVE or DISPROVE

> **(RESTRICTION).** Let an observer be a finite faithful self-modeling system (Paper 5
> Def 1) embedded in h_3(O). It accesses h_3(O) through the C*-bottleneck slice of
> Lemma `lem:bottleneck`: the maximal complex C*-target inside h_3(O) is
> A = h_3(C_u) ≅ M_3(C)^sa for some u in S^6 ⊂ Im(O), reached by a positive unital
> conditional expectation E: h_3(O) -> A (Effros-Stormer). CLAIM: this slice A satisfies
> Paper 5 Definition 1 clause (iii) (minimal internal composite / local tomography), and
> the observer's body-model composite required by clause (iii) is realized COHERENTLY as
> a sub-structure of h_3(O) induced by the Peirce/bottleneck restriction. Consequently
> Paper 5's theorem applies to the slice and certifies the observer's complex C*
> structure - even though h_3(O) as a whole is non-composable.

Prove it: the "self-modeling -> QM -> this basin" through-line is real.
Disprove it (exhibit a structural obstruction): the observer's C and the basin's O are
INDEPENDENT posits, and the program must concede it has two unconnected foundations.

## Inline definitions (authoritative; use these, not the repo's stale papers/)

**Paper 5 Definition 1 (self-modeling system).** A tuple (V, phi, V_BM) with:
(i) V a nontrivial finite-dim spectral order-unit space (>= 2 orthogonal nontrivial
projective units);
(ii) phi: V_B -> V_M an order isomorphism (faithful tracking);
(iii) V_BM the MINIMAL composite order-unit space carrying product states, product
effects, non-signaling constraints, and a product-form sequential product (minimal
internal composite) - this clause is what forces local tomography, hence the complex
field;
(iv) V has no nontrivial direct-sum decomposition (simple).
Theorem (Paper 5): every such system is M_n(C)^sa in the complex case.

**Paper 7 `lem:bottleneck` (C*-bottleneck universality).** Among positive unital
idempotents E: h_3(O) -> A onto Jordan subalgebras A isomorphic to the s.a. part of a
finite-dim complex C*-algebra: every range is A ≅ ⊕_k M_{n_k}(C)^sa with sum n_k <= 3;
the maximal-range targets are A ≅ M_3(C)^sa ≅ h_3(C_u), u in S^6, forming a single
F_4-orbit; and for a rank-1 idempotent in h_3(C_u), the Peirce 0-space within the slice
is h_2(C_u) ≅ M_2(C)^sa.

**Paper 7 `rem:converse`.** Every M_n(C)^sa admits a faithful self-model (take
V_M = V_B = M_n(C)^sa, phi = id, composite M_n(C)^sa (x) M_n(C)^sa = M_{n^2}(C)^sa). For
complex matrix algebras the minimal and maximal composites COINCIDE (BGW), so clause
(iii) is automatically satisfied. (This already gets most of the way - the open part is
the COHERENT-EMBEDDING step below.)

## Decomposition (suggested attack)

1. **Two-composites distinction (make rigorous, non-circularly).** Clause (iii)'s
   composite is the OBSERVER's body-model V_BM. h_3(O)'s non-composability is about the
   UNIVERSE algebra tensoring with another system (BGW Jordan-monoidal). Prove these are
   different objects: non-composability of h_3(O) does NOT entail non-existence of the
   observer's body-model composite. The whole claim is circular/false if these collapse.
2. **Slice satisfies clause (iii).** Verify h_3(C_u) ≅ M_3(C)^sa satisfies all four
   clauses of Def 1 as a self-modeler in its own right (rem:converse gets you (ii)-(iii);
   check (i), (iv)).
3. **Coherent embedding (the hard part - where an obstruction would live).** The
   observer self-models on the slice A, but A sits inside h_3(O) via E (Peirce
   conditional expectation), NOT a tensor factorization. Show the self-modeling structure
   on A (its V_BM, its sequential product a&b = sqrt(a) b sqrt(a)) is consistent with /
   induced by the ambient h_3(O) Jordan structure under E. I.e., does restricting through
   the bottleneck PRESERVE what clause (iii) needs, or is there an obstruction from the
   non-associative ambient?
4. **Verdict.** A clean RESTRICTION theorem, OR a precisely-characterized obstruction.

## Existing pieces / sources
- Live papers (post-reframe): `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`
  (Def 1, App A), `~/repos/blog/landing/papers/sm-from-self-modeling/sections/complexification.tex`
  (lem:bottleneck, rem:converse, Peirce under E_11).
- BGW = Barnum-Graydon-Wilce 2020 (FRJA composability); Effros-Stormer 1979 (positive
  projections onto JB-subalgebras); Hanche-Olsen universal tensor product.
- Context: `~/repos/blog/research/STATE.md`, `~/repos/blog/research/GRAPH.md`,
  `~/repos/blog/research/phi-inaccessibility-program.md` (Interface gaps section).

## Out of scope
- The anthropic "observer-grade" restriction (conceded conditioning input).
- The forced-vs-selected complexification question (downstream of THIS lemma; parked).
- Consciousness / Phi (separate track).

## Reward-hacking guard (engage v1.2.2's self-checks)
Do NOT "prove" the claim by: redefining clause (iii) to be trivially satisfied;
conflating the two composites of step 1; or asserting the Peirce restriction preserves
clause (iii) without demonstrating it on the actual non-associative h_3(O) structure.
The two-composites distinction must be EARNED. A negative result (clean obstruction) is
a fully acceptable, valuable outcome - do not force a positive.
