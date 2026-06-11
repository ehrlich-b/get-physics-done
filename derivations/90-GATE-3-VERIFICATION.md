# Phase 90 (v30.0) — GATE 3 INDEPENDENT VERIFICATION (the decisive fork gate)

**gpd-verifier adversarial re-derivation. VERDICT = DEAD — CONFIRMED (HIGH).**
Driver: `code/clock_connection_indep_check.py` (a THIRD code path, 10/10 PASS, ~160 s, exact
over Q / Q(t) / Q(eta)). octonion_algebra BANNED; shared certified arena RL / vMD / vMD.V24.

---

## What was verified, and by which independent method

| # | Check | Method (distinct from both drivers) | Result |
|---|---|---|---|
| C1 | K_face⁽²⁾ = −(9/2)⟨M,p⟩·tl(C_pM) | **2×2 reduced-density block** ρ_face (rows/cols {1,2}, e₇→i), ε²-coeff route | reproduced (symbolic cut M) |
| C2 | χ = −(9/2)⟨M,p⟩⟨M,D⟩ | **opposite orientation e₇ → −i** (conjugate Fano sign) 3×3-complex rep | χ = −6 in engine, formula, AND e₇→−i rep |
| C3 | F⁽²⁾ = raw da − Bott background | **DIRECT mixed exterior derivative** on a generic complex 2-surface (own frame seeds) | raw da = background → F_sub = 0 |
| C4 | a⁽²⁾ = dχ EXACT (the load-bearing fact) | **sqrt-free octonion engine** along all 4 cut families, symbolic in t (no truncation) | ∇D=0 and a−dχ=0 identically |
| C5 | bug A reproduced | complex vs real param declaration | leak vs clean confirmed |
| C6 | nested-∇ Bott vs genuine da | both computed in the same GS gauge | EQUAL (2201/6930); both the FS holonomy |
| C7 | verdict() non-hardwired; guard 5 | feed both branches; χ constructive | DEAD/LIVE both reachable; χ independent of v29-H |
| C8 | DEAD is contingent (anti-vacuity) | **exact engine**: break ∇D=0, measure exactness defect | parallel→0 (DEAD); broken→nonzero poly in wᵢ (LIVE) |

---

## The decisive computation — and the subtlety I uncovered

The verdict object (clock_connection.py:22–25) is the **background-subtracted** curvature
F⁽²⁾ = d(a_X⁽²⁾) − ⟨R(v,w)𝒦, D⟩ (trap #13: the canonical transport's own Fubini–Study
holonomy must be subtracted). I computed the pieces **directly** on a generic complex 2-surface
and found a sharper picture than a naive "da = 0":

1. **The face/complement bundle has genuinely NONZERO Fubini–Study / Bott curvature.** In a
   concrete Gram–Schmidt gauge the raw exterior derivative of the 1-form is **da = 2201/6930 ≠ 0**
   (dense M); **da = −3404/385 ≠ 0** (a second M). trap #13 is real, not vacuous.

2. **raw da EQUALS the canonical-transport background** ⟨[∇_s,∇_t]𝒦, D⟩ **exactly** (2201/6930 ==
   2201/6930; −3404/385 == −3404/385). Hence the **background-subtracted F⁽²⁾ = da − background = 0**.

3. This subtraction is in fact a **structural identity for any in-face (V₀) field** (I checked
   the matter clock, a frozen face field, a wrong-moment-power field, and the unscaled rate — all
   give raw da = background, F_sub = 0). So the subtracted-curvature statement, while true, is
   **not the discriminating content**. The genuinely contentful, non-vacuous result is:

4. **EXACTNESS.** With the canonical PARALLEL reference D (∇D=0), the clock-drift 1-form is exact,
   **a_X⁽²⁾ = dχ**, χ = ⟨𝒦,D⟩ = −(9/2)⟨M,p⟩⟨M,D_p⟩, because a(v) − ∂_v χ = −⟨𝒦, ∂_v D⟩ = 0 by
   Peirce orthogonality (𝒦 ∈ V₀, ∂_v D ∈ V_{1/2}). Therefore ∮ a = 0 (Stokes) and there is **no
   matter-forced holonomy**. Verified EXACTLY in the sqrt-free engine along all four cut families,
   symbolic in t, with **no truncation** (C4) — the cleanest, bug-A-immune statement.

### Reconciling the truncation behavior (a caveat worth recording)

A low-order (O(η²)) read of "raw da" returns **0** — because the bundle's Bott curvature first
enters ∇D at O(η²). My convergence study (build-order 3,4,5,6) shows raw da stabilizes at
**2201/6930** for build-order ≥ 4. So the executor's/research note's phrasing "naive da = 0" is an
**O(η²) artifact**, not the honest raw curl. This does **not** change the verdict: the executor's
*logic* proves F⁽²⁾ = d(dχ) = 0 from the exactness a=dχ (it never relies on a numerically-computed
raw da), and that exactness is rigorously confirmed here. The research-note sentence "the Bott
background ⟨R𝒦,D⟩ = naive da = 0 … while ⟨R·Y,D⟩ ≠ 0 for a generic face field Y" is **imprecise**:
in my generic-surface gauge BOTH ⟨R𝒦,D⟩ and ⟨R·Y,D⟩ are nonzero (and each equals its own raw da).
The load-bearing claim (exactness ⇒ DEAD) is unaffected and confirmed.

---

## Bug-A and bug-B probes (the two real bugs this run had)

- **Bug A (complex params leak antiholomorphic conj-derivatives).** Reproduced: with an
  *undeclared* `s`, dP/ds carries `Derivative(conjugate(s), s)`; with `s` real it is clean and
  rational (C5). The driver declares `s,t = symbols("s t", real=True)` (clock_connection.py:436).
  I additionally found that the **sqrt normalization** of a Gram–Schmidt phase reference hides the
  SAME failure mode (sympy's sqrt introduces an aux var treated as complex, leaking
  `Derivative(conjugate(_xi),_xi)`). The bug-A-immune route is the **sqrt-free octonion engine**
  (`D_along`), which is exactly what C4/C8 use — and what makes them the decisive checks.

- **Bug B (nested-∇ "Bott" object is nonzero while da of the 1-form is 0).** Resolved with a
  precise answer: on a generic 2-surface the nested commutator ⟨[∇_s,∇_t]𝒦, D⟩ = 2201/6930 and
  the honest raw da = 2201/6930 are **EQUAL** — they are the same object (the bundle's intrinsic
  FS holonomy). The earlier "da = 0" was the O(η²) truncation. The verdict object subtracts this
  background, giving 0. The genuinely curvature-free statement is the gauge-invariant ∮a = 0
  (exactness), proven in the canonical parallel gauge.

---

## Adversarial attempts to overturn DEAD — all failed

| Attempt | Outcome |
|---|---|
| Direct da on a generic complex 2-surface (try to find nonzero matter curvature) | raw da ≠ 0 but = background ⇒ subtracted F = 0; exactness ∮a=0 holds |
| Higher truncation order (3,4,5,6) to expose a hidden term | da stabilizes; equals background at every order ≥ 4; F_sub = 0 |
| Opposite complex orientation e₇ → −i | χ = −6 unchanged; verdict invariant |
| Matrix-log clock −2 log(2ρ) instead of the Taylor clock | differs by a V₀ face term only ⇒ still exact ⇒ DEAD robust |
| Generic / wrong-power / unscaled face fields | all give exact-after-subtraction; none overturn |
| Bug-A pollution (complex params, sqrt aux var) | isolated; the sqrt-free engine result is clean and = DEAD |

**Contingency (C8, exact engine):** breaking ∇D=0 (non-parallel D′) makes the exactness defect a
**nonzero polynomial in the matter components wᵢ** (e.g. at t=1/3:
`162792 w₀²/78125 + 575757 w₀w₁/156250 + 129276 w₀w₇/78125 + 441693 w₁²/312500 + 229824 w₁w₇/78125 − 172368 w₇²/78125`),
so a is no longer exact ⇒ that case would read **LIVE**. DEAD is therefore **contingent on the
derived canonical parallel transport** — not a hardwired or universal artifact.

---

## Key numbers reproduced

| Quantity | Value | How |
|---|---|---|
| χ(E₁₁), M = diag(2,−1,−1)+cut | **−6** | engine, formula, AND e₇→−i rep all agree |
| ⟨M,E₁₁⟩ | 2 | the (1,1) diagonal entry |
| ⟨M,D⟩ | 2/3 | 2× the e₇-coefficient (1/3) of the x₁ entry |
| raw da / Bott background (dense M, generic surface) | **2201/6930** (equal) | direct mixed deriv = nested commutator |
| background-subtracted F⁽²⁾ | **0** | da − background, both M |
| a − dχ (parallel engine D, all 4 families) | **0** identically in t | the load-bearing exactness |

---

## Confidence

**HIGH.**

**DEAD — CONFIRMED.** The clock-drift 1-form a_X⁽²⁾ is EXACT (a = dχ, χ = −(9/2)⟨M,p⟩⟨M,D_p⟩),
proven exactly and independently (2×2 reduced-density K⁽²⁾; opposite-orientation χ; sqrt-free
engine ∇D=0 and a−dχ=0 along all four cut families with no truncation). Hence ∮a = 0 and matter
forces NO form-level curvature on the gluing U(1); the v28 class-only ceiling stands.

Caveat recorded (does not affect the verdict): the bundle's Fubini–Study/Bott curvature is
genuinely nonzero, so the "naive raw da" is 2201/6930 (not 0 — the "0" is an O(η²) truncation
artifact); the verdict rests on the exactness/∮a=0 argument, which is the executor's actual logic
and is fully confirmed. The research-note claim that ⟨R𝒦,D⟩ vanishes while ⟨R·Y,D⟩≠0 for generic Y
is imprecise (both are nonzero in my gauge); it is a supporting control, not load-bearing.
