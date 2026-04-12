# Paper 5 Review Fixes — Round 3

Fifth adversarial review (the hardest yet) identified three technical issues
that previous rounds did not fully address. These are specific mathematical
gaps, not framing issues.

**Integration note:** Same as before. Section files in `sections/` are shared.
Work on section files and new derivations only. Bryan will copy to blog repo.

---

## Problem 1: LT Linear Independence Argument Gap

**File:** `paper/sections/composite-lt.tex`, Theorem 5.8 / Proposition 5.7

**The critique:** The proof that product effects {a_i ⊗ b_j} are linearly
independent in V_BM has a gap. From

  sum_{i,j} alpha_{ij} (a_i ⊗ b_j) = 0

the paper jumps to "for any fixed a, the map b → sum_j alpha_{ij} B(a, b_j) = 0
forces all alpha_{ij} = 0." The reviewer says: "the index i is still dangling,
and B is a bilinear form on the factor spaces, not on the composite."

**Task:** Either fix the contraction argument to be rigorous (make the index
manipulation explicit and justify each step), or provide an alternative proof
of linear independence of product effects from non-degeneracy of B.

The argument should go something like:
1. Suppose sum_{i,j} alpha_{ij} (a_i ⊗ b_j) = 0 in V_BM.
2. Apply the product-form SP with some test effect c ⊗ d.
3. Use the product-form structure to separate the i and j indices.
4. Use non-degeneracy of B to conclude alpha_{ij} = 0 for all i,j.

The key is that the separation into i and j indices must be done within
the composite V_BM, not by appealing to a bilinear form on the factors.

**Deliverable:** Corrected proof in composite-lt.tex.

---

## Problem 2: Barnum-Wilce Categorical Hypotheses

**File:** `paper/sections/type-exclusion.tex`, Theorem 6.2 and surrounding text

**The critique:** The Barnum-Wilce result requires a full "locally tomographic
dagger-compact probabilistic theory" with every object sharp, spectral, and
having a conjugate, plus coherence assumptions. The paper has ONE composite
(V_BM), not a full monoidal theory. The reviewer says: "Those are categorical
hypotheses on an entire theory, not on one system and one chosen composite."

Additionally, the dagger (involution) is exhibited AFTER the C*-algebra
conclusion, making the reference to "dagger given by the involution exhibited
below" circular.

**The reviewer also notes:** "Barnum-Graydon-Wilce's EJA-categorical work
explicitly gives a dagger-compact category InvQM that INCLUDES real, complex,
and quaternionic systems. So even dagger-compactness alone doesn't select
complex." This means BW is not doing the type selection we claim it does.

**Task:** Either:
(a) Honestly downgrade Theorem 6.2 to a consistency check (not an
    independent route to the conclusion), noting that the full categorical
    hypotheses are not constructed here, OR
(b) Construct the required categorical structure (the full locally
    tomographic monoidal theory) from our composite. This would require
    showing that the category of finite-dim spectral OUSs with self-modeling
    composites has the required monoidal/dagger structure.

Option (a) is safer and more honest. The paper already has vdW Theorem 3
as the primary promotion route. BW and HO can be presented as "the
conclusion is consistent with these independent results" rather than
"these provide independent proofs."

**Deliverable:** Updated text in type-exclusion.tex. If downgrading,
change the presentation to clearly label BW and HO as consistency checks.

---

## Problem 3: Hanche-Olsen Independence

**File:** `paper/sections/type-exclusion.tex`, Theorem 6.3

**The critique:** Same issue as BW. The qubit subsystem E_2 comes from
type exclusion (which already used LT to kill non-complex types). So HO
is not an independent route - it's a consistency check that confirms the
C*-conclusion AFTER the complex type has already been established.

**Task:** Downgrade alongside BW per Problem 2. Present as: "Having
established that V = M_n(C)^sa, we note that the conclusion is
independently consistent with [HO theorem], which provides a second
route to the C*-algebra conclusion from the now-available qubit
subsystem."

**Deliverable:** Updated text in type-exclusion.tex.

---

## Not in scope for this round

The following issues from the review are FRAMING issues already addressed
in the paper:
- "phi does no work" → addressed by characterization corollary (7.1)
  and "Assumptions as Self-Modeling" (Section 7.3)
- "minimal composite does the work" → addressed in Section 7.3
- "one premise is overstated" → honest accounting preserved throughout
- "spectral OUS is already 80% quantum" → proximity objection remark

## Verification

1. `tectonic main.tex` compiles clean
2. No [?] citations
3. LT proof is self-contained and rigorous
4. BW and HO clearly labeled as consistency checks, not independent routes
5. vdW Theorem 3 remains the primary promotion route
