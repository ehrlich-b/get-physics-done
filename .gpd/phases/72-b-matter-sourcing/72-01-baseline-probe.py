#!/usr/bin/env python3
"""Phase 72-01 reproduction probe (NOT a main()-registered engine gate).

Reproduces, EXACT over Q, the clean Task-1 results AND the first-result-gate
obstruction that stopped 72-01: the dim-4 cone-Hessian sub-slice is a metric cone
over H^3 (Ricci endomorphism eigenvalues {0,-1,-1,-1}), hence NOT Einstein in n=4,
so the contract's "M=0 center Einstein with R=-3" cannot hold for that metric.

Imports the warm engine (code/bulk_geometry_verification.py) as a module -- does NOT
run its main() (avoids the ~183s harness). Foreground `python3 -u`; prints progress.

Run: python3 -u .gpd/phases/72-b-matter-sourcing/72-01-baseline-probe.py
Expect: every assert passes; final line BASELINE_PROBE_OK; exit 0. The obstruction is
the EXPECTED outcome (eig {0,-1,-1,-1}), reported, not masked.
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


def curvature_tensors_at(delta, slice_pt_vals, simp=cancel):
    """(R_tensor, Ric, Rs, g_at, ginv, detg) of the off-center cone-Hessian slice
    metric at X_bg=I/3+delta evaluated at the rational slice point. EXACT over Q.
    Mirrors the engine _curvature_invariants_at but also exposes the tensors."""
    beta, gamma, p, q = symbols('beta gamma p q', real=True)
    coords = [beta, gamma, p, q]
    Phi = (-_log(E.inv_det_X)).subs(E._offcenter_subs(delta, slice_symbolic=True))
    g_sym = E.hessian_metric(Phi, coords)
    C_sym = E.cubic_form_C(Phi, coords)
    pt = {coords[i]: slice_pt_vals[i] for i in range(n)}
    g_at = g_sym.subs(pt).applyfunc(simp)
    C_at = [[[simp(C_sym[i][j][k].subs(pt)) for k in range(n)] for j in range(n)]
            for i in range(n)]
    detg = simp(g_at.det())
    ginv = g_at.inv().applyfunc(simp)
    Rt = E.totaro_riemann(ginv, C_at, n, simp=simp)
    Ric = Matrix(n, n, lambda j, l: simp(sum(
        ginv[i, k] * Rt[i][j][k][l] for i in range(n) for k in range(n))))
    Rs = simp(sum(ginv[j, l] * Ric[j, l] for j in range(n) for l in range(n)))
    return Rt, Ric, Rs, g_at, ginv, detg


def ricci_decomposition(Rt, g, ginv, n=4, simp=cancel):
    """n=4 GR Ricci decomposition: scalar + traceless-Ricci + Weyl, with the
    reconstruction residual. EXACT over Q. (Prototype for the engine routine.)"""
    Ric = Matrix(n, n, lambda j, l: simp(sum(
        ginv[i, k] * Rt[i][j][k][l] for i in range(n) for k in range(n))))
    Rs = simp(sum(ginv[j, l] * Ric[j, l] for j in range(n) for l in range(n)))
    S = Matrix(n, n, lambda a, b: simp(Ric[a, b] - Rs / n * g[a, b]))
    trace_S = simp(sum(ginv[a, b] * S[a, b] for a in range(n) for b in range(n)))
    coef = Rs / (n * (n - 1))
    Scal = [[[[simp(coef * (g[i, l] * g[j, k] - g[i, k] * g[j, l]))
               for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    Epart = [[[[simp(Rational(1, n - 2) * (S[i, l] * g[j, k] - S[j, l] * g[i, k]
                                           - S[i, k] * g[j, l] + S[j, k] * g[i, l]))
                for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    Weyl = [[[[simp(Rt[i][j][k][l] - Scal[i][j][k][l] - Epart[i][j][k][l])
               for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    resid_zero = all(
        simp(Rt[i][j][k][l] - (Scal[i][j][k][l] + Epart[i][j][k][l] + Weyl[i][j][k][l])) == 0
        for i in range(n) for j in range(n) for k in range(n) for l in range(n))
    return {"Ric": Ric, "Rs": Rs, "S": S, "trace_S": trace_S, "resid_zero": resid_zero}


CENTER = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]
R1 = E.ROUTE1_COMMON_SLICE_PT
BG_DELTA = {4: Rational(1, 4), 7: Rational(1, 5)}
MATTER_DELTA = {11: Rational(1, 3), 15: Rational(1, 6), 19: Rational(1, 3), 23: Rational(1, 7)}

print("=" * 78)
print("PHASE 72-01 baseline probe -- matter mechanism, regression, M=0 obstruction")
print("=" * 78)
tick("engine imported")

# --- Task 1: Peirce index map --------------------------------------------------
groups, diagonal = E.peirce_indices_under_E11()
assert sorted(groups[Rational(1)]) == [0]
assert sorted(groups[Rational(0)]) == list(range(1, 11))
assert sorted(groups[Rational(1, 2)]) == list(range(11, 27))
assert diagonal
tick("PEIRCE: V_1={0}, V_0={1..10}, V_1/2={11..26}, L_E11 diagonal -- CONFIRMED")

# --- Task 1: cross-term is the unique V_0<->V_1/2 octonion channel -------------
Xs = E.X_from_symbols(E.xs)
a, b, g, x1, x2, x3 = E._coord_from_octmat(Xs)
n1, n2, n3 = E._oct_normsq(x1), E._oct_normsq(x2), E._oct_normsq(x3)
cross = E.oct_mul(E.oct_mul(x2, x1), x3)
det_block_expr = a * b * g - a * n1 - b * n2 - g * n3
assert simplify(E.det_3(Xs) - det_block_expr - 2 * cross[0]) == 0
assert not (cross[0].free_symbols & {E.xs[0], E.xs[1], E.xs[2]})
tick("CROSS-TERM: det_3 - diag-norm == 2Re((x2 x1)x3); alpha,beta,gamma absent from triple -- CONFIRMED")

# --- Task 1: non-vacuity preflight ---------------------------------------------
full = {**BG_DELTA, **MATTER_DELTA}
sub = E._offcenter_subs(full, slice_symbolic=False, slice_vals=CENTER)
Xv = E.X_from_symbols([sub[E.xs[k]] for k in range(27)])
_, _, _, x1v, x2v, x3v = E._coord_from_octmat(Xv)
cross_M = simplify(2 * E.oct_mul(E.oct_mul(x2v, x1v), x3v)[0])
assert cross_M == Rational(-13, 315) and cross_M != 0
assert not E.oct_is_zero(x1v) and not E.oct_is_zero(x2v) and not E.oct_is_zero(x3v)
assert x1v[4] != 0 and x2v[4] != 0 and x3v[4] != 0
tick(f"NON-VACUITY: cross-term = {cross_M}, all 3 slots, e_4 content -- CONFIRMED")

# --- Task 1: Phase-71 matterless regression anchors ----------------------------
anchors = {
    "{4:1/3}": ({4: Rational(1, 3)}, Rational(-73041507, 21967969)),
    "{4:1/5,5:1/7}": ({4: Rational(1, 5), 5: Rational(1, 7)}, Rational(-521269105, 154700283)),
    "{4:2/5,6:1/3}": ({4: Rational(2, 5), 6: Rational(1, 3)}, Rational(-137053539, 48874081)),
    "{7:1/3,8:1/4,9:1/5}": ({7: Rational(1, 3), 8: Rational(1, 4), 9: Rational(1, 5)},
                            Rational(-114049215, 37982569)),
}
for lbl, (dlt, expect) in anchors.items():
    Rv, _, _, _, _ = E._curvature_invariants_at(dlt, R1, simp=cancel)
    assert Rv == expect, (lbl, Rv, expect)
    tick(f"REGRESSION R({lbl}) @ R1 = {Rv} -- matches 71-VERIFICATION")
Rc0, _, _, _, _ = E._curvature_invariants_at({}, CENTER, simp=cancel)
assert Rc0 == -3
tick("REGRESSION R(center) = -3 @ center slice -- matches anchor")

# --- FIRST-RESULT GATE: M=0 center Einstein? -----------------------------------
print("-" * 78)
tick("FIRST-RESULT GATE: is the M=0 center (cone-Hessian) Einstein?")
Rt_c, Ric_c, Rs_c, g_c, ginv_c, detg_c = curvature_tensors_at({}, CENTER, simp=cancel)
dec_c = ricci_decomposition(Rt_c, g_c, ginv_c, n=4, simp=cancel)
RicEndo = (ginv_c * Ric_c).applyfunc(cancel)
eig = RicEndo.eigenvals()
S_zero = all(dec_c["S"][i, j] == 0 for i in range(n) for j in range(n))
tick(f"  R(center) = {Rs_c} (expect -3); det_g = {detg_c}")
tick(f"  Ricci endomorphism g^-1 Ric eigenvalues = {dict(eig)}")
tick(f"  traceless Ricci S == 0 (Einstein)? {S_zero}")
tick(f"  decomposition reconstruction residual zero? {dec_c['resid_zero']}; trace(S) = {dec_c['trace_S']}")
# Sectional curvatures expose the cone-over-H^3 structure
for (i, j) in [(0, 1), (2, 3)]:
    vi = [0] * n; vi[i] = 1
    vj = [0] * n; vj[j] = 1
    K, _ = E.sectional_curvature(Rt_c, g_c, vi, vj, n, simp=cancel)
    tick(f"  K(e{i},e{j}) = {K}")
# Assertions: R=-3 holds, decomposition consistent, but NOT Einstein (the obstruction)
assert Rs_c == -3
assert dec_c["resid_zero"] and dec_c["trace_S"] == 0
assert eig == {Rational(-1): 3, Rational(0): 1}, dict(eig)
assert not S_zero, "UNEXPECTED: center came out Einstein -- re-examine the gate"
tick("OBSTRUCTION CONFIRMED: cone-Hessian center is a metric cone over H^3 "
     "(eig {0,-1,-1,-1}), R=-3 but NOT Einstein (S != 0).")

# Construction-(ii) g=eta+h at center is FLAT (the other half of the inconsistency)
MG = E.offcenter_slice_metric({}, slice_vals=CENTER)
assert MG["h"] == Matrix.zeros(4, 4)   # h=0 at center => g=eta_bg constant => R=0
tick("CROSS-CHECK: construction-(ii) g=eta+h at center has h=0 => g=eta (flat, R=0, Lambda=0) "
     "-- contradicts R=-3; the contract conjunction (R=-3 AND Einstein) holds for NEITHER metric.")

print("-" * 78)
print("BASELINE_PROBE_OK -- clean Task-1 results reproduced; first-result-gate "
      "obstruction (cone-over-H^3, NOT Einstein) confirmed exact over Q.")
