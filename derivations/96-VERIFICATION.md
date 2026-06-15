# Phase 96 / v36.0-candidate — INDEPENDENT VERIFICATION: the FIELD-FAITHFULNESS CLAMP gate

**Verdict under test:** `DEAD-POINTWISE` at Gate 0 — field faithfulness `M(x) = φ[M](x)` on
CP² = h₃(ℂ_u) carries **NO local base-derivative term** (the clamp `δF=0 ⟺ δΓ=0` is FALSE,
fork A is PROVEN).

**Independent-verification result: ALL 6 CHARGES PASS. The `DEAD-POINTWISE` verdict is
CONFIRMED. [CONFIDENCE: HIGH].**

Verified via **separate code paths** built from scratch in `/tmp/v96_*.py` (a fresh CP² Wirtinger
engine, FS metric, Laplacian, and FS-integral master formula — NOT importing
`code/faithfulness_clamp.py` and NOT re-running it). The certified v35 engine
`code/area_per_bit.py` and the φ-iteration reference `nonlinear_iteration.py` were READ for
discipline/grounding only. Exact over ℚ / ℚ(i) on every decisive line; sympy 1.14.0; no float in
any verdict; no orphaned python jobs; no brute symbolic cancel over generic multi-parameter
profiles (the symbolic identities use the polynomial-numerator method over ρ-powers; all runs
< a few seconds).

---

## Per-charge dispositions

| # | Charge | Disposition | Decisive evidence (exact over ℚ) |
|---|--------|-------------|----------------------------------|
| 1 | `⟨Y_λ⟩_FS = 0` for nonconstant FS-harmonics (the collapse fact) | **PASS** | Independently re-derived the FS master integral (Dirichlet/Γ form), reconciled with the engine. `⟨φ_d1⟩=⟨φ_gen⟩=⟨φ_s01⟩=0` (λ₁=12 harmonics, eigenvalue −12 verified); `⟨z₁²z̄₂²/ρ²⟩=0` (λ₂=32 harmonic, eigenvalue −32 verified). Constant-mode norm `Vol=1/2 ≠ 0`. NO nonconstant mode has nonzero FS-average. |
| 2 | λ-independence (the decisive discriminant) | **PASS** | `L_F` built from the F2/F3 covariance core `⟨{M̄,h},p⟩ − 2⟨M̄,p⟩⟨h,p⟩`. On `h=h_dir·Y`, `L_F = L0·Y` with `L0` **identical** on the λ=12 and λ=32 carriers. Solving `α − λβ = 1` on both carriers ⟹ **β = 0, α = 1** exact. The local-Δ_FS coefficient is identically 0; the eigenvalue (−12/−32) a local Laplacian injects is ABSENT. |
| 3 | pointwise core IS the −Tr(h²)/Fisher–Bures Hessian | **PASS** | Independently re-derived `A_ii ≡ Var` symbolically over a generic 8-param traceless M and ALL chart points (polynomial-numerator method, exact over ℚ); numeric anchor `A_ii = Var = 1/2 @ d1@P0`; `G_M = Var + ¾⟨M⟩² − ½Tr M²` decomposition holds symbolically. The core IS the quantum Fisher / QGT-real object (Provost–Vallée FS = Re QGT). |
| 4 | Dirichlet-trap `□φ_M = −12 φ_M` (Bug-guard 1) | **PASS** | Independently confirmed `Δ_phys φ_M / φ_M = −12` for all four matter directions (s01, a01, d1, gen). A SCALAR eigenvalue equation (degree-1 harmonic), NOT the ε=20 Lichnerowicz TENSOR. An imported kernel routes to the WRONG TYPE. |
| 5 | NO-CIRCULARITY + WOO fence (by my own reading) | **PASS** | Code-only AST scan (docstrings/comments stripped) of the φ-iteration: F2 and F3 each reference `rho` in **exactly one** place — `expectations(points, rho) = ⟨l_i⟩_ρ`, a GLOBAL mean (sum over all grid points). NO geometric token (Riemann/Ricci/Einstein/Lichnerowicz/curvature/metric) and NO thermo token in the code. Single non-local channel; no independent base-derivative channel; no thermal/coarse-graining ensemble. |
| 6 | off-faithfulness non-vacuity (Bug-guard 3) | **PASS** | The core `L0` at structured off-faithful `M̄ = s01 ≠ I/3` is a genuinely NONZERO rational field (and nonzero for several (M̄,h) pairs). The s9 ground table reproduced exactly: `Var ∈ {1/2, 2/15, 11/16, 27/16}`, `G_M ∈ {−5/16, −13/15, −17/64, −81/64}` (4 distinct values each). At `M̄=0` the core is 0 — the v23 0=0 degeneracy, which `M̄=s01` correctly avoids. |

---

## §1 — The load-bearing collapse fact (Charge 1)

The φ-iteration's only non-locality is the ensemble mean `⟨l_i⟩_ρ`. On a field this is the
global base integral, and its action on harmonics is a rank-1 constant-mode projector. I
independently re-derived the FS master integral on CP² (potential metric `dV_FS ∝ d⁴z/ρ³`):

```
∫_{CP²} s₁^a s₂^b / ρ^K dV_FS  =  a! b! (K−a−b−3)! / (K−1)!   (matched monomials, K = k+3)
```

verified two ways: (a) directly via the U(2)-phase-average + Dirichlet radial integral, and
(b) via the closed-form Γ-function `Γ(a+1)Γ(b+1)Γ(K−a−b−2)/Γ(K)`. The two forms agree on all
test points and match the engine's `_mono_integral`. Then:

- Constant-mode norm: `⟨1⟩ = Vol = 1/2 ≠ 0`.
- λ₁=12 harmonics `φ_M = ⟨M,p⟩`: `⟨φ_d1⟩ = ⟨φ_gen⟩ = ⟨φ_s01⟩ = 0` (eigenvalue independently
  verified `Δ_phys φ_M = −12 φ_M`).
- λ₂=32 harmonic `z₁²z̄₂²/ρ²`: `⟨z₁²z̄₂²/ρ²⟩ = 0` (eigenvalue independently verified
  `Δ_phys Y₃₂ = −32 Y₃₂`).
- Robustness: a mixed field `h = 7 + 3φ_d1 + 5·Y₃₂` gives `⟨h⟩_FS = 7` — only the constant mode
  survives. **`⟨·⟩_FS = Vol·P₀` is exactly a rank-1 constant-mode projector.**

No nonconstant mode has a nonzero FS-average ⟹ the verdict is **not** in danger; the global mean
is a constant in x with `Δ_FS(⟨h⟩) = 0`.

## §2 — The decisive discriminant (Charge 2): the local base-derivative coefficient is 0

Building `L_F` from the F2/F3 covariance functional `δ(⟨M²,p⟩ − ⟨M,p⟩²)` and linearizing at
`M̄ = s01` with the field perturbation `h(x) = h_dir·Y(x)`:

```
L_F[h](x) = ( ⟨{M̄,h_dir},p⟩ − 2⟨M̄,p⟩⟨h_dir,p⟩ ) · Y(x)  =  L0(x) · Y(x)
```

The carrier `Y(x)` enters as a pointwise scalar multiplier **inside** the algebraic variance
functional — it is **not** differentiated. The core `L0` is **identical** on the λ=12 and λ=32
carriers (λ-independent). Writing `L_F = α·L0·Y + β·L0·(Δ_FS Y)` and using `Δ_FS Y = −λ Y` on the
two carriers (λ ∈ {12, 32}) gives the linear system `α − 12β = 1`, `α − 32β = 1`, whose unique
solution is **`β = 0`, `α = 1`** (exact over ℚ). The local base-derivative coefficient is
identically 0. The contrast (the local-Laplacian foil) WOULD inject the eigenvalue (cores −12 vs
−32, differing by exactly `ε = 20`); `L_F` does not.

## §3 — Type and channel (Charges 3, 4, 5)

- **Type of the pointwise core (Charge 3):** `A_ii ≡ Var` (symbolic, all p, all M) ⟹ the core is
  the quantum Fisher / QGT-real `−Tr(h²)`/Fisher–Bures Hessian (the v35 DEAD-FISHER object). The
  `G_M` decomposition holds.
- **Type of any imported derivative (Charge 4):** `□φ_M = −12 φ_M` — a SCALAR (degree-1 harmonic)
  eigenvalue equation, NOT the ε=20 Lichnerowicz TENSOR operator. An imported kernel routes to
  DEAD-WRONG-DERIVATIVE, never ALIVE.
- **No independent channel (Charge 5):** code-only AST scan confirms F2/F3 reference `ρ` solely
  through the GLOBAL mean `⟨l_i⟩_ρ`; no geometric/thermo import. The inherited-derivative /
  circularity worry is structurally refuted; demon-test 2.0 passes.

## §4 — Non-vacuity (Charge 6)

Linearizing at the structured off-faithful `M̄ = s01 ≠ I/3` gives a genuinely nonzero operator
(`L0` a nonzero rational field; `Var`, `G_M` vary over 4 distinct values on the s9 ground points).
The faithful matter-free point `M̄ = 0` gives the v23 0=0 degeneracy, correctly avoided.

---

## Anchors reproduced (exact over ℚ)

| Anchor | Value | Status |
|--------|-------|--------|
| `λ_k = 4k(k+2)` (physical FS metric, Ric = 6g, Λ = 6) | `λ₁ = 12`, `λ₂ = 32` | reproduced (eigenvalues of genuine harmonics) |
| Lichnerowicz `λ_L = λ₂` | `32` | reproduced (Δ_phys eigenvalue of `z₁²z̄₂²/ρ²` = −32) |
| `ε = λ_L − 2Λ` | `32 − 12 = 20` | reproduced |
| v35 `A_ii ≡ Var` (Provost–Vallée FS = Re QGT) | `1/2 @ d1@P0`; symbolic ∀p,∀M | reproduced |
| `G_M = Var + ¾⟨M⟩² − ½Tr M²` | symbolic ∀p,∀M | reproduced |
| s9 ground points `Var`, `G_M` | `(1/2,−5/16),(2/15,−13/15),(11/16,−17/64),(27/16,−81/64)` | reproduced |
| `□φ_M` scalar eigenvalue (Dirichlet trap) | `−12` | reproduced |
| `⟨Y_λ⟩_FS` (nonconstant harmonics) | `0` | reproduced (λ₁ and λ₂) |
| `Vol(CP²)` (constant-mode norm) | `1/2` | reproduced (= the engine value) |

---

## Confidence assessment: HIGH

**[CONFIDENCE: HIGH]** for the primary verdict `DEAD-POINTWISE`. Justification:

1. **Independent re-derivation, not re-run.** A fresh CP² engine (own Wirtinger chart, FS metric,
   inverse, Laplacian, FS-integral master formula) reproduced every decisive object. The FS master
   integral was derived two independent ways (phase-average+Dirichlet, and the Γ-function form) and
   independently reconciled with the engine.
2. **The decisive coefficient β = 0 is over-determined.** Two genuine harmonic carriers with
   distinct eigenvalues (12, 32) force `β = 0` uniquely (the local-Laplacian foil is explicitly
   shown to differ). This is the load-bearing step and it is exact.
3. **The collapse mechanism is exact and robust.** `⟨Y_λ⟩_FS = 0` holds for both a λ₁ and a λ₂
   harmonic; a mixed-field check shows `⟨·⟩_FS` is precisely the rank-1 constant-mode projector.
4. **No-circularity by my own code-only reading** (docstrings stripped): the single ρ-channel and
   the absence of geometric/thermo tokens are confirmed at the AST level, not by trusting the
   executor's guard.
5. **Anchors and type all match** (ε = 20, λ₁ = 12, λ₂ = 32, `A_ii ≡ Var`, `G_M` decomposition,
   `□φ_M = −12 φ_M`).

**Residual uncertainty (the one honest caveat, matching the executor's own §6):** the result is a
determination about the specific φ-iteration F2/F3 maps and the geometry-respecting field extension
via the FS/Lichnerowicz structure. A *different* self-modeling map with a genuinely localized
intrinsic kernel could in principle carry a derivative — but no such map is in the corpus, and
inserting one is fp-imported (Bug-guard 2), and even then it gives the SCALAR `□φ_M` type, not the
ε=20 tensor. This is a no-go on the CLAMP, not a claim about gravity (FENCES below). The verdict is
robust against the inherited-derivative / circularity worry.

---

## FENCES (binding, carried verbatim from the verdict)

NO Einstein / `G=κT` / gravity / Newton / dark-matter / geodesic language as a DERIVED result; the
bits↔area / induced-`G` rate is a framework ratio, NOT Newton's G; FS is USED, not derived;
signature Riemannian (Wall 2 unpaid). `DEAD-POINTWISE` is the expected, honest outcome and the
green light for fork A. Does NOT retract v33 (extremize), v34 (induce), v17–v21 (fiber kills), v23
(I/3 death), v35 (DEAD-FISHER). Paper 5 remains the only result in the more-than-nothing column.
ALIVE is necessary-not-sufficient for gravity (Jaksland arXiv:2005.05055).

---

## Reproduce (independent driver set)

```
/tmp/v96_engine.py        # fresh CP^2 FS engine (metric, inverse, det gN = rho)
/tmp/v96_charge4.py       # Charge 4: box phi_M = -12 phi_M
/tmp/v96_charge1.py       # Charge 1: <Y_lambda>_FS = 0 (lambda_1 and lambda_2)
/tmp/v96_reconcile.py     # FS master integral reconciled vs engine + Dirichlet derivation
/tmp/v96_charge3.py       # Charge 3: A_ii == Var (symbolic), G_M decomposition
/tmp/v96_charge2.py       # Charge 2: lambda-independence, decisive coeff beta = 0
/tmp/v96_charge5.py + 5b + 5c  # Charge 5: code-only AST reading of phi-iteration
/tmp/v96_charge6.py       # Charge 6: off-faithfulness non-vacuity, s9 ground table
/tmp/v96_consolidate.py   # three readings of <.>_rho + anchor ledger eps=20
/tmp/v96_robust.py        # rank-1 constant-mode projector on a mixed field
```

sympy 1.14.0, Python 3.x, exact rational arithmetic over ℚ / ℚ(i); Darwin arm64; no float in any
verdict; no orphaned python jobs.
