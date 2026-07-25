# slot 93 — v33.0: THE BLOCK-C CONFRONTATION (Paper 6) — what, if anything, forces the metric response
# STATUS: READY. Paste AFTER the v32.0 milestone is recorded (the ratification directive has landed
# and `.gpd/` shows v32.0 COMPLETE). This is THE tripwire run set by Bryan's governance:
# gravity or genuinely-don't-know, never math-for-math. CANNOT-FORMULATE or FORCES-NOTHING is a
# RESOLUTION, not a failure — the route parks at fork A (honest-scope write-up = the deliverable).
# Slot 93 supersedes paper6-block-c-confrontation-prompt-DRAFT.md (steelmanned in: Gate 0, A1/A3a
# sharpenings, Track B selection-traceability, lapse/00 ordering resolved).

## 0. Where we stand, and what this run is

The program owns the MATTER side of a variational pair, as theorems on the frozen cut
CP² = h₃(C_u) (Fubini–Study, Kähler–Einstein, Ric = 6g, Λ = 6, λ₁ = 12 mult 8, λ₂ = 32):
- E[φ_M, g] = ∫(|dφ_M|²_g − λ₁ φ_M²) dvol_g is framework-native (v25's field equation is its
  Euler–Lagrange identity); δE/δg is the B3-shaped stress whose unique transverse part is the
  certified v31/v32 mode — TT(B3) = the λ_L = 32 triple-27 straddle, ‖TT(B3)‖² = (1/30)(TrM²)²
  (detM absent), ε = λ_L − 2Λ = 32 − 12 = 20, direction T₂₇[P27(M⊗M)] (c₈ = c₁ = 0).
- The v26 sourced equation and the v27 balance law are exact identities on FROZEN g (v27 is
  metric-free by construction; demanding its persistence under g → g+h forces NOTHING — dead on
  arrival, excluded from the gates below).

What the framework has NEVER produced is the GEOMETRY side: a functional A[g] built from its OWN
resources (NO imported ∫R√g, NO GST prepotential — that chain died circular, gap-analysis.md) whose
coupled extremization with E forces a sourced response (Δ_L − 2Λ)h = κ·TT(B3), or NAMES what
replaces it. The five fiber kills (v17–v21) do NOT transfer: Molien forbids derivative functionals
on the ALGEBRA, but the variety is a MANIFOLD and spectral functionals of g exist there. Wall 1 (the
selection law) has never been asked on the variety. This run asks it, and only it.

## Gate 0 (BINDING — discharge the v32 deferred obligation before consuming ε)

v32.0-B recorded ε = λ_L − 2Λ = 32 − 12 = 20 for the FULL triple-27 straddle mode r, but on
EVIDENCE — Boucetta (arXiv:0712.2830) Table V/VIII row 2 + the degree-counting argument + the
(1,1)-block Schur scalar (both independent (1,1)-operators returned 32 on r[1]) + the single-rep
fingerprint — NOT on a directly-run full-tensor operator. The executor's anti-block `lichnerowicz`
path was flagged UNTRUSTED (spurious 28/4; duplicate def removed). The v32 milestone deferred this
to v33 Gate-0 as a BINDING obligation.

Build a correct full-tensor Lichnerowicz operator Δ_L on CP² and confirm **Δ_L r = 32·r on EVERY
block of r** — the (1,1)-27 AND the (2,0)+(0,2) anti-27s — exact over Q. Control: a correct fixed
Δ_L returns 32 on each block independently (no per-block hand-tuning).

- PASS ⇒ ε = 20 is CERTIFIED; proceed.
- FAIL ⇒ **STOP the entire run, report, and revisit the ε = 20 grade before ANY Block-C verdict.**
  Track A's A3 stiffness is built on ε; an uncertified ε poisons the verdict. (This mirrors v31's
  deferred positive-exhibit, which v32 Gate-0 discharged.)

Sequencing: Gate 0 must PASS before A3/A4/A5 (which consume ε). A1/A2 (literature + embedding
hypotheses, ε-independent) may run alongside Gate 0, but NO Block-C verdict is reported until Gate 0
passes. Also re-run the v32 fingerprint identities (T1/T2/T3 exact/Q) as the machinery-freeze control
before any new computation — deviation = a regression, halt and diagnose.

## Track A (the positive candidate): the λ₁-extremal selection principle

The one geometry-side functional the framework arguably FORCES: the variety's defining embedding is
BY λ₁-eigenfunctions (the moments φ_a, a = 1..8 = the SU(3) adjoint = the λ₁ = 12 eigenspace; v25's
moment construction is algebraic, not chosen). By the Takahashi / El Soufi–Ilias circle — an
isometric minimal immersion by first eigenfunctions ⟺ the metric is λ₁-extremal (a critical point of
g ↦ λ₁[g]·Vol[g]^{2/n}, n = 4) — "FS extremizes λ₁" would be a THEOREM of the construction, the first
candidate for A[g] = λ₁[g]·Vol[g]^{1/2}.

GATES (each falsifiable; exact over Q where in-rep):

- **A1 (literature + scope pin + the joint test).** State the exact Takahashi and El Soufi–Ilias
  theorems. Verify the moment embedding satisfies their hypotheses: isometric (up to the v25
  normalization?), minimal, into which sphere (the trace-form sphere of the Jordan algebra?).
  Deliverable = a PROPERTY-vs-PRINCIPLE verdict on TWO joints, both load-bearing:
  (a) is λ₁-extremality FORCED by the algebraic embedding, or merely TRUE of FS? (If the embedding
      is the moment map BY CONSTRUCTION, extremality is a consequence — FIT; if it has to be checked
      and happens to hold, CLAMP. Apply the joint test; if CLAMP, grade Track A accordingly and say
      so — do NOT relabel "conditional" and proceed.)
  (b) is FS the UNIQUE λ₁-extremal metric in its Kähler class (a genuine SELECTION), or one of many
      extremal metrics (a mere property that selects a CLASS, not FS)? A selection LAW needs
      uniqueness — pin whether a rigidity (e.g. FS maximizes λ₁ among Kähler metrics in the fixed
      class, fixed volume) applies. Non-unique ⇒ A[g] does not select FS ⇒ Track A weakens to a
      consistency condition, not a law. Report which.

- **A2 (in-rep minimality).** Minimality of the moment embedding CP² → S(trace form): the mean
  curvature vanishes (Takahashi: an immersion by λ-eigenfunctions of a NORMALIZED metric is
  automatically minimal-into-sphere — verify which direction is theorem and which needs computing,
  from the v25/v31 machinery).

- **A3a (the blindness check — RUN THIS BEFORE A3).** The second variation of λ₁ couples h through
  the overlaps ⟨dφ_a ⊗_sym dφ_b , h⟩. The products dφ_a ⊗_sym dφ_b are real symmetric 2-tensors;
  Sym²(8) ⊃ 27 once, so they CAN reach the straddle's 27-channel — but the straddle is THREE blocks
  ((1,1)-27 ⊕ (2,0)-27 ⊕ (0,2)-27, the v32 5:4 = (1,1):anti norm split). Test the overlap with EACH
  block separately:
    - zero overlap on all three ⇒ Track A is BLIND to the certified mode ⇒ A4 is degenerate ⇒
      FORCES-NOTHING for this candidate (record it, move to Track B).
    - nonzero on the (1,1)-27 only ⇒ Track A sources just 5/9 of the mode (the (1,1) share); the
      anti-parts get no response ⇒ a PARTIAL, non-Einstein response — grade FORCES-OTHER-PARTIAL,
      NOT FORCES-EINSTEIN-FORM (the full v32 mode includes the anti-27s).
    - nonzero on all three ⇒ Track A can source the full mode; proceed to A3/A4 to see the operator.

- **A3 (the second variation).** Compute δ²(λ₁·Vol^{1/2}) at FS on the TT sector, in-rep on the v32
  multiplet. λ₁ is degenerate (mult 8) ⇒ the variation is the eigenvalue-of-a-matrix problem on the
  8×8 ⟨dφ_a ⊗ dφ_b, h⟩ Gram (the v32 machinery computes this). Deliverable = the quadratic form
  Q_A[h] on the 27-multiplet, exact, SU(3)-equivariant (Schur block-diagonal — deviation = bug).

- **A4 (the coupled equation).** Extremize A[g] + μ·E[φ_M, g] over h at fixed M (μ a Lagrange
  multiplier, NOT a coupling — fence; see trap #21). Deliverable = the sourced linear equation for h,
  exact. STATE which it is:
    (i)   Einstein-form: (Δ_L − 2Λ)h ∝ TT(B3) on the TT sector;
    (ii)  a DIFFERENT named operator (still a sourced metric response — name it, do NOT relabel to
          fit; this IS the framework's gravity-shaped law, Einstein or not);
    (iii) degenerate (no TT response).

- **A5 (the number).** If (i) or a clean (ii): read off κ as the spectral ratio it is. FENCE: κ is a
  ratio of framework numbers, NOT Newton's constant; signature is still Riemannian (Wall 2 unpaid).
  NO outcome here is called "gravity."

## Track B (the exhaustion negative): the native-functional menu

Enumerate ALL framework-native functionals of g on the base. The menu is short and auditable, but
the test for each item is **selection-traceability**, not mere existence: a functional is NATIVE iff
its SELECTION (why THIS functional) traces to algebra/framework data; it is an IMPORT iff it is just
the known gravity action written down. Apply per item:

- (i) ∫G_M dvol (the entropy field): integrand is metric-blind ⇒ at most a trace/conformal response.
  Prove the one-line lemma and retire it.
- (ii) spectral functionals: the λ₁ tower (= Track A — selection traces to the moment embedding,
  NATIVE), λ₂, the heat invariants a_k. **CRITICAL:** a_1 = ∫R√g is a heat invariant — admissible to
  NAME on the menu, but it IS the fenced Einstein–Hilbert import (no framework-side reason selects it
  over any other functional of g; that is exactly the dead GST move). If the ONLY Einstein-producing
  menu item is a_1, the honest verdict is FORCES-NOTHING *natively* — a_1 wearing a spectral-invariant
  costume is still the import. (Trap #22.)
- (iii) Vol[g]: cosmological-constant only.
- (iv) anything from the moment map beyond (i)–(iii): sweep and name, applying the same
  selection-traceability test.

Deliverable: either Track A is the UNIQUE selection-traceable candidate (the menu argument closes),
or the missed candidates are named and priced. If Track A fails AND the menu is exhausted with no
native Einstein-producer ⇒ **FORCES-NOTHING is the verdict; the route parks at fork A** — record it
as the RESOLUTION of don't-know (the tripwire ACCEPTS this; what it forbids is wandering). Log any
silent cap (a functional skipped, a sweep bounded) explicitly — silent truncation reads as
"exhausted" when it isn't.

## Fenced / priced only — NOT run, NOT the verdict

- **lapse/00 — DEFERRED, not run here (ordering call; Bryan can override in one line).** The
  governance tripwire reads "after v32 + lapse/00 the NEXT run must BE Block-C." This run INVERTS
  that order on purpose: Block-C — does any native A[g] force a sourced response — is formulable and
  decidable on the SPATIAL TT sector the program already owns (the certified v31/v32 mode); the
  lapse/00 (time-time) assembly acquires a referent only IF Block-C lands positive (a response to
  complete into a full spacetime law). Running lapse/00 first builds metric-completion machinery that
  FORCES-NOTHING would waste — the math-for-math the tripwire forbids. So: Block-C now; lapse/00
  becomes the immediate follow-up iff the verdict is FORCES-EINSTEIN-FORM or FORCES-OTHER. (Bryan: if
  you want lapse/00 FIRST regardless, say so and this run waits.)
- **OP² lift** (Spin(9), not Kähler): priced, not assumed; off-menu for this run.
- **Base-Sakharov** (one-loop det of the 8 moment scalars on CP²; a_1 ∝ ∫R√g): an IMPORT (the
  functional-integral machinery + extremize-the-effective-action are not native). The v21 kind-4
  kill was the FIBER version (16-vs-6 rank wall); the base version stays PRICED-ONLY here — if Track
  A/B both land negative, it is the NAMED off-menu option for a later Bryan decision, not a silent
  fallback.
- **Thermo scope:** cite the 2026-06-09 unban memo's exact boundary before using ANY
  entropy-extremization language beyond v26's proved vacuum-MaxEnt (a theorem of the doublet, not a
  thermodynamic postulate).

## Verdict taxonomy (frozen at Gate 0; STOP rules binding)

- **FORCES-EINSTEIN-FORM:** A4 lands (i) with forced constants, A3a couples to all three blocks.
  (The program's first selection law — Wall 2 still unpaid, NOT called gravity.)
- **FORCES-OTHER:** A4 lands (ii) — name the operator; that IS the framework's gravity-shaped law,
  Einstein or not. Do NOT relabel to fit.
- **FORCES-OTHER-PARTIAL:** A3a couples to the (1,1)-27 only — a partial (5/9) response; honest
  intermediate, not Einstein.
- **FORCES-NOTHING:** A3a blindness, or A4 degenerate, AND Track B exhausted with no native
  Einstein-producer ⇒ park at fork A. A RESOLUTION — write it that way.
- **CANNOT-FORMULATE:** Gate A1 cannot pin the principle sharply ⇒ same as FORCES-NOTHING per the
  tripwire.

## Traps / controls / discipline

- Trap #20: extremality-as-property smuggled as principle — A1's joint test (a) is the guard.
- Trap #21: the multiplier μ relabeled a coupling — it is not.
- Trap #22: a degenerate A4 "fixed" by adding imported terms — adding ∫R√g at any gate (INCLUDING via
  the heat-kernel a_1 relabeled a "native spectral functional") = STOP.
- Trap #23 (new): a partial (1,1)-only response relabeled "Einstein on the relevant sector" — the
  relevant sector is the FULL straddle; partial is FORCES-OTHER-PARTIAL.
- Controls: the v32 fingerprint identities reproduce before any new computation (machinery freeze);
  A3's quadratic form is SU(3)-equivariant (Schur block-diagonal — deviation = bug); exact over Q.
- Fences (carry into every artifact): NO Einstein-equation / G=κT / dark-matter / geodesic language;
  κ is a framework ratio, NOT Newton's constant; the frozen FS geometry is USED, not derived;
  signature Riemannian (Wall 2 unpaid). v33 does NOT retract v17–v21 (Block-C statements). Paper 5
  remains the only result in the more-than-nothing column.
- Three-path verification standing; milestone HOLD for human ratification. Do NOT self-register v34.

## Through-line (for the milestone, mirror v32's)

v31 the tensor wall OPENS (existence) → v32 the tensor DICTIONARY closes (the forced source data:
κ = 1/30, ε = 20, the triple-27 straddle) → **v33 asks the SELECTION LAW: is there a native A[g]
whose coupled extremization with the matter E forces a sourced metric response, or does the variety
force nothing and the route park at fork A (honest incomplete-TOE)?** This is the tripwire: gravity
or genuinely-don't-know.
