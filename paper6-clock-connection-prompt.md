# GPD Prompt — The Clock Connection: Matter-Sourced Curvature on the Gluing U(1)? (the form-selection fork, run constructively)

**Slot 90 / v30.0-candidate. STATUS: RATIFIED-BY-STANDING-DIRECTIVE
(Bryan, 2026-06-11/12). Ready to run.**

_Context: v29.0 COMPLETE (commit 73f261f6) — thermal time is
irreducibly face-local; the obstruction is the matter-pinned
clock-twist field (the level-2 part of
K_face⁽²⁾ = −(9/2)⟨M,p⟩·traceless(C_pM)). This run executes the
Block-A design pass's output: cast the twist into honest CONNECTION
data and ask whether matter forces CURVATURE on the v22/v28 gluing
U(1). Certified assets consumed: the v28 generator D = [dU,·]
(spectrum {0:9, ±i:1, ±i/2:8}; D restricted to any face = the
SLICE-ROTATION generator — the type-cast's canonical ingredient); the
v29 perturbative machinery (X = I/3 + εM, the ε-graded K_face
expansion, all exact); the canonical homogeneous transport (the same
frozen-geometry machinery behind ΔP/λ₁ and the recorded families);
the v22 loop machinery (the ρ³ = I 3-cycles, slot 82); the v28
topological skeleton (eigenframe zeros, windings). If LIVE, this is
the program's first FORM-LEVEL selection event — and it is
MAXWELL-SHAPED, not Einstein-shaped (a U(1) curvature sourced by
matter on the event-space): it would answer the recorded v22
parking-lot question ("the unforced inter-observer structure is
U(1)-gauge-shaped — why Maxwell?") at the kinematic level. FENCE: no
identification with physical electromagnetism is claimed —
"Maxwell-shaped" is a statement about a U(1) over the candidate base._

_Discipline: v21–v29 pattern — executor + independent verifier
(separate code path), exact verdicts, fail-fast gates, controls with
known answers. No Einstein, no metric law, no Newton constant, no
G = κT, no dark matter, no geodesic-motion language; the v18/v20
MM-connection corpse stays buried (this is the BASE's own gluing, not
a fiber-built spacetime connection)._

## Pre-read: milestone type (pre-registered)

**GENUINE FORK** (v27/v29 class): no expected verdict. LIVE = the
clock connection has nonzero, matter-shaped, background-subtracted
curvature at ε² (the first matter-FORCED form-level structure; the
form-selection fork resolved constructively). DEAD = the twist is
exact as a 1-form (the clock connection is gauge-flat; matter pins
class + rate only, and the form-level U(1) stays unforced — the v28
class-only result is the ceiling). Both branches are payloads. Honest
prior: genuinely open — v29's no-global-H says clock synchronization
fails, but a 1-form can be exact even when the operator-valued
synchronization is over-determined; the two statements are NOT
equivalent (do not conflate them — guard 5). **The design pass caught
trap #13 (instance 13 of the bug class): the canonical transport has
its OWN holonomy (the space is curved), so any matter config would
show naive loop-curvature — the verdict MUST be background-subtracted
analytically.**

## The setup (verify every step)

**The cast (canonical, no clamp).** At each event p, the face carries
the clock K_face(p). The v28 generator D restricted to the face is the
slice-rotation generator (verify against the recorded v28 spectrum:
the face block of D is the ±i:1 slice pair; everything else in the
face is D-killed). Transport along the variety uses the canonical
homogeneous connection (the F₄/SU(3)-invariant transport — the same
frozen-geometry machinery already certified via the families; D_p
along a path = the canonical transport of D). Define the
**clock-drift 1-form**

> **a_X(v) := ⟨ ∇_v K_face , D_p|_face ⟩**,  v ∈ T_p,

∇ = the canonical face-bundle transport. Both ingredients are
certified objects; the only geometry used is the frozen canonical
structure (allowed; not claimed derived). Units: log-scale (exact).
Per-face I-shifts drop automatically (D|_face is traceless on the
face — verify).

**The ε-grading (pre-registered structure).**
- ε⁰ (vacuum): K ∝ I ⇒ ∇K = 0 ⇒ **a ≡ 0 identically** — the vacuum
  has FLAT clock transport (hand-true; Gate-1 control).
- ε¹: K⁽¹⁾ is realized by a global H⁽¹⁾ (v29 T1) ⇒ the ε¹ part of
  a_X must have ZERO loop holonomy (integrable) — a forced control,
  NOT evidence (trap #7's descendant).
- ε²: K⁽²⁾ = −(9/8)a²I + (9/2)(C_pM)² (the v29 hand-closed form; the
  I-part drops in the pairing). **The verdict lives here, and the
  ε²-ring is POLYNOMIAL/RATIONAL — no logs anywhere in the verdict
  path** (logs enter only at finite ε, not used for the verdict).

**Trap #13 and the background subtraction (mandatory).** The
canonical transport around a closed loop has nonzero holonomy (the
canonical curvature of the frozen geometry — for the cut, the
Fubini–Study 2-form; the v22 3-cycle at phase φ is the recorded
instance: flat at φ = 0, nontrivial at φ ≠ 0). Therefore the naive
loop integral ∮a_X picks up [background holonomy acting on the
K-field] even for matter with NO intrinsic twist. The verdict object
is the **background-subtracted holonomy**: compute the pure-transport
prediction for the SAME K-field analytically (the canonical-holonomy
rotation applied to K, paired with D — exact), and subtract. Gate-1
control: the background term alone, on the recorded v22 loops, must
match the recorded canonical values exactly. Secondary cross-check:
the spectrum-matched diagonal reference (same eigenvalues, diagonal
frame — the v24 direction-blind contrast) must show ZERO subtracted
holonomy (it sits in the co-diagonalization strata).

**Loops (the test set).** (i) The recorded v22 ρ³ = I 3-cycles
(u-aligned; phase φ rational instances). (ii) Small loops encircling
ONE eigenframe zero of s_X (the v28 skeleton — does the subtracted
clock holonomy see the zeros?). (iii) A generic small loop away from
all strata (the basic curvature probe: the ε²-curvature 2-form
F = da_X evaluated on a tangent 2-plane at a generic p — computable
directly as a second mixed derivative along two family directions,
no integration needed; this is the PRIMARY verdict object, the loop
integrals are corroboration).

## Claims

**U1 — the cast (lemma grade).** D|_face = the slice-rotation
generator, traceless on the face (from the v28 spectrum, re-verified
directly); a_X well-defined (face-bundle transport canonical;
I-shifts drop); the ε-grading as stated, with the ε² pairing
reducing to **a_X⁽²⁾(v) = (9/2)·⟨ ∇_v[(C_pM)²] , D_p|_face ⟩** plus
the a²-term's I-drop (derive and verify symbolically).

**U2 — controls (zero evidential weight, all must behave).** Vacuum
a ≡ 0; the strata (diagonal X along single-rotation families;
spectrum-matched diagonal reference) give zero SUBTRACTED holonomy;
the ε¹ loop holonomy is zero (forced by v29's H⁽¹⁾); the pure
background term matches the recorded v22 canonical values on the
3-cycles.

**U3 — THE FORK (the verdict, at ε², exact).** Compute
F⁽²⁾ = d(a_X⁽²⁾) — the background-subtracted curvature 2-form — at a
generic event on generic tangent 2-planes (symbolic M where feasible;
u-complex sector first, then full), plus the subtracted holonomies on
the loop set. **LIVE ⟺ F⁽²⁾ ≢ 0**, with the payload: express F⁽²⁾ in
the certified field basis (the level-2 sector — R_M, the twist; state
the exact relation, e.g. F = (const)·d(level-2 field)∧d(level-1
field)-type, whatever it is); report whether F sees the eigenframe
zeros (loop set (ii)) and how F relates to the v28 class. **DEAD ⟺
F⁽²⁾ ≡ 0 identically** (the twist is exact as a 1-form): then exhibit
the global potential χ with a_X⁽²⁾ = dχ explicitly (the constructive
certificate — DEAD must be constructive, not a failure-to-find), and
state the scope theorem: matter pins class + rate but NOT form; the
v28 class-only ceiling stands.

**U4 — the reading (fenced).** IF LIVE: the program's first
matter-FORCED form-level structure — a U(1) curvature on the
event-space sourced by matter at second order; MAXWELL-SHAPED, not
Einstein (the tensor wall stands; Block B untouched); answers the
v22 parking-lot "why Maxwell?" at kinematic level; NO identification
with physical electromagnetism claimed. IF DEAD: the form-selection
fork closes negative — the gluing U(1) is unforced at form level for
ALL the matter data the route possesses (class + rate + twist
exhausted); record it as the third boundary stone of that kind. One
sentence stating which world.

## Gates

- **Gate 0 — the cast (fail-fast).** D|_face from the recorded v28
  matrix (slice pair isolated; traceless on the face); the canonical
  face-bundle transport reproduces the recorded family machinery
  (regression against the v25 ΔP identities); the v29 K⁽²⁾ form
  re-verified.
- **Gate 1 — controls (zero weight).** All of U2, including the
  background-term match on the recorded v22 loops (trap-#13's
  subtraction calibrated BEFORE any verdict computation).
- **Gate 2 — U1** (the ε² pairing derived and verified symbolically).
- **Gate 3 — U3 in the u-complex sector** (the curvature verdict,
  symbolic M where feasible; rational-instance battery otherwise,
  with the verdict object exact per instance).
- **Gate 4 — U3 full + U4** (full-26 where feasible; the loop set;
  the payload expressed in certified fields; the constructive
  certificate if DEAD).
- **Gate 5 — the v31 ledger (exploratory, NO claims).** Price:
  (i) the Lichnerowicz/tensor probe (Block B: do ∇∇φ deformations at
  the λ₁ = 12 threshold get sourced by matter — the Einstein
  make-or-break, designed blog-side); (ii) if LIVE, the F-flux
  quantization question (∮F vs the v28 windings) and the
  lapse/00-assembly consumption; (iii) if DEAD, what (if anything)
  beyond class+rate+twist could still force form — or whether the
  unforced-U(1) is final.
- **STOP rule:** background-term mismatch at Gate 1, or any broken
  setup identity = design hole; report and STOP.

## Guards (pre-registered)

1. **Background subtraction mandatory (trap #13):** no curvature
   verdict without the analytic background term subtracted and
   independently calibrated on the recorded loops.
2. **Order discipline:** ε⁰/ε¹ are controls; only ε² carries the
   verdict; no finite-ε logs in the verdict path (the ε² ring is
   rational).
3. **Strata discipline:** co-diagonalization strata and the
   spectrum-matched diagonal reference carry zero weight.
4. **DEAD must be constructive:** exhibit the potential χ, not a
   failure-to-find.
5. **Do NOT conflate v29's no-global-H with curvature:** the
   operator-valued synchronization failure does not imply (or
   forbid) 1-form curvature — the statements are independent; cite
   v29 only as motivation, never as evidence.
6. **The octonion product-order trap (standing):** independent
   implementations agree on an octonionic battery first.
7. **Language fence:** Maxwell-SHAPED only (a U(1) over the candidate
   base; no physical-EM identification); no Einstein/metric-law/
   Newton-constant/dark-matter/geodesic language; the v18/v20 MM
   corpse stays buried; the frozen canonical geometry is used, not
   derived.

## Deliverables

`derivations/90-VERDICT.md` (U1–U4, the verdict rule applied, scope
stated); `derivations/90-GATE-N-SUMMARY.md` per gate;
`derivations/90-clock-connection-RESEARCH.md` (the cast, the
subtraction, the curvature computation, the payload-in-certified-
fields or the potential certificate, the v31 ledger);
`code/clock_connection.py` (executor) +
`code/clock_connection_verify.py` (independent path; an
`_indep_check.py` third path welcome, v26–v29 parity). Commit; HOLD
the v30.0 milestone bookkeeping for ratification, mirroring v25–v29.
