# Consistency Check: Phase 34 (Emergent Lorentz Invariance)

**Mode:** Rapid
**Date:** 2026-03-29
**Phase checked:** 34-emergent-lorentz-invariance (Plans 01 + 02)
**Checked against:** Full convention lock (STATE.md), Phase 33 sigma model results, Phase 32 Fisher metric results

---

## Convention Compliance (All 18 Types)

| # | Convention | Convention Lock Value | Relevant? | Compliant? | Evidence |
|---|-----------|----------------------|-----------|------------|----------|
| 1 | Metric signature | (+,...,+) Riemannian Fisher | Yes | Yes | Fisher metric explicitly Riemannian (spatial). Emergent Lorentzian (-,+,...,+) distinguished. fp-fisher-is-lorentzian rejected in both plans. |
| 2 | Fourier convention | N/A (lattice spin chain) | Marginal | Yes | Plan 01 asserts e^{-ikx} forward (used in dispersion expansion). Consistent with Fourier used in propagator Eq. (34.25-27). |
| 3 | Natural units | hbar=1, k_B=1, a=1 | Yes | Yes | All expressions use a=1, hbar=1. Dimensional checks pass ([c_s]=J, [v_LR]=J, [tau]=1/J). |
| 4 | Gauge choice | N/A | No | N/A | No gauge fields in sigma model. |
| 5 | Regularization | N/A | No | N/A | Lattice is the regulator. |
| 6 | Renormalization | N/A | Marginal | Yes | Z_c renormalization factor from Phase 33 propagated correctly (c_s = Z_c * sqrt(2) * Ja = 1.664 vs QMC 1.659). |
| 7 | Coordinate system | N/A | No | N/A | Standard Cartesian on square lattice. |
| 8 | Spin basis | S^z eigenbasis | No | N/A | Phase 34 works at sigma model level (classical field n), not spin basis. |
| 9 | State normalization | density matrices trace 1 | No | N/A | No density matrices in Phase 34 derivations. |
| 10 | Coupling convention | J > 0 AFM | Yes | Yes | All expressions use J > 0. omega_q > 0 (physical). H = J sum S_i.S_j with J > 0. |
| 11 | Index positioning | N/A | No | N/A | |
| 12 | Time ordering | N/A | No | N/A | |
| 13 | Commutation convention | N/A | No | N/A | |
| 14 | Levi-Civita sign | N/A | No | N/A | |
| 15 | Generator normalization | N/A | No | N/A | |
| 16 | Covariant derivative sign | N/A | No | N/A | |
| 17 | Gamma matrix convention | N/A | No | N/A | |
| 18 | Creation/annihilation order | N/A | No | N/A | |

**Custom conventions checked:**

| Convention | Value | Compliant? | Evidence |
|-----------|-------|------------|----------|
| Jordan Product | a o b = (1/2)(ab+ba) | N/A | Not used in Phase 34 |
| Peirce Eigenvalues | {0, 1/2, 1} | N/A | Not used in Phase 34 |
| Octonion Convention | Fano e_1 e_2 = e_4 | N/A | Not used in Phase 34 |
| Clifford Signature | Cl(9,0) | N/A | Not used in Phase 34 |
| Sigma model field | O(3) n-field, n^2=1 | Yes | Consistent throughout both plans |
| Fisher metric | SLD, g_F = 4*g_Bures | Yes | Stated in Plan 02 conventions |

---

## Provides/Consumes Verification

### Consumed from Phase 33 (Plan 01)

| Quantity | Phase 33 Value | Phase 34 Value | Match? |
|----------|---------------|----------------|--------|
| c_s (spin-wave velocity) | 1.659 Ja (QMC: 1.65880(6)) | 1.659 Ja | YES |
| Sigma model action Eq. (33.11) | S = 1/(2g) int [(d_tau n)^2/c_s^2 + (nabla n)^2] | Identical form used as starting point | YES |
| rho_s (spin stiffness) | 0.181 J (QMC: 0.180752) | 0.181 J | YES |
| chi_perp (transverse suscept.) | 0.0657/J (QMC: 0.065690) | 0.0657/J | YES |
| g (sigma model coupling) | 9.18 | 9.18 | YES |
| c_s^cl (classical) | sqrt(2) Ja | sqrt(2) Ja (Eq. 34.7 context) | YES |

**Test value:** g = d*c_s/(2*rho_s) = 2*1.659/(2*0.181) = 9.16 (vs reported 9.18 using QMC values: 2*1.65880/(2*0.180752) = 9.18). PASS.

**Test value:** 1/(2gc_s) = 1/(2*9.18*1.659) = 0.0328. rho_s/(d*c_s^2) = 0.181/(2*1.659^2) = 0.0329. PASS (0.03% agreement, as stated in derivation).

### Consumed from Phase 32 (Plan 02)

| Quantity | Phase 32 Value | Phase 34 Value | Match? |
|----------|---------------|----------------|--------|
| Fisher metric g_ij | Positive-definite at interior (OBC, finite N) | Used as spatial metric component | YES |
| Fisher metric = Riemannian | Positive-definite, spatial only | Explicitly stated as spatial only | YES |

**Note:** Phase 32 found d_Fisher/d_lattice -> 0 as N -> infinity in 1D. Phase 34 Plan 02 uses Fisher metric for d >= 2 Neel phase, where Phase 33 CORR-03 establishes g_F ~ O(m_s^2) > 0. This is consistent: the 1D failure is acknowledged, and the d >= 2 case is properly conditioned on CORR-03 hypotheses H1-H4.

### Provided to Phase 35 (downstream)

| Quantity | Value | Status |
|----------|-------|--------|
| Emergent metric ds^2 | -c_s^2 dt^2 + g_ij dx^i dx^j | Established |
| Lorentz invariance | SO(d,1) with speed c_s | Derived via two routes |
| c_s = c_eff | 1.659 Ja | Four-argument justification |
| Reflection positivity | DLS 1978, bipartite lattice | Cited (theorem-level) |

---

## Sign and Factor Spot-Checks

### Check 1: Euclidean time rescaling (load-bearing)

**Equation:** tau' = c_s * tau (Eq. 34.13, corrected version)

Substituting into action:
- (d_tau n)^2/c_s^2 = c_s^2*(d_{tau'} n)^2/c_s^2 = (d_{tau'} n)^2. CORRECT.
- d_tau = d_{tau'}/c_s. CORRECT.
- Result: 1/(2gc_s) int [(d_{tau'} n)^2 + (nabla n)^2]. O(d+1) SYMMETRIC. CORRECT.

### Check 2: Velocity ratio (load-bearing)

v_LR = 8e/(e-1) = 12.6558 J. c_s = 1.65880 J (at a=1). Ratio = 7.63. CORRECT.

### Check 3: Propagator poles (load-bearing)

G_E^{-1} = omega_E^2/c_s^2 + k^2. Wick rotate omega_E -> -i*omega:
G_M^{-1} = (-i*omega)^2/c_s^2 + k^2 = -omega^2/c_s^2 + k^2. Poles: omega = +/- c_s|k|. CORRECT.

### Check 4: Anisotropy coefficient

alpha_4 = -1/96 = -0.01042. At qa = 0.1: anisotropic correction ~ (0.1)^2 * (1/96) ~ 0.01%. CORRECT.

---

## Issues Found

### Issue 1: Rescaling direction inconsistency between derivation files (MINOR)

**Location:** derivations/34-velocity-hierarchy-and-causal-structure.md, lines 118 and 166

**Problem:** File 2 writes the rescaling as "tau' = tau/c_s" in two places (lines 118, 166). File 1 (the primary derivation) self-corrected from tau' = tau/c_s to tau' = c_s*tau (Eq. 34.13 on line 295) and showed that only tau' = c_s*tau produces the O(d+1)-symmetric form.

**Impact:** The written ACTION in file 2 (Eq. 34.7) is correct (it IS the O(d+1) symmetric form). Only the TEXT describing the rescaling direction is wrong. A reader following the text would get a non-symmetric action, but the equation itself is right.

**Classification:** Minor -- text error, equations correct. No impact on physical conclusions.

### Issue 2: Wick rotation direction typo in file 2 (MINOR)

**Location:** derivations/34-velocity-hierarchy-and-causal-structure.md, line 166

**Problem:** Line 166 writes "Wick rotation tau' -> it" (positive i). File 1 correctly uses tau' = -it (Eq. 34.18). The sign of i in the Wick rotation determines the sign of the Minkowski action; using +it instead of -it flips the relation between e^{-S_E} and e^{iS_M}.

**Impact:** Minor text error. The metric equation (34.9) and all physical conclusions are derived from the correct Wick rotation in file 1. File 2 only references the result schematically.

**Classification:** Minor -- text error in supporting document, primary derivation correct.

### Issue 3: Equation numbering collision between derivation files (MINOR)

**Location:** Both derivation files use tag range 34.1-34.12 for different equations.

**Details:**
- File 1: Eq. 34.1 = LSWT dispersion, Eq. 34.7 = anisotropic dispersion, etc.
- File 2: Eq. 34.1 = Lieb-Robinson bound, Eq. 34.7 = rescaled action, etc.

**Impact:** Internal cross-references within each file are consistent (file 2's "Eq. 34.7" on line 166 refers to file 2's own equation, not file 1's). But if a future phase references "Phase 34 Eq. 34.7" without specifying which derivation file, the reference is ambiguous.

**Classification:** Minor documentation issue. No physics impact.

### Issue 4: Overall sign of Minkowski action in Wick rotation (MINOR)

**Location:** derivations/34-emergent-lorentz-invariance.md, Eq. (34.22)

**Problem:** Careful tracking of the Wick rotation from Eq. (34.21) to (34.22) shows an overall sign discrepancy. Starting from S_E = (-i)/(2gc_s) * int [-(d_t n)^2 + (nabla n)^2] and using S_M = S_E/(-i), one obtains S_M = 1/(2gc_s) * int [-(d_t n)^2 + (nabla n)^2] = 1/(2gc_s) * int [(nabla n)^2 - (d_t n)^2]. The derivation Eq. (34.22) instead writes S_M = 1/(2gc_s) * int [(d_t n)^2 - (nabla n)^2].

**Impact:** NONE on physical conclusions. The overall sign of the Lagrangian is a convention (both signs appear in the literature). The equations of motion, propagator poles, and emergent metric are all independent of this sign. The derivation reaches the correct physical conclusions (omega = +/- c_s|k|, ds^2 = -c_s^2 dt^2 + dx^2) regardless.

**Classification:** Minor sign convention ambiguity. Both signs are valid. No downstream impact.

---

## Approximation Validity

| Approximation | Validity Range | Phase 34 Usage | Status |
|--------------|---------------|----------------|--------|
| NL sigma model | ka << 1 | All derivations in continuum limit | VALID |
| Cubic anisotropy irrelevant | L >> a | Continuum limit assumed | VALID |
| Gaussian propagator | weak coupling g | g = 9.18 (not perturbatively small) | NOTED -- g large but sigma model is asymptotically free in d=2; non-perturbative QMC validates |
| Neel order in d=2 | QMC-established, not rigorous | Inherited from Phase 33 | NOTED -- acknowledged uncertainty marker |

No approximation validity violations detected. The large value of g = 9.18 is correctly noted as being in the non-perturbative regime, and QMC validation is cited as the resolution.

---

## Summary

**Checks performed:** 6 (convention compliance matrix, 2 provides/consumes chains, 4 sign/factor spot-checks, equation numbering, approximation validity)

**Issues found:** 4 (all MINOR)
- Rescaling direction text error in file 2 (equations correct)
- Wick rotation sign typo in file 2 text
- Equation numbering collision between two derivation files
- Overall Minkowski action sign convention (no physical impact)

**No convention violations against the full ledger.**
**No provides/consumes mismatches.**
**No approximation validity violations.**
**All load-bearing equations verified numerically.**

---

_Checked: 2026-03-29_
_Mode: rapid_
_Phase: 34-emergent-lorentz-invariance_
