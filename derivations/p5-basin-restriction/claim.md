<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Pure-algebra / definitional. Type/category consistency is the dimensional-analysis analog. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/. -->

# claim.md — The RESTRICTION Claim (derivation notation, allowed inputs, prohibited moves, PAUSE conditions)

**Plan:** 60-01 (Phase 60, milestone v15.0) — DERV-60-04
**Role:** This file pins, in the derivation's own notation, the claim the v15.0 milestone
sets out to prove or disprove, the inputs the derivation is *allowed* to use, the
reward-hacking moves it is *forbidden* to make, and the conditions under which it must
**PAUSE** for a human decision. It governs Phases 60–63.

---

## Notation (derivation-local)

| Symbol | Category | Meaning |
|---|---|---|
| `h_3(O)` | FRJA | exceptional 27-dim formally real Jordan algebra (the universe "basin"); non-special, simple, BGW-non-composable |
| `A := h_3(C_u) ≅ M_3(C)^sa` | FRJA (special) | the maximal complex C*-target Jordan subalgebra inside `h_3(O)`, `u ∈ S^6 ⊂ Im(O)`; the **C*-bottleneck slice** (`lem:bottleneck`) |
| `E : h_3(O) -> A` | conditional expectation | a **positive unital idempotent** (conditional expectation) onto `A` (Effros-Störmer); `E∘E = E`, `E(1)=1`, `E ≥ 0` |
| `V_B, V_M` | OUS | the observer's body / model order-unit spaces |
| `phi : V_B -> V_M` | order isomorphism | faithful tracking map (clause ii) |
| `V_BM` | OUS (composite) | the observer's **minimal internal composite** OUS (clause iii) |
| `a & b := sqrt(a) · b · sqrt(a)` | binary op on effects | the self-modeling sequential product (Luders form, temporally asymmetric) |
| `V_0(E') , V_{1/2}(E') , V_1(E')` | Peirce subspaces | Peirce decomposition w.r.t. a rank-1 idempotent `E' ∈ A` (eigenvalues `0, 1/2, 1`) |

The four clauses of **Paper 5 Def 1** (`def:self-modeling-system`, main.tex line 342),
restated in this notation:

- **(i) `sms:finite`** — `V` is a nontrivial finite-dimensional **spectral** OUS (≥ 2
  orthogonal nontrivial projective units).
- **(ii) `sms:faithful`** — `phi: V_B -> V_M` is an **order isomorphism** (faithful
  tracking).
- **(iii) `sms:minimal`** — `V_BM` is the **minimal composite OUS** carrying *product
  states, product effects, non-signaling constraints, and product-form sequential
  product*. **[reproduced verbatim; see integrity guard below]**
- **(iv) `sms:simple`** — `V` has **no nontrivial direct-sum decomposition**
  (`V ≠ V_1 ⊕ V_2`).

---

## The claim: (RESTRICTION)

> **(RESTRICTION).** Let an observer be a finite faithful self-modeling system (Paper 5
> Def 1) embedded in `h_3(O)`, accessing it through the C*-bottleneck slice
> `A = h_3(C_u) ≅ M_3(C)^sa` of `lem:bottleneck`, reached by a positive unital conditional
> expectation `E : h_3(O) -> A` (Effros-Störmer). **CLAIM:** the slice `A` satisfies Paper
> 5 Def 1 **clause (iii)** (minimal internal composite / local tomography), and the
> observer's body-model composite `V_BM` required by clause (iii) is realized
> **coherently** as a sub-structure of `h_3(O)` **induced by the Peirce/bottleneck
> restriction** (`E`). Consequently Paper 5's theorem applies to the slice and certifies
> the observer's complex C* structure — **even though `h_3(O)` as a whole is
> non-composable.**

- **Prove it** ⟹ the "self-modeling → QM → this basin" through-line is **real**.
- **Disprove it** (exhibit a structural obstruction) ⟹ the observer's `C` and the basin's
  `O` are **independent posits**; the program concedes two unconnected foundations. *A
  clean obstruction is a fully acceptable, valuable outcome.*

### Clause-(iii) integrity guard (verbatim — NOT weakened)

The text of clause (iii), reproduced **verbatim** from `main.tex` `sms:minimal` (lines
351–353):

> (iii) `V_{BM}` is the minimal composite OUS carrying product states, product effects,
> non-signaling constraints, and product-form sequential product;

All four carried data — **product states**, **product effects**, **non-signaling
constraints**, **product-form sequential product** — plus **minimality** are part of the
claim and may **never** be dropped, relaxed, or "trivially satisfied by redefinition."

---

## Allowed inputs

The derivation (Phases 60–63) may use, as premises:

1. **Paper 5 Def 1** (`def:self-modeling-system`) — the four clauses, verbatim
   (`ref-paper5-def1`).
2. **Paper 5's composable/non-composable scoping remark** (main.tex lines 397–401, 165–168)
   — Def 1 characterizes *composable* self-modelers; the non-composable `h_3(O)` case is a
   separate companion-paper regime (`ref-paper5-def1`).
3. **`lem:bottleneck`** (complexification.tex line 409) — the C*-bottleneck universality
   lemma: ranges `A ≅ ⊕_k M_{n_k}(C)^sa`, `Σ n_k ≤ 3`; maximal `A ≅ M_3(C)^sa ≅ h_3(C_u)`,
   single `F_4`-orbit; rank-1 Peirce-0-space within the slice `≅ h_2(C_u) ≅ M_2(C)^sa`.
4. **BGW 2020** (Barnum–Graydon–Wilce) — FRJA composability / Jordan-monoidal composites;
   `h_3(O)` is the unique non-special simple FRJA and is non-composable (`ref-bgw`).
5. **Effros-Störmer 1979** — the range of a positive unital idempotent on a JB-algebra is a
   JB-subalgebra (justifies `E` and `A`).
6. **Hanche-Olsen** — universal tensor product of Jordan algebras; special vs exceptional
   (`ref-hanche-olsen`).
7. **Prior GPD results as context** — v6.0 / v8.0 / v11.0 / v13.0 algebraic results, and
   the v15.0 carry-forwards relevant to the embedding question (Phases 42, 46, 30: e.g.
   `sqrt(T_a) T_b sqrt(T_a)` behavior on Cl(9,0) pairs; Peirce closure of intrinsic
   `h_2(O)` in `V_0` with zero `V_{1/2}` leakage). These are **context**, not load-bearing
   premises for the distinction.

---

## Prohibited reward-hacking moves (DO NOT)

The claim must be **earned**. The following moves "prove" RESTRICTION fraudulently and are
**forbidden**:

1. **(fp-redefine-iii)** *Redefining clause (iii) to be trivially satisfied.* Do **not**
   weaken `sms:minimal` — do not drop product states, product effects, non-signaling, or
   the product-form sequential product, and do not relax "minimal." Clause (iii) is used
   **verbatim** as quoted above. *(This proxy formally attaches to a later claim/phase, but
   it is guarded at the source here.)*

2. **(fp-conflate-composites)** *Conflating the observer's `V_BM` with the BGW
   universe-tensoring of `h_3(O)`.* Do **not** argue "`h_3(O)` is non-composable, so the
   observer cannot have a composite either," nor the converse. `V_BM` (an OUS internal
   composite of the observer's body and model) and the BGW composite (a bifunctor tensoring
   the *whole* `h_3(O)` with an *external* FRJA) are **type-distinct objects**
   (see `two-composites.md`, Independence). Equating them is the **central** reward-hacking
   risk for Phase 60.

3. **(assert-Peirce-preserves-iii)** *Asserting the Peirce/bottleneck restriction preserves
   clause (iii) without demonstrating it on the actual non-associative `h_3(O)` structure.*
   The coherent-embedding step (Phase 62) must be **shown** on the real non-associative
   ambient — that `E`'s interaction with the sequential product `a & b = sqrt(a) b sqrt(a)`
   (not merely the Jordan product) is controlled, and that non-associativity does not leak
   in. Do **not** wave it through.

4. **(fp-converse-already-in-paper)** *Citing `rem:converse` as if it were already a
   labeled remark in the live `complexification.tex`, or treating its "minimal = maximal
   composite coincide for `M_n(C)^sa`" content as already-published.* `rem:converse` is
   **NOT** in the live paper (grep of `complexification.tex` finds `lem:bottleneck` but no
   `rem:converse`). It is **prompt-inline authoritative / to-be-produced**. Treat it as a
   *principle to confirm against BGW* (plan 60-02), never as published provenance.

**And:** do **NOT force a positive verdict** when the honest outcome is an obstruction. A
precisely-characterized obstruction is a fully acceptable deliverable.

---

## PAUSE conditions (milestone-level)

If any of the following is reached, **STOP** and surface a PAUSE for human decision rather
than papering over it:

1. **Two-composites collapse (PAUSE condition 1).** If the observer's `V_BM` and `h_3(O)`'s
   BGW non-composability cannot be distinguished non-circularly — i.e. on inspection they
   are revealed to be the **same object / construction**, or the independence cannot be
   argued without invoking RESTRICTION/embedding/slice-satisfaction (latent circularity) —
   then RESTRICTION is **circular/false**. Record a **DECISIVE NEGATIVE** and PAUSE.
   *(Status after plan 60-01: NOT triggered — distinction earned; see `two-composites.md`
   Independence (e) and `attempt-01.md`.)*

2. **Embedding needs structure not induced by `E` (PAUSE condition 2).** If the
   coherent-embedding step (Phase 62) requires the slice's clause-(iii) structure (its
   `V_BM`, its sequential product) to use structure on `A` that is **not** induced from the
   ambient `h_3(O)` by `E` — i.e. non-associativity leaks in, or `E` fails to transport the
   sequential product coherently — then there is a **structural obstruction**: `C` and `O`
   are independent posits. Record the obstruction precisely and PAUSE. *(This is the
   load-bearing, entirely-unproved step; Phase 62.)*

---

## Status (end of plan 60-01)

- Clause (iii) integrity: **intact** (verbatim, not weakened).
- `fp-conflate-composites`: **actively rejected** — the two composites proved type-distinct
  and logically independent, non-circularly (`two-composites.md` Independence).
- `fp-converse-already-in-paper`: **actively rejected** — `rem:converse` flagged
  prompt-inline, not-in-live-paper; BGW confirmation deferred to 60-02.
- Verdict: **UNDECIDED** (the milestone verdict; Phase 60 establishes only the distinction,
  step 1 of 4). No PAUSE triggered by plan 60-01.
