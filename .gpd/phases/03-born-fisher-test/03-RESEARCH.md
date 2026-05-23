# Phase 3: Born-Fisher Test - Research

**Researched:** 2026-03-16
**Domain:** Quantum information theory / foundations of quantum mechanics
**Confidence:** MEDIUM

## Summary

This phase implements a toy qubit model to numerically test the Born-Fisher-Experiential Conjecture: that Born-rule distributions satisfy (or violate) I_vN(B;M) = S_vN(B)/2 in a bipartite quantum system after decoherence. The computation is self-contained -- it requires density matrix construction, von Neumann entropy, quantum mutual information, and comparison between Born-rule and non-Born probability assignments over pointer states.

A critical mathematical constraint shapes the entire approach: for pure bipartite states, I_vN(B;M) = 2*S_vN(B) always (the ratio is 2, not 0.5), making rho_Q negative and unphysical. The conjecture therefore ONLY applies in the decoherent (mixed-state) regime where the joint state is approximately diagonal in the pointer basis. This means the toy model must either (a) evolve a pure state under Lindblad dynamics and evaluate the ratio during/after decoherence, or (b) directly construct classical-quantum states (diagonal in the pointer basis) and compare Born vs non-Born weightings. Both approaches should be implemented; approach (b) is the minimal decisive test, while (a) provides the full dynamical picture described in the quantum-extension draft (Section 8).

**Primary recommendation:** Implement both a static diagonal-state test (fast, analytically tractable, gives immediate verdict on the half-saturation conjecture) and a Lindblad dynamics test (gives the full rho_Q(t) trajectory, pulse structure, and mu_Q integral). Use numpy/scipy for the core computation; QuTiP is optional but useful for cross-validation.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| quantum-extension/draft.md (Sections 3, 6, 8) | prior artifact | Defines rho_Q, states the conjecture, specifies the toy model setup | Read and implement Section 8 faithfully | plan / execution / verification |
| composite_self_model.py | prior artifact / baseline | Classical 16-state model with rho = I(B;M)*(1-I/H); provides baseline rho = 0.347, I*/H = 0.507 | Cross-check: decoherence limit of quantum model must reproduce classical behavior | execution / verification |
| three_state_chain.py | prior artifact / baseline | Three-state FW metastability verification | Pattern for numerical verification methodology | execution style |
| Baez-Dolan (2001) | definition | Groupoid cardinality motivating 1/|Aut(x)| weighting | Not directly used in qubit computation; cite in context | plan documentation |
| Converse Madelung (arXiv:2511.03552) | method/background | Fisher information uniqueness constrains what functionals can select Born-rule distributions | Cite as theoretical motivation; does not enter numerics | plan documentation |
| Valentini-Westman (2005) | background | H-theorem for relaxation to Born rule; defines "non-Born" distributions | Informs choice of non-Born test distributions | plan / execution |
| Reginatto (1998) | background | Quantum potential = (hbar^2/8m)*I_F; Fisher-Born connection | Theoretical context for why I = S/2 might single out Born rule | plan documentation |

**Missing or weak anchors:** No prior computation of I_vN(B;M)/S_vN(B) for any specific quantum state exists in the literature or project artifacts. This is genuinely novel territory for the specific numerical test. The analytical result I_vN = 2*S_vN for pure states is standard but its implications for the rho_Q functional have not been previously analyzed.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Entropy base | nats (natural logarithm) | bits (log2) | Project convention |
| Mutual information | I(B;M) = S(B) + S(M) - S(BM) | Holevo chi, classical MI | Project convention |
| Von Neumann entropy | S_vN(rho) = -Tr(rho ln rho) | S2 = -log Tr(rho^2) (Renyi) | Project convention |
| Experiential density | rho_Q = I_vN(B;M) * (1 - I_vN(B;M)/S_vN(B)) | -- | quantum-extension/draft.md |
| Density matrix convention | rho is positive semidefinite, Tr(rho) = 1 | -- | Standard |
| Qubit basis | Computational basis {|0>, |1>} as pointer states | -- | quantum-extension/draft.md Sec 8 |
| Born rule | p_k = |alpha_k|^2 where |psi> = sum alpha_k |k> | -- | Standard QM |

**CRITICAL: All equations and results below use these conventions. The entropy is in nats throughout. The classical code (composite_self_model.py) also uses nats, ensuring consistency.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| S_vN(rho) = -Tr(rho ln rho) | Von Neumann entropy | Nielsen-Chuang Ch.11 | Core computation |
| I_vN(B;M) = S_vN(rho_B) + S_vN(rho_M) - S_vN(rho_BM) | Quantum mutual information | Nielsen-Chuang Ch.11 | Core computation |
| rho_Q = I_vN(B;M) * (1 - I_vN(B;M)/S_vN(B)) | Quantum experiential density | quantum-extension/draft.md Sec 3 | The functional being tested |
| rho_B = Tr_M(rho_BM), rho_M = Tr_B(rho_BM) | Partial trace / reduced density matrices | Standard | Required for entropy computation |
| For pure |psi>_BM: S_vN(B) = S_vN(M), S_vN(BM) = 0 | Schmidt decomposition consequence | Standard | CRITICAL constraint (see below) |
| I_vN(B;M) = 2*S_vN(B) for pure bipartite states | Pure-state mutual information | Standard | KILLS naive pure-state approach |

### Critical Mathematical Fact: Pure States Cannot Be Used Directly

For any pure bipartite state |psi>_BM, the von Neumann entropy of the joint system is zero: S_vN(BM) = 0. Therefore:

    I_vN(B;M) = S_vN(B) + S_vN(M) - 0 = 2*S_vN(B)

This gives a ratio I_vN(B;M)/S_vN(B) = 2 for ALL non-product pure states. Substituting into rho_Q:

    rho_Q = 2*S_vN(B) * (1 - 2) = -2*S_vN(B) < 0

This is negative, which is unphysical. The experiential density functional rho_Q was designed for classical systems where 0 <= I(B;M) <= H(B) (mutual information cannot exceed marginal entropy). In quantum mechanics, I_vN(B;M) can exceed S_vN(B) due to entanglement -- in fact for pure states it always equals 2*S_vN(B).

**Consequence:** The entire test must operate in the decoherent/mixed-state regime where quantum correlations have decayed and I_vN(B;M) <= S_vN(B). This is consistent with the quantum-extension draft (Sections 3.2, 6.1) which restricts attention to the SBS (spectrum broadcast structure) regime.

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Eigenvalue decomposition of density matrices | Computes S_vN = -sum lambda_i ln lambda_i | Every entropy computation | numpy.linalg.eigh |
| Partial trace | Obtains reduced density matrices rho_B, rho_M from rho_BM | Every MI computation | Manual reshape+trace or QuTiP ptrace |
| Lindblad master equation integration | Evolves rho_BM(t) under decoherence + tracking interaction | Dynamical test (approach a) | scipy.integrate.solve_ivp on vectorized rho |
| Parametric sweep over initial states | Varies theta in cos(theta)|00>+sin(theta)|11> or varies {p_k} | Both approaches | numpy linspace |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| --- | --- | --- | --- | --- |
| Decoherent/pointer-basis approximation | Off-diagonal coherences << diagonal elements | t >> tau_D (decoherence time) | O(exp(-gamma*t)) | Full Lindblad dynamics |
| Diagonal state ansatz (approach b) | Coherences = 0 exactly | Fully decohered regime | Exact within the ansatz | Lindblad evolution (approach a) |
| Numerical eigenvalue cutoff | lambda_i < 1e-15 treated as 0 in S_vN | Always | O(1e-15 * |ln(1e-15)|) ~ 3e-14 nats | Exact symbolic computation |

## Standard Approaches

### Approach 1: Static Diagonal-State Test (RECOMMENDED as primary)

**What:** Directly construct the joint density matrix in the pointer basis as a classical-quantum state (diagonal in B), compute I_vN and S_vN, and evaluate the ratio for Born-rule vs non-Born weightings. No dynamics needed.

**Why standard:** This directly tests the half-saturation conjecture (I_vN = S_vN/2 at Born rule) without the complication of Lindblad dynamics. It is the minimal decisive test.

**Track record:** Classical analog already implemented in composite_self_model.py with Shannon entropy. This lifts the same computation to von Neumann entropy.

**Key steps:**

1. Define the pointer basis for a qubit body: {|0>, |1>}.
2. Parametrize the body state as a classical mixture: rho_B = p|0><0| + (1-p)|1><1|, where p is the probability of outcome 0. Born rule gives p = cos^2(theta) for some theta.
3. Define the model state conditioned on the body outcome. For a "tracking" model with accuracy alpha:
   - If B = 0: rho_M^(0) = alpha|0><0| + (1-alpha)|1><1|
   - If B = 1: rho_M^(1) = (1-alpha)|0><0| + alpha|1><1|
4. Construct the joint state: rho_BM = p * |0><0| tensor rho_M^(0) + (1-p) * |1><1| tensor rho_M^(1). This is a 4x4 matrix, diagonal in the pointer basis.
5. Compute S_vN(rho_B), S_vN(rho_M), S_vN(rho_BM), I_vN(B;M).
6. Evaluate ratio = I_vN(B;M) / S_vN(B).
7. Sweep over p from 0 to 1, holding alpha fixed. Check if the ratio depends on p (it should for the conjecture to be meaningful).
8. Compare: Born-rule p = cos^2(theta) for various theta, vs non-Born alternatives (p = cos^4(theta)/Z, p = |alpha|, p = uniform, etc.).

**Known difficulties at each step:**
- Step 3: The tracking accuracy alpha is a free parameter. Must sweep over alpha to find where I/S = 0.5.
- Step 5: When p is near 0 or 1, S_vN(B) approaches 0, making the ratio ill-defined. Use 0/0 = 0 convention (matching classical code).
- Step 7: For diagonal states, all entropies reduce to Shannon entropies of the eigenvalues. This means the quantum test with diagonal states is mathematically identical to the classical test. This is by design (decoherence limit) but means the "quantum" test is really a classical information theory computation dressed in density matrix language.

**IMPORTANT SUBTLETY:** For fully diagonal (classical) states, I_vN reduces to Shannon MI, and the ratio I/S depends on the tracking model (alpha), not on whether p follows the Born rule. The Born rule is about which p values arise from quantum mechanics (p = |alpha_k|^2), but in the diagonal-state test, p is just a free parameter. The distinction between "Born" and "non-Born" only becomes meaningful when we ask: "For a given quantum state |psi> = cos(theta)|0> + sin(theta)|1>, which p arises from measurement?" Born says p = cos^2(theta). A non-Born rule might say p = cos^4(theta)/Z or p = |cos(theta)|/Z.

### Approach 2: Lindblad Dynamics Test (COMPLEMENTARY)

**What:** Start from a pure entangled state, evolve under Lindblad dynamics with decoherence and tracking interaction, and monitor I_vN(B;M)/S_vN(B) and rho_Q(t) throughout the evolution.

**Why complementary:** Tests the full dynamical picture from the quantum-extension draft Section 8. Shows the pulse structure of rho_Q(t) during decoherence. Computes mu_Q = integral of rho_Q dt.

**Key steps:**

1. Set up Hilbert space H_B tensor H_M = C^2 tensor C^2.
2. Define initial state |psi> = cos(theta)|00> + sin(theta)|11> as rho_BM(0) = |psi><psi|.
3. Define Lindblad generator L with:
   - Decoherence: collapse operators that project onto pointer basis (dephasing channel)
   - Tracking: interaction Hamiltonian or dissipator that makes M track B
4. Integrate drho/dt = L[rho] using scipy.integrate.solve_ivp (vectorize rho as 16-component real vector).
5. At each time step, compute I_vN(B;M)(t), S_vN(B)(t), rho_Q(t).
6. Compute mu_Q(theta) = integral of rho_Q(t) dt for different theta.
7. Check: does mu_Q(theta) have a maximum? At what theta?

**When to switch:** If the static test (Approach 1) shows the ratio is trivially determined by alpha and independent of p (which it likely will for diagonal states), the Lindblad test becomes the primary test of the conjecture, since it probes the transient regime where the ratio evolves dynamically.

**Tradeoffs:** More complex to implement (Lindblad generator design, ODE integration), but gives richer physics. The challenge is designing a Lindblad generator that produces both decoherence and tracking.

### Anti-Patterns to Avoid

- **Using pure states to test the conjecture:** As shown above, pure bipartite states always give I_vN/S_vN = 2, making rho_Q negative. The conjecture is about the decoherent regime.
- **Confusing "non-Born" with "non-quantum":** A "non-Born" distribution is one where the measurement probabilities are NOT p_k = |<k|psi>|^2. It is still a valid probability distribution, just not the one quantum mechanics predicts. Think of Valentini's quantum non-equilibrium.
- **Expecting the ratio to depend on p for diagonal states:** For diagonal classical-quantum states with a fixed tracking model, the ratio I/S depends on the tracking accuracy alpha and the distribution p, but the half-saturation condition I = S/2 is a joint condition on both. The test must carefully disentangle these.
- **Neglecting the alpha parameter sweep:** The tracking accuracy alpha is as important as the Born-rule parameter theta. Must sweep both.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Pure-state MI identity | I_vN(B;M) = 2*S_vN(B) for pure |psi>_BM | Standard QIT (Schmidt decomposition) | Explains why pure states fail; cite and use as sanity check |
| Von Neumann entropy of qubit | S_vN = -p*ln(p) - (1-p)*ln(1-p) for diagonal rho | Standard | Direct formula for qubit reduced states |
| Classical rho for observer | rho = 0.347, I*/H = 0.507, peak at alpha ~ 0.498 | composite_self_model.py | Baseline: quantum model in decoherence limit must reproduce this pattern |
| Experiential density parabola | rho = I*(1 - I/H) peaks at I = H/2 with rho_max = H/4 | Ehrlich (2026) classical paper | The functional form being tested in the quantum regime |
| Quantum MI bounds | 0 <= I_vN(B;M) <= 2*min(S_vN(B), S_vN(M)) | Araki-Lieb inequality | Validation check on computed MI values |

**Key insight:** The classical composite_self_model.py already computes I(B;M)/H(B) for discrete Markov chains. The diagonal-state quantum test will reduce to the same Shannon entropy computation. The novelty is in the Lindblad dynamics test (Approach 2) and in the specific question of whether the Born-rule parameter theta maps to the half-saturation condition.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Binary entropy function h(p) | h(p) = -p*ln(p) - (1-p)*ln(1-p); max at p=0.5, value ln(2) | Standard | For qubit subsystems |
| Decoherence time formula | tau_D = tau_R * (lambda_dB/Delta_x)^2 | Joos-Zeh 1985 | Sets time scale for Lindblad simulation |
| Exponential information acquisition | I_vN(t) ~ S_vN(B)*(1-exp(-t/tau_D)) | quantum-extension/draft.md Sec 3.3 | Ansatz for Lindblad dynamics cross-check |
| rho_Q pulse peak | Peaks at t = tau_D*ln(2) with value S_vN(B)/4 | quantum-extension/draft.md Sec 3.3 | Validation target for Lindblad simulation |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| quantum-extension/draft.md Sec 8 | Ehrlich | 2026 | Specifies the exact toy model setup | Initial state, what to look for, extension plan |
| Valentini-Westman Proc. R. Soc. A 461, 253 | Valentini, Westman | 2005 | Defines subquantum H-theorem, "non-Born" relaxation | Concept of non-Born distributions; numerical relaxation methodology |
| arXiv:2511.03552 | (Converse Madelung) | 2025 | Fisher information uniqueness | Theoretical context only; does not enter computation |
| arXiv:1103.1589 | Towler, Russell, Valentini | 2012 | Timescales for Born-rule relaxation | Methodology for parametric non-Born tests |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| numpy | numpy.linalg.eigh | Eigenvalue decomposition for S_vN | Standard numerical linear algebra; eigenvalues of Hermitian matrices |
| numpy | numpy.kron | Tensor product of matrices | Constructs joint Hilbert space operators |
| scipy | scipy.integrate.solve_ivp | ODE integration for Lindblad dynamics | Standard adaptive Runge-Kutta; handles stiff systems with method='Radau' |
| matplotlib | pyplot | Visualization of rho_Q(t), mu_Q(theta), ratio sweeps | Standard plotting |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| QuTiP | Cross-validation of entropy/MI computations | Optional: use entropy_vn, entropy_mutual, ptrace to validate hand-written numpy code |
| sympy | Symbolic verification of analytical limits | Optional: verify h(cos^2(theta)) formulas symbolically |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| numpy eigenvalue decomposition | scipy.linalg.logm for matrix logarithm | logm computes -Tr(rho*logm(rho)) directly but is less numerically stable near zero eigenvalues; eigenvalue approach is safer |
| scipy solve_ivp for Lindblad | QuTiP mesolve | QuTiP is more feature-rich but adds a dependency; for a 4x4 system, raw scipy is simpler and sufficient |
| Hand-coded partial trace | QuTiP ptrace | QuTiP is cleaner for larger systems but 4x4 partial trace is trivial to implement manually |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| Diagonal-state test, full sweep over p and alpha | < 1 second | None (4x4 matrices, ~10^4 parameter points) | N/A |
| Lindblad dynamics, single trajectory | < 1 second | None (16-component ODE, ~1000 time steps) | N/A |
| Full parametric sweep (theta, alpha, gamma) | < 10 seconds | None | N/A |
| Extension to qutrits (9x9 matrices) | < 1 minute for full sweep | Slightly larger eigenvalue problems | Still trivial |

**Installation / Setup:**
```bash
# Core dependencies (likely already installed):
pip install numpy scipy matplotlib
# Optional cross-validation:
pip install qutip
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Tr(rho) = 1 | Density matrix normalization | assert abs(np.trace(rho) - 1) < 1e-12 | Passes for all constructed states |
| All eigenvalues >= 0 | Positive semidefiniteness | assert np.all(eigenvalues >= -1e-12) | Passes; clamp tiny negatives to 0 |
| I_vN(B;M) >= 0 | Non-negativity of MI | Check after computation | Always true (strong subadditivity) |
| I_vN(B;M) <= 2*min(S_vN(B), S_vN(M)) | Araki-Lieb bound | Check after computation | Must hold for all states |
| Pure state: I_vN = 2*S_vN(B) | Pure state identity | Compute for initial pure state before decoherence | Ratio should be exactly 2.0 |
| Product state: I_vN = 0 | No correlation | Compute for rho_B tensor rho_M | MI should be 0 within numerical precision |
| Maximally mixed body: S_vN(B) = ln(2) | Maximum qubit entropy | Set p = 0.5 | S_vN should equal ln(2) = 0.6931... nats |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Decoherence limit (t >> tau_D) | gamma*t >> 1 in Lindblad | Quantum state becomes diagonal; MI reduces to Shannon MI | quantum-extension/draft.md Sec 2.2 |
| Perfect tracking (alpha -> 1) | rho_M^(k) = |k><k| | I_vN(B;M) = S_vN(B); ratio = 1; rho_Q = 0 (right zero) | Classical analog: crystal system in composite_self_model.py |
| No tracking (alpha = 0.5 for qubit) | rho_M^(k) = I/2 for all k | I_vN(B;M) = 0; rho_Q = 0 (left zero) | Classical analog: thermostat system |
| Equal superposition (theta = pi/4) | p = 0.5 | S_vN(B) = ln(2); maximum body entropy | Standard |
| Product initial state (theta = 0) | p = 1 | S_vN(B) = 0; degenerate | Trivial |
| Classical observer baseline | alpha ~ 0.5, p ~ 0.5 | rho ~ 0.347, I*/H ~ 0.507 | composite_self_model.py |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| S_vN of maximally mixed qubit | Compute S_vN(I/2) | 1e-12 | ln(2) = 0.693147... nats |
| MI of Bell state |Phi+> = (|00>+|11>)/sqrt(2) | Compute I_vN for pure Bell state | 1e-12 | 2*ln(2) = 1.386294... nats |
| S_vN of Bell state reduced density matrix | Tr_M(|Phi+><Phi+|) | 1e-12 | ln(2) nats |
| Cross-check with QuTiP | entropy_vn, entropy_mutual on same state | 1e-10 | Agreement with numpy computation |
| Decoherence limit matches classical | Compare I_vN/S_vN after full decoherence with Shannon I/H | 1e-6 | Agreement |

### Red Flags During Computation

- **Negative eigenvalues of density matrix (beyond -1e-12):** Indicates a bug in state construction or Lindblad integration. Physical density matrices are positive semidefinite.
- **I_vN(B;M)/S_vN(B) > 1 for a mixed (non-pure) state:** Possible if significant entanglement remains. Not necessarily wrong, but means the state is not sufficiently decohered for the classical rho_Q functional to apply.
- **rho_Q < 0:** Indicates I_vN > S_vN (quantum discord/entanglement regime). Must restrict to decoherent regime.
- **Ratio independent of p for fixed alpha in diagonal test:** This is actually EXPECTED. For diagonal states with a fixed tracking model, the ratio I/S is a function of both p and alpha. If it happens to be constant in p, the half-saturation conjecture is trivially satisfied (or violated) for all distributions, Born or not, and the test is uninformative. This would be a significant negative result.
- **mu_Q(theta) is flat in theta for Lindblad test:** Would indicate the conjecture is false -- Born rule is not special for the experiential density functional.

## Common Pitfalls

### Pitfall 1: Testing Pure States

**What goes wrong:** Pure bipartite states always give I_vN/S_vN = 2 and rho_Q < 0.
**Why it happens:** Quantum MI can exceed marginal entropy due to entanglement. The rho_Q functional was designed for classical (decohered) correlations.
**How to avoid:** Only evaluate rho_Q for mixed states in the decoherent regime where I_vN <= S_vN(B).
**Warning signs:** Negative rho_Q values.
**Recovery:** Switch to diagonal-state construction or wait until Lindblad dynamics has produced sufficient decoherence.

### Pitfall 2: Confusing "Born vs non-Born" with "p = 0.5 vs p != 0.5"

**What goes wrong:** Testing whether the ratio equals 0.5 by varying p, but finding it depends only on alpha, not on the source of p.
**Why it happens:** In the diagonal-state test, p is just a number -- there is no wavefunction. The Born rule is about the MAP from wavefunctions to probabilities, not about any particular value of p.
**How to avoid:** Frame the test correctly. For each initial quantum state |psi> = cos(theta)|0> + sin(theta)|1>:
  - Born rule assigns p = cos^2(theta)
  - Non-Born rule assigns p = f(theta) for some other f
  - Compare rho_Q under p = cos^2(theta) vs p = f(theta) for the same |psi>
  The question is whether the Born-rule assignment produces a special value of rho_Q (peak? half-saturation?) compared to other assignments.
**Warning signs:** Finding the same ratio for all p values.
**Recovery:** Reframe: the interesting quantity is mu_Q(theta) from the Lindblad dynamics, not the static ratio for a single p.

### Pitfall 3: Eigenvalue Precision Near Zero

**What goes wrong:** Computing S_vN = -sum lambda_i * ln(lambda_i) when some lambda_i are numerically ~1e-16 (should be 0).
**Why it happens:** Finite precision arithmetic in eigenvalue decomposition.
**How to avoid:** Filter eigenvalues: set lambda_i = 0 if lambda_i < 1e-15 before computing entropy. Use convention 0*ln(0) = 0.
**Warning signs:** Large entropy values for states that should have low entropy.
**Recovery:** Increase cutoff threshold; verify with higher-precision arithmetic if needed.

### Pitfall 4: Lindblad Generator Design

**What goes wrong:** The Lindblad generator does not produce the intended physics (tracking + decoherence).
**Why it happens:** Designing Lindblad operators for a specific physical process (M tracks B) is non-trivial. Random choices may produce unphysical dynamics.
**How to avoid:** Start with well-known dephasing operators L = sqrt(gamma) * sigma_z for decoherence. For tracking, use a Hamiltonian coupling H_int = g * (sigma_x tensor sigma_x + sigma_y tensor sigma_y) that swaps information between B and M.
**Warning signs:** Trace not preserved; eigenvalues going negative; steady state not matching expected diagonal form.
**Recovery:** Verify CPTP properties at each time step; use QuTiP mesolve as cross-check.

### Pitfall 5: Hilbert Space Dimension

**What goes wrong:** Qubit (d=2) model is too small to be informative. Gleason's theorem requires d >= 3.
**Why it happens:** The qubit system has special properties (e.g., all states on the Bloch sphere are related by SU(2) rotations) that may make it atypical.
**How to avoid:** Plan for qutrit (d=3) extension from the start. Design code to accept arbitrary dimension d as a parameter.
**Warning signs:** Results that depend critically on d=2 symmetry properties.
**Recovery:** Extend to qutrits and check if results persist.

## Level of Rigor

**Required for this phase:** Numerical evidence with analytical cross-checks where possible.

**Justification:** This is a conjecture-testing phase. The goal is a clear numerical verdict (I_vN/S_vN = 0.5 or not for Born-rule distributions), not a proof. Numerical precision ~1e-12 is sufficient to distinguish between 0.5 and any other value.

**What this means concretely:**
- All density matrices must be verified positive semidefinite and trace-1
- All entropy/MI computations must agree with analytical formulas for known limits (Bell state, maximally mixed, product state) to 1e-12
- The verdict must be clear: either the ratio is 0.5 within numerical precision, or it demonstrably is not
- If the ratio is not 0.5, report the actual value and how it depends on parameters
- Cross-check with at least two independent implementations (numpy eigenvalues + QuTiP or symbolic)

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Gleason's theorem (1957) | Operational derivations (Chiribella et al. 2011) | ~2011 | Multiple axiomatic routes to Born rule exist; none use experiential density |
| Valentini H-theorem (1991) | Numerical relaxation studies (Towler et al. 2012, Colin-Struyve 2023) | ~2012 | Non-Born distributions relax to Born rule dynamically; defines what "non-Born" means |
| Classical MI only | Quantum MI (von Neumann) | Standard since ~1990s | The lift from Shannon to von Neumann is standard; applying it to experiential density is novel |

**Superseded approaches to avoid:**
- None directly relevant. The experiential density framework is novel, so there are no superseded methods to avoid. Standard quantum information tools (von Neumann entropy, partial trace, Lindblad dynamics) are current.

## Open Questions

1. **Is the diagonal-state test informative or trivial?**
   - What we know: For diagonal states, quantum MI reduces to Shannon MI. The ratio I/S depends on both p and alpha.
   - What's unclear: Whether the ratio at Born-rule p values is special in any way that non-Born p values are not.
   - Impact on this phase: If trivial, the Lindblad dynamics test becomes the primary test.
   - Recommendation: Implement both; the diagonal test takes minutes and gives immediate signal.

2. **What Lindblad generator produces "tracking" dynamics?**
   - What we know: Dephasing operators are standard. A swap-like Hamiltonian couples B and M.
   - What's unclear: The precise coupling that gives "observe-then-update" behavior (the quantum analog of the classical factorization condition).
   - Impact on this phase: Must be resolved early (CALC-01).
   - Recommendation: Start with simple dephasing + exchange Hamiltonian. Verify that the late-time state is approximately diagonal with the model tracking the body.

3. **Is the 2x2 qubit model sufficient?**
   - What we know: Gleason's theorem fails at d=2. Some quantum information results are atypical at d=2.
   - What's unclear: Whether the I_vN/S_vN ratio has special properties at d=2 that don't generalize.
   - Impact on this phase: May need qutrit extension.
   - Recommendation: Design code for arbitrary d from the start. Run d=2 first, extend to d=3 if results are ambiguous.

4. **Does the conjecture even make sense after the pure-state analysis?**
   - What we know: For pure states, rho_Q < 0. The conjecture is restricted to the decohered regime.
   - What's unclear: Whether the restriction to decohered states makes the conjecture trivial (since decohered states are effectively classical).
   - Impact on this phase: This is the central question. The test will answer it.
   - Recommendation: Proceed. Even a negative result (conjecture trivial or false) is a decisive and valid outcome per the project contract.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Diagonal-state test uninformative | Ratio independent of Born vs non-Born | Full Lindblad dynamics test (Approach 2) | ~2 hours additional implementation |
| Lindblad generator doesn't produce tracking | Wrong coupling design | Use QuTiP mesolve with known decoherence models | ~1 hour; may lose "tracking" physics |
| Qubit model too special | d=2 artifacts | Extend to qutrit (d=3) | ~1 hour; code designed for arbitrary d |
| I_vN/S_vN != 0.5 for any configuration | Conjecture is false | Report falsification as the result (valid per contract) | Zero -- this IS a valid outcome |

**Decision criteria:** If the diagonal-state test shows I/S is the same for Born and non-Born p values at all alpha, abandon the static approach after 1 hour and focus entirely on Lindblad dynamics. If the Lindblad dynamics shows mu_Q(theta) is flat or monotone in theta, the conjecture is falsified -- report this.

## Caveats and Alternatives

### Self-Critique

1. **Assumption that might be wrong:** The assumption that diagonal-state testing captures the conjecture. The conjecture's Section 6.3 ("half-saturation at Born rule") is stated for the decoherent regime, but it may require the full dynamical trajectory (transient regime during decoherence), not just the late-time diagonal state.

2. **Alternative dismissed too quickly:** Using the Holevo quantity (classically accessible information) instead of I_vN. The quantum-extension draft (Sec 3.2) flags discord as a problem and suggests the Holevo chi as an alternative. If I_vN gives anomalous results (e.g., rho_Q < 0 even for mixed states), switching to Holevo chi might save the conjecture. This should be noted as a contingency.

3. **Limitation understated:** The entire diagonal-state approach may be circular. If we're testing whether Born-rule probabilities are special by plugging them into a classical entropy formula, we may just be testing properties of the binary entropy function, not anything about quantum mechanics.

4. **Simpler method overlooked:** Before doing Lindblad dynamics, could test the conjecture by examining the rho_Q functional analytically. For a diagonal qubit state with body probability p and tracking accuracy alpha, both I(B;M) and H(B) have closed-form expressions. The condition I = H/2 can be solved analytically for alpha as a function of p, and then one can check whether the Born-rule value p = cos^2(theta) is special. This analytical approach should precede all numerical work.

5. **Specialist disagreement:** A quantum information theorist might argue that restricting rho_Q to the decoherent regime makes the quantum extension vacuous -- you're just computing classical quantities with quantum notation. The response (from the draft) is that the transient dynamics during decoherence is genuinely quantum, and mu_Q accumulates during this transient. But the diagonal-state test misses this transient entirely.

## Sources

### Primary (HIGH confidence)

- Nielsen, Chuang -- Quantum Computation and Quantum Information, Ch. 11 [von Neumann entropy, quantum mutual information, partial trace]
- Watrous -- The Theory of Quantum Information (2018) [density matrices, quantum channels, CPTP maps]
- Breuer, Petruccione -- The Theory of Open Quantum Systems (2002) [Lindblad master equation, decoherence]
- quantum-extension/draft.md [defines rho_Q, states conjecture, specifies toy model]
- composite_self_model.py [classical baseline code, rho = 0.347 benchmark]

### Secondary (MEDIUM confidence)

- Valentini, Westman (2005), Proc. R. Soc. A 461, 253 [concept of non-Born distributions, H-theorem]
- Towler, Russell, Valentini (2012), Proc. R. Soc. A 468, 990 [numerical Born-rule relaxation timescales]
- arXiv:2511.03552 [converse Madelung theorem, Fisher uniqueness -- theoretical context]
- QuTiP documentation (v5.1) [entropy_vn, entropy_mutual, ptrace, mesolve functions]

### Tertiary (LOW confidence)

- Colin, Struyve (2023), Found. Phys. 53, 73 [Nelson stochastic mechanics relaxation to Born rule -- tangential]

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH -- von Neumann entropy, quantum MI, partial trace are textbook material. The pure-state identity I = 2S is rigorous and well-known.
- Standard approaches: MEDIUM -- the diagonal-state test is straightforward but may be uninformative. The Lindblad dynamics test requires non-trivial generator design. The question of whether the test is informative is genuinely open.
- Computational tools: HIGH -- numpy/scipy are standard and well-tested for 4x4 matrix operations. No exotic tools needed.
- Validation strategies: HIGH -- multiple known limits, analytical formulas, and cross-checks available. The classical baseline provides a strong reference point.

**Research date:** 2026-03-16
**Valid until:** Indefinite (core quantum information theory is stable; computational tools change but numpy/scipy interface is stable)
