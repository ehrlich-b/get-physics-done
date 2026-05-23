# Phase 1: Theorem A Assembly - Research

**Researched:** 2026-03-15
**Domain:** Metastability theory for reversible finite Markov chains; composition of exponential bounds
**Confidence:** HIGH

## Summary

Phase 1 assembles a self-contained proof of Theorem A (Boltzmann brain negligibility) from seven constituent lemmas that draw on four established mathematical frameworks: Freidlin-Wentzell cycle hierarchy (Lemma 1), BEGK potential-theoretic metastability (Lemma 2), quasi-stationary distribution convergence (Lemma 3), and Donsker-Varadhan large deviations (Lemma 6). The remaining lemmas (4, 5, 7) are direct consequences of combining these foundational results with the experiential density definition.

The core mathematical challenge is not proving any individual lemma -- each follows from well-established results in the literature -- but rather ensuring the error terms from all seven lemmas compose cleanly to preserve the exponential form mu_BB/mu_stable <= C*exp(-(Delta_s - Delta_b - alpha)/epsilon). The composition requires tracking how prefactors C_i from each lemma multiply, how correction terms of the form (1 + O(exp(-gamma/epsilon))) combine, and verifying that no hidden polynomial-in-1/epsilon prefactors destroy the exponential bound.

The recommended approach is: (1) state each lemma precisely with its error term in the form "exact quantity * (1 + correction)" where the correction is exponentially small, (2) build the dependency graph bottom-up (L1 feeds L2,L3,L6; L2,L3 feed L4; L2 feeds L5; L4,L5,L6 feed L7), and (3) at L7 verify that the product of all correction factors remains 1 + O(exp(-gamma'/epsilon)) for some gamma' > 0. Validate the assembled bound against the three-state chain numerical results.

**Primary recommendation:** Use the BEGK potential-theoretic framework (Bovier-den Hollander monograph, Chapters 7-8) as the primary reference for Lemma 2, Freidlin-Wentzell (1984/2012, Chapter 6) for Lemma 1, Champagnat-Villemonais (2014) for Lemma 3, and the standard DV large deviation principle for finite chains for Lemma 6. Assemble top-down from the theorem statement, citing each ingredient with its precise error form.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-begk: Bovier, Eckhoff, Gayrard, Klein (2001-2004) | method | Supplies the sharp asymptotic formula for mean exit times via capacities (Lemma 2) | read, cite specific theorems | plan, execution, verification |
| ref-fw: Freidlin, Wentzell (1984/2012) | method | Supplies the cycle hierarchy and communication heights defining basin decomposition (Lemma 1) | read, cite Chapter 6 | plan, execution, verification |
| ref-dv: Donsker, Varadhan (1975-1983) | method | Supplies the large deviation principle for empirical measures giving concentration (Lemma 6) | read, cite | plan, execution, verification |
| Bovier, den Hollander -- Metastability: A Potential-Theoretic Approach (2015) | method | Comprehensive modern reference unifying BEGK + FW for reversible chains; Chapters 7-8 cover finite chains | read, cite as primary reference | plan, execution |
| Landim -- Metastable Markov chains (arXiv:1807.04144, 2018) | review | Modern review of metastability via martingale problem approach; useful for the non-reversible perspective and composition of estimates | read for technique comparison | plan |
| Champagnat, Villemonais (arXiv:1404.1349, 2014) | method | Exponential convergence to QSD; Lemma 3 source | read, cite specific theorem | plan, execution, verification |
| draft.md Section 7/Appendix B | prior artifact | Contains the Theorem A statement and 7-lemma dependency graph | use as specification | plan, execution |
| three_state_chain.py | prior artifact | Numerical verification baseline: mu_BB/mu_stable matches analytical formula within 1% | use for validation | verification |

**Missing or weak anchors:** The draft's Appendix B dependency graph is a one-level ASCII tree. It does not specify the precise inputs and outputs (types, error forms) passed between lemmas. This must be constructed during execution. The DV concentration inequality (Lemma 6) needs a specific form suitable for weighted empirical measures -- the standard DV result is for unweighted empirical measures, so the extension to rho-weighted measures needs careful handling (likely via a contraction principle or direct application of the DV rate function to the functional mu = integral rho(p_t) dt).

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Entropy base | Nats (natural logarithm) | Bits (log base 2) | Project CONVENTIONS.md |
| Generator convention | Probabilist: dp/dt = pQ (row-vector left) | Physicist: dp/dt = Qp (column-vector) | Project CONVENTIONS.md |
| Matrix norm | sup-norm on rows: \|\|P\|\|_inf = max_i sum_j \|P_ij\| | Spectral norm, Frobenius | Project CONVENTIONS.md |
| Communication height | FW convention: Delta = min over paths of max edge cost | Some references use V(x,y) for quasi-potential | Freidlin-Wentzell (1984) |
| Rate scaling | Q_eps(x,y) ~ exp(-[E(y)-E(x)]^+/epsilon) for Metropolis | Glauber dynamics, heat-bath | Draft Section 7.2 |
| Time horizon | T_eps = exp((Delta_s - alpha)/epsilon), continuous time | Discrete time step count | Draft Section 7.2 |
| Basin ordering | Delta_s > Delta_b (stable basin deeper) | This is the critical physics input | Draft Section 7.5 |

**CRITICAL: All equations and results below use these conventions. The probabilist generator convention means the stationary distribution pi satisfies piQ = 0 (row vector times generator = zero). References using the physicist convention (Qp = 0 with column vectors) must be transposed before use.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| mu_BB/mu_stable <= C*exp(-(Delta_s - Delta_b - alpha)/epsilon) | Theorem A bound | Draft Section 7.2 | The target inequality to prove |
| E_x[tau_A] = (1/pi(x)) * (1/cap(x,A)) | BEGK hitting time formula | Bovier-den Hollander Ch.7, Thm 7.8 | Core of Lemma 2 |
| cap(x,A) = sum_{y in A} c(x,y) h_A(y) | Capacity via equilibrium potential | Bovier-den Hollander Ch.7 | Capacity computation |
| pi_QSD convergence: \|\|P^t_D - nu_D\|\| <= C*exp(-gamma_D * t) | QSD convergence | Champagnat-Villemonais (2014) | Lemma 3 |
| I_T(mu) = -(1/T) * inf_u>0 (mu, Lu/u) | DV rate function | Donsker-Varadhan (1975) | Lemma 6 concentration |
| rho(p) = I(B;M) * (1 - I(B;M)/H(B)) | Experiential density | Draft Section 3.1 | Connects abstract bound to physical observable |
| pi_b/pi_s = (1-p)/p * exp(-(Delta_s - Delta_b)/epsilon) | Three-state ratio | three_state_chain.py (verified) | Validation target |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Potential theory for Markov chains | Relates mean hitting times to capacities via Dirichlet forms | Lemma 2 (residence time) | Bovier-den Hollander Ch.7 |
| FW cycle hierarchy construction | Partitions state space into nested metastable wells | Lemma 1 (basin partition) | Freidlin-Wentzell Ch.6 |
| Doob h-transform | Conditions the chain to stay in a basin; produces the QSD | Lemma 3 (QSD convergence) | Champagnat-Villemonais (2014) |
| Spectral theory of sub-Markov semigroups | Gives convergence rate to QSD via spectral gap of killed generator | Lemma 3 (convergence rate) | Collet-Martinez-San Martin (2013) |
| Large deviation principle for empirical measures | Concentration of time-averaged functionals around expectations | Lemma 6 (DV concentration) | Donsker-Varadhan (1975-1983) |
| Renewal theory for excursion cycles | Decomposes trajectory into cycles visiting stable vs BB basins | Lemma 5 (BB occupation bound) | Standard; Bovier-den Hollander Ch.8 |
| Error term multiplication and bounding | Combining (1+delta_i) factors where delta_i are exponentially small | Lemma 7 (ratio assembly) | Elementary but critical |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Low-noise asymptotics (epsilon -> 0) | epsilon (noise/temperature) | epsilon << min(Delta_s, Delta_b) | Corrections O(exp(-c/epsilon)) for c > 0 | Exact computation for specific epsilon values |
| QSD approximation within basins | exp(-gamma*t) where gamma = spectral gap of killed chain | t >> 1/gamma (time within basin much longer than mixing time) | O(exp(-gamma*t)) | Direct simulation of p_t |
| Time horizon truncation | alpha/epsilon in the exponent | 0 < alpha < Delta_s - Delta_b | Loses alpha in the rate; tighter alpha gives longer observation | Adaptive horizon selection |
| Metropolis rate approximation | Exact for Metropolis dynamics; no approximation needed | Reversible chains with energy function | Exact within the model class | Glauber/heat-bath dynamics (similar asymptotics, different prefactors) |

## Standard Approaches

### Approach 1: Potential-Theoretic Assembly (RECOMMENDED)

**What:** Use the BEGK potential-theoretic framework to express all hitting times and exit times in terms of capacities, then use the Dirichlet-Thompson variational principle to bound capacities and hence obtain sharp asymptotics for residence times. Build the proof by stating each lemma with its error term, then composing them in the dependency graph order.

**Why standard:** This is the mature, definitive approach to metastability for reversible finite Markov chains. The Bovier-den Hollander monograph (2015) is the standard reference. The potential-theoretic approach yields sharp (not just logarithmic) asymptotics, meaning the prefactor C is controlled, not just the exponential rate.

**Track record:** Successfully applied to Ising model metastability, random field Curie-Weiss model, stochastic Ising model, Kawasaki dynamics. The BEGK papers (2001-2004) in Comm. Math. Phys. and J. Stat. Phys. are among the most cited in the metastability literature.

**Key steps:**

1. **State Lemma 1 (Basin Partition):** Apply the Freidlin-Wentzell cycle hierarchy to decompose the state space into metastable sets B_stable and B_BB with communication heights Delta_s and Delta_b respectively. This is a graph-theoretic construction using the W-graph (tree of optimal transition paths). Cite FW Ch.6 Theorem 6.3.1.

2. **State Lemma 2 (Residence Time Lower Bound):** Apply the BEGK capacity formula. For a reversible chain with generator Q_eps on finite state space, the mean exit time from basin B_stable satisfies E_x[tau_{B_stable^c}] = (1 + O(eps)) * exp(Delta_s/epsilon) / (pi(x) * cap(B_stable, B_stable^c)). The capacity cap can be bounded using variational principles to get sharp prefactors. The key result is E[tau] ~ K * exp(Delta_s/epsilon) where K is a computable prefactor. Cite Bovier-den Hollander Ch.7 Theorem 7.8 and the original BEGK Comm. Math. Phys. 228 (2002) 219-255.

3. **State Lemma 3 (QSD Convergence):** The killed chain (chain restricted to B_stable with absorption at the boundary) has a unique quasi-stationary distribution nu_QSD. The conditional distribution p_t given survival converges to nu_QSD at exponential rate: ||p_t - nu_QSD||_TV <= C*exp(-gamma*t) where gamma is the spectral gap of the killed generator. Since the mean exit time is exp(Delta_s/epsilon) and the spectral gap is polynomial in the chain parameters (not exponentially small), the chain equilibrates to the QSD long before exit. Cite Champagnat-Villemonais (Prob. Theory Rel. Fields, 2016) and Collet-Martinez-San Martin (2013).

4. **State Lemma 4 (Stable Measure Lower Bound):** Combine L2 and L3. During the residence time ~exp(Delta_s/epsilon) in B_stable, the chain is approximately at the QSD. The experiential density rho(nu_QSD) >= c > 0 by assumption (stable observers have non-trivial self-modeling). Therefore mu_stable = integral rho(p_t) dt >= c * (1-delta) * exp(Delta_s/epsilon) where delta accounts for the initial transient before QSD convergence. Since the transient time is polynomial while the residence time is exponential, delta = O(exp(-c'/epsilon)) for some c' > 0.

5. **State Lemma 5 (BB Occupation Upper Bound):** By the renewal structure of excursions: the chain makes ~1 excursion to B_BB before the observation time T_eps = exp((Delta_s-alpha)/epsilon) expires (because the inter-excursion time is ~exp(Delta_s/epsilon)). Each BB excursion lasts ~exp(Delta_b/epsilon). Total BB occupation is therefore O(exp(Delta_b/epsilon)). The experiential density during BB occupation is bounded by rho_max = H(B)/4. Therefore mu_BB <= rho_max * K' * exp(Delta_b/epsilon).

6. **State Lemma 6 (DV Concentration):** The time-averaged experiential measure (1/T)*integral rho(p_t) dt concentrates around its expected value with exponentially decaying probability of large deviations. For a functional of an ergodic Markov chain, the DV rate function gives P(|time_avg - E[time_avg]| > delta) <= exp(-T * I(delta)) where I is the rate function. Since T is exponentially large, the concentration is super-exponentially tight. This ensures the random variable mu (the actual trajectory integral) is close to its expectation with overwhelming probability.

7. **State Lemma 7 (Ratio Assembly):** Divide the bound from L5 by the bound from L4: mu_BB/mu_stable <= (rho_max * K' * exp(Delta_b/epsilon)) / (c * (1-delta) * exp(Delta_s/epsilon)) = (rho_max * K')/(c * (1-delta)) * exp(-(Delta_s - Delta_b)/epsilon). Set C = rho_max*K'/(c*(1-delta)) and note that the time horizon parameter alpha appears because T_eps = exp((Delta_s-alpha)/epsilon) sets how long we observe. The alpha term enters because the observation horizon limits the number of excursion cycles. Final form: mu_BB/mu_stable <= C * exp(-(Delta_s - Delta_b - alpha)/epsilon).

**Known difficulties at each step:**

- Step 2: The capacity computation requires sharp bounds on the equilibrium potential. For general energy landscapes, this may require the Dirichlet-Thompson variational principle to get matching upper and lower bounds.
- Step 3: Must verify that the spectral gap of the killed chain is not exponentially small -- this is guaranteed for well-separated basins but needs explicit verification.
- Step 5: The renewal argument assumes that successive excursions are approximately independent. This holds because the chain re-equilibrates to the QSD between excursions, but the precise error term needs tracking.
- Step 7: The prefactor C must be shown to be O(1) in epsilon (no polynomial growth in 1/epsilon). This is the critical composition step.

### Approach 2: Martingale Problem Approach (FALLBACK)

**What:** Use the Beltran-Landim characterization of metastable chains as solutions to martingale problems. This approach is more modern, extends to non-reversible chains, and provides a clean separation between the "trace process" (reduced chain on metastable sets) and the "local equilibrium" (QSD within basins).

**When to switch:** If the potential-theoretic approach encounters difficulties with non-sharp error terms or if the reversibility assumption is questioned. Also if the composition of error bounds is cleaner in the martingale framework.

**Tradeoffs:** More abstract; less explicit about prefactors C. The potential-theoretic approach gives sharper bounds (multiplicative 1+o(1) errors). The martingale approach gives cleaner structural results (exact exponential distribution of exit times, exact Markov property of the trace process). For this phase, where explicit C is needed, the potential-theoretic approach is preferred.

**Key references:** Beltran-Landim, J. Stat. Phys. 141 (2010); Landim, arXiv:1807.04144.

### Anti-Patterns to Avoid

- **Sketching instead of assembling:** The forbidden proxy (fp-sketch-only) explicitly rejects "the tools exist" language. Every step must have a precise error term, not just a citation.
  - _Example:_ Writing "By BEGK, the residence time is exponential" without specifying which BEGK theorem, what the prefactor is, and what the error term looks like.

- **Losing track of prefactors:** The theorem requires C to be explicit (not just "there exists a C"). Every multiplicative constant must be tracked through the composition chain.
  - _Example:_ Writing "the error is O(exp(-c/epsilon))" without specifying c relative to Delta_s - Delta_b.

- **Ignoring the alpha parameter:** The time horizon T_eps = exp((Delta_s - alpha)/epsilon) introduces alpha into the bound. Forgetting this makes the bound look like Delta_s - Delta_b in the exponent rather than Delta_s - Delta_b - alpha.
  - _Example:_ Stating the T -> infinity result instead of the finite-horizon result (this was the original error corrected in Section 7.1 of the draft).

- **Conflating expected values with concentration:** The expected occupation times give the right exponential rates, but the theorem needs high-probability bounds, not just expectations. Lemma 6 (DV concentration) bridges this gap.
  - _Example:_ Computing E[mu_BB]/E[mu_stable] without showing that mu_BB and mu_stable concentrate around their expectations.

## Existing Results to Leverage

**This section is MANDATORY.** The individual lemmas are all consequences of established results. The value of this phase is composition, not re-derivation.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| BEGK mean exit time formula | E_x[tau_A] ~ 1/(pi(x)*cap(x,A)) as eps->0 | Bovier et al., Comm. Math. Phys. 228 (2002), Thm 1.2 | Cite directly for Lemma 2 |
| FW cycle hierarchy | State space decomposes into nested metastable cycles with depth = communication height | Freidlin-Wentzell (1984/2012), Ch.6, Thm 6.3.1 | Cite for Lemma 1 |
| QSD existence and uniqueness (finite chain) | Unique QSD exists for irreducible finite chain killed at boundary | Collet-Martinez-San Martin (2013), Thm 3.1 | Cite for Lemma 3 |
| QSD exponential convergence | ||P^n_D(x,.) - nu_QSD||_TV <= C*r^n, r < 1 | Champagnat-Villemonais, PTRF 2016 | Cite for Lemma 3 rate |
| DV large deviation principle (finite chains) | P(L_T in A) ~ exp(-T * inf_{mu in A} I(mu)) | Donsker-Varadhan (1975-1983) | Cite for Lemma 6 |
| Detailed balance => reversibility for 3-state chain | pi_b/pi_s = (1-p)/p * exp(-(Delta_s-Delta_b)/eps) | three_state_chain.py (verified analytically and numerically) | Validation benchmark |
| rho(pi) = I(B;M)*(1-I(B;M)/H(B)) with rho_max = H(B)/4 | Peak at I = H(B)/2 | Draft Section 3.2 | Used in density bounds |

**Key insight:** Every individual lemma restates a known theorem in the context of this specific problem. The phase's contribution is the composition chain -- showing the error terms multiply without destroying the exponential bound. Do not waste context re-proving BEGK or Freidlin-Wentzell results.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Capacity-exit time duality | cap(A,B) = pi(A) / E_pi[tau_B] for equilibrium measure pi | Bovier-den Hollander Ch.7 | Reversible chains |
| Exponential distribution of exit times | tau_exit / E[tau_exit] -> Exponential(1) as eps->0 | BEGK Comm. Math. Phys. 228, Thm 1.4 | Reversible, well-separated basins |
| Spectral gap of killed chain | gamma_D >= polynomial in chain parameters (not exp. small) | Standard spectral theory | Basin diameter bounded, rates bounded below |
| Renewal decomposition of occupation | tau_BB(T) = sum_{k=1}^{N(T)} sigma_k where sigma_k are excursion durations | Standard renewal theory | Regeneration at basin re-entry |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Metastability and Low Lying Spectra in Reversible Markov Chains | Bovier, Eckhoff, Gayrard, Klein | 2002 | Core Lemma 2 source | Thm 1.2 (mean exit time), Thm 1.4 (exponential law) |
| Metastability: A Potential-Theoretic Approach | Bovier, den Hollander | 2015 | Modern comprehensive reference | Ch.7 (finite chains), Ch.8 (applications) |
| Random Perturbations of Dynamical Systems | Freidlin, Wentzell | 1984/2012 | Core Lemma 1 source | Ch.6 (cycle hierarchy), communication heights |
| Exponential convergence to QSD and Q-process | Champagnat, Villemonais | 2014/2016 | Core Lemma 3 source | Main theorem: conditions for exponential QSD convergence |
| Metastable Markov chains | Landim | 2018 | Modern review | Martingale characterization, composition techniques |
| Quasi-Stationary Distributions | Collet, Martinez, San Martin | 2013 | QSD monograph | Existence, uniqueness, spectral theory of killed chains |
| Large deviations for empirical measures of reversible jump Markov processes | Dupuis, Liu, Lipshutz | 2013/2015 | Explicit DV rate function for reversible chains | Rate function formula for finite state reversible chains |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy | sympy (any recent) | Symbolic verification of error term composition | Used in three_state_chain.py already |
| NumPy/SciPy | numpy, scipy.linalg | Numerical verification against three-state chain | Eigenvalue computation, matrix exponentiation |
| Python 3 | standard | Implementation language | Already used in toy model |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Plotting mu_BB/mu_stable vs epsilon for validation | Final validation step |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| SymPy for symbolic algebra | Mathematica | More powerful CAS but external dependency; SymPy sufficient for this problem |
| Manual LaTeX proof | Lean 4 formal verification | Massive overhead; not justified for this problem scale |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Three-state chain validation | < 1 second | None | Already implemented |
| Symbolic error term tracking | Minutes | CAS complexity | Keep expressions simple; use asymptotic forms |
| 16-state toy model cross-check | < 1 second | None | Already implemented in composite_self_model.py |

**Installation / Setup:**
```bash
# All required packages are already available in the project
pip install numpy scipy sympy matplotlib
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Error term composition | Product of (1+delta_i) remains 1+O(exp(-c/eps)) | Multiply all seven error factors symbolically | No polynomial-in-1/eps prefactors in the final bound |
| Dimensional consistency | All terms in the bound have consistent units | Check each lemma's output units match the next lemma's input | All error terms are dimensionless ratios |
| Exponent accounting | Delta_s - Delta_b - alpha appears correctly | Track which lemma contributes which term to the exponent | L2 contributes Delta_s, L5 contributes Delta_b, time horizon contributes alpha |
| Prefactor C is O(1) | C does not grow with 1/epsilon | Examine C = rho_max*K'/(c*(1-delta)) as eps->0 | C converges to a finite constant |
| Dependency graph acyclicity | No circular dependencies among lemmas | Verify the partial order L1 -> {L2,L3,L6}; {L2,L3} -> L4; L2 -> L5; {L4,L5,L6} -> L7 | DAG confirmed |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Three-state chain (eps=0.5) | Delta_s=3.0, Delta_b=1.0, p=0.5 | pi_b/pi_s = exp(-4.0) * 1.0 = 0.0183 (exact) | three_state_chain.py |
| Three-state chain (eps->0) | Slope of log(ratio) vs 1/eps | Slope = -(Delta_s - Delta_b) = -2.0 | three_state_chain.py (verified <1% error) |
| Equal depths (Delta_s = Delta_b) | No suppression | pi_b/pi_s = (1-p)/p (constant) | Draft Section 7.5 |
| Large epsilon | eps >> Delta_s | All basins equally visited; no metastability | Physical intuition |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| mu_BB/mu_stable for three-state chain | Run three_state_chain.py; compare assembled formula against exact computation | < 1% relative error | Analytical formula from the chain |
| Exponential decay rate | Linear fit of log(mu_BB/mu_stable) vs 1/epsilon | Slope within 0.1% of -(Delta_s-Delta_b) | three_state_chain.py existing verification |
| Prefactor C numerical value | Compute C from assembled formula for three-state chain | Should be O(1), not growing | C = rho_b/rho_s * (1-p)/p for three-state chain |

### Red Flags During Computation

- If any error term delta_i grows polynomially in 1/epsilon rather than decaying exponentially, the composition chain is broken. Investigate which lemma boundary is too loose.
- If the prefactor C contains epsilon-dependent terms that blow up, check whether a sharper form of the underlying theorem (with multiplicative 1+o(1) errors rather than additive O(1) errors) is needed.
- If the final exponent is Delta_s - Delta_b rather than Delta_s - Delta_b - alpha, the time horizon constraint has been dropped -- this means the finite-horizon aspect is missing.
- If the bound requires Delta_s - Delta_b > alpha (with alpha free) but the assembled proof fixes alpha, check whether the constraint 0 < alpha < Delta_s - Delta_b is correctly propagated.

## Common Pitfalls

### Pitfall 1: Confusing T -> infinity with epsilon -> 0

**What goes wrong:** Using the ergodic theorem (T -> infinity at fixed epsilon) instead of the metastability regime (epsilon -> 0 at fixed observation time). The ergodic ratio pi_b/pi_s is a positive constant for any fixed epsilon.

**Why it happens:** The T -> infinity limit is the natural first instinct. The draft explicitly corrects this error in Section 7.1.

**How to avoid:** Always state the asymptotic parameter is epsilon -> 0. The observation horizon T_eps = exp((Delta_s - alpha)/epsilon) grows with 1/epsilon but is finite for each epsilon.

**Warning signs:** If the bound doesn't depend on epsilon, something is wrong.

**Recovery:** Go back to the BEGK framework where epsilon -> 0 is the fundamental limit.

### Pitfall 2: Treating Expected Values as High-Probability Bounds

**What goes wrong:** Computing E[mu_BB/mu_stable] and declaring the theorem proved, without showing concentration.

**Why it happens:** Expected values are easier to compute than high-probability bounds.

**How to avoid:** Use Lemma 6 (DV concentration) to convert expectations to high-probability statements. The DV rate function for the empirical measure gives exponential concentration when T is exponentially large.

**Warning signs:** The word "expectation" without "concentration" or "with probability."

**Recovery:** Apply the DV large deviation principle. For exponentially long trajectories, the concentration is super-exponentially tight, so the bound on the expected value transfers to a high-probability bound with only sub-leading corrections.

### Pitfall 3: Non-Composition of Error Terms

**What goes wrong:** Each lemma has an error term "1 + O(exp(-c_i/epsilon))". If c_i < Delta_s - Delta_b for any i, the error term can dominate the main term and the exponential bound is destroyed.

**Why it happens:** Individual lemma error terms may have different rates c_i, and the minimum c_i controls the final bound.

**How to avoid:** Track every c_i explicitly. The final bound requires min_i(c_i) > 0 (and ideally min_i(c_i) > Delta_s - Delta_b - alpha to avoid it entering the exponent).

**Warning signs:** An error term with unspecified rate "O(exp(-c/epsilon))" where c is not compared to Delta_s - Delta_b.

**Recovery:** Go back and compute c_i for each lemma. If any c_i is too small, seek a tighter version of that lemma or restructure the composition.

### Pitfall 4: Missing the Density Contribution

**What goes wrong:** Proving the occupation time ratio tau_BB/tau_stable decays exponentially but forgetting that mu_BB/mu_stable involves the rho-weighted integral, not just raw occupation times.

**Why it happens:** The occupation time ratio is the hard part; the density weighting is "just a multiplicative constant."

**How to avoid:** Track rho(p_t) explicitly within each basin. Use QSD convergence (Lemma 3) to show that rho(p_t) is approximately constant within each basin, then use the density bounds from the theorem's assumptions.

**Warning signs:** The final bound has no reference to rho, c, or rho_max.

**Recovery:** Multiply by rho_max/c to get the correct prefactor.

### Pitfall 5: Reversibility Assumption Leakage

**What goes wrong:** Using a result that requires reversibility but applying it to a sub-chain or modified chain that is not reversible.

**Why it happens:** The killed chain (restricted to B_stable with absorption at boundary) inherits reversibility from the original chain, but this needs to be verified.

**How to avoid:** Explicitly verify that the killed chain is reversible (it is, for Metropolis dynamics restricted to a subset of states).

**Warning signs:** Applying BEGK results to the killed chain without noting it is reversible.

**Recovery:** The killed chain for a reversible original chain is indeed reversible. State this explicitly.

## Level of Rigor

**Required for this phase:** Physicist's proof with controlled error terms

**Justification:** The contract requires a "self-contained proof" but not a formal mathematical proof. The individual lemmas are established theorems; the contribution is showing they compose. Each step must cite a precise theorem from the literature, state the error term explicitly, and verify composition. However, we do not need to re-prove BEGK or Freidlin-Wentzell theory from scratch.

**What this means concretely:**

- Every lemma must cite the specific theorem number from the source reference
- Every error term must be written as a specific function of epsilon (not just "O(small)")
- The composition in Lemma 7 must explicitly multiply all error factors and show the result
- The constant C must be written in terms of the problem parameters (rho_max, c, Delta_s, Delta_b, p, spectral gaps)
- Approximations must state their regime of validity (epsilon << Delta_b is sufficient for most)
- The three-state chain must be verified to match within 1% as a numerical check

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Pathwise large deviations (FW only) | Potential theory + capacities (BEGK) | 2001-2004 | Sharp prefactors, not just logarithmic rates |
| Heuristic metastability arguments | Rigorous QSD theory (Champagnat-Villemonais) | 2014+ | Quantitative convergence rates to QSD |
| Separate treatments of exit times and mixing | Unified potential-theoretic framework (Bovier-den Hollander) | 2015 monograph | Single reference for all ingredients |
| Reversible-only theory | Martingale approach extends to non-reversible (Beltran-Landim) | 2010-2018 | Not needed here (chain is reversible) but available as fallback |

**Superseded approaches to avoid:**

- **Logarithmic asymptotics only:** Early FW results give only log E[tau] ~ Delta/epsilon. We need sharp asymptotics (with prefactor) from BEGK. Using log-level results loses control of the constant C.
- **Coupling-based mixing arguments:** While valid for mixing time bounds, coupling arguments do not give the sharp QSD convergence rate needed here. Use spectral theory instead.

## Open Questions

1. **DV concentration for weighted empirical measures**
   - What we know: Standard DV gives the LDP for the empirical measure (1/T)*sum delta_{X_t}. We need concentration for the rho-weighted functional (1/T)*integral rho(p_t) dt.
   - What's unclear: Whether this requires a contraction principle applied to the DV rate function, or whether a simpler argument (e.g., Lipschitz continuity of rho as a function of the empirical measure) suffices.
   - Impact on this phase: Affects how Lemma 6 is stated.
   - Recommendation: Use the fact that rho is bounded and continuous, so the weighted functional is a bounded Lipschitz functional of the empirical measure. The DV large deviation principle for the empirical measure, combined with the contraction principle, gives the LDP for the weighted functional. For finite state spaces, this is straightforward.

2. **Sharpness of the alpha parameter**
   - What we know: alpha appears because the time horizon T_eps = exp((Delta_s - alpha)/epsilon) is chosen to be strictly shorter than the mean exit time exp(Delta_s/epsilon).
   - What's unclear: Whether alpha can be taken to 0 (recovering the full exponent Delta_s - Delta_b) or whether it is fundamentally necessary.
   - Impact on this phase: Affects the tightness of the final bound.
   - Recommendation: Alpha is necessary because the chain must remain in B_stable with high probability during [0, T_eps]. The probability of exiting before T_eps is ~exp(-alpha/epsilon), which needs to be small. The bound cannot be improved without additional information about the exit time distribution beyond the mean. Proceed with alpha > 0 as stated.

3. **Explicit value of C for the three-state chain**
   - What we know: The three-state chain has C = (rho_b/rho_s) * (1-p)/p analytically.
   - What's unclear: Whether the general formula for C (involving spectral gaps, capacities, and QSD parameters) reduces to this simple form for the three-state chain.
   - Impact on this phase: Validation target.
   - Recommendation: Compute C from the general formula applied to the three-state chain and verify it matches (rho_b/rho_s)*(1-p)/p. This is the key validation test.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| BEGK capacity formula | Error terms not sharp enough for composition | Beltran-Landim martingale approach | Moderate: different framework but same final estimates |
| QSD convergence rate | Spectral gap of killed chain is too small | Direct simulation within basins | Low: numerical fallback |
| DV concentration | Weighted functional complication | Direct Markov chain concentration inequalities (e.g., McDiarmid for Markov chains) | Low: different concentration tool |
| Full composition | Error terms accumulate too fast | Prove a weaker bound (logarithmic asymptotics only: log(mu_BB/mu_stable) ~ -(Delta_s-Delta_b)/epsilon) | Low: weaker result but still meaningful |

**Decision criteria:** If any single error term delta_i is not exponentially small (i.e., grows polynomially in 1/epsilon), that lemma's formulation must be tightened. If tightening fails after investigating the sharp form of the underlying theorem, switch to the logarithmic asymptotics fallback -- this loses the explicit C but preserves the exponential decay rate.

## Caveats and Alternatives

**Self-critique answers:**

1. **What assumption might be wrong?** The assumption that all error terms delta_i in the composition have rates c_i comfortably larger than Delta_s - Delta_b. If some c_i is comparable to Delta_s - Delta_b, the error term enters the exponent and the bound weakens. This is most likely to happen with the QSD convergence rate (Lemma 3) if the spectral gap of the killed chain is comparable to 1/exp(Delta_s/epsilon).

2. **What alternative approach was dismissed too quickly?** The martingale approach of Beltran-Landim. This gives cleaner structural results (exact Markov property of the trace process) and might make the composition more transparent. However, it is less explicit about prefactors, which the contract requires.

3. **What limitation am I understating?** The DV concentration (Lemma 6) for the rho-weighted functional. This is not a direct application of the standard DV theorem but requires an additional step (contraction principle or Lipschitz argument). If rho is not sufficiently smooth as a function of the empirical measure, this step could require more care.

4. **Is there a simpler method?** For the three-state chain, the entire theorem is a direct computation (as in three_state_chain.py). The general proof is needed only because the framework aims for arbitrary finite Markov chains satisfying the setup conditions. There is no simpler method for the general case.

5. **Would a specialist disagree?** A probabilist specializing in metastability might prefer the Beltran-Landim approach over BEGK for aesthetic reasons. They might also insist on sharper statements about the exponential distribution of exit times (BEGK Thm 1.4) rather than just mean exit times. This is a valid point -- using the exponential law directly would strengthen the high-probability bound in Lemma 2 and could make Lemma 6 unnecessary (the exponential law already gives concentration). This is worth investigating as a possible simplification.

## Sources

### Primary (HIGH confidence)

- Bovier, A., den Hollander, F. -- Metastability: A Potential-Theoretic Approach, Springer (2015), Grundlehren vol. 351 -- comprehensive reference for BEGK framework, Chapters 7-8 for finite chains
- Bovier, A., Eckhoff, M., Gayrard, V., Klein, M. -- "Metastability and Low Lying Spectra in Reversible Markov Chains," Comm. Math. Phys. 228 (2002) 219-255 -- original BEGK capacity-exit time formula
- Freidlin, M.I., Wentzell, A.D. -- Random Perturbations of Dynamical Systems, 3rd ed., Springer (2012) -- cycle hierarchy, communication heights
- Champagnat, N., Villemonais, D. -- "Exponential convergence to quasi-stationary distribution and Q-process," Prob. Theory Rel. Fields 164 (2016) 243-283 [arXiv:1404.1349] -- QSD convergence rates
- Donsker, M.D., Varadhan, S.R.S. -- "Asymptotic evaluation of certain Markov process expectations for large time, I-IV," Comm. Pure Appl. Math. (1975-1983) -- large deviation principle for empirical measures
- Collet, P., Martinez, S., San Martin, J. -- Quasi-Stationary Distributions: Markov Chains, Diffusions, and Dynamical Systems, Springer (2013) -- comprehensive QSD reference

### Secondary (MEDIUM confidence)

- Landim, C. -- "Metastable Markov chains," arXiv:1807.04144 (2018) -- modern review via martingale problems
- Beltran, J., Landim, C. -- "Tunneling and Metastability of Continuous Time Markov Chains," J. Stat. Phys. 140 (2010) 1065-1114 -- non-reversible extension
- Dupuis, P., Liu, Y., Lipshutz, D. -- "On the large deviation rate function for the empirical measures of reversible jump Markov processes," Ann. Probab. 43 (2015) 1121-1156 [arXiv:1302.6647] -- explicit DV rate function for reversible chains

### Tertiary (LOW confidence)

- The extension from standard DV (unweighted empirical measure) to the rho-weighted functional -- based on standard contraction principle arguments but not verified against a specific reference for this exact setup. Needs validation during execution.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - All four underlying theories (BEGK, FW, QSD, DV) are established and well-documented in monographs
- Standard approaches: HIGH - The potential-theoretic approach is the canonical method for reversible finite Markov chains
- Computational tools: HIGH - SymPy/NumPy are standard; three-state chain verification already exists
- Validation strategies: HIGH - Three-state chain provides a concrete computable benchmark; analytical formula exists

**Research date:** 2026-03-15
**Valid until:** Indefinite for mathematical results. The underlying theorems (BEGK, FW, QSD, DV) are permanent results in probability theory.
