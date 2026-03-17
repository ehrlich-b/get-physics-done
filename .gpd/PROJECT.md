# Experiential Measure on Structure Space — Formalization

## What This Is

Rigorous formalization of the experiential measure framework on the structure space of self-modeling composite Markov processes. The project completes three formal gaps in the existing draft: assembling Theorem A (Boltzmann brain negligibility) from its constituent metastability lemmas, proving Lipschitz stability of the experiential density, and testing the Born-Fisher-Experiential conjecture on a toy qubit model. The subfield is mathematical physics / information-theoretic foundations, with the expected deliverables being proofs and a numerical falsification test.

## Core Research Question

Can the experiential measure framework on structure space be formalized with rigorous proofs — specifically, can Theorem A be assembled from its constituent lemmas, can rho's Lipschitz stability be proven, and does the Born-Fisher conjecture survive a qubit falsification test?

## Scoping Contract Summary

### Contract Coverage

- **Theorem A assembly (claim-theorem-a):** Self-contained proof composing BEGK, FW, DV, QSD lemmas with explicit error scaling
- **Lipschitz stability (claim-lipschitz):** Proven bound |rho(P) - rho(P')| <= L*||P-P'|| with L characterized
- **Born-Fisher test (claim-born-fisher):** Numerical verdict on whether I_vN(B;M) = S_vN(B)/2 for Born-rule distributions
- **False progress to reject:** Another proof sketch without assembled composition; more numerics without formal bounds

### User Guidance To Preserve

- **User-stated observables:** Complete logical chain from lemma statements to Theorem A; Lipschitz constant L as function of |Omega| and spectral gap; I_vN(B;M)/S_vN(B) ratio for Born-rule distributions
- **User-stated deliverables:** Theorem A proof (derivation), Lipschitz proof (derivation), qubit model code (Python)
- **Must-have references / prior outputs:** draft.md, composite_self_model.py, three_state_chain.py, quantum-extension/draft.md
- **Stop / rethink conditions:** If BEGK/DV/QSD error bounds don't compose (exponential suppression breaks); if qubit test fails (Born-Fisher conjecture falsified)

### Scope Boundaries

**In scope**

- Assemble Theorem A proof from BEGK, Freidlin-Wentzell, Donsker-Varadhan, and QSD lemmas with explicit error scaling
- Prove Lipschitz stability of rho(P) under kernel perturbations
- Compute I_vN(B;M) and S_vN(B) for toy qubit model to test Born-Fisher conjecture

**Out of scope**

- Countable state space generalization (Stage 1 of extension program)
- Full variational structure of mu_Q beyond qubit test
- Non-equilibrium extension via quasi-potentials
- Reference measure nu on structure space
- Eternal inflation regime (fixed epsilon, T -> infinity)

### Active Anchor Registry

- **ref-begk:** Bovier, Eckhoff, Gayrard, Klein — Metastability papers (2001-2004)
  - Why it matters: Exponential residence time bounds for Theorem A Lemma 2
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite

- **ref-fw:** Freidlin, Wentzell — Random Perturbations of Dynamical Systems (1984/2012)
  - Why it matters: Cycle hierarchy and communication heights for Theorem A Lemma 1
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite

- **ref-dv:** Donsker, Varadhan — Large deviations for Markov processes (1975-1983)
  - Why it matters: Concentration inequality for weighted empirical measure in Theorem A Lemma 6
  - Carry forward: planning, execution, verification
  - Required action: read, cite

- **ref-baez-dolan:** Baez, Dolan — From Finite Sets to Feynman Diagrams (2001)
  - Why it matters: Groupoid cardinality motivating 1/|Aut(x)| weighting
  - Carry forward: planning, writing
  - Required action: cite

- **ref-lmc:** Lopez-Ruiz, Mancini, Calbet — A statistical measure of complexity (1995)
  - Why it matters: rho belongs to LMC family — pedigree of I*(1-I/H) form
  - Carry forward: writing
  - Required action: cite

- **ref-gell-mann-lloyd:** Gell-Mann, Lloyd — Effective Complexity (1996/2003)
  - Why it matters: Broader family of measures peaking between order and randomness
  - Carry forward: writing
  - Required action: cite

### Carry-Forward Inputs

- ~/repos/blog/research/experiential-measure/draft.md (main framework draft)
- ~/repos/blog/research/experiential-measure/toy-model/composite_self_model.py (7 chains)
- ~/repos/blog/research/experiential-measure/toy-model/three_state_chain.py (FW verification)
- ~/repos/blog/research/quantum-extension/draft.md (quantum extension)

### Skeptical Review

- **Weakest anchor:** BEGK error bounds may not compose cleanly across all 7 lemmas — individual bounds are established but their product has not been verified to preserve the exponential form
- **Unvalidated assumptions:** Reversibility assumption in Theorem A (real observers are non-equilibrium); factorization condition exactness (real systems have approximate factorization)
- **Competing explanation:** Alternative density functions in the LMC family with same boundary conditions but different peak behavior could work equally well
- **Disconfirming observation:** BEGK/DV/QSD error bounds do not compose; Born-rule distributions do NOT satisfy I_vN(B;M) = S_vN(B)/2
- **False progress to reject:** Another proof sketch without assembled composition; more numerics confirming intuition without formal bounds

### Open Contract Questions

- ~~Exact form of L(|Omega|, spectral_gap) in Lipschitz bound~~ -- RESOLVED: L = (C_I + C_H)/gap(P)
- ~~Whether qubit model needs 2x2 or larger Hilbert space to be informative~~ -- RESOLVED: d=2 sufficient; d=3 spot checks confirm

## Research Questions

### Answered

- [x] Can the 7 lemmas in Theorem A's dependency graph be assembled into a self-contained proof with explicit error scaling? -- **YES.** Proof assembled with composite error rate gamma = min(alpha/2, Ds - alpha). Validated on three-state chain across 9 parameter combinations. -- v1.0
- [x] Is the experiential density rho Lipschitz continuous in the transition kernel, and what is the constant L? -- **YES.** L = (C_I + C_H)/gap(P), scaling as ln|Omega|/gap. Verified numerically: 3000 perturbations, zero violations. -- v1.0
- [x] Do Born-rule distributions satisfy I_vN(B;M) = S_vN(B)/2 in a toy qubit composite process? -- **NO. Conjecture FALSIFIED.** rho_Q <= 0 throughout all 1900+ Lindblad trajectories; mu_Q identically zero. Exchange Hamiltonian maintains I_vN >= S_B at all times. -- v1.0

### Active

(None -- all v1.0 questions answered)

### Out of Scope

- Countable/continuous state space generalization -- paper-length work, deferred
- Non-Markovian quantum channels -- could produce rho_Q > 0 regime, untested
- Non-equilibrium extension -- requires different mathematical framework
- Reference measure nu -- shared open problem with Mueller (2020)
- Amplitude damping channels -- may allow r < 1 transient, untested

## Research Context

### Physical System

Self-modeling composite Markov processes on finite product state spaces Omega = B x M, where B is the "body" subsystem and M is the "self-model" subsystem. The transition kernel satisfies a factorization condition ensuring the model updates by observing the body's state. The structure space S is the quotient of such processes by product-preserving isomorphisms.

### Theoretical Framework

Mathematical physics: stochastic processes, information theory, metastability theory. Key tools: continuous-time Markov chains, mutual information, Shannon/von Neumann entropy, Freidlin-Wentzell theory, BEGK metastability, Donsker-Varadhan large deviations, quasi-stationary distributions.

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
| --------- | ------ | ------ | ----- |
| State space size | \|Omega\| = \|B\| x \|M\| | Finite | Current toy model: 16 states (4x4) |
| Noise intensity | epsilon | epsilon -> 0 | Controls metastability; Theorem A is a low-noise result |
| Communication height (stable) | Delta_s | Delta_s > Delta_b | Depth of stable observer basin |
| Communication height (BB) | Delta_b | Delta_b < Delta_s | Depth of Boltzmann brain basin |
| Tracking accuracy | alpha | [0, 1] | Model-body correlation; rho peaks at alpha ~= 0.5 |
| Observation horizon | T | T_epsilon = exp((Delta_s - alpha_param)/epsilon) | Finite horizon, not T -> infinity |

### Known Results

- Toy model verification: rho = 0.347 for observer, 0.239 for BB+self-model, 0.000 for thermostat/crystal/BB — Ehrlich draft
- Parametric sweep: peak at alpha ~= 0.498, I*/H = 0.507 — Ehrlich draft
- Three-state chain: mu_BB/mu_stable matches analytical formula within 1% — Ehrlich draft
- BEGK residence times: exponential in communication height — Bovier et al. (2001-2004)
- QSD convergence: exponential in spectral gap — Champagnat, Villemonais

### What Is New

Assembling the known metastability tools into a complete proof for the specific observable (rho-weighted trajectory integral). Proving Lipschitz stability as a foundation for approximate factorization. First numerical test of the Born-Fisher-Experiential conjecture.

### Target Venue

To be determined — likely mathematical physics journal (Journal of Mathematical Physics, Communications in Mathematical Physics) or foundations of physics venue.

### Computational Environment

Local workstation. Python with numpy, scipy for qubit model. No HPC needed — all calculations are small-scale (finite state spaces, toy models).

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Information-theoretic: bits or nats for entropy/mutual information, seconds for time (bit-seconds or nat-seconds for trajectory functional mu). No natural units (hbar = c = 1) needed — this is not a QFT calculation.

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

## Key References

- Bovier, Eckhoff, Gayrard, Klein — Metastability papers (2001-2004) [BEGK]
- Freidlin, Wentzell — Random Perturbations of Dynamical Systems (1984/2012)
- Donsker, Varadhan — Large deviations for Markov processes (1975-1983)
- Baez, Dolan — From Finite Sets to Feynman Diagrams (2001)
- Lopez-Ruiz, Mancini, Calbet — A statistical measure of complexity (1995)
- Gell-Mann, Lloyd — Effective Complexity (1996/2003)
- Champagnat, Villemonais — QSD convergence results

## Constraints

- **Reversibility:** Theorem A proof assumes reversible Metropolis-type dynamics — non-equilibrium extension is out of scope
- **Finite state spaces:** All proofs for finite |Omega| only — countable extension deferred

## Key Decisions

| Decision | Rationale | Outcome |
| -------- | --------- | ------- |
| Clean composition over full explicit constants | User prefers self-contained proof with error scaling; constants in appendix | Good -- proof is self-contained |
| Qubit falsification over variational structure | Decisive test first; if it fails, variational work is moot | Good -- conjecture falsified, saved wasted effort |
| Lipschitz over countable extension | Needed for approximate factorization; countable extension is paper-length | Good -- Lipschitz bound proven with explicit constants |
| Deep-theory model profile | Heavy proof work benefits from tier-1 models | Good -- all proofs completed |
| 3 standalone papers over single monograph | Papers written independently for different audiences | Revisit -- peer review suggests Paper 2 may be better as section of Paper 1 |
| Honest framing over cosmological claims | Peer review flagged overclaiming; reframed titles and abstracts | Good -- papers now accurately scope their claims |

## Current State (v1.0 complete)

All three formal gaps in the experiential measure framework are closed:
1. **Theorem A** assembled from 7 metastability lemmas with explicit error composition
2. **Lipschitz stability** proven with L = (C_I + C_H)/gap(P), verified numerically
3. **Born-Fisher conjecture falsified** -- rho_Q <= 0 for all exchange-plus-dephasing Lindblad dynamics (proved analytically)

Three papers written, peer-reviewed (18-agent 6-pass panel), and revised. All math verified correct. Framing toned down per review: exponential suppression attributed to metastability (not rho specifically), literature gaps filled, self-citations corrected.

---

_Last updated: 2026-03-16 after v1.0 milestone_
