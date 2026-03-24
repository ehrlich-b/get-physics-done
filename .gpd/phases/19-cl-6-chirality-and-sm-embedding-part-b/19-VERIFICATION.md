---
phase: 19-cl-6-chirality-and-sm-embedding-part-b
verified: 2026-03-24T02:00:00Z
status: passed
score: 9/9 contract targets verified
consistency_score: 12/12 physics checks passed
independently_confirmed: 10/12 checks independently confirmed
confidence: high
comparison_verdicts:
  - subject_id: claim-cl6-construction
    subject_kind: claim
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    verdict: pass
    metric: "76 Clifford anticommutation relations"
    threshold: "error < 1e-14"
  - subject_id: claim-volume-form
    subject_kind: claim
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    verdict: pass
    metric: "omega_6^2 = -I, tr(P) = 16, rank(P) = 16"
    threshold: "machine precision"
  - subject_id: claim-pati-salam-breaking
    subject_kind: claim
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    verdict: pass
    metric: "stabilizer dimension 21 = 15 + 6 + 0"
    threshold: "exact"
  - subject_id: claim-furey-witt
    subject_kind: claim
    reference_id: ref-furey-2018
    comparison_kind: prior_work
    verdict: pass
    metric: "27 CAR, omega_6 = -i*(-1)^N"
    threshold: "machine precision"
  - subject_id: claim-16-states
    subject_kind: claim
    reference_id: ref-furey-2018
    comparison_kind: benchmark
    verdict: pass
    metric: "16 SM fermion quantum numbers"
    threshold: "exact match to known SM assignments"
  - subject_id: claim-16-states
    subject_kind: claim
    reference_id: ref-todorov-2022
    comparison_kind: benchmark
    verdict: pass
    metric: "Q distribution {-1:2, -1/3:6, 0:2, +2/3:6}"
    threshold: "exact match"
suggested_contract_checks: []
---

# Phase 19 Verification: Cl(6) Chirality and SM Embedding

**Phase goal:** The octonion splitting O = C + C^3 is shown to induce Cl(6) inside Cl(10), whose volume form selects the chiral (left) SM embedding via the Pati-Salam route, with all 16 SM quantum numbers verified computationally.

**Verified:** 2026-03-24
**Status:** PASSED
**Confidence:** HIGH (10/12 checks independently confirmed via executed code)

---

## 1. Contract Coverage

### Plan 01 Claims (Algebraic Derivation)

| Contract ID | Kind | Status | Confidence | Evidence |
|---|---|---|---|---|
| claim-cl6-construction | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 21 Cl(6) + 55 Cl(10) anticommutator relations verified numerically (error = 0) by verifier-independent code |
| claim-volume-form | claim | VERIFIED | INDEPENDENTLY CONFIRMED | omega_6^2 = -I verified (error = 0); P^2 = P (error = 0); tr(P) = 16; rank(P) = 16; (i*omega_6)^2 = +I (involution) |
| claim-pati-salam-breaking | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Stabilizer computation: 21 bivectors commute with omega_6 (15 internal + 6 external + 0 mixed); 24 anticommute. All verified by verifier code |
| claim-furey-witt | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 27 CAR (error = 0); omega_6 = -i*(-1)^N formula verified to exact precision; P selects odd N (N=1: 12 quarks, N=3: 4 leptons) |

### Plan 02 Claims (Computational Verification)

| Contract ID | Kind | Status | Confidence | Evidence |
|---|---|---|---|---|
| claim-explicit-cl6 | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 32x32 matrices built, all 76 relations verified (error = 0) |
| claim-16-states | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 16 independent states, all eigenstates of Cartan generators with residual = 0, Q distribution matches SM exactly |

### Deliverables

| Deliverable ID | Path | Status |
|---|---|---|
| deliv-cl6-derivation | derivations/12-cl6-chirality.md | VERIFIED -- 14 steps + synthesis, all required elements present |
| deliv-cl6-code | tests/test_cl6_sm.py | VERIFIED -- 29 pytest tests, all passing |
| deliv-quantum-number-table | derivations/12-cl6-chirality.md (Part IV) | VERIFIED -- 16-state table with all quantum numbers |

### Acceptance Tests

| Test ID | Status | Evidence |
|---|---|---|
| test-clifford-relations | PASSED | 21/21 Cl(6) relations, error = 0 |
| test-cl6-in-cl10 | PASSED | 55/55 Cl(10) relations, error = 0 |
| test-volume-form-squared | PASSED | omega_6^2 = -I (error = 0) |
| test-projector-rank | PASSED | tr(P) = 16, rank(P) = 16 |
| test-pati-salam-stabilizer | PASSED | dim = 21 = 15+6+0 |
| test-left-embedding | PASSED | 16 -> (4,2,1) + (4bar,1,2), SU(2)_L on left-handed only |
| test-witt-anticommutators | PASSED | 27/27 CAR, error = 0 |
| test-automatic-chirality | PASSED | omega_6 = -i*(-1)^N verified |
| test-clifford-numerical | PASSED | 76 relations, error = 0 |
| test-omega6-numerical | PASSED | 4/4 conditions |
| test-16-state-match | PASSED | 16 independent, in P-subspace, eigenstates |
| test-quantum-numbers | PASSED | All 16 match SM, Q distribution correct |

### Forbidden Proxies

| Proxy ID | Status | Evidence |
|---|---|---|
| fp-cl6-without-o-splitting | REJECTED | Cl(6) explicitly derived from O = C + C^3 splitting with u = e_7; derivation Step 1-2 traces from octonion splitting to gamma matrices |
| fp-chirality-without-lr-distinction | REJECTED | LEFT embedding explicitly distinguished from diagonal; Sawin theorem cited; SU(2)_L acts on (4,2,1) only |
| fp-quantum-numbers-without-matrices | REJECTED | Every quantum number computed as eigenvalue of 32x32 matrix operator; eigenstate residuals all = 0 |
| fp-quantum-numbers-by-hand | REJECTED | All eigenvalues from explicit matrix computation, not by inspection |
| fp-partial-states | REJECTED | All 16 states verified; 4 leptons + 12 quarks = 16 |

### References

| Reference ID | Required Actions | Status |
|---|---|---|
| ref-todorov-2022 | read, compare, cite | COMPLETED |
| ref-furey-2018 | read, compare, cite | COMPLETED |
| ref-baez-sawin | read, compare, cite | COMPLETED |
| ref-krasnov-2025 | read, cite | COMPLETED |
| ref-phase18 | use | COMPLETED |

---

## 2. Required Artifacts

| Artifact | Expected | Status | Details |
|---|---|---|---|
| derivations/12-cl6-chirality.md | Full derivation + quantum number table | VERIFIED (exists, substantive, integrated) | 14 steps across 4 parts; ~525 lines; ASSERT_CONVENTION present |
| tests/test_cl6_sm.py | NumPy verification code | VERIFIED (exists, substantive, integrated) | 29 tests, all passing; ASSERT_CONVENTION present; ~600 lines |

---

## 3. Computational Verification Details

### 3.1 Spot-Check Results (Independently Executed)

All checks below were performed by the verifier using independently written Python code, not by running the artifact test suite.

| Expression | Test Point | Computed | Expected | Match |
|---|---|---|---|---|
| omega_6^2 | full 32x32 | -I_32 (error = 0) | -I_32 | PASS |
| (i*omega_6)^2 | full 32x32 | +I_32 (error = 0) | +I_32 | PASS |
| P^2 | full 32x32 | P (error = 0) | P | PASS |
| tr(P) | full 32x32 | 16.0 | 16 | PASS |
| rank(P) | full 32x32 | 16 | 16 | PASS |
| omega_6 vs -i*(-1)^N | full 32x32 | error = 0 | 0 | PASS |
| N eigenvalues in P-subspace | 16 eigenvalues | {1:12, 3:4} | {1:12, 3:4} | PASS |
| Q(u_R) | via matrix eigenvalue | +2/3 | +2/3 | PASS |
| Q(e_L) | via matrix eigenvalue | -1 | -1 | PASS |
| Q(nu_L) | via matrix eigenvalue | 0 | 0 | PASS |
| Q(d_R) | via matrix eigenvalue | -1/3 | -1/3 | PASS |

### 3.2 Limiting Cases Re-Derived

**Limit 1: Cl(6) volume form sign.**

Starting from omega_6 = gamma_1...gamma_6, compute omega_6^2:
- Each gamma_k must be moved past 5, 4, 3, 2, 1, 0 other gammas.
- Total transpositions: 5 + 4 + 3 + 2 + 1 + 0 = 15 = 6*5/2.
- Each transposition gives a factor of (-1).
- Each gamma_k^2 = +1.
- omega_6^2 = (-1)^15 = -1.

General formula: omega_n^2 = (-1)^{n(n-1)/2}.
Verified for n = 2,3,4,5,6,7,8 and confirmed n=6 gives -1.

**Confidence:** INDEPENDENTLY CONFIRMED (derived from first principles + numerical verification).

**Limit 2: Cl(6) Witt CAR derivation.**

From a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}):
- {a_i, a_j^dag} = (1/4)({gamma_{2i-1}, gamma_{2j-1}} - i{gamma_{2i-1}, gamma_{2j}} + i{gamma_{2i}, gamma_{2j-1}} + {gamma_{2i}, gamma_{2j}})
- For i=j: (1/4)(2 + 0 + 0 + 2) = 1. For i != j: all Kronecker deltas zero -> 0.
- Verified analytically step-by-step AND numerically (27 relations, error = 0).

**Confidence:** INDEPENDENTLY CONFIRMED.

**Limit 3: Gell-Mann-Nishijima relation.**

For each particle type, independently computed Q = J3L + Y/2 where Y = (B-L) + 2*J3R:
- nu_L: Q = 0.5 + (-1-0)/2 = 0. MATCH.
- e_L: Q = -0.5 + (-1)/2 = -1. MATCH.
- u_L: Q = 0.5 + (1/3)/2 = 2/3. MATCH.
- d_L: Q = -0.5 + (1/3)/2 = -1/3. MATCH.
- nu_R: Q = 0 + 0/2 = 0. MATCH.
- e_R: Q = 0 + (-2)/2 = -1. MATCH.
- u_R: Q = 0 + (4/3)/2 = 2/3. MATCH.
- d_R: Q = 0 + (-2/3)/2 = -1/3. MATCH.

**Confidence:** INDEPENDENTLY CONFIRMED.

### 3.3 Cross-Checks Performed

| Result | Primary Method | Cross-Check Method | Agreement |
|---|---|---|---|
| omega_6^2 = -1 | Analytical (15 transpositions) | Numerical (32x32 matrix) | Exact (error = 0) |
| tr(P) = 16 | Analytical (tr(omega_6) = 0) | Numerical eigenvalue computation | Exact |
| Stabilizer dim = 21 | Analytical (bivector commutation) | Numerical (45 bivector commutators) | Exact (15+6+0 = 21) |
| 16 SM quantum numbers | Algebraic (Witt decomposition) | Matrix eigenvalue computation | All residuals = 0 |
| omega_6 = -i*(-1)^N | Analytical (Step 9 derivation) | Numerical (matrix comparison) | Exact (error = 0) |
| Q = J3L + Y/2 | Algebraic formula | Independent arithmetic per particle | 8/8 particles match |

### 3.4 Dimensional Analysis Trace

This phase is purely algebraic/representation-theoretic (dimensionless quantities). Dimensional consistency reduces to dimension counting:

| Quantity | Expected | Computed | Consistent |
|---|---|---|---|
| dim(Cl(6)) | 2^6 = 64 | 64 | YES |
| dim(Cl(10)) | 2^10 = 1024 | 1024 | YES |
| Dirac spinor dim | 2^(10/2) = 32 | 32 | YES |
| Weyl spinor dim | 32/2 = 16 | 16 | YES |
| dim(SU(4)) | 4^2 - 1 = 15 | 15 | YES |
| dim(SU(2)_L + SU(2)_R) | 3 + 3 = 6 | 6 | YES |
| dim(Pati-Salam) | 15 + 6 = 21 | 21 | YES |
| dim(Spin(10)) | C(10,2) = 45 | 45 | YES |
| Broken generators | 45 - 21 = 24 | 24 (= 6 x 4 mixed) | YES |
| 16 decomposition | 4*2*1 + 4*1*2 = 16 | 8 + 8 = 16 | YES |
| SM gauge group dim | 8 + 3 + 1 = 12 | 12 | YES |
| Cl(6) Witt states | 2^3 = 8 | 8 | YES |
| Cl(4) vacuum states | 32/2^3 = 4 | 4 | YES |
| Total SM states | 4 x (3+1) = 16 | 16 | YES |

**Confidence:** INDEPENDENTLY CONFIRMED (all dimensions computed from first principles).

---

## 4. Physics Consistency Summary

| # | Check | Status | Confidence | Notes |
|---|---|---|---|---|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All dimension counts verified from first principles (see 3.4) |
| 5.2 | Numerical spot-check | PASSED | INDEPENDENTLY CONFIRMED | omega_6^2, P properties, Q values for 8 particle types (see 3.1) |
| 5.3 | Limiting cases | VERIFIED | INDEPENDENTLY CONFIRMED | Volume form sign, CAR derivation, Gell-Mann-Nishijima (see 3.2) |
| 5.4 | Cross-check | PASSED | INDEPENDENTLY CONFIRMED | 6 cross-checks between analytical and numerical methods (see 3.3) |
| 5.5 | Intermediate spot-check | PASSED | INDEPENDENTLY CONFIRMED | omega_6 = -i*(-1)^N formula verified as intermediate result |
| 5.6 | Symmetry | VERIFIED | INDEPENDENTLY CONFIRMED | SU(2)_L x SU(2)_R algebra (6 commutation relations), L-R commutativity (9 cross-commutators), omega_6 commutativity |
| 5.7 | Conservation / structure | VERIFIED | INDEPENDENTLY CONFIRMED | Stabilizer decomposition 15+6+0=21, all 45 bivectors classified |
| 5.8 | Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | Sign of omega_6^2 verified analytically (15 transpositions) and numerically |
| 5.10 | Literature agreement | AGREES | INDEPENDENTLY CONFIRMED | Q distribution {-1:2, -1/3:6, 0:2, +2/3:6} matches Todorov/Furey; hypercharge values match standard SM table |
| 5.11 | Physical plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | All quantum numbers in expected ranges; chirality assignment consistent; 8 left + 8 right; 4 leptons + 12 quarks |
| 5.15 | Anomalies/topology | N/A | -- | No anomaly computation in this phase |
| 5.9 | Convergence | N/A | -- | No iterative computation; all results exact |

### Mandatory Verification Gates

**Gate A (Catastrophic Cancellation):** N/A -- all results are exact integers or simple fractions. No cancellation issues.

**Gate B (Analytical-Numerical Cross-Validation):** PASSED -- every analytical formula (omega_6^2, CAR, stabilizer dimension, quantum numbers) was independently verified by explicit 32x32 matrix computation. Agreement is exact (error = 0 in all cases).

**Gate C (Integration Measure):** N/A -- no coordinate transformations or integrals in this algebraic derivation.

**Gate D (Approximation Validity):** N/A -- no approximations used; all results are exact.

---

## 5. Discrepancies Found

| Severity | Location | Issue | Impact | Suggested Fix |
|---|---|---|---|---|
| WARNING | ROADMAP.md line 138 | States "omega_6^2 = 1" instead of correct "omega_6^2 = -1" | Documentation only -- the derivation, code, and Plan 01 acceptance tests all correctly use omega_6^2 = -1. The projector P = (1/2)(1 - i*omega_6) requires omega_6^2 = -1 for idempotency. | Update ROADMAP success criterion 2 to read "omega_6^2 = -1" instead of "omega_6^2 = 1" |
| WARNING | Plan 01 claim-volume-form statement (line 43 of 19-01-PLAN.md) | Claim statement says "omega_6^2 = 1" but acceptance test correctly says "omega_6^2 = -1" | Documentation inconsistency within Plan 01; the acceptance test and actual derivation are correct | Update claim statement to match acceptance test |
| INFO | state.json convention_lock | gamma_matrix_convention: "N/A" despite Phase 19 introducing gamma matrices | Not a physics error; convention lock was set before Phases 18-19. Phase artifacts have their own ASSERT_CONVENTION lines | Consider updating convention lock to reflect Cl(10) Euclidean positive-definite convention |

---

## 6. Anti-Patterns Found

| Category | Pattern | Status |
|---|---|---|
| Physics | TODO/FIXME/placeholders | None found |
| Physics | Suppressed warnings | None found |
| Physics | Magic numbers | None found |
| Numerical | Division without zero check | Division by norm (lines 250, 261, 280) -- norms are checked to be > 1e-10 before division |
| Derivation | Unjustified approximations | None -- all results exact |

---

## 7. Requirements Coverage

| Requirement | Status | Evidence |
|---|---|---|
| CHIR-01 (Cl(6) from O splitting) | SATISFIED | derivations/12-cl6-chirality.md Steps 1-2; 21 Clifford relations verified |
| CHIR-02 (Volume form and projector) | SATISFIED | omega_6^2 = -1, tr(P) = 16, rank(P) = 16 -- all exact |
| CHIR-03 (Pati-Salam and LEFT embedding) | SATISFIED | Stabilizer dim = 21; 16 -> (4,2,1) + (4bar,1,2) |
| CHIR-04 (Furey Witt automatic chirality) | SATISFIED | 27 CAR; omega_6 = -i*(-1)^N; SU(2)_L in stabilizer |
| COMP-01 (Explicit matrix verification) | SATISFIED | 29 pytest tests, all passing; 32x32 matrices |
| COMP-02 (16 SM quantum numbers) | SATISFIED | All 16 states with correct Q, J3L, J3R, T3c, T8c, B-L, Y |

---

## 8. Confidence Assessment

**Overall: HIGH**

This is among the strongest verifications in the project. The key factors:

1. **Every single result was verified by explicit matrix computation.** The 32x32 matrices leave no room for sign errors, factor errors, or algebraic mistakes. All anticommutator relations, projector properties, and quantum numbers were computed to machine precision (error = 0 in all cases).

2. **The verifier independently wrote and executed code** to reproduce all key results: omega_6^2 = -1, projector properties, stabilizer dimension, quantum number table, Gell-Mann-Nishijima relation, omega_6 = -i*(-1)^N formula. These were not just re-runs of the artifact code.

3. **Complete SM quantum number match.** All 16 states identified with correct electric charge Q, weak isospin I_3, weak hypercharge Y, and color charges. The Q distribution {-1:2, -1/3:6, 0:2, +2/3:6} matches the known Pati-Salam Standard Model assignment exactly.

4. **No approximations.** Every result in this phase is exact (algebraic/representation-theoretic). There are no convergence issues, no truncation errors, no statistical uncertainties.

5. **Multiple cross-checks.** Each key result was verified by at least two independent methods: analytical derivation and numerical matrix computation.

The only issue found is a documentation error in the ROADMAP (omega_6^2 = 1 instead of -1), which does not affect the physics -- the derivation and code correctly use omega_6^2 = -1 throughout.

---

## 9. Computational Oracle Evidence

**Executed code block (verifier-independent):**

```
omega_6^2 + I error: 0.00e+00  (omega_6^2 = -I: CONFIRMED)
omega_6^2 - I error: 2.00e+00  (omega_6^2 != +I)
P^2 - P error: 0.00e+00
tr(P) = 16.0
rank(P) = 16
(i*omega_6)^2 - I error: 0.00e+00  (involution: CONFIRMED)
```

```
Stabilizer of omega_6 in spin(10):
  Internal-internal: 15 (expected 15)
  External-external: 6 (expected 6)
  Mixed in stabilizer: 0 (expected 0)
  Broken generators: 24 (expected 24)
  Total: 45 (expected 45)
```

```
SM content: {'u_L': 3, 'd_L': 3, 'nu_L': 1, 'e_L': 1, 'u_R': 3, 'd_R': 3, 'nu_R': 1, 'e_R': 1}
Q distribution: {+2/3: 6, -1/3: 6, 0: 2, -1: 2}
```

```
omega_6 vs -i*(-1)^N: max error = 0.00e+00
N eigenvalues in P-subspace: {1: 12, 3: 4}
```

All executed via `python3 -c "..."` by the verifier agent, not by the artifact test suite.

---

## 10. ROADMAP Success Criteria Assessment

| # | ROADMAP Criterion | Status | Notes |
|---|---|---|---|
| 1 | Six gamma matrices gamma_1...gamma_6 from Im(C^3), Clifford relations inside Cl(10) | VERIFIED | 21 + 55 relations, all error = 0 |
| 2 | omega_6^2 = 1 [sic], P = (1/2)(1 - i*omega_6) trace 16 | VERIFIED (with correction) | omega_6^2 = -1 (not +1 as ROADMAP states); P trace = 16, rank = 16. The ROADMAP has a typo; the derivation is correct |
| 3 | Pati-Salam as stabilizer of omega_6, LEFT embedding | VERIFIED | dim(stabilizer) = 21 = 15+6; SU(2)_L on (4,2,1) only |
| 4 | Furey Witt: automatic chirality without ad hoc projectors | VERIFIED | 27 CAR; omega_6 = -i*(-1)^N; SU(2)_L in stabilizer |
| 5 | All 16 SM quantum numbers (Y, I_3, color) verified computationally | VERIFIED | 16/16 states identified; Q, Y, I_3, T3c, T8c all match SM |
