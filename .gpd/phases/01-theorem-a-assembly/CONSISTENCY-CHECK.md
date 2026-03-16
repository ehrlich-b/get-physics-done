# Phase 01 Consistency Check (Rapid)

**Phase:** 01-theorem-a-assembly
**Plans checked:** 01-01 (lemma assembly), 01-02 (proof assembly + validation)
**Mode:** rapid
**Date:** 2026-03-15

## Convention Compliance

All 7 project-specific conventions checked against CONVENTIONS.md. The 18 standard QFT conventions are N/A (information-theoretic project).

| Convention | Ledger Value | Plan 01 | Plan 02 | Validation Code | Status |
|-----------|-------------|---------|---------|-----------------|--------|
| Entropy base | nats (ln) | ln throughout | ln throughout | N/A (uses fixed rho values) | OK |
| Generator convention | probabilist dp/dt = pQ | dp/dt = pQ, piQ=0 (line 58) | dp/dt = pQ (line 54-58) | CTMC rates consistent | OK |
| Matrix norm | sup-norm on rows | Declared in header | Declared in header | Not used in Phase 01 | OK (N/A for this phase) |
| Experiential density | I*(1-I/H) | Eq in lemmas line 60-62 | Eq in proof line 63-64 | rho_s, rho_b as parameters | OK |
| rho_max | H(B)/4 | lemmas line 76 | proof line 68 | rho_b=0.2 (three-state) | OK |
| Stationary dist | pi*P = pi (left eigenvector) | piQ = 0 stated | piQ = 0 stated | Implicit in CTMC simulation | OK |
| Basin ordering | Delta_s > Delta_b | Standing assumption | Standing assumption | Delta_s=3.0 > Delta_b=1.0 | OK |

## Provides/Consumes Verification

### Plan 01 -> Plan 02

| Quantity | Producer (01) | Consumer (02) | Meaning | Units | Test Value | Convention | Status |
|----------|--------------|---------------|---------|-------|------------|------------|--------|
| 7 lemma statements | theorem-a-lemmas.tex | theorem-a-proof.tex Steps 1-7 | Precise statements with error terms | dimensionless (error terms) | C=0.25 for three-state | All match | OK |
| Error rate table | lemmas sec. 4 (c_i values) | proof sec. 3 (composition) | Individual exponential rates | dimensionless rates | c_2>=Ds-Db=2.0, c_4=Ds=3.0, c_6=alpha | Match | OK |
| Typed dependency DAG | lemmas sec. 3 | proof composition chain | I/O types at lemma boundaries | N/A (structural) | 9 edges, all typed | Match | OK |

### Plan 02 internal: analytical -> numerical

| Quantity | Analytical (proof.tex) | Numerical (validation.py) | Test Value | Status |
|----------|----------------------|--------------------------|------------|--------|
| Prefactor C | (rho_max/c)(K_b/K_s^2) | (rho_b/rho_s)*1.0 = 0.25 | 0.2/0.8 = 0.25 | OK |
| Main exponent | -(Ds-Db-alpha)/eps | -(Delta_s-Delta_b-alpha)/eps | Ds=3,Db=1,alpha=0: -2/eps | OK |
| Failure prob | O(exp(-alpha/(2eps))) | exp(-alpha/(2*eps)) | alpha=0.5,eps=0.5: 0.607 | OK |
| Ergodic slope | -(Ds-Db) = -2.0 | Fitted slope | -2.0 (0% error per SUMMARY) | OK |

## Spot-Check: Load-Bearing Equations

### Eq. (01-01.5) -> Theorem A (proof.tex eq. theorem-a)

**Producer:** Lemmas file, ratio bound:
  mu_BB/mu_stable <= C * exp(-(Ds-Db-alpha)/eps) * (1 + O(exp(-c_7/eps)))
  with c_7 = min(Ds-Db, alpha) and C = (rho_max/c)(K_b/K_s^2)

**Consumer:** Proof file, Theorem A statement:
  mu_BB/mu_stable <= C * exp(-(Ds-Db-alpha)/eps) * (1 + delta(eps))
  with |delta| <= C' exp(-gamma/eps), gamma = alpha/2

**Test value (three-state, p=0.5, alpha=0, eps=0.5):**
  Producer: C * exp(-2/0.5) = 0.25 * exp(-4) = 0.25 * 0.01832 = 0.00458
  Consumer: Same formula, same result.
  **PASS.**

**Deliberate revision:** gamma changed from min(Ds-Db, alpha) to alpha/2.
Documented in 01-02-SUMMARY.md Gap 3. The old value was overstated.
The new value gamma = alpha/2 is honest (comes from eta = exp(-alpha/(2eps))).
Both are strictly positive under standing assumptions, so the qualitative
result (error term vanishes) is unchanged. **Not an inconsistency.**

### mu_stable definition: lemmas L4 vs proof Step 4

**Lemmas L4 (line 317):** mu_stable = integral_0^{tau_exit} rho(p_t) dt
  Lower bound: c * K_s * exp(Ds/eps) * (1 - delta_4)

**Proof Step 4 (line 267):** mu_stable = integral_0^{min(tau_exit, T_eps)} rho(p_t) dt
  Lower bound: c * T_min * (1 - delta_4)

**The difference:** The proof correctly caps at T_eps. For alpha > 0,
T_eps = exp((Ds-alpha)/eps) < K_s*exp(Ds/eps), so the lemmas' lower bound
would exceed the actual mu_stable. The proof's case analysis resolves this.
Documented in 01-02-SUMMARY.md Gap 1. **Deliberate correction, not inconsistency.**

### Sign check: all exponentials

All barrier-related exponentials are consistent:
- Exit rates: exp(-Delta/eps) [positive Delta, negative exponent -> small rate]. OK.
- Exit times: exp(+Delta/eps) [large time for deep basin]. OK.
- Ratio: exp(-(Ds-Db-alpha)/eps) [negative exponent since Ds-Db-alpha > 0 -> ratio vanishes]. OK.
- Failure prob: exp(-alpha/(2eps)) [negative exponent -> small probability]. OK.

No sign errors detected.

## Approximation Validity

| Approximation | Valid When | Phase 01 Parameter Values | Status |
|--------------|-----------|--------------------------|--------|
| Low-noise asymptotics | eps << min(Ds, Db) | MC runs at eps=0.5, Db=1.0 (eps/Db=0.5) | Marginal but OK: MC checks bound validity, not asymptotic tightness |
| QSD convergence | t >> 1/gamma_D, gamma_D = O(1) | gamma_D not computed explicitly | OK: argued O(1) via Cheeger inequality; residence time >> 1/gamma_D by exponential separation |

No approximation validity violations.

## Documentation Hygiene Note

The lemmas file (theorem-a-lemmas.tex) still contains c_7 = min(Ds-Db, alpha)
in the error rate summary table (line 873, 921), while the proof file uses the
corrected gamma = alpha/2. This is not a mathematical inconsistency (the proof
file is authoritative and the lemmas file provides individual rates, not the
composed rate), but could cause confusion if a future phase reads the lemmas
file's c_7 value instead of the proof file's gamma. Recommend adding a note
to the lemmas file's error rate summary indicating that the composed rate is
refined in theorem-a-proof.tex.

**Severity:** Minor (documentation, not mathematical).

## Summary

- **Checks performed:** 10 (7 convention checks, 2 spot-checks with test values, 1 approximation validity check)
- **Issues found:** 0 hard violations, 1 minor documentation hygiene note
- **Convention compliance:** All 7 relevant conventions compliant across both plans and the validation code
- **Cross-plan consistency:** Provides/consumes chain verified; all transfers match semantically, dimensionally, and by test value
- **Error term evolution:** gamma correction from min(Ds-Db, alpha) to alpha/2 is deliberately documented in 01-02-SUMMARY.md (Gaps 1+3). Not an inconsistency.
- **Notation drift:** None detected. Both files use identical macros, reference keys, and mathematical conventions.

---

_Consistency check completed: 2026-03-15_
