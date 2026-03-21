# Computational Approaches: Sequential Product Axioms and Jordan Algebra Structures

**Surveyed:** 2026-03-20
**Domain:** Mathematical physics / quantum foundations (effect algebras, sequential products, Jordan algebras)
**Confidence:** MEDIUM

## Recommended Stack

The computational work for v2.0 is primarily **proof support**, not heavy numerics. The main computational needs are: (1) symbolic verification that specific axiom identities hold for concrete matrix representations, (2) constructing and testing toy models of sequential products, and (3) exploring the Jordan algebra structure that emerges. The recommended stack is **SymPy for symbolic axiom checking** on explicit low-dimensional matrix models, with **SageMath as a reference tool** for Jordan algebra structure verification when needed. No dedicated software exists for effect algebra or sequential product computation -- this is a build-from-scratch-in-Python situation for the domain-specific parts, leveraging standard symbolic/numerical libraries for the linear algebra backbone.

There is no existing software package for "verify van de Wetering axioms S1-S7 on a given sequential product." This must be built as a lightweight test harness. The good news: the axioms are concrete algebraic identities on finite-dimensional spaces, so verification reduces to symbolic matrix manipulation, which SymPy handles well.

## Numerical Algorithms

| Algorithm | Problem | Convergence | Cost per Step | Memory | Key Reference |
|-----------|---------|-------------|---------------|--------|---------------|
| Symbolic identity verification | Check S1-S7 axiom equalities for parametric matrix families | Exact (symbolic) | O(n^3) per matrix multiply, n = dim | O(n^2) | SymPy docs |
| Positive semidefiniteness check | Verify effect algebra membership (0 <= a <= 1) | Exact (eigenvalue) | O(n^3) | O(n^2) | numpy.linalg.eigvalsh |
| Jordan product computation | Compute a o b = (ab + ba)/2 symbolically | Exact | O(n^3) | O(n^2) | Direct implementation |
| Cone membership (Koecher-Vinberg) | Check homogeneity and self-duality of positive cone | Numerical/symbolic | O(n^6) worst case for automorphism search | O(n^4) | Orlitzky (2022) |

### Convergence Properties

These are all exact-arithmetic or finite-precision linear algebra operations, not iterative algorithms. The relevant "convergence" issue is symbolic simplification:

- **Symbolic simplification:** SymPy's `simplify()` is not guaranteed to recognize all equalities. Use `expand()` then `simplify()`, and cross-check numerically for parametric identities.
- **Numerical cross-check:** For any symbolic identity, instantiate at 10+ random parameter values and check to machine precision. If symbolic fails but numerical passes, the identity likely holds but SymPy cannot simplify it -- try manual algebraic manipulation.
- **Known failure mode:** SymPy struggles with expressions involving square roots of matrices (relevant for the Luders product a^{1/2} b a^{1/2}). For 2x2 matrices, compute sqrt explicitly via the Cayley-Hamilton formula. For larger matrices, use numerical evaluation.

## Software Ecosystem

### Primary Tools

| Tool | Version | Purpose | License | Maturity |
|------|---------|---------|---------|----------|
| SymPy | >= 1.12 | Symbolic axiom verification, parametric matrix identities | BSD | Stable |
| NumPy | >= 1.24 | Numerical cross-checks, random matrix generation, eigenvalue computation | BSD | Stable |
| SciPy | >= 1.11 | Matrix functions (sqrtm for Luders product), optimization | BSD | Stable |

### Supporting Tools

| Tool | Version | Purpose | When Needed |
|------|---------|---------|-------------|
| SageMath | >= 10.0 | Jordan algebra structure verification, exceptional algebra exploration | If you need to verify Jordan algebra classification results or work with the full EJA taxonomy |
| Matplotlib | >= 3.7 | Visualizing state spaces, effect algebra geometry | For toy model visualization only |

### Why NOT Other Tools

| Tool | Why Skip |
|------|----------|
| Mathematica | Stronger symbolic engine, but project is Python-native. SymPy suffices for the matrix dimensions involved (2x2 to 4x4). |
| GAP (computational algebra) | Designed for group theory, not Jordan algebras or order unit spaces. |
| Lean/Coq (proof assistants) | Overkill for the current scope. The axiom verification is algebraic identity checking, not deep formal verification. Revisit only if a paper referee demands machine-checked proofs. |
| QuTiP | Designed for quantum dynamics simulation. The v2.0 work is algebraic structure, not dynamics. The existing Lindblad code from v1.0 is irrelevant here. |

## Data Flow

```
Define order unit space V (finite-dim, with unit 1 and positive cone)
  -> Define effects E(V) = {a in V : 0 <= a <= 1}
  -> Define candidate sequential product: seq(a,b) = [self-modeling construction]
  -> Check S1: seq(a, lambda*b1 + (1-lambda)*b2) = lambda*seq(a,b1) + (1-lambda)*seq(a,b2)
  -> Check S2: continuity of a -> seq(a,b) [automatic in finite dim]
  -> Check S3: seq(1, a) = a
  -> Check S4: seq(a,b) = 0 iff seq(b,a) = 0  [THE CRITICAL ONE]
  -> Check S5-S7: compatibility conditions
  -> If all pass: invoke Koecher-Vinberg -> Jordan algebra classification
  -> Validate: check Jordan identity (a o b) o a^2 = a o (b o a^2) on result
```

## Computation Order and Dependencies

| Step | Depends On | Produces | Can Parallelize? |
|------|-----------|----------|-----------------|
| 1. Implement Luders product for M_n(C) | Nothing | Reference sequential product implementation | Yes |
| 2. Implement self-modeling sequential product | Formal definition from Phase 1 proof work | Candidate sequential product function | No (needs math first) |
| 3. Verify S1-S3 symbolically (2x2) | Steps 1-2 | Pass/fail for easy axioms | Yes (independent axioms) |
| 4. Verify S4 symbolically (2x2) | Steps 1-2 | Pass/fail for critical axiom | Yes |
| 5. Verify S5-S7 symbolically (2x2) | Steps 1-2 | Pass/fail for remaining axioms | Yes |
| 6. Numerical cross-check (3x3, 4x4) | Steps 3-5 passing | Confidence in generality | Yes |
| 7. Jordan product verification | Step 6 | Confirm Jordan identity holds | No (needs prior steps) |

## Resource Estimates

| Computation | Time (estimate) | Memory | Storage | Hardware |
|-------------|-----------------|--------|---------|----------|
| Symbolic S1-S7 check (2x2 matrices) | < 1 minute | < 100 MB | Negligible | Local CPU |
| Symbolic S1-S7 check (3x3 matrices) | 1-10 minutes | < 500 MB | Negligible | Local CPU |
| Numerical cross-check (4x4, 1000 samples) | < 1 minute | < 100 MB | Negligible | Local CPU |
| SageMath Jordan algebra classification | < 1 minute | < 500 MB | Negligible | Local CPU |

All computation is trivially local. No HPC, no GPU, no cluster. The matrices involved are at most 4x4 (or 8x8 for body-model composites). This is proof-support computation, not simulation.

## Integration with Existing Code

The v1.0 codebase (Lindblad dynamics, Markov chain analysis) is **not directly relevant** to v2.0. The v2.0 work is algebraic structure theory, not dynamical simulation. However:

- **Input formats:** The self-modeling construction from v1.0 defines body B and model M as finite-dimensional systems with transition matrices. The v2.0 code needs to extract the effect algebra from this.
- **Output formats:** Axiom verification results (pass/fail per axiom, with counterexample if fail). Jordan algebra type classification.
- **Interface points:** The "self-modeling sequential product" definition bridges v1.0 (operational construction) and v2.0 (algebraic axiom checking). This definition is the key formalization task in Phase 1 -- it must be written down mathematically before any code.

## Concrete Toy Models for Testing

These are the sequential products to implement and test against, ordered by usefulness.

### Model 1: Standard Quantum Sequential Product (Luders product on M_2(C))

**What:** For effects a, b in the set of positive operators on C^2 with 0 <= a <= I, define seq(a,b) = a^{1/2} b a^{1/2}.

**Why first:** This is the canonical example that satisfies all of S1-S7 by construction. It serves as a **positive control** -- if your axiom-checking code does not confirm S1-S7 for this model, you have a bug.

**Implementation:**
```python
import numpy as np
from scipy.linalg import sqrtm

def luders_product(a, b):
    """Standard quantum sequential product: sqrt(a) @ b @ sqrt(a)"""
    sqrt_a = sqrtm(a)
    return sqrt_a @ b @ sqrt_a
```

**Dimension:** 2x2 complex matrices. Effects are 2x2 positive semidefinite with eigenvalues in [0,1].

**Reference:** Gudder and Greechie (2002), "Sequential products on effect algebras," Reports on Mathematical Physics 49:87-111.

### Model 2: Classical Sequential Product (diagonal matrices / Boolean algebra)

**What:** For a commutative algebra (diagonal matrices), seq(a,b) = a * b (pointwise product).

**Why second:** This is the classical limit. It trivially satisfies S1-S7 and produces a commutative Jordan algebra (the spin factor of dimension 1, i.e., just R^n with pointwise multiplication). Serves as a **degenerate control**.

**Implementation:**
```python
def classical_product(a, b):
    """Classical sequential product: pointwise multiplication of diagonals"""
    return np.diag(np.diag(a) * np.diag(b))
```

### Model 3: Self-Modeling Sequential Product (THE TARGET)

**What:** For a self-modeling system with body B and model M, the sequential product is: "test effect a on B, update M via the self-modeling map, test effect b on B." The precise mathematical form depends on the Phase 1 formalization.

**Why third:** This is the actual construction to be verified. Cannot be implemented until the formal definition is complete. The code structure should be: define the update map phi: E(B) -> channels on M, then seq(a,b) = [result of testing a, applying phi(a) to update M, then testing b].

**Implementation sketch (pending formalization):**
```python
def self_model_product(a, b, update_map, state):
    """
    Self-modeling sequential product.
    a, b: effects on body B
    update_map: E(B) -> CPTP maps on M
    state: current state of B x M

    Returns: probability of (a then b) = Tr[b . update_map(a)(sqrt(a) state sqrt(a))]
    """
    # Precise form TBD -- depends on Phase 1 formalization
    pass
```

**Key question:** Does seq(a,b) live in E(B), E(M), or E(B tensor M)? The framing choice (effects on B vs effects on B x M) is itself a Phase 1 research question.

### Model 4: Spin Factor Sequential Product

**What:** The spin factor V_n = R + R^n with Jordan product (alpha, x) o (beta, y) = (alpha*beta + <x,y>, alpha*y + beta*x). The effect algebra is {(alpha, x) : alpha + |x| <= 1, alpha - |x| >= 0}. The sequential product is defined via the spectral decomposition.

**Why:** The spin factors are the simplest non-trivial Euclidean Jordan algebras beyond M_n(C). V_3 (the Bloch ball) is isomorphic to the 2x2 quantum case, so it provides an alternative representation of Model 1. V_n for n > 3 gives genuinely non-quantum Jordan algebras that still satisfy S1-S7. Testing against these catches bugs that only appear outside the quantum case.

**Reference:** van de Wetering (2018/2019), arXiv:1803.11139, Section 5.

### Model 5: Non-Example (Violating S4)

**What:** Construct a sequential product that violates S4 (symmetry of orthogonality). For instance, take seq(a,b) = a*b (just matrix multiplication, no symmetrization). This fails S4 because a*b = 0 does not imply b*a = 0 for general matrices.

**Why:** Serves as a **negative control**. If your axiom-checking code does not detect the S4 violation for this model, you have a bug in the S4 check.

**Implementation:**
```python
def asymmetric_product(a, b):
    """Non-example: plain matrix multiplication. Violates S4."""
    return a @ b
```

## Axiom Verification Strategy

For each axiom, the verification approach:

| Axiom | Statement | Verification Method | Difficulty |
|-------|-----------|-------------------|------------|
| S1 | seq(a, lambda*b1 + (1-lambda)*b2) = lambda*seq(a,b1) + (1-lambda)*seq(a,b2) | Symbolic: expand both sides, check equality | Easy |
| S2 | a_n -> a implies seq(a_n, b) -> seq(a, b) | Automatic in finite dimensions (matrix sqrt is continuous on PSD cone) | Free |
| S3 | seq(1, a) = a | Direct substitution | Trivial |
| S4 | seq(a, b) = 0 iff seq(b, a) = 0 | Must check both directions. Symbolic: parameterize generic a, b, impose seq(a,b)=0, check if seq(b,a)=0 follows. Numerical: random search for counterexamples. | HARD -- this is the critical axiom |
| S5 | If a, b commute and a+b <= 1, then seq(a+b, c) = seq(a, c) + seq(b, c) | Symbolic with commutativity constraint | Medium |
| S6 | If a, b commute, then seq(a, b) = seq(b, a) | Symbolic with commutativity constraint | Easy |
| S7 | If a, b commute and a+b <= 1, then a+b commutes with any c that both a,b commute with | Symbolic | Medium |

### S4 Verification -- The Critical Check

S4 is the make-or-break axiom. For the standard Luders product, S4 holds because a^{1/2} b a^{1/2} = 0 iff the ranges of a and b are orthogonal (as subspaces), which is a symmetric relation. For the self-modeling product, this is not obvious.

**Approach for S4:**
1. **Symbolic (2x2):** Parameterize generic 2x2 effects a = [[a11, a12], [a12*, a22]] with 0 <= a <= I. Compute seq(a,b) symbolically. Impose seq(a,b) = 0 (4 equations). Check whether seq(b,a) = 0 follows.
2. **Numerical search for counterexample:** Generate 10,000+ random pairs (a,b) in E(C^2). For each pair where |seq(a,b)| < epsilon, check |seq(b,a)|. If any pair has |seq(a,b)| < epsilon but |seq(b,a)| >> epsilon, S4 fails.
3. **Analytic argument:** If steps 1-2 suggest S4 holds, construct a proof. If they suggest failure, characterize the counterexample.

## Validation Strategy

| Result | Validation Method | Benchmark | Source |
|--------|------------------|-----------|--------|
| Luders product satisfies S1-S7 | Run axiom checker on Model 1 | All axioms pass | Gudder-Greechie (2002), van de Wetering (2018) |
| Classical product satisfies S1-S7 | Run axiom checker on Model 2 | All axioms pass | Trivial (commutative algebra) |
| Asymmetric product violates S4 | Run axiom checker on Model 5 | S4 fails | Construction (non-symmetric zero divisors exist) |
| Jordan identity holds for verified product | Check (a o b) o a^2 = a o (b o a^2) | Identity holds | Definition of Jordan algebra |
| Spin factor classification | SageMath Jordan algebra tools | Known classification (R, spin factors, M_n(R), M_n(C), M_n(H), M_3(O)) | Jordan-von Neumann-Wigner (1934) |

## Open Questions

| Question | Why Open | Impact on Project | Approaches Being Tried |
|----------|---------|-------------------|----------------------|
| Does the self-modeling sequential product satisfy S4? | No prior work on this specific construction | If no: project produces valuable negative result. If yes: involution derived. | Formal proof (Phase 1), computational testing (this plan) |
| Which effect algebra framing is correct? | Effects on B vs effects on B x M give different sequential products | Determines the entire algebraic setup | Try both, see which satisfies more axioms |
| Is there existing GPT computation software? | Web search found no dedicated package | Must build axiom checker from scratch | Confirmed: no existing package. Build lightweight Python harness. |

## Anti-Approaches

| Anti-Approach | Why Avoid | What to Do Instead |
|---------------|-----------|-------------------|
| Using QuTiP or quantum dynamics simulators | v2.0 is algebraic structure theory, not dynamics simulation | Build lightweight symbolic/numerical axiom checker in plain SymPy + NumPy |
| Attempting infinite-dimensional verification | van de Wetering's theorem requires additional assumptions in infinite dimensions | Stay in finite dimensions. Start with n=2, then n=3. |
| Trying to use Lean/Coq for axiom verification | Massive overhead for formalizing effect algebras in a proof assistant; no existing libraries | Use symbolic Python for computational checks; write human-readable proofs |
| Numerical-only axiom checking | Floating point cannot prove identities, only find counterexamples | Symbolic verification primary, numerical as cross-check only |
| SageMath-only approach | SageMath's Jordan algebra module handles specific algebra types (exceptional, from bilinear forms) but not sequential product axioms | Use SageMath only for Jordan algebra classification after axioms are verified; use SymPy for the axiom checking itself |

## Logical Dependencies

```
Formal definition of self-modeling sequential product (MATH, Phase 1)
  -> Implementation of seq(a,b) in Python
  -> Symbolic axiom checking S1-S7 (this computational plan)
  -> If S1-S7 pass: Jordan algebra identification via Koecher-Vinberg

Luders product implementation (KNOWN)
  -> Positive control for axiom checker
  -> Must pass before trusting any results on novel constructions

Classical product implementation (KNOWN)
  -> Degenerate control for axiom checker

S4 verification result
  -> If PASS: proceed to S5-S7 and then Jordan classification
  -> If FAIL: characterize failure, pivot to D'Ariano backup (Phase 4)
```

## Recommended Investigation Scope

Prioritize:
1. **Implement Luders product axiom checker (positive control)** -- confirms tooling works before applying to novel construction
2. **Implement self-modeling sequential product** -- once Phase 1 formalization is complete
3. **S4 verification** -- the decisive computation

Defer:
- **SageMath Jordan algebra exploration** -- only needed after axioms are confirmed
- **Spin factor models** -- useful for intuition but not on the critical path
- **Visualization** -- nice-to-have, not needed for proofs

## Installation / Setup

```bash
# Core stack (likely already installed from v1.0)
pip install numpy scipy sympy matplotlib

# SageMath (optional, for Jordan algebra classification)
# SageMath is a large install (~2GB). Only install if needed for Jordan algebra tools.
# brew install --cask sage   # macOS
# Or use SageMath online: https://sagecell.sagemath.org/
```

No additional specialized packages needed. The axiom checker will be custom Python code using SymPy and NumPy.

## SageMath Jordan Algebra Capabilities (Reference)

SageMath (>= 10.0) provides `sage.algebras.jordan_algebra` with:

- **Construction from associative algebras:** JordanAlgebra(A) where A is an associative algebra, giving Jordan product a o b = (ab + ba)/2
- **Construction from bilinear forms:** JordanAlgebra(M, B) where M is a module and B a symmetric bilinear form
- **Exceptional Jordan algebra:** 27-dimensional algebra of 3x3 self-adjoint matrices over octonions, via `sage.algebras.octonion_algebra`
- **Operations:** Jordan product, unit element, derivation algebra (returns Lie algebra of type F4 for exceptional case)

**Limitation:** SageMath does NOT implement Euclidean Jordan algebras as a standalone class with spectral decomposition, trace form, or cone-of-squares computation. Michael Orlitzky has written extensively on EJA computation for optimization (see his 2022 draft "Euclidean Jordan algebras for optimization") but this is not yet merged into SageMath proper. For our purposes, the main SageMath JordanAlgebra class suffices for structural checks; spectral decomposition on small matrices can be done directly in NumPy/SciPy.

**Relevant SageMath classes:**
- `sage.algebras.jordan_algebra.JordanAlgebra` -- general Jordan algebra construction
- `sage.algebras.octonion_algebra.OctonionAlgebra` -- for exceptional Jordan algebra
- `sage.matrix.matrix2.Matrix.jordan_form()` -- Jordan normal form (different concept, but useful for spectral decomposition of individual elements)

## Key References

- van de Wetering (2018/2019), "Sequential product spaces are Jordan algebras," arXiv:1803.11139, J. Math. Phys. 60:062201 -- Defines axioms S1-S7, proves main theorem via Koecher-Vinberg
- van de Wetering (2018), "Three characterisations of the sequential product," arXiv:1803.08453 -- Additional characterizations, useful for understanding what makes the standard product special
- Gudder and Greechie (2002), "Sequential products on effect algebras," Reports on Mathematical Physics 49:87-111 -- Original sequential product formalism
- Westerbaan, Westerbaan, and van de Wetering (2020), "The three types of normal sequential effect algebras," arXiv:2004.12749, Quantum 4:378 -- Classification into Boolean, convex, and almost-convex types. Key result: no finite non-Boolean SEAs exist (constrains what toy models are possible)
- Orlitzky (2022), "Euclidean Jordan algebras for optimization" (draft) -- Computational algorithms for EJA rank, characteristic polynomials, and cone membership. URL: michael.orlitzky.com
- Barnum, Ududec, van de Wetering (2023), "Composites and categories of Euclidean Jordan algebras," arXiv:2306.00362 -- Compositionality constraints relevant to Phase 2 local tomography
- Plavala (2023), "General probabilistic theories: An introduction," arXiv:2103.07469, Physics Reports 1033:1-64 -- Comprehensive GPT review; Section 6 covers effect algebras and sequential products in GPT context
- SageMath documentation, "Jordan Algebras," doc.sagemath.org/html/en/reference/algebras/sage/algebras/jordan_algebra.html
- SymPy documentation, "Matrices," docs.sympy.org/latest/modules/matrices/matrices.html -- Symbolic matrix operations including noncommutative support

## Sources

- SageMath Jordan algebra module: [doc.sagemath.org](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/jordan_algebra.html) -- Verified 2026-03-20, Release 10.6
- SymPy noncommutative support: [github.com/sympy/sympy](https://github.com/sympy/sympy) -- Verified active, Issue #18367 documents commutative=False behavior
- Orlitzky EJA draft: [michael.orlitzky.com](https://michael.orlitzky.com/documents/books/euclidean_jordan_algebras_for_optimization.pdf) -- Not yet integrated into SageMath
- van de Wetering (2019): [arXiv:1803.11139](https://arxiv.org/abs/1803.11139) -- Published in J. Math. Phys.
- Three types of SEAs: [arXiv:2004.12749](https://arxiv.org/abs/2004.12749) -- Published in Quantum journal
- GPT introduction: [arXiv:2103.07469](https://arxiv.org/abs/2103.07469) -- Published in Physics Reports
