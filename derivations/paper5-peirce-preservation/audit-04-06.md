# Phase 4-06 Circularity Audit — Peirce Feedback Extension

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b (Paper 5) / a&b (v2.0 Phase 4); compression=C_p; peirce_spaces=V_2(p_i)=range(C_{p_i}), V_1(p_i,p_j)=off-diagonal; allowed_axioms={S1, S3, linearity, A-S compression axioms}; forbidden_tokens={M_n(ℂ) as proof device, Jordan, EJA, Lüders, pxp, √a b √a, operator product, f(λ,μ)=√(λμ) as primitive, h_n(ℂ), spin factor as proof device}

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 01 (Foundation wave, task 1: DERV-54-01 audit)
**Audit target:** `derivations/04-peirce-feedback-extension.md` (v2.0 Phase 4-06)
**Audit date:** 2026-04-16
**Auditor:** gpd-executor (Phase 54-01 Task 1)
**Verdict location:** Section 4 below.

---

## Section 1: Commit Pin and Audit Target

**Target file:** `derivations/04-peirce-feedback-extension.md` (423 lines)
**Companion:** `.gpd/phases/04-sequential-product-formalization/04-06-SUMMARY.md`

**Commits pinned:**

| Commit | Subject | What it added |
|--------|---------|----------------|
| `6391f0d3` | `derive(04-06): corrected sequential product via Peirce 1-space feedback with positivity bound and faithful self-modeling selection` | Created `derivations/04-peirce-feedback-extension.md` (the 423-line derivation) |
| `4fa5acec` | `compute(04-06): SymPy verification of corrected product -- S3, bilinearity, classical limit, sharp agreement, Luders match, phi essential` | SymPy artifacts (verification layer) |
| `9608ac54` | `docs(04-06): complete Peirce feedback extension plan -- corrected product passes S3, matches Luders, phi essential` | Created `04-06-SUMMARY.md` (298 lines); this is the plan-closing commit referenced by the plan frontmatter (`ref-phase-4-06`) as the pin |

**Primary pin per PLAN.md frontmatter:** `9608ac54` (plan-closing). The derivation file itself was introduced earlier by `6391f0d3`. Both hashes are recorded for reproducibility; the classification below is against the contents of `derivations/04-peirce-feedback-extension.md` as it stands at `9608ac54` (unchanged from `6391f0d3`).

```
$ git show 9608ac54 --stat
commit 9608ac5430657a36ceda083877b0f82ddd1d55c7
Author: Bryan Ehrlich <ehrlich.bryan@gmail.com>
Date:   Fri Mar 20 22:04:23 2026 -0400

    docs(04-06): complete Peirce feedback extension plan -- corrected product passes S3, matches Luders, phi essential

 .../04-06-SUMMARY.md | 298 +++++++++++++++++++++
 1 file changed, 298 insertions(+)
```

```
$ git log --oneline --all -- derivations/04-peirce-feedback-extension.md
6391f0d3 derive(04-06): corrected sequential product via Peirce 1-space feedback...
```

The derivation file is 423 lines, comprising Steps 1-10 culminating in Eqs. (04-06.1)-(04-06.5). The derivation chain of interest for Phase 54 is Eq. (04-06.1) → Eq. (04-06.4) — i.e., how the general form (04-06.1) is specialized (through positivity in Step 4 and self-modeling in Step 5) to the closed form (04-06.4).

---

## Section 2: Forbidden-Token Grep

### 2.1 Grep commands and raw output

Commands run on `derivations/04-peirce-feedback-extension.md`:

```
$ grep -n -w -E "(Jordan|EJA|Lüders|Luders|pxp|h_n|operator product|spin factor)" derivations/04-peirce-feedback-extension.md
(no hits)

$ grep -n -E "Luders" derivations/04-peirce-feedback-extension.md
(see table below; 13 hits on "Luders")

$ grep -n -E "M_n\(.\)|M_2\(.\)|M_n\(C\)|M_2\(C\)" derivations/04-peirce-feedback-extension.md
(see table below; many hits on "M_2(C)^sa")

$ grep -n -E "sqrt\(a\) b sqrt\(a\)|√a b √a" derivations/04-peirce-feedback-extension.md
(see table below; 4 hits on "sqrt(a) b sqrt(a)")

$ grep -n -E "f\(λ,μ\)=√\(λμ\)|f\(lambda,mu\)=sqrt" derivations/04-peirce-feedback-extension.md
(no hits on the exact primitive form)
```

Tokens with ZERO hits (confirming cleanliness on these): `Jordan`, `EJA`, `pxp`, `h_n`, `operator product`, `spin factor`, `√(λμ) as primitive`.

Tokens with hits (require per-hit classification): `Luders` (13 hits), `M_2(C)` / `M_2(C)^sa` (many hits), `sqrt(a) b sqrt(a)` (4 hits), `sqrt(lambda_1 lambda_2)` and `sqrt(a)` (many hits — real-valued sqrt, not a forbidden pattern, but flagged for per-hit audit).

### 2.2 Per-hit classification — "Luders" (13 hits)

| Line | Excerpt | Classification |
|------|---------|---------------|
| 25 | "coincides with the Luders product on M_2(C)^sa, as expected" | **(c) incidental / match-to-known-result claim** — does not use Luders structure to prove anything; cites known M_2(C)^sa fact for coincidence check |
| 123 | "with equality if and only if the product is the Luders product" | **(c) incidental** — characterizes the bound-saturation case; not a proof step |
| 165 | "f = sqrt(lambda_1 lambda_2) saturates the bound and gives a valid product (the Luders product)" | **(c) incidental** — naming convention for saturating case |
| 203 | "phi = isomorphism (faithful model): f = sqrt(lambda_i lambda_j) (Luders product, maximal coherence)" | **(c) incidental** — parenthetical naming |
| 314 | "f = sqrt(lambda_i lambda_j): faithful self-model (phi isomorphism) -> Luders product, passes S3" | **(c) incidental** |
| 356 | "Luders rule sqrt(a) b sqrt(a) as a DEFINITION \| ABSENT \| We DERIVE the equivalent formula from OUS primitives" | **(c) incidental — explicitly NEGATED**; this is in the Step 9 "Explicit Non-Occurrences" table declaring Luders rule ABSENT as definition |
| 359 | "COINCIDES with the Luders product sqrt(a) b sqrt(a) on M_2(C)^sa ... But the DERIVATION uses only OUS primitives — it does not import sqrt(a) as a C\*-algebra operation" | **(c) incidental — explicitly disclaimed** as non-proof-device |
| 365 | "Step 10: Equivalence with Luders on M_2(C)^sa" | **(c) incidental** — post-hoc equivalence check, not a proof step in (04-06.1)→(04-06.4) chain |
| 367 | "The corrected product Eq. (04-06.4) equals the Luders product sqrt(a) b sqrt(a) on M_2(C)^sa" | **(c) incidental** — claim of Step 10 (validation) |
| 378 | "Luders product:" (computation header) | **(c) incidental** — inside Step 10 validation computation |
| 385 | "the OUS-derived product agrees with the known quantum mechanical product on M_2(C)^sa" | **(c) incidental** |
| 403 | "Eq. (04-06.5): Equivalence with Luders on M_2(C)^sa:" | **(c) incidental** — equivalence claim, labeled as such |
| 418 | "Luders agreement on M_2(C)^sa \| PASS \| Explicit computation, Step 10" | **(c) incidental** — summary table entry for validation |

**Classification summary for "Luders":** No hits use Luders product as a proof device for (04-06.1)→(04-06.4). All hits are (c) incidental mentions in which the Luders product appears as a **match-to-known-result target** (Step 10 validation) or as a **naming convention** (saturating case). The text **explicitly disclaims** (lines 356, 359, 385) that Luders is being used as a definition or proof device. **This token does not fail the audit by itself.**

### 2.3 Per-hit classification — "M_2(C)^sa" / "M_2(C)"

`M_2(C)^sa` appears on lines 25, 48, 82, 119, 125, 127, 218, 222, 359, 365, 367, 369, 385, 403, 418 (selected; full list matches grep output in Section 2.1). These group naturally into four categories:

| Line(s) | Context | Classification |
|---------|---------|---------------|
| 25, 365, 367, 385, 403, 418 | Step 10 and summary/table references: "coincides with Luders on M_2(C)^sa" / "Equivalence with Luders on M_2(C)^sa" / "PASS — Explicit computation, Step 10" | **Validation example** — Step 10 is a post-hoc coincidence check against a known model; not part of (04-06.1)→(04-06.4) chain |
| 48, 82 | Step 1 and Step 2 "Concrete verification on M_2(C)^sa" / "Concrete form on M_2(C)^sa" illustrating the pinching-map identity and P_{01}(b) form | **Validation example** — explicitly framed as concrete illustration of an abstract OUS statement established immediately above |
| 119 | **Theorem (Positivity bound on f).** "For the product Eq. (04-06.1) to map effects to effects **for all effects a, b in M_2(C)^sa**, the mixing function must satisfy $\lvert f(\lambda_1,\lambda_2)\rvert^2 \le \lambda_1\lambda_2$" | **⚠ PROOF DEVICE** — the theorem statement scopes the effects-to-effects claim to M_2(C)^sa, and the proof (line 125ff) performs the derivation inside M_2(C)^sa. See watchpoint W1 below. |
| 125-163 | **Proof (M_2(C)^sa, two-projector case).** Uses matrix form `b = [[b_{00}, b_{01}], [b_{10}, b_{11}]]` in the P_0/P_1 eigenbasis; invokes PSD of 2×2 matrices (`\|b_{01}\|^2 \le b_{00}b_{11}`); computes determinant; saturates bound with rank-1 projector | **⚠ PROOF DEVICE** — this IS the proof of the positivity bound (04-06.2), and it is carried out entirely inside M_2(C)^sa. See watchpoint W1 below. |
| 127 | "Let a = lambda_1 P_0 + lambda_2 P_1 with 0 <= lambda_2 <= lambda_1 <= 1 and P_0 + P_1 = I" | part of W1 proof body — PROOF DEVICE |
| 218, 222 | Step 5 "More precisely, Eq. (04-06.4) says that in M_2(C)^sa: a & b = sqrt(a) b sqrt(a) ... where the matrix product on the right is the CONCRETE REALIZATION of the abstract formula in M_2(C)^sa" | **Validation example** — explicitly labels the matrix product as "CONCRETE REALIZATION", not definition; the abstract formula (04-06.4) is what the derivation produces, M_2(C)^sa is a sanity check |
| 359 | "COINCIDES with the Luders product sqrt(a) b sqrt(a) on M_2(C)^sa. This is expected (the Luders product is the unique SP on B(H)^sa). But the DERIVATION uses only OUS primitives" | **Validation example — explicitly disclaimed** as non-proof-device |
| 369 | Step 10 "For a = lambda_1 P_0 + lambda_2 P_1 in M_2(C)^sa (spectral decomposition)" | **Validation example** — Step 10 verifies Eq. (04-06.4) against Luders, not part of (04-06.1)→(04-06.4) chain |

**Classification summary for "M_2(C)^sa":** Most hits are validation-example framing (Step 1 Step 2 illustrations; Step 5 "concrete realization"; Step 10 equivalence check). The **critical cluster is lines 119-163** (the Theorem + Proof of the positivity bound), where M_2(C)^sa IS the domain of the proof. See watchpoint W1 below for the binary treatment.

### 2.4 Per-hit classification — "sqrt(a) b sqrt(a)"

| Line | Context | Classification |
|------|---------|---------------|
| 220 | "in M_2(C)^sa: a & b = sqrt(a) b sqrt(a)" | **Validation example** — CONCRETE REALIZATION claim for M_2(C)^sa (line 222 explicitly labels it as concrete realization, not definition) |
| 356 | "Luders rule sqrt(a) b sqrt(a) as a DEFINITION \| ABSENT" | **(c) incidental, explicitly NEGATED** |
| 359 | "COINCIDES with the Luders product sqrt(a) b sqrt(a) on M_2(C)^sa" | **Validation example, explicitly disclaimed** |
| 367 | "equals the Luders product sqrt(a) b sqrt(a) on M_2(C)^sa" | **Validation example** — Step 10 equivalence |

No `sqrt(a) b sqrt(a)` hit classifies as a proof device. The pattern appears only as (a) concrete realization inside a specific model (lines 220, 222), (b) explicit negation / absence declaration (line 356), or (c) Step 10 coincidence check.

### 2.5 Per-hit classification — sqrt(a) / sqrt(lambda_i lambda_j) (non-forbidden)

The function `sqrt(lambda_i lambda_j)` and the operator `sqrt(a)` appear throughout Steps 4, 5, 7, 8, 9, 10. These are **NOT forbidden tokens per se** — the forbidden version is the primitive form `f(λ,μ) = √(λμ)` **as a starting primitive**, not the derived conclusion. The derivation consistently treats √ as:

- Real-valued function on spectral values in [0,1] (Step 5 line 209-213 explicit justification)
- Applied via spectral functional calculus `g(a) = sum g(lambda_i) p_i` for g: [0,1] → ℝ (line 209, 342)
- **Derived**, not primitive: f = sqrt(lambda_i lambda_j) is the CONCLUSION of the positivity bound (Step 4) + self-modeling faithfulness (Step 5), not assumed

This usage is **classified (c) incidental** with respect to the forbidden-token list. It is consistent with the allowed-axiom scope (real-valued spectral functional calculus over OUS spectral decomposition is an A-S / vdW-legal OUS operation).

---

## Section 3: Step-by-Step Derivation Trace Table (Eq. 04-06.1 → Eq. 04-06.4)

Classification column uses these codes (per PLAN.md frontmatter):

- **OUS** = OUS primitive (order, unit, positive cone)
- **S1** = vdW 2019 Def. 2 S1 (additivity in 2nd arg)
- **S3** = vdW 2019 Def. 2 S3 (unitality + sharp constraint)
- **LIN** = linearity derived from S1 + finite-dim
- **AS** = A-S compression axiom (idempotency / positivity / complement / projector-fix)
- **SPEC** = spectral decomposition in OUS (A-S Ch. 8 / vdW Def. 9; allowed as prior input)
- **SPFC** = spectral functional calculus on real values (OUS-legal for spectral OUS)
- **VAL** = validation example in a specific model; does not prove the abstract claim
- **JORDAN** = Jordan-level proof device (FAIL)
- **MNC** = M_n(ℂ)-level proof device (FAIL)
- **SPIN** = spin-factor proof device (FAIL)
- **UNDECL** = undeclared / unclassified (FAIL, conservative rule)

### Step-by-step table

| # | Line(s) | Step or Sub-Step | Description | Classification | Notes |
|---|---------|------------------|-------------|----------------|-------|
| 1 | 30-54 | Step 1: C4 correction | States `C_p + C_{p^perp} = pinching = id − P_1(p)`, corrects prior (wrong) `C_p + C_{p^perp} = id` | **AS** | Corrected compression-axiom statement (A-S Ch. 7/8-legal) |
| 2 | 48-52 | Step 1 concrete check | "C_{P_0}(b) + C_{P_1}(b) = P_0 b P_0 + P_1 b P_1 = pinch(b)" on M_2(C)^sa | **VAL** | Validation example; abstract statement stated in lines 42-46 |
| 3 | 66-72 | Step 2: Pinching and P_1 definition | `Pinch(b) := sum_i C_{p_i}(b)`; `P_1(b) := b − Pinch(b)` | **AS** (definition from A-S compressions) | Pure OUS-level definition using A-S compressions |
| 4 | 74-78 | Step 2: Peirce (i,j) component | `P_{ij}(b)` = component of `P_1(b)` in `V_{ij}` | **AS** | OUS-level definition |
| 5 | 80-86 | Step 2: OUS primitive status | Declares `P_1` as OUS-definable from compressions | **AS** | Correctly identifies P_1 as A-S-derived |
| 6 | 82-86 | Step 2: M_2(C)^sa realization | `P_{01}(b) = [[0, b_{01}],[b_{10}, 0]]` | **VAL** | Concrete form as sanity check, not definition |
| 7 | 91-94 | Step 3: **Eq. (04-06.1)** general form | `a ∘ b = sum λ_i C_{p_i}(b) + sum_{i<j} f(λ_i, λ_j) P_{ij}(b)` | **AS + SPEC + LIN** | General ansatz. Uses spectral decomposition of a and linearity of L_a. f unspecified |
| 8 | 102-111 | Step 3: Requirements table on f | Lists S1, S2, S3, effect range, sharp agreement, classical limit, symmetry | **S1 + S3 + OUS** | Requirements, not derivation |
| 9 | 115-118 | Step 4 header: positivity bound proposition | Declares the theorem to be proved: `\|f\|^2 ≤ λ_1 λ_2` | — | Claim, not proof |
| **10 (W1)** | **119-123** | **Theorem statement of the positivity bound, scope = M_2(C)^sa** | "For the product Eq. (04-06.1) to map effects to effects **for all effects a, b in M_2(C)^sa**, the mixing function must satisfy ..." | **⚠ MNC (proof device, conservative rule)** | **SEE WATCHPOINT W1 BELOW.** The theorem itself is scoped to M_2(C)^sa; the "abstract" bound on f is established only on this model. |
| **11 (W1)** | **125-163** | **"Proof (M_2(C)^sa, two-projector case)."** | Writes `b` as 2×2 matrix in P_0/P_1 eigenbasis, uses PSD `\|b_{01}\|^2 ≤ b_{00}b_{11}`, computes 2×2 determinant, saturates with rank-1 projector | **⚠ MNC (proof device)** | **This IS the derivation of Eq. (04-06.2).** Uses matrix structure of M_2(C)^sa (off-diagonal entries, 2×2 determinant, PSD condition in matrix form) as the proof machinery. **Conservative rule: FAIL.** See watchpoint W1 below. |
| 12 | 165 | Step 4 closing: bound is achievable | States `f = sqrt(λ_1 λ_2)` saturates and is valid | — | Observation |
| 13 | 175-194 | Step 5: self-modeling faithfulness | Argues f = sqrt(λ_1 λ_2) is selected by faithful phi (information-preservation principle) | **ARGUMENT (not OUS-primitive)** | Physics argument, not axiomatic derivation; does not itself violate forbidden-token list, but does not formally derive f = √(λ_i λ_j) from S1+S3+LIN+AS alone |
| 14 | 194-198 | **Eq. (04-06.3) / (04-06.4)** | f(λ_i,λ_j) = sqrt(λ_i λ_j); `a ∘ b = sum λ_i C_{p_i}(b) + sum_{i<j} sqrt(λ_i λ_j) P_{ij}(b)` | depends on #11 and #13 | **Inherits the FAIL from step 11.** Also depends on the physics argument in step 13. |
| 15 | 209-222 | Step 5: remark on OUS status of sqrt | Declares sqrt on real spectral values is SPFC-legal; M_2(C)^sa matrix `sqrt(a) b sqrt(a)` is CONCRETE REALIZATION | **SPFC (for abstract √)** + **VAL (for M_2(C)^sa realization)** | The abstract √ usage is OUS-legal; the matrix realization is correctly framed as validation |
| 16 | 232-250 | Step 6: verification of S3 | `1 ∘ a = C_1(a) = a` from spectral decomp of 1 | **S3 + AS** | Verification; OUS-legal |
| 17 | 256-262 | Step 7.1: verification of S1 | Linearity of C_{p_i} and P_{ij} gives a ∘ (b+c) = a∘b + a∘c | **S1 + LIN** | OUS-legal |
| 18 | 264-268 | Step 7.2: verification of S2 | Continuity of spectral decomposition and sqrt | **SPEC + SPFC** | OUS-legal |
| 19 | 270-276 | Step 7.3: sharp agreement | p ∘ b = C_p(b) for sharp p | **S3 + AS** | OUS-legal |
| 20 | 278-284 | Step 7.4: classical limit | V_1 = 0 on simplices, P_{ij} = 0, product reduces to pinching | **AS + OUS** | OUS-legal |
| 21 | 286-288 | Step 7.5: effect range | Cites Step 4 result | **Inherits from #11** | FAIL inherited |
| 22 | 298-325 | Step 8: phi algebraic essentiality | Physics argument about selection of f | **ARGUMENT** | Not a new primitive; non-violating |
| 23 | 329-361 | Step 9: circularity audit (self-audit by the derivation) | Table of primitive usage and explicit non-occurrences; internal audit declares "PASSED" | **VAL (self-audit)** | This is the internal audit claim; the current Phase 54 audit supersedes it and reaches a different conclusion on W1 |
| 24 | 365-385 | Step 10: equivalence with Luders on M_2(C)^sa | Matrix-form equivalence between Eq. (04-06.4) and sqrt(a) b sqrt(a) | **VAL** | Equivalence check, not part of (04-06.1)→(04-06.4) chain |
| 25 | 389-419 | Summary and results table | Restatement of (04-06.1)-(04-06.5); property verification table | — | Summary |

**Row counts by classification** (for (04-06.1)→(04-06.4) derivation chain, rows 1-14):

- OUS + AS + SPEC + LIN + S1 + S3 + SPFC + VAL + ARGUMENT: most rows
- **MNC (proof device, FAIL): 2 rows (#10, #11, the positivity-bound theorem+proof)**
- Row #14 (Eq. (04-06.4) itself): inherits FAIL via positivity-bound dependency

### Cross-reference: "Existing Results to Leverage" row in 54-RESEARCH.md

54-RESEARCH.md Step 1 "Known difficulties" (line 108-111) PREDICTED this watchpoint:

> "Line 125: 'Proof (M_2(C)^sa, two-projector case)' for positivity bound — is this used as proof of the abstract bound, or only as a worked example? If proof, that's a leak."
> "Lines 119, 218, 222: M_2(C)^sa appears in theorem statements and 'concrete realization' — classify each as proof-device vs. validation-example."
> "Paper 5 line ~543 inherits 'generates a two-level face isomorphic to a spin factor, on which the Schur complement criterion gives' — this is a **spin factor** invocation in the proof of the positivity bound. Spin factors are JB-algebras; this is a Jordan-level proof device. Flag."

The current audit confirms all three predictions. See Watchpoints W1 and W3 below.

---

## Section 4: Watchpoints

### Watchpoint W1: Line 125 — "Proof (M_2(C)^sa, two-projector case)" of the positivity bound

**Question:** Is the proof of Eq. (04-06.2) (`|f(λ_1,λ_2)|^2 ≤ λ_1 λ_2`) a proof of an abstract OUS-level bound, or only a worked example validating an abstractly-proved bound?

**Evidence FOR "proof device" (FAIL):**

1. The theorem statement on line 119 explicitly scopes "For the product Eq. (04-06.1) to map effects to effects **for all effects a, b in M_2(C)^sa**, the mixing function must satisfy ..." — the scope of the conclusion is M_2(C)^sa.
2. The proof header on line 125 is explicitly "**Proof (M_2(C)^sa, two-projector case).**" — labels the proof as model-specific.
3. The proof body (lines 127-163) uses:
   - matrix entries `b = [[b_{00}, b_{01}],[b_{10}, b_{11}]]` in the P_0/P_1 eigenbasis
   - PSD criterion in matrix form `|b_{01}|^2 ≤ b_{00} b_{11}` (intrinsically M_2(C) structure)
   - 2×2 determinant non-negativity
   - rank-1 projector to saturate the PSD bound
4. The proof does NOT contain a separate abstract-OUS argument (e.g., Schur-complement on a spin factor, positivity of a 2×2 effect-algebraic sub-object, or compression-algebra combinatorics) — only the matrix computation.
5. The "sufficiency" direction (lines 159-163) is also inside M_2(C)^sa.

**Evidence AGAINST "proof device" (would support VAL):**

1. Lines 48-52 (Step 1) and lines 80-86 (Step 2) do establish the pinching map and P_1 definition at the abstract OUS level, so the ABSTRACT bound `|f| ≤ √(λ_i λ_j)` can be **stated** abstractly.
2. The result (04-06.2) is used later (Step 7.5, Step 10) as if it applied abstractly.

**Classification (conservative rule per PLAN.md fp-audit-ambiguous-verdict):**

The evidence FOR proof-device is much stronger:

- The theorem statement is explicitly scoped to M_2(C)^sa.
- The proof header explicitly says "(M_2(C)^sa, two-projector case)".
- The proof body uses only matrix structure.
- No separate abstract proof is given.

The PLAN.md test-audit-step-trace procedure says: "rows in columns {Jordan-level proof device, M_n(ℂ)-level proof device, undeclared} trigger AUDIT-FAILS; rows in {validation example} are allowed." And the conservative rule says: "if ambiguous, classify FAIL."

This is not even ambiguous: it IS an M_n(C)-level proof, with "M_2" even in the proof header. Classification: **M_n(ℂ)-level proof device (FAIL)**. The positivity-bound conclusion in (04-06.2) is only proved inside the model M_2(C)^sa. Step 14 (Eq. (04-06.4)) inherits this failure because f = √(λ_i λ_j) is selected out of the family `|f| ≤ √(λ_i λ_j)` whose abstract-OUS establishment depends on (04-06.2).

**W1 verdict: FAIL.** The positivity bound Eq. (04-06.2) — and therefore the corrected-product formula Eq. (04-06.4) — is not established by OUS primitives alone inside `derivations/04-peirce-feedback-extension.md`. M_2(C)^sa matrix structure is a proof device for the bound.

### Watchpoint W2: Lines 48, 82, 119, 218, 222 and other M_2(C)^sa mentions

For completeness, per-hit classification outside the W1 cluster:

- **Line 48 ("Concrete verification on M_2(C)^sa: For p = P_0 = |0><0|, p^perp = P_1 = |1><1|")**: VAL. Step 1 abstract statement on lines 42-46 establishes `C_p + C_{p^perp} = pinching = id − P_1(p)` in the abstract OUS setting (citing Alfsen-Shultz). The M_2(C)^sa computation that follows is labeled "concrete verification" and confirms the abstract identity in the specific model. Classification: **validation example (no fail)**.
- **Line 82 ("Concrete form on M_2(C)^sa")**: VAL. Same pattern — abstract definition of P_{01}(b) from compressions (lines 74-80) is immediately illustrated on M_2(C)^sa. Classification: **validation example (no fail)**.
- **Line 119**: **MNC (proof-device)**, part of W1.
- **Lines 218-222 ("Eq. (04-06.4) says that in M_2(C)^sa: a & b = sqrt(a) b sqrt(a), where the matrix product on the right is the CONCRETE REALIZATION")**: VAL. The text explicitly labels it "CONCRETE REALIZATION of the abstract formula" and "The abstract OUS formula is Eq. (04-06.4), which uses only compressions and Peirce projections." This is correctly framed as validation. Classification: **validation example (no fail)**.

**W2 verdict:** Outside the W1 cluster, M_2(C)^sa mentions are all validation-example framing. Lines 48, 82, 218, 222 do NOT independently fail the audit. The failure is isolated to W1 (lines 119-163).

### Watchpoint W3: Paper 5 §3.3 line 547-554 inherited spin-factor Schur-complement positivity argument

The question per PLAN.md is whether the "spin factor + Schur complement" argument in Paper 5 main-jmp-submitted.tex §3.3 lines 547-554 is also used in Phase 4-06's derivation of Eq. (04-06.4), or whether it is a Paper-5-§3.3-local argument that Phase 4-06 does NOT inherit.

**Paper 5 §3.3 text (lines 545-552 of main-jmp-submitted.tex):**

> \begin{proof}
> Every pair of orthogonal atoms p_i, p_j in a spectral OUS generates a two-level face isomorphic to a **spin factor**, on which the **Schur complement criterion** gives |f(λ_i, λ_j)| ≤ √(λ_i λ_j). Face effects embed into global effects, so the bound lifts to the full space.
> \end{proof}

**Phase 4-06 text: does `04-peirce-feedback-extension.md` use this?**

Grep:

```
$ grep -n -E "spin factor|Schur|two-level face|two-level spin" derivations/04-peirce-feedback-extension.md
(no hits)
```

No hits on `spin factor`, `Schur`, `two-level face`, or `two-level spin`. Phase 4-06's proof of the positivity bound is the **M_2(C)^sa matrix computation** (lines 125-163), NOT a spin-factor Schur-complement argument.

**W3 verdict — Paper 5 inheritance:**

- Phase 4-06 does NOT use the spin-factor Schur-complement argument. Phase 4-06 uses a (different and also failing) M_2(C)^sa matrix computation.
- Paper 5 §3.3 uses the spin-factor Schur-complement argument — this is a **separate, Paper-5-local proof device**. Paper 5 §3.3 thus has its own pre-Jordan circularity (spin factors are JB-algebras; invoking "generates a face isomorphic to a spin factor" as a proof step uses post-Jordan structure).
- The two derivations arrive at the same abstract bound `|f(λ_i, λ_j)| ≤ √(λ_i λ_j)` by different proof devices, **both of which are pre-Jordan-illegal** under the forbidden-token list.

**Implication for Phase 54 scope:** Phase 4-06's failure is independent of the Paper 5 §3.3 spin-factor failure — both fail, but the failure mechanisms are different. Phase 4-06 cannot be rehabilitated by adopting the Paper 5 §3.3 argument (that one also fails). The Paper 5 §3.3 positivity-bound Proposition \ref{prop:pos-bound} has its own circularity issue (spin-factor proof device) that is **outside Phase 54's scope per CONTEXT.md** — Phase 54 is specifically the Peirce-preservation claim (lines 508-528), not the positivity bound (lines 534-552). The positivity-bound issue is noted here and flagged for a separate Paper 5 issue that a future phase must address.

**W3 summary:** Phase 4-06's Eq. (04-06.4) derivation does NOT inherit Paper 5's spin-factor Schur-complement argument. Phase 4-06's W1 failure is independent and self-contained. The Paper 5 §3.3 positivity-bound spin-factor failure is a **separate Paper 5 issue outside Phase 54 scope** (to be flagged in RESULT.md and addressed in a later phase).

---

## Section 5: Binary Verdict

**VERDICT: AUDIT-FAILS**

**First failing step:** Line 119 (and continuing through line 163) — **Theorem (Positivity bound on f)** and its proof.

**Failure classification:** **M_n(ℂ)-level proof device** (FAIL per PLAN.md test-audit-step-trace column "M_n(ℂ)-level proof device" → AUDIT-FAILS).

**Failure mechanism (brief):** The positivity bound Eq. (04-06.2), which is the foundational constraint from which Eq. (04-06.4) is selected by self-modeling faithfulness, is proved only inside M_2(C)^sa using matrix structure (off-diagonal entries, 2×2 determinant, PSD in matrix form, rank-1 projector saturation). No abstract-OUS proof is given. Under the conservative rule (ambiguous → FAIL, per PLAN.md fp-audit-ambiguous-verdict), this is unambiguous: the theorem statement is explicitly scoped to M_2(C)^sa, the proof header explicitly says "(M_2(C)^sa, two-projector case)", and no separate abstract proof appears. Eq. (04-06.4) inherits the failure.

**Is the failure in compression algebra or in non-compression machinery?**

Looking at step 11 of the step-by-step trace: the FAILING step (line 125-163) uses **matrix structure of M_2(C)^sa**, NOT A-S compression algebra. The A-S compression axioms (`C_p^2 = C_p`, `C_p + C_{p'} = pinching`, `C_p(p) = p`, `C_{p_i} C_{p_j} = 0` for orthogonal i≠j) do NOT appear in the failing proof. The failure is in matrix-level PSD reasoning, not in compression algebra.

This means the failure is in **non-compression-algebra machinery** (M_n(C) matrix PSD), which matches `option-b-fails-compression` in the PLAN.md Task 2 decision menu (AUDIT-FAILS with failure in non-compression step).

---

## Section 6: Routing Consequence

**Because VERDICT = AUDIT-FAILS:**

Per PLAN.md fp-audit-ambiguous-verdict and CONTEXT.md Decisions §(A) attempt strategy audit-fail case:

> "If Phase 4-06 audit FAILS: single (A) attempt using non-4-06 route (compression combinatorics), then pivot to (C-i). Subject to the 'audit-FAIL pause' trigger — the failure trace may argue for skipping (A) entirely and going straight to (C-i) if the circularity is specifically compression-algebra."

**The failure trace in this audit is in M_n(C) matrix PSD machinery, NOT in compression algebra.** Therefore:

- Plan 54-02 MAY NOT seed attempt-01 from Eq. (04-06.4).
- Plan 54-02 runs a single non-4-06 (A) attempt via compression combinatorics (Approach 2 in 54-RESEARCH.md §Standard Approaches).
- If that single (A) attempt fails, pivot to (C-i).

**Default routing: `option-b-fails-compression`** — AUDIT-FAILS with failure in non-compression step; single non-4-06 (A) attempt via compression combinatorics, then pivot to (C-i) if that fails. The `option-c-fails-compression-algebra` route (direct pivot to (C-i)) is NOT mandatory because the failure is in M_n(C) matrix machinery, not in compression algebra — compression combinatorics remains a viable, un-foreclosed (A) route.

**PAUSE REQUIRED** per CONTEXT.md stop/rethink #2. Plan 54-01 Task 2 is the checkpoint at which the user confirms routing.

**Separate Paper 5 issue to flag in RESULT.md (outside Phase 54 scope):** Paper 5 §3.3 main-jmp-submitted.tex lines 545-552 contains an independent pre-Jordan-illegal proof device — the "spin factor + Schur complement" argument for the positivity bound in Proposition \ref{prop:pos-bound}. This is NOT inherited by Phase 4-06 (Phase 4-06 uses its own, differently-failing M_2(C)^sa matrix computation instead). But the Paper 5 §3.3 positivity bound proof is itself circular and must be addressed in a subsequent Paper 5 revision phase (the positivity bound is NOT in Phase 54's scope, but the defect is now formally recorded for downstream phases).

---

## Section 7: Routing Decision Placeholder (for Task 2)

Task 2 of this plan (Plan 54-01) is a `checkpoint:decision` at which the user selects one of:

- **option-a-passes** (AUDIT-PASSES; this audit rejects this option)
- **option-b-fails-compression** (AUDIT-FAILS, failure in non-compression step; single non-4-06 (A) attempt then (C-i)) — **recommended by this audit**
- **option-c-fails-compression-algebra** (AUDIT-FAILS, failure specifically in A-S compression algebra; direct pivot to (C-i)) — **not recommended by this audit because the failure is in M_n(C) matrix PSD, not in compression algebra**

This audit recommends **option-b-fails-compression**. The user's selection will be recorded below this line by Task 2.

### User Decision Record (populated by Task 2)

```
Selected option: <to be filled by Task 2 checkpoint>
Selected at:    <timestamp>
Plan 54-02 attempt strategy: <populated upon resume>
```

---

## Section 8: Audit Summary

- Forbidden-token grep performed on `derivations/04-peirce-feedback-extension.md`; all hits classified per-line (Section 2.2-2.5). No `Jordan`, `EJA`, `pxp`, `h_n`, `operator product`, `spin factor`, or primitive `f(λ,μ) = √(λμ)` tokens appear.
- `M_2(C)^sa` appears extensively, mostly as validation examples (Steps 1, 2, 5, 10) — BUT the **positivity bound Theorem (line 119) and its proof (line 125-163) use M_2(C)^sa as a proof device**, not a validation example.
- Step-by-step classification table (Section 3) identifies rows #10 and #11 as M_n(ℂ)-level proof device. Row #14 (Eq. (04-06.4)) inherits the failure through dependency on the positivity bound.
- Watchpoint W1 (line 125): **FAIL** — proof device, not validation example.
- Watchpoint W2 (lines 48, 82, 218, 222): VAL (no independent fail).
- Watchpoint W3 (Paper 5 line 547-554): Phase 4-06 does NOT inherit Paper 5's spin-factor argument. Paper 5 has its own separate positivity-bound failure (outside Phase 54 scope).
- **Binary verdict: AUDIT-FAILS**, first failing step at line 119-163 (positivity bound Theorem + Proof).
- **Recommended routing:** `option-b-fails-compression` — single non-4-06 (A) attempt via compression combinatorics in Plan 54-02, then pivot to (C-i) if that fails.

---

_Auditor: gpd-executor (Phase 54-01 Task 1). Audit target: commit 9608ac54 (plan-closing) / 6391f0d3 (derivation file creation). Audit date: 2026-04-16._
