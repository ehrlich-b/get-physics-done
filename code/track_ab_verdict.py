#!/usr/bin/env python3
"""v33 Track A/B verdict core (CORRECTED) — orchestrator-run, exact over Q.
Fixes the two flaws in the first pass: (1) test ON the reality slice (Z1B=conj(Z1)); (2) use the
TRACE-WEIGHTED basis (d2=diag(1,1,-2) has Tr=6, others Tr=2) so the moment sums are basis-honest.

A1  (native?):   sphere  |p-I/3|^2 = Tr((P-I/3)^2) = const (on-slice);  isometric  weighted
                 Sum_a (2/Tr(la^2)) dphi_a (x) dphi_a  proportional to g, anti-blocks 0.
A1-extremal:     Tr(V) = <Sum_a w_a dphi_a(x)dphi_a , r> = <c g, r> = 0 (r traceless) => FS is
                 lambda_1-extremal in the r-direction (delta A[r]=0; no FIRST-order force).
TrackB lemmas:   d/dh of a metric-blind integrand x dvol  and of Vol are PURE-TRACE (kill nothing
                 on TT); a_1 = int R sqrt(g) is the EH IMPORT (named, not native).
"""
import sys, time
sys.path.insert(0,"/Users/ehrlich/scratch/get-physics-done/code")
import sympy as sp
from sympy import cancel, Rational, zeros, Matrix, I
import tensor_probe as TP
import lichnerowicz_response as L

t0=time.time()
def el(): return f"[{time.time()-t0:6.1f}s]"
g=TP.fs_metric(); ginv=TP.fs_metric_inv(g); Gam=TP.christoffel_hol(g,ginv)
Z1,Z2,Z1B,Z2B=TP.Z1,TP.Z2,TP.Z1B,TP.Z2B
# ON-SLICE real points: Z1B=Z1, Z2B=Z2 (real Z1,Z2) -> genuine CP^2 points, P Hermitian
SLICE=[{Z1:Rational(1,2),Z2:Rational(1,3),Z1B:Rational(1,2),Z2B:Rational(1,3)},
       {Z1:Rational(-2,3),Z2:Rational(1,5),Z1B:Rational(-2,3),Z2B:Rational(1,5)},
       {Z1:Rational(3,7),Z2:Rational(-1,4),Z1B:Rational(3,7),Z2B:Rational(-1,4)}]
gm=L._gellmann_directions(); names=[nm for nm,_ in gm]
mats={nm:A for nm,A in gm}
w={nm: Rational(2,1)/cancel((A*A).trace()) for nm,A in gm}   # 2/Tr(la^2): 1 for d1/s/a, 1/3 for d2
print(f"{el()} trace-weights w_a = {{{', '.join(f'{k}:{w[k]}' for k in names)}}}")

# ---------- A1 sphere: |p - I/3|^2 = const on-slice ----------
P=TP.P_chart(); M_emb=(P-Rational(1,3)*sp.eye(3))
sph=cancel((M_emb*M_emb).trace())     # Tr((P-I/3)^2)
vals=[cancel(sph.subs(pt)) for pt in SLICE]
print(f"{el()} A1 sphere: Tr((P-I/3)^2) on-slice = {vals}  (const = 2/3 => lands on the sphere)")

# ---------- A1 isometric: weighted Sum dphi(x)dphi propto g (anti-blocks 0) on-slice ----------
phis={nm:cancel(TP.phi_field(mats[nm])) for nm in names}
Tiso=[zeros(2,2),zeros(2,2),zeros(2,2)]
for nm in names:
    H20,H11,H02=TP.grad_bilinear(phis[nm],simp=TP.together)
    for k,B in enumerate((H20,H11,H02)):
        for a in range(2):
            for b in range(2):
                Tiso[k][a,b]=TP.together(Tiso[k][a,b]+w[nm]*B[a,b])
pt=SLICE[0]
anti0=all(cancel(Tiso[0][a,b].subs(pt))==0 and cancel(Tiso[2][a,b].subs(pt))==0 for a in range(2) for b in range(2))
ratios=set()
for a in range(2):
    for b in range(2):
        gv=cancel(g[a,b].subs(pt))
        if gv!=0: ratios.add(str(cancel(Tiso[1][a,b].subs(pt)/gv)))
print(f"{el()} A1 isometric on-slice: anti-blocks 0? {anti0}; weighted (1,1)/g ratio = {sorted(ratios)} (single => propto g)")
# cross-check at a 2nd on-slice point
ratios2=set()
for a in range(2):
    for b in range(2):
        gv=cancel(g[a,b].subs(SLICE[1]))
        if gv!=0: ratios2.add(str(cancel(Tiso[1][a,b].subs(SLICE[1])/gv)))
print(f"{el()} A1 isometric on-slice pt2: (1,1)/g ratio = {sorted(ratios2)}")

# ---------- A1-extremal: Tr(V) = <Tiso, r> = 0 (r traceless) => FS lambda_1-extremal ----------
print(f"{el()} building r = TT(B3[d1]) ...")
B3=TP.grad_bilinear(phis['d1'],simp=TP.together)
r,wh,wa,f,info=L.extract_tt(B3,g,ginv,Gam,verify=True)
print(f"{el()} extract_tt(d1): div_zero={info.get('div_zero')} tr_zero={info.get('tr_zero')}")
trV=cancel(TP.l2_tensor(Tiso, r, ginv))
print(f"{el()} A1-extremal: Tr(V) = <Sum_a w_a dphi(x)dphi , r> = {trV}  (==0 => delta(lambda_1 Vol^1/2)[r]=0, FS extremal, NO first-order force)")
# also <g, r> directly (should be 0: r traceless)
gtr=(zeros(2,2),Matrix(g),zeros(2,2))
gr=cancel(TP.l2_tensor(gtr, r, ginv))
print(f"{el()} cross-check <g,r> = {gr}  (==0, r traceless; Tr(V)=c<g,r> consistent)")
print(f"{el()} done.")
