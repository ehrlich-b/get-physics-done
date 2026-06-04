# v20.0 closing synthesis — the gravity triangulation is sealed to four corners

**Milestone v20.0, Phase 80 (a fail-fast Gate-0 cheap kill). Verdict: `fp-imported-action`.**
Verifier-hardened HIGH (33/33 independently re-derived, exact over Q), human-ratified.

## What v20.0 ran

The single gravity computation that was **set to zero in v18 and never executed**: v18
Phase 77 used the torsion-free Levi-Civita `ω(e)` (verified `d_ω e = 0`), so no phase
had ever computed `G = κT` with **torsion ON**. v20.0 turns it on the only
non-circular way available — the chiral `V_{1/2}` spin current sourcing torsion through
the algebra's OWN intrinsic cubic coupling, the `C_{(V_{1/2})(V_{1/2})(V_0)}` block
(NOT a posited EC/Palatini action) — and runs the cheap Gate-0 kill before any
requirements/roadmap ceremony.

## What it found (at true strength, both directions)

**Torsion is real and intrinsic in shape (don't deflate).** The `C` block IS the
π_u-soldered Jordan product (bridge const **−2/3**, exact over Q): the spin current is
`to_mink(jordan(E φ, E φ))`, not an inserted bilinear. It is nonzero (G0a),
chirality-tracking (G0b — the `C_{i,i,18}=∓1/6` sign-split flips the `(β−γ)` component
under the 8↔8 flip while the timelike `(β+γ)` stays even), and every coefficient is read
from the algebra with no inserted constant (G0c.1; the AST guard fires on an injected
`κ=8πG`). **The v18 "torsion-free" reading is genuinely superseded — torsion exists and
tracks chirality.**

**But the coupling is imported (don't inflate).** The constant relating that spin
current to a geometric torsion `T^a = d_ω e^a` has weight `λ⁻¹` under the soldering
rescale `e→λe` (T linear in e / weight +1, S quadratic / weight +2) — it is dimensionful
(`1/length²`). **No `h_3(O)` invariant has negative weight**: `R[h_3(O)]^{F_4}` is the
free polynomial ring on Tr (deg 1), Tr² (deg 2), det_3 (deg 3) — all positive
(`H(s)=1/((1−s)(1−s²)(1−s³))`, the v16 RING certificate) — and the only negative-weight
escape (a det_3 quotient) is identically singular on the Lorentz block (`det_3≡0` there,
independently reproducing the v18 Phase-78 fact). So `κ=8πG` comes only with a posited
action. **G0c.2 fails → `fp-imported-action`.**

## The four corners

Three physics-side intrinsic routes to gravity from `h_3(O)`, each on a **different
tensor**, plus the EC-torsion completion — all decisive negatives, all reported at true
strength:

| Milestone | Sector / object | Verdict |
|---|---|---|
| v17.0 | symmetric / cone-Hessian (real part of the QGT) | **NONE** (curved, not Einstein-structured) |
| v18.0 | Lie–Cartan/MM connection, **torsion-free** (imaginary part) | **fp-imported-action** (G≠κT+Λg; ε not forced) |
| v19.0 | antisymmetric / `u=e_7` orientation | **fp-no-intrinsic-orientation** ((1,3) admits no compatible J) |
| **v20.0** | **Einstein-Cartan torsion (spin-sourced)** | **fp-imported-action** (shape forced, coupling imported) |

## Why this is a genuine closure, not three-with-a-hole

The v18 negative was a tensor-support mismatch (`G` on 16 components, `κT` on 6) on the
**antisymmetric** components — exactly where a spin-current contribution lives. EC torsion
sourced by `V_{1/2}` spin was the structurally-possible repair, and "torsion is algebraic
so it won't close" was explicitly forbidden as a substitute for the computation. We ran
it. The torsion is genuine and chirality-tracking — but its coupling to geometry is the
same imported gravitational scale that v18 Phase 78 already found is not fixed by the
trace form / cubic norm (`det_3≡0` on the block, here reproduced independently). **There
is no remaining un-run intrinsic route in which gravity could hide.**

This grounds the program's reading that **the complex/antisymmetric "i" (`u=e_7`) is
internal-gauge-natured and gravity is separate** (the Penrose/'t Hooft shape; converges
with Phase 76, where the Berry curvature `Im(QGT)` was the internal `so(6)=SU(4)` gauge
sector, not gravity). The independent v12/v13 det/GST/Weinberg Einstein result (which
reaches Einstein form *via* a posited N=2 SUSY closure) is not retracted — v20.0, like
v17–v19, is an intrinsic route that falls short of *forced* Einstein gravity without an
imported action.

## The v19 residual, partially addressed

v19.0 logged but did not chase: "can the discrete `V_{1/2}` chirality datum
(`C_{i,i,18}=∓1/6`) fix the orientation where a continuous `J` cannot?" v20.0 shows the
discrete datum **does** source a genuine chirality-tracking torsion (it is not
orientation-trivial — G0b passes on exactly that datum), but the coupling to geometry is
still imported. Whether the 8↔8 labeling is itself `F_4`/Spin-gauge-swappable remains the
open sub-question; it is moot for the gravity verdict, since even a physical chirality
datum cannot supply the missing dynamical coupling.

**Deliverables:** `code/cartan_gate0_torsion.py`, `derivations/80-ec-torsion-gate.tex`,
`derivations/80-triangulation-note.md`, `derivations/80-GATE-0-VERIFICATION.md`.
