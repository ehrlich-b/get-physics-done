"""ATTACK 4 — is FS the UNIQUE SU(3)-invariant lambda_1-extremal metric (upgrading Track A to a law)?
CP^2 = SU(3)/U(2). SU(3)-invariant metrics <-> Ad(U(2))-invariant inner products on the isotropy
rep m (real dim 4). If the isotropy rep is IRREDUCIBLE (over R), the invariant inner product is
UNIQUE up to scale => ALL SU(3)-invariant metrics are homothetic to FS => among SU(3)-invariant
metrics, FS is unique up to scale (trivially lambda_1-extremal-unique in that class).

Test: is the isotropy rep of U(2) on T_o CP^2 irreducible over R?
The isotropy rep is the standard C^2 rep of U(2)=S(U(2)xU(1)) (the 2 of SU(2) tensor a U(1) charge).
As a COMPLEX rep it's irreducible (the standard 2). As a REAL rep (real dim 4) it's also
irreducible BECAUSE it carries a U(2)-invariant complex structure and is C-irreducible of complex
type (not real/quaternionic in a way that splits it). So real-irreducible => unique invariant metric
up to scale.

I verify via Schur: count the dimension of Ad(U(2))-invariant symmetric bilinear forms on m=C^2.
This = multiplicity of the trivial rep in Sym^2_R(m). For the standard U(2) rep on C^2:
 Sym^2_R(C^2) (real symmetric forms) decomposes; the invariants = real symmetric U(2)-invariant
 forms. For an irreducible complex rep of complex type, the ONLY invariant real-symmetric form is
 the real part of the Hermitian form => 1-dimensional => UNIQUE up to scale.
"""
import numpy as np
# Represent U(2) generators acting on R^4 = C^2 (z1,z2)->(x1,y1,x2,y2). Build the Lie algebra u(2)
# action and find the space of symmetric 4x4 matrices S commuting with ALL generators
# (g^T S + S g = 0 for g in the algebra, i.e. S invariant under the orthogonal-ized action).
# u(2) = span{ i*I (overall U(1)), and su(2): i*sigma_x, i*sigma_y, i*sigma_z } acting on C^2.

def cx_to_real(M):
    # M complex 2x2 acting on C^2; real 4x4 acting on (x1,y1,x2,y2) with z=x+iy
    R=np.zeros((4,4))
    for a in range(2):
        for b in range(2):
            re=M[a,b].real; im=M[a,b].imag
            R[2*a,2*b]=re;   R[2*a,2*b+1]=-im
            R[2*a+1,2*b]=im; R[2*a+1,2*b+1]=re
    return R

I2=np.eye(2,dtype=complex)
sx=np.array([[0,1],[1,0]],dtype=complex)
sy=np.array([[0,-1j],[1j,0]],dtype=complex)
sz=np.array([[1,0],[0,-1]],dtype=complex)
gens_cx=[1j*I2, 1j*sx, 1j*sy, 1j*sz]   # u(2) basis (anti-Hermitian)
gens=[cx_to_real(g) for g in gens_cx]

# Space of symmetric 4x4 S with g^T S + S g = 0 for all g (invariant inner products).
# Build linear system on the 10 independent entries of symmetric S.
import itertools
idx=[(i,j) for i in range(4) for j in range(i,4)]   # 10
def S_from(vec):
    S=np.zeros((4,4))
    for v,(i,j) in zip(vec,idx):
        S[i,j]=v; S[j,i]=v
    return S
# constraints: for each g, g^T S + S g = 0 (16 eqs each)
rows=[]
for g in gens:
    for p in range(4):
        for q in range(4):
            # coefficient of each basis S-entry in (g^T S + S g)[p,q]
            row=[]
            for (i,j) in idx:
                Sb=np.zeros((4,4)); Sb[i,j]=1; Sb[j,i]=1
                val=(g.T@Sb + Sb@g)[p,q]
                row.append(val)
            rows.append(row)
A=np.array(rows)
# nullspace dimension = number of invariant symmetric forms
u,s,vt=np.linalg.svd(A)
tol=1e-9
rank=int((s>tol).sum())
null=len(idx)-rank
print(f"dim of invariant symmetric forms on T_o CP^2 (U(2) isotropy) = {null}")
print(f"  (rank A={rank} of {len(idx)} sym entries; {A.shape[0]} constraint rows)")
if null==1:
    print("  => UNIQUE up to scale: ALL SU(3)-invariant metrics on CP^2 are homothetic to FS.")
    print("  => Within the SU(3)-invariant class, FS IS the unique metric (up to scale).")
else:
    print(f"  => {null}-parameter family of invariant metrics; FS not unique even invariantly.")
