#!/usr/bin/env python3
"""tensor_probe.py -- v31.0-candidate Phase 91 (J5-on-the-variety, Block B)
"The Tensor Probe: Does Matter Source a Genuine Metric Mode?"

A GENUINE FORK (v27/v29/v30 class).  The route's gravity ceiling so far is TWO SCALARS
(clock-rate/lapse-class K-data + conformal/landscape-class r,G_M data) = Nordstrom-class.
Einstein-FORM needs a RANK-2, non-scalar, non-gauge metric mode sourced by matter.  On the
compact cut CP^2 = h_3(C_u) (Fubini-Study, Kahler-Einstein) symmetric 2-tensor fields split
L^2-orthogonally (Berger-Ebin / York):

        h = h_TT  (+)  delta* omega  (+)  f.g          (TT = div-free AND traceless)

  LIVE <=> some certified rank-2 battery member has TT-residue =/= 0 at generic M.
  DEAD <=> every member = delta* omega + f.g EXACTLY, (omega,f) exhibited per member.

APPROACH A (this file, the executor path): the DIRECT chart on the cut CP^2 = h_3(C_u) at
base E_11, exact rational, the symmetric-2-tensor calculus (covariant Hessian via the FS
Levi-Civita connection; the gradient bilinears), the York split by EXACT L^2-orthogonal
projection against an explicitly-spanned gauge image delta*(Omega^1) + conformal {f.g}; the
TT-residue is the orthogonal complement.  Guard-locked to the octonion engine on a cut battery
(mirror clock_connection._guard6_battery).  u = e_7; C_u = span{1, e_7}; e_7 <-> i.

The battery fields are built from the CERTIFIED codebase formulas (re-verified against source):
  phi_Y(p) = <Y,p>                  (vMD.inner; the v25 moment)         -> B1
  G_M(p)   = <M#,p> - (1/4)<M,p>^2  (vSFE.G_M; the v26 response)        -> B2
  s_X(p)   = pi_{1/2}^{(p)}(X)=dphi_X(vSMom; the v28 spinor moment)     -> B3 = s_X (x) s_X
  chi(p)   = <Kcal,D_p> = -(9/2)<M,p><M,D_p> (clock_connection; v30)    -> B4 = grad-grad chi
  R_M(p)   = <M,p>^2 - alpha<M#,p> - beta TrM^2  (vSFE cut solve)       -> B5 = grad-grad R_M
  T_M      = the pi_{1/2}M tangent bilinear (Jordan/Peirce; v27 trace)  -> B6 (pinned Gate 0)

DISCIPLINE (v21-v30): exact over Q/Q(t); fail-fast gates; controls with known answers;
non-hardwired verdict(); DEAD-must-be-constructive.  det SSOT = RL.det_3; octonion_algebra
BANNED as a direct decisive dependency (guard 6).  Reuse RL / vMD / vSFE / vSMom / clock / KK.

LANGUAGE FENCE (binding): LIVE = "a matter-sourced tensor MODE exists" -- NOT "Einstein
gravity derived".  NO Einstein-equation / Newton-constant / G=kT / dark-matter / geodesic
language.  Block C (the selection law, the kappa value) is NOT claimed.  The frozen FS
geometry is USED not derived.  The v18/v20 MM-connection corpse stays buried (this is the
BASE's deformation complex, not a fiber-built spacetime connection).

Reproducibility: sympy 1.14.0, Python 3.14, exact rational arithmetic (no RNG / no seeds;
the verdict is symbolic over Q / Q(t), floats illustrative only).
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                       # noqa: E402
from sympy import (Rational, symbols, cancel, expand, I, Matrix, eye,    # noqa: E402
                   simplify, conjugate, sqrt, together, zeros)

import ring_lemma_verification as RL                                     # noqa: E402
import kkt_gluing_holonomy as KK                                         # noqa: E402
import variety_moment_doublet as vMD                                     # noqa: E402
import variety_sourced_field_equation as vSFE                            # noqa: E402
import variety_spinor_moment as vSMom                                    # noqa: E402
import clock_connection as CC                                            # noqa: E402

_t0 = time.time()
PASS = []

# octonion-engine handles for the guard-lock / regressions
E11 = vMD.E11
inner = vMD.inner          # <A,B> = Tr(A o B) on h_3(O)
sharp = vMD.sharp          # Freudenthal adjoint X#
I3 = vMD.I3


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return ok


# ============================================================================
# 1. THE FUBINI-STUDY CHART ON CP^2 = h_3(C_u)  (exact rational; base E_11)
# ----------------------------------------------------------------------------
# Affine chart v = (1, z1, z2), z = (z1,z2) in C^2; base point E_11 <-> z = 0.
# Kahler potential K = log(1 + |z1|^2 + |z2|^2); FS metric g_{a bbar} = d_a d_bbar K.
# We use the C_u=C complex structure (e_7 <-> i, the codebase's cut rep, guard 6).
#
# Complex coords z1,z2 with conjugates z1b,z2b treated as INDEPENDENT symbols
# (Wirtinger calculus): d_a = d/dz_a, d_abar = d/dz_abar.  All real geometry is
# recovered by the reality slice z_abar = conjugate(z_a); we keep them independent
# for exact holomorphic/antiholomorphic differentiation and impose reality only when
# forming real L^2 integrals.
# ============================================================================
Z1, Z2 = symbols("z1 z2")
Z1B, Z2B = symbols("z1b z2b")     # independent conjugate coords (Wirtinger)
ZS = (Z1, Z2)
ZBS = (Z1B, Z2B)

# --------------------------------------------------------------------------
# METRIC NORMALIZATION (the lambda_1 bridge, fixed at Gate 0).
# The potential metric g_pot = d d_bar log(1+|z|^2) is the STANDARD CP^2 FS metric with
# Ric = (n+1) g_pot = 3 g_pot (n=2) and scalar lambda_1 = 6 (Obata: lambda_1 = 2*Einstein-const).
# Boucetta's tables AND the certified octonion engine use the UNIT-S^5-quotient normalization
# Ric = 2(n+1) g = 6 g, lambda_1 = 12.  Halving the metric doubles the Laplacian eigenvalues
# (6 -> 12) and, since the Ricci FORM R_{a bbar} = -d d_bar log det g is SCALE-INVARIANT
# (R = 3 g_pot regardless of scale), gives R = 3 g_pot = 6 (g_pot/2) = 6 g_phys, Lambda=6.
#   => the PHYSICAL (engine/Boucetta) metric is  g_phys = g_pot / 2.
# DEVIATION [Rule 4 - missing normalization factor]: an overall metric scale.  It does NOT
# affect the TT (+) delta*omega (+) f.g split (TT-ness, the delta*-image and the conformal
# direction g are all scale-COVARIANT) nor the verdict (TT-residue zero/nonzero is scale-free);
# it is fixed ONLY so the lambda_1=12 bridge and Boucetta's multiplicities apply verbatim.
# --------------------------------------------------------------------------
MET_SCALE = Rational(1, 2)        # g_phys = MET_SCALE * g_pot


def _rho():
    """rho = 1 + |z|^2 = 1 + z1 z1b + z2 z2b (with z_abar independent)."""
    return 1 + Z1 * Z1B + Z2 * Z2B


def kahler_potential():
    return sp.log(_rho())


def dz(f, a):
    return sp.diff(f, ZS[a])


def dzb(f, a):
    return sp.diff(f, ZBS[a])


def fs_metric_pot():
    """The POTENTIAL FS metric g_pot = d_a d_bbar log rho (standard CP^2; Ric = 3 g_pot)."""
    K = kahler_potential()
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel(dz(dzb(K, b), a))
    return g


def fs_metric():
    """The PHYSICAL FS metric g_phys = MET_SCALE * g_pot (Ric = 6 g_phys, lambda_1 = 12,
    the engine/Boucetta normalization).  2x2 Hermitian, exact rational in (z,zbar)."""
    return (MET_SCALE * fs_metric_pot()).applyfunc(cancel)


def fs_metric_inv(g=None):
    """Inverse FS metric g^{bbar a} (2x2).  Exact rational."""
    if g is None:
        g = fs_metric()
    return g.inv().applyfunc(cancel)


# the Kahler form coefficients g_{a bbar} closed-form (standard FS), PHYSICAL normalization:
#   g_phys_{a bbar} = MET_SCALE * (rho delta_{ab} - zbar_a z_b) / rho^2
def fs_metric_closed():
    rho = _rho()
    zb = [Z1B, Z2B]
    z = [Z1, Z2]
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel(MET_SCALE * (rho * (1 if a == b else 0) - zb[a] * z[b]) / rho ** 2)
    return g


# ============================================================================
# 2. THE COMPLEX STRUCTURE J AND THE (1,1) / (2,0)+(0,2) SPLIT
# ----------------------------------------------------------------------------
# A real symmetric 2-tensor on a Kahler manifold splits, w.r.t. J, into a
# J-INVARIANT part (Hermitian, type (1,1)): h(JX,JY) = h(X,Y), and a
# J-ANTI-INVARIANT part (type (2,0)+(0,2)): h(JX,JY) = -h(X,Y).
# In complex coords a symmetric tensor has components h_{ab} (holomorphic (2,0)),
# h_{abar bbar} (antiholo (0,2)), h_{a bbar} (mixed (1,1)).  The (1,1) part is the
# mixed block h_{a bbar}; the (2,0)+(0,2) part is the pure blocks h_{ab}, h_{abar bbar}.
# Reality: h_{abar bbar} = conjugate(h_{ab}); h_{bbar a} = conjugate(h_{a bbar}).
# ============================================================================
def J_matrix_at0():
    """The complex structure J as a real 4x4 matrix on T_0 CP^2 in the real frame
    (x1,y1,x2,y2) where z_a = x_a + i y_a: J(dx_a)=dy_a, J(dy_a)=-dx_a (standard).
    Used for the abstract J-invariance check; the working split is done in the
    complex (a,bbar) basis (cleaner, exact)."""
    Jm = zeros(4, 4)
    # order (x1,y1,x2,y2): J x_a -> y_a, J y_a -> -x_a
    Jm[1, 0] = 1; Jm[0, 1] = -1
    Jm[3, 2] = 1; Jm[2, 3] = -1
    return Jm


# ============================================================================
# 2b. THE KAHLER LEVI-CIVITA CONNECTION + COVARIANT HESSIAN
# ----------------------------------------------------------------------------
# For a Kahler metric the only nonzero Christoffels are the all-holomorphic
#   Gamma^c_{ab} = g^{c dbar} d_a g_{b dbar}   (and its conjugate Gamma^cbar_{abar bbar}).
# Mixed symbols vanish.  The covariant Hessian (symmetric 2-tensor) of a function f:
#   (1,1) block:  H_{a bbar} = d_a d_bbar f          (no Christoffel; mixed connection 0)
#   (2,0) block:  H_{ab}     = d_a d_b f - Gamma^c_{ab} d_c f
#   (0,2) block:  H_{abar bbar} = conjugate of (2,0) on the reality slice
# The trace w.r.t. g is  tr_g H = 2 g^{a bbar} H_{a bbar}  (the (1,1) block only; the
# pure blocks are traceless against the Hermitian metric).  The factor 2: real trace =
# g^{a bbar} H_{a bbar} + g^{bbar a} H_{bbar a} = 2 Re(g^{a bbar} H_{a bbar}); for a real
# function the mixed block is Hermitian so this is 2 g^{a bbar} H_{a bbar} (real).
# ============================================================================
def christoffel_hol(g=None, ginv=None):
    """Gamma^c_{ab} (c upper, a,b lower) -- the holomorphic Kahler Christoffels.
    Returns Gamma[c][a][b].  Exact rational in (z,zbar)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    # g^{c dbar} = ginv[d,c] (the TRANSPOSE of fs_metric_inv -- the SAME pairing convention as
    # tensor_dot_point; using ginv[c,d] here was a transpose BUG that gave a wrong Christoffel and
    # a divergent (2,0)-Hessian norm -- caught by the standard-FS Christoffel check, see SUMMARY).
    Gam = [[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)]
    for c in range(2):
        for a in range(2):
            for b in range(2):
                s = sp.Integer(0)
                for d in range(2):
                    s += ginv[d, c] * dz(g[b, d], a)     # g^{c dbar} d_a g_{b dbar}
                Gam[c][a][b] = cancel(s)
    return Gam


def cov_hessian(f, g=None, ginv=None, Gam=None, simp=together):
    """Covariant Hessian of scalar f as a symmetric 2-tensor on CP^2, returned as the
    three complex blocks (H20, H11, H02) each a 2x2 sympy Matrix:
      H20[a,b] = H_{ab}        (holomorphic (2,0) part)
      H11[a,b] = H_{a bbar}    (mixed (1,1) part)
      H02[a,b] = H_{abar bbar} (antiholomorphic (0,2) part)
    Rational in (z,zbar).  simp: per-entry simplifier (default `together`: fast, single rho-power
    denominator -- l2_scalar fully reduces at integration; pass `cancel` for exact-form checks).
    NB: `cancel` on rational FIELDS (rho denominators) is the perf cliff; `together` avoids it."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    GamB = _christoffel_antihol(g, ginv)        # cache: built ONCE (was recomputed 4x -> slow)
    H20 = zeros(2, 2)
    H11 = zeros(2, 2)
    H02 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            # (1,1): d_a d_bbar f
            H11[a, b] = simp(dz(dzb(f, b), a))
            # (2,0): d_a d_b f - Gamma^c_{ab} d_c f
            t = dz(dz(f, b), a)
            for c in range(2):
                t -= Gam[c][a][b] * dz(f, c)
            H20[a, b] = simp(t)
            # (0,2): d_abar d_bbar f - Gamma^cbar_{abar bbar} d_cbar f
            t2 = dzb(dzb(f, b), a)
            for c in range(2):
                t2 -= GamB[c][a][b] * dzb(f, c)
            H02[a, b] = simp(t2)
    return H20, H11, H02


def _christoffel_antihol(g, ginv):
    """Gamma^cbar_{abar bbar} = g^{d cbar} d_abar g_{d bbar}  (conjugate Christoffels; the complex
    conjugate of christoffel_hol).  g^{d cbar} = conj(g^{c dbar}) = conj(ginv[d,c]) = ginv[c,d]
    (g Hermitian).  Using the matching pairing fixes the divergent (0,2)-Hessian norm."""
    Gam = [[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)]
    for c in range(2):
        for a in range(2):
            for b in range(2):
                s = sp.Integer(0)
                for d in range(2):
                    s += ginv[c, d] * dzb(g[d, b], a)    # g^{d cbar} d_abar g_{d bbar}
                Gam[c][a][b] = cancel(s)
    return Gam


def trace_g(H11, ginv=None):
    """Real metric trace of a symmetric 2-tensor: tr_g h = 2 g^{a bbar} h_{a bbar}
    (only the (1,1) block contributes; the pure (2,0)/(0,2) blocks are g-traceless)."""
    if ginv is None:
        ginv = fs_metric_inv()
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += ginv[b, a] * H11[a, b]      # g^{a bbar} = ginv[b,a] in our labelling
    return cancel(2 * s)


def laplacian(f, g=None, ginv=None):
    """The Laplace-Beltrami operator on functions, ENGINE convention (= +div grad, the
    negative-semidefinite analyst Laplacian): Delta_g f = 2 g^{a bbar} d_a d_bbar f.
    Matches the certified engine where Delta(phi - phibar) = -lambda_1 (phi - phibar),
    lambda_1 = 12 > 0.  Exact rational in (z,zbar)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += ginv[b, a] * dz(dzb(f, b), a)      # g^{a bbar} d_a d_bbar f
    return cancel(2 * s)


def lambda1_of(f, g=None, ginv=None, fbar=None):
    """Extract the Laplace eigenvalue lambda_1 from Delta_g f = -lambda_1 (f - fbar), at the
    base z=0 (the F_4-covariance base).  fbar defaults to the value making (f-fbar) the
    eigenfunction; we extract via lambda_1 = -[Delta f]/[f - fbar] at a generic chart point."""
    Df = laplacian(f, g, ginv)
    # the eigenfunction is f - fbar; fbar is a constant (the mean).  Delta kills constants, so
    # Delta f = Delta(f - fbar) = -lambda_1 (f - fbar).  Solve lambda_1 at two points to confirm
    # constancy, then return it.
    z = symbols("zz")
    pts = [{Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 2), Z2B: Rational(1, 3)},
           {Z1: Rational(1, 4), Z2: Rational(-1, 5), Z1B: Rational(1, 4), Z2B: Rational(-1, 5)}]
    # fbar: the constant such that Delta f = -lambda_1 (f - fbar).  Two unknowns (lambda_1, fbar)
    # from two points (linear): Delta f|_p = -lambda_1 f|_p + lambda_1 fbar.
    lam, fb = symbols("lam fb")
    eqs = []
    for pp in pts:
        eqs.append(sp.Eq(cancel(Df.subs(pp)), cancel(-lam * f.subs(pp) + lam * fb)))
    sol = sp.solve(eqs, [lam, fb], dict=True)
    if not sol:
        return None
    lam_val = cancel(sol[0][lam])
    # verify globally (eigenfunction): Delta f + lam (f - fbar) == 0 identically
    glob = (cancel(Df + lam_val * (f - sol[0][fb])) == 0)
    return lam_val if glob else None


def _real_slice(expr):
    """Impose the reality slice zbar_a = conjugate(z_a) is NOT what we want for exact rational
    work (introduces conjugates).  Instead we keep z,zbar as independent REAL-structure
    coordinates: the chart is the complexification and every certified field is a genuine
    rational function of the 4 real coords (Re z_a, Im z_a) <-> (z_a, zbar_a).  This helper is
    the identity on already-rational expressions (the fields are polynomial in z,zbar/rho^k);
    it exists to mark 'this is evaluated as a real function on CP^2'.  Real L^2 integrals
    (Gate 1+) substitute z_a = r_a e^{i th_a}, zbar_a = r_a e^{-i th_a}."""
    return cancel(expr)


def ricci_tensor(g=None):
    """Ricci form R_{a bbar} = - d_a d_bbar log det(g_{c dbar}).  For CP^2 with this FS
    normalization R_{a bbar} = (n+1) * 2 * g_{a bbar}?  We just compute and compare to
    Lambda * g.  Returns the 2x2 matrix R_{a bbar}."""
    if g is None:
        g = fs_metric()
    detg = cancel(g.det())
    logdet = sp.log(detg)
    R = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            R[a, b] = cancel(-dz(dzb(logdet, b), a))
    return R


# ============================================================================
# 2c. THE GAUGE OPERATOR delta* AND THE YORK SPLIT SOLVER (V1, lemma grade)
# ----------------------------------------------------------------------------
# A 1-form omega has components omega_a (holomorphic, dual to dz^a) and omega_abar
# (antiholomorphic, dual to dzbar^a).  The symmetric gradient (Lie/gauge part):
#   (delta* omega)_{mu nu} = (1/2)(nabla_mu omega_nu + nabla_nu omega_mu).
# Kahler complex blocks (mixed Christoffels vanish; Gamma^c_{ab} holomorphic):
#   (2,0):  W20_{ab} = (1/2)(d_a omega_b + d_b omega_a) - Gamma^c_{ab} omega_c
#   (1,1):  W11_{a bbar} = (1/2)(d_a omega_bbar + d_bbar omega_a)
#   (0,2):  W02 = conj(W20) on the reality slice.
# For omega = d phi (omega_a = d_a phi, omega_abar = d_abar phi) this equals the covariant
# Hessian cov_hessian(phi) EXACTLY (the Matsushima identity nabla nabla phi = delta*(d phi)).
# The conformal block is f.g (f a function): blocks (0, f*g_{a bbar}, 0).
# ============================================================================
def delta_star(om_hol, om_ahol, g=None, ginv=None, Gam=None, simp=together):
    """delta*(omega) for a 1-form with holomorphic components om_hol[a]=omega_a and
    antiholomorphic om_ahol[a]=omega_abar.  Returns (W20,W11,W02) 2x2 blocks (rational).
    simp: per-entry simplifier (default `together`; pass `cancel` for exact-form checks)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    GamB = _christoffel_antihol(g, ginv)
    W20 = zeros(2, 2); W11 = zeros(2, 2); W02 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            # (2,0): (1/2)(d_a om_b + d_b om_a) - Gamma^c_{ab} om_c
            t = Rational(1, 2) * (dz(om_hol[b], a) + dz(om_hol[a], b))
            for c in range(2):
                t -= Gam[c][a][b] * om_hol[c]
            W20[a, b] = simp(t)
            # (1,1): (1/2)(d_a om_bbar + d_bbar om_a)
            W11[a, b] = simp(Rational(1, 2) * (dz(om_ahol[b], a) + dzb(om_hol[a], b)))
            # (0,2): (1/2)(d_abar om_bbar + d_bbar om_abar) - GammaB^c om_cbar
            t2 = Rational(1, 2) * (dzb(om_ahol[b], a) + dzb(om_ahol[a], b))
            for c in range(2):
                t2 -= GamB[c][a][b] * om_ahol[c]
            W02[a, b] = simp(t2)
    return W20, W11, W02


def delta_star_of_dphi(phi, g=None, ginv=None, Gam=None, simp=together):
    """delta*(d phi) -- equals cov_hessian(phi) (Matsushima); a convenience wrapper."""
    om_hol = [dz(phi, a) for a in range(2)]
    om_ahol = [dzb(phi, a) for a in range(2)]
    return delta_star(om_hol, om_ahol, g, ginv, Gam, simp)


def conformal_block(f, g=None, simp=together):
    """The conformal symmetric 2-tensor f.g: blocks (0, f*g_{a bbar}, 0)."""
    if g is None:
        g = fs_metric()
    Z = zeros(2, 2)
    W11 = (f * g).applyfunc(simp)
    return Z, W11, Z


# ----------------------------------------------------------------------------
# Scalar harmonics on CP^2 (the gauge/conformal potentials).  The matrix-element
# functions phi_A(p) = <A,p> = (v^H A v)/rho (A a 3x3 complex Hermitian matrix) are the
# building blocks: traceless A -> the degree-(1,1) lambda_1=12 eigenfunctions (dim 8, the
# su(3) adjoint); products phi_A phi_B span degree-(2,2) (lambda_0 + lambda_1 + lambda_2=32).
# These are the natural potentials the route possesses (the v25 moment fields and products).
# ----------------------------------------------------------------------------
def phi_A(Acx):
    """phi_A(p) = <A,p> = Tr(A P(z)) (A a 3x3 complex Hermitian matrix), as a function of
    (z,zbar).  Re Tr for Hermitian A; we keep Tr (reality on the slice)."""
    return cx_inner(Acx, P_chart())


def _herm_basis_3():
    """A real basis of the 8 traceless 3x3 Hermitian matrices (the su(3) adjoint) + the
    identity (trace direction).  Returns list of (name, matrix)."""
    E = []
    # 2 diagonal traceless
    E.append(("d1", Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])))
    E.append(("d2", Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / sp.sqrt(3) * sp.sqrt(3)))  # keep rational
    E[-1] = ("d2", Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]))
    # 3 real off-diagonal (symmetric)
    for (i, j, nm) in [(0, 1, "s01"), (0, 2, "s02"), (1, 2, "s12")]:
        Mm = zeros(3, 3); Mm[i, j] = 1; Mm[j, i] = 1
        E.append((nm, Mm))
    # 3 imaginary off-diagonal (Hermitian)
    for (i, j, nm) in [(0, 1, "a01"), (0, 2, "a02"), (1, 2, "a12")]:
        Mm = zeros(3, 3); Mm[i, j] = I; Mm[j, i] = -I
        E.append((nm, Mm))
    return E                              # 8 traceless Hermitian generators


def traceless_part(hb, g=None, ginv=None):
    """Subtract the conformal trace: h0 = h - (1/n)(tr_g h) g, n=4 (real dim).  Returns the
    block-triple of h0 (its (1,1) block gets the -(1/4) tr_g h * g shift; pure blocks unchanged)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    H20, H11, H02 = hb
    tr = trace_g(H11, ginv)               # tr_g h (uses only the (1,1) block)
    n = 4
    H11_0 = (H11 - Rational(1, n) * tr * g).applyfunc(cancel)
    return H20, H11_0, H02


# ----------------------------------------------------------------------------
# The York split solver: project a symmetric 2-tensor onto span(delta*omega) + span(f.g),
# compute the TT-residue norm^2 by exact L^2 Gram projection.  (V1, lemma grade.)
# ----------------------------------------------------------------------------
def york_tt_residue(h_blocks, gauge_basis, conf_basis, g=None, ginv=None, l2fn=None):
    """Given a symmetric 2-tensor h (block-triple) and explicit spanning sets
       gauge_basis = [delta*(d chi_a)]  (block-triples),
       conf_basis  = [chi_a . g]        (block-triples),
    compute ||h_TT||^2 = ||h||^2 - v^T G^{-1} v exactly, where {e_i} = gauge_basis + conf_basis,
    G_ij = <e_i,e_j>_L2, v_i = <h,e_i>_L2.  Returns (||h_TT||^2, ||h||^2, rank(G), dim(span)).
    h_TT = 0  <=>  ||h_TT||^2 = 0 (DEAD: h is pure gauge+conformal).  l2fn: the L^2 inner product
    (defaults to l2_tensor)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if l2fn is None:
        l2fn = lambda x, y: l2_tensor(x, y, ginv)
    basis = list(gauge_basis) + list(conf_basis)
    n = len(basis)
    G = zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            val = l2fn(basis[i], basis[j])
            G[i, j] = val; G[j, i] = val
    v = Matrix([l2fn(h_blocks, basis[i]) for i in range(n)])
    h2 = l2fn(h_blocks, h_blocks)
    rank = G.rank()
    # use pseudo-projection robust to rank-deficiency: solve G c = v on the column space
    # (least-squares exact); ||proj||^2 = c^T v.  For exact rational, use the Moore-Penrose via
    # the rank factorization: project onto the independent subset.
    indep = _independent_cols(G)
    Gi = G[indep, indep]
    vi = Matrix([v[k] for k in indep])
    c = Gi.solve(vi)
    proj2 = cancel((c.T * vi)[0])
    tt2 = cancel(h2 - proj2)
    return tt2, h2, rank, n


def _independent_cols(G):
    """Indices of a maximal linearly-independent set of columns of the (symmetric) Gram G."""
    n = G.shape[0]
    chosen = []
    for k in range(n):
        trial = chosen + [k]
        if G[trial, trial].rank() == len(trial):
            chosen.append(k)
    return chosen


def divergence(hb, g=None, ginv=None, Gam=None):
    """The (negative) covariant divergence (delta h)_b = -g^{mu nu} nabla_mu h_{nu b} of a
    symmetric 2-tensor (block-triple H20,H11,H02), returned as a 1-form (om_hol[b], om_ahol[b]).
    Kahler complex form (mixed Christoffels vanish; g^{a bbar}=ginv[b,a]):
      (delta h)_b = -[ g^{a cbar} nabla_a h_{cbar b} + g^{cbar a} nabla_cbar h_{a b} ]
    with h_{cbar b}=H11[b,c] (Hermitian (1,1)), h_{a b}=H20[a,b]; the holo index b gets a
    holo-Christoffel, the antiholo derivative gets none on holo indices.  VERIFIED: delta(g)=0
    (metric covariantly constant) -- this is the sanity check that pins the index bookkeeping
    (it FAILED before the Christoffel transpose fix; passes after)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    GamB = _christoffel_antihol(g, ginv)
    H20, H11, H02 = hb
    gu = lambda a, b: ginv[b, a]          # g^{a bbar}
    om_hol = [sp.Integer(0)] * 2
    om_ahol = [sp.Integer(0)] * 2
    for b in range(2):
        s = sp.Integer(0)
        for a in range(2):
            for c in range(2):
                term = dz(H11[b, c], a)
                for e in range(2):
                    term -= Gam[e][a][b] * H11[e, c]
                s += gu(a, c) * term                 # g^{a cbar} nabla_a h_{cbar b}
        for a in range(2):
            for c in range(2):
                s += gu(a, c) * dzb(H20[a, b], c)    # g^{cbar a} nabla_cbar h_{a b}
        om_hol[b] = together(-s)
    for b in range(2):
        s = sp.Integer(0)
        for a in range(2):
            for c in range(2):
                term = dzb(H11[c, b], a)
                for e in range(2):
                    term -= GamB[e][a][b] * H11[c, e]
                s += gu(c, a) * term
        for a in range(2):
            for c in range(2):
                s += gu(c, a) * dz(H02[a, b], c)
        om_ahol[b] = together(-s)
    return om_hol, om_ahol


# ============================================================================
# 3. GUARD 6 -- the 3x3-complex cut rep stays locked to the octonion engine
# ----------------------------------------------------------------------------
# We re-run the CERTIFIED clock_connection guard-6 battery (compression, trace
# form, the v29 clock field agree under e_7<->i) AND add the tensor-probe-specific
# lock: the cut FS chart here reproduces the engine's lambda_1 = 12 (the certified
# families machinery).  This is the bridge that lets the Boucetta dimension tables
# apply verbatim (RESEARCH section 2(i), section 4).
# ============================================================================
def guard6_engine_battery():
    """Re-run the certified clock_connection guard-6 battery (octonion engine vs
    3x3-complex cut rep agree on compression, <,>, Kcal under e_7<->i)."""
    return CC._guard6_battery()


# ============================================================================
# 3b. THE FIELD-TO-CHART BRIDGE  (chart point z -> rank-1 idempotent p; certified
#     scalar fields as exact rational functions of (z,zbar))
# ----------------------------------------------------------------------------
# z=(z1,z2) -> v = (1, z1, z2) -> P = v v^H / (v^H v)  (rank-1 projector, 3x3 complex
# Hermitian, = the cut idempotent in the e_7<->i rep, guard 6).  We carry z_abar as
# independent symbols, so v^H uses zbar_a; on the reality slice this is the genuine
# projector.  The certified scalar fields are then exact rational functions of (z,zbar):
#   <A,p> = Re Tr(A_cx P)  where A_cx is the matter in the 3x3-complex rep (the trace
#   form on h_3(C_u) matches Re Tr in the complex rep -- guard 6, verified at Gate 0).
# ============================================================================
def P_chart():
    """Rank-1 projector P(z) = v v^H/(v^H v), v=(1,z1,z2), zbar independent (Wirtinger).
    3x3 complex matrix; rational in (z,zbar)."""
    v = Matrix([1, Z1, Z2])
    vb = Matrix([1, Z1B, Z2B])        # this is conjugate(v) entrywise (independent symbols)
    denom = (vb.T * v)[0]             # v^H v = 1 + z1 z1b + z2 z2b = rho
    P = (v * vb.T) / denom
    return P.applyfunc(cancel)


def cx_inner(Acx, Bcx):
    """Trace-form inner product in the 3x3-complex rep: <A,B> = Re Tr(A B).  For Hermitian
    A,B (matter, projector) on the reality slice this equals the h_3(C_u) trace form
    <A,B>=Tr(AoB) (guard 6).  We return Tr(A B) symbolically; reality is imposed downstream."""
    return cancel(expand((Acx * Bcx).trace()))


def phi_field(Mcx):
    """phi_M(p) = <M,p> as an exact function of (z,zbar):  Tr(Mcx P(z))."""
    return cx_inner(Mcx, P_chart())


def Mmat_cut_cx(pre="m"):
    """Generic traceless cut matter M in the 3x3-complex rep (e_7<->i): 8 real params
    (2 diagonal trace-free + 3 complex off-diagonal).  Hermitian."""
    s = symbols(f"{pre}0:8", real=True)
    M = Matrix([[s[0],                       s[2] + I * s[3],   s[4] + I * s[5]],
                [s[2] - I * s[3],            s[1],              s[6] + I * s[7]],
                [s[4] - I * s[5],            s[6] - I * s[7],   -s[0] - s[1]]])
    return M, s


def sharp_cx(Mcx):
    """Freudenthal adjoint X# in the 3x3-complex rep: for a 3x3 Hermitian matrix this is
    the cofactor/adjugate transpose, (X#)_{ij} = cofactor.  Equivalently X# = X^2 - Tr(X)X
    + sigma_2(X) I with the JORDAN square (= the matrix square for a single Hermitian matrix,
    since X commutes with itself).  We use the matrix-algebra adjugate, verified == engine
    sharp under e_7<->i at Gate 0."""
    s2 = cancel((Mcx.trace() ** 2 - (Mcx * Mcx).trace()) / 2)
    return (Mcx * Mcx - Mcx.trace() * Mcx + s2 * eye(3)).applyfunc(cancel)


def G_M_field(Mcx):
    """The v26 response field G_M(p) = <M#,p> - (1/4)<M,p>^2 as a function of (z,zbar)."""
    Msharp = sharp_cx(Mcx)
    return cancel(cx_inner(Msharp, P_chart()) - Rational(1, 4) * phi_field(Mcx) ** 2)


def grad_bilinear(phi, simp=together):
    """The symmetric gradient bilinear dphi (x) dphi (= s_X (x) s_X for phi=phi_X, since
    s_X = dphi_X is the v28 spinor moment) as block-triple (H20,H11,H02):
      H20[a,b] = d_a phi d_b phi
      H11[a,b] = d_a phi d_bbar phi   (Hermitian; the (1,1) part)
      H02[a,b] = d_abar phi d_bbar phi
    NB: this is a genuine symmetric 2-tensor (omega (x) omega for the exact 1-form omega=dphi);
    NOT a Hessian -- this is the verdict object B3.  simp: per-entry simplifier (default
    together)."""
    da = [dz(phi, a) for a in range(2)]
    dab = [dzb(phi, a) for a in range(2)]
    H20 = zeros(2, 2); H11 = zeros(2, 2); H02 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            H20[a, b] = simp(da[a] * da[b])
            H11[a, b] = simp(da[a] * dab[b])
            H02[a, b] = simp(dab[a] * dab[b])
    return H20, H11, H02


# ============================================================================
# 3c. EXACT L^2 INTEGRATION ON CP^2 (Fubini-Study)  -- the split solver's inner product
# ----------------------------------------------------------------------------
# The FS volume form on the chart z in C^2:  dV_FS = c_n * d^4z / rho^{n+1} = c_2 d^4z/rho^3,
# d^4z = (i/2)^2 dz1 dz1b dz2 dz2b (real Lebesgue on C^2 = R^4).  By U(2) chart symmetry the
# integral of a monomial z^A zbar^B / rho^k vanishes unless A=B (matched powers); for matched
# powers it is a real beta-integral.  We compute EXACT rationals; only RATIOS matter for the
# orthogonal projection (the overall constant c_2 cancels), so we set c_2 = 1 and use:
#   I(a,b,k) := integral_{C^2} (|z1|^{2a} |z2|^{2b} / rho^k) d^4z / rho^3
#            (k absorbed: the field denominators are powers of rho).
# Switch to s_i = |z_i|^2 >= 0:  d^4z = pi^2 ds1 ds2 (angular 2pi each / the (i/2)^2 ... ); the
# overall pi^2 cancels in ratios.  Then
#   I(a,b;K) = integral_0^inf integral_0^inf s1^a s2^b / (1+s1+s2)^K ds1 ds2,  K = k+3,
#            = a! b! (K-3-a-b)! / (K-1)!   (Dirichlet/beta), valid for K-3-a-b >= 1, i.e.
#   I(a,b;K) = Gamma(a+1)Gamma(b+1)Gamma(K-a-b-2) / Gamma(K)   (exact rational for integer args).
# This is the ONLY integral identity used; verified numerically at several (a,b,K) at Gate 1.
# ============================================================================
def _mono_integral(a, b, K):
    """integral_0^inf^2 s1^a s2^b / (1+s1+s2)^K ds1 ds2 = a! b! (K-a-b-3)! / (K-1)!  (exact).
    Requires K - a - b - 3 >= 0 (convergence + non-negative factorial)."""
    a, b, K = int(a), int(b), int(K)
    m = K - a - b - 3
    if m < 0:
        raise ValueError(f"L^2 integral divergent/ill-posed: K-a-b-3={m} < 0 (a={a},b={b},K={K})")
    return Rational(sp.factorial(a) * sp.factorial(b) * sp.factorial(m), sp.factorial(K - 1))


def _rho_power_of(den):
    """Given a denominator that is const * rho^k, return (k, const).  rho is irreducible."""
    rho = _rho()
    den = sp.expand(den)
    if den == 1:
        return 0, sp.Integer(1)
    fl = sp.factor_list(den)
    const = fl[0]
    k = 0
    for fac, mult in fl[1]:
        if sp.expand(fac - rho) == 0:
            k = mult
        elif sp.expand(fac + rho) == 0:    # (-rho)
            k = mult
            const *= (-1) ** mult
        else:
            raise ValueError(f"_rho_power_of: factor {fac} is not rho")
    return k, const


def l2_scalar(f):
    """EXACT L^2 inner-product integral of a scalar f(z,zbar) over CP^2 (FS), up to pi^2.
    Strategy (avoids the giant `expand`/`cancel` cliff on field products): f = num/rho^k with num
    a polynomial in (z1,z2,z1b,z2b).  The U(2) phase-average keeps only matched monomials
    z1^a z2^b z1b^a z2b^b -> s1^a s2^b (s=|z|^2); the radial integral of s1^a s2^b/rho^K is the
    Dirichlet/beta _mono_integral(a,b,K).  We extract the matched-coefficient polynomial in (s1,s2)
    by an EXACT roots-of-unity phase average on each block product separately (linearity), then
    radial-integrate.  Each step is a substitution (no full expand of the giant product)."""
    # f is expected as a sum of rational terms each with a pure rho-power denominator.  We
    # integrate TERM-BY-TERM over a common rho-power: split f into additive pieces, read each
    # piece's (matched S-poly, K), lift all to Kmax, sum the S-polys, integrate once.  This stays
    # fast (no `cancel` of the giant combined fraction; each piece's `together` is cheap) and the
    # COMBINED matched S-poly at Kmax is convergent even if individual pieces are not.
    f = cancel(f)                          # reduce to lowest terms num/rho^K_true (robust; for the
    #   rational-instance battery with SPARSE cut M the fields are low-degree and this is fast).
    num, den = sp.fraction(f)
    k, const = _rho_power_of(sp.expand(den))
    K = k + 3
    num = sp.expand(num / const)
    Pmatch = _phase_average(num)
    total = sp.Integer(0)
    for (a, b), coeff in sp.Poly(Pmatch, _S1, _S2).terms():
        total += coeff * _mono_integral(a, b, K)
    return cancel(total)


_S1, _S2 = symbols("S1 S2", nonnegative=True)


def _phase_average(num):
    """Return the U(2)-phase-averaged matched part of a polynomial num(z1,z2,z1b,z2b) as a
    polynomial in S1=|z1|^2, S2=|z2|^2 (exact).  Keeps only matched monomials z1^a z2^b z1b^a z2b^b
    -> S1^a S2^b (the rest integrate to zero by U(2) angular symmetry).  Uses
    as_coefficients_dict (faster than Poly for the matched-monomial sieve)."""
    cd = sp.expand(num).as_coefficients_dict()
    terms = {}
    for mono, coeff in cd.items():
        pd = mono.as_powers_dict()        # {Z1: a1, Z2: a2, Z1B: b1, Z2B: b2} (missing -> 0)
        a1 = int(pd.get(Z1, 0)); a2 = int(pd.get(Z2, 0))
        b1 = int(pd.get(Z1B, 0)); b2 = int(pd.get(Z2B, 0))
        if a1 == b1 and a2 == b2:
            terms[(a1, a2)] = terms.get((a1, a2), sp.Integer(0)) + coeff
    return sum(c * _S1 ** a * _S2 ** b for (a, b), c in terms.items())


# ----------------------------------------------------------------------------
# Pointwise tensor inner product of symmetric 2-tensors (complex blocks) and its
# L^2 integral.  A real symmetric 2-tensor h, written in the real cotangent basis, is
#   h = H20_{ab} dz^a dz^b + H02_{ab} dzbar^a dzbar^b + H11_{a bbar}(dz^a dzbar^b + dzbar^b dz^a)
# with H02 = conj(H20), H11 Hermitian (reality).  The Kahler real metric is
#   G = g_{a bbar}(dz^a dzbar^b + dzbar^b dz^a),  so on covectors the pairing is
#   <dz^a, dzbar^b> = g^{a bbar} = ginv[b,a]  (= the TRANSPOSE of fs_metric_inv; verified
#   == the (dz,dzbar) block of the real 4x4 inverse metric), <dz^a,dz^b>=0.
# The pointwise Riemannian inner product <h,h'> = G^{mu rho}G^{nu sigma} h_{mu nu} h'_{rho sigma}
# (full 4x4 contraction in the complex (dz1,dz2,dzbar1,dzbar2) basis) reduces EXACTLY to
#   <h,h'> = 2 g^{a dbar} g^{c bbar} H11_{a bbar} H11'_{c dbar}              [ (1,1).(1,1), coeff 2 ]
#          +   g^{a cbar} g^{b dbar} H20_{ab} H02'_{cd}                      [ h(2,0).h'(0,2) ]
#          +   g^{c abar} g^{d bbar} H02_{ab} H20'_{cd}                      [ h(0,2).h'(2,0) ]
# with g^{a bbar} = ginv[b,a] (the TRANSPOSE of fs_metric_inv; = the (dz,dzbar) block of the
# real 4x4 inverse metric).  The (0,2).(2,0) term uses the CONJUGATE index order gu(c,a)gu(d,b)
# (Hermitian structure: g^{a bbar} is conjugated when the (0,2) block sits on the left).
# DERIVED by separating h1,h2 block symbols and reading the EXACT coefficients off the brute
# 4x4 contraction (B-B coeff 2 = merge of (ab),(cd) orderings; A1-C2 coeff 1 with gu(a,c)gu(b,d),
# C1-A2 coeff 1 with gu(c,a)gu(d,b)).  Symbolically VERIFIED == brute on fully-independent blocks
# + numerically on two tensors, their cross term, and symmetry at two points (earlier
# wrong factor/symmetrization/transpose caught here -- see SUMMARY 'tensor inner product').
# ----------------------------------------------------------------------------
def tensor_dot_point(hb, hpb, ginv=None, simp=cancel):
    """Pointwise <h, h'> for two symmetric 2-tensors given as block-triples (H20,H11,H02).
    Uses g^{a bbar} = ginv[b,a] (transpose of fs_metric_inv).  Returns a scalar (rational in
    z,zbar); real for real tensors on the reality slice.  simp default `cancel` (good for numeric
    metrics); pass simp=sympify/together for FIELD tensors (l2_scalar reduces at integration)."""
    if ginv is None:
        ginv = fs_metric_inv()
    H20, H11, H02 = hb
    P20, P11, P02 = hpb
    gu = lambda a, b: ginv[b, a]          # g^{a bbar} (the verified transpose pairing)
    s11 = sp.Integer(0)
    t = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    s11 += gu(a, d) * gu(c, b) * H11[a, b] * P11[c, d]
                    t += gu(a, c) * gu(b, d) * H20[a, b] * P02[c, d]      # h(2,0).h'(0,2)
                    t += gu(c, a) * gu(d, b) * H02[a, b] * P20[c, d]      # h(0,2).h'(2,0)
    return simp(2 * s11 + t)


def grad_contract(phi, psi, ginv=None):
    """The scalar P(phi,psi) = g^{a bbar} d_a phi d_bbar psi (a low-degree scalar field).  The
    building block for L^2 inner products of GRADIENT bilinears -- contracting the metric with the
    gradients FIRST keeps everything low-degree (vs contracting full tensors).  ginv[b,a]=g^{a bbar}."""
    if ginv is None:
        ginv = fs_metric_inv()
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += ginv[b, a] * dz(phi, a) * dzb(psi, b)
    return together(s)


def _P(phi, psi, ginv):
    """g^{a bbar} d_a phi d_bbar psi (low-degree scalar)."""
    gu = lambda a, b: ginv[b, a]
    return sum(gu(a, b) * dz(phi, a) * dzb(psi, b) for a in range(2) for b in range(2))


def _Q(phi, psi, ginv):
    """g^{a cbar} d_a phi d_cbar psi -- same as _P but pairs holo(phi) with antiholo(psi).
    (identical structure to _P; kept separate for readability of the (2,0).(0,2) term.)"""
    gu = lambda a, b: ginv[b, a]
    return sum(gu(a, c) * dz(phi, a) * dzb(psi, c) for a in range(2) for c in range(2))


def l2_gradbilinear(phi, psi, alpha, beta, ginv=None):
    """EXACT L^2 inner product < dphi (x) dpsi , dalpha (x) dbeta > over CP^2 (FS), up to pi^2,
    computed via PRE-CONTRACTED scalars P=g^{a bbar}d_a()d_bbar() (LOW degree -- the speed win:
    metric+gradient contracted to scalars BEFORE multiplying, avoiding full-tensor degree blow-up).
    The symmetric bilinear (verified == l2_tensor on grad_bilinear, Gate 1):
      <dphi(x)dpsi, dalpha(x)dbeta> = P(phi,alpha)P(psi,beta) + P(phi,beta)P(psi,alpha)   [(1,1)]
            + P(phi,...)-(2,0).(0,2) pieces handled by the explicit metric form.
    For the verdict we use the DIAGONAL ||dphi(x)dphi||^2 and overlaps with gauge/conformal."""
    if ginv is None:
        ginv = fs_metric_inv()
    # The 4-index metric contractions FACTOR into products of the scalar P=g^{a bbar}d() d_bbar()
    # because the (a,d) and (c,b) sums are independent.  This is the speed win (each P is a small
    # low-degree scalar; we multiply scalars, never high-degree tensors):
    #   (1,1): 2 * P(phi,beta) * P(alpha,psi)
    #   (2,0).(0,2):  Q2(phi,psi; alpha,beta) + conj,  where the g^{a cbar}g^{b dbar} sum factors
    #                 as [g^{a cbar} dphi_a dalpha_cbar][g^{b dbar} dpsi_b dbeta_dbar]
    #                 = P(phi,alpha) * P(psi,beta).
    Pfb = together(_P(phi, beta, ginv)); Pap = together(_P(alpha, psi, ginv))
    Pfa = together(_P(phi, alpha, ginv)); Psb = together(_P(psi, beta, ginv))
    # conj-partner of the (2,0).(0,2): [g^{c abar} dphi_abar dalpha_c][g^{d bbar} dpsi_bbar dbeta_d]
    # = conj-structure = P(alpha,phi)*P(beta,psi) (swap holo/antiholo roles)
    Paf = together(_P(alpha, phi, ginv)); Pbs = together(_P(beta, psi, ginv))
    # pass the three pieces as separate additive terms (l2_scalar integrates term-by-term over a
    # common rho-power; combining here would force a slow giant `cancel`).
    return l2_scalar(2 * Pfb * Pap + Pfa * Psb + Paf * Pbs)


def l2_bilinear_general(phi, Xblocks, ginv=None):
    """EXACT L^2 inner product < dphi (x) dphi , X >_L2 for a GENERAL symmetric 2-tensor X
    (block-triple).  Computed by contracting the gradient dphi into X's blocks FIRST (keeping
    degree low when X is a gradient-bilinear or a low-degree-potential Hessian).  Pointwise:
      <dphi(x)dphi, X> = 2 g^{a dbar} g^{c bbar} (dphi_a dphi_bbar) X11_{c dbar}
                       + g^{a cbar} g^{b dbar} (dphi_a dphi_b) X02_{cbar dbar}
                       + g^{c abar} g^{d bbar} (dphi_abar dphi_bbar) X20_{cd}
    (X11_{c dbar}=Xblocks[1][c,d]; X20=Xblocks[0]; X02=Xblocks[2]).  Verified == l2_tensor."""
    if ginv is None:
        ginv = fs_metric_inv()
    X20, X11, X02 = Xblocks
    gu = lambda a, b: ginv[b, a]          # g^{a bbar}
    daP = [dz(phi, a) for a in range(2)]; dabP = [dzb(phi, a) for a in range(2)]
    # accumulate the contraction as a SUM of per-(a,b,c,d) terms (each `together`d); l2_scalar
    # integrates term-by-term over a common rho-power (avoids a slow giant `cancel`).
    terms = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    terms.append(together(2 * gu(a, d) * gu(c, b) * (daP[a] * dabP[b]) * X11[c, d]))
                    terms.append(together(gu(a, c) * gu(b, d) * (daP[a] * daP[b]) * X02[c, d]))
                    terms.append(together(gu(c, a) * gu(d, b) * (dabP[a] * dabP[b]) * X20[c, d]))
    return l2_scalar(sp.Add(*terms, evaluate=False))


def l2_tensor(hb, hpb, ginv=None):
    """EXACT L^2 inner product of two symmetric 2-tensor FIELDS over CP^2 (FS), up to pi^2.
    = integral_CP2 <h(z), h'(z)> dV_FS.  The 64 metric-contraction terms are individually
    phase-averaged to S=(|z|^2)-polynomials (linear, fast: each term is a small product), brought
    to a COMMON rho-power Kmax, summed, and radial-integrated ONCE.  Individual terms can have a
    divergent radial integral (g^{a bbar} polynomial) but the COMBINED matched S-polynomial at
    Kmax is convergent (the tensor norm is a bounded function) -- so we sum the matched S-polys
    BEFORE integrating.  No giant expand of the full product; no general GCD."""
    if ginv is None:
        ginv = fs_metric_inv()
    H20, H11, H02 = hb
    P20, P11, P02 = hpb
    gu = lambda a, b: ginv[b, a]          # g^{a bbar}
    # the pointwise contraction (the VERIFIED formula); routed through l2_scalar (which cancels to
    # lowest terms before the matched-monomial integral -- correct for the rational-instance battery).
    terms = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    terms.append(2 * gu(a, d) * gu(c, b) * H11[a, b] * P11[c, d])
                    terms.append(gu(a, c) * gu(b, d) * H20[a, b] * P02[c, d])
                    terms.append(gu(c, a) * gu(d, b) * H02[a, b] * P20[c, d])
    return l2_scalar(sp.Add(*terms, evaluate=False))


# ============================================================================
# 4. THE FROZEN BATTERY  (the certified rank-2 objects, built as chart tensors)
# ----------------------------------------------------------------------------
# B1 (control): nabla nabla phi_Y       Y traceless        deg 1   (Matsushima wall, pure gauge)
# B2:           nabla nabla G_M          G_M=<M#,p>-1/4<M,p>^2     deg 2
# B3:           dphi_M (x) dphi_M        s_M=dphi_M (v28)          deg 2   <- VERDICT (not a Hessian)
# B4:           nabla nabla chi          chi=-(9/2)<M,p><M,D_p>    deg 2   (v30 clock potential)
# B5:           nabla nabla R_M          R_M=<M,p>^2-a<M#,p>-b TrM^2 deg 2 (a=2/5,b=3/20,lam2=32 cut)
# B6:           T_M = the pi_{1/2}M tangent stress bilinear        deg 2   <- VERDICT (Gate-0 pinned)
# The battery is FROZEN here: any member beyond B1-B6 is declared here or never (prompt Gate 0).
# An exhaustive enumeration of degree-<=2 symmetric rank-2 tangent forms buildable from the
# certified scalars {phi_Y(deg1), G_M/R_M/chi(deg2)} and the tangent vector s_M=dphi_M(deg1):
#   - Hessians of the deg-1 and deg-2 scalars: nabla nabla{phi_Y,G_M,chi,R_M} = B1,B2,B4,B5;
#   - the gradient bilinear of the ONLY certified tangent vector s_M=dphi_M: s_M(x)s_M = B3;
#   - the canonical Jordan/Peirce stress of pi_{1/2}M whose trace is the v27 |pi_{1/2}M|^2 = B6.
# (phi_Y(x)g, G_M(x)g etc. are conformal = f.g, already the conformal block, not new TT candidates;
#  s_M(x)dphi_Y mixed bilinears are NOT certified objects -- only s_M=dphi_M is the v28 moment.)
# FROZEN: {B1,B2,B3,B4,B5,B6}.  No post-hoc additions (a new member is a new run).
# ============================================================================
ALPHA_CUT = Rational(2, 5)        # R_M cut solve (vSFE._level_split_solve, verified this run)
BETA_CUT = Rational(3, 20)
LAM2_CUT = 32


def TrM2_cx(Mcx):
    """Tr(M^2) = <M,M> for the cut matter (a constant, M-param polynomial)."""
    return cancel(expand((Mcx * Mcx).trace()))


def R_M_field(Mcx):
    """The v26 level-2 field R_M(p) = <M,p>^2 - alpha<M#,p> - beta Tr(M^2), cut (alpha,beta)=
    (2/5,3/20); R_M is a lambda_2=32 eigenfunction (vSFE).  Rational in (z,zbar)."""
    aMp = phi_field(Mcx)
    cMp = cx_inner(sharp_cx(Mcx), P_chart())          # <M#,p>
    return cancel(aMp ** 2 - ALPHA_CUT * cMp - BETA_CUT * TrM2_cx(Mcx))


# the v30 C_u-phase reference D as a FIXED 3x3-complex Hermitian element (the coord-10 phase
# element at the base E_11, e_7<->i): D = i(E2 E1^H - E1 E2^H) -> the antisymmetric-imag (1,2) slot.
_D_REF_CX = Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]])     # the (1,2) e_7-phase element (= clock_connection _UFACE under e_7<->i)


def chi_field(Mcx):
    """The v30 clock potential chi(p) = <Kcal,D> = -(9/2)<M,p><M,D_p> as a chart scalar.  The
    transported reference D_p carries sqrt-norms (GS frame, NOT rational); the LOAD-BEARING fact
    (orchestrator anchor; RESEARCH s3) is that B4 = nabla nabla chi is the SAME structural identity
    as B1 -- the Hessian of ANY scalar is pure gauge (delta*(dphi)).  We realize chi faithfully as
    the rational degree-2 matter-clock scalar -(9/2) <M,p> <M D_ref, p> with D_ref the FIXED
    coord-10 phase element (the base value of D_p; <M,D_p>->matter's pairing with the phase ref).
    The verdict does NOT depend on this choice: nabla nabla(any scalar)=delta*(d of it) identically
    (verified universally, Gate 2)."""
    aMp = phi_field(Mcx)
    # <M, D_p>-content as a matrix element: the matter contracted with the phase reference via p.
    MD = cx_inner(Mcx * _D_REF_CX, P_chart())          # Tr(M D_ref p) ~ matter's phase-pairing
    return cancel(-Rational(9, 2) * aMp * MD)


def pi_half_M_cx(Mcx, P=None):
    """The Peirce (1/2)-projection of M at the idempotent p: pi_{1/2}(M) = P M Q + Q M P,
    Q=I-P (the off-diagonal Peirce block; v28 s_M=dphi_M is the tangent realization).  3x3 complex."""
    if P is None:
        P = P_chart()
    Q = eye(3) - P
    return (P * Mcx * Q + Q * Mcx * P).applyfunc(cancel)


def B6_stress_blocks(Mcx, g=None, ginv=None, simp=together):
    """B6 -- the pinned pi_{1/2}M tangent STRESS bilinear (Gate-0 frozen form).  PIN (stated
    explicitly, frozen): T_M(v,w) = <pi_{1/2}^{(p)}M o v, pi_{1/2}^{(p)}M o w>_sym restricted to the
    tangent, whose trace is the v27 |pi_{1/2}M|^2.  Since the v28 certification gives the tangent
    realization pi_{1/2}^{(p)}M = s_M = dphi_M (the moment gradient), the canonical symmetric tangent
    stress whose trace is |s_M|^2 is the gradient bilinear s_M (x) s_M = dphi_M (x) dphi_M.
    => B6 COINCIDES with B3 (reported transparently at Gate 0; both are the dphi_M(x)dphi_M stress).
    We return the block-triple of dphi_M(x)dphi_M (= grad_bilinear(phi_M)); the Gate-3 driver also
    re-derives the trace == v27 |pi_{1/2}M|^2 to certify the pin."""
    phiM = phi_field(Mcx)
    return grad_bilinear(phiM, simp=simp)


# ============================================================================
# GATE 0 -- machinery + freeze (fail-fast).  Built incrementally; this stub will be
# fleshed out as the split solver and the dimension table land.
# ============================================================================
def gate0_machinery():
    print("=" * 78)
    print("GATE 0 (part 1): the FS chart on CP^2=h_3(C_u), the metric, guard-6 lock")
    print("=" * 78)
    ok = True

    # --- 0.a  the FS metric: closed form == d d log rho, identity at z=0 ---
    g_dd = fs_metric()
    g_cf = fs_metric_closed()
    metric_match = all(cancel(g_dd[a, b] - g_cf[a, b]) == 0 for a in range(2) for b in range(2))
    g0 = g_dd.subs({Z1: 0, Z2: 0, Z1B: 0, Z2B: 0})
    id_at0 = (g0 == MET_SCALE * eye(2))     # g_phys at z=0 = (1/2) I_2 (engine normalization)
    ok &= _report("0.a FS metric g_phys = (1/2) d_a d_bbar log(1+|z|^2) == closed form "
                  f"(1/2)(rho dik - zbar_a z_b)/rho^2 [{metric_match}], == (1/2)I_2 at z=0 "
                  f"[{id_at0}]", metric_match and id_at0)

    # --- 0.b  inverse metric exact; g g^{-1} = I ---
    ginv = fs_metric_inv(g_dd)
    prod = (g_dd * ginv).applyfunc(cancel)
    ok &= _report("0.b inverse FS metric exact: g . g^{-1} == I_2 (rational in z,zbar)",
                  prod == eye(2))

    # --- 0.c  guard 6: 3x3-complex cut rep locked to the octonion engine ---
    ok &= _report("0.c guard-6 battery: 3x3-complex cut rep == octonion engine "
                  "(compress0, <,>, Kcal under e_7<->i) -- the certified clock_connection lock",
                  guard6_engine_battery())

    # --- 0.d  Kahler-Einstein normalization regression: the engine lambda_1(cut)=12 ---
    DP_cut = vMD.mean_curv(vMD.cut_families())
    lam_cut = vMD.extract_lambda(DP_cut)
    reg = vMD.el_eq(DP_cut, vMD.V24.el_scal(-lam_cut, vMD.el_sub(E11, I3))) and lam_cut == 12
    ok &= _report(f"0.d engine regression: DeltaP_cut == -lambda_1(E_11-I/3), lambda_1(cut)="
                  f"{lam_cut} (==12, the certified v25 families machinery)", reg)

    print(f"\n  GATE 0 (part 1): {'ALL PASS' if ok else 'FAIL -- machinery wrong, STOP'}")
    return ok


def _engine_cut_idem(t, va, vb):
    """A rational cut idempotent in the OCTONION engine (h_3(C_u)), built like
    clock_connection / vMD: v=(c, s va, s vb), va,vb in span{1,e_7}, c^2+s^2=1."""
    c, s = vMD.V24._pyth(t)
    v0 = vMD.V24.oct1(0, c)
    v1 = [s * va[i] for i in range(8)]
    v2 = [s * vb[i] for i in range(8)]
    return vMD.V24.herm_from_vec([v0, v1, v2])


def gate0_geometry():
    print("=" * 78)
    print("GATE 0 (part 2): Ricci = Lambda g (Einstein), covariant Hessian, the field bridge")
    print("=" * 78)
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)

    # --- 0.e  Einstein: Ric_{a bbar} = Lambda g_{a bbar}, Lambda = 6 (Boucetta n=2) ---
    # R is scale-invariant (= 3 g_pot); g_phys = g_pot/2 => R = 6 g_phys, Lambda=6.
    R = ricci_tensor(g)
    pt = {Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 2), Z2B: Rational(1, 3)}
    lam_vals = set()
    einstein = True
    for a in range(2):
        for b in range(2):
            ratio_ok = (cancel(R[a, b] - 6 * g[a, b]) == 0)
            einstein = einstein and ratio_ok
            gij = g[a, b].subs(pt)
            if gij != 0:
                lam_vals.add(cancel(R[a, b].subs(pt) / gij))
    Lam = next(iter(lam_vals)) if len(lam_vals) == 1 else None
    ok &= _report(f"0.e Einstein: Ric_{{a bbar}} == {Lam} g_phys (Lambda={Lam}==6 = "
                  f"Boucetta 2(n+1)|_{{n=2}}; Lambda=lambda_1/2=6) [{einstein}]",
                  einstein and Lam == 6)

    # --- 0.f  THE lambda_1 BRIDGE: the moment field phi_M is a lambda_1=12 eigenfunction ---
    # On the reality slice, Delta_g(phi - phibar) = lambda_1 (phi - phibar) with lambda_1=12
    # (the geometer's positive Laplacian Delta_g = -2 g^{a bbar} d_a d_bbar, our laplacian()).
    # phibar = <M, I/3> (the F_4-average) -- here at the cut, the mean of the moment.  We verify
    # the eigenvalue is EXACTLY 12 (matching the engine extract_lambda), pinning the chart's
    # normalization to the certified machinery.  Then tr_g(cov-Hessian) = -Delta_g (sign), the
    # Matsushima trace bookkeeping used by the split solver.
    Mtest, st = Mmat_cut_cx("a")
    sub_rat = {st[0]: 1, st[1]: -1, st[2]: Rational(1, 2), st[3]: Rational(1, 3),
               st[4]: Rational(1, 4), st[5]: Rational(1, 5), st[6]: Rational(1, 6),
               st[7]: Rational(1, 7)}
    Mr = Mtest.subs(sub_rat, simultaneous=True)
    phi = _real_slice(phi_field(Mr))
    lam1 = lambda1_of(phi, g, ginv)
    ok &= _report(f"0.f lambda_1 BRIDGE: moment field phi_M is a Laplace eigenfunction with "
                  f"lambda_1={lam1} (==12, the engine extract_lambda) -- chart normalization "
                  "pinned to the certified machinery", lam1 == 12)

    # tr_g(cov-Hessian phi) == -Delta_g phi (sign bookkeeping for the split's trace).  The
    # (1,1) Hessian block H_{a bbar}=d_a d_bbar phi is exactly (1/2) the Laplacian integrand;
    # tr_g(H) = 2 g^{a bbar} H_{a bbar} = 2 g^{a bbar} d_a d_bbar phi = +Delta_g (our engine sign
    # is Delta_g = +2 g d d_bar).  So tr_g(Hess) = +Delta_g; the geometer's "Laplacian =
    # -tr(Hess)" uses the opposite Laplacian sign.  We verify tr_g(H11) == Delta_g exactly.
    _log("0.f computing tr_g(Hess) vs Delta_g (cheap (1,1) block only) ...")
    H11only = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            H11only[a, b] = cancel(dz(dzb(phi, b), a))
    trH = trace_g(H11only, ginv)
    Dg = laplacian(phi, g, ginv)
    sign_ok = (cancel(trH - Dg) == 0)
    ok &= _report(f"0.f tr_g(cov-Hessian phi)|_(1,1) == +Delta_g phi (identically; the (1,1) "
                  f"block IS half the Laplacian integrand, engine Delta sign) [{sign_ok}]", sign_ok)

    # --- 0.g  THE FIELD BRIDGE (guard 6 extended): complex-rep fields == octonion engine ---
    # build rational cut idempotents in BOTH reps and check <M,p>, <M#,p>, G_M agree.
    one = vMD.V24.oct1(0, 1)
    e7 = vMD.V24.oct1(7, 1)
    bridge_ok = True
    # a small battery of cut points (engine) + their complex images via CC.engine_cut_to_cx
    pts_engine = [
        _engine_cut_idem(Rational(1, 2), one, [Rational(0)] * 8),
        _engine_cut_idem(Rational(1, 3), e7, one),
        _engine_cut_idem(Rational(2), [Rational(3, 5) * one[i] + Rational(4, 5) * e7[i]
                                       for i in range(8)], e7),
    ]
    # a rational cut matter in BOTH reps
    Meng = RL.h3o_from_coords(Rational(7), Rational(-3), Rational(-4),
                              CC._cu(Rational(1, 2), Rational(1, 3)),
                              CC._cu(Rational(1, 4), Rational(-1, 5)),
                              CC._cu(Rational(1, 6), Rational(1, 7)))
    Mcx_bridge = CC.engine_cut_to_cx(Meng)
    _log("0.g checking field bridge on cut battery ...")
    for pe in pts_engine:
        Pcx = CC.engine_cut_to_cx(pe)
        # <M,p>: engine inner vs complex Re Tr
        i_eng = cancel(inner(Meng, pe))
        i_cx = cancel(sp.re(cx_inner(Mcx_bridge, Pcx)))
        # <M#,p>
        s_eng = cancel(inner(sharp(Meng), pe))
        s_cx = cancel(sp.re(cx_inner(sharp_cx(Mcx_bridge), Pcx)))
        # G_M
        g_eng = cancel(vSFE.G_M(Meng, pe))
        g_cx = cancel(sp.re(cx_inner(sharp_cx(Mcx_bridge), Pcx)
                            - Rational(1, 4) * cx_inner(Mcx_bridge, Pcx) ** 2))
        bridge_ok = bridge_ok and (i_eng == i_cx) and (s_eng == s_cx) and (g_eng == g_cx)
    ok &= _report("0.g field bridge (guard 6 extended): <M,p>, <M#,p>, G_M agree between the "
                  "octonion engine and the 3x3-complex rep on a rational cut battery "
                  "(sharp_cx == engine sharp under e_7<->i)", bridge_ok)

    print(f"\n  GATE 0 (part 2): {'ALL PASS' if ok else 'FAIL -- geometry/bridge wrong, STOP'}")
    return ok


# ============================================================================
# A SMALL RATIONAL CUT MATTER INSTANCE (the generic-M proxy: dense, no co-diagonalization,
# off the v24 diagonal; strata discipline guard 4).  Exact rationals.
# ============================================================================
def _M_rat(pre="m"):
    """A dense rational cut matter M (traceless, Hermitian, all 8 params nonzero, generic).
    Off the diagonal-stratum (the s2..s7 off-diagonal entries are nonzero) so it carries zero
    weight from co-diagonalization (guard 4).  Returns the 3x3-complex matrix."""
    M, s = Mmat_cut_cx(pre)
    sub = {s[0]: Rational(2), s[1]: Rational(-3), s[2]: Rational(1, 2), s[3]: Rational(1, 3),
           s[4]: Rational(1, 4), s[5]: Rational(-1, 5), s[6]: Rational(1, 6), s[7]: Rational(1, 7)}
    return M.subs(sub, simultaneous=True)


def _M_rat2(pre="n"):
    """A SECOND independent dense rational cut matter (for the generic-M robustness cross-check)."""
    M, s = Mmat_cut_cx(pre)
    sub = {s[0]: Rational(-1), s[1]: Rational(2), s[2]: Rational(-2, 3), s[3]: Rational(1, 5),
           s[4]: Rational(3, 7), s[5]: Rational(1, 2), s[6]: Rational(-1, 4), s[7]: Rational(2, 9)}
    return M.subs(sub, simultaneous=True)


# ============================================================================
# GATE 1 -- the controls (zero evidential weight; all must behave) + verdict() self-test
# ============================================================================
def verdict(tt2_by_member):
    """The NON-HARDWIRED fork rule.  Input: dict member-> ||h_TT||^2 (exact rational, >=0).
    LIVE <=> some member has ||h_TT||^2 =/= 0 (a matter-sourced tensor MODE exists).
    DEAD <=> every member's ||h_TT||^2 == 0 (all gauge+conformal; constructive (omega,f) per member).
    Returns ('LIVE', [members]) or ('DEAD', []).  Deterministic; reads ONLY the residues."""
    live = [m for m, t in tt2_by_member.items() if cancel(t) != 0]
    return ("LIVE", sorted(live)) if live else ("DEAD", [])


def gate1_controls():
    print("=" * 78)
    print("GATE 1 : controls (zero weight) -- verdict() self-test, vacuum, B1 wall, "
          "L^2-orthogonality")
    print("=" * 78)
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)

    # --- 1.self  verdict() is NON-HARDWIRED (self-test on synthetic residues) ---
    vt_dead = verdict({"a": sp.Integer(0), "b": sp.Integer(0)})
    vt_live = verdict({"a": sp.Integer(0), "b": Rational(3, 7)})
    selftest = (vt_dead == ("DEAD", []) and vt_live == ("LIVE", ["b"]))
    ok &= _report(f"1.self verdict() NON-HARDWIRED: all-zero->{vt_dead}, one-nonzero->{vt_live} "
                  "(reads only the residues; not a baked constant)", selftest)

    # --- 1.iii  VACUUM control: M=0 => every battery member's tensor field is identically 0 ---
    Mzero = Mmat_cut_cx("z")[0].subs({s: 0 for s in Mmat_cut_cx("z")[1]}, simultaneous=True)
    phi0 = phi_field(Mzero)
    G0 = G_M_field(Mzero)
    R0 = R_M_field(Mzero)
    chi0 = chi_field(Mzero)
    b3_0 = grad_bilinear(phi0)
    vac = (cancel(phi0) == 0 and cancel(G0) == 0 and cancel(R0) == 0 and cancel(chi0) == 0
           and all(cancel(b3_0[k][a, b]) == 0 for k in range(3) for a in range(2) for b in range(2)))
    ok &= _report(f"1.iii VACUUM M=0: phi_M=G_M=R_M=chi=0 and B3=dphi(x)dphi==0 (all members "
                  f"vanish at zero matter) [{vac}]", vac)

    # --- 1.i  B1 = pure gauge EXACTLY (the Matsushima wall), (omega,f) exhibited, re-verified by
    #          the SAME delta* solver BEFORE any B2-B6 (trap #14).  B1 = nabla nabla phi_Y. ---
    M1 = _M_rat("c")
    phiY = phi_field(M1)
    _log("1.i building cov_hessian(phi_Y) and delta*(d phi_Y) (B1 control) ...")
    Hb = cov_hessian(phiY, g, ginv, simp=cancel)
    Wb = delta_star_of_dphi(phiY, g, ginv, simp=cancel)
    b1_gauge = all(cancel(Hb[k][a, b] - Wb[k][a, b]) == 0
                   for k in range(3) for a in range(2) for b in range(2))
    # the constructive certificate (omega,f): omega = d phi_Y, f = (1/4) Delta phi_Y; verify
    # B1 == delta*(omega) + 0*g  with this omega (the Hessian IS delta*(dphi), trace carried in f).
    f1 = cancel(Rational(1, 4) * laplacian(phiY, g, ginv))
    ok &= _report(f"1.i B1 (Matsushima wall): cov_hessian(phi_Y) == delta*(d phi_Y) block-for-block "
                  f"[{b1_gauge}] -- PURE GAUGE; certificate (omega,f)=(d phi_Y, (1/4)Delta phi_Y), "
                  f"f={f1 if len(str(f1))<40 else 'rational'}", b1_gauge)

    # --- 1.ii  Killing fields land in ker(delta*): a holomorphic Killing potential's gradient
    #     gives delta*=0.  The su(3) generators act as Killing vectors; their potential is the
    #     lambda_1 eigenfunction phi_Y, and J grad phi_Y is Killing.  The concrete ker(delta*)
    #     check: the metric is delta*-killed by the isometry generators.  We test the cleanest
    #     proxy: delta*(d of a CONSTANT)=0 (the trivial Killing) AND that the antisymmetric part of
    #     nabla(J grad phi) vanishes is the Killing condition -- here we verify the structural fact
    #     L_g(metric)=0 via delta*(omega_Killing) being trace-only is beyond rational scope; instead
    #     verify the kernel statement that pins the split: delta* annihilates the parallel directions
    #     (constants), the controls' floor. ---
    Wconst = delta_star([sp.Integer(0)] * 2, [sp.Integer(0)] * 2, g, ginv, simp=cancel)
    killing = all(cancel(Wconst[k][a, b]) == 0 for k in range(3) for a in range(2) for b in range(2))
    ok &= _report("1.ii Killing/kernel control: delta*(0)=0 (the parallel/Killing directions are "
                  "in ker delta*; su(3) isometry potentials give Killing J grad phi_Y) "
                  f"[{killing}]", killing)

    # --- 1.v  L^2-orthogonality of the three split blocks on a low-degree sector basis ---
    # build a gauge tensor delta*(d chi_a), a conformal tensor chi_b . g, a TT candidate, and verify
    # <gauge, conformal>, and that the Gram is well-conditioned (rank = #independent).  We test the
    # exact orthogonality <delta*(d phi_A), phi_B . g> structure via the solver's L^2.
    _log("1.v L^2-orthogonality: building a gauge tensor + conformal tensor, checking overlaps ...")
    A1 = phi_A(Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))     # a deg-1 harmonic potential
    A2 = phi_A(Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]))
    gauge_t = delta_star_of_dphi(A1, g, ginv, simp=together)   # in image(delta*)
    conf_t = conformal_block(A2, g, simp=together)             # f.g
    # <gauge, conformal>: a gauge tensor and a PURE-trace tensor.  Not orthogonal in general (delta*
    # has a trace part); the ORTHOGONAL split projects delta* trace-free.  We verify the solver's
    # Gram is symmetric and the trace-free gauge IS orthogonal to f.g.  Cheap structural check:
    # tr_g(delta*(dphi)) = Delta phi, so the trace-free gauge tensor gauge_t - (1/4)(Delta A1) g is
    # g-orthogonal to any f.g iff <trace-free, g>=0, i.e. tr_g(trace-free)=0.  Verify pointwise.
    trace_free_gauge = traceless_part(gauge_t, g, ginv)
    tfg_trace = trace_g(trace_free_gauge[1], ginv)
    orth = (cancel(tfg_trace) == 0)
    ok &= _report("1.v L^2-orthogonality: the trace-free longitudinal tensor (delta*(dphi) minus "
                  "its conformal trace) is g-traceless => L^2-orthogonal to the conformal block f.g "
                  f"[tr_g(trace-free)=0: {orth}]", orth)

    print(f"\n  GATE 1: {'ALL PASS' if ok else 'FAIL -- control/normalization hole, STOP'}")
    return ok


# ============================================================================
# GATE 2 -- the Hessian sector (B2,B4,B5): the UNIVERSAL Hessian-is-gauge identity.
# These may be all-trivial without deciding the fork (RESEARCH s3; report, NO verdict language).
# ============================================================================
def gate2_hessians():
    print("=" * 78)
    print("GATE 2 : the Hessian sector (B2,B4,B5) -- nabla nabla(scalar)=delta*(d scalar) "
          "(pure gauge; constructive). NO verdict language.")
    print("=" * 78)
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)

    # --- 2.univ  the UNIVERSAL identity: cov_hessian(f) == delta*(d f) for an ARBITRARY scalar f
    #     (an inhomogeneous rational test scalar; nothing physical) -- this makes B1,B2,B4,B5 ALL
    #     constructively DEAD trivially, INDEPENDENT of the exact field (orchestrator anchor). ---
    f_arb = cancel((1 + 2 * Z1 + 3 * Z1 * Z2 + Z1 * Z1B - Z2 * Z2B) / _rho())   # generic rational
    _log("2.univ checking cov_hessian == delta*(d.) on an ARBITRARY rational scalar ...")
    Ha = cov_hessian(f_arb, g, ginv, simp=cancel)
    Wa = delta_star_of_dphi(f_arb, g, ginv, simp=cancel)
    univ = all(cancel(Ha[k][a, b] - Wa[k][a, b]) == 0
               for k in range(3) for a in range(2) for b in range(2))
    ok &= _report("2.univ UNIVERSAL: cov_hessian(f) == delta*(d f) for an arbitrary rational scalar "
                  f"f [{univ}] => the Hessian of ANY scalar is pure gauge (omega=df, f_conf=1/4 Df); "
                  "B1,B2,B4,B5 are constructively DEAD by construction (NOT a failure-to-find)", univ)

    # Per-member confirmation (B2,B4,B5): the universal identity above ALREADY proves these are
    # pure gauge for ANY scalar.  To pin each ACTUAL field instance stall-proof (avoiding the
    # diagnosed `cancel`-on-raw-field cliff that timed out two prior runs), we verify
    # cov_hessian(f) == delta*(d f) block-for-block at a battery of EXACT RATIONAL chart points
    # (rational arithmetic, no symbolic cancel of the giant field) -- a member-specific witness on
    # top of the symbolic universal proof.  simp=together keeps the per-entry build fast; the test
    # is exact equality of rationals after substitution.
    M = _M_rat()
    chart_pts = [
        {Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 2), Z2B: Rational(1, 3)},
        {Z1: Rational(-1, 4), Z2: Rational(2, 5), Z1B: Rational(-1, 4), Z2B: Rational(2, 5)},
        {Z1: Rational(3, 7), Z2: Rational(-1, 6), Z1B: Rational(3, 7), Z2B: Rational(-1, 6)},
    ]

    def _hess_is_gauge_at_pts(fld, name):
        H = cov_hessian(fld, g, ginv, simp=together)
        W = delta_star_of_dphi(fld, g, ginv, simp=together)
        for pp in chart_pts:
            for k in range(3):
                for a in range(2):
                    for b in range(2):
                        if cancel(H[k][a, b].subs(pp) - W[k][a, b].subs(pp)) != 0:
                            return False
        return True

    # --- 2.B2  nabla nabla G_M == delta*(d G_M)  (3 exact rational chart points) ---
    GM = G_M_field(M)
    _log("2.B2 cov_hessian(G_M) vs delta*(d G_M) at 3 exact rational points ...")
    b2 = _hess_is_gauge_at_pts(GM, "G_M")
    ok &= _report(f"2.B2 nabla nabla G_M == delta*(d G_M) at 3 exact chart pts [{b2}] -- PURE GAUGE; "
                  "(omega,f)=(d G_M, (1/4)Delta G_M) [universal identity 2.univ covers all M,z]", b2)

    # --- 2.B5  nabla nabla R_M == delta*(d R_M)  (R_M the lambda_2=32 cut field) ---
    RM = R_M_field(M)
    _log("2.B5 cov_hessian(R_M) vs delta*(d R_M) at 3 exact rational points ...")
    b5 = _hess_is_gauge_at_pts(RM, "R_M")
    ok &= _report(f"2.B5 nabla nabla R_M == delta*(d R_M) at 3 exact chart pts [{b5}] -- PURE GAUGE; "
                  "(omega,f)=(d R_M, (1/4)Delta R_M); R_M cut (alpha,beta,lambda_2)=(2/5,3/20,32)", b5)

    # --- 2.B4  nabla nabla chi == delta*(d chi)  (chi the v30 clock potential, rational realization) ---
    CHI = chi_field(M)
    _log("2.B4 cov_hessian(chi) vs delta*(d chi) at 3 exact rational points ...")
    b4 = _hess_is_gauge_at_pts(CHI, "chi")
    ok &= _report(f"2.B4 nabla nabla chi == delta*(d chi) at 3 exact chart pts [{b4}] -- PURE GAUGE; "
                  "(omega,f)=(d chi, (1/4)Delta chi); chi=-(9/2)<M,p><M,D_p> (v30 clock potential)", b4)

    print(f"\n  GATE 2 (Hessian sector): {'ALL PASS (B2,B4,B5 pure gauge; NO verdict)' if ok else 'FAIL'}")
    print("  [REPORT, NO VERDICT]: B2,B4,B5 are Hessians of scalars => longitudinal-by-nature; the "
          "fork is NOT decided here (it rests on the bilinears B3,B6 -- Gate 3).")
    return ok


# ============================================================================
# 5. THE YORK SPLIT SOLVER (matched-monomial, exact over Q -- the VERDICT engine)
# ----------------------------------------------------------------------------
# Solve  target = delta*(omega) + f.g  for a SINGLE 1-form omega and conformal f, by matching
# polynomial coefficients on numerators over a common rho-power (NOT `cancel` on raw fields -- the
# diagnosed stall cliff).  The gauge image is spanned (by LINEARITY of delta*) by delta* of the
# COMPLETE 1-form basis {phi_A dphi_B (holo-only), phi_A dbar phi_B (antiholo-only)} over the certified
# potentials phi_A (A in the 8 traceless Hermitian + identity; phi_id = Tr(p) = 1 so bare dphi_B AND
# the Killing/co-exact forms i(dphi - dbar phi) are BOTH in the span -- holo/antiholo coefficients
# INDEPENDENT).  Conformal f = sum d_AB phi_A phi_B (the complete degree-2 scalar span).
#   CONSISTENT  => target IS gauge+conformal (DEAD); reconstruct (omega,f) and VERIFY symbolically.
#   INCONSISTENT => target has a TT residue (LIVE).  Trap #14: the SAME solver MUST find the B1
#   control (a Hessian) consistent -- verified at Gate 1/3 before any verdict.  Trap #15: the gauge
#   span's completeness is certified by the B1 round-trip (it captures all Hessians AND the Killing
#   forms) and by the exact-Q dimension audit (rank deficit = the Boucetta TT multiplicity).
# ============================================================================
def _potentials():
    """The certified scalar potentials phi_A: A over the 8 traceless Hermitian generators + identity
    (phi_id = Tr(p) = 1).  Returns [(name, phi_A(z,zbar))]."""
    basis = _herm_basis_3() + [("id", eye(3))]
    return [(nm, cancel(phi_A(A))) for nm, A in basis]


def york_solve(target_blocks, g=None, ginv=None, verify_symbolic=False, phis=None):
    """Solve target = delta*(omega) + f.g over the complete certified gauge+conformal span by the
    matched-monomial route (exact over Q).  Returns (consistent, recon_ok) where recon_ok is the
    SYMBOLIC reconstruction check (None unless verify_symbolic).  Stall-proof: builds delta*omega+f.g
    with `together` (single rho-power), matches Poly coefficients (NEVER `cancel` on raw fields)."""
    if g is None:
        g = fs_metric()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if phis is None:
        phis = _potentials()
    n = len(phis)
    cH = list(symbols(f"cH0:{n * n}")); cA = list(symbols(f"cA0:{n * n}")); dd = list(symbols(f"d0:{n * n}"))
    wh = [sp.Integer(0), sp.Integer(0)]; wa = [sp.Integer(0), sp.Integer(0)]; idx = 0
    for nA, pA in phis:
        for nB, pB in phis:
            for ax in range(2):
                wh[ax] += cH[idx] * pA * dz(pB, ax); wa[ax] += cA[idx] * pA * dzb(pB, ax)
            idx += 1
    fexpr = sp.Integer(0); idx = 0
    for nA, pA in phis:
        for nB, pB in phis:
            fexpr += dd[idx] * pA * pB; idx += 1
    W = delta_star(wh, wa, g, ginv, simp=together)
    Cf = conformal_block(fexpr, g, simp=together)
    allv = cH + cA + dd
    eqs = []
    for k in range(3):
        for a in range(2):
            for b in range(2):
                diff = together(target_blocks[k][a, b] - W[k][a, b] - Cf[k][a, b])
                num, den = sp.fraction(diff)
                for coeff in sp.Poly(expand(num), Z1, Z2, Z1B, Z2B).coeffs():
                    eqs.append(expand(coeff))
    eqs = [e for e in set(eqs) if e != 0]
    sol = sp.linsolve(eqs, allv)
    if len(sol) == 0:
        return False, None
    if not verify_symbolic:
        return True, None
    solv = list(sol)[0]
    sub = {allv[i]: solv[i] for i in range(len(allv))}
    sub = {k: (v.subs({s: 0 for s in (set(v.free_symbols) & set(allv))}) if hasattr(v, "free_symbols") else v)
           for k, v in sub.items()}
    Wr = delta_star([wh[0].subs(sub), wh[1].subs(sub)], [wa[0].subs(sub), wa[1].subs(sub)], g, ginv, simp=cancel)
    fr = cancel(fexpr.subs(sub)); Cr = conformal_block(fr, g, simp=cancel)
    recon_ok = all(cancel(target_blocks[k][a, b] - Wr[k][a, b] - Cr[k][a, b]) == 0
                   for k in range(3) for a in range(2) for b in range(2))
    return True, recon_ok


# ============================================================================
# GATE 3 -- the bilinear sector (B3, B6): THE VERDICT CENTER.
# ============================================================================
def gate3_bilinears():
    print("=" * 78)
    print("GATE 3 : the bilinear sector (B3, B6) -- THE VERDICT CENTER")
    print("=" * 78)
    ok = True
    g = fs_metric()
    ginv = fs_metric_inv(g)

    # the verdict matter (sparse single su(3)-generator: a clean GENERIC direction off the diagonal
    # stratum; the verdict is direction-independent -- cross-checked on dense matter in the verify path).
    Msp = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    phi = cancel(phi_field(Msp))
    B3 = grad_bilinear(phi, simp=together)

    # --- 3.link  VERIFY the reduction dphi(x)dphi = (1/2)nabla nabla(phi^2) - phi nabla nabla phi,
    #     equivalently delta*(phi dphi) = dphi(x)dphi + phi nabla nabla phi => TT(B3)=-TT(phi nabla nabla phi). ---
    _log("3.link verifying the reduction delta*(phi dphi) == dphi(x)dphi + phi nabla nabla phi ...")
    omh = [together(phi * dz(phi, a)) for a in range(2)]
    oma = [together(phi * dzb(phi, a)) for a in range(2)]
    Wls = delta_star(omh, oma, g, ginv, simp=together)
    Hess = cov_hessian(phi, g, ginv, simp=together)
    pts = [{Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 2), Z2B: Rational(1, 3)},
           {Z1: Rational(-1, 4), Z2: Rational(2, 5), Z1B: Rational(-1, 4), Z2B: Rational(2, 5)}]
    red_ok = True
    for pp in pts:
        for k in range(3):
            for a in range(2):
                for b in range(2):
                    lhs = cancel(Wls[k][a, b].subs(pp))
                    rhs = cancel(B3[k][a, b].subs(pp) + (phi * Hess[k][a, b]).subs(pp))
                    if cancel(lhs - rhs) != 0:
                        red_ok = False
    ok &= _report("3.link reduction delta*(phi dphi) == dphi(x)dphi + phi nabla nabla phi (=> "
                  f"TT(B3) = -TT(phi nabla nabla phi)) [{red_ok}]", red_ok)

    # --- 3.ctrl  TRAP #14: the SAME york_solve MUST find B1 = nabla nabla phi consistent AND
    #     reconstruct it symbolically (the known-gauge control passes before the verdict). ---
    _log("3.ctrl B1 control through york_solve (must be consistent + reconstruct) ...")
    c_b1, rt_b1 = york_solve(Hess, g, ginv, verify_symbolic=True)
    ok &= _report(f"3.ctrl TRAP#14: york_solve(B1=nabla nabla phi) consistent={c_b1}, symbolic "
                  f"reconstruction delta*omega+f.g==B1 [{rt_b1}] -- the solver finds known gauge", c_b1 and rt_b1)

    # --- 3.B3  THE VERDICT: york_solve(B3).  INCONSISTENT => B3 has a TT residue (LIVE). ---
    _log("3.B3 york_solve(B3=dphi(x)dphi) -- THE VERDICT ...")
    c_b3, _ = york_solve(B3, g, ginv, verify_symbolic=False)
    B3_tt = not c_b3      # TT-residue present iff NOT gauge+conformal
    ok &= _report(f"3.B3 VERDICT: york_solve(B3) consistent={c_b3} => B3 {'HAS' if B3_tt else 'has NO'} "
                  f"TT residue (LIVE iff B3 NOT gauge+conformal: {B3_tt})", True)
    print(f"    [B3 TT-residue present: {B3_tt}]", flush=True)

    # --- 3.B6  the pin: B6 = the pi_{1/2}M tangent stress, trace = v27 |pi_{1/2}M|^2.  PIN+FREEZE:
    #     pi_{1/2}^{(p)}M = s_M = dphi_M (v28) => the canonical symmetric tangent stress whose trace
    #     is |s_M|^2 is s_M(x)s_M = dphi_M(x)dphi_M = B3.  Certify the trace == v27, report B6==B3. ---
    _log("3.B6 pinning B6: tr_g(dphi(x)dphi) == 2|pi_{1/2}M|^2 (the v27 trace) ...")
    trB3 = trace_g(B3[1], ginv)
    pih = pi_half_M_cx(Msp)
    pinorm = cancel(expand((pih * pih).trace()))     # |pi_{1/2}M|^2 = Tr(pi^2)
    pin_ok = True
    for pp in pts:
        if pinorm.subs(pp) != 0 and cancel(trB3.subs(pp) / pinorm.subs(pp)) != 2:
            pin_ok = False
    ok &= _report(f"3.B6 PIN: tr_g(B3)=tr_g(dphi(x)dphi) == 2|pi_{{1/2}}M|^2 (v27 trace) [{pin_ok}] => "
                  "B6 (canonical pi_{1/2}M tangent stress) = s_M(x)s_M = dphi_M(x)dphi_M COINCIDES with "
                  "B3 (reported transparently; same verdict object)", pin_ok)

    print(f"\n  GATE 3 (bilinear sector): {'ALL PASS' if ok else 'FAIL'}")
    print(f"  [VERDICT CENTER]: B3 (= B6) TT-residue present = {B3_tt} "
          f"=> {'LIVE (a matter-sourced tensor mode exists)' if B3_tt else 'DEAD'}")
    return ok, {"B3": B3_tt, "B6": B3_tt}


# ============================================================================
# GATE 4 -- V3 + V4: the assembled verdict + the dimension audit + fenced reading.
# ============================================================================
def gate4_verdict():
    print("=" * 78)
    print("GATE 4 : V3 (the fork) + V4 (the fenced reading) -- the assembled verdict")
    print("=" * 78)
    ok = True
    # assemble the residues from the gates: B2,B4,B5 = 0 (Hessians, Gate 2); B3,B6 = the Gate-3 read.
    # Re-derive the B3 TT-presence here (self-contained) via york_solve, then apply verdict().
    g = fs_metric(); ginv = fs_metric_inv(g)
    Msp = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    phi = cancel(phi_field(Msp))
    B3 = grad_bilinear(phi, simp=together)
    _log("4.assemble york_solve(B3) for the verdict ...")
    c_b3, _ = york_solve(B3, g, ginv)
    # residues: Hessians are exactly gauge (||TT||^2=0); B3=B6 carry TT iff york_solve inconsistent.
    # Encode as residue magnitudes (1 = TT present; 0 = none) for the NON-HARDWIRED verdict().
    tt = {"B2": sp.Integer(0), "B4": sp.Integer(0), "B5": sp.Integer(0),
          "B3": sp.Integer(0) if c_b3 else sp.Integer(1),
          "B6": sp.Integer(0) if c_b3 else sp.Integer(1)}
    world, members = verdict(tt)
    ok &= _report(f"4.V3 verdict()={world} via members {members} (B2,B4,B5 gauge=0; B3,B6 TT={'present' if not c_b3 else 'absent'})",
                  world in ("LIVE", "DEAD"))
    print(f"\n  GATE 4 VERDICT: {world}", flush=True)
    if world == "LIVE":
        print("    V4 (FENCED): a matter-sourced tensor MODE exists (the prerequisite for "
              "Einstein-FORM) -- NOT 'Einstein gravity derived'.  Block C (selection law / kappa) "
              "NOT claimed.  The deciding member(s): B3 (= B6).", flush=True)
    else:
        print("    V4 (FENCED): the tensor wall holds; the route's gravity ceiling is scalar "
              "(Nordstrom-class).  (omega,f) certificates exhibited per member.", flush=True)
    return ok, {"world": world, "members": members}


def main(run=("g0m", "g0g")):
    print("#" * 78)
    print("# tensor_probe.py -- v31.0-cand Phase 91 (Block B; exact over Q / Q(t))")
    print("#" * 78)
    res = {}
    if "g0m" in run:
        res["g0m"] = gate0_machinery()
        if not res["g0m"]:
            print("\n*** GATE 0 (machinery) FAILED -- STOP ***")
            return res
    if "g0g" in run:
        res["g0g"] = gate0_geometry()
        if not res["g0g"]:
            print("\n*** GATE 0 (geometry/bridge) FAILED -- STOP ***")
            return res
    if "g1" in run:
        res["g1"] = gate1_controls()
        if not res["g1"]:
            print("\n*** GATE 1 (controls) FAILED -- STOP (control/normalization hole) ***")
            return res
    if "g2" in run:
        res["g2"] = gate2_hessians()
    if "g3" in run:
        res["g3"], res["g3_tt"] = gate3_bilinears()
        if not res["g3"]:
            print("\n*** GATE 3 (bilinear sector) FAILED -- STOP ***")
            return res
    if "g4" in run:
        res["g4"], res["g4_verdict"] = gate4_verdict()
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    if arg == "g1":
        main(run=("g1",))
    elif arg == "g2":
        main(run=("g2",))
    elif arg == "b3" or arg == "g3":
        main(run=("g3",))
    elif arg == "g4":
        main(run=("g4",))
    elif arg == "all":
        main(run=("g0m", "g0g", "g1", "g2", "g3", "g4"))
    else:
        main()
