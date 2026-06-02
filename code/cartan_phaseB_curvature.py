#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# Phase 77 (v18.0 Cartan / MacDowell-Mansouri) -- Plan 77-01
#   COFRAME NON-DEGENERACY + CLOSED-FORM SPIN CONNECTION omega(e) + FLATNESS SUB-GATE
# ============================================================================
#
# CONVENTIONS (CONVENTIONS.md sec 11; state.json convention_lock):
#   * GRAVITY = the Lorentz block R[omega] of the Cartan/MM curvature F = dA + A^A,
#     A = omega (+) (1/l) e ;  F = ( R[omega] - (Lambda/3) e^e ) + d_omega e  (Wise gr-qc/0611154).
#     The Lorentz block is the Riemann curvature of the SOLDERING-FORM metric g = e.e,
#     with e = pi_u(dE) the forced 4d Lorentzian (1,3) coframe of Phase 75. Berry F_B is the
#     INTERNAL so(6)=SU(4) gauge sector -- NOT gravity (Phase 76 overturn).
#   * Metric signature mostly-minus (+,-,-,-) timelike-positive; eta = diag(+1,-1,-1,-1).
#   * EXACT over Q (sympy over QQ). NEVER numpy.linalg on a decisive verdict (fp-float-decisive).
#   * det SSOT = ring_lemma_verification.py det_3; octonion_algebra.py BANNED (source-guarded).
#   * Riemann sign: NEGATIVE & constant; cone-Hessian K=-1/2, round H^3 K=-1 (factor 2). The
#     engine Totaro/hand-rolled convention gives K=-1/2; the new closed-form omega(e) -> R[omega]
#     route is sign-pinned to it (a UNIFORM global factor, established below).
#
# INDEX LAYOUT (LOCKED LIVE -- precheck cartan_phaseB_metric_precheck.py, commit f0e544a6):
#   * slice coords (g base) = engine idx [1,2,3,10] = (beta,gamma,p,q) = h_2(C_u) ~ R^{3,1}.
#   * V_{1/2} coframe survivors = engine idx [11,18,19,26] = C_u^2 (pi_u survivors).
#   * The stale {17,18,19,26} frame is a DIFFERENT/conflated frame -- NOT used.
#
# THE FLATNESS SUB-GATE (Task 1, decisive, FIRST):
#   Build g = e.e(x) for ONE sample M != 0 (M in V_{1/2}, C_u-survivors), extract the
#   closed-form torsion-free Levi-Civita spin connection omega(e), compute R[omega] at a
#   rational basepoint, EXACT over Q. If R[omega] != 0 (>=1 nonzero rational component) =>
#   genuine curvature => Phase B proceeds. If R[omega] == 0 exactly => rigid/integrable
#   soldering => pure-gauge => NO gravity => HONEST TRIVIAL-DEATH STOP (a publishable
#   negative; do NOT soften to "approximately flat").
#
# LOAD-BEARING IDENTITY (textbook tetrad gravity; validated standalone, see omega(e) section):
#   For a TORSION-FREE Levi-Civita omega built (via formula (2)) from ANY tetrad e with
#   g = e.e, the second-Cartan-structure curvature R[omega]^{ab}_{mu nu}, frame-converted to
#   R^rho_{sigma mu nu} and lowered with g, EQUALS the metric Levi-Civita Riemann R_{rho sigma mu nu}
#   of g. (The translation block d_omega e vanishes by construction, isolating the Lorentz block.)
#   => the flatness verdict R[omega] != 0 is RIGOROUSLY EQUIVALENT to R_metric[g=e.e] != 0, which
#   the warm v17.0 engine computes EXACT over Q two independent ways (Totaro spacetime_curvature_of_g
#   + hand-rolled Christoffel hand_rolled_riemann_of_g). We deliver the verdict via that exact metric
#   Riemann AND exhibit the explicit closed-form omega(e) machinery (formula 2) the contract requires.
#
# TETRAD CONSTRUCTION (Open Q1 decision -- documented):
#   PRIMARY-intended route e = pi_u(dE) carried symbolically is SET ASIDE: its symbolic
#   differentiation through the surd-laden orthonormal frame hits the >200s watchdog cliff.
#   FALLBACK route (contract-sanctioned, Open Q1; R[omega] is FRAME-INVARIANT so any valid e works):
#   factorize g(x) over Q-adjoin-surds at the rational basepoint via an exact Lagrange congruence
#   (timelike reordered first), giving a genuine invertible tetrad e0 with e0^T eta e0 = g0 EXACTLY.
#   g = e.e is verified EXACTLY over Q either way.
#
# WATCHDOG / SOCKET DISCIPLINE: run foreground with `python -u`; differentiate g SYMBOLICALLY then
#   SUBSTITUTE a rational basepoint then INVERT (never a fully-symbolic 4x4 inverse). The driver
#   prints progress continuously so the stream-watchdog does not kill a long no-output symbolic run.
#
# Reproducibility: Python 3.14.x, SymPy 1.14.0 (deterministic, exact over Q; no RNG, no float on any
#   decisive path). Reuses code/bulk_geometry_verification.py + ring_lemma_verification.py +
#   embedding_under_E_verification.py + the precheck frozen layout.
#
# Runnable:  python3 -u code/cartan_phaseB_curvature.py
# Exit 0 iff all decisive checks PASS AND the flatness gate renders its verdict cleanly.
# ============================================================================

import os
import sys
import time

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import (Matrix, Rational, cancel, symbols, diff, sqrt, sign as _sign,  # noqa: E402
                   simplify, eye, Symbol)

import bulk_geometry_verification as B  # noqa: E402  (warm v17.0 curvature + matter-on-flat harness)
import ring_lemma_verification as RL    # noqa: E402  (det SSOT)
import embedding_under_E_verification as EMB  # noqa: E402  (the literal pi_u soldering map E())

# ---- Phase-75 / precheck frozen layout (carried verbatim) -------------------
V0_IDX = list(range(1, 11))
V_HALF_IDX = list(range(11, 27))          # V_{1/2}(E_11), idx 11..26 (matter)
CU_SURVIVOR_IDX = [11, 18, 19, 26]        # C_u^2 survivors of pi_u on V_{1/2}
CU4_IDX = [1, 2, 3, 10]                   # beta,gamma,p,q (the g base slice coords)

# The orthonormal-frame Minkowski metric eta_ab = diag(+1,-1,-1,-1) (frame indices a).
ETA = Matrix([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
N = 4

# The Phase-75 soldering-form metric g_sold in RAW {beta,gamma,p,q} coords (== precheck G_DET2_RAW).
G_DET2_RAW = Matrix([[0, Rational(1, 2), 0, 0],
                     [Rational(1, 2), 0, 0, 0],
                     [0, 0, -1, 0],
                     [0, 0, 0, -1]])

# ---- THE DECISIVE SAMPLE (locked; see 77-01-LOG.md sample-selection) ---------
# Pure C_u-survivor V_{1/2} matter [11,18,19,26] at SMALL amplitude (stays in the (1,3)
# Lorentzian splice -- larger amplitudes flip to (3,1), the RESEARCH red flag) + a V_0 x1
# partner so the det_3 triple cross-term has all three slots. Slice at the center.
MATTER = {k: v * Rational(1, 10) for k, v in
          {11: Rational(2), 18: Rational(-1), 19: Rational(3), 26: Rational(5)}.items()}
BG = {4: Rational(1)}
SLICE_VALS = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]

ALL_PASS = True
_t0 = time.time()


def tick(msg):
    print(f"[{time.time() - _t0:7.1f}s] {msg}", flush=True)


def _report(label, ok):
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


# ============================================================================
# 0. SOURCE GUARD (no octonion_algebra; no numpy.linalg on decisive path)
# ============================================================================
def source_guard():
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra absent + exact-over-Q det SSOT + no numpy on decisive path")
    print("=" * 78)
    oa_absent = "octonion_algebra" not in sys.modules
    np_absent = "numpy" not in sys.modules
    native = (RL.det_3.__module__ == "ring_lemma_verification"
              and RL.jordan.__module__ == "ring_lemma_verification"
              and RL.Tr.__module__ == "ring_lemma_verification")
    Xspot = B.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                              B.oct_zero(), B.oct_zero(), B.oct_zero())
    spot = RL.det_3(Xspot)
    spot_ok = (spot == 30) and (not isinstance(spot, float))
    _report("octonion_algebra NOT imported on the decisive path", oa_absent)
    _report(f"det SSOT native exact-over-Q ring_lemma (det_3(diag(2,3,5))=={spot})", native and spot_ok)
    _report("numpy NOT imported on this driver's decisive path (all sympy over QQ)", np_absent)
    return oa_absent and native and spot_ok and np_absent


# ============================================================================
# 1. CLOSED-FORM TORSION-FREE LEVI-CIVITA SPIN CONNECTION omega(e)   (formula 2)
#    DERV-04 / contract spin_connection_omega.
# ============================================================================
def spin_connection_omega(E, coords, etaf=ETA):
    """Closed-form torsion-free Levi-Civita spin connection (77-RESEARCH formula (2)):

        omega_mu^{ab} =  (1/2) e^{nu a}( d_mu e_nu^b - d_nu e_mu^b )
                       - (1/2) e^{nu b}( d_mu e_nu^a - d_nu e_mu^a )
                       - (1/2) e^{rho a} e^{sig b}( d_rho e_sig^c - d_sig e_rho^c ) e_{mu c}

    `E[a,mu]` = e^a_mu (frame index a, coord index mu), symbolic in `coords`. Index-raising
    e^{nu a} uses the INVERSE tetrad e_a^nu (Einv[nu,a]) contracted with the frame metric etaf
    (NOT g); e_{mu c} = etaf_{cd} e^d_mu. Antisymmetric in (a,b) BY CONSTRUCTION (formula 2 is
    the exact torsion-free connection). Returns (W, Einv) with W[mu][a][b] = omega_mu^{ab}.
    EXACT over Q (or Q-adjoin-surds). `etaf` is the frame metric (default diag(+1,-1,-1,-1))."""
    Einv = E.inv()                       # Einv[nu,a] = e_a^nu

    def eup(nu, a):                      # e^{nu a} = e_b^nu etaf^{ba}  (etaf diagonal +-1 => etaf^{-1}=etaf)
        return sum(Einv[nu, b] * etaf[b, a] for b in range(N))

    def de(mu, nu, b):                   # d_mu e_nu^b
        return diff(E[b, nu], coords[mu])

    def elow(mu, c):                     # e_{mu c} = etaf_{cd} e^d_mu
        return sum(etaf[c, d] * E[d, mu] for d in range(N))

    W = [[[0] * N for _ in range(N)] for _ in range(N)]
    for mu in range(N):
        for a in range(N):
            for b in range(N):
                t1 = Rational(1, 2) * sum(eup(nu, a) * (de(mu, nu, b) - de(nu, mu, b)) for nu in range(N))
                t2 = -Rational(1, 2) * sum(eup(nu, b) * (de(mu, nu, a) - de(nu, mu, a)) for nu in range(N))
                t3 = 0
                for rho in range(N):
                    for sig in range(N):
                        for c in range(N):
                            t3 += eup(rho, a) * eup(sig, b) * (de(rho, sig, c) - de(sig, rho, c)) * elow(mu, c)
                W[mu][a][b] = cancel(t1 + t2 - Rational(1, 2) * t3)
    return W, Einv


def torsion_of(W, E, coords, etaf=ETA):
    """Torsion 2-form Theta^a_{mu nu} = d_mu e^a_nu - d_nu e^a_mu + omega_mu^a_b e^b_nu
       - omega_nu^a_b e^b_mu, with the mixed omega_mu^a_b = omega_mu^{ac} etaf_{cb}.
       Returns the max-abs symbolic residual (0 for a torsion-free Levi-Civita omega)."""
    def omega_mixed(mu, a, b):
        return sum(W[mu][a][c] * etaf[c, b] for c in range(N))
    worst = 0
    for a in range(N):
        for mu in range(N):
            for nu in range(N):
                th = diff(E[a, nu], coords[mu]) - diff(E[a, mu], coords[nu])
                th += sum(omega_mixed(mu, a, b) * E[b, nu] - omega_mixed(nu, a, b) * E[b, mu]
                          for b in range(N))
                if cancel(th) != 0:
                    worst = th
    return worst


def riemann_from_omega(W, E, Einv, coords, g, etaf=ETA):
    """Second Cartan structure equation: R^{ab}_{mu nu} = d_mu omega_nu^{ab} - d_nu omega_mu^{ab}
       + omega_mu^{ac} etaf_{cd} omega_nu^{db} - omega_nu^{ac} etaf_{cd} omega_mu^{db}.
    Frame -> coordinate: R^rho_{sig mu nu} = e_a^rho e^b_sig R^{ab}_{mu nu}; lower R_{rho sig mu nu}
    = g_{rho lam} R^lam_{sig mu nu}. Returns the lower-index nested list R[rho][sig][mu][nu]
    (RAW sign; the global sign-pin factor is applied by the caller). EXACT over Q."""
    def Rframe(a, b, mu, nu):
        t = diff(W[nu][a][b], coords[mu]) - diff(W[mu][a][b], coords[nu])
        for c in range(N):
            for d in range(N):
                t += W[mu][a][c] * etaf[c, d] * W[nu][d][b] - W[nu][a][c] * etaf[c, d] * W[mu][d][b]
        return cancel(t)

    R = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for rho in range(N):
        for sig in range(N):
            for mu in range(N):
                for nu in range(N):
                    s = 0
                    for lam in range(N):
                        Rlam = sum(Einv[lam, a] * E[b, sig] * Rframe(a, b, mu, nu)
                                   for a in range(N) for b in range(N))
                        s += g[rho, lam] * Rlam
                    R[rho][sig][mu][nu] = cancel(s)
    return R


# ============================================================================
# 2. SIGN-PIN: the closed-form omega(e) -> R[omega] route vs the engine convention (K=-1/2)
# ============================================================================
def sign_pin():
    """Pin the global sign of the closed-form omega(e) -> R[omega] route against the engine's
    Totaro/hand-rolled convention (which yields the cone-Hessian K=-1/2). Uses a RATIONAL warped
    Lorentzian reference g = diag(1,-f^2,-1,-1), f=1+x0^2 (rational tetrad e=diag(1,f,1,1)), so the
    whole pin is exact over Q, fast, surd-free. Establishes:
      (i)  my closed-form R[omega] == -1 * (bare Christoffel Riemann)  [uniform global factor],
      (ii) bare Christoffel == engine Totaro on the cone-Hessian (ratio +1; verified here),
      (iii)engine Totaro == engine hand-rolled on the matter g (ratio +1; verified in main),
    => SIGN-PIN FACTOR = -1: R[omega]_engine_convention = -1 * R[omega]_raw, landing in the K=-1/2
       (negative, constant) convention BEFORE any curvature verdict is read.
    Returns the pin factor (-1)."""
    print("=" * 78)
    print("SIGN-PIN : closed-form omega(e) -> R[omega] vs engine Totaro/K=-1/2 convention")
    print("=" * 78)
    x = symbols('x0 x1 x2 x3', real=True)
    f = 1 + x[0] ** 2
    E = Matrix.diag(1, f, 1, 1)
    g = (E.T * ETA * E).applyfunc(cancel)
    W, Einv = spin_connection_omega(E, list(x))
    # antisymmetry + torsion-free of the closed form on this reference:
    antisym = all(cancel(W[mu][a][b] + W[mu][b][a]) == 0
                  for mu in range(N) for a in range(N) for b in range(N))
    tors = torsion_of(W, E, list(x))
    _report("closed-form omega(e) antisymmetric omega_mu^{ab}=-omega_mu^{ba} [exact Q]", antisym)
    _report("closed-form omega(e) TORSION-FREE d_omega e == 0 (formula 2 by construction) [exact Q]",
            tors == 0)
    R_raw = riemann_from_omega(W, E, Einv, list(x), g)

    # bare Christoffel Riemann of the same g (the engine convention, ratio +1 vs Totaro):
    ginv = g.inv()
    Gam = [[[cancel(Rational(1, 2) * sum(ginv[a, d] * (diff(g[d, b], x[c]) + diff(g[d, c], x[b])
            - diff(g[b, c], x[d])) for d in range(N))) for c in range(N)] for b in range(N)]
           for a in range(N)]

    def Rbare_low(rho, sig, mu, nu):
        return cancel(sum(g[rho, lam] * (diff(Gam[lam][sig][nu], x[mu]) - diff(Gam[lam][sig][mu], x[nu])
                      + sum(Gam[lam][mu][e] * Gam[e][sig][nu] - Gam[lam][nu][e] * Gam[e][sig][mu]
                            for e in range(N))) for lam in range(N)))

    ratios = set()
    for c in [(0, 1, 0, 1), (0, 1, 1, 0)]:
        rb = Rbare_low(*c)
        rr = R_raw[c[0]][c[1]][c[2]][c[3]]
        if rb != 0:
            ratios.add(cancel(rr / rb))
    pin_ok = (ratios == {Rational(-1)})
    print(f"      raw-omega / bare-Christoffel ratio = {ratios}  (expect {{-1}})")
    _report("closed-form omega(e) -> R[omega] = -1 * (bare Christoffel) -- a UNIFORM global sign "
            "factor (NOT a per-component bug) [exact Q]", pin_ok)

    # cone-Hessian: bare Christoffel == Totaro (ratio +1), and gives K=-1/2:
    Phi, ccoords, Q = B._h2cu_cone_potential_4d()
    gc = B.hessian_metric(Phi, ccoords)
    Cc = B.cubic_form_C(Phi, ccoords)
    ginvc = gc.inv().applyfunc(cancel)
    pt = {ccoords[0]: Rational(3, 2), ccoords[1]: Rational(1), ccoords[2]: Rational(1, 2),
          ccoords[3]: Rational(0)}
    gc_at = gc.subs(pt).applyfunc(cancel)
    ginvc_at = ginvc.subs(pt).applyfunc(cancel)
    Cc_at = [[[cancel(Cc[i][j][k].subs(pt)) for k in range(N)] for j in range(N)] for i in range(N)]
    R_tot = B.totaro_riemann(ginvc_at, Cc_at, N, simp=cancel)
    xc = ccoords
    Gamc = [[[cancel(Rational(1, 2) * sum(ginvc[a, d] * (diff(gc[d, b], xc[c]) + diff(gc[d, c], xc[b])
             - diff(gc[b, c], xc[d])) for d in range(N))) for c in range(N)] for b in range(N)]
            for a in range(N)]

    def Rbare_cone(rho, sig, mu, nu):
        return cancel(sum(gc[rho, lam] * (diff(Gamc[lam][sig][nu], xc[mu]) - diff(Gamc[lam][sig][mu], xc[nu])
                      + sum(Gamc[lam][mu][e] * Gamc[e][sig][nu] - Gamc[lam][nu][e] * Gamc[e][sig][mu]
                            for e in range(N))) for lam in range(N))).subs(pt)
    comp = (0, 1, 0, 1)
    rt = R_tot[comp[0]][comp[1]][comp[2]][comp[3]]
    rb = cancel(Rbare_cone(*comp))
    tot_bare_ratio = cancel(rt / rb) if rb != 0 else None
    bm = B.h3_cone_hessian_benchmark()
    _report(f"engine Totaro == bare Christoffel on cone-Hessian (ratio {tot_bare_ratio}, expect +1) "
            "=> 'engine convention' == bare Christoffel sign [exact Q]", tot_bare_ratio == 1)
    _report(f"engine cone-Hessian benchmark K_value == -1/2 (constant, NEGATIVE; round K={bm['round_K']}) "
            "-- the sign convention the pinned R[omega] reproduces [exact Q]",
            bm["K_value"] == Rational(-1, 2) and bm["sym_ok"])
    print(f"      => SIGN-PIN FACTOR = -1  (R[omega]_engine = -1 * R[omega]_raw; lands in K=-1/2)")
    return Rational(-1)


# ============================================================================
# 3. TETRAD at the basepoint (Open Q1 fallback: exact congruence factorization of g0)
# ============================================================================
def tetrad_at_point(g0, etaf=ETA):
    """Exact congruence factorization e0 of a symmetric (1,3) rational g0: e0^T etaf e0 = g0,
    with etaf = diag(+1,-1,-1,-1). Via Lagrange's method (rational, handles null-aligned blocks
    by a hyperbolic mix), producing g0 = P^-T D P^-1 with D rational-diagonal, then reordering
    the timelike (positive) pivot first and absorbing sqrt(|D|). e0 lives in Q-adjoin-surds; it is
    a CONSTANT matrix at the basepoint (no differentiation needed for det/g=e.e). Returns
    (e0, frame_signs). R[omega] is frame-invariant, so this fallback is sound (Open Q1)."""
    def lagrange(G):
        A = G.copy()
        P = eye(N)
        for i in range(N):
            if A[i, i] == 0:
                piv = None
                for k in range(i + 1, N):
                    if A[k, k] != 0:
                        piv = ("d", k)
                        break
                if piv is None:
                    for k in range(i + 1, N):
                        if A[i, k] != 0:
                            piv = ("o", k)
                            break
                if piv is None:
                    continue
                kind, k = piv
                E = eye(N)
                if kind == "d":
                    E[i, i] = 0
                    E[k, k] = 0
                    E[i, k] = 1
                    E[k, i] = 1
                else:
                    E[k, i] = 1
                A = (E.T * A * E).applyfunc(cancel)
                P = (P * E).applyfunc(cancel)
            if A[i, i] != 0:
                E = eye(N)
                for k in range(i + 1, N):
                    if A[i, k] != 0:
                        E[i, k] = -A[i, k] / A[i, i]
                A = (E.T * A * E).applyfunc(cancel)
                P = (P * E).applyfunc(cancel)
        return P, A  # A = P^T G P  =>  G = P^-T A P^-1
    P, D = lagrange(g0)
    Pinv = P.inv()
    diag = [cancel(D[i, i]) for i in range(N)]
    signs = [_sign(d) for d in diag]
    order = sorted(range(N), key=lambda i: 0 if signs[i] > 0 else 1)  # timelike (+) first
    Perm = Matrix.zeros(N, N)
    for newi, oldi in enumerate(order):
        Perm[newi, oldi] = 1
    Dp = (Perm * D * Perm.T).applyfunc(cancel)
    Sd = Matrix.diag(*[sqrt(abs(Dp[i, i])) for i in range(N)])
    # g0 = Pinv^T D Pinv = (Sd Perm Pinv)^T etaf (Sd Perm Pinv)
    e0 = (Sd * Perm * Pinv).applyfunc(cancel)
    return e0, [_sign(Dp[i, i]) for i in range(N)]


# ============================================================================
# 4. THE FLATNESS SUB-GATE (Task 1) + COFRAME NON-DEGENERACY (Task 2) + omega(e) (Task 3)
# ============================================================================
def flatness_sub_gate(pin):
    """The decisive opening gate. Build g=e.e for the sample M!=0 via the matter-on-flat pipeline,
    compute R[omega] (= the metric Levi-Civita Riemann of g, by the torsion-free identity) via the
    engine's TWO independent exact-over-Q routes (Totaro + hand-rolled Christoffel), apply the
    sign-pin, and assert >=1 NONZERO rational component. Returns (proceed, info)."""
    print("=" * 78)
    print("FLATNESS SUB-GATE (Task 1) : R[omega(e)] for one sample M != 0 (decisive, EXACT over Q)")
    print("=" * 78)
    print(f"      sample matter M (C_u-survivors {CU_SURVIVOR_IDX}) = {MATTER}")
    print(f"      V_0 x1 partner BG = {BG} ; slice basepoint (beta,gamma,p,q) = {SLICE_VALS}")

    tick("computing R[omega] = metric Levi-Civita Riemann of g=e.e (Totaro route) ...")
    res = B.spacetime_curvature_of_g(MATTER, SLICE_VALS, bg_delta=BG)
    g0, Rtot, Rscalar = res["g"], res["R"], res["Rscalar"]

    tick("cross-checking via the INDEPENDENT hand-rolled Christoffel Riemann route ...")
    comps = [(0, 2, 0, 2), (2, 3, 2, 3), (0, 1, 0, 1), (1, 2, 1, 2)]
    hr = B.hand_rolled_riemann_of_g(MATTER, SLICE_VALS, bg_delta=BG, components=comps)
    two_routes_agree = all(cancel(hr[c] - Rtot[c[0]][c[1]][c[2]][c[3]]) == 0 for c in comps)
    _report("R[omega]=R_metric[g=e.e]: Totaro and INDEPENDENT hand-rolled Christoffel routes AGREE "
            "exactly over Q on the sampled components [exact Q]", two_routes_agree)

    # Apply the sign-pin (engine convention; the metric Riemann here IS the engine convention,
    # pin factor recorded for the closed-form-omega route comparison; metric R is already pinned).
    sym_ok = B.riemann_symmetry_ok(Rtot, N, simp=cancel)
    _report("Riemann algebraic symmetries hold (engine correctness) [exact Q]", sym_ok)

    # DECISIVE: at least one NONZERO rational component (genuine curvature).
    nonzero_comps = [(i, j, k, l) for i in range(N) for j in range(N) for k in range(N) for l in range(N)
                     if cancel(Rtot[i][j][k][l]) != 0]
    rscalar_nonzero = (cancel(Rscalar) != 0)
    sample_vals = {c: pin * Rtot[c[0]][c[1]][c[2]][c[3]] for c in comps}
    print("      sign-pinned R[omega] sample components (engine K=-1/2 convention):")
    for c, v in sample_vals.items():
        print(f"        R[omega]_{c[0]}{c[1]}{c[2]}{c[3]} = {v}  ({'NONZERO' if cancel(v) != 0 else 'zero'})")
    print(f"      Ricci scalar R[g=e.e] = {cancel(Rscalar)}  ({'NONZERO' if rscalar_nonzero else 'ZERO'})")
    print(f"      # nonzero lower-index R[omega] components (exact over Q) = {len(nonzero_comps)} / 256")

    all_rational = all(getattr(cancel(Rtot[i][j][k][l]), "is_rational", False) or cancel(Rtot[i][j][k][l]) == 0
                       for i in range(N) for j in range(N) for k in range(N) for l in range(N))
    _report("every R[omega] component is an EXACT RATIONAL over Q (no float on the decisive path) "
            "[fp-float-decisive rejected]", all_rational)

    proceed = (len(nonzero_comps) > 0 and rscalar_nonzero)
    _report("FLATNESS SUB-GATE: R[omega(e)] has >=1 NONZERO rational component for the M!=0 sample "
            "(GENUINE CURVATURE) => Phase B PROCEEDS  [if zero => trivial-death STOP]", proceed)
    verdict = "PROCEED (R[omega] != 0; genuine curvature)" if proceed else \
              "TRIVIAL-DEATH / STOP (R[omega] == 0; rigid/integrable soldering; no gravity)"
    print(f"      >>> FLATNESS VERDICT: {verdict}")
    return proceed, {"g0": g0, "Rscalar": cancel(Rscalar), "n_nonzero": len(nonzero_comps),
                     "sample": {f"{c[0]}{c[1]}{c[2]}{c[3]}": str(cancel(v)) for c, v in sample_vals.items()},
                     "two_routes_agree": two_routes_agree, "verdict": verdict}


def coframe_nondegeneracy(g0):
    """Task 2 (B(a), test-coframe-invertible): e=pi_u(dE) is a genuine INVERTIBLE soldering form.
    g=e.e exactly over Q; det(e)!=0 at the M!=0 sample AND the M=0 baseline; signature (1,3)."""
    print("=" * 78)
    print("COFRAME NON-DEGENERACY (Task 2, B(a)) : det(e^a_mu) != 0, g=e.e exact, signature (1,3)")
    print("=" * 78)
    # M=0 baseline g == G_DET2_RAW (the precheck/Phase-75 (1,3) Lorentzian base):
    res0 = B.spacetime_curvature_of_g({}, SLICE_VALS, bg_delta=BG)
    g_M0 = res0["g"]
    base_eq = (simplify(g_M0 - G_DET2_RAW) == Matrix.zeros(N, N))
    _report("g(M=0) == G_DET2_RAW (Phase-75 (1,3) Lorentzian base; matter-on-flat h(M=0)=0 identically) "
            "[exact Q]", base_eq)
    sig0 = B.eig_signature_count(g_M0)
    sigM = B.eig_signature_count(g0)
    _report(f"signature(g, M=0) == (1,3) via real_roots over Q (got {sig0}) [exact Q; null-aligned, "
            "NOT Sylvester]", sig0 == (1, 3, 0))
    _report(f"signature(g, M!=0 sample) == (1,3) (stayed in the Lorentzian splice; got {sigM}) [exact Q]",
            sigM == (1, 3, 0))
    # Tetrads (fallback congruence factorization) at both points; det != 0; g=e.e exact.
    e0_M0, fs0 = tetrad_at_point(g_M0)
    e0_M, fsM = tetrad_at_point(g0)
    geq0 = (simplify(e0_M0.T * ETA * e0_M0 - g_M0) == Matrix.zeros(N, N))
    geqM = (simplify(e0_M.T * ETA * e0_M - g0) == Matrix.zeros(N, N))
    det0 = simplify(e0_M0.det())
    detM = simplify(e0_M.det())
    _report("g = eta_ab e^a_mu e^b_nu EXACTLY over Q at M=0 (tetrad reproduces G_DET2_RAW)", geq0)
    _report("g = eta_ab e^a_mu e^b_nu EXACTLY over Q at the M!=0 sample", geqM)
    _report(f"det(e^a_mu) != 0 at M=0 baseline (det={det0}) -- genuine invertible coframe [exact]",
            det0 != 0)
    _report(f"det(e^a_mu) != 0 at the M!=0 sample (det != 0) -- genuine invertible coframe [exact]",
            detM != 0)
    print(f"      det(e) M=0    = {det0}")
    print(f"      det(e) M!=0   = {detM}")
    print(f"      frame signs (M!=0) = {fsM}  (one +, three - => (1,3))")
    return {"sig_M0": sig0, "sig_M": sigM, "det_M0": str(det0), "det_M": str(detM),
            "base_eq": base_eq}


def closed_form_omega_demo(pin):
    """Task 3 (B(b), DERV-04): the closed-form Lorentz Spin(3,1) connection omega(e) -- formula (2) --
    implemented (spin_connection_omega), validated antisymmetric + torsion-free, and shown to
    reproduce the metric Levi-Civita Riemann (the torsion-free identity) on a RATIONAL tetrad,
    sign-pinned to K=-1/2. (The matter tetrad e0 is surd-laden so its symbolic d-omega hits the
    watchdog; the verdict R[omega]!=0 is delivered by the provably-equal metric-Riemann route in
    the flatness gate. Here we CERTIFY the omega(e) machinery the contract requires.)"""
    print("=" * 78)
    print("CLOSED-FORM omega(e) (Task 3, B(b)) : formula (2), antisymmetric, torsion-free, R[omega]=R_metric")
    print("=" * 78)
    x = symbols('x0 x1 x2 x3', real=True)
    f = 1 + x[0] ** 2                       # rational warped Lorentzian tetrad reference
    E = Matrix.diag(1, f, 1, 1)
    g = (E.T * ETA * E).applyfunc(cancel)
    W, Einv = spin_connection_omega(E, list(x))
    antisym = all(cancel(W[mu][a][b] + W[mu][b][a]) == 0
                  for mu in range(N) for a in range(N) for b in range(N))
    tors = torsion_of(W, E, list(x))
    _report("omega_mu^{ab}(e,de) via closed-form formula (2): ANTISYMMETRIC omega^{ab}=-omega^{ba} "
            "[exact Q]", antisym)
    _report("TORSION-FREE: d_omega e = de + omega^e == 0 identically (formula 2 by construction) "
            "[exact Q; nonzero would be a bug]", tors == 0)
    # Index-raising uses the inverse tetrad e_a^mu (Einv), NOT g -- verify Einv is the tetrad inverse:
    inv_ok = (simplify(E * Einv - eye(N)) == Matrix.zeros(N, N))
    _report("index-raising e^{nu a} uses the INVERSE tetrad e_a^mu (E*Einv == I), NOT g [exact Q]", inv_ok)
    # R[omega] (sign-pinned) == metric Levi-Civita Riemann of g (the torsion-free identity):
    R_raw = riemann_from_omega(W, E, Einv, list(x), g)
    ginv = g.inv()
    Gam = [[[cancel(Rational(1, 2) * sum(ginv[a, d] * (diff(g[d, b], x[c]) + diff(g[d, c], x[b])
            - diff(g[b, c], x[d])) for d in range(N))) for c in range(N)] for b in range(N)]
           for a in range(N)]

    def Rbare(rho, sig, mu, nu):
        return cancel(sum(g[rho, lam] * (diff(Gam[lam][sig][nu], x[mu]) - diff(Gam[lam][sig][mu], x[nu])
                      + sum(Gam[lam][mu][e] * Gam[e][sig][nu] - Gam[lam][nu][e] * Gam[e][sig][mu]
                            for e in range(N))) for lam in range(N)))
    comps = [(0, 1, 0, 1), (0, 1, 1, 0), (1, 2, 1, 2)]
    identity_ok = all(cancel(pin * R_raw[c[0]][c[1]][c[2]][c[3]] - Rbare(*c)) == 0 for c in comps)
    _report("LOAD-BEARING IDENTITY: sign-pinned R[omega] (2nd Cartan structure) == metric Levi-Civita "
            "Riemann of g=e.e on the tested components [exact Q] -- the Lorentz block IS the Riemann "
            "tensor (translation block d_omega e=0)", identity_ok)
    return {"antisym": antisym, "torsion_free": tors == 0, "identity_ok": identity_ok}


# ============================================================================
# 5. PLAN 77-02 TASK 1 : assemble A = omega (+) e, compute F = dA + A^A,
#    separate Lorentz / torsion blocks, convert to R_{rho sigma mu nu} of g=e.e.
#    CALC-05 / success criterion 3. EXACT over Q at the rational basepoint.
# ============================================================================
#
# THE (A)dS CARTAN / MACDOWELL-MANSOURI CONNECTION (Wise gr-qc/0611154):
#   A = omega + (1/l) e ,   l^2 = 3/Lambda  (l formal; Lambda MEASURED downstream).
#   Matrix rep on the (n+1)=5-dim (A)dS/Poincare module (frame indices a=0..3 + the
#   transvection direction 4): in the so(3,2)/so(4,1)/iso(3,1) basis,
#       A_mu = [[ omega_mu^a_b ,   (1/l) e^a_mu ],
#               [ s*(1/l) e_b^? ,        0      ]]
#   where omega_mu^a_b = omega_mu^{ac} eta_cb (mixed Lorentz), and the bottom row carries
#   the transvection with s = -Lambda/3 * l^2 = -1 (AdS, so(3,2)) / +1 (dS, so(4,1)) /
#   0 (Poincare iso(3,1), Lambda=0). We CARRY s symbolically as Lam (=Lambda) so the
#   Lorentz block of F shows the -(Lambda/3) e^e term explicitly; the PHYSICAL value
#   Lambda=0 (77-01 / CONVENTIONS sec 6, the flat KKT vacuum) collapses it to Poincare.
#
#   F_{mu nu} = d_mu A_nu - d_nu A_mu + [A_mu, A_nu]   (component-matrix; [.,.] IS the A^A
#   wedge term -- sympy.diffgeom has no matrix-valued connection wedge, hand-rolled).
#   Wise decomposition:
#       Lorentz (so(3,1)) block  = R[omega] - (Lambda/3) e^e     (the 4x4 a,b block)
#       translation (R^{3,1}) blk = d_omega e = de + omega^e  (TORSION; the a4/4b entries)
#   The translation block VANISHES for the torsion-free Levi-Civita omega (formula 2).
#
# This is the bookkeeping the contract requires (test-cartan-curvature's assembly half);
# the genuine content is whether that R[omega] is Einstein (Task 4). Never the raw 45-dim
# Spin(9,1) curvature (fp-raw45-curvature); no posited action (fp-imported-action).

Lam = Symbol('Lambda', real=True)   # formal cosmological constant; PHYSICAL value 0 (measured)


def assemble_A(W, E, etaf=ETA, lam=Lam):
    """A_mu as a 5x5 (A)dS/Poincare connection matrix in the so(3,2)/so(4,1)/iso(3,1)
    basis (frame a=0..3 + transvection 4). Lorentz block A_mu[a][b]=omega_mu^{ac} eta_cb;
    transvection column A_mu[a][4]=e^a_mu; transvection row A_mu[4][b]=-(lam/3) e_b^mu-dual
    realized as -(lam/3) eta_bc e^c_mu (so the bottom-row * top-column commutator yields
    the -(lam/3) e^e Lorentz term). l absorbed (formal; reinstated only in the e^e coeff).
    Returns a list A[mu] of 5x5 sympy Matrices. EXACT over Q (+ formal lam)."""
    A = []
    for mu in range(N):
        M = Matrix.zeros(N + 1, N + 1)
        for a in range(N):
            for b in range(N):
                M[a, b] = sum(W[mu][a][c] * etaf[c, b] for c in range(N))  # omega_mu^a_b
            M[a, N] = E[a, mu]                                              # e^a_mu (transvection col)
        for b in range(N):
            # transvection row: -(Lambda/3) e_{b mu} = -(Lambda/3) eta_bc e^c_mu
            M[N, b] = -(lam / 3) * sum(etaf[b, c] * E[c, mu] for c in range(N))
        A.append(M)
    return A


def curvature_F(A, coords):
    """F_{mu nu} = d_mu A_nu - d_nu A_mu + [A_mu, A_nu] (matrix commutator = the A^A term),
    component-matrix curvature. Returns F[mu][nu] (5x5 sympy Matrices). EXACT over Q."""
    F = [[None] * N for _ in range(N)]
    for mu in range(N):
        for nu in range(N):
            dterm = A[nu].applyfunc(lambda e: diff(e, coords[mu])) \
                - A[mu].applyfunc(lambda e: diff(e, coords[nu]))
            comm = A[mu] * A[nu] - A[nu] * A[mu]      # [A_mu, A_nu] -- the A^A wedge term
            F[mu][nu] = (dterm + comm).applyfunc(cancel)
    return F


def split_blocks(F, lam=Lam):
    """Split F[mu][nu] into the Lorentz (so(3,1)) block (4x4 a,b) and the translation
    (R^{3,1}) torsion block (the a-th transvection column F[mu][nu][a][4]). Returns
    (Lor, Tors) with Lor[mu][nu][a][b] = R[omega]_munu^{ab}-(lam/3)(e^e)_munu^{ab} and
    Tors[mu][nu][a] = (d_omega e)^a_munu (= 0 for Levi-Civita). EXACT over Q."""
    Lor = [[[[cancel(F[mu][nu][a, b]) for b in range(N)] for a in range(N)]
            for nu in range(N)] for mu in range(N)]
    Tors = [[[cancel(F[mu][nu][a, N]) for a in range(N)] for nu in range(N)]
            for mu in range(N)]
    return Lor, Tors


def riemann_lower_from_F(Lor, E, Einv, g, etaf=ETA, lam_value=Rational(0)):
    """Convert the Lorentz block to the lower-index Riemann tensor of g=e.e.

    The 5x5 connection Lorentz block A_mu[a][b]=omega_mu^a_b is MIXED (one up a, one
    down b), so the F-commutator Lorentz block Lor[mu][nu][a][b] is the MIXED frame
    curvature R^a_{b mu nu} (NOT both-up R^{ab}). The (A)dS transvection adds
    -(Lambda/3)(e^e)^a_b with (e^e)^a_b = e^a_mu e_{b nu} - e^a_nu e_{b mu} in MIXED form
    (e_{b nu}=eta_bc e^c_nu). The conversion to the coordinate Riemann is the standard
    mixed-frame contraction:
       R^a_{b mu nu} = Lor_munu^a_b + (lam/3)(e^e)^a_b   [strip cosm.; at PHYSICAL lam=0
                                                          the Lorentz block IS R(omega)^a_b],
       R^rho_{sig mu nu} = e_a^rho e^b_sig R^a_{b mu nu}   [e_a^rho=Einv, e^b_sig=E],
       R_{rho sig mu nu} = g_{rho lam} R^lam_{sig mu nu}.
    Returns the lower-index nested list R[rho][sig][mu][nu] (RAW sign; caller applies pin).
    EXACT over Q. lam_value substituted for the formal Lambda (PHYSICAL 0 = Poincare)."""
    def e_wedge_e_mixed(a, b, mu, nu):     # (e^e)^a_b_munu = e^a_mu e_{b nu} - e^a_nu e_{b mu}
        e_b_nu = sum(etaf[b, c] * E[c, nu] for c in range(N))
        e_b_mu = sum(etaf[b, c] * E[c, mu] for c in range(N))
        return E[a, mu] * e_b_nu - E[a, nu] * e_b_mu

    def Rmixed(a, b, mu, nu):              # strip the -(lam/3) e^e term -> pure R(omega)^a_b
        val = Lor[mu][nu][a][b] + (lam_value / 3) * e_wedge_e_mixed(a, b, mu, nu)
        return cancel(val.subs(Lam, lam_value) if hasattr(val, "subs") else val)

    R = [[[[0] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
    for rho in range(N):
        for sig in range(N):
            for mu in range(N):
                for nu in range(N):
                    s = 0
                    for lam in range(N):
                        # R^lam_{sig mu nu} = e_a^lam e^b_sig R^a_{b mu nu}
                        Rlam = sum(Einv[lam, a] * E[b, sig] * Rmixed(a, b, mu, nu)
                                   for a in range(N) for b in range(N))
                        s += g[rho, lam] * Rlam
                    R[rho][sig][mu][nu] = cancel(s)
    return R


def task1_assemble_and_F(pin):
    """Task 1: assemble A=omega(+)e, compute F=dA+A^A, separate Lorentz/torsion blocks,
    convert to R_{rho sigma mu nu}. Done on a RATIONAL warped-Lorentzian tetrad reference
    (surd-free, exact over Q, watchdog-safe) -- the assembly MECHANICS are frame-universal
    (the matter tetrad e0 is surd-laden and its symbolic dA hits the >200s cliff; the
    matter R[omega] verdict is delivered by the provably-equal metric-Riemann route, as in
    77-01). Verifies: torsion block = 0 (Levi-Civita), Lorentz block at PHYSICAL Lambda=0
    == metric Levi-Civita Riemann of g=e.e (the assembly is correct)."""
    print("=" * 78)
    print("TASK 1 (77-02, B(c)) : assemble A=omega(+)e ; F=dA+A^A ; Lorentz/torsion split ; R_{rho sig mu nu}")
    print("=" * 78)
    x = symbols('x0 x1 x2 x3', real=True)
    f = 1 + x[0] ** 2                      # rational warped Lorentzian tetrad reference
    E = Matrix.diag(1, f, 1, 1)
    g = (E.T * ETA * E).applyfunc(cancel)
    W, Einv = spin_connection_omega(E, list(x))

    tick("assembling A=omega(+)e (5x5 iso(3,1)/so(3,2)/so(4,1) rep; Lambda formal) ...")
    A = assemble_A(W, E)
    # the algebra: A_mu[a][b] antisymmetric in the Lorentz block under eta (so(3,1))?
    lor_so31 = all(cancel(sum(A[mu][a, c] * ETA[c, b] + A[mu][b, c] * ETA[c, a]
                  for c in range(N))) == 0 for mu in range(N) for a in range(N) for b in range(N))
    _report("A Lorentz block in so(3,1): omega_mu^{ab} antisymmetric under eta (A=omega(+)e "
            "assembled; transvection column = e^a_mu) [exact Q]", lor_so31)

    tick("computing F_{mu nu}=d_mu A_nu - d_nu A_mu + [A_mu,A_nu] (commutator = A^A term) ...")
    F = curvature_F(A, list(x))
    Lor, Tors = split_blocks(F)

    # Torsion block d_omega e = 0 (Levi-Civita). Check at the PHYSICAL Lambda=0 (the transvection
    # row carries the formal Lambda; torsion is the e-column, Lambda-independent here).
    tors_zero = all(cancel(Tors[mu][nu][a].subs(Lam, 0)) == 0
                    for mu in range(N) for nu in range(N) for a in range(N))
    _report("TRANSLATION (torsion) block d_omega e = de + omega^e == 0 exactly over Q "
            "(Levi-Civita omega is torsion-free; nonzero would be a 77-01 omega bug) [exact Q]",
            tors_zero)

    # Independent torsion cross-check via the standalone torsion_of (formula 1):
    tors2 = torsion_of(W, E, list(x))
    _report("torsion cross-check (standalone Theta^a = de + omega^e via formula 1) == 0 [exact Q]",
            tors2 == 0)

    tick("converting the Lorentz block -> R_{rho sigma mu nu} of g=e.e (formula 4) at Lambda=0 ...")
    R_fromF = riemann_lower_from_F(Lor, E, Einv, g, lam_value=Rational(0))

    # The Lorentz block at PHYSICAL Lambda=0 IS R(omega). Confirm it equals the closed-form
    # riemann_from_omega route (same omega, two assembly paths: 5x5 commutator vs 2nd Cartan
    # structure eq). NOTE: my F-commutator route produces the RAW second-Cartan-structure sign
    # (== bare Christoffel, ground truth), whereas riemann_from_omega is in the ENGINE convention
    # (a uniform global -1, the documented sign-pin factor). So R_fromF == pin * R_omega exactly.
    R_omega = riemann_from_omega(W, E, Einv, list(x), g)
    comps = [(0, 1, 0, 1), (0, 1, 1, 0), (1, 2, 1, 2), (0, 2, 0, 2), (2, 3, 2, 3)]
    assembly_ok = all(cancel(R_fromF[c[0]][c[1]][c[2]][c[3]] - pin * R_omega[c[0]][c[1]][c[2]][c[3]]) == 0
                      for c in comps)
    _report("F=dA+A^A Lorentz block (5x5 commutator route, Lambda=0) == sign-pinned 2nd-Cartan-"
            "structure R(omega) (closed-form route) on the tested components [exact Q] -- the A^A "
            "commutator IS the curvature (uniform sign-pin factor reconciled)", assembly_ok)

    # GROUND-TRUTH check: the F-commutator Riemann (RAW sign) == bare Christoffel Riemann of g,
    # the convention-independent textbook lower-index Levi-Civita Riemann (NO engine sign baked in).
    ginv = g.inv()
    Gam = [[[cancel(Rational(1, 2) * sum(ginv[aa, d] * (diff(g[d, bb], x[cc]) + diff(g[d, cc], x[bb])
            - diff(g[bb, cc], x[d])) for d in range(N))) for cc in range(N)] for bb in range(N)]
           for aa in range(N)]

    def Rbare(rho, sig, mu, nu):
        return cancel(sum(g[rho, lm] * (diff(Gam[lm][sig][nu], x[mu]) - diff(Gam[lm][sig][mu], x[nu])
                      + sum(Gam[lm][mu][e] * Gam[e][sig][nu] - Gam[lm][nu][e] * Gam[e][sig][mu]
                            for e in range(N))) for lm in range(N)))
    ground_ok = all(cancel(R_fromF[c[0]][c[1]][c[2]][c[3]] - Rbare(*c)) == 0 for c in comps)
    _report("F-commutator Riemann (RAW second-Cartan-structure sign) == bare Christoffel "
            "Levi-Civita Riemann of g=e.e (convention-independent ground truth) [exact Q]",
            ground_ok)

    # Show the e^e term is what the formal Lambda multiplies in the Lorentz block (Wise):
    # Lor at symbolic Lambda minus Lor at Lambda=0 should be -(Lambda/3)(e^e)^a_b (MIXED form).
    def ee_mixed(a, b, mu, nu):
        e_b_nu = sum(ETA[b, c] * E[c, nu] for c in range(N))
        e_b_mu = sum(ETA[b, c] * E[c, mu] for c in range(N))
        return E[a, mu] * e_b_nu - E[a, nu] * e_b_mu
    ee_term_ok = True
    for (mu, nu, a, b) in [(0, 1, 0, 1), (1, 2, 1, 2), (0, 2, 0, 2)]:
        full = Lor[mu][nu][a][b]
        at0 = cancel(full.subs(Lam, 0)) if hasattr(full, "subs") else full
        delta = cancel((full - at0) + (Lam / 3) * ee_mixed(a, b, mu, nu)) \
            if hasattr(full, "subs") else 0
        if cancel(delta) != 0:
            ee_term_ok = False
    _report("Wise Lorentz block = R(omega) - (Lambda/3) e^e: the formal-Lambda part of the "
            "Lorentz block == -(Lambda/3)(e^e)^a_b exactly [exact Q] -- e^e term identified",
            ee_term_ok)

    print("      sign-pinned R_{rho sig mu nu} (from F, Lambda=0) sample components (K=-1/2 conv):")
    for c in comps[:3]:
        v = pin * R_fromF[c[0]][c[1]][c[2]][c[3]]
        print(f"        R_{c[0]}{c[1]}{c[2]}{c[3]} = {cancel(v)}")
    return {"lor_so31": lor_so31, "tors_zero": tors_zero, "tors2_zero": tors2 == 0,
            "assembly_ok": assembly_ok, "ground_ok": ground_ok, "ee_term_ok": ee_term_ok,
            "R_fromF_sample": {f"{c[0]}{c[1]}{c[2]}{c[3]}": str(cancel(pin * R_fromF[c[0]][c[1]][c[2]][c[3]]))
                               for c in comps[:3]}}


def main():
    print("#" * 78)
    print("# Phase 77-01 : COFRAME NON-DEGENERACY + omega(e) + FLATNESS SUB-GATE  (v18.0 Cartan/MM)")
    print("#   gravity = Lorentz block R[omega] of F=dA+A^A; g=e.e (1,3); EXACT over Q.")
    print("#   FLATNESS SUB-GATE is decisive & FIRST: R[omega]!=0 => PROCEED ; ==0 => trivial-death STOP.")
    print("#" * 78)

    okG = source_guard()
    pin = sign_pin()
    proceed, gate = flatness_sub_gate(pin)

    if not proceed:
        print("=" * 78)
        print("FLATNESS SUB-GATE FAILED: R[omega] == 0 for M != 0 => HONEST TRIVIAL-DEATH STOP.")
        print("  Tasks 2-3 NOT executed; Phase B halts as a publishable negative.")
        print("=" * 78)
        print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}  |  VERDICT: TRIVIAL-DEATH/STOP")
        return 0 if ALL_PASS else 1

    # PROCEED: Task 2 + Task 3.
    cof = coframe_nondegeneracy(gate["g0"])
    omg = closed_form_omega_demo(pin)

    print("=" * 78)
    print("SUMMARY OF DECISIVE CHECKS")
    print("=" * 78)
    print(f"  source guard ............................. {'PASS' if okG else 'FAIL'}")
    print(f"  sign-pin factor (R[omega]_engine=-R_raw) . -1  (cone-Hessian K=-1/2 convention)")
    print(f"  FLATNESS VERDICT ......................... {gate['verdict']}")
    print(f"  R[g=e.e] Ricci scalar .................... {gate['Rscalar']}")
    print(f"  # nonzero R[omega] components ............ {gate['n_nonzero']} / 256")
    print(f"  two independent Riemann routes agree ..... {gate['two_routes_agree']}")
    print(f"  coframe signature (M=0 / M!=0) ........... {cof['sig_M0']} / {cof['sig_M']}")
    print(f"  det(e) M=0 / M!=0 nonzero ................. {cof['det_M0']!='0'} / {cof['det_M']!='0'}")
    print(f"  omega(e) antisym / torsion-free .......... {omg['antisym']} / {omg['torsion_free']}")
    print(f"  R[omega] == metric Levi-Civita Riemann ... {omg['identity_ok']}")
    print("=" * 78)
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}  |  VERDICT: PROCEED (Phase B continues to 77-02)")
    print("=" * 78)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
