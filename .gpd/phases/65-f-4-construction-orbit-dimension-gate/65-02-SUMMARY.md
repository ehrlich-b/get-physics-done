---
phase: 65-f-4-construction-orbit-dimension-gate
plan: 02
depth: full
one-liner: "COMPUTED the single-copy generic orbit dimension of F_4 on h_3(O) as the EXACT rank over QQ of the (f_4-generators x 27) infinitesimal-action matrix (rows M.v) at 3 generic INTEGER octonionic points (rank 24 at each, MAX 24); asserted the builder GATE orbit 24 / stabilizer 52-24=28=dim Spin(8) / single-state trdeg 27-24=3, reproducing the Garibaldi-Guralnick/Lawther anchor IN-ENGINE (NOT looked up) -- the Plan-01 f_4 builder is CERTIFIED = Der(h_3(O)) and the pair value (Plan 03) may now be computed"
subsystem: [formalism, validation, computation]
tags: [jordan-algebra, albert-algebra, f4, exceptional-lie-algebra, orbit-dimension, invariant-theory, exact-symbolic, octonions, garibaldi-guralnick, spin8, transcendence-degree]

requires:
  - phase: 65-f-4-construction-orbit-dimension-gate
    plan: 01
    provides: "f_4 = Der(h_3(O)) as the 52-dim span of 324 inner derivations {[L_a,L_b]} (27x27 over Q), dim f_4 = 52 COMPUTED, bracket-closed, infinitesimal F_4-invariance certified for {Tr,Tr^2,det_3}; cached_L_matrices() + E.inner_derivations() in code/orbit_dimension_gate.py"
  - phase: 64-setup-conventions-and-exact-engine
    provides: "Frozen exact-SymPy h_3(O) engine code/ring_lemma_verification.py (X_from_symbols / _flat27 / _coord_from_octmat / octonionic_points, jordan=(1/2)(AB+BA), Phase-64.1 corrected det_3, 27-per-copy layout)"
provides:
  - "Single-copy generic orbit dimension of F_4 on h_3(O) = 24, COMPUTED as the exact rank over QQ of the (52-independent-f_4-basis x 27) infinitesimal-action matrix (rows M.v) at 3 generic INTEGER octonionic points (MAX of 24,24,24 = 24)"
  - "Single-copy stabilizer dim = 52 - 24 = 28 = dim Spin(8) (the Garibaldi-Guralnick generic stabilizer)"
  - "Single-state transcendence degree = 27 - 24 = 3 (= R[Tr, Tr^2, det], degrees 1/2/3; Faraut-Koranyi II-IV, Phase 64)"
  - "Garibaldi-Guralnick / Lawther single-copy anchor (orbit 24 / Spin(8) 28 / trdeg 3) REPRODUCED in-engine -> the Plan-01 f_4 builder is CERTIFIED = Der(h_3(O)) (the RIGHT 52-dim algebra acting correctly, not merely 52-dim)"
  - "HARD GATE backtracking wired in code/orbit_dimension_gate.py: orbit_dim != 24 -> builder broken, pair value (Plan 03) must NOT be computed"
  - "Reusable single-copy recipe carried to Plan 03: generic INTEGER point, substitute-the-point-FIRST, matrix*vector tangents M.v, exact QQ rank; 52-independent f_4 basis selection (exact rref over QQ) for speed"
affects: ["Phase 65 Plan 03 (pair orbit dimension; 54 - orbit_dim = 7 GATE -- now unblocked, builder CERTIFIED)", "Phase 66 (the (b) SPINE: c independence; the orbit-derivative route reuses this infinitesimal-action machinery)"]

methods:
  added: ["exact single-copy orbit-dimension computation = rank over QQ of the (generators x 27) infinitesimal-action matrix M.v at a generic INTEGER point (Derksen-Kemper char-0)", "MAX-over-sampled-points reading of a lower-semicontinuous generic rank", "52-independent f_4 basis selection via exact rref over QQ (basis rank == spanning-set rank under M.v)"]
  patterns: ["substitute the generic INTEGER point into the coordinate vector BEFORE forming the tangent matrix (entries become exact integers; no symbolic expression swell)", "rank a 52-element f_4 basis (not all 324 generators) for the single-copy rank -- same row space, ~2-3x faster", "define the generic integer octonionic sample points EXPLICITLY in-module (not via engine internals) so the GATE's genericity is self-contained and auditable"]

key-files:
  created: []
  modified: ["code/orbit_dimension_gate.py"]

key-decisions:
  - "COMPUTED the single-copy orbit dimension as the exact QQ rank of the infinitesimal-action matrix at 3 generic integer octonionic points; the literature value 24 (Garibaldi-Guralnick) is a CONFIRMATION target only, never the source of truth (forbidden proxy fp-skip-single-copy-gate / Spin(8)-triality back-of-envelope rejected)"
  - "Used a 52-independent f_4 basis (selected by exact rref over QQ on the 324x729 row-flattened generators) for the per-point rank instead of all 324 generators: the row space under M.v is identical, so the rank is unchanged, and it runs ~2-3x faster per point (planner-measured ~47s/basis vs ~130s/full-324)"
  - "Defined the >=2 generic INTEGER octonionic sample points EXPLICITLY in the module (SINGLE_COPY_POINTS: planner-spike P1 + two independent integer points P2/P3) rather than depending on the engine's octonionic_points(), so the GATE's genericity claim is self-contained and auditable; each point validated integer + >=2 nonzero imaginary comps per off-diagonal octonion + distinct diagonal"
  - "Both Plan-02 tasks (Task 1 orbit-rank computation, Task 2 GATE assertions) landed in the SAME inseparable assert-harness file -> one atomic commit (778871af); the orbit-rank functions and the GATE assertions read each other's results in one main() flow, so splitting would require an artificial broken-intermediate commit (same single-file precedent as Plan 01)"

patterns-established:
  - "Pattern: single-copy orbit dimension = exact rank over QQ of the (f_4-generators x 27) matrix whose rows are M.v (matrix*vector), integer point substituted FIRST; trdeg = 27 - orbit_dim; stabilizer = dim f_4 - orbit_dim (Derksen-Kemper char-0)"
  - "Pattern: report the MAX rank over >=2 generic integer points (rank is lower-semicontinuous -- it can only DROP on special loci, so the generic value is the max over sampled points)"

conventions:
  - "arithmetic = exact SymPy over Q (Rational/QQ); NO float64 / NO numpy.linalg.matrix_rank on the decisive path"
  - "ranks via sympy.Matrix(...).rank() over QQ; rref via sympy .rref() over QQ"
  - "jordan product X o Y = (1/2)(XY + YX); octonion table Fano e1 e2 = e4; det_3 generic norm cross 2 Re((x2 x1) x3) (Phase-64.1 corrected; frozen engine E.det_3 -- not touched here, no octonion_algebra.py)"
  - "f_4 = span{[L_a,L_b]} (E.inner_derivations(), 324 nonzero, dim 52 -- Plan 01)"
  - "single-copy infinitesimal action: f_4 acting on ONE copy of h_3(O); the xi-th orbit-tangent row is M_xi . v (matrix*vector), v = _flat27(X*); orbit_dim = rank over QQ of the (generators x 27) tangent matrix at a generic INTEGER point (substituted BEFORE the rank)"
  - "coordinatization: engine-native 27-per-copy layout [alpha,beta,gamma, x1(8), x2(8), x3(8)] via X_from_symbols / _flat27 / _standard_basis_27"
  - "Derksen-Kemper char-0: generic orbit dim = rank of the infinitesimal action at a generic point; trdeg of the invariant field = ambient dim - orbit dim (single copy: 27 - orbit_dim)"

plan_contract_ref: ".gpd/phases/65-f-4-construction-orbit-dimension-gate/65-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-single-copy-orbit-24:
      status: passed
      summary: "The generic single-copy orbit dimension of F_4 on h_3(O) is EXACTLY 24, COMPUTED as the rank over QQ of the infinitesimal-action matrix (rows M.v over a 52-independent f_4 basis, v = _flat27(X*) the flattened coordinates) at 3 generic INTEGER octonionic points; rank == 24 at P1 (planner spike), P2, P3 (each independent generic integer point); MAX = 24 (rank lower-semicontinuous). Integer point substituted BEFORE the rank (entries exact integers). NOT looked up."
      linked_ids: [deliv-single-copy-rank, test-single-copy-24, test-single-copy-multipoint, ref-engine, ref-garibaldi-guralnick, ref-derksen-kemper]
      evidence:
        - verifier: gpd-executor
          method: exact rank over QQ of the (52-basis x 27) infinitesimal-action matrix M.v at 3 generic integer octonionic points, MAX taken
          confidence: high
          claim_id: claim-single-copy-orbit-24
          deliverable_id: deliv-single-copy-rank
          acceptance_test_id: test-single-copy-24
          reference_id: ref-garibaldi-guralnick
          evidence_path: "code/orbit_dimension_gate.py"
    claim-single-copy-stabilizer-trdeg:
      status: passed
      summary: "The single-copy stabilizer dimension is 52 - 24 = 28 = dim Spin(8) (the Garibaldi-Guralnick generic stabilizer), and the single-state transcendence degree is 27 - 24 = 3 (= R[Tr, Tr^2, det], degrees 1/2/3, confirmed in Phase 64). The Garibaldi-Guralnick / Lawther single-copy anchor is REPRODUCED in-engine; the Plan-01 f_4 builder is therefore CERTIFIED = Der(h_3(O)) and the pair value (Plan 03) may now be computed. HARD GATE: orbit != 24 fails the harness and forbids Plan 03."
      linked_ids: [deliv-single-copy-gate, test-stabilizer-28, test-trdeg-3, ref-garibaldi-guralnick, ref-faraut-koranyi]
      evidence:
        - verifier: gpd-executor
          method: exact integer arithmetic on the COMPUTED orbit_dim (52-24==28==dim Spin(8); 27-24==3)
          confidence: high
          claim_id: claim-single-copy-stabilizer-trdeg
          deliverable_id: deliv-single-copy-gate
          acceptance_test_id: test-stabilizer-28
          reference_id: ref-garibaldi-guralnick
          evidence_path: "code/orbit_dimension_gate.py"
  deliverables:
    deliv-single-copy-rank:
      status: passed
      path: code/orbit_dimension_gate.py
      summary: "single_copy_orbit_rank(derivs, v27): forms the (generators x 27) tangent matrix whose row for each f_4 generator M is M . Matrix(v27) (matrix*vector), integer point substituted first, and returns the exact rank over QQ. _select_independent_basis() picks a 52-independent f_4 basis via exact rref over QQ. check_single_copy_orbit_dim() evaluates at 3 generic integer octonionic points (SINGLE_COPY_POINTS) and takes the MAX = 24. must_contain {rank, _flat27, 24} all present."
      linked_ids: [claim-single-copy-orbit-24, test-single-copy-24, test-single-copy-multipoint]
    deliv-single-copy-gate:
      status: passed
      path: code/orbit_dimension_gate.py
      summary: "check_single_copy_gate(orbit_dim): asserts orbit_dim == 24, stabilizer 52 - orbit_dim == 28 (records 28 = dim Spin(8)), trdeg 27 - orbit_dim == 3 (records = R[Tr,Tr^2,det]); records the Garibaldi-Guralnick/Lawther anchor reproduction and the f_4-builder certification. main() wires the STOP-if-not-24 HARD GATE (sets ORBIT_DIM_SINGLE = 24 only on PASS; prints GATE-FAIL + forbids Plan 03 otherwise). must_contain {28, Spin(8), trdeg} all present."
      linked_ids: [claim-single-copy-stabilizer-trdeg, test-stabilizer-28, test-trdeg-3]
  acceptance_tests:
    test-single-copy-24:
      status: passed
      summary: "Single-copy orbit rank over QQ == 24 at the first generic integer octonionic point P1 = [1,-2,3, 1,0,-1,2,0,1,0,-1, 0,2,0,-1,1,0,1,1, 0,-1,1,0,2,-1,1,0] (planner spike; diag (1,-2,3), x1/x2/x3 with imag comps {2,3,5,7}/{1,3,4,6,7}/{1,2,4,5,6}). Tangent matrix M.v over the 52-independent f_4 basis, integer point substituted before the rank. rank == 24 EXACTLY. (Cross-checked: the full 324-row spanning set gives the SAME rank 24 -- prototype, ~130s.)"
      linked_ids: [claim-single-copy-orbit-24, deliv-single-copy-rank, ref-engine, ref-garibaldi-guralnick]
    test-single-copy-multipoint:
      status: passed
      summary: "MAX single-copy orbit rank over QQ == 24 across 3 generic integer octonionic points (P1=24, P2=24, P3=24; MAX=24); no point gives a rank larger than 24. P2 = diag (2,1,-3) and P3 = diag (-1,4,2), each independent and genuinely octonionic (>=4 nonzero imaginary comps per off-diagonal octonion). Rank lower-semicontinuous -> the generic orbit dim is the max over sampled points = 24."
      linked_ids: [claim-single-copy-orbit-24, deliv-single-copy-rank, ref-derksen-kemper]
    test-stabilizer-28:
      status: passed
      summary: "stabilizer dim = dim f_4 - orbit_dim = 52 - 24 == 28 == dim Spin(8) (the Garibaldi-Guralnick generic stabilizer). Exact integer arithmetic on the COMPUTED orbit_dim."
      linked_ids: [claim-single-copy-stabilizer-trdeg, deliv-single-copy-gate, ref-garibaldi-guralnick]
    test-trdeg-3:
      status: passed
      summary: "single-state trdeg = 27 - orbit_dim = 27 - 24 == 3 (matches the single-state ring R[Tr, Tr^2, det], degrees 1/2/3, confirmed in Phase 64; Faraut-Koranyi II-IV). Exact integer arithmetic on the COMPUTED orbit_dim."
      linked_ids: [claim-single-copy-stabilizer-trdeg, deliv-single-copy-gate, ref-faraut-koranyi]
  references:
    ref-engine:
      status: completed
      completed_actions: [read, use]
      missing_actions: []
      summary: "code/ring_lemma_verification.py (frozen engine) + code/orbit_dimension_gate.py Plan-01 REUSED verbatim: E.inner_derivations() (the 324 f_4 generators, dim 52 from Plan 01), E.X_from_symbols / E._flat27 / E._coord_from_octmat (27-per-copy layout), the single-copy tangents M.v reuse the SAME generators built in Plan 01. No f_4 rebuilt; no octonion arithmetic re-derived."
    ref-garibaldi-guralnick:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Garibaldi-Guralnick (arXiv:2308.08214), corroborated Lawther (arXiv:1508.02918): F_4 on 26 -> generic stabilizer Spin(8) dim 28, orbit 24, trdeg 3. THE single-copy anchor; orbit 24 / stab Spin(8) (28) / trdeg 3 REPRODUCED in-engine (COMPUTED, NOT assumed). The match certifies the f_4 builder = Der(h_3(O)). PDF not directly quotable (standard-fact status + Lawther corroboration + in-engine reproduction is the decisive evidence)."
    ref-derksen-kemper:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Derksen-Kemper (Computational Invariant Theory, Sec 4) char-0 criterion USED: generic orbit dim = rank of the infinitesimal action at a generic point; trdeg = ambient dim - orbit dim. Justifies computing orbit_dim as the exact QQ rank of M.v at a generic point, the MAX-over-points reading (lower-semicontinuity), and trdeg = 27 - orbit_dim."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Faraut-Koranyi (Analysis on Symmetric Cones, Ch. II-IV) cited: the single-state ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] has trdeg 3 -- exactly the 27 - 24 = 3 read off here. Ch. II-IV (the Ch. V -> II-IV correction recorded in Phase 64)."
  forbidden_proxies:
    fp-float-rank:
      status: rejected
      notes: "All ranks computed via sympy.Matrix(...).rank() over QQ (and the basis via .rref() over QQ); the integer point is substituted FIRST so the tangent matrix is integer-valued. numpy is never imported in the module; the exact-only source guard asserts 0 np.linalg / numpy.linalg float-rank live calls on the decisive path (passes). A float SVD tolerance would fabricate the 24 verdict (rank is discontinuous)."
    fp-rank-before-substitution:
      status: rejected
      notes: "The generic INTEGER point is substituted into the coordinate vector v = Matrix(v27) BEFORE the tangent matrix M.v is formed (the f_4 generators are already numeric), so the (generators x 27) matrix is integer-valued and ranked over QQ directly. No symbolic 27-variable tangent matrix is ever built or simplify()-ed (that stalls on expression swell)."
    fp-skip-single-copy-gate:
      status: rejected
      notes: "The single-copy orbit-24 / Spin(8) check is COMPUTED and asserted as the builder GATE (Tasks 3+4), NOT skipped; dim 52 alone (Plan 01) is explicitly NOT treated as builder correctness. The literature value 24 is a CONFIRMATION target only -- the rank comes out of the engine. The naive Spin(8)-triality back-of-envelope (the three 8's permuted by triality) is the trap this GATE avoids by computing the rank."

comparison_verdicts:
  - subject_id: claim-single-copy-orbit-24
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-garibaldi-guralnick
    comparison_kind: benchmark
    metric: exact_integer_equality
    threshold: "== 24"
    verdict: pass
    recommended_action: "Treat the f_4 builder as CERTIFIED; carry ORBIT_DIM_SINGLE = 24 + the single-copy recipe to Plan 03 (pair orbit value; consistency anchor 54 - pair_orbit_dim = 7)."
    notes: "COMPUTED single-copy orbit dim = exact QQ rank 24 (MAX over 3 generic integer octonionic points) matches the Garibaldi-Guralnick / Lawther anchor (orbit 24, generic stabilizer Spin(8) dim 28, trdeg 3). The match is an in-engine REPRODUCTION; 24 was COMPUTED, not assumed (fp-skip-single-copy-gate rejected)."
  - subject_id: claim-single-copy-stabilizer-trdeg
    subject_kind: claim
    subject_role: decisive
    reference_id: ref-garibaldi-guralnick
    comparison_kind: benchmark
    metric: exact_integer_equality
    threshold: "52 - orbit_dim == 28 == dim Spin(8); 27 - orbit_dim == 3"
    verdict: pass
    recommended_action: "Builder CERTIFIED; Plan 03 (pair orbit dimension) is unblocked."
    notes: "stabilizer 52 - 24 = 28 = dim Spin(8) and single-state trdeg 27 - 24 = 3 (= R[Tr, Tr^2, det], Faraut-Koranyi II-IV) both reproduce the Garibaldi-Guralnick anchor exactly. Confirmation, computed from the in-engine orbit_dim."

duration: ~75 min (wall-clock; compute is exact-QQ-rank-bound -- 3 single-copy ranks ~20-110s each + the full Plan-01+02 harness ~5 min)
completed: 2026-05-25
---

# Phase 65 Plan 02: Single-Copy Orbit-Dimension GATE Summary

**COMPUTED the single-copy generic orbit dimension of F_4 on h_3(O) as the EXACT rank over QQ of the (f_4-generators x 27) infinitesimal-action matrix (rows M.v, matrix*vector) at 3 generic INTEGER octonionic points (rank 24 at each, MAX 24), and asserted the builder-correctness GATE orbit 24 / stabilizer 52-24=28=dim Spin(8) / single-state trdeg 27-24=3 -- reproducing the Garibaldi-Guralnick/Lawther single-copy anchor IN-ENGINE (NOT looked up). The Plan-01 f_4 builder is CERTIFIED = Der(h_3(O)); the pair value (Plan 03) may now be computed.**

## Performance

- **Duration:** ~75 min wall-clock (compute is exact-QQ-rank-bound: the 3 single-copy ranks ~20-110s each + the full Plan-01+02 harness ~5 min; the rest is exact-rank computation, not idle)
- **Started:** 2026-05-25T21:27:05Z
- **Completed:** 2026-05-25T22:42:28Z
- **Tasks:** 2 (Task 1 orbit-rank computation, Task 2 GATE assertions; both in one inseparable harness file)
- **Files modified:** 1 (`code/orbit_dimension_gate.py`)

## Key Results

- **Single-copy generic orbit dimension = 24, COMPUTED over Q** (not looked up): the exact rank over QQ of the (52-independent-f_4-basis x 27) infinitesimal-action matrix, whose row for each generator M is M . v (matrix*vector), v = `_flat27(X*)` the flattened single-copy coordinates. rank == 24 at all 3 generic integer octonionic points; **MAX(24, 24, 24) = 24**. The full 324-row spanning set gives the SAME rank 24 (prototype cross-check, ~130s). [CONFIDENCE: HIGH]
- **Single-copy stabilizer dimension = 52 - 24 = 28 = dim Spin(8)** -- the Garibaldi-Guralnick generic stabilizer. [CONFIDENCE: HIGH]
- **Single-state transcendence degree = 27 - 24 = 3** -- matches the single-state ring R[Tr, Tr^2, det] (degrees 1/2/3), Faraut-Koranyi II-IV, confirmed in Phase 64. [CONFIDENCE: HIGH]
- **Garibaldi-Guralnick / Lawther single-copy anchor REPRODUCED in-engine** (orbit 24 / Spin(8) 28 / trdeg 3) -> the Plan-01 f_4 builder is CERTIFIED to be Der(h_3(O)) = f_4 (the RIGHT 52-dim algebra acting correctly, not merely 52-dimensional). This is the precondition for the pair orbit value (Plan 03). [CONFIDENCE: HIGH]
- **HARD GATE backtracking wired:** if orbit_dim != 24 the harness prints `[GATE-FAIL]` and forbids Plan 03; `ORBIT_DIM_SINGLE` is set to 24 only on a PASS (carried forward to Plan 03). NONE of the disconfirming observations (orbit 23/25, or a point-to-point rank disagreement) fired.

## Task Commits

Both tasks landed in a single inseparable assert-harness file (see Deviations):

1. **Task 1 (single-copy orbit rank, exact QQ, 3 integer points) + Task 2 (GATE assertions orbit 24 / Spin(8) 28 / trdeg 3)** - `778871af` (verify)

**Plan metadata:** committed with this SUMMARY.

## Files Created/Modified

- `code/orbit_dimension_gate.py` - Extended the Plan-01 builder module with the Plan-02 single-copy orbit-dimension GATE: `single_copy_orbit_rank()` (exact QQ rank of the M.v tangent matrix at an integer point), `_select_independent_basis()` (52-independent f_4 basis via exact rref over QQ), `_is_genuinely_octonionic_integer()` (point validator), `check_single_copy_orbit_dim()` (3 generic integer points, MAX = 24), `check_single_copy_gate()` (orbit 24 / Spin(8) 28 / trdeg 3 assertions + anchor record), and the `main()` wiring with the STOP-if-not-24 HARD GATE. Assert-harness, exits 0.

## Equations Derived / Verified

**Eq. (65.5) — single-copy infinitesimal action (orbit tangent):**

For an f_4 generator M (a 27x27 rational matrix, M in span{[L_a,L_b]}) and a single-copy point with coordinate vector v = _flat27(X*), the orbit tangent is

$$ \delta_M v \;=\; M \, v \qquad (\text{matrix} \times \text{vector}, \ \text{a 27-vector over } \mathbb{Q}) $$

**Eq. (65.6) — single-copy orbit dimension (Derksen-Kemper char-0):**

$$ \dim \mathcal{O}(X^\ast) \;=\; \operatorname{rank}_{\mathbb{Q}}\, \big[\, M_\xi \, v \,\big]_{\xi=1\ldots\dim\mathfrak{f}_4} \;=\; 24 \qquad (v = \_\mathrm{flat27}(X^\ast),\ X^\ast\ \text{generic integer octonionic}) $$

evaluated at >=2 generic integer points and MAX-ed (rank lower-semicontinuous).

**Eq. (65.7) — stabilizer and transcendence degree (the GATE):**

$$ \dim \mathrm{Stab}(X^\ast) \;=\; \dim\mathfrak{f}_4 - \dim\mathcal{O} \;=\; 52 - 24 \;=\; 28 \;=\; \dim \mathrm{Spin}(8), \qquad \operatorname{trdeg}\,\mathbb{R}[h_3(\mathbb{O})]^{F_4} \;=\; 27 - 24 \;=\; 3 $$

## Validations Completed

- **Single-copy orbit rank = 24 over QQ** at P1 (planner spike) -- `sympy.Matrix(...).rank()`; cross-checked that the FULL 324-row spanning set gives the SAME rank 24 (prototype, ~130s) as the 52-independent basis (~47s), confirming the basis-rank == spanning-set-rank reduction is sound.
- **MAX over 3 generic integer octonionic points = 24** (P1=24, P2=24, P3=24); no point exceeds 24 (lower-semicontinuity satisfied).
- **Point genericity validated**: each of P1/P2/P3 is integer-valued, has distinct diagonal entries (non-degenerate), and carries >=4 nonzero imaginary (e_1..e_7) components in each off-diagonal octonion (genuinely octonionic, NOT on the real/commutative subalgebra).
- **Basis re-confirms dim f_4 = 52**: the exact rref over QQ selects exactly 52 independent generators from the 324.
- **Stabilizer 28 = dim Spin(8)** and **trdeg 3 = R[Tr, Tr^2, det]** -- exact integer arithmetic on the computed orbit_dim, both matching the Garibaldi-Guralnick / Faraut-Koranyi anchors.
- **exact-only guard** self-check: 0 octonion_algebra imports, 0 numpy float-rank live calls on the decisive path. The frozen engine's corrected det_3 is reused via E (Plan 01); no float64 path touched.
- **Full harness exits 0** (ALL_PASS) -- every Plan-01 check (re-run) AND every Plan-02 check passes.

## Key Quantities

| Quantity | Symbol | Value | Uncertainty | Source | Valid Range |
| --- | --- | --- | --- | --- | --- |
| Single-copy orbit dimension | dim O | 24 | exact (integer) | MAX exact QQ rank of M.v at 3 generic integer octonionic points | h_3(O), generic point |
| Single-copy stabilizer dimension | dim Stab | 28 | exact (integer) | 52 - 24; = dim Spin(8) | h_3(O), generic point |
| Single-state transcendence degree | trdeg | 3 | exact (integer) | 27 - 24; = R[Tr,Tr^2,det] | h_3(O), exact |
| f_4 dimension (Plan 01, reused) | dim f_4 | 52 | exact (integer) | span rank over QQ (Plan 01) | h_3(O), exact |
| Independent-basis pivot count | \|basis\| | 52 | exact (integer) | exact rref over QQ of 324x729 | re-confirms dim 52 |
| Rank at P1 / P2 / P3 | rank | 24 / 24 / 24 | exact | exact QQ rank, 52-basis tangents | 3 generic integer points |

## Uncertainty Budget

All results are EXACT integers from finite linear algebra over Q -- there is no meaningful numerical uncertainty. The orbit dimension is an exact `sympy.Matrix.rank()` over QQ of an integer matrix (the generic integer point is substituted before the rank, so all entries are exact integers); the stabilizer (52-24) and trdeg (27-24) are exact integer differences. The only methodological subtlety is genericity of the sampled point: handled by (a) sampling >=2 independent generic integer octonionic points and taking the MAX (rank is lower-semicontinuous, so the generic value is the max over samples), and (b) validating each point is genuinely octonionic and non-degenerate. No small parameter, no truncation, no convergence, no tolerance.

## Limiting Cases Verified

- **Garibaldi-Guralnick / Lawther anchor** (orbit 24 / generic stabilizer Spin(8) dim 28 / trdeg 3): REPRODUCED exactly in-engine (the decisive cross-check; the literature value is a confirmation target, the rank was COMPUTED).
- **Faraut-Koranyi single-state ring** R[Tr, Tr^2, det] (trdeg 3, degrees 1/2/3): matches the 27 - 24 = 3 read off here.
- **Consistency with Plan 01** dim f_4 = 52: the independent-basis selection re-confirms exactly 52 generators.

## Validation Events

None triggered as failures. The first-result sanity gate (single-copy rank == 24 at the planner-spike point) was checked FIRST in a standalone prototype before the GATE assertions were written; it passed (rank 24, exact QQ, ~130s full 324-row), so no BACKTRACK fired. All three disconfirming-observation STOP conditions (orbit 23/25; point-to-point rank disagreement with MAX != 24; non-generic sampled point) were checked and NONE fired.

## Approximations Used

None. Exact finite linear algebra over Q end to end -- no small parameter, no truncation, no convergence, no tolerance. Only termination + SymPy expression management (controlled by substituting the integer point into the coordinate vector BEFORE forming the tangent matrix, so the rank is over an integer matrix).

## Decisions Made

- **COMPUTED the single-copy orbit dimension** (exact QQ rank at 3 generic integer octonionic points, MAX) rather than asserting the literature value 24; the Garibaldi-Guralnick value is a CONFIRMATION target only (fp-skip-single-copy-gate / Spin(8)-triality back-of-envelope rejected -- the three 8's are permuted by triality, so the naive count is a trap).
- **Used a 52-independent f_4 basis** (exact rref over QQ) for the per-point rank instead of all 324 generators: identical row space under M.v, so identical rank, but ~2-3x faster per point (~47s vs ~130s). The full 324-row rank was run once as a prototype cross-check and agreed (24).
- **Defined the >=2 generic integer octonionic points EXPLICITLY in-module** (SINGLE_COPY_POINTS: planner-spike P1 + two independent integer points P2/P3) rather than depending on the engine's `octonionic_points()`, so the GATE's genericity claim is self-contained and auditable; each point validated integer + genuinely octonionic (>=4 nonzero imaginary comps per off-diagonal octonion) + distinct diagonal.
- **Reused E.inner_derivations() VERBATIM** from Plan 01 (the same 324 f_4 generators); no f_4 rebuilt, no octonion arithmetic re-derived, no octonion_algebra.py touched.

## Deviations from Plan

### Process Note (no auto-fixed issues)

**1. [Process note - single-file atomicity] Both Plan-02 tasks committed together**

- **Found during:** Task 1 (orbit-rank) checkpoint.
- **Issue:** The plan specifies per-task commits, but Task 1 (single-copy orbit rank) and Task 2 (GATE assertions) are both verifications inside ONE inseparable assert-harness file. The GATE assertions (`check_single_copy_gate`) consume the orbit_dim computed by the orbit-rank function (`check_single_copy_orbit_dim`) in one `main()` flow; splitting into two commits of the same file would require an artificial broken-intermediate commit (the GATE references the orbit-rank result).
- **Fix:** Made one atomic commit (`778871af`) of the complete, passing Plan-02 extension. The commit message describes both the orbit-rank computation and the GATE. Same single-file precedent as Plan 01.
- **Verification:** Module exits 0; both tasks' contract acceptance tests pass.
- **Committed in:** `778871af`

---

**Total deviations:** 0 auto-fixed + 1 process note (single-file atomicity, same packaging artifact as Plan 01). No scope change, no physics redirect, no convergence/approximation issues (exact over Q).

## Issues Encountered

None. The computation is exact over Q and the result (orbit 24) matched the Garibaldi-Guralnick anchor on the first run. The only practical consideration is runtime: the exact QQ rank of the single-copy tangent matrix at an integer octonionic point takes ~20-110s per point (52-basis) and ~130s for the full 324-row spanning set; this is inherent to exact rational linear algebra and is acceptable in-phase (no proxy/float shortcut taken).

## Open Questions

- None blocking. The f_4 builder is CERTIFIED (single-copy orbit 24 / Spin(8) / trdeg 3 reproduces the literature anchor in-engine). `ORBIT_DIM_SINGLE = 24` and the single-copy recipe (generic INTEGER point, substitute-first, matrix*vector tangents M.v, exact QQ rank, 52-independent basis for speed) are carried forward to Plan 03 (the pair orbit dimension; consistency anchor 54 - pair_orbit_dim = 7).

## Next Phase Readiness

- **For Plan 03 (pair orbit dimension):** the CERTIFIED f_4 builder (single-copy orbit 24 confirms it is Der(h_3(O))) is the input. Plan 03 may now compute the pair (52 x 54) orbit value, applying the SAME recipe to the joint 54-vector (X,Y): generic INTEGER point, substitute-first, matrix*vector tangents M.v_joint, exact QQ rank; the 52-independent f_4 basis (selected here via exact rref over QQ) de-risks the pair rank. Consistency anchor: 54 - pair_orbit_dim = 7 (the seven base invariants).
- **For Phase 66 (the (b) SPINE -- c independence):** the orbit-derivative route reuses this exact single-copy infinitesimal-action machinery (tangents M.v over Q at generic integer points); the certified builder is the foundation for the joint 27+27 Jacobian-rank test.

## Self-Check: PASSED

- `code/orbit_dimension_gate.py` exists and reproducibly exits 0 (~5 min end-to-end).
- Commit `778871af` present in git log.
- All `must_contain` tokens present: deliv-single-copy-rank {`rank`, `_flat27`, `24`}; deliv-single-copy-gate {`28`, `Spin(8)`, `trdeg`}.
- Contract coverage COMPLETE: 2/2 claims (both passed), 2/2 deliverables (both passed), 4/4 acceptance tests (all passed), 4/4 references (all completed), 3/3 forbidden proxies (all rejected), 2 comparison verdicts (both pass).
- Exact-over-Q discipline confirmed: orbit rank via `sympy.Matrix.rank()` over QQ on an integer matrix (point substituted FIRST); basis via `.rref()` over QQ; 0 numpy float-rank calls, 0 octonion_algebra imports on the decisive path.
- Domain guard (mathematical physics / topological): the orbit dimension (24), stabilizer (28), and trdeg (3) are exact integers -- computed over QQ, not floats; the orbit dimension is COMPUTED (not the looked-up literature value; Spin(8)-triality back-of-envelope rejected).
- All three disconfirming-observation STOP conditions (orbit != 24; point-to-point rank disagreement; non-generic point) checked; NONE fired. HARD GATE (orbit 24) PASSED.

---

_Phase: 65-f-4-construction-orbit-dimension-gate_
_Completed: 2026-05-25_
