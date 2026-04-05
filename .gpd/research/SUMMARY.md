# Research Summary

**Project:** v11.0 Gap C Complexification from Sequential Product
**Domain:** Clifford algebra complexification / Sequential product operator algebras / Jordan-to-C*-algebra lifting
**Researched:** 2026-04-04
**Confidence:** MEDIUM-HIGH (established algebraic ingredients HIGH; novel assembly MEDIUM)

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|---------|------------------|-----------------|
| Cl(9,0) | Real Clifford algebra, signature (9,0) | dimensionless | Positive-definite Euclidean; {gamma_a, gamma_b} = 2 delta_{ab} I_{16} |
| Cl(9,C) | Complex Clifford algebra | dimensionless | Cl(9,0) tensor_R C = M_{16}(C) + M_{16}(C) |
| T_a | Peirce operator (traceless generator) | dimensionless | T_a = (1/2) gamma_a; {T_a, T_b} = (1/2) delta_{ab} I_{16}; eigenvalues +/-1/2 |
| S_9 | Real spinor of Spin(9) | dimensionless | dim_R = 16; real-type (Frobenius-Schur +1); Lawson-Michelsohn convention |
| S_{10}^+ | Positive-chirality Weyl spinor of Spin(10) | dimensionless | dim_C = 16; S_9 tensor_R C = S_{10}^+ + S_{10}^-; Boyle convention |
| V_{1/2} | Peirce half-space of h_3(O) under E_{11} | dimensionless | V_{1/2} = O^2 = R^{16} carrying S_9 |
| V_1 | Peirce 1-eigenspace | dimensionless | V_1 = R * E_{11}; dim = 1 over R |
| a & b | Sequential product | dimensionless | a & b = sqrt(a) b sqrt(a); Gudder-Greechie / van de Wetering / Paper 5 |
| a circ b | Jordan product | dimensionless | a circ b = (1/2)(ab + ba); NOT the same as sequential product |
| psi | Dynamical correspondence | dimensionless | psi: A -> Der(A); Alfsen-Shultz; ab = a circ b - i psi_b(a) |
| J_u | Krasnov complex structure | dimensionless | J_u = left multiplication by unit imaginary octonion u; J_u^2 = -I_{16} |
| omega | Clifford volume element | dimensionless | omega = gamma_1 ... gamma_9; omega^2 = +I; omega = +I on V_{1/2} |
| P_+/- | Spectral projections of T_a | dimensionless | P_+ = (I + 2T_a)/2, P_- = (I - 2T_a)/2; eigenvalue +1/2 and -1/2 resp. |

**Unit system:** Dimensionless (pure algebra). No physical units.
**Metric signature:** N/A (Euclidean Clifford algebra, no spacetime metric involved).
**Fourier convention:** N/A.

**Convention conflicts resolved (2):**
1. Clifford normalization: Peirce operators T_a = (1/2) gamma_a vs. standard generators gamma_a with {gamma_a, gamma_b} = 2 delta I. Resolution: use T_a as primary (matches codebase), convert via gamma_a = 2 T_a when invoking Lawson-Michelsohn results.
2. Sequential product notation: "&" (Paper 5) vs. "circ_s" (van de Wetering) vs. "o" (Gudder-Greechie). Resolution: use "&" throughout, matching Paper 5.

## Executive Summary

Gap C asks whether the observer's complex quantum-mechanical nature can force the real spinor module V_{1/2} = R^{16} to complexify to S_{10}^+ = C^{16}, thereby producing Spin(10) chiral fermion structure. Previous milestones (v6.0, v8.0) proved that NO purely algebraic route internal to h_3(O) can produce this complexification: the Schur commutant End_{Spin(9)}(S_9) = R admits no equivariant complex structure, and the Peirce 1-eigenspace V_1 = R is one-dimensional over R. The sequential product route attacks from outside: the observer IS a C*-algebra M_n(C)^sa (Paper 5), and its sequential product a & b = sqrt(a) b sqrt(a) is C-linear. The question is whether this C-linearity, when applied to the real Clifford generators T_a of the measurement algebra, forces an extension from Cl(9,0) to Cl(9,C).

The central finding of this research survey is that the answer depends critically on whether the observer applies the sequential product to EFFECTS (operators with eigenvalues in [0,1]) or to INDEFINITE operators (the T_a themselves, with eigenvalues +/-1/2). For effects: the shifted projections E_a = (I + 2T_a)/2 have non-negative eigenvalues, so sqrt(E_a) = E_a is real, and the sequential product E_a & E_b = E_a E_b E_a = (1/2) E_a stays entirely within M_{16}(R). No complexification. For indefinite operators: T_a has eigenvalue -1/2, so the principal square root sqrt(-1/2) = i/sqrt(2) is complex; the complex functional calculus gives sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2 sqrt(2)), and the sequential product sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b exits M_{16}(R) into M_{16}(C). This result was verified numerically for all 72 off-diagonal pairs with errors below 5e-16.

The research program therefore reduces to a single well-posed physical question: is the C*-observer justified in applying the complex functional calculus to the indefinite Peirce operators T_a? The standard sequential product (Gudder-Greechie) is defined on effects [0,I], where this question does not arise. Extension to general self-adjoint operators requires invoking the observer's complex Hilbert space structure -- specifically, the holomorphic functional calculus available in any C*-algebra. The recommended approach is: (1) verify the computational results (trivial -- 16x16 matrices), (2) prove that the observer's C-linear functional calculus on indefinite operators is physically mandated by the self-modeling axioms, and (3) show the resulting complex algebra equals M_{16}(C), completing Cl(9,0) -> Cl(9,C) and thus S_9 -> S_{10}^+. An alternative route via the Alfsen-Shultz dynamical correspondence theorem is also viable: if the observer's C-linear measurement maps induce a dynamical correspondence on M_{16}(R)^sa, the lifting to M_{16}(C) follows by theorem.

## Key Findings

### Computational Approaches

All computations involve 16x16 matrices and are trivially cheap (sub-second on any hardware). The existing Python/NumPy stack suffices with no new dependencies. COMPUTATIONAL.md pre-verified the key results:

**Core approach:**

- **Closed-form matrix sqrt:** sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2 sqrt(2)) -- exact, avoids eigendecomposition entirely
- **Sequential product verification:** sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b for all 72 anticommuting pairs -- verified to machine precision
- **C-linear closure check:** 256 Cl(9,0) monomials are R-linearly independent in M_{16}(R), hence C-linearly independent in M_{16}(C), so C-span = M_{16}(C)
- **Effect algebra closure:** E_a & E_b = (1/2) E_a (real) for Clifford spectral projections -- the effect algebra does NOT complexify

### Prior Work Landscape

**Must reproduce (benchmarks):**

- Cl(9,0) = M_{16}(R) + M_{16}(R) and Cl^+(9,0) = M_{16}(R) -- Lawson-Michelsohn Table I.4.3 [HIGH confidence]
- S_9 tensor_R C = S_{10}^+ + S_{10}^- -- standard branching under Spin(9) -> Spin(10) [HIGH confidence]
- Three impossibility theorems (v8.0 Phase 30): no equivariant J, no J in spin(9), Schur commutant = R [HIGH confidence, computationally verified]
- SM gauge group = commutant of J_u in Spin(9) -- Krasnov, J. Math. Phys. 62 (2021) [HIGH confidence]
- Sequential product spaces are Euclidean Jordan algebras -- van de Wetering, J. Math. Phys. 60 (2019) [HIGH confidence]
- Alfsen-Shultz: JB lifts to C* iff dynamical correspondence exists -- PNAS 95:6596 (1998) [HIGH confidence]

**Novel predictions (contributions):**

- sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b: the sequential product of indefinite Peirce operators exits M_{16}(R) [MEDIUM confidence -- algebraically proven, physically conditioned on complex FC justification]
- Observer's C-linear functional calculus induces dynamical correspondence on M_{16}(R)^sa [LOW-MEDIUM confidence -- no published precedent; this is the novel claim]

**Defer (future work):**

- 256x256 H_eff complexification (straightforward once 16x16 result established)
- Spin(10) representation structure on C^16 (representation theory, not computation)
- Matching induced J with Krasnov J_u (requires additional analysis after complexification established)

### Methods and Tools

Six analytical methods and one computational method were surveyed. The analysis converges on a single decision tree: the complexification mechanism depends entirely on whether the observer applies sqrt to effects or to indefinite operators. For effects, the method is trivial (sqrt of projection = projection, everything real). For indefinite operators, the complex functional calculus produces imaginary components that exit M_{16}(R).

**Major components:**

1. **Spectral analysis of T_a** -- eigenvalues +/-1/2, determines that T_a is NOT an effect, so standard Gudder-Greechie does not apply directly
2. **Complex functional calculus** -- principal branch sqrt on spectrum of T_a, the ONLY route that generates complex operators from real inputs
3. **C*-envelope analysis** -- positive real operators have real square roots (closure); indefinite operators require complex square roots (exit)
4. **Alfsen-Shultz dynamical correspondence** -- alternative route: if observer's maps induce psi on M_{16}(R)^sa, lifting to M_{16}(C) follows by theorem
5. **Representation-theoretic decomposition** -- Cl^+(9,0) = M_{16}(R) -> Cl^+(10,0) = M_{16}(C) requires one additional generator; the sequential product may provide it
6. **Grade analysis** -- for effects, sequential product stays real (grade 0+1, all real coefficients); for indefinite operators, imaginary coefficients appear

### Critical Pitfalls

1. **Real closure of effect sequential product (CRITICAL)** -- The standard sequential product on effects stays real. The shifted projections E_a = (I+2T_a)/2 satisfy sqrt(E_a) = E_a (projection), so E_a & E_b = E_a E_b E_a is a product of real matrices. Prevention: do NOT claim complexification from effects; the argument MUST invoke the complex functional calculus on indefinite T_a operators.

2. **C*-algebra generated by real generators stays real (CRITICAL)** -- Embedding gamma_1,...,gamma_9 in B(H) = M_{16}(C) and forming the C*-subalgebra gives M_{16}(R), not M_{16}(C). Products, sums, and adjoints of real matrices are real. Prevention: must identify where a genuinely complex operator is PRODUCED, not just where one COULD live.

3. **GNS obstruction for exceptional Jordan algebra (MODERATE)** -- h_3(O) has no faithful Hilbert space representation (Hanche-Olsen 1983). Arguments routing through "represent h_3(O) on the observer's Hilbert space" fail. Prevention: work with the observer's GNS (for M_n(C)^sa), not h_3(O)'s. The complexity enters through the OBSERVER's representation of V_{1/2}, not h_3(O)'s self-representation.

4. **V_1 = R bottleneck recurrence (MODERATE)** -- V_1 = R * E_{11} is 1-dimensional over R. The observer's C*-nature does not change the dimension of a Peirce eigenspace of h_3(O). Prevention: never assert V_1 = C; the complexity enters from the observer's internal algebra, not from V_1.

5. **Overclaiming "Gap C closed algebraically" (MINOR)** -- If the result relies on the observer's C*-nature, it is "observer-induced complexification," not unconditional algebraic forcing. Prevention: label the result honestly. Phase 30 impossibility theorems are COMPLEMENTED, not circumvented.

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|-------------|-----------------|-------------|-------------|
| Effect sequential product | a in [0,I] (non-negative eigenvalues) | a has negative eigenvalues | Yes (exact for projections) | Complex FC for indefinite operators |
| Complex functional calculus | Any normal operator in C*-algebra | Branch cut ambiguity for non-isolated spectrum | Yes (principal branch; branch-independent for existence of imaginary part) | Effect sequential product for positive operators |
| Alfsen-Shultz dynamical correspondence | Special JB-algebras (not exceptional) | h_3(O) -- the exceptional Jordan algebra does NOT admit a dynamical correspondence | Yes (theorem) | Sequential product route (same target, different mechanism) |
| Direct 16x16 matrix computation | Any 16x16 problem | Never (exact to machine precision) | Yes (exact) | Symbolic verification in SymPy for algebraic proofs |

**Coverage gap:** The justification for applying complex functional calculus to indefinite Peirce operators has no established method. This is the genuinely novel step requiring original argument. Both the "complex FC" and "Alfsen-Shultz" routes reach the same target (M_{16}(R)^sa -> M_{16}(C)) but through different mechanisms.

## Theoretical Connections

### Connection 1: Grgin-Petersen Observable-Generator Duality (ESTABLISHED)
Self-adjoint operators play dual roles as observables (Jordan product) and generators of dynamics (Lie bracket). The full associative product is ab = a circ b - i psi_b(a). The factor of i is NECESSARY for self-adjoint operators to generate unitary transformations. This is the conceptual ancestor of Alfsen-Shultz and explains WHY complexification is tied to dynamics: real observables generate unitary (complex) dynamics only if the algebra is complexified.

### Connection 2: Sequential Product -> Jordan -> C* Chain (ESTABLISHED)
Van de Wetering proves sequential product spaces are Jordan algebras. Alfsen-Shultz proves JB-algebras lift to C*-algebras iff dynamical correspondence exists. Together: sequential product + dynamical correspondence = C*-algebra. The observer's C-linear sequential product (Paper 5) already carries the dynamical correspondence. The question is whether this propagates to M_{16}(R)^sa.

### Connection 3: Krasnov J_u and the 10th Generator (CONJECTURED)
Cl^+(10,0) = M_{16}(C) is generated by Cl^+(9,0) = M_{16}(R) plus one additional generator gamma_{10} anticommuting with all existing generators. In standard constructions, gamma_{10} = i * J_u. The sequential product sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b produces i times a real matrix. This i factor is the signature of the complexification and may be related to the 10th generator. The precise connection (does the sequential product generate J_u or an element in its G_2 orbit?) is an open question.

### Connection 4: Effect Algebra Closure vs. Observable Algebra Extension (ESTABLISHED)
The effect algebra [0,I] in M_{16}(R) is closed under the sequential product (effects have non-negative eigenvalues, real square roots). The OBSERVABLE algebra (all self-adjoint operators, including indefinite ones) is NOT closed under the complex functional calculus -- applying sqrt to T_a with eigenvalue -1/2 exits into M_{16}(C). This is precisely the boundary between "basin-only" (effects, stays real) and "observer-involved" (complex FC on indefinite operators, exits to complex).

## Contradiction Resolution

### Resolved: "Sequential Product Stays Real" vs. "Sequential Product Produces Complex Operators"

**PITFALLS.md (Pitfall 1):** "The sequential product sqrt(T_a) T_b sqrt(T_a) for Peirce operators T_a, T_b with real eigenvalues +/-1/2 remains entirely in the real subalgebra Cl(9,0). [...] Their square roots are also real symmetric (computed by the spectral theorem over R: eigenvalues are +/-1/2, so sqrt(T_a) has eigenvalues +/-1/sqrt(2), all real)."

**COMPUTATIONAL.md:** "sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for anticommuting Clifford generators. This is purely imaginary, meaning the sequential product of real Cl(9,0) generators immediately exits M_{16}(R) into M_{16}(C)."

**Diagnosis:** PITFALLS.md contains an error in its reasoning. It claims sqrt(T_a) has eigenvalues +/-1/sqrt(2), "all real." This is WRONG. The eigenvalues of T_a are +1/2 and -1/2. The square root of +1/2 is 1/sqrt(2) (real). The square root of -1/2 is i/sqrt(2) (imaginary, under the principal branch of the complex square root). PITFALLS.md conflated "eigenvalues are real" with "square roots of eigenvalues are real." The square root function on the REAL line is only defined for non-negative numbers. For negative eigenvalues, sqrt requires the complex extension.

Specifically: PITFALLS.md states "sqrt(T_a) has eigenvalues +/- 1/sqrt(2)" -- this is incorrect. sqrt(+1/2) = 1/sqrt(2) but sqrt(-1/2) = i/sqrt(2), NOT -1/sqrt(2). (-1/sqrt(2))^2 = 1/2, not -1/2. The spectral theorem over R gives sqrt for POSITIVE operators; for indefinite operators, the spectral theorem must be applied in the COMPLEX functional calculus.

**Resolution:** COMPUTATIONAL.md is correct. The sequential product of indefinite Peirce operators exits M_{16}(R) into M_{16}(C). The PITFALLS.md warning is valid ONLY for effects (operators with non-negative eigenvalues), where sqrt is indeed real. The T_a are NOT effects (they have eigenvalue -1/2), so the warning does not apply to them directly. [CONFIDENCE: HIGH for the resolution]

**However**, PITFALLS.md correctly identifies the deeper issue: the STANDARD Gudder-Greechie sequential product is defined on effects [0,I], not on arbitrary self-adjoint operators. Extending it to indefinite operators via the complex functional calculus is a CHOICE that must be physically justified. The resolution of the computational contradiction does not resolve the physical question of whether this extension is mandated.

### Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | Cl(9,0) tensor_R C = Cl(9,C) = M_{16}(C) + M_{16}(C) | PRIOR-WORK.md | web_search: Cl(9,0) classification Bott periodicity | CONFIRMED -- Wikipedia, Lawson-Michelsohn, nLab all agree |
| 2 | JB-algebra lifts to C* iff dynamical correspondence exists | PRIOR-WORK.md | web_search: Alfsen-Shultz dynamical correspondence 1998 | CONFIRMED -- PNAS 95:6596, Theorem 12 |
| 3 | Sequential product spaces are Jordan algebras | PRIOR-WORK.md | web_search: van de Wetering 1803.11139 | CONFIRMED -- J. Math. Phys. 60, 062201 (2019) |
| 4 | SM gauge group = commutant of J_u in Spin(9) | PRIOR-WORK.md | web_search: Krasnov SO(9) Standard Model | CONFIRMED -- J. Math. Phys. 62, 021703 (2021) |
| 5 | sqrt of operator with negative eigenvalues requires complex extension | METHODS.md, COMPUTATIONAL.md | web_search: matrix square root negative eigenvalues complex functional calculus | CONFIRMED -- standard result; holomorphic FC on spectrum |
| 6 | h_3(O) has no faithful B(H) representation | PITFALLS.md | Hanche-Olsen (1983); standard result in Jordan algebra theory | CONFIRMED by literature consensus |
| 7 | Effect sequential product stays real | METHODS.md, PITFALLS.md | Algebraic: sqrt(projection) = projection; product of real matrices = real | CONFIRMED by explicit computation |

## Cross-Validation Matrix

|                    | Complex FC route | Alfsen-Shultz route | Direct computation | Effect closure |
|--------------------|:---:|:---:|:---:|:---:|
| Complex FC route   | --- | Both predict M_{16}(C) as target | 72-pair numerical verification | Effects stay real (consistency check) |
| Alfsen-Shultz route| Same target algebra | --- | Can verify psi_a(b) = i[a,b] numerically | N/A (different mechanism) |
| Direct computation | Verifies (i/2) T_b identity | Can verify psi_a(b) = i[a,b] numerically | --- | Verifies E_a & E_b = (1/2) E_a |
| Effect closure     | Confirms effects don't complexify | N/A | Real-valued check | --- |

**High-risk:** The Alfsen-Shultz route has no direct cross-validation with the effect closure route (they operate on different domains). The complex FC route and Alfsen-Shultz route cross-validate on the TARGET but not on the MECHANISM.

## Implications for Research Plan

Based on the analysis, the research naturally phases into: a computational verification gate, a theoretical proof phase, and a synthesis phase.

### Phase 1: "Computational Verification of Sequential Product Complexification"

**Rationale:** The core computational result (sqrt(T_a) T_b sqrt(T_a) = (i/2) T_b) was pre-verified during research but must be reproduced in the project codebase with full test coverage. This is a GO/NO-GO gate: if the computation fails, the entire route is dead.
**Delivers:** Verified numerical evidence that the complex FC on indefinite Peirce operators produces purely imaginary sequential products. Effect algebra closure (stays real) as contrast.
**Validates:** All 72 off-diagonal pairs produce (i/2) T_b; all 9 diagonal pairs produce (1/4) I; all effect products stay real.
**Avoids:** Pitfall 1 (real closure) -- by explicitly demonstrating the exit from M_{16}(R) for indefinite operators while confirming real closure for effects.
**Methods:** Closed-form sqrt, direct matrix multiplication, imaginary norm check.
**Cost:** Sub-second. Trivial.

### Phase 2: "Theoretical Proof of Observer-Induced Complexification"

**Rationale:** The computational result (Phase 1) shows THAT complexification occurs under the complex FC. This phase proves WHY the observer is justified in applying the complex FC to indefinite Peirce operators, rather than restricting to effects.
**Delivers:** A theorem: "The C*-observer's measurement of indefinite Peirce operators via the complex functional calculus extends the measurement algebra from Cl(9,0) to Cl(9,C), complexifying V_{1/2} to S_{10}^+."
**Uses:** Alfsen-Shultz dynamical correspondence, Grgin-Petersen observable-generator duality, van de Wetering sequential product classification, Paper 5 self-modeling axioms.
**Builds on:** Phase 1 computational evidence.
**Avoids:** Pitfall 2 (algebra vs module confusion), Pitfall 3 (GNS for h_3(O)), Pitfall 4 (V_1 = R bottleneck), Pitfall 7 (existence != access).
**Risk:** HIGH -- this is genuinely novel mathematics. The key step (C-linear maps inducing dynamical correspondence on M_{16}(R)^sa) has no published precedent.

### Phase 3: "Gap C Closure Statement and Paper Integration"

**Rationale:** Combine Phase 1 evidence and Phase 2 proof into a single Gap C closure theorem. Connect to Krasnov J_u, verify SM gauge group emergence, and integrate into Paper 7 derivation chain.
**Delivers:** Gap C closure theorem; updated Paper 7 with complexification proof; connection to Krasnov J_u family.
**Builds on:** Phase 2 proof.
**Avoids:** Pitfall 9 (overclaiming) -- label result as "observer-induced complexification."

### Phase Ordering Rationale

- Phase 1 before Phase 2: computation provides the ground truth that guides the theoretical proof. If computation shows no complexification (unexpected based on pre-verification), the theoretical work is moot.
- Phase 2 before Phase 3: the paper integration requires a complete proof, not just computational evidence.
- The alternative Alfsen-Shultz route can be pursued in parallel with the complex FC route in Phase 2; they provide independent paths to the same conclusion.

### Phases Requiring Deep Investigation

- **Phase 2:** Genuinely novel mathematics. The justification for extending the sequential product from effects to indefinite operators via the complex functional calculus has no published precedent. The connection between CPTP measurement maps and Jordan derivations (required for Alfsen-Shultz) is nontrivial.

Phases with established methodology:

- **Phase 1:** Standard 16x16 matrix algebra. All algorithms are textbook. Pre-verified during research.
- **Phase 3:** Paper writing and integration. The algebraic chain Cl(9,0) -> Cl(9,C) -> S_{10}^+ is textbook representation theory once the complexification mechanism is established.

## Input Quality -> Roadmap Impact

| Input File | Quality | Affected Recommendations | Impact if Wrong |
|------------|---------|------------------------|-----------------|
| METHODS.md | Good | Method selection, decision tree, phase ordering | Phase 2 may need different approach |
| PRIOR-WORK.md | Good | Benchmark values, theorem inventory, dependency chain | Phases may build on incorrect premises |
| COMPUTATIONAL.md | Good | Phase 1 verification targets, algorithm choices | Negligible (all algorithms are standard) |
| PITFALLS.md | Good (with one error in Pitfall 1 reasoning) | Risk mitigation, GO/NO-GO criteria | Pitfall 1 reasoning error identified and resolved; remaining pitfalls solid |

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Computational Approaches | HIGH | 16x16 matrices, exact algorithms, pre-verified results |
| Prior Work | HIGH | Textbook results (Lawson-Michelsohn, Alfsen-Shultz, van de Wetering, Krasnov) all independently verified |
| Methods | MEDIUM-HIGH | The methods are individually well-established; the novel combination (complex FC on indefinite Peirce operators) is sound but unprecedented |
| Pitfalls | HIGH | Comprehensive coverage; one reasoning error (Pitfall 1: sqrt of negative eigenvalue) identified and corrected; remaining pitfalls are accurate and well-documented |

**Overall confidence:** MEDIUM-HIGH. The algebraic ingredients are all established theorems. The novel step (justifying complex FC on indefinite operators) is well-posed and has clear success criteria but constitutes genuinely new mathematics.

### Gaps to Address

- **Physical justification for complex FC on indefinite operators:** The standard sequential product is defined on effects. Extension to general self-adjoint operators is a modeling choice, not a theorem. Must be derived from the self-modeling axioms or the observer's C*-structure.
- **Connection between CPTP maps and Jordan derivations:** The Alfsen-Shultz route requires showing that the observer's measurement maps (positive linear maps / CPTP channels) induce DERIVATIONS of M_{16}(R)^sa. CPTP maps are positive maps, not derivations; the gap must be bridged.
- **Krasnov J_u identification:** Does the complex structure induced by the observer match Krasnov's J_u (or lie in its G_2 orbit)? This determines whether the SM gauge group emerges.

## Open Questions

1. **(HIGH priority, blocks Phase 2)** Is the C*-observer's complex functional calculus on indefinite Peirce operators physically mandated by the self-modeling axioms, or is it a modeling choice? If modeling choice, what selects it over the effect-restricted sequential product?

2. **(HIGH priority, blocks Phase 2)** Does the observer's C-linear action on V_{1/2} induce a dynamical correspondence on M_{16}(R)^sa in the sense of Alfsen-Shultz? Specifically, do the observer's measurement maps produce the commutator structure psi_a(b) = i[a,b] on the measurement algebra?

3. **(MEDIUM priority, blocks Phase 3)** Does the induced complex structure on V_{1/2}^C match Krasnov's J_u (up to G_2 conjugation)? This determines whether the SM gauge group [SU(3) x SU(2) x U(1)]/Z_6 emerges automatically.

4. **(LOW priority)** Is the branch choice (principal branch: sqrt(-1) = +i vs. -i) physically determined, or are both branches equally valid? The EXISTENCE of complexification is branch-independent, but the SIGN of J matters for chirality.

## Sources

### Primary (HIGH)

- Lawson, Michelsohn, *Spin Geometry* (1989) -- Clifford algebra classification, Bott periodicity, complexification, spinor representations
- [Alfsen, Shultz, "Orientation in operator algebras," PNAS 95:6596 (1998)](https://www.pnas.org/doi/10.1073/pnas.95.12.6596) -- Dynamical correspondence theorem
- Alfsen, Shultz, *Geometry of State Spaces of Operator Algebras* (2003) -- Complete JB/C*-algebra correspondence
- [van de Wetering, "Sequential Product Spaces are Jordan Algebras," J. Math. Phys. 60:062201 (2019)](https://arxiv.org/abs/1803.11139)
- Gudder, Greechie, "Sequential products on effect algebras," Rep. Math. Phys. 49 (2002) 87-111
- [Krasnov, "SO(9) characterization of the standard model gauge group," J. Math. Phys. 62:021703 (2021)](https://arxiv.org/abs/1912.11282)
- Grgin, Petersen, "Duality of observables and generators," J. Math. Phys. 15:764 (1974)
- [Baez, "The Octonions," Bull. AMS 39 (2002) 145-205](https://arxiv.org/abs/math/0105155)
- Phase 29-30 derivations (this project): Peirce operators, Clifford generators, impossibility theorems

### Secondary (MEDIUM)

- [van de Wetering, "Three characterisations of the sequential product"](https://arxiv.org/abs/1803.08453)
- [Gudder, Latremoliere, "The three types of normal sequential effect algebras," Quantum 4:378 (2020)](https://arxiv.org/abs/2004.12749)
- Hanche-Olsen, "On the structure and tensor products of JC-algebras," Can. J. Math. 35 (1983) 1059-1074
- [Conrad, "Complexification"](https://kconrad.math.uconn.edu/blurbs/linmultialg/complexification.pdf)
- [Li, Ruan, "Structure and applications of real C*-algebras"](https://arxiv.org/abs/1505.04091)

### Tertiary (LOW)

- Singh (2025), arXiv:2508.10131 -- Fermion mass ratios from complexified EJA (confirms target but not mechanism)
- Farnsworth (2025), arXiv:2503.10744 -- Exceptional Jordan geometries via NCG (independent route)
- [Marsault, Schoeffel (2025/2026), "Complex Lies, Real Physics"](https://arxiv.org/abs/2509.20929) -- recent preprint

---

_Research analysis completed: 2026-04-04_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "v11.0 Gap C Complexification from Sequential Product"
  synthesis_date: "2026-04-04"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "dimensionless"
  metric_signature: "N/A"
  fourier_convention: "N/A"
  coupling_convention: "N/A"
  renormalization_scheme: "N/A"
  clifford_convention: "{gamma_a, gamma_b} = 2 delta_{ab} I_16; T_a = (1/2) gamma_a"
  sequential_product_convention: "a & b = sqrt(a) b sqrt(a)"

methods_ranked:
  - name: "Complex functional calculus on indefinite Peirce operators"
    regime: "T_a with eigenvalues +/-1/2 (indefinite operators)"
    confidence: MEDIUM
    cost: "O(16^3) per operation -- trivial"
    complements: "Alfsen-Shultz dynamical correspondence (same target, different mechanism)"
  - name: "Alfsen-Shultz dynamical correspondence"
    regime: "Special JB-algebras (M_16(R)^sa)"
    confidence: MEDIUM
    cost: "Theoretical proof -- no computation"
    complements: "Complex functional calculus (same target, different mechanism)"
  - name: "Direct 16x16 matrix computation"
    regime: "All 16x16 problems"
    confidence: HIGH
    cost: "O(16^3) -- sub-millisecond"
    complements: "Symbolic verification in SymPy"
  - name: "Effect algebra sequential product"
    regime: "Operators with eigenvalues in [0,1]"
    confidence: HIGH
    cost: "O(16^3) -- sub-millisecond"
    complements: "Complex FC for indefinite operators"

phase_suggestions:
  - name: "Computational Verification"
    goal: "Verify that complex FC on indefinite Peirce operators produces (i/2)*T_b; verify effect closure stays real"
    methods: ["Direct 16x16 matrix computation", "Effect algebra sequential product"]
    depends_on: []
    needs_research: false
    risk: LOW
    pitfalls: ["pitfall-1-real-closure"]
  - name: "Theoretical Proof"
    goal: "Prove observer's C-linear FC on indefinite operators is physically mandated; prove measurement algebra extends to Cl(9,C)"
    methods: ["Complex functional calculus on indefinite Peirce operators", "Alfsen-Shultz dynamical correspondence"]
    depends_on: ["Computational Verification"]
    needs_research: true
    risk: HIGH
    pitfalls: ["pitfall-2-algebra-vs-module", "pitfall-3-gns-exceptional", "pitfall-4-v1-bottleneck", "pitfall-7-existence-not-access"]
  - name: "Gap C Closure and Paper Integration"
    goal: "State Gap C closure theorem; connect to Krasnov J_u; integrate into Paper 7"
    methods: ["Complex functional calculus on indefinite Peirce operators"]
    depends_on: ["Theoretical Proof"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["pitfall-9-overclaiming"]

critical_benchmarks:
  - quantity: "Sequential product of anticommuting Peirce operators"
    value: "sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for a != b"
    source: "COMPUTATIONAL.md (pre-verified); algebraic derivation from anticommutativity"
    confidence: HIGH
  - quantity: "Sequential product self-product"
    value: "sqrt(T_a) T_a sqrt(T_a) = (1/4)*I"
    source: "COMPUTATIONAL.md (pre-verified)"
    confidence: HIGH
  - quantity: "Effect sequential product"
    value: "E_a & E_b = (1/2)*E_a for spectral projections (real)"
    source: "METHODS.md explicit computation; COMPUTATIONAL.md verification"
    confidence: HIGH
  - quantity: "C-linear closure dimension"
    value: "256 Cl(9,0) monomials C-span M_16(C)"
    source: "COMPUTATIONAL.md; standard linear algebra"
    confidence: HIGH

open_questions:
  - question: "Is the C*-observer's complex functional calculus on indefinite Peirce operators physically mandated by self-modeling axioms?"
    priority: HIGH
    blocks_phase: "Theoretical Proof"
  - question: "Does the observer's C-linear action induce a dynamical correspondence on M_16(R)^sa?"
    priority: HIGH
    blocks_phase: "Theoretical Proof"
  - question: "Does the induced complex structure match Krasnov's J_u up to G_2 conjugation?"
    priority: MEDIUM
    blocks_phase: "Gap C Closure and Paper Integration"
  - question: "Is the branch choice (sqrt(-1) = +i vs -i) physically determined?"
    priority: LOW
    blocks_phase: "none"

contradictions_unresolved: []
```
