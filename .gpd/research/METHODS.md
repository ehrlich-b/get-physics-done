# Methods Research

**Domain:** Noncommutative geometry / Finite spectral triples / KO-dimension classification
**Researched:** 2026-03-22
**Confidence:** HIGH

### Scope Boundary

METHODS.md covers analytical and computational PHYSICS methods for the v4.0 spectral triple milestone: verifying spectral triple axioms, constructing the Dirac operator, analyzing the first-order condition, and classifying by KO-dimension. It does NOT cover software tools or libraries -- those belong in COMPUTATIONAL.md.

**Critical distinction from v3.0:** The v3.0 methods worked at the lattice level (area laws, Lieb-Robinson, Jacobson thermodynamics). The v4.0 methods work at the ALGEBRAIC level of a single site: we have a specific finite-dimensional (H, J, gamma) and must verify whether it forms a real spectral triple. The tools are matrix algebra, representation theory, and the classification theory of finite noncommutative geometries.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|--------|---------|-----------------|
| Direct axiom verification (matrix computation) | Check order zero, KO-dim 6 signs, orientability | The construction is finite-dimensional; all axioms reduce to explicit matrix identities on 2n^2-dimensional H |
| Bimodule decomposition | Classify the A-bimodule structure of H | Standard method (Krajewski, Cacic) for finite spectral triples; determines what Dirac operators are compatible |
| First-order condition linear algebra | Find subalgebra A_F forced by [[D,a], Jb*J^{-1}] = 0 | Reduces to solving a system of matrix commutation relations; the standard technique from Chamseddine-Connes 2008 |
| Krajewski diagram classification | Visualize and classify the finite spectral triple | Diagrammatic encoding of bimodule structure; each vertex = irreducible representation, each edge = allowed D component |
| Representation-theoretic decomposition | Decompose H as direct sum of irreducible A-A^o bimodules | Determines multiplicity matrix; constrains the form of D and the first-order condition |

### Numerical Methods

| Method | Purpose | When to Use |
|--------|---------|-------------|
| Explicit matrix instantiation at small n | Verify axioms for n=2,3,4 concretely | Always use alongside general-n proofs; catches sign errors and index mistakes |
| Brute-force commutator scan | Check order zero and first-order conditions | For small n (n <= 4): enumerate basis elements of A, compute all commutators numerically |
| Null space computation for first-order condition | Find subalgebra satisfying [[D,a], Jb*J^{-1}] = 0 | Recast condition as linear system Mv = 0 where v parameterizes a in A; kernel gives A_F |

### Method Selection by Problem Type

**If verifying order zero condition [a, Jb*J^{-1}] = 0:**
- Use direct matrix computation of the opposite algebra action pi_o(b) = Jb*J^{-1}
- Because our J = (PC)(sector-swap) is explicit, so pi_o(b) can be computed entry-by-entry
- Verify by checking [pi(a), pi_o(b)] = 0 for all basis elements e_{ij} of M_n(C)

**If constructing the Dirac operator D:**
- Use bimodule decomposition to parameterize all possible D, then impose D gamma = -gamma D and JD = DJ
- Because the space of self-adjoint operators on H is 4n^4-dimensional, but the bimodule constraints and symmetry conditions reduce this dramatically
- The sequential product asymmetry L_a - R_a provides the physical candidate; verify it satisfies the required conditions

**If finding the subalgebra from the first-order condition:**
- Use the linear algebra method: for each candidate a in A, [[D,a], Jb*J^{-1}] = 0 for all b is a LINEAR condition on a
- Rewrite as a matrix equation and find the kernel
- Because this is exactly how Chamseddine-Connes-Marcolli (arXiv:0706.3688) identified C + H + M_3(C): they found the maximal subalgebra of M_n(C) satisfying the first-order condition

**If classifying by KO-dimension:**
- Use the sign table directly: check (J^2, JD, J gamma) = (epsilon, epsilon', epsilon'') against the mod-8 classification
- Because this is a finite lookup (8 possible KO-dimensions), and two of three signs (J^2 = +1, J gamma = -gamma J) are already verified

---

## Method Details

### Method 1: Direct Axiom Verification for Finite Real Spectral Triples

**What:** Systematically verify all axioms of a real spectral triple (A, H, D, J, gamma) when A and H are finite-dimensional. In finite dimensions, all axioms reduce to algebraic identities between matrices.

**Mathematical basis:**

A real spectral triple of KO-dimension d (mod 8) consists of:

1. **Algebra representation:** A unital *-algebra A with a faithful *-representation pi: A -> B(H)
2. **Grading:** A self-adjoint unitary gamma on H with gamma^2 = 1, such that [gamma, pi(a)] = 0 for all a in A (even spectral triple)
3. **Real structure:** An antilinear isometry J: H -> H satisfying:
   - J^2 = epsilon * 1
   - J gamma = epsilon'' * gamma J
   - JD = epsilon' * DJ
   where (epsilon, epsilon', epsilon'') are determined by d mod 8
4. **Dirac operator:** A self-adjoint operator D on H with:
   - {D, gamma} = 0 (D anticommutes with gamma, i.e., D is odd)
   - [D, pi(a)] is bounded for all a in A (automatic in finite dims)
5. **Order zero condition:** [pi(a), J pi(b*) J^{-1}] = 0 for all a, b in A
6. **First-order condition:** [[D, pi(a)], J pi(b*) J^{-1}] = 0 for all a, b in A

**KO-dimension sign table (mod 8):**

| d mod 8 | epsilon (J^2) | epsilon' (JD) | epsilon'' (J gamma) |
|---------|---------------|---------------|---------------------|
| 0       | +1            | +1            | +1                  |
| 1       | +1            | -1            | --                  |
| 2       | -1            | +1            | +1                  |
| 3       | -1            | +1            | --                  |
| 4       | -1            | +1            | -1                  |
| 5       | -1            | -1            | --                  |
| 6       | +1            | +1            | -1                  |
| 7       | +1            | +1            | --                  |

For this project: KO-dimension 6 requires (epsilon, epsilon', epsilon'') = (+1, +1, -1).
Already verified: J^2 = +1 and J gamma = -gamma J. Remaining: JD = +DJ (depends on D construction).

**Verification procedure for our construction:**

Step 1: Write J, gamma, pi(a) as explicit matrices on H = C^{2n^2}.
Step 2: Verify gamma^2 = 1 and [gamma, pi(a)] = 0. (gamma = diag(P, -P) in particle/antiparticle block form; P commutes with a tensor 1.)
Step 3: Compute pi_o(b) = J pi(b*) J^{-1} for general b in M_n(C).
Step 4: Check [pi(a), pi_o(b)] = 0 for all a, b (order zero).
Step 5: Parameterize D subject to D* = D and D gamma = -gamma D.
Step 6: Impose JD = DJ to further constrain D.
Step 7: For the surviving D, check the first-order condition.

**Cost:** O(n^4) matrix multiplications for each axiom check at dimension n. For n=4 (SM candidate), matrices are 32x32 -- trivially computable.

**Known failure modes:**
- The naive algebra action pi(a)(psi, chi) = (a tensor 1)(psi, chi) may fail the order zero condition. The fix: modify the action on the antiparticle sector to use the contragredient representation pi(a)(psi, chi) = ((a tensor 1)psi, (a-bar tensor 1)chi), where a-bar is the complex conjugate. This is standard in Connes' framework.
- Missing the grading compatibility: the representation pi must be EVEN, meaning [gamma, pi(a)] = 0. Since gamma = diag(P, -P) and pi(a) = diag(a tensor 1, ?), the action on the antiparticle sector must also commute with P.

**Confidence:** HIGH. This is the standard verification procedure described in van Suijlekom (2024), Chapters 2-3. All steps are explicit finite-dimensional linear algebra.

**Key references:**
- Connes, "Noncommutative geometry and reality," J. Math. Phys. 36, 6194-6231 (1995)
- van Suijlekom, "Noncommutative Geometry and Particle Physics," 2nd ed., Springer (2024), Chapters 2-4
- Barrett, "Matrix geometries and fuzzy spaces as finite spectral triples," arXiv:1502.05383

---

### Method 2: Bimodule Decomposition and Krajewski Diagrams

**What:** Decompose the Hilbert space H into irreducible A-bimodules (equivalently, irreducible representations of A tensor A^o) to classify all compatible Dirac operators. Encode the result as a Krajewski diagram.

**Mathematical basis:**

For A = M_n(C), the irreducible representations are all equivalent to the fundamental representation on C^n. The opposite algebra A^o = M_n(C)^o is anti-isomorphic to A; it acts on the conjugate space C^n-bar.

An A-A^o bimodule is equivalent to a left A tensor A^o module. Since A tensor A^o = M_n(C) tensor M_n(C)^o, the irreducible bimodules are labeled by pairs (i, j) of irreducible representations of A and A^o respectively.

For our H = (C^n tensor C^n)_particle + (C^n tensor C^n)_antiparticle:
- The left A-action is pi(a) = a tensor 1 on each C^n tensor C^n factor
- The right A^o-action (via J) is pi_o(b) = J pi(b*) J^{-1}
- The bimodule decomposition determines which "off-diagonal" blocks D can connect

**Krajewski diagram rules:**
- Vertices: labeled by pairs (p, q) where p indexes the representation of A on the left and q the representation of A^o on the right
- Edges: connect vertices that D can couple (off-diagonal blocks of D in the bimodule decomposition)
- The grading gamma assigns +1 or -1 to each vertex
- D can only connect vertices of opposite grading
- The first-order condition constrains which edges are allowed

**For our construction:**
1. Identify how many irreducible A-A^o bimodule summands appear in H
2. Assign gamma eigenvalues to each summand
3. Draw the Krajewski diagram
4. Read off the allowed D structure
5. The first-order condition further constrains edges

**Cost:** The decomposition is O(n^2) in representation-theoretic complexity. For A = M_n(C), the bimodule structure is determined by how J intertwines the left and right actions.

**Regime of validity:** Works for any finite-dimensional *-algebra A. For semisimple A (our case), the decomposition is completely determined by the multiplicity matrix.

**Confidence:** HIGH. Krajewski diagrams are the standard classification tool for finite spectral triples, introduced by Krajewski (arXiv:hep-th/9701081) and systematized by Cacic (arXiv:0902.2068) and van Suijlekom (2024, Chapter 4).

**Key references:**
- Krajewski, "Classification of finite spectral triples," arXiv:hep-th/9701081
- Cacic, "Moduli spaces of Dirac operators for finite spectral triples," arXiv:0902.2068
- Paschke & Sitarz, "Discrete spectral triples and their symmetries," J. Math. Phys. 39, 6191 (1998)

---

### Method 3: Computing the Opposite Algebra Action

**What:** For our specific J = (PC)(sector-swap), compute the opposite algebra action pi_o(b) = J pi(b*) J^{-1} explicitly and verify the order zero condition.

**Mathematical basis:**

Given:
- pi(a)(psi, chi) = ((a tensor 1)psi, f(a)(chi)) where f(a) is the action on the antiparticle sector (to be determined)
- J(psi, chi) = (PC chi-bar, PC psi-bar) where PC: v tensor w -> w-bar tensor v-bar (swap + conjugate)
- J^{-1} = J (since J^2 = 1)

Compute pi_o(b) = J pi(b*) J^{-1}:

Step 1: J^{-1}(psi, chi) = (PC chi-bar, PC psi-bar)  [same as J]
Step 2: pi(b*)(PC chi-bar, PC psi-bar) = ((b* tensor 1)(PC chi-bar), f(b*)(PC psi-bar))
Step 3: Apply J to the result

The key subtlety: b* tensor 1 acting on PC chi-bar. Since PC maps v tensor w to w-bar tensor v-bar, we need:
(b* tensor 1)(w-bar tensor v-bar) = (b* w-bar) tensor v-bar

Then PC applied to this gives: v tensor (b* w-bar)-bar = v tensor (b-transpose w) [using (b* w-bar)-bar = b^T w].

So the opposite action is effectively 1 tensor b^T on the original space, which commutes with a tensor 1. This is exactly the standard result: for matrix algebras with J = complex conjugation + SWAP, the opposite algebra acts as 1 tensor b^T.

**The order zero condition [a tensor 1, 1 tensor b^T] = 0 holds automatically** for any a, b in M_n(C), because operators on different tensor factors commute.

**Critical check:** This analysis assumes the algebra acts as a tensor 1 on BOTH sectors, or that the action on the antiparticle sector is chosen compatibly. If the action on the antiparticle sector differs (e.g., contragredient: a-bar tensor 1), then pi_o(b) on the antiparticle sector may differ, and the computation must be redone.

**Confidence:** HIGH for the mathematical technique. MEDIUM for applicability to our specific J, because the sector-swap in J introduces cross-terms between particle and antiparticle sectors that must be tracked carefully.

---

### Method 4: Parameterizing and Constraining the Dirac Operator

**What:** Find all self-adjoint operators D on H = C^{2n^2} satisfying D gamma = -gamma D and JD = DJ, then identify which are natural from the self-modeling structure.

**Mathematical basis:**

In block form with respect to gamma eigenspaces H = H_+ + H_-:

gamma = diag(1_{H_+}, -1_{H_-})

D gamma = -gamma D forces D to be off-diagonal:

D = | 0    M* |
    | M    0  |

where M: H_+ -> H_- and D is self-adjoint iff D has this block form with M arbitrary.

For our grading gamma = diag(P, -P), the +1 eigenspace is:
- H_+ = Sym^2(C^n)_particle + wedge^2(C^n)_antiparticle

and the -1 eigenspace is:
- H_- = wedge^2(C^n)_particle + Sym^2(C^n)_antiparticle

So dim(H_+) = n(n+1)/2 + n(n-1)/2 = n^2, and similarly dim(H_-) = n^2.

M is therefore an n^2 x n^2 complex matrix, with n^4 real parameters (after self-adjointness of D).

The condition JD = DJ further constrains M. Since J mixes particle and antiparticle sectors, this imposes relations between the sub-blocks of M connecting:
- Sym^2_particle -> wedge^2_particle (within particle sector)
- wedge^2_antiparticle -> Sym^2_antiparticle (within antiparticle sector)
- Cross-sector terms

**Natural candidate from self-modeling:**
The sequential product asymmetry operator: for a in M_n(C)^sa,
  (L_a - R_a)(b) = sqrt(a) b sqrt(a) - sqrt(b) a sqrt(b)

This is antisymmetric under SWAP (P(L_a - R_a)P = -(L_a - R_a) when acting on C^n tensor C^n via the identification b -> b as matrix = element of C^n tensor C^n). Therefore it maps Sym^2 <-> wedge^2, giving D gamma = -gamma D.

**Procedure:**
1. Write D in block form with respect to gamma eigenspaces
2. Impose D* = D (self-adjointness)
3. Impose JD = DJ (compute J in the same block decomposition)
4. Count free parameters -- this gives the moduli space of Dirac operators
5. Check whether the sequential product asymmetry candidate lies in this space
6. If yes, compute [D, a] for general a in A

**Cost:** For n=4 (SM candidate), D is parameterized by a 16x16 complex matrix M with JD = DJ constraints. The constraint system is a set of linear equations -- solved by null space computation.

**Confidence:** HIGH. The block decomposition method is standard (Barrett arXiv:1502.05383, van Suijlekom 2024 Chapter 3). The sequential product candidate is novel to this project but the verification method is standard.

**Key references:**
- Barrett, "Matrix geometries and fuzzy spaces as finite spectral triples," arXiv:1502.05383
- van Suijlekom (2024), Chapter 3: "Finite Real Noncommutative Spaces"

---

### Method 5: First-Order Condition and Subalgebra Identification

**What:** Given D, find the maximal subalgebra A_F of A = M_n(C) satisfying the first-order condition [[D, pi(a)], J pi(b*) J^{-1}] = 0 for all b in A.

**Mathematical basis:**

The first-order condition says: for each a in A_F, the operator [D, pi(a)] must commute with the entire opposite algebra pi_o(A) = J pi(A*) J^{-1}.

Since pi_o(A) = {1 tensor b^T : b in M_n(C)} (from Method 3), this means:

[[D, a tensor 1], 1 tensor b^T] = 0 for all b in M_n(C)

This is equivalent to: [D, a tensor 1] commutes with all operators of the form 1 tensor b^T, which means [D, a tensor 1] must be of the form c tensor 1 for some c. In other words, [D, a tensor 1] must act trivially on the second tensor factor.

**Algorithm (Chamseddine-Connes method):**
1. Compute [D, e_{ij} tensor 1] for each matrix unit e_{ij} of M_n(C)
2. Check whether [D, e_{ij} tensor 1] is of the form (something) tensor 1
3. If not for all i,j: find the subset of a = sum a_{ij} e_{ij} for which sum a_{ij} [D, e_{ij} tensor 1] IS of the form c tensor 1
4. This subset is the subalgebra A_F
5. Identify A_F as an abstract algebra (by computing its structure constants)

**Alternative algorithm (null space method):**
1. For each pair (a, b), the condition [[D, pi(a)], pi_o(b)] = 0 is linear in a
2. Fix b and vary a: get a linear system. The solution space is A_F(b)
3. Intersect over all b: A_F = intersection of A_F(b) over all b
4. In practice, it suffices to check b ranging over a basis of A

**What Chamseddine-Connes found (arXiv:0706.3688):**
Starting from A = M_k(C) (before tensoring with continuous algebra), the first-order condition on D selects the subalgebra. For k=2: A_F = M_2(C) (no restriction). For k > 2 with a generic D: A_F is a proper subalgebra. The classification theorem states that for k=4 with KO-dimension 6 and quaternion linearity, the maximal subalgebra is C + H + M_3(C).

**Key insight for our construction:**
The starting algebra is M_n(C) acting on C^n tensor C^n. The classification theorem of Chamseddine-Connes-Marcolli says: among irreducible finite geometries of KO-dimension 6 (mod 8) with H of dimension k^2, the maximal subalgebra satisfying the first-order condition for an off-diagonal D is isomorphic to C + H + M_{k-2}(C) when k >= 4.

For our construction, if k = n (matching our C^n tensor C^n decomposition), then:
- n = 4 gives A_F = C + H + M_2(C) -- NOT the SM (need M_3(C))
- n = 5 gives A_F = C + H + M_3(C) -- the SM algebra

However, the dimension matching may be different because our H has dimension 2n^2, not n^2. The precise mapping between our construction and the Chamseddine-Connes framework needs explicit computation.

**Cost:** O(n^6) for the brute-force method (n^2 basis elements of A, each requiring O(n^4) matrix operations). For n <= 6, this is trivially fast.

**Confidence:** HIGH for the method. MEDIUM for predicting which n gives SM, because the mapping between our doubled Hilbert space and the Chamseddine-Connes setup is the core open question.

**Key references:**
- Chamseddine & Connes, "Why the Standard Model," arXiv:0706.3688
- Chamseddine, Connes & Marcolli, "Gravity and the standard model with neutrino mixing," arXiv:hep-th/0610241
- Connes, "Noncommutative geometry and the standard model with neutrino mixing," arXiv:hep-th/0608226

---

### Method 6: KO-Dimension Verification and Sign Consistency

**What:** Verify that all three sign relations (epsilon, epsilon', epsilon'') are simultaneously satisfied for KO-dimension 6 once D is constructed.

**Mathematical basis:**

For KO-dimension 6: (epsilon, epsilon', epsilon'') = (+1, +1, -1).

Current status:
- J^2 = +1: VERIFIED algebraically and independently of D
- J gamma = -gamma J: VERIFIED algebraically and independently of D
- JD = +DJ: DEPENDS ON D, must be checked after D construction

The verification of JD = DJ:
1. Write J in matrix form on H = C^{2n^2}
2. Write D in block form (from Method 4)
3. Compute JD and DJ as explicit matrices
4. Check equality

**Additional KO-dimension consistency checks:**
- The Hochschild homology condition (orientability): there exists a Hochschild d-cycle c such that pi(c) = gamma. For d=6 and finite algebras, this is automatically satisfied when gamma is in the image of the representation.
- Poincare duality: the intersection form on K-theory is non-degenerate. For finite spectral triples, this reduces to checking that the multiplicity matrix is non-degenerate (has non-zero determinant).

**Confidence:** HIGH. This is a direct computation once D is known.

---

## Alternatives Considered

| Recommended | Alternative | When to Use Alternative |
|-------------|-------------|------------------------|
| Direct matrix computation | Abstract C*-algebra methods | Never for finite dims -- direct computation is simpler, more transparent, and catches errors |
| Krajewski diagrams | Exhaustive search over all D | Only if the Krajewski diagram approach fails to constrain D sufficiently (unlikely for our specific A) |
| First-order condition for subalgebra | Postulating A_F and checking | Only as a sanity check AFTER the systematic method identifies A_F; never as the primary method |
| Sequential product asymmetry for D | Generic off-diagonal D | Use generic D for classification; sequential product D for physical interpretation |
| SymPy symbolic verification | Pen-and-paper only | Never skip computational verification; SymPy catches sign errors that pen-and-paper misses |

## What NOT to Use

| Avoid | Why | Use Instead |
|-------|-----|-------------|
| Infinite-dimensional spectral triple methods | Entire construction is finite-dimensional; Dirac operator is a matrix, not an unbounded operator; no analysis needed | Direct matrix algebra |
| Spectral action computation at this stage | Premature -- need D first, and spectral action is a consequence, not an input | Axiom verification first; spectral action only after D is fully determined |
| Fuzzy sphere methods | Our algebra is M_n(C) on a tensor product, not on a fuzzy sphere; different geometry | Krajewski/bimodule decomposition for our specific representation |
| Ad hoc Dirac operator guessing | Unprincipled; the bimodule decomposition constrains D systematically | Method 4 (systematic parameterization) + physical candidate from sequential product |
| Twisted spectral triples | Generalization not needed unless standard axioms fail; adds unnecessary complexity | Standard (untwisted) axioms first; twist only if forced by failure |

---

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
|--------|--------------------|-----------------|
| Order zero condition | Compute [pi(a), pi_o(b)] for all basis elements at n=2,3; must be exactly zero | Connes' SM spectral triple has order zero satisfied for A_F = C + H + M_3(C) on H_F = C^{32} |
| Dirac operator construction | Check D gamma = -gamma D and JD = DJ; verify D* = D; compute spectrum of D | For the SM triple, D has eigenvalues related to Yukawa coupling matrices |
| First-order condition | For identified A_F, verify [[D,a], pi_o(b)] = 0 for all a in A_F, b in A; then check A_F is MAXIMAL | Chamseddine-Connes: A_F = C + H + M_3(C) is the unique maximal subalgebra for k=4, KO-dim 6 |
| KO-dimension | All three signs must match the table simultaneously | Standard: (J^2, JD, Jgamma) = (+1, +1, -1) for KO-dim 6 |
| Krajewski diagram | Must reproduce the known diagram for comparable spectral triples | SM Krajewski diagram has 4 vertices with specific edge structure |

### Cross-Checks

| Check | Expected Result | If It Fails |
|-------|----------------|-------------|
| dim(A_F) | Should be 1 + 4 + 9 = 14 for C + H + M_3(C) | Different subalgebra; recheck D construction |
| Gauge group from A_F | U(A_F) / center should give U(1) x SU(2) x SU(3) | Different gauge group; still publishable if spectral triple is valid |
| KO-dim 6 at general n | All sign relations hold independently of n | If n-dependent, the construction is not robust |
| Order zero at general n | Should hold for ALL n, not just specific values | If only specific n: constraint on the framework |
| Bimodule structure | H should decompose as a direct sum of irreducible A-A^o bimodules with non-trivial multiplicities | Trivial decomposition means D is too constrained |

---

## Installation / Setup

```bash
# Core computational environment (already in project)
pip install numpy scipy sympy

# No additional specialized software needed -- all methods are
# direct matrix algebra implementable in SymPy/NumPy.
# The project already has SymPy verification infrastructure
# from 658+ tests in v2.0.
```

---

## Sources

- Connes, "Noncommutative geometry and reality," J. Math. Phys. 36, 6194-6231 (1995). [PDF](https://alainconnes.org/wp-content/uploads/reality.pdf)
- Chamseddine & Connes, "Why the Standard Model," J. Geom. Phys. 58, 38-64 (2008). [arXiv:0706.3688](https://arxiv.org/abs/0706.3688)
- Chamseddine, Connes & Marcolli, "Gravity and the standard model with neutrino mixing," [arXiv:hep-th/0610241](https://arxiv.org/abs/hep-th/0610241)
- Connes, "Noncommutative geometry and the standard model with neutrino mixing," [arXiv:hep-th/0608226](https://arxiv.org/abs/hep-th/0608226)
- van Suijlekom, "Noncommutative Geometry and Particle Physics," 2nd ed., Springer (2024). [PDF](http://www.waltervansuijlekom.nl/wp-content/uploads/2024/02/ncgphysics2nd.pdf)
- Krajewski, "Classification of finite spectral triples," [arXiv:hep-th/9701081](https://arxiv.org/abs/hep-th/9701081)
- Cacic, "Moduli spaces of Dirac operators for finite spectral triples," [arXiv:0902.2068](https://arxiv.org/abs/0902.2068)
- Barrett, "Matrix geometries and fuzzy spaces as finite spectral triples," [arXiv:1502.05383](https://arxiv.org/abs/1502.05383)
- Paschke & Sitarz, "Discrete spectral triples and their symmetries," J. Math. Phys. 39, 6191-6205 (1998)
- Connes & Marcolli, "Noncommutative Geometry, Quantum Fields and Motives," AMS Colloquium Publications 55 (2008). [PDF](https://www.math.fsu.edu/~marcolli/bookjune4.pdf)

---

_Methods research for: Finite spectral triple verification (v4.0 milestone)_
_Researched: 2026-03-22_
