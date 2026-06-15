# Phase 95 / v35.0-candidate — THE AREA-PER-BIT KILL-TEST — VERDICT

> Driver: `code/area_per_bit.py` (commit `3af1080b`) → exit 0, 25/25 PASS, exact over ℚ, ~2.6 s.
> **MILESTONE HOLD for human ratification.** This file states the verdict, the mechanism, the bug-guard
> dispositions, the fences, the anti-overclaim, and the flagged items for the orchestrator/human.

---

## PRIMARY VERDICT: **DEAD-FISHER / fork A**

The variety (CP² = the C_u cut of OP², where v23's faithful-point fiber kill does not reach) does **NOT** natively
set a geometric bits↔area exchange rate. Its only Fubini–Study-canonical local matter-induced area is **identically
the quantum Fisher / QGT-real metric** `Var_p(M)` — a state-space information object (v17's corpse), not a spacetime
metric. The bits↔area rate (Ryu–Takayanagi's `G`) is therefore a **contingent import** ⇒ **fork A**, the honest-scope
TOE. This is the de-risked expected landing, reached rigorously (not assumed): the literal DEAD-CONSTANT reading
actually FAILS (R shears), but the shear is the Fisher-vs-relative-entropy disagreement, a state-space fact — the
DEAD-FISHER mechanism (Bug-guard 3) is the correct, sharper closure.

**This is a REAL result.** It **closes the entanglement route** — the sixth and last of the 2026-06-14 brainstorm's
gravity angles — through the most defensible identity available: *the variety's canonical "area" is literally the
bit-counter's own metric*. There is no independent geometric area to pair against the entropy. Same fork-A conclusion
family as v33 (extremize FORCES-NOTHING) and the v23 (∇S = 0) death, now reached one level sharper.

---

## THE MECHANISM (the FISHER-CORPSE, exact over ℚ)

Three symbolic identities (proven for ALL chart points `p` and ALL traceless cut matter `M`, via exact
polynomial-numerator comparison over ρ-powers — never a float, never a `cancel`-of-combined-fraction):

1. **The canonical area IS the Fisher metric.** Both FS-canonical, matter-functorial area candidates coincide and
   equal the quantum variance:
   ```
   A_M^(ii)  = g_pot^{a b̄} ∂_a φ_M ∂_{b̄} φ_M = |∇φ_M|²_g   ≡  Var_p(M)        (metric-trace area)
   A_M^(iii) = g_{a b̄} X^a conj(X)^{b̄},  X = J∇φ_M           ≡  Var_p(M)        (KKS symplectic, Kähler tie)
   ```
   By Provost–Vallée (1980), the Fubini–Study metric on pure states **is** the real part of the quantum geometric
   tensor = the quantum Fisher metric. So `A_M = Var = ` the quantum Fisher information of `φ_M` — a STATE-SPACE
   object, the same family as v17's dead real-QGT / cone-Hessian / Fisher metric.

2. **The entropy response is the Fisher information PLUS a non-proportional correction.** The v26 second-order
   relative-entropy Hessian decomposes exactly:
   ```
   G_M(p)  =  Var_p(M)  +  ¾⟨M⟩²_p  −  ½Tr(M²)          (symbolic identity, ≡ 0)
   ```
   So `G_M` is **NOT** ∝ `Var`. The "extra" piece `¾⟨M⟩² − ½Tr(M²)` is a state-space quantity (the relative-entropy
   curvature beyond Fisher), **not** geometry.

3. **Hence R shears — but the shear is state-space, not geometric.**
   ```
   R(p,M) = A_M / |G_M| = Var / |Var + ¾⟨M⟩² − ½Tr(M²)|
   ```
   `R` is NOT literally constant (exact §9 values 8/5, 2/13, 44/17, 4/3 vary by direction and point). But the
   numerator is the **Fisher information** and the denominator is the **relative-entropy Hessian** — both STATE-SPACE
   information measures. The shear is the (well-known) disagreement between two information metrics, **NOT a geometric
   bits↔area exchange rate.**

**Conclusion:** there is no native geometric area independent of the state-space information geometry to pair with the
bits ⇒ the variety sets no native geometric bits↔area rate ⇒ the rate is a contingent import ⇒ **fork A**. The
Fisher-corpse gate (Bug-guard 3) fires in G1 and the run STOPS before G2 (which is not reached and not expected).

**LIVE-TENSOR is killed — but by TT-being-Fisher, not by TT-absence (adversarial sharpening).** The metric-mode
`dφ_M ⊗ dφ_M` is rank-1 (`s⊗s` with `|s|²_g = Var`), so EVERY FS-canonical area invariant of it is a fixed power of
the Fisher variance: metric-trace `A_ii = Var`, full norm `‖dφ_M⊗dφ_M‖²_g = 4·Var²`, and the **transverse-traceless**
part `A_TT = ‖traceless part‖²_g = 3·Var²`. The TT channel is therefore PRESENT (not "structurally precluded"), but it
is itself a Fisher monomial — `R_TT = 3·Var²/|G_M|` shears only via the same Fisher-vs-relative-entropy state-space
mechanism, supplying NO independent geometric shearing rate. So even routing past the Fisher gate to G2, no canonical
area escapes the Fisher object: not LIVE-TENSOR, and no LIVE-SCALAR via an independent rate either.

---

## BUG-GUARD DISPOSITIONS

| # | Guard | Disposition |
|---|-------|-------------|
| 1 | AREA-RIG (≥2 canonical defs; flip ⇒ INCONCLUSIVE) | **CLEARED** — A_ii (metric-trace) ≡ A_iii (KKS symplectic) ≡ Var, symbolically. No flip. |
| 2 | CIRCULARITY (FS imported; no derived G) | **HONORED** — FS USED not derived; this DIAGNOSES native area↔entropy variation; records NO derived G. |
| 3 | FISHER-CORPSE (G_M is state-space; don't read shear as curvature) | **FIRES — DECISIVE** — the AREA too is the Fisher object (A_M ≡ Var); R = Fisher/(rel-entropy) ⇒ DEAD-FISHER. |
| 4 | CONSTANT-BY-SYMMETRY (confirm OFF I/3) | **CLEARED** — G_M(p) genuinely varies with p (G_M(P0)≠G_M(P2) all 4 dirs); ∇S_face ≠ 0; NOT vacuous (unlike v23). |
| 5 | NUMERIC LEAKAGE (exact over ℚ) | **HONORED** — every decisive line exact over ℚ/ℚ(i); no float in the verdict. |

**verdict() is NON-HARDWIRED** — the derived ladder returns 5 distinct verdicts under synthetic inputs
(rigged-constant→DEAD-CONSTANT, non-Fisher shear→LIVE-{TENSOR,SCALAR}, non-agreeing areas→INCONCLUSIVE, A=Var→
DEAD-FISHER); the branch is forced by the computed booleans, proven by the self-tests (all PASS before the real verdict).

---

## FENCES (binding, verbatim — RESEARCH §6)

NO Einstein-equation / G=κT / gravity / Newton / dark-matter / geodesic language as a DERIVED result; the bits↔area
rate is a framework ratio (a contingent import like κ, Λ unless G1 forces otherwise), **NOT Newton's G**; FS is USED,
not derived; signature **Riemannian** (Wall 2 unpaid — NOTHING is called gravity until signature is paid);
DEAD-CONSTANT / DEAD-FISHER and LIVE-\* are NOT derivations of gravity. This run does NOT retract v33 (extremize
FORCES-NOTHING), v34 (induce CLOSES-CONDITIONAL), v17–v21 (fiber kills), or v23 (I/3 death). **Paper 5 remains the
only result in the more-than-nothing column.**

## ANTI-OVERCLAIM (verbatim — RESEARCH §7, Jaksland arXiv:2005.05055)

LIVE (either) = the variety sets a non-constant exchange rate — NECESSARY, not sufficient, for gravity; it is the
area-side diagnostic of the entanglement route, UPSTREAM of the clamp (state-fp ⟹ metric-fp). Even LIVE-TENSOR shows
native area↔entropy variation, NOT that the metric obeys a field equation. A generic Jacobson/RT recovery validates
nothing program-specific — the originality is whether the variety FORCES the rate, not that an area law exists.
DEAD (CONSTANT or FISHER) is the expected and honest outcome; it closes the entanglement route and is the green light
for fork A. Holography is theorem-blocked natively (h₃(O) is finite Type-I₃ by Zelmanov; the "Area/4G from an algebra"
result CPW arXiv:2302.01938 needs a Type III₁ factor the exceptional algebra cannot have). The program has the
Bekenstein BOUND (S ≤ Area, G-free) but NOT the RT EQUALITY (Area = 4G·S, G-valued); the G-valued equality is the
unpaid step = the clamp.

---

## THROUGH-LINE

v24 entropy landscape (LIVE) → v25 moment doublet (X,X#) → v26 source field G_M + MaxEnt → v27 local balance →
v28 spinor moment → v29/v30 clock sector closes → v31 tensor wall OPENS → v32 tensor dictionary (κ=1/30, ε=20) →
v33 EXTREMIZE forces nothing → v34 INDUCE CLOSES-CONDITIONAL (gravity gap = the single state-fp⟹metric-fp clamp) →
**v35 AREA-PER-BIT: DEAD-FISHER / fork A** — the canonical area IS the QGT/Fisher corpse, so there is no native
geometric rate; closes the entanglement route, the sixth brainstorm angle reducing to the one clamp. Every gravity
angle now points at the same single unpaid step (the G-valued RT equality = the clamp).

---

## FLAGGED ITEMS for the orchestrator / human (ratification + downstream verification)

1. **DEVIATION from RESEARCH §3 (denominator-zero locus), non-blocking, physics unchanged.** The §3 guard says
   "G_M → 0 near the **vertex** E_11"; the exact computation shows the genuine `G_M = 0` locus for the rank-2
   directions is the **EQUATOR** (e.g. z₁=±1, z₂=0 for d1, where the (1,2)-block face is maximally mixed). At the
   vertex z=0 it is the **numerator** `Var` that vanishes (E_11 is a d1-eigenstate) while `G_M = −1/4` stays finite.
   Both loci are non-shears (reciprocal |G|/A = 0 finite at the equator; R = 0 at the vertex); the driver tests the
   corrected (exact) facts. The verdict and all §9 numbers are unaffected. **RESOLVED at ratification (2026-06-15):
   RESEARCH §3 wording corrected from "vertex" to "equator".**

2. **DEVIATION on conjugation (latent bug fix), non-blocking, identity holds.** The prompt instructs "use a z↔z̄ swap
   (NEVER sympy conjugate())". The swap ALONE gives A_iii ≠ Var; the **full** complex conjugation = z↔z̄ swap **AND**
   i→−i is required for A_iii ≡ Var. The i→−i flip acts on the genuine imaginary unit (from the matter Hermitian
   off-diagonals and the J-factor i), which is legitimate complex conjugation of a true constant — it is NOT applying
   sympy `conjugate()` to the independent Wirtinger z symbols (which remains banned and is not done). Flagging so the
   independent verifier expects the i→−i piece in the KKS construction.

3. **Metric normalization pinned (non-blocking).** A_ii ≡ Var requires the **potential / Fisher** FS normalization
   `g_pot = ∂∂̄ log ρ = Re(QGT)`; the certified engine metric `g_phys = g_pot/2` gives `A_ii(phys) ≡ 2·Var`. Both are
   reported; the overall scale is the single one G1 allows to normalize away and does NOT affect the verdict (R = A/|G|
   rescales uniformly). The Fisher identification (the whole DEAD-FISHER mechanism) is scale-independent.

4. **Independent-path confirmation (strengthens, not blocks).** All 6 RESEARCH §9 rows were reproduced by a SECOND,
   independent code path (a from-scratch numeric projector using `sympy.conjugate` on the concrete complex chart
   points — distinct from the Wirtinger-symbol chart). The two implementations agree exactly on every decisive
   R-value. The orchestrator's triple-path plan (independent verifier on a separate code path + adversarial) can build
   on this.

5. **Interpretive confidence MEDIUM on the one leap.** The math (A_M ≡ the Fisher metric; G_M = Fisher + correction;
   R shears state-space-only) is exact and HIGH-confidence. The single interpretive step — "a Fisher-object area
   certifies that R's shear is NOT a geometric rate" — rests on the cited Provost–Vallée FS = Re(QGT) identification
   and the program's own pre-registered Fence 3 / Bug-guard 3. It is the de-risked, pre-registered expected landing;
   flagged MEDIUM only because it is interpretive rather than purely computational.

6. **MILESTONE RATIFIED 2026-06-15 (Bryan)** — see the seal below; recorded by hand (state.json / MILESTONES /
   PROJECT / STATE + memory, mirroring v34); did NOT run `gpd phase complete` / `state advance` /
   `complete-milestone`; the next slot is NOT self-registered.

---

## QUAD-PATH VERIFICATION SEAL + RATIFICATION (2026-06-15)

**VERDICT RATIFIED: DEAD-FISHER / fork A — HIGH (math) / MEDIUM-accepted (the one interpretive step).** Bryan's
ratification note: the MEDIUM interpretive step is *robust because even a generous LIVE reading routes to the clamp
via the anti-overclaim fence* (LIVE is necessary-not-sufficient, upstream of the state-fp⟹metric-fp clamp), so the
verdict's downstream meaning (fork A / the clamp is the sole remaining gravity question) does not depend on resolving
the leap either way.

**The four independent paths, all agreeing:**
1. **Orchestrator de-risk** (exact over ℚ): established A_ii ≡ Var, G_M = Var + ¾⟨M⟩² − ½TrM² before any agent ran.
2. **Executor** (`code/area_per_bit.py`, `3af1080b`): 25/25 PASS, exact over ℚ, non-hardwired verdict() + 5 self-tests.
3. **Independent verifier** (`95-VERIFICATION.md`, `599eed9e`): fresh engine, 5/5 charges PASS, HIGH; A_ii ≡ Var
   re-derived a THIRD chart-free way via ⟨ψ|M(1−P)M|ψ⟩ = Var; off-faithfulness CLEARED (not the v23 I/3 death);
   Provost–Vallée FS = Re(QGT) = quantum Fisher metric anchor verified.
4. **Adversarial AREA-RIG** (`95-ADVERSARIAL-CHECK.md`, `599eed9e`): the attack FAILED to overturn and STRENGTHENED
   the verdict — tested the TT-mode and symplectic candidates the executor had only asserted away, and found EVERY
   FS-canonical area of the rank-1 mode is a Var power (A_ii = Var, A_TT = 3·Var², A_full = 4·Var²). Not LIVE-TENSOR
   (TT present but Fisher), not INCONCLUSIVE (no flip — all defs the same Fisher object up to a constant/power).

**Three corrections baked in at ratification (per Bryan):**
- The TT channel is **PRESENT and = 3·Var²** (a Fisher monomial), **NOT "structurally precluded"** — the adversarial's
  sharpening; LIVE-TENSOR is killed by TT-being-Fisher, a stronger kill than TT-absence (corrected throughout this
  doc, the SUMMARY, and RESEARCH §3).
- RESEARCH §3 denominator-zero wording corrected: the rank-2 `G_M = 0` locus is the **EQUATOR** (z₁=±1, z₂=0), not the
  vertex (at the vertex it is the numerator Var that vanishes).
- The two stray untracked files the adversarial left (`code/lichnerowicz_response_adversarial.py` duplicate + a `.pkl`
  cache) deleted.
