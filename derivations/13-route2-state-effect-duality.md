# Route 2: State-Effect Duality and Complexification

% ASSERT_CONVENTION: natural_units=dimensionless, jordan_product=(1/2)(ab+ba), peirce_decomposition=under_E11, state_normalization=Tr(rho)=1

**Phase 22, Plan 02: State-Effect Duality Route to Complexification**

---

## Part I: Observer State Probing of V_{1/2} via Peirce Duality

### Step 1: Observer States on M_n(C)^sa

The observer's algebra is $M_n(\mathbb{C})^{sa}$ -- the self-adjoint part of a complex matrix algebra (Paper 5). In the Peirce decomposition of $h_3(\mathbb{O})$ under $e = E_{11}$, the observer's Peirce 1-space is:

$$V_1 = \{\alpha E_{11} : \alpha \in \mathbb{R}\} \cong \mathbb{R}$$

A **state** on $M_n(\mathbb{C})^{sa}$ is a positive normalized linear functional:

$$\omega: M_n(\mathbb{C})^{sa} \to \mathbb{R}, \quad \omega(a) = \mathrm{Tr}(\rho \cdot a)$$

where $\rho$ is a density matrix: $\rho \geq 0$, $\mathrm{Tr}(\rho) = 1$.

**Properties of states:**
- **Linearity over R:** $\omega(\alpha a + \beta b) = \alpha\,\omega(a) + \beta\,\omega(b)$ for $\alpha, \beta \in \mathbb{R}$
- **Positivity:** $\omega(a^2) \geq 0$ for all $a \in M_n(\mathbb{C})^{sa}$
- **Normalization:** $\omega(\mathbf{1}) = 1$

The **C-linear extension** of $\omega$ to the full algebra $M_n(\mathbb{C})$ is:

$$\omega^{\mathbb{C}}: M_n(\mathbb{C}) \to \mathbb{C}, \quad \omega^{\mathbb{C}}(a + ib) = \omega(a) + i\,\omega(b)$$

for $a, b \in M_n(\mathbb{C})^{sa}$. This extension is:
- Well-defined: every $z \in M_n(\mathbb{C})$ has a unique decomposition $z = a + ib$ with $a, b$ self-adjoint
- Unique: determined entirely by $\omega$ on $M_n(\mathbb{C})^{sa}$
- $\mathbb{C}$-linear: $\omega^{\mathbb{C}}(z_1 + \lambda z_2) = \omega^{\mathbb{C}}(z_1) + \lambda\,\omega^{\mathbb{C}}(z_2)$ for $\lambda \in \mathbb{C}$

### Step 2: Peirce Multiplication Rules and the Observer Interface

The Peirce decomposition $h_3(\mathbb{O}) = V_1 \oplus V_{1/2} \oplus V_0$ under $E_{11}$ satisfies the standard multiplication rules (Alfsen-Shultz, *State Spaces of Operator Algebras*, 2001, Ch. 6):

| Product | Result |
|:---:|:---:|
| $V_1 \circ V_1$ | $\subset V_1$ |
| $V_1 \circ V_{1/2}$ | $\subset V_{1/2}$ |
| $V_1 \circ V_0$ | $= \{0\}$ |
| $V_{1/2} \circ V_{1/2}$ | $\subset V_1 \oplus V_0$ |
| $V_{1/2} \circ V_0$ | $\subset V_{1/2}$ |
| $V_0 \circ V_0$ | $\subset V_0$ |

The **observer interface** consists of two mechanisms by which the observer accesses $V_{1/2}$:

**(a) Left multiplication by V_1 elements.** For any $a \in V_1$, the map $L_a: V_{1/2} \to V_{1/2}$ defined by $v \mapsto a \circ v$ is an endomorphism of $V_{1/2}$. Since $V_1 \cong \mathbb{R}$, every element of $V_1$ is $\alpha E_{11}$, and $L_{\alpha E_{11}}(v) = \alpha \cdot (E_{11} \circ v) = \frac{\alpha}{2} v$. So $L_a$ acts as scalar multiplication by $\alpha/2$ on $V_{1/2}$ -- the observer can only rescale, not rotate, $V_{1/2}$ elements through this channel.

**(b) Peirce-projected bilinear pairing.** For $v, w \in V_{1/2}$, the Jordan product $v \circ w \in V_1 \oplus V_0$. The observer has direct access to $V_1$ (its own Peirce space), so the projection $P_1(v \circ w)$ is the observer-accessible part of this product.

### Step 3: Explicit Computation of P_1(v * w) for V_{1/2} = O^2

Let $v, w \in V_{1/2}$. Using the explicit parametrization from derivation 11:

$$v = \begin{pmatrix} 0 & \bar{x}_3 & x_2 \\ x_3 & 0 & 0 \\ \bar{x}_2 & 0 & 0 \end{pmatrix}, \quad w = \begin{pmatrix} 0 & \bar{y}_3 & y_2 \\ y_3 & 0 & 0 \\ \bar{y}_2 & 0 & 0 \end{pmatrix}$$

where $x_2, x_3, y_2, y_3 \in \mathbb{O}$.

Computing $v \circ w = \frac{1}{2}(vw + wv)$:

The $(1,1)$ entry of $vw$ is:
$$(vw)_{11} = 0 \cdot 0 + \bar{x}_3 \cdot y_3 + x_2 \cdot \bar{y}_2$$

The $(1,1)$ entry of $wv$ is:
$$(wv)_{11} = 0 \cdot 0 + \bar{y}_3 \cdot x_3 + y_2 \cdot \bar{x}_2$$

Therefore the $(1,1)$ entry of $v \circ w$ is:

$$(v \circ w)_{11} = \frac{1}{2}\bigl(\bar{x}_3 y_3 + x_2 \bar{y}_2 + \bar{y}_3 x_3 + y_2 \bar{x}_2\bigr)$$

Using the identity $\bar{a}b + \bar{b}a = 2\,\mathrm{Re}(\bar{a}b)$ for octonions (since $\bar{a}b + \overline{\bar{a}b} = \bar{a}b + \bar{b}a$ and $\mathrm{Re}(q) = \frac{1}{2}(q + \bar{q})$):

$$(v \circ w)_{11} = \mathrm{Re}(\bar{x}_3 y_3) + \mathrm{Re}(x_2 \bar{y}_2)$$

Note: $\mathrm{Re}(x_2 \bar{y}_2) = \mathrm{Re}(\bar{y}_2 x_2) = \mathrm{Re}(\overline{\bar{x}_2 y_2}) = \mathrm{Re}(\bar{x}_2 y_2)$ since $\mathrm{Re}(\bar{q}) = \mathrm{Re}(q)$ for octonions. So:

$$(v \circ w)_{11} = \mathrm{Re}(\bar{x}_3 y_3) + \mathrm{Re}(\bar{x}_2 y_2)$$

Since $V_1 = \mathbb{R} \cdot E_{11}$, the Peirce projection is:

$$\boxed{P_1(v \circ w) = \bigl[\mathrm{Re}(\bar{x}_3 y_3) + \mathrm{Re}(\bar{x}_2 y_2)\bigr] \cdot E_{11}}$$

This is a **real scalar** times $E_{11}$.

**Verification:** The inner product $\langle x, y \rangle = \mathrm{Re}(\bar{x}y)$ is the standard Euclidean inner product on $\mathbb{O} \cong \mathbb{R}^8$. Therefore:

$$P_1(v \circ w) = \bigl[\langle x_3, y_3 \rangle_{\mathbb{R}^8} + \langle x_2, y_2 \rangle_{\mathbb{R}^8}\bigr] \cdot E_{11}$$

This is the standard real inner product on $V_{1/2} = \mathbb{O}^2 \cong \mathbb{R}^{16}$.

SELF-CRITIQUE CHECKPOINT (Step 3):
1. SIGN CHECK: Signs in $(v \circ w)_{11}$ verified: $\bar{x}_3 y_3$ and $x_2 \bar{y}_2$ are conjugation patterns matching the Hermitian matrix structure. The identity $\bar{a}b + \bar{b}a = 2\mathrm{Re}(\bar{a}b)$ holds for octonions. $\checkmark$
2. FACTOR CHECK: Factor of $1/2$ in Jordan product cancels with factor of 2 from $\bar{a}b + \bar{b}a = 2\mathrm{Re}(\bar{a}b)$. $\checkmark$
3. CONVENTION CHECK: Jordan product $\circ = \frac{1}{2}(ab + ba)$, Peirce under $E_{11}$. Octonion conjugation $\bar{x}$ reverses all imaginary units. $\checkmark$
4. DIMENSION CHECK: $P_1(v \circ w) \in V_1 \cong \mathbb{R}$. The inner product maps $\mathbb{R}^{16} \times \mathbb{R}^{16} \to \mathbb{R}$. $\checkmark$

### Step 4: State-Effect Pairing on V_{1/2}

The observer evaluates states on $V_{1/2}$ elements through the Peirce-projected pairing. For a state $\omega$ on $V_1 \cong \mathbb{R}$ (where $\omega(\alpha E_{11}) = \alpha$ since $\omega(E_{11}) = 1$ by normalization when the observer is at this Peirce slot), the state-effect pairing is:

$$\omega(P_1(v \circ w)) = \mathrm{Re}(\bar{x}_3 y_3) + \mathrm{Re}(\bar{x}_2 y_2) \in \mathbb{R}$$

More generally, if the observer's state is $\omega$ with $\omega(E_{11}) = \alpha$ (not necessarily normalized to 1 on $E_{11}$ alone, since $\omega$ is a state on the full $M_n(\mathbb{C})^{sa}$), then:

$$\omega(P_1(v \circ w)) = \alpha \cdot \bigl[\mathrm{Re}(\bar{x}_3 y_3) + \mathrm{Re}(\bar{x}_2 y_2)\bigr]$$

**Key observation:** $P_1(v \circ w)$ is a real scalar times $E_{11}$, and any state $\omega$ evaluated on a real scalar times $E_{11}$ returns a **real number**. The C-linear extension $\omega^{\mathbb{C}}$ does not produce additional information here because:

$$\omega^{\mathbb{C}}\bigl(P_1(v \circ w)\bigr) = \omega\bigl(P_1(v \circ w)\bigr) \in \mathbb{R}$$

since $P_1(v \circ w) \in V_1 \subset M_n(\mathbb{C})^{sa}$ (already self-adjoint, no imaginary part).

### Step 5: The R-bilinear Form Induced by States

The state-effect pairing defines an $\mathbb{R}$-bilinear form on $V_{1/2}$:

$$B_\omega: V_{1/2} \times V_{1/2} \to \mathbb{R}, \quad B_\omega(v, w) = \omega(P_1(v \circ w))$$

**Properties of $B_\omega$:**

1. **$\mathbb{R}$-bilinear:** Follows from $\mathbb{R}$-linearity of the Jordan product and projection.

2. **Symmetric:** $B_\omega(v, w) = B_\omega(w, v)$ since the Jordan product is commutative: $v \circ w = w \circ v$.

3. **Positive semi-definite:** For $v = w$:
   $$B_\omega(v, v) = \alpha \cdot (\|x_3\|^2 + \|x_2\|^2) \geq 0$$
   when $\alpha = \omega(E_{11}) > 0$ (which holds for any faithful state).

4. **Non-degenerate (for faithful states):** $B_\omega(v, w) = 0$ for all $w$ implies $x_2 = x_3 = 0$, hence $v = 0$.

This is the standard Euclidean inner product on $V_{1/2} \cong \mathbb{R}^{16}$, scaled by the state parameter $\alpha$.

### Step 6: C-Linear Extension and the Complexification Question

**Question:** Does the C-linear extension $\omega^{\mathbb{C}}$ upgrade $B_\omega$ to a $\mathbb{C}$-bilinear or sesquilinear form on $V_{1/2} \otimes_\mathbb{R} \mathbb{C}$?

Consider extending $B_\omega$ to $V_{1/2}^{\mathbb{C}} = V_{1/2} \otimes_\mathbb{R} \mathbb{C}$. There are two ways:

**(a) Sesquilinear extension (Hermitian form):**
$$H(v \otimes z_1, w \otimes z_2) = \bar{z}_1 z_2 \cdot B_\omega(v, w)$$

This gives a Hermitian inner product on $V_{1/2}^{\mathbb{C}}$.

**(b) C-bilinear extension:**
$$B^{\mathbb{C}}(v \otimes z_1, w \otimes z_2) = z_1 z_2 \cdot B_\omega(v, w)$$

This gives a symmetric $\mathbb{C}$-bilinear form.

**However**, neither extension is forced by the state-effect pairing. The pairing $B_\omega(v, w)$ is an $\mathbb{R}$-bilinear form on a real vector space. Both (a) and (b) are standard algebraic extensions that exist for any real bilinear form -- they are not specific to the state-effect duality or the C-linear extension $\omega^{\mathbb{C}}$.

**The critical obstruction:** The C-linear extension $\omega^{\mathbb{C}}$ acts on $M_n(\mathbb{C})$ (the observer's full algebra), not on $V_{1/2}$. When applied to $P_1(v \circ w) \in V_1 \cong \mathbb{R}$, the extension $\omega^{\mathbb{C}}$ returns the same real value as $\omega$ because $P_1(v \circ w)$ is already self-adjoint. The complex structure of the observer's algebra is not transmitted to $V_{1/2}$ through this pairing.

---

## Summary of Part I

The state-effect pairing between observer states $\omega$ and $V_{1/2}$ elements, mediated by the Peirce projection $P_1$, yields an $\mathbb{R}$-bilinear form $B_\omega(v,w) = \omega(P_1(v \circ w))$ that is the standard real inner product on $\mathbb{O}^2 \cong \mathbb{R}^{16}$ (up to a positive scalar). The C-linear extension $\omega^{\mathbb{C}}$ does not produce additional complex structure on $V_{1/2}$ because the Peirce projection $P_1$ maps to $V_1 \cong \mathbb{R}$, which is already self-adjoint.

The question for Part II: does any other Peirce-mediated mechanism transmit the observer's complex structure to $V_{1/2}$?
