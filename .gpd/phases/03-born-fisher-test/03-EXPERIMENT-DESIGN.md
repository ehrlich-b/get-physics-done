> **For gpd-executor:** This file contains parameter specifications, convergence criteria, and analysis plans. Use these when executing computational tasks in this phase.

# Experiment Design: Born-Fisher-Experiential Conjecture Test

## Objective

Numerically test whether Born-rule distributions are special for the quantum experiential density rho_Q = I_vN(B;M) * (1 - I_vN(B;M)/S_vN(B)). Specifically: (a) does the static ratio I_vN/S_vN equal 0.5 for any physically meaningful configuration, and (b) does the integrated trajectory functional mu_Q(theta) under Lindblad dynamics select Born-rule initial states?

A decisive verdict -- confirmation, falsification, or triviality -- is the deliverable. All three outcomes are valid per the scoping contract.

## Nature of the Computation

This is **not** a stochastic simulation. All computations are deterministic linear algebra on 4x4 (qubit-qubit) or 9x9 (qutrit-qutrit) density matrices. There are no Monte Carlo samples, no autocorrelation times, no statistical errors. The "numerical parameters" are eigenvalue cutoff thresholds and ODE integrator tolerances, not grid spacings or sample counts. Error is dominated by floating-point arithmetic and ODE adaptive step control, not statistics.

Consequently, the standard Monte Carlo experiment design machinery (sample size estimation, block averaging, decorrelation analysis) does not apply. Instead, the design focuses on:
- Parametric sweep coverage (which (theta, alpha, gamma) values to evaluate)
- Numerical precision verification (eigenvalue cutoff, ODE tolerance)
- Analytical cross-checks at known limits
- Dimension extension (d=2 to d=3) for robustness

## Target Quantities

| Quantity | Symbol | Dimensions | Expected Range | Required Accuracy | Validation |
|----------|--------|------------|----------------|-------------------|------------|
| Von Neumann entropy of body | S_vN(B) | nats | [0, ln(d)] | 1e-12 absolute | S_vN(I/d) = ln(d) |
| Von Neumann entropy of model | S_vN(M) | nats | [0, ln(d)] | 1e-12 absolute | S_vN(I/d) = ln(d) |
| Von Neumann entropy of joint | S_vN(BM) | nats | [0, 2*ln(d)] | 1e-12 absolute | S_vN = 0 for pure state |
| Quantum mutual information | I_vN(B;M) | nats | [0, 2*min(S_B, S_M)] | 1e-12 absolute | I_vN = 2*S_B for pure bipartite |
| MI-to-entropy ratio | I_vN/S_vN(B) | dimensionless | [0, 2] | 1e-10 absolute | = 2 for pure states; in [0,1] for decohered |
| Quantum experiential density | rho_Q | nats | [0, S_vN(B)/4] | 1e-10 absolute | = 0 at I=0 and I=S; peak S/4 at I=S/2 |
| Trajectory functional (Lindblad) | mu_Q(theta) | nat-seconds | [0, S_vN(B)*tau_D/2] | 1e-6 relative | Ansatz: mu_Q = S_vN(B)*tau_D/2 for exponential saturation |

**Derived quantities:**
- alpha_half(p): the tracking accuracy at which I_vN/S_vN = 0.5, as a function of body probability p. Solved by root-finding.
- mu_Q(theta): the integrated trajectory functional as a function of initial state parameter theta. This is the core observable for the conjecture test.
- rho_Q(t): the time-dependent experiential density during Lindblad evolution.

## Control Parameters

### Test A: Static Diagonal-State Test

| Parameter | Symbol | Range | Sampling | N_points | Rationale |
|-----------|--------|-------|----------|----------|-----------|
| Body probability | p | [0.01, 0.99] | Uniform | 200 | Full range of classical body states; avoid 0/0 at p=0,1 |
| Tracking accuracy | alpha | [0.51, 0.999] | Nonuniform: dense near 0.51 and 0.999 | 200 | alpha=0.5 gives I=0 (no tracking for qubit); alpha=1 gives I=S (perfect); interesting physics at intermediate values |
| Hilbert space dimension | d | {2, 3} | Discrete | 2 | d=2 primary; d=3 checks Gleason sensitivity |

**Physics of the alpha range:** For a qubit (d=2), when alpha = 0.5, the conditional model states rho_M^(0) = rho_M^(1) = I/2, so the model carries zero information (I_vN = 0). When alpha = 1, the model is a perfect copy (I_vN = S_vN(B)). The half-saturation point I = S/2 occurs at an intermediate alpha that depends on p. This alpha_half(p) curve is the central object of Test A.

**Born vs non-Born comparison:** For each theta in [0, pi/2], define:
- Born: p = cos^2(theta)
- Non-Born alternatives: p = cos^4(theta)/Z, p = |cos(theta)|/Z, p = uniform (p=0.5 for all theta)
The test evaluates whether alpha_half(p_Born) has any special property (e.g., constant in theta, or equal to a value with physical meaning) that alpha_half(p_nonBorn) does not.

### Test B: Lindblad Dynamics Test

| Parameter | Symbol | Range | Sampling | N_points | Rationale |
|-----------|--------|-------|----------|----------|-----------|
| Initial state angle | theta | [0.05, pi/2 - 0.05] | Uniform | 100 | Parametrizes |psi> = cos(theta)|00> + sin(theta)|11>; avoid degenerate endpoints |
| Decoherence rate | gamma_D | {0.1, 1.0, 10.0} | Logarithmic | 3 | Tests whether mu_Q(theta) shape depends on decoherence speed |
| Tracking coupling | g | {0.1, 0.5, 1.0, 2.0} | Logarithmic | 4 | Strength of B-M interaction Hamiltonian |
| Integration time | T_final | 10 / gamma_D | Adaptive | 1 per (gamma_D) | Ensure full decoherence: T_final >> tau_D = 1/gamma_D |
| Hilbert space dimension | d | {2, 3} | Discrete | 2 | d=2 primary; d=3 for robustness |

**Lindblad generator specification:**

Decoherence (dephasing in pointer basis):
```
L_deph = sqrt(gamma_D) * sigma_z (tensor) I_M
```
This produces exponential decay of off-diagonal elements of rho_B in the pointer basis, with decoherence time tau_D = 1/(2*gamma_D).

Tracking interaction (exchange Hamiltonian):
```
H_int = g * (sigma_x (tensor) sigma_x + sigma_y (tensor) sigma_y)
```
This is a partial swap that transfers state information from B to M. The full Lindblad generator is:
```
L[rho] = -i[H_int, rho] + gamma_D * (L_deph rho L_deph^dag - {L_deph^dag L_deph, rho}/2)
```

For qutrits (d=3), replace sigma operators with SU(3) generators (Gell-Mann matrices): dephasing via diag(1, -1, 0) and diag(1, 0, -1), and tracking via the off-diagonal generators.

## Numerical Parameters and Convergence

| Parameter | Symbol | Values | Expected Order | Convergence Criterion |
|-----------|--------|--------|----------------|----------------------|
| Eigenvalue cutoff | eps_eig | {1e-15, 1e-14, 1e-13, 1e-12} | N/A (threshold) | S_vN changes by < 1e-13 between successive cutoffs |
| ODE relative tolerance | rtol | {1e-12, 1e-10, 1e-8} | Adaptive RK order ~5 | mu_Q changes by < 1e-8 between 1e-12 and 1e-10 |
| ODE absolute tolerance | atol | rtol / 100 | Same as rtol | Coupled to rtol |
| ODE method | method | {'RK45', 'Radau'} | N/A | Agreement to 1e-8; Radau for stiff systems |
| Integration time T_final | T | {5/gamma_D, 10/gamma_D, 20/gamma_D} | Exponential convergence | mu_Q changes by < 1e-6 between 10/gamma and 20/gamma |

**Eigenvalue cutoff protocol:** Compute S_vN(rho) = -sum_{lambda_i > eps_eig} lambda_i * ln(lambda_i). Convention: 0*ln(0) = 0. For 4x4 matrices with eigenvalues from numpy.linalg.eigh, machine epsilon is ~2.2e-16. Setting eps_eig = 1e-15 captures all physically meaningful eigenvalues while avoiding -0.0 * ln(-0.0) = NaN from tiny negative numerical artifacts. Verify: results at eps_eig = 1e-15 and 1e-14 agree to < 1e-13 nats.

**ODE convergence protocol:** For Lindblad dynamics, vectorize the 4x4 density matrix as a 16-component real vector (or 32-component splitting real/imag for complex rho). Integrate with scipy.integrate.solve_ivp. Use rtol=1e-12, atol=1e-14 for production. Verify: mu_Q at rtol=1e-12 vs rtol=1e-10 agrees to < 1e-8.

**CPTP verification at each ODE step:** After each integration step, verify:
1. Tr(rho) = 1 to within 1e-10
2. rho is Hermitian: ||rho - rho^dag|| < 1e-10
3. All eigenvalues >= -1e-10 (clamp tiny negatives to 0)
If any check fails, reduce step size or switch to Radau (implicit, unconditionally stable).

## Grid Specification

### Test A: Full 2D Grid

```
p_grid = np.linspace(0.01, 0.99, 200)      # 200 body probability values
alpha_grid = np.concatenate([
    np.linspace(0.51, 0.60, 30),            # dense near no-tracking boundary
    np.linspace(0.60, 0.95, 100),           # uniform in bulk
    np.linspace(0.95, 0.999, 70),           # dense near perfect-tracking boundary
])                                           # 200 tracking accuracy values
```

Total grid points: 200 * 200 = 40,000 (p, alpha) pairs for d=2.
For d=3: 100 * 100 = 10,000 pairs (reduced for cost; bulk behavior established at d=2).

At each grid point, compute: S_vN(B), S_vN(M), S_vN(BM), I_vN(B;M), ratio = I_vN/S_vN, rho_Q.

**Derived sweep: alpha_half(p) curve**

For each p in p_grid, find alpha such that I_vN(B;M)/S_vN(B) = 0.5 using scipy.optimize.brentq on the interval [0.51, 0.999]. This produces the half-saturation curve. Then evaluate:
- alpha_half(cos^2(theta)) for theta in np.linspace(0.05, pi/2 - 0.05, 200): the Born-rule curve
- alpha_half(cos^4(theta)/Z) for same theta: a non-Born alternative
- Is alpha_half constant in theta for Born but not for non-Born? (Would support conjecture.)
- Is alpha_half constant for ALL p? (Would make the test trivial -- half-saturation is a property of alpha alone, independent of p.)

### Test B: Lindblad Trajectories

```
theta_grid = np.linspace(0.05, np.pi/2 - 0.05, 100)   # 100 initial states
gamma_D_grid = [0.1, 1.0, 10.0]                         # 3 decoherence rates
g_grid = [0.1, 0.5, 1.0, 2.0]                           # 4 coupling strengths
```

Total trajectories: 100 * 3 * 4 = 1,200 for d=2.
For d=3: 50 * 3 * 2 = 300 (reduced grid).

At each trajectory, store: rho_Q(t) sampled at 1000 time points, mu_Q = integral of rho_Q dt.

**Key derived quantity:** For each (gamma_D, g), plot mu_Q(theta). The conjecture predicts mu_Q has a maximum at a theta that corresponds to Born-rule optimality. If mu_Q(theta) is monotone, flat, or has a maximum at theta = pi/4 independent of (gamma_D, g), the conjecture is falsified or trivial respectively.

### Pre-Analytical Computation (Before Any Numerics)

The research document recommends solving I = S/2 analytically before doing numerics. For diagonal qubit states:

- S_vN(B) = h(p) = -p*ln(p) - (1-p)*ln(1-p)
- S_vN(M) = h(p*alpha + (1-p)*(1-alpha))
- S_vN(BM) = h_joint where the joint eigenvalues are {p*alpha, p*(1-alpha), (1-p)*(1-alpha), (1-p)*alpha}
- I_vN = S_B + S_M - S_BM = h(p) + h(p*alpha + (1-p)*(1-alpha)) - H_joint

Setting I_vN = h(p)/2 and solving for alpha as a function of p gives alpha_half(p). This is a transcendental equation -- solve numerically with root-finding, but verify the formula symbolically first.

**Critical check:** If alpha_half(p) is independent of p (constant), then the half-saturation condition is determined entirely by the tracking model, not the body distribution. In that case, the static test cannot distinguish Born from non-Born, and the conjecture's static version is trivially uninformative. This must be checked FIRST, before running the full grid.

## Validation Points

| Configuration | Observable | Known Value | Source | Tolerance |
|---------------|-----------|-------------|--------|-----------|
| Pure Bell state (p=0.5, no decoherence) | I_vN/S_vN(B) | 2.0 | Standard QIT | 1e-12 |
| Pure Bell state | rho_Q | -2*ln(2) = -1.386 nats (negative, unphysical) | I=2S formula | 1e-12 |
| Product state (alpha=0.5, d=2) | I_vN(B;M) | 0.0 | No correlation | 1e-12 |
| Perfect tracking (alpha=1) | I_vN/S_vN(B) | 1.0 | I=S | 1e-12 |
| Maximally mixed body (p=0.5) | S_vN(B) | ln(2) = 0.6931... nats | Standard | 1e-12 |
| Maximally mixed qutrit body (p=1/3,1/3,1/3) | S_vN(B) | ln(3) = 1.0986... nats | Standard | 1e-12 |
| Classical limit: diagonal state, alpha=0.5, p=0.5 | Ratio I/H, rho | Match composite_self_model.py values | Decoherence limit | 1e-6 |
| Lindblad late-time state (t >> tau_D) | Off-diagonal elements of rho | < 1e-6 | Decoherence | 1e-6 |
| Lindblad late-time | I_vN/S_vN matches static diagonal test | Agreement | Consistency | 1e-4 |

**Classical baseline cross-check:** The classical composite_self_model.py uses |B|=|M|=4 with alpha=0.5 and gets rho=0.347, I*/H=0.507. The quantum diagonal-state test with d=2 is a smaller system (|B|=|M|=2) so the numbers will differ, but the pattern should match: rho peaks at intermediate alpha (near 0.5 for d=2), and I/H at the peak is near 0.5. For d=4, the quantum test should reproduce the classical result exactly.

## Analysis Plan

### Test A Analysis Pipeline

1. **2D heatmap:** Plot ratio = I_vN(B;M)/S_vN(B) as a function of (p, alpha). Identify the I=S/2 contour.
2. **alpha_half(p) curve:** Extract the half-saturation locus. Determine if it is constant, monotone, or non-trivial.
3. **Born-rule overlay:** On the alpha_half(p) plot, overlay the Born-rule curve p = cos^2(theta) and non-Born alternatives. Check if Born-rule p values trace a special path through the half-saturation locus.
4. **rho_Q heatmap:** Plot rho_Q(p, alpha). Confirm parabolic structure. Identify the maximum.
5. **Dimension comparison:** Overlay d=2 and d=3 results. If qualitatively different, the d=2 result is artifact.

**Verdict criteria for Test A:**
- If alpha_half(p) = constant (independent of p): Test A is **trivially uninformative**. The half-saturation condition depends only on the tracking model, not the Born rule. Proceed to Test B as primary.
- If alpha_half(p) varies with p AND Born-rule p values satisfy a special condition (e.g., alpha_half(cos^2(theta)) = constant for all theta while alpha_half(f(theta)) varies): **Supports conjecture.**
- If alpha_half(p) varies with p but Born-rule p values show no special property: **Falsifies the static half-saturation conjecture.**

### Test B Analysis Pipeline

1. **mu_Q(theta) curves:** For each (gamma_D, g), plot mu_Q vs theta. Core observable.
2. **Maximum location:** Find theta_max = argmax mu_Q(theta) for each (gamma_D, g).
3. **Born-rule test:** Does theta_max depend on (gamma_D, g)? If theta_max = pi/4 always, it just selects equal superposition (trivial). If theta_max depends on H_int in a Born-consistent way, that supports the conjecture.
4. **rho_Q(t) pulse shape:** For representative (theta, gamma_D, g), plot rho_Q(t). Verify pulse structure from Sec 3.3 of quantum-extension/draft.md.
5. **Pulse peak timing:** Verify peak at t ~ tau_D * ln(2).
6. **Pulse integral:** Compare mu_Q with the analytical ansatz mu_Q = S_vN(B) * tau_D / 2.
7. **Dimension comparison:** Repeat key trajectories at d=3.

**Verdict criteria for Test B:**
- mu_Q(theta) is flat or monotone: **Falsifies the conjecture.** Born rule is not special.
- mu_Q(theta) peaks at theta = pi/4 for all (gamma_D, g): **Trivial.** Equal superposition maximizes S_vN(B), which trivially maximizes mu_Q since rho_Q scales with S_vN(B).
- mu_Q(theta) peaks at a theta_max that depends on (gamma_D, g) in a physically meaningful way AND theta_max coincides with a Born-rule-consistent selection: **Supports conjecture.** This is the strongest positive outcome.
- mu_Q(theta) peaks at theta = pi/4 for symmetric setups but at different theta for asymmetric ones (different decoherence rates for |0> vs |1>): **Interesting.** Would need to check if theta_max = arccos(sqrt(p_Born)) where p_Born is the Born weight for an asymmetric pointer basis.

### Asymmetric Extension (Test B+)

If Test B with symmetric dephasing is trivial (theta_max = pi/4 always), extend to asymmetric decoherence:
```
L_0 = sqrt(gamma_0) * |0><0|  (tensor)  I_M
L_1 = sqrt(gamma_1) * |1><1|  (tensor)  I_M
```
with gamma_0 != gamma_1. This breaks the symmetry: the pointer basis is still {|0>, |1>} but the decoherence rates differ. Now the "natural" Born-rule weight is p_0 = |alpha_0|^2, p_1 = |alpha_1|^2, and if gamma_0 != gamma_1, the optimal theta_max should shift away from pi/4.

Asymmetric parameter grid:
```
gamma_ratio = gamma_0 / gamma_1 in {0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0}  # 7 values
theta_grid: same 100 points
g: fixed at 1.0 (best coupling from symmetric test)
```
Total: 700 trajectories.

## Expected Scaling and Cost Estimate

### Per-Point Cost

| Operation | Matrix Size | FLOPS | Wall Time (est.) |
|-----------|------------|-------|-----------------|
| Eigendecomposition (d=2) | 4x4 | O(64) | < 1 microsecond |
| S_vN from eigenvalues | 4 values | O(4) | negligible |
| Partial trace | 4x4 -> 2x2 | O(16) | negligible |
| Full Test A point (d=2) | 3 eigendecompositions + entropy | -- | ~10 microseconds |
| Full Test A point (d=3) | 3 eigendecompositions of 9x9 | -- | ~50 microseconds |
| Lindblad ODE integration (d=2) | 16-component vector, 1000 steps | O(16000) | ~1 millisecond |
| Lindblad ODE integration (d=3) | 81-component vector, 1000 steps | O(81000) | ~10 milliseconds |

### Total Cost Table

| Run Type | N_points | Dimension | Est. Time/Point | Total Time |
|----------|----------|-----------|-----------------|------------|
| Pre-analytical check: alpha_half(p) constant? | 200 p values | d=2 | 0.1 ms | 0.02 sec |
| Test A: full (p, alpha) grid | 40,000 | d=2 | 0.01 ms | 0.4 sec |
| Test A: alpha_half(p) root-finding | 200 | d=2 | 1 ms | 0.2 sec |
| Test A: d=3 grid | 10,000 | d=3 | 0.05 ms | 0.5 sec |
| Convergence: eigenvalue cutoff | 4 cutoffs * 100 points | d=2 | 0.01 ms | 0.004 sec |
| Test B: Lindblad trajectories | 1,200 | d=2 | 1 ms | 1.2 sec |
| Test B: d=3 trajectories | 300 | d=3 | 10 ms | 3.0 sec |
| Convergence: ODE tolerance | 3 rtols * 30 trajectories | d=2 | 1 ms | 0.09 sec |
| Test B+: asymmetric extension | 700 | d=2 | 1 ms | 0.7 sec |
| Validation points | 9 | d=2 | 0.01 ms | negligible |
| Plotting and post-processing | -- | -- | -- | ~2 sec |
| **Total** | **~53,000** | | | **< 10 sec CPU** |

Budget: 60 seconds. Estimated cost: < 10 seconds. Margin: > 80%. This is an extremely cheap experiment; all budget concerns are about code implementation time, not compute.

## Pre-Production Sanity Checks (< 1% of budget)

Run these before any parametric sweep:

1. **Trace and positivity:** Construct rho_BM for (p=0.5, alpha=0.75, d=2). Verify Tr(rho) = 1 +/- 1e-14, all eigenvalues >= -1e-15.
2. **Pure-state identity:** Construct |psi> = (|00> + |11>)/sqrt(2). Compute I_vN. Verify I_vN = 2*S_vN(B) = 2*ln(2) to 1e-12.
3. **Product-state zero:** Construct rho_B (tensor) rho_M with different marginals. Verify I_vN = 0 to 1e-12.
4. **Known entropy:** Verify S_vN(I/2) = ln(2) and S_vN(I/3) = ln(3) to 1e-12.
5. **Lindblad trace preservation:** Run one Lindblad trajectory for 100 steps. Verify Tr(rho(t)) = 1 +/- 1e-10 at every step.
6. **Lindblad decoherence:** Run Lindblad with gamma_D=1.0, g=0, theta=pi/4 for T=20. Verify off-diagonal elements of rho_B < 1e-8 at T=20.
7. **Araki-Lieb bound:** At every computed point, verify 0 <= I_vN <= 2*min(S_B, S_M).
8. **Symmetry:** For p=0.5 (symmetric), verify I_vN is symmetric under p -> 1-p (i.e., the ratio is the same at p and 1-p).

If any check fails: **stop**. Debug before proceeding.

## Systematic vs Statistical Error Budget

| Error Type | Source | Magnitude | How to Control |
|-----------|--------|-----------|----------------|
| Floating-point | IEEE 754 double precision | ~1e-15 per operation | Accumulates to ~1e-12 for eigenvalue problems; acceptable |
| Eigenvalue cutoff | Threshold for 0*ln(0) | < 3e-14 nats per entropy | Verify invariance across cutoff values |
| ODE integration | Adaptive step control | < 1e-8 for rtol=1e-12 | Richardson: compare rtol=1e-12 vs 1e-10 |
| Lindblad non-CPTP drift | Accumulated numerical error | < 1e-10 per trajectory | Monitor trace and positivity; reproject if needed |
| Finite integration time | T_final < infinity | exp(-gamma_D * T_final) | Use T = 10/gamma_D: error < e^{-10} ~ 5e-5 |

**Dominant error for Test A:** Floating-point arithmetic in eigendecomposition. Magnitude ~1e-13 nats. Negligible compared to the question being asked (is the ratio 0.5 or not?).

**Dominant error for Test B:** ODE integration and finite-time truncation. Combined magnitude ~1e-5 in mu_Q. The question is whether mu_Q(theta) has a maximum, and where -- this requires resolving differences of O(0.01) or larger in mu_Q, so 1e-5 precision is sufficient.

## Execution Order

```
0. Pre-analytical: solve I=S/2 for alpha(p) symbolically/root-finding  [0.1 sec]
   -> Determine if alpha_half depends on p. If not, Test A is trivially uninformative.

1. Sanity checks: 8 validation points                                  [< 0.1 sec]
   -> Must all pass. Stop if any fail.

2. Convergence: eigenvalue cutoff sweep                                [< 0.01 sec]
   -> Verify eps_eig = 1e-15 is stable.

3. Test A: full (p, alpha) grid for d=2                                [0.4 sec]
   -> Produce heatmaps, alpha_half(p) curve, Born vs non-Born comparison.

4. Test A: d=3 grid                                                    [0.5 sec]
   -> Check d=2 results are not artifacts.

5. Test B pilot: 5 trajectories at representative (theta, gamma, g)    [0.005 sec]
   -> Verify Lindblad code produces sensible rho_Q(t) pulse.

6. Convergence: ODE tolerance sweep                                    [0.1 sec]
   -> Verify rtol=1e-12 is converged.

7. Test B: full trajectory grid for d=2                                [1.2 sec]
   -> Produce mu_Q(theta) curves for all (gamma_D, g).

8. Test B: d=3 trajectories                                            [3.0 sec]
   -> Check dimension dependence.

9. Test B+: asymmetric extension (if Test B symmetric is trivial)      [0.7 sec]
   -> Only run if theta_max = pi/4 for all symmetric (gamma, g).

10. Analysis and plotting                                              [2 sec]
    -> All plots and verdict determination.
```

**Dependencies:**
- Step 0 informs whether to invest analysis effort in Test A or skip to Test B
- Steps 1-2 must pass before steps 3-4
- Steps 5-6 must pass before steps 7-8
- Step 9 is conditional on Step 7 results
- Step 10 requires all preceding data

## Decision Tree for Verdict

```
Step 0: Is alpha_half(p) constant in p?
  YES -> Test A is uninformative (ratio at half-saturation determined by
         tracking model alone, not body distribution). Skip to Test B.
  NO  -> Proceed with Test A Born vs non-Born comparison.
         Is alpha_half(cos^2(theta)) special?
           YES -> Test A supports conjecture. Proceed to Test B for dynamics.
           NO  -> Test A falsifies static half-saturation conjecture.
                  Proceed to Test B (dynamics may still be interesting).

Step 7: Does mu_Q(theta) have an interior maximum?
  NO (flat or monotone) -> CONJECTURE FALSIFIED. Born rule is not special
                           for rho_Q. Report as decisive negative result.
  YES, at theta = pi/4 always -> TRIVIALLY SATISFIED. Equal superposition
                                  maximizes S_vN(B) which dominates mu_Q.
                                  Proceed to Test B+ (asymmetric).
  YES, at theta != pi/4 depending on dynamics -> INTERESTING. Check Born
                                                  consistency.

Step 9 (if needed): Does theta_max shift with gamma_ratio?
  NO -> Maximum is robust but always at theta=pi/4. Conjecture is about
        symmetry of S_vN, not Born rule. TRIVIALLY SATISFIED.
  YES -> Does theta_max = arccos(sqrt(p_Born)) where p_Born depends on
         asymmetry in a Born-consistent way?
           YES -> CONJECTURE SUPPORTED.
           NO  -> CONJECTURE FALSIFIED (maximum exists but is not Born-rule).
```

## Expected Outcomes

Based on the analytical structure (Research document, Sec 3.2 self-critique):

**Most likely outcome for Test A:** alpha_half(p) depends on p but in a way that is symmetric under p -> 1-p. Born-rule p = cos^2(theta) values trace a non-special curve through the locus. The static test is **uninformative** about Born vs non-Born because the diagonal-state setup reduces to classical Shannon entropy, which has no knowledge of the underlying quantum state theta.

**Most likely outcome for Test B (symmetric):** mu_Q(theta) peaks at theta = pi/4 because S_vN(B) = h(cos^2(theta)) peaks at theta = pi/4 and rho_Q scales with S_vN(B). This would be **trivially satisfied** -- the maximum is about maximum entropy, not Born rule.

**Most interesting outcome for Test B+ (asymmetric):** If the asymmetric decoherence breaks the theta=pi/4 symmetry and the resulting theta_max tracks the Born-rule prediction, the conjecture has non-trivial content.

**Falsification scenario:** mu_Q(theta) is monotonically increasing in theta (more entanglement always gives more mu_Q) or is flat. This would kill the conjecture decisively.

## Suggested Task Breakdown (for planner)

| Task | Type | Dependencies | Est. Complexity |
|------|------|-------------|-----------------|
| Implement density matrix utilities (partial trace, S_vN, I_vN) | code | none | small |
| Implement diagonal-state constructor and Test A sweep | code | utilities | small |
| Pre-analytical alpha_half(p) computation + constancy check | analysis | Test A code | small |
| Run Test A full grid + d=3 + Born/non-Born comparison | sim | pre-analytical | small |
| Implement Lindblad generator and ODE integrator | code | utilities | medium |
| Run sanity checks + convergence studies | validate | all code | small |
| Run Test B full trajectory grid + d=3 | sim | Lindblad code, convergence | small |
| Run Test B+ asymmetric extension (conditional) | sim | Test B results | small |
| Analysis: plots, verdict determination, comparison to classical baseline | analysis | all sims | medium |
