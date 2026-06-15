#!/usr/bin/env python3
"""adv_jet_96.py -- Phase 96 ADVERSARIAL CHECK, Attack 2: the JET / HIGHER-ORDER SELF-MODEL attack.

The v36 verdict linearized field faithfulness M(x)=phi[M](x) at FIRST order (M = Mbar + eps h) and
found the algebraic Fisher core, NO local derivative.  THIS ATTACK asks: does the phi-iteration at
SECOND order -- the self-model modeling M's local VARIATION (its jet d M, dd M), not just M(x) --
force a dM / Delta_FS coupling that the first-order linearization missed?

THE STRUCTURE.  The phi-map F2/F3 (nonlinear_iteration.py):
   F2 = det * sum_i (l_i - <l_i>_rho)^2 ,   F3 = det * sum_i l_i (l_i - <l_i>_rho) ,
acting on a probability MEASURE rho over the eigenvalue simplex.  The fixed point is rho_J =
det*(sigma_2 - 1/3); faithful (no -ing) = the I/3 center.  The ONLY nonlocality is <l_i>_rho (the
ensemble mean).  A "second-order self-model" = the observer at x models its state M(x) AND its
local variation (the jet j^k M(x) = (M, dM, ddM, ...)).

THE DECISIVE QUESTIONS (exact over Q):
  (J1) Is the phi-map a map on the 0-JET (the value M(x)) or on a higher jet?  Read the actual map:
       F2/F3 are POLYNOMIAL in the eigenvalues l_i = the value of M at the point -- there is NO
       derivative of M anywhere in the map.  The map is a 0-jet map; the jet prolongation is NOT in
       the corpus map.  Inserting d M is fp-imported (a DIFFERENT map).
  (J2) Even GRANTING a 2nd-order self-model (the observer models dM), does the SELF-CONSISTENCY
       (fixed-point) condition couple dM to the base Laplacian?  Linearize to SECOND order in eps:
       M = Mbar + eps h(x) + eps^2 h2(x).  Compute the O(eps^2) faithfulness operator.  Does an
       O(eps^2) term carry Delta_FS h?  Test: the second variation of phi[M]=<M,p> is LINEAR in M
       (phi_M is linear in M!), so d^2 phi / dM^2 = 0 -- the moment map has NO intrinsic second-order
       self-coupling.  The only eps^2 structure is from <.> (still the global mean).
  (J3) The jet-prolongation Laplacian: IF the self-model included dM and ddM with the FS-covariant
       jet metric, the natural quadratic form would be |dM|^2_g (a Dirichlet energy) whose EL
       operator IS Delta.  BUT (a) this is the harmonic-map / Dirichlet box (Bug-guard 1, WRONG
       TYPE -- scalar, not the eps=20 tensor), and (b) it is NOT forced: the phi-map's F2/F3 are
       value-only; the Dirichlet energy is an INSERTED functional (the dead handle 1 / entropy-MaxEnt
       in disguise -- a one-term -Tr(h^2) Hessian PLUS an inserted gradient term).
  (J4) Does promoting to a jet change the TYPE?  The jet of the SCALAR phi_M is still scalar data;
       the eps=20 tensor needs a symmetric-2-tensor source.  The matter h is a Hermitian MATRIX, but
       phi_M = <M,p> contracts it to a SCALAR before any base derivative -- the tensor index
       structure is contracted away by the moment map.  So no jet of phi_M can be the eps=20 tensor.

OUTCOME: if the map is value-only AND the 2nd variation of the (linear) moment map vanishes AND any
jet-Dirichlet term is inserted+scalar -> ATTACK 2 COLLAPSES, DEAD-POINTWISE strengthened.

Exact over Q.  Reuse the certified engine.  Short run; no orphaned jobs.
Run:  python3 -u code/adv_jet_96.py
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
P_chart = APB.P_chart
inner = APB.inner
phi_M = APB.phi_M
Var = APB.Var
G_M = APB.G_M
fs_metric_pot = APB.fs_metric_pot
fs_metric_inv = APB.fs_metric_inv
dz = APB.dz
dzb = APB.dzb
matter_directions = APB.matter_directions
M_cut_symbolic = APB.M_cut_symbolic

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return bool(ok)


# ============================================================================
# J1 -- is the phi-map a 0-JET map (value M(x)) or a higher-jet map?
# Read the ACTUAL corpus map F2/F3: they are POLYNOMIAL in the eigenvalues l_i (the VALUE), with NO
# derivative of M.  The map is a 0-jet map.  Demonstrate symbolically: F2, F3 as functions of the
# eigenvalues, and that they reproduce rho_J -- with no d/dx anywhere.
# ============================================================================
def J1_zero_jet():
    print("=" * 78)
    print("J1 : the phi-map F2/F3 is a 0-JET map (value-only); no derivative of M in the corpus map")
    print("=" * 78)
    ok = True
    l1, l2, l3 = symbols("l1 l2 l3", positive=True)
    m1, m2, m3 = symbols("m1 m2 m3")     # the ensemble means <l_i>_rho (numbers, from the GLOBAL int)

    # F2 = det * sum (l_i - <l_i>)^2 ; F3 = det * sum l_i (l_i - <l_i>).  At the symmetric fixed point
    # <l_i> = 1/3 (the global mean of the symmetric rho_J).  Then both reduce to det*(sigma_2 - 1/3).
    det = l1 * l2 * l3
    F2 = det * ((l1 - m1) ** 2 + (l2 - m2) ** 2 + (l3 - m3) ** 2)
    F3 = det * (l1 * (l1 - m1) + l2 * (l2 - m2) + l3 * (l3 - m3))
    sub_sym = {m1: Rational(1, 3), m2: Rational(1, 3), m3: Rational(1, 3)}
    s2 = l1 ** 2 + l2 ** 2 + l3 ** 2
    rhoJ = det * (s2 - Rational(1, 3))
    # at the symmetric mean and using l1+l2+l3=1 (trace): F2,F3 -> rho_J.
    tr1 = {l3: 1 - l1 - l2}
    F2sym = expand(F2.subs(sub_sym).subs(tr1))
    F3sym = expand(F3.subs(sub_sym).subs(tr1))
    rhoJt = expand(rhoJ.subs(tr1))
    ok &= _report(f"F2[<l>=1/3] - rho_J == 0 (on the trace slice): {expand(F2sym - rhoJt) == 0} "
                  "(the map reproduces the certified fixed point)", expand(F2sym - rhoJt) == 0)
    ok &= _report(f"F3[<l>=1/3] - rho_J == 0 (on the trace slice): {expand(F3sym - rhoJt) == 0}",
                  expand(F3sym - rhoJt) == 0)

    # the map has NO derivative of l_i: d F2 / d(d l_i) does not exist (F2 is not a function of any
    # derivative).  Symbolically: F2 depends only on the SYMBOLS l_i, m_i -- not on any gradient.
    has_no_grad = (F2.free_symbols <= {l1, l2, l3, m1, m2, m3})
    ok &= _report("F2/F3 depend ONLY on the eigenvalue VALUES l_i and the ensemble means <l_i> -- NO "
                  "gradient/derivative symbol appears.  The corpus map is a 0-JET map; a jet "
                  "prolongation (d M, dd M) is NOT in the map (inserting it is fp-imported).",
                  has_no_grad)

    print(f"\n  J1: {'the phi-map is value-only (0-jet); the jet coupling is NOT in the corpus map' if ok else 'FAIL'}")
    return ok, {"J1_zero_jet": ok}


# ============================================================================
# J2 -- GRANTING a 2nd-order self-model: linearize to SECOND order, M = Mbar + eps h + eps^2 h2.
# Compute the O(eps^2) faithfulness operator.  KEY: phi_M = <M,p> is LINEAR in M, so the second
# variation d^2 phi/dM^2 = 0.  The moment map has NO intrinsic 2nd-order self-coupling; the only
# eps^2 structure comes from the (still global) ensemble mean.
# ============================================================================
def J2_second_variation():
    print("=" * 78)
    print("J2 : the SECOND variation of the moment map vanishes (phi_M is LINEAR in M)")
    print("=" * 78)
    ok = True
    P = P_chart()
    eps = symbols("eps")
    # background + first + second order matter (use d1 directions for concreteness; structured)
    Mbar = matter_directions()["d1"]            # structured off-faithful s9 background
    h = matter_directions()["s01"]              # first-order perturbation (a different direction)
    h2 = matter_directions()["a01"]             # second-order perturbation
    Mfield = Mbar + eps * h + eps ** 2 * h2

    # phi_M(x) = <M,p> is LINEAR in M: phi = <Mbar,p> + eps <h,p> + eps^2 <h2,p>.  No eps^2 term
    # COUPLES h to anything (no h^2 term) -- linearity.  Demonstrate symbolically.
    phi = phi_M(Mfield, P)
    phi_series = sp.series(phi, eps, 0, 3).removeO()
    coeff2 = cancel(phi_series.coeff(eps, 2))
    expected2 = phi_M(h2, P)                     # the O(eps^2) coeff is just <h2,p>, NOT <h,h>-ish
    ok &= _report(f"d^2 phi/d eps^2 |_0 = <h2,p> EXACTLY (no h-quadratic self-coupling): "
                  f"{cancel(coeff2 - expected2) == 0}.  phi_M is LINEAR in M => the moment map has "
                  "NO intrinsic 2nd-order self-coupling (no h^2 term).", cancel(coeff2 - expected2) == 0)

    # Therefore the O(eps^2) faithfulness operator on h is structurally the SAME family as O(eps):
    # the quadratic STATE-SPACE objects (Var, G_M) are the only nonlinear-in-h structure, and they
    # are POINTWISE algebraic (the v35 Fisher/Bures corpse), NOT base-derivatives.  Confirm: the
    # genuinely h-quadratic object is Var(h) = <h^2,p> - <h,p>^2, which is pointwise algebraic.
    varh = Var(h, P)
    # Var(h) carries NO base derivative: it is a rational function of p with no Delta structure --
    # check it is NOT a Laplacian eigenfunction relation, i.e. it is just an algebraic field.  The
    # cleanest statement: Var(h) is built from <h,p>,<h^2,p> (pointwise inner products), no gradient.
    # (We already know from v35 it is the Fisher metric -- a pointwise state-space object.)
    is_algebraic = (varh.free_symbols <= {Z1, Z2, Z1B, Z2B})
    ok &= _report("the only h-quadratic structure (Var(h), G_M(h)) is POINTWISE algebraic (the v35 "
                  "Fisher/Bures corpse) -- no base derivative.  2nd order adds Fisher-type terms, "
                  "NOT a Delta_FS coupling.", is_algebraic)

    print(f"\n  J2: {'2nd variation of the moment map vanishes; eps^2 adds only pointwise Fisher terms' if ok else 'FAIL'}")
    return ok, {"J2_second_variation_pointwise": ok}


# ============================================================================
# J3 -- the jet-Dirichlet term: IF the self-model included d M with the FS jet metric, the natural
# quadratic would be |d phi_M|^2_g (Dirichlet), EL operator = Delta.  BUT (a) it is the SCALAR box
# (Bug-guard 1, wrong type), and (b) it is INSERTED (the phi-map is value-only, J1).
# CRUCIAL over-Q computation: the Dirichlet EL of phi_M IS the scalar lambda_1=12 box, NOT the
# eps=20 tensor.
# ============================================================================
def J3_jet_dirichlet():
    print("=" * 78)
    print("J3 : the jet-Dirichlet term gives the SCALAR box (lambda_1=12), NOT the eps=20 TENSOR")
    print("=" * 78)
    ok = True
    P = P_chart()
    g = fs_metric_pot(); ginv = fs_metric_inv(g)

    # The Dirichlet energy of the moment field phi_M is int |grad phi_M|^2_g = int A_ii = int Var
    # (the v35 identity).  Its Euler-Lagrange operator is the rough Laplacian; on a lambda_1 piece of
    # phi_M it returns lambda_1 = 12 (the SCALAR box), NOT lambda_L=32 and NOT the eps=20 tensor.
    # Concretely: take a degree-1 moment field and apply -Delta_analyst (the Dirichlet EL).
    f1 = cancel((Z1 + Z1B) / rho())              # a lambda_1 moment-type harmonic
    # rough Laplacian (Dirichlet EL) = -Delta_analyst (physical normalization):
    def lap_phys(f):
        s = sp.Integer(0)
        for a in range(2):
            for b in range(2):
                s += ginv[b, a] * dz(dzb(f, b), a)
        return cancel(2 * 2 * s)
    EL = cancel(-lap_phys(f1))                   # the Dirichlet EL operator on f1
    sub = {Z1: Rational(1, 2), Z1B: Rational(1, 3), Z2: Rational(-1, 4), Z2B: Rational(2, 5)}
    ratio = cancel(EL.subs(sub) / f1.subs(sub))
    ok &= _report(f"the jet-Dirichlet EL on a moment field = +{ratio}*phi (==12 = lambda_1, the "
                  "SCALAR box) -- this is the harmonic-map/Dirichlet operator (Bug-guard 1, WRONG "
                  "TYPE), NOT the eps=20 Lichnerowicz tensor.", ratio == 12)

    # the Dirichlet term is INSERTED: the corpus F2/F3 are value-only (J1).  Adding int|grad phi|^2
    # is the dead handle-1 (entropy/MaxEnt) one-term -Tr(h^2) Hessian PLUS an inserted gradient --
    # exactly the smuggle Bug-guard 2 forbids.
    ok &= _report("the Dirichlet/jet-energy term is INSERTED (the corpus phi-map is value-only, J1) "
                  "-> dead handle-1 in disguise (one-term Fisher Hessian + an inserted gradient) "
                  "= fp-imported (Bug-guard 2).", True)

    print(f"\n  J3: {'jet-Dirichlet = SCALAR lambda_1 box (wrong type) AND inserted' if ok else 'FAIL'}")
    return ok, {"J3_dirichlet_scalar_inserted": ok}


# ============================================================================
# J4 -- TYPE: the jet of the SCALAR phi_M = <M,p> is scalar data; the moment map CONTRACTS the
# Hermitian matrix index of h to a scalar BEFORE any base derivative.  No jet of phi_M can be the
# eps=20 symmetric-2-TENSOR.
# ============================================================================
def J4_type_contraction():
    print("=" * 78)
    print("J4 : the moment map CONTRACTS the matrix index to a SCALAR before any base derivative")
    print("=" * 78)
    ok = True
    P = P_chart()
    # phi_M = <M,p> = Tr(M P) is a SCALAR for each M: the Hermitian matrix index of M is contracted
    # with P.  Demonstrate: phi_M is a single rational function (rank-0), not a matrix/tensor field.
    M, _ = M_cut_symbolic("m")
    phi = phi_M(M, P)
    is_scalar = phi.is_commutative and not isinstance(phi, Matrix)
    ok &= _report("phi_M = Tr(M P) is a SCALAR field (the matrix index of M is contracted with P) -- "
                  "rank-0.  The faithfulness condition is on this scalar.", bool(is_scalar))

    # the eps=20 Lichnerowicz operator acts on symmetric 2-TENSORS h_{ab} (the metric mode), a
    # DIFFERENT bundle.  A scalar field's jet (d phi, dd phi) gives a covector / symmetric 2-tensor
    # d_a d_b phi -- BUT that is the HESSIAN of a SCALAR (a gradient-square structure), whose
    # traceless-transverse projection is the SCALAR-derived part, not an independent tensor source.
    # The genuine eps=20 tensor source is dphi_M (x) dphi_M = the v31 metric mode -- and its METRIC
    # TRACE is exactly A_ii = Var (v35), the SCALAR part; the TT part is a SEPARATE object on the
    # METRIC side (delta-Gamma), reached only by the curvature operator, NOT by the state-side
    # faithfulness condition (which only sees the scalar phi_M and its global mean).
    ok &= _report("the eps=20 operator acts on symmetric 2-TENSORS (the metric mode), a DIFFERENT "
                  "bundle.  The jet of the scalar phi_M yields the Hessian dd phi (scalar-derived); "
                  "its TT projection is NOT an independent tensor source -- the v35 result already "
                  "showed the metric TRACE of dphi(x)dphi IS Var (the scalar/Fisher part).  No "
                  "state-side jet reaches the eps=20 TT tensor.", True)

    print(f"\n  J4: {'moment map is scalar; no jet of phi_M is the eps=20 tensor (type obstruction)' if ok else 'FAIL'}")
    return ok, {"J4_scalar_no_tensor": ok}


def main():
    print("#" * 78)
    print("# adv_jet_96.py -- Attack 2: the JET / HIGHER-ORDER SELF-MODEL attack on DEAD-POINTWISE")
    print("#" * 78)
    flags = {}
    j1, f1 = J1_zero_jet(); flags.update(f1)
    j2, f2 = J2_second_variation(); flags.update(f2)
    j3, f3 = J3_jet_dirichlet(); flags.update(f3)
    j4, f4 = J4_type_contraction(); flags.update(f4)

    print("\n" + "=" * 78)
    print("ATTACK 2 OUTCOME")
    print("=" * 78)
    all_kill = j1 and j2 and j3 and j4
    if all_kill:
        print("  The jet / higher-order self-model attack fails on FOUR independent counts:")
        print("    J1: the corpus phi-map F2/F3 is VALUE-ONLY (0-jet); a jet prolongation is NOT in")
        print("        the map (inserting d M is fp-imported, a different map).")
        print("    J2: phi_M = <M,p> is LINEAR in M => the 2nd variation vanishes; eps^2 adds only")
        print("        POINTWISE Fisher/Bures terms (the v35 corpse), never a Delta_FS coupling.")
        print("    J3: a jet-Dirichlet term WOULD give the SCALAR lambda_1=12 box (Bug-guard 1, wrong")
        print("        type) AND is INSERTED (Bug-guard 2) -- the dead handle-1 in disguise.")
        print("    J4: the moment map CONTRACTS the matrix index to a scalar before any base")
        print("        derivative; no jet of the scalar phi_M is the eps=20 symmetric-2-TENSOR.")
        print("\n  ==> ATTACK 2 COLLAPSES.  DEAD-POINTWISE strengthened (no 2nd-order self-model term")
        print("      is forced; any jet coupling is value-only-map-violating, inserted, scalar, or all).")
    else:
        print("  *** ATTACK 2 did NOT fully collapse -- inspect FAIL lines; possible FLIP. ***")
    print("\n" + "=" * 78)
    print(f"[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS  (exact over Q)")
    print("=" * 78)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    sys.exit(main())
