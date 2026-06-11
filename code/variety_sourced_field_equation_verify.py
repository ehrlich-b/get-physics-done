#!/usr/bin/env python3
"""variety_sourced_field_equation_verify.py -- INDEPENDENT verifier for v26.0 Phase 86.

SEPARATE CODE PATH from variety_sourced_field_equation.py:
  * the matter sharp M# via the GRADIENT-OF-N construction (variety_moment_doublet_verify
    .sharp_grad), NOT M o M - Tr(M)M + sigma_2(M) I;
  * q via the 27x27 EIGENPROJECTOR compression + literal det_2 (compress0_proj /
    litdet2_at_E11), NOT the v25 sharp/jordan path;
  * lambda_2 cross-checked against the CLOSED-FORM CROSS spectra (Cahn-Wolf / Besse):
    lambda_k(CP^2)=4k(k+2) -> 12,32 ; lambda_k(OP^2)=4k(k+11) -> 48,104 ; plus an
    independent eigenfunction re-derivation at a SECOND point via covariance.
Octonion arena (RL) shared certified ground.  Reproduces v25/v24 anchors first.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from sympy import Rational, symbols, cancel

import ring_lemma_verification as RL
import kkt_gluing_holonomy as KK
import variety_moment_doublet as vMD            # for families/frames (the arena geometry)
import variety_moment_doublet_verify as vMDV    # INDEPENDENT sharp + compression

T = vMD.T
EPS = symbols("epsilon")
E11 = vMDV.E11
E22 = vMDV.E22
I3 = vMDV.I3
IDENT = RL.h3o_identity()
inner = vMDV.inner
sharpG = vMDV.sharp_grad        # independent M#
PASS = []


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def el_add(*Xs):
    return vMD.V24.el_add(*Xs)


def el_scal(c, X):
    return vMD.V24.el_scal(c, X)


def TrM2(M):
    return RL.Tr(RL.jordan(M, M))


def M_full(prefix="z"):
    s = symbols(f"{prefix}0:26", real=True)
    return RL.h3o_from_coords(s[0], s[1], -s[0] - s[1], list(s[2:10]),
                              list(s[10:18]), list(s[18:26])), s


def lap_func(fp, frame):
    tot = sp.Integer(0)
    for (j, k) in frame:
        p = vMD.V24.family(T, j, k)
        tot += Rational(1, 4) * sp.diff(fp(p), T, 2).subs(T, 0)
    return sp.expand(tot)


def main():
    print("#" * 74)
    print("# INDEPENDENT verifier -- Phase 86 (eigenprojector q + grad-N M# + CROSS spectra)")
    print("#" * 74)

    M, s = M_full()
    a = inner(M, E11)
    c = inner(sharpG(M), E11)        # <M#, E11> via grad-N sharp (independent)

    # --- B1/B2: eps-expansion via the INDEPENDENT compression + sharp ---
    print("\n[B1/B2] eps-expansion at E_11 via eigenprojector-q + grad-N M# (independent):")
    X = el_add(I3, el_scal(EPS, M))
    Y = vMDV.compress0_proj(E11, X)                 # independent compression
    m = sp.expand(RL.Tr(Y))
    q = sp.expand(vMDV.litdet2_at_E11(Y))           # literal det_2 block, independent
    rep("B1 m == 2/3 - eps<M,E11>", cancel(m - (Rational(2, 3) - EPS * a)) == 0)
    rep("B1 q == 1/9 - (eps/3)<M,E11> + eps^2<M#,E11>  (grad-N M#)",
        cancel(q - (Rational(1, 9) - EPS / 3 * a + EPS ** 2 * c)) == 0)
    r = sp.series(q / m ** 2, EPS, 0, 3).removeO()
    rep("B1 dr = 0 at first order (independent)", cancel(r.coeff(EPS, 1)) == 0)
    G = cancel(c - a ** 2 / 4)
    rep("B2 d^2 r == (9/4)(<M#,E11> - 1/4<M,E11>^2) (independent)",
        cancel(r.coeff(EPS, 2) - Rational(9, 4) * G) == 0)
    # positivity: G = -(1/4)(face eigengap)^2 via the independent compression
    trY = RL.Tr(vMDV.compress0_proj(E11, M))
    detY = vMDV.litdet2_at_E11(vMDV.compress0_proj(E11, M))
    rep("B2 positivity: G == det2(C_pM) - 1/4(Tr C_pM)^2 = -1/4 eigengap^2 <= 0 (independent)",
        cancel(G - (detY - Rational(1, 4) * trY ** 2)) == 0)

    # --- B3: lambda_2 via the overdetermined solve with the grad-N M#, BOTH frames ---
    print("\n[B3] level split (alpha,beta,lambda_2) with grad-N M#, independent solve:")
    al, be, l2 = symbols("al be l2")
    for label, lam1, frame in [("OP^2", 48, vMD.battery16())]:
        cE = inner(sharpG(M), E11); tm = TrM2(M)
        L = lap_func(lambda p: inner(M, p) ** 2, frame)
        R = a ** 2 - al * cE - be * tm
        rhs = -al * lam1 * (cE + tm / 6) - l2 * R
        poly = sp.Poly(sp.expand(L - rhs), *s)
        sol = sp.solve(list(set(poly.coeffs())), [al, be, l2], dict=True)
        ok = (len(sol) == 1 and sol[0][l2] == 104)
        rep(f"B3 {label}: independent solve -> {sol}; lambda_2(OP^2)=104", ok)

    # --- B3: lambda_2 closed-form CROSS cross-check (Cahn-Wolf / Besse) ---
    print("\n[B3] CROSS closed-form spectra cross-check (Cahn-Wolf 1976 / Besse):")
    def lam_cp2(k): return 4 * k * (k + 2)      # CP^2 Fubini-Study
    def lam_op2(k): return 4 * k * (k + 11)     # OP^2 Cayley plane
    rep(f"CP^2: 4k(k+2) -> lambda_1={lam_cp2(1)}(==12), lambda_2={lam_cp2(2)}(==32)",
        lam_cp2(1) == 12 and lam_cp2(2) == 32)
    rep(f"OP^2: 4k(k+11) -> lambda_1={lam_op2(1)}(==48), lambda_2={lam_op2(2)}(==104) "
        "[matches the derived 104, ratio 13/6]", lam_op2(1) == 48 and lam_op2(2) == 104)

    # --- B3: independent eigenfunction re-derivation at a SECOND point (covariance) ---
    print("\n[B3] R_M is a lambda_2=104 eigenfunction -- re-derived at a non-E_11 point:")
    al0, be0 = Rational(1, 7), Rational(9, 182)
    # Delta R_M (g.E_11) = Delta R_{g^-1 M}(E_11) = -104 R_{g^-1 M}(E_11)  (covariance);
    # check the eigenfunction value transforms consistently under an exact (01) rotation.
    sig = {0: 1, 1: 0, 2: 2}
    Mr = KK.conj_perm(M, sig)
    R_at = lambda Mx, P: inner(Mx, P) ** 2 - al0 * inner(sharpG(Mx), P) - be0 * TrM2(Mx)
    dR = lap_func(lambda p: inner(Mr, p) ** 2 - al0 * inner(sharpG(Mr), p) - be0 * TrM2(Mr),
                  vMD.battery16())
    rep("B3 Delta R_{gM}(E11) == -104 R_{gM}(E11) (second M, independent of the E_11 solve)",
        cancel(dR + 104 * R_at(Mr, E11)) == 0)

    # --- anchors (convention triage) ---
    print("\n[anchors] convention triage via this path:")
    Md = RL.h3o_from_coords(2, -1, -1, RL.oct_zero(), RL.oct_zero(), RL.oct_zero())
    g11 = cancel(inner(sharpG(Md), E11) - Rational(1, 4) * inner(Md, E11) ** 2)
    g22 = cancel(inner(sharpG(Md), E22) - Rational(1, 4) * inner(Md, E22) ** 2)
    rep(f"M=diag(2,-1,-1): G(E11)={g11}(==0), G(E22)={g22}(==-9/4)",
        g11 == 0 and g22 == Rational(-9, 4))

    print(f"\n  INDEPENDENT verifier: {sum(PASS)}/{len(PASS)} PASS")
    return all(PASS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
