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
