# 86 — RESEARCH: The Sourced Field Equation — MaxEnt Derived and the Second-Order Vacuum Structure

**v26.0 Phase 86 (J5-on-the-variety, step 2). Extraction milestone #2.
Drivers: `code/variety_sourced_field_equation.py` (executor, 19/19 PASS, 22.5 s),
`code/variety_sourced_field_equation_verify.py` (independent path, 10/10 PASS).
Exact over Q[ε]/(ε³), Q(t), polynomial-identity solves. VERDICT: B1 PASS, B2 PASS,
B3 PASS (λ₂ = 104 OP² / 32 cut), B4 PASS.**

This run expands the v24/v25 landscape around the vacuum `X = I/3 + εM` (traceless
matter `M`) and extracts the **sourced field equation** for the second-order
entropy-response field. The vacuum's MaxEnt property becomes a theorem of the doublet
(first order empty); the content lives at second order as an explicit relative-entropy
field obeying a Poisson-type equation whose source is quadratic in the matter. The
background canonical geometry is STILL FROZEN; `λ₁, λ₂, α, β, κ₀` are spectral/structural
data of that frozen geometry (imports-as-math), NOT derived couplings — no Newton
constant, no `G = κT`, no SUGRA, no dark-matter language.

---

## 0. Setup

`X = I/3 + εM`, `Tr M = 0`, `M` symbolic (26 params: diagonal `(a,b,−a−b)` + three
octonions). Consumed v25 assets (by reference): the moment doublet `m = Tr(C_pX) =
Tr X − ⟨X,p⟩`, `q = det₂(C_pX) = ⟨X#,p⟩`, `r = q/m²`; the canonical field equation
`Δφ_Y = −λ₁(φ_Y − ⟨Y,I/3⟩)`, `λ₁ = 48` (OP²) / `12` (CP² cut); the mean-curvature
machinery `ΔP = −λ₁(E_11 − I/3)`; the frequency-≤2 fingerprint. `⟨A,B⟩ = Tr(A∘B)`;
`X# = X×X` the Freudenthal adjoint; `σ₂(M) = ½(Tr M² − Tr(M²)) = −½TrM²` for traceless `M`.

---

## 1. B1 — first order: the doublet collapses, MaxEnt derives

Sharp identity (verified): `I × M = −M/2` for traceless `M` (from the cross-product
`I×M = I∘M − ½Tr(I)M + ½(Tr(I)·0 − Tr(M))I = M − (3/2)M`). Hence with `(I/3+εM)# =
(I/3)# + 2ε(I/3 × M) + ε²M# = I/9 − (ε/3)M + ε²M#`:
```
   m = 2/3 − ε⟨M,p⟩,        X# = I/9 − (ε/3)M + ε²M#,
   q = 1/9 − (ε/3)⟨M,p⟩ + ε²⟨M#,p⟩.
```
At first order **δq = δm/3**: there is ONE field, `⟨M,p⟩`, not two. Consequence
(exact, all 27 components):
> **δr = (9/4)δq − (3/4)δm = 0 identically — the purity/entropy landscape is flat at
> first order at EVERY event `p`** (verified at `E_11` symbolic `M` and along all 16
> families over `Q(t)`).

This is the vacuum **MaxEnt property, DERIVED on the variety**: the v24 flattening
result and the v23 zero-gradient fact, re-read. The first-order balance the fiber
(v23) failed to host is structurally empty; the content lives at second order. (B1 is
the honest restatement of v23's kill, now a theorem of the doublet.)

---

## 2. B2 — second order: the entropy-response field

Expanding `r = q/m²` exactly to `ε²` (`a := ⟨M,p⟩`, `c := ⟨M#,p⟩`):
> **δ²r = (9/4)·G_M(p)·ε²,   G_M(p) := ⟨M#,p⟩ − ¼⟨M,p⟩².**

**Entropy conversion.** On the 2-face, `S = f(r)` with `λ± = ½ ± ½√(1−4r)`. In
`u = 1−4r` the `±√u` branches cancel: `S(u) = log 2 − ½u + O(u²)` (analytic at the
degenerate point `r = 1/4`), so `f'(1/4) = −4·(dS/du)|₀ = 2`. Since `δr = 0`,
> **δ²S = f'(1/4)·δ²r = (9/2)·G_M·ε².**

**Relative entropy.** The vacuum face state is maximally mixed (`ρ_vac = I₂/2`), so
exactly `S(ρ_face ‖ ρ_vac) = log 2 − S(ρ_face)`; the response field IS minus the
second-order relative-entropy density.

**Positivity (must hold).** `G_M(p) ≤ 0` for all traceless `M` and all `p`. Structural
proof: `⟨M,p⟩ = Tr(C_pM)`, `⟨M#,p⟩ = det₂(C_pM)` (the v25 C1 with `Y=M`), so
> **`G_M = det₂(C_pM) − ¼(Tr C_pM)² = −¼·(λ₊(C_pM) − λ₋(C_pM))² ≤ 0`**
(the squared eigenvalue gap of the compressed matter on the face), with equality iff
`C_pM ∝ I₂`. Anchor: `M = diag(2,−1,−1)`, `p = E_11` ⇒ `C_{E_11}M = diag(−1,−1) = −I₂`
⇒ `G = 0` (the face sees only the `∝I₂` block); `p = E_22` ⇒ `G = −2 − ¼ = −9/4 < 0`.
Verified structurally + on an exact rational `(M,p)` battery.

---

## 3. B3 — the level split and the sourced field equation

`Sym²(26)` under F₄ `= 1 ⊕ 26 ⊕ 324` (multiplicity one). The only quadratic covariants
of traceless `M` are `M#` (in the 26) and `TrM²·1` (the 1); `M² = M# + ½TrM²·1` is
dependent, not a third covariant. Therefore
> **⟨M,p⟩² = α·⟨M#,p⟩ + β·TrM² + R_M(p)**, `R_M` exactly a `λ₂`-eigenfunction
> (mean-zero level-2 part).

**Operational determination (pointwise at `E_11`, symbolic `M`).** Using
`Δ⟨M,·⟩²(E_11)` (the v25 frame machinery applied to a product of rational `t`-functions),
`Δ⟨M#,·⟩(E_11) = −λ₁(⟨M#,E_11⟩ + TrM²/6)` (since `⟨M#,I/3⟩ = σ₂(M)/3 = −TrM²/6`), and
`ΔR_M(E_11) = −λ₂R_M(E_11)`:
```
   Δ⟨M,·⟩²(E_11) = −αλ₁(⟨M#,E_11⟩ + TrM²/6) − λ₂·R_M(E_11),
   R_M(E_11) = ⟨M,E_11⟩² − α⟨M#,E_11⟩ − β·TrM².
```
This is an OVERDETERMINED polynomial identity in the symbolic `M`-params; its
**consistency IS the level-split claim**. The unique solutions:

| space | `λ₁` | `λ₂` | `λ₂−λ₁` | `λ₂/λ₁` | `(α, β)` | `κ₀` |
|---|---|---|---|---|---|---|
| CP² cut | 12 | **32** | 20 | 8/3 | (2/5, 3/20) | 9/4 |
| OP² | 48 | **104** | 56 | 13/6 | (1/7, 9/182) | 108/13 |

(The cut split uses u-aligned `M` — off-u `M` is invisible there, B4.) **λ₂(cut) = 32**
confirms the Fubini–Study value `4j(j+n)|_{j=2,n=2} = 32`; **λ₂(OP²) = 104** is the
genuinely underived number, **derived here** and cross-checked against the closed-form
Cayley-plane spectrum `λ_k(OP²) = 4k(k+11)` (→ 48, 104; Cahn–Wolf 1976 / Besse), with
`λ_k(CP²) = 4k(k+2)` (→ 12, 32) — both verified four independent ways (the 26-param
symbolic solve, the `c11²` control, the independent grad-of-N-sharp solve, and the
closed forms).

**THE SOURCED FIELD EQUATION.** Combining §2, §3 with the v25 free equation
(`κ₀ = λ₁(1/6 − α/24 + β/4)`, derived symbolically):
> **(Δ + λ₁) G_M = −κ₀·TrM² + ((λ₂ − λ₁)/4)·R_M(p)**
> OP²: `(Δ+48)G_M = −(108/13)TrM² + 14·R_M` ; cut: `(Δ+12)G_M = −(9/4)TrM² + 5·R_M`.

The entropy-response field fails its free Helmholtz equation (v25) by an EXPLICIT
source — a homogeneous term `∝ TrM²` (the matter's total quadratic invariant) plus an
anisotropic term `∝ R_M` (the level-2 part of the squared matter moment) — with both
couplings fixed by canonical spectral data `(λ₁, λ₂−λ₁, α, β)`. This is the route's
first SOURCED (Poisson-type) equation: free propagation (v25) + matter source (this
run). **Kernel note (honest):** `(Δ+λ₁)` annihilates level-1, so the identity does not
*determine* `G_M` from the source — it is an exact identity, not a boundary-value problem.

---

## 4. B4 — the hidden sector (the 4-vs-16 gap materialized)

For `M` supported entirely off-u (octonion directions `e_1..e_6`):
- **(invisibility)** `⟨M,p⟩ ≡ 0` for ALL `p` in the CP² cut (trace-form orthogonality
  of off-u `M` to `h_3(C_u)` — verified symbolically): the cut has NO first-order moment
  and NO direction data for hidden `M`; yet
- **(it still sources)** `G_M|_cut = ⟨M#,p⟩|_cut ≠ 0` for `M ≠ 0` — the hidden squares
  land on the diagonal / in `C_u` (e.g. `⟨M#,E_11⟩ = −(|x1_offu|²)` for the `(2,3)`-block
  part); different cut points see different hidden blocks; and
- **(signature dichotomy)** the cut source is **square-free** (the `−¼⟨M,p⟩²` term
  vanishes identically on the cut ⇒ level ≤ 1, no anisotropic level-2 signature), while
  every u-aligned `M' ≠ 0` is first-order VISIBLE on the cut (cut-moment injectivity,
  from v25's `9 = 1⊕8`) and generically sources at level 2 as well. So on the cut:
  **first-order-invisible ⟺ off-u-supported ⟺ square-free source.**

NO dark-matter language: these are statements about THIS landscape's cut restriction,
nothing else.

---

## 5. Trap guards and anti-overclaim

- **Order-counting (#1):** `δr = 0` and all `ε²` claims are identities in `Q[ε]/(ε³)`,
  exhibited symbolically (not numeric). Held.
- **Branch smoothness (#2):** the `√(1−4r)` branches cancel to an analytic series at
  `r = 1/4`; `f'(1/4) = 2` verified exactly. Held.
- **Projector hygiene (#3):** the level split comes ONLY from the overdetermined symbolic
  solve + the eigenfunction property; no numerically diagonalized projectors; the
  system's consistency IS the claim. Held.
- **Hidden-M bookkeeping (#4):** off-u support by exact coordinate sets; cut-vanishing by
  trace-form block orthogonality (not sampling); octonion product order as v25
  (`conj(x3·x2)`). Held.
- **Trap #5/#6 (with exemption):** still no field equation for the rational `r` or `S`;
  the SOURCED equation for `G_M` is exempt from #6 because the source is EXPLICIT and the
  claim is a specific exact identity with derived constants — NOT an existence claim for
  an annihilator. Held.

**Anti-overclaim (binding).** PASS ≠ Einstein, ≠ J5 complete, ≠ a balance with an
independent geometric variation — the background canonical geometry is STILL FROZEN;
`λ₁, λ₂, α, β, κ₀` are spectral/structural data of that frozen geometry, NOT couplings;
no Newton constant. What this certifies: the vacuum's MaxEnt property is a THEOREM of the
doublet (first order empty — the honest restatement of v23's kill); the second-order
entropy response is an explicit relative-entropy field with a SOURCED Poisson-type
equation whose source is quadratic in matter; and first-order-invisible matter still
sources the cut's field (square-free signature). Signature stays OPEN. The genuine forks
(equation-of-state; connection coupling) are explicitly NOT tested — Gate 5 only prices
them for v27.

---

## 6. Citations

*Second-order entanglement-equilibrium placement.*
- T. Jacobson, "Entanglement Equilibrium and the Einstein Equation," Phys. Rev. Lett. **116** (2016) 201101.
- N. Lashkari & M. Van Raamsdonk, "Canonical Energy is Quantum Fisher Information," JHEP **04** (2016) 153.
- T. Faulkner, M. Guica, T. Hartman, R. C. Myers, M. Van Raamsdonk, "Gravitation from Entanglement in Holographic CFTs," JHEP **03** (2014) 051.
- (The v17 corpse `Hess(−log det) = Fisher–Bures` was the right-object-wrong-side version of this second-order object — explained, not resurrected.)

*The level-2 spectra.*
- A. Ikeda & Y. Taniguchi, "Spectra and eigenforms of the Laplacian on `S^n` and `P^n(C)`," Osaka J. Math. **15** (1978) 515–546 — `λ_k(CP^n) = 4k(k+n)`: `λ_2(CP²) = 32`.
- R. S. Cahn & J. A. Wolf, "Zeta functions and their asymptotic expansions for compact symmetric spaces of rank one," Comment. Math. Helv. **51** (1976) 1–21 — CROSS spectra; the Cayley plane `OP²` spectrum `λ_k = 4k(k+11)`: `λ_2 = 104`.
- A. L. Besse, *Manifolds all of whose Geodesics are Closed*, Springer (1978), ch. 3 / appendix.

*The Jordan covariant facts.*
- K. McCrimmon, *A Taste of Jordan Algebras*, Springer (2004); N. Jacobson, *Structure and Representations of Jordan Algebras*, AMS (1968) — the adjugate `M#`, `M² = M# + σ₂(M)·1`, the `Sym²` covariant content.
