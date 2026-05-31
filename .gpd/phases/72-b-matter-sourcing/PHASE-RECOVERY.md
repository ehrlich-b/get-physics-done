---
phase: 72
phase_name: B — Matter-Sourcing
created: 2026-05-31
outcome: HALTED — backtracked to Phase 70 (researcher decision; backtracking trigger #3 honored)
plans_succeeded: []
plans_partial: ["72-01"]
plans_not_started: ["72-02"]
plans_failed: []
plans_skipped: []
checkpoint_tags: ["gpd-checkpoint/phase-72-wave-1-1780196865-54236"]
verdict_recorded_in: derivations/72-matter-sourcing.tex
reopens: 70
---

# Phase 72 Recovery — HALT & BACKTRACK to Phase 70

## Execution Summary

Phase 72 (B — Matter-Sourcing) was **halted at the Wave-1 first-result gate** by
researcher decision. This is **not a failure**: the plan's explicit backtracking
trigger #3 fired with a decisive, exact-over-Q result, and the result *is* the
Phase-72 VALD-04 finding (negative-result-is-success). The decisive cross-term ON/OFF
matter verdict (72-02) was deliberately **not** run; the milestone backtracks to a
reopened Phase 70.

## The VALD-04 finding (the real result)

The dim-4 cone-Hessian sub-slice `Hess(−log det₃)` at the M=0 center `I/3` is
`diag(9,9,18,18)`, with Ricci endomorphism eigenvalues **{0, −1, −1, −1}** (exact over
Q, reproducible in 3.4s):

- `R = −3` ✓ (matches the Phase-71 anchor), **but** Einstein needs all eigenvalues
  equal to `R/4 = −3/4` → the slice is **NOT Einstein** in n=4.
- The eigenvalue-0 direction `(1,1,0,0) = β+γ` is the **timelike x₀** direction under
  `h₂(C_u) ≃ R^{3,1}` (the det₂ Minkowski form `βγ/3 − p²/3 − q²/3`; the `βγ/3` block
  is the hyperbolic 1+1 part, `(1,1)` its timelike eigenvector). So the M=0 vacuum is
  a **static product `R_time × H³_space`** (the flat factor is *time*), `K(p,q)=−1/2`.
- A non-trivial 4-dim metric cone is never Einstein — textbook, **not an engine bug**
  (all 4 Phase-71 regression anchors reproduced exactly; engine faithful).

**A GR Λ-vacuum must be Einstein (Ric ∝ g).** No baseline subtraction turns a
non-Einstein vacuum into an Einstein one — so "which Λ reference?" presupposes a
maximally-symmetric vacuum this construction does not produce. THAT is the result.

## Adjudication (researcher decision 2026-05-31)

- **(a) det₂=1 H³ leaf — REJECTED (fp-relabel).** References 4d gravity against the
  3d *spatial* hyperboloid, dropping the flat=timelike direction; H³ is the *wrong*
  symmetric space (GR's empty hyperbolic-slice vacuum is Milne = flat Minkowski, not
  H³) and one dimension short. Manufactures a pass by swapping spacetime for space.
  (Quotienting the dilation/timelike direction — old option 3 — is the same move,
  likewise rejected.)
- **(b) construction-(ii) `g=η+h` — CONDITIONAL.** Flat at center = GR's correct empty
  vacuum (right physics), but: (i) flatness is *inserted* by the center-subtraction →
  `Λ=0` built in, not derived (Phase 73 circularity tripwire); (ii) adopting it
  *abandons* the route thesis "gravity = curvature of the cone-Hessian" (cone-Hessian
  gives `R×H³`, not flat). Admissible ONLY after a reopened Phase 70 explicitly rules
  `η+h` (not the cone-Hessian) is THE spacetime metric and restates the thesis.
- **DECISION (c): halt + reopen Phase 70.**

## What is PRESERVED (not what broke)

Committed clean Task-1 results stand and carry forward unchanged to whichever metric
Phase 70 selects:

- Peirce index map `V₁={0}`, `V₀={1..10}`, `V_{1/2}={11..26}` (`L_{E11}` diagonal).
- The unique V₀↔V_{1/2} octonion channel `2·Re((x₂x₁)x₃)`; `α` (V₁) absent from the
  triple → structurally explains Phase-71 V₁-inertness.
- Non-vacuous representative M (cross-term `−13/315 ≠ 0`, all three slots, e₄ content).
- The `ΔR(M) = R(X_bg+M) − R(X_bg)` isolation pipeline + n=4 Ricci decomposition.

## Reopened Phase 70 task (well-posed; resolve exactly one question)

The Riemannian cone-Hessian (thesis → `R×H³` non-Einstein vacuum) and the Lorentzian
`η+h` bridge (→ flat vacuum) disagree about the M=0 geometry → the construction-(ii)
signature bridge is **underdetermined** (the Riemannian/Lorentzian tension already in
CONVENTIONS.md). **Which object is the physical spacetime metric?**

- **If cone-Hessian (thesis):** M=0 vacuum is non-Einstein (`R×H³`) → route does NOT
  yield GR-with-Λ-vacuum. Most it can claim = **linearized matter-response (spin-2) on
  a FIXED non-Einstein `R×H³` background** — a strictly weaker result, NAMED as such,
  never relabeled "GR derived."
- **If `η+h` bridge:** thesis wrong as stated → restate (why the bridge metric, not the
  cone curvature, is the gravitational field); carry the `Λ=0` tripwire into Phase 73;
  (b) becomes the reference.

**Discipline:** exact over Q; do NOT insert any factor to force `Ric ∝ g` or force
flatness (corrupts the verdict it feeds); SSOT `det₃`; headline `{0,−1,−1,−1}`.

## Artifacts

- `derivations/72-matter-sourcing.tex` — VALD-04 finding + adjudication + Phase-70 task
  (commit `62838220`, reframed this session).
- `.gpd/phases/72-b-matter-sourcing/72-01-baseline-probe.py` — 3.4s exact-over-Q
  reproduction (eigenvalues, regression anchors, the obstruction; exit 0).
- Wave-1 checkpoint tag `gpd-checkpoint/phase-72-wave-1-1780196865-54236` (retained —
  phase did not complete normally).

## Next step

`/gpd:revise-phase 70` — supersede the completed Phase 70 and create the replacement
that resolves the metric-selection question above. Phase 72 will be re-planned after
Phase 70 resolves (the matter pipeline is preserved and ready).
