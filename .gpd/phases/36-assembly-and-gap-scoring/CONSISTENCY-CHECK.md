# Phase 36 Consistency Check (Rapid Mode)

**Phase:** 36-assembly-and-gap-scoring
**Plans checked:** 01, 02
**Date:** 2026-03-30
**Mode:** Rapid (post-phase cross-phase consistency)

---

## 1. Convention Compliance (Phase 36 vs Full Ledger)

### ASSERT_CONVENTION Headers

Both deliverables declare:
```
metric_signature=mostly_minus, coupling_convention=J_gt_0_AFM, emergent_speed=c_s=1.659Ja, natural_units=natural, fisher_metric=SLD
```

### Convention-by-Convention Compliance

| Convention | Ledger Value | Phase 36 Usage | Compliant? | Notes |
|---|---|---|---|---|
| metric_signature | "(+,+,...,+) Riemannian Fisher metric" (state.json) | ASSERT says "mostly_minus" for emergent spacetime; Fisher qualified as "spatial only (Riemannian)" throughout | YES (compatible) | The convention_lock was set during v8.0 (algebraic phases). Phase 34 introduced the emergent Lorentzian metric. Phase 36 explicitly documents dual usage: Riemannian for Fisher spatial, Lorentzian (-,+,...,+) for emergent spacetime. Convention note in chain doc line 18 explains this clearly. |
| natural_units | hbar=1, k_B=1, a=1 | Consistent throughout both documents | YES | |
| coupling_convention | J > 0 antiferromagnetic | ASSERT_CONVENTION: J_gt_0_AFM. "AFM" used in chain doc. No ferromagnetic J anywhere. | YES | |
| state_normalization | density matrices trace 1 | Consistent (rho_Lambda used throughout) | YES | |
| spin_basis | standard S^z eigenbasis | Not mentioned explicitly in Phase 36 (assembly phase, no new calculations). Compatible. | YES (N/A -- assembly) | |
| Fourier convention | N/A | Not used in Phase 36 | YES (N/A) | |
| All other canonical conventions | N/A (lattice spin chain) | Not used in Phase 36 | YES (N/A) | |

### Custom Conventions

| Convention | Ledger Value | Phase 36 Usage | Compliant? |
|---|---|---|---|
| Jordan product | a o b = (1/2)(ab+ba) | Not used (Phases 28-30 content) | N/A |
| Peirce eigenvalues | {0, 1/2, 1} | Not used | N/A |
| Octonion convention | Fano e_1 e_2 = e_4 | Not used | N/A |
| Clifford signature | Cl(9,0) | Not used | N/A |

**Convention compliance: ALL COMPLIANT (8 relevant checked, 10 N/A)**

---

## 2. Specific Convention Checks (Per Request)

### Check 2a: No Metric Signature Conflicts

**Result: PASS**

The chain document (line 18) explicitly states:
> "The convention_lock records metric_signature as '(+,+,...,+) Riemannian Fisher metric' for the spatial part. The full emergent spacetime metric uses Lorentzian signature (-,+,...,+) as established in Phase 34."

Phase 36 consistently:
- Qualifies Fisher metric as "spatial only" and "Riemannian" (chain doc lines 72, 74, 487)
- Uses (-,+,...,+) only for the full emergent spacetime metric ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j
- Never conflates the two

### Check 2b: c = c_s = 1.659 Ja Consistently (Never c = v_LR)

**Result: PASS**

- Chain document ASSERT_CONVENTION: emergent_speed=c_s=1.659Ja
- Gap scorecards ASSERT_CONVENTION: emergent_speed=c_s=1.659Ja
- Chain doc line 200: "CRITICAL: The emergent speed of light is c = c_s = 1.659 Ja, NOT v_LR = 12.66 J" (explicit warning)
- v_LR appears only in the velocity hierarchy section where it is clearly distinguished from c_s
- Gap scorecards: c_s = 1.659 Ja appears at line 91 (sigma model), nowhere equated to v_LR
- Consistent with Phase 34 results (STATE.md: c_eff = c_s = 1.659 Ja)
- STATE.md line 54 writes "c_s = 1.659 J (a=1)" which is numerically identical to 1.659 Ja when a=1

### Check 2c: J > 0 Antiferromagnetic Throughout

**Result: PASS**

- Both ASSERT_CONVENTION headers: coupling_convention=J_gt_0_AFM
- Chain doc line 58: "Lieb-Mattis theorem for AFM"
- Chain doc line 420: "Bipartite lattice, AFM coupling"
- Gap scorecards line 153: "Heisenberg AFM with Neel order"
- No instance of J < 0 or ferromagnetic coupling anywhere in Phase 36 deliverables

### Check 2d: Jacobson 2016 Framework (Not 1995)

**Result: PASS**

- Chain doc line 301: "Framework (Jacobson 2016, NOT Jacobson 1995): The argument uses entanglement equilibrium (delta S = 0), not the Clausius relation (delta Q = T dS)."
- Gap scorecards: "Jacobson, PRL 116 (2016) 201101" cited as the framework reference
- 1995 appears only once in scorecards (line 399) in a comparison table noting that Jacobson 1995/2016 "assumes smooth manifold" vs. this chain's lattice derivation -- correctly contextualized as lineage, not the framework used
- Entanglement equilibrium (delta S = 0) used throughout, never Clausius (delta Q = T dS)

---

## 3. Cross-Document Consistency (Chain vs Scorecards)

### Dimension-Dependent Claims

| Claim | Chain Document | Gap Scorecards | Consistent? |
|---|---|---|---|
| d=1 Fisher | FAILS (FISH-03, g_bulk ~ N^{-2.75}) | OPEN (FISH-03 blocks) | YES |
| d=1 Einstein | Trivial (G_ab = 0 in 1+1d) | Moot for gravity | YES |
| d=1 Gap B | Not scored (chain doc is chain, not scoring) | CLOSED (Route A, exact CFT) | COMPATIBLE |
| d=2 Fisher | CONDITIONAL (H1-H4, log L correction) | CONDITIONAL (H1-H4) | YES |
| d=2 Neel | QMC only for S=1/2 | QMC only for S=1/2 | YES |
| d>=3 Fisher | CONDITIONAL (Goldstone convergent) | NARROWED (4 explicit hypotheses) | COMPATIBLE (different rubric: chain uses rigor level, scorecards use gap rubric) |
| d>=3 Neel | Rigorous for S>=1 (DLS), S=1/2 d=3 (KLS) | Same citations | YES |
| Route A/B | Complementary | Complementary | YES |
| MVEH | Structural identification, not proof | Structural identification, not proof | YES |
| Sorce 2024 | Not discussed (chain doc scope) | Cited in Gaps B and D | COMPATIBLE |

### Equation Citations Cross-Check

Spot-checked 5 equation references between the two documents:

| Equation | Chain Doc Citation | Scorecard Citation | Match? |
|---|---|---|---|
| Eq. 32.8 (FISH-01) | Line 81, Hastings-Koma | Line 40, FISH-01 smoothness | YES |
| Eq. 32.12 (FISH-03) | Line 103, g_bulk ~ N^{-2.75} | Line 60, same formula | YES |
| Eq. 33.19 (CORR-03) | Line 139, g_F = O(m_s^2) | Line 73, same formula | YES |
| Eq. 33.11 (sigma model) | Line 127, action formula | Line 88, same action | YES |
| Eq. 34.9 (metric) | Line 207, ds^2 formula | Line 99, same formula | YES |

### Rigor Level vs Gap Score Consistency

The chain document classifies link rigor. The scorecards classify gap status. These use different rubrics (RIGOROUS/CONDITIONAL/PHYSICAL ARGUMENT/ASSUMED vs CLOSED/NARROWED/CONDITIONAL/OPEN). Verified that the mapping is consistent:

- Chain: Link (c) FAILS in d=1 --> Scorecard: Gap A OPEN in d=1 (consistent)
- Chain: Link (c) CONDITIONAL in d>=3 --> Scorecard: Gap A NARROWED in d>=3 (consistent -- the scorecard accounts for the conditional theorem CORR-03 narrowing the gap)
- Chain: Link (f) Route A CONDITIONAL --> Scorecard: Gap B CLOSED only in d=1, OPEN in d>=2 (consistent -- Gap B is the conformal assumption needed for Route A, which is satisfied only in d=1)

No contradictions found.

---

## 4. Provides/Requires Chain Verification

### Phase 36 Consumes From:

| Consumed | Producer | Meaning Match | Convention Match | Status |
|---|---|---|---|---|
| FISH-01 (Eq. 32.8) | Phase 32 | Smoothness bound on rho differences | Natural units, SLD Fisher | OK |
| FISH-03 (Eq. 32.12) | Phase 32 | g_bulk power-law decay in 1D | Same conventions | OK |
| CORR-03 (Eq. 33.19) | Phase 33 | g_F = O(m_s^2) conditional | Same conventions | OK |
| CORR-02 (Eq. 33.11) | Phase 33 | Sigma model action with c_s | c_s = 1.659 Ja consistent | OK |
| LRNZ-01/02 (Eq. 34.16) | Phase 34 | O(d+1) symmetric action | Same conventions | OK |
| Metric (Eq. 34.9) | Phase 34 | ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j | Lorentzian for spacetime, Fisher spatial | OK |
| BWEQ-01 (Eq. 35.1) | Phase 35 | Lattice-BW entanglement Hamiltonian | c_s consistent | OK |
| J1-J3 (Eqs. 35.0a, 35.19/21, 35.3) | Phase 35 | BW, theta=sigma=0, T_U | Conventions match | OK |

All 8 provides/requires pairs verified. No mismatches.

### Phase 36 Provides To (downstream):

- Complete chain document (for paper revision): provides six-link structure with citations
- Gap scorecards (for paper revision): provides individual gap scores with evidence
- Both are terminal deliverables for the v9.0 milestone -- no further computational phases depend on them

---

## 5. Approximation Validity

No new parameter values introduced in Phase 36 (assembly phase, no calculations). All cited values (c_s = 1.659 Ja, v_LR = 12.66 J, m_s = 0.3074, SRF = 0.9993) are passthrough from Phases 32-35 with no modification. No approximation validity ranges violated.

---

## 6. Minor Observations (Not Issues)

1. **Convention_lock vs ASSERT_CONVENTION notation:** The convention_lock in state.json records metric_signature as "(+,+,...,+) Riemannian Fisher metric" while the Phase 36 ASSERT_CONVENTION says "mostly_minus". This is not a conflict -- the convention_lock was set during the v8.0 algebraic phases. Phase 34 introduced the Lorentzian metric and Phase 36 explicitly documents the dual usage. However, the convention_lock could be updated to note the emergent Lorentzian signature for clarity. This is a documentation improvement, not a physics inconsistency.

2. **STATE.md shorthand:** Line 54 writes "c_s = 1.659 J (a=1)" while all derivation documents use "c_s = 1.659 Ja". These are identical when a=1. No inconsistency.

---

## Summary

| Check Category | Items Checked | Issues Found | Status |
|---|---|---|---|
| Convention compliance (full ledger) | 8 relevant + 10 N/A | 0 | PASS |
| Metric signature (Riemannian vs Lorentzian) | Both documents | 0 | PASS |
| c = c_s = 1.659 Ja (not v_LR) | Both documents | 0 | PASS |
| J > 0 antiferromagnetic | Both documents | 0 | PASS |
| Jacobson 2016 (not 1995) | Both documents | 0 | PASS |
| Chain vs scorecards consistency | 10 dimension-dep claims, 5 equation spot-checks | 0 | PASS |
| Provides/requires chain | 8 consumed quantities | 0 | PASS |
| Approximation validity | No new parameters | 0 | PASS |

**Consistency status: CONSISTENT**

No convention violations, no cross-document contradictions, no dimension-dependent claim mismatches. Phase 36 deliverables are internally consistent with each other and with all accumulated conventions from Phases 32-35.

---

_Consistency check performed: 2026-03-30_
_Mode: rapid (post-phase)_
_Checks performed: 7 categories, 41 individual items_
_Issues found: 0_
