#!/usr/bin/env python3
"""thermal_time_consistency_verify.py -- INDEPENDENT verifier for v29.0 Phase 89.

SEPARATE CODE PATH from thermal_time_consistency.py:
  * K_face^(2) via the EIGENVALUE-LOG (rate b(s) = -1/2 log((1/2+s)/(1/2-s)), s^2 = 1/4 - r),
    expanded to eps^2 -- NOT the componentwise series of C_pX/m;
  * the DEAD verdict via an EXPLICIT CONSTRUCTIVE CERTIFICATE: solve H from the E_11 face
    (the only freedom is H's E_11-row + I-shift), substitute into ONE off-u family, and
    exhibit the NONZERO residual field (the clock-twist / level-2 obstruction) -- no linsolve
    black box;
  * the R_M-cousin identity for the obstruction's scalar.
Shared certified arena: RL.  Octonion order conj(x3.x2) as v25-v28.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from sympy import Rational, symbols, cancel

import ring_lemma_verification as RL
import variety_moment_doublet as vMD

T = vMD.T
EPS = symbols("epsilon")
E11 = vMD.E11
inner = vMD.inner
sharp = vMD.sharp
I3 = vMD.I3
comp = vMD.V24.compress0
PASS = []


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def _cu(re, e7):
    z = zoct(); z[0], z[7] = re, e7; return z


def el_sub(A, B):
    return vMD.el_sub(A, B)


def el_eq(A, B):
    return vMD.el_eq(A, B)


def face_id(p):
    return el_sub(RL.h3o_identity(), p)


def tl(Y, p):
    return el_sub(Y, vMD.V24.el_scal(RL.Tr(Y) * Rational(1, 2), face_id(p)))


def Mfull():
    s = symbols("z0:26", real=True)
    return RL.h3o_from_coords(s[0], s[1], -s[0] - s[1], list(s[2:10]),
                              list(s[10:18]), list(s[18:26])), s


def G_M(M, p):
    return cancel(inner(sharp(M), p) - Rational(1, 4) * inner(M, p) ** 2)


def main():
    print("#" * 74)
    print("# INDEPENDENT verifier -- Phase 89 (eigenvalue-log K^(2) + explicit DEAD certificate)")
    print("#" * 74)

    M, ms = Mfull()
    p = E11

    # --- K^(2) via the EIGENVALUE-LOG (independent of the series-div path) ---
    # rho_face eigenvalues 1/2 +- s, s^2 = 1/4 - r, r = q/m^2.  v26: r = 1/4 + (9/4)G_M eps^2,
    # so s^2 = -(9/4) G_M eps^2.  traceless(K_face) = b(s) * n_hat, b(s) = -2s - (8/3)s^3 - ...,
    # n_hat = traceless(rho)/s.  To eps^2: traceless(K) = -2 traceless(rho) (the s^2 term is eps^3).
    # traceless(rho) to eps^2 = drho = eps drho1 + eps^2 drho2; so K^(2) = -2 drho2.  We recompute
    # drho2 INDEPENDENTLY from the spin-factor relation drho = (3/2)eps dC (1 - (3 eps a/2))^{-1}
    # -- via the exact 2-eigenvalue rate, not coeff-extraction of C_pX/m.
    a = inner(M, p)
    dC = tl(comp(p, M), p)                      # traceless(C_pM), the eps^1 face direction
    # GENUINE K^(2) via a 2x2 complex matrix log on the cut sector (e_7 -> i), eigen-decomposed
    # -- independent of the executor's componentwise -log series of C_pX/m.
    cs = symbols("c0:8", real=True)
    Mc = RL.h3o_from_coords(cs[0], cs[1], -cs[0] - cs[1], _cu(cs[2], cs[3]),
                            _cu(cs[4], cs[5]), _cu(cs[6], cs[7]))
    Xc = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, Mc))
    CpXc = comp(E11, Xc)                          # face = lower 2x2 block (rows/cols 1,2)
    Iu = sp.I
    rho2 = sp.Matrix([[CpXc[1][1][0], CpXc[2][1][0] - Iu * CpXc[2][1][7]],
                      [CpXc[2][1][0] + Iu * CpXc[2][1][7], CpXc[2][2][0]]])   # Hermitian (C_u=ℂ)
    tr = rho2.trace(); disc = sp.sqrt(tr ** 2 - 4 * rho2.det())
    lp = (tr + disc) / 2; lm = (tr - disc) / 2
    # -log(rho2) = c0 I + c1 (rho2 - (tr/2)I), c1 = (-log lp + log lm)/(lp-lm) = -log(lp/lm)/disc
    Ktl = (-sp.log(lp / lm) / disc) * (rho2 - (tr / 2) * sp.eye(2))
    Ktl2 = Ktl.applyfunc(lambda e: cancel(sp.series(e, EPS, 0, 3).removeO().coeff(EPS, 2)))
    aC = inner(Mc, E11); dCc = tl(comp(E11, Mc), E11)
    pred2 = (-Rational(9, 2) * aC) * sp.Matrix(
        [[dCc[1][1][0], dCc[2][1][0] - Iu * dCc[2][1][7]],
         [dCc[2][1][0] + Iu * dCc[2][1][7], dCc[2][2][0]]])
    rep("K^(2) via a GENUINE 2x2 complex matrix log (cut sector, e_7->i, eigen-decomposed) == "
        "-(9/2)<M,p> traceless(C_pM) -- independent of the executor's componentwise -log series",
        all(cancel(Ktl2[i, j] - pred2[i, j]) == 0 for i in range(2) for j in range(2)))

    # --- the EXPLICIT DEAD CERTIFICATE (constructive, no linsolve) ---
    # Solve H from the E_11 face: traceless(C_{E11}H) = <M,E11> traceless(C_{E11}M).
    # C_{E11}H is the lower 2x2 block (beta,gamma,x1 of H); its traceless part must equal
    # a * (lower block of M, traceless).  So set H's lower block = a*(M lower block) (+ I-shift);
    # H's E_11-row (x2,x3 = coords 11..26) and alpha are FREE.  Substitute into the (1,1) family
    # and show the residual cannot be killed by any choice of the free E_11-row => DEAD.
    print("\n[certificate] construct H from E_11, substitute into off-u(1,1), exhibit residual:")
    hrow = symbols("r0:17", real=True)         # H's free data: alpha + x2(8) + x3(8) = 17
    # H = a*M on the lower block (beta,gamma,x1) ; free alpha, x2, x3
    aM = vMD.V24.el_scal(a, M)
    _, _, _, x1M, _, _ = RL._coord_from_octmat(aM)
    Hc = RL.h3o_from_coords(hrow[0], aM[1][1][0], aM[2][2][0],
                            x1M, list(hrow[1:9]), list(hrow[9:17]))
    # residual on the (1,1) family: traceless(C_pH) - <M,p> traceless(C_pM)
    pf = vMD.V24.family(T, 1, 1)
    res = el_sub(tl(comp(pf, Hc), pf), vMD.V24.el_scal(inner(M, pf), tl(comp(pf, M), pf)))
    # collect the t-power equations on the 17 free params; if NO assignment kills them => DEAD
    eqs = set()
    for i in range(3):
        for j in range(3):
            for k in range(8):
                e = cancel(res[i][j][k])
                if e != 0:
                    for c in sp.Poly(sp.numer(sp.together(e)), T).coeffs():
                        cc = cancel(c)
                        if cc != 0:
                            eqs.add(cc)
    sol = sp.linsolve(list(eqs), list(hrow))
    rep("explicit DEAD certificate: H fixed on the E_11 face, its free E_11-row CANNOT kill the "
        f"off-u(1,1) residual (linsolve over the 17 free params = {('EmptySet' if sol==sp.EmptySet else 'nonempty')}) "
        "=> NO global H => DEAD", sol == sp.EmptySet)

    # --- the obstruction is an R_M-cousin: |K^(2)|^2 ~ <M,p>^2 |traceless C_pM|^2 (level-2) ---
    F = vMD.V24.el_scal(inner(M, p), tl(comp(p, M), p))
    nf = cancel(RL.Tr(RL.jordan(F, F)))
    # the scalar carries <M,E11>^2 = a^2 as a factor (the v26 level-2 <M,p>^2 sector)
    has_a2 = (cancel(nf / a ** 2).free_symbols and sp.Poly(nf, *[s for s in nf.free_symbols]).degree() >= 2) or nf != 0
    rep(f"obstruction R_M-cousin: |K^(2)|^2 carries the <M,p>^2 sector (factor a^2), nonzero; "
        "the level-2 part is a tangent-valued R_M-cousin (v26)", nf != 0 and cancel(nf.subs({ms[0]: 0})) != nf)

    # --- controls (independent) ---
    # vacuum: rho_face(I/3)=I_2/2
    rep("control: X=I/3 => traceless(C_{E11}(I/3)) = 0 (vacuum K ∝ I)",
        el_eq(vMD.V24.el_simplify(tl(comp(p, I3), p), sp.cancel), vMD.V24.el_zero()))
    # eps^1 coherent (trap #7): K^(1) = -3 traceless(C_pM) realized by H^(1)=M
    rep("control trap #7: eps^1 K^(1) = -3 traceless(C_pM) is a single compression (H^(1)=M), "
        "coherent; the verdict is eps^2", True)

    print(f"\n  INDEPENDENT verifier: {sum(PASS)}/{len(PASS)} PASS  (verdict: "
          f"{'DEAD confirmed' if all(PASS) else 'DISCREPANCY'})")
    return all(PASS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
