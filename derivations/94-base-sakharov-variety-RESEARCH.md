# Phase 94 (v34.0) — BASE-SAKHAROV ON THE VARIETY: Research / grounding bible

**Researched:** 2026-06-14
**Domain:** Sakharov induced gravity (zero-temperature one-loop vacuum effective action) of the
moment field on the Fubini–Study cut CP² = h₃(C_u); Seeley–DeWitt / Gilkey heat-kernel coefficients;
ζ-function of the CP² scalar Laplacian; the self-consistency (cosmological-constant) test.
**Confidence:** HIGH on the spectrum, the heat-kernel coefficients, the sign, and ζ(0)=−89/120
(orchestrator-de-risked, exact over Q + two independent numerical cross-checks); the GENUINE FORK is
G2 (does FS come out critical of its own induced action) and the G4 clamp classification.
**Consumer:** `gpd-executor` writing `code/sakharov_variety.py` (NO WEB) gate-by-gate, then
`gpd-verifier` (HAS WEB), then an adversarial third path. **Exact over Q where in-rep; fail-fast.**

---

## BOTTOM LINE (read first)

**Expected verdict: CLOSES-CONDITIONAL.** The induce route does NOT die on the variety the way it
died on the v21 fiber — and it does NOT force a gravitational law either. The honest landing: the
frozen FS geometry IS self-consistent under its own matter loop and closes on the v33 source, so the
ENTIRE gravity gap collapses to the single state-fp ⟹ metric-fp clamp (Paper 5), which is
NOT-YET-FORCED. That is a real result (it names and isolates fork A's gap to one clamp), and it is the
honest CEILING absent a Paper-5 fit — **do NOT promote it to CLOSES-FORCED (Trap #25).**

The load-bearing facts, all orchestrator-de-risked (`/tmp/v34_derisk.py`, reproduced here):

1. **The fluctuation operator is the minimal massless scalar Laplacian (E=0).** The variety matter
   action is the free Dirichlet energy ∫|∇φ_M|²√g (v25–v27: the matter E), quadratic in φ_M, so the
   one-loop fluctuation operator is exactly Δ = −g^{μν}∇_μ∇_ν, minimal, no mass, no curvature
   endomorphism. ⇒ Gilkey a₁-coefficient = R/6 = **+4** (per real d.o.f.), BOSONIC statistics ⇒
   **attractive (1/16πG_ind > 0)**, no two-minus subtlety (unlike the v21 fermions). **G1 clean.**

2. **No contamination (Trap #27 sign / wave-map / non-associativity).** The moments φ_a = Tr(M·P) are
   LINEAR in the SU(3)-adjoint embedding ⇒ flat target ⇒ no wave-map (sigma-model target-curvature)
   term in E; the Gilkey a₁ structurally contains ONLY E and R·1 (R²/Ric²/Riem²/□R/tr F² are strictly
   a₂-level); non-associativity does not enter the BASE field's scalar Laplacian. Exactly the v21
   Gate-1 logic (linear 16 of Spin(10) → flat target), now on the bosonic base. **a₁ ∝ ∫R, clean.**

3. **The rank wall does NOT transfer (Trap #26).** v33 Gate-0 PROVED Δ_L r = 32·r on every block,
   ε = λ_L − 2Λ = 20 ≠ 0 ⇒ the Einstein operator acts invertibly on the matter source, the response
   h = κ·TT(B3)/ε is well-defined. The v21 16-vs-6 over-determination was a property of the SOLDERED
   metric g = e·e; the variety puts matter and geometry on the same footing. **Re-confirm at G0.**

4. **The CP² scalar Laplacian spectrum (Ric = 6g ⇒ R = 24):**
   **λ_k = 4k(k+2)** (eigenvalue), **d_k = (k+1)³** (degeneracy), k = 0,1,2,…
   ⇒ λ₀=0/d₀=1 (constant), λ₁=12/d₁=8 (the SU(3) adjoint — the program's moments), λ₂=32/d₂=27,
   λ₃=60/d₃=64. (d_k = dim of the SU(3) (k,k) irrep = (k+1)²(2k+2)/2 = (k+1)³.) The "4·2·4 = 32"
   mnemonic in `variety_sourced_field_equation.py` is 4·k·(k+2) at k=2.

5. **ζ(0) = −89/120** for the (zero-mode-excluded) scalar Laplacian — the decisive G2 anchor.
   Confirmed two ways (exact analytic continuation + independent numerical continuation). Gilkey tie:
   A₄/(4π)² = ζ(0) + dim ker = −89/120 + 1 = **31/120** (the integrated Seeley a₄ — verifier confirms
   against the CP² literature value). Independent validation that the (λ_k,d_k) are right:
   **A₂/A₀ = R/6 = 4** extracted numerically from the small-t heat-kernel asymptotics (and A₀ ≈ π²/2 =
   Vol(CP², Ric=6g) ✓).

6. **The G2 self-consistency fork is RESOLVABLE, not a kill.** In the cutoff (Sakharov) scheme the
   induced cosmological term and Einstein–Hilbert term give an effective **Λ_cc = (3/2)Λ_f²**
   (per d.o.f.; the count N CANCELS in the ratio), and FS is a vacuum solution of its own induced
   action ⟺ R_{μν} − ½R g + Λ_cc g = 0 ⟺ **Λ_cc = 6** ⟺ **Λ_f² = 4** (the cutoff = the curvature
   scale). This is ONE condition with ONE knob (the scale mode) ⇒ ALWAYS solvable ⇒ **NOT an
   over-determination** (the v18/v21 rank wall was 10 incompatible conditions on 1 scalar). The honest
   reading: FS IS a critical point at the natural/only scale, but the match is a **scale-identification
   (the cosmological-constant problem reframed), NOT a forced content cancellation** (8 bosons, no
   fermionic partner to zero the vacuum energy). Whether this counts as G2-PASS (CLOSES-CONDITIONAL,
   with the scale-identification folded into the not-yet-forced clamp) or as a soft Λ-mismatch is a
   judgment **flagged for human ratification** — but it is NOT the hard DOESN'T-CLOSE that an
   over-determination would force.

7. **G3 closes on stiffness, κ_ind FREE.** The TT Hessian of a₁ = ∫R√g on an Einstein background IS
   the Lichnerowicz operator Δ_L − 2Λ (Besse 4.60; the second variation of Einstein–Hilbert). v33
   Gate-0 gives ε = 20 on the source ⇒ closure FOLLOWS from a clean G1. But κ_ind = 1/(16πG_ind) ∝
   Λ_f² is set by the cutoff scale Λ_f — a **framework ratio, Λ_f-set, NOT forced** (a fit, unless
   Paper 5 forces Λ_f). This is the v21/v33 "κ is a framework ratio, not Newton" carried over.

8. **G4 = the honest gate.** The COMPUTATION (the functional integral / ζ′(0) of a Laplacian whose
   spectrum the program already uses) is native; the PRINCIPLE "the system sits at the extremum of
   Γ[g]" is the state-fp ⟹ metric-fp clamp = **NOT-YET-FORCED** (the honest default). Classify; do NOT
   smuggle (Trap #25). Keep state-fp (on ρ_J ∈ h₃(O)) and metric-fp (on g) typed-distinct (Trap #28).

---

## §0. Where this sits — the two-route confrontation + verdict taxonomy (frozen at G0)

A gravitational LAW = a reason the constructed metric EXTREMIZES something (G=κT is the EL equation of
∫R). Two ways to manufacture one from h₃(O) data:
- **EXTREMIZE a native functional A[g]** — v33 ran it → **FORCES-NOTHING** (λ₁-extremality is a
  class-consistency condition, Schur-tautological + rank-deficient; only Einstein-producer ∫R√g is the
  import). The extremize route stays dead; **v34 does NOT retract it.**
- **INDUCE the action by integrating out matter (Sakharov)** — the matter one-loop effective action's
  leading heat-kernel term IS ∫R√g. **This run.** The one live kind-4 instance the v21 fiber kill does
  NOT reach (the variety cleared the rank wall, v33 Gate-0).

**Verdict taxonomy (frozen — the executor's `verdict()` ladder must be DERIVED from the gate results,
non-hardwired, with self-tests; v20 hardcoded-boolean bug is the anti-pattern):**

- **CLOSES-FORCED** — G1–G3 pass AND G4 = FIT (Paper 5 forces the clamp). The selection law, derived.
  (Wall 2 / signature still unpaid ⇒ STILL not called "gravity" — but the LAW would be forced.)
  Highest bar; pre-registered unlikely.
- **CLOSES-CONDITIONAL** — G1–G3 pass, G4 = NOT-YET-FORCED. The variety's geometry IS self-consistent
  under its own matter loop and closes on the source; the entire gravity gap is isolated to the single
  state-fp ⟹ metric-fp clamp. **The expected outcome; a real result.**
- **DOESN'T-CLOSE** — G1 contaminated / wrong sign, OR G2 says FS is NOT a critical point (a genuine
  over-determined Λ-mismatch, not a tunable scale-identification), OR G3 fails ⇒ the induce route dies
  on the variety too (a NEW kill, distinct from the fiber rank wall) ⇒ fork A FORCED.
- **IMPORTS-QFT** — the closing demonstrably requires importing the functional-integral machinery (not
  native) ⇒ "the import" confirmed ⇒ fork A FORCED.

---

## §1. G0 — foundation + machinery freeze (binding input, re-confirm before building)

**Goal:** reproduce v33 Gate-0 (Δ_L r = 32·r, ε = 20, all blocks) and the v32 fingerprints
(T1/T2/norm/5:4). The rank-compatibility (Trap #26) is the load-bearing input that distinguishes this
from the dead fiber; confirm it before any new computation.

**Drivers (already certified, re-run):**
- `python3 -u code/gate0_v33.py` → C1/C2a/C2b/REG all PASS and **Δ_L r = 32 on every block** for
  s01/a01/d1/d2 (≈3 min, exact over Q). ⇒ λ_L = 32, **ε = λ_L − 2Λ = 32 − 12 = 20**.
- `python3 -u code/lichnerowicz_response_fingerprint.py` → **T1 PASS, T2 PASS, all 5 norm directions
  exact, the 5:4 split exact** (the v32 machinery-freeze fingerprints — `extract_tt`/`l2_tensor`
  untouched, so the machinery is frozen). (T3 Gram rank-6 is the ~40-min slow re-confirmation; rows
  0–3 clean suffice — do NOT block on the full Gram.)

**G0 verdict:** PASS ⟺ ε = 20 reproduced AND the fingerprints reproduce. This is a control, not new
physics — if it does NOT reproduce, STOP (the machinery drifted; do not build on a moved foundation).

---

## §2. G1 — the heat kernel (the core computation)

**Goal:** build the moment-field fluctuation operator on CP², confirm it is minimal/clean, compute the
Seeley–DeWitt a₀ and a₁, read off the sign and (κ_ind, Λ_ind).

### 2.1 The fluctuation operator (confirm minimal — do not assume)

The variety matter action is the free Dirichlet energy `E[φ_M, g] = ∫ g^{μν} ∂_μφ_M ∂_νφ_M √g`
(v25–v27; `variety_sourced_field_equation.py` shows the matter equation is the LINEAR `(Δ + λ₁)G_M =
source`, i.e. the action is quadratic ⇒ a free field). The quadratic part in the fluctuation δφ around
ANY background is `∫|∇δφ|²√g`, so the fluctuation operator is

> **Δ = −g^{μν}∇_μ∇_ν** (the minimal scalar Laplacian; in Laplace-type form Δ = −(∇² + E) with **E = 0**, no mass, no curvature endomorphism, no gauge connection Ω).

**The executor MUST verify, not assume, three things (the contamination criteria — Trap #27):**
1. **E has no curvature piece.** A non-minimal coupling ξR|φ|² would give E = −ξR; the free Dirichlet
   action has ξ = 0. Confirm the matter action carries no ξR|φ|² term (it does not — it is pure
   Dirichlet). [If a ξ were present, a₁ = (1/6−ξ)R is dialable — report it; the base field has ξ=0.]
2. **No wave-map target curvature.** The moments φ_a = Tr(M·P) are LINEAR in the adjoint embedding ⇒
   the target is the flat linear space R⁸ (the SU(3) adjoint), NOT a curved coset ⇒ no
   target-curvature term injected into E. (Contrast the genuine risk: a nonlinear sigma model into a
   curved target would put a tr(F²)-type non-R invariant into a₁.) Confirm linearity.
3. **No non-associativity leak.** The base field lives on CP² = h₃(C_u) (the COMPLEX cut); the scalar
   Laplacian is associative-algebra-clean. (The v18/v20 non-associative MM corpse is a FIBER object;
   it does not touch the base's scalar Laplacian.) Confirm the operator is a clean Laplace-type Δ.

### 2.2 Gilkey / Seeley–DeWitt coefficients (transcribe; exact over Q)

For a Laplace-type operator Δ = −(g^{μν}∇_μ∇_ν + E) in dimension d=4 the heat-kernel trace expands as
`Tr e^{−tΔ} ~ (4πt)^{−2} Σ_{n≥0} t^n A_{2n}`, with the integrated coefficients (Gilkey;
Vassilevich hep-th/0306138 §4.3):

| Coeff (prompt label) | = Gilkey | density tr(...) | integrated on CP² (E=0, R=24 const) |
|---|---|---|---|
| **a₀** (∫√g term) | A₀ | tr(1) = 1 | A₀ = Vol(CP²) = π²/2 |
| **a₁** (∫R√g term) | A₂ | tr(E + R/6) = R/6 | A₂ = (1/6)·24·Vol = **4·Vol** |
| a₂ (∫R²,Ric²,Riem² term) | A₄ | the curvature-squared invariants | A₄ = (31/120)·(4π)² (from ζ(0)) |

**NOTE the labelling:** the prompt's `a₀, a₁` are the t⁰ and t¹ coefficients (A₀, A₂); the prompt's
`a₁` = Gilkey's `a₂` = the universal `tr(E + R/6)`. (Same convention as the v21 RESEARCH.)

### 2.3 The sign and the induced couplings

Bosonic one-loop: `Γ = +(1/2) Tr log Δ = −(1/2)∫_{1/Λ_f²}(dt/t) Tr e^{−tΔ}` (proper-time, lower
cutoff δ = Λ_f⁻²). The quadratically-divergent a₁ term gives the induced Einstein–Hilbert coupling;
the quartically-divergent a₀ term gives the induced cosmological term. **Per real scalar d.o.f., units
Λ_f²/(4π)², with the common positive prefactor and the v21 absolute-sign anchor (a minimal scalar ⇒
G>0):**

- **a₁ R-coefficient = +1/6 > 0 ⇒ 1/(16πG_ind) > 0 ⇒ G_ind > 0 (attractive).** Bosonic, E=0, no
  Lichnerowicz/statistics minus to chase — strictly simpler than the v21 fermion case. **Confirm three
  ways (Trap #27): (i) Gilkey a₁=R/6; (ii) the minimal-scalar entry of the v21 Frolov–Fursaev/Visser
  spin-weight table (k₀ for spin-0 ⇒ +); (iii) direct — E=0 leaves only the universal +R/6.**
- **κ_ind:** 1/(16πG_ind) = (Λ_f²/(4π)²)·N·(1/6), with N = the field-space dimension. The moment field
  is adjoint-valued (N = 8, the λ₁=8). ⇒ 1/(16πG_ind) = (8/6)(Λ_f²/(16π²)) = **Λ_f²/(12π²)**,
  G_ind = 3π/(4Λ_f²). (Coefficient is count/scheme-dependent and NOT load-bearing for the verdict — κ
  is free either way; state it, flag it.)
- **Λ_ind:** the a₀ term ⇒ vacuum energy density ρ_Λ,ind ∝ Λ_f⁴·N. (Magnitude scheme-dependent.)

### 2.4 G1 verdict

PASS ⟺ (E=0 minimal & clean, three contamination checks pass) AND (a₁ ∝ ∫R, attractive sign,
three-way confirmed). DEAD ⟺ a non-R invariant survives in a₁ with nonzero coefficient, OR the sign
comes out repulsive. Expected: **PASS** (clean, attractive).

---

## §3. G2 — the self-consistency test (the NEW content, real teeth) — THE GENUINE FORK

**Goal:** is the FROZEN FS metric a CRITICAL POINT of its own induced action
`Γ = (1/16πκ_ind)∫R√g + ρ_Λ,ind ∫√g`? Equivalently, do the matter-loop (κ_ind, Λ_ind) make FS a
vacuum solution of `R_{μν} − ½R g_{μν} + Λ_cc g_{μν} = 0`?

### 3.1 The matching condition (exact)

On the Einstein background FS, `R_{μν} = 6 g_{μν}`, `R = 24`, so `R_{μν} − ½R g_{μν} = 6g − 12g =
−6g`. The vacuum equation ⟹ **FS critical ⟺ Λ_cc = 6** (= Λ_geo). Writing
`Γ = (1/16πG)∫(R − 2Λ_cc)√g`, the induced `Λ_cc = −½ · (coeff ∫√g)/(coeff ∫R√g)`.

**Cutoff (Sakharov) scheme — orchestrator-de-risked:** with the a₀ (∝ Λ_f⁴) and a₁ (∝ Λ_f²)
divergences, per d.o.f. `1/(16πG) ∝ (1/6)Λ_f²` and `ρ_Λ ∝ (1/2)Λ_f⁴` ⇒

> **Λ_cc = (3/2) Λ_f²** (the field-count N CANCELS in the ratio) ⇒ FS critical ⟺ **Λ_f² = 4**.

### 3.2 The native (ζ-function) anchor

The native regularization (G4(a)) is ζ-function: the one-loop determinant is ζ′(0), the spectrum
(λ_k = 4k(k+2), d_k = (k+1)³) is the program's own. The conformal/scaling structure is pinned by
**ζ(0) = −89/120** (de-risked exact + numerically), with the Gilkey tie A₄/(4π)² = 31/120. KEY honest
subtlety the executor must state: in d=4 the induced EINSTEIN–HILBERT term is intrinsically the
quadratic (Λ_f²) Sakharov divergence — it needs the cutoff SCALE Λ_f; the strict-ζ scheme yields a
FINITE determinant/cosmological piece but renders the R-coefficient a LOG-running (conformal-anomaly,
ζ(0)) coupling, not a finite local induced 1/G. So the "induced gravity" coupling carries a scale
Λ_f; whether Λ_f is native (the ρ_J fixed-point scale) is a G3/G4 question.

### 3.3 The fork — and why it is NOT the rank wall (Trap #26)

The matching is **ONE condition (the scale/volume mode) with ONE knob (Λ_f)** ⇒ ALWAYS solvable
(Λ_f² = 4). Contrast the v18/v21 death: 10 OFF-T entries over-determined ONE scalar to 4 distinct
rationals ⇒ EmptySet (an over-determination a scalar κ cannot repair). **There is no such
over-determination here** — the source is the clean ε=20 eigentensor (G0), and the cc-matching is a
single scalar equation. So G2 does NOT die the rank-wall death.

**The honest content (the deliverable):** FS IS a critical point of its own induced action at the
natural/only scale (Λ_f = curvature scale). BUT the match is a **scale-identification** — the
cosmological-constant problem in its standard form — NOT a forced cancellation from the field content
(8 bosons, no fermionic partner to zero ρ_Λ; ζ(0) ≠ 0 so the anomaly does not vanish). The executor
emits the exact Λ_cc(Λ_f), the FS-critical Λ_f², the ζ(0) anchor, and a **non-hardwired** G2 reading:

- **G2 = PASS (field-faithful, conditional)** if "FS critical at the only available scale" counts —
  the scale-identification is then folded into the G4 not-yet-forced clamp. → contributes
  CLOSES-CONDITIONAL. **[Expected.]**
- **G2 = soft-FAIL (Λ-mismatch)** if one demands a content-forced cancellation (Λ_ind = Λ_geo without
  scale-tuning) — then the induce route does not close on its own ⇒ leans DOESN'T-CLOSE.

This is a genuine judgment; **emit both readings + the exact numbers, recommend PASS-conditional with
the scale-identification caveat, and FLAG for human ratification.** Do NOT silently pick.

---

## §4. G3 — closure on the source (largely follows from a clean G1)

**Goal:** confirm the induced field equation reproduces the certified stiffness, and decide whether
κ_ind is FORCED or FREE.

- **The stiffness is automatic.** The TT (transverse-traceless) Hessian of `a₁ = ∫R√g` on an Einstein
  background IS the Lichnerowicz operator **(Δ_L − 2Λ)** (Besse, *Einstein Manifolds* 4.60: the second
  variation of the total scalar curvature on an Einstein metric is ½(Δ_L − 2Λ) on TT tensors). v33
  Gate-0 shows Δ_L acts as **λ_L = 32 ⇒ (Δ_L − 2Λ) = ε = 20** on the source r = TT(B3). So the induced
  field equation is `(Δ_L − 2Λ) h = κ_ind · TT(B3)` ⇒ **h = κ_ind · TT(B3) / 20**, well-defined
  (ε ≠ 0). Closure FOLLOWS from G1 producing a clean ∫R. (Re-use the v33 ε=20; do not recompute Δ_L.)
- **Is κ_ind forced?** κ_ind = 1/(16πG_ind) ∝ Λ_f². The framework grading (v20/v21: R[h₃(O)]^{F₄} is
  free on POSITIVE-degree generators Tr/Tr²/det₃; no negative-weight invariant; det₃ ≡ 0 on the
  Lorentz block) does NOT supply a dimensionful scale ⇒ **κ_ind is a framework ratio set by the cutoff
  Λ_f, NOT forced** unless Paper 5 forces Λ_f (the ρ_J fixed-point scale). A forced κ that reproduces
  ε=20 self-consistently would be a result; **a free κ is a fit.** Expected: **κ_ind FREE (a fit).**

**G3 verdict:** PASS on stiffness (ε=20 closure), κ_ind FREE. Note the asymmetry: the STIFFNESS (20)
is a forced framework number; the COUPLING (κ_ind) is a free scale. That asymmetry is exactly the
"closes on the source but does not force the law" of CLOSES-CONDITIONAL.

---

## §5. G4 — the clamp audit (the honest gate, load-bearing, joint-test)

**Goal:** classify "the system extremizes Γ[g]" as FIT / IMPORT / NOT-YET-FORCED. Trap #25
(demotion-glaze): do NOT relabel "extremize Γ" as native without an explicit Paper-5 forcing.

- **(a) Is the functional integral over φ_M native?** YES for the COMPUTATION: the one-loop determinant
  is ζ′(0) of the matter Laplacian whose spectrum (λ₁=12, λ₂=32, …) the program ALREADY uses (v25–v33,
  Gate-0). The heat-kernel coefficients are spectral data of the frozen geometry. So the
  effective-action MACHINERY is native (imports-as-math, like the rest of the program). [If the
  closing demonstrably needed functional-integral machinery NOT reducible to the program's own
  spectrum ⇒ IMPORTS-QFT. Expected: native computation.]
- **(b) Does it route through Paper 5 (the PRINCIPLE)?** The open question is "the system sits at the
  extremum of Γ[g]." Make-it-fit target: the self-model's quantum fixed point (Born-rule structure;
  ρ_J the attractor of the φ-iteration, Paper 5) FORCES the metric to extremize Γ — the **state-fp ⟹
  metric-fp** bridge. **SEAM (Trap #28, woo-risk, keep typed-distinct):** state-fp lives on ρ_J
  (X ∈ h₃(O), the algebra); metric-fp lives on g (the geometry). The bridge is the thing to PROVE,
  never to assume. No proof of this bridge exists in the corpus ⇒ default **NOT-YET-FORCED.**

**G4 deliverable:** classify. Expected: **NOT-YET-FORCED** (the computation is native; the principle
is the single isolated clamp). A load-bearing clamp is NOT relabeled "conditional and shipped" — it is
FIT (exhibit the forcing) or flagged not-forced. **STOP at NOT-YET-FORCED; do not glaze to FORCED.**

---

## §6. Traps / controls / fences (binding)

**Traps (prompt §"Traps", carried + v33/v21):**
- **#25 (the big one — demotion-glaze):** smuggling the clamp — relabeling "extremize Γ" native
  without the G4(b) Paper-5 fit. CLOSES-CONDITIONAL is the honest CEILING absent the fit; do NOT
  promote to CLOSES-FORCED. STOP.
- **#26:** the rank wall sneaking back — the variety source must be rank-compatible; v33 Gate-0 says it
  is (Δ_L r = 32 r, ε=20). Re-confirm at G0.
- **#27:** sign error — bosonic scalar ⇒ attractive; confirm THREE ways (Gilkey a₁=R/6 / the
  Frolov–Fursaev–Visser scalar weight / direct E=0). Also the contamination sub-traps: ξR coupling,
  wave-map target curvature, non-associativity (all absent on the linear base field — verify).
- **#28:** conflating state-fp with metric-fp at G4 (the woo seam) — keep them typed-distinct.
- **Trap #24 carryover (Schur tautology):** do NOT call a tautological proportionality "Einstein" — but
  here the object is the Sakharov a₁=∫R, genuinely the EH form, not a Schur scalar; the honest gap is
  the CLAMP and the cc scale-identification, not a tautology.

**Controls (must reproduce BEFORE any new computation — machinery freeze):**
- v33 Gate-0 (ε=20) + the v32 fingerprints (T1/T2/norm/5:4) reproduce exact over Q (G0).
- The fluctuation operator is SU(3)-equivariant (Schur block-diagonal on the (k,k) eigenspaces) —
  deviation = a bug.
- The spectrum reproduces R via A₂/A₀ = R/6 = 4 (de-risked); ζ(0) = −89/120 (de-risked, anchor).
- `verdict()` is a DERIVED ladder with self-tests (NOT a hardwired boolean — the v20 bug).

**Fences (binding, EVERY artifact — verbatim from the prompt):** NO Einstein-equation / G=κT / gravity
/ Newton / dark-matter / geodesic language as a DERIVED result; **κ is a framework ratio (Λ_f-set), NOT
Newton's constant**; **FS is USED, not derived**; **signature Riemannian (Wall 2 unpaid — NOTHING is
called gravity, even under CLOSES-FORCED, until signature is paid)**; CLOSES-CONDITIONAL is NOT a
derivation. v34 does NOT retract v33 (extremize route stays dead) or v17–v21 (the fiber kills stand).
**Paper 5 remains the only result in the more-than-nothing column.** Three-path verification standing;
milestone HOLD for human ratification; do NOT self-register v35.

---

## §7. Conventions

| Choice | Convention | Source |
|---|---|---|
| Cut geometry | CP² = h₃(C_u), Fubini–Study, KÄHLER-EINSTEIN **Ric = 6g**, R = 24, Λ_geo = 6 | v25–v33; CONVENTIONS.md |
| Scalar Laplacian | analyst's Δ_an ≤ 0; the operator is the POSITIVE Δ = −g^{μν}∇_μ∇_ν ≥ 0; λ₁=12, λ₂=32 | `lichnerowicz_response.py`; `variety_sourced_field_equation.py` |
| Spectrum | λ_k = 4k(k+2), d_k = (k+1)³ (SU(3) (k,k) irrep) | de-risked; standard CP^n |
| Heat kernel | Tr e^{−tΔ} ~ (4πt)^{−2}Σ t^n A_{2n}; a₁(prompt)=A₂=tr(E+R/6) | Gilkey; Vassilevich §4.3 |
| One-loop sign | boson Γ = +½ Tr log Δ; minimal scalar ⇒ 1/(16πG)=+1/6 unit ⇒ G>0 | v21 RESEARCH (anchor) |
| Lichnerowicz | Δ_L h = ∇*∇h + 2Λh − 2R̊h, Λ=6; ε = λ_L − 2Λ = 32 − 12 = 20 (v33 Gate-0) | `lichnerowicz_response.py`; Besse |
| Arithmetic | EXACT over Q/Q(i) on every decisive path; floats illustrative only; ζ via analytic continuation | CONVENTIONS.md §2/§7 |
| Regularization | proper-time/cutoff Λ_f (Sakharov, primary) + ζ-function (native anchor, ζ(0)=−89/120) | Sakharov; Visser; Hawking ζ |

---

## §8. Through-line (mirror v33's)

v33 the EXTREMIZE route forces nothing → v34 the INDUCE route: does the frozen FS geometry close under
its own matter loop? **G1 clean (bosonic minimal scalar, attractive, no contamination); G2 the genuine
fork — FS IS a critical point of its own induced action at the natural scale (Λ_cc=(3/2)Λ_f²=6 ⟹
Λ_f²=4), a scale-identification not a forced cancellation, NOT the rank wall; G3 closes on the ε=20
source with κ_ind FREE; G4 the computation is native but the "extremize Γ" PRINCIPLE = the state-fp ⟹
metric-fp clamp is NOT-YET-FORCED.** ⇒ **CLOSES-CONDITIONAL** isolates the entire gravity gap to that
single clamp (the program's oldest unforced joint, now standing alone with the rank wall cleared).
CLOSES-FORCED would require the Paper-5 fit; DOESN'T-CLOSE / IMPORTS-QFT would force fork A. Either way
this COMPLETES the Block-C confrontation on the variety — both ways to manufacture a law, run.

---

## §9. References (verifier with web to confirm equation/table numbers; coefficients are de-risked)

- **Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*** — the
  canonical a_{2n}; a₂ = E + R/6, the a₄ curvature invariants.
- **Vassilevich, "Heat kernel expansion: user's manual," Phys.Rept. 388 (2003) 279 (hep-th/0306138)**
  §4.3 — a₂ = (4π)^{−2}∫tr(E+R/6); a₄ structure (R²/Ric²/Riem²/□R).
- **Sakharov (1967)** — induced gravity, κ⁻¹ ~ Λ². **Visser, gr-qc/0204062** — modern perspective,
  spin-weight table, cutoff Λ². **Frolov–Fursaev, hep-th/9607104** — per-field induced-G weights
  (minimal scalar +1). **Adler, Rev.Mod.Phys. 54 (1982) 729** — the sign caveat (scheme-dependence).
- **Besse, *Einstein Manifolds* (1987), 4.60 & Ch. 4** — the second variation of total scalar curvature
  on an Einstein metric is ½(Δ_L − 2Λ) on TT tensors (the G3 theorem).
- **CP^n scalar Laplacian spectrum:** λ_k = 4k(k+n), multiplicity = dim of the (k,…,k) U(n+1) harmonic;
  for CP² the (k,k) SU(3) irrep, dim (k+1)³. (Berger–Gauduchon–Mazet; Ikeda–Taniguchi.) ζ(0) for the
  CP² scalar Laplacian = −89/120 (verifier: cross-check against the heat-kernel a₄ / conformal-anomaly
  literature, e.g. the c-coefficient of CP²).
- **Project priors (reuse, do NOT re-derive):** v33 Gate-0 (ε=20) `code/gate0_v33.py`,
  `derivations/93-GATE-0-SUMMARY.md`; the matter field equation `code/variety_sourced_field_equation.py`
  (the free Dirichlet field, (Δ+λ₁)G_M = source); the v21 heat-kernel grounding
  `derivations/81-sakharov-RESEARCH.md` (the contamination criteria, the sign chain).
