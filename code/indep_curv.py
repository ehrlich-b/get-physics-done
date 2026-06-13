"""Independent real-coordinate Christoffel, Riemann, Ricci from the real FS metric.
Verify Ric = 6g (Lambda=6) -- the independent confirmation of the Einstein background."""
import sympy as sp, pickle
from sympy import cancel, zeros, symbols, Rational, together, diff

with open('/tmp/indep_G.pkl','rb') as f:
    D=pickle.load(f)
G=D['G']; RC=D['RC']
n=4
Ginv=G.inv().applyfunc(cancel)
print("metric inverse computed")

# work at a fixed rational test point for SPEED, but compute Christoffels/Riemann symbolically
# then evaluate. To keep it tractable: compute Christoffel symbolically (derivatives of G), then
# Riemann via derivatives of Christoffel. CP^2 FS rational fields -> heavy but doable.
def d(f,i): return diff(f,RC[i])

# Christoffel Gamma^k_{ij} = 1/2 g^{kl}(d_i g_{jl}+d_j g_{il}-d_l g_{ij})
print("building Christoffels...")
Gam=[[[sp.Integer(0)]*n for _ in range(n)] for _ in range(n)]
# precompute dG[i][j][k] = d_i g_{jk}
dG=[[[cancel(d(G[j,k],i)) for k in range(n)] for j in range(n)] for i in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            s=sp.Integer(0)
            for l in range(n):
                if Ginv[k,l]==0: continue
                s+=Ginv[k,l]*(dG[i][j][l]+dG[j][i][l]-dG[l][i][j])
            Gam[k][i][j]=together(Rational(1,2)*s)
    print(f"  Gamma^{k} done")

import pickle as pk
with open('/tmp/indep_gam.pkl','wb') as f:
    pk.dump({'Gam':Gam,'G':G,'Ginv':Ginv,'RC':RC}, f)
print("Christoffels saved; now Riemann + Ricci at a TEST POINT (fast)")

# Riemann R^l_{ijk}= d_i Gam^l_{jk} - d_j Gam^l_{ik} + Gam^l_{im}Gam^m_{jk} - Gam^l_{jm}Gam^m_{ik}
# Ricci R_{jk}=R^i_{ijk}. Compute symbolically then eval; but symbolic deriv of Gamma is heavy.
# Strategy: evaluate Ricci at a test point by computing the needed Christoffel derivatives there.
pt={RC[0]:Rational(1,3),RC[1]:Rational(1,5),RC[2]:Rational(-1,4),RC[3]:Rational(1,7)}

# derivative of Gamma^l_{jk} wrt x_i, then substitute pt
print("computing Ricci at test point...")
Ric=zeros(n,n)
Gam_pt=[[[cancel(Gam[k][i][j].subs(pt)) for j in range(n)] for i in range(n)] for k in range(n)]
for j in range(n):
    for k in range(n):
        s=sp.Integer(0)
        for i in range(n):
            # R^i_{ijk}: l=i summed
            dterm = cancel(d(Gam[i][j][k],i).subs(pt)) - cancel(d(Gam[i][i][k],j).subs(pt))
            quad=sp.Integer(0)
            for m in range(n):
                quad+=Gam_pt[i][i][m]*Gam_pt[m][j][k]-Gam_pt[i][j][m]*Gam_pt[m][i][k]
            s+=dterm+quad
        Ric[j,k]=cancel(s)
Gp=G.subs(pt).applyfunc(cancel)
print("Ricci at test point:")
sp.pprint(Ric.applyfunc(lambda e: sp.nsimplify(e)))
print("\n6*G at test point:")
sp.pprint((6*Gp).applyfunc(cancel))
ratio=zeros(n,n)
ok=True
for i in range(n):
    for j in range(n):
        if Gp[i,j]!=0:
            rr=cancel(Ric[i,j]/Gp[i,j])
            ratio[i,j]=rr
            if cancel(rr-6)!=0: ok=False
        else:
            if cancel(Ric[i,j])!=0: ok=False
print("\nRic/G ratio (should be 6 everywhere):")
sp.pprint(ratio)
print(f"\n*** Ric == 6*G (Einstein, Lambda=6) INDEPENDENTLY CONFIRMED: {ok} ***")
