# Phase 81 (v21.0 Sakharov Gate 0): SIGN of the induced Newton constant — EXECUTOR SUMMARY

**Executed:** 2026-06-06
**Scope:** Gate 0 ONLY (fail-fast pre-flight KILL gate). Gates 1/2/3 NOT run.
**Driver:** `code/sakharov_gate0_sign.py` (exact over Q; `python -u` foreground; byte-identical across 3 runs)
**Derivation:** `derivations/81-sakharov-gate0.tex` (well-formed; pdflatex unavailable in-env, NOT compiled)

---

## VERDICT: SURVIVES (G > 0)

`STr = +8/3` (exact over Q) ⇒ induced `1/(16 pi G) = (Lambda^2/(4pi)^2)*(+8/3) > 0` ⇒ **induced G > 0 (attractive)**, in Sakharov's proper-time/cutoff VACUUM scheme (Casimir-category, zero-temperature, NO thermodynamics).

- **`sign_forced = False`** — (a) the scheme is a choice (Adler RMP 54: "not positive in general"; cutoff-vs-zeta can flip the scalar sign); (b) any scalar wave-map admixture carries a tunable `xi` via `(1/6 - xi)`. The integrated-out field is PURE-DIRAC (see below), so the fermion sign IS forced *within* the scheme, but the scheme choice makes the overall sign unforced.
- **`circularity = False`** — `G>0` arises from the V_{1/2} fermions' OWN Lichnerowicz `E=-R/4`; ZERO bosonic/V_0 partners imported (`n_boson=0`). KILL D (circular GST structure) NOT triggered. Derived from `n_boson=0`, not hardcoded.

**[CONFIDENCE: HIGH within the proper-time/cutoff scheme]** — the per-field heat-kernel coefficients are textbook-exact, and two genuinely independent derivations (heat-kernel `a_1` chain AND the published Frolov-Fursaev induced-G weights) agree term-by-term over Q. **[CONFIDENCE: MEDIUM as a scheme-independent statement]** — hence `sign_forced=False`.

This CONTRADICTS the prompt's prior ("expected DEAD at Gate 0, wrong sign"). That prior rested on the Akama/Adler folklore, which tracks the statistics minus ALONE; with the Lichnerowicz endomorphism included consistently the net fermion sign is positive. Reported at true strength: `G>0` in this scheme, unforced — NOT "Sakharov works" (it passes only the cheapest gate).

---

## The exact-over-Q numbers

### Per-field signed contribution to `1/(16 pi G)` (units `Lambda^2/(4pi)^2`), built from primitives `s * tr(E + R/6)`:

| Field | E coeff | `tr(E+R/6)` | stat `s` | **signed** | → G |
|---|---|---|---|---|---|
| minimal scalar (xi=0) | `0` | `+1/6` | `+1` | **`+1/6`** | G>0 |
| conformal scalar (xi=1/6) | `-1/6` | `0` | `+1` | **`0`** | — (no 1/G) |
| Dirac fermion | `-1/4` | `-1/3` | `-1` | **`+1/3`** | G>0 |
| Weyl fermion | `-1/4` | `-1/6` | `-1` | **`+1/6`** | G>0 |
| massless vector (circularity-only) | n/a | `-1/3` | `+1` | **`-1/3`** | G<0 |

### THE CRUX — the two-minus cancellation (explicit in the code, never hardcoded):
- minus #2 = Lichnerowicz `E=-R/4` ⇒ Dirac bundle coeff `4*(-1/4 + 1/6) = -1/3` (NEGATIVE).
- minus #1 = Fermi statistics `s = -1`.
- product `(-1)*(-1/3) = +1/3` (POSITIVE) — the SAME sign as a minimal scalar. The boson with the OPPOSITE sign is the VECTOR (`-1/3`), not the fermion.

### Supertrace for V_{1/2} (16 Weyl, no bosons), two counts agree:
`STr = 16 * (+1/6) = 8 * (+1/3) = +8/3` (exact over Q; `n_boson = 0`).

### Dual cross-check (heat-kernel chain vs Frolov-Fursaev induced-G weights) — MATCH:
| field | heat-kernel (rel. to scalar) | Frolov-Fursaev | match |
|---|---|---|---|
| minimal scalar | 1 | 1 | OK |
| conformal scalar | 0 | 0 | OK |
| Dirac | 2 | 2 | OK |
| Weyl | 1 | 1 | OK |

Frolov-Fursaev hep-th/9607104: `1/G = (12pi)^{-1}[Σ(1-6xi)m²ln m² + 2Σ_D m²ln m²]` ⇒ Dirac:scalar = 2:1, Weyl:scalar = 1:1, conformal = 0. Agreement defeats the single-/double-minus error.

### R ≠ 0 anchor (warm v18-Ph77 harness `spacetime_curvature_of_g`, the only heavy call, ~2.5 s):
- `R[g=e.e] | M≠0 = 14187524733311967018208791837/634906109300195099205387025 ≠ 0` (exact over Q) ⇒ the induced `a_1 ∝ R` term is a NONZERO term (not vacuous).
- `R[g=e.e] | M=0 = 0` (the B1-derived flat Minkowski vacuum — correct flat-vacuum reference).

### PURE-DIRAC vs wave-map finding (Q5):
`V_{1/2} = 16 of Spin(10)` is a chiral spinor = purely fermionic (Paper 7 / harness Peirce half-eigenspace, engine `[11..26]`). NO wave-map scalar with tunable `xi`; Lichnerowicz fixes `E=-R/4`. ⇒ fermion sign forced WITHIN scheme.

---

## What it means for the selection-law ledger

Gate 0 does **NOT** kill the Sakharov route on sign. In the honest (scheme-aware) statement the induced `G > 0`, so the route lives to Gate 1 — and the predicted real death is deferred to **Gate 2** (the v18 tensor-support mismatch: a scalar induced `kappa` cannot repair `G`'s 16 independent components vs `kappa T`'s 6). This is exactly the ledger's "most likely actual cause of death." A clean SURVIVES-but-unforced at Gate 0 is the deliverable (negative-result-is-success: the cheap sign kill the prior expected did NOT materialize, because the wrong-sign boson is the vector, not the fermion).

---

## Per-gate status (one sentence each)

- **Gate 0 (SIGN)** — **DONE**: SURVIVES (G>0, STr=+8/3 exact over Q, sign_forced=False, circularity=False); does NOT kill.
- **Gate 1 (a_1 ∝ R)** — NOT RUN (fail-fast; deferred — Gate 1 owns the clean `∫R`, free of non-associativity / wave-map target-curvature contamination).
- **Gate 2 (SUPPORT MISMATCH)** — NOT RUN (the predicted real death: the v18 16-vs-6 component mismatch a scalar `kappa` cannot repair).
- **Gate 3 (CLOSURE)** — NOT RUN (deferred; pin `Lambda_f` from the rho_J fixed point and test `G[g]=kappa T` closure).

---

## Conventions (locked, v18.0; carried)

| Choice | Value | Source |
|---|---|---|
| Metric signature | mostly-minus `(+,-,-,-)`, timelike-positive | `convention_lock`; harness `ETA` |
| Scheme | proper-time/cutoff VACUUM (Casimir; zero-T; NO thermodynamics) | prompt (LOCKED) |
| One-loop sign | boson `W=-½Tr log D²`; fermion `W=+½Tr log D²` (`s=±1`) | prompt (LOCKED) |
| Squared Dirac | `(iγ·∇)²=∇²-R/4` ⇒ `E=-R/4` (Lichnerowicz) | prompt (LOCKED) |
| Spinor trace | `tr 1 = 4` (d=4); Weyl = ½ Dirac | standard |
| Heat-kernel `a_1` | `a_1 = E + R/6` (universal `+1/6`) | Vassilevich hep-th/0306138 §4.3 |
| Arithmetic | EXACT over Q (`sympy.Rational` only; NEVER float) | `convention_lock` (LOCKED) |
| det SSOT / banned | `ring_lemma_verification.py`; `octonion_algebra.py` BANNED | project |

---

## Guards / reproducibility

- **Source guard** clean + FIRES on injection: no `numpy.linalg` / `float(...)` / thermodynamic-route token (entropy/horizon/ensemble/temperature) in any decisive-function code; `octonion_algebra` absent from `sys.modules`. Guard proven to fire on an injected violation (not a no-op).
- **Non-hardwired verdict** self-tested: synthetic `STr=-8/3 → DEAD (G<0)`; synthetic `STr=0 → INCONCLUSIVE`; synthetic `STr=+8/3 & circular → DEAD-by-circularity`; real `STr=+8/3 → SURVIVES`. The decisive boolean is DERIVED from `sign(STr)`, not a constant (pre-empts the v20 hardcoded-decisive-boolean bug the verifier caught).
- **Reproducible:** all decisive rationals printed; byte-identical decisive output across 3 runs (no float, no RNG, no Date/clock on a decisive path — only the wall-clock timing breadcrumbs differ).
- `ALL_PASS = True` (all mechanical checks pass).

**Notes for the verifier (HAS web):** confirm the exact citation strings — Vassilevich hep-th/0306138 §4.3 (`a_1=E+R/6`), Frolov-Fursaev hep-th/9607104 (the `(1-6xi)`/`+2` weights), Visser gr-qc/0204062 Table 1 (spin weights + the massless-vector `-1/3`, which is gauge/ghost-convention dependent and non-load-bearing for the V_{1/2}-only verdict), Adler RMP 54 (1982) 729 (the "not positive in general" sign caveat). The numerical coefficients do not depend on these equation numbers (derived two independent ways, internally cross-checked).
