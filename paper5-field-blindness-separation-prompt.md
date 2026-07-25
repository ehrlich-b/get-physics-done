# Paper 5 — The Field-Blindness Separation Theorem (complex = self-modeling + closure of V under the Lie bracket −i[·,·])

## TASK TYPE
Prove a SEPARATION / IRREDUCIBILITY theorem and nail the physical identity of the one irreducible
field-selecting datum. This is NOT an attempt to force complex from self-modeling — that is dead
(real QM is a counterexample). It is to PROVE exactly what complex requires beyond self-modeling and
that the requirement is irreducible.

## BACKGROUND (established this session; do not re-derive)
- `M_2(R)_sa` ⊨ Definition 1 (finite, faithful order-iso φ=id, minimal, simple) — real QM is a
  CONSISTENT self-model ⇒ self-modeling does NOT force complex.
- The forced self-modeling (Lüders) update is anticommutator-generated: for `a=1+εX`,
  `√a ρ √a ≈ ρ + (ε/2){X,ρ}`. Symmetric / Jordan / FIELD-BLIND. (Verified, scratchpad/verify_dc_kill.py.)
- The complex unit `i` lives in the commutator `[a,·]` (Lie). `i[a,b]` Hermitian ⟺ complex.
- **ALGEBRAIC FORM OF THE `+1` (use this language throughout; do NOT say "becoming" in the math):**
  the field-selector = **`V` closed under the bracket `⟦a,b⟧ := −i[a,b]`** (equivalently `V` is the
  self-adjoint part of an associative *-algebra = a **Jordan–Lie / Poisson algebra**). Real QM:
  `⟦a,b⟧ ∉ V` (antisymmetric/imaginary — the missing Y); complex QM: `⟦a,b⟧ ∈ V`. This is the program's
  own "**a Jordan algebra has no Poisson bracket**." `⟦·,·⟧`-closure ⟺ complex (A–S / Jordan–Lie).
- A–S dynamical correspondence (the "bridge" `ψ:V→`skew-derivations, `ψ(a)=i·ad_a`): a JB-algebra
  admits one IFF it is the self-adjoint part of a complex C*-algebra (excludes real/quaternionic/Albert).
- Prior GPD (CLAMP): the forced Lüders order-dependence is in V on every type (cubic Jordan-triple
  object), NOT the A–S commutator `ab−ba`; forcing the bridge = positing `i` = re-imports complex.

## THE CLAIM TO PROVE (the separation theorem)
- **(S1) FIELD-BLINDNESS.** `M_n(R)_sa`, `M_n(C)_sa`, `M_n(H)_sa` are all consistent finite-dim
  self-models — each a homogeneous self-dual EJA carrying the forced sequential product + a faithful
  tracking map, and each carrying reversible order-automorphism dynamics. Self-modeling determines
  the structure ONLY up to the field. [Verify for H; re-confirm R.]
- **(S2) THE BRIDGE IS THE SELECTOR.** The field is selected exactly by the Jordan→Lie bridge =
  the dynamical correspondence = a local complex unit `i` = an orientation (A–S).
- **(S3) IRREDUCIBILITY (the real mathematical content) — STATE IT WELL-POSED, NOT AS A UNIVERSAL.**
  Self-modeling supplies BOTH banks — the Jordan product `a∘b=½{a,b}` AND the existence of reversible
  order-automorphism flows `e^{tD}` — and BOTH are field-blind (prove per type: R/C/H all carry them).
  The selector is closure of `V` under `⟦a,b⟧:=−i[a,b]`, and `⟦·,·⟧`-closure ⟺ complex (A–S). THEREFORE
  the selector is supplied by NO field-blind datum — it is irreducible to self-modeling:
  `complex = self-modeling + ⟦·,·⟧-closure`. (Do NOT try to prove the ill-posed "no property weaker than
  complex forces complex" as a quantifier over all properties — prove the algebraic statement: both banks
  field-blind + `⟦·,·⟧`-closure ⟺ complex. "No weaker property" is an informal [gloss] on that, not the lemma.)
- **(S4) PHYSICAL IDENTITY of the +1 — the MATH is `⟦·,·⟧`-closure; the rest is a labeled gloss.**
  The `+1` = `V` closed under `⟦a,b⟧=−i[a,b]` = "the generator of self-evolution is itself an OBSERVABLE."
  Physical reading [STRUCTURAL-CORRESPONDENCE, not load-bearing]: the observer measures its own BECOMING
  (energy/rate), vs. merely its ORDER (level 1, Jordan/anticommutator, field-blind) or its TRAJECTORY
  (level 2, reversible flow, field-blind). Three-level ladder; level 3 = `⟦·,·⟧`-closure = complex = us.

## ADVERSARIAL GUARD (the ~0-assumption route is dead; do NOT re-open — it thrashes)
Real QM keeps faithful REVERSIBLE RECORDS of its becoming (SO(n) trajectory) with a NON-observable
generator (so(n), antisymmetric, ∉ V). So "record your becoming" = "record your trajectory" is
field-blind (real QM ⊨ it). The bridge (generator-AS-observable) is strictly stronger = complex.
Therefore any claim of the form "self-modeling structure X (record-keeping, reversibility,
self-checking, strange-loop closure) forces the bridge" is FALSE (real QM ⊨ X). Do NOT try to prove
those. The only mathematical content left on the complex step is the IRREDUCIBILITY (S3).

## WHAT TO ACTUALLY PROVE / COMPUTE
1. **(S1)** Exhibit `M_n(H)_sa` as a self-model (homogeneous self-dual EJA + sequential product +
   faithful φ); re-confirm `M_n(R)_sa`. Confirm all three share the Jordan + reversible-dynamics
   structure (the "both banks").
2. **(S3) THE IRREDUCIBILITY LEMMA** (the core): prove that for a finite-dim EJA, "admits a dynamical
   correspondence" is field-equivalent to "complex," and that BOTH the Jordan structure AND the
   existence of reversible order-automorphism dynamics are field-blind (R/C/H all have them).
   Conclude: the bridge is the unique, irreducible field-selector; complex = self-modeling + the
   bridge; the +1 cannot be weakened.
3. **(S4)** State the three-level ladder precisely (order = anticommutator/Jordan; trajectory =
   reversible flow; generator-observable = bridge), rebit at level 2, complex at level 3. Label the
   physical reading [STRUCTURAL-CORRESPONDENCE].

## GUARDRAILS
- This proves a SEPARATION (complex is an irreducible +1), NOT a forcing. Do not overclaim.
- `M_n(R)_sa ⊨ Def-1` is the load-bearing counterexample; keep it central.
- The +1's physical reading ("observer measures its own becoming") is a [STRUCTURAL-CORRESPONDENCE]
  gloss on the bridge — label it; the MATH is the irreducibility lemma (S3).
- State at the EJA / order-derivation level; do NOT route through the undefined φ (PHI-OP / GAP-1).

## OUTPUT
- The separation theorem (S1–S4), stated precisely.
- The irreducibility lemma (S3): PROVED, or the precise obstruction.
- Confirmation `M_n(H) ⊨ Def-1` (S1).
- The three-level ladder (S4) with the physical identity of the +1.
- One-line honest SSOT status.
