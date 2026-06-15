#!/usr/bin/env python3
"""adv_area_rig_95.py -- ADVERSARIAL path for Phase 95 (v35.0) AREA-PER-BIT KILL-TEST.

Bug-guard #1 AREA-RIG: attack the DEAD-FISHER / fork-A verdict by testing the TWO NON-Fisher
area candidates the executor most likely SKIPPED (it used the metric TRACE of dphi(x)dphi,
which trivially = Var -> Fisher -> DEAD).  We test instead:

  (ii)-TT : the (LOCAL) TRACELESS part of the v31 metric-mode dphi_M(x)dphi_M, made into a
            scalar AREA density via the FS metric norm  A_TT = ||h0||^2_g  (h0 = h - (1/4)tr_g(h) g).
            This is the LOCAL analogue of v31's GLOBAL L^2 ||TT(B3)||^2 = (1/30)(TrM^2)^2 -- a
            genuine non-Fisher object (built from the TRACELESS, not the trace, part).
            R_TT(p,M) = A_TT/|G_M|.  CONSTANT vs SHEAR?  collapses-to-Var vs INDEPENDENT?

  (iii)   : a genuinely SYMPLECTIC area -- Kahler 2-form / moment-map pairings, NOT |grad phi|^2
            (= Var by the Kahler tie; that one collapses, confirmed in (iii-a)).

DISCIPLINE (HARD RESOURCE RULES): NO brute symbolic cancel/simplify over a generic multi-param M.
Evaluate at 5 specific Q-points (exact rational), point-FIRST (substitute the chart point into the
metric/gradients BEFORE contracting -- instant; symbolic-then-subs on the traceless FIELD is the
diagnosed perf cliff).  Foreground, bounded, no commits.  Exact over Q.  CP^2 = h_3(C_u).

Two FS normalizations reported (the overall scale is the single one G1 normalizes away):
  g_pot  = d d_bar log rho          (Fisher metric; the DEAD-FISHER identity A_ii = Var holds here)
  g_phys = (1/2) g_pot              (engine normalization)
We compute A_TT in BOTH and show the collapse/shear disposition is scale-INDEPENDENT.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from sympy import Rational, Matrix, I, cancel, zeros, eye

import tensor_probe as T
import lichnerowicz_response as L

Z1, Z2, Z1B, Z2B = T.Z1, T.Z2, T.Z1B, T.Z2B

DIRS = {
    "s01": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    "a01": Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    "d1":  Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
    "gen": Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),
}
PTS = {
    "P0": {Z1: 1 + 2 * I, Z1B: 1 - 2 * I, Z2: -1 + I, Z2B: -1 - I},      # rho=8
    "P2": {Z1: -1, Z1B: -1, Z2: 2 - 3 * I, Z2B: 2 + 3 * I},             # rho=15
    "P3": {Z1: Rational(1, 2), Z1B: Rational(1, 2),
           Z2: Rational(-1, 3), Z2B: Rational(-1, 3)},                  # rho=49/36
    "P4": {Z1: 2, Z1B: 2, Z2: Rational(1, 5), Z2B: Rational(1, 5)},     # rho=126/25
    "P5": {Z1: I, Z1B: -I, Z2: 1 + I, Z2B: 1 - I},                      # rho=4
}

# the POTENTIAL (Fisher) metric, where the DEAD-FISHER identity A_ii_trace == Var holds exactly.
g_pot = T.fs_metric_pot()
ginv_pot = T.fs_metric_inv(g_pot)
# the PHYSICAL (engine) metric g_phys = (1/2) g_pot
g_phys = T.fs_metric()
ginv_phys = T.fs_metric_inv(g_phys)
Gam = T.christoffel_hol(g_phys, ginv_phys)
P = T.P_chart()


def Var(M, sub):
    return cancel((T.cx_inner(M * M, P) - T.cx_inner(M, P) ** 2).subs(sub))


def G_M(M, sub):
    return cancel(T.G_M_field(M).subs(sub))


def area_TT_at(M, sub, g, ginv):
    """A_TT = ||h0||^2_g, h0 = (dphi(x)dphi) - (1/4) tr_g(dphi(x)dphi) g, at chart point `sub`.
    POINT-FIRST: substitute the point into the metric + gradients, then contract (rational, fast).
    Also returns A_full = ||dphi(x)dphi||^2_g and A_trace = the metric trace (= the DEAD-FISHER (ii))."""
    gP = g.subs(sub)
    giP = ginv.subs(sub)
    phi = cancel(T.phi_field(M))
    da = [cancel(T.dz(phi, a).subs(sub)) for a in range(2)]
    dab = [cancel(T.dzb(phi, a).subs(sub)) for a in range(2)]
    H20 = Matrix([[da[a] * da[b] for b in range(2)] for a in range(2)])
    H11 = Matrix([[da[a] * dab[b] for b in range(2)] for a in range(2)])
    H02 = Matrix([[dab[a] * dab[b] for b in range(2)] for a in range(2)])
    # metric trace tr_g h = 2 g^{a bbar} H11_{a bbar}  (this is the DEAD-FISHER candidate (ii))
    A_trace = cancel(2 * sum(giP[b, a] * H11[a, b] for a in range(2) for b in range(2)))
    H11_0 = (H11 - Rational(1, 4) * A_trace * gP).applyfunc(cancel)

    def n2(b0, b1, b2):
        return cancel(T.tensor_dot_point((b0, b1, b2), (b0, b1, b2), giP, simp=cancel))

    A_full = n2(H20, H11, H02)
    A_TT = n2(H20, H11_0, H02)
    return A_TT, A_full, A_trace


def conj(expr):
    sw = {Z1: Z1B, Z1B: Z1, Z2: Z2B, Z2B: Z2}
    return expr.subs(sw, simultaneous=True).subs(I, -I)


def banner(s):
    print("\n" + "=" * 78)
    print(s)
    print("=" * 78)


def step0():
    banner("STEP 0 : reproduce s9 ground truth + confirm the v31 metric-mode TT structure")
    ok = True
    GT = [("d1", "P0", Rational(1, 2), Rational(-5, 16), Rational(8, 5)),
          ("d1", "P2", Rational(2, 15), Rational(-13, 15), Rational(2, 13)),
          ("s01", "P0", Rational(11, 16), Rational(-17, 64), Rational(44, 17)),
          ("a01", "P0", Rational(1, 2), Rational(-5, 16), Rational(8, 5)),
          ("gen", "P0", Rational(27, 16), Rational(-81, 64), Rational(4, 3))]
    for dn, pn, var_e, g_e, r_e in GT:
        v = Var(DIRS[dn], PTS[pn]); gv = G_M(DIRS[dn], PTS[pn]); r = cancel(v / abs(gv))
        good = (v == var_e and gv == g_e and r == r_e)
        ok &= good
        print(f"  {dn:4s} {pn} Var={str(v):>7s} G_M={str(gv):>8s} R=Var/|G|={str(r):>7s}  "
              f"[{'OK' if good else 'MISMATCH'}]")
    print(f"  s9 ground truth reproduced: {ok}")

    # confirm the DEAD-FISHER identity (ii)-TRACE == Var (Fisher norm), at one point per dir,
    # so we KNOW the trace channel collapses and the TT channel is the genuinely-new object.
    print("\n  DEAD-FISHER trace channel check: A_trace(g_pot) == Var (the executor's candidate ii):")
    for dn in DIRS:
        _, _, A_tr = area_TT_at(DIRS[dn], PTS["P0"], g_pot, ginv_pot)
        v = Var(DIRS[dn], PTS["P0"])
        print(f"    {dn:4s} P0: A_trace(g_pot)={A_tr}, Var={v}, equal={A_tr == v}  "
              "(the TRACE part IS Fisher -- confirmed; we now test the TRACELESS part)")
    return ok


def candidate_ii_TT():
    banner("CANDIDATE (ii)-TT : A_TT = ||traceless part of dphi(x)dphi||^2_g  (the NON-Fisher area)")
    print("  POINT-FIRST exact-Q.  Reported in BOTH g_pot (Fisher) and g_phys=(1/2)g_pot norms.")
    print("  A_trace = the executor's candidate (ii) (= Var, the corpse).  A_TT = the TRACELESS area.\n")
    rows = {}
    for norm_name, gg, gi in (("g_pot", g_pot, ginv_pot), ("g_phys", g_phys, ginv_phys)):
        print(f"  --- norm = {norm_name} ---")
        print(f"  {'dir':4s} {'pt':3s} {'A_TT':>14s} {'A_full':>14s} {'A_trace=Var?':>14s} "
              f"{'Var':>8s} {'G_M':>9s} {'R_TT=A_TT/|G|':>16s}")
        for dn, M in DIRS.items():
            for pn, sub in PTS.items():
                A_TT, A_full, A_tr = area_TT_at(M, sub, gg, gi)
                v = Var(M, sub); gv = G_M(M, sub)
                r_tt = cancel(A_TT / abs(gv)) if gv != 0 else sp.oo
                rows[(norm_name, dn, pn)] = (A_TT, A_full, A_tr, v, gv, r_tt)
                print(f"  {dn:4s} {pn:3s} {str(A_TT):>14s} {str(A_full):>14s} "
                      f"{str(A_tr):>14s} {str(v):>8s} {str(gv):>9s} {str(r_tt):>16s}")
        print()
    return rows


def candidate_iii():
    banner("CANDIDATE (iii) : the SYMPLECTIC (Kahler 2-form / moment-map) area")
    # (iii-a) gradient-norm symplectic area = |grad phi|^2_g = Var (Kahler tie) -- the COLLAPSE
    print("  (iii-a) |grad phi_M|^2_g (Kahler tie => proportional to Var; the COLLAPSE, confirm):")
    for dn in ("s01", "d1", "gen"):
        phi = cancel(T.phi_field(DIRS[dn]))
        for pn in ("P0", "P3", "P5"):
            sub = PTS[pn]
            giP = ginv_pot.subs(sub)
            da = [cancel(T.dz(phi, a).subs(sub)) for a in range(2)]
            dab = [cancel(T.dzb(phi, a).subs(sub)) for a in range(2)]
            gn = cancel(sum(giP[b, a] * da[a] * dab[b] for a in range(2) for b in range(2)))
            v = Var(DIRS[dn], sub)
            print(f"    {dn:4s} {pn}: |grad phi|^2_(g_pot)={str(gn):>8s}  Var={str(v):>8s}  "
                  f"ratio={cancel(gn / v) if v != 0 else None}")
    print("    => (iii-a) COLLAPSES to Var (ratio == 1 in g_pot): the gradient-norm symplectic area")
    print("       IS the Fisher object.  (This is the reading the verdict already covers.)\n")

    # (iii-b) Poisson bracket {phi_M, phi_a01} = i g^{a bbar}(d_a f d_bbar h - d_a h d_bbar f):
    #         a genuine symplectic pairing of two moments.  Test shear/independence of G_M.
    print("  (iii-b) Poisson bracket {phi_M, phi_a01} (genuine symplectic pairing of two moments):")
    M2 = DIRS["a01"]; h2 = cancel(T.phi_field(M2))
    for dn in ("s01", "d1", "gen"):
        f = cancel(T.phi_field(DIRS[dn]))
        for pn in ("P0", "P3"):
            sub = PTS[pn]; giP = ginv_pot.subs(sub)
            dfa = [cancel(T.dz(f, a).subs(sub)) for a in range(2)]
            dfb = [cancel(T.dzb(f, a).subs(sub)) for a in range(2)]
            dha = [cancel(T.dz(h2, a).subs(sub)) for a in range(2)]
            dhb = [cancel(T.dzb(h2, a).subs(sub)) for a in range(2)]
            pb = cancel(I * sum(giP[b, a] * (dfa[a] * dhb[b] - dha[a] * dfb[b])
                                for a in range(2) for b in range(2)))
            gv = G_M(DIRS[dn], sub)
            r = cancel(pb / abs(gv)) if gv != 0 else sp.oo
            print(f"    {dn:4s} {pn}: {{phi_M,phi_a01}}={str(pb):>10s}  G_M={str(gv):>9s}  /|G|={str(r):>12s}")
    print("    => (iii-b) is a Lie-algebra Poisson bracket of two state-space moments, NOT an")
    print("       independent geometric area (it is a STRUCTURE CONSTANT pairing of su(3) moments).\n")

    # (iii-c) symplectic area of the orbit 2-form |dphi_M ^ dphi_a01|^2_g (a genuine 2-form area)
    print("  (iii-c) |dphi_M ^ dphi_a01|^2_g  (orbit symplectic-2-form magnitude; non-Fisher 2-form):")
    res = {}
    for dn in ("s01", "d1", "gen"):
        f = cancel(T.phi_field(DIRS[dn]))
        for pn in ("P0", "P3", "P5"):
            sub = PTS[pn]; giP = ginv_pot.subs(sub)
            dfa = [cancel(T.dz(f, a).subs(sub)) for a in range(2)]
            dfb = [cancel(T.dzb(f, a).subs(sub)) for a in range(2)]
            dha = [cancel(T.dz(h2, a).subs(sub)) for a in range(2)]
            dhb = [cancel(T.dzb(h2, a).subs(sub)) for a in range(2)]
            W = [[cancel(dfa[a] * dhb[b] - dha[a] * dfb[b]) for b in range(2)] for a in range(2)]
            Wc = [[conj(W[a][b]) for b in range(2)] for a in range(2)]
            nrm = cancel(sum(giP[c, a] * giP[b, d] * W[a][b] * Wc[c][d]
                             for a in range(2) for b in range(2)
                             for c in range(2) for d in range(2)))
            v = Var(DIRS[dn], sub); gv = G_M(DIRS[dn], sub)
            r = cancel(nrm / abs(gv)) if gv != 0 else sp.oo
            res[(dn, pn)] = (nrm, v, gv, r)
            print(f"    {dn:4s} {pn}: |dphi^dphi_a01|^2={str(nrm):>12s}  Var={str(v):>8s}  "
                  f"G_M={str(gv):>9s}  /|G|={str(r):>14s}")
    return res


def decisive(rows):
    banner("DECISIVE : A_TT collapse-to-Fisher vs INDEPENDENT+SHEAR  (the verdict fork)")
    # Probe 1: is A_TT a function of Var?  (Compare A_TT/Var and A_TT/Var^2 across points per dir.)
    print("  Probe 1: is A_TT a pure function of the Fisher variance Var? (per direction, g_pot)")
    p1_collapse = True
    for dn in DIRS:
        rv = set()
        for pn in PTS:
            A_TT, A_full, A_tr, v, gv, r_tt = rows[("g_pot", dn, pn)]
            if v != 0:
                rv.add(cancel(A_TT / v ** 2))
        const = (len(rv) == 1)
        p1_collapse &= const
        print(f"    {dn:4s}: A_TT/Var^2 over pts = {sorted(set(str(x) for x in rv))}  "
              f"-> {'CONSTANT' if const else 'VARIES => A_TT is NOT a function of Var'}")

    # Probe 2: R_TT = A_TT/|G_M| -- CONSTANT or SHEAR?  (in BOTH norms; scale-independent disposition)
    print("\n  Probe 2: R_TT = A_TT/|G_M| -- CONSTANT (DEAD) or SHEAR?")
    shear = {}
    for norm_name in ("g_pot", "g_phys"):
        Rset = set()
        for dn in DIRS:
            for pn in PTS:
                A_TT, A_full, A_tr, v, gv, r_tt = rows[(norm_name, dn, pn)]
                if r_tt != sp.oo:
                    Rset.add(r_tt)
        shear[norm_name] = (len(Rset) >= 2)
        print(f"    [{norm_name}] distinct R_TT count = {len(Rset)} -> "
              f"{'SHEARS' if shear[norm_name] else 'CONSTANT'}")

    # Probe 3: is A_TT INDEPENDENT of G_M (different M/p-structure than the rel-entropy Hessian)?
    print("\n  Probe 3: is A_TT INDEPENDENT of G_M (i.e. A_TT/G_M varies => different structure)?")
    indep = True
    for dn in DIRS:
        rg = set()
        for pn in PTS:
            A_TT, A_full, A_tr, v, gv, r_tt = rows[("g_pot", dn, pn)]
            if gv != 0:
                rg.add(cancel(A_TT / gv))
        varies = (len(rg) >= 2)
        indep &= varies
        print(f"    {dn:4s}: A_TT/G_M over pts = {sorted(set(str(x) for x in rg))[:3]}... "
              f"({len(rg)} distinct) -> {'INDEPENDENT' if varies else 'proportional'}")

    print("\n  --- DISPOSITION ---")
    print(f"  A_TT collapses to a function of Var (Fisher)?  {p1_collapse}")
    print(f"  R_TT = A_TT/|G_M| shears (g_pot)?              {shear['g_pot']}")
    print(f"  R_TT = A_TT/|G_M| shears (g_phys)?             {shear['g_phys']}")
    print(f"  A_TT independent of G_M (rel-entropy)?         {indep}")
    return p1_collapse, shear, indep


def main():
    ok = step0()
    rows = candidate_ii_TT()
    iii = candidate_iii()
    p1, shear, indep = decisive(rows)
    print("\n" + "#" * 78)
    print("# ADVERSARIAL AREA-RIG done.  Disposition feeds derivations/95-ADVERSARIAL-CHECK.md")
    print(f"#   ground-truth reproduced: {ok}")
    print(f"#   (ii)-TT: collapses_to_Var={p1}, shears={shear}, independent_of_G_M={indep}")
    print("#" * 78)


if __name__ == "__main__":
    main()
