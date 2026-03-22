---
phase: 08-locality-formalization
verified: 2026-03-22T04:00:00Z
status: passed
score: 7/7 contract targets verified
consistency_score: 12/12 physics checks passed
independently_confirmed: 10/12 checks independently confirmed
confidence: high
gaps: []
comparison_verdicts:
  - subject_kind: claim
    subject_id: claim-lr-framework
    reference_id: ref-lieb-robinson
    comparison_kind: benchmark
    verdict: pass
    metric: "relative_error"
    threshold: "<= 0.01"
  - subject_kind: claim
    subject_id: claim-lr-velocity
    reference_id: ref-nachtergaele-sims-phase8
    comparison_kind: benchmark
    verdict: pass
    metric: "analytical_identity"
    threshold: "exact"
suggested_contract_checks:
  - check: "The physical postulate that basis independence of Luders product forces diagonal U(n) invariance of h_xy should be flagged as an assumption, not a theorem, in Paper 6"
    reason: "This is the load-bearing step in deriving h_xy = alpha*I + J*F. It is a physically motivated argument, not a mathematical derivation from the SP axioms alone."
    suggested_subject_kind: claim
    suggested_subject_id: claim-locality-mapping
    evidence_path: "derivations/08-hamiltonian-construction.md"
expert_verification:
  - check: "Verify that basis independence of Luders product rigorously constrains the coupling Hamiltonian to be diagonal U(n)-invariant, as opposed to being a plausible physical argument"
    expected: "Either a proof or an explicit acknowledgment that this is a physical postulate"
    domain: "operator algebras, quantum information"
    why_expert: "The step from 'SP map is U(n)xU(n)-equivariant' to 'coupling Hamiltonian is diagonal U(n)-invariant' involves a non-trivial conceptual leap that distinguishes symmetry of the dynamics generator from symmetry of the generated map"
---

# Phase 8 Verification: Locality Formalization

**Phase goal:** The self-modeling lattice is precisely defined as a quantum lattice system, with interactions encoding the B-M boundary coupling, and an effective causal structure established via Lieb-Robinson bounds.

**Verified:** 2026-03-22
**Status:** PASSED
**Confidence:** HIGH (10/12 checks independently confirmed by computation)

---

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-lattice-definition | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Lattice G=(V,E), A_x=M_n(C), quasi-local algebra, interaction Phi all correctly defined in Bratteli-Robinson framework |
| claim-locality-mapping | claim | VERIFIED | STRUCTURALLY PRESENT | SM-locality -> H-locality argument is logically complete; the "basis independence -> diagonal U(n) invariance" step is a physical postulate, not a mathematical theorem, but is clearly stated as such |
| claim-hamiltonian-construction | claim | VERIFIED | INDEPENDENTLY CONFIRMED | h_xy = alpha*I + J*F derived via Schur-Weyl duality from diagonal U(n) invariance; parameter count 16->2->1 confirmed numerically; SWAP identity verified; eigenvalue structure confirmed |
| claim-lr-framework | claim | VERIFIED | INDEPENDENTLY CONFIRMED | NS framework correctly instantiated; Heisenberg benchmark matches analytical result v_LR = 8eJ/(e-1) to machine precision; convolution constants verified by direct summation |
| claim-lr-velocity | claim | VERIFIED | INDEPENDENTLY CONFIRMED | v_LR computed for Z^1 (12.66J), Z^2 (80.08J), Z^3 (297.92J) with explicit C_LR, mu_LR; all values independently verified by formula evaluation |
| claim-paper5-compatibility | claim | VERIFIED | INDEPENDENTLY CONFIRMED | C1-C4 axioms verified with 25 random trials each (max error ~10^-16); product-form SP verified to 3.07e-16 relative error |
| claim-causal-structure | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Light cone verified on 8-site chain; all commutator norms within LR bound; wavefront propagation consistent with v_LR |

**Score: 7/7 contract targets verified.**

---

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| derivations/08-lattice-definition.md | Formal lattice definition | EXISTS, SUBSTANTIVE, INTEGRATED | 234 lines; contains Definitions 1-6, locality mapping Theorem 1, BR consistency table |
| derivations/08-hamiltonian-construction.md | Hamiltonian from SP constraints | EXISTS, SUBSTANTIVE, INTEGRATED | 255 lines; Schur-Weyl derivation, explicit n=2 form, parameter counting, eigenvalue analysis |
| derivations/08-lr-framework.md | NS LR bound framework | EXISTS, SUBSTANTIVE, INTEGRATED | 249 lines; Eqs (1)-(16) with F-function, C_a, Phi_a, v_LR formulas |
| derivations/08-lr-self-modeling.md | LR velocity for self-modeling H | EXISTS, SUBSTANTIVE, INTEGRATED | 291 lines; v_LR computation, Paper 5 C1-C4 verification, effective causal structure |
| code/self_modeling_hamiltonian.py | Numerical verification | EXISTS, SUBSTANTIVE, INTEGRATED | 500 lines; 9 tests, ALL PASS |
| code/lieb_robinson_benchmark.py | LR benchmark | EXISTS, SUBSTANTIVE, INTEGRATED | 420 lines; Heisenberg benchmark, all checks PASS |
| code/self_modeling_lr_velocity.py | LR velocity + Paper 5 compat | EXISTS, SUBSTANTIVE, INTEGRATED | 609 lines; LR velocity, C1-C4, product SP, light cone, ALL PASS |

---

## Computational Verification Details

### Spot-Check Results

| Expression | Test Point | Computed | Expected | Match |
|------------|-----------|----------|----------|-------|
| F = (1/2)(I+sigma.sigma) | Direct construction vs Pauli decomposition | 0.00e+00 error | Exact match | PASS |
| J*F - (J/2)*I - (J/2)*sigma.sigma | J=1 | 0.00e+00 | 0 | PASS |
| v_LR(a=1) for Z^1 | J=1, z=2, d=1 | 12.6558 | 8e/(e-1)=12.6558 | PASS |
| C_a(d=1, a=1) | coth formula | 1.163953 | 2/(e-1)=1.163953 | PASS |
| C_a(d=1, a=1) | direct summation (cutoff=100) | 1.163953 | Formula value | PASS (rel_err 3.82e-16) |
| v_LR(a=1) for Z^2 | J=1, z=4, d=2 | 80.0848 | Derivation claim | PASS |
| v_LR(a=1) for Z^3 | J=1, z=6, d=3 | 297.9171 | Derivation claim | PASS |
| ||F||_op for n=2,3,4 | Operator norm | 1.0 for all | 1.0 | PASS |
| SWAP structure F(c tensor d)F = d tensor c | 20 random trials | max error 1.39e-17 | 0 | PASS |
| Diagonal U(2) invariance of h=alpha*I+J*F | 100 random unitaries | max violation 2.44e-15 | 0 | PASS |
| Eigenvalues of F | Exact diag | [-1, 1, 1, 1] | [-1, 1, 1, 1] | PASS |
| Eigenvalues of (J/2)*sigma.sigma | Exact diag | [-1.5, 0.5, 0.5, 0.5] | [-3J/2, J/2, J/2, J/2] | PASS |
| Product-form SP | 25 random quadruples | max error 3.07e-16 | 0 | PASS |
| Full SWAP at t=pi/(2J) | Random operators | 1.14e-16 | 0 | PASS |

### Limiting Cases Re-Derived

| Limit | Parameter | Expression Limit | Expected | Agreement | Confidence |
|-------|-----------|-----------------|----------|-----------|------------|
| J -> 0 | J=0 | h_xy = 0, U(t) = I | No coupling, no dynamics | PASS | INDEPENDENTLY CONFIRMED |
| J -> 0 | J=0 | v_LR = 0 | No propagation | PASS | INDEPENDENTLY CONFIRMED |
| v_LR(a -> 0+) | a -> 0 | v_LR -> infinity | F-function too flat, bound trivial | PASS | INDEPENDENTLY CONFIRMED |
| v_LR(a -> infinity) | a -> inf | v_LR -> 0 | Cone shrinks, prefactor blows up | PASS | INDEPENDENTLY CONFIRMED |
| v_LR scaling | J -> 2J | v_LR(2J)/v_LR(J) = 2.000000 | Linear in J | PASS | INDEPENDENTLY CONFIRMED |
| v_LR(d) | d: 1,2,3 | v_LR increases | More pathways in higher d | PASS | INDEPENDENTLY CONFIRMED |

Limiting case derivations were performed by direct evaluation of the v_LR formula at the limiting parameter values, not by inspecting derivation text.

### Intermediate Result Spot-Check

The key intermediate result in the derivation is the Schur-Weyl duality step: diagonal U(n) invariance forces h_xy in span{I, F}.

**Independent verification:** Generated 5 random 4x4 Hermitian matrices, averaged each under 5000 random diagonal U(2) transformations. All averages projected onto span{I, F} with residuals 0.01-0.03 (consistent with finite-sample Monte Carlo error). Elements of span{I, F} verified to be exactly invariant (violations < 2.67e-15 over 100 random unitaries). This independently confirms that span{I, F} is the U(2)-invariant subspace of 4x4 Hermitian matrices.

### Dimensional Analysis Trace

| Equation | Location | LHS Dims | RHS Dims | Consistent |
|----------|----------|----------|----------|------------|
| h_xy = J*F | 08-hamiltonian-construction, Eq 08.1 | [energy] | [energy]*[1] = [energy] | YES |
| H_Lambda = sum h_xy | 08-lattice-definition, Def 6 | [energy] | sum of [energy] = [energy] | YES |
| e^{iHt} | 08-lattice-definition | [1] | exp([energy]*[time]) = exp([1]) = [1] | YES |
| ||Phi||_a = z*J*e^a | 08-lr-framework, Eq 11 | [energy] | [1]*[energy]*[1] = [energy] | YES |
| C_a = sum e^{-ar} | 08-lr-framework, Eq 7 | [1] | sum of [1] = [1] | YES |
| v_LR = 2*||Phi||_a*C_a/a | 08-lr-framework, Eq 5 | [energy] = [1/time] | [energy]*[1]/[1] = [energy] | YES |
| LR bound: ||[A(t),B]|| <= ... | 08-lr-framework, Eq 3 | [1] | [1]*[1]*[1]*[1] = [1] | YES |

With a_lat=1 and natural units: [velocity] = [distance/time] = [1/time] = [energy]. All dimensions consistent throughout.

---

## Physics Consistency

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | All 7 key equations traced; all consistent in natural units with a_lat=1 |
| 5.2 | Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | 12 spot-checks on key expressions, all match to machine precision |
| 5.3 | Limiting cases | PASS | INDEPENDENTLY CONFIRMED | 6 limiting cases independently evaluated and verified |
| 5.5 | Intermediate spot-check | PASS | INDEPENDENTLY CONFIRMED | Schur-Weyl invariant subspace verified by Monte Carlo averaging |
| 5.6 | Symmetry | PASS | INDEPENDENTLY CONFIRMED | Diagonal U(2) invariance verified over 100 random unitaries; exchange symmetry of SWAP verified |
| 5.7 | Conservation | PASS | INDEPENDENTLY CONFIRMED | Hermiticity of H verified (error 0.00e+00); unitarity of time evolution confirmed by full SWAP test |
| 5.8 | Math consistency | PASS | INDEPENDENTLY CONFIRMED | SWAP identity, eigenvalue structure, Pauli decomposition, commutator equivalence all verified |
| 5.9 | Convergence | PASS | INDEPENDENTLY CONFIRMED | Convolution constant sums converge to formula values (rel_err < 10^-12) |
| 5.10 | Literature agreement | PASS | INDEPENDENTLY CONFIRMED | NS formula reproduces 8eJ/(e-1); ratio to classical LR velocity = (e+1)/(e-1) = 1.164, matching known result |
| 5.11 | Physical plausibility | PASS | INDEPENDENTLY CONFIRMED | v_LR > 0 for J > 0; v_LR = 0 for J = 0; linear scaling; increases with z; light cone verified numerically |
| Gate A | Catastrophic cancellation | PASS | N/A | No cancellation: all expressions are sums/products of positive quantities |
| Gate C | Integration measure | N/A | N/A | No coordinate transformations in this phase |
| Gate D | Approximation validity | PASS | STRUCTURALLY PRESENT | Nearest-neighbor truncation: exact if self-modeling coupling is strictly nearest-neighbor (reasonable physical assumption). Exponential F-function: standard for finite-range interactions, no approximation. |
| Gate B | Analytical-numerical cross-validation | PASS | INDEPENDENTLY CONFIRMED | v_LR formula evaluated analytically and numerically match to machine precision; convolution constant formula vs direct summation match to 10^-12 |

---

## Forbidden Proxy Audit

| Proxy | Status | Evidence | Why it matters |
|-------|--------|----------|----------------|
| "Lattice defined without specifying how self-modeling constrains the coupling" | REJECTED | The derivation explicitly derives h_xy = alpha*I + J*F from SP constraints via Schur-Weyl duality, reducing 16 parameters to 1 | If the lattice were defined without connecting to self-modeling, the entire v3.0 chain would be disconnected from its premise |
| "Citing Lieb-Robinson bounds without computing v_LR for the specific Hamiltonian" | REJECTED | v_LR computed explicitly for h_xy = J*F: v_LR(a=1) = 12.66J on Z^1, with C_LR = 1.72, mu_LR = 1 | Without an explicit v_LR, the "effective causal structure" claim would be vacuous |

---

## Comparison Verdict Ledger

| Subject ID | Comparison kind | Verdict | Threshold | Notes |
|------------|----------------|---------|-----------|-------|
| claim-lr-framework | Heisenberg benchmark | PASS | v_LR matches 8eJ/(e-1) to machine precision | NS formula reproduces known analytical result |
| claim-lr-velocity | Self-modeling vs Heisenberg | PASS | Ratio = 1.0 (identical interaction) | Expected: self-modeling h_xy IS the Heisenberg model for n=2 |
| claim-lr-velocity | v_LR vs classical LR | PASS | NS bound is 16.4% above classical | Both are upper bounds; NS is looser but provides the computational framework |

---

## Discrepancies Found

None. All checks pass.

---

## Suggested Contract Checks

| Check | Why it matters | Where evidence should come from |
|-------|---------------|-------------------------------|
| Flag "basis independence -> diagonal U(n) invariance" as a physical postulate in Paper 6, not as a theorem derived from the SP axioms | This is the load-bearing step in the Hamiltonian derivation. Any h_xy in M_n(C) tensor M_n(C) satisfies the product-structure constraint, so the actual constraining power comes from this physical argument about basis independence, not from the SP formalism alone. The derivation acknowledges this (Section C.1), but Paper 6 must be explicit about it as an additional assumption beyond Paper 5. | derivations/08-hamiltonian-construction.md, Section A.5 |

---

## Requirements Coverage

| Requirement | Status | Evidence |
|-------------|--------|----------|
| LOCL-01: Define lattice with local coupling in BR framework | SATISFIED | G=(V,E), A_x=M_n(C), H=sum h_{xy} with h_{xy}=J*F derived from SP constraints; BR consistency table passes all 7 checks |
| LOCL-02: Establish LR bounds with finite v_LR | SATISFIED | v_LR = 8eJ/(e-1) on Z^1 with explicit C_LR=1.72, mu_LR=1; Heisenberg benchmark verified; light cone confirmed numerically on 8-site chain |

---

## Anti-Patterns Found

None. Specifically:
- No TODO/FIXME/placeholder comments in any derivation or code file
- No hardcoded values without justification
- No suppressed warnings
- No unused imports or functions
- All numerical values justified by derivation
- Convergence verified where applicable

---

## Expert Verification Required

| Check | Expected | Domain | Why Expert |
|-------|----------|--------|-----------|
| Is "basis independence -> diagonal U(n) invariance" a theorem or a postulate? | Either a rigorous proof or explicit acknowledgment | Operator algebras / quantum information | The step from U(n)xU(n) equivariance of the SP map to diagonal U(n) invariance of the coupling Hamiltonian involves a conceptual distinction between symmetry of a dynamical generator and symmetry of the generated map. A counterexample (like angular momentum operators being vectors under rotations despite the rotation group being a symmetry) shows this is non-trivial. The physical argument is compelling but not a proof. |

---

## Confidence Assessment

**Overall: HIGH**

The phase achieves all 5 success criteria from the ROADMAP:

1. **Lattice defined** -- G=(V,E), A_x=M_n(C), H=sum h_xy with h_xy encoding self-modeling coupling. INDEPENDENTLY CONFIRMED by checking BR framework axioms and running numerical verification.

2. **Locality mapping** -- Self-modeling locality maps onto Hamiltonian locality via Theorem 1, using C4 non-signaling and product-form SP. The argument is logically complete. STRUCTURALLY PRESENT because the "basis independence -> diagonal U(n) invariance" step is a physical argument, not a theorem. The derivation is transparent about this.

3. **v_LR computed with explicit constants** -- v_LR = 8eJ/(e-1) approximately 12.66J on Z^1, with C_LR = e-1 approximately 1.72, mu_LR = 1. Values for Z^2 and Z^3 also computed. INDEPENDENTLY CONFIRMED by evaluating the formula and matching the Heisenberg benchmark.

4. **Dimensional consistency** -- All equations traced: h_xy has [energy], v_LR has [energy] = [1/time] in natural units with a_lat=1. INDEPENDENTLY CONFIRMED.

5. **Paper 5 compatibility** -- C1-C4 axioms and product-form SP verified numerically with 25 random trials each, max errors ~10^-16. Local tomography dimension count dim(V_xy) = 16 = 4x4. INDEPENDENTLY CONFIRMED.

The one item rated STRUCTURALLY PRESENT (locality mapping) involves a physical argument that is clearly stated as such in the derivation. The derivation does not claim this is a mathematical theorem. This is appropriate for the formalism phase and should be flagged as an explicit assumption in Paper 6.

All numerical computations were executed with actual output; no claims are made without computational evidence. Three independent code files (500+420+609 = 1529 lines) all pass all tests.
