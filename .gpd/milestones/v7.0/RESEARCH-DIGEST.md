# Research Digest: v7.0 Arrow of Time, Complexification, and Evolutionary Selection

Generated: 2026-03-26
Milestone: v7.0
Phases: 23-27

## Narrative Arc

Paper 7 left Gap C open: the complexification of the Peirce half-space V_{1/2} = O^2 to S_{10}^+ is needed for the SM chirality result but is not forced by the Jordan algebra structure of h_3(O). v6.0 proved this algebraic obstruction is genuine (V_1 = R bottleneck). v7.0 attacked from the thermodynamic direction: Phase 23 derived the CPTP depolarizing channel for SWAP dynamics and characterized entropy behavior (monotonic increase under repeated interactions, oscillation for 2-site). Phase 24 proved that chirality requires time-orientation (Cl(d-1,1) volume form flips under T) and established the three-consequence theorem (single u in S^6 determines gauge + chirality + time-orientation requirement). Phase 25 derived the Landauer bound W >= kT I(B;M) on self-modeling and closed the coherence loophole via three independent arguments. Phase 26 synthesized these into the entropy gradient theorem (three independent routes) and narrowed Gap C: complexification is necessary for SM-like observers, but non-SM self-modelers in non-complexified blocks remain open. Phase 27 extracted quantitative predictions (Landauer bound 94 orders weaker than Penrose estimate, rho profile peaks at I = S_B/2). Paper 8 was drafted, reviewed (critical logic error in selection chain found and fixed), and revised to minor-revision status.

**Honest assessment:** The original goal was to close Gap C via thermodynamic selection (rho = 0 for all non-complexified blocks). This was weakened during peer review: the contrapositive logic in the selection chain was invalid. The final result narrows Gap C for SM-like observers only. The math (entropy gradient theorem, Landauer bound, three-consequence theorem) is solid; the gap-closing claim is weaker than intended.

## Key Results

| Phase | Result | Equation / Value | Validity Range | Confidence |
| ----- | ------ | ---------------- | -------------- | ---------- |
| 23 | CPTP depolarizing channel | E(rho) = (1-p)rho + p(I/2), p = sin^2(Jt) | M_2(C) x M_2(C) SWAP | HIGH |
| 23 | Monotonic entropy increase | Delta S >= 0 under repeated interactions with fresh bath | Iterated SWAP, maximally mixed bath | HIGH |
| 24 | Chirality-time theorem | Gamma_* -> -Gamma_* under T; P_L <-> P_R | Lorentzian Cl(d-1,1), even d | HIGH |
| 24 | Three-consequence theorem | u in S^6 -> gauge + chirality + time-orientation | Conditional on A6-A7 (continuum, Lorentzian) | HIGH |
| 25 | Landauer bound on self-modeling | W >= kT I(B;M) per cycle | Finite-dim QM, thermal contact | HIGH |
| 25 | Coherence loophole closed | 3 independent arguments | CPTP, thermal, Sagawa-Ueda | HIGH |
| 25 | Chain theorem | self-modeling -> free energy -> non-equilibrium -> entropy gradient | A1-A3 | HIGH |
| 26 | Entropy gradient theorem | S(t) < S_max for self-modelers with rho > 0 | 3 routes with different assumption subsets | HIGH |
| 26 | Gap C narrowed | Complexification necessary for SM-like observers | SM-specific; non-SM blocks open | MEDIUM |
| 27 | Landauer deficit | ~10^28 nats (94 orders below Penrose 10^122) | Model-dependent on d_M, nu | MEDIUM |
| 27 | Exhaustion ratio | N_exhaust/N_Hubble ~ 10^93 | Model-dependent on S_max | MEDIUM |

## Methods Employed

- **Phase 23:** CPTP channel derivation from partial trace of SWAP unitary; von Neumann entropy analysis; depolarizing channel identification
- **Phase 24:** Clifford algebra volume form analysis in Lorentzian signature; spin structure hierarchy (framing => spin => orientable)
- **Phase 25:** Landauer-Bennett-Reeb-Wolf quantum thermodynamics; Sagawa-Ueda generalized Jarzynski; CPTP decoherence analysis
- **Phase 26:** Three independent proof routes (Direct/Boundary/rho selection); assumption register methodology
- **Phase 27:** Order-of-magnitude estimation; cosmological parameter analysis; sensitivity analysis

## Convention Evolution

| Phase | Convention | Description | Status |
| ----- | ---------- | ----------- | ------ |
| 23 | natural_units=kB_equals_1 | Entropy in nats, kB = 1 | Active |
| 23 | entropy_base=nats | Von Neumann entropy S = -Tr(rho ln rho) | Active |
| 24 | clifford_convention=euclidean_positive | gamma_i gamma_j + gamma_j gamma_i = 2 delta_ij | Active |
| 24 | complex_structure=u_equals_e7 | u = e_7 as complex structure on Im(O) | Active |
| 25 | jordan_product=(1/2)(ab+ba) | Standard Jordan product | Active |
| All | spin_representation=S10plus_boyle | Following Boyle 2020 conventions | Active |
| All | pati_salam=SU4xSU2LxSU2R | Pati-Salam gauge group convention | Active |

## Figures and Data Registry

| File | Phase | Description | Paper-ready? |
| ---- | ----- | ----------- | ------------ |
| paper8/sections/*.tex | All | Paper 8 manuscript (10 sections + 2 appendices) | Yes |
| paper8/refs.bib | All | 21 bibliography entries, verified | Yes |

## Open Questions

1. Can non-SM self-modelers exist in non-complexified blocks? (Gap C not fully closed)
2. Does the spectral action (Connes-Chamseddine-Marcolli) emerge from the framework?
3. What selects 3 generations? (Gap Gen)
4. Can the Past Hypothesis be derived from first principles (not just observer-selected)?
5. Is there an h_3(O)-specific mechanism for complexification beyond extension of scalars?

## Dependency Graph

    Phase 23 "Entropy Increase"
      provides: CPTP channel, entropy monotonicity, depolarizing parameter
      requires: Paper 5 (Luders), Paper 6 (SWAP)
    Phase 24 "Chirality-Time" (parallel with 23)
      provides: chirality-time theorem, three-consequence theorem
      requires: Paper 7 (Cl(6) chirality), Lawson-Michelsohn
    -> Phase 25 "Landauer/Free Energy"
      provides: Landauer bound, coherence closure, chain theorem
      requires: Phase 23 (entropy result)
    -> Phase 26 "Entropy Gradient + Gap C"
      provides: entropy gradient theorem, Gap C narrowing, master theorem
      requires: Phases 23, 24, 25
    -> Phase 27 "Predictions"
      provides: Landauer deficit, rho profile, exhaustion timescale
      requires: Phase 26

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
| ----------- | ------ | ------------ | ---------- |
| ENTR-01 (entropy increase) | Complete | Phase 23 | Monotonic increase under repeated SWAP |
| ENTR-02 (decrease conditions) | Complete | Phase 23 | 2-site oscillates; N-site monotonic |
| CALC-01 (2-qubit calculation) | Complete | Phase 23 | Depolarizing channel p = sin^2(Jt) |
| CHIR-01 (chirality-time) | Complete | Phase 24 | Gamma_* flips under T |
| CHIR-02 (three-consequence) | Complete | Phase 24 | u -> gauge + chirality + time |
| VALD-01 (Lawson-Michelsohn) | Complete | Phase 24 | Verified for Cl(d-1,1) |
| LAND-01 (Landauer bound) | Complete | Phase 25 | W >= kT I(B;M) |
| LAND-02 (quantitative bound) | Complete | Phase 25 | kT I(B;M) per cycle |
| LAND-03 (coherence loophole) | Complete | Phase 25 | Closed via 3 arguments |
| VALD-02 (Sagawa-Ueda) | Complete | Phase 25 | Consistent |
| VALD-03 (equilibrium rho=0) | Complete | Phase 25 | I=0 at equilibrium |
| GRAD-01 (entropy gradient) | Complete | Phase 26 | 3 independent routes |
| GRAD-02 (Gap C) | Partial | Phase 26 | Narrowed, not closed |
| CALC-02 (predictions) | Complete | Phase 27 | 94-order gap, rho profile |
