# Pass 2: Mathematical Soundness Review

**Manuscript:** papers/paper2-lipschitz/main.tex
**Title:** Lipschitz Stability of the Experiential Density Functional
**Reviewer:** gpd-review-math (Stage 3)
**Date:** 2026-03-16

---

## Overall Mathematical Confidence: HIGH

The proof is a clean three-step composition of standard results (Cho-Meyer, Fannes-Audenaert, multivariate MVT). Each step is invoked correctly within its stated domain of validity. The algebra connecting the steps was traced line by line and is correct. No sign errors, no missing factors, no convention mismatches were found. Two minor edge-case issues are documented below; neither affects any claim made in the paper.

---

## Equations Checked

### EQ-1: Definition of rho (Eq. 1, main.tex line 76; Eq. 2, derivation eq:rho-def)

**Statement:**  rho(P) = I_pi(B;M) * (1 - I_pi(B;M) / H_pi(B))

**Checks performed:**
- Dimensional consistency: I has units [nats], I/H is dimensionless, product is [nats]. PASS.
- Boundary values: I=0 gives rho=0; I=H gives rho=0; maximum at I=H/2 gives rho=H/4. All correct by direct substitution.
- Concavity: d^2(rho)/dI^2 = -2/H < 0, confirming a unique maximum. PASS.

**Verdict: SECURE.**

---

### EQ-2: Cho-Meyer bound (Eq. 6, main.tex line 259; derivation eq:cho-meyer)

**Statement:**  ||pi - pi'||_1 <= ||P - P'||_inf / gap(P)

**Checks performed:**
- The proof sketch derives pi' - pi = pi'(P' - P)(I - P + Pi)^{-1}, then uses submultiplicativity ||vA||_1 <= ||v||_1 * ||A||_inf. This is the correct norm pairing (row-vector L1 times matrix row-sum norm). PASS.
- The bound ||(I - P + Pi)^{-1}||_inf <= 1/gap(P) is cited from Cho-Meyer 2001, Theorem 3.1. This is a standard result in Markov chain perturbation theory (see also Meyer 1975, Seneta 2006). The citation is accurate.
- Norm convention: ||P - P'||_inf = max_i sum_j |P_ij - P'_ij| is consistent with the row-sum norm stated in Definition 2. PASS.
- The key subtlety: The result holds for the absolute spectral gap (1 - |lambda_2|), not the multiplicative gap. The paper defines gap(P) = 1 - |lambda_2(P)| consistently throughout. PASS.

**What I did NOT check:** I did not independently re-derive the bound ||(I - P + Pi)^{-1}||_inf <= 1/gap(P). This is a well-known result and was accepted from the literature.

**Verdict: SECURE** (modulo trusting the cited Cho-Meyer/Meyer result, which is standard).

---

### EQ-3: Fannes-Audenaert entropy continuity (Eq. 9, main.tex line 313; derivation eq:fannes)

**Statement:**  |H(p) - H(q)| <= (delta/2) * ln(k-1) + h_bin(delta/2), where delta = ||p - q||_1

**Checks performed:**
- L1/TV conversion: The standard Audenaert 2007 result uses total variation delta_TV. The paper states delta_TV = delta/2 and substitutes correctly: delta_TV * ln(k-1) + h_bin(delta_TV) becomes (delta/2) * ln(k-1) + h_bin(delta/2). Remark 5 in the derivation makes this explicit. PASS.
- Validity domain: The bound requires delta in (0, 2(1-1/k)]. For k=4 (marginal B or M): delta < 1.5. For k=16 (joint): delta < 1.875. The paper uses delta = eps/gap, which can exceed these limits when gap is small. However, (a) in that regime the bound becomes vacuous (exceeds rho_max), and (b) h_bin is well-defined and bounded by ln(2) for all arguments in [0,1], so the formula produces a finite non-negative value regardless. The Fannes-Audenaert bound technically fails outside its stated domain, but the resulting expression is always an overestimate of the true entropy difference (since H is bounded by ln(k)). This is a MINOR edge case, not an error.
- The tight constant (due to Audenaert 2007, improving the original Fannes 1973 bound) is correctly attributed.

**What I did NOT check:** I did not re-derive the Audenaert tight bound from scratch. This is a published, peer-reviewed result.

**Verdict: SECURE** with a MINOR edge-case note on validity domain at large delta.

---

### EQ-4: Mutual information continuity bound (Eq. 12, main.tex line 374; derivation eq:MI-bound)

**Statement:**  |I_p(B;M) - I_q(B;M)| <= (delta/2)[ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 3 * h_bin(delta/2)

**Checks performed:**
- Triangle inequality decomposition: I = H(B) + H(M) - H(B,M), so |I - I'| <= |H(B) - H'(B)| + |H(M) - H'(M)| + |H(B,M) - H'(B,M)|. This is the standard triangle inequality. PASS.
- Marginal contraction: ||p_B - q_B||_1 <= ||p - q||_1 is used to apply Fannes-Audenaert to marginals at full joint perturbation delta. The proof of marginal contraction (triangle inequality on sums) is correct. PASS.
- Alphabet sizes: H(B) uses k = |B|, H(M) uses k = |M|, H(B,M) uses k = n = |B|*|M|. All correct.
- Coefficient counting: Three Fannes-Audenaert applications produce (delta/2)*[ln(|B|-1) + ln(|M|-1) + ln(n-1)] from the log terms and 3*h_bin(delta/2) from the binary entropy terms. Sum verified. PASS.

**Potential concern -- is the triangle inequality tight here?** No. Since I = H(B) + H(M) - H(B,M), the perturbations dH(B) + dH(M) and dH(B,M) can partially cancel (e.g., if the joint entropy change tracks the marginal entropy changes). This makes the triangle inequality a genuine overestimate, contributing to the observed 450-9500x tightness gap. But as a valid upper bound, it is correct.

**Verdict: SECURE.**

---

### EQ-5: MVT composition (Eq. 17-18, main.tex lines 418-429; derivation eq:mvt)

**Statement:**  |f(I,H) - f(I',H')| <= |I - I'| + |H - H'|, where f(I,H) = I(1 - I/H)

**Checks performed:**
- Partial derivatives:
  - df/dI = d/dI [I - I^2/H] = 1 - 2I/H. Correct.
  - df/dH = d/dH [I - I^2/H] = I^2/H^2. Correct.
- Gradient bounds on D = {(I,H) : 0 <= I <= H, H > 0}:
  - |df/dI| = |1 - 2I/H|. With r = I/H in [0,1]: |1 - 2r| achieves maximum 1 at r=0 and r=1. PASS.
  - |df/dH| = (I/H)^2. With r in [0,1]: r^2 <= 1. PASS.
- Domain convexity: For (I1,H1), (I2,H2) in D and t in [0,1]:
  - H_bar = (1-t)H1 + tH2 > 0 since H1, H2 > 0. PASS.
  - I_bar = (1-t)I1 + tI2 <= (1-t)H1 + tH2 = H_bar since I1 <= H1 and I2 <= H2. PASS.
  - So (I_bar, H_bar) in D. Domain is convex.
- MVT applicability: f is differentiable on the interior of D (which is open and convex), so the multivariate mean value theorem applies. The gradient bound gives ||nabla f||_inf <= 1, yielding the stated inequality.

**Key insight verified:** The paper correctly notes that this yields the bound with coefficient (C_I + C_H)/gap rather than the weaker (2C_I + C_H)/gap that a naive product-rule decomposition would give. The improvement comes from |df/dI| <= 1 (not <= 2 as a direct estimate f = I*(1-I/H) -> |df| <= |dI| + I*|d(I/H)| would suggest). This is correct and meaningful.

**Edge case: H -> 0.** At H = 0, rho is undefined (0/0 form). However, I <= H forces I -> 0 as well, and lim_{H->0, I/H=r} f(I,H) = lim H*r*(1-r) = 0 for any fixed r. So f extends continuously to 0 at the boundary. The MVT is applied on the open interior where H > 0, so this boundary behavior is not a problem for the proof.

**Verdict: SECURE.**

---

### EQ-6: Final nonlinear bound composition (Eq. 20, main.tex lines 446-458; derivation eq:rho-bound-nonlinear)

**Statement:**  |rho(P) - rho(P')| <= (delta/2)[2*ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 4*h_bin(delta/2)

**Checks performed:**
- Combines EQ-5 (|rho - rho'| <= |I - I'| + |H - H'|) with EQ-4 (bound on |I - I'|) and the separate H(B) bound (Eq. 14: |H - H'| <= (delta/2)*ln(|B|-1) + h_bin(delta/2)).
- Log coefficient: [ln(|B|-1) + ln(|M|-1) + ln(n-1)] + [ln(|B|-1)] = 2*ln(|B|-1) + ln(|M|-1) + ln(n-1). PASS.
- Binary entropy coefficient: 3 + 1 = 4. PASS.
- Substituting the Cho-Meyer bound delta <= eps/gap converts from delta-parameterized to eps-parameterized form. PASS.

**Verdict: SECURE.**

---

### EQ-7: Linear Lipschitz constant (Eq. 22, main.tex lines 466-475; derivation eq:L-final)

**Statement:**  L(delta) = (C_I(delta) + C_H(delta)) / gap(P), where C_I = (1/2)[ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 3*eta and C_H = (1/2)*ln(|B|-1) + eta, with eta = h_bin(delta/2)/delta.

**Checks performed:**
- Factoring delta out of the nonlinear bound: The nonlinear bound is (delta/2)*[log terms] + 4*h_bin(delta/2). Writing h_bin(delta/2) = delta * eta, the bound becomes delta * [(1/2)*(log terms) + 4*eta]. PASS.
- Identifying C_I and C_H: C_I collects the MI-bound contribution: (1/2)*[ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 3*eta. C_H collects the H(B)-bound contribution: (1/2)*ln(|B|-1) + eta. Sum is (1/2)*[2*ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 4*eta. This matches the nonlinear bound divided by delta. PASS.
- Then |rho - rho'| <= (C_I + C_H)*delta <= (C_I + C_H)/gap * eps. PASS.

**Note on delta-dependence:** The paper correctly identifies that L(delta) is not a true Lipschitz constant in the classical sense (it depends on the perturbation size through eta). This is because Shannon entropy is not globally Lipschitz. The nonlinear bound (EQ-6) is the cleanest statement. This is accurately discussed in Remark 8 (derivation) / Remark in Section 5 (main.tex).

**Verdict: SECURE.**

---

### EQ-8: Asymptotic expansion (Eq. 12, main.tex line 222; derivation eq:L-asymptotic)

**Statement:**  L ~ (1/(2*gap))*[2*ln(|B|-1) + ln(|M|-1) + ln(n-1)] + (2/gap)*ln(2*gap/eps)

**Checks performed:**
- For small delta = eps/gap: h_bin(delta/2)/delta = h_bin(x)/2x where x = delta/2.
- h_bin(x) = -x*ln(x) - (1-x)*ln(1-x) ~ -x*ln(x) + x for small x (since ln(1-x) ~ -x).
- So h_bin(x)/x ~ -ln(x) + 1 = ln(1/x) + 1.
- Then h_bin(delta/2)/delta = h_bin(x)/(2x) ~ (1/2)*(ln(1/x) + 1) = (1/2)*ln(2/delta) + 1/2.
- The leading behavior of 4*eta = 4*h_bin(delta/2)/delta ~ 2*ln(2/delta) + 2.
- Substituting delta = eps/gap: 2*ln(2*gap/eps) + 2.
- The "+2" is subleading and dropped in the asymptotic expression. The log term matches the paper's Eq. 12.

**Minor note:** The asymptotic expression drops O(1) terms. This is standard and correctly described as asymptotic (~) rather than exact (=). PASS.

**Verdict: SECURE.**

---

### EQ-9: Uniform bound (Eq. 13, main.tex line 232; derivation eq:uniform)

**Statement:**  |rho - rho'| <= (eps/(2*gap))*[2*ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 4*ln(2)

**Checks performed:**
- Uses h_bin(x) <= ln(2) for all x in [0,1]. This is the well-known maximum of binary entropy at x=1/2. PASS.
- Substituting into the nonlinear bound: (delta/2)*[log terms] + 4*ln(2). With delta <= eps/gap: (eps/(2*gap))*[log terms] + 4*ln(2). PASS.
- The numerical value 4*ln(2) = 2.773 nats. Consistent with the paper's claim.

**Verdict: SECURE.**

---

## Derivation Integrity

The proof has a clean three-step pipeline:

1. **Kernel -> Stationary distribution** (Cho-Meyer): eps -> delta. Standard result, correctly cited, correct norm pairing.
2. **Stationary distribution -> Information quantities** (Fannes-Audenaert + marginal contraction): delta -> |dI|, |dH|. Triangle inequality and three Fannes applications. All alphabet sizes correct, L1/TV conversion correct.
3. **Information quantities -> rho** (MVT): |dI|, |dH| -> |d(rho)|. Gradient bounds correct, domain convexity verified, MVT correctly applied.

Each interface is clean: Step 1 outputs delta (dimensionless L1 distance), Step 2 consumes delta and outputs entropy/MI bounds (in nats), Step 3 consumes those bounds and outputs the rho bound (in nats).

**Self-consistency between main.tex and derivations/lipschitz-stability.tex:** The derivation and the paper state identical equations. The paper is a condensed version of the derivation with added context (introduction, numerical verification, discussion). No discrepancies found.

**Self-consistency between paper and code:** The `nonlinear_bound()` function in the verification code implements exactly (delta/2)*log_coeff + 4*h_bin(delta/2), matching Eq. 6 of the paper. The `L_proven()` function correctly computes nonlinear_bound(eps/gap)/eps. The `compute_rho()` function correctly implements rho = I*(1-I/H(B)) using numpy's natural logarithm.

---

## Limiting Cases

| Limit | Paper's claim | Verification | Status |
|-------|---------------|-------------|--------|
| P' = P (zero perturbation) | Bound = 0 | eps=0, delta=0, first term vanishes, h_bin(0)=0. Direct: rho(P)-rho(P)=0. | PASS |
| gap -> 1 (fast mixing) | L_eff ~ 3.00 for toy model | (1/2)*[2*ln(3)+ln(3)+ln(15)] = (1/2)*[2.197+1.099+2.708] = (1/2)*6.004 = 3.002. | PASS |
| gap -> 0 (slow mixing) | L -> infinity | delta = eps/gap -> infinity (capped at 2); bound grows; L diverges. Physically: near-reducible chains have sensitive stationary distributions. | PASS |
| I = 0 (independent B,M) | rho ~ I for small I | f(I,H) = I - I^2/H ~ I for I << H. Bound gives |d(rho)| <= |dI| + |dH|, consistent. | PASS |
| I = H (perfect tracking) | rho ~ H - I near boundary | f(I,H) = I(1-I/H) = (I/H)(H-I). At I~H: rho ~ (H-I). df/dI = 1-2I/H ~ -1, correct. | PASS |
| |B|=|M|=2 minimal system | Bound reduces to (delta/2)*ln(3) + 4*h_bin(delta/2) | Only ln(n-1)=ln(3) contributes since ln(|B|-1)=ln(1)=0 and ln(|M|-1)=0. Correct. | PASS |

**Additional limit not in paper but checked:** rho_max = H(B)/4. For the toy model with uniform body marginal: H(B) = ln(4) = 1.386, so rho_max = 0.347 nats. The paper's Table 1 states rho(P) = 0.346, which is consistent (the chain is not perfectly at the maximum since I/H = 0.508, not exactly 0.5).

---

## Numerical Verification Cross-Check

**What the code does correctly:**
- Convention checks (line 406-453): verifies nats, MI=0 for independent, rho(0,H)=0, rho(H,H)=0, rho(H/2,H)=H/4, h_bin boundaries.
- Perturbation generation (line 154-207): adds zero-sum random noise to each row, clips, renormalizes, checks irreducibility via spectral gap > 1e-6. This is a valid perturbation method.
- The comparison metric is correct: L_numerical = max |rho - rho'| / ||P - P'||_inf (actual epsilon, not target epsilon). Compared against L_proven = nonlinear_bound(eps/gap) / eps.

**Potential concern with perturbation method:** Clipping and renormalization change the effective perturbation magnitude. The code uses the *actual* ||P - P'||_inf (line 202), not the target epsilon, when computing ratios. This is correct.

**What the figure shows (verified from PDF):**
- Panel (a): Histogram of Lipschitz ratios at eps=0.01. All values clustered near 0, with L_proven = 109.43 far to the right. Zero violations.
- Panel (b): Log-log plot of L_numerical vs gap. Power-law fit exponent -0.89, R^2 = 0.97. Consistent with theoretical -1.
- Panel (c): L*gap vs ln|Omega|. L_proven*gap shows clear linear trend (R^2 = 0.975). L_numerical*gap is flat/declining. This is expected: the *proven* bound scales as ln|Omega|/gap by construction, while the *actual* sensitivity need not (random perturbations of larger systems may be less effective).
- Panel (d): Convergence plot. L_numerical stabilizes by N~500.

**Cross-check of reported values against the bound formula (hand-computed):**
- eps=0.01, gap=0.1: delta = 0.1. Bound = (0.05)*[2*1.099 + 1.099 + 2.708] + 4*h_bin(0.05).
  - = 0.05 * 6.005 + 4*[-0.05*ln(0.05) - 0.95*ln(0.95)]
  - = 0.300 + 4*[0.05*2.996 + 0.95*0.0513]
  - = 0.300 + 4*[0.1498 + 0.0487]
  - = 0.300 + 4*0.1985 = 0.300 + 0.794 = 1.094. Matches paper's 1.094.
- L_proven = 1.094 / 0.01 = 109.4. Matches paper's 109.4.
- eps=0.01, gap=1.0: delta = 0.01. Bound = 0.005*6.005 + 4*h_bin(0.005).
  - = 0.0300 + 4*[-0.005*ln(0.005) - 0.995*ln(0.995)]
  - = 0.0300 + 4*[0.005*5.298 + 0.995*0.00501]
  - = 0.0300 + 4*[0.02649 + 0.00499]
  - = 0.0300 + 4*0.03148 = 0.0300 + 0.1259 = 0.156. Matches paper's 0.156.

**Verdict:** Numerical verification logic is sound. Code correctly implements the bound. Reported numbers are consistent with hand computation.

---

## Self-Consistency Checks

| Check | Status |
|-------|--------|
| Derivation and paper state identical equations | PASS |
| Code implements the same formula as derivation | PASS |
| L1 norm convention used consistently (never TV without explicit conversion) | PASS |
| Entropy base is nats (ln) everywhere: derivation, paper, code | PASS |
| Spectral gap definition (absolute, 1-|lambda_2|) consistent across all files | PASS |
| Row-stochastic convention (pi*P = pi) consistent across all files | PASS |
| Row-sum norm convention consistent across derivation and code | PASS |
| C_I and C_H sum to the correct total for the nonlinear bound | PASS |
| Table values in Section 7 match the formula | PASS (verified two entries by hand) |
| The "4" coefficient in 4*h_bin(delta/2) is correct (3 from MI bound + 1 from H(B) bound) | PASS |

---

## Unchecked Risk Areas

1. **Cho-Meyer Theorem 3.1 itself.** I accepted the bound ||(I - P + Pi)^{-1}||_inf <= 1/gap(P) from the literature without re-derivation. This is a standard result (Meyer 1975, Cho-Meyer 2001) and is not in doubt, but for full rigor one would trace through the resolvent bound.

2. **Tightness of the bound.** The paper reports tightness gaps of 450-9500x and correctly identifies four sources of slack. I did not attempt to prove a lower bound on the Lipschitz constant or to construct adversarial perturbations that approach the bound. The paper does not claim tightness, so this is not an error.

3. **Fannes-Audenaert validity at delta > 2(1-1/k).** As noted under EQ-3, the Fannes bound is technically stated for delta in (0, 2(1-1/k)]. When delta exceeds this (which requires gap << eps, putting us in the vacuous regime), the formula still produces a finite bound but it is no longer guaranteed to be an upper bound by the Audenaert theorem. However, in that regime the bound exceeds rho_max anyway, so it is vacuously true that |rho - rho'| <= bound (since |rho - rho'| <= rho_max < bound). The paper could acknowledge this more explicitly, but it does not affect correctness.

4. **Numerical verification samples only random perturbations, not adversarial ones.** The zero-violation result over 3000 random perturbations is strong evidence but not a proof. The paper correctly treats this as verification, not proof. The proof is the analytical derivation.

5. **Extension to non-irreducible P'.** The theorem requires P' irreducible. If P' has a zero spectral gap, the stationary distribution may not be unique. The code enforces gap(P') > 1e-6. The paper states this requirement in the domain of validity. No issue, but worth noting.

---

## Issues Found

### MATH-1 (MINOR): Fannes-Audenaert validity domain at extreme delta

**Location:** main.tex Eq. 6 (nonlinear bound), code line 120 (delta cap at 2.0)
**Description:** The Fannes-Audenaert bound requires delta/2 < 1 - 1/k. For the marginals with k=4, this means delta < 1.5. For the joint with k=16, delta < 1.875. The code caps delta at 2.0, which can exceed both limits. The paper's nonlinear bound formula is applied at delta values outside Fannes-Audenaert's stated validity.
**Impact:** None on any reported result. In the regime where delta exceeds the Fannes validity bound, the overall Lipschitz bound exceeds rho_max, so it is vacuously valid. The bound is still finite and non-negative.
**Required action:** None (would be a minor presentation improvement to note this in the domain of validity statement).
**Severity:** Minor/suggestion.
**Blocking:** No.

### MATH-2 (MINOR): The "Lipschitz constant" is not a true constant

**Location:** main.tex Eq. 8-10 (L(delta) definition), Remark after Eq. 22 in derivation
**Description:** L(delta) diverges logarithmically as delta -> 0. This means rho is not globally Lipschitz with a finite constant. The paper correctly identifies this in Remark 8/Section 5 Remark and attributes it to the entropy functional, but the title "Lipschitz Stability" could be read as claiming a global Lipschitz bound. The nonlinear bound (EQ-6) is the clean result; the "Lipschitz constant" L(delta) is a derived convenience.
**Impact:** No mathematical error. The nonlinear bound is valid for all delta simultaneously.
**Required action:** None (already adequately discussed in the text).
**Severity:** Minor/suggestion.
**Blocking:** No.

---

## Summary Table

| Item | Status |
|------|--------|
| EQ-1: rho definition | SECURE |
| EQ-2: Cho-Meyer bound | SECURE |
| EQ-3: Fannes-Audenaert | SECURE (minor edge-case note) |
| EQ-4: MI continuity bound | SECURE |
| EQ-5: MVT composition | SECURE |
| EQ-6: Nonlinear bound (main result) | SECURE |
| EQ-7: Linear Lipschitz constant | SECURE |
| EQ-8: Asymptotic expansion | SECURE |
| EQ-9: Uniform bound | SECURE |
| Derivation pipeline | Correct, clean three-step composition |
| Limiting cases (6/6) | All verified |
| Dimensional consistency | All terms checked, no mismatches |
| Convention consistency | L1/TV, nats, row-stochastic all consistent |
| Numerical verification logic | Sound |
| Code-paper agreement | Exact match |
| Unchecked areas | Cho-Meyer re-derivation, adversarial tightness, Fannes edge |

**Bottom line:** The mathematics in this paper is correct. The three-step composition is sound, each ingredient is standard and correctly applied, and all algebraic manipulations check out. The bound is conservative (by 450-9500x) but valid. No blocking issues found.
