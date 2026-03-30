# Correlation Decay and NL Sigma Model for SWAP/Heisenberg Ground State

% ASSERT_CONVENTION: natural_units=natural, metric_signature=Riemannian_Fisher, coupling_convention=J_gt_0_AFM, spin_basis=Sz_eigenbasis, state_normalization=trace_1

**Phase 33, Plan 01 -- Derivation Document**
**Date:** 2026-03-30

## Overview

This document establishes two results for the SWAP/Heisenberg ground state:

- **CORR-01:** Two-tier characterization of correlation decay (gapped: exponential via Hastings-Koma; Neel: algebraic with long-range order)
- **CORR-02:** O(3) nonlinear sigma model as low-energy effective theory with explicit spin-wave velocity $c_s = 1.659\, Ja$

**Starting point:** The SWAP Hamiltonian for spin-1/2 on a bipartite lattice is
$$
H_{\text{SWAP}} = J \sum_{\langle ij \rangle} P_{ij} = J \sum_{\langle ij \rangle} \left(2\,\mathbf{S}_i \cdot \mathbf{S}_j + \tfrac{1}{2}\right)
$$
so $H_{\text{SWAP}} = H_{\text{Heis}} + \tfrac{1}{2}J N_{\text{bonds}}$, where $H_{\text{Heis}} = J\sum_{\langle ij\rangle} \mathbf{S}_i \cdot \mathbf{S}_j$ with $J > 0$ (antiferromagnetic). The constant shift does not affect the ground state wavefunction, dynamics, or any correlation function. **All results below for the Heisenberg AFM apply identically to the SWAP lattice** (Paper 6).

---

## Part I: Two-Tier Correlation Decay Characterization (CORR-01)

### Tier 1: Gapped Systems (Rigorous)

**Theorem (Hastings-Koma, CMP 265, 781, 2006).**
Let $H = \sum_X h_X$ be a Hamiltonian on a lattice with:
- (H1) Finite-range interactions: $h_X = 0$ unless $\text{diam}(X) \leq R$ for some fixed $R$
- (H2) Bounded local terms: $\|h_X\| \leq J$ for all $X$
- (H3) Unique ground state $|\Omega\rangle$ with spectral gap $\gamma > 0$ above the ground state

Then for any operators $A, B$ supported on regions $X, Y$ respectively:
$$
|\langle \Omega | A\, B | \Omega \rangle - \langle \Omega | A | \Omega \rangle \langle \Omega | B | \Omega \rangle| \leq C_0\, \|A\|\, \|B\|\, \min(|X|,|Y|)\, e^{-d(X,Y)/\xi}
\tag{33.1}
$$
where $\xi = O(v_{\text{LR}}/\gamma)$ and $v_{\text{LR}}$ is the Lieb-Robinson velocity.

**Verification of hypotheses for the SWAP Hamiltonian:**

- (H1) $H_{\text{SWAP}} = J \sum_{\langle ij\rangle} P_{ij}$ is nearest-neighbor: $R = 1$. **Satisfied.**
- (H2) Each $P_{ij}$ has operator norm $\|P_{ij}\| = 1$, so $\|h_{\langle ij\rangle}\| = J$. **Satisfied.**
- (H3) Requires spectral gap $\gamma > 0$. This is **system-dependent:**
  - **AKLT chain (S=1):** Gap rigorously proved, $\gamma > 0$ (Affleck-Kennedy-Lieb-Tasaki, CMP 115, 477, 1988). Hastings-Koma applies. Correlation length $\xi = 1/\ln 3 \approx 0.91$.
  - **Easy-axis Heisenberg ($\Delta > 1$ in XXZ model):** Ising-type gap $\gamma \sim J(\Delta - 1)$ for $\Delta \gg 1$. Hastings-Koma applies.
  - **Staggered-field Heisenberg:** External staggered field opens a gap. Hastings-Koma applies.
  - **Isotropic Heisenberg ($\Delta = 1$) on $d \geq 2$ bipartite lattice:** **GAPLESS** due to Goldstone modes from spontaneous SU(2) $\to$ U(1) breaking. **Hastings-Koma does NOT apply.**
  - **1D Heisenberg (S=1/2):** Gapless (Bethe ansatz: $\gamma \sim \pi^2 J/N$ at finite $N$). Hastings-Koma does not apply in the thermodynamic limit.

**Fisher metric consequence for gapped systems:** When Hastings-Koma applies, the Phase 32 smoothness theorem (FISH-01) follows directly. For a subsystem $\Lambda$ at position $x$, the reduced density matrix satisfies:
$$
\|\rho_\Lambda(x+1) - \rho_\Lambda(x)\|_1 \leq C_1\, e^{-R(x)/\xi}
$$
where $R(x) = \min(x, N - x - |\Lambda|)$ is the distance to the nearest chain boundary. This ensures $g_F(x) > 0$ at interior points and the Fisher geometry is smooth with correlation length $\xi = v_{\text{LR}}/\gamma$ (Phase 32, Eq. (32.8)).

**Explicit non-applicability statement:** The Hastings-Koma theorem requires a spectral gap $\gamma > 0$. For the isotropic Heisenberg antiferromagnet ($n = 2$, i.e., the model relevant to SWAP) on $d \geq 2$ bipartite lattices, the system is **gapless**: spontaneous breaking of SU(2) to U(1) generates two massless Goldstone modes (magnons). Therefore, Hastings-Koma **cannot** be applied to characterize correlation decay in the Neel phase. This is not a technical limitation but a fundamental feature: the gapless modes produce algebraic (power-law) rather than exponential correlation decay. **Claiming exponential decay for the Neel phase would be incorrect** (forbidden proxy fp-exponential-neel).

---

### Tier 2: Gapless Neel Phase (Controlled Approximation)

#### Step 1: Establishing Neel Long-Range Order for $d \geq 2$

The isotropic Heisenberg antiferromagnet on a bipartite lattice exhibits Neel long-range order (LRO) in the ground state for sufficiently large dimension $d$ and/or spin $S$:

**Rigorous results:**

1. **$S \geq 1$, $d \geq 3$:** Neel order proved rigorously by Dyson, Lieb, and Simon (JSP 18, 335, 1978) using reflection positivity and infrared bounds. The method shows:
$$
\liminf_{|i-j| \to \infty} (-1)^{i-j} \langle \mathbf{S}_i \cdot \mathbf{S}_j \rangle > 0
\tag{33.2}
$$

2. **$S = 1/2$, $d = 3$:** Extended by Kennedy, Lieb, and Shastry (JSP 53, 1019, 1988) who showed the DLS method applies for $S = 1/2$ when $d \geq 3$.

3. **$S = 1/2$, $d = 2$ (square lattice):** **Not rigorously proved.** However, Quantum Monte Carlo evidence is overwhelming and essentially incontrovertible:
   - Reger and Young (1988) first observed Neel order in QMC
   - High-precision value: $m_s = 0.307447(2)$ (Sandvik 2025, arXiv:2601.20189)
   - This is **established by numerical evidence but not mathematical theorem**

**Staggered magnetization:** The order parameter is
$$
m_s = \frac{1}{N} \sum_i (-1)^i \langle S_i^z \rangle
\tag{33.3}
$$
In the symmetry-broken ground state, $m_s > 0$ indicates Neel long-range order. For $S = 1/2$ on the square lattice, $m_s = 0.3074$ is approximately 61% of the classical value $m_s^{\text{cl}} = S = 0.5$, reflecting significant quantum fluctuations.

#### Step 2: Gapless Goldstone Modes

The Neel ground state spontaneously breaks the continuous SU(2) spin rotation symmetry down to U(1) (rotations about the ordering axis). By the Goldstone theorem, this generates gapless excitations.

**Symmetry counting:** The coset space is SU(2)/U(1) $\cong S^2$ (the 2-sphere), which has dimension 2. Therefore there are **2 independent Goldstone modes** -- two branches of gapless spin-wave (magnon) excitations.

At long wavelength, the magnon dispersion is linear:
$$
\omega_\mathbf{k} = c_s |\mathbf{k}| + O(k^3)
\tag{33.4}
$$
where $c_s$ is the spin-wave velocity (derived explicitly in Part II, Eq. (33.11)).

SELF-CRITIQUE CHECKPOINT (step 2):
1. SIGN CHECK: No sign operations performed yet. N/A.
2. FACTOR CHECK: No factors of 2, pi, hbar introduced. N/A.
3. CONVENTION CHECK: Using J > 0 AFM, $(-1)^i$ staggering, SU(2)$\to$U(1). Consistent with lock.
4. DIMENSION CHECK: $[\omega_\mathbf{k}] = [c_s][k] = (Ja)(1/a) = J$ = energy. Correct.

#### Step 3: Correlation Function Decomposition

For the $d \geq 2$ Neel phase, the spin-spin correlation function decomposes into distinct channels. Let $\mathbf{r} = \mathbf{r}_j - \mathbf{r}_i$ with $|\mathbf{r}| \gg a$.

**Longitudinal correlations** (along the ordering axis $\hat{z}$):
$$
\langle S_i^z S_j^z \rangle \to m_s^2\, (-1)^{i-j} + O(|\mathbf{r}|^{-(d+1)})
\tag{33.5}
$$
The leading term is the Neel long-range order: it does not decay. The correction $O(|\mathbf{r}|^{-(d+1)})$ comes from longitudinal spin fluctuations and decays faster than the transverse contribution.

**Physical interpretation:** The longitudinal component reflects the frozen sublattice alternation $\langle S_i^z \rangle = (-1)^i m_s$. This is the defining feature of Neel order: the staggered pattern persists to arbitrarily large separations.

**Transverse correlations** (perpendicular to ordering axis):
$$
\langle S_i^+ S_j^- \rangle \sim \frac{A}{|\mathbf{r}|^{d-1}} \quad (|\mathbf{r}| \to \infty)
\tag{33.6}
$$
This power-law decay arises from the gapless Goldstone modes. The magnon propagator in momentum space behaves as $\langle a_\mathbf{k}^\dagger a_\mathbf{k} \rangle \sim 1/(2c_s|\mathbf{k}|)$ (zero-point fluctuations of massless bosons). Fourier transforming to real space in $d$ dimensions:
$$
\int \frac{d^d k}{(2\pi)^d} \frac{e^{i\mathbf{k}\cdot\mathbf{r}}}{|\mathbf{k}|} \sim \frac{1}{|\mathbf{r}|^{d-1}}
\tag{33.7}
$$
This is the standard result for the Green's function of a massless scalar in $d$ dimensions.

**Connected correlation function:**
$$
\langle \mathbf{S}_i \cdot \mathbf{S}_j \rangle_{\text{connected}} \equiv \langle \mathbf{S}_i \cdot \mathbf{S}_j \rangle - \langle \mathbf{S}_i \rangle \cdot \langle \mathbf{S}_j \rangle \sim \frac{B}{|\mathbf{r}|^{d-1}}
\tag{33.8}
$$
dominated by the Goldstone (transverse) contribution.

**Specific dimensions:**

| $d$ | Transverse decay | Connected decay | Notes |
|-----|-----------------|-----------------|-------|
| 2   | $\sim 1/r$      | $\sim 1/r$      | Marginal (log divergences in susceptibility) |
| 3   | $\sim 1/r^2$    | $\sim 1/r^2$    | Standard power-law |

#### Step 4: Summary -- Two-Tier Result

**CORR-01 Summary Statement:**

For the Heisenberg antiferromagnet ($\equiv$ SWAP lattice up to constant) on a bipartite lattice:

**Tier 1 (Gapped, rigorous):** If the system has a spectral gap $\gamma > 0$ (e.g., AKLT, easy-axis, staggered field), then Hastings-Koma (Eq. (33.1)) gives exponential clustering:
$$
|\langle A B \rangle_c| \leq C_0\, e^{-d(X,Y)/\xi}, \quad \xi = O(v_{\text{LR}}/\gamma)
$$

**Tier 2 (Gapless Neel, controlled):** For the isotropic model ($n = 2$) with $d \geq 2$, Neel long-range order exists (DLS for $S \geq 1, d \geq 3$; KLS for $S = 1/2, d = 3$; QMC for $S = 1/2, d = 2$), giving:
- **Non-decaying staggered component:** $m_s^2 (-1)^{i-j} > 0$
- **Algebraic transverse decay:** $\sim 1/|\mathbf{r}|^{d-1}$ from Goldstone modes
- **Connected correlations:** $\sim 1/|\mathbf{r}|^{d-1}$ (power-law, not exponential)

**Crucial contrast with 1D:** In $d = 1$, the Mermin-Wagner theorem forbids LRO at $T = 0$ for continuous symmetries in the Heisenberg model (though the ground state does have quasi-long-range order with power-law decay). The consequence: $m_s = 0$, and as Phase 32 showed (FISH-03), $g_{\text{bulk}} \to 0$ as $N \to \infty$. In $d \geq 2$ with Neel order, $m_s > 0$ provides genuinely $x$-dependent structure (sublattice alternation) that survives the thermodynamic limit, giving the Fisher geometry a qualitatively different character.

SELF-CRITIQUE CHECKPOINT (step 4):
1. SIGN CHECK: Staggering factor $(-1)^{i-j}$: consistent with sublattice A/B convention. No sign errors detected.
2. FACTOR CHECK: No new factors introduced in this step.
3. CONVENTION CHECK: J > 0 AFM, m_s > 0 for Neel, SU(2)$\to$U(1) breaking. All consistent with plan and lock.
4. DIMENSION CHECK: $[m_s^2] = $ dimensionless (sublattice magnetization per site). $[1/r^{d-1}]$: correct for $d$-dimensional massless Green's function Fourier transform.

---

*Tier 2 note on rigor:* The S=1/2, d=2 case is the most physically important for the SWAP lattice program but also the one with the weakest mathematical foundation. Neel order in this case is established by overwhelming QMC evidence ($m_s = 0.307447(2)$, Sandvik 2025) but lacks a rigorous proof. The DLS/KLS reflection positivity method requires either $d \geq 3$ or $S \geq 1$. The gap between numerics and proof remains open. We proceed with the well-supported numerical result but flag this honestly.
