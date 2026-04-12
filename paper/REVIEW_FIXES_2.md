# Paper 5 Review Fixes — Round 2

Three independent expert-level reviews (one harshly critical, one constructive,
one balanced) identified problems that the previous round did NOT catch. The
previous round fixed citation misstatements, S6/S7 proofs, decomposition
independence, and general positivity. This round targets deeper structural
issues with the derivation itself.

**Integration note:** Same as before. Section files in `sections/` are shared.
Work on section files and new derivations. Bryan will copy to the blog repo.

**Priority:** Problem 1 > Problem 2 > Problem 3 > Problem 4. Problems 1 and 2
are mathematical. Problems 3 and 4 are presentation/ordering fixes.

---

## Problem 1: The Ansatz Problem (CRITICAL)

**The critique:** The corrected product formula

  a · b = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} f(λ_i, λ_j) P_{ij}(b)

is *postulated*, not *derived* from self-modeling. The paper shows the naive
extension (pinching) fails, then writes down a Peirce-corrected ansatz and
finds a mixing function that works. But there is no theorem showing that a
faithful self-model forces this specific form. The reviewer calls this
"reverse-engineering, not derivation."

**What needs to happen:** Prove that any bilinear map on effects that:
(a) agrees with compression on sharp effects (p · q = C_p(q)),
(b) extends to general effects via the spectral decomposition,
(c) is compatible with the tracking map φ (in some precise sense),
MUST have the Peirce-corrected form. In other words, derive the ansatz
rather than assume it.

**Possible approach:** The spectral extension from sharp to general effects
is forced by S1 (additivity) + S2 (continuity) + the spectral theorem.
Any bilinear extension that is:
- linear in the second argument (S1),
- continuous in the first argument (S2),
- agrees with C_p on sharp effects,
must respect the Peirce decomposition structure because compressions
generate the Peirce projections. The question is whether the general form
is FORCED to be Σ_i f_i(λ) C_{p_i}(b) + Σ_{i<j} g_{ij}(λ) P_{ij}(b),
or whether other terms (mixing between Peirce 0-spaces and 1-spaces,
for instance) are possible.

If the spectral ansatz IS forced by S1 + S2 + compression on sharps, then
the ansatz is not an assumption — it's a consequence of the axioms. Write
this as a theorem (call it "Spectral Extension Theorem" or similar).

If the spectral ansatz is NOT forced (i.e., other bilinear extensions exist
that agree on sharps but don't have the Peirce-corrected form), then we have
a genuine additional assumption that needs to be made explicit.

**Deliverable:** Either a proof that the Peirce-corrected form is the unique
extension, or an honest characterization of what additional assumptions
constrain it.

---

## Problem 2: Functional Form Gap in Maximal Coherence (IMPORTANT)

**The critique:** The proof of Prop 3.3 (now a Proposition with proof) assumes
f(λ_i, λ_j) = c · √(λ_i λ_j) where c is a CONSTANT. But the positivity
bound only gives |f(λ_i, λ_j)| ≤ √(λ_i λ_j), which means we can write
f(λ_i, λ_j) = c(λ_i, λ_j) · √(λ_i λ_j) where c is a FUNCTION of the
eigenvalues, not necessarily a single number.

The current proof shows c² = c for a constant c. But if c depends on the
eigenvalues, the S5 associativity equation becomes a functional equation:

  c(α₁,α₂) · c(β₁,β₂) = c(α₁β₁, α₂β₂)

for all compatible effects with eigenvalues α_i and β_j.

**What needs to happen:** Derive the full functional equation from S5 for
general f (not just f = c·√). Then show that the only continuous solution
satisfying the boundary conditions f(1,λ) = λ, f(0,λ) = 0, and the
positivity bound, is f = √(λ_i λ_j).

**Constructive hint from reviewer 2:** "The LHS Peirce coefficient will
involve f composed with f, and the RHS will involve f applied to the product
eigenvalues. This should yield a multiplicative functional equation on f,
something like f(α₁,α₂)·f(β₁,β₂) = f(α₁β₁, α₂β₂), which combined with
continuity (S2), boundary conditions, and positivity, forces f = √(λ_i λ_j)."

**Deliverable:** A complete proof of Prop 3.3 that does NOT assume the
constant-c parametrization. The proof should work for arbitrary continuous
f satisfying the positivity bound and derive f = √(λ_i λ_j) from S5 + S2 +
boundary conditions.

---

## Problem 3: Composite Bootstrapping Circularity (PRESENTATION)

**The critique:** There is an apparent circularity in Section 5:
- To verify S1-S7 on V_BM, we need the sequential product defined on ALL
  of V_BM (not just product effects).
- But we need S1-S7 (hence EJA structure, hence LT) to know that product
  effects span V_BM.

**The resolution (reviewer 2 suggests this):** The product-form SP extends
by bilinearity to the algebraic tensor product V_B ⊗ V_M regardless of
whether this equals V_BM. S1-S7 can be verified on this subspace. Then EJA
structure applies to the subspace, the trace form argument gives LT, and
minimality gives V_BM = V_B ⊗ V_M.

**What needs to happen:** Make this logical ordering explicit in the paper.
Add a remark or restructure Section 5 so the verification order is:
1. Define product-form SP on algebraic tensor product V_B ⊗ V_M
2. Verify S1-S7 on this subspace
3. Conclude EJA structure on the subspace
4. Prove LT using trace form + minimality
5. Conclude V_BM = V_B ⊗ V_M

**Deliverable:** Updated text in `sections/composite-lt.tex` that makes the
ordering explicit and addresses the bootstrapping concern.

---

## Problem 4: Proximity Objection (PRESENTATION)

**The critique:** A spectral OUS with compressions, Peirce decomposition,
facial structure, and resolution of unity is "already 80% quantum." The
framework knows about non-commutativity and complementarity via the Peirce
1-space before self-modeling even enters.

**The defense (which exists but isn't in the paper):** Classical probability
theory lives comfortably in this framework as the special case where V_1 = {0}
(all Peirce 1-spaces are trivial). The framework is NOT biased toward quantum
mechanics. What self-modeling does is force non-trivial V_1 content — it
forces the off-diagonal structure that makes the theory non-classical. Without
self-modeling, you could have a perfectly valid spectral OUS that is entirely
classical.

**What needs to happen:** Add a paragraph to the introduction or Section 2
making this defense explicit. Something like: "The Alfsen-Shultz framework
is not biased toward quantum mechanics. Classical probability theory lives
within it as the special case where all Peirce 1-spaces are trivial and the
sequential product reduces to pointwise multiplication on a simplex. The
content of our derivation is that self-modeling forces non-trivial
off-diagonal structure."

**Deliverable:** One paragraph in `sections/discussion.tex` or the
introduction addressing the proximity objection.

---

## Verification

After all fixes:
1. Any new proofs have SymPy test coverage where applicable
2. The ansatz derivation (Problem 1) should be testable: verify that the
   general form is the unique extension on M_n(C)^sa for small n
3. The functional equation (Problem 2) should be verified numerically:
   try non-constant c functions and confirm S5 fails
4. Circularity resolution (Problem 3) should not change any theorem
   statements, only the presentation ordering
5. `tectonic main.tex` compiles clean after all changes
