# Phase 39: Spontaneous Symmetry Breaking Proof

% ASSERT_CONVENTION: natural_units=natural, metric_signature=riemannian,
%   jordan_product=(1/2)(ab+ba),
%   clifford_normalization={T_a,T_b}=(1/2)delta_{ab}I,
%   coupling_convention=J_gt_0_antiferro

## 0. Correction: SSB Pattern Clarification

The Phase 38 handoff document and the roadmap stated the SSB pattern as "F_4 -> Spin(9)" with target space OP^2 (dim 16) and 16 broken generators. This conflated two distinct symmetry-breaking stages:

1. **Explicit breaking** (by construction of H_eff): F_4 -> Spin(9). The Peirce projection that defines the T_a operators breaks F_4 to Spin(9). This is not spontaneous -- it is built into the Hamiltonian.

2. **Spontaneous breaking** (by ground state selection in thermodynamic limit): Spin(9) -> Spin(8). The ordered state selects a direction n in S^8 subset R^9, breaking the Spin(9) symmetry of H_eff down to its stabilizer Spin(8).

The sigma model target space for the spontaneous breaking is S^8 = Spin(9)/Spin(8) (dim 8), NOT OP^2 = F_4/Spin(9) (dim 16).

This distinction is physically critical: the Goldstone modes, infrared bounds, and universality class are all determined by the spontaneous breaking pattern Spin(9) -> Spin(8), not by the explicit breaking F_4 -> Spin(9).

## 1. SSB Pattern Resolution

### 1.1 Symmetry of H_eff

From Phase 38:

$$
H_{\text{eff}} = J \sum_{\langle ij \rangle} \sum_{a=0}^{8} T_a^{(i)} \otimes T_a^{(j)}, \quad \{T_a, T_b\} = \tfrac{1}{2}\delta_{ab} I_{16}
$$

Phase 38 established (three independent proofs):
- [H_2, G_{ab}^{total}] = 0 for all 36 Spin(9) generators (exact)
- [H_2, J_u^{total}] != 0 (||comm|| = 24.0) for the F_4 generator J_u outside Spin(9)
- Spectrum degeneracies {1, 9, 36, 84, 126} = {C(9,k)} match Spin(9) irreps exclusively

**Therefore: The symmetry group of H_eff is G = Spin(9) (dim 36).**

The F_4 -> Spin(9) breaking is explicit (encoded in the Hamiltonian via the Peirce projection).

### 1.2 Ground State and Order Parameter

From Phase 38 (Plan 01):
- Ground state: Lambda^1(V_9) (vector representation of Spin(9), dim 9)
- Sector: symmetric (ferromagnetic)
- Energy: E_0 = -7/4 J

The order parameter space is the set of expectation values of the local spin operator. The on-site operator is the 9-component vector (T_0, T_1, ..., T_8). In the classical limit, the ordered state selects a unit vector n in S^8 subset R^9 such that:

$$
\langle T_a^{(i)} \rangle \to S_{\text{eff}} \cdot n_a \quad \text{for all sites } i
$$

where S_eff is the effective spin magnitude and n = (n_0, ..., n_8) is a unit vector in R^9.

### 1.3 Stabilizer of the Ordered State

The ordered state selects n in S^8 subset R^9. The stabilizer of a nonzero vector in R^9 under the Spin(9) action (via the vector representation) is:

$$
\text{Stab}_{\text{Spin}(9)}(n) = \text{Spin}(8) \quad (\dim = 28)
$$

**Proof:** Spin(9) acts on R^9 via its vector representation. This is the double cover of the SO(9) action on R^9. The stabilizer of any nonzero vector under SO(9) is SO(8). Taking the double cover: Stab_{Spin(9)}(n) = Spin(8). (Standard result: the fiber of the quotient map Spin(9) -> S^8 = Spin(9)/Spin(8) is Spin(8).)

### 1.4 Spontaneous SSB Pattern

$$
\boxed{G = \text{Spin}(9) \xrightarrow{\text{spontaneous}} H = \text{Spin}(8)}
$$

- Number of broken generators: dim(Spin(9)) - dim(Spin(8)) = 36 - 28 = 8
- Goldstone manifold: Spin(9)/Spin(8) = S^8 (8-sphere, dim = 8)

**SELF-CRITIQUE CHECKPOINT (step 1):**
1. SIGN CHECK: No sign-carrying operations. N/A.
2. FACTOR CHECK: No numerical factors introduced. N/A.
3. CONVENTION CHECK: Spin(9) from Phase 38 convention lock (Cl(9,0), positive definite). Consistent.
4. DIMENSION CHECK: dim(Spin(9)) = C(9,2) = 36, dim(Spin(8)) = C(8,2) = 28, 36-28 = 8 = dim(S^8). Consistent.

### 1.5 Consistency Check: dim(G/H) vs dim(S^n)

dim(S^8) = 8. dim(Spin(9)/Spin(8)) = 36 - 28 = 8. Check.

The 8-sphere S^8 is the homogeneous space Spin(9)/Spin(8), confirming the Goldstone manifold is S^8.

### 1.6 Alternative Check: Could F_4/Spin(8) Be Relevant?

F_4/Spin(8) would have dimension 52 - 28 = 24. This is NOT a standard symmetric space. The quotient F_4/Spin(8) is not a well-defined coset space because Spin(8) is not a maximal subgroup of F_4 (it sits inside Spin(9) which is maximal in F_4).

The physics is clear: the sigma model describes fluctuations of the order parameter around the ordered state. The order parameter lives in the spontaneously broken symmetry manifold G/H = Spin(9)/Spin(8) = S^8. The explicit breaking F_4 -> Spin(9) is irrelevant for the low-energy dynamics.

### 1.7 Full Symmetry Breaking Chain

$$
F_4 \xrightarrow{\text{explicit}} \text{Spin}(9) \xrightarrow{\text{spontaneous}} \text{Spin}(8)
$$

| Stage | Breaking | Mechanism | Generators | Target |
|-------|----------|-----------|------------|--------|
| Explicit | F_4 -> Spin(9) | Peirce projection in H_eff | 16 | OP^2 (not physical for sigma model) |
| Spontaneous | Spin(9) -> Spin(8) | Ground state order in thermo. limit | 8 | S^8 (physical Goldstone manifold) |

## 2. Classical SSB via FSS Infrared Bounds

### 2.1 Classical Model Formulation

The classical limit of the quantum model on Z^d replaces quantum states by classical spins. Each site i carries a unit vector n_i in S^8 subset R^9 (|n_i| = 1). The classical action is:

$$
S_{\text{cl}} = -\beta J \sum_{\langle ij \rangle} \mathbf{n}_i \cdot \mathbf{n}_j
$$

where the sum is over nearest-neighbor bonds on Z^d. This is the classical O(9) model with S^8 target space, or equivalently the classical Spin(9)/Spin(8) sigma model.

Note: J > 0 and the ferromagnetic ground state means the energy is minimized when n_i = n_j for all i,j (uniform alignment). The minus sign ensures this.

### 2.2 Reflection Positivity for the Classical S^8 Model

We verify the FSS conditions (Froehlich-Simon-Spencer 1976; Biskup 2006 conditions RP1-RP5) for the classical S^8 model on Z^d:

**RP1 (Bipartite lattice):** Z^d is bipartite with checkerboard sublattices A = {x : sum x_k even}, B = {x : sum x_k odd}. Every nearest-neighbor bond connects A to B. (Phase 38, Section 2.2.)

**RP2 (Reflection plane):** Choose a hyperplane Sigma_mu perpendicular to axis mu, bisecting bonds between the hyperplanes x_mu = 0 and x_mu = 1. The lattice splits into left and right halves Lambda_L and Lambda_R connected by bonds crossing Sigma_mu.

**RP3 (On-site measure):** Each spin n_i takes values in S^8 with the uniform (Haar) measure d(mu)(n) = (surface area of S^8)^{-1} d(Omega_8)(n). This measure is SO(9)-invariant (and hence Spin(9)-invariant). It is also invariant under n -> -n (inversion symmetry).

**RP4 (Reflection-positive interaction):** The nearest-neighbor coupling n_i . n_j for a bond crossing Sigma_mu can be written as:

$$
\exp\left(\beta J \sum_{a=0}^{8} n_i^a n_j^a \right) = \exp\left(\beta J \, \mathbf{n}_i \cdot \mathbf{n}_j\right)
$$

where i is in Lambda_L and j = theta(i) is its reflection in Lambda_R. The inner product is a sum of products of left-side and right-side variables: n_i^a * n_j^a = (left function) * (right function). By the standard FSS argument, the Boltzmann weight for a single reflected bond factorizes as:

$$
e^{\beta J \, \mathbf{n}_i \cdot \theta(\mathbf{n}_i)} = e^{\beta J \sum_a n_i^a \, n_{\theta(i)}^a}
$$

This has the form $\sum_k f_k(\text{left}) \overline{f_k(\text{right})}$ after expanding the exponential (each term in the Taylor expansion is a product of left and right factors). By the Schur product theorem, the product over reflected bonds preserves reflection positivity.

**RP5 (Inner product type interaction):** The interaction n_i . n_j = sum_a n_i^a n_j^a is of inner-product type (it equals the O(9)-invariant inner product on R^9). This is the canonical form required by the FSS framework.

**Conclusion:** All RP conditions are satisfied. The classical S^8 model on Z^d is reflection-positive.

**SELF-CRITIQUE CHECKPOINT (step 2):**
1. SIGN CHECK: The Boltzmann weight is exp(+beta J n.n) with beta,J > 0. Ferromagnetic alignment gives positive exponent. Correct.
2. FACTOR CHECK: No factors of 2, pi, hbar, c introduced. The Haar measure normalization cancels from expectation values.
3. CONVENTION CHECK: J > 0 convention matches coupling_convention in convention lock.
4. DIMENSION CHECK: [beta J n.n] = [1/energy * energy * dimensionless] = [dimensionless]. Exponent is dimensionless. Correct.

### 2.3 Infrared Bound via Gaussian Domination

**Theorem (FSS 1976, adapted to O(N) model with N=9):** For the classical O(9) model on Z^d with reflection-positive nearest-neighbor interaction, the Fourier-space 2-point function satisfies:

$$
\hat{G}^{ab}(\mathbf{k}) \leq \frac{\delta^{ab}}{2\beta J \, E(\mathbf{k})}
$$

where:
- $\hat{G}^{ab}(\mathbf{k}) = \sum_x e^{i\mathbf{k}\cdot\mathbf{x}} \langle n_0^a n_x^b \rangle$ is the Fourier-transformed 2-point function
- $E(\mathbf{k}) = \sum_{\mu=1}^{d} (1 - \cos k_\mu)$ is the lattice Laplacian eigenvalue (with our normalization convention: NO factor of 2)
- The bound follows from Gaussian domination: the Gibbs measure is bounded above by a Gaussian with covariance $(2\beta J \cdot E(\mathbf{k}))^{-1}$

**Derivation sketch (FSS method):**

Consider the partition function $Z(h) = \int \prod_i d\mu(n_i) \exp(\beta J \sum_{\langle ij \rangle} n_i \cdot n_j + \sum_i h_i \cdot n_i)$ with external field h. Gaussian domination states that $Z(h) \leq Z(0) \exp(||h||^2 / (4\beta J z))$ where z is coordination number. This is proved using reflection positivity: the ratio Z(h)/Z(0) is bounded by the partition function of a free (Gaussian) theory.

Taking two functional derivatives with respect to h and setting h = 0 yields the infrared bound on the 2-point function.

The key constant in the bound: The on-site average $\langle n_i^a n_i^b \rangle = \frac{1}{N}\delta^{ab}$ where N = 9 (by SO(9) invariance of the Haar measure on S^8, each component gets equal weight). This factor enters through the sum rule but NOT directly in the infrared bound.

### 2.4 Sum Rule and Proof of Long-Range Order

**Sum rule:** From the constraint |n_i|^2 = 1:

$$
\sum_a \frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} \hat{G}^{aa}(\mathbf{k}) \, d^d k = \langle |\mathbf{n}_0|^2 \rangle = 1
$$

Therefore the trace over components:

$$
\frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} \sum_a \hat{G}^{aa}(\mathbf{k}) \, d^d k = 1
$$

**Combining with the infrared bound:**

$$
\hat{G}^{aa}(\mathbf{k}) \leq \frac{1}{2\beta J \, E(\mathbf{k})} \quad \text{for each } a
$$

Summing over all N = 9 components except one direction (say a = 0, the ordered direction), the infrared bound gives:

$$
\sum_{a \neq 0} \frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} \hat{G}^{aa}(\mathbf{k}) \, d^d k \leq \frac{N-1}{2\beta J} I_d
$$

where:

$$
I_d = \frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} \frac{d^d k}{E(\mathbf{k})} = \frac{1}{(2\pi)^d} \int_{[-\pi,\pi]^d} \frac{d^d k}{\sum_\mu (1 - \cos k_\mu)}
$$

The sum rule gives:

$$
\frac{1}{(2\pi)^d} \int \hat{G}^{00}(\mathbf{k}) \, d^d k = 1 - \sum_{a \neq 0} \frac{1}{(2\pi)^d} \int \hat{G}^{aa}(\mathbf{k}) \, d^d k \geq 1 - \frac{(N-1)}{2\beta J} I_d
$$

Now, separating the k = 0 mode from the integral:

$$
\frac{1}{(2\pi)^d} \int \hat{G}^{00}(\mathbf{k}) \, d^d k = m_0^2 + \text{(integral over k} \neq 0)
$$

where $m_0^2 = \lim_{|x|\to\infty} \langle n_0^0 n_x^0 \rangle$ is the long-range order parameter. In a finite volume L^d, the k=0 contribution is $L^{-d} \hat{G}^{00}(0)$. In the thermodynamic limit:

$$
m_0^2 = \lim_{L\to\infty} L^{-d} \hat{G}^{00}(0) \geq 1 - \frac{(N-1)}{2\beta J} I_d - \frac{1}{(2\pi)^d} \int_{k \neq 0} \frac{dk}{2\beta J \, E(k)}
$$

The integral over k != 0 is bounded by $I_d / (2\beta J)$ (one component's contribution). So:

$$
m_0^2 \geq 1 - \frac{N}{2\beta J} I_d = 1 - \frac{9}{2\beta J} I_d
$$

This is positive when:

$$
\beta J > \frac{N}{2} I_d = \frac{9}{2} I_d
$$

**SELF-CRITIQUE CHECKPOINT (step 3):**
1. SIGN CHECK: m_0^2 >= 1 - (positive term). The bound gives positive m_0^2 when beta*J is large enough. Correct sign structure.
2. FACTOR CHECK: N = 9 components. The bound uses N/2 = 9/2. The factor of 2 comes from the infrared bound constant 1/(2*beta*J). Consistent with {T_a,T_b} = (1/2)*delta*I normalization.
3. CONVENTION CHECK: E(k) = sum(1-cos k_mu) without factor of 2. Matches plan specification.
4. DIMENSION CHECK: [beta*J] = [1/energy * energy] = [dimensionless]. [I_d] = [dimensionless]. [m_0^2] = [dimensionless]. All consistent.

### 2.5 Critical Temperature and Classical SSB Theorem

**Definition:** The critical inverse temperature for classical long-range order is:

$$
\beta_c J = \frac{N}{2} I_d = \frac{9}{2} I_d
$$

For d = 3: I_3 is the Watson integral (to be computed numerically in Task 2). The known value is I_3 = W_3 ~ 0.5055 (with our normalization E(k) = sum(1-cos k_mu)). Therefore:

$$
\beta_c J = \frac{9}{2} \times 0.5055 \approx 2.275
$$

**Theorem (Classical SSB).** For d >= 3, the classical O(9) model on Z^d with Hamiltonian S_cl = -beta J sum_{<ij>} n_i . n_j and n_i in S^8 satisfies:

For beta > beta_c = (9/2) I_d / J, there exists delta > 0 such that:

$$
\lim_{|x|\to\infty} \langle n_0^a n_x^a \rangle \geq \delta > 0 \quad \text{(for the ordered component } a)
$$

The long-range order spontaneously breaks Spin(9) -> Spin(8), with the ordered state selecting a direction n in S^8.

**Proof:** By FSS infrared bounds (Section 2.3-2.4). The key ingredients are:
1. Reflection positivity of the classical S^8 model on Z^d (Section 2.2)
2. Infrared bound: G_hat(k) <= 1/(2*beta*J*E(k))
3. Sum rule: integral of G_hat = 1
4. Finiteness of I_d for d >= 3

### 2.6 Mermin-Wagner Check (d <= 2)

For d = 1: E(k) = 1 - cos k. I_1 = (1/2pi) int_{-pi}^{pi} dk/(1-cos k) = infinity (the integrand diverges at k=0 as 1/k^2).

For d = 2: E(k) = (1-cos k_1) + (1-cos k_2). I_2 = (1/(2pi)^2) int dk_1 dk_2 / ((1-cos k_1)+(1-cos k_2)). This diverges logarithmically at k -> 0 (the integrand goes as 1/|k|^2 in 2D, and int d^2k / |k|^2 ~ int dr/r = log r -> infinity).

Therefore: For d <= 2, I_d = infinity, and the infrared bound cannot force long-range order regardless of beta. This is consistent with the Mermin-Wagner theorem, which forbids spontaneous breaking of continuous symmetries in d <= 2 for short-range interactions.

For d >= 3: I_d is finite (the integrand goes as 1/|k|^2, and int d^dk/|k|^2 converges for d >= 3). Long-range order is possible.

**Summary:**

| d | I_d | LRO possible? | Consistent with MW? |
|---|-----|---------------|---------------------|
| 1 | divergent | No | Yes |
| 2 | divergent (log) | No | Yes |
| 3 | W_3 ~ 0.5055 | Yes, for beta J > 9/2 * I_3 ~ 2.275 | Yes (MW only forbids d <= 2) |
| >= 4 | finite, < I_3 | Yes, at lower beta_c | Yes |

## 3. (Continued in Task 2: BCS Quantum Lift)

---

_Phase: 39-spontaneous-symmetry-breaking-and-universality-class, Plan: 01, Task 1_
_Completed: 2026-03-30_
