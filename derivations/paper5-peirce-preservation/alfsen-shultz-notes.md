# Alfsen-Shultz Citation Resolution — Paper 5 §3.3-§3.4 Baseline (Phase 54-01) [SHARED ARTIFACT]

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: as_2001=Alfsen-Shultz 2001 vol. 179 "State Spaces of Operator Algebras: Basic Theory, Orientations, and C*-products" (Birkhäuser PM 179); as_2003=Alfsen-Shultz 2003 vol. 190 "Geometry of State Spaces of Operator Algebras" (Birkhäuser PM 190); NEVER collapse the two volumes into "Alfsen-Shultz"; any AMBIGUOUS volume requires a dated research TODO
% CORRECTION 2026-04-16 (post-baseline; user-supplied A-S 2003 TOC research): compression theory lives in **A-S 2003** Ch. 2 (Abstract characterization, p. 75), Ch. 7 (General Compressions, p. 211), Ch. 8 (Spectral Theory, p. 251) — NOT in A-S 2001. A-S 2001 is the C*-algebra-flavored volume. The PRE-JORDAN-LEGAL boundary is a CHAPTER boundary within A-S 2003 (Ch. 1-8 pre-Jordan-legal; Ch. 9 Jordan-state-space-characterization is post-Jordan-illegal). Baseline rows below attributing compression axioms to "A-S 2001 Ch. 7-8" are CORRECTED inline to "A-S 2003 Ch. 2/7/8" in-place (see change-log at end of file).

**SHARED ARTIFACT — produced in Phase 54-01; extended by Phases 55 (§3.3-§3.4 S4 argument), 57 (phi-audit), 58 (Lean axiom audit). Please do not edit existing rows without a dated change-log entry at the bottom of this file.**

**Schema:** Every row follows: `(Paper 5 line number | citation key as it appears in .bib | resolved-volume | chapter | section | prop/thm number | exact-book-statement (quoted, not paraphrased) | match-to-Paper-5 verdict)`.

**Convention:** "Verified against book text" means the executor had access to the A-S book(s) and transcribed the Prop/Thm statement verbatim. "QUOTE-PENDING" means the book text was not accessible to the executor at the time of row creation and the statement is deferred. "VERIFICATION-DEFERRED" means the Prop/Thm number itself is not yet confirmed. In no case is an A-S statement paraphrased (Paper 5 R5 pitfall, ADDENDUM finding).

---

## Section 1: Paper 5 §3.3-§3.4 A-S Citation Inventory

Paper 5 is located at `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` (frozen at git tag `paper5-jmp-submitted`).

**Grep command** (run 2026-04-16 during Phase 54-01 Task 4):

```
$ awk 'NR>=483 && NR<=713 && /AlfsenShultz/' \
    ~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex
```

**§3.3-§3.4 scope boundaries in main-jmp-submitted.tex:**

- §3.3 "The Corrected Product via Peirce Feedback" — starts line 483, ends line 563
- §3.4 "Determining the Mixing Function" — starts line 565, ends line 712
- §3.5 "Circularity Check" — starts line 714 (out of scope for this baseline, covered by Phase 55 when it extends the notes)

**Grep result** (all `\cite{AlfsenShultz...}` in lines 483-713):

| Paper 5 Line | Citation Key | Context (snippet) |
|--------------|--------------|-------------------|
| **513** | `AlfsenShultz2003` | `(Alfsen--Shultz~\cite{AlfsenShultz2003}), so linearity gives a block decomposition: \seqp{a}{\cdot} maps each Peirce subspace to itself.` |

**Count:** 1 citation in the strict §3.3-§3.4 scope (lines 483-713). This is the load-bearing citation for the R2 non-sequitur that Phase 54 is replacing.

Additional A-S mentions by NAME (not `\cite`) in §3.3-§3.4 scope (for reference; not independent citations requiring resolution but noted for completeness):

| Paper 5 Line | Context | Notes |
|--------------|---------|-------|
| 423 (prior to §3.3, just for reference) | `where $\comp{p}$ is the Alfsen--Shultz compression for the face` | outside §3.3 scope; covered by Section 5 below |
| 730 (inside §3.5, outside baseline scope) | `\item Alfsen--Shultz compressions $\comp{p}$ for faces of` | covered by Phase 55 extension |

The §3.3 citation at line 513 is THE citation that Phase 54 replaces. Rows for A-S-outside-the-explicit-\cite-scope (e.g., line 423 `Alfsen--Shultz compression for the face` which is in §3.2) are handled in the A-S 2003 Ch. 2/7/8 compression axioms sub-table (Section 5) rather than as independent citation rows.

---

## Section 2: Paper 5 Citations Outside §3.3-§3.4 That Are Relevant (Information Only)

For context and to track consistency across the paper (downstream phases may pull these in):

| Paper 5 Line | Citation Key | Resolved Vol. | Context |
|--------------|--------------|---------------|---------|
| 182 | `AlfsenShultz2003` | 2003 vol. 190 | `Alfsen--Shultz~\cite{AlfsenShultz2003}.` in §2 Preliminaries — §2.1 Order Unit Spaces — preliminary reference |
| 205 | `AlfsenShultz2003` | 2003 vol. 190 | `structure~\cite{AlfsenShultz2003}, prior to and independent of any` in §2.1 — OUS framework reference |

These are pre-§3.3 references; they are tagged for reference only. Phase 54-01 baseline does not resolve them row-by-row (§3.3-§3.4 scope). Phase 57 (phi-audit) or Phase 55 (S4 phi-independence) may want to revisit these.

---

## Section 3: Citation Resolution Table (§3.3-§3.4 baseline)

### Row 1 — Paper 5 Line 513 (the load-bearing non-sequitur citation)

| Field | Value |
|-------|-------|
| Paper 5 line number | 513 |
| Citation key (as in .bib) | `AlfsenShultz2003` |
| Resolved volume | **2003 vol. 190** (explicit `2003` in the cite key) |
| Chapter | UNCERTAIN (not specified in Paper 5); candidates based on ADDENDUM reading of A-S 2003 TOC: **Ch. 1-3** (Part I Peirce-Jordan development), **Ch. 7-8** (general compressions / spectral theory), or **Ch. 9** (Jordan state-space characterization) |
| Section | UNCERTAIN (no specific section or theorem cited in Paper 5 at this line) |
| Prop/Thm number | UNCERTAIN (no specific Prop/Thm cited at line 513; the cite is bare `\cite{AlfsenShultz2003}`) |
| Exact-book-statement | QUOTE-PENDING — Paper 5 cites the 2003 book generically for "compressions project onto these subspaces"; the underlying claim is pre-Jordan in A-S 2001 Ch. 7-8 but post-Jordan in A-S 2003 Ch. 9 (Thm 9.37) per ADDENDUM. The specific Prop/Thm number must be determined by downstream extension of this row before any Paper 5 revision can safely cite it. |
| Match-to-Paper-5 verdict | **DOES-NOT-IMPLY** (as cited; and PRE-JORDAN-ILLEGAL **if Paper 5 intended A-S 2003 Thm 9.37**) |

**Elaboration on verdict:**

Paper 5 line 513 cites `\cite{AlfsenShultz2003}` in support of: "Compressions project onto these subspaces (Alfsen-Shultz 2003), so linearity gives a block decomposition: `\seqp{a}{\cdot}` maps each Peirce subspace to itself." This is TWO claims:

1. **"Compressions project onto these subspaces"** — pre-Jordan-legal. Compressions onto faces (A-S 2003 Ch. 2 "Abstract characterization," Ch. 7 "General Compressions," Ch. 8 "Spectral Theory"). Paper 5 cites the correct VOLUME (2003), but the citation is chapter-level-bare — it should point explicitly to Ch. 2 / Ch. 7 / Ch. 8 to avoid ambiguity with Ch. 9 (Jordan characterization, post-Jordan, illegal here). _Earlier baseline text here said "correct vol. is 2001" — that was a misattribution; see change-log 2026-04-16._

2. **"Linearity gives a block decomposition that `\seqp{a}{\cdot}` maps each Peirce subspace to itself"** — this is the R2 non-sequitur. NO A-S theorem (either volume) implies that a GENERAL linear map `L_a` respects the Peirce decomposition; the only A-S-level facts are (a) individual compressions preserve their own range (Peirce 2-space), not that a COMPOSITE map respects the full decomposition. This is the core Phase 54 claim to prove or axiomatize.

Therefore the line-513 citation is:

- **Either insufficient (it doesn't license the full claim)** → DOES-NOT-IMPLY
- **Or under-specified (correct volume, missing chapter; compression axioms live at A-S 2003 Ch. 2 "Abstract characterization" / Ch. 7 / Ch. 8)** → DOES-NOT-IMPLY as it stands; revision must pin the chapter to avoid Ch. 9 ambiguity
- **Or implicitly invoking A-S 2003 Thm 9.37** (the Peirce direct sum theorem in the Jordan-characterization chapter) → PRE-JORDAN-ILLEGAL per ADDENDUM

**Action for downstream phases:** This row MUST be resolved (disambiguate which of the sub-cases applies) before Paper 5 §3.3 can be rewritten with a correct A-S citation. Plan 54-03 replaces this citation entirely: (A) is closed (both routes fail); (C-i) invokes the S0 axiom and drops the post-Jordan appeal, while citing A-S 2003 Ch. 2/7/8 for the compression axioms S0 defers to.

---

## Section 4: Mandatory Explicit Flags

### Flag 4.1 — A-S 2003 Thm 9.37: **PRE-JORDAN-ILLEGAL**

| Field | Value |
|-------|-------|
| Citation target | A-S 2003 (vol. 190) Theorem 9.37 |
| Verdict | **PRE-JORDAN-ILLEGAL** |
| Chapter | Ch. 9 — "Characterization of Jordan Algebra State Spaces" (per ADDENDUM finding, A-S 2003 TOC) |
| Reason | A-S 2003 vol. 190 Ch. 9 is the Jordan-state-space-characterization chapter per ADDENDUM (`.gpd/research/ADDENDUM-independent-literature-check.md` §Finding 1). Any invocation of Thm 9.37 at the pre-Jordan §3.3 level is circular: the theorem lives in the chapter whose very purpose is to characterize Jordan state spaces, and §3.3 has not yet invoked Jordan structure. |
| Exact-book-statement | QUOTE-PENDING — book text not on hand to executor at time of baseline creation (2026-04-16). Per ADDENDUM Finding 1: "Paper 5 cites 'Theorem 9.37' for the Peirce direct sum. Chapter 9 is a Jordan-state-space characterization chapter." Transcription of the exact book statement is an action item for Phase 55 (or whenever the A-S 2003 book is accessed physically / digitally). Do NOT paraphrase. |
| Replacement | Any Paper 5 §3.3 invocation of Thm 9.37 MUST be replaced by either (a) A-S 2003 vol. 190 Ch. 2 / Ch. 7 / Ch. 8 compression citation (if the invoked property is compression-theoretic and the claim is correctly scoped) OR (b) the Phase 54 (C-i) S0 axiom (if the invoked property is Peirce-invariance of the left-multiplication `L_a`). |
| Action item | Phase 55 (when accessing A-S 2003 physically/digitally): transcribe the exact Thm 9.37 statement, update this row, add it to the Phase 55 alfsen-shultz-notes extension. |

### Flag 4.2 — A-S 2003 Prop 7.36: **PROP-NUMBER-UNVERIFIED**

| Field | Value |
|-------|-------|
| Citation target | A-S 2003 (vol. 190) Proposition 7.36 |
| Consumer | Lean file `~/repos/research/lean/RadicalRelativity/SelfModelingBridge.lean` — 2 citations (line 51 and line 765-766) |
| Exact Lean citation context | Line 51: `"- S4 (orthogonality symmetry): facial orthogonality (Alfsen-Shultz Prop 7.36)"`. Line 765-766: `"/-- S4 sub-axiom 2: If b lives in the orthogonal face of a's support, then sp(b,a) = 0. (Alfsen-Shultz 2003, Prop 7.36.) -/ axiom orthogonal_face_sp_zero"`. |
| Verdict | **PROP-NUMBER-UNVERIFIED** |
| Chapter | Ch. 7 per the Lean citation ("7.36"). Ch. 7 in A-S 2003 is "General Compressions" (per ADDENDUM TOC reading) — pre-Jordan-legal if the prop is indeed in Ch. 7 of the 2003 volume. |
| Section | UNCERTAIN |
| Exact-book-statement | QUOTE-PENDING — book text not on hand; Lean file paraphrases as "If b lives in the orthogonal face of a's support, then sp(b, a) = 0." This paraphrase MUST NOT be propagated into Paper 5 or this row as verified — the executor must transcribe the exact A-S 2003 Prop 7.36 statement verbatim when the book is accessed. Note: the Lean claim ("sp(b,a) = 0") is about the sequential product, but A-S 2003 Prop 7.36 (if the number is correct) is about compression/face theory, NOT sequential products. There may be a **Lean statement-mismatch** at this citation (a type-(iii) axiom per Phase 58 taxonomy). |
| Dated research TODO (2026-04-16) | **TODO:** Verify Prop 7.36 number against A-S 2003 vol. 190 book text. Do NOT paraphrase. Update this entry when verified (or downgrade verdict to NEEDS-VERIFICATION → VERIFIED/INCORRECT). Consumed by Phase 58 Lean axiom audit. If the Lean citation is verified but the content mismatches (`sp(b, a) = 0` vs. an A-S compression/face statement), flag as **type-(iii) statement-mismatch** per Phase 58 axiom-class taxonomy. |

### Additional note (post-baseline observation): the Lean file also cites A-S 2003 for several other props/thms in the same file — Prop 7.44, Prop 7.48, Prop 7.50, Thm 7.55, Thm 9.33, Thm 9.37, Ch. 6, Ch. 7, Ch. 9. These are **out of Phase 54-01 scope** (they are S4, sequential-product, and compression-system claims, not Peirce-preservation claims) but are flagged here so Phase 58 can extend this row/table with them. Phase 58 should add rows for each; the `alfsen-shultz-notes.md` footer's change-log tracks those extensions.

---

## Section 5: A-S 2003 Ch. 2/7/8 Compression Axioms Sub-Table

The four A-S compression axioms actually used in Phase 54. **Correct source** (per user-supplied A-S 2003 TOC research, 2026-04-16, consistent with ADDENDUM Finding 1): **A-S 2003 vol. 190**, specifically:

- **Ch. 2 §"Abstract characterization of compressions"** (p. 75) — the axiomatic framing of compressions
- **Ch. 7 "General Compressions"** (p. 211) — P-projections, projective units, projective faces
- **Ch. 8 "Spectral Theory"** (p. 251) — lattice of compressions, spaces in spectral duality

The PRE-JORDAN-LEGAL boundary is a **chapter** boundary within A-S 2003: Ch. 1-8 are pre-Jordan (including the compression framework and the abstract characterization); Ch. 9 "Characterization of Jordan Algebra State Spaces" is post-Jordan, and Thm 9.37 is illegal to invoke at Paper 5 §3.3. A-S 2001 vol. 179 is a DIFFERENT volume ("Basic Theory, Orientations, and C*-products") and is **not** the source for compression axioms.

**Important scope note:** The executor at Phase 54-01 time (2026-04-16) does NOT have A-S 2003 vol. 190 physical or digital book access. All entries below are marked VERIFICATION-DEFERRED for the Prop/Thm number and QUOTE-PENDING for the exact book statement. **These must be resolved before Phase 54 closes** — see Section 5A below for the secondary-source verification path (Niestegge 2010, Hanche-Olsen/Størmer 1984) that may skip the need for direct A-S 2003 access.

### Section 5A: Secondary-Source Verification Path (added 2026-04-16)

Before escalating to physical A-S 2003 access, Plan 54-03 (or a Phase 55 sub-task) SHOULD attempt verification via secondary sources already in Paper 5's citation universe:

1. **Niestegge (2010)** "Conditional probability, three-slit experiments, and the Jordan algebra structure of quantum mechanics," arXiv:1001.3633 — already cited by Paper 5. Uses A-S compression framework. If it states compression axioms explicitly with A-S Prop/Thm inline references, that pins the verification without needing A-S 2003 on disk.
   - Recommended grep: `rg -n "compression|Alfsen|Shultz|projective unit|P-projection" <niestegge.pdf converted to text>`
2. **Hanche-Olsen & Størmer (1984)** "Jordan Operator Algebras," Pitman — standard graduate reference; covers compressions; often easier to access than A-S 2003; cross-references A-S.
3. **Jenčová-Pulmannová (2021)** — already read in ADDENDUM Finding 2; uses compression bases on OUS/JB-algebras; may cite A-S Prop/Thm numbers.

If these secondary sources state the four axioms verbatim with explicit A-S 2003 Prop/Thm references, VERIFICATION-DEFERRED rows can be closed without direct book access. If they do not, the final fallback is physical A-S 2003 access (local university library walk-in or paperback purchase ~$50; ISBN 978-1461265757).

### Axiom 5.1 — Idempotency: `C_p² = C_p`

| Field | Value |
|-------|-------|
| Compression axiom name | Idempotency |
| Formal statement | For any compression `C_p` (A-S 2003 P-projection onto face(p)), `C_p ∘ C_p = C_p`. |
| Source volume | **A-S 2003 vol. 190** (CORRECTED 2026-04-16; compression material lives in the 2003 volume, Ch. 2/7/8 — NOT in 2001; see change-log) |
| Chapter | Ch. 7 "General Compressions" (per internal cross-reference; idempotency stated jointly with positivity at Prop 7.23) |
| Section | UNCERTAIN (within Ch. 7) |
| Exact Prop/Thm number | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → **A-S 2003 Prop 7.23**. Upgraded from VERIFICATION-DEFERRED on 2026-04-16 per Plan 54-03 NEW SCOPE item 2 (see `secondary-source-verification.md`): `derivations/04-axiom-S4.md` line 63 cites A-S Prop 7.23 for "A3 (Idempotence): `C_p(C_p(b)) = C_p(b)`", produced under the convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY`. Phase 55 or later should perform direct A-S 2003 book verification to upgrade to VERIFIED-AGAINST-BOOK-TEXT. |
| Exact-book-statement | QUOTE-PENDING — direct book transcription pending A-S 2003 access (TODO for Phase 55). Prop-number 7.23 cross-referenced from internal project derivations. |
| Phase 54 usage | Foundational in every (A) attempt and the (C-i) derivation of Propositions 3.1, 3.2, 3.3 in claim.md; used in `s0-axiom.md` Sections 5.0, 5.a, 5.b. |

### Axiom 5.2 — Positivity: `C_p ≥ 0`

| Field | Value |
|-------|-------|
| Compression axiom name | Positivity |
| Formal statement | For any compression `C_p`, `C_p` preserves the positive cone: `b ≥ 0 ⇒ C_p(b) ≥ 0`. |
| Source volume | **A-S 2003 vol. 190** (CORRECTED 2026-04-16; compression material lives in the 2003 volume, Ch. 2/7/8 — NOT in 2001; see change-log) |
| Chapter | Ch. 7 "General Compressions" (per internal cross-reference; positivity stated jointly with idempotency at Prop 7.23) |
| Section | UNCERTAIN (within Ch. 7) |
| Exact Prop/Thm number | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → **A-S 2003 Prop 7.23**. Upgraded from VERIFICATION-DEFERRED on 2026-04-16 per Plan 54-03 NEW SCOPE item 2 (see `secondary-source-verification.md`): `derivations/04-axiom-S4.md` line 61 cites A-S Prop 7.23 for "A1 (Positivity): `C_p` is a positive map: `b >= 0 => C_p(b) >= 0`". Niestegge 2008 (arXiv:1001.3633) §3 also uses a "positive projection" `U_e` as the compression analog. Phase 55 or later should perform direct A-S 2003 book verification. |
| Exact-book-statement | QUOTE-PENDING — direct book transcription pending A-S 2003 access. |
| Phase 54 usage | Used in positivity-bound arguments in Plan 54-02 (A) attempt and claim.md Section 4.3. |

### Axiom 5.3 — Complement on sharp effects: `C_p + C_{p'} = pinching` (NOT = id in non-commutative OUS)

| Field | Value |
|-------|-------|
| Compression axiom name | Complement on sharp effects |
| Formal statement | For a sharp effect `p` and its complement `p' := 1 − p`, `C_p + C_{p'}` equals the **pinching map** `Pinch(b) = C_p(b) + C_{p'}(b)` — which is NOT the identity in non-commutative OUS; the map `Pinch` annihilates the Peirce 1-space `V_1(p, p')`. |
| Source volume | **A-S 2003 vol. 190** (CORRECTED 2026-04-16; compression material lives in the 2003 volume, Ch. 2/7/8 — NOT in 2001; see change-log) + correction from `derivations/04-peirce-feedback-extension.md` Step 1 (v2.0 Phase 4-06 C4 correction) |
| Chapter | Ch. 7 "General Compressions" or Ch. 8 "Spectral Theory" (complementary projections) |
| Section | UNCERTAIN |
| Exact Prop/Thm number | **AXIOM-STATED-IN-SECONDARY-SOURCE** (partial upgrade from VERIFICATION-DEFERRED on 2026-04-16 per Plan 54-03 NEW SCOPE item 2; see `secondary-source-verification.md`). The PINCHING form is confirmed via `derivations/04-peirce-feedback-extension.md` Step 1 (v2.0 Phase 4-06 C4 correction) and the WEAK form `C_p(p^⊥) = 0` is cross-referenced in `derivations/04-axiom-S4.md` line 64. However, the specific A-S 2003 Prop/Thm number for the pinching identity itself is still unresolved — VERIFICATION-DEFERRED for direct A-S 2003 access. |
| Exact-book-statement | QUOTE-PENDING — 2026-04-16 TODO (Phase 55 or later). |
| Important caveat | This was INCORRECTLY stated as `C_p + C_{p'} = id` in v2.0 Phase 4 Plan 01 C4; the correct form (`= pinching`, not `= id`) is documented in `derivations/04-peirce-feedback-extension.md` Step 1. Every Phase 54 attempt must use the CORRECTED form. |
| Phase 54 usage | Central to Peirce-1-space analysis in Propositions 3.2 and 3.3 of claim.md. |

### Axiom 5.4 — Projector fix: `C_p(p) = p`

| Field | Value |
|-------|-------|
| Compression axiom name | Projector fix |
| Formal statement | `C_p(p) = p` — the compression onto face(p) fixes p itself. |
| Source volume | **A-S 2003 vol. 190** (CORRECTED 2026-04-16; compression material lives in the 2003 volume, Ch. 2/7/8 — NOT in 2001; see change-log) |
| Chapter | Ch. 7 "General Compressions" (per internal cross-reference; Def 7.1 states `C_p(1) = p`, and projector-fix `C_p(p) = p` follows from idempotency on face(p)) |
| Section | UNCERTAIN |
| Exact Prop/Thm number | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → **A-S 2003 Def 7.1** (for `C_p(1) = p`) + Prop 7.23 (for idempotency yielding `C_p(p) = C_p(C_p(1)) = C_p(1) = p`). Upgraded from VERIFICATION-DEFERRED on 2026-04-16 per Plan 54-03 NEW SCOPE item 2 (see `secondary-source-verification.md`): `derivations/04-axiom-S4.md` line 62 cites A-S Def 7.1 for "A2 (Unit image): `C_p(1) = p`". Niestegge 2008 §3 also has `U_e(e) = e` as a direct consequence of the `U_e` framework. Phase 55 or later should perform direct A-S 2003 book verification. |
| Exact-book-statement | QUOTE-PENDING — direct book transcription pending A-S 2003 access. |
| Phase 54 usage | Used in Proposition 3.1 (V_2-invariance) argument and in relating compression action on sharp vs non-sharp effects. |

---

## Section 6: Orthogonal-Projective-Unit Compressional Annihilation

The fact `C_{p_i} C_{p_j} = 0` for orthogonal projective units `i ≠ j` is a CENTRAL Phase 54 tool (used in claim.md Section 4.3 and in every (A)/ (C-i) proof of the three target inclusions). Its status:

| Field | Value |
|-------|-------|
| Statement | `C_{p_i} C_{p_j} = 0` for `i ≠ j` in an orthogonal family `{p_k}` of projective units in a spectral OUS |
| Source volume (candidate) | **A-S 2003 vol. 190** Ch. 7 "General Compressions" (Prop 7.50 on compression composition for compatible projective units, specialized to orthogonal pairs where the meet is trivial) |
| Chapter / Section / Prop-or-Thm | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → **A-S 2003 Prop 7.50** via `derivations/04-axioms-S1-S3-S5-S7.md` line 165 ("We need C_p ∘ C_q = C_{p ∧ q}. This is a standard result in compression theory (Alfsen-Shultz Prop. 7.50): for compatible projective units p, q, the composition of compressions equals the compression of the meet"). Specialized to orthogonal projective units `p_i, p_j` (face-disjoint), the meet is trivial: `p_i ∧ p_j = 0`, hence `C_{p_i} ∘ C_{p_j} = C_{p_i ∧ p_j} = C_0 = 0`. Upgraded from NEEDS-VERIFICATION on 2026-04-16 per Plan 54-03 NEW SCOPE item 2 (see `secondary-source-verification.md`). |
| Exact-book-statement | QUOTE-PENDING — direct book transcription of A-S Prop 7.50 pending A-S 2003 access (Phase 55 or later). Prop-number 7.50 cross-referenced from internal project derivations. |
| Match-to-Paper-5 verdict | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** (upgraded from NEEDS-VERIFICATION 2026-04-16) |
| Status update (2026-04-17, post-attempt-01) | Plan 54-02 attempt-01 proved that ALL THREE target propositions in claim.md converge on the same missing bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0`. This bridge is provably NOT derivable from {S1, S3, linearity, A-S compressions} without S2, associativity, or the invariance claim itself. So even if `C_{p_i} C_{p_j} = 0` is A-S-legal, the (A) route fails at a DIFFERENT step. (A) is now foreclosed regardless of this row's resolution. Phase 54 outcome: PIVOT-TO-C-I. |
| Status update (2026-04-16, Plan 54-03 NEW SCOPE item 2 post-processing) | `C_{p_i} C_{p_j} = 0` for orthogonal `p_i, p_j` is now VERIFIED-VIA-INTERNAL-CROSS-REFERENCE → A-S 2003 Prop 7.50. This resolves the row status but does NOT re-open (A): the attempt-01 missing bridge is about `C_{p_k}(a)` with `a = Σ λ_j p_j` and `b ∈ V_1(p_k, p_l)` — the derivation still needs the V_1 off-diagonal Lemma (requiring S0 / compression-additivity on orthogonal pairs), which is a DIFFERENT step from the orthogonal compressional annihilation resolved here. See `s0-axiom.md` Section 5.0 for the V_1 off-diagonal Lemma derivation; see `secondary-source-verification.md` Section 4.1 for the independence-stance resolution ("S0 is a theorem of A-S via Prop 7.50 applied to orthogonal projective units"). |
| Contingency | Under (C-i), this fact is either (a) cited directly from A-S 2003 Prop 7.50 (as now upgraded; the §3.3 revision can cite A-S Prop 7.50 explicitly), or (b) absorbed into the S0 axiom statement per claim.md Section 4.6 (the current `s0-axiom.md` draft chooses this route for interface stability with the Phase 58 Lean axiom audit). |
| Phase 54 coupling | Upgraded from NEEDS-VERIFICATION to VERIFIED-VIA-INTERNAL-CROSS-REFERENCE; under (C-i), the S0 axiom as drafted in `s0-axiom.md` Section 2 is now backed by the A-S Prop 7.50 cross-reference, making the (C-i) route DOUBLY defended (OUS-level S0 axiom + A-S compression-theoretic theorem backing). See `secondary-source-verification.md` Section 4.2 for the revision-text framing. |

---

## Section 7: Change Log

```
## Change Log
- 2026-04-16 (Phase 54-01, Task 4): Initial §3.3-§3.4 baseline created.
  - 1 \cite{AlfsenShultz...} row resolved (line 513, 2003 vol. 190, verdict DOES-NOT-IMPLY / PRE-JORDAN-ILLEGAL variants).
  - Thm 9.37 flagged PRE-JORDAN-ILLEGAL (Flag 4.1; QUOTE-PENDING; transcription TODO).
  - Prop 7.36 flagged PROP-NUMBER-UNVERIFIED (Flag 4.2; QUOTE-PENDING; transcription TODO; potential type-(iii) statement-mismatch for Phase 58).
  - A-S 2001 Ch. 7-8 compression axioms sub-table: 4 axioms recorded with VERIFICATION-DEFERRED / QUOTE-PENDING markers. (Volume attribution corrected on 2026-04-16 — see entry below.)
  - Section 6: orthogonal-projective-unit compressional annihilation flagged NEEDS-VERIFICATION (hinge between (A) and (C-i)).
  - No A-S statements paraphrased; all un-quoted entries are explicitly QUOTE-PENDING / VERIFICATION-DEFERRED per fp-as-notes-paraphrase.
  - No collapsed "Alfsen-Shultz" citations; AlfsenShultz2003 at line 513 resolved explicitly to 2003 vol. 190.
- 2026-04-16 (post-baseline correction; user-supplied A-S 2003 TOC research):
  - Volume attribution for compression axioms CORRECTED: A-S 2001 vol. 179 → A-S 2003 vol. 190. Compression theory lives in the 2003 volume (Ch. 2 "Abstract characterization of compressions" p. 75; Ch. 7 "General Compressions" p. 211; Ch. 8 "Spectral Theory" p. 251), consistent with ADDENDUM Finding 1 TOC reading and user-supplied research. A-S 2001 ("Basic Theory, Orientations, and C*-products") is a distinct volume that does not carry the compression axioms used here.
  - PRE-JORDAN-LEGAL boundary re-framed as CHAPTER-level within A-S 2003: Ch. 1-8 pre-Jordan-legal; Ch. 9 (Jordan state-space characterization) post-Jordan-illegal. Thm 9.37 PRE-JORDAN-ILLEGAL flag unchanged.
  - Section 5 heading and all 4 axiom-row Source-volume/Chapter fields updated in place; Section 6 orthogonal-annihilation row updated; line 83/90/93/108 narrative corrections applied.
  - Section 5A added: secondary-source verification path (Niestegge 2010 arXiv:1001.3633; Hanche-Olsen & Størmer 1984; Jenčová-Pulmannová 2021) — Plan 54-03 sub-task to close VERIFICATION-DEFERRED rows without direct A-S 2003 access.
- 2026-04-17 (Plan 54-02 attempt-01 post-processing):
  - Section 6 status update: attempt-01 proved all three target propositions converge on the missing bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0`, which is NOT derivable from the (A) tool-set. (A) now foreclosed regardless of whether `C_{p_i} C_{p_j} = 0` resolves. Phase 54 outcome: PIVOT-TO-C-I; load-bearing bridge migrates to S0 axiom in Plan 54-03.
- 2026-04-16 (Plan 54-03 NEW SCOPE item 2 secondary-source verification):
  - Axiom 5.1 (Idempotency): VERIFICATION-DEFERRED → VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (A-S 2003 Prop 7.23 via `derivations/04-axiom-S4.md` line 63).
  - Axiom 5.2 (Positivity): VERIFICATION-DEFERRED → VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (A-S 2003 Prop 7.23 via `derivations/04-axiom-S4.md` line 61; also Niestegge 2008 §3).
  - Axiom 5.3 (Complement on sharp effects / pinching): VERIFICATION-DEFERRED → AXIOM-STATED-IN-SECONDARY-SOURCE (pinching form confirmed via v2.0 Phase 4-06 C4 correction `derivations/04-peirce-feedback-extension.md`; weak form `C_p(p^⊥) = 0` via `derivations/04-axiom-S4.md` line 64). Specific A-S 2003 Prop/Thm remains VERIFICATION-DEFERRED (most subtle of the four; requires direct book access for full resolution).
  - Axiom 5.4 (Projector fix): VERIFICATION-DEFERRED → VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (A-S 2003 Def 7.1 via `derivations/04-axiom-S4.md` line 62; also Niestegge 2008 §3 via `U_e(e) = e`).
  - Section 6 (Orthogonal-projective-unit compressional annihilation): NEEDS-VERIFICATION → VERIFIED-VIA-INTERNAL-CROSS-REFERENCE (A-S 2003 Prop 7.50 specialized to orthogonal-pair meet `p ∧ q = 0`, via `derivations/04-axioms-S1-S3-S5-S7.md` line 165).
  - Independence-stance for S0 resolved: **S0 is a THEOREM of A-S compression theory** (via A-S Prop 7.50 + face-disjointness of orthogonal projective units); the §3.3 revision cites S0 as an axiom for interface stability with Phase 58 Lean axiom audit, backed by A-S Prop 7.50 as secondary verification. See `derivations/paper5-peirce-preservation/secondary-source-verification.md`.
  - No A-S statements paraphrased in the upgrades; all Prop/Thm numbers sourced from internal GPD v2.0 derivations under convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY`. Exact-book-statement QUOTE-PENDING for all rows; direct A-S 2003 book verification deferred to Phase 55 or later.
- <future phases append here as rows are extended or resolved>
```

---

## Section 8: Phase 55-01 Extension — §S4 Region Citation Audit (2026-04-16)

**Phase:** 55 (S4 Facial Structure Lemma)
**Plan:** 01 (Audit-only classification; see `.gpd/phases/55-s4-facial-structure-lemma/55-01-CLASSIFICATION.md`)
**Scope:** Paper 5 `sections/axiom-verification.tex` §S4 (lines 95-168) + contiguous Thm 9.37 at line 68 (S2 scope), and `sections/appendix-proofs.tex` §S4-proof (lines 9-138). Append-only: no Phase 54 row modified.

### Row 55-01-A1 — axiom-verification.tex:39 (S1 proof bare Ch. 7 cite)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/axiom-verification.tex:39` |
| Verbatim quote | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~7), and the Peirce` |
| Citation target | A-S 2003 vol. 190, Ch. 7 (bare chapter) |
| Classification | **(i) A-S-compression-only / pre-Jordan-legal** |
| Citation proposal | **TIGHTEN-CITE** → `\cite[Ch.~7, Prop.~7.23, Def.~7.1]{AlfsenShultz2003}` (Prop 7.23 covers positivity/idempotency; Def 7.1 covers unit-image) |
| Scope | S1 (Additivity) proof; outside §S4 strict scope. LOW priority for Plan 55-02. |
| Rationale | Compressions as positive linear maps is Ch. 7 content; bare Ch. 7 cite is pre-Jordan-legal but under-specified (R5 minor). Phase 54 already verified Prop 7.23 + Def 7.1 via internal cross-reference. |
| Status | OPEN for Plan 55-02 (optional tightening) |

### Row 55-01-A2 — axiom-verification.tex:68 (S2 proof Thm 9.37 — PRE-S4 SCOPE)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/axiom-verification.tex:68` |
| Verbatim quote | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Ch.~9, Thm.~9.37).` |
| Citation target | A-S 2003 vol. 190, Ch. 9, Thm 9.37 |
| Classification | **(iii) Implicit Jordan appeal / PRE-JORDAN-ILLEGAL** |
| Citation proposal | **REPLACE** → cite A-S 2003 Ch. 8 "Spectral Theory" (p. 251) for continuous spectral functional calculus, OR cite textbook (Bhatia *Matrix Analysis* §VI or Conway *Functional Analysis* §X.2). Drop Thm 9.37 invocation entirely. |
| Scope | **PRE-S4** — inside S2 (Continuity) proof (lines 47-70 of axiom-verification.tex). 55-01-CLASSIFICATION.md Section 4 records the pre-S4 verdict with 3+ sentences of evidence. **INCLUDE in Plan 55-02 edit scope.** |
| Rationale | Thm 9.37 is in A-S 2003 Ch. 9 (Jordan state-space characterization), flagged PRE-JORDAN-ILLEGAL per Flag 4.1. S2 is proved before S4, so invoking Jordan structure at this line is R6 circularity. The actual content (spectral functional calculus continuity in finite dim) is classical and has pre-Jordan substitutes. |
| Status | OPEN for Plan 55-02 (MANDATORY replacement) |

### Row 55-01-A3 — axiom-verification.tex:125 (S4 Case A Thm 9.37 — PRIMARY BUG)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/axiom-verification.tex:125` |
| Verbatim quote | `(Alfsen--Shultz~\cite{AlfsenShultz2003}, Theorem~9.37)` (context: Peirce direct sum `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i,p_j)`) |
| Citation target | A-S 2003 vol. 190, Ch. 9, Thm 9.37 |
| Classification | **(iii) Implicit Jordan appeal / PRE-JORDAN-ILLEGAL** |
| Citation proposal | **REPLACE-WITH-S0 + REPLACE-WITH-LEMMA** → `(by axiom~\ref{ax:S0} (Peirce coherence, §3.3) and Lemma~\ref{lem:peirce-preservation})`. The Phase 54 S0 axiom and Peirce-Preservation Lemma are the pre-Jordan-legal substitutes for the Peirce direct sum at compression level. |
| Scope | §S4 Case A main proof sketch. **PRIMARY PHASE 55 BUG.** INCLUDE in Plan 55-02 edit scope (HIGHEST PRIORITY). |
| Rationale | Thm 9.37 is PRE-JORDAN-ILLEGAL (Flag 4.1). The Peirce direct sum `V = ⊕_i V_2(p_i) ⊕ ⊕_{i<j} V_1(p_i,p_j)` is pre-Jordan-legal via the Phase 54 S0 axiom (mutual compressional annihilation on orthogonal projective units) + A-S compression additivity. The Phase 54 (C-i) seal authorized this substitution exactly. |
| Phase 54 cross-link | Phase 54 `\begin{axiom}[S0]` in main.tex lines 537-545 with `\label{ax:S0}`; `\begin{lemma}[Peirce-Preservation Lemma]\label{lem:peirce-preservation}` in main.tex lines 590-612 (Parts i, ii, iii). |
| Status | OPEN for Plan 55-02 (MANDATORY replacement, PRIMARY BUG) |

### Row 55-01-A4 — axiom-verification.tex:136-137 + appendix-proofs.tex:78-79 (Prop 7.43 facial absorption)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/axiom-verification.tex:136-137` AND `sections/appendix-proofs.tex:78-79` (consolidated row) |
| Verbatim quote (axiom-verification.tex) | `The crucial step invokes the Alfsen--Shultz facial absorption theorem (Proposition~7.43 of~\cite{AlfsenShultz2003}):` followed by blockquote at lines 138-141: `If $C_p(b) = 0$ and $b \ge 0$, then $b \in \mathrm{face}(p^\perp)$.` |
| Verbatim quote (appendix-proofs.tex) | `The key step is the \emph{facial absorption theorem} (Alfsen--Shultz~\cite{AlfsenShultz2003}, Proposition~7.43):` followed by blockquote at lines 80-84: `If \comp{p}(b) = 0 and b \geq 0, then b \in \mathrm{face}(p^{\perp})`. |
| Citation target | A-S 2003 vol. 190, Ch. 7, Prop 7.43 |
| Classification | **(i) A-S-compression-only / pre-Jordan-legal** (Ch. 7 is pre-Jordan-legal) |
| Citation proposal | **TIGHTEN-CITE** → `\cite[Ch.~7, Prop.~7.43]{AlfsenShultz2003}` at both sites. Preserve the existing verbatim blockquote (already correctly stated). |
| Verification status | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** (see `secondary-source-verification.md` → "Prop 7.43 Verification (Phase 55-01, 2026-04-16)" appended entry). Internal cross-reference: `derivations/04-axiom-S4.md` line 65 explicitly cites "A5 (Face containment): b >= 0 and C_p(b) = 0 => b in face(p^perp) | Alfsen-Shultz, Prop. 7.43". Paper 5 blockquote matches verbatim (modulo notation). |
| Chapter resolution | Ch. 7 "General Compressions" (p. 211) per ADDENDUM Finding 1 TOC reading |
| Fallback (if verification had failed) | Approach 2 (Foulis-Holland) — NOT TRIGGERED (verification succeeded) |
| Scope | §S4 Case B; §S4-proof Case B. INCLUDE in Plan 55-02 edit scope (HIGH priority — cite tightening, no content change). |
| Status | OPEN for Plan 55-02 (cite tightening only; content verified) |

### Row 55-01-A5 — axiom-verification.tex:143-147, 155-157 + appendix-proofs.tex:109-113 (Peirce 1-space cross-term facial-structure handwave)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/axiom-verification.tex:143-147` AND `:155-157` AND `sections/appendix-proofs.tex:109-113` (consolidated row; three parallel invocations of the same unnamed facial-structure handwave) |
| Verbatim quote (axiom-verification.tex:143-147) | `By the facial structure of spectral order unit spaces, the Peirce $1$-space components $V_1(p_i, p_j)$ connecting a face to its complement are excluded: an effect in $\mathrm{face}(p^\perp)$ has zero component in every $V_1(p_i,p_j)$ for $i\le m$, $j > m$.` |
| Verbatim quote (axiom-verification.tex:155-157) | `The Peirce $1$-space terms $Q_{jk}(a)$ either vanish by facial structure (when both $\mu_j,\mu_k>0$) or carry zero weight $\sqrt{\mu_j\mu_k}=0$.` |
| Verbatim quote (appendix-proofs.tex:109-113) | `The Peirce $1$-space terms $Q_{jk}(a)$ either vanish by facial structure (when both $\mu_{j}, \mu_{k} > 0$, so both $q_{j}, q_{k} \leq p_{+}^{\perp}$, and $a$ has no component in $V_{1}(q_{j}, q_{k})$ since $a$ is supported on the complementary face) or carry zero weight $f(\mu_{j}, 0) = 0$ (when $\mu_{k} = 0$).` |
| Citation target | Unnamed "facial structure" — no A-S prop/thm in the current text |
| Classification | **(ii) Unnamed facial appeal (post-Jordan-circular risk)** |
| Citation proposal | **REPLACE-WITH-LEMMA (Part iii)** → `by Lemma~\ref{lem:peirce-preservation} Part (iii) (R3 cross-term case, with role-swap $a \leftrightarrow b$)`. The Phase 54 Peirce-Preservation Lemma Part (iii) was authored precisely for the R3 cross-term case: `q_j, q_k ⊆ p_+^⊥` with `a` supported on `p_+` implies `Q_{jk}(a) = 0`. |
| Role-swap note | Part (iii) is stated for `L_a` acting on `V_1(p_k, p_l)` with `{p_k}` as orthogonal projective units and `a = Σ_i λ_i p_i`. For the reverse product in S4, roles swap: `b = Σ_j μ_j q_j` plays the role of "a", and `a = Σ_i λ_i p_i` plays the role of "b". The swap is licit (Part (iii) is stated for generic orthogonal families) but must be made explicit in the revision text. |
| Scope | §S4 Case B; §S4-proof Case B. INCLUDE in Plan 55-02 edit scope (HIGH priority). |
| Status | OPEN for Plan 55-02 (replacement text) |

### Row 55-01-A6 — axiom-verification.tex:154 + appendix-proofs.tex:106-108 (unnamed "facial orthogonality theorem")

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/axiom-verification.tex:154` AND `sections/appendix-proofs.tex:106-108` (consolidated row) |
| Verbatim quote (axiom-verification.tex) | `the facial orthogonality theorem gives $C_{q_j}(a) = 0$ for all $j$ with $\mu_j > 0$.` |
| Verbatim quote (appendix-proofs.tex) | `since $q_{j} \leq p_{+}^{\perp}$ and $a$ is supported on $p_{+}$ (all nonzero eigenvalues correspond to $p_{+}$), the facial orthogonality of complementary faces gives $\comp{q_{j}}(a) = 0$.` |
| Citation target | Unnamed "facial orthogonality theorem" — no A-S prop/thm in current text |
| Classification | **(ii) Unnamed facial appeal (post-Jordan-circular risk)** |
| Citation proposal | **RESOLVE-VIA-S0-TERMWISE** → explicit derivation from S0 axiom: `since $q_j \leq p_+^\perp$ and $p_i \leq p_+$ for each $i \in I_+$, orthogonality in the face lattice gives $q_j \perp p_i$; axiom~\ref{ax:S0} then yields $C_{q_j}(p_i) = 0$; by linearity of $C_{q_j}$ and the spectral decomposition $a = \sum_{i \in I_+} \lambda_i p_i$, we have $C_{q_j}(a) = \sum_i \lambda_i C_{q_j}(p_i) = 0$`. |
| Alternative (not preferred) | RESOLVE-VIA-PROP-743 — specialize Prop 7.43 to the complementary face with `(p, b) = (q_j, p_+)`. This requires a second Prop 7.43 invocation and is less direct than the S0-termwise derivation. |
| Scope | §S4 Case B; §S4-proof Case B. INCLUDE in Plan 55-02 edit scope (HIGH priority). |
| Rationale | Unnamed "facial orthogonality theorem" is an R5 + R6 pitfall (no cite + possible Jordan-circularity). The S0-termwise derivation is pre-Jordan-legal (S0 was authored for this exact use-case in Phase 54) and directly derivable from the already-available Phase 54 toolkit. |
| Status | OPEN for Plan 55-02 (replacement text with explicit derivation) |

### Row 55-01-B1 — appendix-proofs.tex:37-49 (Peirce direct sum reference in §S4-proof main proof)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/appendix-proofs.tex:37-49` |
| Verbatim quote | `By the Peirce decomposition~\eqref{eq:peirce-proj}, the terms $\comp{p_{i}}(b) \in V_{2}(p_{i})$ and $\peirce{ij}(b) \in V_{1}(p_{i}, p_{j})$ lie in mutually orthogonal subspaces.  In a direct sum, a sum vanishes if and only if each summand vanishes.` |
| Citation target | `\eqref{eq:peirce-proj}` (internal Paper 5 equation label); no A-S cite |
| Classification | **(i) A-S-compression-only / pre-Jordan-legal** (after Phase 54 integration; `\eqref{eq:peirce-proj}` upstream resolves through main.tex §3.3) |
| Citation proposal | **TIGHTEN-CITE** (optional) → add parenthetical `(by axiom~\ref{ax:S0} and Lemma~\ref{lem:peirce-preservation})` alongside `\eqref{eq:peirce-proj}` for reader clarity. |
| Scope | §S4-proof Case A/B opening. LOW priority for Plan 55-02 (reader-aid tightening; not a correctness issue). |
| Status | OPEN for Plan 55-02 (optional) |

### Row 55-01-B2 — appendix-proofs.tex:85-89 (compressions act independently on orthogonal faces)

| Field | Value |
|-------|-------|
| Paper 5 file:line | `sections/appendix-proofs.tex:85-89` |
| Verbatim quote | `Since $\comp{p_{i}}(b) = 0$ for each $i \in I_{+}$, and compressions for orthogonal projective units act independently on their respective faces, we have $\comp{p_{+}}(b) = \sum_{i \in I_{+}} \comp{p_{i}}(b) = 0$.` |
| Citation target | Unnamed "compressions ... act independently" — no A-S cite |
| Classification | **(i) A-S-compression-only / pre-Jordan-legal** (the statement is true; just needs a cite) |
| Citation proposal | **TIGHTEN-CITE** → add `\ref{ax:S0}` (S0 axiom) for the independence property, OR `\cite[Ch.~7, Prop.~7.50]{AlfsenShultz2003}` for the compression-composition route. Either is pre-Jordan-legal. |
| Scope | §S4-proof Case B support-projection step. MEDIUM priority for Plan 55-02. |
| Rationale | The "act independently" claim is exactly S0 (mutual annihilation on orthogonal pairs) + compression additivity. Phase 54 Prop 7.50 internal cross-reference authorizes the `C_p ∘ C_q = C_{p ∧ q}` route. |
| Status | OPEN for Plan 55-02 (citation insertion) |

---

## Change Log Addendum (Phase 55-01)

- **2026-04-16 (Phase 55-01):** Appended Section 8 with 7 new rows covering Paper 5 `sections/axiom-verification.tex` §S4 region + contiguous pre-S4 Thm 9.37 at line 68, and `sections/appendix-proofs.tex` §S4-proof region. No Phase 54 row modified (append-only discipline).

  **Rows added:**
  - **55-01-A1** — axiom-verification.tex:39 → (i) TIGHTEN-CITE (S1 proof bare Ch. 7 cite; LOW priority)
  - **55-01-A2** — axiom-verification.tex:68 → (iii) REPLACE (Thm 9.37 in S2 proof; PRE-S4 SCOPE per 55-01-CLASSIFICATION.md Section 4; MANDATORY Plan 55-02 fix)
  - **55-01-A3** — axiom-verification.tex:125 → (iii) REPLACE-WITH-S0 + REPLACE-WITH-LEMMA (Thm 9.37 for Peirce direct sum; PRIMARY PHASE 55 BUG)
  - **55-01-A4** — axiom-verification.tex:136-137 + appendix-proofs.tex:78-79 → (i) TIGHTEN-CITE (Prop 7.43 facial absorption; **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** per `secondary-source-verification.md` Phase 55-01 entry at `derivations/04-axiom-S4.md:65`)
  - **55-01-A5** — axiom-verification.tex:143-147, 155-157 + appendix-proofs.tex:109-113 → (ii) REPLACE-WITH-LEMMA (Part iii) (Peirce 1-space cross-term handwave; role-swap required)
  - **55-01-A6** — axiom-verification.tex:154 + appendix-proofs.tex:106-108 → (ii) RESOLVE-VIA-S0-TERMWISE (unnamed "facial orthogonality theorem"; explicit S0-termwise derivation)
  - **55-01-B1** — appendix-proofs.tex:37-49 → (i) TIGHTEN-CITE optional (Peirce direct sum reference; reader-aid)
  - **55-01-B2** — appendix-proofs.tex:85-89 → (i) TIGHTEN-CITE (compressions act independently; add S0 or Prop 7.50 cite)

  **A-S 2001 citation check:** `grep -n 'AlfsenShultz2001' sections/axiom-verification.tex sections/appendix-proofs.tex` returns zero hits. No fp-volume-collapse bug to correct in the §S4 region.

  **Prop 7.43 verification status:** VERIFIED-VIA-INTERNAL-CROSS-REFERENCE → A-S 2003 Ch. 7, Prop 7.43 via `derivations/04-axiom-S4.md` line 65. Exact statement `b ≥ 0 ∧ C_p(b) = 0 ⟹ b ∈ face(p^⊥)` matches Paper 5 blockquote verbatim.

  **Line 68 scope decision:** PRE-S4 SCOPE (S2 proof), INCLUDE IN PLAN 55-02 EDIT SCOPE. See `.gpd/phases/55-s4-facial-structure-lemma/55-01-CLASSIFICATION.md` Section 4 for 3+ sentence justification.

  **Consumed by:** Plan 55-02 (revision text + integration), Plan 55-03 (phase close + adversarial review).

  **Classification document:** `.gpd/phases/55-s4-facial-structure-lemma/55-01-CLASSIFICATION.md`.

---

_Downstream consumers (Phases 55, 57, 58) may append rows but MUST NOT modify existing rows without a dated change-log entry. Resolving a VERIFICATION-DEFERRED / QUOTE-PENDING / NEEDS-VERIFICATION row is a modification and requires the change-log entry; do NOT silently overwrite. Paraphrasing A-S book text is strictly forbidden per fp-as-notes-paraphrase — if the book is not accessible, keep the QUOTE-PENDING marker and flag for later verification._
