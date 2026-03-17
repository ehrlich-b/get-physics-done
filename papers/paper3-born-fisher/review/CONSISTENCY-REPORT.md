---
reviewed: 2026-03-16T22:00:00Z
scope: panel_consistency_check
---

# Consistency Report: Panel Cross-Check

**Manuscript:** papers/paper3-born-fisher/main.tex
**Title:** Falsification of the Born-Fisher-Experiential Conjecture in a Qubit Toy Model
**Date:** 2026-03-16

## 1. Panel Agreement Map

### Areas of unanimous agreement

All five panel stages agree on the following:

1. **Mathematics is sound.** The Lindblad superoperator construction, RK4 integration, quantum information calculations, and falsification logic are all correct. No stage found a structural mathematical error. (Math stage: "HIGH confidence"; Physics stage: "HIGH confidence"; Reader: no math concerns.)

2. **Physics is correct.** The physical mechanism (exchange Hamiltonian maintains I_vN >= S_vN(B), preventing r < 1) is correctly identified and supported by both analytical reasoning and numerical evidence. (Physics stage: "correctly diagnosed"; Math stage: "SOUND"; Reader: "airtight within the stated scope.")

3. **Claims are proportionate to evidence.** Every stage independently concluded that the paper does not overclaim the scope of the falsification. The paper consistently qualifies the result as applying to "this model class." (Reader: FLAG-001 and FLAG-002 rated as minor; Physics: PHYS-012 "proportional to evidence"; Significance: "appropriately proportional.")

4. **One narrative typo: factor-of-2 in rho_Q.** The math stage identified this (line 402: -0.693 should be -1.386 nats) and all subsequent stages treated it as a minor presentation issue that does not affect conclusions.

5. **Self-citation titles are wrong.** The literature stage identified this (LIT-002) and it was not contested. Confirmed by direct inspection of companion paper titles.

### Areas of agreement with nuance

6. **Significance is limited.** The reader stage rated the paper's recommendation ceiling at minor_revision. The significance stage independently concluded "low external significance" and recommended major_revision for Foundations of Physics, reject for PRL. The physics stage rated minor_revision based on physics quality alone, explicitly noting "PHYS-003, PHYS-005, PHYS-007 are about clarifying scope and emphasis." The final adjudication weighs significance more heavily than the physics and math stages because publication suitability requires significance, not just correctness. **Resolution: major_revision is appropriate because the significance deficit is a publication-relevant problem, not merely a stylistic one.**

7. **Literature gaps are material.** The literature stage identified missing Deutsch-Wallace and Zurek envariance references as blocking (LIT-001). The reader stage flagged the Fisher information absence (FLAG-005) as moderate. The physics stage noted the conjecture's underspecification (PHYS-003) as major. These three findings are independent but reinforce a common concern: the paper does not adequately situate itself in the existing discourse on Born-rule derivations. **Resolution: REF-002 (literature) is blocking; REF-006 (Fisher) is a minor issue.**

## 2. Panel Disagreements and Their Resolution

### Disagreement 1: Recommendation ceiling

| Stage | Ceiling | Rationale |
|-------|---------|-----------|
| Reader (Pass 1) | minor_revision | "The overclaiming is marginal and could be fixed with small wording changes" |
| Math (Pass 2) | minor_revision (implicit) | No blocking mathematical errors found |
| Physics (Pass 3) | minor_revision | "The physics is sound... three major findings are about clarifying scope and emphasis" |
| Significance (Pass 4) | major_revision | "Not scientifically significant enough for most peer-reviewed journals as a standalone submission" |
| Literature (Pass 5) | major_revision | "Two findings are blocking: missing Deutsch-Wallace/Zurek and wrong self-citation titles" |

**Resolution:** The math and physics stages focus on technical correctness, where the paper excels. The significance and literature stages focus on publishability, where the paper has genuine deficits. The peer-review protocol is explicit: "a mathematically coherent paper can still deserve major revision or rejection if its physical story is weak, its novelty collapses against prior work, or its significance is overstated." The significance and literature concerns are not mere stylistic complaints -- they are publication-relevant problems that cannot be fixed with local edits. **Final adjudication: major_revision.**

### Disagreement 2: Severity of conjecture underspecification (PHYS-003)

The physics stage rated the conjecture's underspecification as "major" (PHYS-003) because the conjecture does not specify which dynamics, Hamiltonian, or channel class it applies to, limiting the strength of the falsification. The reader stage identified this as FLAG-004 (moderate) and assessed that "the paper handles this appropriately in Sec 5 and Sec 5.3."

**Resolution:** Both stages are correct but emphasize different aspects. The paper does handle the scoping appropriately in the discussion, which supports the reader's assessment. But the physics stage is right that the conjecture's vagueness limits the falsification's power -- falsifying a vague conjecture for one specific model is a weaker result than falsifying a precise conjecture. This is not a blocking issue (the paper is honest about the scope) but it contributes to the significance concern. **Absorbed into REF-001 (significance).**

### Disagreement 3: Is the negative result "surprising"?

The significance stage argues (Section 1, point 3) that "the negative result is not surprising" because the pure-state constraint already shows rho_Q < 0 for entangled states, and the monotone decrease of r follows from the dynamics structure. The physics stage counters (PHYS-010) that the physical mechanism is "correctly identified and analytically verified" as a genuine insight.

**Resolution:** Both are correct. The mechanism is a genuine structural insight about quantum information flow. But the result is predictable from the model's structure -- a competent physicist looking at the initial condition (pure entangled state, r=2) and the dynamics (exchange preserves populations, dephasing destroys coherences) would predict r decreasing monotonically to 1 without computation. The 1,900 trajectories confirm what analysis predicts but do not reveal surprises. **This predictability reinforces REF-004 (missing analytical proof) -- if the result is analytically obvious, prove it analytically.**

## 3. Cross-Stage Consistency of Evidence Assessment

| Claim | Reader | Math | Physics | Significance | Literature | Consistent? |
|-------|--------|------|---------|--------------|------------|------------|
| CLM-001 (main falsification) | Supported (within scope) | SOUND | Supported | Supported (low significance) | Not contested | Yes |
| CLM-002 (Test A) | Fully supported | SOUND | Supported | Not separately assessed | Not separately assessed | Yes |
| CLM-003 (Test B) | Fully supported | SOUND | Supported | Supported | Not separately assessed | Yes |
| CLM-004 (mechanism) | Fully supported | SOUND | Supported | "Analytically predictable" | Not separately assessed | Minor tension (see above) |
| CLM-006 (Lipschitz unaffected) | Weakly supported | Not checked | Not checked | Not assessed | Not assessed | No contradiction; under-examined |
| CLM-008 (novelty) | Deferred to lit stage | N/A | N/A | "Novelty is in application context" | Overstated (missing refs) | Consistent: novelty is weak |

## 4. Issues Not Raised by Any Stage (Adjudicator Spot-Checks)

### Spot-check 1: The max(rho_Q, 0) clamp in the trajectory functional

The conjecture (Eq. 6) defines mu_Q using max(rho_Q, 0), which clamps negative values to zero. The math stage verified this is correctly implemented. The physics stage noted this means the conjecture "is only about the positive part of rho_Q." No stage questioned whether this clamping is physically well-motivated -- it is essentially an arbitrary choice that ensures mu_Q >= 0. For the falsification, it does not matter (rho_Q is never positive anyway). But for future modifications of the conjecture, the clamping needs physical justification. **Not a current issue; noted for completeness.**

### Spot-check 2: Qutrit evidence adequacy

The reader stage noted (Weakness 3) that the d=3 evidence is thin: 3 dynamic trajectories and limited static points. The physics stage accepted the qutrit results without flagging the small sample. **Assessment: The paper claims the falsification is "not a d=2 artifact" based on 3 trajectories and ~6 static points. This is plausible given the structural nature of the argument (the mechanism is independent of d), but the claim would be stronger with more d=3 data. This is a minor issue, not blocking.**

### Spot-check 3: Asymmetric dephasing collapse operators

The physics stage verified (PHYS-015) that the asymmetric operators L_0, L_1 produce similar physics to the symmetric case. The math stage verified the code implementation (lines 77-83 of lindblad.py). No stage noted that the asymmetric dephasing operators (projective collapse operators |k><k| x I) produce a slightly different dissipator than the symmetric case (sigma_z x I). The paper handles this correctly by specifying the asymmetric extension separately (Eq. 10), and the physics stage confirmed the argument for r >= 1 still holds. **No issue.**

## 5. Confidence Assessment

| Assessment | Confidence | Basis |
|------------|-----------|-------|
| Mathematics is correct | HIGH | Five key equations verified by math stage; code logic confirmed; one narrative typo only |
| Physics is correct | HIGH | Mechanism analytically derived and numerically confirmed; physics stage rated HIGH |
| Falsification is valid for stated scope | HIGH | All stages agree; proportionate claims; 1900+ trajectories |
| Significance is insufficient for standalone publication | HIGH | Significance stage provides detailed analysis; reader and literature stages concur |
| Literature gaps are blocking | HIGH | Missing references confirmed against known literature; self-citation errors verified |
| Final recommendation (major_revision) | HIGH | Consistent with the panel's collective evidence, with significance and literature concerns properly weighted |

## 6. Summary

The panel is internally consistent. The two apparent "disagreements" (recommendation ceiling and result predictability) are not contradictions -- they reflect different stages emphasizing different dimensions (technical correctness vs. publication suitability). The final adjudication resolves these by applying the peer-review panel's guardrails: significance and literature positioning are publication-relevant problems, and a mathematically sound paper with weak external significance merits major_revision, not minor_revision.

The paper's core strength -- honest self-falsification with thorough numerical execution -- is unanimously recognized. Its core weakness -- low external significance of a self-posed, untested conjecture -- is recognized by all stages that assess publishability.

---

_Panel consistency check: 2026-03-16T22:00:00Z_
_Adjudicator: AI assistant (gpd-referee)_
