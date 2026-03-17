# Claims Extraction: Pass 1 (Reader)

**Manuscript:** papers/paper3-born-fisher/main.tex
**Title (in-document):** Falsification of the Born--Fisher--Experiential Conjecture in a Qubit Toy Model
**Author:** Bryan Ehrlich
**Review date:** 2026-03-16

---

## 1. Main Claim (one sentence)

The Born--Fisher--Experiential conjecture -- that Born-rule probability assignments are dynamically selected by the half-saturation condition of the quantum experiential density -- is cleanly falsified in a qubit toy model with exchange-plus-dephasing Lindblad dynamics, because the information ratio I_vN/S_vN(B) stays in [1,2] throughout evolution and never enters the regime where the experiential density is positive.

---

## 2. Summary of Claims

### CLM-001: Main Result (Falsification)
- **Type:** main_result
- **Text:** The Born--Fisher--Experiential conjecture is cleanly falsified for the qubit toy model class studied.
- **Location:** Abstract (lines 70-71), Sec 5.1 (lines 518-530), Sec 6 (lines 581-609)
- **Evidence:** Test A (static) + Test B (dynamic), 1900+ trajectories, d=2 and d=3

### CLM-002: Static Falsification (Test A)
- **Type:** method / sub-result
- **Text:** The half-saturation tracking accuracy alpha_half(p) varies with p (spread 0.069 for d=2), but Born-rule body probabilities are indistinguishable from non-Born alternatives at half saturation.
- **Location:** Sec 3.3 (lines 356-375), Test A verdict (lines 388-391)
- **Evidence:** 200x200 grid sweep, bisection root-finding, 4 probability rules compared, d=3 confirmation

### CLM-003: Dynamic Falsification (Test B)
- **Type:** method / sub-result
- **Text:** Under Lindblad evolution with exchange coupling and dephasing, rho_Q(t) <= 0 throughout the evolution for all 1900+ trajectories, making mu_Q identically zero with no dynamical selection mechanism.
- **Location:** Sec 4.2-4.4 (lines 418-467), Test B verdict (lines 464-467)
- **Evidence:** 1200 symmetric + 700 asymmetric trajectories, 3 d=3 spot checks

### CLM-004: Physical Mechanism
- **Type:** physical_interpretation
- **Text:** The exchange Hamiltonian is "too good" at tracking: it ensures I_vN >= S_vN(B) at all times, preventing the system from entering the under-correlated regime. The system transitions directly from over-correlated (entangled, r=2) to perfectly correlated (classical, r=1) without passing through under-correlation (r<1).
- **Location:** Sec 5 (lines 470-511)
- **Evidence:** Monotonic r(t) decay from 2 to 1 across all trajectories; analytical dephasing formula verified to 5e-11; late-time off-diagonal magnitude < 2e-9

### CLM-005: Well-Definedness of rho_Q
- **Type:** method (positive residual)
- **Text:** The experiential density functional rho_Q is well-defined and well-behaved, correctly identifying the parabolic peak structure (rho_Q_max = S_vN(B)/4 at r=1/2) in the static diagonal-state regime.
- **Location:** Sec 5.2 (lines 534-541)
- **Evidence:** Test A grid confirms peak to 0.002% accuracy

### CLM-006: Lipschitz Stability Unaffected
- **Type:** significance (scope preservation)
- **Text:** The Lipschitz stability of the classical experiential measure is unaffected by the quantum falsification.
- **Location:** Sec 5.2 (lines 543-548)
- **Evidence:** Assertion only; no new computation. References [Ehrlich2026b].

### CLM-007: Generality Beyond d=2
- **Type:** generality
- **Text:** The falsification is not an artifact of the qubit (d=2) Hilbert space; d=3 qutrit tests confirm the same qualitative behavior.
- **Location:** Sec 3.4 (lines 379-385), Sec 4.4 (lines 452-461)
- **Evidence:** d=3 static: spread 0.023, mean alpha_half=0.848. d=3 dynamic: 3 trajectories, max rho_Q = -9.6e-10.

### CLM-008: Novelty -- No Prior Variational Born-Rule Derivation via Observer Correlations
- **Type:** novelty
- **Text:** No existing Born-rule derivation programme (Gleason, operational, Valentini H-theorem) connects the Born rule to a variational principle acting on the observer's internal correlations.
- **Location:** Sec 1 (lines 79-88)
- **Evidence:** Literature assertion only. Cites Gleason, Chiribella, Valentini.

### CLM-009: Pure-State Negativity of rho_Q
- **Type:** method (structural)
- **Text:** For all entangled pure states, rho_Q < 0 because I_vN = 2*S_vN(B) > S_vN(B), a phenomenon with no classical analogue.
- **Location:** Sec 1, Eq. (3) (lines 121-132)
- **Evidence:** Analytical identity from Schmidt decomposition. Verified numerically.

### CLM-010: Future Directions
- **Type:** significance (future work)
- **Text:** Non-Markovian channels and amplitude damping remain open avenues for modified conjectures; the experiential density framework may find quantum application in a different variational principle.
- **Location:** Sec 5.3 (lines 553-578)
- **Evidence:** Speculation only. No computation.

---

## 3. Promised Deliverables vs. Actual Evidence

| Deliverable | Promised | Delivered | Status |
|---|---|---|---|
| Static sweep (200x200, d=2) | Sec 2.2, Sec 3.1 | test_a_static.py, test_a_results.json | Complete |
| alpha_half(p) extraction | Sec 2.2, Sec 3.2 | Bisection in test_a_static.py | Complete |
| Born vs non-Born comparison | Sec 3.3 | 4 rules compared, spreads reported | Complete |
| d=3 static check | Sec 3.4 | test_a_static.py step 4 | Complete |
| Lindblad integrator | Sec 2.3-2.4 | lindblad.py with RK4 | Complete |
| 1200 symmetric trajectories | Sec 4.2 | test_b_dynamics.py | Complete |
| 700 asymmetric trajectories | Sec 4.3 | test_b_dynamics.py | Complete |
| d=3 dynamic spot check | Sec 4.4 | 3 trajectories in test_b_dynamics.py | Complete |
| 10 QI sanity checks | App A.1 | quantum_info.py validation suite | Complete |
| 6 Lindblad validation checks | App A.2 | lindblad.py validation suite | Complete |
| RK4 convergence verification | Sec 2.4 | n=2000 vs n=4000, delta < 1e-15 | Complete |
| Physical mechanism explanation | Sec 5 | Analytical + numerical | Complete |
| Verdict figure | -- | figures/verdict_summary.pdf | Complete |

All promised deliverables are present and backed by code artifacts.

---

## 4. Overclaiming Flags

### FLAG-001: Title vs. Actual Scope [MINOR]
- **Issue:** The title uses "Falsification of the Born--Fisher--Experiential Conjecture" without qualification. The body text consistently says "for this model class" or "for the qubit toy model class studied here." The abstract is appropriately scoped (line 70: "The conjecture is cleanly falsified for this model class"). The in-document title "...in a Qubit Toy Model" is properly scoped.
- **Severity:** Minor. The title is already properly qualified with "in a Qubit Toy Model." No action needed.

### FLAG-002: "Cleanly falsified" language [MINOR]
- **Issue:** The phrase "cleanly falsified" appears in the abstract (line 70), Sec 5.1 (line 519), and Sec 6 (line 607). The word "cleanly" adds rhetorical emphasis but the evidence does support this characterization: the falsification is not borderline (mu_Q is exactly zero to 1e-15, not just small). The falsification is for one specific model class, not for the conjecture in general, and the paper says so.
- **Severity:** Minor. The claim is supported within its stated scope.

### FLAG-003: "No classical analogue" for quantum overcorrelation [MINOR]
- **Issue:** Line 130 states I_vN > S_vN(B) is "a phenomenon with no classical analogue." This is standard quantum information theory and is not an overclaim, but it could be stated more precisely: classically I(B;M) <= H(B) always holds; quantum mechanically I_vN(B;M) can exceed S_vN(B) for entangled states. The claim is correct.
- **Severity:** None. Standard fact.

### FLAG-004: Scope of "falsification" [MODERATE -- KEY CONCERN]
- **Issue:** The paper falsifies the conjecture for one specific class of quantum channels: Markovian Lindblad evolution with exchange Hamiltonian + dephasing. The paper acknowledges this (Sec 5.3, Sec 6), but the degree to which this model class is representative of the conjecture's intended scope is unclear. The conjecture (Eq. 6, lines 134-150) is stated without specifying a particular dynamics -- it says "dynamically selected" without naming the channel. The paper tests exactly one channel family and finds the channel is pathological (exchange Hamiltonian "too good" at tracking). A skeptical reader could argue this is less "the conjecture is falsified" and more "the tested channel is unsuitable for the conjecture."
- **Assessment:** The paper handles this appropriately in Sec 5 (physical mechanism) and Sec 5.3 (future directions), identifying the exchange Hamiltonian's perfect-tracking as the specific cause and suggesting non-Markovian alternatives. However, the framing in the abstract and conclusion could better distinguish between "the conjecture is falsified in general" vs. "the conjecture has no content for this channel class." The paper lands on the correct side of this distinction but the language leans slightly toward the stronger reading.
- **Recommendation:** The paper should either (a) add a sentence to the abstract clarifying that the falsification is channel-specific and driven by the exchange Hamiltonian's perfect tracking, or (b) explicitly acknowledge in the abstract that the conjecture might survive for other channel classes. The conclusion does this (line 607-609) but the abstract is slightly less careful.

### FLAG-005: Fisher Information Connection Never Demonstrated [MODERATE]
- **Issue:** The conjecture is called "Born--Fisher--Experiential" and the introduction mentions "The connection to Fisher information arises through the Baez-Dolan groupoid cardinality" (lines 155-158). However, no Fisher information computation appears anywhere in the paper. The "Fisher" component of the conjecture's name is introduced but never operationalized or tested. The paper tests the experiential density part, not the Fisher information part.
- **Assessment:** The paper does not explicitly promise to test the Fisher information connection, and the name appears to be inherited from the conjecture's name in the parent framework. But the title and framing create an expectation that Fisher information plays a role, and it does not appear at all. This is a naming/framing issue rather than an evidence gap, since the conjecture as stated (Eq. 6) is purely about the experiential density. Still, a reader coming to the paper for Fisher information content will find nothing.
- **Recommendation:** Either explain why Fisher information is in the name but not in the test, or drop "Fisher" from the paper's treatment and note this explicitly.

### FLAG-006: Lipschitz Stability Claim Unsubstantiated [MINOR]
- **Issue:** CLM-006 states that the Lipschitz stability of the classical measure is "unaffected" by the quantum falsification. This is asserted without argument or reference to why the quantum result would have threatened the classical result in the first place. It reads as defensive reassurance rather than a substantiated claim.
- **Severity:** Minor. It is a true statement (the classical result is a separate theorem about a separate quantity), but including it in the discussion of a quantum negative result is slightly misleading in that it implies the quantum work might have threatened the classical result, which it could not have.

---

## 5. Negative-Result Narrative Assessment

### Narrative Structure
The paper follows a competent negative-result structure:
1. State the conjecture precisely (Sec 1, Conjecture 1)
2. Describe the test methodology (Sec 2)
3. Report results (Sec 3-4), with clear verdicts at the end of each section
4. Explain the physical mechanism behind the negative result (Sec 5)
5. Identify what survives and what fails (Sec 5.1-5.2)
6. Suggest future directions (Sec 5.3)
7. Conclude with the negative result and its scope (Sec 6)

This is a textbook-quality negative result narrative. The paper does not try to salvage the conjecture, does not bury the negative finding, and does not inflate the importance of the positive side-results (CLM-005, CLM-006).

### Logical Flow
The logical chain is:
- Conjecture: mu_Q(theta) extremized at Born-rule theta
- Prerequisite: rho_Q(t) must be positive at some time for mu_Q to be nonzero
- Finding: rho_Q(t) <= 0 for all t in all tested trajectories
- Therefore: mu_Q = 0 identically, no selection mechanism exists
- Root cause: exchange Hamiltonian keeps I/S_B >= 1 at all times

This is airtight within the stated scope. The static test (Test A) provides independent falsification evidence from a complementary angle.

### Strength of Evidence
- **Numerical evidence:** Comprehensive. 1900+ trajectories, d=2 and d=3, symmetric and asymmetric channels, 16 validation checks.
- **Analytical evidence:** The I/S_B ratio trajectory is analytically derived for pure dephasing (Lindblad integrator matches to machine precision). The pure-state identity I = 2*S_B is rigorous.
- **Code quality:** Clean implementation, no external dependencies beyond numpy, all validation passing.

### Weaknesses
1. The model class tested is narrow: only exchange Hamiltonian with dephasing. The paper acknowledges this.
2. The negative result is, in a sense, "too clean" -- the experiential density never even gets to be tested as a selector because it is always non-positive. This means the paper falsifies the conjecture for a class where the conjecture had no chance, rather than finding a class where the conjecture could have worked but didn't.
3. The d=3 evidence is thin (only 3 dynamic trajectories and ~6 static points). "Not a d=2 artifact" is weakly supported but plausible.

### Overall Assessment
The paper is a well-executed negative result with appropriately scoped claims. The main risk is FLAG-004 (scope of falsification) and FLAG-005 (Fisher information absent from the test despite being in the name). Neither is severe enough to constitute a major revision requirement. The narrative is honest and the evidence is thorough within its scope.

**Recommendation ceiling:** minor_revision. The overclaiming is marginal and could be fixed with small wording changes. There are no structural problems with the claim-evidence chain.

---

## 6. Claim-Evidence Summary Table

| Claim ID | Type | Location | Evidence | Support Status | Overclaim? |
|---|---|---|---|---|---|
| CLM-001 | main_result | Abstract, Sec 5.1, Sec 6 | Tests A+B, 1900+ trajectories | Supported (within scope) | Minor (scope) |
| CLM-002 | sub-result | Sec 3.2-3.3 | 200x200 grid, 4 rules | Fully supported | None |
| CLM-003 | sub-result | Sec 4.2-4.4 | 1900+ trajectories | Fully supported | None |
| CLM-004 | physical_interpretation | Sec 5 | Analytical + numerical | Fully supported | None |
| CLM-005 | positive_residual | Sec 5.2 | Test A grid peak | Supported | None |
| CLM-006 | scope_preservation | Sec 5.2 | Assertion only | Weakly supported | Minor |
| CLM-007 | generality | Sec 3.4, 4.4 | d=3 (limited) | Partially supported | None |
| CLM-008 | novelty | Sec 1 | Literature assertion | Unclear (no lit check done here) | Deferred to Lit stage |
| CLM-009 | structural | Sec 1, Eq. 3 | Analytical + numerical | Fully supported | None |
| CLM-010 | future_work | Sec 5.3 | Speculation | N/A | N/A |

---

_Pass 1 complete. Handoff to specialist reviewers._
