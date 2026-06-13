"""INDEPENDENT real-coordinate Lichnerowicz operator, applied to the control Hess(R_M).
Delta_L h_{ij} = nabla*nabla h_{ij} + R_{ik}h^k_j + R_{jk}h^k_i - 2 R_{ikjl}h^{kl}
On Einstein Ric=Lambda g (Lambda=6): = nabla*nabla h + 12 h - 2 Rdot h, Rdot h_{ij}=R_{ikjl}h^{kl}.
nabla*nabla h = -g^{ij} nabla_i nabla_j h  (positive geometer's Laplacian).
Built ENTIRELY in the real 4D frame from the real metric G (zero shared code with the complex op).
Test eigentensor: Hess(R_M) (the provable lambda=32 control). Expect Delta_L = 32 * h.

Strategy for tractability: everything symbolic in real coords is heavy; we evaluate the FINAL
Delta_L h and h at a rational test point and check Delta_L h = 32 h there (an eigentensor identity
holds pointwise, so a single generic point with all entries matching over Q is a strong check;
we use TWO points to rule out coincidence)."""
import sympy as sp, pickle
from sympy import cancel, zeros, symbols, Rational, I, together, diff, Matrix

x1,y1,x2,y2=symbols('x1 y1 x2 y2',real=True); RC=[x1,y1,x2,y2]; xs=[x1,x2]; ys=[y1,y2]
import sys; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import tensor_probe as TP
Z1,Z2,Z1B,Z2B=TP.Z1,TP.Z2,TP.Z1B,TP.Z2B
SUB={Z1:x1+I*y1,Z2:x2+I*y2,Z1B:x1-I*y1,Z2B:x2-I*y2}
def c2r(f): return sp.expand(f.subs(SUB))

# --- real metric + Christoffels (reuse the saved Christoffels from indep_curv) ---
D=pickle.load(open('/tmp/indep_gam.pkl','rb'))
G=D['G']; Ginv=D['Ginv']; Gam=D['Gam']   # Gam[k][i][j] symbolic
def d(f,i): return diff(f,RC[i])
n=4

# --- dictionary: complex blocks -> real 4x4 symmetric tensor field ---
def cobasis(mu):
    v=[sp.Integer(0)]*4
    if mu<2: a=mu; v[2*a]=1; v[2*a+1]=I
    else:    a=mu-2; v[2*a]=1; v[2*a+1]=-I
    return v
def blocks_to_real(blocks):
    H20,H11,H02=blocks
    def Tget(mu,nu):
        bar=lambda i:i>=2; ix=lambda i:i%2
        if not bar(mu) and not bar(nu): return H20[ix(mu),ix(nu)]
        if bar(mu) and bar(nu):         return H02[ix(mu),ix(nu)]
        if not bar(mu) and bar(nu):     return H11[ix(mu),ix(nu)]
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
    for i in range(4):
        for j in range(4):
            T[i][j]=together(T[i][j])
    return T

# --- covariant derivative of a (0,2) tensor: nabla_k T_{ij} = d_k T_{ij} - Gam^m_{ki}T_{mj} - Gam^m_{kj}T_{im}
def nabla_T(T):
    """returns D[k][i][j] = nabla_k T_{ij}, symbolic."""
    D3=[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                t=d(T[i][j],k)
                for m in range(n):
                    t-=Gam[m][k][i]*T[m][j]+Gam[m][k][j]*T[i][m]
                D3[k][i][j]=together(t)
    return D3

# --- rough Laplacian nabla*nabla T = -g^{kl} nabla_k nabla_l T (POSITIVE) ---
# nabla_k nabla_l T_{ij} = d_k (nabla_l T)_{ij} - Gam^m_{kl}(nabla_m T)_{ij}
#                          - Gam^m_{ki}(nabla_l T)_{mj} - Gam^m_{kj}(nabla_l T)_{im}
def rough_lap(T, pt):
    """returns the 4x4 (nabla*nabla T)_{ij} EVALUATED at pt (rationals)."""
    DT=nabla_T(T)                      # symbolic first cov deriv
    Gam_pt=[[[cancel(Gam[a][b][c].subs(pt)) for c in range(n)] for b in range(n)] for a in range(n)]
    Ginv_pt=Ginv.subs(pt).applyfunc(cancel)
    out=zeros(n,n)
    for i in range(n):
        for j in range(n):
            acc=sp.Integer(0)
            for k in range(n):
                for l in range(n):
                    gkl=Ginv_pt[k,l]
                    if gkl==0: continue
                    # second cov deriv (nabla_k nabla_l T)_{ij} at pt
                    t=cancel(d(DT[l][i][j],k).subs(pt))
                    for m in range(n):
                        t-=Gam_pt[m][k][l]*cancel(DT[m][i][j].subs(pt))
                        t-=Gam_pt[m][k][i]*cancel(DT[l][m][j].subs(pt))
                        t-=Gam_pt[m][k][j]*cancel(DT[l][i][m].subs(pt))
                    acc+=gkl*t
            out[i,j]=cancel(-acc)
    return out

# --- Riemann R_{ikjl} (all lower) at pt, and Rdot h_{ij}=R_{ikjl}h^{kl} ---
def riemann_lower_pt(pt):
    """R^a_{bcd}=d_c Gam^a_{db}-d_d Gam^a_{cb}+Gam^a_{cm}Gam^m_{db}-Gam^a_{dm}Gam^m_{cb}; lower with G."""
    Gam_pt=[[[cancel(Gam[a][b][c].subs(pt)) for c in range(n)] for b in range(n)] for a in range(n)]
    Gp=G.subs(pt).applyfunc(cancel)
    Rup=[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    t=cancel(d(Gam[a][dd][b],cc).subs(pt))-cancel(d(Gam[a][cc][b],dd).subs(pt))
                    for m in range(n):
                        t+=Gam_pt[a][cc][m]*Gam_pt[m][dd][b]-Gam_pt[a][dd][m]*Gam_pt[m][cc][b]
                    Rup[a][b][cc][dd]=cancel(t)
    # lower: R_{abcd}=g_{ae}R^e_{bcd}
    Rl=[[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    s=sp.Integer(0)
                    for e in range(n):
                        s+=Gp[a,e]*Rup[e][b][cc][dd]
                    Rl[a][b][cc][dd]=cancel(s)
    return Rl

def Rdot_pt(T, Rl, pt):
    """Rdot h_{ij}=R_{ikjl} h^{kl}; raise h with Ginv at pt."""
    Gp=G.subs(pt).applyfunc(cancel); Ginv_pt=Ginv.subs(pt).applyfunc(cancel)
    Tp=Matrix([[cancel(T[i][j].subs(pt)) for j in range(n)] for i in range(n)])
    # h^{kl}=g^{km}g^{ln}h_{mn}
    hup=zeros(n,n)
    for k in range(n):
        for l in range(n):
            s=sp.Integer(0)
            for m in range(n):
                for nn in range(n):
                    s+=Ginv_pt[k,m]*Ginv_pt[l,nn]*Tp[m,nn]
            hup[k,l]=cancel(s)
    out=zeros(n,n)
    for i in range(n):
        for j in range(n):
            s=sp.Integer(0)
            for k in range(n):
                for l in range(n):
                    s+=Rl[i][k][j][l]*hup[k,l]
            out[i,j]=cancel(s)
    return out

# ===== TEST: control Hess(R_M), M = s01 (lambda_1 dir) -> R_M lambda_2=32 scalar =====
M=Matrix([[0,1,0],[1,0,0],[0,0,0]])   # s01
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam_c=TP.christoffel_hol(g,ginv)
RM=TP.R_M_field(M)
HRM_blocks=TP.cov_hessian(RM,g,ginv,Gam_c,simp=cancel)   # complex blocks of Hess(R_M)
print("converting Hess(R_M) to real 4x4 tensor field...")
Hreal=blocks_to_real(HRM_blocks)

for ip,pt in enumerate([{x1:Rational(1,3),y1:Rational(1,5),x2:Rational(-1,4),y2:Rational(1,7)},
                        {x1:Rational(2,5),y1:Rational(-1,3),x2:Rational(1,6),y2:Rational(1,4)}]):
    print(f"\n=== TEST POINT {ip+1}: {pt} ===")
    Hp=Matrix([[cancel(Hreal[i][j].subs(pt)) for j in range(n)] for i in range(n)])
    print("h symmetric:", Hp==Hp.T, " h real:", all(sp.im(Hp[i,j])==0 for i in range(n) for j in range(n)))
    rl=rough_lap(Hreal,pt)
    Rl=riemann_lower_pt(pt)
    rd=Rdot_pt(Hreal,Rl,pt)
    DL=zeros(n,n)
    for i in range(n):
        for j in range(n):
            DL[i,j]=cancel(rl[i,j]+12*Hp[i,j]-2*rd[i,j])
    # eigenvalue: DL = lam * Hp ?
    lam=None; ok=True
    for i in range(n):
        for j in range(n):
            if Hp[i,j]!=0:
                r=cancel(DL[i,j]/Hp[i,j])
                if lam is None: lam=r
                elif cancel(lam-r)!=0: ok=False; print(f"  NONPROP [{i},{j}]: {r} vs {lam}")
            else:
                if cancel(DL[i,j])!=0: ok=False; print(f"  h=0 but DL!=0 at [{i},{j}]: {DL[i,j]}")
    print(f"  rough_lap[0,0]={cancel(rl[0,0])}")
    print(f"  Rdot[0,0]={cancel(rd[0,0])}, 12*h[0,0]={12*Hp[0,0]}")
    print(f"  Delta_L eigenvalue lambda = {lam}  (expect 32);  proportional on all entries: {ok}")
    print(f"  *** INDEPENDENT Delta_L(Hess R_M) = {lam} * h  [lambda==32: {lam==32 and ok}] ***")
