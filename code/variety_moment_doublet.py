#!/usr/bin/env python3
"""variety_moment_doublet.py  --  v25.0 Phase 85  (J5-on-the-variety, step 1)
"The Moment Doublet and the Canonical Field Equation on the Event-Space."

CLAIMS (all verdicts symbolic/exact over Q / Q(t); floats illustrative only):

  C1 (moment-doublet identity).  For all X in h_3(O), all rank-1 idempotents p:
        m(p;X) := Tr(C_p X)       == Tr(X) - <X, p>
        q(p;X) := det_2(C_p X)    == <X#, p>
     where <A,B> = Tr(A o B), C_p = Peirce-0 compression (THE v24 code path),
     X# = X x X the Freudenthal adjoint.  Consequence: the entire v24 face
     landscape r = q/m^2 is the moment doublet of (X, X#) -- two LINEAR moment
     fields over the event-space, nothing else.

  C2 (forced canonical field equation).  Every moment field phi_Y(p) = <Y,p> is
     constants (+) first canonical Laplace level: it obeys
        Delta(phi_Y - phibar_Y) = -lambda_1 (phi_Y - phibar_Y),  phibar_Y = <Y, I/3>,
     with lambda_1 FIXED by the canonical geometry (matter-independent).  Sharpest
     form (all Y at once, at E_11): the mean-curvature vector
        Delta P := sum_i (1/4) p_i''(0)   ==   -lambda_1 (E_11 - I/3),
     lambda_1 = 48 on OP^2 (16-frame), 12 on the CP^2 cut (4-frame).

  C3 (geodesic-frequency fingerprint).  Every moment along every canonical geodesic
     is a + b cos2t + c sin2t  (frequency <= 2; t=tan(theta/2) the rational chart);
     equivalently moment*(1+t^2)^2 is a polynomial in t of degree <= 4.

DISCIPLINE: reuse v24's EXACT compression path (import variety_entropy_landscape);
det SSOT = RL.det_3; octonion_algebra BANNED.  Engines: ring_lemma_verification (RL),
kkt_gluing_holonomy (KK).  u = e_7; cut = h_3(C_u), C_u = span{1,e_7}.

TRAP GUARDS (binding): #5 -- r = q/m^2 is a RATIONAL function (infinite harmonic
content); NO field equation is claimed for r; the contentful objects are the
UNNORMALIZED doublet (m,q).  #6 -- only the FIRST-ORDER (single-eigenvalue) statement
is contentful; no polynomial-in-Delta annihilator is reported as a law.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                                       # noqa: E402
from sympy import Rational, symbols, cancel, together, Poly, degree      # noqa: E402

import ring_lemma_verification as RL                                     # noqa: E402
import kkt_gluing_holonomy as KK                                         # noqa: E402
import variety_entropy_landscape as V24   # THE v24 compression path     # noqa: E402

_t0 = time.time()
PASS = []
T = symbols("t")
E11 = KK.E_ii(0)
IDENT = RL.h3o_identity()      # the algebra identity I (for the sharp formula)
I3 = V24._I_over_3()           # I/3 (the F_4-average idempotent; for means/vacuum)


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}")


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


# ----------------------------------------------------------------------------
# 0. the Freudenthal adjoint  X# = X x X  (built ONLY from RL.jordan/Tr/identity;
#    no new convention surface) and the moment doublet
# ----------------------------------------------------------------------------
def Sigma2(X):
    """S(X) = sigma_2(X) = (Tr(X)^2 - Tr(X o X))/2  (2nd char-poly coeff)."""
    return (RL.Tr(X) ** 2 - RL.Tr(RL.jordan(X, X))) / 2


def sharp(X):
    """X# = X x X = X o X - Tr(X) X + S(X) I   (h3o-math-library.md sec.5)."""
    return V24.el_add(RL.jordan(X, X), V24.el_scal(-RL.Tr(X), X),
                      V24.el_scal(Sigma2(X), IDENT))


def inner(A, B):
    """Trace form <A,B> = Tr(A o B)."""
    return RL.Tr(RL.jordan(A, B))


def m_moment(p, X):
    """m(p;X) = Tr(X) - <X,p>   (the C1 RHS for the trace moment)."""
    return RL.Tr(X) - inner(X, p)


def q_moment(p, X):
    """q(p;X) = <X#, p>          (the C1 RHS for the det_2 moment)."""
    return inner(sharp(X), p)


def el_sub(A, B):
    return V24.el_add(A, V24.el_scal(-1, B))


def el_eq(A, B, simp=sp.cancel):
    return all(simp(A[i][j][k] - B[i][j][k]) == 0
               for i in range(3) for j in range(3) for k in range(8))


def d2_at0(p_of_t):
    """Second t-derivative of an h_3(O) family at t=0 (an h_3(O) element)."""
    return [[[sp.diff(p_of_t[i][j][k], T, 2).subs(T, 0) for k in range(8)]
             for j in range(3)] for i in range(3)]


def d1_at0(p_of_t):
    return [[[sp.diff(p_of_t[i][j][k], T).subs(T, 0) for k in range(8)]
             for j in range(3)] for i in range(3)]


# ----------------------------------------------------------------------------
# the 16-direction battery + the CP^2 cut selection
# ----------------------------------------------------------------------------
# family(t,j,k): rotate E_11 toward E_{jj} along the e_k octonion dir of the (0,j) entry.
#   j=1 -> (0,1) entry x3 -> V_{1/2} slots 19..26 (slot 19+k);
#   j=2 -> (0,2) entry x2 -> V_{1/2} slots 11..18 (slot 11+k).
# The u-aligned CP^2 cut tangent = {11,18,19,26} (V_{1/2} cap h_3(C_u)): families
#   (2,0)->11, (2,7)->18, (1,0)->19, (1,7)->26.
def battery16():
    return [(j, k) for j in (1, 2) for k in range(8)]


def slot_of(j, k):
    return (19 + k) if j == 1 else (11 + k)


CUT_SLOTS = {11, 18, 19, 26}


def cut_families():
    return [(j, k) for (j, k) in battery16() if slot_of(j, k) in CUT_SLOTS]


def c11_form_ok(p):
    """Per-family canonical-form (unit-speed geodesic) certificate:
       c11(t) = Tr(p o E_11) == ((1-t^2)/(1+t^2))^2."""
    c11 = cancel(inner(p, E11))
    ref = ((1 - T ** 2) / (1 + T ** 2)) ** 2
    return cancel(c11 - ref) == 0


# ----------------------------------------------------------------------------
# GATE 0 -- frames + machinery (fail-fast)
# ----------------------------------------------------------------------------
def gate0():
    print("=" * 78)
    print("GATE 0 : frames + machinery (the moment doublet, the cut, the Laplacian)")
    print("=" * 78)
    ok_all = True

    # --- 0.a  sharp self-pinning: the 3 defining identities (convention guard) ---
    print("\n  0.a sharp X# pinned by its defining identities (repo conventions):")
    Xg = V24.state_generic()
    Yv = V24.state_v18_matter()
    Xs = sharp(Xg)
    adj = el_eq(sharp(Xs), V24.el_scal(RL.det_3(Xg), Xg), sp.expand)
    grad = (cancel(inner(Xs, Yv)) == cancel(RL.polarize_d(Xg, Xg, Yv) / 2))
    trsig = (cancel(RL.Tr(Xs) - Sigma2(Xg)) == 0)
    rk1 = el_eq(sharp(E11), V24.el_zero()) and (RL.Tr(E11) == 1)
    ok_all &= _report("(X#)# == det_3(X) X  (adjugate identity)", adj)
    ok_all &= _report("Tr(X# o Y) == (1/2) d(X,X,Y)  (X# = grad of N)", grad)
    ok_all &= _report("Tr(X#) == sigma_2(X);  rank-1: E_11# == 0, Tr E_11 == 1", trsig and rk1)

    # --- 0.b  16-family battery: idempotent, Tr=1, p(0)=E_11, c11-form certificate ---
    print("\n  0.b 16-family battery (j in {1,2}, k in 0..7) exact over Q(t):")
    survivors, cut = [], []
    for (j, k) in battery16():
        p = V24.family(T, j, k)
        pp = RL.jordan(p, p)
        idem = el_eq(pp, p)
        trp = (cancel(RL.Tr(p)) == 1)
        at0 = el_eq([[[p[i][jj][kk].subs(T, 0) for kk in range(8)]
                      for jj in range(3)] for i in range(3)], E11, sp.simplify)
        cform = c11_form_ok(p)
        ok = idem and trp and at0 and cform
        ok_all &= ok
        if ok:
            survivors.append((j, k))
            if slot_of(j, k) in CUT_SLOTS:
                cut.append((j, k))
        if not ok or (j, k) in cut_families():
            print(f"      ({j},{k}) slot {slot_of(j,k):2d}: idem={idem} Tr1={trp} "
                  f"p0=E11={at0} c11-cert={cform}"
                  f"{'   <-- CUT' if slot_of(j,k) in CUT_SLOTS else ''}")
    _report(f"all 16 families pass idem/Tr/base/c11-cert; survivors={len(survivors)} "
            f"(need >=16)", len(survivors) == 16)
    _report(f"CP^2 cut = 4 c11-certified families {cut} (slots {sorted(slot_of(j,k) for j,k in cut)} "
            f"== {{11,18,19,26}})",
            len(cut) == 4 and sorted(slot_of(j, k) for j, k in cut) == [11, 18, 19, 26])
    ok_all &= (len(survivors) == 16 and len(cut) == 4)

    # --- 0.c  orthonormality of the 16 tangent directions (trace-form Gram) ---
    print("\n  0.c tangent frame at E_11 (trace-form Gram of e_i = p_i'(0)):")
    tangents = {(j, k): d1_at0(V24.family(T, j, k)) for (j, k) in battery16()}
    keys = battery16()
    gram_diag_const = True
    gram_offdiag_zero = True
    norms = set()
    for a in range(16):
        for b in range(a, 16):
            g = cancel(inner(tangents[keys[a]], tangents[keys[b]]))
            if a == b:
                norms.add(g)
            elif g != 0:
                gram_offdiag_zero = False
    gram_diag_const = (len(norms) == 1)
    nval = next(iter(norms))
    ok_all &= _report(f"Gram = {nval} * I_16  (orthogonal, equinormed => orthonormal "
                      f"frame {{e_i/sqrt({nval})}})", gram_diag_const and gram_offdiag_zero)

    # --- 0.d  Laplacian assembler + chain-rule, verified on cos^2 theta ---
    print("\n  0.d Laplacian assembler  Delta f(E_11) = sum_i (1/4) (d^2/dt^2 f@gamma_i)|_0 :")
    # chain rule at t=0: dt/dtheta=(1+t^2)/2 -> 1/2 ; d^2 t/dtheta^2 = t(1+t^2) -> 0.
    # so f''_theta(0) = (1/2)^2 f''_t(0) + 0 = (1/4) f''_t(0).  Verify on c11 = cos^2 theta:
    c11 = inner(V24.family(T, 1, 0), E11)
    f2t = sp.diff(c11, T, 2).subs(T, 0)            # = -8
    contrib_theta = Rational(1, 4) * f2t           # = -2  (per direction)
    ok_chain = (contrib_theta == -2)
    ok_all &= _report(f"chain rule on c11=cos^2(theta): (1/4) c11''_t(0) = {contrib_theta} "
                      f"== -2 (= (cos^2)''_theta)", ok_chain)
    print(f"\n  GATE 0: {'ALL PASS' if ok_all else 'FAIL'}")
    return ok_all, survivors, cut


# ----------------------------------------------------------------------------
# the mean-curvature vector and the C2 eigenvalue extraction
# ----------------------------------------------------------------------------
def mean_curv(frame):
    """Delta P = sum_i (1/4) p_i''(0) over a frame of (j,k) families (an h_3(O) elt)."""
    DP = V24.el_zero()
    for (j, k) in frame:
        DP = V24.el_add(DP, V24.el_scal(Rational(1, 4), d2_at0(V24.family(T, j, k))))
    return V24.el_simplify(DP, sp.cancel)


def extract_lambda(DP):
    """lambda_1 from ONE component (non-hardwired): -Delta c11 / (c11(E11) - cbar).
       c11(E11)=<E11,E11>=1, cbar=<E11,I/3>=1/3 => denominator 2/3."""
    num = inner(E11, DP)               # = Delta phi_{E11}(E11)
    den = inner(E11, E11) - inner(E11, I3)
    return cancel(-num / den)


# ----------------------------------------------------------------------------
# GATE 1 -- controls (known answers; zero evidential weight; must behave)
# ----------------------------------------------------------------------------
def freq_le2(expr):
    """C3 test: expr(t) = a + b cos2theta + c sin2theta  <=>  expr*(1+t^2)^2 is a
       polynomial in t of degree <= 4.  Returns (ok, numerator_poly_or_None)."""
    e = cancel(expr * (1 + T ** 2) ** 2)
    if e.free_symbols and not e.is_polynomial(T):
        return False, None
    p = Poly(sp.expand(e), T)
    return (degree(p, T) <= 4), p


def gate1():
    print("=" * 78)
    print("GATE 1 : controls (known answers; ZERO evidential weight; must behave)")
    print("=" * 78)
    ok_all = True

    # known-LIVE: c11 = phi_{E11} passes Helmholtz with lambda_1 = 48 (OP^2), 12 (cut)
    DP_full = mean_curv(battery16())
    DP_cut = mean_curv(cut_families())
    lam_full = extract_lambda(DP_full)
    lam_cut = extract_lambda(DP_cut)
    c1 = el_eq(DP_full, V24.el_scal(-lam_full, el_sub(E11, I3)))
    c2 = el_eq(DP_cut, V24.el_scal(-lam_cut, el_sub(E11, I3)))
    ok_all &= _report(f"known-LIVE control: phi_E11 Helmholtz, lambda_1(OP^2)={lam_full} "
                      f"(==48), full-vector DeltaP==-lam(E11-I/3): {c1}", lam_full == 48 and c1)
    ok_all &= _report(f"known-LIVE control: phi_E11 Helmholtz, lambda_1(CP^2 cut)={lam_cut} "
                      f"(==12), full-vector identity: {c2}", lam_cut == 12 and c2)

    # known-MIXED (discriminating power): c11^2 = cos^4 theta = frequency 4 -> must FAIL freq<=2
    c11 = inner(V24.family(T, 1, 0), E11)
    okp, _ = freq_le2(c11)
    okp2, _ = freq_le2(c11 ** 2)
    ok_all &= _report(f"known-MIXED control: c11 freq<=2 (PASS={okp}) but c11^2=cos^4 "
                      f"freq<=2 (PASS={okp2}) -> test CAN say no", okp and (not okp2))

    # trivial control: X = I/3 -> both moments constant, Delta = 0, equation 0=0
    Xv = I3
    triv_ok = True
    for (j, k) in cut_families():
        p = V24.family(T, j, k)
        triv_ok &= (cancel(m_moment(p, Xv) - Rational(2, 3)) == 0)
        triv_ok &= (cancel(q_moment(p, Xv) - Rational(1, 9)) == 0)
    ok_all &= _report("trivial control: X=I/3 -> m==2/3, q==1/9 constant (Delta=0, 0=0)", triv_ok)
    print(f"\n  GATE 1: {'ALL PASS' if ok_all else 'FAIL'}")
    return ok_all


# ----------------------------------------------------------------------------
# GATE 2 -- C1: the doublet identity + completeness (the core)
# ----------------------------------------------------------------------------
def _symX():
    xs = symbols("X0:27", real=True)
    return RL.h3o_from_coords(xs[0], xs[1], xs[2], list(xs[3:11]),
                              list(xs[11:19]), list(xs[19:27])), xs


def gate2():
    print("=" * 78)
    print("GATE 2 : C1 -- the moment-doublet identity + completeness (THE CORE)")
    print("=" * 78)
    ok_all = True
    Xsym, _ = _symX()

    # --- C1 at p = E_11, SYMBOLIC X (the F_4-covariance BASE point) ---
    Cp = V24.compress0(E11, Xsym)
    m_lhs = sp.expand(RL.Tr(Cp))
    q_lhs = sp.expand((RL.Tr(Cp) ** 2 - RL.Tr(RL.jordan(Cp, Cp))) / 2)
    m_base = (sp.simplify(m_lhs - sp.expand(m_moment(E11, Xsym))) == 0)
    q_base = (sp.simplify(q_lhs - sp.expand(q_moment(E11, Xsym))) == 0)
    ok_all &= _report("C1 @ E_11, symbolic X (27 params): m==Tr(X)-<X,E11>, q==<X#,E11>",
                      m_base and q_base)

    # --- C1 along ALL 16 families, SYMBOLIC X over Q(t) (decisive, no shortcut) ---
    print("\n  C1 along all 16 families, symbolic X over Q(t):")
    fam_ok = True
    for (j, k) in battery16():
        p = V24.family(T, j, k)
        Cp = V24.compress0(p, Xsym)
        m_l = cancel(RL.Tr(Cp))
        q_l = cancel((RL.Tr(Cp) ** 2 - RL.Tr(RL.jordan(Cp, Cp))) / 2)
        mm = (cancel(m_l - m_moment(p, Xsym)) == 0)
        qq = (cancel(q_l - q_moment(p, Xsym)) == 0)
        fam_ok &= (mm and qq)
        if (j, k) in cut_families() or not (mm and qq):
            print(f"      ({j},{k}) slot {slot_of(j,k):2d}: m=={mm}  q=={qq}")
    ok_all &= _report("C1 holds along all 16 families, symbolic X over Q(t) "
                      "(incl. off-u (1,1)..(1,6),(2,1)..)", fam_ok)

    # --- F_4-covariance closure (all p) + an exact non-stabilizer spot-check ---
    print("\n  covariance closure  phi_Y(g.p) = phi_{g^-1 Y}(p)  (g = exact F_4 autos):")
    sig01 = {0: 1, 1: 0, 2: 2}                 # E_11<->E_22  (involution)
    sig012 = {0: 1, 1: 2, 2: 0}                # 3-cycle
    sig012_inv = {0: 2, 1: 0, 2: 1}
    cov_ok = True
    for (sig, sinv, nm) in [(sig01, sig01, "(01)"), (sig012, sig012_inv, "(012)")]:
        for (Yname, Ymat) in [("X_gen", V24.state_generic()), ("X#_gen", sharp(V24.state_generic()))]:
            for tv in [Rational(1, 3), Rational(2)]:
                p = V24.family(tv, 1, 1)       # an off-u sample point
                lhs = cancel(inner(Ymat, KK.conj_perm(p, sig)))
                rhs = cancel(inner(KK.conj_perm(Ymat, sinv), p))
                cov_ok &= (cancel(lhs - rhs) == 0)
    ok_all &= _report("phi_Y(g.p)==phi_{g^-1 Y}(p) for g in {(01),(012)}, Y in {X,X#}, "
                      "off-u samples => C1 at E_11 (all X) closes to ALL p", cov_ok)
    print("      [closure argument] every rank-1 p = g.E_11 (F_4 transitive, Borel); C1 is")
    print("      F_4-covariant: m(g.E11;X)=m(E11;g^-1 X), q likewise (g preserves Tr, o, #).")
    print("      => C1 @ E_11 for symbolic X  =>  C1 @ all p for all X.  QED.")

    # --- completeness: the v24 verdict object r = q/m^2 is a function of (m,q) alone ---
    print("\n  completeness -- v24 phenomenology reproduced FROM the doublet:")
    ok_all &= _completeness()
    print(f"\n  GATE 2: {'ALL PASS' if ok_all else 'FAIL'}")
    return ok_all


def _completeness():
    ok = True
    # (a) vacuum row DERIVED: X=I/3 -> X#=I/9 -> q=1/9, m=2/3, r=1/4
    sharp_I3 = sharp(I3)
    vac = el_eq(sharp_I3, V24.el_scal(Rational(1, 9), RL.h3o_identity()))
    ok &= _report("(a) vacuum DERIVED: (I/3)# == I/9 => q==1/9, m==2/3, r==1/4 "
                  "(homogeneity because both moments of (I/3,(I/3)#) are constant)", vac)

    # (b) diagonal direction-blindness DERIVED (not just observed)
    Xd = V24.state_diagonal()
    Xds = sharp(Xd)
    diag_sharp = el_eq(el_sub(Xds, _diag_part(Xds)), V24.el_zero())   # X# is diagonal
    qs = []
    for k in (0, 1, 7):
        qs.append(cancel(q_moment(V24.family(T, 1, k), Xd)))
    blind = all(cancel(qs[0] - qq) == 0 for qq in qs)
    ok &= _report("(b) diagonal X => X# diagonal => <X#,p> sees only diag(p) & |offdiag|^2 "
                  f"=> q INDEPENDENT of e_k (k=0,1,7 identical): {blind}", diag_sharp and blind)

    # (c) one recorded generic-X r(t) with exact sample values
    Xg = V24.state_generic()
    r_offu = together(q_moment(V24.family(T, 1, 1), Xg) / m_moment(V24.family(T, 1, 1), Xg) ** 2)
    r_cu = together(q_moment(V24.family(T, 1, 7), Xg) / m_moment(V24.family(T, 1, 7), Xg) ** 2)
    s_offu2 = cancel(r_offu.subs(T, 2))
    s_cu3 = cancel(r_cu.subs(T, 3))
    rec = (s_offu2 == Rational(2727493, 12700800)) and (s_cu3 == Rational(503003, 2252432))
    ok &= _report(f"(c) generic-X r(t) FROM doublet: off-u r(2)={s_offu2} (==2727493/12700800), "
                  f"C_u-phase r(3)={s_cu3} (==503003/2252432)", rec)

    # (d) eigenframe-critical-points: transverse-real (1,0) gives standard frame {-1,0,1};
    #     matter-coupled (1,7),(1,1) give degree-8 (rotated eigenframe) -- structural reproduction
    r_tr = together(q_moment(V24.family(T, 1, 0), Xg) / m_moment(V24.family(T, 1, 0), Xg) ** 2)
    roots_tr = sorted([rr for rr in sp.solve(sp.numer(cancel(sp.diff(r_tr, T))), T)
                       if rr.is_real], key=lambda z: float(z))
    deg_offu = degree(Poly(sp.numer(cancel(sp.diff(r_offu, T))), T), T)
    ok &= _report(f"(d) critical pts: transverse-real dr/dt=0 at {roots_tr} (==[-1,0,1], standard "
                  f"frame); off-u numerator degree {deg_offu} (>4 => eigenframe-tracking)",
                  roots_tr == [-1, 0, 1] and deg_offu >= 5)

    # (e) flattening DERIVED: X_s = (1-s)I/3 + s X_gen -> moments affine in s near vacuum,
    #     landscape gradient dr/dtau|_0 vanishes at s=0 and grows with matter (recorded table)
    s = symbols("s")
    tau = symbols("tau")
    pprobe = V24.family(tau, 1, 1)
    flat_tbl, flat_ok = [], True
    for sv in [Rational(0), Rational(1, 4), Rational(1, 2), Rational(3, 4), Rational(1)]:
        Xs = V24.el_add(V24.el_scal(1 - sv, I3), V24.el_scal(sv, Xg))
        rr = together(q_moment(pprobe, Xs) / m_moment(pprobe, Xs) ** 2)
        grad = cancel(sp.diff(rr, tau).subs(tau, 0))
        flat_tbl.append((sv, grad))
        if sv == 0 and grad != 0:
            flat_ok = False
    rec_tbl = (flat_tbl[1][1] == Rational(13879, 1837500)) and (flat_tbl[4][1] == Rational(629, 58800))
    ok &= _report("(e) flattening DERIVED: dr/dtau|_0 == 0 at s=0 (vacuum homogeneous), "
                  f"==13879/1837500 at s=1/4, ==629/58800 at s=1 (recorded): {rec_tbl}",
                  flat_ok and rec_tbl)
    return ok


def _diag_part(X):
    out = V24.el_zero()
    for i in range(3):
        out[i][i] = list(X[i][i])
    return out


# ----------------------------------------------------------------------------
# GATE 3 -- C2 + C3: the field equation and the eigenvalues
# ----------------------------------------------------------------------------
def gate3():
    print("=" * 78)
    print("GATE 3 : C2 (field equation, lambda_1) + C3 (frequency fingerprint)")
    print("=" * 78)
    ok_all = True

    # --- C2: the mean-curvature vector identity, both frames (the field equation) ---
    DP_full = mean_curv(battery16())
    DP_cut = mean_curv(cut_families())
    lam_full = extract_lambda(DP_full)
    lam_cut = extract_lambda(DP_cut)
    idF = el_eq(DP_full, V24.el_scal(-lam_full, el_sub(E11, I3)))
    idC = el_eq(DP_cut, V24.el_scal(-lam_cut, el_sub(E11, I3)))
    print(f"      Delta P (OP^2 16-frame) = {_diagstr(DP_full)}  ;  lambda_1 = {lam_full}")
    print(f"      Delta P (CP^2 4-frame ) = {_diagstr(DP_cut)}  ;  lambda_1 = {lam_cut}")
    ok_all &= _report(f"C2 OP^2: DeltaP == -{lam_full}(E_11 - I/3) [all 27 comps]; lambda_1=48 "
                      f"pre-registered {'CONFIRMED' if lam_full==48 else 'CORRECTED'}",
                      idF and lam_full == 48)
    ok_all &= _report(f"C2 CP^2 cut: DeltaP == -{lam_cut}(E_11 - I/3) [all 27 comps]; lambda_1=12 "
                      f"pre-registered {'CONFIRMED' if lam_cut==12 else 'CORRECTED'} "
                      f"(== 4(n+1)|_{{n=2}}, Fubini-Study)", idC and lam_cut == 12)
    ok_all &= _report(f"ratio lambda_1(OP^2)/lambda_1(CP^2) = {Rational(lam_full,lam_cut)} == 4 "
                      f"== dimension ratio 16/4", Rational(lam_full, lam_cut) == 4)

    # --- C2 means + field equations for the doublet (symbolic X) ---
    Xsym, _ = _symX()
    mbar = cancel(inner(Xsym, I3))            # <X, I/3> = (1/3)Tr X
    qbar = cancel(inner(sharp(Xsym), I3))     # <X#, I/3> = (1/3)Tr(X#) = sigma_2/3
    mbar_ok = (cancel(mbar - Rational(1, 3) * RL.Tr(Xsym)) == 0)
    # m = Tr X - phi_X => mean of m is Tr X - <X,I/3> = (2/3)Tr X
    m_mean_ok = (cancel((RL.Tr(Xsym) - mbar) - Rational(2, 3) * RL.Tr(Xsym)) == 0)
    qbar_ok = (cancel(qbar - Rational(1, 3) * RL.Tr(sharp(Xsym))) == 0)
    ok_all &= _report("means via <Y,I/3>: mbar==(2/3)Tr X, qbar==sigma_2(X)/3=Tr(X#)/3 "
                      "(F_4-average p=I/3, exact, no integration)", mbar_ok and m_mean_ok and qbar_ok)
    print("      => field equations (final form):")
    print("         Delta m = -lambda_1 ( m - (2/3) Tr X )")
    print("         Delta q = -lambda_1 ( q - sigma_2(X)/3 ),   lambda_1 = 48 (OP^2) / 12 (cut)")

    # --- C2 eigenfunction identity for SYMBOLIC Y at E_11 (all Y at once) ---
    # Delta phi_Y(E11) = <Y, DeltaP> = -lambda_1 <Y, E11 - I/3> for ALL Y  <=>  the vector
    # identity DeltaP = -lambda_1 (E11 - I/3) already proven => holds for symbolic Y.  Spot-check:
    Ysym, ys = _symX()
    lhsY = cancel(inner(Ysym, DP_full))
    rhsY = cancel(-lam_full * (inner(Ysym, E11) - inner(Ysym, I3)))
    ok_all &= _report("C2 for SYMBOLIC Y at E_11: <Y,DeltaP> == -48 <Y, E_11 - I/3> "
                      "(linear identity in all 27 Y-params)", cancel(lhsY - rhsY) == 0)

    # --- C3: frequency fingerprint per family, symbolic X ---
    print("\n  C3 frequency fingerprint (moment*(1+t^2)^2 is deg<=4 in t):")
    c3_ok = True
    for (j, k) in cut_families() + [(1, 1)]:
        p = V24.family(T, j, k)
        m_ok, _ = freq_le2(m_moment(p, Xsym))
        q_ok, _ = freq_le2(q_moment(p, Xsym))
        c3_ok &= (m_ok and q_ok)
        print(f"      ({j},{k}) slot {slot_of(j,k):2d}: m freq<=2 {m_ok}, q freq<=2 {q_ok}")
    ok_all &= _report("C3: m,q frequency<=2 (a+b cos2t+c sin2t) on all cut + off-u families, "
                      "symbolic X", c3_ok)
    # the v24 r(t) is then a ratio of frequency-2 trigs over a squared one -> rational (guard #5)
    print("      => r = q/m^2 is a RATIO of frequency-2 trigs over a squared one: a RATIONAL")
    print("         function (infinite harmonic content) -- correctly BANNED as a field-eq object.")

    # --- C3 hand anchor: diag(7,5,3) on (1,0) gives m=9-cos2t, q=18-3cos2t ---
    Xd = V24.state_diagonal()
    cos2 = 2 * ((1 - T ** 2) / (1 + T ** 2)) ** 2 - 1
    a1 = (cancel(m_moment(V24.family(T, 1, 0), Xd) - (9 - cos2)) == 0)
    a2 = (cancel(q_moment(V24.family(T, 1, 0), Xd) - (18 - 3 * cos2)) == 0)
    ok_all &= _report("C3 anchor: diag(7,5,3) on (1,0): m==9-cos2theta, q==18-3cos2theta", a1 and a2)

    # --- frame-independence (Gate 0.4 closure): DeltaP from a rotated cut frame agrees ---
    print("\n  frame-independence: DeltaP_cut from a Pythagorean-rotated cut frame:")
    DP_cut_rot = _mean_curv_rotated_cut()
    fi1 = el_eq(DP_cut, DP_cut_rot)
    # and the entry-swap Spin(9) automorphism leaves DeltaP_full invariant
    sig_swap = {0: 0, 1: 2, 2: 1}             # swap entries 2<->3 (fixes E_11, in Spin(9))
    DP_full_swap = V24.el_simplify(KK.conj_perm(DP_full, sig_swap), sp.cancel)
    fi2 = el_eq(DP_full, DP_full_swap)
    ok_all &= _report(f"frame-indep: DeltaP_cut(standard)==DeltaP_cut(rotated 3/5-4/5): {fi1}; "
                      f"entry-swap Spin(9): DeltaP_full invariant: {fi2}", fi1 and fi2)
    print(f"\n  GATE 3: {'ALL PASS' if ok_all else 'FAIL'}")
    return ok_all, lam_full, lam_cut


def _diagstr(X):
    return "diag(" + ", ".join(str(X[i][i][0]) for i in range(3)) + ")"


def _cu_family(t, va, vb):
    """A rank-1 idempotent family in h_3(C_u): v=(c, s*va, s*vb), va,vb in span{1,e_7}
       (shared k=7 => exact via cmul_k).  c=(1-t^2)/(1+t^2), s=2t/(1+t^2)."""
    c, s = V24._pyth(t)
    v0 = V24.oct1(0, c)
    v1 = [s * va[i] for i in range(8)]
    v2 = [s * vb[i] for i in range(8)]
    return V24.herm_from_vec([v0, v1, v2])


def _mean_curv_rotated_cut():
    """Cut 4-frame rotated by a Pythagorean SO(2) (3/5,4/5) mixing the (j=1,j=2) entries,
       in both the real and the e_7 channel.  Still v0=c => same c11 cert (unit-speed)."""
    a, b = Rational(3, 5), Rational(4, 5)
    one = V24.oct1(0, 1)
    e7 = V24.oct1(7, 1)
    dirs = [
        ([a * one[i] for i in range(8)], [b * one[i] for i in range(8)]),    # real, +
        ([-b * one[i] for i in range(8)], [a * one[i] for i in range(8)]),   # real, perp
        ([a * e7[i] for i in range(8)], [b * e7[i] for i in range(8)]),      # e7, +
        ([-b * e7[i] for i in range(8)], [a * e7[i] for i in range(8)]),     # e7, perp
    ]
    DP = V24.el_zero()
    for (va, vb) in dirs:
        p = _cu_family(T, va, vb)
        DP = V24.el_add(DP, V24.el_scal(Rational(1, 4), d2_at0(p)))
    return V24.el_simplify(DP, sp.cancel)


# ----------------------------------------------------------------------------
# GATE 4 -- the v26 design ledger (EXPLORATORY, NON-BLOCKING, no law claims)
# ----------------------------------------------------------------------------
def gate4(lam_full, lam_cut):
    print("=" * 78)
    print("GATE 4 : v26 design ledger (EXPLORATORY, NON-BLOCKING; NO law/balance claims)")
    print("=" * 78)
    Xg = V24.state_generic()
    # (b) per-class doublet table: where (X, X#) sit, trace-heavy vs V_{1/2}-supported
    print("\n  (b) per-class doublet table (m,q at E_11; means; level):")
    print(f"      {'state':22s} {'m(E11)':>10s} {'q(E11)':>14s} {'mbar=2TrX/3':>14s} {'qbar=s2/3':>14s}")
    for nm, X in [("I/3 (vacuum)", I3), ("diag(7,5,3)", V24.state_diagonal()),
                  ("v18-matter V_1/2", V24.state_v18_matter()), ("GENERIC", Xg)]:
        mE = cancel(m_moment(E11, X)); qE = cancel(q_moment(E11, X))
        mb = cancel(Rational(2, 3) * RL.Tr(X)); qb = cancel(Sigma2(X) / 3)
        print(f"      {nm:22s} {str(mE):>10s} {str(qE):>14s} {str(mb):>14s} {str(qb):>14s}")
    print("      -- both sources (X, X#) are level-<=1 moment fields with the SAME lambda_1;")
    print("         NO level>=2 contamination is possible in THIS landscape (CGM/Speranza")
    print("         exposure structurally absent -- finite face-purity, not a QFT entropy).")

    # (a) balance inventory (design input only)
    print("\n  (a) candidate J5/Jacobson-type balances on the variety (v26 DESIGN INPUT ONLY):")
    print("      1. linear moment relation  alpha*m + beta*q = c11-reference moment  (both")
    print("         level-1; a balance fixes (alpha,beta) -- vacuity risk: trivially solvable")
    print("         unless a SECOND constraint (e.g. q from X# vs m from X) is imposed.")
    print("      2. constrained extremization  extremize S(face)=S(m,q) at fixed canonical")
    print("         moment <Y0,p> -- multiplier nonzero iff dS/dp not parallel to the canonical")
    print("         gradient; v24 Gate-3 distinctness (eigenframe vs direction-blind) suggests")
    print("         it can be -- the v26 test object.")
    print("      3. all-balls quantifier analog: demand the balance hold for ALL faces (all p);")
    print("         the covariance closure (C1) makes this a single-point condition -- low")
    print("         vacuity risk but also possibly content-free; flag for v26 triage.")

    # (c) cut-vs-mother comparison
    print("\n  (c) cut (CP^2, lambda_1=12) vs mother (OP^2, lambda_1=48):")
    print(f"      lambda ratio {Rational(lam_full,lam_cut)} = dim ratio 4; the 16-frame carries 12")
    print("      extra (non-C_u) directions {12..17,20..25} that the 4-frame does NOT -- the")
    print("      bottleneck's first dynamical fingerprint is exactly this 4-vs-16 gap (matter")
    print("      in the off-u octonion directions is invisible to the cut).  Design input for v26.")
    return True


# ----------------------------------------------------------------------------
def main(run=(0, 1, 2, 3, 4)):
    print("#" * 78)
    print("# variety_moment_doublet.py -- v25.0 Phase 85 (exact over Q / Q(t))")
    print("#" * 78)
    res = {}
    survivors = cut = None
    if 0 in run:
        res["gate0"], survivors, cut = gate0()
        if not res["gate0"]:
            print("\n*** GATE 0 FAILED (frames/machinery) -- FAIL-FAST STOP ***")
            return res
    if 1 in run:
        res["gate1"] = gate1()
        if not res["gate1"]:
            print("\n*** GATE 1 controls FAILED -- machinery broken, STOP ***")
            return res
    lam_full = lam_cut = None
    if 2 in run:
        res["gate2"] = gate2()
    if 3 in run:
        res["gate3"], lam_full, lam_cut = gate3()
    if 4 in run:
        res["gate4"] = gate4(lam_full or 48, lam_cut or 12)
    print("\n" + "=" * 78)
    c1 = res.get("gate2")
    c2 = res.get("gate3")
    print(f"  VERDICT: C1 {'PASS' if c1 else 'FAIL'} (moment-doublet identity); "
          f"C2 {'PASS' if c2 else 'FAIL'} (field equation, lambda_1=48 OP^2 / 12 CP^2 cut); "
          f"C3 frequency<=2 fingerprint {'PASS' if c2 else 'FAIL'}.")
    print("=" * 78)
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return res


if __name__ == "__main__":
    main()
