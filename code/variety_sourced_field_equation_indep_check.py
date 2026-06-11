#!/usr/bin/env python3
"""FROM-SCRATCH independent check of v26.0 Phase 86.

Imports NEITHER variety_sourced_field_equation*.py NOR variety_moment_doublet*.py.
I build, from scratch:
  - the octonion product (my OWN Cayley-Dickson table, then cross-checked vs RL.oct_mul);
  - the h3o layout, Jordan product, trace, trace form;
  - M# via the HERMITIAN ADJUGATE (cofactor matrix) -- a DIFFERENT construction from
    both the executor (M o M - Tr(M)M + sigma2(M) I) and the verifier (gradient-of-N);
  - the compression C_p X and the Laplacian assembler.
RL is used ONLY as the shared certified octonion arena cross-check (octonion_algebra BANNED).
I confirm independently:
  (a) dr=0 identically in Q[eps]; d^2 r = (9/4) G_M at E_11, symbolic traceless M;
  (b) positivity G_M = -(1/4)(eigengap)^2 <= 0; anchors G(E11)=0, G(E22)=-9/4;
  (c) the level-split overdetermined solve -> (1/7,9/182,104) OP^2, (2/5,3/20,32) cut;
  (d) kappa_0 = 108/13 (OP^2) and the sourced-equation identity;
  (e) hidden-sector invisibility <M,p>=0 on the cut for off-u M;
  plus the I x M = -M/2 sharp identity and an adversarial 104-not-hardwired check.
"""
import sympy as sp
from sympy import Rational as R, symbols, cancel, expand, sqrt, log as slog

# ---- RL ONLY as the certified octonion ARENA cross-check (allowed shared ground) ----
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "/Users/ehrlich/scratch/get-physics-done/code")
import ring_lemma_verification as RL

EPS = symbols("epsilon")
T = symbols("t")
PASS = []


def rep(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


# ============================================================================
# 1. MY OWN octonion multiplication, built from Cayley-Dickson doubling of the
#    quaternions, INDEPENDENT of RL's Fano-table _MUL_TABLE.  Then cross-check.
# ============================================================================
# Cayley-Dickson: O = H (+) H e, with (a,b)(c,d) = (ac - conj(d) b, d a + b conj(c)).
# Quaternion basis 1,i,j,k = e0,e1,e2,e3 ; octonion e4 = the doubling unit.
# e_{4+m} = e_m * e4 for m=0..3.  This gives a CONCRETE 8-dim table.
def _quat_mul(a, b):
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3,
            a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1,
            a0*b3 + a1*b2 - a2*b1 + a3*b0)


def _quat_conj(a):
    return (a[0], -a[1], -a[2], -a[3])


def my_oct_mul(x, y):
    """My own octonion product via Cayley-Dickson (a,b)(c,d)=(ac-conj(d)b, da+b conj(c))."""
    a = tuple(x[0:4]); b = tuple(x[4:8])
    c = tuple(y[0:4]); d = tuple(y[4:8])
    # ac - conj(d) b
    p1 = _quat_mul(a, c)
    p2 = _quat_mul(_quat_conj(d), b)
    lo = tuple(p1[i] - p2[i] for i in range(4))
    # d a + b conj(c)
    p3 = _quat_mul(d, a)
    p4 = _quat_mul(b, _quat_conj(c))
    hi = tuple(p3[i] + p4[i] for i in range(4))
    return list(lo) + list(hi)


def _basis(i):
    z = [sp.Integer(0)] * 8
    z[i] = sp.Integer(1)
    return z


# NOTE: my Cayley-Dickson basis labels need NOT match RL's Fano labels e_1..e_7.
# I do NOT need them to match -- I run my ENTIRE pipeline twice (once with my product,
# once with RL's) and check each reproduces the SAME claimed rationals.  The claims are
# basis-label-independent (alpha,beta,lambda_2,kappa_0,the anchors), so agreement of
# BOTH self-consistent pipelines is the strongest cross-check.  I also verify my product
# is a valid normed division algebra (alternative + norm-multiplicative) below.

def oct_conj(a):
    return [a[0]] + [-a[i] for i in range(1, 8)]


def oct_normsq(a):
    return sum(a[i]**2 for i in range(8))


# sanity: my product is unital, alternative, and norm-multiplicative (=> a composition algebra)
def _check_my_octonions():
    e = [_basis(i) for i in range(8)]
    one = _basis(0)
    # unital
    for i in range(8):
        assert my_oct_mul(one, e[i]) == e[i] and my_oct_mul(e[i], one) == e[i]
    # imaginary units square to -1
    for i in range(1, 8):
        assert my_oct_mul(e[i], e[i]) == [-1 if k == 0 else 0 for k in range(8)]
    # norm multiplicative on a few symbolic vectors: N(xy)=N(x)N(y)
    xs = symbols("a0:8"); ys = symbols("b0:8")
    x = list(xs); y = list(ys)
    lhs = expand(oct_normsq(my_oct_mul(x, y)))
    rhs = expand(oct_normsq(x) * oct_normsq(y))
    assert expand(lhs - rhs) == 0, "my octonions not norm-multiplicative!"
    # alternative algebra: (xx)y = x(xy)
    assert all(expand(c) == 0 for c in
               (sp.Matrix(my_oct_mul(my_oct_mul(x, x), y)) - sp.Matrix(my_oct_mul(x, my_oct_mul(x, y)))))
    return True


# ============================================================================
# 2. h_3(O) layout (matches the repo: alpha, conj(x3), x2 / x3, beta, conj(x1) / ...)
#    parametrized by (a,b,g, x1,x2,x3); built into a full 3x3 octonion matrix.
# ============================================================================
def h3o(a, b, g, x1, x2, x3):
    a = [sp.sympify(a)] + [sp.Integer(0)]*7
    b = [sp.sympify(b)] + [sp.Integer(0)]*7
    g = [sp.sympify(g)] + [sp.Integer(0)]*7
    return [[a, oct_conj(x3), x2],
            [x3, b, oct_conj(x1)],
            [oct_conj(x2), x1, g]]


def Z8():
    return [sp.Integer(0)]*8


def IDENT():
    return h3o(1, 1, 1, Z8(), Z8(), Z8())


def matadd(*Xs):
    out = [[Z8() for _ in range(3)] for _ in range(3)]
    for X in Xs:
        for i in range(3):
            for j in range(3):
                for k in range(8):
                    out[i][j][k] = out[i][j][k] + X[i][j][k]
    return out


def matscal(c, X):
    c = sp.sympify(c)
    return [[[c*X[i][j][k] for k in range(8)] for j in range(3)] for i in range(3)]


def matmul(A, B, omul):
    C = [[Z8() for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            acc = Z8()
            for k in range(3):
                pr = omul(A[i][k], B[k][j])
                acc = [acc[m] + pr[m] for m in range(8)]
            C[i][j] = acc
    return C


def jordan(A, B, omul):
    AB = matmul(A, B, omul)
    BA = matmul(B, A, omul)
    return matscal(R(1, 2), matadd(AB, BA))


def Tr(X):
    return X[0][0][0] + X[1][1][0] + X[2][2][0]


def inner(A, B, omul):
    return Tr(jordan(A, B, omul))


def coords_of(X):
    # alpha,beta,gamma,x1,x2,x3 with x3=X[1][0], x2=X[0][2], x1=X[2][1]
    return X[0][0][0], X[1][1][0], X[2][2][0], X[2][1], X[0][2], X[1][0]


# ============================================================================
# 3. M# via the HERMITIAN ADJUGATE (cofactor matrix).  INDEPENDENT construction.
#    For Hermitian 3x3 octonion M with layout above, the Freudenthal adjoint is
#       (M#)_{ii} = product of the OTHER two diagonals - |off-diag opposite|^2
#       (M#) off-diagonal = the 2x2 cofactor (conjugated appropriately).
#    I derive each entry from the standard adjugate of a Hermitian octonion matrix
#    (Freudenthal): with diag (a,b,g) and octonions x1 (entry (3,2)), x2 (0,2), x3 (1,0):
#       (M#)_a = b g - |x1|^2
#       (M#)_b = a g - |x2|^2
#       (M#)_g = a b - |x3|^2
#       (M#)_x1 = conj(x2 x3) - a x1      [the (3,2)-cofactor]
#       (M#)_x2 = conj(x3 x1) - b x2      [wait: derive carefully below]
#       (M#)_x3 = conj(x1 x2) - g x3
#    The conj(x_i x_j) ORDER is the known trap; I resolve it by REQUIRING the two
#    defining identities (M#)# = det3(M) M and Tr(M#)=sigma2(M), testing BOTH order
#    choices and keeping the one that satisfies them (then it is forced).
# ============================================================================
def sigma2(M, omul):
    return (Tr(M)**2 - Tr(jordan(M, M, omul))) / 2


def det3(M, omul):
    a, b, g, x1, x2, x3 = coords_of(M)
    n1, n2, n3 = oct_normsq(x1), oct_normsq(x2), oct_normsq(x3)
    # cross term Re((x2 x1) x3) -- I test this order vs alternatives against (M#)#=N M below
    cross = omul(omul(x2, x1), x3)
    return a*b*g - a*n1 - b*n2 - g*n3 + 2*cross[0]


def sharp_adjugate(M, omul, order):
    """M# via cofactors. `order` selects the off-diagonal octonion factor order;
    we determine the correct one by the defining identities (no peeking at the repo)."""
    a, b, g, x1, x2, x3 = coords_of(M)
    da = b*g - oct_normsq(x1)
    db = a*g - oct_normsq(x2)
    dg = a*b - oct_normsq(x3)
    if order == "A":
        # (M#)_{x_i} = conj(x_{i+1} x_{i+2}) - (opposite diag) x_i, cyclic
        s1 = [c for c in oct_conj(omul(x2, x3))]   # for x1
        s2 = [c for c in oct_conj(omul(x3, x1))]   # for x2
        s3 = [c for c in oct_conj(omul(x1, x2))]   # for x3
    else:  # "B": reversed octonion order
        s1 = [c for c in oct_conj(omul(x3, x2))]
        s2 = [c for c in oct_conj(omul(x1, x3))]
        s3 = [c for c in oct_conj(omul(x2, x1))]
    nx1 = [s1[k] - (a*x1[k]) for k in range(8)]
    nx2 = [s2[k] - (b*x2[k]) for k in range(8)]
    nx3 = [s3[k] - (g*x3[k]) for k in range(8)]
    return h3o(da, db, dg, nx1, nx2, nx3)


def pick_sharp_order(omul):
    """Determine the cofactor octonion order from (M#)#=N(M) M and Tr(M#)=sigma2(M)."""
    # generic rational test element with genuine octonion content
    xa = [R(1, 2), R(1, 3), R(-1, 5), R(2, 7), R(1, 11), R(-3, 4), R(1, 6), R(5, 8)]
    xb = [R(-1, 4), R(2, 9), R(1, 7), R(-1, 3), R(3, 5), R(1, 2), R(-2, 5), R(1, 9)]
    xc = [R(1, 8), R(-1, 6), R(3, 7), R(1, 5), R(-1, 2), R(2, 11), R(1, 4), R(-3, 8)]
    M = h3o(R(3, 2), R(-2, 3), R(5, 4), xa, xb, xc)
    N = det3(M, omul)
    good = []
    for order in ("A", "B"):
        Ms = sharp_adjugate(M, omul, order)
        Mss = sharp_adjugate(Ms, omul, order)
        adj_ok = all(cancel(Mss[i][j][k] - N*M[i][j][k]) == 0
                     for i in range(3) for j in range(3) for k in range(8))
        tr_ok = (cancel(Tr(Ms) - sigma2(M, omul)) == 0)
        if adj_ok and tr_ok:
            good.append(order)
    return good


# ============================================================================
# 4. compression + family geometry (rebuilt from scratch)
# ============================================================================
def pyth(t):
    den = 1 + t**2
    return (1 - t**2)/den, 2*t/den


def cmul_k(a, b, k):
    r = Z8()
    r[0] = a[0]*b[0] - a[k]*b[k]
    r[k] = a[0]*b[k] + a[k]*b[0]
    return r


def herm_from_vec(v):
    p = [[Z8() for _ in range(3)] for _ in range(3)]
    k_used = None
    for vi in v:
        for kk in range(1, 8):
            if vi[kk] != 0:
                k_used = kk
    if k_used is None:
        k_used = 7
    for i in range(3):
        for j in range(3):
            p[i][j] = cmul_k(v[i], oct_conj(v[j]), k_used)
    return p


def family(t, j, k):
    c, s = pyth(t)
    v = [Z8(), Z8(), Z8()]
    v[0] = [c] + [sp.Integer(0)]*7
    vj = Z8(); vj[k] = s
    v[j] = vj
    return herm_from_vec(v)


def E_ii(i):
    d = [R(1) if m == i else R(0) for m in range(3)]
    return h3o(d[0], d[1], d[2], Z8(), Z8(), Z8())


def compress0(p, X, omul):
    LpX = jordan(p, X, omul)
    Lp2X = jordan(p, LpX, omul)
    return matadd(matscal(2, Lp2X), matscal(-3, LpX), X)


def battery16():
    return [(j, k) for j in (1, 2) for k in range(8)]


def slot_of(j, k):
    return (19 + k) if j == 1 else (11 + k)


def cut_families():
    return [(j, k) for (j, k) in battery16() if slot_of(j, k) in {11, 18, 19, 26}]


def lap(fp, frame, omul):
    tot = sp.Integer(0)
    for (j, k) in frame:
        p = family(T, j, k)
        tot += R(1, 4) * sp.diff(fp(p), T, 2).subs(T, 0)
    return sp.expand(tot)


def M_full(omul, prefix="w"):
    s = symbols(f"{prefix}0:26", real=True)
    M = h3o(s[0], s[1], -s[0]-s[1], list(s[2:10]), list(s[10:18]), list(s[18:26]))
    return M, s


def _cu(re, e7):
    z = Z8(); z[0] = re; z[7] = e7
    return z


def M_ualigned(omul, prefix="u"):
    s = symbols(f"{prefix}0:8", real=True)
    M = h3o(s[0], s[1], -s[0]-s[1], _cu(s[2], s[3]), _cu(s[4], s[5]), _cu(s[6], s[7]))
    return M, s


def _offu(comps):
    z = Z8()
    for i in range(6):
        z[i+1] = comps[i]
    return z


def M_offu(omul, prefix="h"):
    s = symbols(f"{prefix}0:18", real=True)
    M = h3o(0, 0, 0, _offu(s[0:6]), _offu(s[6:12]), _offu(s[12:18]))
    return M, s


# ============================================================================
# THE PIPELINE (run once per octonion product)
# ============================================================================
def run_pipeline(omul, name, sharp_order):
    print(f"\n{'='*70}\n  PIPELINE with octonion product: {name}\n{'='*70}")

    def sharp(M):
        return sharp_adjugate(M, omul, sharp_order)

    def G_M(M, p):
        return inner(sharp(M), p, omul) - R(1, 4) * inner(M, p, omul)**2

    E11 = E_ii(0); E22 = E_ii(1); E33 = E_ii(2)
    I3 = matscal(R(1, 3), IDENT())

    # --- sharp identity I x M = -M/2 for traceless M (cross x via x B = AoB - ... ; but we test
    #     the CONSEQUENCE directly: (I/3 + eps M)# = I/9 - (eps/3)M + eps^2 M#). The I x M = -M/2
    #     identity is exactly what makes the eps^1 coeff -(1/3)M.) Verify on symbolic traceless M.
    M, s = M_full(omul)
    X = matadd(I3, matscal(EPS, M))
    Xs = sharp(X)
    target = matadd(matscal(R(1, 9), IDENT()), matscal(-EPS/3, M), matscal(EPS**2, sharp(M)))
    sharp_exp_ok = all(cancel(Xs[i][j][k] - target[i][j][k]) == 0
                       for i in range(3) for j in range(3) for k in range(8))
    rep(f"[{name}] X# = I/9 - (eps/3)M + eps^2 M#  (=> I x M = -M/2 for traceless M, sharp identity)",
        sharp_exp_ok)

    # --- (a) B1: m, q, dq=dm/3, dr=0 IDENTICALLY in Q[eps]; B2: d^2 r = (9/4) G_M ---
    a = inner(M, E11, omul); c = inner(sharp(M), E11, omul)
    m = sp.expand(Tr(X) - inner(X, E11, omul))
    q = sp.expand(inner(sharp(X), E11, omul))
    m_ok = cancel(m - (R(2, 3) - EPS*a)) == 0
    q_ok = cancel(q - (R(1, 9) - EPS/3*a + EPS**2*c)) == 0
    # dr=0 as an IDENTITY in Q[eps]: series r to O(eps^3); coeff(eps,1) must be 0 as a polynomial in s
    r = sp.series(q / m**2, EPS, 0, 3).removeO()
    dr1 = sp.expand(cancel(r.coeff(EPS, 1)))
    dr0_identity = (sp.Poly(dr1, *s).total_degree() == 0 and dr1 == 0) if dr1 != 0 else True
    G = cancel(c - a**2/4)
    dr2_ok = cancel(r.coeff(EPS, 2) - R(9, 4)*G) == 0
    rep(f"[{name}] B1: m=2/3-eps a, q=1/9-(eps/3)a+eps^2 c, dr=0 IDENTITY in Q[eps] (poly deg of "
        f"eps^1 coeff -> {0 if dr1==0 else 'NONZERO'})", m_ok and q_ok and dr1 == 0)
    rep(f"[{name}] B2: d^2 r = (9/4) G_M with G_M=<M#,E11>-1/4<M,E11>^2 (symbolic traceless M)", dr2_ok)

    # dr=0 along all 16 families over Q(t) too (every event p)
    fam_dr = True
    for (j, k) in battery16():
        p = family(T, j, k)
        Xp = matadd(I3, matscal(EPS, M))
        mp = Tr(Xp) - inner(Xp, p, omul)
        qp = inner(sharp(Xp), p, omul)
        rp = sp.series(qp/mp**2, EPS, 0, 2).removeO()
        fam_dr &= (cancel(rp.coeff(EPS, 1)) == 0)
    rep(f"[{name}] B1: dr=0 along ALL 16 families over Q(t) (MaxEnt flat at every event p)", fam_dr)

    # --- (b) positivity G_M = -(1/4)(eigengap)^2 <= 0 + anchors ---
    p11 = family(T, 1, 1)
    Cp = compress0(p11, M, omul)
    trCp = Tr(Cp)
    det2 = (Tr(Cp)**2 - Tr(jordan(Cp, Cp, omul)))/2
    struct_ok = (cancel(G_M(M, p11) - (det2 - R(1, 4)*trCp**2)) == 0
                 and cancel(det2 - inner(sharp(M), p11, omul)) == 0)
    Md = h3o(2, -1, -1, Z8(), Z8(), Z8())
    g11 = cancel(G_M(Md, E11)); g22 = cancel(G_M(Md, E22))
    rep(f"[{name}] B2 positivity: G_M == det2(C_pM) - 1/4(Tr C_pM)^2 = -1/4 eigengap^2 (structural <=0)",
        struct_ok)
    rep(f"[{name}] anchors M=diag(2,-1,-1): G(E11)={g11}(==0), G(E22)={g22}(==-9/4); "
        f"<M#,E22>={cancel(inner(sharp(Md),E22,omul))}(==-2)",
        g11 == 0 and g22 == R(-9, 4) and inner(sharp(Md), E22, omul) == -2)
    # positivity battery (rational instances all <= 0)
    batt_ok = True
    Ms = [h3o(3, -1, -2, Z8(), Z8(), Z8()),
          h3o(R(1, 2), R(1, 3), R(-5, 6),
              [R(1, 4) if i == 1 else 0 for i in range(8)],
              [R(1, 5) if i == 7 else 0 for i in range(8)],
              [R(1, 6) if i == 3 else 0 for i in range(8)])]
    for Mi in Ms:
        for p in [E11, E22, E33, family(R(2), 1, 1), family(R(1, 3), 2, 7)]:
            if cancel(G_M(Mi, p)) > 0:
                batt_ok = False
    rep(f"[{name}] B2 positivity battery (10 rational (M,p) instances all G_M<=0)", batt_ok)

    # --- (c) the level-split overdetermined solve on OP^2 and cut ---
    def level_split(Mbuild, frame, lam1, label):
        M2, s2 = Mbuild(omul)
        al, be, l2 = symbols("al be l2")
        aE = inner(M2, E11, omul); cE = inner(sharp(M2), E11, omul)
        tm = Tr(jordan(M2, M2, omul))
        L = lap(lambda p: inner(M2, p, omul)**2, frame, omul)
        R_E = aE**2 - al*cE - be*tm
        rhs = -al*lam1*(cE + tm/6) - l2*R_E
        poly = sp.Poly(sp.expand(L - rhs), *s2)
        eqs = list(set(poly.coeffs()))
        sols = sp.solve(eqs, [al, be, l2], dict=True)
        print(f"      {label}: {len(eqs)} overdetermined eqs in (al,be,l2) -> {sols}")
        return (sols[0] if len(sols) == 1 else None), (al, be, l2), len(eqs)

    sop, (al, be, l2), nop = level_split(M_full, battery16(), 48, "OP^2 (16-frame full M)")
    scut, _, ncut = level_split(M_ualigned, cut_families(), 12, "cut (4-frame u-aligned M)")
    rep(f"[{name}] (c) OP^2 level split UNIQUE+CONSISTENT ({nop} eqs > 3 unknowns) -> "
        f"(1/7,9/182,104); lambda_2(OP^2)=104",
        sop is not None and sop[al] == R(1, 7) and sop[be] == R(9, 182) and sop[l2] == 104)
    rep(f"[{name}] (c) cut level split UNIQUE+CONSISTENT ({ncut} eqs) -> (2/5,3/20,32); "
        f"lambda_2(cut)=32", scut is not None and scut[al] == R(2, 5) and scut[be] == R(3, 20)
        and scut[l2] == 32)

    # --- (d) kappa_0 = 108/13 on OP^2 + the sourced-equation identity at E_11 ---
    for nm, lam1, Mb, sol in [("OP^2", 48, M_full, sop), ("cut", 12, M_ualigned, scut)]:
        alv, bev, l2v = sol[al], sol[be], sol[l2]
        frame = battery16() if nm == "OP^2" else cut_families()
        M3, s3 = Mb(omul)
        aE = inner(M3, E11, omul); cE = inner(sharp(M3), E11, omul)
        tm = Tr(jordan(M3, M3, omul))
        R_E = aE**2 - alv*cE - bev*tm
        kappa0 = cancel(lam1*(R(1, 6) - alv/24 + bev/4))
        lhs = lap(lambda p: G_M(M3, p), frame, omul) + lam1*G_M(M3, E11)
        rhs = -kappa0*tm + R(l2v - lam1, 4)*R_E
        idok = cancel(lhs - rhs) == 0
        dR = lap(lambda p: inner(M3, p, omul)**2 - alv*inner(sharp(M3), p, omul) - bev*tm, frame, omul)
        eigok = cancel(dR - (-l2v*R_E)) == 0
        exp_k = R(108, 13) if nm == "OP^2" else R(9, 4)
        rep(f"[{name}] (d) sourced eq on {nm}: kappa_0={kappa0}(=={exp_k}); identity holds @E11: "
            f"{idok}; R_M is lambda_2={l2v} eigenfunction: {eigok}",
            idok and eigok and kappa0 == exp_k)

    # --- (e) hidden-sector invisibility <M,p>=0 on the cut for off-u M ---
    Mh, sh = M_offu(omul)
    inv = all(cancel(inner(Mh, family(T, j, k), omul)) == 0 for (j, k) in cut_families())
    inv_E = cancel(inner(Mh, E11, omul)) == 0
    src = cancel(inner(sharp(Mh), E11, omul))
    rep(f"[{name}] (e) hidden off-u M: <M,p>=0 on ALL cut p (invisibility); still sources "
        f"<M#,E11>={src}(!=0)", inv and inv_E and src != 0)

    return sop, scut, (al, be, l2)


# ============================================================================
# ADVERSARIAL: is 104 hardwired?  Re-solve OP^2 forcing l2 to be FREE and check it
# comes out 104 WITHOUT being supplied; and verify the system is genuinely
# overdetermined (more eqs than unknowns) AND inconsistent if we perturb the ansatz.
# ============================================================================
def adversarial(omul, sharp_order):
    print(f"\n{'='*70}\n  ADVERSARIAL: 104 not hardwired; overdetermination genuine\n{'='*70}")

    def sharp(M):
        return sharp_adjugate(M, omul, sharp_order)
    E11 = E_ii(0)
    M, s = M_full(omul, "v")
    al, be, l2 = symbols("al be l2")
    aE = inner(M, E11, omul); cE = inner(sharp(M), E11, omul)
    tm = Tr(jordan(M, M, omul))
    L = lap(lambda p: inner(M, p, omul)**2, battery16(), omul)
    R_E = aE**2 - al*cE - be*tm
    rhs = -al*48*(cE + tm/6) - l2*R_E
    poly = sp.Poly(sp.expand(L - rhs), *s)
    eqs = list(set(poly.coeffs()))
    # 1. genuinely overdetermined: #independent eqs > 3 unknowns
    print(f"      #distinct coeff-equations = {len(eqs)} (unknowns = 3) => overdetermined={len(eqs) > 3}")
    sols = sp.solve(eqs, [al, be, l2], dict=True)
    print(f"      unconstrained solve -> {sols}")
    got104 = (len(sols) == 1 and sols[0][l2] == 104)
    rep(f"      104 EMERGES from the unconstrained solve (NOT supplied): {got104}", got104)
    # 2. force a WRONG l2 and confirm the (alpha,beta) system becomes INCONSISTENT
    #    (if it were under-determined / fittable, a wrong l2 would still solve)
    wrong = []
    for l2try in (100, 104, 108):
        eqs2 = [e.subs(l2, l2try) for e in eqs]
        s2 = sp.solve(eqs2, [al, be], dict=True)
        wrong.append((l2try, bool(s2)))
    print(f"      (l2 forced, solve for alpha,beta) consistency: {wrong}")
    only_104 = all((cons == (l2try == 104)) for (l2try, cons) in wrong)
    rep(f"      forcing l2!=104 makes (alpha,beta) INCONSISTENT; only l2=104 consistent "
        f"=> consistency is the CLAIM, not a fit: {only_104}", only_104)


# ============================================================================
# branch smoothness S=f(r) at r=1/4 (independent)
# ============================================================================
def branch_check():
    print(f"\n{'='*70}\n  BRANCH: S=f(r) analytic at r=1/4, f'(1/4)=2 (independent)\n{'='*70}")
    u = symbols("u", nonnegative=True)
    w = sqrt(u)
    lp = (1 + w)/2; lm = (1 - w)/2
    S = -lp*slog(lp) - lm*slog(lm)
    ser = sp.series(S, u, 0, 3).removeO()
    smooth = sp.simplify(ser - (slog(2) - u/2 - u**2/4)) == 0  # check NO odd sqrt(u) powers, analytic
    # actually just confirm expansion has only integer powers of u (=> analytic in u=1-4r):
    has_sqrt = ser.has(w)
    dSdu0 = sp.limit(sp.diff(S, u), u, 0)
    fprime = cancel(-4*dSdu0)
    rep(f"branch S(u): series in u has NO sqrt(u) (analytic): {not has_sqrt}; "
        f"S = log2 - u/2 - u^2/4 + ...: {smooth}; f'(1/4) = -4 dS/du|_0 = {fprime}(==2)",
        (not has_sqrt) and fprime == 2)


# ============================================================================
def main():
    print("#"*70)
    print("# FROM-SCRATCH independent check -- Phase 86 (my own octonions + adjugate M#)")
    print("#"*70)

    _check_my_octonions()
    print("  [ok] my Cayley-Dickson octonions: unital, alternative, norm-multiplicative")

    # cross-check my octonion product reproduces a composition algebra; pick the adjugate
    # order separately for each product (both must be self-consistent via (M#)#=N M).
    my_order = pick_sharp_order(my_oct_mul)
    rl_order = pick_sharp_order(RL.oct_mul)
    print(f"  adjugate octonion-order satisfying (M#)#=N M & Tr(M#)=sigma2: "
          f"mine={my_order}, RL={rl_order}")
    assert my_order and rl_order, "no consistent adjugate order found -- M# construction broken"

    # run the FULL pipeline with BOTH products (each self-consistent)
    run_pipeline(RL.oct_mul, "RL-Fano", rl_order[0])
    run_pipeline(my_oct_mul, "my-CayleyDickson", my_order[0])

    adversarial(RL.oct_mul, rl_order[0])
    branch_check()

    print("\n" + "="*70)
    print(f"  FROM-SCRATCH: {sum(PASS)}/{len(PASS)} PASS")
    print("="*70)
    return all(PASS)


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
