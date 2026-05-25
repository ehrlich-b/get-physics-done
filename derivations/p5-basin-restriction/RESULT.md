<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Pure-algebra: Jordan product a o b = (1/2)(ab+ba); sequential product a&b = sqrt(a) b sqrt(a) (CFC, principal branch, LEFT association in the ambient). Type/category + Peirce-grade consistency is the dimensional-analysis analog. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/. -->
<!-- Slice: A = h_3(C_u) ~ M_3(C)^sa (n=3; u = e_7; any u in S^6 equivalent under G_2). -->

# RESULT.md — Milestone verdict: the P5 ↔ Basin RESTRICTION Lemma

> **DRAFT — verdict line + finalization pending the 63-02 adversarial fresh-eyes review.**
> This file **assembles** the milestone verdict from the settled Phase 62 outcome; it does
> **not** recompute anything (every number is restated **verbatim** from `embedding-under-E.md`
> §4/§5, cross-checked against `62-03-SUMMARY.md`). The **one-sentence milestone verdict line**
> (DERV-00-02) and the removal of this **DRAFT** marker are **deliberately deferred to plan
> 63-02**, which runs the fresh-eyes adversarial guard review **before** finalization (ROADMAP
> Success Criterion 2: the review must **precede** finalization). Until 63-02's guard review
> passes, this stays a DRAFT.

**Plan:** 63-01 (Phase 63, milestone v15.0) — DERV-63-01 (draft). **Step 4 of 4.**
**Role:** The milestone deliverable. Reads the Phase 62 coherent-embedding verdict **(O)
AMBIENT-TRANSPORT OBSTRUCTION** into the milestone-level `RESTRICTION` verdict and interprets it
as a **REFINEMENT** of `RESTRICTION` to **coexistence-as-island** — the
"self-modeling → QM → `h_3(O)`" through-line **SURVIVES**.

---

## 1. The milestone and the four-step attack (recap)

**v15.0 = The P5 ↔ Basin RESTRICTION Lemma.** The milestone tests the load-bearing join between
Paper 5 (an observer is forced complex by **having a composite** — Def 1 clause (iii)) and
Paper 7 (the universe "basin" is forced octonionic by **non-composability** — `h_3(O)`). The
question (`claim.md`, `RESTRICTION`): does the C\*-bottleneck slice `A = h_3(C_u) ≅ M_3(C)^sa`
of `lem:bottleneck` carry Paper 5's structure, so that Paper 5's theorem certifies the observer's
complex QM **even though `h_3(O)` as a whole is non-composable**?

The attack ran in four steps (derivation-tree `STATE.md`, four-step table):

| Step | Phase | Description | State |
|---|---|---|---|
| 1 | **60** | **Two-composites distinction.** The observer's clause-(iii) `V_BM` is a *type-distinct* object from `h_3(O)`'s BGW non-composability (no circular collapse at step 1). | **COMPLETE** (60-01 distinction earned; 60-02 `rem:converse` CONFIRMED-WITH-CAVEAT against BGW) |
| 2 | **61** | **Slice satisfies clause (iii).** `A ≅ M_3(C)^sa` meets all four Def 1 clauses (i)–(iv) **intrinsically** (as a self-modeler in its own right). | **COMPLETE** (61-02 exact-symbolic evidence; 61-01 clause-by-clause; clause (iii) AS STATED via the minimal composite `M_9(C)^sa`, dim 81; `minimal ≠ maximal`) |
| 3 | **62** | **Coherent embedding under `E` (the hard/load-bearing part).** Does `E` *transport* the self-modeling structure from the non-associative ambient — or is there a precise obstruction? | **COMPLETE** — verdict **(O) AMBIENT-TRANSPORT OBSTRUCTION** (verifier 14/14 + 11/11 physics checks re-derived; consistency CONSISTENT; human-approved 2026-05-24) |
| 4 | **63** | **Verdict (this file).** A clean RESTRICTION theorem, or a precisely-characterized obstruction — read into the milestone verdict. | **THIS** (DRAFT; verdict line + finalization → 63-02 after the adversarial review) |

This file (Step 4) **assembles** Step 3's settled (O) verdict into the milestone-level
`RESTRICTION` verdict. Steps 1–3 are inputs, not re-derived here.

---

## 2. The CORRECTED governing frame (coexistence-as-island) — stated BEFORE the verdict

> **This frame is stated before the branch because it governs the verdict regardless of which
> branch the computation took** (`embedding-under-E.md` §5.2).

`RESTRICTION` needs **only** **COEXISTENCE-AS-ISLAND**. The CORRECTED embedding clause
(`claim.md`, Bryan 2026-05-24):

> *"the observer **self-models on the slice** `A = h_3(C_u)` (Phase 61, all four Def 1 clauses
> verbatim, intrinsically), which **sits inside `h_3(O)` as the range of the projection
> `E`**."*

Here **`E` is the ACCESS / PROJECTION map** — it is **NOT** required to be a Jordan morphism on
the ambient (and it is not: `E(X ∘ X) ≠ (EX) ∘ (EX)` for generic ambient `X`, §5). Whether `E`
**TRANSPORTS** the observer's structure — in particular the sequential product — **from the
ambient** is a **STRONGER, NOT-REQUIRED** property (the original wording's over-ask). The
observer does **not** need its structure derived from the ambient via `E`; it self-certifies on
the slice (Phase 61), and the slice **sits inside `h_3(O)` as `range E`**.

> **Reconciliation of the stale requirement texts (load-bearing).** The pre-correction phrasing
> in **ROADMAP Success Criterion 3**, **DERV-00-02**, and **DERV-63-01** — that an obstruction
> means the observer's `C` and the basin's `O` are *"independent posits"* / *"two unconnected
> foundations"* / a *"program collapse"* — is **SUPERSEDED** by Bryan's load-bearing 2026-05-24
> decision. The corrected, governing authority is **coexistence-as-island** (ROADMAP Phase 62/63
> **FRAMING NOTE**; `embedding-under-E.md` §5.2/§5.O.2; `claim.md` CORRECTED-FRAMING notes). An
> ambient-transport obstruction **REFINES** `RESTRICTION` to a self-contained C\* island; it does
> **NOT** establish independent posits and is **NOT** a program collapse. This file uses the
> corrected framing throughout; the stale phrasing appears below **only** as explicitly-negated
> or marked-superseded quotation, never to describe the (O) consequence affirmatively
> (`fp-overstate-obstruction`).

**Two integrity invariants the frame preserves** (carried verbatim from `claim.md` / §3.7):

- **(I) Clause (iii) is NOT weakened (`fp-redefine-iii`).** Clause (iii) stands **verbatim** —
  all four data (product states, product effects, non-signaling constraints, **product-form
  sequential product**) plus minimality — established **intrinsically** in Phase 61. **Only
  `RESTRICTION`'s embedding clause** is weakened. Weakening the embedding clause is **not** the
  same as weakening clause (iii).
- **(II) `V_BM` is NOT conflated with the ambient (`fp-conflate-composites`).** `V_BM = A ⊗ A ≅
  M_9(C)^sa` remains the observer's **OWN** internal composite, **never** identified with the
  BGW universe-tensoring `⊠̃` of `h_3(O)`. Coexistence-as-island is **fully consistent** with the
  Phase 60 two-composites distinction: the island has its own composite; the basin fixes the
  **TYPE** `M_3(C)^sa`, not the composite. (Consistent with U-B-M: Peirce `≠` tensor.)

---

## 3. The DECISIVE verdict: (O) AMBIENT-TRANSPORT OBSTRUCTION

> **`E` does NOT transport the self-modeling sequential product `a & b = sqrt(a) b sqrt(a)`
> coherently from the non-associative `h_3(O)`.** (Stated exactly as **computed** in Phase 62,
> **NOT forced**.)

The decisive object is the **ambient-transport residual** for **GENERIC ambient** `X, Y ∈ h_3(O)`
(off-diagonal octonion entries with nonzero `(e_1,…,e_6)`-parts — **not** confined to the slice):

$$
R \;:=\; E\big(\sqrt{X}\,Y\,\sqrt{X}\big) \;-\; \sqrt{EX}\,(EY)\,\sqrt{EX},
$$

where `sqrt(X)` is the **ambient** principal root (computed in the non-associative `h_3(O)` via
the exact-square trick `X = C·C`, so `sqrt(X) = C` exactly), and `sqrt(EX)` is the **slice**
(`M_3(C)`) root of the projected `EX ∈ A`. Per the §3.6 obstruction-or-preservation fork, exact
`R ≠ 0 ⇒` branch **(O)**.

**The exact Phase 62 result (`embedding-under-E.md` §4.2/§5.1, restated verbatim):**

$$
\boxed{\;R \;\neq\; 0 \quad(\text{exact}),\qquad \texttt{is\_zero\_exact} = [\text{False}, \text{False}].\;}
$$

- **Pair 0 (clean rational pair):** `R ≠ 0` exactly; `||R||_F^2 = 38593/72` (≈ 536).
  Representative exactly-nonzero entry **`R_{11} = -2`** — an `O(1)` **rational, no surd**, so the
  residual is **definitively nonzero, not float round-off** and not an accidental cancellation.
- **Pair 1 (second generic pair):** `R ≠ 0` exactly;
  `||R||_F^2 = 127725937/64800 - 13·sqrt(67134)/2 - 277·sqrt(183513)/900` (≈ 155); representative
  exactly-nonzero entry `R_{11} = 1/6`.

The exact-arithmetic harness asserts only the **honest consistency** `octmat_is_zero(R) ⟺
is_zero_exact` — it does **not** hardcode (P) or (O). Both generic pairs gave `R ≠ 0`. **This is
branch (O) of the §3.6 fork.** One exact nonzero residual on non-associativity-load-bearing
generic data **suffices** to establish (O); **two** were found.

---

## 4. The verdict TOUCHES the actual non-associative structure (anti-reward-hack)

The verdict is grounded in the **genuinely non-associative** `h_3(O)`, not a trivial corner.

**(a) Non-associativity is LOAD-BEARING on the SAME decisive triple `(sqrt(X), Y, sqrt(X))`.**
On the *same* `(X, Y)` whose residual is `R` (clean pair), the associator of the decisive triple
is **exactly nonzero** (`embedding-under-E.md` §4.2, restated verbatim):

$$
\big\|(\sqrt{X}\,Y)\,\sqrt{X} \;-\; \sqrt{X}\,(Y\,\sqrt{X})\big\|_F^2 \;=\; \tfrac{524}{9} \;\neq\; 0
\qquad(\text{exact}).
$$

So the decisive test genuinely exercises `(xy)z ≠ x(yz)` — it is **not** an
accidentally-associative corner (`fp-ignore-nonassociativity` rejected).

**(b) `E` is NOT a Jordan morphism on the ambient.** Even the (less rigid) Jordan structure is
not transported by `E` from the ambient (`embedding-under-E.md` §4.2(1), restated verbatim):

$$
\big\|E(X \circ X) \;-\; (EX) \circ (EX)\big\|_F^2 \;=\; \tfrac{3797527}{34560000} \;\neq\; 0
\qquad(\text{exact}).
$$

A fortiori the **sequential product** (an even more rigid CFC triple product) need not be — which
is exactly what makes the ambient-transport question genuinely non-trivial rather than a corollary
of `lem:bottleneck`.

**(c) The slice-internal case is the TRIVIAL CONTROL — named as such, NOT the decisive test.**
For `a, b ∈ A`, the slice `A = h_3(C_u) ≅ M_3(C)^sa` is a **closed, associative** Jordan
subalgebra (`= range E`), so `sqrt(a) b sqrt(a) ∈ A` with **leakage EXACTLY 0**
(`E(sqrt(a) b sqrt(a)) = sqrt(a) b sqrt(a)`) and triple **associator EXACTLY 0**. This is the
limit where non-associativity is switched off; it carries **no** information about ambient
transport. It is recorded strictly as the control. **The verifier independently re-ran a
slice-confined control yielding `R = 0`**, which **PROVES the test genuinely CAN yield branch
(P)** — so the (O) result is **NOT rigged** (`fp-assert-preservation`, `fp-force-positive`
rejected; the harness does not hardcode the branch).

---

## 5. Precise obstruction characterization

**(a) What `E` cannot transport.** The **product-form sequential-product datum** (clause (iii)'s
fourth datum, the actual `sqrt(a) b sqrt(a)` — `fp-redefine-iii` rejected) from the ambient. For
generic ambient `X, Y`: `E(sqrt(X) Y sqrt(X)) ≠ sqrt(EX)(EY)sqrt(EX)` (exact, `R ≠ 0`).

**(b) Where the defect lives — INSIDE `A`, not leakage out of it.** Both `E(sqrt(X) Y sqrt(X))`
and `sqrt(EX)(EY)sqrt(EX)` lie in `A` (since `E` projects **every** matrix entry onto `C_u`), so
the residual `R` is a genuine **slice element**. The all-entry `C_u`-vs-`(e_1,…,e_6)` split
(clean pair) gives (`embedding-under-E.md` §5.O.1(b), restated verbatim):

$$
\big(\text{$C_u$-part}\big)^2 = \tfrac{38593}{72}, \qquad \big((e_1,\dots,e_6)\text{-part}\big)^2 = 0,
$$

summing to `||R||_F^2 = 38593/72`. So the obstruction is the **failure of the two slice elements
to coincide**, **NOT** leakage out of `A`.

**(c) Positional `E_11` Peirce-grade decomposition (the pure-algebra dimensional-analysis
self-check).** The positional `E_11` Peirce grades partition the nine matrix entries (faithful for
the non-Hermitian defect — see (e)), so the grade magnitudes **sum exactly** to `||R||_F^2`
(`embedding-under-E.md` §5.O.1(b), restated verbatim):

$$
\|V_1(R)\|^2 = 4,\qquad \|V_{1/2}(R)\|^2 = \tfrac{1033}{18},\qquad \|V_0(R)\|^2 = \tfrac{3797}{8},
$$

$$
\boxed{\;4 \;+\; \tfrac{1033}{18} \;+\; \tfrac{3797}{8} \;=\; \tfrac{288}{72} + \tfrac{4132}{72} + \tfrac{34173}{72} \;=\; \tfrac{38593}{72} \;=\; \|R\|_F^2.\;}
$$

(Verified exactly: `288 + 4132 + 34173 = 38593`.) The defect is **spread across all three Peirce
grades** — dominantly `V_0` (the `h_2(C_u) ≅ M_2(C)^sa` block), then `V_{1/2}` (the `C_u^2`
interface), with a **nonzero `V_1` scalar bottleneck component** `||V_1(R)||^2 = 4`.

**(d) Mechanism.** The ambient `sqrt(X) Y sqrt(X)` populates `(e_1,…,e_6)`-components that `E`
then projects away; `E` applied **after** the ambient triple product retains contributions from
the killed directions that `sqrt(EX)(EY)sqrt(EX)` (built **entirely inside `A`**) never sees, so
the two `C_u`-images differ.

**(e) Sharpening — non-Hermiticity (new Phase 62 finding).** The ambient sequential product
`sqrt(X) Y sqrt(X)` is itself **NOT Hermitian** in `h_3(O)`: the would-be involution identity
`(sqrt(X) Y sqrt(X))† = sqrt(X) Y sqrt(X)` **fails** because `(AB)C ≠ A(BC)`. (The left
association `(sqrt(X) Y) sqrt(X)` leaves the formally-real Jordan cone; the SP is
association-dependent in the ambient — the left association is used throughout, and the
obstruction holds for it and for any fixed association.) This is an **additional**,
association-dependent way `E` fails to transport the SP coherently, on top of `R ≠ 0` — it
reinforces (O), and is why the defect `R` is characterized with the **positional** `E_11` Peirce
grading and the all-entry `C_u`/`(e_1,…,e_6)` split (faithful for non-Hermitian matrices), **not**
a Hermitian-coordinate reconstruction.

**(f) Rank bookkeeping (the type-consistency analog).** `27 = 9 (= dim range E) + 18 (= dim ker
E)`; the slice Peirce bookkeeping is `9 = 1 + 4 + 4` (`V_1 ≅ R`, `V_{1/2} ≅ C_u^2`, `V_0 ≅
h_2(C_u) ≅ M_2(C)^sa`). Both hold exactly.

**Trustworthiness (carried from §4.4/§5.5).** Two independent routes — the direct ambient
residual `R` and the positional-Peirce/grade-component decomposition — **agree** on (O) for both
generic pairs (the harness raises on a split decision; none occurred). The arithmetic is **exact**
(SymPy, zero tolerance on the decisive assertion); `R_{11} = -2` is an exact rational, excluding
float round-off and accidental cancellation; the exact-square trick `X = C·C` is documented and
**confirmed not to trivialize non-associativity** (associator `= 524/9 ≠ 0` on the same `X, Y`).

---

## 6. The program consequence — coexistence-as-island (the through-line SURVIVES)

Under (O), the consequence for the Radical Relativity program is **coexistence-as-island**
(`embedding-under-E.md` §5.O.2):

- **The observer is a self-contained C\* island.** It self-certifies its `M_3(C)^sa` QM **on the
  slice** `A = h_3(C_u)` (Phase 61, all four Def 1 clauses **verbatim**, **intrinsically**), and
  the slice **sits inside `h_3(O)` as the range of the projection `E`**.
- **The through-line SURVIVES** as the **island through-line**:

  > **`h_3(O)` is the basin whose maximal C\* slice is `M_3(C)^sa`, on which Paper 5 certifies the
  > observer's QM; `E` is the access/projection map.**

  `E` is **not** required to be a Jordan morphism (it is not — §4(b)) nor an SP-morphism (it is
  not — §3) on the ambient. The basin **fixes the TYPE** `M_3(C)^sa`; it does **not** transport
  the observer's structure. **(P)** would have given the **stronger** "induced from the ambient"
  through-line; **(O)** gives the **island** through-line. **Both branches give a coherent
  through-line — the fork chooses WHICH through-line, not WHETHER there is one.**

- **(O) does NOT establish "independent posits / two unconnected foundations" and is NOT a program
  collapse.** It **REFINES** `RESTRICTION` to a self-contained C\* island. The stale
  PAUSE-condition-2 framing ("obstruction ⇒ `C` and `O` independent posits, PAUSE") is
  **superseded** by coexistence-as-island for the embedding clause (Bryan 2026-05-24; `claim.md`
  CORRECTED notes). A clean (O) is the **EXPECTED, ACCEPTABLE, valuable** deliverable, surfaced
  and human-acknowledged at the 62-03 interactive checkpoint — **not** a fraudulent force-pass and
  **not** a collapse.

- **Consistent with U-B-M (`fp-conflate-composites` preserved).** Peirce `≠` tensor; the basin
  fixes the **TYPE** `M_3(C)^sa`, not the composite. The observer's own composite `V_BM = A ⊗ A ≅
  M_9(C)^sa` is **never** identified with the BGW universe-tensoring `⊠̃` of `h_3(O)`. The Phase 60
  two-composites distinction stands.

- **Asymmetry respected (project memory: basin-only vs observer+basin).** This (O) concerns
  **only** whether the observer's complex structure is **TRANSPORTED by `E` from the
  non-associative basin** — the stronger, now-not-required property. It does **NOT** downgrade
  Paper 7's separate complexification claim, nor Paper 5's / Phase 61's **intrinsic** result (the
  slice satisfies clause (iii) in its own right). The obstruction is characterized at **exactly
  that join** (ambient `E`-transport of the SP) and is **not** over-generalized into "independent
  posits."

---

## 7. What would have to change to close the obstruction

Ambient transport — the **stronger, NOT-required** property — would need the SP's
`(e_1,…,e_6)`-content (the part of `sqrt(X) Y sqrt(X)` that does **not** survive the projection
`E`) to be recoverable from the **slice data alone**. It is **not**: `E` discards exactly those
directions (`ker E`, real-dim **18**), and the exact residual confirms the discarded content
changes the `C_u`-image (`embedding-under-E.md` §5.O.1(c)).

In **Hanche-Olsen induced-vs-imported** terms: `E` does **not INDUCE** the sequential-product
datum from `h_3(O)`; ambient transport would require **IMPORTING** an external datum on `h_3(O)`
**not in `range E`** — concretely, a rule fixing how the killed `(e_1,…,e_6)`-content feeds back
into the `C_u`-image. No such rule is supplied by `E`, and §3–§5 show the naive "project and
compute in `A`" route disagrees with "compute in the ambient and project."

> **WEAKEST ANCHOR (flagged; not inflated).** This **minimal extra input** is the
> **least-certain** part of the analysis. It is stated as precisely as the evidence allows (an
> external datum on `h_3(O)` not in `range E`, via Hanche-Olsen induced-vs-imported) and flagged
> for the 63-02 review / future work — **NOT** overstated (`fp-force-positive` over-claim guard).
> **NOTE explicitly: coexistence-as-island does NOT require this extra input AT ALL.** The
> observer already self-models on the slice (Phase 61), which sits inside `h_3(O)` as `range E`;
> the minimal extra input is **only** what the stronger AMBIENT TRANSPORT would need. The island
> claim needs none of it.

---

## 8. What is NOT decided here (handoff to 63-02)

This file is a **DRAFT**. The following are **deliberately deferred to plan 63-02**, which runs
the fresh-eyes adversarial guard review **before** finalization (ROADMAP Success Criterion 2 — the
review must **precede** finalization):

- **The one-sentence milestone verdict LINE (DERV-00-02)** is **NOT written here.** (It belongs to
  63-02, after the adversarial review passes.)
- **The DRAFT marker is NOT removed here** and finalization is **NOT** declared
  (`fp-overclaim-milestone` — the milestone verdict stays UNDECIDED until 63-02).
- **The adversarial fresh-eyes review of the three reward-hacking guards** is 63-02's job:
  (i) clause (iii) **not redefined** (only the embedding clause weakened);
  (ii) the **two composites not conflated** (`V_BM ≠` the ambient BGW `⊠̃`);
  (iii) **preservation not asserted** without demonstration on the actual non-associative `h_3(O)`
  (the decisive test was the **ambient** residual on generic `X, Y` with the associator `= 524/9`
  load-bearing).
  A backtracking trigger would fire only on a **guard violation** found at review — a
  contingency, not expected.

Until 63-02's guard review passes, this RESULT.md remains a DRAFT.

---

## 9. Numbers ledger (restated, NOT re-derived)

Every exact number above is restated **verbatim** from the Phase 62 deliverable; the source
section is given so the 63-02 reviewer and the verifier can cross-check transcription. **No number
in this file is re-derived or approximated.**

| Quantity | Exact value | Source (verbatim) | Cross-check |
|---|---|---|---|
| Ambient-transport residual norm (clean pair 0) | `‖R‖_F² = 38593/72` (≈ 536) | `embedding-under-E.md` §4.2(4), §5.1 | `62-03-SUMMARY.md` Eq. (62.9), Key Results |
| Representative residual entry (pair 0) | `R_{11} = -2` (exact rational, no surd) | `embedding-under-E.md` §4.2(4), §5.1 | `62-03-SUMMARY.md` Eq. (62.9) |
| Residual norm (pair 1) | `‖R‖_F² = 127725937/64800 - 13·√67134/2 - 277·√183513/900` (≈ 155) | `embedding-under-E.md` §4.2(4) | `STATE.md` (≈155 second pair) |
| Representative residual entry (pair 1) | `R_{11} = 1/6` | `embedding-under-E.md` §4.2(4) | — |
| Decisive-triple associator (same `X,Y`) | `‖(√X Y)√X − √X(Y√X)‖² = 524/9` (≈ 58.2) | `embedding-under-E.md` §4.2(3), §5.1 | `62-03-SUMMARY.md` Eq. (62.10) |
| `E` not a Jordan morphism on ambient | `‖E(X∘X) − (EX)∘(EX)‖_F² = 3797527/34560000` (≈ 0.110) | `embedding-under-E.md` §4.2(1), §5.O.1(a) | `62-03-SUMMARY.md` Eq. (62.12) |
| Peirce grade `V_1` of `R` | `‖V_1(R)‖² = 4` | `embedding-under-E.md` §4 char., §5.O.1(b) | `62-03-SUMMARY.md` Eq. (62.11) |
| Peirce grade `V_{1/2}` of `R` | `‖V_{1/2}(R)‖² = 1033/18` | `embedding-under-E.md` §4 char., §5.O.1(b) | `62-03-SUMMARY.md` Eq. (62.11) |
| Peirce grade `V_0` of `R` | `‖V_0(R)‖² = 3797/8` | `embedding-under-E.md` §4 char., §5.O.1(b) | `62-03-SUMMARY.md` Eq. (62.11) |
| Peirce-grade sum (self-check) | `4 + 1033/18 + 3797/8 = 38593/72 = ‖R‖_F²` | `embedding-under-E.md` §5.O.1(b) | LCD-72: `288/72 + 4132/72 + 34173/72`; ✓ exact |
| All-entry split (pair 0) | `C_u`-part² `= 38593/72`, `(e_1…e_6)`-part² `= 0` | `embedding-under-E.md` §5.O.1(b) | sums to `‖R‖_F²` |
| Rank bookkeeping | `27 = 9 (range E) + 18 (ker E)` | `embedding-under-E.md` §0.2 | ✓ exact |
| Slice Peirce bookkeeping | `9 = 1 + 4 + 4` (`V_1 ≅ R`, `V_{1/2} ≅ C_u²`, `V_0 ≅ M_2(C)^sa`) | `embedding-under-E.md` §1.4 | ✓ exact |
| Verdict branch | **(O)** (exact `R ≠ 0`; `is_zero_exact = [False, False]`) | `embedding-under-E.md` §4.3, §5.1 | `62-03-SUMMARY.md` verdict (O) |

---

## 10. Type/category + Peirce self-audit

| Load-bearing object / claim | Subject category | Type-correct? |
|---|---|---|
| decisive residual `R = E(√X Y √X) − √(EX)(EY)√(EX)` | residual in `h_3(O)` for **generic ambient** `X,Y` | ✓ (generic ambient; associator `= 524/9 ≠ 0` load-bearing) |
| sequential product `a & b = √a b √a` | **CFC triple product on effects** (NOT a Jordan op) | ✓ (clause (iii) datum 4; never treated as a Jordan op) |
| slice-internal `√a b √a` (`a,b ∈ A`) | **TRIVIAL control** (closed associative subalgebra) | ✓ (leakage 0, associator 0; tagged control, not decisive) |
| `E : h_3(O) → A` | **access / projection map** (positive unital idempotent) | ✓ (NOT a Jordan morphism nor SP-morphism on the ambient) |
| clause (iii) | OUS composite datum, **verbatim** | ✓ (UNCHANGED — only `RESTRICTION`'s embedding clause weakened) |
| `V_BM = A ⊗ A ≅ M_9(C)^sa` | observer's OWN OUS self-composite | ✓ (NOT conflated with BGW `⊠̃` on `h_3(O)`) |
| verdict (O) | ambient-transport obstruction → coexistence-as-island | ✓ (EXPECTED; refines `RESTRICTION` to island; NOT forced, NOT a collapse) |
| milestone verdict | `RESTRICTION` milestone | ✓ (UNDECIDED — verdict line + finalization to 63-02) |
| Peirce-grade arithmetic | `4 + 1033/18 + 3797/8 = 38593/72` | ✓ (dimensional-analysis analog; verified exactly) |
| v11.0/Phase 42 precedent | historically adjacent (Clifford pairs) | ✓ (NOT carried as evidence — different mechanism) |

**Forbidden proxies — all REJECTED in this assembly:** `fp-force-positive` (both directions:
verdict (O) = the exact computation, not forced to (P); and (O) reported as the expected
coexistence-as-island refinement, **not** over-stated as a collapse/"independent posits");
`fp-overstate-obstruction` (the stale "independent posits / two unconnected foundations / program
collapse" phrasing is used **only** as explicitly-negated/marked-superseded quotation; the
through-line is stated to SURVIVE); `fp-vague-verdict` (a single DECISIVE branch (O), no "mostly
works"/"broadly preserved"/"largely consistent" hedging); `fp-not-touch-nonassociative` (the
associator `= 524/9 ≠ 0` load-bearing on the **same** generic `X,Y`; the slice-internal case named
the trivial control); `fp-redefine-iii-result` (clause (iii) unchanged; `V_BM` not conflated with
the BGW universe-tensoring); `fp-attempt-fabricate` (N/A here — the attempt-log audit is Task 2).

**[CONFIDENCE: HIGH]** that the milestone verdict, **as assembled**, is the (O) ambient-transport
obstruction refining `RESTRICTION` to **coexistence-as-island**, with every number matching the
Phase 62 deliverable verbatim (cross-checked against `62-03-SUMMARY.md`) and the Peirce-grade
self-check `4 + 1033/18 + 3797/8 = 38593/72` holding exactly. *Independent checks supporting HIGH:*
(i) the Peirce-grade arithmetic re-verified exactly here (LCD-72); (ii) rank bookkeeping `27 = 9 +
18` and slice Peirce `9 = 1 + 4 + 4` re-verified; (iii) cross-artifact number consistency (`§4/§5`
↔ `62-03-SUMMARY.md`); (iv) the framing matches the corrected governing authority (`claim.md`
CORRECTED notes, ROADMAP FRAMING NOTE). **[CONFIDENCE: explicitly DEFERRED — the milestone verdict
LINE and finalization]:** NOT written here; owned by 63-02 after the adversarial guard review
(ROADMAP Success Criterion 2). **[CONFIDENCE: flagged weakest anchor]:** the Hanche-Olsen minimal
extra input (§7) — stated as precisely as the evidence allows, not inflated; coexistence-as-island
does not require it.

---

_Plan: 63-01 (Phase 63, milestone v15.0) — DERV-63-01 (DRAFT). Step 4 of 4._
_Assembles the Phase 62 verdict (O) (`embedding-under-E.md` §4/§5; `62-03-SUMMARY.md`,
human-approved 2026-05-24) into the milestone coexistence-as-island `RESTRICTION` verdict._
_Verdict LINE (DERV-00-02) + finalization (remove DRAFT) deferred to 63-02, after the adversarial
guard review (ROADMAP Success Criterion 2)._
