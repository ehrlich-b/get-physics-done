# Consistency Check: Phase 6 (Paper Assembly)

**Mode:** Rapid
**Phase checked:** 06-paper-assembly (Plans 01-03)
**Checked against:** Full conventions ledger, Phase 4 (04-01 through 04-04, 04-06), Phase 5 (05-01, 05-02)
**Date:** 2026-03-21

---

## Convention Compliance Matrix

| Convention | Introduced | Relevant? | Compliant? | Evidence | Notes |
|---|---|---|---|---|---|
| Sequential product: `a & b` (internal) / `a . b` (paper) | Phase 4 | Yes | YES | `\sp{a}{b}` macro renders `a . b` throughout; zero `\&` in math mode; derivation files use `&` notation internally | Deliberate convention change for paper: `&` in derivations, dot in paper. Documented in 06-01-SUMMARY. |
| Jordan product: `a * b` (internal) / `a circ b` (paper) | Phase 4 | Yes | YES | `\jp{a}{b}` macro renders `a \circ b`; used in composite-lt.tex Eq. (5.2), axiom-verification.tex S7 | Consistent |
| Compression: `C_p` | Phase 4 | Yes | MINOR ISSUE | `\comp{p}` macro used in main.tex and appendix-proofs.tex; raw `C_{p_i}` used throughout axiom-verification.tex | See Issue 1 below |
| Axiom source: arXiv:1803.11139 Def 2 EXCLUSIVELY | Phase 4 | Yes | ISSUE | S1-S5 match vdW Def 2; S6 and S7 blockquotes in axiom-verification.tex do NOT match the formal Def 2.3 stated in main.tex | See Issue 2 below |
| Corrected product formula | Phase 4, Plan 06 | Yes | YES | Eq. (04-06.4) matches paper Eqs. (3.6) and (4.1) exactly | `sum lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b)` |
| Composite product: `(a tensor b) & (c tensor d)` | Phase 5, Plan 01 | Yes | YES | Eq. (05-01.1) matches paper Eq. (5.1) | Product-form SP consistent |
| Local tomography: `dim(V_BM) = dim(V_B) * dim(V_M)` | Phase 5, Plan 01 | Yes | YES | Eq. (05-01.5) matches paper Theorem 5.1 | Consistent |
| Correlation form: `B(a,b) = tau(a * phi^{-1}(b))` | Phase 5, Plan 01 | Yes | YES | Eq. (05-01.4) matches paper Definition 5.3 Eq. (5.2) | Consistent |
| Dimensionless algebraic quantities | Phase 4 | Yes | YES | No unit conversions needed; all quantities are algebraic | N/A for this project type |

### Standard Convention Types (18 canonical)

All 18 standard QFT conventions (metric signature, Fourier, natural units, gauge choice, etc.) are correctly marked N/A in both CONVENTIONS.md and preamble.sty. This is an algebraic/categorical project with no spacetime, field theory, or dimensional quantities. No issues.

---

## Provides/Consumes Verification

### Phase 4 -> Phase 6 transfers

| Quantity | Producer | Consumer | Meaning Match | Formula Match | Convention Match | Status |
|---|---|---|---|---|---|---|
| Corrected product formula (Eq. 04-06.4) | Phase 4, Plan 06 | Paper Eqs. (3.6), (4.1) | YES | YES | YES (& -> dot notational) | OK |
| S1-S7 proofs | Phase 4, Plans 03-04 | Paper Section 4 | YES | YES | ISSUE (S6, S7 statements) | Issue 2 |
| S4 proof (facial orthogonality) | Phase 4, Plan 04 | Paper Section 4 + Appendix A | YES | YES | YES | OK |
| EJA classification (vdW Thm 1) | Phase 4, Plan 04 | Paper Theorem 4.2 | YES | YES | YES | OK |
| Non-associativity confirmation | Phase 4, Plan 02 | Paper Remark after Thm 4.2 | YES | N/A (cited) | YES | OK |
| Positivity bound | Phase 4, Plan 06 | Paper Proposition 3.1 | YES | YES | YES | OK |
| Faithful selection principle | Phase 4, Plan 06 | Paper Proposition 3.2 | YES | YES | YES | OK |

### Phase 5 -> Phase 6 transfers

| Quantity | Producer | Consumer | Meaning Match | Formula Match | Convention Match | Status |
|---|---|---|---|---|---|---|
| Local tomography (Eq. 05-01.5) | Phase 5, Plan 01 | Paper Theorem 5.1 | YES | YES | YES | OK |
| Composite OUS definition | Phase 5, Plan 01 | Paper Definition 5.1 (C1-C4) | YES | YES | YES | OK |
| Product-form SP (Eq. 05-01.1) | Phase 5, Plan 01 | Paper Eq. (5.1) | YES | YES | YES (& -> dot) | OK |
| Correlation form (Eq. 05-01.4) | Phase 5, Plan 01 | Paper Eq. (5.2) | YES | YES | YES | OK |
| S1-S7 inheritance | Phase 5, Plan 01 | Paper Proposition 5.1 | YES | YES | YES | OK |
| Non-degeneracy of trace form | Phase 5, Plan 01 | Paper Proposition 5.2 | YES | YES | YES | OK |
| Dimension mismatch (R: 9!=10, H: 36!=28) | Phase 5, Plan 01 | Paper Remark 5.5 | YES | YES | YES | OK |
| Type exclusion (all five types) | Phase 5, Plan 02 | Paper Section 6.2 | YES | YES | YES | OK |
| C*-promotion (three-theorem chain) | Phase 5, Plan 02 | Paper Section 6.3 | YES | YES | YES | OK |
| Involution P1-P4 | Phase 5, Plan 02 | Paper Section 6.4 | YES | YES | YES | OK |

---

## Issues Found

### Issue 1: Inconsistent compression macro usage (MINOR)

**Severity:** Minor (cosmetic, does not affect correctness)

**Description:** The `\comp{p}` macro (defined in preamble.sty, expanding to `C_p`) is used in main.tex (17 instances) and appendix-proofs.tex (11 instances), but axiom-verification.tex uses raw `C_{p_i}` notation throughout (15+ instances, zero `\comp` usage). The rendered output is identical (`C_p`), so this is a maintainability issue, not a correctness issue.

**Impact:** If the compression notation is ever changed (e.g., to `U_p`), axiom-verification.tex would need manual updates while other sections would update automatically via the macro.

**Recommended fix:** Replace raw `C_{p_i}` with `\comp{p_i}` in axiom-verification.tex for consistency with the rest of the manuscript.

### Issue 2: S6 and S7 axiom statements in axiom-verification.tex do not match Definition 2.3 in main.tex (SIGNIFICANT)

**Severity:** Significant (axiom statement mismatch across paper sections)

**Description:** The formal axiom definitions in main.tex Section 2 (Definition 2.3, lines 255-276) quote vdW arXiv:1803.11139 Definition 2. The proof sketches in axiom-verification.tex quote *different* statements in the blockquotes for S6 and S7:

**S6 discrepancy:**
- **main.tex (Def 2.3):** "Additivity of compatibility: If `a compatible b` then `a compatible (1-b)`; if also `a compatible c` then `a compatible (b+c)` whenever `b+c <= 1`."
  - This is about the *compatibility relation* being closed under complement and addition.
- **axiom-verification.tex (blockquote):** "If `a.1 = a`, then for compatible `a` and `b`: `(a+b).c = a.c + b.c` whenever `a+b <= 1`."
  - This is about *first-argument additivity* of the product for compatible effects.

These are distinct mathematical statements. The first says the set of effects compatible with `a` is closed under complement and finite sums. The second says the product is additive in its first argument for compatible effects.

**S7 discrepancy:**
- **main.tex (Def 2.3):** "Multiplicativity of compatibility: If `a compatible b` and `a compatible c` then `a compatible (b.c)`."
  - This says compatibility is closed under the sequential product.
- **axiom-verification.tex (blockquote):** "For compatible `a` and `b`: `a.b = a circ b` (the Jordan product)."
  - This says the sequential product *equals* the Jordan product for compatible effects.

Again, distinct statements. The first is about closure of compatibility. The second is an identity relating the sequential product to the Jordan product.

**Analysis:** Both the statements in main.tex AND the statements in axiom-verification.tex are valid properties that appear in vdW's work. However, the specific axiom labels S6 and S7 as defined in vdW arXiv:1803.11139 Definition 2 correspond to the statements in main.tex Definition 2.3. The statements in axiom-verification.tex are *consequences* or *related properties* but are not the literal S6/S7 axioms.

The Phase 4, Plan 03 summary confirms the proofs address the correct content (compatibility closure properties), but the paper's axiom-verification section quotes incorrect axiom statements in the blockquotes.

**Impact:** A referee comparing the blockquoted axiom statements in Section 4 against the formal Definition 2.3 in Section 2 would notice the discrepancy. The proofs themselves may be proving the correct properties (the proof sketch for S6 discusses `a.1 = a` which is relevant to the actual S6, and the proof for S7 discusses functional calculus which is relevant to the actual S7), but the *stated* axioms being proved do not match the *defined* axioms.

**Recommended fix:** Replace the S6 and S7 blockquote statements in axiom-verification.tex with the verbatim statements from Definition 2.3 in main.tex:

- S6 blockquote should read: "If `a compatible b` then `a compatible (1-b)`; if also `a compatible c` then `a compatible (b+c)` whenever `b+c <= 1`."
- S7 blockquote should read: "If `a compatible b` and `a compatible c` then `a compatible (b.c)`."

Then adjust the proof sketches to directly address these statements rather than the related properties currently stated.

---

## Convention Evolution

No convention changes between Phase 4/5 (derivation) and Phase 6 (paper) beyond the documented notation switch:
- Internal notation: `a & b` for sequential product
- Paper notation: `a . b` (dot) via `\sp{a}{b}` macro

This change is documented in 06-01-SUMMARY ("Dot notation (\\sp{a}{b} -> a . b) used throughout. The & notation does not appear in the paper.") and is consistent across all paper sections.

---

## Spot-Check: Load-Bearing Equations

### Check 1: Corrected product formula

**Phase 4 source (Eq. 04-06.4):**
`a & b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b)`

**Paper (Eq. 3.6 / eq:corrected-product):**
`a . b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b)`

**Test value:** For a = 1 (spectral decomposition: single eigenvalue lambda_1 = 1, single projector p_1 = 1):
- Phase 4: 1 & b = 1 * C_1(b) = b (since C_1 = id). Peirce 1-space sum empty. Result: b. [S3 satisfied]
- Paper: 1 . b = 1 * C_1(b) = b. Same. MATCH.

**Test value:** For a = 0:
- Phase 4: 0 & b = 0 * C_1(b) = 0 (single eigenvalue lambda_1 = 0). Result: 0.
- Paper: 0 . b = 0. Same. MATCH.

STATUS: PASS

### Check 2: Local tomography dimension equality

**Phase 5 source (Eq. 05-01.5):** dim(V_BM) = dim(V_B) * dim(V_M)

**Paper (Theorem 5.1):** dim(V_BM) = dim(V_B) * dim(V_M)

**Test value:** For V = V_3 = M_2(C)^sa: dim(V) = 4. dim(V_BM) = 4 * 4 = 16 = dim(M_4(C)^sa). MATCH.

**Negative test (real):** dim(M_2(R)^sa) = 3. 3^2 = 9 != 10 = dim(composite). Paper Remark 5.5 table shows 9 vs 10. MATCH.

**Negative test (quaternionic):** dim(M_2(H)^sa) = 6. 6^2 = 36 != 28 = dim(composite). Paper Remark 5.5 table shows 36 vs 28. MATCH.

STATUS: PASS

### Check 3: Correlation bilinear form

**Phase 5 source (Eq. 05-01.4):** B(a,b) = tau(a * phi^{-1}(b))

**Paper (Definition 5.3, Eq. 5.2):** B(a,b) = tau(a circ phi^{-1}(b))

The `*` in Phase 5 denotes the Jordan product, and `circ` in the paper denotes the same. Consistent notation change (internal `*` -> paper `circ`). Both denote the Jordan product on the EJA.

STATUS: PASS

---

## Cross-Phase Error Pattern Check

| Pattern | Checked? | Found? | Detail |
|---|---|---|---|
| Sign absorbed into definition | Yes | No | No sign-dependent quantities cross phase boundaries |
| Normalization factor change | Yes | No | All normalizations consistent (trace tau normalized to tau(1)=1 across phases) |
| Implicit assumption violated | Yes | No | All four standing assumptions (finite-dim, faithful, minimal, simple) consistently stated in both derivation phases and paper |
| Coupling convention mismatch | N/A | -- | No coupling constants in this algebraic project |
| Factor of 2pi error | N/A | -- | No Fourier transforms or momentum-space quantities |
| Wick rotation sign | N/A | -- | No spacetime formulation |
| Boundary condition mismatch | N/A | -- | No boundary conditions |

---

## Narrative Coherence

- **Problem-method alignment:** YES. The problem (derive QM from self-modeling) is addressed by the method (construct SP, verify axioms, classify algebra).
- **Result-problem alignment:** YES. The main theorem (self-modeling implies M_n(C)^sa) directly answers the research question.
- **Conclusion-evidence alignment:** YES. Conclusions are supported by the 8-step derivation chain, each step either proved or cited with hypothesis verification.
- **Open threads acknowledged:** YES. Discussion Section 7.2 analyzes all four standing assumptions. Section 7.4 lists five future directions. Section 7.5 addresses five anticipated objections.

---

## Summary

| Metric | Count |
|---|---|
| Provides/consumes pairs verified | 17 |
| Convention compliance checks | 10 |
| Spot-checks performed | 3 |
| Issues found | 2 |
| -- Significant | 1 (S6/S7 axiom statement mismatch) |
| -- Minor | 1 (compression macro inconsistency) |
| Cross-phase error patterns checked | 7 |
| Cross-phase errors found | 0 |

**Overall assessment:** The Phase 6 paper correctly transfers all key results from Phases 4 and 5. The corrected product formula, local tomography theorem, type exclusion arguments, and C*-promotion chain are all faithfully represented. The sequential product notation change (& -> dot) is consistently applied and documented. The one significant issue is the S6/S7 axiom statement mismatch in axiom-verification.tex, which quotes properties that differ from the formal vdW Definition 2 axioms stated in main.tex Section 2.

---

_Consistency check performed: 2026-03-21_
_Mode: rapid_
_Checker: gpd-consistency-checker_
