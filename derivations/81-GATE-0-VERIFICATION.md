---
phase: 81-sakharov-gate0
milestone: v21.0 (Sakharov Induced Gravity from V_{1/2} on h_3(O))
verified: 2026-06-06T00:00:00Z
verifier: gpd-verifier (adversarial, web-enabled)
status: passed
verdict: SURVIVES-confirmed
score: 1/1 decisive claim verified (the boson-vs-fermion sign)
consistency_score: 9/9 physics checks passed
independently_confirmed: 7/9 independently confirmed; 2/9 structurally present (citation eq-numbers)
confidence_within_scheme: HIGH
confidence_scheme_independent: MEDIUM (sign_forced=False is honest)
gaps: []
comparison_verdicts:
  - subject_kind: claim
    subject_id: "boson-vs-fermion relative sign (the crux)"
    reference_id: "Frolov-Fursaev hep-th/9607104 + textbook a_1(Dirac)"
    comparison_kind: benchmark
    verdict: pass
    metric: "Dirac:scalar signed induced-1/G ratio"
    threshold: "= +2 (same sign), conformal scalar = 0"
  - subject_kind: claim
    subject_id: "fermion is SAME sign as scalar (not Akama anti-gravity)"
    reference_id: "Tanaka PRD 53 6941 + Adler RMP 54 729 reconciliation"
    comparison_kind: prior_work
    verdict: pass
    metric: "per-Weyl induced-1/G sign"
    threshold: "positive (+1/6), folklore reconciled not adopted"
suggested_contract_checks:
  - check: "Gate 1 must verify a_1 is CLEANLY proportional to R[g] (no non-associative / wave-map target-curvature tr(F^2) contamination of the EH coefficient)"
    reason: "Gate 0 only establishes the SIGN of the R-coefficient; it does not establish that the induced curvature term is a clean integral-R. The squared fluctuation operator built from a non-associative wave-map kinetic term may not be a clean Laplace-type D^2=-(nabla^2+E) -- a real risk flagged by the research note Q6 and deferred to Gate 1."
    suggested_subject_kind: acceptance_test
    suggested_subject_id: "Gate-1-a1-proportional-to-R"
    evidence_path: "derivations/81-sakharov-RESEARCH.md (Q6)"
---

# Gate 0 (SIGN) Adversarial Verification — Phase 81, milestone v21.0

## ONE-LINE VERDICT

**SURVIVES (G > 0) — CONFIRMED.** The executor's surprising survival of the gate everyone
expected to kill withstands an independent re-derivation by three routes that do NOT reuse
the driver's code. The fermion induces `1/(16πG)` with the **same (positive) sign** as a
minimal scalar (signed weight `+1/3` per Dirac, `+1/6` per Weyl), not the opposite sign;
`STr = +8/3 > 0`; Gate 0 does not kill on sign. Confidence **HIGH within the committed
proper-time/cutoff vacuum scheme**, **MEDIUM scheme-independent** (the executor's
`sign_forced=False` hedge is honest and correct).

I genuinely tried to break it. I could not. The "fermions = anti-gravity (Akama/Adler)"
folklore is the wrong mental model (it tracks the statistics minus alone), and the
wrong-sign boson is indeed the massless vector, not the fermion.

---

## The decisive thing I had to break (and could not)

The entire verdict turns on ONE claim: a Dirac/Weyl fermion induces `1/(16πG)` with the
SAME sign as a minimal scalar. The executor's reasoning is the two-minus cancellation:
statistics `s=-1` (minus #1) times the Lichnerowicz bundle coefficient
`tr(E+R/6)=4(-1/4+1/6)=-1/3` (minus #2, itself negative) `= +1/3` (positive).

I re-derived the boson-vs-fermion relative sign by **three genuinely independent routes**,
none of which reuse `sakharov_gate0_sign.py`:

### Route 1 — My own Seeley-DeWitt a_2 heat-kernel re-derivation (from scratch, exact over Q)

Built the per-field signed coefficient `s · tr(E + R/6)` from primitives in a fresh script:

| Field | E (Lichnerowicz/non-minimal) | `tr(E+R/6)` (raw a_1) | statistics `s` | **signed → 1/G** |
|---|---|---|---|---|
| minimal scalar (ξ=0) | `E=0` | `+1/6` | `+1` | **`+1/6`** (G>0) |
| conformal scalar (ξ=1/6) | `E=-R/6` | `0` | `+1` | **`0`** |
| Dirac fermion | `E=-R/4`, tr 1 = 4 | `-1/3` (NEGATIVE) | `-1` | **`+1/3`** (G>0) |
| Weyl fermion | `E=-R/4`, ½ Dirac | `-1/6` | `-1` | **`+1/6`** (G>0) |

Relative to the minimal scalar: Dirac/scalar = **+2**, Weyl/scalar = **+1**, conformal = **0**.
**My independent derivation reproduces the executor's coefficients exactly. Dirac is the
SAME sign as the scalar.**

**Convention-robustness sub-test (the most important skeptic's attack):** the one
convention a skeptic would attack is `E=-R/4` vs `E=+R/4` (Vassilevich vs opposite-E-sign
split). I re-ran both conventions consistently (flipping the E-sign DEFINITION for *both*
scalar and Dirac, since they share the same `D²=-(∇²+E)` split). The signed Dirac:scalar
ratio came out **+2 in BOTH conventions** — it is convention-independent, because the
E-sign flip cancels between numerator and denominator. The crux does not hang on the one
convention choice that could plausibly hide a sign error.

### Route 2 — The published Frolov-Fursaev induced-G formula (web-confirmed, not from the driver)

Independently confirmed via web search (multiple result snippets, NOT the driver):
```
1/G = (1/12π) [ Σ_s (1 - 6ξ_s) m_s² ln m_s²  +  2 Σ_d m_d² ln m_d² ]
```
The scalar weight is `(1-6ξ)` and the Dirac weight is `+2`, **inside the same bracket with
the same `1/12π` prefactor and the same `m² ln m²` structure** ⇒ Dirac and scalar have the
**same overall sign**, ratio 2:1, and conformal scalar (ξ=1/6) gives exactly **0**. This is
an explicit FINAL formula for `1/G` (not an intermediate Tr-log), so the relative sign is
unambiguous. Matches Route 1 term-by-term.

### Route 3 — The bare textbook a_1 coefficient (web-confirmed, independent of the driver)

Web search returned the standard textbook values verbatim: *"For a minimal scalar field
a₀=1 and a₁=(1/6)R. For a Dirac spinor field a₀=2^{d/2} and a₁=−2^{d/2}(1/12)R."* In d=4,
`2^{d/2}=4`, so the Dirac `a₁ = −4·(1/12)R = −1/3 R` — **exactly the executor's raw Dirac
bundle coefficient −1/3, NEGATIVE before the statistics sign.** This independently confirms
minus #2.

**All three routes agree: the fermion is the SAME sign as the scalar.** If any route had
given the fermion the opposite sign, I would have reported DEAD. None did.

---

## The statistics sign (minus #1) — verified convention-independent

From first principles: a boson Gaussian integral gives `det(D²)^{-1/2}`, a fermion Grassmann
integral gives `det(D_Dirac)^{+1} = det(D²)^{+1/2}`. The **relative** statistics sign
fermion:boson `= -1` is therefore FORCED (opposite power of det ⇒ opposite Tr log),
independent of the overall sign convention for `W`. The prompt's "boson `-½Tr log`, fermion
`+½Tr log`" is one consistent labeling; the opposite overall labeling is equally valid; only
the relative `-1` matters and it is unambiguous. **Verified.**

The apparent contradiction in the web snippets ("fermions and scalars contribute with
opposite signs" vs "fermions same sign as scalars") is resolved: the first describes the
**raw a_1** (scalar `+1/6`, Dirac `-1/3` — genuinely opposite); the second describes the
**statistics-weighted signed contribution to 1/G** (scalar `+1/6`, Dirac `+1/3` — same).
Both are correct descriptions of different objects. The executor's claim is about the latter
and is correct.

---

## Akama/Adler reconciliation (the single most-likely-wrong place — chased hard)

I separated three logically distinct statements; only the first is the executor's claim:

- **(A) Signed per-field contribution to 1/(16πG)** in the cutoff vacuum scheme: scalar
  `+1/6`, Dirac `+1/3` (same sign), vector `-1/3` (opposite). **= the executor's claim.**
  Confirmed by all three routes above.
- **(B) The statistics factor alone** (a fermion loop carries an extra `-1` vs a boson loop):
  TRUE, but only HALF the story. `(A) = (B) × (minus #2)`. The "fermion = anti-gravity"
  folklore is the ERROR of stopping at (B) and forgetting the negative Lichnerowicz a_1.
- **(C) Adler RMP 54 (1982) 729 "the induced Newton constant is not positive in general":**
  TRUE, and it is a statement about the **net** induced G over a **realistic mixed spectrum**
  (which contains vectors — and vectors ARE negative) and about its **scheme/dynamics
  dependence** (the vacuum-condensate sign in the symmetry-breaking formulation). It does NOT
  assert "one Dirac fermion alone gives G<0." It is exactly the reason the executor sets
  `sign_forced=False`.

**Verdict on the folklore:** "fermions give G<0" is genuinely (b) the wrong mental model
(statistics-only) — NOT a clean per-fermion result that overturns the verdict. Where it
becomes true is (C) net-mixed-spectrum + scheme, which is honestly captured by
`sign_forced=False`. The executor reconciled this correctly.

**Independent corroboration — the Tanaka title-logic test.** Tanaka, *Three Generations or
More for an Attractive Gravity?* (PRD 53, 6941 (1996), hep-ph/9504259) concludes you need
**≥ 3 generations of chiral (quark/lepton) multiplets for ATTRACTIVE (G>0)** gravity. That
"three or MORE → attractive" logic only works if **adding fermions HELPS attraction** — i.e.
the chiral multiplet (Weyl + complex scalar) is net positive and adding more pushes G
positive. With the executor's Weyl `=+1/6`: chiral multiplet `= 2(1/6)+1/6 = +1/2` (strongly
positive ✓). With the strong "fermion = anti-gravity at −2× scalar" folklore: chiral
`= 2(1/6)+(-1/3) = 0`, so adding generations would do nothing — **contradicting Tanaka's
title.** The published induced-gravity literature's own logic is inconsistent with the
folklore and consistent with the executor.

> Note on the garbled-PDF trap: WebFetch on hep-ph/9504259 (a binary-unparseable PDF)
> *paraphrased* "fermions give a negative contribution." I did NOT use this — WebFetch
> on the garbled PDFs is unreliable (it admitted so on every arXiv PDF this session). The
> clean abstract-level snippets say "scalar/chiral **multiplet** positive, vector
> **multiplet** negative" — a statement about MULTIPLETS (fermion+scalar), which the
> garbled paraphrase collapsed into "fermion." The SUSY-multiplet signs alone do not even
> discriminate the bare-fermion sign (I checked: both w=+1/6 and w=-1/6 reproduce "chiral
> positive, vector negative"). The decisive evidence is the per-field a_1 (Routes 1+3) and
> Frolov-Fursaev's explicit +2 (Route 2).

---

## Scheme robustness (is SURVIVES an artifact of the chosen scheme?)

- The prompt **legitimately restricts** to Sakharov's zero-temperature proper-time/cutoff
  VACUUM (Casimir) scheme and BANS thermodynamics/horizons/entropy. Scheme choice is
  therefore allowed. The `sign_forced=False` hedge correctly records that (a) zeta vs cutoff
  can flip the *scalar* sign (Adler), and (b) a scalar wave-map admixture would carry a
  tunable ξ. Within the committed scheme the fermion sign is forced (Lichnerowicz fixes E,
  no ξ for a pure spinor). **The hedge is honest.**
- **Thermodynamic-ban compliance VERIFIED.** I scanned the driver: the banned tokens
  (entropy/horizon/ensemble/temperature) appear ONLY in (a) docstrings stating the ban, (b)
  the source-guard's forbidden-token list, and (c) the injected test-violation string. None
  is load-bearing decisive code. The driver's own AST source-guard enforces this and was
  demonstrated to FIRE on an injected violation (not a no-op). **Frolov-Fursaev is borrowed
  for its vacuum heat-kernel WEIGHTS only** (`(1-6ξ)`, `+2`); none of its black-hole-entropy
  or horizon logic enters. This is exactly the legitimate part of a black-hole-entropy paper.

---

## The other "also-verify" items

| Item | Status | Evidence |
|---|---|---|
| **STr arithmetic** `16×(+1/6) = 8×(+1/3) = +8/3` exact over Q | INDEPENDENTLY CONFIRMED | Recomputed in a fresh script `16·(s·tr(E+R/6)·½) = +8/3`; matches driver both counts. |
| **V_{1/2}=16 purely fermionic** (no bosonic partner) | INDEPENDENTLY CONFIRMED | 16 of Spin(10) = chiral spinor, dim `2^{(10-2)/2}=16`; Peirce `V_1(1)+V_{1/2}(16)+V_0(10)`; STr has only s=−1 terms, no `+` bosonic contributions. |
| **Non-hardwired verdict()** (v20-bug absent) | INDEPENDENTLY CONFIRMED | Fed FRESH synthetics the driver never tested: `verdict(+1/7)→SURVIVES`, `verdict(-1)→DEAD`, `verdict(5/3,circ=True)→DEAD-by-circularity`, `verdict(0)→INCONCLUSIVE`, `verdict(100)→SURVIVES`. The decisive boolean tracks `sign(STr)` and `circularity`, not a constant. |
| **R≠0 anchor** (M≠0 ⇒ R≠0; M=0 ⇒ R=0) | INDEPENDENTLY CONFIRMED | Re-ran the warm harness on a DIFFERENT matter sample/slice: `R = 558146594821824/71833701506287 ≠ 0` (exact rational), and `R=0` at M=0 (flat vacuum, slice-independent). The driver's locked sample also reproduces (R = 14187…/634906…). The R≠0 result is generic, not cherry-picked. |
| **Circularity = False** (G>0 from fermions' own E=-R/4, n_boson=0) | INDEPENDENTLY CONFIRMED | STr computed with zero bosons is already +8/3; no V_0/SUGRA partner imported. The positivity is the two-minus cancellation, not a boson balance. Honest. |
| **Massless vector −1/3 (the "wrong-sign boson")** | STRUCTURALLY PRESENT | I independently reproduced the *sign* (negative) and a defensible magnitude via the standard gauge+ghost counting (`4·(1/6) + tr(-Ric)/R = -1/3` gauge-only; `-2/3` with 2 ghosts). The exact magnitude is gauge/ghost-convention dependent (executor flagged MEDIUM); web-confirmed "vector multiplets generate a negative Newton constant." The SIGN — all the verdict needs — is robust and convention-independent. Non-load-bearing (vector ∉ V_{1/2}). |
| **Citations (Vassilevich §4, Frolov-Fursaev weights, Visser Table 1, Adler "not positive")** | STRUCTURALLY PRESENT | The arXiv PDFs are systematically binary-unparseable by WebFetch (as the research note warned). I confirmed the *content* (Frolov-Fursaev formula structure, the "scalar positive / vector negative" sign pattern, Adler "not positive in general", textbook a_1=−2^{d/2}(1/12)R for Dirac) via multiple independent search-engine snippets. The exact equation/table NUMBERS I could not byte-verify; the coefficients do not depend on them (derived three independent ways). |

---

## Computational oracle evidence (executed, with output)

Independent heat-kernel re-derivation (fresh script, not the driver), exact over Q:
```
minimal scalar (xi=0):   bundle tr(E+R/6) = 1/6  ; s=+1 ; signed = 1/6
conformal scalar(xi=1/6):bundle tr(E+R/6) = 0    ; s=+1 ; signed = 0
Dirac fermion (E=-R/4):  bundle tr(E+R/6) = -1/3 ; s=-1 ; signed = 1/3   (SAME sign as scalar)
Weyl fermion (1/2 Dirac):bundle (eff)     = -1/6 ; s=-1 ; signed = 1/6
>>> Dirac/scalar relative weight = 2 (SAME sign);  Weyl/scalar = 1;  conformal = 0
```
Convention-robustness (E-sign flip): Dirac:scalar signed ratio = **2 in BOTH conventions**.

Driver re-run (`python -u code/sakharov_gate0_sign.py`): `ALL_PASS = True`; STr=+8/3;
verdict ladder non-hardwired (synthetic −8/3→DEAD, +8/3&circ→DEAD-by-circularity);
R[g=e.e](M≠0)=14187524733311967018208791837/634906109300195099205387025 ≠ 0; R(M=0)=0.

Independent anchor (different sample): R = 558146594821824/71833701506287 ≠ 0; R(M=0)=0.

---

## Discrepancies / issues found

1. **(INFO, non-blocking) Stale convention_lock in state.json.** `.gpd/state.json`
   `convention_lock` still carries the v18.0/v20.0 conventions (Cl(9,0) gamma matrices,
   Berry-curvature sector, `generator_normalization T_a=(1/2)γ_a`, etc.), NOT a v21.0
   Sakharov lock. The load-bearing physics conventions for THIS gate (mostly-minus,
   `E=-R/4`, tr 1 = 4, `s=±1`, exact-over-Q) are carried inline in the SUMMARY / .tex /
   driver `ASSERT_CONVENTION` header and are the standard ones. No physics impact, but a
   notation-coordinator pass should refresh the lock for v21.0 if the milestone continues.

2. **(INFO, non-blocking) Spacetime sub-slice index labeling lag.** CONVENTIONS.md §
   spacetime sub-slice = `{17,18,19,26}`; the driver/harness use spacetime block
   `[1,2,3,10]` and V_{1/2} survivors `[11,18,19,26]` (the v18.0-Ph77 engine indexing). The
   R≠0 anchor reproduces correctly via the warm harness, so the indexing is internally
   consistent; only the CONVENTIONS.md label is older. Non-load-bearing for a SIGN gate
   (only R≠0 existence is needed).

3. **(NOTE, deferred by design) Gate 0 does not establish `a_1 ∝ R` cleanly.** It establishes
   only the SIGN of the R-coefficient. Whether the induced curvature term is a clean
   `∫R` (free of non-associativity / wave-map target-curvature `tr(F²)` contamination) is
   Gate 1's job and a genuine risk. Recorded as a `suggested_contract_check`, not a gap
   (Gate 0 was correctly scoped fail-fast).

No BLOCKER or SIGNIFICANT discrepancies. No sign error found. The verdict is sound.

---

## Confidence assessment

- **(i) Within the committed proper-time/cutoff vacuum scheme: HIGH.** The fermion sign is
  forced (Lichnerowicz fixes E, no ξ for a pure spinor), and three independent routes
  (my heat-kernel a_2, Frolov-Fursaev's explicit +2, the textbook bare a_1=−1/3) all give
  the fermion the SAME sign as the scalar. The two-minus cancellation is real and
  convention-independent. STr=+8/3 exact over Q.
- **(ii) Scheme-independent: MEDIUM.** This is the honest level, matching the executor's
  `sign_forced=False`. The scalar sign is genuinely scheme-sensitive (Adler), the scheme is
  a (legitimate, prompt-sanctioned) choice, and a hypothetical wave-map ξ admixture would
  un-force it. The MEDIUM rating is a feature, not a defect — the executor reported it
  correctly and did not overclaim "Sakharov works."

The only items below INDEPENDENTLY CONFIRMED are the exact citation equation-numbers (the
arXiv PDFs are binary-unparseable; content confirmed, numbers not byte-verified) and the
massless-vector magnitude (convention-dependent, non-load-bearing). Neither affects the
verdict.

---

## VERDICT

**Gate 0 SURVIVES (G > 0). The executor's sign is CORRECT; the route does NOT die at Gate 0.**
The fermion induces gravity with the same sign as a scalar; the "Akama/Adler fermions =
anti-gravity" prior is the wrong mental model (statistics-only); the wrong-sign boson is the
vector. Confidence HIGH within-scheme, MEDIUM scheme-independent (`sign_forced=False` honest).
The predicted real death is correctly deferred to Gate 2 (the v18 tensor-support mismatch).
