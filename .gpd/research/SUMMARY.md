# Research Summary

**Project:** v13.0 Paper 6 Closure -- G4 + N=2 from Algebraic Structure
**Domain:** Exceptional Jordan algebras / Kantor-Koecher-Tits construction / Very special real geometry / GST classification
**Researched:** 2026-04-12
**Confidence:** HIGH for algebraic foundations; MEDIUM-HIGH for the "N=2 as consequence" assembly; MEDIUM for G5 (compact so(3) vs so(3,1)) resolution

## Unified Notation

| Symbol | Quantity | Units/Dimensions | Convention Notes |
|--------|----------|------------------|------------------|
| h_3(O) | Exceptional (Albert) Jordan algebra | dim 27, dimensionless | 3x3 hermitian octonionic matrices |
| h_2(C_u) | Projected Peirce complement | dim 4, dimensionless | pi_u(V_0); isomorphic to R^{3,1} as spin factor JSpin(3,1) |
| h_2(O) | Full Peirce complement V_0 | dim 10, dimensionless | JSpin(9); carries R^{9,1} Minkowski via det_2 |
| V_1, V_{1/2}, V_0 | Peirce spaces at E_{11} | dim 1, 16, 10 | 27 = 1 + 16 + 10 decomposition |
| det_2(Y) | Quadratic norm on h_2(C_u) | dimensionless | Gives Minkowski metric diag(+1,-1,-1,-1) |
| det_3(X) / N(X) | Cubic norm on h_3(O) | dimensionless | Unique F_4-invariant cubic form (Springer 1962) |
| d_{IJK} | Polarized cubic form coefficients | symmetric 3-tensor | det_3(X) = (1/6) d_{IJK} X^I X^J X^K; Phase 47: 106 nonzero |
| C_{IJK} | GST cubic tensor | symmetric 3-tensor | C_{IJK} = d_{IJK}/6; determines bosonic Lagrangian |
| V(h) | Very special real prepotential | dimensionless | V(h) = C_{IJK} h^I h^J h^K; constraint surface V=1 |
| a_{IJ} | VSR scalar metric | dimensionless | a_{IJ} = -(1/2) d_I d_J ln V at V=1 |
| pi_u | Projection h_2(O) -> h_2(C_u) | linear map | Keeps C_u = span{1,u} component |
| u | Observer's complex structure | u in S^6 subset Im(O) | Default: u = e_7 (Fano convention) |
| F_4 | Aut(h_3(O)) | dim 52 | Preserves Jordan product, Tr, and det |
| E_{6(-26)} | Str(h_3(O)) | dim 78 | Structure group; preserves det up to scale. ALWAYS specify real form |
| TKK(J) / KKT(J) | Tits-Kantor-Koecher Lie algebra | 3-graded Lie algebra | g = J + Str_0(J) + J |
| Str_0(J) | Reduced structure algebra | subalgebra of TKK | For h_2(C): so(3,1) + R (Lorentz + dilatation), dim 7 |
| Der(J) | Derivation algebra | subalgebra of Str_0 | For h_2(C): so(3), dim 3 (spatial rotations only) |
| OD1-OD7 | Operational spacetime criteria | -- | Dimension, signature, causal, conformal, homogeneity, isotropy, reduction |
| F(X) | 4d prepotential | dimensionless | F(X) = d_{IJK} X^I X^J X^K / (6 X^0); degree 2 in X^I |

**Metric signature:** (+,-,-,-) (mostly minus). det_2 on h_2(C_u) gives Gram = diag(+1,-1,-1,-1).

**Unit system:** Natural units (hbar = c = 1) for Lagrangian; dimensionless for pure algebra.

**Octonion basis:** Fano convention with e_1 e_2 = e_4, complex structure u = e_7.

**Key convention reconciliation:** The 5d prepotential V(h) = C_{IJK} h^I h^J h^K is degree 3 and homogeneous. The 4d prepotential F(X) = d_{IJK} X^I X^J X^K / (6 X^0) is degree 2 (projective). These are related by the c-map (circle reduction); C_{IJK} = d_{IJK}/6 with our Phase 49 normalization. All four research files use consistent conventions on this point.

## Executive Summary

The v13.0 milestone closes two chain-critical gaps in the algebraic derivation of Einstein gravity from h_3(O): (G4) V_0 = spacetime as a derived result rather than an identification, and (G2) N=2 SUSY as a consequence rather than an assumption. Both closures rest on well-established mathematics applied in a novel combination. For G4, the Kantor-Koecher-Tits construction (Tits 1962, Koecher 1967, Gunaydin 1993) applied to h_2(C_u) yields so(4,2) -- the full conformal algebra of 3+1 Minkowski spacetime -- deriving not just the metric (already established in Phase 46) but the complete operational spacetime structure including translations, Lorentz transformations, dilatation, and special conformal transformations. F_4 transitivity on rank-1 idempotents (Freudenthal 1954) guarantees observer independence. For G2, the GST classification theorem (1984) combined with Springer's uniqueness theorem (1962) and de Wit-Van Proeyen's very special real geometry (1992) shows that the bosonic Lagrangian is uniquely determined by C_{IJK} + E_{6(-26)} covariance + two-derivative restriction, without assuming supersymmetry. The resulting Lagrangian happens to coincide with the GST N=2 MESGT bosonic sector; SUSY is a mathematical consequence, not an input.

The principal risk is circularity in the N=2 derivation (pitfall C5): the argument must construct the Lagrangian from E_{6(-26)} invariance and the cubic form alone, then identify the result with GST, not start from "In N=2 MESGT..." The recommended approach splits cleanly into two phases: Phase 52 (G4 spacetime via OD1-OD7 + KKT + F_4) and Phase 53 (G2 SUSY via VSR metric + E_{6(-26)} invariant term enumeration). All computations are exact finite-dimensional algebra on spaces dim <= 27 with ~70% of infrastructure already implemented, total runtime under 15 seconds. The KKT construction additionally resolves gap G5 (compact so(3) vs non-compact so(3,1)): Der(h_2(C)) = so(3) gives only rotations, but Str_0(h_2(C)) = so(3,1) + R provides the full Lorentz algebra including boosts. The boosts live in the structure algebra, not the automorphism group -- a conceptually important distinction that Spin(9) compactness obscured.

The recommended phase structure is two phases (52 and 53) that are largely independent computationally but logically ordered: G4 closure establishes that V_0 IS spacetime (prerequisite for the Lagrangian to have physical meaning), then G2 closure establishes the Lagrangian is unique and N=2 supersymmetric. Both phases build on validated v12.0 infrastructure (Phases 46-50) and require no new software dependencies.

## Key Findings

### Computational Approaches

All five algorithms operate on exact finite-dimensional algebra (dim <= 27). No numerical approximation, no convergence issues, no Monte Carlo. Total estimated runtime: < 15 seconds on a single-core laptop. No new Python dependencies beyond NumPy. SymPy optional for exact rational cross-checks.

**Core approach:**

- **KKT(h_2(C_u)) = so(4,2):** Derives full conformal algebra from Jordan algebra axioms -- the strongest form of "V_0 is spacetime" [HIGH confidence, textbook result applied to Peirce output]
- **E_{6(-26)} invariant Lagrangian uniqueness:** Proves bosonic Lagrangian uniquely determined without SUSY input -- closes G2 [MEDIUM-HIGH confidence, novel assembly of established results]
- **VSR metric a_{IJ}:** Computes scalar field metric from d_{IJK}, verifies positive definiteness on E_{6(-26)}/F_4 -- confirms ghost-free kinetic terms [HIGH confidence, standard formula]
- **F_4 observer independence:** Proves all idempotent choices give isomorphic spacetime structure [HIGH confidence, classical theorem]

### Prior Work Landscape

**Must reproduce (benchmarks):**

- TKK(h_2(C)) = su(2,2) = so(4,2), dim = 15 (Koecher 1967, Gunaydin 1993) [HIGH confidence]
- F_4/Spin(9) = OP^2, dim = 16 (Freudenthal 1954) [HIGH confidence]
- GST bosonic Lagrangian L_bos from C_{IJK} = d_{IJK}/6 matches Phase 49 Eq. 49.6 [HIGH confidence]
- Scalar manifold E_{6(-26)}/F_4, dim = 26 in 5d; E_{7(-25)}/(E_6 x U(1)), dim = 54 in 4d [HIGH confidence]
- VSR metric a_{IJ} positive definite on N=1 constraint surface (26 positive eigenvalues) [HIGH confidence]

**Novel predictions (contributions):**

- The full spacetime structure (conformal algebra, causal structure, Lorentz boosts) derived from Peirce V_0 via KKT, not assumed
- N=2 SUSY is a consequence of h_3(O) algebraic structure via cubic form uniqueness + E_{6(-26)} covariance, not an input
- Gap G5 (compact so(3) -> non-compact so(3,1)) resolved: boosts emerge from Str_0, not Der or Aut
- Lambda = 0 forced by E_{6(-26)} invariance on E_{6(-26)}/F_4 (no non-trivial invariant scalar potential)

**Defer (future work):**

- Fermionic sector completion (predicted by N=2, not derived from algebra)
- Gauged MESGT and nonzero cosmological constant (requires gauge coupling g as additional input)
- 3-generation structure and so(6) -> G_SM reduction (gaps G6, G7)

### Methods and Tools

Five analytical methods cover the full closure. Methods 1-3 address G4 (spacetime): operational axiomatics OD1-OD7 formalize what "being spacetime" means in Jordan-algebraic terms, the KKT construction derives so(4,2) from h_2(C_u), and F_4 orbit theory ensures observer independence. Methods 4-5 address G2 (SUSY): the VSR metric a_{IJ} from the cubic norm establishes the scalar manifold geometry, and E_{6(-26)}-invariant term enumeration proves the two-derivative Lagrangian is unique. All computations extend the existing octonion_algebra.py codebase (4258 lines, ~70% of needed primitives already implemented).

**Major components:**

1. **OD1-OD4 verification** -- Consolidates Peirce structure checks (faithfulness rank=10, multiplication rules, Jordan identity). Runtime < 0.5 sec.
2. **KKT bracket computation** -- 15 generators of so(4,2), 105 commutation relations, Killing form signature (6,9). Runtime < 0.1 sec.
3. **VSR metric a_{IJ}** -- Constrained Hessian of log(det) on N=1, 26 positive eigenvalues. Runtime < 0.5 sec.
4. **E_{6(-26)} invariant enumeration** -- 78 generators, Schur's lemma on irreducible 26 of F_4. Runtime < 10 sec.
5. **Observer independence** -- E_{22} Peirce decomposition, isomorphism via permutation. Runtime < 1 sec.

### Critical Pitfalls

1. **C1 (CRITICAL): Fisher-Rao trap** -- Fisher information metric is positive-definite; it CANNOT give Minkowski signature. The spacetime metric is det_2 (algebraic), not Fisher-Rao (statistical). Prevention: never derive spacetime metric from information geometry.

2. **C5 (CRITICAL): N=2 SUSY circularity** -- If the Lagrangian derivation starts with "In N=2 MESGT...", SUSY is an input. Prevention: construct the Lagrangian from E_{6(-26)} + cubic form + two-derivative restriction, then identify the result with GST.

3. **C4 (CRITICAL): Compact so(3) vs non-compact so(3,1)** -- Spin(9) is compact, Lorentz group is not. Resolution via KKT: Str_0(h_2(C)) = so(3,1) + R contains the full Lorentz algebra; boosts are L_a operators, not derivations.

4. **C6 (HIGH): Relative coefficient fixing** -- The ratio between -R/2 and matter kinetic terms requires E_{6(-26)} covariance on the symmetric space (Schur's lemma on irreducible F_4 isotropy representation).

5. **C7 (MODERATE): Wrong real form** -- Always write E_7(-25) for octonionic magic, NOT E_7(7). Check maximal compact subgroup.

## Approximation Landscape

| Method | Valid Regime | Breaks Down When | Controlled? | Complements |
|--------|-------------|-----------------|-------------|-------------|
| KKT construction | All simple Jordan algebras | N/A (exact algebraic) | Yes -- exact | Direct metric computation (weaker) |
| VSR geometry from cubic | Euclidean degree-3 Jordan algebras with V=1 | Non-Euclidean J, boundary of moduli | Yes -- closed-form | Direct sigma model on coset |
| E_{6(-26)} invariant enumeration | Two-derivative, symmetric scalar manifold | Higher-derivative terms | Yes -- rep theory | Noether procedure (more involved) |
| Weinberg spin-2 theorem | Low energy, massless spin-2 | Finite-energy corrections | Yes -- E/M_Pl | Lattice route (v9.0-v10.0) |
| F_4 orbit theory | h_3(O) automorphisms | N/A (exact) | Yes -- exact | Explicit numerical verification |

**Coverage gap:** No reliable method for quantum corrections to ungauged MESGT. Acceptable: v13.0 is tree-level algebraic closure.

## Theoretical Connections

### Structural Parallels

1. **KKT as universal conformal construction** [ESTABLISHED]: TKK(h_2(K)) = so(dim(K)+2, 2) for all division algebras K. The 4d spacetime so(4,2) is one entry in a complete table parametrized by K = R, C, H, O.

2. **Cubic form determines everything** [ESTABLISHED]: Springer uniqueness -> GST classification -> de Wit-Van Proeyen VSR geometry. The cubic norm det_3 is the single algebraic datum from which spacetime metric, matter couplings, and (claimed) SUSY all follow.

3. **Der -> Str_0 -> KKT hierarchy** [ESTABLISHED]: For h_2(C): so(3) -> so(3,1)+R -> so(4,2). Each step adds physical generators: rotations -> boosts+dilatation -> special conformal. Resolves G5.

### Cross-Validation Matrix

|  | VSR Metric | KKT Algebra | Phase 49 Lagrangian | F_4 Orbit |
|---|:---:|:---:|:---:|:---:|
| **KKT Algebra** | Conformal group of metric | -- | Conformal invariance | F_4 conjugates KKT |
| **VSR Metric** | -- | Metric in Str_0 | a_{IJ} matches kinetic terms | F_4-invariant |
| **d_{IJK}** | a_{IJ} from d_{IJK} | Cubic defines KKT product | Lagrangian coefficients | Unique F_4-invariant |

### Critical Claim Verification

| # | Claim | Source | Verification | Result |
|---|-------|--------|--------------|--------|
| 1 | TKK(h_2(C)) = so(4,2) | PRIOR-WORK.md | Wikipedia, nLab, Gunaydin (2001) | CONFIRMED |
| 2 | GST: cubic Jordan -> N=2 MESGT unique | PRIOR-WORK.md | nLab, multiple JHEP refs | CONFIRMED |
| 3 | F_4 transitive on rank-1 idempotents | PRIOR-WORK.md | Springer-Veldkamp (2000), McCrimmon (2004) | CONFIRMED |
| 4 | det(X) unique F_4-invariant cubic | METHODS.md | Springer-Veldkamp textbook | CONFIRMED |
| 5 | E_{6(-26)}/F_4 rank-2 symmetric, dim 26 | PRIOR-WORK.md | Cartan classification | CONFIRMED |
| 6 | F_4 acts irreducibly on 26-dim tangent | METHODS.md | Slansky (1981) tables | CONFIRMED |
| 7 | C_{IJK} determines bosonic Lagrangian in MESGT | PRIOR-WORK.md | de Wit-Van Proeyen (1992) | CONFIRMED |

## Implications for Research Plan

Based on analysis, suggested phase structure:

### Phase 52: G4 Spacetime Derivation -- V_0 IS Spacetime

**Rationale:** Must establish that V_0 = h_2(C_u) is spacetime before the Lagrangian on this spacetime has physical meaning. All prior phases assumed this; Phase 52 derives it.
**Delivers:** OD1-OD7 verified, KKT(h_2(C_u)) = so(4,2) with 15 generators, F_4 observer independence, G5 resolved via Str_0 boost identification.
**Validates:** dim(KKT) = 15, Killing form signature (6,9), all 105 brackets match so(4,2), boost generators in Str_0 not Der.
**Avoids:** C1 (Fisher-Rao trap), C3 (u-dependence), C4 (compact/non-compact), C7 (wrong real form).

### Phase 53: G2 N=2 SUSY as Consequence -- Lagrangian Uniqueness

**Rationale:** With spacetime established, show the matter-gravity Lagrangian is uniquely determined by algebraic data, and the unique result is N=2 supersymmetric.
**Delivers:** VSR metric a_{IJ} positive-definite (26 eigenvalues), E_{6(-26)}-invariant 2-derivative terms = exactly 4, coefficients match Phase 49, Lambda=0 as consequence.
**Uses:** VSR metric formula (Method 4), E_{6(-26)} invariant enumeration (Method 5).
**Builds on:** Phase 47 (d_{IJK}), Phase 49 (Lagrangian), Phase 52 (spacetime).

### Phase Ordering Rationale

- Phase 52 before 53: spacetime must be established before writing a Lagrangian on it
- Algorithms 1-4 parallelize within phases; Algorithm 5 depends on Algorithm 4
- Both phases are short (~1-2 plans each) due to ~70% infrastructure coverage
- No deep investigation needed: all methods are established constructions applied to computed data

### Phases Requiring Deep Investigation

Phases likely needing additional theoretical or computational exploration:

- **Phase 53 (C5 avoidance):** The circularity avoidance requires careful logical ordering. Not a research gap but a proof-structure challenge.

Phases with established methodology (straightforward execution):

- **Phase 52:** KKT construction is a textbook computation. OD criteria are direct verifications of known Jordan algebra properties. F_4 orbit theory is a 70-year-old result.

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Computational Approaches | HIGH | All exact finite-dim algebra; 70% codebase coverage; < 15 sec total |
| Prior Work | HIGH | All core results established mathematics (1954-2001); multiple sources |
| Methods | HIGH (G4), MEDIUM-HIGH (G2) | KKT textbook; E_{6(-26)} enumeration is novel assembly |
| Pitfalls | HIGH | 12 pitfalls identified; C5 and C4 critical, both have resolutions |

**Overall confidence:** MEDIUM-HIGH

### Gaps to Address

- **G5 resolution depth:** Explicit boost generator identification in Str_0 needs numerical verification in Phase 52.
- **E_{6(-26)} coset generators:** 26 coset generators must be constructed explicitly for invariant enumeration.
- **Fermion sector:** Bosonic Lagrangian derived; fermionic completion predicted by N=2 but not independently derived. Honest limitation, not a v13.0 gap.
- **Lambda=0 interpretation:** Consequence of ungauged theory, not a prediction. Must state clearly.

## Sources

### Primary (HIGH)

- Tits (1962), Kantor (1964), Koecher (1967) -- TKK construction
- Freudenthal (1954) -- F_4 transitivity on OP^2
- Springer (1962), Springer-Veldkamp (2000) -- Cubic form uniqueness, exceptional groups
- Gunaydin-Sierra-Townsend (1983, 1984) -- Magic supergravity, GST classification
- de Wit-Van Proeyen (1992) -- Very special real geometry, c-map
- McCrimmon (2004) -- Jordan algebra structure theory
- Baez (2002) -- Division algebra spacetimes
- Gunaydin (1993) -- Generalized conformal groups from Jordan algebras

### Secondary (MEDIUM)

- Lauria-Van Proeyen, arXiv:2004.11433 -- N=2 SUGRA modern conventions
- Faraut-Koranyi (1994) -- Symmetric cones
- Gunaydin-Koepsell-Nicolai (2001) -- Conformal realizations of exceptional groups
- Todorov-Drenska, arXiv:1805.06739 -- F_4 in particle physics
- Slansky (1981) -- Group theory branching rules
- Yokota (2009) -- Exceptional Lie group real forms

### Tertiary (LOW)

- Kamenshchik-Marrani-Muscolino (2026) -- Carroll symmetry and Jordan algebras (tangential)

---

_Research synthesis completed: 2026-04-12_
_Ready for research plan: yes_

```yaml
# --- ROADMAP INPUT (machine-readable, consumed by gpd-roadmapper) ---
synthesis_meta:
  project_title: "v13.0 Paper 6 Closure -- G4 + N=2 from Algebraic Structure"
  synthesis_date: "2026-04-12"
  input_files: [METHODS.md, PRIOR-WORK.md, COMPUTATIONAL.md, PITFALLS.md]
  input_quality: {METHODS: good, PRIOR-WORK: good, COMPUTATIONAL: good, PITFALLS: good}

conventions:
  unit_system: "natural"
  metric_signature: "mostly_minus"
  fourier_convention: "physics"
  coupling_convention: "alpha = g^2/(4pi), C_IJK = d_IJK/6"
  renormalization_scheme: "N/A"

methods_ranked:
  - name: "KKT construction on h_2(C_u)"
    regime: "All simple Jordan algebras (exact)"
    confidence: HIGH
    cost: "O(15^3) ~ O(3375) for bracket verification"
    complements: "Direct metric identification (weaker but faster)"
  - name: "E_{6(-26)} invariant Lagrangian enumeration"
    regime: "Two-derivative, symmetric scalar manifold E_{6(-26)}/F_4"
    confidence: MEDIUM
    cost: "O(78 * 27^2) ~ O(57000) for Lie derivative checks"
    complements: "GST SUSY construction (assumes what we derive)"
  - name: "VSR metric a_{IJ} from cubic norm"
    regime: "Euclidean degree-3 Jordan algebras on V=1"
    confidence: HIGH
    cost: "O(27^3) ~ O(20000) for d_{IJK} contraction"
    complements: "Direct sigma model on coset"
  - name: "F_4 orbit theory on OP^2"
    regime: "h_3(O) automorphisms (exact)"
    confidence: HIGH
    cost: "O(27^2) per orbit check"
    complements: "Explicit computation for each diagonal idempotent"
  - name: "Operational criteria OD1-OD7"
    regime: "Finite-dim formally real Jordan algebras"
    confidence: HIGH
    cost: "O(1) per criterion (direct verification)"
    complements: "KKT (provides OD4 conformal criterion)"

phase_suggestions:
  - name: "G4 Spacetime Derivation"
    goal: "Derive V_0 = spacetime via OD1-OD7 + KKT(h_2(C_u)) = so(4,2) + F_4 covariance"
    methods: ["KKT construction on h_2(C_u)", "Operational criteria OD1-OD7", "F_4 orbit theory on OP^2"]
    depends_on: []
    needs_research: false
    risk: LOW
    pitfalls: ["C1", "C3", "C4", "C7"]
  - name: "G2 N=2 SUSY as Consequence"
    goal: "Derive N=2 SUSY as consequence of Lagrangian uniqueness from det(X) + E_{6(-26)}"
    methods: ["VSR metric a_{IJ} from cubic norm", "E_{6(-26)} invariant Lagrangian enumeration"]
    depends_on: ["G4 Spacetime Derivation"]
    needs_research: false
    risk: MEDIUM
    pitfalls: ["C5", "C6", "C8", "C9", "C10", "C11"]

critical_benchmarks:
  - quantity: "dim(KKT(h_2(C_u)))"
    value: "15"
    source: "Koecher (1967), Gunaydin (1993)"
    confidence: HIGH
  - quantity: "Killing form signature of so(4,2)"
    value: "(6, 9)"
    source: "Standard Lie theory"
    confidence: HIGH
  - quantity: "dim(E_{6(-26)}/F_4)"
    value: "26"
    source: "Cartan classification"
    confidence: HIGH
  - quantity: "Number of E_{6(-26)}-invariant 2-derivative terms"
    value: "4 (EH + scalar kinetic + gauge kinetic + CS)"
    source: "GST (1984), Schur's lemma on irreducible 26 of F_4"
    confidence: MEDIUM
  - quantity: "VSR metric a_{IJ} eigenvalue count on V=1"
    value: "26 positive, 1 null"
    source: "de Wit-Van Proeyen (1992)"
    confidence: HIGH

open_questions:
  - question: "Is Lagrangian uniqueness from E_{6(-26)} + 2-derivative robust at the level needed for publication?"
    priority: HIGH
    blocks_phase: "G2 N=2 SUSY as Consequence"
  - question: "Does Lambda=0 constitute a prediction or a limitation?"
    priority: MEDIUM
    blocks_phase: "none"
  - question: "Does the C*-bottleneck on V_0 require independent justification beyond V_{1/2} analogy?"
    priority: MEDIUM
    blocks_phase: "none"

contradictions_unresolved: []
```
