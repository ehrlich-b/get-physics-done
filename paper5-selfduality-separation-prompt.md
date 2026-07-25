# Paper 5 — The Self-Duality Separation (does faithful self-tracking FORCE pure-state-transitivity = self-duality, or is it an irreducible dynamical +1?)

## TASK TYPE
Settle ONE specific claim (CLAIM SD-FORCE below), prove-or-disprove, with a decision tree.
This is the **exact analogue of the field-blindness separation** done for the complex step
(`paper5-field-blindness-separation-prompt.md`). There, complex = self-modeling + an irreducible
dynamical datum (the generator is an observable / `V` closed under `⟦a,b⟧=−i[a,b]`), with the
rebit `M_n(R)` as the field-blind witness. **Here we ask the same question one level down, at the
Jordan step:** is self-duality FORCED by faithful self-tracking, or is it (like complex) an
irreducible dynamical import witnessed by a model?

This is NOT a re-run of "does Def-1 entail self-duality" — that is **settled FALSE** (Vinberg /
Niestegge ⊨ Def-1, non-self-dual; verified this session, `joint1_jordan.py`, exact/ℚ). The new,
un-run question is whether a **dynamical** demand on the self-tracking flow forces it.

---

## 0. The one claim to settle

> **CLAIM SD-FORCE.** Faithful self-modeling forces the **reversible** self-tracking group (the
> compact / order-automorphism flows that preserve the state space) to act **transitively on pure
> states**. Equivalently, given the field-blind self-modeling core, it forces **self-duality**
> (hence, with homogeneity, Jordan — Koecher–Vinberg).

Prove it or disprove it.
- **Disproof** = exhibit a faithful self-model whose reversible self-tracking can "work from any
  state" in whatever sense faithful self-modeling actually requires, *without* being
  pure-state-transitive (candidate: **Vinberg**). ⟹ self-duality is an **irreducible import**,
  witnessed by a model — Paper 5's Jordan step is an IMPORT (the P1 / conditional paper), and we
  instead deliver a clean **separation theorem** (SD1–SD4 below).
- **Proof** = show "faithful + reversible + works-from-any-state" self-tracking entails the
  reversible group is pure-state-transitive, **non-circularly** (without assuming self-duality,
  symmetric transition, K≅K*, or a conjugate-correlator as input), with **Vinberg explicitly
  excluded**. ⟹ the Jordan step is **FORCED** (the P2 upgrade).

Both outcomes are publishable and both are wanted. This decides whether the Jordan step is a
forcing or an import — the single remaining open question in Paper 5's spine.

---

## 1. Why this is the question (context — read once)

The spine: `self-modeling → loop builds eq:sp-explicit → S1–S7 → [vdW Thm 1, biconditional] EJA
→ [self-duality/S4] → [central-i/LT] complex M_n(C)`.

Two selectors sit on this spine. As of this session BOTH are proven irreducible **by explicit
models**, so as-stated Paper 5 is a two-import synthesis with zero forcing steps:
- **complex** ← central-i / dynamical correspondence; witness it's needed: **rebit `M_n(R)`** (⊨
  the field-blind core, not complex). *Settled import* — see field-blindness prompt.
- **Jordan** ← self-duality (= vdW S4 = symmetric transition = recognition symmetry); witness:
  **Niestegge-2024 rank-2 ℓ⁴ qubit** (⊨ Def-1, non-self-dual: transition 3/4 ≠ 9/16, X*=ℓ^{4/3}≠ℓ⁴;
  verified exact/ℚ this session) and **Vinberg** (homogeneous, non-self-dual, non-Jordan).

The static question ("does Def-1 force self-duality?") is **closed: NO**. THIS task asks the
**dynamical** question that the static witnesses do not touch: the witnesses are static order-unit
spaces; self-modeling is a *loop* (test → update → test), i.e. a **dynamics**. Does the dynamics —
specifically a *reversible* self-tracking flow that must work from *any* state — force what the
static structure does not?

**The complex step is the precedent for HOW this can go.** There, the analogous dynamical hope
("self-models track their becoming ⟹ complex") **died** because the rebit tracks its becoming
reversibly with a non-observable generator (a field-blind "level 2" witness exists). The question
here is whether the self-duality analogue has an equally clean field-blind escape, or whether the
"works from any state" demand has **no** non-transitive witness and thus forces self-duality.

---

## 2. The objects (self-contained)

### 2.1 Homogeneity vs pure-state-transitivity (THE FULCRUM — do not conflate)
- **Homogeneity:** the *full* linear automorphism group of the cone acts transitively on the cone
  **interior**. (Vinberg's cone IS homogeneous.)
- **Pure-state-transitivity:** the group of **reversible** transformations (those preserving the
  normalized state space — the compact / "physical-symmetry" subgroup) acts transitively on the
  **pure states** (extreme points). (Quantum: `U(n)` on pure states. **Vinberg's reversible group
  does NOT** — that failure *is* its non-self-duality.)
- **Koecher–Vinberg:** homogeneous + self-dual ⟺ symmetric cone ⟺ EJA.
- **Barnum–Ududec–van de Wetering** (arXiv:2306.00362, *verify exact statement*): homogeneity +
  pure-state-transitivity ⟹ **self-dual**. Converse on homogeneous cones: self-dual ⟹ the
  reversible isotropy group is pure-state-transitive.

So **self-dual ⟺ pure-state-transitive reversible group** (given homogeneity). Vinberg separates
homogeneity from pure-state-transitivity: it has the first, not the second. **This is why the
question is not a rename of self-duality** — "the reversible flow reaches all pure states" is a
substantive dynamical condition that a homogeneous-but-non-self-dual cone fails.

### 2.2 The self-tracking flow (de-woo the loop into a group)
The loop is test → update → record → test. State its dynamical content algebraically, NOT in prose:
- A **self-tracking flow** = a one-parameter group of order-automorphisms `e^{tD}` under which the
  model faithfully follows the body's state. (Stone: a reversible flow has a generator `D`.)
- **Reversible** = information-preserving = the record is lossless (a *faithful* record loses no
  information about what it records, so the recording map is invertible on its image).
- **Works from any state** = the self-model must represent the body's evolution starting from
  *any* of its states (a model that only tracks trajectories through one fixed state is not a
  faithful model of the whole system).

The candidate FIT (to prove or break): **reversible + works-from-any-state ⟹ the reversible group
is transitive on pure states**.

### 2.3 Definition 1 / the field-blind core
Read main.tex:357–376. For this task, take the **field-blind core** = everything Vinberg also
satisfies (Def-1 clauses with φ=id, spectral/compression structure, homogeneity to the extent the
loop supplies it). We are *isolating the discriminator*: by construction Vinberg ⊨ the core, so the
ONLY thing that can exclude it is the dynamical datum. **Known subtlety to flag, not relitigate:**
deep-note §15 records Vinberg failing S4 *and* S6 (vdW §VII), so homogeneity may itself not be
fully loop-forced. Do NOT re-open joint-1 homogeneity here — assume the core and test whether the
*dynamical* datum forces self-duality (S4) on top of it. If your verdict depends on the S6 gap,
say so.

---

## 3. The separation theorem to state (the deliverable when SD-FORCE is FALSE)

Mirror the field-blindness theorem's S1–S4 structure.

- **(SD1) STATIC-BLINDNESS.** Vinberg (homogeneous, non-self-dual, non-Jordan) ⊨ the field-blind
  core — so static self-modeling does not force self-duality. PLUS every static strengthening is
  blind: confirm each of {records-are-states (gives K≅K via φ=id, NOT K≅K*); no-cloning;
  no-broadcasting; Breuer self-measurement; recursive self-model tower; self-induced decoherence}
  is satisfied by Vinberg (i.e. none excludes it). [Re-confirm Vinberg ⊨ core; confirm the list.]
- **(SD2) THE DYNAMICAL DATUM IS THE SELECTOR.** Self-duality is selected exactly by:
  **pure-state-transitivity of the reversible self-tracking group** (Barnum–Ududec–vdW + KV).
- **(SD3) IRREDUCIBILITY (well-posed, not a universal quantifier).** Vinberg *has* reversible flows
  (its compact isotropy subgroup) that are NOT pure-state-transitive. So "carries reversible
  self-tracking dynamics" is field-blind (Vinberg ⊨ it); the selector is the strictly stronger
  **transitivity** of that group. State as the algebraic biconditional `self-dual ⟺
  reversible-pure-state-transitive (given homogeneity)`, NOT as "no property weaker than self-dual
  forces self-dual."
- **(SD4) PHYSICAL IDENTITY [STRUCTURAL-CORRESPONDENCE — label it].** The +1 = "the reversible
  self-tracking flow reaches all my pure states" = "no dynamically-preferred state" =
  relativity-of-isomorphism in dynamical form. This is the constitutive gloss; the math is SD3.

## 3′. The forcing to attempt FIRST (the deliverable when SD-FORCE is TRUE)

Before settling for the separation, **try to make it a FIT** (steelman mandate). Attempt to prove:

> **faithful (lossless ⟹ reversible) self-tracking that works from any state ⟹ the reversible
> self-tracking group acts transitively on pure states.**

Concretely this requires breaking the disproof in §4. The make-it-fit hunt routes through an
already-trusted result: you do NOT need to prove self-duality directly — by Barnum–Ududec–vdW it
suffices to force **pure-state-transitivity** given homogeneity. So the entire forcing reduces to:
*does faithful reversible self-tracking force the reversible group transitive?*

---

## 4. The decider (the actual computation — Vinberg is the crux)

**Question:** Does **Vinberg** admit a *reversible* self-tracking flow that "works from any state"
in the sense faithful self-modeling requires, **without** its reversible group being
pure-state-transitive?

- Compute Vinberg's reversible (compact / order-automorphism-preserving-the-state-space) group and
  its orbits on pure states. Confirm it is **not** transitive (it can't be — non-self-dual), and
  identify the orbit structure (which pure states are reachable from which).
- Then decide the constitutive question: is "works from any state" satisfiable by these
  **non-transitive** reversible flows (each orbit self-tracks fine, the model just can't reversibly
  *map between* orbits)? Two outcomes:
  - **YES** — Vinberg self-tracks faithfully and reversibly within its orbits, and faithful
    self-modeling does NOT demand reversible inter-orbit maps ⟹ **SD-FORCE FALSE**, self-duality
    is an irreducible import (deliver SD1–SD4). This is the rebit-analogue: a clean field-blind
    "level-2" witness.
  - **NO** — faithful self-modeling genuinely demands the reversible flow connect *any* two pure
    states (e.g. the model must be able to reversibly re-base on any state it represents), which
    Vinberg's group cannot do ⟹ **SD-FORCE TRUE**, self-duality is FORCED, Vinberg excluded by a
    principled dynamical obstruction (name it).

**The trap that makes it a rename (must be checked):** if "works from any state" is *defined* so
that it already means "reversibly inter-mappable," it IS pure-state-transitivity by another name
and the forcing is vacuous (CLAMP-rename). The proof of SD-FORCE TRUE is only real if "works from
any state" is justified from *faithful self-modeling* independently of inter-mappability, and the
transitivity is then **derived**. State precisely which independent property of self-modeling does
the work, and check Vinberg fails *that* property (not a relabeling of self-duality).

---

## 5. Relationship to the complex step (state this — it's the prize)

Both selectors are facets of ONE object, the reversible self-tracking flow:
- **self-dual** ⟸ the flow is **transitive** on pure states (this task);
- **complex** ⟸ the flow's **generator is an observable** (`⟦·,·⟧`-closure; field-blindness prompt).

Report which unification holds:
- If SD-FORCE TRUE: the Jordan step is forced; Paper 5 = 1 forcing (Jordan) + 1 import (complex).
- If SD-FORCE FALSE: state whether the two imports collapse into a **single** dynamical-relativity
  postulate ("the reversible self-tracking flow is transitive AND its generators are observable")
  that yields both self-dual and complex — i.e. whether P2 is "self-modeling + ONE postulate ⟹ QM"
  rather than two separate imports. (Even this is a postulate, not a forcing — label honestly.)

---

## 6. Guards (anti-glaze / anti-thrash)

- **The static route is dead — do NOT re-open it.** Vinberg ⊨ every static form (SD1 list). Any
  claim "static self-modeling property X forces self-duality" is FALSE (Vinberg ⊨ X). The only
  live content is the *dynamical* datum (§4).
- **No circular inputs.** Do not use self-duality, symmetric transition probabilities, K≅K*, a
  conjugate / conjugate-correlator (Wilce), or "states are effects" as a *premise* — those ARE
  self-duality. Allowed premises: Def-1, eq:sp-explicit, "a reversible self-tracking flow exists,"
  "faithful tracking works from any state," Stone, homogeneity (flagged per §2.3).
- **Verify, do not cite.** Re-confirm Vinberg ⊨ the core and its reversible-group orbit structure
  by explicit construction (Vinberg's 5-dim T-algebra cone; vdW §VII gives coordinates). Confirm
  the Barnum–Ududec–vdW statement you use actually says what you need (homogeneity +
  pure-state-transitivity ⟹ self-dual).
- **Exact arithmetic** for any concrete orbit / norm computation (ℚ / algebraic).
- **DEFLATION vs SURRENDER.** "SD-FORCE is FALSE, here is the separation theorem" is a real result
  IF backed by the Vinberg orbit computation showing non-transitive reversible self-tracking
  suffices. It is NOT a license to wave the joint away. Conversely, do not declare SD-FORCE TRUE on
  a "works from any state" premise that secretly = transitivity (CLAMP-rename) — the §4 trap.
- **Make-it-fit before dead.** Attempt §3′ (the forcing) first; only fall to §3 (separation) after
  the Vinberg decider in §4 shows a genuine non-transitive faithful self-tracking model.

---

## 7. Citations (verify each before relying on it)
- van de Wetering 2018, arXiv:1803.11139 (S1–S7 ⟺ EJA; S4 = symmetry of orthogonality; Vinberg in §VII).
- Barnum, Ududec, van de Wetering 2023, arXiv:2306.00362 (homogeneity + pure-state-transitivity ⟹ self-dual). **Verify.**
- Koecher–Vinberg theorem (homogeneous + self-dual ⟺ EJA); Faraut–Korányi, *Analysis on Symmetric Cones*.
- Vinberg 1960/63, the homogeneous non-self-dual T-algebra cone (coordinates via vdW §VII).
- Niestegge 2024, arXiv:2208.07135 (rank-2 ℓ⁴ qubit — the verified static non-self-dual witness).
- Wilce, conjugate-correlator / self-duality-from-conjugates (arXiv:1206.2897 — **verify number**; use only as the *circular-input* to avoid, per §6, unless deriving its hypothesis from self-modeling).
- Barnum–Hilgert 2019, arXiv:1904.03753 (spectral + strongly symmetric ⟺ Jordan).
- Paper under test: `landing/papers/qm-from-self-modeling/` — Def-1 at main.tex:357–376; recognition-symmetry / Niestegge cite at main.tex:734; prop:coherence.

---

## 8. Output
- A definite verdict on **CLAIM SD-FORCE: TRUE or FALSE.**
- The **Vinberg decider** (§4): its reversible-group orbit structure on pure states, and whether
  non-transitive faithful reversible self-tracking is genuinely possible — with the explicit
  construction or the explicit obstruction.
- If FALSE: the separation theorem **SD1–SD4**, stated precisely, with the SD1 static-graveyard list
  confirmed.
- If TRUE: the forcing proof (§3′), with the exact independent self-modeling property that does the
  work and the check that it is NOT a relabeling of self-duality (§4 trap cleared).
- The unification statement (§5): one forcing + one import, OR a single unified dynamical postulate.
- One-line honest SSOT status (expect: no flip — P5 stays CONDITIONAL-SYNTHESIS; this sharpens the
  Jordan step from "import" to either "forced" or "import with a precise dynamical separation").
