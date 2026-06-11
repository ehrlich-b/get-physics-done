#!/usr/bin/env python3
"""variety_moment_doublet_verify.py -- INDEPENDENT verifier for v25.0 Phase 85.

SEPARATE CODE PATH from variety_moment_doublet.py (NO covariance shortcut for C1):
  * compression  C_p X  via the explicit 27x27 L_p EIGENPROJECTOR P_0 (Lagrange
    interpolation as a matrix), NOT the nested 2 L^2 - 3 L + 1 jordan calls;
  * sharp  X#  via the GRADIENT-OF-N construction  <X#,E_a> = (1/2) d(X,X,E_a)
    reconstructed through the trace-form Gram dual, NOT  X o X - Tr(X)X + S(X)I;
  * det_2 of the face at E_11 via the LITERAL lower 2x2 block determinant
    beta*gamma - |x1|^2, NOT (Tr^2 - Tr(YoY))/2.
The octonion ARENA (RL.oct_mul/Tr/det_3/polarize_d) is the shared certified ground
(there is one octonion algebra; using it is not borrowing the proof).  CONVENTION
TRIAGE FIRST: reproduce the recorded v24 anchors; only then are C1/C2 substantive.

C1: brute symbolic expansion at E_11 (27 params) + along the off-u (1,1) family over
    Q(t).  C2: a DIFFERENT frame (rotated cut) + lambda_1 from a DIFFERENT component
    (E_22) + the field equation Delta m = -lambda(m - (2/3)Tr X) checked directly.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from sympy import Rational, symbols, cancel, Matrix, eye, together

import ring_lemma_verification as RL
import variety_entropy_landscape as V24   # ONLY for octonion-list helpers + family geometry

T = symbols("t")
PASS = []


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


BASIS = RL._standard_basis_27()              # 27 standard h_3(O) basis elements
IDENT = RL.h3o_identity()


def E_ij_diag(i):
    d = [Rational(1) if k == i else Rational(0) for k in range(3)]
    return RL.h3o_from_coords(d[0], d[1], d[2], RL.oct_zero(), RL.oct_zero(), RL.oct_zero())


E11 = E_ij_diag(0)
E22 = E_ij_diag(1)
I3 = V24.el_scal(Rational(1, 3), IDENT)


def coords(X):
    return Matrix(RL._flat27(X))


def from_coords(v):
    """Rebuild an h_3(O) element from a 27-vector (inverse of _flat27, via the basis)."""
    out = V24.el_zero()
    for a in range(27):
        out = V24.el_add(out, V24.el_scal(v[a], BASIS[a]))
    return out


# ---- INDEPENDENT compression: the 27x27 eigenprojector P_0(p) ---------------
def compress0_proj(p, X):
    """C_p X via P_0 = (L_p - 1/2 I)(L_p - I)/((0-1/2)(0-1)) as a 27x27 matrix."""
    L = RL.jordan_L_matrix(p, BASIS)         # 27x27 multiplication-by-p matrix
    P0 = (L - Rational(1, 2) * eye(27)) * (L - eye(27)) / Rational(1, 2)
    y = P0 * coords(X)
    return from_coords([cancel(c) for c in y])


# ---- INDEPENDENT sharp: gradient of the cubic norm via the Gram dual --------
_GRAM = Matrix(27, 27, lambda a, b: RL.Tr(RL.jordan(BASIS[a], BASIS[b])))
_GRAM_INV = _GRAM.inv()


def sharp_grad(X):
    """X# from <X#, E_a> = (1/2) d(X,X,E_a):  X#_coords = Gram^{-1} . (1/2 d-vector)."""
    dvec = Matrix([Rational(1, 2) * RL.polarize_d(X, X, BASIS[a]) for a in range(27)])
    xs = _GRAM_INV * dvec
    return from_coords([cancel(c) for c in xs])


def inner(A, B):
    return RL.Tr(RL.jordan(A, B))


# ---- family geometry (rebuilt; the arena, not the claim) -------------------
def fam(t, j, k):
    return V24.family(t, j, k)


def litdet2_at_E11(Y):
    """Literal lower 2x2 block determinant of Y at E_11: beta*gamma - |x1|^2."""
    _, beta, gamma, x1, _, _ = RL._coord_from_octmat(Y)
    return cancel(beta * gamma - sum(x1[i] ** 2 for i in range(8)))


# ============================================================================
def main():
    print("#" * 74)
    print("# INDEPENDENT verifier -- Phase 85 (eigenprojector + grad-N sharp + literal det2)")
    print("#" * 74)

    # ---- 0. convention triage: reproduce recorded v24 anchors --------------
    print("\n[0] convention triage -- reproduce recorded v24 anchors via THIS path:")
    Xd = V24.state_diagonal()
    Y0 = compress0_proj(E11, Xd)
    m0 = RL.Tr(Y0)
    q0 = litdet2_at_E11(Y0)
    rep(f"diag(7,5,3) @E_11 via eigenprojector+literal-det2: m={m0}, q={q0}, r={cancel(q0/m0**2)} "
        f"(==8,15,15/64)", m0 == 8 and q0 == 15 and cancel(q0 / m0 ** 2) == Rational(15, 64))
    Xg = V24.state_generic()
    p11 = fam(T, 1, 1)
    Yg = compress0_proj(p11, Xg)
    rg = together(cancel((RL.Tr(Yg) ** 2 - RL.Tr(RL.jordan(Yg, Yg))) / 2) / RL.Tr(Yg) ** 2)
    rep(f"generic off-u r(2)={cancel(rg.subs(T,2))} (==2727493/12700800)",
        cancel(rg.subs(T, 2)) == Rational(2727493, 12700800))

    # ---- sharp triage: grad-N sharp reproduces (X#)#=N X and anchors -------
    Xs = sharp_grad(Xg)
    adj = all(cancel(c) == 0 for c in (coords(sharp_grad(Xs)) - RL.det_3(Xg) * coords(Xg)))
    rep(f"grad-N sharp: (X#)# == det_3(X) X  (independent adjugate identity)", adj)

    # ---- 1. C1 brute at E_11, symbolic X (27 params), NO covariance --------
    print("\n[1] C1 brute: symbolic X (27 params) at E_11 (independent compression+sharp):")
    xs = symbols("Z0:27", real=True)
    Xsym = RL.h3o_from_coords(xs[0], xs[1], xs[2], list(xs[3:11]),
                              list(xs[11:19]), list(xs[19:27]))
    Y = compress0_proj(E11, Xsym)
    m_lhs = sp.expand(RL.Tr(Y))
    q_lhs = sp.expand(litdet2_at_E11(Y))
    m_rhs = sp.expand(RL.Tr(Xsym) - inner(Xsym, E11))
    q_rhs = sp.expand(inner(sharp_grad(Xsym), E11))
    rep("C1 @E_11: m_LHS(eigenproj) == Tr(X)-<X,E11>", sp.simplify(m_lhs - m_rhs) == 0)
    rep("C1 @E_11: q_LHS(literal-det2) == <X#_gradN, E11>", sp.simplify(q_lhs - q_rhs) == 0)

    # ---- C1 brute along the off-u (1,1) family over Q(t), symbolic X -------
    print("\n[2] C1 brute along off-u (1,1) family over Q(t), symbolic X (no shortcut):")
    p = fam(T, 1, 1)
    Y = compress0_proj(p, Xsym)
    m_l = cancel(RL.Tr(Y))
    # det_2 along a general p via (Tr^2 - Tr(YoY))/2 ON the eigenprojector-compressed Y
    q_l = cancel((RL.Tr(Y) ** 2 - RL.Tr(RL.jordan(Y, Y))) / 2)
    m_r = cancel(RL.Tr(Xsym) - inner(Xsym, p))
    q_r = cancel(inner(sharp_grad(Xsym), p))
    rep("C1 off-u(1,1): m_LHS == Tr(X)-<X,p>  (symbolic X, Q(t))", cancel(m_l - m_r) == 0)
    rep("C1 off-u(1,1): q_LHS == <X#_gradN, p>  (symbolic X, Q(t))", cancel(q_l - q_r) == 0)

    # ---- 3. C2 independent: DIFFERENT frame + lambda from E_22 component ----
    print("\n[3] C2 independent: rotated-cut frame + lambda_1 from the E_22 component:")
    DP = _rotated_cut_meancurv()
    # independent lambda extraction: use the E_22 diagonal component, NOT E_11.
    DP22 = DP[1][1][0]
    target22 = (E11[1][1][0] - Rational(1, 3))      # (E_11 - I/3)_{22} = -1/3
    lam_cut = cancel(-DP22 / target22)
    full_id = all(cancel(c) == 0 for c in (coords(DP) + lam_cut * coords(V24.el_add(E11, V24.el_scal(-1, I3)))))
    rep(f"rotated-cut DeltaP = {_d(DP)}, lambda_1 (from E_22 comp) = {lam_cut} (==12), "
        f"full-vector DeltaP==-12(E11-I/3): {full_id}", lam_cut == 12 and full_id)

    # full OP^2 frame, independent assembly, lambda from E_22
    DPf = _full_meancurv()
    lam_full = cancel(-DPf[1][1][0] / target22)
    rep(f"OP^2 16-frame DeltaP = {_d(DPf)}, lambda_1 (from E_22 comp) = {lam_full} (==48)",
        lam_full == 48)

    # ---- field equation checked DIRECTLY for symbolic X --------------------
    print("\n[4] field equation  Delta m = -lambda (m - (2/3)Tr X)  directly, symbolic X:")
    # Delta m (E_11) = sum_i (1/4) d^2/dt^2 m(p_i(t); X) |_0  over the 16-frame
    dm = sp.Integer(0)
    for j in (1, 2):
        for k in range(8):
            mt = RL.Tr(Xsym) - inner(Xsym, fam(T, j, k))
            dm += Rational(1, 4) * sp.diff(mt, T, 2).subs(T, 0)
    m_at_E11 = RL.Tr(Xsym) - inner(Xsym, E11)
    rhs = -48 * (m_at_E11 - Rational(2, 3) * RL.Tr(Xsym))
    rep("Delta m == -48 (m - (2/3) Tr X)  [symbolic X, 16-frame]", sp.expand(dm - rhs) == 0)
    # and for q with sigma_2/3
    dq = sp.Integer(0)
    for j in (1, 2):
        for k in range(8):
            qt = inner(sharp_grad(Xsym), fam(T, j, k))
            dq += Rational(1, 4) * sp.diff(qt, T, 2).subs(T, 0)
    q_at_E11 = inner(sharp_grad(Xsym), E11)
    s2 = (RL.Tr(Xsym) ** 2 - RL.Tr(RL.jordan(Xsym, Xsym))) / 2
    rhsq = -48 * (q_at_E11 - s2 / 3)
    rep("Delta q == -48 (q - sigma_2(X)/3)  [symbolic X, 16-frame]", sp.expand(dq - rhsq) == 0)

    print(f"\n  INDEPENDENT verifier: {sum(PASS)}/{len(PASS)} PASS")
    return all(PASS)


def _d(X):
    return "diag(" + ", ".join(str(X[i][i][0]) for i in range(3)) + ")"


def _meancurv(builders):
    DP = V24.el_zero()
    for b in builders:
        p = b(T)
        d2 = [[[sp.diff(p[i][j][k], T, 2).subs(T, 0) for k in range(8)]
               for j in range(3)] for i in range(3)]
        DP = V24.el_add(DP, V24.el_scal(Rational(1, 4), d2))
    return V24.el_simplify(DP, sp.cancel)


def _full_meancurv():
    return _meancurv([(lambda t, j=j, k=k: fam(t, j, k)) for j in (1, 2) for k in range(8)])


def _rotated_cut_meancurv():
    """Different cut frame than the main driver's 3/5-4/5: use the 5/13-12/13 rotation."""
    a, b = Rational(5, 13), Rational(12, 13)
    one = V24.oct1(0, 1)
    e7 = V24.oct1(7, 1)

    def cu(t, va, vb):
        c, s = V24._pyth(t)
        return V24.herm_from_vec([V24.oct1(0, c),
                                  [s * va[i] for i in range(8)],
                                  [s * vb[i] for i in range(8)]])
    dirs = [
        (lambda t: cu(t, [a * one[i] for i in range(8)], [b * one[i] for i in range(8)])),
        (lambda t: cu(t, [-b * one[i] for i in range(8)], [a * one[i] for i in range(8)])),
        (lambda t: cu(t, [a * e7[i] for i in range(8)], [b * e7[i] for i in range(8)])),
        (lambda t: cu(t, [-b * e7[i] for i in range(8)], [a * e7[i] for i in range(8)])),
    ]
    return _meancurv(dirs)


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
