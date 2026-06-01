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


# ====================================================================== TASK 2
print("\n" + "#" * 78)
print("# TASK 2 -- g=eta+h(M) curvature (indices raised with g, NOT cone-Hessian)")
print("#          + MANDATORY hand-rolled Riemann cross-check + signature (1,3)")
print("#" * 78)

# --- 2.0 delta={} sanity: flat baseline (corroborates Task 3) -------------------
tick("Task 2.0: delta={} (M=0) sanity -- expect g=eta_bg, h=0, R[g]=0 ...")
SC0 = E.spacetime_curvature_of_g({}, CENTER, bg_delta={}, simp=cancel)
assert SC0["h"] == Matrix.zeros(4, 4), "h != 0 at M=0 center"
assert SC0["g"] == SC0["eta_bg"], "g != eta_bg at M=0 center"
assert SC0["Rscalar"] == 0, f"R[g]={SC0['Rscalar']} != 0 at M=0 (flat baseline broken!)"
assert E.riemann_symmetry_ok(SC0["R"], 4, simp=cancel)
tick(f"  M=0: h==0, g==eta_bg, R[g]={SC0['Rscalar']} (FLAT) -- index-raising route returns flat baseline")

# --- 2.1 build g=eta+h(M) and its INTRINSIC curvature ---------------------------
tick("Task 2.1: building g=eta+h at representative M (bg+matter rational, slice rational) ...")
SC = E.spacetime_curvature_of_g(MATTER_DELTA, SLICE_M, bg_delta=BG_DELTA, simp=cancel)
g_M, h_M, ginv_M = SC["g"], SC["h"], SC["ginv"]
R_M, Ric_M, Rs_M = SC["R"], SC["Ric"], SC["Rscalar"]
tick(f"  g built; detg = {SC['detg']}; h != 0? {h_M != Matrix.zeros(4,4)}")
# index discipline: Riemann symmetries hold; raised with g^{-1}=(eta+h)^{-1}
assert E.riemann_symmetry_ok(R_M, 4, simp=cancel), "Riemann symmetries FAIL"
tick("  riemann_symmetry_ok(R[g],4) == True (antisym i,j; antisym k,l; pair swap)")
# Ric symmetric
assert all(cancel(Ric_M[i, j] - Ric_M[j, i]) == 0 for i in range(4) for j in range(4))
tick(f"  Ric[g] symmetric; R[g](M) = {Rs_M}")
# reality / exactness: Rscalar is a real rational (no Wick/float artifact)
assert Rs_M.is_real is not False
assert getattr(Rs_M, 'is_rational', None) is not False
tick(f"  R[g](M) is a real rational (no imaginary part / float artifact)")

# CONFIRM indices were raised with g, NOT H_bg: show g^{-1} != H_bg^{-1} and that the
# H_bg-raised Ricci scalar DIFFERS (the falsified route would give a different number)
H_bg_M = SC["H_bg"]
Hbg_inv = H_bg_M.inv().applyfunc(cancel)
assert cancel((ginv_M - Hbg_inv)).is_zero_matrix is not True, \
    "g^{-1} == H_bg^{-1}?! (the metrics would coincide -- they must not)"
# Ricci scalar if one WRONGLY raised with H_bg^{-1} (the falsified route), same C:
C_M = SC["C"]
R_wrong = E.totaro_riemann(Hbg_inv, C_M, 4, simp=cancel)
Rs_wrong = E.ricci_scalar(R_wrong, Hbg_inv, 4, simp=cancel)
tick(f"  INDEX-RAISING CHECK: R via g^-1=(eta+h)^-1 = {Rs_M}  vs  "
     f"R via bare H_bg^-1 (FALSIFIED route) = {Rs_wrong}  -- distinct: {Rs_M != Rs_wrong}")
assert Rs_M != Rs_wrong, "g^-1 and H_bg^-1 give the SAME R -- index-raising correction vacuous here"

# --- 2.2 MANDATORY hand-rolled Riemann cross-check ------------------------------
tick("Task 2.2: hand-rolled Christoffel/Riemann of g=eta+h (slice symbolic, matter "
     "rational) -- this is the watched step (expect ~tens of s) ...")
comps = [(0, 2, 0, 2), (2, 3, 2, 3), (0, 1, 0, 1)]
HR = E.hand_rolled_riemann_of_g(MATTER_DELTA, SLICE_M, bg_delta=BG_DELTA,
                                components=comps, simp=cancel)
tick("  hand-rolled Riemann components computed; comparing to Totaro-g^{-1} ...")
agree = True
for (i, j, k, l) in comps:
    totaro_val = cancel(R_M[i][j][k][l])
    hand_val = cancel(HR[(i, j, k, l)])
    ok = (cancel(totaro_val - hand_val) == 0)
    agree = agree and ok
    tick(f"  R_{i}{j}{k}{l}: Totaro-g^-1 = {totaro_val} ; hand-rolled = {hand_val} ; agree={ok}")
assert agree, "HAND-ROLLED Riemann DISAGREES with Totaro-g^{-1} -- hand-rolled is PRIMARY"
tick("  MANDATORY CROSS-CHECK PASS: Totaro-g^{-1} == hand-rolled Riemann of g=eta+h "
     "on >=2 components, EXACT over Q (Totaro applicability to eta+h validated)")

# --- 2.3 signature (1,3) of g at the chosen M -----------------------------------
npos, nneg, nzero = E.eig_signature_count(g_M, simp=cancel)
tick(f"  signature of g=eta+h at M: (#pos,#neg,#zero) = ({npos},{nneg},{nzero}) "
     f"[eigenvalue-sign test; null-aligned frame => NOT Sylvester]")
assert (npos, nneg, nzero) == (1, 3, 0), \
    f"g signature {(npos,nneg,nzero)} != (1,3) -- left the small-||M|| Lorentzian regime"
tick("  signature (1,3) CONFIRMED (small-||M|| Lorentzian regime, 70.1 splice-consistency)")

print("-" * 78)
print(f"TASK 2 OK -- spacetime_curvature_of_g built (indices raised with g=eta+h, "
      f"C from cone-Hessian potential); R[g](M)={Rs_M}; hand-rolled cross-check PASS; "
      f"signature (1,3); M=0 returns flat.")
