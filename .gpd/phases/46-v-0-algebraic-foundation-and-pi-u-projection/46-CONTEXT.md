# Phase 46: V_0 Algebraic Foundation and pi_u Projection - Context

**Gathered:** 2026-04-11
**Status:** Ready for planning

<domain>
## Phase Boundary

Construct the explicit projection pi_u: h_2(O) -> h_2(C_u) = R^{3,1}, verify Minkowski signature via det_2, characterize the non-homomorphism failure Delta(A,B) = pi_u(A circ B) - pi_u(A) circ pi_u(B), and compute V_{1/2} x V_{1/2} -> V_0 Peirce product under pi_u.

Requirements: [ALGB-01, ALGB-04, ALGB-05]

</domain>

<contract_coverage>
## Contract Coverage

- **pi_u formula + signature proof:** Explicit pi_u matrix/map formula with det_2(pi_u(Y)) having signature (1,3), verified by eigenvalue computation. Gate deliverable for Phases 47 and 48.
- **Acceptance signal:** det(E_{11})=0, det(I_2)=1, signature (1,3) in (x0,x1,x2,x3) parametrization where x0=(a+d)/2, x3=(a-d)/2, x1=Re(b), x2=<Im(b),u>.
- **False progress to reject:** Claiming R^{3,1} without explicit pi_u (h_2(O) = R^{9,1}, not R^{3,1}); treating V_0 circ V_0 within h_3(O) without verifying closure.

</contract_coverage>

<user_guidance>
## User Guidance To Preserve

- **User-stated observables:** Signature (1,3) on det_2(pi_u(Y)); Delta(A,B) algebraic structure; V_{1/2} x V_{1/2} -> V_0 image under pi_u.
- **User-stated deliverables:** (1) Explicit pi_u formula. (2) det_2 signature verification with benchmarks. (3) Delta(A,B) general formula (basis computation then closed form). (4) V_{1/2} x V_{1/2} -> V_0 product structure under pi_u.
- **Must-have references / prior outputs:** Baez 2002 (h_2(C) = R^{3,1}); Paper 7 Peirce decomposition (27 = 1+16+10); existing octonion multiplication code from earlier phases.
- **Stop / rethink conditions:** (1) If det_2(pi_u(Y)) doesn't give signature (1,3), check u choice and projection formula. (2) If Delta != 0 on h_2(C_u) restriction, projection formula is wrong. (3) If Delta = 0 on all of h_2(O), computation is wrong (contradicts octonion non-associativity). (4) If V_0 circ V_0 leaks into V_{1/2}, the Peirce decomposition setup has an error.

</user_guidance>

<decisions>
## Methodological Decisions

### pi_u Construction

- **Component-wise projection on off-diagonal octonions.** Formula: pi_u(a, b; b*, d) = (a, proj_u(b); proj_u(b)*, d) where proj_u(b) = Re(b) + <Im(b), u>u.
- Justification: simpler than Peirce-projector route, gives explicit formulas, and agreement with Peirce projector can be verified afterward.
- Diagonal entries (real) are untouched; projection kills 6 of 8 imaginary octonion directions, keeping only the u-component.
- Target h_2(C_u) is 4-dimensional with basis {diag(1,0), diag(0,1), off-diag with 1, off-diag with u}.
- det_2 = ad - |b|^2 with standard parametrization x0=(a+d)/2, x3=(a-d)/2, x1=Re(b), x2=<Im(b),u> gives signature (1,3).

### Jordan Product Scope

- **Use both intrinsic h_2(O) and inherited h_3(O) Peirce products.** Verify they agree on V_0 x V_0 (standard result for Peirce-0 spaces; verify explicitly for h_3(O) exceptional case).
- V_0 x V_0 should close within V_0 -- no leakage into V_{1/2} expected. Leakage is a red flag.
- For V_{1/2} x V_{1/2} -> V_0, use the h_3(O) Peirce product (physically relevant: fermion interactions producing spacetime vectors).
- Early falsifiers: (1) dim(V_0 circ V_0) != 10, (2) intrinsic and inherited products disagree on any basis pair.

### V_{1/2} Product Computation

- **Compute algebra first, defer physics interpretation to Phase 49.** Phase 46 establishes what the product IS. GST matching and Dirac bilinear identification are separate.
- One-line breadcrumb noting the connection to fermion bilinears is acceptable; no derivation or matching.
- Method for computing on V_{1/2} = O^2 basis elements: agent's discretion (full table vs. covariance reduction).
- **Limiting case:** Restricting to C_u^2 subset O^2 and projecting to h_2(C_u) should recover the standard 2x2 Hermitian outer product (known Dirac bilinear form).

### Verification Strategy

- **Purely symbolic/analytic proofs.** h_2(O) is 10-dimensional -- small enough for exact computation.
- Numerical sanity checks are fine as cross-validation but are not the proof.
- For Delta(A,B) and V_{1/2} product: compute on basis elements first (concrete), then extract general formula (abstract). Basis results serve as verification of the formula.
- Check ordering: (1) signature first (cheapest), (2) Peirce closure, (3) Delta(A,B), (4) V_{1/2} product. If (1) or (2) fail, stop before investing in (3) and (4).

### Agent's Discretion

- Choice of basis for V_{1/2} = O^2 (standard octonion basis vs. Spin(9)-adapted)
- Whether to compute full 16x16 product table or use Spin(9) covariance reduction
- Level of intermediate algebra documentation
- Whether to verify pi_u agrees with Peirce projector (recommended but not required)

</decisions>

<assumptions>
## Physical Assumptions

- V_0 = h_2(O) is a Peirce-0 subalgebra of h_3(O) (standard Jordan algebra result) | If wrong: the entire Peirce decomposition from Paper 7 is compromised
- proj_u is well-defined for any u in S^6 (G_2 equivalence from v8.0) | If wrong: the choice of u matters physically, not just algebraically
- The C_u = span{1,u} subalgebra of O is isomorphic to C | If wrong: pi_u target is not h_2(C) and Baez identification fails
- Peirce multiplication rules {V_i, V_j} subset V_{|i-j|} + V_{min(i+j,2-i-j)} hold for h_3(O) | If wrong: product landing sectors are different, entire structure changes

</assumptions>

<limiting_cases>
## Expected Limiting Behaviors

- When all off-diagonal octonion entries are in C_u: pi_u should be the identity on h_2(C_u), Delta should vanish
- When off-diagonal entry is purely in Im(O) perpendicular to u: pi_u should kill it entirely, leaving diagonal matrix
- V_{1/2} restricted to C_u^2 under pi_u: should recover standard h_2(C) Hermitian outer product (Dirac bilinear)
- h_2(O) with all entries real: pi_u should be identity (real numbers are in every C_u)

</limiting_cases>

<anchor_registry>
## Active Anchor Registry

- Baez 2002 (h_2(K) = R^{dim(K)+1,1})
  - Why it matters: target signature prediction h_2(C) = R^{3,1}
  - Carry forward: planning, execution, verification
  - Required action: cite, compare

- Paper 7 Peirce decomposition (27 = 1+16+10)
  - Why it matters: defines V_0, V_{1/2}, V_1 sectors and their dimensions
  - Carry forward: planning, execution, verification
  - Required action: use, compare

- Existing octonion code (from earlier phases)
  - Why it matters: multiplication tables and Cl(9,0) gamma matrices already implemented
  - Carry forward: execution
  - Required action: reuse (not rebuild)

- Octonion convention: Fano e_1 e_2 = e_4 (matches Paper 7)
  - Why it matters: projection formula depends on consistent octonion multiplication
  - Carry forward: execution
  - Required action: use

- Complex structure: u = e_7 by default (any u in S^6 equivalent under G_2)
  - Why it matters: concrete choice needed for explicit computation
  - Carry forward: execution
  - Required action: use

</anchor_registry>

<skeptical_review>
## Skeptical Review

- **Weakest anchor:** The claim that V_0 circ V_0 closes within V_0 (standard but unverified for h_3(O) specifically). If the exceptional algebra behaves differently from generic Jordan algebras here, the whole product analysis changes.
- **Unvalidated assumptions:** proj_u(xy) structure for octonion products -- the non-associativity of O means the failure term could have unexpected structure beyond simple "lost components."
- **Competing explanation:** The (1,3) signature might require a different parametrization than the naive one; if the natural quadratic form on h_2(C_u) is not det_2 but some other invariant, the signature claim could be technically correct but misleadingly stated.
- **Disconfirming check:** Compute det_2(pi_u(Y)) for a generic Y with all 10 components nonzero. If the eigenvalues of the associated quadratic form are not {+,−,−,−}, stop immediately.
- **False progress to reject:** Getting signature (1,3) on a restricted subspace (e.g., diagonal matrices only) without checking the full 4-parameter family.

</skeptical_review>

<deferred>
## Deferred Ideas

None -- discussion stayed within phase scope.

</deferred>

---

_Phase: 46-v-0-algebraic-foundation-and-pi-u-projection_
_Context gathered: 2026-04-11_
