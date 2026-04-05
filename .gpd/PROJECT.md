# Experiential Measure on Structure Space

## What This Is

Deriving the fundamental laws of physics from the algebraic structure of self-modeling composite processes. v1.0 formalized the experiential measure framework. v2.0 derived QM from a single operational premise (Paper 5). v3.0 derived GR via locality -> area law -> Jacobson (Paper 6). v4.0 found that simple M_n(C) cannot give SM gauge group (structural obstruction). v5.0 derived chirality from h_3(O) via Cl(6), assembling Paper 7 with 9-link chain conditional on Gaps A, B1, B2. v6.0 proved that Gap C cannot be closed algebraically (all 4 Peirce-mediated routes failed -- but those routes looked for complexification internal to h_3(O)). v7.0 derived entropy gradient theorem, Landauer bound on self-modeling, and three-consequence theorem; narrowed Gap C for SM-like observers but did not close it. v8.0 proved basin impossibility theorems for Gap C; Paper 7 complexification claim correct. v9.0 demonstrated the continuum limit mechanism on a Heisenberg toy model: Fisher geometry, emergent Lorentz, BW/KMS, Jacobson -- chain conditionally complete for d>=3. v10.0 proves the self-modeler network in h_3(O) is in the right universality class to close all four Paper 6 gaps unconditionally. The subfield is mathematical physics / quantum foundations / information geometry.

## Core Research Question

Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself?

## Current Milestone: v11.0 Gap C Complexification from Sequential Product

**Goal:** Close Gap C algebraically by showing the observer's C-linear sequential product extends the measurement algebra Cl(9,0) to Cl(9,C), forcing spinor module complexification S_9 -> S_{10}^+.

**Target results:**

- Prove or disprove that C-linear composition of real Cl(9,0) generators via the observer's sequential product extends to Cl(9,C)
- If successful: state Gap C closure as a single theorem (C*-observer -> complexification -> Spin(10) -> chirality)
- If unsuccessful: characterize the precise obstruction and evaluate contingency routes (Peirce multiplication, conditional expectations, GNS, tensor product, observable algebra)

## Current State (after v10.0)

The derivation chain from self-modeling to Einstein equations now runs on the real algebra h_3(O), not a toy model. Key established results:

- **Algebraic segment (unconditional):** Self-modeling -> h_3(O) -> Peirce -> Cl(9,0) -> H_eff = J*sum T_a T_a -> Z^d bipartite lattice
- **SSB segment (classical proved):** Spin(9)->Spin(8) on S^8 via FSS infrared bounds (d>=3); 8 Type-A Goldstone modes; O(9) NL sigma model asymptotically free
- **Gravity segment (conditional):** Fisher geometry -> Lorentz -> BW/KMS -> Jacobson -> Einstein, with O(9)-specific values (c_s=J*sqrt(3/2), v_LR=27eJ)
- **Gap status:** A NARROWED (d>=3), B CLOSED/OPEN, C CONDITIONAL-DERIVED (tensoriality derived via Lovelock), D CONDITIONAL-THEOREM (MVEH proved via Gibbs)
- **Single remaining conditionality:** Quantum SSB at S_eff=1/2 (BCS fails, Speer blocks quantum RP)

## v10.0 Summary (complete 2026-03-31)

Universality class of self-modeler network and full gap closure. Effective Hamiltonian H_eff computed from Peirce multiplication: 256x256 Clifford-Heisenberg model with Spin(9) symmetry, ferromagnetic ground state. Classical SSB Spin(9)->Spin(8) proved via FSS (d>=3). 8 Type-A Goldstone modes (rho_ab=0, real Clifford). O(9) sigma model on S^8, asymptotically free (Ric=7g). UC1-UC4 all classical-verified. Gap C upgraded CONDITIONAL-DERIVED, Gap D upgraded CONDITIONAL-THEOREM. Complete 12-link chain (a')-(l) on h_3(O) with O(9)-specific values. Conditionally complete for d>=3; quantum SSB (S_eff=1/2) is single remaining conditionality.

## v9.0 Summary (complete 2026-03-30)

Continuum limit from finite-dimensional observer. Six-link derivation chain assembled from finite-dim observer (Paper 5) to Einstein equations (Jacobson 2016). Fisher metric smooth and positive-definite at finite N (FISH-01/02); distance recovery fails in 1D (FISH-03) but rescued for d>=2 by Neel LRO (CORR-03 conditional theorem). Sigma model c_s = 1.659 Ja (QMC 0.3%). Emergent Lorentz via RG irrelevance + DLS. BW/KMS derived (not assumed), Jacobson inputs J1-J3 packaged. Four Paper 6 gaps scored individually: Gap A NARROWED (d>=3), Gap B CLOSED (d=1 Route A only), Gaps C,D CONDITIONAL. Chain conditionally complete for d>=3.

## v8.0 Summary (complete 2026-03-29)

Basin impossibility proved, Paper 7 complexification claim correct. Observable algebra = M_16(R), three impossibility theorems (Schur commutant, grade separation, minimal input = u in S^6). 71 tests, zero error.

## v7.0 Summary (complete -- weakened)

Arrow of time and thermodynamics of self-modeling. The math is solid but the gap-closing claim failed:
1. **Entropy gradient theorem** proved via 3 independent routes: self-modelers require S(t) < S_max
2. **Landauer bound** W >= kT I(B;M) on self-modeling cycle; coherence loophole closed
3. **Three-consequence theorem** extending Paper 7: u in S^6 determines gauge + chirality + time-orientation requirement
4. **Gap C narrowed** for SM-like observers: complexification necessary for chirality, which requires time-orientation
5. **Gap C NOT closed**: the selection chain's contrapositive was invalid; non-SM self-modelers in non-complexified blocks remain open
6. Paper 8 drafted, reviewed (critical logic error found and fixed), revised to minor-revision status

## Scoping Contract Summary

### Contract Coverage

- **Continuum limit (claim-continuum):** Show that a finite-dimensional C*-observer on the SWAP lattice necessarily sees smooth effective geometry, closing all four Paper 6 gaps
- **Fisher geometry (claim-fisher):** Reduced states rho_Lambda(x) form a smooth manifold with positive-definite Fisher information metric recovering lattice distance
- **Correlation structure (claim-decay):** Characterize correlation decay for SWAP Hamiltonian ground state. Heisenberg AFM (n=2) in d>=2 is GAPLESS with algebraic decay (Neel order, Goldstone modes). Two-tier approach: rigorous for gapped models, NL sigma model effective theory argument for n=2
- **Emergent Lorentz (claim-lorentz):** Isotropy + LR finite speed + Fisher smoothness -> Lorentz invariance via von Ignatowsky
- **Acceptance signal:** Complete derivation chain from finite-dim observer to Einstein equations with all steps rigorous (or honestly flagged as conditional)
- **False progress to reject:** Claiming constructive continuum limit in mathematical sense; assuming exponential decay without proof/citation for n=2; citing Lorentz invariance without connecting to the specific Fisher metric; treating BW as automatic without checking Wightman axioms in effective theory

### User Guidance To Preserve

- **User-stated observables:** Fisher information metric g_ij(x) on reduced states; correlation decay rate xi; LR velocity as effective speed of light; SRF convergence for BW
- **User-stated deliverables:** Derivation chain document: finite-dim observer + SWAP + decay -> Fisher manifold -> Lorentz -> BW -> Jacobson -> Einstein
- **User-stated phases:** (A) Fisher geometry, (B) Correlation structure (gapless for n=2 d>=2; two-tier strategy), (C) Emergent Lorentz, (D) BW/equilibrium, (E) Assembly
- **Must-have references:** Braunstein-Caves 1994, Zanardi et al. 2007, Provost-Vallee 1980, Hastings 2004/2007, Nachtergaele-Sims 2006, von Ignatowsky 1911, Hamma et al. 2009, Dyson-Lieb-Simon 1978, Papers 5-6
- **Stop / rethink conditions:** If Fisher metric fails to be positive-definite on reduced states; if exponential decay cannot be established even for n=2 in d>=2; if the effective theory doesn't satisfy Wightman axioms needed for BW
- **Strategy on failure:** If exponential decay fails for all n, the chain is conditional (like MVEH in Paper 6 v3.0). If Fisher geometry fails, the entire approach is wrong. If Lorentz fails, fall back to emergent diffeomorphism invariance only.

### Scope Boundaries

**In scope**

- Fisher information geometry on manifold of reduced states rho_Lambda(x)
- Exponential correlation decay for SWAP Hamiltonian (prove n=2, conjecture general n)
- Emergent Lorentz invariance via von Ignatowsky (isotropy + finite speed)
- BW theorem and local equilibrium in effective theory
- Assembly of complete derivation chain closing Paper 6 gaps
- Numerical verification on small lattices (N=8-20)

**Out of scope**

- Constructive continuum limit in mathematical sense (convergence of correlators to continuum QFT)
- Re-deriving Papers 5, 6, 7 results
- Gap C, Gaps A/B1/B2 (separate milestones)
- Spectral action computation
- New paper writing (derivation document only; paper revision deferred)

### Active Anchor Registry

- **ref-braunstein-caves1994:** Braunstein-Caves -- Statistical distance and the geometry of quantum states (PRL 72, 1994)
  - Why it matters: Fisher information metric on quantum state manifolds; foundation for Phase A
  - Carry forward: planning, execution, verification
  - Required action: read, cite

- **ref-hastings2004:** Hastings -- Spectral gap and exponential decay of correlations (CMP 265, 2006)
  - Why it matters: Gap -> exponential decay theorem; foundation for Phase B
  - Carry forward: execution, verification
  - Required action: read, cite

- **ref-nachtergaele-sims2006:** Nachtergaele-Sims -- Lieb-Robinson bounds (CMP 265, 2006)
  - Why it matters: LR bounds for lattice systems; provides finite speed for Phase C
  - Carry forward: execution, verification
  - Required action: read, cite

- **ref-vonignatowsky1911:** von Ignatowsky -- Das Relativitatsprinzip (Archiv der Mathematik und Physik 17, 1911)
  - Why it matters: Isotropy + finite max speed -> Lorentz; key theorem for Phase C
  - Carry forward: execution
  - Required action: read, cite

- **ref-zanardi2007:** Zanardi et al. -- Information-geometric differential equations (PRA 76, 2007)
  - Why it matters: Information geometry of quantum phase transitions; Fisher metric on state manifolds
  - Carry forward: planning, execution
  - Required action: read, cite

- **ref-paper5:** Paper 5 (v2.0) -- QM from self-modeling
  - Why it matters: CRITICAL -- M_n(C)^sa finite-dimensional; the observer IS the UV cutoff
  - Carry forward: planning, execution, verification
  - Required action: read, cite

- **ref-paper6:** Paper 6 (v3.0) -- GR from self-modeling
  - Why it matters: SWAP lattice, area law, Jacobson route; the four gaps this milestone closes
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite, update

### Carry-Forward Inputs

- Paper 5: M_n(C)^sa with dim n^2 -- observer's finite dimension is the UV cutoff mechanism
- Paper 6: SWAP lattice H = sum J*SWAP, area law, Jacobson route, four gaps (continuum limit, conformal, tensoriality, MVEH)
- Paper 6 Phase 11: ED benchmarks N=8-20, area-law scaling, K_A locality (SRF=0.9993), MVEH support
- v3.0: Nachtergaele-Sims LR bound v_LR = 8eJ/(e-1) computed for SWAP on Z^1

### Skeptical Review

- **Weakest anchor:** Heisenberg AFM (n=2) in d>=2 is gapless with algebraic (not exponential) correlation decay due to Neel order and Goldstone modes. Fisher geometry smoothness with algebraic decay is an open question -- no rigorous resolution exists in the literature.
- **Unvalidated assumptions:** That the Fisher metric on reduced states is non-degenerate (it should be, but needs proof); that lattice symmetry group gives sufficient isotropy for von Ignatowsky; that the effective theory satisfies Wightman axioms needed for BW
- **Competing explanation:** Continuum limit might require genuinely new mathematics beyond the observer-as-cutoff picture. The information-geometric approach might give smoothness but not the right symmetry group.
- **Disconfirming observation:** Fisher metric degenerate at some lattice points; exponential decay fails for SWAP (gapless ground state); LR velocity direction-dependent at long wavelengths (breaking isotropy)
- **False progress to reject:** Numerics on small lattices showing "smooth" behavior that's actually finite-size artifact; citing von Ignatowsky without verifying his premises hold in the lattice setting; treating BW as automatic without checking axioms

### Open Contract Questions

- Does the Fisher metric on reduced states have the right signature for Lorentzian geometry (or only Riemannian)?
- Is the connection from Fisher metric to spacetime metric unique, or are there ambiguities?
- Does the SWAP Hamiltonian in d=3 have a spectral gap for all n, or only certain n values?
- Can the BW theorem be applied to the effective theory, or do we need a lattice version?

## Research Questions

### Answered

- [x] Can the 7 lemmas in Theorem A's dependency graph be assembled into a self-contained proof with explicit error scaling? -- **YES.** Proof assembled with composite error rate gamma = min(alpha/2, Ds - alpha). Validated on three-state chain across 9 parameter combinations. -- v1.0
- [x] Is the experiential density rho Lipschitz continuous in the transition kernel, and what is the constant L? -- **YES.** L = (C_I + C_H)/gap(P), scaling as ln|Omega|/gap. Verified numerically: 3000 perturbations, zero violations. -- v1.0
- [x] Do Born-rule distributions satisfy I_vN(B;M) = S_vN(B)/2 in a toy qubit composite process? -- **NO. Conjecture FALSIFIED.** rho_Q <= 0 throughout all 1900+ Lindblad trajectories; mu_Q identically zero. -- v1.0
- [x] Does the self-modeling sequential product satisfy van de Wetering's axioms S1-S7? -- **YES.** All seven axioms proved for the corrected product on finite-dim spectral OUS. S4 proved via facial orthogonality (phi-independent). -- v2.0
- [x] Does S4 (symmetry of orthogonality) hold for the self-modeling construction? -- **YES.** Proved via facial orthogonality argument; holds for all mixing functions f with f(0,x)=0. -- v2.0
- [x] Does B-M compositionality (independent accessibility) imply local tomography? -- **YES.** Proved via state separation on minimal composite OUS. dim(V_BM) = dim(V_B) * dim(V_M). -- v2.0
- [x] Which effect algebra framing is correct for the self-modeling sequential product? -- **E(B).** E(B x M) framing fails in three ways; E(B) framing gives correct corrected product formula. -- v2.0
- [x] Does self-modeling locality force area-law entanglement entropy? -- **YES** via WVCH (thermal MI) and channel capacity (pure S); sub-volume scaling for gapless case. -- v3.0
- [x] Does a lattice of self-modeling M_n(C)^sa systems satisfy Jacobson's thermodynamic inputs? -- **YES**: (J1) area law established, (J2) entanglement first law exact, (J3) MVEH as structural identification via Connes-Rovelli. -- v3.0
- [x] Can Einstein's field equations be derived from self-modeling? -- **YES** via two routes: Jacobson entanglement equilibrium (Route A, conformal) and Lovelock uniqueness (Route B, d>=2). Paper 6 assembled. -- v3.0
- [x] Does the order zero condition [a, Jb*J^{-1}] = 0 hold for the natural algebra action? -- **YES.** [pi(a), pi_o(b)] = 0 for all a, b in M_n(C) at general n. -- v4.0
- [x] What Dirac operator D arises naturally from the sequential product's temporal asymmetry? -- **Barrett-form D_K(X) = KX + XK** with K real symmetric. D moduli dim = n^2(n^2+1). Jordan product = linearized sequential product. -- v4.0
- [x] What subalgebra A_F does the first-order condition force? -- **A_F = M_n(C)** for Barrett D (trivially satisfied); **A_F = C** for general D. No D produces C + H + M_3(C). -- v4.0
- [x] Does the doubled self-modeling composite carry a real spectral triple of KO-dimension 6? -- **YES** (valid spectral triple with U(n) gauge group), but simple M_n(C) cannot give SM. Structural obstruction: SM requires direct sum algebra. -- v4.0

### Answered in v8.0

- [x] Do C*-observer Peirce multiplication maps L_a: V_{1/2} -> V_{1/2} force complexification of V_{1/2} = O^2 in h_3(O)? -- **NO (basin alone).** Observable algebra = M_16(R); containment of J_u is vacuous. Three impossibility theorems prove basin's Peirce structure cannot force complexification. Observer's C*-nature (Paper 5) remains the correct justification. -- v8.0
- [x] Does the observer's complex structure (u in S^6) upgrade V_1 from R*E_{11} to a complex 1-dim space? -- **V_1 = R confirmed.** L_{E_{11}} = (1/2)*I_{16}. V_0 channel: 10 T_b are Cl(9) generators but symmetric (cannot produce antisymmetric J_u). -- v8.0
- [x] If algebraic closure fails, what is the weakest sufficient condition? -- **u in S^6 = Gap B2.** G_2 acts transitively on S^6, so all choices conjugate. Three theorems pin this as the exact additional input. -- v8.0

### Answered in v10.0

- [x] Is the self-modeler network in h_3(O) in the right universality class? -- **YES (classical).** UC1-UC4 all verified for O(9) sigma model on S^8. Quantum UC1/UC4 conditional (S_eff=1/2). -- v10.0
- [x] Do all four Paper 6 gaps close once the universality class is established? -- **CONDITIONALLY.** Gap C upgraded CONDITIONAL-DERIVED (tensoriality derived via Lovelock). Gap D upgraded CONDITIONAL-THEOREM (MVEH proved via Gibbs). Gaps A,B unchanged. 15 assumptions: 8 resolved, 7 assumed. -- v10.0
- [x] What is the effective Hamiltonian H_eff for self-modelers interacting via the Jordan product of h_3(O)? -- **H_eff = J*sum T_a^(1)T_a^(2)** on R^256. 5-level Spin(9) spectrum. Ferromagnetic ground state Lambda^1(V_9). -- v10.0
- [x] Does H_eff exhibit spontaneous F_4 breaking via DLS/infrared bounds? -- **SSB is Spin(9)->Spin(8) on S^8** (not F_4->Spin(9) on OP^2). Classical proved via FSS (d>=3). Quantum conditional. 8 Type-A Goldstone modes. -- v10.0

### Active

- [ ] Does a C*-observer's sequential product (C-linear Luders composition) extend the measurement algebra Cl(9,0) on V_{1/2} to Cl(9,C)?
- [ ] If algebraic extension fails, does Peirce multiplication, GNS, or observable algebra analysis close Gap C via an alternative route?
- [ ] What is the weakest sufficient condition for complexification of V_{1/2} = O^2 inside h_3(O)?

### Answered in v9.0

- [x] Does the Fisher information metric on reduced states of the SWAP ground state recover lattice distance at leading order? -- **NO in 1D** (FISH-03: g_bulk ~ N^{-2.75}), **CONDITIONAL YES in d>=2** (CORR-03: g_F = O(m_s^2) > 0 under H1-H4). Distance recovery fails in 1D but rescued by Neel LRO for d>=2. -- v9.0
- [x] Does the Heisenberg AFM (n=2) on d>=2 lattice have a spectral gap with exponential correlation decay? -- **NO spectral gap; YES algebraic LRO.** Neel order gives m_s > 0 (QMC-established for S=1/2 d=2); correlations = m_s^2 + transverse 1/r^{d-1} from Goldstone modes. Gapped tier has exponential decay (rigorous). -- v9.0
- [x] Does isotropy + LR finite speed + Fisher smoothness uniquely determine Lorentz invariance on the effective manifold? -- **YES via sigma model route.** Isotropy from RG irrelevance (rho~2), O(d+1) rescaling + DLS reflection positivity. c_eff = c_s = 1.659 Ja. Von Ignatowsky supporting route. -- v9.0
- [x] Does the effective theory from Fisher geometry satisfy Wightman axioms sufficient for BW theorem? -- **CONDITIONAL.** W1-W4 satisfied for NL sigma model EFT; W5 conditional on mass gap; W6 open. Lattice-BW (Giudici et al.) bypasses W6, SRF=0.9993. -- v9.0
- [x] Does the complete chain (finite-dim observer -> Fisher -> Lorentz -> BW -> Jacobson) close all four Paper 6 gaps? -- **CONDITIONALLY for d>=3.** Gap A NARROWED, Gap B CLOSED (d=1 Route A only) / OPEN (d>=2), Gap C CONDITIONAL, Gap D CONDITIONAL. Chain assembled with all links explicit. No gap fully CLOSED for d>=3. -- v9.0

### Answered in v7.0

- [x] Does Luders sequential product dynamics produce monotonic entropy increase? -- **YES** under repeated interactions with fresh bath; 2-site oscillates -- v7.0
- [x] Does chirality require time-orientation in the lattice/algebraic context? -- **YES** via Cl(d-1,1) volume form; lattice framing provides spin structure -- v7.0
- [x] Does self-modeling require free energy (Landauer bound)? -- **YES** W >= kT I(B;M) per cycle; coherence loophole closed -- v7.0
- [x] Can the Past Hypothesis be derived from self-modeling + finitude + chirality? -- **PARTIAL** Entropy gradient theorem proved (S < S_max), but does not explain WHY initial entropy was low -- v7.0
- [x] Is complexification a thermodynamic selection effect (rho = 0 for non-complexified)? -- **NO** Original claim invalid (wrong contrapositive). Narrowed: complexification necessary for SM-like observers, but non-SM blocks open -- v7.0

### Answered in v6.0

- [x] Do C*-observer measurement maps on V_{1/2} force complexification? -- **NO.** All 4 algebraic routes failed. V_1 = R bottleneck. Gap C cannot be closed algebraically. -- v6.0
- [x] Is there an h_3(O)-specific mechanism for complexification? -- **NO.** Only generic extension of scalars (works for any real V). -- v6.0

### Answered in v5.0

- [x] Does C*-algebra observer nature force complexification of h_3(O) Peirce decomposition? -- **YES.** Extension of scalars V_{1/2}^C = S_{10}^+ follows from C*-nature alone. -- v5.0
- [x] Does complexification upgrade Spin(9) to Spin(10) on V_1 = O^2? -- **YES.** Branching rule S_{10}^+|_{Spin(9)} = S_9^C; F_4 -> E_6. -- v5.0
- [x] Does the O = C + C^3 splitting induce Cl(6) inside Cl(10) with chiral volume form? -- **YES.** omega_6^2 = -1, P = (1/2)(1-i*omega_6), tr(P) = 16. -- v5.0
- [x] Does the Cl(6)/Pati-Salam route give the SM gauge group with LEFT embedding? -- **YES.** SU(4) x SU(2)_L x SU(2)_R -> SU(3)_C x SU(2)_L x U(1)_Y with LEFT. All 16 SM quantum numbers verified. -- v5.0
- [x] Is chirality automatic (Furey) or does it require an additional discrete choice? -- **Automatic given u.** Witt decomposition channels SU(2) to single chirality without ad hoc projectors. The choice of u in S^6 is the remaining input (Gap B2). -- v5.0

### Out of Scope

- Countable/continuous state space generalization -- paper-length work, deferred
- Non-Markovian quantum channels -- could produce rho_Q > 0 regime, untested
- Non-equilibrium extension -- requires different mathematical framework
- Reference measure nu -- shared open problem with Mueller (2020)
- Self-modeling constants experiment -- Level 6, requires experimental apparatus
- Full spectral action computation (coupling constants, Higgs mass) -- beyond Paper 7 scope
- Phenomenological predictions -- requires spectral action computation

## Research Context

### Physical System

A single self-modeling composite: body B and model M, each carrying M_n(C)^sa (from Paper 5). The doubled Hilbert space H = (C^n x C^n)_particle + (C^n x C^n)_antiparticle, where the two sectors correspond to which subsystem plays the observer role. The SWAP operator P decomposes C^n x C^n into Sym^2(C^n) (P=+1) and wedge^2(C^n) (P=-1). The construction (H, J, gamma) with J(psi, chi) = (PC chi-bar, PC psi-bar) and gamma(psi, chi) = (P psi, -P chi) gives KO-dimension 6 sign relations (J^2 = +1, J gamma = -gamma J verified).

### Theoretical Framework

Noncommutative geometry (Connes program): real spectral triples, KO-dimension classification, spectral action principle. Key tools: order zero condition, first-order condition, Chamseddine-Connes classification theorem. Built on algebraic quantum theory (Paper 5) and SWAP/Schur-Weyl structure (Paper 6).

### Key Parameters and Scales

| Parameter | Symbol | Regime | Notes |
| --------- | ------ | ------ | ----- |
| Local algebra dimension | n | General, then specialize | Each site is M_n(C)^sa; n=4 conjectured for SM |
| Hilbert space dimension | dim(H) | 2n^2 | Doubled: particle + antiparticle sectors |
| KO-dimension | d_KO | 6 | Sign relations J^2=+1, J gamma=-gamma J verified |
| Symmetric sector dim | dim(Sym^2) | n(n+1)/2 | SWAP eigenvalue +1 |
| Antisymmetric sector dim | dim(wedge^2) | n(n-1)/2 | SWAP eigenvalue -1 |

### Known Results

- v2.0: Self-modeling forces M_n(C)^sa with Luders product and J = conjugate transpose (Paper 5)
- v2.0: Sequential product a.b = sqrt(a) b sqrt(a), temporally asymmetric (a.b != b.a)
- v3.0: SWAP Hamiltonian forced by diagonal U(n) covariance + Schur-Weyl (Paper 6)
- v3.0: Einstein's equations via Jacobson (Route A) and Lovelock (Route B)
- Connes (1995): Real spectral triple axioms, KO-dimension classification
- Chamseddine-Connes (2008): KO-dim 6 + first-order condition -> C + H + M_3(C)
- Verified: J^2 = +1 and J gamma = -gamma J for the candidate construction

### What Is New

Constructing a spectral triple directly from the self-modeling composite's algebraic structure, without postulating particle physics content. The doubled Hilbert space, J (observer swap), and gamma (SWAP x matter-sign) all arise from self-modeling. If the spectral triple axioms are satisfied and the first-order condition gives C + H + M_3(C), this would derive the Standard Model gauge group from self-modeling -- a result with no precedent.

### Target Venue

Journal of Mathematical Physics, Communications in Mathematical Physics, or Journal of Noncommutative Geometry. High-impact if SM gauge group emerges.

### Computational Environment

Local workstation. Algebraic proofs + SymPy verification. Python for explicit matrix computations at small n.

## Notation and Conventions

See `.gpd/CONVENTIONS.md` for all notation and sign conventions.
See `.gpd/NOTATION_GLOSSARY.md` for symbol definitions.

## Unit System

Natural units (hbar = c = k_B = 1) for the GR/thermodynamic portions. Dimensionless for algebraic portions (Paper 5 framework).

## Requirements

See `.gpd/REQUIREMENTS.md` for the detailed requirements specification.

## Key References

- Braunstein-Caves (1994), PRL 72 -- Statistical distance and geometry of quantum states (Fisher metric)
- Zanardi et al. (2007), PRA 76 -- Information geometry of quantum phase transitions
- Provost-Vallee (1980), CMP 76 -- Riemannian structure on manifolds of quantum states
- Hastings (2004/2006), CMP 265 -- Spectral gap implies exponential decay of correlations
- Hastings (2007), JSTAT -- Area law in 1D from spectral gap
- Nachtergaele-Sims (2006), CMP 265 -- Lieb-Robinson bounds for lattice systems
- von Ignatowsky (1911), Archiv Math. Phys. 17 -- Lorentz group from isotropy + finite speed
- Hamma et al. (2009) -- Lieb-Robinson and Lorentz invariance on lattices
- Dyson-Lieb-Simon (1978) -- Phase transitions in quantum Heisenberg models
- Paper 5 (this project, v2.0) -- QM from self-modeling; M_n(C)^sa finite-dimensional
- Paper 6 (this project, v3.0) -- GR from self-modeling; SWAP lattice, four gaps to close

## Constraints

- **Finite dimensions:** All proofs for finite-dimensional systems only (Paper 5 restriction)
- **Rigorous proofs:** Algebraic identities must be proved exactly, not argued physically; SymPy verification required
- **Papers 5-6 as input:** Takes M_n(C)^sa, J = dagger, sequential product, SWAP Hamiltonian as established
- **No ad hoc choices:** J, gamma, D must be derived from self-modeling structure, not postulated to match Connes
- **General n first:** Work at general n, then specialize; do not assume n=4 until forced

## Key Decisions

| Decision | Rationale | Outcome |
| -------- | --------- | ------- |
| Clean composition over full explicit constants | User prefers self-contained proof with error scaling; constants in appendix | Good -- proof is self-contained |
| Qubit falsification over variational structure | Decisive test first; if it fails, variational work is moot | Good -- conjecture falsified, saved wasted effort |
| Lipschitz over countable extension | Needed for approximate factorization; countable extension is paper-length | Good -- Lipschitz bound proven with explicit constants |
| Deep-theory model profile | Heavy proof work benefits from tier-1 models | Good -- all proofs completed |
| 3 standalone papers over single monograph | Papers written independently for different audiences | Revisit -- peer review suggests Paper 2 may be better as section of Paper 1 |
| Honest framing over cosmological claims | Peer review flagged overclaiming; reframed titles and abstracts | Good -- papers now accurately scope their claims |
| Sequential product route over direct involution construction | van de Wetering axioms give cleaner path; D'Ariano as backup | Good -- S1-S7 all proved, backup not needed |
| Explore both effect algebra framings | Correct framing is a Phase 1 result, not a premise | Good -- E(B) selected, E(B x M) failure documented |
| Lattice architecture for GR extension | Connects directly to Hastings area-law machinery; Cao-Carroll-Michalakis precedent | Pending |
| Strong argument over full theorem | First pass; full theorem too ambitious; bare conditional too weak | Pending |
| Standalone Paper 6 over Paper 5 extension | Clean conceptual separation: Paper 5 = QM, Paper 6 = GR | Pending |

## v1.0 Summary (complete)

All three formal gaps in the experiential measure framework are closed:
1. **Theorem A** assembled from 7 metastability lemmas with explicit error composition
2. **Lipschitz stability** proven with L = (C_I + C_H)/gap(P), verified numerically
3. **Born-Fisher conjecture falsified** -- rho_Q <= 0 for all exchange-plus-dephasing Lindblad dynamics (proved analytically)

Three papers written, peer-reviewed (18-agent 6-pass panel), and revised.

## v2.0 Summary (complete)

QM derived from a single operational premise (faithful self-modeling):
1. **Sequential product formalized** on finite-dim spectral OUS; corrected product with Peirce 1-space feedback
2. **S1-S7 all proved** -- S4 via facial orthogonality (phi-independent); functional form f = sqrt(xy) forced by S5 + S2
3. **Local tomography proved** from faithful tracking via state separation on minimal composite
4. **Type exclusion** -- all non-complex EJA types excluded by dimension counting + Barnum-Wilce
5. **C*-algebra promotion** via vdW Theorem 3; involution = conjugate transpose

Paper 5 assembled, passed three rounds of adversarial review. Chain: L4 -> SP -> EJA -> LT -> type exclusion -> C*-algebra -> M_n(C)^sa.

## v3.0 Summary (complete)

GR derived from self-modeling locality:
1. **Self-modeling lattice** with SWAP Hamiltonian forced by diagonal U(n) covariance + Schur-Weyl
2. **Area-law entanglement** via WVCH (thermal MI), Heisenberg ground-state properties, modular Hamiltonian locality
3. **Einstein's equations** via two routes: Jacobson entanglement equilibrium (Route A, conformal) and Lovelock uniqueness (Route B, d>=2)
4. **Numerical verification** on N=8-20 lattices: ED benchmarks, area-law scaling, K_A locality, MVEH support

Paper 6 assembled, passed adversarial review. Gaps honestly identified: continuum limit (shared wall), conformal approximation (Route A), tensoriality (Route B).

## v4.0 Summary (closed, medium success)

Spectral triple investigation for self-modeling composite:
1. **Order zero verified** -- [pi(a), pi_o(b)] = 0 at general n; bimodule H = 2 x C^{n^2}; k=4 at n=4
2. **D moduli parameterized** -- dim = n^2(n^2+1); Barrett-form D = Jordan product (linearized sequential product)
3. **First-order condition resolved** -- Barrett D: A_F = M_n(C) (gauge U(n)); general D: A_F = C (gauge U(1))
4. **Structural obstruction** -- Simple M_n(C) cannot produce SM gauge group C + H + M_3(C). SM requires direct sum starting algebra.

Phases 16-17 abandoned. New approach needed for Paper 7.

## v5.0 Summary (complete)

Chirality from h_3(O) via Cl(6):
1. **Complexification derived** -- C*-observer nature forces extension of scalars on Peirce V_{1/2} = O^2, upgrading Spin(9) -> Spin(10), F_4 -> E_6
2. **Cl(6) chirality** -- O = C + C^3 splitting by u induces Cl(6) inside Cl(10); volume form omega_6 selects LEFT embedding via Pati-Salam breaking; all 16 SM quantum numbers verified
3. **One choice, two consequences** -- Single u in S^6 simultaneously gives SM gauge group (F_4 intersection) and chirality (Cl(6) volume form)
4. **Paper 7 assembled** -- 6 sections, 9-link chain L1-L9, honest gap register (B1/B2 HIGH, A MEDIUM, Gen/SA LOW), zero overclaiming

Result conditional on three gaps: A (non-composability), B1 (idempotent choice), B2 (complex structure choice).

## v6.0 Summary (closed, negative result)

Gap C algebraic investigation:
1. **All 4 routes NEGATIVE** -- conditional expectations, state-effect duality, GNS, tensor product all failed to find h_3(O)-specific complexification mechanism
2. **Root cause** -- V_1 = R*E_11 is 1-dimensional; Peirce interface is scalar multiplication by 1/2; no complex structure transmittable
3. **No C*-subalgebra inside h_3(O)** (Shirshov-Cohn) -- observer necessarily external
4. **Extension of scalars** is valid but generic (works for any real V with any C-algebra)

Phases 23-25 cancelled. Gap C requires non-algebraic resolution -- motivates v7.0 thermodynamic approach.

---

_Last updated: 2026-04-04 after v11.0 milestone initialization_
