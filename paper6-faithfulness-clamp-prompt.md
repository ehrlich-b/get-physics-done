# GPD Prompt: Does FIELD Faithfulness Carry a Derivative Term? (the one un-run clamp gate)

_Created 2026-06-15, re-aimed same day after a record check. PROVE-OR-DISPROVE task
for GPD (`~/scratch/get-physics-done/`). This is the ONE residual gap after both
substrates were exhausted (fiber dead across six kinds; variety = extremize
FORCES-NOTHING v33, induce CLOSES-CONDITIONAL v34, entanglement DEAD-FISHER v35).
The whole gravity gap is the single clamp below. See `selection-law-ledger.md` §6,
`entanglement-route.md` §8.2-8.3, `lie-sector-gravity.md` (the [PROGRAMMATIC]
faithfulness conjecture), and `paper6-v2-fork-a-draft.md` §5._

---

## The clamp, and why this is the only un-run piece of it

The clamp = **state-fp ⟹ metric-fp**: the self-modeling-faithful state (Paper 5's
φ-iteration fixed point) is a critical point of the gravitational action its own
matter fluctuations induce. As an equality of critical-point conditions:

> **δF/δM = 0  ⟺  δΓ/δM = 0**

where `Γ[g[M]]` is the induced gravity action (v34, slot 94: clean
`a₁ ∝ ∫R√g`) and `F[M]` is the field-level self-modeling **faithfulness
functional** on the variety matter profile `M(x)`. We have Γ; the open object is F.

**The asymmetry that defines the gate.** `δΓ = G_μν − κT_μν` is a *curvature*
object — second-derivative-in-metric. For the faithful profile to extremize it, the
faithfulness variation `δF` must carry matching base-derivative structure. So the
ENTIRE clamp rides on one question:

> **Does field faithfulness (`M(x) = φ[M](x)` on the curved variety) carry a
> genuine base-derivative term, or does it collapse to the pointwise algebraic
> `−Tr(h²)` form that is already dead?**

Collapse ⇒ faithfulness is a state-space (Fisher) extremum, structurally distinct
from the curvature extremum δΓ ⇒ **the clamp is FALSE** (faithful ≠ Einstein-
extremal). Derivative structure ⇒ F has the right TYPE to possibly match Γ, and
only then is the comparison non-vacuous.

## WHAT IS ALREADY DEAD — do NOT re-run (this is the whole point of the re-aim)

Three costumes of "faithfulness = extremize something" are already killed. The slot
is wasted if it re-derives any of them:

1. **Entropy / MaxEnt costume — DEAD (one-term tautology + v35).** "Faithful = the
   entropy maximum at fixed trace" is a *one-term* extremum = a tautology ("of
   course the max is the max"; `δ²S ∝ −Tr(h²)`, `entanglement-route.md` §8.1-8.2).
   Gravity needs a *two-term* balance (Jacobson: geometric/area vs matter). The
   missing second (geometric) term was then computed away by **v35 DEAD-FISHER**:
   every FS-canonical "area" is a power of the quantum Fisher variance — the SAME
   state-space object as the entropy, not an independent geometric term. Do not
   re-propose entropy-max as F.
2. **Fixed-point-SCALE handle — DEAD.** "Faithfulness fixes `κ_ind` via the fixed
   point's intrinsic scale (`det X*`, `Tr X*²` → `Λ_f`)" fails: the faithful point
   is the matter-free `I/3` shell (`Tr X² = 1/3`), so its scale is trivial, not a
   physical cutoff (2026-06-06). Do not pin `κ_ind` by importing the fixed-point
   scale.
3. **Static / pointwise `ρ_J` handle — DEAD.** Pointwise faithfulness gives
   `ρ_J = 0 ⟹ X ∝ I` (matter-free) or `det = 0` (incomplete) (2026-06-06). F must
   be the FIELD condition on `M(x)`, NOT pointwise `ρ_J`.

The naive field extension "apply φ pointwise at every base point" reproduces (3)
and trivially collapses (no derivatives) — that is the uninteresting disproof. The
NON-trivial, un-run object is the **geometry-respecting** field faithfulness: the
profile self-models faithfully using the variety's OWN Fubini-Study / Lichnerowicz
structure (the same geometry that sources the metric mode in v31-v34) to relate
neighboring base points.

## Background (established, exact over Q)

- `h_3(O)`; Peirce `V_1(1)+V_{1/2}(16)+V_0(10)`; `V_0 → R^{3,1}`;
  `V_{1/2} = 16` of Spin(10).
- **Variety substrate:** the algebra's idempotent variety (OP² / CP² C*-cut). v31/v32:
  a matter-sourced TT metric mode EXISTS, `‖TT(B3)‖² = (1/30)(Tr M²)²` closes. v33
  Gate-0: `Δ_L r = 32 r`, `ε = λ_L − 2Λ = 20 ≠ 0` (the rank wall is CLEARED here;
  the metric dofs exist and are sourced by a single ε=20 eigentensor).
- **Γ in hand (v34, slot 94, triple-path HIGH):** integrating out `φ_M` on CP² gives
  `a₁ ∝ ∫R√g`; the FS geometry is self-consistent under its own *matter-loop* (the
  metric-side fixed point). `ε = 20` FORCED, `κ_ind` FREE. **NB: v34 did the
  METRIC-side loop only; the STATE-side faithfulness F and the coincidence check are
  un-run** — that is exactly this task. Reuse the slot-94 harness.
- **φ-iteration:** `nonlinear_iteration.py` (`ρ_J` is its attractor; faithful = the
  model matches the substrate = fixed point).
- **The dead pointwise form:** `δ²S ∝ −Tr(h²)` (Fisher/Bures), `entanglement-route.md`
  §8.1. Gate 0 is asking whether the geometry-respecting field F escapes this.
- CONSTRAINT: no thermodynamics / horizons / ensemble / epistemic entropy (demon
  test 2.0). F is a self-consistency/fixed-point functional. If a step needs an
  ensemble or coarse-graining entropy, it is woo — flag and stop.

## Gates (run IN ORDER; stop at the first DEAD)

### Gate 0 — DERIVATIVE STRUCTURE OF FIELD FAITHFULNESS (the decisive gate)
Take the φ-iteration fixed-point condition and promote the state to a FIELD `M(x)`
on the variety, extended via the variety's intrinsic FS/Lichnerowicz geometry (NOT
a naive pointwise copy). Linearize the fixed-point condition; inspect the
faithfulness operator `L_F = δ(faithfulness)/δM`.
- **DEAD if** the only well-defined field extension is pointwise — `L_F` is the
  algebraic `−Tr(h²)`-type (state-space/Fisher) operator with no base derivatives.
  Then faithfulness is structurally distinct from the curvature operator δΓ, the
  clamp is **FALSE** (faithful ≠ Einstein-extremal), fork A is **proven** (not just
  adopted), and the 2026-06-07 "self-modeling is fiber-local" brainstorm is upgraded
  to a **theorem** (self-modeling provably cannot reach the base metric). Report the
  obstruction exactly.
- **PROCEED if** the geometry-respecting field faithfulness carries a genuine
  base-derivative term (a Laplacian/Lichnerowicz-type operator on `M`, same TYPE as
  δΓ). Report the operator.

### Gate 1 — WRITE F
If Gate 0 proceeds, write the field faithfulness functional `F[M(x)]` whose
stationarity is the geometry-respecting field φ-fixed-point, exact over Q. It must
not reduce to pointwise `ρ_J` or to entropy-max.

### Gate 2 — COMPARE CRITICAL POINTS (the clamp)
Compute `δF/δM = 0` and `δΓ/δM = 0` (Γ from slot 94). Do they share critical points
— `F = Γ∘(M↦g)` up to a monotone reparametrization, or proportional variations on
the sourced ε=20 mode?
- **ALIVE if** they coincide: the faithful profile IS the metric-critical profile.
  `state-fp ⟹ metric-fp` is proved by direct computation.
- **DEAD if** the faithful and gravitating profiles generically differ. Clamp false;
  report the exact mismatch.

### Gate 3 — DOES THE MATCH PIN κ_ind?
If Gate 2 is ALIVE: does the coincidence `δF = δΓ` hold only at a specific `κ_ind`
(pinning the free coupling by the MATCHING condition, NOT by importing a scale —
handle 2 is dead), or for all `κ_ind` (form-only)?
- **ALIVE (strong)** — matching pins `κ_ind` ⟹ a definite induced `G`; gravity with
  a number. By Lovelock, F yielding ANY local 2nd-order covariant divergence-free
  rank-2 law already forces Einstein + Λ.
- **ALIVE (form-only)** — matching for all `κ_ind` ⟹ the clamp forces the LAW
  (`G_μν = κT_μν`, the constructed/variety metric IS Einstein) with `κ` contingent.
  This is still deriving gravity in the GR sense (GR does not predict `G` either) —
  report as the genuine result, with `κ` flagged contingent (Level-6 / Molien).

## Deliverable

State the gate it died at (or that it reached ALIVE at Gate 3), exact over Q:
whether field faithfulness is pointwise-collapse or derivative (Gate 0, the
decisive number — the form of `L_F`); the explicit `F` if written (Gate 1); the
`δF=0` vs `δΓ=0` comparison (Gate 2); the `κ_ind` status (Gate 3). One sentence
each on the clamp, the selection-law ledger, and the 06-06↔06-07 tension.

## Expected outcome

Skeptical prior: **DEAD at Gate 0** — the 2026-06-07 fiber-locality intuition and
the substrate-dictionary "model-shadow" read both bet field faithfulness collapses
to the pointwise state-space form. BUT both were argued on the FIBER; on the VARIETY
the matter mode already lives in a Lichnerowicz/FS derivative context (v31-v34), and
v34's metric-side loop is self-consistent there — so the collapse is NOT a foregone
conclusion, and that is precisely the un-run uncertainty. Either way the result is
theorem-grade and governance-compliant:
- **DEAD at Gate 0/2** ⟹ the clamp is *refuted*; fork A stops being "localized to an
  OPEN conjecture" and becomes "localized to a CLOSED one" — Paper 6 v2 ships as a
  genuine no-go, and we have *proven* why self-modeling forces QM but not gravity.
- **ALIVE through Gate 3** ⟹ the clamp is dissolved by computation; the program
  derives the gravitational law (with `κ` forced or contingent); first
  more-than-Paper-5 result; Paper 6 is rewritten as a positive result.
