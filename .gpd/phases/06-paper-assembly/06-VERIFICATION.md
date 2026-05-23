---
phase: 06-paper-assembly
verified: 2026-03-21T22:00:00Z
status: gaps_found
score: 8/10 contract targets verified
consistency_score: 10/12 physics checks passed
independently_confirmed: 6/12 checks independently confirmed
confidence: medium
gaps:
  - subject_kind: claim
    subject_id: claim-axiom-exposition
    expectation: "S6 and S7 proof sketches in Section 4 must verify the SAME axioms stated in Definition 2 (Section 2.3)"
    expected_check: "Axiom statements in Section 4 match Definition 2"
    status: failed
    category: math_consistency
    reason: >
      Section 4 restates S6 as first-argument additivity for compatible effects
      ("If sp(a,1)=a, then sp(a+b,c)=sp(a,c)+sp(b,c)") and S7 as "sp(a,b) = a circ b
      for compatible a,b". These do NOT match Definition 2 in Section 2.3, which states
      S6 as "If a|b then a|(1-b); if also a|c then a|(b+c)" (additivity of the
      compatibility relation) and S7 as "If a|b and a|c then a|(b.c)" (multiplicativity
      of compatibility). The proofs verify different properties than what is needed.
      The properties proven may imply the actual S6/S7 or be equivalent on EJAs, but
      this equivalence is not stated or proved.
    computation_evidence: >
      Direct comparison of axiom text: Definition 2 lines 269-275 of main.tex vs
      axiom-verification.tex lines 183-215. The two formulations are syntactically and
      semantically different. Def 2 S6 is about COMPATIBILITY being closed under
      complement/sum; Sec 4 S6 is about the PRODUCT being additive in the first argument.
      Def 2 S7 is about COMPATIBILITY being closed under the sequential product;
      Sec 4 S7 is about the PRODUCT equaling the Jordan product for compatible effects.
    artifacts:
      - path: paper/sections/axiom-verification.tex
        issue: "S6 statement (lines 185-188) and S7 statement (lines 202-204) do not match Definition 2 in main.tex (lines 269-275)"
    missing:
      - "Correct the S6 proof sketch to verify that compatibility is closed under complement and sum"
      - "Correct the S7 proof sketch to verify that compatibility is closed under the sequential product"
      - "Or prove that the stated properties are equivalent to S6/S7 on finite-dimensional spectral OUS"
    severity: significant

  - subject_kind: deliverable
    subject_id: deliv-bib
    expectation: "Bibliography entries have correct publication data"
    expected_check: "DOIs, journals, and page numbers match actual publications"
    status: failed
    category: literature_agreement
    reason: >
      Two bibliography errors found: (1) vandeWetering2019 lists journal as J. Math. Phys.
      but the paper was actually published in Compositionality. (2) vandeWetering2019b
      has DOI 10.1063/1.5093063 but the actual DOI appears to be 10.1063/1.5093504.
    computation_evidence: >
      Web search confirms: "An effect-theoretic reconstruction of quantum theory"
      (arXiv:1801.05798) was published in Compositionality vol 1, 2019, not J. Math. Phys.
      "Sequential product spaces are Jordan algebras" (arXiv:1803.11139) DOI per AIP
      Publishing is 10.1063/1.5093504, not the 10.1063/1.5093063 in refs.bib.
    artifacts:
      - path: paper/refs.bib
        issue: "vandeWetering2019 wrong journal; vandeWetering2019b wrong DOI"
    missing:
      - "Fix vandeWetering2019 to cite Compositionality vol 1 (2019)"
      - "Fix vandeWetering2019b DOI to 10.1063/1.5093504"
    severity: minor

comparison_verdicts:
  - subject_kind: claim
    subject_id: claim-type-exclusion-exposition
    reference_id: ref-barnum-wilce
    comparison_kind: benchmark
    verdict: pass
    metric: "dimension_counting_algebra"
    threshold: "exact match"
  - subject_kind: claim
    subject_id: claim-sp-construction-exposition
    reference_id: ref-vdw2018
    comparison_kind: benchmark
    verdict: pass
    metric: "Luders_product_equivalence_on_M2C"
    threshold: "machine_epsilon"

suggested_contract_checks:
  - check: "Verify S6/S7 as stated in Def 2 hold for the corrected product"
    reason: "Section 4 proves different properties than what Def 2 S6/S7 require"
    suggested_subject_kind: acceptance_test
    suggested_subject_id: "test-s6s7-correct-axioms"
    evidence_path: "paper/sections/axiom-verification.tex"
---

# Phase 6 Verification: Paper Assembly

**Phase Goal:** Paper 5 is assembled as a complete, self-contained, publication-ready manuscript presenting the full chain (L4 -> QM with one premise).

**Verified:** 2026-03-21
**Status:** gaps_found
**Confidence:** MEDIUM
**Score:** 8/10 contract targets verified

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|---------|
| claim-paper-opening | claim | VERIFIED | INDEPENDENTLY CONFIRMED | main.tex Sections 1-2: abstract states result, comparison table present, 4 assumptions listed |
| claim-sp-construction-exposition | claim | VERIFIED | INDEPENDENTLY CONFIRMED | main.tex Section 3: complete narrative from OUS through corrected product, circularity check included |
| claim-axiom-exposition | claim | PARTIAL | STRUCTURALLY PRESENT | axiom-verification.tex: S1-S5 correctly stated and proved; **S6-S7 misstated** (see gap) |
| claim-lt-exposition | claim | VERIFIED | INDEPENDENTLY CONFIRMED | composite-lt.tex: composite def, product-form SP, correlation form, non-degeneracy, LT theorem, entangled sector addressed |
| claim-type-exclusion-exposition | claim | VERIFIED | INDEPENDENTLY CONFIRMED | type-exclusion.tex: all 5 types addressed, 3-theorem chain with hypothesis tables, involution exhibited, main theorem stated |
| claim-discussion | claim | VERIFIED | STRUCTURALLY PRESENT | discussion.tex: 4 assumptions analyzed, 4 competitors compared in depth, 5 future directions, 5 referee objections |
| claim-manuscript-complete | claim | VERIFIED | STRUCTURALLY PRESENT | All 7 sections + 2 appendices + figure + bibliography assembled in main.tex |
| claim-no-circularity | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Circularity audit: no Hilbert/C*/density-matrix imports in Secs 1-5 (all mentions are disclaimers) |
| deliv-bib | deliverable | PARTIAL | STRUCTURALLY PRESENT | All cited keys have bib entries; 2 unused entries; **2 bibliographic errors** (see gap) |
| deliv-chain-figure | deliverable | VERIFIED | INDEPENDENTLY CONFIRMED | derivation-chain.tex: TikZ figure with 8 nodes, novel/published color coding, assumption annotations |

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| paper/main.tex | Complete manuscript | VERIFIED | 607 lines, all sections input'd, abstract + 7 sections + 2 appendices |
| paper/preamble.sty | Notation macros | VERIFIED | 104 lines, theorem environments, sp/jp/comp/peirce/eff macros |
| paper/refs.bib | Bibliography | PARTIAL | 253 lines, 24 entries, 22 cited; 2 bibliographic data errors |
| paper/sections/axiom-verification.tex | Section 4 | PARTIAL | S1-S5 correct; S6-S7 axiom statements do not match Definition 2 |
| paper/sections/composite-lt.tex | Section 5 | VERIFIED | Composite def, product-form SP, correlation form, LT theorem |
| paper/sections/type-exclusion.tex | Section 6 | VERIFIED | Type exclusion, C*-promotion, involution, main theorem |
| paper/sections/discussion.tex | Section 7 | VERIFIED | Assumptions, competitors, future directions, objections, conclusion |
| paper/sections/appendix-proofs.tex | Appendix A | VERIFIED | Full S4 proof + local tomography proof |
| paper/sections/appendix-numerical.tex | Appendix B | VERIFIED | 844+ SymPy tests documented, Phase 4 + Phase 5 coverage |
| paper/figures/derivation-chain.tex | Figure 1 | VERIFIED | TikZ derivation chain, 8 nodes, color-coded novel vs published |

## Computational Verification Details

### Spot-Check Results

| Expression | Test Point | Computed | Expected | Match |
|-----------|-----------|---------|----------|-------|
| Luders vs corrected product on M_2(C)^sa | 10 random effect pairs | max error 1.11e-16 | 0 | PASS |
| S3 unitality sp(1,b)=b | 5 random effects | max error 0.00e+00 | 0 | PASS |
| S4 orthogonality symmetry | orthogonal projections p1,p2 | sp(p1,p2)=0, sp(p2,p1)=0 | both 0 | PASS |
| Non-associativity | generic triple (a,b,c) | delta=0.0046 | nonzero | PASS |

### Limiting Cases Re-Derived

| Limit | Parameter | Expression Limit | Expected | Agreement | Confidence |
|-------|----------|-----------------|----------|-----------|------------|
| Real n=2 dim counting | n=2, K=R | d=3, d^2=9, comp=10 | 9 != 10 | PASS | INDEPENDENTLY CONFIRMED |
| Complex n=2 dim counting | n=2, K=C | d=4, d^2=16, comp=16 | 16 = 16 | PASS | INDEPENDENTLY CONFIRMED |
| Quaternionic n=2 dim counting | n=2, K=H | d=6, d^2=36, comp=28 | 36 != 28 | PASS | INDEPENDENTLY CONFIRMED |
| Real exclusion algebra | (n+1)^2 = 2(n^2+1) | n=0 or n=1 | only n=1 trivial | PASS | INDEPENDENTLY CONFIRMED |
| Quaternionic exclusion algebra | (2n-1)^2 = 2n^2-1 | n=0 or n=1 | only n=1 trivial | PASS | INDEPENDENTLY CONFIRMED |
| Complex multiplicative stability | d=n^2, d^2=n^4 | n^4 = n^4 for all n | always true | PASS | INDEPENDENTLY CONFIRMED |

### Cross-Checks Performed

| Result | Primary Method | Cross-Check Method | Agreement |
|--------|---------------|-------------------|-----------|
| Corrected product = Luders on M_2(C)^sa | Formula (eq:corrected-product) | numpy eigendecomposition + matrix multiplication | PASS (error < 1e-15) |
| Dimension formulas | Paper's algebraic exclusion | Sympy solve() for n | PASS (solutions match) |

## Physics Consistency

| Check | Status | Confidence | Notes |
|-------|--------|------------|-------|
| 5.1 Dimensional analysis | N/A | N/A | Algebraic project, no physical dimensions |
| 5.2 Numerical spot-check | PASS | INDEPENDENTLY CONFIRMED | 10 random Luders vs corrected product comparisons on M_2(C)^sa; all agree to machine epsilon |
| 5.3 Limiting cases | PASS | INDEPENDENTLY CONFIRMED | All dimension formulas verified for n=1,2,3,4 across R,C,H; algebraic exclusion equations solved symbolically |
| 5.6 Symmetry (S4) | PASS | INDEPENDENTLY CONFIRMED | Orthogonality symmetry verified numerically; full proof in Appendix A |
| 5.7 Conservation (unitality S3) | PASS | INDEPENDENTLY CONFIRMED | sp(1,b)=b verified numerically to machine precision |
| 5.8 Math consistency | PARTIAL | STRUCTURALLY PRESENT | S1-S5 proofs consistent; **S6-S7 statements do not match Definition 2** |
| 5.10 Literature agreement | PARTIAL | STRUCTURALLY PRESENT | All key published theorems cited with hypothesis verification tables; **2 bib data errors** |
| 5.11 Physical plausibility | PASS | INDEPENDENTLY CONFIRMED | Non-associativity confirmed (delta=0.0046); complex type uniquely survives LT |
| Gate A: Catastrophic cancellation | N/A | N/A | No numerical results with potential cancellation |
| Gate B: Analytical-numerical cross-validation | PASS | INDEPENDENTLY CONFIRMED | Corrected product formula matches numerical Luders computation |
| Gate C: Integration measure | N/A | N/A | No coordinate transformations |
| Gate D: Approximation validity | N/A | N/A | No approximations (exact algebraic proofs) |

### Paper-Writing Profile Checks

| Check | Status | Notes |
|-------|--------|-------|
| Equations match derivations | PASS | Corrected product (eq:corrected-product) matches Phase 4 formula |
| Notation consistent throughout | PASS | sp, comp, peirce, eff macros used consistently (100, 34, 14, 13 uses respectively) |
| All symbols defined | PASS | Definition environments for OUS, effect space, compression, Peirce decomposition, sequential product |
| References exist in bib | PASS | All 22 cited keys have bib entries |
| Section structure complete | PASS | Abstract + 7 sections + 2 appendices + bibliography + figure |
| Comparison table present | PASS | Table 1 compares 7 programs including this work |
| Main theorem formally stated | PASS | Theorem 6.4 (self-modeling implies complex QM) |
| Assumptions explicitly numbered | PASS | Assumptions 1-4 formally stated in main.tex and composite-lt.tex |
| Circularity audit | PASS | No C*/Hilbert imports before Section 6; all mentions are disclaimers |
| Referee objections addressed | PASS | 5 objections in Remarks 7.1-7.5 |

## Forbidden Proxy Audit

| Proxy | Status | Evidence |
|-------|--------|---------|
| Paper assumes C* without acknowledging as additional premise | REJECTED | Abstract and Section 1 explicitly state "four standing structural assumptions"; C* emerges as consequence in Section 6 |
| Overclaiming scope | REJECTED | Abstract: "finite-dimensional"; Discussion: "most restrictive assumption"; all 4 assumptions analyzed |
| Paper without self-contained logical chain | REJECTED | Derivation chain figure (Fig. 1) + main theorem proof outline (Theorem 6.4) trace complete chain |

## Comparison Verdict Ledger

| Subject | Comparison Kind | Verdict | Threshold | Notes |
|---------|----------------|---------|-----------|-------|
| Dimension counting (R, n=2) | benchmark | PASS | exact | 3^2=9 vs comp=10, paper says 9<10 |
| Dimension counting (C, n=2) | benchmark | PASS | exact | 4^2=16 vs comp=16, paper says 16=16 |
| Dimension counting (H, n=2) | benchmark | PASS | exact | 6^2=36 vs comp=28, paper says 36!=28 |
| Luders equivalence | cross-method | PASS | < 1e-12 | Corrected product = sqrt(a)b*sqrt(a) to machine epsilon |
| Non-associativity | existence | PASS | nonzero | delta = 0.0046 for generic triple |

## Discrepancies Found

| Severity | Location | Evidence | Root Cause | Fix |
|----------|----------|----------|------------|-----|
| SIGNIFICANT | axiom-verification.tex S6 (lines 183-197) | Sec 4 S6 statement differs from Def 2 S6 | Axiom was restated as a different property during exposition | Rewrite S6 proof to verify compatibility closure under complement and sum |
| SIGNIFICANT | axiom-verification.tex S7 (lines 200-215) | Sec 4 S7 statement differs from Def 2 S7 | Axiom was restated as Jordan product equality instead of compatibility multiplicativity | Rewrite S7 proof to verify compatibility closure under sequential product |
| MINOR | refs.bib vandeWetering2019 | Wrong journal (says JMP, actually Compositionality) | Likely copy error from vandeWetering2019b entry | Fix journal to Compositionality vol 1 (2019) |
| MINOR | refs.bib vandeWetering2019b | DOI 10.1063/1.5093063 appears incorrect | Web search suggests correct DOI is 10.1063/1.5093504 | Verify and correct DOI |

## Requirements Coverage

| Requirement | Status | Notes |
|-------------|--------|-------|
| PAPR-01: Paper 5 manuscript | PARTIAL | Manuscript assembled and largely correct; S6/S7 exposition needs correction |

## Anti-Patterns Found

| Category | Location | Impact |
|----------|----------|--------|
| INFO | refs.bib: 2 unused entries (AlfsenShultz2001, ThisWork) | No physics impact; cleanup for submission |
| INFO | main.tex line 12: "[Authors]" placeholder | Must be filled before submission |
| INFO | main.tex line 587: "[To be added.]" acknowledgments | Must be filled before submission |

## Expert Verification Required

| Check | Expected | Domain | Why Expert |
|-------|----------|--------|-----------|
| S6/S7 equivalence on finite-dim spectral OUS | The properties proved in Section 4 may be equivalent to the actual vdW S6/S7 on this class of spaces | Algebraic quantum foundations | Requires knowledge of whether compatibility closure follows from the proved properties on EJAs; a subtle algebraic question |
| Hypothesis verification for Barnum-Wilce Theorem 4.1 | Spin factors V_n (n>=4) admit no locally tomographic composite | GPT compositionality | The paper invokes this as a black box; verifying the hypothesis match requires reading Barnum-Wilce carefully |
| vdW Theorem 3 hypothesis match | The composite constructed satisfies all hypotheses of vdW Thm 3 | Sequential product theory | The paper provides a hypothesis verification table but expert should confirm the "locally tomographic" hypothesis is exactly the right version |

## Confidence Assessment

Overall confidence is MEDIUM for the following reasons:

**Strengths (supporting HIGH):**
1. The logical chain from self-modeling to C*-algebra is complete and well-structured
2. All dimension counting claims verified computationally to exact values
3. The Luders-corrected product equivalence verified to machine epsilon
4. Circularity audit passes cleanly -- no C*/Hilbert imports before Section 6
5. All four standing assumptions explicitly stated, numbered, and discussed
6. Comparison table and referee objection handling are thorough
7. The derivation chain figure correctly identifies novel vs published contributions

**Weaknesses (preventing HIGH):**
1. **S6/S7 axiom statements in Section 4 do not match Definition 2** -- this is the most significant finding. The paper claims to verify S1-S7 per vdW Definition 2, but Section 4 actually verifies different properties for S6 and S7. The true vdW S6 (compatibility closed under complement/sum) and S7 (compatibility closed under sequential product) may follow from the properties that were proved, but this equivalence is not stated or demonstrated.
2. Two bibliography errors (wrong journal for one entry, wrong DOI for the central reference)
3. Could not access the vdW paper directly to confirm the exact axiom formulations, though the paper's own Definition 2 is internally consistent and the discrepancy between Definition 2 and Section 4 is clear

## Gaps Summary

Two gaps were identified:

**Gap 1 (SIGNIFICANT): S6/S7 Axiom Mismatch.** The paper's own Definition 2 (Section 2.3, main.tex lines 269-275) correctly states S6 and S7 as properties of the compatibility relation. But the "verification" in Section 4 (axiom-verification.tex) proves different properties -- first-argument additivity (S6) and Jordan product equality (S7) for compatible effects. These are related but not identical to the actual axioms. The fix is either: (a) rewrite the Section 4 S6/S7 proofs to verify the correct axioms, or (b) prove that the stated properties are equivalent to S6/S7 on finite-dimensional spectral OUS. Root cause: the axiom statements were paraphrased during exposition and the paraphrasing changed the mathematical content.

**Gap 2 (MINOR): Bibliography Errors.** vandeWetering2019 cites the wrong journal (J. Math. Phys. instead of Compositionality), and vandeWetering2019b has an incorrect DOI. These are data errors that do not affect the physics but should be corrected before submission.
