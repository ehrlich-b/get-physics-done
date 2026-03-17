# Mathematical Soundness Review -- Theorem A

**Manuscript:** papers/paper1-theorem-a/main.tex
**SHA256:** fc8b55325e52c5d1558160d8c016f9efd6d23961b8733cf2311244672d7d6ba3
**Reviewer pass:** 2 (Mathematical Soundness)
**Date:** 2026-03-16

---

## Equations Checked

### EQ-1: Experiential density definition (main.tex eq 1, line 86)

    rho(p) = I(B;M) * (1 - I(B;M)/H(B))

**Checks performed:**

- **Non-negativity:** I(B;M) >= 0 always. The factor (1 - I/H) >= 0 when I <= H(B), which holds by definition (mutual information never exceeds marginal entropy). Therefore rho >= 0. CORRECT.
- **Zeros:** rho = 0 when I = 0 (no self-modeling) or I = H(B) (degenerate copy). Both are physically motivated boundary conditions. CORRECT.
- **Maximum:** rho = I(1 - I/H) is a downward parabola in I with maximum at I = H(B)/2, yielding rho_max = H(B)/4. This matches the claimed bound rho_max = H(B)/4 (A2, line 189). CORRECT.
- **Units:** I and H are in nats (dimensionless information units). rho is therefore dimensionless (nats). Combined with the time integral, mu has units nat-seconds. CORRECT.
- **Consistency:** The definition is identically stated in main.tex (eq 1), theorem-a-proof.tex (line 64), theorem-a-lemmas.tex (line 61), and CONVENTIONS.md. No discrepancy across files.

**Verdict: SOUND.**

---

### EQ-2: Metropolis generator (main.tex eq 3, line 161)

    Q_eps(x,y) = r(x,y) * exp(-[E(y)-E(x)]^+ / eps),  x != y

**Checks performed:**

- **Detailed balance:** For the Gibbs measure pi(x) proportional to exp(-E(x)/eps), we need pi(x)Q(x,y) = pi(y)Q(y,x). LHS = r(x,y)*exp(-E(x)/eps)*exp(-[E(y)-E(x)]^+/eps). For E(y) > E(x): LHS = r(x,y)*exp(-E(y)/eps). RHS = r(y,x)*exp(-E(y)/eps)*exp(0) = r(y,x)*exp(-E(y)/eps). Since r(x,y) = r(y,x), LHS = RHS. For E(y) < E(x): symmetrically correct. CORRECT.
- **Irreducibility:** r(x,y) > 0 for all x != y ensures all transition rates are positive. CORRECT.
- **Row sum:** Q(x,x) = -sum_{y!=x} Q(x,y) ensures zero row sums, consistent with probabilist generator convention dp/dt = pQ. CORRECT.

**Verdict: SOUND.**

---

### EQ-3: Mean exit time (main.tex eq 6, line 322; lemmas eq 5)

    E_x[tau_{B_stable^c}] = K_s * exp(Delta_s / eps) * (1 + delta_2)

with |delta_2| <= C_2 * exp(-c_2/eps), c_2 >= Delta_s - Delta_b.

**Checks performed:**

- **Source:** BEGK Theorem 1.2 (Comm. Math. Phys. 228, 2002) gives sharp capacity asymptotics for mean exit times of reversible Markov chains. The Arrhenius form K_s * exp(Delta_s/eps) is the standard result for Metropolis dynamics with barrier height Delta_s. This is a well-established result in metastability theory. CORRECT citation.
- **Error rate c_2 >= Delta_s - Delta_b:** The sub-leading correction to the capacity comes from the next-to-leading saddle in the cycle hierarchy. The bound c_2 >= Delta_s - Delta_b is the standard estimate when the sub-leading barrier is at height Delta_b. PLAUSIBLE; consistent with BdH15 Theorem 7.8.
- **Prefactor K_s = O(1):** For finite state spaces with Metropolis rates, K_s is a rational function of rate prefactors and energies. This is standard (BdH15 Theorem 7.8). CORRECT.

**Verdict: SOUND.** The claim rests on a well-established theorem applied to a finite-state reversible chain, which is squarely within the theorem's domain of applicability.

---

### EQ-4: Theorem A main bound (main.tex eq 8, line 217-223)

    mu_BB / mu_stable <= C * exp(-(Delta_s - Delta_b - alpha)/eps) * (1 + delta(eps))

with C = (rho_max / c) * (K_b / K_s^2), |delta| <= C' * exp(-gamma/eps), gamma = alpha/2.

**Checks performed:**

- **Exponent sign and magnitude:** Since 0 < alpha < Delta_s - Delta_b, the exponent Delta_s - Delta_b - alpha > 0, so the exponential is between 0 and 1 and goes to 0 as eps -> 0. CORRECT.
- **Prefactor dimensions:** rho_max/c is dimensionless (nats/nats). K_b/K_s^2 is dimensionless (both K_s and K_b are O(1) prefactors with the same dimensional structure). C is dimensionless as required for a bound on a ratio. CORRECT.
- **Derivation trace (Step 7, ergodic-limit route):** The ratio bound follows from dividing eq (5c) (BB upper bound) by the stable lower bound:

      E[mu_BB] / E[mu_stable]
      <= [rho_max * (K_b/K_s) * exp((Db-alpha)/eps)] / [c * K_s * exp(Ds/eps)]
      = (rho_max/c) * (K_b/K_s^2) * exp((Db - alpha - Ds)/eps)
      = C * exp(-(Ds - Db - alpha)/eps)

  The algebra is straightforward. CORRECT.

- **Error correction factor:** The product (1+delta_5)/((1-delta_2)(1-delta_4')(1-eta)) with all delta_i = O(exp(-c_i/eps)) gives 1 + O(exp(-min(c_i)/eps)). The minimum rate is alpha/2 from the choice eta = exp(-alpha/(2eps)). CORRECT.

**Verdict: SOUND.** The core bound follows from clean division of upper and lower bounds with correct error propagation.

---

### EQ-5: Excursion probability (main.tex eq 14, line 472-476; proof eq exc-prob)

    P(tau_{B_stable^c} < T_eps) <= (T_eps / E[tau]) * (1 + o(1)) = exp(-alpha/eps) / K_s * (1 + o(1))

**Checks performed:**

- **Exponential law usage:** For X ~ Exp(1), P(X < s) = 1 - exp(-s) ~ s for small s. With s = T_eps/E[tau] = exp(-alpha/eps)/K_s -> 0, the approximation P ~ s is valid asymptotically. CORRECT.
- **Substitution:** T_eps/E[tau] = exp((Ds-alpha)/eps) / (K_s * exp(Ds/eps) * (1+delta_2)) = exp(-alpha/eps) / (K_s * (1+delta_2)). CORRECT.
- **Direction of bound:** This is an upper bound on the exit probability. The approximation 1-exp(-s) <= s holds for all s >= 0 (since exp(-s) >= 1-s). So the bound P(exit) <= s = exp(-alpha/eps)/K_s * (1+o(1)) is actually a slight overestimate for finite eps, which is the correct direction for an upper bound. CORRECT.

**Verdict: SOUND.**

---

### EQ-6: Error rate gamma = alpha/2 (main.tex eq 10, line 232; proof eq gamma-final)

    gamma = min(c_2, Ds - alpha, c_5, alpha/2) = alpha/2

**Checks performed:**

- **Ordering verification:**
  - c_2 >= Ds - Db > alpha (since alpha < Ds - Db).
  - Ds - alpha > Db > 0 (since alpha < Ds - Db implies Ds - alpha > Db > 0, actually Ds - alpha > Ds - (Ds-Db) = Db > 0).
  - c_5 >= Ds - Db > alpha > alpha/2.
  - alpha/2 < alpha < Ds - Db <= c_2, c_5.
  - Is alpha/2 < Ds - alpha? We need alpha/2 < Ds - alpha, i.e., 3alpha/2 < Ds. Since alpha < Ds - Db < Ds, we have 3alpha/2 < 3Ds/2, which is not sufficient. But actually we need alpha < 2(Ds - alpha)/3... wait. Let me re-examine.

  The claim in the proof (main.tex line 738) states: "alpha/2 < alpha < Ds - Db <= Ds - alpha". The last inequality Ds - Db <= Ds - alpha holds iff alpha <= Db. But alpha can be as large as Ds - Db, which is larger than Db when Ds > 2*Db.

  **FINDING: The chain of inequalities "Ds - Db <= Ds - alpha" on line 738 (main.tex) and line 607 (proof) is INCORRECT when alpha > Db.**

  For the three-state example: Ds = 3, Db = 1, alpha can range in (0, 2). When alpha = 1.5, Ds - Db = 2 but Ds - alpha = 1.5, so Ds - Db > Ds - alpha. The inequality is reversed.

  However, this does NOT affect the conclusion gamma = alpha/2, because all that is needed is that alpha/2 is the minimum of the four rates. Let me re-verify:
  - c_2 >= Ds - Db >= alpha/2 (since alpha < Ds - Db implies alpha/2 < Ds - Db).
  - Ds - alpha > 0 and alpha/2 < alpha, but is alpha/2 < Ds - alpha? This requires 3alpha/2 < Ds, which holds when alpha < 2Ds/3. Since alpha < Ds - Db < Ds, and Ds - Db < 2Ds/3 iff Db > Ds/3, this is NOT guaranteed. Example: Ds = 3, Db = 0.5, alpha = 2.4: then alpha/2 = 1.2, Ds - alpha = 0.6. So Ds - alpha < alpha/2.
  - c_5 >= Ds - Db > alpha/2 (same reasoning as c_2).

  In this edge case (Db small, alpha close to Ds - Db), the minimum would actually be Ds - alpha, not alpha/2. So gamma = min(c_2, Ds - alpha, c_5, alpha/2) = min(alpha/2, Ds - alpha), not necessarily alpha/2.

  **Severity assessment:** In the regime alpha > 2Ds/3, we have Ds - alpha < Ds/3, and alpha/2 > Ds/3, so gamma = Ds - alpha < alpha/2. This means the stated gamma = alpha/2 is an OVERSTATEMENT of the error rate in this regime. The error decays FASTER than claimed (since Ds - alpha < alpha/2 means exp(-(Ds-alpha)/eps) < exp(-alpha/(2eps))), so the claimed error bound exp(-gamma/eps) = exp(-alpha/(2eps)) is actually LARGER than the true error bound exp(-(Ds-alpha)/eps).

  Wait -- a larger gamma means faster decay, so stating gamma = alpha/2 when the true minimum is Ds - alpha < alpha/2 means the CLAIMED error is LARGER (slower decay) than the ACTUAL error. An upper bound on the error that overstates the error is still a valid bound. The error term is |delta| <= C' * exp(-gamma/eps), and if the true gamma_true = Ds - alpha > gamma_claimed = alpha/2... no, I had it backwards. If Ds - alpha < alpha/2, then gamma_true = Ds - alpha < alpha/2. The claim says gamma = alpha/2, meaning |delta| <= C' * exp(-alpha/(2eps)). But the actual minimum rate is Ds - alpha < alpha/2, meaning the error could be as large as C' * exp(-(Ds-alpha)/eps), which is LARGER than C' * exp(-alpha/(2eps)) (since Ds - alpha < alpha/2 means the exponential decays slower).

  Actually hold on. exp(-a/eps) for smaller a gives a LARGER value, i.e., SLOWER decay. If gamma_true = Ds - alpha < alpha/2, then exp(-gamma_true/eps) > exp(-alpha/(2eps)). The claim |delta| <= C' * exp(-alpha/(2eps)) would then be TIGHTER than what the proof actually establishes.

  **This is a genuine error in the error rate formula.** The correct statement is gamma = min(alpha/2, Ds - alpha, Ds - Db). When alpha > 2(Ds - alpha), i.e., alpha > 2Ds/3, we get Ds - alpha < alpha/2 and gamma should be Ds - alpha, not alpha/2.

  **Mitigation:** The constraint alpha in (0, Ds - Db) means alpha < Ds - Db. We need to check when Ds - alpha < alpha/2, i.e., when 2Ds < 3alpha, i.e., alpha > 2Ds/3. Since alpha < Ds - Db, this requires Ds - Db > 2Ds/3, i.e., Db < Ds/3. So the error only arises when Db < Ds/3 AND alpha is close to Ds - Db.

  For the three-state chain benchmark (Ds = 3, Db = 1), Db = Ds/3 exactly, so the threshold is alpha = 2Ds/3 = 2, but alpha < Ds - Db = 2, so alpha/2 < 1 = Ds - alpha for all valid alpha. The error does not arise in this specific benchmark.

  For general systems with Db < Ds/3, the gamma = alpha/2 claim is incorrect near the upper end of the alpha range. The correct formula is gamma = min(alpha/2, Ds - alpha).

**Verdict: MINOR ERROR in the proof of the error rate.** The stated chain of inequalities is incorrect, and gamma = alpha/2 is only correct when Ds - alpha >= alpha/2, i.e., alpha <= 2Ds/3. For Db < Ds/3 and alpha near Ds - Db, the correct error rate is gamma = min(alpha/2, Ds - alpha). This does not affect the leading-order exponential suppression but makes the stated error decay rate wrong in a corner of parameter space.

---

### EQ-7: Concentration inequality (main.tex eq 13, lemmas eq exp-concentration)

    P(|tau/E[tau] - 1| > eta) <= 2*exp(-eta/2)

**Checks performed:**

- **Source check:** For X ~ Exp(1), P(X > 1+eta) = exp(-(1+eta)) and P(X < 1-eta) = 1-exp(-(1-eta)) for eta < 1. Their sum is exp(-(1+eta)) + 1 - exp(-(1-eta)). The claimed bound 2*exp(-eta/2) is an approximation.
  - At eta = 0: LHS = exp(-1) + 1 - exp(-1) = 1, RHS = 2. Valid.
  - At eta = 0.5: LHS = exp(-1.5) + 1 - exp(-0.5) = 0.223 + 1 - 0.607 = 0.616, RHS = 2*exp(-0.25) = 1.558. Valid.
  - At eta = 1: LHS = exp(-2) + 1 - 1 = 0.135, RHS = 2*exp(-0.5) = 1.213. Valid.

  The bound holds but is loose. For the application, eta is taken to be exp(-alpha/(2eps)) which goes to 0, so the bound in this regime is fine. The looseness does not matter since only the exponential rate matters.

- **Applicability:** This is used with the BEGK exponential law, which gives distributional convergence to Exp(1) as eps -> 0. For finite eps, there are corrections, but the concentration bound is asymptotically valid. CORRECT.

**Verdict: SOUND.** The bound is valid (though not tight), and the looseness does not propagate to the main result.

---

## Derivation Integrity

### Step-by-step chain: L1 -> (L2, L3) -> (L4, L5) -> L6 -> L7

**L1 -> L2:** Basin partition feeds communication height Delta_s into BEGK. Exact-to-exact transfer. NO GAP.

**L1 -> L3:** Basin partition feeds B_stable as subset for killed chain. Exact-to-exact transfer. NO GAP.

**L2 -> L4:** Mean exit time (expectation) feeds into lower bound on mu_stable. The type conversion from expectation to per-trajectory bound uses the Lipschitz continuity of rho plus QSD convergence (from L3). The key integration bound:

    mu_stable >= integral_{t_0}^{T_min} [rho(nu_QSD) - L_rho * C_3 * exp(-gamma_D * t)] dt
             >= c * (T_min - t_0) - L_rho * C_3 / gamma_D

is correct. The integral of L_rho * C_3 * exp(-gamma_D * t) from t_0 to T_min is bounded by L_rho * C_3 / gamma_D (integrating from t_0 to infinity). CORRECT.

**L3 -> L4:** QSD convergence gives the rate at which rho(p_t) approaches rho(nu_QSD). The Lipschitz bound |rho(p) - rho(q)| <= L_rho * ||p-q||_TV is claimed with L_rho = O(H(B)). For rho = I(B;M)*(1 - I(B;M)/H(B)), the Lipschitz constant with respect to TV distance on the joint distribution over B x M is bounded: since I(B;M) is a bounded continuous function of the distribution and H(B) is fixed, the Lipschitz constant is finite for finite state spaces. PLAUSIBLE (not proven in the paper, but standard for smooth functions of distributions on finite spaces).

**L2 -> L5:** Exit time gives excursion probability via exponential law. The bound P(exit) <= T_eps/E[tau] uses 1-exp(-s) <= s, which is exact. Then the BB occupation during one excursion uses BEGK for the B_BB exit time. The product structure (P(exit) * E[BB time | visit]) for the expected BB occupation is valid because the exit event and the subsequent BB visit are conditionally independent given exit. CORRECT.

**IMPORTANT SUBTLETY in L5:** The proof bounds the EXPECTED BB measure but the theorem states a HIGH-PROBABILITY bound. The conversion relies on the case analysis in Step 6: on event A1 (no exit), mu_BB = 0 trivially; on event A2 (exit), the whole event is absorbed into the failure probability. This is logically valid -- the bound holds deterministically on A1, and A2 has probability within the failure budget. NO GAP.

**L6 (Case analysis):** The central structural insight. On A1 = {tau > T_eps}: mu_BB = 0, bound trivially satisfied. On A2 = {tau <= T_eps}: P(A2) = O(exp(-alpha/eps)) <= O(exp(-alpha/(2eps))) = failure budget. This is clean and correct. The probability comparison alpha/eps > alpha/(2eps) for eps > 0 is trivial. CORRECT.

**L7 (Assembly):** On A1, the ratio is 0 and the right-hand side of the bound is positive, so the inequality holds. The error term delta(eps) is the composition of all sub-error terms, with rate gamma = alpha/2 (subject to the minor correction noted in EQ-6). CORRECT modulo the gamma issue.

### Verdict on derivation chain: SOUND with one minor correction needed.

---

## Limiting Cases

### alpha -> 0 (observation time approaches mean exit time)

- T_eps -> exp(Ds/eps) = E[tau] (up to K_s and delta_2). P(exit) -> O(1), so the high-probability regime breaks down as expected.
- The bound becomes C * exp(-(Ds-Db)/eps), which is the ergodic ratio. For p = 0.5 in the three-state chain, C = 0.25 matches exactly.
- Remark 1 (line 239-246) correctly identifies this limit. CORRECT.

### alpha -> Ds - Db (suppression exponent vanishes)

- The main exponent Ds - Db - alpha -> 0. The bound becomes C * (1 + delta), giving no exponential suppression.
- T_eps = exp(Db/eps), which is the mean exit time from B_BB. The observation window is too short relative to B_stable's stability to provide suppression.
- Remark 1 correctly identifies this. CORRECT.

### eps -> 0 (low-noise limit)

- exp(-(Ds-Db-alpha)/eps) -> 0 exponentially. The ratio vanishes. CORRECT.
- P(A2) = O(exp(-alpha/eps)) -> 0. The failure probability vanishes. CORRECT.
- All error terms delta_i = O(exp(-c_i/eps)) -> 0. The correction factor -> 1. CORRECT.
- The BEGK asymptotics and QSD convergence all become sharp. CORRECT.

### Delta_s = Delta_b (no metastability separation)

- The theorem requires Delta_s > Delta_b as a standing assumption (A1). With Delta_s = Delta_b, the exponent is -alpha/eps < 0, which still gives suppression, but c_2 >= Delta_s - Delta_b = 0, violating the error rate positivity requirement.
- The paper correctly excludes this case. CORRECT.

### p -> 0 and p -> 1 (three-state chain routing extremes)

- p -> 0: All exits go to BB. C_exact = (rho_b/rho_s)*(1-p)/p -> infinity. The general bound C = 0.25 is finite, which would be violated in the ergodic limit. The paper acknowledges this (Section 7, p < 0.5 discussion). For alpha > 0, the bound is trivially satisfied on A1 (ratio = 0). CORRECTLY HANDLED.
- p -> 1: No exits go to BB. C_exact -> 0. The bound C = 0.25 is conservative. CORRECT.

### Single-state basins (K_s = K_b = 1)

- For single-state basins, the BEGK formula simplifies: the capacity is just the exit rate, and K = 1. The paper correctly identifies this for the three-state chain. CORRECT.
- The QSD on a single-state basin is the delta measure. rho(delta_s) = rho_s by definition. CORRECT.

---

## Numerical Verification Cross-Check

### Validation script logic (theorem_a_validation.py)

**Check 1 (Ergodic limit):** Compares C_bound = 0.25 with C_exact = (rho_b/rho_s)*(1-0.5)/0.5 = 0.25 for p = 0.5. Fits the exponential slope log(ratio) vs 1/eps. Expected slope = -(Ds-Db) = -2.0. The code logic is correct.

**Check 2 (Monte Carlo):** Simulates the three-state CTMC with Gillespie-style dynamics. I trace through the rate structure:
- Q(s,u) = exp(-3/eps), Q(u,s) = p, Q(u,b) = 1-p, Q(b,u) = exp(-1/eps).
- Start in state 0 (s). Holding time at s is Exp(exp(-3/eps)), i.e., mean = exp(3/eps). This is the exit time from B_stable = {s}. CORRECT.
- At saddle u, transition to s with probability p/(p+(1-p)) = p, to b with probability 1-p. CORRECT.
- The test checks whether the fraction of MC runs violating the bound exceeds the claimed failure probability. CORRECT test structure.

**OBSERVATION:** The MC uses eps = 0.5, which is not particularly small. At eps = 0.5, the asymptotic regime is only marginally reached. The BEGK exponential law is an asymptotic result (eps -> 0), and at eps = 0.5 the distributional convergence to Exp(1) may not be complete. The verification report notes this as an expert verification item. The fact that all 9 tests pass at eps = 0.5 is encouraging but does not constitute a rigorous numerical verification of the asymptotic claim.

**Check 3 (Gamma):** Verifies gamma = alpha/2 for multiple alpha values. The code correctly computes gamma_old = min(Ds-Db, alpha) and gamma_new = alpha/2, showing gamma_new is the honest value. CORRECT.

**Check 4 (p-sensitivity):** Demonstrates that C = 0.25 < C_exact for p < 0.5 in the ergodic limit, and correctly explains why the sub-ergodic theorem is still valid. CORRECT.

**Script deficiency:** The script does not test at smaller eps values (e.g., eps = 0.1, 0.01) where the asymptotic regime would be better approximated. At eps = 0.5, E[tau_exit] = exp(6) ~ 403 time units and T_eps = exp(5) ~ 148 for alpha = 1. These are moderate numbers. At eps = 0.1, E[tau_exit] = exp(30) ~ 10^13, which would be impractical for direct simulation. The choice of eps = 0.5 is a pragmatic compromise, but the paper should acknowledge this limitation.

---

## Self-Consistency

### Cross-file definition consistency

| Quantity | main.tex | proof.tex | lemmas.tex | validation.py | CONVENTIONS.md | Consistent? |
|---|---|---|---|---|---|---|
| rho(p) | I(B;M)(1-I/H) | I(B;M)(1-I/H) | I(B;M)(1-I/H) | rho_s=0.8, rho_b=0.2 | I(B;M)*(1-I(B;M)/H(B)) | YES |
| mu | integral rho dt | integral rho dt | integral rho dt | sum(rho*dt) | integral_0^T rho(p_t) dt | YES |
| mu_stable | integral_0^{min(tau,T)} rho dt | integral_0^{min(tau,T)} rho dt | integral_0^{tau} rho dt | sum over state 0 | -- | SEE NOTE |
| Q_eps | Metropolis, eq 3 | Metropolis, same | Metropolis, same | rates match | probabilist dp/dt=pQ | YES |
| C | (rho_max/c)*(K_b/K_s^2) | same | same | rho_b/rho_s = 0.25 | -- | YES |
| gamma | alpha/2 | alpha/2 | -- | alpha/2 | -- | YES |

**NOTE on mu_stable:** The lemmas file (theorem-a-lemmas.tex, Lemma 4, line 318) defines mu_stable with integral to tau_{B_stable^c} (no min with T_eps), while main.tex and proof.tex use min(tau, T_eps). The verification report (01-VERIFICATION.md) notes this as INFO-level: "lemma is valid as standalone; proof redefines for the theorem context." This is acceptable -- the lemma provides a per-residence bound, and the proof applies it with truncation.

### Inconsistency between lemmas.tex and proof.tex on delta_4

- lemmas.tex (line 325-327): delta_4 = O(exp(-Ds/eps)) with c_4 = Ds. This is the error when T_min ~ tau ~ K_s*exp(Ds/eps).
- proof.tex (line 272-274): delta_4 = O(1/(gamma_D * T_min)). On event A1, T_min = T_eps = exp((Ds-alpha)/eps), giving delta_4 = O(exp(-(Ds-alpha)/eps)), with rate c_4 = Ds - alpha.
- main.tex (line 408): delta_4 = O(1/(gamma_D * T_min)), matching proof.tex.

The difference is because lemmas.tex computes delta_4 for the full-residence case (T_min = tau ~ exp(Ds/eps)), while proof.tex truncates at T_eps on event A1. Both are correct in their respective contexts, but the error rate in the final composition uses c_4 = Ds - alpha (proof), not c_4 = Ds (lemmas). The error table in the proof (line 570, main.tex line 779) correctly lists the rate as Ds - alpha for L4.

### Prefactor C = K_b/K_s^2 vs K_b/K_s

The BB upper bound (L5) contains K_b/K_s from the excursion calculation. The stable lower bound (L4) contains K_s from the mean exit time. Dividing: (K_b/K_s) / K_s = K_b/K_s^2. This is correct. For the three-state chain with K_s = K_b = 1, C = rho_max/c = 0.25. CONSISTENT.

---

## Unchecked Risk Areas

1. **Lipschitz constant of rho:** The proof uses |rho(p) - rho(q)| <= L_rho * ||p - q||_TV with L_rho = O(H(B)). This is claimed but not proven. For finite state spaces, rho is a smooth function of the distribution, and a Lipschitz bound exists. The exact value of L_rho would require computing the gradient of I(B;M)*(1-I(B;M)/H(B)) with respect to the joint distribution. This is a standard but nontrivial calculation that is not provided.

2. **BEGK Theorem 1.4 finite-eps corrections:** The exponential law tau/E[tau] -> Exp(1) is asymptotic. The rate of convergence in distribution is not quantified. At finite eps, there are O(1) corrections to the distributional convergence. The proof uses this asymptotically, which is valid, but the MC validation at eps = 0.5 operates in a regime where finite-eps corrections matter.

3. **Multiple excursions:** The proof bounds at most one excursion to B_BB. For alpha close to 0, the probability of multiple exits from B_stable during [0, T_eps] is non-negligible, and the renewal structure (factor 1/p in the ergodic limit) is not captured. The paper acknowledges this limitation (Section 7.2, point 4). Not a mathematical error but a scope limitation.

4. **QSD spectral gap gamma_D = O(1) claim:** The proof argues this via the Cheeger inequality for the killed chain, citing BdH15 Section 7.2. The argument is that within-basin rates are O(1) because internal barriers are strictly less than Delta_s, and the killing removes the slow inter-basin rates. This is physically correct but depends on the gap between internal barriers and Delta_s. If internal barriers are close to (but strictly less than) Delta_s, gamma_D could be very small (though still O(1) in the asymptotic sense). The bound is valid asymptotically but gamma_D could be exponentially small in a different parameter.

5. **The gamma = alpha/2 overstatement** when Db < Ds/3 and alpha is near Ds - Db (see EQ-6 above). This is a genuine minor error but does not affect the leading-order result.

---

## Findings Summary

| ID | Location | Check | Status | Severity | Impact |
|---|---|---|---|---|---|
| MATH-01 | rho definition (EQ-1) | Non-negativity, zeros, maximum, units | PASS | -- | -- |
| MATH-02 | Metropolis generator (EQ-2) | Detailed balance, irreducibility | PASS | -- | -- |
| MATH-03 | Mean exit time (EQ-3) | BEGK citation, error rate, prefactor | PASS | -- | -- |
| MATH-04 | Main bound (EQ-4) | Exponent sign, prefactor, derivation | PASS | -- | -- |
| MATH-05 | Excursion probability (EQ-5) | Exponential law, substitution | PASS | -- | -- |
| MATH-06 | Error rate gamma (EQ-6) | Ordering of rates | MINOR ERROR | minor | gamma = min(alpha/2, Ds-alpha), not alpha/2 in all cases |
| MATH-07 | Concentration (EQ-7) | Exp(1) tail bound | PASS | -- | -- |
| MATH-08 | Derivation chain L1-L7 | Step-by-step logic | PASS | -- | -- |
| MATH-09 | Limiting cases | 6 limits checked | PASS | -- | -- |
| MATH-10 | Numerical validation | Logic trace | PASS (with note) | suggestion | eps=0.5 is marginal for asymptotics |
| MATH-11 | Self-consistency | Cross-file definitions | PASS (with note) | -- | mu_stable definition differs between lemmas and proof (acceptable) |
| MATH-12 | Lipschitz constant | L_rho = O(H(B)) | UNCHECKED | minor risk | Plausible but not proven |
| MATH-13 | Finite-eps convergence | BEGK exponential law rate | UNCHECKED | low risk | Standard asymptotic result |
| MATH-14 | Multiple excursions | Renewal factor 1/p | ACKNOWLEDGED | scope limitation | Not a bug, but limits the ergodic-limit applicability |

---

## Overall Mathematical Confidence: HIGH

**Justification:** The core mathematical claim -- exponential suppression of the BB/stable ratio -- follows from a clean, well-structured proof that correctly composes established results from metastability theory (BEGK, Freidlin-Wentzell, Champagnat-Villemonais). The proof's case-analysis structure (trivial bound on the dominant event A1, failure-probability absorption for A2) is sound. The one error found (gamma = alpha/2 is not universally correct) is a minor issue in the error-term analysis that does not affect the leading-order exponential suppression. The correct formula gamma = min(alpha/2, Ds - alpha) would be a one-line fix. All limiting cases check out. Dimensional consistency is maintained throughout. The numerical validation is consistent with the analytical claims, though it operates at moderate eps where asymptotic formulas are only approximately valid.

The mathematical framework is internally coherent: the experiential density is well-defined and bounded, the Metropolis generator satisfies the conditions needed for the cited theorems, and the error composition preserves the exponential form. No fatal logical gaps were found in the seven-lemma composition chain.
