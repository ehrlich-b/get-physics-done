# Physics Assessment -- Pass 3

**Manuscript:** papers/paper3-born-fisher/main.tex
**Title:** Falsification of the Born--Fisher--Experiential Conjecture in a Qubit Toy Model
**Reviewer role:** Physical soundness (Stage 4)
**Date:** 2026-03-16

---

## 1. Physical Assumptions

### 1.1 The quantum experiential density functional

The quantum extension rho_Q = I_vN(B;M)(1 - I_vN/S_vN(B)) is obtained by formally replacing Shannon entropies with von Neumann entropies in the classical experiential density. This is a standard and well-defined mathematical operation. However, the physical interpretation of the resulting functional is weaker than in the classical case because:

**Finding PHYS-001 (minor):** The classical functional rho = I(1 - I/H) has a clear interpretation: it peaks when the model captures exactly half of the body's entropy, penalizing both triviality (I=0) and redundancy (I=H). In the quantum case, I_vN can exceed S_vN(B) by a factor of 2 for pure states. The paper acknowledges this at Eq. (5) and correctly restricts interpretation to the mixed-state regime where 0 < r < 1. This restriction is physically honest and appropriately stated.

**Finding PHYS-002 (minor):** The paper does not discuss quantum discord. The quantum mutual information I_vN includes both classical correlations and quantum discord. This means rho_Q conflates two physically distinct types of correlation. For the diagonal-state test (Test A), this is irrelevant because diagonal states have zero discord. For the Lindblad test (Test B), the distinction matters during the transient: the ratio r > 1 includes a discord contribution that has no classical analog. The paper implicitly acknowledges this by noting that the ratio exceeds 1 for entangled states, but does not name discord as the mechanism. This is a minor omission that does not affect the falsification verdict.

### 1.2 The Born-Fisher-Experiential Conjecture

**Finding PHYS-003 (major):** The conjecture (Conjecture 1, Eq. 6) is underspecified in a way that limits the strength of the falsification. The conjecture states that Born-rule probability assignments are "dynamically selected" by the condition that the time-integrated experiential density mu_Q(theta) is "extremised" at the Born-rule initial state. But it does not specify:

- Which dynamics (Lindblad, unitary, non-Markovian)?
- Which Hamiltonian or interaction model?
- What class of decoherence channels?
- Whether "extremised" means maximised, minimised, or merely a critical point.

The paper tests one specific dynamics (exchange Hamiltonian + dephasing) and finds mu_Q = 0 identically. This falsifies the conjecture for this model class, which the paper correctly states. But the conjecture itself is so loosely stated that it could survive by retreating to a different dynamics. The paper handles this honestly in the Discussion (Section 5.2, "What is not falsified") and future directions (Section 5.3), explicitly listing non-Markovian channels, amplitude damping, and weak coupling as open avenues. This is appropriate behavior for a falsification paper testing a self-posed conjecture.

### 1.3 The bipartite body-model structure

**Finding PHYS-004 (suggestion):** The paper treats "body" and "model" as abstract quantum subsystems with no physical motivation beyond the analogy with the classical experiential measure framework. In the classical case, the body represents a physical system being observed and the model represents the observer's internal state, connected by a factorization condition. In the quantum case, what physical system has this bipartite structure? The paper does not address this, though the parent framework paper (Ehrlich2026a) presumably does. For the purpose of this paper -- testing a specific mathematical conjecture -- the bipartite setup is well-defined and sufficient. But for readers not familiar with the parent framework, the physical motivation for the B-M decomposition is thin. This is a presentation issue, not a physics error.

### 1.4 The exchange Hamiltonian as a "tracking" interaction

**Finding PHYS-005 (major):** The exchange Hamiltonian H_int = g(sigma_x x sigma_x + sigma_y x sigma_y) is called a "tracking interaction" that drives the model to track the body. This physical claim is central to the paper's explanation of why the conjecture fails: the exchange coupling is "too good" at tracking, keeping I_vN >= S_vN(B) at all times and preventing the system from entering the under-correlated regime.

Is this physical characterization correct? The exchange Hamiltonian generates partial swaps between B and M. For the initial state cos(theta)|00> + sin(theta)|11>, the exchange Hamiltonian preserves the diagonal populations (since the initial state is already in the subspace spanned by |00> and |11>, which are invariant under the exchange), so the "tracking" interpretation is that the exchange coupling preserves the correlations that already exist. Combined with dephasing (which destroys off-diagonal coherences but preserves populations), the system settles into a classically correlated state where M tracks B perfectly.

This explanation is physically sound for the specific initial states tested. The exchange coupling does indeed maintain I_vN >= S_vN(B) throughout the evolution, and the analytical derivation in the verification document (ratio = 2 - h((1+exp(-2*gamma_D*t))/2)/ln(2), monotonically decreasing from 2 to 1) confirms this. The physical picture -- decoherence destroys quantum correlations while exchange rebuilds classical ones, with the system transitioning directly from over-correlated to perfectly-correlated -- is correct.

However, the claim that this makes the exchange Hamiltonian "too good" at tracking contains an important physical insight that deserves more emphasis: the result is not about the strength of the coupling g but about the structure of the interaction. Even at weak coupling (g = 0.1), the ratio stays in [1, 2]. This suggests the issue is structural, not parametric.

### 1.5 The pure-state negativity of rho_Q

**Finding PHYS-006 (supported):** The paper correctly identifies that rho_Q < 0 for all entangled pure states (Eq. 5) because I_vN = 2*S_vN(B). This is a direct consequence of the Schmidt decomposition and is a standard result in quantum information theory. The physical interpretation -- that quantum mutual information can exceed the marginal entropy due to entanglement, a phenomenon with no classical analog -- is correct.

This is the single most important physical fact in the paper. It means the quantum extension of the experiential density is not simply a "quantum version" of the classical functional; it behaves qualitatively differently because the quantum mutual information violates the classical bound I <= H(B). The paper deserves credit for identifying this clearly and not glossing over it.

## 2. Regime of Validity

### 2.1 Model class tested

**Finding PHYS-007 (major):** The paper tests only one class of Lindblad models: exchange Hamiltonian + dephasing (symmetric and asymmetric), with initial states of the form cos(theta)|00> + sin(theta)|11>. The falsification is valid for this model class but the paper's title -- "Falsification of the Born-Fisher-Experiential Conjecture in a Qubit Toy Model" -- is proportionate to this scope.

The key question for regime of validity is: could the conjecture hold in other quantum regimes not tested? The paper explicitly discusses this:

1. **Non-Markovian channels:** Could produce oscillations in I_vN(t) that temporarily reduce r below 1. This is a physically plausible scenario. Memory effects in non-Markovian dynamics can cause information backflow, temporarily reducing the mutual information below its steady-state value.

2. **Amplitude damping:** Unlike dephasing, amplitude damping changes populations of rho_B, potentially creating transient under-correlation. This is another physically plausible scenario. Amplitude damping destroys both coherences and populations, which could drive I_vN below S_vN(B) transiently.

3. **Weak/imperfect coupling:** The paper tested g from 0.1 to 2.0 but the exchange Hamiltonian always produces perfect tracking at late times (I -> S_B). A different coupling mechanism (e.g., one that introduces noise or mismatch into the tracking) could allow r < 1.

4. **Higher dimensions:** The d = 3 spot check confirms the same behavior. The paper correctly notes this but does not claim the result extends to all dimensions.

These four avenues are physically reasonable and honestly identified. The falsification is not overclaimed as universal.

### 2.2 Parameter coverage

The parameter coverage within the tested model class is thorough:

- 100 theta values spanning (0.05, pi/2 - 0.05)
- 3 dephasing rates spanning two orders of magnitude (0.1 to 10.0)
- 4 coupling strengths spanning an order and a half (0.1 to 2.0)
- 7 asymmetry ratios spanning two orders of magnitude (0.1 to 10.0)
- d = 2 primary with d = 3 spot checks

This gives 1900+ trajectories covering the parameter space without obvious gaps. The result (mu_Q = 0 identically for all parameters) is robust, not a marginal or fine-tuned outcome.

### 2.3 Numerical reliability

The Lindblad integrator is validated to extraordinary precision:
- Trace preservation to 10^{-16}
- Positivity to 10^{-31}
- Dephasing rate agreement to 5 x 10^{-11} relative error
- RK4 fourth-order convergence confirmed

These tolerances are many orders of magnitude better than needed for the physics conclusion (r >= 1 vs r < 1 is an O(1) distinction). The numerical results are trustworthy.

## 3. Interpretation Assessment

### 3.1 Test A interpretation

**Finding PHYS-008 (supported):** The Test A verdict -- that alpha_half(p) varies with p but Born-rule distributions show no special property -- is physically appropriate. The paper correctly identifies the fundamental issue: for diagonal states, all entropies reduce to Shannon entropies, and the ratio I/S depends on both p and alpha. The Born rule maps theta to p via p = cos^2(theta), but this is just a parameterization of p in [0, 1]; any other mapping theta -> p produces a different but equally unremarkable curve through the alpha_half(p) locus. The Born rule has no distinguished role in this static test because the static test does not probe the dynamics of how p arises from theta.

This interpretation is correct and avoids overstating the Test A result.

### 3.2 Test B interpretation

**Finding PHYS-009 (supported):** The Test B verdict -- mu_Q = 0 identically because the system never enters the under-correlated regime -- is physically clear and well-supported. The mechanism (exchange + dephasing transitions from over-correlated to perfectly-correlated without passing through under-correlated) is analytically proven and numerically confirmed. The interpretation is proportionate to the evidence.

### 3.3 The "Physical Mechanism" section (Section 4)

**Finding PHYS-010 (supported):** Section 4 provides a clear, correct physical explanation for why the falsification occurs. The key insight -- that the exchange Hamiltonian maintains I_vN >= S_vN(B) at all times by rebuilding classical correlations as fast as dephasing destroys quantum ones -- is supported by both analytical derivation and numerical evidence. The quantitative statement about off-diagonal decay (exp(-2*gamma_D*t)) is validated to relative error 5 x 10^{-11}.

The section correctly identifies this as a model-class-level result rather than a numerical accident, which is the physically important conclusion.

### 3.4 Implications for the broader framework

**Finding PHYS-011 (suggestion):** The paper states that "the experiential density functional rho_Q itself is well-defined and well-behaved" (Section 5.2). This is true for the classical regime (diagonal states), but the fact that rho_Q is negative for all entangled pure states represents a more fundamental issue: the quantum extension of the experiential density functional does not share the non-negativity property of its classical ancestor. This is a structural limitation of the extension, not just a limitation of the particular conjecture being tested.

The paper would benefit from a sentence in the Discussion explicitly noting that the negativity of rho_Q for pure states is a structural property that any future quantum extension of the experiential measure must address -- either by modifying the functional form (e.g., replacing I_vN with a quantity bounded by S_vN, such as the Holevo quantity), or by restricting the domain to decohered states.

## 4. Falsification Verdict Assessment

### 4.1 Is the falsification physically meaningful or a mathematical artifact?

The falsification is physically meaningful, not a mathematical artifact. The key physical fact is that quantum mutual information can exceed marginal entropy (I_vN > S_vN(B)) due to entanglement, which has no classical analog. This means:

1. For pure entangled states, rho_Q < 0 always. This is a structural fact about quantum information theory.
2. For the specific dynamics tested (exchange + dephasing), the system transitions directly from over-correlated to perfectly-correlated. This is a physical property of the dynamics, not a numerical accident.
3. The conjecture requires the system to pass through the under-correlated regime (r < 1) where rho_Q > 0. The tested dynamics do not permit this transition.

The falsification would be a mathematical artifact if it depended on numerical precision or a degenerate parameter choice. It does not: the result holds exactly (r >= 1 is analytically provable) for all parameter values tested.

### 4.2 Is the falsification verdict proportional to the evidence?

**Finding PHYS-012 (supported):** The paper claims "cleanly falsified for this model class" which is proportional to the evidence. It does not claim the conjecture is universally falsified or that no modified version could work. The abstract says "cleanly falsified for this model class" and the Discussion lists open avenues. This is honest and proportionate.

### 4.3 Scope of the falsification

The falsification has two parts:

1. **Static (Test A):** Born-rule distributions are not special at half-saturation in diagonal states. This is a clean negative result but with limited physical significance because diagonal states are effectively classical.

2. **Dynamic (Test B):** mu_Q = 0 identically because rho_Q is never positive during Lindblad evolution. This is the stronger result because it shows the functional has no opportunity to act as a selector in the first place.

The combination of both tests makes the falsification convincing: even in the regime where rho_Q can be positive (diagonal states), the Born rule is not special; and in the dynamical regime, rho_Q is never positive.

## 5. Quantum Formalism Correctness

### 5.1 Lindblad formalism

**Finding PHYS-013 (supported):** The Lindblad master equation (Eq. 8) is in standard form. The superoperator construction (Eq. 12) correctly implements the vectorization:

- Hamiltonian part: -i(I x H - H^T x I) for column-stacking convention. Verified correct in code (lindblad.py line 69).
- Dissipator: L_k^* x L_k - (1/2)(I x L_k^dag L_k) - (1/2)(L_k^dag L_k)^T x I. Verified correct in code (lines 77-83). The conjugation (L_k.conj() on line 77) is correct for the column-stacking convention.

The code implements L rho L^dag via (L_k^* kron L_k), which follows from vec(L rho L^dag) = (L^dag)^T kron L) vec(rho) = (L^* kron L) vec(rho). This is the standard result for column-stacking vectorization (see Breuer & Petruccione, or any Lindblad superoperator reference). Correct.

### 5.2 Exchange Hamiltonian

**Finding PHYS-014 (supported):** The exchange Hamiltonian H = g(sigma_x x sigma_x + sigma_y x sigma_y) = 2g(|01><10| + |10><01|) is a standard exchange (flip-flop) coupling that preserves the {|00>, |11>} subspace and acts nontrivially on {|01>, |10>}. For initial states in the {|00>, |11>} subspace (as all tested initial states are), the Hamiltonian commutes with the initial state's population distribution. This is why it preserves the diagonal correlations. Physically correct.

### 5.3 Dephasing collapse operator

**Finding PHYS-015 (supported):** The symmetric dephasing operator L = sqrt(gamma_D)(sigma_z x I) implements pointer-basis dephasing. Under this channel, the off-diagonal coherences of the joint state in the pointer basis decay as exp(-2*gamma_D*t), while diagonal populations are preserved. This is the standard qubit dephasing channel. The paper verifies the decay rate to relative error 5 x 10^{-11}. Correct.

The asymmetric collapse operators L_0 = sqrt(gamma_0)(|0><0| x I) and L_1 = sqrt(gamma_1)(|1><1| x I) implement projective dephasing with state-dependent rates. The dissipator is:

D[rho] = gamma_0(P_0 rho P_0 - (1/2){P_0, rho}) + gamma_1(P_1 rho P_1 - (1/2){P_1, rho})

where P_k = |k><k| x I. For gamma_0 = gamma_1 = gamma_D, this reduces to (gamma_D/2)(sigma_z x I) rho (sigma_z x I) + ..., which is not identical to the symmetric case but produces similar dephasing physics. The paper handles this correctly by specifying the asymmetric extension separately.

### 5.4 Quantum mutual information

**Finding PHYS-016 (supported):** I_vN(B;M) = S_vN(B) + S_vN(M) - S_vN(BM) is the standard definition. The paper correctly notes that this satisfies the Araki-Lieb bound 0 <= I_vN <= 2*min(S_B, S_M), verified for all computed states. The bound is saturated (I_vN = 2*S_B) for pure states, which is correctly identified and exploited throughout. All formulas and bounds are standard quantum information theory (Nielsen-Chuang Chapter 11).

### 5.5 Von Neumann entropy computation

The eigenvalue decomposition approach with cutoff eps = 10^{-15} is numerically sound for the matrix sizes involved (4x4 for qubits, 9x9 for qutrits). The stability verification across cutoff values (10^{-15}, 10^{-14}, 10^{-13}) showing agreement to 10^{-13} nats confirms the cutoff is not affecting the results. The convention 0*ln(0) = 0 is standard.

## 6. Overall Physics Confidence

**Confidence: HIGH**

The physical reasoning throughout the paper is sound. The key results are:

1. **Correctly identified:** The quantum mutual information exceeding marginal entropy for entangled states is the structural reason why rho_Q is negative -- a genuine quantum phenomenon with no classical analog.

2. **Correctly diagnosed:** The exchange Hamiltonian's "tracking" behavior (maintaining I_vN >= S_vN(B)) is the dynamical mechanism preventing the system from reaching the regime where rho_Q > 0.

3. **Correctly scoped:** The falsification is limited to the tested model class. The paper does not overclaim.

4. **Correctly implemented:** The Lindblad formalism, superoperator construction, and quantum information measures are all standard and verified.

**Strengths:**
- Honest falsification of the authors' own conjecture
- Clear physical mechanism identified and analytically verified
- Thorough parameter coverage (1900+ trajectories)
- Numerical validation far exceeding requirements
- Proportionate claims with open avenues clearly stated
- The pure-state negativity of rho_Q (Eq. 5) is an important physical insight correctly identified

**Weaknesses:**
- The conjecture being tested is underspecified (PHYS-003), limiting what the falsification proves
- No discussion of quantum discord (PHYS-002), which would clarify why I_vN > S_vN(B)
- The structural negativity of rho_Q for pure states (PHYS-011) deserves more discussion as a limitation of the quantum extension itself, not just of the specific conjecture

**No unsupported physical conclusions.** All physical claims in the paper are either directly established by the numerical results, analytically proven, or clearly marked as speculation (future directions).

## Summary of Findings

| ID | Severity | Category | Summary |
|----|----------|----------|---------|
| PHYS-001 | minor | interpretation | Classical vs quantum interpretation of rho_Q functional not fully developed |
| PHYS-002 | minor | omission | No discussion of quantum discord as mechanism for I > S_B |
| PHYS-003 | major | assumption | Conjecture is underspecified (which dynamics, which channels); falsification scope limited |
| PHYS-004 | suggestion | presentation | Physical motivation for body-model bipartite structure is thin |
| PHYS-005 | major | interpretation | Exchange Hamiltonian "tracking" characterization is correct but the structural (not parametric) nature could be emphasized more |
| PHYS-006 | supported | physics | Pure-state negativity of rho_Q correctly identified and interpreted |
| PHYS-007 | major | regime | Falsification valid for tested model class only; other quantum regimes untested |
| PHYS-008 | supported | interpretation | Test A interpretation is correct and appropriately scoped |
| PHYS-009 | supported | interpretation | Test B interpretation is correct and proportionate |
| PHYS-010 | supported | physics | Physical mechanism section is correct and well-supported |
| PHYS-011 | suggestion | interpretation | Structural negativity of rho_Q for pure states deserves more discussion as limitation of quantum extension |
| PHYS-012 | supported | claims | Falsification verdict is proportional to evidence |
| PHYS-013 | supported | formalism | Lindblad formalism correctly implemented |
| PHYS-014 | supported | formalism | Exchange Hamiltonian correctly implemented and physically appropriate |
| PHYS-015 | supported | formalism | Dephasing operators correctly implemented |
| PHYS-016 | supported | formalism | Quantum mutual information correctly computed |

## Recommendation Ceiling

**minor_revision**

Rationale: The physics is sound. The falsification is valid for the stated scope. The quantum formalism is correctly applied. The physical mechanism is correctly identified. The claims are proportionate to the evidence. The three major findings (PHYS-003, PHYS-005, PHYS-007) are about clarifying scope and emphasis rather than correcting errors. None of them undermine the paper's central conclusion. The suggestions (PHYS-004, PHYS-011) would improve the paper but are not required for correctness. The central physical story -- that the quantum extension of rho_Q is structurally negative for entangled states and the exchange Hamiltonian prevents the system from entering the positive regime -- is well-supported and clearly articulated.
