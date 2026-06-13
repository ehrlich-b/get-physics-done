"""The complex-block <-> real 4x4 symmetric tensor dictionary, built independently.
A symmetric 2-tensor in complex frame has blocks (H20,H11,H02) with components
  T_{ab}=H20[a,b], T_{a bbar}=H11[a,b], T_{abar bbar}=H02[a,b],
in the cobasis (dz^a, dzbar^a).  We convert to the real cobasis (dx_a,dy_a) via
  dz^a = dx_a + i dy_a,  dzbar^a = dx_a - i dy_a.
A real symmetric tensor T = T_{mu nu} dq^mu dq^nu (mu over z1,z2,zbar1,zbar2) becomes, in
real coords q=(x1,y1,x2,y2):  T_real = sum T_{mu nu} (e^mu)(e^nu) with e^{z_a}=dx_a+i dy_a etc.
Verify: the complex metric blocks (0, g_{a bbar}, 0) -> the real metric G (cross-check).
"""
import sympy as sp, pickle
from sympy import cancel, zeros, symbols, Rational, I, together, diff, Matrix

# the COMPLEX-frame fields use tensor_probe's z1,z2,z1b,z2b. We bridge by substituting
# z_a = x_a + i y_a, zbar_a = x_a - i y_a into the complex fields, getting real-coord functions.
x1,y1,x2,y2 = symbols('x1 y1 x2 y2', real=True)
RC=[x1,y1,x2,y2]; xs=[x1,x2]; ys=[y1,y2]

import sys; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import tensor_probe as TP
Z1,Z2,Z1B,Z2B=TP.Z1,TP.Z2,TP.Z1B,TP.Z2B
SUB={Z1:x1+I*y1, Z2:x2+I*y2, Z1B:x1-I*y1, Z2B:x2-I*y2}

def cplx_to_real_field(f):
    return sp.expand(f.subs(SUB))

# real cobasis vectors as coefficient rows in (dx1,dy1,dx2,dy2):
# index map: complex mu in {0,1,2,3}={z1,z2,zbar1,zbar2}
# e^{z_a} = dx_a + i dy_a ; e^{zbar_a}=dx_a - i dy_a
# real coords order q=(x1,y1,x2,y2) -> positions: x_a at 2a, y_a at 2a+1
def cobasis(mu):
    v=[sp.Integer(0)]*4
    if mu<2:   # z_a
        a=mu; v[2*a]=1; v[2*a+1]=I
    else:      # zbar_a
        a=mu-2; v[2*a]=1; v[2*a+1]=-I
    return v

def blocks_to_real(blocks):
    """Convert complex blocks (H20,H11,H02) [each 2x2 sympy, entries in z,zbar] to a real 4x4
    symmetric tensor T_real[i][j] in coords (x1,y1,x2,y2) [entries real-coord functions]."""
    H20,H11,H02=blocks
    # full complex T_{mu nu}, mu,nu in 0..3, symmetric. _Tget:
    def Tget(mu,nu):
        bar=lambda i:i>=2; ix=lambda i:i%2
        if not bar(mu) and not bar(nu): return H20[ix(mu),ix(nu)]
        if bar(mu) and bar(nu):         return H02[ix(mu),ix(nu)]
        if not bar(mu) and bar(nu):     return H11[ix(mu),ix(nu)]
        return H11[ix(nu),ix(mu)]
    Treal=[[sp.Integer(0)]*4 for _ in range(4)]
    for mu in range(4):
        em=cobasis(mu)
        for nu in range(4):
            en=cobasis(nu)
            Tmn=cplx_to_real_field(Tget(mu,nu))
            for i in range(4):
                if em[i]==0: continue
                for j in range(4):
                    if en[j]==0: continue
                    Treal[i][j]+=Tmn*em[i]*en[j]
    # realify (should be real symmetric)
    for i in range(4):
        for j in range(4):
            Treal[i][j]=cancel(sp.re(sp.expand(Treal[i][j])) + sp.I*sp.im(sp.expand(Treal[i][j])))
    return Treal

# CROSS-CHECK: complex metric (0,g,0) -> real metric G
g=TP.fs_metric()
gblocks=(zeros(2,2), g, zeros(2,2))
Greal=blocks_to_real(gblocks)
with open('/tmp/indep_G.pkl','rb') as f:
    G_direct=pickle.load(f)['G']
# both as real-coord matrices; compare at test point
pt={x1:Rational(1,3),y1:Rational(1,5),x2:Rational(-1,4),y2:Rational(1,7)}
print("Checking complex-blocks->real metric matches independent direct metric G:")
match=True
for i in range(4):
    for j in range(4):
        a=cancel(Greal[i][j].subs(pt)); b=cancel(G_direct[i,j].subs(pt))
        if cancel(a-b)!=0:
            match=False
            print(f"  MISMATCH [{i},{j}]: blocks->{a} vs direct {b}")
print(f"*** dictionary metric match: {match} ***")
print("Greal[0][0] at pt:", cancel(Greal[0][0].subs(pt)), " G_direct[0][0]:", cancel(G_direct[0,0].subs(pt)))
print("imag parts of Greal at pt all zero:", all(sp.im(cancel(Greal[i][j].subs(pt)))==0 for i in range(4) for j in range(4)))

import pickle as pk
pk.dump({'SUB':SUB}, open('/tmp/indep_sub.pkl','wb'))
print("done")
