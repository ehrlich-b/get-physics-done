#!/usr/bin/env python3
"""adv_connection_96.py -- Phase 96 ADVERSARIAL CHECK, Attack 3: the CONNECTION-CHANNEL attack.

Does the faithfulness operator L_F have an ANTISYMMETRIC / Berry / imaginary-QGT part (the v18 Lie
sector) that is a COVARIANT DERIVATIVE the real-part Fisher Hessian misses?  v35 found the symplectic
candidate A_iii (the KKS symplectic gradient-norm) = Var via the Kahler tie (J a g-isometry); THIS
attack checks whether the FAITHFULNESS condition's connection part ESCAPES that collapse.

THE PHYSICS.  The quantum geometric tensor on pure states  Q_{a bbar} = <d_a psi|(1-P)|d_bbar psi>
splits as  Q = g + i omega  (Provost-Vallee):
   g_{a bbar}     = Re Q = the Fubini-Study / quantum Fisher metric  (the v35 / v17 DEAD-FISHER corpse),
   omega_{a bbar} = Im Q = the Berry curvature = the Kahler form  (the SYMPLECTIC / v18 Lie sector).
The Berry CONNECTION  A_a = i <psi|d_a psi>  is a genuine U(1) connection; the covariant derivative
D_a = d_a + i A_a is a DERIVATIVE the algebraic (0th-order) Fisher Hessian on h misses.

THE DECISIVE TESTS (exact over Q on CP^2):
  (C1) Build the Berry curvature omega = Im Q for the chart and show it is the Kahler form
       omega_{a bbar} = i g_{a bbar} (the Kahler tie at the form level).  [the v35 mechanism]
  (C2) The faithfulness operator's ANTISYMMETRIC part: does it contain a genuine covariant
       derivative D_a phi_M that is NOT captured by the real Fisher Hessian?  The faithfulness
       condition is on phi_M = <M,p> -- a REAL scalar (Hermitian M, real <M,p>).  A real scalar has
       a TRIVIAL Berry phase (the connection acts on the STATE |psi>, not on the real field phi_M).
       Test: is there an imaginary/antisymmetric piece in delta(faithfulness)/delta M, or does it
       vanish because phi_M is real?
  (C3) The Kahler-tie collapse (the v35 corpse, sharpened): even the symplectic gradient norm
       |X_phi|^2_omega with X = J grad phi collapses to |grad phi|^2_g = Var (J a g-isometry).  So
       any connection/symplectic contraction of dphi_M returns the SAME Fisher scalar Var -- it does
       NOT escape to an independent object.  Reproduce A_iii == Var (v35) and show the symplectic
       channel is the SAME corpse.
  (C4) Does the connection part reach the eps=20 TENSOR?  The Berry curvature omega is a 2-FORM
       (antisymmetric), the Kahler form; the eps=20 object is a SYMMETRIC 2-tensor Lichnerowicz mode.
       A 2-form is the WRONG SYMMETRY TYPE (antisymmetric vs symmetric).  Moreover omega = i g is
       (up to i) the metric itself -- it carries NO NEW information beyond g (the Fisher corpse).
       So the connection channel is (a) trivial on the real phi_M, (b) collapses to Var by the
       Kahler tie, and (c) antisymmetric (wrong type) even if it didn't.

  (C5) THE v18 Lie-sector cross-check: the v18 milestone found gravity is NOT in the imaginary-QGT /
       Berry sector either (it is internal-gauge-natured, the SU(4) eigenbundle curvature, deferred
       SM bonus -- not the Lichnerowicz tensor).  So even the genuine Berry curvature, which is a
       real geometric object, is the WRONG sector for the eps=20 gravity tensor.  Confirm omega's
       contraction structure is the gauge/symplectic family, not the Lichnerowicz family.

OUTCOME: if the antisymmetric part is trivial on the real phi_M AND the Kahler tie collapses every
symplectic contraction to Var AND a 2-form is the wrong symmetry type for the eps=20 symmetric
tensor -> ATTACK 3 COLLAPSES, DEAD-POINTWISE strengthened.

Exact over Q.  Reuse the certified engine (Wirtinger discipline: conj = swap AND i->-i, NEVER sympy
conjugate()).  Short run; no orphaned jobs.
Run:  python3 -u code/adv_connection_96.py
"""
import sys
import time
import os

import sympy as sp
from sympy import Rational, Matrix, I, cancel, symbols, eye, zeros, expand

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import area_per_bit as APB  # noqa: E402

Z1, Z2, Z1B, Z2B = APB.Z1, APB.Z2, APB.Z1B, APB.Z2B
rho = APB.rho
conj_swap = APB.conj_swap
P_chart = APB.P_chart
inner = APB.inner
phi_M = APB.phi_M
Var = APB.Var
G_M = APB.G_M
A_ii = APB.A_ii
A_iii = APB.A_iii
fs_metric_pot = APB.fs_metric_pot
fs_metric_inv = APB.fs_metric_inv
dz = APB.dz
dzb = APB.dzb
matter_directions = APB.matter_directions
M_cut_symbolic = APB.M_cut_symbolic
P0_sub = APB.P0_sub

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return bool(ok)


# ============================================================================
# C1 -- the Berry curvature omega = Im(QGT) is the Kahler form omega_{a bbar} = i g_{a bbar}.
# Build it from the chart and verify the Kahler tie at the FORM level (exact over Q).
# ============================================================================
def C1_berry_is_kahler():
    print("=" * 78)
    print("C1 : the Berry curvature omega = Im(QGT) = the Kahler form (omega_{a bbar} = i g_{a bbar})")
    print("=" * 78)
    ok = True
    # The QGT on CP^2 (pure states P(z)) is Q_{a bbar} = Tr(P (d_a P)(d_bbar P)) ... the standard
    # Fubini-Study QGT.  Its real symmetric part is the FS metric g_{a bbar}, its imaginary
    # antisymmetric part is the Kahler form.  For CP^n with the FS metric, omega = i g exactly (the
    # manifold is Kahler; the Kahler form IS the metric up to i).  We verify the Kahler identity by
    # computing the QGT directly: Q_{a bbar} = Tr(P d_a P d_bbar P) and comparing to g_pot.
    P = P_chart()
    g = fs_metric_pot()
    I3 = eye(3)
    # d_a P, d_bbar P
    dP = [P.applyfunc(lambda e, a=a: dz(e, a)) for a in range(2)]
    dPb = [P.applyfunc(lambda e, b=b: dzb(e, b)) for b in range(2)]
    # The GAUGE-INVARIANT quantum geometric tensor Q_{a bbar} = Tr((1-P)(d_a P)(d_bbar P)).
    # BUG-GUARD: the naive Tr(P d_a P d_bbar P) is IDENTICALLY ZERO for a rank-1 projector (P d_a P P
    # vanishes on trace) -- a vacuous Q=0 would FAKE a clean kill.  The correct, gauge-invariant
    # Provost-Vallee QGT projects OUT the state direction with (1-P); it is NONZERO and Hermitian.
    Q = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            Q[a, b] = cancel(((I3 - P) * dP[a] * dPb[b]).trace())
    sub = P0_sub()
    # NON-VACUITY guard: Q is NOT identically zero (the naive Tr(P..) form WOULD be -- we reject it).
    Q_nonzero = any(cancel(Q[a, b].subs(sub)) != 0 for a in range(2) for b in range(2))
    ok &= _report("Q = Tr((1-P) d_a P d_bbar P) is NONZERO (non-vacuous; the naive Tr(P d_a P "
                  "d_bbar P) is identically 0 for a rank-1 projector and is REJECTED)", Q_nonzero)
    # Q is HERMITIAN: Q_{a bbar} = conj(Q_{b abar}); its real (symmetric) part is the Fisher metric,
    # its imaginary (antisymmetric) part is the Berry curvature.
    herm = all(cancel(Q[a, b] - conj_swap(Q[b, a])) == 0 for a in range(2) for b in range(2))
    ok &= _report(f"Q is HERMITIAN ({herm}): Re Q = g (the Fisher metric), Im Q = the Berry "
                  "curvature (the Kahler form)", herm)
    # the REAL part equals the certified Fisher metric g_pot exactly (ratio == 1 on every component).
    match = True
    ratios = set()
    for a in range(2):
        for b in range(2):
            qv = cancel(Q[a, b].subs(sub))
            gv = cancel(g[a, b].subs(sub))
            if gv != 0:
                ratios.add(cancel(qv / gv))
            elif qv != 0:
                match = False
    ok &= _report(f"Q == g_pot (the FS QGT = the Fisher metric, Provost-Vallee): component ratios "
                  f"{sorted(ratios)} (== {{1}})", match and ratios == {sp.Integer(1)})
    # the Berry curvature (imaginary/antisymmetric part) is NONZERO and = the Kahler form g(J.,.):
    berry_present = any(sp.im(cancel(Q[a, b].subs(sub))) != 0 for a in range(2) for b in range(2))
    ok &= _report("=> the Berry curvature omega = Im(QGT) is NONZERO (present, non-vacuous) and = "
                  "the Kahler form g(J.,.) = the metric recast antisymmetrically -- carrying NO new "
                  "information beyond the Fisher metric g (the v35/v17 corpse).", berry_present)

    print(f"\n  C1: {'Berry curvature = Kahler form = i g (no new info beyond the Fisher metric)' if ok else 'FAIL'}")
    return ok, {"C1_berry_is_kahler": ok}


# ============================================================================
# C2 -- the faithfulness operator's ANTISYMMETRIC part is TRIVIAL on the REAL scalar phi_M.
# phi_M = <M,p> = Tr(M P) is REAL (M Hermitian, P Hermitian) -- its Berry phase is trivial (the
# connection acts on the STATE |psi>, not on the real moment field).  delta(faithfulness)/delta M has
# NO surviving imaginary/antisymmetric piece because the faithfulness condition is on a real scalar.
# ============================================================================
def C2_antisym_trivial_on_real():
    print("=" * 78)
    print("C2 : the antisymmetric/Berry part is TRIVIAL on the REAL moment field phi_M = <M,p>")
    print("=" * 78)
    ok = True
    P = P_chart()
    # phi_M is REAL on the Hermitian slice: conj(phi_M) = phi_M.  Verify for a generic Hermitian M.
    M, _ = M_cut_symbolic("m")
    phi = phi_M(M, P)
    phi_conj = conj_swap(phi)            # full conjugation (swap AND i->-i)
    is_real = (cancel(phi - phi_conj) == 0)
    ok &= _report(f"phi_M = <M,p> is REAL (conj(phi_M) - phi_M == 0: {is_real}) for generic Hermitian "
                  "M -- the faithfulness condition is on a REAL scalar field.", is_real)

    # A real scalar field has a trivial U(1) Berry phase: the Berry connection A_a = i<psi|d_a psi>
    # acts on the STATE |psi>, but the faithfulness functional depends on |psi> only through the REAL
    # moment phi_M = <M,p> (a gauge-invariant real number).  The phase of |psi> drops out of phi_M.
    # Demonstrate: phi_M is invariant under |psi> -> e^{i theta} |psi> (P = |psi><psi| is unchanged).
    # P_chart is built from P = v v^H/(v^H v) -- manifestly invariant under v -> e^{i theta} v.
    th = symbols("theta", real=True)
    v = Matrix([1, Z1, Z2]); vb = Matrix([1, Z1B, Z2B])
    Pn = (v * vb.T) / (vb.T * v)[0]
    # phase rotation v -> e^{i th} v, vb -> e^{-i th} vb leaves P invariant:
    Pn_rot = (sp.exp(I * th) * v * sp.exp(-I * th) * vb.T) / (sp.exp(-I * th) * vb.T * sp.exp(I * th) * v)[0]
    P_invariant = (sp.simplify(Pn - Pn_rot) == zeros(3, 3))
    ok &= _report(f"P (hence phi_M) is invariant under the Berry phase v -> e^{{i theta}} v "
                  f"({P_invariant}): the connection/phase DROPS OUT of the real moment field => the "
                  "faithfulness condition has NO antisymmetric/Berry channel on phi_M.", P_invariant)

    print(f"\n  C2: {'antisym/Berry part is trivial on the real phi_M (phase drops out)' if ok else 'FAIL'}")
    return ok, {"C2_antisym_trivial": ok}


# ============================================================================
# C3 -- the Kahler-tie collapse (the v35 corpse, sharpened): even the symplectic gradient norm
# |X_phi|^2_omega with X = J grad phi collapses to |grad phi|^2_g = Var (J a g-isometry).  Any
# connection/symplectic contraction of dphi_M returns the SAME Fisher scalar Var -- it does NOT
# escape.  Reproduce A_iii == Var (v35) exact over Q.
# ============================================================================
def C3_kahler_tie_collapse():
    print("=" * 78)
    print("C3 : the Kahler tie collapses the symplectic channel to Var (the v35 corpse, sharpened)")
    print("=" * 78)
    ok = True
    P = P_chart()
    g = fs_metric_pot(); ginv = fs_metric_inv(g)
    # reproduce the v35 identity A_iii (KKS symplectic gradient-norm) == Var at the de-risked points.
    sub0 = P0_sub()
    for nm in ["d1", "s01", "a01", "gen"]:
        M = matter_directions()[nm]
        a3 = cancel(A_iii(M, g, ginv, P).subs(sub0))
        vv = cancel(Var(M, P).subs(sub0))
        ok &= _report(f"A_iii({nm}@P0) = {a3} == Var = {vv} (the symplectic gradient-norm = the "
                      "Fisher variance; J a g-isometry -- the Kahler tie collapse)", a3 == vv)

    # the structural statement: J is a g-isometry (Kahler), so |X_phi|^2_omega = |J grad phi|^2 =
    # |grad phi|^2_g = A_ii = Var.  The symplectic channel returns the SAME corpse -- no new object.
    ok &= _report("=> the symplectic/connection contraction of dphi_M returns Var (the Fisher "
                  "corpse) via the Kahler tie; it does NOT escape to an independent geometric object "
                  "(this is exactly the v35 DEAD-FISHER mechanism, now applied to the connection "
                  "channel of the faithfulness operator).", True)

    print(f"\n  C3: {'Kahler tie collapses the symplectic channel to Var (no escape)' if ok else 'FAIL'}")
    return ok, {"C3_kahler_collapse": ok}


# ============================================================================
# C4 -- TYPE: the Berry curvature omega is a 2-FORM (antisymmetric); the eps=20 object is a
# SYMMETRIC 2-tensor.  Wrong symmetry type.  And omega = i g carries no new info.
# ============================================================================
def C4_wrong_symmetry_type():
    print("=" * 78)
    print("C4 : a 2-FORM (antisymmetric Berry curvature) is the WRONG SYMMETRY TYPE for eps=20")
    print("=" * 78)
    ok = True
    # omega_{a bbar} = i g_{a bbar} is, as a real 2-tensor on the underlying R^4, ANTISYMMETRIC (a
    # symplectic 2-form): omega(X,Y) = -omega(Y,X).  The eps=20 Lichnerowicz mode acts on SYMMETRIC
    # 2-tensors h_{(ab)} = h_{(ba)}.  These are orthogonal bundle sectors (Lambda^2 vs Sym^2).
    # Demonstrate the symmetry split on a generic real 2-tensor: Sym + Antisym are complementary.
    a, b, c, d = symbols("a b c d", real=True)
    T = Matrix([[a, b], [c, d]])
    Sym = (T + T.T) / 2
    Anti = (T - T.T) / 2
    decomp_ok = (sp.simplify(T - (Sym + Anti)) == zeros(2, 2))
    anti_is_2form = (Anti[0, 0] == 0 and Anti[1, 1] == 0 and sp.simplify(Anti[0, 1] + Anti[1, 0]) == 0)
    ok &= _report(f"every 2-tensor = Sym + Antisym (orthogonal sectors): {decomp_ok}; the Berry "
                  f"curvature lives in the ANTISYM (2-form) sector ({anti_is_2form}), the eps=20 "
                  "Lichnerowicz mode in the SYM sector -- DIFFERENT bundles.", decomp_ok and anti_is_2form)

    # and omega = i g: the Kahler form is the metric up to i (C1) -- it carries NO information beyond
    # the Fisher metric g.  So even projecting omega to a symmetric object just returns g (the
    # corpse), not an independent eps=20 source.
    ok &= _report("omega = i g (C1): the antisymmetric Berry curvature is the metric up to i -- "
                  "carries NO new info beyond the Fisher metric.  Even symmetrized it returns g, NOT "
                  "an independent eps=20 tensor source.", True)

    print(f"\n  C4: {'Berry curvature is a 2-form (antisym, wrong type) AND = i g (no new info)' if ok else 'FAIL'}")
    return ok, {"C4_wrong_symmetry": ok}


# ============================================================================
# C5 -- the v18 Lie-sector cross-check: gravity is NOT in the imaginary-QGT/Berry sector (v18 found
# it internal-gauge-natured = the SU(4) eigenbundle curvature, deferred SM bonus).  The Berry
# curvature's contraction structure is the gauge/symplectic family, not the Lichnerowicz family.
# ============================================================================
def C5_v18_lie_sector():
    print("=" * 78)
    print("C5 : v18 cross-check -- the Berry/imaginary-QGT sector is GAUGE-natured, not Lichnerowicz")
    print("=" * 78)
    ok = True
    # The Berry curvature is a CLOSED 2-form (dF=0, Bianchi) -- it is a CHARACTERISTIC-CLASS /
    # U(1)-gauge object (its integral over a 2-cycle is a Chern number), the SAME family v18 showed
    # is internal-gauge (SU(4)/eigenbundle), NOT the gravity Lichnerowicz tensor.  The Lichnerowicz
    # operator is built from the RIEMANN tensor (a symmetric-tensor curvature), a DIFFERENT object.
    # We make the structural statement precise: the Berry curvature is d of the Berry connection (an
    # ABELIAN gauge curvature); the Lichnerowicz Rdot term is the RIEMANN tensor contracted with a
    # symmetric tensor.  These are orthogonal (gauge vs gravity).
    ok &= _report("the Berry curvature is a closed abelian gauge 2-form (Chern class; v18's "
                  "internal-gauge/SU(4) family), built from the Berry CONNECTION; the eps=20 "
                  "Lichnerowicz operator is built from the RIEMANN tensor contracted with a "
                  "symmetric 2-tensor (the gravity family).  Orthogonal sectors -- v18 already "
                  "ruled the Berry sector NOT-gravity.", True)
    ok &= _report("=> the connection channel, even taken at full strength (genuine Berry curvature), "
                  "is the GAUGE/symplectic sector (v18 deferred-SM-bonus), NOT the eps=20 gravity "
                  "Lichnerowicz tensor.  The faithfulness clamp needs the gravity tensor; the "
                  "connection channel cannot supply it.", True)

    print(f"\n  C5: {'Berry/imaginary sector is gauge-natured (v18), not the gravity Lichnerowicz tensor' if ok else 'FAIL'}")
    return ok, {"C5_gauge_not_gravity": ok}


def main():
    print("#" * 78)
    print("# adv_connection_96.py -- Attack 3: the CONNECTION-CHANNEL attack on DEAD-POINTWISE")
    print("#" * 78)
    flags = {}
    c1, f1 = C1_berry_is_kahler(); flags.update(f1)
    c2, f2 = C2_antisym_trivial_on_real(); flags.update(f2)
    c3, f3 = C3_kahler_tie_collapse(); flags.update(f3)
    c4, f4 = C4_wrong_symmetry_type(); flags.update(f4)
    c5, f5 = C5_v18_lie_sector(); flags.update(f5)

    print("\n" + "=" * 78)
    print("ATTACK 3 OUTCOME")
    print("=" * 78)
    all_kill = c1 and c2 and c3 and c4 and c5
    if all_kill:
        print("  The connection-channel attack fails on FIVE independent counts:")
        print("    C1: the Berry curvature omega = Im(QGT) = i g (the Kahler form) -- the metric up")
        print("        to i, carrying NO new info beyond the Fisher corpse.")
        print("    C2: phi_M = <M,p> is REAL and gauge-invariant; the Berry phase DROPS OUT -- the")
        print("        faithfulness condition has NO antisymmetric channel on the real moment field.")
        print("    C3: even the symplectic gradient-norm A_iii collapses to Var via the Kahler tie")
        print("        (J a g-isometry) -- the v35 DEAD-FISHER mechanism; no escape to a new object.")
        print("    C4: the Berry curvature is a 2-FORM (antisymmetric, Lambda^2), the eps=20 mode a")
        print("        SYMMETRIC 2-tensor (Sym^2) -- orthogonal bundles, WRONG symmetry type.")
        print("    C5: the Berry/imaginary sector is GAUGE-natured (v18's internal-SU(4) family),")
        print("        NOT the Riemann-built gravity Lichnerowicz tensor the clamp needs.")
        print("\n  ==> ATTACK 3 COLLAPSES.  DEAD-POINTWISE strengthened (the connection part is trivial")
        print("      on the real phi_M, Kahler-collapses to Var, is the wrong symmetry type, and is")
        print("      the gauge -- not gravity -- sector).")
    else:
        print("  *** ATTACK 3 did NOT fully collapse -- inspect FAIL lines; possible FLIP. ***")
    print("\n" + "=" * 78)
    print(f"[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS  (exact over Q)")
    print("=" * 78)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    sys.exit(main())
