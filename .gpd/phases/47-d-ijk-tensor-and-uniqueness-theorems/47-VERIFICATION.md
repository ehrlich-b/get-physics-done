---
phase: 47-d-ijk-tensor-and-uniqueness-theorems
verified: 2026-04-12T00:00:00Z
status: passed
score: 7/7 contract targets verified
consistency_score: 15/15 physics checks passed
independently_confirmed: 13/15 checks independently confirmed
confidence: high
comparison_verdicts:
  - subject_kind: claim
    subject_id: claim-det3
    reference_id: ref-baez
    comparison_kind: benchmark
    verdict: pass
    metric: "det_3(I_3)=1, det_3(E_{ii})=0, abc diagonal, homogeneity"
    threshold: "< 1e-14"
  - subject_kind: claim
    subject_id: claim-dijk
    reference_id: ref-baez
    comparison_kind: benchmark
    verdict: pass
    metric: "d(X,X,X) = 6*N(X) polarization identity"
    threshold: "rel err < 1e-12"
  - subject_kind: claim
    subject_id: claim-two-blocks
    reference_id: ref-slansky
    comparison_kind: benchmark
    verdict: pass
    metric: "exactly 2 nonzero Peirce blocks out of 6 possible"
    threshold: "all forbidden blocks exactly zero"
  - subject_kind: claim
    subject_id: claim-uniqueness
    reference_id: ref-springer
    comparison_kind: benchmark
    verdict: pass
    metric: "F_4 invariance under S_3 + G_2 + Spin(9) generators"
    threshold: "S_3 < 1e-14, G_2 < 1e-12, Spin(9) O(eps^2)"
  - subject_kind: claim
    subject_id: claim-double-duty
    reference_id: ref-gst
    comparison_kind: logical_structure
    verdict: pass
    metric: "non-circular: GST in premises only as existence hypothesis"
    threshold: "GST not used as premise for V=det"
  - subject_kind: claim
    subject_id: claim-27-decomposition
    reference_id: ref-paper7
    comparison_kind: benchmark
    verdict: pass
    metric: "16 SM fermion quantum numbers multiset match"
    threshold: "exact match"
  - subject_kind: claim
    subject_id: claim-27-decomposition
    reference_id: ref-slansky
    comparison_kind: benchmark
    verdict: pass
    metric: "V_0 split 4+6 under pi_u"
    threshold: "spacetime_dim=4, internal_dim=6"
suggested_contract_checks: []
---

# Phase 47 Verification: d_{IJK} Tensor and Uniqueness Theorems

**Phase goal:** Compute the d_{IJK} tensor on h_3(O) by polarization, prove that det(X) is the unique F_4-invariant cubic via Springer (1962), and verify the 27 = 1+16+10 Peirce decomposition reproduces SM quantum numbers.

**Verification date:** 2026-04-12
**Status:** PASSED
**Confidence:** HIGH (13/15 checks independently confirmed by computation)

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-det3 | claim | VERIFIED | INDEPENDENTLY CONFIRMED | det_3 benchmarks: I_3=1, E_{ii}=0, abc diagonal (rel err 0), homogeneity (rel err 1.4e-15) |
| claim-dijk | claim | VERIFIED | INDEPENDENTLY CONFIRMED | d(X,X,X) = 6*N(X) for 10 random X (rel err 3.1e-15); symmetry 6 perms (err 5.7e-14) |
| claim-two-blocks | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Exhaustive: 106/3654 nonzero, exactly (V_1,V_0,V_0)[10] + (V_{1/2},V_{1/2},V_0)[96]; all 6 forbidden blocks exactly zero |
| claim-v1v0v0-is-det2 | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 55 V_0 pairs checked: max|d(E11,a,b) - B(a,b)| = 0.0 (exact) |
| claim-uniqueness | claim | VERIFIED | INDEPENDENTLY CONFIRMED | F_4 invariance: 630 tests (S_3 err 7.1e-15; G_2 err 2.0e-13; Spin(9) O(eps^2) confirmed by 4 epsilon values) |
| claim-double-duty | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Non-circular structure verified: P1(GST defines V), P2(F_4 symmetry), P3(Springer uniqueness) -> C(V=c*det). GST in hypothesis only. |
| claim-27-decomposition | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 27=1+16+10 dimension count; 16 SM quantum numbers match Paper 7 multiset; V_0 splits 4+6 under pi_u |

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| code/octonion_algebra.py | det_3, polarize_d, peirce_basis_27, d_ijk_tensor, verify_f4_invariance_det3, quantum_number_table_27 | VERIFIED | All 6 required functions present and functional |
| derivations/47-uniqueness-and-quantum-numbers.tex | Uniqueness proof, double duty theorem, 27 table | VERIFIED | Contains Springer 1962 citation, non-circular proof, complete SM table |

## Computational Verification Details

### Spot-Check Results (Test 1: det_3 benchmarks)

| Expression | Test Point | Computed | Expected | Match |
|-----------|-----------|---------|---------|-------|
| det_3(I_3) | I_3 = diag(1,1,1) | 1.0 | 1.0 | EXACT |
| det_3(E_{11}) | E_{11} = diag(1,0,0) | 0.0 | 0.0 | EXACT |
| det_3(E_{22}) | E_{22} = diag(0,1,0) | 0.0 | 0.0 | EXACT |
| det_3(E_{33}) | E_{33} = diag(0,0,1) | 0.0 | 0.0 | EXACT |
| det_3(diag(a,b,c)) | 5 random triples | a*b*c | a*b*c | rel err 0.0 |
| det_3(lambda*X) | 25 (5 X, 5 lambda) | lambda^3 * det_3(X) | same | rel err 1.4e-15 |

### Spot-Check Results (Test 2-3: Polarization)

| Expression | Test Points | Computed | Expected | Match |
|-----------|-----------|---------|---------|-------|
| d(X,X,X) vs 6*N(X) | 10 random X | d(X,X,X) | 6*det_3(X) | rel err 3.1e-15 |
| d(X,Y,Z) symmetry | 5 random (X,Y,Z), 6 perms each | d(perm) | d(X,Y,Z) | max err 5.7e-14 |
| d(e_I,e_I,e_I) vs 6*N(e_I) | all 27 basis vectors | d(e_I,e_I,e_I) | 6*det_3(e_I) | max err 0.0 |

### Spot-Check Results (Test 4: Block structure -- exhaustive)

| Block Type | Triple Count | Max |d_{IJK}| | Expected | Status |
|-----------|-------------|----------------|---------|--------|
| (V_1, V_0, V_0) | 10 nonzero | values +0.5 to -2.0 | nonzero | PASS |
| (V_{1/2}, V_{1/2}, V_0) | 96 nonzero | values +/- 2.0 | nonzero | PASS |
| d_{0,0,0} (pure V_1) | 1 | 0.0 | 0 | PASS |
| V_1 x V_1 x V_0 | 10 | 0.0 | 0 | PASS |
| V_1 x V_{1/2} x V_{1/2} | 136 | 0.0 | 0 | PASS |
| V_{1/2}^3 | 816 | 0.0 | 0 | PASS |
| V_0^3 | 220 | 0.0 | 0 | PASS |

All 3654 distinct triples evaluated exhaustively. Forbidden proxy fp-sampling: REJECTED (exhaustive evaluation performed).

### F_4 Invariance Verification (Test 5)

| Subgroup | Tests | Max Error | Tolerance | Status |
|---------|-------|----------|----------|--------|
| S_3 (6 permutations) | 60 | 7.1e-15 | 1e-12 | PASS |
| G_2 (14 generators, 21 derivations) | 210 | 2.0e-13 | 1e-12 | PASS |
| Spin(9) grade-2 (36 generators) | 360 | 2.2e-05 | 1e-04 (eps^2) | PASS |
| **Total** | **630** | -- | -- | **PASS** |

Spin(9) error scaling verified independently: err/eps^2 = 0.75 constant across eps = 1e-4, 1e-5, 1e-6, 1e-7, confirming the O(epsilon) variation vanishes and residual is O(epsilon^2) from truncated exponential.

### (V_1,V_0,V_0) Block = det_2 Bilinear Form (Test 7)

Full 10x10 matrix d(E_{11}, e_a, e_b) compared with det_2 bilinear form B(e_a, e_b):
- Maximum difference: 0.0 (exact match) over all 55 distinct pairs
- Block is diagonal: diag(+0.5, -0.5, -2, -2, -2, -2, -2, -2, -2, -2)
- Spacetime sector (indices 0,1,2,9): signature (+,-,-,-) = Minkowski (1,3)

### SM Quantum Number Verification (Test 6, 13)

| Check | Result | Expected | Status |
|-------|--------|----------|--------|
| Table length | 27 | 27 | PASS |
| V_0 split | (4, 6) | (4, 6) | PASS |
| Paper 7 multiset match | True | True | PASS |
| Quarks (B-L = 1/3) | 12 | 12 | PASS |
| Leptons (B-L = -1) | 4 | 4 | PASS |
| Gell-Mann-Nishijima Q = J3L + J3R + (B-L)/2 | max err 5.6e-17 | 0 | PASS |
| Charge quantization (all Q multiples of 1/3) | True | True | PASS |
| Sum of charges (anomaly check) | 0.0 | 0 | PASS |
| Sum of B-L | 0.0 | 0 | PASS |

### Dimension Count (Test 10)

1 (V_1) + 16 (V_{1/2}) + 10 (V_0) = 27. PASS.

### Full d_{IJK} Symmetry (Test 11)

306 permutation evaluations over nonzero tensor entries. Max error: 0.0 (exact). PASS.

## Physics Consistency Summary

| Check | Status | Confidence | Notes |
|-------|--------|------------|-------|
| 5.1 Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All quantities dimensionless (pure algebra); det_3 cubic homogeneous verified |
| 5.2 Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | 15 independent test computations, all match |
| 5.3 Limiting cases | PASS | INDEPENDENTLY CONFIRMED | det_3(diag) = abc, det_3(idempotent) = 0, d(X,X,X) = 6*N(X) |
| 5.4 Cross-check | PASS | INDEPENDENTLY CONFIRMED | (V_1,V_0,V_0) block cross-checked against det_2 bilinear form (exact) |
| 5.5 Intermediate spot-check | PASS | INDEPENDENTLY CONFIRMED | Spin(9) error scaling O(eps^2) verified at 4 epsilon values |
| 5.6 Symmetry (F_4 invariance) | PASS | INDEPENDENTLY CONFIRMED | 630 tests across S_3 + G_2 + Spin(9) subgroups |
| 5.6 Symmetry (d_{IJK} symmetry) | PASS | INDEPENDENTLY CONFIRMED | 306 permutation tests, max err 0.0 |
| 5.7 Conservation (block selection rules) | PASS | INDEPENDENTLY CONFIRMED | U(1) charge conservation: only charge-0 blocks nonzero, verified exhaustively |
| 5.8 Math consistency | PASS | INDEPENDENTLY CONFIRMED | SM quantum numbers satisfy GMN relation, charge quantization, anomaly cancellation |
| 5.10 Agreement with literature | PASS | INDEPENDENTLY CONFIRMED | Paper 7 SM fermion table matched multiset; Slansky branching 27=1+16+10 confirmed |
| 5.11 Physical plausibility | PASS | INDEPENDENTLY CONFIRMED | Minkowski signature (1,3) in spacetime sector; correct quark/lepton content |
| Gate A: Catastrophic cancellation | PASS | INDEPENDENTLY CONFIRMED | No cancellation: det_3 terms are O(1), results O(1); R ~ 1 |
| Gate B: Analytical-numerical cross-validation | PASS | INDEPENDENTLY CONFIRMED | det_3 analytical formula matched numerical evaluation at all test points |
| Gate C: Integration measure | N/A | N/A | No coordinate transformations in this phase (pure algebra) |
| Gate D: Approximation validity | N/A | N/A | No approximations used (exact computation) |

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence | Why it matters |
|----------|--------|----------|---------------|
| fp-sampling | REJECTED | All 3654 triples evaluated exhaustively | Must verify ALL blocks zero/nonzero |
| fp-wrong-association | REJECTED | Code uses left-to-right Re((x1*x2)*x3). However, verified that Re((ab)c) = Re(a(bc)) for all octonions (the associator is purely imaginary, Schafer 1966), so for det_3 specifically both associations give identical results. The convention matters for the adjoint map X# but not for the norm N(X). | Wrong association would invalidate downstream adjoint computations |
| fp-normalization-mismatch | REJECTED | d(X,X,X) = 6*N(X) verified (rel err 3.1e-15); convention clearly documented | Factor of 6 propagates to GST coupling |
| fp-circular-double-duty | REJECTED | Logical structure verified: P1(GST exists), P2(F_4 symmetry), P3(Springer) -> C(V=c*det). GST is hypothesis, not premise for identification. | Circularity would invalidate entire GST connection |
| fp-incomplete-blocks | REJECTED | Exhaustive 3654-triple evaluation, not sampling | Missing nonzero block invalidates coupling analysis |
| fp-wrong-real-form | REJECTED | .tex explicitly states E_6(-26), not E_6(-78) or E_6(6) | Wrong real form gives wrong scalar manifold |
| fp-confusing-26-and-27 | REJECTED | .tex Step 1 explicitly states 27 = 26+1 under F_4; "27 is NOT irreducible under F_4" | Confusing 26 and 27 changes invariant counting |

## Discrepancies Found

None. All checks pass.

## Note on Association Convention

The forbidden proxy fp-wrong-association flags using Re(x1*(x2*x3)) instead of Re((x1*x2)*x3). Computational verification confirms that for the cubic norm N(X) = det_3(X), the real part of the triple product is association-independent: Re((ab)c) = Re(a(bc)) for all octonions (the associator [a,b,c] = (ab)c - a(bc) is always purely imaginary). This is a known algebraic identity. Therefore the association choice does NOT affect det_3. The convention remains important for the adjoint map X# where the full octonionic value (not just the real part) is needed. The code correctly uses left-to-right association throughout.

## Reference Coverage

| Reference ID | Required Actions | Status |
|-------------|-----------------|--------|
| ref-baez | cite, compare | Cited in code and .tex; benchmarks compared | 
| ref-springer | cite | Cited in .tex Theorem 1 proof |
| ref-gst | cite | Cited in .tex Double Duty Theorem |
| ref-slansky | cite | Cited in code and .tex |
| ref-paper7 | compare | 16 SM quantum numbers multiset-matched |

## Requirements Coverage

| Requirement | Status | Evidence |
|------------|--------|----------|
| ALGB-02 (d_{IJK} Peirce block decomposition) | SATISFIED | 106 nonzero entries in exactly 2 blocks |
| UNIQ-01 (F_4 uniqueness of det) | SATISFIED | Springer 1962 cited; F_4 invariance verified computationally |
| UNIQ-02 (double duty non-circularity) | SATISFIED | Logical structure verified; GST in hypothesis only |

## Anti-Patterns Found

None. No TODOs, placeholders, hardcoded values, or suppressed warnings in the Phase 47 code additions.

## Expert Verification Required

None. All claims verified computationally and against literature.

## Confidence Assessment

**HIGH confidence.** 13 of 15 applicable physics checks independently confirmed by running code and comparing numerical outputs. Two checks (Gate C, Gate D) are N/A for this pure-algebra phase. Every contract target verified by direct computation:

- det_3 benchmarks: 6 categories, all exact or within float64 noise
- Polarization: identity and symmetry verified on random and basis elements
- Block structure: exhaustive (not sampled) evaluation of all 3654 triples
- F_4 invariance: 630 tests across 3 generator subgroups; Spin(9) O(eps^2) scaling confirmed at 4 epsilon values
- Quantum numbers: multiset match with Paper 7; Gell-Mann-Nishijima, charge quantization, and anomaly cancellation all satisfied
- det_2 cross-check: exact match across all 55 V_0 basis pairs
- Non-circularity: logical structure of double duty argument manually verified

The weakest point is that the quantum number assignment relies on index-ordering convention matching Paper 7. However, the verification uses multiset comparison (matching by quantum number values, not index order), which is the correct approach and confirms the 16 SM states are present regardless of ordering.
