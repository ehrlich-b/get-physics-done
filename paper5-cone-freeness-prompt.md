# GPD Milestone: The Paper 5 Cone-Freeness Theorem (positivity of the Lüders product)

**Is Paper 5's "self-modeling -> complex QM" a DERIVATION or a CONDITIONAL SYNTHESIS? It
comes down to one positivity question.** Prove or disprove a single claim about ordered
vector spaces.

Written 2026-06-23 after a cold third-party review (Codex) rejected Paper 5: the "derives
complex QM" chain rests on an ASSUMED axiom (positivity of the corrected product), not a
proof, and the obvious proof is circular (it presupposes the Jordan structure being
derived). This prompt isolates the exact load-bearing joint. Self-contained: all
definitions are inline (do NOT trust the repo's `papers/` copies; the live source is
`~/repos/blog/landing/papers/qm-from-self-modeling/`).

---

## Why this is the whole ballgame

Paper 5's chain is: self-modeling Definition 1 -> a sequential product on a spectral
order-unit space -> (van de Wetering Thm 1) Euclidean Jordan algebra -> [imported local
tomography] complex type -> C* -> complex QM. A cold review collapsed its three "fatal"
objections into ONE:

- The paper's "corrected product" `a·b = Σ_i λ_i C_{p_i}(b) + Σ_{i<j} √(λ_i λ_j) P_{ij}(b)`
  is precisely the Peirce expansion of the LÜDERS SANDWICH `a·b = √a · b · √a` (with
  `a = Σ_i λ_i p_i`; the `√(λ_i λ_j)` are √a's own spectral coefficients). So the mixing
  function `f = √` is FORCED — not a free choice needing a separate "unitality" argument.
  (This dissolves objection #1.)
- The composite / local-tomography step (objection #3) is the SEPARATE selector of complex
  over real/quaternionic; it is honestly imported and is NOT the subject of this prompt.
- What remains (objection #2) is the ENTIRE question: **is the Lüders product
  cone-preserving — `a·b ≥ 0` for all `a,b ≥ 0` — on an abstract spectral order-unit space
  that is NOT assumed to be a Jordan algebra?** In `M_n(C)` yes (Lüders). Abstractly, the
  paper builds the Peirce-1 projection `P_{ij}` as a difference of compressions
  (`P_1 = id − C_p − C_{p⊥}`), which is NOT a positive map; and the clean proof that
  `√a·b·√a` preserves the cone is the Jordan/JB theorem that the quadratic representation
  `U_{√a}` is positive — which PRESUPPOSES the Jordan structure the paper is trying to
  derive. That circularity is the rejection.

THE PHYSICAL REDUCTION (why GPD should care): positivity is the self-consistency closure
of self-modeling — `a·b` is the self-model of "do `a`, then `b`," and it must land back in
the valid state cone or the model is unfaithful (predicts states the system cannot
occupy). "Faithful self-modeling forces positivity" is sound but reduces to exactly the
math question below, because faithfulness forces `a·b ≥ 0` only on spaces that are
realizable systems, and whether the abstract class "non-classical spectral OUS" coincides
with the realizable ones IS this question.

## The claim to PROVE or DISPROVE

> **(CONE-FREENESS).** Let `V` be a finite-dimensional spectral order-unit space equipped
> with Alfsen–Shultz compressions `{C_p : p ∈ Proj(V)}` and the induced Peirce
> decomposition (below). Call `V` NON-CLASSICAL if some Peirce 1-space `V_1(p) ≠ {0}`
> (equivalently the pinching map `C_p + C_{p⊥} ≠ id`; equivalently `V` is
> non-commutative). For `a ∈ V_+` with spectral resolution `a = Σ_i λ_i p_i`, define the
> LÜDERS PRODUCT
>     `a·b := Σ_i λ_i C_{p_i}(b) + Σ_{i<j} √(λ_i λ_j) P_{ij}(b)`   (`= √a · b · √a` in the associative case).
> CLAIM: on EVERY such `V`, the Lüders product is cone-preserving (`a·b ∈ V_+` whenever
> `a,b ∈ V_+`) and satisfies the sequential-product axioms S1–S7 — equivalently (via van de
> Wetering Theorem 1), `V` is a Euclidean Jordan algebra.

PROVE it -> positivity is FREE from the spectral + non-classical structure: Paper 5's axiom
`selfModelProduct_nonneg` is a THEOREM, the corrected-product construction is valid, and
"self-modeling -> Jordan" closes non-circularly. The derivation is recovered (modulo the
separate, imported local-tomography step to complex).

DISPROVE it (exhibit a finite-dim non-classical spectral OUS with valid Alfsen–Shultz
compressions on which `b ↦ √a·b·√a` leaves the cone for some `a,b ∈ V_+`, OR fails some
S-axiom): positivity is genuine EXTRA CONTENT, not derivable from the spectral structure.
Paper 5 is then an honest CONDITIONAL SYNTHESIS — positivity must be IMPORTED as a
physically-motivated premise ("the self-model stays in its valid state cone"), and the
headline downgrades from "derives" to "houses/forces, given a cone-preservation premise."

## The structure-theory fork (the run cannot come back empty)

Built into the claim is the question: **does "finite-dim spectral OUS with Alfsen–Shultz
compressions" ALREADY imply Euclidean Jordan algebra?** Resolve it explicitly — it routes
to one of three decision-relevant verdicts:

1. **Positivity-free (PROVE):** the Lüders product is always cone-preserving on the
   non-classical class -> RECOVERY.
2. **Counterexample (DISPROVE):** a non-classical spectral OUS where the sandwich leaves
   the cone (or fails an S-axiom) -> LEVEL-2 conditional synthesis.
3. **Premise smuggles Jordan:** "spectral OUS with compressions" already entails JB
   independent of the Lüders product (e.g. Alfsen–Shultz's own characterization already
   forces it) -> positivity is free but the PREMISE was Jordan all along -> a DIFFERENT
   circularity to disclose (the contribution shrinks to a known structure theorem).

The decisive sub-task: state EXACTLY which Alfsen–Shultz axioms you take as "spectral OUS
with compressions" (bare compressions + spectral resolutions, vs. the full
JB-characterization set including symmetry of compressions / orientation / the
ellipticity–"Hilbert ball" property), and determine WHERE on that axiom ladder the answer
flips. Alfsen–Shultz spectrality is understood to be NECESSARY but not SUFFICIENT for JB —
so a non-Jordan non-classical spectral OUS plausibly EXISTS, which would make Case 2 (or a
refined Case 1: positive-but-fails-another-S-axiom) the live outcome. Pin it down.

## Inline definitions (authoritative; use these)

**Spectral order-unit space (finite-dim).** A finite-dim order-unit space `(V, ≤, 𝟙)` in
spectral duality with its dual: each `a ∈ V` has a spectral resolution `a = Σ_i λ_i p_i`
into mutually orthogonal projective units `p_i` (`Σ p_i = 𝟙`) with real eigenvalues
`λ_i`, and a functional calculus (so `√a = Σ_i √λ_i p_i` for `a ≥ 0`). [Alfsen–Shultz
2003, Ch. 8.]

**Alfsen–Shultz compression.** For a projective unit `p`, the compression `C_p : V -> V`
is the order-theoretic "filtering onto the face of `p`" — a positive linear idempotent
with `range = face(p)`, complement `C_{p⊥}`, satisfying the Alfsen–Shultz compression
axioms. [Alfsen–Shultz 2003, Ch. 7.]

**Peirce decomposition (relative to `p`).** `V = V_2(p) ⊕ V_1(p) ⊕ V_0(p)`, with
`V_2(p) = range(C_p) = face(p)`, `V_0(p) = range(C_{p⊥}) = face(p⊥)`, and
`V_1(p) = ker(C_p) ∩ ker(C_{p⊥})` the Peirce 1-space. The pinching map `C_p + C_{p⊥}`
annihilates `V_1(p)`; it equals `id` iff `V_1(p) = {0}` (classical/commutative). For a
resolution `{p_1,...,p_n}`, `P_{ij}` projects onto the `(i,j)` Peirce 1-space
`V_1(p_i,p_j)`, with `b = Σ_i C_{p_i}(b) + Σ_{i<j} P_{ij}(b)`.

**Sequential product axioms S1–S7 (van de Wetering, Def. 2).** A binary op `(·)` on
effects with: S1 additivity (`a·(b+c)=a·b+a·c` when `b+c≤𝟙`); S2 norm-continuity of
`a ↦ a·b`; S3 unitality (`𝟙·a=a`); S4 `a·b=0 ⟹ b·a=0`; S5 associativity on compatibles
(`a~b ⟹ a·(b·c)=(a·b)·c`, where `a~b` means `a·b=b·a`); S6/S7 compatibility
additivity/multiplicativity. (Implicit: the product maps effects to effects — i.e. it is
cone/order-preserving — and THIS is the positivity at issue.)

**van de Wetering Theorem 1.** A finite-dim (cone-preserving) sequential product space
satisfying S1–S7 is the self-adjoint part of a Euclidean Jordan algebra, with
`a·b = √a · b · √a` the canonical (Lüders) sequential product. [van de Wetering 2019,
"Sequential product spaces are Jordan algebras."]

**Generalized no-broadcasting (context, GIVEN — not the task).** Barnum–Barrett–Leifer–
Wilce, PRL 99, 240501 (2007): a finite-dim GPT permits broadcasting (distinct perfect
copies) iff it is classical (a simplex). With the program's relativity-of-isomorphism
axiom ("no distinct perfect copies"), this FORCES the self-modeler's state space to be
NON-CLASSICAL — which is why the claim is posed on the non-classical class. Treat as
established; do not re-derive.

## Decomposition (suggested attack)

1. **Pin the axiom set.** Fix exactly which Alfsen–Shultz axioms define "spectral OUS with
   compressions" here. Decide whether they already force JB (Case 3) — check Alfsen–Shultz
   2003 (the JB state-space characterization: spectrality + symmetry + ellipticity /
   orientation) and Hanche-Olsen–Størmer.
2. **If not already-JB: try to build a counterexample.** A finite-dim non-classical
   spectral OUS that is NOT a Euclidean Jordan algebra (candidates: cones with a nonzero
   Peirce-1 space but a non-Jordan product structure; "almost-Jordan" cones; polygon /
   non-locally-tomographic GPT state spaces that are spectral but not Jordan). On it,
   compute `b ↦ √a·b·√a` via the compression/Peirce formula and test cone-preservation on
   extreme rays.
3. **If no counterexample: prove cone-preservation WITHOUT the Jordan quadratic-rep
   theorem.** The whole point is non-circularity — a proof invoking "`U_{√a}` is positive
   because `V` is a JB-algebra" is INADMISSIBLE (it assumes the conclusion). Find an
   order-theoretic / compression-only argument, or show one cannot exist.
4. **Verdict + scope.** State which of the three cases holds, with the axiom dependence
   explicit.

## Existing pieces / sources
- Live paper: `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` (`eq:peirce`
  ~line 258; sequential-product `Def. 2` ~line 298), `sections/axiom-verification.tex` (the
  corrected product + the compression-difference positivity claim, ~lines 22–42),
  `sections/type-exclusion.tex` and `sections/discussion.tex` (the `√a·b·√a`
  identification).
- Alfsen–Shultz 2003, *Geometry of State Spaces of Operator Algebras* (compressions Ch. 7;
  spectral duality Ch. 8; JB characterization). van de Wetering 2019 (sequential product
  -> Jordan). Barnum–Barrett–Leifer–Wilce 2007 (no-broadcasting). Hanche-Olsen–Størmer
  (JB algebras).
- Context: `~/repos/blog/research/STATE.md` (2026-06-23 Paper-5 block), `GRAPH.md` (P5
  node + SHOCK 1), `~/repos/blog/TODO.md` (top section), memory
  `paper5-recovery-relativity-of-isomorphism`.

## Out of scope
- The complex-vs-real-vs-quaternionic selection (imported local tomography) — separate,
  downstream, parked.
- The no-broadcasting -> non-classical step (established; given).
- Whether faithfulness "should" be formalized as `ρ>0` vs `φ`-iso — the physical
  motivation; this prompt is the pure math joint it reduces to.
- Consciousness / Φ / gravity (separate tracks).

## Reward-hacking guard (engage the self-checks)
Do NOT "prove" cone-preservation by invoking any Jordan/JB-algebra fact that presupposes
the multiplication (`U_a` positivity, the JB spectral theorem, etc.) — that is the exact
circularity under review. Do NOT redefine "spectral OUS" to be a Jordan algebra by fiat,
or "non-classical" to exclude the hard cases. If the honest finding is that "spectral OUS
with compressions" already smuggles Jordan, SAY SO (Case 3) — a valuable negative. A clean
COUNTEREXAMPLE (Case 2) is an equally valuable, fully acceptable outcome; do not force a
positive. The deliverable is a verdict with the Alfsen–Shultz axiom dependence made
explicit, not a defense of Paper 5.
