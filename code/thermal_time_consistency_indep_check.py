# Re-verify K^(2) and DEAD on the ENGINE'S octonion table (guard #6), but with my OWN
# matrix-log + my OWN solvability logic (independent code path; shared only the oct product).
import sys; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import ring_lemma_verification as RL
import variety_entropy_landscape as V24
import sympy as sp
from sympy import cancel, Rational as R, symbols, series, expand, together, EmptySet, linsolve
EPS=symbols("epsilon"); TT=symbols("t"); PASS=[]
def rep(l,ok): PASS.append(bool(ok)); print(f"  [{'PASS' if ok else 'FAIL'}] {l}"); return ok

# use engine primitives directly
H=RL.h3o_from_coords; ident=RL.h3o_identity
def madd(*Xs):
    out=RL.octmat_zero()
    for X in Xs: out=RL.octmat_add(out,X)
    return out
msub=RL.octmat_sub; mscal=RL.octmat_scal
def jordan(A,B): return RL.jordan(A,B)
Tr=RL.Tr
def inner(A,B): return RL.Tr(RL.jordan(A,B))
def comp(p,X): return V24.compress0(p,X)
def face_id(p): return msub(ident(),p)
def traceless_face(Y,p): return msub(Y, mscal(Tr(Y)*R(1,2),face_id(p)))
def miszero(A): return all(cancel(A[i][j][k])==0 for i in range(3) for j in range(3) for k in range(8))
def meq(A,B): return miszero(msub(A,B))
def msimp(A): return [[[cancel(A[i][j][k]) for k in range(8)] for j in range(3)] for i in range(3)]
E11=V24.family(0,1,0) if False else RL.h3o_from_coords(1,0,0,RL.oct_zero(),RL.oct_zero(),RL.oct_zero())
# E11 as idempotent: actually E_11 = diag(1,0,0)
E11=RL.h3o_from_coords(1,0,0,RL.oct_zero(),RL.oct_zero(),RL.oct_zero())
I3=mscal(R(1,3),ident())
def Mfull():
    s=symbols("w0:26",real=True)
    return H(s[0],s[1],-s[0]-s[1],list(s[2:10]),list(s[10:18]),list(s[18:26])),s

def safe_coeff(expr,n):
    e=cancel(expr)
    if e==0: return sp.Integer(0)
    pe=sp.expand(e)
    if pe.is_polynomial(EPS): return cancel(pe.coeff(EPS,n))
    return cancel(sp.series(e,EPS,0,n+1).removeO().coeff(EPS,n))

def K2_indep(p,M):
    X=madd(I3,mscal(EPS,M)); rho=comp(p,X); mm=Tr(rho)
    det2=cancel((mm**2-Tr(jordan(rho,rho)))/2); r=cancel(together(det2/mm**2)); s2=cancel(R(1,4)-r)
    sum_f=series(-sp.log(R(1,4)-s2),EPS,0,3).removeO()
    S=symbols("S",positive=True)
    g=series(-(1/(2*S))*sp.log((R(1,2)+S)/(R(1,2)-S)),S,0,3).removeO()
    b=series(expand(g.subs(S**2,s2)),EPS,0,3).removeO()
    a=series(expand(cancel((sum_f-b)/2)),EPS,0,3).removeO()
    Klog=madd(mscal(a,face_id(p)),mscal(b,mscal(1/mm,rho)))
    Ktl=traceless_face(Klog,p)
    return [[[safe_coeff(Ktl[i][j][k],2) for k in range(8)] for j in range(3)] for i in range(3)]

print("="*72); print("GUARD #6: re-verify K^(2) & DEAD on the ENGINE octonion table"); print("="*72)
# K^(2) at E11
M,ms=Mfull(); K2=K2_indep(E11,M)
pred=mscal(-R(9,2)*inner(M,E11),traceless_face(comp(E11,M),E11))
rep("[engine table] K^(2) = -(9/2)<M,p> traceless(C_pM) @ E11 (my matrix-log)", meq(msimp(K2),msimp(pred)))
# K^(2) at engine generic faces (rational): use engine V24.herm_from_vec
fA=V24.herm_from_vec([V24.oct1(0,R(1,3)),V24.oct1(0,R(2,3)),V24.oct1(0,R(2,3))])
fE7=V24.herm_from_vec([V24.oct1(0,R(1,3)),V24.oct1(7,R(2,3)),V24.oct1(0,R(2,3))])
import random; random.seed(11)
allok=True
for p in [fA,fE7]:
    for _ in range(2):
        sv=[R(random.randint(-4,4),random.randint(1,4)) for _ in range(26)]
        Mr=H(sv[0],sv[1],-sv[0]-sv[1],list(sv[2:10]),list(sv[10:18]),list(sv[18:26]))
        K2r=K2_indep(p,Mr)
        predr=mscal(-R(9,2)*inner(Mr,p),traceless_face(comp(p,Mr),p))
        allok&=meq(msimp(K2r),msimp(predr))
rep("[engine table] K^(2) formula holds at generic faces (anchor + octonionic e7) x random M", allok)

# DEAD on engine table
def Hs():
    s=symbols("h0:27",real=True); return H(s[0],s[1],s[2],list(s[3:11]),list(s[11:19]),list(s[19:27])),list(s)
def Ffield(M,p): return mscal(inner(M,p),traceless_face(comp(p,M),p))
def eqs_at(Hh,M,p,t=False):
    r=msub(traceless_face(comp(p,Hh),p),Ffield(M,p)); out=[]
    for i in range(3):
        for j in range(3):
            for k in range(8):
                e=cancel(r[i][j][k])
                if e!=0:
                    if t:
                        num=sp.numer(sp.together(e))
                        try: cs=sp.Poly(num,TT).coeffs()
                        except sp.PolynomialError: cs=[num]
                        for c in cs:
                            cc=cancel(c)
                            if cc!=0: out.append(cc)
                    else: out.append(e)
    return list(set(out))
Hh,hs=Hs(); M2,_=Mfull()
print("  E11-only solvable:", linsolve(eqs_at(Hh,M2,E11),hs)!=EmptySet)
Hh2,hs2=Hs()
eqs=eqs_at(Hh2,M2,E11)+eqs_at(Hh2,M2,V24.family(TT,1,1),t=True)+eqs_at(Hh2,M2,V24.family(TT,1,0),t=True)
sol=linsolve(list(set(eqs)),hs2)
rep("[engine table] E11+off-u(1,1)+(1,0) over Q(t): global H = EmptySet => DEAD", sol==EmptySet)
Hh3,hs3=Hs()
eqs3=eqs_at(Hh3,M2,E11)+eqs_at(Hh3,M2,fA)+eqs_at(Hh3,M2,fE7)
sol3=linsolve(list(set(eqs3)),hs3)
rep("[engine table] E11+2 generic rational anchors (incl octonionic): EmptySet => DEAD", sol3==EmptySet)
print(f"\n[engine-table] {sum(PASS)}/{len(PASS)}")
