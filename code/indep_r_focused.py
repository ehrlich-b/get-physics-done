"""Focused INDEPENDENT Delta_L on r(s01): reuse the saved r + the validated real-frame operator.
Single direction, single point -> the independent confirmation that r is a 32-eigentensor of MY
operator (which is already control-validated == true Lichnerowicz via Hess(R_M)=32 on all entries)."""
import sys,time,pickle; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import sympy as sp
from sympy import cancel, zeros, symbols, Rational, I, together, diff, Matrix
t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
x1,y1,x2,y2=symbols('x1 y1 x2 y2',real=True); RC=[x1,y1,x2,y2]
import tensor_probe as TP
Z1,Z2,Z1B,Z2B=TP.Z1,TP.Z2,TP.Z1B,TP.Z2B
SUB={Z1:x1+I*y1,Z2:x2+I*y2,Z1B:x1-I*y1,Z2B:x2-I*y2}
def c2r(f): return sp.expand(f.subs(SUB))
D=pickle.load(open('/tmp/indep_gam.pkl','rb')); G=D['G']; Ginv=D['Ginv']; Gam=D['Gam']
def d(f,i): return diff(f,RC[i])
n=4
def cobasis(mu):
    v=[sp.Integer(0)]*4
    if mu<2: a=mu; v[2*a]=1; v[2*a+1]=I
    else: a=mu-2; v[2*a]=1; v[2*a+1]=-I
    return v
def blocks_to_real(blocks):
    H20,H11,H02=blocks
    def Tget(mu,nu):
        bar=lambda i:i>=2; ix=lambda i:i%2
        if not bar(mu) and not bar(nu): return H20[ix(mu),ix(nu)]
        if bar(mu) and bar(nu): return H02[ix(mu),ix(nu)]
        if not bar(mu) and bar(nu): return H11[ix(mu),ix(nu)]
        return H11[ix(nu),ix(mu)]
    T=[[sp.Integer(0)]*4 for _ in range(4)]
    for mu in range(4):
        em=cobasis(mu)
        for nu in range(4):
            en=cobasis(nu)
            Tmn=c2r(Tget(mu,nu))
            for i in range(4):
                if em[i]==0: continue
                for j in range(4):
                    if en[j]==0: continue
                    T[i][j]+=Tmn*em[i]*en[j]
    return [[cancel(T[i][j]) for j in range(4)] for i in range(4)]
def nabla_T(T):
    D3=[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                t=d(T[i][j],k)
                for m in range(n): t-=Gam[m][k][i]*T[m][j]+Gam[m][k][j]*T[i][m]
                D3[k][i][j]=together(t)
    return D3
def rough_lap(T,pt):
    DT=nabla_T(T)
    Gam_pt=[[[cancel(Gam[a][b][c].subs(pt)) for c in range(n)] for b in range(n)] for a in range(n)]
    Ginv_pt=Ginv.subs(pt).applyfunc(cancel); out=zeros(n,n)
    for i in range(n):
        for j in range(n):
            acc=sp.Integer(0)
            for k in range(n):
                for l in range(n):
                    gkl=Ginv_pt[k,l]
                    if gkl==0: continue
                    t=cancel(d(DT[l][i][j],k).subs(pt))
                    for m in range(n):
                        t-=Gam_pt[m][k][l]*cancel(DT[m][i][j].subs(pt))
                        t-=Gam_pt[m][k][i]*cancel(DT[l][m][j].subs(pt))
                        t-=Gam_pt[m][k][j]*cancel(DT[l][i][m].subs(pt))
                    acc+=gkl*t
            out[i,j]=cancel(-acc)
    return out
def riemann_lower_pt(pt):
    Gam_pt=[[[cancel(Gam[a][b][c].subs(pt)) for c in range(n)] for b in range(n)] for a in range(n)]
    Gp=G.subs(pt).applyfunc(cancel)
    Rup=[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    t=cancel(d(Gam[a][dd][b],cc).subs(pt))-cancel(d(Gam[a][cc][b],dd).subs(pt))
                    for m in range(n): t+=Gam_pt[a][cc][m]*Gam_pt[m][dd][b]-Gam_pt[a][dd][m]*Gam_pt[m][cc][b]
                    Rup[a][b][cc][dd]=cancel(t)
    Rl=[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    s=sp.Integer(0)
                    for e in range(n): s+=Gp[a,e]*Rup[e][b][cc][dd]
                    Rl[a][b][cc][dd]=cancel(s)
    return Rl
def Rdot_pt(T,Rl,pt):
    Ginv_pt=Ginv.subs(pt).applyfunc(cancel)
    Tp=Matrix([[cancel(T[i][j].subs(pt)) for j in range(n)] for i in range(n)])
    hup=zeros(n,n)
    for k in range(n):
        for l in range(n):
            s=sp.Integer(0)
            for m in range(n):
                for nn in range(n): s+=Ginv_pt[k,m]*Ginv_pt[l,nn]*Tp[m,nn]
            hup[k,l]=cancel(s)
    out=zeros(n,n)
    for i in range(n):
        for j in range(n):
            s=sp.Integer(0)
            for k in range(n):
                for l in range(n): s+=Rl[i][k][j][l]*hup[k,l]
            out[i,j]=cancel(s)
    return out

r=pickle.load(open('/tmp/r_s01.pkl','rb'))['r']
print(f"{el()} converting r(s01) to real 4x4 ...")
Rreal=blocks_to_real(r)
pt={x1:Rational(1,3),y1:Rational(1,5),x2:Rational(-1,4),y2:Rational(1,7)}
Hp=Matrix([[cancel(Rreal[i][j].subs(pt)) for j in range(n)] for i in range(n)])
print(f"{el()} r real symmetric={Hp==Hp.T} real={all(sp.im(Hp[i,j])==0 for i in range(n) for j in range(n))}")
print(f"{el()} rough_lap ...")
rl=rough_lap(Rreal,pt)
print(f"{el()} riemann ...")
Rl=riemann_lower_pt(pt)
rd=Rdot_pt(Rreal,Rl,pt)
DL=zeros(n,n)
for i in range(n):
    for j in range(n): DL[i,j]=cancel(rl[i,j]+12*Hp[i,j]-2*rd[i,j])
lam=None; ok=True
for i in range(n):
    for j in range(n):
        if Hp[i,j]!=0:
            rr=cancel(DL[i,j]/Hp[i,j])
            if lam is None: lam=rr
            elif cancel(lam-rr)!=0: ok=False; print(f"  NONPROP[{i},{j}]:{rr} vs {lam}")
        else:
            if cancel(DL[i,j])!=0: ok=False; print(f"  h0_DLnz[{i},{j}]:{DL[i,j]}")
print(f"{el()} *** INDEPENDENT Delta_L r(s01) = {lam} * r  [lambda==32 & prop_all: {lam==32 and ok}] ***")
