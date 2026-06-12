#!/usr/bin/env python3
"""tensor_probe_indep_check.py -- ADVERSARIAL THIRD PATH (path 3) for Phase 91 (v31.0-cand).

GOAL: REFUTE the executor's LIVE verdict (B3 = dphi_M (x) dphi_M has a nonzero TT-residue).
The LIVE rests on york_solve(B3) INCONSISTENT over the CERTIFIED gauge ansatz
{delta*(phi_A dphi_B)} + conformal {phi_A phi_B . g} while the B1=grad-grad-phi control IS
consistent.  We try HARD to break it: solve B3 = delta*omega + f.g with the MOST GENERAL omega
possible (general polynomial of degree D in (z1,z2,z1b,z2b) over rho^k, undetermined Q coeffs,
matched-monomial linsolve -- NEVER `cancel` on raw fields).  Push D up until the B1 Hessian control
is comfortably solved, and check whether B3 EVER becomes consistent.

  B3 solves at some D  => REFUTED (DEAD: a missing longitudinal generator was found).
  B3 stays inconsistent while B1 solves, degree-stable => LIVE corroborated (no door found).

This file builds delta* and the metric INDEPENDENTLY from tensor_probe's closed forms (geometry
cross-check) but reuses tensor_probe's exact rational fields for the targets (so we test the SAME
B3).  Exact over Q.  ANTI-STALL: short runs, progress prints, matched-monomial/point-eval only.

FENCE (binding): no Einstein / G=kT / Newton / geodesic; Block C not claimed.  We only test
whether B3 is or is not pure gauge+conformal.

RESULT (this run): FAILED TO REFUTE -> LIVE CORROBORATED.  Across a fully-general omega
(deg D=2..7, rho-power kw=kf in {1,2,3,4}; up to 1650 undetermined Q coeffs), B3 is INCONSISTENT
at every (D,kw) where the B1 Hessian control SOLVES; no missing longitudinal generator exists.
Symbolic-M (8-param traceless cut) and several dense rational M all agree.  The dimension_audit
B1_deficit=1-on-dense-M is a SAMPLING-RANK artifact (too few points / off-slice rank saturation),
NOT a real span gap -- the exact matched-monomial york_solve(B1)=CONSISTENT on dense M (no sampling).
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                       # noqa: E402
from sympy import Rational, symbols, cancel, expand, I, Matrix, eye, zeros, together  # noqa: E402

import tensor_probe as TP                                               # noqa: E402

_t0 = time.time()


def _log(m):
    print(f"[{time.time() - _t0:7.1f}s] {m}", flush=True)


Z1, Z2 = TP.Z1, TP.Z2
Z1B, Z2B = TP.Z1B, TP.Z2B
ALLV = (Z1, Z2, Z1B, Z2B)


def _rho():
    return 1 + Z1 * Z1B + Z2 * Z2B


# ============================================================================
# INDEPENDENT geometry (closed-form FS metric, holomorphic Christoffels, delta*).
# Built from scratch (NOT calling TP.delta_star) so the gauge mechanics is cross-checked.
# Physical normalization g_phys = (1/2) g_pot (matches TP.MET_SCALE) -- but the verdict
# (TT zero/nonzero) is scale-free, so the overall 1/2 is irrelevant to consistency.
# ============================================================================
MET = Rational(1, 2)


def metric():
    rho = _rho()
    z = [Z1, Z2]; zb = [Z1B, Z2B]
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel(MET * (rho * (1 if a == b else 0) - zb[a] * z[b]) / rho ** 2)
    return g


def metric_inv(g=None):
    if g is None:
        g = metric()
    return g.inv().applyfunc(cancel)


def dz(f, a):
    return sp.diff(f, ALLV[a])


def dzb(f, a):
    return sp.diff(f, ALLV[2 + a])


def christoffel_hol(g=None, ginv=None):
    """Gamma^c_{ab} = g^{c dbar} d_a g_{b dbar} = sum_d ginv[d,c] d_a g[b,d]."""
    if g is None:
        g = metric()
    if ginv is None:
        ginv = metric_inv(g)
    Gam = [[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)]
    for c in range(2):
        for a in range(2):
            for b in range(2):
                s = sp.Integer(0)
                for d in range(2):
                    s += ginv[d, c] * dz(g[b, d], a)
                Gam[c][a][b] = cancel(s)
    return Gam


def christoffel_antihol(g=None, ginv=None):
    if g is None:
        g = metric()
    if ginv is None:
        ginv = metric_inv(g)
    Gam = [[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)]
    for c in range(2):
        for a in range(2):
            for b in range(2):
                s = sp.Integer(0)
                for d in range(2):
                    s += ginv[c, d] * dzb(g[d, b], a)
                Gam[c][a][b] = cancel(s)
    return Gam


def delta_star(om_hol, om_ahol, g=None, ginv=None, Gam=None, GamB=None, simp=together):
    """(delta* omega)_{mu nu} = 1/2(nabla_mu om_nu + nabla_nu om_mu).  Kahler complex blocks
    (W20,W11,W02).  Independent rebuild of TP.delta_star."""
    if g is None:
        g = metric()
    if ginv is None:
        ginv = metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = christoffel_antihol(g, ginv)
    W20 = zeros(2, 2); W11 = zeros(2, 2); W02 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            t = Rational(1, 2) * (dz(om_hol[b], a) + dz(om_hol[a], b))
            for c in range(2):
                t -= Gam[c][a][b] * om_hol[c]
            W20[a, b] = simp(t)
            W11[a, b] = simp(Rational(1, 2) * (dz(om_ahol[b], a) + dzb(om_hol[a], b)))
            t2 = Rational(1, 2) * (dzb(om_ahol[b], a) + dzb(om_ahol[a], b))
            for c in range(2):
                t2 -= GamB[c][a][b] * om_ahol[c]
            W02[a, b] = simp(t2)
    return W20, W11, W02


def conformal_block(f, g=None, simp=together):
    if g is None:
        g = metric()
    Z = zeros(2, 2)
    return Z, (f * g).applyfunc(simp), Z


# ============================================================================
# GEOMETRY CROSS-CHECK: my independent metric/delta* == tensor_probe's.
# ============================================================================
def geometry_crosscheck():
    _log("geometry cross-check: my metric & delta* == tensor_probe ...")
    g = metric(); gtp = TP.fs_metric()
    mok = all(cancel(g[a, b] - gtp[a, b]) == 0 for a in range(2) for b in range(2))
    # delta*(d phi) on a sample scalar == TP
    phi = cancel(TP.phi_field(Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])))
    omh = [dz(phi, a) for a in range(2)]; oma = [dzb(phi, a) for a in range(2)]
    W = delta_star(omh, oma, simp=cancel)
    Wtp = TP.delta_star_of_dphi(phi, simp=cancel)
    dok = all(cancel(W[k][a, b] - Wtp[k][a, b]) == 0
              for k in range(3) for a in range(2) for b in range(2))
    print(f"  metric match: {mok}; delta*(dphi) match: {dok}", flush=True)
    return mok and dok


# ============================================================================
# THE GENERAL-OMEGA YORK SOLVER.  omega_a, omega_abar = (general polynomial of degree D in
# z1,z2,z1b,z2b) / rho^k ; f = (general poly degree Df)/rho^kf.  All coeffs undetermined over Q.
# Solve target = delta*omega + f.g by matched-monomial linsolve on numerators over a common
# rho-power.  NEVER `cancel` on raw symbolic-coefficient fields -- we build numerator polys and
# match coefficients (the only safe, stall-proof route).
#
# DEGREE-SUFFICIENCY note: a function p/rho^j with deg(p)<=d equals (p rho^{kw-j})/rho^kw with
# numerator degree <= d + 2(kw-j).  So {poly_D / rho^kw} is a SUPERSET of every {poly_d/rho^j :
# j<=kw, d<=D-2(kw-j)}.  Fixing a high kw and growing D therefore sweeps ALL lower (degree,power)
# omega forms simultaneously.  The B1 control's true omega=dphi (phi~deg1/rho) is deg2/rho^2, i.e.
# poly_{2+2(kw-2)}/rho^kw -- it FIRST appears at D=2+2(kw-2)=2kw-2 (D=6 at kw=4; D=2 at kw=2).
# We require B1 to SOLVE before reading B3's verdict at that (D,kw).
# ============================================================================
def _monomials(D):
    """All monomials z1^a z2^b z1b^c z2b^d with a+b+c+d <= D.  Returns list of (a,b,c,d)."""
    out = []
    for tot in range(D + 1):
        for a in range(tot + 1):
            for b in range(tot - a + 1):
                for c in range(tot - a - b + 1):
                    d = tot - a - b - c
                    out.append((a, b, c, d))
    return out


def _poly_from(coeffs, monos):
    """sum coeffs[i] * z1^a z2^b z1b^c z2b^d."""
    e = sp.Integer(0)
    for ci, (a, b, c, d) in zip(coeffs, monos):
        e += ci * Z1 ** a * Z2 ** b * Z1B ** c * Z2B ** d
    return e


def general_york_solve(target_blocks, D, kw=2, kf=2, g=None, ginv=None, Gam=None, GamB=None,
                       label=""):
    """Solve target = delta*omega + f.g with omega = (deg<=D poly)/rho^kw (per component:
    om_hol[0],om_hol[1],om_ahol[0],om_ahol[1]) and f = (deg<=D poly)/rho^kf, undetermined Q coeffs.
    Returns (consistent, n_unknowns, n_eqs).

    Matched-monomial route: build delta*omega + f.g symbolically in the coeffs (rational in z,zbar
    with rho denominators), subtract target, bring each block entry over a common denominator,
    require every (z,zbar)-monomial coeff of the numerator (linear in the unknowns) to vanish.
    linsolve over Q."""
    if g is None:
        g = metric()
    if ginv is None:
        ginv = metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = christoffel_antihol(g, ginv)
    monos = _monomials(D)
    nm = len(monos)
    rho = _rho()
    cwh = [list(symbols(f"wh{ax}_0:{nm}")) for ax in range(2)]
    cwa = [list(symbols(f"wa{ax}_0:{nm}")) for ax in range(2)]
    cf = list(symbols(f"ff_0:{nm}"))
    om_hol = [_poly_from(cwh[ax], monos) / rho ** kw for ax in range(2)]
    om_ahol = [_poly_from(cwa[ax], monos) / rho ** kw for ax in range(2)]
    fexpr = _poly_from(cf, monos) / rho ** kf
    allc = cwh[0] + cwh[1] + cwa[0] + cwa[1] + cf
    _log(f"  [{label}] D={D} kw={kw} kf={kf}: {len(allc)} unknowns; building delta*omega+f.g ...")
    W = delta_star(om_hol, om_ahol, g, ginv, Gam, GamB, simp=together)
    Cf = conformal_block(fexpr, g, simp=together)
    eqs = set()
    for k in range(3):
        for a in range(2):
            for b in range(2):
                diff = together(target_blocks[k][a, b] - W[k][a, b] - Cf[k][a, b])
                num, den = sp.fraction(diff)
                num = expand(num)
                P = sp.Poly(num, Z1, Z2, Z1B, Z2B)
                for co in P.coeffs():
                    co = expand(co)
                    if co != 0:
                        eqs.add(co)
        _log(f"  [{label}] D={D}: block k={k} done, |eqs|={len(eqs)}")
    eqs = [e for e in eqs if e != 0]
    _log(f"  [{label}] D={D}: linsolve {len(eqs)} eqs in {len(allc)} unknowns ...")
    sol = sp.linsolve(eqs, allc)
    consistent = len(sol) > 0
    _log(f"  [{label}] D={D}: CONSISTENT={consistent}  (eqs={len(eqs)}, unk={len(allc)})")
    return consistent, len(allc), len(eqs)


# ============================================================================
# The targets: B3 = dphi (x) dphi and the B1 = grad-grad-phi control.  Built from
# tensor_probe's exact fields (same objects the executor tested).
# ============================================================================
def B3_target(Mcx):
    phi = cancel(TP.phi_field(Mcx))
    return TP.grad_bilinear(phi, simp=together)


def B1_control(Mcx, g=None, ginv=None):
    phi = cancel(TP.phi_field(Mcx))
    return TP.cov_hessian(phi, g, ginv, simp=together)


# ============================================================================
# INDEPENDENT DIMENSION AUDIT (modular point-rank).  Diagnoses the orchestrator's claim that
# TP.dimension_audit gives a FALSE B1_deficit=1 on dense M.  We build the COMPLETE gauge+conformal
# span (delta*(phi_A dphi_B) holo+antiholo + conformal phi_A phi_B . g) from OUR delta*, evaluate at
# off-slice rational points, take modular rank.  We then test deficit STABILITY vs npts/point-set --
# the reliability question.  With z,zbar INDEPENDENT random rationals the field is already real (no
# Wirtinger conjugacy), so sp.im(...) of a real-substituted block is the matter's I-content only.
# ============================================================================
_PRIMES = (2147483647, 2147483629, 4294967291)


def _tofrac(x):
    x = sp.nsimplify(x)
    return (int(sp.numer(x)), int(sp.denom(x)))


def _modrank(rows, P):
    M = [[(num % P) * pow(den % P, P - 2, P) % P for (num, den) in r] for r in rows]
    m = len(M); nn = len(M[0]) if m else 0; rank = 0
    for col in range(nn):
        piv = None
        for r in range(rank, m):
            if M[r][col] % P != 0:
                piv = r; break
        if piv is None:
            continue
        M[rank], M[piv] = M[piv], M[rank]
        inv = pow(M[rank][col], P - 2, P); M[rank] = [(x * inv) % P for x in M[rank]]
        for r in range(m):
            if r != rank and M[r][col] % P != 0:
                ff = M[r][col]; M[r] = [(M[r][i] - ff * M[rank][i]) % P for i in range(nn)]
        rank += 1
        if rank == m:
            break
    return rank


def _span_rows(pts, g, ginv, Gam, GamB):
    """Rows of the COMPLETE gauge+conformal image evaluated at pts (re+im per entry)."""
    phis = [(nm, cancel(TP.phi_A(A))) for nm, A in (TP._herm_basis_3() + [("id", eye(3))])]

    def vec_of(tb):
        out = []
        for pp in pts:
            for k in range(3):
                for a in range(2):
                    for b in range(2):
                        e = cancel(tb[k][a, b].subs(pp))
                        out.append(_tofrac(sp.re(e))); out.append(_tofrac(sp.im(e)))
        return out
    gauge = []
    for nA, pA in phis:
        for nB, pB in phis:
            omh = [together(pA * dz(pB, 0)), together(pA * dz(pB, 1))]
            gauge.append(delta_star(omh, [sp.Integer(0)] * 2, g, ginv, Gam, GamB, simp=together))
            oma = [together(pA * dzb(pB, 0)), together(pA * dzb(pB, 1))]
            gauge.append(delta_star([sp.Integer(0)] * 2, oma, g, ginv, Gam, GamB, simp=together))
    conf = [conformal_block(together(pA * pB), g, simp=together) for nA, pA in phis for nB, pB in phis]
    return [vec_of(t) for t in gauge + conf], vec_of


def indep_audit(Mcx, npts=30, seed=7, offslice=True, g=None, ginv=None, Gam=None, GamB=None):
    """Independent dimension audit.  offslice=True: z,zbar independent (correct); False: z=zbar
    (the diagnosed aliasing slice).  Returns dict with dim_span, b1_deficit, b3_deficit per prime."""
    import random
    if g is None:
        g = metric()
    if ginv is None:
        ginv = metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = christoffel_antihol(g, ginv)
    rng = random.Random(seed)

    def rr():
        return Rational(rng.randint(-11, 11), rng.randint(1, 11))
    pts = []
    for _ in range(npts):
        z1, z2 = rr(), rr()
        if offslice:
            pts.append({Z1: z1, Z2: z2, Z1B: rr(), Z2B: rr()})
        else:
            pts.append({Z1: z1, Z2: z2, Z1B: z1, Z2B: z2})       # reality slice z=zbar (aliasing)
    rows, vec_of = _span_rows(pts, g, ginv, Gam, GamB)
    phi = cancel(TP.phi_field(Mcx))
    B1 = TP.cov_hessian(phi, g, ginv, simp=together)
    B3 = TP.grad_bilinear(phi, simp=together)
    b1v = vec_of(B1); b3v = vec_of(B3)
    out = {"npts": npts, "offslice": offslice}
    rS = [_modrank(rows, P) for P in _PRIMES]
    rB1 = [_modrank(rows + [b1v], P) for P in _PRIMES]
    rB3 = [_modrank(rows + [b3v], P) for P in _PRIMES]
    out["dim_span"] = rS
    out["b1_deficit"] = [rB1[i] - rS[i] for i in range(len(_PRIMES))]
    out["b3_deficit"] = [rB3[i] - rS[i] for i in range(len(_PRIMES))]
    return out


# ============================================================================
# SYMBOLIC-M test.  Instead of a rational instance, carry the matter's 8 real params as SYMBOLS.
# We test whether B3(M) is gauge+conformal for GENERIC M by the matched-monomial york_solve with
# the field built from a symbolic M.  (Heavier: the numerator coeffs are polynomials in the m-params
# AND the unknown omega coeffs.  We keep D small -- the executor's effective degree -- to stay
# tractable, and confirm INCONSISTENCY is an identity in the m-params, not an instance accident.)
# ============================================================================
def symbolic_M_solve(D=2, kw=2, kf=2):
    """york_solve(B3) and york_solve(B1) for a SYMBOLIC traceless cut M (8 real params).  Returns
    (b1_consistent, b3_consistent)."""
    g = metric(); ginv = metric_inv(g)
    Gam = christoffel_hol(g, ginv); GamB = christoffel_antihol(g, ginv)
    Msym, s = TP.Mmat_cut_cx("q")
    phi = cancel(TP.phi_field(Msym))
    _log(f"symbolic-M: building B1, B3 for 8-param M (deg D={D}) ...")
    B1 = TP.cov_hessian(phi, g, ginv, simp=together)
    B3 = TP.grad_bilinear(phi, simp=together)
    c1, _, _ = general_york_solve(B1, D=D, kw=kw, kf=kf, g=g, ginv=ginv, Gam=Gam, GamB=GamB,
                                  label="B1-sym")
    c3, _, _ = general_york_solve(B3, D=D, kw=kw, kf=kf, g=g, ginv=ginv, Gam=Gam, GamB=GamB,
                                  label="B3-sym")
    return c1, c3


# ============================================================================
# DRIVERS
# ============================================================================
def run_sweep(Mcx, label, Dlist, kw, kf):
    """General-omega sweep over Dlist at fixed (kw,kf) for B1 control + B3.  Returns list of
    (D, b1_consistent, b3_consistent)."""
    g = metric(); ginv = metric_inv(g)
    Gam = christoffel_hol(g, ginv); GamB = christoffel_antihol(g, ginv)
    B1 = B1_control(Mcx, g, ginv)
    B3 = B3_target(Mcx)
    res = []
    for D in Dlist:
        print(f"########## [{label}] D={D} kw={kw} kf={kf} ##########", flush=True)
        c1, _, _ = general_york_solve(B1, D=D, kw=kw, kf=kf, g=g, ginv=ginv, Gam=Gam, GamB=GamB,
                                      label=f"{label}.B1")
        c3, _, _ = general_york_solve(B3, D=D, kw=kw, kf=kf, g=g, ginv=ginv, Gam=Gam, GamB=GamB,
                                      label=f"{label}.B3")
        res.append((D, c1, c3))
        print(f">>> [{label}] D={D} kw={kw} kf={kf}: B1={c1} B3={c3}", flush=True)
    return res


def exact_york_on_dense_M():
    """The audit-reliability core: exact matched-monomial york_solve(B1) on DENSE M (no sampling).
    If CONSISTENT, the TP.dimension_audit B1_deficit=1-on-dense-M is a sampling artifact, not a
    real span gap."""
    g = metric(); ginv = metric_inv(g)
    Gam = christoffel_hol(g, ginv); GamB = christoffel_antihol(g, ginv)
    Mden = TP._M_rat()
    Mden2 = TP._M_rat2()
    out = {}
    for nm, Mc in [("dense1", Mden), ("dense2", Mden2)]:
        B1 = B1_control(Mc, g, ginv)
        B3 = B3_target(Mc)
        c1, _, _ = general_york_solve(B1, D=2, kw=2, kf=2, g=g, ginv=ginv, Gam=Gam, GamB=GamB,
                                      label=f"{nm}.B1")
        c3, _, _ = general_york_solve(B3, D=2, kw=2, kf=2, g=g, ginv=ginv, Gam=Gam, GamB=GamB,
                                      label=f"{nm}.B3")
        out[nm] = (c1, c3)
        print(f">>> EXACT york on {nm}: B1 consistent={c1}, B3 consistent={c3}", flush=True)
    return out


if __name__ == "__main__":
    print("#" * 78)
    print("# tensor_probe_indep_check.py -- ADVERSARIAL refutation of LIVE (Phase 91)")
    print("#" * 78)
    arg = sys.argv[1] if len(sys.argv) > 1 else "xcheck"
    Msp = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])

    if arg == "xcheck":
        ok = geometry_crosscheck()
        print(f"\nGEOMETRY CROSS-CHECK: {'PASS' if ok else 'FAIL'}")

    elif arg == "sweep2":            # kw=kf=2, D=2..4 (executor's natural power)
        run_sweep(Msp, "sparse_kw2", [2, 3, 4], kw=2, kf=2)

    elif arg == "sweep4":            # kw=kf=4 superset, D=4..7 (contains all lower power/degree)
        run_sweep(Msp, "sparse_kw4", [4, 5, 6, 7], kw=4, kf=4)

    elif arg == "denseaudit":        # exact york on dense M (the audit-reliability check)
        exact_york_on_dense_M()

    elif arg == "modaudit":          # independent modular audit, vary npts + on/off slice
        g = metric(); ginv = metric_inv(g)
        Gam = christoffel_hol(g, ginv); GamB = christoffel_antihol(g, ginv)
        Mden = TP._M_rat()
        for npts in (20, 30, 45, 70):
            a = indep_audit(Mden, npts=npts, offslice=True, g=g, ginv=ginv, Gam=Gam, GamB=GamB)
            print(f">>> dense off-slice npts={npts}: dim={a['dim_span']} b1_def={a['b1_deficit']} "
                  f"b3_def={a['b3_deficit']}", flush=True)
        a0 = indep_audit(Msp, npts=45, offslice=True, g=g, ginv=ginv, Gam=Gam, GamB=GamB)
        print(f">>> sparse off-slice npts=45: dim={a0['dim_span']} b1_def={a0['b1_deficit']} "
              f"b3_def={a0['b3_deficit']}", flush=True)

    elif arg == "aliasing":          # on-slice (z=zbar) vs off-slice: confirm the executor's call
        g = metric(); ginv = metric_inv(g)
        Gam = christoffel_hol(g, ginv); GamB = christoffel_antihol(g, ginv)
        for off in (False, True):
            a = indep_audit(Msp, npts=45, offslice=off, g=g, ginv=ginv, Gam=Gam, GamB=GamB)
            tag = "OFF-slice (z,zbar indep)" if off else "ON-slice (z=zbar, ALIASING)"
            print(f">>> {tag}: dim={a['dim_span']} b1_def={a['b1_deficit']} "
                  f"b3_def={a['b3_deficit']}", flush=True)

    elif arg == "symbolicM":         # symbolic 8-param M
        c1, c3 = symbolic_M_solve(D=2, kw=2, kf=2)
        print(f"\n>>> SYMBOLIC-M (8 params) D=2: B1 consistent={c1}, B3 consistent={c3}")

    else:
        print(f"unknown arg {arg!r}; use: xcheck|sweep2|sweep4|denseaudit|modaudit|aliasing|symbolicM")
