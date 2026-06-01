# Computational and Analytical Methods

**Project:** v18.0 — Gravity as the Curvature of the Peirce-Frame (Cartan / MacDowell–Mansouri) Connection on h_3(O)
**Physics Domain:** Mathematical physics — Cartan/MacDowell–Mansouri gauge gravity; quantum geometric tensor / Berry curvature of a coherent-state (rank-1 projector) family; reductive coset geometry of F_4/Spin(9); complex-structure reduction of a real eigenspace to a Lorentzian coframe; exact symbolic computation over Q on octonionic (h_3(O)) data.
**Researched:** 2026-06-01
**Overall confidence:** HIGH on the four load-bearing construction methods (QGT/Berry projector formula; MM/Cartan assembly + ε-contraction; reductive g = h ⊕ m split with Lorentz sub-block extraction; C_u → Lorentzian reduction), each pinned to a peer-reviewed source AND an in-repo exact-over-Q harness for the curvature step. MEDIUM on the one genuinely-conjectural step the milestone must *measure* not assume: whether the C_u reduction of V_{1/2}(16) lands on a forced 4-dim Lorentzian coframe (Phase A), and whether the ε-contraction is forced by the trace form rather than posited (Phase C).

### Scope Boundary

This file covers analytical/numerical PHYSICS-and-geometry METHODS: the projector-form QGT and its imaginary (Berry) part; the Cartan/MM connection assembly, curvature 2-form, and ε-contraction; the reductive coset connection on a symmetric space and Lorentz-sub-block extraction; and the complex-structure reduction to a Lorentzian coframe. Software/library version pins and the in-repo engine inventory live in COMPUTATIONAL.md. The research landscape (solid vs conjectural, the dead routes) lives in PRIOR-WORK.md / SUMMARY.md. Convention/sign traps live in PITFALLS.md.

---

## TL;DR for the roadmapper (read this first)

1. **Phase A (the KILL gate) and Phase A.5 (the SOFT-KILL gate) use DIFFERENT method families — do A first, it is the cheapest.** A is pure linear algebra over Q (Method 4 + Method 5): apply the existing π_u/C_u bottleneck to the 16-dim V_{1/2}, take the image dimension by exact rank, and read the Gram-matrix signature by exact eigenvalues. No connection, no curvature, no calculus. If the image is not 4-dim, or not Lorentzian (1,3), or the reduction needs a choice beyond (E_11, u), STOP — route dead.

2. **Phase A.5 uses the CANONICAL (tautological) Berry curvature, not the dynamical connection.** Method 1 gives `F_B = i·Tr(P[∂_μ P, ∂_ν P])` for the rank-1 projector `P(x) = ` the state at `E(x)`. This needs **no metric-compatibility / torsion equation** (it is the curvature of the Grassmannian tautological bundle), so it is cheap and computable immediately as a diagnostic. The mandatory consistency check: the REAL part of the same QGT must reproduce the dead v17.0 cone-Hessian `Hess(−log det)` (Provost–Vallée: real part = Fubini–Study metric). If it does not, the QGT construction is wrong — STOP before trusting `F_B`.

3. **Use the PROJECTOR form of the QGT everywhere, never the `|∂ψ⟩` form on the decisive path.** `Q_{μν} = Tr(P ∂_μ P ∂_ν P)` is manifestly gauge-invariant (no phase/`U(1)` ambiguity to fix), so it is the clean object for exact-over-Q symbolic evaluation. Real part = quantum metric `g_{μν}=½Tr(∂_μ P ∂_ν P)`; imaginary part = `−½ F_B`. Avoid `Q_{μν}=⟨∂_μψ|(1−P)|∂_νψ⟩` symbolically — it carries a gauge phase you would have to fix by hand (an `fp-` risk).

4. **Phase B assembles the (A)dS Cartan connection by Wise's exact recipe (Method 2), then computes `F = dA + A∧A` symbolically.** The block split is fixed: `F = R[ω] − (Λ/3) e∧e + d_ω e`; so(3,1) block = Riemann + cosmological, R^{3,1} block = torsion. The Lorentz block `R[ω]` is the 4d Riemann tensor — cross-check it against the in-repo `hand_rolled_riemann_of_g` Levi-Civita engine on ≥5 components (the same Ph72/73 harness).

5. **Extract `ω` (the Lorentz spin connection) as the so(3,1) sub-block of the ambient so(9,1) reductive connection (Method 3), do NOT use the raw 45-dim Spin(9,1) curvature.** The reductive split is `f_4 = spin(9) ⊕ V_{1/2}(16)` at the algebra level and, for the non-compact slice, `e_{6(-26)} ⊃ stab(E_11)` with Levi ~ so(9,1) ⊃ so(3,1) ⊕ so(6); project onto the so(3,1) Lorentz block. Gravity is the 10-dim `A = ω ⊕ e`, never the 45-dim connection.

6. **Everything decisive stays EXACT over Q.** Reuse `ring_lemma_verification.py` (det_3 SSOT, Tr, polarize_d, jordan), `orbit_dimension_gate.py` (exact `Matrix.rank` over QQ; `infinitesimal_action`), and the `bulk_geometry_verification.py` curvature harness (`totaro_riemann`, `hand_rolled_riemann_of_g`, `ricci_scalar`, `ricci_decomposition_n4`, `sectional_curvature`, `h3_constant_curvature`). Do NOT rebuild octonion arithmetic; `octonion_algebra.py` is BANNED. **NOTE:** the spec cites `code/peirce_coupling.py` as a build-on but **that file is not present in the repo** — the Peirce decomposition under E_11 must be drawn from `ring_lemma_verification.py` / `embedding_under_E_verification.py` (which carry the jordan product and the E_11 grade structure) or implemented fresh in Phase 0 (flagged for the roadmapper, see Gaps).

---

## Recommended Methods

### Primary Analytical Methods

| Method | Purpose | Applicability | Limitations |
| ------ | ------- | ------------- | ----------- |
| **M1. Projector-form QGT + Berry curvature** `Q_{μν}=Tr(P ∂_μP ∂_νP)`, `F_B = i·Tr(P[∂_μP,∂_νP])` | Phase A.5: the canonical Berry curvature of the idempotent/state family `E(x)`; its M=0 vacuum level; Einstein-vs-EM shape; and the consistency check that Re(Q) = cone-Hessian | Any smooth rank-1 (or rank-r) projector family; gauge-invariant, no phase fixing | Canonical (tautological) `F_B` is a DIAGNOSTIC, not the dynamical `F` of Phase B; `F_B` and the assembled `F` need not be equal |
| **M2. Cartan/MM connection assembly + ε-contraction** `A=ω+(1/ℓ)e`, `F=dA+A∧A=R[ω]−(Λ/3)e∧e+d_ω e`, `S∝∫ε F̂∧F̂` | Phase B: assemble the (A)dS connection, read off Riemann + cosmological + torsion; Phase C: audit whether the ε-contraction (Einstein term) is forced or posited | A coframe `e` (soldering form) and a Lorentz connection `ω` valued in the reductive split so(4,1)/so(3,2) ≅ so(3,1) ⊕ R^{3,1} | The action `∫ε F̂∧F̂` is *posited* in MM; Phase C must decide if the ε-tensor/Hodge-⋆ is fixed by the h_3(O) trace form (else `fp-imported-action`) |
| **M3. Reductive-coset Cartan connection + Lorentz sub-block extraction** `g = h ⊕ m`, canonical (Nomizu) connection, project to so(3,1) | Phase B(b): obtain `ω` = the Lorentz Spin(3,1) part of the ambient Spin(9,1) connection compatible with `e`, via the reductive `f_4 = spin(9) ⊕ V_{1/2}` (and non-compact `e_{6(-26)}`) split | Reductive (Ad_H-invariant `m`); for a symmetric space `[m,m]⊂h` ⇒ torsion-free canonical connection = Levi-Civita | F_4/Spin(9) IS symmetric (so canonical = torsion-free), but the *physical* `ω` must be metric-compatible with the *reduced 4d* `e`, which is a sub-quotient — torsion need not vanish after reduction (a Phase-B output to MEASURE) |
| **M4. Complex-structure reduction to a Lorentzian coframe** `π_u : V_{1/2}(16) → ` 4-dim, induced pairing from det/trace form | Phase A(a,b): the C_u bottleneck (the Phase-46 mechanism that sent `h_2(O) → h_2(C_u) ≅ R^{3,1}`) applied to `V_{1/2}`; image dimension + Gram signature | `u = e_7` is a fixed complex structure; the pairing is the restriction of the cubic-norm polarization / trace form | The parallel to V_0 (which gave 4-dim Lorentzian) is a HEURISTIC, not a theorem for V_{1/2}; the image dim and signature MUST be computed, not assumed (the Phase-A KILL) |
| **M5. Orbit–stabilizer / infinitesimal-action rank** (residual structure group; forced-vs-arbitrary) | Phase 0 calibration anchors; Phase A(c): is the residual structure group on the 4-dim coframe ⊇ SO(3,1) and FORCED by (E_11,u)? | Char-0 Lie-algebra action; generic orbit dim = rank of the infinitesimal-action matrix at a generic integer point | Distinguishes "SO(3,1) is forced" from "an extra choice was smuggled in" only if the stabilizer/normalizer computation is done over the SAME (E_11,u) data — an arbitrary frame choice would show up as extra free parameters |

### Primary Numerical Methods

| Method | Purpose | Convergence | Cost Scaling | Implementation |
| ------ | ------- | ----------- | ------------ | -------------- |
| **Exact rational arithmetic (SymPy over QQ)** | The DECISIVE path: octonion arithmetic, det_3, image/Gram ranks, QGT components, curvature components, signature eigenvalues | Exact (no convergence notion) | Rank over QQ via `DomainMatrix` ~ O(n^3) in matrix entries, but entry blow-up from octonion products is the real cost — bounded by working with rational basepoints | `sympy.Matrix.rank()` / `DomainMatrix(...).rank()`; in-repo `exact_qq_rank`, `span_rank_over_QQ` |
| **Generic-point sampling over Z** | Establish an image dimension / Gram rank / non-vanishing at a GENERIC point (rank is lower-semicontinuous: max over a few integer points = generic rank) | Generic rank reached at ≥2 generic integer points w.h.p. | A few exact rank evals | `octonionic_points()` / `generic_rational_X()` pattern (in `ring_lemma_verification.py`, `orbit_dimension_gate.py`) |
| **High-precision mpmath spot-check** | Triage which QGT/curvature components are nonzero before a full symbolic simplify; sanity-check a signature | High-precision float, cross-check only | Cheap | mpmath; NEVER a decisive verdict (that is `fp-float-decisive`) |

### Computational Tools

| Tool | Version | Purpose | Why |
| ---- | ------- | ------- | --- |
| SymPy | 1.14.0 (confirmed in env) | Exact symbolic algebra; `Matrix.rank()`, `Matrix.eigenvals()`, `Poly`, `diff`, `simplify`, `cancel`, exterior products by hand | The whole program runs exact over Q; `DomainMatrix` over QQ is the fast exact-rank path (used in-repo) |
| NumPy | 2.4.2 (confirmed in env) | Float spot-checks only (signature eigenvalue triage) | NEVER on a decisive rank/eigenvalue/zero-test (`numpy.linalg.matrix_rank` is a FORBIDDEN PROXY on the decisive path, engine convention) |

### Supporting Libraries

| Library | Language | Purpose | When to Use |
| ------- | -------- | ------- | ----------- |
| `sympy.diffgeom` | Python | `metric_to_Christoffel_2nd`, `metric_to_Riemann_components` from an explicit metric | ONLY on the reduced 4-dim slice metric AS A CROSS-CHECK; prefer the closed-form Totaro/hand-rolled engines for the decisive numbers (cost + simplify control) |
| `ring_lemma_verification.py` | Python (in-repo) | det_3 SSOT, Tr, Tr2, c(X,Y), polarize_d, jordan, jordan_L_matrix, X_from_symbols, exact-Q guards | det/trace/Jordan products on h_3(O); the cubic-norm polarization tensor for the induced pairing (M4) and any trace-form contraction (Phase C) |
| `orbit_dimension_gate.py` | Python (in-repo) | `infinitesimal_action`, `exact_qq_rank`, `span_rank_over_QQ`, f_4/e_6 generator machinery, calibration anchors | Phase 0 anchors; Phase A(c) forced-structure-group rank; any new stabilizer count |
| `bulk_geometry_verification.py` | Python (in-repo) | `totaro_riemann`, `hand_rolled_riemann_of_g` (Levi-Civita ≥5-component cross-check), `ricci_scalar`, `ricci_decomposition_n4`, `sectional_curvature`, `h3_constant_curvature` (the K=−1/2 benchmark) | Phase B Riemann cross-check + vacuum Einstein/(A)dS test + the H^3 sign calibration; Phase A.5 Re(QGT)=cone-Hessian consistency check |
| `embedding_under_E_verification.py` | Python (in-repo) | octonion arithmetic, jordan, proj_u, slice_to_complex, the E-bottleneck | the π_u / C_u reduction (M4) reuses `proj_u`/`slice_to_complex`; Peirce-grade bookkeeping under E_11 |

---

## Method Details

### Method 1 — Projector-form Quantum Geometric Tensor and Berry Curvature (Phase A.5)

**What.** For a smooth family of rank-1 states `|ψ(x)⟩` with projector `P(x) = |ψ(x)⟩⟨ψ(x)|` over the 4d base, the quantum geometric tensor (QGT) and its parts are

```
Q_{μν}(x) = Tr( P  ∂_μ P  ∂_ν P )                          (projector form, gauge-invariant)
g_{μν}    = Re Q_{μν} = ½ Tr( ∂_μ P  ∂_ν P )                 (quantum metric = Fubini–Study)
F_B,{μν}  = −2 Im Q_{μν} = i·Tr( P [∂_μ P, ∂_ν P] )          (Berry curvature 2-form)
```

Equivalently in the state form (carries a gauge phase — avoid symbolically): `Q_{μν} = ⟨∂_μψ|(1−P)|∂_νψ⟩`, with `g = Re Q`, `F_B = −2 Im Q = i(⟨∂_μψ|∂_νψ⟩ − ⟨∂_νψ|∂_μψ⟩)`.

**Mathematical basis.** Provost & Vallée (CMP 76, 289–301, 1980): the Hilbert-space metric on a parametrized state manifold has a gauge-invariant complex tensor whose **real part is a Riemannian (Fubini–Study) metric** and whose **imaginary part is of symplectic structure = the Berry curvature**. The projector form is the eigenprojector/Bloch-vector route (Graf & Piéchon, PRB 104, 085114, arXiv:2102.09899; Wikipedia "Quantum geometry (condensed matter)"). `F_B` is the curvature of the **tautological/canonical connection** on the Grassmannian/projective eigenbundle — it requires no metric-compatibility or torsion equation, which is exactly why Phase A.5 is cheap.

**What it outputs.** (a) `F_B` at M=0 — flat, pure-Λ (`F_B ∝ e∧e`), or other (the vacuum level). (b) `F_B` with `M ∈ V_{1/2}` turned on — whether the matter-sourced part is "Einstein-shaped" (its ε-contraction `F_B ∧ F_B` onto the Lorentz block matches a `V_{1/2}` stress-energy `T[M]` at the SAME order in M and on the SAME support) or "EM-shaped" (a generic U(1)-type field strength). (c) The same-wall check: does `F_B`'s matter source come out non-proportional to `T[M]` the way the cone-Hessian's did (support disjoint from `T`, ~10^3 magnitude/shape mismatch)?

**Consistency check (mandatory).** Compute `Re Q_{μν}` and confirm it reproduces the dead v17.0 cone-Hessian `Hess(−log det)` (via `bulk_geometry_verification.py`). If it does not, the QGT construction or the state family `|ψ(x)⟩` is wrong — STOP before trusting `F_B`. (This is the load-bearing identity that justifies "the dead route was the real part, this route is the imaginary part" — the v17.0 NONE binds only Re Q.)

**Known failure modes.** (i) Using the `|∂ψ⟩` form symbolically introduces an undetermined gauge phase `e^{iα(x)}` that must be fixed by hand — use the projector form. (ii) `F_B` is the CANONICAL curvature; a vanishing or EM-shaped `F_B` does not by itself kill Phase B's dynamical `F` (they can differ), but a hopeless same-wall mismatch is the SOFT-KILL signal. (iii) Power-counting/support matching (the v17.0 Ph73 lesson) is the real test, not "some 2-form appears."

**Implementation notes.**
```
# rank-1 state at E(x): |ψ⟩ ∝ a column/eigenvector of the idempotent E(x) (P = E in the
#   formally-real Jordan setting: primitive idempotents ARE rank-1 projectors).
# Work in a complex matrix model of the relevant block; differentiate P(x) symbolically in x.
P  = E(x)                                  # primitive idempotent field, exact-over-Q entries
dP = [diff(P, x[mu]) for mu in range(4)]
Q  = lambda mu,nu: (P * dP[mu] * dP[nu]).trace()        # exact
g  = lambda mu,nu: sympy.Rational(1,2)*(dP[mu]*dP[nu]).trace()
FB = lambda mu,nu: sympy.I*(P*(dP[mu]*dP[nu]-dP[nu]*dP[mu])).trace()
# decisive numbers: simplify/cancel over QQ (or QQ(I)); never numpy.
```
**Confidence:** HIGH on the formula and the real/imaginary split (Provost–Vallée, multiply attested). MEDIUM on the cleanest matrix realization of `P = E(x)` over octonionic entries (a Phase-0/A.5 modeling step — see Gaps; the QGT is naturally a complex-Hermitian object, so the C_u complex structure likely enters here too).

---

### Method 2 — Cartan / MacDowell–Mansouri Connection Assembly and ε-Contraction (Phase B, Phase C)

**What.** Assemble the (anti-)de Sitter Cartan connection and read off 4d gravity from its curvature, then audit the action contraction.

**Mathematical basis (Wise, gr-qc/0611154, eqs. as extracted from the paper).** Gauge group `G ⊃ SO(3,1)` with `G = SO(4,1)` for `Λ>0`, `SO(3,2)` for `Λ<0`. The Lie algebra has a **Killing-orthogonal, SO(3,1)-invariant vector-space split** (not a Lie-algebra split):

```
so(4,1) ≅ so(3,1) ⊕ R^{3,1}                                         (Wise eq. 1)
```

The Lorentz connection `ω` and coframe `e` combine into one `G`-connection:

```
A = ω + (1/ℓ) e ,        ℓ = constant with units of length, ℓ² = 3/Λ     (Wise eq. for A)
```

Its curvature `F[A] = dA + A∧A` splits along the same decomposition:

```
F = R[ω] − (Λ/3) e∧e + d_ω e
      └── so(3,1) block ──┘   └ R^{3,1} block ┘
    so(3,1) block = R[ω] − (Λ/3) e∧e          (Riemann + cosmological term)
    R^{3,1} block = d_ω e = de + ω∧e          (torsion T)
```

With `ℓ²=3/Λ`, `F[A]=0` precisely when `ω` is the torsion-free spin connection of a spacetime locally isometric to de Sitter. The MM action and its Palatini equivalence:

```
S_MM[A] = (−3 / 2GΛ) ∫ tr( F̂ ∧ ⋆ F̂ )                                 (Wise eq. 2)
      F̂ = projection of F into so(3,1); ⋆ = internal Hodge star.
      The projection BREAKS SO(4,1) → SO(3,1) (by hand, or by spontaneous SSB).
S_Pal = S_MM − (3 / 2GΛ) ∫ tr( R ∧ ⋆R )                                (topological/GB difference)
```

In the `ε_{abcd}` form, `tr(F̂∧⋆F̂) ∝ ε_{abcd} F^{ab}∧F^{cd}` over the so(3,1) block; expanding `F^{ab}=R^{ab}−(Λ/3)e^a∧e^b` gives three pieces:
`ε R^{ab}∧R^{cd}` (Gauss–Bonnet, topological), `ε R^{ab}∧e^c∧e^d` (Einstein–Hilbert), `ε e^a∧e^b∧e^c∧e^d` (cosmological Λ).

**What it outputs.** Phase B: `R[ω]` (the 4d Riemann tensor — identify and cross-check), the cosmological piece `−(Λ/3)e∧e` (read off `Λ`'s value/sign as MEASURED), and the torsion `d_ω e` (vanishes? matter-sourced?). Phase C: a verdict on whether the `ε`/`⋆` contraction is FIXED by the h_3(O) trace form (STRONG WIN) or POSITED (the GST sin in new clothes = `fp-imported-action`).

**Known failure modes / limitations.** (i) The Einstein term in `S_MM` appears **only because of the specific ε-contraction / symmetry-breaking projection `F̂`** — Wise is explicit that "we have broken symmetry in the Lagrangian by hand." Reproducing Einstein–Hilbert from `∫ε F∧F` is therefore NOT a derivation unless the contraction is forced by intrinsic data (Phase C, the whole point). (ii) Conventions: Wise uses `Λ>0 → SO(4,1)`; the milestone's corrected §6 expects `Λ=0` / flat vacuum (do NOT reintroduce `Λ<0`); read `Λ` as an output, and note the `−Λ/3` coefficient sign is convention-locked to the K=−1/2 H^3 benchmark before any verdict. (iii) `ℓ²=3/Λ` is singular at `Λ=0` — at the flat vacuum the Poincaré contraction `iso(3,1)` is the right model algebra, not `so(4,1)`; assemble `A` in `iso(3,1)` when `Λ→0` (Wise's "rolling" picture degenerates smoothly).

**Implementation notes.**
```
# Represent ω as an antisymmetric so(3,1)-valued 1-form ω^{ab}_μ dx^μ; e as e^a_μ dx^μ.
# Build A as a (4+1)x(4+1) so(4,1) matrix [[ω^{ab}, (1/ℓ)e^a],[-(1/ℓ)e_b, 0]] (Λ>0)
#   or the iso(3,1) contraction at Λ=0.
# F = dA + A∧A computed as exterior derivative + wedge of matrix-valued forms, by hand,
#   exact over Q (component functions are rational in the slice coordinates).
# Lorentz block of F → R[ω]; cross-check R[ω] vs hand_rolled_riemann_of_g on ≥5 components.
```
**Confidence:** HIGH on the formulas (extracted verbatim from Wise gr-qc/0611154). HIGH that the Einstein term is contraction-dependent (this is the explicit content of the MM "trick"); MEDIUM on whether the h_3(O) trace form supplies that contraction — the Phase-C question, genuinely open.

---

### Method 3 — Reductive-Coset Cartan Connection and Lorentz Sub-Block Extraction (Phase B(b))

**What.** Obtain `ω` = the Lorentz Spin(3,1) part of the ambient Spin(9,1) connection, compatible with the reduced coframe `e`, via the reductive structure of the coset.

**Mathematical basis.** On a reductive homogeneous space `G/H` with `Ad_H`-invariant split `g = h ⊕ m` (here, at the algebra level, `f_4 = spin(9) ⊕ V_{1/2}(16)` — `spin(9) = h`, `m = V_{1/2} = T_E OP^2`), the **canonical (Nomizu 1954) connection** is the `h`-component of the Maurer–Cartan form. For a SYMMETRIC space (`[m,m] ⊂ h` — true for F_4/Spin(9)), the canonical connection is **torsion-free and = Levi-Civita** of the invariant metric (Encyclopedia of Math; "Symmetric space", Wikipedia; Nomizu). The non-compact real form relevant to spacetime sits in `Stab_{E_6(-26)}(E_11)` with Levi ~ `so(9,1) ⊃ so(3,1) ⊕ so(6)` (the milestone's Lorentz × internal split). The physical spin connection `ω` is the **projection of the `h`-connection onto the so(3,1) Lorentz block** selected by (E_11, u).

**What it outputs.** `ω^{ab}` (a, b = Lorentz indices) as the so(3,1) part of the reductive connection; the metric/torsion compatibility condition `de^a + ω^a_b ∧ e^b = T^a` to be solved/measured. The reference benchmark to reproduce first (Phase 0/calibration): `dim Stab_{E_6}(E_11) = 61`, `Stab_{V_0} = 45 = Spin(9,1)`, `e_6 = 78 = 52+26`, `orbit(E_11)=17`.

**Known failure modes / limitations.** (i) F_4/Spin(9) is RIEMANNIAN symmetric (compact, positive-definite) — its canonical connection is torsion-free, but the PHYSICAL object is the connection compatible with the *Lorentzian, 4d-reduced* coframe, a sub-quotient of `m = V_{1/2}`; torsion need not vanish after the C_u reduction, so `T = d_ω e` is a Phase-B OUTPUT to measure, not assume zero. (ii) "Lorentz sub-block of so(9,1)" is forced only if (E_11, u) selects a unique so(3,1) ⊂ so(9,1); the so(3,1) ⊕ so(6) split must be the (E_11,u)-stabilizer-compatible one (cross-check with the Phase-48 so(3) × so(6) data and Method 5). (iii) Do NOT compute the raw 45-dim Spin(9,1) curvature and call it gravity — gravity is the 10-dim `A = ω ⊕ e`; the 45-dim connection is the ambient frame data only.

**Confidence:** HIGH on the reductive/canonical-connection machinery and the symmetric-space torsion-free fact (textbook, Nomizu/Kobayashi–Nomizu). MEDIUM on the cleanest extraction of the Lorentzian so(3,1) sub-block from the non-compact `e_{6(-26)}` slice (a Phase-B construction; the compact F_4 picture must be transported to the non-compact real form — see PITFALLS on compact-vs-noncompact).

---

### Method 4 — Complex-Structure Reduction of V_{1/2} to a Lorentzian Coframe (Phase A(a,b))

**What.** Apply the C_u bottleneck (`u = e_7`) to the 16-dim soldering form `e = dE ∈ V_{1/2}(E_11)`, compute the image dimension and the signature of the induced pairing — the Phase-A KILL gate.

**Mathematical basis.** A complex structure on a real even-dimensional space halves dimension by selecting the `+i` eigenspace / a complex-linear quotient. The established precedent (this program's Phase 46, `52-kkt-spacetime` / `52-observer-uniqueness`): `π_u` sent `V_0 = h_2(O)` (10-dim real) to `h_2(C_u) ≅ R^{3,1}` (4-dim) with the **det/cubic-norm restricting to the Minkowski quadratic form** `det = t² − x² − y² − z²`, signature (1,3) — the same mechanism by which 2×2 Hermitian matrices over C model Minkowski space (confirmed: nLab "Minkowski metric"; the SL(2,C) → SO(1,3) double cover; for division algebras R,C,H,O the 2×2 Hermitian determinant IS the Minkowski form in dims 3,4,6,10). The METHOD for V_{1/2} is the SAME `π_u`, with the induced pairing taken from the **cubic-norm polarization `polarize_d`** (or the trace form) restricted to the image.

**What it outputs.** (a) `dim π_u(V_{1/2}(16))` by exact rank over QQ (the KILL number — expect 4). (b) The Gram matrix of the induced pairing on the image, by exact eigenvalues over QQ → signature (the KILL signature — expect Lorentzian (1,3), mostly-minus). (c) Feeds Method 5 for the forced-vs-arbitrary structure-group verdict.

**Known failure modes / limitations.** (i) The V_0 → 4d-Lorentzian precedent is a HEURISTIC for V_{1/2}, NOT a theorem — V_{1/2} is 16-dim (vs V_0's 10) and carries a different Spin(9) representation, so the image could be ≠ 4 or non-Lorentzian; this is precisely the KILL gate and must be COMPUTED. (ii) `fp-arbitrary-reduction`: if reaching 4-dim requires a choice beyond (E_11, u) (e.g. picking a sub-octonion line by hand), it is not a result — the reduction must be forced. (iii) The induced pairing must come from intrinsic h_3(O) data (cubic-norm polarization / trace form), not from a metric inserted by hand. (iv) Reuse `proj_u`/`slice_to_complex` from `embedding_under_E_verification.py` so the C_u mechanism is literally the same map as the validated V_0 case.

**Implementation notes.**
```
# V_{1/2}(E_11) = the (1,2) and (1,3) octonionic off-diagonal slots (16 real dims).
# π_u: apply the SAME C_u projection that sent V_0 → h_2(C_u); restrict octonion entries
#   to the C_u = span_R{1,u=e7} sub-line per the Phase-46 mechanism.
basis_Vhalf = [ ... 16 real basis elements of V_{1/2} ... ]
img = [ pi_u(b) for b in basis_Vhalf ]
image_dim = Matrix([flatten(v) for v in img]).rank()        # exact over QQ  → KILL number
Gram = Matrix([[ pairing(img[i], img[j]) for j in ...] for i in ...])  # polarize_d / trace form
signature = sign_counts(Gram.eigenvals())                    # exact → expect (1,3)
```
**Confidence:** HIGH on the C_u mechanism and the V_0 precedent (validated in-repo, `52-kkt-spacetime`). LOW–MEDIUM on the OUTCOME for V_{1/2} (the open KILL question — by design).

---

### Method 5 — Orbit–Stabilizer / Infinitesimal-Action Rank (Phase 0 anchors; Phase A(c))

**What.** Compute residual structure-group dimensions and decide forced-vs-arbitrary via exact ranks of infinitesimal-action matrices.

**Mathematical basis.** Generic orbit dimension = rank of the infinitesimal-action matrix at a generic point (Derksen–Kemper, char 0; the in-repo `orbit_dimension_gate.py` reproduces orbit 24 / Spin(8) at single copy). For Phase A(c): the residual structure group on the 4d coframe is the subgroup of the ambient (Spin(9,1)) that (i) fixes E_11 and u, and (ii) preserves the reduced coframe; its Lie algebra is the kernel of the appropriate action, computed as a nullspace/rank over QQ. SO(3,1) is FORCED iff this stabilizer-compatible residual group contains so(3,1) with no extra free parameters tracing to an arbitrary frame choice.

**What it outputs.** The dimension and identification of the residual structure group (⊇ SO(3,1)?); the forced-vs-arbitrary verdict (extra free parameters ⇒ a smuggled choice ⇒ `fp-arbitrary-reduction`).

**Known failure modes / limitations.** (i) An arbitrary basis choice in V_{1/2} can masquerade as "extra structure" — anchor the computation to the (E_11, u) data only. (ii) Reproduce the calibration anchors (orbit(E_11)=17, Stab_{E_6}(E_11)=61, Stab_{V_0}=45) BEFORE trusting any new stabilizer count (the Phase-0 gate). (iii) The v16.0 GATE surprise (naive "7" refuted by the orbit method) is the cautionary precedent: do not trust a back-of-envelope dimension count; run the rank.

**Confidence:** HIGH (the method and the in-repo harness are validated across v16.0/v17.0).

---

## Phase → Method Map

| Phase | Goal | Methods | Decisive exact-over-Q outputs |
| ----- | ---- | ------- | ----------------------------- |
| **0** | Engine recovery; tangent identity; calibration | det_3 SSOT (ring_lemma); M5 (orbit anchors); Peirce-grade bookkeeping (ring_lemma/embedding — `peirce_coupling.py` ABSENT, see Gaps) | `E_11∘δ=(1/2)δ`; `T_{E_11}OP^2=V_{1/2}(16)`; anchors 17/61/45/78; CH + 324/324 |
| **A** (KILL) | C_u reduces V_{1/2}(16) to a forced 4d Lorentzian coframe? | **M4** (image dim + Gram signature); **M5** (residual structure group, forced-vs-arbitrary) | image dim (expect 4); Gram signature (expect (1,3)); SO(3,1) forced (yes/no) |
| **A.5** (SOFT KILL) | Canonical Berry curvature Einstein-shaped or EM-shaped? | **M1** (projector `F_B`); cone-Hessian consistency check via `bulk_geometry_verification.py` | Re(Q)=Hess(−log det) (consistency); `F_B` at M=0; `F_B` matter-source M-power/structure/support vs `T[M]` |
| **B** (if A,A.5 survive) | `F=dA+A∧A` Lorentz block = 4d Riemann; vacuum Einstein/(A)dS; V_{1/2}-sourced | **M2** (assemble A, compute F, block split); **M3** (extract ω); `hand_rolled_riemann_of_g` (≥5-component cross-check); `h3_constant_curvature` (K=−1/2 benchmark); `ricci_decomposition_n4` | invertible `e` (det≠0); `R[ω]` = Riemann (cross-checked); `Λ` value/sign; torsion `d_ω e`; matter-sourced Ricci |
| **C** (audit) | ε-contraction (Einstein term) forced by trace form or posited? | **M2** (ε/⋆ contraction); trace-form contraction via `polarize_d`/Tr (ring_lemma) | is `ε_{abcd}`/`⋆` fixed by the h_3(O) trace form (STRONG WIN) or external (fp-imported-action)? |

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
| -------- | ----------- | ----------- | ------- |
| QGT form | Projector `Q=Tr(P ∂P ∂P)` (M1) | State form `Q=⟨∂ψ|(1−P)|∂ψ⟩` | Carries a gauge phase to fix by hand symbolically (an `fp-` risk); projector form is manifestly gauge-invariant |
| Berry-curvature object for the SOFT-KILL diagnostic | Canonical/tautological `F_B` (M1) | The full dynamical `F=dA+A∧A` of Phase B | The canonical `F_B` needs no metric/torsion equation → cheap; the dynamical `F` is the load-bearing object but expensive — gate with `F_B` first |
| 4d Riemann computation | Block split of `F` (M2) + `hand_rolled_riemann_of_g` cross-check | `sympy.diffgeom` on the assembled connection | Connection-side curvature is `dA+A∧A` (a 2-form), not a metric-Christoffel chain; use the structure equation, cross-check the Lorentz block against the Levi-Civita engine |
| Spin connection ω | Reductive `h`-projection to so(3,1) (M3) | Raw 45-dim Spin(9,1) curvature | Spin(9,1) is the AMBIENT group; gravity is the 10-dim `A=ω⊕e` — using the 45-dim curvature is a category error the spec explicitly forbids |
| Decisive arithmetic | Exact over QQ (SymPy `Matrix.rank`, `eigenvals`) | numpy float ranks/eigenvalues | `fp-float-decisive` — banned on decisive verdicts; rank/signature/curvature must be exact |
| Octonion arithmetic | `ring_lemma_verification.py` det_3 SSOT | `octonion_algebra.py` det_3 | BANNED — buggy `(x1 x2)x3` cross-term order, float, 0.67 associator gap |
| Spacetime metric source | (this route) imaginary part of QGT / Lie sector | (v17.0) real part / cone-Hessian `Hess(−log det)` | The cone-Hessian is the SYMMETRIC sector → verdict NONE; that NONE binds only Re(Q), not the antisymmetric `F_B`/`F` |

---

## Installation / Setup

```bash
# Environment is already provisioned (confirmed in repo):
#   Python 3, SymPy 1.14.0, NumPy 2.4.2 — no new packages required for the decisive path.
# Optional cross-check only:
#   sympy.diffgeom ships with SymPy 1.14 (no install).
# DO NOT pip-install a new computer-algebra/group-theory package on the decisive path
#   without orchestrator permission; the exact-over-Q SymPy harness is sufficient and validated.
```

---

## Validation Strategy

| Check | Expected Result | Tolerance | Reference |
| ----- | --------------- | --------- | --------- |
| det_3 Cayley–Hamilton + F_4-invariance | CH holds; 324/324 inner-derivation annihilation | exact over Q | `ring_lemma_verification.py` (in-repo SSOT) |
| Tangent identity | `E_11∘δ=(1/2)δ` for `δ∈V_{1/2}`; `T_{E_11}OP^2=V_{1/2}(16)` | exact over Q | McCrimmon (Peirce); Baez 2002 §3.4 |
| Calibration anchors | orbit(E_11)=17; Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1); e_6=78 | exact | `orbit_dimension_gate.py` |
| QGT real-part consistency (A.5) | `Re Q_{μν}` = cone-Hessian `Hess(−log det)` | exact over Q | Provost–Vallée 1980; `bulk_geometry_verification.py` |
| H^3 sign benchmark | cone-Hessian on `det=1` hyperboloid has `K = −1/2` | exact | `h3_constant_curvature` (in-repo); round-sphere `K=−1` differs by factor 2 |
| Riemann cross-check (B) | `R[ω]` (from `F`) = Levi-Civita Riemann on ≥5 components | exact over Q | `hand_rolled_riemann_of_g` (in-repo; the Ph72/73 harness) |
| Image-dimension KILL (A) | `dim π_u(V_{1/2}(16))` = 4 (or KILL) | exact rank over QQ | M4; `52-kkt-spacetime` precedent |
| Gram-signature KILL (A) | Lorentzian (1,3) (or KILL) | exact eigenvalues over QQ | M4; `det = t²−x²−y²−z²` (nLab Minkowski metric) |
| Vacuum structure (B(d)) | M=0 flat / pure-Λ (NOT the dead `R×H^3`); read `Λ` as measured | exact | corrected CONVENTIONS §6 (Λ=0, flat KKT η) |

---

## Sources

- **D. K. Wise, "MacDowell–Mansouri gravity and Cartan geometry," arXiv:gr-qc/0611154, Class. Quantum Grav. 27 (2010) 155010.** THE reference for Method 2; exact eqs. extracted: `so(4,1)≅so(3,1)⊕R^{3,1}` (eq. 1), `A=ω+(1/ℓ)e`, `F=R−(Λ/3)e∧e+d_ω e` (ℓ²=3/Λ), `S_MM=(−3/2GΛ)∫tr(F̂∧⋆F̂)` (eq. 2), Palatini difference `(3/2GΛ)∫tr R∧⋆R`. Confidence HIGH (primary, formulas read directly).
- **MacDowell & Mansouri, Phys. Rev. Lett. 38 (1977) 739.** Original broken de Sitter/Lorentz gauge theory; the `∫ε F∧F → EH+Λ` result. Confidence HIGH (canonical, via Wise).
- **Provost & Vallée, "Riemannian structure on manifolds of quantum states," Commun. Math. Phys. 76 (1980) 289–301.** Method 1: QGT real part = gauge-invariant Riemannian (Fubini–Study) metric, imaginary part = symplectic/Berry curvature. Confidence HIGH (primary; verified via Springer/ProjectEuclid + multiple secondary attestations).
- **Graf & Piéchon, "Berry curvature and quantum metric in N-band systems — an eigenprojector approach," Phys. Rev. B 104 (2021) 085114, arXiv:2102.09899.** Method 1 projector form `Q=Tr(P ∂P ∂P)`, gauge-invariant `g=½Tr(∂P∂P)`, `F_B` from `P`-commutators. Confidence HIGH (peer-reviewed; projector formula also on Wikipedia "Quantum geometry (condensed matter)").
- **R. W. Sharpe, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (Springer, 1997).** Method 3: Cartan connections, soldering forms, reductive `g=h⊕m`. Confidence HIGH (standard text).
- **K. Nomizu, "Invariant affine connections on homogeneous spaces," Amer. J. Math. 76 (1954) 33–65** (+ Kobayashi–Nomizu, *Foundations of Differential Geometry* vol. II; Encyclopedia of Math "Homogeneous space"; Wikipedia "Symmetric space"). Method 3: canonical connection on a reductive `G/H`; for symmetric spaces `[m,m]⊂h` ⇒ torsion-free = Levi-Civita. Confidence HIGH.
- **J. C. Baez, "The Octonions," Bull. Amer. Math. Soc. 39 (2002) 145–205, arXiv:math/0105155, §3.4 (Cayley plane).** `OP^2=F_4/Spin(9)`, `T_E OP^2 = V_{1/2}(E)`; F_4 = Aut(J_3(O)). Confidence HIGH (Cayley-plane = F_4/Spin(9) cross-confirmed via Wikipedia "Cayley plane"/HandWiki).
- **K. McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004).** Peirce decomposition, primitive idempotents, the `E∘δ=(1/2)δ` tangent identity. Confidence HIGH (standard text).
- **nLab "Minkowski metric"; SL(2,C)→SO(1,3) double cover (multiple sources).** Method 4 precedent: the 2×2 Hermitian determinant over a division algebra IS the Minkowski form, `det = t²−x²−y²−z²`, signature (1,3); division-algebra dims 3,4,6,10. Confidence HIGH.
- **Faraut & Koranyi, *Analysis on Symmetric Cones* (Oxford, 1994).** Cone-Hessian (real-part-of-QGT) consistency cross-check ONLY (the v17.0 object). Confidence HIGH (used in v17.0).
- **In-repo harness (validated v16.0/v17.0, exact over Q):** `ring_lemma_verification.py` (det_3 SSOT), `orbit_dimension_gate.py` (exact-rank orbit method), `bulk_geometry_verification.py` (`totaro_riemann`, `hand_rolled_riemann_of_g`, `ricci_scalar`, `ricci_decomposition_n4`, `sectional_curvature`, `h3_constant_curvature`), `embedding_under_E_verification.py` (`proj_u`, `slice_to_complex`, octonion arithmetic). Confidence HIGH.

### External tool note
The arXiv ABSTRACT page for gr-qc/0611154 did not yield equations via WebFetch (abstract-only), and a first WebFetch of the PDF returned binary stream metadata; the equations in Method 2 were extracted by downloading the PDF and running `pdftotext` locally (lines 55–130 of the converted text), so they are quoted from the primary source, not training data. No search returned a benchmark numeric value requiring separate verification.
