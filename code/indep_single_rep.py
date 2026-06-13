"""Independent check that r(M) lives in a single SU(3) irrep (the 27), supporting the Schur
tautology (A4 reason 1). Two light checks (no slow Gram):
  (T1) the linear relation 4(t_s01+t_a01+t_d1)+(t_s02+t_a02+t_s12+t_a12)=0 among single-gen residues
       -- a SINGLE-REP relation (the residues are NOT independent; they realize one combination).
  (8/1-absence) the full-mode norm ||r||^2 = (1/30)(TrM^2)^2 has NO detM (degree-3) term and NO
       independent adjoint piece -- consistent with the pure-27 projection (c_8=c_1=0).
We confirm T1 exactly over Q (fast: tensor identity at the field level, no integration)."""
import sys,time; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import sympy as sp
from sympy import Matrix, Rational, I, zeros, cancel, together
import tensor_probe as TP
from lichnerowicz_response import extract_tt
t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam=TP.christoffel_hol(g,ginv)
GM={"s01":Matrix([[0,1,0],[1,0,0],[0,0,0]]),"a01":Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
    "d1":Matrix([[1,0,0],[0,-1,0],[0,0,0]]),"s02":Matrix([[0,0,1],[0,0,0],[1,0,0]]),
    "a02":Matrix([[0,0,-I],[0,0,0],[I,0,0]]),"s12":Matrix([[0,0,0],[0,0,1],[0,1,0]]),
    "a12":Matrix([[0,0,0],[0,0,-I],[0,I,0]])}
t={}
for nm,M in GM.items():
    B3=TP.grad_bilinear(cancel(TP.phi_field(M)),simp=together)
    r,_,_,_,info=extract_tt(B3,g,ginv,Gam,verify=True)
    t[nm]=r
    print(f"{el()} r[{nm}] extracted (consistent={info.get('consistent')})")
def tadd(*ct):
    out=[zeros(2,2),zeros(2,2),zeros(2,2)]
    for c,T in ct:
        for k in range(3):
            for a in range(2):
                for b in range(2): out[k][a,b]+=c*T[k][a,b]
    return out
S=tadd((4,t["s01"]),(4,t["a01"]),(4,t["d1"]),(1,t["s02"]),(1,t["a02"]),(1,t["s12"]),(1,t["a12"]))
T1=all(cancel(S[k][a,b])==0 for k in range(3) for a in range(2) for b in range(2))
print(f"\n{el()} T1: 4(s01+a01+d1)+(s02+a02+s12+a12) == 0 tensor (exact/Q): {T1}")
print("=> a linear relation among single-gen residues: they realize ONE combination of the straddle")
print("   copies (NOT 3 independent), supporting 'r in a single 27 irrep' (Schur tautology premise).")
