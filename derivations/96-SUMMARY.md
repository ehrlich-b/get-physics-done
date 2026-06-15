# Phase 96 / v36.0-candidate — SUMMARY: the FIELD-FAITHFULNESS CLAMP gate

**One-liner:** Field faithfulness `M(x) = φ[M](x)` on CP² = h₃(ℂ_u) carries **NO local
base-derivative term** — the faithfulness operator `L_F` is the pointwise algebraic
`−Tr(h²)`/Fisher–Bures Hessian plus a nonlocal rank-1 global-mean correction, with the local
Laplacian (`Δ_FS`) coefficient **identically 0** exact over ℚ; verdict **`DEAD-POINTWISE`** at
Gate 0, the clamp `δF=0 ⟺ δΓ=0` is FALSE, **fork A is PROVEN** (self-modeling provably cannot reach
the base metric). The single un-run gravity gate is now closed.

**Driver:** `code/faithfulness_clamp.py` — fresh, self-contained, exact over ℚ, non-hardwired
`verdict()` with §7 self-tests, certified anchors reproduced. **24/24 PASS, exit 0, ~0.7 s.**
**Commits:** `8aadfe14`, `f5d6ee7d`, `09202541`.

---

## §1 — Gate table

| Gate | Question | Result | Decisive fact (exact over ℚ) |
|------|----------|--------|------------------------------|
| **anchors** | reproduce the certified objects | **PASS** | `ε = λ_L − 2Λ = 32 − 12 = 20`; v35 `A_ii ≡ Var = 1/2 @ d1@P0`; `G_M` decomposition holds at all 4 s9 ground points |
| **source guard** | Bug-guard 5 (NO-CIRCULARITY) + Bug-guard 4 (WOO) | **PASS** | no `R`/`Ric`/`Riemann`/`Einstein`/`Lichnerowicz`/`tensor_probe` token, no thermo token, in the Gate-0 code; guard FIRES on injection |
| **Gate 0** | does field faithfulness carry a genuine local base-derivative term? | **DEAD-POINTWISE** | local-`Δ_FS` coefficient **≡ 0** across all 3 readings of `⟨·⟩_ρ`; `L_F` = pointwise Fisher Hessian − rank-1 global-mean |
| Gate 1 | write `F[M(x)]` | **NOT REACHED** | Gate 0 decisive DEAD |
| Gate 2 | `δF=0` vs `δΓ=0` | **NOT REACHED** | — |
| Gate 3 | does the match pin `κ_ind`? | **NOT REACHED** | `κ_ind` stays FREE (v34 ratio) |

The verdict ladder is **non-hardwired**: the §7 self-tests prove it returns DEAD-POINTWISE,
ALIVE / ALIVE-THROUGH-GATE-3, DEAD-WRONG-DERIVATIVE, INCONCLUSIVE on the matching rigged controls
(5 distinct verdicts under synthetic inputs).

---

## §2 — The decisive `L_F` form + coefficient (exact over ℚ)

The φ-fixed-point's **only** non-locality is the ensemble expectation `⟨l_i⟩_ρ` (read off the
φ-iteration F2 = `det·Σ(l_i − ⟨l_i⟩_ρ)²`, F3 = `det·Σ l_i(l_i − ⟨l_i⟩_ρ)`, which produce the
faithful fixed point `ρ_J = det(σ₂ − 1/3)`; faithful = the I/3 center). Promoting to a field
`M(x)`, linearizing `M(x) = M̄ + ε h(x)` at a **structured off-faithful** `M̄ = s01`:

```
L_F[h](x)  =  ( ⟨{M̄,h},p(x)⟩ − 2⟨M̄,p(x)⟩⟨h,p(x)⟩ )           ←  pointwise −Tr(h²)/Fisher–Bures
              −  c · ⟨h⟩_ρ                                      ←  nonlocal rank-1 global-mean
              +  0 · Δ_FS h(x)                                  ←  LOCAL base-derivative, coeff ≡ 0
```

**The three readings of `⟨·⟩` (RESEARCH §2 structural fork) — all give coefficient 0:**

1. **POINTWISE** (`⟨·⟩` at x's own state ⟹ `φ[M](x)=φ(M(x))`): the genuine `O(ε)`
   deviation field is `(algebraic Fisher core)(x)·Y(x)`, the core **identical** on the `λ₂=32` and
   `λ₁=12` modes (λ-INDEPENDENT) — the eigenvalue does not enter; discriminant `L_F[h] ≠
   (core)·Δ_FS Y` on both modes ⟹ **no `Δ_FS` term**. Coefficient `= 0`.
2. **GLOBAL mean-field** (`⟨·⟩ = ∫_base`): `⟨Y_λ⟩_FS = 0` (the ensemble mean annihilates every
   nonconstant harmonic — couples to the constant mode ONLY); the nonlocal piece is a constant in x
   with `Δ_FS(⟨h⟩) = 0` ⟹ a **rank-1 projector**, NOT a local differential operator. Coefficient `= 0`.
3. **LOCAL / geometry-respecting** (FS-kernel neighborhood average): the native kernel is the FLAT
   global average `K = 1/Vol` (localized second moment 0); a local `Δ_FS` term appears only with an
   **imported** kernel of second moment `σ²`, coefficient `½σ²`, which `→ 0` as `σ² → 0`
   (Bug-guard 2 / IMPORTED-KERNEL) — and even then it is the **scalar** harmonic-map `□φ_M`
   (`□φ_M = −12 φ_M`, Bug-guard 1 / DIRICHLET-TRAP), the WRONG TYPE vs `δΓ`'s `ε=20` Lichnerowicz
   TENSOR operator. Coefficient `= 0` (forced).

**Obstruction operator (exact):** `L_F = −Tr(h²)-Hessian (pointwise, the v35 Fisher/Bures corpse)
− c·⟨h⟩ (nonlocal rank-1 global-mean)`, local-`Δ_FS` coefficient `≡ 0`. Structurally a **different
TYPE** from `δΓ` (a local 2nd-order Lichnerowicz operator, the `ε=20` tensor mode) ⟹ the clamp is
FALSE.

---

## §3 — Symbolic identities reproduced (exact over ℚ, the sanity floor)

| Identity | Value | Role |
|----------|-------|------|
| `ε = λ_L − 2Λ` | `32 − 12 = 20` | the Lichnerowicz mode; the TYPE `δΓ` lives in (the object `L_F` must match) |
| scalar `λ₁` (rough Laplacian on `φ_M`, physical metric Ric=6g) | `+12` | a degree-1 FS harmonic; `□φ_M = −12 φ_M` (the Dirichlet-trap scalar type) |
| scalar `λ₂` (rough Laplacian on `z₁²z̄₂²/ρ²`) | `+32 = λ_L` | a degree-2 harmonic; the Lichnerowicz eigenvalue level |
| v35 `A_ii ≡ Var` @ d1@P0 | `1/2` | the canonical FS area IS the quantum Fisher (the v35 DEAD-FISHER object) |
| v35 `G_M = Var + ¾⟨M⟩² − ½Tr M²` | holds @ all 4 s9 points | the relative-entropy / Bures structure; G_M genuinely varies (Bug-guard 3 non-vacuous) |
| s9 ground points | `d1@P0: Var=1/2, G_M=−5/16`; `d1@P2: Var=2/15, G_M=−13/15`; `s01@P0: Var=11/16, G_M=−17/64`; `gen@P0: Var=27/16, G_M=−81/64` | the off-faithful de-risk table (Var, G_M vary ⟹ probe is non-vacuous) |
| `⟨Y_λ⟩_FS` for any nonconstant harmonic | `0` | the global ensemble mean couples to the constant mode ONLY (the collapse mechanism) |

---

## §4 — Conventions

| Convention | Value (this phase) |
|------------|--------------------|
| Variety / arena | CP² = h₃(ℂ_u) (the C_u cut of OP²; octonion engine NOT on the decisive path) |
| Chart | Wirtinger affine `v=(1,z₁,z₂)`, `ρ=1+|z₁|²+|z₂|²`; `z`, `z̄` INDEPENDENT symbols; conjugation = z↔z̄ swap + `i→−i` (NEVER sympy `conjugate()`) |
| FS metric (eigenvalue/Lichnerowicz anchors) | PHYSICAL `g_phys = g_pot/2`: Ric=6g, R=24, Λ=6, `λ_k = 4k(k+2)` ⟹ `λ₁=12`, `λ₂=32=λ_L`, `ε=20` |
| FS metric (v35 `A_ii≡Var` identity) | POTENTIAL/Fisher `g_pot = ∂∂̄ log ρ` (= Re QGT) |
| Inner product / moment | `⟨X,p⟩ = Tr(XP)`, `φ_M = ⟨M,p⟩` (linear in M); `Var = ⟨M²,p⟩−⟨M,p⟩²`; `G_M = ⟨M#,p⟩−¼⟨M,p⟩²` |
| Matter | traceless Hermitian (`Tr M = 0`); directions s01, a01, d1, gen; structured off-faithful `M̄ = s01` |
| Laplacian sign | analyst `Δ = +2 g^{ab̄}∂_a∂_b̄` (negative-semidef, `λ`-harmonic ⟹ `Δ = −λ`); rough `∇*∇ = −Δ = +λ` |
| Arithmetic | exact over ℚ / ℚ(i) on every decisive line; NO float in any verdict |

The overall metric scale (`g_pot` vs `g_phys = g_pot/2`) is the single overall scale that does NOT
decide the verdict (it rescales `λ` and `A` uniformly).

---

## §5 — Deviations

- **[Rule 4 — completeness] Two FS-metric normalizations carried.** The certified `ε=20` uses the
  PHYSICAL metric (`g_phys = g_pot/2`, Ric=6g, `λ₁=12`); the v35 `A_ii ≡ Var` identity is canonical
  in the POTENTIAL/Fisher metric (`g_pot`, Re QGT). Both are reported; the eigenvalue/Lichnerowicz
  anchors are routed through `g_phys` so they match the certified `ε=20`. (Initial run used `g_pot`
  for the anchors, giving `λ₁=6, λ₂=16` — half the certified values; corrected to `g_phys`.) This is
  a normalization completeness fix, not a physics change — the overall scale does not decide the
  verdict.
- **No physics redirections (Rule 5) or scope changes (Rule 6).** The skeptical prior (DEAD-POINTWISE)
  was confirmed; the result matches the de-risked expectation (RESEARCH §9).
- **HARD PROCESS RULES honored:** no brute symbolic cancel/simplify/solve over a generic
  multi-parameter profile; the decisive object is a structural/at-points determination (mode-carrier
  λ-independence + the exact `⟨Y_λ⟩_FS = 0` integral); every invocation completed in <1 s; no orphaned
  python jobs; committed after each gate.

---

## §6 — Confidence

**[CONFIDENCE: HIGH]** for the primary verdict `DEAD-POINTWISE`. Independent checks (>3, genuinely
distinct principles):

1. **Mode-carrier λ-independence** — `L_F` on `h = h_dir·Y` is identical for `Y` a `λ₂=32` and a
   `λ₁=12` harmonic (the eigenvalue is absent); discriminant `L_F[h] ≠ (core)·Δ_FS Y` on both modes.
2. **Exact `⟨Y_λ⟩_FS = 0`** — the global ensemble mean (Dirichlet integral over CP²) annihilates
   every nonconstant harmonic, so the only non-locality is a rank-1 constant-mode projector with
   `Δ_FS(·) = 0`.
3. **Structural single-channel** — AST-parsing the φ-iteration confirms F2/F3's sole `ρ`-dependence
   is `⟨l_i⟩_ρ`; no independent base-derivative channel exists in the φ-fixed-point.
4. **AST guards** — NO-CIRCULARITY (no `R`/`Ric`/`G`/`Δ_L` in `L_F`) and WOO (no thermo) both pass
   and FIRE on injection (the result is not contaminated by the metric action and not woo).
5. **Anchors + dimension/type** — `ε=20`, `λ₁=12`, `λ₂=32`, v35 `A_ii≡Var`, `G_M` decomposition all
   reproduced exact over ℚ; the WRONG-TYPE alternative (scalar `□φ_M = −12 φ_M`) is the only thing an
   imported kernel could produce, never the `ε=20` tensor.

**Residual uncertainty (why not stated more strongly):** the result is a determination about the
specific φ-iteration F2/F3 maps and the geometry-respecting field extension via the FS/Lichnerowicz
structure; a *different* self-modeling map with a genuinely localized intrinsic kernel could in
principle carry a derivative — but no such map is in the corpus, and inserting one is fp-imported
(Bug-guard 2). The verdict is robust against the inherited-derivative / circularity worry
(structurally closed). The verdict ladder is non-hardwired (5 distinct synthetic verdicts).

---

## §7 — Fences (binding, verbatim)

NO Einstein / `G=κT` / gravity / Newton / dark-matter / geodesic language as a DERIVED result; the
bits↔area / induced-`G` rate is a framework ratio, NOT Newton's G; FS is USED, not derived;
signature Riemannian (Wall 2 unpaid). DEAD-\* and ALIVE-\* are NOT derivations of gravity. ALIVE is
necessary-not-sufficient for gravity (Jaksland). Does NOT retract v33 (extremize), v34 (induce),
v17–v21 (fiber kills), v23 (I/3 death), v35 (DEAD-FISHER). Paper 5 remains the only result in the
more-than-nothing column. `DEAD-POINTWISE` is the expected, honest outcome and the green light for
fork A.
