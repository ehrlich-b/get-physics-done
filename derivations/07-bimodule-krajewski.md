# Bimodule Decomposition and Krajewski Diagram for M_n(C) Spectral Triple

% ASSERT_CONVENTION: commutation_convention=[A,B]=AB-BA, inner_product=linear_in_second_argument, opposite_algebra=pi_o(b)=J_pi(b*)_J^{-1}

**References:**
- van Suijlekom 2024, NCG and Particle Physics, 2nd ed., Ch. 3-4 (bimodule decomposition, Krajewski diagram)
- Krajewski 1997, hep-th/9701081 (Krajewski diagram formalism for finite spectral triples)
- Barrett 2015, arXiv:1502.05383 (matrix geometry classification, H = V tensor M_n(C))
- Chamseddine-Connes 2008, arXiv:0706.3688 (dim(H_F) = k^2 classification)
- Paper 5 (M_n(C)^sa algebra)
- Paper 6 (doubled space H, J, gamma)

## Setup

**Algebra.** A = M_n(C), simple.

**Hilbert space.** H = C^{n^2}_p + C^{n^2}_{ap} = C^{2n^2}, where each sector is C^n tensor C^n.

**Representations (established in Plan 13-01, verified in Plan 13-02):**
- pi(a) = diag(a tensor I_n, a tensor I_n) — acts on first tensor factor
- pi_o(b) = diag(I_n tensor b^T, I_n tensor b^T) — acts on second tensor factor

**Operators (established in Plan 13-02):**
- gamma = diag(P, -P) where P = SWAP
- J(psi, chi) = (P conj(chi), P conj(psi)), antilinear
- J^2 = +1, J gamma = -gamma J (KO-dim 6)

## Step 1: Confirm pi and pi_o match standard bimodule actions

The A-A^o bimodule structure on H is:
- Left action: a . xi = pi(a) xi, i.e., a acts as a tensor I on each sector
- Right action: xi . b^o = pi_o(b) xi, i.e., b^o acts as I tensor b^T on each sector

Within each sector C^n tensor C^n:
- Left action of a: (a tensor I)(v tensor w) = (av) tensor w
- Right action of b^o: (I tensor b^T)(v tensor w) = v tensor (b^T w)

The right action by b^o = I tensor b^T is equivalent to the bimodule right action (v tensor w) . b^o = v tensor (b^T w).

**Cross-check with standard bimodule definition:** The unique irreducible M_n(C)-M_n(C)^o bimodule is C^n tensor (C^n)* with:
- a . (v tensor f) = (av) tensor f
- (v tensor f) . b^o = v tensor (f . b) = v tensor (b^T f) [since f . b in the dual means f(b . -) = f(b(-)) which transposes b]

Under the identification (C^n)* = C^n (using the standard inner product, linear in second argument), f . b corresponds to b^T f. This matches our pi_o(b) = I tensor b^T exactly.

SELF-CRITIQUE CHECKPOINT (Step 1):
1. SIGN CHECK: No sign changes. Expected: 0. Actual: 0.
2. FACTOR CHECK: No factors of 2, pi, hbar, c introduced.
3. CONVENTION CHECK: Still using [A,B] = AB - BA, linear-in-second inner product. Transpose convention consistent.
4. DIMENSION CHECK: a tensor I is n x n tensor n x n = n^2 x n^2. Acts on C^{n^2}. Consistent.

## Step 2: Bimodule structure of each sector

Each sector C^{n^2} = C^n tensor C^n carries:
- Left M_n(C)-action: a tensor I
- Right M_n(C)^o-action: I tensor b^T

**Claim:** Each sector is one copy of the unique irreducible M_n(C)-M_n(C)^o bimodule.

**Proof:** M_n(C) tensor M_n(C)^{op} = M_n(C) tensor M_n(C) (as algebras, since M_n(C)^{op} = M_n(C)) = M_{n^2}(C). The algebra M_{n^2}(C) is simple, so it has a unique irreducible module, namely C^{n^2}. The left-right action (a tensor I)(I tensor b^T) = a tensor b^T generates all of M_{n^2}(C) as a,b range over M_n(C) (because {a tensor b^T : a, b in M_n(C)} spans M_n(C) tensor M_n(C) = M_{n^2}(C)). Therefore C^{n^2} is irreducible as an M_n(C)-M_n(C)^o bimodule.

**Result:**
- Particle sector C^{n^2}_p: one copy of the irreducible bimodule
- Antiparticle sector C^{n^2}_{ap}: one copy of the irreducible bimodule
- Total: H = 2 x C^{n^2} as M_n(C)-M_n(C)^o bimodules

The multiplicity is m = 2.

## Step 3: Gamma eigenspace decomposition within each sector

gamma = diag(P, -P) where P is the SWAP operator on C^n tensor C^n.

**SWAP eigenspaces:** P has eigenvalues +1 and -1:
- Sym^2(C^n) = {v tensor w + w tensor v : v, w in C^n} has P = +1, dim = n(n+1)/2
- wedge^2(C^n) = {v tensor w - w tensor v : v, w in C^n} has P = -1, dim = n(n-1)/2

**Particle sector:** gamma|_p = P, so:
- gamma = +1 subspace: Sym^2_p(C^n), dim = n(n+1)/2
- gamma = -1 subspace: wedge^2_p(C^n), dim = n(n-1)/2

**Antiparticle sector:** gamma|_{ap} = -P, so:
- gamma = +1 subspace: wedge^2_{ap}(C^n), dim = n(n-1)/2 (P = -1, negated to +1)
- gamma = -1 subspace: Sym^2_{ap}(C^n), dim = n(n+1)/2 (P = +1, negated to -1)

**Dimension check:**
- dim(gamma = +1) = n(n+1)/2 + n(n-1)/2 = n^2
- dim(gamma = -1) = n(n-1)/2 + n(n+1)/2 = n^2
- Total: n^2 + n^2 = 2n^2. Correct.

SELF-CRITIQUE CHECKPOINT (Step 3):
1. SIGN CHECK: gamma|_{ap} = -P, so P = +1 maps to gamma = -1 (negation). Expected 2 sign flips (particle vs antiparticle). Actual: 2.
2. FACTOR CHECK: No new factors.
3. CONVENTION CHECK: gamma = diag(P, -P) from Plan 13-02. Consistent.
4. DIMENSION CHECK: n(n+1)/2 + n(n-1)/2 = (n^2+n+n^2-n)/2 = n^2. Correct.

## Step 4: Gamma-refined bimodule decomposition

The full gamma-refined decomposition of H:

$$H = \underbrace{\text{Sym}^2_p(+1)}_{\dim = n(n+1)/2} \oplus \underbrace{\wedge^2_p(-1)}_{\dim = n(n-1)/2} \oplus \underbrace{\wedge^2_{ap}(+1)}_{\dim = n(n-1)/2} \oplus \underbrace{\text{Sym}^2_{ap}(-1)}_{\dim = n(n+1)/2}$$

Dimensions: n(n+1)/2 + n(n-1)/2 + n(n-1)/2 + n(n+1)/2 = 2n^2. Check.

**Important:** These are NOT irreducible as bimodules. The Sym^2 and wedge^2 subspaces are NOT preserved by the bimodule actions (a tensor I and I tensor b^T do not preserve the symmetry/antisymmetry of a tensor). They are gamma-eigenspaces, providing a finer grading on H, but the irreducible bimodule decomposition remains H = 2 x C^{n^2}.

**Why the gamma-grading matters:** In NCG, the Dirac operator D must satisfy D: H_+ -> H_- (where H_+/- are gamma = +/-1 eigenspaces) for an even spectral triple. The gamma-grading constrains which matrix entries of D are nonzero, which is critical for Phase 14.

## Step 5: Krajewski diagram

**Krajewski diagram rules** (Krajewski 1997, van Suijlekom 2024 Ch. 3):
- Vertices: one per irreducible representation of A (as a *-algebra)
- Since A = M_n(C) is simple, it has exactly ONE irreducible representation: the fundamental C^n
- A vertex is placed at position (i, j) where i labels the left irrep and j labels the right irrep (from A^o)
- Since there is one irrep, the diagram has one vertex type at position (n, n)
- Multiplicity: the number of times the irreducible bimodule C^n tensor (C^n)* appears in H gives the multiplicity at vertex (n, n)
- Our multiplicity = 2 (one from each sector)

**The Krajewski diagram:**

```
        A^o irreps
        |
        n
        |
  A     *----- m = 2
irreps  |
        n
        |

Vertex (n, n): multiplicity m = 2
```

More precisely, since A = M_n(C) has one irrep (the fundamental), the Krajewski diagram is:

```
                  (C^n)*
                    |
   C^n  -----  (n,n): m=2, graded
                    |

Gamma decoration:
  Sector 1 (particle):   gamma_1 = P  (eigenvalues: +1 on Sym^2, -1 on wedge^2)
  Sector 2 (antiparticle): gamma_2 = -P (eigenvalues: +1 on wedge^2, -1 on Sym^2)

J-connection:
  J maps Sector 1 <-> Sector 2 (particle-antiparticle exchange)
  J^2 = +1 (KO-dim 6)
```

**Detailed vertex structure:**

The single vertex at (n, n) has multiplicity 2. The two copies are distinguished by:
1. gamma eigenvalue assignment (P vs -P)
2. J connects them (J swaps particle and antiparticle sectors)

In the Krajewski diagram formalism:
- The vertex (n, n) is occupied by a 2x2 multiplicity matrix
- gamma acts on the multiplicity space as sigma_3 = diag(+1, -1) (up to the internal Sym^2/wedge^2 decomposition)
- J acts on the multiplicity space as sigma_1 = [[0,1],[1,0]] (swapping the two copies)
- The constraint J gamma = -gamma J is satisfied: sigma_1 * sigma_3 = -sigma_3 * sigma_1. Verified.

## Step 6: Barrett isomorphism

**Barrett (2015) matrix geometry framework:** For A = M_n(C), the Hilbert space of a finite spectral triple takes the form H = V tensor M_n(C) where V is a "spinor space" and M_n(C) is viewed as a Hilbert space with inner product (X, Y) = Tr(X^dagger Y).

**Our case:** Each sector has C^n tensor C^n. The Barrett isomorphism is:

$$C^n \otimes C^n \xrightarrow{\sim} M_n(\mathbb{C}) \quad \text{via} \quad v \otimes w \mapsto v \cdot w^T$$

This is a vector space isomorphism (dim = n^2 on both sides).

**Verification of bimodule actions under this identification:**

Under v tensor w <-> X = v w^T:

- Left action: a . (v tensor w) = (av) tensor w <-> (av) w^T = a (v w^T) = aX
  $\therefore$ pi(a) corresponds to LEFT multiplication X -> aX

- Right action: (v tensor w) . b^o = v tensor (b^T w) <-> v (b^T w)^T = v w^T b = X b
  $\therefore$ pi_o(b) corresponds to RIGHT multiplication X -> Xb

**Physical interpretation:** The M_n(C) spectral triple has H_sector = M_n(C) as a Hilbert space, with the algebra acting by left and right multiplication. The particle and antiparticle sectors each carry one copy of this "matrix Hilbert space."

**Barrett's classification:** For the simplest case with V = C^1 (trivial spinor space, since our multiplicity per sector is 1 irreducible bimodule), we have:

$$H_{\text{sector}} = \mathbb{C}^1 \otimes M_n(\mathbb{C}) = M_n(\mathbb{C})$$

The full Hilbert space H = 2 * M_n(C) with the two sectors.

SELF-CRITIQUE CHECKPOINT (Step 6):
1. SIGN CHECK: No signs to track. Expected: 0. Actual: 0.
2. FACTOR CHECK: No new factors.
3. CONVENTION CHECK: v w^T has (vw^T)_{ij} = v_i w_j. Under pi(a): a(vw^T) = (av)w^T, (av)_i = sum_k a_{ik} v_k. Under pi_o(b): (vw^T)b = v(w^T b) = v(b^T w)^T. So pi_o(b) gives right multiplication by b, and the tensor product operator is I tensor b^T. Consistent.
4. DIMENSION CHECK: M_n(C) has dim = n^2 as vector space. H = 2 * n^2 = 2n^2. Correct.

## Step 7: Complete bimodule structure summary

| Property | Value |
|---|---|
| Algebra A | M_n(C), simple |
| Hilbert space H | C^{2n^2} = C^{n^2}_p + C^{n^2}_{ap} |
| Irreducible A-A^o bimodule | C^n tensor (C^n)* = C^{n^2} (unique) |
| Multiplicity in H | m = 2 (one per sector) |
| Dim per irreducible summand | n^2 |
| Dim total | 2n^2 |
| Gamma on particle sector | P (SWAP): eigenvalues +1 on Sym^2, -1 on wedge^2 |
| Gamma on antiparticle sector | -P: eigenvalues +1 on wedge^2, -1 on Sym^2 |
| Dim(gamma = +1) | n^2 |
| Dim(gamma = -1) | n^2 |
| J action | Swaps particle <-> antiparticle sector |
| J^2 | +1 (KO-dim 6) |
| J gamma | -gamma J (KO-dim 6) |
| Barrett identification | H_sector = M_n(C) via v tensor w <-> v w^T |
| Barrett spinor space V | C^1 (trivial) |
| Krajewski vertex | Single vertex (n,n) with multiplicity 2 |

## Step 8: Even condition failure implications (from Plan 13-02)

The even condition [gamma, pi(a)] = 0 FAILS for all non-scalar a in M_n(C). This means:

1. The gamma-eigenspaces Sym^2 and wedge^2 are NOT preserved by pi(a), since P(a tensor I)P = I tensor a != a tensor I for a != c*I.

2. Consequence for the bimodule decomposition: the gamma-grading does NOT refine the bimodule decomposition. The irreducible bimodule C^{n^2} is NOT the direct sum of a gamma = +1 part and a gamma = -1 part as bimodules (because pi(a) mixes them).

3. Consequence for the spectral triple: with this (pi, gamma) pair, the spectral triple is NOT even. The options are:
   (a) Find a different algebra action that commutes with gamma
   (b) Find a different chirality operator that commutes with pi(a)
   (c) Work with an odd spectral triple (no gamma)

4. Note: this is NOT a problem for the bimodule decomposition itself. The decomposition H = 2 * C^{n^2} holds regardless of whether the even condition is satisfied. The Krajewski diagram is valid as a description of the bimodule structure; the gamma decoration indicates a constraint that cannot be simultaneously satisfied with the given algebra action.

## Verification Summary

1. **Total dimension:** 2 * n^2 = 2n^2. PASS.
2. **Gamma eigenspace dimensions:** n^2 + n^2 = 2n^2, equal split. PASS.
3. **Bimodule actions match pi and pi_o from Plans 01-02:** Left = a tensor I, Right = I tensor b^T. PASS.
4. **Barrett identification consistent:** C^n tensor C^n = M_n(C) with correct left/right actions. PASS.
5. **Krajewski diagram structure:** Single vertex for simple algebra, multiplicity 2. PASS.
6. **Number of irreducible summands = 2** (not any other value). PASS.
7. **J sigma_1, gamma sigma_3 consistency:** sigma_1 * sigma_3 = -sigma_3 * sigma_1 matches J gamma = -gamma J. PASS.
