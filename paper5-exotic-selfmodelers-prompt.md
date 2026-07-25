# Paper 5 — The Exotic Self-Modelers (arm the "not like us" bracket; settle whether the non-Jordan ones are dynamically FROZEN)

## TASK TYPE
Settle ONE specific claim (**CLAIM FROZEN-UNIVERSAL** below), prove-or-disprove, exact/ℚ, with a
decision tree — AND, as a secondary deliverable, verify/sharpen the "rogues' gallery" of concrete,
non-circular physical reasons each non-quantum self-model is **not a physical self-modeler like us**.

This is NOT a forcing task. We are NOT trying to prove self-modeling forces Jordan/complex — that is
**settled FALSE** by explicit models (rebit `M_n(ℝ)`, Vinberg cone, Niestegge ℓ⁴ qubit all ⊨ Def-1;
verified prior sessions, exact/ℚ). The final paper's chosen frame is **bracketing, not selection**:
present the spine to complex QM, then acknowledge the non-quantum self-models exist and **bracket
them as physically exotic / inaccessible in a universe like ours, each for a concrete reason**. This
GPD's job is to **arm that bracket** with true, non-circular, physically meaningful reasons — and in
particular to decide whether the strongest available reason on the Jordan side ("dynamically
frozen") is **universal** or only holds for the minimal cone.

---

## 0. The claims to settle

> **CLAIM FROZEN-UNIVERSAL.** Every non-self-dual homogeneous cone has a **reversible** automorphism
> group (the subgroup of `Aut(K)` preserving the normalized state space — equivalently the maximal
> compact subgroup / the order-automorphisms fixing the order unit and its dual) whose **identity
> component is trivial**: the reversible group is finite/discrete. I.e. a non-Jordan self-model is
> **dynamically frozen** — it carries **no continuous reversible flow** at all.
>
> Contrapositive form (what to disprove): *any homogeneous cone carrying a positive-dimensional
> reversible automorphism group is self-dual.*

- **TRUE** ⟹ the non-Jordan self-models cannot support continuous reversible time evolution. The
  Jordan-side bracket is the punchy one: *"a universe like ours has continuous reversible dynamics
  (a Hamiltonian flow); these self-models provably cannot, so they are not physical."*
- **FALSE** ⟹ exhibit a non-self-dual homogeneous cone with a continuous (positive-dim) reversible
  flow (candidate: a **complex/quaternionic-Hermitian sparsity-pattern cone**, §4). Then the
  Jordan-side bracket falls back to the **GUARANTEED FLOOR** below — still a clean, true reason,
  just less punchy.

> **THE FREE FLOOR (already a theorem — verify, do not re-derive).** By Barnum–Ududec–van de
> Wetering (homogeneity + pure-state-transitivity ⟹ self-dual), the contrapositive gives: **every
> non-self-dual homogeneous cone has a reversible group that is NOT transitive on its pure states.**
> So *unconditionally*, every non-Jordan self-model has **dynamically preferred states** — pairs of
> its own pure states that no reversible evolution of it can ever connect. That is a true,
> non-circular, program-native bracket on its own ("Radical Relativity: a relativistic self-modeler
> has no dynamically preferred state; these do"). FROZEN-UNIVERSAL only upgrades it from "has
> preferred states" to "has no dynamics at all."

So the bracket frame **works regardless of the verdict.** FROZEN-UNIVERSAL decides only its strength
on the Jordan side. Report the verdict AND confirm the floor.

---

## 1. Why this is the question (context — read once)

Spine: `self-modeling → loop builds eq:sp-explicit → S1–S7 → [vdW Thm 1] EJA → [self-duality/S4] →
[central-i / local tomography] complex M_n(ℂ)`. Two selectors (self-duality → Jordan; central-i/LT →
complex), both proven irreducible by explicit models ⟹ as-stated Paper 5 is a two-import synthesis.

**The final paper will not call these "selections."** It will study physical self-modelers, derive
that they are complex QM, and then run a short "exotic self-modelers" section: *yes, non-complex /
non-Jordan self-models exist as order-unit spaces; here is precisely why each is not a physical
self-modeler in a universe like ours; we set them aside.* The whole game is that **each "why" is a
concrete physical property the exotic model LACKS — never "it's uninteresting" and never "because
it's not quantum" (circular).** This GPD supplies and stress-tests those properties.

The deepest under-verified reason is on the Jordan side. §16 (anchor `paper5-virtuous-loop-three-
joints.md`) found the **minimal** 5-dim Vinberg cone is dynamically frozen (reversible isotropy Lie
algebra = 0, finite order 8, exact/ℚ `sd_separation.py`) — but asserted, without building it,
whether higher-dim non-self-dual homogeneous cones are also frozen or carry continuous reversible
flows. That single unbuilt fact is CLAIM FROZEN-UNIVERSAL.

---

## 2. The objects (self-contained — do not conflate these three groups)

For a finite-dim cone `K` (interior = states):
- **Full automorphism group `Aut(K)`** = linear maps preserving `K`. **Homogeneous** = `Aut(K)`
  transitive on the **interior**. NB these maps include NON-compact, non-state-preserving ones
  (scalings, shears) — the minimal Vinberg cone is homogeneous via 3 scalings + 2 shears, **zero
  antisymmetric/compact generators**.
- **Reversible group** = the subgroup preserving the **normalized state space** (fixing the order
  unit `e` and the unit effect) = the maximal compact subgroup of `Aut(K)`. These are the
  "physical symmetries" / the analogue of unitaries. **"Dynamically frozen" = this group's identity
  component is trivial** (no continuous reversible one-parameter flow `e^{tD}`).
- **Pure-state-transitivity** = the reversible group acts transitively on the extreme rays
  (pure states). Quantum: `U(n)` on the Bloch sphere. **Self-dual ⟺ reversible-pure-state-transitive,
  given homogeneity** (Barnum–Ududec–vdW + Koecher–Vinberg).

THE FULCRUM (state it, do not blur): homogeneity (full group, non-compact, interior-transitive) is
**not** reversible-pure-state-transitivity (compact group, pure-states). A non-self-dual homogeneous
cone has the first, lacks the second. "Frozen" is the strongest possible failure of the second (the
compact group is not just non-transitive, it's discrete). The minimal Vinberg cone is frozen;
FROZEN-UNIVERSAL asks if all non-self-dual homogeneous cones are.

Why "frozen" is the physical bracket: a continuous reversible flow `e^{tD}` is exactly a
Hamiltonian/Schrödinger-type time evolution by state-preserving symmetries. A frozen self-model has
**none** — it has no continuous reversible time evolution whatsoever (only discrete symmetries and
non-reversible distortions). A universe like ours manifestly has continuous reversible dynamics.

---

## 3. Deliverables

### 3A. Primary — the FROZEN-UNIVERSAL verdict (the §4 computation)
Definite TRUE/FALSE with the explicit construction or the explicit obstruction, exact/ℚ.

### 3B. Secondary — the rogues' gallery (verify each reason; flag any that is circular or false)
For each non-quantum simple self-model, give the **one strongest concrete, non-circular physical
property it lacks** vs. a physical self-modeler. Confirm or correct this starting table:

| Exotic self-model | The bracket: "not like us because…" | Source to verify |
|---|---|---|
| Real `M_n(ℝ)` (rebit) | its reversible generators `so(n)` are **not observables** — no measurable energy/Hamiltonian (`⟦a,b⟧=−i[a,b]∉V`); and its body–model composite is **not locally tomographic** (`9<10`: an entangled sector of itself it cannot resolve by product measurements) | field-blindness sep. §13; Barnum–Wilce; `field_blindness.py` |
| Quaternionic `M_n(ℍ)` | its composite has **fewer** dimensions than `d²` — product effects are linearly dependent, so it **over-counts** its own joint states | type-exclusion.tex; Barnum–Wilce |
| Spin factor `V_n` (n≥4, n≠5) | **no locally tomographic composite** (rank-doubling forces dims 10/16/28; only 16 is a square ⇒ only `V_3=M_2(ℂ)`) | type-exclusion.tex; vdW Prop 39–40 |
| Albert `M_3(𝕆)` | **no consistent composite exists at all** — it cannot form a body–model pair with anything non-classical, so it cannot even self-model in the composite sense | BGW arXiv:2009.xxxxx (verify); type-exclusion.tex |
| Niestegge ℓ⁴ rank-2 qubit | **asymmetric recognition / non-symmetric transition** (`R(p,q)≠R(q,p)`, `3/4≠9/16`) — "seeing A from B" differs from "B from A": a built-in preferred direction | Niestegge 2024 arXiv:2208.07135; `joint1_jordan.py` |
| Vinberg / non-Jordan homogeneous | **dynamically preferred states** (reversible flow not pure-state-transitive) [FLOOR, guaranteed]; and possibly **dynamically frozen** (no continuous reversible dynamics) [iff FROZEN-UNIVERSAL] | this GPD §4; BUvdW arXiv:2306.00362 |

Each reason must be **non-circular** (does NOT use "because it isn't complex/Jordan/quantum") and
**true** (verify by computation or primary source). Kill or fix any row that fails either test.

---

## 4. The decider (the actual computation — exact/ℚ)

**Goal:** find a non-self-dual homogeneous cone with **positive-dimensional reversible isotropy**, or
prove none exists.

1. **Reconfirm the minimal Vinberg cone is frozen** (sanity, exact/ℚ): `P={sym 3×3, (2,3)≡0}`,
   reversible isotropy Lie algebra = 0 (the §16 / `sd_separation.py` result). This is the dim-5,
   rank-3 base case.

2. **Build candidate non-frozen witnesses.** The natural place continuous reversible symmetry
   survives a self-duality-breaking pattern is a **complex- or quaternionic-Hermitian sparsity-
   pattern cone**:
   - Candidate C: `K = {3×3 complex-Hermitian PSD matrices with the (1,3),(3,1) entry ≡ 0}` (path
     graph 1–2–3 over ℂ). Sparsity-pattern cones on chordal graphs are homogeneous (verify, Ishi /
     Letac–Massam / Andersson). Compute (a) is it **self-dual**? (the zeroed pattern should break it,
     as in the real case); (b) its **reversible isotropy Lie algebra** — the surviving off-diagonal
     **phase rotations `U(1)`** on the (1,2) and (2,3) blocks should give **positive-dimensional**
     compact isotropy. If non-self-dual AND positive-dim reversible isotropy ⟹ **FROZEN-UNIVERSAL
     FALSE**, witness in hand.
   - Candidate Q: the quaternionic analogue (gives `Sp(1)` phases) if C is inconclusive.
   - Candidate R+: a higher-rank real pattern containing a full symmetric 2×2 block "rotatable" by
     an `SO(2)` while an asymmetric coupling elsewhere breaks self-duality.

   For each: compute reversible isotropy = `{X : XᵀG+GX state-preserving, pattern-preserving}` Lie
   algebra dimension, and non-self-duality (exhibit `B ∈ K*∖K`, e.g. a PSD-completable pattern
   matrix that is not itself PSD, with an exact negative eigenvalue / `det<0`). All exact/ℚ (or
   ℚ(i)/ℚ-quaternion).

3. **If every candidate is self-dual or frozen**, attempt the no-go: for a homogeneous cone, the
   compact part of `Aut(K)` is contained in the reductive Levi factor of the Vinberg T-algebra
   structure; argue (or find in Vinberg 1963 / Ishi) that a positive-dim compact factor forces the
   T-algebra structure constants symmetric ⟹ self-dual. State precisely which structural fact does
   the work; verify it, do not hand-wave.

**Prior (do not let it bias the computation):** non-frozen non-self-dual homogeneous cones are
**expected to exist** (continuous phase symmetries survive pattern-breaking in the complex/
quaternionic cases), so FROZEN-UNIVERSAL is **expected FALSE** — in which case the honest, still-
good bracket is the FLOOR ("dynamically preferred states / non-relativistic"), and you should say so
without strain. Do NOT manufacture a frozen-universal proof to get the punchier headline.

---

## 5. Guards (anti-glaze / anti-thrash / anti-woo)

- **"Not interesting" is NOT a reason.** Every bracket must be a concrete physical/dynamical property
  the exotic model **lacks** (no continuous reversible flow; generators not observable; no locally
  tomographic composite; no composite at all; asymmetric recognition; dynamically preferred states).
  Aesthetic dismissal ("weird," "pathological," "uninteresting") is woo here — reject it.
- **No circular brackets.** A reason may not be "because it is not complex/Jordan/quantum," nor any
  restatement of self-duality / local tomography / central-i as the *reason* (those are the
  conclusion). The reason must be statable **pre-quantumly**, about the cone and its automorphism
  group. (Frozen-ness, observability of generators, composite dimension counts, transition symmetry
  all qualify; "it isn't self-dual" does not.)
- **Verify, do not cite.** Reconfirm the minimal-cone frozen result by construction; confirm the
  BUvdW statement (homogeneity + pure-state-transitivity ⟹ self-dual) says what the FLOOR needs;
  confirm any sparsity-pattern-cone homogeneity claim from a primary source before relying on it.
- **Exact arithmetic** (ℚ / ℚ(i) / algebraic) for every isotropy-dimension, determinant, eigenvalue,
  and dual-cone-membership computation. Hand-derive at least the load-bearing numbers.
- **DEFLATION vs SURRENDER.** "FROZEN-UNIVERSAL is FALSE, the bracket is the FLOOR" is a real,
  publishable result — it is NOT waving the joint away, because the FLOOR is a theorem and the
  witness is explicit. Conversely do not over-claim FROZEN-UNIVERSAL TRUE on an incomplete search;
  TRUE requires the structural no-go of §4.3, not just "I didn't find one."
- **This does not change Paper 5's status.** Expect: no SSOT flip (P5 stays CONDITIONAL-SYNTHESIS);
  this sharpens the *exposition* of the exotic-bracket section, and pins how strong the Jordan-side
  bracket is.

---

## 6. Citations (verify each before relying on it)
- Barnum, Ududec, van de Wetering 2023, arXiv:2306.00362 — homogeneity + pure-state-transitivity ⟹
  self-dual (Thm 2; Cor 3/4 sharpenings). **The FLOOR depends on this; verify the exact statement.**
- van de Wetering 2018, arXiv:1803.11139 — S1–S7 ⟺ EJA; Vinberg cone in §VII; Prop 39–40 (spin
  factor rank-doubling dimension count).
- Vinberg 1960/63 — homogeneous cones, T-algebras, the structure of `Aut(K)` (Levi + solvable).
- Ishi (e.g. arXiv:1207.xxxx / 2012.12131 with Koufany) and Letac–Massam / Andersson–Wojnar —
  homogeneous cones as sparsity-pattern cones on (homogeneous) chordal graphs; isotropy structure.
- Koecher–Vinberg; Faraut–Korányi, *Analysis on Symmetric Cones* (symmetric ⟺ homogeneous + self-dual).
- Niestegge 2024, arXiv:2208.07135 — rank-2 ℓ⁴ qubit (the verified non-symmetric-transition witness).
- Barnum–Wilce 2014; Barnum–Graydon–Wilce — composite/local-tomography dimension facts and the
  no-composite result for the Albert algebra (verify the BGW number).
- Paper under test: `landing/papers/qm-from-self-modeling/` — Def-1 main.tex:357–376; the Vinberg
  remark main.tex:728–734; type-exclusion.tex (the gallery of dimension exclusions).
- Anchor: `research/paper5-virtuous-loop-three-joints.md` §16 (minimal-cone frozen result, exact/ℚ).

---

## 7. Output
- **CLAIM FROZEN-UNIVERSAL: TRUE or FALSE**, with the §4 computation (the explicit non-frozen
  non-self-dual witness with its reversible isotropy dimension + non-self-duality certificate, OR
  the structural no-go), exact/ℚ.
- **Confirmation of the FREE FLOOR** (every non-self-dual homogeneous cone has dynamically preferred
  states), with the verified BUvdW statement it rests on.
- **The rogues' gallery (3B)**: the corrected/verified table of one concrete non-circular physical
  bracket per exotic self-model, each checked true and non-circular; kill or fix any bad row.
- **One-line honest SSOT status** (expect no flip; this sharpens the exotic-bracket exposition and
  fixes the strength of the Jordan-side reason).
