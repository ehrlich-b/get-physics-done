# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-20)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Does the sequential product structure of self-modeling systems satisfy van de Wetering's axioms S1-S7, thereby deriving quantum mechanics from a single operational premise?
**Current focus:** Phase 4 -- Sequential Product Formalization

## Current Position

**Current Phase:** 4
**Current Phase Name:** Sequential Product Formalization
**Total Phases:** 4 (Phases 4-7; v1.0 Phases 1-3 complete)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Ready to plan
**Last Activity:** 2026-03-20
**Last Activity Description:** Roadmap created for v2.0 milestone

**Progress:** [░░░░░░░░░░] 0%

## Active Calculations

None yet.

## Intermediate Results

None yet (v1.0 results archived in MILESTONES.md).

## Open Questions

- Which effect algebra framing is correct for the self-modeling sequential product (effects on B vs B x M)?
- Whether S4 (symmetry of orthogonality) holds for the self-modeling construction
- Whether B-M independent accessibility implies local tomography
- Does the self-modeling framework admit a qubit-like 2-dimensional subsystem?
- Is the self-modeling sequential product non-associative?

## Performance Metrics

(v1.0 metrics archived in MILESTONES.md)

| Label | Duration | Tasks | Files |
| ----- | -------- | ----- | ----- |
| -     | -        | -     | -     |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [Phase 0]: Sequential product route chosen over direct involution construction (van de Wetering axioms give cleaner path; D'Ariano as backup)
- [Phase 0]: Explore both effect algebra framings in Phase 4 (correct framing is a result, not a premise)
- [Phase 0]: Non-associativity check ordered early in Phase 4 (kills the program if it fails)
- [Phase 0]: Roadmap created with 4 phases (4-7), Phase 7 contingency only

### Active Approximations

None (algebraic proof work, no approximations).

**Convention Lock:**

- Metric signature: N/A (algebraic/categorical project)
- Natural units: N/A (dimensionless algebraic work)
- All other convention fields: N/A

*Custom conventions:*
- Entropy Base: nats (natural logarithm)
- Mutual Information: I(B;M) = H(B) + H(M) - H(B,M)
- Experiential Density: rho(p) = I(B;M) * (1 - I(B;M)/H(B))
- Sequential product notation: a . b (dot notation, per van de Wetering journal version)
- Jordan product: a o b = (1/2)(a . b + b . a)
- Orthogonality: a perp b iff a . b = 0
- Axiom source: van de Wetering arXiv:1803.11139 EXCLUSIVELY (not Gudder-Greechie)

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

- S4 is the single-point-of-failure with no independent cross-check method
- Circularity risk: update map must use ONLY order unit space primitives

## Session Continuity

**Last session:** 2026-03-20
**Stopped at:** Roadmap created for v2.0; ready to plan Phase 4
**Resume file:** --
