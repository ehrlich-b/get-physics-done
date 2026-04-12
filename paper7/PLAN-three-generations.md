# Plan: Add Three Generations Section to Paper 7

## What we have

Four theorems from the Peirce tower analysis (derivation 32):
1. Iterated Peirce gives exactly 3 levels, terminates at R
2. Observer breaks S_3 -> S_2, structural 2+1 split
3. 8:1 coupling hierarchy (direct vs tower), universal
4. x_1 zero bilinear coupling - only cubic vertex

Plus: 8+8+8 decomposition from rho_J, null result on mass ratios,
comparison with Boyle/Singh/Farnsworth.

## Files to modify

All in `~/scratch/get-physics-done/paper7/`:

### 1. gaps.tex (Gap Gen, ~line 121-128)

**Current:** LOW severity, "no mechanism producing 3 copies of 16"

**Change to:** LOW -> NARROWED. Update description:
- Peirce tower gives exactly 3 levels (Theorem 1)
- Observer breaks triality S_3 -> S_2 (Theorem 2)
- 8:1 coupling hierarchy quantified (Theorem 3)
- x_1 zero bilinear coupling (Theorem 4)
- REMAINING: 2nd-vs-3rd generation split (S_2 breaking), mass ratios
  (requires D_F eigenvalues)
- "What would close it" -> D_F eigenvalue computation on h_3(O)

### 2. discussion.tex - Outlook item 3 (~line 225-233)

**Current:** 8-line placeholder mentioning Furey and Boyle

**Expand to:** ~40-line subsection "Generation structure: the Peirce tower"

Contents:
- State the Peirce tower result (3 levels, dimensions 16/8/0)
- State the 2+1 symmetry breaking (observer E_{11} breaks S_3 -> S_2)
- State the 8:1 coupling hierarchy
- State x_1 zero bilinear coupling + cubic vertex as only path
- Compare with Boyle (symmetric S_3, no hierarchy) and Singh (inputs charge)
- Cite Farnsworth 2025 as path to mass ratios via D_F
- Acknowledge: 2nd-vs-3rd split and actual mass ratios remain open

### 3. discussion.tex - "Not claimed" section (~line 281-282)

**Current:** "No mechanism producing three generations of fermions"

**Change to:** "The Peirce tower gives three levels with a 2+1 split and
8:1 coupling hierarchy, but specific mass ratios and the 2nd-vs-3rd
generation split remain open."

### 4. main.tex - Abstract (~line 37-38)

**Current:** "one-generation chiral Standard Model representation"

**Change to:** Keep "one-generation" in the main claim but add a sentence:
"The iterated Peirce decomposition of h_3(O) yields exactly three levels
with an 8:1 coupling hierarchy, providing a structural account of three
generations."

### 5. refs.bib

Add:
- Singh 2022 (Eur. Phys. J. Plus 137, 664)
- Farnsworth 2025 (arXiv:2503.10744)

## What NOT to change

- The main derivation chain (Parts A + B + Synthesis) is untouched
- Gap A, B1, B2, C statuses unchanged
- The 9-link chain table unchanged
- One-generation claim remains the PROVED result; three generations is
  ARGUED (Peirce tower) not proved

## Verification

1. Paper compiles: `cd paper7 && tectonic main.tex`
2. No broken refs
3. Gap register consistent with discussion
4. Abstract accurately reflects what's proved vs argued
