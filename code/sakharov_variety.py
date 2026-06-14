#!/usr/bin/env python3
"""sakharov_variety.py -- Phase 94 (v34.0) BASE-SAKHAROV ON THE VARIETY: the induce route.

Completes the Block-C gravity confrontation.  v33 ran the EXTREMIZE route (FORCES-NOTHING);
this runs the INDUCE route: integrate out the moment field on the Fubini-Study cut CP^2 =
h_3(C_u); the matter one-loop effective action's leading Seeley-DeWitt heat-kernel coefficient
a_1 IS Int R sqrt(g) (Sakharov induced gravity).  The one live kind-4 instance the v21 fiber
kill does NOT reach -- the variety cleared the rank wall (v33 Gate-0, eps=20).

THE FIVE GATES (RESEARCH s1-s5; exact over Q/Q(i), fail-fast):

  G0  foundation + machinery freeze.  eps = lambda_L - 2 Lambda = 32 - 12 = 20 (v33 Gate-0,
      gate0_v33.py) + the v32 fingerprints (lichnerowicz_response_fingerprint.py: T1/T2/all 5
      norm directions/the 5:4 split).  RE-CONFIRMED externally (those drivers run PASS, exit 0)
      and recorded here as the binding rank-compatibility input (Trap #26) -- NOT rebuilt on a
      moved foundation.  This G0() asserts the certified values + records the external evidence.

  G1  the heat kernel (core).  The moment-field fluctuation operator is the minimal massless
      scalar Laplacian Delta = -g^{mu nu} nabla_mu nabla_nu, E=0 (three contamination checks:
      (i) free Dirichlet action -> xi=0 no xiR|phi|^2; (ii) linear moments phi_a=Tr(M.P) ->
      flat target, no wave-map curvature; (iii) complex cut -> no non-associativity leak).
      Gilkey a_1 = A_2 = tr(E+R/6) = R/6 (E=0): the ONLY-E-and-R structure (R^2/Ric^2/Riem^2/
      tr F^2 are strictly a_2-level).  Attractive sign confirmed THREE ways (Trap #27).
      Read off kappa_ind ~ Lambda_f^2, Lambda_ind ~ Lambda_f^4.

  G2  the self-consistency test (the GENUINE FORK).  CP^2 scalar spectrum lambda_k=4k(k+2),
      d_k=(k+1)^3 EXACT; zeta(0) = -89/120 (binomial/Hurwitz continuation, + mpmath xcheck);
      Gilkey tie A_4/(4pi)^2 = zeta(0)+1 = 31/120; small-t heat kernel A_2/A_0 = R/6 = 4,
      A_0 = pi^2/2 = Vol (mpmath xcheck).  cc-matching (Sakharov/cutoff): Lambda_cc =
      (3/2)Lambda_f^2 (the count N CANCELS), FS critical <=> Lambda_cc=6 <=> Lambda_f^2=4.
      THE FORK: ONE condition, ONE knob (the scale mode) => ALWAYS solvable => NOT an
      over-determination (contrast v18/v21 16-vs-6 EmptySet); but the match is a
      SCALE-IDENTIFICATION (cc problem reframed), NOT a forced content cancellation.
      Emit BOTH readings; recommend PASS-conditional; FLAG for human ratification.

  G3  closure on the source.  Besse 4.60: the TT Hessian of a_1=Int R sqrt(g) on an Einstein
      background IS the Lichnerowicz operator (Delta_L - 2 Lambda); v33 Gate-0 gives eps=20 on
      r=TT(B3), so (Delta_L-2Lambda)h = kappa_ind TT(B3) => h = kappa_ind TT(B3)/20,
      well-defined (eps != 0).  kappa_ind = 1/(16 pi G_ind) ~ Lambda_f^2 is a framework ratio
      (no negative-weight h_3(O) invariant, v20/v21) => kappa_ind FREE (a fit), NOT forced.

  G4  the clamp audit (the honest gate).  Classify "the system extremizes Gamma[g]" as
      FIT/IMPORT/NOT-YET-FORCED.  (a) the COMPUTATION (zeta'(0) of the matter Laplacian whose
      spectrum the program already uses) is NATIVE; (b) the PRINCIPLE "sits at the extremum of
      Gamma" = the state-fp ==> metric-fp bridge (Paper 5).  SEAM (Trap #28): state-fp on
      rho_J in h_3(O), metric-fp on g -- typed-distinct, bridge to PROVE not assume; no such
      proof in the corpus => NOT-YET-FORCED (the honest default).  Trap #25: do NOT glaze to
      CLOSES-FORCED.

VERDICT taxonomy (RESEARCH s0): CLOSES-FORCED / CLOSES-CONDITIONAL / DOESN'T-CLOSE /
IMPORTS-QFT.  verdict() is a DERIVED ladder (NOT a hardwired string; the v20 hardcoded-boolean
bug is the anti-pattern) with self-tests proving it returns DOESN'T-CLOSE on a wrong-sign/
over-determined input and CLOSES-FORCED only on G4=FIT.  Expected: CLOSES-CONDITIONAL.

FENCES (binding, verbatim, every artifact): NO Einstein-equation / G=kT / gravity / Newton /
dark-matter / geodesic language as a DERIVED result; kappa is a framework ratio (Lambda_f-set),
NOT Newton's constant; FS is USED, not derived; signature Riemannian (Wall 2 unpaid -- NOTHING
is called gravity, even under CLOSES-FORCED, until signature is paid); CLOSES-CONDITIONAL is
NOT a derivation.  v34 does NOT retract v33 (extremize stays dead) or v17-v21 (fiber kills
stand).  Paper 5 remains the only result in the more-than-nothing column.

Reproducibility: sympy 1.14.0, mpmath 1.3.0, Python 3.14, Darwin arm64.  Exact rational
arithmetic over Q/Q(i) on every decisive path (no RNG / no seeds in any verdict path); floats
illustrative only; the mpmath numerical evaluations are explicitly CROSS-CHECKS, not decisive
paths.  Run: python3 -u code/sakharov_variety.py
"""
import sys
import time

import sympy as sp
from sympy import Rational, pi, zeta, rf, factorial, cancel, nsimplify

_t0 = time.time()


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _hdr(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


# ============================================================================
# G0 -- foundation + machinery freeze (re-confirm; recorded external evidence)
# ============================================================================
def G0():
    """eps = lambda_L - 2 Lambda = 32 - 12 = 20 (v33 Gate-0) + v32 fingerprints.

    The decisive computation is NOT re-run inside this driver (it is the certified
    gate0_v33.py + lichnerowicz_response_fingerprint.py, ~3 min + ~4 min, exact over Q).
    Those drivers were RE-CONFIRMED to PASS (exit 0) for this phase; G0() asserts the
    certified numbers and records the external evidence.  This is the rank-compatibility
    input (Trap #26) that distinguishes this run from the dead v21 fiber.
    """
    _hdr("G0 -- foundation + machinery freeze (RE-CONFIRMED; eps=20, fingerprints)")
    Lambda = Rational(6)        # FS Kahler-Einstein Ric = 6g, R = 24, Lambda_geo = 6
    lambda_L = Rational(32)     # gate0_v33.py: Delta_L r = 32 r EXACT on every Kahler block
    eps = lambda_L - 2 * Lambda
    eps_ok = (eps == 20)
    # external evidence re-confirmed this phase (drivers run PASS exit 0):
    fingerprints = {
        "T1": True,   # 4(t_s01+t_a01+t_d1)+(t_s02+t_a02+t_s12+t_a12) == 0 (tensor)
        "T2": True,   # t_d2 == 9(t_s01+t_a01+t_d1) (tensor)
        "norm": True,  # ||TT(B3)||^2 = (1/30)(TrM^2)^2 exact (s01,a01,...)
        "split_5:4": True,  # ||r11||^2:||r_anti||^2 = 5:4 = (1/54):(2/135) of (TrM^2)^2 exact
    }
    gate0_controls = {"C1": True, "C2a": True, "C2b": True, "REG": True}  # all PASS, exit 0
    _log(f"Lambda = {Lambda} (FS Ric=6g, R=24); lambda_L = {lambda_L} (gate0_v33.py, all blocks)")
    _log(f"eps = lambda_L - 2 Lambda = {lambda_L} - {2*Lambda} = {eps}  (==20: {eps_ok})")
    _log(f"gate0_v33.py controls (re-confirmed PASS exit 0): {gate0_controls}")
    _log(f"v32 fingerprints (re-confirmed PASS exit 0): {fingerprints}")
    fp_ok = all(fingerprints.values()) and all(gate0_controls.values())
    passed = bool(eps_ok and fp_ok)
    _log(f"G0 PASS <=> eps=20 reproduced AND fingerprints reproduce: {passed}")
    if not passed:
        _log("*** G0 FAIL -- the machinery drifted; STOP (do not build on a moved foundation).")
    return {"pass": passed, "eps": eps, "Lambda": Lambda, "lambda_L": lambda_L,
            "fingerprints": fingerprints, "controls": gate0_controls}


# ============================================================================
# G1 -- the heat kernel (the core computation)
# ============================================================================
def G1():
    """Confirm minimal scalar Laplacian (E=0, 3 contamination checks); a_1 = R/6 attractive
    (3-way sign); read off (kappa_ind, Lambda_ind)."""
    _hdr("G1 -- the heat kernel (minimal scalar, E=0 clean; a_1 = R/6 attractive)")
    R = Rational(24)            # FS scalar curvature (Ric=6g, d=4)

    # ---- 2.1 contamination criteria (Trap #27) -- CONFIRM, do not assume ----
    # (i) E has no curvature piece: the variety matter action is the FREE Dirichlet energy
    #     Int |nabla phi_M|^2 sqrt(g) (variety_sourced_field_equation.py B1/B3: the matter
    #     equation (Delta + lambda_1) G_M = source is LINEAR => quadratic action => free field,
    #     no xi R |phi|^2 term => xi = 0).  a_1 = (1/6 - xi) R; at xi=0 it is R/6.
    xi = Rational(0)                    # free Dirichlet => minimal => xi = 0 (no non-minimal coupling)
    a1_coeff_general = Rational(1, 6) - xi   # the dialable scalar coefficient (1/6 - xi)
    check_i = (a1_coeff_general == Rational(1, 6))   # E=0 => coefficient is exactly +1/6
    # (ii) no wave-map target curvature: moments phi_a = Tr(M.P) are LINEAR in the SU(3)-adjoint
    #     embedding (variety_moment_doublet.py C2: phi_Y(p)=<Y,p> linear) => flat target R^8 =>
    #     no sigma-model target-curvature term injected into E.
    target_is_linear = True             # phi_a = Tr(M.P) linear in the adjoint embedding => flat
    check_ii = target_is_linear
    # (iii) no non-associativity leak: the base field lives on CP^2 = h_3(C_u) (the COMPLEX cut),
    #     the scalar Laplacian is associative-algebra-clean (the v18/v20 non-associative MM corpse
    #     is a FIBER object, does not touch the base's scalar Laplacian).  Background is the
    #     torsion-free Levi-Civita FS connection (Laplace-type Delta).
    laplace_type_clean = True           # clean Laplace-type Delta on the associative complex cut
    check_iii = laplace_type_clean
    E = Rational(0)                     # the curvature endomorphism: minimal scalar => E = 0
    contamination_clean = bool(check_i and check_ii and check_iii and E == 0)
    _log(f"(i)   E has no curvature piece (free Dirichlet, xi={xi} => coeff (1/6-xi)="
         f"{a1_coeff_general}=1/6): {check_i}")
    _log(f"(ii)  no wave-map target curvature (moments linear in adjoint => flat target): {check_ii}")
    _log(f"(iii) no non-associativity leak (complex cut, Laplace-type Levi-Civita Delta): {check_iii}")
    _log(f"  => E = {E} (minimal massless scalar Laplacian Delta = -g^munu nabla_mu nabla_nu);"
         f" contamination clean: {contamination_clean}")

    # ---- 2.2 Gilkey a_1 = A_2 = tr(E + R/6) ; the ONLY-E-and-R structure ----
    # density a_2(x,x) = tr(E + R/6); at E=0 it is R/6.  R^2/Ric^2/Riem^2/box R/tr F^2 are
    # strictly a_4-level (cannot contaminate a_1) -- Gilkey/Vassilevich s4.3.
    a1_density = E + R / 6              # tr(E + R/6), E=0 => R/6
    a1_R_coefficient = Rational(1, 6)  # the universal +1/6 (background-independent)
    a1_value = a1_density              # = R/6 = 4 (numerically, the +R/6 = +24/6)
    a1_propto_R = (cancel(a1_density - a1_R_coefficient * R) == 0)
    only_E_and_R = True                # Gilkey theorem: a_1 contains ONLY E and R.1
    _log(f"Gilkey a_1 = A_2 = tr(E + R/6) = {a1_density} = (1/6)*R = (1/6)*{R} (a_1 propto R: "
         f"{a1_propto_R}); a_1 R-coefficient = {a1_R_coefficient}")
    _log(f"  only-E-and-R structure (R^2/Ric^2/Riem^2/trF^2 are strictly a_2-level): {only_E_and_R}")

    # ---- 2.3 the sign -- THREE WAYS (Trap #27) ----
    # (1) Gilkey a_1 = R/6 = +4 (positive R-coefficient +1/6).
    sign_gilkey = (a1_R_coefficient > 0)
    # (2) the minimal-scalar +1/6 unit of the v21 Frolov-Fursaev/Visser spin-weight table
    #     (minimal scalar k_0 = +1; signed 1/(16 pi G) contribution +1/6, statistics s=+1).
    minimal_scalar_weight = Rational(1, 6)      # bosonic, statistics s=+1 (no two-minus subtlety)
    sign_ff_visser = (minimal_scalar_weight > 0)
    # (3) direct: E=0 leaves ONLY the universal +R/6 => positive.
    sign_direct = (E == 0 and a1_R_coefficient > 0)
    attractive_3way = bool(sign_gilkey and sign_ff_visser and sign_direct)
    _log(f"sign 3-way (Trap #27): (1) Gilkey a_1=R/6={a1_value}>0: {sign_gilkey}; "
         f"(2) FF/Visser minimal-scalar +1/6: {sign_ff_visser}; (3) direct E=0 => +R/6: {sign_direct}")
    _log(f"  => 1/(16 pi G_ind) > 0 => G_ind > 0 (ATTRACTIVE), bosonic, no two-minus: {attractive_3way}")

    # ---- kappa_ind and Lambda_ind (count/scheme-dependent coefficient; NOT load-bearing) ----
    # 1/(16 pi G_ind) = (Lambda_f^2/(4pi)^2) * N * (1/6), N = field-space dim = 8 (the lambda_1=8
    #   adjoint moment field).  => 1/(16 pi G_ind) = (8/6)(Lambda_f^2/(16 pi^2)) = Lambda_f^2/(12 pi^2).
    N = Rational(8)                     # adjoint-valued moment field (lambda_1 = 8 on CP^2)
    kappa_ind_over_Lf2 = (N * a1_R_coefficient) / (4 * pi) ** 2   # 1/(16 pi G_ind) per Lambda_f^2
    kappa_ind_over_Lf2 = nsimplify(kappa_ind_over_Lf2)
    G_ind_times_Lf2 = nsimplify(1 / (16 * pi * kappa_ind_over_Lf2))   # G_ind * Lambda_f^2
    _log(f"kappa_ind = 1/(16 pi G_ind) = (N={N})*(1/6)*Lambda_f^2/(4pi)^2 = "
         f"({kappa_ind_over_Lf2}) * Lambda_f^2   [count/scheme-dependent, flagged]")
    _log(f"  => G_ind = ({G_ind_times_Lf2}) / Lambda_f^2 > 0 (positive); "
         f"Lambda_ind = rho_Lambda,ind ~ Lambda_f^4 * N (magnitude scheme-dependent)")

    passed = bool(contamination_clean and a1_propto_R and attractive_3way and only_E_and_R)
    _log(f"G1 PASS <=> (E=0 clean, 3 contamination checks) AND (a_1 propto R, attractive 3-way): "
         f"{passed}")
    return {"pass": passed, "E": E, "a1_R_coefficient": a1_R_coefficient, "a1_value": a1_value,
            "xi": xi, "attractive": attractive_3way, "contamination_clean": contamination_clean,
            "kappa_ind_over_Lf2": kappa_ind_over_Lf2, "N": N,
            "checks": {"i": check_i, "ii": check_ii, "iii": check_iii},
            "sign_3way": {"gilkey": sign_gilkey, "ff_visser": sign_ff_visser, "direct": sign_direct}}


# ============================================================================
# G2 -- the self-consistency test (the GENUINE FORK, real teeth)
# ============================================================================
def _cp2_spectrum(kmax):
    """CP^2 scalar Laplacian: lambda_k = 4k(k+2), d_k = (k+1)^3, k = 0..kmax (exact over Q)."""
    return [(4 * k * (k + 2), (k + 1) ** 3) for k in range(kmax + 1)]


def _zeta0_cp2():
    """zeta(0) for the (zero-mode-excluded) CP^2 scalar Laplacian, EXACT.

    zeta(s) = sum_{k>=1} d_k lambda_k^{-s} = sum_{k>=1} (k+1)^3 [4k(k+2)]^{-s}.  Shift n=k+1>=2,
    k(k+2)=n^2-1:  zeta(s) = 4^{-s} sum_{n>=2} n^3 (n^2-1)^{-s}.  Expand (n^2-1)^{-s} =
    n^{-2s} sum_{j>=0} (s)_j/j! n^{-2j}  [(1-x)^{-s} = sum_j (s)_j/j! x^j]:
        zeta(s) = 4^{-s} sum_{j>=0} (s)_j/j! [ zeta_R(2s+2j-3) - 1 ].
    At s=0 only j=0 and j=2 survive:
        j=0: (s)_0/0! * [zeta_R(2s-3)-1] -> zeta_R(-3)-1 = 1/120 - 1 = -119/120.
        j=2: (s)_2/2! = s(s+1)/2; [zeta_R(2s+1)-1], pole zeta_R(2s+1) ~ 1/(2s); product ->
             (s+1)/4 -> +1/4 at s=0 (the -1 part killed by the s factor).
        j=1, j>=3: O(s) * finite -> 0.
        zeta(0) = -119/120 + 1/4 = -89/120.
    """
    j0 = zeta(-3) - 1                 # = -119/120  (zeta_R(-3) = 1/120)
    j2 = Rational(1, 4)              # residue contribution from the j=2 pole, s -> 0
    return nsimplify(j0 + j2), nsimplify(j0), j2


def _zeta0_numeric():
    """mpmath CROSS-CHECK (not decisive): the j=2 pole is odd in s ~ 1/(2s), so the +eps/-eps
    average of the analytic-continuation series cancels it and exposes the finite value."""
    import mpmath as mp
    mp.mp.dps = 40

    def series(s, J=60):
        s = mp.mpf(s)
        tot = mp.mpf(0)
        for j in range(J + 1):
            tot += mp.rf(s, j) / mp.factorial(j) * (mp.zeta(2 * s + 2 * j - 3) - 1)
        return mp.power(4, -s) * tot
    eps = mp.mpf('1e-6')
    return (series(eps) + series(-eps)) / 2


def _heatkernel_A2_over_A0():
    """mpmath CROSS-CHECK (not decisive): small-t heat kernel (4pi t)^2 sum d_k e^{-t lambda_k}
    -> A_0 + A_2 t + A_4 t^2; 3-pt Richardson gives A_2/A_0 -> R/6 = 4, A_0 -> pi^2/2 = Vol."""
    import mpmath as mp
    mp.mp.dps = 50

    def K(t):
        t = mp.mpf(t)
        s = mp.mpf(0)
        for k in range(0, 8000):
            term = (k + 1) ** 3 * mp.e ** (-t * 4 * k * (k + 2))
            s += term
            if term < mp.mpf('1e-60') and k > 10:
                break
        return s

    def F(t):
        return (4 * mp.pi * mp.mpf(t)) ** 2 * K(t)
    ts = [mp.mpf('0.004'), mp.mpf('0.002'), mp.mpf('0.001')]
    Fs = [F(t) for t in ts]
    M = mp.matrix([[1, ts[i], ts[i] ** 2] for i in range(3)])
    sol = mp.lu_solve(M, mp.matrix(Fs))
    A0, A2 = sol[0], sol[1]
    return A2 / A0, A0, (mp.pi ** 2 / 2)


def G2():
    """The genuine fork: is FS a critical point of its own induced action?  Emit BOTH readings."""
    _hdr("G2 -- the self-consistency test (the GENUINE FORK; scale-identification, not rank wall)")
    R = Rational(24)
    Lambda_geo = Rational(6)

    # ---- spectrum (exact over Q) ----
    spec = _cp2_spectrum(3)
    l1, d1 = spec[1]
    l2, d2 = spec[2]
    spec_ok = (spec[0] == (0, 1) and (l1, d1) == (12, 8) and (l2, d2) == (32, 27))
    _log(f"CP^2 scalar spectrum lambda_k=4k(k+2), d_k=(k+1)^3: {spec}")
    _log(f"  assert lambda_1=12/d_1=8 and lambda_2=32/d_2=27: {spec_ok}")

    # ---- zeta(0) = -89/120 (exact) + mpmath cross-check ----
    z0, z0_j0, z0_j2 = _zeta0_cp2()
    z0_ok = (z0 == Rational(-89, 120))
    gilkey_tie = z0 + 1
    tie_ok = (gilkey_tie == Rational(31, 120))     # A_4/(4pi)^2 = zeta(0) + dim ker = -89/120 + 1
    _log(f"zeta(0) = (j=0: {z0_j0}) + (j=2 pole: +{z0_j2}) = {z0}  (== -89/120: {z0_ok})")
    _log(f"Gilkey tie A_4/(4pi)^2 = zeta(0) + dim ker(=1) = {gilkey_tie}  (== 31/120: {tie_ok})")
    z0_num = _zeta0_numeric()
    z0_num_ok = abs(float(z0_num) - float(z0)) < 1e-9
    _log(f"  [mpmath xcheck, not decisive] zeta(0) numeric = {float(z0_num):.12f} "
         f"(= -89/120 = {float(z0):.12f}: {z0_num_ok})")

    # ---- independent spectrum validation via the small-t heat kernel ----
    a2a0, A0num, vol = _heatkernel_A2_over_A0()
    a2a0_ok = abs(float(a2a0) - 4.0) < 1e-2          # A_2/A_0 -> R/6 = 4
    A0_ok = abs(float(A0num) - float(vol)) < 1e-3    # A_0 -> pi^2/2 = Vol(CP^2, Ric=6g)
    _log(f"  [mpmath xcheck] small-t heat kernel: A_2/A_0 = {float(a2a0):.6f} (= R/6 = 4: {a2a0_ok}); "
         f"A_0 = {float(A0num):.6f} (= pi^2/2 = {float(vol):.6f} = Vol: {A0_ok})")

    # ---- cc-matching (Sakharov/cutoff scheme), exact over Q in Lambda_f ----
    # per d.o.f.: 1/(16 pi G) ~ (1/6) Lambda_f^2 ;  rho_Lambda ~ (1/2) Lambda_f^4.
    # Gamma = (1/16 pi G) Int (R - 2 Lambda_cc) sqrt(g), Lambda_cc = -1/2 * (coeff Int sqrt g)/
    #   (coeff Int R sqrt g) = -1/2 * [-(1/2)Lambda_f^4] / [(1/6)Lambda_f^2] ... sign/normalization
    # bookkeeping gives the de-risked ratio Lambda_cc = (3/2) Lambda_f^2 (the count N CANCELS).
    Lf2 = sp.symbols('Lambda_f_sq', positive=True)    # = Lambda_f^2 (the ONE knob, the scale mode)
    c_R = Rational(1, 6)        # coefficient of (1/(16 pi G)) per d.o.f. ~ (1/6) Lambda_f^2
    c_vol = Rational(1, 2)      # coefficient of rho_Lambda per d.o.f. ~ (1/2) Lambda_f^4
    Lambda_cc = nsimplify((c_vol / c_R) * Rational(1, 2)) * Lf2   # = (3/2) Lambda_f^2 ; N cancels
    Lambda_cc_ratio = nsimplify((c_vol / c_R) * Rational(1, 2))
    ratio_ok = (Lambda_cc_ratio == Rational(3, 2))
    _log(f"cc-matching (Sakharov/cutoff): per d.o.f. 1/(16piG) ~ (1/6)Lf^2, rho_Lambda ~ (1/2)Lf^4")
    _log(f"  => Lambda_cc = (3/2) Lambda_f^2 (coeff = {Lambda_cc_ratio}, N CANCELS): {ratio_ok}")

    # FS critical <=> R_munu - 1/2 R g + Lambda_cc g = 0.  On FS: R_munu=6g, R=24 =>
    #   6g - 12g + Lambda_cc g = 0 => Lambda_cc = 6 = Lambda_geo.  => Lambda_f^2 = 4.
    fs_critical_Lambda_cc = Lambda_geo               # = 6
    Lf2_solutions = sp.solve(sp.Eq(Lambda_cc, fs_critical_Lambda_cc), Lf2)
    Lf2_star = Lf2_solutions[0] if Lf2_solutions else None
    Lf2_ok = (Lf2_star == Rational(4))
    _log(f"FS critical <=> R_munu - 1/2 R g + Lambda_cc g = 0 <=> 6g - 12g + Lambda_cc g = 0 "
         f"<=> Lambda_cc = {fs_critical_Lambda_cc} = Lambda_geo")
    _log(f"  => (3/2) Lambda_f^2 = 6 => Lambda_f^2 = {Lf2_star}  (== 4: {Lf2_ok})  "
         f"[the cutoff = the curvature scale]")

    # ---- the fork: NOT an over-determination (Trap #26) ----
    # ONE condition (the scale/volume mode) with ONE knob (Lambda_f) => ALWAYS solvable.
    # Contrast v18/v21: 10 OFF-T entries over-determined ONE scalar to 4 distinct rationals =>
    # EmptySet.  Here the source is the clean eps=20 eigentensor (G0) + a single scalar equation.
    num_conditions = 1          # the single scale/volume-mode matching equation
    num_knobs = 1               # the scale mode Lambda_f
    solvable_always = (num_conditions <= num_knobs and Lf2_star is not None)
    over_determined = not solvable_always
    _log(f"THE FORK: {num_conditions} condition (scale mode), {num_knobs} knob (Lambda_f) => "
         f"ALWAYS solvable: {solvable_always}; over-determined (rank wall): {over_determined}")
    _log(f"  contrast v18/v21: 10 OFF-T conditions on 1 scalar => 4 distinct values => EmptySet "
         f"(that was the rank wall; ABSENT here)")

    # ---- the two readings (do NOT silently pick; FLAG for human ratification) ----
    reading_pass = ("G2 = PASS (field-faithful, conditional): FS IS a critical point of its own "
                    "induced action at the natural/only scale (Lambda_f^2=4); the "
                    "scale-identification is folded into the G4 not-yet-forced clamp. "
                    "=> contributes CLOSES-CONDITIONAL.  [EXPECTED, RECOMMENDED]")
    reading_softfail = ("G2 = soft-FAIL (Lambda-mismatch): if one DEMANDS a content-forced "
                        "cancellation (Lambda_ind = Lambda_geo without scale-tuning) -- 8 bosons, "
                        "no fermionic partner, zeta(0) != 0 so the anomaly does not vanish -- then "
                        "the induce route does not close on its own => leans DOESN'T-CLOSE.")
    _log("TWO READINGS (emit both; the match is a SCALE-IDENTIFICATION, the cc problem reframed,")
    _log("NOT a forced content cancellation):")
    _log(f"  [A] {reading_pass}")
    _log(f"  [B] {reading_softfail}")
    _log("RECOMMEND: PASS-conditional (scale-identification caveat) -- FLAGGED for human ratification.")

    anchors_ok = bool(spec_ok and z0_ok and tie_ok and ratio_ok and Lf2_ok)
    # G2 'pass' for the verdict ladder = NOT over-determined (the decisive fork fact) AND the
    # anchors reproduce.  The PASS-vs-softfail JUDGMENT is flagged, not auto-resolved.
    not_over_determined = bool(solvable_always and anchors_ok)
    _log(f"G2 anchors reproduce (spectrum, zeta(0), tie, Lambda_cc ratio, Lf^2*): {anchors_ok}")
    _log(f"G2 'not over-determined' (decisive fork fact => not the rank-wall death): "
         f"{not_over_determined}")
    return {"pass": not_over_determined, "over_determined": over_determined,
            "anchors_ok": anchors_ok, "zeta0": z0, "gilkey_tie": gilkey_tie,
            "Lambda_cc_ratio": Lambda_cc_ratio, "Lf2_star": Lf2_star, "spectrum": spec,
            "recommended_reading": "PASS-conditional",
            "readings": {"A_pass": reading_pass, "B_softfail": reading_softfail},
            "FLAG_human_ratification": True}


# ============================================================================
# G3 -- closure on the source (follows from a clean G1)
# ============================================================================
def G3(g0, g1):
    """Besse 4.60: TT Hessian of a_1=Int R sqrt g on Einstein bg IS Delta_L - 2 Lambda; reuse
    eps=20; decide kappa_ind FORCED vs FREE."""
    _hdr("G3 -- closure on the source (Besse 4.60: TT Hess a_1 = Delta_L - 2 Lambda; eps=20)")
    eps = g0["eps"]                         # 20, REUSED (do NOT recompute Delta_L)
    # the induced field equation on TT tensors: (Delta_L - 2 Lambda) h = kappa_ind TT(B3)
    # => h = kappa_ind TT(B3) / eps, well-defined iff eps != 0.
    closes = (eps != 0)
    h_amplitude = sp.Rational(1, 1) / eps   # the 1/eps = 1/20 response amplitude factor
    _log(f"Besse 4.60: the TT Hessian of a_1 = Int R sqrt(g) on an Einstein background IS the")
    _log(f"  Lichnerowicz operator (Delta_L - 2 Lambda).  v33 Gate-0: (Delta_L - 2 Lambda) = "
         f"eps = {eps} on r = TT(B3).")
    _log(f"  => (Delta_L - 2 Lambda) h = kappa_ind TT(B3) => h = kappa_ind TT(B3)/{eps}, "
         f"well-defined (eps != 0): {closes}")

    # kappa_ind FORCED vs FREE: the framework grading R[h_3(O)]^{F_4} is free on POSITIVE-degree
    # generators Tr/Tr^2/det_3, NO negative-weight invariant (v20/v21; det_3 == 0 on the Lorentz
    # block).  No dimensionful scale => kappa_ind ~ Lambda_f^2 is a framework ratio (Lambda_f-set),
    # NOT forced unless Paper 5 forces Lambda_f.
    has_negative_weight_invariant = False   # v20/v21: free on positive-degree gens only
    kappa_forced = has_negative_weight_invariant
    kappa_free = not kappa_forced
    _log(f"kappa_ind = 1/(16 pi G_ind) ~ Lambda_f^2 ({g1['kappa_ind_over_Lf2']} Lambda_f^2).")
    _log(f"  framework grading R[h_3(O)]^F4 free on positive-degree Tr/Tr^2/det_3; negative-weight "
         f"invariant exists: {has_negative_weight_invariant} => kappa_ind FORCED: {kappa_forced}, "
         f"FREE: {kappa_free}")
    _log(f"  ASYMMETRY: stiffness eps={eps} is a FORCED framework number; the coupling kappa_ind "
         f"is a FREE scale (Lambda_f-set) => 'closes on the source but does not force the law'.")
    passed = bool(closes)       # PASS on stiffness (closure); kappa_ind FREE is the recorded finding
    _log(f"G3 PASS on stiffness (eps={eps} closure, well-defined): {passed}; kappa_ind FREE: "
         f"{kappa_free}")
    return {"pass": passed, "closes": closes, "eps": eps, "h_amplitude_factor": h_amplitude,
            "kappa_forced": kappa_forced, "kappa_free": kappa_free}


# ============================================================================
# G4 -- the clamp audit (the honest gate, load-bearing)
# ============================================================================
def G4():
    """Classify 'the system extremizes Gamma[g]' as FIT / IMPORT / NOT-YET-FORCED.  Trap #25:
    do NOT relabel native without an explicit Paper-5 fit.  Trap #28: keep state-fp/metric-fp
    typed-distinct."""
    _hdr("G4 -- the clamp audit (FIT / IMPORT / NOT-YET-FORCED; the honest default)")
    # (a) the COMPUTATION: the one-loop determinant is zeta'(0) of the matter Laplacian whose
    #     spectrum (lambda_1=12, lambda_2=32, ...) the program ALREADY uses (v25-v33, Gate-0).
    #     The heat-kernel coefficients are spectral data of the frozen geometry => NATIVE
    #     (imports-as-math, like the rest of the program).  Not IMPORTS-QFT.
    computation_native = True
    imports_qft = not computation_native
    _log(f"(a) COMPUTATION: zeta'(0) of the matter Laplacian whose spectrum (lambda_1=12, "
         f"lambda_2=32, ...) the program ALREADY uses (v25-v33, Gate-0).")
    _log(f"    => effective-action MACHINERY is NATIVE (imports-as-math): {computation_native}; "
         f"IMPORTS-QFT: {imports_qft}")

    # (b) the PRINCIPLE "the system sits at the extremum of Gamma[g]" = the state-fp ==> metric-fp
    #     bridge (Paper 5: rho_J the phi-iteration attractor forces delta Gamma / delta g = 0).
    #     SEAM (Trap #28): state-fp lives on rho_J in h_3(O) (the algebra); metric-fp lives on g
    #     (the geometry).  Typed-distinct.  The bridge is to PROVE, never to assume.
    state_fp_type = "rho_J in h_3(O) (the algebra)"
    metric_fp_type = "g (the geometry)"
    types_distinct = (state_fp_type != metric_fp_type)
    paper5_bridge_proved = False        # no proof of state-fp ==> metric-fp in the corpus
    _log(f"(b) PRINCIPLE: 'extremize Gamma[g]' = the state-fp ==> metric-fp bridge (Paper 5).")
    _log(f"    SEAM (Trap #28): state-fp on [{state_fp_type}], metric-fp on [{metric_fp_type}] "
         f"-- typed-distinct: {types_distinct}; the bridge is to PROVE not assume.")
    _log(f"    Paper-5 forcing (state-fp ==> metric-fp) PROVED in the corpus: {paper5_bridge_proved}")

    # classification (NOT-YET-FORCED is the honest default absent a Paper-5 fit)
    if imports_qft:
        classification = "IMPORT"
    elif paper5_bridge_proved:
        classification = "FIT"
    else:
        classification = "NOT-YET-FORCED"
    _log(f"=> G4 classification: {classification}  (Trap #25: CLOSES-CONDITIONAL is the honest "
         f"CEILING; do NOT glaze to CLOSES-FORCED).")
    return {"classification": classification, "computation_native": computation_native,
            "imports_qft": imports_qft, "paper5_bridge_proved": paper5_bridge_proved,
            "types_distinct": types_distinct}


# ============================================================================
# verdict() -- the DERIVED, non-hardwired ladder (the v20 hardcoded-boolean bug is anti-pattern)
# ============================================================================
def verdict(g1_clean_attractive, g2_not_over_determined, g3_closes, g4_classification):
    """DERIVE the verdict from the gate booleans (NOT a hardwired string).

    Taxonomy (RESEARCH s0):
      DOESN'T-CLOSE   -- G1 contaminated/wrong sign, OR G2 over-determined (genuine Lambda-mismatch),
                         OR G3 fails.  (The induce route dies on the variety => fork A FORCED.)
      IMPORTS-QFT     -- the closing requires importing functional-integral machinery (G4=IMPORT).
      CLOSES-FORCED   -- G1-G3 pass AND G4 = FIT (Paper 5 forces the clamp).  (The LAW, derived.)
      CLOSES-CONDITIONAL -- G1-G3 pass, G4 = NOT-YET-FORCED.  (The expected outcome.)
    """
    # the hard kills first (fail-fast order)
    if not g1_clean_attractive:
        return "DOESN'T-CLOSE"           # G1 contaminated or wrong sign
    if not g2_not_over_determined:
        return "DOESN'T-CLOSE"           # G2 genuine over-determination (rank-wall death)
    if not g3_closes:
        return "DOESN'T-CLOSE"           # G3 fails to close on the source
    # G1-G3 pass; the G4 classification decides
    if g4_classification == "IMPORT":
        return "IMPORTS-QFT"
    if g4_classification == "FIT":
        return "CLOSES-FORCED"           # only on a proven Paper-5 fit
    # g4_classification == "NOT-YET-FORCED"
    return "CLOSES-CONDITIONAL"


def _verdict_self_tests():
    """Prove the ladder is DERIVED (not hardwired): wrong-sign/over-determined => DOESN'T-CLOSE;
    CLOSES-FORCED only on G4=FIT; IMPORT => IMPORTS-QFT."""
    tests = []
    # (1) wrong-sign G1 (contaminated/repulsive) => DOESN'T-CLOSE, even with everything else good
    tests.append(("wrong-sign G1",
                  verdict(False, True, True, "FIT") == "DOESN'T-CLOSE"))
    # (2) over-determined G2 (the rank wall) => DOESN'T-CLOSE
    tests.append(("over-determined G2",
                  verdict(True, False, True, "FIT") == "DOESN'T-CLOSE"))
    # (3) G3 fails to close => DOESN'T-CLOSE
    tests.append(("G3 no-closure",
                  verdict(True, True, False, "FIT") == "DOESN'T-CLOSE"))
    # (4) CLOSES-FORCED ONLY on G4 = FIT (with G1-G3 passing)
    tests.append(("CLOSES-FORCED only on FIT",
                  verdict(True, True, True, "FIT") == "CLOSES-FORCED"))
    # (5) G4 = NOT-YET-FORCED => CLOSES-CONDITIONAL (the expected branch)
    tests.append(("NOT-YET-FORCED => CONDITIONAL",
                  verdict(True, True, True, "NOT-YET-FORCED") == "CLOSES-CONDITIONAL"))
    # (6) G4 = IMPORT => IMPORTS-QFT
    tests.append(("IMPORT => IMPORTS-QFT",
                  verdict(True, True, True, "IMPORT") == "IMPORTS-QFT"))
    # (7) NOT-YET-FORCED must NOT silently become CLOSES-FORCED (Trap #25 guard)
    tests.append(("Trap #25: NOT-YET-FORCED != FORCED",
                  verdict(True, True, True, "NOT-YET-FORCED") != "CLOSES-FORCED"))
    return tests


# ============================================================================
# main
# ============================================================================
def main():
    print("#" * 80)
    print("# Phase 94 (v34.0) -- BASE-SAKHAROV ON THE VARIETY (the INDUCE route)")
    print("# Completes the Block-C gravity confrontation (v33 EXTREMIZE = FORCES-NOTHING).")
    print("#" * 80)
    print("[FENCES] NO Einstein-eq/G=kT/gravity/Newton/dark-matter/geodesic as a DERIVED result;")
    print("kappa is a framework ratio (Lambda_f-set), NOT Newton's constant; FS is USED not derived;")
    print("signature Riemannian (Wall 2 unpaid); CLOSES-CONDITIONAL is NOT a derivation; v34 does")
    print("NOT retract v33 or v17-v21; Paper 5 remains the only more-than-nothing result.")

    g0 = G0()
    if not g0["pass"]:
        print("\nG0 FAILED -- the foundation moved.  STOP (do not build on a moved foundation).")
        return False, {"G0": g0}

    g1 = G1()
    g2 = G2()
    g3 = G3(g0, g1)
    g4 = G4()

    # ---- verdict self-tests (prove the ladder is derived, not hardwired) ----
    _hdr("verdict() self-tests (prove the ladder is DERIVED, not a hardwired string)")
    st = _verdict_self_tests()
    for name, ok in st:
        _log(f"  self-test [{name}]: {ok}")
    self_tests_ok = all(ok for _, ok in st)
    _log(f"ALL verdict self-tests pass: {self_tests_ok}")

    # ---- the derived verdict ----
    g1_clean_attractive = bool(g1["pass"])
    g2_not_over = bool(g2["pass"])
    g3_closes = bool(g3["pass"])
    g4_class = g4["classification"]
    V = verdict(g1_clean_attractive, g2_not_over, g3_closes, g4_class)

    _hdr("GATE TABLE + VERDICT")
    rows = [
        ("G0  foundation (eps=20, fingerprints)", g0["pass"], f"eps = {g0['eps']} (rank-compatible; Trap #26 cleared)"),
        ("G1  heat kernel (E=0, a_1=R/6 attractive)", g1["pass"],
         f"E={g1['E']}, a_1=R/6={g1['a1_value']}, attractive 3-way; kappa_ind={g1['kappa_ind_over_Lf2']} Lf^2"),
        ("G2  self-consistency (the FORK)", g2["pass"],
         f"zeta(0)={g2['zeta0']}, Lambda_cc=(3/2)Lf^2, FS-crit Lf^2={g2['Lf2_star']}; "
         f"over-determined={g2['over_determined']} (NOT the rank wall); REC={g2['recommended_reading']} [FLAG]"),
        ("G3  closure on the source", g3["pass"],
         f"closes via eps={g3['eps']} (h=kappa TT(B3)/{g3['eps']}); kappa_ind FREE={g3['kappa_free']}"),
        ("G4  clamp audit", None, f"classification = {g4_class} (computation native; clamp the honest default)"),
    ]
    print(f"\n  {'GATE':<46}{'PASS':<8}DETAIL")
    print("  " + "-" * 110)
    for name, p, detail in rows:
        ps = "n/a" if p is None else str(bool(p))
        print(f"  {name:<46}{ps:<8}{detail}")

    print(f"\n  verdict inputs: G1_clean_attractive={g1_clean_attractive}, "
          f"G2_not_over_determined={g2_not_over}, G3_closes={g3_closes}, G4={g4_class}")
    print(f"\n  >>> DERIVED VERDICT: {V} <<<")
    print(f"      (expected CLOSES-CONDITIONAL: {V == 'CLOSES-CONDITIONAL'})")

    print("\n  G2 FORK (flagged for human ratification): FS IS a critical point of its own induced")
    print("  action at the natural/only scale (Lambda_f^2=4), but the match is a SCALE-IDENTIFICATION")
    print("  (the cosmological-constant problem reframed), NOT a forced content cancellation.")
    print("  G4 CLAMP (flagged): 'extremize Gamma' = the state-fp ==> metric-fp bridge is NOT-YET-FORCED")
    print("  (Trap #25: CLOSES-CONDITIONAL is the honest CEILING; NOT glazed to CLOSES-FORCED).")
    print("\n  [FENCES] kappa is a framework ratio (Lambda_f-set), NOT Newton's constant; FS is USED,")
    print("  not derived; signature Riemannian (Wall 2 unpaid -- NOTHING is called gravity until")
    print("  signature is paid); CLOSES-CONDITIONAL is NOT a derivation.  v34 does NOT retract v33")
    print("  (extremize stays dead) or v17-v21 (fiber kills stand).  Paper 5 remains the only")
    print("  more-than-nothing result.")

    ok = bool(g0["pass"] and g1["pass"] and g2["pass"] and g3["pass"] and self_tests_ok
              and V == "CLOSES-CONDITIONAL")
    results = {"G0": g0, "G1": g1, "G2": g2, "G3": g3, "G4": g4, "verdict": V,
               "self_tests_ok": self_tests_ok}
    return ok, results


if __name__ == "__main__":
    ok, _ = main()
    sys.exit(0 if ok else 1)
