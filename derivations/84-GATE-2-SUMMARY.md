# 84 — GATE 2 SUMMARY: THE TEST — the landscape of structured states

**v24.0 Gate 2 (decisive). Exact over Q. VERDICT = LIVE.**
Driver `code/variety_entropy_landscape.py`; 12/12 checks PASS in 7.4 s. Independently
cross-checked orchestrator-side via the 27×27 spectral-projector compression path
(exact match at all sample t) and by the from-scratch gpd-verifier.

## Verdict object

For each (state X, family p(t)), the face purity
    r(t) = det(ρ_face(p(t))) = det_2(C_p X)/Tr(C_p X)²   (exact rational function over Q).
`r(t)` constant ⟺ S_X(p) constant ⟺ DEAD; `r(t)` non-constant ⟺ LIVE.

## Test states (guard #1)

| state | det_3 | full-rank | dim Stab_{F_4} |
|---|---|---|---|
| GENERIC (decisive) | 696029/6720 > 0 | yes | 28 |
| v18-matter (V_{1/2} only) | 1388171/58800 > 0 | yes | 28 |
| diagonal (special) | 105 > 0 | yes | 28 |
| I/3 (vacuum) | — | — | 52 (= all of F_4) |

Every regular X has Stab ≅ Spin(8) (dim 28) — the stabilizer of its eigenframe; this
is generic, NOT a vacuity flag. The operative guard is **transversality**: the
families move E_11, and for X_gen the eigenframe is NOT the standard E_ii frame, so
the families are transverse to Stab(X_gen)-orbits. The non-vacuity witness is the
diagonal-vs-generic contrast below.

## THE RESULT — r(t) VARIES for the generic state (LIVE)

For X_gen, r(t) is non-constant along **all four** families, and the three (0,1)-entry
families give **different** rational functions — the landscape **resolves the octonion
/ Peirce direction of the matter**:

- off-u(e_1):  r(t) = (658836 t⁸ + 189420 t⁷ + 3688475 t⁶ + … + 658836) / (2822400 t⁸ + 940800 t⁷ + 17012800 t⁶ + … + 2822400)
- C_u-phase(e_7):  r(t) = (658836 t⁸ + 66570 t⁷ + 3688475 t⁶ + … + 658836) / (2822400 t⁸ + 352800 t⁷ + 16945425 t⁶ + … + 2822400)
- transverse-real:  r(t) = (658836 t⁸ + 3688475 t⁶ + 6059278 t⁴ + 3688475 t² + 658836) / (2822400 t⁸ + 16934400 t⁶ + 31046400 t⁴ + …) — even (no odd powers)

(Sample values, exact: off-u r(2)=2727493/12700800, r(3)=8878651/40043584,
r(5)=83558976059/366799809600; C_u-phase r(2)=5270711/24354225, r(3)=503003/2252432.
Both Tr and det_2 vary; the purity r varies.)

## Non-vacuity witness — diagonal vs generic (bug-guard #1)

For the **diagonal** state diag(7,5,3), the three (0,1)-entry families give the
**IDENTICAL** function
    r(t) = (15 t⁸ + 84 t⁶ + 138 t⁴ + 84 t² + 15) / (64 t⁸ + 384 t⁶ + 704 t⁴ + 384 t² + 64)
— the landscape is **octonion-direction-blind** (the large effective symmetry of a
diagonal state can't tell e_7 from e_0 from e_1). The **generic** state breaks this
degeneracy (three distinct r(t)). This proves the LIVE variation is genuine matter
content, not a stabilizer-orbit artifact: matter is what resolves the directions.

## Critical-point structure (the landscape's shape)

dr/dt = 0 along each generic-state family:
- transverse-real: t ∈ {−1, 0, 1} — exactly the standard frame (t=0→E_11, t=±1→E_22).
- C_u-phase(e_7), off-u(e_1): roots of degree-8 polynomials (CRootOf) — **generic
  positions tracking the matter's rotated eigenframe**, NOT the standard frame.

So the landscape's critical points follow the **state's own eigenframe/Peirce data**
(the natural conjecture in the prompt): for the real direction the matter happens to
leave the standard frame critical, but along the genuinely matter-coupled directions
(e_7, e_1) the critical points move to where p aligns with X_gen's rotated eigen-
idempotents.

## Flattening — I/3 is the unique homogeneous point (the claim's uniqueness half)

Along X_t = (1−t)·I/3 + t·X_gen (off-u probe family, leading sensitivity dr/ds|_0):

| t | dr/ds\|_0 (landscape gradient at E_11) |
|---|---|
| 0 | **0** (and d²r/ds²\|_0 = 0) |
| 1/4 | 13879/1837500 |
| 1/2 | 102021/10765300 |
| 3/4 | 2548557/248199700 |
| 1 | 629/58800 |

The landscape variation **vanishes exactly at t=0** (X_0 = I/3, the whole family is
flat, r≡1/4) and **grows monotonically with matter**. The vacuum is the homogeneous
point of the family; matter shapes the field, and the more matter, the more landscape.

## Bug-guards (all held)

1. **stabilizer vacuity** — non-vacuity witnessed by the diagonal-blind vs
   generic-resolving contrast; families move E_11, transverse to Stab(X_gen).
2. **special-family artifact** — variation along all independent families incl. the
   **off-u** one; not a single-family accident.
3. **normalization** — full-rank states ⟹ Tr(C_p X) > 0 along families (proper
   rational r, no pole hit).
4. **u-alignment of maps** — N/A (each face computed independently; no face-to-face
   transposition maps).
5. **numeric leakage** — verdict is r(t) constancy over Q; zero float entropy on the
   decisive path. verdict() is non-hardwired (self-test: const→DEAD, varying→LIVE).

## VERDICT — LIVE

Over the primitive-idempotent variety OP², **matter shapes a non-trivial scalar field
(the face-entropy / purity landscape)**: r(p) is non-constant for generic structured
full-rank X — and the landscape resolves the octonion/Peirce direction of the matter —
while the faithful state I/3 is the **unique homogeneous point**, with the landscape
flattening exactly there and growing with matter. For the first time the program has
matter shaping a field over a geometry-bearing space of many points (the algebra's own
event-space) — the **first ingredient of the base/format object**.

## Anti-overclaim (binding scope)

LIVE ≠ a metric, ≠ geometry-from-entanglement, ≠ J5, ≠ Einstein, ≠ the base/format
object built. It establishes EXACTLY: "matter shapes a non-trivial scalar field over
the algebra's native many-point space, whose homogeneous point is the faithful state."
The signature question (variety Riemannian; spacetime Lorentzian) is untouched and
stays an open fence. Borel/Liu/bottleneck math imported as math; GST-era roles retired.
Compactness/cosmology out of scope. DEAD-at-family-level ≠ DEAD on all of OP² — three
guard-1-clean independent families (incl. off-u) is the registered evidence standard
for this gate; full-variety universality is not claimed. No κ, no Λ, no G=κT.

Gate 3 (geometry contact — ∇S critical structure vs the canonical Borel geometry) is
LIVE-only exploratory and NON-BLOCKING: the critical-point structure above (eigenframe-
tracking, generic positions off the standard frame) is the curiosity it feeds, with NO
law/balance/fixed-volume claims attached.
