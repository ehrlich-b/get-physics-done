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
    # ginv[c,d] here is g^{c dbar} (we built g as g[a,b]=g_{a bbar}; its inverse is g^{bbar a}
    # but as a 2x2 numeric inverse the index labels are symmetric for our use: g^{c dbar}).
    Gam = [[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)]
    for c in range(2):
        for a in range(2):
            for b in range(2):
                s = sp.Integer(0)
                for d in range(2):
                    s += ginv[c, d] * dz(g[b, d], a)     # g^{c dbar} d_a g_{b dbar}
                Gam[c][a][b] = cancel(s)
    return Gam


def cov_hessian(f, g=None, ginv=None, Gam=None):
    """Covariant Hessian of scalar f as a symmetric 2-tensor on CP^2, returned as the
    three complex blocks (H20, H11, H02) each a 2x2 sympy Matrix:
      H20[a,b] = H_{ab}        (holomorphic (2,0) part)
      H11[a,b] = H_{a bbar}    (mixed (1,1) part)
      H02[a,b] = H_{abar bbar} (antiholomorphic (0,2) part)
    Exact rational in (z,zbar)."""
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
            H11[a, b] = cancel(dz(dzb(f, b), a))
            # (2,0): d_a d_b f - Gamma^c_{ab} d_c f
            t = dz(dz(f, b), a)
            for c in range(2):
                t -= Gam[c][a][b] * dz(f, c)
            H20[a, b] = cancel(t)
            # (0,2): d_abar d_bbar f - Gamma^cbar_{abar bbar} d_cbar f
            t2 = dzb(dzb(f, b), a)
            for c in range(2):
                t2 -= GamB[c][a][b] * dzb(f, c)
            H02[a, b] = cancel(t2)
    return H20, H11, H02


def _christoffel_antihol(g, ginv):
    """Gamma^cbar_{abar bbar} = g^{cbar d} d_abar g_{d bbar}  (conjugate Christoffels)."""
    Gam = [[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)]
    for c in range(2):
        for a in range(2):
            for b in range(2):
                s = sp.Integer(0)
                for d in range(2):
                    s += ginv[d, c] * dzb(g[d, b], a)    # g^{cbar d} d_abar g_{d bbar}
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
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
