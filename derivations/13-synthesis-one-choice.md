# Synthesis: One Choice (u in S^6), Two Consequences (Gauge Group + Chirality)

% ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba), peirce_decomposition=under_E11, clifford_convention=euclidean_positive, octonion_basis=fano_e1e2=e4, complex_structure=u_equals_e7, spin_representation=S10plus_boyle

**Phase 20, Plan 01: F_4 Intersection Route and Single-Input Proof**

References: Todorov-Drenska arXiv:1805.06739, Todorov arXiv:1911.13124, Baez "The Octonions" (Bull. AMS 39, 2002), Furey arXiv:1806.00612, Boyle arXiv:2006.16265, Yokota "Exceptional Lie Groups" Ch. 2-3

---

## Part I: The F_4 Intersection Route (Todorov-Drenska)

### Step 1: Starting Point — F_4, Spin(9), and the Observer's Idempotent

The exceptional Jordan algebra $h_3(\mathbb{O})$ has automorphism group $F_4$ with $\dim(F_4) = 52$.

The observer selects a rank-1 idempotent $e = E_{11}$ (Phase 18, Step 2). The stabilizer of $E_{11}$ in $F_4$ is $\mathrm{Spin}(9)$ (Phase 18, Step 4):

$$\mathrm{Stab}_{F_4}(E_{11}) = \mathrm{Spin}(9), \qquad \dim(\mathrm{Spin}(9)) = 36$$

The orbit is the octonionic projective plane: $F_4 / \mathrm{Spin}(9) = \mathbb{OP}^2$, $\dim = 52 - 36 = 16$.

After complexification (Phase 18, Plan 02), this upgrades to:
- $F_4 \to E_6$, $\mathrm{Spin}(9) \to \mathrm{Spin}(10) \times \mathrm{U}(1)$
- $\mathbf{27} \to \mathbf{1} \oplus \mathbf{10} \oplus \mathbf{16}$ under $\mathrm{Spin}(10)$

**Input so far:** The rank-1 idempotent $E_{11}$ (Gap B step 1: taken as given, not derived from self-modeling).

### Step 2: G_2 = Aut(O) and the Color Group SU(3)_C

The octonion automorphism group $G_2 = \mathrm{Aut}(\mathbb{O})$ has $\dim(G_2) = 14$. It embeds in $F_4$ as a subgroup: every automorphism of $\mathbb{O}$ extends to an automorphism of $h_3(\mathbb{O})$ by acting entry-by-entry on the octonion entries of each $3 \times 3$ Hermitian matrix (Baez, Sec 4.3).

The same complex structure $u = e_7$ that was used in Phase 19 to define $\mathrm{Cl}(6)$ also acts on $\mathrm{Im}(\mathbb{O})$ via left multiplication. The stabilizer of $u$ in $G_2$ is $\mathrm{SU}(3)$:

$$\mathrm{SU}(3)_C := \mathrm{Stab}_{G_2}(u) = \mathrm{Stab}_{G_2}(e_7)$$

$$\dim(\mathrm{SU}(3)_C) = 8$$

The orbit of $u$ under $G_2$ is:

$$S^6 = G_2 / \mathrm{SU}(3), \qquad \dim(S^6) = 14 - 8 = 6$$

This is the space of unit imaginary octonions, and $\mathrm{SU}(3)_C$ is precisely the subgroup of $G_2$ that preserves the complex structure $J: W \to W$ defined by $J(w) = u \cdot w$ on the 6-dimensional complement $W = u^\perp \cap \mathrm{Im}(\mathbb{O})$. Under $\mathrm{SU}(3)_C$, the space $W \cong \mathbb{C}^3$ carries the defining 3-dimensional representation of $\mathrm{SU}(3)$.

**Dimension check:** $\dim(G_2) - \dim(\mathrm{SU}(3)) = 14 - 8 = 6 = \dim(S^6)$. Correct.

### Step 3: The F_4 Breaking by u — The Todorov-Drenska Subgroup

Choosing $u \in S^6 \subset \mathrm{Im}(\mathbb{O})$ splits the octonions:

$$\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3, \qquad \mathbb{C} = \mathrm{span}_{\mathbb{R}}\{1, u\}, \qquad \mathbb{C}^3 = \text{complexification of } W$$

This splitting induces a decomposition of the Jordan algebra. Each octonion entry $x_k$ in an element of $h_3(\mathbb{O})$ decomposes as $x_k = z_k + w_k$ where $z_k \in \mathbb{C}$ and $w_k \in \mathbb{C}^3$. The Hermitian matrices whose entries lie entirely in $\mathbb{C} \subset \mathbb{O}$ form a subalgebra:

$$h_3(\mathbb{C}) \subset h_3(\mathbb{O}), \qquad \dim(h_3(\mathbb{C})) = 9$$

(3 real diagonal entries + 3 complex off-diagonal = 3 + 2 $\times$ 3 = 9.)

The subgroup of $F_4$ that preserves the splitting $\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$ — equivalently, that commutes with the complex structure $J$ defined by $u$ on the octonion entries — contains (Todorov-Drenska arXiv:1805.06739, Yokota Ch. 3):

$$\frac{\mathrm{SU}(3)_C \times \mathrm{SU}(3)_J}{\mathbb{Z}_3} \subset F_4$$

where:

- $\mathrm{SU}(3)_C = \mathrm{Stab}_{G_2}(u)$ acts on the $\mathbb{C}^3$ factor of each octonion entry (the **color** group, preserving the complex structure $J$)
- $\mathrm{SU}(3)_J = \mathrm{Aut}(h_3(\mathbb{C}))$ acts on the Jordan algebra structure of $h_3(\mathbb{C})$ — it permutes the rows/columns of the $3 \times 3$ matrices while preserving the $\mathbb{C}$-valued entries (a **"Jordan flavor"** group)
- The $\mathbb{Z}_3$ quotient arises because the center of each $\mathrm{SU}(3)$ intersects: the cube roots of unity $\omega = e^{2\pi i/3}$ act as $\omega$ on $\mathbb{C}^3$ and $\omega^{-1}$ on $h_3(\mathbb{C})$, giving a common $\mathbb{Z}_3$ kernel

**Dimension:** $\dim([\mathrm{SU}(3) \times \mathrm{SU}(3)] / \mathbb{Z}_3) = 8 + 8 = 16$

**Dimension check against F_4:**
- $\dim(F_4) = 52$
- The breaking $F_4 \supset [\mathrm{SU}(3) \times \mathrm{SU}(3)]/\mathbb{Z}_3$ has codimension $52 - 16 = 36$

**Note on the stabilizer dimension:** The subgroup of $F_4$ preserving the $u$-splitting is at least $[\mathrm{SU}(3) \times \mathrm{SU}(3)]/\mathbb{Z}_3$ (dim 16). Whether it is exactly this group or strictly larger requires checking whether any additional F_4 generators preserve the splitting. The standard result (Yokota, Adams) is that this is a maximal-rank subgroup of $F_4$, meaning it contains a maximal torus (rank 4 = rank of F_4). Therefore no additional semisimple or abelian factors can be added while remaining in $F_4$, and it is indeed the full identity component of the $u$-preserving subgroup.

**NOTE:** The F_4 route gives the gauge GROUP but does NOT specify a chiral representation. The 27-dim representation of $h_3(\mathbb{O})$ under $F_4$ is a real representation. There is no natural complex structure on the $\mathbf{27}$ from the $F_4$ perspective alone, and therefore no chirality.

### Step 4: The SM Gauge Group from the Intersection

We now compute the intersection of the two stabilizers:

$$\mathrm{Stab}_{F_4}(E_{11}) \cap \text{(u-preserving subgroup)} = \mathrm{Spin}(9) \cap \frac{\mathrm{SU}(3)_C \times \mathrm{SU}(3)_J}{\mathbb{Z}_3}$$

The intersection must contain $\mathrm{SU}(3)_C$ (since $G_2 \subset \mathrm{Spin}(9)$ via the chain $G_2 \subset F_4 \supset \mathrm{Spin}(9)$, and in fact $G_2 \subset \mathrm{Spin}(7) \subset \mathrm{Spin}(9)$, so $\mathrm{SU}(3)_C = \mathrm{Stab}_{G_2}(u) \subset \mathrm{Spin}(9)$).

The $\mathrm{SU}(3)_J$ factor acts on the $h_3(\mathbb{C})$ structure. Inside $\mathrm{Spin}(9)$, the stabilizer of $E_{11}$ means we are looking at automorphisms that fix the first diagonal entry. The intersection of $\mathrm{SU}(3)_J$ (acting on rows/columns of $h_3(\mathbb{C})$) with $\mathrm{Stab}(E_{11})$ gives:

- The subgroup of $\mathrm{SU}(3)_J$ that fixes $E_{11}$. In $\mathrm{SU}(3)_J = \mathrm{Aut}(h_3(\mathbb{C}))$, the stabilizer of the first idempotent $E_{11}$ is $\mathrm{U}(2) \subset \mathrm{SU}(3)_J$ (the block diagonal $\mathrm{U}(1) \times \mathrm{SU}(2)$ preserving the $1 + 2$ partition of rows/columns).

So:

$$\mathrm{Spin}(9) \cap \frac{\mathrm{SU}(3)_C \times \mathrm{SU}(3)_J}{\mathbb{Z}_3} \supset \frac{\mathrm{SU}(3)_C \times \mathrm{U}(2)_J}{\mathbb{Z}_3}$$

Now $\mathrm{U}(2) = \mathrm{SU}(2) \times \mathrm{U}(1) / \mathbb{Z}_2$, so the intersection contains:

$$\mathrm{SU}(3)_C \times \mathrm{SU}(2) \times \mathrm{U}(1) \quad (\text{up to finite quotient})$$

**Dimension:** $8 + 3 + 1 = 12$. This is the Standard Model gauge group.

**Cross-check on dimension:**
- $\dim(\mathrm{Spin}(9)) = 36$
- $\dim([\mathrm{SU}(3) \times \mathrm{SU}(3)]/\mathbb{Z}_3) = 16$
- $\dim(\text{intersection}) = 12$ is consistent: it is less than either subgroup individually, as expected for a non-trivial intersection.

**Cross-check on codimension in F_4:**
- $\dim(F_4) - \dim(\mathrm{SM}) = 52 - 12 = 40$
- The 40 broken generators correspond to the coset space of the SM gauge group inside $F_4$

This is the **Todorov-Drenska result**: the Standard Model gauge group arises as the intersection of two stabilizers in $F_4$:
1. $\mathrm{Stab}_{F_4}(E_{11}) = \mathrm{Spin}(9)$ (the observer's choice of idempotent)
2. $\text{Subgroup preserving } \mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$ (the choice of complex structure $u$)

---

## Part II: The Single Algebraic Input

### Step 5: Tracing u Through Both Routes

The key claim of this phase is that both consequences — the gauge group and chirality — trace to a single algebraic input: the choice of $u \in S^6 = G_2/\mathrm{SU}(3)$.

Both routes begin with the same decomposition:

$$\mathrm{Im}(\mathbb{O}) = \mathrm{span}\{u\} \oplus W, \qquad W = u^\perp \cap \mathrm{Im}(\mathbb{O}), \qquad \dim(W) = 6$$

**Route A (F_4 intersection / Todorov-Drenska):**

| Step | Input | Output |
|------|-------|--------|
| A1 | $u \in S^6$ chosen | $\mathrm{Im}(\mathbb{O}) = \mathrm{span}\{u\} \oplus W$ |
| A2 | $u$ defines $J: W \to W$ by $J(w) = u \cdot w$ | $W \cong \mathbb{C}^3$ as complex vector space |
| A3 | $\mathrm{Stab}_{G_2}(u)$ preserves $J$ | $\mathrm{SU}(3)_C$ = color group (dim 8) |
| A4 | $\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$ breaks $F_4$ | $[\mathrm{SU}(3)_C \times \mathrm{SU}(3)_J]/\mathbb{Z}_3 \subset F_4$ (dim 16) |
| A5 | Intersect with $\mathrm{Spin}(9) = \mathrm{Stab}_{F_4}(E_{11})$ | $\mathrm{SU}(3)_C \times \mathrm{SU}(2) \times \mathrm{U}(1)$ (dim 12) |

**Route B (Cl(6)/Pati-Salam / Phase 19):**

| Step | Input | Output |
|------|-------|--------|
| B1 | Same $u \in S^6$ chosen | Same $\mathrm{Im}(\mathbb{O}) = \mathrm{span}\{u\} \oplus W$ |
| B2 | $W$ provides 6 real directions | $\gamma_1, \ldots, \gamma_6$ generate $\mathrm{Cl}(6) \subset \mathrm{Cl}(10)$ |
| B3 | $\omega_6 = \gamma_1 \cdots \gamma_6$ | Chirality operator, $\omega_6^2 = -1$ |
| B4 | $\mathrm{Stab}_{\mathrm{Spin}(10)}(\omega_6)$ | $\mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$ (Pati-Salam, dim 21) |
| B5 | Same $u$ breaks $\mathrm{SU}(4) \to \mathrm{SU}(3)_C \times \mathrm{U}(1)_{B-L}$ | $\mathrm{SU}(3)_C \times \mathrm{SU}(2)_L \times \mathrm{U}(1)_Y$ (dim 12) |

**The common algebraic operation:** In both routes, $u$ acts on $\mathrm{Im}(\mathbb{O})$, splitting it into $\mathrm{span}\{u\} \oplus W$. The 6-dimensional subspace $W = u^\perp \cap \mathrm{Im}(\mathbb{O})$ is **identical** in both routes. It is the same six directions ($e_1, \ldots, e_6$ in the Fano convention with $u = e_7$).

Route A uses $W$ via the complex structure $J: W \to W$ to define $\mathrm{SU}(3)_C = \mathrm{Stab}_{G_2}(u)$, then intersects within $F_4$.

Route B uses $W$ directly as the 6 generators of $\mathrm{Cl}(6)$, builds the volume form $\omega_6$, and breaks via the Pati-Salam chain.

### Step 6: The Single-Input Theorem

**Theorem (Single Input).** Let $u \in S^6 \subset \mathrm{Im}(\mathbb{O})$ be a unit imaginary octonion, and let $E_{11}$ be a rank-1 idempotent in $h_3(\mathbb{O})$. Then the single choice of $u$ determines:

(i) **The decomposition** $\mathrm{Im}(\mathbb{O}) = \mathrm{span}\{u\} \oplus W$ with $W = u^\perp \cap \mathrm{Im}(\mathbb{O})$, $\dim(W) = 6$.

(ii) **The F_4 breaking:** The splitting $\mathbb{O} = \mathbb{C} \oplus \mathbb{C}^3$ induces the subgroup $[\mathrm{SU}(3)_C \times \mathrm{SU}(3)_J] / \mathbb{Z}_3 \subset F_4$. Its intersection with $\mathrm{Spin}(9) = \mathrm{Stab}_{F_4}(E_{11})$ contains $\mathrm{SU}(3)_C \times \mathrm{SU}(2) \times \mathrm{U}(1)$ (the SM gauge group).

(iii) **The Cl(6) construction:** The same $W$ provides the 6 generators of $\mathrm{Cl}(6) \subset \mathrm{Cl}(10)$, whose volume form $\omega_6$ breaks $\mathrm{Spin}(10) \to \mathrm{SU}(4) \times \mathrm{SU}(2)_L \times \mathrm{SU}(2)_R$. The same $u$ further breaks $\mathrm{SU}(4) \to \mathrm{SU}(3)_C \times \mathrm{U}(1)_{B-L}$, giving the SM gauge group with the LEFT chiral embedding.

No additional algebraic input beyond $u$ and $E_{11}$ is needed for either route.

---

*(Part III and Part IV continue in Task 2.)*
