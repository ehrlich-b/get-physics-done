---
phase: 38-effective-hamiltonian-from-peirce-multiplication
plan: 02
depth: full
one-liner: "Frame stabilizer = Spin(9) (not F_4) from Peirce projection argument + J_u commutator; Z^d bipartite lattice confirmed; cubic det(A) vanishes identically on OP^2"

subsystem: [formalism, derivation, computation, validation]
tags: [f4, spin9, frame-stabilizer, bipartite-lattice, cubic-invariant, octonionic-projective-plane, goldstone-modes]

requires:
  - phase: 38-effective-hamiltonian-from-peirce-multiplication
    plan: 01
    provides: "2-site spectrum, ferromagnetic ground state, T_a generators, Spin(9) commutation"
  - phase: 28-peirce-multiplication-operators
    provides: "10 T_b operators, Clifford structure, J_u matrix"
  - phase: 37-gap-dependency-theorem
    provides: "UC1-UC4 verification roadmap for Phase 39"
provides:
  - "Frame stabilizer identification: Spin(9) (dim 36) via algebraic + computational proof"
  - "SSB pattern: F_4 -> Spin(9), target space OP^2 (dim 16)"
  - "Physical lattice Z^d bipartite (K_3 is on-site, not the lattice)"
  - "Cubic det(A) = 0 identically on OP^2 (geometric constraint)"
  - "Goldstone mode count: 16 broken generators, Type I vs II TBD by Phase 39"
  - "Complete Phase 39 handoff document"
affects: [39-ssb-analysis, 40-universality-class]

methods:
  added: [frame-stabilizer-analysis, j-u-commutator-test, rank-1-projection-argument]
  patterns: [peirce-projection-breaks-f4, det-vanishes-on-op2]

key-files:
  modified:
    - code/effective_hamiltonian.py
  created:
    - derivations/38-lattice-and-symmetry.md

key-decisions:
  - "Cubic det(A) analysis corrected from sublattice-Z_2 argument (AFM-specific) to geometric det=0 on OP^2 argument (universal)"
  - "Goldstone mode type (I vs II) deferred to Phase 39 -- requires computing symplectic form rank on lattice ground state"

patterns-established:
  - "Peirce projection Pi_{1/2} is Spin(9)-covariant but NOT F_4-covariant -- determines stabilizer for any Peirce-projected Hamiltonian"
  - "OP^2 = rank-1 idempotents => det = 0 identically => cubic terms absent from sigma model"

conventions:
  - "hbar = 1, k_B = 1, a = 1"
  - "metric = (+,+,...,+) Riemannian"
  - "{T_a, T_b} = (1/2)*delta_{ab}*I_16 (uniform Clifford normalization)"
  - "J > 0 antiferromagnetic convention (system is ferromagnetic)"

plan_contract_ref: ".gpd/phases/38-effective-hamiltonian-from-peirce-multiplication/38-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-frame-stabilizer:
      status: passed
      summary: "Frame stabilizer = Spin(9) (dim 36). Proved by (A) algebraic argument that Peirce projection breaks F_4 to Spin(9), (B) J_u commutator ||[H_2, J_u^total]|| = 24.0 != 0, (C) spectrum degeneracies match Spin(9) irreps C(9,k) with no F_4 enhancement"
      linked_ids: [deliv-symmetry-code, deliv-derivation, test-f4-commutation, test-stabilizer-dimension, ref-baez2002, ref-todorov-drenska, ref-plan01-spectrum]
      evidence:
        - verifier: self-check
          method: algebraic argument + numerical commutator + spectrum degeneracy analysis
          confidence: high
          claim_id: claim-frame-stabilizer
          deliverable_id: deliv-symmetry-code
          acceptance_test_id: test-f4-commutation
    claim-lattice-bipartite:
      status: passed
      summary: "Physical lattice = Z^d (bipartite via checkerboard decomposition). K_3 Peirce graph is on-site algebraic structure of single h_3(O), NOT the physical lattice. DLS reflection positivity applies to Z^d."
      linked_ids: [deliv-derivation, test-lattice-argument, ref-dls-bipartite]
      evidence:
        - verifier: self-check
          method: explicit 6-step argument distinguishing K_3 from Z^d
          confidence: high
          claim_id: claim-lattice-bipartite
          deliverable_id: deliv-derivation
          acceptance_test_id: test-lattice-argument
    claim-cubic-assessment:
      status: passed
      summary: "Cubic det(A) has scaling dimension 3/2 in d=3 (formally RG-relevant), but vanishes identically on OP^2 = F_4/Spin(9) because OP^2 consists of rank-1 projections with det=0. Bilinear H_eff is sufficient."
      linked_ids: [deliv-derivation, test-cubic-scaling, ref-baez2002]
      evidence:
        - verifier: self-check
          method: geometric argument (rank-1 projection implies det=0) + explicit verification det(E_ii)=0
          confidence: high
          claim_id: claim-cubic-assessment
          deliverable_id: deliv-derivation
          acceptance_test_id: test-cubic-scaling
  deliverables:
    deliv-symmetry-code:
      status: passed
      path: "code/effective_hamiltonian.py"
      summary: "Added test_f4_beyond_spin9() and frame_stabilizer_analysis() functions implementing J_u commutator test, spin(9) projection, and spectral degeneracy cross-check"
      linked_ids: [claim-frame-stabilizer, test-f4-commutation, test-stabilizer-dimension]
    deliv-derivation:
      status: passed
      path: "derivations/38-lattice-and-symmetry.md"
      summary: "Contains frame stabilizer proof (Sec 1), lattice structure argument (Sec 2), cubic det(A) assessment (Sec 3), and Phase 39 handoff (Sec 4)"
      linked_ids: [claim-frame-stabilizer, claim-lattice-bipartite, claim-cubic-assessment, test-lattice-argument, test-cubic-scaling]
  acceptance_tests:
    test-f4-commutation:
      status: passed
      summary: "J_u (grade-3 Cl(9,0) element outside spin(9)) gives ||[H_2, J_u^total]||_F = 24.0, relative = 2.0. Spin(9) residual of J_u = 86.6%. Direct proof that H_2 does NOT have F_4 symmetry."
      linked_ids: [claim-frame-stabilizer, deliv-symmetry-code]
    test-stabilizer-dimension:
      status: passed
      summary: "Stabilizer = Spin(9) (dim 36). Cross-checked against F_4 maximal subgroup list (Baez 2002, Todorov-Drenska 2018): Spin(9) is the unique maximal subgroup stabilizing the Peirce decomposition."
      linked_ids: [claim-frame-stabilizer, deliv-symmetry-code, deliv-derivation, ref-todorov-drenska]
    test-lattice-argument:
      status: passed
      summary: "6-step argument: (1) h_3(O) is on-site, (2) K_3 describes single h_3(O), (3) Z^d is physical lattice, (4) H_ij acts on V_{1/2}^(i) x V_{1/2}^(j), (5) Z^d is bipartite (checkerboard), (6) DLS applies to Z^d not K_3."
      linked_ids: [claim-lattice-bipartite, deliv-derivation, ref-dls-bipartite]
    test-cubic-scaling:
      status: passed
      summary: "Scaling dimension 3(d-2)/2 = 3/2 in d=3 (relevant). But coefficient = 0 exactly: det(p) = 0 for all p in OP^2 (rank-1 projections). Verified det(E_11) = det(E_22) = det(E_33) = 0, and by F_4-transitivity, det = 0 on all of OP^2."
      linked_ids: [claim-cubic-assessment, deliv-derivation, ref-baez2002]
  references:
    ref-baez2002:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "Used F_4 = Aut(h_3(O)), Spin(9) = Stab(E_11), F_4/Spin(9) = OP^2 structure. Cubic determinant definition from Sec 3.4."
    ref-todorov-drenska:
      status: completed
      completed_actions: [compare]
      missing_actions: []
      summary: "Cross-checked Spin(9) against F_4 maximal subgroup list: Spin(9) (dim 36) is the unique maximal subgroup stabilizing Peirce decomposition."
    ref-dls-bipartite:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "DLS reflection positivity requires bipartite lattice; Z^d satisfies this via standard checkerboard decomposition."
    ref-plan01-spectrum:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "2-site spectrum degeneracies {1,9,36,84,126} used for spectral cross-check of Spin(9) stabilizer. Ferromagnetic ground state noted for Goldstone analysis."
  forbidden_proxies:
    fp-assumed-spin9:
      status: rejected
      notes: "Frame stabilizer determined FROM H_eff via three independent methods (algebraic, J_u commutator, spectral), not assumed a priori"
    fp-assumed-bipartite:
      status: rejected
      notes: "K_3 explicitly identified as on-site Peirce structure; Z^d explicitly identified as physical lattice; bipartiteness proved for Z^d via checkerboard decomposition"
    fp-ignored-cubic:
      status: rejected
      notes: "Cubic det(A) explicitly assessed: scaling dimension computed (3/2 in d=3, relevant), then shown to vanish identically on OP^2 target space"
  uncertainty_markers:
    weakest_anchors:
      - "No external benchmark for F_4 lattice models -- all validation internal"
      - "Goldstone mode type (I vs II) deferred to Phase 39"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 6min
completed: 2026-03-30
---

# Phase 38, Plan 02: Frame Stabilizer, Lattice Structure, and Cubic Assessment

**Frame stabilizer = Spin(9) (not F_4) from Peirce projection argument + J_u commutator; Z^d bipartite lattice confirmed; cubic det(A) vanishes identically on OP^2**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-30T22:02:31Z
- **Completed:** 2026-03-30T22:08:19Z
- **Tasks:** 2
- **Files modified:** 2

## Key Results

- Frame stabilizer of H_eff is Spin(9) (dim 36), not full F_4 (dim 52). Three independent proofs: algebraic (Peirce projection breaks F_4), computational (||[H_2, J_u^total]|| = 24.0), spectral (multiplicities = C(9,k)). SSB pattern F_4 -> Spin(9), target space OP^2 (dim 16). [CONFIDENCE: HIGH]
- Physical lattice is Z^d (bipartite, DLS-compatible). K_3 Peirce graph is on-site algebraic structure. 6-step argument explicitly resolves the K_3 non-bipartiteness concern. [CONFIDENCE: HIGH]
- Cubic det(A) vanishes identically on OP^2 = F_4/Spin(9) because OP^2 consists of rank-1 projections with det = 0. This geometric argument supersedes the Z_2 sublattice argument (which fails for ferromagnets) and eliminates cubic corrections to the sigma model. [CONFIDENCE: HIGH]
- Goldstone modes: 16 broken generators. Type I (linear, 16 modes) vs Type II (quadratic, 8 modes) depends on symplectic form rank -- deferred to Phase 39. [CONFIDENCE: MEDIUM]

## Task Commits

1. **Task 1: Frame stabilizer identification in F_4** - `29cc33a` (derive)
2. **Task 2: Lattice structure, cubic assessment, and Phase 39 handoff** - `d69e4e8` (derive)

## Files Created/Modified

- `code/effective_hamiltonian.py` - Added test_f4_beyond_spin9() and frame_stabilizer_analysis()
- `derivations/38-lattice-and-symmetry.md` - Lattice structure argument, frame stabilizer proof, cubic assessment, Phase 39 handoff

## Next Phase Readiness

- SSB pattern F_4 -> Spin(9) confirmed -- Phase 39 can construct sigma model on OP^2
- Bipartite lattice confirmed -- DLS infrared bounds applicable
- Cubic term absent from sigma model -- bilinear H_eff sufficient
- Ferro ground state flagged -- Phase 39 must determine Goldstone type (I vs II)
- UC1-UC4 verification roadmap documented in handoff

## Contract Coverage

- claim-frame-stabilizer -> passed (Spin(9), three independent proofs)
- claim-lattice-bipartite -> passed (Z^d bipartite, K_3 on-site)
- claim-cubic-assessment -> passed (det = 0 on OP^2, geometric argument)
- deliv-symmetry-code -> passed (code/effective_hamiltonian.py)
- deliv-derivation -> passed (derivations/38-lattice-and-symmetry.md)
- test-f4-commutation -> passed (||[H_2,J_u]|| = 24.0)
- test-stabilizer-dimension -> passed (dim 36, matches F_4 maximal subgroup)
- test-lattice-argument -> passed (6-step argument)
- test-cubic-scaling -> passed (dim 3/2, coefficient = 0)
- ref-baez2002 -> completed (read, cite)
- ref-todorov-drenska -> completed (compare)
- ref-dls-bipartite -> completed (cite)
- ref-plan01-spectrum -> completed (read)
- fp-assumed-spin9 -> rejected
- fp-assumed-bipartite -> rejected
- fp-ignored-cubic -> rejected

## Equations Derived

**Eq. (38.5): Frame stabilizer result**

$$
[H_2, J_u^{\mathrm{total}}] \neq 0, \quad \|[H_2, J_u^{\mathrm{total}}]\|_F = 24.0
$$

Implies $\mathrm{Stab}_{F_4}(H_{\text{eff}}) = \mathrm{Spin}(9)$, not $F_4$.

**Eq. (38.6): SSB target space**

$$
F_4 \to \mathrm{Spin}(9), \quad F_4/\mathrm{Spin}(9) = \mathbb{OP}^2, \quad \dim(\mathbb{OP}^2) = 16
$$

**Eq. (38.7): Cubic vanishing on OP^2**

$$
\det(\phi) = 0 \quad \forall \phi \in \mathbb{OP}^2 = \{p \in \mathfrak{h}_3(\mathbb{O}) : p^2 = p, \mathrm{Tr}(p) = 1\}
$$

## Validations Completed

- Frame stabilizer: algebraic (Peirce projection argument), computational (J_u commutator = 24.0), spectral (C(9,k) multiplicities, no F_4 enhancement)
- J_u properties: antisymmetric (exact), J_u^2 = -I (exact), NOT in spin(9) (86.6% residual)
- Spin(9) is valid F_4 maximal subgroup (Todorov-Drenska cross-check)
- Lattice bipartiteness: standard checkerboard decomposition of Z^d
- Cubic: det(E_11) = det(E_22) = det(E_33) = 0 verified explicitly
- All 16 existing tests pass (no regression)

## Decisions Made

- Replaced plan's Z_2 sublattice symmetry argument (AFM-specific) with geometric det=0 argument (universal). The plan was written assuming antiferromagnetic ground state; Plan 01 found ferromagnetic. The geometric argument is strictly stronger and applies to both cases.
- Deferred Goldstone mode type determination to Phase 39. The Type I vs Type II question requires computing the symplectic form rank on the lattice ground state, which is beyond Phase 38 scope.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 5 - Physics redirect] Cubic det(A) symmetry argument corrected for ferromagnetic ground state**

- **Found during:** Task 2 (cubic assessment)
- **Issue:** Plan assumed antiferromagnetic ground state and used sublattice Z_2 symmetry (A -> -A) to forbid cubic. Plan 01 found FERROMAGNETIC ground state, invalidating this argument.
- **Fix:** Replaced with geometric argument: det(phi) = 0 for all phi in OP^2 because OP^2 = {rank-1 projections} and rank-1 => det = 0. This is STRONGER (exact zero, not symmetry-forbidden) and applies universally.
- **Files modified:** derivations/38-lattice-and-symmetry.md
- **Verification:** det(E_11) = det(E_22) = det(E_33) = 0 verified; F_4-transitivity on OP^2 extends to all points.
- **Committed in:** d69e4e8

---

**Total deviations:** 1 auto-fixed (physics redirect -- upgraded from symmetry argument to geometric argument)
**Impact on plan:** Result is stronger than planned. No scope change.

## Issues Encountered

None.

## Open Questions

- Goldstone mode type (I vs II): ferromagnetic ground state allows Type-II Goldstone modes with quadratic dispersion. Must compute symplectic form rank in Phase 39.
- Physical significance of S_9 being a real representation of Spin(9): this determines whether Goldstone modes are Type I (all 16 independent) or could pair into Type II (8 modes).

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Stabilizer dimension | dim(H) | 36 | exact | algebraic + computational | all J |
| Broken generators | dim(F_4/H) | 16 | exact | 52 - 36 | all J |
| J_u commutator norm | ||[H_2,J_u]|| | 24.0 | exact | eigh + matrix multiply | all J |
| Cubic on OP^2 | det(phi) | 0 | exact | geometric (rank-1) | all phi in OP^2 |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|---------------|----------------|
| Bilinear truncation (no cubic) | ALWAYS on OP^2 | zero (det = 0 exactly) | never (geometric constraint) |
| Nearest-neighbor only | short-range coupling | O(k_2/k_1) ~ O(1/2) | V_0-mediated indirect coupling dominates |

---

_Phase: 38-effective-hamiltonian-from-peirce-multiplication, Plan: 02_
_Completed: 2026-03-30_
