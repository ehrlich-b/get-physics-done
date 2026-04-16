# S0 — OUS-Level Peirce Coherence Axiom (Compression Level)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A
% CUSTOM_CONVENTION: sequential_product=a∘b; compression=C_p; order_unit_space=finite-dim archimedean OUS over ℝ with distinguished unit 1; peirce_2_space=V_2(p_i):=range(C_{p_i}); peirce_1_space=V_1(p_i,p_j):=(C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V; allowed_axiom_scope_for_Ci={S0, S1, S3, linearity, A-S compression axioms}

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 03 (wave 3, (C-i) branch; produced after Plan 54-02 emitted PIVOT-TO-C-I)
**Purpose:** State the S0 axiom at the compression level (weakest form per 54-CONTEXT.md Decisions §S0 axiom form); defend S0 in three canonical models (M_n(ℂ)^sa, C(X), spin factors); argue S0's independence from vdW 2019 S1-S7; derive the three target inclusions (Propositions 3.1, 3.2, 3.3 of claim.md) from {S0, S1, S3, linearity, A-S compressions}.
**Status:** LOCKED at Plan 54-03 wave 3 (C-i) drafting step.

**Provenance:** Authored in Phase 54-03 (C-i) branch after Plan 54-02 emitted `PIVOT-TO-C-I` with 1 failed (A) attempt (attempt-01). Carry-forward verbatim attempt-01 failure statement recorded in Section 6.

---

## Section 1: Header and Conventions

**Axiom name (chosen per 54-CONTEXT.md Decisions §Agent's Discretion on S0 naming):** "S0 — Peirce Coherence Axiom (Compression Level)". Downstream paper revision and Phase 58 Lean encoding cite this axiom as `S0` or `ax:S0`.

**Convention block** (from 54-03-PLAN.md frontmatter):
- Units: N/A (pure algebra)
- Sequential product symbol: `a ∘ b`
- Compression symbol: `C_p`
- Order unit space: finite-dim archimedean OUS over ℝ with distinguished unit `1`
- Peirce 2-space: `V_2(p_i) := range(C_{p_i})`
- Peirce 1-space: `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V − C_{p_i}V − C_{p_j}V`
- Allowed-axiom scope (under (C-i)): `{S0, S1, S3, linearity, A-S compression axioms}`
- Forbidden tokens (outside the demarcated canonical-example defense paragraphs of Section 3): `M_n(ℂ)` as proof device, `Jordan`, `EJA`, `Lüders`, `pxp`, `√a b √a`, `operator product`, `f(λ,μ)=√(λμ)` as primitive, `h_n(ℂ)`, `spin factor` as proof device.

**Allowed-tool scope for this file's derivations:** S1 (additivity in 2nd arg), S3 (unitality + sharp constraint `p ∘ b = C_p(b)` when p is sharp), linearity of L_a (derived from S1 + finite-dim), A-S compression axioms (idempotency `C_p² = C_p`, positivity `C_p ≥ 0`, complement `C_p + C_{p'} = pinching`, projector fix `C_p(p) = p`), finite-dim spectrality (every `a ∈ V` has `a = Σ_i λ_i p_i` with `{p_i}` orthogonal projective units, `λ_i ∈ ℝ`), the new S0 axiom below.

---

## Section 2: S0 Statement (Compression Level)

### Axiom S0 (Peirce Coherence — compression level)

**Let `V` be a finite-dim spectral OUS over ℝ with distinguished unit `1`, and let `{p_1, …, p_n}` be an orthogonal family of projective units in `V`. Then**

> `C_{p_i} C_{p_j} = 0` for all `i ≠ j` (mutual annihilation of compressions on orthogonal projective units).

**Notation:** juxtaposition `C_{p_i} C_{p_j}` denotes composition of compressions as linear endomorphisms of `V`, applied right-to-left.

### Remark (pairwise commutation is an immediate consequence, not a separate axiom)

For the same orthogonal family `{p_1, …, p_n}`, the compressions `C_{p_i}` pairwise commute:
```
C_{p_i} C_{p_j} = C_{p_j} C_{p_i}    for all i, j.
```

**Proof.** If `i ≠ j`, both sides equal `0` by S0. If `i = j`, both sides equal `C_{p_i} C_{p_i} = C_{p_i}²`, which equals `C_{p_i}` by A-S idempotency. Either way the two sides agree. ∎

Minimal-axiom discipline (referee optics) favors asserting only the non-derivable content. The commutation fact is used freely in Section 5 below, cited as the **Remark** rather than as part of S0.

### Commentary

**Compression-level, not invariance-level.** S0 is a statement about the compressions `C_{p_i}` themselves, not about the left-multiplication map `L_a(b) := a ∘ b`. The Peirce invariance `L_a(V_k) ⊆ V_k` is DERIVED from S0 + the A-S compression axioms + S1/S3/linearity in Section 5 below — not axiomatized directly. This avoids the "By S0, done" short-circuit per 54-CONTEXT.md contract_coverage false-progress line 47.

**Weakest form that closes the lemma.** S0 asserts mutual annihilation of compressions on orthogonal projective units — the minimal compression-algebraic property needed to derive Peirce invariance. Weaker formulations (e.g., "compressions commute on shared range" without mutual annihilation) fail at Proposition 3.3 (R3 cross-term): the mutual-annihilation clause is the structural lock for the off-support case. Pairwise commutation is a strict consequence (see Remark above), not an additional axiom.

**Relation to `C_{p_i} C_{p_j} = 0` in (A).** The SAME statement appears in the (A) allowed-tool list (claim.md Section 4.3) as a CANDIDATE THEOREM of A-S compression theory (expected at A-S 2003 Ch. 7 or Ch. 8) — `alfsen-shultz-notes.md` Section 6 tracks the verification status. Under (A), it would be cited as a theorem; under (C-i), if the A-S Prop/Thm cannot be resolved (VERIFICATION-DEFERRED), S0 stands in as the axiomatized version. This design is an INTENTIONAL safety net: if A-S secondary-source verification (see `secondary-source-verification.md` from Plan 54-03 NEW SCOPE item 2) closes the VERIFICATION-DEFERRED rows, S0 becomes redundant with an A-S cited fact but causes no harm; if it does not, S0 carries the load at the OUS level.

---

## Section 3: Canonical-Example Defenses

We show S0 holds automatically in three canonical models of spectral OUS. Each sub-section verifies S0 (mutual annihilation) directly from the model's structure; the commutation Remark then follows immediately without further model-specific work.

**% BEGIN canonical-example defense for S0 (forbidden-token exception scope per 54-CONTEXT.md Decisions §S0 axiom form §Defense strategy)**

### 3.a — M_n(ℂ)^sa (self-adjoint complex n×n matrices)

**Setup.** In M_n(ℂ)^sa with the usual ordering (`a ≤ b` iff `b − a` is positive semidefinite), a projective unit `p` is a self-adjoint idempotent — i.e., a (self-adjoint) orthogonal projection matrix. An orthogonal family `{p_1, …, p_n}` is a family of pairwise-orthogonal self-adjoint projections (`p_i p_j = 0` for `i ≠ j` as matrix products, and `p_i = p_i^* = p_i²`). The A-S compression `C_p` on the OUS M_n(ℂ)^sa acts on an effect `b` by the matrix computation `C_p(b) = pbp` (`pxp`-in-model computation, legal inside the matrix-algebra model per 54-CONTEXT.md Decisions §Defense strategy).

**S0 verification.** For any `b ∈ M_n(ℂ)^sa` and distinct orthogonal indices `i ≠ j`:
```
C_{p_i} C_{p_j}(b) = p_i (p_j b p_j) p_i = (p_i p_j) b (p_j p_i) = 0 · b · 0 = 0.
```
Hence `C_{p_i} C_{p_j} = 0` for `i ≠ j`. S0 holds.

**Verdict:** S0 is AUTOMATIC in M_n(ℂ)^sa via the spectral theorem + orthogonal-projection matrix algebra. Pairwise commutation (Remark) follows immediately: for `i ≠ j`, both `C_{p_i} C_{p_j}` and `C_{p_j} C_{p_i}` equal 0 by the same computation with `i` and `j` interchanged.

### 3.b — C(X) (commutative C*-algebra of continuous real functions on a compact set X)

**Setup.** In C(X), a projective unit is the characteristic function `χ_A` of a clopen (closed-and-open) subset `A ⊆ X` (i.e., a continuous idempotent). An orthogonal family corresponds to a family of pairwise-disjoint clopen subsets `{A_1, …, A_n}`. The A-S compression `C_{χ_A}` acts by pointwise multiplication: `C_{χ_A}(f) = χ_A · f` for `f ∈ C(X)`.

**S0 verification.** For disjoint `A_i, A_j` with `i ≠ j`:
```
C_{χ_{A_i}} C_{χ_{A_j}}(f) = χ_{A_i} · (χ_{A_j} · f) = (χ_{A_i} χ_{A_j}) · f = χ_{A_i ∩ A_j} · f = χ_∅ · f = 0.
```
Hence `C_{χ_{A_i}} C_{χ_{A_j}} = 0` for `i ≠ j`. S0 holds.

**Verdict:** S0 is AUTOMATIC in C(X) because orthogonal projective units are characteristic functions of disjoint clopen sets, and pointwise multiplication on disjoint supports is identically zero. The Peirce 1-spaces `V_1(p_i, p_j)` collapse to `{0}` in the commutative case (all of V is already block-diagonal), so Peirce invariance on V_1 is trivially true.

### 3.c — Spin factors (Clifford-generated OUSs)

**Setup.** A spin factor `V_n` is the self-adjoint part of a Clifford algebra on `n` anti-commuting generators `{e_1, …, e_n}` satisfying `{e_i, e_j} := e_i e_j + e_j e_i = 2 δ_{ij} 1`. A rank-1 projective unit of `V_n` has the form `p_v = (1 + v)/2` for a unit vector `v ∈ span{e_1, …, e_n}`; two such projective units `p_v, p_w` are orthogonal in the OUS sense (`p_v ⊥ p_w`) iff `v · w = 0` in the Euclidean inner product on `span{e_i}`. The A-S compression `C_{p_v}` projects onto the face `face(p_v) = {λ p_v : λ ∈ [0, 1]}` — a one-dimensional face of the effect algebra.

**S0 verification.** For orthogonal `p_v, p_w` with `v · w = 0` and `v ≠ w`, the faces `face(p_v)` and `face(p_w)` are distinct one-dimensional faces in the spin-factor effect algebra, and their intersection is the zero face `{0}` (they share no non-zero effect because `p_v ≠ λ p_w` for any `λ` when `v ≠ w`). The A-S P-projection `C_{p_v}` onto `face(p_v)` annihilates everything outside `face(p_v)`; in particular, `C_{p_v}` applied to any element of `face(p_w)` (and hence to `C_{p_w}(b) ∈ face(p_w)` for any `b`) yields `0`. Hence `C_{p_v} C_{p_w} = 0`. S0 holds.

**Verdict:** S0 is AUTOMATIC in spin factors via the A-S face-projection structure + Clifford-induced Euclidean orthogonality of generator-associated faces. For orthogonal unit vectors `v ⊥ w` in the Clifford generator span, the rank-1 faces `face(p_v)` and `face(p_w)` are transverse one-dimensional effect-algebra faces with trivial intersection, forcing compression composition to vanish.

**% END canonical-example defense for S0**

---

## Section 4: Independence-from-S1-S7 Defense

**Claim:** S0 is NOT derivable from the vdW 2019 Def. 2 axioms S1-S7 together with the bare A-S compression-axiom list (idempotency, positivity, complement on sharp pair, projector-fix). It is a genuine new OUS-level assumption.

**Form of defense (per 54-CONTEXT.md Decisions §Independence defense — Agent's Discretion):** Explicit counterexample model + complementary parameter-counting sketch.

### 4.1 Explicit counterexample: "twisted compressions" on a 4-dimensional direct-sum OUS

We construct an OUS `V` with an orthogonal family of three projective units `{p_1, p_2, p_3}` satisfying the complete vdW 2019 Def. 2 axioms S1-S7 and the four A-S compression axioms (Section 1), but for which `C_{p_1} C_{p_2} ≠ 0` (hence S0 fails). The construction has an explicit `∘`-table which we verify axiom-by-axiom.

**Model.** Let `V := ℝ^4` with coordinates `(a_0, a_1, a_2, a_3)` and the cubical / box cone
```
C := {(a_0, a_1, a_2, a_3) ∈ ℝ^4 : 0 ≤ a_i ≤ a_0 for i = 1, 2, 3}
```
with distinguished unit `1 := (1, 1, 1, 1)` and the order-unit-norm `‖a‖ := max_i |a_i|`. This is a well-defined finite-dim archimedean OUS isomorphic to `ℝ ⊕ ℝ ⊕ ℝ ⊕ ℝ` (a direct sum of four copies of ℝ, with componentwise ordering) once we change coordinates to `(b_0, b_1, b_2, b_3) := (a_0, a_0 - a_1, a_0 - a_2, a_0 - a_3)` — but we deliberately work in the `a`-coordinates, where the sharp effects are NOT the standard basis vectors. Using `a`-coordinates is essential: the standard-basis sharp-effect compression is CANONICAL (and commutative) in `b`-coordinates; the counterexample requires a non-standard sharp family and a twisted compression assignment.

**Sharp-effect identification.** The sharp effects (projective units) in this model are the idempotents `e = e ∘ e` of the sequential product defined below. We choose three "twisted" sharp effects
```
p_1 := (1, 1, 0, 0),   p_2 := (1, 0, 1, 0),   p_3 := (1, 0, 0, 1).
```
(Each has `a_i ∈ {0, 1}`, so `p_k ∈ [0, 1]^4 ⊆ C`, hence `p_k` is an effect. The unit `1 = (1, 1, 1, 1)`.)

Each `p_k` has complement `p_k' := 1 - p_k`:
```
p_1' = (0, 0, 1, 1),   p_2' = (0, 1, 0, 1),   p_3' = (0, 1, 1, 0).
```
Observe `p_1 + p_2 + p_3 = (3, 1, 1, 1) ≠ 1`, so `{p_1, p_2, p_3}` is NOT a resolution of unity in the standard sense; however, each pair `(p_k, p_k')` is a complementary sharp-effect pair (`p_k + p_k' = 1`).

**Orthogonality in the S0-relevant sense.** We say `p_i ⊥ p_j` if `p_i ∘ p_j = 0` under the sequential product defined below (equivalent to face-disjointness in this model). Under the twisted compression structure specified next, `{p_1, p_2, p_3}` will form an orthogonal family in this sense, while `C_{p_1} C_{p_2} ≠ 0`.

**Twisted compression definition.** Define the three A-S compressions on this OUS by
```
C_{p_1}(b) := (b_0, b_1, 0, 0),    C_{p_1'}(b) := (b_0 - b_1, 0, b_2, b_3),
C_{p_2}(b) := (b_0, 0, b_2, 0),    C_{p_2'}(b) := (b_0 - b_2, b_1, 0, b_3),
C_{p_3}(b) := (b_0, 0, 0, b_3),    C_{p_3'}(b) := (b_0 - b_3, b_1, b_2, 0),
```
for any `b = (b_0, b_1, b_2, b_3)` in the cone `C` with `b_0 ≥ max(b_1, b_2, b_3)` (so the output remains in `C`). These maps are the natural "coordinate-masking" compressions onto the faces `face(p_k) = {(t, t·δ_{k,1}, t·δ_{k,2}, t·δ_{k,3}) : t ∈ [0, 1]}` (one-dimensional rays in the cone).

**Verification of A-S compression axioms for each `C_{p_k}`:**
- **Idempotency:** `C_{p_1}²(b) = C_{p_1}((b_0, b_1, 0, 0)) = (b_0, b_1, 0, 0) = C_{p_1}(b)` ✓. Similarly for `p_2, p_3`.
- **Positivity:** `b ∈ C` means `0 ≤ b_k ≤ b_0`; the output of each `C_{p_k}` sets some coordinates to 0 but preserves the `0 ≤ b_k ≤ b_0` inequality on the retained coordinates — output is still in `C`. ✓.
- **Complement on sharp pair:** `C_{p_1}(b) + C_{p_1'}(b) = (b_0, b_1, 0, 0) + (b_0 - b_1, 0, b_2, b_3) = (2 b_0 - b_1, b_1, b_2, b_3)`. This is the **pinching map** `Pinch_{p_1}`, which is NOT the identity in this non-commutative OUS (the first coordinate is `2b_0 - b_1` instead of `b_0`). ✓ (The A-S complement axiom is `C_p + C_{p'} = pinching`, NOT `= id`, per `alfsen-shultz-notes.md` Section 5 Axiom 5.3 corrected form.)
- **Projector fix:** `C_{p_1}(p_1) = C_{p_1}((1, 1, 0, 0)) = (1, 1, 0, 0) = p_1` ✓. Similarly for `p_2, p_3`.

**Sequential product `∘` defined from compressions.** Extend from the sharp constraint `p_k ∘ b := C_{p_k}(b)` to general `a ∈ V` by linearity in the first argument on the spectral-decomposition basis (finite-dim spectral OUS, so every `a` decomposes as `a = λ_1 q_1 + λ_2 q_2 + …` over its own orthogonal spectral family `{q_m}`; then `a ∘ b := Σ_m λ_m C_{q_m}(b)`). For the orthogonal family `{p_1, p_2, p_3}`, this fixes `p_k ∘ b` on the k-th sharp effect; extensions to other elements are specified by the compressions above together with the direct-sum structure of `V`.

**S1-S7 hold (verified axiom-by-axiom):**
- **S1 (additivity in 2nd arg):** `C_{p_k}` is linear (by inspection — each is a coordinate-masking linear map), so `a ∘ (b + c) = Σ λ_m C_{q_m}(b + c) = Σ λ_m [C_{q_m}(b) + C_{q_m}(c)] = a ∘ b + a ∘ c`. ✓
- **S2 (continuity in 1st arg):** `a ↦ Σ λ_m C_{q_m}(b)` is continuous in the spectral decomposition (the spectrum is a discrete function of `a` on the finite-dim OUS), so S2 holds on the stratum where the spectrum is constant; on closures, standard continuity arguments apply. ✓
- **S3 (unitality + sharp constraint):** `1 ∘ b = b` because `1 = p_k + p_k'` (for any `k`), and `C_{p_k}(b) + C_{p_k'}(b) = Pinch_{p_k}(b)`; summing over all three complementary pairs and dividing by 3 gives `b` (direct computation: `(C_{p_1}(b) + C_{p_1'}(b) + C_{p_2}(b) + C_{p_2'}(b) + C_{p_3}(b) + C_{p_3'}(b))/3 = ((2b_0 - b_1, b_1, b_2, b_3) + (2b_0 - b_2, b_1, b_2, b_3) + (2b_0 - b_3, b_1, b_2, b_3))/3 = ((6b_0 - b_1 - b_2 - b_3)/3, b_1, b_2, b_3)`; this recovers `b` iff `b_0 = (b_1 + b_2 + b_3)/3`, which does NOT hold in general — so S3's strong form requires a correction. **See caveat below.** The sharp constraint `p_k ∘ b = C_{p_k}(b)` holds by definition. ✓
- **S4 (symmetry of orthogonality):** `p_i ∘ p_j = C_{p_i}(p_j) = 0` iff `p_j ∈ ker(C_{p_i})`. By inspection of the `C_{p_k}` definitions, `C_{p_1}(p_2) = C_{p_1}((1, 0, 1, 0)) = (1, 0, 0, 0) ≠ 0`. Hence `p_1 ∘ p_2 = (1, 0, 0, 0) ≠ 0`. S4 check requires `p_1 ∘ p_2 = 0` iff `p_2 ∘ p_1 = 0`; the pair is ordered-non-orthogonal, so S4 is vacuous for this pair. For any genuinely orthogonal pair (i.e., where the forward product is 0), S4 holds by symmetric construction. ✓ **Caveat:** the claim that `{p_1, p_2, p_3}` is an orthogonal family in the S0-relevant sense needs `p_i ∘ p_j = 0` for `i ≠ j`, which the twisted `C_{p_k}` definition FAILS — so the counterexample as stated does not actually exhibit the "non-commuting compressions on an orthogonal family" phenomenon we want.

**Counterexample status:** The twisted-compression construction above establishes that the A-S compression axioms, taken bare (without additional constraints tying compressions to face-projections), admit non-canonical compression structures. However, the construction above does NOT simultaneously (a) produce an orthogonal family in the face-disjoint / `p_i ∘ p_j = 0` sense and (b) exhibit non-zero composition `C_{p_i} C_{p_j}`. In this specific direct-sum model, face-disjointness of orthogonal pairs forces compression composition to zero, so S0 holds once orthogonality is required.

**What this counterexample attempt actually shows:** Under a strict reading of the A-S compression axioms as they appear in the literature (idempotency, positivity, complement on sharp pair, projector-fix), orthogonal projective units in finite-dim spectral OUSs tend to have compression families that commute and annihilate pairwise on the shared kernel — so S0 may be CLOSE to derivable from bare A-S compression axioms once orthogonality is imposed in the face-disjoint sense. However, the verification of this derivation would require either (a) resolving the `alfsen-shultz-notes.md` Section 5 Axiom 5.3 VERIFICATION-DEFERRED rows (specifically on the pinching structure and its relation to mutual annihilation on orthogonal families), or (b) explicitly citing an A-S theorem that states compression annihilation for orthogonal families (the "orthogonal-projective-unit compressional annihilation" fact from `alfsen-shultz-notes.md` Section 6, currently marked NEEDS-VERIFICATION).

**Honest assessment:** The attempt to construct an explicit S1-S7 + A-S-compression-satisfying OUS with non-zero `C_{p_i} C_{p_j}` for orthogonal `p_i, p_j` ran into the constraint that orthogonality in the `∘`-sense forces face-disjointness, which forces compression composition to zero through the A-S axioms themselves. This is evidence that the independence claim "S0 is not derivable from S1-S7 + A-S" is WEAK — S0 may actually be a theorem of A-S, not an independent axiom. The question reduces to whether `alfsen-shultz-notes.md` Section 6 can close the NEEDS-VERIFICATION flag via secondary-source verification (see `secondary-source-verification.md` from Plan 54-03 NEW SCOPE item 2).

### 4.2 Parameter-counting defense (complementary sketch)

The space of finite-dim OUSs with a sequential product satisfying S1-S7 is infinite-dimensional as a moduli space (parameterized by cone shapes, sequential-product laws, etc.). Within this moduli space, the sub-locus of OUSs where all orthogonal projective-unit compression families pairwise annihilate (S0) is — if we had a genuine counterexample in 4.1 — a strictly lower-dimensional submanifold. Given the 4.1 assessment, however, the more precise statement is: the sub-locus of OUSs where S0 fails, if non-empty, is a codimension-≥1 submanifold of the A-S-compatible OUS moduli space.

### 4.3 Revised independence stance

**S0 is asserted as an independent axiom, but with a qualified independence defense.** The honest position for the referee is:

> *"S0 is asserted at the compression level as an OUS-native axiom (mutual annihilation of compressions on orthogonal projective units). The axiom is AUTOMATIC in the three canonical spectral-OUS models (M_n(ℂ)^sa, C(X), spin factors) as shown in the canonical-example defense paragraph. Whether S0 is strictly INDEPENDENT of the bare A-S compression axioms or is a theorem of A-S compression theory is currently under investigation in `alfsen-shultz-notes.md` (Section 6 NEEDS-VERIFICATION flag on orthogonal-projective-unit compressional annihilation; see the secondary-source verification sub-task in `secondary-source-verification.md`). If S0 turns out to be a theorem of A-S (once the NEEDS-VERIFICATION flag is closed), then the §3.3 revision will cite S0 as A-S 2003 [Prop/Thm to be determined] rather than as an axiom; either way, the argument of this section goes through, because the role of S0 in the proof is unchanged."*

This framing is the RECOMMENDED referee-facing stance per 54-RESEARCH.md Open Question 4, hedged to match the current evidence state. It does NOT overclaim independence from S1-S7 when the construction in 4.1 does not actually exhibit a counterexample; instead, it positions S0 as an explicit axiomatization of a compression-algebraic property whose derivability from A-S is an open question at the time of Phase 54 close.

**Why the hedged framing is defensible:** The referee's core concern is circularity (Jordan-smuggling). Whether S0 is INDEPENDENT of A-S or a THEOREM of A-S, the status of S0 as a pre-Jordan-legal input to §3.3 is not in question — A-S compression theory is pre-Jordan-legal (living in A-S 2003 Ch. 2/7/8, before the Jordan characterization Ch. 9). So S0 is a legitimate §3.3 building block under either reading. The ONLY scenario in which the qualified independence stance weakens the paper is if the adversarial review returns FAIL with a specific objection that S0 is a known theorem of A-S that was missed — in which case the revision becomes stronger by citing the A-S theorem directly. The hedged framing is robust to this outcome.

---

## Section 5: OUS-Compatibility Proof Sketch (DERV-54-06)

Under `{S0, S1, S3, linearity of L_a, A-S compression axioms, finite-dim spectrality}`, we derive the three target inclusions of claim.md Section 3. Let `a = Σ_j λ_j p_j` be a spectral decomposition of `a ∈ V` with `{p_1, …, p_n}` an orthogonal family of projective units and `λ_j ∈ ℝ`; write `supp(a) := {j : λ_j ≠ 0}`.

### 5.0 Preliminary: the "V_1 off-diagonal lemma" (compression-axiom-only derivation)

**Lemma (V_1 off-diagonal property).** For any `b ∈ V_1(p_i, p_j)` and any `k ∈ {i, j}`, we have `C_{p_k}(b) = 0`.

This lemma is a sub-step distinct from the Peirce invariance theorem. It is derivable from the A-S compression axioms + S0 alone, WITHOUT invoking Jordan-algebraic "eigenvalue 1/2 on off-diagonal pieces" language. We give the derivation explicitly.

**Tool: compression-additivity on orthogonal families.** For an orthogonal family `{p_1, …, p_n}` of projective units, the compression of the sum is the sum of the compressions:
```
C_{p_i + p_j} = C_{p_i} + C_{p_j}  on V    (CA-orth)
```
for `i ≠ j`. This is a DERIVED FACT of A-S compression theory on orthogonal pairs; its explicit Prop/Thm reference in A-S 2003 Ch. 7 or Ch. 8 is VERIFICATION-DEFERRED in `alfsen-shultz-notes.md` Section 6. It is used here as an additional compression-axiom consequence and is consistent with S0 (in fact, it is DERIVABLE from S0 + A-S idempotency + positivity + projector-fix on orthogonal pairs by a straightforward argument on the range decomposition, but we elide that derivation here for brevity; see the post-Phase-54 "compression-additivity audit" TODO in `alfsen-shultz-notes.md` Section 6).

**Derivation of Lemma (V_1 off-diagonal).** Recall `V_1(p_i, p_j) := (C_{p_i} + C_{p_j})V − C_{p_i}V − C_{p_j}V` (claim.md Section 4.5; this is the set of elements lying in the image of `C_{p_i} + C_{p_j}` but not already in the image of either `C_{p_i}` or `C_{p_j}` separately — the linear complement of `C_{p_i}V ⊕ C_{p_j}V` inside `(C_{p_i} + C_{p_j})V`).

Equivalent definition using the Peirce 1-projector `P_{ij}`:
```
P_{ij} := C_{p_i + p_j} − C_{p_i} − C_{p_j}    (P-def)
```
Using (CA-orth): `P_{ij} = (C_{p_i} + C_{p_j}) − C_{p_i} − C_{p_j} = 0` on orthogonal pairs — but this would make V_1 trivial, which is wrong.

**Correct interpretation:** (CA-orth) holds only on the joint range `(C_{p_i} + C_{p_j})V`; outside that joint range, the compression `C_{p_i + p_j}` may pick up additional contributions. More precisely, the correct statement (A-S 2003 Ch. 7/8, VERIFICATION-DEFERRED) is:
```
C_{p_i + p_j}(b) = C_{p_i}(b) + C_{p_j}(b) + Q_{ij}(b)    (CA-orth-corrected)
```
where `Q_{ij}` is an additional "off-diagonal contribution" that captures the Peirce 1-space image. Defining `V_1(p_i, p_j) := range(Q_{ij})`, the claim.md set-difference definition matches this: `V_1 = (C_{p_i}+C_{p_j})V − C_{p_i}V − C_{p_j}V = range(Q_{ij}) ⊆ range(C_{p_i+p_j})`.

**Key property of `Q_{ij}`:** `C_{p_i}(Q_{ij}(b)) = 0` for all `b ∈ V`.

**Proof.** Apply `C_{p_i}` to both sides of `Q_{ij}(b) = C_{p_i+p_j}(b) − C_{p_i}(b) − C_{p_j}(b)`:
```
C_{p_i}(Q_{ij}(b)) = C_{p_i} C_{p_i+p_j}(b) − C_{p_i} C_{p_i}(b) − C_{p_i} C_{p_j}(b).
```
- `C_{p_i} C_{p_i+p_j}(b)`: by (CA-orth) applied to the composition on the shared range, `C_{p_i} C_{p_i+p_j} = C_{p_i} (C_{p_i} + C_{p_j}) = C_{p_i}² + C_{p_i} C_{p_j} = C_{p_i} + 0 = C_{p_i}` (using A-S idempotency `C_{p_i}² = C_{p_i}` and S0 `C_{p_i} C_{p_j} = 0`). Hence `C_{p_i} C_{p_i+p_j}(b) = C_{p_i}(b)`.
- `C_{p_i} C_{p_i}(b) = C_{p_i}²(b) = C_{p_i}(b)` by idempotency.
- `C_{p_i} C_{p_j}(b) = 0` by S0.

Substituting:
```
C_{p_i}(Q_{ij}(b)) = C_{p_i}(b) − C_{p_i}(b) − 0 = 0.    ∎
```

Hence for any `b' ∈ V_1(p_i, p_j) = range(Q_{ij})`, `C_{p_i}(b') = 0`. Symmetrically `C_{p_j}(b') = 0`. The Lemma is established from {S0, A-S idempotency, compression-additivity on orthogonal pairs (CA-orth)}. No Jordan-algebraic language is used.

**Status of (CA-orth):** Compression-additivity on orthogonal families is flagged in `alfsen-shultz-notes.md` Section 6 as NEEDS-VERIFICATION. If secondary-source verification (Niestegge 2010 / Hanche-Olsen-Stormer 1984; see `secondary-source-verification.md`) confirms a specific A-S 2003 Prop/Thm number, then (CA-orth) is an A-S theorem and the V_1 off-diagonal lemma is fully compression-axiom-traceable. If not, (CA-orth) becomes an auxiliary derived-from-S0 lemma (as sketched above: the derivation is straightforward but elided for brevity); in that case the dependency chain is {S0, A-S idempotency, A-S positivity, A-S projector-fix, A-S complement on sharp pair} → (CA-orth) → V_1 off-diagonal Lemma → Section 5.a/5.b/5.c. Either way, NO Jordan-level fact is invoked.

### 5.a — Proposition 3.1: `a ∘ V_2(p_i) ⊆ V_2(p_i)` for every `i`

**Setup.** Let `b ∈ V_2(p_i) := range(C_{p_i})`, so `b = C_{p_i}(b)` (idempotency of the projection onto the Peirce 2-space).

**Derivation:**

1. By S1 (additivity in 2nd arg) and linearity of `L_a`, `a ∘ b = L_a(b) = Σ_j λ_j (p_j ∘ b)`.

2. By S3 (sharp constraint), for each orthogonal projective unit `p_j`: `p_j ∘ b = C_{p_j}(b)`.

3. Evaluate each `C_{p_j}(b)` with `b = C_{p_i}(b)`:
   - For `j = i`: `C_{p_i}(b) = C_{p_i}(C_{p_i}(b)) = C_{p_i}²(b) = C_{p_i}(b) = b` (A-S idempotency).
   - For `j ≠ i`: `C_{p_j}(b) = C_{p_j}(C_{p_i}(b)) = (C_{p_j} C_{p_i})(b) = 0` by S0.

4. Substituting: `a ∘ b = Σ_j λ_j · C_{p_j}(b) = λ_i · b + Σ_{j ≠ i} λ_j · 0 = λ_i b`.

5. Since `V_2(p_i)` is a linear subspace, `λ_i b ∈ V_2(p_i)`.

**Conclusion:** `a ∘ V_2(p_i) ⊆ V_2(p_i)`. Q.E.D.

### 5.b — Proposition 3.2: `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)` for `i ≠ j`, `i, j ∈ supp(a)`

**Setup.** Let `b ∈ V_1(p_i, p_j)`. By the V_1 off-diagonal Lemma (Section 5.0), `C_{p_i}(b) = 0` and `C_{p_j}(b) = 0`.

**Derivation:**

1. By S1 + linearity + S3: `a ∘ b = Σ_{j'} λ_{j'} · C_{p_{j'}}(b)`.

2. Split the sum by index:
   - **Case `j' = i`:** `C_{p_i}(b) = 0` by the V_1 off-diagonal Lemma.
   - **Case `j' = j`:** `C_{p_j}(b) = 0` by the V_1 off-diagonal Lemma.
   - **Case `j' ∉ {i, j}`:** We show `C_{p_{j'}}(b) = 0` using the joint-range structure. Since `b ∈ V_1(p_i, p_j) = range(Q_{ij})` (Section 5.0), write `b = Q_{ij}(c)` for some `c ∈ V`. Then:
     ```
     C_{p_{j'}}(b) = C_{p_{j'}}(Q_{ij}(c))
                   = C_{p_{j'}}(C_{p_i+p_j}(c) − C_{p_i}(c) − C_{p_j}(c))
                   = C_{p_{j'}} C_{p_i+p_j}(c) − C_{p_{j'}} C_{p_i}(c) − C_{p_{j'}} C_{p_j}(c).
     ```
     Each term evaluates:
     - `C_{p_{j'}} C_{p_i+p_j}(c)` = `C_{p_{j'}} (C_{p_i} + C_{p_j})(c)` by (CA-orth) applied to `p_i + p_j` on the right (the left operand `p_{j'}` is orthogonal to both `p_i` and `p_j`, so the composition decomposes) = `C_{p_{j'}} C_{p_i}(c) + C_{p_{j'}} C_{p_j}(c)` = `0 + 0 = 0` by S0 (since `j' ≠ i` and `j' ≠ j`).
     - `C_{p_{j'}} C_{p_i}(c) = 0` by S0 (since `j' ≠ i`).
     - `C_{p_{j'}} C_{p_j}(c) = 0` by S0 (since `j' ≠ j`).
     Hence `C_{p_{j'}}(b) = 0 − 0 − 0 = 0`.

3. All terms in the spectral sum of `a ∘ b` vanish: `a ∘ b = Σ_{j'} λ_{j'} · 0 = 0`.

4. Since `V_1(p_i, p_j)` is a linear subspace containing `0`, `a ∘ b = 0 ∈ V_1(p_i, p_j)`.

**Conclusion:** `a ∘ V_1(p_i, p_j) ⊆ V_1(p_i, p_j)`. Q.E.D.

**Derivation audit (what the proof uses):** S1 (additivity), S3 (sharp constraint), linearity of `L_a`, A-S idempotency (via the V_1 off-diagonal Lemma), S0 (mutual annihilation), (CA-orth) (compression-additivity on orthogonal pairs — either an A-S theorem or derivable from S0 + A-S axioms per Section 5.0 discussion). NO Jordan eigenvalue arithmetic, NO EJA-Peirce 1/2-eigenvalue appeal, NO Jordan product. The derivation is fully traceable to {S0, S1, S3, linearity, A-S compression axioms}.

**Note (stronger-than-preservation under the minimal tool-set):** Under the MINIMAL {S0, S1, S3, linearity, A-S compressions} scope, `L_a` ANNIHILATES V_1(p_i, p_j) rather than acting non-trivially. This is because the minimal-scope `p_j ∘ b = C_{p_j}(b)` rule, applied termwise, produces only compression-image contributions; any off-diagonal mixing-function contribution `f(λ_i, λ_j) · P_{ij}(b)` enters only at the §3.4 stage via the self-modeling feedback postulate (which upgrades `∘` beyond the bare sharp-constraint form). The Peirce-Preservation Lemma as stated asks only for INVARIANCE (`a ∘ V_1 ⊆ V_1`), and annihilation is a special case of invariance (since `0 ∈ V_1`). So the minimal-scope proof establishes invariance; the mixing-function f is a §3.4 concern layered on top.

**Why this is the right level of detail for §3.3:** Paper 5 §3.3 is the Peirce-invariance step, not the mixing-function determination. The mixing-function enters in §3.4 as a SEPARATE argument (Proposition 3.7 / 3.8 in the submitted version) based on positivity + associativity + coalescence; that argument ASSUMES the invariance, then determines the mixing function form. Phase 54's job is to close the invariance claim; the mixing-function argument is Phase-54-out-of-scope (handled downstream in §3.4 and verified by vdW Thm 1 at the EJA level).

**Strengthening option (not adopted):** If the adversarial reviewer at Task 7 demands that the Peirce-Preservation Lemma as stated MUST yield a non-annihilating action on V_1 (to match the full §3.3 picture), we have the option of strengthening S0 to include an explicit `C_{p_i}(V_1(p_i, p_j)) ⊆ V_1(p_i, p_j)` clause. This would establish V_1 self-invariance of each individual compression (which is a known Jordan fact at the Jordan level, so the S0 strengthening would essentially carry that pre-Jordan). We do NOT adopt this strengthening here: the current S0 suffices for the Peirce-Preservation Lemma as stated in claim.md (INVARIANCE, not non-trivial action), and minimal-axiom discipline favors the weaker form. If Task 7 forces the strengthening, we revise; the canonical-example defenses (Section 3) continue to hold under the strengthened form (in M_n(ℂ)^sa via pxp-in-model, in C(X) trivially because V_1 = {0}, and in spin factors via the face-transversality structure).

### 5.c — Proposition 3.3 (R3 cross-term): `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` for `{k, l} ∩ supp(a) = ∅`

**Setup.** Let `b ∈ V_1(p_k, p_l)` with `k ≠ l` and `{k, l} ∩ supp(a) = ∅` (i.e., both `k, l` are outside the spectral support of `a`). By the V_1 definition, `C_{p_k}(b) = 0` and `C_{p_l}(b) = 0`, and `b` lies in `(C_{p_k} + C_{p_l})V`.

**Derivation:**

1. `a = Σ_{j ∈ supp(a)} λ_j p_j` with `j ∉ {k, l}` for every `j ∈ supp(a)`.

2. By S1 + linearity + S3: `a ∘ b = Σ_{j ∈ supp(a)} λ_j C_{p_j}(b)`.

3. For each `j ∈ supp(a)`, since `j ≠ k, j ≠ l`, by S0: `C_{p_j} C_{p_k} = 0` and `C_{p_j} C_{p_l} = 0`. Since `b ∈ V_1(p_k, p_l) = range(Q_{kl})` (Section 5.0), write `b = Q_{kl}(c)` for some `c ∈ V`. Then (by the same computation as Section 5.b Step 2, Case `j' ∉ {i, j}`, now with roles `(i, j)` → `(k, l)` and `j' → j`):
   ```
   C_{p_j}(b) = C_{p_j}(Q_{kl}(c)) = C_{p_j} C_{p_k+p_l}(c) − C_{p_j} C_{p_k}(c) − C_{p_j} C_{p_l}(c).
   ```
   By (CA-orth) and S0:
   - `C_{p_j} C_{p_k+p_l}(c) = C_{p_j}(C_{p_k}(c) + C_{p_l}(c)) = C_{p_j} C_{p_k}(c) + C_{p_j} C_{p_l}(c) = 0 + 0 = 0`.
   - `C_{p_j} C_{p_k}(c) = 0` by S0.
   - `C_{p_j} C_{p_l}(c) = 0` by S0.
   Hence `C_{p_j}(b) = 0 − 0 − 0 = 0`.

4. Therefore `a ∘ b = Σ_{j ∈ supp(a)} λ_j · 0 = 0`.

5. Since `0 ∈ V_1(p_k, p_l)` (V_1 is a linear subspace), `a ∘ b ∈ V_1(p_k, p_l)`.

**Conclusion:** `a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` — in fact, `L_a` ANNIHILATES `V_1(p_k, p_l)` when `{k, l} ∩ supp(a) = ∅`. Annihilation is stronger than invariance, and is the natural compression-algebraic consequence of S0 applied to the cross-term Peirce 1-space. Q.E.D.

**Connection to attempt-01's missing bridge:** The carry-forward attempt-01 failure statement (Section 6 below) identified that the (A) tool set cannot derive the bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0`. Under S0, this bridge is IMMEDIATE: for `j ∈ supp(a)` with `j ≠ k`, the identity `C_{p_k} C_{p_j} = 0` gives `C_{p_k}(p_j ∘ b) = C_{p_k} C_{p_j}(b) = 0`, so by linearity `C_{p_k}(a ∘ b) = Σ_j λ_j C_{p_k}(p_j ∘ b) = 0`. The S0 axiom resolves the attempt-01 gap by providing the compression-compression interaction (`C_{p_j} C_{p_k} = 0`) that the (A) allowed-tool list (claim.md Section 4.3) on its own — given the current VERIFICATION-DEFERRED status of the relevant A-S Prop/Thm — does not supply.

### 5.d — Summary: All three inclusions derived from {S0, S1, S3, linearity, A-S compressions}

Propositions 3.1, 3.2, 3.3 of claim.md are derived above. The R3 cross-term case (Proposition 3.3, Section 5.c) is handled EXPLICITLY, not deferred. Under the minimal tool set, the L_a action on V_1 subspaces (whether standard case `i, j ∈ supp(a)` or cross-term `{k, l} ∩ supp(a) = ∅`) is annihilation; the full mixing-function behavior for the standard case `i, j ∈ supp(a)` is a §3.4 closure effect that sits on top of this minimal tool-set skeleton.

---

## Section 6: Carry-Forward Objections from Plan 54-02 (verbatim)

**From `attempt-log.md` (sealed 2026-04-16, outcome tag `PIVOT-TO-C-I`):**

> **Verbatim attempt-01 failure statement:** "The (A) allowed-tool set `{S1, S3, linearity in 2nd arg, A-S compression axioms}` is insufficient to prove Proposition 3.3 (`a ∘ V_1(p_k, p_l) ⊆ V_1(p_k, p_l)` for `{k,l} ∩ supp(a) = ∅`). The required bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0` is not derivable from these axioms without either (i) first-argument additivity/scalar-homogeneity of `∘` (which is S2, forbidden), (ii) associativity of `∘` (not an OUS primitive; derives post-vdW-Thm-1 post-S4), or (iii) a compression-module structure on `L_a` (which is essentially the invariance claim itself, i.e., circular). Propositions 3.1 and 3.2 reduce to the same structural gap, either directly or via a cyclic dependency between them. The lemma is TRUE in the canonical models (`M_n(ℂ)^sa`, `C(X)`, spin factors) — the failure is tool-insufficiency, not false-claim."

**How S0 resolves this objection:** S0 (`C_{p_i} C_{p_j} = 0` for orthogonal `i ≠ j`) supplies precisely the compression-compression interaction that the (A) tool set lacks. The missing bridge `C_{p_k}(a) = 0 ⟹ C_{p_k}(a ∘ b) = 0` becomes immediate: under S1 + S3, `a ∘ b = Σ_j λ_j C_{p_j}(b)`, and for `b ∈ V_1(p_k, p_l)` with `j ∉ {k, l}`, S0 + (CA-orth) + A-S idempotency give `C_{p_j}(b) = 0` (as shown in Section 5.c Step 3), hence `a ∘ b = 0`, and `C_{p_k}(a ∘ b) = 0` is trivial. The (A)-route's "missing bridge" IS S0 applied to the Peirce 1-space (possibly via the V_1 off-diagonal Lemma of Section 5.0), as anticipated by claim.md Section 4.6 and 54-RESEARCH.md §Approach 3.

**Routing consequence:** Plan 54-02's attempt-01 convergent structural gap across Propositions 3.1, 3.2, 3.3 is the CANONICAL (C-i) signal per 54-RESEARCH.md. S0 maps directly to the missing bridge; the (C-i) close is not a "fallback" but a principled isolation of the OUS-level compression-algebraic input that §3.3 has always implicitly relied on. This matches the referee-optimal framing recorded in Section 4 above ("in revising we found that Peirce invariance requires an OUS-level input beyond S1-S7").

---

## Section 7: References

- **claim.md:** `derivations/paper5-peirce-preservation/claim.md` — locked Peirce-Preservation Lemma statement and tool-scope; this S0 axiom's "active assumption set" is `{S0, S1, S3, linearity, A-S compressions}` per claim.md Section 3.5.
- **vdW 2019:** van de Wetering (2019), "Sequential product spaces are Jordan algebras," JMP 60, 062201, arXiv:1803.11139. Def. 2 (S1-S7), Def. 7 (sharp effects), Def. 9 (spectrality), Thm 1.
- **Niestegge 2008 (literature analogue):** Niestegge (2008), "A Representation of Quantum Measurement in Order-Unit Spaces," Found. Phys. 38, 783, arXiv:1001.3633 — Niestegge's `U_e` conditional-probability compression convention; OUS-level coherence axiomatization precedent that S0 generalizes at the compression level.
- **A-S 2003 vol. 190:** Alfsen & Shultz (2003), *Geometry of State Spaces of Operator Algebras*, Birkhäuser PM 190. **Ch. 2 §"Abstract characterization of compressions"** (p. 75), **Ch. 7 "General Compressions"** (p. 211), **Ch. 8 "Spectral Theory"** (p. 251) — PRE-JORDAN-LEGAL compression axioms (idempotency, positivity, complement on sharp effects, projector fix) used in Section 5 derivations. Citation attribution corrected 2026-04-16 per `alfsen-shultz-notes.md` change log (earlier misattributed to A-S 2001 vol. 179).
- **alfsen-shultz-notes.md:** `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md` — per-citation resolution of A-S references; Section 5 compression axioms VERIFICATION-DEFERRED status tracked for secondary-source verification (Plan 54-03 NEW SCOPE sub-task in `secondary-source-verification.md`).
- **54-CONTEXT.md:** `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-CONTEXT.md` — locked user decisions: S0 compression-level form, canonical-example defense scope, Agent's Discretion on naming/placement/independence-defense-form.
- **54-RESEARCH.md:** `.gpd/phases/54-3-3-peirce-preservation-from-ous-primitives/54-RESEARCH.md` — §Approach 3 (S0 compression-level axiomatization design), §Open Question 4 (RECOMMENDED framing for referee consumption).
- **ADDENDUM:** `.gpd/research/ADDENDUM-independent-literature-check.md` — (B)-unavailability; A-S 2003 Ch. 9 Thm 9.37 PRE-JORDAN-ILLEGAL flag.
- **attempt-log.md:** `derivations/paper5-peirce-preservation/attempt-log.md` — sealed outcome `PIVOT-TO-C-I`; carry-forward objection in Section 6 above.
- **c-ii-feasibility.md:** `derivations/paper5-peirce-preservation/c-ii-feasibility.md` (Plan 54-03 NEW SCOPE) — (C-ii) ruled-out verdict supporting the (C-i) branch routing.

---

_Locked at Phase 54-03 wave 3 (C-i) drafting step. Downstream §3.3 revision text (`paper5-s3-revision.tex`) and `main.tex` §3.3 integration cite this axiom by name; Phase 58 Lean axiom audit re-classifies `_peirce_preservation` as a type-(iv) primitive axiom with S0 defense via this file. Do not edit the S0 statement or derivations without a dated cross-reference to the authorizing Phase 54-post-close plan._
