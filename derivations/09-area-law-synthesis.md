# Area-Law Synthesis: Which-State Resolution, Jacobson Bridge, and Gap Statement

% ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, coupling_convention=H_sum_hxy, entropy_base=nats, state_normalization=Tr_rho_1, commutation_convention=standard

**Phase:** 09-area-law-derivation, Plan 03
**Date:** 2026-03-22

---

## Part A: The "Which State?" Resolution

### A.1 The Problem

The self-modeling framework (Phases 4-5, Paper 5) specifies the LOCAL algebraic structure:
- Each site carries $A_x = M_n(\mathbb{C})$
- Composites have product-form sequential product: $(a \otimes b) \mathbin{\&} (c \otimes d) = (a \mathbin{\&} c) \otimes (b \mathbin{\&} d)$
- The interaction Hamiltonian is $h_{xy} = JF_{xy}$ (SWAP), forced by diagonal $U(n)$ covariance (Phase 8)

This constrains the interaction but does NOT specify a unique global quantum state. The Hamiltonian $H = \sum_{\langle x,y \rangle} JF_{xy}$ admits infinitely many states: ground states (FM or AFM depending on sign of $J$), thermal states at any temperature, arbitrary excited states, and mixed states of all kinds.

**The question:** Which state has area-law entanglement? The answer depends on which state we consider.

### A.2 Three Complementary Perspectives

We resolve the "which state?" problem by identifying three complementary perspectives, each applicable to a different class of states. Together, they cover the physically relevant state space.

---

### Perspective 1: Thermal States (Any $T > 0$) -- Mutual Information Area Law

**Assumption A1 (Thermal State Identification).** The physically relevant state is a Gibbs state $\rho_\beta = e^{-\beta H}/Z$ at some finite temperature $T = 1/\beta > 0$.

**Result (Plan 01, Eq. 09.3, WVCH 2008):**

$$I(A:B) \leq 2\beta \, |\partial(A)| \, |J| \tag{09-03.1}$$

This is a mutual information area law:
- $I(A:B)$ scales with boundary $|\partial(A)|$, not volume $|A|$
- Holds for BOTH signs of $J$ (depends on $|J|$)
- Holds in ALL spatial dimensions
- Requires no spectral gap
- The von Neumann entropy $S(A)$ itself has a volume-law thermal contribution at finite $T$, but the mutual information -- which captures quantum + classical correlations beyond thermal noise -- obeys area law

**Physical motivation for A1:**
- Gibbs state maximizes von Neumann entropy at fixed energy (MaxEnt)
- Unique KMS state for local Hamiltonians (Bratteli-Robinson, Vol. 2, Theorem 5.3.30)
- For Jacobson's gravity derivation, the relevant state IS thermal: the Unruh vacuum restricted to a Rindler wedge is a thermal state at the Unruh temperature $T_U = a/(2\pi)$

---

### Perspective 2: Pure States -- Von Neumann Entropy Area Law

**Assumption A2 (Pure Global State).** The global state is a pure state $|\psi\rangle \in \mathcal{H}_A \otimes \mathcal{H}_B$.

**Result (Plan 02, Eq. 09-02.1, Channel Capacity + DPI):**

$$S(A) \leq \log(n) \cdot |\partial(A)| \tag{09-03.2}$$

This is a von Neumann entropy area law:
- $S(A)$ scales with boundary, not volume
- Holds for ANY pure state, not just ground states or eigenstates
- Independent of $J$, $\beta$, or the specific Hamiltonian -- depends only on graph structure and local dimension
- Requires no spectral gap

**Physical motivation for A2:**
- A closed quantum system evolving unitarily from a pure initial state remains pure
- In quantum cosmology, the global state of the universe is often taken to be pure

**Derivation chain:** DPI (locality) $\to$ channel capacity per bond ($2\log n$ nats MI) $\to$ pure state identity $I(A:B) = 2S(A)$ $\to$ $S(A) \leq \log(n) \cdot |\partial(A)|$

---

### Perspective 3: Any State, via Entanglement First Law -- THE KEY INSIGHT

**This perspective requires no assumption about which state the system is in.** It addresses what Jacobson's argument actually needs: not that $S(A)$ obeys area law, but that $\delta S$ -- the change in entropy under small perturbations -- scales with boundary area.

**Entanglement First Law.** For a quantum state $\rho$ with reduced state $\rho_A = \mathrm{Tr}_B(\rho)$ and modular Hamiltonian $K_A = -\ln \rho_A$, the first-order change in entanglement entropy under a perturbation $\rho \to \rho + \delta\rho$ is:

$$\delta S(A) = \delta \langle K_A \rangle \tag{09-03.3}$$

This is an EXACT quantum information identity (first-order perturbation theory for von Neumann entropy). It is not an approximation. It holds for any state $\rho$ and any small perturbation $\delta\rho$ satisfying $\mathrm{Tr}(\delta\rho) = 0$.

% IDENTITY_CLAIM: delta S(A) = delta <K_A> (entanglement first law)
% IDENTITY_SOURCE: Blanco, Casini, Hung, Myers 2013, JHEP 1308:060; also standard QI result from first-order expansion of S = -Tr(rho ln rho)
% IDENTITY_VERIFIED: (1) For thermal state: delta S = beta * delta <H>, recovering standard thermodynamic first law. (2) For product state rho_A = |0><0|, K_A = infinity * (1 - |0><0|), delta S = 0 for perturbations within |0><0| -- correct. (3) For maximally mixed rho_A = I/n, K_A = ln(n) * I, delta S = ln(n) * Tr(delta rho_A) = 0 -- correct since Tr(delta rho) = 0.

**Derivation of Eq. (09-03.3):**

$$S(\rho_A + \delta\rho_A) = -\mathrm{Tr}[(\rho_A + \delta\rho_A)\ln(\rho_A + \delta\rho_A)]$$

Expanding to first order in $\delta\rho_A$:

$$\delta S = -\mathrm{Tr}[\delta\rho_A \ln \rho_A] - \mathrm{Tr}[\rho_A \cdot \rho_A^{-1} \delta\rho_A]$$
$$= -\mathrm{Tr}[\delta\rho_A \ln \rho_A] - \mathrm{Tr}[\delta\rho_A]$$
$$= -\mathrm{Tr}[\delta\rho_A \ln \rho_A] \quad (\text{since } \mathrm{Tr}(\delta\rho_A) = 0)$$
$$= \mathrm{Tr}[\delta\rho_A \cdot K_A] = \delta\langle K_A \rangle$$

where $K_A = -\ln \rho_A$ is the modular Hamiltonian. $\square$

SELF-CRITIQUE CHECKPOINT (Eq. 09-03.3 derivation):
1. SIGN CHECK: $K_A = -\ln \rho_A$ (negative sign). $\delta S = -\mathrm{Tr}[\delta\rho_A \ln \rho_A] = +\mathrm{Tr}[\delta\rho_A K_A]$. Signs consistent.
2. FACTOR CHECK: No factors of 2, $\pi$, $\hbar$, $c$ involved. Pure algebraic identity.
3. CONVENTION CHECK: Using $S = -\mathrm{Tr}(\rho \ln \rho)$ in nats. Consistent with convention lock.
4. DIMENSION CHECK: $[\delta S] = [\text{dimensionless}]$. $[\delta\langle K_A \rangle] = [\text{dimensionless}]$ since $K_A = -\ln \rho_A$ is dimensionless (logarithm of dimensionless operator). Consistent.

### A.3 The $\delta S \sim |\partial(A)|$ Argument

The key question: does $\delta\langle K_A \rangle$ scale with $|\partial(A)|$ (boundary) or $|A|$ (volume)?

**Assumption A3 (Modular Hamiltonian Locality).** The modular Hamiltonian $K_A = -\ln \rho_A$ has its dominant support near the entangling surface $\partial(A)$.

This means $K_A$ can be approximated as:

$$K_A \approx \sum_{x \in \partial(A)} k_x + \text{corrections decaying exponentially with distance from } \partial(A) \tag{09-03.4}$$

where $k_x$ are operators supported near boundary site $x$.

**Evidence for A3:**

1. **Bisognano-Wichmann theorem (exact in QFT).** For the vacuum state of a relativistic QFT and the Rindler wedge (half-space), $K_A = 2\pi \int d^{d-1}x \; x_\perp \; T_{00}(x)$, where $x_\perp$ is the distance to the entangling surface. The modular Hamiltonian is a local integral of the stress-energy tensor weighted by distance to the boundary. This is exactly boundary-localized.

2. **Lattice systems with area-law entanglement (Peschel 2003, Eisler-Peschel 2009).** For free-fermion lattice models, $K_A$ is a one-body operator whose matrix elements decay exponentially with distance from the entangling surface. The decay length is the correlation length $\xi$.

3. **General argument from locality of $H$.** The Hamiltonian $H = \sum_{\langle x,y \rangle} JF_{xy}$ is nearest-neighbor. The Lieb-Robinson bound (Phase 8) establishes that information propagates at finite velocity $v_{LR} = 8eJ/(e-1)$. Perturbations at distance $d$ from the boundary affect $\rho_A$ (and hence $K_A$) only through the light-cone propagation, which is exponentially suppressed beyond $d \sim v_{LR} \cdot t$. For static perturbations, the relevant "time" is the thermal time $\beta$ (or the inverse gap), giving a locality scale.

**Consequence.** For local perturbations $\delta H$ supported near the boundary $\partial(A)$:

$$\delta\langle K_A \rangle = \mathrm{Tr}[\delta\rho_A \cdot K_A] \sim O(|\partial(A)|) \tag{09-03.5}$$

because (i) $\delta\rho_A$ is localized near the boundary (local perturbation), and (ii) $K_A$ has its dominant support near the boundary (Assumption A3). The overlap of two boundary-localized operators scales as the boundary area.

**Dimensional check:** $[\delta\langle K_A \rangle] = [\text{dimensionless}]$, $[|\partial(A)|] = [\text{count}]$. The proportionality constant is dimensionless. Consistent.

Therefore:

$$\boxed{\delta S(A) = \delta\langle K_A \rangle \sim O(|\partial(A)|) \quad \text{for local perturbations}} \tag{09-03.6}$$

**This is what Jacobson's argument needs.** Not that $S(A)$ itself scales with boundary, but that changes $\delta S(A)$ under local perturbations scale with boundary.

---

## Part B: Jacobson Bridge -- What Phase 10 Needs

Jacobson's 2016 entanglement equilibrium argument (PRL 116, 201101) derives Einstein's equation from thermodynamic principles applied to entanglement entropy. The argument requires three inputs:

### (J1) Area-Law Entanglement Structure

**Jacobson needs:** $\delta S(A) \sim |\partial(A)|$ for a small geodesic ball $A$. That is, changes in entanglement entropy under perturbations scale with the boundary area.

**Phase 9 delivers:** Perspective 3 establishes exactly this. Eq. (09-03.6) gives $\delta S(A) = \delta\langle K_A \rangle \sim O(|\partial(A)|)$ for local perturbations, under Assumption A3 (modular Hamiltonian locality).

Additionally, the static area-law bounds from Perspectives 1 and 2 provide independent evidence:
- Thermal MI: $I(A:B) \leq 2\beta|\partial||J|$ (Perspective 1, A1)
- Pure-state S: $S(A) \leq \log(n)|\partial|$ (Perspective 2, A2)

**Status: ESTABLISHED** (under A3 for the $\delta S$ route; under A1 or A2 for the static bounds).

### (J2) Entanglement First Law

**Jacobson needs:** $\delta S = \delta\langle K \rangle$ where $K$ is the modular Hamiltonian.

**Phase 9 delivers:** Eq. (09-03.3) is an exact QI identity. No additional assumptions needed.

**Status: EXACT IDENTITY** -- always holds.

### (J3) Maximal Vacuum Entanglement Hypothesis (MVEH)

**Jacobson needs:** Among all states with the same expectation value of $T_{\mu\nu}$ (the stress-energy tensor), the vacuum state maximizes the entanglement entropy $S(A)$.

**Phase 9 status:** NOT ESTABLISHED for the self-modeling lattice. The MVEH is a physical hypothesis about the vacuum state that goes beyond what the area-law analysis provides.

**Status: OPEN GAP** -- the main remaining challenge for Phase 10.

### Jacobson Interface Summary

| Jacobson Input | Content | Phase 9 Status | Assumption |
|---|---|---|---|
| (J1) | $\delta S \sim |\partial|$ | Established (Eq. 09-03.6) | A3 (modular $K$ locality) |
| (J2) | $\delta S = \delta\langle K\rangle$ | Exact identity (Eq. 09-03.3) | None |
| (J3) | MVEH | NOT established | Phase 10 gap |

---

## Part C: Why Ground-State Analysis Alone Is Insufficient

### C.1 Ferromagnetic Ground State ($J < 0$)

From Plan 01 (derivations/09-heisenberg-entanglement.md):
- Ground state: product state $|\uparrow\cdots\uparrow\rangle$ (and SU(2) rotations)
- Entanglement: $S(A) = 0$ for all $A$
- Gap: $\Delta_{FM} \sim 2\pi^2|J|/N^2 \to 0$

Area law is trivially satisfied ($S = 0$), but zero entanglement is useless for Jacobson: $\delta S = 0$ for local perturbations of a product state (to first order), which means the entanglement-thermodynamic argument has no content.

### C.2 Antiferromagnetic Ground State ($J > 0$)

From Plan 01 (derivations/09-heisenberg-entanglement.md):
- Ground state: Bethe ansatz singlet (1D), Neel order ($d \geq 2$)
- Entanglement in 1D: $S(L) = \frac{1}{3}\ln L + \text{const}$ (Calabrese-Cardy, $c = 1$ CFT)
- Gap: $\Delta_{AFM} = 0$ (exactly gapless, des Cloizeaux-Pearson 1962)

The logarithmic scaling $S \sim \ln L$ violates the strict area law $S = \text{const}$ in 1D. This is not a fatal problem (the correction is much weaker than volume-law), but it means ground-state analysis alone does not give a clean area law.

### C.3 The Takeaway

| Sign | Ground-State $S(A)$ | Area Law? | Useful for Jacobson? |
|---|---|---|---|
| $J < 0$ (FM) | $0$ | Trivially yes | No ($\delta S = 0$) |
| $J > 0$ (AFM) | $(1/3)\ln L$ in 1D | Log-corrected, not strict | Partially (nontrivial $\delta S$, but log not area) |

**Neither sign gives a clean area law from ground-state analysis.** This is why Perspectives 1-3 are essential: they establish area-law structure through information-theoretic (Perspective 2), thermodynamic (Perspective 1), and perturbative (Perspective 3) routes that do not rely on ground-state properties.

### C.4 Hastings Does Not Apply

Hastings 2007 (JSTAT P08024) requires a spectral gap $\Delta > 0$. As established in Plan 01:
- FM: $\Delta \sim O(1/N^2) \to 0$ (gapless)
- AFM: $\Delta = 0$ exactly (Bethe ansatz)

The gap condition fails for both signs. Hastings is cited as a foil (an inapplicable theorem), not as a supporting result.

---

## Part D: Sign-of-$J$ Ambiguity Resolution for Gravity

Phase 8 established that the coupling constant $J$ is undetermined in sign by the self-modeling (sequential product) constraints. We address this ambiguity for the gravity connection.

### D.1 Sign Independence of Area-Law Results

1. **WVCH bound (Perspective 1):** $I(A:B) \leq 2\beta|\partial||J|$ depends on $|J|$, not $\text{sign}(J)$. Sign-independent.

2. **Channel capacity bound (Perspective 2):** $S(A) \leq \log(n)|\partial|$ is entirely $J$-independent. Sign-independent.

3. **$\delta S$ scaling (Perspective 3):** $\delta S \sim |\partial|$ depends on locality of $H$ and modular Hamiltonian $K$. The locality of $H$ (nearest-neighbor with $\|h_{xy}\| = |J|$) is sign-independent. The Lieb-Robinson velocity $v_{LR} = 8e|J|/(e-1)$ depends on $|J|$. Sign-independent.

**All three area-law results are sign-independent.**

### D.2 Physical Selection for Gravity

While the area-law argument itself is sign-independent, the gravity application likely requires a physically selected sign:

1. **FM ($J < 0$) ground state:** Product state with $S = 0$ and $\delta S = 0$ to first order. Cannot drive Jacobson's argument, which requires nontrivial $\delta S$.

2. **AFM ($J > 0$) ground state:** Nontrivial entanglement ($S \sim \ln L$ in 1D, area law in $d \geq 2$) with nontrivial $\delta S$. Can potentially drive Jacobson's argument.

3. **Thermal state (either sign):** At any finite $T > 0$, the thermal state has nontrivial correlations and nontrivial $\delta S$ for both signs of $J$.

**Conclusion:** The area-law argument is sign-independent (all three perspectives work for both signs). For the gravity application, the physically relevant regime is either:
- $J > 0$ (AFM) at any temperature, or
- Any $J \neq 0$ at finite temperature $T > 0$

This is NOT an additional assumption -- it is a physical selection criterion. The self-modeling constraints do not select the sign; the gravity application selects the physically relevant regime.

---

SELF-CRITIQUE CHECKPOINT (Task 1 complete):
1. SIGN CHECK: All three perspectives checked for sign dependence. WVCH: |J|. Channel capacity: J-free. delta S: |J| via v_LR. No sign errors.
2. FACTOR CHECK: No new factors of 2, pi, hbar introduced beyond those inherited from Plans 01-02. Entanglement first law derivation introduces no numerical factors.
3. CONVENTION CHECK: Entropy in nats, H = sum h_xy, K_A = -ln(rho_A). All consistent with convention lock.
4. DIMENSION CHECK: [delta S] = [dimensionless], [delta <K_A>] = [dimensionless], [|boundary|] = [count]. All consistent.

All checks pass.
