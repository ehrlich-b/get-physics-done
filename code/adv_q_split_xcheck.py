"""Resolve the sum question precisely. Tr(V)=<sum_a w_a dphi(x)dphi, r> = <4g, r> = 0 (WEIGHTED).
Confirm: weighted numerator sum = sum_a w_a * <r, dphi_a(x)dphi_a> = 0.  (w: 1 for the 7, 1/3 for d2.)
Also confirm the SHIFT sum (sum_a delta_a) -- the trace of the eigenvalue-perturbation operator.
The shifts delta_a = num_a/den_a with den_a = <phi_a,phi_a>. So sum of SHIFTS != weighted num sum.
Both being computed cleanly is the point: the 8 shifts are UNEQUAL (degeneracy lifts) regardless.
"""
import sys,time
sys.path.insert(0,"/Users/ehrlich/scratch/get-physics-done/code")
import sympy as sp
from sympy import cancel, Rational
import tensor_probe as TP
import lichnerowicz_response as L
t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam=TP.christoffel_hol(g,ginv)
gm=L._gellmann_directions(); mats=dict(gm); names=[nm for nm,_ in gm]
w={nm: Rational(2,1)/cancel((A*A).trace()) for nm,A in gm}
B3=TP.grad_bilinear(cancel(TP.phi_field(mats['d1'])),simp=TP.together)
r,_,_,_,_=L.extract_tt(B3,g,ginv,Gam,verify=False)
wnum=0; shifts=[]
for nm in names:
    Ba=TP.grad_bilinear(cancel(TP.phi_field(mats[nm])),simp=TP.together)
    num=cancel(TP.l2_tensor(r,Ba,ginv))
    den=cancel(TP.l2_scalar(cancel(TP.phi_field(mats[nm]))**2))
    wnum=cancel(wnum + w[nm]*num)
    shifts.append(cancel(num/den))
print(f"{el()} WEIGHTED numerator sum  sum_a w_a<r,dphi_a x dphi_a> = {wnum}  (Tr(V); expect 0)")
print(f"{el()} SHIFT sum  sum_a delta_a = {cancel(sum(shifts))}  (trace of perturbation; was 0 in attack1b)")
print(f"{el()} 8 shifts = {shifts}")
print(f"{el()} shifts all equal? {all(cancel(s-shifts[0])==0 for s in shifts)}  (FALSE => degeneracy LIFTS)")
