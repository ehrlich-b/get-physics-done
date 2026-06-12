# Phase 92 (v32.0-candidate) — GATE 3 SUMMARY: The Closed Form (the verdict center)

> **CORRECTION (v32.0-B, binding).** This first-pass summary predates the three-path reconciliation
> (`v32-reconciliation-directive.md`; Boucetta arXiv:0712.2830 fetched directly). The matter TT mode
> is NOT the "λ=12 (1,1) dim-8 su(3)-adjoint", and the verdict norm is NOT κ=1/54. RECONCILED: a single
> **λ_L=32 eigentensor straddling the triple-27** (Boucetta Table V/VIII row 2 (1,1)-27 ⊕ Tables VI/VII
> (2,0)/(0,2)-27s), norm **‖TT(B3)‖²=(1/30)(TrM²)²** (full mode; 1/54 was the (1,1)-block share, forced
> 5:4 split), **ε=20**, direction **T₂₇[P27(M⊗M)]** (the 27-channel; c₈=c₁=0; c∝N(M) FAILS as a
> wrong-channel claim, not "richer"); Koiso clean (no TT at λ=12). Wherever this file says
> "dim-8/(1,1)/adjoint", "κ=1/54", "c∝N richer", "rank-6=d-symbol image", or "Weitzenböck shift", read
> `92-VERDICT.md` + `92-tensor-dictionary-RESEARCH.md` §7/§8 instead.


**Driver:** `python3 -u code/lichnerowicz_response.py` (the extract_tt / l2_tensor / direction
computations) → exact over Q.

Gate 3 is the verdict center. It extracts the closed form, tests the direction hypothesis, verifies
the FORCED norm identity, and closes the York dictionary.

| # | Object | Result |
|---|---|---|
| 3a | extended solve B3 = Σc_a t_a + δ*ω + f·g | **CLOSES** — every direction's TT residue exhibited (tr_g=0, δ=0, nonzero) in the λ=12 (1,1) multiplet; sparse + dense + generic; consistent with v31 (no contradiction) |
| 3b | direction c(M) ∝ N(M) = M²−⅓TrM²·I | **FAILS (a FINDING)** — N(s01)=N(d1) but r^{(1,1)}(s01) ≠ r^{(1,1)}(d1); the residue carries MORE than the d-symbol square |
| 3c | **‖TT(B3)‖² norm identity** | **‖TT(B3)‖² = (1/54)(TrM²)²** — single FORCED κ=1/54, **detM ABSENT** (s01, d1, d2[detM=−2], a01, dense[detM=−7] all give κ=1/54) |
| 3d | York dictionary B3 = TT + δ*ω + f·g | **CLOSES EXACT over Q** — (ω, f) in certified closed form; r tr_g=0, δ=0 |

## (3a) The extended solve closes — cliff-free

The deferred v31 positive-exhibit certificate, obtained cliff-free. For every matter direction the
unique York TT residue `r = B3 − δ*ω − f·g` (tr_g r = 0 AND δr = 0) is EXTRACTED EXPLICITLY by the
matched-monomial CRT solve (RESEARCH §5A): consistent, `r` nonzero, in the λ=12 (1,1)-Hermitian
multiplet. This confirms v31's EXISTENCE result constructively, for sparse (s01), generic single
generators (all 8), and dense generic matter — direction-independent, exact over Q. No contradiction
with v31 (STOP rule 2 not triggered).

## (3b) The direction hypothesis c(M) ∝ N(M) — a genuine FINDING (FAIL)

The NAMED hypothesis (object (i)) was `c(M) ∝ N(M) = M² − ⅓Tr(M²)I` (the d-symbol square, the
multiplicity-one projection direction). **It FAILS.** The clean test: for the two single generators
s01 and d1, `N(s01) = N(d1) = diag(1,1,0) − ⅔I` exactly (both off-diagonal/Cartan collapse to the same
adjoint square). If `c(M) ∝ N(M)`, the residue would depend on M only through N(M), giving
`r^{(1,1)}(s01) = r^{(1,1)}(d1)`. **But the residues DIFFER** (verified exact over Q). So the TT tensor
direction carries MORE M-information than the d-symbol square — the full `dφ_M⊗dφ_M` gradient-bilinear
structure (φ_{s01} and φ_{d1} are different eigenfunctions), not just `N(M)`.

This is a FINDING, not a gate failure (RESEARCH §6, 3b verbatim: "a FAIL is a FINDING"). It refines
object (i): the closed form `TT(B3) = Σc_a t_a` EXISTS, but `c(M)` is richer than the named
hypothesis. The dictionary's first nuance — named. (It does NOT touch the LIVE criterion, which is the
norm (3c), not the direction.)

## (3c) THE NORM IDENTITY — the FORCED closed form (object (ii), the verdict center)

**‖TT(B3)‖² = (1/54)·(TrM²)²** — a single FORCED rational constant κ = 1/54, with **detM ABSENT**.

| matter M | ‖TT(B3)‖² | (TrM²)² | detM | κ = ‖TT‖²/(TrM²)² |
|---|---|---|---|---|
| s01 (off-diagonal) | 2/27 | 4 | 0 | **1/54** |
| d1 (diagonal) | 2/27 | 4 | 0 | **1/54** |
| d2 (diagonal, detM≠0) | 2/3 | 36 | **−2** | **1/54** |
| a01 (imaginary off-diag) | 2/27 | 4 | 0 | **1/54** |
| dense generic (detM≠0) | 128/27 | 256 | **−7** | **1/54** |

The constant κ = 1/54 is the SAME across all matters, INCLUDING matters with detM ≠ 0 (d2: detM=−2;
dense: detM=−7). So **detM is ABSENT** — the norm does NOT depend on the cubic invariant (the v27
cubic-blindness). This is forced by SU(3)-invariance + Cayley–Hamilton: the only degree-4 invariant of
a traceless 3×3 Hermitian M is `(TrM²)²` (since `TrM⁴ = ½(TrM²)²` and `detM·TrM = 0`). **No fitted
constant, no free function — the FORCED closed form that is the v32 LIVE criterion** (the strictly
higher bar of RESEARCH §0/§6).

(Method: the (1,1)-sector residue norm `‖r^{(1,1)}‖² = l2_tensor((0,r^{(1,1)},0), same)` — ONE exact L²
integral per matter, NOT a Gram; cliff-free.)

## (3d) The York dictionary closes

`B3 = r + δ*ω + f·g` EXACT over Q (verified: `B3 − r − δ*ω − f·g ≡ 0` block-for-block), with `(ω, f)`
assembled in certified closed form from the gauge+conformal potentials (object (iv)). The residue `r`
is the explicit TT tensor (tr_g r = 0, δr = 0). The full deformation-complex dictionary is closed.

## The verdict (FROZEN Gate-4 criteria)

`verdict(closes_3a=True, norm_forced=True, norm_needs_outside=None, schur_ok=True,
contradicts_v31=False) = ('LIVE', ...)`. LIVE because (3a) the residue closes for all matter AND (3c)
the norm closes with a FORCED exact constant κ=1/54 over the frozen tuple {(TrM²)²} (detM absent, no
free function). The direction-N(M) failure (3b) is a documented finding refining object (i), NOT a
PARTIAL trigger (the LIVE criterion is the norm, and the norm needs no invariant outside the frozen
tuple).

## Scope fence (binding, verbatim)

This is the deformation-complex DICTIONARY of a FROZEN imported geometry. No dynamical metric, no
selection law, no κ. LIVE = "the tensor sector's source data closes in canonical form" — a DICTIONARY
fact, not a dynamics fact. No Einstein-equation / Newton-constant / G=κT / dark-matter / geodesic
language; frozen FS geometry USED not derived; the v18/v20 MM corpse stays buried; OP² priced only.
Does NOT retract v17–v21 (Block-C statements; v32 is the strictly weaker upstream dictionary).
