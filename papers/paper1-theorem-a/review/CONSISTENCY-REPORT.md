---
reviewed: 2026-03-16T12:00:00Z
scope: panel_consistency_check
---

# Consistency Report: Panel Cross-Check

**Manuscript:** papers/paper1-theorem-a/main.tex
**Panel stages reviewed:** Claims Extraction, Math Soundness, Physics Assessment, Significance Assessment, Literature Context

---

## 1. Panel Agreement Summary

### Areas of Full Agreement (5/5 passes)

1. **The mathematics is sound.** Every pass acknowledges the proof is internally consistent, the lemma composition is correct, and the error tracking is thorough. No pass found a mathematical error that affects the leading-order result.

2. **The title and abstract overclaim.** Every pass flags the gap between "Boltzmann Brain Suppression" in the title and the actual scope of the theorem (finite-state reversible Markov chains). The reader pass (FLAG-1), physics pass (item 1 in recommendations), significance pass (title section), and literature pass (Section 4.1) all converge on this independently.

3. **The experiential density is unmotivated.** The reader pass (CLM-002, FLAG-2), physics pass (Section 1), and significance pass (critical novelty question) all flag that rho is posited without derivation, that it is non-unique, and that the suppression result does not depend on its specific form.

4. **The validation is adequate for the mathematics but insufficient for physical claims.** All passes accept the three-state chain as a correct mathematical benchmark. The significance pass and physics pass both note it is insufficient for physical relevance.

5. **Recommendation ceiling is major_revision.** The reader pass does not issue a formal recommendation but identifies blocking overclaims. The math pass has HIGH mathematical confidence but flags the framing issues. The physics pass caps at major_revision. The significance pass caps at major_revision. The literature pass caps at major_revision. No pass suggests accept or minor_revision is appropriate.

### Areas of Strong Agreement (4/5 passes)

6. **The suppression is from metastability, not from rho.** The physics pass (Section 3.3, point 1), significance pass (section on novelty assessment), and reader pass (CLM-002, observation on "trivial" nature) all independently identify this. The math pass does not flag it as an issue because it is a physics/framing concern outside its scope.

7. **Literature coverage is deficient.** The reader pass, literature pass, significance pass, and physics pass all flag missing references, though the literature pass provides the most comprehensive list. The math pass does not assess literature.

### Areas of Partial Disagreement

8. **Severity of the gamma = alpha/2 error.** The math pass calls this a "MINOR ERROR" that is "a one-line fix" and confirms it does not affect the leading-order result. The reader pass does not identify it (it is a technical detail). The other passes do not address it. I agree with the math pass: this is minor. The error bound is claimed to be tighter than what the proof establishes in a corner of parameter space, but the stated bound remains valid where it matters (the leading exponential is unaffected).

9. **Venue fit.** The significance pass recommends arXiv or JMP, considers PRD/JCAP inappropriate without major extensions, and explicitly rejects PRL. The physics pass says the math is solid but recommends "reframing as a mathematical result." The literature pass does not make a venue recommendation. The reader pass and math pass do not address venue. I concur with the significance pass: JMP is the most natural venue after reframing; PRD/PRL are inappropriate in the current form.

### No Disagreements Found Between Panel Members

No two passes make contradictory factual claims. The strongest asymmetry is that the math pass gives HIGH confidence and focuses on the correctly done technical work, while the physics and significance passes are much more skeptical about the physical content. This is not a disagreement -- it reflects their different scopes. The math is sound; the physics framing is weak. Both statements are true simultaneously.

---

## 2. Cross-Artifact Consistency

### Issue ID Alignment

The panel artifacts use different labeling schemes (CLM-xxx for claims, FLAG-x for overclaims, MATH-xx for math checks, LIT-xxx for literature findings, and unnumbered items in physics/significance). I have unified these into the REF-xxx scheme in the REFEREE-REPORT.md. The mapping:

| REFEREE-REPORT ID | Source(s) |
|---|---|
| REF-001 (title overclaim) | CLM-009, CLM-010, FLAG-1 (reader); Physics item 1; Significance title section; LIT-002 (literature) |
| REF-002 (metastability vs rho) | CLM-002, FLAG-2, observation (reader); Physics Section 3.3 point 1; Significance novelty section |
| REF-003 (missing literature) | Reader handoff notes; LIT-001, LIT-002, LIT-003, LIT-004, LIT-007 (literature); Significance comparison table |
| REF-004 (unmotivated rho) | CLM-002, CLM-014, FLAG-2 (reader); Physics Section 1; Significance critical novelty question; LIT-003 (literature) |
| REF-005 (trivial bound on A1) | Observation on "trivial" nature (reader); Physics Section 3.3 points 2-3; Significance section on impact; LIT-007 (literature) |
| REF-006 (gamma error) | MATH-06 (math) |
| REF-007 (BEGK title) | LIT-005 (literature) |
| REF-008 (self-citations) | LIT-006 (literature) |
| REF-009 (within 1% claim) | CLM-011, FLAG-4 (reader) |

### Claim-Evidence Proportionality Audit

| Claim | Claim Type | Manuscript Location | Direct Evidence | Support Status | Overclaim Severity | Required Fix |
|---|---|---|---|---|---|---|
| "Boltzmann Brain Suppression" | significance | Title | Theorem A (finite Markov chain bound) | partially_supported | HIGH | Revise title to reflect actual scope |
| "Rigorous proof from metastability theory" | novelty | Title, abstract | Seven-lemma proof with error tracking | supported (for math); overclaimed (for physics) | MODERATE | Qualify as proof within the formal framework |
| "Experiential measure framework addresses [the BB problem]" | physical_interpretation | Abstract, line 33-36 | Definition of rho + Theorem A | unsupported | HIGH | Reframe as "proposes" not "addresses"; no physical validation provided |
| "first complete, self-contained assembly" | novelty | Line 124-125 | The paper exists and is self-contained | supported narrowly | LOW | Add "within this framework" qualifier |
| Main bound (Theorem A) | main_result | Section 3 | Full proof in Sections 4-6; validation in Section 7 | supported | NONE | No change needed |
| Error rate gamma = alpha/2 | method | Proposition 1 | Explicit rate enumeration | partially_supported (edge case error) | LOW | Fix formula: gamma = min(alpha/2, Ds - alpha) |
| "all matching within 1%" | method | Abstract, line 51 | Validation code | partially_supported | MODERATE | Revise to accurately describe what was matched |
| Born-Fisher test as future work | significance | Section 8.3, line 1045-1048 | Falsified per project history | unsupported (actively contradicted) | MODERATE | Acknowledge falsification or remove reference |

### Convention Consistency

- **Entropy convention:** nats (ln) used throughout. Consistent across main.tex, all equations.
- **Generator convention:** dp/dt = pQ (row-vector left multiplication, probabilist convention). Stated in Section 2 (line 170). Used consistently.
- **Metropolis rates:** Q(x,y) = r(x,y) exp(-[E(y)-E(x)]^+/eps). Stated in eq 3. Consistent throughout.
- **Communication height:** V(x,y) = min over paths of max barrier. Matches FW convention. Consistent.
- **Time units:** Continuous time. mu has units nat-seconds (line 102). Consistent.

No convention inconsistencies detected.

### Numerical Consistency

- C = (rho_max/c)(K_b/K_s^2) = (0.2/0.8)(1/1) = 0.25. Consistent between general formula and three-state specialization.
- Delta_s = 3.0, Delta_b = 1.0. Consistent between setup and validation.
- rho_s = 0.8, rho_b = 0.2. Consistent between text and validation.
- alpha constraint: 0 < alpha < Delta_s - Delta_b = 2. Test values alpha in {0.5, 1.0, 1.5} all within range.

---

## 3. Confidence Assessment for Overall Verdict

| Dimension | Panel Confidence | Adjudicator Confidence | Notes |
|---|---|---|---|
| Mathematical correctness | HIGH (math pass) | HIGH | Thorough equation-by-equation check performed |
| Overclaiming diagnosis | HIGH (all passes agree) | HIGH | Five independent passes converge on the same diagnosis |
| Literature gap severity | HIGH (literature pass) | HIGH | Specific missing references identified with justification |
| Venue fit | MEDIUM-HIGH (significance pass) | HIGH | Clear mismatch for cosmology venues; plausible for JMP |
| Physical interpretation | MEDIUM-LOW (physics pass) | MEDIUM | The physics assessment is fair but some judgments (e.g., whether rho adds anything at all) are matters of framing that the author could partially address |
| Recommendation floor | HIGH (all passes) | HIGH | major_revision is justified by the conjunction of overclaiming, literature gaps, and undistinguished metastability contribution |

### Final Confidence: HIGH

The panel is unanimous on the key issues and no disagreements require external resolution. The recommendation of major_revision is robust: the mathematics is correct, but the framing, literature positioning, and physical motivation require substantial work before the paper is publishable.

---

## 4. Conditions for Acceptance After Revision

A revised paper could achieve acceptance (at JMP or Foundations of Physics) if it:

1. **Reframes the title and abstract** to accurately reflect the mathematical scope (finite reversible Markov chains, not cosmological BB suppression).
2. **Adds a literature review section** covering existing BB solutions with explicit comparison to the experiential measure approach.
3. **Distinguishes metastability from rho** by including a plain-occupation-time comparison and clearly stating what rho contributes beyond the prefactor.
4. **Motivates or contextualizes rho** by either deriving it from axioms or explicitly placing it in the LMC/IIT family and discussing non-uniqueness.
5. **Discusses the trivial-bound structure** for alpha > 0 and its parallel to geometric cutoff measures.
6. **Fixes the gamma formula** (trivial one-line correction).
7. **Corrects the bibliography** (BEGK title, self-citations, missing references).

Items 1-5 are blocking. Items 6-7 are non-blocking.

---

_Cross-check completed: 2026-03-16T12:00:00Z_
_Reviewer: AI assistant (gpd-referee)_
