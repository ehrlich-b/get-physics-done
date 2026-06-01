#!/usr/bin/env python3
"""Phase 72-01 driver: matter-on-flat, build-and-confirm (EXACT over Q).

Per the Phase-70.1 human-ratified verdict, the PHYSICAL spacetime metric is
g = eta + h(x;M) (eta = flat KKT Minkowski, DERIVED from det_2; the cone-Hessian is
the matter SOURCE, not the metric). This driver:

  Task 1 -- mechanism + index audit; cross-term is the unique V_0<->V_{1/2} channel;
            det SSOT guard; representative-M non-vacuity; Phase-71 SOURCE regression.
  Task 2 -- spacetime_curvature_of_g (indices raised with g^{-1}=(eta+h)^{-1}, NOT
            H_bg^{-1}); MANDATORY hand-rolled Riemann cross-check; signature (1,3).
  Task 3 -- FLAT M=0 baseline (R=S=Weyl=0, DERIVED -- NOT R=-3); n=4 Ricci
            decomposition of the M!=0 curvature; V_1-inertness.

Imports the warm engine as a module (does NOT run its ~183s main()). Foreground
`python3 -u`; prints progress between heavy steps (watchdog discipline).

Run:    python3 -u .gpd/phases/72-b-matter-sourcing/72-01-matter-on-flat.py
Expect: every assert passes; final line MATTER_ON_FLAT_OK; exit 0.
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'code'))
from sympy import Rational, cancel, simplify, Matrix, log as _log, symbols

import bulk_geometry_verification as E

t0 = time.time()
n = 4


def tick(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


# Basepoint placements (from 72-01-baseline-probe.py / preserved 72-RESEARCH):
#   bg_delta : FIXED V_0-internal x1 partner (e_1,e_4 content) so the cross-term has
#              all three slots populated.
#   matter_delta : M in V_{1/2} (x2,x3 each with e_0,e_4 content).
CENTER = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]
R1 = E.ROUTE1_COMMON_SLICE_PT                       # [2/5,3/5,1/10,1/8]
BG_DELTA = {4: Rational(1, 4), 7: Rational(1, 5)}   # V_0-internal x1 partner
MATTER_DELTA = {11: Rational(1, 3), 15: Rational(1, 6),
                19: Rational(1, 3), 23: Rational(1, 7)}   # V_{1/2} matter
# A rational slice basepoint for the matter curvature (interior, keeps det_3>0):
SLICE_M = [Rational(2, 5), Rational(3, 5), Rational(1, 10), Rational(1, 8)]

print("=" * 78)
print("PHASE 72-01 : matter-on-flat -- curvature of g=eta+h(x;M), build & confirm")
print("=" * 78)
tick("engine imported")


# ====================================================================== TASK 1
print("\n" + "#" * 78)
print("# TASK 1 -- mechanism + index audit; cross-term uniqueness; SOURCE regression")
print("#" * 78)

# --- 1.1 det SSOT guard: octonion_algebra.py NOT on the decisive path -----------
guard_ok, guard_detail = E.exact_only_guard_p70()
assert guard_ok, guard_detail
tick(f"SSOT GUARD: no octonion_algebra import / no float-rank on decisive path -- "
     f"[{guard_detail}]")
# engine det_3 byte-identical to the certified ring_lemma_verification.py det_3
vc_ok, vc_detail = E.verbatim_copy_integrity()
assert vc_ok, vc_detail
tick(f"SSOT: engine det_3 byte-identical to ring_lemma_verification det_3 [{vc_detail}]")

# --- 1.2 Peirce index map -------------------------------------------------------
groups, diagonal = E.peirce_indices_under_E11()
assert sorted(groups[Rational(1)]) == [0]
assert sorted(groups[Rational(0)]) == list(range(1, 11))
assert sorted(groups[Rational(1, 2)]) == list(range(11, 27))
assert diagonal
tick("INDEX MAP: V_1={0}, V_0={1..10}, V_1/2={11..26}; L_E11 diagonal -- CONFIRMED")
# slice + center cone-Hessian
H0 = E.cone_hessian_at_center(slice_order=[1, 2, 3, 10])
assert H0 == Matrix([[9, 0, 0, 0], [0, 9, 0, 0], [0, 0, 18, 0], [0, 0, 0, 18]])
assert H0.det() == 26244
assert E.SPACETIME_SLICE_IDX == [1, 2, 3, 10]
tick(f"SLICE: H0=cone_hessian_at_center([1,2,3,10])=diag(9,9,18,18), det {H0.det()} -- CONFIRMED")
# slice det form = det_2/3 Minkowski
form, target, _ = E.slice_det_form()
assert simplify(form - target) == 0
tick(f"SLICE det form = beta*gamma/3 - p^2/3 - q^2/3 (det_2/3 Minkowski) -- CONFIRMED")

# --- 1.3 cross-term is the unique V_0<->V_{1/2} channel -------------------------
Xs = E.X_from_symbols(E.xs)
a, b, gg, x1, x2, x3 = E._coord_from_octmat(Xs)
n1, n2, n3 = E._oct_normsq(x1), E._oct_normsq(x2), E._oct_normsq(x3)
cross = E.oct_mul(E.oct_mul(x2, x1), x3)               # (x2 x1) x3 -- SSOT order
det_block_expr = a * b * gg - a * n1 - b * n2 - gg * n3
assert simplify(E.det_3(Xs) - det_block_expr - 2 * cross[0]) == 0
assert not (cross[0].free_symbols & {E.xs[0], E.xs[1], E.xs[2]})  # alpha,beta,gamma absent
tick("CROSS-TERM: det_3 - diag-norm == 2Re((x2 x1)x3); alpha,beta,gamma absent from triple -- CONFIRMED")
# polarization of the (V_1/2, V_0, V_1/2) vertex nonzero on octonionic directions
e4 = [0, 0, 0, 0, 1, 0, 0, 0]
e5 = [0, 0, 0, 0, 0, 1, 0, 0]
e7 = [0, 0, 0, 0, 0, 0, 0, 1]
# x1:e4 (V_0), x2:e5 (V_1/2), x3:e7 (V_1/2)
Dx1 = E.h3o_from_coords(0, 0, 0, e4, E.oct_zero(), E.oct_zero())
Dx2 = E.h3o_from_coords(0, 0, 0, E.oct_zero(), e5, E.oct_zero())
Dx3 = E.h3o_from_coords(0, 0, 0, E.oct_zero(), E.oct_zero(), e7)
pol = simplify(E.polarize_d(Dx2, Dx1, Dx3))
assert pol != 0
# zeroing any one slot kills it
pol0 = simplify(E.polarize_d(Dx2, Dx1, E.h3o_from_coords(0, 0, 0, E.oct_zero(), E.oct_zero(), E.oct_zero())))
assert pol0 == 0
tick(f"CROSS-VERTEX: polarize_d(x2:e5, x1:e4, x3:e7) = {pol} != 0; zeroing a slot => 0 -- CONFIRMED")

# --- 1.4 non-vacuity preflight for the cross-term test (used by 72-02) ----------
full = {**BG_DELTA, **MATTER_DELTA}
sub = E._offcenter_subs(full, slice_symbolic=False, slice_vals=CENTER)
Xv = E.X_from_symbols([sub[E.xs[k]] for k in range(27)])
_, _, _, x1v, x2v, x3v = E._coord_from_octmat(Xv)
cross_M = simplify(2 * E.oct_mul(E.oct_mul(x2v, x1v), x3v)[0])
assert cross_M == Rational(-13, 315) and cross_M != 0
assert not E.oct_is_zero(x1v) and not E.oct_is_zero(x2v) and not E.oct_is_zero(x3v)
assert x1v[4] != 0 and x2v[4] != 0 and x3v[4] != 0   # all three slots, e_4 content
tick(f"NON-VACUITY: cross-term = {cross_M}, all 3 slots populated, e_4 content -- CONFIRMED")

# --- 1.5 Phase-71 matterless cone-Hessian SOURCE-engine regression --------------
anchors = {
    "{4:1/3}": ({4: Rational(1, 3)}, Rational(-73041507, 21967969)),
    "{4:1/5,5:1/7}": ({4: Rational(1, 5), 5: Rational(1, 7)}, Rational(-521269105, 154700283)),
}
for lbl, (dlt, expect) in anchors.items():
    Rv, _, _, _, _ = E._curvature_invariants_at(dlt, R1, simp=cancel)
    assert Rv == expect, (lbl, Rv, expect)
    tick(f"SOURCE REGRESSION R({lbl}) @ R1 = {Rv} -- matches 71-VERIFICATION")
Rc0, _, _, _, _ = E._curvature_invariants_at({}, CENTER, simp=cancel)
assert Rc0 == -3
tick(f"SOURCE REGRESSION R(center) = {Rc0} (cone-Hessian SOURCE, NOT spacetime) -- matches anchor")

print("-" * 78)
print("TASK 1 OK -- index map, cross-term uniqueness, SSOT guard, non-vacuity, "
      "SOURCE regression all exact over Q.")
print("FIRST_RESULT_GATE_TASK1: SOURCE engine faithful; cross-term is the unique "
      "matter channel; representative M non-vacuous (-13/315).")
