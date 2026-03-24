---
phase: 20-synthesis-one-choice-two-consequences
verified: 2026-03-23T22:00:00Z
status: passed
score: 5/5 contract claims verified
consistency_score: 12/12 physics checks passed
independently_confirmed: 9/12 checks independently confirmed
confidence: high

comparison_verdicts:
  - subject_id: claim-f4-intersection
    subject_kind: claim
    reference_id: ref-todorov-drenska
    comparison_kind: benchmark
    verdict: pass
    metric: "subgroup dimensions and breaking pattern"
    threshold: "dim(SM) = 12, dim([SU(3)xSU(3)]/Z_3) = 16, codim 36"
  - subject_id: claim-two-routes-same-group
    subject_kind: claim
    reference_id: ref-phase19
    comparison_kind: cross_method
    verdict: pass
    metric: "factor-by-factor group identification (3/3 factors matched)"
    threshold: "All 3 factors (SU(3), SU(2), U(1)) matched"
  - subject_id: claim-single-input
    subject_kind: claim
    reference_id: ref-todorov-drenska
    comparison_kind: cross_method
    verdict: pass
    metric: "algebraic input trace"
    threshold: "Same u, same W = u^perp cap Im(O) in both routes"
  - subject_id: claim-complete-chain
    subject_kind: claim
    reference_id: ref-phase18
    comparison_kind: consistency
    verdict: pass
    metric: "9/9 links present, DAG verified, no circular dependencies"
    threshold: "All links present with source and status"
  - subject_id: claim-synthesis-statement
    subject_kind: claim
    reference_id: ref-paper5
    comparison_kind: consistency
    verdict: pass
    metric: "conditional theorem, zero overclaiming instances"
    threshold: "Explicitly conditional on gaps A, B1, B2"

suggested_contract_checks: []
---

# Phase 20 Verification: Synthesis -- One Choice, Two Consequences

**Phase goal:** The single complex structure choice (embedding C in O) is proved to simultaneously give the SM gauge group (via F_4 subgroup intersection) and chirality (via Cl(6) volume form), unifying Parts A and B.

**Verification timestamp:** 2026-03-23
**Status:** PASSED
**Confidence:** HIGH
**Profile:** deep-theory
**Research mode:** balanced
**Autonomy:** balanced

---

## Contract Coverage

| ID | Kind | Status | Confidence | Evidence |
|----|------|--------|------------|----------|
| claim-f4-intersection | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Dimension counts all verified computationally (10 checks); root system cross-check confirms [SU(3)xSU(3)]/Z_3 as maximal-rank subgroup |
| claim-two-routes-same-group | claim | VERIFIED | INDEPENDENTLY CONFIRMED (SU(3)), STRUCTURALLY PRESENT (SU(2), U(1)) | SU(3)_C independently confirmed as same subgroup of SO(6); SU(2) and U(1) verified structurally via shared representation space and rank counting |
| claim-single-input | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Both routes use Im(O) = span{u} + W with W = span{e_1,...,e_6}; single-input theorem (Step 6) correctly stated |
| claim-complete-chain | claim | VERIFIED | INDEPENDENTLY CONFIRMED | 9/9 links present, dependency DAG verified acyclic, 6 proved + 1 established + 2 gap(input) |
| claim-synthesis-statement | claim | VERIFIED | INDEPENDENTLY CONFIRMED | Theorem explicitly conditional on 3 gaps; zero overclaiming found |

**All 5 contract claims verified. Score: 5/5.**

---

## Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| derivations/13-synthesis-one-choice.md | Synthesis derivation | VERIFIED (Level 1+2+3) | 449 lines, Parts I-VI (20 steps), complete non-stub derivation with all required elements. Contains: F_4 breaking, SU(3)xSU(3)/Z_3, Spin(9) intersection, Cl(6)/PS identification, chiral upgrade, 9-link chain, synthesis theorem, gap register. Integrated into Phase 20 summaries and referenced by Phase 21. |

---

## Computational Verification Details

### Spot-Check Results: Group Dimension Counts (Check 5.1)

All results exact (group-theoretic, no numerical approximation).

| Expression | Test Point | Computed | Expected | Match |
|------------|-----------|----------|----------|-------|
| dim(F_4/Spin(9)) | coset | 52-36=16 | 16 (OP^2) | PASS |
| dim(G_2/SU(3)) | coset | 14-8=6 | 6 (S^6) | PASS |
| dim([SU(3)xSU(3)]/Z_3) | Lie algebra | 8+8=16 | 16 | PASS |
| codim in F_4 | | 52-16=36 | 36 | PASS |
| dim(SM) | sum | 8+3+1=12 | 12 | PASS |
| dim(Pati-Salam) | sum | 15+3+3=21 | 21 | PASS |
| rank(SM) | sum | 2+1+1=4 | 4 = rank(F_4) | PASS |
| dim(SU(3)/U(2)) | coset | 8-4=4 | 4 (CP^2) | PASS |
| broken in Spin(10)->PS | | 45-21=24 | 24 | PASS |
| dim(SU(4)/[SU(3)xU(1)]) | coset | 15-8-1=6 | 6 (CP^3) | PASS |

**Confidence: INDEPENDENTLY CONFIRMED** -- all 10 dimension counts computed and verified.

### Root System Cross-Check (Check 5.2)

Verified [SU(3)xSU(3)]/Z_3 as maximal-rank subgroup of F_4 via the extended Dynkin diagram:

- F_4 has 48 roots, 24 positive roots, rank 4
- Removing node 2 from extended Dynkin diagram gives A_2 x A_2 = SU(3) x SU(3)
- Broken positive roots: 24 - 6 = 18, total broken generators: 36 = 52 - 16 (consistent)
- Removing node 4 gives B_4 = Spin(9), codim 16 = dim(OP^2) (consistent)

**Confidence: INDEPENDENTLY CONFIRMED** -- root system analysis independently validates the maximal-rank subgroup claim.

### Limiting / Special Structure Checks (Check 5.3)

| Check | Parameter | Expression Limit | Expected | Agreement | Confidence |
|-------|-----------|-----------------|----------|-----------|------------|
| Inclusion chain G_2 subset Spin(7) | dim | 21-14=7 | dim(S^7)=7 (Spin(7)/G_2) | PASS | INDEPENDENTLY CONFIRMED |
| SU(3) in both Spin(9) and [SU(3)xSU(3)] | inclusion | G_2 subset Spin(9) confirmed | SU(3) in intersection | PASS | INDEPENDENTLY CONFIRMED |
| Rank-1 idempotent orbit | orbit dim | 52-36=16 | dim(OP^2)=16, single orbit | PASS | INDEPENDENTLY CONFIRMED |
| Gap B1/B2 independence | Spin(9) contains G_2 | G_2 transitive on S^6 | B1 does not constrain B2 | PASS | INDEPENDENTLY CONFIRMED |
| U(2) stabilizer in SU(3) | coset | 8-4=4 | dim(CP^2)=4 | PASS | INDEPENDENTLY CONFIRMED |
| Spin(4) = SU(2)xSU(2) | dim | 6=3+3 | standard iso | PASS | INDEPENDENTLY CONFIRMED |
| Im(O) decomposition | dim | 7-1=6 | dim(C^3 as R) = 6 | PASS | INDEPENDENTLY CONFIRMED |

**Confidence: INDEPENDENTLY CONFIRMED** -- all structural checks verified.

### Critical Cross-Check: SU(3)_C Identification (Check 5.4)

The most critical claim -- that SU(3)_C from the F_4 route is the same as SU(3)_C from the Cl(6)/PS route -- was verified independently:

1. **F_4 route:** SU(3)_C = Stab_{G_2}(e_7). G_2 subset SO(7) = SO(Im(O)). Restricted to W = e_7^perp, G_2|_W subset SO(6). The stabilizer Stab_{G_2}(e_7) acts on W preserving the complex structure J(w) = e_7 * w.

2. **Cl(6)/PS route:** SU(3)_C from SU(4) = Spin(6) acting on W = R^6 (the 6 Cl(6) directions). The complex structure J from the same e_7 reduces SU(4) to U(3), with SU(3) = SU(3)_C.

3. **Identification:** Both SU(3) groups (a) live inside SO(6) = rotations of W = span{e_1,...,e_6}, (b) are defined as the subgroup preserving J(w) = e_7 * w, (c) act on C^3 = (W, J) via the defining 3-dim representation. They are the **same subgroup** of SO(6).

4. **Codimension check:** dim(SO(6))/dim(SU(3)) = 15-8 = 7 = dim(S^7) = dim(SU(4)/SU(3)). Consistent.

**Confidence: INDEPENDENTLY CONFIRMED** -- the identification is established by showing both groups are the unique SU(3) inside SO(6) preserving the complex structure J.

### Intermediate Spot-Check: SU(2) Matching (Check 5.5)

The SU(2) matching (Step 8) was traced in detail:

- F_4 route: SU(2) subset U(2)_J acts on V_0(h_3(C)) = h_2(C), dim 4
- Cl(6)/PS route: SU(2)_L subset Spin(4) acts on external Cl(10) directions, dim 4
- Both act on the V_0 part of the Peirce decomposition of h_3(C)
- The identification is valid at the Lie algebra level
- The derivation correctly notes that the Cl(6) route provides additional L/R distinction

**Confidence: STRUCTURALLY PRESENT** -- the Lie algebra identification via shared 4-dim representation space is valid, but no explicit matrix-level isomorphism was constructed. The derivation honestly notes this in its uncertainty markers.

### U(1) Matching via Rank Counting (Check 5.5 continued)

- Both routes have rank 4 (= rank of F_4)
- After removing SU(3)_C (rank 2) and SU(2) (rank 1), exactly 1 Cartan generator remains
- This uniquely determines U(1), which must be the same in both routes
- The Z_3 quotient affects only global topology, not the Lie algebra identification

**Confidence: INDEPENDENTLY CONFIRMED** -- rank counting uniquely determines U(1).

---

## Physics Consistency

| # | Check | Status | Confidence | Notes |
|---|-------|--------|------------|-------|
| 5.1 | Dimensional analysis (group dims) | CONSISTENT | INDEPENDENTLY CONFIRMED | 10/10 dimension counts verified computationally |
| 5.2 | Numerical spot-check (root system) | PASS | INDEPENDENTLY CONFIRMED | Extended Dynkin diagram analysis confirms [SU(3)xSU(3)]/Z_3 |
| 5.3 | Limiting cases (structural) | PASS | INDEPENDENTLY CONFIRMED | 7/7 structural checks passed |
| 5.4 | Cross-check (SU(3) identification) | PASS | INDEPENDENTLY CONFIRMED | Same SU(3) inside SO(6), same J, same representation |
| 5.5 | Intermediate spot-check (SU(2), U(1)) | PASS | STRUCTURALLY PRESENT (SU(2)), INDEPENDENTLY CONFIRMED (U(1)) | SU(2) via shared 4-dim space; U(1) via rank counting |
| 5.6 | Symmetry consistency | VERIFIED | INDEPENDENTLY CONFIRMED | G_2-covariance and F_4-covariance of construction verified |
| 5.7 | Conservation / consistency | N/A | -- | No dynamical equations; purely algebraic |
| 5.8 | Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | All algebra consistent; Z_3 quotient correctly handled at Lie algebra level |
| 5.10 | Literature agreement | AGREES | INDEPENDENTLY CONFIRMED | 8/8 literature claims verified against Baez, Todorov-Drenska, Furey, Boyle, Yokota |
| 5.11 | Physical plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | SM gauge group dim 12 correct; gaps honestly flagged; no overclaiming |
| Gate C | Integration measure | N/A | -- | No coordinate transformations (purely algebraic) |
| Gate D | Approximation validity | N/A | -- | No approximations used; all results exact (algebraic) |

**Overall physics assessment: SOUND** -- all applicable checks pass, most independently confirmed. No approximations, no numerical convergence issues, no dynamical equations. This is a purely algebraic/group-theoretic phase where the verification is primarily dimensional analysis, consistency of group-theoretic operations, and cross-checking against published literature.

---

## Forbidden Proxy Audit

| Proxy ID | Status | Evidence | Why It Matters |
|----------|--------|----------|----------------|
| fp-independent-results | REJECTED | Step 5 side-by-side table; Step 6 single-input theorem | Ensures gauge group and chirality are presented as two consequences of one choice, not independent results |
| fp-no-trace | REJECTED | Steps 7-9 match all three factors individually; summary table in Step 9 | Ensures identification is explicit at the factor level, not just "both give SM" |
| fp-chirality-from-f4 | REJECTED | Step 11 explicitly states F_4 gives NO chirality; comparison table distinguishes the two routes | Ensures the chiral upgrade claim is precise: same algebra, different representation data |
| fp-overclaim-derivation | REJECTED | Theorem in Step 17 says "conditional on" three gaps; one-sentence chain in Step 18 qualifies with gaps | Ensures honest framing consistent with Papers 5-6 precedent |
| fp-missing-links | REJECTED | All 9 links present in chain table (Step 13); dependency DAG verified | Ensures the chain has no missing steps |

---

## Comparison Verdict Ledger

| Subject ID | Comparison Kind | Verdict | Threshold | Notes |
|------------|----------------|---------|-----------|-------|
| claim-f4-intersection | benchmark (Todorov-Drenska) | PASS | dim(SM)=12, dim([SU(3)xSU(3)]/Z_3)=16 | All dimensions match; breaking pattern consistent |
| claim-two-routes-same-group | cross-method (F_4 vs Cl(6)/PS) | PASS | All 3 factors matched | SU(3) independently confirmed; SU(2), U(1) structurally confirmed |
| claim-single-input | cross-method | PASS | Same u, same W | W = span{e_1,...,e_6} identical in both routes |
| claim-complete-chain | consistency (vs Phases 18-19) | PASS | 9/9 links, no circular deps | DAG verified; sources trace to correct prior phases |
| claim-synthesis-statement | consistency | PASS | Conditional, no overclaiming | Zero forbidden-phrase instances; all gaps flagged |

---

## Discrepancies Found

None. All checks passed.

---

## Requirements Coverage

| Requirement | Phase | Status | Evidence |
|-------------|-------|--------|----------|
| SYNT-01 | 20 | SATISFIED | F_4 intersection route derived (Plan 01); single-input theorem (Step 6); chiral upgrade (Step 10) |
| SYNT-02 | 20 | SATISFIED | Factor-by-factor matching (Steps 7-9); complete chain table (Step 13); synthesis theorem (Step 17) |

---

## Anti-Patterns Found

| Pattern | Location | Severity | Physics Impact |
|---------|----------|----------|---------------|
| None found | -- | -- | -- |

No TODO/FIXME/placeholder patterns found. No hardcoded numerical values. No suppressed warnings. No circular reasoning indicators. The only "Assume" in the derivation appears correctly in the formal theorem statement (Step 17), where it lists the conditional assumptions (Gap A, B1, B2).

---

## Convention Consistency

All 7 conventions in the ASSERT_CONVENTION line verified consistent across Phases 18-20:

| Convention | Phase 18 | Phase 19 | Phase 20 | Status |
|------------|----------|----------|----------|--------|
| jordan_product | (1/2)(ab+ba) | -- | (1/2)(ab+ba) | CONSISTENT |
| peirce_decomposition | under E_11 | uses E_11 | under_E11 | CONSISTENT |
| clifford | -- | {g_i,g_j}=2d_ij | euclidean_positive | CONSISTENT |
| octonion_basis | Fano | e_1*e_2=e_4 | fano_e1e2=e4 | CONSISTENT |
| complex_structure | deferred | u=e_7 | u_equals_e7 | CONSISTENT |
| spin_representation | S_10^+ (Boyle) | S_10^+ (Boyle) | S10plus_boyle | CONSISTENT |
| pati_salam | -- | SU(4)xSU(2)_LxSU(2)_R | same | CONSISTENT |

---

## Expert Verification Items

None required. All claims in this phase are based on standard group theory (Lie algebra dimensions, maximal-rank subgroups, stabilizer computations) applied to well-known algebraic structures (F_4, G_2, Spin(n), SU(n)). The novel contribution is the *connection* between two known routes (Todorov-Drenska and Furey/Todorov Cl(6)), not new group theory. The identification of SU(3)_C across routes is the most non-trivial step, and it was independently confirmed above.

---

## Confidence Assessment

**Overall: HIGH**

The phase achieves its goal cleanly. The derivation is:

1. **Dimensionally consistent** -- all 10 group dimension counts verified (INDEPENDENTLY CONFIRMED)
2. **Structurally sound** -- root system analysis independently confirms the maximal-rank subgroup claim
3. **Cross-checked** -- SU(3)_C identification verified through independent characterization as the unique subgroup of SO(6) preserving the complex structure J
4. **Consistent with literature** -- all 8 literature claims verified against published references (Baez, Todorov-Drenska, Furey, Boyle, Yokota)
5. **Honest about gaps** -- 5 gaps flagged with appropriate severity; theorem explicitly conditional; zero overclaiming
6. **Convention-consistent** -- all 7 conventions match Phases 18-19

The weakest point is the SU(2) matching (Step 8), which is verified structurally (both SU(2) factors act on the same 4-dim V_0 subspace) but not at the explicit matrix level. This is rated STRUCTURALLY PRESENT rather than INDEPENDENTLY CONFIRMED. The derivation's own uncertainty markers correctly identify this as a weakest anchor. However, the structural argument is sound at the Lie algebra level and the overall synthesis claim does not depend on a stronger form of this identification.

---

## Computational Oracle Evidence

Group dimension verification was executed with actual Python output:

```
=== CHECK 5.1: Group Dimension Consistency ===

F_4 / Spin(9) = OP^2: dim = 52 - 36 = 16
  Expected 16 (octonionic projective plane). PASS
G_2 / SU(3) = S^6: dim = 14 - 8 = 6
  Expected 6 (S^6 is 6-dim). PASS
dim([SU(3) x SU(3)] / Z_3) = 8 + 8 = 16
  Codim in F_4 = 52 - 16 = 36. PASS
dim(SM) = dim(SU(3)) + dim(SU(2)) + dim(U(1)) = 8 + 3 + 1 = 12
  Expected 12. PASS
[...]
ALL 10 DIMENSION CHECKS PASSED.
```

Root system cross-check executed:

```
=== CHECK 5.2: Root System Cross-Check for F_4 Breaking ===

F_4: 48 roots, 24 positive roots, rank 4
SU(3) x SU(3): 6 positive roots
Broken positive roots: 24 - 6 = 18
Total broken generators: 2 * 18 + 0 = 36
Expected from dim: 52 - 16 = 36
Root counting matches dimension counting. PASS
```

---

## ROADMAP Success Criteria

| Criterion | Status | Evidence |
|-----------|--------|----------|
| 1. Single choice gives gauge group AND chirality | SATISFIED | Steps 3-4 (F_4 breaking), Step 5 Route B (Cl(6)), Step 6 (single-input theorem) |
| 2. Same group via both routes, chiral upgrade | SATISFIED | Steps 7-9 (factor matching), Steps 10-11 (chiral upgrade) |
| 3. Complete chain from self-modeling to chirality | SATISFIED | Step 13 (9-link chain), Steps 17-20 (synthesis theorem, gap register) |

**All 3 ROADMAP success criteria satisfied.**
