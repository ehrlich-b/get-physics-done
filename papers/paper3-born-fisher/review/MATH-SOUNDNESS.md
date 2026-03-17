# Mathematical Soundness Review -- Pass 2

**Manuscript:** `papers/paper3-born-fisher/main.tex`
**Title:** Falsification of the Born--Fisher--Experiential Conjecture in a Qubit Toy Model
**Reviewer role:** Mathematical soundness (equations, derivations, statistics, code logic)
**Date:** 2026-03-16
**Manuscript SHA256:** `e8b6fc30f0ca73022373abfb7cf730ee85ab94e456ecc9b3de823c5642dd34a4`

---

## 1. Equations Checked

Five key equations/derivation steps were selected for detailed verification, covering the central definitions, the pure-state limit, the superoperator construction, and the falsification mechanism.

### 1.1 Quantum experiential density (Eq. 3, Definition 1)

**Equation:**
`rho_Q = I_vN(B;M) * (1 - I_vN(B;M) / S_vN(B))`

where `I_vN(B;M) = S_vN(B) + S_vN(M) - S_vN(BM)`.

**Check:** This is the direct quantum analogue of the classical Eq. (1), `rho = I(B;M)*(1 - I/H(B))`, with Shannon entropies replaced by von Neumann entropies. The substitution is consistent with the stated conventions (nats, natural log). The code in `quantum_info.py` lines 95-127 implements this exactly:
- `i_vn = s_b + s_m - s_bm`
- `ratio = i_vn / s_b`
- `rho_q = i_vn * (1.0 - ratio)`

This algebraically equals `I * (1 - I/S_B)`. When `S_B < 1e-15`, it returns 0, avoiding division by zero. **SOUND.**

**Note on domain:** Unlike the classical case where `0 <= I <= H(B)` always (so `rho >= 0`), the quantum mutual information satisfies `0 <= I_vN <= 2*min(S_B, S_M)` (Araki-Lieb). For `I_vN > S_B`, the factor `(1 - I/S_B) < 0`, making `rho_Q < 0`. The paper correctly identifies this at Eq. (4) and throughout. **SOUND.**

### 1.2 Pure-state limit (Eq. 4)

**Equation:**
For pure `|psi>_{BM}`: `S_BM = 0`, `S_B = S_M` (Schmidt decomposition), so `I_vN = 2*S_B`, hence `rho_Q = 2*S_B*(1 - 2) = -2*S_B < 0`.

**Check:** For a pure bipartite state, `S(BM) = 0` is immediate from the definition. The Schmidt decomposition gives `rho_B` and `rho_M` with identical spectra, hence `S_B = S_M`. Then `I = S_B + S_M - 0 = 2*S_B`. Substituting: `rho_Q = 2*S_B*(1 - 2*S_B/S_B) = 2*S_B*(-1) = -2*S_B`. For any entangled pure state, `S_B > 0`, so `rho_Q < 0`. **SOUND.**

**For theta=pi/4 (Bell state):** `S_B = ln(2)`, so `I_vN = 2*ln(2) = 1.386...` and `rho_Q = -2*ln(2) = -1.386...`. The paper states `rho_Q = -0.693 nats` on line 402. Let me check: `rho_Q = 2*S_B*(1-2) = -2*ln(2) = -1.386`. But the paper says `-0.693 nats`. **ERROR FOUND.** The paper states `rho_Q = -0.693 nats` for the pilot trajectory at `theta = pi/4`. The correct value from the formula is `-2*S_B = -2*ln(2) = -1.386 nats`. The value `-0.693` is `-ln(2) = -S_B`, not `-2*S_B`.

Wait -- let me re-read more carefully. Line 401-402: "At t = 0, the state is pure with I_vN = 2*ln(2) = 1.386 nats and S_vN(B) = ln(2) = 0.693 nats, giving r = 2 and rho_Q = -0.693 nats."

**Recalculation:** `rho_Q = I*(1 - I/S_B) = 1.386*(1 - 1.386/0.693) = 1.386*(1 - 2) = 1.386*(-1) = -1.386 nats.`

The paper claims `rho_Q = -0.693 nats` but the correct value is `-1.386 nats`. This is a factor-of-two error in the reported numerical value. The formula `rho_Q = -2*S_B` from Eq. (4) gives `-2*0.693 = -1.386`, not `-0.693`. **MINOR ERROR in the narrative text.** The subsequent analysis is unaffected because the sign (negative) is what matters for the falsification, and the code correctly computes `rho_Q` from the formula (not from a hard-coded value).

**Status: MINOR ERROR (factor of 2 in a quoted numerical value, line 402). Does not affect any conclusion.**

### 1.3 Superoperator construction (Eqs. 13-14)

**Equation (vectorization):** `d/dt vec(rho) = L * vec(rho)` where

`L = -i(I x H - H^T x I) + sum_k (L_k^* x L_k - (1/2) I x L_k^dag L_k - (1/2) (L_k^dag L_k)^T x I)`

using column-stacking vectorization `vec(rho) = rho.flatten('F')`.

**Check against standard:** The column-stacking (Fortran-order) identity is `vec(A rho B) = (B^T kron A) vec(rho)`. Therefore:
- `vec(-i*H*rho) = -i*(I kron H) vec(rho)` (set A=H, B=I, so B^T=I)
- `vec(+i*rho*H) = +i*(H^T kron I) vec(rho)` (set A=I, B=H, so B^T=H^T)
- Combined Hamiltonian part: `-i*(I kron H - H^T kron I)`. This matches the paper Eq. (14) and the code `lindblad.py` line 69.

For the dissipator `L_k rho L_k^dag`:
- `vec(L_k rho L_k^dag) = (L_k^dag)^T kron L_k = L_k^* kron L_k`. Code line 77: `np.kron(L_k.conj(), L_k)`. **CORRECT.**

For `-(1/2) L_k^dag L_k rho`:
- `vec(L_k^dag L_k rho) = (I kron L_k^dag L_k) vec(rho)`. Code line 80: `-0.5 * np.kron(I, L_dag_L)`. **CORRECT.**

For `-(1/2) rho L_k^dag L_k`:
- `vec(rho L_k^dag L_k) = ((L_k^dag L_k)^T kron I) vec(rho)`. Code line 83: `-0.5 * np.kron(L_dag_L.T, I)`. **CORRECT.**

The verification artifact (03-VERIFICATION.md, Oracle 2) confirms the superoperator matches explicit Lindblad computation to machine precision. **SOUND.**

### 1.4 Dephasing rate and off-diagonal decay

**Claim:** For `L = sqrt(gamma_D) * (sigma_z kron I)`, the off-diagonal element `rho_BM[0,3]` decays as `exp(-2*gamma_D*t)`.

**Check:** `L^dag L = gamma_D * (sigma_z^2 kron I) = gamma_D * I_4` (since `sigma_z^2 = I`).

The dissipator on element `(0,3)` (connecting `|00>` and `|11>`):
- `L|00> = sqrt(gamma_D) * (+1) * |00>` (sigma_z|0> = |0>)
- `L|11> = sqrt(gamma_D) * (-1) * |11>` (sigma_z|1> = -|1>)
- `(L rho L^dag)[0,3] = sqrt(gamma_D)*(+1) * rho[0,3] * sqrt(gamma_D)*(-1) = -gamma_D * rho[0,3]`
- `-(1/2)*(L^dag L rho + rho L^dag L)[0,3] = -(1/2)*(gamma_D * rho[0,3] + rho[0,3] * gamma_D) = -gamma_D * rho[0,3]`
- Total dissipator: `-gamma_D * rho[0,3] - gamma_D * rho[0,3] = -2*gamma_D * rho[0,3]`

So `d rho[0,3]/dt` (dissipator part) `= -2*gamma_D * rho[0,3]`, giving decay `exp(-2*gamma_D*t)`.

The paper states `tau_D = 1/(2*gamma_D)` (line 271). This is the decoherence time constant, meaning the off-diagonal decays as `exp(-t/tau_D) = exp(-2*gamma_D*t)`. **SOUND.**

The verification artifact confirms numerical agreement to relative error `5e-11` at multiple time points.

### 1.5 Exchange Hamiltonian and the r >= 1 mechanism

**Claim:** The exchange Hamiltonian `H = g*(sigma_x kron sigma_x + sigma_y kron sigma_y)` ensures `I_vN/S_B >= 1` throughout the Lindblad evolution.

**Check of H structure:**
- `sigma_x kron sigma_x + sigma_y kron sigma_y` in the computational basis `{|00>, |01>, |10>, |11>}` gives:
  - `sigma_x kron sigma_x = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]`
  - `sigma_y kron sigma_y = [[0,0,0,-1],[0,0,1,0],[0,1,0,0],[-1,0,0,0]]`
  - Sum = `[[0,0,0,0],[0,0,2,0],[0,2,0,0],[0,0,0,0]]`

This is `2g * (|01><10| + |10><01|)`, the partial swap operator on the `{|01>, |10>}` subspace. It does not mix `|00>` or `|11>`. This means:
- Starting from `cos(theta)|00> + sin(theta)|11>`, the Hamiltonian alone preserves the populations in `|00>` and `|11>` (since `H|00> = 0` and `H|11> = 0`).
- Dephasing destroys the `|00><11|` coherence, making the state diagonal: `cos^2(theta)|00><00| + sin^2(theta)|11><11|`.
- This diagonal state has `rho_B = diag(cos^2(theta), sin^2(theta))` and `rho_M = diag(cos^2(theta), sin^2(theta))`, with `S_BM = S_B` (same spectrum as `rho_B`), giving `I = S_B + S_M - S_BM = S_B + S_B - S_B = S_B`, hence `r = 1`.

**Monotonic decrease from r=2 to r=1:** At `t=0`, the pure state has `r=2`. As dephasing acts, `S_BM` increases from 0 (it was 0 for a pure state) toward `S_B` (the late-time diagonal state). Meanwhile `S_B` and `S_M` are preserved because (a) the Bell state has a maximally mixed marginal, and local dephasing does not change it, and (b) more generally, `sigma_z kron I` commutes with the body's marginal. So `I = 2*S_B - S_BM` decreases monotonically as `S_BM` increases from 0 to `S_B`. The ratio `r = I/S_B = 2 - S_BM/S_B` decreases from 2 to 1. **It never drops below 1** because `S_BM` never exceeds `S_B` in this model: the late-time state has `S_BM = S_B` (diagonal with same spectrum as marginals), and the approach is monotone.

This reasoning holds for the maximally entangled case. For general `theta`, the argument is slightly more involved because `S_B` may change during the evolution. However, the exchange Hamiltonian preserves the populations of `|00>` and `|11>` (its kernel), and dephasing only affects off-diagonals, so the diagonal populations are time-invariant. The body marginal is `rho_B = diag(cos^2 theta, sin^2 theta)` at all times, hence `S_B` is constant. The model marginal similarly remains `rho_M = diag(cos^2 theta, sin^2 theta)` at all times (by the same argument -- trace over B of the joint state preserves populations). The joint entropy `S_BM` increases monotonically from 0 to `h(cos^2 theta)`, giving `r = 2 - S_BM/S_B` decreasing from 2 to 1. **SOUND.**

**For asymmetric dephasing** with `L_0 = sqrt(gamma_0)*|0><0| kron I` and `L_1 = sqrt(gamma_1)*|1><1| kron I`:
- `L_0^dag L_0 = gamma_0 * |0><0| kron I`
- `L_1^dag L_1 = gamma_1 * |1><1| kron I`
- These projective collapse operators still only destroy off-diagonal coherences (in the pointer basis). The populations `|00><00|` and `|11><11|` are unchanged.
- The exchange Hamiltonian still has `H|00> = H|11> = 0`.
- Therefore the same argument applies: the ratio `r` monotonically decreases from 2 to 1. **SOUND.**

## 2. Derivation Integrity

### 2.1 Conjecture statement (Conjecture 1)

The conjecture states that `mu_Q(theta) = integral_0^T max(rho_Q(t), 0) dt` is extremized at the Born-rule initial state. This is well-defined. The `max(rho_Q, 0)` clamp ensures `mu_Q >= 0`. If `rho_Q <= 0` everywhere, then `mu_Q = 0` identically -- a degenerate case the paper correctly handles.

The "equivalently, I_vN = S_B/2 plays a distinguished role" is a heuristic restatement: if `rho_Q` is maximized at `r=1/2`, then the trajectory spending the most time near `r=1/2` would maximize `mu_Q`. The paper does not rely on this equivalence for its falsification; it works directly with `mu_Q = 0`. **SOUND.**

### 2.2 Diagonal BM state parametrization (Eqs. 6-7)

The state `rho_BM = p*|0><0| kron rho_M^(0) + (1-p)*|1><1| kron rho_M^(1)` with `rho_M^(0) = diag(alpha, 1-alpha)` and `rho_M^(1) = diag(1-alpha, alpha)` is diagonal in the computational basis. The code (`quantum_info.py` lines 160-181) constructs diagonal entries `[p*alpha, p*(1-alpha), (1-p)*(1-alpha), (1-p)*alpha]` for `d=2`, which matches the formula. Trace = `p*alpha + p*(1-alpha) + (1-p)*(1-alpha) + (1-p)*alpha = p + (1-p) = 1`. **SOUND.**

The boundary cases:
- `alpha=1`: `rho_BM = diag(p, 0, 0, 1-p)`, a perfectly correlated state. `S_BM = h(p) = S_B`. `I = S_B`. `r = 1`. **CORRECT.**
- `alpha=0.5`: `rho_BM = diag(p/2, p/2, (1-p)/2, (1-p)/2) = rho_B kron (I/2)`. Product state. `I = 0`. **CORRECT.**

### 2.3 RK4 integrator

The code in `lindblad.py` lines 92-113 implements standard RK4:
```
k1 = L @ rho_vec
k2 = L @ (rho_vec + dt/2 * k1)
k3 = L @ (rho_vec + dt/2 * k2)
k4 = L @ (rho_vec + dt * k3)
rho_new = rho_vec + dt/6 * (k1 + 2*k2 + 2*k3 + k4)
```

This is the standard Butcher tableau for RK4. The verification artifact confirms fourth-order convergence (error ratio 16x between successive step-size halvings). **SOUND.**

## 3. Statistical Analysis Verification

This paper is not a statistical study. It is a deterministic numerical computation on density matrices. No Monte Carlo sampling, no stochastic errors, no p-values, no chi-squared tests. The claims are:
- `rho_Q <= 0` at all time points across all 1900+ trajectories
- `mu_Q = 0` to `10^{-15} nat-time`

These are exact (to floating-point precision) outcomes of a deterministic ODE integration, not statistical estimates. The verification artifact confirms trace preservation to `10^{-16}`, positivity to `10^{-31}`, and RK4 convergence to `10^{-15}`. The tolerance margins are many orders of magnitude better than needed.

The paper does not make statistical claims, so there are no p-values or hypothesis tests to check. The falsification is structural (the ratio stays in [1,2] by the dynamics), not statistical. **APPROPRIATE; no statistical issues.**

## 4. Code Logic Verification

### 4.1 `quantum_info.py`

- **`von_neumann_entropy`**: Uses `eigh` for Hermitian matrices (correct for density matrices), filters eigenvalues below `1e-15` (appropriate for double precision), computes `-sum(lambda * ln(lambda))`. **SOUND.**
- **`partial_trace`**: Reshapes `(d_b*d_m, d_b*d_m)` to `(d_b, d_m, d_b, d_m)` and traces over axes (1,3) for `trace_over='M'` or (0,2) for `trace_over='B'`. This is the correct index structure for `|i_B j_M><k_B l_M|`. **SOUND.**
- **`quantum_mutual_information`**: `I = S_B + S_M - S_BM`. **SOUND.**
- **`experiential_density`**: Returns `(rho_Q, I, S_B, ratio)` with `rho_Q = I*(1-I/S_B)`. Handles `S_B = 0` edge case. **SOUND.**
- **`diagonal_bm_state`**: Constructs the diagonal state as described. For `d=3`, uses `body_probs = [p, (1-p)/2, (1-p)/2]` and model `rho_M^(k)` with `alpha` on diagonal `k`, `(1-alpha)/(d-1)` elsewhere. **SOUND.**

### 4.2 `lindblad.py`

- **`build_lindblad_superoperator`**: Implements Eq. (14) correctly as verified in Section 1.3 above.
- **`rk4_step`**: Standard RK4 as verified in Section 2.3 above.
- **`integrate_lindblad`**: Vectorizes with Fortran order, integrates, reconstructs density matrix, enforces Hermiticity via `(rho + rho^dag)/2`, computes all observables at each stored step. The `np.real()` call on line 182 before passing to `experiential_density` is safe because the density matrix should be real after Hermitization (up to floating-point imaginary parts). **SOUND.**
- **`build_qubit_system`**: `H = g*(sigma_x kron sigma_x + sigma_y kron sigma_y)`, `L = sqrt(gamma_D)*(sigma_z kron I)`. Matches Eqs. (8)-(9). **SOUND.**
- **`build_asymmetric_system`**: `L_0 = sqrt(gamma_0)*(|0><0| kron I)`, `L_1 = sqrt(gamma_1)*(|1><1| kron I)`. Matches Eq. (10). **SOUND.**
- **`initial_entangled_state`**: For `d=2`, constructs `psi = [cos(theta), 0, 0, sin(theta)]` and `rho = |psi><psi|`. The ordering is `|00>, |01>, |10>, |11>` (standard computational basis with first qubit as "most significant"). `|00>` is index 0, `|11>` is index 3. **SOUND.**

### 4.3 `test_a_static.py`

- Grid construction, ratio computation, bisection root-finding, Born/non-Born comparison all follow the experiment design. The code correctly uses `quantum_info` functions and does not introduce independent formulas. **SOUND.**

### 4.4 `test_b_dynamics.py`

- Uses `np.trapezoid` (NumPy >= 2.0 name for `np.trapz`) for integrating `max(rho_Q, 0)` over the time grid. This is trapezoidal rule, appropriate for the stored time grid. **SOUND.**
- Decision tree logic (lines 275-371) correctly checks: first whether `rho_Q` is ever positive, then whether `mu_Q` is flat, then whether the peak is at `pi/4`. The falsification branch (`rho_Q` never positive anywhere) is the one taken, leading to FALSIFIED. **SOUND.**

## 5. Falsification Logic Assessment

The paper's central claim is: "The conjecture is falsified for this model class."

The logical structure is:
1. The conjecture predicts that `mu_Q(theta)` is extremized at the Born-rule initial state.
2. If `mu_Q(theta) = 0` identically for all `theta`, there is no extremum (or equivalently, every point is trivially an extremum), and the conjecture has no non-trivial content.
3. The paper shows `mu_Q = 0` identically because `rho_Q <= 0` throughout the entire Lindblad evolution for every tested trajectory.
4. The reason `rho_Q <= 0` is that `I_vN/S_B >= 1` throughout, which follows from the exchange Hamiltonian's tracking behavior.

**Assessment:**

- Step 3 is supported by 1900+ numerical trajectories across a wide parameter range (symmetric dephasing, asymmetric dephasing, varying coupling strengths, d=2 and d=3), plus the analytical argument in Section 1.5 above.
- The falsification is valid *for this model class* (exchange Hamiltonian + dephasing, Markovian Lindblad). The paper correctly scopes this: "The conjecture is cleanly falsified for this class of Lindblad models."
- The paper correctly notes that non-Markovian channels or amplitude damping might produce different behavior.

**Logical soundness of the falsification:** If the conjecture claims that `mu_Q(theta)` selects Born-rule states via an extremum, and `mu_Q` is identically zero for all states, then no selection occurs. This is a clean falsification of the specific model, not a generic falsification of the conjecture across all possible quantum channels. The paper does not overclaim. **SOUND.**

**One subtlety the paper handles correctly:** The conjecture as stated in Eq. (5) uses `max(rho_Q, 0)`, which clamps negative values to zero. This means the conjecture is only about the *positive* part of `rho_Q`. Since `rho_Q` is never positive in the dynamics, the clamped integrand is identically zero. The paper correctly identifies this and does not claim falsification based on `rho_Q` being negative (which would be a weaker argument).

## 6. Unchecked Risk Areas

The following items were not fully verified in this review:

1. **Qutrit (d=3) generalization:** The d=3 initial state `|psi> = cos(theta)|00> + sin(theta)/sqrt(2)*(|11> + |22>)` and the d=3 swap Hamiltonian construction in `test_b_dynamics.py` lines 576-595 were not independently verified for correctness. The paper reports only 3 spot-check trajectories for d=3. The normalization of the d=3 state should be verified: `|cos(theta)|^2 + 2*|sin(theta)/sqrt(2)|^2 = cos^2(theta) + sin^2(theta) = 1`. **This checks out.** The swap Hamiltonian `H_swap[idx_ij, idx_ji] += g` for all `(i,j)` is the full permutation operator, which is the correct generalization of the qubit XX+YY coupling to the full SWAP.

2. **Non-Markovian channels and amplitude damping:** The paper identifies these as open directions. They were not tested. The falsification claim is appropriately scoped to Markovian Lindblad dynamics.

3. **Analytical proof that r >= 1 for general theta (not just theta=pi/4):** The analytical argument in Section 1.5 of this review covers this case by noting that populations are time-invariant and marginals are constant. However, a formal proof with Hamiltonian + dephasing interaction terms would require showing that the Hamiltonian does not transfer populations between `|00>, |01>, |10>, |11>` for the initial state form used. Since `H|00> = 0` and `H|11> = 0`, the `|00>` and `|11>` populations are indeed invariant under both H and the dephasing. The `|01>` and `|10>` populations start at zero and are mixed by H, but they are populated only if there is a transition from `|00>` or `|11>` into the `{|01>, |10>}` subspace. Since H does not create such transitions from `|00>` or `|11>`, and dephasing only destroys coherences (not populations), the `{|01>, |10>}` subspace remains unpopulated. **This closes the analytical gap.** r >= 1 throughout.

4. **Convergence of trapezoidal integration for mu_Q:** Since `max(rho_Q, 0) = 0` at all stored points, the trapezoidal integral is exactly zero regardless of step size. This is trivially converged. **No issue.**

5. **The claim about alpha_half spread of 0.069 in Test A:** This is a numerical result from the bisection root-finder on a 200-point grid. I did not independently reproduce the number, but the code logic is sound and the bisection tolerances (1e-12) are far tighter than the claimed spread. Plausible and self-consistent with the reported table values (alpha_half ranges from 0.890 to 0.959, spread = 0.069). **Not independently confirmed but no reason to doubt.**

## 7. Summary of Findings

| Item | Location | Status | Severity |
|------|----------|--------|----------|
| Quantum experiential density definition | Eq. (3), Def. 1 | SOUND | -- |
| Pure-state limit I = 2*S_B, rho_Q = -2*S_B | Eq. (4) | SOUND | -- |
| Reported rho_Q value for pilot trajectory | Line 402 | **ERROR** | **Minor** |
| Superoperator construction | Eq. (14), lindblad.py | SOUND | -- |
| Dephasing rate exp(-2*gamma_D*t) | Eq. (9), validation | SOUND | -- |
| Exchange Hamiltonian structure | Eq. (8) | SOUND | -- |
| r >= 1 mechanism (monotone decrease from 2 to 1) | Section 5, code | SOUND | -- |
| Diagonal BM state construction | Eqs. (6)-(7), quantum_info.py | SOUND | -- |
| RK4 integrator | lindblad.py | SOUND | -- |
| Falsification logic (mu_Q = 0 implies no selection) | Section 4, 6 | SOUND | -- |
| Parabolic peak rho_Q_max = S_B/4 at r=1/2 | Lines 330-332 | SOUND | -- |
| Asymmetric dephasing extension | Eq. (10), test_b_dynamics.py | SOUND | -- |
| Qutrit generalization | test_b_dynamics.py lines 570-610 | Plausible, not fully verified | -- |

### Error Detail

**Line 402:** The paper states "giving r = 2 and rho_Q = -0.693 nats" for the pilot trajectory at theta = pi/4. Given `I_vN = 2*ln(2) = 1.386 nats` and `S_B = ln(2) = 0.693 nats`, the experiential density is `rho_Q = I*(1 - I/S_B) = 1.386*(1-2) = -1.386 nats`, not `-0.693 nats`. The reported value is off by a factor of 2. This is a typo in the narrative; the code computes the correct value.

## 8. Overall Mathematical Confidence

**HIGH.** The paper's mathematical framework is self-consistent. The core equations are standard quantum information theory (von Neumann entropy, quantum mutual information) applied to a well-defined functional. The superoperator construction and RK4 integrator are correct. The falsification logic is valid: the exchange Hamiltonian preserves populations in the `{|00>, |11>}` subspace while dephasing destroys coherences, so the system transitions directly from r=2 (entangled pure) to r=1 (perfectly tracked classical) without entering the r < 1 regime where rho_Q > 0. The one numerical error found (factor of 2 in a quoted value) is a presentation issue that does not affect any conclusion.

The mathematical claim "mu_Q = 0 identically for all tested parameters" follows necessarily from "rho_Q <= 0 throughout the evolution," which in turn follows from "r >= 1 throughout," which is analytically provable for this Hamiltonian + dephasing model class.
