# Attempt Log — Phase 54 Plan 54-02 Peirce-Preservation (A) Attempts

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 02 (Wave 2, (A) attempt cycle)
**Purpose:** Chronological record of all (A) proof attempts on the Peirce-Preservation Lemma (claim.md), with per-attempt verdict, early-gate results, adversarial-review verdict, status, failure mode (if applicable), and final plan outcome tag.

**Routing precondition (from Plan 54-01 Task 2, recorded in audit-04-06.md §7):** `option-b-fails-compression`. Plan 54-02 attempt-01 is therefore compression-combinatorics (Approach 2 per 54-RESEARCH.md §Standard Approaches), NOT seeded from Eq. (04-06.4) (which AUDIT-FAILS).

---

## Attempts Ledger

| # | Seed strategy | Gate (a) forbidden-token grep | Gate (b) SymPy rank-1 | Gate (c) model-instantiation | Adversarial review | Status | Failure mode (verbatim if FAILED) |
|---|---|---|---|---|---|---|---|
| 01 | Approach 2 (compression combinatorics, non-4-06 seed). Only (A) approach available under option-b-fails-compression. | PASS: all hits confined to (a) Forbidden Tokens declaration header, (b) Drift Log (rejected temptations), (c) Model-Instantiation sanity check with explicit "NOT proof device" labeling, (d) Status/Verdict citing forbidden bridge candidates as REJECTED. Zero hits in proof body. | PASS: H_3(ℝ), two orthogonal rank-1 projectors p_1, p_2; Prop 3.1 (V_2) verified; Prop 3.2 (V_1(p_1,p_2)) verified; bonus Prop 3.3 cross-term (a = λ_3 p_3, b ∈ V_1(p_1, p_2)) verified (trivially yields 0, which is in V_1). Lemma statement TRUE in H_3(ℝ). | Performed in attempt-01.md §Model-Instantiation. Lemma holds in M_n(ℂ)^sa (Jordan theorem), C(X) (trivially; Peirce decomp collapses), spin factors (Clifford anti-commutation). No proof to instantiate since argument did not close; verified target claim is consistent with canonical models. | NOT INVOKED — attempt-01 self-reported structural-insufficiency before reaching adversarial-review stage; adversarial review is invoked only for attempts that close the proof at the (A) tool-set level. Spending review budget on a known-incomplete argument would be wasteful per CONTEXT.md adversarial-review discipline. | FAILED | The (A) allowed-tool set `{S1, S3, linearity in 2nd arg, A-S compression axioms}` is insufficient to prove Proposition 3.3 (`a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` for `{k,l} ∩ supp(a) = ∅`). The required bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0` is not derivable from these axioms without either (i) first-argument additivity/scalar-homogeneity of `∘` (which is S2, forbidden), (ii) associativity of `∘` (not an OUS primitive; derives post-vdW-Thm-1 post-S4), or (iii) a compression-module structure on `L_a` (which is essentially the invariance claim itself, i.e., circular). Propositions 3.1 and 3.2 reduce to the same structural gap, either directly or via a cyclic dependency between them. The lemma is TRUE in the canonical models (`M_n(ℂ)^sa`, `C(X)`, spin factors) — the failure is tool-insufficiency, not false-claim. |

---

## Task 2 Checkpoint — Status Before User Decision

**Executor has paused at the Task 2 `checkpoint:human-verify` gate per the plan's interactive contract and per CONTEXT.md stop/rethink #2 (4-06 audit FAIL trigger, here propagated as the single-non-4-06-attempt failure). Awaiting user decision.**

### Attempt-01 status

- **Verdict:** FAILED — structural insufficiency of (A) tool set.
- **Gate (a):** PASS (forbidden-token grep clean modulo legal declarations/drift-log).
- **Gate (b):** PASS (SymPy rank-1 on H_3(ℝ) confirms lemma is TRUE).
- **Gate (c):** PASS (lemma consistent across M_n(ℂ)^sa, C(X), spin factors).
- **Adversarial review:** NOT INVOKED (early-gate failure resolution: the structural gap was identified inside the attempt itself without needing adversarial probe; no argument exists to review).

### Options for user decision (Task 2 resume-signal menu)

| Resume signal | When appropriate | Next action |
|---|---|---|
| `attempt-01-CLOSURE-accept` | INAPPLICABLE: attempt-01 FAILED, not CLOSURE. Do not select. | n/a |
| `authorize-attempt-02` | If user believes another structural strategy could close (A). However, the two allowed (A) approaches are BOTH now closed: Approach 1 (4-06 seed) by audit-04-06 AUDIT-FAILS; Approach 2 (compression combinatorics) by the present attempt-01 structural gap. No genuinely new (A) structural strategy is apparent. | Draft attempt-02.md with verbatim attempt-01 objection carried forward. Execute Task 3 of 54-02-PLAN.md. |
| `pivot-to-C-i-now` | **RECOMMENDED.** The convergent structural gap — all three sub-proofs block on the same bridge, which is precisely the form of a missing compression-module axiom — is the canonical (C-i) signal. Pivot to Plan 54-03 (C-i) with attempt-01's verbatim failure statement as direct input to the S0 defense. | Write final outcome tag `PIVOT-TO-C-I` in this log (see §Outcome Tag below, draft-only until user confirms). Advance to Plan 54-03 (wave 3); skip Tasks 3-5 of this plan. |

### Recommendation

**PIVOT-TO-C-I** is strongly motivated:

1. The failure mode is convergent: three independent sub-proofs (Propositions 3.1, 3.2, 3.3) ALL reduce to the same missing bridge.
2. The missing bridge is structurally a compression-module / commutation property — which is EXACTLY the candidate S0 axiom form documented in claim.md Section 4.6 and 54-RESEARCH.md §Approach 3.
3. Both (A) approaches (Approach 1 = 4-06 seed, Approach 2 = compression combinatorics) are closed: 4-06 route by audit AUDIT-FAILS, compression-combinatorics route by the present structural gap. There is no third (A) route inside the allowed-tool set.
4. Attempting an attempt-02 with "another (A) strategy" would require re-opening either the 4-06 audit (not possible without new evidence) or finding a structural route not in the allowed-tool set (which by hypothesis does not exist).
5. Per CONTEXT.md budget discipline: *"Just be reasonable … we probably won't let it get that far though."* The attempt cap is an OUTER bound; converging evidence after attempt-01 for PIVOT-TO-C-I is the prescribed response.

**Uncertainty flag for user:** If user believes there is a specific (A) structural strategy not yet explored (e.g., leveraging a specific A-S 2001 Ch. 7-8 Prop/Thm that the executor is not aware of because of the alfsen-shultz-notes.md VERIFICATION-DEFERRED status, or a hybrid decomposition strategy), that could motivate authorizing attempt-02. But the executor does not identify such a strategy within the allowed-tool set as currently characterized.

---

## Outcome Tag (SEALED 2026-04-16; user-confirmed `pivot-to-C-i-now` at Task 2 checkpoint)

```
outcome: PIVOT-TO-C-I
reason: attempt-01 FAILED (structural insufficiency of (A) tool set at bridge C_{p_k}(a)=0 ⟹ C_{p_k}(a∘b)=0);
        no further (A) route available (Approach 1 closed by audit-04-06 AUDIT-FAILS;
        Approach 2 closed by attempt-01 structural gap).
carry-forward to Plan 54-03 (C-i):
  attempt-01 verbatim failure: "The (A) allowed-tool set {S1, S3, linearity in 2nd arg, A-S compression axioms}
  is insufficient to prove Proposition 3.3 (a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l) for {k,l} ∩ supp(a) = ∅). The
  required bridge C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0 is not derivable from these axioms without either
  (i) first-argument additivity/scalar-homogeneity of ∘ (which is S2, forbidden), (ii) associativity of ∘
  (not an OUS primitive; derives post-vdW-Thm-1 post-S4), or (iii) a compression-module structure on L_a
  (which is essentially the invariance claim itself, i.e., circular). Propositions 3.1 and 3.2 reduce to
  the same structural gap. The lemma is TRUE in the canonical models (M_n(ℂ)^sa, C(X), spin factors) —
  the failure is tool-insufficiency, not false-claim."
  S0 candidate pointer: the missing bridge IS the compression-module / commutation property, which maps
  directly to the claim.md Section 4.6 candidate S0 statement "{C_{p_i}} pairwise commute and C_{p_i}C_{p_j}=0
  for i≠j" (this gives the commutation piece; additional compression-L_a interaction may be needed in the
  S0 final form — Plan 54-03 to determine).
```

**Status:** SEALED. Plan 54-03 (wave 3) branches to (C-i). Tasks 3-5 of Plan 54-02 (attempt-02, attempt-03) SKIPPED per the user's `pivot-to-C-i-now` resume signal — convergent structural gap across all three sub-proofs + both (A) approaches closed (4-06 audit-FAILS, compression-combinatorics tool-insufficient) make further (A) attempts low-value.

---

## Schema

- Each executed attempt adds one row to the Attempts Ledger table above.
- Verbatim adversarial objections (if any) are preserved in the row's last column; no paraphrase.
- The final outcome tag line is emitted EXACTLY ONCE, at plan close, in the form `outcome: (A) via attempt-NN` OR `outcome: PIVOT-TO-C-I` (no composite or ambiguous tags).
- Carry-forward block (verbatim objections for Plan 54-03 S0-defense input) is populated iff outcome = `PIVOT-TO-C-I`.

---

_Last updated: 2026-04-16 — attempt-01 sealed, awaiting Task 2 user decision._
