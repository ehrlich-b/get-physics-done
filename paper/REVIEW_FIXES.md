# Paper 5 Review Fixes

Four independent adversarial reviews found no fatal flaws but identified
substantive issues that need fixing. Some are text-level corrections already
applied to `main.tex` in the blog repo. Others require real math work.

**Integration note:** Bryan's blog repo (`~/repos/blog/landing/papers/qm-from-self-modeling/`)
has main.tex edits already applied (premise count updated from "one" to "two",
Prop 3.3 converted to Assumption, Prop 3.2 proof sketch labeled). The section
files in `sections/` are shared between both repos. When GPD fixes section
files here, Bryan will copy them to the blog repo. Do NOT touch main.tex
here - work only on section files and new derivations.

---

## Immediate Fixes (section files)

### Fix 1: Theorem 6.2 (Barnum-Wilce) misstated
**File:** `paper/sections/type-exclusion.tex` lines 134-157

**Problem:** The paper states Thm 6.2 as: "finite-dimensional EJA + locally
tomographic composite + qubit subsystem => M_n(C)^sa". The actual
Barnum-Wilce result requires a "locally tomographic dagger-HSD probabilistic
theory containing a qubit" with specific categorical structure, not just the
three bare properties.

**Also:** Lines 151-154 claim "any orthogonal pair {p, p^perp} defines a
V_3-like 2-level sector." But V_2 = M_2(R)^sa, V_3 = M_2(C)^sa,
V_5 = M_2(H)^sa. A two-level face is NOT generically complex across EJA
types. This is an internal contradiction.

**Fix:** Restate Thm 6.2 to match the actual BW hypotheses. The qubit
subsystem claim should come AFTER type exclusion has already eliminated
real and quaternionic via dimension counting. At that point, the only
remaining simple EJA is complex, so two-level faces ARE V_3 = M_2(C)^sa.
Restructure the argument order accordingly.

### Fix 2: Theorem 6.3 (Hanche-Olsen) misstated
**File:** `paper/sections/type-exclusion.tex` lines 159-171

**Problem:** The paper states: "If a JB-algebra admits a tensor product
(V tensor V that is again a JB-algebra with product states), then V is
the self-adjoint part of a C*-algebra." The actual Hanche-Olsen theorem
(LNM 1132, pp. 121-131) is specifically about E tensor E_2 where E_2 is
the 2x2 complex Hermitian matrices, with specific factorization identities
for the Jordan product. The paper's statement is too broad.

**Fix:** Restate to match the source. Note that E_2 is provided by the
qubit subsystem, which by this point in the argument (after Fix 1's
restructuring) is known to be complex.

### Fix 3: Umlaut encoding in refs.bib
**File:** `paper/refs.bib`

**Problem:** Tectonic's built-in BibTeX hangs with the `alpha` bibliography
style when multiple entries use `M{\"u}ller` (braces around the umlaut
command). The alpha style's label disambiguation algorithm loops infinitely
on the braced form when multiple entries share the same surname.

**Fix:** Change all instances of `M{\"u}ller` to `M\"uller` (remove inner
braces). Both render identically but the unbraced form doesn't confuse
alpha's label generator. Apply to all entries with accented author names.

---

## Deep Math Issues (new derivations needed)

### Issue 1: Derive maximal coherence from faithfulness (or prove independence)

**Context:** The paper now states maximal coherence as a separate operational
principle (Assumption in main.tex). The reviewer correctly noted this was
previously presented as following from faithfulness, but the paper admits
"this is a selection principle, not a uniqueness theorem."

**Task:** Can you show that any sub-maximal mixing function f with
0 < f < sqrt(lambda_i * lambda_j) violates S1-S7 or some other necessary
property of the self-modeling cycle?

Known: f=0 fails S3 (unitality). But does f = c * sqrt(lambda_i * lambda_j)
for 0 < c < 1 fail any axiom?

- If YES (some axiom fails for all c < 1): maximal coherence is DERIVED from
  the axioms, and the premise count drops back to 1+4. Write the proof.
- If NO (sub-maximal f still satisfies S1-S7): maximal coherence is genuinely
  independent. Write a counterexample showing a valid sequential product with
  sub-maximal f. This is also a useful result - it characterizes the "landscape"
  of self-modeling products.

**Hint:** Check S5 (associativity of compatible effects). For compatible a, b:
a . (b . c) = (a . b) . c. With f = c * sqrt, the LHS and RHS may differ
because the mixing function compounds differently. Also check S4 (symmetry of
orthogonality): if a . b = 0 then b . a = 0. Does sub-maximal f break this?

### Issue 2: Decomposition-independence of formula (10)

**Problem:** The corrected product formula depends on a spectral decomposition
a = sum_i lambda_i p_i and the associated Peirce projections P_{ij}. When
eigenvalues are degenerate (repeated), the spectral decomposition is not
unique. The product must be shown to give the same result regardless of
which valid decomposition is chosen.

In quantum mechanics, this independence is guaranteed because sqrt(a) b sqrt(a)
is defined via functional calculus, which is basis-free. Here, basis-freeness
is exactly what needs to be reconstructed.

**Task:** Prove that the corrected product (10) is independent of the chosen
spectral resolution. Key cases:
- Two distinct eigenvalues with multiplicity > 1
- Degenerate case where all eigenvalues are equal (a = lambda * 1)
- Perturbation argument: show the product is continuous through degeneracies
  (which the paper claims in S2 but doesn't prove rigorously)

### Issue 3: General positivity bound (Prop 3.2)

**Problem:** The positivity bound |f(lambda_i, lambda_j)| <= sqrt(lambda_i *
lambda_j) is derived via a Schur complement argument on M_2(C)^sa. This is
not a general proof for arbitrary finite-dimensional spectral OUS.

**Task:** Either:
(a) Prove the bound for arbitrary finite-dim spectral OUS, or
(b) Show the M_2(C)^sa argument generalizes (every spectral OUS contains
    2-level faces where the Schur complement argument applies, and the bound
    on 2-level faces implies the global bound)

### Issue 4: S6/S7 full proofs for general n

Already flagged by three prior reviews. The proofs are proof-sketch quality.
Specific gaps:

**S6 part (i):** The critical square-root identity does not hold in general.
The proof pivots to "direct computation" via compression commutativity but
doesn't deliver the computation.

**S7:** The proof claims commutativity of compressions C_{p_i} "propagates"
to spectral projectors of d = b . c. This is nontrivial and not established.
Specifically: even if C_{p_i} commutes with C_{q_j} (compressions from b's
decomposition), it does not automatically follow that C_{p_i} commutes with
the compressions for d's spectral projectors, because d's decomposition
depends nonlinearly on b and c.

**Task:** Write complete proofs of S6 and S7 that work for arbitrary n,
not just n=2. The SymPy tests (844+) confirm the results hold, so the
proofs should exist. The structure is there; the details need filling in.

---

## Verification

After all fixes:
1. `tectonic main.tex` compiles clean (no [?] citations, no hanging)
2. Thms 6.2 and 6.3 match their cited sources exactly
3. Qubit subsystem claim appears only after type exclusion
4. Any new derivations have SymPy test coverage
5. All `M{\"u}ller` changed to `M\"uller` in refs.bib

## Priority

Fix 1-3 (immediate) > Issue 1 (maximal coherence) > Issue 2 (decomposition
independence) > Issue 3 (general positivity) > Issue 4 (S6/S7)
