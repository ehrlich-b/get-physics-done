"""ATTACK 1 — is the lambda_1-Hessian eigenvalue q on the matter-27 a FORCED number = 20?
First: establish the structure. lambda_1 = 12 on CP^2-FS is the FIRST nonzero Laplacian eigenvalue,
8-fold degenerate (the SU(3) adjoint = the moment functions phi_a). v25 used this: the moment map
embeds via these 8.

The verdict A4 says: Q_A = the lambda_1-extremal Hessian (second variation of lambda_1.Vol^{1/2}),
and on the matter-27 it acts as a scalar q (Schur). The attack: compute q and compare to 20.

CRUCIAL OBSTRUCTION (which I test): lambda_1 is DEGENERATE (8-fold). The second variation of a
DEGENERATE eigenvalue under a metric perturbation h is NOT a single number -- the 8 eigenvalues
SPLIT to first order in h (generically), so 'the lambda_1-Hessian' is ill-defined as a single scalar
unless the perturbation preserves the degeneracy. This is the heart of whether q carries content.

Test the premise: under a perturbation h = r (the matter mode, in the 27), does lambda_1=12 stay
8-fold degenerate to first order, or split? The first-order eigenvalue shift for eigenfunction phi_a
is  delta lambda_a = -<h, Hess-type bilinear of phi_a> / ||phi_a||^2  (the standard formula).
If the 8 shifts are UNEQUAL, lambda_1 splits => no single q => the second variation is set-valued
=> 'q=20' is not even well-posed => the Schur-dismissal of A4 is CORRECT (the operator is not a
clean scalar on a single irrep in the way 'q=20' would require).

Compute the 8 first-order shifts delta lambda_a for h = r(d1).
The Rayleigh-quotient first-order shift under g -> g + t h (h a symmetric 2-tensor, TT):
  d lambda_a/dt = - integral( h^{ij} d_i phi_a d_j phi_a ) / integral(phi_a^2)   [for the Laplacian
  eigenvalue, TT h, normalized]  -- up to the standard sign/normalization; the RELATIVE spread
  across a is what matters (equal => no split; unequal => split).
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
gm=L._gellmann_directions(); mats=dict(gm); names=[nm for nm,_ in gm]

# matter mode h = r(d1) (TT)
B3=TP.grad_bilinear(cancel(TP.phi_field(mats['d1'])),simp=TP.together)
r,_,_,_,info=L.extract_tt(B3,g,ginv,Gam,verify=True)
print(f"{el()} h=r(d1) extracted: tr0={info.get('tr_zero')} div0={info.get('div_zero')}")

# first-order shift of lambda_a: delta_a = <h, dphi_a (x) dphi_a> / <phi_a,phi_a>
# = l2_tensor(h, grad_bilinear(phi_a)) / l2_scalar(phi_a^2)   (the Rayleigh numerator perturbation)
shifts={}
for nm in names:
    phia=cancel(TP.phi_field(mats[nm]))
    Ba=TP.grad_bilinear(phia,simp=TP.together)  # dphi_a (x) dphi_a as a block-triple
    num=cancel(TP.l2_tensor(r, Ba, ginv))        # <h, dphi_a (x) dphi_a>
    den=cancel(TP.l2_scalar(phia**2))            # <phi_a, phi_a> (the L2 norm of phi_a)
    shifts[nm]=cancel(num/den) if den!=0 else None
    print(f"{el()} delta_{nm} = {shifts[nm]}  (num={num}, den={den})")
vals=[v for v in shifts.values() if v is not None]
allequal = all(cancel(v-vals[0])==0 for v in vals)
print(f"{el()} all 8 first-order shifts EQUAL? {allequal}")
print(f"   distinct shift values: {sorted(set(str(v) for v in vals))}")
if not allequal:
    print("   => lambda_1=12 SPLITS to first order under h=r => 'the lambda_1-Hessian eigenvalue q'")
    print("      is NOT a single well-defined scalar => 'q=20' ill-posed => Schur-dismissal HOLDS.")
else:
    print("   => degeneracy preserved to first order; q may be well-defined -- pursue second order.")
