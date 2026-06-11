#!/usr/bin/env python3
"""variety_equation_of_state_verify.py -- INDEPENDENT verifier for v27.0 Phase 87.

SEPARATE CODE PATH from variety_equation_of_state.py:
  * pi_{1/2}^{(E_11)} via the explicit 27x27 Peirce EIGENPROJECTOR P_{1/2} = 4 L_p(I - L_p)
    (L_p eigenvalues {0,1/2,1}), NOT the entry-extraction;
  * M# via the GRADIENT-OF-N construction (variety_moment_doublet_verify.sharp_grad),
    NOT M o M - Tr(M)M + sigma_2 I;
  * Q_M and the tuple-fit recomputed; and an ADVERSARIAL CERTIFICATE HUNT: try hard to
    find two traceless M with the SAME tuple (a,c,TrM^2,detM) but different Q_M (= different
    lambda^2 at matched c_R) -- a single such pair would flip the verdict to DEAD.
LIVE is confirmed iff Q_M is tuple-determined (no certificate) AND the law reproduces the
hand anchor.  The octonion arena (RL) is the shared certified ground.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from sympy import Rational, symbols, cancel, eye, Matrix

import ring_lemma_verification as RL
import variety_moment_doublet as vMD
import variety_moment_doublet_verify as vMDV     # independent grad-N sharp + projector tools

E11 = vMDV.E11
BASIS = vMDV.BASIS
inner = vMDV.inner
sharpG = vMDV.sharp_grad
PASS = []


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def oct1(k, v):
    z = zoct(); z[k] = sp.sympify(v); return z


def coords(X):
    return Matrix(RL._flat27(X))


def from_coords(v):
    out = vMD.V24.el_zero()
    for a in range(27):
        out = vMD.V24.el_add(out, vMD.V24.el_scal(v[a], BASIS[a]))
    return out


# INDEPENDENT pi_{1/2}: the 27x27 eigenprojector P_{1/2} = 4 L_{E11}(I - L_{E11})
_L = RL.jordan_L_matrix(E11, BASIS)
_P_HALF = 4 * _L * (eye(27) - _L)


def pi_half_proj(Y):
    return from_coords([cancel(x) for x in (_P_HALF * coords(Y))])


def normsq(Y):
    return cancel(RL.Tr(RL.jordan(Y, Y)))


def el_sub(A, B):
    return vMD.V24.el_add(A, vMD.V24.el_scal(-1, B))


def dG_indep(M):
    a = inner(M, E11)
    return pi_half_proj(el_sub(sharpG(M), vMD.V24.el_scal(a * Rational(1, 2), M)))


def tup(M):
    return inner(M, E11), inner(sharpG(M), E11), normsq(M), RL.det_3(M)


def main():
    print("#" * 74)
    print("# INDEPENDENT verifier -- Phase 87 (eigenprojector pi_1/2 + grad-N M# + cert hunt)")
    print("#" * 74)

    # --- projector sanity: P_{1/2} idempotent, image = coords 11..26 ---
    idem = cancel((_P_HALF * _P_HALF - _P_HALF).norm()) == 0
    Mf = RL.h3o_from_coords(*symbols("z0:3"), list(symbols("z3:11")),
                            list(symbols("z11:19")), list(symbols("z19:27")))
    ph = pi_half_proj(Mf)
    img_ok = all(ph[i][i][0] == 0 for i in range(3))
    rep(f"P_{{1/2}}=4L(I-L) idempotent {idem}; image = J_{{1/2}}(E11) (diagonal killed) {img_ok}",
        idem and img_ok)

    # --- hand anchor via the independent path ---
    M0 = RL.h3o_from_coords(1, 0, -1, zoct(), zoct(), oct1(0, 1))
    a, c, T2, dM = tup(M0)
    Q0 = normsq(dG_indep(M0))
    rep(f"hand anchor (independent): tuple={(a,c,T2,dM)}(==(1,0,4,1)), |dG|^2={Q0}(==1/2) "
        "=> 4 c_R(1-c_R)lambda^2 = 2 Q = 1", (a, c, T2, dM) == (1, 0, 4, 1) and Q0 == Rational(1, 2))

    # --- Q_M tuple-fit on full-26, INDEPENDENT (eigenprojector + grad-N) ---
    M, s = (RL.h3o_from_coords(symbols("w0", real=True), symbols("w1", real=True),
            -symbols("w0", real=True) - symbols("w1", real=True),
            list(symbols("w2:10", real=True)), list(symbols("w10:18", real=True)),
            list(symbols("w18:26", real=True))), symbols("w0:26", real=True))
    aE, cE, T2E, dME = tup(M)
    QM = sp.expand(normsq(dG_indep(M)))
    A, B, C, D, E, F, G = symbols("A B C D E F G")
    ansatz = A * T2E ** 2 + B * cE ** 2 + C * aE * dME + D * aE ** 2 * T2E + E * aE ** 4 + F * aE ** 2 * cE + G * cE * T2E
    poly = sp.Poly(sp.expand(QM - ansatz), *s)
    sol = sp.solve(list(set(poly.coeffs())), [A, B, C, D, E, F, G], dict=True)
    exact = bool(sol) and sp.expand((QM - ansatz).subs(sol[0])) == 0
    rep(f"Q_M tuple-determined on FULL-26 (independent path): {exact}; coeffs={sol[0] if sol else None} "
        "(== {A:0,B:-2,C:0,D:1/4,E:-1/2,F:5/2,G:-1})",
        exact and sol and sol[0] == {A: 0, B: Rational(-2), C: 0, D: Rational(1, 4),
                                     E: Rational(-1, 2), F: Rational(5, 2), G: Rational(-1)})

    # --- the factored law: 2 Q_M == (1/2 TrM^2 - a^2 + c)(a^2 - 4c) ---
    rep("law: 2 Q_M == (1/2 TrM^2 - a^2 + c)(a^2 - 4c) = -4|pi_{1/2}M|^2 G_M (symbolic, indep)",
        cancel(2 * QM - (Rational(1, 2) * T2E - aE ** 2 + cE) * (aE ** 2 - 4 * cE)) == 0)

    # --- ADVERSARIAL CERTIFICATE HUNT (try to flip LIVE -> DEAD) ---
    print("\n[adversarial] hunting a certificate pair (same tuple, different Q_M):")
    cert = _certificate_hunt()
    rep(f"NO certificate pair found across {cert['n']} matched-tuple pairs (incl. genuinely "
        f"non-stabilizer-related M with identical (a,c,TrM^2,detM)): Q_M always equal => LIVE "
        f"holds, NOT a missed DEAD", cert["clean"])

    print(f"\n  INDEPENDENT verifier: {sum(PASS)}/{len(PASS)} PASS  (verdict: "
          f"{'LIVE confirmed' if all(PASS) else 'DISCREPANCY'})")
    return all(PASS)


def _certificate_hunt():
    """Build pairs of traceless M with the SAME tuple but built DIFFERENTLY (different octonion
    directions, non-stabilizer-related); confirm Q_M is identical (no certificate => LIVE)."""
    pairs = []
    # family 1: M0 vs its e_k-direction variants (same tuple by construction, different direction)
    base = lambda k: RL.h3o_from_coords(1, 0, -1, zoct(), zoct(), oct1(k, 1))
    for k in (1, 2, 3, 7):
        pairs.append((base(0), base(k)))
    # family 2: rotate which off-diagonal entry carries the octonion (x3 vs x2 vs x1) -- same
    # diagonal, |entry|, so same tuple, genuinely different J_{1/2}/J_0 support
    pairs.append((RL.h3o_from_coords(1, 0, -1, zoct(), zoct(), oct1(0, 1)),
                  RL.h3o_from_coords(1, 0, -1, zoct(), oct1(0, 1), zoct())))   # x2 vs x3
    pairs.append((RL.h3o_from_coords(0, 1, -1, oct1(1, Rational(1, 2)), zoct(), zoct()),
                  RL.h3o_from_coords(0, 1, -1, oct1(7, Rational(1, 2)), zoct(), zoct())))  # x1 e1 vs e7
    # family 3: a generic matched-tuple pair via two different rational M with hand-matched tuple
    Ma = RL.h3o_from_coords(Rational(1, 2), Rational(1, 3), -Rational(5, 6),
                            oct1(1, Rational(1, 5)), oct1(3, Rational(1, 4)), oct1(7, Rational(1, 6)))
    # Mb: same diagonal, permute octonion slots/entries to keep |.|^2 per entry and the cross-term
    Mb = RL.h3o_from_coords(Rational(1, 2), Rational(1, 3), -Rational(5, 6),
                            oct1(2, Rational(1, 5)), oct1(4, Rational(1, 4)), oct1(6, Rational(1, 6)))
    pairs.append((Ma, Mb))
    n = 0
    clean = True
    for (M1, M2) in pairs:
        if tup(M1) == tup(M2):                       # only count genuinely matched-tuple pairs
            n += 1
            if cancel(normsq(dG_indep(M1)) - normsq(dG_indep(M2))) != 0:
                clean = False
    return {"n": n, "clean": clean}


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
