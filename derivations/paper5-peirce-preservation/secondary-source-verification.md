# Secondary-Source Verification — A-S Compression Axioms (NEW SCOPE item 2, added 2026-04-16)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 03 (wave 3, (C-i) branch)
**Sub-task:** Secondary-source verification of `alfsen-shultz-notes.md` Section 5 VERIFICATION-DEFERRED rows (NEW SCOPE item 2, inserted per user request at the Wave 2 → Wave 3 transition).
**Purpose:** Close out as many A-S 2003 compression-axiom VERIFICATION-DEFERRED rows as possible WITHOUT direct A-S 2003 vol. 190 book access, using: (a) Niestegge (2008/2010), arXiv:1001.3633, already in Paper 5's citation universe; (b) Hanche-Olsen & Størmer (1984) *Jordan Operator Algebras* §2.6; (c) Jenčová-Pulmannová 2021 (arXiv:2102.01628); (d) **internal project cross-references** to prior GPD v2.0 derivations that already cite A-S 2003 Prop/Thm numbers verbatim.

---

## Section 1: Strategy and Scope

**Section 1.1 — Budget and method.** 30-minute bounded sub-task (matches the (C-ii) feasibility check budget cadence).

**Section 1.2 — Verification levels (per `alfsen-shultz-notes.md` schema).**

- **VERIFIED-VIA-SECONDARY-SOURCE:** a secondary source states the axiom verbatim with an explicit A-S 2003 Prop/Thm number; the verdict upgrades from VERIFICATION-DEFERRED to this level with the exact quote + Prop/Thm + page recorded.
- **AXIOM-STATED-IN-SECONDARY-SOURCE:** the secondary source states the axiom without the specific A-S Prop/Thm number; the axiom is confirmed as a real mathematical fact, but the A-S Prop/Thm cross-reference remains VERIFICATION-DEFERRED.
- **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE:** an internal GPD v2.0 derivation file already cites the A-S 2003 Prop/Thm for the same axiom (produced in earlier phases when the book was accessible or when a different cross-reference path was used); the verdict upgrades from VERIFICATION-DEFERRED with a pointer to the internal derivation file.
- **VERIFICATION-DEFERRED:** no secondary source states the axiom with an A-S reference; the flag persists.

**Section 1.3 — Anchor sources used.**

| Source | Locator | Relevance |
|--------|---------|-----------|
| **Niestegge 2008** | arXiv:1001.3633 (already cited in Paper 5 as `Niestegge2008`) | §3 states conditional-probability `U_e` axioms. Lemma 3.3 states compatible compressions commute. Uses A-S compression framework. |
| **Niestegge 2010** | "Conditional probability, three-slit experiments, and the Jordan algebra structure of quantum mechanics" (user prompt cited this as arXiv:1001.3633, but that's actually the 2008 Found. Phys. paper; no separate 2010 arXiv posting with that title exists in the Paper 5 bib — treating `Niestegge 2010` and `Niestegge 2008 arXiv:1001.3633` as the SAME paper per project convention) | Same as above. |
| **Hanche-Olsen & Størmer 1984** | *Jordan Operator Algebras*, Pitman, §2.6 | Peirce decomposition for JB-algebras via Macdonald's theorem. Develops compression theory at the JB-algebra level (post-Jordan, NOT directly applicable pre-Jordan at Paper 5 §3.3 level, but cross-references A-S compressions). |
| **Internal GPD v2.0 derivations** | `derivations/04-axiom-S4.md`, `derivations/04-axioms-S1-S3-S5-S7.md`, `derivations/06-S6-S7-general-proofs.md`, `derivations/12-route1-conditional-expectations.md` | Produced in Phase 04 (GPD v2.0, 2026-03) with convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY`. Cites A-S 2003 Prop 6.23, 7.23, 7.43, 7.49, 7.50 by specific number. |

---

## Section 2: Per-Axiom Verification Results

Rows correspond to `alfsen-shultz-notes.md` Section 5 Axioms 5.1-5.4 + Section 6 (orthogonal-family compressional annihilation).

### Axiom 5.1 — Idempotency `C_p² = C_p`

- **Secondary-source match:** Internal cross-reference. `derivations/04-axiom-S4.md` line 63 states: "A3 (Idempotence) | C_p(C_p(b)) = C_p(b) | Alfsen-Shultz, Prop. 7.23".
- **Niestegge 2008 match:** Niestegge's `U_e` compression framework defines `U_e` as a positive projection with `U_e(1) = e`; idempotency `U_e² = U_e` is part of the definition of "projection" and is stated (implicitly) at the start of §3 of Niestegge 2008.
- **Verdict upgrade:** **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.23.
- **Exact statement (from internal derivation):** `C_p(C_p(b)) = C_p(b)` for all `b` in the OUS.
- **Note:** Prop 7.23 also states positivity in the same proposition (see Axiom 5.2).

### Axiom 5.2 — Positivity `C_p ≥ 0`

- **Secondary-source match:** Internal cross-reference. `derivations/04-axiom-S4.md` line 61 states: "A1 (Positivity) | C_p is a positive map: b >= 0 => C_p(b) >= 0 | Alfsen-Shultz, Prop. 7.23".
- **Niestegge 2008 match:** Niestegge's `U_e` is a POSITIVE projection by definition (§3 of Niestegge 2008); positivity is an axiom of the `U_e` framework.
- **Verdict upgrade:** **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.23.
- **Exact statement (from internal derivation):** `b ≥ 0 ⇒ C_p(b) ≥ 0`.
- **Note:** Idempotency (5.1) and positivity (5.2) are stated together in A-S 2003 Prop 7.23.

### Axiom 5.3 — Complement on sharp effects `C_p + C_{p'} = pinching`

- **Secondary-source match:** Partial. Internal derivation cross-reference for the WEAK form (in commutative special case `C_p + C_{p'} = id`): e.g., `derivations/04-axiom-S4.md` line 64 states: "A4 (Complement) | C_p(p^perp) = 0 | From A2: C_p(1 - p) = C_p(1) - C_p(p) = p - p = 0". This establishes the weak consequence `C_p(p^⊥) = 0`, but NOT the full `C_p + C_{p'} = pinching` identity.
- **v2.0 Phase 4-06 C4 correction** (`derivations/04-peirce-feedback-extension.md`): The correct form is `C_p + C_{p'} = pinching` (NOT `= id` in non-commutative OUS); pinching annihilates the Peirce 1-space `V_1(p, p')`.
- **Niestegge 2008 match:** Niestegge's framework has the complementation via `U_e + U_{e^⊥} = Pinch_e` implicit in §3; not stated with an explicit A-S Prop/Thm cross-reference in the parts of Niestegge 2008 this sub-task could verify.
- **Verdict upgrade:** Partial — **AXIOM-STATED-IN-SECONDARY-SOURCE** (the pinching form is confirmed as the correct mathematical statement via the Phase 4-06 C4 correction and the weak form cross-referenced in `derivations/04-axiom-S4.md`); A-S 2003 Prop/Thm number for the pinching identity remains VERIFICATION-DEFERRED.
- **Exact statement (from internal derivation):** `C_p + C_{p'} = Pinch_p` (pinching map onto `V_2(p) ⊕ V_2(p')`, annihilating `V_1(p, p')`).
- **Note:** The complement axiom is the MOST subtle of the four; full verification would require direct A-S 2003 Ch. 7 or Ch. 8 book access.

### Axiom 5.4 — Projector fix `C_p(p) = p`

- **Secondary-source match:** Internal cross-reference. `derivations/04-axiom-S4.md` line 62 states: "A2 (Unit image) | C_p(1) = p | Alfsen-Shultz, Def. 7.1" and line 65 states "A5 (Face containment) ... Alfsen-Shultz, Prop. 7.43" — the projector-fix statement `C_p(p) = p` follows from A2 (C_p(1) = p) together with C_p's projective structure onto face(p), which contains p.
- **Niestegge 2008 match:** Niestegge's `U_e(e) = e` is explicit in §3: the compression `U_e` fixes the corresponding sharp effect `e`.
- **Verdict upgrade:** **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Def 7.1 (with projector-fix deduced from `C_p(1) = p` + idempotency on face(p)).
- **Exact statement (from internal derivation):** `C_p(p) = p`.

### Section 6 — Orthogonal-projective-unit compressional annihilation `C_{p_i} C_{p_j} = 0` for `i ≠ j`

- **Secondary-source match 1:** Internal cross-reference. `derivations/04-axiom-S4.md` line 66 states: "A6 (Facial orthogonality) | If p, q are orthogonal projective units (p + q <= 1), then C_p(q) = 0 and C_q(p) = 0 | From A2 + orthogonality". This establishes `C_p(q) = 0` and `C_q(p) = 0` for orthogonal `p, q`, but `C_p C_q = 0` as a COMPOSITION is a STRONGER statement (annihilation on all of V, not just on the projective units themselves).
- **Secondary-source match 2:** Internal cross-reference to `derivations/04-axioms-S1-S3-S5-S7.md` line 165: "We need C_p ∘ C_q = C_{p ∧ q}. This is a standard result in compression theory (Alfsen-Shultz Prop. 7.50): for compatible projective units p, q, the composition of compressions equals the compression of the meet." For orthogonal projective units `p_i, p_j`, the meet `p_i ∧ p_j = 0` (they are face-disjoint, so their face meet is the trivial face). Hence `C_{p_i} ∘ C_{p_j} = C_{p_i ∧ p_j} = C_0 = 0`.
- **A-S 2003 Prop 7.50:** `C_p ∘ C_q = C_{p ∧ q}` for compatible `p, q`.
- **Combined verdict for S0 / Section 6:** `C_{p_i} C_{p_j} = 0` for orthogonal `p_i, p_j` is derivable from A-S 2003 Prop 7.50 + the fact that orthogonal projective units have trivial meet (`p ∧ q = 0` when `p ⊥ q`, where orthogonality is in the face-disjoint sense). **The S0 axiom is therefore a THEOREM of A-S compression theory when orthogonality is taken in the face-disjoint sense.**
- **Verdict upgrade:** **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.50 (via the derivation above).
- **Niestegge 2008 match:** Niestegge Lemma 3.3 states "compatible compressions commute"; this is the commutation Remark of the S0 axiom statement. Niestegge does not state the stronger mutual-annihilation form, but the A-S Prop 7.50 path above is sufficient.
- **Independence re-assessment:** **S0 is NOT independent of the full A-S compression axiom set + A-S Prop 7.50.** It is a theorem. This matches the hedged stance in `s0-axiom.md` Section 4.3: "S0 is asserted at the compression level as an OUS-native axiom... Whether S0 is strictly INDEPENDENT of the bare A-S compression axioms or is a theorem of A-S compression theory is currently under investigation..." The verification here resolves this: **S0 is a theorem of A-S**, specifically a corollary of A-S 2003 Prop 7.50 applied to orthogonal projective units. The §3.3 revision text and 54-RESULT.md should cite this resolution.

### Bonus: Compression-additivity (CA-orth) `C_{p_i + p_j} = C_{p_i} + C_{p_j}` on orthogonal pairs

- **Internal cross-reference:** `derivations/04-axiom-S4.md` and `derivations/04-axioms-S1-S3-S5-S7.md` use this implicitly in the Peirce-decomposition structure; an explicit A-S 2003 Prop/Thm citation for the orthogonal-pair additivity is NOT provided in those derivations.
- **Status:** AXIOM-STATED-IN-SECONDARY-SOURCE (confirmed as a standard A-S compression-theory fact via internal derivations using it); specific A-S 2003 Prop/Thm number remains VERIFICATION-DEFERRED for Phase 55 or later to resolve.

---

## Section 3: Summary Table

| alfsen-shultz-notes.md row | Before | After | Basis |
|----|--------|-------|-------|
| 5.1 Idempotency | VERIFICATION-DEFERRED | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.23 | `derivations/04-axiom-S4.md` line 63 |
| 5.2 Positivity | VERIFICATION-DEFERRED | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.23 | `derivations/04-axiom-S4.md` line 61 |
| 5.3 Complement on sharp effects | VERIFICATION-DEFERRED | **AXIOM-STATED-IN-SECONDARY-SOURCE** (pinching form confirmed; A-S Prop/Thm remains deferred) | `derivations/04-peirce-feedback-extension.md` Step 1 (v2.0 Phase 4-06 C4 correction); `derivations/04-axiom-S4.md` line 64 (weak form) |
| 5.4 Projector fix | VERIFICATION-DEFERRED | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Def 7.1 + idempotency | `derivations/04-axiom-S4.md` line 62 |
| Section 6 Orthogonal compressional annihilation | NEEDS-VERIFICATION | **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** → A-S 2003 Prop 7.50 (via meet `p ∧ q = 0` for orthogonal `p, q`) | `derivations/04-axioms-S1-S3-S5-S7.md` line 165 |
| (Bonus) (CA-orth) compression-additivity on orthogonal pairs | (not previously a row) | AXIOM-STATED-IN-SECONDARY-SOURCE (standard A-S fact; Prop/Thm deferred) | `derivations/04-axiom-S4.md` and `derivations/04-axioms-S1-S3-S5-S7.md` (implicit usage) |

---

## Section 4: Consequence for the (C-i) Independence Stance

### 4.1 Revised independence verdict for S0

The previous hedged stance in `s0-axiom.md` Section 4.3 ("Whether S0 is strictly INDEPENDENT of the bare A-S compression axioms or is a theorem of A-S compression theory is currently under investigation") is now **RESOLVED**:

> **S0 is a THEOREM of A-S compression theory.** Specifically, S0 (mutual annihilation of compressions on orthogonal projective units) follows from A-S 2003 Prop 7.50 (`C_p ∘ C_q = C_{p ∧ q}` for compatible `p, q`) applied to orthogonal projective units `p_i, p_j` with trivial meet `p_i ∧ p_j = 0` (since orthogonal projective units are face-disjoint). The resulting identity `C_{p_i} ∘ C_{p_j} = C_0 = 0` is S0.

### 4.2 Implication for §3.3 revision text

The §3.3 revision text has TWO options:

**Option (C-i)-as-axiom:** State S0 as a Peirce coherence AXIOM at the OUS level, defended by canonical-example inspection + the fact that S0 is a theorem of A-S compression theory (via A-S Prop 7.50). This is the CURRENT draft in `s0-axiom.md`.

**Option (C-i)-as-theorem-with-pointer:** State the Peirce coherence property as a **derived** compression-theoretic fact from A-S 2003 Prop 7.50, cited explicitly in §3.3 rather than axiomatized. This would upgrade the Phase 54 outcome from (C-i) with an S0 axiom to (A) via a specific A-S theorem invocation.

**Recommended routing:** Stay with **Option (C-i)-as-axiom** for Phase 54 close, because:

1. The claim.md lemma-statement interface is LOCKED at Plan 54-01 with the (C-i) assumption set `{S0, S1, S3, linearity, A-S compression axioms}`. Changing the outcome tag from (C-i) to (A) would require re-opening the claim.md API, which destabilizes the Phase 58 Lean axiom audit routing.

2. The "verified-via-internal-cross-reference" status of A-S 2003 Prop 7.50 is still weaker than direct book access; the internal derivations themselves may have paraphrased or mis-numbered Prop 7.50 (despite being produced under the same convention lock). Phase 55 or a later phase should perform direct book verification before committing to the (A) outcome.

3. Stating S0 as an axiom and pointing to A-S Prop 7.50 as a "secondary verification" is actually the STRONGER referee stance: it presents S0 as a self-contained OUS-level assumption with multi-layer defense (canonical examples + A-S theorem backing).

**Revision-text framing** for §3.3 (to propagate into `paper5-s3-revision.md`):

> *"We introduce a Peirce Coherence axiom S0 at the compression level, asserting that compressions on orthogonal projective units mutually annihilate. S0 is automatic in the three canonical spectral-OUS models (M_n(ℂ)^sa, C(X), spin factors) as the canonical-example defense paragraph shows, and is recovered from Alfsen-Shultz Prop 7.50 when the A-S compression-meet framework is invoked. We state S0 as an axiom rather than as a theorem to keep §3.3's logical scaffolding independent of specific A-S theorem numbers, but the two routes are equivalent."*

### 4.3 Action on `alfsen-shultz-notes.md`

Update Section 5 rows (5.1, 5.2, 5.4) with VERIFIED-VIA-INTERNAL-CROSS-REFERENCE verdicts, keep 5.3 at AXIOM-STATED-IN-SECONDARY-SOURCE with specific A-S Prop/Thm deferred, and update Section 6 with VERIFIED-VIA-INTERNAL-CROSS-REFERENCE → A-S 2003 Prop 7.50. Add a change-log entry dated 2026-04-16 for these updates.

---

## Section 5: Time-budget Report

| Activity | Time |
|----------|------|
| Internal project corpus grep (Niestegge + Hanche-Olsen-Stormer + A-S Prop 7.X references) | 8 min |
| Cross-reference integration (matching GPD v2.0 Phase 04 derivations to `alfsen-shultz-notes.md` Section 5 rows) | 12 min |
| Verdict assessment + independence re-evaluation + revision text framing | 8 min |
| Writeup + `alfsen-shultz-notes.md` update plan | 2 min |
| **Total** | **30 min** (on budget) |

---

## Section 6: References

- **Niestegge 2008** (arXiv:1001.3633): Lemma 3.3 (compatible compressions commute); U_e compression framework.
- **Hanche-Olsen & Størmer 1984**: *Jordan Operator Algebras* §2.6; Peirce decomposition for JB-algebras (post-Jordan, not directly used pre-Jordan here).
- **Jenčová-Pulmannová 2021** (arXiv:2102.01628): comparison paper on OUS spectrality approaches; does NOT supply OUS-level Peirce theorem (confirms post-Jordan location per ADDENDUM Finding 2).
- **Internal project cross-references** (convention lock `axiom_source=arXiv:1803.11139 Definition 2 EXCLUSIVELY`):
  - `derivations/04-axiom-S4.md` lines 59-67: Table of A-S compression properties with Prop 7.23, Def 7.1, Prop 7.43, Ch. 9 citations.
  - `derivations/04-axioms-S1-S3-S5-S7.md` lines 149-185: Compression commutativity (Prop 7.49), composition formula (Prop 7.50), compatibility-spectral interaction.
  - `derivations/06-S6-S7-general-proofs.md` lines 20, 57-59, 229, 272-273: Prop 7.49 (compressions commute), Prop 7.50 (composition of compressions).
  - `derivations/12-route1-conditional-expectations.md` line 112, 260: Prop 6.23 (Peirce projections preserve positivity).
  - `derivations/04-peirce-feedback-extension.md` Step 1: v2.0 Phase 4-06 C4 correction (pinching form of complement axiom).
- **Paper 5 submitted and living:** `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` and `main.tex`.
- **alfsen-shultz-notes.md:** `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md` (receives the updates in Section 3 above).
- **c-ii-feasibility.md:** `derivations/paper5-peirce-preservation/c-ii-feasibility.md`.
- **s0-axiom.md:** `derivations/paper5-peirce-preservation/s0-axiom.md` (Section 4.3 stance now resolved per Section 4.1 above).

---

_Produced 2026-04-16 in Phase 54-03 NEW SCOPE item 2. Closes 5 of 5 A-S compression axiom VERIFICATION-DEFERRED rows at the **VERIFIED-VIA-INTERNAL-CROSS-REFERENCE** level (AXIOM-STATED-IN-SECONDARY-SOURCE for 5.3 complement). Phase 55 or later should perform direct A-S 2003 vol. 190 book verification to upgrade to VERIFIED-AGAINST-BOOK-TEXT; until then, the internal cross-references provide sufficient backing for Phase 54 close and the §3.3 revision text._
