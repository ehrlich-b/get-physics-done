# GPD Milestone: The Paper 5 Recognition-Symmetry Theorem (self-duality / S4 is the real Jordan-selecter)

**Is Paper 5's "self-modeling -> complex QM" a DERIVATION or a CONDITIONAL SYNTHESIS? It
comes down to ONE axiom — and it is NOT positivity.** Prove or disprove a single claim
about whether *symmetry of the recognition functional* forces self-duality on a homogeneous
spectral GPT.

Written 2026-06-23. SUPERSEDES the framing of `paper5-cone-freeness-prompt.md`: a
literature-verification pass (van de Wetering 2019 §VII; Barnum-Ududec-van de Wetering 2023)
established that **positivity/cone-preservation does NOT force Jordan and never could** —
vdW's own Vinberg-T-algebra product is positive, total, associative-on-compatibles, and
homogeneous, yet not self-dual, hence not Jordan. So the cone-freeness fight was about the
wrong axiom. The Jordan-selecting content is concentrated in ONE thin axiom: **S4
(orthosymmetry), equivalently SELF-DUALITY, equivalently SYMMETRY OF TRANSITION /
RECOGNITION PROBABILITIES.** This prompt isolates that joint and asks whether the program's
own foundational axiom (relativity-of-isomorphism) can force it non-circularly.

Self-contained: all definitions are inline. Live paper source is
`~/repos/blog/landing/papers/qm-from-self-modeling/`.

---

## Why this is now the whole ballgame

Paper 5's chain is: self-modeling -> a (total, positive) sequential product on a spectral
order-unit space -> (van de Wetering Thm 1) Euclidean Jordan algebra (EJA) -> [imported
local tomography] complex type -> C* -> complex QM. Koecher-Vinberg factors the EJA step:

> **(Koecher-Vinberg).** A finite-dim cone is the cone of a Euclidean Jordan algebra IFF it
> is **homogeneous** (its linear automorphism group acts transitively on the interior) AND
> **self-dual** (V_+ = V_+^* under some inner product).

The two conditions split cleanly across the operational reading of self-modeling:

- **HOMOGENEITY is (largely) FREE.** Under the operational reading the sequential product is
  the actual physical "do `a` then `b`" operation, so cone-preservation (positivity) is
  automatic — a real operation maps states to states. Positivity + S5 (associativity on
  compatibles) yields homogeneity via the Kadison spectral theorem and the `L_a`-invertibility
  argument (`a^{-1}·(a·b) = (a^{-1}·a)·b = b` makes left multiplication an order-iso). This is
  half of Jordan, and it is cheap.
- **SELF-DUALITY is the ENTIRE remaining gap, and it is NOT free.** vdW 2019 §VII: there is a
  positive, total, S1-S3/S5/S7-satisfying, homogeneous product (built from a Vinberg
  T-algebra on any non-symmetric homogeneous cone) that is **not self-dual**, hence not
  Jordan. Self-duality rides specifically on **S4** (`a·b = 0 ⟹ b·a = 0`, orthogonality is
  symmetric), whose content is **symmetry of transition probabilities** `ω_p(q) = ω_q(p)`
  (route: S4 -> rank-2 strict convexity -> spin factors -> symmetric transition form ->
  self-dualizing inner product). Independently: Barnum-Ududec-van de Wetering 2023 (Thm 2),
  homogeneity + **pure transitivity** -> self-dual, with self-duality the *derived*
  conclusion.

THE PROGRAM REDUCTION (why this is the recovery's heart): a transition probability `ω_p(q)`
is the degree to which state `p` reads as state `q` — a **degree of isomorphism**. The
program's foundational axiom (relativity-of-isomorphism, core-insight #2/#3: isomorphic
structures are identical) makes the isomorphism relation **symmetric** — it is an
equivalence relation, an *unordered* relation on the pair `{p,q}`. So `ω_p(q) = ω_q(p)` is
relativity-of-isomorphism applied to states. The self-modeler recognizes states by
isomorphism-comparison; faithfulness ties that recognition to the substrate's transition
probabilities; therefore the substrate is self-dual. The Jordan-selecting axiom is the
program's own core axiom in operational clothing — "you can't NOT select Jordan," because
not selecting it makes recognition asymmetric, contradicting relativity-of-isomorphism.

**This prompt's job is to decide whether that reduction is a FIT (non-circular, the program
axiom does real work) or a CLAMP (recognition-symmetry secretly = self-duality posited by
fiat = assuming Jordan).** GPD settles the MATH scaffolding (A/B/C below). The metaphysical
bridge ("self-modeling MANDATES symmetric recognition") is a labeled `[STRUCTURAL-
CORRESPONDENCE]` for the paper, NOT a GPD task — but GPD decides whether the math leaves
ROOM for it to be non-circular and non-vacuous.

## The claim to PROVE or DISPROVE

Setup. Let `V` be a finite-dim **homogeneous spectral** order-unit space `(V, ≤, 𝟙)`
equipped with a **total positive sequential product** `(·)` satisfying van de Wetering's
S1-S3, S5-S7 but **NOT assuming S4 / self-duality**. (Such `V` exist and are non-Jordan: the
Vinberg-T-algebra products of vdW 2019 §VII over a non-symmetric homogeneous cone.) The
**repeatable tests** are the idempotents `e·e = e` = the projective units `Proj(V)`; the
**atoms** are the minimal projective units (associated to pure states). For pure states
`p,q` with atoms `e_p, e_q`, define the **recognition functional**
>     `R(p,q) := e_p(q)`   (the probability that a system prepared in `q` passes the test "are you `p`?").

Prove or disprove the three linked parts; the run cannot come back empty (each routes to a
decision-relevant verdict).

> **(A) SUFFICIENCY.** If `R` is symmetric — `R(p,q) = R(q,p)` for all pure `p,q` — then `V`
> is self-dual, hence (with the assumed homogeneity, by Koecher-Vinberg) a Euclidean Jordan
> algebra. [Expected PROVE, via the symmetric transition form self-dualizing the cone;
> prove it IN THIS SETTING, do not merely cite.]
>
> **(B) NON-REDUNDANCY.** `R` symmetric is NOT automatic from homogeneity + spectrality +
> the total positive sequential product (S1-S3, S5-S7). Exhibit a concrete finite-dim such
> `V` on which `R` is **ASYMMETRIC** (`R(p,q) ≠ R(q,p)` for some pure `p,q`), with the
> asymmetry computed EXACTLY (rational/closed form). [Expected DISPROVE-of-automatic = a
> Vinberg witness. If instead symmetry turns out automatic, that CONTRADICTS vdW §VII and
> would itself be a major finding — flag loudly.]
>
> **(C) FIT-vs-CLAMP CLASSIFICATION.** Is the condition "`R` symmetric" (i) STRICTLY WEAKER
> than / independently stateable from "self-dual" — an order-theoretic condition on the
> recognition functional that *implies* self-duality given homogeneity but is not a verbatim
> restatement — or (ii) LOGICALLY EQUIVALENT to "self-dual" as stated (so that imposing it
> IS imposing self-duality)? Decide which, and identify the minimal extra structure (if any)
> needed to state `R`-symmetry without already invoking a self-dualizing inner product.

## The decision fork (what each verdict means for Paper 5)

1. **(A) PROVE + (B) asymmetric-Vinberg-witness + (C-i) strictly-weaker:** the recovery has
   a REAL, NON-CIRCULAR target. Self-modeling must justify exactly ONE thing —
   "recognition is symmetric" — a condition (i) weaker than Jordan, (ii) violated by generic
   non-Jordan GPTs (so the program axiom does real selection work), and (iii) independently
   motivated by relativity-of-isomorphism (isomorphism is an unordered relation). Then Paper
   5 becomes: "GIVEN relativity-of-isomorphism, self-modeling forces complex QM," every other
   step a theorem — a strong result conditional on ONE grounded, program-native, non-vacuous
   axiom (NOT an arbitrary technical import). Paper 5's Lean self-duality assumption
   downgrades to "follows from recognition-symmetry."

2. **(A) PROVE + (B) witness + (C-ii) equivalent:** honest CLAMP. "Recognition symmetric" is
   self-duality reworded; positing it = positing Jordan. The self-modeling argument for it is
   interpretive only. Paper 5 = Level-2 conditional synthesis with the assumption renamed
   positivity -> self-duality -> recognition-symmetry. Still true, still publishable,
   narrower. (Note: even here the bridge is non-circular IF its motivation — isomorphism is
   unordered — does not itself route through Jordan; (C-ii) makes the math equivalence
   verbatim but does not by itself make the *argument* circular. Distinguish the two.)

3. **(A) DISPROVE** (symmetric `R` does NOT force self-duality even given homogeneity): the
   whole reduction fails; recognition-symmetry is necessary-not-sufficient and there is a
   further hidden Jordan-selector. Identify it. (Low prior given Koecher-Vinberg + BUvdW
   2023, but check — e.g. a homogeneous non-self-dual cone with symmetric atom-transition but
   asymmetric higher structure.)

## Inline definitions (authoritative; use these)

**Homogeneous cone.** `V_+` is homogeneous if `Aut(V_+) = {g ∈ GL(V) : g V_+ = V_+}` acts
transitively on the interior `int(V_+)`. [Operational gloss: no preferred state; any
strictly positive state maps to any other by a cone-automorphism.]

**Self-dual cone.** There is an inner product `⟨·,·⟩` with
`V_+ = V_+^* := {y : ⟨y,x⟩ ≥ 0 ∀ x ∈ V_+}`. Equivalently states and effects are identified.

**Spectral order-unit space (finite-dim).** Each `a ∈ V` has a spectral resolution
`a = Σ_i λ_i p_i` into mutually orthogonal projective units `p_i` (`Σ p_i = 𝟙`, real `λ_i`),
with functional calculus (so `√a = Σ_i √λ_i p_i` for `a ≥ 0`). [Alfsen-Shultz 2003, Ch. 8.]

**Sequential product axioms (van de Wetering, Def. 2).** Binary `(·)` on effects `[0,𝟙]_V`,
with `a~b` ("compatible") meaning `a·b = b·a`: S1 additivity (`a·(b+c)=a·b+a·c`); S2
norm-continuity of `a ↦ a·b`; S3 unitality (`𝟙·a=a`); **S4 orthosymmetry (`a·b=0 ⟹
b·a=0`)** — THE axiom at issue; S5 associativity on compatibles (`a~b ⟹ a·(b·c)=(a·b)·c`);
S6/S7 compatibility additivity/multiplicativity. "Total" = defined on ALL pairs. "Positive"
= maps effects to effects (cone-preserving). vdW minimal rank-2 set is {S1,S3,S5,S6}; S7 is
redundant (Prop. 47). [vdW 2019, arXiv:1803.11139.]

**van de Wetering Thm 1.** A finite-dim total positive sequential product satisfying S1-S7
is the s.a. part of a Euclidean Jordan algebra with `a·b = √a·b·√a`. [arXiv:1803.11139.]
**vdW 2019 §VII (the counterexample to use/adapt for B):** on any non-symmetric homogeneous
cone there is a Vinberg-T-algebra product satisfying S1-S3,S5,S7 — positive, total,
associative, homogeneous — that FAILS S4/S6 and is NOT self-dual / NOT Jordan.

**Barnum-Ududec-van de Wetering 2023 (Thm 2).** Homogeneity + pure transitivity -> self-dual
(self-duality derived). [arXiv:2306.00362.] **Niestegge 2012** (arXiv:0912.0203): total
positive conditioning is necessary-not-sufficient for Jordan; the load-bearing extra is
no-third-order-interference (an S4 analogue). **Janotta-Lal 2013** (PRA 87 052131,
arXiv:1302.2632): regular-polygon GPTs — odd `n` strongly self-dual, even `n` not; `n=4` is
box-world (not self-dual) — a non-Jordan witness family adjacent to B.

**Generalized no-broadcasting (context, GIVEN — not the task).** Barnum-Barrett-Leifer-Wilce,
PRL 99, 240501 (2007): a finite-dim GPT permits broadcasting iff classical (a simplex). With
relativity-of-isomorphism ("no distinct perfect copies") this forces the self-modeler's
state space NON-CLASSICAL. Established; do not re-derive.

## Decomposition (suggested attack)

1. **Instantiate `R` cleanly.** Confirm `e_p` (atom of pure `p`) and `R(p,q)=e_p(q)` are
   well-defined on the homogeneous-spectral-with-sequential-product class WITHOUT assuming
   self-duality. State exactly what "atom of a pure state" means absent an inner product.
2. **(A)** Prove symmetric `R` -> self-dual -> EJA in this setting (the transition form
   `⟨p,q⟩ := R(p,q)` symmetric + nondegenerate self-dualizes the cone; mind homogeneity).
3. **(B)** Build the smallest explicit Vinberg-T-algebra `V` (rank 3 suffices; the
   non-symmetric homogeneous cone of e.g. upper-triangular / the Vinberg cone is the standard
   source) and COMPUTE `R(p,q)` vs `R(q,p)` on two pure states, exact arithmetic. Deliver the
   rational asymmetry as the witness.
4. **(C)** Compare "`R` symmetric" to "self-dual": is the former a strictly weaker
   order-condition, or verbatim equivalent? Pin the minimal structure to state it intrinsically.
5. **Verdict + scope:** which fork (1/2/3), with the axiom dependence explicit, and the
   explicit Vinberg witness attached.

## Existing pieces / sources
- Live paper: `~/repos/blog/landing/papers/qm-from-self-modeling/` (`main.tex`,
  `sections/axiom-verification.tex`, `type-exclusion.tex`, `discussion.tex`).
- vdW 2019 (arXiv:1803.11139, esp. §VII + minimality §); BUvdW 2023 (arXiv:2306.00362);
  Niestegge 2012 (arXiv:0912.0203); Janotta-Lal 2013 (arXiv:1302.2632); Koecher-Vinberg
  (Faraut-Koranyi, *Analysis on Symmetric Cones*); Alfsen-Shultz 2003; BBLW 2007.
- Context: `~/repos/blog/research/STATE.md` (2026-06-23 Paper-5 block), `GRAPH.md` (P5 node +
  SHOCK 1), memory `paper5-recovery-relativity-of-isomorphism` (THE PIN section), the
  superseded `paper5-cone-freeness-prompt.md`.

## Out of scope
- The complex-vs-real-vs-quaternionic selection (imported local tomography) — separate, parked.
- HOMOGENEITY itself — taken as granted here (the operational reading delivers positivity+S5
  -> homogeneity); if you doubt it, note it but do not let it consume the run.
- The metaphysical bridge "self-modeling MANDATES symmetric recognition" — the paper's
  `[STRUCTURAL-CORRESPONDENCE]`, grounded in relativity-of-isomorphism; GPD decides only
  whether the math (A/B/C) leaves it room to be non-circular and non-vacuous.
- Consciousness / Φ / gravity (separate tracks).

## Reward-hacking guard (engage the self-checks)
Do NOT prove (A) by assuming self-duality or by invoking any inner product not built from
`R` itself — that is the circularity under review. Do NOT declare `R`-symmetry "automatic"
by importing a Jordan/JB fact (the JB spectral theorem, `U_a` positivity) — those presuppose
the conclusion; the Vinberg counterexample says symmetry is genuinely extra, so an
asymmetric witness (B) is the EXPECTED and fully acceptable outcome — do not force a
positive. Do NOT redefine "homogeneous spectral OUS with sequential product" to be a Jordan
algebra by fiat, or "pure state / atom" to smuggle an inner product. The deliverable is the
A/B/C verdict with axiom dependence explicit AND the exact Vinberg recognition-asymmetry —
not a defense of Paper 5. If the honest finding is (C-ii) equivalent (recognition-symmetry
= self-duality verbatim), SAY SO — it is a valuable result that pins the assumption's true
name.
