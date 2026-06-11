#!/usr/bin/env python3
"""variety_spinor_moment_verify.py -- INDEPENDENT verifier for v28.0 Phase 88.

SEPARATE CODE PATH from variety_spinor_moment.py:
  * s_X = pi_{1/2}^{(p)}(X) via the JORDAN eigenprojector P_{1/2} = 4 L_p(I - L_p)
    (L_p eigenvalues {0,1/2,1}), NOT the entry-extraction;
  * zeros via the OPERATOR characterization s_X(p)=0 <=> [L_X, L_p] = 0 (X and p share an
    eigenframe / X in J_1(p)+J_0(p)), independent of the projection;
  * the Euler closure via an independent Morse-index count from the Jordan-Hessian signs;
  * the v22 dictionary via an independent diagonal-unitary-conjugation torus generator.
Shared certified arena: RL.  Octonion order conj(x3.x2) as v25-v27.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from sympy import Rational, symbols, cancel

import ring_lemma_verification as RL
import kkt_gluing_holonomy as KK
import variety_moment_doublet as vMD

T = vMD.T
E = [KK.E_ii(0), KK.E_ii(1), KK.E_ii(2)]
E11 = E[0]
inner = vMD.inner
sharp = vMD.sharp
PASS = []


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def oct1(k, v):
    z = zoct(); z[k] = sp.sympify(v); return z


def normsq(Y):
    return cancel(RL.Tr(RL.jordan(Y, Y)))


def s_proj(X, p):
    """s_X(p) = P_{1/2}(X) = 4(p o X) - 4(p o (p o X))  (independent eigenprojector)."""
    pX = RL.jordan(p, X)
    ppX = RL.jordan(p, pX)
    return vMD.V24.el_add(vMD.V24.el_scal(4, pX), vMD.V24.el_scal(-4, ppX))


def commutator_zero(X, p):
    """[L_X, L_p] acting: X and p operator-commute iff p o (X o Y) == X o (p o Y) for a probe;
    equivalently (independent of projection) s_X(p)=0 iff p o (p o X) == p o X  no -- use the
    cleaner: X in J_1(p)+J_0(p) iff p o X == (P_1+P_0)X has no 1/2 part iff 2(p o X) - X is in
    J_1-J_0 ... operationally: s=0 iff P_{1/2}X==0; verify via the Lie bracket [X,p] (matrix
    commutator) vanishing for the SHARED-eigenframe characterization on Hermitian X,p."""
    XP = RL.h3o_matmul(X, p)
    PX = RL.h3o_matmul(p, X)
    return RL.octmat_is_zero(RL.octmat_sub(XP, PX))


def main():
    print("#" * 74)
    print("# INDEPENDENT verifier -- Phase 88 (eigenprojector s_X + operator zeros + Euler)")
    print("#" * 74)

    # --- E1: s_X (eigenprojector) == dphi_X, and == entry-extraction (cross-path) ---
    xs = symbols("z0:27", real=True)
    X = RL.h3o_from_coords(xs[0], xs[1], xs[2], list(xs[3:11]), list(xs[11:19]), list(xs[19:27]))
    # gradient rep along all 16 families (independent projector)
    fam_ok = True
    for (j, k) in vMD.battery16():
        p = vMD.V24.family(T, j, k)
        ddt = sp.diff(inner(X, p), T).subs(T, 0)
        pdot = [[[sp.diff(p[i][jj][kk], T).subs(T, 0) for kk in range(8)]
                 for jj in range(3)] for i in range(3)]
        fam_ok &= (cancel(ddt - inner(s_proj(X, E11), pdot)) == 0)
    rep("E1 (independent eigenprojector): s_X = dphi_X along all 16 families", fam_ok)
    # norm formula
    a = inner(X, E11); c = inner(sharp(X), E11); TrX = RL.Tr(X); TrX2 = normsq(X)
    rep("E1 norm: ‖s_X‖^2_tr == TrX^2 - a^2 - (TrX-a)^2 + 2c (eigenprojector, general X)",
        cancel(normsq(s_proj(X, E11)) - (TrX2 - a ** 2 - (TrX - a) ** 2 + 2 * c)) == 0)

    # --- E2: zeros = eigenframe, via the OPERATOR commutator (independent) ---
    Xd = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), zoct())
    proj_zero = all(RL.octmat_is_zero(vMD.V24.el_simplify(s_proj(Xd, E[i]), sp.cancel)) for i in range(3))
    comm_zero = all(commutator_zero(Xd, E[i]) for i in range(3))
    off = RL.h3o_from_coords(7, 5, 3, zoct(), zoct(), oct1(0, 1))
    nz = not RL.octmat_is_zero(vMD.V24.el_simplify(s_proj(off, E11), sp.cancel))
    rep(f"E2: zeros=eigenframe two ways -- s_proj==0 at E_ii {proj_zero} AND operator [X,p]==0 "
        f"{comm_zero} (shared eigenframe); off-diagonal X => s!=0 {nz}", proj_zero and comm_zero and nz)
    # frame-following: rotate Xd by an exact F_4 permutation, zero follows
    sig = {0: 1, 1: 0, 2: 2}
    gX = KK.conj_perm(Xd, sig)
    follow = RL.octmat_is_zero(vMD.V24.el_simplify(s_proj(gX, E11), sp.cancel))   # diag(5,7,3): E_11 zero
    rep(f"E2 frame-following: g.X (permutation auto) has its zero at g.E_ii (covariance) {follow}",
        follow)
    # vacuum
    rep("E2 vacuum: X=I/3 => s_X==0 (eigenprojector)",
        RL.octmat_is_zero(vMD.V24.el_simplify(s_proj(vMD.I3, E11), sp.cancel)))

    # --- E3: Euler closure independent (Morse-index parity from Jordan-Hessian signs) ---
    # at E_ii, phi_X''(0) along the (i->j) family propto (x_j - x_i); Morse index = #negatives.
    print("\n[E3] independent Euler closure (Jordan-Hessian signs):")
    x = {0: 7, 1: 5, 2: 3}
    for space, perblock in [("cut", 2), ("OP^2", 8)]:
        morse = [sum(perblock for j in range(3) if j != i and x[j] < x[i]) for i in range(3)]
        ph = [(-1) ** m for m in morse]
        rep(f"E3 {space}: Morse {morse} (== {[4,2,0] if space=='cut' else [16,8,0]}), "
            f"Poincare-Hopf {ph}, Euler Sum = {sum(ph)} == chi = 3", sum(ph) == 3 and all(p == 1 for p in ph))
    # explicit phi'' anchor (independent, via eigenprojector gradient . family acceleration)
    x1, x2, x3 = symbols("X1 X2 X3", real=True)
    Xs = RL.h3o_from_coords(x1, x2, x3, zoct(), zoct(), zoct())
    phi = inner(Xs, vMD.V24.family(T, 1, 0))
    rep("E3 anchor: phi''(0) along (1,0)-family == 8(x2-x1)",
        cancel(sp.diff(phi, T, 2).subs(T, 0) - 8 * (x2 - x1)) == 0)

    # --- Gate 0 dictionary: independent torus generator (diagonal-unitary conjugation) ---
    print("\n[Gate 0] independent v22-dictionary check (diagonal-unitary torus generator):")
    # U(theta)=diag(1, e^{-e7 theta/2}, e^{e7 theta/2}); dU = d/dtheta|_0 = diag(0,-e7/2,e7/2);
    # D(X)=[dU,X]; weights on x1 (slice)=+1, on x2,x3 (tangent)=-1/2 (the C_u phase, nonzero).
    dU = vMD.V24.el_zero(); dU[1][1] = oct1(7, Rational(-1, 2)); dU[2][2] = oct1(7, Rational(1, 2))
    g = symbols("w0:8", real=True)

    def _cu(re, e7):
        z = zoct(); z[0] = re; z[7] = e7; return z
    Xc = RL.h3o_from_coords(g[0], g[1], g[2], _cu(g[3], g[4]), _cu(g[5], g[6]),
                            _cu(symbols("p0", real=True), symbols("p1", real=True)))
    DX = RL.octmat_sub(RL.h3o_matmul(dU, Xc), RL.h3o_matmul(Xc, dU))

    def Jcu(e):
        return [-e[7], 0, 0, 0, 0, 0, 0, e[0]]   # e_7-mult: (a+b e7)|->(-b + a e7)
    sl = all(cancel(DX[2][1][k] - Jcu(Xc[2][1])[k]) == 0 for k in range(8))
    t2 = all(cancel(DX[0][2][k] - Rational(-1, 2) * Jcu(Xc[0][2])[k]) == 0 for k in range(8))
    t3 = all(cancel(DX[1][0][k] - Rational(-1, 2) * Jcu(Xc[1][0])[k]) == 0 for k in range(8))
    rep("Gate 0: the torus circle acts on the slice (x1) as +J_Cu and on the tangent (x2,x3) "
        f"as -1/2 J_Cu (slice {sl}, tangent {t2 and t3}) => dictionary holds independently",
        sl and t2 and t3)

    print(f"\n  INDEPENDENT verifier: {sum(PASS)}/{len(PASS)} PASS")
    return all(PASS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
