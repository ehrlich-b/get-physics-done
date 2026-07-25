# GPD Prompt — The Entropy Landscape on the Idempotent Variety (the base-route's first gate)

**Slot 84 / v24.0-candidate. STATUS: RATIFIED-BY-REQUEST (Bryan: "I need a
prompt," 2026-06-10, following the variety-route exploration). Ready to run.**

_Context (blog repo): `research/gr-from-h3o/entanglement-route.md` (v23.0
DEAD §11 — the fiber has no Jacobson vacuum, degree-independent; the route
is gated on the base/format object) + the variety-route exploration (the
base candidate = the algebra's own idempotent variety). Recorded math this
run leans on: {rank-1 idempotents} = F_4/Spin(9) = OP², dim 16
(`h3o-math-library.md:100`); OP² is a compact Einstein manifold (Borel
1950); CP² = SU(3)/U(2) is 4-dim, Einstein, totally geodesic in OP² (Liu
1998; the recorded bottleneck chain OP² → C*-bottleneck → CP²). The
GST-era ROLE claims for these objects are RETIRED — their math is imported
as math; no GST narrative. Correction for this session's framing: the
claim-2 (J4 thermal-time) design blocker is RESOLVED (referent-free
consistency design, slot-83 prompt appendix) — it is a separate,
already-pinned run, not blocked; do not conflate with this one._

_Discipline: v21-v23 pattern — executor + independent verifier (separate
code path), exact over Q, fail-fast gates, pre-registered failure modes,
one sharp claim. No κ, no Λ, no G = κT anywhere. v23's face-entropy
machinery and the v22 u-aligned rotation generators are the starting
assets._

## The claim (sharp, falsifiable)

> Over the primitive-idempotent variety (the algebra's native space of
> observer-positions), the face-entropy function
> **S_X(p) = S(ρ_face(p))**, ρ_face(p) = C_p(X)/Tr(C_p(X)) on the rank-2
> complement face of p, is a **NON-TRIVIAL LANDSCAPE for generic
> structured (matter-bearing, full-rank) states X** — matter shapes a
> scalar field over the event-space — while the faithful state I/3 has a
> **HOMOGENEOUS (constant) landscape** ("vacuum = homogeneity over the
> variety"), and on interpolating families the landscape flattens exactly
> at I/3.

DEAD and LIVE both informative:
- **DEAD** (the landscape is constant for generic structured X): matter
  does NOT shape any structure over the variety; the variety route's
  first ingredient fails; the base-candidate dies its cheap death and the
  route goes to the fork-A annex.
- **LIVE** (non-constant with computable structure): the program has, for
  the first time, **matter shaping a field over a geometry-bearing space
  of many points** — the first ingredient of the base/format object, on
  the algebra's own event-space. Report the landscape's structure
  (critical points vs the state's eigenframe/Peirce data).

## The exact verdict criterion (mandatory — no numerics in the verdict)

S_X(p) is constant in p **iff the spectrum of ρ_face(p) is
p-independent** iff the coefficients of the characteristic polynomial of
ρ_face(p) are constant along the family. **All verdicts via char-poly
coefficient constancy, exact over Q** (entropies involve logs of
algebraic eigenvalues — numerical S values may be reported as
illustration only, never as the verdict).

## Setup

- h_3(O) over Q, octonion conventions as v17-v23 (u = e_7).
- Faces: for rank-1 idempotent p, the rank-2 complement face V_2(1−p);
  ρ_face(p) = the compression of X, normalized. Domain: FULL-RANK states
  X only (det > 0, interior of the cone) so ρ_face(p) is well-defined for
  all p; flag any normalization degeneracies along families.
- Variety families (Gate 0 builds them): rational one-parameter families
  of rank-1 idempotents through E_11 — at minimum (i) the v22 u-aligned
  C_u-phase circle, (ii) at least one family TRANSVERSE to it, (iii) at
  least one family leaving the u-aligned locus (to compare on- vs
  off-bottleneck). Rank-1 condition p∘p = p, Tr p = 1 enforced exactly.

## Gates

### Gate 0 — families + the bottleneck tangent count

Build the rational idempotent families (above) with exactness checks.
Compute the TANGENT DIMENSION of the u-aligned rank-1 locus at E_11
(linearize p∘p = p, Tr p = 1, u-alignment): **pre-registered expectation
= 4 if the recorded OP² → CP² bottleneck chain governs here** — but
derive it; any value is informative (4 confirms the recorded 4d cut in
this context; ≠ 4 means the bottleneck reduction does NOT govern the
entanglement-route's event-space and the recorded chain's new role is
falsified at the first hurdle). Fail-fast if the families can't be built
exactly.

### Gate 1 — vacuum-homogeneity calibration (must pass; zero evidential weight)

Verify the char-poly of ρ_face(p) for X = I/3 is constant along ALL
families (F_4-invariance guarantees it; S ≡ log 2). This is the
calibration tautology, pre-registered as such.

### Gate 2 — THE TEST: the landscape of structured states

Pre-registered states: the v18 matter configs (recorded rational
structured states) + at least one GENERIC full-rank rational X (generic =
verify its F_4-stabilizer is trivial/small FIRST — see guard 1). Compute
the char-poly coefficients of ρ_face(p) along all families:

- constant for generic X ⇒ **DEAD** (matter shapes nothing over the
  variety).
- non-constant ⇒ **LIVE**: report which coefficients vary, the critical
  points of the leading varying coefficient along each family, and
  whether the critical points align with X's eigenframe (the natural
  conjecture: the landscape's critical points = the state's own Peirce
  frame). Then the FLATTENING check: on the interpolation
  X_t = (1−t)·I/3 + t·X_structured, verify the landscape's variation
  vanishes exactly at t = 0 and grows with t (the vacuum is the
  homogeneous point of the family — the claim's uniqueness half at
  family level; full uniqueness is NOT claimed).

### Gate 3 — geometry contact (exploratory, NON-BLOCKING)

Where the landscape is nontrivial: along each family, compare ∇S's
critical structure with the canonical (Borel) geometry restricted to the
family (e.g., are critical points at canonical-metric-distinguished
positions?). Tagged curiosity feeding the J5-on-the-variety follow-up. NO
law-claims, no balance-claims, no fixed-volume machinery in this run.

## Pre-registered failure modes (bug guards)

1. **Invariance/stabilizer vacuity:** S_X(g·p) = S_{g⁻¹·X}(p) — a state
   with a LARGE F_4-stabilizer can show constancy along stabilizer-orbit
   families without any content. Compute/bound the stabilizer of each
   test state FIRST; choose families transverse to it; DEAD requires
   constancy for GENERIC X along TRANSVERSE families.
2. **Special-family artifact (the dual trap):** constancy along ONE
   family ≠ constancy on the variety. DEAD needs constancy along all
   independent families incl. the off-u one; LIVE needs variation along
   at least one family that survives guard 1.
3. **Normalization degeneracies:** Tr C_p(X) must stay bounded away from
   0 along families (full-rank X should ensure it; verify, don't assume).
4. **u-alignment bookkeeping (the v22 lesson):** off-u families are
   ALLOWED here (Gate 0(iii) explicitly leaves the aligned locus), but
   any face-to-face MAPS used must be u-aligned; bare frame
   transpositions carry the antiholomorphic conjugation.
5. **Numeric leakage:** the verdict is char-poly constancy over Q.
   Any gate whose verdict rests on floating-point entropy values is
   void.

## Anti-overclaim (binding scope)

LIVE ≠ a metric, ≠ geometry-from-entanglement, ≠ J5, ≠ Einstein, ≠ the
base/format object built. It establishes exactly: "matter shapes a
nontrivial scalar field over the algebra's native many-point space, whose
homogeneous point is the faithful state." The signature question
(variety is Riemannian; spacetime is Lorentzian) is untouched and stays
an open fence. The Borel/Liu/bottleneck math is imported as math; the
GST-era roles stay retired. Compactness/cosmology out of scope. DEAD at
the family level ≠ DEAD on all of OP² — but say so once, without
inflating (three independent families with guard-1 hygiene is the
registered evidence standard for this gate).

## Deliverables

- derivations/84-* (families + tangent count; calibration; the
  char-poly tables per state × family; verdict).
- code/variety_entropy_landscape.py (executor, exact/Q); independent
  verifier on a separate code path (at minimum: re-derive the tangent
  count independently + re-verify Gate 2's verdict on one state × family
  via a different parametrization).
- One-paragraph verdict: DEAD / LIVE(structure), with the Gate-0 tangent
  count and the flattening-check result stated separately.
