# Paper 5 — The Jordan-φ Fixed-Point Sharpness Probe (is the rebit's recursive self-model irreducibly BLURRED, and does that blur ever become an ABSENCE?)

## TASK TYPE
Compute, exact/ℚ where possible, with a PRE-DECLARED decision tree. This is primarily a
**characterization** computation (quantify how the real self-model's recursive fixed point degrades vs
complex), with ONE narrow fork that could bear on forcing. Read the billing in "HONEST FRAME" before
deciding the result moves anything.

## HONEST FRAME (read first — do NOT overclaim the result)
- The **complex-axis forcing question is already CLOSED** by the field-blindness separation theorem
  (commit `e42bb84`, §13): `M_n(ℝ)ˢᵃ ⊨ Definition 1` as a finite, faithful (φ=id), consistent
  self-model ⇒ self-modeling does NOT force complex. `complex = self-modeling + ⟦a,b⟧:=−i[a,b] closure`
  ("the generator of self-update is itself an observable" = DOM), proven IRREDUCIBLE with the rebit as
  the independence model. This probe does **not** reopen that. The rebit is a self-model, full stop.
- What is still OPEN is the **constitutive reading** of Definition 1's faithfulness clause: §13 used the
  STATIC order-iso (φ=id). If faithfulness should be read DYNAMICALLY — the model must track the
  system's own *becoming*, i.e. φ must be a self-consistent fixed point of the recursive map
  `ρ* = R(M(ρ*))`, not merely a static order-iso — then maybe the rebit fails the dynamical reading.
  Cheap evidence (`phi_recursion.py` Part B) says the rebit **stalls at a blurred mixed state**
  (purity ≈ 0.646), it does NOT lose the fixed point ⇒ leans **selection** (a blurred self-model is
  still a self-model).
- Therefore the EXPECTED, high-value deliverable is a **characterization**: an exact, basis-free
  statement of HOW the real self-model's recursive fixed point degrades (blur, generator leakage) while
  complex stays sharp — the quantitative centerpiece of the characterization paper. The forcing fork
  (real fixed point VANISHES, not just blurs, under the canonical basis-free φ) is a LOW-probability
  bonus, not the goal. Do not report a blurred-but-existing fixed point as a forcing.

## THE CLAIM (CLAIM REBIT-BLUR)
For the canonical basis-free Jordan-φ recursion on `M_2(𝕂)ˢᵃ`:
- **(Selection / expected):** real self-tracking flows have φ-fixed points that EXIST but sit below a
  purity ceiling `Tr(ρ²) < 1` (blurred), while complex admits sharp stable fixed points
  (`Tr(ρ²) → 1` reachable). The gap is a *characterization* of the central-i import, not a new import.
- **(Forcing / low-P fork — would need to hold to matter):** for EVERY nontrivial real self-tracking
  flow the φ-fixed point exists only below a **field-INDEPENDENT** purity bound, OR fails to exist as a
  consistent recursive fixed point at all — i.e. the rebit cannot dynamically model its own becoming
  even fuzzily. Only THIS would bear on the constitutive reading (push it toward forcing).
- **(Null):** ℝ and ℂ behave the same once each is projected into its own legal state space ⇒ no
  dynamical separation; DOM/§13 (the static algebraic separation) is the whole story.

## THE φ — DECLARE IT ALGEBRAICALLY BEFORE ANY NUMERICS (this is the crux; get it right)
Two hard-won constraints from prior work (memory `phi-op-status-not-undefined`, up-tower README):
1. **Do NOT use an eigenvalue-level / individual-state map** — every such candidate OVERSHOOTS to the
   pure vertex (1,0,0); the ρ_J peak is a saddle, unstable at every learning rate. (7+ such candidates
   already dead.)
2. **Do NOT invent coordinate damping** (Codex's guard) — no hand-tuned per-axis shrink factors. The
   damping must come from the algebra (off-diagonal Peirce coupling), or there is no result.
The legitimate candidate is the **Jordan/Peirce φ**: define φ via the Peirce decomposition
`V = V₁ ⊕ V_{1/2} ⊕ V₀` relative to the current model idempotent, using the multiplication rules
(`V₁·V_{1/2} ⊂ V_{1/2}`, `V_{1/2}·V_{1/2} ⊂ V₁+V₀`, …). The off-diagonal `V_{1/2}` block is exactly
where the field 𝕂 = ℝ/ℂ/ℍ lives, so a Peirce-defined φ is *intrinsically field-sensitive and basis-free*
— it is the only φ for which "ℝ vs ℂ" is a fair, non-circular test. **State the closed-form algebraic
map `φ: V → V` (or `φ: state → state`) explicitly, prove it is automorphism-equivariant (basis-free),
THEN iterate.** If you cannot write a basis-free φ, report THAT as the obstruction and stop — do not
fall back to a coordinate map.

## THE RECURSION
`ρ* = R(M(ρ*))`, the "I am a self-model modeling myself" fixed point:
- `M` = the model's update (the forced sequential/Lüders product compressed into the model block).
- `R` = the recognition/read-back order-iso (Paper 5's faithful tracking map).
- Iterate `ρ_{k+1} = R(M(ρ_k))` (= the Peirce-φ above) from a spread of seeds; study the fixed set.

## METRICS (Codex's six — compute all, exact/ℚ where the algebra allows)
1. **Existence** of fixed points (per field 𝕂 = ℝ, ℂ; optionally ℍ).
2. **Stability basin** (which seeds converge; is the fixed point an attractor or a saddle).
3. **Purity** `Tr(ρ*²)` at the fixed point (the blur measure; the rebit's ≈0.646 to confirm/refute).
4. **Distance to the pure-state boundary** (how far the fixed point sits from the cone's extreme rays).
5. **Generator leakage / projection residual**: take the reversible self-update generator at ρ*
   (`−i[ρ*, H]` for the tracked H); measure the norm of its component OUTSIDE V (for the rebit this is
   the Pauli-Y / so(2) part, provably ∉ V; for complex it is 0). This is the DOM blind-spot, quantified.
6. **Invariance** under automorphism / basis change (confirms the result is φ-intrinsic, not coordinate).

## DECISION TREE (pre-declared — classify the result, do not narrate around it)
- **Real fixed point VANISHES or is field-INDEPENDENTLY bounded away from purity 1** (and complex is
  sharp), robust under metric 6 ⇒ **forcing fork lives**: report as bearing on the constitutive reading
  (dynamical Def-1 may exclude the rebit). HIGH bar — needs metrics 1+3+6 to all point the same way.
- **Real fixed point EXISTS but blurred (purity < 1), gap depends on φ/generator choice** ⇒
  **SELECTION confirmed**: the characterization result. Report the exact purity ceiling + generator
  leakage (metric 5) as the quantitative face of the central-i import. EXPECTED outcome.
- **ℝ and ℂ identical in their own legal state spaces** ⇒ **NULL**: no dynamical separation beyond §13's
  static one. Report that DOM/§13 is the complete complex-axis story and the recursion adds nothing.

## GUARDRAILS
- The rebit is a consistent self-model (§13, `e42bb84`); a blurred-but-existing fixed point is NOT a
  forcing — say so. Only metric-1 absence or a field-independent metric-3 bound bears on forcing.
- φ MUST be basis-free (Peirce/automorphism-equivariant). A coordinate-damped φ invalidates the run.
- Exact/ℚ for `M_2`; numeric cross-check `M_3` optional. Report exact purity ceiling if one exists.
- No SSOT status flip from a Selection or Null result (both already the standing P5 status). Only a
  robust Forcing-fork result would warrant escalating to Bryan for a status discussion.

## OUTPUT
- The explicit basis-free φ (algebraic closed form) + proof of automorphism-equivariance, OR the
  obstruction to writing one.
- The six metrics for ℝ and ℂ (M_2), exact where possible; the rebit purity ceiling.
- Decision-tree classification: Forcing-fork / Selection / Null, with the evidence that placed it.
- One-line honest SSOT status (expected: "Selection confirmed, characterization sharpened, no flip").
