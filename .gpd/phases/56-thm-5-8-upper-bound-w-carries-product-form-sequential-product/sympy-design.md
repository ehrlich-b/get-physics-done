---
artifact: sympy-design
phase: 56
plan: 01
task: 5
status: DESIGN COMPLETE (NO CODE EXECUTED IN THIS TASK)
conventions:
  ambient_model: V_test = H_3(R) (x) H_3(R) ≅ 6x6 "tensor-symmetric" block; dim 36
  W_wedge_default: Peirce-1 off-diagonal 3-dim subspace of H_3(R) (Interpretation (A))
  W_full_test: span{a_i (x) b_j : a_i, b_j standard 6-dim basis of H_3(R)} = 36-dim (= V_test in this small case)
  reuse_source: Phase 54 derivations/paper5-peirce-preservation/closeout-sympy.py (compress, seq_prod)
  reuse_source_2: Phase 55 derivations/paper5-peirce-preservation/s4-sympy-spot-check.py (symbolic-exact pattern, two-mixing-function verification)
  runtime_budget: "< 30 seconds"
  exit_code: "0 = all tests PASS; non-zero = any FAIL"
---

# Plan 56-02 SymPy Spot-Check — Design Document

This document DESIGNS the SymPy H_3(R) ⊗ H_3(R) spot-check that Plan 56-02 will
execute. NO CODE IS EXECUTED in Task 5. Plan 56-02 is the consumer of this design;
the actual script (`derivations/paper5-w-carries-sp/w-carries-sympy.py` or similar) is
an output of Plan 56-02.

## Section 1 — "Wedge component" ambiguity resolution

**Roadmap phrase.** The Phase 56 roadmap scope names "Small-case SymPy check on
H_3(R) wedge component" and research flags that "H_3(R) is symmetric; plausible
interpretation is Peirce-1 off-diagonal 3-dim subspace."

**Literal-reading problem.** H_3(R) = 3x3 real symmetric matrices, dim 6. The
antisymmetric subspace of 3x3 REAL matrices is the Lie algebra so(3), also 3-dim.
But the antisymmetric subspace of a SYMMETRIC matrix is {0}: every symmetric matrix
has zero antisymmetric part. So "3-dim antisymmetric subspace of H_3(R)" taken
literally is vacuous.

**Plausible reconstructions.**

- **Interpretation (A) — Peirce-1 off-diagonal 3-dim subspace of H_3(R).** With
  respect to the three orthogonal diagonal rank-1 projectors
  `p_1 = diag(1,0,0)`, `p_2 = diag(0,1,0)`, `p_3 = diag(0,0,1)`, the Peirce-1
  subspaces V_1(p_i, p_j) are each 1-dim (spanned by `E_ij + E_ji`, the (i,j)-off-
  diagonal symmetric basis element). Their direct sum
  `V_1(p_1, p_2) ⊕ V_1(p_1, p_3) ⊕ V_1(p_2, p_3)` is the 3-dim off-diagonal
  symmetric subspace of H_3(R). Inside H_3(R), this is the complement of the
  diagonal subalgebra `V_2(p_1) ⊕ V_2(p_2) ⊕ V_2(p_3) = diag(R³)`. **THIS IS THE
  DEFAULT INTERPRETATION** for Plan 56's small-case SymPy test.

- **Interpretation (B) — Literal Λ²(R³) ≅ R³ (exterior algebra).** 3-dim but not
  naturally a subspace of H_3(R). The embedding would need an extra structure
  (e.g., Hodge dual) and is a non-sequitur for Paper 5's W-carries-SP question.

- **Interpretation (C) — Any 3-dim slice.** Ambiguous and useless.

**Default resolution.** Per planner decision: "wedge component" = **Peirce-1-space
off-diagonal 3-dim subspace of H_3(R)** w.r.t. diagonal rank-1 projector family
`{p_1, p_2, p_3}`. This interpretation (A):

- is canonical (Peirce decomposition is the natural algebra-level decomposition of
  an EJA relative to a primitive idempotent family);
- matches Phase 54's H_3(R) infrastructure (the `compress(B, i, n)` helper already
  computes C_{p_i} for exactly these projectors);
- produces a 3-dim subspace as the roadmap's "3-dim antisymmetric" numerical claim
  suggests (the coincidence "3-dim" = "number of off-diagonal pairs" is what the
  research flag is probably pointing at);
- is overridable at the Task-6 checkpoint.

**User-override path.** At Task 6, the user may override Interpretation (A) with
Interpretation (B), Interpretation (C), or an alternative. If overridden, Plan 56-02
re-scopes W_wedge accordingly.

**fp-wedge-component-silent-interpretation rejection.** This section explicitly
acknowledges the roadmap's ambiguity, names the literal-reading problem (no
antisymmetric subspace of H_3(R)), enumerates three plausible reconstructions, and
picks Interpretation (A) as an explicit planner choice, with user-override path at
the Task-6 checkpoint.

## Section 2 — Concrete W_test specification

**Ambient test space.**

```
V_test := H_3(R) (x) H_3(R)
       = symmetric-tensor-product space of two copies of 3x3 real symmetric matrices
Dim(V_test) = 6 * 6 = 36.
```

**W_test — full version.**

```
W_full := span{a_i (x) b_j : a_i, b_j ∈ standard 6-dim basis of H_3(R)}
       = V_test (since the 36 product basis elements span V_test).
Dim(W_full) = 36.
```

In this small case W_full = V_test (local tomography holds trivially at the algebraic
tensor level, the EJA being simple and the composite being H_3(R) ⊗_R H_3(R) without
extra structure). The face-status question inside V_test is vacuous at this scale,
matching the complex-case vacuity noted in `w-face-status.md` §3. This is why Plan
56 supplements with the Peirce-1-restricted test below.

**W_wedge — specialized 9-dim version (Interpretation (A)).**

```
W_off3 := V_1(p_1, p_2) ⊕ V_1(p_1, p_3) ⊕ V_1(p_2, p_3) ⊂ H_3(R), dim 3.
W_wedge := span{a_i (x) b_j : a_i, b_j ∈ W_off3 basis} ⊂ V_test, dim 9.
```

**Basis for W_off3 (SymPy-concrete):**

```
M_{12} := (1/sqrt(2)) * (E_12 + E_21)   — 3x3 matrix with 1/sqrt(2) in (1,2) and (2,1) slots, 0 elsewhere
M_{13} := (1/sqrt(2)) * (E_13 + E_31)
M_{23} := (1/sqrt(2)) * (E_23 + E_32)
```

Normalized via Frobenius inner product so `tr(M_{ij} * M_{kl}) = delta_{(ij),(kl)}`.

**Basis for W_wedge:** the 9 tensor products `M_{ij} ⊗ M_{kl}` for `{ij} ∈ {12, 13,
23}` and `{kl} ∈ {12, 13, 23}`.

**Projective units (for both factors, reused from Phase 54):**

```
p_1 = diag(1, 0, 0)
p_2 = diag(0, 1, 0)
p_3 = diag(0, 0, 1)
```

**Factor-level `seq_prod` (Phase 54 import).** Phase 54's `closeout-sympy.py` provides
`seq_prod(a, b)` on H_n(R) computed via the minimal tool-set derivation:

```
seq_prod(a, b) = sum_j lambda_j * compress(b, j, n)
```

where `lambda_j` is the j-th eigenvalue of `a` and `compress` is the model-level
realization of the A-S compression C_{p_j}.

**Tensor-level `seq_prod_W` (new, defined by product form):**

```
seq_prod_W(a_tensor, b_tensor) := decompose each into factor-basis coordinates,
                                  then apply bilinear extension:
    (a_1 (x) a_2) ∘_W (b_1 (x) b_2) := seq_prod(a_1, b_1) (x) seq_prod(a_2, b_2).
```

Extended to all of `a_tensor, b_tensor ∈ V_test` via bilinearity of the tensor
product on both arguments.

## Section 3 — Test cases

### TEST-CLOSURE (sense (a) on W_wedge and W_full)

**Goal.** Verify `seq_prod_W([0,1]_W × [0,1]_W) ⊆ W` symbolically.

**Concrete realization.** For each of a fixed small set of rational-coefficient
elements `a, b ∈ [0,1]_W`, compute `seq_prod_W(a, b)` in SymPy, check symbolic
equality with a product-basis expansion, and verify the result lies inside W
(non-zero coefficients only on basis elements of W).

**Expected result.** PASS. The product-form identity
`(a_1 ⊗ a_2) ∘ (b_1 ⊗ b_2) = (a_1 ∘ b_1) ⊗ (a_2 ∘ b_2)` is closed by construction,
because factor-level `seq_prod(a_1, b_1)` lands in H_3(R) and similarly for the
second factor.

**Test cases (explicit):**

- **W_full case 1:** `a = p_1 ⊗ p_1`, `b = p_2 ⊗ p_2`. Expected
  `seq_prod_W(a, b) = C_{p_1}(p_2) ⊗ C_{p_1}(p_2) = 0 ⊗ 0 = 0 ∈ W_full`. PASS.
- **W_full case 2:** `a = (p_1 + p_2) ⊗ (p_1 + p_2)`, `b = p_1 ⊗ p_2`. Expected
  factor-wise `seq_prod(p_1 + p_2, p_1) = C_{p_1}(p_1) + C_{p_2}(p_1) = p_1 + 0 = p_1`;
  similar for 2nd factor; result `p_1 ⊗ p_2 ∈ W_full`. PASS.
- **W_wedge case 1:** `a = M_{12} ⊗ M_{13}`, `b = M_{23} ⊗ M_{12}`. Expected
  `seq_prod_W(a, b)` ∈ W_wedge iff factor-level `seq_prod(M_{12}, M_{23})` and
  `seq_prod(M_{13}, M_{12})` each land in W_off3. This is a sharper test —
  **factor-level Peirce-1 ∘ Peirce-1 may produce V_2 components**, in which case
  W_wedge is NOT closed under ∘_W and sense (a) fails on the specialized W_wedge.
  If this occurs, the test identifies it as the right answer (sense (a) fails on
  the specialized wedge but holds on W_full, i.e., the wedge interpretation is
  over-narrow). PASS condition for this case: output matches the Peirce-decomposition
  prediction.

### TEST-S1 (additivity on W)

**Goal.** For product effects `a ⊗ b ∈ [0,1]_W`, `c ⊗ d, c' ⊗ d' ∈ [0,1]_W`, verify:

```
(a ⊗ b) ∘_W ((c ⊗ d) + (c' ⊗ d')) == (a ⊗ b) ∘_W (c ⊗ d) + (a ⊗ b) ∘_W (c' ⊗ d')
```

**Strategy.** SymPy `simplify` on the symbolic difference LHS − RHS; expect zero.
Use general (symbolic) rational coefficients where possible, and fall back to a
randomly-sampled batch of rational test-case instantiations if pure symbolic
simplification is too slow.

**Expected.** PASS. Follows from bilinearity of the tensor product AND factor-level
S1 on `seq_prod`.

### TEST-S3 (unitality on W)

**Goal.** For generic `a ∈ [0,1]_{H_3(R)}`, `b ∈ [0,1]_{H_3(R)}`, verify:

```
(1_3 ⊗ 1_3) ∘_W (a ⊗ b) == a ⊗ b
```

where `1_3` is the 3x3 identity.

**Strategy.** SymPy `simplify(LHS - RHS)`; expect zero.

**Expected.** PASS. Factor-level S3 gives `seq_prod(1_3, a) = a` and
`seq_prod(1_3, b) = b`, hence `(1_3 ⊗ 1_3) ∘_W (a ⊗ b) = a ⊗ b`.

### TEST-S4 (orthogonality symmetry on W)

**Goal.** For compatible product effects `a ⊗ b, c ⊗ d ∈ [0,1]_W` with
`(a ⊗ b) ∘_W (c ⊗ d) = 0`, verify:

```
(c ⊗ d) ∘_W (a ⊗ b) == 0
```

**Strategy.** Select concrete product effects with factor-level orthogonality (e.g.,
`a = p_1`, `c = p_2` so `seq_prod(a, c) = 0`), compute LHS = forward, compute
reverse; expect zero. Apply factor-level S4 on each factor separately.

**Test cases (explicit):**

- `a = p_1, b = p_1, c = p_2, d = p_2`. Forward:
  `seq_prod(p_1, p_2) ⊗ seq_prod(p_1, p_2) = 0 ⊗ 0 = 0`. Reverse:
  `seq_prod(p_2, p_1) ⊗ seq_prod(p_2, p_1) = 0 ⊗ 0 = 0`. PASS.
- `a = p_1 + p_2, b = p_3, c = p_3, d = p_1`. Forward requires factor-level S4
  on `seq_prod(p_1 + p_2, p_3)` and `seq_prod(p_3, p_1)`. Compute symbolically.

**Expected.** PASS. Factor-level S4 on each component + tensor bilinearity. The
tensor-level forward-to-reverse reduction uses the product-state-separation trick
of `prop:inheritance` (composite-lt.tex:81-89); in the SymPy test we merely verify
the identity symbolically on concrete effects, which is sufficient evidence without
re-deriving the proof.

### TEST-NEGATIVE (sense (a) counterexample search)

**Goal.** Search for a concrete `(a, b) ∈ [0,1]_W × [0,1]_W` with
`seq_prod_W(a, b) ∉ W`. This should FAIL to find a counterexample on W_full (where
closure is guaranteed by the product-form identity). On W_wedge, it may or may not
find a counterexample — if it does, the finding distinguishes "sense (a) on W_full"
from "sense (a) on W_wedge".

**Strategy.** For a small fixed list of test pairs (e.g., boundary effects at the
corners of `[0,1]_{W_wedge}`), compute `seq_prod_W(a, b)` in the ambient V_test
basis; check whether the result has non-zero coefficients on ambient basis elements
OUTSIDE W.

**Expected on W_full.** NO COUNTEREXAMPLE FOUND (PASS for sense (a) on W_full).

**Expected on W_wedge.** Either NO COUNTEREXAMPLE FOUND (PASS for sense (a) on the
wedge) or a counterexample is found (indicates the specialized wedge interpretation
is NOT closed under ∘ and the small-case test is actually diagnosing something
about the Peirce structure, not about the main theorem).

### Skipped tests (covered by factor-level Phase 54/55 infrastructure)

- **S2 (continuity):** factor-level continuity + tensor continuity; infinite-
  dimensional subtlety not present in finite case.
- **S5 (compatible associativity):** reduces to factor-level S5; already verified
  by Phase 54 `closeout-sympy.py` on factor H_3(R).
- **S6 (compatible additivity):** ditto.
- **S7 (compatible multiplicativity):** ditto.

These are NOT run in the spot-check; the plan 56-02 proof text cites the factor-
level reduction.

## Section 4 — Reuse plan for Phase 54/55 infrastructure

**From `/Users/ehrlich/scratch/get-physics-done/derivations/paper5-peirce-preservation/closeout-sympy.py`:**

- Import `compress(B, i, n)` — concrete H_n(R) realization of A-S compression C_{p_i}.
  Used for factor-level sequential product.
- Import `seq_prod(a, b, ...)` — the factor-level sequential product helper.
- Reuse H_3(R) basis-generator helpers (if present) for generating the six-element
  standard basis of H_3(R).
- Baseline runtime: 0.013 s on H_3(R) and H_4(R). Tensor case estimated at 10-100x
  (still well under the 30 s budget).

**From `/Users/ehrlich/scratch/get-physics-done/derivations/paper5-peirce-preservation/s4-sympy-spot-check.py`:**

- Reuse symbolic-exact simplification pattern: `sp.simplify(LHS - RHS); assert it
  simplifies to 0`.
- Reuse two-mixing-function verification structure: if Plan 56-02 wants to guard
  against an f-choice-specific bug, run both `f = sqrt(λ μ)` and `f = λ μ` as
  Phase 55 did for the factor-level compatibility case. For Phase 56 this is
  optional since f does not appear explicitly in the product-form tensor construction
  at the S4 verification level.

**New helpers to add in `w-carries-sympy.py` (Plan 56-02):**

- `tensor_product(A, B)` — SymPy Matrix tensor product via `sp.zeros(m*p, n*q)` and
  block-assignment. SymPy provides `TensorProduct` but using explicit block
  construction is clearer for the 6x6 output.
- `product_sp(a_tensor, b_tensor)` — decomposes each tensor into factor-basis
  coordinates via a stored basis-matrix-lookup table, applies factor-level
  `seq_prod` separately, re-assembles.
- `is_in_W_full(x)` — checks `x ∈ span{a_i ⊗ b_j}` by solving a linear system
  symbolically.
- `is_in_W_wedge(x)` — same but against the 9-dim W_wedge basis.

## Section 5 — Runtime budget + exit code

**Runtime budget:** < 30 seconds on a standard developer workstation (Phase 54 H_3
baseline 0.013 s; tensor case estimated 1-3 s; margin ≈ 10-30x).

**Exit code criterion:**

- Exit 0 if all scheduled tests (TEST-CLOSURE on W_full, TEST-S1, TEST-S3, TEST-S4,
  TEST-NEGATIVE) PASS.
- Exit 1 if any test FAILS.
- Output header includes: SymPy version, Python version, wallclock timing per test,
  per-test PASS/FAIL record, total-elapsed.

**Output format:**

```
# Plan 56-02 SymPy Spot-Check Output
Python: <version>
SymPy: <version>
Timestamp: <ISO 8601>
Wedge interpretation: (A) Peirce-1 off-diagonal 3-dim
[TEST-CLOSURE/W_full] PASS in N.NNN s
[TEST-CLOSURE/W_wedge] PASS/FAIL in N.NNN s
[TEST-S1] PASS in N.NNN s
[TEST-S3] PASS in N.NNN s
[TEST-S4] PASS in N.NNN s
[TEST-NEGATIVE/W_full] PASS (no counterexample) in N.NNN s
TOTAL elapsed: N.NNN s
Exit code: 0
```

## Section 6 — FAIL routing

| FAIL mode                            | Diagnosis                                                                  | Route                                                                                      |
|--------------------------------------|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| TEST-CLOSURE FAIL on W_full          | Sense (a) fails on the algebraic tensor product itself                     | Approach 3 (Gudder-Greechie-style) triggered. Phase 56 outcome = (C). Plan 56-03 revision  |
|                                      |                                                                            | text abandons sense-(b)/(c) claim; `sms:minimal` needs re-scoping. Milestone pause.         |
| TEST-CLOSURE FAIL on W_wedge         | The specialized wedge interpretation (A) is over-narrow                    | Interpretation (A) is not closed under ∘; Plan 56-02 reports the wedge-limitation         |
|                                      |                                                                            | and scopes the sense-(b) proof to W_full (not W_wedge). User notified at Plan 56-02 close. |
| TEST-S1 FAIL                         | Additivity fails on W                                                      | Diagnose: factor-level S1 (Phase 54 baseline passes → shouldn't happen) vs. bilinear-       |
|                                      |                                                                            | extension misdefinition. Fix `product_sp` helper if bilinear-extension issue.              |
| TEST-S3 FAIL                         | Unitality fails on W                                                       | Diagnose: factor-level S3 (Phase 54 baseline) vs. 1_W = 1_B ⊗ 1_M conversion.              |
| TEST-S4 FAIL                         | Orthogonality symmetry fails on W                                          | Diagnose whether factor-level S4 holds (Phase 55 baseline) or whether the tensor-         |
|                                      |                                                                            | reduction has a sign error. Re-verify symbolic simplification.                             |
| TEST-NEGATIVE finds a counterexample | Sense (a) genuinely fails on W                                             | Treat as TEST-CLOSURE FAIL; route per above.                                              |

**Cross-pollination with Task 6 checkpoint:** If TEST-CLOSURE or TEST-S4 FAIL, Plan
56-02 STOP'S and returns to the Task 6 hand-off routing to flip (e.g., from (b)+(c)
target to sense (a) only + Approach 3 footnote).

## Forbidden-proxy rejections

- **fp-wedge-component-silent-interpretation** — REJECTED. Section 1 explicitly
  names the literal-reading problem (no antisymmetric subspace of H_3(R)),
  enumerates three reconstructions, and picks Interpretation (A) as an explicit
  planner choice with user-override path.
- **No code executed in this task.** This is a design document only; Plan 56-02 is
  the consumer. Zero writes to scripts; Phase 54/55 scripts referenced by read-only
  path citations.
