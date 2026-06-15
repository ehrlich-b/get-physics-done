#!/usr/bin/env python3
"""faithfulness_clamp.py -- Phase 96 / v36.0-candidate: THE FIELD-FAITHFULNESS CLAMP GATE.

A FRESH, self-contained driver (NOT a copy of any /tmp script; built directly from
derivations/96-faithfulness-clamp-RESEARCH.md).  The SINGLE residual gravity gate: every other
angle is closed (fiber dead across six kinds v17-v21; variety extremize FORCES-NOTHING v33; induce
CLOSES-CONDITIONAL v34; entanglement DEAD-FISHER v35).

THE CLAMP.  state-fp ==> metric-fp: the self-modeling-faithful matter profile is a critical point
of the gravitational action its own fluctuations induce -- delta F/delta M = 0 <=> delta Gamma/
delta M = 0.  We HAVE Gamma (v34: a_1 ~ Int R sqrt(g)).  The open object is F[M(x)] = the field-
level self-modeling FAITHFULNESS functional.  delta Gamma = G_munu - kappa T_munu is a CURVATURE
object (a Lichnerowicz/Laplacian operator on the profile -- the v33 eps=20 mode).  For the faithful
profile to extremize it, delta F must carry MATCHING base-derivative structure.

THE DECISIVE GATE (Gate 0).  Does field faithfulness (M(x) = phi[M](x) on the curved variety) carry
a genuine LOCAL base-derivative term (a Laplacian/Lichnerowicz operator on M, SAME TYPE as delta
Gamma), or does it collapse to the pointwise algebraic -Tr(h^2) Fisher form that is already dead?
The decisive NUMBER (exact over Q on CP^2) is the coefficient of the local base-derivative term in
L_F = delta(faithfulness)/delta M, computed from the phi-fixed-point condition ALONE (NO reference
to Int R -- Bug-guard 5 / NO-CIRCULARITY).

THE STRUCTURAL FORK (RESEARCH s2; the whole gate).  The phi-map's ONLY non-locality is the ENSEMBLE
EXPECTATION <l_i>_rho (read off nonlinear_iteration.py: F2 = det.sum(l_i - <l_i>_rho)^2,
F3 = det.sum l_i(l_i - <l_i>_rho); the faithful fixed point rho_J = det(sigma_2 - 1/3); faithful =
the I/3 center).  Promoting to a field gives three -- and only three -- readings of <.>:
  (1) POINTWISE       <.> at x's own reduced state => phi[M](x)=phi(M(x)); L_F pure algebraic
                      -Tr(h^2)-Hessian (Fisher/Bures); NO base derivative.  COLLAPSE.
  (2) GLOBAL mean     <.> = Int_base over the WHOLE base => L_F = (pointwise Hessian) - (rank-1
                      projector onto the global mean mode); a NONLOCAL integral operator, NOT a
                      local differential operator.  COLLAPSE (nonlocal).
  (3) LOCAL/geometric <.> uses an FS-kernel neighborhood average => COULD yield Delta_FS M; the
                      ONLY reading that PROCEEDS -- but only if the kernel is FORCED by the
                      variety's intrinsic structure (else fp-imported, Bug-guard 2).

VERDICT TAXONOMY (report exactly which one, exact over Q):
  DEAD-POINTWISE          -- L_F algebraic -Tr(h^2) (+ at most a nonlocal global-mean correction);
                             local-derivative coeff == 0; clamp FALSE; fork A PROVEN.
  DEAD-WRONG-DERIVATIVE   -- L_F carries a base derivative but the harmonic-map scalar box phi_M
                             (WRONG TYPE vs delta Gamma's Lichnerowicz operator); Gate 0 proceeds,
                             Gate 2 dead.
  ALIVE                   -- L_F carries the RIGHT (eps=20 Lichnerowicz tensor) derivative AND
                             delta F=0, delta Gamma=0 share critical points.
  ALIVE-THROUGH-GATE-3    -- ALIVE + matching pins kappa_ind (Lovelock => Einstein+Lambda) OR holds
                             for all kappa_ind (form-only).
  INCONCLUSIVE            -- the verdict flips between two equally-canonical field extensions.

THE 5 BUG-GUARDS (all checked before any PROCEED):
  1. DIRICHLET-TRAP        a base derivative that is box phi_M (harmonic-map) is the WRONG TYPE.
  2. IMPORTED-KERNEL       a local derivative appearing ONLY after a smoothing kernel => fp-imported
                           unless the kernel is FORCED by the intrinsic FS structure.
  3. FAITHFUL-POINT-MATTER-FREE  the faithful point is I/3 (matter-free); probe on STRUCTURED M!=0.
  4. WOO / DEMON-TEST 2.0  NO thermodynamics/horizons/coarse-graining/epistemic ensemble entropy.
  5. NO-CIRCULARITY        compute L_F from the phi-fixed-point ALONE; AST-guard the driver against
                           importing R/Ric/G/Delta_L into L_F itself.

DISCIPLINE: exact over Q on every decisive line (sympy.Rational/cancel/simplify; NEVER a float in a
verdict).  NO brute symbolic cancel/simplify/solve over a generic multi-parameter profile -- work
analytically + at RATIONAL POINTS (the s9 ground points).  Non-hardwired verdict() with the s7
self-tests (rigged controls print PASS BEFORE the real verdict).  Reproduce the certified anchors
(eps=20 Lichnerowicz; v35 A_ii==Var, G_M decomposition).  Commit after each gate.

FENCES (binding, verbatim -- see derivations/96-VERDICT.md s6): NO Einstein-equation / G=kT /
gravity / Newton / dark-matter / geodesic language as a DERIVED result; the bits<->area / induced-G
rate is a framework ratio, NOT Newton's G; FS is USED, not derived; signature Riemannian (Wall 2
unpaid -- NOTHING is called gravity until signature is paid); DEAD-* and ALIVE-* are NOT derivations
of gravity.  ALIVE is necessary-not-sufficient for gravity (Jaksland arXiv:2005.05055).  Does NOT
retract v33 (extremize), v34 (induce), v17-v21 (fiber kills), v23 (I/3 death), v35 (DEAD-FISHER).
Paper 5 remains the only result in the more-than-nothing column.

Reproducibility: sympy 1.14.0, Python 3.x, exact rational arithmetic over Q / Q(i) (no RNG / no
seeds in the verdict path; floats illustrative only).  Darwin arm64.
Run:  python3 -u code/faithfulness_clamp.py
"""
import ast as _ast
import os
import sys
import time

import sympy as sp
from sympy import Rational, Matrix, I, cancel, simplify, symbols, eye, zeros, expand

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return bool(ok)


def _hdr(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


# ============================================================================
# 1. THE WIRTINGER CHART ON CP^2 = h_3(C_u)  (reuse the v35 certified machinery)
# ----------------------------------------------------------------------------
# Affine chart v = (1, z1, z2); z and zbar INDEPENDENT Wirtinger symbols; conjugation = the
# z<->zbar SWAP (NEVER sympy conjugate() -- that silently breaks the Kahler identity).  We reuse
# the EXACT objects of area_per_bit.py / tensor_probe.py: P(z), <X,p>, X#, FS metric, phi_M, Var,
# G_M.  Built fresh here (self-contained) but byte-identical in form to the certified engines.
# ============================================================================
Z1, Z2 = symbols("z1 z2")
Z1B, Z2B = symbols("z1b z2b")
ZS = (Z1, Z2)
ZBS = (Z1B, Z2B)
_SWAP = {Z1: Z1B, Z1B: Z1, Z2: Z2B, Z2B: Z2}


def conj_swap(expr):
    """Complex conjugation on the Wirtinger chart: the z<->zbar SWAP on the independent symbols AND
    i -> -i on the genuine imaginary unit.  NEVER sympy conjugate() on the z symbols."""
    return expr.subs(_SWAP, simultaneous=True).subs(I, -I)


def rho():
    return 1 + Z1 * Z1B + Z2 * Z2B


def dz(f, a):
    return sp.diff(f, ZS[a])


def dzb(f, a):
    return sp.diff(f, ZBS[a])


def P_chart():
    """Rank-1 CP^2 projector P(z) = v v^H / (v^H v), v=(1,z1,z2); z->0 gives diag(1,0,0)=E11."""
    v = Matrix([1, Z1, Z2])
    vb = Matrix([1, Z1B, Z2B])
    denom = (vb.T * v)[0]
    return (v * vb.T / denom).applyfunc(cancel)


def inner(A, P):
    """Trace-form inner product <A,p> = Tr(A.P)."""
    return cancel(sp.expand((A * P).trace()))


def sharp(M):
    """Freudenthal adjoint M# = M^2 - Tr(M) M + sigma_2 I, sigma_2=((TrM)^2-Tr(M^2))/2."""
    s2 = cancel((M.trace() ** 2 - (M * M).trace()) / 2)
    return (M * M - M.trace() * M + s2 * eye(3)).applyfunc(cancel)


def phi_M(M, P=None):
    """phi_M(p) = <M,p> = Tr(M P(z)) (the v25 moment field; LINEAR in M)."""
    if P is None:
        P = P_chart()
    return inner(M, P)


def Var(M, P=None):
    """Quantum variance Var_p(M) = <M^2,p> - <M,p>^2 (the QGT-real / Fisher object; >= 0)."""
    if P is None:
        P = P_chart()
    return cancel(inner(M * M, P) - inner(M, P) ** 2)


def G_M(M, P=None):
    """The v26 second-order entropy response field G_M(p) = <M#,p> - (1/4)<M,p>^2 (<= 0)."""
    if P is None:
        P = P_chart()
    return cancel(inner(sharp(M), P) - Rational(1, 4) * inner(M, P) ** 2)


def fs_metric_pot():
    """g_pot_{a bbar} = d_a d_bbar log rho = (rho delta_{ab} - zbar_a z_b)/rho^2 (Fisher metric)."""
    K = sp.log(rho())
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel(dz(dzb(K, b), a))
    return g


def fs_metric_phys():
    """The engine/Boucetta PHYSICAL metric g_phys = g_pot/2 (the CERTIFIED normalization): Ric=6g,
    R=24, Lambda=6, scalar spectrum lambda_k = 4k(k+2) so lambda_1=12, lambda_2=32=lambda_L (the
    Lichnerowicz mode, eps = lambda_L - 2 Lambda = 20).  Used for the eigenvalue/Lichnerowicz
    anchors (the TYPE delta Gamma lives in).  The v35 A_ii==Var identity uses g_pot (Fisher); the
    overall scale is the single overall scale that does NOT decide the verdict."""
    g = fs_metric_pot()
    return (g / 2).applyfunc(cancel)


def fs_metric_inv(g):
    return g.inv().applyfunc(cancel)


def _gu(ginv, a, b):
    """g^{a bbar} = ginv[b,a] (the certified transpose pairing)."""
    return ginv[b, a]


def laplacian_scalar(f, g=None, ginv=None):
    """The analyst Laplacian Delta f = +2 g^{a bbar} d_a d_bbar f (negative-semidefinite; a lambda_1
    harmonic has Delta = -12, a lambda_2 harmonic Delta = -32).  The rough (geometer's) Laplacian
    nabla*nabla = -Delta is +12 / +32 respectively.  This is the local base-derivative TYPE."""
    if g is None:
        g = fs_metric_pot()
    if ginv is None:
        ginv = fs_metric_inv(g)
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += 2 * _gu(ginv, a, b) * dz(dzb(f, b), a)
    return cancel(s)


# ============================================================================
# 2. THE MATTER DIRECTIONS + the s9 de-risked ground points
# ============================================================================
def matter_directions():
    return {
        "s01": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
        "a01": Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
        "d1":  Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
        "gen": Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
    }


def P0_sub():
    # z1 = 1+2i, z2 = -1+i  => rho = 1 + 5 + 2 = 8
    return {Z1: 1 + 2 * I, Z1B: 1 - 2 * I, Z2: -1 + I, Z2B: -1 - I}


def P2_sub():
    # z1 = -1, z2 = 2-3i  => rho = 1 + 1 + 13 = 15
    return {Z1: -1, Z1B: -1, Z2: 2 - 3 * I, Z2B: 2 + 3 * I}


# ============================================================================
# verdict() -- NON-HARDWIRED ladder from computed booleans, with the s7 self-tests
# ----------------------------------------------------------------------------
# A DERIVED ladder; the branch taken is FORCED by the input flags (proven by the self-tests, which
# flip the verdict under synthetic inputs).  Returns one of
#   {DEAD-POINTWISE, DEAD-WRONG-DERIVATIVE, ALIVE, ALIVE-THROUGH-GATE-3, INCONCLUSIVE}.
# ============================================================================
def verdict(flags):
    """Map computed booleans to the Gate-0/clamp verdict (RESEARCH s0 taxonomy).

    flags keys (all booleans unless noted):
      extensions_agree       -- the canonical field extensions of the phi-fixed-point AGREE (else
                                INCONCLUSIVE; the two-non-agreeing-extensions guard).
      local_deriv_coeff_zero -- the DECISIVE NUMBER: the coefficient of the local base-derivative
                                (Laplacian) term in L_F is == 0 (only algebraic -Tr(h^2) + at most a
                                nonlocal global-mean correction).  True => DEAD-POINTWISE.
      kernel_is_forced       -- a local-derivative term, IF present, comes from a kernel FORCED by
                                the intrinsic FS structure (NOT an inserted smoothing; Bug-guard 2).
      deriv_is_lichnerowicz  -- the local-derivative term (if present and forced) is the eps=20
                                Lichnerowicz tensor operator (the RIGHT type vs delta Gamma).
      deriv_is_scalar_box    -- the local-derivative term is the harmonic-map scalar box phi_M
                                (Bug-guard 1, DIRICHLET-TRAP; the WRONG type).
      matching_pins_kappa    -- (only if ALIVE) the deltaF=deltaGamma match pins kappa_ind.
    """
    # Bug-guard / INCONCLUSIVE FIRST: a verdict that flips between canonical extensions is an artifact.
    if not flags.get("extensions_agree", False):
        return "INCONCLUSIVE"
    # the decisive coefficient: zero => the collapse (pointwise or nonlocal-global-mean).
    if flags.get("local_deriv_coeff_zero", False):
        return "DEAD-POINTWISE"
    # a nonzero local-derivative term exists.  Was it FORCED, or smuggled via an imported kernel?
    if not flags.get("kernel_is_forced", False):
        # an imported kernel => the native object collapsed and the derivative was smuggled (B-g 2).
        return "DEAD-POINTWISE"
    # forced local derivative present: which TYPE?
    if flags.get("deriv_is_scalar_box", False):
        return "DEAD-WRONG-DERIVATIVE"     # harmonic-map box phi_M (Bug-guard 1)
    if flags.get("deriv_is_lichnerowicz", False):
        # the RIGHT type AND forced => PROCEED.  Gate-3 split (kappa pinned vs form-only).
        return "ALIVE-THROUGH-GATE-3" if flags.get("matching_pins_kappa", False) else "ALIVE"
    # a forced local derivative of neither recognized type: cannot classify => INCONCLUSIVE.
    return "INCONCLUSIVE"


def verdict_self_tests():
    """The verdict() ladder MUST flip correctly under synthetic (rigged) inputs (RESEARCH s7):
      - rigged POINTWISE (<.> forced to the local state)        -> DEAD-POINTWISE
      - rigged LOCAL-LAPLACIAN (a forced eps=20 Lichnerowicz)   -> ALIVE/PROCEED (ladder CAN say alive)
      - rigged SCALAR-box (a hand-built harmonic-map box phi_M) -> DEAD-WRONG-DERIVATIVE (B-g 1 fires)
      - two NON-AGREEING extensions                             -> INCONCLUSIVE
    Plus the imported-kernel control (forced=False => DEAD-POINTWISE: a smuggled derivative)."""
    _hdr("verdict() SELF-TESTS (must all PASS before the real verdict; proves non-hardwired)")
    ok = True
    # (1) RIGGED POINTWISE: the decisive coefficient is zero by construction => DEAD-POINTWISE.
    v1 = verdict({"extensions_agree": True, "local_deriv_coeff_zero": True,
                  "kernel_is_forced": False, "deriv_is_lichnerowicz": False,
                  "deriv_is_scalar_box": False})
    ok &= _report(f"self-test rigged-POINTWISE (<.> local; coeff==0) -> {v1} (==DEAD-POINTWISE)",
                  v1 == "DEAD-POINTWISE")
    # (2) RIGGED LOCAL-LAPLACIAN: a FORCED eps=20 Lichnerowicz derivative => ALIVE (the ladder CAN
    #     say alive -- it is NOT rigged to kill).  + kappa-pinned variant => ALIVE-THROUGH-GATE-3.
    v2 = verdict({"extensions_agree": True, "local_deriv_coeff_zero": False,
                  "kernel_is_forced": True, "deriv_is_lichnerowicz": True,
                  "deriv_is_scalar_box": False, "matching_pins_kappa": False})
    v2k = verdict({"extensions_agree": True, "local_deriv_coeff_zero": False,
                   "kernel_is_forced": True, "deriv_is_lichnerowicz": True,
                   "deriv_is_scalar_box": False, "matching_pins_kappa": True})
    ok &= _report(f"self-test rigged-LOCAL-LAPLACIAN (forced eps=20) -> {v2}/{v2k} "
                  "(==ALIVE / ALIVE-THROUGH-GATE-3; the ladder CAN say alive)",
                  v2 == "ALIVE" and v2k == "ALIVE-THROUGH-GATE-3")
    # (3) RIGGED SCALAR-box: a FORCED harmonic-map box phi_M => DEAD-WRONG-DERIVATIVE (B-g 1 fires).
    v3 = verdict({"extensions_agree": True, "local_deriv_coeff_zero": False,
                  "kernel_is_forced": True, "deriv_is_lichnerowicz": False,
                  "deriv_is_scalar_box": True})
    ok &= _report(f"self-test rigged-SCALAR-box (forced box phi_M) -> {v3} "
                  "(==DEAD-WRONG-DERIVATIVE; Bug-guard 1 fires)", v3 == "DEAD-WRONG-DERIVATIVE")
    # (4) two NON-AGREEING extensions -> INCONCLUSIVE.
    v4 = verdict({"extensions_agree": False, "local_deriv_coeff_zero": True,
                  "kernel_is_forced": False, "deriv_is_lichnerowicz": False,
                  "deriv_is_scalar_box": False})
    ok &= _report(f"self-test two NON-AGREEING extensions -> {v4} (==INCONCLUSIVE)",
                  v4 == "INCONCLUSIVE")
    # (5) IMPORTED-KERNEL control: a nonzero derivative but NOT forced => DEAD-POINTWISE (smuggled).
    v5 = verdict({"extensions_agree": True, "local_deriv_coeff_zero": False,
                  "kernel_is_forced": False, "deriv_is_lichnerowicz": True,
                  "deriv_is_scalar_box": False})
    ok &= _report(f"self-test IMPORTED-KERNEL (deriv present but NOT forced) -> {v5} "
                  "(==DEAD-POINTWISE; Bug-guard 2: a smuggled derivative is the collapse)",
                  v5 == "DEAD-POINTWISE")
    # non-hardwired demonstration: the SAME function returned >=4 distinct verdicts.
    distinct = {v1, v2, v2k, v3, v4, v5}
    ok &= _report(f"verdict() is NON-HARDWIRED: produced {sorted(distinct)} under synthetic inputs "
                  "(it flips with the flags, not a constant)", len(distinct) >= 4)
    print(f"\n  SELF-TESTS: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ============================================================================
# ANCHORS -- reproduce the certified objects (the s7/s9 sanity floor; exact over Q)
# ----------------------------------------------------------------------------
def anchors():
    """Reproduce the certified anchors EXACT over Q (RESEARCH s9, the sanity floor):
      - eps = lambda_L - 2 Lambda = 32 - 12 = 20 (the Lichnerowicz mode; the TYPE delta Gamma lives
        in).  The Lambda=6 (FS Ric=6g) and the lambda_L=32 (= the lambda_2 scalar eigenvalue level,
        reproduced HERE cheaply via the scalar Laplacian on a degree-2 harmonic) are the two pieces.
      - v35 identities: A_ii == Var (the FS metric-trace of dphi_M = the quantum Fisher), and the
        G_M decomposition G_M = Var + 3/4 <M>^2 - 1/2 Tr M^2 (numeric at the s9 ground points).
      - the s9 off-faithful ground points (Var, G_M genuinely VARY => non-vacuous off-faithful)."""
    _hdr("ANCHORS -- certified objects (eps=20 Lichnerowicz; v35 identities; s9 ground points)")
    ok = True
    P = P_chart()
    dirs = matter_directions()
    g = fs_metric_pot(); ginv = fs_metric_inv(g)
    # the PHYSICAL metric (g_pot/2) carries the certified eps=20 normalization (lambda_1=12, etc.):
    gph = fs_metric_phys(); ginvph = fs_metric_inv(gph)

    # --- eps = 20: Lambda=6, lambda_L=32 (the lambda_2 scalar level reproduced cheaply) ---
    Lambda = Rational(6)            # FS Kahler-Einstein Ric = 6g, R = 24, Lambda_geo = 6
    # the lambda_1 scalar eigenvalue (rough Laplacian) on phi_M (a degree-1 harmonic): +12.
    phi_d1 = phi_M(dirs["d1"], P)
    lam1 = cancel(-laplacian_scalar(phi_d1, gph, ginvph) / phi_d1)    # rough = -analyst; == +12
    ok &= _report("scalar lambda_1 = 12 on phi_M (a degree-1 FS harmonic; rough Laplacian "
                  "nabla*nabla phi = +12 phi; PHYSICAL metric Ric=6g) [exact Q]", lam1 == 12)
    # the lambda_2 scalar eigenvalue (rough Laplacian) on a degree-2 harmonic: +32 == lambda_L.
    f2 = cancel(Z1 ** 2 * Z2B ** 2 / rho() ** 2)                      # a (2,-2) degree-2 harmonic
    lam2 = cancel(-laplacian_scalar(f2, gph, ginvph) / f2)
    lambda_L = lam2
    ok &= _report("scalar lambda_2 = 32 on a degree-2 FS harmonic (== lambda_L, the Lichnerowicz "
                  "eigenvalue level; rough Laplacian +32) [exact Q]", lam2 == 32)
    eps = cancel(lambda_L - 2 * Lambda)
    ok &= _report("eps = lambda_L - 2 Lambda = 32 - 12 = 20 (the v33 eps=20 Lichnerowicz mode; the "
                  "TYPE delta Gamma lives in -- the object L_F must MATCH to proceed) [exact Q]",
                  eps == 20)

    # --- v35 identity A_ii == Var at the s9 ground point d1@P0 (== 1/2) ---
    # A_ii = g^{a bbar} d_a phi d_bbar phi (the metric-TRACE of the metric mode dphi_M).
    def A_ii(M):
        phi = phi_M(M, P)
        s = sp.Integer(0)
        for a in range(2):
            for b in range(2):
                s += _gu(ginv, a, b) * dz(phi, a) * dzb(phi, b)
        return cancel(s)
    a2 = cancel(A_ii(dirs["d1"]).subs(P0_sub()))
    vv = cancel(Var(dirs["d1"], P).subs(P0_sub()))
    ok &= _report(f"v35 anchor: A_ii(d1@P0) = {a2} == Var(d1@P0) = {vv} (== 1/2; the canonical FS "
                  "area IS the quantum Fisher -- the v35 DEAD-FISHER object) [exact Q]",
                  a2 == Rational(1, 2) and vv == Rational(1, 2) and a2 == vv)

    # --- the G_M decomposition G_M = Var + 3/4<M>^2 - 1/2 Tr M^2 at the s9 ground points ---
    dec_ok = True
    gp_tbl = []
    for (dn, sub, subnm) in [("d1", P0_sub(), "P0"), ("d1", P2_sub(), "P2"),
                             ("s01", P0_sub(), "P0"), ("gen", P0_sub(), "P0")]:
        M = dirs[dn]
        phi = cancel(phi_M(M, P).subs(sub))
        var = cancel(Var(M, P).subs(sub))
        gm = cancel(G_M(M, P).subs(sub))
        TrM2 = cancel((M * M).trace())
        rhs = cancel(var + Rational(3, 4) * phi ** 2 - Rational(1, 2) * TrM2)
        dec_ok &= (cancel(gm - rhs) == 0)
        gp_tbl.append((dn, subnm, var, gm))
    for (dn, sn, var, gm) in gp_tbl:
        print(f"      {dn}@{sn}: Var={var}, G_M={gm}")
    ok &= _report("v35 G_M decomposition G_M = Var + 3/4<M>^2 - 1/2 Tr M^2 holds at all 4 s9 ground "
                  "points (G_M genuinely VARIES => non-vacuous off-faithful; Bug-guard 3) [exact Q]",
                  dec_ok)

    # --- s9 ground-point values (the exact-over-Q de-risk table) ---
    g_P0 = cancel(G_M(dirs["d1"], P).subs(P0_sub()))
    g_P2 = cancel(G_M(dirs["d1"], P).subs(P2_sub()))
    ok &= _report("s9 ground points reproduce EXACTLY: d1@P0 Var=1/2,G_M=-5/16; d1@P2 Var=2/15,"
                  "G_M=-13/15 [exact Q]",
                  cancel(Var(dirs["d1"], P).subs(P0_sub())) == Rational(1, 2)
                  and g_P0 == Rational(-5, 16)
                  and cancel(Var(dirs["d1"], P).subs(P2_sub())) == Rational(2, 15)
                  and g_P2 == Rational(-13, 15))

    print(f"\n  ANCHORS: {'ALL PASS' if ok else 'FAIL'}")
    return ok, {"eps": eps, "Lambda": Lambda, "lambda_L": lambda_L}


# ============================================================================
# placeholder for the gate functions (built incrementally; committed per gate)
# ============================================================================
def main():
    print("#" * 80)
    print("# faithfulness_clamp.py -- Phase 96 / v36.0-candidate: THE FIELD-FAITHFULNESS CLAMP")
    print("# (exact over Q; CP^2 = h_3(C_u); the single un-run gravity gate)")
    print("#" * 80)

    # ---- verdict() self-tests FIRST (must pass before any real verdict) ----
    if not verdict_self_tests():
        print("\n*** verdict() SELF-TESTS FAILED -- the ladder is broken; STOP. ***")
        return 1

    # ---- certified anchors (the sanity floor) ----
    a_ok, anc = anchors()
    if not a_ok:
        print("\n*** ANCHORS FAILED -- the certified objects did not reproduce; STOP. ***")
        return 1

    print(f"\n[{time.time() - _t0:6.1f}s] scaffold + self-tests + anchors PASS: {sum(PASS)}/{len(PASS)}")
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    sys.exit(main())



if __name__ == "__main__":
    sys.exit(main())
