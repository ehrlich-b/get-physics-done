"""Confirm the anti-block norm structure: pure (2,0).(2,0) =0 but the combined (2,0)+(0,2) block
gives 8/135 via the CROSS term. This tells us the 'anti-27' is the real combination (2,0)+(0,2),
not two separate copies. CRUCIAL for the rank argument.
"""
import sys, time
sys.path.insert(0,"/Users/ehrlich/scratch/get-physics-done/code")
import sympy as sp
from sympy import cancel, Rational, zeros
import tensor_probe as TP
import lichnerowicz_response as L
t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam=TP.christoffel_hol(g,ginv)
gm=L._gellmann_directions(); mats={nm:A for nm,A in gm}
nm='s01'
B3=TP.grad_bilinear(cancel(TP.phi_field(mats[nm])),simp=TP.together)
r,wh,wa,f,info=L.extract_tt(B3,g,ginv,Gam,verify=True)
z=zeros(2,2)
n20  =cancel(TP.l2_tensor((r[0],z,z),(r[0],z,z),ginv))
n02  =cancel(TP.l2_tensor((z,z,r[2]),(z,z,r[2]),ginv))
ncross=cancel(TP.l2_tensor((r[0],z,z),(z,z,r[2]),ginv))
nant_combined=cancel(TP.l2_tensor((r[0],z,r[2]),(r[0],z,r[2]),ginv))
n11  =cancel(TP.l2_tensor((z,r[1],z),(z,r[1],z),ginv))
print(f"{el()} (2,0).(2,0) = {n20}")
print(f"{el()} (0,2).(0,2) = {n02}")
print(f"{el()} (2,0).(0,2) cross = {ncross}")
print(f"{el()} combined ((r0,0,r2).(r0,0,r2)) = {nant_combined}  [expect 8/135={Rational(8,135)}]")
print(f"{el()} (1,1).(1,1) = {n11}  [expect 2/27={Rational(2,27)}]")
print(f"{el()} 2*cross = {cancel(2*ncross)}")
# Is the anti-block pointwise nonzero?
print(f"{el()} r[0] entries (sample): {[cancel(r[0][a,b]) for a in range(2) for b in range(2)]}")
