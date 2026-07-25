# GPD Prompt — The Moment Doublet and the Canonical Field Equation on the Event-Space (J5-on-the-variety, step 1)

**Slot 85 / v25.0-candidate. STATUS: RATIFIED-BY-STANDING-DIRECTIVE (Bryan,
2026-06-10: "create the v25 prompt ... don't wait for my ratification").
Ready to run.**

_Context (blog repo): `research/gr-from-h3o/base-route-map.md` (Route 1,
v24.0 COMPLETE LIVE) + `entanglement-route.md`. v24.0 established: matter
shapes a non-trivial, direction-resolving face-purity landscape r(p) over
the idempotent variety OP² = F_4/Spin(9), with the u-aligned CP² cut
(tangent {11,18,19,26}) confirmed at 4d, homogeneous exactly at I/3.
v24.0 Gate 3 (design input, 84-GATE-3-SUMMARY.md): the matter landscape
and the canonical (Borel) geometry are GENUINELY DISTINCT structures —
the canonical transition function c11(t) = Tr(p(t)∘E_11) =
((1−t²)/(1+t²))² takes the SAME form along every family
(direction-blind), while the landscape's critical points track the matter
eigenframe. This run is STEP 1 of the J5-on-the-variety program: certify
the landscape's canonical TYPE (which structure the matter field IS,
relative to the canonical geometry's own operator) before any balance
question. Step 2 (the balance proper) is v26, designed against this run's
output._

_Discipline: v21–v24 pattern — executor + independent verifier (separate
code path), exact over Q / Q(t) / symbolic, fail-fast gates,
pre-registered expectations, controls with known answers. No G = κT, no
Newton constant, no SUGRA dynamics anywhere (the math-library note that
X# "is the field equation of 5d magic supergravity" is a recorded
CURIOSITY — v21's circularity fence stands; nothing here imports SUGRA).
All v24 objects are reused BY REFERENCE: ρ_face(p) = C_p(X)/Tr(C_p(X)) on
the rank-2 complement face, r = det ρ_face, the vv* Pythagorean family
construction, conventions u = e_7, families through E_11._

## Pre-read: what kind of milestone this is (honest-read, pre-registered)

This is a **verification-and-extraction milestone** (the v18-coframe /
v23-Gate-0 type), NOT a coin-flip test. The central claim (C1 below) has
a derivation sketch supplied and has already been hand-checked against
two recorded v24 data points at the design stage. Expected outcome:
PASS. The run's new-information content on expected-PASS: the exact
canonical eigenvalues (pre-registered 12 and 48 — confirm or correct),
the completeness theorem, the retro-derivation of ALL v24 phenomenology
from one identity, and the v26 design ledger. ANY failure = the
covariance argument has a hole = more informative than passing; report
the broken step exactly and STOP.

Two design-stage trap-class catches are binding on this run (instances
#5 and #6 of the designed-in-trivial-verdict bug class):

- **#5 (rational-function trap):** the normalized purity r = q/m² is a
  RATIONAL function of p, hence has infinite harmonic content on the
  variety; a "field equation for r" test is structurally un-passable and
  is hereby BANNED as a verdict object. The canonical polynomial
  observables are the char-poly coefficients of the UNNORMALIZED
  compression — the doublet (m, q) below.
- **#6 (annihilator trap):** ANY function with finitely many Laplace
  levels satisfies SOME polynomial-in-Δ identity (∏(Δ−λ_i) annihilates
  it). Only the FIRST-ORDER (single-eigenvalue / Helmholtz) statement is
  contentful. No higher-order annihilator may be reported as a law.

## The claims

**C1 (the moment-doublet identity — the core).** For all X ∈ h_3(O) and
all rank-1 idempotents p:

> m(p; X) := Tr(C_p(X)) = Tr(X) − ⟨X, p⟩
> q(p; X) := det₂(C_p(X)) = **⟨X#, p⟩**

where ⟨A,B⟩ = Tr(A∘B) and X# = X × X is the Freudenthal adjoint
(`h3o-math-library.md` §5: (X#)# = det(X)X, Tr(X#∘Y) = 3N(X,X,Y)).
Since the rank-2 face state has exactly two spectral invariants (trace
and determinant of a spin-factor element), (m, q) GENERATE the entire
v24 verdict object: r = q/m², and the full normalized face char-poly is
a function of (m, q) alone. **Consequence: the entire v24 landscape is
the moment doublet of the pair (X, X#) — two linear moment fields over
the event-space, nothing else.**

Derivation sketch (verify, don't trust): (i) m: Tr(U_{1−p}X) =
⟨X, U_{1−p}1⟩ = ⟨X, 1−p⟩ (U self-adjoint for the trace form, p
idempotent). (ii) q at p = E_11: the complement face is the lower 2×2
block (x₂, c; c̄, x₃); its rank-2 determinant x₂x₃ − c c̄ equals
(X#)₁₁ (the Freudenthal cofactor) = ⟨X#, E_11⟩. (iii) Extend to all p
by F_4-covariance: F_4 preserves the trace form and the cubic norm,
hence commutes with # and maps compressions to compressions, and acts
transitively on rank-1 idempotents (Borel, recorded). The full symbolic
verification (octonionic X, along all families) must be done exactly —
conventions and the octonionic off-diagonal entries of # are where this
could still break. The identity is presumably CLASSICAL for cubic Jordan
algebras (adjoint/cofactor identity — cite Jacobson 1968 / McCrimmon /
Springer if located; novelty is NOT claimed for the identity itself; the
program content is the doublet READING of v24 plus C2).

Design-stage anchors already checked by hand (the run must reproduce
these and the rest of the recorded tables):
- X = diag(7,5,3) (v24's diagonal state), t = 0 (p = E_11): q = 15,
  m = 8, r = 15/64 = the recorded 84-GATE-2 value.
- Same state, t = 1 (p = E_22 on the (1,0)-family): q = 21, m = 10,
  r = 21/100 = the recorded value.
- X = I/3: X# = I/9 ⇒ q ≡ 1/9, m ≡ 2/3, r ≡ 1/4 — the recorded vacuum
  homogeneity, now DERIVED (the vacuum is homogeneous because both
  moments of (I/3, (I/3)#) are constant).

**C2 (the forced canonical field equation).** Linear moment functions
restricted to the variety span exactly {constants} ⊕ {the first
canonical Laplace level}: on OP², h_3(O)* = 27 = 1 ⊕ 26 under F_4, the
restriction is injective (rank-1 idempotents span the algebra; ⟨1,p⟩ ≡ 1
is the constant), the 26 is the first spherical harmonic of the
two-point homogeneous space OP² (multiplicity-free L², Cartan/Helgason);
on the CP² cut, h_3(C_u)* = 9 = 1 ⊕ 8 under SU(3), same structure.
Therefore every moment field φ_Y(p) = ⟨Y, p⟩ satisfies the canonical
Helmholtz/Poisson-type equation

> **Δ (φ_Y − φ̄_Y) = −λ₁ (φ_Y − φ̄_Y)**, with the mean exactly
> **φ̄_Y = ⟨Y, I/3⟩** (the F_4-average of p is I/3 by invariance — exact,
> no integration needed),

with λ₁ FIXED by the canonical geometry alone — matter-independent =
universal. In particular the doublet obeys it with sources (X, X#):
Δq = −λ₁(q − σ₂(X)·(2/3·...)) — concretely q̄ = Tr(X#)/3 = σ₂(X)/3 and
m̄ = (2/3)Tr(X): **the field equation's background level is the state's
second char-poly coefficient σ₂(X)** (recorded: σ₂ = Tr(X#)).

Pre-registered eigenvalues (in the run's own normalization, where the
vv* families are unit-speed canonical geodesics — verified via the
recorded c11 form, see Gate 0): for ANY Y, Δφ_Y(E_11) = Σ over an
orthonormal geodesic frame of (φ_Y ∘ γ_i)''(0). For Y = E_11 each
direction gives cos²θ, second derivative −2, so:
- **CP² cut: Δc11(E_11) = −8, c11 − c̄ = 1 − 1/3 = 2/3 ⇒ λ₁ = 12** —
  this must and does match the literature value λ₁(CP^n) = 4(n+1) at
  n = 2 (Fubini–Study, holomorphic sectional curvature 4; Ikeda–Taniguchi
  1978 / Berger–Gauduchon–Mazet) — a free external cross-check.
- **OP²: Δc11(E_11) = −32 ⇒ λ₁ = 48** (16 directions; cross-check
  non-blocking vs CROSS spectra, Cahn–Wolf 1976 / Besse ch. 3).
- The ratio λ₁(OP²)/λ₁(CP²) = 4 = the dimension ratio — report it.

**C3 (the geodesic-frequency fingerprint — the cheap structural
signature).** Level ≤ 1 ⟺ the restriction of φ_Y to every closed
canonical geodesic is a + b·cos2θ + c·sin2θ (frequency ≤ 2; t = tan(θ/2)
is the rational chart). Hand-checked anchor: diag(7,5,3) on the
(1,0)-family gives m = 9 − cos2θ, q = 18 − 3cos2θ exactly. Every moment
along every family must have this form; the v24 rational r(t) tables are
then ratios (a−b·cos2θ−c·sin2θ-type over squared), which the run must
reproduce EXACTLY from the doublet — including the recorded generic-X
sample values (e.g., off-u r(2) = 2727493/12700800, C_u-phase
r(3) = 503003/2252432) and the three-families-three-functions
direction-resolution (now read off the octonionic components of X and
X# entering the moments).

## The exact verdict criterion

All verdicts symbolic/exact: C1 as polynomial identities over Q in
symbolic X (27 free rational parameters) along each family over Q(t);
C2's eigenfunction statement as a LINEAR identity in Y — verify on a
basis of 27 Y's (equivalently symbolic Y) at E_11; the extension to all
p is the covariance closure Δφ_Y(g·E_11) = Δφ_{g⁻¹Y}(E_11) (state the
argument; spot-check with one exact non-stabilizer rotation from the v22
u-aligned generator assets). Floating point illustrative only; any gate
whose verdict rests on floats is void.

## Gates

### Gate 0 — frames + machinery (fail-fast)

1. Build the missing cut family (2,7) (coord 26) and, for the OP²
   secondary, the full 16-direction battery (j,k), j ∈ {1,2},
   k ∈ {0..7}, by the same vv* construction. Exactness checks per
   family: p∘p = p, Tr p = 1, p(0) = E_11 over Q(t).
2. **Per-family canonical-form check (the normalization guard):** verify
   c11(t) = ((1−t²)/(1+t²))² along EVERY family used (this certifies
   unit-speed canonical geodesics; any family failing the form is
   EXCLUDED from frames — fail-fast if fewer than 4 cut / 16 full
   survive).
3. Orthonormality of the frame directions at E_11 (the V_{1/2} trace
   form on distinct (j,k) slots); the Laplacian assembler
   Δf(E_11) = Σ_i (f∘γ_i)''(0) in the θ-chart (dt/dθ = (1+t²)/2,
   so at t = 0 use f''_θ = f''_t·(1/4) + f'_t·(t-chain terms) — derive
   the exact chain rule once, verify on cos²θ).
4. Frame-independence check: assemble Δ from two DIFFERENT orthonormal
   frames (e.g., the standard (j,k) frame and a rotated frame via an
   exact rational rotation); results must agree exactly.

### Gate 1 — controls (known answers; zero evidential weight; must behave)

- **Known-LIVE control:** c11 = φ_{E_11} passes the Helmholtz test with
  λ₁ exactly (12 on the cut, 48 on OP²).
- **Known-MIXED control (discriminating power):** c11² restricted to
  geodesics = cos⁴θ (frequency 4) — it must FAIL the first-order test
  (this proves the test can say no; without it the gate is decoration).
- **Trivial control:** X = I/3 ⇒ both moments constant, Δ = 0, equation
  holds as 0 = 0 (pre-registered tautology, carried for the record).

### Gate 2 — C1: the doublet identity + completeness (the core)

Full symbolic verification of m = Tr(X) − ⟨X,p⟩ and q = ⟨X#,p⟩: symbolic
X (27 parameters), along all four cut families and at least two off-u
families over Q(t); plus the closed covariance argument for all p.
Completeness: exhibit the v24 verdict object (normalized face char-poly)
as a function of (m, q) alone, and REPRODUCE from the doublet: (a) the
recorded vacuum row (q ≡ 1/9, m ≡ 2/3, r ≡ 1/4); (b) the diagonal-state
r(t) and its direction-blindness (X and X# diagonal ⇒ the three
(0,1)-families' moments differ only through the e_k-component of the
relevant off-diagonal entry, which vanishes for diagonal X — derive,
don't just observe); (c) one recorded generic-X r(t) with its exact
sample values; (d) the eigenframe-critical-points finding (critical
points of q/m² along geodesics = where the two frequency-2 trigs align —
relate to the eigenframes of X and X#); (e) v24's flattening result
(the interpolation X_t = (1−t)I/3 + tX gives moments affine in t around
the constant vacuum moments ⇒ variation vanishing at t = 0 to the
recorded order — derive the exact mechanism).

### Gate 3 — C2 + C3: the field equation and the eigenvalues

The eigenfunction identity for symbolic Y at E_11 on the cut frame
(primary) and the 16-frame (secondary); extract λ₁ both ways;
means via ⟨Y, I/3⟩; the frequency fingerprint per family for symbolic Y;
the pre-registered values 12 and 48 confirmed or corrected (a corrected
value is a finding, not a failure — but the c11/literature cross-check
must then be reconciled before proceeding). Report the field equations
in final form: Δm = −λ₁(m − (2/3)TrX), Δq = −λ₁(q − σ₂(X)/3).

### Gate 4 — the v26 design ledger (exploratory, NON-BLOCKING, no law claims)

(a) The balance inventory: with both the matter side (m, q; sources X,
X#) and the canonical side (c11-type reference moments) now certified as
the SAME TYPE of object (level-≤1 moment fields with the same λ₁), list
the candidate forms a J5/Jacobson-type balance could take on the variety
(linear relations among moment fields; constrained extremization of
S(face) = S(m,q) at fixed canonical moment; the all-balls quantifier
analog), with for each: what would be varied, what could force a
nonzero multiplier, and the predicted vacuity risks. DESIGN INPUT ONLY.
(b) Per-class doublet table: where (X, X#) sit for trace-heavy vs
off-diagonal (V_{1/2}-supported) states — and the structural note that
NO level ≥ 2 contamination is possible in THIS landscape (the
CGM/Speranza exposure is structurally absent here; scope fence: this is
the finite face-purity landscape, not a QFT entanglement entropy — the
CGM question returns only when/if a base QFT is built).
(c) The cut-vs-mother comparison: anything the OP² 16-frame shows that
the CP² 4-frame doesn't (the bottleneck's first dynamical fingerprint —
or its absence).

## Pre-registered failure modes (bug guards)

1. **Convention drift:** the # and trace-form conventions must be THE
   REPO'S (X# = X×X with Tr(X#∘Y) = 3N(X,X,Y); cubic norm as in
   v17–v24). The C1 check must use the same compression code path as
   v24 (or reproduce its recorded tables first). A C1 failure must be
   triaged convention-vs-substance before being reported as substance.
2. **Frame/normalization (Gate 0.2-0.4):** no family enters a frame
   without the c11-form certificate; Δ must be frame-independent.
3. **Covariance bookkeeping:** any rotation used must be verified
   exactly (φ_Y(g·p) = φ_{g⁻¹Y}(p) on samples); off-u moves carry the
   v22 conjugation subtleties — u-alignment bookkeeping as in v24
   guard 4.
4. **Trap-class catches #5/#6 binding** (see Pre-read): no field
   equation claimed for r itself; no polynomial-in-Δ annihilator
   reported as a law.
5. **Numeric leakage (standing):** symbolic/exact verdicts only.

## Anti-overclaim (binding scope)

PASS ≠ Einstein, ≠ J5, ≠ a balance, ≠ dynamics: the background geometry
is FROZEN (Borel's metric, imported as math); this run certifies the
matter field's canonical TYPE and its forced linear field equation on
that fixed background — the entropy SIDE of a would-be balance, not the
balance. λ₁ is a property of the canonical geometry, not a derived
coupling; no Newton constant exists here. The identity C1 is presumably
classical Jordan theory (cite, don't claim). Signature remains OPEN
(Riemannian/compact); the variety remains the CANDIDATE event-space;
family-sampled differential claims are closed by the covariance argument
— state where the argument carries the load. The deflation stands: the
landscape's harmonic finiteness is automatic once C1 holds; the CONTENT
is (i) the doublet characterization (all of v24's phenomenology from one
identity), (ii) the single-level fact with the universal λ₁, (iii) the
exact eigenvalues, (iv) the v26 ledger.

## Deliverables

- derivations/85-moment-doublet-RESEARCH.md (derivation sketch worked
  out + citations: Jacobson/McCrimmon/Springer for the identity;
  Ikeda–Taniguchi / Cahn–Wolf / Besse for the spectra; Helgason for the
  two-point-homogeneous harmonic structure).
- derivations/85-GATE-N-SUMMARY.md per gate; independent verifier
  (separate code path) on C1 (brute symbolic expansion, NO covariance
  shortcut, at least one off-u family) and on C2 (different frame +
  independent λ₁ extraction); 85-GATE-2/3-VERIFICATION.md.
- code/variety_moment_doublet.py (executor, exact).
- One-paragraph verdict: C1 PASS/FAIL, C2 PASS/FAIL with λ₁ values, C3
  fingerprint, stated separately from the Gate-4 ledger.
- Milestone bookkeeping per the v24 pattern (PROJECT/STATE/state.json/
  MILESTONES → v25.0).
