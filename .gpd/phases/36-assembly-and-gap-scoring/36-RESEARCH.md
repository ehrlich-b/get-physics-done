# Phase 36: Assembly and Gap Scoring - Research

**Researched:** 2026-03-30
**Domain:** Emergent gravity / Entanglement thermodynamics / Derivation chain assembly
**Confidence:** MEDIUM

## Summary

Phase 36 is an assembly and assessment phase, not a new derivation phase. Its job is to (1) lay out the complete derivation chain from finite-dimensional observer to Einstein equations with every link explicit, and (2) score each of the four Paper 6 gaps individually using the results from Phases 32-35. The physics content is already established in prior phases; the challenge here is honest calibration and clear exposition.

The derivation chain has six links: (a) finite-dim observer (Paper 5) -> (b) SWAP lattice (Paper 6) -> (c) correlation structure and Fisher manifold (Phases 32-33) -> (d) emergent Lorentz invariance (Phase 34) -> (e) BW + equilibrium (Phase 35) -> (f) Jacobson 1995/2016 -> Einstein equations. Each link has been developed in prior phases. The assembly must make explicit what is proved, what is argued physically, and what is assumed at each step.

The gap scoring uses a four-level scale: CLOSED (rigorous proof), NARROWED (conditional on stated assumption), CONDITIONAL (physical argument, not rigorous), OPEN (not addressed). Based on prior phase results, the expected scores are: Gap A (continuum limit) -- NARROWED/CONDITIONAL (effective smoothness established for d >= 3, fails in 1D, log corrections in d=2); Gap B (conformal approximation) -- CONDITIONAL (Route A needs CFT, Route B via Lovelock circumvents it); Gap C (tensoriality) -- CONDITIONAL (assumed for Route B, derived for Route A in conformal regime); Gap D (MVEH) -- CONDITIONAL (structural identification via Connes-Rovelli + Van Raamsdonk, not a proof).

**Primary recommendation:** Organize the assembly document as a self-contained derivation chain with a "link status" table at the top, then each link in sequence with its assumptions and prior-phase citations, then individual gap scorecards. Do NOT re-derive anything; cite Phase 32-35 results by equation number. The critical task is honest framing: distinguish proved results (FISH-01/02, Hastings-Koma) from conditional results (CORR-03, sigma model Lorentz) from structural identifications (MVEH).

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| Paper 5 (ref-paper5) | Starting point | Finite-dimensional observer, C*-algebraic setting | Cite as chain origin | Link (a) in chain |
| Paper 6 (ref-paper6) | Gap definitions | Defines the four gaps to score; provides Links L1-L5 | Cite gap definitions; score against | Gap scorecards |
| Jacobson 1995 (gr-qc/9504004) | Framework | Original thermodynamic derivation: delta Q = T dS on local Rindler horizons | Cite for conceptual lineage | Discussion of Route A |
| Jacobson 2016 (arXiv:1505.04753) | Framework | Entanglement equilibrium argument: MVEH + first law + area law -> Einstein | Map J1-J3 inputs from Phase 35 | Link (f) in chain |
| Phase 32 FISH-01/02/03 | Prior results | Smoothness, positive-definiteness, distance non-recovery (1D) | Cite; FISH-03 failure feeds Gap A scoring | Links (c), Gap A |
| Phase 33 CORR-01/02/03 | Prior results | Correlation decay, sigma model, conditional Fisher smoothness for d>=2 | Cite; CORR-03 conditional status feeds Gap A | Links (c), Gap A |
| Phase 34 LRNZ-01/02 | Prior results | Emergent isotropy and Lorentz invariance | Cite | Link (d) |
| Phase 35 BWEQ-01/02 | Prior results | BW axioms, lattice-BW form, KMS, Unruh temperature, J1-J3 packaged | Cite J1-J3 directly | Link (e), Link (f) |
| Lovelock 1971/1972 | Theorem | Uniqueness of Einstein tensor from symmetric 2-tensor with <=2 derivatives | Cite for Route B | Gap C scoring |
| Casini-Huerta-Myers 2011 (arXiv:1102.0440) | Standard result | CHM conformal modular Hamiltonian | Cite for Route A | Gap B scoring |
| Sorce 2024 | Caveat | Geometric modular flow requires conformal symmetry | Cite for MVEH/Gap B assessment | Gap D scoring |

**Missing or weak anchors:** No rigorous proof that the NL sigma model describes the continuum limit of the SWAP lattice in d >= 2 (only physical universality argument). No rigorous Neel order proof for S=1/2 d=2 (QMC evidence only, not Dyson-Lieb-Simon which needs S >= 1). These affect Gap A scoring.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Units | Natural (hbar=1, k_B=1, a=1) | SI | Project convention |
| Metric signature | (-,+,...,+) Lorentzian for emergent spacetime; (+,...,+) Riemannian for Fisher | (+,-,-,-) | Phases 34-35; Jacobson 2016 uses (-,+,+,+) |
| Modular Hamiltonian | K_A = -ln(rho_A), rho_A = e^{-K_A}/Z | With additive constant | Paper 6, Phase 35 |
| KMS temperature | beta = 2pi for Rindler wedge | | BW theorem |
| Unruh temperature | T_U = a/(2pi) | | Phase 35 Eq. (35.3) |
| Fisher metric | SLD, g_F = 4 g_Bures | | Phases 32-33 |
| Coupling | J > 0 antiferromagnetic | | Paper 6 |
| Emergent speed of light | c = c_s (spin-wave velocity, NOT v_LR) | c = v_LR | Phase 34 |

**CRITICAL: The emergent metric uses c_s, not v_LR. The convention_lock lists Riemannian Fisher metric for metric_signature, which is the spatial part. The full spacetime metric ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j uses Lorentzian signature (-,+,...,+) as established in Phase 34.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| G_ab + Lambda g_ab = 8pi G_N T_ab | Einstein field equation | Jacobson 2016, Eq. (eq:einstein) in Paper 6 | Target: the end of the chain |
| delta S = delta S_UV + delta S_mat = 0 | Entanglement equilibrium | Jacobson 2016 (MVEH) | Link (f): the equilibrium condition |
| delta S_UV = eta delta A | Area-entropy proportionality | Links L1-L5 of Paper 6 | Feeds delta A from Raychaudhuri |
| delta S_mat = delta <K_B> | Entanglement first law | Exact identity | Connects entropy to modular Hamiltonian |
| K_A = 2pi K_boost | BW theorem | Phase 35, Eq. (35.0a) | J1 input to Jacobson |
| theta = sigma = 0 at bifurcation | Local equilibrium | Phase 35, Eqs. (35.19, 35.21) | J2 input to Jacobson |
| T_U = a/(2pi) | Unruh temperature | Phase 35, Eq. (35.3) | J3 input to Jacobson |
| ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j | Emergent Lorentzian metric | Phase 34, Eq. (34.9) | Input: spacetime where Jacobson lives |
| g_F(x) = O(m_s^2) > 0 for d >= 2 | Fisher metric in Neel phase | Phase 33, Eq. (33.19) | Link (c): spatial geometry exists |
| G_N = 1/(4 eta) | Newton's constant from entropy density | Paper 6, Eq. (eq:newton) | Parameter identification |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Derivation chain assembly | Organizes logical dependencies between results | Entire phase | This is the primary technique |
| Gap scoring rubric | Classifies each gap as CLOSED/NARROWED/CONDITIONAL/OPEN | ASBL-02 | Paper 6 Sec. discussion |
| Assumption tracking | Lists every assumption at each chain link, classifies rigor level | All links | Standard logical analysis |
| Raychaudhuri equation (linearized) | Computes delta A from curvature perturbation | Link (f), Route A | Wald 1984, Jacobson 2016 |
| Lovelock uniqueness theorem | Constrains geometric equation to Einstein | Link (f), Route B | Lovelock 1971/1972 |

### Approximation Schemes

Phase 36 does not introduce new approximations. It catalogues the approximations already made in Phases 32-35 and assesses their cumulative impact:

| Approximation | Where Introduced | Small Parameter | Status |
| --- | --- | --- | --- |
| Hastings-Koma exponential clustering | Phase 32 | Requires gap gamma > 0 | Rigorous for gapped; FAILS for gapless Neel phase |
| NL sigma model for d >= 2 Heisenberg | Phase 33 | a/xi << 1 | Physical argument (MEDIUM confidence) |
| Sublattice alternation mechanism | Phase 33 | Requires Neel LRO m_s > 0 | Conditional on H1-H4 |
| Lattice anisotropy -> emergent isotropy | Phase 34 | a/L << 1, RG irrelevant (rho ~ 2) | Physical argument with numerical support |
| Wick rotation justified by DLS reflection positivity | Phase 34 | Exact for bipartite lattice | Rigorous for Euclidean theory; extension to Lorentzian is physical |
| Lattice-BW entanglement Hamiltonian | Phase 35 | a/L << 1, Lorentz-invariant low-energy theory | Numerical (SRF = 0.9993) not rigorous |
| CHM conformal modular Hamiltonian | Paper 6 Route A | (m ell)^{2 Delta} corrections | Exact only for CFT; problematic in d >= 2 |
| Tensoriality assumption | Paper 6 Route B | Second-derivative truncation | Assumed, physically motivated |
| Wilsonian continuum limit | Paper 6 | a/L << 1, universality | Physical argument; NOT proved for SWAP lattice |

## Standard Approaches

### Approach 1: Sequential Link Assembly with Status Tracking (RECOMMENDED)

**What:** Assemble the derivation chain as a sequence of numbered links, each with: (i) statement of what the link establishes, (ii) assumptions/inputs, (iii) prior phase citation, (iv) rigor level (theorem/conditional/physical argument/assumed).

**Why standard:** This is how mathematical physics derivation chains are presented -- e.g., Jacobson 1995 himself traces the chain from Clausius relation through Raychaudhuri to Einstein. The Faulkner-Lewkowycz-Maldacena chain (arXiv:1307.2892) similarly presents link-by-link with explicit assumptions.

**Track record:** All successful derivations of Einstein from entanglement (Jacobson 1995, Jacobson 2016, Lashkari-McDermott-Van Raamsdonk 2014, Cao-Carroll-Michalakis 2017) present in this format.

**Key steps:**

1. Write the link status summary table (6 links, each with status RIGOROUS/CONDITIONAL/PHYSICAL ARGUMENT/ASSUMED)
2. For each link (a)-(f), write a self-contained section: what it establishes, what it assumes, what prior phase proves it, what its rigor level is
3. Map the three Jacobson inputs J1-J3 to their sources in Phase 35
4. State the Einstein equation derivation (both Route A and Route B) with explicit conditions
5. Write individual gap scorecards with justification from specific phase results
6. Write the "honest assessment" section: what the chain actually establishes vs what it claims

**Known difficulties at each step:**

- Step 1: The hardest part is not papering over failed results (FISH-03 in 1D) while still making a positive case for d >= 3
- Step 5: The gap scores must be justified by SPECIFIC results, not hand-waving. Each score needs a theorem/equation citation.
- Step 6: Risk of overclaiming (P7 from PITFALLS) or underclaiming (failing to credit genuine progress)

### Anti-Patterns to Avoid

- **Lumping all gaps together (P7):** Each gap has a different status. Gap A is the hardest, Gap D is a philosophical reframing. Scoring them uniformly is dishonest.
- **Claiming CLOSED when result is CONDITIONAL:** If a result depends on H1-H4 (like CORR-03), the gap is NARROWED or CONDITIONAL, not CLOSED. The conditions must be stated.
- **Re-deriving Phase 32-35 results:** Assembly means CITING, not re-deriving. Every equation should reference a prior derivation file by equation number.
- **Claiming constructive continuum limit:** Paper 6 explicitly states that the continuum limit is the principal open problem. Phase 36 must not claim it is solved. The result is "effective smoothness" for finite systems, not a constructive continuum limit.
- **Ignoring the 1D FISH-03 failure:** The distance recovery failure in 1D is a genuine negative result. It must appear in the chain with an honest assessment of what it means.
- **Confusing v_LR with c:** The emergent speed of light is c_s (Phase 34), not v_LR. Using v_LR would be wrong and the chain must be explicit about this.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form or Status | Source | How to Use |
| --- | --- | --- | --- |
| FISH-01: Fisher smoothness at finite N | rho_Lambda(x) smooth, derivatives bounded by exp(-R(x)/xi) | Phase 32, derivations/32-fisher-geometry-theorems.md | Cite in Link (c) |
| FISH-02: Fisher positive-definiteness | g(x) > 0 at interior points with full-rank rho | Phase 32, derivations/32-fisher-geometry-theorems.md | Cite in Link (c) |
| FISH-03: Distance non-recovery in 1D | d_Fisher/d_lattice -> 0 as N -> infinity; g_bulk ~ N^{-2.75} | Phase 32, derivations/32-fisher-geometry-theorems.md | Cite as negative result; drives Gap A scoring |
| CORR-01: Two-tier correlation decay | Gapped: exponential; Neel: algebraic LRO | Phase 33 Plan 01 | Cite in Link (c) |
| CORR-02: O(3) NL sigma model | c_s = 1.659 Ja, matches QMC to 0.3% | Phase 33 Plan 01 | Cite in Link (c)/(d) |
| CORR-03: Conditional Fisher smoothness for Neel phase | g_F = O(m_s^2) > 0 for d >= 2, conditional on H1-H4 | Phase 33 Plan 03, derivations/33-fisher-smoothness-algebraic-decay.md | Key for Gap A; cite rigor level explicitly |
| LRNZ-01: Emergent isotropy | Anisotropy O(a^2/L^2), RG irrelevant with rho ~ 2 | Phase 34 Plan 01 | Cite in Link (d) |
| LRNZ-02: Lorentz from sigma model | O(d+1) symmetric action + DLS reflection positivity + Wick rotation | Phase 34 Plan 01 | Cite in Link (d) |
| Velocity hierarchy | v_LR/c_s = 7.63, c_eff = c_s by four arguments | Phase 34 Plan 02 | Cite in Link (d) |
| Emergent metric assembly | ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j | Phase 34 Plan 02 | Cite in Link (d)/(e) |
| BWEQ-01: BW prerequisites | W1-W4 satisfied, W5 conditional, W6 open | Phase 35 Plan 01 | Cite in Link (e) |
| BWEQ-01: Lattice-BW form | H_ent = (2pi/c_s) sum x_perp h_x, SRF = 0.9993 | Phase 35 Plan 01 | Cite in Link (e) |
| BWEQ-02: KMS and Unruh | T_U = a/(2pi), theta = sigma = 0 at bifurcation | Phase 35 Plan 02 | Cite in Link (e); feeds J1-J3 |
| J1-J3 Jacobson inputs | J1: K_A = 2pi K_boost; J2: theta=sigma=0; J3: T_U = a/(2pi) | Phase 35 Plan 02 | Direct inputs to Link (f) |
| Einstein equation (Route A) | G_ab + Lambda g_ab = 8pi G_N T_ab | Paper 6 Sec. V | Target equation |
| Einstein equation (Route B) | Same, from Lovelock uniqueness | Paper 6 Sec. V | Alternative route |
| Raychaudhuri (linearized) | delta A = -(Omega_{d-1} ell^{d+1})/(2d) [(d+1) R_ab n^a n^b + R] | Paper 6 Eq. (delta-area) | Cite; do not re-derive |
| CHM modular Hamiltonian | K_B = 2pi integral_B (ell^2 - |x|^2)/(2 ell) T_00 | Casini-Huerta-Myers 2011 | Cite for Route A |
| Lovelock theorem | Unique divergence-free symmetric 2-tensor from metric + <=2 derivatives = G_ab + Lambda g_ab | Lovelock 1971/1972 | Cite for Route B |

**Key insight:** Every result above is already derived and documented in derivation files. Phase 36 assembles and cites them. The only new content is the gap scoring judgments and the overall chain narrative.

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Thermodynamics of Spacetime | Jacobson | 1995 | Original derivation: delta Q = T dS on local Rindler horizons -> Einstein | Conceptual lineage; the 1995 approach uses Clausius, the 2016 approach uses MVEH |
| Entanglement Equilibrium | Jacobson | 2016 | Direct framework: MVEH + first law + area law -> Einstein | Precise inputs J1-J3; the entanglement equilibrium condition |
| Comments on Jacobson's argument | Speranza | 2016 | Conformal modular Hamiltonian corrections for non-conformal fields | Quantifies Gap B: corrections O((m ell)^{2 Delta}) |
| Geometric modular flows | Sorce | 2024 | Conformal symmetry required for geometric modular flow | Constrains MVEH interpretation; Sorce caveat |
| Space from Hilbert Space | Cao-Carroll-Michalakis | 2017 | Alternative approach: assumes factored Hilbert space, derives spatial constraint | Comparison point for the chain |
| Entanglement first law -> linearized Einstein | Lashkari-McDermott-Van Raamsdonk | 2014 | Linearized Einstein from holographic entanglement first law | Comparison: requires AdS/CFT, gives linearized only |
| Lattice BW | Giudici et al. | 2018 | Numerical evidence for lattice-BW when low-energy theory is Lorentz-invariant | Supports Link (e) |
| Area-law reviews | Eisert-Cramer-Plenio 2010 | 2010 | Comprehensive review of area-law entanglement entropy | Background for Gap A |

## Computational Tools

### Core Tools

Phase 36 is primarily a writing/assembly phase. No new computations are required.

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| Existing derivation files (derivations/*.md) | N/A | Source material to cite | Contains all Phase 32-35 results |
| Phase SUMMARY.md files | N/A | Quick reference for prior phase outcomes | Contain contract results and equation lists |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| LaTeX (if writing for paper) | Typeset the chain document | If assembly feeds directly into paper draft |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| No new computation needed | 0 | N/A | N/A |
| Chain document writing | ~2-4 hours | Logical organization | Follow the 6-link structure |
| Gap scoring | ~1-2 hours | Honest calibration | Use the 4-level rubric strictly |

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Convention consistency | All links use same metric, units, speed | Compare convention declarations across Phase 32-35 SUMMARY files | All natural units, SLD Fisher, J>0 AFM |
| Logical dependency order | No link uses a result before it's established | Trace dependency graph: (a) -> (b) -> (c) -> (d) -> (e) -> (f) | Linear chain, no circular dependencies |
| BW comes after Lorentz | No circularity (Pitfall P4) | Verify Phase 34 (Lorentz) precedes Phase 35 (BW) in both phases and chain | Phases ordered 34 < 35 |
| Jacobson inputs complete | J1-J3 all present with citations | Check Phase 35 Plan 02 SUMMARY | J1: Eq. 35.0a; J2: Eqs. 35.19, 35.21; J3: Eq. 35.3 |
| Gap A scoring matches FISH-03 | Continuum limit gap scored consistently with 1D failure and d>=2 conditional | Compare score with FISH-03 status (failed) and CORR-03 status (conditional) | Gap A should be NARROWED or CONDITIONAL, not CLOSED |
| Gap B scoring distinguishes routes | Route A needs conformal, Route B doesn't | Verify Route A gets lower score on Gap B than Route B | Gap B: CONDITIONAL for Route A, N/A for Route B |
| Fisher metric is spatial only | No claim that Fisher gives Lorentzian metric (Pitfall P1) | Grep chain document for "Fisher" + "Lorentzian" or "spacetime metric" | Fisher always qualified as "spatial" |
| Speed of light = c_s, not v_LR | Chain uses c_s not v_LR for emergent c | Check Phase 34 citation | c_s = 1.659 Ja, not v_LR = 12.66 J |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| d = 1 conformal limit | SU(2) Heisenberg chain | WZW CFT with c=1; Route A exact; Gap B vanishes | Paper 6; Phase 33 |
| d >= 3 Neel-ordered | Heisenberg AFM, bipartite lattice | Neel order rigorous (DLS 1978 for S >= 1); Goldstone integral convergent | Phase 33 CORR-03 |
| d = 2 marginal case | S = 1/2 isotropic Heisenberg | Neel order from QMC (not rigorous theorem); log(L) Goldstone correction | Phase 33 CORR-03 |
| Gapped systems (AKLT, easy-axis) | gamma > 0 | Hastings-Koma exponential clustering; FISH-01 smoothness | Phase 32 |
| G_ab = 0 in d=1 | 1+1 spacetime | Einstein tensor vanishes identically; only cosmological equation | Paper 6; Jacobson 2016 |

### Red Flags During Assembly

- If any link claims a result at higher rigor than the source phase established -- recheck
- If Gap A is scored CLOSED without addressing FISH-03 failure in 1D -- wrong
- If MVEH is claimed as "derived" rather than "structurally identified" -- overclaim
- If the chain claims to hold "for all dimensions" without distinguishing d=1, d=2, d>=3 -- oversimplification
- If Route B's tensoriality assumption is not listed as an assumption -- missing input

## Common Pitfalls

### Pitfall 1: Overclaiming Gap Closure (P7 from PITFALLS.md)

**What goes wrong:** Scoring all four gaps as CLOSED or lumping them together as "addressed" when the evidence is heterogeneous.
**Why it happens:** Assembly phases tend toward optimism -- the goal is to show the chain works, which biases toward favorable scoring.
**How to avoid:** Use the 4-level rubric strictly. Each gap gets its own scorecard with specific equation citations. If a result is conditional on H1-H4, the gap score is NARROWED or CONDITIONAL, not CLOSED.
**Warning signs:** All four gaps getting the same score; no gap scored worse than NARROWED.
**Recovery:** Revisit each gap independently with fresh eyes. Ask: "If a skeptical referee read this, would they agree with the score?"

### Pitfall 2: Observer-Cutoff Overclaim (P6 from PITFALLS.md)

**What goes wrong:** Claiming that the finite-dimensional observer provides a constructive continuum limit, when the result is effective smoothness at finite N.
**Why it happens:** The v9.0 milestone is about closing Paper 6 gaps, which creates pressure to claim the continuum limit gap is closed.
**How to avoid:** Distinguish "effective smoothness" (Fisher metric smooth at finite N, Phases 32-33) from "constructive continuum limit" (rigorous N -> infinity limit with controlled error, which is NOT established). State this distinction explicitly in the chain document.
**Warning signs:** The words "continuum limit" without qualification; claiming Fisher geometry "converges" to smooth manifold without the FISH-03 caveat.
**Recovery:** Replace "continuum limit" with "effective smoothness at finite N" wherever the latter is what was actually proved.

### Pitfall 3: Dimension-Dependent Results Presented as Universal

**What goes wrong:** Stating results without specifying which dimensions they hold for.
**Why it happens:** The derivation chain has genuinely different status in d=1, d=2, and d>=3. Collapsing these into a single statement loses critical information.
**How to avoid:** Every chain link and every gap score must specify which dimensions it applies to. Use a dimension comparison table.
**Warning signs:** Sentences like "the Fisher metric is smooth" without specifying d=1 (fails) vs d>=2 (conditional) vs gapped (rigorous).
**Recovery:** Add a dimension column to every assessment table.

### Pitfall 4: Confusing Jacobson 1995 with Jacobson 2016

**What goes wrong:** Mixing the 1995 thermodynamic argument (delta Q = T dS on local Rindler horizons, using Clausius relation and Raychaudhuri) with the 2016 entanglement equilibrium argument (MVEH + first law + area law, using causal diamond setup).
**Why it happens:** Both derive Einstein's equation from thermodynamic/entropic arguments. The 2016 paper refines and extends the 1995 approach.
**How to avoid:** Paper 6 follows Jacobson 2016 (entanglement equilibrium), not Jacobson 1995 (thermodynamic equation of state). The chain should use the 2016 framework with the 1995 paper cited for conceptual lineage only.
**Warning signs:** References to "Clausius relation" or "delta Q = T dS" in the chain when the actual argument uses "delta S = 0" (entanglement equilibrium).
**Recovery:** Rewrite any 1995-framework language in terms of the 2016 framework.

## Level of Rigor

**Required for this phase:** Honest assessment / logical analysis (NOT formal proof or numerical evidence)

**Justification:** Phase 36 is an assembly and scoring phase. The rigor requirement is on the ASSESSMENT, not on new derivations. The assessment must be honest about what each phase proved vs argued vs assumed. The scoring must be consistent with the evidence.

**What this means concretely:**

- Every claim in the chain document must cite a specific prior derivation with equation number
- Every gap score must be justified by specific phase results, not hand-waving
- The rigor level of each chain link must be stated using the taxonomy: theorem (formal proof), conditional theorem (proof under stated assumptions), physical argument (dimensionally correct, symmetry-consistent, but not proved), assumed (taken as input without justification)
- The chain document must be readable by someone familiar with Papers 5-6 without re-deriving anything

## Jacobson's Entanglement Equilibrium: Precise Input Mapping

This section maps what Jacobson 2016 needs to what Phase 35 provides.

### Jacobson 2016 Inputs

Jacobson's entanglement equilibrium argument requires:

1. **Entropy decomposition:** S = S_UV + S_mat, with S_UV = eta * A (area-proportional UV term)
2. **MVEH:** Vacuum maximizes S at fixed <T_ab> -> delta S = 0 for first-order perturbations
3. **Geometric variation:** delta A from Raychaudhuri equation for null generators of causal diamond; requires theta = sigma = 0 at bifurcation surface (local equilibrium)
4. **Matter variation:** delta S_mat = delta <K_B> from entanglement first law; for conformal fields, K_B is the CHM modular Hamiltonian
5. **Emergent geometry:** A smooth Lorentzian manifold (M, g_ab) with Riemann normal coordinates at each point, small geodesic ball B, and causal diamond D(B)

### What the Chain Provides

| Jacobson Input | Chain Provides | Source | Status |
| --- | --- | --- | --- |
| S_UV = eta * A (area law) | Area-law entanglement from SWAP lattice (Links L1-L5) | Paper 6 Sec. arealaw | CONDITIONAL (proved for gapped; physical argument for Neel) |
| MVEH | Structural identification via Connes-Rovelli + Van Raamsdonk | Paper 6 Sec. equilibrium | CONDITIONAL (structural identification, not proof) |
| theta = sigma = 0 | Derived from Killing symmetry of boost vector | Phase 35, Eqs. (35.19, 35.21) | RIGOROUS (standard GR once boost is identified) |
| K_B = CHM form (Route A) | Applies only in conformal regime (d=1 WZW) | Paper 6 Sec. conformal-approx; CHM 2011 | RIGOROUS for d=1; FAILS for d>=2 Neel |
| K_A = 2pi K_boost | BW theorem applied to effective Lorentz-invariant theory | Phase 35, Eq. (35.0a) | CONDITIONAL (lattice-BW numerical, not theorem) |
| T_U = a/(2pi) | Derived from KMS + proper time conversion | Phase 35, Eq. (35.3) | RIGOROUS (once BW is accepted) |
| Smooth Lorentzian manifold | Fisher spatial metric + sigma model temporal + Wick rotation | Phases 32-34 | CONDITIONAL (effective smoothness, not constructive limit) |
| Raychaudhuri delta A | Standard GR calculation on emergent metric | Paper 6, Eq. (delta-area) | RIGOROUS (once smooth manifold is accepted) |

### Beyond J1-J3: Additional Jacobson Requirements

Phase 35 packaged J1-J3 for Phase 36. But Jacobson's full argument also needs:

- **J4: Smooth manifold (M, g_ab):** This comes from the Fisher manifold construction (Phases 32-33) + Lorentz assembly (Phase 34). It is the continuum limit assumption -- Gap A.
- **J5: Area-entropy proportionality S_UV = eta A:** This is Links L1-L5 of Paper 6. The area law for the SWAP lattice ground state.
- **J6: Small-ball limit validity:** The causal diamond must be much larger than the lattice spacing (a << ell) and much smaller than the curvature radius (ell << L_curv). This is the Wilsonian regime assumption.
- **J7: Entanglement first law delta S_mat = delta <K_B>:** An exact identity (does not require additional assumptions).
- **J8: Tensoriality (Route B only):** The entanglement-geometry equation is a symmetric 2-tensor with at most 2 derivatives. This is Gap C.

## The Four Paper 6 Gaps: Detailed Analysis

### Gap A: Continuum Limit (Principal Open Problem)

**Paper 6 definition:** "The Wilsonian argument that the lattice produces a smooth Riemannian manifold (M, g_ab) at long wavelengths is the principal open problem." (Paper 6, Sec. gaps)

**What Phases 32-35 established:**
- FISH-01/02: Fisher metric smooth and positive-definite at FINITE N (Phase 32) [RIGOROUS]
- FISH-03: Distance recovery FAILS in 1D (g_bulk ~ N^{-2.75}) [RIGOROUS NEGATIVE RESULT]
- CORR-03: For d >= 2 with Neel order, g_F = O(m_s^2) > 0 [CONDITIONAL on H1-H4]
- For d >= 3: Goldstone integral convergent, Neel order rigorously proved for S >= 1 [RIGOROUS for S >= 1; QMC for S = 1/2]
- For d = 2: Log(L) Goldstone correction, Neel order not rigorously proved for S = 1/2 [MEDIUM confidence]
- Effective smoothness at finite N, NOT constructive continuum limit as N -> infinity

**What is still missing:**
- Rigorous N -> infinity limit of Fisher geometry for d >= 2
- Rigorous Neel order for S = 1/2 d = 2 (only QMC evidence)
- Proof that sigma model is the correct continuum description of the SWAP lattice (universality argument is physical, not proved)

**Expected score:** NARROWED for d >= 3 (conditional on sigma model description holding, but strong physical evidence and some rigorous ingredients). CONDITIONAL for d = 2 (additional log corrections, Neel order not rigorously proved for S = 1/2). OPEN for d = 1 (FISH-03 shows distance recovery fails).

### Gap B: Conformal Approximation (Route A Only)

**Paper 6 definition:** "The CHM conformal modular Hamiltonian is exact only for CFTs in causal diamonds. For non-conformal fields, corrections of O((m ell)^{2 Delta}) appear." (Paper 6, Sec. gaps)

**What Phases 32-35 established:**
- Phase 33: In d = 1, SU(2)_1 WZW CFT -> conformal approximation exact. Gap B vanishes.
- Phase 33: In d >= 2, Neel order -> NL sigma model, NOT CFT. Conformal approximation problematic.
- Phase 34: Emergent Lorentz invariance established, but NOT conformal invariance in d >= 2.
- Paper 6 Route B (Lovelock) circumvents Gap B entirely -- does not need conformal K_B.

**What is still missing:**
- For Route A in d >= 2: quantification of conformal corrections for the NL sigma model
- Whether the "conformal window" a << ell << 1/m exists for the Heisenberg AFM (the mass scale m is set by Neel gap / spin-wave gap)

**Expected score:** CLOSED for d = 1 Route A (exact CFT). OPEN for d >= 2 Route A (no conformal symmetry). N/A for Route B (bypassed by Lovelock). Overall: CONDITIONAL (Route A works in d = 1, Route B circumvents in d >= 2, but Route B introduces its own assumption -- Gap C).

### Gap C: Tensoriality (Route B Only)

**Paper 6 definition:** "The Lovelock route assumes that the entanglement-geometry equation is a symmetric 2-tensor equation with at most second derivatives." (Paper 6, Sec. gaps)

**What Phases 32-35 established:**
- Phase 34: Emergent metric ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j is a symmetric 2-tensor
- Phase 34: The metric is assembled from two independent sources (Fisher spatial, sigma model temporal)
- Paper 6 argues: symmetry from metric, second-derivative restriction from first-order entanglement first law

**What is still missing:**
- Proof that the entanglement-geometry relation does not contain higher-derivative or non-local terms
- Proof that the entanglement first law (first-order perturbation) restricts the geometric equation to second-order derivatives

**Expected score:** CONDITIONAL (physically motivated assumption, not proved). The argument from Paper 6 is: entanglement first law is first-order -> couples to modular Hamiltonian (local at leading order in derivative expansion) -> geometric equation has at most 2 derivatives. This is a physical argument.

### Gap D: MVEH (Maximum Vacuum Entanglement Hypothesis)

**Paper 6 definition:** "MVEH is not listed as a gap; it is reframed as a structural identification via the Connes-Rovelli thermal time hypothesis." (Paper 6, Sec. gaps note)

**What Phases 32-35 established:**
- Phase 35: Modular flow identified with Lorentz boost (BW theorem)
- Phase 35: KMS property at beta = 2pi (thermal equilibrium)
- Paper 6: MVEH reframed as structural identification: in pre-geometric framework, the vacuum IS the geometry-defining state (Connes-Rovelli + Van Raamsdonk argument)
- Numerical evidence from Paper 6: all Hamiltonian perturbations decrease S(A)
- Sorce caveat: geometric modular flow requires conformal symmetry (satisfied in d = 1, problematic in d >= 2)

**What is still missing:**
- Proof of existence and uniqueness of geometry-defining state
- Proof that Van Raamsdonk's argument (less entanglement -> less connected geometry) applies to the SWAP lattice
- Resolution of Sorce caveat for d >= 2 (where theory is not conformal)

**Expected score:** CONDITIONAL (structural identification accepted; not a mathematical proof; Sorce caveat addressed only in d = 1). The honest framing: MVEH is the only available vacuum selection criterion in a pre-geometric framework, and the argument for it is physically compelling but not proved.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Jacobson 1995 (delta Q = T dS) | Jacobson 2016 (entanglement equilibrium) | 2016 | More precise: uses MVEH instead of Clausius, works for all causal diamonds not just Rindler |
| Einstein from holography (AdS/CFT assumed) | Einstein from entanglement (no holography needed) | 2016+ | Paper 6 chain does not assume AdS/CFT |
| Continuum limit as assumption | Continuum limit as derivation target | v9.0 milestone | Paper 6 Phases 32-35 attempt to derive it from finite lattice |

**Superseded approaches to avoid:**

- Jacobson 1995 Clausius approach: Replaced by Jacobson 2016 entanglement equilibrium for this context. The 1995 approach uses heat flux delta Q, while 2016 uses entropy variation delta S. Both derive Einstein, but 2016 is cleaner for the entanglement setting.
- Assuming AdS/CFT for Einstein derivation: Lashkari-McDermott-Van Raamsdonk (2014) and Faulkner-Lewkowycz-Maldacena (2014) assume holography. Paper 6 does not.

## Open Questions

1. **Does the full chain hold in d = 2 with the log(L) Goldstone correction?**
   - What we know: CORR-03 says d >= 3 is clean, d = 2 has marginal log correction
   - What's unclear: Whether the log correction invalidates the chain or is absorbed by normalization
   - Impact on this phase: Affects Gap A scoring for d = 2
   - Recommendation: Score d = 2 as CONDITIONAL (one step below d >= 3's NARROWED)

2. **Does Route A or Route B (or both) apply in d >= 2?**
   - What we know: Route A fails without conformal symmetry; Route B needs tensoriality
   - What's unclear: Whether the combined evidence from both routes is stronger than either alone
   - Impact on this phase: Affects overall chain assessment
   - Recommendation: Present both routes with their respective assumptions; note complementarity as Paper 6 does

3. **What is the precise relationship between "effective smoothness at finite N" and "continuum limit"?**
   - What we know: Fisher metric is smooth at finite N (FISH-01/02). But FISH-03 fails in 1D.
   - What's unclear: Whether CORR-03 conditional smoothness for d >= 2 constitutes an effective continuum limit
   - Impact on this phase: Core issue for Gap A scoring
   - Recommendation: Frame as "effective smoothness" not "continuum limit" to avoid overclaim

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Chain assembly shows logical gap | Missing link between phases | Identify which phase needs extension; return to planning | Medium -- requires new phase work |
| Gap A scored OPEN even for d >= 3 | CORR-03 conditions turn out to be wrong | Restrict chain to gapped systems only | Low -- still proves chain for a subclass |
| Route A and Route B both fail | Conformal + tensoriality both problematic in d >= 2 | Frame chain as "programme" with specific remaining targets | Low -- honest framing, not technical failure |
| Gap scoring reveals chain is weaker than expected | Honest assessment shows too many CONDITIONAL links | Document as research programme with clear next steps | Low -- the value is in honest assessment |

**Decision criteria:** The primary approach (assembling the full chain and scoring honestly) cannot truly "fail" -- the assembly is an organizational task, and the scoring is a judgment call backed by evidence. The only failure mode is dishonest scoring, which is avoided by using the rubric strictly.

## Sources

### Primary (HIGH confidence)

- Jacobson, "Thermodynamics of Spacetime: The Einstein Equation of State," PRL 75 (1995) 1260, arXiv:gr-qc/9504004 -- original thermodynamic derivation
- Jacobson, "Entanglement Equilibrium and the Einstein Equation," PRL 116 (2016) 201101, arXiv:1505.04753 -- entanglement equilibrium framework used in Paper 6
- Bisognano-Wichmann, JMP 16 (1975) 985; JMP 17 (1976) 303 -- modular Hamiltonian = boost generator
- Lovelock, "The Einstein Tensor and Its Generalizations," JMP 12 (1971) 498 -- uniqueness theorem
- Casini-Huerta-Myers, JHEP 1105:036 (2011), arXiv:1102.0440 -- conformal modular Hamiltonian
- Hastings-Koma, CMP 265 (2006) 781 -- exponential clustering from spectral gap
- Dyson-Lieb-Simon, J. Stat. Phys. 18 (1978) 335 -- Neel order proof
- Phase 32-35 derivation files (project-internal, HIGH confidence for what they prove)

### Secondary (MEDIUM confidence)

- Giudici et al., PRB 98 (2018) 134403, arXiv:1807.01322 -- lattice-BW numerical evidence
- Speranza (2016) -- non-conformal corrections to modular Hamiltonian
- Sorce (2024) -- geometric modular flow requires conformal symmetry
- Connes-Rovelli, CQG 11 (1994) 2899 -- thermal time hypothesis
- Van Raamsdonk, Gen. Rel. Grav. 42 (2010) 2323, arXiv:0907.2939 -- entanglement and geometry

### Tertiary (LOW confidence)

- Lashkari-McDermott-Van Raamsdonk (2014) -- linearized Einstein from holographic first law (comparison)
- Cao-Carroll-Michalakis (2017) -- space from Hilbert space (comparison)

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- Jacobson 2016, Lovelock, BW, CHM are all textbook-level results
- Standard approaches: HIGH -- sequential assembly is the standard method
- Computational tools: HIGH -- no new computation needed
- Validation strategies: HIGH -- consistency checks are straightforward
- Gap scoring judgments: MEDIUM -- honest assessment is the goal, but reasonable people can disagree on NARROWED vs CONDITIONAL

**Research date:** 2026-03-30
**Valid until:** Indefinite for the physics; Phase 32-35 results are project-specific and stable.

## Caveats and Alternatives (Self-Critique)

1. **Am I underestimating the strength of the chain?** Possibly. The combination of FISH-01/02 + CORR-03 + LRNZ-01/02 + BWEQ-01/02 provides a more complete argument than any previous lattice-to-Einstein program. The honest assessment may look pessimistic compared to what the results actually achieve. Counter: better to be conservative and let the results speak.

2. **Should I recommend a different scoring rubric?** The 4-level CLOSED/NARROWED/CONDITIONAL/OPEN scale is from the phase description. An alternative would be a numerical confidence (0-100%). I stay with the 4-level scale because it maps directly to the requirement (ASBL-02) and avoids false precision.

3. **Is there a simpler assembly?** I could recommend just writing a table mapping each gap to its outcome. But the phase description requires "a reader familiar with Papers 5-6 can follow the argument without re-deriving prior results," which means a narrative chain document, not just a table.

4. **What about the d=1 case?** The chain is strongest in d=1 (WZW CFT, conformal modular Hamiltonian exact) but the Einstein tensor vanishes identically in 1+1 dimensions, so the result is trivial (cosmological constant equation only). This is a genuine limitation: the chain is most rigorous where the physics is least interesting (d=1), and most interesting where the chain is conditional (d>=3). This should be stated honestly.

5. **What about higher Lovelock terms?** In d+1 > 4, Lovelock's theorem allows Gauss-Bonnet and higher curvature terms. The chain restricts to d+1 <= 4 (so d <= 3 spatial dimensions) for Route B, or must assume the second-derivative restriction separately. Paper 6 already notes this.
