# Slot 83 / v23.0-candidate — GATE 2 SUMMARY (THE TEST)

**The Two-Term Balance Question (Jacobson J5, fiber side) — Gate 2: the exhaustive
forced-λ non-degenerate-competition sweep at X = I/3.**

## VERDICT: **DEAD at degree ≤ 3**

No candidate × constraint forces a non-degenerate competing λ ≠ 0. The fiber carries **no
program-native second term** that turns the faithful point into a genuine two-term
Jacobson balance — the vacuum-identification flip (§4) is, at the fiber level and through
degree 3, **decoration**: the route is FULLY gated on the base/format object.

Gate 3 NOT run (correctly — LIVE-only). Exact over Q (log symbolic), source-guarded.
Driver: `code/entanglement_two_term.py` `gate2()` (deterministic non-hardwired verdict;
self-tested).

---

## The sweep (16 candidates × 4 constraints = 64 cells)

**Candidates** = every deg-≤3 monomial in the Gate-0 generators
`{α(1), T=β+γ(1), Q_v(2), Q_s(2), det_3(3)}`:
`α, T, α², α·T, T², Q_v, Q_s, α³, α²T, αT², T³, Q_vα, Q_vT, Q_sα, Q_sT, det_3`.

**Constraints** = `{ fixed Tr, fixed Tr_face=β+γ, no constraint, fixed det }`
(bug-guard #3: `Tr X²=1/3` BANNED — the faithful branch).

## The mechanism (exact over Q)

Gate 1: **∇S_face(I/3) = 0** in all 27 directions. So criticality
`δ(S_face + λA) − μ·δg = 0` reduces to `λ·∇A(I/3) = μ·∇g(I/3)`, and **(λ,μ)=(0,0) ALWAYS
solves it** ⇒ **λ = 0 always allowed ⇒ λ ≠ 0 never FORCED.** Verified cell-by-cell with
exact `linsolve` (not assumed). Three failure modes, all → NOT FORCED:

| mode | when | solset | verdict |
|------|------|--------|---------|
| tautology | ∇A≠0, no constraint | `λ∇A=0 ⇒ λ=0` | not forced |
| λ-glaze | ∇A=0 (`Q_s`, `Q_sα`, `Q_sT`) | `{(λ,0)}` λ free | DEAD (bug-guard #2) |
| constraint-absorbed | ∇A ∥ ∇g | 1-param family incl. (0,0) | λ=0 allowed |

## The obstruction pattern (precise)

**Every candidate gradient at I/3 lies in the 3-dim DIAGONAL subspace `span{e_0,e_1,e_2}`**
(∇α=e_0, ∇T=e_1+e_2, ∇Q_v=−⅓(e_1+e_2), **∇Q_s=0**, ∇det_3=⅑(e_0+e_1+e_2)). The S_face
Fisher curvature lives on the **traceless** face block (β−γ and the x1-octonion). The
A-gradients pull only along diagonal/trace directions ⇒ **no shared block ⇒ no Jacobson
saddle**.

**Deepest statement:** a forced two-term balance requires `∇S_face ≠ 0`, but I/3 is the
entropy MAXIMUM so `∇S_face = 0` necessarily. *The faithful point being the vacuum/max is
precisely what makes a forced balance impossible there.* This is the §8.1/§8.2 deflation,
exact over Q: the one-term extremum is a tautology; the missing competing (geometric) term
IS the base/format object, not anything on the fiber.

(Second-order note: some candidate Hessians DO touch the Fisher block — `Q_v` family
positive, `det_3` `−2/3` on β−γ — but it is never *triggered*, because λ is never forced
off 0. The obstruction is first-order, not a 2nd-order misalignment.)

## Bug-guards (binding) — all satisfied

- **#1 vacuity / non-hardwired:** the forced-λ routine is GENERAL — a hypothetical
  off-faithful input (∇S_face≠0, ∦∇g) returns `forced=True`; I/3 returns `False`. LIVE is
  detectable in principle ⇒ the DEAD answer is SUBSTANTIVE, not a designed-in trivial pass.
  Does NOT collapse to the first-law δS=δ⟨K⟩ identity (tests the SECOND term).
- **#2 λ-glaze:** a free λ = DEAD (the `Q_s` family), recorded as such.
- **#3 constraint-smuggling:** `Tr X²=1/3` BANNED, asserted absent.
- **#4 normalization:** pinned compress-then-normalize ρ_face used throughout.
- **#5 u-alignment:** N/A (single-face, single-point at I/3; no inter-face map).

## Anti-overclaim + notes

- **DEAD at degree ≤ 3 ≠ absolute DEAD** (said once): degree ≥ 4 invariants remain, with a
  naturalness penalty as a "geometric/volume" term. The candidate space was exhaustive
  THROUGH degree 3 (Gate-0 closure).
- This is the clean publishable scope theorem the brief anticipated: **the fiber-side
  analog of "Molien has no κ-slot"** — the second/geometric Jacobson term provably does not
  live on the fiber (at low degree); the route is gated on the base/format object. Jaksland
  governs (only program-native J5 counts; this localizes the gate precisely).
- **§8.5 contact:** the I/3 2nd-order object δ²S_face ∝ −Tr(h²) = v17's Fisher–Bures
  corpse, STATE-side (right object, wrong side of the state/event divide; not a
  resurrection).
- **§8.5a:** the J5 target is the MODIFIED (CGM/Speranza R^(2Δ)) Jacobson. No contact
  forced here — DEAD is about the *existence of a native second term*, upstream of the
  relevant-operator R^(2Δ) question (which lives on the un-built emergent QFT).
- **LIVE ≠ Einstein/gravity/J5-won** (moot — DEAD). No κ, no Λ, no G = κT anywhere.

## Confidence

**[CONFIDENCE: HIGH].** The verdict rests on three independent exact-over-Q facts: (1)
∇S_face(I/3) = 0 in all 27 directions (Gate 1, polynomial identity); (2) all 16 candidate
gradients are diagonal / the Q_s family vanishes (direct computation); (3) every one of the
64 criticality systems admits (λ,μ)=(0,0) (exact `linsolve`). The non-hardwired self-test
confirms the routine would flag LIVE if the geometry allowed it. The mechanism is
structural (vanishing entropy gradient at the maximum), not a numerical near-miss.
