# Peirce Decomposition, Complexification, and Spin(9) -> Spin(10) Upgrade

% ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba), peirce_decomposition=under_E11, octonion_notation=O_8dim

**Phase 18, Plan 01: Complexification from C*-Observer**

---

## Part I: Peirce Decomposition of h_3(O) under E_11

### Step 1: The Exceptional Jordan Algebra h_3(O)

The exceptional Jordan algebra $h_3(\mathbb{O})$ (also called the Albert algebra) consists of $3 \times 3$ Hermitian matrices over the octonions $\mathbb{O}$:

$$
X = \begin{pmatrix} \alpha & \bar{x}_3 & x_2 \\ x_3 & \beta & \bar{x}_1 \\ \bar{x}_2 & x_1 & \gamma \end{pmatrix}
$$

where $\alpha, \beta, \gamma \in \mathbb{R}$ and $x_1, x_2, x_3 \in \mathbb{O}$, with $\bar{\cdot}$ denoting octonion conjugation. Hermiticity means $X_{ij} = \bar{X}_{ji}$.

**Dimension count:**
$$\dim(h_3(\mathbb{O})) = 3 \cdot 1 + 3 \cdot 8 = 3 + 24 = 27$$

The three real diagonal entries contribute 3, and the three independent octonion off-diagonal entries (upper triangle) contribute $3 \times 8 = 24$.

The Jordan product is:
$$A \circ B = \frac{1}{2}(AB + BA)$$
where $AB$ denotes the usual matrix product with octonion entries (well-defined for $3 \times 3$ Hermitian matrices even though $\mathbb{O}$ is non-associative, by the results of Albert and Jordan-von Neumann-Wigner).

### Step 2: Peirce Decomposition under e = E_{11}

The observer selects a rank-1 idempotent $e = E_{11}$, the $3 \times 3$ matrix with 1 in the $(1,1)$ entry and 0 elsewhere:

$$
e = E_{11} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
$$

This is indeed an idempotent: $e \circ e = e$ (since $E_{11}^2 = E_{11}$ in the usual matrix product, so $e \circ e = \frac{1}{2}(E_{11}^2 + E_{11}^2) = E_{11}$).

The Peirce decomposition of $h_3(\mathbb{O})$ under $e$ produces eigenspaces of the multiplication operator $L_e(X) = e \circ X$:

$$h_3(\mathbb{O}) = V_1 \oplus V_{1/2} \oplus V_0$$

where $V_\lambda = \{X \in h_3(\mathbb{O}) : e \circ X = \lambda X\}$.

**Computing $L_e(X)$ explicitly:**

$$
e \circ X = \frac{1}{2}(E_{11} X + X E_{11})
$$

For $E_{11} X$:
$$
E_{11} X = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} \alpha & \bar{x}_3 & x_2 \\ x_3 & \beta & \bar{x}_1 \\ \bar{x}_2 & x_1 & \gamma \end{pmatrix} = \begin{pmatrix} \alpha & \bar{x}_3 & x_2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}
$$

For $X E_{11}$:
$$
X E_{11} = \begin{pmatrix} \alpha & \bar{x}_3 & x_2 \\ x_3 & \beta & \bar{x}_1 \\ \bar{x}_2 & x_1 & \gamma \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} \alpha & 0 & 0 \\ x_3 & 0 & 0 \\ \bar{x}_2 & 0 & 0 \end{pmatrix}
$$

Therefore:
$$
e \circ X = \frac{1}{2} \begin{pmatrix} 2\alpha & \bar{x}_3 & x_2 \\ x_3 & 0 & 0 \\ \bar{x}_2 & 0 & 0 \end{pmatrix}
$$

**Identifying the Peirce eigenspaces:**

**$V_1$ (eigenvalue 1):** $e \circ X = X$ requires:
- $2\alpha / 2 = \alpha$ (always true for the $(1,1)$ entry)
- $\bar{x}_3 / 2 = \bar{x}_3 \implies \bar{x}_3 = 0$, so $x_3 = 0$
- $x_2 / 2 = x_2 \implies x_2 = 0$
- $0 = \beta$, $0 = \bar{x}_1$, $0 = \gamma$

Thus $V_1 = \{ \alpha E_{11} : \alpha \in \mathbb{R} \} \cong \mathbb{R}$.

$$\dim(V_1) = 1$$

**$V_{1/2}$ (eigenvalue 1/2):** $e \circ X = \frac{1}{2}X$ requires examining each entry of $e \circ X = \frac{1}{2}X$:
- $(1,1)$: $\alpha = \frac{1}{2}\alpha \implies \alpha = 0$
- $(1,2)$: $\frac{1}{2}\bar{x}_3 = \frac{1}{2}\bar{x}_3$ (always true)
- $(1,3)$: $\frac{1}{2}x_2 = \frac{1}{2}x_2$ (always true)
- $(2,1)$: $\frac{1}{2}x_3 = \frac{1}{2}x_3$ (always true)
- $(2,2)$: $0 = \frac{1}{2}\beta \implies \beta = 0$
- $(2,3)$: $0 = \frac{1}{2}\bar{x}_1 \implies x_1 = 0$
- $(3,1)$: $\frac{1}{2}\bar{x}_2 = \frac{1}{2}\bar{x}_2$ (always true)
- $(3,2)$: $0 = \frac{1}{2}x_1 \implies x_1 = 0$ (consistent)
- $(3,3)$: $0 = \frac{1}{2}\gamma \implies \gamma = 0$

Thus $V_{1/2}$ consists of matrices with $\alpha = \beta = \gamma = 0$, $x_1 = 0$, and $x_2, x_3 \in \mathbb{O}$ free:

$$
V_{1/2} = \left\{ \begin{pmatrix} 0 & \bar{x}_3 & x_2 \\ x_3 & 0 & 0 \\ \bar{x}_2 & 0 & 0 \end{pmatrix} : x_2, x_3 \in \mathbb{O} \right\} \cong \mathbb{O} \oplus \mathbb{O} = \mathbb{O}^2
$$

$$\dim(V_{1/2}) = 8 + 8 = 16$$

**$V_0$ (eigenvalue 0):** $e \circ X = 0$ requires:
- $(1,1)$: $\alpha = 0$
- $(1,2)$: $\frac{1}{2}\bar{x}_3 = 0 \implies x_3 = 0$
- $(1,3)$: $\frac{1}{2}x_2 = 0 \implies x_2 = 0$
- The remaining entries are automatically zero in $e \circ X$

Thus $V_0$ consists of matrices with $\alpha = 0$, $x_2 = x_3 = 0$, and $\beta, \gamma \in \mathbb{R}$, $x_1 \in \mathbb{O}$ free:

$$
V_0 = \left\{ \begin{pmatrix} 0 & 0 & 0 \\ 0 & \beta & \bar{x}_1 \\ 0 & x_1 & \gamma \end{pmatrix} : \beta, \gamma \in \mathbb{R},\, x_1 \in \mathbb{O} \right\} \cong h_2(\mathbb{O})
$$

$$\dim(V_0) = 2 + 8 = 10$$

### Step 3: Dimension Verification

$$\dim(V_1) + \dim(V_{1/2}) + \dim(V_0) = 1 + 16 + 10 = 27 = \dim(h_3(\mathbb{O})) \quad \checkmark$$

SELF-CRITIQUE CHECKPOINT (Step 3):
1. SIGN CHECK: No sign changes involved (dimension counting). N/A.
2. FACTOR CHECK: No factors of 2, pi, hbar, c. Dimensions are integer counts.
3. CONVENTION CHECK: Jordan product $\circ = \frac{1}{2}(ab + ba)$ used consistently. Peirce eigenvalues are $\{0, 1/2, 1\}$ as standard. $\checkmark$
4. DIMENSION CHECK: $1 + 16 + 10 = 27$ $\checkmark$

### Step 4: Stabilizer of e in F_4 and Spin(9) Action

The automorphism group of $h_3(\mathbb{O})$ is the exceptional Lie group:

$$\mathrm{Aut}(h_3(\mathbb{O})) = F_4$$

with $\dim(F_4) = 52$ (Baez, "The Octonions," Bull. AMS 39 (2002), Sec 4.3).

The stabilizer of the idempotent $e = E_{11}$ in $F_4$ is:

$$\mathrm{Stab}_{F_4}(E_{11}) = \mathrm{Spin}(9)$$

with $\dim(\mathrm{Spin}(9)) = 36 = \binom{9}{2}$.

**Coset dimension check:** $\dim(F_4) - \dim(\mathrm{Spin}(9)) = 52 - 36 = 16 = \dim(V_{1/2})$, consistent with $F_4/\mathrm{Spin}(9) \cong \mathbb{O}P^2$ (the Cayley projective plane, also 16-dimensional). $\checkmark$

**Spin(9) action on the Peirce spaces:**

Under the $\mathrm{Spin}(9)$ stabilizer, the Peirce decomposition $27 = 1 + 16 + 10$ corresponds to:

- $V_1 \cong \mathbb{R}$ carries the **trivial representation** of $\mathrm{Spin}(9)$
- $V_{1/2} \cong \mathbb{O}^2$ carries the **real spinor representation $S_9$** of $\mathrm{Spin}(9)$
- $V_0 \cong h_2(\mathbb{O})$ carries the **vector representation $\mathbf{9}$ plus trace**: the traceless part of $h_2(\mathbb{O})$ is 9-dimensional (the defining/vector representation of $\mathrm{Spin}(9)$ via the $\mathrm{SO}(9)$ quotient), and the trace part contributes 1 additional dimension, giving $9 + 1 = 10$

**Verification that $V_{1/2}$ carries $S_9$:**

$\mathrm{Spin}(9)$ has a unique real irreducible spinor representation $S_9$ of dimension:
$$\dim_{\mathbb{R}}(S_9) = 2^{[9/2]} = 2^4 = 16$$

This matches $\dim(V_{1/2}) = 16$. The identification $V_{1/2} = \mathbb{O}^2 = S_9$ as a $\mathrm{Spin}(9)$-representation is established in:

- Baez, "The Octonions," Bull. AMS 39 (2002), Section 4.3 (Theorem 5)
- Yokota, "Exceptional Lie Groups" (2009), Chapter 2

The key structural fact is that $\mathrm{Spin}(9)$ acts on $\mathbb{O}^2$ via its spinor representation because the Cayley plane $\mathbb{O}P^2 = F_4/\mathrm{Spin}(9)$ has tangent spaces isomorphic to $\mathbb{O}^2$ at the basepoint corresponding to $E_{11}$, and the isotropy representation of $\mathrm{Spin}(9)$ on this tangent space is precisely $S_9$.

**Note on V_0:** The space $V_0 = h_2(\mathbb{O})$ can be decomposed further. The trace $\mathrm{tr} : h_2(\mathbb{O}) \to \mathbb{R}$ splits off a trivial representation, leaving the traceless part $h_2^0(\mathbb{O})$ of dimension 9, which carries the defining (vector) representation of $\mathrm{SO}(9) = \mathrm{Spin}(9)/\mathbb{Z}_2$. The full decomposition under $\mathrm{Spin}(9)$ is:
$$27 = \mathbf{1} \oplus \mathbf{16} \oplus (\mathbf{9} \oplus \mathbf{1})$$
where the first $\mathbf{1}$ comes from $V_1$, the $\mathbf{16}$ is $S_9$, and $\mathbf{9} \oplus \mathbf{1}$ is $V_0$.

SELF-CRITIQUE CHECKPOINT (Step 4):
1. SIGN CHECK: No sign-dependent computations. N/A.
2. FACTOR CHECK: Coset dimension $52 - 36 = 16$ $\checkmark$. Spinor dimension $2^4 = 16$ $\checkmark$.
3. CONVENTION CHECK: $F_4 = \mathrm{Aut}(h_3(\mathbb{O}))$ is the compact form. $\mathrm{Spin}(9)$ stabilizer is standard. $\checkmark$
4. DIMENSION CHECK: $1 + 16 + (9 + 1) = 27$ $\checkmark$

---

## Summary of Part I

| Peirce Space | Identification | $\dim_{\mathbb{R}}$ | $\mathrm{Spin}(9)$ Rep |
|:---:|:---:|:---:|:---:|
| $V_1$ | $\mathbb{R} \cdot E_{11}$ | 1 | trivial $\mathbf{1}$ |
| $V_{1/2}$ | $\mathbb{O}^2$ | 16 | spinor $S_9 = \mathbf{16}$ |
| $V_0$ | $h_2(\mathbb{O})$ | 10 | $\mathbf{9} \oplus \mathbf{1}$ |
| **Total** | $h_3(\mathbb{O})$ | **27** | $\mathbf{1} \oplus \mathbf{16} \oplus \mathbf{9} \oplus \mathbf{1}$ |

**Input assumption:** The observer's idempotent $e = E_{11}$ is taken as given input (the "rank-1 idempotent choice" / symmetry breaking that appears as Gap B step 1 in the roadmap). We do not derive why the observer selects this particular diagonal slot.
