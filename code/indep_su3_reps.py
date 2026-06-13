"""Independent SU(3) representation theory check for A4.
Verify: Sym^2(adjoint 8) = 1 + 8 + 27 (27 with multiplicity EXACTLY ONE).
Method: compute the decomposition via SU(3) character theory / weight multiplicities.
8 (x) 8 = 27 + 10 + 10bar + 8 + 8 + 1 (dim 64). Symmetric part Sym^2(8) has dim 8*9/2=36.
Antisymmetric Lambda^2(8) has dim 8*7/2=28. Standard: Sym^2(8)=1+8+27 (1+8+27=36),
Lambda^2(8)=8+10+10bar (8+10+10=28). Verify by dimension AND by the symmetry of each irrep
in the tensor product (which factors are symmetric vs antisymmetric)."""
import sympy as sp
from sympy import Rational, Matrix, zeros, I

# --- SU(3) irreps by Dynkin labels (p,q): dim = (p+1)(q+1)(p+q+2)/2 ---
def dim(p,q): return (p+1)*(q+1)*(p+q+2)//2
reps={'1':(0,0),'3':(1,0),'3bar':(0,1),'6':(2,0),'8':(1,1),'10':(3,0),'10bar':(0,3),
      '27':(2,2),'15':(2,1)}
for nm,(p,q) in reps.items():
    print(f"  dim {nm} (p,q)=({p},{q}) = {dim(p,q)}")
print()
print("8 (x) 8 dim =", 8*8, "= 64")
print("Sym^2(8) dim = 8*9/2 =", 8*9//2)
print("Lambda^2(8) dim = 8*7/2 =", 8*7//2)
print()
# proposed: 8x8 = 27+10+10bar+8+8+1 ; Sym^2 = 27+8+1 ; Lambda^2 = 10+10bar+8
print("Check 8x8 = 27+10+10bar+8+8+1:", dim(2,2)+dim(3,0)+dim(0,3)+dim(1,1)+dim(1,1)+dim(0,0), "(==64?)")
print("Check Sym^2(8) = 1+8+27:", dim(0,0)+dim(1,1)+dim(2,2), "(==36?)")
print("Check Lambda^2(8) = 8+10+10bar:", dim(1,1)+dim(3,0)+dim(0,3), "(==28?)")
print()
# Multiplicity of 27 in Sym^2(8): is it exactly 1? The 27 appears ONCE in 8x8 total.
# Since 27 appears once in 8x8, and 8x8 = Sym^2 (+) Lambda^2, 27 is in exactly one of them.
# 27=(2,2) is the highest weight 2*(adjoint h.w.)=(2,2): the Cartan square of the highest root,
# which is SYMMETRIC (the leading term of Sym^2). So 27 in Sym^2 with multiplicity 1. Confirm via
# the highest-weight count below.
print("="*60)
print("RIGOROUS: multiplicity of 27=(2,2) in 8x8 via weight-multiplicity (Brauer/Klimyk),")
print("then its location in Sym^2 vs Lambda^2 by the highest-weight symmetry.")
print("="*60)

# Build the weights of the adjoint 8 explicitly (su(3) roots + 2 zero weights for Cartan).
# Use the standard root system in the (alpha1,alpha2) simple-root basis -> express weights in the
# fundamental-weight (Dynkin) basis. Roots of su(3): +/-alpha1, +/-alpha2, +/-(alpha1+alpha2),
# plus two zero weights (rank 2 Cartan). Dynkin labels of a root = (<root,alpha1^v>,<root,alpha2^v>)
# Cartan matrix A=[[2,-1],[-1,2]]. Simple roots in Dynkin basis: alpha1=(2,-1), alpha2=(-1,2).
A=Matrix([[2,-1],[-1,2]])
a1=(2,-1); a2=(-1,2); a12=(1,1)   # alpha1+alpha2 in Dynkin labels = a1+a2=(1,1)
adjoint_weights=[a1,a2,a12,(-a1[0],-a1[1]),(-a2[0],-a2[1]),(-a12[0],-a12[1]),(0,0),(0,0)]
print("adjoint(8) weights (Dynkin):",adjoint_weights, " count=",len(adjoint_weights))

# tensor product weight multiplicities: all pairwise sums
from collections import Counter
prod=Counter()
for w1 in adjoint_weights:
    for w2 in adjoint_weights:
        prod[(w1[0]+w2[0], w1[1]+w2[1])]+=1
print("total weights in 8x8:", sum(prod.values()), "(==64?)")
# highest weight (2,2) multiplicity in the product:
print("multiplicity of weight (2,2) in 8x8 =", prod[(2,2)], "(highest weight of 27; ==1 => 27 once)")

# Now Sym^2 weight multiplicities: for w1<=w2 ordered pairs plus the diagonal counted once.
# Sym^2 multiplicity of a weight mu = (#pairs(w1,w2) unordered with w1+w2=mu, w1!=w2)
#                                    + (#weights w with 2w=mu).
# We must respect that the 8 has TWO identical zero weights (treat as 2 distinct basis vectors e_a,e_b).
wlist=adjoint_weights  # 8 vectors, indices 0..7 (two zero-weight vectors index 6,7)
symc=Counter(); antc=Counter()
for i in range(8):
    for j in range(i,8):
        mu=(wlist[i][0]+wlist[j][0], wlist[i][1]+wlist[j][1])
        symc[mu]+=1            # i<=j -> symmetric basis element e_i e_j (i=j included)
for i in range(8):
    for j in range(i+1,8):
        mu=(wlist[i][0]+wlist[j][0], wlist[i][1]+wlist[j][1])
        antc[mu]+=1            # i<j -> antisymmetric
print("Sym^2 total dim:", sum(symc.values()), "(==36?)  Lambda^2 total:", sum(antc.values()), "(==28?)")
print("Sym^2 multiplicity of weight (2,2):", symc[(2,2)], "(==1 => 27 in Sym^2 once)")
print("Lambda^2 multiplicity of weight (2,2):", antc[(2,2)], "(==0 => 27 NOT in Lambda^2)")

# Confirm 27 multiplicity in Sym^2 by subtracting lower irreps (Kostant): the count of h.w.(2,2)
# in Sym^2 is the multiplicity of the IRREP 27 in Sym^2 (highest weight has irrep-mult = weight-mult
# minus contributions from higher irreps; (2,2) is the top, so weight-mult == irrep-mult).
print()
print(f"*** Sym^2(8) contains 27 with multiplicity EXACTLY {symc[(2,2)]} ***")
print(f"*** => A4 claim (image of Q_A carries 27 once) rep-theory: CONFIRMED ({symc[(2,2)]}==1) ***")
