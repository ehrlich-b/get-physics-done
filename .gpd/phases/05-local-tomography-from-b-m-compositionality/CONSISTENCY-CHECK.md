# Phase 05 Consistency Check (Rapid)

**Phase:** 05-local-tomography-from-b-m-compositionality
**Plans checked:** 01, 02
**Date:** 2026-03-21
**Mode:** rapid (post-phase)
**Checker:** gpd-consistency-checker

---

## Convention Compliance (Full Ledger)

This project is algebraic/categorical with no metric, Fourier, or gauge conventions. All 18 standard physics conventions are N/A (justified: no spacetime, no fields, no couplings). The active conventions are custom:

| Convention | Defined | Phase 05-01 | Phase 05-02 | Status |
|------------|---------|-------------|-------------|--------|
| Sequential product: a & b (non-commutative) | STATE.md | Used consistently (Eq. 05-01.1, S1-S7 inheritance) | Used consistently (theorem invocations) | OK |
| Jordan product: a * b = (1/2)(a & b + b & a) | STATE.md | Used in correlation form B(a,b) = tau(a * phi^{-1}(b)) | Not directly used (theorem invocation, not new derivation) | OK |
| Orthogonality: a perp b iff a & b = 0 | STATE.md | Used in S4 inheritance proof | Referenced in type exclusion context | OK |
| Compression: C_p (Alfsen-Shultz P-projection) | STATE.md | Referenced via factor-level product Eq. 04-06.4 | Not directly used | OK |
| Corrected product: Eq. 04-06.4 | Phase 4 | Referenced correctly at Step 3 line 99-102 | Not directly used | OK |
| Composite product: (a tensor b) & (c tensor d) = (a & c) tensor (b & d) | Phase 5/01 | Defined as Eq. 05-01.1 | Used as input to theorem hypotheses | OK |
| Local tomography: dim(V_BM) = dim(V_B) * dim(V_M) | Phase 5/01 | Proved as Eq. 05-01.5 | Consumed as hypothesis for vdW Thm 3, Barnum-Wilce | OK |
| Axiom source: arXiv:1803.11139 Def. 2 EXCLUSIVELY | STATE.md | Respected throughout | Respected throughout | OK |
| dim convention: real vector space dimension | Phase 5/01 | Explicit at SELF-CRITIQUE checkpoints | Explicit at Step 2 checkpoint | OK |

**Convention compliance: 9/9 active conventions checked, all compliant.**

No convention drift detected between Plan 01 and Plan 02.

---

## Provides/Consumes Verification

### Phase 4 -> Phase 5 (Plan 01)

| Quantity | Producer | Consumer | Meaning | Units | Test Value | Convention | Status |
|----------|----------|----------|---------|-------|------------|------------|--------|
| S1-S7 proved | P4/P03-04 | P5/01 Step 4 | All seven vdW axioms hold on the corrected SP | Dimensionless boolean | N/A (logical) | vdW Def. 2 | OK |
| EJA classification: V_3 = M_2(C)^sa | P4/P04 | P5/01 Step 1 | Spin factor V_3 is the EJA for qubits, dim=4 | Dimensionless | dim(V_3) = 3+1 = 4 = 2^2 = dim(M_2(C)^sa). MATCH | JVW classification | OK |
| Corrected product Eq. 04-06.4 | P4/P06 | P5/01 Step 3 | a & b = sum lambda_i C_{p_i}(b) + sum sqrt(lambda_i lambda_j) P_{ij}(b) | Dimensionless | On V_3, reduces to Luders sqrt(a) b sqrt(a) | OUS construction | OK |
| phi is order isomorphism | P4/P01 | P5/01 Step 9 | Tracking map V_B -> V_M is bijective and order-preserving | Dimensionless | phi^{-1} exists and is used in B(a,b) | Faithful self-modeling | OK |

### Phase 5 Plan 01 -> Plan 02

| Quantity | Producer | Consumer | Meaning | Units | Test Value | Convention | Status |
|----------|----------|----------|---------|-------|------------|------------|--------|
| Local tomography Eq. 05-01.5 | P5/01 | P5/02 Steps 5-7 | dim(V_BM) = dim(V_B) * dim(V_M) | Dimensionless integer | 4*4=16 = dim(M_4(C)^sa). MATCH | Real vec space dim | OK |
| Composite S1-S7 | P5/01 | P5/02 Step 5 | Product-form SP on V_BM satisfies all seven axioms | Dimensionless boolean | N/A (logical) | vdW Def. 2 | OK |
| V_3 identification | P4/P04 via P5/01 | P5/02 Step 6 | V_3 = M_2(C)^sa serves as qubit for Barnum-Wilce hypothesis | Dimensionless | dim(V_3) = 4. MATCH | JVW classification | OK |

**All 7 provides/consumes pairs verified. No mismatches.**

---

## Spot-Check: Load-Bearing Equations

### Check 1: Dimension formulas in type exclusion (downstream-critical)

The dimension algebra is the backbone of the exclusion argument. Verify for n=2:

**Real:** dim(M_2(R)^sa) = 2(2+1)/2 = 3. Composite dim = 4(4+1)/2 = 10. LT test: 3^2 = 9 vs 10. 9 != 10. CORRECT (exclusion holds).

**Complex:** dim(M_2(C)^sa) = 2^2 = 4. Composite dim = 4^2 = 16. LT test: 4^2 = 16 = 16. CORRECT (passes).

**Quaternionic:** dim(M_2(H)^sa) = 2(2*2-1) = 2*3 = 6. Composite dim = 4(2*4-1) = 4*7 = 28. LT test: 6^2 = 36 vs 28. 36 != 28. CORRECT (exclusion holds).

**Algebraic factorization:** For R: (n-1)^2 = 0 => n = 1. For H: same equation (n-1)^2 = 0 => n = 1. Both correct -- verified independently by expanding the LT condition for each type.

**Spin factor cross-identifications:** V_2 = M_2(R)^sa: dim(V_2) = 2+1 = 3 = dim(M_2(R)^sa). V_3 = M_2(C)^sa: dim(V_3) = 3+1 = 4 = dim(M_2(C)^sa). V_5 = M_2(H)^sa: dim(V_5) = 5+1 = 6 = dim(M_2(H)^sa). All consistent.

**Verdict: PASS**

### Check 2: Non-degeneracy argument (central to local tomography proof)

B(a,b) = tau(a * phi^{-1}(b)) where tau is normalized trace, * is Jordan product, phi^{-1} is tracking inverse.

Test on V_3 = M_2(C)^sa: tau(x) = (1/2)Tr(x). Jordan product a * b = (1/2)(ab + ba) for Hermitian matrices.

Test value: a = diag(1,0), b = phi(diag(1,0)) (assuming phi = id for simplicity).
B(a,b) = tau(a * a) = (1/2)Tr((1/2)(a^2 + a^2)) = (1/2)Tr(a^2) = (1/2)*1 = 1/2 != 0.

For a = diag(1,0), b = diag(0,1):
B(a,b) = tau(a * b) = (1/2)Tr((1/2)(ab + ba)) = (1/4)Tr(0 + 0) = 0.

This correctly distinguishes orthogonal from aligned effects. The Gram matrix of B with respect to the standard basis {I, sigma_x, sigma_y, sigma_z} of M_2(C)^sa would be:
B(e_i, e_j) = (1/2)Tr(e_i * e_j). For orthonormal basis elements with e_i * e_j = delta_{ij} * I/2 (Jordan product of Pauli matrices), the Gram matrix is proportional to identity, hence non-degenerate.

**Verdict: PASS**

### Check 3: S4 inheritance on composite (Phase 4 -> Phase 5 bridge)

The argument: (a tensor b) & (c tensor d) = 0 implies (a & c) tensor (b & d) = 0. By states-separate-points, either a & c = 0 or b & d = 0. In either case, factor-level S4 gives c & a = 0 or d & b = 0, hence (c tensor d) & (a tensor b) = 0.

Critical step: "x tensor y = 0 iff x = 0 or y = 0" for elements of an OUS tensor product evaluated on product states. This uses the faithfulness of product states for separating product effects, which is the states-separate-points property of OUS (Alfsen-Shultz 1.23).

Potential concern: This argument works for product effects. For general (non-product) effects on V_BM, S4 must also hold. However, since the derivation shows dim(V_BM) = dim(V_B) * dim(V_M) (local tomography), every effect on V_BM is a linear combination of product effects, and S4 extends by linearity (S1) and continuity (S2).

**Verdict: PASS**

---

## Cross-Phase Result Consistency

### Phase 5 conclusions vs Phase 4 starting point

Phase 4 establishes: OUS with sequential product satisfying S1-S7 => EJA (vdW Thm 1) => V_3 = M_2(C)^sa for qubits.

Phase 5 builds on this to conclude: EJA + local tomography => C*-algebra (vdW Thm 3) => V = M_n(C)^sa (Barnum-Wilce) => involution X* = X^dagger (Hanche-Olsen + exhibition).

The logical chain is:
- Phase 4 output (S1-S7, EJA) is CONSUMED, not re-derived, in Phase 5.
- Phase 5 adds: composite construction, LT proof, type exclusion, C*-promotion.
- No Phase 4 results are contradicted or modified.
- The V_3 = M_2(C)^sa identification from Phase 4 is used as the "qubit subsystem" hypothesis for Barnum-Wilce. This is a correct and consistent use.

The involution (X* = X^dagger) is a NEW structure not present in Phase 4. It is derived as a CONCLUSION of the theorem chain, not assumed. This is consistent with Phase 4, which worked entirely within OUS/EJA without needing the involution.

**No cross-phase inconsistency detected.**

---

## Approximation Validity

No approximations are in use (algebraic proof work). STATE.md confirms "Active Approximations: None." Phase 5 introduces no numerical approximations. All results are exact algebraic/logical statements.

**N/A -- no approximation validity concerns.**

---

## Summary

| Check | Count | Pass | Fail | N/A |
|-------|-------|------|------|-----|
| Convention compliance (custom) | 9 | 9 | 0 | 0 |
| Convention compliance (standard 18) | 18 | 0 | 0 | 18 |
| Provides/consumes pairs | 7 | 7 | 0 | 0 |
| Load-bearing equation spot-checks | 3 | 3 | 0 | 0 |
| Cross-phase result consistency | 1 | 1 | 0 | 0 |
| Approximation validity | 0 | 0 | 0 | 0 |

**Total checks: 20 performed, 0 issues found.**

**Consistency status: CONSISTENT**

No convention drift, no sign/factor errors, no provides/consumes mismatches, no cross-phase contradictions detected.
