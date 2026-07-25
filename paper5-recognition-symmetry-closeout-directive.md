# GPD Directive: Ratify and Record the Paper 5 Recognition-Symmetry Verdict (FORK 1)

**RATIFIED on the blog side after independent re-derivation. Record BY HAND**
(the `gpd phase complete` / `state advance` path is buggy — do NOT use it). This is a
Paper-5 (QM) track milestone, NOT a numbered gravity phase.

## Verdict (FORK 1): A-PROVE + B-asymmetric-Vinberg-witness + C-i-strictly-weaker

The recognition-symmetry gate (`paper5-recognition-symmetry-prompt.md`) returned the
strongest of its three forks. The Paper-5 recovery has a real, non-circular target.

- **(A) PROVED, in-setting.** `R` symmetric ⟹ self-dual ⟹ EJA. The self-dualizing inner
  product is built ENTIRELY from `R`: the atom map Φ: states→effects is a positive linear
  bijection; `R` symmetric ⟺ Φ self-adjoint ⟺ the transition form is symmetric; positivity
  ⟹ PSD, `e_p(p)=1` ⟹ nondegenerate ⟹ self-dualizes the cone ⟹ Koecher–Vinberg. No imported
  inner product, no spin-factor, no JB facts. Guard-clean.
- **(B) WITNESS.** `R` symmetric is NOT automatic. On the Vinberg cone (smallest non-self-dual
  homogeneous, rank 3) recognition is asymmetric two independent ways: canonical Koszul-duality
  `R(A,B)=391/84 ≠ R(B,A)=2543/1560`; genuine `[0,1]` transition probability `5/6 ≠ 2/3`, with
  the self-dual control symmetric at `2/3`. Re-derived by hand + sympy blog-side.
- **(C-i) STRICTLY WEAKER.** `R`-symmetric is EXTENSIONALLY equivalent to self-dual but
  INTENSIONALLY strictly weaker — a canonical, checkable recognition condition, not the
  inner-product existential. The CLAMP worry is defeated by (B). Relativity-of-isomorphism
  (iso is unordered ⟹ `R` symmetric) grips it non-circularly.

## Three corrections to the prompt's premises (change framing, not the fork)

1. The prompt's premise was WRONG: vdW §VII does not build a non-self-dual sequential product
   — total S1–S7 forces Jordan. The Vinberg product fails BOTH S4 and S6 (not S4 alone).
2. "S4 is the lone selector" is vdW-CONJECTURAL — his own counterexample fails S4+S6 jointly,
   he cannot isolate S4. Precise selector = {S4, S6}, with S4 the recognition-symmetry one.
3. Paper 5's actual gap is LOCATED: `main.tex` "Step 3: Symmetry" (was ~l.819–825). It does
   not posit self-duality; it asserts the Peirce-1 mixing `E(x,y)=E(y,x)` is automatic from
   "unordered Peirce pairs." That inference is the unestablished recognition-symmetry content.

## Blog-side actions already taken (record as DONE)

Paper fixes APPLIED to the live working copy
`~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` (NOT the frozen
`main-jmp-submitted.tex`, which stays untouched):
- Step 3 relabeled from a silent geometric fact to a named imported premise (recognition
  symmetry `E(x,y)=E(y,x)` / `R(p,q)=R(q,p)`, grounded in relativity-of-isomorphism, with the
  Vinberg non-vacuity witness `5/6 ≠ 2/3` inline).
- Proposition `coherence` hypothesis list gains orthosymmetry / S4.
- Cone-freeness caveat added (positivity is necessary but NOT Jordan-selecting; the selector
  is recognition symmetry via self-duality).
Verdict banked in memory `project_p5_recognition_symmetry`; blog memory
`paper5-recovery-relativity-of-isomorphism` is the standing pin.

## Record by hand

- GPD STATE / PROJECT: Paper-5 recognition-symmetry gate = FORK 1; Jordan/self-duality
  selection reduces to ONE named premise (recognition symmetry = relativity-of-isomorphism);
  (A) proved, (B) witnessed, (C-i). Close this task.
- memory `project_p5_recognition_symmetry`: already holds the verdict; confirm it records (A)/(B)/(C-i)
  and the three corrections.

## Scope-guard — bind into the record, do NOT overclaim

Record as: **"Paper 5 = the first rigorous CONDITIONAL — GIVEN recognition symmetry
(relativity-of-isomorphism), self-modeling forces complex QM; every other step a theorem."**

- **NOT** "self-modeling derives QM from nothing." The math beyond Koecher–Vinberg is the
  bridge (A): the program's recognition functional, if symmetric, IS a self-dualizing inner
  product. K–V still does the Jordan step. Contribution = bridge (A) + grounding of its premise
  in relativity-of-isomorphism + the (B) non-vacuity witness.
- The premise `relativity-of-isomorphism ⟹ R symmetric` is a load-bearing CLAMP, UPGRADED
  (from a silent Alfsen–Shultz "geometric fact" to a named program axiom) but NOT yet a FIT.
  Making it a FIT is the next task (`paper5-recognition-fit-prompt.md`).
- Local tomography → complex (over real/quaternionic) remains separately imported, parked.

## Fences (carry into the record)

(B)+(C-i) — "premise non-vacuous and non-circular" — are proven. The "self-modeling MANDATES
symmetric recognition" bridge is a labeled [STRUCTURAL-CORRESPONDENCE], NOT a GPD result. Do
NOT mark Paper 5 "derivation/closed"; it stays CONDITIONAL-SYNTHESIS on one named premise. The
frozen JMP snapshot is untouched; no JMP return until the decision letter lands.

## After recording

**Do NOT self-register the next slot.** The next direction
(`paper5-recognition-fit-prompt.md` — the R-inherits-isomorphism-symmetry FIT question) is
decided blog-side.
