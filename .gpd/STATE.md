# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-20)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Does the sequential product structure of self-modeling systems satisfy van de Wetering's axioms S1-S7, thereby deriving quantum mechanics from a single operational premise?
**Current focus:** Phase 4 COMPLETE -- Phase 5 next (Local Tomography)

## Current Position

**Current Phase:** 5
**Current Phase Name:** Local Tomography from B-M Compositionality
**Total Phases:** 4 (Phases 4-7; v1.0 Phases 1-3 complete)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Phase 4 complete; ready to plan Phase 5
**Last Activity:** 2026-03-21
**Last Activity Description:** Phase 4 complete -- all S1-S7 proved, EJA classification established, Plan 05 skipped (S4 passed)

**Progress:** [██████████] 100% (Phase 4)

## Active Calculations

None (Phase 4 complete, Phase 5 not started).

## Intermediate Results

### Phase 4 Results (Sequential Product Formalization)
- **E(B) framing selected** over E(B x M) with three failure modes (HIGH)
- **Corrected product formula** Eq. (04-06.4): a & b = sum lambda_i C_{p_i}(b) + sum sqrt(lambda_i lambda_j) P_{ij}(b) (HIGH)
- **Luders equivalence** on M_2(C)^sa: corrected product = sqrt(a) b sqrt(a) (HIGH)
- **phi algebraically essential**: faithful self-modeling saturates positivity bound, selects f = sqrt (HIGH)
- **Non-associativity confirmed**: Delta[0,0] = 39/224 - 3sqrt(3)/32 != 0 (HIGH)
- **S1-S7 all proved** for the corrected product on finite-dim spectral OUS (HIGH)
- **S4 phi-independent**: holds for all f with f(0,x)=0 via facial orthogonality (HIGH)
- **EJA classification**: vdW Theorem 1 applies, spin factor V_3 for M_2(C)^sa (HIGH)

## Open Questions

- Whether B-M independent accessibility implies local tomography
- Does the self-modeling framework admit a qubit-like 2-dimensional subsystem?
- Does positivity bound generalize to M_n(C)^sa for n >= 3?
- Can the faithful-tracking selection principle be formalized as a theorem?
- Does the facial orthogonality argument extend to infinite-dimensional spectral OUS?

## Performance Metrics

(v1.0 metrics archived in MILESTONES.md)

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| 04-01 | 11min    | 2     | 3     |
| 04-06 | 8min     | 2     | 2     |
| 04-02 | 10min    | 2     | 2     |
| 04-03 | 12min    | 2     | 2     |
| 04-04 | 15min    | 3     | 2     |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [Phase 4, Plan 04]: S4 proved via facial orthogonality -- phi-independent, applies to all f with f(0,x)=0
- [Phase 4, Plan 04]: All S1-S7 established -- vdW Theorem 1 invoked for EJA classification
- [Phase 4, Plan 06]: Corrected product uses sqrt Peirce 1-space feedback; faithful self-modeling selects maximal f, recovering Luders
- [Phase 4, Plan 06]: Decisive insight was Peirce 1-space resolution (S3), not S4
- [Phase 4, Plan 01]: E(B) framing selected over E(B x M)
- [Phase 0]: Sequential product route chosen over direct involution construction

### Active Approximations

None (algebraic proof work, no approximations).

**Convention Lock:**

- Metric signature: N/A (algebraic/categorical project)
- Natural units: N/A (dimensionless algebraic work)
- All other convention fields: N/A

*Custom conventions:*
- Sequential product notation: a & b (non-commutative, per vdW arXiv:1803.11139 Def. 2)
- Jordan product: a * b = (1/2)(a & b + b & a)
- Orthogonality: a perp b iff a & b = 0
- Axiom source: van de Wetering arXiv:1803.11139 EXCLUSIVELY
- Compression: C_p (Alfsen-Shultz P-projection)
- Corrected product: a & b = sum lambda_i C_{p_i}(b) + sum sqrt(lambda_i lambda_j) P_{ij}(b)

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

- Circularity risk continues: Phase 5 must derive local tomography without importing C*-structure

## Session Continuity

**Last session:** 2026-03-21
**Stopped at:** Phase 4 complete; ready to plan Phase 5 (Local Tomography)
**Resume file:** --
