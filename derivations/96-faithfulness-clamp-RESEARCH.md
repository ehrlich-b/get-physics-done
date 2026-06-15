# Phase 96 / v36.0-candidate — RESEARCH: Does FIELD faithfulness carry a derivative term? (the one un-run clamp gate)

_Orchestrator-staged grounding bible for the no-web gpd-executor. Source prompt:
`~/repos/blog/research/gr-from-h3o/faithfulness-clamp-prompt.md` (registered by Bryan
2026-06-15). Exact over ℚ. Built from certified objects (v33 Δ_L, v34 Γ=∫R√g, v35 CP²
engine). This is the SINGLE residual gravity gate: every other angle (fiber dead across
six kinds; variety extremize FORCES-NOTHING v33; induce CLOSES-CONDITIONAL v34;
entanglement DEAD-FISHER v35) reduces to the clamp below._

---

## §0 — BOTTOM LINE + VERDICT TAXONOMY

**The clamp = state-fp ⟹ metric-fp:** the self-modeling-faithful matter profile is a
critical point of the gravitational action its own fluctuations induce —
`δF/δM = 0 ⟺ δΓ/δM = 0`. We HAVE Γ (v34, slot 94: clean `a₁ ∝ ∫R√g`). The open object
is `F[M(x)]` = the field-level self-modeling **faithfulness functional**.

**The asymmetry that defines the whole gate.** `δΓ = G_μν − κT_μν` is a *curvature*
object — SECOND-derivative-in-the-base (a Lichnerowicz/Laplacian operator on the profile).
For the faithful profile to extremize it, `δF` must carry MATCHING base-derivative
structure. So the entire clamp rides on ONE question (Gate 0, the decisive gate):

> **Does field faithfulness (`M(x) = φ[M](x)` on the curved variety) carry a genuine
> base-derivative term (a Laplacian/Lichnerowicz operator on `M`, SAME TYPE as `δΓ`), or
> does it collapse to the pointwise algebraic `−Tr(h²)` Fisher form that is already dead?**

**VERDICT TAXONOMY (report exactly which one, exact over ℚ):**

- **DEAD-POINTWISE (Gate 0; the skeptical prior).** The only well-defined geometry-
  respecting field extension is pointwise (or nonlocal-global-mean) — `L_F` is the algebraic
  `−Tr(h²)`-type (state-space / Fisher) operator with **no FORCED local base-derivative
  term**. Then faithfulness is structurally a different TYPE from the curvature operator
  `δΓ`, the clamp is **FALSE** (faithful ≠ Einstein-extremal), **fork A is PROVEN** (not
  merely adopted), and the 2026-06-07 "self-modeling is fiber-local" brainstorm is upgraded
  to a **theorem** (self-modeling provably cannot reach the base metric). Report the
  obstruction operator exactly.
- **DEAD-WRONG-DERIVATIVE (Gate 0 PROCEEDS → Gate 2 DEAD).** `L_F` carries a base derivative,
  but it is the harmonic-map / Dirichlet scalar Laplacian `□φ_M` (a *reproduction* functional
  gives harmonic/minimal maps — the "Dirichlet-dead reading" already flagged) — the WRONG
  TYPE vs `δΓ`'s Lichnerowicz curvature operator on the metric mode. Proceeds past Gate 0 but
  the critical points generically differ at Gate 2. Clamp FALSE, one notch sharper.
- **ALIVE (Gate 2).** `L_F` carries the RIGHT (Lichnerowicz, the v33 `ε = λ_L−2Λ = 20`
  eigentensor) derivative term AND `δF=0` and `δΓ=0` share critical points on the sourced
  mode. `state-fp ⟹ metric-fp` proved by direct computation. (Necessary-not-sufficient for
  gravity per Jaksland — see §6; it does not by itself pay Wall 2 / signature.)
- **ALIVE-THROUGH-GATE-3.** As ALIVE, plus: matching pins `κ_ind` (strong — a definite
  induced `G`; by Lovelock any local 2nd-order divergence-free rank-2 law forces Einstein+Λ)
  OR holds for all `κ_ind` (form-only — the LAW `G=κT` forced, `κ` contingent / Level-6).
- **INCONCLUSIVE.** The verdict flips between two equally-canonical field extensions of the
  φ-fixed-point. Report both and STOP (do not pick the convenient one).

**Skeptical prior = DEAD-POINTWISE at Gate 0** (§9 de-risk). NOT foregone: on the VARIETY
the matter mode `dφ_M⊗dφ_M` already lives in a Lichnerowicz/FS derivative context (v31–v34)
and v34's metric-side loop is self-consistent there — so the collapse is exactly the un-run
uncertainty. **Run it; do not assume it.** Report the truth the exact math gives.

---

## §1 — CERTIFIED OBJECTS + ENGINE API (reuse; do NOT re-derive)

Work entirely in **`h_3(ℂ)` = the C_u cut = CP²** (no octonion engine on the decisive path).
READ and REUSE these certified drivers — do not rebuild their objects from scratch (that is
what orphaned the v35 jobs):

- **`code/area_per_bit.py` (v35, certified 25/25).** The CP² Wirtinger chart `P(z)=vvᴴ/(vᴴv)`,
  `v=(1,z₁,z₂)`, `ρ=1+|z₁|²+|z₂|²`; `⟨X,p⟩=Tr(XP)`; `X#=adj(X)`; the FS metric
  `g_{ij̄}=∂_i∂_{j̄}log ρ`; `φ_M=⟨M,p⟩`; `Var_p(M)=⟨M²,p⟩−⟨M,p⟩²`; `G_M=⟨M#,p⟩−¼⟨M,p⟩²
  = Var+¾⟨M⟩²−½Tr(M²)`. **Wirtinger discipline (MANDATORY):** `z` and `z̄` are INDEPENDENT
  symbols; conjugation = the `z↔z̄` swap; NEVER call sympy `conjugate()` on them (it silently
  breaks the Kähler identity — the v35 de-risk bug).
- **`code/lichnerowicz_response.py` + `..._verify.py` (v31/v32/v33).** The matter-sourced TT
  metric mode and the Lichnerowicz operator on the variety: `Δ_L r = 32 r`, `ε = λ_L − 2Λ =
  32 − 12 = 20 ≠ 0`, `‖TT(B3)‖² = (1/30)(Tr M²)²`. **This is the base-derivative TYPE `δΓ`
  lives in** — the object `L_F` must be compared against (its eigenvalue/eigentensor is the
  ε=20 mode). Reproduce one anchor (e.g. `ε=20`) as a self-test.
- **v34 Γ harness:** `code/sakharov_variety.py`, `sakharov_gate1_a1R.py`, `indep_sakharov_checks.py`.
  Γ = the induced action with `a₁ ∝ ∫R√g`, `ε=20` FORCED, `κ_ind` FREE. v34 did the METRIC-side
  loop ONLY; the STATE-side `F` and the coincidence check are un-run — that is THIS task. Reuse
  this harness for Gate 2.
- **The φ-iteration:** `~/repos/blog/research/sm-vacuum-computation/nonlinear_iteration.py`
  (READ-ONLY reference; numpy/illustrative, do NOT import — re-encode the map exact over ℚ).
  The self-model is `ρ = R(M(ρ))` with the new measure read off a model formed from **ensemble
  expectations** `⟨l_i⟩_ρ`. Fixed point `ρ_J = det·(σ₂−1/3)`. **Faithful (no -ing) = the I/3
  center** (`det≠0`, `σ₂−1/3=0`): complete but un-differentiated, matter-free.

Matter directions (traceless Hermitian, Tr M = 0): `s01=[[0,1,0],[1,0,0],[0,0,0]]`,
`a01=[[0,-i,0],[i,0,0],[0,0,0]]`, `d1=diag(1,-1,0)`, `gen=diag(1,1,-2)`. Off-faithful test
states `X = I/3 + εM` (the v35 ground: `Var`, `G_M` genuinely vary with `p` — §9).

---

## §2 — GATE 0: THE DERIVATIVE STRUCTURE OF FIELD FAITHFULNESS (decisive)

**Object.** Promote the matter state to a FIELD `M(x)` on the variety. Write the geometry-
respecting field φ-fixed-point condition (NOT a naive pointwise copy). Linearize at the
faithful profile (`M=0`, the I/3 shell — but probe the RESPONSE on STRUCTURED `M≠0`, the
v23/v35 off-faithfulness lesson, else you hit §8.1's doubly-degenerate 0=0). Inspect the
faithfulness operator `L_F = δ(faithfulness)/δM`.

**The structural fork the executor MUST resolve (this is the whole gate).** The φ-map's ONLY
non-locality is the ensemble expectation `⟨l_i⟩_ρ`. Promoting to a field gives three — and
only three — well-defined readings of `⟨·⟩`:

1. **POINTWISE** — `⟨·⟩` taken at `x`'s own reduced state ⟹ `φ[M](x)=φ(M(x))`. `L_F` is the
   pure algebraic `−Tr(h²)`-Hessian (the Fisher/Bures form, §8.1). NO base derivative.
   = dead handle 3 (`ρ_J=0 ⟹ X∝I` or `det=0`). **COLLAPSE.**
2. **GLOBAL mean-field** — `⟨·⟩ = ∫_base` over the WHOLE base ⟹ `L_F` = (pointwise Hessian) −
   (rank-1 projector onto the global mean mode). A NONLOCAL integral operator, NOT a local
   differential operator. Still not the Lichnerowicz TYPE. Effectively dead vs `δΓ` (a local
   2nd-order differential operator). **COLLAPSE (nonlocal).**
3. **LOCAL / geometry-respecting** — `⟨·⟩` uses the variety's intrinsic FS/Lichnerowicz
   structure to average over a NEIGHBORHOOD of `x` ⟹ could yield `Δ_FS M` (a local Laplacian).
   The ONLY reading that can PROCEED. **But the decisive sub-question: is the neighborhood/
   kernel FORCED by the variety's intrinsic structure, or an inserted smoothing (fp-imported)?**

**DECISIVE NUMBER.** The coefficient of the local base-derivative term in `L_F`, computed
EXACT over ℚ on CP² from the φ-fixed-point condition ALONE (no reference to ∫R — Bug-guard 5):
- **= 0 identically** (only algebraic `−Tr(h²)` + at most a nonlocal global-mean correction)
  ⟹ **DEAD-POINTWISE**, clamp FALSE, fork A PROVEN.
- **FORCED ≠ 0** and a genuine LOCAL Laplacian ⟹ **PROCEED to Gate 1**; report the operator
  and which TYPE (Lichnerowicz-on-metric → real proceed; scalar `□φ_M` → Bug-guard-1 flag,
  routes to DEAD-WRONG-DERIVATIVE).

**BUG-GUARDS (all must be checked before any PROCEED):**
1. **DIRICHLET-TRAP.** A base-derivative that is the harmonic-map scalar `□φ_M` (a reproduction
   functional → harmonic/minimal maps) is the WRONG TYPE vs `δΓ`'s Lichnerowicz curvature
   operator. It is NOT a clean Gate-0 PROCEED — flag it and route to DEAD-WRONG-DERIVATIVE at
   Gate 2. The right type is the ε=20 Lichnerowicz tensor mode of `lichnerowicz_response.py`.
2. **IMPORTED-KERNEL.** If a local derivative appears ONLY after choosing a smoothing kernel /
   neighborhood, prove the kernel is FORCED by the variety's intrinsic FS structure, NOT an
   inserted regulator. An imported kernel ⟹ the native object collapsed and you smuggled the
   derivative ⟹ DEAD-POINTWISE.
3. **FAITHFUL-POINT-MATTER-FREE.** The faithful point is I/3 (matter-free, `ρ_J=0`); naively
   linearizing AT it gives §8.1's doubly-degenerate `0=0`. Probe the response on STRUCTURED
   off-faithful `M≠0` (so the operator is non-vacuous). This is also the v23-death tripwire.
4. **WOO / DEMON-TEST 2.0 (HARD STOP).** NO thermodynamics / horizons / coarse-graining or
   epistemic ENSEMBLE entropy. `F` is a self-consistency / fixed-point functional. The φ-map's
   `⟨·⟩` is a SELF-CONSISTENCY mean over the state's own distribution — NOT a thermodynamic
   ensemble. If the field extension requires a coarse-graining/thermal ensemble over the base
   to produce a derivative ⟹ that is woo — **flag and STOP** (and the derivative is not native).
5. **NO-CIRCULARITY.** Compute `L_F` PURELY from the φ-fixed-point condition with ZERO reference
   to `∫R` / the metric action / Γ. The comparison to `δΓ` happens only at Gate 2, independently.
   AST-guard the Gate-0 driver against importing `R`, `Ric`, `G_munu`, `Δ_L` into `L_F` itself.

---

## §3 — GATE 1: WRITE F (only if Gate 0 PROCEEDS)

Write the field faithfulness functional `F[M(x)]` whose stationarity is the geometry-respecting
field φ-fixed-point, exact over ℚ. It must NOT reduce to pointwise `ρ_J` (handle 3) or to
entropy-max (handle 1 / v35). Report `F` explicitly and its Euler–Lagrange operator.

## §4 — GATE 2: COMPARE CRITICAL POINTS (the clamp; only if Gate 1 written)

Compute `δF/δM=0` and `δΓ/δM=0` (Γ from the v34 slot-94 harness). Do they share critical points
— `F = Γ∘(M↦g)` up to a monotone reparametrization, or proportional variations on the sourced
ε=20 mode? **ALIVE** if they coincide (`state-fp ⟹ metric-fp` proved). **DEAD** if the faithful
and gravitating profiles generically differ; report the exact mismatch (e.g. the ε=20 vs
scalar-□ support split, the v17/v18 16-vs-6-style wall).

## §5 — GATE 3: DOES THE MATCH PIN κ_ind? (only if Gate 2 ALIVE)

Does `δF=δΓ` hold only at a specific `κ_ind` (pinning the free coupling by the MATCHING
condition — NOT by importing a scale; handle 2 is dead) or for all `κ_ind` (form-only)?
ALIVE-strong = `κ_ind` pinned (Lovelock ⟹ Einstein+Λ). ALIVE-form-only = the LAW `G=κT` forced
with `κ` contingent (Level-6 / Molien) — still gravity in the GR sense.

---

## §6 — FENCES (binding) + WHAT IS ALREADY DEAD (do NOT re-run)

**Three dead handles — the slot is WASTED if it re-derives any:**
1. **Entropy / MaxEnt-as-F — DEAD** (one-term tautology: `δ²S ∝ −Tr(h²)`; the missing
   geometric second term was computed away by v35 DEAD-FISHER — every FS-canonical "area" is a
   power of the SAME quantum Fisher variance, not an independent geometric term). Do not
   re-propose entropy-max as `F`.
2. **Fixed-point-SCALE handle — DEAD.** `κ_ind` via the fixed point's intrinsic scale
   (`det X*`, `Tr X*²`→`Λ_f`) fails: the faithful point is the matter-free I/3 shell
   (`Tr X²=1/3`), scale trivial. Do not pin `κ_ind` by importing the fixed-point scale.
3. **Static / pointwise `ρ_J` handle — DEAD.** Pointwise faithfulness ⟹ `ρ_J=0 ⟹ X∝I`
   (matter-free) or `det=0` (incomplete). `F` must be the FIELD condition on `M(x)`, NOT
   pointwise `ρ_J`. The naive "apply φ pointwise at every base point" reproduces this and
   trivially collapses (no derivatives) — that is the UNINTERESTING disproof, not Gate 0's
   answer. Gate 0's object is the GEOMETRY-RESPECTING field extension.

**Anti-overclaim (binding, verbatim from v33–v35).** NO Einstein / `G=κT` / gravity / Newton /
dark-matter / geodesic language as a DERIVED result; the bits↔area / induced-`G` rate is a
framework ratio, NOT Newton's G; FS is USED, not derived; signature Riemannian (**Wall 2
unpaid** — NOTHING is called gravity until signature is paid); DEAD-* and ALIVE-* are NOT
derivations of gravity. ALIVE is **necessary-not-sufficient** for gravity (Jaksland
arXiv:2005.05055) — it sits UPSTREAM of the state-fp⟹metric-fp clamp, which itself sits upstream
of Wall 2. Does NOT retract v33 (extremize), v34 (induce), v17–v21 (fiber kills), v23 (I/3
death), v35 (DEAD-FISHER). Paper 5 remains the only result in the more-than-nothing column.

---

## §7 — SELF-TESTS + NON-HARDWIRED verdict()

`verdict()` is a deterministic ladder from COMPUTED booleans (never a hardwired string). Before
the real verdict it MUST print PASS on rigged controls:
- **rigged pointwise** (a φ-map with `⟨·⟩` forced to the local state) → must return DEAD-POINTWISE.
- **rigged local-Laplacian** (a hand-built `L_F` with a genuine FORCED `Δ_FS` Lichnerowicz term)
  → must return PROCEED/ALIVE (proves the ladder CAN say alive — not rigged to kill).
- **rigged scalar-□** (a hand-built harmonic-map `□φ_M`) → must return DEAD-WRONG-DERIVATIVE
  (proves Bug-guard-1 fires).
- **two non-agreeing extensions** → must return INCONCLUSIVE.
Plus: reproduce the `ε=20` Lichnerowicz anchor and the v35 `A_ii≡Var` / `G_M=Var+¾⟨M⟩²−½TrM²`
identities (the certified-engine sanity checks). Exact over ℚ on every decisive line (sympy
`Rational`/`cancel`/`simplify`; NEVER a float in a verdict). Commit after each gate.

---

## §8 — THROUGH-LINE

v24 entropy landscape (LIVE) → v25 moment doublet → v26 source field `G_M` → v27 local balance →
v28 spinor moment → v29/v30 clock sector → v31 tensor wall OPENS → v32 dictionary (κ=1/30, ε=20)
→ v33 EXTREMIZE forces nothing → v34 INDUCE CLOSES-CONDITIONAL (gravity gap = the single
state-fp⟹metric-fp clamp) → v35 AREA-PER-BIT DEAD-FISHER (entanglement route closed) → **v36
FAITHFULNESS CLAMP: does the STATE-side `F` carry the base-derivative the clamp needs?** Every
gravity angle now points at this one operator `L_F`. DEAD ⟹ the clamp is *refuted* (fork A
proven, Paper 6 v2 ships as a genuine no-go: self-modeling provably forces QM but not gravity).
ALIVE-through-3 ⟹ the clamp dissolves by computation; the program derives the gravitational law
(first more-than-Paper-5 result).

---

## §9 — DE-RISKED GROUND TRUTH / EXPECTED STRUCTURE (orchestrator de-risk)

**Structural de-risk (done before this file; the executor must CONFIRM concretely or REFUTE):**
The φ-iteration's sole non-locality is the GLOBAL ensemble expectation `⟨l_i⟩_ρ` taken over the
STATE/measure space. On a field `M(x)` that `⟨·⟩` is a base-INTEGRAL (a global mean-field), which
linearizes to a NONLOCAL rank-1 operator (subtract the global mean mode) — **NOT a local
Lichnerowicz differential operator.** A LOCAL base-derivative term requires REPLACING the global
average with a local-neighborhood / FS-kernel average — a smoothing that is NOT present in the
φ-iteration as defined; inserting it is fp-imported (Bug-guard 2), and even then it yields the
Dirichlet-dead harmonic-map `□φ_M` (the WRONG type, Bug-guard 1), not the ε=20 Lichnerowicz
tensor operator. **Expected: DEAD-POINTWISE at Gate 0** — `L_F = (algebraic −Tr(h²)-Hessian) +
(nonlocal global-mean correction)`, decisive local-derivative coefficient `≡ 0`.

**Certified anchors to reproduce (exact over ℚ; the sanity floor):**
- `ε = λ_L − 2Λ = 32 − 12 = 20` (the Lichnerowicz mode; the TYPE `δΓ` lives in).
- v35 identities: `A_ii ≡ Var`, `G_M − (Var + ¾⟨M⟩² − ½Tr M²) ≡ 0` (symbolic over ℚ).
- §9-style off-faithful ground points (Var, G_M genuinely vary ⟹ non-vacuous off-faithful test):
  `d1@P0(z₁=1+2i,z₂=−1+i)`: `Var=1/2, G_M=−5/16`; `d1@P2(z₁=−1,z₂=2−3i)`: `Var=2/15, G_M=−13/15`;
  `s01@P0`: `Var=11/16, G_M=−17/64`; `gen@P0`: `Var=27/16, G_M=−81/64`.

**Honest reading.** The skeptical prior is robust (the φ-map carries no local differential
coupling), BUT the prompt's counter is real: on the variety the metric mode `dφ_M⊗dφ_M` already
sits in a derivative context, and v34's metric-side loop is self-consistent there. The un-run
uncertainty is precisely whether the STATE-side condition INDEPENDENTLY inherits that derivative
or whether that inheritance is the metric-side loop in disguise (circularity, Bug-guard 5).
Compute `L_F` from the φ-fixed-point ALONE; let the decisive coefficient decide.
