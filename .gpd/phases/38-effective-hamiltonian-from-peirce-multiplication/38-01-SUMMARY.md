---
phase: 38-effective-hamiltonian-from-peirce-multiplication
plan: 01
depth: full
one-liner: "Constructed 2-site Clifford Heisenberg Hamiltonian H_2 on R^256, computed exact spectrum with 5 Spin(9) irreps Lambda^k(V_9), determined ferromagnetic ground state in Lambda^1 (dim 9)"

subsystem: [computation, formalism, validation]
tags: [spin9, clifford-algebra, heisenberg-model, clebsch-gordan, exact-diagonalization]

requires:
  - phase: 28-peirce-multiplication-operators
    provides: "10 T_b operators as 16x16 real matrices with Clifford structure"
provides:
  - "2-site Hamiltonian H_2 = J sum T_a(1)T_a(2) as 256x256 real symmetric matrix"
  - "Exact 2-site spectrum: 5 levels with multiplicities 9, 84, 126, 36, 1"
  - "Ferromagnetic ground state in Lambda^1(V_9) (dim 9, symmetric sector)"
  - "Energy gap Delta = 1.0 J between Lambda^1 and Lambda^3"
  - "Spin(9) commutation verified for all 36 generators (max error 0)"
  - "Casimir cross-check: E_R = J/2 (c_total(R) - 9/2) exact for all 5 irreps"
affects: [38-02, 39-ssb-analysis]

methods:
  added: [exact-diagonalization-256, clifford-normalization-rescaling, casimir-crosscheck]
  patterns: [spin9-cg-decomposition, swap-sector-analysis]

key-files:
  created:
    - code/effective_hamiltonian.py
    - tests/test_effective_hamiltonian.py

key-decisions:
  - "Used rescaled T_a = (1/2)*gamma_a for uniform {T_a,T_b}=(1/2)*delta*I (raw T_b have non-uniform normalization)"
  - "Ferromagnetic ground state determined from SWAP eigenvalue +1 in symmetric sector"
  - "Spin(9) irreps identified as Lambda^k(V_9) via dimension matching C(9,k)"

patterns-established:
  - "Spin(9) CG: S_9 x S_9 = Lambda^0 + Lambda^1 + Lambda^2 + Lambda^3 + Lambda^4"
  - "Energy levels: E_k = J/2 * (c_total(Lambda^k) - 9/2)"

conventions:
  - "hbar = 1, k_B = 1, a = 1"
  - "metric = (+,+,...,+) Riemannian"
  - "{T_a, T_b} = (1/2)*delta_{ab}*I_16 (uniform Clifford normalization)"
  - "J > 0 antiferromagnetic convention (but system is ferromagnetic)"
  - "T_a = (1/2)*gamma_a where {gamma_a, gamma_b} = 2*delta_{ab}*I"

plan_contract_ref: ".gpd/phases/38-effective-hamiltonian-from-peirce-multiplication/38-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-heff-construction:
      status: passed
      summary: "H_eff = J sum_{a=0}^{8} T_a^(i) T_a^(j) constructed as explicit 256x256 real symmetric matrix from rescaled Phase 28 T_b operators"
      linked_ids: [deliv-heff-code, test-hermiticity, test-spin9-commutation, ref-phase28-tb]
      evidence:
        - verifier: self-check
          method: numerical verification
          confidence: high
          claim_id: claim-heff-construction
          deliverable_id: deliv-heff-code
          acceptance_test_id: test-hermiticity
    claim-2site-spectrum:
      status: passed
      summary: "2-site spectrum exactly computed: 5 levels (E/J = -7/4, -3/4, 1/4, 5/4, 9/4) with multiplicities (9, 84, 126, 36, 1) matching Lambda^k(V_9) dimensions; ground state in symmetric sector = ferromagnetic"
      linked_ids: [deliv-heff-code, deliv-heff-tests, test-degeneracy-structure, test-trace-consistency, test-casimir-check, ref-phase28-tb, ref-spin-geometry]
      evidence:
        - verifier: self-check
          method: casimir cross-check and dimension counting
          confidence: high
          claim_id: claim-2site-spectrum
          deliverable_id: deliv-heff-code
          acceptance_test_id: test-degeneracy-structure
    claim-spin9-symmetry:
      status: passed
      summary: "H_2 commutes with all 36 Spin(9) generators G_{ab} = [T_a, T_b] to exact machine precision (max norm = 0)"
      linked_ids: [deliv-heff-code, deliv-heff-tests, test-spin9-commutation, ref-phase28-tb]
      evidence:
        - verifier: self-check
          method: explicit commutator computation
          confidence: high
          claim_id: claim-spin9-symmetry
          deliverable_id: deliv-heff-code
          acceptance_test_id: test-spin9-commutation
  deliverables:
    deliv-heff-code:
      status: passed
      path: "code/effective_hamiltonian.py"
      summary: "Contains construct_2site_hamiltonian, diagonalize_2site, verify_spin9_commutation, analyze_spectrum, identify_spin9_irreps, determine_magnetic_character, print_spectrum_summary"
      linked_ids: [claim-heff-construction, claim-2site-spectrum, claim-spin9-symmetry]
    deliv-heff-tests:
      status: passed
      path: "tests/test_effective_hamiltonian.py"
      summary: "16 tests covering hermiticity, trace, casimir, spin9 commutation, eigenvalue count/sum, degeneracy, j=0 limit, swap eigenvalues, ground state sector, casimir crosscheck, energy gap"
      linked_ids: [claim-2site-spectrum, claim-spin9-symmetry]
  acceptance_tests:
    test-hermiticity:
      status: passed
      summary: "norm(H_2 - H_2^T) = 0 (exact to machine precision)"
      linked_ids: [claim-heff-construction, deliv-heff-code]
    test-spin9-commutation:
      status: passed
      summary: "max norm of [H_2, G_{ab}^total] across all 36 generators = 0 (exact)"
      linked_ids: [claim-spin9-symmetry, deliv-heff-code, deliv-heff-tests]
    test-degeneracy-structure:
      status: passed
      summary: "Multiplicities {1, 9, 36, 84, 126} match C(9,k) for k=0..4 exactly; total = 256"
      linked_ids: [claim-2site-spectrum, deliv-heff-code]
    test-trace-consistency:
      status: passed
      summary: "Tr(H_2) = 0, sum of eigenvalues = 0 (exact)"
      linked_ids: [claim-2site-spectrum, deliv-heff-code]
    test-casimir-check:
      status: passed
      summary: "Single-site Casimir sum T_a^2 = (9/4)*I_16 with error 0"
      linked_ids: [claim-2site-spectrum, deliv-heff-code]
  references:
    ref-phase28-tb:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "Phase 28 T_b operators loaded via compute_T_b_matrices(), rescaled to uniform Clifford normalization, used to construct H_eff"
    ref-spin-geometry:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Spin(9) CG decomposition S_9 x S_9 = sum Lambda^k(V_9) confirmed numerically: all 5 irrep dimensions match C(9,k)"
  forbidden_proxies:
    fp-generic-heff:
      status: rejected
      notes: "Explicit 256x256 matrix elements computed from Phase 28 T_b operators via rescale_to_clifford_generators + Kronecker product"
    fp-assumed-antiferro:
      status: rejected
      notes: "Ferro/antiferro determined from explicit SWAP eigenvalue analysis of ground state eigenvectors; result is FERROMAGNETIC"
  uncertainty_markers:
    weakest_anchors:
      - "No external benchmark for F_4 lattice model; validation purely internal (Casimir, dimensions, commutation)"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 7min
completed: 2026-03-30
---

# Phase 38, Plan 01: H_eff Construction and 2-Site Spectrum Summary

**Constructed 2-site Clifford Heisenberg Hamiltonian H_2 on R^256, computed exact spectrum with 5 Spin(9) irreps Lambda^k(V_9), determined ferromagnetic ground state in Lambda^1 (dim 9)**

## Performance

- **Duration:** 7 min
- **Started:** 2026-03-30T21:50:27Z
- **Completed:** 2026-03-30T21:57:45Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- H_2 = J * sum_{a=0}^{8} T_a (x) T_a constructed as 256x256 real symmetric matrix with Spin(9) symmetry verified exactly (all 36 commutators = 0) [CONFIDENCE: HIGH]
- 2-site spectrum: 5 levels with E/J = -7/4, -3/4, 1/4, 5/4, 9/4 and multiplicities 9, 84, 126, 36, 1 matching Lambda^k(V_9) for k = 1, 3, 4, 2, 0 [CONFIDENCE: HIGH]
- Ground state: Lambda^1(V_9) (vector rep, dim 9), symmetric sector, FERROMAGNETIC character with energy gap Delta = J [CONFIDENCE: HIGH]
- Casimir cross-check: E_R = J/2 * (c_total(R) - 9/2) reproduces all 5 eigenvalues exactly [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: Construct and diagonalize 2-site Hamiltonian H_2** - `60969f4` (compute)
2. **Task 2: Spectrum interpretation and CG cross-check with tests** - `e49d214` (validate)

## Files Created/Modified

- `code/effective_hamiltonian.py` - H_eff construction, diagonalization, Spin(9) verification, spectrum analysis
- `tests/test_effective_hamiltonian.py` - 16 tests covering all acceptance criteria

## Next Phase Readiness

- Full 2-site spectrum available for Plan 02 (cubic assessment, frame stabilizer)
- Ferromagnetic ground state in Lambda^1(V_9) determines SSB pattern for Phase 39
- Energy gap Delta = J available for excitation spectrum analysis
- Spin(9) invariance numerically exact -- ready for symmetry-breaking analysis

## Contract Coverage

- claim-heff-construction -> passed (explicit 256x256 matrix from Phase 28 operators)
- claim-2site-spectrum -> passed (5 levels matching Lambda^k(V_9), ferro determined)
- claim-spin9-symmetry -> passed (36 commutators all exactly zero)
- deliv-heff-code -> passed (code/effective_hamiltonian.py)
- deliv-heff-tests -> passed (tests/test_effective_hamiltonian.py, 16/16)
- test-hermiticity -> passed (error = 0)
- test-spin9-commutation -> passed (max norm = 0)
- test-degeneracy-structure -> passed (dims match C(9,k))
- test-trace-consistency -> passed (Tr = 0)
- test-casimir-check -> passed (C_1 = 9/4 * I)
- ref-phase28-tb -> completed (read, use)
- ref-spin-geometry -> completed (compare)
- fp-generic-heff -> rejected
- fp-assumed-antiferro -> rejected

## Equations Derived

**Eq. (38.1): 2-site Hamiltonian**

$$
H_2 = J \sum_{a=0}^{8} T_a^{(1)} \otimes T_a^{(2)}, \quad \{T_a, T_b\} = \tfrac{1}{2}\delta_{ab} I_{16}
$$

**Eq. (38.2): Eigenvalue formula (Casimir relation)**

$$
E_R = \frac{J}{2}\left(c_{\text{total}}(R) - \frac{9}{2}\right), \quad R \in \{\Lambda^k(V_9)\}_{k=0}^{4}
$$

**Eq. (38.3): Spectrum table**

| Level | $E/J$ | Multiplicity | Irrep | Sector | $c_{\text{total}}$ |
|-------|-------|-------------|-------|--------|-----------|
| 0 | $-7/4$ | 9 | $\Lambda^1(V_9)$ | sym | 1 |
| 1 | $-3/4$ | 84 | $\Lambda^3(V_9)$ | antisym | 3 |
| 2 | $+1/4$ | 126 | $\Lambda^4(V_9)$ | sym | 5 |
| 3 | $+5/4$ | 36 | $\Lambda^2(V_9)$ | antisym | 7 |
| 4 | $+9/4$ | 1 | $\Lambda^0(V_9)$ | sym | 9 |

**Eq. (38.4): CG decomposition**

$$
S_9 \otimes S_9 = \bigoplus_{k=0}^{4} \Lambda^k(V_9), \quad \dim = 1 + 9 + 36 + 84 + 126 = 256
$$

## Validations Completed

- H_2 = H_2^T: exact (Frobenius norm of antisymmetric part = 0)
- Tr(H_2) = 0: exact
- Single-site Casimir: sum T_a^2 = (9/4)*I_16, error = 0
- Spin(9) commutation: max |[H_2, G_{ab}]| = 0 for all 36 generators
- Eigenvalue count: 256, sum = 0
- Degeneracies: {1, 9, 36, 84, 126} = {C(9,0), ..., C(9,4)}
- Casimir cross-check: all 5 eigenvalues match E = J/2*(c_total - 9/2)
- J=0 limit: all eigenvalues = 0
- SWAP spectrum: +1 (dim 136), -1 (dim 120)
- Symmetric sector: 9 + 126 + 1 = 136; antisymmetric: 84 + 36 = 120

## Decisions Made

- Used rescaled Clifford generators T_a = (1/2)*gamma_a for uniform normalization. Raw T_b from Phase 28 have non-uniform norm: T_b[1] satisfies {T,T} = (1/8)*I while T_b[2..9] satisfy {T,T} = (1/2)*I. Rescaling via rescale_to_clifford_generators() gives {T_a,T_b} = (1/2)*delta*I uniformly across all 9 generators, which is required for Spin(9) invariance of H_2.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing component] Non-uniform Clifford normalization of raw T_b**

- **Found during:** Task 1 (Casimir check)
- **Issue:** Raw T_b[1] has {T,T} = (1/8)*I, not (1/2)*I. Plan assumed uniform normalization.
- **Fix:** Used rescale_to_clifford_generators() to get gamma_a with {gamma,gamma} = 2*delta*I, then T_a = (1/2)*gamma_a gives uniform {T_a,T_b} = (1/2)*delta*I.
- **Files modified:** code/effective_hamiltonian.py
- **Verification:** All 45 anticommutator checks pass; Casimir = (9/4)*I exact.
- **Committed in:** 60969f4

---

**Total deviations:** 1 auto-fixed (1 missing component)
**Impact on plan:** Essential normalization correction. No scope change.

## Issues Encountered

None beyond the normalization deviation.

## Open Questions

- The energy ordering Lambda^1 < Lambda^3 < Lambda^4 < Lambda^2 < Lambda^0 is not the naive "k ordering." The Casimir cross-check confirms this, but the physical meaning of the non-monotonic c_total(Lambda^k) sequence deserves investigation.
- Ferromagnetic character with J > 0 convention is noteworthy: differs from SU(2) Heisenberg where J > 0 gives antiferro. This is because the smallest total Casimir for Spin(9) spinor tensor product is in the symmetric sector.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Ground state energy | E_0 | -7/4 J | exact | eigh diagonalization | all J |
| Energy gap | Delta | J | exact | eigh diagonalization | all J |
| Ground state multiplicity | d_0 | 9 | exact | eigenvalue counting | all J |
| Single-site Casimir | C_1 | 9/4 | exact | sum T_a^2 | N/A |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|---------------|----------------|
| Bilinear truncation (no cubic det) | det(A) RG-irrelevant | O(J_cubic/J_bilinear) | cubic term qualitatively changes ground state |
| Nearest-neighbor only | short-range coupling | O(k_2/k_1) ~ O(1/2) | V_0-mediated indirect coupling dominates |

---

_Phase: 38-effective-hamiltonian-from-peirce-multiplication, Plan: 01_
_Completed: 2026-03-30_
