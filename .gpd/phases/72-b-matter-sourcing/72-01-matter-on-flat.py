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
#              all three slots populated (used in Task 1's non-vacuity check).
#   matter_delta : M in V_{1/2} (x2,x3 each with e_0,e_4 content).
CENTER = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]
R1 = E.ROUTE1_COMMON_SLICE_PT                       # [2/5,3/5,1/10,1/8]
BG_DELTA = {4: Rational(1, 4), 7: Rational(1, 5)}   # V_0-internal x1 partner
# Task-1 cross-term representative (large amplitude; non-vacuity = -13/315). Under the
# B1 metric g=eta+h this amplitude is OUTSIDE the small-||M|| Lorentzian regime: the
# matter-induced h dominates eta_bg and FLIPS the signature to (0,4) (the documented
# perturbative boundary; see the plan `approximations` block). It is retained ONLY for
# the Task-1 cross-term non-vacuity assertion, NOT as a curvature-of-g basepoint.
MATTER_DELTA = {11: Rational(1, 3), 15: Rational(1, 6),
                19: Rational(1, 3), 23: Rational(1, 7)}   # V_{1/2} matter (Task-1)
# A rational slice basepoint (interior, keeps det_3>0) for the Task-1 cross-term:
SLICE_M = [Rational(2, 5), Rational(3, 5), Rational(1, 10), Rational(1, 8)]

# Task-2/3 SMALL-||M|| LORENTZIAN representative (INSIDE the declared perturbative
# regime): the SAME V_{1/2} matter PATTERN scaled by 1/10, at the CENTER slice point
# (where the matterless cone-Hessian = diag(9,9,18,18), det 26244 -- comfortably away
# from the det_3=0 boundary). Here the B1 h is small (||h|| < ||eta_bg||~O(1)), so g
# stays Lorentzian (1,3) AND R[g](M)!=0 (genuinely curved). No bg partner needed: the
# cross-term non-vacuity is a Task-1 fact, independent of the curvature basepoint.
MATTER_L = {k: v * Rational(1, 10) for k, v in MATTER_DELTA.items()}
SLICE_L = CENTER

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

# --- 2.0 M=0 FLAT BASELINE (B1), over a NEIGHBOURHOOD (not just at the center pt) ----
# B1: h(x;M=0) = H_source(x;bg) - H_source(x;bg) == 0 IDENTICALLY in x => g=eta_bg
# EVERYWHERE => R[g]=0 over a neighbourhood (the DERIVED flat baseline). This is the
# CORRECTION to the disconfirming observation: the OLD centered h := H_bg - H_center
# gave R[g](M=0)=17496 (curved!) because H_center is a CONSTANT (h!=0 off-center).
tick("Task 2.0: B1 M=0 flat baseline at the CENTER slice point ...")
SC0 = E.spacetime_curvature_of_g({}, CENTER, bg_delta={}, simp=cancel)
assert SC0["h"] == Matrix.zeros(4, 4), "h != 0 at M=0 center"
assert SC0["g"] == SC0["eta_bg"], "g != eta_bg at M=0 center"
assert SC0["Rscalar"] == 0, f"R[g]={SC0['Rscalar']} != 0 at M=0 center (flat baseline broken!)"
assert E.riemann_symmetry_ok(SC0["R"], 4, simp=cancel)
tick(f"  M=0 @ center: h==0, g==eta_bg, R[g]={SC0['Rscalar']} (FLAT)")
tick("Task 2.0b: B1 M=0 flat baseline at an OFF-CENTER slice point (neighbourhood test) ...")
SC0o = E.spacetime_curvature_of_g({}, SLICE_M, bg_delta={}, simp=cancel)
assert SC0o["h"] == Matrix.zeros(4, 4), "B1 h(x;M=0) != 0 OFF-center (centered-h bug!)"
assert SC0o["Rscalar"] == 0, f"R[g]={SC0o['Rscalar']} != 0 at M=0 OFF-center (NOT flat over nbhd!)"
tick(f"  M=0 @ OFF-center: h==0 identically in x, R[g]={SC0o['Rscalar']} (FLAT over a NEIGHBOURHOOD -- B1)")
tick("Task 2.0c: B1 M=0 flat with the V_0 background partner ON (bg cancels) ...")
SC0b = E.spacetime_curvature_of_g({}, SLICE_M, bg_delta=BG_DELTA, simp=cancel)
assert SC0b["h"] == Matrix.zeros(4, 4) and SC0b["Rscalar"] == 0, "bg partner did NOT cancel at M=0"
tick(f"  M=0 / bg ON: h==0 (V_0 partner retained in BOTH terms => cancels), R[g]=0")

# --- 2.1 build g=eta+h(M) and its INTRINSIC curvature (small-||M|| Lorentzian M) ----
tick("Task 2.1: building g=eta+h at the small-||M|| LORENTZIAN representative "
     "(matter pattern /10, slice at center) ...")
SC = E.spacetime_curvature_of_g(MATTER_L, SLICE_L, bg_delta={}, simp=cancel)
g_M, h_M, ginv_M = SC["g"], SC["h"], SC["ginv"]
R_M, Ric_M, Rs_M = SC["R"], SC["Ric"], SC["Rscalar"]
tick(f"  g built; detg = {SC['detg']}; h != 0? {h_M != Matrix.zeros(4,4)}; R[g](M) != 0? {Rs_M != 0}")
assert h_M != Matrix.zeros(4, 4), "h == 0 at M != 0 (matter not entering!)"
assert Rs_M != 0, "R[g](M) == 0 at M != 0 (no curvature -- matter inert?!)"
# index discipline: Riemann symmetries hold; raised with g^{-1}=(eta+h)^{-1}
assert E.riemann_symmetry_ok(R_M, 4, simp=cancel), "Riemann symmetries FAIL"
tick("  riemann_symmetry_ok(R[g],4) == True (antisym i,j; antisym k,l; pair swap)")
# Ric symmetric
assert all(cancel(Ric_M[i, j] - Ric_M[j, i]) == 0 for i in range(4) for j in range(4))
tick(f"  Ric[g] symmetric; R[g](M) = {Rs_M}")
# reality / exactness: Rscalar is a real rational (no Wick/float artifact)
assert Rs_M.is_real is not False and getattr(Rs_M, 'is_rational', None) is not False
tick(f"  R[g](M) is a real rational (no imaginary part / float artifact)")

# CONFIRM indices were raised with g, NOT H_bg: g^{-1} != H_bg^{-1}, and the
# H_bg-raised Ricci scalar (the FALSIFIED route, same C) gives a DIFFERENT number.
H_bg_M = SC["H_bg"]
Hbg_inv = H_bg_M.inv().applyfunc(cancel)
assert cancel((ginv_M - Hbg_inv)).is_zero_matrix is not True, \
    "g^{-1} == H_bg^{-1}?! (the metrics would coincide -- they must not)"
C_M = SC["C"]
R_wrong = E.totaro_riemann(Hbg_inv, C_M, 4, simp=cancel)
Rs_wrong = E.ricci_scalar(R_wrong, Hbg_inv, 4, simp=cancel)
tick(f"  INDEX-RAISING CHECK: R via g^-1=(eta+h)^-1 = {Rs_M}  vs  "
     f"R via bare H_bg^-1 (FALSIFIED route) = {Rs_wrong}  -- distinct: {Rs_M != Rs_wrong}")
assert Rs_M != Rs_wrong, "g^-1 and H_bg^-1 give the SAME R -- index-raising correction vacuous here"

# --- 2.2 MANDATORY hand-rolled Riemann cross-check (the watched heavy step) ---------
tick("Task 2.2: hand-rolled Levi-Civita Riemann of g=eta+h (slice symbolic, matter "
     "rational; WATCHDOG-SAFE evaluate-then-invert; ~tens of s) ...")
comps = [(0, 2, 0, 2), (2, 3, 2, 3), (0, 1, 0, 1)]
HR = E.hand_rolled_riemann_of_g(MATTER_L, SLICE_L, bg_delta={},
                                components=comps, simp=cancel)
tick("  hand-rolled Riemann components computed; comparing to Totaro-g^{-1} ...")
agree = True
for (i, j, k, l) in comps:
    totaro_val = cancel(R_M[i][j][k][l])
    hand_val = cancel(HR[(i, j, k, l)])
    ok = (cancel(totaro_val - hand_val) == 0)
    agree = agree and ok
    tick(f"  R_{i}{j}{k}{l}: Totaro-g^-1 == hand-rolled (exact over Q): {ok}")
assert agree, "HAND-ROLLED Riemann DISAGREES with Totaro-g^{-1} -- hand-rolled is PRIMARY"
tick("  MANDATORY CROSS-CHECK PASS: Totaro-g^{-1} == hand-rolled Levi-Civita Riemann of "
     "g=eta+h on 3 components, EXACT over Q (Totaro applicability to eta+h VALIDATED)")

# --- 2.3 signature (1,3) of g at the Lorentzian M -----------------------------------
npos, nneg, nzero = E.eig_signature_count(g_M, simp=cancel)
tick(f"  signature of g=eta+h at the small-||M|| representative: "
     f"({npos},{nneg},{nzero}) [exact real_roots sign test; null-aligned frame => NOT Sylvester]")
assert (npos, nneg, nzero) == (1, 3, 0), \
    f"g signature {(npos,nneg,nzero)} != (1,3) -- left the small-||M|| Lorentzian regime"
tick("  signature (1,3) CONFIRMED (small-||M|| Lorentzian regime, 70.1 splice-consistency)")

# --- 2.4 PERTURBATIVE BOUNDARY (documented): the LARGE Task-1 cross-term M flips it ---
tick("Task 2.4: perturbative-boundary demo -- the LARGE Task-1 M (cross-term -13/315) "
     "leaves the Lorentzian regime ...")
SC_big = E.spacetime_curvature_of_g(MATTER_DELTA, SLICE_M, bg_delta=BG_DELTA, simp=cancel)
sig_big = E.eig_signature_count(SC_big["g"], simp=cancel)
tick(f"  large-M signature = {sig_big} (h dominates eta_bg => signature FLIPS; "
     f"this IS the documented perturbative boundary, NOT a failure)")
assert sig_big != (1, 3, 0), "large-M expected to flip signature (perturbative boundary)"

print("-" * 78)
print(f"TASK 2 OK -- spacetime_curvature_of_g built (B1; indices raised with g=eta+h, "
      f"C from the DIFFERENCE potential); R[g](M)={Rs_M} != 0; hand-rolled Levi-Civita "
      f"cross-check PASS exact over Q; signature (1,3) at small M; M=0 FLAT over a "
      f"neighbourhood; large-M flips signature (perturbative boundary).")
