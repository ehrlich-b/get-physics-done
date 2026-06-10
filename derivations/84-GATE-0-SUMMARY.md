# 84 — GATE 0 SUMMARY: families + the bottleneck tangent count

**v24.0 Gate 0. Driver: `code/variety_entropy_landscape.py`. Exact over Q. PASS.**

## Families built (exact over Q(t))

Four rational one-parameter families of rank-1 idempotents through E_11, each
verified `p∘p = p`, `Tr p = 1`, `p(0) = E_11` symbolically over Q(t):

| family | (j,k) | kind | result |
|---|---|---|---|
| u-aligned C_u-phase(e_7) | (1, 7) | u-aligned | PASS |
| transverse-real | (1, 0) | u-aligned | PASS |
| off-u(e_1) | (1, 1) | **off-u** | PASS |
| u-aligned E_33-real | (2, 0) | u-aligned | PASS |

Construction: p = v v* with v in span{1,e_k}³ (associative ⟹ exact idempotent),
v_0=c, v_j=s·e_k, (c,s)=Pythagorean((1−t²)/(1+t²), 2t/(1+t²)). Fail-fast gate
cleared (all families exact).

## Tangent dimension at E_11 (the bottleneck count)

**FULL variety tangent = 16.** Linearizing p∘p=p at p=E_11+εH gives L_{E_11}H = ½H
⟹ H ∈ V_{1/2}(E_11); Tr p=1 ⟹ Tr H=0 (automatic on V_{1/2}). Computed as
nullspace(L_{E_11} − ½I) = dim **16** = V_{1/2}(E_11) = coords {11..26}. (This is the
tangent to OP² = F_4/Spin(9), dim 16. ✓)

**u-ALIGNED locus tangent = 4.** The u-aligned locus = rank-1 idempotents of
h_3(C_u) (C_u=span{1,e_7}) = **CP² = SU(3)/U(2)** ⊂ OP². Its tangent at E_11 =
V_{1/2}(E_11) ∩ h_3(C_u) = the (0,1) and (0,2) entries restricted to span{1,e_7} =
2 entries × 2 real-dim = **4**, at coords **{11, 18, 19, 26}** (the e_0 and e_7 slots
of the two V_{1/2} octonion blocks).

> **PRE-REGISTERED 4 — CONFIRMED.** The recorded OP² → CP² bottleneck cut (CP²
> 4-dim, Einstein, totally geodesic in OP², Liu 1998) **governs** the
> entanglement-route event-space. (≠ 4 would have falsified the recorded chain's
> new role at the first hurdle; the computed value is 4.)

Cross-consistency: the C_u-survivor index set {11,18,19,26} is exactly the v18/v19
C_u² coframe survivor set — the same 4 real directions the Cartan/orientation
milestones isolated, now re-derived as the CP² tangent. Independently re-derived by
the verifier via a different method (restrict L_{E_11} to the 9-dim h_3(C_u) and
count the ½-eigenspace → 4).

## Gate 0 verdict

Families exact + FULL tangent 16 + u-aligned tangent 4 (pre-registered confirmed).
Gate 0 PASS — proceed to Gate 1.
