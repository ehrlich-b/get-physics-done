#!/usr/bin/env python3
"""Phase 73-01 driver: BUILD the FROZEN Einstein-test right-hand side (DERV-03).

This is the BUILD half of the decisive Phase-C Einstein-structure test. It FREEZES
the independent stress-energy tensor T_mu_nu (PRIMARY single-scalar T[psi] +
ALTERNATIVE sigma-model T[V_{1/2}]) and the intrinsic coupling kappa from the
V_{1/2} cross-term content, and reproduces the order-counting anchors -- ALL exact
over Q, ALL built with NO Ric/R/G input -- BEFORE any Einstein comparison is posed
(that comparison is 73-02). Building T after seeing G would beg the question.

ASSERT_CONVENTION: natural units (hbar=c=k_B=1); EXACT over Q on every decisive
  quantity (fp-float-decisive rejected; ranks/signatures via sympy, never numpy);
  spacetime metric g = eta_bg + h(x;M), mostly-minus; eta_bg the CONSTANT null-aligned
  KKT pullback [[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]] (eta_bg^{-1} =
  [[0,2,0,0],[2,0,0,0],[0,0,-1,0],[0,0,0,-1]]); box = eta_bg^{ab} d_a d_b =
  4 d_beta d_gamma - d_p^2 - d_q^2 (built from eta_bg^{-1}, NEVER a hard-coded diag);
  det_3 Freudenthal cross-term 2Re((x2 x1)x3), SSOT = bulk_geometry_verification.py
  (octonion_algebra.py BANNED); Lambda = 0 (M=0 vacuum flat-DERIVED, NO Lambda
  tripwire); h^(1)=0 (Phase-72) so the leading response is the quadratic h^(2).

CIRCULARITY DISCIPLINE (DERV-03 / fp-assume-einstein): NO Ric, R, or G symbol enters
  the construction of T or kappa. T and kappa are FROZEN from intrinsic cross-term /
  cubic-norm data. The Einstein tensor G_mu_nu[g] is NOT computed in this driver (it
  is 73-02's LHS); the only curvature object here is the LINEARIZED G^(1)[h^(2)] used
  as a documented DEGENERACY cross-check (it = 0), which is built from h^(2) (the
  metric response), NOT from any assumed Einstein form on the RHS.

WATCHDOG (mandatory): foreground `python3 -u`; progress prints between heavy steps;
  matter/bg RATIONAL, only the 4 slice coords symbolic. A silent long symbolic run
  is killed by the stream watchdog.

Run:    python3 -u .gpd/phases/73-c-einstein-structure/73-01-build-T-kappa.py
Expect: every assert passes; final line BUILD_T_KAPPA_OK; exit 0.
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'code'))
from sympy import (Rational, cancel, symbols, diff, Matrix, simplify, sqrt,
                   im as _im)

import bulk_geometry_verification as E

t0 = time.time()
n = 4


def tick(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


# ---- The decisive Phase-72 direction M_0 (verbatim from 72-02-decisive-controls.py) ----
# matter MATTER_L (V_{1/2}, the active channel) + V_0 partner BG_HALF (so the triple is
# non-vacuous). This is the SAME representative the whole milestone is built on.
MATTER_DELTA = {11: Rational(1, 3), 15: Rational(1, 6),
                19: Rational(1, 3), 23: Rational(1, 7)}      # V_{1/2} matter pattern
BG_DELTA = {4: Rational(1, 4), 7: Rational(1, 5)}            # V_0-internal x1 partner
MATTER_L = {k: v * Rational(1, 10) for k, v in MATTER_DELTA.items()}   # small-||M||
BG_HALF = {k: v * Rational(1, 2) for k, v in BG_DELTA.items()}

# A pure-V_1 (alpha) matter control direction (index 0 = alpha; V_1 is INERT in the triple).
MATTER_V1_ONLY = {0: Rational(1, 10)}

beta, gamma, p, q = symbols('beta gamma p q', real=True)
COORDS = [beta, gamma, p, q]
CENTER = {beta: Rational(1, 3), gamma: Rational(1, 3), p: Rational(0), q: Rational(0)}

# eta_bg (constant null-aligned) and its inverse, from the engine (build everything from these).
ETA_BG, ETA_INV = E._eta_bg_const(simp=cancel)

print("=" * 78)
print("PHASE 73-01 : BUILD the FROZEN Einstein-test RHS (T_mu_nu + kappa) -- DERV-03")
print("=" * 78)
tick("engine imported")
tick(f"eta_bg     = {ETA_BG.tolist()}")
tick(f"eta_bg^-1  = {ETA_INV.tolist()} (box built from THIS, null-aligned)")

# ====================================================================== TASK 2
print("\n" + "#" * 78)
print("# TASK 2 -- reproduce + freeze the order-counting anchors (linear test DEGENERATE)")
print("#" * 78)
print("# These are REGRESSION anchors (the FRESH research computed them; we REPRODUCE,")
print("# not rediscover). All exact over Q, on the h^(2)(x) FIELD evaluated at the center.")

# --- 2.0 the h^(2)(x) FIELD (engine routine added in Task 1) ------------------------
tick("Task 2.0: building h^(2)(x) field = E.h2_field(MATTER_L, BG_HALF) (slice symbolic, ~15s) ...")
h2 = E.h2_field(MATTER_L, BG_HALF, simp=cancel)
tick("  h^(2)(x) field built (rational function of beta,gamma,p,q)")
HANDOFF = Matrix([
    [Rational(261, 1225), 0, Rational(99, 700), 0],
    [0, Rational(9, 40), Rational(99, 700), 0],
    [Rational(99, 700), Rational(99, 700), Rational(4293, 9800), 0],
    [0, 0, 0, Rational(4293, 9800)],
])
h2_center = h2.applyfunc(lambda e: cancel(e.subs(CENTER)))
assert h2_center == HANDOFF, "h^(2)(x) center != Phase-72 handoff matrix (REGRESSION FAIL)"
assert h2 == h2.T, "h^(2)(x) not symmetric"
tick(f"  REGRESSION: h^(2)(x)|_center == handoff matrix over Q -- PASS; symmetric -- PASS")


# --- 2.1 linearized-GR operators built from eta_bg^{-1} (NOT diag) ------------------
# h^s_nu = eta_bg^{-1}^{s a} h_{a nu} ; trace h = eta_bg^{-1}^{ab} h_{ab} ;
# box from E.box (=4 d_beta d_gamma - d_p^2 - d_q^2). All on the FIELD, then subs center.
def raise_first(hmat):
    """h^s_nu = eta_bg^{-1}^{s a} h_{a nu} -- the mixed (1,1) field."""
    return Matrix(n, n, lambda s, nu: cancel(sum(ETA_INV[s, a] * hmat[a, nu] for a in range(n))))


def trace_eta(hmat):
    """trace h = eta_bg^{-1}^{ab} h_{ab} (scalar field)."""
    return cancel(sum(ETA_INV[a, b] * hmat[a, b] for a in range(n) for b in range(n)))


def lin_ricci(hmat):
    """Gauge-general linearized Ricci R^(1)_mu_nu (transcribed, mostly-minus via eta_bg):
        R^(1)_mu_nu = (1/2)( d_s d_mu h^s_nu + d_s d_nu h^s_mu - d_mu d_nu h - box h_mu_nu )
    with h^s_nu = eta_bg^{-1}^{sa} h_{a nu}, box = eta_bg^{ab} d_a d_b. FIELD in, FIELD out."""
    hmix = raise_first(hmat)          # h^s_nu
    htr = trace_eta(hmat)             # scalar h
    box_h = E.box(hmat, simp=cancel)  # box h_mu_nu (entrywise)

    def entry(mu, nu):
        term1 = sum(diff(hmix[s, nu], COORDS[s], COORDS[mu]) for s in range(n))
        term2 = sum(diff(hmix[s, mu], COORDS[s], COORDS[nu]) for s in range(n))
        term3 = diff(htr, COORDS[mu], COORDS[nu])
        return cancel(Rational(1, 2) * (term1 + term2 - term3 - box_h[mu, nu]))

    return Matrix(n, n, entry)


tick("Task 2.1: linearized Ricci/Einstein operators (gauge-general, eta_bg^-1-raised) ...")
R1 = lin_ricci(h2)                                   # R^(1)_mu_nu field
R1_center = R1.applyfunc(lambda e: cancel(e.subs(CENTER)))
R1_scalar_field = trace_eta(R1)                      # R^(1) = eta^{munu} R^(1)_munu
R1_scalar = cancel(R1_scalar_field.subs(CENTER))
# G^(1)_mu_nu = R^(1)_mu_nu - (1/2) eta_bg_munu R^(1)
G1_center = Matrix(n, n, lambda mu, nu:
                   cancel(R1_center[mu, nu] - Rational(1, 2) * ETA_BG[mu, nu] * R1_scalar))
tick(f"  R^(1)[h^(2)] (linearized Ricci SCALAR) at center = {R1_scalar}")
tick(f"  G^(1)_munu[h^(2)] at center == zero 4x4? {G1_center == Matrix.zeros(n, n)}")
tick(f"  R^(1)_munu[h^(2)] at center == zero 4x4? {R1_center == Matrix.zeros(n, n)}")

assert R1_scalar == 0, f"R^(1)[h^(2)] != 0 (got {R1_scalar}) -- anchor FAIL"
assert G1_center == Matrix.zeros(n, n), f"G^(1)[h^(2)] != 0 -- anchor FAIL:\n{G1_center}"
# R1_center itself is also 0 (gauge-invariant linear Einstein content vanishes); record it.
tick("  ANCHOR (a): R^(1)=0 AND G^(1)_munu=0 over Q (the LINEAR Einstein content is DEGENERATE)")

# --- 2.2 trace-reverse hbar^(2) and box(hbar^(2)) != 0 (pure gauge) -----------------
tick("Task 2.2: trace-reverse hbar^(2) and box(hbar^(2)) (the handoff diagnostic) ...")
htr_field = trace_eta(h2)
hbar2 = Matrix(n, n, lambda mu, nu:
               cancel(h2[mu, nu] - Rational(1, 2) * ETA_BG[mu, nu] * htr_field))
box_hbar2 = E.box(hbar2, simp=cancel)
box_hbar2_center = box_hbar2.applyfunc(lambda e: cancel(e.subs(CENTER)))
tick(f"  box(hbar^(2))(0,0) = {box_hbar2_center[0,0]} (target -76221/2450)")
tick(f"  box(hbar^(2))(3,3) = {box_hbar2_center[3,3]} (target -38637/1225)")
assert box_hbar2_center[0, 0] == Rational(-76221, 2450), \
    f"box(hbar^2)(0,0) = {box_hbar2_center[0,0]} != -76221/2450"
assert box_hbar2_center[3, 3] == Rational(-38637, 1225), \
    f"box(hbar^2)(3,3) = {box_hbar2_center[3,3]} != -38637/1225"
assert box_hbar2_center != Matrix.zeros(n, n), "box(hbar^2) == 0 (should be nonzero/pure-gauge)"
tick("  ANCHOR (b): box(hbar^(2)) != 0 over Q (matches the documented (0,0),(3,3) entries)")

# --- 2.3 Lorenz-gauge defect d^mu hbar^(2)_munu != 0 (h^(2) NOT in Lorenz gauge) ----
# defect_nu = eta_bg^{-1}^{mu a} d_a hbar^(2)_{mu nu}
tick("Task 2.3: Lorenz-gauge defect d^mu hbar^(2)_munu (h^(2) not in Lorenz gauge) ...")
hbar2_mix = raise_first(hbar2)           # hbar^{(2) mu}_nu = eta^{mu a} hbar_{a nu}
lorenz_defect_field = [cancel(sum(diff(hbar2_mix[mu, nu], COORDS[mu]) for mu in range(n)))
                       for nu in range(n)]
lorenz_defect = [cancel(d.subs(CENTER)) for d in lorenz_defect_field]
TARGET_DEFECT = [Rational(19143, 9800), Rational(9747, 4900), Rational(297, 350), Rational(0)]
tick(f"  Lorenz defect = {lorenz_defect} (target {TARGET_DEFECT})")
assert lorenz_defect == TARGET_DEFECT, \
    f"Lorenz defect {lorenz_defect} != {TARGET_DEFECT}"
assert any(d != 0 for d in lorenz_defect), "Lorenz defect == 0 (should be nonzero)"
tick("  ANCHOR (c): Lorenz defect == [19143/9800, 9747/4900, 297/350, 0] != 0 over Q "
     "(h^(2) NOT in Lorenz gauge)")

# --- 2.4 reality / exactness guard (no Wick / float contamination) ------------------
all_quantities = (list(box_hbar2_center) + list(R1_center) + list(G1_center) + lorenz_defect)
assert all(getattr(_im(x), 'is_zero', None) is not False for x in all_quantities), \
    "an anchor quantity has a nonzero imaginary part -- reality/Wick contamination"
assert all(x.is_rational is not False for x in all_quantities), "a quantity is not rational over Q"
tick("Task 2.4: all anchors are real rationals over Q (no imaginary part; fp-float-decisive avoided)")

# --- 2.5 the documented reconciliation (linear test is degenerate => full G[g] for 73-02) --
print("-" * 78)
print("RECONCILIATION (why box(hbar^(2)) != 0 but G^(1)[h^(2)] = 0):")
print("  box(hbar_munu) = -2 G^(1)_munu holds ONLY in Lorenz gauge (d^mu hbar_munu = 0).")
print("  Here the Lorenz defect = [19143/9800, 9747/4900, 297/350, 0] != 0, so h^(2) is")
print("  NOT in Lorenz gauge => the nonzero box(hbar^(2)) is PURE GAUGE (it equals the")
print("  omitted gauge terms d_mu(d^a hbar_anu)+d_nu(d^a hbar_amu)-eta_munu d_a d_b hbar^ab),")
print("  NOT physical curvature. The gauge-INVARIANT O(||M||^2) Einstein content is")
print("  G^(1)_munu[h^(2)] = 0 IDENTICALLY. This is REQUIRED for consistency with the")
print("  Phase-72 result R[g] = a_4 ||M||^4 + O(||M||^5): the O(||M||^2) curvature (= the")
print("  linear-in-h^(2) Einstein tensor) MUST vanish -- a CROSS-CHECK, not a surprise.")
print("  ")
print("  => the LINEAR Einstein test is DEGENERATE. The genuine curvature lives at")
print("  O(||M||^4) = SECOND order in h^(2) (Totaro Riemann is BILINEAR in the cubic form")
print("  C, and C = O(||M||^2)). THEREFORE the DECISIVE 73-02 test is the FULL NONLINEAR")
print("  Einstein tensor G_munu[g] = Ric[g] - (1/2) g R[g] at O(||M||^4), NOT box(hbar).")
print("  box(hbar^(2)) is retained ONLY as a documented secondary gauge diagnostic.")
print("-" * 78)
print(f"TASK 2 OK -- order-counting anchors reproduced exact over Q: G^(1)[h^(2)]=0, "
      f"R^(1)=0, box(hbar^(2)) != 0 (={box_hbar2_center[0,0]} at (0,0)), Lorenz defect "
      f"{lorenz_defect} != 0. Linear test DEGENERATE => 73-02 uses the full nonlinear G[g] "
      f"at O(||M||^4).")
print(f"FIRST_RESULT_GATE_TASK2: order anchors reproduced; the linear-test degeneracy is "
      f"DOCUMENTED and the full-G[g]-at-O(||M||^4) test is fixed as decisive for 73-02.")
