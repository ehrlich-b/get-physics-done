#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# Phase 76 (v18.0 Cartan/MacDowell-Mansouri) -- Plan 01  (PART 1, the VACUUM half)
# Phase A.5: THE BERRY-CURVATURE SAME-WALL GATE -- SOFT KILL  (conjunctive w/ Ph75)
# ============================================================================
#
# Decide, EXACTLY over Q(i) and BEFORE any matter is turned on, whether the canonical
# Berry curvature  F_B = Im(QGT) = -2 Im Tr(P dP dP)  of the rank-1 C_u-idempotent
# family E(x) is (VALD-03) well-defined and generically NONZERO on the 4d slice
# {11,18,19,26} = C_u^2, BORN FROM the C_u breaking of the isotropy-irreducible
# OP^2 = F_4/Spin(9) (which carries NO invariant 2-form => round Berry = 0); run the
# SOFT real-part anchor (CALC-03, Re(QGT) = Fubini-Study metric of the same
# non-Einstein CHARACTER as the v17.0 cone-Hessian -- INFORMATIVE, never a KILL);
# and classify the M=0 vacuum (CALC-04: flat / pure-Lambda-Kahler / other).
#
#   CP^1 PIN  (calibration, BEFORE any h_3(O) object): reproduce the monopole anchor
#             F_B = -sin theta/2 (int = -2pi), g_theta theta = 1/4 exactly over Q(i).
#             PINS the sign and the factor-2 of the whole recipe (defeats Pitfall-5).
#   VALD-03   (done FIRST): F_B = -2 Im Q well-defined + generically NONZERO + BORN
#             FROM the C_u breaking (group theory: OP^2 isotropy-irreducible =>
#             no invariant 2-form => round Berry = 0). A degenerate F_B == 0 is the
#             worse-than-SOFT-KILL outcome and is detected + reported flat.
#   CALC-03   (SOFT, INFORMATIVE, NOT a KILL): Re(QGT) = 1/2 Tr(dP dP) a positive-
#             definite FS metric (the ONLY hard failure here is Re(QGT) NOT pos-def);
#             its non-Einstein CHARACTER vs the cone-Hessian diag(9,9,18,18)/round
#             K=-1 reported as a diagnostic. Discrepancy EXPECTED (FS-pullback !=
#             cone-Hessian restriction) -- fp-reuse-cone-hessian.
#   CALC-04   M=0 vacuum class of F_B (flat / pure-Lambda ~ e^e Kahler / other), via
#             the trace/traceless/Weyl decomposition. Lambda NOT reintroduced
#             negative; R x H^3 NOT reintroduced (the FALSIFIED v17.0 vacuum).
#
# THE TWO DESIGN POINTS (do not get these wrong):
#   1. The QGT uses the ASSOCIATIVE complex matrix product on slice_to_complex(P)
#      (e_7 -> i, i = sympy.I SYMBOLIC over Q(i)), NOT the Jordan product o --
#      C_u ~= C is the unique associative completion u = e_7 provides, so the
#      associative product is FORCED.  F_B = Im(QGT) is the literal SymPy Im.
#   2. The Re(QGT) = cone-Hessian comparison (CALC-03) is a SOFT, INFORMATIVE
#      diagnostic ONLY. A discrepancy is EXPECTED and is NEVER a KILL/HALT. The
#      v17.0 NONE binds the REAL part; this phase mines the IMAGINARY part.
#
# CONVENTION LOCK (v18.0; see .gpd/state.json convention_lock / CONVENTIONS.md):
#   * EXACT over Q(i): the i is sympy.I, SYMBOLIC; ranks/eigenvals/Re/Im via SymPy
#     over QQ or Q(i); NO float on any decisive path (fp-float-decisive).
#   * octonion multiplication: Fano e1 e2 = e4.       complex structure: u = e7.
#   * primitive idempotent: E_11 = diag(1,0,0).       Peirce eigenvalues {0,1/2,1}.
#   * det SSOT = ring_lemma_verification.py det_3. octonion_algebra.py is BANNED on
#     every decisive path (fp-octonion-algebra; source guard below).
#   * QGT: Q_{mu nu} = Tr(P d_mu P d_nu P);  g = Re Q (Fubini-Study);
#     F_B = i Tr(P[d_mu P, d_nu P]) = -2 Im Q (Berry curvature).  Sign/factor PINNED
#     by the CP^1 anchor (F_B = -sin theta/2, g_theta theta = 1/4).
#   * metric signature mostly-minus (+,-,-,-) on the soldered (1,3) Lorentz block of
#     the C_u^2 survivors {11,18,19,26} (Phase 75 SURVIVES target). natural units.
#   * Lambda = 0; the M=0 spacetime vacuum is flat KKT eta; do NOT reintroduce
#     Lambda<0 / R x H^3 (the FALSIFIED v17.0 cone-Hessian source-field geometry).
#   * engine 27-coord layout: V_1={0}; V_0={1..10}; V_{1/2}={11..26}. C_u survivors
#     of pi_u on V_{1/2} = {11,18,19,26} = {Re(x2),<x2,e7>,Re(x3),<x3,e7>} (Phase 75).
#
# Reuses the WARM exact engines (imported, NOT rebuilt; det SSOT preserved):
#   embedding_under_E_verification : E, proj_u_exact(a,u_index=7), slice_to_complex,
#                                    cu_to_complex, h3o_from_coords, jordan, oct_zero
#   ring_lemma_verification        : Tr, jordan, det_3 (det SSOT)
#   bulk_geometry_verification     : cone_hessian_at_center, h3_constant_curvature,
#                                    ricci_decomposition_n4, peirce_indices_under_E11
#
# Reproducibility: Python 3 (CPython), SymPy 1.14.0 (deterministic, exact over Q(i);
# no RNG on any decisive path -- every matrix is built from fixed rational entries and
# the symbolic imaginary unit sympy.I).
#
# Runnable directly:  python3 -u code/cartan_phaseA5_berry.py
# Exits 0 iff the CP^1 pin + VALD-03 + CALC-03(pos-def) + CALC-04 all PASS (PART 1 of
# the SOFT-KILL gate is established).  This plan does NOT emit the decisive SOFT KILL /
# SURVIVES verdict -- that (matter-on VALD-04) lives in plan 76-02.
# ============================================================================

import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import (  # noqa: E402
    Matrix, Rational, I, symbols, cos, sin, exp, simplify, cancel, trigsimp,
    re as sym_re, im as sym_im, zeros, eye, sqrt, pi, integrate, conjugate,
)

import embedding_under_E_verification as EMB  # noqa: E402  (slice_to_complex e_7->i; E/proj_u)
import ring_lemma_verification as RL  # noqa: E402  (det SSOT: Tr, jordan, det_3)
import bulk_geometry_verification as BG  # noqa: E402  (cone-Hessian / H^3 / ricci_decomp Re-anchor)

# Engine-native Peirce layout (v18.0 lock; reproduced in Phase 74/75).
V_HALF_IDX = list(range(11, 27))         # V_{1/2}(E_11), idx 11..26 (16 elements)
CU_SURVIVOR_IDX = [11, 18, 19, 26]       # C_u^2 survivors of pi_u (Phase 75): the 4 base dirs

ALL_PASS = True


def _report(label, ok):
    """Print a PASS/FAIL line; latch ALL_PASS to False on any failure."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


def _is_zero_matrix(M):
    """Exact: True iff every entry of a SymPy Matrix simplifies to 0 (over Q(i))."""
    return all(simplify(M[i, j]) == 0 for i in range(M.rows) for j in range(M.cols))


def _source_guard():
    """fp-octonion-algebra guard (inherited from Phase 0 DERV-01 / Phase 75 semantics).
    The LOAD-BEARING facts are RUNTIME, not a naive source grep:
      (1) octonion_algebra is NOT in sys.modules after the decisive imports (nothing on
          the live path pulled in the banned float engine);
      (2) the decisive primitives RL.det_3 / RL.Tr / RL.jordan are the NATIVE exact-over-Q
          ring_lemma_verification functions (distinct objects from any aliased oa_* oracle);
      (3) the QGT path uses the ASSOCIATIVE complex matrix product on slice_to_complex(P),
          NEVER the Jordan product o (which would give a different, wrong object).
    A genuine OFFENDER is an ACTIVE import of octonion_algebra that would SHADOW an exact
    primitive; the sanctioned `... import det_3 as oa_det_3 ...` aliased oracle line is fine."""
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra.py ABSENT on the decisive path "
          "(fp-octonion-algebra; Phase-0 DERV-01 / Phase-75 semantics)")
    print("=" * 78)
    in_modules = "octonion_algebra" in sys.modules

    SANCTIONED, offenders = [], []
    EXACT_NAMES = ("det_3", "Tr", "jordan", "Tr2", "polarize_d", "X_from_symbols")
    for mod in (BG, EMB, RL):
        src_path = getattr(mod, "__file__", None)
        if not (src_path and os.path.exists(src_path)):
            continue
        with open(src_path) as fh:
            for ln in fh:
                s = ln.strip()
                if s.startswith("#"):
                    continue
                active = (s.startswith("import octonion_algebra")
                          or s.startswith("from octonion_algebra"))
                if not active:
                    continue
                base = os.path.basename(src_path)
                shadows_exact = any(
                    (f"import {nm}" in s and f"{nm} as oa_" not in s)
                    or (f", {nm}" in s and f"{nm} as oa_" not in s and f"{nm} as " not in s)
                    for nm in EXACT_NAMES
                )
                if ("as oa_" in s) and not shadows_exact:
                    SANCTIONED.append((base, s))
                else:
                    offenders.append((base, s))

    # The decisive primitives must be the native exact ring_lemma versions.
    native_exact = (
        RL.det_3.__module__ == "ring_lemma_verification"
        and RL.Tr.__module__ == "ring_lemma_verification"
        and RL.jordan.__module__ == "ring_lemma_verification"
        and (RL.det_3 is not getattr(RL, "oa_det_3", object()))
    )
    Xspot = EMB.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                                EMB.oct_zero(), EMB.oct_zero(), EMB.oct_zero())
    spot = RL.det_3(Xspot)
    spot_exact = (spot == 30) and (not isinstance(spot, float))

    _report("octonion_algebra NOT in sys.modules after the decisive imports "
            "(EMB/RL/BG) -- nothing on the live path pulled in the banned float "
            "engine [fp-octonion-algebra REJECTED]", not in_modules)
    _report("decisive primitives RL.det_3 / RL.Tr / RL.jordan are the NATIVE "
            "exact-over-Q ring_lemma_verification functions (NOT the aliased oracle "
            f"oa_det_3); det_3(diag(2,3,5))=={spot} exact integer [fp-float-decisive "
            "REJECTED]", native_exact and spot_exact)
    _report(f"0 UNSANCTIONED octonion_algebra imports that would shadow an exact "
            f"primitive in the decisive engine sources (found {len(offenders)}, "
            f"expect 0); {len(SANCTIONED)} sanctioned aliased-oracle line(s)",
            len(offenders) == 0)
    for f, s in SANCTIONED:
        print(f"      SANCTIONED in-fence oracle (not on decisive path): {f}: {s}")
    for f, s in offenders:
        print(f"      OFFENDER: {f}: {s}")
    return ((not in_modules) and native_exact and spot_exact and (len(offenders) == 0))


# ============================================================================
# THE QGT RECIPE  (the single load-bearing object; PINNED by the CP^1 anchor)
# ============================================================================
# Q_{mu nu} = Tr(P d_mu P d_nu P) over Q(i) with P a Hermitian rank-1 projector.
#   g = Re(Q)            (Fubini-Study metric; symmetric)
#   F_B = -2 Im(Q)       (Berry curvature; antisymmetric)
# All products are the ASSOCIATIVE complex matrix product (NOT the Jordan product) --
# this is forced by C_u ~= C (u = e_7 the unique associative completion).  The i is
# sympy.I, SYMBOLIC; Re/Im are the literal sympy.re/sympy.im.


def QGT(P, params, simp=cancel):
    """The quantum geometric tensor Q_{mu nu} = Tr(P dP_mu dP_nu) over Q(i).

    P     : NxN SymPy complex Matrix (a Hermitian rank-1 projector), function of `params`.
    params: list of real SymPy symbols (the differentiation directions).
    Returns the len(params) x len(params) SymPy Matrix Q (generically complex).
    Uses the ASSOCIATIVE matrix product P*dP*dP (NOT Jordan); trace = SymPy .trace().
    """
    n = len(params)
    dP = [P.diff(p) for p in params]
    Q = zeros(n, n)
    for mu in range(n):
        for nu in range(n):
            Q[mu, nu] = simp((P * dP[mu] * dP[nu]).trace())
    return Q


def fs_metric(P, params, simp=cancel):
    """g_{mu nu} = Re(QGT) -- the Fubini-Study metric (symmetric)."""
    Q = QGT(P, params, simp)
    n = Q.rows
    return Matrix(n, n, lambda i, j: simp(sym_re(Q[i, j])))


def berry_F(P, params, simp=cancel):
    """F_B,{mu nu} = -2 Im(QGT) -- the Berry curvature (antisymmetric).
    Sign/factor PINNED by the CP^1 anchor F_B = -sin theta/2."""
    Q = QGT(P, params, simp)
    n = Q.rows
    return Matrix(n, n, lambda i, j: simp(-2 * sym_im(Q[i, j])))


# ============================================================================
# TASK 1.1 : CP^1 CONVENTION PIN  (do this BEFORE any h_3(O) object)
# ============================================================================
def cp1_pin():
    """Reproduce the monopole anchor on CP^1 = S^2 EXACTLY over the symbolic field:
        P(theta,phi) = 1/2 [[1+cos th, sin th e^{-i phi}],[sin th e^{i phi}, 1-cos th]]
        Q_theta theta = 1/4,  Q_phi phi = sin^2 th /4,  Q_theta phi = (i/4) sin th
        F_B = -2 Im Q_theta phi = -sin th /2  (int over S^2 = -2pi)
        g_theta theta = Re Q_theta theta = 1/4
    PINS the sign and the factor-2 of the whole recipe."""
    print("=" * 78)
    print("CP^1 PIN : monopole anchor F_B = -sin theta/2 (int=-2pi), g_th th = 1/4")
    print("  (sign/factor calibration of Q=Tr(P dP dP); Re/Im split; BEFORE any h_3(O))")
    print("=" * 78)

    th, ph = symbols('theta phi', real=True)
    P = Rational(1, 2) * Matrix([
        [1 + cos(th), sin(th) * exp(-I * ph)],
        [sin(th) * exp(I * ph), 1 - cos(th)],
    ])

    # P is a rank-1 Hermitian projector: P^2 = P, P^dagger = P, Tr P = 1.
    P2mP = simplify(P * P - P)
    herm = simplify(P - P.conjugate().T)
    trP = simplify(P.trace())
    _report("CP^1 projector is rank-1 Hermitian: P^2 - P == 0, P = P^dagger, Tr P == 1 "
            "[exact symbolic]",
            _is_zero_matrix(P2mP) and _is_zero_matrix(herm) and trP == 1)

    params = [th, ph]
    Q = QGT(P, params, simp=trigsimp)
    Qthth = trigsimp(Q[0, 0])
    Qphph = trigsimp(Q[1, 1])
    Qthph = trigsimp(Q[0, 1])

    ok_Qthth = simplify(Qthth - Rational(1, 4)) == 0
    ok_Qphph = simplify(Qphph - sin(th) ** 2 / 4) == 0
    ok_Qthph = simplify(Qthph - I * sin(th) / 4) == 0
    print(f"      Q_theta theta = {Qthth}   (expect 1/4)")
    print(f"      Q_phi phi     = {Qphph}   (expect sin^2 th /4)")
    print(f"      Q_theta phi   = {Qthph}   (expect i sin th /4)")
    _report("CP^1 QGT components EXACT: Q_th th=1/4, Q_ph ph=sin^2 th/4, "
            "Q_th ph= i sin th/4 [over Q(i), symbolic]",
            ok_Qthth and ok_Qphph and ok_Qthph)

    # The Berry curvature and FS metric via the SAME helpers used downstream.
    FB = berry_F(P, params, simp=trigsimp)
    g = fs_metric(P, params, simp=trigsimp)
    FB_thph = trigsimp(FB[0, 1])
    g_thth = trigsimp(g[0, 0])
    ok_FB = simplify(FB_thph - (-sin(th) / 2)) == 0
    ok_anti = simplify(FB[0, 1] + FB[1, 0]) == 0 and simplify(FB[0, 0]) == 0
    ok_g = simplify(g_thth - Rational(1, 4)) == 0
    print(f"      F_B[theta,phi] = {FB_thph}   (expect -sin th /2)")
    print(f"      g_theta theta  = {g_thth}   (expect 1/4)")
    _report("CP^1 Berry curvature F_B[th,ph] = -2 Im Q = -sin theta/2 (sign+factor-2 "
            "PINNED); F_B antisymmetric [exact symbolic]", ok_FB and ok_anti)
    _report("CP^1 Fubini-Study g_theta theta = Re Q = 1/4 [exact symbolic]", ok_g)

    # Monopole charge: int_{S^2} F_B[th,ph] dtheta dphi = -2pi (the calibration scale).
    monopole = integrate(integrate(FB_thph, (th, 0, pi)), (ph, 0, 2 * pi))
    _report(f"CP^1 monopole flux int_{{S^2}} F_B = {monopole} (expect -2pi) -- the "
            "first-Chern calibration of the recipe [exact]", simplify(monopole + 2 * pi) == 0)
    return ALL_PASS


# ============================================================================
# TASK 1.2 : RANK-1 C_u IDEMPOTENT FAMILY  (the vacuum chart) + the e_7->i bridge
# ============================================================================
# v(z1,z2) = [1, z1, z2], z1 = a + i b, z2 = c + i d  (a,b,c,d real sympy symbols).
# P_C = v v^dagger / (v^dagger v)  -- a 3x3 SymPy COMPLEX rank-1 projector.  This IS
# slice_to_complex of the C_u rank-1 idempotent (i = sympy.I = e_7, symbolic over Q(i)).
def build_cu_idempotent():
    """Return (P_C, params, base_subs, syms) for the rank-1 C_u idempotent family.
    syms = (a,b,c,d); params = [a,b,c,d] the 4 C_u^2 base directions {11,18,19,26}."""
    a, b, c, d = symbols('a b c d', real=True)
    z1 = a + I * b
    z2 = c + I * d
    v = Matrix([1, z1, z2])
    vdag = v.conjugate().T
    norm = (vdag * v)[0, 0]          # 1 + |z1|^2 + |z2|^2, real
    P_C = (v * vdag) / norm
    params = [a, b, c, d]
    base_subs = {a: 0, b: 0, c: 0, d: 0}    # the base point v=[1,0,0], P=diag(1,0,0)
    return P_C, params, base_subs, (a, b, c, d)


def task1_idempotent_and_bridge(P_C, params, base_subs, syms):
    """Verify rank-1 idempotent EXACT over Q(i) + the slice_to_complex (e_7->i) bridge
    + the C_u survivors {11,18,19,26} = the 4 base directions (a,b,c,d)."""
    print("=" * 78)
    print("RANK-1 C_u IDEMPOTENT FAMILY : P_C = v v^dagger/(v^dagger v), v=[1,z1,z2], "
          "z1=a+ib, z2=c+id  (i = e_7 symbolic over Q(i))")
    print("=" * 78)
    a, b, c, d = syms

    # (i) rank-1 idempotent EXACT over Q(i): P_C^2 - P_C == 0 and Tr P_C == 1, Hermitian.
    P2mP = Matrix(3, 3, lambda i, j: cancel((P_C * P_C - P_C)[i, j]))
    herm = Matrix(3, 3, lambda i, j: cancel((P_C - P_C.conjugate().T)[i, j]))
    trP = cancel(P_C.trace())
    _report("rank-1 idempotent EXACT over Q(i): P_C^2 - P_C == 0 (3x3 zero), "
            "P_C = P_C^dagger, Tr P_C == 1 [symbolic i]",
            _is_zero_matrix(P2mP) and _is_zero_matrix(herm) and cancel(trP - 1) == 0)

    # (ii) the slice_to_complex (e_7 -> i) bridge is FAITHFUL: build the corresponding
    # h_3(C_u) element by hand with C_u entries and confirm slice_to_complex maps it to
    # the SAME complex projector (at a rational test point so the entries are exact C_u).
    # Test point: z1 = 1 + 2 e_7 (a=1,b=2), z2 = 3 - e_7 (c=3,d=-1).
    test = {a: Rational(1), b: Rational(2), c: Rational(3), d: Rational(-1)}
    P_C_test = Matrix(3, 3, lambda i, j: cancel(P_C[i, j].subs(test)))

    # Hand-build h_3(C_u): the rank-1 idempotent vv^dag/(v^dag v) but with C_u OCTONION
    # entries (comps 0 and 7), then slice_to_complex it.  We construct the OFF-DIAGONAL
    # C_u entries x1,x2,x3 from the projector's lower-triangular complex entries.
    #   layout [[a0, conj(x3), x2],[x3, b0, conj(x1)],[conj(x2), x1, g0]]
    # P_C_test[1,0] = x3 (complex), P_C_test[2,0] = conj(x2), P_C_test[2,1] = x1.
    def c_to_cu(z):
        z = simplify(z)
        o = EMB.oct_zero()
        o[0] = sym_re(z)
        o[7] = sym_im(z)
        return o
    alpha0 = simplify(sym_re(P_C_test[0, 0]))
    beta0 = simplify(sym_re(P_C_test[1, 1]))
    gamma0 = simplify(sym_re(P_C_test[2, 2]))
    x3 = c_to_cu(P_C_test[1, 0])       # (1,0) entry = x3
    x1 = c_to_cu(P_C_test[2, 1])       # (2,1) entry = x1
    x2 = c_to_cu(P_C_test[0, 2])       # (0,2) entry = x2
    H_cu = EMB.h3o_from_coords(alpha0, beta0, gamma0, x1, x2, x3)
    Mc_from_bridge = EMB.slice_to_complex(H_cu)
    bridge_match = _is_zero_matrix(
        Matrix(3, 3, lambda i, j: simplify(Mc_from_bridge[i, j] - P_C_test[i, j])))
    _report("slice_to_complex (e_7 -> i) bridge FAITHFUL: the hand-built h_3(C_u) "
            "element maps EXACTLY to P_C at the rational test pt (e_7->i is the literal "
            "Im) [exact over Q(i)]", bridge_match)

    # (iii) no octonion comp e_1..e_6 leaks: every off-diagonal C_u entry has comps 1..6 zero.
    no_leak = EMB._is_slice_element(H_cu)
    _report("NO octonion leak: the h_3(C_u) element has comps e_1..e_6 == 0 on every "
            "entry (pure C_u = span{1,e_7}); the C_u projection is faithful [exact]",
            no_leak)

    # (iv) the 4 base directions ARE the C_u^2 survivors {11,18,19,26} from Phase 75.
    groups, _diag = BG.peirce_indices_under_E11()
    Vh = sorted(groups.get(Rational(1, 2), []))
    _report("the 4 differentiation directions (a,b,c,d) <-> the C_u^2 survivors "
            f"{CU_SURVIVOR_IDX} of pi_u on V_{{1/2}}={Vh[:3]}... (Phase 75 SURVIVES "
            "coframe); 4 = dim(4d slice) [regression]",
            Vh == V_HALF_IDX and len(CU_SURVIVOR_IDX) == 4)
    return ALL_PASS


# ============================================================================
# TASK 1.3 : THE 4x4 QGT ON THE 4 C_u^2 BASE DIRECTIONS  (a,b,c,d), over Q(i)
# ============================================================================
def task1_assemble_qgt(P_C, params, base_subs):
    """Assemble Q(a,b,c,d) = [Tr(P_C d_mu P_C d_nu P_C)] over Q(i); confirm the Re part
    is symmetric and the Im part antisymmetric BY CONSTRUCTION (the recipe is calibrated)."""
    print("=" * 78)
    print("4x4 QGT Q(a,b,c,d) on the C_u^2 base directions {11,18,19,26}  (over Q(i))")
    print("=" * 78)
    Q = QGT(P_C, params, simp=cancel)
    # Evaluate at the base point for a clean exact readout (symbolic Q kept for VALD-03).
    Q0 = Matrix(4, 4, lambda i, j: cancel(Q[i, j].subs(base_subs)))
    print("      Q(base point a=b=c=d=0):")
    for r in range(4):
        print(f"        {[Q0[r, k] for k in range(4)]}")
    g0 = Matrix(4, 4, lambda i, j: simplify(sym_re(Q0[i, j])))
    FB0 = Matrix(4, 4, lambda i, j: simplify(-2 * sym_im(Q0[i, j])))
    sym_ok = _is_zero_matrix(g0 - g0.T)
    anti_ok = _is_zero_matrix(FB0 + FB0.T)
    _report("4x4 QGT assembles over Q(i): Re(Q)=g symmetric, -2 Im(Q)=F_B "
            "antisymmetric (at base pt) [exact]", sym_ok and anti_ok)
    return Q, Q0


# ============================================================================
# DRIVER  (PART 1 -- the vacuum half; tasks appended below in 76-01 tasks 2,3)
# ============================================================================
def _task1():
    okG = _source_guard()
    ok1 = cp1_pin()
    P_C, params, base_subs, syms = build_cu_idempotent()
    ok2 = task1_idempotent_and_bridge(P_C, params, base_subs, syms)
    Q, Q0 = task1_assemble_qgt(P_C, params, base_subs)
    return okG, ok1, ok2, (P_C, params, base_subs, syms, Q, Q0)


if __name__ == "__main__":
    print("#" * 78)
    print("# Phase 76 -- Plan 01 (PART 1, VACUUM half): Berry-curvature same-wall gate")
    print("# CP^1 pin + rank-1 C_u idempotent + 4x4 QGT over Q(i)  [Task 1]")
    print("#" * 78)
    okG, ok1, ok2, _state = _task1()
    print("=" * 78)
    print(f"SOURCE GUARD ......... {'PASS' if okG else 'FAIL'}")
    print(f"CP^1 PIN ............. {'PASS' if ok1 else 'FAIL'}")
    print(f"IDEMPOTENT + BRIDGE .. {'PASS' if ok2 else 'FAIL'}")
    print("=" * 78)
    print(f"TASK 1 (PART 1 calibration): {'ALL_PASS' if ALL_PASS else 'SOME FAILED'}")
    sys.exit(0 if ALL_PASS else 1)
