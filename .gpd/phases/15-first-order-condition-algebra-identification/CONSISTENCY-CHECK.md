# Consistency Check: Phase 15 (First-Order Condition and Algebra Identification)

**Mode:** rapid
**Scope:** Phase 15 (Plans 15-01, 15-02) checked against full conventions ledger and phases 13, 14
**Date:** 2026-03-23

## Conventions Self-Test

Convention lock in state.json and CONVENTIONS.md / STATE.md are aligned. Most QFT conventions are N/A (algebraic/categorical project). The active conventions relevant to phases 13-15 are:

| Convention | Value | Source | Self-consistent? |
|---|---|---|---|
| Commutator | [A,B] = AB - BA | Convention lock | YES |
| KO-dim 6 signs | (epsilon, epsilon', epsilon'') = (+1, +1, -1) | Phase 13, 14, 15 | YES |
| Barrett isomorphism | v tensor w -> v w^T | Phase 13-03 | YES |
| J (antilinear) | J(X_p, X_ap) = (overline{X_ap}^T, overline{X_p}^T) | Phase 13 | YES |
| gamma | diag(P, -P), P = transpose | Phase 13-02 | YES |
| pi(a) / pi_o(b) | L_a / R_b under Barrett iso | Phase 13 | YES |
| Jordan product | a * b = (1/2)(ab + ba) | Convention lock | YES |
| Sequential product | a & b = sqrt(a) b sqrt(a) | Convention lock | YES |
| Barrett-form D | D_K(X) = KX + XK, K in M_n(R)^sym | Phase 14-02 | YES |

No cross-convention incompatibilities detected.

## Provides/Consumes Verification

| Quantity | Producer | Consumer | Meaning Match | Units Match | Test Value | Convention Match | Status |
|---|---|---|---|---|---|---|---|
| Barrett-form D_K(X) = KX + XK | Phase 14-02 | Phase 15-01 | YES | YES (dimensionless) | K=diag(1,0), a=E_{12}, X=E_{21}: both give E_{11} | YES | PASS |
| pi(a)=L_a, pi_o(b)=R_b, [L_a,R_b]=0 | Phase 13-01 | Phase 15-01 | YES | YES | Tensor factor commutativity = associativity | YES | PASS |
| D moduli dim = n^2(n^2+1) | Phase 14-01 | Phase 15-02 | YES | YES | n=2: 20, n=3: 90, n=4: 272 match | YES | PASS |
| Barrett subspace dim = n(n+1)/2 | Phase 14-02 | Phase 15-02 | YES | YES | n=4: 10 matches | YES | PASS |
| A_F = M_n(C) for Barrett D | Phase 15-01 | Phase 15-02 | YES | YES | dim(A_F)=n^2 confirmed in both | YES | PASS |
| Involution M = J_+ M^T J_+ | Phase 14-01 | Phase 15-02 | YES | YES | Used in moduli sampling | YES | PASS |

**All 6 provides/consumes pairs verified. Zero failures.**

## Convention Compliance Matrix (Phase 15 vs Full Ledger)

| Convention | Introduced | Relevant to Phase 15? | Compliant? | Evidence |
|---|---|---|---|---|
| [A,B] = AB - BA | Phase 0 | YES | YES | All commutators in Eqs. (15-01.2), (15-02.1), (15-02.2) use AB - BA |
| KO-dim 6: (+1,+1,-1) | Phase 13 | YES | YES | Phase 15-01 conventions block states epsilon'=+1; Barrett D selected by this sign |
| Barrett iso: v tensor w -> vw^T | Phase 13-03 | YES | YES | Phase 15 uses L_a, R_b throughout Barrett iso |
| J antilinear | Phase 13 | YES (indirectly) | YES | Phase 15 inherits J via Phase 14 moduli constraint |
| gamma = diag(P,-P) | Phase 13-02 | YES (indirectly) | YES | D block form [[0,M^dag],[M,0]] anticommutes with gamma |
| Jordan product a*b = (1/2)(ab+ba) | Phase 14-02 | YES | YES | Phase 15-01 convention block: K*X = (1/2)(KX+XK). Matches. |
| SP notation a&b = sqrt(a)b sqrt(a) | Phase 0 | NO (SP not used in Phase 15) | N/A | Phase 15 works with linearized form (Jordan product) only |
| Tr(rho) = 1 | Phase 0 | NO | N/A | No density matrices in Phase 15 |
| H = sum h_{xy} (no 1/2) | Phase 8 | NO | N/A | No Hamiltonian in Phase 15 |

**All relevant conventions compliant. Zero violations.**

## Sign and Factor Spot-Checks (3 Load-Bearing Equations)

### Check 1: Eq. (15-01.2) -- [D_1, L_a] = L_{[K,a]}

Test: K = diag(1,0), a = E_{12}, X = E_{21} at n=2.

- D_1(aX) = D_1(E_{12}*E_{21}) = D_1(E_{11}) = KE_{11} + E_{11}K = diag(1,0)*E_{11} + E_{11}*diag(1,0) = E_{11} + E_{11} = 2E_{11}
- aD_1(X) = E_{12}*(KE_{21} + E_{21}K) = E_{12}*(diag(1,0)*E_{21} + E_{21}*diag(1,0)) = E_{12}*(E_{21} + 0) = E_{11}
- [D_1, L_a](E_{21}) = 2E_{11} - E_{11} = E_{11}
- [K,a] = diag(1,0)*E_{12} - E_{12}*diag(1,0) = E_{12} - 0 = E_{12}
- L_{[K,a]}(E_{21}) = E_{12}*E_{21} = E_{11}

**Result: E_{11} = E_{11}. PASS.**

### Check 2: Eq. (15-01.3) -- [[D_1, L_a], R_b] = 0

This reduces to [L_C, R_b] = 0 where C = [K,a] = E_{12}. Test with b = E_{21}, X = E_{11}.

- L_C(R_b(X)) = L_C(X*b) = L_C(E_{11}*E_{21}) = E_{12}*0 = 0
- R_b(L_C(X)) = (CX)*b = (E_{12}*E_{11})*E_{21} = 0*E_{21} = 0

**Result: 0 = 0. PASS.** (Associativity verified.)

### Check 3: Eq. (15-02.2) -- Master formula [[M, L_a], R_b](X) = sum_k [A_k, a] X [b, B_k]

Barrett form: M(X) = KX + XK. Operator sum: A_1=K, B_1=I; A_2=I, B_2=K.

- Term 1: [K, a] X [b, I] = [K, a] * X * 0 = 0
- Term 2: [I, a] X [b, K] = 0 * X * [b, K] = 0
- Total: 0

**Result: 0 = 0. PASS.** (Barrett triviality confirmed by master formula.)

## Approximation Validity

No new parameter values or approximation ranges introduced in Phase 15. All results are exact algebraic identities (not approximations), verified numerically at n=2,3,4.

## Cross-Phase Error Pattern Check

| Pattern | Instances | Status |
|---|---|---|
| Sign absorbed into definition | 0 | No sign redefinitions between phases 14 and 15 |
| Normalization factor change | 0 | No normalization changes |
| Implicit assumption violated | 0 | Phase 15 correctly requires K real symmetric (from Phase 14-02) |
| Coupling convention mismatch | 0 | N/A |
| Factor of 2pi | 0 | No Fourier transforms or momentum integrals |

## Specific Cross-Phase Consistency Notes

1. **Phase 14-02 uncertainty marker resolved:** Phase 14-02 noted "Barrett-form subspace (n(n+1)/2 params) expected to coincide with first-order condition subspace, but not verified until Phase 15." Phase 15-02 Step 13 confirms this: imposing A_F = M_n(C) on the first-order condition selects exactly the Barrett subspace. The Barrett-CCM correspondence (Barrett 2015 Prop 3.1) is confirmed.

2. **Phase 13-02 even condition failure propagation:** Phase 13-02 established that [gamma, pi(a)] = 0 fails for non-scalar a. Phase 15 does not require the even condition for its derivation (the first-order condition is independent of gamma commutation with pi). This is correctly handled -- no silent assumption violation.

3. **Dimension chain consistency:** Phase 14-01 gives dim(moduli) = n^2(n^2+1). Phase 14-02 gives dim(Barrett subspace) = n(n+1)/2. Phase 15-02 computes codimension = n^2(n^2+1) - n(n+1)/2 = n(n+1)(2n^2-1)/2. At n=4: 272 - 10 = 262. Algebraic identity verified: 4*5*31/2 = 310. Wait: n(n+1)(2n^2-1)/2 at n=4 = 4*5*(32-1)/2 = 4*5*31/2 = 310. But the text says 262. Let me recheck: n^2(n^2+1) = 16*17 = 272. n(n+1)/2 = 10. 272 - 10 = 262. The formula n(n+1)(2n^2-1)/2 at n=4 = 4*5*31/2 = 310 does NOT equal 262. The algebraic simplification in the derivation file is incorrect: n^2(n^2+1) - n(n+1)/2 = n(2n^3 + 2n^2 - n - 1)/2, NOT n(n+1)(2n^2-1)/2. However, this is a cosmetic algebra error in Step 13 of the derivation -- the numerical value 262 is correct (272 - 10 = 262), and neither the derivation's conclusions nor any downstream result depends on this intermediate algebraic simplification. **MINOR: cosmetic formula error in codimension expression; numerical values correct.**

## Summary

| Check Category | Performed | Issues |
|---|---|---|
| Convention compliance | 9 conventions checked | 0 violations |
| Provides/consumes pairs | 6 verified | 0 failures |
| Sign/factor spot-checks | 3 equations tested | 0 errors |
| Approximation validity | Checked | No new approximations |
| Cross-phase error patterns | 5 patterns checked | 0 instances |
| Dimension chain | Verified | 1 minor cosmetic issue (codimension formula simplification in Step 13) |

**Overall status: CONSISTENT**

The single minor finding (cosmetic codimension algebra in derivation Step 13) does not affect any claimed result or downstream computation. The numerical value 262 = 272 - 10 is correct throughout.

---

_Generated: 2026-03-23_
_Checker: gpd-consistency-checker (rapid mode)_
_Phase: 15-first-order-condition-algebra-identification_
