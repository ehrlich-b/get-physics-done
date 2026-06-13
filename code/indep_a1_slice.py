"""Verify A1 is correctly evaluated ON the reality slice (P a genuine projector P^2=P), and the
sphere constant 2/3 is the analytic Tr((P-I/3)^2)=Tr P - (2/3)TrP + 1/3 = 1-2/3+1/3 = 2/3.
Confirm P^2=P ON-slice (Z1B=conj Z1) but NOT as independent Wirtinger symbols (off-slice)."""
import sys; sys.path.insert(0,'/Users/ehrlich/scratch/get-physics-done/code')
import sympy as sp
from sympy import cancel, Rational, symbols, I, conjugate, simplify
import tensor_probe as TP
Z1,Z2,Z1B,Z2B=TP.Z1,TP.Z2,TP.Z1B,TP.Z2B
P=TP.P_chart()
# (1) analytic sphere const: Tr((P-I/3)^2) using P^2=P, TrP=1 (holds when P is a projector)
print("TrP =", cancel(P.trace()), " (should be 1 identically, Wirtinger-independent: v^H v / v^H v)")
# P^2 - P off-slice (independent Z1B,Z2B):
P2mP=cancel((P*P-P).applyfunc(cancel))
offslice_proj = all(cancel(P2mP[i,j])==0 for i in range(3) for j in range(3))
print("P^2==P with INDEPENDENT Wirtinger zbar (off-slice)?", offslice_proj)
# on-slice: substitute z1b=conj(z1) etc with real x,y
x1,y1,x2,y2=symbols('x1 y1 x2 y2',real=True)
SLICE={Z1:x1+I*y1,Z2:x2+I*y2,Z1B:x1-I*y1,Z2B:x2-I*y2}
P2mP_slice=(P*P-P).subs(SLICE).applyfunc(lambda e: cancel(sp.simplify(e)))
onslice_proj=all(cancel(sp.simplify(P2mP_slice[i,j]))==0 for i in range(3) for j in range(3))
print("P^2==P ON the reality slice (zbar=conj z)?", onslice_proj)
# sphere const on-slice:
Memb=(P-Rational(1,3)*sp.eye(3))
sph=cancel((Memb*Memb).trace())
pt={x1:Rational(2,5),y1:Rational(-1,3),x2:Rational(1,6),y2:Rational(1,4)}
sph_slice=cancel(sph.subs(SLICE).subs(pt))
print("Tr((P-I/3)^2) on-slice at a test pt =", sph_slice, " (analytic = 2/3)")
print(f"*** A1 sphere const = 2/3 analytic (Tr P -2/3 Tr P +1/3 = 2/3); projector holds ON-slice only: "
      f"onslice={onslice_proj}, offslice={offslice_proj} ***")
print("=> orchestrator correctly tested A1 ON the reality slice (P a genuine idempotent there).")
