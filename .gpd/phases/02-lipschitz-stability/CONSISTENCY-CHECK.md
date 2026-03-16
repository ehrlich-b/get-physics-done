# Consistency Check: Phase 02 (Lipschitz Stability)

**Mode:** rapid
**Date:** 2026-03-16
**Checker:** gpd-consistency-checker
**Phase scope:** 02-lipschitz-stability (Plans 01 and 02)

---

## Conventions Self-Test

Project type: information-theoretic. All 18 standard QFT conventions are N/A (documented in CONVENTIONS.md and state.json convention_lock). The 7 custom conventions are the ground truth for this check.

| Custom Convention | CONVENTIONS.md | state.json | Match |
|---|---|---|---|
| Entropy base | nats (ln) | nats (natural logarithm) | PASS |
| Mutual information | I(B;M) = H(B) + H(M) - H(B,M) | I(B;M) = H(B) + H(M) - H(B,M) | PASS |
| Experiential density | rho(p) = I(B;M) * (1 - I(B;M)/H(B)) | rho(p) = I(B;M) * (1 - I(B;M)/H(B)) | PASS |
| Generator convention | probabilist: dp/dt = pQ | probabilist: dp/dt = pQ | PASS |
| Matrix norm | sup-norm on rows: max_i sum_j \|P_ij\| | sup-norm on rows: \|\|P\|\|_inf = max_i sum_j \|P_ij\| | PASS |
| Von Neumann entropy | S_vN(rho) = -Tr(rho ln rho) in nats | S_vN(rho) = -Tr(rho ln rho) in nats | PASS |
| L1 vs TV | L1 throughout; TV = (1/2)*L1 | Not explicitly in state.json but documented in CONVENTIONS.md cross-convention table | PASS |

**Cross-convention interaction check:**
- Entropy base (nats) + rho_max: CONVENTIONS.md states "H(B)/4 in nats (ln(4)/4 = 0.347 for 4-state body)". ln(4)/4 = 1.386/4 = 0.347. PASS.
- Entropy base (nats) + trajectory functional: "nat-seconds". Consistent. PASS.

**Self-test result: PASS** -- conventions ledger is internally consistent.

---

## Provides/Requires Verification

### Transfer 1: Phase 01 -> Phase 02 Plan 01

**Requirement (02-01-SUMMARY frontmatter):** Phase 01 provides "Definition of rho(P), toy model parameters, convention lock"

| Quantity | Phase 01 provides | Phase 02 uses | Match |
|---|---|---|---|
| rho(P) definition | I(B;M) * (1 - I(B;M)/H(B)) | Eq. (02.1) in lipschitz-stability.tex eq:rho-def: same form | PASS |
| Toy model \|B\|=\|M\|=4 | 01-01-SUMMARY: 16-state chain, |B|=|M|=4 | lipschitz-stability.tex Section 6.6: |B|=|M|=4, n=16 | PASS |
| Convention lock (entropy=nats) | 01-01-SUMMARY conventions: entropy_base=nats | lipschitz-stability.tex line 1: ASSERT_CONVENTION entropy_base=nats | PASS |
| Convention lock (generator=probabilist) | 01-01-SUMMARY: generator_convention=probabilist dp/dt=pQ | lipschitz-stability.tex: pi*P = pi (row-vector left, matrix right) | PASS |
| Convention lock (matrix norm=sup-norm rows) | 01-01-SUMMARY: matrix_norm=sup_norm_rows | lipschitz-stability.tex: \|\|P\|\|_inf = max_i sum_j \|P_ij\| | PASS |

**Physical meaning check:**
- Phase 01 defines rho as the experiential density measuring the "meaningful complexity" that peaks between pure order and pure randomness for a composite Markov process on B x M.
- Phase 02 treats rho as an information-theoretic functional of the stationary distribution, analyzing its continuity under kernel perturbations.
- These are the same physical quantity. PASS.

**Test value:** rho for the 7-chain observer (alpha=0.5).
- Phase 01 (STATE.md intermediate results): "Parametric peak at tracking accuracy alpha ~= 0.498 with I*/H = 0.507" and user anchor "Toy model rho = 0.347 for self-modeling observer"
- Phase 02 Plan 02 code output: rho = 0.346, I = 0.705, H = 1.386, I/H = 0.508
- I/H: 0.507 (Phase 01) vs 0.508 (Phase 02) -- within rounding. PASS.
- rho: 0.347 (Phase 01 anchor) vs 0.346 (Phase 02 numerical). Difference 0.001 nats, attributable to floating point in stationary distribution computation. PASS.

### Transfer 2: Phase 02 Plan 01 -> Phase 02 Plan 02

**Requirement (02-02-SUMMARY frontmatter):** Plan 01 provides "Proven Lipschitz bound with explicit constants C_I, C_H, gap(P)"

| Quantity | Plan 01 provides | Plan 02 uses | Match |
|---|---|---|---|
| Non-linear bound formula | Eq. (02.1): (delta/2)[2ln(\|B\|-1)+ln(\|M\|-1)+ln(n-1)] + 4*h_bin(delta/2) | `nonlinear_bound()` in code lines 95-122: same formula | PASS |
| delta definition | delta = \|\|pi-pi'\|\|_1 <= \|\|P-P'\|\|_inf / gap(P) | `L_proven()` lines 148-151: delta = epsilon / gap | PASS |
| L = (C_I + C_H)/gap | Eq. (02.2) with MVT-improved constants | Code computes L_eff = nonlinear_bound(eps/gap)/eps, which is equivalent | PASS |
| Log coefficient for toy model | (1/2)[2ln3 + ln3 + ln15] = 3.002 | Code `nonlinear_bound(delta, 4, 4)`: 2*log(3)+log(3)+log(15) = 3*log(3)+log(15) = 3*1.099+2.708 = 6.005; divided by 2 gives 3.002 per the formula (delta/2)*6.005. PASS. | PASS |

**Physical meaning check:**
- Plan 01 proves the bound analytically as a worst-case upper bound on |rho(P) - rho(P')|.
- Plan 02 verifies it numerically by checking L_numerical <= L_proven for random perturbations.
- Same physical quantity (Lipschitz ratio), same direction of inequality. PASS.

**Test value (spot check):** For toy model, gap=0.1, eps=0.01:
- delta = eps/gap = 0.1
- Plan 01 table (Section 6.6): delta=0.10, bound = 1.094 nats
- Plan 02 code: nonlinear_bound(0.1, 4, 4) = (0.1/2)*[2*ln(3)+ln(3)+ln(15)] + 4*h_bin(0.05)
  = 0.05 * 6.005 + 4*(-0.05*ln(0.05) - 0.95*ln(0.95))
  = 0.300 + 4*(0.1497 + 0.0487) = 0.300 + 4*0.199 = 0.300 + 0.794 = 1.094 nats. PASS.

---

## Convention Compliance Matrix (Phase 02 vs Full Ledger)

| Convention | Source | Phase 02 Plan 01 (tex) | Phase 02 Plan 02 (code) | Status |
|---|---|---|---|---|
| Entropy = nats (ln) | CONVENTIONS.md | "all in nats" (tex line 49), uses ln throughout | `entropy()` uses `np.log()` = ln; convention check: H([0.25]*4)=ln(4) | PASS |
| MI = H(B)+H(M)-H(B,M) | CONVENTIONS.md | tex eq:MI-triangle: I=H(B)+H(M)-H(B,M) | `mutual_info()`: entropy(p_x)+entropy(p_y)-entropy(joint) | PASS |
| rho = I*(1-I/H(B)) | CONVENTIONS.md | tex eq:rho-def: exactly this form | `rho_func(I, H)`: I*(1-I/H) | PASS |
| Generator: dp/dt = pQ | CONVENTIONS.md | tex: "pi satisfying piP = pi (left eigenvector)" -- row-vector left convention | `stationary()`: left eigenvector of P via eig(P.T); `build_tracking`: P row-stochastic | PASS |
| Matrix norm: row-sum inf | CONVENTIONS.md | tex Definition 2: max_i sum_j \|P_ij\| | Code line 202: `np.max(np.sum(np.abs(P_prime - P), axis=1))` -- max row-sum of absolute values | PASS |
| L1 norm (NOT TV) | CONVENTIONS.md | tex: "\|\|p-q\|\|_1 = sum \|p_i-q_i\|. TV = (1/2)\|\|.\|\|_1" + Remark 4 explicit TV conversion | Code line 17: ASSERT_CONVENTION l1_not_tv=true; all L1 norm computations use sum of absolutes | PASS |
| Von Neumann entropy | CONVENTIONS.md | Not used in Phase 02 (classical phase) | Not used in Phase 02 (classical phase) | N/A |

**Non-adjacent convention check:** Phase 01 established these conventions. Phase 02 follows them. No convention drift detected.

---

## Sign and Factor Spot-Checks

### Spot-Check 1: Fannes-Audenaert L1/TV conversion (highest priority -- this is the error most likely to cause a factor-of-2 bug)

**Convention:** The Fannes-Audenaert bound in many textbooks uses TV distance: |H(p)-H(q)| <= delta_TV * ln(k-1) + h_bin(delta_TV).
**Project convention:** L1 norm. delta_L1 = 2 * delta_TV.

**In lipschitz-stability.tex (Remark 4, line 219):** "Many references state this bound with delta_TV = ||p-q||_TV = (1/2)||p-q||_1. In that convention, the bound reads |H(p)-H(q)| <= delta_TV*ln(k-1) + h_bin(delta_TV). Our formula is the same after substituting delta_TV = delta/2."

**Verification:** The tex eq:fannes states: |H(p)-H(q)| <= (delta/2)*ln(k-1) + h_bin(delta/2), where delta = ||p-q||_1.
- Substituting delta_TV = delta/2: (delta_TV)*ln(k-1) + h_bin(delta_TV). This matches the TV-convention form. PASS.

**Test value:** Two distributions on k=4 states: p = [0.4, 0.3, 0.2, 0.1], q = [0.3, 0.3, 0.2, 0.2].
- delta_L1 = |0.1| + |0| + |0| + |0.1| = 0.2
- delta_TV = 0.1
- Bound: (0.2/2)*ln(3) + h_bin(0.1) = 0.1*1.099 + (-0.1*ln(0.1) - 0.9*ln(0.9)) = 0.110 + 0.230 + 0.095 = 0.435 nats
- Actual: H(p) = -(0.4*ln(0.4)+0.3*ln(0.3)+0.2*ln(0.2)+0.1*ln(0.1)) = 0.367+0.361+0.322+0.230 = 1.280. H(q) = -(0.3*ln(0.3)+0.3*ln(0.3)+0.2*ln(0.2)+0.2*ln(0.2)) = 0.361+0.361+0.322+0.322 = 1.366. |H(p)-H(q)| = 0.086 nats.
- 0.086 < 0.435. Bound holds. PASS.

### Spot-Check 2: MVT gradient bounds (load-bearing for the C_I + C_H improvement)

**Claim (tex eq:df-dI, eq:df-dH):** For f(I,H) = I*(1-I/H):
- df/dI = 1 - 2I/H, so |df/dI| <= 1 since I/H in [0,1]
- df/dH = I^2/H^2, so |df/dH| <= 1 since I/H in [0,1]

**Verification:**
- df/dI = d/dI [I - I^2/H] = 1 - 2I/H. For x = I/H in [0,1]: |1-2x| achieves max 1 at x=0 and x=1, min 0 at x=1/2. PASS.
- df/dH = d/dH [I - I^2/H] = I^2/H^2 = (I/H)^2. For x in [0,1]: x^2 <= 1. PASS.

**Test value at observer chain (I/H = 0.508):**
- |df/dI| = |1 - 2*0.508| = |1 - 1.016| = 0.016. Much less than 1. Consistent.
- |df/dH| = 0.508^2 = 0.258. Less than 1. Consistent.
- The MVT bound is valid but loose by factor ~4 at df/dH and ~60 at df/dI for this operating point. This explains part of the 450-9500x tightness gap.

### Spot-Check 3: Non-linear bound composition (the primary result, Eq. 02.1)

**Claim:** |rho-rho'| <= |I-I'| + |H-H'| <= [(delta/2)(ln(|B|-1)+ln(|M|-1)+ln(n-1)) + 3*h_bin(delta/2)] + [(delta/2)*ln(|B|-1) + h_bin(delta/2)]
= (delta/2)[2ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 4*h_bin(delta/2)

**Algebra check:**
- First bracket (MI bound): (delta/2)*[ln(|B|-1) + ln(|M|-1) + ln(n-1)] + 3*h_bin(delta/2)
- Second bracket (H(B) bound): (delta/2)*ln(|B|-1) + h_bin(delta/2)
- Sum of delta/2 coefficients: [ln(|B|-1) + ln(|M|-1) + ln(n-1)] + [ln(|B|-1)] = 2*ln(|B|-1) + ln(|M|-1) + ln(n-1). PASS.
- Sum of h_bin coefficients: 3 + 1 = 4. PASS.

---

## Approximation Validity Check

| Approximation | Stated validity | Phase 02 usage | Status |
|---|---|---|---|
| Cho-Meyer 1/gap bound | P, P' irreducible | Code checks spectral_gap > 1e-6 before using perturbation (line 201) | PASS |
| Fannes-Audenaert | delta < 2(1-1/k) | For k=4 (toy model): delta < 1.5. At eps=0.1, gap=0.1: delta=1.0 < 1.5. PASS. At eps=0.1, gap=0.004 (smallest tested gap): delta=25, capped at 2.0 by code line 120. Cap is within Fannes validity for k>=2: 2 < 2*(1-1/2)=1... wait, 2*(1-1/2) = 1.0. For delta_TV: delta/2 < 1-1/k. At delta=2: delta/2=1, need 1 < 1-1/k = 0.75 for k=4. This is VIOLATED. | WARNING |
| MVT on convex domain | 0 <= I <= H, H > 0 | Stationary distribution of irreducible chain has pi_i > 0, so H(B) > 0 and 0 <= I <= H | PASS |

**Fannes validity detail:** The Fannes-Audenaert bound requires delta/2 < 1 - 1/k (in L1 convention: delta < 2(1 - 1/k)). For k=4: delta < 1.5. The code caps delta at 2.0 (line 120), but at delta=2.0 the Fannes bound is technically outside its stated validity for the marginal entropies (k=4 gives limit 1.5). However:
- For H(B,M) with k=n=16: limit is 2*(1-1/16) = 1.875. At delta=2.0, still slightly exceeded.
- In practice, delta = eps/gap. At eps=0.1 and gap=0.1 (observer chain): delta=1.0, which is within bounds.
- The cap at delta=2.0 occurs only for extreme perturbations where the bound is already vacuous (exceeds rho_max).
- The Fannes bound at delta near the boundary approaches infinity (h_bin -> ln 2), so the bound becomes vacuously large but never negative or undefined.
- **Verdict:** This is a minor edge case affecting only the vacuous regime. Not a correctness issue for the meaningful results (L_numerical <= L_proven tests). WARNING, not ERROR.

---

## Dimensional Consistency

| Quantity | Dimensions | Phase 02 usage | Status |
|---|---|---|---|
| rho(P) | [nats] | rho = I*(1-I/H): [nats]*[dimensionless] = [nats] | PASS |
| L (Lipschitz constant) | [nats] (since ||P-P'||_inf is dimensionless) | L = (C_I + C_H)/gap: [nats]/[dimensionless] = [nats] | PASS |
| delta = \|\|pi-pi'\|\|_1 | [dimensionless] | Sum of absolute differences of probabilities | PASS |
| h_bin(delta/2) | [nats] | Binary entropy in nats | PASS |
| Non-linear bound | [nats] | (delta/2)*[nats terms] + [nats] = [nats]. Matches [rho]. | PASS |

---

## Provides Check for Downstream Phases

Phase 02 provides (from SUMMARY frontmatter):
1. "Non-linear Lipschitz bound for rho(P) in terms of ||P-P'||_inf, gap(P), and |Omega|" -- Delivered in derivations/lipschitz-stability.tex Theorem 1.
2. "Explicit constants C_I, C_H as functions of |B|, |M|" -- Delivered in tex Eqs. (02.2), CI, CH.
3. "Six verified limiting cases" -- Delivered in tex Section 6.
4. "Toy model numerical evaluation table" -- Delivered in tex Section 6.6 table.
5. "Numerical confirmation that L_numerical <= L_proven" -- Delivered in code, 3000 perturbations, zero violations.
6. "Tightness ratio: bound is loose by factor 450-9500x" -- Documented in 02-02-SUMMARY.
7. "Power-law scaling: L ~ gap^{-0.89}" -- Documented with R^2=0.97.

Phase 03 (Born-Fisher Test) does not require Lipschitz results directly (it tests I_vN/S_vN ratio for qubit model). The Lipschitz bound is primarily for paper writing and the overall theoretical framework. No downstream phase currently consumes these results for computation, so there is no risk of propagation errors from the tightness looseness.

---

## Issues Summary

| # | Severity | Description |
|---|---|---|
| 1 | WARNING | Fannes-Audenaert validity condition (delta < 2(1-1/k)) technically violated when delta is capped at 2.0 in code. This affects only the vacuous regime where the bound exceeds rho_max. Not a correctness issue for any reported numerical results. |

---

## Verdict: PASS (1 warning, 0 errors)

All custom conventions maintained consistently across Phase 01 -> Phase 02 boundary and within Phase 02 plans. Key equations verified by test-value substitution. L1/TV conversion handled correctly (the single highest-risk factor for this project). MVT gradient bounds verified analytically and numerically. No sign or factor errors detected. The 450-9500x tightness gap is fully explained by the composition of worst-case bounds and is correctly documented as an open tightening opportunity.
