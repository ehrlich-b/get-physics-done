#!/usr/bin/env python3
"""clock_connection_indep_check.py -- v30.0 Phase 90, the gpd-verifier's INDEPENDENT path.

A THIRD code path (distinct from clock_connection.py and clock_connection_verify.py), built to
adversarially re-derive the VERDICT = DEAD and to try hard to break it (make it LIVE).  Exact
over Q / Q(t) / Q(eta).  octonion_algebra BANNED.  u = e_7; cut = h_3(C_u), C_u = span{1, e_7}.
Shared certified arena: ring_lemma_verification (RL), variety_moment_doublet (vMD), vMD.V24.

THE LOAD-BEARING RESULT (DEAD): the clock-drift 1-form a_X^(2)(v)=<nabla_v Kcal, D> built from
the v29 clock Kcal=-(9/2)<M,p> tl(C_pM) and the canonical PARALLEL phase reference D is EXACT,
a_X^(2)=dchi with chi=<Kcal,D>=-(9/2)<M,p><M,D_p>, because
   (1) nabla D = 0 (D parallel: d_v D in V_{1/2}, killed by the face projector C_p), AND
   (2) <Kcal, d_v D> = 0 (Peirce orthogonality <V_0,V_{1/2}>=0),
so a(v)-d_v chi = -<Kcal,d_v D> = 0 => oint a = 0 (Stokes) => no matter-forced holonomy => DEAD.
This is verified EXACTLY in the sqrt-free octonion engine along cut families (C4, C8), where
nabla D=0 holds identically (no truncation) -- the cleanest, bug-A-immune statement.

WHAT IS INDEPENDENT vs the two drivers:
  * K_face^(2) re-derived by the 2x2 REDUCED-DENSITY block (rows/cols {1,2}, e_7->i), and
    cross-checked vs the matrix-log clock -2 log(2rho) (a DIFFERENT clock; differs by a V_0 term
    only => DEAD robust to the clock definition).                                           (C1)
  * chi re-confirmed in a 3x3-complex rep with the OPPOSITE orientation e_7 -> -i.           (C2)
  * The DIRECT 2-form da(d_s,d_t) on a generic complex 2-surface, computed honestly.  FINDING
    (the subtle, correct picture): the face/complement bundle has GENUINELY NONZERO Fubini-Study/
    Bott curvature, so in any concrete Gram-Schmidt gauge the RAW da != 0 (e.g. 2201/6930).  BUT
    raw da EQUALS the canonical-transport background <[nabla_s,nabla_t]Kcal,D> identically (this
    is a STRUCTURAL identity for any in-face field), so the background-subtracted F^(2)=0.  The
    decisive, non-vacuous content is therefore the EXACTNESS a=dchi (C4/C8), not the (always-zero)
    subtraction.  An EARLY-TRUNCATION read of "raw da" returns 0 -- that is the O(eta^2) artifact
    (the Bott term enters at O(eta^2) in nabla D); the honest raw da is 2201/6930.    (C3, C6)
  * BUG-A reproduced (complex params leak Derivative(conjugate(s),s)); the sqrt normalization
    also hides such an aux var -- the engine's sqrt-FREE path (C4/C8) is immune.             (C5)
  * verdict() non-hardwired; guard 5 (chi constructive, not v29's no-global-H).              (C7)
  * ANTI-VACUITY (exact engine): break nabla D=0 => the exactness defect a-dchi=-<Kcal,d_v D>
    becomes a NONZERO polynomial in the matter components => a NOT exact => would be LIVE.  So
    DEAD is contingent on the derived canonical parallel transport, not a universal artifact.  (C8)
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                       # noqa: E402
from sympy import (Rational, symbols, cancel, expand, I, Matrix, eye,    # noqa: E402
                   series, sqrt, diff as Dd)

import ring_lemma_verification as RL                                     # noqa: E402
import variety_moment_doublet as vMD                                     # noqa: E402

_t0 = time.time()
PASS = []
inner = vMD.inner
comp = vMD.V24.compress0
E11 = vMD.E11
I3 = vMD.I3
EPS = symbols("epsilon")          # the matter scale eps (the eps^2 verdict order)
ETA = symbols("eta")              # joint (s,t) surface-order bookkeeping


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


def zoct():
    return [sp.Integer(0)] * 8


def cu(re, e7):
    z = zoct(); z[0], z[7] = re, e7; return z


def Kcal_engine(M, p):
    fid = vMD.el_sub(RL.h3o_identity(), p)
    Cp = comp(p, M)
    tl = vMD.el_sub(Cp, vMD.V24.el_scal(RL.Tr(Cp) * Rational(1, 2), fid))
    return vMD.V24.el_scal(-Rational(9, 2) * inner(M, p), tl)


def D_engine_E11():
    """The canonical C_u-phase reference at E_11: e_7 in the x1=(2,1) entry (coord 10)."""
    return RL.h3o_from_coords(0, 0, 0, cu(0, 1), zoct(), zoct())


def Mcut(pre="w"):
    s = symbols(f"{pre}0:8", real=True)
    return RL.h3o_from_coords(s[0], s[1], -s[0] - s[1],
                              cu(s[2], s[3]), cu(s[4], s[5]), cu(s[6], s[7])), s


def verdict(a_is_exact):
    """NON-HARDWIRED: DEAD iff the clock-drift 1-form is EXACT (a=dchi => oint a=0 => no
    matter-forced curvature); LIVE iff a is non-exact (genuine matter holonomy)."""
    return "DEAD" if a_is_exact else "LIVE"


# ============================================================================
# C1.  K_face^(2) via the 2x2 REDUCED-DENSITY-MATRIX block (independent route)
# ============================================================================
def C1_reduced_density_K2():
    print("=" * 74)
    print("C1 : K_face^(2) via the 2x2 reduced-density block (rows/cols {1,2}, e_7->i)")
    print("=" * 74)
    M, _ = Mcut()
    X = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
    CpX = comp(E11, X)
    mtr = RL.Tr(CpX)

    def ecx(O):                       # octonion in span{1,e_7} -> complex (e_7 -> i)
        return O[0] + I * O[7]

    rho = Matrix(2, 2, lambda a, b: cancel(
        sp.series(ecx(CpX[1 + a][1 + b]) / mtr, EPS, 0, 3).removeO()))
    drho2 = Matrix(2, 2, lambda a, b: cancel(rho[a, b].coeff(EPS, 2)))
    K2 = -2 * drho2
    K2_tl = K2 - (K2.trace() / 2) * eye(2)
    N = comp(E11, M)
    Nb = Matrix(2, 2, lambda a, b: cancel(ecx(N[1 + a][1 + b])))
    Nb_tl = Nb - (Nb.trace() / 2) * eye(2)
    pred = cancel(-Rational(9, 2) * inner(M, E11)) * Nb_tl
    match = (K2_tl - pred).applyfunc(lambda e: cancel(expand(e))).is_zero_matrix
    rep("C1 reduced-density K^(2) traceless == -(9/2)<M,E_11> traceless(C_pM) (symbolic cut M)",
        bool(match))

    A = (2 * rho - eye(2)).applyfunc(lambda e: sp.expand(e))      # = O(eps)
    logm = (A - (A * A) / 2).applyfunc(lambda e: sp.expand(e))    # log(2rho) to eps^2
    Klog2 = Matrix(2, 2, lambda a, b: cancel((-2 * logm)[a, b].coeff(EPS, 2)))
    Klog2_tl = Klog2 - (Klog2.trace() / 2) * eye(2)
    diff = (Klog2_tl - K2_tl).applyfunc(lambda e: cancel(expand(e)))
    nonzero = not diff.is_zero_matrix
    herm = (diff - diff.H).applyfunc(lambda e: cancel(expand(e))).is_zero_matrix
    rep("C1 clock-def ambiguity confined to V_0: (matrix-log clock - cast clock) is a nonzero "
        f"Hermitian FACE matrix [nonzero={nonzero}, herm={herm}] => DEAD robust to clock def",
        nonzero and herm)
    print("      (the v29 'cast' clock -2*d^2_eps rho matches; the log clock -2 log(2rho) adds a "
          "V_0 face term -- both in V_0, both give a=dchi)")
    return True


# ============================================================================
# C2.  chi and the verdict in the OPPOSITE complex orientation  e_7 -> -i
# ============================================================================
def C2_opposite_orientation():
    print("=" * 74)
    print("C2 : chi & verdict in the OPPOSITE orientation e_7 -> -i (conjugate Fano sign)")
    print("=" * 74)
    M = RL.h3o_from_coords(Rational(2), Rational(-1), Rational(-1),
                           cu(Rational(1, 2), Rational(1, 3)),
                           cu(Rational(1, 4), Rational(-1, 5)),
                           cu(Rational(1, 6), Rational(1, 7)))
    D = D_engine_E11()
    chi_eng = cancel(inner(Kcal_engine(M, E11), D))
    chi_formula = cancel(-Rational(9, 2) * inner(M, E11) * inner(M, D))

    def ecx_m(O):                     # OPPOSITE orientation e_7 -> -i
        return O[0] - I * O[7]

    Mx = Matrix(3, 3, lambda a, b: ecx_m(M[a][b]))
    Dx = Matrix(3, 3, lambda a, b: ecx_m(D[a][b]))
    P11 = Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]])
    Q = eye(3) - P11
    a = (Mx * P11).trace()
    CM = Q * Mx * Q
    Kx = cancel(-Rational(9, 2) * a) * (CM - (CM.trace() / 2) * Q)
    chi_opp = cancel(expand((Kx * Dx).trace()))
    rep(f"C2 chi independent of orientation: engine={chi_eng}, formula={chi_formula}, "
        f"e_7->-i rep={chi_opp} (all equal)",
        cancel(chi_eng - chi_formula) == 0 and cancel(chi_eng - chi_opp) == 0)
    print(f"      chi(E_11) = -(9/2)<M,p><M,D> = -(9/2)(2)(2/3) = -6 "
          f"[<M,p>={inner(M, E11)}, <M,D>={inner(M, D)}]")
    return True


# ============================================================================
# C3.  DIRECT 2-form da on a generic complex surface -- raw da == background (=> F_sub=0)
# ============================================================================
def _surface(build_order=5):
    """A generic complex holomorphic chart (frame seeds DIFFERENT from the executor's) + the
    Gram-Schmidt phase reference, eta-series to total degree `build_order`.  REAL surface params."""
    s, t = symbols("s t", real=True)
    g1 = Rational(2, 3) - I * Rational(1, 5); g2 = Rational(1, 4) + I * Rational(3, 7)
    h1 = Rational(1, 6) + I * Rational(2, 9); h2 = -Rational(3, 5) - I * Rational(1, 11)
    E1 = Matrix([0, 1, 0]); E2 = Matrix([0, 0, 1])

    def trunc(Mm, n=build_order):
        return Mm.applyfunc(lambda e: series(sp.expand(e), ETA, 0, n).removeO())

    v = Matrix([1, ETA * (s * g1 + t * h1), ETA * (s * g2 + t * h2)])
    P = trunc((v * v.H) * (1 / cancel((v.H * v)[0])))
    Q = eye(3) - P
    w2 = Q * E1; n2 = cancel((w2.H * w2)[0])
    u2 = trunc(w2 * series(1 / sqrt(n2), ETA, 0, build_order).removeO())
    w3 = Q * E2 - u2 * ((u2.H * (Q * E2))[0]); n3 = cancel((w3.H * w3)[0])
    u3 = trunc(w3 * series(1 / sqrt(n3), ETA, 0, build_order).removeO())
    D = trunc(I * (u3 * u2.H - u2 * u3.H))
    return s, t, P, Q, D, trunc


def C3_direct_curvature():
    print("=" * 74)
    print("C3 : DIRECT 2-form da on a generic complex surface -- raw da == Bott background")
    print("=" * 74)
    s, t, P, Q, D, trunc = _surface(build_order=5)
    Ms = {
        "dense": Matrix([[Rational(2), Rational(1, 2) + I * Rational(1, 3),
                          Rational(1, 4) - I * Rational(1, 5)],
                         [Rational(1, 2) - I * Rational(1, 3), Rational(-1),
                          Rational(1, 6) + I * Rational(1, 7)],
                         [Rational(1, 4) + I * Rational(1, 5),
                          Rational(1, 6) - I * Rational(1, 7), Rational(-1)]]),
        "asym": Matrix([[Rational(5), I * Rational(2), Rational(-3)],
                        [-I * Rational(2), Rational(-2), I],
                        [Rational(-3), -I, Rational(-3)]]),
    }

    def a_dir(K, var):
        dK = K.applyfunc(lambda e: Dd(e, var))
        return series(sp.expand((Q * dK * Q * D).trace()), ETA, 0, 4).removeO()

    def nab(K, var):
        return trunc(Q * (K.applyfunc(lambda e: Dd(e, var))) * Q)

    all_sub_zero = True
    for name, Mx in Ms.items():
        a = (Mx * P).trace(); CM = Q * Mx * Q
        K = trunc((-Rational(9, 2) * a) * (CM - (CM.trace() / 2) * Q))
        da = cancel((Dd(a_dir(K, t), s) - Dd(a_dir(K, s), t)).subs({s: 0, t: 0, ETA: 1}))
        bg = cancel(series(sp.expand(((nab(nab(K, t), s) - nab(nab(K, s), t)) * D).trace()),
                           ETA, 0, 4).removeO().subs({s: 0, t: 0, ETA: 1}))
        F_sub = cancel(da - bg)
        print(f"      M={name:5s}: raw da = {da},  Bott background = {bg},  F=da-bg = {F_sub}")
        all_sub_zero = all_sub_zero and (F_sub == 0)
    rep("C3 raw da (nonzero FS/Bott holonomy, trap #13) == canonical-transport background for "
        "both M => background-subtracted F^(2) = 0 (the subtraction is a structural identity for "
        "in-face fields; the load-bearing non-vacuous result is the EXACTNESS a=dchi, C4/C8)",
        all_sub_zero)
    print("      NOTE: an O(eta^2) read of raw da returns 0 (the Bott term enters nabla D at "
          "O(eta^2)); the honest raw da is 2201/6930 and equals the background.")
    return all_sub_zero


# ============================================================================
# C4.  THE LOAD-BEARING RESULT -- nabla D=0 (sqrt-free) + a=dchi EXACT everywhere => oint a=0
# ============================================================================
def C4_exact_everywhere():
    print("=" * 74)
    print("C4 : LOAD-BEARING -- canonical PARALLEL D (sqrt-free engine): nabla D=0 & a=dchi EXACT")
    print("=" * 74)
    import clock_connection_verify as CV
    T = vMD.T
    M, _ = Mcut()
    par_all = True; exact_all = True
    for (j, k) in [(1, 7), (1, 0), (2, 7), (2, 0)]:
        Dfam, _ = CV.D_along(j, k)             # canonical PARALLEL phase ref (sqrt-free engine)
        pfam = vMD.V24.family(T, j, k)
        dD = [[[sp.diff(Dfam[i][a][b], T) for b in range(8)] for a in range(3)] for i in range(3)]
        nabD = comp(pfam, dD)
        par = all(cancel(nabD[i][a][b]) == 0 for i in range(3) for a in range(3) for b in range(8))
        Kc = Kcal_engine(M, pfam)
        chi = inner(Kc, Dfam)
        dK = [[[sp.diff(Kc[i][a][b], T) for b in range(8)] for a in range(3)] for i in range(3)]
        a_v = inner(comp(pfam, dK), Dfam)
        resid = cancel(expand(a_v - sp.diff(chi, T)))
        par_all = par_all and par
        exact_all = exact_all and (resid == 0)
    rep(f"C4 along ALL 4 cut families (symbolic in t): nabla D=0 [{par_all}] AND a(d_t)-d_t chi==0 "
        f"identically [{exact_all}] => a=dchi EXACT => oint a=0 (Stokes) => matter forces NO "
        "curvature => DEAD (the decisive, bug-A-immune, no-truncation result)",
        par_all and exact_all)
    return par_all and exact_all


# ============================================================================
# C5.  BUG-A reproduction -- complex (undeclared) params leak conjugate-derivative terms
# ============================================================================
def C5_bugA():
    print("=" * 74)
    print("C5 : BUG-A -- undeclared (complex) surface params leak antiholomorphic conj-derivs")
    print("=" * 74)
    sc = symbols("s")                 # NOT real
    sr = symbols("s", real=True)      # real
    vc = Matrix([1, sc, 0]); Pc = (vc * vc.H) / cancel((vc.H * vc)[0])
    vr = Matrix([1, sr, 0]); Pr = (vr * vr.H) / cancel((vr.H * vr)[0])
    dPc = Pc.applyfunc(lambda e: Dd(e, sc))
    dPr = Pr.applyfunc(lambda e: Dd(e, sr))
    leak = any(("Derivative" in str(dPc[i, j]) and "conjugate" in str(dPc[i, j]))
               for i in range(3) for j in range(3))
    clean = not any("Derivative" in str(dPr[i, j]) for i in range(3) for j in range(3))
    rep("C5 complex-param dP/ds carries Derivative(conjugate(s),s) (LEAK); real-param dP/ds is "
        f"clean/rational [leak={leak}, real_clean={clean}] => REAL declaration is load-bearing",
        leak and clean)
    print("      the executor declares s,t real (clock_connection.py:436); the spurious-LIVE path "
          "is closed.  (The sqrt-normalization ALSO hides an aux var -- the sqrt-FREE engine path "
          "used in C4/C8 is immune by construction; this is why C4/C8 are the decisive checks.)")
    return True


# ============================================================================
# C6.  BUG-B resolution -- nested-nabla Bott == raw da (both the FS background); subtract => 0
# ============================================================================
def C6_bugB():
    print("=" * 74)
    print("C6 : BUG-B -- nested <[nabla_s,nabla_t]Kcal,D> == raw da (both the FS/Bott background)")
    print("=" * 74)
    s, t, P, Q, D, trunc = _surface(build_order=5)
    Mx = Matrix([[Rational(2), Rational(1, 2) + I * Rational(1, 3),
                  Rational(1, 4) - I * Rational(1, 5)],
                 [Rational(1, 2) - I * Rational(1, 3), Rational(-1),
                  Rational(1, 6) + I * Rational(1, 7)],
                 [Rational(1, 4) + I * Rational(1, 5),
                  Rational(1, 6) - I * Rational(1, 7), Rational(-1)]])
    a = (Mx * P).trace(); CM = Q * Mx * Q
    K = trunc((-Rational(9, 2) * a) * (CM - (CM.trace() / 2) * Q))

    def nab(Y, var):
        return trunc(Q * (Y.applyfunc(lambda e: Dd(e, var))) * Q)

    bott = cancel(series(sp.expand(((nab(nab(K, t), s) - nab(nab(K, s), t)) * D).trace()),
                         ETA, 0, 4).removeO().subs({s: 0, t: 0, ETA: 1}))

    def a_dir(var):
        dK = K.applyfunc(lambda e: Dd(e, var))
        return series(sp.expand((Q * dK * Q * D).trace()), ETA, 0, 4).removeO()
    da = cancel((Dd(a_dir(t), s) - Dd(a_dir(s), t)).subs({s: 0, t: 0, ETA: 1}))
    rep(f"C6 nested Bott <[nabla_s,nabla_t]Kcal,D> = {bott} == raw da = {da} (EQUAL); both ARE the "
        "bundle's intrinsic Fubini-Study holonomy (trap #13).  The 'which is the right F^(2)?' "
        "worry: they COINCIDE here, and the verdict object subtracts this background to 0 (DEAD); "
        "the genuinely contentful statement is exactness a=dchi (C4)",
        bott != 0 and da != 0 and cancel(bott - da) == 0)
    return True


# ============================================================================
# C7.  verdict() non-hardwired + guard 5 (DEAD not importing v29 no-global-H)
# ============================================================================
def C7_verdict_and_guard5():
    print("=" * 74)
    print("C7 : verdict() non-hardwired (both branches) + guard 5 (chi constructive, not v29-H)")
    print("=" * 74)
    rep("C7 verdict() non-hardwired: verdict(exact=True)=DEAD, verdict(exact=False)=LIVE",
        verdict(True) == "DEAD" and verdict(False) == "LIVE")
    M, _ = Mcut()
    chi = cancel(inner(Kcal_engine(M, E11), D_engine_E11()))
    chi_formula = cancel(-Rational(9, 2) * inner(M, E11) * inner(M, D_engine_E11()))
    rep("C7 guard 5: chi=<Kcal,D> exhibited constructively (symbolic M) == -(9/2)<M,p><M,D_p>, "
        "with NO appeal to v29's no-global-H => exactness is an independent statement",
        cancel(chi - chi_formula) == 0)
    return True


# ============================================================================
# C8.  ANTI-VACUITY (EXACT engine) -- break nabla D=0 => a NON-exact => would be LIVE
# ============================================================================
def C8_contingency():
    """The decisive non-vacuity test, in the sqrt-free engine (exact, no truncation, bug-A-immune).
    Exactness a=dchi holds because the defect a(v)-d_v chi = -<Kcal, d_v D> = 0, which needs
    d_v D in V_{1/2}, i.e. the DERIVED nabla D=0.  With the canonical PARALLEL D (D_along) the
    defect is EXACTLY 0 (DEAD).  Replace D by a deliberately NON-parallel D' = D + t*C_p(F_face)
    (a face/V_0 bump): the defect becomes a NONZERO polynomial in the matter components w_i => a is
    NOT exact => oint a != 0 => the SAME matter would read LIVE.  Hence DEAD is contingent on the
    canonical parallel transport -- not a universal artifact of the construction."""
    print("=" * 74)
    print("C8 : ANTI-VACUITY (exact engine) -- break nabla D=0 => a NON-exact => would be LIVE")
    print("=" * 74)
    import clock_connection_verify as CV
    T = vMD.T
    M, ms = Mcut()
    Dpar, _ = CV.D_along(1, 7)
    pf = vMD.V24.family(T, 1, 7)
    K = Kcal_engine(M, pf)

    def defect(D):
        chi = inner(K, D)
        dK = [[[sp.diff(K[i][a][b], T) for b in range(8)] for a in range(3)] for i in range(3)]
        a_v = inner(comp(pf, dK), D)
        return cancel(expand(a_v - sp.diff(chi, T)))

    d_par = defect(Dpar)
    # non-parallel reference: add a constant traceless face (V_0) bump, t-scaled, kept in-face
    Fface = RL.h3o_from_coords(0, Rational(1), Rational(-1), zoct(), zoct(), zoct())
    bump = comp(pf, Fface)
    Dbad = [[[Dpar[i][a][b] + T * bump[i][a][b] for b in range(8)] for a in range(3)]
            for i in range(3)]
    d_bad = defect(Dbad)
    bad_nonzero = (d_bad != 0) and any(cancel(d_bad.subs(T, tv)) != 0
                                       for tv in [Rational(1, 3), Rational(1, 2)])
    v_par = verdict(d_par == 0)
    v_bad = verdict(d_bad == 0)
    rep(f"C8 exact engine: parallel-D defect a-dchi = {d_par} (=> {v_par}); broken-D defect is a "
        f"nonzero poly in w_i (=> {v_bad}) => DEAD contingent on the DERIVED nabla D=0 (not vacuous)",
        d_par == 0 and bad_nonzero and v_par == "DEAD" and v_bad == "LIVE")
    print(f"      broken-D defect at t=1/3 (nonzero, matter-dependent): "
          f"{sp.nsimplify(d_bad.subs(T, Rational(1, 3)))}")
    return d_par == 0


# ============================================================================
def main():
    print("#" * 74)
    print("# clock_connection_indep_check.py -- gpd-verifier INDEPENDENT path (exact/Q,Q(t),Q(eta))")
    print("#" * 74)
    C1_reduced_density_K2()
    C2_opposite_orientation()
    C3_direct_curvature()
    a_exact = C4_exact_everywhere()
    C5_bugA()
    C6_bugB()
    C7_verdict_and_guard5()
    C8_contingency()

    v = verdict(a_exact)                          # DEAD iff a=dchi exact (the load-bearing fact)
    print("\n" + "=" * 74)
    print(f"  INDEPENDENT verdict: a_X^(2) = dchi EXACT (nabla D=0 + Peirce orth) => oint a=0 => {v}")
    print(f"  {sum(PASS)}/{len(PASS)} checks PASS  "
          f"({'DEAD CONFIRMED -- clock-drift 1-form is exact; no matter-forced curvature' if all(PASS) and v == 'DEAD' else 'DISCREPANCY -- INVESTIGATE'})")
    print("=" * 74)
    print(f"\n[{time.time() - _t0:6.1f}s]")
    return all(PASS) and v == "DEAD"


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
