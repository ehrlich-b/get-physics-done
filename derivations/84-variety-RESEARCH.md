# 84 — The Entropy Landscape on the Idempotent Variety (v24.0): setup & method

**Milestone v24.0, pre-flight fail-fast gated test.** Source of truth:
`paper6-variety-entropy-landscape-prompt.md` (RATIFIED-BY-REQUEST, Bryan
2026-06-10). Driver: `code/variety_entropy_landscape.py`. Exact over Q.

## Why this milestone

v23.0 (the two-term Jacobson balance, fiber side) returned **DEAD at degree ≤ 3**
with the *fiber-side scope theorem*: the second/geometric Jacobson term does NOT
live on the h_3(O) fiber at low degree — "the entanglement route is fully gated on
the **base/format object**." v24.0 attacks that base object's **first gate**: does
matter even shape a non-trivial *structure over the algebra's native event-space*
before any metric/format question is asked?

## The event-space

The primitive-idempotent variety = {rank-1 idempotents p of h_3(O) : p∘p=p, Tr p=1}
= F_4/Spin(9) = **OP²** (the octonionic projective plane, dim 16; compact Einstein,
Borel 1950). This is the algebra's own "space of observer-positions." The recorded
bottleneck chain OP² → C*-bottleneck → CP² (CP²=SU(3)/U(2), 4-dim, Einstein, totally
geodesic in OP², Liu 1998) predicts a 4-dim u-aligned cut.

## The face object (general, exact)

For a rank-1 idempotent p, the **rank-2 complement face** is the Peirce-0 subalgebra
V_0(p) ≅ h_2(O) (the rank-2 Jordan algebra with unit 1−p). The face state is the
normalized compression
    ρ_face(p) = C_p(X) / Tr(C_p(X)),   C_p X = P_0(p)·X.
Since L_p has eigenvalues {0, ½, 1}, the Peirce-0 spectral projector is the matrix
polynomial P_0 = 2 L_p² − 3 L_p + 1, so
    **C_p X = 2 (p∘(p∘X)) − 3 (p∘X) + X**     (two nested Jordan products — no 27×27
matrix needed; fully symbolic over Q(t) along families).
ρ_face is a rank-2 (spin-factor) state; its char-poly is λ² − λ + det(ρ_face), so the
single nontrivial coefficient is the **face purity**
    **r(p) := det(ρ_face) = det_2(C_p X) / Tr(C_p X)²**,
    det_2(Y) = (Tr(Y)² − Tr(Y∘Y))/2   (rank-2 generic norm of Y ∈ V_0(p)).

## The exact verdict criterion (NO numerics — bug-guard #5)

    S_X(p) constant in p
      ⟺ spectrum of ρ_face(p) p-independent
      ⟺ char-poly coefficients of ρ_face(p) constant
      ⟺ r(p) constant (as a rational function of the family parameter, over Q).
Entropies S = −Σ λ log λ (logs of algebraic eigenvalues) are reported as ILLUSTRATION
ONLY; the verdict rests entirely on the rational function r(t). (S is a strictly
monotone function of r for a 2-level state, so r varies ⟺ S varies.)

## Families (rational, exact, through E_11)

p(t) = v(t) v(t)*, v=(v_0,v_1,v_2) in a common associative subalgebra span{1,e_k}
(so p is an exact rank-1 idempotent of h_3(span{1,e_k})). Rotate E_11 (index 0)
toward E_jj along the e_k direction of the (0,j) entry: v_0=c, v_j=s·e_k,
(c,s)=((1−t²)/(1+t²), 2t/(1+t²)) (Pythagorean → rational). At t=0, p=E_11.

| family | (j,k) | kind | tangent direction |
|---|---|---|---|
| u-aligned C_u-phase | (1, e_7=u) | u-aligned | C_u-imaginary of (0,1) |
| transverse-real | (1, e_0) | u-aligned | real of (0,1) (⊥ to phase) |
| off-u | (1, e_1) | **off-u** | e_1 of (0,1) (leaves h_3(C_u)) |
| E_33-real | (2, e_0) | u-aligned | real of (0,2) |

Three independent guard-1-clean families (two u-aligned + one off-u) = the registered
evidence standard for this gate.

## Conventions / engines

- det / cubic-norm SSOT = `ring_lemma_verification.det_3`; `octonion_algebra` BANNED.
- u = e_7; C_u = span{1, e_7}; coord layout α=0, β=1, γ=2, x1=3..10 (V_0 octonion),
  x2=11..18, x3=19..26 (V_{1/2}); V_1(E_11)={0}, V_0(E_11)={1..10}=h_2(O),
  V_{1/2}(E_11)={11..26}.
- Exact over Q (and Q(t) along families). No κ, no Λ, no G=κT anywhere.

## Bug-guards (binding)

1. **stabilizer vacuity** — S_X(g·p)=S_{g⁻¹X}(p); a large-stabilizer state can show
   constancy along stabilizer-orbit families without content. Families MOVE E_11 and
   are transverse to the E_11-fixing part of any stabilizer; the diagonal-vs-generic
   contrast (item Gate 2) is the non-vacuity witness.
2. **special-family artifact** — DEAD would need constancy along ALL independent
   families incl. the off-u one; LIVE needs variation surviving guard 1.
3. **normalization** — Tr C_p(X) bounded away from 0 (full-rank X ⟹ positive face).
4. **u-alignment of maps** — N/A: each p's face is computed independently; no
   face-to-face transposition maps (no antiholomorphic-conjugation issue).
5. **numeric leakage** — the verdict is r(t) constancy over Q; no float entropy on the
   decisive path.

## Anti-overclaim (binding)

LIVE ≠ a metric, ≠ geometry-from-entanglement, ≠ J5, ≠ Einstein, ≠ the base/format
object built. It establishes EXACTLY: "matter shapes a non-trivial scalar field over
the algebra's native many-point space, whose homogeneous point is the faithful state."
The signature question (variety Riemannian; spacetime Lorentzian) is untouched and
stays an open fence. Borel/Liu/bottleneck math imported as math; GST-era roles retired.
DEAD-at-family-level ≠ DEAD on all of OP².
