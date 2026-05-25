# Known Pitfalls Research: Paper 5 JMP Revision -- Six Jigsaw-Piece Gaps

**Domain:** Axiomatic quantum mechanics from sequential-product axioms; spectral order unit spaces in the Alfsen-Shultz sense; Peirce decomposition for compressions; JB-algebra / EJA identification; operator-algebra formalization in Lean 4
**Researched:** 2026-04-16
**Confidence:** HIGH for circularity-ordering pitfalls (R1-R4), literature-citation precision (R5-R7), and Lean-axiom audit (R8-R9); MEDIUM-HIGH for cross-phase sequencing (R10-R11); MEDIUM for referee-timeline risk (R12)

**Scope:** Pitfalls specific to v14.0 -- closing six load-bearing jigsaw gaps in Paper 5 "QM from Self-Modeling" (submitted to JMP 2026-03-28, ref JMP26-AR-00922) before the referee report lands. The submission is frozen at git tag `paper5-jmp-submitted`; revision happens in `main.tex`. Six phases are planned: 54 (§3.3 Peirce preservation), 55 (S4 facial structure), 56 (Thm 5.8 W upper bound), 57 (Phi inert-wrapper), 58 (Lean axiom audit), 59 (minimal composite defense).

**Relationship to prior pitfall files:** v12.0 pitfalls P1-P9 and v13.0 pitfalls C1-C12 covered Paper 6 (spacetime/SUSY). This file (R1-R12) is orthogonal: it covers the revision mechanics for Paper 5, not the physics chain downstream of it. The v2.0 Phase 4 work established the corrected sequential-product formula `a & b = Σ λ_i C_{p_i}(b) + Σ √(λ_i λ_j) P_{ij}(b)` (Eq. 04-06.4); the present milestone's pitfalls concern whether Paper 5's EXPOSITION of that derivation survives referee scrutiny at the step level, not whether the math is right.

**Key stance:** The failure modes here are subtle because the paper is already internally consistent at the reading level. The question is whether each argument is RECONSTRUCTIBLE FROM PRIMITIVES by a skeptical reader, not whether it is VISUALLY PLAUSIBLE to the author. Every pitfall below distinguishes "looks right" from "is right from the stated primitives."

---

## Critical Pitfalls

### R1: Assuming the Conclusion -- Using Jordan Structure to Prove Something Meant to Derive Jordan Structure

**What goes wrong:**
Paper 5's strategic core is that Jordan-algebra structure is DERIVED from sequential-product axioms (van de Wetering Theorem 1), not assumed. Any argument in §3.3 (or any phase revising it) that invokes "a ∘ b is a Jordan product," "the Jordan identity `a²`∘(b∘a) = (a²∘b)∘a`," or "self-adjoint operator multiplication" to prove Peirce invariance of `a ∘ (−)` has circularly assumed what it was meant to derive. The same trap applies to invoking "operator compression" in the B(H) sense (i.e., x ↦ pxp) rather than "Alfsen-Shultz compression" in the OUS sense (positive projection c_p with specified order-theoretic properties).

Concretely: the claim Phase 54 must prove is that `a ∘ V_2(p_i) ⊆ V_2(p_i)` and `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)` using ONLY (S1) additivity in the second argument, (S3) `1 ∘ a = a` and sharp constraint `a ∘ b = c_a(b)` when a is projective, order-unit-space primitives, and Alfsen-Shultz compression properties. Any appeal to `(a ∘ b) = (1/2)(ab + ba)` with ab, ba understood as operator products is a circular step.

**Why it happens:**
The mental model Paper 5 assumes -- M_n(C)^sa with Lüders product -- is the prototype for everything. When writing exposition, it is natural to verify claims by "checking on M_n(C)^sa" and then asserting the general case by analogy. But the analogy is the thing being derived; analogy-to-M_n(C) is the payload of the theorem, not a proof tool. Additionally, "compression" has two meanings (B(H)-compression `pxp`, A-S compression `c_p`) that coincide for projectors in M_n(C) but are distinct primitives in an abstract OUS.

**Consequences:**
A referee will correctly identify the argument as circular. If §3.3 depends on §4 or §5 results that depend on §3.3, the paper's derivation spine is broken even though every individual claim may be true. Outcome (C) of the Phase 54 deliverable matrix.

**Prevention:**
- Every proof attempt in Phase 54 must begin with an explicit allowed-tool list: order unit, ≤, ||·||, `c_p` (with its A-S axioms: idempotent, positive, `c_p + c_{p'} = id` on sharp effects' face, `c_p(p) = p`), S1, S3, linearity, finite dimension.
- Explicit forbidden-tool list: Jordan multiplication `·`, `a² = a∘a` with any associativity-style manipulation, `M_n(C)^sa`, JB-algebra spectral theorem, `vdW Theorem 1`, anything from §4 or §5 of Paper 5, any result downstream of the sequential product being proved to be a Jordan operation.
- Adversarial review must apply grep for forbidden tokens in the proof: `M_n`, `M_2(C)`, `Jordan product`, `EJA`, `f(λ,μ) = √(λμ)` (this last formula IS a conclusion of §3.3/§4, not a primitive available to §3.3's proof).

**Detection:**
Grep patterns on any RESULT.md or proof file: `"since .* Jordan"`, `"because .* Jordan"`, `"M_n\(C\)"`, `"Lüders"`, `"M_2"`, `"operator product"`, `"pxp"`, `"√a.*b.*√a"`. Any hit is suspect. Also: if the proof is shorter than 30 lines for a claim about compositions of compressions and Peirce projections in an abstract OUS, it is likely hand-waving.

**Phase to address:** Phase 54 (primary). Phase 56 secondary (Thm 5.8 W upper bound: asserting "W carries a product-form sequential product" must not implicitly assume W is already Jordan-structured). Phase 58 tertiary (Lean axiom audit: an `axiom` that states "sequential product of Jordan elements is Jordan" is a circular axiom, not a genuine primitive).

**References:**
- Paper 5 v2.0 Phase 4 (04-06-SUMMARY.md): established the Peirce-feedback formula with explicit "circularity audit" deliverable; reuse this audit pattern.
- van de Wetering (2019), "Sequential product spaces are Jordan algebras," JMP 60, 062201 (arXiv:1803.11139). Theorem 1 is the sink, not the source: a proof in §3.3 that uses Theorem 1's conclusion has inverted the dependency.
- Alfsen-Shultz (2003), "Geometry of State Spaces of Operator Algebras," Birkhäuser. Compressions are defined order-theoretically; see Ch. 7-8.

---

### R2: Conflating Peirce Decomposition (Fact About V) with Peirce Invariance (Claim About a ∘ (−))

**What goes wrong:**
The Peirce decomposition `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i, p_j)` is a theorem about the space V with respect to a family of orthogonal projective units {p_i}. It says V splits into subspaces -- nothing more. The claim Phase 54 needs is that the linear map `L_a : b ↦ a ∘ b` preserves this splitting, i.e., that each summand is L_a-invariant. These are DIFFERENT statements.

Decomposition ≠ invariance. Every space that admits a family of orthogonal projections decomposes; whether a given endomorphism respects the decomposition is a separate question. Citing "Peirce decomposition (Alfsen-Shultz)" as the justification for "`a ∘ V_2(p_i) ⊆ V_2(p_i)`" is a cited non-sequitur.

**Why it happens:**
"Peirce" is load-bearing language in Paper 5. In Jordan theory, "the Peirce decomposition of V with respect to p" is often presented with simultaneous claims about how Jordan multiplication respects the decomposition -- because in a Jordan algebra, Jordan multiplication DOES respect the decomposition. But this is a theorem requiring the Jordan product's properties; it is not free. In an OUS with only S1 and S3, no such result is automatic.

**Consequences:**
If this conflation passes, §3.3 has zero content for the invariance claim -- it has only cited that V decomposes. The reviewer will correctly say "you have cited decomposition; where is invariance?"

**Prevention:**
- In Phase 54's claim.md, state Peirce DECOMPOSITION and Peirce INVARIANCE as two separate propositions. Prove invariance; decomposition is a given.
- In Phase 55 (S4 facial structure), distinguish "face F_p of the state space exists and corresponds to projective unit p" (A-S geometric fact) from "orthogonality of effects factors through face structure in a phi-independent way" (the claim Paper 5 makes in §3.4 for S4).
- Any passage in main.tex of the form "the Peirce decomposition theorem gives X" should be audited for whether X is a decomposition statement or an invariance / preservation statement.

**Detection:**
Grep `main.tex` for `Peirce`. For each hit, classify the sentence: decomposition statement (V splits) or invariance/action statement (some map respects the split). All invariance statements need proofs distinct from decomposition citations.

**Phase to address:** Phase 54 (central). Phase 55 (analogous conflation for face structure).

**References:**
- Alfsen-Shultz (2003), Ch. 8 treats Peirce decomposition for JB-algebras with the Jordan product's action on the decomposition simultaneously. In a pre-Jordan OUS, only the decomposition part is available.
- Foulis-type spectral compression bases (arXiv:2102.01628, "Geometric and algebraic aspects of spectrality in order unit spaces"): confirms decomposition-in-OUS is strictly weaker than A-S spectrality, and A-S spectrality is strictly weaker than Jordan-algebra structure.

---

### R3: Confusing Single-Compression Invariance with Composite-Map Invariance

**What goes wrong:**
Alfsen-Shultz establishes that individual compressions `c_{p_i}` are idempotent positive projections whose ranges are the Peirce 2-spaces: `c_{p_i}(V) = V_2(p_i)` and `c_{p_i}` fixes V_2(p_i) pointwise. This is a statement about the LIST of maps `{c_{p_i}}`. The claim in §3.3 is about a SINGLE map `L_a : b ↦ a ∘ b` where `a = Σ λ_i p_i`. One does not trivially imply the other, because the corrected sequential product is not just a sum of compressions -- it includes Peirce-1-space terms with mixing coefficients.

Specifically, v2.0 Phase 4 established:
```
a & b = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} √(λ_i λ_j) P_{ij}(b)
```
The first sum operates via compressions and therefore preserves V_2(p_i) by A-S. The second sum involves `P_{ij}(b) = b − Σ_k C_{p_k}(b)`, the Peirce-1 projection. Its invariance on V_1(p_i, p_j) is a SEPARATE claim requiring proof. The phrase "compressions preserve Peirce subspaces" is true of the first sum's factors; it does NOT by itself give invariance of the full sum.

**Why it happens:**
When reading the formula `a & b = Σ λ_i C_{p_i}(b) + ...`, the eye sees "compressions appear; compressions preserve Peirce spaces; therefore the whole thing does." But linearity of L_a requires each TERM in the sum to preserve the relevant subspace, and the mixed-coefficient Peirce-1 term is a new object. Also: even for the diagonal part, `C_{p_i}` preserves V_2(p_i) but sends V_1(p_j, p_k) to... what? A-S says `c_{p_i}` sends V_1(p_i, p_j) to zero (the off-diagonal-involving-p_i part gets killed). The composite map's action on V_1(p_j, p_k) for i ∉ {j,k} is a case analysis, not a one-liner.

**Consequences:**
A proof that only cites "compressions preserve Peirce spaces" has proved nothing about `L_a`'s block structure. Outcome (B) from the Phase 54 deliverable matrix would require a precise citation; none exists for the composite-map claim specifically.

**Prevention:**
- Phase 54's proof MUST do case analysis on L_a's action on each Peirce subspace: V_2(p_i), V_1(p_i, p_j), and cross-terms V_1(p_k, p_l) with k ≠ i, l ≠ i, l ≠ j.
- For the corrected formula (v2.0 Eq. 04-06.4), each of the two sums needs independent invariance verification.
- An explicit lemma: "If T_1, T_2, ..., T_n are linear maps each preserving subspace W, then Σ c_k T_k preserves W." This is trivial but should be STATED so the argument is not hand-waved as "sum of invariant-preserving maps."

**Detection:**
In any Phase 54 proof, check: does the proof address BOTH the compression-sum term AND the mixing term? If only one, the proof is incomplete. Grep for `P_{ij}` or "Peirce-1 term" or "mixing function" -- these should appear in a complete proof.

**Phase to address:** Phase 54 (central).

**References:**
- v2.0 Phase 4 Plan 06 summary (`04-06-SUMMARY.md`): the formula decomposition that makes the case analysis explicit. Phase 54 should reuse this structure.
- Alfsen-Shultz (2003) Ch. 7: individual-compression properties.
- vdW Def. 2 (S1, S3): the only axioms allowed.

---

### R4: "It's Obvious" Rate-Limiting

**What goes wrong:**
The Paper 5 §3.3 passage at lines 508-528 spends ~20 lines asserting Peirce invariance of `a ∘ (−)`. If the claim were obvious, those 20 lines would be a one-liner. The word "obvious" (or synonyms "clearly," "immediately," "of course") in a revision of a passage that was already 20 lines is a sign that the writer has given up trying to prove the claim and is using rhetorical weight as a substitute. Reviewers recognize this instantly.

More dangerously: "obvious" in the revision can LOSE information. If the original 20 lines were doing actual work, compressing to "obviously, a ∘ (−) preserves each Peirce subspace" deletes whatever structure was being built. The revision gets shorter but weaker.

**Why it happens:**
Pressure to make §3.3 tighter, plus the author's correct intuition that the claim IS true on M_n(C)^sa, combine to make a shortcut tempting. The shortcut fails because:
1. The reader does not share the author's mental picture.
2. True-on-M_n(C)^sa ≠ proved-from-OUS-primitives.
3. A reviewer's job is to NOT accept "obvious."

**Consequences:**
A revised §3.3 that is shorter than the original but does not resolve the gap is worse than the original. The reviewer may approve the shorter version on first read (less to object to), but flag it harder on second read (content was removed without replacement).

**Prevention:**
- In Phase 54's RESULT.md, if outcome is (A) -- proof from primitives -- the proof must be at least as long as the original 20 lines. If shorter, something is missing.
- Forbidden words in the revised §3.3: "obvious," "obviously," "clearly," "immediately follows," "of course." These are acceptable ONLY following a cited theorem number with a page reference.
- Adversarial review: a second agent with "ruthless skeptic" persona must read the proof and attempt to find the gap.

**Detection:**
Word-count comparison: revised §3.3 length vs. submitted §3.3 length (lines 508-528 of main.tex). Grep for rhetorical shortcuts in the revision.

**Phase to address:** All phases 54-59, especially 54 and 57 where exposition is dense.

**References:**
- Tao's blog post "The 'no self-defeating object' argument" and related meta-mathematical discussions of when rhetorical shortcuts substitute for proof. (General methodological reference; no specific URL needed.)

---

### R5: Vague Alfsen-Shultz Citations -- "AlfsenShultz2003" Without Theorem Number

**What goes wrong:**
Paper 5 currently cites `\cite{AlfsenShultz2003}` throughout §2-3 without theorem or proposition numbers. The book is 467 pages. "Alfsen-Shultz 2003" as a general citation tells the reader "there's a book somewhere that justifies this" -- which is functionally equivalent to no citation. A referee will correctly demand the specific theorem or proposition being invoked.

Additionally: Alfsen-Shultz has TWO relevant books, and the citation must distinguish:
- Alfsen & Shultz (2001), *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products* (Birkhäuser Progress in Mathematics v. 179)
- Alfsen & Shultz (2003), *Geometry of State Spaces of Operator Algebras* (Birkhäuser Progress in Mathematics v. 190)

These are sequentially-written volumes on the same topic with different theorem numbering. Paper 5 cites "2003" -- so the second volume -- but §3.3 invokes compression theory which is developed primarily in the 2001 volume's Ch. 7-8. The citation may be to the wrong volume for some invocations.

**Why it happens:**
Early-draft physics habit: cite the book, worry about pages later. "Later" never arrives. Also: LaTeX's `\cite` completion makes `AlfsenShultz2003` trivially available and there is no compiler warning if the citation is imprecise.

**Consequences:**
For Phase 55 outcome (B), the deliverable is "precise Alfsen-Shultz citation" meaning chapter + section + theorem. A bare `\cite{AlfsenShultz2003}` does not satisfy this. The referee will flag it. Worse: if the claim isn't actually in A-S, the citation is wrong AND imprecise.

**Prevention:**
- Phase 55 must produce `alfsen-shultz-notes.md` with, for each Paper 5 invocation of A-S, the specific theorem/proposition number and which volume (2001 or 2003).
- Replace `\cite{AlfsenShultz2003}` with `\cite[Thm X.Y.Z]{AlfsenShultz2003}` form in all §3.3-§3.5 invocations.
- If a claim is not found in either A-S volume at the stated precision, flag it: the claim may be folklore, may require a proof, or may be false. Folklore claims should be proved inline; false claims are the whole point of the milestone to catch.

**Detection:**
`grep -n "cite{AlfsenShultz" main.tex` followed by `grep -n "cite\[" main.tex | grep AlfsenShultz`. The first count should equal the second count in a clean revision. Any `\cite{AlfsenShultz...}` without square brackets containing a theorem number is an offender.

**Phase to address:** Phase 55 (primary deliverable), Phase 54 (inherited: §3.3 citations). Phase 58 (Lean axioms that cite A-S must also cite precisely).

**References:**
- Alfsen & Shultz (2001), Progress in Math v. 179. Covers basic theory, orientations, compressions for C*-algebras.
- Alfsen & Shultz (2003), Progress in Math v. 190. Covers geometry of state spaces, Jordan-algebra state spaces, facial structure.
- Published review of A-S by Araki (2004 AMS Bull) notes the volumes have distinct but related content.

---

### R6: Face-Phi-Independence Leaning on State Separation (Which Leans on Jordan)

**What goes wrong:**
Paper 5 §3.4 (or the S4 axiom verification) argues that facial orthogonality of effects is phi-independent: whether two effects a, b are F-orthogonal (their supporting faces don't overlap) does not depend on the self-modeling map phi. This is the crucial claim that lets S4 (`a ∘ b = 0 ⟹ b ∘ a = 0`) be checked once rather than for every phi.

The subtle pitfall: facial orthogonality IS phi-independent, BUT the proof that this is so may implicitly use state separation (different faces = different sets of separating states), and state separation in an OUS that is not a priori known to be Jordan requires either (i) Alfsen-Shultz spectrality + projective units + separating families (A-S chapters 7-9, proved in the ORDER-UNIT setting) or (ii) Jordan-algebra structure. If Paper 5's argument accidentally routes through (ii), it is circular again.

Barnum-Wilce (2014) and subsequent work on reconstruction consistently note that the step from "operational structure" to "faithful separating state family" is load-bearing and often proved via techniques that presuppose more than the stated axioms. This has been a recurring referee objection in the field.

**Why it happens:**
In practice, everyone works in M_n(C)^sa where states (density matrices) separate effects automatically. In a general OUS, A-S separation is a theorem of spectrality theory, not a free fact. When writing the paper, the step "effects a, b have disjoint supporting faces ⟹ distinguishable by states ⟹ S4 holds independent of phi" elides which version of "states separate effects" is being used.

**Consequences:**
If Phase 55 finds the phi-independence proof uses separation-via-Jordan, §3.4 has a circularity at S4 -- parallel to the §3.3 circularity for Peirce. Mitigation is harder because S4 is the axiom that promotes OUS to EJA via vdW Theorem 1; if S4's verification circularly uses EJA structure, the whole derivation chain collapses.

**Prevention:**
- Phase 55's proof of phi-independence of facial orthogonality must explicitly track what "face" means: A-S geometric face (defined by extreme-point support on the state space) or EJA-face (Peirce 2-space of a projector). For the argument to be non-circular, the geometric face definition must be in play, and separation of faces by states must come from A-S (not from EJA).
- If A-S separation requires spectrality, and spectrality requires... check the dependency graph in Alfsen-Shultz (2001) Ch. 7-9 versus (2003) Ch. 1-2. Do NOT use anything that Paper 5 has not yet established.
- Cross-reference with van de Wetering's paper: vdW assumes spectral OUS as input to his Theorem 1. If Paper 5 is proving it is a spectral OUS, the spectrality cannot be invoked during the proof.

**Detection:**
In Phase 55 work, for every invocation of "states separate effects" or "faces are determined by extreme states," trace the justification back to an explicit axiom list. If the trace hits Jordan structure, EJA classification, or any vdW Theorem 1 consequence, the argument is circular.

**Phase to address:** Phase 55 (central), Phase 54 (if §3.3 uses similar separation arguments).

**References:**
- Barnum, Wilce (2014), "Local Tomography and the Jordan Structure of Quantum Theory," Found. Phys. 44, 192-212 (arXiv:1202.4513). Discusses separation assumptions in operational reconstructions.
- Barnum, Graydon, Wilce (2020), "Composites and Categories of Euclidean Jordan Algebras," Quantum 4, 359 (quantum-journal.org/papers/q-2020-11-08-359/). Explicit on which composition constraints preserve Jordan structure versus require it as input.
- Alfsen-Shultz (2001), Ch. 7-9 for spectral theory and separation in OUS.

---

### R7: Thm 5.8 Upper Bound -- "Carries" is Ambiguous Between Closure and Structural Preservation

**What goes wrong:**
Paper 5 Theorem 5.8 asserts an upper bound via a substructure W that "carries" the product-form sequential product on the composite. "Carries" is an informal word; its precise meaning matters. Concretely, "W carries the product" can mean:
1. **Closure:** For all `a, b ∈ W`, the product `a ∘ b` (defined on the ambient space) lies in W.
2. **Induced structure:** W with the ambient product RESTRICTED to W is itself a sequential-product space (all axioms S1-S7 hold on W).
3. **Functorial preservation:** W with the ambient product satisfies the axioms AND the inclusion `W ↪ V` is a morphism of sequential-product spaces.

These are three progressively stronger claims. (1) is sometimes true without (2): the product closes but associativity of compatible effects (S5) fails on W because compatibility in W differs from compatibility in V. (2) is sometimes true without (3): W is internally a SPS but the inclusion is not structural (e.g., compressions in W are not A-S compressions inherited from V).

The Gudder-Greechie literature contains an explicit counterexample (Example 39 in several SEA papers): a sequential effect algebra that is NOT order-isomorphic to the unit interval of a EJA, whose sequential product IS associative -- meaning "abstract SEA + associativity" does not imply "EJA substructure." This counterexample is directly analogous to what can go wrong with Thm 5.8's W.

**Why it happens:**
The word "carries" reads as obviously meaning (3), but many proof attempts only establish (1). In the literature, this kind of equivocation has been flagged in Barnum-Graydon-Wilce's work on Jordan composites: not every subalgebra of an EJA is itself an EJA under the induced product.

**Consequences:**
If Thm 5.8's proof only establishes (1) but the downstream use requires (2) or (3), the theorem is too weak to serve its purpose. The upper bound is not actually bounding.

**Prevention:**
- Phase 56's work must explicitly state which sense of "carries" is intended and prove that sense.
- For each of S1-S7, prove the axiom holds on W with the induced product. Do not assume that "W is closed under ∘" suffices.
- Check: if W is a spin factor V_n with n ≥ 4 (one of the EJA types that fails local tomography), does the composite product on V ⊗ V restrict to a product on W ⊗ W that is still SPS? The answer may be no, making Thm 5.8 inapplicable in that case.
- Look for classical counterexamples in EJA literature: the Albert algebra h_3(O)'s behavior under tensor composition is the canonical source of "closes but not structurally" pathologies.

**Detection:**
In Phase 56's deliverable, grep the proof for the word "carries" or "inherits" or "restricts to." For each, verify an explicit S1-S7 check has been performed on W.

**Phase to address:** Phase 56 (central). Phase 59 (minimal composite: similar issues about what structure the composite inherits).

**References:**
- Gudder, Greechie (2002), "Sequential products on effect algebras," Rep. Math. Phys. 49, 87. Example 39 of associative non-EJA SEA.
- Westerbaan, Westerbaan, van de Wetering (2020), "The three types of normal sequential effect algebras," Quantum 4, 378. Catalogs which SEA types are vs. are not EJA-embedded.
- Barnum, Graydon, Wilce (2020), "Composites and Categories of Euclidean Jordan Algebras," Quantum 4, 359. Composites-of-EJAs subtleties.

---

## Moderate Pitfalls

### R8: Phi Cross-Section Equivocation -- Same Symbol, Different Objects Across Sections

**What goes wrong:**
Paper 5's phi (the self-modeling map) appears in multiple roles across sections. Common uses include:
- §2: phi as a map from B's effect space to M's effect space, parametrizing the self-model.
- §3: phi as a tracking map whose faithfulness selects the mixing function `f = √(λμ)` (v2.0 Phase 4 result).
- §4: phi as an inert wrapper around the sequential product, with the product's structure not depending on phi beyond faithfulness.
- §5-6: phi possibly reinterpreted or specialized in the local-tomography and C*-completion arguments.

If phi means slightly different things in different sections -- different domain/codomain, different faithfulness condition, different role -- a reviewer will correctly say "which phi? At line X you treat phi as inert wrapper; at line Y you use a specific property that inert wrappers do not have."

**Why it happens:**
Progressive refinement during drafting: each section locally makes sense with its version of phi, but the global consistency is never audited. This is a standard revision pitfall for papers with a single symbol doing heavy lifting.

**Consequences:**
Referee complains "phi is overloaded." Revision must either rename the different roles or prove they all coincide.

**Prevention:**
- Phase 57 must produce an explicit phi-audit: every occurrence of phi in main.tex, what role it plays there, what properties are assumed.
- If multiple roles are in fact the same object, prove coincidence explicitly.
- If multiple roles are different objects, rename: `\phi_{\text{track}}`, `\phi_{\text{inert}}`, etc., or (better) restructure the paper so phi is introduced once and used consistently.

**Phase to address:** Phase 57.

**References:**
- v2.0 Phase 4 Plan 06: established that faithful phi selects `f = √(λμ)`. This is the "essential phi" role.
- Standard paper-revision methodology: Strunk-White (rule 17), stable referents across sections.

---

### R9: Lean Axiom Audit -- Three Failure Types

**What goes wrong:**
Paper 5's Lean 4 formalization has 16 axioms and 0 sorry. Each axiom can be:
- **Type (i): Theorem-in-disguise.** The axiom states something that is actually a theorem (in Alfsen-Shultz, in vdW, or derivable from earlier axioms). Keeping it as axiom either (a) admits the proof was hard and skipped, or (b) hides a non-trivial mathematical step from the reader. Either way, a skeptical referee will ask for the proof.
- **Type (ii): Definition-as-axiom.** The axiom declares a STRUCTURE that should be introduced via `def` or `structure`. E.g., `axiom compression_is_idempotent : ∀ p, c p (c p x) = c p x` is really part of the definition of compression, not an axiom. Lean will accept this, but it misrepresents the logical role.
- **Type (iii): Statement-mismatch.** The axiom states a claim whose wording doesn't quite match the cited published theorem. E.g., axiom states `a ∘ b = c_a(b)` for all effects, but the cited A-S proposition requires a to be PROJECTIVE (sharp). This is a silent strengthening and is a correctness bug in the formalization.

Mathlib community has flagged type (iii) as the most dangerous: type-correct code that does not match the cited mathematics. A type-(i) or type-(ii) axiom is annoying; a type-(iii) axiom can make the formalization unsound relative to its cited justification.

**Why it happens:**
- Type (i): early development used `axiom` to make progress; converting to `theorem` was postponed.
- Type (ii): formalization starts from the paper's wording, which conflates definitional properties with theorems.
- Type (iii): paper's informal language is imprecise (missing "projective," "sharp," "compatible" qualifiers); formalization copies the informal statement.

**Consequences:**
For a JMP referee, Lean formalization is supplementary. But 0 sorry with 16 axioms is not equivalent to 0 sorry with 3 axioms if those 16 contain type-(i) and type-(iii) entries. The formalization's credibility hinges on what the axioms actually are.

**Prevention:**
- Phase 58 must classify each of the 16 axioms: (i), (ii), or (iii) + "genuine primitive."
- Type (i): prove it, demote to `theorem`.
- Type (ii): refactor into `def` / `structure`.
- Type (iii): either (a) prove the STRONGER statement (if true from the cited source), or (b) weaken to the cited version and audit downstream proofs for whether they still compile.
- Produce an axiom manifest with one-line justification for each remaining axiom: "genuine primitive because no OUS primitives can derive it, and it is assumed throughout the A-S / vdW framework."

**Phase to address:** Phase 58 (central).

**References:**
- Mathlib4 axiom conventions: `leanprover-community/mathlib4` README and CONTRIBUTING. Axioms are reserved for genuine extensions to the core Lean logic (e.g., `Classical.choice`) plus a short controlled list; adding axioms in application code is discouraged.
- Avigad-Massot, *Mathematics in Lean* v4.19 (2025). Best practices for Lean formalization of research mathematics.
- Zulip discussions (leanprover-community.zulipchat.com): periodic threads on axiom audits for research formalizations.

---

### R10: Minimal Composite / Simplicity Assumption as Adversarial-Review Magnet

**What goes wrong:**
Paper 5 relies (in §5-6, and by reference to vdW Theorem 3) on a minimal-composite or simplest-composite assumption to pick out C*-algebra structure from EJA structure. Some form of this assumption is unavoidable in any Jordan-to-C* promotion. But the specific FORM of the assumption, and its operational motivation, are classical attack surfaces in axiomatic QM reviews.

Historical pattern:
- Hardy's 2001 "Five Reasonable Axioms" paper had a "Simplicity" axiom that postulated the smallest-dimensional solution is realized. This was immediately criticized as un-motivated; subsequent reconstructions (Masanes-Müller, Dakić-Brukner, Chiribella-D'Ariano-Perinotti) explicitly REMOVED Hardy's simplicity and replaced it with more operational axioms.
- Chiribella-D'Ariano-Perinotti's purification axiom, while operational, still takes flak for being "not physically obvious."
- Masanes-Müller's (2011) reconstruction uses "continuous reversibility" in place of simplicity.
- Barnum-Wilce's use of local tomography attracts the same objection: why THIS composite axiom?

Every one of these gets flagged by some reviewer. Paper 5's minimal-composite assumption will be flagged.

**Why it happens:**
Operational axioms are never fully uncontroversial. There is always a choice between multiple formulations (Hardy-simplicity, CD-P-purification, Masanes-reversibility, local-tomography, independent-accessibility) and a committed opponent can attack any single choice. The defense is to (a) show your formulation is operationally well-motivated, (b) show it is IMPLIED by more primitive self-modeling considerations, or (c) show it is weaker than / equivalent to the standard literature formulations.

**Consequences:**
Without a prepared defense, Phase 59's work amounts to "we assume it because we need it" -- which is exactly the objection the milestone wants to preempt.

**Prevention:**
- Phase 59 must produce an explicit comparison: Paper 5's minimal-composite axiom vs. local-tomography (Barnum-Wilce, vdW Thm 3) vs. purification (Chiribella et al.) vs. independent-accessibility (Paper 5's earlier sections). Where in the implication chain does Paper 5's axiom sit?
- Produce at least one operational motivation: "if the self-model M is to faithfully represent B, the composite B ⊗ M must be... [specific property]. This is what minimal-composite encodes." Bryan's intuition is NOT a shortcut here; the motivation must be mathematically tight.
- Anticipate three specific reviewer objections: (a) "why not purification instead?"; (b) "is this just local tomography renamed?"; (c) "does this exclude interesting non-standard QM (e.g., real QM)?" Prepare written responses.

**Phase to address:** Phase 59.

**References:**
- Hardy (2001), "Quantum Theory From Five Reasonable Axioms," arXiv:quant-ph/0101012. Original "Simplicity."
- Masanes, Müller (2011), "A derivation of quantum theory from physical requirements," NJP 13, 063001 (arXiv:1004.1483). Replaces simplicity with reversibility.
- Chiribella, D'Ariano, Perinotti (2011), "Informational derivation of quantum theory," PRA 84, 012311 (arXiv:1011.6451). Purification axiom.
- Dakić, Brukner (2011), "Quantum theory and beyond: is entanglement special?" Also post-Hardy reconstruction.
- Barnum, Wilce (2014), arXiv:1202.4513. Local tomography route.
- Hardy-critique literature: see "The operational framework for quantum theories is both epistemologically and ontologically neutral" (ScienceDirect, Hagar-Hemmo type critique).

---

### R11: Cross-Phase Sequencing -- Phase 54 Outcome (C) Cascading

**What goes wrong:**
The phases 54-59 are scoped sequentially but their dependencies are not linear. If Phase 54's outcome is (C) -- structural gap, Peirce invariance requires Jordan structure Paper 5 hasn't yet derived -- then:
- Phase 55's S4 facial-structure argument may have the same circularity (similar proof strategy).
- Phase 56's Thm 5.8 W upper bound may rest on the Peirce-invariance claim.
- Phase 57's phi-inert-wrapper argument depends on whether the product's block structure is phi-independent, which depends on Peirce invariance.
- Phase 58's Lean axiom audit may reveal the circular dependency already encoded as an axiom.
- Phase 59's minimal-composite defense may be premature if upstream axioms are suspect.

If Phases 54-59 run strictly in sequence and Phase 54 is (C), phases 55-59 do not automatically pause -- they may accumulate work that assumes Phase 54's outcome is (A) or (B).

Conversely: running 54-59 in parallel risks duplicating work (the same Alfsen-Shultz citation audit would be repeated in Phases 54, 55, 57) and allowing inconsistent resolutions (Phase 55 uses a spectrality assumption that Phase 54 ruled out).

**Why it happens:**
Milestone is scoped as "six gaps, six phases" without a dependency DAG. Plus the urgency of the JMP referee timeline (see R12) creates pressure to parallelize.

**Consequences:**
Best case: duplicated work. Worst case: phases close with contradictory resolutions, and the paper revision is internally inconsistent.

**Prevention:**
- Roadmapper (downstream consumer of this PITFALLS file) must produce a dependency graph:
  - Phase 54 is the root; its outcome determines the pattern.
  - Phase 55 depends on Phase 54's Alfsen-Shultz citation audit (shared deliverable).
  - Phase 56 depends on Phase 54's resolution of Peirce invariance (used downstream).
  - Phase 57 depends on Phase 54 AND Phase 55 (phi inertness requires both Peirce and facial structure to be phi-independent).
  - Phase 58 runs concurrently with 54-57 but MUST be re-audited after they close.
  - Phase 59 is mostly independent but depends on Phase 56's formalization of "composite structure."
- Define a single shared `alfsen-shultz-notes.md` produced in Phase 54, consumed in Phases 55, 57, 58.
- Gate: Phase 55 cannot start until Phase 54 closes with (A), (B), or (C). If (C), orchestrator must pause for human decision before Phase 55 proceeds.

**Phase to address:** Orchestration / roadmap construction, not a specific phase. Relevant to all phases 54-59.

**References:**
- Paper 5 revision prompt (`paper5-revision-prompt.md`): explicitly states Phase 1 (= Phase 54) outcome (C) "pauses milestone for human decision." Inherit this gating pattern to 55-59.

---

## Minor Pitfalls

### R12: JMP Timeline -- 16+ Days with Associate Editor, No Referee Report

**What goes wrong:**
Paper 5 has been at JMP for 16+ days with no referee report. JMP Editorial Policies state manuscripts are "sent to an expert referee for evaluation and, if necessary, to another reviewer for a second opinion." No numerical timeline is published. For mathematical physics journals, common timelines are:
- Desk rejection / desk accept within 2-4 weeks of associate editor receipt.
- First referee report within 2-6 months of being sent out.
- Full review cycle often 6-12 months.

16 days is within the associate-editor-consideration window. It does NOT indicate either (a) desk rejection is imminent or (b) referee reports are about to arrive. It is normal. The milestone's goal of closing gaps "before the referee report lands" is prudent but the deadline is uncertain.

**Why it happens:**
Anxiety about an imminent referee report can distort priorities. The milestone prompt's phrasing "16+ days have passed, no referee report" could be read as urgency -- but JMP does not commit to any specific timeline.

**Consequences:**
- If phases 54-59 are rushed, quality suffers (see R4, R10).
- If phases 54-59 are paced assuming months of runway, a fast referee response catches the revision half-finished.
- The right pace is "as fast as quality allows, on the assumption of 2-3 months of runway, with stopping-point discipline if a referee report lands earlier."

**Prevention:**
- Do not read "16 days" as a deadline signal. It is ambient JMP pacing.
- Phases 54-59 should each produce a standalone deliverable that could be incorporated into a revision response INDEPENDENTLY. If the referee report lands with only Phase 54 closed, the response should still be improvable by Phase 54's work alone.
- Each phase's RESULT.md should be drafted as a potential "response to Reviewer 1 point N" in the revision letter -- i.e., quotable in the response-to-referees document.

**Detection:**
Check JMP submission system (JMP26-AR-00922) weekly for status changes. Use any status update (e.g., "with referee" or "decision: revise") as a hard gate on phase 59's closing.

**Phase to address:** All, as metadata.

**References:**
- JMP Editorial Policies (pubs.aip.org/aip/jmp/pages/policies): no published review timeline commitment.
- SciRev crowdsourced JMP review times (scirev.org/journal/journal-of-mathematical-physics/): typical 3-6 months first response.
- Physical Review Letters Review Time 2026 (manusights.com/blog/physical-review-letters-review-time): for comparison, PRL averages 5 weeks; JMP is typically longer.

---

## Approximation Shortcuts

Shortcuts that seem reasonable but introduce systematic errors specific to this revision.

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
| -------- | ----------------- | -------------- | --------------- |
| Prove Peirce invariance by checking on M_2(C)^sa | Fast, concrete, obviously true | Circular; every referee will spot it | Never for outcome (A). Allowed ONLY as a sanity check ALONGSIDE a primitive-only proof. |
| Cite "AlfsenShultz2003" without page/theorem | Saves time finding reference | Referee correctly asks "where?"; citation is functionally empty | Never in the revision. v2.0 drafts: OK as placeholder; must be completed before revision submission. |
| Collapse §3.3's 20 lines to "it follows immediately" | Shorter paper | Loses content; referee flags "where's the proof?" | Never. See R4. |
| Formalize sequential-product axioms in Lean via a structure that assumes Jordan identity | Makes Lean proofs easy | Lean formalization now depends on Jordan structure, which Paper 5 is supposed to derive | Never. See R1 and R9. |
| Defer Phase 58 Lean audit to post-revision | Focuses effort on exposition | If axioms have type-(iii) mismatches, formalization is unsound; referee with Lean familiarity will find this | Acceptable only if a (non-rushed) audit pass happened in v2.0 Phase 6 and the 16 current axioms are unchanged since then. Verify this assumption before deferring. |
| Argue minimal-composite from "Bryan's intuition" | Fast | Exactly the failure mode the milestone was designed to prevent | Never. Milestone prompt explicitly forbids. |

---

## Convention Traps

Convention mismatches specific to this revision.

| Convention Issue | Common Mistake | Correct Approach |
| ---------------- | -------------- | ---------------- |
| Sequential product notation | Paper 5 uses `a ∘ b`; vdW uses `a & b`; v2.0 Phase 4 uses `a & b` | Revise Paper 5 to match vdW notation (`a & b`) for symmetric-product vs. `a * b` for Jordan product OR keep `∘` but explicitly distinguish from Jordan product `·`. Inconsistent notation between Paper 5 and vdW's cited Theorem 1 is itself a referee-attack surface. |
| Compression notation | `c_p` (A-S) vs `C_p` (vdW) vs `U_e` (Niestegge) | Pin to one; explicitly state "c_p denotes the A-S compression of Alfsen-Shultz 2001 Ch. 7" once, then use consistently. v2.0 Phase 4 uses `C_p`. |
| Projective unit vs. projection vs. sharp effect | Paper 5 may use interchangeably; A-S distinguishes | "Projective unit p": element with a specific A-S-axiomatic role. "Sharp effect": p with `p ∘ p = p` and `p ∘ p' = 0` (vdW Def. 7). These coincide for finite-dim SPS but are conceptually distinct. Audit usage. |
| Face vs. subspace vs. Peirce component | Paper 5 §3.3-3.4 uses geometric language loosely | "Face of state space": geometric (A-S Ch. 1). "Peirce component V_2(p_i)": algebraic, inside V (A-S Ch. 8 in JB setting). These are DUAL objects, not the same thing. Referee will catch conflation. |
| Two Alfsen-Shultz volumes | `\cite{AlfsenShultz2003}` for everything | (2001) vol. 179 for basic compression theory; (2003) vol. 190 for Jordan state spaces. Cite correctly per claim. |
| Finite-dimensional vs. general OUS | Implicit finite-dim in proofs, general OUS in statements | Paper 5 assumes finite-dim (vdW Theorem 1's hypothesis). Either state this hypothesis every time or state it once and mark each section's scope. |

---

## Numerical Traps

Paper 5 is primarily analytical; "numerical" pitfalls here refer to Lean-formalization traps.

| Trap | Symptoms | Prevention | When It Breaks |
| ---- | -------- | ---------- | -------------- |
| Decidable-instance blow-up in Lean for OUS | Slow elaboration, timeouts on basic tactics | Use `Classical.dec` sparingly; prefer `DecidableEq` only where genuinely needed. For abstract OUS with no decidable order, mark non-decidable explicitly. | OUS is not presented as a decidable order in mathlib; naive instances fail. |
| `axiom` vs. `opaque` in Lean 4 | axiom admits anything including `False`; opaque is safer | Prefer `opaque` for definitional constants; `axiom` only for genuine extensions to Lean's core logic. | Type-(ii) failure mode of R9. |
| `simp` normal form drift for compression algebra | `simp` reduces `c p (c p x)` to `c p x` but may also reduce other expressions unpredictably | Use explicit `@[simp]` tags sparingly; prefer targeted rewriting. | Large compression proofs become brittle under mathlib version bumps. |
| Nat vs. Fin for projector indexing | `Fin n` indices cause clumsy proofs; `Nat` indices admit invalid values | Use `Fin n` with `Fintype` for finite orthogonal projector families; lift to `Nat` only at the boundary. | Formalizing `Σ_i λ_i p_i` for a spectral decomposition. |

---

## Interpretation Mistakes

Domain-specific errors in interpreting what Phase 54-59 work actually shows.

| Mistake | Risk | Prevention |
| ------- | ---- | ---------- |
| Reading Phase 54 outcome (A) proof as justifying the full §3.3 passage | False confidence; §3.3 says more than just Peirce invariance | Phase 54 only addresses the Peirce-invariance claim at lines 508-528. Other §3.3 claims need independent audits. |
| Treating outcome (B) citation as "problem solved" | If the A-S citation is imprecise, the problem is not solved | Outcome (B) requires chapter+section+theorem+page. "Cite A-S somewhere in Ch. 8" is not (B). |
| Treating outcome (C) as catastrophic | Outcome (C) is a correct finding of a real gap; paper has an ordering problem but is not wrong | Per milestone prompt: outcome (C) pauses milestone, triggers human decision on restructuring -- NOT paper retraction. |
| Reading Lean 0-sorry as certificate of correctness | 0 sorry + type-(iii) axioms = false certificate | Lean certifies modulo its axioms. The milestone's whole point is to audit what those axioms actually assert vs. what they should assert. |
| Treating "carries" in Thm 5.8 as natural-language obvious | Proof may only establish closure (sense 1 of R7), not structural preservation (sense 3) | Distinguish closure / induced-structure / functorial in the proof and state which sense applies. |
| Treating minimal-composite objection as merely philosophical | It is technical: the choice determines which JVW algebras are excluded | Different composite axioms exclude different subsets of {M_n(R), M_n(C), M_n(H), V_n, h_3(O)}. The choice matters for Paper 5's conclusion. |
| Assuming independence from upstream v2.0 work | Paper 5 inherited v2.0 Phase 4-6 results; those phases had their own assumptions | Audit v2.0 Phase 4-6 for any "we assume" or "by standard argument" that Paper 5 now needs to prove from primitives. Prior GPD work on sequential product (v2.0) may have settled pieces, or may have ASSUMED them -- check which. |

---

## Publication Pitfalls

Common mistakes specific to Paper 5's JMP revision.

| Pitfall | Impact | Better Approach |
| ------- | ------ | --------------- |
| Silent revision of §3.3 without explaining to referee | Reviewer won't know what changed; may re-flag resolved issues | In the response-to-referees letter, explicitly address each of the six gaps: "At §3.3, we have added a full proof of Peirce invariance from OUS primitives; see revised lines 508-560." |
| Shortening the paper under revision | "Simpler = better" instinct; but the referee flagged gaps BECAUSE of insufficient detail | Expect revised Paper 5 to be LONGER than submitted version, not shorter. Phase 54's (A) proof adds 30-50 lines; Phase 55's lemma adds 20; Phase 56's Thm 5.8 revision adds 15; etc. |
| Introducing new results in revision not flagged by referee | Feature creep; risks new objections on new content | Unless a new result closes a flagged gap, defer to Paper 6. Revision should be responsive, not exploratory. |
| Not updating the arXiv / Zenodo copy | Paper 5 arXiv:[id] and Zenodo DOI 10.5281/zenodo.19342703 diverge from JMP version | Plan arXiv v2 replacement and Zenodo new version simultaneously with JMP revision submission. |
| Not freezing revision state | Continued fiddling after submission | Tag `paper5-jmp-revision-v1` at revision submission; any post-submission changes become v2. |

---

## "Looks Correct But Is Not" Checklist

Checklist for Phase 54-59 work review.

- [ ] **§3.3 revised proof:** Uses only the allowed tool list (OUS, ≤, 1, c_p A-S axioms, S1, S3, linearity, finite-dim)? No forbidden tokens (Jordan, EJA, M_n, √(λμ), vdW Thm 1)?
- [ ] **§3.4 S4 phi-independence proof:** Does not circularly use state separation derived from Jordan structure? Cites A-S separation explicitly with theorem number?
- [ ] **Thm 5.8 "carries" sense:** Which of {closure, induced-structure, functorial preservation} does the proof establish? Is this the sense the downstream use requires?
- [ ] **Phi role audit:** Every occurrence of phi classified; multiple roles either proved coincident or renamed?
- [ ] **Lean 16 axioms:** Each classified as (i) theorem-in-disguise, (ii) definition-as-axiom, (iii) statement-mismatch, or (iv) genuine primitive? Post-audit axiom count ≤ 10?
- [ ] **Minimal composite defense:** Operational motivation independent of "Bryan's intuition"? Compared to Hardy / Masanes-Müller / Chiribella / Barnum-Wilce alternatives?
- [ ] **A-S citation precision:** Every `\cite{AlfsenShultz...}` upgraded to `\cite[Ch.Sec.Thm]{AlfsenShultz...}` with correct volume (2001 vs. 2003)?
- [ ] **Cross-phase consistency:** All six phases cite the same version of the Peirce invariance result, the same phi definition, the same minimal-composite formulation?
- [ ] **Revision letter:** Each of 6 gaps explicitly addressed in response-to-referees? Quotes from RESULT.md files usable verbatim?
- [ ] **Notation consistency:** `a & b` vs `a ∘ b` vs `a * b` distinctions preserved throughout? v2.0 Phase 4 conventions compatible with revised Paper 5?

---

## Recovery Strategies

When pitfalls occur despite prevention.

| Pitfall | Recovery Cost | Recovery Steps |
| ------- | ------------- | -------------- |
| R1 (circularity in §3.3) detected late | HIGH | Phase 54 outcome (C); pause milestone; human decision on restructuring. May require moving §4 derivation of Jordan structure earlier, or adding an explicit assumption at §3.3 and re-writing §3.4-§3.5 to depend on it. |
| R2 / R3 (Peirce conflation) detected in review | MEDIUM | Add explicit case-analysis lemma to §3.3; expand proof by ~20 lines; re-verify downstream §4. |
| R5 (vague A-S citations) detected late | LOW-MEDIUM | One-time audit of main.tex; replace `\cite{AlfsenShultz2003}` with precise citations. ~2 hours of work + verification of each theorem's actual content. |
| R6 (phi-independence circularity at S4) detected late | HIGH | If §3.4's argument truly requires Jordan-structured separation, S4 proof must be rewritten with explicit A-S spectrality instead. If A-S spectrality is unavailable without Jordan, §3.4 has the same ordering problem as §3.3 and the two circularities stack. |
| R7 ("carries" equivocation) detected late | MEDIUM | Thm 5.8 statement may need to be weakened (from "W carries" to "W admits a closed operation satisfying S1-S3"), with downstream use re-audited. |
| R8 (phi overloading) detected late | LOW | Symbol-rename pass; ~1-2 hours. |
| R9 (Lean type-iii axiom) detected late | LOW-HIGH depending on dependency | If axiom is only used in one theorem, weaken axiom to match cited A-S statement and re-verify. If axiom is used throughout, may require proving the stronger form from primitives (which was the whole point of this milestone). |
| R10 (minimal composite flagged by reviewer) | MEDIUM | Expand Phase 59's response letter section; add a subsection "Relation to alternative composite axioms" citing Masanes-Müller and Chiribella et al. |
| R11 (cross-phase cascade) detected mid-milestone | MEDIUM-HIGH | Pause active phases; consolidate shared deliverables (A-S notes, phi audit); restart. |
| R12 (referee lands early) | Depends on phase progress | If only Phase 54 closed, respond only to §3.3-related reviewer points; request extension for other points. If Phase 58 incomplete, note "Lean formalization revision in progress" in cover letter. |

---

## Pitfall-to-Phase Mapping

Primary and secondary phases per pitfall.

| Pitfall | Primary Phase | Secondary Phase(s) | Verification |
| ------- | ------------- | ------------------ | ------------ |
| R1 (circularity via Jordan) | Phase 54 | 56, 58 | Forbidden-token grep on RESULT.md and main.tex revision. |
| R2 (decomposition vs. invariance) | Phase 54 | 55 | Proof explicitly distinguishes the two; cited theorems match what is being cited for. |
| R3 (single vs. composite compression) | Phase 54 | -- | Case analysis for each Peirce subspace type; mixing term treated explicitly. |
| R4 ("obvious" rate limit) | All 54-59 | -- | Word-count compare revised vs. submitted; forbidden-word grep. |
| R5 (A-S citation precision) | Phase 55 | 54, 57, 58 | Every A-S cite has chapter/section/theorem/volume; manual spot-check against Birkhäuser books. |
| R6 (facial orthogonality phi-indep.) | Phase 55 | 54 (if shared argument pattern) | Explicit dependency trace on separation-of-states. |
| R7 ("carries" equivocation) | Phase 56 | 59 | Explicit S1-S7 on W; distinction between closure/induced/functorial. |
| R8 (phi overloading) | Phase 57 | -- | Symbol audit; every occurrence classified. |
| R9 (Lean axiom audit) | Phase 58 | -- | 16 axioms classified (i-iv); post-audit count; each remaining axiom has one-line justification. |
| R10 (minimal composite) | Phase 59 | -- | Comparison table to Hardy / Masanes-Müller / CD-P / Barnum-Wilce; anticipated-objection responses prepared. |
| R11 (cross-phase cascade) | Orchestration | All | Dependency graph exists; shared deliverables defined; Phase 54 outcome gates 55-59. |
| R12 (JMP timeline) | Metadata | All | Weekly status check; each phase's RESULT.md is revision-letter-ready standalone. |

---

## Sources

### Peer-reviewed primary sources

- van de Wetering, J. (2019). "Sequential product spaces are Jordan algebras." J. Math. Phys. 60, 062201. arXiv:1803.11139. [DOI](https://pubs.aip.org/aip/jmp/article-abstract/60/6/062201/233722/).
- van de Wetering, J. (2018). "Three characterisations of the sequential product." J. Math. Phys. 59, 082202. arXiv:1803.08453. [DOI](https://pubs.aip.org/aip/jmp/article-abstract/59/8/082202/233970/).
- Gudder, S., Greechie, R. (2002). "Sequential products on effect algebras." Rep. Math. Phys. 49, 87. Contains the non-EJA SEA counterexamples directly relevant to R7.
- Gudder, S., Greechie, R. (2005). "Uniqueness and Order in Sequential Effect Algebras." Int. J. Theor. Phys. 44, 755.
- Westerbaan, A., Westerbaan, B., van de Wetering, J. (2020). "The three types of normal sequential effect algebras." Quantum 4, 378. [Quantum Journal](https://quantum-journal.org/papers/q-2020-12-24-378/).
- Barnum, H., Wilce, A. (2014). "Local Tomography and the Jordan Structure of Quantum Theory." Found. Phys. 44, 192. arXiv:1202.4513.
- Barnum, H., Graydon, M., Wilce, A. (2020). "Composites and Categories of Euclidean Jordan Algebras." Quantum 4, 359. [Quantum Journal](https://quantum-journal.org/papers/q-2020-11-08-359/).
- Alfsen, E.M., Shultz, F.W. (2001). *State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products*. Birkhäuser Progress in Math. v. 179.
- Alfsen, E.M., Shultz, F.W. (2003). *Geometry of State Spaces of Operator Algebras*. Birkhäuser Progress in Math. v. 190.
- Hardy, L. (2001). "Quantum Theory From Five Reasonable Axioms." arXiv:quant-ph/0101012.
- Masanes, L., Müller, M. (2011). "A derivation of quantum theory from physical requirements." NJP 13, 063001. arXiv:1004.1483.
- Chiribella, G., D'Ariano, G.M., Perinotti, P. (2011). "Informational derivation of quantum theory." PRA 84, 012311. arXiv:1011.6451.
- Niestegge, G. (2020). "Local tomography and the role of the complex numbers in quantum mechanics." arXiv:2001.11421.

### Methodological / tooling sources

- Avigad, J., Massot, P. (2025). *Mathematics in Lean* v4.19. [PDF](https://leanprover-community.github.io/mathematics_in_lean/mathematics_in_lean.pdf).
- Lean Theorem Proving in Lean 4, Ch. 12 "Axioms and Computation." [lean-lang.org](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/).
- Jacobs-Mandemaker (2012) and subsequent work on sequential effect algebra categorical semantics.

### Editorial / timeline sources

- JMP Editorial Policies. [pubs.aip.org/aip/jmp/pages/policies](https://pubs.aip.org/aip/jmp/pages/policies).
- SciRev crowdsourced review times for Journal of Mathematical Physics.

### Internal GPD sources (prior work to build on)

- v2.0 Phase 4 (`04-sequential-product-formalization/`), plans 01-06: established compression-based SP, corrected with Peirce-1 feedback, S3 verified, classical limit verified, Lüders-on-M_2(C) equivalence verified. Especially Plan 06 summary for the corrected formula and circularity audit pattern.
- v2.0 Phase 5 (`05-local-tomography-from-b-m-compositionality/`): established relationship between independent accessibility and local tomography; foundation for Phase 59 minimal-composite defense.
- Paper 5 source: `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main.tex` at tag `paper5-jmp-submitted`. §3.3 lines 508-528, §3.4 lines (TBD in Phase 55 survey).
- Paper 5 Lean formalization: `~/repos/research/lean/Paper5/` with 16 axioms, 0 sorry as of 2026-03-28 submission.
- Milestone prompt: `/Users/ehrlich/scratch/get-physics-done/paper5-revision-prompt.md`.

---

_Known pitfalls research for: Paper 5 JMP revision (v14.0)_
_Researched: 2026-04-16_
_Supersedes v13.0 PITFALLS.md for purposes of the Paper 5 revision milestone; v12.0 P1-P9 and v13.0 C1-C12 remain valid for Paper 6 work and will be consulted if Paper 5 revisions touch the Paper 6 chain._
