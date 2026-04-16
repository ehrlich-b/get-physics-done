# Alfsen-Shultz Citation Resolution — Paper 5 §3.3-§3.4 Baseline (Phase 54-01) [SHARED ARTIFACT]

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: as_2001=Alfsen-Shultz 2001 vol. 179 "State Spaces of Operator Algebras" (Birkhäuser Progress in Mathematics 179); as_2003=Alfsen-Shultz 2003 vol. 190 "Geometry of State Spaces of Operator Algebras" (Birkhäuser Progress in Mathematics 190); NEVER collapse the two volumes into "Alfsen-Shultz"; any AMBIGUOUS volume requires a dated research TODO

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

The §3.3 citation at line 513 is THE citation that Phase 54 replaces. Rows for A-S-outside-the-explicit-\cite-scope (e.g., line 423 `Alfsen--Shultz compression for the face` which is in §3.2) are handled in the A-S 2001 Ch. 7-8 compression axioms sub-table (Section 5) rather than as independent citation rows.

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

1. **"Compressions project onto these subspaces"** — pre-Jordan-legal. Compressions onto faces (A-S 2001 Ch. 7 compression theory; A-S 2003 Ch. 7 general compressions). If the cite is for this, correct vol. is 2001 vol. 179 Ch. 7, not 2003 vol. 190. Paper 5 cites the wrong volume.

2. **"Linearity gives a block decomposition that `\seqp{a}{\cdot}` maps each Peirce subspace to itself"** — this is the R2 non-sequitur. NO A-S theorem (either volume) implies that a GENERAL linear map `L_a` respects the Peirce decomposition; the only A-S-level facts are (a) individual compressions preserve their own range (Peirce 2-space), not that a COMPOSITE map respects the full decomposition. This is the core Phase 54 claim to prove or axiomatize.

Therefore the line-513 citation is:

- **Either insufficient (it doesn't license the full claim)** → DOES-NOT-IMPLY
- **Or mis-cited (wrong volume; the compression-projects-onto-face fact is A-S 2001 Ch. 7-8)** → DOES-NOT-IMPLY as it stands
- **Or implicitly invoking A-S 2003 Thm 9.37** (the Peirce direct sum theorem in the Jordan chapter) → PRE-JORDAN-ILLEGAL per ADDENDUM

**Action for downstream phases:** This row MUST be resolved (disambiguate which of the three sub-cases applies) before Paper 5 §3.3 can be rewritten with a correct A-S citation. Plan 54-03 replaces this citation entirely: (A) would cite A-S 2001 Ch. 7-8 compression axioms (correct volume); (C-i) would invoke S0 axiom and drop the post-Jordan appeal.

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
| Replacement | Any Paper 5 §3.3 invocation of Thm 9.37 MUST be replaced by either (a) A-S 2001 vol. 179 Ch. 7-8 compression citation (if the invoked property is compression-theoretic and the claim is correctly scoped) OR (b) the Phase 54 (C-i) S0 axiom (if the invoked property is Peirce-invariance of the left-multiplication `L_a`). |
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

## Section 5: A-S 2001 Ch. 7-8 Compression Axioms Sub-Table

The four A-S compression axioms actually used in Phase 54 (A-S 2001 vol. 179 Ch. 7-8). Source is A-S 2001 per the pre-Jordan-legal requirement (A-S 2003 Ch. 9 is post-Jordan illegal per Flag 4.1).

**Important scope note:** The executor at Phase 54-01 time (2026-04-16) does NOT have A-S 2001 vol. 179 physical or digital book access. All entries below are marked VERIFICATION-DEFERRED for the Prop/Thm number and QUOTE-PENDING for the exact book statement. **These must be resolved before any Phase 54 attempt closes** (planned in Plan 54-02 or 54-03 as a supporting task, or assigned to a human verification step).

### Axiom 5.1 — Idempotency: `C_p² = C_p`

| Field | Value |
|-------|-------|
| Compression axiom name | Idempotency |
| Formal statement | For any compression `C_p` (A-S 2001 P-projection onto face(p)), `C_p ∘ C_p = C_p`. |
| Source volume | **A-S 2001 vol. 179** |
| Chapter | Ch. 7 (compression theory; per Active Anchor Registry in 54-CONTEXT.md) |
| Section | UNCERTAIN |
| Exact Prop/Thm number | VERIFICATION-DEFERRED — book not accessed by Phase 54-01 executor (2026-04-16). Candidates from secondary sources: may be in A-S 2001 Ch. 7 §1 as a definition property (a compression is defined as a positive idempotent onto a face), not a theorem. Must be verified. |
| Exact-book-statement | QUOTE-PENDING — 2026-04-16 TODO. |
| Phase 54 usage | Foundational in every (A) attempt and the (C-i) derivation of Propositions 3.1, 3.2, 3.3 in claim.md. |

### Axiom 5.2 — Positivity: `C_p ≥ 0`

| Field | Value |
|-------|-------|
| Compression axiom name | Positivity |
| Formal statement | For any compression `C_p`, `C_p` preserves the positive cone: `b ≥ 0 ⇒ C_p(b) ≥ 0`. |
| Source volume | **A-S 2001 vol. 179** |
| Chapter | Ch. 7 |
| Section | UNCERTAIN |
| Exact Prop/Thm number | VERIFICATION-DEFERRED — 2026-04-16 TODO. |
| Exact-book-statement | QUOTE-PENDING — 2026-04-16 TODO. |
| Phase 54 usage | Used in positivity-bound arguments in Plan 54-02 (A) attempt and claim.md Section 4.3. |

### Axiom 5.3 — Complement on sharp effects: `C_p + C_{p'} = pinching` (NOT = id in non-commutative OUS)

| Field | Value |
|-------|-------|
| Compression axiom name | Complement on sharp effects |
| Formal statement | For a sharp effect `p` and its complement `p' := 1 − p`, `C_p + C_{p'}` equals the **pinching map** `Pinch(b) = C_p(b) + C_{p'}(b)` — which is NOT the identity in non-commutative OUS; the map `Pinch` annihilates the Peirce 1-space `V_1(p, p')`. |
| Source volume | **A-S 2001 vol. 179** + correction from `derivations/04-peirce-feedback-extension.md` Step 1 (v2.0 Phase 4-06 C4 correction) |
| Chapter | Ch. 7 or Ch. 8 (spectral) |
| Section | UNCERTAIN |
| Exact Prop/Thm number | VERIFICATION-DEFERRED — 2026-04-16 TODO. |
| Exact-book-statement | QUOTE-PENDING — 2026-04-16 TODO. |
| Important caveat | This was INCORRECTLY stated as `C_p + C_{p'} = id` in v2.0 Phase 4 Plan 01 C4; the correct form (`= pinching`, not `= id`) is documented in `derivations/04-peirce-feedback-extension.md` Step 1. Every Phase 54 attempt must use the CORRECTED form. |
| Phase 54 usage | Central to Peirce-1-space analysis in Propositions 3.2 and 3.3 of claim.md. |

### Axiom 5.4 — Projector fix: `C_p(p) = p`

| Field | Value |
|-------|-------|
| Compression axiom name | Projector fix |
| Formal statement | `C_p(p) = p` — the compression onto face(p) fixes p itself. |
| Source volume | **A-S 2001 vol. 179** |
| Chapter | Ch. 7 |
| Section | UNCERTAIN |
| Exact Prop/Thm number | VERIFICATION-DEFERRED — 2026-04-16 TODO. |
| Exact-book-statement | QUOTE-PENDING — 2026-04-16 TODO. |
| Phase 54 usage | Used in Proposition 3.1 (V_2-invariance) argument and in relating compression action on sharp vs non-sharp effects. |

---

## Section 6: Orthogonal-Projective-Unit Compressional Annihilation

The fact `C_{p_i} C_{p_j} = 0` for orthogonal projective units `i ≠ j` is a CENTRAL Phase 54 tool (used in claim.md Section 4.3 and in every (A)/ (C-i) proof of the three target inclusions). Its status:

| Field | Value |
|-------|-------|
| Statement | `C_{p_i} C_{p_j} = 0` for `i ≠ j` in an orthogonal family `{p_k}` of projective units in a spectral OUS |
| Source volume (candidate) | **A-S 2001 vol. 179** Ch. 7 or Ch. 8 |
| Chapter / Section / Prop-or-Thm | UNCERTAIN — VERIFICATION-DEFERRED — 2026-04-16 TODO |
| Exact-book-statement | QUOTE-PENDING — 2026-04-16 TODO |
| Match-to-Paper-5 verdict | **NEEDS-VERIFICATION** |
| Contingency | If this fact is NOT cleanly derivable from A-S 2001 Ch. 7-8 (e.g., it turns out to only appear at the JB-algebra / Ch. 9 / Ch. 1 level of A-S 2003), then this becomes the load-bearing piece that **must be taken as part of Phase 54's S0 axiom** under the (C-i) outcome. The (C-i) S0 axiom (candidate form per claim.md Section 4.6) explicitly includes "C_{p_i} C_{p_j} = 0 for i ≠ j" for exactly this reason. |
| Research TODO (2026-04-16) | Verify whether `C_{p_i} C_{p_j} = 0` for orthogonal projective units is stated in A-S 2001 vol. 179 Ch. 7-8 with specific Prop/Thm number OR whether it must be axiomatized via S0. Downstream attempts (Plan 54-02 single (A) attempt) cannot seal until this is resolved. If the A-S 2001 version is available, (A) is not foreclosed on this axis; if not, (A) is pre-foreclosed and (C-i) is the only remaining route. |
| Phase 54 coupling | This is the **hinge** between (A) and (C-i). If this fact is A-S-legal pre-Jordan, (A) is possible. If not, (A) fails and (C-i) is necessary. Plan 54-02 and 54-03 must resolve this before closing. |

---

## Section 7: Change Log

```
## Change Log
- 2026-04-16 (Phase 54-01, Task 4): Initial §3.3-§3.4 baseline created.
  - 1 \cite{AlfsenShultz...} row resolved (line 513, 2003 vol. 190, verdict DOES-NOT-IMPLY / PRE-JORDAN-ILLEGAL variants).
  - Thm 9.37 flagged PRE-JORDAN-ILLEGAL (Flag 4.1; QUOTE-PENDING; transcription TODO).
  - Prop 7.36 flagged PROP-NUMBER-UNVERIFIED (Flag 4.2; QUOTE-PENDING; transcription TODO; potential type-(iii) statement-mismatch for Phase 58).
  - A-S 2001 Ch. 7-8 compression axioms sub-table: 4 axioms recorded with VERIFICATION-DEFERRED / QUOTE-PENDING markers.
  - Section 6: orthogonal-projective-unit compressional annihilation flagged NEEDS-VERIFICATION (hinge between (A) and (C-i)).
  - No A-S statements paraphrased; all un-quoted entries are explicitly QUOTE-PENDING / VERIFICATION-DEFERRED per fp-as-notes-paraphrase.
  - No collapsed "Alfsen-Shultz" citations; AlfsenShultz2003 at line 513 resolved explicitly to 2003 vol. 190.
- <future phases append here as rows are extended or resolved>
```

---

_Downstream consumers (Phases 55, 57, 58) may append rows but MUST NOT modify existing rows without a dated change-log entry. Resolving a VERIFICATION-DEFERRED / QUOTE-PENDING / NEEDS-VERIFICATION row is a modification and requires the change-log entry; do NOT silently overwrite. Paraphrasing A-S book text is strictly forbidden per fp-as-notes-paraphrase — if the book is not accessible, keep the QUOTE-PENDING marker and flag for later verification._
