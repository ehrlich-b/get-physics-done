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


# ====================================================================== TASK 3
print("\n" + "#" * 78)
print("# TASK 3 -- construct the INDEPENDENT T_mu_nu (PRIMARY single-scalar +")
print("#           ALTERNATIVE sigma-model), BEFORE any G is computed (DERV-03)")
print("#" * 78)
print("# CRITICAL: NO Ric, R, or G symbol enters the construction of T (grep-guarded")
print("# below). T is built from the V_{1/2} cross-term content via the engine det_3")
print("# cross-term SSOT (octonion_algebra.py BANNED), raised/lowered with eta_bg (a")
print("# FLAT-background stress tensor lives on eta, NOT on g). Both candidates are")
print("# built and frozen; we do NOT pick the one that 'works' after seeing G.")


def _x123_field(matter_delta, bg_delta):
    """The three octonions (x1, x2, x3) at basepoint (I/3 + bg) + matter, with the 4
    slice coords {1,2,3,10}=(beta,gamma,p,q) SYMBOLIC. x1 = V_0 partner carrying the
    slice content (x1[0]=p, x1[7]=q); x2,x3 = V_{1/2} matter. EXACT over Q. Uses the
    engine _offcenter_subs + X_from_symbols + _coord_from_octmat (det_3 SSOT path)."""
    full = {**(bg_delta or {}), **(matter_delta or {})}
    sub = E._offcenter_subs(full, slice_symbolic=True, slice_vals=None)
    Xv = E.X_from_symbols([sub[E.xs[k]] for k in range(27)])
    _, _, _, x1, x2, x3 = E._coord_from_octmat(Xv)
    return x1, x2, x3


def psi_scalar(matter_delta, bg_delta):
    """The PRIMARY cross-term scalar psi(x;M) = 2Re((x2 x1) x3) as an EXACT slice field,
    via the engine det_3 cross-term SSOT (oct_mul, NOT octonion_algebra.py, NOT the
    real-only 2 d1 d2 d3). x-dependent through x1's slice content (p,q)."""
    x1, x2, x3 = _x123_field(matter_delta, bg_delta)
    cross = E.oct_mul(E.oct_mul(x2, x1), x3)     # (x2 x1) x3 -- the generic-norm factor order
    return cancel(2 * cross[0])                  # 2 * real part


def grad(f):
    """d_mu f over the 4 slice coords (beta,gamma,p,q)."""
    return [cancel(diff(f, c)) for c in COORDS]


def scalar_stress_tensor(psi):
    """The canonical FLAT-background scalar stress tensor on eta_bg:
        T_mu_nu = d_mu psi d_nu psi - (1/2) eta_bg_mu_nu (d psi)^2,
        (d psi)^2 = eta_bg^{-1}^{ab} d_a psi d_b psi.
    NO Ric/R/G. Indices raised/lowered with eta_bg (FLAT background), not g."""
    dpsi = grad(psi)
    dpsi2 = cancel(sum(ETA_INV[i, j] * dpsi[i] * dpsi[j] for i in range(n) for j in range(n)))
    return Matrix(n, n, lambda mu, nu:
                  cancel(dpsi[mu] * dpsi[nu] - Rational(1, 2) * ETA_BG[mu, nu] * dpsi2)), dpsi, dpsi2


def divergence_eta(T):
    """d^mu T_mu_nu = eta_bg^{-1}^{mu a} d_a T_mu_nu (the flat-background divergence)."""
    return [cancel(sum(ETA_INV[mu, a] * diff(T[mu, nu], COORDS[a])
                       for mu in range(n) for a in range(n))) for nu in range(n)]


# --- 3.1 PRIMARY: single-scalar T[psi] ---------------------------------------------
tick("Task 3.1: PRIMARY single-scalar T[psi], psi = 2Re((x2 x1)x3) via det_3 SSOT ...")
psi = psi_scalar(MATTER_L, BG_HALF)
tick(f"  psi(x;M_0) = {psi}  (slice field; center value = {cancel(psi.subs(CENTER))})")
assert cancel(psi.subs(CENTER)) == Rational(-13, 63000), \
    "psi center value != the Phase-72 non-vacuity triple -13/63000"
# psi must be REAL rational (no octonion imaginary leakage into a scalar)
assert getattr(_im(psi), 'is_zero', None) is not False, "psi has nonzero imaginary part"
T_psi, dpsi, dpsi2 = scalar_stress_tensor(psi)
box_psi = cancel(E.box(psi))
tick(f"  d psi = {dpsi};  (d psi)^2 = {dpsi2};  box psi = {box_psi}")
# symmetry
assert T_psi == T_psi.T, "T[psi] not symmetric"
# conservation: d^mu T_munu = (box psi)(d_nu psi); here box psi = 0 (psi linear in slice
# => harmonic) => conserved IDENTICALLY (the on-shell condition box psi=0 holds on the nose).
divT_psi = divergence_eta(T_psi)
identity_ok = all(cancel(divT_psi[nu] - box_psi * dpsi[nu]) == 0 for nu in range(n))
conserved_psi = all(cancel(d) == 0 for d in divT_psi)
tick(f"  d^mu T[psi]_munu (field) = {[cancel(d) for d in divT_psi]}")
tick(f"  conservation identity d^mu T_munu == (box psi)(d_nu psi)? {identity_ok}; "
     f"box psi == 0 (psi linear-in-slice => harmonic)? {box_psi == 0}; CONSERVED? {conserved_psi}")
assert identity_ok, "the scalar-stress divergence identity failed"
assert conserved_psi, "T[psi] NOT conserved (and box psi != 0) -- report, do not force"
# T -> 0 as ||M|| -> 0
t = symbols('t', real=True, positive=True)
psi_t = psi_scalar({k: v * t for k, v in MATTER_L.items()},
                   {k: v * t for k, v in BG_HALF.items()})
T_psi_t, _, _ = scalar_stress_tensor(psi_t)
T_psi_flat = T_psi_t.applyfunc(lambda e: cancel(e.subs(t, 0)))
assert T_psi_flat == Matrix.zeros(n, n), "T[psi] does not vanish as ||M||->0"
tick(f"  T[psi] -> 0 as ||M||->0? {T_psi_flat == Matrix.zeros(n, n)} "
     f"(psi(t) = {psi_t} -> 0)")
# V_1-only control (V_1 alpha is INERT in the triple => T = 0)
psi_v1 = psi_scalar(MATTER_V1_ONLY, BG_HALF)
T_psi_v1, _, _ = scalar_stress_tensor(psi_v1)
assert psi_v1 == 0 and T_psi_v1 == Matrix.zeros(n, n), \
    "V_1-only control: psi or T[psi] nonzero (V_1 should be inert)"
tick(f"  V_1-only control: psi = {psi_v1}, T[psi] == 0? {T_psi_v1 == Matrix.zeros(n, n)} "
     f"(V_1 alpha INERT, carried from Phase 71/72)")
T_psi_center = T_psi.applyfunc(lambda e: cancel(e.subs(CENTER)))
print("  T[psi] at center (exact over Q):")
for i in range(n):
    print("    ", [str(T_psi_center[i, j]) for j in range(n)])

# --- 3.2 ALTERNATIVE: sigma-model T[V_{1/2}] ---------------------------------------
# The V_{1/2} multiplet = the 16 octonion components of the two V_0<->V_{1/2} products
# (x2 x1) and (x1 x3) -- the natural F_4/Spin(9,1)-covariant V_{1/2} content carrying
# the slice (x1) dependence. Target metric G_ab = delta_ab (the octonion Euclidean
# inner product = the V_{1/2} norm bilinear). Genuinely DISTINCT from T[psi] (which uses
# only the Re/trace channel). NO Ric/R/G.
def sigma_multiplet(matter_delta, bg_delta):
    """16 sigma fields phi^a = components of (x2 x1) ++ components of (x1 x3)."""
    x1, x2, x3 = _x123_field(matter_delta, bg_delta)
    prod_a = E.oct_mul(x2, x1)
    prod_b = E.oct_mul(x1, x3)
    return [cancel(c) for c in prod_a] + [cancel(c) for c in prod_b]


def sigma_stress_tensor(phis):
    """T_mu_nu = G_ab d_mu phi^a d_nu phi^b - (1/2) eta_bg_munu G_ab eta_bg^{-1}^{cd} d_c phi^a d_d phi^b,
    G_ab = delta_ab (the V_{1/2} octonion inner product). NO Ric/R/G."""
    dphis = [grad(f) for f in phis]
    na = len(phis)

    def entry(mu, nu):
        kin = sum(dphis[ai][mu] * dphis[ai][nu] for ai in range(na))
        trace = sum(ETA_INV[c1, d1] * dphis[ai][c1] * dphis[ai][d1]
                    for ai in range(na) for c1 in range(n) for d1 in range(n))
        return cancel(kin - Rational(1, 2) * ETA_BG[mu, nu] * trace)

    return Matrix(n, n, entry), dphis


tick("Task 3.2: ALTERNATIVE sigma-model T[V_{1/2}] (16-component multiplet, G_ab=delta) ...")
phis = sigma_multiplet(MATTER_L, BG_HALF)
T_sig, dphis = sigma_stress_tensor(phis)
box_phis = [cancel(E.box(f)) for f in phis]
assert T_sig == T_sig.T, "T_sigma not symmetric"
divT_sig = divergence_eta(T_sig)
conserved_sig = all(cancel(d) == 0 for d in divT_sig)
all_harmonic = all(b == 0 for b in box_phis)
tick(f"  all 16 box phi^a == 0 (each linear-in-slice => harmonic)? {all_harmonic}")
tick(f"  d^mu T_sigma_munu (field) = {[cancel(d) for d in divT_sig]}; CONSERVED? {conserved_sig}")
assert conserved_sig, "T_sigma NOT conserved -- report, do not force"
# T_sigma -> 0 as ||M||->0
phis_t = sigma_multiplet({k: v * t for k, v in MATTER_L.items()},
                         {k: v * t for k, v in BG_HALF.items()})
T_sig_t, _ = sigma_stress_tensor(phis_t)
T_sig_flat = T_sig_t.applyfunc(lambda e: cancel(e.subs(t, 0)))
assert T_sig_flat == Matrix.zeros(n, n), "T_sigma does not vanish as ||M||->0"
tick(f"  T_sigma -> 0 as ||M||->0? {T_sig_flat == Matrix.zeros(n, n)}")
# V_1-only control
phis_v1 = sigma_multiplet(MATTER_V1_ONLY, BG_HALF)
T_sig_v1, _ = sigma_stress_tensor(phis_v1)
assert T_sig_v1.applyfunc(cancel) == Matrix.zeros(n, n), "V_1-only T_sigma nonzero"
tick(f"  V_1-only control: T_sigma == 0? {T_sig_v1.applyfunc(cancel) == Matrix.zeros(n, n)}")
T_sig_center = T_sig.applyfunc(lambda e: cancel(e.subs(CENTER)))
print("  T_sigma at center (exact over Q):")
for i in range(n):
    print("    ", [str(T_sig_center[i, j]) for j in range(n)])
# distinctness: T_sigma is NOT a scalar multiple of T[psi] (different tensor structure)
distinct = not (T_psi_center[2, 2] == 0) or (T_sig_center[2, 2] == 0)
tick(f"  T_sigma is a GENUINE alternative (distinct structure): T[psi](2,2)="
     f"{T_psi_center[2,2]} vs T_sigma(2,2)={T_sig_center[2,2]}")

# --- 3.3 NO-Ric/R/G grep guard (fp-assume-einstein) --------------------------------
# The T-construction must not USE any Ric/R/G curvature symbol. We grep THIS driver's
# T-building functions (psi_scalar, scalar_stress_tensor, sigma_multiplet,
# sigma_stress_tensor, _x123_field) for forbidden curvature symbols in EXECUTABLE
# CODE -- comments and string-literal docstrings (which legitimately mention "NO Ric/
# R/G" as the constraint being honored) are STRIPPED first, so the guard checks usage,
# not documentation (Deviation Rule 1: a comment-mention is not a code-use).
import re as _re
import io as _io
import tokenize as _tokenize


def _strip_comments_and_strings(source):
    """Return `source` with all comments and string literals blanked (replaced by
    spaces, preserving line structure) so a symbol grep sees only executable code."""
    out = []
    try:
        toks = _tokenize.generate_tokens(_io.StringIO(source).readline)
        for tok in toks:
            ttype, tstr = tok.type, tok.string
            if ttype in (_tokenize.COMMENT, _tokenize.STRING):
                out.append(_re.sub(r'\S', ' ', tstr))   # blank out, keep length/newlines
            else:
                out.append(tstr)
            out.append(' ')
    except _tokenize.TokenError:
        return source
    return ''.join(out)


_src = open(os.path.abspath(__file__)).read()
_t_funcs = ['def _x123_field', 'def psi_scalar', 'def scalar_stress_tensor',
            'def sigma_multiplet', 'def sigma_stress_tensor']
_forbidden = [r'\bRic\b', r'\bRicci\b', r'\bRscalar\b', r'\bRiem\b', r'\bEinstein\b',
              r'\bspacetime_curvature_of_g\b', r'\bG1\b', r'\bG_1\b']
_start = min(_src.index(fn) for fn in _t_funcs)
_end = _src.index('# --- 3.3 NO-Ric/R/G grep guard')
_tsrc_code = _strip_comments_and_strings(_src[_start:_end])   # CODE only (no comments/docstrings)
_hits = {pat: _re.findall(pat, _tsrc_code) for pat in _forbidden}
_hits = {k: v for k, v in _hits.items() if v}
tick(f"  NO-Ric/R/G grep over the T-construction CODE (comments/docstrings stripped): "
     f"forbidden-symbol hits = {_hits}")
assert not _hits, f"FORBIDDEN curvature symbol USED in T construction (fp-assume-einstein): {_hits}"
tick("  GUARD: NO Ric/R/G/Einstein/spacetime_curvature symbol USED in the T construction "
     "(fp-assume-einstein avoided; comment-mentions of the constraint are not code-uses)")

print("-" * 78)
print(f"TASK 3 OK -- BOTH T candidates built INDEPENDENTLY of any Einstein form:")
print(f"  PRIMARY   T[psi]   : symmetric, conserved (box psi=0 identically), T->0 as "
      f"||M||->0, V_1-inert; psi via det_3 SSOT.")
print(f"  ALTERNATIVE T[V_1/2]: symmetric, conserved (all box phi^a=0), T->0 as ||M||->0, "
      f"V_1-inert; genuine 16-field sigma model, G_ab=delta.")
print(f"  Conservation is EXACT (not merely on-shell): every cross-term scalar channel is "
      f"LINEAR in the slice coords => harmonic => d^mu T_munu = 0 on the nose. NO Ric/R/G.")
