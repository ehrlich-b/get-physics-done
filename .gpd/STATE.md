# Research State

## Project Reference

See: .gpd/PROJECT.md (updated 2026-03-20)

**Machine-readable scoping contract:** `.gpd/state.json` field `project_contract`

**Core research question:** Does the sequential product structure of self-modeling systems satisfy van de Wetering's axioms S1-S7, thereby deriving quantum mechanics from a single operational premise?
**Current focus:** Phase 5 COMPLETE -- Phase 6 next (Paper Assembly)

## Current Position

**Current Phase:** 6
**Current Phase Name:** Paper Assembly
**Total Phases:** 4 (Phases 4-7; v1.0 Phases 1-3 complete)
**Current Plan:** --
**Total Plans in Phase:** TBD
**Status:** Phase 5 complete; ready to plan Phase 6
**Last Activity:** 2026-03-21
**Last Activity Description:** Phase 5 complete -- local tomography proved, all non-complex types excluded, C*-algebra promotion established, verification passed (6/6)

**Progress:** [██████████] 100% (Phase 5)

## Active Calculations

None (Phase 5 complete, Phase 6 not started).

## Intermediate Results

### Phase 5 Results (Local Tomography from B-M Compositionality)
- **Composite OUS V_BM formalized** with product-form SP; S1-S7 inherited from factors (HIGH)
- **Local tomography proved**: dim(V_BM) = dim(V_B) * dim(V_M) via EJA trace form non-degeneracy + composite minimality (HIGH)
- **Correlation form**: B(a, b) = tau(a * phi^{-1}(b)) -- non-degenerate on simple EJA (HIGH)
- **Negative checks**: real (9!=10) and quaternionic (36!=28) correctly excluded (HIGH)
- **658+ SymPy tests** on V_3 tensor V_3 all pass (HIGH)
- **Researcher checkpoint APPROVED** (HIGH)

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

- RESOLVED: B-M independent accessibility implies local tomography (proved in Plan 05-01)
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
| 05-01 | 28min    | 3     | 3     |
| 05-02 | 15min    | 2     | 2     |

## Accumulated Context

### Decisions

Full log: `.gpd/DECISIONS.md`

**Recent high-impact:**
- [Phase 5, Plan 01]: Composite V_BM defined as MINIMAL OUS with product-form SP
- [Phase 5, Plan 01]: Correlation form B(a,b) = tau(a * phi^{-1}(b)) bridges faithful tracking to local tomography
- [Phase 5, Plan 01]: Entangled sector eliminated via minimality + SP closure + non-degeneracy
- [Phase 5, Plan 01]: Researcher approved -- load-bearing: non-degeneracy -> span d_B*d_M -> equals maximal for complex only
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
- Composite product: (a tensor b) & (c tensor d) = (a & c) tensor (b & d)
- Local tomography: dim(V_BM) = dim(V_B) * dim(V_M)

### Propagated Uncertainties

None yet.

### Pending Todos

None yet.

### Blockers/Concerns

- RESOLVED: Circularity risk -- local tomography derived without importing C*-structure (circularity audit passed)
- Minimality assumption for composite: physically justified for complex QM (minimal = maximal) but a substantive choice

## Session Continuity

**Last session:** 2026-03-21
**Stopped at:** Phase 5 complete; ready to plan Phase 6 (Paper Assembly)
**Resume file:** --
