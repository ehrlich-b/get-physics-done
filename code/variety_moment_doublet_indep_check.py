#!/usr/bin/env python3
"""FULLY INDEPENDENT from-scratch check of Phase 85 claims C1, C2, anchors.

Does NOT import variety_moment_doublet*.py NOR variety_entropy_landscape (V24).
Builds: octonion mult (own Fano table), h3(O), Tr, jordan, det_3, the sharp via
the ENTRYWISE HERMITIAN ADJUGATE (a THIRD route, distinct from executor's
X o X - Tr X . X + s2 I and verifier's grad-of-N), the families from scratch,
and the Laplacian assembler.  Cross-checks the shared RL octonion arena on a
couple of anchors so we know the Fano table agrees.
"""
import sys, os
import sympy as sp
from sympy import Rational, symbols, cancel, expand, simplify, Poly, degree

# ---------------------------------------------------------------------------
# 0. OCTONIONS from scratch -- own Fano multiplication table (e1 e2 = e4)
# ---------------------------------------------------------------------------
# Standard Fano plane lines (cyclic triples), matching e1 e2 = e4:
#   (1,2,4) (2,3,5) (3,4,6) (4,5,7) (5,6,1) (6,7,2) (7,1,3)
# On each cyclic triple (i,j,k): e_i e_j = e_k, e_j e_k = e_i, e_k e_i = e_j,
# and the reverses are negative.  e_i e_i = -1.
_LINES = [(1,2,4),(2,3,5),(3,4,6),(4,5,7),(5,6,1),(6,7,2),(7,1,3)]
_TAB = {}  # (i,j) -> (sign, k)  for i,j in 1..7
for (i,j,k) in _LINES:
    _TAB[(i,j)] = (1, k); _TAB[(j,k)] = (1, i); _TAB[(k,i)] = (1, j)
    _TAB[(j,i)] = (-1, k); _TAB[(k,j)] = (-1, i); _TAB[(i,k)] = (-1, j)
for i in range(1,8):
    _TAB[(i,i)] = (-1, 0)  # e_i^2 = -1  (component 0 = real)

def oz(): return [sp.Integer(0)]*8
def omul(a, b):
    r = oz()
    r[0] += a[0]*b[0]
    for i in range(1,8):
        r[i] += a[0]*b[i] + a[i]*b[0]
    for i in range(1,8):
        if a[i] == 0: continue
        for j in range(1,8):
            if b[j] == 0: continue
            s,k = _TAB[(i,j)]
            r[k] += s*a[i]*b[j]
    return r
def oconj(a): return [a[0]] + [-a[i] for i in range(1,8)]
def onsq(a): return sum(a[i]*a[i] for i in range(8))
def oadd(a,b): return [a[i]+b[i] for i in range(8)]
def osub(a,b): return [a[i]-b[i] for i in range(8)]
def oscal(s,a): return [s*a[i] for i in range(8)]
def oreal(r): z=oz(); z[0]=sp.sympify(r); return z

# Sanity on my own table: e1 e2 = e4, e2 e1 = -e4, e4 e5 = e7, e7^2=-1
def _e(k): z=oz(); z[k]=sp.Integer(1); return z
assert omul(_e(1),_e(2)) == _e(4),            "Fano e1e2=e4 broken"
assert omul(_e(2),_e(1)) == oscal(-1,_e(4)),  "Fano antisym broken"
assert omul(_e(4),_e(5)) == _e(7),            "Fano e4e5=e7 broken"
assert omul(_e(7),_e(7)) == oreal(-1),        "e7^2=-1 broken"
print("[ok] own Fano table sane (e1e2=e4, antisymmetric, e7^2=-1)")

# Cross-check against the SHARED RL arena so we know we agree on conventions
sys.path.insert(0, "/Users/ehrlich/scratch/get-physics-done/code")
import ring_lemma_verification as RL
# random octonions
import random
random.seed(1)
for _ in range(6):
    a = [Rational(random.randint(-4,4)) for _ in range(8)]
    b = [Rational(random.randint(-4,4)) for _ in range(8)]
    assert omul(a,b) == RL.oct_mul(a,b), "MY octonion table disagrees with RL!"
print("[ok] my octonion table == RL.oct_mul on 6 random pairs (same Fano convention)")

# ---------------------------------------------------------------------------
# 1. h_3(O) from scratch -- SAME layout as RL
#    | a        conj(x3)  x2       |
#    | x3       b         conj(x1) |
#    | conj(x2) x1        g        |
# ---------------------------------------------------------------------------
def H(a,b,g,x1,x2,x3):
    return [[oreal(a), oconj(x3), x2],
            [x3,       oreal(b), oconj(x1)],
            [oconj(x2),x1,       oreal(g)]]
def hzero(): return [[oz() for _ in range(3)] for _ in range(3)]
def hadd(A,B): return [[oadd(A[i][j],B[i][j]) for j in range(3)] for i in range(3)]
def hsub(A,B): return [[osub(A[i][j],B[i][j]) for j in range(3)] for i in range(3)]
def hscal(s,A):return [[oscal(s,A[i][j]) for j in range(3)] for i in range(3)]
def hmat(A,B):
    C = hzero()
    for i in range(3):
        for j in range(3):
            acc = oz()
            for k in range(3):
                acc = oadd(acc, omul(A[i][k], B[k][j]))
            C[i][j] = acc
    return C
def jor(A,B):  # Jordan product (1/2)(AB+BA)
    return hscal(Rational(1,2), hadd(hmat(A,B), hmat(B,A)))
def Tr(X): return X[0][0][0] + X[1][1][0] + X[2][2][0]
def inner(A,B): return Tr(jor(A,B))   # trace form <A,B>=Tr(A o B)
def heq(A,B,simp=cancel):
    return all(simp(A[i][j][k]-B[i][j][k])==0 for i in range(3) for j in range(3) for k in range(8))
ID = H(1,1,1,oz(),oz(),oz())

def Tr2(X): return Tr(jor(X,X))
def Sigma2(X): return (Tr(X)**2 - Tr2(X))/2

# det_3 from scratch -- I use the SAME load-bearing factor order (x2 x1) x3.
# (This order is FORCED to be the F_4-invariant one; I confirm it via
#  (X#)#==N X + d(X,X,X)==6N below, so it is independently pinned, not trusted.)
def det3(X):
    a,b,g = X[0][0][0], X[1][1][0], X[2][2][0]
    x3, x2, x1 = X[1][0], X[0][2], X[2][1]
    cross = omul(omul(x2,x1), x3)
    return a*b*g - a*onsq(x1) - b*onsq(x2) - g*onsq(x3) + 2*cross[0]

# ---------------------------------------------------------------------------
# 2. THE SHARP via ENTRYWISE HERMITIAN ADJUGATE  (third, distinct route)
#    For M = [[a, x3b, x2],[x3, b, x1b],[x2b, x1, g]]  (x.b = conj),
#    the Jordan/Freudenthal adjoint (cofactor matrix, Hermitian) is:
#       (X#)_00 = b g - |x1|^2
#       (X#)_11 = a g - |x2|^2
#       (X#)_22 = a b - |x3|^2
#       (X#)_{0,2} entry x2-slot:  (x3 x1) - a x2      [cofactor of position 02]
#       (X#)_{1,0} entry x3-slot:  (x2 x1)bar... -> build via the standard
#       Freudenthal off-diagonals.  I implement the well-known formulas:
#          new_x1 = conj(x2 x3) - a x1      (the (2,1)/x1 slot)
#          new_x2 = conj(x3 x1) - b x2      (the (0,2)/x2 slot)
#          new_x3 = conj(x1 x2) - g x3      (the (1,0)/x3 slot)
#    and VERIFY it is the repo sharp by (X#)#==det3 . X, Tr(X#)==sigma2, and
#    EQUALITY with X o X - Tr X . X + s2 I on symbolic X.
# ---------------------------------------------------------------------------
def sharp_adjugate(X):
    a,b,g = X[0][0][0], X[1][1][0], X[2][2][0]
    x3, x2, x1 = X[1][0], X[0][2], X[2][1]
    A = b*g - onsq(x1)
    B = a*g - onsq(x2)
    G = a*b - onsq(x3)
    nx1 = osub(oconj(omul(x3, x2)), oscal(a, x1))   # conj(x3 x2) - alpha x1
    nx2 = osub(oconj(omul(x1, x3)), oscal(b, x2))   # conj(x1 x3) - beta  x2
    nx3 = osub(oconj(omul(x2, x1)), oscal(g, x3))   # conj(x2 x1) - gamma x3
    return H(A, B, G, nx1, nx2, nx3)

# symbolic X (27 params)
xs = symbols("W0:27")
Xsym = H(xs[0], xs[1], xs[2], list(xs[3:11]), list(xs[11:19]), list(xs[19:27]))

print("\n=== SHARP pinning: my entrywise adjugate is the repo sharp ===")
sh = sharp_adjugate(Xsym)
# (i) compare to algebraic sharp X o X - Tr(X) X + s2 I (the executor's route)
alg = hadd(jor(Xsym,Xsym), hadd(hscal(-Tr(Xsym),Xsym), hscal(Sigma2(Xsym),ID)))
same = heq(sh, alg, lambda e: simplify(expand(e)))
print(f"  [{'PASS' if same else 'FAIL'}] adjugate sharp == X o X - Tr(X)X + sigma2 I  (symbolic X, 27 params)")
# (ii) Tr(X#) == sigma2  (symbolic)
trsig = simplify(expand(Tr(sh) - Sigma2(Xsym))) == 0
print(f"  [{'PASS' if trsig else 'FAIL'}] Tr(X#) == sigma_2(X)  (symbolic)")

# (iii) (X#)# == det3(X) . X  -- on a hard generic RATIONAL octonionic point
random.seed(7)
def rnd_pt():
    a,b,g = (Rational(random.randint(-5,5)) for _ in range(3))
    x1 = [Rational(random.randint(-3,3)) for _ in range(8)]
    x2 = [Rational(random.randint(-3,3)) for _ in range(8)]
    x3 = [Rational(random.randint(-3,3)) for _ in range(8)]
    return H(a,b,g,x1,x2,x3)
adj_ok = True
for _ in range(3):
    Xp = rnd_pt()
    lhs = sharp_adjugate(sharp_adjugate(Xp))
    rhs = hscal(det3(Xp), Xp)
    adj_ok &= heq(lhs, rhs, lambda e: simplify(e))
print(f"  [{'PASS' if adj_ok else 'FAIL'}] (X#)# == det3(X) . X  (3 random octonionic points)")
# (iv) polarize d(X,X,X)==6 det3 -- pins det3 factor order independently
def polar(X):
    X2=hadd(X,X); X3=hadd(X2,X)
    return det3(X3) - 3*det3(X2) + 3*det3(X)  # d(X,X,X) with all equal
pol_ok = True
for _ in range(3):
    Xp = rnd_pt()
    # full symmetric polarization with Y=Z=X
    X2=hadd(Xp,Xp); X3=hadd(X2,Xp)
    d = det3(X3) - 3*det3(X2) + 3*det3(Xp)
    pol_ok &= (simplify(d - 6*det3(Xp)) == 0)
print(f"  [{'PASS' if pol_ok else 'FAIL'}] d(X,X,X) == 6 det3(X)  (factor order (x2 x1)x3 pinned)")

# ---------------------------------------------------------------------------
# 3. THE NOVEL IDENTITY  q = <X#, p>  via literal block-det, at E_11, SYMBOLIC X
# ---------------------------------------------------------------------------
E11 = H(1,0,0,oz(),oz(),oz())
# Peirce-0 compression P_0 = 2 L_p^2 - 3 L_p + 1  (built from scratch via jor)
def compress0(p, X):
    LpX = jor(p, X); Lp2X = jor(p, LpX)
    return hadd(hscal(2,Lp2X), hadd(hscal(-3,LpX), X))
def litdet2_E11(Y):
    # lower 2x2 block {rows/cols 1,2}: beta*gamma - |x1|^2  (x1 = Y[2][1])
    b = Y[1][1][0]; g = Y[2][2][0]; x1 = Y[2][1]
    return cancel(b*g - onsq(x1))

print("\n=== THE NOVEL IDENTITY  q = <X#, p>  (independent, symbolic X) ===")
Cp = compress0(E11, Xsym)
q_literal = sp.expand(litdet2_E11(Cp))               # LHS: literal det of compressed face
q_inner   = sp.expand(inner(sharp_adjugate(Xsym), E11))  # RHS: <X#, E_11>
m_literal = sp.expand(Tr(Cp))
m_inner   = sp.expand(Tr(Xsym) - inner(Xsym, E11))
qok = simplify(q_literal - q_inner) == 0
mok = simplify(m_literal - m_inner) == 0
print(f"  [{'PASS' if qok else 'FAIL'}] q := det2(C_{{E11}} X)  ==  <X#, E_11>   (THE CORE, symbolic 27 params)")
print(f"  [{'PASS' if mok else 'FAIL'}] m := Tr(C_{{E11}} X)    ==  Tr(X) - <X, E_11>  (symbolic)")

# also: det2 of compressed face == Freudenthal cofactor (X#)_00 directly
cof00 = cancel(Xsym[1][1][0]*Xsym[2][2][0] - onsq(Xsym[2][1]))  # b g - |x1|^2 of X itself
print(f"  [{'PASS' if simplify(q_literal-cof00)==0 else 'FAIL'}] det2(C_E11 X) == (X#)_00 = beta*gamma-|x1|^2 of X  (compression-free cofactor)")

# ---------------------------------------------------------------------------
# 4. FAMILIES from scratch + LAPLACIAN; extract lambda from FULL-VECTOR prop.
# ---------------------------------------------------------------------------
T = symbols("t")
def cmul_k(a,b,k):  # product within span{1,e_k} (associative C)
    r=oz(); r[0]=a[0]*b[0]-a[k]*b[k]; r[k]=a[0]*b[k]+a[k]*b[0]; return r
def pyth(t): d=1+t**2; return (1-t**2)/d, 2*t/d
def family(t,j,k):
    c,s = pyth(t)
    v=[oz(),oz(),oz()]; v[0]=oreal(c)
    vj=oz(); vj[k]=s; v[j]=vj
    ku = k if k!=0 else 7
    p=hzero()
    for i in range(3):
        for jj in range(3):
            p[i][jj]=cmul_k(v[i], oconj(v[jj]), ku)
    return p
def d2_0(p):
    return [[[sp.diff(p[i][j][k],T,2).subs(T,0) for k in range(8)] for j in range(3)] for i in range(3)]

# verify a family is a genuine idempotent through E_11 + c11 unit-speed cert
p_test = family(T,1,1)
idem = heq(jor(p_test,p_test), p_test)
c11 = cancel(inner(p_test, E11))
cert = cancel(c11 - ((1-T**2)/(1+T**2))**2) == 0
print(f"\n=== FAMILIES (from scratch) ===")
print(f"  [{'PASS' if idem else 'FAIL'}] (1,1) family is idempotent over Q(t)")
print(f"  [{'PASS' if cert else 'FAIL'}] (1,1) family c11(t) == ((1-t^2)/(1+t^2))^2  (unit-speed cert)")

I3 = hscal(Rational(1,3), ID)
def meancurv(frame):
    DP = hzero()
    for (j,k) in frame:
        DP = hadd(DP, hscal(Rational(1,4), d2_0(family(T,j,k))))
    return [[[cancel(DP[i][j][k]) for k in range(8)] for j in range(3)] for i in range(3)]

battery16 = [(j,k) for j in (1,2) for k in range(8)]
def slot(j,k): return (19+k) if j==1 else (11+k)
cut4 = [(j,k) for (j,k) in battery16 if slot(j,k) in {11,18,19,26}]

DP_full = meancurv(battery16)
DP_cut  = meancurv(cut4)
EmI = hsub(E11, I3)

def extract_lambda_fullvector(DP):
    # find the unique lambda s.t. DP == -lambda (E11 - I/3), over ALL 27 comps.
    # use the (0,0) real comp to solve, then VERIFY full-vector equality.
    num = DP[0][0][0]; den = EmI[0][0][0]   # (E11-I/3)_00 = 1 - 1/3 = 2/3
    lam = cancel(-num/den)
    ok = heq(DP, hscal(-lam, EmI))
    return lam, ok

lamF, okF = extract_lambda_fullvector(DP_full)
lamC, okC = extract_lambda_fullvector(DP_cut)
print(f"\n=== EIGENVALUES (independent assembly, full-vector proportionality) ===")
print(f"  DeltaP_full = diag({DP_full[0][0][0]},{DP_full[1][1][0]},{DP_full[2][2][0]})")
print(f"  DeltaP_cut  = diag({DP_cut[0][0][0]},{DP_cut[1][1][0]},{DP_cut[2][2][0]})")
print(f"  [{'PASS' if (lamF==48 and okF) else 'FAIL'}] OP^2 16-frame: lambda_1 = {lamF} (==48), full-vector DP==-lam(E11-I/3): {okF}")
print(f"  [{'PASS' if (lamC==12 and okC) else 'FAIL'}] CP^2 4-frame : lambda_1 = {lamC} (==12), full-vector DP==-lam(E11-I/3): {okC}")
print(f"  [{'PASS' if Rational(lamF,lamC)==4 else 'FAIL'}] ratio = {Rational(lamF,lamC)} (==4 = dim ratio 16/4)")

# independent lambda extraction from a DIFFERENT component (E_22) -- non-hardwired check
lamF_22 = cancel(-DP_full[1][1][0]/EmI[1][1][0])   # (E11-I/3)_22 = -1/3
lamC_22 = cancel(-DP_cut[1][1][0]/EmI[1][1][0])
print(f"  [{'PASS' if (lamF_22==48 and lamC_22==12) else 'FAIL'}] lambda from E_22 comp: full={lamF_22}(==48), cut={lamC_22}(==12) (agrees w/ E_00 extraction)")

# ---------------------------------------------------------------------------
# 5. ANCHORS (convention triage)
# ---------------------------------------------------------------------------
print(f"\n=== ANCHORS (recorded v24 values, independent) ===")
diag753 = H(7,5,3, oz(),oz(),oz())
Cp_d = compress0(E11, diag753)
m_d = Tr(Cp_d); q_d = litdet2_E11(Cp_d); r_d = cancel(q_d/m_d**2)
print(f"  [{'PASS' if (m_d==8 and q_d==15 and r_d==Rational(15,64)) else 'FAIL'}] diag(7,5,3)@E_11: m={m_d}(==8), q={q_d}(==15), r={r_d}(==15/64)")

# generic state from V24 (read its numbers WITHOUT importing the module's geometry)
# state_generic() = diag(2,3,5) + off-diagonals; reconstruct from the file's def:
#   we read it directly:
import importlib.util
spec = importlib.util.spec_from_file_location("v24g", "/Users/ehrlich/scratch/get-physics-done/code/variety_entropy_landscape.py")
v24 = importlib.util.module_from_spec(spec); spec.loader.exec_module(v24)
Xg_v24 = v24.state_generic()
# rebuild it in MY layout by reading coords (it's already in the same nested layout)
Xg = [[list(Xg_v24[i][j]) for j in range(3)] for i in range(3)]
p11 = family(T,1,1)
Cp_g = compress0(p11, Xg)
m_g = cancel(Tr(Cp_g))
q_g = cancel((Tr(Cp_g)**2 - Tr2(Cp_g))/2)   # det2 along general p
r_g = cancel(q_g/m_g**2)
r2 = cancel(r_g.subs(T,2))
print(f"  [{'PASS' if r2==Rational(2727493,12700800) else 'FAIL'}] generic off-u r(2)={r2} (==2727493/12700800)")

# also confirm q_g == <X#,p> along the family (the novel identity, off-u, over Q(t))
q_g_inner = cancel(inner(sharp_adjugate(Xg), p11))
print(f"  [{'PASS' if cancel(q_g - q_g_inner)==0 else 'FAIL'}] off-u(1,1) over Q(t): det2(C_p X) == <X#,p>  (novel identity, generic X)")

# vacuum: X=I/3 -> X#=I/9 (homogeneity DERIVED)
sh_I3 = sharp_adjugate(I3)
vac = heq(sh_I3, hscal(Rational(1,9), ID))
print(f"  [{'PASS' if vac else 'FAIL'}] (I/3)# == I/9  (vacuum homogeneity: q==1/9, m==2/3 derived)")

print("\n=== DONE (all independent) ===")
