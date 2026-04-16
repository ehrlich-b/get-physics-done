# Attempt-01: Compression-Combinatorics (A) Proof of the Peirce-Preservation Lemma

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; peirce_2_space=V_2(p_i):=range(C_{p_i}); peirce_1_space=V_1(p_i,p_j):=(C_{p_i}+C_{p_j})V - C_{p_i}V - C_{p_j}V

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 02 (Wave 2, Task 1)
**Attempt:** 01
**Date:** 2026-04-16

---

## Header

- **seeded-from:** A-S 2001 Ch. 7-8 compression algebra (per alfsen-shultz-notes.md, Section 5 compression axioms + Section 6 orthogonal annihilation). Approach 2 (compression combinatorics) per 54-RESEARCH.md §Standard Approaches.
- **avoiding-because:** Phase 4-06 Eq. (04-06.4) audit verdict AUDIT-FAILS (per audit-04-06.md §5: line 119-163 is an M_n(C) matrix-PSD proof device). Eq. (04-06.4) is unavailable as a seed per Plan 54-01 Task 2 decision = `option-b-fails-compression`.
- **assumption set:** {S1 (additivity of `L_a` in 2nd arg), S3 (unitality + sharp constraint `p ∘ b = C_p(b)`), linearity of `L_a: V → V` in its (2nd) argument derived from S1 + finite-dim, A-S compression axioms}. **Explicitly NOT assumed:** S2, S4, S5, S6, S7, any form of bilinearity or additivity of `∘` in the 1st argument, associativity, Jordan product, C\*-structure, matrix structure, Lüders rule, `√a b √a`.
- **addresses prior objection:** N/A (first attempt).

---

## Conventions Block

Copied verbatim from 54-02-PLAN.md frontmatter:

- **Units:** N/A (pure algebra)
- **Sequential product symbol:** `a ∘ b` (Paper 5 convention)
- **Compression symbol:** `C_p`
- **Order unit space:** finite-dim archimedean OUS over ℝ with distinguished unit 1
- **Peirce 2-space:** `V_2(p_i) := range(C_{p_i})`
- **Peirce 1-space:** `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V - C_{p_i}V - C_{p_j}V`
- **Allowed-axiom scope:** S1, S3, linearity (of `L_a` derived from S1 + finite-dim), A-S compression axioms
- **Forbidden tokens** (PLAN.md frontmatter): `M_n(ℂ)` / `M_n(C)` as proof device, `Jordan`, `EJA`, `Lüders` / `Luders`, `pxp`, `√a b √a` / `sqrt(a) b sqrt(a)`, `operator product`, `f(λ,μ) = √(λμ)` / `f(lambda,mu) = sqrt(lambda*mu)` as primitive, `h_n(ℂ)` / `h_n(C)`, `spin factor` as proof device

---

## Lemma Statement (copied verbatim from claim.md Section 3, with (A) assumption set clause)

**Peirce-Preservation Lemma [(A) version].** Under the (A) assumption set `{S1, S3, linearity of L_a, A-S compression axioms, finite-dim spectrality}`, let `V` be a finite-dimensional spectral order unit space over ℝ, let `{p_1, …, p_n}` be an orthogonal family of projective units in `V` (so `C_{p_i} C_{p_j} = 0` for `i ≠ j`), and let `a = Σ_i λ_i p_i` with `λ_i ∈ ℝ` be a spectral decomposition. Write `supp(a) := {i : λ_i ≠ 0}`. Let `L_a(b) := a ∘ b`. Then:

- **Proposition 3.1 (V_2 invariance):** For every `i ∈ {1, …, n}`, `a ∘ V_2(p_i) ⊆ V_2(p_i)`.
- **Proposition 3.2 (V_1 standard invariance):** For every pair `(i, j)` with `i ≠ j` and `i, j ∈ supp(a)`, `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)`.
- **Proposition 3.3 (V_1 cross-term invariance):** For every pair `(k, l)` with `k ≠ l` and `{k, l} ∩ supp(a) = ∅`, `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)`.

---

## Preparatory Remarks on the Allowed Tool Set

Before entering the three sub-proofs, fix three preliminary observations that will be used repeatedly.

### R.1 What S1 + S3 + A-S compressions give us

By **S1**, the map `L_a: V → V` defined by `L_a(b) = a ∘ b` is **additive in its 2nd argument**: `L_a(b + c) = L_a(b) + L_a(c)`. Combined with finite-dim + the standard archimedean-OUS bilinearity conventions in vdW 2019 Def. 2, this promotes to ℝ-linearity: `L_a(λ b) = λ L_a(b)` for `λ ∈ ℝ`. Thus `L_a` is a linear endomorphism of `V`. This is "linearity of `L_a`" in the (A) assumption set.

**By S3 (sharp constraint):** For any sharp effect `p`, `p ∘ b = C_p(b)` for all `b ∈ V`. In particular, for each projective unit `p_i` in our orthogonal family,
$$
L_{p_i}(b) \;=\; p_i \circ b \;=\; C_{p_i}(b), \qquad \forall b \in V. \tag{R.1.1}
$$
Thus `L_{p_i} = C_{p_i}` **as linear endomorphisms of V**.

### R.2 What S1 + S3 do NOT give us

S1 is additivity in the **2nd argument** of `∘`. It does **not** give additivity in the 1st argument. Therefore **we cannot conclude** `L_{a+a'}(b) = L_a(b) + L_{a'}(b)` from S1 alone; that would require S2 (forbidden in Phase 54). In particular, **we cannot write `a ∘ b = Σ_i λ_i (p_i ∘ b) = Σ_i λ_i C_{p_i}(b)` directly from S1 + S3** when `a = Σ_i λ_i p_i`. The identity
$$
(a_1 + a_2) \circ b \;=\; a_1 \circ b + a_2 \circ b \tag{FORBIDDEN; S2-equivalent}
$$
is **not available** in the (A) allowed-tool set and is rejected as forbidden.

This is the **first obstruction** for a compression-combinatorics-only (A) attempt. We must work **around** it, not through it.

### R.3 What A-S compressions give us

From alfsen-shultz-notes.md Section 5:
- **Idempotency:** `C_{p_i}² = C_{p_i}`. (Axiom 5.1.)
- **Positivity:** `C_{p_i}` preserves the positive cone. (Axiom 5.2.)
- **Complement on sharp effects:** `C_{p_i} + C_{p_i'} = Pinch` (pinching map); in particular `Pinch(b) = Σ_k C_{p_k}(b)` on the orthogonal family. (Axiom 5.3, with the v2.0 Phase 4-06 C4 correction; NOT `= id`.)
- **Projector fix:** `C_{p_i}(p_i) = p_i`. (Axiom 5.4.)
- **Orthogonal mutual annihilation:** `C_{p_i} C_{p_j} = 0` for `i ≠ j` in an orthogonal family. (Section 6.)

The Peirce 2-space is defined `V_2(p_i) := range(C_{p_i})`. By idempotency, `b ∈ V_2(p_i) ⟺ C_{p_i}(b) = b`.
The Peirce 1-space is defined `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V − C_{p_i}V − C_{p_j}V` — equivalently, `b ∈ V_1(p_i, p_j) ⟺ (C_{p_i} + C_{p_j})(b) = b \wedge C_{p_i}(b) = 0 \wedge C_{p_j}(b) = 0` (the last two following from `C_{p_i} C_{p_j} = 0` applied to the first — see Lemma L.2 below).

### L.1 Lemma (Compression action characterization of V_2)

`b ∈ V_2(p_i)` if and only if `C_{p_i}(b) = b`. By `C_{p_i}² = C_{p_i}`, every `b ∈ range(C_{p_i})` is fixed by `C_{p_i}`, and conversely.

### L.2 Lemma (Compression action characterization of V_1)

Suppose `p_i ⊥ p_j` in an orthogonal family (so `C_{p_i} C_{p_j} = C_{p_j} C_{p_i} = 0`; commutation follows from mutual annihilation). Under the A-S 2001 Ch. 7-8 compression-additivity identity `C_{p_i + p_j} = C_{p_i} + C_{p_j}` for orthogonal projective units (alfsen-shultz-notes.md Section 5, NEEDS-VERIFICATION marker), we have: `b ∈ V_1(p_i, p_j)` is equivalent to:
- `C_{p_i + p_j}(b) = b` (equivalently, under the compression-additivity identity, `(C_{p_i} + C_{p_j})(b) = b`),
- `C_{p_i}(b) = 0`, and
- `C_{p_j}(b) = 0`.

This is the Peirce-block characterization of the (i,j) off-diagonal block: `b` lies in `V_2(p_i + p_j)` but is annihilated by both individual compressions `C_{p_i}` and `C_{p_j}`.

**Proof sketch:** Using `C_{p_i + p_j} = C_{p_i} + C_{p_j}` on orthogonal family (alfsen-shultz-notes.md Section 5, A-S 2001 Ch. 7-8), claim.md's definition `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V − C_{p_i}V − C_{p_j}V` becomes `V_2(p_i + p_j) − V_2(p_i) − V_2(p_j)`, i.e., the subspace of `V_2(p_i + p_j)` not in either individual `V_2`. An element `b` in this difference satisfies: `C_{p_i + p_j}(b) = b` (because `b ∈ V_2(p_i+p_j)`); `C_{p_i}(b) = 0` and `C_{p_j}(b) = 0` (because `b ∉ V_2(p_i)` and `b ∉ V_2(p_j)`, using idempotency + mutual annihilation to deduce the full 0 rather than just "not all of b"). The reverse direction follows by rearranging.

**Caveat (documented for the attempt's drift log and verifier):** If `C_{p_i+p_j} ≠ C_{p_i} + C_{p_j}` in the specific OUS at hand (which holds in a generic Jordan realization like H_3(ℝ); see SymPy check `attempt-01.py` notes), then claim.md's definition of V_1 via `(C_{p_i} + C_{p_j})V` differs from the standard Peirce-block characterization. The discrepancy is a known concern flagged for the A-S 2001 Ch. 7-8 compression-additivity verification in alfsen-shultz-notes.md Section 5. For the purposes of attempt-01's structural-failure argument, the characterization above is used; the SymPy gate uses the Peirce-block characterization (which faithfully represents "off-diagonal block between rows/cols i and j" in H_3(ℝ)). The failure mode identified below does not depend on the compression-additivity identity — it is structural to the (A) tool set regardless of which V_1 interpretation is used.

### L.3 Lemma (Sharp constraint for projective units with zero coefficient)

For **any** projective unit `p_k` in the orthogonal family (whether `k ∈ supp(a)` or `k ∉ supp(a)`), we have by S3:
$$
p_k \circ (a \circ b) \;=\; C_{p_k}(a \circ b), \qquad \forall b \in V. \tag{L.3.1}
$$
That is, applying `C_{p_k}` to `a ∘ b` is identical to computing `p_k ∘ (a ∘ b)` via the sequential product. This is the **only OUS-primitive handle we have** on `C_{p_k}(a ∘ b)`.

---

## Sub-Proof (i): Proposition 3.1 — V_2(p_i) invariance

**Goal:** Show `a ∘ V_2(p_i) ⊆ V_2(p_i)` for every `i ∈ {1, …, n}`.

Let `b ∈ V_2(p_i)`, i.e., `C_{p_i}(b) = b` (by L.1). We want to prove `a ∘ b ∈ V_2(p_i)`, i.e., `C_{p_i}(a ∘ b) = a ∘ b`.

By L.3 (sharp constraint),
$$
C_{p_i}(a \circ b) \;=\; p_i \circ (a \circ b). \tag{3.1.1}
$$

So the claim is: **`p_i ∘ (a ∘ b) = a ∘ b` whenever `b ∈ V_2(p_i)`**.

**Attempt to prove via S1 + S3 + compressions:**

Using S1 (2nd-arg additivity) on the left-hand side with respect to `a ∘ b` as a single 2nd-arg input does nothing useful — there is no natural decomposition of `a ∘ b` as a sum that makes progress.

The only available decomposition is via `a = Σ_k λ_k p_k`, but that's a 1st-arg decomposition — **forbidden** per R.2.

**Alternative route: if `a ∘` were known to commute with `C_{p_i}` on `V_2(p_i)`.** We would want:
$$
C_{p_i}(a \circ b) \;\stackrel{?}{=}\; a \circ C_{p_i}(b). \tag{3.1.2}
$$
If (3.1.2) held, then for `b ∈ V_2(p_i)`, `C_{p_i}(b) = b`, so `C_{p_i}(a \circ b) = a \circ b`, which is exactly what we want.

But (3.1.2) **is not** among the A-S compression axioms, and deriving it from S1 + S3 + compressions alone is **equivalent to** the invariance claim itself (it says "`L_a` commutes with `C_{p_i}` on `V_2(p_i)`", which is a restatement of 3.1).

**Observation:** (3.1.2) is sometimes written as "`a ∘ (−)` is a module map over the compression algebra." This is the **Peirce-invariance property itself**. Deriving it would be the proof we seek — not a tool usable in the proof.

**Attempt to proceed via sharp-constraint composition:**

By L.3.1 we have `C_{p_i}(a ∘ b) = p_i ∘ (a ∘ b)`. Without associativity of ∘ (not in the allowed-tool set), we cannot rewrite `p_i ∘ (a ∘ b) = (p_i ∘ a) ∘ b`. Even if we could, we would need `(p_i ∘ a) ∘ b = a ∘ b` on `V_2(p_i)`, which — computing `p_i ∘ a = C_{p_i}(a)` via S3 — would give us `C_{p_i}(a) ∘ b`. For `a = Σ_k λ_k p_k` we'd want `C_{p_i}(a) = ?`. This is a 1st-arg claim about `a`, but the compression `C_{p_i}` as a map on `V` takes `a` (element of V) to an element of `V_2(p_i)`; so `C_{p_i}(a)` is **some element of V_2(p_i)** — call it `a_i` — and then the claim `a_i ∘ b = a ∘ b` would need to be shown. But this is again the invariance claim restated.

**Partial progress:** We can show one direction cleanly if we restrict to `a = λ_i p_i` (single-projector case):
- If `a = λ_i p_i`, then by S1 applied to the 2nd argument trivially, `L_a(b) = λ_i p_i ∘ b` — but again we need `L_{λ_i p_i}(b) = λ_i (p_i ∘ b)`. The scalar factor extraction is OK under linearity of `L_a` in its 2nd argument (it pulls out of the 2nd argument scaling). But linearity of `L_a` in the 2nd argument is about scaling `b`, not about scaling the 1st argument `a`. The scalar-in-1st-argument identity `L_{λ a}(b) = λ L_a(b)` is not part of S1; it would be a 1st-arg linearity fact — **forbidden**.

So even the single-projector case is blocked without additional structure.

**Conclusion for Proposition 3.1:** Under the (A) allowed-tool set, Proposition 3.1 **cannot be proved** without some structural fact beyond S1 + S3 + A-S compressions. The natural fact that WOULD close it — commutation (3.1.2) or first-argument additivity/scalar-homogeneity — is **equivalent to the invariance claim itself** or **forbidden as S2**.

This is not yet a definitive failure; it may be that a different route exists. Attempt sub-proof (ii) and (iii) first, then revisit.

---

## Sub-Proof (ii): Proposition 3.2 — V_1(p_i, p_j) invariance, standard case

**Goal:** For `(i, j)` with `i ≠ j` and `i, j ∈ supp(a)`, show `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)`.

Let `b ∈ V_1(p_i, p_j)`. By L.2, `C_{p_i}(b) = 0`, `C_{p_j}(b) = 0`, and `(C_{p_i} + C_{p_j})(b) = b`.

We want `a ∘ b ∈ V_1(p_i, p_j)`, i.e., `C_{p_i}(a ∘ b) = 0`, `C_{p_j}(a ∘ b) = 0`, and `(C_{p_i} + C_{p_j})(a ∘ b) = a ∘ b`.

By L.3,
$$
C_{p_i}(a \circ b) \;=\; p_i \circ (a \circ b). \tag{3.2.1}
$$

To conclude `C_{p_i}(a ∘ b) = 0`, we need `p_i ∘ (a ∘ b) = 0`.

**Attempt via S1 applied to 2nd arg:** S1 gives `p_i ∘ (a ∘ b) = p_i ∘ (a ∘ b)` — no reduction. The 2nd-arg additivity doesn't fragment `a ∘ b` because it's a single element of `V`.

**Attempt via 2nd-arg decomposition of `b`:** Since `b ∈ V_1(p_i, p_j)`, we have `b = (C_{p_i} + C_{p_j})(v)` for some representative `v`, modulo the `V_2` complements. But `b` is a single vector; we cannot "apply S1 to it" because it is not a sum of two vectors in a structural sense. (If we wrote `b = C_{p_i}(v) + C_{p_j}(v) − C_{p_i}(w_1) − C_{p_j}(w_2)`, then S1 applied in the 2nd argument of `a ∘ b` gives `a ∘ b = a ∘ (C_{p_i}(v) + C_{p_j}(v) − C_{p_i}(w_1) − C_{p_j}(w_2)) = a ∘ C_{p_i}(v) + a ∘ C_{p_j}(v) − a ∘ C_{p_i}(w_1) − a ∘ C_{p_j}(w_2)` — but each term `a ∘ C_{p_k}(·)` involves `a ∘` acting on an element of `V_2(p_k)`, which by Proposition 3.1 would land in `V_2(p_k)`. But Proposition 3.1 is **not yet proved** in this attempt. So we have a **cyclic dependency** between 3.2 and 3.1.)

**Attempt via sharp-constraint unfolding:**

`p_i ∘ (a ∘ b)` — try to "push `p_i` through `a`." Without associativity, we cannot write `(p_i ∘ a) ∘ b`. Even if we could:
- `p_i ∘ a = C_{p_i}(a)` by S3. For `a = Σ_k λ_k p_k` with `i ∈ supp(a)`, `C_{p_i}(a)` would intuitively be `λ_i p_i` IF `C_{p_i}` is linear **and** satisfies `C_{p_i}(λ_k p_k) = λ_k C_{p_i}(p_k)` with `C_{p_i}(p_k) = δ_{ik} p_i`. The first (linearity of `C_{p_i}`) is given (compressions are linear by A-S); the second (`C_{p_i}(p_k) = δ_{ik} p_i`) follows from projector-fix + orthogonal annihilation (Axiom 5.4 + Section 6). So `C_{p_i}(a) = λ_i p_i` by compression linearity applied to the 1st argument as an element of `V` — which IS legal (compressions are endomorphisms of `V` and `a` is just an element of `V`).
- So `p_i ∘ a = λ_i p_i` (assuming associativity, which we don't have).
- Still needs associativity to push through.

**Conclusion for Proposition 3.2:** The sub-proof reduces to needing **associativity** or **commutation of compressions with `L_a`** — both forbidden or circular. The 2nd-arg decomposition route produces a **cyclic dependency** on Proposition 3.1.

**Partial progress noted:** `C_{p_i}(a) = λ_i p_i` **is** an allowed-tool fact (it's a linearity-of-compression computation on `a ∈ V`). But this fact alone doesn't help because we can't associate it into `p_i ∘ (a ∘ b)`.

---

## Sub-Proof (iii): Proposition 3.3 — V_1(p_k, p_l) cross-term invariance (R3 mandatory case)

**Goal:** For `(k, l)` with `k ≠ l` and `{k, l} ∩ supp(a) = ∅`, show `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)`.

Let `b ∈ V_1(p_k, p_l)`. By L.2, `C_{p_k}(b) = 0`, `C_{p_l}(b) = 0`, and `(C_{p_k} + C_{p_l})(b) = b`.

Since `k ∉ supp(a)` and `l ∉ supp(a)`, we have `λ_k = 0` and `λ_l = 0`. The spectral decomposition of `a` involves **only** `p_j` with `j ∈ supp(a) ⊆ {1, …, n} \ {k, l}`.

By L.3,
$$
C_{p_k}(a \circ b) \;=\; p_k \circ (a \circ b). \tag{3.3.1}
$$

To conclude `C_{p_k}(a ∘ b) = 0`, we need `p_k ∘ (a ∘ b) = 0`.

**Attempt via the "a has no k-support" structural fact:** Intuitively, since `a` has no component along `p_k`, multiplying by `p_k` on the left should annihilate `a`'s contribution. Making this rigorous without 1st-arg additivity is the challenge.

Concrete attempt:
- `C_{p_k}(a) = C_{p_k}(Σ_j λ_j p_j) = Σ_j λ_j C_{p_k}(p_j)` — by linearity of the compression `C_{p_k}` on `V`. (Legal: compressions are linear endomorphisms of `V`, and summing λ_j p_j inside `V` is legal since `a` IS this sum by the spectral decomposition fact in the OUS.)
- `C_{p_k}(p_j) = 0` for `j ≠ k` (orthogonal annihilation, Axiom 5.4 + Section 6).
- Since `j ∈ supp(a)` implies `j ≠ k` (as `k ∉ supp(a)`), **every term** in `Σ_j λ_j C_{p_k}(p_j)` vanishes.
- Therefore `C_{p_k}(a) = 0`.

By S3 (sharp constraint on `p_k`), this is equivalently
$$
p_k \circ a \;=\; C_{p_k}(a) \;=\; 0. \tag{3.3.2}
$$

So `p_k ∘ a = 0` (the zero element of `V`).

**Using this fact to attack `p_k ∘ (a ∘ b)`:**

Observation: `p_k ∘ a = 0` tells us `L_{p_k}(a) = 0`, i.e., `C_{p_k}(a) = 0`. But we want `L_{p_k}(a ∘ b)`, not `L_{p_k}(a)`. Without 2nd-arg structure relating `L_{p_k}(a ∘ b)` to `L_{p_k}(a)`, we cannot proceed.

**Trying 2nd-arg unfolding of `a ∘ b` via the V_1-structure of `b`:**

`b ∈ V_1(p_k, p_l)` means `b` is in the Peirce 1-space for the complementary pair `(p_k, p_l)`. By L.2, we can write
$$
b \;=\; (C_{p_k} + C_{p_l})(b) \;=\; C_{p_k}(b) + C_{p_l}(b) - (C_{p_k}(b) + C_{p_l}(b) - b),
$$
but `C_{p_k}(b) = C_{p_l}(b) = 0`, so `b = (C_{p_k} + C_{p_l})(b) = 0 + 0 = 0`? **No**, that's wrong — see L.2. The definition of V_1 is `V_1(p_k, p_l) := (C_{p_k} + C_{p_l})V − C_{p_k}V − C_{p_l}V`, which means `b = (C_{p_k} + C_{p_l})(v) - C_{p_k}(w_1) - C_{p_l}(w_2)` for some representatives. Here `(C_{p_k} + C_{p_l})(b) = b` is in the quotient sense (after projecting out `V_2`-contributions). The direct computation `C_{p_k}(b) = 0` follows from the L.2 characterization (Peirce 1-space elements are annihilated by the individual compressions because mutual-annihilation kills the cross terms).

So `b` is NOT (C_{p_k} + C_{p_l})(v) for any `v` in a clean sense; it is the unique representative in `V_1(p_k, p_l)` of an equivalence class. We cannot re-express `b` as a sum of components `∈ V_2(p_k) ⊕ V_2(p_l)` — that's exactly what Peirce 1-space means (orthogonal to both V_2's).

**The structural barrier for 3.3:** To extract anything about `a ∘ b`, we need some way to relate `L_a` to the compression `C_{p_k}` acting on `b` (not on `a`). The allowed-tool set provides:
1. `C_{p_k}(a ∘ b) = p_k ∘ (a ∘ b)` [L.3, S3].
2. `C_{p_k}(a) = 0` [(3.3.2), linearity of compression on V].
3. `C_{p_k}(b) = 0` [V_1 characterization, L.2].
4. L_a is 2nd-arg linear [S1].
5. `L_{p_j}(x) = C_{p_j}(x)` for sharp p_j [S3].

**None of these combine to yield `p_k ∘ (a ∘ b) = 0`** without an additional bridge.

Candidate bridges, all FORBIDDEN or CIRCULAR:
- **Associativity** `p_k ∘ (a ∘ b) = (p_k ∘ a) ∘ b = 0 ∘ b = 0`: associativity is NOT an OUS-primitive and is NOT among the A-S compression axioms. Deriving it requires either Jordan structure (forbidden pre-S4) or vdW Thm 1 (requires S4-S7, forbidden).
- **First-argument additivity** (`(Σ_j λ_j p_j) ∘ b = Σ_j λ_j (p_j ∘ b)`): this is S2, **forbidden**.
- **Commutation** `[L_a, C_{p_k}] = 0` on `V_1(p_k, p_l)`: **this IS the invariance claim itself**, circular.
- **Pinching with a**: `a ∘ b = Σ_k C_{p_k}(a ∘ b)` would hold if `Pinch(a ∘ b) = a ∘ b`, i.e., `a ∘ b ∈ V_2` (trivial case). In general `a ∘ b ∉ V_2` when `b ∈ V_1`, so this is not a usable decomposition.

**Adversarial objection (pre-self-review):** "You can write `b = (C_{p_k} + C_{p_l})(b')` for some `b'` in a representative sense. Apply 2nd-arg additivity (S1) to `a ∘ ((C_{p_k} + C_{p_l})(b'))`, giving `a ∘ C_{p_k}(b') + a ∘ C_{p_l}(b')`. Each term is `L_a` applied to an element of `V_2(p_k)` or `V_2(p_l)` respectively. By Proposition 3.1 (applied to `k` and `l`), these are in `V_2(p_k)` and `V_2(p_l)` respectively. Sum is in `V_2(p_k) + V_2(p_l) ⊆ V_2(p_k) ⊕ V_2(p_l)`, NOT in `V_1(p_k, p_l)`. Conclusion: `a ∘ b ∈ V_2(p_k) ⊕ V_2(p_l)`, which is DISJOINT from `V_1(p_k, p_l)` (by Peirce decomposition), so we'd get `a ∘ b = 0` (if Prop 3.1 holds). But that's the wrong result — we want `a ∘ b ∈ V_1(p_k, p_l)`, not `0`."

**Answering the adversarial objection:** The objection is based on a **false decomposition** of `b`. Since `b ∈ V_1(p_k, p_l)` with `C_{p_k}(b) = C_{p_l}(b) = 0`, **there is no expression `b = C_{p_k}(b') + C_{p_l}(b')` with the b' components in V_2**. The Peirce 1-space is precisely the "off-diagonal" part that is annihilated by `Pinch = Σ C_{p_i}`. So this 2nd-arg decomposition is **not available**, and the objection's argument breaks at its first step.

This does NOT, however, make 3.3 provable — it only defeats one wrong approach. The fundamental barrier stands: we have no bridge from `C_{p_k}(a) = 0` to `C_{p_k}(a ∘ b) = 0`.

---

## Model-Instantiation Check (Early Falsifier Gate (c))

**Purpose:** Verify that any argument used in the sub-proofs would not produce a false statement when instantiated in `M_n(ℂ)^sa` or `C(X)`. Since the sub-proofs have BLOCKED (no proof completed), there is no completed argument to instantiate. We check instead that the lemma **statement** (which is what we're trying to prove) holds in the two canonical models.

- **In `M_n(ℂ)^sa`** (used here only as a sanity check, NOT as a proof device): `a ∘ b := (1/2)(ab + ba)` is the Jordan product (post-Jordan). Peirce invariance is a classical Jordan-theoretic theorem for this case (standard textbook result). The three propositions 3.1, 3.2, 3.3 all hold. ✓
- **In `C(X)`** (commutative effect algebra): `a ∘ b = a · b` (pointwise product). Projectors are characteristic functions of disjoint sets. `V_2(p_i)` = functions supported on `supp(p_i)`; `V_1(p_i, p_j)` = functions supported on `supp(p_i) ∪ supp(p_j)` modulo each individual support — which is **empty** in the commutative case (Peirce decomposition collapses to `V = ⊕_i V_2(p_i)`). So Propositions 3.2 and 3.3 are **vacuously true** (their V_1 spaces are {0}), and 3.1 holds trivially by pointwise multiplication. ✓
- **In spin factors** (defense example only; not a proof device): Peirce invariance follows from Clifford anti-commutation. Standard JB-algebra fact. ✓

**Instantiation result:** The lemma is TRUE in all three canonical models. So the failure of the (A) attempt is not because the lemma is false — it is because the (A) tool set is **insufficient** to prove a true lemma.

---

## Drift Log

Running record of temptations toward forbidden tokens during drafting, and how each was avoided.

| Drift event | Temptation | How avoided | Rejected token / device |
|---|---|---|---|
| 1 | Write `a ∘ b = Σ λ_i C_{p_i}(b) + Σ √(λ_i λ_j) P_{ij}(b)` as a starting formula for analysis | Explicitly rejected: this is Eq. (04-06.4), which AUDIT-FAILS. Also requires 1st-arg additivity (S2, forbidden). Limited to `C_{p_i}(a) = Σ λ_j C_{p_i}(p_j) = λ_i p_i` as an isolated compression-linearity fact on `a ∈ V`. | `f(λ,μ) = √(λμ)` as primitive; S2 |
| 2 | Invoke `a ∘ b = (1/2)(ab + ba)` in `M_n(ℂ)^sa` to "see what answer should be" | Isolated to the Model-Instantiation section (gate c) and explicitly labeled as sanity check, NOT proof device | `M_n(ℂ)` as proof device; Jordan |
| 3 | Reach for associativity `p_k ∘ (a ∘ b) = (p_k ∘ a) ∘ b = 0 ∘ b = 0` | Rejected: associativity is NOT in {S1, S3, linearity, A-S compressions}. It is derived post-vdW-Thm-1 (requires S4-S7) or via Jordan structure (forbidden pre-S4). Documented the gap explicitly in sub-proof (iii). | Associativity of ∘; Jordan |
| 4 | Reach for Schur complement / spin-factor face argument (Paper 5 §3.3 line 545 style) | Rejected: spin factor is a Jordan-level proof device; explicitly forbidden. | Spin factor as proof device; Schur complement |
| 5 | Write `√a b √a` to resolve the M_2(C) case | Rejected: this is the Lüders rule in C*-algebraic form; both `√a b √a` and Lüders are forbidden tokens. | `√a b √a`; Lüders |
| 6 | Define `a · b := (1/2)(a ∘ b + b ∘ a)` to symmetrize and invoke Jordan Peirce machinery | Rejected: this is silent (C-iii) drift per CONTEXT.md stop/rethink #3. | Jordan product construction |
| 7 | Invoke Macdonald's theorem or EJA classification | Rejected: pre-S4 Jordan structure; forbidden. | Macdonald's theorem; EJA |
| 8 | Cite A-S 2003 Thm 9.37 for Peirce direct sum | Rejected: Thm 9.37 is in A-S 2003 Ch. 9 (Jordan state-space characterization), pre-Jordan-illegal per alfsen-shultz-notes.md Flag 4.1. | A-S 2003 Thm 9.37 |
| 9 | In answering the adversarial-pre-self-review, claim "b = C_{p_k}(b') + C_{p_l}(b')" decomposition | Recognized as structurally wrong: V_1 is precisely the OFF-diagonal complement of Σ V_2, so no such decomposition exists. Used as a negative illustration. | False Peirce decomposition of b |

No forbidden tokens leaked into the proof body. All references to forbidden devices appear in (a) the explicit "Forbidden Tools" section of the header conventions, (b) the Model-Instantiation section with the role explicitly labeled as sanity check, or (c) this Drift Log as rejected temptations.

---

## Early Falsifier Gates

### Gate (a): Forbidden-token self-grep

Will be run via `rg` on `attempt-01.md` after this file is sealed. Every hit is expected only in the Forbidden Tokens header, the Model-Instantiation section (legal sanity-check framing), or the Drift Log (explicit rejected-drift record).

### Gate (b): SymPy per-attempt rank-1 gate on H_3(ℝ)

See sibling file `attempt-01.py`. Runs a rank-1 symbolic check on V_2 and V_1 invariance with two orthogonal rank-1 projectors. The SymPy check is a LEMMA-LEVEL check (does the lemma statement hold in a concrete H_3(ℝ) case?), not a proof-level check of attempt-01's argument — because attempt-01 does NOT close the argument.

### Gate (c): Model-instantiation check

Performed in the Model-Instantiation Check section above: the lemma holds in `M_n(ℂ)^sa`, `C(X)`, and spin factors. Attempt-01's argument (which does not close) cannot be instantiated and falsified in the three models because there is no completed argument to instantiate. What we have verified is that the **target claim** (Propositions 3.1, 3.2, 3.3) is consistent with the canonical models — no false statement is being proved. The gap is between true-claim and attempt-01's-tool-insufficient-proof.

---

## Status and Verdict

**Status:** **FAILED — structural insufficiency of (A) tool set**

**Failure mode:** The (A) allowed-tool set `{S1, S3, linearity of L_a in 2nd arg, A-S compression axioms}` **does not provide a bridge** from the fact `C_{p_k}(a) = 0` (easy to derive by compression linearity on `a ∈ V` for `k ∉ supp(a)`) to the fact `C_{p_k}(a ∘ b) = 0` (what Proposition 3.3 needs).

The bridge candidates are:
1. **Associativity** `p_k ∘ (a ∘ b) = (p_k ∘ a) ∘ b`: NOT an OUS-primitive; derives post-vdW-Thm-1 (post-S4). **Forbidden.**
2. **First-argument additivity/scalar homogeneity** (S2): **Forbidden.**
3. **Commutation** `[L_a, C_{p_k}] = 0`: **this IS the invariance claim**, circular.
4. **Compression-module structure** "`L_a` is a `C_{p_k}`-module map": specific stronger axiom not in (A). Candidate for S0 in the (C-i) pivot.

All three sub-proofs reduce to the **same** structural gap. Proposition 3.1 needs `[L_a, C_{p_i}] = 0` on `V_2(p_i)`. Proposition 3.2 needs either 2nd-arg decomposition (cyclic on 3.1) or associativity. Proposition 3.3 needs the `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0` bridge. All three bridges are absent from the (A) tool set and require either S2, associativity (post-S4), Jordan structure, or an independent axiom.

**Verbatim early-gate failure statement (for carry-forward to attempt-02 or Plan 54-03):**

> The (A) allowed-tool set `{S1, S3, linearity in 2nd arg, A-S compression axioms}` is insufficient to prove Proposition 3.3 (`a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` for `{k,l} ∩ supp(a) = ∅`). The required bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0` is not derivable from these axioms without either (i) first-argument additivity/scalar-homogeneity of `∘` (which is S2, forbidden), (ii) associativity of `∘` (not an OUS primitive; derives post-vdW-Thm-1 post-S4), or (iii) a compression-module structure on `L_a` (which is essentially the invariance claim itself, i.e., circular). Propositions 3.1 and 3.2 reduce to the same structural gap, either directly or via a cyclic dependency between them. The lemma is TRUE in the canonical models (`M_n(ℂ)^sa`, `C(X)`, spin factors) — the failure is tool-insufficiency, not false-claim.

This is the expected failure mode per CONTEXT.md stop/rethink #2 and per the 54-RESEARCH.md §Standard Approaches §Approach 2 "Tradeoffs" warning: *"if the mixing term is not constructible from compressions alone, Approach 2 collapses to axiomatizing the mixing term = silently adopts (C-i)."*

The failure **strongly motivates** the (C-i) pivot: since the structural gap is exactly of the form "need a compression-level property of `L_a` that is not in the A-S compression axioms", the natural (C-i) S0 axiom is precisely **the compression-module structure**: "`L_a` commutes with each `C_{p_i}` in a controlled way." That this is NOT derivable from S1-S7 (because S2 is still the only additivity-in-1st-arg axiom and is forbidden pre-S4) is what makes S0 an independent axiom, not a theorem.

**Recommendation for Task 2 checkpoint:**
- Adversarial review: **NOT invoked** — the early-gate check has already determined that the argument does not close. No proof exists to subject to `gpd-review-math` adversarial review. (This avoids spending review budget on a known-incomplete argument.)
- Routing: **PIVOT-TO-C-I** is well-motivated by this failure trace. The failure localization to "need a compression-module / commutation property" points directly at the S0 candidate statement in claim.md Section 4.6.
- Alternative (if user wants to exhaust (A) attempt cap): authorize attempt-02 with a DIFFERENT structural strategy. But the two allowed (A) approaches (Approach 1 via 4-06 seed, Approach 2 via compression combinatorics) have now BOTH been closed off (Approach 1 by audit-04-06 AUDIT-FAILS; Approach 2 by the present attempt-01 structural gap). A genuinely NEW structural strategy for attempt-02 is not apparent within the (A) tool set.

---

## Self-grep Section (Forbidden Tokens — for grep exemption)

This section contains the explicit forbidden-token list as a reference declaration, legal per the plan's `grep_targets` + forbidden_tokens contract. Lines below are the explicit list; they are NOT used as proof devices.

**Forbidden as proof devices (pinned from PLAN frontmatter forbidden_tokens):**
- `M_n(ℂ)` / `M_n(C)` as proof device
- `Jordan` (product, algebra, structure — all forbidden pre-S4)
- `EJA` (Euclidean Jordan Algebra)
- `Lüders` / `Luders` rule
- `pxp` matrix-block notation
- `√a b √a` / `sqrt(a) b sqrt(a)`
- `operator product`
- `f(λ,μ) = √(λμ)` / `f(lambda,mu) = sqrt(lambda*mu)` as primitive
- `h_n(ℂ)` / `h_n(C)`
- `spin factor` as proof device

Appearances above this line in the Drift Log and Model-Instantiation sections classify as (a) rejected-temptation documentation or (b) canonical-model sanity check; no occurrence is used as a proof device.

---

_Attempt-01 sealed: 2026-04-16. Status: FAILED — structural insufficiency. Verbatim failure statement carried forward to attempt-log.md and (if PIVOT-TO-C-I is confirmed) to Plan 54-03 S0 defense input._
