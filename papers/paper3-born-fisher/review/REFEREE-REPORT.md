---
reviewed: 2026-03-16T22:00:00Z
scope: manuscript
target_journal: unspecified (arXiv companion preferred; Foundations of Physics marginal)
recommendation: major_revision
confidence: high
major_issues: 4
minor_issues: 5
---

# Referee Report

**Scope:** Full manuscript review (Pass 6 final adjudication of 5-stage panel)
**Date:** 2026-03-16
**Target Journal:** Unspecified; assessed for Foundations of Physics (marginal fit) and arXiv companion (good fit)

## Summary

This paper tests the Born-Fisher-Experiential conjecture -- that Born-rule probability assignments are dynamically selected by the time-integrated quantum experiential density functional mu_Q(theta) -- using a qubit toy model with two complementary approaches. Test A performs a static sweep over diagonal body-model states on a 200x200 grid and finds that the half-saturation tracking accuracy varies with body probability but Born-rule distributions show no distinguished behavior. Test B integrates the Lindblad master equation (exchange Hamiltonian plus dephasing) for 1,900+ trajectories and finds that the experiential density rho_Q(t) is non-positive throughout the entire evolution for every tested parameter combination, making mu_Q identically zero. The conjecture is falsified for this model class.

The mathematics is sound. The Lindblad superoperator construction, RK4 integration, and quantum information calculations are correct and validated to extraordinary precision (trace preservation to 10^{-16}, positivity to 10^{-31}, fourth-order RK4 convergence confirmed). The physical mechanism -- the exchange Hamiltonian maintains I_vN >= S_vN(B) at all times, preventing the system from entering the under-correlated regime where rho_Q > 0 -- is analytically provable and numerically verified. One minor numerical error exists in the narrative (a factor-of-2 misquote of rho_Q for the pilot trajectory) that does not affect any conclusion.

The central problems are significance and literature context, not correctness. The conjecture being falsified is the author's own, unpublished, and without community uptake. The negative result, while cleanly executed, is not surprising once the pure-state constraint I_vN = 2*S_vN(B) and the exchange Hamiltonian's population-preserving structure are recognized. The literature positioning omits two major Born-rule derivation programmes (Deutsch-Wallace and Zurek envariance) that directly bear on the paper's novelty claim. The self-citation titles in the bibliography do not match the actual companion papers. These issues are fixable but require substantial revision, not just local edits.

## Panel Evidence

| Stage | Artifact | Assessment | Key blockers or concerns |
| ----- | -------- | ---------- | ------------------------ |
| Read | CLAIMS-EXTRACTION.md | Strong | Scope of "falsification" (FLAG-004); Fisher info absent despite name (FLAG-005) |
| Literature | LITERATURE-CONTEXT.md | Adequate | Missing Deutsch-Wallace/Zurek (LIT-001); wrong self-citation titles (LIT-002); Fisher/IIT uncited |
| Math | MATH-SOUNDNESS.md | Strong | One minor error: factor-of-2 in quoted rho_Q value (line 402) |
| Physics | PHYSICS-ASSESSMENT.md | Strong | Conjecture underspecified (PHYS-003); model class narrow (PHYS-007); structural negativity discussion thin |
| Significance | SIGNIFICANCE-ASSESSMENT.md | Adequate | Low external significance; conjecture has no community uptake; method not novel |

## Recommendation

**MAJOR REVISION**

The paper is mathematically correct, physically honest, and well-executed within its scope. The falsification is valid for the tested model class and the claims are appropriately proportionate to the evidence. These are genuine strengths that many papers lack.

However, four problems prevent a recommendation of minor_revision or accept:

1. **Significance for standalone publication is weak.** The conjecture being falsified has no external significance -- it was proposed by the author in unpublished companion work and has no community investment. A negative result on a self-posed conjecture in a minimal toy model is an internal research-program exercise, not a standalone contribution to the literature. This is the paper's fundamental publication challenge.

2. **Literature positioning has material gaps.** The novelty claim that no Born-rule derivation connects the rule to "a variational principle acting on the observer's internal correlations" is overstated without engaging the Deutsch-Wallace decision-theoretic programme and Zurek's envariance. Both involve observer-oriented reasoning about probability assignments. The self-citation titles are also incorrect.

3. **The negative result is analytically predictable.** The monotone decrease of r from 2 to 1 under exchange-plus-dephasing dynamics follows straightforwardly from the facts that (a) the initial state lies in the {|00>, |11>} subspace, (b) the exchange Hamiltonian annihilates |00> and |11>, and (c) dephasing preserves populations while destroying coherences. The 1,900+ trajectories confirm what an analytic argument could prove in a few lines. The paper would be substantially stronger if it proved an analytical theorem characterizing the class of Markovian channels for which r >= 1 throughout, rather than remaining purely numerical.

4. **The Fisher information component is phantom.** "Fisher" appears in the conjecture name and the paper title but no Fisher information computation, definition, or substantive connection appears anywhere. This creates a misleading expectation for readers.

The path to publication requires either (a) folding this material into a comprehensive paper that presents the full experiential measure framework (positive and negative results together), (b) strengthening the paper with an analytical no-go theorem for Markovian channels, or (c) substantially reframing the contribution to focus on the structural insight about quantum mutual information dynamics rather than the conjecture falsification per se.

## Evaluation

### Strengths

1. **Intellectual honesty.** The author formulates a conjecture, tests it rigorously, and reports its failure without attempting to salvage it. Self-falsification is rare and scientifically commendable.

2. **Thorough numerical execution.** 1,900+ Lindblad trajectories spanning symmetric dephasing, asymmetric dephasing, multiple coupling strengths, and qutrit extensions, with 16 validation checks passing to many orders of magnitude better than required. The result (mu_Q = 0 identically) is not marginal or fine-tuned.

3. **Clear physical mechanism.** Section 5 provides a correct and insightful explanation of why the conjecture fails: the exchange Hamiltonian maintains I_vN >= S_vN(B) at all times by rebuilding classical correlations as fast as dephasing destroys quantum ones, so the system transitions directly from over-correlated (r=2) to perfectly correlated (r=1) without passing through under-correlation (r<1). This is the structural insight that deserves emphasis.

4. **Correct identification of the pure-state constraint.** Equation (4) -- that rho_Q = -2*S_vN(B) < 0 for all entangled pure states because I_vN = 2*S_vN(B) -- is the single most important physical fact in the paper. It reveals that the quantum extension of the experiential density behaves qualitatively differently from its classical ancestor because quantum mutual information can exceed the marginal entropy.

5. **Proportionate claims.** The paper consistently qualifies the falsification as applying to "this model class" and explicitly identifies open avenues (non-Markovian channels, amplitude damping, weak coupling, higher dimensions).

### Major Issues

#### Issue 1: Insufficient standalone significance for journal publication

**ID:** REF-001
**Dimension:** significance
**Severity:** Major revision required
**Location:** Entire manuscript framing; Abstract (lines 46-74); Discussion (Sec 5); Conclusion (Sec 6)

**Description:** The Born-Fisher-Experiential conjecture is the author's own hypothesis, introduced in unpublished companion work, without any community uptake, citation history, or established significance. Falsifying a self-posed conjecture in a minimal toy model with one specific Hamiltonian class is an internal research-program exercise. The negative result does not constrain any well-known open problem, does not resolve any existing controversy, and does not provide results that illuminate any research programme beyond the author's own.

**Quoted claim:** "The conjecture is cleanly falsified for this model class" (abstract, line 70; conclusion, line 607).

**Missing evidence:** Any indication that the broader community has a stake in the conjecture's truth or falsity. Any connection to an existing open question beyond the author's framework. A general theorem or characterization (not just numerical evidence) that would have independent mathematical interest.

**Impact:** The paper is technically correct but scientifically insufficient for standalone publication in most peer-reviewed venues. The significance assessment (Pass 4) rates this as "low external significance" with venue fit marginal for Foundations of Physics and poor for PRL/PRA.

**Suggested fix:** Three options (not mutually exclusive):
(a) Merge this material into a comprehensive paper presenting the full experiential measure framework, where the negative result is one section alongside the positive results from Papers 1 and 2.
(b) Prove an analytical theorem characterizing the class of Markovian channels for which the information ratio r remains >= 1 throughout. This would elevate the contribution from "numerical observation in a toy model" to "structural result about quantum information dynamics."
(c) Reframe the paper around the positive insight -- the structural behavior of quantum mutual information under exchange-plus-dephasing dynamics -- rather than around the falsification of a self-posed conjecture.

#### Issue 2: Missing major Born-rule derivation programmes in literature

**ID:** REF-002
**Dimension:** literature_context
**Severity:** Major revision required
**Location:** Introduction, lines 83-88

**Description:** The paper claims (lines 86-88): "none connects the Born rule to a variational principle acting on the observer's internal correlations." This novelty framing omits two major programmes that involve observer-oriented reasoning about probability assignments in quantum mechanics:

- **Deutsch-Wallace decision theory** derives Born-rule probabilities from decision-theoretic (observer-rational) constraints on an agent's preferences. This is a variational/optimization argument on the observer's probability assignments.
- **Zurek's envariance / quantum Darwinism** derives Born-rule probabilities from entanglement symmetries between system and environment, where the environment plays a role structurally analogous to the "model" subsystem.

The omission is not a mere citation gap -- it materially weakens the novelty claim that motivates the paper.

**Quoted claim:** "none connects the Born rule to a variational principle acting on the observer's internal correlations" (line 87-88).

**Missing evidence:** Engagement with Deutsch (1999), Wallace (2007, 2010), Zurek (2003, 2005, 2009) and an explanation of how the experiential density approach differs from these observer-oriented programmes.

**Impact:** The novelty framing in the introduction is overstated. Without engaging Deutsch-Wallace and Zurek, the reader cannot assess whether the experiential density approach offers anything categorically new.

**Suggested fix:** Add citations to Deutsch-Wallace and Zurek envariance. Revise the novelty claim to either: (a) narrow it to "no prior work uses a bipartite mutual-information functional as a variational selector for Born-rule probabilities," or (b) explain substantively how the experiential density approach differs from decision-theoretic and envariance programmes.

#### Issue 3: Incorrect self-citation titles in bibliography

**ID:** REF-003
**Dimension:** literature_context
**Severity:** Major revision required
**Location:** Bibliography entries, lines 728-739

**Description:** Both self-citations have titles that do not match the actual companion papers:

- **Ehrlich2026a** is listed as "Experiential density as a measure of meaningful complexity: Theorem A and the classical parabolic bound" but the actual Paper 1 title is "Boltzmann Brain Suppression via Experiential Measure: A Rigorous Proof from Metastability Theory."
- **Ehrlich2026b** is listed as "Lipschitz stability of the experiential density under perturbation of the body-model coupling" but the actual Paper 2 title is "Lipschitz Stability of the Experiential Density Functional."

**Impact:** This is a bibliography integrity issue. Readers and referees cannot verify the cited works because the titles do not match. This must be corrected before any submission.

**Suggested fix:** Update both bibliography entries to match the actual manuscript titles.

#### Issue 4: Analytical proof absent -- the result relies entirely on numerical evidence

**ID:** REF-004
**Dimension:** completeness
**Severity:** Major revision required
**Location:** Section 5 (Physical Mechanism, lines 470-511)

**Description:** The paper demonstrates numerically that r(t) = I_vN/S_vN(B) monotonically decreases from 2 to 1 under exchange-plus-dephasing dynamics across 1,900+ trajectories. Section 5 gives a correct qualitative physical explanation. However, the paper never proves this analytically as a theorem.

The analytical proof is straightforward and would substantially strengthen the paper: for initial states in the {|00>, |11>} subspace, the exchange Hamiltonian annihilates both basis states, populations are preserved by both H and the dephasing channel, marginals are time-independent, and I_vN = 2*S_B - S_BM with S_BM increasing monotonically from 0 to S_B. This establishes r >= 1 at all times.

More valuable still would be a characterization of the class of Markovian channels for which r >= 1 throughout. This would transform the paper from a numerical exercise on one model class into a structural result about quantum mutual information dynamics.

**Impact:** Without an analytical proof, the paper's main result is a numerical observation, not a theorem. The numerical evidence is overwhelming for the tested model class, but the absence of an analytical argument limits the paper's contribution and prevents generalization.

**Suggested fix:** (a) State and prove analytically that r(t) >= 1 for all t under exchange-plus-dephasing dynamics with initial states of the form cos(theta)|00> + sin(theta)|11>. The proof follows from the observations already made in Section 5. (b) Ideally, characterize a broader class of Markovian channels for which this holds, using the structure of the Lindblad generators.

### Minor Issues

#### Issue 5: Factor-of-2 error in quoted rho_Q value

**ID:** REF-005
**Dimension:** correctness
**Severity:** Minor revision
**Location:** Section 4.1, line 402

**Description:** The paper states "giving r = 2 and rho_Q = -0.693 nats" for the pilot trajectory at theta = pi/4. Given I_vN = 2*ln(2) = 1.386 nats and S_vN(B) = ln(2) = 0.693 nats, the correct value is rho_Q = I*(1 - I/S_B) = 1.386*(1-2) = -1.386 nats. The reported value -0.693 = -ln(2) = -S_B is wrong by a factor of 2. The code computes the correct value; this is a narrative typo.

**Suggested fix:** Change "-0.693 nats" to "-1.386 nats" on line 402.

#### Issue 6: Fisher information invoked in name but absent from paper

**ID:** REF-006
**Dimension:** clarity
**Severity:** Minor revision
**Location:** Title (line 37), Introduction (lines 155-158)

**Description:** "Fisher" appears in the conjecture name and the introduction mentions "the connection to Fisher information arises through the Baez-Dolan groupoid cardinality." However, no Fisher information computation, definition, or derivation appears anywhere in the paper. The connection is asserted in one sentence and attributed to the companion work. Readers expecting Fisher information content (especially those familiar with Frieden's programme on physics from Fisher information variational principles) will find nothing.

**Suggested fix:** Either (a) add 2-3 sentences explaining the Fisher information connection and cite Frieden (1998), or (b) explicitly state that the Fisher component is developed in the companion work and is not tested in this paper.

#### Issue 7: No discussion of quantum discord

**ID:** REF-007
**Dimension:** completeness
**Severity:** Minor revision
**Location:** Section 1 (discussion of I_vN > S_B), Section 5

**Description:** The quantum mutual information I_vN includes both classical correlations and quantum discord. The ratio r > 1 in Test B is driven by the discord contribution, which has no classical analog. The paper correctly notes that I_vN can exceed S_B for entangled states but does not name discord as the mechanism. A brief mention would clarify the physics for readers in quantum information theory.

**Suggested fix:** Add one sentence noting that the excess mutual information (I_vN > S_B) for entangled states includes a quantum discord contribution, with a reference to Ollivier-Zurek (2001) or Henderson-Vedral (2001).

#### Issue 8: Structural negativity of rho_Q for pure states deserves more discussion

**ID:** REF-008
**Dimension:** completeness
**Severity:** Minor revision
**Location:** Section 5.2 (lines 534-548)

**Description:** The fact that rho_Q < 0 for all entangled pure states is a structural limitation of the quantum extension, not just a limitation of the specific conjecture. Any future quantum application of the experiential density must address this -- either by modifying the functional form (e.g., replacing I_vN with a quantity bounded by S_B, such as the Holevo quantity) or by restricting the domain to decohered states. The paper notes the negativity but does not discuss its implications for the broader framework.

**Suggested fix:** Add 2-3 sentences in Section 5.2 noting that the pure-state negativity is a structural property of the quantum extension and discussing what it implies for future attempts to define a quantum experiential density (e.g., alternative functionals or domain restrictions).

#### Issue 9: Missing comparison to integrated information theory

**ID:** REF-009
**Dimension:** literature_context
**Severity:** Minor revision
**Location:** Introduction (lines 93-102)

**Description:** The experiential density is a bipartite information-theoretic functional measuring "meaningful complexity." Tononi's integrated information theory (IIT) and its quantum extensions (Zanardi et al. 2018) are structurally parallel: both are bipartite quantum information functionals intended to measure meaningful internal structure. The paper does not cite or discuss this line of work. The comparison is relevant because quantum IIT faces analogous challenges when extending classical information measures to quantum states.

**Suggested fix:** Add a brief (2-3 sentence) comparison to IIT/QIIT in the introduction or discussion, noting the structural parallel and any differences.

### Suggestions

1. **Reframe for positive content.** The paper's strongest result is the structural insight that exchange-plus-dephasing dynamics produce a monotone transition from r=2 to r=1 without ever entering the under-correlated regime. This is a statement about quantum information flow under open dynamics that has independent interest. Reframing the paper around this positive insight (with the conjecture falsification as a consequence) would be more compelling than framing the paper as a negative result on a self-posed conjecture.

2. **Consider merging with companion papers.** The strongest publication strategy may be a single comprehensive paper presenting the experiential measure framework: Theorem A (positive), Lipschitz stability (positive), and the Born-Fisher test (negative, showing falsifiability and identifying the quantum boundary). A three-paper series on a single-author research program with no external citations to the framework risks appearing as academic vanity publishing.

3. **Add Masanes-Galley-Muller (2019) reference.** This is the most recent major Born-rule derivation (from other quantum postulates plus state estimation, Nature Communications 2019). Including it completes the landscape in the introduction.

4. **Explore amplitude damping in a brief appendix.** The paper identifies amplitude damping as a potential avenue for r < 1. Even a single pilot trajectory with amplitude damping showing qualitatively different behavior (r transiently dipping below 1) would substantially strengthen the paper by showing the falsification is model-specific and the experiential density is not generically trivial.

## Detailed Evaluation

### 1. Novelty: WEAK

The paper introduces no new methods, proves no new theorems, and the specific functional (rho_Q) is inherited from companion work. The novelty is limited to the application context: first numerical test of rho_Q under Lindblad dynamics and identification of the monotone-decrease mechanism. The conjecture being tested is self-posed and unpublished. The novelty framing in the introduction (CLM-008: no prior Born-rule derivation uses observer-correlation variational principles) is overstated without engaging Deutsch-Wallace and Zurek envariance.

### 2. Correctness: VERIFIED (one minor narrative error)

The math stage verified five key equations and found all sound. The superoperator construction (Eq. 14) matches the standard Lindblad vectorization identity. The pure-state constraint I_vN = 2*S_B is rigorous. The falsification logic (mu_Q = 0 because rho_Q <= 0 throughout) is valid. One minor error: line 402 quotes rho_Q = -0.693 nats for the pilot trajectory when the correct value is -1.386 nats (factor-of-2 typo in narrative; code computes correctly).

**Equations checked:**

| Equation | Location | Dimensional | Limits | Status |
| -------- | -------- | ----------- | ------ | ------ |
| rho_Q definition (Eq. 3) | Def. 1, line 111 | ok (nats) | I=0: rho_Q=0; I=S_B: rho_Q=0 | pass |
| Pure-state limit (Eq. 4) | line 126 | ok (nats) | Schmidt: I=2S_B, rho_Q=-2S_B | pass |
| Superoperator (Eq. 14) | line 299 | ok (1/time) | Matches Breuer-Petruccione | pass |
| Exchange Hamiltonian (Eq. 8) | line 262 | ok (energy) | 2g(|01><10|+|10><01|) verified | pass |
| Dephasing decay | line 506-508 | ok (1/time) | exp(-2*gamma_D*t) verified to 5e-11 | pass |

### 3. Clarity: GOOD

The paper is well-organized with clear section structure. The logical flow (conjecture -> method -> static test -> dynamic test -> mechanism -> discussion -> conclusion) is easy to follow. Test verdicts are clearly stated at the end of each section. The notation is consistent throughout. One clarity issue: the Fisher information connection is invoked but never developed, creating a gap between the paper's name and its content.

### 4. Completeness: GAPS

All promised deliverables (static sweep, Lindblad trajectories, qutrit checks, validation suites) are present and backed by code. The main gap is the absence of an analytical proof for r >= 1 under exchange-plus-dephasing dynamics -- the proof follows from observations already in the paper but is never stated as a theorem. The qutrit evidence is thin (3 dynamic spot checks, limited static points). The discussion of structural negativity of rho_Q for pure states and its implications for the broader framework is underdeveloped.

### 5. Significance: LOW

The conjecture has no external significance. The negative result is analytically predictable. The model class is minimal. The methodology is standard. The paper extracts no positive physics beyond the mechanism identification. Within the author's research program, the result is essential and honest. Outside it, the contribution is slight.

### 6. Reproducibility: FULLY REPRODUCIBLE

All computational parameters are stated (grid sizes, step counts, tolerances, dephasing rates, coupling strengths). The implementation uses only Python/NumPy. The code is described in sufficient detail. Validation checks pass to machine precision. A competent physicist could reproduce all results from the manuscript alone.

### 7. Literature Context: INCOMPLETE

The bibliography (9 entries) is too small. Two major Born-rule derivation programmes (Deutsch-Wallace, Zurek envariance) are omitted. Frieden's Fisher information programme is uncited despite Fisher being in the conjecture name. Integrated information theory (Tononi, Zanardi) is uncited despite structural parallels. Self-citation titles do not match actual companion papers.

### 8. Presentation Quality: NEEDS POLISHING

The manuscript is well-written and professionally formatted. The main presentation issues are: (a) the Fisher information gap between name and content, (b) the factor-of-2 typo in line 402, (c) the bibliography corrections needed. The validation appendix is thorough and well-structured.

### 9. Technical Soundness: SOUND

The Lindblad formalism is correctly implemented. The superoperator construction, RK4 integration, quantum information measures, and diagonal-state parametrization are all standard and verified. The exchange Hamiltonian structure is correct. The dephasing operators are appropriate. The falsification logic is valid.

### 10. Publishability: MAJOR REVISION

The paper is technically correct but faces significant challenges for standalone publication. The significance is too low for most venues. The literature context needs substantial repair. The contribution would be elevated by analytical results. The strongest path to publication is merging into a comprehensive paper or reframing around the positive structural insight.

## Physics Checklist

| Check | Status | Notes |
| ----- | ------ | ----- |
| Dimensional analysis | pass | All key equations checked (nats, 1/time) |
| Limiting cases | pass | I=0, I=S_B, pure state, alpha=1, alpha=1/2 all verified |
| Symmetry preservation | pass | I(p,alpha) = I(1-p,alpha) verified to 2e-16 |
| Conservation laws | pass | Trace preservation to 10^{-16} |
| Error bars present | pass (N/A) | Deterministic ODE; no statistical uncertainty. Numerical precision 10^{-15} |
| Approximations justified | pass | No approximations beyond numerical integration; RK4 convergence verified |
| Convergence demonstrated | pass | n=2000 vs n=4000 gives delta < 10^{-15} |
| Literature comparison | fail | Missing Deutsch-Wallace, Zurek, Frieden, IIT |
| Reproducible | pass | All parameters stated; Python/NumPy only |

---

### Actionable Items

```yaml
actionable_items:
  - id: "REF-001"
    finding: "Insufficient standalone significance for journal publication"
    severity: "major"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Reframe contribution or merge into comprehensive paper; add analytical theorem"
    estimated_effort: "large"
    blocks_publication: true
  - id: "REF-002"
    finding: "Missing Deutsch-Wallace and Zurek envariance in literature review"
    severity: "major"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Add citations and revise novelty claim in introduction (lines 83-88)"
    estimated_effort: "small"
    blocks_publication: true
  - id: "REF-003"
    finding: "Self-citation titles do not match actual companion papers"
    severity: "major"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Update Ehrlich2026a and Ehrlich2026b bibliography entries (lines 728-739)"
    estimated_effort: "trivial"
    blocks_publication: true
  - id: "REF-004"
    finding: "Missing analytical proof of r >= 1 for exchange-plus-dephasing dynamics"
    severity: "major"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Add a theorem in Section 5 proving r(t) >= 1 analytically; ideally characterize the channel class"
    estimated_effort: "medium"
    blocks_publication: true
  - id: "REF-005"
    finding: "Factor-of-2 error in quoted rho_Q value for pilot trajectory"
    severity: "minor"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Change rho_Q = -0.693 nats to rho_Q = -1.386 nats on line 402"
    estimated_effort: "trivial"
    blocks_publication: false
  - id: "REF-006"
    finding: "Fisher information invoked in name but absent from paper"
    severity: "minor"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Explain Fisher connection or clarify it is developed in companion work; cite Frieden"
    estimated_effort: "small"
    blocks_publication: false
  - id: "REF-007"
    finding: "No discussion of quantum discord as mechanism for I_vN > S_B"
    severity: "minor"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Add one sentence naming discord; cite Ollivier-Zurek (2001)"
    estimated_effort: "trivial"
    blocks_publication: false
  - id: "REF-008"
    finding: "Structural negativity of rho_Q for pure states inadequately discussed"
    severity: "minor"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Add 2-3 sentences in Section 5.2 on implications for quantum extension"
    estimated_effort: "small"
    blocks_publication: false
  - id: "REF-009"
    finding: "Missing comparison to integrated information theory"
    severity: "minor"
    specific_file: "papers/paper3-born-fisher/main.tex"
    specific_change: "Add brief comparison to IIT/QIIT in introduction or discussion"
    estimated_effort: "small"
    blocks_publication: false
```

### Confidence Self-Assessment

| Dimension | Confidence | Notes |
|-----------|-----------|-------|
| Correctness | HIGH | All five key equations verified; code logic confirmed by math stage |
| Novelty | HIGH | Literature gaps identified with specific references; confirmed by web-available sources |
| Significance | HIGH | The internal-vs-external significance distinction is clear from the paper itself |
| Completeness | HIGH | All promised deliverables present; gaps in analytical proof and discussion are clear |
| Reproducibility | HIGH | All parameters stated; Python/NumPy only; validation comprehensive |
| Literature context | HIGH | Missing references confirmed against known literature |
| Technical soundness | HIGH | Lindblad formalism, superoperator, RK4 all verified against standard references |
| Clarity | HIGH | Paper is well-organized; issues are specific and localized |
| Presentation | HIGH | Issues are minor and fixable |
| Publishability | MEDIUM | Depends on venue choice and whether the author pursues merger vs. standalone reframing |

---

_Reviewed: 2026-03-16T22:00:00Z_
_Reviewer: AI assistant (gpd-referee)_
_Disclaimer: This is an AI-generated mock referee report. It supplements but does not replace expert peer review._
