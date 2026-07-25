# Paper 5 — Dynamical-Correspondence Route to Complex (replaces imported local tomography)

## TASK TYPE
Prove or disprove a specific claim, and classify the load-bearing joint as **FIT** (forced by
the self-modeling structure already in hand) or **CLAMP** (requires an added postulate).
Keep PROVED MATH rigidly separate from any constitutive [STRUCTURAL-CORRESPONDENCE] residual.

## SCOPE
This closes the **complex step only** (Jordan → complex). The Jordan step itself rests on the
separately-tracked recognition-symmetry/self-duality joint and is NOT settled here; the whole
chain is forced only if BOTH close (or if step 5's unification works). Primary discriminator =
**real vs complex** (`M_n(R)_sa` vs `M_n(C)_sa`); quaternionic/Albert/spin are secondary checks.

## BACKGROUND (established; do not re-derive)
- Paper 5 yields (modulo the separately-tracked recognition-symmetry/self-duality joint) a
  Euclidean Jordan algebra (EJA) `V` carrying the FORCED sequential ("cross") product — the
  test→update→test loop — of Lüders form `a·b = √a b √a` (`eq:corrected-product`). **In hand
  WITHOUT local tomography.**
- The bare Jordan product `a∘b` is symmetric (no bracket). The SEQUENTIAL product is
  order-dependent: `a·b ≠ b·a`. Write `ab = a∘b + ½[a,b]`; the antisymmetric `[a,b]` is the
  bracket the bare Jordan structure lacks. (The program separately PROVED "an EJA has no Poisson
  bracket" — the HKT-gravity route; `selection-law-ledger.md`.)
- The program separately established (lie-sector, TARGET 1, FORCED): a nonzero bracket generates
  a one-parameter automorphism group = time [Stone]. **But that ran the implication BACKWARD
  (complex ⟹ bracket ⟹ time). This task runs it FORWARD.**
- FORCING THEOREM (cite, do not reprove): **Alfsen–Shultz dynamical correspondence.** A
  JB-algebra is (Jordan-isomorphic to) the self-adjoint part of a complex C*-algebra IFF it
  admits a *dynamical correspondence*: a linear map `ψ: V → SkewOrderDerivations(V)` with
  (i) each `ψ(a)` a skew order-derivation (generator of a one-parameter group of
  order-automorphisms = dynamics); (ii) `ψ(a)a = 0` (an observable is conserved under the flow
  it generates); (iii) `[ψ(a), ψ(b)] = −[L_a, L_b]` (`L_a` = Jordan mult.; the integrability
  condition reconstructing `ab = a∘b + i·ψ`). This EXCLUDES `M_n(R)_sa`, `M_n(H)_sa`, and the
  Albert algebra `h_3(O)`; it selects exactly complex `M_n(C)_sa`.
  [Alfsen–Shultz, "Orientation in operator algebras," PNAS/CMP 1998; *State Spaces of Operator
  Algebras*, 2001 — already in Paper 5's bib as the compression source `AlfsenShultz2003`.]

## THE CLAIM TO PROVE OR DISPROVE
The self-modeling sequential product itself induces a dynamical correspondence on `V` —
concretely `ψ(a) :=` the skew order-derivation given by the antisymmetric part of
cross-product-with-`a` (`a ↦ [a, ·]` up to the forced normalization) satisfies Alfsen–Shultz
(i)–(iii) — so that, by the forcing theorem, `V` is forced to be complex `M_n(C)_sa`, excluding
`M_n(R)_sa`, `M_n(H)_sa`, `h_3(O)` **without invoking local tomography.**

## DEALBREAKER PRE-CHECK (do this FIRST; if it fails, the route is dead before the main question)
On `M_2(C)_sa`, verify that the antisymmetric part of the FORCED sequential product
(`eq:corrected-product` / Lüders `√a b √a`) actually reproduces the C* commutator `[a,b]=ab−ba`
that the Alfsen–Shultz correspondence `ψ(a)=i[a,·]` is built from — i.e. that the self-modeling
product's order-dependence IS the A-S bracket, not a different object. If the forced product's
antisymmetric part is not (proportional to) the associative commutator, the identification
"order-dependence ↔ dynamical correspondence" fails and the route is dead. Report this first.

## THE DISCRIMINATING QUESTION (the real output): FIT or CLAMP
Is the dynamical correspondence SUPPLIED by the already-forced sequential product (FIT — complex
genuinely forced), or does it require an ADDED postulate that the self-model represent its own
order-dependence as an observable / that `ψ` be complete-into-the-algebra (CLAMP — same status
as the imported local tomography, merely relocated)?

Compute / determine:
1. On each simple EJA type (`M_n(R)_sa`, `M_n(C)_sa`, `M_n(H)_sa`, spin factors, `h_3(O)`),
   compute the antisymmetric part `[a,b]` of the forced sequential product. Is it valued in the
   order-derivations of `V`? Is it valued in the OBSERVABLES (`V` itself) or OUTSIDE `V`?
2. Check axioms (i)–(iii) for `ψ(a) = [a,·]`-up-to-normalization. On which types do they hold?
   (Expectation: hold iff complex — `M_n(R)_sa`'s bracket lands in the antisymmetric/non-observable
   part, failing observability; `M_n(C)_sa`'s `i[a,b]` is Hermitian, passing.)
3. Does the EXISTENCE of the forced sequential product (which EXISTS on real QM too — the rebit
   has a Lüders product) by itself force (i)–(iii)? Or do they hold only once the field is
   complex — i.e., is "`ψ` is a dynamical correspondence" *equivalent to* "the field is complex,"
   hence non-forcing by itself?
4. Identify the MINIMAL additional clause (if any) needed, and classify it: (a) a genuine
   FAITHFULNESS/self-representation condition — "a faithful self-model must represent its own
   measurement-order-dependence `[a,b]` as one of its own observables" — distinct from assuming
   the field → FIT-eligible; or (b) equivalent to assuming complex → CLAMP. **Be adversarial:**
   the failure mode is that "represent your own bracket as an observable" silently RE-NAMES "the
   field is complex." If so, that is the DISPROVE outcome and it is valuable. CANDIDATE
   non-statistical necessity to test (the one thing that could push it FIT not CLAMP): the
   program's measure paper proves the observable-projection `P_O` and the stream/time propagator
   `φ` do NOT commute (`[φ,P_O]≠0`, strong-form complementarity). Does THIS self-modeling-native
   tension force the order-dependence `[a,b]` to be carried as an observable (not merely known as
   order-dependent statistics, the way a rebit can)? If yes → faithfulness-FIT; if it too reduces
   to assuming complex → CLAMP.
5. UNIFICATION CHECK: does the same self-representation principle that would supply the dynamical
   correspondence ALSO supply recognition-symmetry/self-duality (the separately-tracked Jordan
   joint)? Is there ONE principle ("a faithful self-model represents all of its own structure —
   its recognition symmetry AND its order-dependence — as accessible observables") that forces
   BOTH Jordan and complex, or are they independent?

## GUARDRAILS
- State everything at the EJA / order-derivation level. Do NOT route through the self-modeling
  operation `φ` (node PHI-OP / GAP 1, formally undefined). The claim must stand on the algebra.
- Separate PROVED MATH (the per-type computations; the A-S forcing) from any CONSTITUTIVE
  [STRUCTURAL-CORRESPONDENCE] residual. Do not let a constitutive premise masquerade as a theorem.
- The bare existence of a sequential product holds on real QM; the discriminator must be
  something self-modeling adds BEYOND "a product exists."

## OUTPUT
- VERDICT: complex FORCED via a self-modeling dynamical correspondence (FIT) / forced only via
  an added clause (CLAMP) / DISPROVED (route re-imports complex).
- Per-type computation of `[a,b]` and which types pass (i)–(iii).
- The minimal clause needed and its classification (faithfulness-FIT vs field-choice-CLAMP).
- Whether one principle unifies the Jordan and complex steps.
- One-line honest status for the SSOT.
