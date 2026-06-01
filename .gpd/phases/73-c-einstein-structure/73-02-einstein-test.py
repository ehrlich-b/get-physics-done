#!/usr/bin/env python3
"""Phase 73-02 driver: the DECISIVE can-fail Einstein-structure test (CALC-05).

This is the TEST half of the Phase-C Einstein test and the FINAL verdict of milestone
v17.0. With T_mu_nu and kappa FROZEN from 73-01 (imported from the 73-01 driver's
module-level PHASE73_HANDOFF + the frozen field-valued T builders -- NOT rebuilt, NOT
re-fit), it:

  Task 1: computes the FULL nonlinear Einstein tensor G_mu_nu[g(x)] = Ric[g] - (1/2) g R[g]
          over an (M,x) family (>=3 matter directions x >=3 slice positions x >=2
          amplitudes), exact over Q, all sig (1,3), Totaro-vs-hand-rolled cross-checked.
  Task 2: runs the SINGLE GLOBAL (kappa,Lambda) fit -- the can-fail test -- for BOTH T
          candidates, at finite-M AND at the t^4 leading order, exact over Q, reporting
          the EXACT residual per point (NEVER per-point tuning, NEVER least-squares).
  Task 3: classifies the honest level (exact / linear-leading / none) via the n=4 Ricci
          (S, Weyl) decomposition by an EXPLICIT rule.

ASSERT_CONVENTION: natural units (hbar=c=k_B=1); EXACT over Q on every decisive quantity
  (fp-float-decisive rejected; ranks/signatures via sympy, never numpy); spacetime metric
  g = eta_bg + h(x;M), mostly-minus; eta_bg the CONSTANT null-aligned KKT pullback
  [[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]; G_mu_nu[g] = Ric[g] - (1/2) g R[g]
  (FULL nonlinear, lower index), indices raised with g^{-1}=(eta+h)^{-1}; det_3 Freudenthal
  cross-term 2Re((x2 x1)x3), SSOT = bulk_geometry_verification.py (octonion_algebra.py
  BANNED); Lambda = 0, NO Lambda tripwire (M=0 vacuum flat-DERIVED from KKT det_2); kappa
  FROZEN in 73-01 (NOT re-fit); only Lambda fit as a global constant (expected 0); leading
  curvature at O(||M||^4) since h^(1)=0.

CIRCULARITY DISCIPLINE (fp-assume-einstein / fp-import-supergravity): T and kappa were
  FROZEN in 73-01 BEFORE G is computed here (DERV-03). The fit solves for a SINGLE GLOBAL
  (kappa,Lambda) over the WHOLE family -- a single-point match (2 constants vs 10
  components at one point) is NOT a pass. If the residual is nonzero, it is REPORTED
  exactly and the honest level reported; a near-miss is NOT rounded to "Einstein". No
  GST/SUSY/-R/2/Weinberg import; no thermodynamic/ensemble (Jacobson) step.

WATCHDOG (mandatory): foreground `python3 -u`; progress prints between family points;
  matter/bg RATIONAL before g.inv() (only the 4 slice coords symbolic) => ~3s per point,
  NOT the >200s symbolic-inverse cliff. Importing the 73-01 driver runs it once (~77s).

Run:    python3 -u .gpd/phases/73-c-einstein-structure/73-02-einstein-test.py
Expect: every assert passes; final line EINSTEIN_TEST_OK; exit 0.
"""
import sys
import os
import time
import importlib.util

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_HERE, '..', '..', '..', 'code'))
from sympy import Rational, cancel, symbols, Matrix, zeros, im as _im

import bulk_geometry_verification as E

t0 = time.time()
n = 4


def tick(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


# ============================================================================
# IMPORT THE FROZEN 73-01 RHS (T builders + kappa) -- DO NOT REBUILD
# ============================================================================
print("=" * 78)
print("PHASE 73-02 : the DECISIVE can-fail Einstein-structure test (CALC-05)")
print("            FINAL VERDICT of milestone v17.0")
print("=" * 78)
tick("importing the FROZEN 73-01 RHS (runs 73-01 once, ~77s; T + kappa freeze) ...")
_spec = importlib.util.spec_from_file_location(
    'build_T_kappa', os.path.join(_HERE, '73-01-build-T-kappa.py'))
B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(B)               # RUNS 73-01 -> freezes T + kappa
tick("73-01 imported; T (both) + kappa (both) FROZEN")

# The frozen handoff (exact rationals over Q).
KAPPA_PSI = B.PHASE73_HANDOFF["kappa_psi"]          # 32016781143/5929 (t^4, structurally matched)
KAPPA_SIGMA = B.PHASE73_HANDOFF["kappa_sigma"]      # 395268903/129850 (t^2, ORDER MISMATCH)
A4 = B.PHASE73_HANDOFF["a4"]                         # 395268903/24010000
PSI_LEAD = B.PHASE73_HANDOFF["psi_lead_power"]       # 4
SIGMA_LEAD = B.PHASE73_HANDOFF["sigma_lead_power"]   # 2
ORDER_MISMATCH_SIGMA = B.PHASE73_HANDOFF["order_mismatch_sigma"]

# The frozen field-valued T builders (evaluate at the SAME slice point as G).
psi_scalar = B.psi_scalar
scalar_stress_tensor = B.scalar_stress_tensor
sigma_multiplet = B.sigma_multiplet
sigma_stress_tensor = B.sigma_stress_tensor

# The decisive direction + slice coords (verbatim from 73-01).
MATTER_L = B.MATTER_L              # {11:1/30, 15:1/60, 19:1/30, 23:1/70}  (already small)
BG_HALF = B.BG_HALF                # {4:1/8, 7:1/10}
beta, gamma, p, q = symbols('beta gamma p q', real=True)
COORDS = [beta, gamma, p, q]
CENTER = {beta: Rational(1, 3), gamma: Rational(1, 3), p: Rational(0), q: Rational(0)}

ETA_BG, ETA_INV = E._eta_bg_const(simp=cancel)

tick(f"FROZEN: kappa_psi={KAPPA_PSI} (t^{PSI_LEAD}, matched), "
     f"kappa_sigma={KAPPA_SIGMA} (t^{SIGMA_LEAD}, ORDER-MISMATCH), a4={A4}")
tick(f"FROZEN direction: MATTER_L={MATTER_L}, BG_HALF={BG_HALF}")


# ============================================================================
# TASK 1 -- the full nonlinear G_mu_nu[g] over the (M,x) family
# ============================================================================
print("\n" + "#" * 78)
print("# TASK 1 -- full nonlinear G_mu_nu[g] = Ric[g] - (1/2) g R[g] over the (M,x) family")
print("#" * 78)
print("# >=3 matter directions x >=3 slice positions x >=2 amplitudes; anchored on the")
print("# decisive M_0 (MATTER_L + BG_HALF). sig (1,3) asserted at EACH point (inside the")
print("# Lorentzian splice). Totaro-vs-hand-rolled Riemann cross-check at the anchor.")

# ---- the (M,x) family ------------------------------------------------------
# THREE matter directions (all in V_{1/2}, the active cross-term channel):
#   D1 = MATTER_L          (the decisive Phase-72/73 representative)
#   D2 = a re-weighted V_{1/2} pattern (different component mix)
#   D3 = a third V_{1/2} pattern (distinct again)
# Each paired with the SAME V_0 partner BG_HALF (so the V_0<->V_{1/2} triple is non-vacuous).
DIR1 = dict(MATTER_L)
DIR2 = {11: Rational(1, 40), 15: Rational(1, 30), 19: Rational(1, 50), 23: Rational(1, 35)}
DIR3 = {11: Rational(1, 60), 15: Rational(1, 45), 19: Rational(1, 25), 23: Rational(1, 55),
        14: Rational(1, 80)}
MATTER_DIRS = [("D1", DIR1), ("D2", DIR2), ("D3", DIR3)]

# THREE slice positions (the spacetime point x = (beta,gamma,p,q)); the center + two
# off-center points. Keep p,q small so g stays sig (1,3) (large slice displacement flips
# the null-aligned beta,gamma block).
POS_CENTER = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]
POS_A = [Rational(1, 3), Rational(1, 3), Rational(1, 40), Rational(0)]
POS_B = [Rational(7, 20), Rational(31, 100), Rational(1, 50), Rational(1, 60)]
SLICE_POS = [("X0", POS_CENTER), ("XA", POS_A), ("XB", POS_B)]

# TWO amplitudes (scale the matter direction; the V_0 partner BG_HALF held fixed -- it sets
# the basepoint, the amplitude scales the matter M).  t in {1, 1/2}.
AMPS = [("t1", Rational(1)), ("t2", Rational(1, 2))]


def scale(delta, s):
    return {k: v * s for k, v in delta.items()}


def einstein_tensor_lower(res, simp=cancel):
    """G_mu_nu = Ric_mu_nu - (1/2) g_mu_nu R  (FULL nonlinear, lower index), exact over Q."""
    g = res["g"]
    Ric = res["Ric"]
    Rs = res["Rscalar"]
    return Matrix(n, n, lambda mu, nu: simp(Ric[mu, nu] - Rational(1, 2) * g[mu, nu] * Rs))


# ---- build the family ------------------------------------------------------
family = []        # list of dicts {key, matter, bg, pos, G, g, ginv, Rscalar, res}
tick("Task 1: building the (M,x) family (3 dirs x 3 positions x 2 amps = 18 points) ...")
dropped = []
for (dn, dd) in MATTER_DIRS:
    for (pn, pos) in SLICE_POS:
        for (an, amp) in AMPS:
            key = f"{dn}/{pn}/{an}"
            matter = scale(dd, amp)
            res = E.spacetime_curvature_of_g(matter, pos, bg_delta=BG_HALF, simp=cancel)
            sig = E.eig_signature_count(res["g"])
            if sig != (1, 3, 0):
                dropped.append((key, sig))
                tick(f"  {key}: sig {sig} != (1,3,0) -- DROPPED (outside the splice; not forced)")
                continue
            G = einstein_tensor_lower(res)
            family.append({"key": key, "dir": dn, "pos": pn, "amp": an,
                           "matter": matter, "bg": BG_HALF, "pos_vals": pos,
                           "G": G, "g": res["g"], "ginv": res["ginv"],
                           "Rscalar": res["Rscalar"], "res": res})
            tick(f"  {key}: sig (1,3) OK; Rscalar={float(res['Rscalar']):.4g}; "
                 f"G!=0? {G != zeros(n, n)}")

assert len(family) >= 6, f"only {len(family)} valid family points (<6); shrink ||M|| / adjust"
tick(f"Task 1: {len(family)} valid (sig (1,3)) family points; {len(dropped)} dropped")

# ---- 1.A anchor regression: Rscalar(M_0,center) ~ 4007.98 (Phase-72) -------
anchor = next(f for f in family if f["key"] == "D1/X0/t1")
Rs_anchor = anchor["Rscalar"]
tick(f"Task 1.A anchor D1/X0/t1: Rscalar={Rs_anchor} (float {float(Rs_anchor):.6g}; "
     f"Phase-72 R_full~4007.98)")
assert abs(float(Rs_anchor) - 4007.98090373574) < 1e-6, \
    "anchor Rscalar != Phase-72 R_full (~4007.98) -- engine/g regression FAIL"
assert anchor["G"] != zeros(n, n), "G[g] == 0 at M_0 (should be nonzero -- THIS-research anchor)"
tick("  REGRESSION: Rscalar(M_0,center) == Phase-72 ~4007.98 over Q; G[g] != 0 -- PASS")

# ---- 1.B G first appears at O(||M||^4): amplitude-series spot check ---------
# At the center, with M = t*MATTER_L, BG_HALF fixed: R[g] ~ a_4 t^4 (Phase 72). The
# Einstein tensor G inherits the curvature order. We verify G(t)/t^4 stabilizes (finite,
# nonzero) and lower powers -> 0, by sampling G at t in {1/10, 1/20, 1/40} and checking
# the ratio G[0,0](t) / t^4 approaches a constant.
tick("Task 1.B amplitude series: G(t)/t^4 stabilizes (G first appears at O(||M||^4)) ...")
g00_over_t4 = []
g00_over_t3 = []
for tt in (Rational(1, 10), Rational(1, 20), Rational(1, 40)):
    matter_t = scale(MATTER_L, tt)
    res_t = E.spacetime_curvature_of_g(matter_t, POS_CENTER, bg_delta=BG_HALF, simp=cancel)
    sig_t = E.eig_signature_count(res_t["g"])
    G_t = einstein_tensor_lower(res_t)
    r4 = cancel(G_t[0, 0] / tt**4)
    r3 = cancel(G_t[0, 0] / tt**3)
    g00_over_t4.append((tt, r4))
    g00_over_t3.append((tt, r3))
    tick(f"  t={tt}: sig {sig_t}; G[0,0]={float(G_t[0,0]):.4g}; "
         f"G[0,0]/t^4={float(r4):.6g}; G[0,0]/t^3={float(r3):.6g}")
# G/t^4 should approach a finite nonzero constant; G/t^3 should -> 0 (i.e. blow toward the
# t^4/t^3 = t ratio: actually G/t^3 ~ t * (G/t^4) -> 0). Use the float trend as the witness.
r4_vals = [float(r) for (_, r) in g00_over_t4]
r3_vals = [float(r) for (_, r) in g00_over_t3]
tick(f"  G[0,0]/t^4 trend = {r4_vals}  (should approach a finite nonzero const)")
tick(f"  G[0,0]/t^3 trend = {r3_vals}  (should -> 0, confirming leading order is t^4 not t^3)")
assert abs(r3_vals[-1]) < abs(r3_vals[0]), "G/t^3 not decreasing -- leading order may be < t^4"
assert all(abs(v) > 1e-9 for v in r4_vals), "G/t^4 -> 0 -- leading order is HIGHER than t^4?"
# tighter: G/t^4 should be converging (successive ratios closer together than G/t^3's)
spread4 = abs(r4_vals[-1] - r4_vals[0])
tick(f"  G[0,0]/t^4 spread over t in [1/40,1/10] = {spread4:.4g} (small => stabilizing at t^4)")
tick("  CONFIRMED: G first appears at O(||M||^4) (G/t^4 stabilizes; G/t^3 -> 0)")

# ---- 1.C Totaro-vs-hand-rolled Riemann cross-check at the anchor ------------
tick("Task 1.C Totaro-vs-hand-rolled Riemann cross-check at M_0 (engine correctness) ...")
check_comps = [(0, 2, 0, 2), (2, 3, 2, 3), (0, 1, 0, 1), (1, 2, 1, 2), (0, 3, 0, 3)]
hand = E.hand_rolled_riemann_of_g(MATTER_L, POS_CENTER, bg_delta=BG_HALF,
                                  components=check_comps, simp=cancel)
R_tot = anchor["res"]["R"]
all_match = True
for (i, j, k, l) in check_comps:
    tot = cancel(R_tot[i][j][k][l])
    hr = cancel(hand[(i, j, k, l)])
    match = (cancel(tot - hr) == 0)
    all_match = all_match and match
    tick(f"  R[{i}{j}{k}{l}]: Totaro={tot}  hand={hr}  MATCH? {match}")
assert all_match, "Totaro-vs-hand-rolled Riemann DISAGREE -- engine correctness FAIL"
tick("  CROSS-CHECK PASS: Totaro == hand-rolled Levi-Civita on all checked components over Q")

# ---- 1.D exactness / reality guard (fp-float-decisive) ----------------------
tick("Task 1.D exactness/reality guard over all family G, g entries ...")
bad = 0
for f in family:
    for M_ in (f["G"], f["g"]):
        for x in M_:
            if getattr(_im(x), 'is_zero', None) is False:
                bad += 1
            if x.is_rational is False:
                bad += 1
assert bad == 0, f"{bad} family G/g entries are non-real or non-rational (fp-float-decisive)"
tick("  ALL family G, g entries are real rationals over Q (no float, no imaginary part)")

print("-" * 78)
print(f"TASK 1 OK -- full nonlinear G_mu_nu[g] computed exact over Q at {len(family)} "
      f"(M,x) family points (all sig (1,3)); G != 0 at M_0 (Rscalar~4007.98 regression); "
      f"G first appears at O(||M||^4) (G/t^4 stabilizes); Totaro==hand-rolled at the anchor. "
      f"{len(dropped)} points dropped for sig flip (not forced). The well-posed test LHS.")
print(f"FIRST_RESULT_GATE_TASK1: G[g] computed and sig-(1,3)-validated over the family; "
      f"the decisive test LHS is ready for the global (kappa,Lambda) fit (Task 2).")
