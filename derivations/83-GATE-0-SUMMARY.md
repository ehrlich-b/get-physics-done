# Slot 83 / v23.0-candidate — GATE 0 SUMMARY (one screen)

**The Two-Term Balance Question (Jacobson J5, fiber side) — Gate 0: the invariant
candidate space + face machinery.** Status: **COMPLETE — ALL_PASS, ring CLOSES at
degree 3.** Gates 1/2/3 NOT run (fail-fast; orchestrator routes the next gate).

Exact over Q (entropy/log symbolic). No κ, no Λ, no G = κT. det SSOT =
`ring_lemma_verification.det_3`; `octonion_algebra` banned; u = e_7. Driver:
`code/entanglement_two_term.py` (source-guarded, self-tested, ~5 s).

---

## Spin(9) Peirce decomposition (Stab_{F_4}(E_11), dim 36; exact, irreducibility certified)

```
   h_3(O) = 27  under  Spin(9) :
     V_1   =  1            trivial   — direction  α  (coord 0)
     V_0   =  1  ⊕  9      trivial = β+γ trace ; vector 9   (commutant dim = 1)
     V_{1/2} =  16          spinor                            (commutant dim = 1)
```

36 spin(9) generators act block-diagonally; trivial dirs = **α** and **(β+γ)**.

## THE CANDIDATE-A LIST — exhaustive ≤deg-3 Spin(9)-invariant ring

Invariant Hilbert function `(deg 0,1,2,3) = (1, 2, 5, 9)` — each dim is the
derivation-kernel dimension, two-prime certified; explicit generators **span** the
kernel at every degree.

| deg | new generators (exact forms) | + reducible products |
|-----|------------------------------|----------------------|
| 1 | `α` ; `Tr_{V_0} = β+γ`  (≡ `Tr=α+β+γ`, `α`) | — |
| 2 | `Q_vector = |9|² = Σ_{3..10}c² − βγ` ; `Q_spinor = |16|² = Σ_{11..26}c²` | `α², α·Tr_{V_0}, Tr_{V_0}²` |
| 3 | **`det_3`** (cubic norm SSOT; F_4-inv ⇒ Spin(9)-inv) | `deg1 × deg2` (span 8) |

**Minimal generating set:** `{ α, Tr_{V_0}, Q_vector, Q_spinor, det_3 }` (degrees
1,1,2,2,3). Every native face-functional of degree ≤ 3 is a polynomial in these.

**Key structural finding:** the spinor–vector–spinor `16 × 9 × 16 → R` Γ-coupling is
**NOT an independent generator** — it is the cross-term content of `det_3` (coefficient
−1/2). The fiber carries no separate cubic Yukawa; the only cubic invariant is `det_3`.

## FACE CONVENTION (pinned; bug-guard #4 satisfied)

```
   ρ_face(X) = C_p(X) / Tr(C_p(X))      — COMPRESS FIRST, NORMALIZE SECOND.
```
`C_p` = projection onto `V_1(p) = h_k(O)` (the corner); `S_face` = von Neumann entropy.

- **rank-1 face** `p=E_11`: corner = scalar α ⇒ `S ≡ 0` (TRIVIAL).
- **rank-2 face** `q=E_22+E_33`: corner = `h_2(O)` block `[[β,x1],[x1*,γ]]`,
  `λ_± = (β+γ)/2 ± √(((β−γ)/2)² + |x1|²)`. **⟹ the MEANINGFUL face.**
- tangents: rank-1 = `{0}`; rank-2 = `{1..10}` (10-dim `h_2(O)`); rank-2 compression
  KILLS `{0}=α` and `{11..26}=x2,x3`.

## I/3 VERIFICATION (X = h3o_identity()/3)

| face | ρ_face at I/3 | S_face at I/3 |
|------|---------------|----------------|
| rank-1 | density 1 | **0** (trivial) |
| rank-2 | maximally mixed `I_2/2`, eigs `(1/2,1/2)` | **log 2** |

Bug-guard #4: along both face directions `S_face = log 2 − (9/2)t² + O(t³)`,
`dS/dt|_0 = 0` — **no spurious linear criticality**; clean 2nd-order Fisher form (coeff
−9/2, no log). Set up so Gate 2 can use `δ²S ∝ −Tr(h²)` directly (§8.1; the state-side
copy of v17's Fisher–Bures object, §8.5).

## FAIL-FAST STATUS

**PASS — the Spin(9)-invariant ring closes cleanly at degree 3** (generators span the
kernel at every degree; deg-3 explicit span = kernel dim = 9; no anomalous kernel dim).
The fail-fast boolean is DERIVED from the computed kernel dims + span ranks (not
hardcoded). **PROCEED to next gate** (orchestrator routes Gate 1).

## SCOPE

Gate 0 establishes WHAT A can be + pins the face/entropy convention. It does NOT test
the two-term balance (Gate 2), does NOT claim λ≠0 forced, makes NO Einstein/J5 claim.
LIVE/DEAD undecided until Gate 2.
