#!/usr/bin/env python3
"""From-scratch independent check of Phase 87 (v27.0). Imports NEITHER v27 driver.
Uses ONLY the certified RL octonion arena (the one octonion algebra) + my OWN
pi_1/2, M#, |.|^2, and the certificate hunt. Goal: try HARD to break LIVE."""
import os, sys, itertools, random
sys.path.insert(0, "/Users/ehrlich/scratch/get-physics-done/code")
import sympy as sp
from sympy import Rational, symbols, cancel, expand, eye, Matrix, sqrt
import ring_lemma_verification as RL

R0 = Rational(0)
def zoct(): return [R0]*8
def oct1(k,v): z=zoct(); z[k]=sp.sympify(v); return z

# ---- my own h3o helpers, built directly on RL.oct_* primitives ----
def hm(al,be,ga,x1,x2,x3): return RL.h3o_from_coords(al,be,ga,x1,x2,x3)
def add(A,B): return RL.octmat_add(A,B)
def sub(A,B): return RL.octmat_sub(A,B)
def scal(s,A): return RL.octmat_scal(s,A)
def Tr(X): return RL.Tr(X)
def jo(A,B): return RL.jordan(A,B)
def inner(A,B): return RL.Tr(RL.jordan(A,B))          # trace form <A,B>=Tr(AoB)
IDENT = RL.h3o_identity()
E11 = hm(1,0,0,zoct(),zoct(),zoct())

# ---- my OWN sharp: via cofactor/adjugate definition X# s.t. (X#)#=N(X)X is downstream.
# Use the Cayley-Hamilton route X# = X o X - Tr(X) X + sigma2(X) I  -- but to be DIFFERENT
# from BOTH drivers, ALSO build a literal-cofactor sharp and demand they agree.
def sigma2(X): return (Tr(X)**2 - Tr(jo(X,X)))/2
def sharp_CH(X):
    return add(sub(jo(X,X), scal(Tr(X),X)), scal(sigma2(X), IDENT))

def sharp_cofactor(X):
    """Literal 3x3 octonionic cofactor (adjugate) of a Hermitian matrix.
    For h_3(O): (X#)_ii = X_jj*X_kk - |X_jk|^2 (real); off-diag entries are
    conj(X_ij*X_jk) - X_ik*X_kk style cofactors. Build directly from coords."""
    a,b,g,x1,x2,x3 = RL._coord_from_octmat(X)
    # diagonal cofactors
    A11 = b*g - RL._oct_normsq(x1)
    A22 = a*g - RL._oct_normsq(x2)
    A33 = a*b - RL._oct_normsq(x3)
    om = RL.oct_mul; oc = RL.oct_conj; osub=RL.oct_sub; oscal=RL.oct_scal
    # Freudenthal adjoint off-diagonal (standard h_3(O) formula):
    #   (X#) entry for (1,2)-slot x3#: x3# = conj(x1*x2) - g*x3    ... need correct slots.
    # Layout: x1=X[2][1], x2=X[0][2], x3=X[1][0].
    # Freudenthal cross (see Jacobson/Springer): with x1,x2,x3 the off-diag octonions,
    #   x1^# = conj(x2 * x3) - a*x1   (the entry NOT touching index 1=alpha row... )
    # We'll DERIVE the correct ones by matching to sharp_CH on a symbolic instance below;
    # but to keep this an INDEPENDENT construction, use the textbook Freudenthal formulas:
    x1s = osub(oc(om(x2,x3)), oscal(a,x1))   # x1# = conj(x2 x3) - alpha x1
    x2s = osub(oc(om(x3,x1)), oscal(b,x2))   # x2# = conj(x3 x1) - beta  x2
    x3s = osub(oc(om(x1,x2)), oscal(g,x3))   # x3# = conj(x1 x2) - gamma x3
    return hm(A11,A22,A33,x1s,x2s,x3s)

# ---- my OWN pi_1/2 at E_11: THREE independent ways ----
def pi_entry(Y):
    """Way 1: keep (0,1),(1,0),(0,2),(2,0) entries (the row-1 off-diag block)."""
    out = RL.octmat_zero()
    out[0][1]=list(Y[0][1]); out[1][0]=list(Y[1][0])
    out[0][2]=list(Y[0][2]); out[2][0]=list(Y[2][0])
    return out

def Lp_matrix(p):
    return RL.jordan_L_matrix(p, RL._standard_basis_27())
def flat(X): return Matrix(RL._flat27(X))
def unflat(v):
    B=RL._standard_basis_27(); out=RL.octmat_zero()
    for a in range(27): out=RL.octmat_add(out, RL.octmat_scal(v[a],B[a]))
    return out
_L11 = Lp_matrix(E11)
_PHALF_eig = 4*_L11*(eye(27)-_L11)              # Way 2: 4 L(I-L)
_PHALF_lag = (_L11-Rational(1,2)*eye(27))*(_L11-R0*eye(27))/Rational(1,2)  # placeholder
# Way 3: Lagrange projector onto eigenvalue 1/2: P_{1/2}=(L-0)(L-1)/((1/2-0)(1/2-1))
_PHALF_lag = (_L11)*(_L11-eye(27))/Rational(-1,4)
def pi_eig(Y):  return unflat([cancel(x) for x in (_PHALF_eig*flat(Y))])
def pi_lag(Y):  return unflat([cancel(x) for x in (_PHALF_lag*flat(Y))])

def normsq(Y): return cancel(Tr(jo(Y,Y)))
def el_eq(A,B):
    D=sub(A,B); return all(cancel(D[i][j][k])==0 for i in range(3) for j in range(3) for k in range(8))

print("="*70); print("STEP 0: sharp constructions agree (CH vs literal Freudenthal cofactor)")
# symbolic-ish: a random rational h3o
random.seed(1)
def randoct(): return [Rational(random.randint(-3,3),random.randint(1,4)) for _ in range(8)]
Xr = hm(Rational(1,2),Rational(-1,3),Rational(5,7),randoct(),randoct(),randoct())
print("  sharp_CH == sharp_cofactor on random rational X:", el_eq(sharp_CH(Xr), sharp_cofactor(Xr)))
# also check (X#)# = N(X) X for BOTH
chk1 = el_eq(sharp_CH(sharp_CH(Xr)), scal(RL.det_3(Xr),Xr))
chk2 = el_eq(sharp_cofactor(sharp_cofactor(Xr)), scal(RL.det_3(Xr),Xr))
print("  (X#)#==N X for CH:", chk1, " for cofactor:", chk2)

print("="*70); print("STEP 1: the three pi_1/2 agree on symbolic Y")
zz=symbols("z0:27", real=True)
Ysym = hm(zz[0],zz[1],zz[2], list(zz[3:11]), list(zz[11:19]), list(zz[19:27]))
p1=pi_entry(Ysym); p2=pi_eig(Ysym); p3=pi_lag(Ysym)
print("  pi_entry==pi_eig:", el_eq(p1,p2), " pi_entry==pi_lag:", el_eq(p1,p3))

print("="*70); print("STEP 2: |pi_1/2(R)|^2 = 2 c_R(1-c_R) for a BATTERY of rank-1 idempotents R")
# rebuild rank-1 idempotents myself: R = v v^dagger style. A rank-1 idempotent in h3(O)
# is herm_from_vec of a UNIT octonion-triple in the spin-factor sense. Use the family
# rotations + GENERIC rank-1 idempotents via projector p with p o p = p, Tr p =1.
def is_idem(R): return el_eq(jo(R,R),R) and cancel(Tr(R))==1
def test_R(R, label):
    cR = cancel(inner(R,E11))
    lhs = normsq(pi_entry(R))
    rhs = cancel(2*cR*(1-cR))
    ok = cancel(lhs-rhs)==0 and is_idem(R)
    print(f"    [{('OK ' if ok else 'XXX')}] {label}: c_R={cR}, |pi(R)|^2={lhs}, 2c_R(1-c_R)={rhs}")
    return ok
allR=True
t=symbols("t")
# (a) the real (1,0)-family idempotent (the anchor's R)
c=(1-t**2)/(1+t**2); s=2*t/(1+t**2)
Ra = hm(c**2, s**2, 0, zoct(), zoct(), oct1(0, c*s))
allR &= test_R(Ra, "real (1,0)-family R(t) [Q(t)]")
# (b) an e7-family idempotent
Rb = hm(c**2, s**2, 0, zoct(), zoct(), oct1(7, c*s))
allR &= test_R(Rb, "e7 (1,0)-family R(t) [Q(t)]")
# (c) a fully generic rank-1 idempotent built from a unit spin-vector (rational)
# Build p = projector onto a generic direction via the family applied twice / explicit.
# Use rank-1 idempotents of the form R = u u^T with u a unit-norm Jordan 'vector':
# easiest certified route: take R = g . E11 for an explicit F4-ish rotation we can rebuild.
# Instead: directly solve a rational rank-1 idempotent. Pick diag-ish:
for (al, x3k, x3v) in [(Rational(1,4),0,None),(Rational(9,25),7,None)]:
    aa=al; bb=1-al; off=sp.sqrt(aa*bb)
    # only rational when aa*bb is a perfect square; 9/25*16/25 -> off=12/25 rational
for cfg in [(Rational(9,25),Rational(16,25),Rational(12,25),0),
            (Rational(9,25),Rational(16,25),Rational(12,25),7),
            (Rational(1,2),Rational(1,2),Rational(1,2),3)]:
    aa,bb,offv,kk = cfg
    Rc = hm(aa,bb,0, zoct(), zoct(), oct1(kk, offv))
    allR &= test_R(Rc, f"generic rational rank-1 R (diag {aa},{bb}, off e{kk}={offv})")
# (d) a rank-1 idempotent with TWO off-diagonal entries populated (genuinely off the cut)
# p with support in both x2 and x3: need p o p = p. Construct via normalized vector
# in the 10-dim spin factor of (alpha,beta,gamma; x1,x2,x3) is hard; use g.E11 route:
# rotate E11 by composing two family rotations (real (1,0) then real (2,0)) numerically-exact.
print("="*70); print("STEP 3: the dG formula via the SECOND path (d/dt G_M along families == <dG,pdot>)")
import variety_entropy_landscape as V24   # ONLY for family geometry (the arena)
def G_M(M,p): return inner(sharp_CH(M),p) - Rational(1,4)*inner(M,p)**2
def dG(M):
    a=inner(M,E11)
    return pi_entry(sub(sharp_CH(M), scal(a*Rational(1,2),M)))
Mt = V24.state_generic()
Mt = sub(Mt, scal(Rational(1,3)*Tr(Mt), IDENT))   # traceless
pathok=True
for (j,k) in [(1,0),(1,1),(1,3),(1,7),(2,0),(2,5),(2,7)]:
    p=V24.family(t,j,k)
    GM = inner(sharp_CH(Mt),p) - Rational(1,4)*inner(Mt,p)**2
    ddt = sp.diff(GM,t).subs(t,0)
    pdot=[[[sp.diff(p[i][jj][kk],t).subs(t,0) for kk in range(8)] for jj in range(3)] for i in range(3)]
    pair = inner(dG(Mt), pdot)
    ok = cancel(ddt-pair)==0
    pathok &= ok
    print(f"    [{('OK ' if ok else 'XXX')}] family ({j},{k}): d/dt G = <dG,pdot>")
print("  SECOND-PATH dG formula holds on all families:", pathok)

print("="*70); print("STEP 4: Q_M tuple-determined on FULL-26 (MY sharp_CH + MY pi_entry)")
ss=symbols("u0:26", real=True)
M = hm(ss[0],ss[1],-ss[0]-ss[1], list(ss[2:10]), list(ss[10:18]), list(ss[18:26]))
a=inner(M,E11); cc=inner(sharp_CH(M),E11); T2=normsq(M); dM=RL.det_3(M)
QM = expand(normsq(dG(M)))
A,B,C,D,E,F,G=symbols("A B C D E F G")
ansatz=A*T2**2+B*cc**2+C*a*dM+D*a**2*T2+E*a**4+F*a**2*cc+G*cc*T2
poly=sp.Poly(expand(QM-ansatz),*ss)
sol=sp.solve(list(set(poly.coeffs())),[A,B,C,D,E,F,G],dict=True)
exact = bool(sol) and expand((QM-ansatz).subs(sol[0]))==0
print("  tuple-fit EXACT (identically zero residual):", exact)
print("  coeffs:", sol[0] if sol else None)
# factored law
fac = cancel((Rational(1,2)*T2 - a**2 + cc)*(a**2-4*cc))
print("  2 Q_M == (1/2 TrM^2 - a^2 + c)(a^2-4c):", cancel(2*QM-fac)==0)
print("  expected coeffs {A:0,B:-2,C:0,D:1/4,E:-1/2,F:5/2,G:-1}:",
      sol and sol[0]=={A:R0,B:Rational(-2),C:R0,D:Rational(1,4),E:Rational(-1,2),F:Rational(5,2),G:Rational(-1)})

print("="*70); print("STEP 5: ADVERSARIAL CERTIFICATE HUNT (try HARD to find same-tuple, diff Q_M)")
def tup(M): return (inner(M,E11), inner(sharp_CH(M),E11), normsq(M), RL.det_3(M))
def QMval(M): return normsq(dG(M))
hits=0; pairs_checked=0; cert=None
# Strategy A: brute random matched-tuple search. Generate many random traceless M,
# bucket by tuple, compare Q_M within buckets.
random.seed(7)
buckets={}
def rrat(lo=-3,hi=3,dmax=5): return Rational(random.randint(lo,hi),random.randint(1,dmax))
N=4000
for _ in range(N):
    d0=rrat(); d1=rrat()
    # random sparse octonion entries (1-2 nonzero comps each) to raise collision odds
    def re():
        z=zoct()
        for _ in range(random.randint(0,2)):
            z[random.randint(0,7)] += rrat(-2,2,3)
        return z
    M=hm(d0,d1,-d0-d1, re(), re(), re())
    key=tup(M)
    q=QMval(M)
    if key in buckets:
        for (Mo,qo) in buckets[key]:
            pairs_checked+=1
            if cancel(q-qo)!=0:
                cert=(Mo,M,key,qo,q); hits+=1
        buckets[key].append((M,q))
    else:
        buckets[key]=[(M,q)]
print(f"  Strategy A (random brute): {N} matrices, {pairs_checked} same-tuple pairs compared, "
      f"{hits} certificate(s).")
if cert: print("  *** CERTIFICATE:", cert[2], " Q diff", cert[3], "vs", cert[4])

# Strategy B: targeted — fix the ANCHOR tuple (1,0,4,1) and build genuinely different M with it.
# M0 = diag(1,0,-1)+x3=e0. Want OTHER traceless M with a=1,c=0,TrM^2=4,detM=1 but in
# different octonion directions / different entry support, NOT stabilizer images.
print("  Strategy B (targeted on anchor tuple (1,0,4,1)):")
def show(M,label):
    a,c,T2,dM=tup(M); q=QMval(M)
    print(f"     {label}: tuple={(a,c,T2,dM)}  Q_M={q}")
    return (a,c,T2,dM),q
anchor=hm(1,0,-1,zoct(),zoct(),oct1(0,1))
tA,qA=show(anchor,"anchor x3=e0")
candidates=[]
# different single octonion direction in x3
for kk in range(8):
    candidates.append((hm(1,0,-1,zoct(),zoct(),oct1(kk,1)), f"x3=e{kk}"))
# put the entry in x2 instead (different Peirce support: x2 is ALSO J_1/2 at E11)
for kk in range(8):
    candidates.append((hm(1,0,-1,zoct(),oct1(kk,1),zoct()), f"x2=e{kk}"))
# put the entry in x1 (the J_0 block — NOT in J_1/2 at E11!) — tuple may match, dG differs
for kk in range(8):
    candidates.append((hm(1,0,-1,oct1(kk,1),zoct(),zoct()), f"x1=e{kk} (J0 support!)"))
# mixed: split |off|^2=1 across two comps of x3
candidates.append((hm(1,0,-1,zoct(),zoct(),[Rational(3,5) if i==0 else (Rational(4,5) if i==1 else 0) for i in range(8)]), "x3=(3/5,4/5)"))
# split across x2 AND x3 (both J_1/2): need |x2|^2+|x3|^2 to keep TrM^2 and detM... detM changes!
qset={}
for M,lab in candidates:
    key,q=tup(M),QMval(M)
    if key==tA:
        qset.setdefault(q,[]).append(lab)
print("     among candidates with EXACT anchor tuple (1,0,4,1):")
for q,labs in qset.items():
    print(f"        Q_M={q}: {labs}")
if len(qset)>1:
    print("  *** CERTIFICATE FOUND in Strategy B: distinct Q_M at identical tuple!")
else:
    print("  Strategy B: all anchor-tuple candidates share Q_M =", list(qset.keys()))

# Strategy C: the x1 (J_0) trap — these have the SAME tuple but the off-diagonal sits in
# the J_0 Peirce block, which pi_1/2 KILLS. If such an M lands on the anchor tuple, dG(M)
# could be SMALLER (pi kills x1), a prime DEAD candidate. Check explicitly.
print("  Strategy C (J_0-support trap: does x1=e_k give the anchor tuple?):")
for kk in [0,1,7]:
    Mx1=hm(1,0,-1,oct1(kk,1),zoct(),zoct())
    print(f"     x1=e{kk}: tuple={tup(Mx1)} (anchor is (1,0,4,1)), Q_M={QMval(Mx1)}, dG=0? {el_eq(dG(Mx1),RL.octmat_zero())}")

print("="*70)
print("STEP 6: is the fit an OVER-RICH ansatz fitting noise? Drop a needed alignment invariant.")
# alignment invariant J := <pi_1/2 M, pi_1/2 M#>  (degree 3 in M, NOT in the tuple).
# If LIVE is real, Q_M must NOT secretly depend on J beyond what the tuple fixes.
# Test: is J itself tuple-determined? If NOT, and Q_M genuinely needs J, the fit would FAIL.
# Since the fit is EXACT with only 7 tuple monomials, Q_M does not need J. Confirm J is NOT
# generally tuple-determined (so the exact fit is a real identity, not a coincidence of an
# over-rich basis).
Mg = hm(ss[0],ss[1],-ss[0]-ss[1], list(ss[2:10]), list(ss[10:18]), list(ss[18:26]))
Jalign = expand(inner(pi_entry(Mg), pi_entry(sharp_CH(Mg))))
# fit J to the tuple monomials of degree 3: a*c, a^3, a*T2, detM, ... and any deg-3 combos
a3,c3,T23,dM3=symbols("aa cc TT dd")
mon3=[symbols("A3"),symbols("B3"),symbols("C3"),symbols("D3")]
A3,B3,C3,D3=mon3
ans3=A3*a*cc+B3*a**3+C3*a*T2+D3*dM
poly3=sp.Poly(expand(Jalign-ans3),*ss)
sol3=sp.solve(list(set(poly3.coeffs())),mon3,dict=True)
exact3 = bool(sol3) and expand((Jalign-ans3).subs(sol3[0]))==0
print("  alignment invariant J=<pi M, pi M#> tuple-determined (deg-3 monomials)?", exact3)
print("    -> if FALSE, Q_M's exact 7-monomial fit is a genuine identity (J not needed), not over-rich noise.")

# also: drop ONE needed monomial from the Q_M ansatz and confirm the fit then FAILS (the
# ansatz is not redundant — each used monomial is necessary).
print("  necessity check: drop each USED monomial; fit must then FAIL:")
used = {'B':B,'D':D,'E':E,'F':F,'G':G}   # A,C had coeff 0
for name,var in used.items():
    A2,B2,C2,D2,E2,F2,G2=symbols("A B C D E F G")
    full={A2:T2**2,B2:cc**2,C2:a*dM,D2:a**2*T2,E2:a**4,F2:a**2*cc,G2:cc*T2}
    syms=[A2,B2,C2,D2,E2,F2,G2]
    drop_sym={'A':A2,'B':B2,'C':C2,'D':D2,'E':E2,'F':F2,'G':G2}[name]
    keep=[x for x in syms if x!=drop_sym]
    ans=sum(x*full[x] for x in keep)
    poly=sp.Poly(expand(QM-ans),*ss)
    sol=sp.solve(list(set(poly.coeffs())),keep,dict=True)
    ex = bool(sol) and expand((QM-ans).subs(sol[0]))==0
    print(f"     drop {name}: fit exact? {ex}  (must be False if {name} is necessary)")
print("="*70); print("DONE.")
