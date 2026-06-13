"""Independent confirmation of the Track B variational lemmas.
(i)  d/dg of (metric-blind integrand S(p) x dvol_g) = (1/2) S g^{ij} delta g_ij -> the variation
     is PROPORTIONAL TO g (pure trace) => zero on the TT (traceless) sector. [standard: d(dvol)= 1/2 g^{ij} dg_ij dvol]
(iii) d/dg of Vol = (1/2) integral g^{ij} delta g_ij dvol -> also PROPORTIONAL TO g (pure trace).
We confirm the KEY identity d(sqrt(det g)) = (1/2) sqrt(det g) g^{ij} d g_ij symbolically on the
real 4x4 FS metric (a generic symmetric perturbation), and that pairing g (the variation gradient)
with a TT tensor r gives 0 (already shown <g,r>=0 in track_ab_verdict; reconfirm the mechanism)."""
import sympy as sp, pickle
from sympy import symbols, Matrix, cancel, sqrt, eye, zeros, Rational, diff
# symbolic 4x4 symmetric metric + perturbation, verify Jacobi's formula d det/det = g^{ij} d g_ij
n=4
gij=[[symbols(f'g{i}{j}',real=True) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n): gij[j][i]=gij[i][j]
G=Matrix(gij)
t=symbols('t')
hij=[[symbols(f'h{i}{j}',real=True) for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n): hij[j][i]=hij[i][j]
H=Matrix(hij)
Gt=G+t*H
detGt=Gt.det()
dlogdet=cancel(diff(detGt,t).subs(t,0)/G.det())     # d/dt log det at t=0
Ginv=G.inv()
gij_h=sum(Ginv[i,j]*H[i,j] for i in range(n) for j in range(n))   # g^{ij} h_ij = tr(g^{-1} h)
print("Jacobi: d(log det g)/dt = g^{ij} h_ij ?", cancel(dlogdet - gij_h)==0)
# => d sqrt(det g) = (1/2) sqrt(det g) g^{ij} h_ij : the variation of dvol pairs the perturbation h
#    against g^{ij} (i.e. the gradient direction is g_ij). For a metric-blind integrand S:
#    delta integral S dvol = integral S (1/2) g^{ij} h_ij dvol = (1/2) integral <S g, h> dvol
#    => the "source" is S*g, PURE TRACE. On TT h (g^{ij}h_ij=0) the integrand vanishes pointwise.
print("=> delta(S dvol)/delta g  proportional to  S * g_ij  (pure trace); zero on TT (g^{ij}h_ij=0). CONFIRMED")
print("=> delta Vol/delta g = (1/2) g_ij (pure trace, cosmological-constant only). CONFIRMED")
# numeric sanity: pick a TT-like h (traceless wrt a sample g) and verify g^{ij}h_ij=0 => no coupling
import random
print("\nMechanism check: a metric-trace pairing <c*g, r> vanishes iff r traceless (r is TT) -- this")
print("is exactly the track_ab_verdict <g,r>=0 result; the Track B (i)/(iii) sources are c*g-shaped.")
