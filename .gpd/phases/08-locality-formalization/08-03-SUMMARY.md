---
phase: 08-locality-formalization
plan: 03
depth: full
one-liner: "Computed v_LR = 8eJ/(e-1) for self-modeling SWAP Hamiltonian on Z^1; verified all Paper 5 composite OUS axioms C1-C4 and product-form SP to machine precision; confirmed light cone on N=8 chain"
subsystem: formalism
tags: [lieb-robinson, lattice, locality, self-modeling, heisenberg, causal-structure, paper5-compatibility]

requires:
  - phase: 08-locality-formalization
    plan: 01
    provides: "h_{xy} = J*F (SWAP interaction), locality mapping, lattice definition"
  - phase: 08-locality-formalization
    plan: 02
    provides: "NS LR bound framework with C_a, ||Phi||_a, v_LR formulas"
provides:
  - "v_LR = 2zJe^a C_a / a for self-modeling Hamiltonian (= Heisenberg) on Z^d"
  - "Explicit constants: C_LR, mu_LR, v_LR for Z^1, Z^2, Z^3"
  - "Paper 5 C1-C4 + product-form SP verified for lattice two-site system"
  - "Light cone confirmed numerically on N=8 chain"
  - "Complete Phase 8 deliverables: LOCL-01 (lattice) + LOCL-02 (LR bounds)"
affects: [09-area-law, 10-jacobson, 11-numerics]

methods:
  added: [NS LR velocity applied to self-modeling interaction, composite OUS axiom verification, light cone simulation via exact diagonalization]
  patterns: [self-modeling h_{xy} = J*F identical to Heisenberg, v_LR independent of n]

key-files:
  created:
    - derivations/08-lr-self-modeling.md
    - code/self_modeling_lr_velocity.py
    - .gpd/phases/08-locality-formalization/08-03-SUMMARY.md

key-decisions:
  - "v_LR monotonically decreasing in a for all Z^d tested (d=1,2,3); no finite optimizer -- report a=1 as reference"
  - "Self-modeling Hamiltonian IS Heisenberg for n=2, so v_LR^SM/v_LR^Heis = 1 exactly"

patterns-established:
  - "v_LR is independent of local dimension n (||F|| = 1 for all n >= 2)"
  - "Phase 8 complete: lattice defined, locality mapped, v_LR computed, Paper 5 compatible"

conventions:
  - "natural units (hbar = c = k_B = 1)"
  - "lattice spacing a_lat = 1"
  - "H = sum h_{xy} (no 1/2)"
  - "a & b = Luders product a^{1/2}ba^{1/2}"
  - "(a tensor b) & (c tensor d) = (a & c) tensor (b & d)"
  - "[A,B] = AB - BA"

plan_contract_ref: ".gpd/phases/08-locality-formalization/08-03-PLAN.md#/contract"

contract_results:
  claims:
    claim-lr-velocity:
      status: passed
      summary: "v_LR = 8eJ/(e-1) = 12.66J computed for Z^1 with explicit C_LR = 1.718, mu_LR = 1; also computed for Z^2 (80.08J) and Z^3 (297.92J)"
      linked_ids: [deliv-lr-computation, deliv-lr-code, test-lr-explicit, test-lr-dimensional, test-lr-limits, ref-nachtergaele-sims-phase8, ref-lieb-robinson-phase8]
      evidence:
        - verifier: self
          method: NS framework application + numerical verification
          confidence: high
          claim_id: claim-lr-velocity
          deliverable_id: deliv-lr-computation
          acceptance_test_id: test-lr-explicit
    claim-paper5-compatibility:
      status: passed
      summary: "Lattice two-site system satisfies all Paper 5 composite OUS axioms C1-C4 and product-form SP to machine precision (25 random trials each, max error 3.07e-16)"
      linked_ids: [deliv-compatibility-check, deliv-lr-code, test-c1c4, test-product-sp, ref-paper5-phase8]
      evidence:
        - verifier: self
          method: numerical verification with 25 random inputs per axiom
          confidence: high
          claim_id: claim-paper5-compatibility
          deliverable_id: deliv-compatibility-check
          acceptance_test_id: test-c1c4
    claim-causal-structure:
      status: passed
      summary: "Self-modeling lattice has effective causal structure with light cone slope v_LR; confirmed by N=8 chain simulation showing all commutator norms within LR bound"
      linked_ids: [deliv-causal-structure, deliv-lr-code, test-light-cone, ref-nachtergaele-sims-phase8]
      evidence:
        - verifier: self
          method: exact diagonalization light cone simulation
          confidence: high
          claim_id: claim-causal-structure
          deliverable_id: deliv-causal-structure
          acceptance_test_id: test-light-cone
  deliverables:
    deliv-lr-computation:
      status: passed
      path: derivations/08-lr-self-modeling.md
      summary: "Parts A-D: interaction norm, v_LR for Z^1/Z^2/Z^3, full LR bound constants, Heisenberg comparison, effective causal structure"
      linked_ids: [claim-lr-velocity, test-lr-explicit, test-lr-dimensional]
    deliv-compatibility-check:
      status: passed
      path: derivations/08-lr-self-modeling.md
      summary: "Parts E-F: C1 (dimension 16=4x4), C2 (I4), C3 (product states), C4 (non-signaling < 2.2e-16), product-form SP (error < 3.1e-16)"
      linked_ids: [claim-paper5-compatibility, test-c1c4, test-product-sp]
    deliv-causal-structure:
      status: passed
      path: derivations/08-lr-self-modeling.md
      summary: "Part D: effective light cone statement, interpretation for Phase 9 (area law), Phase 10 (Jacobson), Phase 11 (numerics)"
      linked_ids: [claim-causal-structure, test-light-cone]
    deliv-lr-code:
      status: passed
      path: code/self_modeling_lr_velocity.py
      summary: "Contains compute_self_modeling_lr_velocity(), verify_composite_ous(), verify_product_sp(), verify_light_cone() -- all pass"
      linked_ids: [claim-lr-velocity, claim-paper5-compatibility, claim-causal-structure]
  acceptance_tests:
    test-lr-explicit:
      status: passed
      summary: "v_LR = 12.6558 J on Z^1, v_LR = 80.0848 J on Z^2, v_LR = 297.9171 J on Z^3 -- all explicit numerical values at a=1"
      linked_ids: [claim-lr-velocity, deliv-lr-computation, deliv-lr-code]
    test-lr-dimensional:
      status: passed
      summary: "[v_LR] = [J] = [energy] = [1/time] in natural units with a_lat = 1. Consistent with velocity."
      linked_ids: [claim-lr-velocity, deliv-lr-computation]
    test-lr-limits:
      status: passed
      summary: "J -> 0: v_LR = 0. J > 0: v_LR = 12.66 > 0. v_LR(2J)/v_LR(J) = 2.000000. All three limits correct."
      linked_ids: [claim-lr-velocity, deliv-lr-code]
    test-c1c4:
      status: passed
      summary: "C1: dim 16 = 4x4, embedding verified for 25 random products. C2: ||I2 tensor I2 - I4|| = 0. C3: 25 product states positive, trace 1, expectations factor. C4: max NS violation 2.2e-16 over 25 entangled states."
      linked_ids: [claim-paper5-compatibility, deliv-compatibility-check]
    test-product-sp:
      status: passed
      summary: "25 random effect quadruples: max ||LHS - RHS|| = 3.07e-16 < 1e-10 threshold"
      linked_ids: [claim-paper5-compatibility, deliv-lr-code]
    test-light-cone:
      status: passed
      summary: "N=8 chain, J=1, 21 time points x 7 sites = 147 data points. All commutator norms within LR bound. Wavefront at t=0.1: r=3 gives 1.6e-3, r=5 gives 2.0e-6, r=7 gives 1.2e-9 (exponential decay outside cone)."
      linked_ids: [claim-causal-structure, deliv-lr-code]
  references:
    ref-paper5-phase8:
      status: completed
      completed_actions: [read, compare]
      missing_actions: []
      summary: "Paper 5 composite OUS axioms C1-C4 and product-form SP read from paper/sections/composite-lt.tex; lattice two-site system verified to reproduce all axioms"
    ref-nachtergaele-sims-phase8:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "NS LR bound framework (Theorem 3.4 equivalent) applied to self-modeling Hamiltonian; cited as primary method source"
    ref-lieb-robinson-phase8:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Original LR bound cited as historical anchor for finite group velocity result"
  forbidden_proxies:
    fp-cite-without-compute-phase8:
      status: rejected
      notes: "v_LR explicitly computed as 8eJ/(e-1) = 12.66J for Z^1, with C_LR = 1.718, mu_LR = 1. Not just 'LR bounds apply'."
    fp-assume-compatibility:
      status: rejected
      notes: "Compatibility verified numerically: 25 trials for C1-C4, 25 trials for product-form SP, all to machine precision. Not assumed."
  uncertainty_markers:
    weakest_anchors:
      - "v_LR is an upper bound; actual propagation speed may be slower by a constant factor"
      - "v_LR(a) is monotonically decreasing in a for Z^1-Z^3 with exponential F-function; the reported a=1 value is a representative point, not a tight bound"
    unvalidated_assumptions:
      - "Exponential F-function may not be optimal for the self-modeling interaction (Wang-Hazzard improved bounds may be tighter)"
    competing_explanations: []
    disconfirming_observations: []

comparison_verdicts:
  - subject_id: test-lr-explicit
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-nachtergaele-sims-phase8
    comparison_kind: benchmark
    metric: analytical_match
    threshold: "machine precision"
    verdict: pass
    recommended_action: "None -- v_LR correctly computed"
    notes: "Self-modeling h_{xy} = JF identical to Heisenberg; v_LR = 8eJ/(e-1) matches Plan 02 benchmark exactly"
  - subject_id: test-c1c4
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-paper5-phase8
    comparison_kind: benchmark
    metric: numerical_match
    threshold: "< 1e-10"
    verdict: pass
    recommended_action: "None -- all axioms verified"
    notes: "Max error across all axiom checks: 2.2e-16 (C4 non-signaling)"
  - subject_id: test-product-sp
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-paper5-phase8
    comparison_kind: benchmark
    metric: relative_error
    threshold: "< 1e-10"
    verdict: pass
    recommended_action: "None -- SP verified to machine precision"
    notes: "Max ||LHS - RHS|| = 3.07e-16 over 25 random quadruples"

duration: 15min
completed: 2026-03-22
---

# Plan 08-03: LR Velocity for Self-Modeling Hamiltonian and Paper 5 Compatibility

**Computed v_LR = 8eJ/(e-1) for self-modeling SWAP Hamiltonian on Z^1; verified all Paper 5 composite OUS axioms C1-C4 and product-form SP to machine precision; confirmed light cone on N=8 chain**

## Performance

- **Duration:** ~15 min
- **Started:** 2026-03-22T01:06:51Z
- **Completed:** 2026-03-22T01:22:00Z
- **Tasks:** 2
- **Files modified:** 3

## Key Results

- **v_LR = 8eJ/(e-1) = 12.66J** on Z^1 for the self-modeling Hamiltonian h_{xy} = JF (SWAP) [CONFIDENCE: HIGH]
- The self-modeling Hamiltonian IS the isotropic Heisenberg model for n=2, so v_LR^SM / v_LR^Heisenberg = 1 exactly [CONFIDENCE: HIGH]
- v_LR is independent of local dimension n (since ||F_n|| = 1 for all n >= 2) [CONFIDENCE: HIGH]
- Paper 5 composite OUS axioms C1-C4 all verified numerically to machine precision [CONFIDENCE: HIGH]
- Product-form SP verified: max error 3.07e-16 over 25 random effect quadruples [CONFIDENCE: HIGH]
- Light cone confirmed on N=8 chain: all 147 commutator measurements within LR bound [CONFIDENCE: HIGH]

## Task Commits

1. **Task 1: LR velocity computation + Paper 5 verification code** - `baaa539` (derive)
2. **Task 2: SUMMARY.md** - (this commit)

## Files Created/Modified

- `derivations/08-lr-self-modeling.md` - LR velocity derivation (Parts A-D), Paper 5 compatibility (Parts E-F), Phase 8 summary (Part G)
- `code/self_modeling_lr_velocity.py` - Numerical verification: LR velocity, C1-C4, product-form SP, light cone simulation
- `.gpd/phases/08-locality-formalization/08-03-SUMMARY.md` - This summary

## Next Phase Readiness

- **Phase 9 (Area Law):** Hamiltonian H = sum JF_{xy} ready; v_LR provides locality input; key open question is sign of J (AFM: gapless with log corrections; FM: gapped with trivial area law)
- **Phase 10 (Jacobson):** v_LR = emergent speed of light; effective causal structure established; continuum limit procedure TBD
- **Phase 11 (Numerics):** Timescales set by v_LR; exact diagonalization verified for N=8; larger chains may need DMRG
- **Phase 8 complete:** All 5 ROADMAP success criteria addressed (lattice, locality mapping, v_LR, BR compatibility, Paper 5 LT compatibility)

## Contract Coverage

- Claim IDs advanced: claim-lr-velocity -> passed, claim-paper5-compatibility -> passed, claim-causal-structure -> passed
- Deliverable IDs produced: deliv-lr-computation -> passed, deliv-compatibility-check -> passed, deliv-causal-structure -> passed, deliv-lr-code -> passed
- Acceptance test IDs run: test-lr-explicit -> passed, test-lr-dimensional -> passed, test-lr-limits -> passed, test-c1c4 -> passed, test-product-sp -> passed, test-light-cone -> passed
- Reference IDs surfaced: ref-paper5-phase8 -> completed (read, compare), ref-nachtergaele-sims-phase8 -> completed (read, cite), ref-lieb-robinson-phase8 -> completed (cite)
- Forbidden proxies rejected: fp-cite-without-compute-phase8 -> rejected (explicit computation), fp-assume-compatibility -> rejected (numerical verification)
- Decisive comparison verdicts: test-lr-explicit -> pass, test-c1c4 -> pass, test-product-sp -> pass

## Equations Derived

**Eq. (08-03.1): Self-modeling interaction norm**

$$\|h_{xy}^{\mathrm{int}}\| = \|JF\| = |J|, \quad \|F\| = 1 \; \forall \, n \geq 2$$

**Eq. (08-03.2): Self-modeling LR velocity on Z^d**

$$v_{LR}(a) = \frac{2zJe^a}{a}\left[\left(\coth\frac{a}{2}\right)^d - 1\right]$$

identical to Heisenberg benchmark (Plan 02, Eq. 12).

**Eq. (08-03.3): Z^1 reference value**

$$v_{LR}(a=1) = \frac{8eJ}{e-1} \approx 12.66 \, J$$

**Eq. (08-03.4): Full LR bound**

$$\|[\tau_t(A_x), B_y]\| \leq \frac{2\|A\|\|B\|}{C_a}\left(e^{2\|\Phi\|_a C_a |t|} - 1\right)e^{-a \, d(x,y)}$$

with $C_a = (\coth(a/2))^d - 1$, $\|\Phi\|_a = zJe^a$.

## Validations Completed

- **Dimensional analysis:** [v_LR] = [J] = [energy] = [1/time] in natural units with a_lat = 1. Consistent with velocity.
- **Limiting cases:** J -> 0: v_LR = 0. J > 0: v_LR > 0. v_LR(2J) = 2*v_LR(J). All pass.
- **Heisenberg comparison:** v_LR^SM / v_LR^Heis = 1 (identical interaction form).
- **n-independence:** ||F_n|| = 1 verified for n = 2, 3, 4.
- **C1:** dim(V_{xy}) = 16 = 4 * 4 = dim(V_x) * dim(V_y). 25 random embeddings verified.
- **C2:** ||I_2 tensor I_2 - I_4|| = 0 exactly.
- **C3:** 25 random product states: all positive, trace 1, expectations factor correctly.
- **C4:** 25 random entangled states: max non-signaling violation 2.2e-16.
- **Product-form SP:** 25 random quadruples: max ||LHS - RHS|| = 3.07e-16.
- **Light cone:** N=8 chain, 147 commutator measurements, all within LR bound. Wavefront decays exponentially outside cone.

## Decisions & Deviations

### Decisions

- **Monotonicity:** v_LR(a) is monotonically decreasing for Z^1, Z^2, and Z^3 (no finite minimizer for any dimension with exponential F-function). Report a=1 as reference value.
- **Task structure:** Combined code for both tasks into a single script since all verifications are tightly coupled and share utility functions.

### Deviations

None -- plan executed exactly as written.

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|---|---|---|---|---|---|
| LR velocity (Z^1) | $v_{LR}$ | 12.6558 J | exact (upper bound) | NS formula | J > 0 |
| LR velocity (Z^2) | $v_{LR}$ | 80.0848 J | exact (upper bound) | NS formula | J > 0 |
| LR velocity (Z^3) | $v_{LR}$ | 297.9171 J | exact (upper bound) | NS formula | J > 0 |
| LR prefactor (Z^1) | $C_{LR}$ | 1.7183 | exact | NS formula, a=1 | a=1 |
| LR decay rate | $\mu_{LR}$ | 1.0 | exact | a=1 | a=1 |
| Non-signaling violation | -- | 2.2e-16 | machine precision | 25 random trials | n=2 |
| SP product error | -- | 3.07e-16 | machine precision | 25 random trials | n=2 |

## Open Questions

- **Sign of J:** The SP constraints do not determine whether J > 0 (AFM) or J < 0 (FM). This affects the entanglement structure (gapless vs gapped ground state) and must be resolved for Phase 9.
- **Tighter bounds:** The NS exponential F-function gives v_LR = 12.66J on Z^1, while the classical Dyson-series bound gives 10.87J. Neither is tight; the actual propagation speed may be significantly slower. Wang-Hazzard improved bounds could give tighter values.
- **Continuum limit:** How does the discrete light cone (v_LR on the lattice) map onto a continuous spacetime light cone? This is the core question for Phase 10.

## Self-Check: PASSED

- [x] derivations/08-lr-self-modeling.md exists
- [x] code/self_modeling_lr_velocity.py exists
- [x] Checkpoint baaa539 exists in git log
- [x] All numerical tests pass (all 6 acceptance tests verified)
- [x] Convention consistency: all files use natural units, a_lat = 1, H = sum h_xy, Luders product
- [x] Contract: all 3 claim IDs passed, all 4 deliverable IDs produced, all 6 acceptance test IDs run, all 3 reference IDs surfaced, both forbidden proxies rejected

---

_Phase: 08-locality-formalization, Plan 03_
_Completed: 2026-03-22_
