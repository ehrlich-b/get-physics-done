---
phase: 48-equivariance-and-lorentz-subgroup
verified: 2026-04-12T23:00:00Z
status: passed
score: 7/7 contract targets verified (1 partial by design)
consistency_score: 12/12 physics checks passed
independently_confirmed: 10/12 checks independently confirmed
confidence: high
comparison_verdicts:
  - subject_kind: claim
    subject_id: claim-stabilizer-dim
    reference_id: ref-phase46
    comparison_kind: benchmark
    verdict: pass
    metric: "exact_integer_dimension"
    threshold: "SVD gap > 1e-8"
  - subject_kind: claim
    subject_id: claim-10x10-rep
    reference_id: ref-phase47
    comparison_kind: benchmark
    verdict: pass
    metric: "antisymmetry_error"
    threshold: "< 1e-14"
  - subject_kind: claim
    subject_id: claim-lorentz-embedding
    reference_id: ref-baez
    comparison_kind: benchmark
    verdict: partial
    metric: "rotation_subalgebra_only"
    threshold: "so(3) not so(3,1)"
    notes: "Compact Spin(9) admits only so(3) (rotations), not full so(3,1) (rotations+boosts). This is correct physics, not a failure. Baez 2002 SL(2,K)=Spin(dim(K)+1,1) describes the non-compact completion."
suggested_contract_checks: []
---

# Phase 48 Verification: Equivariance and Lorentz Subgroup

**Phase goal:** The full stabilizer of u in Spin(9) is identified, SL(2,C_u) = Spin(3,1) is verified as the Lorentz subgroup acting on h_2(C_u), and pi_u equivariance under this subgroup is established.

**Verified:** 2026-04-12 | **Status:** passed | **Confidence:** HIGH

**Key finding:** The phase goal is achieved with one important refinement: the stabilizer spacetime block is so(3) (3 rotations), the maximal compact subalgebra of so(3,1), rather than the full so(3,1). This is mathematically necessary since Spin(9) is compact and cannot contain non-compact SL(2,C). The execution correctly identified this, marked the Lorentz embedding claim as PARTIAL, and provided precise framing. All other claims are fully verified.

---

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-10x10-rep | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 36 generators, antisymmetry 2.2e-16, closure residual 0, traceless exact |
| claim-stabilizer-dim | claim | VERIFIED | INDEPENDENTLY CONFIRMED | dim=18, SVD gap=0.71, closure residual 5.3e-17 |
| claim-stabilizer-structure | claim | VERIFIED | INDEPENDENTLY CONFIRMED | so(3)+so(6), Killing=-0.5*I_3 and -2*I_15, center dim=0 |
| claim-lorentz-embedding | claim | PARTIAL (by design) | INDEPENDENTLY CONFIRMED | so(3) only (3 gens), not so(3,1) (6 gens); eta-compatibility verified |
| claim-internal-so6 | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 15 generators, Killing negative definite, all eigenvalues=-2.0 |
| claim-equivariance | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 180 basis tests + 1800 random tests, max err 1.4e-16 |
| claim-mixing-identification | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 18 mixing gens, stab+coset rank=36 |

**Note on PARTIAL status of claim-lorentz-embedding:** The contract predicted "so(3,1) = sl(2,C)_R with exactly 6 generators (3 rotations + 3 boosts)." The computation found only 3 generators (rotations). This is the correct physical result: compact Spin(9) cannot contain non-compact boosts. The execution correctly identified and documented this, so the PARTIAL status reflects an updated physical understanding, not an error.

---

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| code/octonion_algebra.py: compute_spin9_v0_rep | Function returning 36 10x10 generators | VERIFIED | Lines 2662-2716, returns dict with generators, labels, T_flat, ortho basis |
| code/octonion_algebra.py: compute_v0_stabilizer | Function returning stabilizer classification | VERIFIED | Lines 2719-2930, returns 14-field dict with full classification |
| code/octonion_algebra.py: verify_lorentz_equivariance | Function with Lorentz/equivariance checks | VERIFIED | Lines 2933-3134, returns 18-field dict with complete analysis |
| derivations/48-lorentz-equivariance.tex | LaTeX summary of results | VERIFIED | 271 lines, complete with theorem statements, verification data, references |

---

## Computational Verification Details

### Spot-Check Results

All spot-checks performed by independently running the code functions.

| Expression | Test Point | Computed | Expected | Match |
|------------|-----------|----------|----------|-------|
| Number of generators | C(9,2) | 36 | 36 | PASS |
| Antisymmetry (ortho basis) | max\|M+M^T\| | 2.22e-16 | < 1e-14 | PASS |
| Tracelessness | max\|Tr(M)\| | 0.00e+00 | < 1e-14 | PASS |
| Lie algebra closure | 100 random brackets | 0.00e+00 | < 1e-12 | PASS |
| Stabilizer dimension | SVD nullspace | 18 | integer | PASS |
| SVD gap | gap between null/non-null | 0.7071 | > 1e-8 | PASS |
| Off-diagonal blocks | max\|M[S,I]\| | 5.15e-17 | < 1e-14 | PASS |
| Killing form (so(3)) | eigenvalues | -0.5, -0.5, -0.5 | all < 0 | PASS |
| Killing form (so(6)) | eigenvalues | -2.0 (x15) | all < 0 | PASS |
| Equivariance | 18x10 basis tests | 5.15e-17 | < 1e-14 | PASS |
| Cross-brackets | max\|[so(3),so(6)]\| | 5.31e-17 | < 1e-14 | PASS |
| G_SM contained | lstsq residual | 4.85e-15 | < 1e-10 | PASS |

### Limiting Cases Re-Derived

| Limit | Parameter | Expression Limit | Expected | Agreement | Confidence |
|-------|-----------|-----------------|----------|-----------|------------|
| Invariant subspace | All 36 generators on e_0 | max\|M@e_0\| = 0 | e_0 is singlet | PASS | INDEPENDENTLY CONFIRMED |
| 9-dim irrep | Restrict to e_1..e_9 | rank = 36, faithful so(9) | V_0 = 1+9 under so(9) | PASS | INDEPENDENTLY CONFIRMED |
| Stabilizer of 3+6 in so(9) on R^9 | SVD of constraint | dim = 18 | S(O(3)xO(6)) = so(3)+so(6) | PASS | INDEPENDENTLY CONFIRMED |
| Grassmannian dimension | 36 - 18 | 18 | dim Gr(3,9) = 3x6 = 18 | PASS | INDEPENDENTLY CONFIRMED |

### Cross-Checks Performed

| Result | Primary Method | Cross-Check Method | Agreement |
|--------|---------------|-------------------|-----------|
| Killing form eigenvalue -0.5 (so(3)) | Code computation | Hand calculation: Tr(ad(J_0)^2) from structure constants | EXACT MATCH |
| Killing form ratio so(6)/so(3) = 4 | Code eigenvalues | Normalization analysis: (1/2)^2 rescaling from gamma_ab/4 | CONSISTENT |
| Jacobi identity | Code (full 10x10) | Independent: [A,[B,C]]+cyc = 0 | max error 0.00e+00 |
| Rotation generators (Minkowski) | Code | Comparison with derivation Eq.(3) matrices | EXACT MATCH |
| Commutation relations | Code structure constants | Comparison with derivation Eq.(4) | EXACT MATCH |
| No boosts in spin(9) | Spacetime block rank = 3 | Scan all 36 generators for time-space mixing: 0 found | CONFIRMED |
| Equivariance | 180 basis tests | 1800 random vector tests | max err 1.4e-16 |

### Intermediate Result Spot-Checks

| Step | Intermediate Expression | Independent Result | Match |
|------|------------------------|-------------------|-------|
| V_0 Gram matrix | B^T @ eta @ B | diag(0.25, -0.25, -1, -1) | EXACT |
| Minkowski basis inverse | np.linalg.inv(B) | Manual: B_inv = [[2,0,0,0],[0,0,0,2],[0,1,0,0],[0,0,1,0]] | EXACT |
| Commutator bracket | B@(L0_S@L1_S - L1_S@L0_S)@B_inv | Direct J[0]@J[1]-J[1]@J[0] | EXACT |

### Dimensional Analysis Trace

| Equation | Location | LHS Dims | RHS Dims | Consistent |
|----------|----------|----------|----------|------------|
| [gamma_ab/4, T_c] = sum M_dc T_d | Eq.(1) derivation | [16x16 matrix] | [16x16 matrix] | YES |
| L_mink = B L_S B^{-1} | Eq.(2) derivation | [4x4 matrix] | [4x4 matrix] | YES |
| eta L + L^T eta = 0 | Eq.(5) derivation | [4x4 matrix] | [4x4 matrix] | YES |
| P_S(L.Y) = L_S(P_S.Y) | Eq.(6) derivation | [R^4 vector] | [R^4 vector] | YES |

All quantities are dimensionless (pure algebra), so dimensional analysis reduces to matrix-size consistency, which is verified.

---

## Physics Consistency

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All matrices have correct sizes; dimensionless algebra |
| 5.2 | Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | All 12 spot-checks pass (see table above) |
| 5.3 | Limiting cases | PASS | INDEPENDENTLY CONFIRMED | 4 limits independently re-derived (see table above) |
| 5.4 | Independent cross-check | PASS | INDEPENDENTLY CONFIRMED | 7 cross-checks performed (see table above) |
| 5.5 | Intermediate spot-check | PASS | INDEPENDENTLY CONFIRMED | 3 intermediate results verified (see table above) |
| 5.6 | Symmetry | PASS | INDEPENDENTLY CONFIRMED | Antisymmetry, eta-compatibility, Killing form symmetry all verified |
| 5.7 | Conservation / closure | PASS | INDEPENDENTLY CONFIRMED | Lie bracket closure: 153 brackets, max residual 5.3e-17 |
| 5.8 | Math consistency | PASS | INDEPENDENTLY CONFIRMED | Jacobi identity 0.0, dimension accounting 3+15=18, 18+18=36 |
| 5.9 | Numerical convergence | N/A | -- | Pure algebra (exact arithmetic modulo floating point) |
| 5.10 | Literature agreement | PASS | INDEPENDENTLY CONFIRMED | Baez SL(2,K) framework consistent; so(3) is maximal compact of so(3,1) |
| 5.11 | Physical plausibility | PASS | INDEPENDENTLY CONFIRMED | Compact stabilizer, negative-definite Killing form, correct Grassmannian |
| 5.14 | Algebraic structure | PASS | INDEPENDENTLY CONFIRMED | Killing form = -0.5*I_3 (so(3)) and -2*I_15 (so(6)), cross-brackets zero |

**Gate A (Catastrophic cancellation):** No cancellation issues. All results are exact integers or ratios (18, 36, 3, 15, -0.5, -2.0). Floating-point errors are at machine epsilon level (1e-16 to 1e-17).

**Gate B (Analytical-numerical cross-validation):** The derivation Eq.(3) rotation generator matrices match the code output exactly. The commutation relations Eq.(4) match exactly.

**Gate C (Integration measure):** N/A -- no coordinate transformations requiring Jacobians. The basis change B is a linear transformation correctly applied as B@L@B_inv.

**Gate D (Approximation validity):** No approximations used. All results are from exact linear algebra (SVD, lstsq, eigenvalue decomposition) with floating-point arithmetic.

---

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence |
|----------|--------|----------|
| fp-spin9-so9 | REJECTED | Code discusses spin(9) Lie algebra throughout; double cover noted |
| fp-approximate-dim | REJECTED | SVD gap 0.71; dimension exactly 18 |
| fp-abstract-branching | REJECTED | All results from explicit 10x10 matrix computations |
| fp-non-compact-embedding | REJECTED | Derivation Remark 2 explicitly addresses compact/non-compact; summary marks PARTIAL |
| fp-stabilizer-confusion | REJECTED | V_0 stabilizer (dim 18) vs V_{1/2} stabilizer (dim 8) distinguished; G_SM containment verified |
| fp-incomplete-equivariance | REJECTED | All 18 generators x all 10 basis vectors checked (180 tests) + 1800 random tests |
| fp-ignoring-extra-stabilizer | REJECTED | so(6) internal and 18 mixing generators fully classified |

---

## Comparison Verdict Ledger

| Subject ID | Comparison kind | Verdict | Threshold | Notes |
|------------|----------------|---------|-----------|-------|
| claim-stabilizer-dim | benchmark (Phase 46) | PASS | exact integer | dim=18, SVD gap=0.71 |
| claim-10x10-rep | benchmark (Phase 47) | PASS | error < 1e-14 | 36 generators verified |
| claim-lorentz-embedding | benchmark (Baez 2002) | PARTIAL | so(3,1) expected | Only so(3) embeds in compact Spin(9); correct physics |
| claim-internal-so6 | benchmark (Krasnov 2019) | PASS | G_SM subset verified | G_SM (dim 8) subset of so(6) (dim 15) with residual 4.85e-15 |

---

## Discrepancies Found

| Severity | Location | Computation Evidence | Root Cause | Suggested Fix |
|----------|----------|---------------------|------------|---------------|
| INFO | Plan 01 dimensional_check predicted stabilizer_dim=21 | Actual dim=18 | so(3,1) is non-compact; only so(3) (dim 3) embeds in compact Spin(9) | Prediction was noted as uncertain; execution correctly reported actual value |
| INFO | Plan 02 predicted lorentz_dim=6, internal_dim=15, mixing_dim=15 | Actual: rotation_dim=3, internal_dim=15, mixing=18 | Same root cause as above | Execution correctly updated all dimensions |

These are not errors in the execution -- they are corrections to pre-execution predictions. The execution handled them correctly by reporting actual values and providing physical explanations.

---

## Requirements Coverage

| Requirement | Status | Evidence |
|-------------|--------|---------|
| ALGB-03 (Stabilizer + Lorentz identification) | SATISFIED | Stabilizer fully classified; rotation subalgebra identified as maximal compact subalgebra of so(3,1); equivariance proved |

---

## Anti-Patterns Found

No anti-patterns detected. Code is clean, documented, and free of TODOs/placeholders/hardcoded values. All functions have proper docstrings with convention assertions.

---

## Expert Verification Required

None. All claims are computationally verified to machine precision. The physical interpretation (so(3) = maximal compact subalgebra of so(3,1), boosts absent from compact embedding) is standard Lie group theory.

---

## Confidence Assessment

**Overall: HIGH**

All key results are independently confirmed by running the code, performing cross-checks, and re-deriving intermediate steps. The computational verification is exhaustive:

- 36 generators verified (antisymmetry, tracelessness, closure)
- 18-dimensional stabilizer found via SVD with clear gap (0.71)
- Direct sum so(3) + so(6) confirmed by Killing form analysis (-0.5*I_3 and -2*I_15)
- Cross-brackets [so(3), so(6)] = 0 verified (max 5.3e-17)
- Equivariance verified for all 180 generator-basis pairs + 1800 random tests
- Rotation generators match derivation document exactly (matrices and commutation relations)
- Eta-compatibility verified (max error 2.2e-16)
- G_SM containment verified (residual 4.85e-15)
- V_0 = 1 + 9 decomposition independently discovered and verified
- Coset space dimension matches Gr(3,9) = 18
- Killing form normalization ratio consistent with gamma_ab/4 convention

The only "discrepancy" with the phase goal (so(3) instead of so(3,1)) is correct physics that was properly handled by the execution. The phase goal as literally stated ("SL(2,C_u) = Spin(3,1) is verified as the Lorentz subgroup") is partially met: the rotation subalgebra SU(2) of SL(2,C) is verified; the full SL(2,C) cannot embed in compact Spin(9). This is documented accurately in both the summary and derivation.
