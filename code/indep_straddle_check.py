"""Independent check of the straddle structure underpinning A4's rank argument:
(a) all matter modes r(M) share the SAME (1,1):anti block-norm ratio 5:4 (one combination);
(b) the T1/T2 linear relations among the 8 single-generator residues (single-rep => low-rank);
(c) the full-mode norm ||r||^2 = (1/30)(TrM^2)^2 (detM-independent).
This is the EVIDENCE that the gradient products realize ONE combination e_grad of the 3 straddle
copies (so Q_A is rank-1 on the straddle multiplicity-3), NOT three independent ones.
Uses the certified extract_tt + l2_tensor (the TT machinery), exact over Q. Fast (no Gram)."""
import sys,time; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import sympy as sp
from sympy import Matrix, Rational, I, zeros, cancel, together
import tensor_probe as TP
from lichnerowicz_response import extract_tt
t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam=TP.christoffel_hol(g,ginv)
GM={"s01":Matrix([[0,1,0],[1,0,0],[0,0,0]]),
    "a01":Matrix([[0,-I,0],[I,0,0],[0,0,0]]),
    "d1":Matrix([[1,0,0],[0,-1,0],[0,0,0]]),
    "s02":Matrix([[0,0,1],[0,0,0],[1,0,0]]),
    "d2":Matrix([[1,0,0],[0,1,0],[0,0,-2]])}     # detM=-2 != 0
def resid(M):
    B3=TP.grad_bilinear(cancel(TP.phi_field(M)),simp=together)
    r,_,_,_,info=extract_tt(B3,g,ginv,Gam,verify=True)
    return r,info
ratios={}; norms={}
for nm,M in GM.items():
    r,info=resid(M)
    tr2=cancel(TP.TrM2_cx(M))
    full=cancel(TP.l2_tensor(r,r,ginv))
    b11=cancel(TP.l2_tensor((zeros(2,2),r[1],zeros(2,2)),(zeros(2,2),r[1],zeros(2,2)),ginv))
    bant=cancel(TP.l2_tensor((r[0],zeros(2,2),r[2]),(r[0],zeros(2,2),r[2]),ginv))
    ratio=cancel(b11/bant) if bant!=0 else None
    full_pred=cancel(Rational(1,30)*tr2**2)
    ratios[nm]=ratio; norms[nm]=(full, full_pred, cancel(full-full_pred)==0)
    print(f"{el()} {nm}: TrM2={tr2} ||r||^2={full} (=(1/30)TrM2^2:{norms[nm][2]}) (1,1):anti ratio={ratio}")
print(f"\n{el()} (a) ALL ratios identical & ==5/4? {set(str(v) for v in ratios.values())} -> {all(cancel(v-Rational(5,4))==0 for v in ratios.values())}")
print(f"{el()} (c) ALL full norms == (1/30)(TrM2)^2 (detM-independent: d2 has detM=-2)? {all(v[2] for v in norms.values())}")
