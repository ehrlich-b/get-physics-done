# GPD: Can Recognition-Symmetry be a FIT? (does self-modeling FORCE R(p,q)=R(q,p)?)

**The Paper-5 recovery now rests on ONE imported premise — recognition symmetry,
`R(p,q)=R(q,p)`. This prompt asks whether that premise is a THEOREM of the self-modeling
definition (a FIT) or an irreducible import (a grounded CLAMP).** Prove or disprove a single
claim about Paper 5's Definition 1.

Written 2026-06-23, downstream of the recognition-symmetry FORK 1 verdict
(`paper5-recognition-symmetry-prompt.md` + `...-closeout-directive.md`): (A) `R` symmetric ⟹
self-dual ⟹ EJA is PROVED; (B) `R` symmetric is NON-automatic (Vinberg witness `5/6 ≠ 2/3`);
(C-i) it is a real, strictly-weaker, checkable condition. So Paper 5 is now "GIVEN `R`
symmetric, self-modeling forces complex QM." The ONLY remaining question for a
derivation-from-the-program is whether `R` symmetric itself follows from self-modeling.
Self-contained; live source `~/repos/blog/landing/papers/qm-from-self-modeling/`.

## The claim to PROVE or DISPROVE

Setup as in the recognition-symmetry prompt: `V` a finite-dim homogeneous spectral order-unit
space with a total positive sequential product (S1–S3, S5–S7), NOT assuming S4. `R(p,q) :=
e_p(q)` the recognition functional on pure states (`e_p` = atom of pure `p`). ADD Paper 5's
**Definition 1** (`def:self-modeling-system` in `main.tex`) — a faithful tracking map `φ`
(body → internal model) closing the test–update–test cycle. Pull Definition 1 VERBATIM from
the live paper; do not paraphrase its clauses.

> **(FIT).** Definition 1's faithfulness / tracking condition ENTAILS `R(p,q) = R(q,p)` for
> all pure `p,q`. Equivalently: any `V` that carries a Definition-1 self-modeling structure
> has symmetric recognition — recognition-symmetry is a theorem of self-modeling, not an extra
> axiom.

**PROVE** ⟹ recognition-symmetry UPGRADES from imported premise to FIT: Paper 5 becomes
"self-modeling forces complex QM," conditional on NOTHING beyond Definition 1 (+ the parked
local-tomography import). The Lean `recognition_symmetry` / Step-3 premise downgrades to a
derived lemma. This is the strongest possible outcome for the program.

**DISPROVE** (exhibit a `V` + a fully valid Definition-1 self-modeling structure on it with
`R` ASYMMETRIC — e.g. the rank-3 Vinberg cone of (B), IF it admits a Def-1 tracking map):
recognition-symmetry is genuinely INDEPENDENT of self-modeling-as-formalized; the paper
correctly IMPORTS it and its only justification is the [STRUCTURAL-CORRESPONDENCE]
"isomorphism is unordered." Paper 5 stays a conditional synthesis on one grounded premise.
Identify the minimal extra Def-1 clause that WOULD force symmetry, if any.

## The crux (why this is non-trivial — do not collapse it)

"Isomorphism is symmetric" as a BINARY relation (`p≅q ⟺ q≅p`) is trivial. But `R(p,q)=e_p(q)`
is a DEGREE in `[0,1]`, not yes/no. The Vinberg witness (B) shows the DEGREE can be asymmetric
(`5/6 ≠ 2/3`) while the binary iso-relation stays symmetric. So a FIT must show Definition 1
forces symmetry of the DEGREE — NOT merely that "isomorphic-or-not" is a symmetric relation
(which is free and proves nothing). This is exactly the gap between the metaphysical slogan
and the math.

## Decomposition (suggested attack)

1. Write `e_p(q)` and `e_q(p)` explicitly in terms of `φ` and the Alfsen–Shultz compressions.
   Determine what faithfulness of `φ` actually equates: the supports (binary — free) or the
   degrees (the load-bearing claim).
2. Confront the Vinberg cone (the (B) witness): does it admit ANY map satisfying EVERY clause
   of Definition 1? If yes with asymmetric `R` ⟹ DISPROVE (import confirmed). If Definition 1
   provably excludes it ⟹ candidate PROVE; exhibit the excluding clause.
3. Pin the minimal Definition-1 clause equivalent to (or forcing) `R`-symmetry — i.e. name the
   exact faithfulness content that is recognition-symmetry in disguise, or show none is.

[Inline definitions: reuse `paper5-recognition-symmetry-prompt.md` verbatim; add Definition 1
from `main.tex`.]

## Reward-hacking guard
Do NOT "prove" FIT by assuming `φ` is an isometry for an inner product not built from the
program's own primitives — that re-imports self-duality (the exact circularity under review).
Do NOT "prove" FIT from the binary symmetry of the isomorphism relation — the degree is the
question. Do NOT declare DISPROVE without exhibiting a CONCRETE Def-1 structure (a tracking map
satisfying every clause) on the asymmetric witness — "Def 1 probably allows it" is not a
disproof. Symmetric (FIT, upgrade) and a concrete asymmetric Def-1 witness (import confirmed)
are BOTH fully acceptable, decision-relevant outcomes; do not force a positive. Deliverable =
the FIT/IMPORT verdict with the exact Definition-1 clause dependence, not a defense of Paper 5.
