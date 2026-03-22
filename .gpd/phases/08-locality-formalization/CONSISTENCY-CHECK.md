# Phase 08 Consistency Check

**Phase:** 08-locality-formalization (Plans 01-03)
**Mode:** rapid
**Date:** 2026-03-22
**Checker:** gpd-consistency-checker

## Conventions Self-Test

Phase 08 introduces new conventions (natural units, metric (-,+,+,+), lattice spacing a_lat=1) atop the existing algebraic conventions from Phases 04-06. The CONVENTIONS.md file covers the project's original information-theoretic and Markov-process conventions but does NOT yet include the lattice/QFT conventions introduced in Phase 08 (part of milestone v3.0). This is flagged below.

| Self-Test | Result |
|-----------|--------|
| Convention lock in state.json vs CONVENTIONS.md | CONVENTIONS.md covers v1-v2 conventions only; Phase 08 conventions in SUMMARY frontmatter are consistent with state.json convention_lock |
| Cross-convention compatibility (metric + Heisenberg picture) | O(t) = e^{iHt}Oe^{-iHt} with [A,B] = AB - BA gives dO/dt = i[H,O]. Standard physics convention. PASS |
| Coupling convention consistency | H = sum h_xy (no 1/2 factor) stated in state.json, all derivation files, and code. PASS |

**Self-test verdict: PASS** (with advisory on convention ledger update needed)

## Provides/Consumes Verification

### Transfer 1: Phase 05-01 -> Phase 08-01

| Field | Value |
|-------|-------|
| **Quantity** | M_n(C)^sa per site, local tomography, composite OUS with product-form SP |
| **Producer meaning** | EJA classification forces state space to be M_n(C)^sa; composite V_BM has dim = dim(V_B) * dim(V_M); product-form SP: (a tensor b) & (c tensor d) = (a & c) tensor (b & d) with Luders product a & c = a^{1/2}ca^{1/2} |
| **Consumer meaning** | Local algebra A_x = M_n(C) per lattice site; product-form SP defines the coupling channel between adjacent sites; composite OUS axioms C1-C4 constrain the interaction Hamiltonian |
| **Meaning match** | YES -- Phase 08 correctly identifies A_x^sa = M_n(C)^sa as the EJA output of Phase 05, and uses the product-form SP as the structural input for deriving h_xy |
| **Units match** | YES -- both phases work with dimensionless algebraic quantities (OUS elements, effects). Phase 08 introduces an energy scale J for the Hamiltonian, which is new (not transferred). |
| **Test value** | dim(V_x) = n^2 = 4 for n=2. Phase 05: dim(V_BM) = 4*4 = 16. Phase 08: dim(A_{xy}^sa) = 16. MATCH. |
| **Convention match** | YES -- sequential product notation (a & b), composite product ((a tensor b) & (c tensor d) = (a & c) tensor (b & d)), Luders product (a^{1/2}ca^{1/2}), axiom source (vdW arXiv:1803.11139 exclusively) all consistent. |
| **Status** | OK |

### Transfer 2: Phase 08-01 -> Phase 08-02

| Field | Value |
|-------|-------|
| **Quantity** | h_xy = JF (SWAP interaction), ||h_xy|| = |J|, nearest-neighbor support |
| **Producer meaning** | The interaction Hamiltonian derived from diagonal U(n) covariance + Schur-Weyl duality; SWAP operator F satisfies F^2 = 1, ||F|| = 1 |
| **Consumer meaning** | Input to NS LR bound framework: ||Phi||_a requires ||h_xy|| = J and nearest-neighbor support |
| **Meaning match** | YES |
| **Units match** | YES -- [||h_xy||] = [J] = [energy] in both phases |
| **Test value** | ||h_xy|| = J = 1 (setting J=1). Producer: ||JF|| = |J| * ||F|| = 1. Consumer: used as J in ||Phi||_a = zJe^a = 2*1*e = 5.437. MATCH. |
| **Convention match** | YES -- natural units (hbar=1), coupling convention (H = sum h_xy), lattice spacing (a_lat=1) |
| **Status** | OK |

### Transfer 3: Phase 08-02 -> Phase 08-03

| Field | Value |
|-------|-------|
| **Quantity** | NS LR bound framework: C_a, ||Phi||_a, v_LR formulas |
| **Producer meaning** | General LR velocity formula v_LR(a) = 2*||Phi||_a * C_a / a with C_a = (coth(a/2))^d - 1 |
| **Consumer meaning** | Applied to self-modeling Hamiltonian (||h_xy|| = J, z neighbors) to compute v_LR for Z^1, Z^2, Z^3 |
| **Meaning match** | YES |
| **Units match** | YES -- [v_LR] = [J] = [energy] = [1/time] in natural units with a_lat=1 |
| **Test value** | Z^1, a=1: C_a = 2/(e-1) = 1.1640, ||Phi||_a = 2*J*e = 5.4366, v_LR = 8eJ/(e-1) = 12.6558. Producer and consumer agree to machine precision. MATCH. |
| **Convention match** | YES |
| **Status** | OK |

### Provides/Consumes Summary

| Quantity | Producer | Consumer | Meaning | Units | Test Value | Convention | Status |
|----------|----------|----------|---------|-------|------------|------------|--------|
| M_n(C)^sa + LT + SP | Phase 05-01 | Phase 08-01 | YES | YES | PASS | YES | OK |
| h_xy = JF, ||h_xy|| | Phase 08-01 | Phase 08-02 | YES | YES | PASS | YES | OK |
| C_a, ||Phi||_a, v_LR | Phase 08-02 | Phase 08-03 | YES | YES | PASS | YES | OK |

**All 3 transfers verified. No issues.**

## Convention Compliance Matrix

### Relevant canonical conventions (18 types)

| # | Convention | Introduced | Relevant to Phase 08? | Compliant? | Evidence |
|---|-----------|-----------|----------------------|------------|----------|
| 1 | Metric signature | Phase 08 (new) | Marginally -- used only in ASSERT headers, not in equations | YES | (-,+,+,+) declared but not exercised; no Minkowski-space calculations in Phase 08 |
| 2 | Fourier convention | N/A | NO | N/A | No Fourier transforms in Phase 08 |
| 3 | Natural units | Phase 08 (new) | YES | YES | hbar=c=k_B=1 used consistently; [H_Lambda t] = dimensionless; [v_LR] = [J] = energy |
| 4 | Gauge choice | N/A | NO | N/A | No gauge theory |
| 5 | Regularization scheme | N/A | NO | N/A | No regularization |
| 6 | Renormalization scheme | N/A | NO | N/A | No renormalization |
| 7 | Coordinate system | Phase 08 (new) | YES | YES | Lattice sites indexed by graph vertices; Manhattan distance d(x,y) = ||x-y||_1 on Z^d |
| 8 | Spin basis | N/A | NO | N/A | Working with M_n(C)^sa, not spin basis |
| 9 | State normalization | Phase 04 | YES | YES | Tr(rho) = 1 used in C3 verification (product states) |
| 10 | Coupling convention | Phase 04/08 | YES | YES | H = sum h_xy (no 1/2 factor) consistent with state.json and all derivation files |
| 11 | Index positioning | N/A | NO | N/A | No tensor index gymnastics |
| 12 | Time ordering | N/A | NO | N/A | No time-ordered products |
| 13 | Commutation convention | Phase 04 | YES | YES | [A,B] = AB - BA used in LR bound and Heisenberg evolution |
| 14 | Levi-Civita sign | N/A | NO | N/A | Not used |
| 15 | Generator normalization | N/A | NO | N/A | Not used |
| 16 | Covariant derivative sign | N/A | NO | N/A | Not used in Phase 08 (lattice, no covariant derivatives) |
| 17 | Gamma matrix convention | N/A | NO | N/A | Not used |
| 18 | Creation/annihilation order | N/A | NO | N/A | Not used |

### Custom conventions

| Convention | Introduced | Relevant? | Compliant? | Evidence |
|-----------|-----------|-----------|------------|----------|
| Sequential product: a & b | Phase 04 | YES | YES | Used consistently in all derivation files; Luders product a^{1/2}ba^{1/2} |
| Jordan product: a * b = (1/2)(a & b + b & a) | Phase 04 | YES | YES | Referenced in correlation form B(a,b) = tau(a * phi^{-1}(b)) |
| Composite product: (a tensor b) & (c tensor d) = (a & c) tensor (b & d) | Phase 05 | YES | YES | Used in locality mapping proof and Paper 5 compatibility verification |
| Local tomography: dim(V_BM) = dim(V_B) * dim(V_M) | Phase 05 | YES | YES | Verified in 08-03: dim(V_xy) = 16 = 4*4 |
| Axiom source: vdW arXiv:1803.11139 EXCLUSIVELY | Phase 04 | YES | YES | All SP axiom references cite vdW |

## Convention Evolution

### New conventions introduced in Phase 08

Phase 08 introduces several new conventions that were previously marked N/A in the convention lock:

1. **Natural units (hbar = c = k_B = 1)**: New for this milestone (v3.0). Previous phases (v1-v2) used dimensionless algebraic quantities where units were irrelevant. Now energy and time scales appear via the Hamiltonian.

2. **Metric signature (-,+,+,+)**: Declared in ASSERT headers but not exercised in any equation. This is forward-looking for Phase 10 (Jacobson/continuum limit).

3. **Lattice spacing a_lat = 1**: New physical convention. Makes graph distance dimensionless.

4. **Heisenberg picture sign convention**: O(t) = e^{iHt} O e^{-iHt}. Standard physics convention giving dO/dt = i[H,O].

**Assessment:** These convention introductions are legitimate (new physical content in v3.0 that was not present in v1-v2). However, they should be documented in CONVENTIONS.md and convention_lock in state.json for downstream phases to reference.

**Impact:** LOW -- the new conventions do not conflict with existing ones (which were all N/A for the relevant categories). But failing to update the ledger risks silent convention drift in Phases 09-12.

## Cross-Phase Error Pattern Checks

### 5a. Sign conventions absorbed into definitions

**Check:** The Hamiltonian uses O(t) = e^{iHt}Oe^{-iHt} (Heisenberg picture). The SWAP operator F has eigenvalues +1 (symmetric, dim 3) and -1 (antisymmetric, dim 1). For J > 0 (AFM): ground state energy = -J (singlet). For J < 0 (FM): ground state energy = -|J| (triplet).

**Verified:** The sign convention is internally consistent. e^{iJFt} at t = pi/(2J) gives the full SWAP: e^{iJFt}(c tensor d)e^{-iJFt} = d tensor c. Numerically verified to 5.9e-17.

**No sign absorption errors detected.**

### 5b. Normalization factors

**Check:** Phase 08 uses F = (1/2)(I + sigma.sigma) and h_xy^int = (J/2)*sigma.sigma. The relationship JF = (J/2)*I + (J/2)*sigma.sigma is exact. Dropping the constant (J/2)*I gives h_xy^int = (J/2)*sigma.sigma.

**Verified numerically:** ||JF - (h_int + (J/2)I)|| = 0 exactly. No normalization factor errors.

### 5c. Implicit assumptions becoming explicit constraints

**Check:** Phase 05 derives local tomography under the minimality assumption (V_BM is the minimal OUS). Phase 08 uses this in the lattice setting. The minimality assumption is explicitly acknowledged in both phases and in STATE.md blockers.

Phase 08 introduces additional assumptions:
- Time-independent Hamiltonian (not Lindbladian)
- Nearest-neighbor truncation is exact
- Sign of J undetermined

All three are explicitly documented in uncertainty_markers. No silent assumption violations.

### 5d. Coupling constant convention

**Check:** H = sum h_xy (no 1/2 factor). The interaction h_xy = JF has ||h_xy|| = |J|. The LR velocity is v_LR = 2z||Phi||_a C_a / a where ||Phi||_a = zJe^a.

**Verified:** The coupling convention H = sum h_xy (not (1/2)*sum) is stated consistently in:
- state.json convention_lock
- 08-01-SUMMARY.md conventions
- 08-02-SUMMARY.md conventions
- 08-03-SUMMARY.md conventions
- derivations/08-lattice-definition.md (Definition 6)
- derivations/08-lr-framework.md (Section 9)
- derivations/08-lr-self-modeling.md (Part G)

No coupling convention mismatch.

### 5e. Factor-of-2pi conventions

**Not applicable.** No Fourier transforms or momentum-space quantities in Phase 08.

## Spot-Check: Load-Bearing Equations

### Eq. (08.1): h_xy = alpha*1 + J*F

**Downstream references:** Used in Plans 08-02, 08-03, and will be used in Phases 09, 10, 11.

**Test value:** For J=1, n=2: h_xy^int = F = SWAP matrix (diagonal entries 1, off-diagonal entries 1 in the |01><10| and |10><01| positions). Eigenvalues: {+1, +1, +1, -1}. ||h_xy^int|| = 1. VERIFIED NUMERICALLY.

### Eq. (08-02.3): v_LR(a) = 2zJe^a[coth(a/2)^d - 1]/a

**Downstream references:** Core result for Phase 09 (area law) and Phase 10 (Jacobson).

**Test value:** Z^1, a=1, J=1: v_LR = 8e/(e-1) = 12.6558. VERIFIED to machine precision (formula and direct computation agree to < 1e-12).

**Limiting cases:**
- J -> 0: v_LR -> 0. PASS (no interaction = no propagation).
- v_LR(2J) = 2*v_LR(J). PASS (linear in J, as expected from ||Phi||_a proportional to J).

### Eq. (08-03.4): Full LR bound

**Test value:** C_LR = 2/C_1 = 2*(e-1)/2 = e-1 = 1.718. mu_LR = a = 1. v_LR = 12.66J. All dimensionless/energy-dimensioned as appropriate. VERIFIED.

## Approximation Validity

No active approximations in STATE.md. Phase 08 introduces no approximations -- all results are exact (algebraic classification, operator norm computation, LR bound as rigorous upper bound).

The one physical approximation (nearest-neighbor truncation) is acknowledged as an unvalidated assumption in uncertainty_markers.

## Issues Found

### Issue 1 (ADVISORY): CONVENTIONS.md not updated for Phase 08 conventions

**Severity:** Low (advisory, not blocking)

**Detail:** Phase 08 introduces natural units (hbar=c=k_B=1), metric signature (-,+,+,+), lattice spacing (a_lat=1), and Heisenberg picture convention (e^{iHt}Oe^{-iHt}). These are declared in derivation file ASSERT_CONVENTION headers and SUMMARY frontmatter, but CONVENTIONS.md still reflects only the v1-v2 information-theoretic conventions.

**Impact:** Downstream phases (09-12) need to reference these conventions. Without a ledger update, convention drift risk increases.

**Recommended fix:** Update CONVENTIONS.md with a "Lattice/Continuum Conventions" section covering the Phase 08 introductions, including test values.

### Issue 2 (NOTE): Minor text inconsistency in code docstring

**Severity:** Cosmetic (not blocking)

**Detail:** In `code/self_modeling_hamiltonian.py` line 12 and line 65, the docstring says "U(n) x U(n) covariance" but the derivation corrected this to "diagonal U(n) covariance" (the U(n) x U(n) -> diagonal U(n) correction is the auto-fixed deviation documented in 08-01-SUMMARY). The code itself is correct (implements diagonal U(n) invariance), only the docstring text was not updated.

**Impact:** None on correctness. Could cause confusion if someone reads only the docstring.

## Summary

**Provides/Consumes pairs verified:** 3 total
- Meaning match: 3/3
- Units match: 3/3
- Test-value pass: 3/3
- Convention match: 3/3
- Failed transfers: 0

**Convention compliance (all phases in scope):**
- Active conventions checked: 8 (of 18 canonical + 5 custom)
- Compliant: 8/8
- Violated: 0
- Not applicable: 13 (correctly identified as irrelevant)

**Convention evolution:**
- New conventions introduced: 4 (natural units, metric, lattice spacing, Heisenberg picture)
- Properly documented in derivation headers: YES
- Updated in CONVENTIONS.md: NO (advisory issued)

**Cross-phase error patterns:**
- Sign absorbed into definition: 0 instances
- Normalization factor change: 0 instances
- Implicit assumption violated: 0 instances
- Coupling convention mismatch: 0 instances
- Factor of 2pi error: N/A

**Load-bearing equations spot-checked:** 3
- All pass test-value verification to machine precision

**Approximation validity:** No violations (no active approximations)

---

_Consistency check performed: 2026-03-22_
_Mode: rapid (post-phase)_
_Phase checked: 08-locality-formalization (Plans 01-03)_
