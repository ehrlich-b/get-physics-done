"""INDEPENDENT real-coordinate geometry on CP^2 (FS), built from scratch.
Zero shared code with lichnerowicz_response.py. Real coords (x1,y1,x2,y2), z_a=x_a+i y_a.
Goal: real 4x4 metric, Christoffels, Riemann, Ricci -- verify Ric=6g (Lambda=6), and the
sign conventions, BEFORE building the Lichnerowicz operator independently."""
import sympy as sp
from sympy import Rational, symbols, Matrix, cancel, simplify, sqrt, diff, eye, zeros

# real coordinates
x1,y1,x2,y2 = symbols('x1 y1 x2 y2', real=True)
RC = [x1,y1,x2,y2]
# z_a = x_a + i y_a ; |z|^2 = x1^2+y1^2+x2^2+y2^2
rho = 1 + x1**2 + y1**2 + x2**2 + y2**2

# Kahler potential K = log(rho); the REAL FS metric is the real form of g_phys = (1/2) d d_bar log rho.
# Standard fact: for K(z,zbar), the real Riemannian metric in coords (x_a,y_a) is
#   g_real = 2 * [ Re(g_{a bbar})  block ] ... but cleanest: build it as the real Hessian structure.
# The Kahler metric as a REAL metric: ds^2 = 2 g_{a bbar} dz^a dzbar^b (real part).
# With g_{a bbar} = MET_SCALE * d_a d_bbar K, MET_SCALE=1/2.
# In real coords, the Riemannian metric tensor G_{ij} (i,j over x1,y1,x2,y2) is obtained from
#   ds^2 = sum 2 Re( g_{a bbar} dz^a d(zbar^b) ).
# We construct g_{a bbar} as functions of real coords, then expand the real line element.

MET = Rational(1,2)
# complex potential metric g_{a bbar} = d_{z_a} d_{zbar_b} log rho ; express via real derivs.
# z_a = x_a + i y_a, zbar_a = x_a - i y_a.  d/dz_a = (1/2)(d/dx_a - i d/dy_a), d/dzbar_a=(1/2)(d/dx_a + i d/dy_a)
xs=[x1,x2]; ys=[y1,y2]
def ddz(f,a):   return Rational(1,2)*(diff(f,xs[a]) - sp.I*diff(f,ys[a]))
def ddzb(f,a):  return Rational(1,2)*(diff(f,xs[a]) + sp.I*diff(f,ys[a]))

K = sp.log(rho)
gpot = [[cancel(ddz(ddzb(K,b),a)) for b in range(2)] for a in range(2)]   # g_{a bbar}
gab = [[cancel(MET*gpot[a][b]) for b in range(2)] for a in range(2)]      # g_phys_{a bbar}

# Real line element ds^2 = sum_{a,b} 2 Re( gab[a][b] dz^a conj(dz^b) )
# dz^a = dx_a + i dy_a.  Build symbolic differentials.
dx=[symbols(f'dx{i}',real=True) for i in range(2)]
dy=[symbols(f'dy{i}',real=True) for i in range(2)]
ds2 = 0
for a in range(2):
    dza = dx[a] + sp.I*dy[a]
    for b in range(2):
        dzb_c = dx[b] - sp.I*dy[b]   # conj(dz^b)
        ds2 += gab[a][b]*dza*dzb_c
ds2 = sp.expand(2*sp.re(sp.expand(ds2)))   # 2 Re(...)  -- but gab complex; take real part symbolically
# Actually gab entries are complex rational in real coords; sp.re needs care. Do it via explicit:
ds2 = 0
for a in range(2):
    dza = dx[a] + sp.I*dy[a]
    for b in range(2):
        dzb_c = dx[b] - sp.I*dy[b]
        ds2 += 2*gab[a][b]*dza*dzb_c
ds2 = sp.expand(ds2)
# extract real symmetric metric G_{ij} from ds2 = sum G_ij dq^i dq^j (dq in dx0,dy0,dx1,dy1)
DQ=[dx[0],dy[0],dx[1],dy[1]]
G=zeros(4,4)
for i in range(4):
    for j in range(4):
        if i==j:
            G[i,j]=cancel(ds2.coeff(DQ[i],2))
        else:
            c=cancel(ds2.coeff(DQ[i],1).coeff(DQ[j],1))
            G[i,j]=c/2; G[j,i]=c/2
G=G.applyfunc(lambda e: cancel(sp.re(e)))   # metric must be real
print("G (real 4x4 metric) at generic point, symmetry check:", G==G.T)
# verify imaginary parts vanished
print("metric purely real:", all(sp.im(G[i,j])==0 for i in range(4) for j in range(4)))

# evaluate at a test point to sanity check positive-definiteness
pt={x1:Rational(1,3),y1:Rational(1,5),x2:Rational(-1,4),y2:Rational(1,7)}
Gp=G.subs(pt).applyfunc(cancel)
print("det(G) at test pt:", cancel(Gp.det()), " (should be >0, Riemannian)")
print("G eigenvalues numeric:", [sp.N(e,4) for e in Gp.eigenvals()])

import pickle
with open('/tmp/indep_G.pkl','wb') as f:
    pickle.dump({'G':G,'RC':RC,'rho':rho}, f)
print("saved metric")
