# GPD — K1: does the Niestegge ℓ⁴ qubit admit an in-family tower? (THE decider for the genericity route, §19)

Written 2026-07-01 (Fable pass). Context: `~/repos/blog/research/paper5-virtuous-loop-three-joints.md` §19
(read it first) — axiom B deployed as a literal measure (the B-histories-mass) makes complex QM the unique
B-critical self-model type, BUT the theorem is scoped to simple EJAs with in-family towers. The one live
threat (kill-condition K1) is the non-EJA spectral sub-ensemble, test case ℓ⁴. This GPD decides it.
Anti-glaze; exact arithmetic where possible; ground every claim or tag it.

## CLAIM K1 (prove or disprove)
**The Niestegge rank-2 ℓ⁴ system (the ice-cream cone over the ℓ⁴ disk; Niestegge 2024, arXiv:2208.07135,
Thm 7.1 system) admits an in-framework self-composite:** a composite order-unit space carrying product
states, product effects, non-signaling constraints, and a sequential product extending the product form
`(a⊗b)∘(c⊗d) = (a∘c)⊗(b∘d)`, with the composite itself spectral (Def-1(i) grade:
`~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` lines 395–424).

## Why each branch matters (both are decisive — this is not a formality)
- **TRUE ⇒ the ℓ⁴ tower exists.** Then compute: (a) its readable/product-sector dimension growth dᵏ vs its
  full composite dimension D_k; (b) |Aut| of the tower (the single system's linear symmetry group is FINITE
  — hyperoctahedral-type — which the B-measure REWARDS). If the tower is readable with sub-factorial Aut,
  **ℓ⁴ out-masses ℂ and the genericity route is DEAD** — report loudly, including the uncomfortable
  corollary that B taken literally would *select* ℓ⁴ over QM (a problem for axiom B itself, worth knowing).
- **FALSE ⇒ ℓ⁴ is depth-bounded** (no in-family tower) ⇒ it dies the Albert death in the histories measure
  (vanishing relative mass, no self-duality import needed) ⇒ the Jordan-side wall brick is handled by the
  measure. Then GENERALIZE: characterize which non-EJA spectral Def-1 systems admit in-family towers at all
  (ℓᵖ all even p; polygon/gbit systems if they clear Def-1(i) spectrality at all; van de Wetering's weaker
  sequential-product spaces). If none do, §19.4's scope-gap closes by depth-boundedness.

## Traps / hints
- Do NOT confuse the composite requirement with full S1–S7: vdW Thm 1 says a valid (S1–S7) sequential
  product forces EJA, and the ℓ⁴ single system already fails S4 and S6 — Def-1(iii) demands only the
  product-form sequential product on the composite, a strictly weaker structure. The question is whether
  even THAT exists with the composite spectral.
- The catalogue (`~/repos/blog/research/self-modelers-catalogue.md` §11 finding (A), the "open probe")
  already framed the two outcomes on different axes: composite-exists-but-fails-LT (second selection death,
  wall sharpened) vs not-in-framework (witness removed / here: depth-bounded). §19 adds the measure stakes.
- Niestegge's composability status is `?` in the catalogue master matrix (line ~233). Check his 2024 paper
  and any sequels for composite constructions before deriving from scratch.
- Spectrality of composites is restrictive (Alfsen–Shultz compressions on the composite). The min/max GPT
  tensor products always exist but are NOT automatically spectral or sequential-product-bearing — existence
  of *some* composite is not the claim; the claim is the Def-1(iii)-grade one.
- Exact arithmetic: the ℓ⁴ unit ball is semialgebraic (quartic); pursue rational/symbolic witnesses; if a
  composite candidate exists, its failure/success on spectrality should be checkable on explicit elements.

## Output
Verdict on K1: TRUE (with the tower's readable-dim and |Aut| growth computed and the mass comparison to ℂ
run) / FALSE (with the obstruction named and the generalization to the non-EJA sub-ensemble attempted) /
BLOCKED (with the precise missing lemma). File the result back into `paper5-virtuous-loop-three-joints.md`
(new subsection under §19) and propagate STATE.md / GRAPH.md / memory per CLAUDE.md. No SSOT flip without
Bryan.
