# Phase 2: Lipschitz Stability - Research

**Researched:** 2026-03-16
**Domain:** Perturbation theory for finite Markov chains; continuity of information-theoretic functionals
**Confidence:** HIGH

## Summary

Phase 2 proves that the experiential density rho(P) = I(B;M) * (1 - I(B;M)/H(B)) is Lipschitz continuous in the transition kernel P under the sup-norm ||P - P'||_inf, with an explicit Lipschitz constant L characterized in terms of |Omega| and the spectral gap of P. The proof decomposes into two independent steps -- (Step 1) perturbation theory for stationary distributions showing ||pi - pi'||_1 is controlled by ||P - P'||_inf / gap(P), and (Step 2) continuity of mutual information showing |I(B;M) under pi - I(B;M) under pi'| is controlled by ||pi - pi'||_1 * log(|Omega|) -- followed by (Step 3) composing these through the rho = I*(1-I/H) functional form to get the final bound.

The mathematical ingredients are entirely standard. Perturbation theory for stationary distributions of finite ergodic Markov chains has been studied since Schweitzer (1968), with sharp bounds available via ergodicity coefficients, the group inverse of (I - P), and spectral gap arguments. Continuity of Shannon entropy and mutual information in total variation distance for finite alphabets is textbook material (Csiszar-Korner 1981, Cover-Thomas 2006). The contribution of this phase is composing these two standard results through the specific rho functional form with explicit constants, then verifying the bound numerically.

The draft (Section 3.7) already sketches this argument: "(i) stationary distribution is smooth in kernel entries, (ii) mutual information is Lipschitz in total variation, (iii) compose." This phase makes that sketch rigorous with explicit constants.

**Primary recommendation:** Use the Cho-Meyer perturbation bound for stationary distributions (||pi - pi'||_1 <= ||P - P'||_inf / gap(P)) as Step 1, the entropy continuity bound |H(p) - H(q)| <= delta * log(|A|-1) + h(delta) (with delta = ||p-q||_1, h = binary entropy) as the core of Step 2, and derive the Lipschitz constant for rho by chain-rule differentiation through I*(1-I/H). The expected form is L = O(|Omega|^2 * log(|Omega|) / gap(P)).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| ref-lmc: Lopez-Ruiz, Mancini, Calbet (1995) | definition | rho belongs to LMC family; C = H * D where D = disequilibrium; our rho = I*(1-I/H) is a bivariate LMC variant | cite | plan, writing |
| ref-gell-mann-lloyd: Gell-Mann, Lloyd (1996/2003) | background | Places rho in broader effective complexity family; motivation for why rho peaks between order and randomness | cite | writing |
| composite_self_model.py | prior artifact | Provides the 7-chain toy model (16 states, |B|=|M|=4) for numerical verification of Lipschitz bound | use for VALD-01 | plan, execution, verification |
| draft.md Section 3.7 | prior artifact | Contains the stability conjecture (Lipschitz form) with the two-step argument sketch; this phase proves it | use as specification | plan, execution |

**Missing or weak anchors:** The draft's Section 3.7 conjecture uses I/H notation without specifying whether H = H(B) or H(B,M). From the definition rho = I(B;M)*(1 - I(B;M)/H(B)), the denominator is H(B), not the joint entropy. This must be kept precise throughout. The draft also mentions a "Pinsker-type bound" for MI continuity, but the sharper tool is the entropy continuity lemma (uniform continuity of entropy), not Pinsker's inequality (which bounds total variation in terms of KL divergence, the wrong direction).

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Entropy base | Nats (natural logarithm) | Bits (log2) | Project CONVENTIONS.md |
| Mutual information | I(B;M) = H(B) + H(M) - H(B,M) | Conditional entropy form | Project CONVENTIONS.md |
| Experiential density | rho(P) = I(B;M) * (1 - I(B;M)/H(B)) | -- | Project CONVENTIONS.md |
| Matrix norm | sup-norm on rows: \|\|P\|\|_inf = max_i sum_j \|P_ij\| | Spectral norm, Frobenius | Project CONVENTIONS.md |
| Spectral gap (discrete) | gap(P) = 1 - \|lambda_2\| | Some refs use 1-lambda_2 (without absolute value); for reversible chains these coincide | Project CONVENTIONS.md |
| Stationary distribution | Row vector pi with piP = pi | Column vector convention | Project CONVENTIONS.md (probabilist convention) |
| Total variation distance | \|\|p - q\|\|_TV = (1/2) \|\|p - q\|\|_1 | Some refs use \|\|p-q\|\|_1 without the 1/2 factor | Use \|\|.\|\|_1 throughout and convert at boundaries |

**CRITICAL: All equations and results below use these conventions. The perturbation literature often uses ||.||_TV = (1/2)||.||_1. We use the L1 norm ||.||_1 = sum |p_i - q_i| throughout (which equals twice the total variation distance). All bounds below are stated in L1 norm. When citing results from papers using TV convention, multiply their bounds by 2.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| rho(P) = I_pi(B;M) * (1 - I_pi(B;M) / H_pi(B)) | Experiential density at stationarity | Draft Section 3.1 | The functional whose Lipschitz continuity we prove |
| pi P = pi, pi' P' = pi' | Stationary distribution equations | Standard | Starting point for perturbation theory |
| \|\|pi - pi'\|\|_1 <= (1/gap(P)) * \|\|P - P'\|\|_inf | Stationary distribution perturbation bound | Cho-Meyer (2001); Seneta (1993) | Step 1 of the proof |
| \|H(p) - H(q)\| <= delta * ln(\|A\| - 1) + h_bin(delta) for delta = \|\|p-q\|\|_1/2 | Entropy continuity (Fannes-Audenaert type) | Csiszar-Korner (1981), Cover-Thomas Ch.2; Audenaert (2007) for tight form | Core of Step 2 |
| I(B;M) = H(B) + H(M) - H(B,M) | MI decomposition into entropies | Standard information theory | Reduces MI continuity to entropy continuity |
| \|I_p(B;M) - I_q(B;M)\| <= \|H_p(B) - H_q(B)\| + \|H_p(M) - H_q(M)\| + \|H_p(B,M) - H_q(B,M)\| | Triangle inequality on MI | Trivial | Connects MI continuity to marginal entropy continuity |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Perturbation theory for stochastic matrices | Bounds sensitivity of pi to changes in P | Step 1 | Cho-Meyer, SIAM J. Matrix Anal. (2001); Seneta (1993); Schweitzer (1968) |
| Entropy continuity lemma | Bounds |H(p)-H(q)| in terms of \|\|p-q\|\|_1 | Step 2 | Csiszar-Korner, Information Theory (1981/2011); Cover-Thomas, Ch.2 |
| Marginal distribution perturbation | Relates \|\|p_B - q_B\|\|_1 to \|\|p - q\|\|_1 for marginals | Step 2 (marginalization step) | Data processing for L1: \|\|p_B - q_B\|\|_1 <= \|\|p - q\|\|_1 |
| Chain rule differentiation for composed functionals | Computes Lipschitz constant of f(g(x)) = Lip(f)*Lip(g) | Step 3 (composition) | Elementary calculus |
| Product formula differentiation | Lipschitz constant of rho = I*(1-I/H) via product rule | Step 3 | Elementary: \|f*g(x) - f*g(y)\| <= \|f\|*\|g(x)-g(y)\| + \|g\|*\|f(x)-f(y)\| |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Perturbation is small: \|\|P-P'\|\|_inf << gap(P) | \|\|P-P'\|\|_inf / gap(P) | P' must be irreducible; perturbation must not close the spectral gap | Exact for any size perturbation preserving irreducibility | Restrict to perturbation class with uniform spectral gap lower bound |
| Entropy continuity linear regime | \|\|pi - pi'\|\|_1 << 1 | When delta = \|\|pi-pi'\|\|_1/2 is small | The Fannes bound is exact up to constant; for small delta, |Delta H| ~ O(delta * ln(\|A\|)) | Full nonlinear Fannes-Audenaert bound |

## Standard Approaches

### Approach 1: Three-Step Composition (RECOMMENDED)

**What:** Decompose the proof into three independent steps:

1. **Step 1 (Stationary distribution perturbation):** For ergodic P, P' with gap(P) > 0, bound ||pi - pi'||_1 in terms of ||P - P'||_inf and gap(P).
2. **Step 2 (MI continuity):** For joint distributions p, q on B x M with ||p - q||_1 <= delta, bound |I_p(B;M) - I_q(B;M)| in terms of delta and |B|, |M|.
3. **Step 3 (rho composition):** Use the product structure rho = I*(1-I/H) to bound |rho(P) - rho(P')| by composing Steps 1 and 2 with the product rule.

**Why standard:** Each step uses a textbook result. The composition is straightforward chain-rule calculus. The draft's Section 3.7 already identifies this decomposition.

**Track record:** Perturbation bounds for stationary distributions: Schweitzer (1968), Seneta (1993), Cho-Meyer (2001), Mitrophanov (2005). Entropy/MI continuity: Csiszar-Korner (1981), Cover-Thomas (2006), Audenaert (2007). The individual ingredients are among the most basic results in their respective fields.

**Key steps:**

1. **Step 1: Stationary distribution perturbation bound.**
   - Let P, P' be irreducible stochastic matrices on Omega with |Omega| = n. Let pi, pi' be their respective stationary distributions.
   - The key bound: ||pi - pi'||_1 <= (1/gap(P)) * ||P - P'||_inf, where gap(P) = 1 - |lambda_2(P)| is the absolute spectral gap.
   - This follows from writing pi' - pi = pi'(P' - P)(I - P + Pi)^{-1} where Pi = 1*pi is the stationary projector, and bounding the group inverse ||(I - P + Pi)^{-1}|| <= 1/gap(P).
   - For reversible chains, |lambda_2| = max(lambda_2, |lambda_n|) where lambda_2 is the second-largest eigenvalue and lambda_n is the most negative. The spectral gap is well-defined.
   - **Sharper bound (Cho-Meyer):** ||pi - pi'||_1 <= ||pi||_inf * ||(I - P + Pi)^{-1}||_inf * ||P - P'||_inf. The condition number kappa = ||pi||_inf * ||(I - P + Pi)^{-1}||_inf is bounded above by 1/gap(P) for general chains, and can be much smaller.
   - **For this phase:** Use the simpler bound ||pi - pi'||_1 <= (1/gap(P)) * ||P - P'||_inf. This may overestimate for specific chains but gives the correct scaling. The numerical verification will confirm tightness.

2. **Step 2: Mutual information continuity.**
   - Let p, q be joint distributions on B x M with ||p - q||_1 <= delta. We need |I_p(B;M) - I_q(B;M)|.
   - Decompose: I(B;M) = H(B) + H(M) - H(B,M). By triangle inequality: |I_p - I_q| <= |H_p(B) - H_q(B)| + |H_p(M) - H_q(M)| + |H_p(B,M) - H_q(B,M)|.
   - For each term, use the entropy continuity lemma. For distributions on an alphabet of size k with ||p - q||_1 <= delta (where delta < 1):
     - |H(p) - H(q)| <= (delta/2) * ln(k - 1) + h_bin(delta/2)
     - where h_bin(x) = -x*ln(x) - (1-x)*ln(1-x) is binary entropy in nats.
   - For small delta: h_bin(delta/2) ~ (delta/2)*ln(2/delta), so |H(p) - H(q)| ~ O(delta * ln(k/delta)).
   - Apply to each term: |H_p(B) - H_q(B)| with k = |B|, using ||p_B - q_B||_1 <= ||p - q||_1 <= delta (data processing); |H_p(M) - H_q(M)| with k = |M|, using ||p_M - q_M||_1 <= delta; |H_p(B,M) - H_q(B,M)| with k = |B|*|M| = |Omega|, using ||p - q||_1 <= delta.
   - Combined: |I_p(B;M) - I_q(B;M)| <= (delta/2)[ln(|B|-1) + ln(|M|-1) + ln(|Omega|-1)] + 3*h_bin(delta/2).
   - Simplification for delta << 1: |I_p - I_q| <= C_I * delta * ln(|Omega|) where C_I is an O(1) constant (roughly 3/2 from the three terms, plus logarithmic corrections).
   - **Tighter bound (direct approach):** Instead of decomposing MI into three entropies, one can bound MI continuity directly. However, the three-entropy approach is more transparent and gives explicit |Omega| dependence.

3. **Step 3: Compose through rho = I*(1-I/H).**
   - Write rho = f(I, H) where f(I, H) = I*(1 - I/H) and I = I_pi(B;M), H = H_pi(B).
   - Both I and H are functions of pi, which is a function of P.
   - We need: |rho(P) - rho(P')| = |f(I, H) - f(I', H')|.
   - By product rule: |f(I,H) - f(I',H')| <= |I - I'| * |1 - I/H| + I * |I/H - I'/H'|.
   - The first factor: |1 - I/H| <= 1 always.
   - The second factor: |I/H - I'/H'| <= |I - I'|/H + I*|H - H'|/H^2 (quotient rule, assuming H, H' bounded away from 0).
   - So: |rho - rho'| <= |I - I'| + I*(|I - I'|/H + I*|H - H'|/H^2).
   - Since I <= H(B) <= ln(|B|), and H >= H_min (the minimum entropy of B under perturbation): |rho - rho'| <= O(1) * (|I - I'| + |H - H'|).
   - From Step 2: |I - I'| <= C_I * ||pi - pi'||_1 * ln(|Omega|) and |H - H'| <= C_H * ||pi - pi'||_1 * ln(|B|).
   - From Step 1: ||pi - pi'||_1 <= (1/gap(P)) * ||P - P'||_inf.
   - **Final bound:** |rho(P) - rho(P')| <= L * ||P - P'||_inf where L = O(ln(|Omega|) / gap(P)).
   - More precisely: L = C * ln(|Omega|) / gap(P) where C is a universal constant that depends on |B|, |M| only logarithmically.

**Known difficulties at each step:**

- Step 1: The bound ||pi - pi'||_1 <= (1/gap(P)) * ||P - P'||_inf assumes P' preserves irreducibility. If the perturbation drives P' to reducibility (gap(P') = 0), the bound still holds as a one-sided statement (pi exists for P, pi' may not exist for P' if reducible). Restrict to perturbations preserving irreducibility.
- Step 1: The 1/gap(P) factor can be large for slowly mixing chains. This is fundamental, not an artifact. The Lipschitz constant genuinely grows as mixing slows.
- Step 2: The entropy continuity bound requires delta < 1 (i.e., the distributions are not too far apart). For large perturbations, MI can change by O(ln(|Omega|)) in a single step. The Lipschitz bound is only useful in the regime delta << 1.
- Step 2: The bound involves ln(|Omega|-1), which is the correct scaling for worst-case entropy perturbation. For the specific rho functional, the bound may be tighter because rho = 0 at both I = 0 and I = H(B), so perturbations near these boundaries produce smaller changes. The numerical verification will test whether the proven L is tight.
- Step 3: The composition requires H_pi(B) to be bounded away from zero. If B is nearly deterministic (one state has pi_B ~ 1), then H(B) ~ 0 and the I/H ratio is ill-conditioned. This is a genuine mathematical issue: rho is not Lipschitz uniformly over all P, only over P with H(B) bounded away from zero. The Lipschitz constant L must explicitly depend on a lower bound for H(B), or equivalently on how far P is from having a degenerate marginal on B.

### Approach 2: Direct Differentiation (FALLBACK)

**What:** Instead of decomposing into perturbation-theory + MI-continuity, directly compute the derivative d(rho)/d(P_ij) for each matrix entry and bound the operator norm.

**When to switch:** If the composed bound is too loose (L >> L_numerical for the toy model). Direct differentiation gives a tighter bound because it accounts for cancellations between the three entropy terms.

**Tradeoffs:** More computation but potentially sharper. Requires expressing d(pi)/d(P_ij) explicitly (the sensitivity matrix), which involves the group inverse (I - P + Pi)^{-1}. The resulting L is tighter but less transparent in its dependence on |Omega| and gap(P).

**Key reference:** Cho, Meyer, "Comparison of perturbation bounds for the stationary distribution of a Markov chain," Linear Algebra Appl. 335 (2001) 137-150.

### Anti-Patterns to Avoid

- **Proving existence without explicit constants:** The forbidden proxy (fp-numerics-only) demands a formal bound. Writing "L exists by compactness" or "rho is continuous by composition of continuous functions" is not acceptable. L must be an explicit formula.
  - _Example:_ "Since pi depends continuously on P and MI depends continuously on pi, rho depends continuously on P." This is true but fails the contract: L must be written down.

- **Ignoring the H(B) -> 0 degenerate case:** If pi_B is concentrated on one state, H(B) ~ 0 and rho/H(B) is ill-conditioned. The bound must either assume H(B) >= h_min > 0 or handle this regime separately.
  - _Example:_ Dividing by H(B) without noting this requires H(B) > 0 would introduce an implicit assumption.

- **Mixing up L1 and TV conventions:** The literature uses both ||.||_1 and ||.||_TV = (1/2)||.||_1. A factor-of-2 error propagates through all bounds.
  - _Example:_ Citing a result with TV convention and plugging into a formula with L1 convention (or vice versa) doubles or halves L.

- **Conflating ||P - P'||_inf (operator norm) with entry-wise max:** The sup-norm on rows is ||P||_inf = max_i sum_j |P_ij|, which for the difference of stochastic matrices gives ||P - P'||_inf = max_i sum_j |P_ij - P'_ij| = max_i ||P_i - P'_i||_1. This is the row-sum norm, not max_ij |P_ij - P'_ij|. The perturbation literature sometimes uses max_ij |E_ij| where E = P' - P; this differs by a factor of |Omega|.

## Existing Results to Leverage

**This section is MANDATORY.** Both steps of the proof use textbook results. The value of this phase is the composition with explicit constants, not re-deriving perturbation theory or entropy continuity.

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Stationary dist. perturbation | \|\|pi - pi'\|\|_1 <= (1/gap(P)) * \|\|P - P'\|\|_inf | Cho-Meyer (2001), Thm 3.1; see also Seneta (1993) | Step 1: cite directly |
| Entropy continuity (Fannes type) | \|H(p) - H(q)\| <= (delta/2)*ln(k-1) + h_bin(delta/2) where delta = \|\|p-q\|\|_1, k = alphabet size | Csiszar-Korner (1981/2011) Lemma 2.7; tight form: Audenaert (2007) | Step 2: apply to each entropy term |
| Data processing for L1 | \|\|p_B - q_B\|\|_1 <= \|\|p - q\|\|_1 for marginals | Standard; Schur complement | Step 2: marginal perturbation bound |
| MI decomposition | I(B;M) = H(B) + H(M) - H(B,M) | Standard information theory | Step 2: reduce MI to entropies |
| rho boundary conditions | rho(I=0) = rho(I=H(B)) = 0; rho_max = H(B)/4 at I = H(B)/2 | Draft Section 3.1 | Step 3: bound rho and its derivatives |
| Spectral gap of toy model | gap(P) for the 7-chain model is computable from eigenvalues | composite_self_model.py | Numerical verification |

**Key insight:** Both the perturbation bound and the entropy continuity lemma are single-sentence citations. The phase's contribution is (a) composing them with explicit tracking of constants through rho = I*(1-I/H), and (b) verifying the result numerically against the toy model. Do not waste effort re-proving either ingredient.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Group inverse bound | \|\|(I - P + Pi)^{-1}\|\|_inf <= 1/gap(P) | Meyer (1975); Cho-Meyer (2001) | Ergodic P |
| Condition number for Markov chains | kappa(P) = \|\|pi\|\|_inf * \|\|(I-P+Pi)^{-1}\|\|_inf | Cho-Meyer (2001) | Can be much smaller than 1/gap(P) |
| Ergodicity coefficient bound | \|\|pi - pi'\|\|_1 <= (1/(1-tau(P))) * max_i \|\|P_i - P'_i\|\|_1 | Seneta (1993); Dobrushin (1956) | tau(P) = (1/2)*max_{x,x'}\|\|P_x - P_{x'}\|\|_1; relates to but differs from spectral gap |
| Derivative of entropy | dH/dp_i = -(1 + ln(p_i)) | Standard calculus | For direct differentiation approach |
| Lipschitz constant of x*(1-x) | \|x(1-x) - y(1-y)\| <= \|x-y\| for x,y in [0,1] | Elementary: derivative 1-2x bounded by 1 | For Step 3 product rule |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Comparison of perturbation bounds for stationary distributions | Cho, Meyer | 2001 | Primary Step 1 reference | Theorem 3.1: the bound and its sharpness |
| Sensitivity of the Stationary Distribution | Seneta | 1993 | Alternative Step 1 reference via ergodicity coefficient | Complements spectral gap bound with mixing-based bound |
| Perturbation theory and finite Markov chains | Schweitzer | 1968 | Historical reference, first perturbation bound | Foundational approach |
| Information Theory: Coding Theorems | Csiszar, Korner | 1981/2011 | Step 2: entropy continuity lemma | Lemma 2.7: tight entropy continuity |
| Elements of Information Theory | Cover, Thomas | 2006 | Step 2: standard reference for MI properties | Chapter 2: entropy continuity, Fano inequality |
| A continuity property of the entropy | Audenaert | 2007 | Tight version of Fannes inequality | Optimal constant in entropy continuity |
| Sharp entrywise perturbation bounds for Markov chains | Ipsen, Selee | 2011 | Entrywise (not just norm) perturbation bounds | If sharper bounds needed |
| A Statistical Measure of Complexity | Lopez-Ruiz, Mancini, Calbet | 1995 | rho belongs to LMC family | Cite for pedigree; note our rho is bivariate LMC |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | numpy.linalg | Eigenvalue computation (spectral gap), matrix operations | Already used in composite_self_model.py |
| SciPy | scipy.linalg | Eigenvalue solver for spectral gap | Numerically stable eigenvalue computation |
| Python 3 | standard | Implementation language | Already used in toy model |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| matplotlib | Plot L_numerical vs L_proven across perturbation magnitudes | Validation visualization |
| SymPy | Symbolic verification of Lipschitz constant formula | Optional: verify algebra in Step 3 |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| Computing spectral gap numerically | Analytical bound for specific chain | More precise but chain-specific |
| Random perturbation testing | Adversarial perturbation construction | Random is faster; adversarial tests sharpness of bound |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Spectral gap of 16x16 matrix | < 1 ms | None | numpy.linalg.eig |
| 100+ random perturbations of toy model | < 1 second total | None | Vectorize perturbation generation |
| Compute rho for each perturbed kernel | < 1 second total | None | Already implemented in composite_self_model.py |
| L_numerical = max |rho(P)-rho(P')| / \|\|P-P'\|\|_inf | < 1 second | None | Simple max over perturbation samples |

**Installation / Setup:**
```bash
# All required packages already available
pip install numpy scipy matplotlib sympy
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| L_numerical <= L_proven | Proven bound is valid | Compute L_numerical from 100+ random perturbations; compare to formula | L_numerical strictly below L_proven for all perturbation sizes |
| L_proven finite for fast-mixing chains | Non-vacuousness | Compute L for toy model (gap > 0) | L = finite, reasonable value |
| rho(P) = rho(P) for zero perturbation | Consistency | Evaluate bound at P' = P | Bound gives 0, as required |
| Dimensional analysis | Units consistency | Check [L] = [rho] / [norm of P] = nats / 1 = nats | L has units of nats (since rho is in nats and \|\|P-P'\|\|_inf is dimensionless) |
| Boundary behavior | rho -> 0 at I=0 and I=H(B) | Perturb near degenerate kernels (independent B,M or M=f(B)) | |rho - rho'| should be small near boundaries (quadratic vanishing) |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Large spectral gap | gap(P) -> 1 (rapidly mixing) | L ~ O(ln(\|Omega\|)) -- finite, non-vacuous | The bound formula |
| Small spectral gap | gap(P) -> 0 (nearly reducible) | L -> infinity | Fundamental: nearly reducible chains have sensitive stationary distributions |
| Independent B, M | I(B;M) = 0, rho = 0 | |rho(P) - rho(P')| = |rho(P')| which is small for small perturbations | Continuity of MI near zero |
| Perfect tracking | I(B;M) = H(B), rho = 0 | Same as above; rho vanishes at right boundary | Quadratic vanishing of rho at I = H |
| Uniform stationary dist | pi = (1/n, ..., 1/n) | H(B) = ln(\|B\|), maximum entropy; rho most sensitive near I = H/2 | Maximum sensitivity regime |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| L_numerical for 7-chain observer | 1000 random perturbations with \|\|E\|\|_inf in {0.001, 0.01, 0.1}; compute max ratio | L_numerical <= L_proven | L_proven from formula |
| Scaling test: L vs gap | Sweep gap by varying inter-basin transition rate in toy model | L_numerical ~ 1/gap (linear scaling) | Matches theoretical 1/gap dependence |
| Scaling test: L vs \|Omega\| | Construct chains with \|B\|=\|M\|=k for k=2,3,4,5,6; measure L | L_numerical ~ ln(\|Omega\|) (logarithmic scaling) | Matches theoretical ln(\|Omega\|) dependence |
| Convergence of L_numerical | Increase number of perturbation samples from 100 to 10000 | L_numerical converges (not increasing without bound) | Stable value |

### Red Flags During Computation

- If L_numerical > L_proven for ANY perturbation, the proof has an error. This is a hard failure -- investigate immediately. Most likely cause: a factor-of-2 error in the TV/L1 convention, or a missing factor of |Omega| in the entropy bound.
- If L_proven >> L_numerical by more than a factor of |Omega|, the bound is vacuous (technically true but useless). This triggers the fallback to direct differentiation (Approach 2) for a tighter L.
- If the spectral gap of the perturbed chain changes sign (gap(P') = 0), the perturbed chain is reducible and the bound does not apply. Discard that perturbation sample. If this happens frequently, restrict the perturbation class.
- If rho is not monotonically approaching 0 as perturbation magnitude decreases, there is a bug in the computation (rho is continuous, so |rho(P) - rho(P')| -> 0 as ||P - P'|| -> 0).

## Common Pitfalls

### Pitfall 1: L1 vs Total Variation Convention

**What goes wrong:** Literature uses both ||p-q||_1 = sum |p_i - q_i| and ||p-q||_TV = (1/2)*sum |p_i - q_i|. Mixing conventions introduces a factor of 2 that propagates through all bounds and can cause L_numerical > L_proven (false failure) or L_proven that is 2x too loose.

**Why it happens:** Probabilists prefer TV; information theorists prefer L1 or variational distance (which can mean either). No universal convention exists.

**How to avoid:** State the convention once (we use L1 = sum |p_i - q_i|) and convert every cited result to L1 before using it. The Fannes bound in TV form uses delta = ||p-q||_TV; convert to delta = ||p-q||_1 / 2 before applying.

**Warning signs:** A factor of 2 discrepancy between L_proven and L_numerical.

**Recovery:** Check all cited bounds for their convention and insert conversion factors.

### Pitfall 2: H(B) Near Zero

**What goes wrong:** The ratio I(B;M)/H(B) appears in rho. When H(B) -> 0 (degenerate B marginal), this ratio is ill-conditioned. The Lipschitz constant L formally diverges.

**Why it happens:** If B is nearly deterministic under pi, H(B) is small, and small perturbations to pi can cause large relative changes in I/H.

**How to avoid:** State the Lipschitz bound conditional on H_pi(B) >= h_min > 0. The Lipschitz constant depends on 1/h_min. For the toy model, H(B) = 1.386 nats (uniform over 4 states), so h_min is not an issue.

**Warning signs:** L_proven contains a 1/H(B) factor that becomes large.

**Recovery:** This is not a bug but a genuine mathematical feature. Report L as depending on h_min = min(H_pi(B), H_pi'(B)), noting that the bound degrades gracefully as H(B) -> 0 (where rho -> 0 anyway, so the bound becomes vacuous only where rho is already trivially zero).

### Pitfall 3: Perturbation Destroying Irreducibility

**What goes wrong:** The perturbation P' = P + E might not be a valid stochastic matrix (rows don't sum to 1) or might not be irreducible (stationary distribution may not be unique).

**Why it happens:** Random perturbations E with ||E||_inf small will keep rows summing to 1 only if the perturbation is constrained to lie in the tangent space of stochastic matrices (each row sums to 0). Irreducibility can be broken by setting some entries to exactly 0.

**How to avoid:** (a) Generate perturbations as: E = random matrix with row sums 0, scaled to ||E||_inf = epsilon; P' = P + E; clip to ensure non-negative entries; renormalize rows. (b) Check that P' is irreducible (all eigenvalues of P' except 1 have |lambda| < 1). (c) The Lipschitz bound applies to the open set of irreducible stochastic matrices; no claim is made at the boundary.

**Warning signs:** numpy.linalg.eig returns a second eigenvalue with |lambda_2| = 1 for P'.

**Recovery:** Discard non-irreducible P' samples. In the proof, state the domain of the Lipschitz bound as the set of irreducible stochastic matrices with gap >= gap_min.

### Pitfall 4: Confusing Operator Norm vs Entry-wise Norm

**What goes wrong:** ||P - P'||_inf = max_i sum_j |P_ij - P'_ij| (row-sum norm, i.e., the operator norm for the sup-norm on vectors). This is NOT max_ij |P_ij - P'_ij| (entry-wise max). The two differ by a factor of up to |Omega|.

**Why it happens:** Both are natural norms on matrices and both are called "infinity norm" in different communities.

**How to avoid:** State explicitly: ||P||_inf = max_i ||P_i||_1 = max_i sum_j |P_ij| (the matrix norm induced by the vector infinity norm). For stochastic matrices P, P': ||P - P'||_inf = max_i ||P_i - P'_i||_1. This is the convention in CONVENTIONS.md.

**Warning signs:** If L_numerical computed with entry-wise max is |Omega| times larger than expected.

**Recovery:** Recompute with the correct norm definition.

## Level of Rigor

**Required for this phase:** Physicist's proof with explicit constants

**Justification:** The contract requires "proven with no hand-waving steps" and "L characterized explicitly." Each step cites a precise theorem. Constants are tracked. However, we are not writing a pure mathematics paper: we can cite Cho-Meyer's theorem rather than re-proving it, and we can use standard calculus inequalities without full epsilon-delta proofs.

**What this means concretely:**

- Step 1 cites the specific perturbation theorem (Cho-Meyer Theorem 3.1 or equivalent) with its precise statement
- Step 2 cites the entropy continuity lemma (Csiszar-Korner Lemma 2.7 or Audenaert's tight form) with its precise statement
- Step 3 gives complete algebra showing how L depends on |Omega|, gap(P), and H(B)
- Every inequality has a stated regime of validity (irreducible P, H(B) > 0, perturbation preserving irreducibility)
- The final L formula is an explicit expression, not "there exists an L"
- Numerical verification checks L_numerical <= L_proven for 100+ perturbations

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Schweitzer (1968): first perturbation bound, not tight | Cho-Meyer (2001): tight condition number | 2001 | Sharper bounds with explicit condition number |
| Fannes (1973): entropy continuity for quantum states | Audenaert (2007): tight classical/quantum Fannes inequality | 2007 | Optimal constant in entropy continuity; the Fannes bound is now tight |
| Entry-wise perturbation bounds | Row-norm perturbation bounds (Ipsen-Selee 2011) | 2011 | Sharper entry-wise control if needed |

**Superseded approaches to avoid:**

- **Dobrushin's coefficient alone:** While Dobrushin's ergodicity coefficient bounds perturbation sensitivity, it does not directly give the spectral gap dependence. For reversible chains (our case), the spectral gap is more natural and gives tighter bounds. Use spectral gap, not just ergodicity coefficient.
- **Generic "continuity by compactness" arguments:** These prove existence of L but give no value. Unacceptable per the contract.

## Open Questions

1. **Tightness of the composed bound**
   - What we know: The composed bound L = O(ln(|Omega|)/gap(P)) uses worst-case estimates at each step. For the specific rho functional, the bound may be much tighter because rho vanishes at both boundaries of the I range.
   - What's unclear: Whether the 1/gap(P) factor is necessary or whether rho has better stability than the raw stationary distribution. The rho functional might benefit from cancellation (perturbations that increase I also change H, and the I*(1-I/H) form could partially cancel these effects).
   - Impact on this phase: Determines whether L_proven is within O(1) of L_numerical or is loose by a factor of |Omega|.
   - Recommendation: Prove the composed bound first (guaranteed to work). If L_proven >> L_numerical, investigate direct differentiation (Approach 2) for tighter constants. Report both L_proven and L_numerical in the deliverable.

2. **Dependence on H(B) lower bound**
   - What we know: The ratio I/H in rho requires H(B) > 0. Near-degenerate B marginals make the bound blow up.
   - What's unclear: Whether to state L as a function of gap(P) and |Omega| alone (absorbing H(B) dependence into the gap, since small H(B) typically implies small gap), or to keep H(B) as an independent parameter.
   - Impact on this phase: Affects the exact form of L(|Omega|, spectral_gap) required by the contract.
   - Recommendation: State L = C * ln(|Omega|) / (gap(P) * h_min) where h_min = min(H_pi(B), epsilon_0) for some minimum entropy threshold. Then note that for the toy model h_min = ln(4), gap = [computed], giving L = [explicit number].

3. **Extension to continuous-time generators**
   - What we know: The draft uses CTMC generators Q. Perturbation theory for stationary distributions of CTMCs is analogous but uses ||Q - Q'||_inf and the spectral gap of Q (negative of the second-largest real part of eigenvalues).
   - What's unclear: Whether the proof should be stated for discrete-time P or continuous-time Q.
   - Impact on this phase: The toy model uses discrete-time P. The framework uses continuous-time Q.
   - Recommendation: Prove for discrete-time P (matching the toy model and the contractual ||P - P'||_inf notation). Note that the CTMC version follows by uniformization with the same bound structure.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Composed bound (3-step) | L_proven >> L_numerical (too loose) | Direct differentiation (Approach 2) | Low: same framework, just compute d(rho)/d(P_ij) directly |
| Spectral gap bound for Step 1 | Spectral gap not the right parameter | Ergodicity coefficient (Seneta/Dobrushin) bound | Low: different sensitivity parameter, same structure |
| Uniform Lipschitz over all P | H(B) -> 0 degenerate case | Restrict to P with gap >= gap_min, H(B) >= h_min | None: this is the expected outcome |
| Audenaert entropy bound for Step 2 | Need tighter MI-specific bound | Direct MI continuity via Pinsker + data processing | Low: different information-theoretic inequality |

**Decision criteria:** If L_proven > 10 * L_numerical for the toy model, the bound is too loose and Approach 2 should be tried. If L_proven < 3 * L_numerical, the bound is acceptably tight (within a small constant factor is fine for a first proof).

## Caveats and Alternatives

**Self-critique answers:**

1. **What assumption might be wrong?** The assumption that the 3-step composed bound gives a non-vacuous L for realistic parameters. If the product of the three Lipschitz constants (perturbation bound * MI continuity * rho derivative) is much larger than the true Lipschitz constant of rho, the bound exists but is useless. Numerical verification is essential to check this.

2. **What alternative approach was dismissed too quickly?** Direct computation of d(rho)/d(P_ij) via the chain rule through the stationary distribution. This avoids the looseness of composing three separate worst-case bounds. For a 16x16 matrix, the gradient has 16^2 = 256 components and is straightforward to compute numerically. The analytical formula involves the group inverse (I - P + Pi)^{-1}, which is a 16x16 matrix -- tractable. This approach would give an exact local Lipschitz constant. Dismissed as the fallback (Approach 2) rather than the primary approach because the 3-step method gives cleaner dependence on |Omega| and gap(P).

3. **What limitation am I understating?** The requirement that H(B) be bounded away from zero. For kernels where B is nearly deterministic, the Lipschitz constant formally diverges. This is real: rho = I*(1-I/H) has a singularity as H -> 0 with I/H fixed. However, rho itself goes to zero in this limit (since I <= H -> 0), so the bound becomes vacuous only where rho is already trivially small. The correct statement is: rho is locally Lipschitz on the open set of irreducible kernels, with L depending on H(B).

4. **Is there a simpler method?** For the toy model specifically, one could simply compute rho for a grid of perturbations and plot |rho(P) - rho(P')| / ||P - P'||. This gives L_numerical directly. But this is exactly what fp-numerics-only forbids: the contract demands a proven bound, not just numerical evidence. The formal proof is unavoidable.

5. **Would a specialist disagree?** An information theorist might note that the MI continuity bound via three separate entropy terms is loose. A tighter bound exists using the mutual information's relationship to KL divergence: I(B;M) = D(p_BM || p_B * p_M), and KL divergence has better continuity properties than entropy. Specifically, if p is close to q in L1, then |D(p||r) - D(q||r)| can be bounded more tightly when r = p_B * p_M is also perturbed consistently with p. This is a valid point -- if the 3-step bound is too loose, this is the direction to tighten it.

## Sources

### Primary (HIGH confidence)

- Cho, G.E., Meyer, C.D. -- "Comparison of perturbation bounds for the stationary distribution of a Markov chain," Linear Algebra Appl. 335 (2001) 137-150 -- Step 1 perturbation bound, condition number for Markov chains
- Seneta, E. -- "Sensitivity of finite Markov chains under perturbation," Statist. Probab. Lett. 17 (1993) 163-168 -- Alternative Step 1 via ergodicity coefficient
- Cover, T.M., Thomas, J.A. -- Elements of Information Theory, 2nd ed., Wiley (2006) -- Chapter 2: entropy properties, continuity, Fano inequality
- Csiszar, I., Korner, J. -- Information Theory: Coding Theorems for Discrete Memoryless Systems, 2nd ed., Cambridge (2011) -- Lemma 2.7: entropy continuity lemma (tight form)

### Secondary (MEDIUM confidence)

- Audenaert, K.M.R. -- "A sharp continuity estimate for the von Neumann entropy," J. Phys. A 40 (2007) 8127-8136 [arXiv:quant-ph/0610146] -- Tight Fannes inequality; optimal constant
- Ipsen, I.C.F., Selee, T.M. -- "Ergodicity coefficients defined by vector norms," SIAM J. Matrix Anal. Appl. 32 (2011) 153-200 -- Entry-wise perturbation bounds
- Schweitzer, P.J. -- "Perturbation theory and finite Markov chains," J. Appl. Probab. 5 (1968) 401-413 -- Historical: first perturbation bound for stationary distributions
- Mitrophanov, A.Yu. -- "Sensitivity and convergence of uniformly ergodic Markov chains," J. Appl. Probab. 42 (2005) 1003-1014 -- Modern perturbation bounds
- Lopez-Ruiz, R., Mancini, H.L., Calbet, X. -- "A statistical measure of complexity," Phys. Lett. A 209 (1995) 321-326 -- LMC complexity family pedigree

### Tertiary (LOW confidence)

- The exact tightness of the composed 3-step bound for the specific rho functional -- not verified in literature. The individual steps are tight, but the composition may be loose. Numerical verification required.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - Both perturbation theory and entropy continuity are textbook material with decades of development
- Standard approaches: HIGH - The 3-step composition is the natural approach; the draft already identifies it
- Computational tools: HIGH - NumPy eigenvalue computation for 16x16 matrices is trivial
- Validation strategies: HIGH - 100+ random perturbations with explicit comparison to proven L is definitive

**Research date:** 2026-03-16
**Valid until:** Indefinite for mathematical results. The perturbation bounds and entropy continuity results are permanent results in linear algebra and information theory.
