# KMS Equilibrium and Modular Hamiltonian = Boost Identification

% ASSERT_CONVENTION: natural_units=natural (hbar=1 k_B=1 a=1), metric_signature=mostly_minus (-,+,...,+) for emergent Lorentzian spacetime, modular_hamiltonian=K_A=-ln(rho_A), kms_temperature=beta=2pi for Rindler, unruh_temperature=T_U=a/(2pi), modular_parameter=s with physical Rindler time tau=2pi*s, coupling_convention=J>0 AFM

**Phase 35, Plan 02 -- BWEQ-02**

---

## Part I: KMS Property Derived from BW

### Step 1: Logical Chain and Non-Circularity

The derivation in this document follows a strict logical order. Each step uses only results established in earlier steps or earlier phases:

1. **Phase 34 (INPUT):** Emergent Lorentz invariance with metric $ds^2 = -c_s^2 \, dt^2 + \delta_{ij} \, dx^i dx^j$, $c_s = 1.659 \, Ja$ (Eq. (34.30)). DLS 1978 reflection positivity on bipartite lattice. *NOT derived here.*

2. **Plan 01 (INPUT):** Bisognano-Wichmann identification $K_A = 2\pi K_{\text{boost}}$ for the vacuum restricted to the right Rindler wedge (Eq. (35.0a)). Wightman axioms W1--W4 satisfied, W5 conditional, W6 open; lattice-BW route as primary mitigation. SRF = 0.9993 validates BW locality. *NOT derived here.*

3. **This derivation (Plan 02):** BW $\to$ modular flow = boost $\to$ Tomita-Takesaki KMS $\to$ physical Unruh temperature $T_U = a/(2\pi)$ $\to$ local equilibrium $\theta = \sigma = 0$ at bifurcation surface.

The logical flow is:

$$
\boxed{
\text{Phase 34 (Lorentz)} \;\longrightarrow\; \text{Plan 01 (BW)} \;\longrightarrow\; \text{Plan 02 (KMS + equilibrium)} \;\longrightarrow\; \text{Phase 36 (Jacobson)}
}
$$

No step in this chain uses a later result. In particular, BW does NOT establish Lorentz invariance -- it uses it (via W2, established in Phase 34).

---

### Step 2: BW Identification (from Plan 01)

From Plan 01, the Bisognano-Wichmann theorem applied to the right Rindler wedge $W_R = \{x \in \mathbb{R}^{d+1} : x^1 > |x^0|\}$ gives:

$$
\Delta_\Omega^{it} = U(\Lambda(-2\pi t)) \qquad \forall t \in \mathbb{R} \tag{35.0}
$$

Equivalently, the modular Hamiltonian is:

$$
K_A = -\ln \Delta_\Omega = 2\pi K_{\text{boost}} \tag{35.0a}
$$

where $K_{\text{boost}}$ generates Lorentz boosts preserving $W_R$. The factor of $2\pi$ is load-bearing.

**Source:** Bisognano & Wichmann, *JMP* **16**, 985 (1975); *JMP* **17**, 303 (1976). Stated in Plan 01, Eq. (35.0a).

---

### Step 3: The Modular Automorphism Group (Tomita-Takesaki)

Let $\mathcal{R}(W_R)$ be the von Neumann algebra of observables localized in $W_R$, and let $|\Omega\rangle$ be the vacuum state. By Tomita-Takesaki theory (Bratteli-Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vol. 2, Ch. 2.5), the pair $(\mathcal{R}(W_R), |\Omega\rangle)$ determines a unique one-parameter automorphism group $\sigma_t : \mathcal{R}(W_R) \to \mathcal{R}(W_R)$:

$$
\sigma_t(A) = \Delta^{it} \, A \, \Delta^{-it} \tag{35.7}
$$

where $\Delta = e^{-K_A}$ is the modular operator.

**The key theorem** (Tomita-Takesaki + HHW): The state $\omega(\cdot) = \langle\Omega|\cdot|\Omega\rangle$ satisfies the **KMS condition** at inverse temperature $\beta_{\text{mod}} = 1$ with respect to $\sigma_t$. Explicitly, for all $A, B \in \mathcal{R}(W_R)$:

> There exist functions $F_{A,B}(z)$ analytic in the strip $0 < \text{Im}(z) < 1$ and continuous on the closure, with boundary values:
>
> $$
> F_{A,B}(t) = \omega(A \, \sigma_t(B)), \qquad F_{A,B}(t + i) = \omega(\sigma_t(B) \, A) \tag{35.8}
> $$

This is the KMS condition at $\beta_{\text{mod}} = 1$ in modular time $t$.

**Source:** Haag, Hugenholtz, Winnink, *CMP* **5**, 215 (1967) -- definition of KMS states. Bratteli-Robinson Vol. 2, Theorem 2.5.31 -- Tomita-Takesaki uniqueness of the modular group. The Tomita-Takesaki theorem and KMS property are *cited*, not re-derived.

---

### Step 4: Modular Flow = Lorentz Boost (Applying BW)

Substituting the BW identification $K_A = 2\pi K_{\text{boost}}$ (Eq. (35.0a)) into the modular automorphism (Eq. (35.7)):

$$
\sigma_t(A) = e^{i(2\pi K_{\text{boost}})t} \, A \, e^{-i(2\pi K_{\text{boost}})t} = U(\Lambda(-2\pi t)) \, A \, U(\Lambda(-2\pi t))^{-1} \tag{35.9}
$$

where $\Lambda(s)$ is a Lorentz boost by rapidity $s$ in the $x^1$ direction. The modular flow $\sigma_t$ acts as a Lorentz boost by rapidity $-2\pi t$.

SELF-CRITIQUE CHECKPOINT (Step 4):
1. SIGN CHECK: The sign in the rapidity is $-2\pi t$ (from the BW convention $\Delta^{it} = U(\Lambda(-2\pi t))$). Expected: 1 sign. Actual: 1 sign (the minus in $-2\pi t$). Consistent with BW.
2. FACTOR CHECK: Factor of $2\pi$ from $K_A = 2\pi K_{\text{boost}}$ correctly propagated.
3. CONVENTION CHECK: Using mostly-minus metric, $K_{\text{boost}}$ generates boosts in $x^1$. Consistent.
4. DIMENSION CHECK: $[K_{\text{boost}}] = [\text{dimensionless}]$ (generates dimensionless rapidity), $[t] = [\text{dimensionless}]$ (modular parameter). $[2\pi t] = [\text{dimensionless}]$ (rapidity). Consistent.

By Step 3 (Tomita-Takesaki), the vacuum $\omega$ is KMS at $\beta_{\text{mod}} = 1$ with respect to $\sigma_t$. Since $\sigma_t$ acts as a boost by rapidity $2\pi t$, this means:

> **The Minkowski vacuum restricted to the Rindler wedge $W_R$ is KMS at $\beta_{\text{mod}} = 1$ with respect to the boost flow parameterized by modular time $t$.**

This is the KMS property *derived* from BW, not assumed.

---

### Step 5: Physical Temperature -- From Modular Time to Proper Time

The modular parameter $t$ is dimensionless and abstract. To extract a physical temperature, we must relate it to the proper time of a specific observer.

**Rindler observer:** A uniformly accelerated observer with proper acceleration $a$ follows the worldline:

$$
x^0(\tau) = \frac{1}{a} \sinh(a\tau), \qquad x^1(\tau) = \frac{1}{a} \cosh(a\tau) \tag{35.10}
$$

where $\tau$ is the proper time. One verifies:

- At $\tau = 0$: position is $(0, 1/a)$ -- on the positive $x^1$ axis, inside $W_R$.
- The four-velocity is $u^\mu = (\cosh(a\tau), \sinh(a\tau))$, with $u^\mu u_\mu = -1$ (timelike, correctly normalized in the $(-,+,\ldots,+)$ metric).
- The four-acceleration is $a^\mu = (a \sinh(a\tau), a \cosh(a\tau))$, with $a^\mu a_\mu = +a^2$. The proper acceleration magnitude is $a$.

The boost rapidity along this worldline is $\eta = a\tau$. A boost by rapidity $s$ advances the proper time by $\Delta\tau = s/a$.

The modular flow $\sigma_t$ boosts by rapidity $2\pi t$. This corresponds to a proper time advance of:

$$
\Delta\tau = \frac{2\pi t}{a} \tag{35.11}
$$

Therefore the modular parameter and proper time are related by:

$$
t = \frac{a \, \tau}{2\pi} \tag{35.12}
$$

The KMS condition at $\beta_{\text{mod}} = 1$ in modular time $t$ becomes a KMS condition in proper time $\tau$ at:

$$
\beta_{\text{phys}} = \frac{\beta_{\text{mod}} \cdot 2\pi}{a} = \frac{2\pi}{a} \tag{35.13}
$$

The physical (Unruh) temperature is:

$$
\boxed{T_U = \frac{1}{\beta_{\text{phys}}} = \frac{a}{2\pi}} \tag{35.3}
$$

For unit acceleration $a = 1$ (in natural units): $T_U = 1/(2\pi) \approx 0.1592$.

SELF-CRITIQUE CHECKPOINT (Step 5):
1. SIGN CHECK: All positive -- acceleration $a > 0$, temperature $T_U > 0$, $\beta_{\text{phys}} > 0$. No sign issues. Expected: 0 sign changes. Actual: 0.
2. FACTOR CHECK: The $2\pi$ enters once from $K_A = 2\pi K_{\text{boost}}$ (Step 2) and propagates to $\beta_{\text{phys}} = 2\pi/a$. No extra factors of $2\pi$ introduced or dropped. Verified: $\beta_{\text{mod}} = 1 \to \beta_{\text{phys}} = 2\pi/a$ via $t = a\tau/(2\pi)$.
3. CONVENTION CHECK: Using $\hbar = 1$, $k_B = 1$, $c_s = 1$ (natural units for the emergent spacetime). The formula $T_U = a/(2\pi)$ is the standard result.
4. DIMENSION CHECK: $[T_U] = [a/(2\pi)] = [\text{acceleration}]/([\text{dimensionless}]) = [\text{energy}]$ in natural units ($\hbar = k_B = c = 1$). For the emergent spacetime: proper acceleration has dimensions of $[\text{energy}]$ (since $[a] = [v/t] = [1/\text{length}] = [\text{energy}]$ with $\hbar = c = 1$). Consistent: $[T_U] = [\text{energy}]$.

**Tracing the $2\pi$ factor end-to-end:**

| Step | Expression | The $2\pi$ |
|------|-----------|-------------|
| BW identification | $K_A = 2\pi K_{\text{boost}}$ | Introduced here |
| Modular flow | $\sigma_t =$ boost by $2\pi t$ | Carried through |
| TT KMS | $\beta_{\text{mod}} = 1$ in modular time | $\beta_{\text{mod}}$ is dimensionless, $= 1$ |
| Proper time relation | $t = a\tau/(2\pi)$ | Inverted to relate times |
| Physical KMS | $\beta_{\text{phys}} = 2\pi/a$ | The $2\pi$ from BW becomes the $2\pi$ in $T_U$ |
| Unruh temperature | $T_U = a/(2\pi)$ | Final result |

No factor of $2\pi$ is doubled or dropped. The $2\pi$ in $T_U = a/(2\pi)$ descends directly and uniquely from the $2\pi$ in $K_A = 2\pi K_{\text{boost}}$.

---

### Step 6: Rindler Observer and the Unruh Effect

The result of Step 5 is the **Unruh effect** (Unruh, *PRD* **14**, 870 (1976)):

> A uniformly accelerated observer with proper acceleration $a$ in the Minkowski vacuum perceives a thermal bath at temperature $T_U = a/(2\pi)$.

The Rindler observer's worldline (Eq. (35.10)) is confined to the right Rindler wedge $W_R$. The Rindler horizon, from this observer's perspective, is the boundary $\partial W_R = \{x^1 = |x^0|\}$. The bifurcation surface is the intersection of this boundary with the $t = 0$ surface:

$$
B = \{x : x^0 = 0, \; x^1 = 0\} \tag{35.14}
$$

The physical picture: the vacuum fluctuations, when restricted to the causal domain $W_R$ accessible to the accelerated observer, have the statistics of a thermal state. The modular Hamiltonian $K_A = 2\pi K_{\text{boost}}$ acts as the "thermal Hamiltonian" for this observer, and the KMS condition ensures all correlation functions satisfy the periodicity in imaginary time characteristic of thermal equilibrium.

---

### Step 7: Lattice Cross-Check -- Position-Dependent Effective Temperature

On the finite lattice, the "KMS property" manifests as the thermal structure of the reduced density matrix $\rho_A = e^{-H_{\text{ent}}}/Z$, where the entanglement Hamiltonian is the lattice-BW form (Eq. (35.1) from Plan 01):

$$
H_{\text{ent}}^{\text{BW}} = \frac{2\pi}{c_s} \sum_{x \in A} x_\perp \, h_x \tag{35.1}
$$

The coefficient of $h_x$ at site $x_\perp$ is $2\pi x_\perp / c_s$, which plays the role of the position-dependent effective inverse temperature:

$$
\beta_{\text{eff}}(x_\perp) = \frac{2\pi \, x_\perp}{c_s} \tag{35.2}
$$

This is the lattice analog of the Rindler temperature profile: the Unruh temperature for a Rindler observer at distance $x_\perp$ from the horizon (measured in units where $c_s = 1$) is $T(x_\perp) = c_s/(2\pi x_\perp)$, which diverges at the horizon ($x_\perp \to 0$) and vanishes far from it ($x_\perp \to \infty$). Eq. (35.2) reproduces this behavior.

The SRF = 0.9993 (Plan 01, Step 9) confirms that this thermal structure is quantitatively accurate: 99.93% of the modular Hamiltonian's Frobenius weight resides in the range-1 (nearest-neighbor) terms predicted by the BW structure.

**On the finite lattice, the "KMS property" is formal:** the reduced density matrix $\rho_A$ is a Gibbs state $e^{-H_{\text{ent}}}/Z$ on a finite-dimensional type I algebra, which is a standard thermal state. The rigorous KMS property (in the sense of HHW 1967, requiring the analytic continuation Eq. (35.8)) holds only in the thermodynamic limit where the algebra becomes type III$_1$. On the lattice, $\rho_A$ is thermal in the Gibbs sense, which is the finite-dimensional shadow of the continuum KMS property.
