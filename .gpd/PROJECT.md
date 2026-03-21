# Experiential Measure on Structure Space

## What This Is

Deriving quantum mechanics from the algebraic structure of self-modeling composite processes. The v1.0 milestone formalized the experiential measure framework (Theorem A, Lipschitz stability, Born-Fisher falsification). The v2.0 milestone closes the last gap in the algebraic genericity chain: why should a self-modeling system's algebra carry a C*-involution? The route is through van de Wetering's sequential product axioms — if self-modeling "test-update-test" satisfies S1-S7, the involution is derived, not postulated. The subfield is mathematical physics / quantum foundations, with the expected deliverable being a paper (Paper 5) deriving QM from a single operational premise (L4: self-models test and update).

## Core Research Question

Does the sequential product structure of self-modeling systems satisfy van de Wetering's axioms S1-S7, thereby deriving quantum mechanics from a single operational premise?

## Current Milestone: v2.0 QM from Algebraic Genericity

**Goal:** Derive the C*-algebra involution from the sequential product structure of self-modeling systems, closing the last gap in the L4 → QM chain.

**Target results:**

- Proof or disproof that the self-modeling sequential product satisfies van de Wetering's S1-S7
- If S1-S7 hold: proof that B-M compositionality implies local tomography, completing the Jordan → C* promotion
- Paper 5 assembling the full chain (one premise) or conditional chain (L4 + C*)

## Scoping Contract Summary

### Contract Coverage

- **Sequential product axioms (claim-sp-axioms):** Formal verification of S1-S7 for the self-modeling construction, with S4 as the critical test
- **Local tomography (claim-local-tomo):** Proof or disproof that B-M independent accessibility implies local tomography
- **Paper assembly (claim-paper-5):** Complete chain paper (if Phases 1-2 succeed) or conditional chain paper (if either fails)
- **False progress to reject:** A sketch arguing S1-S7 "should hold" without formally checking each axiom against the construction; hand-waving about the effect algebra framing

### User Guidance To Preserve

- **User-stated observables:** Whether each of S1-S7 holds for the self-modeling sequential product; which effect algebra framing (effects on B vs B x M) is correct
- **User-stated deliverables:** Proof/disproof of S1-S7 (Phase 1), proof/disproof of local tomography (Phase 2), Paper 5 (Phase 3)
- **Must-have references / prior outputs:** van de Wetering (2018, arXiv:1803.11139), Gudder-Greechie (2002), v1.0 papers, blog repo drafts (experiential-measure/draft.md, quantum-extension/draft.md)
- **Stop / rethink conditions:** If the effect algebra framing is fundamentally incompatible with the self-modeling construction; if S4 fails AND the D'Ariano backup also fails

### Scope Boundaries

**In scope**

- Formalize the self-modeling sequential product on a finite-dimensional order unit space
- Verify axioms S1-S7, exploring both framings (effects on B, effects on B x M)
- If S1-S7 hold: prove local tomography from B-M compositionality
- Assemble Paper 5 (full chain or conditional)
- D'Ariano backup route (Phase 4, only if Phase 1 fails)

**Out of scope**

- Standard Model derivation (Level 4+)
- Self-modeling constants experiment (Level 6)
- Experiential measure extensions beyond v1.0
- Blog series (separate project)
- Countable/continuous state space generalization

### Active Anchor Registry

- **ref-vdw2018:** van de Wetering — Sequential product spaces are Jordan algebras (2018, arXiv:1803.11139)
  - Why it matters: Theorems 1 and 3 are the key results — S1-S7 → Jordan algebra, Jordan + local tomography → C*-algebra
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite

- **ref-gudder-greechie:** Gudder, Greechie — Sequential products on effect algebras (2002)
  - Why it matters: Original sequential product formalism; definitions and basic properties
  - Carry forward: planning, execution, writing
  - Required action: read, cite

- **ref-barnum2023:** Barnum, Ududec, van de Wetering — Composites and categories of Euclidean Jordan algebras (2023, arXiv:2306.00362)
  - Why it matters: Compositionality constraints on Jordan algebras; relevant to Phase 2 local tomography
  - Carry forward: planning, execution, writing
  - Required action: read, cite

- **ref-dariano2006:** D'Ariano — How to derive the Hilbert space formulation (2006, arXiv:quant-ph/0611094)
  - Why it matters: Backup route — Postulate 5 (symmetric faithful state) gives explicit involution construction
  - Carry forward: planning (Phase 4 only)
  - Required action: read if Phase 1 fails

- **ref-barandes:** Barandes — Stochastic-quantum bijection (2025)
  - Why it matters: Final step in chain — quantum indivisibility from unitary automorphisms
  - Carry forward: writing
  - Required action: cite

- **ref-motzkin-taussky:** Motzkin, Taussky — Pairs of matrices with property L (1955)
  - Why it matters: Generic non-commutativity of matrix algebras — NC step in the chain
  - Carry forward: writing
  - Required action: cite

### Carry-Forward Inputs

- ~/repos/blog/research/experiential-measure/draft.md (main framework draft)
- ~/repos/blog/research/quantum-extension/draft.md (quantum extension, algebraic genericity chain)
- ~/repos/blog/research/qm-genericity-review/ (adversarial review of the chain)
- v1.0 papers (Theorem A, Lipschitz, Born-Fisher falsification)

### Skeptical Review

- **Weakest anchor:** S4 (symmetry of orthogonality) for the self-modeling construction — no prior work verifies this specific axiom for this specific construction
- **Unvalidated assumptions:** That "test-update-test" maps cleanly onto van de Wetering's sequential product formalism; that the correct effect algebra is effects on B (vs B x M)
- **Competing explanation:** The involution might require an independent physical postulate (C*-axiom) rather than being derivable — many reconstruction programs assume it
- **Disconfirming observation:** S4 fails for the self-modeling sequential product; or the effect algebra framing is incompatible with the construction entirely
- **False progress to reject:** Arguing axioms hold "by physical intuition" without formal proofs; checking axioms for quantum sequential products (which trivially satisfy them) instead of the self-modeling construction

### Open Contract Questions

- Which effect algebra framing is correct (effects on B vs effects on B x M)?
- Whether S4 holds for the self-modeling sequential product
- Whether B-M independent accessibility is sufficient for local tomography

## Research Questions

### Answered

- [x] Can the 7 lemmas in Theorem A's dependency graph be assembled into a self-contained proof with explicit error scaling? -- **YES.** Proof assembled with composite error rate gamma = min(alpha/2, Ds - alpha). Validated on three-state chain across 9 parameter combinations. -- v1.0
- [x] Is the experiential density rho Lipschitz continuous in the transition kernel, and what is the constant L? -- **YES.** L = (C_I + C_H)/gap(P), scaling as ln|Omega|/gap. Verified numerically: 3000 perturbations, zero violations. -- v1.0
- [x] Do Born-rule distributions satisfy I_vN(B;M) = S_vN(B)/2 in a toy qubit composite process? -- **NO. Conjecture FALSIFIED.** rho_Q <= 0 throughout all 1900+ Lindblad trajectories; mu_Q identically zero. Exchange Hamiltonian maintains I_vN >= S_B at all times. -- v1.0

### Active

- [ ] Does the self-modeling sequential product satisfy van de Wetering's axioms S1-S7?
- [ ] Does S4 (symmetry of orthogonality) hold for the self-modeling construction?
- [ ] Does B-M compositionality (independent accessibility) imply local tomography?
- [ ] Which effect algebra framing is correct for the self-modeling sequential product?

### Out of Scope

- Countable/continuous state space generalization -- paper-length work, deferred
- Non-Markovian quantum channels -- could produce rho_Q > 0 regime, untested
- Non-equilibrium extension -- requires different mathematical framework
- Reference measure nu -- shared open problem with Mueller (2020)
- Standard Model derivation -- Level 4+, far beyond current scope
- Self-modeling constants experiment -- Level 6, requires experimental apparatus

## Research Context

### Physical System

Self-modeling composite processes with body B and model M. The sequential product structure arises from the operational cycle: test effect a on B, update M based on result, test effect b on B. The algebraic structure of this operation determines whether the system's observables form a C*-algebra (quantum) or something else.

### Theoretical Framework

Quantum foundations / algebraic quantum theory: effect algebras, sequential products, order unit spaces, Euclidean Jordan algebras, C*-algebras. Key tools: van de Wetering's sequential product characterization, Artin-Wedderburn structure theory, Skolem-Noether theorem, Gleason's theorem.

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
| --------- | ------ | ------ | ----- |
| Body dimension | dim(B) | Finite | Determines effect algebra structure |
| Model dimension | dim(M) | Finite | Must be sufficient to track B |
| Effect algebra | E(B) or E(B x M) | To be determined | Phase 1 resolves which framing |

### Known Results

- Algebraic genericity chain validated through 6 rounds of LLM research + 2 adversarial reviews -- Ehrlich blog repo
- Chain airtight from Step 3 onward (NC generic → matrix algebras → unitary → QM) -- Ehrlich blog repo
- Gap isolated to involution (*-operation) on the algebra -- Ehrlich blog repo
- v1.0 results: Theorem A, Lipschitz stability, Born-Fisher falsification -- this project
- van de Wetering (2018): S1-S7 → Jordan algebra; Jordan + local tomography → C*-algebra
- Gudder-Greechie (2002): sequential product formalism on effect algebras

### What Is New

Connecting self-modeling "test-update-test" to sequential product formalism to derive the C*-involution. No prior work has checked van de Wetering's axioms for this specific construction. If it works, QM follows from one premise (L4) instead of postulating the C*-algebra structure.

### Target Venue

Foundations of physics journal (Foundations of Physics, Physical Review A — Quantum Foundations, or New Journal of Physics).

### Computational Environment

Local workstation. Primarily proof work — no heavy computation needed. Python for any small verification calculations.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Dimensionless (algebraic/categorical work). No physical units needed for the sequential product verification.

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

## Key References

- van de Wetering (2018), arXiv:1803.11139 — Sequential product spaces are Jordan algebras
- Gudder, Greechie (2002) — Sequential products on effect algebras
- Barnum, Ududec, van de Wetering (2023), arXiv:2306.00362 — Composites of Euclidean Jordan algebras
- D'Ariano (2006), arXiv:quant-ph/0611094 — Hilbert space from operational axioms
- Barandes (2025) — Stochastic-quantum bijection
- Motzkin, Taussky (1955) — Generic non-commutativity
- Gleason (1957) — Born rule uniqueness

## Constraints

- **Finite dimensions:** All proofs for finite-dimensional systems only
- **Proof-driven:** No numerics-as-substitute for formal arguments (v1.0 lesson)

## Key Decisions

| Decision | Rationale | Outcome |
| -------- | --------- | ------- |
| Clean composition over full explicit constants | User prefers self-contained proof with error scaling; constants in appendix | Good -- proof is self-contained |
| Qubit falsification over variational structure | Decisive test first; if it fails, variational work is moot | Good -- conjecture falsified, saved wasted effort |
| Lipschitz over countable extension | Needed for approximate factorization; countable extension is paper-length | Good -- Lipschitz bound proven with explicit constants |
| Deep-theory model profile | Heavy proof work benefits from tier-1 models | Good -- all proofs completed |
| 3 standalone papers over single monograph | Papers written independently for different audiences | Revisit -- peer review suggests Paper 2 may be better as section of Paper 1 |
| Honest framing over cosmological claims | Peer review flagged overclaiming; reframed titles and abstracts | Good -- papers now accurately scope their claims |
| Sequential product route over direct involution construction | van de Wetering axioms give cleaner path; D'Ariano as backup | Pending |
| Explore both effect algebra framings | Correct framing is a Phase 1 result, not a premise | Pending |

## v1.0 Summary (complete)

All three formal gaps in the experiential measure framework are closed:
1. **Theorem A** assembled from 7 metastability lemmas with explicit error composition
2. **Lipschitz stability** proven with L = (C_I + C_H)/gap(P), verified numerically
3. **Born-Fisher conjecture falsified** -- rho_Q <= 0 for all exchange-plus-dephasing Lindblad dynamics (proved analytically)

Three papers written, peer-reviewed (18-agent 6-pass panel), and revised.

---

_Last updated: 2026-03-20 after v2.0 milestone initialization_
