# Order Zero Condition for the Self-Modeling Spectral Triple

% ASSERT_CONVENTION: natural_units=N/A, commutation_convention=[A,B]=AB-BA, inner_product=linear_in_second_argument

**References:**
- Connes 1995, J. Math. Phys. 36, 6194 (order zero condition definition)
- van Suijlekom 2024, NCG and Particle Physics, 2nd ed., Ch. 2-4 (opposite algebra computation)
- Paper 5 (M_n(C)^sa, J = dagger, sequential product)
- Paper 6 (SWAP operator P, doubled space H, J definition)

## Setup

**Algebra.** A = M_n(C) for general n >= 1.

**Hilbert space.** H = C^{n^2}\_p + C^{n^2}\_{ap} (particle + antiparticle sectors), where each sector is C^n tensor C^n. Elements are pairs (psi, chi). dim(H) = 2n^2.

**Conventions.**
- P (SWAP): P(v tensor w) = w tensor v, with P^2 = I, P real and self-adjoint
- C (conjugation): C(v) = v-bar (componentwise conjugation in computational basis)
- J (real structure): J(psi, chi) = (P(conj(chi)), P(conj(psi))), antilinear
- gamma (chirality): gamma(psi, chi) = (P psi, -P chi)
- Matrix units: (E_{ij})_{kl} = delta_{ik} delta_{jl}
- Opposite algebra: pi_o(b) = J pi(b*) J^{-1} where b* = b^dagger

**KO-dimension 6 signs verified:** J^2 = +1 (epsilon = +1), J gamma = -gamma J (epsilon'' = -1).

## Derivation of pi_o(b) at General n

### Step 1: Algebra action pi(a) on H

**Naive action:** pi(a)(psi, chi) = ((a tensor I_n)psi, (a tensor I_n)chi).

In block form: pi(a) = diag(a tensor I_n, a tensor I_n).

This is a *-representation: pi(ab) = pi(a)pi(b), pi(a*) = pi(a)^dagger, pi(I) = I.

### Step 2: J as antilinear operator

J(psi, chi) = (P(conj(chi)), P(conj(psi)))

where conj denotes componentwise conjugation. J is antilinear:

J(alpha psi, alpha chi) = (P(conj(alpha chi)), P(conj(alpha psi)))
= (alpha* P(conj(chi)), alpha* P(conj(psi))) = alpha* J(psi, chi).

### Step 3: Verify J^2 = I and J^{-1} = J

J(J(psi, chi)) = J(P(conj(chi)), P(conj(psi)))
= (P(conj(P(conj(psi)))), P(conj(P(conj(chi)))))

Since P is a real matrix (permutation matrix in the computational basis), conj(P(v)) = P(conj(v)) for any v. Therefore:

= (P(P(conj(conj(psi)))), P(P(conj(conj(chi)))))
= (P^2(psi), P^2(chi))
= (psi, chi).

So J^2 = I and J^{-1} = J.

### Step 4: Compute pi_o(b) = J pi(b*) J^{-1} step-by-step

For b in M_n(C), b* = b^dagger.

**Step 4a.** Apply J^{-1} = J to input (psi, chi):

J(psi, chi) = (P(conj(chi)), P(conj(psi)))

**Step 4b.** Apply pi(b*) to the result:

pi(b^dagger)(P(conj(chi)), P(conj(psi)))
= ((b^dagger tensor I)(P(conj(chi))), (b^dagger tensor I)(P(conj(psi))))

**Step 4c.** Apply J to the result of Step 4b:

J((...), (...)) = (P(conj((b^dagger tensor I)(P(conj(psi))))), P(conj((b^dagger tensor I)(P(conj(chi))))))

The particle sector output depends on psi; the antiparticle sector output depends on chi. Computing each separately.

### Step 5: Evaluate P(conj((b^dagger tensor I)(P(conj(v))))) component-by-component

Let v = sum_{ij} V_{ij} e_i tensor e_j.

1. conj(v) = sum_{ij} V_{ij}* e_i tensor e_j

2. P(conj(v)) = sum_{ij} V_{ij}* e_j tensor e_i

3. (b^dagger tensor I)(P(conj(v))) = sum_{ij} V_{ij}* (b^dagger e_j) tensor e_i
   = sum_{ijk} V_{ij}* (b^dagger)_{kj} e_k tensor e_i
   = sum_{ijk} V_{ij}* b_{jk}* e_k tensor e_i

   (using (b^dagger)_{kj} = b_{jk}*.)

4. conj(step 3 result) = sum_{ijk} V_{ij} b_{jk} e_k tensor e_i

   **KEY ANTILINEARITY STEP:** The conjugation from J converts b_{jk}* (from b^dagger) to b_{jk} (entries of b itself).

5. P(step 4 result) = sum_{ijk} V_{ij} b_{jk} e_i tensor e_k

Reading off the (i,k) matrix entry of the result: R_{ik} = sum_j V_{ij} b_{jk} = (Vb)_{ik}.

**Result:** P(conj((b^dagger tensor I)(P(conj(v))))) corresponds to matrix V * b (right multiplication by b).

### Step 6: Express as tensor product operator

Right multiplication by b on the matrix V corresponds to the tensor product operator I_n tensor b^T.

**Proof:** (I_n tensor M)v has (i,k) entry = sum_j V_{ij} M_{kj}. Setting this equal to (Vb)_{ik} = sum_j V_{ij} b_{jk} requires M_{kj} = b_{jk}, i.e., M = b^T.

### Step 7: Result for pi_o(b)

Combining Steps 5-6 for both sectors:

$$\boxed{\pi_o(b)(\psi, \chi) = ((I_n \otimes b^T)\psi, \; (I_n \otimes b^T)\chi)}$$

In block form:

$$\pi_o(b) = \mathrm{diag}(I_n \otimes b^T, \; I_n \otimes b^T)$$

**Physical interpretation:** J's antilinearity converts the left algebra action (b^dagger on first tensor factor) into a transpose action on the second tensor factor (b^T). The SWAP operator P permutes the tensor factors during this conversion. The chain of identities is:

b^dagger has entries (b^dagger)_{kj} = b_{jk}* --> conj converts b_{jk}* to b_{jk} --> SWAP rearranges indices --> result is I tensor b^T.

### Step 8: Verification that pi_o is a *-representation of A^{op}

**(a) Multiplicativity (as representation of A^{op}):**

pi_o(a) pi_o(b) = diag(I tensor a^T b^T, I tensor a^T b^T)

pi_o(ba) = diag(I tensor (ba)^T, I tensor (ba)^T) = diag(I tensor a^T b^T, I tensor a^T b^T)

So pi_o(a) pi_o(b) = pi_o(ba) = pi_o(a \*\_{op} b). Confirmed: pi_o is a homomorphism from A^{op}.

**(b) *-preserving:**

pi_o(a^dagger) = diag(I tensor (a^dagger)^T, ...) = diag(I tensor conj(a), ...)

pi_o(a)^dagger = diag((I tensor a^T)^dagger, ...) = diag(I tensor conj(a), ...)

(since (a^T)^dagger = conj(a).)

Therefore pi_o(a*) = pi_o(a)^dagger. Confirmed.

**(c) Identity:**

pi_o(I_n) = diag(I_n tensor I_n, I_n tensor I_n) = I_{2n^2}. Confirmed.

### Step 9: Limiting case n = 1

For n = 1: M_1(C) = C. b is a scalar, b^T = b.

pi_o(b) = diag(b, b) = b * I_2.
pi(a) = diag(a, a) = a * I_2.

These commute trivially. Consistent.

### Step 10: Antilinearity tracking audit

At every step where J acts:
- Step 4a: J(psi, chi) -> conjugation of chi, psi applied. Antilinear.
- Step 4c: J acts on a vector containing b^dagger entries -> conjugation converts b_{jk}* to b_{jk}. This is the KEY antilinearity step.
- No step treats J as a linear operator.
- The critical identity: conj(b^dagger) = conj((b^T)*) = b^T. Treating J as linear would give conj(b) instead of b^T -- WRONG.
