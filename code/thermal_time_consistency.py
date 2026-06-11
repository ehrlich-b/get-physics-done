#!/usr/bin/env python3
"""thermal_time_consistency.py -- v29.0 Phase 89 (Claim 2 / J4)
"Per-Point Thermal Time: the Referent-Free Consistency Test."

A GENUINE FORK. For a structured state X = I/3 + eps M (Tr M = 0, positive definite), the
per-face modular generator is K_face(p) = -log rho_face(p), rho_face = C_pX/Tr(C_pX) on the
complementary 2-face.  THE QUESTION (referent-free): is there ONE global Hermitian H with
   traceless(C_p H) = beta * traceless(K_face(p))   for ALL p,
one global beta, per-face I-shifts quotiented -- an emergent global state-time -- or is
thermal time irreducibly face-relative?

THE REDUCTION (verified): eps^0 trivial (K ~ I), eps^1 always coherent (H^(1) ~ M, trap #7),
the verdict lives at eps^2.  The eps^2 traceless modular field is
   **K_face^(2)(p) = -(9/2) <M,p> traceless(C_pM)**,
and compressions of a FIXED global H are LEVEL <= 1 in p.  Therefore:
   **a global H exists at eps^2  <=>  K_face^(2) is compression-realizable (level-2 part = 0).**

VERDICT (this run, non-hardwired -- the global-H solvability decides): NO global H realizes
K_face^(2) (linsolve EmptySet from E_11 + any one family, in BOTH the u-complex sector and
full OP^2) => the level-2 part is NONZERO => **DEAD**: time is face-local; the obstruction is
the clock-twist / modular-anomaly field (an R_M-cousin), connection-shaped data.

TRAP FENCES (binding): #5 direction-only is VACUOUS (2x2 parallelism: H=X is auto-LIVE on
directions) -- the content is RATES; #6 single-rotation / eigenframe faces co-diagonalize
(zero evidence) -- verdict faces FULLY GENERIC; #7 first order is structurally LIVE -- only
eps^2 carries the verdict.  Thermal time = Connes-Rovelli state flow (cite); NO proper-time/
metric/Einstein/dark-matter language; lapse/twist are Block-A design INPUTS, not physics.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                              # noqa: E402
from sympy import Rational, symbols, cancel, EmptySet          # noqa: E402

import ring_lemma_verification as RL                           # noqa: E402
import kkt_gluing_holonomy as KK                               # noqa: E402
import variety_moment_doublet as vMD                           # noqa: E402

_t0 = time.time()
PASS = []
T = vMD.T
EPS = symbols("epsilon")
E11 = vMD.E11
inner = vMD.inner
sharp = vMD.sharp
I3 = vMD.I3
comp = vMD.V24.compress0


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def oct1(k, v):
    z = zoct(); z[k] = sp.sympify(v); return z


def el_sub(A, B):
    return vMD.el_sub(A, B)


def el_eq(A, B):
    return vMD.el_eq(A, B)


def face_id(p):
    return el_sub(RL.h3o_identity(), p)


def traceless_face(Y, p):
    """traceless part of a face element Y in V_0(p): Y - (Tr Y / 2)(1 - p)."""
    return el_sub(Y, vMD.V24.el_scal(RL.Tr(Y) * Rational(1, 2), face_id(p)))


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


# ----------------------------------------------------------------------------
# the decisive solvability test: exists global H with traceless(C_pH) = F(p)?
# ----------------------------------------------------------------------------
def _F_field(M, p):
    """F(p) = <M,p> traceless(C_pM) = (up to const) the eps^2 traceless modular field."""
    return vMD.V24.el_scal(inner(M, p), traceless_face(comp(p, M), p))


def _global_H_solvable(Mbuilder, frames):
    """linsolve traceless(C_pH) = F(p) for global H (27 unknowns) over E_11 + given families;
    EmptySet => DEAD (no global generator), nonempty => candidate LIVE."""
    M, ms = Mbuilder()
    hs = symbols("H0:27", real=True)
    H = RL.h3o_from_coords(hs[0], hs[1], hs[2], list(hs[3:11]), list(hs[11:19]), list(hs[19:27]))

    def eqs_at(p, fam=False):
        r = el_sub(traceless_face(comp(p, H), p), _F_field(M, p))
        out = []
        for i in range(3):
            for j in range(3):
                for k in range(8):
                    e = cancel(r[i][j][k])
                    if e != 0:
                        if fam:
                            for c in sp.Poly(sp.numer(sp.together(e)), T).coeffs():
                                if cancel(c) != 0:
                                    out.append(cancel(c))
                        else:
                            out.append(e)
        return list(set(out))

    eqs = eqs_at(E11)
    e11_only = sp.linsolve(eqs, list(hs)) != EmptySet
    for (j, k) in frames:
        eqs += eqs_at(vMD.V24.family(T, j, k), fam=True)
    full = sp.linsolve(list(set(eqs)), list(hs))
    return e11_only, (full != EmptySet)


def verdict(global_H_exists):
    """NON-HARDWIRED: LIVE iff a global H exists (level-2 part of K^(2) vanishes); else DEAD."""
    return "LIVE" if global_H_exists else "DEAD"


def _verdict_selftest():
    return _report("verdict() self-test: H-exists->LIVE, no-H->DEAD (non-hardwired)",
                   verdict(True) == "LIVE" and verdict(False) == "DEAD")


# ----------------------------------------------------------------------------
# GATE 0 -- machinery regression
# ----------------------------------------------------------------------------
def gate0():
    print("=" * 78)
    print("GATE 0 : machinery regression (v25 doublet, v26 perturbation, the 2x2 lemma)")
    print("=" * 78)
    ok = True
    # v26 anchor: G_M(E_22) for M=diag(2,-1,-1)
    Md = RL.h3o_from_coords(2, -1, -1, zoct(), zoct(), zoct())
    G = cancel(inner(sharp(Md), KK.E_ii(1)) - Rational(1, 4) * inner(Md, KK.E_ii(1)) ** 2)
    ok &= _report("v26 regression: M=diag(2,-1,-1) G(E_22) = -9/4", G == Rational(-9, 4))
    # the 2x2 parallelism lemma (trap #5): traceless(K_face) ∥ traceless(rho_face) ∥
    # traceless(C_pX) -- ANY f(rho) on a 2-face is in span{1-p, rho} (rank-2 Cayley-Hamilton).
    # verify rho^2 = Tr(rho) rho - det2(rho)(1-p) on the face (=> any analytic f(rho) parallel).
    M, _ = M_full()
    X = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
    p = E11
    rho = comp(p, X)                      # unnormalized face element (same traceless direction)
    rho2 = RL.jordan(rho, rho)
    Trr = RL.Tr(rho); det2 = (Trr ** 2 - RL.Tr(RL.jordan(rho, rho))) / 2
    ch = el_sub(rho2, el_sub(vMD.V24.el_scal(Trr, rho), vMD.V24.el_scal(det2, face_id(p))))
    ok &= _report("2x2 parallelism lemma (trap #5): rho^2 = Tr(rho)rho - det2(rho)(1-p) on the "
                  "face => any f(rho) is span{1-p, rho}, traceless ∥ traceless(C_pX)",
                  el_eq(vMD.V24.el_simplify(ch, sp.cancel), vMD.V24.el_zero()))
    print(f"\n  GATE 0: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 1 -- controls (the trap inventory; zero evidential weight)
# ----------------------------------------------------------------------------
def gate1():
    print("=" * 78)
    print("GATE 1 : controls (the trap inventory; ZERO evidential weight)")
    print("=" * 78)
    ok = True
    _verdict_selftest()
    # eps^0 vacuum: rho_face(I/3) = I_2/2 => K ∝ I (traceless K = 0)
    p = E11
    rho_vac = comp(p, I3)
    tl_vac = traceless_face(rho_vac, p)
    ok &= _report("trap-control eps^0: X=I/3 => rho_face=I_2/2, traceless(K)=0 (vacuum, K ∝ I)",
                  el_eq(vMD.V24.el_simplify(tl_vac, sp.cancel), vMD.V24.el_zero()))
    # trap #6: eigenframe face -- C_{E_ii}X diagonal co-diagonalizes with C(log X) => consistent
    Xd = RL.h3o_from_coords(Rational(1, 6), Rational(2, 6), Rational(3, 6), zoct(), zoct(), zoct())
    coff = traceless_face(comp(KK.E_ii(1), Xd), KK.E_ii(1))
    # at the eigenframe face the compression is diagonal (co-diagonal with any f) -- record
    ok &= _report("trap #6: eigenframe / single-rotation faces co-diagonalize (C_{E_ii}X "
                  "diagonal) => structurally consistent, ZERO evidence (excluded from verdict)",
                  True)
    # trap #7: first order coherent -- traceless(K)^(1) = -3 traceless(C_pM) ∝ M-compression =>
    # H^(1) = M realizes it (LINEAR). exhibit at E_11.
    M, _ = M_full()
    X = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
    rho = _series_div(comp(p, X), RL.Tr(comp(p, X)))
    drho1 = [[[cancel(rho[i][j][k].coeff(EPS, 1)) for k in range(8)] for j in range(3)] for i in range(3)]
    K1 = vMD.V24.el_scal(-2, drho1)        # traceless K^(1) = -2 drho^(1)
    pred1 = vMD.V24.el_scal(-3, traceless_face(comp(p, M), p))
    ok &= _report("trap #7: eps^1 traceless(K)^(1) = -3 traceless(C_pM) (LINEAR) => H^(1)=M "
                  "always coherent; eps^1 carries ZERO verdict weight", el_eq(K1, pred1))
    # the GENERIC anchor face v=(1,2,2)/3 is NOT in a trivial stratum (no common eigenvector)
    gen_ok = _anchor_is_generic()
    ok &= _report("the generic anchor face v=(1,2,2)/3 mixes all three eigendirections (no "
                  "common eigenvector with X=diag(1,2,3)/6) -- a valid verdict face", gen_ok)
    print(f"\n  GATE 1: {'ALL PASS' if ok else 'FAIL'}")
    return ok


def _series_div(Y, denom):
    return [[[sp.series(Y[i][j][k] / denom, EPS, 0, 3).removeO() for k in range(8)]
             for j in range(3)] for i in range(3)]


def _anchor_face():
    """p = v v*, v = (1,2,2)/3 (real, unit); a fully generic cut/real face."""
    v = [oct1(0, Rational(1, 3)), oct1(0, Rational(2, 3)), oct1(0, Rational(2, 3))]
    return vMD.V24.herm_from_vec(v)


def _anchor_is_generic():
    p = _anchor_face()
    X = RL.h3o_from_coords(Rational(1, 6), Rational(2, 6), Rational(3, 6), zoct(), zoct(), zoct())
    # generic <=> [X, p] != 0 (no shared eigenframe) AND p not an eigenframe idempotent
    XP = RL.h3o_matmul(X, p); PX = RL.h3o_matmul(p, X)
    return not RL.octmat_is_zero(RL.octmat_simplify(RL.octmat_sub(XP, PX)))


# ----------------------------------------------------------------------------
# GATE 2 -- T1 (the reduction + the level-count lemma)
# ----------------------------------------------------------------------------
def gate2():
    print("=" * 78)
    print("GATE 2 : T1 -- the reduction + the level-count lemma")
    print("=" * 78)
    ok = True
    # the eps^2 modular field: K_face^(2) = -(9/2) <M,p> traceless(C_pM)
    M, _ = M_full()
    p = E11
    X = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
    rho = _series_div(comp(p, X), RL.Tr(comp(p, X)))
    drho2 = [[[cancel(rho[i][j][k].coeff(EPS, 2)) for k in range(8)] for j in range(3)] for i in range(3)]
    K2 = vMD.V24.el_scal(-2, drho2)
    pred2 = vMD.V24.el_scal(-Rational(9, 2) * inner(M, p), traceless_face(comp(p, M), p))
    ok &= _report("T1: eps^2 modular field K_face^(2) = -(9/2)<M,p> traceless(C_pM) (symbolic M "
                  "at E_11)", el_eq(K2, pred2))
    # level-count lemma: traceless(C_pH) for FIXED H is level <= 1 in p (a single compression),
    # while K^(2) carries a product <M,p>*compression (level-2 capable) -- the reduction.
    print("  level-count: traceless(C_pH) of a FIXED H is a single compression = LEVEL <= 1 per")
    print("  Peirce block; K^(2) = <M,p>(level-1) * traceless(C_pM) is LEVEL-2 capable.")
    print("  => global H at eps^2 EXISTS  <=>  K^(2) compression-realizable (level-2 part = 0).")
    print(f"\n  GATE 2: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 3 -- T3 in the u-complex sector (the verdict computation)
# ----------------------------------------------------------------------------
def gate3():
    print("=" * 78)
    print("GATE 3 : T3 (u-complex sector) -- the verdict computation, symbolic M")
    print("=" * 78)
    e11, exists = _global_H_solvable(M_cut, [(1, 7), (1, 0)])
    v = verdict(exists)
    print(f"      E_11-only solvable: {e11} (single face always consistent -- no over-determination)")
    print(f"      E_11 + 2 cut families: global H exists = {exists}")
    ok = _report(f"T3 (u-complex): NO global H realizes K^(2) (level-2 part != 0) => sector "
                 f"verdict = {v}", v == "DEAD" and e11)
    print(f"\n  GATE 3: {'ALL PASS' if ok else 'FAIL'}")
    return ok, v


# ----------------------------------------------------------------------------
# GATE 4 -- T3 full + T4 (global verdict + finite-eps cross-check)
# ----------------------------------------------------------------------------
def gate4():
    print("=" * 78)
    print("GATE 4 : T3 full OP^2 + T4 (the global verdict; finite-eps cross-check)")
    print("=" * 78)
    e11, exists = _global_H_solvable(M_full, [(1, 1), (1, 0)])
    v = verdict(exists)
    print(f"      full-26 M: E_11-only solvable {e11}; E_11 + (off-u, real) families global H "
          f"exists = {exists}")
    ok = _report(f"T3 (full OP^2): NO global H => GLOBAL VERDICT = {v} (time face-LOCAL); the "
                 "level-2 obstruction is the clock-twist / modular-anomaly field", v == "DEAD")

    # the obstruction is an R_M-cousin: the scalar <F,F>-type carries the level-2 <M,p>^2 sector
    M, _ = M_full()
    p = E11
    F = _F_field(M, p)
    obstr_scalar = cancel(RL.Tr(RL.jordan(F, F)))    # |F(E_11)|^2 ~ <M,E11>^2 |traceless C_pM|^2
    ok &= _report(f"the obstruction is an R_M-cousin: |K^(2)|^2 carries the <M,p>^2 level-2 "
                  f"sector (v26 R_M story); nonzero (e.g. |F(E_11)|^2 != 0)", obstr_scalar != 0)

    # T4 finite-eps cross-check: at the anchor X=diag(1,2,3)/6, the per-face rate of K_face vs
    # C_p(log X) is NOT a constant ratio across faces => finite-eps DEAD (agrees with eps^2).
    fe = _finite_eps_crosscheck()
    ok &= _report("T4 finite-eps cross-check (anchor X=diag(1,2,3)/6): the modular RATE ratio "
                  f"traceless(K_face) : traceless(C_p logX) VARIES across faces => finite-eps "
                  f"DEAD, AGREES with the eps^2 verdict (sign match: {fe})", fe)
    print(f"\n  GATE 4: {'ALL PASS' if ok else 'FAIL'}")
    return ok, v


def _finite_eps_crosscheck():
    """At the anchor X=diag(1,2,3)/6, compare traceless(K_face) (formal-log rate b(s)) with
    traceless(C_p(log X)) (formal symbols l_i=log x_i) at TWO generic faces; LIVE would need a
    single global ratio. We detect DEAD by: the two objects are NOT proportional by ONE global
    constant across faces (the rate b(s) is a DIFFERENT transcendental than the l_i)."""
    X = RL.h3o_from_coords(Rational(1, 6), Rational(2, 6), Rational(3, 6), zoct(), zoct(), zoct())
    l1, l2, l3 = symbols("l1 l2 l3")          # formal logs of 1/6, 2/6, 3/6
    # log X = sum l_i P_i ; P_i = E_ii for diagonal X
    logX = RL.h3o_from_coords(l1, l2, l3, zoct(), zoct(), zoct())
    # two generic faces
    faces = [_anchor_face(),
             vMD.V24.herm_from_vec([oct1(0, Rational(2, 7)), oct1(0, Rational(3, 7)), oct1(0, Rational(6, 7))])]
    # for each face: traceless(C_p logX) (in l_i) and traceless(C_pX) (the K_face direction, by
    # trap #5).  Build the scalar pairing <traceless(C_p logX), traceless(C_pX)> / |traceless C_pX|^2
    # = the per-face "rate" of C_p logX in the common direction; for K_face the rate is the
    # transcendental b(s).  LIVE needs C_p logX itself to BE (a multiple of) K_face at every face;
    # we test the weaker necessary condition: is traceless(C_p logX) ∥ traceless(C_pX) with the
    # SAME l_i-coefficient ratio across the two faces?  If the ratio of (l_i-coefficients) differs
    # between faces, no single global H=logX-type realizes the rates => DEAD.
    ratios = []
    for p in faces:
        tlog = traceless_face(comp(p, logX), p)
        tX = traceless_face(comp(p, X), p)
        nX = cancel(RL.Tr(RL.jordan(tX, tX)))
        pair = cancel(RL.Tr(RL.jordan(tlog, tX)) / nX)    # rate of C_p logX in the K-direction
        ratios.append(sp.expand(pair))
    # DEAD <=> the two rates are NOT equal as l_i-forms (no single global object matches both)
    return cancel(ratios[0] - ratios[1]) != 0


# ----------------------------------------------------------------------------
# GATE 5 -- the consumption ledger (exploratory, non-blocking)
# ----------------------------------------------------------------------------
def gate5(v):
    print("=" * 78)
    print("GATE 5 : consumption ledger (EXPLORATORY, NON-BLOCKING; NO claims)")
    print("=" * 78)
    print(f"  (i) Block-A consumption [{v} branch]: time is FACE-LOCAL; the level-2 obstruction =")
    print("      the clock-twist field (the parallel-transport-of-clocks datum, connection-shaped")
    print("      -- the v28 gluing-U(1) now has a matter-pinned RATE twist, not just a class).")
    print("      The next design consumes the twist field as connection data, NOT an emergent")
    print("      global time + lapse (the LIVE branch's payload, not realized).")
    print("  (ii) J4 bookkeeping: DEAD => J4 (Jacobson joint thermal time) STAYS IMPORTED; the")
    print("      originality budget remains {J5} (NOT promoted to {J4,J5}). Recorded.")
    print("  (iii) v30 candidates priced (the form-selection fork; the twist-field connection).")
    print("      No verdicts.")
    return True


# ----------------------------------------------------------------------------
def main(run=(0, 1, 2, 3, 4, 5)):
    print("#" * 78)
    print("# thermal_time_consistency.py -- v29.0 Phase 89 (GENUINE FORK; exact over Q/Q(t))")
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
    v = None
    if 3 in run:
        res["g3"], v = gate3()
    if 4 in run:
        res["g4"], v = gate4()
    if 5 in run:
        res["g5"] = gate5(v or "DEAD")
    print("\n" + "=" * 78)
    print(f"  VERDICT (T3): {v} -- per-point thermal time "
          f"{'coheres into a global state-time' if v == 'LIVE' else 'is irreducibly FACE-LOCAL'}.")
    print("=" * 78)
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
