"""ATTACK 2 — the 5:4 split for the REMAINING single generators (s02,a02,s12,a12) and a 2nd
dense direction. If ALL give 5:4, the 'one straddle combination' claim is robust => rank arg holds.
If ANY differs, the matter reaches >1 combination => CRACK.
Cheaper dense witness: d3 = diag(2,-1,-1) (TrM^2=6, detM=2). Plus the 4 unchecked single gens.
"""
import sys, time
sys.path.insert(0,"/Users/ehrlich/scratch/get-physics-done/code")
import sympy as sp
from sympy import cancel, Rational, zeros, Matrix
import tensor_probe as TP
import lichnerowicz_response as L
t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam=TP.christoffel_hol(g,ginv)
gm=L._gellmann_directions(); mats=dict(gm); z=zeros(2,2)
def split_of(M, label):
    B3=TP.grad_bilinear(cancel(TP.phi_field(M)),simp=TP.together)
    r,_,_,_,info=L.extract_tt(B3,g,ginv,Gam,verify=False)
    if r is None: print(f"{el()} {label}: FAIL"); return
    b11 =cancel(TP.l2_tensor((z,r[1],z),(z,r[1],z),ginv))
    bant=cancel(TP.l2_tensor((r[0],z,r[2]),(r[0],z,r[2]),ginv))
    ratio=cancel(b11/bant) if bant!=0 else None
    s11=cancel(b11/(b11+bant)) if (b11+bant)!=0 else None
    print(f"{el()} {label}: ratio(11:anti)={ratio}  norm-split 11={s11} (5:4 => 5/4, 5/9)")
for nm in ['s02','a02','s12','a12']:
    split_of(mats[nm], f"single {nm}")
split_of(Matrix([[2,0,0],[0,-1,0],[0,0,-1]]), "d3=diag(2,-1,-1) detM=2 dense")
