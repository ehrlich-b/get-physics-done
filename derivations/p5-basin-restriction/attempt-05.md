<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Attempt log (DERV-00-01, Phase 63 slice). Provenance: LIVE papers only (~/repos/blog/landing/papers/). -->

# Attempt 05 — Phase 63 verdict assembly: assembling the (O) ambient-transport obstruction into the milestone coexistence-as-island RESTRICTION verdict

**Plan:** 63-01 (Phase 63, milestone v15.0) — DERV-00-01 slice (continuing attempt-01, attempt-02, attempt-03, attempt-04)
**Date:** 2026-05-24
**Step attacked:** Step 4 of 4 — the **milestone verdict**. Assemble `RESULT.md` (the milestone
deliverable) from the **settled** Phase 62 outcome — verdict **(O) AMBIENT-TRANSPORT
OBSTRUCTION** — and complete the attempt-log audit.
**Goal:** Read the Phase 62 coherent-embedding step's (O) verdict into the milestone-level
`RESTRICTION` verdict as a **REFINEMENT** to **coexistence-as-island** (the through-line
survives); restate every exact number **verbatim** (no re-computation); reconcile the stale
requirement phrasing against the corrected authority. The **one-sentence verdict line**
(DERV-00-02) and the **finalization** (removing the DRAFT marker) are deliberately **LEFT to
63-02**, which runs the fresh-eyes adversarial guard review **before** finalization (ROADMAP
Success Criterion 2).

> **This attempt does NOT recompute anything.** The decisive computation (Phase 62, VALD-62-01:
> exact SymPy, assert-based harness, NO pytest) is **DONE** and verified (verifier 14/14 contract
> targets + 11/11 physics checks independently re-derived; consistency CONSISTENT; human sign-off
> APPROVED at the 62-03 interactive checkpoint, 2026-05-24). This is a **synthesis/assembly**
> attempt.

---

## Coverage audit (attempt-01..04)

Audited against the derivation-tree `STATE.md` four-step table. Every serious proof/obstruction
attempt across Phases 60–62 has a log entry; the numbering is contiguous.

| Attempt | Plan | Step / Phase | Subject (verified from the file's own header) | Outcome |
|---|---|---|---|---|
| `attempt-01.md` | 60-01 | Step 1 / Phase 60 | two-composites distinction (does the observer's clause-(iii) `V_BM` differ, non-circularly, from `h_3(O)`'s BGW non-composability?) | distinction **EARNED**; no collapse, no PAUSE |
| `attempt-02.md` | 60-02 | Step 1 / Phase 60 | `rem:converse` grounded against BGW 2020 | **CONFIRMED-WITH-CAVEAT** (minimal `≠` maximal; minimal is a direct summand; clause (iii) auto-satisfied as written) |
| `attempt-03.md` | 61-01 | Step 2 / Phase 61 | slice `A = M_3(C)^sa` satisfies Paper 5 Def 1 (i)–(iv) **intrinsically** | honest **POSITIVE** (intrinsic); induced-by-`E` deferred to Phase 62 |
| `attempt-04.md` | 62-03 | Step 3 / Phase 62 | coherent embedding under `E` (ambient-transport decisive; slice-internal trivial control) | verdict **(O) AMBIENT-TRANSPORT OBSTRUCTION** (refines `RESTRICTION` to coexistence-as-island) |

**Conclusion: COMPLETE COVERAGE across Phases 60–62.** No serious attempt is missing a log entry.
The four-step table's Steps 1–3 each have their attempt(s) recorded (Step 1 spans plans 60-01 and
60-02, hence two entries; Steps 2 and 3 one each). `attempt-05.md` (this file) is the new **Phase
63** entry for the verdict assembly (Step 4); the numbering is **01..05**, contiguous. No gap was
found, so none is recorded (no fabricated "attempt" is padded in — `fp-attempt-fabricate`
rejected).

---

## Inputs used

All inputs are **LIVE / local** artifacts. The executor has **no web**; every input is read from
the working tree or the LIVE papers directory.

| Input | Source (LIVE / repo) | Used for |
|---|---|---|
| The exact (O) computation + verdict + characterization | `derivations/p5-basin-restriction/embedding-under-E.md` §4 (62-02, VALD-62-01) and §5 (62-03, the verdict read-off + coexistence-as-island interpretation) | the EXACT numbers restated verbatim in `RESULT.md` (`‖R‖² = 38593/72`; `R_{11} = -2`; associator `524/9`; `‖E(X∘X)−(EX)∘(EX)‖² = 3797527/34560000`; positional Peirce grades `4`, `1033/18`, `3797/8`; the `C_u`/`(e_1…e_6)` split; the non-Hermiticity finding; the §3.6 fork; §3.7/§5.2 governing frame; §5.O.1 obstruction characterization; §5.O.1(c) minimal extra input) |
| The corrected `RESTRICTION` claim + verdict semantics + forbidden moves | `derivations/p5-basin-restriction/claim.md` (DERV-60-04, updated 62-03) | the CORRECTED embedding clause (coexistence-as-island); the CORRECTED verdict semantics (obstruction REFINES, NOT independent posits); the CORRECTED PAUSE condition 2 (ambient-transport obstruction = expected deliverable, not a collapse); clause (iii) integrity guard (verbatim); `fp-conflate-composites`; the EXTENDED `fp-force-positive` (both directions) |
| The effective Phase 63 contract (supersedes the stale phrasing) | `.gpd/ROADMAP.md` Phase 63 entry (FRAMING NOTE + Contract Coverage + Success Criteria) | the authoritative reconciliation: the stale "independent posits / two unconnected foundations / program collapse" phrasing in Success Criterion 3 / DERV-00-02 / DERV-63-01 is SUPERSEDED by coexistence-as-island; Success Criterion 2 (the adversarial review must PRECEDE finalization) → defer the verdict line + finalization to 63-02 |
| The human-approved verdict read-off + numbers (benchmark) | `.gpd/phases/62-coherent-embedding-under-e-the-hard-part/62-03-SUMMARY.md` (human approved 2026-05-24) | cross-check that every number restated in `RESULT.md` matches the verified, human-approved Phase 62 record exactly (Eq. (62.9)–(62.12); Key Results; Self-Check numbers) |
| The four-step coverage map | `derivations/p5-basin-restriction/STATE.md` (derivation-tree) | the four-step attack table; which attempt log covers which plan (attempt-01 = 60-01, attempt-02 = 60-02, attempt-03 = 61-01, attempt-04 = 62-03) — the coverage-audit basis |
| The attempt-log structure convention | `derivations/p5-basin-restriction/attempt-04.md` (DERV-00-01) | the header / section convention this file continues (Inputs used / Argument / Outcome / Failure modes / Prohibited moves NOT used / Deliverables); the numbering sequence (01..04 → 05) |
| Paper 5 clause (iii) (`sms:minimal`), verbatim | `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` lines 351–353 | confirm the decisive SP datum is the ACTUAL product-form `√a b √a` and that clause (iii) is restated unchanged (only `RESTRICTION`'s embedding clause is weakened) |

**Independent re-confirmation this plan (executed):**
- Peirce-grade self-check re-verified exactly (Python `fractions.Fraction`):
  `4 + 1033/18 + 3797/8 = 288/72 + 4132/72 + 34173/72 = 38593/72 = ‖R‖_F²`. **PASS.**
- Rank bookkeeping re-verified: `27 = 9 + 18`; slice Peirce `9 = 1 + 4 + 4`. **PASS.**
- Cross-artifact number consistency confirmed: `embedding-under-E.md` §4/§5 ↔ `62-03-SUMMARY.md`
  (Eq. (62.9)–(62.12)) ↔ `RESULT.md` Numbers ledger — all identical.
- (The decisive harness `python tests/test_embedding_under_E.py` was re-run and re-confirmed
  exit 0 / verdict (O) during 62-03; this synthesis plan restates that settled outcome and does
  not re-run it as part of the assembly.)

---

## Argument

This attempt **ASSEMBLES** (does **not** recompute) the settled Phase 62 verdict into the
milestone-level `RESULT.md`:

1. **Recap the four-step attack** and locate this file as Step 4 (the verdict), with Steps 1–3
   (Phases 60–62) as completed inputs.

2. **State the corrected governing frame BEFORE the verdict** (`embedding-under-E.md` §5.2;
   `claim.md` CORRECTED embedding clause): `RESTRICTION` needs **only** coexistence-as-island —
   the observer self-models on the slice `A = h_3(C_u)` (Phase 61, all four Def 1 clauses
   verbatim, intrinsically), and the slice sits inside `h_3(O)` as `range E`. `E` is the
   **access/projection map**, **not** required to be a Jordan/SP morphism on the ambient. Whether
   `E` transports the SP from the ambient is a **stronger, NOT-required** property. The stale
   "independent posits / two unconnected foundations / program collapse" phrasing (Success
   Criterion 3 / DERV-00-02 / DERV-63-01) is **SUPERSEDED** (ROADMAP FRAMING NOTE; `claim.md`;
   `embedding-under-E.md` §5.2/§5.O.2; Bryan 2026-05-24).

3. **Read off the DECISIVE verdict (O)** exactly as computed (not forced): the ambient-transport
   residual `R = E(√X Y √X) − √(EX)(EY)√(EX)` is **EXACTLY nonzero** (`is_zero_exact = [False,
   False]`) for two distinct generic ambient `(X, Y)`; `‖R‖_F² = 38593/72`, `R_{11} = -2` (clean
   pair). Branch (O) of the §3.6 fork.

4. **Show the verdict TOUCHES the non-associative structure** (anti-reward-hack): the associator
   `‖(√X Y)√X − √X(Y√X)‖² = 524/9 ≠ 0` is load-bearing on the **same** decisive triple; `E` is not
   even a Jordan morphism on the ambient (`‖E(X∘X)−(EX)∘(EX)‖² = 3797527/34560000 ≠ 0`); the
   slice-internal case is named the **trivial control** (leakage 0, associator 0), and the
   verifier's slice-confined `R = 0` control proves the test genuinely CAN yield (P) — so (O) is
   not rigged.

5. **Characterize the obstruction precisely**: the product-form SP datum `E` cannot transport; the
   defect lives **inside `A`** (`C_u` directions `e_0, e_7`; `(e_1…e_6)`-part `= 0`), spread across
   all three positional `E_11` Peirce grades (`‖V_1‖² = 4`, `‖V_{1/2}‖² = 1033/18`, `‖V_0‖² =
   3797/8`, summing to `38593/72` — the pure-algebra dimensional-analysis self-check); the
   mechanism (the ambient triple product populates `(e_1…e_6)`-content `E` then projects away); the
   ambient SP non-Hermitian (sharpening).

6. **State the program consequence — coexistence-as-island** (`embedding-under-E.md` §5.O.2): the
   observer is a self-contained C\* island; the through-line **SURVIVES** as the island
   through-line (`h_3(O)` is the basin whose maximal C\* slice is `M_3(C)^sa`, on which Paper 5
   certifies QM; `E` = access/projection map). (O) does **NOT** establish independent posits and is
   **NOT** a collapse; it **REFINES** the claim. Consistent with U-B-M (Peirce `≠` tensor; the
   basin fixes the TYPE, not the composite; `V_BM = A ⊗ A` is the observer's own composite, not the
   ambient — `fp-conflate-composites` preserved).

7. **State what would close the obstruction** (the stronger, not-required ambient transport): an
   external datum on `h_3(O)` not in `range E` (Hanche-Olsen induced-vs-imported) — flagged as the
   **weakest anchor**, stated as precisely as the evidence allows, not inflated; coexistence-as-
   island does **not** require it.

8. **Defer the verdict line + finalization to 63-02** (after the adversarial guard review;
   Success Criterion 2). `RESULT.md` is marked **DRAFT** throughout.

A **Numbers ledger** is included in `RESULT.md` listing every exact number with its source section,
so the 63-02 reviewer and the verifier can cross-check transcription. The reconciliation of the
stale requirement texts against the corrected authority is stated explicitly (the stale phrasing
appears only as negated / marked-superseded quotation).

---

## Outcome

**DRAFT `RESULT.md` assembled (Task 1).** The milestone-level `RESTRICTION` verdict is the **(O)
AMBIENT-TRANSPORT OBSTRUCTION**, read off the verified Phase 62 computation and interpreted as a
**REFINEMENT to coexistence-as-island**: the observer is a self-contained C\* island, and the
through-line **SURVIVES** (basin `h_3(O)` → maximal C\* slice `M_3(C)^sa` → Paper 5 certifies QM;
`E` = access/projection map). Every exact number is restated **verbatim** from
`embedding-under-E.md` §4/§5 (cross-checked against `62-03-SUMMARY.md`); the Peirce-grade self-check
`4 + 1033/18 + 3797/8 = 38593/72` holds exactly. Clause (iii) is **unchanged** (only the embedding
clause weakened); `V_BM` is **not** conflated with the ambient.

**No PAUSE** (corrected PAUSE condition 2: an ambient-transport obstruction is the **expected**
deliverable, not a backtracking trigger). The genuinely-unexpected-pathology triggers did **not**
fire (the slice-internal control is trivial as expected — leakage 0, associator 0; the slice is a
closed associative subalgebra; the two-composites distinction stands).

**The one-sentence milestone verdict LINE (DERV-00-02) and the finalization (removing the DRAFT
marker) are LEFT to 63-02**, after the fresh-eyes adversarial guard review of the three
reward-hacking guards (clause (iii) not redefined; the two composites not conflated; preservation
not asserted without demonstration on `h_3(O)`). This respects ROADMAP Success Criterion 2 (the
review must **precede** finalization). The milestone verdict is therefore **NOT** declared finalized
here (`fp-overclaim-milestone`).

---

## Failure modes / what remains open

- **The adversarial fresh-eyes review (63-02) is still pending.** It could in principle find a
  guard violation (a backtracking trigger). This is a contingency, not expected — the three guards
  were honored throughout Phase 62 (the decisive test was the **ambient** residual on generic
  `X, Y` with non-associativity load-bearing; clause (iii) verbatim; `V_BM` not conflated) — but
  the review is the gate, and finalization waits on it.
- **The Hanche-Olsen minimal extra input is the WEAKEST ANCHOR.** The precise external datum on
  `h_3(O)` (not in `range E`) that ambient transport would need is the least-certain part; stated
  as precisely as the evidence allows, flagged for 63-02 / future work, **NOT** overstated.
  **Coexistence-as-island does not require it** (the observer self-models on the slice, Phase 61).
- **The milestone verdict LINE is not yet written** (deferred to 63-02; this is by design, not an
  omission).
- **Generality caveat (inherited from §4.6/§5.5):** one exact nonzero residual on
  non-associativity-load-bearing generic data **suffices** to establish (O); we have two. The
  complementary "no generic `X, Y` ever gives `R = 0`" is **not** needed for (O) and is **not**
  claimed.
- **`rem:converse` provenance:** still prompt-inline / not-in-live-paper (FUTR-01), confirmed
  against BGW in Phase 60; not load-bearing for this attempt.

---

## Prohibited reward-hacking moves — explicitly NOT used

- **`fp-force-positive`** — REJECTED (both directions). The verdict (O) equals the exact Phase 62
  computation: **not** forced to (P) (no positive theorem manufactured; the exact `R ≠ 0` result
  not relaxed), and **not** over-stated as a refutation/collapse — reported as the **expected**
  coexistence-as-island refinement.
- **`fp-overstate-obstruction`** — REJECTED. The stale "independent posits / two unconnected
  foundations / program collapse" phrasing is used in `RESULT.md` **only** as explicitly-negated or
  marked-superseded quotation; the (O) consequence is framed as a REFINEMENT, and the through-line
  is stated to **SURVIVE**.
- **`fp-vague-verdict`** — REJECTED. `RESULT.md` commits to a single DECISIVE branch (O); no
  "mostly works" / "broadly preserved" / "largely consistent" hedging describes the verdict.
- **`fp-not-touch-nonassociative`** — REJECTED. The verdict is grounded in the genuinely
  non-associative `h_3(O)` (associator `= 524/9 ≠ 0` load-bearing on the **same** generic `X, Y`;
  defect in `C_u` / positional `E_11` Peirce grades), **not** the trivial slice-internal control.
- **`fp-redefine-iii-result` / `fp-conflate-composites`** — REJECTED. Clause (iii) is restated
  **unchanged** (only `RESTRICTION`'s embedding clause weakened); `V_BM = A ⊗ A ≅ M_9(C)^sa` is the
  observer's OWN composite, never identified with / conflated with the BGW universe-tensoring `⊠̃`
  of `h_3(O)`. The clause-(iii) integrity guard and the `V_BM` distinction are preserved.
- **`fp-attempt-fabricate`** — REJECTED. The coverage audit was done against the actual
  `attempt-01..04` files and the four-step `STATE.md` table; no missing attempt was found, so none
  was fabricated, and `attempt-05` records a genuinely-made (synthesis) attempt — not a checkbox.
- **`fp-overclaim-milestone`** — REJECTED. The verdict LINE (DERV-00-02) and finalization are
  deferred to 63-02 (after the adversarial review); the milestone verdict is left UNDECIDED here.

---

## Deliverables this attempt

- `derivations/p5-basin-restriction/RESULT.md` — **DRAFT** (Task 1): the (O) ambient-transport
  obstruction verdict refining `RESTRICTION` to coexistence-as-island, with the precise obstruction
  characterization (exact Phase 62 numbers; Peirce-grade self-check passing), the program
  consequence (through-line survives), the close-the-obstruction note (Hanche-Olsen minimal extra
  input, flagged as the weakest anchor), the Numbers ledger, the type/Peirce self-audit, and the
  explicit deferral of the verdict line + finalization to 63-02. **DRAFT marker present.**
- `derivations/p5-basin-restriction/attempt-05.md` — **this file** (DERV-00-01; continuing
  attempt-01..04).
- **To follow in 63-02:** the one-sentence milestone verdict LINE (DERV-00-02), the finalization
  (remove the DRAFT marker), and the adversarial fresh-eyes guard review (Success Criterion 2).
- **NOT modified this plan:** `embedding-under-E.md`, `claim.md`, `STATE.md`, `two-composites.md`,
  `rem-converse-bgw.md`, `slice-clause-iii.md`, and the `code/`+`tests/` harness — all are inputs
  to this synthesis, restated, not re-derived or edited.

---

_Plan: 63-01 (Phase 63, milestone v15.0) — DERV-00-01 slice. Continues attempt-01..04._
_Synthesis/assembly attempt: assembles the settled Phase 62 verdict (O) into the milestone
coexistence-as-island `RESTRICTION` verdict; verdict LINE + finalization deferred to 63-02 (ROADMAP
Success Criterion 2)._
