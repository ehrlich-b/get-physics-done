"""ATTACK 2 — clean multiplicity of 27 via the standard fact:
mult of irrep (a,b) in a rep = (mult of the dominant weight (a,b))
                             - sum over higher dominant weights mu>lambda of [mult_lambda in irrep(mu)].
For the HIGHEST dominant weight present, mult of the irrep = mult of that weight (no corrections).
(2,2) is the highest weight in Sym^2(8) and 8x8 (since 8x8 max is 16=2+2+...; (2,2)=Dynkin gives
the 27 which is the largest irrep). So mult_27 = mult of the weight with Dynkin (2,2).

Dynkin (a,b) <-> diagonal weight (h1,h2,h3): a=h1-h2, b=h2-h3, sum h=0 (su3). The (2,2) Dynkin
highest weight has h-differences (2,2). In our (h1,h2,h3) basis with FIXED sum = sum of the two
adjoint weights' sums. We just find, in each rep's weight dict, the dominant weight whose
(h1-h2, h2-h3) = (2,2), and report its multiplicity. That IS the 27 multiplicity (it's the top).
"""
from collections import defaultdict
def gt_patterns(top):
    l1,l2,l3=top; out=[]
    for m1 in range(l2,l1+1):
        for m2 in range(l3,l2+1):
            for k in range(m2,m1+1): out.append((l1,l2,l3,m1,m2,k))
    return out
def weight_of(p):
    l1,l2,l3,m1,m2,k=p; return (k, m1+m2-k, l1+l2+l3-(m1+m2))
def wmult(a,b):
    mm=defaultdict(int)
    for p in gt_patterns((a+b,b,0)): mm[weight_of(p)]+=1
    return mm
w8=[w for w,m in wmult(1,1).items() for _ in range(m)]
def add(u,v): return tuple(x+y for x,y in zip(u,v))
sym=defaultdict(int); ten=defaultdict(int); alt=defaultdict(int)
for i in range(8):
    for j in range(8):
        s=add(w8[i],w8[j]); ten[s]+=1
        if i<j: sym[s]+=1; alt[s]+=1
        elif i==j: sym[s]+=1
def top_dynkin_mult(wm, dyn):
    # find dominant weights, identify the one with Dynkin == dyn and maximal (h1-h3)
    best=None
    for w,m in wm.items():
        if m<=0: continue
        if w[0]>=w[1]>=w[2]:
            d=(w[0]-w[1], w[1]-w[2])
            if d==dyn:
                if best is None or (w[0]-w[2])>best[0]:
                    best=(w[0]-w[2], m, w)
    return best
for name,wm in [("8x8",ten),("Sym^2(8)",sym),("Lambda^2(8)",alt)]:
    b=top_dynkin_mult(wm,(2,2))
    print(f"{name}: 27=(2,2) appears with multiplicity {b[1] if b else 0}  (weight {b[2] if b else None})")
# also report the FULL dominant-weight spectrum (mult of each dominant weight) for transparency
print("\nDominant weight multiplicities (Dynkin: count) in Sym^2(8):")
dom=defaultdict(int)
for w,m in sym.items():
    if w[0]>=w[1]>=w[2] and m>0: dom[(w[0]-w[1],w[1]-w[2])]=m
for d,m in sorted(dom.items()): print(f"  Dynkin {d}: weight-mult {m}")
