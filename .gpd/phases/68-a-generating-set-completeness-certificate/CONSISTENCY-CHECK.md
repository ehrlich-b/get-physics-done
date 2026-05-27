# Phase 68 Cross-Phase Consistency Check (RAPID MODE)

**Phase:** 68 — (a) Generating-Set Completeness Certificate (RING-01)
**Mode:** rapid (post-phase)
**Date:** 2026-05-27
**Verdict:** CONSISTENT
**Checks performed:** 11 | **Issues found:** 0 (1 INFO note carried forward, non-blocking)

## Scope

Exact symbolic invariant theory over Q on the F_4 two-copy ring R[27⊕27]^{F_4}.
Two plans: 68-01 (Molien-Weyl bigraded Hilbert series H(s,t), no Sage) and
68-02 (generating-set completeness + minimality certificate). Checked against the
full conventions ledger (state.json convention_lock: 18 canonical + 14 custom) and
the v16.0 cross-phase numerical chain (Phases 65, 65.1, 66, 67).

## 1. Convention compliance vs full ledger — ALL COMPLIANT

| Convention (ledger) | Relevant? | Phase 68 usage | Status |
|---|---|---|---|
| Group F_4 = Aut(h_3(O)), NOT E_6 | Yes | Weyl group \|W(F_4)\|=1152; 48 roots; Blind E_6 used only as labelled contrast, NOT as H_true (fp-e6-free rejected) | OK |
| Rep 27 = 1 ⊕ 26 (trace-free irred) | Yes | Eq (68.2): D(u,w)=(1-u)^3·∏_{24 wts}(1-u w^{2μ}); 27-weight multiset {0^3}∪{24 nonzero} | OK |
| c = Tr(X∘Y), bidegree (1,1) | Yes | candidate #7, bidegree (1,1); c(X,X)=Tr(X^2) NOT (Tr X)^2 | OK |
| jordan = (1/2)(AB+BA) | Yes | stated in both SUMMARY conventions + ASSERT_CONVENTION | OK |
| Cubic norm det X; polarize d(X,X,X)=6 det_3; det_3 cross=2Re((x2x1)x3) [Phase 64.1] | Yes | 68-02 uses polarize_d ONLY to PRODUCE (2,1)/(1,2) candidates (Schwarz); det_3 fix referenced | OK |
| Exact over Q; ranks via sympy/DomainMatrix-over-QQ, NEVER numpy float rank | Yes | exact_qq_rank throughout (14 / 22 refs in the two files); module-local exact-only guard PASS | OK |
| Krull target = 10; superseded 7 FORBIDDEN | Yes | KRULL_TARGET=10 (code ln 160); fp-krull7 rejected | OK |
| octonion_algebra (float64) = formula reference ONLY, never decisive | Yes | 0 imports on decisive path (matches are "NEVER import" comments only) | OK |
| R_pt frozen; Tr(X)Tr(Y) ∈ R_pt; c ∉ R_pt | Yes | (1,1) lower-product = Tr(X)Tr(Y) (rank 1), +c → 2 | OK |
| Metric (+,+,…,+) Riemannian Fisher; Fourier/gauge/renorm = N/A (pure algebra) | Partial | ASSERT_CONVENTION restates N/A for non-algebra conventions | OK / N/A |

Non-applicable canonical conventions (Fourier, gauge, regularization, renormalization,
coordinate, index positioning, time ordering, covariant derivative, creation/annihilation,
Levi-Civita) are all N/A for pure invariant theory and are explicitly tagged N/A in the
ledger and in the ASSERT_CONVENTION header. No silent skips.

## 2. NAMING-QUIRK RESOLUTION (the flagged short/long label) — DOCUMENTATION-ONLY, NOT A VIOLATION

**Finding:** code/molien_bigraded.py labels the norm^2=2 vectors "short_roots" and the
norm^2=1 vectors "long_roots" — swapped vs standard Bourbaki (Bourbaki: long=norm^2=2,
short=norm^2=1). This is the documented quirk.

**Decisive object verified independently (no harness):**
- The 26 of F_4 is the small-fundamental / short-root rep: its 24 nonzero weights are the
  **norm^2=1** vectors {±e_i (8)} ∪ {(±1/2)^4 (16)}. I reconstructed both root sets from
  scratch: 24 vectors at norm^2=2 (perms(±1,±1,0,0)) and 24 at norm^2=1; total 48 = F_4. ✓
- Phase 68 uses the **norm^2=1** set as the 26's nonzero weights (it calls them "long_roots").
  This is the **correct** weight set, and it is **gate-pinned**: using norm^2=2 gives
  d_(1,1)=3 (spurious antisymmetric trivial in Λ^2(27)) and FAILS gate G2; norm^2=1 gives
  d_(1,1)=2 (Phase 67 anchor) and the correct single-copy series.
- The ASSERT_CONVENTION header (ln 69) and REP-DECOMP (ln 70) BOTH explicitly state the
  label is swapped vs Bourbaki and that "the 26's weights are the norm^2=1 set."

**Conclusion:** The label is cosmetic and transparently documented. The physics (weight set
= norm^2=1) is correct and pinned by the calibration gate. NOT a convention violation; does
NOT affect any result. The Weyl-measure numerator uses all 48 roots and is length-symmetric
(CT=1152 either way), so only the CHARACTER weight set matters — and it is the right one.

## 3. Cross-phase numerical chain — ALL ANCHORS AGREE (independently recomputed)

| Quantity | Producer | Phase 68 value | Independent check | Status |
|---|---|---|---|---|
| trdeg = 54 − orbit_dim(44) | Phase 65/65.1 | Krull=10 | 54−44=10 ✓ (NOT 7) | OK |
| Chain trdeg ≥ SPINE rank ≥ quotient | 65.1/66/67 | 10 ≥ 7 ≥ 1 | 10≥7≥1 ✓ | OK |
| Krull (Phase 68) == trdeg | 65 → 68 | 10 | 10==10 ✓ | OK |
| bidegree-(1,1) coeff | Phase 67 = 2 | Molien 2; kernel 729−727=2 | all three == 2 ✓ | **OK (decisive)** |
| single-copy H(s,0) | Phase 68 | [1,1,2,3,4,5,7] | #partitions(n, parts≤3) = [1,1,2,3,4,5,7] ✓ | OK (plan typo "6" correctly rejected) |

**Single-copy s^6 = 7, not 6 (plan typo):** independently confirmed by direct partition
enumeration. The executor caught the plan's typo via gate G1 and corrected it — this is the
gate working as designed, not drift.

## 4. Two-route f_4-kernel arithmetic — SELF-CONSISTENT

dim Sym^a(27)⊗Sym^b(27) − rank == Molien coeff, all recomputed from comb(a+26,26):

| bidegree | space dim (Sym check) | rank | dim−rank | Molien | Status |
|---|---|---|---|---|---|
| (1,1) | 27·27 = 729 | 727 | 2 | 2 | OK (reproduces Phase 67) |
| (2,0)/(0,2) | 378·1 = 378 | 376 | 2 | 2 | OK |
| (2,1)/(1,2) | 378·27 = 10206 | 10202 | 4 | 4 | OK |
| (2,2) | 378·378 = 142884 | 142875 | 9 | 9 | OK (full, no fallback) |

Phase 67 Route-A integers re-checked: Sym^2(27)=378, Sym^2(26)=351=1+26+324. ✓

## 5. Minimality / (2,2) generator decision — INTERNALLY CONSISTENT

- All 10 in-span-of-lower-products increments == +1 (genuine generators). ✓
- (2,2): lower-product rank 8, +Tr(X^2∘Y^2) → 9 = d_true(2,2)=9 ⇒ GENERATOR (8+1=9). ✓
- c at (1,1): lower-product 1 (= Tr(X)Tr(Y) ∈ R_pt) +c → 2 = d_(1,1) — reproduces the
  Phase-67 quotient-1 structure exactly. ✓
- # ring generators (10) == # field generators (Phase-65.1 trdeg-10 set, 10) — every field
  generator is also a ring generator; consistent, not a contradiction. ✓

## 6. Provides/consumes verification

Phase 68 consumes from 65 (52-gen f_4 basis, exact_qq_rank, Krull 10), 65.1 (10-candidate
set + bidegrees verbatim), 67 (the (1,1)=2 anchor + Leibniz-lift engine). All consumed values
verified to match the producers semantically and numerically (see §3–§4). Plan 02 regenerates
Plan 01's d_true by IMPORTING molien_bigraded (not hand-typed), re-firing the handoff gates
(CT=1152, [1,1,2,3,4,5,7], (1,1)=2, (2,2)=9, symmetry) — a clean producer→consumer transfer.

Phase 68 provides to v16.0 closeout / Phase 69: the CERTIFIED-COMPLETE minimal generating set
(10 generators), (2,2)=GENERATOR, FREE-through-deg-6. These do not feed a downstream numerical
consumer in the current roadmap (Phase 69 is STATEMENT-only REDUCIBILITY), so no forward
test-value mismatch is possible.

## 7. Honest-finding / scope note (not an inconsistency)

The ring is FREE through total degree 6 (plog all {0,+1}, no syzygies), contrary to the Blind
E_6 non-free EXPECTATION. Reported honestly with the explicit caveat that the certificate is
degree ≤6 only and the first relation (if non-free) is at degree ≥7. This is correctly framed
as a `tension` comparison_verdict against Blind (NOT fp-e6-free-form: d_true was computed
independently by Molien-Weyl and merely HAPPENS to match the free product through deg 6).
Cross-phase-consistent and within the contract's NEGATIVE-RESULT-IS-SUCCESS framing.

## Carried-forward INFO note (from Phase 67 verification, non-blocking)

code/degree2_uniqueness.py:704 sets block_02 = block_20 by assignment while an adjacent
comment says "recompute (not assume)". Math correct by X↔Y symmetry; verifier independently
confirmed (0,2)=2. Phase 68 reconfirms symmetry d_(a,b)=d_(b,a) for all a+b≤6, so this note
does not propagate into Phase 68. No action required.

## Summary

All v16.0-binding conventions are honored. The flagged short/long naming quirk is a
transparently-documented label issue only; the decisive weight set (norm^2=1 = the 26's
nonzero weights) is correct and gate-pinned. Every cross-phase numerical anchor —
trdeg 10 ≥ rank 7 ≥ quotient 1, Krull 10, and the bidegree-(1,1) coefficient = 2 across
Phases 67 and both Phase-68 routes — agrees exactly. Exact-over-Q discipline (no numpy float
rank, no octonion_algebra on the decisive path) is enforced by module-local guards in both
files. **VERDICT: CONSISTENT.**
