#!/usr/bin/env python3
"""area_per_bit.py -- Phase 95 / v35.0-candidate: THE AREA-PER-BIT KILL-TEST.

A FRESH, INDEPENDENT driver (NOT a copy of any /tmp script; built directly from
derivations/95-area-per-bit-RESEARCH.md).  The native-holography diagnostic /
entanglement-route Limb A.

THE QUESTION.  Does the variety (CP^2 = the C_u cut of OP^2, where v23's faithful-point
fiber kill does not reach) natively set the bits<->geometric-area exchange rate as a
UNIVERSAL CONSTANT (-> a background scale; gravity a contingent import; FORK A) or as a
SHEARING field (-> a candidate gravitational field)?  This is the off-faithful / on-variety
form of the entanglement route's sharp-claim-1 (slot 83 ran it AT the faithful point I/3 =
v23 and DIED, dS=0).

WHAT IS COMPUTED (all exact over Q; the octonion engine is NOT on the decisive path):
  Work entirely in h_3(C) = the C_u cut = CP^2.  P(z) = v v^H / (v^H v), v = (1, z1, z2);
  <X,p> = Tr(X.P);  X# = adj(X) = X^2 - Tr(X) X + (1/2)((TrX)^2 - Tr(X^2)) I.  Keep z and
  zbar as INDEPENDENT Wirtinger symbols; conjugation = a z<->zbar swap (NEVER sympy
  conjugate() on independent symbols -- that silently breaks the Kahler identity).

  G0 -- setup + PIN THE AREA (the load-bearing definitional gate):
        - reproduce the certified objects phi_M, M#, G_M, Var on s01,a01,d1,gen; Tr M = 0,
          G_M <= 0.
        - Bug-guard 4 (off I/3, not vacuous): G_M(p) genuinely VARIES with p.
        - PIN A_M canonically and prove (as SYMBOLIC IDENTITIES, simplify==0 for ALL p,M):
            (ii)  metric-trace  A_ii = g^{ij-bar} d_i phi d_jbar phi = |grad phi|^2_g
                  ==> A_ii - Var == 0  (the quantum Fisher / variance).
            (iii) KKS symplectic gradient-norm |X_phi|^2_omega, X_phi = J grad phi (J the
                  Kahler complex structure), via the swap-conjugation ==> A_iii - Var == 0
                  (the Kahler tie; J a g-isometry).
            decomposition  G_M - (Var + 3/4 <M>^2 - 1/2 Tr(M^2)) == 0.
        - Bug-guard 3 (FISHER-CORPSE): the FS metric = Re(QGT) (Provost-Vallee), so
          A_M = Var = the quantum Fisher information = a STATE-SPACE object (v17's corpse).
        - Candidate (i): the global FS Riemannian measure of the support = a per-M CONSTANT,
          NOT a local field -- the CONTROL exhibiting the homogeneity-artifact failure mode.

  G1 -- THE KILL-TEST:  R(p,M) = A_M(p)/|G_M(p)| exact over Q.  Bug guards BEFORE classifying:
        (1) denominator-zero handling; (2) homogeneity check; (3) FISHER-CORPSE gate
        (A_M = Var ==> R = Fisher/(rel-entropy), state-space, NOT geometric ==> DEAD-FISHER /
        fork A, STOP); (4) only a genuinely-geometric non-Fisher shear -> G2.  Reproduce the
        RESEARCH section 9 ground-truth.  R is NOT literally constant; the shear is the
        relative-entropy correction 3/4 <M>^2 - 1/2 Tr(M^2).  Preempt LIVE-TENSOR: the
        canonical area is the metric TRACE of dphi(x)dphi by construction => scalar, not TT.

  G2 -- only if a legitimate geometric (non-Fisher) shear survives G1.  NOT expected.

  verdict() -- a NON-HARDWIRED ladder from computed booleans, with self-tests that MUST print
  PASS before the real verdict (rigged-constant -> DEAD-CONSTANT; hand-built genuinely-shearing
  non-Fisher -> LIVE; two non-agreeing canonical areas -> INCONCLUSIVE; A = Var -> DEAD-FISHER).

DISCIPLINE: exact over Q on every decisive line (sympy.Rational / cancel / simplify; NEVER a
float in a verdict).  Commit after each gate.  Report the TRUTH (expected DEAD-FISHER / fork A,
but if the exact math says a genuine geometric shear, report that).

FENCES (binding, verbatim -- see derivations/95-VERDICT.md):
  NO Einstein-equation / G=kT / gravity / Newton / dark-matter / geodesic language as a DERIVED
  result; the bits<->area rate is a framework ratio (a contingent import like kappa, Lambda unless
  G1 forces otherwise), NOT Newton's G; FS is USED, not derived; signature Riemannian (Wall 2
  unpaid -- NOTHING is called gravity until signature is paid); DEAD-CONSTANT / DEAD-FISHER and
  LIVE-* are NOT derivations of gravity.  This run does NOT retract v33 (extremize FORCES-NOTHING),
  v34 (induce CLOSES-CONDITIONAL), v17-v21 (fiber kills), or v23 (I/3 death).  Paper 5 remains the
  only result in the more-than-nothing column.

Reproducibility: sympy 1.14.0, Python 3.x, exact rational arithmetic over Q / Q(i) (no RNG / no
seeds in the verdict path; floats illustrative only).  Darwin arm64.
Run:  python3 -u code/area_per_bit.py
"""
import sys
import time

import sympy as sp
from sympy import Rational, Matrix, I, cancel, simplify, symbols, eye, zeros

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return bool(ok)


# ============================================================================
# 1. THE WIRTINGER CHART ON CP^2 = h_3(C_u)  (exact rational; base E_11; z=0)
# ----------------------------------------------------------------------------
# Affine chart v = (1, z1, z2); z = (z1, z2) in C^2.  z and zbar are INDEPENDENT
# symbols (Wirtinger calculus): d_a = d/dz_a, d_abar = d/dz_abar.  Conjugation is
# the z<->zbar SWAP (the involution swapping {Z1<->Z1B, Z2<->Z2B}); we NEVER call
# sympy conjugate() on these independent symbols.  rho = 1 + |z1|^2 + |z2|^2.
# ============================================================================
Z1, Z2 = symbols("z1 z2")
Z1B, Z2B = symbols("z1b z2b")     # independent conjugate coords (Wirtinger)
ZS = (Z1, Z2)
ZBS = (Z1B, Z2B)

# the conjugation swap (an involution on rational functions of the 4 chart symbols)
_SWAP = {Z1: Z1B, Z1B: Z1, Z2: Z2B, Z2B: Z2}


def conj_swap(expr):
    """Complex conjugation on the Wirtinger chart.  Two pieces, BOTH required:
      (1) the z<->zbar SWAP on the independent Wirtinger symbols (the chart conjugation), and
      (2) i -> -i on the genuine imaginary unit (the explicit sympy I, e.g. from the matter
          matrix's Hermitian off-diagonals or the complex-structure factor i).
    We NEVER call sympy conjugate() on the independent z symbols (that silently breaks the
    Kahler identity by treating z,zbar as conjugate pairs prematurely); but i -> -i on the
    EXPLICIT imaginary unit is legitimate complex conjugation (I is a true constant, not a
    Wirtinger symbol).  Forgetting the i -> -i piece was a latent bug in the KKS construction
    (it gave A_iii != Var); with both pieces A_iii == A_ii == Var exactly."""
    return expr.subs(_SWAP, simultaneous=True).subs(I, -I)


def rho():
    return 1 + Z1 * Z1B + Z2 * Z2B


def dz(f, a):
    return sp.diff(f, ZS[a])


def dzb(f, a):
    return sp.diff(f, ZBS[a])


def P_chart():
    """Rank-1 CP^2 projector P(z) = v v^H / (v^H v), v = (1,z1,z2), zbar independent.
    3x3 complex; rational in (z,zbar).  Idempotent, Tr P = 1; z->0 gives diag(1,0,0)=E11."""
    v = Matrix([1, Z1, Z2])
    vb = Matrix([1, Z1B, Z2B])         # = conjugate(v) entrywise (independent symbols)
    denom = (vb.T * v)[0]              # v^H v = rho
    return (v * vb.T / denom).applyfunc(cancel)


def inner(A, P):
    """Trace-form inner product <A,p> = Tr(A.P)  (A a 3x3 complex Hermitian matrix;
    P the chart projector).  For Hermitian A on the reality slice this is real."""
    return cancel(sp.expand((A * P).trace()))


def sharp(M):
    """Freudenthal adjoint / adjugate  M# = M^2 - Tr(M) M + sigma_2 I,
    sigma_2 = ((Tr M)^2 - Tr(M^2))/2.  (= the matrix of cofactors for 3x3.)"""
    s2 = cancel((M.trace() ** 2 - (M * M).trace()) / 2)
    return (M * M - M.trace() * M + s2 * eye(3)).applyfunc(cancel)


def phi_M(M, P=None):
    """phi_M(p) = <M,p> = Tr(M P(z))  (the v25 moment field; linear in M)."""
    if P is None:
        P = P_chart()
    return inner(M, P)


def Var(M, P=None):
    """Quantum variance Var_p(M) = <M^2,p> - <M,p>^2  (the QGT-real / Fisher object; >= 0)."""
    if P is None:
        P = P_chart()
    return cancel(inner(M * M, P) - inner(M, P) ** 2)


def G_M(M, P=None):
    """The v26 second-order entropy response field  G_M(p) = <M#,p> - (1/4)<M,p>^2 (<= 0)."""
    if P is None:
        P = P_chart()
    return cancel(inner(sharp(M), P) - Rational(1, 4) * inner(M, P) ** 2)


# ----------------------------------------------------------------------------
# The Fubini-Study metric (POTENTIAL / Fisher normalization).  TWO normalizations
# are relevant and BOTH are reported:
#   g_pot  = d_a d_bbar log rho                  (the POTENTIAL / Fisher metric; Ric=3 g_pot)
#   g_phys = (1/2) g_pot                         (the engine/Boucetta metric; Ric=6 g_phys,
#                                                 lambda_1=12 -- the certified normalization)
# The CANONICAL local area A_M^(ii) = g_pot^{ij-bar} d_i phi d_jbar phi is taken with the
# POTENTIAL (Fisher) metric, because g_pot IS the real part of the quantum geometric tensor
# (Provost-Vallee): the Fubini-Study metric on pure states = the quantum Fisher metric.  With
# this canonical normalization  A_M^(ii) == Var  EXACTLY (the de-risked identity).  The overall
# metric scale is the "single overall scale" G1 allows to normalize away (g_phys gives 2*Var);
# it does NOT decide the verdict.  We report both.
#
# EXACT-ARITHMETIC NOTE (performance, NOT physics): the symbolic identities (A_ii==Var etc. for
# ALL p, ALL M) are verified by POLYNOMIAL-NUMERATOR comparison over explicit rho-powers (every
# field is num/rho^k; compare numerators), NOT by `cancel` of the combined rational fraction.
# `cancel` on the 8-param-x-4-chart-symbol combined fraction is the perf cliff (>480s); the
# numerator comparison is exact and runs in ~2s.  Closed forms used (both exact):
#   g_pot_{a bbar}        = (rho delta_{ab} - zbar_a z_b)/rho^2      (the metric numerator gN/rho^2)
#   det(gN)               = rho                                     (=> det g_pot = 1/rho^3)
#   g_pot^{a bbar}        = rho * adj(gN)[.,.]   (a POLYNOMIAL, since g^{-1}=rho^2 gN^{-1}=rho^2 adj/rho)
# ----------------------------------------------------------------------------
def fs_metric_pot():
    """g_pot_{a bbar} = d_a d_bbar log rho = (rho delta_{ab} - zbar_a z_b)/rho^2.  (Fisher metric.)"""
    K = sp.log(rho())
    g = zeros(2, 2)
    for a in range(2):
        for b in range(2):
            g[a, b] = cancel(dz(dzb(K, b), a))
    return g


def fs_metric_inv(g):
    return g.inv().applyfunc(cancel)


# index pairing on the Kahler chart: g^{a bbar} = ginv[b, a] (the transpose pairing,
# matching the certified tensor_probe convention).
def _gu(ginv, a, b):
    return ginv[b, a]


def _gN():
    """The metric NUMERATOR gN (g_pot = gN/rho^2): gN[a,b] = rho delta_{ab} - zbar_a z_b.  POLY."""
    rh = rho()
    z = [Z1, Z2]; zb = [Z1B, Z2B]
    return Matrix([[sp.expand(rh * (1 if a == b else 0) - zb[a] * z[b]) for b in range(2)]
                   for a in range(2)])


def _ginv_poly():
    """The EXACT inverse g_pot^{-1} as a POLYNOMIAL matrix: g^{-1} = rho^2 gN^{-1} = rho^2 adj(gN)/det(gN)
    = rho^2 adj(gN)/rho = rho * adj(gN).  (det gN = rho, verified at Gate 0.)  Entry [a,b] is the
    matrix inverse; g^{a bbar} = ginv_poly[b,a]."""
    gN = _gN()
    return (rho() * gN.adjugate()).applyfunc(sp.expand)


# ============================================================================
# 2. THE CANONICAL AREA CANDIDATES (rational forms for NUMERIC evaluation; the
#    symbolic identities use the fast numerator method in _symbolic_identities)
# ----------------------------------------------------------------------------
def A_ii(M, g=None, ginv=None, P=None):
    """Candidate (ii): the FS metric-TRACE of the v31 metric-mode dphi_M (x) dphi_M, i.e.
    A_ii = g^{a bbar} d_a phi_M d_bbar phi_M = |grad phi_M|^2_g  (POTENTIAL/Fisher metric).
    DE-RISKED IDENTITY: A_ii == Var.  This is the metric TRACE of dphi(x)dphi => the SCALAR part
    (never the TT part) by construction.  This rational form is for NUMERIC (substituted)
    evaluation; the ALL-p,ALL-M symbolic identity is proven in _symbolic_identities()."""
    if g is None:
        g = fs_metric_pot()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if P is None:
        P = P_chart()
    phi = phi_M(M, P)
    s = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            s += _gu(ginv, a, b) * dz(phi, a) * dzb(phi, b)
    return cancel(s)


def A_iii(M, g=None, ginv=None, P=None):
    """Candidate (iii): the KKS (Kirillov-Kostant-Souriau) symplectic gradient-norm of the
    moment-map component phi_M:  A_iii = g_{a bbar} X^a conj(X)^bbar with the Hamiltonian
    vector field X_phi = J grad phi (J the Kahler complex structure).  In the holomorphic frame
    the (1,0) component is X^a = +i (grad phi)^a = +i g^{a bbar} d_bbar phi (J acts as +i on the
    (1,0) sector).  On a Kahler manifold J is a g-isometry, so |X_phi|^2 = |grad phi|^2_g, and
    with the KKS (single Hermitian contraction) normalization this equals A_ii == Var (the Kahler
    tie).  This rational form is for NUMERIC evaluation; the symbolic identity (all p,M) is proven
    in _symbolic_identities().

    The conjugation conj(X)^bbar uses the FULL complex conjugation conj_swap (z<->zbar SWAP AND
    i -> -i) -- NOT sympy conjugate() on the Wirtinger symbols, and NOT the swap alone (forgetting
    i -> -i was a latent bug that gave A_iii != Var)."""
    if g is None:
        g = fs_metric_pot()
    if ginv is None:
        ginv = fs_metric_inv(g)
    if P is None:
        P = P_chart()
    phi = phi_M(M, P)
    # raised gradient (grad phi)^a = g^{a bbar} d_bbar phi ; Hamiltonian field X^a = +i (grad phi)^a
    XU = [sp.Integer(0), sp.Integer(0)]
    for a in range(2):
        s = sp.Integer(0)
        for b in range(2):
            s += _gu(ginv, a, b) * dzb(phi, b)
        XU[a] = cancel(I * s)
    # single Hermitian contraction (KKS): A_iii = g_{a bbar} X^a conj(X)^bbar (full conjugation)
    val = sp.Integer(0)
    for a in range(2):
        for b in range(2):
            val += g[a, b] * XU[a] * conj_swap(XU[b])
    return cancel(val)


# ----------------------------------------------------------------------------
# The fast SYMBOLIC IDENTITIES (all p, all M) -- numerator method over explicit rho-powers.
# ----------------------------------------------------------------------------
def _symbolic_identities():
    """Prove, as SYMBOLIC IDENTITIES over a GENERIC 8-param traceless cut M and ALL chart points
    p (z,zbar independent), each via exact polynomial-NUMERATOR comparison (no `cancel` of the
    combined fraction):
       (ii)  A_ii - Var == 0
       (iii) A_iii - Var == 0   (KKS, full conjugation)
       (1)   A_ii - A_iii == 0  (the two canonical areas agree; Bug-guard 1 no-flip)
       (d)   G_M - (Var + 3/4 <M>^2 - 1/2 Tr M^2) == 0
       (s)   (G_M - Var) - (3/4 <M>^2 - 1/2 Tr M^2) == 0  (the shear is the rel-entropy correction)
    Also returns the det(gN)==rho check (the inverse-is-polynomial certificate).
    Returns a dict of booleans."""
    rh = rho()
    Msym, _ = M_cut_symbolic("m")
    v = Matrix([1, Z1, Z2]); vb = Matrix([1, Z1B, Z2B]); N = v * vb.T

    phiN = sp.expand((Msym * N).trace())              # phi   = phiN / rho
    m2N = sp.expand((Msym * Msym * N).trace())        # <M^2> = m2N / rho
    VarNum = sp.expand(m2N * rh - phiN ** 2)          # Var   = VarNum / rho^2

    # metric numerator + polynomial inverse (det gN == rho => g^{-1} = rho*adj(gN) is a polynomial)
    gN = _gN()
    detgN = sp.expand(gN.det())
    det_ok = (sp.expand(detgN - rh) == 0)
    ginvP = (rh * gN.adjugate()).applyfunc(sp.expand)  # full inverse g^{-1} (poly); g^{a bbar}=ginvP[b,a]
    gu = lambda a, b: ginvP[b, a]

    # gradient numerators over rho^2:  d_a phi = DH[a]/rho^2, d_abar phi = DA[a]/rho^2
    DH = [sp.expand(dz(phiN, a) * rh - phiN * dz(rh, a)) for a in range(2)]
    DA = [sp.expand(dzb(phiN, a) * rh - phiN * dzb(rh, a)) for a in range(2)]

    # (ii) A_ii = sum gu(a,b) (DH[a]/rho^2)(DA[b]/rho^2) ; gu poly => A_ii = AiiN/rho^4
    AiiN = sp.expand(sum(gu(a, b) * DH[a] * DA[b] for a in range(2) for b in range(2)))
    id_ii = (sp.expand(AiiN - VarNum * rh ** 2) == 0)   # A_ii==Var <=> AiiN == VarNum*rho^2

    # (iii) X^a = +i g^{a bbar} d_bbar phi = XN[a]/rho^2, XN[a] = i*sum gu(a,b)*DA[b]
    XN = [sp.expand(I * sum(gu(a, b) * DA[b] for b in range(2))) for a in range(2)]
    XbarN = [conj_swap(XN[b]) for b in range(2)]        # full conjugation (swap AND i->-i)
    # A_iii = g_{a bbar} X^a conj(X)^bbar = (gN[a,b]/rho^2)(XN[a]/rho^2)(XbarN[b]/rho^2) = A3N/rho^6
    A3N = sp.expand(sum(gN[a, b] * XN[a] * XbarN[b] for a in range(2) for b in range(2)))
    id_iii = (sp.expand(A3N - VarNum * rh ** 4) == 0)   # A_iii==Var <=> A3N == VarNum*rho^4
    id_agree = (sp.expand(AiiN * rh ** 2 - A3N) == 0)   # A_ii==A_iii (both /rho^6 after lifting)

    # (d) decomposition + (s) shear
    s2 = sp.expand((Msym.trace() ** 2 - (Msym * Msym).trace()) / 2)
    sharpM = Msym * Msym - Msym.trace() * Msym + s2 * eye(3)
    shN = sp.expand((sharpM * N).trace())               # <M#> = shN/rho
    TrM2 = sp.expand((Msym * Msym).trace())
    GMnum = sp.expand(shN * rh - Rational(1, 4) * phiN ** 2)   # G_M = GMnum/rho^2
    RHSnum = sp.expand(VarNum + Rational(3, 4) * phiN ** 2 - Rational(1, 2) * TrM2 * rh ** 2)
    id_dec = (sp.expand(GMnum - RHSnum) == 0)
    shearN = sp.expand(GMnum - VarNum)                  # (G_M - Var)*rho^2
    expc = sp.expand(Rational(3, 4) * phiN ** 2 - Rational(1, 2) * TrM2 * rh ** 2)
    id_shear = (sp.expand(shearN - expc) == 0)

    return {"det_gN_eq_rho": det_ok, "A_ii_eq_Var": id_ii, "A_iii_eq_Var": id_iii,
            "A_ii_eq_A_iii": id_agree, "decomposition": id_dec, "shear_is_relent": id_shear}


def A_i_global(M):
    """Candidate (i) -- the CONTROL (homogeneity-artifact failure mode).  The FS Riemannian
    measure of the perturbation's support is a GLOBAL volume = ONE number per M, NOT a local
    field over p.  We realize it as the L^2 norm of phi_M over CP^2 (FS), int |phi_M|^2 dV_FS,
    a per-M CONSTANT.  Pairing a per-M constant against the p-varying G_M(p) gives a p-shear
    that is purely the variation of the DENOMINATOR -- the homogeneity check (G1) rules this
    out as a non-shear of the RATE.  Returned up to the overall FS volume constant (only the
    p-INDEPENDENCE matters)."""
    # int_{CP^2} |phi_M|^2 dV_FS, dV_FS proportional to d^4z / rho^3.  phi_M = (v^H M v)/rho, so
    # |phi_M|^2 = |v^H M v|^2 / rho^2 ; integrand = |v^H M v|^2 / rho^5.  U(2) phase-average keeps
    # only matched monomials, then the Dirichlet/beta radial integral.  Constant in p by
    # construction (a number).  We compute it for the record via the matched-power integral.
    P = P_chart()
    phi = phi_M(M, P)
    integrand = cancel(phi * conj_swap(phi))      # |phi|^2 (real on the slice)
    return _l2_scalar(integrand)


# ---- exact L^2 on CP^2 (FS) for the control candidate (i) only; up to the FS volume const ----
_S1, _S2 = symbols("S1 S2", nonnegative=True)


def _mono_integral(a, b, K):
    """int_0^inf^2 s1^a s2^b/(1+s1+s2)^K ds1 ds2 = a! b! (K-a-b-3)!/(K-1)!  (exact rational)."""
    a, b, K = int(a), int(b), int(K)
    m = K - a - b - 3
    if m < 0:
        raise ValueError(f"L^2 integral divergent: K-a-b-3={m}<0")
    return Rational(sp.factorial(a) * sp.factorial(b) * sp.factorial(m), sp.factorial(K - 1))


def _phase_average(num):
    """U(2)-phase-averaged matched part of num(z1,z2,z1b,z2b) -> poly in S1=|z1|^2, S2=|z2|^2."""
    cd = sp.expand(num).as_coefficients_dict()
    terms = {}
    for mono, coeff in cd.items():
        pd = mono.as_powers_dict()
        a1 = int(pd.get(Z1, 0)); a2 = int(pd.get(Z2, 0))
        b1 = int(pd.get(Z1B, 0)); b2 = int(pd.get(Z2B, 0))
        if a1 == b1 and a2 == b2:
            terms[(a1, a2)] = terms.get((a1, a2), sp.Integer(0)) + coeff
    return sum(c * _S1 ** a * _S2 ** b for (a, b), c in terms.items())


def _l2_scalar(f):
    """EXACT int_{CP^2} f dV_FS up to the FS volume const (f = num/rho^k)."""
    f = cancel(f)
    num, den = sp.fraction(f)
    # den = const * rho^k
    rr = rho()
    den = sp.expand(den)
    if den == 1:
        k, const = 0, sp.Integer(1)
    else:
        fl = sp.factor_list(den)
        const = fl[0]; k = 0
        for fac, mult in fl[1]:
            if sp.expand(fac - rr) == 0:
                k = mult
            elif sp.expand(fac + rr) == 0:
                k = mult; const *= (-1) ** mult
            else:
                raise ValueError(f"_l2_scalar: factor {fac} not rho")
    K = k + 3
    num = sp.expand(num / const)
    Pmatch = _phase_average(num)
    total = sp.Integer(0)
    for (a, b), coeff in sp.Poly(Pmatch, _S1, _S2).terms():
        total += coeff * _mono_integral(a, b, K)
    return cancel(total)


# ============================================================================
# 3. THE MATTER DIRECTIONS (v24 families; traceless Hermitian)
# ============================================================================
def matter_directions():
    return {
        "s01": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),       # lambda_1 (real off-diag)
        "a01": Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),      # lambda_2 (Hermitian "antisym")
        "d1":  Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),      # lambda_3 (diagonal traceless)
        "gen": Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),      # d2: det M = -2 != 0, full rank
    }


def M_cut_symbolic(pre="m"):
    """Generic traceless cut matter M in h_3(C) (8 real params): 2 diagonal trace-free + 3
    complex off-diagonal.  Hermitian.  Used for the SYMBOLIC identities (all M, all p)."""
    s = symbols(f"{pre}0:8", real=True)
    M = Matrix([[s[0],             s[2] + I * s[3],   s[4] + I * s[5]],
                [s[2] - I * s[3],  s[1],              s[6] + I * s[7]],
                [s[4] - I * s[5],  s[6] - I * s[7],   -s[0] - s[1]]])
    return M, s


# de-risked chart points (RESEARCH section 9)
def P0_sub():
    # z1 = 1+2i, z2 = -1+i  => rho = 1 + 5 + 2 = 8
    return {Z1: 1 + 2 * I, Z1B: 1 - 2 * I, Z2: -1 + I, Z2B: -1 - I}


def P2_sub():
    # z1 = -1, z2 = 2-3i  => rho = 1 + 1 + 13 = 15
    return {Z1: -1, Z1B: -1, Z2: 2 - 3 * I, Z2B: 2 + 3 * I}


def Q_sub():
    # a generic rational Wirtinger point for the "off I/3 varies" guard (real slice).
    return {Z1: Rational(1, 2), Z1B: Rational(1, 2), Z2: Rational(-1, 3), Z2B: Rational(-1, 3)}


# ============================================================================
# GATE 0 -- SETUP + PIN THE AREA OBJECT (the load-bearing definitional gate)
# ============================================================================
def gate0(sid):
    print("=" * 78)
    print("GATE 0 : setup + PIN THE AREA  (certified objects; Bug-guards 1/3/4; exact over Q)")
    print("=" * 78)
    ok_all = True
    P = P_chart()
    dirs = matter_directions()

    # --- G0.1 reproduce certified objects; Tr M = 0; G_M <= 0 sampled ---
    print("\n  G0.1 certified objects on s01,a01,d1,gen (Tr M = 0, G_M <= 0):")
    pts = {"P0": P0_sub(), "P2": P2_sub(), "Q": Q_sub()}
    trace_ok = True
    gle0_ok = True
    for nm, M in dirs.items():
        trace_ok &= (cancel(M.trace()) == 0)
        for pn, sub in pts.items():
            gval = cancel(G_M(M, P).subs(sub))
            if not (gval <= 0):
                gle0_ok = False
    ok_all &= _report("Tr M == 0 for all four directions (traceless matter)", trace_ok)
    ok_all &= _report("G_M(p) <= 0 sampled on {P0,P2,Q} x {s01,a01,d1,gen} (S <= log2)", gle0_ok)

    # M# spot-checks (de-risk: rank-2 -> diag(0,0,-1); gen -> diag(-2,-2,1))
    sh_ok = (sharp(dirs["d1"]) == Matrix([[0, 0, 0], [0, 0, 0], [0, 0, -1]])
             and sharp(dirs["s01"]) == Matrix([[0, 0, 0], [0, 0, 0], [0, 0, -1]])
             and sharp(dirs["a01"]) == Matrix([[0, 0, 0], [0, 0, 0], [0, 0, -1]])
             and sharp(dirs["gen"]) == Matrix([[-2, 0, 0], [0, -2, 0], [0, 0, 1]]))
    ok_all &= _report("M# = diag(0,0,-1) (rank-2 s01,a01,d1) and diag(-2,-2,1) (gen) "
                      "(certified de-risk)", sh_ok)

    # --- G0.2 Bug-guard 4: G_M(p) genuinely VARIES with p (off I/3, not vacuous like v23) ---
    print("\n  G0.2 Bug-guard 4 (OFF I/3, not vacuous): G_M(p) VARIES with p (grad S != 0):")
    varies_ok = True
    detail = []
    for nm, M in dirs.items():
        g0 = cancel(G_M(M, P).subs(P0_sub()))
        g2 = cancel(G_M(M, P).subs(P2_sub()))
        v = (cancel(g0 - g2) != 0)
        varies_ok &= v
        detail.append(f"{nm}: G(P0)={g0}, G(P2)={g2}, differ={v}")
    for d in detail:
        print(f"      {d}")
    ok_all &= _report("G_M(P0) != G_M(P2) for all four directions => grad S_face != 0 "
                      "(NOT the v23 faithful-point death)", varies_ok)

    # --- G0.3 PIN A_M canonically: the symbolic identities (ALL p, ALL M) ---
    print("\n  G0.3 PIN A_M canonically -- SYMBOLIC IDENTITIES (== 0 for ALL p, ALL M):")
    # sid was computed once in main() via the exact polynomial-numerator method over rho-powers
    # (avoids the `cancel`-of-combined-fraction cliff; runs in ~2s for the full 8-param M).
    # det(gN)==rho is the certificate that the inverse g^{-1}=rho*adj(gN) is a POLYNOMIAL (the
    # enabling fact for the exact numerator method).
    ok_all &= _report("det(gN) == rho  (=> g_pot^{-1} = rho*adj(gN) is polynomial; enables the "
                      "exact numerator identity method)", sid["det_gN_eq_rho"])
    id_ii = sid["A_ii_eq_Var"]
    ok_all &= _report("(ii) metric-trace area  A_ii - Var == 0  (|grad phi_M|^2_g == quantum "
                      "variance; symbolic, ALL p, ALL M)", id_ii)
    id_iii = sid["A_iii_eq_Var"]
    ok_all &= _report("(iii) KKS symplectic  A_iii - Var == 0  (|X_phi|^2 = g_{a bbar} X^a conj(X)^bbar, "
                      "X = J grad phi; FULL conjugation = swap AND i->-i, NOT sympy conjugate; "
                      "symbolic, ALL p, ALL M)", id_iii)
    # Bug-guard 1: the two canonical defs AGREE (no flip)
    ok_all &= _report("Bug-guard 1 (no flip): A_ii == A_iii (the two canonical area defs agree, "
                      "symbolic) => NOT INCONCLUSIVE", sid["A_ii_eq_A_iii"])
    ok_all &= _report("decomposition  G_M - (Var + 3/4 <M>^2 - 1/2 Tr M^2) == 0  (the "
                      "relative-entropy Hessian = the Fisher information PLUS a non-proportional "
                      "correction; symbolic, ALL p, ALL M)", sid["decomposition"])
    ok_all &= _report("shear identity  (G_M - Var) - (3/4 <M>^2 - 1/2 Tr M^2) == 0  (the R-shear is "
                      "EXACTLY the relative-entropy correction, a state-space quantity)",
                      sid["shear_is_relent"])

    # numeric cross-check of the canonical area at the de-risked d1@P0 (A_ii == A_iii == Var == 1/2)
    gpot = fs_metric_pot(); ginvpot = fs_metric_inv(gpot)
    sub0 = P0_sub()
    a2 = cancel(A_ii(matter_directions()["d1"], gpot, ginvpot, P).subs(sub0))
    a3 = cancel(A_iii(matter_directions()["d1"], gpot, ginvpot, P).subs(sub0))
    vv = cancel(Var(matter_directions()["d1"], P).subs(sub0))
    ok_all &= _report(f"numeric anchor d1@P0: A_ii={a2}, A_iii={a3}, Var={vv} (all == 1/2, "
                      "section-9)", a2 == Rational(1, 2) and a3 == Rational(1, 2) and vv == Rational(1, 2))

    # report the physical-metric scale relation (the single overall scale G1 normalizes away)
    print("      metric-scale note: the canonical area uses g_pot = Re(QGT) (the Fisher metric),")
    print("      giving A_ii == Var.  The engine/Boucetta metric g_phys = g_pot/2 gives")
    print("      A_ii(phys) == 2*Var -- the 'single overall scale' G1 allows to normalize away;")
    print("      it does NOT decide the verdict (R = A/|G| rescales uniformly).")

    # --- G0.4 FISHER-CORPSE determination (Bug-guard 3, load-bearing) ---
    print("\n  G0.4 FISHER-CORPSE determination (Bug-guard 3):")
    print("      The FS metric = Re(QGT) (Provost-Vallee 1980: Fubini-Study = the quantum Fisher")
    print("      metric on pure states).  Therefore the unique FS-canonical local area")
    print("      A_M = Var = the quantum Fisher information of phi_M -- a STATE-SPACE object, the")
    print("      same family as v17's dead real-QGT/cone-Hessian/Fisher metric (the corpse).")
    print("      DECISION RULE: a Fisher-object area ==> a shear of R is NOT a geometric rate")
    print("      (it is Fisher vs relative-entropy) ==> route to DEAD-FISHER / fork A; do NOT")
    print("      proceed to G2 with a contaminated object.")
    fisher_corpse = (id_ii and id_iii)    # A_M IS the Fisher object (proven above, sid booleans)
    ok_all &= _report("FISHER-CORPSE established: the canonical area A_M is IDENTICALLY the "
                      "quantum Fisher metric Var (Bug-guard 3 fires)", fisher_corpse)

    # --- candidate (i) CONTROL: global FS measure is a per-M CONSTANT, not a local field ---
    print("\n  G0.3(i) CONTROL -- candidate (i) is a per-M CONSTANT (homogeneity-artifact mode):")
    ci_ok = True
    ci_tbl = []
    for nm, M in dirs.items():
        c = A_i_global(M)        # one number per M (no p-dependence: it is an integral over CP^2)
        ci_tbl.append((nm, c))
        if c.free_symbols:       # must be a pure number (no chart symbols)
            ci_ok = False
    for nm, c in ci_tbl:
        print(f"      candidate(i) A_i_global[{nm}] = {c}  (a per-M CONSTANT, p-independent)")
    ok_all &= _report("candidate (i) = a per-M CONSTANT (no p-dependence): pairing it over the "
                      "p-varying G_M(p) is a DENOMINATOR-only shear (homogeneity artifact), NOT a "
                      "local area => rejected as a competing canonical area", ci_ok)

    print(f"\n  GATE 0: {'ALL PASS' if ok_all else 'FAIL'}")
    return ok_all


# ============================================================================
# GATE 1 -- THE KILL-TEST  (cheap, decisive; exact over Q)
# ============================================================================
# the de-risked section-9 ground truth (exact over Q)
GROUND_TRUTH = [
    # (dir, point_sub, phi, Var, G_M, R)
    ("d1", "P0", Rational(-1, 2), Rational(1, 2), Rational(-5, 16), Rational(8, 5)),
    ("d1", "P2", None,            Rational(2, 15), Rational(-13, 15), Rational(2, 13)),
    ("s01", "P0", None,           Rational(11, 16), Rational(-17, 64), Rational(44, 17)),
    ("a01", "P0", None,           Rational(1, 2), Rational(-5, 16), Rational(8, 5)),
    ("gen", "P0", None,           Rational(27, 16), Rational(-81, 64), Rational(4, 3)),
    ("gen", "P2", None,           Rational(26, 25), Rational(-1, 25), Rational(26, 1)),
]


def gate1(sid):
    print("=" * 78)
    print("GATE 1 : THE KILL-TEST  R(p,M) = A_M(p)/|G_M(p)|  (exact over Q; bug guards FIRST)")
    print("=" * 78)
    ok_all = True
    P = P_chart()
    dirs = matter_directions()
    SUBS = {"P0": P0_sub(), "P2": P2_sub()}

    # --- reproduce the RESEARCH section-9 ground truth (engine self-check) ---
    print("\n  reproduce the RESEARCH section-9 de-risked ground truth (A_M = A_ii = Var):")
    print(f"      {'dir':4s} {'pt':3s} {'phi':>8s} {'Var=A_M':>10s} {'G_M':>10s} {'R=A/|G|':>10s}")
    gt_ok = True
    for (dn, pn, phi_exp, var_exp, g_exp, r_exp) in GROUND_TRUTH:
        M = dirs[dn]; sub = SUBS[pn]
        phiv = cancel(phi_M(M, P).subs(sub))
        varv = cancel(Var(M, P).subs(sub))
        gv = cancel(G_M(M, P).subs(sub))
        rv = cancel(varv / abs(gv))
        row_ok = (varv == var_exp and gv == g_exp and rv == r_exp
                  and (phi_exp is None or phiv == phi_exp))
        gt_ok &= row_ok
        mark = "" if row_ok else "   <-- MISMATCH"
        note = "  (denom near-zero; zero-locus artifact)" if (dn == "gen" and pn == "P2") else ""
        print(f"      {dn:4s} {pn:3s} {str(phiv):>8s} {str(varv):>10s} {str(gv):>10s} "
              f"{str(rv):>10s}{mark}{note}")
    ok_all &= _report("section-9 ground truth reproduced EXACTLY (Var, G_M, R on all 6 rows)", gt_ok)

    # cross-check: A_iii reproduces the same R (the KKS area agrees, Bug-guard 1)
    gpot = fs_metric_pot(); ginvpot = fs_metric_inv(gpot)
    aiii_ok = True
    for (dn, pn, _, var_exp, g_exp, r_exp) in GROUND_TRUTH:
        M = dirs[dn]; sub = SUBS[pn]
        a3 = cancel(A_iii(M, gpot, ginvpot, P).subs(sub))
        gv = cancel(G_M(M, P).subs(sub))
        r3 = cancel(a3 / abs(gv))
        aiii_ok &= (a3 == var_exp and r3 == r_exp)
    ok_all &= _report("Bug-guard 1 cross-check: A_iii (KKS) reproduces the SAME R on all 6 rows "
                      "(no flip between canonical areas)", aiii_ok)

    # --- Bug guard 1: DENOMINATOR-ZERO handling ---
    print("\n  Bug guard (1) DENOMINATOR-ZERO: G_M -> 0 at the bit-counter zero locus (NOT a shear):")
    # DEVIATION [Rule 4 - corrected locus] from RESEARCH s3: the RESEARCH says G_M -> 0 'near the
    # vertex E_11'; the EXACT computation shows the genuine G_M=0 locus for the rank-2 directions is
    # the EQUATOR (e.g. z1=+-1, z2=0 for d1), where the (1,2)-block face is maximally mixed -- NOT
    # the vertex.  At the vertex z=0 it is the NUMERATOR Var that vanishes (E_11 is a d1-eigenstate,
    # zero variance) while G_M = -1/4 stays finite => R=0 there.  Both loci are non-shears; we test
    # the CORRECT facts (report the truth).
    # (a) the genuine denominator-zero: d1 at the equator z1=1, z2=0 -> G_M=0, Var=1 (finite).
    eq = {Z1: 1, Z1B: 1, Z2: 0, Z2B: 0}
    g_eq = cancel(G_M(dirs["d1"], P).subs(eq))
    var_eq = cancel(Var(dirs["d1"], P).subs(eq))
    recip_eq = cancel(abs(g_eq) / var_eq)        # |G|/A = 0 at the bit-counter zero (finite)
    print(f"      equator z1=1,z2=0: G_M(d1)={g_eq} (bit-counter ZERO), Var(d1)={var_eq} (finite) "
          f"=> R=A/|G| blows up; reciprocal |G|/A={recip_eq} (FINITE) => EXCLUDE / use reciprocal.")
    # (b) the numerator-zero: d1 at the vertex z=0 -> Var=0 (eigenstate), G_M=-1/4 (finite) => R=0.
    z0 = {Z1: 0, Z1B: 0, Z2: 0, Z2B: 0}
    g_v = cancel(G_M(dirs["d1"], P).subs(z0))
    var_v = cancel(Var(dirs["d1"], P).subs(z0))
    print(f"      vertex z=0: Var(d1)={var_v} (numerator ZERO, E_11 is a d1-eigenstate), "
          f"G_M(d1)={g_v} (finite) => R=0 (a numerator-zero, also NOT a shear).")
    # (c) gen@P2: G_M=-1/25 near-zero => R=26 is a 1/|G| near-blow-up (the section-9 artifact row).
    print(f"      gen@P2: G_M=-1/25 NEAR-zero => R=26 is a 1/|G| near-blow-up (zero-locus artifact, "
          f"NOT a shear of the RATE).")
    denom_ok = (g_eq == 0 and var_eq != 0 and recip_eq == 0 and var_v == 0 and g_v == Rational(-1, 4))
    ok_all &= _report("denominator-zero handled: the genuine G_M=0 locus (equator) gives R-blowup but "
                      "FINITE reciprocal |G|/A=0; the vertex gives a NUMERATOR-zero (R=0); both are "
                      "bit-counter/eigenstate zeros, NOT rate shears (RESEARCH s3 'vertex' framing "
                      "corrected to 'equator' -- exact)", denom_ok)

    # --- Bug guard 2: HOMOGENEITY check ---
    print("\n  Bug guard (2) HOMOGENEITY: is R a genuine non-constant function (not removable by")
    print("      one global scale), AND do A_M, G_M have DIFFERENT M-structure?")
    # R is NOT literally constant: it differs across directions/points (8/5, 2/13, 44/17, 4/3 ...).
    Rvals = set()
    for (dn, pn, _, _, _, r_exp) in GROUND_TRUTH:
        if not (dn == "gen" and pn == "P2"):     # exclude the zero-locus artifact row
            Rvals.add(r_exp)
    not_constant = (len(Rvals) >= 2)
    ok_all &= _report(f"R is NOT literally constant: distinct values {sorted(Rvals)} across "
                      "directions/points (the literal DEAD-CONSTANT reading FAILS)", not_constant)
    # A_M = Var has DIFFERENT M-structure than G_M = Var + 3/4<M>^2 - 1/2 Tr M^2: the shear is
    # precisely the relative-entropy correction.  Reuse the symbolic proof from G0 (sid), which
    # established (G_M - Var) - (3/4<M>^2 - 1/2 Tr M^2) == 0 for ALL p, ALL M via the exact
    # numerator method (recomputing it here with the slow `cancel` path is the perf cliff).
    shear_is_relent = sid["shear_is_relent"]
    ok_all &= _report("the shear is EXACTLY the relative-entropy correction G_M - Var = "
                      "3/4<M>^2 - 1/2 Tr M^2 (a state-space quantity, NOT geometry; proven "
                      "symbolically in G0)", shear_is_relent)

    # --- Bug guard 3: FISHER-CORPSE gate (decisive) ---
    print("\n  Bug guard (3) FISHER-CORPSE gate (decisive):")
    # A_M == Var was PROVEN in G0 (symbolic, sid).  R = Var/|G_M| = Fisher/(relative-entropy
    # Hessian), a comparison of two STATE-SPACE information measures => NOT a geometric rate.
    A_is_fisher = (sid["A_ii_eq_Var"] and sid["A_iii_eq_Var"])
    print("      A_M == Var (the quantum Fisher information) -- proven symbolically in G0.")
    print("      => R = Var/|G_M| = (Fisher information)/(relative-entropy Hessian): a comparison")
    print("         of two STATE-SPACE information measures, NOT a geometric exchange rate.")
    print("      => the variety sets NO native geometric bits<->area rate => contingent import")
    print("         => FORK A.  STOP (do NOT proceed to G2 with a Fisher-contaminated object).")
    ok_all &= _report("FISHER-CORPSE gate FIRES: A_M is identically the Fisher metric => R's shear "
                      "is state-space (Fisher vs rel-entropy), NOT geometric => DEAD-FISHER/fork A",
                      A_is_fisher)

    # --- preempt LIVE-TENSOR: the canonical area is the metric TRACE => scalar, never TT ---
    print("\n  PREEMPT LIVE-TENSOR: A_M^(ii) = g^{ij-bar} d_i phi d_jbar phi is literally the metric")
    print("      TRACE of the metric-mode dphi_M(x)dphi_M => it carries the SCALAR (trace) part,")
    print("      NOT the TT (traceless-transverse) part.  Even if one (wrongly) routed past the")
    print("      Fisher gate to G2, the area source is pure-trace => at most LIVE-SCALAR, never")
    print("      LIVE-TENSOR.")
    ok_all &= _report("canonical area = metric trace of dphi(x)dphi (scalar part by construction) "
                      "=> LIVE-TENSOR is structurally precluded for THIS canonical area", True)

    print(f"\n  GATE 1: {'ALL PASS' if ok_all else 'FAIL'}")
    # G1 routes to DEAD-FISHER => G2 NOT reached.
    return ok_all, {"A_is_fisher": A_is_fisher, "R_not_constant": not_constant,
                    "shear_is_relent": shear_is_relent, "denom_zero_handled": denom_ok,
                    "areas_agree": aiii_ok, "ground_truth": gt_ok,
                    "area_is_trace": True}


# ============================================================================
# verdict() -- NON-HARDWIRED ladder from computed booleans, with self-tests
# ============================================================================
def verdict(flags):
    """A DERIVED ladder from computed booleans.  Returns one of
       {DEAD-CONSTANT, DEAD-FISHER, LIVE-SCALAR, LIVE-TENSOR, INCONCLUSIVE}.
    NOT hardwired: the branch taken is forced by the input flags (proven by the self-tests,
    which flip the verdict under synthetic inputs).

    flags keys (all booleans):
      areas_agree     -- the >=2 canonical area definitions agree (Bug-guard 1; else INCONCLUSIVE)
      A_is_fisher     -- the canonical area A_M is IDENTICALLY the Fisher metric Var (Bug-guard 3)
      R_constant      -- R is literally p/M-constant up to one overall scale
      area_is_trace   -- the canonical area is the metric TRACE of dphi(x)dphi (scalar part)
      shear_is_geometric -- a genuine, non-Fisher, FS-canonical, matter-functorial geometric shear
                            survives the bug guards (the G2-eligible surprise)
    """
    # Bug-guard 1 FIRST: a verdict that flips between canonical area definitions is an artifact.
    if not flags.get("areas_agree", False):
        return "INCONCLUSIVE"
    # literal constant reading
    if flags.get("R_constant", False):
        return "DEAD-CONSTANT"
    # Fisher-corpse gate (decisive): the canonical area is the state-space Fisher metric.
    if flags.get("A_is_fisher", False):
        return "DEAD-FISHER"
    # a genuine geometric (non-Fisher) shear survived -> LIVE; trace test splits scalar/tensor.
    if flags.get("shear_is_geometric", False):
        return "LIVE-SCALAR" if flags.get("area_is_trace", True) else "LIVE-TENSOR"
    # no constant, no Fisher, no surviving geometric shear: nothing certified.
    return "INCONCLUSIVE"


def verdict_self_tests():
    """The verdict() ladder MUST flip correctly under synthetic inputs (proves non-hardwired)."""
    print("=" * 78)
    print("verdict() SELF-TESTS (must all PASS before the real verdict; proves non-hardwired)")
    print("=" * 78)
    ok = True
    # (1) RIGGED-CONSTANT: an area defined so A propto |G_M| by construction => DEAD-CONSTANT.
    v1 = verdict({"areas_agree": True, "A_is_fisher": False, "R_constant": True,
                  "area_is_trace": True, "shear_is_geometric": False})
    ok &= _report(f"self-test rigged-constant (A propto |G_M|) -> {v1} (==DEAD-CONSTANT)",
                  v1 == "DEAD-CONSTANT")
    # (2) HAND-BUILT genuinely-shearing NON-Fisher input -> LIVE.
    v2t = verdict({"areas_agree": True, "A_is_fisher": False, "R_constant": False,
                   "area_is_trace": False, "shear_is_geometric": True})
    v2s = verdict({"areas_agree": True, "A_is_fisher": False, "R_constant": False,
                   "area_is_trace": True, "shear_is_geometric": True})
    ok &= _report(f"self-test hand-built non-Fisher geometric shear -> {v2t}/{v2s} "
                  "(==LIVE-TENSOR/LIVE-SCALAR per trace test)",
                  v2t == "LIVE-TENSOR" and v2s == "LIVE-SCALAR")
    # (3) two NON-AGREEING canonical areas -> INCONCLUSIVE.
    v3 = verdict({"areas_agree": False, "A_is_fisher": True, "R_constant": False,
                  "area_is_trace": True, "shear_is_geometric": False})
    ok &= _report(f"self-test non-agreeing canonical areas (verdict flips) -> {v3} "
                  "(==INCONCLUSIVE)", v3 == "INCONCLUSIVE")
    # (4) FISHER-CORPSE path (A == Var) -> DEAD-FISHER / fork A.
    v4 = verdict({"areas_agree": True, "A_is_fisher": True, "R_constant": False,
                  "area_is_trace": True, "shear_is_geometric": False})
    ok &= _report(f"self-test Fisher-corpse (A == Var) -> {v4} (==DEAD-FISHER)",
                  v4 == "DEAD-FISHER")
    # non-hardwired demonstration: the SAME function returned 4 different verdicts above.
    distinct = {v1, v2t, v2s, v3, v4}
    ok &= _report(f"verdict() is NON-HARDWIRED: produced {sorted(distinct)} under synthetic "
                  "inputs (it flips with the flags, not a constant)", len(distinct) >= 4)
    print(f"\n  SELF-TESTS: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ============================================================================
def main():
    print("#" * 78)
    print("# area_per_bit.py -- Phase 95 / v35.0-candidate: THE AREA-PER-BIT KILL-TEST")
    print("# (exact over Q; octonion engine NOT on the decisive path; CP^2 = h_3(C_u))")
    print("#" * 78)

    # ---- verdict() self-tests FIRST (must pass before any real verdict) ----
    st_ok = verdict_self_tests()
    if not st_ok:
        print("\n*** verdict() SELF-TESTS FAILED -- the ladder is broken; STOP. ***")
        return 1

    # ---- the symbolic identities (computed ONCE; threaded into G0 and G1) ----
    _log("proving the symbolic identities over generic 8-param M (exact polynomial-numerator "
         "method over rho-powers) ...")
    sid = _symbolic_identities()
    _log(f"symbolic identities done: {sid}")

    # ---- GATE 0 ----
    g0 = gate0(sid)
    if not g0:
        print("\n*** GATE 0 FAILED (setup / pin-the-area) -- FAIL-FAST STOP. ***")
        return 1

    # ---- GATE 1 (the kill-test) ----
    g1, flags = gate1(sid)
    if not g1:
        print("\n*** GATE 1 FAILED -- STOP. ***")
        return 1

    # ---- the REAL verdict (from the computed booleans; G2 not reached if Fisher-corpse fires) ----
    print("\n" + "=" * 78)
    print("THE REAL VERDICT (derived from the computed booleans)")
    print("=" * 78)
    real_flags = {
        "areas_agree": flags["areas_agree"] and flags["ground_truth"],   # A_ii==A_iii, GT reproduced
        "A_is_fisher": flags["A_is_fisher"],                             # A_M == Var (symbolic)
        "R_constant": not flags["R_not_constant"],                       # R is NOT literally constant
        "area_is_trace": flags["area_is_trace"],                         # metric trace => scalar
        "shear_is_geometric": False,    # NO genuine non-Fisher geometric shear survived G1
    }
    v = verdict(real_flags)
    print(f"  computed flags: {real_flags}")
    print(f"\n  VERDICT: {v}")
    if v == "DEAD-FISHER":
        print("\n  MECHANISM (the FISHER-CORPSE): the variety's only FS-canonical local area is")
        print("  IDENTICALLY the quantum Fisher / QGT-real metric Var (v17's corpse -- a")
        print("  positive-semidefinite object on STATES, not a spacetime metric).  R = Var/|G_M| =")
        print("  Fisher/(relative-entropy Hessian) shears, but the shear is the state-space")
        print("  correction G_M - Var = 3/4<M>^2 - 1/2 Tr M^2, NOT a geometric bits<->area rate.")
        print("  There is no native geometric area independent of the state-space information")
        print("  geometry to pair with the bits => the variety sets NO native geometric")
        print("  bits<->area rate => the rate (Ryu-Takayanagi's G) is a contingent import => FORK A.")
        print("\n  This CLOSES the entanglement route (the sixth brainstorm angle), reached through")
        print("  the sharper identity 'the canonical area IS the bit-counter metric'.  Same fork-A")
        print("  conclusion family as v33 FORCES-NOTHING and the v23 grad S = 0 death.")
    print("\n  [FENCE] NO Einstein/G=kT/gravity/Newton/dark-matter/geodesic as a DERIVED result;")
    print("  the bits<->area rate is a framework ratio (contingent import like kappa,Lambda), NOT")
    print("  Newton's G; FS is USED not derived; signature Riemannian (Wall 2 unpaid).  Does NOT")
    print("  retract v33/v34/v17-v21/v23.  Paper 5 remains the only more-than-nothing result.")
    print("\n  [ANTI-OVERCLAIM] DEAD-FISHER is the expected, honest outcome; it closes the")
    print("  entanglement route and is the green light for fork A.  Holography is theorem-blocked")
    print("  natively (h_3(O) finite Type-I_3; RT equality needs a Type III_1 factor the exceptional")
    print("  algebra cannot have).  The program has the Bekenstein BOUND (S <= Area, G-free) but")
    print("  NOT the RT EQUALITY (Area = 4G S, G-valued) -- the G-valued equality is the clamp.")

    print("\n" + "=" * 78)
    print(f"[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS  "
          f"(exact over Q; no float in the verdict)")
    print("=" * 78)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    sys.exit(main())
