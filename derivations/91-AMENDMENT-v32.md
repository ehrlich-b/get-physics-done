# Phase 91 (v31.0) — AMENDMENT (raised by v32.0-B; pending human ratification of the fold-in)

This note records a correction to the ratified v31 record discovered during v32.0-B (the three-path
reconciliation, `v32-reconciliation-directive.md`; blog-side fetched Boucetta arXiv:0712.2830
directly). **The v31 committed record (`91-VERDICT.md`, the milestone bookkeeping) is left INTACT** —
this is a flagged amendment for the human to ratify, not a self-amendment (STOP rule 2 / the standing
discipline).

## What STANDS (unchanged, re-confirmed three ways)

**v31's EXISTENCE verdict: LIVE — matter sources a genuine nonzero transverse-traceless metric mode
on the cut CP².** B3 = dφ_M⊗dφ_M (= the pinned π_{1/2}M tangent stress B6) has a nonzero TT residue;
york_solve(B3) inconsistent while the B1 Hessian control solves (Trap #14). Re-confirmed in v32 by
(i) the cliff-free `extract_tt` (tr_g r = 0, δr = 0, r ≠ 0 for all matter directions), (ii) the
first independent verifier, (iii) the blog-side fingerprints. The Nordström-class two-scalar ceiling
is broken. **This is not in question.**

## What is RETRACTED (the isotypic localization)

1. **"the (2,0)+(0,2) blocks of B3 are jointly gauge ⇒ the TT residue is purely (1,1)"** — RETRACTED.
   The unique York TT residue `r` carries **nonzero (2,0) AND (0,2) blocks** (confirmed exact over Q
   on all 8 Gell-Mann directions, `code/lichnerowicz_response_fingerprint.py`). The residue straddles
   all three Kähler sectors.

2. **"the residue lives in the λ=12 (1,1)-Hermitian Boucetta dim-8 su(3)-adjoint multiplet"** —
   CORRECTED. The residue is a **single Lichnerowicz eigentensor at λ_L = 32** spanning the
   **triple-27**: the (1,1)-dim-27 (Boucetta Table V/VIII **row 2**, φ∘δ*_h∘δ̄*_h(T^{0,0}_{2,2}),
   λ=4(m+2)(m+4)=32) ⊕ the (2,0)/(0,2)-dim-27s (Tables VI/VII row 1, λ=32). The λ=12 dim-8 adjoint
   (Table V/VIII **row 1**) is **non-transverse** and is NOT the mode. The matter bilinear's
   transverse content is the **27-channel** of Sym²(8) = 27⊕8⊕1; the 8 and 1 channels have no
   transverse home at this level (c₈ = c₁ = 0).

3. **"the TT deficit is forced to 1 by Sym²(8) ⊇ 8 once (multiplicity one)"** — the rep-theory
   *counting* is fine, but it was applied to the WRONG channel. The transverse direction is
   P27(M⊗M) (the 27-channel, multiplicity one in Sym²(8)), not N(M) = the 8-channel adjoint square.
   The v31 dimension-audit "deficit = 1 per direction" coincidentally matched because a single
   generator's 27-image has the relevant low rank, but the *identification* (8-adjoint) was wrong.

## Why v31's "jointly gauge" solve succeeded (diagnosis)

v31's block-restricted gauge solve (`_york_solve_blocks` on the (2,0)+(0,2) blocks) reported the
anti blocks as in-gauge-span. This was an **ansatz-space artifact**: at the degree/span used, the
(2,0)+(0,2) part of B3 was absorbable into the block-restricted gauge image, but the FULL York
solve (matching all blocks simultaneously, with the transversality coupling between (1,1) and
(2,0)/(0,2)) leaves a genuine transverse anti content. The shared failure mode across v31 AND the
v32 first-verifier: **both stopped at Boucetta table row 1** (the λ=12 dim-8) as "the" TT multiplet,
missing row 2 (the λ=32 (1,1)-dim-27). Status: diagnosed at the level of "ansatz-space / wrong-row";
a full byte-level re-trace of the v31 `_york_solve_blocks` run is **diagnosed-pending** (not
verdict-critical — v32's full-solve straddle result is the corrected ground truth).

## Net effect on v31

EXISTENCE: unchanged (LIVE). Localization: corrected (triple-27 at λ=32, not dim-8 at λ=12). The v31
*headline* ("matter sources a genuine TT metric mode") is correct as stated; only the *which mode*
sub-claim moves. v32.0-B is the corrected, strengthened continuation (the norm closes:
‖TT(B3)‖² = (1/30)(TrM²)², ε = 20). Recommend the human fold this correction into the v31 record at
the next bookkeeping pass, or carry it as a standing amendment.
