# Route 4: Tensor Product A tensor_R V_{1/2} and Complexification

% ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba), peirce_decomposition=under_E11, state_normalization=Tr(rho)=1

**Phase 22, Plan 04: Route 4 -- Tensor Product Complexification**

References:
- Hanche-Olsen, *On the structure and tensor products of JC-algebras*, Canad. J. Math. 35 (1983), 1059--1074
- Alfsen-Shultz, *State Spaces of Operator Algebras* (2001)
- Baez, *The Octonions*, Bull. AMS 39 (2002), 145--205

---

## Part I: Setup and the R-Tensor Product

### Step 1: The Data

**Observer.** From Paper 5 (self-modeling forces C*-algebra): the observer's full algebra is $A = M_n(\mathbb{C})$, a C*-algebra over $\mathbb{C}$. Its self-adjoint part $A^{sa} = M_n(\mathbb{C})^{sa}$ is the Jordan algebra of observables. As a real vector space, $\dim_\mathbb{R}(A) = 2n^2$. As a complex vector space (with scalar multiplication by $z \in \mathbb{C}$ via $z \cdot a = za$), $\dim_\mathbb{C}(A) = n^2$.

**Target module.** The Peirce half-space of $h_3(\mathbb{O})$ under $e = E_{11}$:
$$V_{1/2} = \mathbb{O}^2 \cong S_9 \quad (\text{real Spin}(9)\text{ spinor, } \dim_\mathbb{R} = 16)$$

This is a real vector space. It carries the structure of a Jordan module (Peirce bimodule) over $V_1 \cong \mathbb{R}$ and $V_0 \cong h_2(\mathbb{O})$ via the Peirce multiplication rules $V_i \circ V_{1/2} \subseteq V_{1/2}$. However, $V_{1/2}$ is NOT itself a Jordan algebra -- it is a module (bimodule) in the Peirce decomposition.

**The question.** What happens when the observer $A = M_n(\mathbb{C})$ "probes" $V_{1/2}$, modeled by the tensor product $A \otimes_\mathbb{R} V_{1/2}$?

### Step 2: The R-Tensor Product $A \otimes_\mathbb{R} V_{1/2}$

**Definition.** The tensor product $A \otimes_\mathbb{R} V_{1/2}$ is formed over $\mathbb{R}$. This means we treat both $A$ and $V_{1/2}$ as real vector spaces and form the usual algebraic tensor product over the reals.

**Real dimension:**
$$\dim_\mathbb{R}(A \otimes_\mathbb{R} V_{1/2}) = \dim_\mathbb{R}(A) \cdot \dim_\mathbb{R}(V_{1/2}) = 2n^2 \cdot 16 = 32n^2$$

**Left A-module structure.** Since $A = M_n(\mathbb{C})$ is an algebra, $A \otimes_\mathbb{R} V_{1/2}$ is naturally a left $A$-module via:
$$a \cdot \left(\sum_i a_i \otimes v_i\right) = \sum_i (a \cdot a_i) \otimes v_i$$

where $a \cdot a_i$ is the product in $M_n(\mathbb{C})$.

**Induced complex structure.** Since $A$ is a $\mathbb{C}$-algebra, the left $A$-module $A \otimes_\mathbb{R} V_{1/2}$ inherits a complex structure from $A$: for $z \in \mathbb{C}$ and $\sum_i a_i \otimes v_i \in A \otimes_\mathbb{R} V_{1/2}$,
$$z \cdot \left(\sum_i a_i \otimes v_i\right) := \sum_i (z a_i) \otimes v_i$$

This is well-defined because $z a_i \in A$ (since $A$ is a $\mathbb{C}$-algebra). The map $z \mapsto (z \cdot -)$ satisfies $(z_1 z_2) \cdot x = z_1 \cdot (z_2 \cdot x)$ and $1 \cdot x = x$, so this gives $A \otimes_\mathbb{R} V_{1/2}$ the structure of a complex vector space.

**Complex dimension.** As a complex vector space under this $\mathbb{C}$-action:
$$\dim_\mathbb{C}(A \otimes_\mathbb{R} V_{1/2}) = \frac{\dim_\mathbb{R}(A \otimes_\mathbb{R} V_{1/2})}{2} = \frac{32n^2}{2} = 16n^2$$

**Verification:** This can be seen directly. Choose a $\mathbb{C}$-basis $\{e_1, \ldots, e_{n^2}\}$ for $A$ and an $\mathbb{R}$-basis $\{v_1, \ldots, v_{16}\}$ for $V_{1/2}$. Then $\{e_j \otimes v_k\}_{j=1,\ldots,n^2;\, k=1,\ldots,16}$ is a $\mathbb{C}$-basis for $A \otimes_\mathbb{R} V_{1/2}$, giving $\dim_\mathbb{C} = n^2 \cdot 16$. (This works because every element can be written as a $\mathbb{C}$-linear combination: $(ie_j) \otimes v_k = i \cdot (e_j \otimes v_k)$, so $\{e_j, ie_j\}_{j}$ over $\mathbb{R}$ reduces to $\{e_j\}_{j}$ over $\mathbb{C}$.)

### Step 3: The C-Tensor Product $A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}$

**Definition.** Let $V_{1/2}^\mathbb{C} = V_{1/2} \otimes_\mathbb{R} \mathbb{C}$ be the standard complexification of $V_{1/2}$. This is a complex vector space with:
$$\dim_\mathbb{C}(V_{1/2}^\mathbb{C}) = \dim_\mathbb{R}(V_{1/2}) = 16$$

Now form the tensor product over $\mathbb{C}$:
$$A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}$$

**Complex dimension:**
$$\dim_\mathbb{C}(A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}) = \dim_\mathbb{C}(A) \cdot \dim_\mathbb{C}(V_{1/2}^\mathbb{C}) = n^2 \cdot 16 = 16n^2$$

This matches $\dim_\mathbb{C}(A \otimes_\mathbb{R} V_{1/2}) = 16n^2$. The dimensions agree.

### Step 4: Canonical Isomorphism $A \otimes_\mathbb{R} V_{1/2} \cong A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}$

**Claim.** There is a canonical isomorphism of complex $A$-modules:
$$\varphi: A \otimes_\mathbb{C} V_{1/2}^\mathbb{C} \xrightarrow{\;\sim\;} A \otimes_\mathbb{R} V_{1/2}$$

**Construction of $\varphi$:** Define on elementary tensors:
$$\varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) = (za) \otimes_\mathbb{R} v$$

where $a \in A$, $v \in V_{1/2}$, $z \in \mathbb{C}$.

**Well-definedness over $\mathbb{C}$:** The tensor product $\otimes_\mathbb{C}$ identifies $wa \otimes_\mathbb{C} u = a \otimes_\mathbb{C} wu$ for $w \in \mathbb{C}$, $u \in V_{1/2}^\mathbb{C}$, $a \in A$. We must check $\varphi$ respects this. Take $u = v \otimes_\mathbb{R} z$:

- LHS: $\varphi(wa \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) = (zwa) \otimes_\mathbb{R} v$
- RHS: $\varphi(a \otimes_\mathbb{C} w(v \otimes_\mathbb{R} z)) = \varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} wz)) = (wza) \otimes_\mathbb{R} v$

Since $zwa = wza$ (commutativity of $\mathbb{C}$), LHS = RHS. $\checkmark$

**Construction of $\psi$ (inverse):** Define:
$$\psi: A \otimes_\mathbb{R} V_{1/2} \to A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}$$
$$\psi(a \otimes_\mathbb{R} v) = a \otimes_\mathbb{C} (v \otimes_\mathbb{R} 1)$$

**Verification that $\varphi$ and $\psi$ are mutual inverses:**

$\varphi \circ \psi$: For $a \otimes_\mathbb{R} v$,
$$\varphi(\psi(a \otimes_\mathbb{R} v)) = \varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} 1)) = (1 \cdot a) \otimes_\mathbb{R} v = a \otimes_\mathbb{R} v \quad \checkmark$$

$\psi \circ \varphi$: For $a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)$,
$$\psi(\varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z))) = \psi((za) \otimes_\mathbb{R} v) = (za) \otimes_\mathbb{C} (v \otimes_\mathbb{R} 1) = a \otimes_\mathbb{C} z(v \otimes_\mathbb{R} 1) = a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z) \quad \checkmark$$

The second-to-last equality uses the $\mathbb{C}$-tensor product relation $za \otimes_\mathbb{C} u = a \otimes_\mathbb{C} zu$.

**$\mathbb{C}$-linearity:** For $w \in \mathbb{C}$,
$$\varphi(w \cdot (a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z))) = \varphi((wa) \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) = (zwa) \otimes_\mathbb{R} v = w \cdot ((za) \otimes_\mathbb{R} v) = w \cdot \varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) \quad \checkmark$$

**$A$-linearity (left module map):** For $b \in A$,
$$\varphi(b \cdot (a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z))) = \varphi((ba) \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) = (zba) \otimes_\mathbb{R} v = b \cdot ((za) \otimes_\mathbb{R} v) = b \cdot \varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) \quad \checkmark$$

SELF-CRITIQUE CHECKPOINT (Step 4):
1. SIGN CHECK: No signs involved -- all maps are linear (no minus signs).
2. FACTOR CHECK: No numerical factors introduced. The map is purely algebraic.
3. CONVENTION CHECK: $\otimes_\mathbb{R}$ and $\otimes_\mathbb{C}$ are correctly distinguished. Scalars act on the LEFT factor of the tensor product ($A$-side). $\checkmark$
4. DIMENSION CHECK: Both sides have $\dim_\mathbb{C} = 16n^2$. $\checkmark$

### Step 5: Hanche-Olsen Context

**Hanche-Olsen (1983)** established a tensor product theory for **JC-algebras** -- Jordan algebras that can be realized as self-adjoint parts of C*-algebras, i.e., $B \subseteq C^*\text{-alg}^{sa}$.

Key points from Hanche-Olsen's framework:

**(a) JC-algebras tensor with C*-algebras.** For a JC-algebra $B$ and a C*-algebra $A$, Hanche-Olsen defines $B \hat{\otimes} A^{sa}$, a JC-algebra tensor product. This uses the universal C*-algebra $C^*(B)$ of $B$: every JC-algebra $B$ embeds in $C^*(B)^{sa}$, and the tensor product is defined via $C^*(B) \otimes A$.

**(b) The exceptional case.** $h_3(\mathbb{O})$ is NOT a JC-algebra. It cannot be embedded in any $B(H)^{sa}$ (Alfsen-Shultz 2001, Theorem 11.59). Consequently, the Hanche-Olsen JC-algebra tensor product framework does not apply directly to $h_3(\mathbb{O})$.

**(c) But $V_{1/2}$ is not a Jordan algebra.** $V_{1/2} = \mathbb{O}^2$ is a Peirce bimodule, not a Jordan algebra (it has no identity element, and the Jordan product $V_{1/2} \circ V_{1/2} \subseteq V_1 \oplus V_0$ takes elements OUT of $V_{1/2}$). The tensor product $A \otimes_\mathbb{R} V_{1/2}$ is formed between a C*-algebra and a real vector space -- this is simply the algebraic tensor product of vector spaces. No Jordan or C*-structure of $V_{1/2}$ is needed.

**(d) Scope of our construction.** Our tensor product $A \otimes_\mathbb{R} V_{1/2}$ is:
- Well-defined for ANY real vector space $V$ and ANY $\mathbb{C}$-algebra $A$
- Independent of the Hanche-Olsen JC-algebra framework
- Does not require $V_{1/2}$ to carry algebra structure
- Does not require $h_3(\mathbb{O})$ to be a JC-algebra

The Hanche-Olsen theory is relevant context (it tells us what would happen if we tried to tensor the Jordan algebras $V_1$ or $V_0$ with $A$ in the Jordan framework), but our construction bypasses it entirely.

### Step 6: The Peirce Interface vs. Tensor Product Model

**Two models of "observer probes $V_{1/2}$":**

**Model T (Tensor product).** The observer forms $A \otimes_\mathbb{R} V_{1/2}$, treating $V_{1/2}$ as a space the observer has "a copy of for each degree of freedom." This is the model analyzed above. It gives: the observer's description space is $A \otimes_\mathbb{R} V_{1/2} \cong A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}$, and $V_{1/2}^\mathbb{C}$ appears necessarily.

**Model P (Peirce interface).** The observer interacts with $V_{1/2}$ through the Peirce multiplication rule $V_1 \circ V_{1/2} \subseteq V_{1/2}$. Since $V_1 = \mathbb{R} \cdot E_{11}$, the Peirce action of $V_1$ on $V_{1/2}$ is simply scalar multiplication by a real number: $(\alpha E_{11}) \circ w = \frac{1}{2}\alpha w$ for $w \in V_{1/2}$. The observer enriches $V_1$ from $\mathbb{R}$ to $\mathbb{C}$ (since $A = M_n(\mathbb{C})$ contains $\mathbb{C} \cdot E_{11}$ as a subalgebra), and the enriched Peirce action becomes $\mathbb{C}$-scalar multiplication on $V_{1/2}$, which requires extending $V_{1/2}$ to $V_{1/2}^\mathbb{C}$.

**The distinction:** Model T uses the full tensor product structure; Model P uses only the Peirce interface (a much more constrained interaction). Both lead to $V_{1/2}^\mathbb{C}$ appearing, but via different mechanisms:

- Model T: $V_{1/2}^\mathbb{C}$ appears because $A \otimes_\mathbb{R} V = A \otimes_\mathbb{C} V^\mathbb{C}$ for any real vector space $V$.
- Model P: $V_{1/2}^\mathbb{C}$ appears because the enriched Peirce action requires $\mathbb{C}$-scalars to act on $V_{1/2}$.

Model P is the extension-of-scalars argument from Phase 18, Step 6, now seen from the Peirce angle.

---

## Summary of Part I

| Object | Definition | $\dim_\mathbb{R}$ | $\dim_\mathbb{C}$ |
|:---:|:---:|:---:|:---:|
| $A = M_n(\mathbb{C})$ | Observer's C*-algebra | $2n^2$ | $n^2$ |
| $V_{1/2} = \mathbb{O}^2$ | Peirce half-space | 16 | N/A (real) |
| $V_{1/2}^\mathbb{C}$ | Complexification | 32 | 16 |
| $A \otimes_\mathbb{R} V_{1/2}$ | R-tensor product | $32n^2$ | $16n^2$ |
| $A \otimes_\mathbb{C} V_{1/2}^\mathbb{C}$ | C-tensor product | $32n^2$ | $16n^2$ |

Canonical isomorphism: $\varphi: A \otimes_\mathbb{C} V_{1/2}^\mathbb{C} \xrightarrow{\sim} A \otimes_\mathbb{R} V_{1/2}$, with $\varphi(a \otimes_\mathbb{C} (v \otimes_\mathbb{R} z)) = (za) \otimes_\mathbb{R} v$.
