# Phase 92 (v32.0-candidate) — GATE 0 SUMMARY: Machinery + Freeze

**Driver:** `python3 -u code/lichnerowicz_response.py g0` → **6/6 PASS** (~400s, exact over Q).

Gate 0 reproduces the v31 geometry, builds and verifies the certified Lichnerowicz machinery, freezes
the dim-8 (1,1)-Hermitian TT basis {t_a}, and freezes the four verdict objects.

| # | Check | Result |
|---|---|---|
| 0.geom | v31 geometry reproduced: Ric_{ab̄}=6 g_phys (Einstein, Λ=6), λ₁=12 bridge, octonion-engine↔3×3-complex field bridge | PASS |
| 0.riem | Kähler Riemann contracts to Ricci: g^{cd̄} R_{ab̄cd̄} == Ric_cert == 6 g_phys (curvature used in Rdot is consistent) | PASS |
| 0.signpin | rough-Laplacian SIGN PIN: ∇*∇ = −Δ_analyst; **λ₁=12, λ₂=32** through the rough-Laplacian sign (+12/+32 on the eigenfunctions) | PASS |
| 0.basis | extraction: all 8 directions consistent, every residue tr_g=0 AND δ=0 (each t_a is an EXPLICIT TT tensor); 8/8 nonzero | PASS |
| 0.gram | single-generator residue Gram **rank 6** (the d-symbol image of single generators) + generic-M {N(M)} **rank 8** (the full dim-8 multiplet) | PASS |
| 0.dL | **Δ_L^{(1,1)} t_d1 = 32 t** (a scalar action — eigentensor; ∇*∇ + 2Λ − 2 Rdot, Λ=6) | PASS |

## The cliff-free TT extraction (V1, the load-bearing method)

The deferred v31 positive-exhibit certificate is obtained here cliff-free. The York decomposition
`B3 = r + δ*ω + f·g` is unique (up to Killing in ω), with `r` the TT part (`tr_g r = 0` AND `δr = 0`).
We find `(ω, f)` — the same complete certified gauge+conformal ansatz as `york_solve` (δ* of {φ_A dφ_B,
φ_A d̄φ_B} over the 8 su(3) generators + identity; conformal {φ_A φ_B·g}) — such that `r := B3 − δ*ω
− f·g` is traceless AND divergence-free. **Method:** the gauge+conformal basis tensors' `(tr_g, δ)`
images are computed once as MATCHED-MONOMIAL coefficient dicts over a common ρ^7 (cached to disk;
conformal blocks via the analytic `tr_g(f·g)=4f`, `δ(f·g)_b=−∂_b f`); the target `B3`'s image is
matched against them by an EXACT CRT modular solve (Gaussian elimination over 40 primes + rational
reconstruction). The result `r = B3 − Σc_i e_i` is the explicit TT tensor.

**Why matched-monomial, not point-evaluation:** point evaluation at small-denominator rationals
produces an ill-conditioned system whose gauge coefficients explode (≥186-bit) and fail
reconstruction; matched-monomial keeps small integer-ish coefficients and reconstructs cleanly. The
exact residual over Q (all rows) is the genuine TT certificate (`tr_g r=0`, `δr=0` verified
symbolically per direction).

## The dim-8 multiplet and the d-symbol image (the rank-6/rank-8 structure)

v31 PROVED (Boucetta Table VIII, multiplicity-one) the TT residue lives in the **λ=12 (1,1)-Hermitian
su(3)-adjoint multiplet (dim 8)**; the (2,0)+(0,2) blocks are individually pure gauge.

- **The 8 single-generator residues span rank 6** (their L² Gram has rank 6). This is a genuine
  su(3) d-symbol fact, NOT a defect: the residue direction is `c(M) ∝ N(M) = M² − ⅓Tr(M²)I` (object
  (i)'s hypothesis), and for a SINGLE generator λ_a, `N(λ_a)` collapses into the Cartan, so the
  single-generator `{N(λ_a)}` spans only rank 2 (and the single-generator residues, rank 6).
- **The full dim-8 multiplet is reached by GENERIC matter:** the quadratic map `M ↦ N(M)` is
  surjective onto the dim-8 adjoint (the d-symbol is non-degenerate), and `{N(M)}` for 12 generic
  dense matters has **rank 8** (verified algebraically, exact over Q).

So the multiplet is dim-8 (Boucetta/v31), realized by generic matter; the single-generator basis
probes a rank-6 d-symbol slice (sufficient for the Schur eigenvalue, which is a single scalar because
the multiplet is irreducible).

## The frozen Lichnerowicz Δ_L^{(1,1)} and the sign pin

**Δ_L h = ∇*∇h + Ric∘h + h∘Ric − 2R̊h**, with `∇*∇ = −g^{μν}∇_μ∇_ν` the POSITIVE (geometer's) rough
Laplacian. On the Einstein background Ric=6g: **Δ_L h = ∇*∇h + 12h − 2R̊h**.

- **Sign pin (mandatory):** `∇*∇ = −Δ_analyst`; verified +12 on a λ₁ scalar, +32 on a λ₂ scalar
  through the rough-Laplacian code path BEFORE any tensor eigenvalue.
- **The full Kähler Weitzenböck R̊** is built per block (the v31-verified (1,1) form `R_{ab̄cd̄}h^{cd̄}`
  plus the holo/antiholo (2,0)/(0,2) forms), CROSS-CHECKED by `R̊(g) = Ric = 6g` and `Δ_L(g) = 0`
  (the metric is Δ_L-harmonic on KE — the known structural answer).
- **The verdict operator is Δ_L^{(1,1)}** (the (1,1) sector, where the certified v31 multiplet lives);
  it acts as the Schur SCALAR **λ_L = 32** on the multiplet (the eigentensor check, confirmed across
  directions at Gate 1f).

## The four FROZEN verdict objects (no post-hoc additions — STOP rule 3)

- **(i)** `TT(B3) = Σ_a c_a(M) t_a` over the frozen dim-8 basis {t_a} (named hypothesis: `c(M) ∝ N(M)
  = M²−⅓Tr(M²)I` — verified at Gate 3b);
- **(ii)** `‖TT(B3)‖²` closed form in the frozen tuple {(TrM²)², detM-probe} with FORCED constant;
- **(iii)** `ε = λ_L − 2Λ = λ_L − 12` (the Schur scalar; Gate 2);
- **(iv)** `B3 = TT + δ*ω + f·g` with (ω, f) in closed form (Gate 3d).

## Scope fence (binding, verbatim)

This is the deformation-complex DICTIONARY of a FROZEN imported geometry. No dynamical metric, no
selection law, no κ. LIVE = "the tensor sector's source data closes in canonical form" — a DICTIONARY
fact, not a dynamics fact. No Einstein-equation / Newton-constant / G=κT / dark-matter / geodesic
language; frozen FS geometry USED not derived; the v18/v20 MM corpse stays buried; OP² priced only.
Does NOT retract v17–v21 (Block-C statements; v32 is the strictly weaker upstream dictionary).

## Reproducibility

sympy 1.14.0, Python 3.14.5, Darwin arm64; exact rational arithmetic over Q/Q(i) (no RNG/seeds in the
verdict path; the modular CRT primes and the generic-M rank seed are deterministic and diagnostic
only). The gauge+conformal basis `(tr_g,δ)` matched-monomial images are cached to
`code/.p92_basis_images.pkl` (243 columns, 1944 monomial rowkeys; a regenerable build artifact).
