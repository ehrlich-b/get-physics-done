# Experiential Measure on Structure Space

## What This Is

Deriving the fundamental laws of physics from the algebraic structure of self-modeling composite processes. v1.0 formalized the experiential measure framework. v2.0 derived QM from a single operational premise (Paper 5). v3.0 derived GR via locality -> area law -> Jacobson (Paper 6). v4.0 found that simple M_n(C) cannot give SM gauge group (structural obstruction). v5.0 derived chirality from h_3(O) via Cl(6), assembling Paper 7 with 9-link chain conditional on Gaps A, B1, B2. v6.0 proved that Gap C cannot be closed algebraically (all 4 Peirce-mediated routes failed -- but those routes looked for complexification internal to h_3(O)). v7.0 derived entropy gradient theorem, Landauer bound on self-modeling, and three-consequence theorem; narrowed Gap C for SM-like observers but did not close it. v8.0 proved basin impossibility theorems for Gap C; Paper 7 complexification claim correct. v9.0 demonstrated the continuum limit mechanism on a Heisenberg toy model: Fisher geometry, emergent Lorentz, BW/KMS, Jacobson -- chain conditionally complete for d>=3. v10.0 proves the self-modeler network in h_3(O) is in the right universality class to close all four Paper 6 gaps unconditionally. v11.0 closed Gap C: C*-observer sequential product extends Cl(9,0) to Cl(9,C), theorem assembled with L1-L9 zero regressions. v12.0 derived Einstein gravity algebraically: V_0 = h_2(O) projected via pi_u to R^{3,1} carries GST magic supergravity with prepotential det(X); Weinberg 1964 forces -R/2 from spin-2 + universal coupling (all algebraic inputs from h_3(O)). Complete SM+GR assembly DAG with 18 nodes verified acyclic. 13 gaps catalogued honestly (chain-critical: N=2 SUSY as input, compact so(3) vs so(3,1)). v13.0 closes the two chain-critical algebraic gaps: V_0 = spacetime derived via operational definition match (OD1-OD7 + KKT(h_2(C_u)) = so(4,2) + F_4 covariance), and N=2 SUSY derived as consequence of Lagrangian uniqueness from det(X) + E_{6(-26)} via GST classification. v14.0 is a Paper 5 revision cycle: Paper 5 is 16+ days with the JMP associate editor (JMP26-AR-00922, Zenodo DOI 10.5281/zenodo.19342703). A jigsaw-piece-level review identified 6 places where the logical chain is visually sound but the author cannot independently reconstruct the argument from primitives; close them before the referee report lands so revisions ship fast and survive scrutiny. The subfield is mathematical physics / quantum foundations / information geometry.

## Core Research Question

Can the Standard Model + GR be derived from the requirement that a composite system faithfully models itself?

## v12.0 Summary (complete 2026-04-12)

Einstein gravity derived algebraically from h_3(O) via GST magic supergravity. pi_u: h_2(O) -> h_2(C_u) = R^{3,1} with Minkowski signature (1,3). d_{IJK} tensor computed (106 nonzero, 97% sparse). det(X) unique F_4-invariant cubic (Springer 1962). V_0 stabilizer = so(3) x so(6), pi_u equivariant. 4d N=2 MESGT: 1 gravity + 26 vectors, prepotential F(X) = d_{IJK} X^I X^J X^K / (6 X^0). C_{IJK} decomposed: 10 gravitational + 48 spacetime + 48 internal. Weinberg 1964 applied: spin-2 (10=9+1), massless (M=det_2), universal coupling (C_{i,j,a}) force -R/2 at low energies. Assembly DAG: 18 nodes, 31 edges, acyclic. 13 gaps catalogued. Chain-critical: N=2 SUSY (ASSUMED), compact so(3) vs so(3,1) (CONDITIONAL-DERIVED). Paper 6 lattice route ABANDONED; v12.0 route independent.

## Current State (after v13.0)

The derivation chain (Papers 5-6-7) is complete end-to-end with 13 gaps catalogued. v14.0 does NOT extend this chain. It turns inward: Paper 5 is 16+ days with the JMP associate editor and a jigsaw-piece review found 6 gaps in its internal exposition that must close before the referee report arrives.

Two independent routes to Einstein gravity from self-modeling are established (carried forward from v13.0):

- **Route 1 (v9.0-v10.0, lattice):** Fisher geometry -> Lorentz -> BW/KMS -> Jacobson -> Einstein. Conditional on quantum SSB at S_eff=1/2.
- **Route 2 (v12.0-v13.0, algebraic):** h_3(O) -> Peirce V_0 -> pi_u -> R^{3,1} -> det(X) prepotential -> MESGT (N=2 derived via GST) -> Weinberg -> -R/2.

**Complete chain:** Self-modeling (Paper 5) -> C*-algebra -> h_3(O) (Paper 7) -> QM + SM fermions (V_{1/2}) + chirality (Cl(6)) + spacetime (V_0) + matter-gravity couplings (det(X)) + Einstein gravity (Weinberg). Assembly DAG verified acyclic with 18 nodes.

**Why v14.0 is not more derivation chain work:** Paper 5 is the foundational paper the rest of the chain builds on. If its internal exposition has a §3.3-level gap visible to a referee, everything downstream is weakened at a presentation level. v14.0 is maintenance of the paper that already shipped, not extension of the derivation frontier.

## Current Milestone: v14.0 Paper 5 Revision -- Close Load-Bearing Jigsaw-Piece Gaps

**Goal:** Close 6 jigsaw-piece gaps in Paper 5 before the JMP referee report lands, so revisions ship fast and survive reviewer scrutiny.

**Target results (in order):**

1. §3.3 Peirce preservation from OUS primitives -- outcome (A) proof / (B) precise Alfsen-Shultz citation / (C) structural-gap characterization. **Load-bearing and only phase fully scoped; Phases 2-6 are stubs to be expanded as Phase 1 closes.**
2. S4 facial structure lemma -- precise Alfsen-Shultz citation or standalone proof
3. Thm 5.8 upper bound -- W carries product-form sequential product (currently asserted)
4. Phi inert-wrapper resolution -- stop equivocating across sections
5. Lean axiom audit -- 16 axioms vs cited Alfsen-Shultz / van de Wetering statements
6. Minimal composite assumption defense -- every adversarial reviewer flags this

**Pause condition:** Outcome (C) on any phase -> milestone pauses for human decision on whether to restructure, add an explicit assumption, or rip out and rework. Above GPD's pay grade.

**Dependencies:**

- Paper 5 source (frozen): `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main.tex`, git tag `paper5-jmp-submitted`, revision copy at `main-jmp-submitted.tex`
- §3.3 content: lines 483-562 of `main.tex`; key claim lines 508-528
- Alfsen-Shultz 2003 "Geometry of State Spaces of Operator Algebras" (Birkhauser)
- van de Wetering axioms S1-S7 (§3.2 of Paper 5)
- Paper 5 Lean formalization: `~/repos/research/lean/Paper5/` (0 sorry, 16 axioms)
- Prior GPD v2.0 work on sequential product (Phases 4-6): check whether any of those attempts settled the §3.3 claim or assumed it

**Deliverables location:** `derivations/paper5-peirce-preservation/` (STATE.md, claim.md, attempt-NN.md, RESULT.md, alfsen-shultz-notes.md) for Phase 1.

## v13.0 Summary (complete 2026-04-13)

Closed the two chain-critical algebraic gaps for Paper 6: V_0 = spacetime derived via operational definition match (OD1-OD7 all verified, KKT(h_2(C_u)) = so(4,2) Killing sig (8,7), F_4 covariance, uniqueness theorem via Gr(3,9) classification), and N=2 SUSY derived as consequence of Lagrangian uniqueness from det(X) + E_{6(-26)} via GST classification. Paper 6 claim upgraded to "one definition + one premise -> GR" (no geometric input, no SUSY input). VSR metric G_{IJ} = (9/2)x_Ix_J - 3C_{IJK}h^K with 26 positive tangent eigenvalues; exactly 4 E_{6(-26)}-invariant two-derivative terms proved (-R/2, G d phi d phi, G FF, CAFF); all coefficient ratios fixed without assuming SUSY. GST bijection applied to h_3(O): degree 3 + formally real + positive-definite trace form all verified; unique Lagrangian identified as N=2 MESGT bosonic sector. Phase 49 cross-check max error = 0; circularity audit AC1-AC4 PASS.

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

- **Phase 1 §3.3 claim (claim-peirce):** a o V_2(p_i) c V_2(p_i) and a o V_1(p_i,p_j) c V_1(p_i,p_j) for a = sum lambda_i p_i in a spectral OUS, with sequential product satisfying S1 (additivity in second arg) and S3 (sharp constraint a o b = c_a(b) when a is a projective unit), restricted to OUS primitives only. Outcome must be (A) proof / (B) precise Alfsen-Shultz citation / (C) structural-gap characterization.
- **Acceptance signal (Phase 1):** (A) complete proof with zero uses of Jordan product, EJA, sequential product formula sqrt(lambda mu), C*-structure, or h_n(C); or (B) chapter + section + theorem number in Alfsen-Shultz 2003 that implies the claim from OUS primitives; or (C) explicit gap characterization naming the minimum additional axiom/derivation step needed and the ordering change Paper 5 would require.
- **Milestone-level acceptance signal:** Each of 6 gaps closed with (A), (B), or explicit (C) flag. Revision response text drafted for each closed gap.
- **Adversarial review gate:** Phase 1 outcome reviewed by a second fresh-eyes agent before RESULT.md finalizes.
- **False progress to reject:** "Since a o b is a Jordan product..." (uses the structure being derived); citing the Peirce decomposition theorem as if it proves Peirce invariance of a o (-); conflating "compressions c_{p_i} preserve Peirce subspaces" (Alfsen-Shultz fact about individual compressions) with "a o (-) preserves Peirce subspaces" (claim about the composite map b -> a o b); rate-limiting on "it's obvious" when Paper 5 spends 20 lines asserting it.

### User Guidance To Preserve

- **User-stated observables:** Peirce-preservation property of a o (-) on V_2(p_i) and V_1(p_i,p_j); S1 and S3 axioms as stated in Paper 5 §3.2; compression properties per Alfsen-Shultz 2003 (idempotent, positive, c_p + c_{p'} = id, Peirce decomposition).
- **User-stated deliverables:** `derivations/paper5-peirce-preservation/` tree with STATE.md, claim.md (restated in derivation's own notation), attempt-NN.md (one per serious proof attempt), RESULT.md (outcome A/B/C with proof / citation / gap), alfsen-shultz-notes.md (specific AS theorems consulted with page numbers). Revision text for §3.3 in RESULT.md.
- **User-stated phases:** (1) §3.3 Peirce preservation [fully scoped], (2) S4 facial structure lemma, (3) Thm 5.8 upper bound, (4) Phi inert-wrapper resolution, (5) Lean axiom audit, (6) Minimal composite assumption defense. Phases 2-6 as stubs -- expanded only as Phase 1 closes.
- **Must-have references:** Alfsen-Shultz 2003 "Geometry of State Spaces of Operator Algebras" (Birkhauser); Paper 5 main.tex (frozen at `paper5-jmp-submitted`, copy at `main-jmp-submitted.tex`); van de Wetering S1-S7 axioms; Paper 5 Lean formalization (`~/repos/research/lean/Paper5/`); prior GPD v2.0 Phases 4-6 sequential product work.
- **Stop / rethink conditions:** Outcome (C) on any phase -- milestone pauses for human decision on whether to restructure §3.3 (move Jordan derivation earlier), add an explicit assumption, or rip out and rework. "Above GPD's pay grade."
- **Strategy on failure:** If proof attempts accumulate and none closes cleanly from OUS primitives, escalate to outcome (C) rather than sneak in Jordan structure. Precise citation (B) beats hand-waved proof (A). Honest gap (C) beats contested proof.

### Scope Boundaries

**In scope**

- OUS / spectral order unit space primitives: order unit, compressions (idempotent, positive, c_p + c_{p'} = id, Peirce decomposition), faithful normal states
- van de Wetering S1 (additive in second arg), S3 (sharp constraint a o b = c_a(b) when a is projective unit)
- Linear endomorphism property of a o (-): allowed as an input to Phase 1 per Paper 5
- Alfsen-Shultz 2003 page-level consultation
- Lean formalization audit (Phase 5) -- 16 axioms vs cited Alfsen-Shultz / vdW
- Deriving minimum revision text for each Paper 5 section touched

**Out of scope**

- Any use of Jordan multiplication, EJA structure, sequential product formula f(lambda,mu) = sqrt(lambda mu), or C*-structure in Phase 1 proof
- Any use of h_n(C) or specific EJA realization in Phase 1 proof
- Anything downstream of §3.3 (S4, S5, sequential product formula, etc.) in Phase 1 proof
- Revisiting Paper 6 / Paper 7 / v13.0 results
- New derivation chain extensions (no new physics)
- Major restructuring of Paper 5 without human approval (any outcome (C) pauses milestone)

### Active Anchor Registry

- **ref-alfsen-shultz-2003:** Alfsen, Shultz -- Geometry of State Spaces of Operator Algebras (Birkhauser 2003)
  - Why it matters: CRITICAL -- defines the OUS / spectral order unit space / compressions framework Paper 5 §2-3 cite throughout; (B) outcome depends on page-level consultation
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite, page-level lookup

- **ref-paper5-frozen:** Paper 5 frozen JMP submission (git tag `paper5-jmp-submitted`, copy at `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex`)
  - Why it matters: CRITICAL -- §3.3 lines 508-528 contain the exact claim; §3.3 lines 483-562 the surrounding context; revisions will land in `main.tex`
  - Carry forward: planning, execution, verification, writing
  - Required action: read, cite

- **ref-vdw-sequential:** van de Wetering -- sequential product axioms S1-S7
  - Why it matters: S1 and S3 are the allowed primitives in Phase 1; the rest are downstream of §3.3 and PROHIBITED in Phase 1 proof
  - Carry forward: planning, execution
  - Required action: read, cite

- **ref-paper5-lean:** Paper 5 Lean formalization `~/repos/research/lean/Paper5/` (0 sorry, 16 axioms)
  - Why it matters: Phase 5 audit target -- each of 16 axioms must trace to a cited Alfsen-Shultz or vdW statement
  - Carry forward: execution (Phase 5), verification
  - Required action: read, audit

- **ref-gpd-v2-sp-phases:** Prior GPD v2.0 Phases 4-6 (Sequential Product on OUS)
  - Why it matters: May already have attempted the §3.3 claim; if yes and (A) achieved, promote; if yes and assumed, flag; if no, note that prior work did not address it
  - Carry forward: planning
  - Required action: read, check

### Carry-Forward Inputs

- Paper 5 submission JMP26-AR-00922 with Zenodo DOI 10.5281/zenodo.19342703 (submitted 2026-03-28)
- Paper 5 main.tex §3.3 lines 483-562 (subsection "The Corrected Product via Peirce Feedback")
- Paper 5 Lean formalization `~/repos/research/lean/Paper5/` (0 sorry, 16 axioms)
- Prior GPD v2.0 Phases 4-6 sequential product work (content unknown until Phase 1 checks)
- Zero "Bryan's intuition says X" shortcuts -- this milestone exists because intuition is insufficient

### Skeptical Review

- **Weakest anchor:** The §3.3 claim itself -- if Paper 5 spent 20 lines asserting it, it is not trivial, and the author cannot independently reconstruct it. Probability of outcome (C) is non-trivial.
- **Unvalidated assumptions:** That S1 + S3 + linearity are sufficient primitives (the whole question). That Alfsen-Shultz 2003 contains an implicit theorem covering this case. That the prior GPD v2.0 work either settled or assumed the claim -- neither has been verified.
- **Competing explanation:** §3.3's argument may be conflating "compressions preserve Peirce subspaces" with "a o (-) preserves Peirce subspaces" -- these are about different objects and one does not trivially imply the other.
- **Disconfirming observation (=outcome C):** A proof attempt succeeds but requires Jordan structure / EJA / sequential product formula one step earlier in the chain than §3.3 currently allows. This would force Paper 5 to either (i) move the Jordan-structure derivation earlier, (ii) state an explicit assumption, or (iii) find a genuinely pre-Jordan argument.
- **False progress to reject:** "Since the Peirce decomposition exists in any spectral OUS (Alfsen-Shultz), the sequential product respects it" -- decomposition of V != invariance of a o (-) under V; "Jordan structure gives it" -- circular; "It's obvious from compressions" -- compressions c_{p_i} are not the same object as b -> a o b.

### Open Contract Questions

- Does prior GPD v2.0 Phase 4-6 work contain a Phase 1 proof attempt, an assumption, or no engagement with the §3.3 claim?
- Do the allowed primitives (S1, S3, linearity, OUS structure) suffice, or is there a hidden dependency on the sequential product formula itself?
- If outcome is (B), does the Alfsen-Shultz statement require any additional hypothesis that must be verified in Paper 5's setting?
- Are the 16 Lean axioms a red flag for the logical chain (Phase 5), or straightforward Alfsen-Shultz/vdW restatements?

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

### Answered in v11.0

- [x] Does a C*-observer's sequential product (C-linear Luders composition) extend the measurement algebra Cl(9,0) on V_{1/2} to Cl(9,C)? -- **YES.** C-linear closure proved by dimension counting. Gap C theorem assembled: 7-step chain, L1-L9 zero regressions. -- v11.0

### Answered in v12.0

- [x] Does the C*-bottleneck projection pi_u: h_2(O) -> h_2(C) carry the right equivariance (Lorentz group inside stabilizer)? -- **YES (compact part).** V_0 stabilizer = so(3) x so(6), pi_u equivariant. so(3) = rotation subalgebra. Boosts absent from compact Spin(9); require complexification. -- v12.0
- [x] Does the GST field content (27 = 1 + 16 + 10 under Peirce) match Paper 7's SM particle spectrum? -- **YES.** 16 SM fermions match Paper 7. V_0 splits 4(spacetime) + 6(internal). All quantum numbers verified. -- v12.0
- [x] Is det(X) uniquely forced as both the self-modeling density factor and the gravitational prepotential by F_4-invariance? -- **YES.** Springer 1962 uniqueness + F_4 = Aut(h_3(O)). Double duty non-circular. -- v12.0
- [x] Does the algebraic structure of h_3(O) force Einstein gravity? -- **YES (at low energies).** det(X) -> MESGT -> spin-2 + massless + universal coupling -> Weinberg 1964 -> -R/2. N=2 SUSY identification is ASSUMED, not derived. -- v12.0

### Active

- [ ] Does a o (-) preserve Peirce subspaces V_2(p_i) and V_1(p_i,p_j) from OUS primitives alone (S1 + S3 + linearity + compressions)? Outcome (A), (B), or (C). (v14.0 Phase 54)
- [ ] Does Alfsen-Shultz 2003 contain a theorem implying this preservation from OUS primitives, with precise chapter/section/theorem? (v14.0 Phase 54)
- [ ] Does prior GPD v2.0 Phase 4-6 work already contain this proof, assume the claim, or neither? (v14.0 Phase 54 prerequisite)
- [ ] Is the S4 facial structure lemma citable to Alfsen-Shultz or provable standalone? (v14.0 Phase 55, stub)
- [ ] Does W carry the product-form sequential product asserted by Thm 5.8 upper bound? (v14.0 Phase 56, stub)
- [ ] Does Phi have a single consistent interpretation across Paper 5 sections, or is the inert-wrapper usage equivocating? (v14.0 Phase 57, stub)
- [ ] Do each of the 16 axioms in the Paper 5 Lean formalization trace to a cited Alfsen-Shultz or van de Wetering statement? (v14.0 Phase 58, stub)
- [ ] Is the minimal composite assumption defensible against adversarial review, and does Paper 5 currently defend it adequately? (v14.0 Phase 59, stub)
- [ ] Can Todorov's F_4-Spin(9) intersection mechanism close gap G6 (so(6) -> G_SM) within self-modeling? (deferred)
- [ ] Can Boyle's triality mechanism address gap G7 (3 generations)? (deferred)

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

**v14.0-critical (Paper 5 revision):**

- Alfsen-Shultz (2003) -- Geometry of State Spaces of Operator Algebras (Birkhauser) -- OUS / compressions / Peirce decomposition; (B) citation target for Phase 54
- Paper 5 (this project, v2.0; JMP submission JMP26-AR-00922, Zenodo DOI 10.5281/zenodo.19342703) -- QM from self-modeling; the paper under revision
- van de Wetering -- sequential product axioms S1-S7 (S1 + S3 are the Phase 54 primitives)
- Paper 5 Lean formalization `~/repos/research/lean/Paper5/` -- 16 axioms for Phase 58 audit

**Carried forward from prior milestones (v1.0-v13.0):**

- Braunstein-Caves (1994), PRL 72 -- Fisher metric
- Hastings (2004/2006), CMP 265 -- Spectral gap implies exponential decay
- Nachtergaele-Sims (2006), CMP 265 -- Lieb-Robinson bounds
- von Ignatowsky (1911), Archiv Math. Phys. 17 -- Lorentz from isotropy + finite speed
- Paper 6 (this project, v3.0) -- GR from self-modeling
- Paper 7 (this project, v5.0/v11.0) -- chirality from h_3(O) via Cl(6), Gap C closure

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

_Last updated: 2026-04-16 after v14.0 milestone initialization (Paper 5 revision)_
