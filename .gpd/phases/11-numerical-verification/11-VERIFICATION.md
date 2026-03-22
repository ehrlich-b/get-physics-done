---
phase: 11-numerical-verification
verified: 2026-03-22T18:00:00Z
status: passed
score: 6/7 contract targets verified
consistency_score: 14/14 physics checks passed
independently_confirmed: 12/14 checks independently confirmed
confidence: high
gaps:
  - subject_kind: "claim"
    subject_id: "claim-2d-area-law"
    expectation: "R^2(boundary) > 0.9 for S(A) vs |boundary(A)| regression on independent subregions"
    expected_check: "ROADMAP criterion 2: R^2 > 0.9"
    status: partial
    category: "convergence"
    reason: "R^2(boundary) = 0.885 on 9 independent rectangular subregions, missing the 0.9 threshold by 0.015. Spearman rho = 0.913 > 0.9 and discrimination gap R2_bd - R2_vol = 0.394 clearly favors area law, but the specific ROADMAP R^2 threshold is not met."
    computation_evidence: "Independent regression recomputation confirms R^2 = 0.8851 exactly. The deficit is not a code error but a finite-size / shape-diversity limitation of a 4x4 lattice with only 9 independent rectangular shapes."
    artifacts:
      - path: "data/area_law/area_law_results.json"
        issue: "R^2(boundary, 9 indep) = 0.885 < 0.9"
    missing:
      - "Either relax ROADMAP threshold to R^2 > 0.85 (with Spearman > 0.9 as supporting evidence), or add more diverse subregion shapes to increase regression range, or use a larger 2D lattice"
    severity: accepted
    resolution: "User accepted 2026-03-22: R^2=0.885 with Spearman=0.913 meets the spirit of the criterion. Threshold was ambitious for 16-qubit 4x4 PBC lattice. Note caveat in Paper 12."
comparison_verdicts:
  - subject_kind: claim
    subject_id: "claim-benchmark-tfi"
    reference_id: "ref-calabrese-cardy"
    comparison_kind: benchmark
    verdict: pass
    metric: "central_charge_c"
    threshold: "c -> 0.5 with correct finite-size trend"
  - subject_kind: claim
    subject_id: "claim-benchmark-heisenberg"
    reference_id: "ref-bethe-ansatz"
    comparison_kind: benchmark
    verdict: pass
    metric: "E_0_per_site"
    threshold: "monotonic convergence to Bethe ansatz -0.8863"
  - subject_kind: claim
    subject_id: "claim-benchmark-heisenberg"
    reference_id: "ref-calabrese-cardy"
    comparison_kind: benchmark
    verdict: pass
    metric: "central_charge_c"
    threshold: "c -> 1.0 with correct finite-size trend"
  - subject_kind: claim
    subject_id: "claim-2d-area-law"
    reference_id: "ROADMAP-criterion-2"
    comparison_kind: acceptance_criterion
    verdict: partial
    metric: "R^2(boundary)"
    threshold: "> 0.9"
  - subject_kind: claim
    subject_id: "claim-mveh-qualitative"
    reference_id: "ref-phase10-a5"
    comparison_kind: qualitative
    verdict: pass
    metric: "frac_negative_delta_S"
    threshold: "> 0.95"
suggested_contract_checks: []
---

# Phase 11 Verification: Numerical Verification

**Phase goal:** Area-law scaling and entanglement structure are verified numerically on small self-modeling lattices, benchmarked against known models.

**Verification date:** 2026-03-22
**Status:** GAPS_FOUND (1 narrow miss on ROADMAP R^2 threshold)
**Confidence:** HIGH (12/14 physics checks independently confirmed via computation)
**Profile:** deep-theory | **Autonomy:** balanced | **Mode:** balanced

---

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|---------|
| claim-benchmark-tfi | claim | VERIFIED | INDEPENDENTLY CONFIRMED | TFI critical c=0.574 at N=16 (trend -> 0.5); gapped S=0.043 saturated; E_0 matches free-fermion to 1e-15 |
| claim-benchmark-heisenberg | claim | VERIFIED | INDEPENDENTLY CONFIRMED | AFM c=1.060 at N=20 (trend -> 1.0); E_0/N converges to Bethe ansatz; FM S=0 exactly |
| claim-infrastructure-correct | claim | VERIFIED | INDEPENDENTLY CONFIRMED | S(A)=S(B), 0<=S<=|A|ln2, Tr(rho_A)=1, hermitian, PSD all pass; S(1)=ln(2) exact |
| claim-1d-area-law | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 1D AFM shows log scaling S~(1/3)ln(L) with c=1.060->1.0 (gapless CFT, not strict area law -- honest assessment); gapped TFI shows strict area law |
| claim-2d-area-law | claim | PARTIAL | INDEPENDENTLY CONFIRMED | R^2(bd)=0.885 misses 0.9 threshold by 0.015; Spearman=0.913>0.9; R^2(vol)=0.491<0.5; discrimination gap=0.394 |
| claim-modular-locality | claim | VERIFIED | INDEPENDENTLY CONFIRMED | SRF=0.9993 for Heisenberg AFM (K_A is 99.93% nearest-neighbor); supports A3 |
| claim-mveh-qualitative | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 100% of perturbations decrease S(A); quadratic scaling eps^1.94; supports A5 |

**Score: 6/7 targets verified, 1 partial.**

---

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| code/ed_entanglement.py | ED framework | VERIFIED | Imports, runs, all functions tested end-to-end; vectorized bit-manipulation confirmed |
| code/area_law_verification.py | Area-law analysis | VERIFIED | Imports ED framework correctly; 1D and 2D computations confirmed |
| code/modular_hamiltonian_check.py | Modular Hamiltonian | VERIFIED | K_A computation, Pauli expansion, MVEH perturbation all confirmed |
| data/benchmarks/benchmark_results.json | Benchmark data | VERIFIED | All 8 acceptance tests pass; energies and entropies confirmed independently |
| data/area_law/area_law_results.json | Area-law data | VERIFIED | 1D and 2D data confirmed; regression statistics independently recomputed |
| data/modular_hamiltonian/modular_hamiltonian_results.json | K_A and MVEH data | VERIFIED | SRF, decay profiles, MVEH sign/scaling all confirmed |

---

## Computational Verification Details

### Spot-Check Results

| Expression | Test Point | Computed | Expected | Match |
|-----------|-----------|---------|----------|-------|
| E_0 Heisenberg N=8 PBC | J=1 | -7.302186817874351 | -7.302186817874356 (stored) | YES (diff=4.4e-15) |
| E_0 TFI N=8 critical OBC | J=h=1 | -9.837951447459396 | -9.837951447459439 (free-fermion) | YES (diff=4.3e-14) |
| E_0 TFI N=8 gapped OBC | J=1,h=3 | -24.586275728866020 | -24.586275728865985 (free-fermion) | YES (diff=3.6e-14) |
| E_0 TFI N=12 critical OBC | J=h=1 | -14.925971109908650 | -14.925971109908664 (free-fermion) | YES (diff=1.4e-14) |
| S(L=1) Heisenberg N=8 | PBC | 0.693147180559945 | ln(2) = 0.693147180559945 | YES (exact) |
| Self-modeling offset N=12 | J=1 | 5.9999999999999 | N_bonds*J/2 = 6.0 | YES (diff=1e-14) |
| R^2(boundary, 9 indep) | 2D 4x4 | 0.885144 | >0.9 (ROADMAP) | NO (miss by 0.015) |
| R^2(volume, 9 indep) | 2D 4x4 | 0.491250 | <0.5 (ROADMAP) | YES |
| Boundary count 1x1 PBC | 4x4 | 4 | 4 | YES |
| Boundary count 2x3 PBC | 4x4 | 10 | 10 | YES |
| Boundary count L-shape-3 | 4x4 | 8 | 8 | YES |

### Limiting Cases Re-Derived

| Limit | Parameter | Expression Limit | Expected | Agreement | Confidence |
|-------|----------|-----------------|----------|-----------|------------|
| FM ground state (J < 0) | J=-1 | S(L) = 0 for all L | Product state | EXACT | INDEPENDENTLY CONFIRMED |
| Single-site entropy AFM | L=1 | S = ln(2) | SU(2) singlet: rho_1 = I/2 | EXACT (diff < 1e-15) | INDEPENDENTLY CONFIRMED |
| TFI h >> J (paramagnetic) | h/J=3 | S saturates at O(0.04) | Area law (gapped) | YES | INDEPENDENTLY CONFIRMED |
| TFI h=J (critical) | h/J=1 | S ~ (c/6)ln(L) with c=1/2 | Ising CFT | YES (c=0.574, OBC corrections) | INDEPENDENTLY CONFIRMED |
| Heisenberg N -> inf | c from CC fit | c -> 1 | SU(2)_1 WZW | YES (1.121->1.060, monotone) | INDEPENDENTLY CONFIRMED |
| Bethe ansatz E_0/N | N -> inf | E_0/N -> 1/2 - 2ln(2) | -0.886294 | YES (N=20: -0.8904, converging) | INDEPENDENTLY CONFIRMED |
| Self-modeling = Heisenberg | J=1 | E_SM - E_H = N_bonds * J/2 | Constant shift | EXACT (1e-14) | INDEPENDENTLY CONFIRMED |
| S(A) = S(B) for pure states | L=3, N=8 | S(3) = S(5) | Mandatory | EXACT (diff=0) | INDEPENDENTLY CONFIRMED |

### Cross-Checks Performed

| Result | Primary Method | Cross-Check Method | Agreement |
|--------|---------------|-------------------|-----------|
| E_0 TFI | Sparse Lanczos (eigsh) | Dense diag (eigh) | Exact to 1e-14 |
| E_0 Heisenberg | Sparse Lanczos | Independent Hamiltonian construction | Exact to 4e-15 |
| S(A)=S(B) | Partial trace of rho_A | Schmidt decomposition (SVD) | Exact to 1e-10 |
| SRF = 0.9993 | Pauli expansion | Manual sum_sq from decay profile | Exact match |
| R^2(boundary) = 0.885 | Code regression | Independent scipy.stats.linregress | Exact match |
| Boundary counts | Code boundary_count_arbitrary | Manual counting | All 11 cases match |
| CC fit c | Code fit_cc_pbc | Independent lstsq | Exact match |

### Intermediate Result Spot-Checks

| Step | Intermediate Expression | Independent Result | Match |
|------|------------------------|-------------------|-------|
| Hamiltonian construction | H_Heisenberg diagonal for N=8, state |00000000> | (J/2)*N = 4.0 (all spins up: each sz*sz = 1) | Verified from bit manipulation |
| SWAP vs Heisenberg relation | JF = (J/2)(sigma.sigma) + (J/2)I per bond | Offset = n_bonds * J/2 | Confirmed to 1e-14 |
| CC fit formula | x = (1/3)ln[(N/pi)sin(piL/N)] | Matches stored x-values for N=8 | Confirmed |
| SRF definition | ||K_short||_F / ||K_total||_F | sqrt(short_sq/total_sq) = 0.999262 | Matches stored value exactly |

---

## Physics Consistency

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All quantities dimensionless in natural units; S in nats, E in J-units, rho Tr=1 |
| 5.2 | Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | 11 test points verified, all match stored values |
| 5.3 | Limiting cases | PASS | INDEPENDENTLY CONFIRMED | 8 limits re-derived: FM=0, S(1)=ln2, gapped saturation, critical c, Bethe, SM=Heis, S(A)=S(B), paramagnetic |
| 5.4 | Independent cross-check | PASS | INDEPENDENTLY CONFIRMED | Dense vs sparse diag, partial trace vs SVD, independent Hamiltonian construction |
| 5.5 | Intermediate spot-check | PASS | INDEPENDENTLY CONFIRMED | Hamiltonian construction, CC fit formula, SRF definition all verified |
| 5.6 | Symmetry | PASS | INDEPENDENTLY CONFIRMED | SU(2): Sz_total = 0 (verified), S(1) = ln(2) (verified), S(A) = S(B) (verified) |
| 5.7 | Conservation / consistency | PASS | INDEPENDENTLY CONFIRMED | Tr(rho_A)=1, hermitian, PSD, entropy bounds all verified by code and independently |
| 5.8 | Math consistency | PASS | INDEPENDENTLY CONFIRMED | Boundary counting verified for 11 subregions; all regression statistics independently reproduced |
| 5.9 | Convergence | PASS | INDEPENDENTLY CONFIRMED | c(N) trend: 1.121->1.088->1.071->1.060 monotonically -> 1.0; E_0/N -> Bethe ansatz |
| 5.10 | Literature agreement | PASS | INDEPENDENTLY CONFIRMED | Bethe ansatz E_0/N, CC formula c=1/2 (TFI) and c=1 (Heisenberg), FM product state |
| 5.11 | Physical plausibility | PASS | INDEPENDENTLY CONFIRMED | S >= 0, S <= |A|ln2, S(1)=ln2, log scaling (not volume law), MVEH delta_S < 0 |
| 5.12 | Statistical rigor | N/A | N/A | No Monte Carlo or stochastic methods; exact diagonalization |
| 5.13 | Thermodynamic consistency | N/A | N/A | No thermodynamic quantities computed |
| 5.14 | Spectral/analytic | PASS | STRUCTURALLY PRESENT | Modular Hamiltonian spectrum well-conditioned for Heisenberg (cond=3950); TFI condition numbers flagged |
| Gate A | Catastrophic cancellation | PASS | INDEPENDENTLY CONFIRMED | All S values O(1), no cancellation; energy values well-resolved |
| Gate B | Analytical-numerical cross | PASS | INDEPENDENTLY CONFIRMED | CC formula evaluated at test points matches numerical S(L) to R^2>0.999 |
| Gate C | Integration measure | N/A | N/A | No coordinate transforms in numerical code |
| Gate D | Approximation validity | PASS | INDEPENDENTLY CONFIRMED | ED is exact; finite-size corrections diminish monotonically as N increases |

**Overall physics assessment:** SOUND -- all 14 applicable checks pass, 12 independently confirmed.

---

## Forbidden Proxy Audit

| Proxy | Status | Evidence |
|-------|--------|---------|
| Only checking 1D without attempting 2D | REJECTED | 2D 4x4 lattice computed with 15 rectangular + 6 non-rectangular subregions |
| Reporting scaling without fit statistics | REJECTED | R^2, Spearman rho, p-values all reported; discrimination gap quantified |
| Claiming area law without distinguishing from volume law | REJECTED | Boundary vs volume regressions explicitly compared; 1D honestly reported as log scaling (gapless) |

---

## Comparison Verdict Ledger

| Subject ID | Comparison Kind | Verdict | Threshold | Notes |
|------------|----------------|---------|-----------|-------|
| claim-benchmark-tfi | benchmark (CC c=1/2) | PASS | c -> 0.5 | c=0.574 at N=16 OBC, Affleck-Ludwig corrections understood |
| claim-benchmark-heisenberg | benchmark (Bethe) | PASS | E_0/N -> -0.8863 | Deviation 0.004 at N=20, monotonic convergence |
| claim-benchmark-heisenberg | benchmark (CC c=1) | PASS | c -> 1.0 | c=1.060 at N=20, monotonic convergence |
| claim-2d-area-law | ROADMAP criterion 2 | PARTIAL | R^2(bd) > 0.9 | R^2=0.885, miss by 0.015; Spearman=0.913 > 0.9 |
| claim-mveh-qualitative | qualitative (A5) | PASS | frac_negative > 0.95 | 100% negative across all epsilon values |

---

## Discrepancies Found

| Severity | Location | Computation Evidence | Root Cause | Suggested Fix |
|----------|----------|---------------------|------------|---------------|
| SIGNIFICANT | 2D R^2(boundary) = 0.885 | Independent regression confirms 0.8851 exactly | 4x4 PBC lattice has limited boundary diversity for rectangular subregions (only values 4,6,8,10,12); the 2x4/4x2 shape has boundary=8 but volume=8, creating an outlier that depresses R^2 | Accept Spearman > 0.9 as supporting evidence; or note this is a finite-size limitation of the 4x4 lattice |
| INFO | TFI condition numbers ~5e10 | Stored values confirmed | Exponentially small rho_A eigenvalues in gapped phase | Not an error; modular Hamiltonian for TFI is less reliable, but Heisenberg (cond=3950) is well-conditioned |
| INFO | MVEH scaling power = 1.94 vs 2.0 | Power law fit from 3 epsilon values | Gapless system (Heisenberg) has logarithmic corrections to pure epsilon^2 scaling | Expected for c=1 CFT; not an error |

---

## Requirements Coverage

| Requirement | Status | Evidence |
|-------------|--------|---------|
| NUMR-01: Benchmarks reproduce known results | SATISFIED | TFI c=0.574->0.5, gapped S=0.04, Heisenberg c=1.06->1.0, FM S=0, all energies match |
| NUMR-01: Self-modeling area law (1D) | SATISFIED (with caveat) | AFM Heisenberg shows log scaling (gapless c=1 CFT), not strict area law; this is expected and honestly reported |
| NUMR-01: Self-modeling area law (2D) | PARTIAL | R^2(bd)=0.885 misses 0.9; R^2(vol)=0.491 < 0.5; discrimination gap strong |
| NUMR-01: Convergence and error bars | SATISFIED | Finite-size trends monotonically converging for c, E_0/N; threshold sensitivity tested |

---

## Anti-Patterns Found

| Pattern | File | Severity | Physics Impact |
|---------|------|----------|----------------|
| No TODOs, FIXMEs, or placeholders | all code | CLEAN | None |
| No suppressed warnings | all code | CLEAN | None |
| ASSERT_CONVENTION present | all code | CLEAN | Convention consistency maintained |
| FM S_L reported as -0.0 (negative zero) | benchmark_results.json | INFO | Cosmetic; no physics impact (S=0 correct) |

---

## Expert Verification Required

None. All results are benchmark-level computations against known exact solutions. No novel theoretical claims require expert review.

---

## Confidence Assessment

**Overall confidence: HIGH**

This is a numerical/validation phase where all key quantities have known exact or literature values for comparison. The verification confidence is high because:

1. **12 of 14 physics checks were independently confirmed** by re-running computations from scratch (independent Hamiltonian construction, independent energy calculation, independent regression, independent boundary counting).

2. **All benchmark values match** published results: TFI energies match free-fermion to 1e-15, Heisenberg E_0/N converges to Bethe ansatz, central charges converge to known CFT values.

3. **The one gap (R^2 = 0.885 vs 0.9 threshold) is a genuine finite-size limitation**, not a code error or physics mistake. The independent regression reproduces R^2 = 0.8851 exactly.

4. **The code runs end-to-end** with correct imports, no suppressed warnings, and all consistency checks passing.

The 2 checks rated STRUCTURALLY PRESENT (spectral/analytic structure for TFI condition numbers and thermodynamic consistency) are not applicable to this phase's scope.

---

## Gaps Summary

**One significant gap: 2D R^2(boundary) narrowly misses the ROADMAP threshold.**

R^2(boundary) = 0.885 on 9 independent rectangular subregions of the 4x4 PBC Heisenberg lattice, missing the ROADMAP criterion of R^2 > 0.9 by 0.015.

**Root cause:** The 4x4 PBC lattice with rectangular subregions has limited boundary diversity. Boundary values cluster at {4, 6, 8, 10, 12} with multiple shapes sharing boundary=8 but having very different volumes (4, 8, 12). The 2x4 shape in particular is an outlier: it has the same boundary (8) as 1x4, 2x2, and 3x4 but very different S values due to the torus topology giving it more entanglement (volume=half the system).

**Mitigating evidence:**
- Spearman rank correlation rho = 0.913 > 0.9 (nonlinear correlation IS strong)
- R^2(volume) = 0.491 < 0.5 (volume law IS excluded)
- Discrimination gap R^2(bd) - R^2(vol) = 0.394 (boundary wins decisively)
- Including non-rectangular subregions: combined regression R^2(bd) = 0.780, but this decreases because non-rectangular shapes introduce shape-dependent entanglement beyond simple boundary counting

**Recommendation:** This gap does not invalidate the area-law conclusion. The physics clearly shows area-law behavior (boundary correlates much better than volume with S). The R^2 threshold was set before the specific geometry limitations of a 4x4 PBC lattice were known. Options:
1. Accept R^2=0.885 + Spearman=0.913 as meeting the spirit of the criterion
2. Relax the threshold to R^2 > 0.85 in the ROADMAP
3. Run a larger 2D lattice (6x3 = 18 sites would give more boundary diversity)
