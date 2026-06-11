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


def _rho():
    """rho = 1 + |z|^2 = 1 + z1 z1b + z2 z2b (with z_abar independent)."""
    return 1 + Z1 * Z1B + Z2 * Z2B


def kahler_potential():
    return sp.log(_rho())


def dz(f, a):
    return sp.diff(f, ZS[a])


def dzb(f, a):
    return sp.diff(f, ZBS[a])


def fs_metric():
    """g_{a bbar} = d_a d_bbar log rho.  Returns the 2x2 Hermitian matrix (a row, bbar col),
    as exact rational functions of (z, zbar).  At z=0 it is the identity (round normalization
    of the Kahler potential)."""
    K = kahler_potential()
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel(dz(dzb(K, b), a))
    return g


def fs_metric_inv(g=None):
    """Inverse FS metric g^{bbar a} (2x2).  Exact rational."""
    if g is None:
        g = fs_metric()
    return g.inv().applyfunc(cancel)


# the Kahler form coefficients g_{a bbar} closed-form (standard FS):
#   g_{a bbar} = (rho delta_{ab} - zbar_a z_b) / rho^2
def fs_metric_closed():
    rho = _rho()
    zb = [Z1B, Z2B]
    z = [Z1, Z2]
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel((rho * (1 if a == b else 0) - zb[a] * z[b]) / rho ** 2)
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
    id_at0 = (g0 == eye(2))
    ok &= _report("0.a FS metric g_{a bbar} = d_a d_bbar log(1+|z|^2) == closed form "
                  f"(rho dik - zbar_a z_b)/rho^2 [{metric_match}], == I_2 at z=0 [{id_at0}]",
                  metric_match and id_at0)

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


def main(run=("g0m",)):
    print("#" * 78)
    print("# tensor_probe.py -- v31.0-cand Phase 91 (Block B; exact over Q / Q(t))")
    print("#" * 78)
    res = {}
    if "g0m" in run:
        res["g0m"] = gate0_machinery()
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
