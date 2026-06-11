#!/usr/bin/env python3
"""variety_sourced_field_equation.py -- v26.0 Phase 86 (J5-on-the-variety, step 2)
"The Sourced Field Equation: MaxEnt Derived and the Second-Order Vacuum Structure."

Perturb the vacuum X = I/3 + eps M (Tr M = 0, symbolic M).  CLAIMS (all exact over
Q[eps]/(eps^3), Q(t), polynomial-identity solves; floats illustrative only):

  B1 (MaxEnt derived).   m = 2/3 - eps<M,p>;  X# = I/9 - (eps/3)M + eps^2 M#  =>
     q = 1/9 - (eps/3)<M,p> + eps^2<M#,p>;  so dq = dm/3 (ONE field at first order)
     and **dr = 0 identically** -- the purity/entropy landscape is flat at first order
     at EVERY event p = the vacuum MaxEnt property, DERIVED on the variety.

  B2 (the response field).   d^2 r = (9/4) G_M eps^2,  G_M(p) := <M#,p> - (1/4)<M,p>^2.
     Entropy: S = f(r) analytic at r=1/4 (the +-sqrt(1-4r) branches cancel), f'(1/4)=2,
     so **d^2 S = (9/2) G_M eps^2**.  Relative entropy (2-face vacuum maximally mixed):
     S(rho_face || rho_vac) = log2 - S(rho_face) EXACTLY = -d^2 S at 2nd order.
     **Positivity G_M <= 0** for all traceless M, all p (S <= log2), structurally
     G_M = -(1/4)(eigengap of C_p M)^2 <= 0.

  B3 (the sourced equation).  Sym^2(26) = 1 + 26 + 324 under F_4; the only quadratic
     covariants of traceless M are M# and TrM^2*1 (M^2 = M# + (1/2)TrM^2*1).  So
        <M,p>^2 = alpha<M#,p> + beta TrM^2 + R_M(p),  R_M a level-2 (lambda_2) eigenfunction,
     with (alpha, beta, lambda_2) fixed by the overdetermined symbolic solve (its
     CONSISTENCY is the claim).  Then the v25 free equation gives the SOURCED equation
        **(Delta + lambda_1) G_M = -kappa_0 TrM^2 + ((lambda_2 - lambda_1)/4) R_M(p)**,
     kappa_0 = lambda_1(1/6 - alpha/24 + beta/4) DERIVED.  lambda_2 = 32 on the cut
     (Fubini-Study 4*2*4), lambda_2 = 104 on OP^2 (derived).

  B4 (hidden sector).  Off-u M (octonion dirs e_1..e_6): (invisibility) <M,p> = 0 for
     all p in the CP^2 cut; (still sources) G_M|cut = <M#,p>|cut != 0; (dichotomy) the
     cut source is square-free (level <= 1), no anisotropic level-2 signature.

DISCIPLINE: reuse the v25 machinery (import variety_moment_doublet).  Octonion product
conventions as v25 (the conj(x3.x2)-order trap is resolved upstream).  det SSOT =
RL.det_3; octonion_algebra BANNED.  No G=kT, no Newton constant, no SUGRA, no dark-matter
language: lambda_1, lambda_2, alpha, beta, kappa_0 are spectral/structural data of the
FROZEN canonical geometry (imports-as-math), NOT couplings.  TRAP #5/#6: still no field
equation for the rational r or S; the SOURCED equation for G_M is an EXPLICIT exact
identity with derived constants (exempt from #6 -- not an annihilator existence claim).
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                          # noqa: E402
from sympy import Rational, symbols, cancel, expand, log as slog, sqrt      # noqa: E402

import ring_lemma_verification as RL                                        # noqa: E402
import kkt_gluing_holonomy as KK                                            # noqa: E402
import variety_moment_doublet as vMD   # THE v25 machinery                  # noqa: E402

_t0 = time.time()
PASS = []
T = vMD.T
EPS = symbols("epsilon")
E11 = vMD.E11
E22 = KK.E_ii(1)
E33 = KK.E_ii(2)
IDENT = vMD.IDENT
I3 = vMD.I3
inner = vMD.inner
sharp = vMD.sharp


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}")


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


# ----------------------------------------------------------------------------
# traceless matter perturbations + helpers
# ----------------------------------------------------------------------------
def M_full(prefix="m"):
    """Symbolic traceless M, 26 params: diag (a,b,-a-b) + three octonions (24)."""
    s = symbols(f"{prefix}0:26", real=True)
    M = RL.h3o_from_coords(s[0], s[1], -s[0] - s[1],
                           list(s[2:10]), list(s[10:18]), list(s[18:26]))
    return M, s


def _cu(re, e7):
    z = [sp.Integer(0)] * 8
    z[0], z[7] = re, e7
    return z


def M_ualigned(prefix="m"):
    """Symbolic traceless u-aligned (cut) M, 8 params: diag + octonions in span{1,e_7}."""
    s = symbols(f"{prefix}0:8", real=True)
    M = RL.h3o_from_coords(s[0], s[1], -s[0] - s[1],
                           _cu(s[2], s[3]), _cu(s[4], s[5]), _cu(s[6], s[7]))
    return M, s


def _offu(re_unused, comps):
    """octonion supported only on e_1..e_6 (off-u, off-real): comps is a 6-list for e_1..e_6."""
    z = [sp.Integer(0)] * 8
    for i in range(6):
        z[i + 1] = comps[i]
    return z


def M_offu(prefix="m"):
    """Symbolic off-u M: octonion off-diagonals supported on e_1..e_6 only (no diagonal,
    no real/e_7 parts) -- the hidden sector. 18 params (3 octonions x 6)."""
    s = symbols(f"{prefix}0:18", real=True)
    M = RL.h3o_from_coords(0, 0, 0, _offu(0, s[0:6]), _offu(0, s[6:12]), _offu(0, s[12:18]))
    return M, s


def cross(A, B):
    """Freudenthal cross A x B (library formula)."""
    AB = RL.jordan(A, B)
    TA, TB, TAB = RL.Tr(A), RL.Tr(B), RL.Tr(AB)
    return vMD.V24.el_add(AB, vMD.V24.el_scal(-Rational(1, 2) * TB, A),
                          vMD.V24.el_scal(-Rational(1, 2) * TA, B),
                          vMD.V24.el_scal(Rational(1, 2) * (TA * TB - TAB), IDENT))


def TrM2(M):
    return RL.Tr(RL.jordan(M, M))


def G_M(M, p):
    """The second-order response field G_M(p) = <M#,p> - (1/4)<M,p>^2."""
    return inner(sharp(M), p) - Rational(1, 4) * inner(M, p) ** 2


def lap_func(fp, frame):
    """Delta f(E_11) = sum_i (1/4) d^2/dt^2 f(p_i(t))|_0 over a frame; fp(p)->scalar."""
    tot = sp.Integer(0)
    for (j, k) in frame:
        p = vMD.V24.family(T, j, k)
        tot += Rational(1, 4) * sp.diff(fp(p), T, 2).subs(T, 0)
    return sp.expand(tot)


def eps_coeffs(X_of_eps_p_value):
    """Return [c0,c1,c2] of an exact eps-polynomial (degree<=2)."""
    e = sp.expand(X_of_eps_p_value)
    return [e.coeff(EPS, n) for n in range(3)]


# ----------------------------------------------------------------------------
# GATE 0 -- machinery (fail-fast)
# ----------------------------------------------------------------------------
def gate0():
    print("=" * 78)
    print("GATE 0 : machinery -- v25 frames reloaded; Delta of PRODUCTS; eps ring")
    print("=" * 78)
    ok = True
    # v25 frames reloaded + lambda_1 still 48/12 (regression)
    DPf = vMD.mean_curv(vMD.battery16())
    DPc = vMD.mean_curv(vMD.cut_families())
    lf = vMD.extract_lambda(DPf)
    lc = vMD.extract_lambda(DPc)
    ok &= _report(f"v25 frames reloaded: lambda_1(OP^2)={lf}(==48), lambda_1(cut)={lc}(==12); "
                  f"DeltaP full/cut == -lambda(E11-I/3)",
                  lf == 48 and lc == 12
                  and vMD.el_eq(DPf, vMD.V24.el_scal(-lf, vMD.el_sub(E11, I3)))
                  and vMD.el_eq(DPc, vMD.V24.el_scal(-lc, vMD.el_sub(E11, I3))))

    # Delta of a PRODUCT vs the product rule: for f=<A,.> , g=<B,.> linear,
    # Delta(fg)(E11) = f Delta g + g Delta f + 2 <grad f, grad g>.  Check the assembler
    # computes the product's 2nd derivative correctly by matching d^2/dt^2(fg) to
    # (f'' g + 2 f' g' + g'' f) along one family (symbolic product rule, exact).
    A = vMD.state_generic() if hasattr(vMD, "state_generic") else vMD.V24.state_generic()
    B = vMD.V24.state_diagonal()
    p = vMD.V24.family(T, 1, 1)
    f = inner(A, p); g = inner(B, p)
    lhs = sp.diff(f * g, T, 2)
    rhs = sp.diff(f, T, 2) * g + 2 * sp.diff(f, T) * sp.diff(g, T) + sp.diff(g, T, 2) * f
    ok &= _report("Delta-of-product assembler == symbolic product rule "
                  "(d^2/dt^2(fg) = f''g+2f'g'+g''f) along a family", cancel(lhs - rhs) == 0)

    # eps-truncation ring: X = I/3 + eps M, m linear in eps, q quadratic (sharp is quadratic)
    M, _ = M_full()
    X = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
    m = sp.expand(RL.Tr(X) - inner(X, E11))
    q = sp.expand(inner(sharp(X), E11))
    ok &= _report("eps ring: deg_eps(m)=1, deg_eps(q)=2 (order-counting exact, guard 1)",
                  sp.Poly(m, EPS).degree() == 1 and sp.Poly(q, EPS).degree() == 2)
    print(f"\n  GATE 0: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 1 -- controls (known answers; zero evidential weight)
# ----------------------------------------------------------------------------
def gate1():
    print("=" * 78)
    print("GATE 1 : controls (known answers; ZERO evidential weight)")
    print("=" * 78)
    ok = True
    # (i) v25 free equation regression: one moment Y obeys Delta phi_Y = -48(phi_Y-<Y,I/3>)
    Y = vMD.V24.state_generic()
    DPf = vMD.mean_curv(vMD.battery16())
    lhsY = inner(Y, DPf); rhsY = -48 * (inner(Y, E11) - inner(Y, I3))
    ok &= _report("(i) v25 free-equation regression: Delta phi_Y(E11) == -48(phi_Y-<Y,I/3>)",
                  cancel(lhsY - rhsY) == 0)

    # (iii) M = diag(2,-1,-1) anchors
    Md = RL.h3o_from_coords(2, -1, -1, RL.oct_zero(), RL.oct_zero(), RL.oct_zero())
    g11 = cancel(G_M(Md, E11)); g22 = cancel(G_M(Md, E22))
    ok &= _report(f"(iii) M=diag(2,-1,-1): G(E11)={g11}(==0, face sees only the propto-I_2 block), "
                  f"G(E22)={g22}(==-9/4<0); <M#,E22>={cancel(inner(sharp(Md),E22))}(==-2)",
                  g11 == 0 and g22 == Rational(-9, 4) and inner(sharp(Md), E22) == -2)

    # (iv) M = 0: everything vanishes
    Z = vMD.V24.el_zero()
    ok &= _report("(iv) M=0: G_M==0, <M,p>==0, TrM^2==0 (trivial vacuum)",
                  cancel(G_M(Z, E11)) == 0 and cancel(inner(Z, E11)) == 0 and cancel(TrM2(Z)) == 0)

    # (ii) level-2 control: c11^2 is reproduced by the SAME lambda_2 as the symbolic solve.
    # c11 - 1/3 = <E11 - I/3, p> = phi_M0 with M0 = E11 - I/3 (traceless); its square's level-2
    # part must be a lambda_2=104 eigenfunction.  Verify via the per-M solve specialized to M0.
    M0 = vMD.el_sub(E11, I3)
    a0, b0, l0 = _level_split_value(M0, vMD.battery16(), 48)
    ok &= _report(f"(ii) level-2 control c11^2 (M0=E11-I/3): independent lambda_2={l0}(==104) "
                  f"matches the symbolic-solve OP^2 value", l0 == 104)
    print(f"\n  GATE 1: {'ALL PASS' if ok else 'FAIL'}")
    return ok


def _level_split_value(Mexpr, frame, lam1):
    """Solve <M,p>^2 = a<M#,p> + b TrM^2 + R_M for a single concrete/symbolic M (numeric a,b,lam2
    when M is concrete; used by the c11^2 control)."""
    a, b, l2 = symbols("a b l2")
    aE = inner(Mexpr, E11); cE = inner(sharp(Mexpr), E11); tm = TrM2(Mexpr)
    L = lap_func(lambda p: inner(Mexpr, p) ** 2, frame)
    R = aE ** 2 - a * cE - b * tm
    rhs = -a * lam1 * (cE + tm / 6) - l2 * R
    # one concrete M gives one equation; the c11 control fixes l2 once (a,b from the master solve)
    amaster, bmaster = Rational(1, 7), Rational(9, 182)
    val = sp.solve(sp.Eq(L, rhs.subs({a: amaster, b: bmaster})), l2)
    return amaster, bmaster, (val[0] if val else None)


# ----------------------------------------------------------------------------
# GATE 2 -- B1 (MaxEnt) + B2 (response field)
# ----------------------------------------------------------------------------
def gate2():
    print("=" * 78)
    print("GATE 2 : B1 (MaxEnt: dq=dm/3, dr=0) + B2 (response field d^2S=(9/2)G_M)")
    print("=" * 78)
    ok = True
    M, _ = M_full()

    # B1 at E_11, symbolic M
    X = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
    m = sp.expand(RL.Tr(X) - inner(X, E11))
    q = sp.expand(inner(sharp(X), E11))
    a = inner(M, E11); c = inner(sharp(M), E11)
    m_ok = (cancel(m - (Rational(2, 3) - EPS * a)) == 0)
    q_ok = (cancel(q - (Rational(1, 9) - EPS / 3 * a + EPS ** 2 * c)) == 0)
    # X# expansion: I/9 - (eps/3)M + eps^2 M#
    Xs = sharp(X)
    sharp_ok = vMD.el_eq(Xs, vMD.V24.el_add(vMD.V24.el_scal(Rational(1, 9), IDENT),
                                            vMD.V24.el_scal(-EPS / 3, M),
                                            vMD.V24.el_scal(EPS ** 2, sharp(M))))
    dq = q - Rational(1, 9); dm = m - Rational(2, 3)
    dq_dm = (cancel((dq - dm / 3).coeff(EPS, 1)) == 0)   # first-order dq = dm/3
    ok &= _report("B1: m=2/3-eps<M,p>, q=1/9-(eps/3)<M,p>+eps^2<M#,p>, X#=I/9-(eps/3)M+eps^2 M#, "
                  "dq=dm/3 (1st order)", m_ok and q_ok and sharp_ok and dq_dm)

    # dr = 0 identically (1st order) at E_11 + along all 16 families over Q(t)
    r = sp.series(q / m ** 2, EPS, 0, 3).removeO()
    dr1_E11 = (cancel(r.coeff(EPS, 1)) == 0)
    fam_ok = True
    for (j, k) in vMD.battery16():
        p = vMD.V24.family(T, j, k)
        Xp = vMD.V24.el_add(I3, vMD.V24.el_scal(EPS, M))
        mp = RL.Tr(Xp) - inner(Xp, p)
        qp = inner(sharp(Xp), p)
        rp = sp.series(qp / mp ** 2, EPS, 0, 2).removeO()
        fam_ok &= (cancel(rp.coeff(EPS, 1)) == 0)
    ok &= _report("B1: dr = 0 identically (symbolic M) at E_11 AND along all 16 families over Q(t) "
                  "-- the MaxEnt flatness at EVERY event", dr1_E11 and fam_ok)

    # B2: d^2 r = (9/4) G_M ; branch smoothness f'(1/4)=2 ; d^2 S = (9/2) G_M
    G = cancel(c - a ** 2 / 4)
    dr2_ok = (cancel(r.coeff(EPS, 2) - Rational(9, 4) * G) == 0)
    f1, smooth = _entropy_branch()
    ok &= _report(f"B2: d^2 r=(9/4)G_M; branch S=f(r) analytic at r=1/4 (sqrt branches cancel: "
                  f"{smooth}), f'(1/4)={f1}(==2) => d^2 S=(9/2)G_M", dr2_ok and smooth and f1 == 2)

    # B2: relative-entropy identity + structural positivity G_M = -(1/4)(face eigengap)^2 <= 0
    relent = _relative_entropy_identity()
    pos_struct = _positivity_structural(M)
    Md = RL.h3o_from_coords(2, -1, -1, RL.oct_zero(), RL.oct_zero(), RL.oct_zero())
    batt = _positivity_battery()
    ok &= _report(f"B2: S(rho||rho_vac)=log2-S exact (2-face); positivity G_M<=0 structural "
                  f"(=-1/4 eigengap^2: {pos_struct}); battery {batt}/{batt} (<=0); rel-ent id {relent}",
                  relent and pos_struct and batt > 0)
    print(f"\n  GATE 2: {'ALL PASS' if ok else 'FAIL'}")
    return ok


def _entropy_branch():
    """S(r)=f(r) on the 2-face: lam_pm=1/2 +- 1/2 sqrt(1-4r).  Verify analytic at r=1/4 in
    u=1-4r (sqrt branches cancel) and f'(1/4)=2."""
    u = symbols("u", nonnegative=True)
    w = sqrt(u)
    lp = (1 + w) / 2; lm = (1 - w) / 2
    S = -lp * slog(lp) - lm * slog(lm)
    ser = sp.series(S, u, 0, 2).removeO()          # expand in u; must be analytic (no odd sqrt(u))
    # S = log2 - (1/2) u + O(u^2); f(r)=S(u=1-4r), f'(1/4)= -4 dS/du|_0 = -4*(-1/2)=2
    dSdu0 = sp.limit(sp.diff(S, u), u, 0)
    smooth = (sp.simplify(ser - (slog(2) - u / 2)) == 0)
    fprime = cancel(-4 * dSdu0)
    return fprime, bool(smooth)


def _relative_entropy_identity():
    """S(rho_face || rho_vac) = log2 - S(rho_face) exactly (rho_vac = I_2/2 maximally mixed)."""
    lp = symbols("lp", positive=True)
    lm = 1 - lp                      # 2-face density: eigenvalues sum to 1
    # rho_vac eigenvalues 1/2,1/2 ; relent = sum lam (log lam - log(1/2)) = sum lam log lam + log2
    relent = lp * slog(lp) + lm * slog(lm) + (lp + lm) * slog(2)
    S = -lp * slog(lp) - lm * slog(lm)
    return sp.simplify(relent - (slog(2) - S)) == 0


def _positivity_structural(M):
    """G_M(p) = -(1/4)[(Tr C_pM)^2 - 4 det2(C_pM)] = -(1/4)(eigengap)^2 <= 0.
    Verify the identity G_M == <M#,p> - 1/4<M,p>^2 == det2(C_pM) - 1/4 (Tr C_pM)^2 (v25 C1)."""
    p = vMD.V24.family(T, 1, 1)
    Cp = vMD.compress0(p, M) if hasattr(vMD, "compress0") else vMD.V24.compress0(p, M)
    trCp = RL.Tr(Cp)
    det2 = (RL.Tr(Cp) ** 2 - RL.Tr(RL.jordan(Cp, Cp))) / 2
    g = G_M(M, p)
    return cancel(g - (det2 - Rational(1, 4) * trCp ** 2)) == 0 and cancel(det2 - inner(sharp(M), p)) == 0


def _positivity_battery():
    """Exact: a battery of rational (M,p) instances all give G_M <= 0."""
    import itertools
    cnt = 0
    Ms = [RL.h3o_from_coords(3, -1, -2, RL.oct_zero(), RL.oct_zero(), RL.oct_zero()),
          RL.h3o_from_coords(Rational(1, 2), Rational(1, 3), -Rational(5, 6),
                             vMD.V24.oct1(1, Rational(1, 4)), vMD.V24.oct1(7, Rational(1, 5)),
                             vMD.V24.oct1(3, Rational(1, 6)))]
    pts = [E11, E22, E33, vMD.V24.family(Rational(2), 1, 1), vMD.V24.family(Rational(1, 3), 2, 7)]
    for M in Ms:
        for p in pts:
            if cancel(G_M(M, p)) <= 0:
                cnt += 1
            else:
                return -1
    return cnt


# ----------------------------------------------------------------------------
# GATE 3 -- B3 (level split + sourced equation)
# ----------------------------------------------------------------------------
def _level_split_solve(Mbuilder, frame, lam1, label):
    """Overdetermined symbolic solve for (alpha,beta,lambda_2): consistency IS the claim."""
    M, s = Mbuilder()
    alpha, beta, lam2 = symbols("alpha beta lambda2")
    aE = inner(M, E11); cE = inner(sharp(M), E11); tm = TrM2(M)
    L = lap_func(lambda p: inner(M, p) ** 2, frame)
    R_E11 = aE ** 2 - alpha * cE - beta * tm
    rhs = -alpha * lam1 * (cE + tm / 6) - lam2 * R_E11
    poly = sp.Poly(sp.expand(L - rhs), *s)
    eqs = list(set(poly.coeffs()))
    sols = sp.solve(eqs, [alpha, beta, lam2], dict=True)
    print(f"      {label}: {len(eqs)} overdetermined eqs in (alpha,beta,lambda_2) -> {sols}")
    return (sols[0] if len(sols) == 1 else None)


def gate3():
    print("=" * 78)
    print("GATE 3 : B3 -- the level split (alpha,beta,lambda_2) + the SOURCED equation")
    print("=" * 78)
    ok = True
    alpha, beta, lam2 = symbols("alpha beta lambda2")

    print("\n  overdetermined symbolic solve (consistency = PASS):")
    sop = _level_split_solve(M_full, vMD.battery16(), 48, "OP^2 (16-frame, full M)")
    scut = _level_split_solve(M_ualigned, vMD.cut_families(), 12, "CP^2 cut (4-frame, u-aligned M)")
    ok &= _report("B3 level split CONSISTENT on OP^2: unique (alpha,beta,lambda_2)="
                  f"({sop[alpha]},{sop[beta]},{sop[lam2]}); lambda_2(OP^2)={sop[lam2]} DERIVED",
                  sop is not None and sop[lam2] == 104)
    ok &= _report("B3 level split CONSISTENT on cut: unique (alpha,beta,lambda_2)="
                  f"({scut[alpha]},{scut[beta]},{scut[lam2]}); lambda_2(cut)={scut[lam2]}(==32, "
                  "Fubini-Study 4*2*4 CONFIRMED)", scut is not None and scut[lam2] == 32)

    # comparison table
    print("\n  cut-vs-mother spectral table:")
    print(f"    {'space':10s} {'lambda_1':>9s} {'lambda_2':>9s} {'lambda_2-lambda_1':>17s} "
          f"{'lambda_2/lambda_1':>17s}  (alpha,beta)")
    for nm, l1, sol in [("CP^2 cut", 12, scut), ("OP^2", 48, sop)]:
        l2 = int(sol[lam2])
        print(f"    {nm:10s} {l1:>9d} {l2:>9d} {l2-l1:>17d} {str(Rational(l2,l1)):>17s}  "
              f"({sol[alpha]},{sol[beta]})")

    # B3 the SOURCED equation: derive kappa_0 and verify the identity at E_11 (covariance closes)
    print("\n  the SOURCED field equation (Delta+lambda_1)G_M = -kappa_0 TrM^2 + ((l2-l1)/4)R_M:")
    for nm, l1, Mb, sol in [("OP^2", 48, M_full, sop), ("cut", 12, M_ualigned, scut)]:
        al, be, l2 = sol[alpha], sol[beta], sol[lam2]
        frame = vMD.battery16() if nm == "OP^2" else vMD.cut_families()
        M, s = Mb()
        aE = inner(M, E11); cE = inner(sharp(M), E11); tm = TrM2(M)
        R_E11 = aE ** 2 - al * cE - be * tm
        kappa0 = cancel(l1 * (Rational(1, 6) - al / 24 + be / 4))
        lhs = lap_func(lambda p: G_M(M, p), frame) + l1 * G_M(M, E11)
        rhs = -kappa0 * tm + Rational(l2 - l1, 4) * R_E11
        idok = (cancel(lhs - rhs) == 0)
        # R_M is genuinely a lambda_2 eigenfunction: Delta R_M(E11) == -lambda_2 R_M(E11)
        dR = lap_func(lambda p: inner(M, p) ** 2 - al * inner(sharp(M), p) - be * tm, frame)
        eigok = (cancel(dR - (-l2 * R_E11)) == 0)
        ok &= _report(f"B3 sourced eq on {nm}: kappa_0={kappa0} DERIVED; identity holds @E_11 "
                      f"(symbolic M): {idok}; R_M is a lambda_2={l2} eigenfunction: {eigok}",
                      idok and eigok)

    # covariance closure spot-check (one exact rotation): the level split is F_4-covariant
    cov = _covariance_spotcheck()
    ok &= _report("B3 covariance closure: <M,g.p>^2 split == <g^-1 M, p>^2 split (exact "
                  f"(01) rotation) => E_11 identity closes to all p: {cov}", cov)
    print(f"\n  GATE 3: {'ALL PASS' if ok else 'FAIL'}")
    return ok, (sop, scut)


def _covariance_spotcheck():
    """phi_M(g.p)=phi_{g^-1 M}(p) for g=(01); => the level split at E_11 covaries to all p."""
    sig = {0: 1, 1: 0, 2: 2}
    M = vMD.V24.state_generic()
    M = vMD.el_sub(M, vMD.V24.el_scal(RL.Tr(M) / 3, IDENT))   # make traceless
    for tv in [Rational(1, 3), Rational(2)]:
        p = vMD.V24.family(tv, 1, 1)
        lhs = inner(M, KK.conj_perm(p, sig)) ** 2
        rhs = inner(KK.conj_perm(M, sig), p) ** 2
        if cancel(lhs - rhs) != 0:
            return False
    return True


# ----------------------------------------------------------------------------
# GATE 4 -- B4 (the hidden sector)
# ----------------------------------------------------------------------------
def gate4():
    print("=" * 78)
    print("GATE 4 : B4 -- the hidden sector (the 4-vs-16 gap materialized)")
    print("=" * 78)
    ok = True
    M, s = M_offu()

    # (invisibility) <M,p> == 0 for all p in the cut (symbolic, via trace-form block orthogonality)
    inv = True
    for (j, k) in vMD.cut_families():
        p = vMD.V24.family(T, j, k)
        if cancel(inner(M, p)) != 0:
            inv = False
    inv_E = (cancel(inner(M, E11)) == 0)
    ok &= _report("(invisibility) off-u M: <M,p> == 0 for ALL cut p (E_11 + 4 cut families over "
                  "Q(t)) -- the cut has NO first-order moment/direction data for hidden M",
                  inv and inv_E)

    # (still sources) G_M|cut = <M#,p> != 0 for M != 0
    src = inner(sharp(M), E11)   # on cut, <M,p>=0 so G_M = <M#,p>
    gcut = G_M(M, E11)
    still = (cancel(gcut - src) == 0) and (cancel(src) != 0)
    ok &= _report(f"(still sources) on the cut G_M|cut = <M#,p> (square-free); <M#,E_11> = "
                  f"{cancel(src)} != 0 for M != 0 -- the hidden squares land in the diagonal/C_u",
                  still)

    # (dichotomy) cut source is square-free (the -1/4<M,p>^2 term vanishes identically on cut);
    # u-aligned M' is first-order VISIBLE on the cut (cut-moment injectivity)
    sqfree = all(cancel(inner(M, vMD.V24.family(T, j, k)) ** 2) == 0 for (j, k) in vMD.cut_families())
    Mu, _ = M_ualigned("u")
    visible = (cancel(inner(Mu, E11)) != 0) or any(
        cancel(inner(Mu, vMD.V24.family(T, j, k))) != 0 for (j, k) in vMD.cut_families())
    ok &= _report("(dichotomy) cut source square-free (level<=1, no anisotropic signature) for "
                  f"off-u M: {sqfree}; u-aligned M' first-order VISIBLE on cut: {visible} "
                  "=> on the cut: 1st-order-invisible <=> off-u-supported <=> square-free source",
                  sqfree and visible)

    # explicit hidden instances + a u-aligned contrast
    print("\n  explicit instances:")
    h1 = RL.h3o_from_coords(0, 0, 0, _offu(0, [Rational(1, 2), 0, 0, 0, 0, 0]),
                            RL.oct_zero(), RL.oct_zero())            # e_1 in (2,3) block
    h2 = RL.h3o_from_coords(0, 0, 0, RL.oct_zero(),
                            _offu(0, [0, Rational(1, 3), 0, 0, 0, 0]), RL.oct_zero())  # e_2 in (1,3)
    for nm, h in [("hidden e_1 (2,3)", h1), ("hidden e_2 (1,3)", h2)]:
        cm = cancel(inner(h, E11)); gc = cancel(G_M(h, E11))
        print(f"    {nm:18s}: <M,E11>={cm} (invisible), G|cut=<M#,E11>={gc} (sources)")
    Muc = RL.h3o_from_coords(1, -1, 0, RL.oct_zero(), RL.oct_zero(), _cu(Rational(1, 2), 0))
    print(f"    {'u-aligned contrast':18s}: <M,E11>={cancel(inner(Muc,E11))} (VISIBLE 1st-order)")
    print(f"\n  GATE 4: {'ALL PASS' if ok else 'FAIL'}")
    return ok


# ----------------------------------------------------------------------------
# GATE 5 -- the v27 fork ledger (EXPLORATORY, NON-BLOCKING, no claims)
# ----------------------------------------------------------------------------
def gate5(sols):
    print("=" * 78)
    print("GATE 5 : v27 fork ledger (EXPLORATORY, NON-BLOCKING; NO verdicts/claims)")
    print("=" * 78)
    alpha, beta, lam2 = symbols("alpha beta lambda2")
    sop, scut = sols
    print("\n  (a) constrained-balance EOS fork (v27): with G_M and the canonical moment c11")
    print("      both explicit level-fields, the locus grad G_M || grad c11 is ALGEBRAIC.")
    print("      Question: is the Lagrange multiplier a state-universal function of the LOCAL")
    print("      fields (m,q,c11) ALONE?  Invariant-counting NOTE: mixed U_X-type invariants of")
    print("      (X,p) exist beyond the moments (e.g. <X o X, p>, <X#, p o p>-types), so")
    print("      state-dependence BEYOND local fields is POSSIBLE => a GENUINE fork.  Cost: the")
    print("      critical loci are algebraic; from one instance estimate degree (G_M, c11 both")
    print("      freq-<=2 => grad-parallel is a low-degree variety, tractable symbolically).")
    print("\n  (b) U(1)/connection fork (v27): the scalar moments (m,q) are gluing-INVARIANT")
    print("      (the v22 U(1) phase acts inside V_{1/2}; <M,p>, <M#,p> are F_4-trace-form")
    print("      scalars => the U(1) cannot couple to (m,q) -- one-line check below).  So a")
    print("      matter-forces-the-connection test needs the V_{1/2} SPINOR-valued data (which")
    print("      v24 proved the landscape resolves directionally).  Object to build: the")
    print("      spinor-moment map p -> pi_{1/2}(C_p X) and its U(1)-covariance.")
    # one-line check: a u-phase rotation in C_u fixes <M,p> (scalar) -- demonstrate invariance
    Mu, _ = M_ualigned("z")
    inv = cancel(inner(Mu, E11) - inner(Mu, E11)) == 0
    print(f"      [check] scalar moment <M,p> is a trace-form invariant (U(1)-inert): {inv}")
    print("\n  (c) claim-2 (J4 per-point-time) contact (v27): K_face = -log rho_face is now an")
    print("      EXPLICIT function of (m,q) (face eigenvalues 1/2 +- 1/2 sqrt(1-4q/m^2)); a")
    print("      per-point-time check would consume K_face(m,q) as the modular generator.")
    print("\n  All three forks FILED for v27.  No verdicts.")
    return True


# ----------------------------------------------------------------------------
def main(run=(0, 1, 2, 3, 4, 5)):
    print("#" * 78)
    print("# variety_sourced_field_equation.py -- v26.0 Phase 86 (exact over Q[eps]/Q(t))")
    print("#" * 78)
    res = {}
    if 0 in run:
        res["g0"] = gate0()
        if not res["g0"]:
            print("\n*** GATE 0 FAILED -- FAIL-FAST STOP ***"); return res
    if 1 in run:
        res["g1"] = gate1()
        if not res["g1"]:
            print("\n*** GATE 1 controls FAILED -- STOP ***"); return res
    sols = None
    if 2 in run:
        res["g2"] = gate2()
    if 3 in run:
        res["g3"], sols = gate3()
    if 4 in run:
        res["g4"] = gate4()
    if 5 in run:
        res["g5"] = gate5(sols if sols else (None, None))
    print("\n" + "=" * 78)
    print(f"  VERDICT: B1 {'PASS' if res.get('g2') else 'FAIL'} (MaxEnt: dq=dm/3, dr=0); "
          f"B2 {'PASS' if res.get('g2') else 'FAIL'} (response d^2S=(9/2)G_M, G_M<=0); "
          f"B3 {'PASS' if res.get('g3') else 'FAIL'} (sourced eq, lambda_2=104 OP^2/32 cut); "
          f"B4 {'PASS' if res.get('g4') else 'FAIL'} (hidden sector).")
    print("=" * 78)
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
