# REJECT: S6/S7 Proofs Are Circular — Must Be Rewritten

## The Problem

Phase 6 is NOT complete. The S6 and S7 proofs in `sections/axiom-verification.tex` use Jordan algebra and matrix language that is **not available at the point in the paper where these proofs appear**. This is a circularity that a reviewer will immediately reject.

The logical structure of the paper is:

1. Define the sequential product on a spectral OUS (Section 3)
2. **Verify S1-S7 using ONLY OUS-level constructions (Section 4)**
3. Invoke vdW Theorem 1 to get EJA structure (end of Section 4)
4. Use EJA structure for local tomography, type exclusion, C*-promotion (Sections 5-6)

Steps 3 and 4 are DOWNSTREAM of step 2. You cannot use Jordan algebra structure, matrix multiplication, the Luders formula, or commutator notation in the S1-S7 proofs. The only tools available are:

- The OUS $(V, V^+, \mathbf{1})$ and its effect space
- Spectral decompositions (available in spectral OUS)
- Alfsen-Shultz compressions $C_p$ and their properties
- Peirce decompositions (from compressions)
- The corrected product formula (eq. 6 / eq. 10)
- Previously verified axioms (S1-S3 for S5-S7, etc.)

## Exact Lines That Are Circular

### S6 (lines 191-211 of axiom-verification.tex)

**Part (i), line 196:** `"when $a$ and $b$ are compatible ($[a,b] = 0$ in the Jordan algebra)"`
- CIRCULAR: There is no Jordan algebra yet. Compatibility is defined as $\sp{a}{b} = \sp{b}{a}$ (Definition 2 of vdW). The commutator $[a,b]$ is matrix language.

**Part (i), lines 197-198:** `"the Luders product reduces to the ordinary product, giving $\sp{b}{a} = ba$"`
- CIRCULAR: The Luders product is a matrix formula. "Ordinary product" means matrix multiplication. Neither exists at the OUS level.

**Part (ii), lines 206-211:** `"simultaneously diagonalizable. In the common eigenbasis the Luders product reduces to ordinary multiplication, so $\sp{(b+c)}{a} = (b+c)\,a = ba + ca$"`
- CIRCULAR: Same issue. "Common eigenbasis," "ordinary multiplication," matrix product notation.

### S7 (lines 221-241 of axiom-verification.tex)

**Line 221:** `"By the functional calculus, $[a,b] = 0$ implies $[a, f(b)] = 0$"`
- CIRCULAR: This is the C*-algebraic functional calculus. At OUS level, the spectral functional calculus gives $f(b) = \sum_i f(\mu_i) q_i$ for the spectral decomposition of $b$, but the commutator notation implies matrix structure.

**Lines 222-223:** `"$\sp{b}{c} = \sqrt{b}\,c\,\sqrt{b}$ (Luders form)"`
- CIRCULAR: This IS the Luders formula on $M_n(\mathbb{C})^{sa}$. It is the conclusion of the paper, not a tool available in Section 4.

**Lines 225-231:** The entire matrix multiplication chain `$a\,\sqrt{b}\,c\,\sqrt{b} = \sqrt{b}\,a\,c\,\sqrt{b} = ...$`
- CIRCULAR: Matrix multiplication does not exist at the OUS level.

**Lines 238-241** acknowledge that "at the OUS level, the argument uses compression commutativity (Niestegge, Lemma 3.3)" — but this one-sentence remark is NOT the proof. It is a footnote pointing at what the proof SHOULD be.

## What the Fix Must Look Like

### S6 Fix

The key insight for S6 is that "compatible" means $\sp{a}{b} = \sp{b}{a}$, which at the corrected-product level means the effects share a joint spectral decomposition. Work entirely in the spectral/compression framework:

**Part (i):** We need $\sp{a}{(\mathbf{1}-b)} = \sp{(\mathbf{1}-b)}{a}$.

The left side follows from S1: $\sp{a}{(\mathbf{1}-b)} = a - \sp{a}{b}$. (This part of the current proof is fine — it uses only S1 and S3.)

For the right side, use S1 applied to the FIRST argument: $b \mapsto \sp{b}{a}$ is the map we need to show is additive in $b$. But S1 only gives additivity in the SECOND argument. So we need the corrected product formula directly.

Write $b = \sum_j \mu_j q_j$. Then $\mathbf{1} - b = \sum_j (1-\mu_j) q_j$ has the same spectral projectors. Since $a \compatible b$ means $\sp{a}{b} = \sp{b}{a}$, and the corrected product for compatible effects (shared spectral decomposition) gives scalar-valued products on each Peirce component, show that the corrected product formula for $\sp{(\mathbf{1}-b)}{a}$ equals $a - \sp{b}{a}$ by direct computation from eq. (6/10).

**Part (ii):** We need $\sp{(b+c)}{a} = \sp{b}{a} + \sp{c}{a}$ when $a \compatible b$ and $a \compatible c$.

Since $a$, $b$, and $c$ are pairwise compatible, they share a common spectral resolution (this IS available at spectral OUS level — compatible effects in a spectral OUS have a joint spectral decomposition). In the common resolution, the corrected product reduces to a scalar product on each Peirce component, and additivity follows from the linearity of compressions and Peirce projections.

### S7 Fix

We need: if $a \compatible b$ and $a \compatible c$, then $a \compatible \sp{b}{c}$.

**OUS-level argument (expand the compression commutativity footnote into a full proof):**

Since $a \compatible b$, the spectral projectors of $a$ commute with those of $b$ in the compression sense: $C_{p_i} \circ C_{q_j} = C_{q_j} \circ C_{p_i}$ for all spectral projectors $p_i$ of $a$ and $q_j$ of $b$ (Alfsen-Shultz Prop. 7.49, or Niestegge Lemma 3.3). Similarly for $a$ and $c$.

Now $\sp{b}{c}$ is built from compressions and Peirce projections of $c$ using the spectral data of $b$ (eq. 10). Show that the spectral projectors of $a$ commute with every building block of $\sp{b}{c}$:

1. $C_{p_i}$ commutes with $C_{q_j}$ (compressions for $a$'s and $b$'s projectors commute by hypothesis).
2. $C_{p_i}$ commutes with $C_{r_k}$ (compressions for $a$'s and $c$'s projectors commute by hypothesis).
3. The Peirce projections $P_{jk}^{(b)}$ for $b$'s resolution are built from $b$'s compressions, so $C_{p_i}$ commutes with $P_{jk}^{(b)}$ by (1).
4. Therefore $C_{p_i}$ commutes with every term in $\sp{b}{c} = \sum_j \mu_j C_{q_j}(c) + \sum_{j<k} \sqrt{\mu_j \mu_k} P_{jk}^{(b)}(c)$.
5. Compression commutativity of all spectral projectors of $a$ with $\sp{b}{c}$ gives $\sp{a}{(\sp{b}{c})} = \sp{(\sp{b}{c})}{a}$, i.e., $a \compatible \sp{b}{c}$.

Step 5 needs to be made explicit: show that when all spectral projectors of $a$ commute (in the compression sense) with all spectral projectors of $d = \sp{b}{c}$, then $\sp{a}{d} = \sp{d}{a}$. This follows from writing both products in the corrected form and showing term-by-term equality using compression commutativity.

## Constraints

- Do NOT use: Jordan products, matrix multiplication, Luders formula, commutator brackets, "ordinary product," "common eigenbasis" (use "common spectral resolution" instead)
- DO use: compressions $C_p$, Peirce projections $P_{ij}$, spectral decompositions, compression commutativity (Alfsen-Shultz Prop. 7.49, Niestegge Lemma 3.3), the corrected product formula (eq. 10)
- The proofs must work for ANY spectral OUS, not just $M_n(\mathbb{C})^{sa}$
- After the fix, re-run the circularity audit: grep for "Jordan," "Luders," "matrix," "ordinary product," "[a,b]" in Section 4. Zero hits required before vdW Theorem 1 is invoked.
- Update the S6/S7 SymPy tests if needed (the tests themselves can use matrix language since they're numerical verification, but the proofs cannot)

## Verification

After rewriting, the following must hold:
1. Circularity audit: zero uses of Jordan/matrix/Luders/commutator language in Section 4 before Theorem 4.1 (vdW Theorem 1 invocation)
2. All 844+ SymPy tests still pass (the product formula doesn't change, only the proof language)
3. The proofs are complete arguments, not sketches pointing at matrix-level versions
