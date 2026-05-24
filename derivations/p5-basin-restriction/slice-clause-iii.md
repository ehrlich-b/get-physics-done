<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Pure-algebra clause-by-clause verification. No numerics in THIS file; the quantitative -->
<!-- witnesses are the exact-symbolic 61-02 SymPy deliverable, cited at point of use. -->
<!-- The "dimensional-analysis" requirement maps to TYPE/CATEGORY consistency + OUS dimension bookkeeping. -->
<!-- Provenance: LIVE papers only (~/repos/blog/landing/papers/). NOT the stale repo papers/ copy. -->
<!-- Slice: A = h_3(C_u) ~ M_3(C)^sa (n = 3; complex structure u = e_7; any u in S^6 equivalent under G_2). -->

# slice-clause-iii.md — The slice `A = M_3(C)^sa` satisfies Paper 5 Def 1 (i)–(iv) as a self-modeler in its own right

**Plan:** 61-01 (Phase 61, milestone v15.0) — DERV-61-01 (clause i), DERV-61-02 (clause iv),
DERV-61-03 (rem:converse corrected ⇒ clauses ii, iii); cites VALD-61-01 (61-02 SymPy).
**Step:** 2 of the v15.0 four-step attack (Phase 61).
**Purpose:** Verify that the C\*-bottleneck slice `A = h_3(C_u) ≅ M_3(C)^sa` (`lem:bottleneck`,
`n = 3`) meets **all four** clauses of Paper 5 Definition 1 (`def:self-modeling-system`) **as a
self-modeler IN ITS OWN RIGHT (intrinsically)** — clauses (i) and (iv) verified **directly** for
`M_3(C)^sa`, clauses (ii) and (iii) supplied by **`rem:converse` in its CORRECTED
direct-summand form** (Phase 60, `rem-converse-bgw.md`). Clause (iii) is checked **AS STATED**
(all four data, minimality in full force), the clause-(iii) object being the **minimal** composite
`M_9(C)^sa` (real-dim 81). Every quantitative claim **cites the 61-02 exact-symbolic SymPy
evidence** (`code/slice_clause_iii_verification.py`, `tests/test_slice_clause_iii.py`), not an
estimate or "looks right."

**Scope of what this file does and does NOT claim.**
- **DOES:** establish that `A = M_3(C)^sa`, considered as a Jordan algebra / OUS in its own
  right, is a finite faithful self-modeling system in the sense of Paper 5 Def 1.
- **Does NOT:** claim that this four-clause structure is **coherently induced by the conditional
  expectation `E`** from the non-associative ambient `h_3(O)`. That is the **Phase 62** question
  (the load-bearing, entirely-unproved step) and is **explicitly deferred** (§6). No step here uses
  `RESTRICTION`, `E`, or slice-induction as a premise.

---

## 0. Setup, inputs, and the type/category ledger

### 0.1 The slice and the self-model `rem:converse` instantiates

From `lem:bottleneck` (`~/repos/blog/landing/papers/sm-from-self-modeling/sections/`
`complexification.tex`, `\label{lem:bottleneck}` line 409): the maximal C\*-target Jordan
subalgebra inside the universe basin `h_3(O)` is

$$ A \;=\; h_3(C_u) \;\cong\; M_3(\mathbb{C})^{sa}, \qquad n = 3, \quad u \in S^6 \subset \operatorname{Im}(\mathbb{O}) \ (\text{single } F_4\text{-orbit}). $$

The self-model that `rem:converse` instantiates for `A` (see `rem-converse-bgw.md` §1):

$$ V \;=\; V_B \;=\; V_M \;=\; M_3(\mathbb{C})^{sa}, \qquad \varphi \;=\; \mathrm{id}: V_B \to V_M, \qquad V_{BM} \;=\; M_3(\mathbb{C})^{sa} \otimes M_3(\mathbb{C})^{sa} \;\cong\; M_9(\mathbb{C})^{sa}. $$

Paper 5 Def 1 is a tuple `(V, φ, V_BM)`; clauses (i) and (iv) constrain the single OUS `V`,
clause (ii) constrains `φ: V_B → V_M`, clause (iii) constrains `V_BM`. With `V = V_B = V_M`, the
intrinsic clauses (i)/(iv) are checked on `M_3(C)^sa` and the relational clauses (ii)/(iii) on the
identity tracking map and the minimal self-composite.

### 0.2 Paper 5 Definition 1 — verbatim (LIVE paper, re-read this plan)

Re-read from `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`,
`\label{def:self-modeling-system}` (line 342), clauses at lines 346–356 (verbatim, confirms the
quotes already carried in `rem-converse-bgw.md` §1, §3):

> **(i) `\label{sms:finite}`** `$V$` is a nontrivial finite-dimensional spectral order unit space
> (i.e., `$V$` has at least two orthogonal nontrivial projective units);
>
> **(ii) `\label{sms:faithful}`** `$\varphi: V_{B} \to V_{M}$` is an order isomorphism (faithful
> tracking);
>
> **(iii) `\label{sms:minimal}`** `$V_{BM}$` is the minimal composite OUS carrying product states,
> product effects, non-signaling constraints, and product-form sequential product;
>
> **(iv) `\label{sms:simple}`** `$V$` has no nontrivial direct-sum decomposition: there is no
> splitting `$V = V_1 \oplus V_2$` into nonzero order-unit subspaces.

Unpacking of `sms:minimal` (main.tex lines 375–384, verbatim): *"If the body–model composite
carried states that product measurements could not distinguish, those states would be opaque to the
self-modeler … Minimality says: the composite has no such hidden structure."*

### 0.3 Type/category ledger (the pure-algebra analog of dimensional analysis)

Carried from `two-composites.md` and `rem-converse-bgw.md` §0. Every object carries **one**
category tag; no inference equates objects of different tags. (Full self-audit in §7.)

| Object | Category tag | What it is |
|---|---|---|
| `A = M_3(C)^sa` (`= h_3(C_u)`) | **FRJA (special, simple)** = BGW `C_3` | the slice; the OUS `V = V_B = V_M` |
| `V_BM = M_9(C)^sa` | **FRJA (special, simple)** carrying OUS structure | the **minimal** internal composite (clause iii object); real-dim **81** |
| maximal `C_3 ⊠̃ C_3 = M_9(C)^sa ⊕ M_9(C)^sa` | **FRJA (special, NOT simple)** | the **universal** composite; real-dim **162** (extra classical bit); **NOT** the clause (iii) object |
| `φ = id : V_B → V_M` | **order isomorphism** | faithful tracking (clause ii) |
| BGW bifunctor `⊠̃` on `h_3(O)` | **bifunctor / monoidal** | tensoring the *whole* universe with an external FRJA; `h_3(O)` is BGW-**non**-composable |
| `E : h_3(O) → A` | **conditional expectation** | **forward reference only** — used in Phase 62, **NOT** here |

> **Dimensional-analysis analog stated up front:** "minimal vs maximal" is a **same-category**
> comparison (FRJA-composite ↔ FRJA-composite); its answer is **NOT-equal** (`81 ≠ 162`). `V_BM`
> (OUS internal self-composite, body⊗model) is **never** identified with the BGW `⊠̃` evaluated on
> `h_3(O)` (bifunctor). These are the two type-consistency invariants this file preserves.

### 0.4 Evidence base (61-02, VALD-61-01) — independently re-confirmed this plan

The exact-symbolic SymPy deliverable `code/slice_clause_iii_verification.py` (+ pytest harness
`tests/test_slice_clause_iii.py`, 21 tests) was **re-run at execution start of this plan**:
`OVERALL: ALL CHECKS PASS`, exit 0. It establishes, by **exact** rational/surd arithmetic (no float
tolerance):

| Datum | 61-02 result | Used in |
|---|---|---|
| Jordan rank of `M_3(C)^sa` | **3** — three mutually orthogonal nontrivial rank-1 projective units `E_11,E_22,E_33`, Jordan- and matrix-orthogonal, `Σ = I_3`; **frame-independent** (standard + rotated unitary frames) | clause (i) |
| simplicity | center`(M_3(C)) = C·I_3`; only central idempotents are `0, I_3` (`λ²=λ ⇒ λ∈{0,1}`) | clause (iv) |
| minimal composite real-dim | **81 = 9·9** = `dim_R M_9(C)^sa` (`kron` of two `3×3` Hermitians lands in `M_9(C)^sa`) | clause (iii) object |
| maximal composite real-dim | **162 = 2·81 ≠ 81** (extra classical bit; BGW) | clause (iii) contrast |
| product-form sequential product | `√a · b · √a` on the full `9×9` **equals** `(a_B & b_B) ⊗ (a_M & b_M)` **exactly**, via `√(a_B⊗a_M)=√a_B⊗√a_M`; S3 unitality `I_9 & a = a`; `a&b` an effect | clause (iii) datum 4 |

All five are the **standard, known** structure of `M_3(C)^sa`; per the plan, a *failure* of any one
would be a **backtracking trigger** (revisit the Phase 60 framing), not a force-pass. **No failure
occurred.**

---

## CLAUSE (i) — `sms:finite` (DERV-61-01) — verified DIRECTLY

**Statement to verify:** `V = M_3(C)^sa` is a nontrivial finite-dimensional **spectral** order-unit
space with **at least two** orthogonal nontrivial projective units.

1. **Finite-dimensional OUS.** `M_3(C)^sa = { 3×3 H : H = H† }` is a real vector space of dimension
   `9` (3 real diagonal + 3 complex off-diagonal = 3 + 6), with order unit the identity `I_3` and
   positive cone the PSD matrices. 61-02 verifies `dim_R(M_3(C)^sa) = 9` and that the general
   `3×3` builder is Hermitian (`H = H†`, exact symbolic). Finite-dimensional ✓; nontrivial
   (`V ≇ R`, it has nontrivial projective units — item 3) ✓.

2. **Spectral.** Every self-adjoint complex `3×3` matrix has a spectral decomposition into real
   eigenvalues with mutually orthogonal eigenprojections (finite-dimensional spectral theorem). So
   `M_3(C)^sa` is a spectral OUS. ✓

3. **At least two orthogonal nontrivial projective units — in fact exactly three (Jordan rank 3).**
   `M_3(C)^sa` has Jordan rank 3: the three matrix-unit diagonal projections

   $$ E_{11} = e_1 e_1^\dagger,\quad E_{22} = e_2 e_2^\dagger,\quad E_{33} = e_3 e_3^\dagger $$

   are mutually orthogonal nontrivial rank-1 projective units satisfying (61-02, Eq. 61.1)

   $$ E_{ii}^2 = E_{ii},\qquad E_{ii} = E_{ii}^\dagger,\qquad \operatorname{rank} E_{ii} = 1 \ (\neq 0,\ \neq I_3),\qquad E_{ii}\circ E_{jj} = \tfrac12(E_{ii}E_{jj}+E_{jj}E_{ii}) = 0\ (i\neq j),\qquad E_{11}+E_{22}+E_{33} = I_3. $$

   **CITE 61-02 (VALD-61-01):** `check_rank_three_units` proves, by exact symbolic computation,
   that `E_11,E_22,E_33` are each a nontrivial rank-1 projection, are mutually Jordan- **and**
   matrix-orthogonal, and sum to `I_3`; that the rank caps at 3 (`I_3 − ΣE_ii = 0_3`, no room for a
   4th orthogonal nonzero projective unit); and that **the same three-unit resolution of identity
   holds in a fixed rotated/phase unitary frame** — so this is the *intrinsic* Jordan rank, not a
   basis artifact. This is the explicit projective-unit computation the roadmap demands.

   `rank = 3 ≥ 2` ⇒ the "at least two orthogonal nontrivial projective units" requirement is met
   **with strict margin**.

**Clause (i) holds for `M_3(C)^sa`. ✓** (Direct verification + 61-02 exact-symbolic evidence.)

> **Type/category check (clause i):** all objects here are inside the single special simple FRJA
> `M_3(C)^sa` (OUS-level). No cross-category step. ✓

---

## CLAUSE (ii) — `sms:faithful` (DERV-61-03) — supplied via `rem:converse`

**Statement to verify:** `φ: V_B → V_M` is an order isomorphism (faithful tracking).

Instantiate `rem:converse` for `n = 3` (`rem-converse-bgw.md` §1): take

$$ V_B \;=\; V_M \;=\; M_3(\mathbb{C})^{sa}, \qquad \varphi \;=\; \mathrm{id} : V_B \to V_M. $$

The identity map is **trivially an order isomorphism**: it is a linear bijection, and `x ≥ 0 ⇔
id(x) ≥ 0` since the orders on `V_B` and `V_M` are the *same* PSD cone on `M_3(C)^sa`. Hence `φ`
preserves all operationally accessible (order) structure — faithful tracking in Paper 5's sense
(main.tex line 349, verbatim: *"`$\varphi: V_{B} \to V_{M}$` is an order isomorphism (faithful
tracking)"*).

**Clause (ii) holds. ✓** (Via `rem:converse`, corrected-form instantiation; `φ = id`.)

> **Provenance guard (clause ii):** `rem:converse` is used as a **prompt-inline authoritative
> principle confirmed against BGW in Phase 60**, NOT cited as an already-published labeled remark in
> the live `complexification.tex` (grep-verified absent there, Phase 60; FUTR-01 will insert the
> corrected remark). See §6.2 and `fp-converse-already-in-paper`.

> **Type/category check (clause ii):** `φ` is an order-isomorphism between two copies of the OUS
> `M_3(C)^sa`. Same-category (OUS ↔ OUS). ✓

---

## CLAUSE (iii) — `sms:minimal` (DERV-61-03) — checked AS STATED, all four data, via `rem:converse` CORRECTED form

**Statement to verify (VERBATIM, main.tex lines 351–353):**

> (iii) `$V_{BM}$` is the **minimal composite OUS carrying product states, product effects,
> non-signaling constraints, and product-form sequential product**.

**The clause (iii) object is the MINIMAL/standard composite**

$$ V_{BM} \;=\; M_3(\mathbb{C})^{sa} \otimes M_3(\mathbb{C})^{sa} \;\cong\; M_9(\mathbb{C})^{sa}, \qquad \dim_{\mathbb R} V_{BM} = 81 = 9\cdot 9 \quad (\text{61-02, Eq. 61.3}). $$

The four carried data are each checked for `n = 3`, **none dropped, none weakened** (mirroring
`rem-converse-bgw.md` §3 instantiated at `n = 3`):

**Datum 1 — product states.** `M_9(C)^sa = M_3(C)^sa ⊗ M_3(C)^sa` carries product states
`ρ_B ⊗ ρ_M` (the standard QM tensor product of density matrices on the body and model factors). ✓

**Datum 2 — product effects.** It carries product effects `a ⊗ b` with `a ∈ [0,I]_B`,
`b ∈ [0,I]_M` (BGW Proposition 4.5, p.24: *"Let `p ∈ A` and `q ∈ B` be projections. Then `p ⊗ q`
is a projection in `AB`"* — product effects are genuine effects of the composite). **CITE 61-02:**
`check_composite_dimension` confirms `kron(H1,H2)` of two `3×3` Hermitians is a `9×9` Hermitian
(`K = K†`, exact), i.e. product effects land in `M_9(C)^sa`. ✓

**Datum 3 — non-signaling constraints.** The standard complex-QM tensor product is the
non-signaling composite: testing the body and updating the model act on **separate** tensor factors,
so neither operation's outcome statistics on its own factor are affected by the choice of operation
on the other (BGW Definition 4.1 imposes this no-signaling condition; the standard composite
satisfies it). ✓

**Datum 4 — product-form sequential product (Phase 60 OPEN ITEM, now CLOSED).** The self-modeling
sequential product `a & b = √a · b · √a` (Lüders form, `def:product-sp`) acts in **product form**
across the body–model split on `M_9(C)^sa`:

$$ (a_B \otimes a_M) \,\&\, (b_B \otimes b_M) \;=\; \sqrt{a_B \otimes a_M}\,(b_B \otimes b_M)\sqrt{a_B \otimes a_M} \;=\; (a_B \,\&\, b_B)\otimes(a_M \,\&\, b_M) \qquad (\text{61-02, Eq. 61.4}). $$

**CITE 61-02 (the substantive closure):** `check_seqprod_factorization` / `test-sympy-seqprod-
factorize` prove this **EXACTLY** by computing `√a · b · √a` on the **full `9×9`** composite (via an
exact spectral matrix square root `matrix_sqrt_nxn`) and showing equality with the factored form
`(a_B & b_B) ⊗ (a_M & b_M)`, for two distinct product-effect pairs (off-diagonal real and complex
factors). The intermediate identity `√(a_B ⊗ a_M) = √a_B ⊗ √a_M` (PSD factors, Kronecker
mixed-product property) is verified, and S3 unitality `I_9 & a = a` holds. This is **derived by
direct matrix computation**, not merely asserted from the abstract Lüders form — closing the Phase
60 open item flagged in 60-02 (`rem-converse-bgw.md` §8: the factorization was previously
*asserted* from the Lüders form). ✓

**MINIMALITY (in full force).** `M_9(C)^sa` is **simple** (no nontrivial direct-sum decomposition;
same argument as clause (iv), applied to `M_9`), hence the **smallest** composite carrying exactly
this data — "the composite has no hidden structure" (main.tex lines 375–384). Now the
**CORRECTED `rem:converse`** (Phase 60, `rem-converse-bgw.md` §2–§3, BGW Thm 4.15 / Cor 4.16 /
Table 2):

- The **maximal/universal** composite `C_3 ⊠̃ C_3 = M_9(C)^sa ⊕ M_9(C)^sa` is **STRICTLY LARGER**
  (real-dim `162`; an **extra classical bit**) — **CITE 61-02:** `dim_minimal = 81 ≠ 162 =
  dim_maximal` (exact integer inequality).
- The minimal composite `M_9(C)^sa` is a **DIRECT SUMMAND** of the maximal one (BGW Theorem 4.15:
  `AB` is an ideal in `A ⊠̃ B`; Corollary 4.16: `AB` is a direct summand of `A ⊠̃ B`).
- Clause (iii)'s **minimality SELECTS the standard summand**: the maximal composite has a nontrivial
  direct-sum decomposition (the extra classical bit is exactly the "hidden structure" minimality
  forbids), so it is **not** the minimal composite; minimality picks out `M_9(C)^sa`.

**State plainly:** `minimal ≠ maximal` (`81 ≠ 162`). Clause (iii) holds **because minimality picks
the minimal composite `M_9(C)^sa`**, **NOT** because the two composites coincide.

**Clause (iii) holds for `M_3(C)^sa` — AS STATED, all four data verified for `n = 3`, minimality in
full force. ✓** (Via the corrected `rem:converse`; quantitative data from 61-02.)

> **`fp-redefine-iii` rejected:** none of the four data was dropped or relaxed; "minimal" is used in
> its full force — indeed it is the very lever that selects `M_9(C)^sa` over the extra-bit composite.
> **`fp-conflate-composites` rejected:** the clause (iii) object is the **minimal** composite
> (dim 81); the maximal (dim 162) is flagged as the extra-classical-bit contrast, never reported as
> "the composite"; and `V_BM` (the observer's body⊗model self-composite) is **not** identified with
> the BGW `⊠̃` universe-tensoring of `h_3(O)` (see §7).

---

## CLAUSE (iv) — `sms:simple` (DERV-61-02) — verified DIRECTLY

**Statement to verify:** `V = M_3(C)^sa` has no nontrivial direct-sum decomposition: there is no
splitting `V = V_1 ⊕ V_2` into nonzero order-unit subspaces.

`M_3(C)` is a simple algebra: its center is `Z(M_3(C)) = C·I_3` (scalars only), so its only central
idempotents are `0` and `I_3`. A nontrivial order-unit direct-sum decomposition `V = V_1 ⊕ V_2`
would require a nontrivial central idempotent `z` (`0 ≠ z ≠ I_3`, `z² = z`, central) splitting the
order unit `I_3 = z + (I_3 − z)`; none exists. Hence `M_3(C)^sa` is simple (61-02, Eq. 61.2):

$$ Z(M_3(\mathbb C)) = \{X : [X,g]=0 \ \forall g\} = \mathbb{C}\cdot I_3, \qquad z^2 = z \ \text{central} \Rightarrow z \in \{0, I_3\}. $$

**CITE 61-02 (VALD-61-01):** `check_simplicity` solves the commutant of the matrix-unit generating
set `{E_12,E_21,E_23,E_32,E_13,E_31}` in `M_3(C)` by exact `linsolve`, obtaining a single free scalar
parameter with **all off-diagonal entries identically zero** — i.e. center `= C·I_3`; and confirms
`λ² = λ ⇒ λ ∈ {0,1}`, so the only central idempotents are `0, I_3`. No nontrivial order-unit split.

**Clause (iv) holds for `M_3(C)^sa`. ✓** (Direct verification + 61-02 exact-symbolic evidence.)

> **Type/category check (clause iv):** simplicity is an intrinsic property of the FRJA/OUS
> `M_3(C)^sa`. Same-category. ✓

---

## 5. ASSEMBLY / VERDICT

**All four clauses of Paper 5 Definition 1 hold for `A = h_3(C_u) ≅ M_3(C)^sa` as a self-modeling
system IN ITS OWN RIGHT (intrinsically):**

| Clause | Label | Route | Result | 61-02 evidence |
|---|---|---|---|---|
| (i) | `sms:finite` | **direct** | finite-dim spectral OUS; **three** (`≥2`) orthogonal nontrivial projective units `E_11,E_22,E_33 → I_3` | rank 3, frame-independent |
| (ii) | `sms:faithful` | `rem:converse` | `V_B = V_M = M_3(C)^sa`, `φ = id` is an order isomorphism | (relational; identity map) |
| (iii) | `sms:minimal` | `rem:converse` **corrected** | minimal composite `M_9(C)^sa` (dim 81) carries all four data **AS STATED**; minimality selects it; `minimal ≠ maximal` (maximal `M_9⊕M_9` dim 162, extra classical bit) | dim 81 vs 162; product-form factorization on `M_9(C)^sa` |
| (iv) | `sms:simple` | **direct** | simple; center `= C·I_3`; no nontrivial central idempotent | center `= C·I_3` |

So Paper 5's theorem applies to the slice and certifies the observer's complex C\* structure **for
`A` taken intrinsically**. The intrinsic question of Phase 61 is therefore answered **positively**
(honestly — no clause required redefinition; no datum was dropped; the verdict is not forced). This
is exactly Step 2 of the four-step attack; the milestone verdict remains **UNDECIDED** pending
Phase 62 (§6) and Phase 63.

---

## 6. PHASE 62 DEFERRAL (mandatory) — the induced-by-`E` question is NOT claimed here

**Explicit deferral.** Whether the four-clause self-modeling structure on `A` is **coherently
INDUCED by the conditional expectation `E : h_3(O) → A`** (Effros–Störmer) from the **non-associative
ambient `h_3(O)`** is **Phase 62's question and is NOT claimed here.** The Phase 61 result is the
**intrinsic** statement only:

> **`A = M_3(C)^sa` is a standard self-modeler in its own right.** Whether `E` transports that
> structure coherently from `h_3(O)` — in particular whether `E`'s interaction with the **sequential
> product** `a & b = √a · b · √a` (not merely the Jordan product) is controlled, or whether
> non-associativity leaks in — is **UNPROVEN** (Phase 62, the load-bearing step; PAUSE condition 2 if
> an obstruction is found).

**The factorization checked in clause (iii) datum 4 is on the ASSOCIATIVE composite.** 61-02's
`√a · b · √a` factorization is computed entirely within the **associative** `M_9(C)^sa =
M_3(C)^sa ⊗ M_3(C)^sa` (61-02 grep-verifies no `octonion_algebra`/`h_3(O)` import; an explicit test
asserts the non-associative module is never loaded). The **non-associative `h_3(O)` computation —
`E`'s interaction with `&` on the actual Albert-algebra structure — is the Phase 62
NON-ASSOCIATIVITY guard and is kept strictly separate.** Carried context (not used as premises
here): GPD Phase 42 found `√(T_a) T_b √(T_a)` *exits* `M_16(R)` for anticommuting Cl(9,0) pairs, and
Phase 46 found intrinsic `h_2(O)` Jordan product closes in `V_0` with zero `V_{1/2}` leakage — both
bear on the Phase 62 embedding question and are flagged there, not invoked now.

**No-premise confirmation (guards `fp-automatic-without-check` and `assert-Peirce-preserves-iii`).**
No step in §0–§5 used `RESTRICTION`, the conditional expectation `E`, the Peirce decomposition w.r.t.
`E`, or "slice-induction" as a premise or a conclusion. Clauses (i)/(iv) are intrinsic facts of
`M_3(C)^sa`; clauses (ii)/(iii) come from the self-model `(V_B=V_M=M_3(C)^sa, φ=id, V_BM=M_9(C)^sa)`
and the corrected `rem:converse`. The induced-by-`E` claim is neither asserted nor pre-empted.

### 6.1 (intentionally part of §6) — relation to PAUSE conditions

Phase 61's positive intrinsic verdict does **not** discharge PAUSE condition 2 (embedding needs
structure not induced by `E`). That condition lives entirely in Phase 62 and remains open. No PAUSE
is triggered by this plan.

### 6.2 `rem:converse` provenance (carried)

`rem:converse` is **prompt-inline authoritative** (`~/scratch/get-physics-done/`
`p5-basin-restriction-prompt.md`), **NOT** a labeled remark in the live `complexification.tex`
(Phase 60 grep: 0 matches; `lem:bottleneck` at line 409). It is used here as a **principle confirmed
against BGW in Phase 60**, never as published provenance. FUTR-01 will insert the **corrected**
remark (direct-summand form, no "coincide") after `lem:bottleneck`. (`fp-converse-already-in-paper`
rejected.)

---

## 7. STALE-TEXT FLAG (mandatory) — "minimal = maximal per BGW" is STALE; corrected form used

> ╔══════════════════════════════════════════════════════════════════════════════════╗
> ║ **STALE-TEXT FLAG.** The phrase **"minimal = maximal per BGW"** (and equivalents     ║
> ║ such as "the minimal and maximal composites coincide for `M_n(C)^sa`") still         ║
> ║ literally appears in several project artifacts that were written **BEFORE** Phase 60 ║
> ║ grounded `rem:converse` against BGW — and is therefore **STALE / WRONG**:            ║
> ║                                                                                      ║
> ║   • ROADMAP Phase 61 **Success Criterion 3** (SC3)                                    ║
> ║   • REQUIREMENTS **DERV-61-03**                                                       ║
> ║   • the project-contract **`deliv-slice-clause-iii.must_contain`** entry              ║
> ║   • **`ref-bgw.why_it_matters`** (in the 61-01 plan contract / project metadata)      ║
> ║   • the **`user_asserted_anchors`**                                                   ║
> ║                                                                                      ║
> ║ **CORRECTED FACT (Phase 60, `rem-converse-bgw.md`; 60-02-SUMMARY.md):** for           ║
> ║ `A = B = C_n = M_n(C)^sa`,                                                            ║
> ║     • the **minimal/standard** composite is `M_{n^2}(C)^sa` (one copy; real-dim `n^4`;║
> ║       `n=3` ⇒ 81) — the clause (iii) object;                                          ║
> ║     • the **maximal/universal** composite is `C_n ⊠̃ C_n = M_{n^2}(C)^sa ⊕            ║
> ║       M_{n^2}(C)^sa` (two copies; real-dim `2 n^4`; `n=3` ⇒ 162) — an **extra         ║
> ║       classical bit**, BGW Table 2 / Thm 4.15 / Cor 4.16;                             ║
> ║     • **`minimal ≠ maximal`**; the minimal composite is a **direct summand** of the   ║
> ║       maximal one, and clause (iii)'s **minimality selects** the minimal summand.     ║
> ║                                                                                      ║
> ║ **This deliverable uses the CORRECTED direct-summand form throughout** and does       ║
> ║ NOT reproduce the stale "coincide" wording as an assertion about the slice's          ║
> ║ composite structure (it appears here only inside this flag, as the text being         ║
> ║ corrected). Source of truth: `derivations/p5-basin-restriction/rem-converse-bgw.md`   ║
> ║ and `.gpd/phases/.../60-02-SUMMARY.md`. 61-02's exact `dim 81 vs 162` check is the    ║
> ║ quantitative witness of this correction.                                             ║
> ║                                                                                      ║
> ║ **Bidirectional guard.** This flag also prevents the *opposite* error: a downstream   ║
> ║ reader or verifier must **NOT** "correct" the corrected (direct-summand) form back     ║
> ║ to the stale "coincide" wording on the basis of the stale ROADMAP/contract text.      ║
> ╚══════════════════════════════════════════════════════════════════════════════════╝

---

## 8. Type-/structural-consistency self-audit (mirror of `rem-converse-bgw.md` §6)

Every load-bearing object, tagged by category (the pure-algebra dimensional-analysis analog):

| Load-bearing object / claim | Subject category | Type-correct? |
|---|---|---|
| `A = M_3(C)^sa` special, simple FRJA = BGW `C_3` (`= h_3(C_u)`) | FRJA (simple) | ✓ |
| minimal composite `V_BM = M_9(C)^sa` (clause iii object) | FRJA (simple) carrying OUS structure | ✓ |
| maximal composite `M_9(C)^sa ⊕ M_9(C)^sa` (universal) | FRJA (NOT simple) | ✓ |
| **"minimal vs maximal" comparison** | FRJA-composite ↔ FRJA-composite (**same category**) | ✓ (answer: **NOT equal**, `81 ≠ 162`) |
| clause (i)/(iv) on `V = M_3(C)^sa` | OUS intrinsic | ✓ |
| clause (ii): `φ = id : V_B → V_M` | order isomorphism (OUS ↔ OUS) | ✓ |
| clause (iii): four data carried by minimal `V_BM` | OUS composite | ✓ (four data verbatim, minimality intact) |
| `dim(V_BM) = dim(V_B)·dim(V_M)` for minimal (`81 = 9·9`) | OUS dimension bookkeeping | ✓ |
| maximal fails product-dimension (`162 ≠ 81`) ⇒ extra bit | OUS bookkeeping | ✓ |
| **`V_BM` ≠ BGW `⊠̃` on `h_3(O)`** | OUS self-composite vs bifunctor on whole algebra | ✓ (never equated) |
| `E : h_3(O) → A` | conditional expectation | ✓ (forward reference only; **not used** §0–§5) |

- **Clause (iii) integrity:** four data (product states, product effects, non-signaling,
  product-form sequential product) + minimality, present and verbatim. **Not weakened.** ✓
- **No cross-category equation:** `V_BM` (OUS) is never set equal to a BGW-monoidal property of
  `h_3(O)`; "minimal vs maximal" is a same-category (FRJA-composite) comparison with answer
  NOT-equal. ✓
- **Composite identity:** the clause (iii) object is the **minimal** composite `M_9(C)^sa` (dim 81),
  never the maximal (dim 162). ✓ (`fp-conflate-composites` rejected.)
- **Provenance:** `rem:converse` flagged prompt-inline / not-in-paper; corrected direct-summand form
  used; BGW cited via the Phase 60 grounding. ✓ (`fp-converse-already-in-paper` rejected.)
- **Honest verdict:** all 61-02 checks passed; no clause required redefinition; the positive verdict
  is earned, not forced. ✓ (`fp-force-positive` rejected — the backtracking branch was wired but not
  taken.)

---

## 9. Citations

- **`ref-paper5-def1`** — `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex`,
  `def:self-modeling-system` (line 342); clauses (i) `sms:finite` (346–348), (ii) `sms:faithful`
  (349–350, verbatim *"`φ: V_B → V_M` is an order isomorphism (faithful tracking)"*), (iii)
  `sms:minimal` (351–353, verbatim, four data), (iv) `sms:simple` (354–356); unpacking of
  `sms:minimal` (375–384). **Re-read this plan.**
- **`ref-lem-bottleneck`** — `~/repos/blog/landing/papers/sm-from-self-modeling/sections/`
  `complexification.tex`, `lem:bottleneck` (line 409): the slice `A ≅ M_3(C)^sa` (`n=3`, single
  `F_4`-orbit). `rem:converse` is prompt-inline, **not** labeled here (FUTR-01 insertion point).
- **`ref-bgw`** — Barnum–Graydon–Wilce, *Quantum* **4**, 359 (2020); arXiv:1606.09331v3. Decisive
  for the corrected `rem:converse`: **Theorem 4.15** (p.29, `AB` ideal in `A ⊠̃ B`), **Corollary
  4.16 + discussion** (p.29, for `A=B=C_n`: `A ⊠̃ B = M_{n^2}(C)_sa ⊕ M_{n^2}(C)_sa`, usual QM
  composite `M_{n^2}(C)_sa` a separate direct summand), **Table 2** (p.21), **Table 1(a)** (p.19),
  **Proposition 4.5** (p.24, product effects). Grounded in Phase 60 (`rem-converse-bgw.md`; BGW PDF
  read directly there).
- **VALD-61-01 (61-02 evidence)** — `code/slice_clause_iii_verification.py`,
  `tests/test_slice_clause_iii.py`; `.gpd/phases/61-slice-satisfies-clause-iii/61-02-SUMMARY.md`.
  Exact-symbolic: rank 3 / three orthogonal projective units → `I_3`; simplicity (center `= C·I_3`);
  composite real-dim `81` vs maximal `162 ≠ 81`; product-form sequential-product factorization on
  `M_9(C)^sa`. **Re-run this plan: ALL CHECKS PASS, exit 0.**
- **Phase 60 grounding** — `derivations/p5-basin-restriction/rem-converse-bgw.md` (CONFIRMED-WITH-
  CAVEAT; corrected direct-summand form; provenance flag), `two-composites.md` (categories ledger;
  two-composites distinction), `claim.md` (RESTRICTION, allowed inputs, prohibited moves, PAUSE
  conditions).

---

## 10. Confidence

**[CONFIDENCE: HIGH]** — all four clauses verified for `A = M_3(C)^sa` as a self-modeler in its own
right; `rem:converse` instantiated in the corrected direct-summand form; clause (iii) checked AS
STATED with minimality in full force; induced-by-`E` explicitly deferred to Phase 62.

Independent checks supporting HIGH (the pure-algebra analog of "≥3 independent verifications"):
1. **Direct algebra:** clauses (i) [Jordan rank 3] and (iv) [simplicity, center `= C·I_3`] are
   standard, textbook facts of `M_3(C)^sa`, derived here from first principles.
2. **Exact-symbolic oracle (Level-5 external CAS):** 61-02's SymPy harness reproduces rank 3 (in two
   frames), simplicity, `dim 81 ≠ 162`, and the product-form factorization on `M_9(C)^sa`
   **exactly** (no float tolerance) — re-run this plan, exit 0. This breaks the self-consistency
   loop.
3. **Literature benchmark:** the corrected `rem:converse` (minimal a direct summand of maximal;
   `minimal ≠ maximal`) is grounded against BGW Thm 4.15 / Cor 4.16 / Table 2 (Phase 60, BGW PDF
   read directly), and 61-02's `81 vs 162` exact integer inequality is the quantitative witness.

**Residual uncertainty (kept OUT of the Phase 61 claim, flagged for Phase 62):** the **induced-by-`E`
coherence** from the non-associative `h_3(O)` is entirely unproven; the sequential-product
factorization verified here is on the **associative** composite only. If Phase 62 finds that `E`
fails to transport `&` coherently (non-associativity leaks in), the *intrinsic* Phase 61 result
stands but the **RESTRICTION through-line** does not — a precisely-characterized obstruction, which
is an acceptable milestone outcome (PAUSE condition 2). This residual is a property of Phase 62, not
a weakness of the Phase 61 intrinsic verification.

---

_Plan: 61-01 — DERV-61-01/02/03, citing VALD-61-01_
_Milestone: v15.0 The P5 ↔ Basin Restriction Lemma — Step 2 of 4_
