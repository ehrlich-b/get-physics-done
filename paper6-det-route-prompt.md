# Paper 6 New Route: GR from det(X) on h_3(O)

## Research Question

Does the Peirce complement V_0 = h_2(O), viewed through the C*-observer's
complex structure, give a 4-dimensional Lorentzian spacetime h_2(C) = R^{3,1}
on which the GST magic supergravity Lagrangian (prepotential = det(X))
produces Einstein gravity with the correct SM matter coupling?

If yes: GR is derived from h_3(O) via proved theorems (GST 1983, Peirce
decomposition, C*-bottleneck). No lattice, no modeling choices.

## Context

### The derivation chain (Papers 5 + 7, proved)

1. Self-modeling → sequential product → Jordan → C* → M_n(C)^sa (Paper 5)
2. Non-composability → h_3(O) (Paper 7)
3. Peirce at rank-1 E: V_1(1) + V_{1/2}(16) + V_0(10) (standard)
4. C*-bottleneck on V_{1/2}: Spin(9) → Spin(10), chirality, SM gauge group (Paper 7)

### The new claim for GR

5. C*-bottleneck on V_0: h_2(O) → h_2(C) = R^{3,1} (THIS COMPUTATION)
6. det(X) on h_3(O) is the gravitational prepotential (GST 1983, proved)
7. GST Lagrangian on h_2(C) gives Einstein + SM matter (TO VERIFY)

### Key proved results to use

- h_2(C) = R^{3,1} with det = Minkowski metric (classical, see below)
- SL(2,C)/Z_2 = SO_0(3,1) acts on h_2(C) by X → gXg* (classical)
- Gunaydin-Sierra-Townsend (1983-84): The bosonic Lagrangian of 5d N=2
  MESGT for the exceptional magic case is completely determined by det(X)
  on h_3(O). The Lagrangian is:
  ```
  L = -R/2 - (1/4) a_{IJ} F^I F^J - (1/2) g_{xy} dphi^x dphi^y + CS
  ```
  where a_{IJ} = -(1/3) d_I d_J ln(det)|_{det=1}, g_{xy} is the pullback
  metric on E_{6(-26)}/F_4, and CS is the cubic Chern-Simons term.
- The bosonic truncation (fermions = 0) is always consistent.
- de Wit-Van Proeyen (hep-th/9112027): classification of symmetric very
  special real manifolds. E_{6(-26)}/F_4 is the unique exceptional case.

### The h_2(C) = R^{3,1} identification

An element of h_2(C) is:
```
X = (t+z    x+iy)     a, d real, b complex
    (x-iy   t-z )
```
det(X) = t^2 - x^2 - y^2 - z^2 = Minkowski norm.
SL(2,C) acts by X → gXg*, which IS the Lorentz group.
This is standard: h_2(C) ≅ R^{3,1} as an inner product space.

### The Peirce decomposition of h_3(O)

For E = E_{11} (the (1,1)-diagonal idempotent):
```
h_3(O) = V_1(E) + V_{1/2}(E) + V_0(E)

V_1 = {lambda * E_{11} : lambda in R}             dim 1
V_{1/2} = {off-diagonal (1,2) and (1,3) entries}  dim 16  (O + O)
V_0 = {the (2,3) block = h_2(O)}                  dim 10
```

V_0 consists of elements:
```
Y = (0  0    0  )
    (0  a    b  )    a, d in R, b in O
    (0  b*   d  )
```
This IS h_2(O), the 10-dimensional spin factor (Jordan algebra).

## Phase 1: Formalize the C*-Bottleneck on V_0

### 1A. Define the projection

The observer's complex structure is J = J_u for some u in S^6 subset Im(O).
This J determines a complex subspace C_u = span_R{1, u} inside O.

Define the projection:
```
proj_u : O ��� C_u
proj_u(x) = Re(x) + <Im(x), u> u
```
where <,> is the inner product on Im(O) = R^7.

Then define:
```
pi_u : h_2(O) → h_2(C_u) ≅ h_2(C)

pi_u(a, b; b*, d) = (a, proj_u(b); proj_u(b)*, d)
```

**Task 1A:** Verify this is well-defined. Compute explicitly for the
standard choice u = e_1 (the first imaginary octonion unit).

### 1B. Metric structure

det on h_2(O): det(Y) = ad - |b|^2 (for Y = (a, b; b*, d))
det on h_2(C_u): det(pi_u(Y)) = ad - |proj_u(b)|^2

These are NOT equal in general. That's expected: the observer doesn't see
the full 10d metric. The observer sees the 4d Minkowski metric on h_2(C_u).

**Task 1B:** Compute the relationship between det_10 (on h_2(O)) and
det_4 (on h_2(C_u)). Show that det_4 = Minkowski metric on the 4d subspace.
Identify the 6d kernel explicitly. Verify det_10 = det_4 + (quadratic form
on kernel), i.e., the 10d metric splits as 4d Minkowski + 6d internal.

### 1C. Equivariance

Spin(9) acts on V_0 = h_2(O) (as Aut(h_2(O)) plus the vector representation).
The projection pi_u breaks Spin(9) symmetry (it depends on u in S^6).

**Task 1C:**
1. What subgroup of Spin(9) preserves the decomposition h_2(O) = h_2(C_u) + ker(pi_u)?
2. Does this subgroup contain the Lorentz group SL(2,C_u) acting on h_2(C_u)?
3. What is the structure group on ker(pi_u)? Does it match gauge symmetries?

Expected: the stabilizer of u in Spin(9) should be related to SU(4) or
Spin(6), and the decomposition should be 10 = 4 + 6 where:
- 4 carries the (1/2, 1/2) representation of SL(2,C) (vector of SO(3,1))
- 6 carries a representation of SU(3) (antisymmetric tensor)

This would match the Calabi-Yau-like decomposition already noted in the
research program.

### 1D. Peirce multiplication compatibility

The Peirce rules say V_{1/2} * V_{1/2} subset V_0 + V_1. When two
V_{1/2}-elements multiply and land in V_0, their product is in h_2(O).

**Task 1D:** Apply pi_u to the V_0-component of V_{1/2} * V_{1/2} products.
1. Does the pi_u image carry the right quantum numbers?
2. Does the Peirce product V_{1/2} * V_{1/2} → V_0 → h_2(C_u) reproduce
   any known physics coupling (e.g., fermion bilinear → spacetime vector)?

## Phase 2: GST Field Content vs Paper 7

### 2A. Decompose the 27 under Peirce

The 27-dimensional representation of E_6 (which is h_3(O) as a vector space)
decomposes under the Peirce idempotent E as:
```
27 = 1 (V_1) + 16 (V_{1/2}) + 10 (V_0)
```

In the GST Lagrangian, the 27 scalars h^I parametrize the exceptional magic
scalar manifold. Under the Peirce decomposition, these should split into:
- 1 scalar from V_1 (observer degree of freedom)
- 16 scalars from V_{1/2} (matter content)
- 10 scalars from V_0 (spacetime + internal geometry)

**Task 2A:** Perform this decomposition explicitly. Verify that under the
SM gauge group (the intersection F_4 ∩ [Spin(9) × SU(3)^2/Z_3]):
1. The 16 from V_{1/2} gives one generation of SM fermions (as in Paper 7)
2. The 10 from V_0 decomposes as 4 (spacetime, after C*-bottleneck) + 6
   (internal, matching the kernel of pi_u)
3. The 1 from V_1 is a gauge singlet

### 2B. The Chern-Simons coupling

The GST Lagrangian has a cubic CS term:
```
(1/6sqrt6) C_{IJK} eps^{abcde} F^I_{ab} F^J_{cd} A^K_e
```
where C_{IJK} = d_{IJK} are the structure constants of det(X).

**Task 2B:** Decompose C_{IJK} under the Peirce decomposition. The
components C_{alpha beta gamma} where alpha, beta, gamma range over V_1,
V_{1/2}, V_0 should correspond to known physical couplings:
- C with all indices in V_{1/2}: fermion-fermion-fermion vertex?
- C with indices in V_{1/2}, V_{1/2}, V_0: fermion-fermion-spacetime?
- C with all indices in V_0: gravitational self-coupling?

Compare with the SM Lagrangian. Does the decomposition match any known
structure?

### 2C. The "double duty" theorem

**Task 2C:** State and prove:

**Theorem:** det(X) is the unique (up to scale) cubic polynomial on h_3(O)
invariant under F_4 = Aut(h_3(O)). Consequently:
(a) Any F_4-symmetric cubic density on h_3(O) is proportional to det(X).
    In particular, the cubic factor in rho_J = det(X)*(Tr(X^2) - 1/3) is
    forced by F_4-invariance.
(b) Any F_4-symmetric cubic prepotential on h_3(O) is proportional to det(X).
    In particular, the GST gravitational prepotential is forced by the
    algebraic symmetry of the basin.
(c) Therefore rho_J and the GST prepotential share det(X) because there is
    no other cubic F_4-invariant available. The connection between self-modeling
    density and gravitational dynamics is algebraically forced.

Proof should use: Springer 1962 (uniqueness of cubic invariant), the
representation theory of F_4 on h_3(O) (the 27 is irreducible under F_4,
so the space of cubic invariants is 1-dimensional).

## Phase 3: 5d → 4d Reduction (if Phases 1-2 succeed)

Standard circle compactification of the GST Lagrangian. The 5d theory on
M_5 = M_4 × S^1 gives:
- 5d metric → 4d metric + graviphoton + dilaton
- 27 5d vectors → 27 4d vectors + 27 scalars
- 26 5d scalars → 26 4d scalars
Total in 4d: 1 metric, 28 vectors, 56 scalars on E_{7(-25)}/(E_6 × U(1))

**Task 3A:** Identify M_4 = h_2(C_u). Compute the 4d Einstein equations
explicitly from the reduced Lagrangian.

**Task 3B:** Verify the matter coupling: do the 4d field equations give
the correct SM + gravity structure when the fields are decomposed under
the Peirce + C*-bottleneck?

**Task 3C:** What is the cosmological constant? The GST theory has Lambda = 0
in 5d (Minkowski vacuum). After reduction, is Lambda = 0 or Lambda ≠ 0?

## Deliverables

For each phase, produce:
1. A derivation document with all computations shown
2. Explicit matrix representations (use the standard E_{11} idempotent and
   u = e_1 for concreteness, then argue general case by F_4/G_2 transitivity)
3. Clear statement of what's proved vs what's argued
4. If any step FAILS, explain precisely why and what would need to be
   different

## Success Criteria

The route works if:
- pi_u : h_2(O) → h_2(C) is well-defined with the right equivariance (Phase 1)
- The GST field content matches Paper 7's SM content under Peirce (Phase 2)
- The 4d reduced theory gives Einstein + SM on h_2(C) (Phase 3)

The route fails if:
- The equivariance of pi_u doesn't contain the Lorentz group
- The GST field content is incompatible with Paper 7's SM particles
- The 4d reduction introduces pathologies (ghosts, wrong signs, etc.)

## References

- Gunaydin-Sierra-Townsend, Phys. Lett. B 133 (1983) 72
- Gunaydin-Sierra-Townsend, Nucl. Phys. B 242 (1984) 244
- de Wit-Van Proeyen, hep-th/9112027 (classification)
- Ferrara-Gunaydin, hep-th/9708025 (orbits + invariants)
- Ferrara-Gunaydin, hep-th/0606108 (attractors)
- Todorov-Drenska, arXiv:1805.06739 (SM from F_4)
- Boyle, arXiv:2006.16265 (triality + generations)
- Baez, math/0105155 (octonions survey)
- Faraut-Koranyi, "Analysis on Symmetric Cones" (1994)
- Springer, Indag. Math. 24 (1962) 259 (cubic invariant uniqueness)
- Ciaglia-Jost-Schwachhofer, arXiv:2005.02023 (Jordan → metrics)
- Farnsworth, arXiv:2503.10744 (exceptional spectral geometry)
