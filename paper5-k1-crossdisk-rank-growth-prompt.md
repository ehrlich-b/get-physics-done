# Paper 5 — K1 cross-disk rank-growth (does hereditary spectrality FORCE unbounded hidden rank, killing the ℓ⁴ tower — or does it close at finite rank?)

## TASK TYPE
Settle ONE specific claim (**CLAIM XD-GROWTH**, §0), prove-or-disprove, with a decision tree.
This is the **analytic decider** for K1 — the single gate of the Paper-5 genericity route (§19 of
`~/repos/blog/research/paper5-virtuous-loop-three-joints.md`). Two campaign sessions reduced K1 to
exactly this analytic question; the numerics are confirmed undecidable (they decelerate, §1). This
prompt is the sharpened successor of `paper5-genericity-k1-l4-composability-prompt.md` (which asked
the *level-0* "does any composite exist" question — now answered: below dim 13 NO, above 13 a
hybrid/classical-faced weak composite probably exists but is off-family). The live question is the
**hereditary** one: must an in-family ℓ⁴ self-composite grow hidden rank without bound?

Anti-glaze. Exact arithmetic (ℚ / algebraic) wherever possible. Ground every claim or tag it.

---

## 0. The one claim to settle

> **CLAIM XD-GROWTH.** Let τ ≠ σ be two distinct *close* legal Bell frames of the Niestegge rank-2
> ℓ⁴ qubit (frame manifold in §2.2). In any hereditary level-1 self-composite (§2.4), hereditary
> spectrality of **all** cross-disk differences D = p − q (p a disk atom of frame τ, q of frame σ)
> forces the cross-kernels to be bounded below:
>
>   **max( ‖K_{τσ}^{st}‖_{Y→Y} , ‖K_{στ}^{ts}‖_{Y→Y} ) ≥ f(P_{τσ}) > 0**
>
> for some strictly positive function f of the inter-frame overlap P_{τσ}, at every same-hidden-block
> pair (s, t). (‖·‖_{Y→Y} is the true ℓ^{4/3}→ℓ^{4/3} operator norm on 2×2 kernels.)

Prove it or disprove it.

- **PROOF (the wanted outcome — forced selection).** XD-GROWTH TRUE kills the orthogonal-block
  "vanishing trick" (setting all cross-kernels K = 0, which otherwise satisfies every box — §2.4).
  Combined with (i) compactness of the legal-frame curve and (ii) the banked m = 2 no-sharing
  theorem (§2.3), a continuum of 2-D hidden planes that can never be mutually orthogonal AND can
  never coincide forces **hidden rank to grow without bound** ⟹ **no finite-dimensional hereditary
  ℓ⁴ self-composite exists** ⟹ **hereditary-K1 FALSE** ⟹ the ℓ⁴ rival admits no in-family record
  tower ⟹ the genericity package survives its gate = **quantum selection is forced.** GRADE the
  compactness step (ii) honestly — it is currently [ARGUED], not proved; XD-GROWTH alone is the
  crux but not by itself the whole kill. Deliver both: the theorem, and an explicit statement of
  what compactness still owes.

- **DISPROOF = the PRE-REGISTERED KILL (report as the route's death — do NOT soften).** If instead
  the cross-kernels can all be driven to zero (or below cap) while every cross-disk difference stays
  spectral — i.e. a **bounded-rank** hereditary kernel {H_{τ,s}, G_{τ,s}} works on dense frame
  samples — then exhibit/characterize it. If that bounded-rank kernel admits an exact closed form
  that **recursively reproduces itself at level 2** (Codex "T4 flip": the generated faces ν(p,q) are
  again ℓ⁴ disks of the same kernel), then a genuine hereditary ℓ⁴ tower exists ⟹ **hereditary-K1
  TRUE** ⟹ the ℓ⁴ rival out-masses ℂ in the B-histories measure ⟹ **the §19 genericity route is
  DEAD, with no further escapes.** Report this loudly and plainly as the death of the route. Do not
  move goalposts, do not relabel it "conditional." (This honesty guard is Bryan's binding
  instruction: pursue the forced-selection outcome as hard as honestly possible, and if the math
  says the route dies, say so.)

Both branches are decisive. This is the whole ballgame for the genericity route.

---

## 1. Why this is the question (context — read once)

**Program stack.** Paper 5 derives complex quantum theory from a self-modeling fixed point, but as
proven it is a **two-import conditional characterization** (self-duality → Jordan; a central
imaginary unit / local tomography → complex), with *forcing* closed off by the Conservation No-Go
(§18). The live upgrade is **§19: the B-histories-mass** — axiom B read as a literal 1/|Aut|
groupoid measure over record-towers, under which ℂ is the unique "B-critical" type (net exponent ≡
+1 at every tower depth), scoped to simple EJAs with in-family towers. Everything hinges on one
threat: **if the non-EJA Niestegge ℓ⁴ qubit (finite automorphism group) admits in-family
record-towers, those towers out-mass ℂ and the whole route collapses.** That threat is **K1**.

**What the campaign established (banked; §2.3).** The ℓ⁴ qubit provably cannot self-compose
spectrally below dimension 13; its real cousin, the rebit, does it at dimension 10 = M₄(ℝ), sitting
*exactly* on every threshold the ℓ⁴ model misses. Above dim 13 a *weak* composite probably exists,
but its Bell faces come out classical (segments), not ℓ⁴ disks — a **hybrid**, off-family. Under the
adopted **hereditary reading** (a tower must be ℓ⁴ all the way down — Def-1(iv) given a composability
job), a hybrid does not count. So the surviving question is purely: **can a strictly ℓ⁴-faced
(hereditary) self-composite exist in finite dimension?**

**Why it is now analytic, not numeric.** The hereditary demand *measurably* costs hidden rank:
level-1 feasibility gives a confirmed prefix m*(n = 4) = 8, m*(n = 8) = 11, m*(n = 12) = 12 (n =
number of sampled frames; both starvation axes; true ℓ^{4/3} norms; witnesses brute-force verified)
— roughly **double** the level-0 saturation of ≤ 5. BUT the growth **decelerates** (log fit beats
linear; increments +3 then +1), and dense cells at n = 16, 20 are unresolved-descending. The
numerics **cannot** distinguish unbounded growth (forced selection) from saturation near 13 (route
dead). The decision therefore rests on the **analytic cross-disk equality mechanism** below — which
is exactly CLAIM XD-GROWTH.

---

## 2. The objects (self-contained — the solver has no other context)

### 2.1 The ℓ⁴ qubit and its dual
The Niestegge rank-2 system (Niestegge 2024, arXiv:2208.07135): state space is the ice-cream cone
over the 2-D **ℓ⁴ disk**; the effect/norming ball is the dual **ℓ^{4/3} disk**. Write
- **X = ℓ⁴₂** (state ball, ‖·‖₄), **Y = ℓ^{4/3}₂** (effect ball, ‖·‖_{4/3}), dual pairing ⟨x, y⟩.
- **J(y) ∈ X** = the unique norming state of a boundary effect y (the ℓ⁴/ℓ^{4/3} duality map,
  gradient of ‖·‖_{4/3}); likewise norming effects of boundary states. These are the "sharp"
  directions of the quartic ball.

Key hardness fact (banked, [CERTIFIED]): the maximal correlation over legal pairs is
**τ = 1/(√3 · 2^{1/4}) ≈ 0.485492 < ¾**. Consequence: the ℓ⁴ qubit has **no sharp (rank-1) Bell
atoms** — every correlated spectral resolution must use rank-2 flat units, and heredity then forces
each such unit's face to be a full ℓ⁴ disk (fat face). *This is why heredity bites ℓ⁴ and only ℓ⁴*
(the p = 2 rebit escapes via sharp rank-1 Bell atoms; §6 control).

### 2.2 Legal Bell frames (closed form — banked, [PROVED])
The legal Bell frames form the swap-symmetric rational curve (plus one-sided D₄ images):
- attainment pair v_s ∝ (1, s³), w_s = S v_s (S the swap), s a rational parameter;
- interpolant **T_s = √(1 + s⁴)/(1 + s² + s⁴) · [[1 + s², s], [s, 1 + s²]]**, with
  **‖T_s‖_{4/3 → 4} = 1** and norm attained exactly on {±v_s, ±w_s};
- product-sector cross-transition data:
  **A_{τσ}^{st} = ¼ + (st/8) · T_τ(E_σ)**, with the correlation P_{τσ} ≤ 2 and equality only when
  σ = τ (same frame). P_{τσ} is the natural inter-frame overlap; f in CLAIM XD-GROWTH is a function
  of it.
(Scripts: `k1_frame_manifold.py`, `k1_rank_global.py`.)

### 2.3 Banked ledger — DO NOT RESPEND (proofs filed; use as lemmas)
- **[PROVED, exact] m = 2 two-frame no-sharing.** With G_i = ½(H_iᵀ)⁻¹, V_ij = H_iᵀG_j satisfies
  V_ij·V_ji = ¼I identically ⟹ 1 ≤ ½ + P_ij·P_ji/8 ⟹ P_ij·P_ji ≥ 4 ⟹ both = 2 ⟹ i = j. **Two
  distinct legal frames can never share a single 2-D hidden block.** (Attainment strictness
  sympy-verified via the T_s closed form.)
- **[CERTIFIED] τ = 1/(√3·2^{1/4}) < ¾** (§2.1). Kills correlated rank-1 atoms and the dim-10
  non-degenerate case by pigeonhole.
- **[PROVED/CERTIFIED, assembled] below dim 13:** no ℓ⁴ spectral self-composite (m = 1 rank-2-Gram
  kill; m = 2 theorem; m = 3 breakpoint; dim-11 is [ARGUED]). **Control: the rebit composes at dim
  10 = M₄(ℝ), exactly on every threshold** (its Bell atoms are points; τ_rebit = ½).
- **[COMPUTED] level-0 (flat-Gram, box caps only): m* saturates ≤ 5** (no necessary-condition kill
  above dim 13 — this is why the *weak* composite probably exists).
- **[COMPUTED, bankable] level-1 (hereditary disk faces): prefix m* = 8, 11, 12** (§1); decelerating;
  numerically undecidable at the asymptote. This prompt decides the asymptote analytically.

### 2.4 The hereditary level-1 self-composite (the arena — Codex reply_009/010, exact)
For each legal frame τ and sign s = ±, the flat unit P_{τ,s} carries an internal ℓ⁴ **disk** of
atoms varying only in hidden directions. With hidden matrices H_{τ,s}, G_{τ,s} ∈ ℝ^{m×2}:
- **face atoms:** a_{τ,s,y} = ½ P_{τ,s} + H_{τ,s} y, ‖y‖_{4/3} = 1;
- **face carriers:** ω_{τ,s,x} = ω⁰_{τ,s} + G_{τ,s} x, ‖x‖₄ = 1, with ω⁰_{τ,s} carrying
  product-sector correlation s·T_τ;
- **forced same-frame equalities** (each face = a scaled canonical ℓ⁴/ℓ^{4/3} duality, NOT boxes):
  **G_{τ,s}ᵀ H_{τ,s} = ½ I₂**, **G_{τ,s}ᵀ H_{τ,−s} = 0**. (These force m ≥ 4 per frame by rank —
  control C1.)
- **cross-frame boxes** (τ ≠ σ), positivity of all product⊕hidden effects:
  0 ≤ A_{τσ}^{st} + xᵀ K_{τσ}^{st} y ≤ 1 for ‖x‖₄ ≤ 1, ‖y‖_{4/3} ≤ 1, where
  **K_{τσ}^{st} = G_{τ,s}ᵀ H_{σ,t}** — equivalently the operator-norm cap
  **‖K_{τσ}^{st}‖_{ℓ^{4/3}→ℓ^{4/3}} ≤ min(A_{τσ}^{st}, 1 − A_{τσ}^{st})**.

**The vanishing trick (the thing XD-GROWTH must kill):** K_{τσ}^{st} = 0 always satisfies the boxes.
So box-feasibility alone never forces rank growth; cross-kernels can vanish. The NEW constraint that
might forbid vanishing is cross-disk **spectrality**:

**The cross-disk generated-face condition (Codex reply_010, exact — the crux).** For any two disk
atoms p = a_{τ,s,y} and q = a_{σ,t,z} with norming states J(y), J(z), the ambient cross-transitions
are α = A_{τσ}^{st} + J(y)ᵀ K_{τσ}^{st} z and β = A_{στ}^{ts} + J(z)ᵀ K_{στ}^{ts} y. **Spectrality of
D = p − q forces a rank-2 projective face containing both atoms; under heredity that face must
itself be an ℓ⁴ disk** ν(p, q): there exist internal directions r, u ∈ ∂Y, maps H_ν, G_ν, unit R_ν
with
- ½ R_ν + H_ν r = p, ½ R_ν + H_ν u = q, G_νᵀ H_ν = ½ I, i.e. after eliminating the center
  **H_ν(r − u) = p − q**,
- and its *internal* ℓ⁴ transition values must **match the ambient ones**:
  **α = (1 + J(r)·u)/2** and **β = (1 + J(u)·r)/2**.

Anchors (for the σ → τ perturbation): at coincident frames (σ = τ) the within-frame equality forces
**K_ττ = ½ I** (NOT zero); the generated faces sweep a **4-parameter continuum** (one per cross-disk
atom pair (y, z)) versus level-0's 1-parameter frame curve. If K_{τσ} = K_{στ} = 0, then (α, β) are
pinned by the product bases A_{τσ}, A_{στ} alone — **constant in (y, z)** — while the interpolation
H_ν(r − u) = p − q makes the required internal (r, u) vary over the full 4-parameter family. The
theorem is whether that constancy-vs-sweep tension is a genuine contradiction.

---

## 3. The forcing to attempt FIRST (make-it-fit — steelman mandate)

Before settling for either verdict, try to PROVE XD-GROWTH via the σ → τ perturbation:

> With K_{τσ} = K_{στ} = 0 (the vanishing trick), the ambient transitions α, β are constants fixed by
> product-sector data. The generated ℓ⁴ face ν(p, q) must simultaneously (a) interpolate the vector
> difference p − q via H_ν(r − u) = p − q as (y, z) sweep the 4-parameter cross-disk family, and (b)
> reproduce those *constant* α, β as its internal transitions (1 + J(r)·u)/2, (1 + J(u)·r)/2. Show
> the ℓ⁴-disk internal transition map (r, u) ↦ ((1 + J(r)·u)/2, (1 + J(u)·r)/2) **cannot be constant**
> on the constraint surface H_ν(r − u) = p − q as p − q ranges over the family — hence K = 0 is
> impossible, hence ‖K‖ ≥ f(P_{τσ}) > 0.

Concrete sub-questions to settle this (exact arithmetic):
1. **Realizable-range check.** For fixed close τ, σ, is the constant product-only value of α (at K =
   0) even inside the set of internal transitions {(1 + J(r)·u)/2} realizable by *some* (r, u)
   interpolating a given p − q? If product-only α exits that realizable set for some cross-disk pair,
   XD-GROWTH is immediate (spectrality is unsatisfiable at K = 0).
2. **Rigidity / dimension count.** Parametrize the constraint surface H_ν(r − u) = p − q. Count
   degrees of freedom vs the number of matching equations α = (1+J(r)·u)/2, β = (1+J(u)·r)/2 across
   the 4-parameter family. Is the system overdetermined at K = 0? A clean rank/Jacobian argument at
   σ = τ (where everything is explicit: K_ττ = ½ I, ν = the frame's own disk, transitions match
   identically) extended by continuity to close σ ≠ τ would prove f(P_{τσ}) > 0 for P_{τσ} near max.
3. **Lower bound f.** If forced nonzero, extract an explicit f(P_{τσ}) (even a crude positive bound)
   — needed for the compactness step to conclude unbounded rank.

The make-it-fit hunt routes through already-banked results: you do NOT need to re-derive the frame
manifold or the m = 2 theorem — use them as lemmas (§2.2, §2.3).

---

## 4. The decider — run BOTH tracks (Track A primary, Track B cross-check)

**Track A — analytic (primary).** Execute §3 in exact arithmetic (sympy). The crux computation is
local: expand around coincidence σ → τ, where K_ττ = ½ I is forced and the generated face is the
frame's own disk (transitions match identically). Perturb σ = τ + δ. Decide whether the leading
order in δ forces ‖K_{τσ}‖ ≳ c·|δ| > 0 (⟹ TRUE, with f(P) vanishing only as σ → τ, harmless for
compactness) or admits a consistent K = O(δ²)/K = 0 solution (⟹ toward FALSE). Keep every norm the
**true ℓ^{4/3} norm** — the spectral proxy differs by a factor in [0.84, 2^{1/4} = 1.189] and WOULD
flip verdicts.

**Track B — numeric level-2 probe (cross-check / hedge).** Extend `k1_tower_level1.py` to a **level-2
encoding**: add generated-face variables ν(p, q) for adjacent sampled frames and sampled atom pairs,
with the equalities of §2.4, and test **bounded-rank feasibility** as n (frames) and the atom-pair
sample density grow. Read out: does required rank keep climbing past the {8, 11, 12} prefix, or does
a bounded-rank kernel satisfy the level-2 equalities on dense samples (the FALSE signal)?

**PRE-REGISTER controls before running Track B (this campaign was burned twice by skipping this):**
- **Coincident-frame cell must reproduce K = ½ I** and the generated face = the frame's own disk. A
  run that fails this is discarded wholesale.
- **Iteration-scaling discriminator on EVERY boundary cell:** residual collapsing under 4× warm-
  started iterations = slow-feasible; flat plateau with nit → 0 = infeasible. Never read a verdict
  off a single iteration budget.
- **p = 2 control must stay vacuous/feasible** (rebit closes through the shared Y⊗Y direction via
  sharp rank-1 Bell atoms). *A proof or a solver that also kills p = 2 is mis-normalized* — the whole
  mechanism must exploit the ℓ⁴ strictness (τ < ¾, no sharp Bell atoms), which p = 2 lacks (§6).

Numeric anchor for both tracks: the confirmed prefix {(n=4, m*=8), (n=8, m*=11), (n=12, m*=12)},
decelerating.

---

## 5. The pre-registered kill — explicit (honesty guard, binding)

If Track A finds a consistent K = 0 (or below-cap) solution keeping all cross-disk differences
spectral, and/or Track B finds a bounded-rank kernel feasible on dense samples:
1. **Exhibit the bounded-rank kernel explicitly** ({H_{τ,s}, G_{τ,s}} as functions of the frame
   parameter, the rank at which it closes).
2. **Test the level-2 self-reproduction (T4 flip):** are the generated faces ν(p, q) again ℓ⁴ disks
   of the SAME kernel (does the construction recurse without new rank)? If yes → a genuine hereditary
   ℓ⁴ tower exists.
3. **Report as death:** hereditary-K1 TRUE ⟹ the ℓ⁴ rival admits in-family towers ⟹ it out-masses ℂ
   in the B-histories measure ⟹ **the §19 genericity route is DEAD.** State this plainly. Do not
   hedge to "conditional," do not invent a new escape clause. (An honest death here is worth more
   than a laundered survival — it retires the genericity route and sends Paper 5 back to its
   two-import floor cleanly.)

---

## 6. Guards (anti-glaze / anti-thrash — mandatory)
- **True ℓ^{4/3} → ℓ^{4/3} operator norms only.** The spectral proxy would have flipped level-1
  verdicts (n = 8 witness worst box: −2.3e-7 true vs +0.047 spectral). Ratio range [0.84, 1.189].
- **Pre-registered controls; discard on control failure.** A feasibility run whose control cell fails
  is thrown out entirely, not patched (the Nelder-Mead table died this way).
- **The p = 2 strictness check is load-bearing, not decorative.** The entire kill mechanism must use
  τ < ¾ ⟹ no sharp ℓ⁴ Bell atoms ⟹ fat faces. If your argument does not visibly consume this
  strictness, it is either wrong or mis-normalized (it would also kill the rebit, which composes).
- **Do NOT conflate the level-0 and level-1/2 problems.** Level-0 (box caps) saturates ≤ 5 and proves
  nothing above dim 13; the whole content is the level-1 equalities + the level-2 cross-disk
  spectrality. A "kill" that only uses boxes is a starvation artifact.
- **Exact arithmetic** (ℚ / algebraic) for the σ → τ expansion and any orbit/norm computation; the
  quartic ℓ⁴ ball is semialgebraic — pursue rational/symbolic witnesses.
- **DEFLATION vs SURRENDER.** Proving XD-GROWTH FALSE with an explicit bounded-rank recursive kernel
  is a real result (the pre-registered kill — deliver it as death). *Failing to prove XD-GROWTH TRUE*
  is NOT the same as proving it FALSE — if you can neither force nonzero K nor exhibit a closing
  kernel, return **BLOCKED** with the precise missing lemma, do not fake either verdict.
- **Compactness is [ARGUED], not proved.** Even a clean XD-GROWTH TRUE does not finish the kill until
  the "compact legal curve + f > 0 + m = 2 no-sharing ⟹ unbounded rank" step is written out. State
  what it still owes.

---

## 7. Citations / artifacts (verify before relying)
- **Deep note (THE record):** `~/repos/blog/research/paper5-virtuous-loop-three-joints.md` §19.15–§19.21
  (campaign session 2), §19.20 (the cross-disk formulation narrative), §19.9 (the decider package).
- **Handoff brief:** `~/repos/blog/research/qm-genericity-review/HANDOFF-K1-OPUS.md` (ledger + both tracks).
- **Codex channel replies:** `~/.codex-channels/k1-composability/reply_009.md` (level-1 feasibility,
  T1–T4), `reply_010.md` (corrected p = 2 control + the cross-disk forced-frame condition = CLAIM
  XD-GROWTH's exact origin).
- **Scripts:** `~/repos/blog/research/qm-genericity-review/k1_frame_manifold.py`, `k1_rank_global.py`,
  `k1_m3_feasibility.py` (sympy exactness), `k1_tower_*.py` (level-1 suite — extend for Track B).
- **Predecessor prompt (superseded):** `paper5-genericity-k1-l4-composability-prompt.md` (level-0
  existence question).
- Niestegge 2024, arXiv:2208.07135 (the rank-2 ℓ⁴ qubit; Def-1 model, non-self-dual, non-EJA).
- Paper under test: `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` — Def-1 at 357–376;
  spectrality/compression grade at 395–424.

---

## 8. Output
- A definite verdict on **CLAIM XD-GROWTH: TRUE / FALSE / BLOCKED.**
- **If TRUE (forced selection):** the σ → τ rigidity proof (§3), the explicit lower bound f(P_{τσ}) >
  0, and a precise statement of what the compactness → unbounded-rank step still owes ([ARGUED]).
  Physical one-liner for the report: *ℓ⁴ frames provably can't share one hidden Bell direction, and
  facing two frames' fat faces off forces new hidden bookkeeping every time — the compounding never
  terminates, so the ℓ⁴ rival has no in-family memory tower, and quantum is the only type that can
  remember its own history: selection forced.*
- **If FALSE (pre-registered kill):** the explicit bounded-rank recursive kernel (§5), the level-2
  self-reproduction check, and the plain report that the genericity route is DEAD. No softening.
- **If BLOCKED:** the precise missing lemma and the cheapest computation that would settle it.
- File the result into `paper5-virtuous-loop-three-joints.md` as a new subsection under §19, update
  the handoff brief, and propagate per CLAUDE.md (STATE.md / GRAPH.md / memory). **NO SSOT flip
  without Bryan** (P5 stays CONDITIONAL-SYNTHESIS regardless; this decides the genericity *upgrade*,
  not the floor).
