# 86 — GATE 3 SUMMARY: B3 — the level split + the sourced field equation

**v26.0 Phase 86. Exact over Q. VERDICT = B3 PASS (λ₂ = 104 OP² / 32 cut).**
Independently confirmed (`..._verify.py`, 10/10; λ₂ four ways) and the gpd-verifier
(`86-GATE-3-VERIFICATION.md`).

## The level split

`Sym²(26) = 1 ⊕ 26 ⊕ 324` under F₄; the only quadratic covariants of traceless `M` are
`M#` and `TrM²·1` (`M² = M# + ½TrM²·1`, dependent). So
> **⟨M,p⟩² = α⟨M#,p⟩ + β·TrM² + R_M(p)**, `R_M` a mean-zero level-2 (`λ₂`) eigenfunction,

with `(α, β, λ₂)` fixed by the OVERDETERMINED symbolic solve at `E_11` (consistency IS
the claim — not a fit). Unique solutions:

| space | `λ₁` | `λ₂` | `λ₂−λ₁` | `λ₂/λ₁` | `(α, β)` | `κ₀` |
|---|---|---|---|---|---|---|
| CP² cut | 12 | **32** | 20 | 8/3 | (2/5, 3/20) | 9/4 |
| OP² | 48 | **104** | 56 | 13/6 | (1/7, 9/182) | 108/13 |

(Cut uses u-aligned `M`; off-u `M` is invisible there — B4.) **λ₂(cut) = 32** confirms
Fubini–Study `4·2·(2+2)`; **λ₂(OP²) = 104** is the genuinely underived number, **derived**
and cross-checked against the closed-form spectra `λ_k(CP²) = 4k(k+2)` (12, 32) and
`λ_k(OP²) = 4k(k+11)` (48, 104) (Cahn–Wolf/Besse) — confirmed **four independent ways**
(26-param symbolic solve, `c11²` control, grad-of-N-sharp solve, closed forms).

## The sourced field equation

`κ₀ = λ₁(1/6 − α/24 + β/4)` derived symbolically; the identity verified at `E_11` for
symbolic `M`, `R_M` confirmed a genuine `λ₂`-eigenfunction (`ΔR_M = −λ₂R_M`), covariance
closing it to all `p`:
> **(Δ + λ₁) G_M = −κ₀·TrM² + ((λ₂−λ₁)/4)·R_M(p)**
> OP²: `(Δ+48)G_M = −(108/13)TrM² + 14·R_M` ; cut: `(Δ+12)G_M = −(9/4)TrM² + 5·R_M`.

The entropy-response field fails its free Helmholtz equation by an EXPLICIT source —
homogeneous `∝ TrM²` plus anisotropic `∝ R_M` — with both couplings fixed by canonical
spectral data. The route's first SOURCED (Poisson-type) equation: free propagation (v25)
+ matter source (this run). **Kernel honesty:** `(Δ+λ₁)` annihilates level-1, so this is
an exact identity, not a boundary-value problem (and exempt from trap #6 — the source is
explicit, not an annihilator existence claim).

**Gate 3: B3 PASS.** `λ₁, λ₂, α, β, κ₀` are spectral/structural data of the FROZEN
geometry — not couplings; no Newton constant.
