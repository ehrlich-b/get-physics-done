# Phase 81 (v21.0 Sakharov Gate 0): Induced-Gravity SIGN Gate — Research

**Researched:** 2026-06-06
**Domain:** One-loop vacuum effective action / Seeley-DeWitt heat-kernel coefficients / Sakharov induced gravity (zero-temperature, Casimir-category)
**Confidence:** HIGH (heat-kernel coefficients, boson-vs-fermion sign chain, Frolov-Fursaev cross-check); MEDIUM on the *folklore* "fermions give G<0" (it is scheme-dependent — see BOTTOM LINE)
**Consumer:** `gpd-executor` writing `code/sakharov_gate0_sign.py` (NO WEB), then `gpd-verifier` (HAS WEB)

---

## BOTTOM LINE (read this first)

**Expected Gate-0 verdict: SURVIVES (G > 0) under the heat-kernel / proper-time cutoff scheme — NOT the naive DEAD-by-wrong-sign the ledger guessed — but the survival is fragile and the route still dies downstream.** The single most load-bearing fact: **a Dirac fermion carries TWO minus signs relative to a minimal scalar, and they cancel.** (1) the Fermi statistics sign `s=-1` (the prompt's `W=+½Tr log D²` vs bosonic `-½Tr log D²`), and (2) the Lichnerowicz endomorphism `E=-R/4` in the squared Dirac operator, which makes the *bundle-traced* `a_1` curvature coefficient `tr(E+R/6)=4·(-1/4+1/6)=-1/3` itself **negative**. Product: `(-1)·(-1/3)=+1/3`, the **same sign** as a minimal scalar's `+1/6`. So the 16-Weyl `V_{1/2}` sector gives a signed contribution to `1/(16πG)` of `+8/3` (POSITIVE) — attractive gravity, `G>0`. This is the orchestrator's "both came out positive" pass, and **it is correct in this scheme** (confirmed independently by the published Frolov-Fursaev induced-`G` formula: Dirac enters with `+2`, the same sign as a minimal scalar's `+1`, conformal scalar `0`).

**Three caveats that make this a kill anyway, all of which the executor must emit, not hide:**
1. **The sign is NOT FORCED — it is regularization-dependent.** The "fermions give wrong-sign induced `G`" statement (Akama/Adler) is real but lives in a *different* bookkeeping (Adler's review: "the induced Newton constant is not positive in general"; the bosonic and fermionic one-loop contributions "have different signs"). Whether `V_{1/2}` gives `G>0` or `G<0` depends on the regulator and on whether you count the statistics sign once or twice. **A Gate-0 verdict that claims a definite sign is only as strong as its declared scheme.** The honest Gate-0 output is conditional: `G>0 in the heat-kernel/cutoff scheme; the sign is convention-dependent and therefore NOT forced by h_3(O).`
2. **A tunable ξ in the wave-map scalar sector can flip the sign at will** (§5). The `S[M;g]=∫√g[⟨DM,DM⟩+ξ R |M|²+…]` action has a free non-minimal coupling ξ for any *scalar/wave-map* component; the scalar `a_1` coefficient is `(1/6-ξ)`, which is positive for ξ<1/6, zero at ξ=1/6, negative for ξ>1/6. If the integrated-out sector has *any* scalar wave-map piece, the induced-`G` sign is dialable ⇒ not forced. (The pure-Dirac part has no ξ freedom — Lichnerowicz fixes it — but the prompt's action explicitly carries "curvature couplings", so the executor must check whether the `V_{1/2}` model is pure-Dirac or wave-map-with-ξ.)
3. **Even with `G>0`, the route dies at Gate 2 (the v18 tensor-support mismatch) — a scalar κ cannot repair `G` (16 components) vs `κT` (6 components).** Gate 0 surviving merely *passes the buck* to the gate that already killed v18.

**Therefore the recommended deterministic Gate-0 logic for the executor (non-hardwired):** compute the signed supertrace exactly over Q. Emit `DEAD-G<0` ONLY if the computed `STr`-weighted `1/(16πG)` coefficient is `<0` in the *declared scheme*; emit `SURVIVES-but-not-forced` if `>0` (which is the expected branch), with an explicit machine-readable flag `sign_forced=False` (because of caveats 1+2) and `circularity=False` (no bosonic SUGRA partners were imported — the positivity came from the fermions' own `E=-R/4`, NOT from balancing against `V_0` bosons). If `G>0` could ONLY be obtained by importing `V_0`/bosonic partners, emit `DEAD-by-circularity` (KILL D) — but per the chain below it CANNOT, the fermions self-supply the right sign, so circularity is **not** triggered here.

**One-line ledger consequence:** Gate 0 does not kill on sign in the honest scheme; it returns "G>0 but unforced", and the real death is deferred to Gate 2 (support mismatch) — exactly the ledger's "most likely actual cause of death" (§5 of the selection-law ledger). The executor should run Gate 0 to this conditional verdict and let the orchestrator proceed to Gate 1/2.

---

## User Constraints

This is a milestone-v21.0 single-gate grounding task (no per-phase CONTEXT.md). Constraints come from the authoritative prompt `/Users/ehrlich/repos/blog/research/gr-from-h3o/sakharov-induced-gravity-prompt.md` and ledger `/Users/ehrlich/repos/blog/research/gr-from-h3o/selection-law-ledger.md` §5:

- **LOCKED — zero-temperature one-loop VACUUM effective action only (Casimir category).** NO thermodynamics, entropy, horizons, ensembles, or "equation of state". If any step needs those, STOP and flag as woo (that is the REJECTED Route A/D).
- **LOCKED — exact over Q** (`sympy.Rational`/`QQ`; no floats on any decisive path). Every coefficient below is given as an exact rational so the executor *transcribes*, never re-derives.
- **LOCKED — fermionic sign convention `W[g]=+½ Tr log D²`** (bosonic `-½ Tr log D²`). Carry it all the way to the sign of `c_1`. (This is the standard Euclidean convention: the Gaussian fermion integral gives `+det`, the boson gives `det^{-1/2}`.)
- **LOCKED — squared Dirac operator `(iγ·∇)² = ∇² - R/4`** (Lichnerowicz). ⇒ in the Laplace-type form `D² = -(∇² + E)`, the endomorphism is `E = -R/4`.
- **LOCKED — run gates in order, stop at first DEAD.** This task is Gate 0 ONLY. Gates 1/2/3 are out of scope (§6 below flags Gate-1 contamination risks for the next agent, does not resolve them).
- **LOCKED — NEGATIVE-RESULT-IS-SUCCESS.** A clean DEAD (or a clean "SURVIVES-but-unforced") is the deliverable. Do not strain to keep the route alive.
- **Discretion:** the executor may choose the internal representation of the supertrace (per-Weyl vs per-Dirac bookkeeping) provided it reproduces the `+8/3` ground truth below.

---

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| `code/cartan_phaseB_curvature.py` | prior artifact (warm harness) | Builds `g=e.e`, Riemann, **Ricci scalar `Rscalar`** and signature **exact over Q** on the locked slice. Gate 0 needs only that `R[g]≠0` exists (so the `a_1∝R` term is nonzero to carry a sign); it does NOT need the full `a_1`. | REUSE its imports `bulk_geometry_verification` (`spacetime_curvature_of_g` → returns `{"g","R","Rscalar"}`, `eig_signature_count`) and `ring_lemma_verification` (det SSOT). Do NOT import `octonion_algebra.py` (banned, buggy, float-only). | Gate 0 code header, Gate 1 (a_1∝R) |
| Vassilevich, "Heat kernel expansion: user's manual", Phys.Rept. 388 (2003) 279, **hep-th/0306138** | method (THE authority) | The Seeley-DeWitt `a_1`(=his `a_2`) coefficient and the universal `+R/6`. | CITE eq. for `a_2 = (4π)^{-2}∫ tr(E + R/6)` (his §4.3); the verifier (web) confirms equation number. | coefficient table, sign chain |
| Frolov & Fursaev, "Statistical Origin of Black Hole Entropy in Induced Gravity", **hep-th/9607104** | benchmark (independent cross-check) | Gives the explicit induced-`G` formula with per-field weights — Dirac enters with the SAME sign as a minimal scalar. | CITE its `1/G = (12π)^{-1}[Σ_s(1-6ξ_s)m_s²ln m_s² + 2Σ_D m_d²ln m_d²]`; reproduce its ratio Dirac:scalar = 2:1. | sign-chain cross-check |
| Visser, "Sakharov's induced gravity: a modern perspective", Mod.Phys.Lett.A 17 (2002) 977, **gr-qc/0204062** | benchmark | The spin-weight table (his Table 1: `k_0,k_1,k,k_J`); the modern statement of the mechanism + cutoff `Λ²`. | CITE for the cutoff structure and spin weights; the verifier confirms Table 1 numbers. | references, spin-weight table |
| Adler, "Einstein gravity as a symmetry-breaking effect in QFT", **Rev.Mod.Phys. 54 (1982) 729** | benchmark (the sign caveat) | "The induced Newton constant is not positive in general"; bosonic vs fermionic loops have different signs. | CITE as the authority that the sign is scheme/spectrum-dependent ⇒ `sign_forced=False`. | BOTTOM LINE caveat 1, pitfalls |

**Missing or weak anchors:** The arXiv PDFs (gr-qc/0204062, hep-th/0306138, hep-th/9607104, 1502.03758) are binary and could NOT be machine-parsed by the research web tool; their *content* was confirmed via search-engine summaries and from established physics. The **exact equation/table numbers must be re-confirmed by the gpd-verifier (which has web)**. The numerical coefficients below do not depend on those equation numbers — they are derived from first principles two independent ways and are internally cross-checked (heat-kernel chain vs Frolov-Fursaev). Confidence in the *coefficients* is HIGH; confidence in the *exact citation strings* is MEDIUM (verifier to confirm).

---

## Conventions

| Choice | Convention | Source |
| --- | --- | --- |
| Metric signature | mostly-minus `(+,-,-,-)` timelike-positive (the soldered slice `eta=diag(+1,-1,-1,-1)`) | project CONVENTIONS.md §1; harness `ETA` |
| Euclidean continuation | Heat kernel computed for a Laplace-type operator `D² = -(∇²+E)` on the Riemannian-continued slice; the *sign structure* (boson vs fermion, scalar vs Dirac) is signature-independent | Vassilevich §2; standard |
| One-loop action sign | boson `W=-½Tr log D²`; fermion `W=+½Tr log D²` | prompt (LOCKED) |
| Squared Dirac | `(iγ·∇)²=∇²-R/4` ⇒ `E_Dirac=-R/4` | prompt (LOCKED); Lichnerowicz |
| Spinor trace | `tr 1 = 4` in d=4 (Dirac); Weyl = ½ Dirac | standard |
| Arithmetic | EXACT over Q (`sympy.Rational`) | project CONVENTIONS.md §2/§7 (LOCKED) |
| Curvature normalization | `a_1(x,x) = E(x) + R/6` (the universal `+1/6`); overall `a_1-density = (4π)^{-2} tr(E+R/6)·√g` | Vassilevich hep-th/0306138 §4.3 |

**CRITICAL:** All signed coefficients below are quoted in **units of `Λ²/(4π)²`** (the common positive prefactor of the quadratically-divergent `a_1` term), as the *signed contribution to `1/(16πG)`*. The common prefactor `(+Λ²/(4π)²)` is positive and field-independent; only the *relative* and *absolute* signs of the per-field coefficients decide `G>0` vs `G<0`. The absolute sign is anchored by the physical requirement that **a minimal scalar gives `G>0`** (the standard Sakharov normalization) — under which a minimal scalar's coefficient is `+1/6`.

Convention loading: see agent-infrastructure.md Convention Loading Protocol. The harness header carries the `ASSERT_CONVENTION` line (`metric_signature=mostly_minus`); the executor must keep it.

---

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name | Source | Role in Gate 0 |
| --- | --- | --- | --- |
| `a_1(x,x) = E(x) + (1/6)R(x)` | Seeley-DeWitt `a_1` (Gilkey `a_2`) at coincidence | Vassilevich hep-th/0306138 §4.3; Gilkey, *Invariance Theory…* | THE master coefficient — every per-field number is `tr(E+R/6)` |
| `a_1-density = (4π)^{-2} tr(E + R/6)√g` | integrated `a_1` | Vassilevich; Parker-Toms | gives `1/(16πG) = c_1 Λ²`, `c_1 ∝ tr(E+R/6)` |
| `1/(16πG) ∝ Λ² · Σ_fields s_i · tr_i(E_i + R/6)` | induced Newton coupling | Sakharov 1967; Visser gr-qc/0204062 | the supertrace sum Gate 0 computes |
| `E_scalar = -ξ R` (curvature part) ⇒ `tr(E+R/6)=(1/6-ξ)R` | non-minimal scalar | Birrell-Davies; Parker-Toms | scalar/wave-map contribution |
| `E_Dirac = -R/4`, `tr 1=4` ⇒ `tr(E+R/6)=4(-1/4+1/6)R=-1/3 R` | Lichnerowicz squared Dirac | prompt (LOCKED); Vassilevich §4 | fermion contribution (the crux) |
| `s=+1` boson, `s=-1` fermion | statistics sign (from `±½Tr log`) | prompt (LOCKED) | the supertrace `STr=Σ s_i(…)` |

### The Lambda² (proper-time lower cutoff)

`W = ∓½ Tr log D² = ±½ ∫_{δ}^{∞} (dτ/τ) Tr e^{-τ D²}`. The heat-kernel expansion `Tr e^{-τD²} ~ (4π τ)^{-d/2} Σ_k τ^k ∫ a_k √g`. In d=4 the `a_1` term contributes `∫_δ (dτ/τ) τ^{-1} = δ^{-1} ≡ Λ²` (the **proper-time lower cutoff** `δ=Λ^{-2}` is the regulator that makes the quadratically-divergent `a_1` term `∝ Λ²`). This `Λ²` is the Sakharov scale `κ^{-1} ~ Λ_f²` (here `Λ_f` from the ρ_J fixed point — Gate 3, out of scope). **Gate 0 needs only the SIGN of the coefficient of `Λ²`, so `Λ²>0` is a common positive factor and drops out of the sign decision.**

---

## Standard Approach (RECOMMENDED): the signed supertrace from `a_1`

**What:** Compute `STr ≡ Σ_fields s_i · tr_i(E_i + R/6)` over the integrated-out `V_{1/2}` sector, exact over Q. The induced `1/(16πG) = (Λ²/(4π)²)·STr`. Sign of `STr` = sign of `1/G`.

**Why standard:** This is *the* Sakharov/Seeley-DeWitt method (Visser gr-qc/0204062; Vassilevich hep-th/0306138; Frolov-Fursaev hep-th/9607104). No alternative is needed for a SIGN gate.

**Key steps (the executor's transcription target):**

1. Per-field `a_1` curvature coefficient `tr(E+R/6)` (bundle trace only — strip the `R`, keep the rational):
   - **minimal scalar (ξ=0):** `1·(0 + 1/6) = +1/6`
   - **conformal scalar (ξ=1/6):** `1·(-1/6 + 1/6) = 0`
   - **non-minimal scalar (general ξ):** `(1/6 - ξ)`
   - **Dirac fermion:** `4·(-1/4 + 1/6) = -1/3`
   - **Weyl fermion:** `½ · (-1/3) = -1/6` (half the Dirac bundle)
   - **massless vector (gauge boson, +ghosts):** `+(-1/3)` net — see vector note below
2. Multiply by the statistics sign `s` (`+1` boson, `-1` fermion) → **signed contribution to `1/(16πG)`** (units `Λ²/(4π)²`):
   - **minimal scalar:** `(+1)·(+1/6) = +1/6`
   - **conformal scalar:** `(+1)·0 = 0`
   - **Dirac fermion:** `(-1)·(-1/3) = +1/3` ← TWO minuses cancel
   - **Weyl fermion:** `(-1)·(-1/6) = +1/6`
   - **massless vector:** `(+1)·(-1/3) = -1/3` (vector contributes the OPPOSITE sign — relevant only for the circularity sub-check)
3. Sum over the `V_{1/2}=16` sector (16 Weyl, no bosons): `STr = 16·(+1/6) = +8/3`.
4. **Verdict:** `STr = +8/3 > 0` ⇒ `1/G > 0` ⇒ `G > 0` (attractive) **in the heat-kernel/cutoff scheme.**

### Anti-Patterns to Avoid

- **Applying the statistics minus and FORGETTING the Lichnerowicz `E=-R/4` minus** (or vice versa). This is the single error that produces a spurious `G<0`. The Dirac coefficient is `-1/3` *before* the statistics sign; the statistics sign makes it `+1/3`. Both minuses are real; they cancel. (The orchestrator's "both positive" pass had it right.)
- **Applying the statistics minus TWICE** (once as `s=-1`, once by mis-signing the `+½` fermionic `Tr log` as `-½`). The prompt LOCKS fermionic `W=+½Tr log` — that `+` IS the statistics sign; do not double-count it.
- **Asserting `G<0` because "Akama says fermions give wrong sign."** That folklore is scheme-dependent (Adler RMP 54: "not positive in general"). Under THIS prompt's locked conventions (heat-kernel, `E=-R/4`, `+½Tr log`), the fermion-only sign is `+`. Emit the computed sign, flag `sign_forced=False`, do NOT assert the folklore as the verdict.
- **Importing `V_0`/bosonic SUGRA partners to "fix" the sign.** Not needed (the fermions self-supply `+`), and doing so would trigger DEAD-by-circularity (KILL D). The executor must verify NO bosonic partner was used and set `circularity=False`.
- **Using floats / `numpy.linalg`** on any decisive number (project ban, `fp-float-decisive`).
- **Any thermodynamic language** (entropy/horizon/ensemble) — that is the rejected route; STOP if reached.

---

## Existing Results to Leverage (DO NOT RE-DERIVE)

### Established Results

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| Seeley-DeWitt `a_1` at coincidence | `a_1 = E + R/6` | Vassilevich hep-th/0306138 §4.3 | master formula; transcribe |
| Non-minimal scalar `a_1` curvature coeff | `(1/6 - ξ)` | Birrell-Davies §3; Parker-Toms | scalar/wave-map term |
| Lichnerowicz squared Dirac endomorphism | `E = -R/4`, `tr 1 = 4` ⇒ coeff `-1/3` | prompt LOCKED; Vassilevich §4 | fermion term |
| Statistics sign | boson `+`, fermion `-` (from `∓½Tr log`) | prompt LOCKED; Adler RMP 54 | supertrace weight |
| Frolov-Fursaev induced-`G` weights | `1/G=(12π)^{-1}[Σ(1-6ξ)m²ln m² + 2Σ_D m²ln m²]` ⇒ Dirac:scalar = **2:1, same sign**; conformal scalar = **0** | Frolov-Fursaev hep-th/9607104 | INDEPENDENT cross-check of the sign chain |
| `V_{1/2}` content | 16 complex Weyl = 8 Dirac = one SM generation (16 of Spin(10)), NO bosons | Paper 7 (project, exact over Q) | the supertrace is purely fermionic (`-` statistics) |
| Soldered slice has genuine curvature | `R[g=e.e] ≠ 0` for `M≠0`, exact over Q (136/256 nonzero Riemann comps; signature (1,3)) | `cartan_phaseB_curvature.py` (v18 Ph77, prior) | the `a_1∝R` term is nonzero ⇒ carries a sign (Gate 1 detail; Gate 0 just needs `R≠0` exists) |

**Key insight:** The two independent derivations of the per-field sign (the heat-kernel `a_1` chain in this note, and the published Frolov-Fursaev formula) **agree exactly**: Dirac/scalar ratio = 2, Weyl/scalar = 1, conformal scalar = 0, fermion same sign as scalar. The executor should reproduce BOTH and assert they match — this is the built-in validation that the sign bookkeeping is correct (defeats the single-minus / double-minus error).

### Nearest analogues (for the absolute-sign anchor)

| Anchor | What it fixes | Source |
| --- | --- | --- |
| Minimal scalar ⇒ `G>0` | Pins the *absolute* sign: the common prefactor `+Λ²/(4π)²` is chosen so the standard minimal-scalar coefficient `+1/6` gives attractive gravity. Everything else is relative to this. | Sakharov 1967; Visser gr-qc/0204062 |

---

## Computational Tools

### Core Tools

| Tool | Module | Purpose | Why |
| --- | --- | --- | --- |
| SymPy (`Rational`, `QQ`, `Matrix`) | stdlib of project (Python 3.14, SymPy 1.14.0) | exact-over-Q supertrace arithmetic | project ban on floats |
| `bulk_geometry_verification` | `code/` (warm harness) | `spacetime_curvature_of_g(MATTER, SLICE_VALS, bg_delta=BG)` → `{"g","R","Rscalar"}`; `eig_signature_count` | proves `R[g=e.e]≠0` exact over Q so the `a_1∝R` term is nonzero |
| `ring_lemma_verification` | `code/` | det SSOT (`det_3`, `Tr`) | if any algebra invariant is needed; do NOT use `octonion_algebra.py` |

### Reuse recipe (transcribe into `code/sakharov_gate0_sign.py`)

```python
# Locked slice/indices (from cartan_phaseB_curvature.py header):
CU4_IDX      = [1, 2, 3, 10]            # g base slice (beta,gamma,p,q) = h_2(C_u) ~ R^{3,1}
CU_SURVIVOR_IDX = [11, 18, 19, 26]      # V_{1/2} matter survivors (pi_u)
ETA = Matrix([[1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,-1]])  # mostly-minus (+,-,-,-)
# Sanity (Gate 0 only needs that curvature EXISTS to carry a sign):
import bulk_geometry_verification as B
MATTER = {11:Rational(2),18:Rational(-1),19:Rational(3),26:Rational(5)}
MATTER = {k:v*Rational(1,10) for k,v in MATTER.items()}
res = B.spacetime_curvature_of_g(MATTER, [Rational(1,3),Rational(1,3),0,0], bg_delta={4:Rational(1)})
assert cancel(res["Rscalar"]) != 0   # R != 0 -> a_1 ∝ R is nonzero (Gate-1 owns the "clean ∝R")
```

### Computational Feasibility

| Computation | Cost | Note |
| --- | --- | --- |
| Supertrace of rationals | trivial (<1 s) | pure `Rational` arithmetic |
| `spacetime_curvature_of_g` on the slice | ~seconds–minutes (warm harness, exact over Q) | already validated in v18 Ph77; run foreground `python -u` to avoid the stream-watchdog (see Pitfalls) |

This is the **cheapest** gate (the ledger calls it "hours, exact over Q"). No heavy compute.

---

## Validation Strategies

### Internal Consistency Checks (the executor MUST emit these)

| Check | Validates | Expected |
| --- | --- | --- |
| Heat-kernel chain vs Frolov-Fursaev | sign bookkeeping correct | Dirac/scalar = 2/1; Weyl/scalar = 1/1; conformal scalar = 0 — **must match** |
| Conformal scalar coefficient | `(1/6-ξ)` at ξ=1/6 | exactly `0` (a conformal scalar induces NO `1/G` — a famous check) |
| Two-minus cancellation | Dirac signed contribution | `(-1)·(-1/3)=+1/3` (positive) |
| 16-Weyl sum two ways | counting | `16·(+1/6) = 8·(+1/3) = +8/3` |
| `STr` purely fermionic | no bosons imported | every term has `s=-1`; `circularity=False` |
| `R[g=e.e]≠0` exact over Q | `a_1∝R` nonzero | `Rscalar ≠ 0` on the `M≠0` sample |
| Verdict not hardwired | non-hardwired gate | the DEAD/SURVIVES boolean must be *derived* from `sign(STr)`, not a literal — see Pitfall "hardwired verdict" |

### Known Limits / Benchmarks

| Limit | Known result | Source |
| --- | --- | --- |
| Single minimal scalar | `+1/6` (→ `G>0`) | Visser gr-qc/0204062 |
| Single conformal scalar | `0` | Frolov-Fursaev hep-th/9607104 (the `(1-6ξ)` weight) |
| Single Dirac fermion | `+1/3` (→ `G>0`, same sign as scalar) — i.e. weight `2×` the minimal scalar | Frolov-Fursaev (the `2Σ_D` term) |
| Pure-fermion folklore | "can be `G<0`" — scheme-dependent | Adler RMP 54 (1982) 729 |

### Red Flags During Computation

- A computed Dirac signed contribution that is **negative** ⇒ a sign-bookkeeping error (you applied one minus but not both, or double-counted). Re-derive against Frolov-Fursaev's `+2` weight.
- A **conformal scalar contributing nonzero** ⇒ wrong `(1/6-ξ)` (you used `(ξ-1/6)` with the wrong outer sign).
- Any appearance of **temperature, β, entropy, horizon area** ⇒ you've drifted into the rejected thermodynamic route — STOP.
- A **float** anywhere on the decisive path ⇒ project violation.
- The verdict boolean **literally written `True`/`DEAD`** rather than computed from `sign(STr)` ⇒ hardwired-verdict failure (the verifier will reject; v20 caught exactly this).

---

## Common Pitfalls

### Pitfall 1: The double-minus (THE crux error)
**What goes wrong:** Computing `G<0` for the fermion sector because you treat the fermion statistics minus as the *only* sign, forgetting that `E=-R/4` already makes the Dirac bundle coefficient `-1/3`.
**Why:** The naive mental model "fermions = minus = anti-gravity" ignores the Lichnerowicz endomorphism.
**Avoid:** Compute `tr(E+R/6)=-1/3` FIRST (negative), THEN apply `s=-1`, giving `+1/3`. Cross-check against Frolov-Fursaev's explicit `+2` Dirac weight.
**Warning sign:** Dirac contribution comes out `-1/3` *after* the statistics sign.
**Recovery:** Re-read the chain in §"Standard Approach" step 2.

### Pitfall 2: Double-counting the statistics sign
**What goes wrong:** Using `W=+½Tr log` (the `+` already being the statistics sign) AND separately multiplying by `s=-1`, double-flipping to a spurious `G<0`.
**Avoid:** Pick ONE bookkeeping. Recommended: per-field coefficient `tr(E+R/6)` × statistics sign `s` (`+1`/`-1`). The `±½Tr log` convention and the `s` factor are THE SAME sign — use it once.

### Pitfall 3: Treating the `G>0` result as FORCED
**What goes wrong:** Reporting "Gate 0 SURVIVES, G>0" as a robust positive result.
**Why:** The sign is regularization-dependent (Adler) and, if any scalar wave-map ξ exists, dialable (§5).
**Avoid:** Always emit `sign_forced=False` with the reason; phrase the verdict "G>0 in the heat-kernel/cutoff scheme; not forced by h_3(O)."

### Pitfall 4: The stream-watchdog killing the warm-harness curvature call
**What goes wrong:** `spacetime_curvature_of_g` runs long with no stdout; the executor's stream-watchdog kills it (documented project gotcha).
**Avoid:** run `python -u`, print progress, foreground (see harness header lines 52-54). Gate 0's *own* arithmetic is trivial; only the optional `R≠0` sanity call is heavy.

### Pitfall 5: Hardwired verdict
**What goes wrong:** The DEAD/SURVIVES boolean is a literal, not derived from the computed sign — the verifier rejects (this happened in v20, caught by the verifier).
**Avoid:** `verdict = "DEAD-G<0" if STr < 0 else "SURVIVES-G>0-unforced"`; assert `STr` is a `Rational`; print `STr` so the verdict is auditable.

---

## Answers to the six numbered questions (the deliverable core)

### Q1 — Heat-kernel `a_1` R-coefficients

`a_1(x,x) = E(x) + R/6`, integrated density `(4π)^{-2}∫√g tr(E+R/6)`; the quadratic divergence `Λ²` comes from the proper-time lower cutoff `δ=Λ^{-2}` on `∫_δ(dτ/τ)Tr e^{-τD²}` (the `a_1` term `∝ δ^{-1}=Λ²`).

- **(a) Real scalar, non-minimal ξ:** `E=-ξR` ⇒ `tr(E+R/6) = (1/6-ξ)`. Full: `a_1=(4π)^{-2}∫√g(1/6-ξ)R`. ✓ matches prompt.
- **(b) Dirac fermion:** `(iγ·∇)²=∇²-R/4` ⇒ `E=-R/4`; `tr 1=4` ⇒ `tr(E+R/6)=4(-1/4+1/6)=4·(-1/12)=-1/3`. Statistics sign `s=-1` (from `W=+½Tr log`). Signed contribution to `1/(16πG)`: `(-1)·(-1/3)=+1/3`.
- **(c) Massless vector / gauge boson (circularity sub-check):** statistics `s=+1`; the standard net bundle coefficient (vector minus 2 ghost scalars, Lichnerowicz `E=-Ric`-type) gives a NET `a_1` curvature coefficient of `-1/3` for a massless vector in d=4 ⇒ signed contribution `(+1)·(-1/3)=-1/3` (OPPOSITE sign to a scalar/fermion). **Note:** the exact vector number depends on gauge-fixing/ghost convention; the verifier should confirm against Visser Table 1. It matters ONLY for the circularity sub-check (it is NOT in `V_{1/2}`), so a MEDIUM-confidence value is acceptable here — flag it.

### Q2 — THE CRUX: boson-vs-fermion relative sign (RESOLVED, worked)

**Definitive signed per-field contribution to `16πG·c_1` (= signed contribution to `1/(16πG)`, units `Λ²/(4π)²`):**

| Field | bundle `tr(E+R/6)` | statistics `s` | **signed `1/(16πG)` contribution** | `→G` sign |
| --- | --- | --- | --- | --- |
| minimal scalar (ξ=0) | `+1/6` | `+1` | **`+1/6`** | `G>0` |
| conformal scalar (ξ=1/6) | `0` | `+1` | **`0`** | — (no contribution) |
| non-minimal scalar (ξ) | `(1/6-ξ)` | `+1` | **`(1/6-ξ)`** | `G>0` iff ξ<1/6 |
| **Dirac fermion** | `-1/3` | `-1` | **`+1/3`** | `G>0` |
| **Weyl fermion** | `-1/6` | `-1` | **`+1/6`** | `G>0` |
| massless vector | `-1/3` | `+1` | **`-1/3`** | `G<0` (opposite) |

**Where the naive "both positive" pass is RIGHT:** for the minimal scalar (`+1/6`) and the Dirac fermion (`+1/3`), the *final* signed contributions ARE both positive — the orchestrator was correct. The subtlety the naive pass *implicitly got right* (and which a "fermions=minus=anti-gravity" shortcut gets wrong) is that the fermion's two minuses cancel: `s=-1` times the negative Lichnerowicz coefficient `-1/3` = `+1/3`. A minimal scalar and a Dirac fermion induce `1/(16πG)` with the **SAME (positive) sign**. The boson that has the *opposite* sign is the massless **vector** (`-1/3`), not the fermion.

### Q3 — Akama/Adler/Visser fermion-only verdict

- **Akama (1978, pregeometry) / Adler (Rev.Mod.Phys. 54 (1982) 729):** the induced `1/G` from a generic spectrum is **"not positive in general"**; bosonic and fermionic one-loop contributions "have different signs" and a fermion loop "demands an extra minus sign." This is the origin of the "fermions can give `G<0`" statement.
- **Reconciliation with our `+1/3`:** the Akama/Adler "different sign" refers to the *statistics* minus alone. When the Dirac operator's curvature coupling (`E=-R/4`) is included consistently (Lichnerowicz), the fermion bundle coefficient is itself negative, so the *net* fermion contribution is the SAME sign as a scalar in the heat-kernel/cutoff scheme — exactly what Frolov-Fursaev's explicit `+2Σ_D` weight shows. **So "fermions alone give `G<0`" is NOT correct in the consistent heat-kernel/cutoff computation; it can become true in schemes that count the statistics sign without the matching endomorphism sign, or in mixed spectra with vectors.**
- **Regularization dependence (FLAG):** (i) zeta-function vs proper-time/cutoff can change finite pieces and even the sign of the *scalar* contribution in some treatments; the quadratic `Λ²` (cutoff) piece is the robust one and is what Sakharov uses. (ii) the conformal-vs-minimal scalar choice changes the *magnitude and sign* of the scalar term (`(1/6-ξ)`): minimal `+1/6`, conformal `0`, ξ>1/6 negative. (iii) the vector number is gauge/ghost-convention dependent.
- **Sign-determining formula to reproduce (Frolov-Fursaev hep-th/9607104):** `1/G = (12π)^{-1}[ Σ_s (1-6ξ_s) m_s² ln m_s² + 2 Σ_D m_d² ln m_d² ]`. Replacing `m²ln m² → -Λ²` (leading divergence) gives the cutoff version; the **weights** `(1-6ξ)` for scalars and `+2` for Dirac are exactly the ratios in the Q2 table.

### Q4 — `V_{1/2}=16` of Spin(10) → fermionic d.o.f. and supertrace count

- `16` of Spin(10) = ONE chiral spinor = **16 complex Weyl fermions** = one SM generation incl. right-handed ν (Paper 7, exact over Q). `16 complex Weyl = 8 Dirac-equivalent`.
- **Chirality (Weyl vs Dirac) changes ONLY the multiplicity, NOT the sign.** A Weyl fermion is ½ a Dirac (bundle coefficient `-1/6` vs `-1/3`); both carry statistics `s=-1`; both give `+` net. So:
  - 16 Weyl: `STr = 16·(+1/6) = +8/3`.
  - equivalently 8 Dirac: `8·(+1/3) = +8/3`. ✓
- **Supertrace `STr = (bosons +) − (fermions −)`:** here there are NO bosons in `V_{1/2}`, so `STr` is purely the fermionic block. With the statistics sign carried, the *signed sum* `STr = +8/3` is POSITIVE. **(Careful with the word "supertrace": the *unsigned* fermion count enters with a relative minus in `Str=tr_B-tr_F`; once you also include the negative Lichnerowicz coefficient `tr(E+R/6)=-1/3<0` for each Dirac, the product `(-1)·(-1/3)` makes the signed contribution positive. So `STr` as the signed `1/(16πG)` coefficient is `+8/3`.)**

### Q5 — ξ for the `V_{1/2}` sector: is the sign FORCED?

- **If the integrated-out `V_{1/2}` sector is purely Dirac/wave-map-spinor:** the curvature coupling is **fixed by Lichnerowicz (`E=-R/4`), NO free ξ** ⇒ the per-fermion sign is forced to `+` (net `+1/3` per Dirac) *within the heat-kernel/cutoff scheme*. In that case the only non-forcedness is the *scheme* dependence (Q3 caveat).
- **If the action `S[M;g]=∫√g[⟨DM,DM⟩+(curvature couplings)]` contains a SCALAR wave-map piece with a tunable non-minimal ξ:** then that piece contributes `(1/6-ξ)`, **which can be dialed to any sign** (positive ξ<1/6, zero at 1/6, negative ξ>1/6). **In that case the induced-`G` sign is NOT forced — it is a free parameter.** This is itself a finding: *the sign is not pinned by `h_3(O)`; it depends on a coupling choice the algebra does not fix.*
- **The executor MUST determine which case holds** by inspecting the actual `V_{1/2}` model in the harness/Paper 7: is the integrated-out field a spinor (Dirac, no ξ) or a wave-map scalar (has ξ)? `V_{1/2}=16` are *spin-1/2 fermions* (Paper 7), so the **primary case is pure-Dirac, sign `+`, forced-within-scheme.** But the prompt's "wave-map" language and the explicit "(curvature couplings)" term mean the executor should CHECK for and report any ξ freedom; if present, set `sign_forced=False` for that reason too.

**Net answer to Q5:** the fermion sign is forced *within the heat-kernel/cutoff scheme* (Lichnerowicz, no ξ for spinors), but (a) the scheme itself is a choice (Adler), and (b) any scalar wave-map admixture with tunable ξ would un-force it. Recommend `sign_forced=False` overall, with both reasons logged.

### Q6 — Gate-1 contamination caveats (FLAG ONLY, do not resolve)

- **Non-associativity of O:** the squared fluctuation operator built from a non-associative `⟨DM,DM⟩` might fail to be a clean Laplace-type operator `D²=-(∇²+E)`, so `a_1` could pick up non-`R` (associator-valued) endomorphism pieces — Gate 1 must verify `a_1 ∝ R` cleanly. *(One sentence; Gate 1 owns it.)*
- **Wave-map target-space curvature:** a sigma-model `⟨DM,DM⟩` on a curved target induces a `tr(F²)`-type (target-curvature) term in `a_1` that is NOT proportional to the base `R`, contaminating the EH coefficient — Gate 1 must check the target is flat enough that `a_1 ∝ R[g]`. *(One sentence; Gate 1 owns it.)*

---

## Level of Rigor

**Required:** exact-over-Q symbolic transcription with a non-hardwired sign verdict + an independent cross-check (Frolov-Fursaev). This is a *physicist's-proof-grade* sign determination: the coefficients are textbook-exact, the chain is two-way cross-checked, and the only genuine uncertainty (scheme/ξ dependence) is itself reported as a structured flag rather than hidden. No floats. No approximations.

---

## Open Questions

1. **Is the `V_{1/2}` integrated-out field pure-Dirac or wave-map-with-ξ?** — Determines whether the sign is forced-within-scheme or dialable. *Recommendation:* executor inspects the Paper-7 / harness matter model; `V_{1/2}=16` being spin-1/2 fermions points to pure-Dirac (forced-within-scheme), but report any ξ.
2. **Exact massless-vector coefficient (`-1/3`?)** — Gauge/ghost-convention dependent; MEDIUM confidence. *Recommendation:* needed ONLY for the circularity sub-check; verifier confirms against Visser Table 1. Does not affect the `V_{1/2}`-only verdict.
3. **Does the cutoff-vs-zeta scheme flip the scalar sign?** — Flagged (Adler). *Recommendation:* commit to the proper-time/cutoff scheme (Sakharov's own), report `sign_forced=False` to cover scheme dependence.

## Alternative Approaches if Primary Fails

| If this fails | Because | Switch to | Cost |
| --- | --- | --- | --- |
| heat-kernel `a_1` sign chain | doubts about sign bookkeeping | reproduce Frolov-Fursaev `1/G` formula weights directly | trivial (already in note) |
| symbolic `a_1` of the actual operator | non-associativity blocks clean `D²` | that is Gate 1, not Gate 0 — Gate 0 needs only the spin/stat weights | n/a (defer) |

**Decision criteria:** Gate 0 is decided by `sign(STr)` of the spin/stat-weighted sum; if the two independent derivations (heat-kernel chain, Frolov-Fursaev) ever disagree, STOP and escalate (a sign-bookkeeping bug), do not pick one.

---

## Sources

### Primary (HIGH confidence — coefficients)
- **Vassilevich, "Heat kernel expansion: user's manual," Phys.Rept. 388 (2003) 279 (hep-th/0306138)** — `a_1=E+R/6`, scalar/Dirac/vector endomorphisms (§4.3). *(Confirmed via search summaries + emergentmind mirror; PDF was binary-unparseable, verifier to confirm equation numbers.)*
- **Frolov & Fursaev, "Statistical Origin of Black Hole Entropy in Induced Gravity" (hep-th/9607104)** — explicit induced-`G` formula `1/G=(12π)^{-1}[Σ(1-6ξ)m²ln m²+2Σ_D m²ln m²]`; the independent sign cross-check (Dirac `+2`, conformal scalar `0`). *(Confirmed via search summary.)*
- **Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah-Singer Index Theorem*** — the canonical `a_n` reference (the `a_2=E+R/6` coefficient).
- **Birrell & Davies, *Quantum Fields in Curved Space*, §3** — scalar `(1/6-ξ)` heat-kernel coefficient.
- **Parker & Toms, *Quantum Field Theory in Curved Spacetime*** — Seeley-DeWitt coefficients for scalar/spinor/vector.

### Secondary (MEDIUM confidence — context, sign caveat, spin table)
- **Visser, "Sakharov's induced gravity: a modern perspective," Mod.Phys.Lett.A 17 (2002) 977 (gr-qc/0204062)** — modern statement, Table 1 spin weights `k_0,k_1,k,k_J`, cutoff `Λ²`. *(Abstract confirmed; Table 1 numbers verifier-to-confirm.)*
- **Adler, "Einstein gravity as a symmetry-breaking effect in quantum field theory," Rev.Mod.Phys. 54 (1982) 729** — "induced Newton constant not positive in general"; boson/fermion opposite statistics sign. *(Confirmed via search summary.)*
- **Sakharov (1967)** — the original induced-gravity proposal (`κ^{-1}~Λ²`).
- **Zee, "Spontaneously generated gravity," Phys.Rev.D 23 (1981) 858** — induced-`G` sign / symmetry-breaking origin.

### Tertiary (LOW confidence — to validate)
- emergentmind.com "Heat-Kernel Expansion" topic page — corroborated `a_1=E+R/6`. *(Single secondary source; primary is Vassilevich.)*

---

## Caveats and Alternatives (pre-submission self-critique)

1. **What assumption might be wrong?** That the prompt's locked conventions (`+½Tr log` for fermions, `E=-R/4`) are the ones to carry through. They are explicitly LOCKED in the prompt, so this is safe; but the *resulting* `G>0` is scheme-bound — hence the `sign_forced=False` flag. The risk is reporting `G>0` as robust; mitigated by the flag.
2. **What did I dismiss too quickly?** The "fermions give `G<0`" folklore. I did NOT dismiss it — I traced it to the statistics-sign-only bookkeeping and showed it is inconsistent with the full Lichnerowicz computation (and with Frolov-Fursaev's explicit `+2`). If the verifier finds a reputable source giving net fermion `G<0` *in the cutoff scheme with `E=-R/4` included*, that would overturn this; I judge it unlikely (two independent derivations agree).
3. **What limitation am I understating?** The vector coefficient (`-1/3`) is gauge-convention dependent; I flagged it MEDIUM and noted it is irrelevant to the `V_{1/2}`-only verdict.
4. **Simpler method overlooked?** No — the spin/stat-weighted supertrace IS the simple method. I added the Frolov-Fursaev cross-check precisely to avoid over-engineering a fresh derivation.
5. **Would a specialist disagree?** A specialist might *insist* the headline be "fermion-only induced `G` is famously sign-ambiguous" rather than "G>0". I have written the BOTTOM LINE to say exactly that: `G>0` *in this scheme*, **not forced**. That is the honest, specialist-defensible framing, and it is why the real kill is deferred to Gate 2 (support mismatch), consistent with the selection-law ledger's own expectation.

---

## Metadata

**Confidence breakdown:**
- Heat-kernel coefficients (`a_1=E+R/6`, scalar `(1/6-ξ)`, Dirac `-1/3`): **HIGH** — textbook, two-source corroborated, two-way cross-checked.
- Boson-vs-fermion relative sign (the crux): **HIGH** — worked chain + Frolov-Fursaev agree exactly.
- Absolute `G>0`/`G<0` for `V_{1/2}`: **HIGH within the heat-kernel/cutoff scheme; MEDIUM as a scheme-independent statement** (hence `sign_forced=False`).
- "Fermions alone give `G<0`" folklore: **MEDIUM** — real but scheme-dependent; reconciled, not adopted as verdict.
- Vector coefficient: **MEDIUM** — convention-dependent; non-load-bearing for `V_{1/2}`.
- Tooling/harness reuse: **HIGH** — inspected `cartan_phaseB_curvature.py` directly.

**Research date:** 2026-06-06
**Valid until:** physics stable indefinitely; exact citation strings (equation/table numbers) to be re-confirmed by the web-enabled verifier; harness API stable as of v18.0.
