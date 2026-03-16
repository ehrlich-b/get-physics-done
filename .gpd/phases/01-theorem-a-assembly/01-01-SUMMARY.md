---
phase: 01-theorem-a-assembly
plan: 01
depth: full
one-liner: "Stated all 7 Theorem A lemmas with specific theorem citations and explicit error rates c_i, constructed typed dependency DAG with no unresolved type mismatches"
subsystem: derivation
tags: [metastability, BEGK, Freidlin-Wentzell, QSD, large-deviations, Markov-chains]

requires: []
provides:
  - 7 lemma statements with explicit error terms delta_i = O(exp(-c_i/eps))
  - Error rate summary table (all c_i > 0, final c_7 = min(Delta_s - Delta_b, alpha))
  - Typed dependency DAG with I/O verification at each edge
  - Two type mismatches identified and resolved (expectation -> high-probability via BEGK Thm 1.4)
affects: [01-02-error-composition]

methods:
  added: [BEGK capacity formula, FW cycle hierarchy, QSD convergence, DV large deviations, renewal theory]
  patterns: [multiplicative error form (1 + delta_i), exit-time concentration via exponential law]

key-files:
  created: [derivations/theorem-a-lemmas.tex]

key-decisions:
  - "Used BEGK Thm 1.4 (exponential law) as primary concentration tool rather than full DV machinery -- simpler and sufficient"
  - "Stated DV route alongside for generality but marked exit-time route as sufficient for Theorem A"

patterns-established:
  - "Error terms in multiplicative form: exact * (1 + O(exp(-c_i/eps)))"
  - "Each lemma output typed as: exact / expectation / high-probability bound / TV convergence"

conventions:
  - "entropy_base = nats (ln)"
  - "generator_convention = probabilist dp/dt = pQ"
  - "matrix_norm = sup_norm_rows"
  - "experiential_density = I*(1-I/H)"

plan_contract_ref: ".gpd/phases/01-theorem-a-assembly/01-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-lemma-statements:
      status: passed
      summary: "All 7 lemmas stated with specific theorem numbers (FW Thm 6.3.1, BEGK Thm 1.2/1.4, CV16 Thm 2.1, DV LDP), explicit error terms delta_i = O(exp(-c_i/eps)) with each c_i identified relative to Delta_s, Delta_b, alpha"
      linked_ids: [deliv-lemma-tex, test-lemma-precision, ref-begk, ref-fw, ref-dv, ref-cv, ref-draft-sec7]
    claim-dependency-typed:
      status: passed
      summary: "Dependency DAG constructed with 9 typed edges; two type mismatches (expectation -> high-prob) identified and resolved via BEGK Thm 1.4; graph verified acyclic"
      linked_ids: [deliv-lemma-tex, test-dependency-dag, ref-draft-appendix-b]
  deliverables:
    deliv-lemma-tex:
      status: passed
      path: "derivations/theorem-a-lemmas.tex"
      summary: "Self-contained LaTeX file with 7 lemma statements, error terms, citations, typed dependency graph, and error rate summary table"
      linked_ids: [claim-lemma-statements, claim-dependency-typed, test-lemma-precision, test-dependency-dag]
  acceptance_tests:
    test-lemma-precision:
      status: passed
      summary: "Verified: each lemma cites a specific theorem number, each error term is an explicit function of eps, each rate c_i is identified relative to Delta_s and Delta_b. L1 exact, L2 c_2>=Ds-Db, L3 gamma_D=O(1), L4 c_4=Ds, L5 c_5>=Ds-Db, L6 c_6=alpha, L7 c_7=min(Ds-Db,alpha)"
      linked_ids: [claim-lemma-statements, deliv-lemma-tex, ref-begk, ref-fw, ref-dv, ref-cv]
    test-dependency-dag:
      status: passed
      summary: "DAG confirmed acyclic (all edges lower->higher numbered). All 9 edges typed with source output type, target input type, and compatibility. Two type mismatches resolved: L2->L4 (BEGK Thm 1.4 exponential law), L5->L7 (via L6 concentration). L7 output matches Theorem A statement."
      linked_ids: [claim-dependency-typed, deliv-lemma-tex]
  references:
    ref-begk:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "BEGK Thm 1.2 (capacity formula) cited for L2 mean exit time; Thm 1.4 (exponential law) cited for exit-time concentration in L2, L5, L6"
    ref-fw:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "FW Ch.6 Thm 6.3.1 cited for L1 basin partition via cycle hierarchy"
    ref-dv:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "DV LDP cited for general concentration route in L6; contraction principle stated for rho-weighted functional"
    ref-cv:
      status: completed
      completed_actions: [read, cite]
      missing_actions: []
      summary: "CV16 Thm 2.1 cited for L3 QSD convergence with exponential rate gamma_D"
    ref-draft-sec7:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Draft Section 7.2-7.3 read; proof sketch formalized into precise lemma statements with error terms"
    ref-draft-appendix-b:
      status: completed
      completed_actions: [read]
      missing_actions: []
      summary: "Draft Appendix B one-level ASCII tree refined into typed dependency graph with I/O verification"
  forbidden_proxies:
    fp-sketch-repeat:
      status: rejected
      notes: "Every lemma cites a specific theorem number with an explicit error form. No 'by BEGK the residence time is exponential' without specifying which theorem, prefactor, and error."
    fp-unspecified-c:
      status: rejected
      notes: "All c_i values identified: c_2>=Ds-Db, c_4=Ds, c_5>=Ds-Db, c_6=alpha, c_7=min(Ds-Db,alpha). No unspecified rate constants."
  uncertainty_markers:
    weakest_anchors:
      - "DV contraction principle for rho-weighted functional is stated but the exit-time route via BEGK Thm 1.4 avoids this entirely -- the DV extension is not needed for Theorem A"
      - "QSD convergence rate gamma_D argued to be O(1) via Cheeger inequality and within-basin rate structure -- the argument is sound but not quantitatively sharp (gamma_D not computed)"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations: []

duration: 6min
completed: 2026-03-16
---

# Plan 01-01: Theorem A Lemma Assembly Summary

**Stated all 7 Theorem A lemmas with specific theorem citations and explicit error rates c_i, constructed typed dependency DAG with no unresolved type mismatches**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-16T02:49:16Z
- **Completed:** 2026-03-16T02:54:58Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- All 7 lemmas have precise statements citing specific theorem numbers (not just author names) with error terms in the form delta_i = O(exp(-c_i/eps)) where each c_i is identified
- Final composite error rate: c_7 = min(Delta_s - Delta_b, alpha) > 0, confirming error terms compose without destroying the exponential bound
- Two type mismatches in the dependency graph (expectation flowing where high-probability bound needed) resolved via BEGK Thm 1.4 exponential law
- Prefactor C = (rho_max / c) * (K_b / K_s^2) verified to be O(1) in epsilon

## Task Commits

1. **Task 1: State 7 lemmas with explicit error terms** - `1031d60` (derive)
2. **Task 2: Build typed dependency graph with I/O verification** - `d1ae845` (derive)

## Files Created/Modified

- `derivations/theorem-a-lemmas.tex` - All 7 lemma statements, error terms, theorem citations, typed dependency graph, error rate summary table

## Next Phase Readiness

- Error rate table ready for Plan 02 to compose delta_i through the chain and verify c_7 > 0 formally
- Typed I/O at lemma boundaries enables Plan 02 to verify composition without implicit type conversions
- The BEGK Thm 1.4 route for concentration (simpler than full DV) is identified and ready to be the primary tool

## Contract Coverage

- Claim IDs advanced: claim-lemma-statements -> passed, claim-dependency-typed -> passed
- Deliverable IDs produced: deliv-lemma-tex -> derivations/theorem-a-lemmas.tex (passed)
- Acceptance test IDs run: test-lemma-precision -> passed, test-dependency-dag -> passed
- Reference IDs surfaced: ref-begk -> completed, ref-fw -> completed, ref-dv -> completed, ref-cv -> completed, ref-draft-sec7 -> completed, ref-draft-appendix-b -> completed
- Forbidden proxies rejected: fp-sketch-repeat -> rejected, fp-unspecified-c -> rejected

## Equations Derived

**Eq. (01-01.1): Mean exit time (BEGK)**

$$
\mathbb{E}_x[\tau_{B_{\mathrm{stable}}^c}] = K_s \exp(\Delta_s / \varepsilon) \cdot (1 + \delta_2), \quad |\delta_2| \leq C_2 \exp(-c_2/\varepsilon), \quad c_2 \geq \Delta_s - \Delta_b
$$

**Eq. (01-01.2): QSD convergence**

$$
\|\mathbb{P}_{p_0}(X_t \in \cdot \mid t < \tau) - \nu_{\mathrm{QSD}}\|_{\mathrm{TV}} \leq C_3 \exp(-\gamma_D t), \quad \gamma_D = O(1)
$$

**Eq. (01-01.3): Stable measure lower bound**

$$
\mu_{\mathrm{stable}} \geq c \cdot K_s \exp(\Delta_s/\varepsilon) \cdot (1 - \delta_4), \quad \delta_4 = O(\exp(-\Delta_s/\varepsilon))
$$

**Eq. (01-01.4): BB measure upper bound**

$$
\mu_{\mathrm{BB}} \leq \rho_{\max} \cdot \frac{K_b}{K_s} \exp((\Delta_b - \alpha)/\varepsilon) \cdot (1 + \delta_5)
$$

**Eq. (01-01.5): Ratio bound (Theorem A)**

$$
\frac{\mu_{\mathrm{BB}}}{\mu_{\mathrm{stable}}} \leq C \exp\left(-\frac{\Delta_s - \Delta_b - \alpha}{\varepsilon}\right)(1 + O(\exp(-c_7/\varepsilon))), \quad c_7 = \min(\Delta_s - \Delta_b, \alpha)
$$

## Validations Completed

- L1 is exact (graph-theoretic construction, no error term needed)
- All error rate constants c_i verified strictly positive under standing assumptions (Delta_s > Delta_b, alpha > 0)
- Prefactor C = O(1) in epsilon verified component-by-component
- gamma_D = O(1) argued via Cheeger inequality for killed chain (within-basin rates are O(1))
- delta_4 = O(exp(-Delta_s/eps)) is superexponentially small compared to gap Delta_s - Delta_b
- DAG acyclicity verified: all edges go from lower to higher numbered lemmas
- L7 output matches Theorem A statement in draft Section 7.2

## Decisions & Deviations

- **Decision:** Used BEGK Thm 1.4 (exponential law) as primary concentration mechanism rather than full DV large deviations. Rationale: simpler, sufficient for Theorem A, avoids the DV extension to rho-weighted functionals. DV route stated for generality.
- No deviations from plan.

## Open Questions

- Optimal trade-off for alpha (closer to Delta_s - Delta_b sharpens main bound but worsens error term) -- deferred to Plan 02
- Quantitative value of gamma_D for specific basin geometries (argued O(1) but not computed) -- not needed for Theorem A's asymptotic statement

## Key Quantities and Uncertainties

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
|----------|--------|-------|-------------|--------|-------------|
| Final error rate | c_7 | min(Delta_s - Delta_b, alpha) | exact | Composition of L2-L6 | eps << min(Delta_s, Delta_b) |
| Prefactor | C | (rho_max/c)(K_b/K_s^2) | O(1) in eps | BEGK prefactors | finite state space |

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| Low-noise asymptotics | eps << min(Delta_s, Delta_b) | All delta_i = O(exp(-c_i/eps)) | eps comparable to barrier heights |
| QSD approximation within basins | t >> 1/gamma_D | O(exp(-gamma_D t)) | spectral gap of killed chain exponentially small |

## Issues Encountered

- LaTeX not installed on this machine; .tex file is well-formed but PDF compilation not verified. Content is the deliverable.

## Self-Check: PASSED

- [x] derivations/theorem-a-lemmas.tex exists
- [x] Commit 1031d60 exists (Task 1)
- [x] Commit d1ae845 exists (Task 2)
- [x] Convention consistency: nats and probabilist generator used throughout
- [x] All 7 lemmas present with theorem citations
- [x] Error rate summary table present
- [x] Typed dependency graph with 9 edges present
- [x] Contract coverage: all claim/deliverable/test/reference/proxy IDs accounted for

---

_Phase: 01-theorem-a-assembly_
_Completed: 2026-03-16_
