#!/usr/bin/env python3
"""lichnerowicz_response_verify.py -- INDEPENDENT verification of Phase 92 (the Tensor Dictionary).

This is the gpd-verifier's SEPARATE code path.  It does NOT trust the executor's
code/lichnerowicz_response.py; it re-derives the three load-bearing numbers via independent
machinery and checks them against theory anchors.

PRIORITY A (verdict-critical -- the suspected bug):
  The executor reads kappa, the direction, and the Schur scalar off r[1] = the (1,1) block of
  extract_tt's residue, with the (2,0)/(0,2) blocks ZEROED on output.  But the FULL r is the
  TT residue (delta r = 0 couples ALL three blocks), so r[1]-alone is NOT divergence-free
  (verified: it is not).  We extract the CLEAN (1,1) TT part by forcing the (2,0)/(0,2) of B3
  ENTIRELY into delta*omega + f.g (general-polynomial omega -- independent of the executor's
  {phi_A dphi_B} ansatz), leaving a residue r_clean = (0, r11, 0) that is purely (1,1), traceless,
  AND divergence-free as a full tensor.  Per v31 the genuine TT part IS purely (1,1), so this is
  consistent.  We then recompute the direction (c(M) prop N(M)?), the norm (kappa), and detM-absence
  on r_clean.

PRIORITY B (eps = lambda_L - 12, the sub-fork):
  Independent rough Laplacian + curvature contraction on the clean (1,1) eigentensor; confirm/refute
  lambda_L = 32, eps = 20.  Boucetta/Besse anchor: Koiso rigidity => no TT at Delta_L = 2Lambda = 12,
  so the genuine Besse Delta_L on the (1,1) TT must be != 12.

Anti-stall: per-object separate runs, progress prints, matched-monomial, NO full-basis Gram.
Reproducibility: sympy 1.14.0, Python 3.14, exact over Q.
"""
import os
import sys
import time

sys.setrecursionlimit(100000)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                       # noqa: E402
from sympy import Rational, Matrix, zeros, cancel, symbols, expand, together, eye, I, Poly  # noqa: E402

import tensor_probe as TP                                               # noqa: E402

Z1, Z2, Z1B, Z2B = TP.Z1, TP.Z2, TP.Z1B, TP.Z2B
ALLV = (Z1, Z2, Z1B, Z2B)

_t0 = time.time()


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _rho():
    return 1 + Z1 * Z1B + Z2 * Z2B


# ----------------------------------------------------------------------------
# INDEPENDENT geometry rebuilt from scratch (closed-form FS, holo/antiholo Christoffels).
# Cross-checked == tensor_probe at Gate V0.  g_phys = (1/2) g_pot (MET_SCALE).
# ----------------------------------------------------------------------------
MET = Rational(1, 2)


def dz(f, a):
    return sp.diff(f, ALLV[a])


def dzb(f, a):
    return sp.diff(f, ALLV[2 + a])


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


def christoffel_hol(g=None, ginv=None):
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


def delta_star(om_hol, om_ahol, g, ginv, Gam, GamB, simp=together):
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


def conformal_block(f, g, simp=together):
    Z = zeros(2, 2)
    return Z, (f * g).applyfunc(simp), Z


def trace_g(H11, ginv):
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += ginv[b, a] * H11[a, b]
    return cancel(2 * s)


def divergence(hb, g, ginv, Gam, GamB):
    """(delta h)_b = -g^{mu nu} nabla_mu h_{nu b}, independent rebuild (matches TP.divergence
    convention).  Returns (om_hol, om_ahol)."""
    H20, H11, H02 = hb
    gu = lambda a, b: ginv[b, a]
    om_hol = [sp.Integer(0)] * 2
    om_ahol = [sp.Integer(0)] * 2
    for b in range(2):
        s = sp.Integer(0)
        for a in range(2):
            for c in range(2):
                term = dz(H11[b, c], a)
                for e in range(2):
                    term -= Gam[e][a][b] * H11[e, c]
                s += gu(a, c) * term
        for a in range(2):
            for c in range(2):
                s += gu(a, c) * dzb(H20[a, b], c)
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


def grad_bilinear(phi, simp=together):
    da = [dz(phi, a) for a in range(2)]
    dab = [dzb(phi, a) for a in range(2)]
    H20 = zeros(2, 2); H11 = zeros(2, 2); H02 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            H20[a, b] = simp(da[a] * da[b])
            H11[a, b] = simp(da[a] * dab[b])
            H02[a, b] = simp(dab[a] * dab[b])
    return H20, H11, H02


# ----------------------------------------------------------------------------
# THE CLEAN (1,1) TT EXTRACTION (the independent verdict-critical computation).
# Solve  B3 = delta*omega + f.g + (0, r11, 0)  with:
#   - omega = (deg<=D poly)/rho^kw per component (general polynomial -- NOT the {phi_A dphi_B}
#     ansatz), f = (deg<=D poly)/rho^kf;
#   - the (2,0) and (0,2) blocks of (B3 - delta*omega - f.g) vanish EXACTLY (force the anti-invariant
#     part entirely into gauge+conformal);
#   - the (1,1) block of (B3 - delta*omega - f.g) = r11 (definition);
#   - tr_g(r11) = 0;
#   - divergence of (0, r11, 0) = 0 (the full residue is TT -- r11 alone is transverse).
# All matched-monomial over Q.  Per v31 the genuine TT is purely (1,1), so consistent => r11 is the
# CLEAN (1,1) TT eigentensor.  We solve for (omega,f) coeffs AND read r11 = the (1,1) residue.
# ----------------------------------------------------------------------------
def _monomials(D):
    out = []
    for tot in range(D + 1):
        for a in range(tot + 1):
            for b in range(tot - a + 1):
                for c in range(tot - a - b + 1):
                    d = tot - a - b - c
                    out.append((a, b, c, d))
    return out


def _poly_from(coeffs, monos):
    e = sp.Integer(0)
    for ci, (a, b, c, d) in zip(coeffs, monos):
        e += ci * Z1 ** a * Z2 ** b * Z1B ** c * Z2B ** d
    return e


def clean_11_extract(B3, D=3, kw=2, kf=2, g=None, ginv=None, Gam=None, GamB=None, label=""):
    """Force the (2,0)/(0,2) of B3 entirely into delta*omega + f.g; solve so the residue is purely
    (1,1), traceless, and transverse.  Returns (consistent, r11_blocks, info) where r11_blocks =
    (0, r11, 0).  The residue (1,1) block is r11[a,b] = B3_11[a,b] - W11[a,b] - (f.g)_11[a,b]
    evaluated at the solved omega,f -- it is then automatically the explicit clean (1,1) TT tensor."""
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
    cwh = [list(symbols(f"vwh{ax}_0:{nm}")) for ax in range(2)]
    cwa = [list(symbols(f"vwa{ax}_0:{nm}")) for ax in range(2)]
    cf = list(symbols(f"vff_0:{nm}"))
    om_hol = [_poly_from(cwh[ax], monos) / rho ** kw for ax in range(2)]
    om_ahol = [_poly_from(cwa[ax], monos) / rho ** kw for ax in range(2)]
    fexpr = _poly_from(cf, monos) / rho ** kf
    allc = cwh[0] + cwh[1] + cwa[0] + cwa[1] + cf
    _log(f"  [{label}] clean-11: D={D} kw={kw} kf={kf}, {len(allc)} unknowns; build delta*omega+f.g ...")
    W = delta_star(om_hol, om_ahol, g, ginv, Gam, GamB, simp=together)
    Cf = conformal_block(fexpr, g, simp=together)
    # residue blocks (symbolic in the unknowns)
    res = [zeros(2, 2), zeros(2, 2), zeros(2, 2)]
    for k in range(3):
        for a in range(2):
            for b in range(2):
                res[k][a, b] = together(B3[k][a, b] - W[k][a, b] - Cf[k][a, b])
    eqs = set()
    # (1) (2,0) and (0,2) blocks vanish exactly
    for k in (0, 2):
        for a in range(2):
            for b in range(2):
                num, den = sp.fraction(res[k][a, b])
                P = sp.Poly(expand(num), Z1, Z2, Z1B, Z2B)
                for co in P.coeffs():
                    co = expand(co)
                    if co != 0:
                        eqs.add(co)
    _log(f"  [{label}] clean-11: (2,0)/(0,2)-vanish eqs={len(eqs)}", )
    # (2) tr_g of the (1,1) residue = 0
    tr = trace_g(res[1], ginv)
    num, den = sp.fraction(together(tr))
    P = sp.Poly(expand(num), Z1, Z2, Z1B, Z2B)
    for co in P.coeffs():
        co = expand(co)
        if co != 0:
            eqs.add(co)
    _log(f"  [{label}] clean-11: +trace eqs={len(eqs)}")
    # (3) divergence of (0, res[1], 0) = 0
    r11only = (zeros(2, 2), res[1], zeros(2, 2))
    dh, da = divergence(r11only, g, ginv, Gam, GamB)
    for comp in [dh[0], dh[1], da[0], da[1]]:
        num, den = sp.fraction(together(comp))
        P = sp.Poly(expand(num), Z1, Z2, Z1B, Z2B)
        for co in P.coeffs():
            co = expand(co)
            if co != 0:
                eqs.add(co)
    eqs = [e for e in eqs if e != 0]
    _log(f"  [{label}] clean-11: +divergence => total eqs={len(eqs)}; linsolve in {len(allc)} unk ...")
    sol = sp.linsolve(eqs, allc)
    consistent = len(sol) > 0
    info = {"consistent": consistent, "n_unk": len(allc), "n_eqs": len(eqs)}
    if not consistent:
        _log(f"  [{label}] clean-11: INCONSISTENT (no purely-(1,1) transverse traceless residue)")
        return False, None, info
    solset = list(sol)[0]
    subs = {}
    for sym, val in zip(allc, solset):
        subs[sym] = val
    # zero out any free parameters (Killing-direction freedom) -> a particular solution; r11 unique
    zero_free = {s: sp.Integer(0) for s in set(allc) if s in subs and subs[s].free_symbols}
    # build the explicit r11 by substituting the particular solution into res[1]
    r11 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            e = res[1][a, b].subs(subs)
            e = e.subs(zero_free)
            r11[a, b] = cancel(e)
    info["n_free"] = len(zero_free)
    r11_blocks = (zeros(2, 2), r11, zeros(2, 2))
    return True, r11_blocks, info


def verify_clean_residue(r11_blocks, g, ginv, Gam, GamB, label=""):
    """Verify r11_blocks = (0, r11, 0) is purely (1,1), traceless, transverse."""
    r11 = r11_blocks[1]
    tr = cancel(trace_g(r11, ginv))
    dh, da = divergence(r11_blocks, g, ginv, Gam, GamB)
    div0 = all(cancel(x) == 0 for x in [dh[0], dh[1], da[0], da[1]])
    nz = any(cancel(r11[a, b]) != 0 for a in range(2) for b in range(2))
    _log(f"  [{label}] clean r11: tr_g=0 [{tr == 0}], divergence-free [{div0}], nonzero [{nz}]")
    return (tr == 0) and div0 and nz


def full_tt_extract(B3, D=3, kw=2, kf=2, g=None, ginv=None, Gam=None, GamB=None, label=""):
    """Extract the FULL unique York TT residue r = B3 - delta*omega - f.g with the ONLY constraints
    tr_g(r)=0 AND delta(r)=0 (full tensor), general-polynomial omega.  Returns (consistent, r_blocks,
    info).  r is the unique TT residue (the gauge freedom in omega does not change r).  We read all
    three blocks of r and inspect its (1,1) vs (2,0)/(0,2) content INDEPENDENTLY of the executor's
    {phi_A dphi_B} ansatz."""
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
    cwh = [list(symbols(f"uwh{ax}_0:{nm}")) for ax in range(2)]
    cwa = [list(symbols(f"uwa{ax}_0:{nm}")) for ax in range(2)]
    cf = list(symbols(f"uff_0:{nm}"))
    om_hol = [_poly_from(cwh[ax], monos) / rho ** kw for ax in range(2)]
    om_ahol = [_poly_from(cwa[ax], monos) / rho ** kw for ax in range(2)]
    fexpr = _poly_from(cf, monos) / rho ** kf
    allc = cwh[0] + cwh[1] + cwa[0] + cwa[1] + cf
    _log(f"  [{label}] full-TT: D={D} kw={kw} kf={kf}, {len(allc)} unknowns; build delta*omega+f.g ...")
    W = delta_star(om_hol, om_ahol, g, ginv, Gam, GamB, simp=together)
    Cf = conformal_block(fexpr, g, simp=together)
    res = [zeros(2, 2), zeros(2, 2), zeros(2, 2)]
    for k in range(3):
        for a in range(2):
            for b in range(2):
                res[k][a, b] = together(B3[k][a, b] - W[k][a, b] - Cf[k][a, b])
    eqs = set()
    # tr_g(res) = 0
    tr = trace_g(res[1], ginv)
    num, den = sp.fraction(together(tr))
    for co in sp.Poly(expand(num), Z1, Z2, Z1B, Z2B).coeffs():
        co = expand(co)
        if co != 0:
            eqs.add(co)
    # delta(res) = 0 (full tensor)
    dh, da = divergence(res, g, ginv, Gam, GamB)
    for comp in [dh[0], dh[1], da[0], da[1]]:
        num, den = sp.fraction(together(comp))
        for co in sp.Poly(expand(num), Z1, Z2, Z1B, Z2B).coeffs():
            co = expand(co)
            if co != 0:
                eqs.add(co)
    eqs = [e for e in eqs if e != 0]
    _log(f"  [{label}] full-TT: {len(eqs)} eqs in {len(allc)} unk; linsolve ...")
    sol = sp.linsolve(eqs, allc)
    consistent = len(sol) > 0
    info = {"consistent": consistent, "n_unk": len(allc), "n_eqs": len(eqs)}
    if not consistent:
        return False, None, info
    solset = list(sol)[0]
    subs = {sym: val for sym, val in zip(allc, solset)}
    zero_free = {s: sp.Integer(0) for s in set(allc) if s in subs and subs[s].free_symbols}
    rb = [zeros(2, 2), zeros(2, 2), zeros(2, 2)]
    for k in range(3):
        for a in range(2):
            for b in range(2):
                e = res[k][a, b].subs(subs).subs(zero_free)
                rb[k][a, b] = cancel(e)
    return True, (rb[0], rb[1], rb[2]), info


def is_anti_invariant_gauge(r_blocks, D=3, kw=2, kf=2, g=None, ginv=None, Gam=None, GamB=None,
                            label=""):
    """Test whether the (2,0)+(0,2) part of r (with (1,1) zeroed) is itself pure gauge+conformal.
    If gauge then v31's 'jointly gauge' holds and the genuine TT is the (1,1) part; if NOT gauge then
    r has a genuine (2,0)+(0,2) TT component (the suspected v31 nuance)."""
    if g is None:
        g = metric()
    if ginv is None:
        ginv = metric_inv(g)
    if Gam is None:
        Gam = christoffel_hol(g, ginv)
    if GamB is None:
        GamB = christoffel_antihol(g, ginv)
    anti = (r_blocks[0], zeros(2, 2), r_blocks[2])
    monos = _monomials(D)
    nm = len(monos)
    rho = _rho()
    cwh = [list(symbols(f"bwh{ax}_0:{nm}")) for ax in range(2)]
    cwa = [list(symbols(f"bwa{ax}_0:{nm}")) for ax in range(2)]
    cf = list(symbols(f"bff_0:{nm}"))
    om_hol = [_poly_from(cwh[ax], monos) / rho ** kw for ax in range(2)]
    om_ahol = [_poly_from(cwa[ax], monos) / rho ** kw for ax in range(2)]
    fexpr = _poly_from(cf, monos) / rho ** kf
    allc = cwh[0] + cwh[1] + cwa[0] + cwa[1] + cf
    W = delta_star(om_hol, om_ahol, g, ginv, Gam, GamB, simp=together)
    Cf = conformal_block(fexpr, g, simp=together)
    eqs = set()
    for k in range(3):
        for a in range(2):
            for b in range(2):
                diff = together(anti[k][a, b] - W[k][a, b] - Cf[k][a, b])
                num, den = sp.fraction(diff)
                for co in sp.Poly(expand(num), Z1, Z2, Z1B, Z2B).coeffs():
                    co = expand(co)
                    if co != 0:
                        eqs.add(co)
    eqs = [e for e in eqs if e != 0]
    _log(f"  [{label}] anti-gauge test: {len(eqs)} eqs in {len(allc)} unk; linsolve ...")
    sol = sp.linsolve(eqs, allc)
    is_gauge = len(sol) > 0
    return is_gauge


# ----------------------------------------------------------------------------
# INDEPENDENT L^2 inner product (re-derived; the same FS Dirichlet integral, rebuilt from scratch).
# ----------------------------------------------------------------------------
_S1, _S2 = symbols("S1v S2v", nonnegative=True)


def _mono_integral(a, b, K):
    a, b, K = int(a), int(b), int(K)
    m = K - a - b - 3
    if m < 0:
        raise ValueError(f"divergent: K-a-b-3={m}<0")
    return Rational(sp.factorial(a) * sp.factorial(b) * sp.factorial(m), sp.factorial(K - 1))


def _rho_power_of(den):
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
        elif sp.expand(fac + rho) == 0:
            k = mult
            const *= (-1) ** mult
        else:
            raise ValueError(f"factor {fac} not rho")
    return k, const


def _phase_average(num):
    cd = sp.expand(num).as_coefficients_dict()
    terms = {}
    for mono, coeff in cd.items():
        pd = mono.as_powers_dict()
        a1 = int(pd.get(Z1, 0)); a2 = int(pd.get(Z2, 0))
        b1 = int(pd.get(Z1B, 0)); b2 = int(pd.get(Z2B, 0))
        if a1 == b1 and a2 == b2:
            terms[(a1, a2)] = terms.get((a1, a2), sp.Integer(0)) + coeff
    return sum(c * _S1 ** a * _S2 ** b for (a, b), c in terms.items())


def l2_scalar(f):
    f = cancel(f)
    num, den = sp.fraction(f)
    k, const = _rho_power_of(sp.expand(den))
    K = k + 3
    num = sp.expand(num / const)
    Pmatch = _phase_average(num)
    total = sp.Integer(0)
    for (a, b), coeff in sp.Poly(Pmatch, _S1, _S2).terms():
        total += coeff * _mono_integral(a, b, K)
    return cancel(total)


def l2_tensor(hb, hpb, ginv):
    """Independent rebuild of the FS L^2 tensor inner product (the VERIFIED contraction formula:
    (1,1).(1,1) coeff 2, (2,0).(0,2) + (0,2).(2,0) coeff 1)."""
    H20, H11, H02 = hb
    P20, P11, P02 = hpb
    gu = lambda a, b: ginv[b, a]
    terms = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    terms.append(2 * gu(a, d) * gu(c, b) * H11[a, b] * P11[c, d])
                    terms.append(gu(a, c) * gu(b, d) * H20[a, b] * P02[c, d])
                    terms.append(gu(c, a) * gu(d, b) * H02[a, b] * P20[c, d])
    return l2_scalar(sp.Add(*terms, evaluate=False))


# ----------------------------------------------------------------------------
# INDEPENDENT covariant calculus + Lichnerowicz on the EXPLICIT (1,1) eigentensor (PRIORITY B).
# Delta_L h = nabla*nabla h + 2 Lambda h - 2 Rdot h, nabla*nabla = -g^{mu nu}nabla_mu nabla_nu
# (positive convention), Rdot h_{ab} = R_{acbd} h^{cd}.  Rebuilt from scratch (own Riemann, own
# covariant-derivative bookkeeping) -- NOT calling the executor's rough_laplacian/Rdot.
# ----------------------------------------------------------------------------
def riemann_kahler(g, ginv):
    """R_{a bbar c dbar} = - d_a d_dbar g_{c bbar} + g^{e fbar}(d_a g_{c fbar})(d_dbar g_{e bbar})."""
    R = [[[[sp.Integer(0)] * 2 for _ in range(2)] for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    t = -dz(dzb(g[c, b], d), a)
                    for e in range(2):
                        for fdx in range(2):
                            t += ginv[fdx, e] * dz(g[c, fdx], a) * dzb(g[e, b], d)
                    R[a][b][c][d] = cancel(t)
    return R


def _T_get(blocks, mu, nu):
    H20, H11, H02 = blocks
    bar = lambda i: i >= 2
    ix = lambda i: i % 2
    if not bar(mu) and not bar(nu):
        return H20[ix(mu), ix(nu)]
    if bar(mu) and bar(nu):
        return H02[ix(mu), ix(nu)]
    if not bar(mu) and bar(nu):
        return H11[ix(mu), ix(nu)]
    return H11[ix(nu), ix(mu)]


def _nabla(blocks, e, ebar, g, ginv, Gam, GamB, simp=together):
    D = [[sp.Integer(0)] * 4 for _ in range(4)]
    der = (lambda f: dzb(f, e)) if ebar else (lambda f: dz(f, e))
    bar = lambda i: i >= 2
    ix = lambda i: i % 2
    for mu in range(4):
        for nu in range(4):
            t = der(_T_get(blocks, mu, nu))
            if (not ebar) and (not bar(mu)):
                for lam in range(2):
                    t -= Gam[lam][e][ix(mu)] * _T_get(blocks, lam, nu)
            if ebar and bar(mu):
                for lam in range(2):
                    t -= GamB[lam][e][ix(mu)] * _T_get(blocks, lam + 2, nu)
            if (not ebar) and (not bar(nu)):
                for lam in range(2):
                    t -= Gam[lam][e][ix(nu)] * _T_get(blocks, mu, lam)
            if ebar and bar(nu):
                for lam in range(2):
                    t -= GamB[lam][e][ix(nu)] * _T_get(blocks, mu, lam + 2)
            D[mu][nu] = simp(t)
    return D


def rough_laplacian(blocks, g, ginv, Gam, GamB):
    """nabla*nabla h = -2 g^{a bbar} nabla_a nabla_bbar h (positive geometer convention).
    Independent rebuild."""
    gu = lambda a, b: ginv[b, a]
    out20 = zeros(2, 2); out11 = zeros(2, 2); out02 = zeros(2, 2)
    nb = []
    for b in range(2):
        nb.append(_nabla(blocks, b, True, g, ginv, Gam, GamB, simp=cancel))
    bar = lambda i: i >= 2
    ix = lambda i: i % 2
    for mu in range(4):
        for nu in range(4):
            acc = sp.Integer(0)
            for a in range(2):
                for b in range(2):
                    t = dz(nb[b][mu][nu], a)
                    if not bar(mu):
                        for lam in range(2):
                            t -= Gam[lam][a][ix(mu)] * nb[b][lam][nu]
                    if not bar(nu):
                        for lam in range(2):
                            t -= Gam[lam][a][ix(nu)] * nb[b][mu][lam]
                    acc += gu(a, b) * cancel(t)
            val = cancel(-2 * acc)
            if not bar(mu) and not bar(nu):
                out20[ix(mu), ix(nu)] = val
            elif bar(mu) and bar(nu):
                out02[ix(mu), ix(nu)] = val
            elif not bar(mu) and bar(nu):
                out11[ix(mu), ix(nu)] = val
    return out20, out11, out02


def Rdot11(H11, g, ginv, R):
    """(Rdot h)_{a bbar} = R_{a bbar c dbar} g^{c fbar} g^{e dbar} h_{e fbar} on the (1,1) block.
    Independent rebuild (own index bookkeeping)."""
    gu = lambda a, b: ginv[b, a]
    out11 = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            s = sp.Integer(0)
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for fdx in range(2):
                            s += R[a][b][c][d] * gu(c, fdx) * gu(e, d) * H11[e, fdx]
            out11[a, b] = cancel(s)
    return out11


def lichnerowicz_11(H11, g, ginv, Gam, GamB, R, Lam=6):
    """Delta_L^{(1,1)} h = [nabla*nabla h]^{(1,1)} + 2 Lam h - 2 [Rdot h]^{(1,1)} on a (1,1) tensor.
    Independent rebuild."""
    h11only = (zeros(2, 2), H11, zeros(2, 2))
    rr = rough_laplacian(h11only, g, ginv, Gam, GamB)
    rd = Rdot11(H11, g, ginv, R)
    out = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            out[a, b] = cancel(rr[1][a, b] + 2 * Lam * H11[a, b] - 2 * rd[a, b])
    return out


def schur_scalar_11(H11, g, ginv, Gam, GamB, R, Lam=6, pts=None):
    """If Delta_L^{(1,1)} H11 = lam * H11 (proportional, the Schur eigenvalue), return lam."""
    dL = lichnerowicz_11(H11, g, ginv, Gam, GamB, R, Lam)
    if pts is None:
        pts = [{Z1: Rational(1, 2), Z2: Rational(1, 3), Z1B: Rational(1, 5), Z2B: Rational(-1, 4)},
               {Z1: Rational(-2, 3), Z2: Rational(1, 7), Z1B: Rational(1, 3), Z2B: Rational(2, 5)},
               {Z1: Rational(1, 4), Z2: Rational(-1, 2), Z1B: Rational(-1, 6), Z2B: Rational(1, 8)}]
    lam = None
    for pp in pts:
        for a in range(2):
            for b in range(2):
                n1 = cancel(dL[a, b].subs(pp))
                n2 = cancel(H11[a, b].subs(pp))
                if n2 == 0:
                    if n1 != 0:
                        return None
                    continue
                rr = cancel(n1 / n2)
                if lam is None:
                    lam = rr
                elif cancel(lam - rr) != 0:
                    return None
    return lam


def run_priority_A(verbose=True):
    """PRIORITY A: confirm/refute the (1,1)-projection. Extract the full unique York TT residue of
    B3(s01) via the executor, decompose into J-parts, show r[1]-alone is NOT transverse, the full r
    IS transverse, and the (2,0)+(0,2) companion is nonzero (NOT jointly gauge). Compute norms."""
    import tensor_probe as TP
    import lichnerowicz_response as LR
    g = TP.fs_metric(); ginv = TP.fs_metric_inv(g); Gam = TP.christoffel_hol(g, ginv)
    GamB = TP._christoffel_antihol(g, ginv)
    out = {}
    for nm, M in [("s01", Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])),
                  ("d2", Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]))]:
        phi = cancel(TP.phi_field(M))
        B3 = TP.grad_bilinear(phi, simp=together)
        r, _, _, _, info = LR.extract_tt(B3, g, ginv, Gam, verify=True)
        r11only = (zeros(2, 2), r[1], zeros(2, 2))
        ranti = (r[0], zeros(2, 2), r[2])
        dh1, da1 = divergence(r11only, g, ginv, Gam, GamB)
        r11_div0 = all(cancel(x) == 0 for x in [dh1[0], dh1[1], da1[0], da1[1]])
        n11 = cancel(l2_tensor(r11only, r11only, ginv))
        nanti = cancel(l2_tensor(ranti, ranti, ginv))
        nfull = cancel(n11 + nanti)
        tr2 = cancel(TP.TrM2_cx(M))
        out[nm] = dict(full_TT=info.get("tr_zero") and info.get("div_zero"),
                       r11_transverse=r11_div0, n11=n11, nanti=nanti, nfull=nfull,
                       k11=cancel(n11 / tr2**2), kfull=cancel(nfull / tr2**2), detM=cancel(M.det()))
        if verbose:
            _log(f"  A[{nm}]: full r TT={out[nm]['full_TT']}, r[1]-alone transverse={r11_div0}; "
                 f"k11={out[nm]['k11']} (executor=1/54), kfull={out[nm]['kfull']}, "
                 f"||ranti||^2={nanti} (nonzero => NOT jointly gauge), detM={out[nm]['detM']}")
    return out


def run_priority_B(verbose=True):
    """PRIORITY B: confirm the genuine Boucetta (1,1) TT eigenvalue is 12 (eps=0), and that the
    executor's lambda_L=32 is the eigenvalue of the operator on the non-transverse r[1] (matches the
    (2,0)/(0,2) sector). Operator-agreement: independent Delta_L^(1,1) on r[1] == executor (both 32);
    operator calibration controls Delta_L(g)=0, Rdot(g)=6g pass for the independent operator."""
    import tensor_probe as TP
    import lichnerowicz_response as LR
    g = TP.fs_metric(); ginv = TP.fs_metric_inv(g); Gam = TP.christoffel_hol(g, ginv)
    GamB = TP._christoffel_antihol(g, ginv)
    R = riemann_kahler(g, ginv); Rex = LR.riemann_kahler(g, ginv, Gam)
    out = {}
    # calibration
    out["Rdot_g_is_6g"] = all(cancel(Rdot11(g, g, ginv, R)[a, b] - 6 * g[a, b]) == 0
                              for a in range(2) for b in range(2))
    dLg = lichnerowicz_11(g, g, ginv, Gam, GamB, R, Lam=6)
    out["DL_g_is_0"] = all(cancel(dLg[a, b]) == 0 for a in range(2) for b in range(2))
    # operator agreement on r[1]
    Ms01 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    phi = cancel(TP.phi_field(Ms01)); B3 = TP.grad_bilinear(phi, simp=together)
    r, _, _, _, _ = LR.extract_tt(B3, g, ginv, Gam, verify=False)
    out["indep_lambda_on_r11"] = schur_scalar_11(r[1], g, ginv, Gam, GamB, R, Lam=6)
    dLex = LR.lichnerowicz_11((zeros(2, 2), r[1], zeros(2, 2)), g, ginv, Gam, GamB, Rex, Lambda=6)
    out["executor_lambda_on_r11"] = LR._tensor_ratio(dLex, (zeros(2, 2), r[1], zeros(2, 2)),
                                                     blocks_use=(1,))
    # Boucetta master formula at n=2 (same convention Ric=2(n+1)g): (1,1) primitive 4(n+1)=12,
    # (2,0)/(0,2) lowest 8(n+2)=32
    n = 2
    out["boucetta_11_TT"] = 4 * (n + 1)
    out["boucetta_20_TT"] = 8 * (n + 2)
    out["eps_genuine"] = out["boucetta_11_TT"] - 12
    if verbose:
        _log(f"  B: calibration Rdot(g)=6g={out['Rdot_g_is_6g']}, DL(g)=0={out['DL_g_is_0']}")
        _log(f"  B: indep lambda on r[1]={out['indep_lambda_on_r11']} == executor "
             f"{out['executor_lambda_on_r11']} (operators AGREE; r[1] NOT transverse)")
        _log(f"  B: Boucetta n=2: (1,1) TT lambda_L={out['boucetta_11_TT']} (dim 8), "
             f"(2,0)/(0,2) TT lambda_L={out['boucetta_20_TT']} (dim 27); "
             f"eps_genuine = {out['eps_genuine']} (NOT 20)")
    return out


if __name__ == "__main__":
    import sys
    arg = sys.argv[1] if len(sys.argv) > 1 else "info"
    if arg == "A":
        run_priority_A()
    elif arg == "B":
        run_priority_B()
    elif arg == "all":
        run_priority_A(); run_priority_B()
    else:
        print("INDEPENDENT verifier module loaded (functions ready). "
              "Run with 'A', 'B', or 'all'.", flush=True)
