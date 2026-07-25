# GPD Prompt: Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry

## Context (read first)

This is a **fresh route to gravity** that replaces two dead ones. Do NOT
import the machinery of either:

- **DEAD (lattice/Fisher):** `paper6-continuum-limit-prompt.md` builds a
  smooth metric from a self-modeling lattice's Fisher geometry. Abandoned -
  the lattice is a modeling choice reviewers reject. We use **no lattice**.
- **DEAD (det/GST/Weinberg):** derivations `47-*` through `50-*` and `53-*`
  posit the GST/N=2 supergravity Lagrangian with det(X) as prepotential and
  read off the Einstein term. This is **circular** (the supergravity multiplet
  data, including -R/2, is fixed by the SUSY closure that is assumed). We
  posit **no Lagrangian and no SUSY**.

The new route: **the positive cone of h_3(O) is an intrinsically curved
Riemannian symmetric space whose curvature is fixed by the cubic norm alone.**
A self-modeler is "along for the ride": its primitive idempotent E_11 picks a
spacetime slice (the Peirce V_0), and its off-center state (X != I/3, i.e.
rho_J > 0) picks a basepoint. Gravity is the curvature the slice inherits from
the bulk, sourced by the cubic norm's cross-terms coupling the spacetime
sector V_0 to the matter sectors V_1, V_{1/2}. No observers-make-gravity
ensemble argument (that is woo and is explicitly rejected); one observer, one
off-center point, and the algebra's own geometry does the rest.

**What is already SOLID (standard math, do not re-derive, cite):**
- The positive cone Omega = {X in h_3(O) : X positive} is a symmetric cone;
  its canonical metric is g_X = Hess(-log det X) (Faraut-Koranyi). The det=1
  hypersurface is the Riemannian symmetric space E_{6(-26)}/F_4 (26-dim).
- Primitive idempotents form the Cayley plane OP^2 = F_4/Spin(9) (16-dim).
- For the observer at E_11: Peirce decomposition h_3(O) = V_1(1) + V_{1/2}(16)
  + V_0(10), with V_0 = h_2(O). The complex sub-slice h_2(C_u) ~= R^{3,1} has
  det = the Minkowski quadratic form; its positive cone is the forward light
  cone; the det=1 hyperboloid is H^3 = SL(2,C)/SU(2). (Existing GPD work:
  `52-kkt-spacetime`, `52-observer-uniqueness`.)

**What is CONJECTURAL (the thing to prove or disprove):** that the curvature
the V_0 slice inherits from the bulk cubic-norm geometry is gravitational -
position-dependent and sourced by matter content in V_1/V_{1/2}.

## Conventions

```
jordan_product = (1/2)(XY + YX)        # XY = formal matrix mult w/ octonion mul
octonion_basis = fano, e1*e2 = e4      # match peirce_coupling.py
complex_structure u = e7               # h_2(C_u) sub-slice of h_2(O)
cubic_norm = Freudenthal det(X)        # WITH cross-terms; verify association
idempotent E_11 = diag(1,0,0)
Peirce: V_1 = (1,1) entry (1-dim, = R E_11)
        V_{1/2} = (1,2),(1,3) octonions (16-dim)
        V_0 = lower-right h_2(O) block (10-dim); spacetime slice = h_2(C_u) (4-dim)
cone metric g_X(A,B) = -d/ds d/dt log det(X + sA + tB)|_{s=t=0}   # = Hess(-log det)
center = I/3 (the F_4-symmetric point, rho_J = 0)
```

**CAUTION on the cubic norm cross-term.** Octonion non-associativity makes the
det cross-term association-sensitive; a prior bug (`trip_tracking.py`) coded
`2Re(x0(x1 x2))` where the correct term is `2Re(x2* x0* x1)`. Use the cubic
norm exactly as implemented in the corrected `h3o_tower.py` / verify against
`det = abc - a N(x) - b N(y) - c N(z) + 2 Re(triple)` with explicit
multiplicativity and Cayley-Hamilton checks before any geometry.

## The Claim

Fix E_11 and the slice V_0 (with its h_2(C_u) ~= R^{3,1} sub-slice). Build a
position-dependent metric on spacetime by restricting the bulk cone geometry:

  g_mu_nu(x) := the metric the h_3(O) cubic-norm geometry induces on the V_0
                slice at basepoint X_bg + x,

where x in V_0 is the spacetime point, X_bg = I/3 + M is the background, and
M ("matter") lies in V_1 + V_{1/2}. The background reduces to Minkowski
(eta_mu_nu, from h_2(C_u)'s own det per `52-kkt-spacetime`) when M = 0 and x is
at the center; write g_mu_nu(x) = eta_mu_nu + h_mu_nu(x). Then:

- **(A)** h_mu_nu(x) is genuinely position-dependent after fixing E_11 - NOT
  reducible to a fixed homogeneous metric by the residual symmetry
  Stab_{E_6}(E_11).
- **(B)** The curvature of g_mu_nu(x) is sourced by M: with M = 0 the slice is
  flat (or pure cosmological-constant); turning on M in V_1 + V_{1/2} produces
  Riemann curvature through the cubic-norm cross-terms coupling V_0 to
  V_1/V_{1/2}.
- **(C)** [strong form] The Einstein tensor G_mu_nu[g(x)] is proportional to a
  stress-energy T_mu_nu built from the V_1/V_{1/2} cross-term content.

## What To Prove

### Phase A: The homogeneity dealbreaker (DO THIS FIRST - it is cheap and it kills or greenlights everything)

**Sub-task A0 (signature bridge).** State precisely the map from the ambient
Riemannian cone-Hessian g_X = Hess(-log det) to a Lorentzian metric on the
h_2(C_u) slice. Two candidate constructions to test:
  (i) restrict g_X to V_0-tangent directions and Wick-rotate via the
      complex structure u (the C*-bottleneck / Phase 46 mechanism); or
  (ii) take the background Lorentzian eta from h_2(C_u)'s own det and let the
      h_3(O) cone-Hessian supply only the perturbation h_mu_nu.
Pick the one that reduces to exact Minkowski at (M=0, center) and report which.

**Theorem target A.** With E_11 fixed, compute h_mu_nu(x) explicitly (symbolic
or high-precision numeric expansion of g_X around X = I/3 in the V_0
directions). Decide:

  (a) Is h_mu_nu(x) constant in x (homogeneous), or does it genuinely vary
      with the spacetime point x?
  (b) Equivalently: does Stab_{E_6}(E_11) act transitively enough on basepoints
      to make all (basepoint, slice) pairs isometric? Compute
      dim Stab_{E_6}(E_11) and the dimension of the basepoint family modulo
      that stabilizer.

**KILL CONDITION:** if h_mu_nu(x) is x-independent (the slice carries one fixed
homogeneous metric, no position-dependent field), the route is DEAD. Report
"Phase A homogeneous - route dead" and STOP. Do not proceed to B/C.

### Phase B: Sourcing by matter

(Only if A shows genuine x-dependence.)

**Theorem target B.** Compute the Riemann tensor of g_mu_nu(x).
  (a) Confirm M = 0 gives R = 0 (flat) or R = const (pure Lambda).
  (b) Turn on M in V_1 + V_{1/2}. Show the curvature is generated by the
      det cross-terms 2Re(...) that couple V_0 to V_1/V_{1/2} - i.e. switching
      off the cross-terms (replacing det by the block-diagonal product
      det(V_1) * det(V_0)) removes the M-sourced curvature.
  (c) Quantify: relate the curvature scale to ||M|| and to rho_J(X_bg)
      (off-center-ness). Use `rho_directional_derivatives.py` for the
      expansion around I/3.

### Phase C: Einstein structure (strong form)

**Theorem target C.** Define a candidate stress-energy T_mu_nu from the
V_1/V_{1/2} cross-term content of M. Test whether
  G_mu_nu[g(x)] = kappa * T_mu_nu + Lambda * g_mu_nu
holds (a) exactly, (b) at linear order in M, or (c) not at all. Report the
honest level. "Curved but not Einstein-structured" is a real and acceptable
outcome - do not force it into Einstein form.

## Pass/Fail Summary

| Outcome | Verdict |
|---------|---------|
| Phase A homogeneous (h_mu_nu x-independent) | **KILL.** Route dead, stop. |
| A varies, B sourced by cross-terms | **SURVIVES:** matter curves the slice via the cubic norm (real, novel). |
| C: G_mu_nu ∝ T_mu_nu (exact or linearized) | **STRONG WIN:** gravity-from-bulk-geometry mechanism. |

## Reporting discipline

State which Phase A branch actually occurred without softening. A homogeneous
result is a clean, valuable KILL - report it as such, do not relabel it
"approximately position-dependent." A sourced-but-not-Einstein result (B yes,
C no) is the most likely real outcome; report it plainly. The point of the
task is to find out whether gravity is intrinsic to the h_3(O) bulk geometry,
not to confirm it.

## Build on (do not rebuild)

- `peirce_coupling.py` - h_3(K) for K = R,C,H,O, Jordan product, Peirce
  decomposition under E_11.
- `52-kkt-spacetime`, `52-observer-uniqueness` - h_2(C_u) ~= R^{3,1},
  Lorentzian signature from det, conformal algebra so(4,2).
- `rho_directional_derivatives.py` - directional derivatives / off-center
  expansion of rho_J around I/3.
- The corrected cubic norm (cross-term association verified).

## Stay distinct from (do not reuse as load-bearing)

- `paper6-continuum-limit-prompt.md` (lattice/Fisher route - abandoned).
- Derivations `47-*`,`48-*`,`49-*`,`50-*`,`53-*` (det/GST/Weinberg supergravity
  Lagrangian - circular, dead). We compute INTRINSIC cubic-norm curvature, not
  a posited supergravity action.

## Key references

- Faraut & Koranyi, *Analysis on Symmetric Cones* (1994) - the cone metric
  g_X = Hess(-log det), characteristic function, symmetric-space structure.
- Vinberg (1963), Koszul - canonical metric on a convex homogeneous cone.
- McCrimmon, *A Taste of Jordan Algebras* - Peirce decomposition, cubic norm,
  quadratic representation P(X).
- Baez, "The Octonions" (2002) - h_3(O), F_4, OP^2 = F_4/Spin(9).
- Gunaydin-Sierra-Townsend (1983-84) - very special geometry / magic
  supergravity scalar manifold E_{6(-26)}/F_4. **For the geometry only; we do
  NOT adopt their Lagrangian** (that is the dead route).
- (Contrast only, do not use:) Jacobson 1995 - Einstein equations as equation
  of state. The thermodynamic/ensemble route is explicitly rejected here.
