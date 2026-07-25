# Paper 5 — The Diachronic-Faithfulness Narrowness Theorem (is "self-history transparency does not vanish" already ⟺ complex, over EVERY Euclidean Jordan algebra — and is it strictly weaker than full local tomography?)

## TASK TYPE
Prove or DISPROVE one crisp claim, exact/ℚ where the algebra allows, with a PRE-DECLARED decision
tree. This is a NARROWNESS / weakest-axiom computation, NOT a forcing attempt. Read HONEST FRAME before
deciding the result moves anything.

## HONEST FRAME (read first — do NOT overclaim)
- The **complex-axis forcing question is CLOSED** (commit `e42bb84`, §13): `M_n(ℝ)ˢᵃ ⊨ Definition 1` as a
  finite, faithful, consistent self-model ⇒ self-modeling does NOT force complex. The rebit is a
  self-model, full stop. This probe does NOT reopen that and CANNOT produce a forcing.
- What this probe sharpens is the **selecting axiom's reach**. Paper 5 selects ℂ from {ℝ,ℂ,ℍ} via an
  import. We are renaming/recasting that import as **diachronic faithfulness** across **self-model time**
  (the parameter τ whose ticks are the test → test′ → test″ chain; the faithful k-tick record of the
  history is the k-fold self-composite). The three-matrix-field result is ALREADY computed exactly
  (finding D, below). This probe asks the ALL-EJA + STRICTLY-WEAKER questions, which decide whether the
  diachronic axiom is a genuine self-native axiom or merely **local tomography reglossed** (the live
  referee objection).
- Best realistic outcome = a clean weakest-axiom theorem ("self-tower transparency ↛ 0 ⟺ ℂ among all
  EJAs, and this is formally weaker than full LT"). Worst-for-the-hinge = a **bounded intruder** (a
  non-ℂ EJA whose self-tower transparency stays bounded away from 0), which would mean diachronic
  faithfulness does NOT pin ℂ and the paper must fall back to full LT. Either is publishable as an
  honest characterization result; only the intruder is news for Bryan.

## DEFINITIONS — STATE THESE PRECISELY BEFORE ANY NUMERICS
Let `V` be a finite-dimensional simple Euclidean Jordan algebra (the self-model). `dim V` = its real
vector-space dimension (= the number of real effect parameters).
- **Self-history tower.** After `k` ticks of self-model time the faithful record of the whole history
  test, test′, …, test⁽ᵏ⁾ is a state on the `k`-fold composite `V^{⊗k}` (the model `M ≅ V`, the model's
  model `M₂ ≅ V`, …, all order-isomorphic to the system). One tick = append one tensor copy.
  **The identification "persist k ticks = faithfully hold the k-fold joint self-record" is the
  load-bearing MODELING CHOICE — state it as such; it is the diachronic axiom, not a theorem.**
- **Product-faithful (self-transparency) fraction.**
  `r_V(k) = (∏ local effect-dims) / (effect-dim of the composite V^{⊗k})` for the matrix fields where the
  composite over-counts is the reciprocal — define `r_V(k) := min(P,C)/max(P,C)` with `P = (dim V)^k` and
  `C = dim(V^{⊗k})`, so `r ∈ (0,1]` always and `r = 1 ⟺ local tomography holds at that tensor power`.
  `r_V(k) → 0` = asymptotically self-opaque; `r_V(k) ↛ 0` (bounded below) = diachronically faithful.
- **THE COMPOSITE IS THE HAZARD — defining it (or proving it does not exist) is PART OF THE TASK.**
  `M_n(ℝ)` and `M_n(ℂ)` composites are unambiguous (`M_{nm}(𝕂)`). For `M_n(ℍ)`, spin factors, and the
  Albert algebra there may be NO associative `*`-tensor inside the EJA framework (ℍ⊗ℍ ≅ M₄(ℝ); exceptional
  and most special non-C* EJAs have no C*-tensor). If `V` has no associative self-composite, the tower is
  UNDEFINED past `k = 1` — record that as a THIRD outcome (structural exclusion), not an error.

## KNOWN ANCHORS (finding D — verified exact; reconfirm, do not re-derive from scratch)
- `r_ℝ(k) = (n+1)ᵏ / [2^{k−1}(nᵏ+1)] = 2·((n+1)/2n)ᵏ · [1+o(1)] → 0` (rebit n=2: 1, .9, .75, .596, .460, .350).
- `r_ℂ(k) ≡ 1` for all `n,k` (local tomography at every tensor power).
- `r_ℍ(k) = (2nᵏ−1)/(2n−1)ᵏ → 0` (n=2: 1, .778, .556, .383, .259, .174) — UNDER the M_{nᵏ}(ℍ) composite
  choice; FLAG whether that composite is even legitimate (quaternionic QM's tensor is famously
  problematic, Araki). If it is not, ℍ may belong to the structural-exclusion bucket instead.

## THE CLAIM TO PROVE OR DISPROVE (CLAIM DIACHRONIC-NARROW)
For every finite-dimensional simple Euclidean Jordan algebra `V`:
> `r_V(k) ↛ 0` (the self-history transparency is bounded below as k→∞)  **⟺**  `V ≅ M_n(ℂ)ˢᵃ`
> (equivalently `r_V(k) ≡ 1`). Every other simple EJA either has `r_V(k) → 0` or has no associative
> self-composite (tower undefined past k=1).

And the SECOND, novelty-deciding question:
> Is "`r_V(k) ↛ 0` on **self-towers** `V^{⊗k}`" STRICTLY WEAKER than full local tomography
> (`dim(A⊗B) = dim A · dim B` for **all** pairs A,B), while still selecting exactly `M_n(ℂ)`? I.e. does
> demanding transparency only of the system-with-itself buy anything over demanding it of all composites,
> or does self-tower-LT already entail full LT?

## WHAT TO COMPUTE (exact/ℚ where possible)
1. Reconfirm `r_ℝ, r_ℂ` exactly; resolve the `r_ℍ` composite question (legitimate tensor → compute decay;
   illegitimate → structural-exclusion bucket).
2. **Spin factors `V_q` (dim q+1), every q** — including the low-rank coincidences `V_2≅h₂(ℝ)`,
   `V_3≅M_2(ℂ)ˢᵃ` (= the complex qubit — the ℂ case in disguise), `V_5≅h₂(ℍ)`, `V_9≅h₂(𝕆)`. Determine the
   self-composite (or its non-existence) and `r_{V_q}(k)`. The decisive sub-question: is there a spin
   factor with `r(k)` BOUNDED in (0,1) — a **bounded intruder** that would falsify CLAIM DIACHRONIC-NARROW.
3. **Albert algebra `h₃(𝕆)` (dim 27)** — exceptional, not the s.a. part of any associative algebra ⇒
   almost certainly structural-exclusion (no self-composite). Confirm.
4. Settle the strictly-weaker question: exhibit an EJA that fails full LT but is diachronically faithful
   (⇒ strictly weaker, real novelty), OR prove self-tower-faithfulness ⟹ full LT among EJAs (⇒ same
   selected class as LT, axiom merely a weaker-looking restatement — still self-natively motivated).

## DECISION TREE (pre-declared — classify, do not narrate around it)
- **NARROW-CLEAN:** every non-ℂ simple EJA has `r→0` or no self-composite; only ℂ has `r↛0`. CLAIM
  DIACHRONIC-NARROW **TRUE**. Report whether the axiom is strictly weaker than full LT (best: weaker AND
  same class ⇒ the self-native weakest-axiom result that answers the "you reglossed LT" referee).
- **NARROW-FAILS (bounded intruder):** some non-ℂ EJA `E` has `r_E(k)` bounded in (0,1). CLAIM **FALSE**.
  Report `E` and its bound. Consequence: diachronic faithfulness does NOT pin ℂ; the paper needs full LT
  (`r≡1`), and the "weaker axiom" novelty dies. THIS is the only outcome to escalate to Bryan.
- **VACUOUS-DOMINATED:** the non-matrix EJAs are excluded structurally (no self-composite) rather than by
  decay. CLAIM TRUE but for a different reason (a self-model that cannot compose its own history is a
  fortiori not diachronically faithful). Report the partition: decay-killed {ℝ, ℍ?} vs structurally-killed
  {spin n≠3, Albert} vs survivor {ℂ}.

## GUARDRAILS
- NO forcing claim. NO SSOT status flip (P5 stays CONDITIONAL-SYNTHESIS) from CLEAN or VACUOUS — both are
  the standing "selected, not forced" status, now with a precise reach. Escalate ONLY a bounded intruder.
- The rebit `M_n(ℝ)ˢᵃ ⊨ Def-1` stays the load-bearing independence witness; a diachronically-opaque
  self-model is still a synchronically faithful self-model. Say so.
- The identification "persist across self-model time = faithfully hold the k-fold self-record" is the
  diachronic AXIOM (a modeling choice), not a theorem — keep it labeled; do not smuggle it as forced.
- If you cannot define the self-composite for a family, report the obstruction as the result (structural
  exclusion), do NOT substitute the GPT minimal tensor (which makes `r≡1` trivially and voids the question).
- Exact/ℚ for matrix families and the dimension counts; spin/Albert may be closed-form or structural.

## OUTPUT
- The precise definitions actually used (composite per family, `r_V(k)`), with the matrix anchors reconfirmed.
- A per-family table: `dim V`, the self-composite (or "none"), `r_V(k)` closed form, decay/bounded/≡1/undefined.
- Verdict on CLAIM DIACHRONIC-NARROW: NARROW-CLEAN / NARROW-FAILS / VACUOUS-DOMINATED, with the evidence.
- Verdict on strictly-weaker-than-LT: weaker (with witness) or equivalent (with proof).
- One-line honest SSOT status (expected: "diachronic faithfulness selects exactly ℂ among EJAs, weakest
  form is self-tower transparency ↛ 0, no flip" — unless a bounded intruder, which escalates).
