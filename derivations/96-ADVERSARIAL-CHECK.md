# Phase 96 / v36.0-candidate — ADVERSARIAL CHECK: attacking DEAD-POINTWISE (the FIELD-FAITHFULNESS CLAMP)

**Bottom line: the verdict SURVIVES and is STRENGTHENED.** All four attacks COLLAPSE exact over ℚ.
No genuine FORCED local Lichnerowicz (`ε=20` tensor) base-derivative term can be driven into field
faithfulness from the variety's own structure. **`DEAD-POINTWISE` holds; fork A stays proven.**

This is the analog of the v35 AREA-RIG attack: I tried my hardest to FLIP the verdict toward
PROCEED/ALIVE by forcing a local `Δ_FS`-type tensor derivative into `L_F`, and every route failed
on a specific, exact-over-ℚ mechanism. No FLIP, no INCONCLUSIVE.

**Drivers (all fresh, exact over ℚ, sub-second, no orphaned jobs):**
- `code/adv_kernel_96.py` — Attack 1 (FS-geometric-kernel): **20/20 PASS**, exit 0.
- `code/adv_jet_96.py` — Attack 2 (jet / higher-order self-model): **9/9 PASS**, exit 0.
- `code/adv_connection_96.py` — Attack 3 (connection-channel / Berry): **15/15 PASS**, exit 0.
- `code/adv_circularity_96.py` — Attack 4 (metric-inheritance circularity): **12/12 PASS**, exit 0.
- Total **56/56 PASS**. Anchors reproduced (`ε=20`, `λ₁=12`, `λ₂=32`, v35 `A_ii≡Var=1/2`).

---

## The single decisive theorem (what every attack reduces to)

**Spectral-multiplier obstruction (exact over ℚ).** Any kernel intrinsic to `(CP², g_FS)` and
`U(3)`-invariant is a **Fourier multiplier** `m(Δ_FS)` — diagonal on the harmonic decomposition.
The φ-iteration's only non-locality, the ensemble mean `⟨·⟩_ρ`, is the multiplier `m = 𝟙_{ker Δ}`
(value 1 on the constant mode, **0 on every nonconstant harmonic**): the **rank-1 projector onto the
constant mode**, NOT a Laplacian. Two absolute consequences:

1. **No scale-free route to `+Δ`.** A scale-free (homogeneous) multiplier is a power `Δ^s`. The
   native `⟨·⟩` is the `s → −∞` / projector limit; the local Laplacian is `s = +1`. No scale-free
   deformation connects them (different homogeneity degree). The only *intrinsic, scale-free*
   non-projector multiplier on CP² is the **Green's function** `G = Δ^{-1}` (`s = −1`) — an
   order **−2 smoothing** operator (eigenvalues `1/λ` DECAY), the **opposite** of a local derivative.
2. **Scalar, never the `ε=20` tensor.** Every `m(Δ)` acts on the **scalar** moment field
   `φ_M = ⟨M,p⟩`; at most it produces the scalar box `Δφ_M = −12 φ_M` (Bug-guard 1, the wrong
   TYPE). The `ε=20` Lichnerowicz operator acts on **symmetric 2-tensors** `h_{(ab)}` — a different
   bundle. The moment map contracts the matrix index to a scalar *before* any base derivative.

Both obstructions are structural and exact. Every attack below is a specific failed attempt to
evade one or both.

---

## Attack 1 — FS-geometric-kernel  (`code/adv_kernel_96.py`, 20/20 PASS) — **COLLAPSES**

> Is there a kernel the variety's OWN structure FORCES (FS heat kernel, FS Green's function,
> covariant FS-neighbor comparison) that is NOT an inserted-scale regulator and DOES carry a
> localized second moment → a real `Δ_FS` term?

| Candidate | Exact-over-ℚ outcome | Verdict |
|---|---|---|
| **K1** flat global average (the φ-map's NATIVE `⟨·⟩`) | `⟨Y_λ⟩_FS = 0` for both the `λ₁=12` and `λ₂=32` harmonics (Dirichlet/U(2) integral); `Δ_FS(⟨h⟩)=Δ_FS(const)=0` | rank-1 constant-mode projector, **NO derivative** |
| **K2** FS heat kernel `e^{-tΔ}` | small-`t`: `e^{-tλ}=1−tλ+…`, the `+Δ` coefficient **is** the inserted scale `t`; `lim_{t→0}=1` (identity); fixed `t>0` is a bounded smoothing | **IMPORTED scale** (Bug-guard 2) |
| **K3** FS Green's function `G=Δ^{-1}` (intrinsic + **scale-free**, the strongest) | `G=cΔ` forces `c=1/λ²` → `1/144` (λ=12) vs `1/1024` (λ=32), **incompatible**; `G` eigenvalues `1/λ` DECAY while `Δ` eigenvalues GROW; full-support kernel (nonlocal) | order **−2 smoothing**, the OPPOSITE of a local Laplacian; scale-free but wrong operator |
| **K4** geodesic-sphere / parallel-transport comparison | `⟨h⟩_{S(x,r)} = h + (r²/2n)Δh+…`, coefficient `= r²/2n` = the kernel second moment; `lim_{r→0}=0`; `r` not forced (CP² homogeneous) | **INSERTED radius** (Bug-guard 2), scalar |

**Mechanism that kills it:** the spectral-multiplier theorem. The strongest candidate (the
scale-free Green's function) is an *inverse* of the Laplacian — it gains derivatives, it does not
lose them, and its kernel is delocalized (full support). There is no scale-free intrinsic kernel
strictly between the projector (`s=−∞`) and `+Δ` (`s=+1`); the variety supplies the projector and
the smoothing `G`, never the derivative. And all are scalar multipliers on `φ_M`.

---

## Attack 2 — jet / higher-order self-model  (`code/adv_jet_96.py`, 9/9 PASS) — **COLLAPSES**

> Does the φ-iteration at SECOND order (the self-model modeling M's local VARIATION `∂M`, not just
> `M(x)`) force a `∂M / Δ_FS` coupling the first-order linearization missed?

- **J1 — the corpus map is value-only (0-jet).** AST/symbolic: `F2 = det·Σ(l_i−⟨l_i⟩)²` and
  `F3 = det·Σ l_i(l_i−⟨l_i⟩)` are POLYNOMIAL in the eigenvalue VALUES `l_i`; **no derivative of M
  appears**. Both reproduce `ρ_J = det(σ₂−1/3)` on the trace slice. A jet prolongation `(∂M,∂∂M)`
  is NOT in the corpus map — inserting it is a *different map* (fp-imported).
- **J2 — the second variation of the moment map VANISHES.** `φ_M = ⟨M,p⟩` is **linear in M**, so
  `d²φ/dε²|₀ = ⟨h₂,p⟩` exactly (no `h`-quadratic self-coupling). The only `h`-quadratic structure
  is `Var(h), G_M(h)` — **pointwise algebraic** (the v35 Fisher/Bures corpse), never a `Δ_FS`
  coupling. Second order adds Fisher terms, not a base derivative.
- **J3 — a jet-Dirichlet term is scalar AND inserted.** The Dirichlet EL of a moment field returns
  `+12·φ` (= `λ₁`, the SCALAR box, Bug-guard 1), NOT the `ε=20` tensor; and `∫|∇φ|²` is INSERTED
  (the corpus map is value-only) — dead handle-1 (entropy/MaxEnt) in disguise.
- **J4 — the moment map contracts the matrix index to a scalar** before any base derivative; no jet
  of the scalar `φ_M` is the `ε=20` symmetric-2-tensor (v35 already showed the metric trace of
  `dφ⊗dφ` IS `Var`, the scalar/Fisher part).

**Mechanism that kills it:** linearity of the moment map (`d²φ/dM²=0`) + the value-only corpus map.
The "second-order self-model" cannot manufacture a derivative the linear map structurally lacks.

---

## Attack 3 — connection-channel / Berry  (`code/adv_connection_96.py`, 15/15 PASS) — **COLLAPSES**

> Does `L_F` have an antisymmetric / Berry / imaginary-QGT part (the v18 Lie sector) that is a
> covariant derivative the real-part Fisher Hessian misses? (v35 found the symplectic candidate =
> Var via the Kähler tie — does faithfulness escape that?)

- **C1 — the Berry curvature is genuinely present and = the Kähler form.** Using the **gauge-
  invariant** QGT `Q_{ab̄}=Tr((1−P)∂_aP ∂_b̄P)` (the naive `Tr(P∂P∂P)` is identically 0 for a
  rank-1 projector — **a vacuous Q=0 that would FAKE a kill; I caught and rejected it**), `Q` is
  NONZERO, Hermitian, with `Re Q = g_pot` exactly (ratio = 1 on every component) and a NONZERO
  imaginary/antisymmetric part = the Berry curvature = `g(J·,·)` (the metric recast
  antisymmetrically, no new info).
- **C2 — trivial on the real `φ_M`.** `φ_M=⟨M,p⟩` is REAL (`conj φ_M − φ_M = 0`) and gauge-invariant
  (`P` is invariant under `v→e^{iθ}v`); the Berry phase DROPS OUT. The faithfulness condition has
  **no antisymmetric channel** on the real moment field.
- **C3 — Kähler-tie collapse (the v35 corpse, sharpened).** The symplectic gradient-norm `A_iii`
  (`X=J∇φ`) `= Var` exactly at all four s9 points (`1/2, 11/16, 1/2, 27/16`): `J` a `g`-isometry, so
  every symplectic/connection contraction of `dφ_M` returns the **same Fisher scalar Var** — no
  escape to an independent object.
- **C4 — wrong symmetry type.** The Berry curvature is a 2-FORM (antisymmetric, `Λ²`); the `ε=20`
  mode is a SYMMETRIC 2-tensor (`Sym²`) — orthogonal bundles. And `ω = i g` carries no new info.
- **C5 — v18 cross-check.** The Berry/imaginary sector is a closed abelian gauge curvature (Chern
  class; v18's internal-SU(4) family), NOT the Riemann-built gravity Lichnerowicz tensor. v18
  already ruled this sector NOT-gravity.

**Mechanism that kills it:** the faithfulness condition lives on the **real, gauge-invariant**
moment `φ_M`, where the connection phase drops out; and the Kähler tie collapses the symplectic
channel to `Var` exactly as in v35. Even at full strength the Berry sector is antisymmetric (wrong
type) and gauge-natured (wrong sector).

---

## Attack 4 — metric-inheritance circularity probe  (`code/adv_circularity_96.py`, 12/12 PASS) — **COLLAPSES**

> Is there ANY route by which the STATE-side F independently inherits δΓ's derivative (the
> `dφ_M⊗dφ_M` context) WITHOUT importing the metric-side loop? (Find a second ρ-channel.)

- **D1 — exactly ONE ρ-channel (AST-confirmed).** Parsing the actual `nonlinear_iteration.py`:
  `iteration_F2` and `iteration_F3` reference `ρ` in exactly **one** expression each, and the ONLY
  ρ-consuming call is `expectations()` (the flat global mean `Σ points[:,i]·ρ_norm`); its source
  contains **no** metric/kernel/neighborhood/christoffel/laplacian token. No second ρ-channel exists.
- **D2 — the derivative `dφ_M` is METRIC-side.** It appears only in `grad_bilinear` = `dφ⊗dφ` (the
  v31 metric mode `B₃`, the SOURCE for δΓ), computed on the metric side — NOT in the state-side
  faithfulness condition (which is on the value `φ_M` / the eigenvalues `l_i`).
- **D3 — the state side is METRIC-FREE.** `F2/F3` are functions of the spectrum invariants
  `Tr M, Tr M², det M` (no `z,z̄`). Forming `g^{ab}∂_aφ ∂_b̄φ` REQUIRES the FS metric `g` (which is
  `z,z̄`-dependent); the state side supplies **no `g`**, so no `dφ` contraction can form natively.
- **D4 — no hidden volume-measure channel.** `dV_FS = dV/ρ³` has NO matter-M dependence
  (`δ(dV_FS)/δM = 0`); and the corpus `⟨·⟩` is a simplex average over the spectrum, with no `dV_FS`
  at all. Varying the matter state opens no second `g`-channel.
- **D5 — the only route is the circular metric loop.** A `dφ_M` term in `δF/δM` requires a `g` to
  contract (D3); the state side has none (D4); so `g` must be `g=g(M)` — the v34 **metric-side
  loop**, i.e. δΓ's derivative IMPORTED into F (circularity, Bug-guard 5), NOT an independent
  state-side channel. Concrete tie: the metric trace of `dφ⊗dφ` IS `A_ii = Var = 1/2` — even the
  borrowed object collapses to the pointwise Fisher Hessian.

**Mechanism that kills it:** the state-side condition carries no metric, so the only way to
introduce a base derivative is to borrow `g=g(M)` from the metric side — which is exactly the loop
the circularity guard forbids. The inherited-derivative worry from RESEARCH §9 is **structurally
closed**.

---

## Load-bearing discriminant (re-confirmed directly)

The verdict's mode-carrier **λ-independence** holds exact over ℚ: building the algebraic Fisher core
of `L_F` on `h = h_dir·Y(x)` gives a FIXED pointwise number (`1/4, 11/8, −1/4, 3/8` for
`h ∈ {d1,s01,a01,gen}` at P0, with `M̄ = s01`) that carries **no harmonic eigenvalue**. A local
`Δ_FS` term would inject `−λ` (= `−12` or `−32`); the core does not → the local `Δ_FS` coefficient
is **identically 0**. None of these numbers is the `ε=20` structure; the tensor mode is absent.

---

## Bug-guards I ran (and what fired)

- **VACUOUS-QGT (caught a real trap).** My first connection-attack used `Tr(P∂P∂P)`, which is
  identically 0 for a rank-1 projector — a vacuous `Q=0` that would have FAKED a clean kill. I
  detected it, switched to the gauge-invariant `Tr((1−P)∂P∂P)`, and added an explicit non-vacuity
  guard (`Q ≠ 0`, Hermitian, `Re Q = g`). The Berry curvature is genuinely present; the kill is real.
- **λ₂ anchor correction.** `z₁z̄₂/ρ` is the degree-1 moment (`λ=12`), NOT degree-2; the genuine
  `λ₂=32` carrier is `z₁²z̄₂²/ρ²` (verified eigenfunction at two points). Anchors then reproduce
  `ε=20`.
- **No brute symbolic cancel over generic multi-parameter profiles.** Every decisive line is
  exact-over-ℚ at rational points or a closed-form spectral fact; all four drivers run <1 s; no
  orphaned python jobs.

---

## Outcome (mirror v35 AREA-RIG rules)

> All attacks collapse / no FORCED local Lichnerowicz term (every derivative is imported-kernel,
> wrong-type scalar □, or circular) → **DEAD-POINTWISE robust / strengthened.**

This is the realized branch. Each attack dies on a *specific* mechanism, exact over ℚ:

| Attack | Killing mechanism |
|---|---|
| 1 (kernel) | spectral multiplier: scale-free ⇒ `Δ^s`; native `⟨·⟩` is the projector (`s=−∞`), `G` is smoothing (`s=−1`); never `+Δ`; and all SCALAR |
| 2 (jet) | `φ_M` linear in M ⇒ `d²φ/dM²=0`; the corpus map is value-only; any jet-Dirichlet is scalar + inserted |
| 3 (connection) | real gauge-invariant `φ_M` ⇒ Berry phase drops out; Kähler tie ⇒ symplectic channel = `Var`; 2-form (wrong type); gauge sector (v18) |
| 4 (circularity) | one ρ-channel (AST); state side metric-free; only route to `dφ` is the circular metric loop `g=g(M)` (Bug-guard 5) |

**No FLIP. No INCONCLUSIVE.** The `DEAD-POINTWISE` verdict is robust and strengthened: field
faithfulness `M(x)=φ[M](x)` on CP² carries **no genuine local base-derivative term** — `L_F` is the
pointwise Fisher/Bures Hessian plus a nonlocal rank-1 global-mean, the local Lichnerowicz (`Δ_FS`,
`ε=20` tensor) coefficient is **identically 0**, the clamp `δF=0 ⟺ δΓ=0` is **FALSE**, and **fork A
stays PROVEN**.

**Fences honored (verbatim):** NO Einstein / `G=κT` / gravity / Newton / dark-matter / geodesic as a
DERIVED result; the bits↔area / induced-`G` rate is a framework ratio; FS is USED, not derived;
signature Riemannian (Wall 2 unpaid). Does NOT retract v33/v34/v17–v21/v23/v35. Paper 5 remains the
only result in the more-than-nothing column. `DEAD-POINTWISE` is the expected, honest outcome and
the green light for fork A.

**[CONFIDENCE: HIGH]** — four independent attacks, each killed by a distinct exact-over-ℚ mechanism;
the load-bearing λ-independence discriminant and the spectral-multiplier theorem both re-confirmed;
the one genuine trap (vacuous QGT) caught and corrected; 56/56 checks PASS, all drivers exit 0.
