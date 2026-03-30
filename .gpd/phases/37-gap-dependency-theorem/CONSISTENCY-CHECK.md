# Consistency Check: Phase 37 (Gap Dependency Theorem)

**Mode:** Rapid
**Phase:** 37-gap-dependency-theorem (Plans 01 and 02)
**Checker:** gpd-consistency-checker
**Date:** 2026-03-30

---

## 1. Convention Compliance (Phase 37 vs Full Ledger)

### 1a. Metric Signature

**Project-level convention_lock (state.json):** `(+,+,...,+) Riemannian Fisher metric`
**CONVENTIONS.md:** Lists metric signature under "Not Applicable" for QFT-standard conventions.
**Phase 37 ASSERT_CONVENTION:** `metric_signature=mostly_minus`
**Phase 37 body text:** `(-,+,+,+)` Lorentzian throughout all three derivation files.

**Assessment: CONSISTENT (not a drift).** The convention_lock records the *spatial* Fisher metric signature (Riemannian, positive-definite), which is the foundational object from Phases 32-33. Phase 37 works with the *emergent spacetime* metric, which is Lorentzian `(-,+,+,+)`. This distinction was explicitly documented in Phase 36 (`derivations/36-derivation-chain.md`, line 18): "The convention_lock records metric_signature as '(+,+,...,+) Riemannian Fisher metric' for the spatial part. The full emergent spacetime metric uses Lorentzian signature (-,+,...,+) as established in Phase 34."

The two metrics apply to different physical objects:
- Fisher metric $g_F$: spatial, Riemannian, `(+,+,...,+)` -- used in Phases 32-34
- Emergent spacetime metric $g_{\mu\nu}$: full spacetime, Lorentzian, `(-,+,+,+)` -- used in Phases 35-37

Phase 37 correctly uses `(-,+,+,+)` for the emergent spacetime where BW, Raychaudhuri, and Lovelock operate. No sign error.

### 1b. Natural Units

**Convention lock:** `hbar=1, k_B=1, lattice spacing a=1`
**Phase 37:** `hbar=1, k_B=1, a=1` (ASSERT_CONVENTION header on all three files)

**Assessment: CONSISTENT.** All three Phase 37 derivation files assert natural units matching the convention lock exactly.

### 1c. Coupling Convention

**Convention lock:** `J > 0 antiferromagnetic`
**Phase 37:** `J > 0 AFM` (all three files)

**Assessment: CONSISTENT.**

### 1d. Modular Hamiltonian Convention

**Phase 35 established:** $K_A = -\ln \rho_A$ (positive operator), Eq. (35.0a)
**Phase 37 Gap C chain:** $K_A = -\ln \rho_A$, $\rho_A = e^{-K_A}/Z$ (Step 1, line 33)
**Phase 37 Gap D chain:** $K_A = -\ln \rho_A$ (Step 1, line 35)
**Phase 37 dependency theorem:** $K_A = -\ln \rho_A$ (Section 1, UC7* note)

**Assessment: CONSISTENT.** Sign convention (K_A positive, $\rho_A = e^{-K_A}/Z$) uniform across all Phase 35/36/37 documents.

### 1e. KMS Temperature

**Phase 35 established:** $\beta_{\text{mod}} = 1$ for modular flow; $\beta_{\text{phys}} = 2\pi/a$ for Rindler
**Phase 37 Gap D chain:** $\beta_{\text{mod}} = 1$ (Step 2, line 66); $\beta_{\text{phys}} = 2\pi/a$ (Step 3, line 105)

**Assessment: CONSISTENT.** The crucial factor of $2\pi$ is correctly propagated from Phase 35 Eq. (35.0a) through Phase 37's closure chains.

### 1f. Gap Scoring Rubric

**Convention:** CLOSED / NARROWED / CONDITIONAL / OPEN
**Phase 37:** Uses these four canonical scores consistently, plus two new intermediate scores (CONDITIONAL-DERIVED for Gap C, CONDITIONAL-THEOREM for Gap D). The intermediate scores are clearly defined as upgrades from CONDITIONAL that remain below CLOSED.

**Assessment: CONSISTENT.** The new intermediate scores are well-defined extensions of the rubric, not violations. The ordering OPEN < CONDITIONAL < CONDITIONAL-DERIVED/THEOREM < NARROWED < CLOSED is maintained.

### 1g. State Normalization

**Convention lock:** `density matrices trace 1`
**Phase 37:** Uses $\text{Tr}(\rho) = 1$ implicitly throughout (e.g., Gap D, $S(\rho) = -\text{Tr}(\rho \ln \rho)$).

**Assessment: CONSISTENT.**

### 1h. Spin Basis, Custom Conventions

Jordan product, Peirce eigenvalues, octonion convention, complex structure, Clifford signature: **Not used in Phase 37.** Phase 37 works entirely within the BW/Lovelock/Gibbs framework, which does not reference the algebraic structures from Phases 28-30. No convention interaction to check.

**Assessment: N/A (correctly absent).**

---

## 2. Provides/Requires Consistency

### 2a. Phase 35 -> Phase 37

**Consumed by Phase 37:**
| Quantity | Phase 35 Source | Phase 37 Usage | Match? |
|----------|----------------|----------------|--------|
| $K_A = 2\pi K_{\text{boost}}$ | Eq. (35.0a) | Gap C Step 1, Gap D Step 1 | YES |
| KMS at $\beta_{\text{mod}} = 1$ | Eq. (35.8) | Gap D Step 2 | YES |
| $\theta = \sigma = 0$ at bifurcation | Eqs. (35.19), (35.21) | Gap C Step 4 (derived from Killing) | YES |
| $T_U = a/(2\pi)$ | Eq. (35.3) | Gap D Step 3 | YES |
| SRF = 0.9993 | Phase 35 Step 9 | Gap D Sorce analysis | YES |

**Semantic check:** Phase 37 correctly interprets $K_A = 2\pi K_{\text{boost}}$ as the modular Hamiltonian being $2\pi$ times the boost generator (not $K_{\text{boost}}$ alone). The factor of $2\pi$ is explicitly load-bearing (Phase 35 line 27: "The factor of $2\pi$ is load-bearing").

**Test value:** $\beta_{\text{mod}} = 1$ (modular time periodicity) converts to $\beta_{\text{phys}} = 2\pi/a$ via $t = a\tau/(2\pi)$. Phase 37 Gap D Step 3 line 105 gives $\beta_{\text{phys}} = 2\pi/a$, $T_U = a/(2\pi)$. This matches Phase 35 Eq. (35.3). PASS.

### 2b. Phase 36 -> Phase 37

**Consumed by Phase 37:**
| Quantity | Phase 36 Source | Phase 37 Usage | Match? |
|----------|----------------|----------------|--------|
| Gap A: NARROWED (d>=3) | Gap scorecards | Theorem part (i), Section 4 | YES |
| Gap B: CLOSED (d=1 Route A) | Gap scorecards | Theorem part (ii), Section 5 | YES |
| Gap C: CONDITIONAL | Gap scorecards | Section 6 baseline | YES |
| Gap D: CONDITIONAL | Gap scorecards | Section 6 baseline | YES |
| Derivation chain links (a)-(f) | derivations/36-derivation-chain.md | Referenced in theorem proof sketch | YES |

**Assessment: CONSISTENT.** Phase 37 correctly imports v9.0 baseline scores and upgrades only Gap C and D (with explicit justification). Gaps A and B scores are explicitly stated as unchanged.

### 2c. Phase 37 Plan 01 -> Plan 02

**Consumed by Plan 02:**
| Quantity | Plan 01 Source | Plan 02 Usage | Match? |
|----------|----------------|----------------|--------|
| Gap C assumption list: UC5, UC6, UC8, UC9, UC10 | Gap C chain conclusion | Section 1 assumption list | YES |
| Gap D assumption list: UC5, CS, TL | Gap D chain conclusion | Section 1 assumption list | YES |
| Gap C tensoriality DERIVED | Gap C chain key result | Section 6 upgrade assessment | YES |
| Gap D MVEH THEOREM | Gap D chain key result | Section 6 upgrade assessment | YES |
| Sorce two-tier analysis | Gap D Sorce caveat section | Theorem part (iv), Section 6 | YES |

**Assessment: CONSISTENT.** Plan 02 faithfully assembles Plan 01's results without altering claims.

---

## 3. Sign and Factor Spot-Checks

### 3a. Area Deficit Sign (Eq. 37.4)

$$\delta A = -\frac{\Omega_{d-2} \ell^d}{2(d^2-1)} R_{ik}{}^{ik}$$

**Convention check:** The minus sign means positive Ricci curvature ($R_{ab} k^a k^b > 0$, which holds for matter satisfying the null energy condition) causes area DECREASE. This is physically correct: positive curvature causes geodesics to converge (Raychaudhuri focusing), reducing the cross-sectional area.

**Cross-reference:** This matches Jacobson (2016), PRL 116, 201101, Eq. (5). The sign is consistent with the mostly-minus metric convention $(-,+,+,+)$ used throughout Phase 37.

**Assessment: CONSISTENT.**

### 3b. Entanglement First Law Sign (Eq. 37.1)

$$\delta S_A = \delta \langle K_A \rangle$$

With $K_A = -\ln \rho_A$ (positive operator): increasing $K_A$ means $\rho_A$ becomes less mixed (peaked on fewer states), which decreases $S_A$. But the first law is about first-order variations around the reference state, where $\delta S_A = \delta \langle K_A \rangle$ is an exact identity from the expansion $S(\rho + \delta\rho) - S(\rho) = -\text{Tr}(\delta\rho \ln \rho) - \text{Tr}(\delta\rho) + O(\delta^2) = \text{Tr}(\delta\rho \, K_A) = \delta \langle K_A \rangle$.

**Convention consistency:** With $K_A = -\ln \rho_A$, we have $\delta S_A = \delta \langle K_A \rangle = \delta(-\text{Tr}(\rho_A \ln \rho_A)) / \delta\rho_A$ evaluated correctly. The sign is right: $\delta S = \delta \langle K \rangle$ (positive = positive).

**Assessment: CONSISTENT.**

### 3c. Free Energy Minimization (Eq. 37.8)

$$\delta F = \delta \langle K_A \rangle - \delta S = 0$$

Combined with the entanglement first law $\delta S = \delta \langle K_A \rangle$, this gives $\delta F = 0$ identically at first order. The Gibbs variational principle says the KMS state MINIMIZES $F = \langle K \rangle - S$ (not maximizes). This is consistent because $F = \langle K \rangle - S$ and the KMS state has $\delta F = 0$ (stationarity) with $\delta^2 F \geq 0$ (concavity of $S$ implies $-\delta^2 S \geq 0$, hence $\delta^2 F = \delta^2 \langle K \rangle - \delta^2 S \geq 0$ for perturbations at fixed $K$).

**Assessment: CONSISTENT.**

### 3d. Einstein Equation Sign (Eq. 37.6)

$$G_{ab} + \Lambda g_{ab} = 8\pi G_N T_{ab}$$

With $G_N = 1/(4\eta)$ where $\eta > 0$ (positive area-entropy proportionality constant). The sign convention: positive energy density $T_{00} > 0$ on the RHS gives positive $R_{00}$ (via trace-reversed Einstein), which causes geodesic convergence (Raychaudhuri). This is the standard GR sign convention in mostly-minus signature.

**Assessment: CONSISTENT with standard physics.**

---

## 4. Cross-Phase Convention Interactions

### 4a. Fisher Metric (Riemannian) vs Spacetime Metric (Lorentzian)

Phase 33 uses `metric_signature=Riemannian_Fisher` for the spatial Fisher metric $g_F(x)$.
Phase 34 uses `metric_signature=Riemannian_Fisher` and constructs the Lorentzian extension $ds^2 = -c_s^2 dt^2 + g_{ij} dx^i dx^j$.
Phases 35-37 use `metric_signature=mostly_minus` for the full spacetime metric.

The convention_lock records the Fisher metric signature. The ASSERT_CONVENTION headers correctly track which metric is in play. Phase 36's explicit documentation (derivation chain, line 18) bridges the two. No silent convention drift.

### 4b. Coupling Convention Across Phases

Phase 33: `J_gt_0_AFM` (same as `J > 0 antiferromagnetic`)
Phase 34: `J>0_AFM`
Phase 35: `J>0 AFM`
Phase 36: `J_gt_0_AFM`
Phase 37: `J>0_AFM`

These are notational variants of the same convention. No physical inconsistency.

### 4c. Modular Hamiltonian Sign Across Phases

Phase 35: $K_A = -\ln \rho_A$ (Eq. 35.0a), explicitly "positive operator"
Phase 36: $K_A = -\ln \rho_A$ (derivation chain, ASSERT_CONVENTION)
Phase 37: $K_A = -\ln \rho_A$ (all three files)

No sign flip anywhere in the chain. The dangerous pattern (some authors use $K = +\ln \rho$, making it negative) does not appear.

---

## 5. Approximation Validity

No new numerical parameter values are introduced in Phase 37. The phase is purely logical/structural (closure chains and dependency theorem). The only numerical value referenced is SRF = 0.9993 from Phase 35, used in the Sorce caveat analysis for Gap D. This value is used correctly (as evidence for approximate geometric content in non-conformal theories, not as an input to any calculation).

No approximation validity boundaries are violated.

---

## 6. Compliance Matrix (Phase 37 vs Full Conventions Ledger)

| Convention | Locked Value | Phase 37 | Compliant? | Notes |
|-----------|-------------|----------|-----------|-------|
| metric_signature | (+,+,...,+) Riemannian Fisher | (-,+,+,+) Lorentzian spacetime | YES | Different physical objects; documented in Phase 36 |
| natural_units | hbar=1, k_B=1, a=1 | hbar=1, k_B=1, a=1 | YES | |
| coupling_convention | J > 0 AFM | J > 0 AFM | YES | |
| spin_basis | standard S^z eigenbasis | N/A | N/A | Phase 37 does not use spin variables |
| state_normalization | Tr(rho)=1 | Tr(rho)=1 (implicit) | YES | |
| Entropy base | nats (ln) | ln used in S_vN = -Tr(rho ln rho) | YES | |
| Jordan product | a o b = (1/2)(ab+ba) | N/A | N/A | Not used in Phase 37 |
| Peirce eigenvalues | {0, 1/2, 1} | N/A | N/A | Not used in Phase 37 |
| Octonion convention | Fano e_1 e_2 = e_4 | N/A | N/A | Not used in Phase 37 |
| Complex structure | u = e_7 | N/A | N/A | Not used in Phase 37 |
| Clifford signature | Cl(9,0) | N/A | N/A | Not used in Phase 37 |
| Modular Hamiltonian | K_A = -ln(rho_A) | K_A = -ln(rho_A) | YES | Consistent across Phases 35-37 |
| KMS temperature | beta_mod=1, beta_phys=2pi/a | beta_mod=1, beta_phys=2pi/a | YES | Factor of 2pi correctly propagated |
| Gap scoring | CLOSED/NARROWED/CONDITIONAL/OPEN | Extended with CONDITIONAL-DERIVED, CONDITIONAL-THEOREM | YES | Extensions are well-defined |

---

## 7. Issues Found

None.

---

## Summary

**Checks performed:** 14

| Check Category | Count | Pass | Fail | N/A |
|---------------|-------|------|------|-----|
| Convention compliance | 8 | 6 | 0 | 2 |
| Provides/requires transfers | 3 | 3 | 0 | 0 |
| Sign/factor spot-checks | 4 | 4 | 0 | 0 |
| Approximation validity | 1 | 1 | 0 | 0 |
| Cross-phase interactions | 3 | 3 | 0 | 0 |

**Consistency status: CONSISTENT**

All Phase 37 artifacts are convention-compliant with the full project conventions ledger. The provides/requires chain from Phases 35-36 into Phase 37 is semantically correct. Sign conventions (metric, modular Hamiltonian, area deficit, Einstein equation) are uniform. The metric_signature apparent discrepancy (Riemannian in convention_lock vs Lorentzian in Phase 37) is a documented, physically justified distinction between the spatial Fisher metric and the emergent spacetime metric, not a drift.

---

_Checked: 2026-03-30_
_Mode: rapid_
_Phase: 37-gap-dependency-theorem_
