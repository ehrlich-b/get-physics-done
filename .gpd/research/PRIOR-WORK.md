# Prior Work: Paper 5 v14.0 Revision -- Sequential-Product Peirce Preservation and Related Exposition Gaps

**Surveyed:** 2026-04-16
**Domain:** Operational quantum foundations / Sequential effect algebras / Order-unit spaces / Peirce decomposition / Jordan-algebra axiomatization / Local tomography / Lean 4 formalization of operator algebras
**Confidence:** MEDIUM-HIGH overall; MEDIUM on the specific Phase 54 Peirce-preservation question because the literature is silent in exactly the form Paper 5 needs

This document covers prior work for the v14.0 Paper 5 revision cycle, targeted specifically at the six jigsaw-piece gaps identified pre-referee. It focuses exclusively on the literature available for each gap, with explicit attention to (A) is it already proven somewhere citable, (B) does a precise citation exist, or (C) is the literature silent and must Paper 5 prove it.

The most important finding: **the Phase 54 Peirce-preservation claim (sequential product preserves V_2(p_i) and V_1(p_i, p_j) from OUS primitives S1 + S3 alone) is not stated in this form anywhere in the surveyed literature.** Alfsen-Shultz proves Peirce decomposition structure; van de Wetering derives EJA structure; Niestegge derives compression properties; but no source proves the specific claim "given only S1 and S3 on an arbitrary sequential product, the left multiplication L_a = a o (-) preserves the Peirce subspaces associated with the spectral projectors of a." Phase 54 outcome is most likely (A) from OUS primitives + internal GPD v2.0 results OR (C) structural-gap characterization with Alfsen-Shultz citation as partial support.

---

## Key Results

| Result | Expression / Value | Conditions | Source | Year | Confidence |
|--------|-------------------|------------|--------|------|------------|
| Peirce decomposition of a Jordan algebra | V = V_1(p) + V_{1/2}(p) + V_0(p); V_i . V_j subset V_{i+j-1} (Peirce rules) | p idempotent in Jordan algebra over char != 2 | Peirce (1870), Albert (1947), Jacobson (1968) | 1947 | HIGH |
| Peirce decomposition in JB-algebras via compressions | V_2(p) = range(U_p), V_0(p) = range(U_{1-p}), V_1(p) = range(U_p + U_{1-p})^perp | p projection in JBW-algebra; U_p quadratic representation | Alfsen-Shultz 2003, Prop 2.16; Hanche-Olsen-Stormer 1984, Thm 2.6.8 | 2003 | HIGH |
| Compressions (P-projections) on OUS | P^2 = P positive, P(1) = e (projective unit), complemented by P' with P+P' = pinching | Alfsen-Shultz spectral OUS with P-projection structure | Alfsen-Shultz 2003, Ch 7-8; Niestegge 2008 | 2003 | HIGH |
| vdW S1-S7 force EJA structure (fin-dim) | Sequential product space => Euclidean Jordan algebra | V finite-dim OUS with bilinear SP satisfying S1-S7 | van de Wetering, J. Math. Phys. 60 (2019), arXiv:1803.11139, Thm 1 | 2019 | HIGH |
| vdW SP + local tomography => C*-algebra | V fin-dim SP space locally tomographic with itself => exists C*-algebra A with V = A^sa | S1-S7 + V tensor V is SP space with (a1 tensor b1) & (a2 tensor b2) = (a1 & a2) tensor (b1 & b2) | van de Wetering 2019, Thm 3 | 2019 | HIGH |
| Three characterisations of Luders SP | SP is uniquely sqrt(a) b sqrt(a) under any of: (i) order-iso invariance, (ii) inner-product symmetry, (iii) invertibility preservation | vN algebra or EJA baseline | van de Wetering, J. Math. Phys. 59 (2018), arXiv:1803.08453 | 2018 | HIGH |
| Associativity forces commutativity for normal SEAs | If sequential product is associative then algebra is commutative | normal sequential effect algebra | Westerbaan-Westerbaan-vdW, Quantum 4, 378 (2020), arXiv:2004.12749 | 2020 | HIGH |
| Classical uniqueness of SP on simplices | Pointwise product is the unique SP on C(X) satisfying Gudder-Greechie axioms | classical/simplex case | Gudder-Greechie, Rep. Math. Phys. 49, 87 (2002) | 2002 | HIGH |
| Niestegge conditional probability via compressions | mu(f \| e) = mu_hat(U_e f) / mu(e); U_e is a positive projection with U_e(1) = e | OUS with compression base | Niestegge, Found. Phys. 38, 783 (2008), arXiv:1001.3633 | 2008 | HIGH |
| Barnum-Wilce: Jordan + local-tomo + qubit => complex QM | EJA satisfying local tomography for a qubit subsystem forces M_n(C)^sa type (excludes real, quaternionic, spin factor, exceptional) | Barnum-Wilce Found. Phys. 44 (2014), arXiv:1202.4513 | 2014 | HIGH |
| Spectral OUS vs convex sequential effect algebra correspondence | Convex sigma-SEAs <-> unit intervals of spectral OUS with homogeneous positive cone | Jencova, Flaminio, Kroupa 2023 | 2023 | HIGH |
| Foulis-based spectrality strictly more general than Alfsen-Shultz | Foulis approach contains Alfsen-Shultz as special case | Jencova 2021, arXiv:2102.01628 | 2021 | HIGH |
| **GAP**: "S1+S3 alone => L_a preserves Peirce subspaces" | NO literature statement found in this form | Would be decisive for Phase 54 (B) outcome | -- | -- | N/A (absence is the finding) |

---

## Foundational Work

### van de Wetering (2019) -- "Sequential Product Spaces are Jordan Algebras"

**Key contribution:** Theorem 1: any finite-dimensional OUS with continuous sequential product satisfying S1-S7 is order-isomorphic to a Euclidean Jordan algebra. Theorem 3: if the SP space is also locally tomographic with itself, the EJA arises from a C*-algebra.

**Method:** Axiomatic. vdW assumes S1-S7 as the primitive structure, builds spectral decomposition internally (Corollary 7), constructs Jordan product as p * q = (1/2)(L_p + L_{p^perp} - L_{p^perp p p^perp})q for atomic sharp p (Def. 15-16), invokes Koecher-Vinberg.

**Limitations for Phase 54:** vdW works WITH the full S1-S7 structure and WITH pre-existing spectral decomposition. Phase 54 asks the weaker question: given only S1 and S3 (not the full axiom set, and not the derived EJA structure), is Peirce invariance automatic? vdW does not answer this because he never considers S1+S3 alone. vdW's Peirce-like structure emerges only after S4 is used (homogeneity + self-duality, Prop 8 and Prop 30).

**Relevance:** Primary axiom source (arXiv:1803.11139 Def. 2 defines S1-S7). This is the reference Paper 5 §3.3 must use for its sequential-product notation and axiom numbering. A Phase 54 (C) outcome could cite vdW to characterize the gap: "S1+S3 alone is insufficient for Peirce invariance; the homogeneity properties of the cone (used in vdW Prop 8) are required."

### Alfsen-Shultz (2003) -- "Geometry of State Spaces of Operator Algebras"

**Key contribution:** Comprehensive geometric development of JB-algebra and JBW-algebra state spaces. Establishes P-projection / compression theory, spectral theorem for JB-algebras, face structure of state spaces, and characterization theorems for C*-algebra state spaces among JB-algebra state spaces via orientability.

**Method:** Geometric. Develops compressions as positive idempotent maps P: V -> V with P' complementary such that P and P' partition the identity (in the projective-unit sense, not the commutative sense). Peirce decomposition for a projection p in a JBW-algebra A gives A = U_p A + U_{1-p} A + (centered Peirce 1-space), where U_p is the quadratic representation -- NOT the sequential product. In a JB-algebra, U_p and the sequential product sqrt(p) . sqrt(p) coincide on sharp p, but this identification requires the JB structure, which Phase 54 is not allowed to assume.

**Chapter structure (partial, from AMS Bull review + Springer TOC):**
- Part I: Jordan algebras and their state spaces (Ch 1-5)
  - Ch 1: JB-algebras
  - Ch 2: JBW-algebras
  - Ch 3: Structure of JBW-algebras
  - Ch 4: Representations of JB-algebras as Jordan operator algebras
  - Ch 5: State spaces of Jordan algebras
- Part II: Compressions and spectral theory
  - Ch 7: General compressions (order-unit space setting)
  - Ch 8: Spectral theory
  - Ch 9 onward: Orientation, dynamical correspondence, C*-algebra characterization

**Note on chapter numbering:** The 2003 Birkhauser edition is the companion volume to Alfsen-Shultz (2001) "State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products". The 2003 book focuses on JB/JBW-algebra state spaces; the 2001 book focuses on C*-algebra state spaces. For the JB-side results (which is what §3.3 needs), the 2003 volume is the correct citation target.

**Limitations for Phase 54:** Alfsen-Shultz proves Peirce invariance for compressions/quadratic-representation operators in a JB-algebra, NOT for sequential-product left multiplication in an abstract spectral OUS lacking Jordan structure. The Jordan structure is precisely the downstream target of §3.3 in Paper 5, so invoking Alfsen-Shultz for Peirce preservation of the sequential product would be circular at the point where Paper 5 invokes it.

**Relevance:** HIGH as background for Peirce decomposition existence (a spectral OUS in Paper 5's sense has Peirce decomposition as structural fact), but NOT sufficient as a (B) citation for Phase 54's exact claim. A Phase 54 (B) outcome would require a theorem of the form "In any spectral OUS with sequential product o satisfying S1 and S3, the left multiplication L_a preserves Peirce subspaces of a's spectral projectors" -- this is not in Alfsen-Shultz.

**Precise citation candidates for different roles:**
- For **Peirce decomposition existence**: Alfsen-Shultz (2003), Ch 2-3 (JBW-algebra structure), especially Prop 2.5-2.16 on the range of P-projections
- For **compression-Peirce compatibility in JB-algebras**: Alfsen-Shultz (2003), Ch 2, Prop 2.16 and following; Hanche-Olsen-Stormer (1984), Thm 2.6.8 and surrounding Peirce discussion
- NOT available: Alfsen-Shultz never states the §3.3 exact claim, because compression-preservation of Peirce subspaces in AS is a JB-algebra result, not an abstract OUS result.

### Gudder-Greechie (2002) -- "Sequential Products on Effect Algebras"

**Key contribution:** Original definition of sequential effect algebra (SEA). Axioms A1-A5 (weaker than vdW's S1-S7). Proves uniqueness of pointwise multiplication as the SP on a fuzzy set system (classical simplex case).

**Method:** Effect-algebraic. Works with abstract effect algebras (not OUS), defines sequential product operation axiomatically.

**Limitations for Phase 54:** Does NOT address Peirce preservation. Gudder-Greechie axioms are strictly weaker than vdW's; the axiomatization Paper 5 uses is vdW's, so Gudder-Greechie is reference material only.

**Relevance:** Historical. Paper 5 §3.3 should cite both Gudder-Greechie (historical precedent) and van de Wetering (current standard) when introducing sequential products.

### Hanche-Olsen-Stormer (1984) -- "Jordan Operator Algebras"

**Key contribution:** First comprehensive monograph on Jordan operator algebras. Develops JB-algebra and JC-algebra theory. Includes Peirce decomposition for JB-algebras, spectral theorem for self-adjoint elements in JB-algebras, and classification of finite-dim formally real Jordan algebras (reproduces Jordan-von Neumann-Wigner).

**Method:** Operator-algebraic. Treats JB-algebras as closed Jordan subalgebras of B(H)^sa (in the JC case) or axiomatic (general JB). Peirce decomposition introduced in Ch 2 via idempotent elements.

**Limitations for Phase 54:** Takes Peirce decomposition as derived from Jordan algebraic structure. Does not address the abstract OUS case prior to JB structure. Peirce invariance is proved for the Jordan product L_a = a o (1/2)(- + -), not for an abstract sequential product.

**Relevance:** Background reference. If Phase 54's (A) proof uses properties of sharp effects that are closer to JB-algebra structure than to pure OUS structure, Hanche-Olsen-Stormer Ch 2 (Peirce decomposition) should be cited as context.

**Availability:** Freely available at https://hanche.folk.ntnu.no/joa/ (authors released under CC-BY-NC-ND).

### Niestegge (2008) -- "A Representation of Quantum Measurement in Order-Unit Spaces"

**Key contribution:** Defines compressions U_e on OUS corresponding to measurement update. Shows U_e is a positive projection, U_e(1) = e, and U_e U_f = U_f U_e when e <= f. Conditional probability formula mu(f | e) = mu_hat(U_e f)/mu(e). Establishes the connection between OUS compressions and Luders-type measurement conditioning.

**Method:** Axiomatic on OUS. Introduces "projective units" axiom (existence of a compression base) on an OUS; derives measurement-theoretic properties.

**Limitations for Phase 54:** Niestegge works at the level of the compression itself (U_e), not the sequential product a o b in abstract. The passage from "U_e is a positive projection" to "a o b = U_{something}(b) preserves Peirce subspaces" requires the additional step of identifying a o b with a compression expression, which requires additional axioms (vdW's S4-S7 or equivalents). Niestegge does not make this identification at the level of §3.3 primitives.

**Relevance:** Background for OUS compressions. Cite for: compressions exist in spectral OUS and are positive projections with U_e(1) = e.

### Westerbaan-Westerbaan-van de Wetering (2020) -- "Three Types of Normal Sequential Effect Algebras"

**Key contribution:** Classification: every normal SEA is a direct sum of three types: commutative (classical), quantum (corresponding to B(H)^sa for some H), and spin-factor (order-unit space of n-dim Minkowski-type cone). Associativity of the sequential product forces commutativity.

**Method:** Effect-algebraic. Extends Westerbaan-Westerbaan sequential-effect-algebra machinery to classify normal cases.

**Limitations for Phase 54:** Classification result, not a structural result about invariance. Peirce preservation not addressed.

**Relevance:** Supporting evidence for non-associativity sanity checks. Paper 5 §5 Thm 5.8 upper bound claim (gap 3) needs a "cannot do better than product-form" structural result, and the three-type classification might provide machinery (the decomposition into at most three blocks could constrain the upper bound). Worth checking in detail for Phase 56 (gap 3).

### Barnum-Wilce (2014) -- "Local Tomography and the Jordan Structure of Quantum Theory"

**Key contribution:** Orthodox finite-dim complex QM with superselection rules is the unique probabilistic theory in which (i) systems are Jordan algebras, (ii) composites are locally tomographic, (iii) at least one system is a qubit. This is the second half of Paper 5's chain (EJA + local tomography + qubit => M_n(C)^sa).

**Method:** EJA classification (Jordan-von Neumann-Wigner) combined with local tomography dimension counting. Spin factors V_n, M_n(R)^sa, M_n(H)^sa, M_3(O)^sa each fail one of the conditions.

**Limitations for Phase 54:** Orthogonal to Phase 54. Barnum-Wilce is downstream of the §3.3 argument; Phase 54 is about establishing the Peirce-invariance lemma for the sequential product, which sits before even the EJA structure emerges. Barnum-Wilce assumes EJA.

**Relevance:** Background. Paper 5 already uses this; no revision needed to the reference.

---

## Recent Developments (2020-2026)

| Paper | Authors | Year | Advance | Impact on Paper 5 Revision |
|-------|---------|------|---------|----------------------------|
| "Three types of normal sequential effect algebras" (Quantum 4, 378) | Westerbaan, Westerbaan, van de Wetering | 2020 | Three-type classification; assoc => commutative | Supports non-associativity sanity check; may help Phase 56 upper-bound argument |
| "Geometric and algebraic aspects of spectrality" (arXiv:2102.01628) | Jencova | 2021 | Foulis spectrality strictly generalizes Alfsen-Shultz | Phase 54 must be careful which spectrality notion is used; Paper 5's §3.3 setup must specify Alfsen-Shultz spectral OUS explicitly |
| "Spectral resolutions in effect algebras" (Quantum 2022) | Jencova, Plavala | 2022 | Spectral resolutions in convex effect algebras | Relevant to Paper 5 §3.3 spectral decomposition machinery |
| "Spectrality in convex sequential effect algebras" (arXiv:2312.13003) | Jencova, Flaminio, Kroupa | 2023 | Convex sigma-SEA <-> unit interval of spectral OUS with homogeneous positive cone; spectral iff every maximal commutative subalgebra is monotone sigma-complete | MAJOR: possible alternate citation for Paper 5's OUS-SP framework; worth examining whether their spectrality theorem yields Phase 54's Peirce preservation as a corollary |
| "On the properties of spectral effect algebras" (arXiv:1811.12407) | Jencova, Pulmannova | 2018/2019 | Structure of spectral effect algebras; context uniqueness | Background for spectral structure |
| "A Formalization of the Generalized Quantum Stein's Lemma in Lean" (arXiv:2510.08672) | Various | 2025 | First Lean formalization of a deep operator-algebra theorem; uses mathlib | Phase 58 (Lean axiom audit) baseline: shows the formalization style currently used |
| Lean-QuantumInfo library | Various | 2024-2025 | Formalized quantum info theory in Lean 4 | Phase 58 baseline for what is/isn't already available |

---

## Known Limiting Cases and Benchmarks

| Limit | Known Result | Source | Verified By |
|-------|--------------|--------|-------------|
| V = C(X) (classical simplex) | a o b = a * b (pointwise product) | Gudder-Greechie 2002 | Analytic proof; GPD Phase 4-06 SymPy verification (25 pairs) |
| V = M_n(C)^sa (quantum) | a o b = sqrt(a) b sqrt(a) (Luders) | vdW 2018 (uniqueness) | GPD Phase 4-06 SymPy verification on M_2(C)^sa |
| phi = trivial / no feedback | a o b degenerates, S3 fails (1 o P+ != P+) | GPD Phase 4-01 (failure case) | SymPy test-phi-algebraic |
| phi = isomorphism / faithful feedback | mixing f = sqrt(lambda_i lambda_j), S3 passes | GPD Phase 4-06 | SymPy verification |
| associative SP | Forces commutativity (algebra is classical) | Westerbaan-Westerbaan-vdW 2020 | Theoretical (do not re-derive) |

---

## Open Questions in the Literature

Questions where the literature is silent or inconclusive, with explicit relevance to the six revision gaps.

### 1. (Phase 54, CORE) Does S1 + S3 alone imply Peirce invariance of L_a?

**Status:** OPEN. Not addressed in vdW, Alfsen-Shultz, Niestegge, Gudder-Greechie, WWvdW, Jencova, or Barnum-Wilce.

**What vdW's paper does address:** vdW builds Peirce-like structure (homogeneity, self-duality) using S1-S7 jointly. He never asks "what subset of axioms forces Peirce invariance alone?"

**What Alfsen-Shultz addresses:** Proves Peirce invariance for U_p (quadratic representation) in JB-algebras. NOT for abstract sequential product in spectral OUS.

**What Niestegge addresses:** Proves U_e (compression) is a positive projection. Does not prove L_a = a o (-) preserves Peirce.

**Phase 54 implication:** The likely outcomes are:
- (A) Direct proof from Paper 5's specific L4 + spectral OUS structure, using the definition of a o b via compressions on sharp effects and spectral extension to general effects. The GPD v2.0 Phase 4-06 derivation (Eq. 04-06.4: a o b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b)) shows Peirce structure explicitly -- this is PRIOR GPD WORK directly relevant.
- (C) Structural gap characterization: "S1 + S3 alone is insufficient; need an additional assumption equivalent to compression-by-compression extension."
- (B) is UNLIKELY -- no precise citation in the required form exists.

### 2. (Phase 55, S4 facial structure lemma) What faces does S4 preserve in a spectral OUS?

**Status:** PARTIALLY ADDRESSED. vdW Prop 30 proves S4 + homogeneity => self-dual cone. Alfsen-Shultz proves face structure of state spaces in JB-algebras. But the explicit claim "S4 implies sequential-product-image of a face is contained in the same face" is not stated.

**Why it matters:** Paper 5 §3 or later uses facial structure lemma; needs either proof from vdW/Alfsen-Shultz machinery or direct OUS proof.

**Literature silence:** No single reference states "S4 => facial structure is preserved." vdW treats S4 as sufficient for inner-product symmetry (arXiv:1803.08453 Cor. 2). Alfsen-Shultz develops facial structure from JB-algebra axioms, not from sequential product S4.

### 3. (Phase 56, upper bound W carries product-form SP) Is the product-form SP the maximal SP on a wedge space?

**Status:** OPEN in the specific form. WWvdW 2020 three-type classification gives decomposition into commutative + quantum + spin-factor blocks, and each block has a canonical SP. The claim "W carries product-form SP as upper bound" likely means: any SP on W extends to (or is bounded by) the tensor-product SP derived from component SPs.

**Literature relevance:** WWvdW 2020 classification theorem. Also relevant: arXiv:1803.08453 Thm 3 (invariance-based uniqueness of Luders). Neither proves the "upper bound" claim explicitly.

**Phase 56 implication:** Likely (A) with help from WWvdW decomposition, or (C) with structural gap noted.

### 4. (Phase 57, Phi inert-wrapper technique) Is the Phi wrapper a standard technique?

**Status:** NON-STANDARD IN THE LITERATURE in this exact form. The notation "Phi inert wrapper" does not appear in vdW, Alfsen-Shultz, or other standard sources.

**Closest precedent:** GPD v2.0 internal work. Phase 4-06 uses phi as a tracking map E(B) -> E(M) and identifies phi-parametrization algebraically via the mixing function f(lambda_i, lambda_j). The "inert wrapper" framing appears to be Paper 5 terminology for phi as a formal parameter that enters axiomatically but does not break Jordan structure downstream.

**Phase 57 implication:** Paper 5 should probably rename or define "Phi inert wrapper" precisely, not cite it. Add a definition rather than a citation. If the literature is silent, that is a paper-exposition issue not a derivation issue.

### 5. (Phase 58, Lean audit) Are the 16 Lean axioms consistent with Alfsen-Shultz + vdW?

**Status:** TO BE VERIFIED. Lean formalizations of JB/JBW-algebras, sequential effect algebras, or spectral OUS do NOT currently exist in mathlib4 as of 2025-2026 search.

**What exists in mathlib:**
- General algebraic structures (rings, modules, order structures)
- Jordan algebra stub: `Mathlib.Algebra.Jordan.Basic` (elementary definitions only)
- Operator algebra formalization (partial, Stein's lemma paper arXiv:2510.08672 is recent breakthrough but specialized)
- Quantum info: Lean-QuantumInfo library (quantum channels, entropies)

**What does NOT exist:**
- JB-algebra or JBW-algebra formalization
- Sequential effect algebra / vdW axioms formalization
- Alfsen-Shultz compression theory in Lean
- Peirce decomposition in Lean

**Phase 58 implication:** The 16 Paper 5 Lean axioms are (necessarily) a bespoke formalization. The audit question is whether each axiom corresponds to a single citable Alfsen-Shultz or vdW result, or whether axioms are introduced that combine multiple literature results. A one-to-one axiom-to-citation mapping is the correct deliverable.

### 6. (Phase 59, minimal composite assumption) What is the minimal compositional assumption for local tomography?

**Status:** ADDRESSED. vdW 2019 Thm 3 uses "V is locally tomographic composite with itself" -- i.e., V tensor V is again an SP space with factorizing tensor product. Barnum-Wilce 2014 uses local tomography differently (in the Jordan algebra setting).

**Literature complete on this question:** Yes, for the EJA-to-C*-algebra step. Paper 5's minimal-composite defense should cite vdW Thm 3 and Barnum-Wilce and argue that no weaker compositional assumption gives the M_n(C)^sa specification.

**Phase 59 implication:** (B) outcome with vdW 2019 Thm 3 as primary citation. Paper 5 already uses this; the revision task is exposition, not re-derivation.

---

## Notation Conventions in the Literature

| Quantity | Standard Symbol(s) | Variations | Our Choice | Reason |
|----------|-------------------|------------|-----------|--------|
| Sequential product | a o b, a & b, a;b | Gudder-Greechie use o; vdW uses &; some use ; | a o b (Paper 5 convention) | Paper 5 submission uses o; milestone revision must preserve this |
| Jordan product | a . b, a o b, a * b | Can collide with sequential product notation | a . b | Distinct from sequential product |
| Compression | U_e, C_e, P_e | U_e in Niestegge; C_p in GPD Phase 4; P in Alfsen-Shultz | C_p (Paper 5 uses this for §3.3) | Consistent with GPD v2.0 derivation |
| Peirce subspace for projection p | V_2(p), V_1(p), V_0(p); A_1(p), A_{1/2}(p), A_0(p) | Different in Albert, AS, HOS | V_2(p), V_1(p, q), V_0 | Paper 5's §3.3 convention; aligns with AS 2003 for JBW-algebras |
| Sharp effect | projection, idempotent, projective unit | vdW uses "sharp"; AS uses "projection" | projective unit | Matches Paper 5 and Niestegge |
| Axiom label | S1-S7 (vdW); A1-A5 (Gudder-Greechie); different in AS | Different formalisms | S1-S7 (vdW) | Pinned in Paper 5 submission |

**Critical convention note for Paper 5 §3.3:** The exact axiom statements S1 (additivity in 2nd argument), S3 (unitality) must be pinned to arXiv:1803.11139 Definition 2 verbatim. Paper 5 v2.0 already does this; revision must not drift.

---

## Summary of Phase-by-Phase Prior Art

### Phase 54 (§3.3 Peirce preservation)

- **Prior GPD work (CRITICAL):** Phase 4-06 Peirce Feedback Extension (commit `9608ac54`). Derived corrected sequential product a o b = sum_i lambda_i C_{p_i}(b) + sum_{i<j} sqrt(lambda_i lambda_j) P_{ij}(b) with explicit Peirce structure. This is the STRUCTURAL formula Phase 54 needs to build the Peirce-invariance argument on.
- **External (A) support:** None complete. Alfsen-Shultz gives Peirce decomposition existence in JB-algebras (2003, Ch 2, Prop 2.16 area); Niestegge gives compression properties (2008, Prop 3.1); but no single source proves S1+S3 => Peirce invariance.
- **External (B) citation candidates:** NOT AVAILABLE in the required form. Closest partial supports are: AS 2003 Ch 2 for Peirce decomposition existence; vdW 2019 Corollary 7 for spectral decomposition; but these combined do not prove the §3.3 claim from S1+S3 alone.
- **Recommendation:** Pursue (A) using Paper 5's GPD v2.0 Phase 4-06 corrected product formula directly. The formula exhibits Peirce structure by construction; Peirce invariance is immediate from Eq. 04-06.4 structure. If the argument needs to work from S1+S3 axioms WITHOUT assuming the corrected-product formula (i.e., for arbitrary SP satisfying S1+S3), (C) is the likely outcome.

### Phase 55 (S4 facial structure lemma)

- **Prior work:** vdW 2019 Prop 30 (S4 + homogeneity => self-dual cone). arXiv:1803.08453 Cor 2 (S4 <=> inner-product symmetry in EJA setting).
- **Gap:** "S4 => facial structure preservation" not explicitly stated. Alfsen-Shultz develops facial structure from JB-algebra axioms, not S4.
- **Recommendation:** (A) proof using vdW Prop 30 + AS facial structure machinery from Ch 2-3. Or (C).

### Phase 56 (Thm 5.8 upper bound)

- **Prior work:** WWvdW 2020 three-type classification. vdW Thm 3.
- **Gap:** "W carries product-form SP as upper bound" not in literature explicitly.
- **Recommendation:** (A) using WWvdW 2020 classification + vdW tensor construction. Check if the "upper bound" is a consequence of the three-type decomposition restricted to W.

### Phase 57 (Phi inert-wrapper)

- **Prior work:** GPD v2.0 Phase 4-06 phi tracking map.
- **Gap:** Phi inert wrapper is Paper 5 internal terminology; not a standard technique.
- **Recommendation:** Define precisely; do not cite external literature for the wrapper itself. Cite Phase 4-06 or equivalent internal derivation for phi's algebraic role.

### Phase 58 (Lean axiom audit)

- **Prior work:** No JB/vdW Lean formalization exists. mathlib4 has elementary Jordan algebra stub only. Lean-QuantumInfo and Stein's lemma formalization (arXiv:2510.08672) are closest precedents.
- **Gap:** The 16 Paper 5 Lean axioms are a bespoke formalization with no literature counterpart.
- **Recommendation:** Audit each axiom against its exact Alfsen-Shultz (2003) chapter/section and vdW (2019) theorem/corollary. Produce a one-to-one mapping table. Flag any axioms that combine multiple literature results or introduce assumptions not stated elsewhere.

### Phase 59 (Minimal composite assumption)

- **Prior work:** vdW 2019 Thm 3 + Barnum-Wilce 2014.
- **Gap:** None. Literature is complete.
- **Recommendation:** (B) outcome. Cite vdW 2019 Thm 3 and Barnum-Wilce 2014; argue no weaker composition assumption gives M_n(C)^sa.

---

## Sources

### Primary references (HIGH confidence)

- **van de Wetering (2019)**, "Sequential product spaces are Jordan algebras," J. Math. Phys. 60, 062201 (2019), [arXiv:1803.11139](https://arxiv.org/abs/1803.11139) -- S1-S7 definitions (Def. 2); Thm 1 (SP => EJA); Thm 3 (SP + local tomo => C*-algebra); spectral decomposition (Cor 7); Jordan product construction (Def 15-16); homogeneity (Prop 8); self-duality from S4 (Prop 30). THE axiom source for Paper 5 §3.3.
- **van de Wetering (2018)**, "Three characterisations of the sequential product," J. Math. Phys. 59, 082202 (2018), [arXiv:1803.08453](https://arxiv.org/abs/1803.08453) -- Uniqueness of Luders product via invariance, inner product symmetry, or invertibility preservation. Relevant for Phase 55 (S4 via inner product).
- **Westerbaan, Westerbaan, van de Wetering (2020)**, "The three types of normal sequential effect algebras," Quantum 4, 378 (2020), [arXiv:2004.12749](https://arxiv.org/abs/2004.12749) -- Three-type classification. Associativity => commutativity. Relevant for Phase 56 upper-bound argument.
- **Alfsen, Shultz (2003)**, "Geometry of State Spaces of Operator Algebras," Birkhauser Boston. [Springer link](https://link.springer.com/book/10.1007/978-1-4612-0019-2) -- Compression theory (Ch 7); spectral theorem; JB-algebra structure; Peirce decomposition for JBW-algebras. Primary reference for Paper 5's spectral OUS assumptions.
- **Alfsen, Shultz (2001)**, "State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products," Birkhauser Boston. [Springer link](https://link.springer.com/book/10.1007/978-1-4612-0147-2) -- Companion volume for C*-algebra state space characterization.
- **Hanche-Olsen, Stormer (1984)**, "Jordan Operator Algebras," Pitman (Monographs Studies Math. 21), 183 pp. Freely available at [https://hanche.folk.ntnu.no/joa/](https://hanche.folk.ntnu.no/joa/) -- Peirce decomposition in Ch 2; JB-algebra theory.
- **Niestegge (2008)**, "A Representation of Quantum Measurement in Order-Unit Spaces," Found. Phys. 38, 783-795 (2008), [arXiv:1001.3633](https://arxiv.org/abs/1001.3633) -- Compression theory on OUS; conditional probability formula.
- **Gudder, Greechie (2002)**, "Sequential products on effect algebras," Rep. Math. Phys. 49, 87-111. [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0034487702800076) -- Original SEA definition; classical uniqueness.
- **Barnum, Wilce (2014)**, "Local tomography and the Jordan structure of quantum theory," Found. Phys. 44, 192-212, [arXiv:1202.4513](https://arxiv.org/abs/1202.4513) -- EJA + local tomo + qubit => M_n(C)^sa.

### Secondary references (MEDIUM confidence for Paper 5 specifically)

- **Jencova (2021)**, "Geometric and algebraic aspects of spectrality in order unit spaces: a comparison," [arXiv:2102.01628](https://arxiv.org/abs/2102.01628) -- Foulis vs Alfsen-Shultz spectrality. Important caveat: Paper 5 §3.3 setup must specify which spectrality notion it uses.
- **Jencova, Flaminio, Kroupa (2023)**, "Spectrality in convex sequential effect algebras," [arXiv:2312.13003](https://arxiv.org/abs/2312.13003) -- Convex sigma-SEA <-> spectral OUS with homogeneous positive cone. Worth examining for potential Phase 54 corollaries.
- **Jencova, Pulmannova (2018/2019)**, "On the properties of spectral effect algebras," [arXiv:1811.12407](https://arxiv.org/abs/1811.12407) -- Spectral effect algebra structure theorems.
- **Barnum, Graydon, Wilce (2020)**, "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359, [arXiv:1606.09331](https://arxiv.org/abs/1606.09331) -- Compositionality excludes exceptional types.
- **Chiribella, D'Ariano, Perinotti (2010/2011)**, "Informational derivation of quantum theory," Phys. Rev. A 84, 012311 (2011), [arXiv:1011.6451](https://arxiv.org/abs/1011.6451) -- Alternative operational reconstruction. Relevant if Phase 57 (phi wrapper) benefits from reframing in operational terms.
- **D'Ariano, Chiribella, Perinotti (2017)**, "Quantum Theory from First Principles," Cambridge University Press -- Textbook development of operational quantum theory.

### Tertiary references (background)

- **Gudder (2005)**, "Open problems for sequential effect algebras," Int. J. Theor. Phys. 44, 2199. Some problems now resolved by vdW and WWvdW.
- **Gudder, Greechie (2005)**, "Uniqueness and Order in Sequential Effect Algebras," Int. J. Theor. Phys. 44, 755.
- **McCrimmon (2004)**, "A Taste of Jordan Algebras," Springer -- Comprehensive Jordan algebra textbook including Peirce decomposition (Ch 17).
- **Iochum (1984)**, "Cones autopolaires et algebres de Jordan," Lecture Notes in Math. 1049 -- Self-dual cones and Jordan algebras.

### Lean formalization references (Phase 58)

- **Ax-Prover team (2025)**, "A Formalization of the Generalized Quantum Stein's Lemma in Lean," [arXiv:2510.08672](https://arxiv.org/html/2510.08672) -- First deep operator-algebra Lean formalization; style baseline.
- **Lean-QuantumInfo** library, [description at emergentmind.com](https://www.emergentmind.com/topics/lean-quantuminfo-library) -- Quantum channels, entropies in Lean 4.
- **mathlib4 Algebra.Jordan.Basic**, [mathlib4 docs](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Jordan/Basic.html) -- Elementary Jordan algebra stub only; no JB/JBW formalization.

### Internal GPD references (HIGH confidence, directly used)

- **GPD Phase 4-06**, "Peirce Feedback Extension," completed 2026-03-21, commit `9608ac54`. Located at `.gpd/phases/04-sequential-product-formalization/04-06-PLAN.md` and `04-06-SUMMARY.md`. Derived corrected sequential product with explicit Peirce 1-space and 2-space structure (Eq. 04-06.4). **CORE prior art for Phase 54.**
- **GPD Phase 4 research**, `.gpd/phases/04-sequential-product-formalization/04-RESEARCH.md` -- Comprehensive sequential product axiom analysis with references.
- **GPD Phase 5 (v2.0)**, local tomography and C*-promotion. Established the derivation chain from SP + local tomo => M_n(C)^sa.
- **GPD Phase 6 (v2.0)**, paper assembly (predecessor of Paper 5). See commit `feffb9bf`.
- **GPD Phase 28**, "Peirce Verification and V_0 Channel Exploration" -- Computational verification of Peirce structure in h_3(O) Albert algebra context; different phase (v13.0) but Peirce machinery is related.

---

## Confidence Assessment

| Area | Confidence | Notes |
|------|-----------|-------|
| Primary axiom sources (vdW, Alfsen-Shultz, Niestegge) | HIGH | Published, well-reviewed, decades-stable |
| Phase 54 (A) outcome feasibility via GPD Phase 4-06 formula | HIGH | Already proved internally; restate and check |
| Phase 54 (B) outcome (precise external citation) | LOW | Literature is silent in the exact form required; no Alfsen-Shultz theorem matches |
| Phase 55 (S4 facial structure) | MEDIUM | vdW Prop 30 + AS facial structure likely suffice for (A); no direct (B) |
| Phase 56 (Thm 5.8 upper bound) | MEDIUM | WWvdW 2020 classification relevant; needs analysis |
| Phase 57 (Phi wrapper) | HIGH | Non-citation issue; exposition defense needed |
| Phase 58 (Lean axiom audit) | MEDIUM-HIGH | Current Lean ecosystem well-surveyed; bespoke axioms expected; one-to-one citation mapping is correct deliverable |
| Phase 59 (minimal composite) | HIGH | Literature complete; vdW 2019 Thm 3 + Barnum-Wilce 2014 |

---

## Quality Gate Compliance

- [x] Every reference concrete and locatable (author + year + venue + arXiv/DOI)
- [x] Alfsen-Shultz 2003 page references include explicit chapter (Ch 7, Ch 2, Ch 8) where proposed as partial support
- [x] Distinguished "Peirce decomposition exists" (AS 2003 Ch 2) from "SP preserves Peirce subspaces" (NOT in AS; not found anywhere) -- this distinction is central
- [x] Flagged literature silence at Phase 54 as a (C) outcome signal explicitly
- [x] Included vdW "Three characterisations" (arXiv:1803.08453)
- [x] Included EJA / JB-algebra axiomatizations: Hanche-Olsen-Stormer (Peirce decomposition = derived from JB axioms), Iochum (self-dual cones + Jordan); neither takes Peirce invariance of sequential product as axiom or theorem in the §3.3 form
- [x] Noted GPD v2.0 Phases 4-6 prior art: Phase 4-06 Peirce feedback extension is the CORE internal reference for Phase 54

---

_Prior Work compiled 2026-04-16 for v14.0 Paper 5 revision cycle._
_Next step: orchestrator reviews this file, confirms Phase 54 outcome expectation (A via Phase 4-06 internal prior art, or (C) if argument must start from S1+S3 axioms alone), then spawns Phase 54 planner._
