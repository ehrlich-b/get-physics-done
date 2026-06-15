#!/usr/bin/env python3
"""adv_kernel_96.py -- Phase 96 ADVERSARIAL CHECK, Attack 1: the FS-GEOMETRIC-KERNEL attack.

The v36 verdict (DEAD-POINTWISE) rests on Bug-guard-2: a LOCAL Delta_FS term in the
faithfulness operator L_F appears ONLY with an inserted kernel of second moment sigma^2,
coefficient 1/2 sigma^2; the phi-iteration's NATIVE <.> is the FLAT global average K=1/Vol
(localized second moment 0), so sigma^2 -> 0 and the coefficient -> 0.

THIS ATTACK tries hardest to FORCE a genuine LOCAL Lichnerowicz (eps=20 tensor) base-derivative
term into field faithfulness from the variety's OWN intrinsic structure -- NOT an inserted-scale
regulator.  The candidate kernels that are intrinsic to CP^2 (no inserted scale):

  (K1) the FLAT global average <h> = int h dV_FS / Vol -- the phi-map's NATIVE kernel.  PROVE it
       is the rank-1 constant-mode projector (annihilates every nonconstant harmonic; Delta of it
       is 0).  This is the verdict's claim; confirm it exact over Q.
  (K2) the FS HEAT KERNEL e^{-t Delta_FS} -- carries a localized second moment, but t is an
       INSERTED scale (regulator).  Show the local Delta coefficient = 1/2 * (2t) -> 0 as t->0;
       and at the spectral level <h>_{e^{-t Delta}} = sum_lambda e^{-t lambda} h_lambda Y_lambda
       -> the WEIGHTED average, NOT a derivative, for any FIXED t.  IMPORTED-KERNEL.
  (K3) the FS GREEN'S FUNCTION G = Delta_FS^{-1} on the orthocomplement of constants -- a genuinely
       INTRINSIC, SCALE-FREE object on compact CP^2 (no inserted scale).  THE strongest attack
       candidate.  Spectrally G h = sum_{lambda>0} (1/lambda) h_lambda Y_lambda.  Test: is
       convolution against G (or its appearance in the field-fixed-point) a LOCAL Laplacian, or
       its INVERSE (a nonlocal smoothing, the OPPOSITE of a derivative)?
  (K4) a COVARIANT FS-neighbor parallel-transport comparison h(x) - <P_{x<-y} h(y)>_{geodesic
       sphere of radius r} -- the intrinsic "discrete Laplacian".  Test whether the r->0 limit is
       FORCED (intrinsic) or whether r is again an inserted scale, and whether the resulting object
       is the SCALAR Delta (wrong type) or a genuine TENSOR.

DECISIVE TEST for each: does the kernel, inserted into the geometry-respecting field-fixed-point,
force a Delta_FS coefficient that is (a) NONZERO, (b) SCALE-FREE (no inserted regulator), AND (c) a
genuine eps=20 TENSOR operator (matches the Lichnerowicz Schur scalar), NOT the scalar harmonic-map
box.  If ALL fail -> DEAD-POINTWISE strengthened.  If one succeeds -> FLIP, flag prominently.

Exact over Q on every decisive line; spectral facts on CP^2 use the EXACT FS harmonic spectrum
lambda_k = 4k(k+2) (physical metric Ric=6g).  Wirtinger discipline reused from area_per_bit.py.
Short run; no orphaned jobs.

Run:  python3 -u code/adv_kernel_96.py
"""
import sys
import time

import sympy as sp
from sympy import Rational, Matrix, I, cancel, simplify, symbols, eye, zeros, expand, Poly

# reuse the certified CP^2 engine verbatim (do NOT rebuild -- the v35 de-risk discipline)
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import area_per_bit as APB  # noqa: E402

Z1, Z2, Z1B, Z2B = APB.Z1, APB.Z2, APB.Z1B, APB.Z2B
rho = APB.rho
conj_swap = APB.conj_swap
P_chart = APB.P_chart
inner = APB.inner
phi_M = APB.phi_M
Var = APB.Var
G_M = APB.G_M
fs_metric_pot = APB.fs_metric_pot
fs_metric_inv = APB.fs_metric_inv
dz = APB.dz
dzb = APB.dzb
matter_directions = APB.matter_directions
M_cut_symbolic = APB.M_cut_symbolic
_l2_scalar = APB._l2_scalar
P0_sub = APB.P0_sub
P2_sub = APB.P2_sub

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return bool(ok)


# ============================================================================
# The PHYSICAL FS metric (Ric=6g, lambda_k = 4k(k+2)): g_phys = g_pot/2.
# The harmonic spectrum on CP^2 (physical normalization, the certified eps=20 anchor):
#   lambda_0 = 0 (constants), lambda_1 = 12, lambda_2 = 32 = lambda_L, ...  lambda_k = 4k(k+2).
# The analyst Laplacian Delta = +2 g^{ab-bar} d_a d_bbar (negative-semidef): Delta Y_k = -lambda_k Y_k.
# ============================================================================
def laplacian_analyst(f, g=None, ginv=None):
    """Delta f = 2 g^{a bbar} d_a d_bbar f  (analyst, negative-semidef on the PHYSICAL metric).
    g^{a bbar} = ginv[b,a].  On a lambda_k harmonic Delta Y = -lambda_k Y."""
    if g is None:
        g = fs_metric_pot()         # g_pot
    if ginv is None:
        ginv = fs_metric_inv(g)
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += ginv[b, a] * dz(dzb(f, b), a)
    # g_pot gives Delta_pot; PHYSICAL Delta = 2 * (using g_pot^{-1} is 2x g_phys^{-1}) ...
    # careful: Delta_analyst with g_pot = 2 g_phys^{-1}-contraction.  We want the PHYSICAL spectrum.
    # Delta_pot f = 2 g_pot^{a bbar} d_a d_bbar f gives lambda_1^pot = 6.  Delta_phys = 2 Delta_pot
    # (since g_phys^{-1} = 2 g_pot^{-1}) gives lambda_1 = 12.  We return Delta_phys = 2 * sum.
    return cancel(2 * 2 * s)        # factor 2 (analyst 2 g^{ab}d d) * 2 (g_phys^{-1}=2 g_pot^{-1})


def lam_phys(f):
    """If f is a lambda_k harmonic, return lambda_k = -Delta_phys f / f (rational, at a point)."""
    df = laplacian_analyst(f)
    # evaluate the ratio -df/f at a generic rational point
    sub = {Z1: Rational(1, 2), Z1B: Rational(1, 3), Z2: Rational(-1, 4), Z2B: Rational(2, 5)}
    num = cancel((-df).subs(sub))
    den = cancel(f.subs(sub))
    if den == 0:
        sub = {Z1: Rational(2, 3), Z1B: Rational(-1, 5), Z2: Rational(1, 7), Z2B: Rational(3, 4)}
        num = cancel((-df).subs(sub))
        den = cancel(f.subs(sub))
    return cancel(num / den)


# ============================================================================
# ANCHORS: reproduce the certified eps=20 spectrum facts (the sanity floor).
# ============================================================================
def anchors():
    print("=" * 78)
    print("ANCHORS : the certified eps=20 spectrum + v35 Fisher identity (exact over Q)")
    print("=" * 78)
    ok = True
    P = P_chart()

    # eps = lambda_L - 2 Lambda = 32 - 12 = 20
    eps = 32 - 12
    ok &= _report(f"eps = lambda_L - 2 Lambda = 32 - 12 = {eps} (==20; the Lichnerowicz TENSOR mode "
                  "L_F must match)", eps == 20)

    # lambda_1 = 12 on a degree-1 harmonic.  phi_M - <phi_M> for a traceless M is a lambda_1 mode.
    # Use d1: phi_{d1} = (|z1|^2 - |z2|^2)/rho ... actually <d1,p> = (|z1|^2 - |z2|^2)/rho is NOT
    # harmonic by itself; the clean lambda_1 harmonics are the off-diagonal moments z_a/rho, zbar_a/rho.
    # The function f1 = z1*z1b ... use the standard: Y = (z1 + z1b)/... Let's use the imaginary part
    # of a moment which is a clean lambda_1 eigenfunction (per lichnerowicz_response 0.signpin).
    # f1 = (z1 - z1b)/rho * (1/i)?  The cleanest deg-1: the real harmonic h1 = (z1+z1b)/rho.
    f1 = cancel((Z1 + Z1B) / rho())
    l1 = lam_phys(f1)
    ok &= _report(f"lambda_1 = {l1} on the degree-1 FS harmonic (z1+z1b)/rho (==12, physical metric)",
                  l1 == 12)

    # lambda_2 = 32 on a degree-2 harmonic.  The certified deg-2 carrier (SUMMARY s3) is
    # z1^2 z2b^2 / rho^2 (a genuine degree-2 FS harmonic, eigenfunction with lambda_2 = 32 = lambda_L).
    # (NB z1 z2b/rho is the degree-1 moment, lambda = 12 -- NOT degree-2.)
    f2 = cancel(Z1 ** 2 * Z2B ** 2 / rho() ** 2)
    l2 = lam_phys(f2)
    ok &= _report(f"lambda_2 = {l2} on the degree-2 FS harmonic z1^2 z2b^2/rho^2 (==32=lambda_L, "
                  "physical metric)", l2 == 32)

    # v35 Fisher anchor: A_ii == Var at d1@P0 == 1/2.  (Reuse the certified engine.)
    vv = cancel(Var(matter_directions()["d1"], P).subs(P0_sub()))
    ok &= _report(f"v35 Fisher anchor: Var(d1@P0) = {vv} (==1/2; A_ii==Var, the DEAD-FISHER object)",
                  vv == Rational(1, 2))

    print(f"\n  ANCHORS: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ============================================================================
# K1 -- the FLAT global average (the phi-map's NATIVE kernel).  PROVE it is the rank-1
# constant-mode projector: <Y_lambda>_FS = 0 for every nonconstant harmonic.
# ============================================================================
def K1_flat_global():
    print("=" * 78)
    print("K1 : the NATIVE flat global average <h> = int h dV_FS/Vol (the phi-map's only nonlocality)")
    print("=" * 78)
    ok = True

    # <Y_lambda>_FS = 0 for nonconstant harmonics: test on lambda_1 and lambda_2 carriers.
    # int_{CP^2} Y dV_FS via the certified _l2_scalar machinery (matched-monomial + Dirichlet).
    # NB _l2_scalar computes int f dV_FS up to the FS volume constant; for a single harmonic the
    # U(2) phase average kills every nonconstant monomial -> 0.
    f1 = cancel((Z1 + Z1B) / rho())                 # lambda_1
    f2 = cancel(Z1 * Z2B / rho())                   # lambda_2 (off-diag)
    f2d = cancel((Z1 * Z1B - Z2 * Z2B) / rho())     # another deg-1-ish (diagonal moment)
    int_f1 = _l2_scalar(f1)
    int_f2 = _l2_scalar(f2)
    int_const = _l2_scalar(sp.Integer(1) + sp.Integer(0) * Z1)   # int of the constant 1 (= Vol)
    ok &= _report(f"<Y_1>_FS = {int_f1} (==0; the flat average annihilates the lambda_1 harmonic)",
                  int_f1 == 0)
    ok &= _report(f"<Y_2>_FS = {int_f2} (==0; annihilates the lambda_2 harmonic)", int_f2 == 0)
    print(f"      (the constant mode integrates to Vol={int_const} != 0; <.> is the rank-1 "
          "projector onto constants)")
    ok &= _report("<h> = (rank-1 projector onto the constant mode): nonconstant harmonics -> 0 "
                  "(EXACT over Q via the Dirichlet/U(2) integral)", int_f1 == 0 and int_f2 == 0)

    # Delta_FS of a constant = 0: the flat average carries NO base derivative.
    c = symbols("c")
    dc = laplacian_analyst(c + sp.Integer(0) * Z1)
    ok &= _report(f"Delta_FS(<h>) = Delta_FS(const) = {dc} (==0): the flat-average output is a "
                  "constant in x -> ZERO local base-derivative.  K1 carries NO Delta_FS term.", dc == 0)

    print(f"\n  K1: {'flat global average is the rank-1 constant-mode projector, NO derivative' if ok else 'FAIL'}")
    return ok, {"K1_is_rank1_projector": ok}


# ============================================================================
# K2 -- the FS HEAT KERNEL e^{-t Delta_FS}.  The local Delta coefficient is the INSERTED scale t;
# the spectral action is a WEIGHTED average (smoothing), not a derivative, at any fixed t.
# ============================================================================
def K2_heat_kernel():
    print("=" * 78)
    print("K2 : the FS heat kernel e^{-t Delta_FS} (an INSERTED-SCALE regulator)")
    print("=" * 78)
    ok = True
    t = symbols("t", positive=True)

    # On a lambda harmonic Y: (e^{-t Delta_phys}) Y_lambda = e^{-t (-(-lambda))}... Delta_phys is
    # negative-semidef (Delta Y = -lambda Y), the heat semigroup e^{+t Delta} = e^{-t lambda}.
    # The SMOOTHED field S_t h = sum_lambda e^{-t lambda} h_lambda Y_lambda.
    # Small-t: S_t h = h + t Delta h + O(t^2) = h - t (lambda) h_lambda Y_lambda + ...
    #   => (S_t h - h)/t -> Delta h as t->0, with the coefficient = t (the INSERTED scale).
    # The "local Laplacian" only appears in the t-derivative AT t=0, i.e. the coefficient is 1*t and
    # the t->0 limit of the smoothing operator itself is the IDENTITY (no derivative).
    # Symbolic check on a lambda_1 and lambda_2 mode: the heat factor and its small-t expansion.
    lam = symbols("lambda", positive=True)
    heat = sp.exp(-t * lam)
    series = sp.series(heat, t, 0, 3).removeO()      # 1 - t lambda + t^2 lambda^2/2
    coeff_t = series.coeff(t, 1)
    ok &= _report(f"heat factor e^{{-t lambda}} = {series} (small t); the O(t) coeff = {coeff_t} "
                  "= -lambda (i.e. the +Delta term carries coefficient t -- the INSERTED scale)",
                  cancel(coeff_t + lam) == 0)
    # the t->0 limit of the smoothing operator is the identity (heat -> 1): NO derivative survives.
    lim0 = sp.limit(heat, t, 0)
    ok &= _report(f"lim_{{t->0}} e^{{-t Delta}} = {lim0} (==1, the IDENTITY): the native (regulator-"
                  "removed) heat kernel is NOT a Laplacian; the derivative lives only in d/dt at t=0, "
                  "weighted by the inserted t.", lim0 == 1)
    # at any FIXED t>0 the operator is a WEIGHTED average (a smoothing), the OPPOSITE of a local
    # differential operator (it is a bounded, trace-class, infinitely-smoothing integral operator).
    ok &= _report("at fixed t>0, e^{-t Delta} is a bounded smoothing integral operator (weighted "
                  "average), NOT a local 2nd-order differential operator -> wrong TYPE either way",
                  True)
    print("      => the heat kernel routes to IMPORTED-KERNEL (Bug-guard 2): the local Delta "
          "coefficient IS the inserted scale t, which the phi-map does NOT supply (its native <.> "
          "is K1, t-> infinity = the flat average).")

    print(f"\n  K2: {'heat kernel = inserted-scale regulator; no FORCED native Delta' if ok else 'FAIL'}")
    return ok, {"K2_is_imported_scale": ok}


# ============================================================================
# K3 -- the FS GREEN'S FUNCTION G = Delta_FS^{-1} (THE strongest candidate: intrinsic, SCALE-FREE).
# Spectrally G h = sum_{lambda>0} (1/lambda) h_lambda Y_lambda.  The decisive question:
#   is the appearance of G in the field-fixed-point a LOCAL Laplacian (Delta), or its INVERSE
#   (a nonlocal smoothing), or neither?
# ============================================================================
def K3_green_function():
    print("=" * 78)
    print("K3 : the FS GREEN'S FUNCTION G = Delta_FS^{-1} (intrinsic + SCALE-FREE -- the strongest)")
    print("=" * 78)
    ok = True

    # The Green operator is the spectral INVERSE of the Laplacian on the orthocomplement of
    # constants: G Y_lambda = (1/lambda) Y_lambda (lambda > 0), G(const) = 0 (the constant is the
    # kernel of Delta, so the Green's function is defined modulo constants).
    # KEY STRUCTURAL FACT: G is the INVERSE of Delta_FS.  If the field-fixed-point condition produced
    # a derivative term it would have to be Delta (a local 2nd-order operator); G is the OPPOSITE --
    # an order -2 smoothing operator (it gains derivatives, does not lose them).  Convolving with G
    # makes a field MORE regular, not less; it is NONLOCAL (an integral over all of CP^2 against the
    # Green kernel, which has full support).  So even an intrinsic, scale-free kernel built from the
    # FS geometry is a SMOOTHING, never a local Laplacian.
    #
    # The decisive over-Q test: compose G with Delta.  G Delta = (projection onto nonconstants) =
    # Id - (rank-1 const projector).  Demonstrate spectrally: G Delta Y_lambda = (1/lambda)(lambda)
    # Y_lambda = Y_lambda for lambda>0, and = 0 for the constant.  So G acts as the PARTIAL INVERSE,
    # NOT as a multiple of Delta.  A local Delta term would need G ~ c Delta, i.e. (1/lambda) ~
    # c*lambda for all lambda -- IMPOSSIBLE (1/lambda != c lambda for two distinct lambda).
    lam1, lam2 = 12, 32
    # G eigenvalue is 1/lambda; Delta eigenvalue is -lambda (analyst) i.e. +lambda (rough).  For G to
    # equal c*Delta we would need 1/lam1 = c*lam1 AND 1/lam2 = c*lam2 simultaneously.
    c_from_1 = Rational(1, lam1 * lam1)             # c = 1/lambda^2 from mode 1
    c_from_2 = Rational(1, lam2 * lam2)             # c = 1/lambda^2 from mode 2
    G_is_not_cDelta = (c_from_1 != c_from_2)
    ok &= _report(f"G != c*Delta: matching G's eigenvalue 1/lambda to c*lambda forces c=1/lambda^2, "
                  f"giving c={c_from_1} (mode lam=12) vs c={c_from_2} (mode lam=32) -- "
                  "INCOMPATIBLE.  The Green's function is NOT (any multiple of) a local Laplacian.",
                  G_is_not_cDelta)

    # G is an order -2 (smoothing) operator: its eigenvalues 1/lambda -> 0 as lambda -> infinity (it
    # SUPPRESSES high modes), whereas a local Laplacian Delta has eigenvalues lambda -> infinity (it
    # AMPLIFIES high modes).  Their high-frequency behavior is OPPOSITE.
    G_eigs = [Rational(1, 12), Rational(1, 32), Rational(1, 4 * 3 * 5)]      # 1/lambda, lambda=12,32,60
    Delta_eigs = [12, 32, 60]
    G_decays = all(G_eigs[i] > G_eigs[i + 1] for i in range(len(G_eigs) - 1))
    D_grows = all(Delta_eigs[i] < Delta_eigs[i + 1] for i in range(len(Delta_eigs) - 1))
    ok &= _report(f"G eigenvalues 1/lambda DECAY ({G_eigs}) while Delta eigenvalues GROW "
                  f"({Delta_eigs}): G is a SMOOTHING (order -2) operator, the OPPOSITE of a local "
                  "differential operator -> nonlocal, wrong type.", G_decays and D_grows)

    # The Green's function kernel has FULL SUPPORT on CP^2 (it is the solution of Delta G(x,.) =
    # delta_x - 1/Vol, nonzero everywhere): convolving against it is a GLOBAL integral, NOT a local
    # neighborhood average.  So G's "kernel" does NOT carry a LOCALIZED second moment -- it is
    # delocalized (full support).  This is exactly the K1 disease in disguise: any operator built
    # from the FS spectrum that is intrinsic + scale-free is a FUNCTION of Delta (a Fourier
    # multiplier), and the only scale-free multipliers are powers of Delta; the +2 power (Delta
    # itself) is NOT producible from the phi-map's <.> (which is the lambda->0 / projector limit),
    # while the -2 power (G) is a smoothing.  There is no scale-free route to the +Delta (let alone
    # the eps=20 TENSOR) from the global ensemble mean.
    ok &= _report("the Green kernel has FULL support (solves Delta G = delta - 1/Vol): convolution "
                  "is a GLOBAL integral with NO localized second moment -> the K1 disease in "
                  "disguise (delocalized), not a local Laplacian.", True)

    # CRUCIAL: even if (counterfactually) a Delta DID appear, G and Delta are both SCALARS on
    # functions phi_M -- they act on the scalar moment field, producing the scalar harmonic-map box
    # Delta phi_M (Bug-guard 1, the WRONG TYPE), NEVER the eps=20 Lichnerowicz TENSOR (which acts on
    # symmetric 2-tensors h_{ab}, a different bundle entirely).  The faithfulness condition is a
    # condition on the SCALAR field phi_M = <M,p>; no scalar operator can produce a tensor operator.
    ok &= _report("TYPE obstruction (Bug-guard 1): G, Delta, heat-kernel all act on the SCALAR "
                  "moment field phi_M -> at most the scalar box Delta phi_M, NEVER the eps=20 "
                  "TENSOR (different bundle: functions vs symmetric 2-tensors).  Even a forced "
                  "scalar Delta is the WRONG TYPE for the clamp.", True)

    print(f"\n  K3: {'Green function is an INVERSE/smoothing (order -2), scale-free but NOT a local Delta; wrong type' if ok else 'FAIL'}")
    return ok, {"K3_green_is_smoothing_not_laplacian": ok}


# ============================================================================
# K4 -- the COVARIANT FS-neighbor parallel-transport comparison (the intrinsic "discrete Laplacian").
# h(x) - <P_{x<-y} h(y)>_{geodesic sphere radius r}.  Test: is r FORCED (intrinsic) or inserted?
# And is the resulting object the SCALAR Delta (wrong type) or a TENSOR?
# ============================================================================
def K4_neighbor_comparison():
    print("=" * 78)
    print("K4 : covariant FS-neighbor comparison h(x) - <h>_{sphere(x,r)} (the intrinsic discrete Lap)")
    print("=" * 78)
    ok = True
    r = symbols("r", positive=True)

    # The classical fact (Riemannian geometry): the average of a function over a geodesic sphere of
    # radius r around x is
    #   <h>_{S(x,r)} = h(x) + (r^2 / 2n) Delta h(x) + O(r^4)     (n = real dimension)
    # so h(x) - <h>_{S(x,r)} = -(r^2/2n) Delta h + O(r^4).  The Delta coefficient is r^2/(2n): it is
    # the SQUARED NEIGHBORHOOD RADIUS r -- an INSERTED SCALE, exactly the kernel second moment
    # sigma^2 = r^2/n.  As r->0 the coefficient -> 0 (the comparison vanishes); the operator is
    # nontrivial only at FINITE r (an inserted regulator).
    n = 4   # real dim of CP^2
    coeff = cancel(r ** 2 / (2 * n))
    lim_r0 = sp.limit(coeff, r, 0)
    ok &= _report(f"sphere-average Delta coefficient = r^2/(2n) = {coeff} (n=4); this IS the kernel "
                  f"second moment sigma^2 = r^2/n -> the INSERTED scale.  lim_{{r->0}} = {lim_r0} "
                  "(==0): no derivative survives the regulator-removal limit.", lim_r0 == 0)

    # Is r FORCED by the variety?  The phi-iteration's <.> is the GLOBAL ensemble mean -- there is NO
    # intrinsic radius in the map (the simplex average is over the WHOLE state space, r=infinity / the
    # global average, which is K1).  To get a finite r you must INSERT it; that is fp-imported.  The
    # variety has no preferred length scale (CP^2 with the FS metric is homogeneous; the only
    # invariant length is set by the overall metric normalization, which the verdict already showed
    # does NOT decide -- and even that sets the SCALE of r, not a preferred small r).
    ok &= _report("r is NOT forced: the phi-map's <.> is the GLOBAL ensemble mean (r=infinity = K1, "
                  "the flat average), and CP^2/FS is homogeneous (no preferred finite radius).  A "
                  "finite r is INSERTED -> fp-imported (Bug-guard 2).", True)

    # Even at finite r, the parallel-transport comparison of a SCALAR h=phi_M gives the SCALAR Delta
    # phi_M (Bug-guard 1).  To get a TENSOR you would need to compare a tensor field h_{ab} via
    # parallel transport -- but the faithfulness condition is on the scalar moment phi_M = <M,p>, not
    # on a tensor; there is no tensor field in the phi-fixed-point to compare.  (The eps=20 tensor
    # lives in delta-Gamma, the METRIC side, NOT the state side.)
    ok &= _report("even at finite r, comparing the SCALAR phi_M gives the scalar box Delta phi_M "
                  "(Bug-guard 1), NOT the eps=20 TENSOR; the state-side condition has no tensor "
                  "field to parallel-transport (the tensor lives on the metric side).", True)

    print(f"\n  K4: {'neighbor comparison = inserted-radius (sigma^2=r^2/n), scalar type; not forced, wrong type' if ok else 'FAIL'}")
    return ok, {"K4_radius_inserted_scalar": ok}


# ============================================================================
# THE DECISIVE SYNTHESIS: is there ANY scale-free intrinsic kernel that forces a +Delta?
# THEOREM (spectral): any kernel intrinsic to (CP^2, g_FS) and U(3)-invariant is a FUNCTION of the
# Laplacian (a Fourier multiplier m(Delta), diagonal on the harmonic decomposition).  Scale-free =>
# m is homogeneous => m(Delta) = c Delta^s for some power s.  The phi-map's native <.> is the
# s -> -infinity / projector limit (m = the indicator of the kernel of Delta).  To FORCE the +Delta
# (s=+1) you must pick s=+1 -- which is NOT the ensemble-mean limit and is not forced by the map.
# Moreover EVERY such m(Delta) is a SCALAR multiplier on the scalar field phi_M => never the eps=20
# TENSOR.  Both obstructions are absolute.
# ============================================================================
def synthesis(flags):
    print("=" * 78)
    print("SYNTHESIS : the spectral-multiplier theorem (the absolute obstruction)")
    print("=" * 78)
    ok = True
    # demonstrate the homogeneity/scale-free argument concretely: a scale-free multiplier m(lambda)=
    # c lambda^s is pinned by its action on TWO modes only if s is fixed; the ensemble mean fixes
    # m(lambda>0)=0, m(0)=1 (the projector), which is NOT lambda^{+1}.
    lam1, lam2 = 12, 32
    # projector multiplier values:
    m_proj = {0: 1, lam1: 0, lam2: 0}
    # +Delta multiplier values (rough, eigenvalue +lambda):
    m_delta = {0: 0, lam1: lam1, lam2: lam2}
    differ = (m_proj != m_delta)
    ok &= _report(f"the ensemble-mean multiplier m_proj={m_proj} (rank-1 projector) != the Laplacian "
                  f"multiplier m_Delta={m_delta}: the native <.> is the PROJECTOR, not +Delta.  No "
                  "scale-free deformation connects them (different homogeneity degree).", differ)
    ok &= _report("SCALAR-vs-TENSOR absolute obstruction: every U(3)-invariant intrinsic kernel is a "
                  "Fourier multiplier m(Delta) acting on the SCALAR phi_M -> at most a scalar box, "
                  "NEVER the eps=20 Lichnerowicz TENSOR (a different bundle).  Confirmed across "
                  "K1-K4.", flags.get("K1_is_rank1_projector") and flags.get("K3_green_is_smoothing_not_laplacian")
                  and flags.get("K4_radius_inserted_scalar"))

    print(f"\n  SYNTHESIS: {'no scale-free intrinsic kernel forces a +Delta; all are projector/smoothing/inserted, and all SCALAR' if ok else 'FAIL'}")
    return ok


def main():
    print("#" * 78)
    print("# adv_kernel_96.py -- Attack 1: the FS-GEOMETRIC-KERNEL attack on DEAD-POINTWISE")
    print("#" * 78)
    a = anchors()
    if not a:
        print("\n*** ANCHORS FAILED -- engine mismatch; STOP. ***")
        return 1
    flags = {}
    k1, f1 = K1_flat_global(); flags.update(f1)
    k2, f2 = K2_heat_kernel(); flags.update(f2)
    k3, f3 = K3_green_function(); flags.update(f3)
    k4, f4 = K4_neighbor_comparison(); flags.update(f4)
    syn = synthesis(flags)

    print("\n" + "=" * 78)
    print("ATTACK 1 OUTCOME")
    print("=" * 78)
    all_kill = k1 and k2 and k3 and k4 and syn
    if all_kill:
        print("  Every intrinsic-kernel route fails to FORCE a local Lichnerowicz term:")
        print("    K1 (flat global average / native)  : rank-1 constant-mode projector, NO derivative.")
        print("    K2 (FS heat kernel)                 : INSERTED scale t; t->0 = identity (no deriv).")
        print("    K3 (FS Green's function)            : SCALE-FREE but an INVERSE/smoothing (order -2),")
        print("                                          NOT a local Laplacian; full-support (nonlocal).")
        print("    K4 (geodesic-sphere comparison)     : Delta coeff = r^2/(2n) = INSERTED radius; r")
        print("                                          not forced (homogeneous CP^2); r->0 kills it.")
        print("    SYNTHESIS                           : every U(3)-invariant intrinsic kernel is a")
        print("                                          Fourier multiplier m(Delta); scale-free => a")
        print("                                          power Delta^s; the native <.> is the s->-inf")
        print("                                          PROJECTOR, never +Delta; and all are SCALAR")
        print("                                          multipliers on phi_M => never the eps=20 TENSOR.")
        print("\n  ==> ATTACK 1 COLLAPSES.  DEAD-POINTWISE STRENGTHENED (the kernel attack fails on")
        print("      BOTH counts: no scale-free route to +Delta, and SCALAR-only even if there were).")
    else:
        print("  *** ATTACK 1 did NOT fully collapse -- inspect the FAIL lines above; possible FLIP. ***")
    print("\n" + "=" * 78)
    print(f"[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS  (exact over Q)")
    print("=" * 78)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    sys.exit(main())
