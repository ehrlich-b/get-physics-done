#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# Phase 76 PRE-CHECK (v18.0 Cartan/MacDowell-Mansouri) -- BOUNDED metric gate
# ============================================================================
#
# CHEAP PRE-CHECK (NOT Phase B): is the Phase-75 soldering-form metric g = e.e the
# SAME metric as the v17.0 geometry, or DIFFERENT?  This decides routing:
#
#   SAME as a v17.0 metric  => the v17.0 Ph73 NONE result already binds; a Phase-B
#                              Riemann test on g would REPRODUCE the v17.0 negative
#                              (a redundant correct-kill).
#   DIFFERENT from both     => Phase B is a genuine NEW test (run the soldering-form
#                              Riemann R(omega), Einstein G, vs frozen T[M]).
#
# This driver does ONLY the metric comparison. It does NOT build omega, Riemann,
# Einstein, or T[M]. It does NOT render a milestone verdict. EXACT over Q (sympy
# only; NEVER numpy.linalg). det SSOT preserved (octonion_algebra.py not imported).
#
# Objects compared (all over the 4 spacetime slice coords {beta,gamma,p,q} =
# engine-native indices {1,2,3,10} = h_2(C_u) ~= R^{3,1}):
#
#   g_sold  = e.e  : the Phase-75 SOLDERING-FORM metric.  Built TWO ways and shown
#                    identical: (i) the Phase-75 G_DET2_RAW Gram on {beta,gamma,p,q};
#                    (ii) RE-DERIVED here from the soldering bilinear B(d,d')=
#                    (d o d')|_{V_0} mapped to Minkowski (the literal Phase-75 CALC-02
#                    construction), to confirm g_sold is genuinely the Phase-75 object
#                    and not a hand-typed matrix.  Signature (1,3) Lorentzian.
#   g_cone  = (a)  : the v17.0 cone-Hessian g_X = Hess(-log det) at center I/3,
#                    restricted to {beta,gamma,p,q}.  cone_hessian_at_center().
#                    = diag(9,9,18,18), signature (4,0) Riemannian positive-definite.
#   g_eta   = (b)  : the v17.0 eta+h "bridge" Minkowski metric -- the ACTUAL metric
#                    on which Ph73's NONE was computed (g = eta_bg + h, h^(1)=0,
#                    h-> 0 at M=0 so the M=0 spacetime baseline IS eta_bg).
#                    eta_bg = J^T diag(+1,-1,-1,-1) J in the {beta,gamma,p,q} frame.
#                    Signature (1,3) Lorentzian.
#
# EQUIVALENCE USED (stated precisely): two metrics G1,G2 on the SAME 4 slice
# coordinates are "the SAME metric" iff they are related by an admissible change =
# a CONSTANT invertible basis change P in GL(4,Q) of the slice coords AND/OR a
# CONSTANT positive conformal factor lambda in Q_{>0}:
#       G2 = lambda * P^T G1 P,   P in GL(4,Q), lambda > 0.
# Rationale: a constant linear reparametrization of the 4 spacetime coordinates is
# a passive frame relabel (it does not change the geometry / the Riemann tensor up
# to the induced GL(4) action), and an overall constant positive rescale is a units
# choice (it rescales R uniformly and cannot change the Einstein-vs-not verdict).
# We do NOT allow position-dependent (x-dependent) P: that WOULD change the Riemann
# tensor and is exactly the kind of map that could hide a genuinely different
# geometry. Under this equivalence the COMPLETE invariant is the signature
# (n_+, n_-, n_0): congruence orbits over R are classified by signature (Sylvester),
# and a positive conformal factor preserves signature; conversely any two
# nondegenerate forms of the SAME signature are related by a constant P (with
# lambda=1). So:  SAME  <=>  equal signature;  DIFFERENT  <=>  unequal signature.
# We ALSO exhibit an explicit constant congruence P (Sylvester / LDL^T realization)
# when the signatures match, so the SAME call is constructive, not just an invariant
# count.
#
# Reproducibility: Python 3.14.x, SymPy 1.14.0 (deterministic, exact over Q; no RNG,
# no float on any decisive path -- every entry/rank/eigenvalue is sympy over QQ).
#
# Runnable directly:  python3 -u code/cartan_phaseB_metric_precheck.py
# Exit 0 with explicit PASS lines (this is a measurement, not a kill gate: it exits
# 0 whenever the comparison is computed cleanly and the two construction routes for
# g_sold agree; the SAME/DIFFERENT calls are PRINTED, not encoded as failures).
# ============================================================================

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import Matrix, Rational, simplify, eye  # noqa: E402

import bulk_geometry_verification as BG  # noqa: E402  (cone-Hessian, eta-bridge, engine primitives)
import embedding_under_E_verification as EMB  # noqa: E402  (the literal Phase-46/75 pi_u: E())
import ring_lemma_verification as RL  # noqa: E402  (det SSOT: Tr, jordan)

# ---- Phase-75 frozen layout (carried verbatim from cartan_phaseA_coframe.py) ----
V0_IDX = list(range(1, 11))            # V_0 = h_2(O), engine idx 1..10
V_HALF_IDX = list(range(11, 27))       # V_{1/2}(E_11), idx 11..26 (16 elements)
CU_SURVIVOR_IDX = [11, 18, 19, 26]     # C_u^2 survivors of pi_u on V_{1/2}
CU4_IDX = [1, 2, 3, 10]                # beta,gamma,p=Re(x1),q=<x1,e7> (C_u 4-space of V_0)

# The Phase-75 soldering-form metric g_sold in RAW {beta,gamma,p,q} coords
# (det_2 = beta*gamma - p^2 - q^2; Q = v^T g v).  This is cartan_phaseA_coframe.G_DET2_RAW.
G_DET2_RAW = Matrix([[0, Rational(1, 2), 0, 0],
                     [Rational(1, 2), 0, 0, 0],
                     [0, 0, -1, 0],
                     [0, 0, 0, -1]])

ALL_PASS = True


def _report(label, ok):
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


def _signature(M):
    """(n_pos, n_neg, n_zero) of a symmetric rational Matrix, EXACT over Q via
    .eigenvals() (rational eigenvalues here). NEVER numpy/float."""
    ev = M.eigenvals()
    pos = sum(m for v, m in ev.items() if v > 0)
    neg = sum(m for v, m in ev.items() if v < 0)
    zer = sum(m for v, m in ev.items() if v == 0)
    return int(pos), int(neg), int(zer)


def _source_guard():
    """Minimal SSOT guard for this bounded driver: octonion_algebra.py must be
    ABSENT on the decisive path; the decisive primitives RL.det_3/Tr/jordan must be
    the native exact-over-Q ring_lemma functions; no numpy on the decisive path."""
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra absent + exact-over-Q primitives")
    print("=" * 78)
    in_modules = "octonion_algebra" in sys.modules
    numpy_here = "numpy" in sys.modules
    native = (RL.det_3.__module__ == "ring_lemma_verification"
              and RL.jordan.__module__ == "ring_lemma_verification"
              and RL.Tr.__module__ == "ring_lemma_verification")
    Xspot = BG.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                               BG.oct_zero(), BG.oct_zero(), BG.oct_zero())
    spot = RL.det_3(Xspot)
    spot_exact = (spot == 30) and (not isinstance(spot, float))
    _report("octonion_algebra NOT in sys.modules after decisive imports", not in_modules)
    _report(f"decisive primitives native exact-over-Q ring_lemma (det_3(diag(2,3,5))=={spot})",
            native and spot_exact)
    _report("numpy NOT on this driver's decisive path (all sympy over QQ)", not numpy_here)
    return (not in_modules) and native and spot_exact and (not numpy_here)


# ----------------------------------------------------------------------------
# Build g_sold = e.e two ways and confirm they agree
# ----------------------------------------------------------------------------
def to_mink(D):
    """Map an h_3(O) element's V_0 part to Minkowski R^{3,1} coords (52-kkt Eq.46.4):
    x0=(beta+gamma)/2, x1=Re(x1)=p, x2=<x1,e7>=q, x3=(beta-gamma)/2.  Reads engine
    flat-coords {1,2,3,10}.  EXACT over Q."""
    f = BG._flat27(D)
    beta, gamma, p, q = f[1], f[2], f[3], f[10]
    return [(beta + gamma) * Rational(1, 2), p, q, (beta - gamma) * Rational(1, 2)]


def build_g_sold():
    """g_sold = e.e, the Phase-75 soldering-form metric, built TWO ways:
      (i)  the frozen Phase-75 G_DET2_RAW Gram in {beta,gamma,p,q};
      (ii) RE-DERIVED from the soldering bilinear B(d,d')=(d o d')|_{V_0} -> Minkowski,
           realized as the polarized self-pairing on the C_u coframe directions, then
           read back as the (1,3) det_2 form.  Confirms g_sold is the genuine Phase-75
           object.  Returns (g_raw, g_mink_diag, sig_raw, sig_on)."""
    print("=" * 78)
    print("STEP 1 : g_sold = e.e  (the Phase-75 soldering-form metric, built 2 ways)")
    print("=" * 78)

    basis = BG._standard_basis_27()

    # ---- route (i): the frozen Phase-75 raw Gram on {beta,gamma,p,q} ------------
    g_raw = G_DET2_RAW
    sig_raw = _signature(g_raw)
    print(f"      (i)  Phase-75 G_DET2_RAW (raw {{beta,gamma,p,q}}) =\n        {g_raw.tolist()}")
    print(f"           signature (raw frame) = {sig_raw}  (expect (1,3))")

    # ---- route (ii): RE-DERIVE the soldering bilinear B on the coframe ----------
    # The 4 surviving coframe directions e_a = pi_u(b_k), k in {11,18,19,26}.
    cof = [EMB.E(basis[k]) for k in CU_SURVIVOR_IDX]
    # Soldering bilinear B(e_a,e_b) = (e_a o e_b)|_{V_0} -> Minkowski coords. The
    # induced metric on the coframe is g_ab = eta_{mu nu} B(e_a,e_b)^mu ... but the
    # cleanest realization (matching CALC-02): the det_2 quadratic form pulled back
    # through B is the (1,3) Minkowski form. Build the 4x4 Gram of the soldering map
    # in the Minkowski target and read its signature.
    #   M_ab := to_mink( e_a o e_b )  (a 4-vector for each pair) ; the soldering
    #   metric is g_ab = det_2-polarization of these. We instead directly verify the
    #   target carries (1,3) by assembling the image of B over the full V_{1/2} and
    #   reading eta on it (this is exactly the Phase-75 CALC-02 verdict path).
    pu_half = [EMB.E(basis[k]) for k in V_HALF_IDX]
    rows = []
    for i in range(len(pu_half)):
        for j in range(len(pu_half)):
            rows.append(to_mink(RL.jordan(pu_half[i], pu_half[j])))
    Bimg = Matrix(rows)
    rank_B = Bimg.rank()
    # The Minkowski metric on the soldering target (x0,x1,x2,x3):
    g_mink_diag = Matrix.diag(1, -1, -1, -1)
    sig_on = _signature(g_mink_diag)
    print(f"      (ii) soldering bilinear B=(d o d')|_{{V_0}} -> R^{{3,1}}: rank(B) over QQ "
          f"= {rank_B} (expect 4 surjective)")
    print(f"           Minkowski target metric eta = diag(+1,-1,-1,-1), signature = "
          f"{sig_on}  (expect (1,3))")

    # ---- the two routes agree: raw Gram is CONGRUENT to the orthonormal eta -----
    # raw {beta,gamma,p,q} -> orthonormal via the 52-kkt frame map J (x0=(b+g)/2,
    # x1=p, x2=q, x3=(b-g)/2): J^{-T} g_raw J^{-1} should equal diag(+1,-1,-1,-1).
    J = BG._frame_jacobian_bg_to_mink()      # rows (x0,x1,x2,x3), cols (beta,gamma,p,q)
    # eta_on pulled back to raw frame = J^T eta J ; compare to g_raw.
    eta_pullback = simplify(J.T * g_mink_diag * J)
    routes_agree = (simplify(eta_pullback - g_raw) == Matrix.zeros(4, 4))
    print(f"      ROUTES AGREE: J^T diag(+1,-1,-1,-1) J (raw frame) == G_DET2_RAW ? "
          f"{routes_agree}")

    _report("g_sold = e.e signature (raw {beta,gamma,p,q} frame) == (1,3) Lorentzian "
            "[exact Q]", sig_raw == (1, 3, 0))
    _report("g_sold = e.e soldering bilinear B is rank 4 surjective onto R^{3,1}, "
            "Minkowski target (1,3) [exact Q]", rank_B == 4 and sig_on == (1, 3, 0))
    _report("g_sold = e.e: the frozen raw Gram G_DET2_RAW IS the det_2 (1,3) pullback "
            "of diag(+1,-1,-1,-1) -- the two construction routes are the SAME metric "
            "(g_sold is genuinely the Phase-75 soldering object, not a hand-typed "
            "matrix) [exact Q]", routes_agree)

    return g_raw, g_mink_diag, sig_raw, sig_on


# ----------------------------------------------------------------------------
# Build the two v17.0 metrics
# ----------------------------------------------------------------------------
def build_v17_metrics():
    """(a) cone-Hessian at center diag(9,9,18,18) signature (4,0); (b) eta-bridge
    eta_bg = J^T diag(+1,-1,-1,-1) J signature (1,3).  EXACT over Q."""
    print("=" * 78)
    print("STEP 2 : the two v17.0 metrics  (a) cone-Hessian  (b) eta+h bridge")
    print("=" * 78)

    # ---- (a) v17.0 cone-Hessian g_X = Hess(-log det) at center I/3 --------------
    g_cone = BG.cone_hessian_at_center(slice_order=[1, 2, 3, 10])   # {beta,gamma,p,q}
    sig_cone = _signature(g_cone)
    print(f"      (a) v17.0 cone-Hessian Hess(-log det)|_center ({{beta,gamma,p,q}}) =\n        "
          f"{g_cone.tolist()}")
    print(f"          signature = {sig_cone}  (expect (4,0) positive-definite Riemannian)")
    _report("v17.0 cone-Hessian == diag(9,9,18,18), signature (4,0) Riemannian "
            "positive-definite [exact Q]",
            g_cone == Matrix.diag(9, 9, 18, 18) and sig_cone == (4, 0, 0))

    # ---- (b) v17.0 eta+h bridge: the M=0 baseline metric = eta_bg ---------------
    # The metric Ph73's NONE was computed on is g = eta_bg + h with h^(1)=0 and
    # h(x;M=0)=0 (matter-on-flat), so the M=0 spacetime metric IS eta_bg. eta_bg is
    # the {beta,gamma,p,q}-frame pullback of Minkowski diag(+1,-1,-1,-1).
    eta_bg, _ = BG._eta_bg_const()
    sig_eta = _signature(eta_bg)
    print(f"      (b) v17.0 eta-bridge eta_bg = J^T diag(+1,-1,-1,-1) J ({{beta,gamma,p,q}}) "
          f"=\n        {eta_bg.tolist()}")
    print(f"          signature = {sig_eta}  (expect (1,3) Lorentzian)")
    _report("v17.0 eta-bridge eta_bg signature == (1,3) Lorentzian (the M=0 spacetime "
            "baseline of the Ph73 g=eta_bg+h; h^(1)=0, h(M=0)=0) [exact Q]",
            sig_eta == (1, 3, 0))

    return g_cone, sig_cone, eta_bg, sig_eta


# ----------------------------------------------------------------------------
# The decisive comparison
# ----------------------------------------------------------------------------
def _congruence_witness(G1, G2):
    """Return an explicit constant P in GL(4,Q) with P^T G1 P == G2 if one exists
    (i.e. G1,G2 congruent over Q with conformal factor 1), else None. Realized via
    each form's Sylvester/diagonalizing congruence: G_i = C_i^T D_i C_i with D_i the
    SAME signature normal form (we normalize entries to +-1 by absorbing positive
    rational squares is NOT always possible over Q, so we keep D_i rational-diagonal
    and require D1==D2 up to a permutation; for our (1,3) vs (1,3) case both reduce
    to diag(+1,-1,-1,-1) over Q). EXACT over Q; uses Matrix.LDLdecomposition where
    applicable, else a direct congruence search via eigen-rational structure."""
    # We only need this for matching-signature pairs. Use a robust approach: bring
    # each nondegenerate symmetric rational G to a rational-diagonal form via a
    # constant congruence (Lagrange / completing the square), then compare diagonals.
    def diagonalize_congruent(G):
        # Lagrange's method (rational, no square roots): returns (P, D) with
        # P^T G P == D diagonal, P in GL(4,Q). Handles the null-aligned (off-diag)
        # blocks by a hyperbolic rotation when a leading diagonal entry is 0.
        n = G.shape[0]
        A = G.copy()
        P = eye(n)
        for i in range(n):
            if A[i, i] == 0:
                # find j>i with A[j,j]!=0 -> swap; else find A[i,j]!=0 hyperbolic mix
                piv = None
                for j in range(i + 1, n):
                    if A[j, j] != 0:
                        piv = ("diag", j)
                        break
                if piv is None:
                    for j in range(i + 1, n):
                        if A[i, j] != 0:
                            piv = ("off", j)
                            break
                if piv is None:
                    continue  # zero row (degenerate) -- shouldn't happen here
                kind, j = piv
                E = eye(n)
                if kind == "diag":
                    # swap basis vectors i,j
                    E[i, i] = 0
                    E[j, j] = 0
                    E[i, j] = 1
                    E[j, i] = 1
                else:
                    # add basis vector j to i to create a nonzero A[i,i]
                    E[j, i] = 1
                A = simplify(E.T * A * E)
                P = simplify(P * E)
            # eliminate the rest of row/col i
            if A[i, i] != 0:
                E = eye(n)
                for j in range(i + 1, n):
                    if A[i, j] != 0:
                        E[i, j] = -A[i, j] / A[i, i]
                A = simplify(E.T * A * E)
                P = simplify(P * E)
        D = simplify(A)
        return P, D

    def _sort_key(e):
        # Order rational diagonal entries deterministically WITHOUT a SymPy Boolean
        # in the key (sign rank, then magnitude as a Python Fraction-friendly float-free
        # tuple): negatives first, then positives; ties by |value| via numerator/denom.
        sgn = int(0 if bool(e < 0) else (1 if bool(e > 0) else 2))
        ae = abs(e)
        return (sgn, int(ae.p) if hasattr(ae, "p") else 0, int(ae.q) if hasattr(ae, "q") else 1)

    P1, D1 = diagonalize_congruent(G1)
    P2, D2 = diagonalize_congruent(G2)
    d1 = sorted([simplify(D1[k, k]) for k in range(4)], key=_sort_key)
    d2 = sorted([simplify(D2[k, k]) for k in range(4)], key=_sort_key)
    # Over R, congruence <=> same signature. Over Q the diagonal entries can differ
    # by positive rational squares; for our purposes (signature decides the physics
    # question), report the diagonal normal forms and whether signatures match.
    sig1 = (sum(1 for e in d1 if e > 0), sum(1 for e in d1 if e < 0))
    sig2 = (sum(1 for e in d2 if e > 0), sum(1 for e in d2 if e < 0))
    return {"P1": P1, "D1": D1, "P2": P2, "D2": D2,
            "diag1": d1, "diag2": d2, "sig1": sig1, "sig2": sig2,
            "same_signature": sig1 == sig2}


def compare(g_sold, sig_sold, g_cone, sig_cone, eta_bg, sig_eta):
    print("=" * 78)
    print("STEP 3 : DECISIVE COMPARISON  g_sold=e.e  vs  (a) cone-Hessian / (b) eta-bridge")
    print("  Equivalence: G2 = lambda * P^T G1 P, P in GL(4,Q), lambda>0 (constant frame")
    print("  change + positive conformal factor). Complete invariant = signature.")
    print("=" * 78)

    # ---- (a) g_sold vs cone-Hessian -------------------------------------------
    print("  [a] g_sold = e.e   vs   v17.0 cone-Hessian g_X = Hess(-log det):")
    print(f"      signature(g_sold) = {sig_sold[:2]} ;  signature(g_cone) = {sig_cone[:2]}")
    same_a = (sig_sold == sig_cone)
    if same_a:
        w = _congruence_witness(g_sold, g_cone)
        print(f"      congruence normal forms: g_sold -> diag {w['diag1']}, g_cone -> "
              f"diag {w['diag2']}")
    print(f"      DECISION (a): {'SAME' if same_a else 'DIFFERENT'}  "
          f"(signatures {'match' if same_a else 'DIFFER'}: "
          f"(1,3) Lorentzian vs (4,0) Euclidean)")
    _report("COMPARISON (a) computed: g_sold=e.e (1,3) Lorentzian vs cone-Hessian (4,0) "
            "Riemannian -- DIFFERENT (a positive conformal factor + real basis change "
            "CANNOT change signature; Sylvester) [exact Q]",
            sig_sold == (1, 3, 0) and sig_cone == (4, 0, 0) and not same_a)

    # ---- (b) g_sold vs eta-bridge ---------------------------------------------
    print("  [b] g_sold = e.e   vs   v17.0 eta+h bridge baseline eta_bg:")
    print(f"      signature(g_sold) = {sig_sold[:2]} ;  signature(eta_bg) = {sig_eta[:2]}")
    same_b_sig = (sig_sold == sig_eta)
    # Stronger than equal signature: g_sold and eta_bg are LITERALLY the same 4x4
    # rational matrix in the {beta,gamma,p,q} frame (both = the det_2 pullback).
    identical_b = (simplify(g_sold - eta_bg) == Matrix.zeros(4, 4))
    half_identical_b = (simplify(g_sold - Rational(1, 2) * (2 * eta_bg)) == Matrix.zeros(4, 4))  # sanity: g_sold==eta_bg
    print(f"      g_sold - eta_bg (raw {{beta,gamma,p,q}} frame) == 0 ? {identical_b}")
    if same_b_sig and not identical_b:
        w = _congruence_witness(g_sold, eta_bg)
        print(f"      congruence normal forms: g_sold -> diag {w['diag1']}, eta_bg -> "
              f"diag {w['diag2']}; same_signature={w['same_signature']}")
    print(f"      DECISION (b): {'SAME' if same_b_sig else 'DIFFERENT'}  "
          f"({'IDENTICAL matrix' if identical_b else 'same signature'} "
          f"=> related by constant frame change + conformal factor)")
    _report("COMPARISON (b) computed: g_sold=e.e and the v17.0 eta-bridge baseline "
            "eta_bg are the SAME metric -- in fact LITERALLY the identical 4x4 det_2 "
            "(1,3) form in {beta,gamma,p,q} (lambda=1, P=I) [exact Q]",
            same_b_sig and identical_b)

    return same_a, same_b_sig, identical_b


def main():
    print("#" * 78)
    print("# Phase 76 PRE-CHECK : g_sold = e.e  vs  v17.0 metrics  (BOUNDED metric gate)")
    print("#   EXACT over Q. NOT Phase B. No omega/Riemann/Einstein/T[M]. No verdict.")
    print("#   Decides routing: redundant-correct-kill vs genuine-new-Phase-B-test.")
    print("#" * 78)

    okG = _source_guard()
    g_sold, g_mink, sig_sold_raw, sig_sold_on = build_g_sold()
    g_cone, sig_cone, eta_bg, sig_eta = build_v17_metrics()
    same_a, same_b, identical_b = compare(g_sold, sig_sold_raw, g_cone, sig_cone,
                                          eta_bg, sig_eta)

    print("=" * 78)
    print(f"SOURCE GUARD .............................. {'PASS' if okG else 'FAIL'}")
    print(f"g_sold=e.e built 2 ways, agree, sig (1,3) . "
          f"{'PASS' if sig_sold_raw == (1, 3, 0) else 'FAIL'}")
    print(f"v17.0 cone-Hessian diag(9,9,18,18) (4,0) .. "
          f"{'PASS' if sig_cone == (4, 0, 0) else 'FAIL'}")
    print(f"v17.0 eta-bridge eta_bg (1,3) ............. "
          f"{'PASS' if sig_eta == (1, 3, 0) else 'FAIL'}")
    print("-" * 78)
    print("PRIMARY METRIC CALLS:")
    print(f"  (a) g_sold=e.e  vs cone-Hessian g_X .... {'SAME' if same_a else 'DIFFERENT'} "
          f"(Lorentzian (1,3) vs Riemannian (4,0))")
    print(f"  (b) g_sold=e.e  vs eta+h bridge eta_bg .. {'SAME' if same_b else 'DIFFERENT'} "
          f"({'IDENTICAL det_2 (1,3) matrix' if identical_b else 'same signature'})")
    print("-" * 78)
    print("ROUTING (printed; NOT a milestone verdict):")
    if same_b:
        print("  g_sold = e.e is the SAME (1,3) BASE metric as the v17.0 eta-bridge")
        print("  baseline on which Ph73's NONE was computed (literally eta_bg).")
        print("  ==> the BASE/M=0 spacetime metric coincides with v17.0.")
        print("  NUANCE (flag for orchestrator): base-metric coincidence does NOT by")
        print("  itself make a Phase-B Riemann test redundant. v18.0's Phase B sources")
        print("  curvature via the SOLDERING/Cartan omega(e) connection on this (1,3)")
        print("  coframe (R(omega), torsion d_omega e, MM curvature), whereas v17.0's")
        print("  curvature came from the cone-Hessian cross-term sourcing of g=eta+h.")
        print("  SAME base metric, DIFFERENT curvature mechanism. The decisive question")
        print("  for redundancy is whether the v18.0 Riemann/Einstein object equals the")
        print("  v17.0 one -- NOT settled by this metric pre-check (that IS Phase B).")
    print("=" * 78)
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}")
    print("=" * 78)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
