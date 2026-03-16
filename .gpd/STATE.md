# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-15)

**Core research question:** Can the experiential measure framework on structure space be formalized with rigorous proofs?
**Current focus:** Phase 3 complete -- Born-Fisher conjecture FALSIFIED

## Current Position

**Current Phase:** 3
**Current Phase Name:** Born-Fisher Test
**Total Phases:** 3
**Current Plan:** 2/2 (complete)
**Total Plans in Phase:** 2
**Status:** Phase 3 complete (verified)
**Last Activity:** 2026-03-16 -- Born-Fisher conjecture FALSIFIED: mu_Q identically zero across 1900+ trajectories

**Progress:** [██████████] 100%

## Active Calculations

None (Phase 3 execution complete, pending verification).

## Intermediate Results

- Theorem A error composition rate: gamma = alpha/2 (from eta = exp(-alpha/(2*eps)) choice)
- Theorem A prefactor: C = (rho_max/c)(K_b/K_s^2) = O(1) in epsilon; C = 0.25 for three-state chain (p=0.5)
- MC validation: all 9 (p,alpha) test cases pass (p in {0.3, 0.5, 0.7}, alpha in {0.3, 0.5, 1.0})
- Lipschitz bound: |rho-rho'| <= (delta/2)[2ln(|B|-1)+ln(|M|-1)+ln(n-1)] + 4*h_bin(delta/2)
- L(delta) = (C_I+C_H)/gap(P), improved from plan's (2C_I+C_H)/gap(P) via MVT
- Observer chain: gap=0.1, rho=0.346 nats, I/H=0.508
- Numerical validation: 3000 perturbations, zero violations, tightness 450-9500x
- Test A (static): alpha_half(p=0.5,d=2) = 0.890, spread over p = 0.069; Born-rule not special; FALSIFIES STATIC
- d=3 confirms: not a d=2 artifact (alpha_half spread = 0.023)
- Test B (dynamic): rho_Q(t) <= 0 throughout all 1900+ Lindblad trajectories; mu_Q = 0 identically
- Exchange Hamiltonian maintains perfect tracking (I=S_B late-time), system never enters I < S_B
- FINAL VERDICT: Born-Fisher-Experiential conjecture FALSIFIED

## Open Questions

- Whether non-Markovian or amplitude-damping channels could produce rho_Q > 0 regime
- Bound looseness (450-9500x): direct differentiation could yield tighter L

## Performance Metrics

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| 01-01 | 6min     | 2     | 1     |
| 01-02 | 11min    | 2     | 3     |
| 01-02-fix | 25min | 3     | 3     |
| 02-01 | 10min    | 2     | 1     |
| 02-02 | 10min    | 2     | 2     |
| 03-01 | 7min     | 2     | 7     |
| 03-02 | 8min     | 2     | 7     |

## Accumulated Context

### Decisions

- Used BEGK Thm 1.4 (exponential law) as primary concentration tool for Theorem A, avoiding full DV extension to rho-weighted functionals
- Corrected gamma from min(Delta_s-Delta_b, alpha) to alpha/2 after verification found overstatement
- Restructured mu_stable bound with case analysis using min(tau_exit, T_eps) after verification found original bound exceeded observation window
- Used MVT for Lipschitz Step 3 composition, yielding tighter L = (C_I+C_H)/gap instead of (2C_I+C_H)/gap
- Stated non-linear Lipschitz bound as primary result (linear L is delta-dependent due to h_bin logarithmic divergence)
- Test A verdict: FALSIFIES STATIC -- Born-rule distributions have no special property at half-saturation for diagonal states
- Test B verdict: FALSIFIED -- mu_Q identically zero, no dynamical selection mechanism
- Combined: Born-Fisher conjecture falsified in this toy model (valid decisive result per contract)

### Active Approximations

None yet.

**Convention Lock:**

- Metric signature: N/A (information-theoretic project)
- Fourier convention: N/A (information-theoretic project)
- Natural units: Not applicable (information-theoretic project)
- Gauge choice: N/A (information-theoretic project)
- Regularization scheme: N/A (information-theoretic project)
- Renormalization scheme: N/A (information-theoretic project)
- Coordinate system: N/A (information-theoretic project)
- Spin basis: N/A (information-theoretic project)
- State normalization: N/A (information-theoretic project)
- Coupling convention: N/A (information-theoretic project)
- Index positioning: N/A (information-theoretic project)
- Time ordering: N/A (information-theoretic project)
- Commutation convention: N/A (information-theoretic project)
- Levi-Civita sign: N/A (information-theoretic project)
- Generator normalization: N/A (information-theoretic project)
- Covariant derivative sign: N/A (information-theoretic project)
- Gamma matrix convention: N/A (information-theoretic project)
- Creation/annihilation order: N/A (information-theoretic project)

*Custom conventions:*
- Entropy Base: nats (natural logarithm)
- Custom Conventions.Entropy Base: nats (natural logarithm)
- Custom Conventions.Mutual Information: I(B;M) = H(B) + H(M) - H(B,M)
- Custom Conventions.Experiential Density: rho(p) = I(B;M) * (1 - I(B;M)/H(B))
- Custom Conventions.Generator Convention: probabilist: dp/dt = pQ (row-vector left, generator right)
- Custom Conventions.Matrix Norm: sup-norm on rows: ||P||_inf = max_i sum_j |P_ij|
- Custom Conventions.Von Neumann Entropy: S_vN(rho) = -Tr(rho ln rho) in nats

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

None

## Session Continuity

**Last session:** 2026-03-16
**Stopped at:** All 3 phases complete -- milestone ready for completion
**Resume file:** —
