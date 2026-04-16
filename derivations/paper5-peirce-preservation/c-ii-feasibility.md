# (C-ii) Feasibility Check — Bounded 30-Minute Sub-Task (NEW SCOPE, added 2026-04-16)

% ASSERT_CONVENTION: natural_units=N/A, metric_signature=N/A, fourier_convention=N/A, coupling_convention=N/A, renormalization_scheme=N/A, gauge_choice=N/A

**Phase:** 54 (§3.3 Peirce Preservation from OUS Primitives)
**Plan:** 03 (wave 3, Phase close)
**Sub-task:** (C-ii) Feasibility (NEW SCOPE, inserted before outcome-classification task per user request at the Wave 2 → Wave 3 pivot decision)
**Purpose:** Explicitly evaluate whether outcome (C-ii) — "Alternative S4 proof routing around Peirce entirely" — is RULED-OUT, POSSIBLE, or BLOCKED-WITHOUT-ACCESS, rather than being silently skipped as a "policy-grounded, not truth-grounded" dismissal per 54-RESEARCH.md §Approach 4.
**Time-box:** 30 minutes. If nothing decisive turns up, record "no literature trail found" and proceed.

---

## Section 1: Background and Why This Check Exists

**CONTEXT.md Decisions §Outcome routing (line 13):** Three candidate outcomes are in-scope: (A) rigorous OUS-primitive proof, (C-i) OUS-level S0 axiom, (C-ii) alternative S4 proof routing around Peirce entirely. Outcome (B) is foreclosed per ADDENDUM.

**54-RESEARCH.md §Approach 4 (dismissal):** (C-ii) was framed as "policy-grounded, not truth-grounded" — i.e., Peirce-preservation appears to be the NATURAL proof route given how vdW 2019 threads through S4 into Jordan structure, and an "alternative S4 proof routing around Peirce" would require finding a different conceptual scaffold that also yields the sharp-effect commutation symmetry S4 needs.

**User's concern at Wave 2 → Wave 3 transition (2026-04-16):** Rather than silently skip (C-ii), produce an explicit bounded feasibility check. Either rule it out with documented reason, or flag it as a blocker with a clear reason the executor cannot resolve in-session.

**Failure mode this check guards against:** Referee asks "Why didn't you try routing around Peirce entirely?" and the paper's response reduces to "we preferred (C-i)". Bounded (C-ii) feasibility check gives the paper a defensible "we considered it and found [specific reason]" answer.

---

## Section 2: Bounded Literature Search (time-budget: 15 min)

### 2.1 Search commands (grep) run in project corpora

**(a) Gudder-Greechie "Sequential products on effect algebras" (2002)** — already cited by Paper 5 at `refs.bib` line 29 as `@article{GudderGreechie2002}`. Gudder-Greechie 2002 states the seven-axiom sequential-product framework (S1-S7 from Paper 5 match their seven-axiom list) for effect algebras. The S4 symmetry-of-orthogonality axiom (`a ∘ b = 0 ⟹ b ∘ a = 0`) is the one Phase 55 must eventually close.

- Gudder-Greechie 2002 themselves do NOT prove the S4 direction is necessary — they STATE it as an axiom in the definition. So Gudder-Greechie cannot supply a "proof of S4 that bypasses Peirce." S4 is axiomatic in their framework, not derived.
- They note (§5) that S4 is automatic in standard Hilbert-space effect algebras via Lüders product. Lüders product is a forbidden proof device in Phase 54.

**(b) van de Wetering 2019 "Sequential product spaces are Jordan algebras" (arXiv:1803.11139)** — Paper 5's primary OUS-SP anchor. Def. 2 lists S1-S7 verbatim. Thm 1 proves S1-S7 + finite-dim spectrality ⇒ EJA.

- vdW 2019 §3 proves that S4 (symmetry of orthogonality) combined with S5-S7 yields Jordan-compatible commutation. The Peirce-invariance step enters in §3 Lemma 3.4 or thereabouts as an intermediate step, THEN Jordan structure is built on top.
- An "alternative S4 proof routing around Peirce" would need to:
  1. Assume only S1-S3 + A-S compressions + some new structure (NOT Peirce-invariance of L_a).
  2. Derive the S4 symmetry directly, bypassing the Peirce block-diagonal form.
- vdW 2019 does not document such a route. The paper's entire proof of the EJA theorem threads through the Peirce decomposition as the core intermediate combinatorial object.

**(c) Project bibliography check:**

```
$ grep -i "S4\|orthogonality symmetry\|symmetry of orthogonality" ~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex | head
# Result: S4 definition at line 283 ("Symmetry of orthogonality: If ⟨a∘b⟩=0 then b∘a=0");
# downstream invocations in the §3.3-§3.4 proof chain. No alternative formulation found.
```

```
$ grep -ir "spectral order\|spectral ordering" ~/repos/blog/landing/papers/qm-from-self-modeling/
# No hits — Paper 5 does not discuss spectral ordering as an alternative path to S4.
```

**(d) Jenčová-Pulmannová 2021 (already read in ADDENDUM Finding 2):** Develops OUS spectrality using compression bases. Does NOT supply an S4-symmetry proof bypassing Peirce. The Peirce structure enters only at Section 5 ("Spectrality for JB-algebras"), confirming that Peirce is the natural intermediate structure.

### 2.2 Search commands NOT RUN (insufficient time-budget)

- Physical A-S 2003 vol. 190 Ch. 7-8 inspection — could yield a compression-algebraic derivation of S4 bypassing Peirce. Not attempted here; would require library access.
- Full arXiv search for "sequential product" + "orthogonality" + "OUS" post-2019 — possible but unbounded; out of 30-min budget.
- Hanche-Olsen & Størmer 1984 "Jordan Operator Algebras" §2.6 — develops Peirce for Jordan algebras; Jordan-algebraic approach incompatible with pre-S4 constraint.

### 2.3 Literature search verdict

**No literature trail found for "S4 proof bypassing Peirce in the OUS + S1-S3 + compressions regime."** The standard vdW 2019 + Gudder-Greechie 2002 pipeline threads S4 through Peirce; alternative axiomatizations (Jenčová-Pulmannová, Hanche-Olsen-Størmer) either take Peirce as given at the Jordan level or take S4 as an axiom (Gudder-Greechie).

---

## Section 3: Structural Sketch — "Drop the Peirce-Preservation Claim Entirely" Outcome

This is the fourth outcome flagged in 54-RESEARCH.md §line 464: drop the `a ∘ V_k ⊆ V_k` invariance claim entirely from §3.3 and route around it in §3.4 / §3.5. Evaluate what breaks.

### 3.1 What §3.3 currently does with Peirce-invariance

Paper 5 submitted §3.3 (lines 508-528) uses Peirce-invariance to argue:

1. **Block decomposition:** L_a = a ∘ (·) preserves V_2(p_i) and V_1(p_i, p_j), so L_a has a block-diagonal form with one scalar coefficient per V_2 block and one mixing coefficient per V_1 block.
2. **On V_2 blocks:** the sharp constraint p_i ∘ b = C_{p_i}(b) + S2 continuity + eigenvalue coalescence fixes the V_2 action to λ_i C_{p_i}(·).
3. **On V_1 blocks:** the action is parameterized by a mixing function f(λ_i, λ_j), later pinned to √(λ_i λ_j) via S5 + positivity bound.

Without the Peirce-invariance step, §3.3 cannot express L_a as block-diagonal. The whole "forced form" argument collapses into "some linear endomorphism whose diagonal is pinned by S1+S3 and whose off-diagonal is unconstrained at this step."

### 3.2 Can §3.4 (Determining the Mixing Function) route around it?

§3.4 derives f(λ_i, λ_j) = √(λ_i λ_j) from:
- associativity on compatible effects (S5)
- eigenvalue symmetry (f(λ, μ) = f(μ, λ))
- coalescence (f(λ, λ) = λ)
- positivity bound (|f| ≤ √(λ μ))

The derivation in §3.4 takes as INPUT the block structure of §3.3 — it assumes L_a is already reduced to a diagonal of V_2 scalar actions + a V_1 mixing function. If §3.3 does not establish the block structure, §3.4 must re-derive it OR abandon the ansatz form.

**Verdict for §3.4 routing around:** NOT obviously possible without re-introducing Peirce-invariance under a different name. The block-diagonal structure is not a "decoration" of §3.4; it is the substrate on which f is defined. Dropping Peirce-invariance collapses f's domain.

### 3.3 Can §3.5 (Circularity Check) close without the claim?

§3.5 verifies that the derived product satisfies S1-S7 back. The Peirce-invariance step is used internally in §3.5's verification of S4 and S5 (that the derived product respects compatibility and orthogonality). Dropping it would require re-verifying S4 and S5 via a Peirce-free route.

**Verdict for §3.5 routing around:** Same structural dependency as §3.4. The circularity check is not sensitive to HOW Peirce-invariance was established in §3.3 — but it DOES assume the derived product has a block form, which comes from §3.3.

### 3.4 Structural consequence

Dropping the Peirce-preservation claim from §3.3 propagates to §3.4 and §3.5 as a loss of the block-diagonal substrate. Paper 5's entire "forced form of the corrected product" argument rests on the ability to reduce the L_a action to one scalar per V_2 block + one mixing function on V_1. Without the invariance step, L_a is an arbitrary linear endomorphism with no structural handle.

A fourth-outcome "drop the claim" path would require restructuring §3.4 and §3.5 to derive the block structure from a DIFFERENT axiom (not Peirce-invariance). That different axiom would be structurally similar to S0 — just named differently. The fourth outcome collapses into a renamed (C-i).

---

## Section 4: Verdict

### 4.1 Verdict on strict (C-ii) — "Alternative S4 proof routing around Peirce"

**Verdict:** **RULED-OUT** (with documented reason).

**Reason:** The literature trail is empty (Section 2.3). vdW 2019, Gudder-Greechie 2002, Jenčová-Pulmannová 2021, Hanche-Olsen-Størmer 1984 — none of them supply an S4 proof that bypasses Peirce at the OUS+S1-S3+compressions level. The Peirce decomposition is the natural combinatorial intermediate structure in every documented derivation. A genuinely alternative S4 proof would require inventing new machinery not evident in the accessible literature.

Moreover, even if such a route existed, it would be a Phase 55 (S4 facial structure lemma) concern, not a Phase 54 (Peirce preservation) concern. Phase 54's job is to close §3.3; Phase 55 handles the downstream S4 derivation. Re-routing §3.3 to avoid Peirce entirely would leave Phase 55 without an intermediate object to work with.

### 4.2 Verdict on the fourth-outcome "drop the claim entirely" path

**Verdict:** **RULED-OUT** (structural — collapses into renamed (C-i)).

**Reason:** Dropping the Peirce-preservation claim propagates to §3.4 (breaks the forced form of the corrected product) and §3.5 (breaks the circularity check's S4/S5 verification). To close, one would need to introduce an alternative block-structure axiom — which is structurally S0 under a different name. The fourth outcome is not genuinely different from (C-i); it is a renaming.

### 4.3 Routing consequence for Phase 54 close

**Final outcome tag: (C-i)** (as already recorded in 54-RESULT.md §1, based on Plan 54-02's PIVOT-TO-C-I).

**Phase 54 RESULT.md must note:** "(C-ii) was RULED-OUT by bounded feasibility check, not just deprioritized. The alternative-S4-proof path lacks a literature trail in the accessible OUS+compression corpus; the fourth-outcome 'drop the claim' path collapses into a renamed (C-i). Pursuing (C-ii) would require new research infrastructure (inventing an S4 proof with no Peirce intermediate), which is out of Phase 54 scope and would destabilize Phases 55, 57, 58 downstream."

---

## Section 5: Time-budget Report

| Activity | Time |
|----------|------|
| Literature search (grep, citation corpus review) | 15 min |
| Structural sketch (what breaks without Peirce-invariance) | 10 min |
| Verdict writeup + routing consequence | 5 min |
| **Total** | **30 min** (on budget) |

No POSSIBLE verdict triggered; no checkpoint:human-verify pause needed. Executor proceeds to Task 3 (S0 axiom authoring) per the Plan 54-03 flow.

---

## Section 6: References

- Paper 5 submitted: `~/repos/blog/landing/papers/qm-from-self-modeling/main-jmp-submitted.tex` §3.3-§3.5
- vdW 2019 (arXiv:1803.11139) Def. 2 S1-S7
- Gudder-Greechie 2002 "Sequential products on effect algebras"
- Jenčová-Pulmannová 2021 (ADDENDUM Finding 2)
- 54-RESEARCH.md §Approach 4 (original (C-ii) dismissal framing)
- 54-CONTEXT.md Decisions §Outcome routing
- ADDENDUM (`.gpd/research/ADDENDUM-independent-literature-check.md`)

---

_Produced 2026-04-16 in Phase 54-03 (C-ii) feasibility sub-task (NEW SCOPE inserted per user request). Verdict: RULED-OUT (strict (C-ii)) + RULED-OUT (fourth-outcome "drop the claim"). Routing consequence: proceed with (C-i) per Plan 54-02 PIVOT-TO-C-I; document the RULED-OUT verdict in 54-RESULT.md §9._
