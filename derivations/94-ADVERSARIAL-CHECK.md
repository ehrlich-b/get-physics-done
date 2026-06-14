# Phase 94 (v34.0) — BASE-SAKHAROV ON THE VARIETY: ADVERSARIAL THIRD-PATH CHECK

**Role:** adversarial path 3 of 3. Mandate: REFUTE the claimed verdict **CLOSES-CONDITIONAL** by
pushing it to **DOESN'T-CLOSE** (a kill: over-determination / wrong sign / un-tunable Λ-mismatch /
contamination) or **CLOSES-FORCED** (the clamp is actually forced) or **IMPORTS-QFT**. Default every
attack to "the verdict is wrong"; concede only when the computation defeats the attack.

**Drivers:** `code/adv_attack1_rankwall.py`, `code/adv_attack2_sign.py`, `code/adv_attack3_ccmismatch.py`,
`code/adv_attack4_clamp.py`. Exact over Q/Q(i) on every decisive path (sympy 1.14.0, mpmath 1.3.0,
Python 3.14.5, Darwin arm64). The v21 over-determination template (`code/sakharov_gate2_support.py`)
is the reference for what a real kill looks like.

---

## BOTTOM LINE

**CLOSES-CONDITIONAL SURVIVES. All four attacks FAILED to overturn it; every one STRENGTHENED the
verdict by replacing a hand-asserted claim with a computed fact.** No attack produced a kill
(DOESN'T-CLOSE), a forcing (CLOSES-FORCED), or a smuggle (IMPORTS-QFT). The G2 PASS-vs-soft-FAIL
fork and the G4 NOT-YET-FORCED classification are both **robust** under adversarial pressure.

The single most valuable result: the executor's `num_conditions = 1` / `num_knobs = 1` in
`sakharov_variety.py:G2()` were **hand-asserted literals** — the entire "this isn't the v21 rank
wall" turned on them. Attack 1 **proved them** by direct computation (the v33 source `TT(B3)` is a
PURE ε=20 eigentensor on all three Kähler blocks for all four matter directions; trace and TT
sectors constrain decoupled knobs). The claim was not glazed; it is now load-bearing-verified.

| Attack | Target | Result | Effect on verdict |
|---|---|---|---|
| **1** rank wall (Trap #26) | DOESN'T-CLOSE via over-determination | **FAILED** (all 4 sub) | STRENGTHENED (proved one-condition-one-knob) |
| **2** sign/contamination (Trap #27) | DOESN'T-CLOSE via wrong sign | **FAILED** (all 3 sub) | STRENGTHENED (sign mass-robust) |
| **3** cc un-tunable mismatch | DOESN'T-CLOSE via fixed Λ-offset | **FAILED** (all 4 sub) | STRENGTHENED (one-knob robust to mass) |
| **4** clamp FORCED / IMPORTED (Traps #25/#28) | CLOSES-FORCED or IMPORTS-QFT | **FAILED** (all 3 dir) | STRENGTHENED (NOT-YET-FORCED + native) |

---

## ATTACK 1 — the rank wall sneaking back (Trap #26, the v21 killer) — **FAILED, verdict STRENGTHENED**

**The refutation attempt.** The v21 kill (`sakharov_gate2_support.py`): `G = κT + Λg`, on the 10
OFF-T entries (G≠0, T=0) the equation collapses to `G_μν = Λ g_μν`, forcing ONE scalar Λ to equal
4 distinct rationals ⇒ EmptySet. A real kill = ≥2 independent conditions on a knob that disagree.
The v34 G2 claim that this is one-condition-one-knob is encoded as the literals `num_conditions = 1`,
`num_knobs = 1` — so I built the FULL induced field-equation system and checked for the v21 analog.

**The computation (exact over Q, `adv_attack1_rankwall.py`):**

- **1a — is FS-critical really ONE tensor condition?** Built the vacuum induced Einstein tensor
  `Eq = R_μν − ½R g_μν + Λ_cc g_μν` on FS and split into trace + traceless. Since FS is Einstein
  (`Ric = 6g`, verified entrywise), the **traceless part ≡ 0 identically** (independent of Λ_cc).
  ⇒ the vacuum induced field equation is genuinely ONE (scale) condition; the TT sector imposes no
  independent condition. *Proven, not asserted.* **Refutation FAILED.**

- **1b — is `TT(B3)` a PURE ε=20 eigentensor? (THE DECISIVE SUB-ATTACK, the v21 off-T analog).**
  The G3 response `h = κ_ind·TT(B3)/(Δ_L − 2Λ)` is well-defined only if `TT(B3)` lies entirely in
  the `(Δ_L − 2Λ) = 20` eigenspace. A component OUTSIDE it is the variety analog of the v21 off-T
  block (the field equation cannot source it). Ran `extract_tt(grad_bilinear(φ_M))` and the
  control-validated `lichnerowicz_full_v33` for 4 matter directions (s01, a01, d1, GEN=detM=−2):

  > `Δ_L r == 32 r` **EXACT on ALL THREE Kähler blocks** [H20, H11, H02] for **all 4 directions**
  > (each consistent / traceless / divergence-free). PURE 20-eigentensor: **True** ×4.

  **There is NO off-eigenspace residue ⇒ NO v21 off-T analog.** This is the structural reason the
  rank wall does not recur on the variety: the v33 source lives entirely inside the eigenspace.
  **Refutation FAILED — the strongest possible strengthening.**

- **1c — multi-matter over-determination.** v21 died because one scalar faced many incompatible
  conditions. Computed the `(Δ_L − 2Λ)` eigenvalue on `TT(B3[M])` for all 4 directions:
  `{s01: 20, a01: 20, d1: 20, GEN: 20}` — the **same 20 for every matter direction** (1 distinct
  value; contrast v21's 4 distinct Λ). One knob (ε=20) works for all M. **Refutation FAILED.**

- **1d — a4 higher-derivative contamination of the scale mode.** a4 is dimensionless (`Λ_f^0`, the
  conformal-anomaly/log piece), subleading to the `Λ_cc = (3/2)Λ_f²` matching (which is the
  `a0(Λ_f^4)/a1(Λ_f^2)` ratio) by `Λ_f²`. On the symmetric FS background the a4 variation is ∝ g
  (Einstein-preserving) ⇒ renormalizes Λ_cc, adds no traceless condition. **Refutation FAILED.**

**Final decoupling cross-check (airtight):** the trace mode constrains Λ_f (one equation, one knob:
`(3/2)Λ_f² = 6 ⇒ Λ_f² = 4`); the TT mode imposes **NO** constraint on Λ_f (ε ≠ 0 ⇒ `h =
κ_ind·TT(B3)/20` is solvable for ANY free κ_ind). The two sectors constrain **DIFFERENT, DECOUPLED
knobs** (Λ_f for the scale, the free κ_ind for the TT amplitude). This is the structural OPPOSITE of
the v21 kill (≥2 conditions on the SAME scalar). **The executor's `num_conditions = 1` is CORRECT —
now proven.**

**VERDICT: Attack 1 FAILED to overturn. G2 "not over-determined" is STRENGTHENED from an asserted
literal to a computed fact.**

---

## ATTACK 2 — the sign / contamination (Trap #27) — **FAILED, verdict STRENGTHENED**

**The refutation attempt.** Make G1 wrong-sign or contaminated: a hidden ξR|φ|² coupling, a
wave-map target curvature, or the mass `m² = λ₁ = 12` flipping the leading a₁ sign.

**The computation (exact over Q, `adv_attack2_sign.py`):**

- **2a — hidden ξR|φ|²?** `a₁ = (1/6 − ξ)R`; the conformal `ξ = 1/6` would give `a₁ = 0`. Computed
  `Δφ_d1 / (φ_d1 − φ̄) = −12` — a **constant** (not R(z)-dependent), so the `+λ₁` in the matter
  equation is a genuine Laplace eigenvalue, NOT a ξR coupling. The Dirichlet action has ξ = 0 ⇒
  `a₁ = +R/6 = 4`. No conformal `a₁ = 0` trap, no repulsive ξ > 1/6. **Refutation FAILED.**

- **2b — wave-map target curvature?** `φ_{aM1+bM2} == a·φ_M1 + b·φ_M2` (LINEAR in M ⇒ flat target
  ℝ⁸), and the target metric `d²⟨M,M⟩/dM²` has all-constant entries (field-independent ⇒ flat). No
  sigma-model target-curvature term enters E. **Refutation FAILED.**

- **2c — the mass m² = 12 sign flip (THE SHARPEST sign attack).** The matter equation
  `(Δ + λ₁)G_M = source` is a MASSIVE operator (`m² = λ₁ = 12`, Laplace-type `Δ − E` with
  `E = −12`). The full a₁ density `tr(E + R/6) = R/6 − m² = 4 − 12 = −8 < 0` — **would flip the
  sign** if read as 1/G. But the Sakharov-induced `1/(16πG)` is the **COEFFICIENT OF R** in a₁ (the
  term multiplying ∫R√g) = **+1/6, mass-INDEPENDENT**; the `E = −12` is a constant that multiplies
  ∫√g (renormalizes the induced **cosmological** term a₀, NOT 1/G). So `1/(16πG) = +1/6·Λ_f² > 0`
  stays ATTRACTIVE even WITH the mass. **Refutation FAILED.**

**Residual doubt carried forward (honest):** the mass DOES shift the induced cosmological constant
(the `−m²` piece lands in a₀). This feeds G2's cc-matching ⇒ tested directly in Attack 3c.

**VERDICT: Attack 2 FAILED to overturn. G1 clean+attractive is STRENGTHENED; the sign is robust to
the mass (the leading R-coefficient is mass-independent).**

---

## ATTACK 3 — the cc-match as an un-tunable mismatch — **FAILED, verdict STRENGTHENED**

**The refutation attempt.** Is `Λ_cc = (3/2)Λ_f²` really a single free Λ_f, or do the finite
(ζ-regularized, Λ_f-independent) pieces — or the mass shift (Attack 2c) — add a fixed offset the
cutoff cannot absorb (⇒ genuine mismatch ⇒ DOESN'T-CLOSE)?

**The computation (exact over Q, `adv_attack3_ccmismatch.py`):**

- **3a — careful cutoff bookkeeping.** `k_EH = (1/6)Λ_f²` (coeff of ∫R√g), `k_cc = (1/2)Λ_f⁴`
  (coeff of ∫√g) ⇒ `Λ_cc = k_cc/(2 k_EH) = (3/2)Λ_f²`, with **zero** Λ_f-independent part
  (`Λ_cc(Λ_f→0) = 0`). The matching `Λ_cc = 6` has the unique solution `Λ_f² = 4`. **One knob.
  Refutation (leading) FAILED.**

- **3b — strict ζ-reg native cc.** In strict ζ-reg there is NO power divergence ⇒ NO finite local
  induced 1/G; the EH R-coefficient LOG-RUNS (governed by `ζ(0) = −89/120 ≠ 0`, the conformal
  anomaly — verified, with the Gilkey tie `ζ(0)+1 = 31/120`). So strict-ζ supplies no fixed finite
  Λ_cc to match — there is **no forced number ≠ 6**, hence no un-tunable mismatch. The EH matching
  genuinely lives in the cutoff scheme (one knob Λ_f) — the KNOWN "induced gravity needs the cutoff
  scale" fact, NOT a kill. **Refutation FAILED.**

- **3c — the mass contribution (carried from 2c).** With `m² = 12`, the cc picks up a `−½m²Λ_f²`
  piece ⇒ `Λ_cc = (3/2)Λ_f² − 18` (a **fixed −18 Λ_f-independent offset**). Does that break tuning?
  Solved: `(3/2)Λ_f² − 18 = 6 ⇒ Λ_f² = 16` (positive, valid). **The mass SHIFTS the required cutoff
  (Λ_f²: 4 → 16) but does NOT over-determine** — still ONE equation in ONE knob. The fixed offset
  changes the *solution*, not the *number of conditions*. **Refutation FAILED.** (Residual: the exact
  mass-cc coefficient is scheme-dependent, but ANY finite mass shift stays a single Λ_f²-linear
  condition — the one-knob structure is robust.)

- **3d — the N-cancellation + unzeroed vacuum energy.** N cancels in the ratio `Λ_cc = (3/2)Λ_f²`
  (verified: both a0, a1 scale linearly in N). The unzeroed `ρ_Λ ~ (1/2)N Λ_f⁴` (8 bosons, no
  fermionic partner, anomaly ≠ 0) is the cosmological-constant PROBLEM, **NOT** an over-determination
  — it is reading [B]'s soft-FAIL, a JUDGMENT, not a hard EmptySet. The matching stays one-knob.
  **Refutation FAILED.**

**VERDICT: Attack 3 FAILED to overturn. G2's one-knob scale-identification is STRENGTHENED and shown
robust to the mass correction. Reading [B] is confirmed a JUDGMENT (the cc problem reframed), not a
hard kill — the executor's "FLAG for human ratification" is the honest call.**

---

## ATTACK 4 — is the clamp secretly FORCED (or secretly IMPORTED)? (Traps #25/#28) — **FAILED, verdict STRENGTHENED**

**The refutation attempt.** Two directions: (a) does an existing corpus result FORCE state-fp ⟹
metric-fp (⇒ CLOSES-FORCED)? (b) is the ζ′(0) machinery smuggled QFT (⇒ IMPORTS-QFT)? Plus the
seam (c): is there a state-fp/metric-fp conflation (an illegitimate CLOSES-FORCED)?

**The computation / corpus evidence (`adv_attack4_clamp.py`):**

- **4a — CLOSES-FORCED direction.** Paper 5 (`paper/`, "Quantum Mechanics from Self-Modeling")
  derives the STATE-SPACE (the JB-algebra h₃(𝕆) structure) from self-modeling. **ACTUAL
  spacetime-metric/gravitational claims in Paper 5: 0** (its 7 "geometry" mentions are state-space
  Alfsen–Shultz, NOT a spacetime metric). A corpus grep for a forcing of `δΓ/δg = 0` returns 2 raw
  hits, both **REJECTED** by a ±3-line context classifier: (i) the v33 VERDICT line is the
  FORCES-NOTHING **negative result** ("NO native functional ... forces ..."), (ii) the v34 RESEARCH
  line is the **make-it-fit TARGET** ending "No proof of this bridge exists in the corpus ⇒ default
  NOT-YET-FORCED." **ACTUAL forcing proofs: 0.** The bridge is ABSENT ⇒ NOT-YET-FORCED is correct;
  the refutation toward CLOSES-FORCED FAILS (no forcing to exhibit).

  *Methodology note (honest):* my first classifier pass gave a FALSE positive (it flagged both
  lines as proofs) because the rejection tokens ("NO native", "make-it-fit") spill into the *adjacent*
  lines that a single-line grep cannot see. Fixed by reading a ±3-line window directly from each
  file; both then correctly REJECT. The verdict-overturn was a detector bug, not a real forcing.

- **4b — IMPORTS-QFT direction.** The CP² spectrum (`λ_k = 4k(k+2)`, `d_k = (k+1)³`, λ₁=12, λ₂=32)
  is a NATIVE pre-v34 program object (27 lines across `variety_moment_doublet`, `sourced_field_equation`,
  `lichnerowicz_response`, `gate0_v33`). `ζ(0) = −89/120` is reproducible from that native spectrum
  by pure math (binomial/Hurwitz continuation; **cross-checked** by the independent Gilkey-a₄
  curvature route `indep_zeta0_gilkey.py`, ZERO shared code, PASS). ⇒ the effective-action MACHINERY
  is imports-as-MATH (native), NOT IMPORTS-QFT. **Refutation FAILED.**

  *Honest caveat (residual):* "the heat-kernel a₁ IS ∫R" and "one-loop Γ = ½ Tr log Δ" ARE QFT
  formalism imported as math (exactly like differential geometry / Gilkey / Besse are imported). The
  program OWNS the spectrum but BORROWS the effective-action identity. G4's NATIVE-computation call
  is defensible *under the program's own imports-as-math standard*, and the LOAD-BEARING gap is
  correctly placed at the PRINCIPLE (the clamp), not the computation. A stricter reviewer who
  refuses to import the effective-action identity could lean IMPORTS-QFT here — but that standard
  would also reject Gilkey/Besse, which the whole program already uses. This is a definitional
  judgment, not a computational kill; flagged.

- **4c — the seam (Trap #28).** state-fp lives on `ρ_J ∈ h₃(𝕆)` (the 27-dim algebra); metric-fp
  lives on `g` (the symmetric 2-tensor / deformation complex) — **typed-distinct** on different
  spaces. No `ρ_J = g` conflation in the v34 verdict/summary/driver (0 hits). The NOT-YET-FORCED
  classification is HONEST: a real typed gap between the proven state-fp and the unproven metric-fp;
  an illegitimate CLOSES-FORCED (by conflation) is ABSENT. **Refutation FAILED.**

**VERDICT: Attack 4 FAILED to overturn. G4 NOT-YET-FORCED + native-computation is STRENGTHENED; the
seam held; Trap #25 (no glaze to CLOSES-FORCED) and Trap #28 (typed-distinct) both honored.**

---

## OVERALL ADJUDICATION

**CLOSES-CONDITIONAL SURVIVES, and is materially STRENGTHENED.** Every attack defaulted to "the
verdict is wrong" and every attack was defeated by the computation:

1. **The G2 "not over-determined" fact is no longer an assertion.** Attack 1 proved, exact over Q,
   that (i) FS-Einstein makes the vacuum induced equation traceless-part-zero (one scale condition),
   (ii) the v33 source `TT(B3)` is a **PURE ε=20 eigentensor on all three Kähler blocks for all four
   matter directions** (no v21 off-T analog), (iii) the stiffness is the same 20 for every matter
   direction, and (iv) trace and TT constrain decoupled knobs. The executor's `num_conditions = 1`
   literal is **verified-correct**, not glazed. The "this isn't the v21 rank wall" claim is robust.

2. **The G2 PASS-vs-soft-FAIL judgment is robust.** It is genuinely a JUDGMENT (scale-identification
   = the cc problem reframed vs demand a content-forced cancellation), NOT a hard over-determination.
   Attack 3 confirmed the one-knob match survives even the mass correction (Λ_f²: 4 → 16, still one
   condition). The executor's FLAG-for-human-ratification on [A] vs [B] is the honest call — neither
   reading is a kill, and the recommendation (PASS-conditional with the scale-identification caveat)
   is defensible. **The G2 PASS gate, with its soft-FAIL caveat, holds.**

3. **The G4 NOT-YET-FORCED classification is robust.** No corpus proof forces state-fp ⟹ metric-fp
   (Paper 5 has zero gravitational claims; the only forcing-pattern hits are the v33 negative result
   and the v34 make-it-fit target). The computation is native (spectrum is a pre-v34 object, ζ(0)
   reproducible by two independent math routes). The seam is typed-distinct with no conflation.
   **NOT-YET-FORCED is the honest CEILING; Trap #25 (no glaze) and Trap #28 (seam) both held.**

**No attack succeeded.** No DOESN'T-CLOSE (no over-determination, no wrong sign, no un-tunable
mismatch, no contamination), no CLOSES-FORCED (no forcing proof, no conflation), no IMPORTS-QFT
(native computation). The derived verdict CLOSES-CONDITIONAL is the correct landing.

### Strongest residual doubt (flagged, NOT a kill)

The single genuine residual is the **G4(b) imports-as-math boundary** (Attack 4b caveat): the
effective-action *identity* (`Γ = ½ Tr log Δ`, `a₁ = ∫R`) is borrowed QFT formalism. The program's
own standard treats such formalism as imports-as-math (like Gilkey/Besse, which it already uses), so
NATIVE-computation is defensible — but a reviewer applying a stricter "owns it or imports it" line
could lean IMPORTS-QFT. This is a **definitional judgment about the import boundary**, not a
computational error, and it does not change the bottom line (either NOT-YET-FORCED ⇒ CONDITIONAL or
IMPORTS-QFT both leave Paper 5 as the only more-than-nothing result and the gravity gap unforced).
It is worth a human ratification line alongside the G2 [A]/[B] flag.

### Are the two flagged judgments robust?

- **G2 PASS-vs-soft-FAIL: ROBUST.** Attacks 1+3 confirm it is a tunable scale-identification, not an
  over-determination; the PASS (reading [A]) is the recommended, defensible call, with [B] a
  legitimate stricter standard the human should rule on. Not a hidden kill.
- **G4 NOT-YET-FORCED: ROBUST.** Attack 4 confirms no forcing exists and the seam is honest. The only
  adjacent flag is the imports-boundary judgment (4b caveat), which does not threaten CONDITIONAL.

---

## FENCES (binding, verbatim)

NO Einstein-equation / G=κT / gravity / Newton / dark-matter / geodesic language as a DERIVED result;
κ is a framework ratio (Λ_f-set), NOT Newton's constant; FS is USED, not derived; signature
Riemannian (Wall 2 unpaid — NOTHING is called gravity, even under CLOSES-FORCED, until signature is
paid); CLOSES-CONDITIONAL is NOT a derivation. v34 does NOT retract v33 (extremize route stays dead)
or v17–v21 (the fiber kills stand). Paper 5 remains the only result in the more-than-nothing column.
Three-path verification standing; milestone HOLD for human ratification; do NOT self-register v35.

---

## Reproducibility

sympy 1.14.0, mpmath 1.3.0, Python 3.14.5, Darwin arm64. Exact rational arithmetic over Q/Q(i) on
every decisive path (no RNG / no seeds in any verdict path; floats illustrative only). Attack 1's
`extract_tt` reuses `code/.p92_basis_images.pkl` (243-column disk cache) and the certified
`lichnerowicz_full_v33` operator (control-validated in `gate0_v33.py`: C1/C2a/C2b/REG). Attack 4b
runs the independent `indep_zeta0_gilkey.py` (Gilkey-a₄ curvature route, zero shared code with the
spectral-ζ path).

## Artifacts

- `code/adv_attack1_rankwall.py` — Attack 1 (the v21 rank-wall recurrence; 4 sub-attacks; the
  decisive `TT(B3)` PURE-ε=20-eigentensor check on all 3 blocks × 4 matter directions, ~290 s).
- `code/adv_attack2_sign.py` — Attack 2 (sign/contamination; ξR / wave-map / mass-flip; ~0.1 s).
- `code/adv_attack3_ccmismatch.py` — Attack 3 (cc un-tunable mismatch; cutoff/strict-ζ/mass/N; ~0.1 s).
- `code/adv_attack4_clamp.py` — Attack 4 (clamp FORCED/IMPORTS-QFT/seam; corpus evidence + ζ(0)
  native reproduction + Gilkey cross-check; ~3 s).
- `derivations/94-ADVERSARIAL-CHECK.md` — this file.
