---
phase: 70-a0-engine-reconciliation-signature-bridge
plan: 01
depth: full
one-liner: "Certified code/bulk_geometry_verification.py det_3 (cross 2Re((x2 x1) x3)) as the unique F_4=Aut(h_3(O))-invariant SSOT cubic norm — byte-identical verbatim copy, CH norm + 324/324 inner-derivation annihilation, buggy ordering rejected off-by-16, all exact over Q"
subsystem: [formalism, validation]
tags: [octonions, jordan-algebra, h3o, cubic-norm, f4-invariance, cayley-hamilton, exact-over-Q, ssot-engine]

requires:
  - phase: 64-setup-conventions-and-exact-engine
    provides: "ring_lemma_verification.py det_3 (cross 2Re((x2 x1) x3)) + LOCK harness + cayley_hamilton_norm + inner_derivations (the SSOT engine)"
  - phase: 64.1-det3-norm-consistency-fix
    provides: "Phase-64.1 cross-term factor-order fix ((x2 x1) x3) + the generic-norm-consistency lock (CH + 324/324) that the buggy (x1 x2) x3 order fails"
provides:
  - "code/bulk_geometry_verification.py — the Phase-70 self-contained exact-SymPy-over-Q cubic-norm SSOT engine for v17.0 (det_3 certified F_4-invariant; ALL_PASS, exit 0)"
  - "det_3 byte-identity guarantee (sha256 e43d6a3f...; runtime LOCK 0) — every downstream v17.0 curvature is built from a correct, F_4-invariant det"
  - "Three-ordering reconciliation table (SSOT/conjugated/buggy) rejecting fp-wrong-cross-term with exact-over-Q evidence (off by 16)"
affects: [70-02, 71, 72, 73]

methods:
  added: ["verbatim-copy integrity check via inspect.getsource (LOCK 0)", "fence-free exact-only guard wrapper (exact_only_guard_p70)", "three-ordering cross-term reconciliation with full-associator + order-discriminator non-vacuity"]
  patterns: ["self-contained decisive module (COPY not import) pinning conventions in one place", "F_4 certificate = CH-norm equality + 324/324 inner-derivation annihilation, exact over Q"]

key-files:
  created: [code/bulk_geometry_verification.py]
  modified: []

key-decisions:
  - "Copied Sections 1-3 (incl det_3, cayley_hamilton_norm, inner_derivations) VERBATIM from ring_lemma_verification.py via a single contiguous source slice (import sys -> end of inner_derivations), then asserted byte-identity at runtime (LOCK 0) and offline (sha256 e43d6a3f...) — guarantees no transcription drift in the SSOT det."
  - "Dropped ring_lemma's oracle-fence octonion_algebra touch entirely (Open Question 2): the module has ZERO octonion_algebra imports. Added exact_only_guard_p70() wrapper requiring in-fence==0 (Deviation Rule 4) since the verbatim guard hard-codes in-fence==1."
  - "Non-vacuity for the reconciliation uses the FULL associator (nonzero octonion) AND the association-order discriminator Re((x2 x1)x3)-Re((x1 x2)x3)=8, NOT the real-part triple-product associator (=0 at octonionic_points()[1]) — heeds plan-check Note A."

patterns-established:
  - "Pattern 1: a v17.0-milestone decisive module is a self-contained verbatim copy of the SSOT engine + a runtime byte-identity assertion, so the engine SSOT survives file decoupling."
  - "Pattern 2: certify an h_3(O) cubic norm as the F_4-invariant generic norm via TWO exact-over-Q certificates (Cayley-Hamilton norm equality at octonionic points + full inner-derivation annihilation), never via the necessary-but-insufficient LOCKs 1-5 alone."

conventions:
  - "arithmetic = EXACT over Q (sympy.Rational); ranks via sympy.Matrix.rank(), NEVER numpy.linalg.matrix_rank"
  - "jordan product a o b = (1/2)(ab+ba); Fano e1 e2 = e4; complex structure u = e7"
  - "det_3 cross-term = 2Re((x2 x1) x3) [SSOT]; buggy (x1 x2) x3 FORBIDDEN; polarization d(X,X,X)=6 det_3"
  - "engine-native layout: x0,x1,x2=diag(alpha,beta,gamma); x3..x10=oct x1->X[2][1]; x11..x18=oct x2->X[0][2]; x19..x26=oct x3->X[1][0]"
  - "metric signature mostly-minus on slice / Riemannian in bulk (v17.0 lock, commit 0d10eeea)"

plan_contract_ref: ".gpd/phases/70-a0-engine-reconciliation-signature-bridge/70-01-PLAN.md#/contract"
contract_results:
  claims:
    claim-engine-ssot:
      status: passed
      summary: "code/bulk_geometry_verification.py carries a single det_3 (cross 2Re((x2 x1) x3)) byte-identical to ring_lemma_verification.det_3 (sha256 e43d6a3f...; LOCK 0), equal to the Cayley-Hamilton generic norm at all 3 octonionic points (LOCK 7a) and annihilated by all 324 inner derivations [L_a,L_b] (LOCK 7b, dim f_4=52); LOCKs 1-5 + LAYOUT round-trip + fence-free exact-only guard all PASS, exact over Q; ALL_PASS, exit 0, deterministic across two runs."
      linked_ids: [deliv-bulk-engine, test-engine-all-pass, test-cross-term-association, ref-warm-engine, ref-faraut-koranyi]
      evidence:
        - verifier: gpd-executor
          method: "exact-over-Q assert harness (python3 code/bulk_geometry_verification.py -> ALL_PASS, exit 0) + inspect.getsource byte-identity (sha256 match)"
          confidence: high
          claim_id: claim-engine-ssot
          deliverable_id: deliv-bulk-engine
          acceptance_test_id: test-engine-all-pass
          reference_id: ref-warm-engine
          evidence_path: "code/bulk_geometry_verification.py (LOCK 0 + LOCKs 1-5/7a/7b; commit eb261773)"
    claim-cross-term-reconciled:
      status: passed
      summary: "On octonionic_points()[1] (genuinely non-associative; full associator [0,16,12,10,2,-24,-24,0]) the SSOT (x2 x1)x3 and conjugated x2*(x1*x3) orderings both give Re(cross)=+4 and det == CH norm = -24; the buggy (x1 x2)x3 gives Re(cross)=-4 and det = -40 != CH norm, off by exactly N_SSOT-N_buggy=16. Non-vacuity via full associator nonzero AND order discriminator = 8. fp-wrong-cross-term explicitly REJECTED with exact-over-Q evidence."
      linked_ids: [deliv-bulk-engine, test-cross-term-association, ref-warm-engine, ref-h3o-tower]
      evidence:
        - verifier: gpd-executor
          method: "exact-over-Q three-ordering reconciliation table + cross-check vs cayley_hamilton_norm"
          confidence: high
          claim_id: claim-cross-term-reconciled
          deliverable_id: deliv-bulk-engine
          acceptance_test_id: test-cross-term-association
          reference_id: ref-h3o-tower
          evidence_path: "code/bulk_geometry_verification.py (Section 9 + Task 3 block; commit eb261773)"
  deliverables:
    deliv-bulk-engine:
      status: passed
      path: code/bulk_geometry_verification.py
      summary: "Phase-70 exact-SymPy-over-Q cubic-norm engine: Sections 1-3 of ring_lemma_verification.py copied VERBATIM (byte-identical det_3 + cayley_hamilton_norm + inner_derivations + exact_only_guard + X_from_symbols + engine-native layout), re-running LOCKs 1-5/7a/7b ALL_PASS + a three-ordering reconciliation pre-flight. NO octonion_algebra import on the decisive path. Contains all must_contain tokens (def det_3, def cayley_hamilton_norm, def inner_derivations, def exact_only_guard, 2Re((x2 x1) x3), LOCK 7a, LOCK 7b, 324, reconciliation)."
      linked_ids: [claim-engine-ssot, claim-cross-term-reconciled, test-engine-all-pass, test-cross-term-association]
  acceptance_tests:
    test-cross-term-association:
      status: passed
      summary: "At octonionic_points()[1]: SSOT Re(cross)=+4 & det==CH (-24); conjugated Re(cross)=+4 & det==CH; buggy Re(cross)=-4 & det=-40 != CH (off by 16); full associator nonzero ([0,16,12,10,2,-24,-24,0]) and order discriminator = 8 (non-vacuous); LOCK 7a == 0 at all 3 points; LOCK 7b == 324/324. All exact over Q."
      linked_ids: [claim-cross-term-reconciled, claim-engine-ssot, deliv-bulk-engine, ref-warm-engine]
    test-engine-all-pass:
      status: passed
      summary: "python3 code/bulk_geometry_verification.py prints PASS for LOCK 0 (byte-identity), LOCK 1-5, LAYOUT round-trip, the fence-free exact-only guard, LOCK 7a, LOCK 7b; OVERALL ALL_PASS; exit 0; no FAIL line; the source-token guard reports 0 octonion_algebra imports and 0 numpy.linalg.matrix_rank calls. Deterministic (run1 == run2 byte-for-byte)."
      linked_ids: [claim-engine-ssot, deliv-bulk-engine, ref-warm-engine]
  references:
    ref-warm-engine:
      status: completed
      completed_actions: [read, use, compare, cite]
      missing_actions: []
      summary: "ring_lemma_verification.py is the decisive ground truth: Sections 1-3 copied verbatim; det_3 + 12 helpers proven byte-identical at runtime (LOCK 0) and via inspect.getsource sha256 match (e43d6a3f...); its ALL_PASS reproduced on the new module."
    ref-h3o-tower:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "h3o_tower's conjugated (x0,x1,x2) labeling 2Re(x2* x0* x1) cited as the third (conjugated) reconciliation row x2*(x1*x3); shown to equal the SSOT and the CH norm (+4, det=-24). Float64 reference only; NEVER on the decisive path (not imported)."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Faraut-Koranyi Ch. II-IV cited in the module docstring for the cone metric g_X=Hess(-log det) and R[h_3(O)]^{F_4}=R[Tr,Tr^2,det] (free, degrees 1/2/3) — det is the decisive degree-3 generator the engine certifies. Uniqueness not re-derived."
  forbidden_proxies:
    fp-wrong-cross-term:
      status: rejected
      notes: "The buggy (x1 x2) x3 order is evaluated locally ONLY for the contrast row; it gives Re(cross)=-4, det=-40 != CH norm (off by 16), and (per Phase 64.1) is annihilated by only 30/324 inner derivations. The decisive det_3 uses the SSOT (x2 x1) x3 (byte-identical to ring_lemma). octonion_algebra.py is NOT imported (guard confirms 0 imports)."
    fp-float-decisive:
      status: rejected
      notes: "Every verdict (LOCK 0 byte-identity, LOCK 1-5, LOCK 7a '=0?', LOCK 7b 324/324 count, the three-ordering '==CH norm?' comparisons) is exact over Q via sympy.simplify(...)==0 and sympy.Matrix; the exact_only_guard_p70 source-token scan confirms 0 numpy.linalg.matrix_rank calls. No float on the decisive path (no float used at all in this plan)."
    fp-vacuous-association:
      status: rejected
      notes: "The reconciliation runs on octonionic_points()[1] with nonzero e4..e7 content; non-vacuity is established by the FULL associator being a nonzero octonion ([0,16,12,10,2,-24,-24,0]) AND the order discriminator Re((x2 x1)x3)-Re((x1 x2)x3)=8. The real-part triple-product associator (=0 here) is recorded but explicitly NOT used as the gate (plan-check Note A)."
  uncertainty_markers:
    weakest_anchors:
      - "Stale .gpd/research/METHODS.md / PITFALLS.md call octonion_algebra.py the corrected SSOT — empirically WRONG (its (x1 x2) x3 order fails CH + 324/324). This plan follows the contract/brief; the buggy order is the rejected contrast row only."
    unvalidated_assumptions:
      - "None on the decisive path — det_3 is byte-identical to the certified v16.0 engine (sha256 e43d6a3f...) and re-certified here (LOCK 0 + 7a + 7b)."
    competing_explanations:
      - "The CONVENTIONS.md/state.json label 2Re(x2* x0* x1) vs the engine line 2Re((x2 x1) x3) is the SAME det in two index labelings (conjugated h3o_tower vs engine-native), reconciled in Task 3 (both = +4 = CH norm). Not a contradiction."
    disconfirming_observations:
      - "Would-disconfirm: LOCK 7b < 324/324 (port error) — did NOT fire (324/324). SSOT==buggy det at the test point (vacuous) — did NOT fire (-24 vs -40). The real-part triple associator being the only non-vacuity witness — correctly avoided (it is 0 at pt[1])."

comparison_verdicts:
  - subject_id: claim-engine-ssot
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: cross_method
    metric: exact_equality_over_Q
    threshold: "det_3(P) - cayley_hamilton_norm(P) == 0 at all 3 octonionic points (exact)"
    verdict: pass
    recommended_action: "Proceed to Plan 70-02 — det_3 certified the F_4-invariant generic norm (CH-norm equality + 324/324 annihilation)."
    notes: "det_3 = 3243600188173/129859329600, -24, -42 == CH norm at the 3 points; 324/324 inner derivations annihilate det_3 (dim f_4=52). Also byte-identical to ring_lemma_verification.det_3 (sha256 e43d6a3f...)."
  - subject_id: claim-cross-term-reconciled
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: cross_method
    metric: exact_equality_over_Q
    threshold: "N_SSOT == N_conj == CH norm; N_buggy != CH norm with N_SSOT - N_buggy == 16 (exact)"
    verdict: pass
    recommended_action: "fp-wrong-cross-term rejected with exact evidence; no action — buggy ordering is the contrast row only."
    notes: "At octonionic_points()[1]: SSOT/conjugated Re(cross)=+4, det==CH=-24; buggy Re(cross)=-4, det=-40 != CH; off by 16. Non-vacuous (full associator nonzero, discriminator=8)."

duration: 55 min
completed: 2026-05-30
---

# Phase 70 (A0) Plan 01: Engine Reconciliation — bulk_geometry_verification.py SSOT Certification Summary

**Certified `code/bulk_geometry_verification.py`'s `det_3` (cross-term `2Re((x2 x1) x3)`) as the unique F_4 = Aut(h_3(O))-invariant SSOT cubic norm: byte-identical verbatim copy of the v16.0 engine, equal to the Cayley-Hamilton generic norm at 3 octonionic points, annihilated by all 324 inner derivations, and discriminated from the buggy (x1 x2) x3 ordering off-by-16 — all exact over Q.**

## Performance

- **Duration:** ~55 min (most wall-clock spent resolving a directory-path mismatch in the spawn prompt and recovering from shell-batch cancellations — see Issues; the symbolic compute itself is ~3 s, LOCK 7b built 324 brackets in 0.5 s)
- **Started:** 2026-05-30T21:11:30Z
- **Completed:** 2026-05-30 (≈22:06Z)
- **Tasks:** 3 (all build the single deliverable file)
- **Files modified:** 1 created (`code/bulk_geometry_verification.py`)

## Key Results

- **det_3 byte-identical to the SSOT engine (LOCK 0):** all 13 load-bearing functions — `oct_mul, oct_conj, _oct_normsq, _coord_from_octmat, Tr, det_3, Tr2, c, polarize_d, jordan, cayley_hamilton_norm, jordan_L_matrix, inner_derivations` — are byte-for-byte identical to `code/ring_lemma_verification.py` (det_3 sha256 `e43d6a3f64eea4f8...`, 1870 chars). The SSOT guarantee holds with zero transcription drift.
- **F_4 certificate (LOCKs 7a + 7b), exact over Q:** `det_3(P) == cayley_hamilton_norm(P)` at all 3 octonionic points (det_3 = `3243600188173/129859329600`, `-24`, `-42`); and **324/324** nonzero inner derivations `[L_a, L_b]` annihilate det_3 (dim f_4 = 52). This is what certifies det_3 is the *unique* F_4-invariant generic norm (LOCKs 1-5 alone do not — the buggy order also passes them).
- **Three-ordering reconciliation (off-by-16):** at `octonionic_points()[1]`, SSOT `(x2 x1)x3` and conjugated `x2*(x1*x3)` both give `Re(cross) = +4` and `det == CH norm = -24`; the buggy `(x1 x2)x3` gives `Re(cross) = -4` and `det = -40 != CH`, with `N_SSOT - N_buggy = 16`. **`fp-wrong-cross-term` rejected with exact evidence.**
- **Associator gap:** the full triple-product associator at the test point is `(x1 x2)x3 - x1(x2 x3) = [0, 16, 12, 10, 2, -24, -24, 0]` (a nonzero octonion → genuinely non-associative data). The association-*order* discriminator `Re((x2 x1)x3) - Re((x1 x2)x3) = 8`, which propagates to the `2*Re(cross)` det term as the `±4 → 16` cross-term gap.
- **ALL_PASS, exit 0, deterministic:** two consecutive runs are byte-identical; no `[FAIL]` line; the fence-free exact-only guard confirms 0 `octonion_algebra` imports and 0 `numpy.linalg.matrix_rank` calls on the decisive path.

## Task Commits

All three tasks build the single deliverable `code/bulk_geometry_verification.py`; committed as one atomic, fully-certified unit:

1. **Tasks 1+2+3 (certified engine):** `eb261773` (calc) — verbatim copy + LOCKs 1-5/LAYOUT/guard (Task 1), LOCK 7a/7b F_4 certificate (Task 2), three-ordering reconciliation (Task 3).

**Plan metadata:** committed separately (this SUMMARY).

## Files Created/Modified

- `code/bulk_geometry_verification.py` — the Phase-70 exact-SymPy-over-Q cubic-norm SSOT engine. Sections 1-3 copied verbatim from `ring_lemma_verification.py`; a new `main()` re-runs the full LOCK harness (LOCK 0 byte-identity, LOCKs 1-5, LAYOUT, fence-free guard, LOCK 7a/7b) and the three-ordering reconciliation. Runnable: `python3 code/bulk_geometry_verification.py` (exit 0 iff ALL_PASS).

## Validations Completed

- **Verbatim-copy byte-identity** (LOCK 0 + offline `inspect.getsource` sha256 match `e43d6a3f...`): det_3 and 12 dependencies identical to source. ✓
- **Algebraic grading** (the "dimensional" check for this pure-algebra phase): det_3 homogeneous degree 3, Tr degree 1, Tr2 degree 2, polarize_d degree 3 with `d(X,X,X)=6 det_3` (LOCK 1). ✓
- **Limiting/special values:** `det_3(diag(a,b,c)) = abc` (symbolic), `det_3(I) = 1`, `c(X,X) = Tr(X^2)`, Fano `e1 e2 = e4`. ✓
- **F_4 invariance** (the decisive cross-check): CH-norm equality at 3 octonionic points + 324/324 inner-derivation annihilation, exact over Q. ✓
- **Cross-method discrimination:** three orderings vs the Cayley-Hamilton norm — SSOT/conjugated agree (+4=CH=-24), buggy disagrees (-4, det=-40, off by 16). ✓
- **Reproducibility / determinism:** two runs byte-identical; SymPy 1.14.0, Python 3.14.2, NumPy 2.4.x, macOS Darwin 24.6.0; hardcoded test points, no random seeds. ✓

## Equations / Quantities Verified

| Quantity | Value | Source |
|---|---|---|
| det_3 at octonionic_points()[0] | 3243600188173/129859329600 | LOCK 7a (== CH norm) |
| det_3 at octonionic_points()[1] | -24 | LOCK 7a (== CH norm) |
| det_3 at octonionic_points()[2] | -42 | LOCK 7a (== CH norm) |
| inner-derivation annihilation count | 324/324 | LOCK 7b (dim f_4 = 52) |
| Re(cross) SSOT / conjugated / buggy at pt[1] | +4 / +4 / -4 | Task 3 reconciliation |
| N_SSOT / N_conj / N_buggy at pt[1] | -24 / -24 / -40 | Task 3 reconciliation |
| N_SSOT - N_buggy (off-by) | 16 | Task 3 reconciliation |
| full associator (x1 x2)x3 - x1(x2 x3) at pt[1] | [0,16,12,10,2,-24,-24,0] | non-vacuity (i) |
| order discriminator Re((x2 x1)x3)-Re((x1 x2)x3) | 8 | non-vacuity (ii) |
| det_3 source sha256 (== ring_lemma) | e43d6a3f64eea4f8... | LOCK 0 byte-identity |

## Decisions Made

- **Verbatim region as a single contiguous slice:** extracted source lines `import sys` → end of `inner_derivations()` (everything except the leading docstring and trailing `main()`), guaranteeing every required function is byte-identical without fragile multi-range splicing. The header docstring and a fresh `main()` were appended around it; the verbatim region was never hand-edited. Confirmed by sha256 (`e43d6a3f...`).
- **Fence-free exact-only guard (Deviation Rule 4):** the copied `exact_only_guard()` hard-codes `oa_imports_in_fence == 1` (it expected the v16.0 oracle fence). This module deliberately drops the octonion_algebra touch entirely (Open Question 2). Rather than edit the verbatim guard (which would break byte-identity), added `exact_only_guard_p70()` that re-uses the verbatim source-token scan and requires `in-fence == 0`. The security property (no octonion_algebra, no float rank) is unchanged — only the expected in-fence count.
- **Non-vacuity predicate (plan-check Note A):** used the FULL associator (nonzero octonion) AND the order discriminator (=8), NOT the real-part triple-product associator (=0 at pt[1]). The latter is recorded for transparency but explicitly not used as the gate.

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 4 - Missing Component] Fence-free exact-only guard wrapper**

- **Found during:** Task 1 (running the copied `exact_only_guard()` — it returned FAIL on the first harness run).
- **Issue:** The verbatim guard requires exactly 1 sanctioned `octonion_algebra` import inside an oracle fence (`oa_imports_in_fence == 1`), but the plan (Task 1 step 4 / Open Question 2) directs dropping the oracle fence entirely, so this module has 0 such imports. The guard's own diagnostic confirmed the module is actually clean (`0 in-fence + 0 outside; float-rank 0`).
- **Fix:** Added `exact_only_guard_p70()` that re-uses the verbatim guard's exact source-token scan and asserts the stricter fence-free condition (`in-fence == 0`). Kept `exact_only_guard()` byte-identical (it is part of the SSOT copy).
- **Files modified:** code/bulk_geometry_verification.py
- **Verification:** `exact_only_guard_p70()` PASS with detail "0 in-fence + 0 outside; float-rank calls: 0".
- **Committed in:** eb261773

**2. [Rule 4 - Missing Component] Added LOCK 0 verbatim-copy integrity check**

- **Found during:** Task 1 (standing up the copied module).
- **Issue:** The plan/contract requires the new det_3 be byte-identical to the source (the SSOT guarantee), but the plan did not specify a runtime check for it.
- **Fix:** Added `verbatim_copy_integrity()` (LOCK 0) asserting via `inspect.getsource` that det_3 + 12 dependencies match `ring_lemma_verification` exactly. Non-decisive if the source is unimportable (the F_4 certificate is the decisive proof regardless).
- **Files modified:** code/bulk_geometry_verification.py
- **Verification:** LOCK 0 PASS; offline sha256 of det_3 source matches (e43d6a3f...).
- **Committed in:** eb261773

---

**Total deviations:** 2 auto-fixed (both Rule 4 — correctness additions). No scope creep; both strengthen the SSOT guarantee the contract demands.

## Issues Encountered

- **Spawn-prompt directory path mismatch (resolved):** the prompt's `<files_to_read>` and `<objective>` named the phase dir `70-engine-reconciliation-signature-bridge`, but the actual on-disk directory (and the path in the PLAN frontmatter) is `70-a0-engine-reconciliation-signature-bridge` (with the `a0-` segment). Initial reads failed with "file does not exist"; resolved by locating the real directory via `find .gpd -name '*70*'`. The plan, plan-check, and research files were then read from the correct path. No physics impact.
- **Shell-batch cancellations / stale temp files (resolved):** several parallel tool batches were cancelled mid-flight (one bad call in a batch cancels the rest), which (a) deleted an intermediate `/tmp` verbatim file that had to be re-extracted, and (b) caused an earlier harness run against an OLD version of `main()` (with a `TypeError` on a sympy `Integer` format spec and the unfixed `exact_only_guard()`). Recovered by re-extracting the verbatim region, rewriting `main()` (fixed the table formatting with `str().rjust()` and the fence-free guard), re-assembling, and re-running to a clean ALL_PASS. The committed file is the corrected version; the broken intermediate was never committed.
- **Numbers corrected before SUMMARY commit:** the det_3 values at points [0] and [2] were initially mis-transcribed in a draft (guessed `5847/4400`, `581/40`); the actual computed values are `3243600188173/129859329600` and `-42`, now correct throughout. Point [1] = -24 was confirmed against the source engine from the start.

## Open Questions

- None blocking. The certified engine is ready for Plan 70-02 (signature bridge: `g_mu_nu(x) = eta_mu_nu + h_mu_nu(x)` via construction (ii); Hessian benchmark `diag(9,9,18,18)`/det 26244; H^3 constant curvature −1). Plan-check Note B (the Minkowski-reduction gate is tautological-by-construction; lean on the Hessian benchmark + index map for the real anti-contamination content) is a 70-02 concern, flagged for that plan's executor.

## Next Phase Readiness

`code/bulk_geometry_verification.py` is the certified single-source-of-truth cubic-norm engine for the entire v17.0 milestone. Every downstream curvature (g_X = Hess(−log det), Totaro Riemann) is now guaranteed to be built from a correct, F_4-invariant det. **Plan 70-02 consumes this module** for the signature bridge and the H^3 curvature benchmark. The A0 gate (SETU-01) is satisfied.

---

## Self-Check: PASSED

- `code/bulk_geometry_verification.py` exists on disk and is git-tracked (EXISTS_IN_HEAD). ✓
- `.gpd/phases/70-a0-engine-reconciliation-signature-bridge/70-01-SUMMARY.md` exists. ✓
- Commit `eb261773` present in `git log` (the engine commit). ✓
- Key result reproduces: `python3 code/bulk_geometry_verification.py` → ALL_PASS, exit 0, deterministic (run1 == run2). ✓
- Convention consistency: decisive det_3 uses SSOT `(x2 x1) x3`; buggy `(x1 x2) x3` appears only in the reconciliation contrast row + associator. ✓
- Contract coverage: all claim / deliverable / acceptance-test / reference / forbidden-proxy IDs covered; 2 comparison_verdicts (both `pass`). ✓

## Validation: PASSED

- Algebraic grading (det_3 deg 3, Tr deg 1, Tr2 deg 2, polarize_d deg 3 with d=6 det_3). ✓
- F_4 invariance certificate exact over Q: CH-norm equality at 3 octonionic points + 324/324 inner-derivation annihilation. ✓
- Cross-method discrimination (three orderings vs CH norm; SSOT/conjugated agree, buggy off by 16). ✓
- Byte-identity of det_3 to the certified v16.0 SSOT engine (sha256 e43d6a3f...). ✓

---

_Phase: 70-a0-engine-reconciliation-signature-bridge_
_Completed: 2026-05-30_
