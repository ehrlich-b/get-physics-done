# Phase 92 (v32.0-candidate) — GATE 1 SUMMARY: Controls (zero evidential weight)

> **CORRECTION (v32.0-B, binding).** This first-pass summary predates the three-path reconciliation
> (`v32-reconciliation-directive.md`; Boucetta arXiv:0712.2830 fetched directly). The matter TT mode
> is NOT the "λ=12 (1,1) dim-8 su(3)-adjoint", and the verdict norm is NOT κ=1/54. RECONCILED: a single
> **λ_L=32 eigentensor straddling the triple-27** (Boucetta Table V/VIII row 2 (1,1)-27 ⊕ Tables VI/VII
> (2,0)/(0,2)-27s), norm **‖TT(B3)‖²=(1/30)(TrM²)²** (full mode; 1/54 was the (1,1)-block share, forced
> 5:4 split), **ε=20**, direction **T₂₇[P27(M⊗M)]** (the 27-channel; c₈=c₁=0; c∝N(M) FAILS as a
> wrong-channel claim, not "richer"); Koiso clean (no TT at λ=12). Wherever this file says
> "dim-8/(1,1)/adjoint", "κ=1/54", "c∝N richer", "rank-6=d-symbol image", or "Weitzenböck shift", read
> `92-VERDICT.md` + `92-tensor-dictionary-RESEARCH.md` §7/§8 instead.


**Driver:** `python3 -u code/lichnerowicz_response.py g1` → **6/6 PASS** (~250s, exact over Q).

Gate 1 runs the controls (zero evidential weight, all must behave): the non-hardwired `verdict()`
self-test, the vacuum, the Δ_L structural identities (Δ_L on g, the gauge-preservation identity), the
sign-pin regressions, and the mandatory Schur check. A failure of 1d or 1f would be a machinery /
convention bug — STOP, not physics.

| # | Check | Result |
|---|---|---|
| 1a | `verdict()` NON-HARDWIRED: LIVE→LIVE, PARTIAL→PARTIAL, contradiction→STOP, Schur-fail→STOP (reads only the flags) | PASS |
| 1b | VACUUM M=0: B3≡0, extracted TT r≡0, Δ_L(0)≡0 (every object vanishes at zero matter) | PASS |
| 1e | SIGN PIN regression: ∇*∇ = −Δ_analyst gives **+12 on λ₁, +32 on λ₂** (the Δ_L sign is pinned) | PASS |
| 1c | **Δ_L(g) = 0**: ∇*∇g=0, +2Λg=12g, −2R̊(g)=−2 Ric=−12g ⇒ Δ_L g = 0 (the metric is Δ_L-harmonic on KE — known answer) | PASS |
| 1d | **Δ_L^{(1,1)}(δ*(dφ)) has ZERO (1,1) TT-residue** ⇒ Δ_L preserves the gauge image (Δ_L δ*=δ* Δ_H on Einstein bg, IN-REP) | PASS |
| 1f | **SCHUR (mandatory): Δ_L^{(1,1)} t_a = λ_L t_a with the SAME λ_L=32** for d1, d2, s01 (forced by equivariance + multiplicity-one) | PASS |

## The two STOP-gated convention controls (1c, 1d) — and why they pass

These are the controls that, if they had failed, would have meant the Lichnerowicz/Weitzenböck
convention bookkeeping was wrong (STOP rule 1, never reinterpret as physics):

- **1c — Δ_L(g) = 0.** On the Einstein KE background the metric is Δ_L-harmonic: `∇*∇g = 0` (metric
  covariantly constant), `+2Λg = 12g`, and `−2R̊(g) = −2 Ric = −12g`. The net is exactly 0 — the
  known structural answer. This pins the relative normalization of `∇*∇`, the `+2Λ` term, and the
  Weitzenböck `R̊` (in particular `R̊(g) = Ric = 6g` was cross-checked directly at Gate 0).
- **1d — gauge preservation.** A Hessian `δ*(dφ)` is pure gauge. Δ_L^{(1,1)} maps it back into the
  (1,1) gauge image (its extracted (1,1) TT-residue is ZERO). This realizes the Einstein-background
  identity `Δ_L δ*ω = δ* Δ_H ω` IN-REP on the certified objects.

## The Schur check (1f) — the mandatory multiplet control

`Δ_L^{(1,1)}` acts as a SCALAR on the λ=12 (1,1)-Hermitian multiplet: `Δ_L^{(1,1)} t_a = λ_L t_a` with
the SAME constant **λ_L = 32** for three independent single-generator residues (d1, d2, s01). This is
forced by su(3)-equivariance + the Boucetta multiplicity-one (the multiplet is irreducible); a
deviation would be an engine bug. The Schur scalar λ_L = 32 is the input to Gate 2 (`ε = λ_L − 12 =
20`). The eigen-identity itself is KINEMATICS (trap #17) — the verdict objects are the COEFFICIENTS
(c(M), the norm, ε), never the Schur identity.

## Scope fence (binding, verbatim)

This is the deformation-complex DICTIONARY of a FROZEN imported geometry. No dynamical metric, no
selection law, no κ. LIVE = "the tensor sector's source data closes in canonical form" — a DICTIONARY
fact, not a dynamics fact. No Einstein-equation / Newton-constant / G=κT / dark-matter / geodesic
language; frozen FS geometry USED not derived; the v18/v20 MM corpse stays buried; OP² priced only.
Does NOT retract v17–v21 (Block-C statements; v32 is the strictly weaker upstream dictionary).
