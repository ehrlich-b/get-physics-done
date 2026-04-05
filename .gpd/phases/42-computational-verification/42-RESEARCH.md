# Phase 42: Computational Verification - Research

**Researched:** 2026-04-04
**Domain:** Clifford algebra Cl(9,0) / Sequential product on indefinite operators / M_16(R) -> M_16(C) exit verification
**Confidence:** HIGH

## Summary

Phase 42 is a computational GO/NO-GO gate: verify that the sequential product sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for all 72 off-diagonal anticommuting Clifford generator pairs, that sqrt(T_a) T_a sqrt(T_a) = (1/4)*I for 9 diagonal pairs, and that the effect algebra E_a & E_b = (1/2)*E_a stays real as a control. This is a pure verification phase -- no new mathematics, no theoretical argument. The deliverable is a single Python script with both SymPy exact and NumPy numerical verification.

The computation is trivial in scale (16x16 matrices, sub-second runtime) but critical in scope: all 72+9+72 = 153 pairs must pass. The closed-form sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2*sqrt(2)) is exact and avoids eigendecomposition. All T_a entries are exactly +/-1/2 or 0, enabling exact rational/algebraic verification in SymPy alongside numerical NumPy checks.

The project-level COMPUTATIONAL.md already pre-verified all results during the research survey. Phase 42 reproduces these results in the project codebase with proper test structure, exhaustive pair coverage, and explicit imaginary-norm checks.

**Primary recommendation:** Write a single verification script using the closed-form sqrt formula. Use both SymPy (exact algebraic proof) and NumPy (numerical cross-check with explicit error bounds). Tolerance: Frobenius norm < 1e-14. Structure: iterate over all (a,b) pairs systematically, report per-pair errors, fail loudly on any violation.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| T_a matrices from v8.0 Phase 29 | prior artifact | The 9 Cl(9,0) generators in M_16(R) that are the inputs to all computations | use directly via `get_traceless_generators()` | Plan: every task; Execution: script imports |
| Cl(9,0) anticommutation {T_a,T_b} = (1/2)*delta_{ab}*I_16 | benchmark | Precondition that must be verified before sequential product computation | verify as prerequisite check | Plan: precondition task |
| Closed-form sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2*sqrt(2)) | method | The exact formula avoiding eigendecomposition; pre-verified in COMPUTATIONAL.md | implement and verify sqrt^2 = T_a | Plan: sqrt construction task |
| COMPUTATIONAL.md pre-verification results | prior artifact | Error bounds (< 5e-16) from research survey; Phase 42 must match or improve | compare against | Plan: validation |
| Phase 29 associative closure = M_16(R) | prior artifact | Confirms Cl(9,0) generators span full M_16(R) on R^16 | cite (do not re-derive) | Plan: context only |

**Missing or weak anchors:** None. All required inputs exist and have been verified in prior phases.

## Conventions

| Choice | Convention | Alternatives | Source |
| --- | --- | --- | --- |
| Clifford normalization | {T_a, T_b} = (1/2)*delta_{ab}*I_16 | {gamma_a, gamma_b} = 2*delta*I (related by T_a = gamma_a/2) | Phase 28/29, effective_hamiltonian.py |
| Unit system | Dimensionless | N/A | Algebraic computation |
| Sequential product | a & b = sqrt(a) b sqrt(a) | Luders product for effects only | Paper 5; Gudder-Greechie 2002 |
| Square root branch | Principal branch: sqrt(z) with Re(sqrt(z)) >= 0 | Negative branch gives -i instead of +i; existence of imaginary part is branch-independent | Standard complex analysis |
| Effect definition | E_a = (I + 2*T_a)/2 (spectral projection, eigenvalues 0 and 1) | Could use E_a = (I - 2*T_a)/2 for the other projection | Phase description |
| V_{1/2} basis | (x2_0,...,x2_7, x3_0,...,x3_7) | Could interleave | Phase 28 convention lock |
| T_a entry values | Exactly +/-1/2 or 0 (verified) | N/A | Computed from octonion Fano triples |

**CRITICAL: All equations and results below use {T_a, T_b} = (1/2)*delta_{ab}*I_16 normalization. The raw T_b matrices from compute_T_b_matrices() have non-uniform normalization; use get_traceless_generators() which returns the uniformly-normalized T_a.**

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| --- | --- | --- | --- |
| {T_a, T_b} = (1/2)*delta_{ab}*I_16 | Clifford anticommutation (Peirce normalization) | Phase 28/29 | Precondition check |
| T_a^2 = (1/4)*I_16 | Consequence of anticommutation | Direct | Implies eigenvalues +/-1/2 |
| sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2*sqrt(2)) | Closed-form principal square root | COMPUTATIONAL.md; derived from spectral decomposition | Core formula for all computations |
| sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b for a != b | Sequential product identity (off-diagonal) | COMPUTATIONAL.md; algebraic derivation | Primary verification target |
| sqrt(T_a) T_a sqrt(T_a) = (1/4)*I_16 | Sequential product identity (diagonal) | Direct: T_a commutes with sqrt(T_a), T_a^2 = (1/4)I | Secondary verification target |
| E_a = (I + 2*T_a)/2 | Spectral projection (effect) | Standard | Effect algebra input |
| E_a E_b E_a = (1/2)*E_a for a != b | Effect sequential product (stays real) | METHODS.md grade analysis | Control verification |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --- | --- | --- | --- |
| Closed-form matrix sqrt via spectral projections | Computes sqrt(T_a) exactly without eigendecomposition | All sequential product computations | Standard functional calculus |
| SymPy exact rational/algebraic arithmetic | Provides algebraic proof (not just numerical evidence) | Parallel verification alongside NumPy | SymPy docs |
| Frobenius norm error checking | Quantifies deviation from expected result | Every verification check | Standard linear algebra |
| Imaginary-part norm detection | Confirms exit from M_16(R) into M_16(C) | Off-diagonal sequential products | Trivial (np.linalg.norm of .imag) |

### Approximation Schemes

None. All computations are exact. SymPy provides algebraic proof; NumPy provides numerical verification to machine precision (float64, ~15 decimal digits). No approximations, series truncations, or iterative methods are involved.

## Standard Approaches

### Approach 1: Closed-Form Sqrt + Direct Matrix Multiplication (RECOMMENDED)

**What:** Use the closed-form formula sqrt(T_a) = ((1+i)I + (1-i)2T_a)/(2*sqrt(2)) and compute sequential products by direct matrix triple-product.

**Why standard:** The formula exploits the known eigenvalue structure (all +/-1/2) to avoid eigendecomposition entirely. It is exact in both SymPy and NumPy. The project-level COMPUTATIONAL.md already recommends this approach and pre-verified the results.

**Track record:** Pre-verified during v11.0 research survey (COMPUTATIONAL.md): all 72 off-diagonal pairs to < 5e-16 error. Phase 42 research verification (above) confirms: max error 2.23e-16 for off-diagonal, 2.23e-16 for diagonal, 0.00 for effects.

**Key steps:**

1. Load T_a via `get_traceless_generators()` (9 matrices, 16x16 real)
2. Verify preconditions: {T_a, T_b} = (1/2)*delta_{ab}*I_16 for all pairs
3. Compute sqrt(T_a) for all 9 generators using closed-form
4. Verify sqrt(T_a)^2 = T_a for all 9 (sanity check)
5. Compute sqrt(T_a) T_b sqrt(T_a) for all 81 (a,b) pairs
6. Check off-diagonal (72 pairs): result = (i/2)*T_b
7. Check diagonal (9 pairs): result = (1/4)*I_16
8. Check imaginary part nonzero for all 72 off-diagonal pairs
9. Compute E_a = (I + 2*T_a)/2 for all 9 generators
10. Verify E_a E_b E_a = (1/2)*E_a for all 72 off-diagonal effect pairs
11. Verify E_a E_b E_a is real for all 72 off-diagonal effect pairs

**Known difficulties at each step:**

- Step 1: Non-uniform normalization of raw T_b matrices. Use `get_traceless_generators()` which handles rescaling. Do NOT use `compute_T_b_matrices()` directly.
- Step 3: The formula involves complex arithmetic on real matrices. NumPy handles this transparently with dtype promotion to complex128.
- Step 6: The comparison must use Frobenius norm, not element-wise, to handle small floating-point deviations distributed across 256 entries.

### Approach 2: Eigendecomposition-Based Sqrt (FALLBACK)

**What:** Compute sqrt(T_a) via numpy.linalg.eigh eigendecomposition, applying sqrt to each eigenvalue independently (including sqrt(-1/2) = i/sqrt(2)).

**When to switch:** Only if the closed-form formula is suspected of a sign error or branch mismatch.

**Tradeoffs:** Slightly less numerically stable (eigendecomposition introduces O(epsilon) errors in eigenvectors), but provides an independent cross-check of the closed-form result.

### Anti-Patterns to Avoid

- **Using scipy.linalg.sqrtm:** Designed for general matrices via Schur decomposition. Overkill for known-spectrum matrices and may choose a different branch. The closed-form is simpler and exact.
- **Using the existing _matrix_sqrt from fisher_metric.py:** That implementation clips negative eigenvalues to zero (designed for PSD matrices). It will silently produce WRONG results for T_a.
- **Symbolic computation with abstract SymPy variables:** 16x16 matrices with symbolic entries would be catastrophically slow. Instead use exact numeric values (Rational(1,2), etc.) in SymPy Matrix objects.
- **Spot-checking a few pairs and declaring success:** The contract explicitly forbids partial verification. ALL 72 off-diagonal pairs, ALL 9 diagonal pairs, ALL 72 effect pairs must be checked.
- **Checking only the off-diagonal identity without checking the imaginary norm:** Success criterion 4 requires explicit confirmation that Im(sqrt(T_a) T_b sqrt(T_a)) != 0 for all 72 pairs.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| {T_a, T_b} = (1/2)*delta_{ab}*I_16 | Clifford anticommutation | Phase 28/29 | Precondition check only |
| T_a^2 = (1/4)*I_16 | From anticommutation | Phase 28 | Used in diagonal pair check |
| Eigenvalues of T_a are +/-1/2 (each with multiplicity 8) | Spectrum | Phase 29 | Justifies the closed-form sqrt |
| Associative closure of {T_a} = M_16(R) | dim = 256 | Phase 29, ALGV-03 | Do not re-verify; cite |
| omega = gamma_1...gamma_9 = +I_16 on V_{1/2} | Volume element | Phase 29 | Do not re-verify; cite |
| E_a = (I + 2*T_a)/2 is a projection (E_a^2 = E_a) | From T_a^2 = (1/4)I | Direct algebra | Justifies sqrt(E_a) = E_a |
| P_+ T_b P_+ = 0 and P_- T_b P_- = 0 for a != b | From anticommutativity of T_a, T_b | Algebraic derivation in METHODS.md | Underlies the (i/2)*T_b identity |
| Effect closure: products of real matrices are real | Standard linear algebra | Textbook | Justifies why effect algebra stays in M_16(R) |

**Key insight:** The algebraic derivation of sqrt(T_a) T_b sqrt(T_a) = (i/2)*T_b is a 5-line calculation using P_+ T_b P_- + P_- T_b P_+ = T_b and the cross-term structure. Phase 42 does NOT need to re-derive this; it needs to VERIFY it computationally for all pairs.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| T_a entries are exactly +/-1/2 or 0 | Enables exact SymPy verification via Rational(1,2) | Verified during this research | Always true (Fano triple construction) |
| SymPy 16x16 matrix multiplication takes < 0.1s per product | SymPy verification is feasible for all 153 pairs | Timed during this research | SymPy 1.14.0 |
| NumPy errors are < 5e-16 | Well within 1e-14 tolerance | Pre-verified in COMPUTATIONAL.md and re-verified here | NumPy 2.4.2, float64 |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| --- | --- | --- | --- | --- |
| Sequential products on effect algebras | Gudder & Greechie | 2002 | Defines sequential product a & b = sqrt(a) b sqrt(a) for effects | Definition only; we extend to indefinite operators |
| Sequential Product Spaces are Jordan Algebras | van de Wetering | 2019 | Classifies sequential product spaces | Not directly used in computation; background |
| Spin Geometry, Table I.4.3 | Lawson & Michelsohn | 1989 | Cl(9,0) = M_16(R) + M_16(R) classification | Confirms T_a generate M_16(R) on R^16 |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| NumPy | 2.4.2, numpy.linalg | Matrix multiplication, Frobenius norm, eigenvalue checks | Standard numerical linear algebra; already in codebase |
| SymPy | 1.14.0, sympy.Matrix | Exact algebraic verification with Rational and I | Provides proof-level certainty (zero error, not just < epsilon) |
| Python | 3.14.2 | Runtime | Already installed |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| effective_hamiltonian.get_traceless_generators() | Load uniformly-normalized T_a matrices | Entry point for all computation |
| octonion_algebra.compute_T_b_matrices() | Raw T_b matrices (non-uniform normalization) | Only if debugging normalization issues |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| SymPy exact verification | NumPy only | Loses proof-level certainty; adequate for numerical evidence but not for "verified algebraically" |
| Closed-form sqrt | scipy.linalg.sqrtm or eigendecomposition | Slower, may choose different branch, unnecessary complexity |
| Single script | Separate test file + code module | Over-engineering for a verification task with no reuse beyond this phase |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| 9 sqrt(T_a) computations (NumPy) | < 1 ms | None | N/A |
| 81 sequential products (NumPy) | < 10 ms | None | N/A |
| 72 effect products (NumPy) | < 10 ms | None | N/A |
| 81 sequential products (SymPy exact) | < 10s total | SymPy matrix multiply | Still trivial |
| Total pipeline | < 15s | SymPy portion | Acceptable |

**Installation / Setup:**
```bash
# No new packages needed. All dependencies already available:
# numpy 2.4.2, sympy 1.14.0, both installed.
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| {T_a, T_b} = (1/2)*delta*I | Input matrices are correct Cl(9,0) generators | Compute T_a@T_b + T_b@T_a for all 81 pairs | Frobenius error < 1e-14 |
| sqrt(T_a)^2 = T_a | Closed-form formula is correct | sT @ sT - T_a for all 9 | Frobenius error < 1e-14 |
| E_a^2 = E_a | Spectral projections are idempotent | E_a @ E_a - E_a for all 9 | Frobenius error < 1e-14 |
| E_a + E_a' = I | Complementary projections sum to identity | E_a + (I - 2T_a)/2 | Exact (algebraic identity) |
| SymPy result = 0 exactly | Algebraic proof of the identity | SymPy simplify(sp - expected) | Exact zero |
| NumPy result < 1e-14 | Numerical cross-check | np.linalg.norm(sp - expected, 'fro') | < 1e-14 |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Diagonal pair (a = b) | T_a commutes with sqrt(T_a) | sqrt(T_a) T_a sqrt(T_a) = T_a^2 = (1/4)*I | Direct algebra |
| Effect algebra (positive operators) | E_a eigenvalues in {0, 1} | E_a & E_b = E_a E_b E_a = (1/2)*E_a (real) | METHODS.md grade analysis |
| Pre-verification benchmark | Same computation, prior session | Max error < 5e-16 | COMPUTATIONAL.md |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| Off-diagonal identity | ||sqrt(T_a) T_b sqrt(T_a) - (i/2)T_b||_F | < 1e-14 | 0 (exact) |
| Diagonal identity | ||sqrt(T_a) T_a sqrt(T_a) - (1/4)I||_F | < 1e-14 | 0 (exact) |
| Imaginary norm | ||Im(sqrt(T_a) T_b sqrt(T_a))||_F | > 0.5 (actually = 1.0) | ||T_b||_F / 2 = 1.0 |
| Real part zero | ||Re(sqrt(T_a) T_b sqrt(T_a))||_F | < 1e-14 | 0 (exact) |
| Effect reality | ||Im(E_a E_b E_a)||_F | = 0.0 exactly | 0 (real matrices) |
| Effect identity | ||E_a E_b E_a - (1/2)E_a||_F | < 1e-14 | 0 (exact) |

### Red Flags During Computation

- If any off-diagonal sequential product has ||Im(result)||_F < 0.1, something is fundamentally wrong with the sqrt formula or the T_a matrices.
- If any diagonal product differs from (1/4)*I by more than 1e-12, the T_a matrices may not satisfy T_a^2 = (1/4)*I (input corruption).
- If the effect algebra product has any nonzero imaginary part at all, the E_a matrices are not real projections (input corruption).
- If SymPy simplification does not yield exact zero, the closed-form formula has a sign or coefficient error.

## Common Pitfalls

### Pitfall 1: Using Wrong T_a Normalization

**What goes wrong:** The raw T_b matrices from `compute_T_b_matrices()` have non-uniform normalization: T_b[1] (traceless diagonal) satisfies {T_b[1], T_b[1]} = (1/8)*I while T_b[2..9] satisfy {T_a, T_a} = (1/2)*I.
**Why it happens:** Historical: the Peirce decomposition naturally produces operators with different norms depending on whether they come from diagonal or off-diagonal h_3(O) elements.
**How to avoid:** Always use `get_traceless_generators()` from effective_hamiltonian.py, which handles the rescaling to uniform normalization.
**Warning signs:** Anticommutation check fails for pair (0,0) but passes for others.
**Recovery:** Re-run with correct function.

### Pitfall 2: Using fisher_metric._matrix_sqrt

**What goes wrong:** That function clips negative eigenvalues to zero, producing sqrt(T_a) = (1/sqrt(2))*P_+ instead of the correct complex result.
**Why it happens:** fisher_metric._matrix_sqrt was designed for positive semidefinite matrices (density matrices, Fisher metrics).
**How to avoid:** Use the closed-form formula exclusively. Never import from fisher_metric for this computation.
**Warning signs:** sqrt(T_a) is real; sequential product is real; no complexification detected.
**Recovery:** Replace with closed-form formula.

### Pitfall 3: Branch Choice Confusion

**What goes wrong:** Different branch choices for sqrt(-1/2) give +i/sqrt(2) or -i/sqrt(2), leading to sqrt(T_a) T_b sqrt(T_a) = +(i/2)*T_b or -(i/2)*T_b.
**Why it happens:** The principal branch is a convention, not a physical constraint.
**How to avoid:** Use principal branch consistently (sqrt with Re >= 0). Document that the EXISTENCE of the imaginary part is branch-independent; only its SIGN depends on the branch.
**Warning signs:** Result is -(i/2)*T_b instead of +(i/2)*T_b (still passes criterion 4 since Im != 0).
**Recovery:** Not needed; both branches prove the same thing (exit from M_16(R)).

### Pitfall 4: Partial Verification

**What goes wrong:** Checking a few representative pairs and declaring success.
**Why it happens:** Temptation to save time on a "trivial" computation.
**How to avoid:** The contract explicitly requires ALL 72 off-diagonal, ALL 9 diagonal, ALL 72 effect pairs. Use nested loops. Report counts.
**Warning signs:** Script checks fewer than 72 + 9 + 72 = 153 pairs.
**Recovery:** Add the missing pairs.

### Pitfall 5: SymPy Float Contamination

**What goes wrong:** Converting T_a entries to SymPy via `Matrix(T_a.tolist())` produces SymPy Float objects instead of exact Rational. Then `simplify()` may not reduce to exact zero.
**Why it happens:** Python float -> SymPy Float is approximate, not exact.
**How to avoid:** Convert explicitly: `Rational(int(round(2*x)), 2)` for each entry (since all values are exactly +/-1/2 or 0). Or use `nsimplify()` to recover exact rationals.
**Warning signs:** SymPy simplify returns expressions like `2.22e-16` instead of `0`.
**Recovery:** Re-convert using exact Rational.

## Level of Rigor

**Required for this phase:** Numerical verification to machine precision (< 1e-14) for ALL pairs, supplemented by exact algebraic verification via SymPy for proof-level certainty.

**Justification:** This is a GO/NO-GO computational gate. The result is either exactly correct or the entire sequential product route fails. Machine-precision numerical agreement across all 153 pairs, combined with SymPy exact verification, constitutes definitive computational proof.

**What this means concretely:**

- Every pair must be checked individually; no "by symmetry" shortcuts
- Frobenius norm tolerance: 1e-14 (approximately 100x machine epsilon for 16x16 matrices)
- SymPy must yield exact zero for the key identities
- Both real and imaginary parts of sequential products must be checked explicitly
- Pass/fail counts must be reported

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| Eigendecomposition-based sqrt | Closed-form sqrt from known spectrum | This project (COMPUTATIONAL.md) | Simpler, faster, avoids eigenvector numerical errors |
| Numerical-only verification | Dual NumPy + SymPy verification | This project | Provides proof-level certainty alongside numerical evidence |
| Spot-check representative pairs | Exhaustive all-pairs verification | This project | Required by contract; prevents false confidence |

**Superseded approaches to avoid:**

- scipy.linalg.sqrtm: General-purpose, slower, may pick non-principal branch. Use closed-form instead.
- fisher_metric._matrix_sqrt: Clips negative eigenvalues. WRONG for this application.

## Open Questions

None. This is a straightforward computational verification with no open mathematical questions. The only question is whether the computation passes or fails, which is the entire point of the phase.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| Closed-form sqrt | Sign error in formula | Eigendecomposition: eigh(T_a), apply sqrt to eigenvalues manually | Minutes; already understood |
| SymPy exact verification | SymPy simplification timeout | Accept NumPy-only verification (still sufficient for numerical evidence) | None; just skip SymPy |
| ALL 72 pairs fail | Closed-form formula fundamentally wrong | Eigendecomposition cross-check; if that also fails, the GO/NO-GO gate fires: proceed to Phase 45 contingency | Project-level pivot |

**Decision criteria:** If criterion 1 fails for ANY pair, the sequential product route is dead. STOP and proceed to Phase 45 (Contingency). This is specified in the phase contract.

## Sources

### Primary (HIGH confidence)

- COMPUTATIONAL.md (project-level research) - Pre-verified all results; provides closed-form formula, error bounds, algorithm details
- METHODS.md (project-level research) - Grade analysis proving effect closure stays real; spectral analysis of T_a
- SUMMARY.md (project-level research) - Contradiction resolution confirming sqrt(-1/2) = i/sqrt(2), not -1/sqrt(2)
- [Gudder & Greechie, "Sequential products on effect algebras," Rep. Math. Phys. 49 (2002) 87-111](https://ui.adsabs.harvard.edu/abs/2002RpMP...49...87G/abstract) - Original sequential product definition
- [Lawson & Michelsohn, Spin Geometry (1989), Table I.4.3](https://en.wikipedia.org/wiki/Classification_of_Clifford_algebras) - Cl(9,0) classification
- [Square root of a matrix, Wikipedia](https://en.wikipedia.org/wiki/Square_root_of_a_matrix) - Principal branch definition
- [Nick Higham, "What Is a Matrix Square Root?"](https://nhigham.com/2020/05/21/what-is-a-matrix-square-root/) - Matrix sqrt theory and branch cuts

### Secondary (MEDIUM confidence)

- [van de Wetering, arXiv:1803.11139](https://arxiv.org/abs/1803.11139) - Sequential product spaces classification (background)
- [SymPy Matrices documentation](https://docs.sympy.org/latest/modules/matrices/matrices.html) - Matrix operations API

### Tertiary (LOW confidence)

- None. All sources for this computational verification phase are HIGH or MEDIUM confidence.

## Metadata

**Confidence breakdown:**

- Mathematical framework: HIGH - All equations are textbook results or pre-verified closed-form formulas
- Standard approaches: HIGH - Direct matrix multiplication; no subtle algorithms
- Computational tools: HIGH - NumPy and SymPy are mature; 16x16 matrices are trivial
- Validation strategies: HIGH - Multiple independent checks (SymPy exact, NumPy numerical, imaginary norm, effect algebra control)

**Research date:** 2026-04-04
**Valid until:** Indefinitely (pure algebra; no tool version sensitivity for these simple operations)

## Caveats and Self-Critique

1. **Assumption: T_a entries are exactly +/-1/2 or 0.** Verified empirically for all 9 generators. This is expected from the Fano triple construction but is not proven in general -- it is a consequence of our specific V_{1/2} basis choice. If someone changes the basis, SymPy exact verification would require nsimplify() or a different rational conversion strategy.

2. **No alternative approach explored in depth.** The closed-form sqrt is so clean that I dismissed eigendecomposition immediately. If the closed-form has a subtle error (unlikely given pre-verification), the eigendecomposition fallback is straightforward.

3. **SymPy verification is redundant given NumPy errors < 1e-15.** True in practice. But the contract says "verified," and exact algebraic proof is stronger than numerical evidence. The SymPy component adds < 10s to runtime with zero downside.

4. **The 1e-14 tolerance is generous.** Actual errors are < 5e-16. We could tighten to 1e-15, but the wider tolerance provides margin without any loss of confidence. The gap between actual error (1e-16) and tolerance (1e-14) is 100x.

5. **Would a specialist disagree?** No. This is straightforward computational linear algebra. The only specialist concern would be the PHYSICAL justification for applying sqrt to indefinite operators, which is Phase 43's problem, not Phase 42's.
