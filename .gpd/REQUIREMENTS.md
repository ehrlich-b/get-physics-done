# Requirements: Paper 5 Revision -- Close Load-Bearing Jigsaw-Piece Gaps

**Defined:** 2026-04-16
**Core Research Question:** Can each of the six jigsaw-piece gaps in the submitted Paper 5 be closed with outcome (A) rigorous proof, (B) precise external citation, or (C) explicit structural-gap characterization, before the JMP referee report arrives?

## Milestone Context

Paper 5 ("Quantum Mechanics from Self-Modeling") was submitted to JMP 2026-03-28 (JMP26-AR-00922, Zenodo DOI 10.5281/zenodo.19342703) and is 19 days with the associate editor (as of 2026-04-16). A jigsaw-piece-level review identified six places where the logical chain is visually sound but the author cannot independently reconstruct the argument from primitives. One is load-bearing (Phase 54 §3.3 Peirce preservation); the rest are material. Close them before the referee report lands so revisions ship fast and survive scrutiny.

**Central risk (per PITFALLS.md):** circularity — invoking Jordan structure to prove something that feeds vdW Theorem 1, which is what *produces* Jordan structure. Every phase's success criteria includes a circularity audit.

**Prior on Phase 54 outcomes (per ADDENDUM + PRIOR-WORK + METHODS synthesis):**
- (A) proof from OUS primitives via GPD v2.0 Phase 4-06 corrected-product formula — MEDIUM, conditional on Phase 4-06 circularity audit passing
- (B) precise external Alfsen-Shultz citation — essentially ruled out; Peirce decomposition is post-Jordan in accessible literature (A-S 2003 TOC + Jenčová-Pulmannová 2021 §3-5)
- (C-i) add OUS-level "Peirce coherence" axiom S0 alongside S1-S7 — HIGH fallback probability
- (C-ii) alternative S4 proof routing around Peirce — speculative
- (C-iii) restructure chain to derive Jordan before S4 — UNAVAILABLE (vdW Thm 1 circularity)

**Pause condition:** outcome (C) on any phase → milestone pauses for human decision on whether to restructure, add an explicit assumption, or rewrite. Above GPD's pay grade.

## Primary Requirements

### Phase 54 — §3.3 Peirce Preservation from OUS Primitives (load-bearing)

- [ ] **DERV-54-01**: Circularity audit of GPD v2.0 Phase 4-06 (commit `9608ac54`) corrected-product derivation. Verify whether the formula `a ∘ b = Σᵢ λᵢ C_{pᵢ}(b) + Σ_{i<j} √(λᵢλⱼ) P_{ij}(b)` is derived using only OUS primitives (order unit, compressions, S1, S3, linearity) or silently invokes Jordan structure / EJA / sequential-product formula `f(λ,μ) = √(λμ)` / C*-structure / `h_n(ℂ)`. **Mandatory first task.** If audit fails, (A) via internal prior art is unavailable and milestone shifts to (C-i) per ADDENDUM fallback.
- [ ] **DERV-54-02**: If DERV-54-01 passes, rebuild §3.3 Peirce-preservation proof from the Phase 4-06 formula using only S1, S3, linearity, and A-S compression primitives (idempotency, positivity, `C_p + C_{p'} = id`). Proof must verify both `a ∘ V_2(pᵢ) ⊆ V_2(pᵢ)` and `a ∘ V_1(pᵢ, pⱼ) ⊆ V_1(pᵢ, pⱼ)`. Must NOT use Jordan multiplication, EJA structure, sequential-product formula `√(λμ)`, C*-structure, `h_n(ℂ)`, or any §3.3-downstream result (S4, S5, …).
- [ ] **DERV-54-03**: Produce `derivations/paper5-peirce-preservation/claim.md` restating the §3.3 claim in the derivation's own notation, with explicit statement of allowed primitives (S1, S3, linearity, OUS, compressions) and prohibited tools (Jordan, EJA, `√(λμ)`, C*, `h_n(ℂ)`).
- [ ] **DERV-54-04**: Produce `derivations/paper5-peirce-preservation/attempt-NN.md` for each serious proof attempt (numbered, most recent last). Each attempt file states: inputs used, proof sketch, failure mode if any.
- [ ] **DERV-54-05**: Produce `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md` with specific A-S theorems consulted, page numbers where accessible (ADDENDUM identified Paper 5 cites Thm 9.37 for Peirce direct sum — verify whether this citation is pre-Jordan-legal; ADDENDUM says NO), and what each theorem establishes vs. does NOT establish. This file is a SHARED DELIVERABLE consumed by Phases 55, 57, 58.
- [ ] **DERV-54-06**: If DERV-54-01 or DERV-54-02 fails, produce `derivations/paper5-peirce-preservation/RESULT.md` with outcome (C-i): explicit statement of OUS-level "Peirce coherence" axiom S0, defense of its naturalness, and draft revision text for §3.3 stating and defending it. (C-iii) restructure-before-S4 is explicitly OUT OF SCOPE.
- [ ] **VALD-54-01**: Small-case SymPy sanity check on H_3(ℝ) (3×3 real symmetric matrices): construct `a = Σᵢ λᵢ pᵢ` with two orthogonal rank-1 projectors, compute `a ∘ b` for `b` in each Peirce subspace, verify Peirce invariance numerically. Expected runtime < 1 second.
- [ ] **VALD-54-02**: Adversarial review of Phase 54 RESULT.md by a second fresh-eyes agent before finalization, verifying no prohibited structures were silently used.

### Phase 55 — S4 Facial Structure Lemma

- [ ] **DERV-55-01**: Audit Paper 5's current S4 argument in §3.3-§3.4. Classify whether it uses (i) Alfsen-Shultz compressions only (pre-Jordan, preferred), (ii) Hanche-Olsen facial structure (post-Jordan, circular if invoked before S4 is verified), or (iii) an implicit Jordan appeal.
- [ ] **DERV-55-02**: If (i), promote citation precision using Phase 54's `alfsen-shultz-notes.md` — verify Paper 5's Prop 7.36 / Prop 7.43 citations against the actual A-S chapter (there are TWO A-S volumes: 2001 vol. 179 and 2003 vol. 190 — Paper 5 cites 2003 but compression theory may be in 2001).
- [ ] **DERV-55-03**: If (ii) or (iii), propose Foulis-Holland pre-Jordan alternative or explicit assumption.
- [ ] **DERV-55-04**: Produce revision text for §3.3-§3.4 S4 argument, consistent with Phase 54 outcome. If Phase 54 adopted (C-i) S0, ensure S4 argument uses S0 rather than implicit Peirce appeal.

### Phase 56 — Thm 5.8 Upper Bound (W Carries Product-Form Sequential Product)

- [ ] **DERV-56-01**: Extract the exact "product-form sequential product" identity asserted by Thm 5.8 from `main.tex` (text extraction task; precondition for all Phase 56 work).
- [ ] **DERV-56-02**: Verify that W is a **face** of the ambient EJA (not merely a closed subspace). This is a precondition for invoking Koecher-Vinberg (vdW 2019 Thm 1) to establish product closure.
- [ ] **DERV-56-03**: If W is a face, prove W carries the product-form sequential product by restricting vdW 2019 Thm 1 to W. Provide proof or precise citation.
- [ ] **DERV-56-04**: If W is not a face, characterize the failure and draft revision text acknowledging the gap. Consider Gudder-Greechie 2002 Example 39 (associative non-EJA SEA) as a precedent for "closure without structural preservation."
- [ ] **VALD-56-01**: Small-case SymPy check on smallest nontrivial W: H_3(ℝ) wedge component (3-dim antisymmetric). Compute sequential product restricted to W, verify product-form closure or surface failure mode.

### Phase 57 — Phi Inert-Wrapper Resolution

- [ ] **DERV-57-01**: `grep -n "\\\\phi\\|\\\\Phi" main.tex` to enumerate every occurrence of Phi in Paper 5. Classify each into categories: (a) self-modeling tracking map B→M, (b) inert auxiliary wrapper / ancilla, (c) state-preparation notation, (d) exposition shorthand. Produce `phi-audit.md` as a SHARED DELIVERABLE for Phases 54, 58, 59.
- [ ] **DERV-57-02**: Identify every section where Phi's role shifts between categories without explicit reintroduction. These are the equivocation points.
- [ ] **DERV-57-03**: Decide whether to (a) split notation (Φ for tracking, φ for wrapper, Φ̂ for ancilla, …) or (b) add a standing definition + per-section role qualifier. Defer to author preference; produce both drafts.
- [ ] **DERV-57-04**: Produce revision text for each affected Paper 5 section.

### Phase 58 — Lean Axiom Audit (critical-path bottleneck)

- [ ] **FORM-58-01**: Reconcile the axiom count. Milestone prompt says 16; grep of `~/repos/research/lean/RadicalRelativity/` finds 19 top-level `axiom` declarations (4 in `NonComposability.lean`, 1 in `ObserverInterface.lean`, 13 in `SelfModelingBridge.lean`, 1 in `CStarBridge.lean`). Determine which 16 are Paper-5-relevant by running `#print axioms` on the paper's headline theorems. **Mandatory first task.**
- [ ] **FORM-58-02**: Full axiom inventory — for each of the (confirmed count) Paper-5 axioms: statement, existing docstring citation (some already cite "Alfsen-Shultz 2003, Thm 9.33" etc.), and classification as (i) theorem-in-disguise [should be proved, or an explicit assumption], (ii) definition-as-axiom [should be a `def`], (iii) statement-mismatch [stated form doesn't match cited published theorem], or (iv) genuine primitive [correct].
- [ ] **FORM-58-03**: For each (i)/(ii)/(iii) axiom, propose a fix: prove it, rewrite as definition, or correct the citation. Produce `axiom-audit-table.md` for inclusion in Paper 5 as appendix or supplementary.
- [ ] **FORM-58-04**: Baseline check: `lake exe cache get && lake build` in `~/repos/research/lean/` confirms "0 sorry" baseline before audit begins. If build fails under pinned toolchain, Phase 58 cannot proceed.
- [ ] **FORM-58-05**: Cross-check: reconcile Phase 58 citations against Phase 54's `alfsen-shultz-notes.md` and Phase 57's `phi-audit.md`.

### Phase 59 — Minimal Composite Assumption Defense

- [ ] **DERV-59-01**: Review Paper 5's current minimal-composite defense text against adversarial patterns from published peer review:
  - Hardy 2001 "simplicity" axiom critiques (Masanes-Müller, Chiribella-D'Ariano-Perinotti, Barnum-Wilce all replaced it)
  - Dakić-Brukner 2009 subspace reconstruction
  - Masanes-Müller 2011 continuous reversibility
  - Masanes-Galley-Müller 2019
  - Barnum-Wilce 2014 qubit-subsystem
  - Kent 2024 arXiv:2405.17733 critique pattern
- [ ] **DERV-59-02**: Draft a pre-emptive adversarial defense for each pattern. Do NOT assume any one pattern will be the actual referee response; defend against all.
- [ ] **DERV-59-03**: Install `latexdiff` and `git-latexdiff` (brew prerequisite; latexdiff not currently on this machine) — needed for the final referee-response diff.
- [ ] **DERV-59-04**: Produce revision text for Paper 5's composite-assumption section.

### Milestone-Level Deliverables

- [ ] **DERV-00-01**: Per-phase `RESULT.md` with outcome classification (A) / (B) / (C) and revision text for the affected Paper 5 section. Six RESULT.md files, one per phase.
- [ ] **DERV-00-02**: Consolidated revision-response draft that references every RESULT.md, suitable for inclusion in the eventual JMP referee response letter.
- [ ] **VALD-00-01**: Full `latexdiff` against frozen `paper5-jmp-submitted` tag showing all revisions, committed as `paper5-revisions.pdf` artifact.

## Follow-up Requirements

### Deferred to Future Milestones (v15.0+)

- **FUTR-01**: Close gap G6 (so(6) → G_SM) via Todorov-Drenska F_4-Spin(9) intersection mechanism — from v13.0 follow-up
- **FUTR-02**: Close gap G7 (3 generations) via Boyle triality mechanism — from v13.0 follow-up
- **FUTR-03**: If Phase 54 lands (C-i) with new axiom S0, reconsider whether the N=2/GR chain (v13.0) imports S0 anywhere — may require a Paper 7 erratum depending on where S0 propagates.

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| Using Jordan multiplication / EJA / C*-structure / sequential-product formula `√(λμ)` in Phase 54 proof | Would invert the derivation chain; vdW Thm 1 consumes S4 to produce Jordan |
| Using `h_n(ℂ)` or specific EJA realization in Phase 54 proof | Circular with respect to §3.3's pre-Jordan status |
| Anything downstream of §3.3 (S4, S5, sequential product formula, …) in Phase 54 proof | Same pre-Jordan discipline |
| Revisiting Paper 6 / Paper 7 / v13.0 results | This milestone is Paper 5 maintenance only; derivation chain is complete as of v13.0 |
| New derivation-chain extensions (so(6)→G_SM, 3 generations, Λ≠0) | Deferred to v15.0+ |
| (C-iii) restructure Paper 5 chain to derive Jordan before S4 | Explicitly UNAVAILABLE per ADDENDUM: vdW Thm 1 circularity |
| Major restructuring of Paper 5 without human approval | Any outcome (C) pauses milestone for above-pay-grade decision |
| "Bryan's intuition says X" shortcuts | Milestone exists precisely because intuition is insufficient |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| DERV-54-01 (Phase 4-06 circularity) | Binary pass/fail; every step traced to an allowed primitive or flagged | Symbol-level audit; grep for forbidden tokens (Jordan, EJA, `sqrt(lambda`, `h_n(C)`) |
| DERV-54-02 (§3.3 proof) | Complete proof, every step cites an allowed primitive; no Jordan appeals | Adversarial review by second fresh-eyes agent (VALD-54-02) |
| DERV-54-05 (A-S notes) | Chapter + section + theorem number for each citation; explicit distinction between A-S 2001 and 2003 volumes | Cross-check against Springer TOC or library copy; flag any unverified prop numbers |
| VALD-54-01 (SymPy sanity) | H_3(ℝ) numerical verification passes; < 1 sec runtime | `python -c "…"` assertion |
| FORM-58-01 (axiom count) | Count reconciled; each of N axioms classified (i)/(ii)/(iii)/(iv) | `#print axioms` on headline theorems; grep for `^axiom ` |
| FORM-58-02 (axiom-to-citation) | Every axiom has (stated form, cited theorem, type classification) | Docstring cross-check against `alfsen-shultz-notes.md` |
| DERV-57-01 (Phi grep) | Every Phi occurrence classified (a)/(b)/(c)/(d) | `grep -cn` count reconciled with audit table |
| DERV-59-01 (composite defense) | Adversarial patterns from 6 published reviews all addressed | Per-pattern checklist; each has a drafted response |
| VALD-00-01 (final diff) | `latexdiff` clean output; all revisions visible | `git diff paper5-jmp-submitted` + `latexdiff` PDF |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| DERV-54-01 | Pass/fail audit verdict with token-level trace | GPD v2.0 Phase 4-06 commit `9608ac54` | Paper 5 §3.3; v2.0 Phase 4 STATE | "Looks OK" without grep trace; silent Jordan import |
| DERV-54-02 | §3.3 proof using only OUS primitives | A-S compressions Ch. 7 (2001 or 2003 vol. — verify); vdW S1, S3 | Phase 4-06 corrected-product formula; Phase 54 `claim.md` | Citing A-S Peirce decomposition theorem as if it proves `L_a` invariance (Pitfall R2); citing A-S Thm 9.37 at pre-Jordan level (ADDENDUM Pitfall) |
| DERV-54-05 | `alfsen-shultz-notes.md` shared artifact | A-S 2001 vol. 179 + A-S 2003 vol. 190 | ADDENDUM TOC findings | Collapsing the two A-S volumes into one citation |
| DERV-54-06 (if triggered) | RESULT.md with (C-i) S0 axiom draft + §3.3 revision text | ADDENDUM fallback recommendation | §3.3 current text | Silently shifting to (C-iii) |
| DERV-55-01 | S4 argument classified (i)/(ii)/(iii) | Foulis-Holland; Hanche-Olsen §2.6 | Paper 5 §3.3-§3.4 | Invoking Hanche-Olsen facial argument before S4 is verified (pre-Jordan circularity) |
| DERV-56-02 | W-face verification | vdW 2019 Thm 1 face restriction | Paper 5 §5 Thm 5.8 text | Asserting W-closure without face check (Pitfall R7) |
| DERV-57-01 | `phi-audit.md` shared artifact | `main.tex` grep output | Paper 5 all sections | Fixing one occurrence without checking all |
| FORM-58-01 | Axiom-count reconciliation (16 vs 19) | `#print axioms` on headline theorems | `~/repos/research/lean/RadicalRelativity/` | Classifying without running `#print axioms` |
| FORM-58-02 | Axiom audit table with (i)/(ii)/(iii)/(iv) classification per axiom | A-S 2001/2003 + vdW 2019 | Existing docstring citations (some exist) | Accepting docstring citation without verification |
| DERV-59-01 | Adversarial defense draft vs. 6 published patterns | Hardy, Masanes-Müller, Chiribella-D'Ariano-Perinotti, Barnum-Wilce, Kent 2024 | Paper 5 composite-assumption section | Defending against only one pattern |

## Traceability

Which phases cover which requirements. Populated by roadmap.

| Requirement | Phase | Status |
| ----------- | ----- | ------ |
| DERV-54-01 | 54 | Pending |
| DERV-54-02 | 54 | Pending |
| DERV-54-03 | 54 | Pending |
| DERV-54-04 | 54 | Pending |
| DERV-54-05 | 54 | Pending |
| DERV-54-06 | 54 | Pending (conditional on DERV-54-01 or DERV-54-02 failure) |
| VALD-54-01 | 54 | Pending |
| VALD-54-02 | 54 | Pending |
| DERV-55-01 | 55 | Pending |
| DERV-55-02 | 55 | Pending |
| DERV-55-03 | 55 | Pending |
| DERV-55-04 | 55 | Pending |
| DERV-56-01 | 56 | Pending |
| DERV-56-02 | 56 | Pending |
| DERV-56-03 | 56 | Pending |
| DERV-56-04 | 56 | Pending (conditional on DERV-56-02 failure) |
| VALD-56-01 | 56 | Pending |
| DERV-57-01 | 57 | Pending |
| DERV-57-02 | 57 | Pending |
| DERV-57-03 | 57 | Pending |
| DERV-57-04 | 57 | Pending |
| FORM-58-01 | 58 | Pending |
| FORM-58-02 | 58 | Pending |
| FORM-58-03 | 58 | Pending |
| FORM-58-04 | 58 | Pending |
| FORM-58-05 | 58 | Pending |
| DERV-59-01 | 59 | Pending |
| DERV-59-02 | 59 | Pending |
| DERV-59-03 | 59 | Pending |
| DERV-59-04 | 59 | Pending |
| DERV-00-01 | 54-59 | Pending (one per phase) |
| DERV-00-02 | 59 | Pending |
| VALD-00-01 | 59 | Pending |

**Coverage:**

- Primary requirements: 32 total
- Mapped to phases: 32 (Phase 54: 8, Phase 55: 4, Phase 56: 5, Phase 57: 4, Phase 58: 5, Phase 59: 4, Milestone-level: 3 post-59)
- Unmapped: 0

---

_Requirements defined: 2026-04-16_
_Last updated: 2026-04-16 after v14.0 milestone initialization_
