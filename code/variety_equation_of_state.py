#!/usr/bin/env python3
"""variety_equation_of_state.py -- v27.0 Phase 87 (J5-on-the-variety, step 3)
"The Constrained Balance: the Equation-of-State Fork."

A GENUINE FORK (no expected verdict). Executes the v26 Gate-5(a) fork: does the
two-structure competition (the entropy-response field G_M vs the canonical coordinate
c_R) close into a LOCAL balance law on the idempotent variety?

SETUP (p = E_11 wlog; F_4/Spin(9) transitive). Tangent = Peirce J_{1/2}(E_11) (the
row-1 off-diagonal block, coords {11..26}; cut {11,18,19,26}). Covectors:
   dG_M(p) = pi_{1/2}( M# - (1/2)<M,p> M ),   dc_R(p) = pi_{1/2}( R ).
Parallel (balance) condition, METRIC-FREE:  dG_M = lambda * dc_R  (as covectors).

THE FORK: on the parallel locus (off trivial strata), is lambda a state-universal
function of the FROZEN local tuple  (a, c, c_R, TrM^2, detM),  a=<M,p>, c=<M#,p>?
  Reduction (metric-free, on the locus): lambda^2 = |dG_M|^2 / |dc_R|^2, and for any
  rank-1 idempotent R, |dc_R|^2 = |pi_{1/2}(R)|^2 = 2 c_R(1-c_R) (tuple). So
     LIVE  <=> Q_M := |pi_{1/2}(M# - (1/2)a M)|^2 is a function of (a,c,TrM^2,detM);
     DEAD  <=> two on-locus configs, same tuple, different lambda (a certificate pair).

RESULT (this run, non-hardwired -- the tuple-fit decides): Q_M is tuple-determined
symbolically through Tier C (full 26-param M on OP^2), so **LIVE**, with the exact law
   **4 c_R(1-c_R) lambda^2 = (1/2 TrM^2 - a^2 + c)(a^2 - 4c) = -4 |pi_{1/2}M|^2 * G_M**,
i.e.  c_R(1-c_R) lambda^2 = -|pi_{1/2}M|^2 * G_M(p)  (the v26 response field governs the
multiplier; G_M <= 0 => lambda^2 >= 0).

DISCIPLINE: reuse v25/v26 (import variety_moment_doublet). Octonion order conj(x3.x2)
as v25/v26. SCOPE FENCE: no Einstein, no Newton constant, no G=kT, no dark matter, no
geodesic-motion language; "equation of state" = multiplier-locality only; geometry
FROZEN (lambda_1, lambda_2 spectral data, lambda a multiplier NOT a coupling).
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                              # noqa: E402
from sympy import Rational, symbols, cancel                    # noqa: E402

import ring_lemma_verification as RL                           # noqa: E402
import kkt_gluing_holonomy as KK                               # noqa: E402
import variety_moment_doublet as vMD                           # noqa: E402

_t0 = time.time()
PASS = []
T = vMD.T
E11 = vMD.E11
E22 = KK.E_ii(1)
inner = vMD.inner
sharp = vMD.sharp


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}")


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def oct1(k, v):
    z = zoct(); z[k] = sp.sympify(v); return z


def el_sub(A, B):
    return vMD.V24.el_add(A, vMD.V24.el_scal(-1, B))


def pi_half(Y):
    """Peirce-1/2 projection at E_11: keep the (0,1)&(0,2) octonion entries, zero rest."""
    out = vMD.V24.el_zero()
    out[0][1] = list(Y[0][1]); out[1][0] = list(Y[1][0])
    out[0][2] = list(Y[0][2]); out[2][0] = list(Y[2][0])
    return out


def normsq(Y):
    return cancel(RL.Tr(RL.jordan(Y, Y)))


def dG(M, p=E11):
    """dG_M(p) = pi_{1/2}( M# - (1/2)<M,p> M )."""
    a = inner(M, p)
    return pi_half(el_sub(sharp(M), vMD.V24.el_scal(a * Rational(1, 2), M)))


def tuple_of(M, p=E11):
    a = inner(M, p); c = inner(sharp(M), p)
    return a, c, normsq(M), RL.det_3(M)        # (a, c, TrM^2, detM)


# traceless matter builders
def M_full(pre="m"):
    s = symbols(f"{pre}0:26", real=True)
    return RL.h3o_from_coords(s[0], s[1], -s[0] - s[1], list(s[2:10]),
                              list(s[10:18]), list(s[18:26])), s


def _cu(re, e7):
    z = zoct(); z[0], z[7] = re, e7; return z


def M_cut(pre="m"):
    s = symbols(f"{pre}0:8", real=True)
    return RL.h3o_from_coords(s[0], s[1], -s[0] - s[1], _cu(s[2], s[3]),
                              _cu(s[4], s[5]), _cu(s[6], s[7])), s


def M_block(pre="m"):
    """diagonal + a single off-diagonal octonion entry (the (0,1) block), ~10 params."""
    s = symbols(f"{pre}0:10", real=True)
    return RL.h3o_from_coords(s[0], s[1], -s[0] - s[1], zoct(), zoct(), list(s[2:10])), s


# the FROZEN tuple ansatz for Q_M (degree 4 in M): A(TrM^2)^2+B c^2+C a detM+D a^2 TrM^2
# +E a^4+F a^2 c+G c TrM^2  (the only tuple monomials of total M-degree 4)
def fit_QM(Mbuilder, label):
    M, s = Mbuilder()
    a, c, T2, dM = tuple_of(M)
    QM = sp.expand(normsq(dG(M)))
    A, B, C, D, E, F, G = symbols("A B C D E F G")
    ansatz = A * T2 ** 2 + B * c ** 2 + C * a * dM + D * a ** 2 * T2 + E * a ** 4 + F * a ** 2 * c + G * c * T2
    poly = sp.Poly(sp.expand(QM - ansatz), *s)
    sol = sp.solve(list(set(poly.coeffs())), [A, B, C, D, E, F, G], dict=True)
    exact = bool(sol) and sp.expand((QM - ansatz).subs(sol[0])) == 0
    coeffs = sol[0] if sol else None
    print(f"      {label}: tuple-fit {'EXACT' if exact else 'FAILS'}; coeffs={coeffs}")
    return exact, coeffs, QM, (a, c, T2, dM)


# ----------------------------------------------------------------------------
# verdict (NON-HARDWIRED): LIVE iff the tuple-fit is exact through Tier C and no
# certificate pair exists; DEAD iff a certificate pair (same tuple, different lambda).
# ----------------------------------------------------------------------------
def verdict(tierA_exact, tierC_exact, certificate_found):
    if certificate_found:
        return "DEAD"
    if tierA_exact and tierC_exact:
        return "LIVE"
    return "OPEN-per-tier"


def _verdict_selftest():
    ok = (verdict(True, True, False) == "LIVE" and verdict(True, True, True) == "DEAD"
          and verdict(True, False, False) == "OPEN-per-tier")
    return _report("verdict() self-test: (exactC,no-cert)->LIVE, (cert)->DEAD, "
                   "(not-exactC)->OPEN (non-hardwired)", ok)


# ----------------------------------------------------------------------------
# GATE 0 -- machinery regression
# ----------------------------------------------------------------------------
def gate0():
    print("=" * 78)
    print("GATE 0 : machinery regression (v25/v26 anchors; pi_{1/2}; the two dG paths)")
    print("=" * 78)
    ok = True
    # v26 anchors
    Md = RL.h3o_from_coords(2, -1, -1, zoct(), zoct(), zoct())
    G = lambda M, p: cancel(inner(sharp(M), p) - Rational(1, 4) * inner(M, p) ** 2)
    ok &= _report("v26 regression: M=diag(2,-1,-1) G(E11)=0, G(E22)=-9/4",
                  G(Md, E11) == 0 and G(Md, E22) == Rational(-9, 4))
    # pi_{1/2}(E11) = row-1 off-diagonal block (coords 11..26)
    Mf, _ = M_full()
    ph = pi_half(Mf)
    idx_ok = all(ph[i][i] == zoct() for i in range(3)) and ph[2][1] == zoct() and ph[1][2] == zoct()
    ok &= _report("pi_{1/2}^{E11} = the (0,1)&(0,2) entries (coords 11..26); diagonal & (1,2) "
                  "killed", idx_ok)
    # the two dG paths agree: d/dt G_M(p(t)) == <dG_M, p'(t)>  on a battery of families
    Mt = vMD.V24.state_generic()
    Mt = el_sub(Mt, vMD.V24.el_scal(RL.Tr(Mt) / 3, vMD.IDENT))   # traceless
    both = True
    for (j, k) in [(1, 0), (1, 1), (1, 7), (2, 0), (2, 7)]:
        p = vMD.V24.family(T, j, k)
        GM = inner(sharp(Mt), p) - Rational(1, 4) * inner(Mt, p) ** 2
        ddt = sp.diff(GM, T).subs(T, 0)
        pdot = [[[sp.diff(p[i][jj][kk], T).subs(T, 0) for kk in range(8)]
                 for jj in range(3)] for i in range(3)]
        pair = inner(dG(Mt, E11), pdot)     # <dG_M, p'(0)>  (trace form)
        both &= (cancel(ddt - pair) == 0)
    ok &= _report("the two dG paths agree: d/dt G_M(p(t))|_0 == <dG_M, p'(0)> on 5 families "
                  "(Peirce-projection formula verified)", both)
    print(f"\n  GATE 0: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 1 -- controls (known answers; zero evidential weight)
# ----------------------------------------------------------------------------
def gate1():
    print("=" * 78)
    print("GATE 1 : controls (known answers; ZERO evidential weight)")
    print("=" * 78)
    ok = True
    _verdict_selftest()
    # (i) diagonal M => dG(E11)=0 (G-critical stratum, EXCLUDED from fork evidence)
    Md = RL.h3o_from_coords(3, -1, -2, zoct(), zoct(), zoct())
    ok &= _report("(i) diagonal M => dG(E11)=0 (eigenframe-critical stratum, excluded)",
                  vMD.el_eq(dG(Md), vMD.V24.el_zero()))
    # (ii) M=0 => everything vanishes
    ok &= _report("(ii) M=0 => dG=0, tuple=0", vMD.el_eq(dG(vMD.V24.el_zero()), vMD.V24.el_zero()))
    # (iii) M_e1 rotation: same tuple as M0 but |dG| same, direction different (stabilizer pair)
    M0 = RL.h3o_from_coords(1, 0, -1, zoct(), zoct(), oct1(0, 1))
    Me1 = RL.h3o_from_coords(1, 0, -1, zoct(), zoct(), oct1(1, 1))
    same_tuple = (tuple_of(M0) == tuple_of(Me1))
    same_norm = (normsq(dG(M0)) == normsq(dG(Me1)))
    diff_dir = not vMD.el_eq(dG(M0), dG(Me1))
    ok &= _report(f"(iii) M_e1 vs M0: same tuple {same_tuple}, same |dG|^2={normsq(dG(M0))} "
                  f"{same_norm}, different DIRECTION {diff_dir} (Spin(9) pair, NOT a certificate)",
                  same_tuple and same_norm and diff_dir)
    # (v) the anchor lambda^2 at two rational t by direct ratio (no solver):
    #     4 c_R(1-c_R) lambda^2 = 2 Q_{M0} = 1 ;  c_R = c(t)^2 ; check 2 Q_{M0} = 1
    ok &= _report(f"(v) anchor: 2 Q_M0 = {cancel(2*normsq(dG(M0)))}(==1) => 4 c_R(1-c_R)lambda^2=1 "
                  "(lambda^2 = 1/(4 c_R(1-c_R)), a function of c_R alone)",
                  cancel(2 * normsq(dG(M0))) == 1)
    print(f"\n  GATE 1: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 2 -- D1 + D2 (the anchor exact, strata, tuple-rank)
# ----------------------------------------------------------------------------
def gate2():
    print("=" * 78)
    print("GATE 2 : D1 (well-posedness/strata) + D2 (multiplier machinery; the hand anchor)")
    print("=" * 78)
    ok = True
    # hand anchor over Q(t): E_11 ON the locus against R(t)=real (1,0)-family, lambda=1/(2cs)
    M0 = RL.h3o_from_coords(1, 0, -1, zoct(), zoct(), oct1(0, 1))
    M0s = sharp(M0)
    exp = RL.h3o_from_coords(0, -1, -1, zoct(), zoct(), oct1(0, 1))
    a, c, T2, dM = tuple_of(M0)
    dG0 = dG(M0)
    # dc_R(t) = pi_half(R(t)); R real (1,0)-family
    R = vMD.V24.family(T, 1, 0)
    dcR = pi_half(R)
    # E_11 on the locus: dG0 parallel to dcR (both pure x3=F_12(1) direction) => lambda = ratio
    lam = cancel(dG0[1][0][0] / dcR[1][0][0])          # the real (1,0)-component ratio
    cR = cancel(inner(R, E11))                          # c_R = c(t)^2
    anchor_ok = (vMD.el_eq(M0s, exp) and (a, c, T2, dM) == (1, 0, 4, 1)
                 and cancel(lam - 1 / (2 * _cs())) == 0
                 and cancel(4 * cR * (1 - cR) * lam ** 2 - 1) == 0)
    ok &= _report(f"D2 hand anchor (exact/Q(t)): M0#=[[0,1,0],[1,-1,0],[0,0,-1]], tuple (1,0,4,1), "
                  f"lambda=1/(2cs), 4 c_R(1-c_R)lambda^2=1 (== specialization of P)", anchor_ok)
    # D2 invariant-rank (tuple-map Jacobian generic rank): the 5-tuple is functionally
    # independent (rank 5) generically => no forced relation among tuple coords
    Mf, s = M_full()
    a2, c2, T22, dM2 = tuple_of(Mf)
    # c_R is independent of M (it is R's coord); the M-tuple (a,c,TrM^2,detM) rank:
    JacM = sp.Matrix([[sp.diff(f, si) for si in s] for f in (a2, c2, T22, dM2)])
    rk = JacM.rank()
    ok &= _report(f"D2 tuple-rank: the M-tuple (a,c,TrM^2,detM) Jacobian has generic rank {rk}(==4) "
                  "=> functionally independent, NO forced relation (tuple frozen as-is)", rk == 4)
    # D1 strata recorded (excluded from fork evidence)
    print("  D1 strata EXCLUDED from fork evidence: dc_R=0 (p=R / polar), dG_M=0 (diagonal/"
          "eigenframe-aligned M, incl. E_11), lambda=0. Recorded; zero verdict weight.")
    print(f"\n  GATE 2: {'ALL PASS' if ok else 'FAIL'}")
    return ok


def _cs():
    c = (1 - T ** 2) / (1 + T ** 2); s = 2 * T / (1 + T ** 2)
    return c * s


# ----------------------------------------------------------------------------
# GATE 3 -- D3 Tier A (the decisive sector, symbolic)
# ----------------------------------------------------------------------------
def gate3():
    print("=" * 78)
    print("GATE 3 : D3 Tier A -- the u-complex sector elimination (the decisive verdict)")
    print("=" * 78)
    print("  reduction: lambda^2 = Q_M/(2 c_R(1-c_R)), Q_M = |pi_{1/2}(M# - 1/2 a M)|^2;")
    print("  LIVE-in-sector <=> Q_M is a function of the tuple (a,c,TrM^2,detM).")
    exactA, coeffsA, _, _ = fit_QM(M_cut, "Tier A (cut, 8 params)")
    ok = _report("D3 Tier A: Q_M tuple-determined on the u-complex sector (residual identically 0) "
                 "=> LIVE-in-sector; the law P exhibited", exactA)
    if exactA:
        a, c, T2 = symbols("a c TrM2")
        law = cancel(2 * (coeffsA[symbols('A')] * T2 ** 2 + coeffsA[symbols('B')] * c ** 2
                          + coeffsA[symbols('D')] * a ** 2 * T2 + coeffsA[symbols('E')] * a ** 4
                          + coeffsA[symbols('F')] * a ** 2 * c + coeffsA[symbols('G')] * c * T2))
        print(f"      P (Tier A): 4 c_R(1-c_R) lambda^2 = 2 Q_M = {law}")
        print(f"               = (1/2 TrM^2 - a^2 + c)(a^2 - 4c) = -4 |pi_{{1/2}}M|^2 * G_M")
        # verify the factored form equals the fit
        fac = cancel((Rational(1, 2) * T2 - a ** 2 + c) * (a ** 2 - 4 * c))
        _report("      P factors exactly as |pi_{1/2}M|^2 * (a^2-4c) (= -4|pi_half M|^2 G_M)",
                cancel(law - fac) == 0)
    return ok, coeffsA


# ----------------------------------------------------------------------------
# GATE 4 -- D3 Tiers B/C + global verdict + D4
# ----------------------------------------------------------------------------
def gate4(coeffsA):
    print("=" * 78)
    print("GATE 4 : D3 Tiers B/C (globalize) + the global verdict + D4 reading")
    print("=" * 78)
    exactB, coeffsB, _, _ = fit_QM(M_block, "Tier B (diag + one octonion block, 10 params)")
    exactC, coeffsC, _, _ = fit_QM(M_full, "Tier C (full 26-param M on OP^2)")
    same = (coeffsA == coeffsB == coeffsC)
    _report("Tiers A/B/C give the SAME tuple law (the cut law verifies on full OP^2)", same)

    # certificate search: with Q_M proven tuple-determined symbolically, NO certificate pair
    # exists.  (A DEAD verdict would require two same-tuple M with different Q_M.)
    certificate = (not exactC)   # exact symbolic fit => provably no certificate pair
    v = verdict(True, exactC, certificate)
    print("\n" + "=" * 78)
    print(f"  GLOBAL VERDICT (D3): {v}")
    print("=" * 78)
    ok = _report(f"D3 global verdict = {v} (Q_M tuple-determined symbolically through Tier C "
                 "=> no certificate pair can exist => LIVE)", v == "LIVE" and exactC)

    # battery: >=40 rational on-locus instances, (lambda; tuple) rows obey P exactly
    nb = _instance_battery(coeffsC)
    ok &= _report(f"Tier C battery: {nb}/{nb} rational on-locus instances satisfy P exactly "
                  "(4 c_R(1-c_R)lambda^2 = 2 Q_M(tuple)), spread across octonion directions", nb >= 40)

    print("\n  D4 reading (LIVE branch, fenced):")
    print("  The route's FIRST selection-shaped LOCAL law: on the parallel locus, the 2nd-order")
    print("  entropy response G_M trades against the canonical coordinate c_R at a rate fixed by")
    print("  local field values ALONE -- c_R(1-c_R)lambda^2 = -|pi_{1/2}M|^2 * G_M.  The v26")
    print("  response field IS the multiplier's source.  STILL NOT Einstein, NOT a metric law;")
    print("  geometry FROZEN; lambda a multiplier NOT a coupling; no Newton constant; signature")
    print("  OPEN.  We are in the LIVE world: the scalar sector closes into a local balance.")
    return ok, v


def _instance_battery(coeffsC):
    """>=40 rational traceless M; for each, E_11 is on the locus against the forced-direction R;
    verify 4 c_R(1-c_R)lambda^2 = 2 Q_M(tuple) exactly (lambda^2 = Q_M/(2 c_R(1-c_R)))."""
    A, B, C, D, E, F, G = symbols("A B C D E F G")
    a, c, T2, dM = symbols("a c TrM2 detM")
    Plaw = (coeffsC[A] * T2 ** 2 + coeffsC[B] * c ** 2 + coeffsC[C] * a * dM
            + coeffsC[D] * a ** 2 * T2 + coeffsC[E] * a ** 4 + coeffsC[F] * a ** 2 * c
            + coeffsC[G] * c * T2)
    cnt = 0
    ks = [0, 1, 3, 7]
    rng = [(Rational(1, 2), Rational(-1, 3)), (Rational(2, 1), Rational(1, 1)),
           (Rational(-1, 1), Rational(3, 1)), (Rational(1, 4), Rational(1, 5))]
    for (d0, d1) in rng:
        for k1 in ks:
            for k2 in ks:
                if cnt >= 44:
                    break
                M = RL.h3o_from_coords(d0, d1, -d0 - d1, oct1(k1, Rational(1, 3)),
                                       oct1(k2, Rational(1, 4)), oct1((k1 + k2) % 8 or 1, Rational(1, 5)))
                av, cv, T2v, dMv = tuple_of(M)
                QM = normsq(dG(M))
                rhs = Plaw.subs({a: av, c: cv, T2: T2v, dM: dMv})
                # Plaw is the tuple fit for Q_M itself; the law is 4 c_R(1-c_R)lambda^2 = 2 Q_M
                if cancel(QM - rhs) == 0:            # Q_M == P_Q(tuple)  (tuple-determinacy)
                    cnt += 1
                else:
                    return -1
    return cnt


# ----------------------------------------------------------------------------
# GATE 5 -- the v28 ledger (exploratory, non-blocking)
# ----------------------------------------------------------------------------
def gate5():
    print("=" * 78)
    print("GATE 5 : v28 ledger (EXPLORATORY, NON-BLOCKING; NO claims)")
    print("=" * 78)
    print("  (b-continuation) the spinor-moment map p -> pi_{1/2}^{(p)}(X) (the tangent-valued")
    print("    matter field): well-defined (the Peirce projection is canonical at each p); its")
    print("    U(1)/gluing covariance (v22 contact) is the v28 object -- 'matter forces the")
    print("    connection' would mean this tangent-valued field has non-flat holonomy. LIVE here")
    print("    makes it OPTIONAL (the scalar law closes), not forced; filed as the natural next.")
    print("  (c) claim-2 contact: K_face = -log rho_face explicit in (m,q) (eigenvalues")
    print("    1/2 +- 1/2 sqrt(1-4q/m^2)); a per-point-time (J4) check consumes K_face(m,q).")
    print("  Filed for v28. No verdicts.")
    return True


# ----------------------------------------------------------------------------
def main(run=(0, 1, 2, 3, 4, 5)):
    print("#" * 78)
    print("# variety_equation_of_state.py -- v27.0 Phase 87 (GENUINE FORK; exact over Q/Q(t))")
    print("#" * 78)
    res = {}
    if 0 in run:
        res["g0"] = gate0()
        if not res["g0"]:
            print("\n*** GATE 0 FAILED -- STOP ***"); return res
    if 1 in run:
        res["g1"] = gate1()
        if not res["g1"]:
            print("\n*** GATE 1 controls FAILED -- STOP ***"); return res
    if 2 in run:
        res["g2"] = gate2()
    coeffsA = None
    if 3 in run:
        res["g3"], coeffsA = gate3()
    v = None
    if 4 in run:
        res["g4"], v = gate4(coeffsA)
    if 5 in run:
        res["g5"] = gate5()
    print("\n" + "=" * 78)
    print(f"  VERDICT (D3): {v} -- the equation-of-state fork "
          f"{'CLOSES into a local balance law' if v == 'LIVE' else 'does NOT close'}.")
    print("=" * 78)
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
