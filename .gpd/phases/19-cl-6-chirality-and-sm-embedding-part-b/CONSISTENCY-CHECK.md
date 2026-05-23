# Phase 19 Consistency Check

**Mode:** rapid
**Phase:** 19 -- Cl(6) Chirality and SM Embedding (Part B)
**Date:** 2026-03-23
**Scope:** Phase 19 Plans 01 and 02 checked against CONVENTIONS.md and Phase 18 provides

---

## 1. Convention Compliance

### Conventions Ledger Status

The project CONVENTIONS.md was established for the algebraic/information-theoretic framework (Phases 1-12). Phase 19 introduces Clifford algebra and spinor conventions that are **new** to the project. The conventions ledger marks gamma matrices, Levi-Civita sign, generator normalization, covariant derivatives, and creation/annihilation ordering as "N/A" -- but Phase 19 now uses all of these. The STATE.md convention_lock similarly has these as N/A.

**Finding (WARNING):** The conventions ledger has not been updated for Phase 19's new conventions. Phase 19 defines its own conventions in SUMMARY frontmatter and in ASSERT_CONVENTION headers of derivation and test files:

- `clifford_convention = euclidean_positive` ({gamma_i, gamma_j} = 2 delta_ij)
- `octonion_basis = fano_e1e2=e4`
- `complex_structure = u = e_7`
- `witt_operators = a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j})`
- `hypercharge = pati_salam_Y = (B-L) + 2*J3R`
- `su2_construction = schwinger_boson_from_cl4_witt`
- `spin_representation = S10plus_boyle`

These are self-consistent within Phase 19 (verified below) but should be propagated to CONVENTIONS.md and convention_lock before Phase 20.

### Relevant Convention Types (of the 18 canonical)

| # | Convention | Status | Detail |
|---|-----------|--------|--------|
| 3 | Natural units | Compliant | Dimensionless algebraic work, consistent with ledger |
| 13 | Commutation convention | Compliant | [A,B] = AB - BA used throughout |
| 14 | Levi-Civita sign | Newly relevant | omega_6 = gamma_1...gamma_6 implicitly fixes orientation; self-consistent |
| 15 | Generator normalization | Newly relevant | SU(2) algebra [J+, J-] = 2*J3 (standard); SU(3) Cartan T3c, T8c standard Gell-Mann |
| 17 | Gamma matrix convention | Newly relevant | Euclidean positive-definite: {gamma_i, gamma_j} = 2*delta_ij throughout |
| 18 | Creation/annihilation order | Newly relevant | a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}), {a_i, a_j^dag} = delta_ij |
| -- | Custom: S_{10}^+ convention | Newly relevant | Boyle convention for positive-chirality Weyl spinor |

All other canonical conventions remain N/A for this algebraic phase.

---

## 2. Phase 18 -> Phase 19 Data Handoff

### 2a. S_{10}^+ (Weyl spinor, 16-dim complex)

**Producer (Phase 18-01):** V_{1/2}^C = S_{10}^+ established as complexified Peirce V_{1/2} space. dim_C = 16. S_9 tensor_R C = S_{10}^+.

**Consumer (Phase 19-01):** Uses S_{10}^+ as one Weyl component of the 32-dim Dirac spinor Delta_10 = S_{10}^+ + S_{10}^-. The Cl(6) volume form omega_6 acts on the full Dirac spinor and projects to a DIFFERENT 16-dim subspace.

**Meaning match:** Yes -- both phases refer to the positive-chirality Weyl spinor of Spin(10), 16-dim complex.

**Units/dimensions:** Both dimensionless (algebraic). Consistent.

**Test value:** dim_C(S_{10}^+) = 16 in Phase 18 = tr(P) in Phase 19. PASS.

**Convention match:** Both use S_{10}^+ label following Boyle 2020. CONSISTENT.

**Clarification needed:** Phase 19 SUMMARY (ref-phase18) states "The 16-dim Weyl spinor from Phase 18 is the space on which Cl(6) acts." This is imprecise. Cl(6) acts on the full 32-dim Dirac spinor. The omega_6 projector P selects a 16-dim subspace that is DIFFERENT from S_{10}^+ (numerically verified: tr(P * P_Weyl) = 8, not 16, where P_Weyl projects onto S_{10}^+ via Gamma_11). The S_{10}^+ from Phase 18 is the representation-theoretic context; Phase 19's P-projected space is a physically different 16-dim subspace. This does not affect any results because the code works on the full 32-dim space and projects correctly.

**Status:** CONSISTENT (with minor text imprecision noted)

### 2b. 27 -> 1 + 10 + 16 decomposition (Spin(10))

**Producer (Phase 18-02):** 27 = 1 (V_1^C) + 10 (V_0^C) + 16 (V_{1/2}^C = S_{10}^+) under Spin(10).

**Consumer (Phase 19):** The 16 from this decomposition is the starting point for the Cl(6) chirality construction. Phase 19 does not directly use the 1 or 10, which are for Phase 20.

**Status:** CONSISTENT.

### 2c. Spin(10) x U(1) stabilizer

**Producer (Phase 18-02):** Stab_{E_6}(E_11) = Spin(10) x U(1), dim = 46.

**Consumer (Phase 19):** Uses Spin(10) as the group whose stabilizer under omega_6 gives Pati-Salam. The U(1) factor (B-L charges -4, 2, -1) is consumed in Phase 19 Plan 02 where B-L = 1 - (2/3)N.

**Status:** CONSISTENT.

---

## 3. Plan 01 <-> Plan 02 Internal Consistency

### 3a. Clifford convention

Both plans use {gamma_i, gamma_j} = 2*delta_ij (Euclidean positive-definite). Verified: 21 Cl(6) and 55 Cl(10) anticommutator relations all exact (error = 0) in the 32x32 matrix representation.

**Status:** CONSISTENT.

### 3b. omega_6^2 = -1

Plan 01 derives omega_6^2 = (-1)^{n(n-1)/2} = (-1)^{15} = -1 analytically.
Plan 02 verifies omega_6^2 = -I_{32} numerically (error = 0).

**Status:** CONSISTENT.

### 3c. omega_6 eigenvalue selected by P [**WARNING**]

Plan 01 Step 4 text states: "The projector P = (1/2)(1 - i*omega_6) selects the eigenspace with eigenvalue -i."

Plan 01 Step 9 text states: "P = (1/2)(1 - i*omega_6) selects the omega_6 = -i eigenspace (even particle number)."

Plan 02 SUMMARY correctly states: "P selects omega_6 = +i eigenspace = odd N."

**Algebraic verification:**
For an eigenstate |v> with omega_6|v> = lambda|v>:
P|v> = (1/2)(1 - i*lambda)|v>
- lambda = +i: (1/2)(1 - i*(+i)) = (1/2)(1+1) = 1 -> SELECTED
- lambda = -i: (1/2)(1 - i*(-i)) = (1/2)(1-1) = 0 -> PROJECTED OUT

**Conclusion:** P = (1/2)(I - i*omega_6) selects the omega_6 = **+i** eigenspace, not -i. The Plan 01 derivation text (Steps 4 and 9) contains an incorrect claim about which eigenvalue P selects. Plan 02 code and SUMMARY are correct. The derivation Step 9 also correctly computes that odd-N states have omega_6 = +i and then incorrectly states P selects the -i eigenspace, but the "Wait --" correction paragraph resolves the dimension puzzle by noting the Cl(10) tensor product structure.

**Impact:** LOW. The incorrect text in Steps 4 and 9 does not propagate to any computed result because:
1. Plan 02 code correctly implements P = (1/2)(I - i*omega_6) and projects onto the right states
2. All 16 SM quantum numbers come from the code, not from the erroneous text
3. The particle interpretation (N=1 quarks, N=3 leptons) is correct in both plans
4. All 29 pytest tests pass

**Recommended fix:** Correct the text in derivations/12-cl6-chirality.md:
- Step 4, line 124: Change "eigenvalue -i" to "eigenvalue +i"
- Step 9, line 355: Change "selects the omega_6 = -i eigenspace (even particle number)" to "selects the omega_6 = +i eigenspace (odd particle number)"

### 3d. Witt operator convention

Plan 01: a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j})
Plan 02: Same formula, verified numerically (error = 0 for all 3 operators).

**Status:** CONSISTENT.

### 3e. gamma_{2j-1} * gamma_{2j} = i*(1 - 2*n_j)

Derived analytically in Step 9, verified numerically (error = 0 for all 3 pairs).

**Status:** CONSISTENT.

### 3f. omega_6 = -i * (-1)^N

Derived analytically in Step 9, verified numerically (error = 3.7e-16 ~ machine epsilon).

**Status:** CONSISTENT.

### 3g. Schwinger boson SU(2)

Plan 02: J3L = (m1 + m2 - 1)/2, J3R = (m1 - m2)/2.
SU(2)_L algebra verified: [J+L, J-L] = 2*J3L, [J3L, J+/-L] = +/-*J+/-L. All exact.
SU(2)_R algebra verified: Same structure. All exact.
L-R commutativity: all 9 cross-commutators = 0. Exact.
Both commute with omega_6: verified. Exact.

This convention is introduced in Plan 02 (not present in Plan 01). Internal consistency verified.

**Status:** CONSISTENT.

### 3h. B-L formula

Plan 02: B-L = 1 - (2/3)*N.
Test values: N=1 -> B-L = +1/3 (quarks), N=3 -> B-L = -1 (leptons). Correct.
Plan 02 SUMMARY notes the sign was initially wrong ((2/3)N - 1) and corrected -- a bug fix deviation, properly documented.

**Status:** CONSISTENT.

---

## 4. Approximation Validity

No approximations used in Phase 19 -- all results are exact algebraic/representation-theoretic. No parameter ranges to violate.

**Status:** N/A.

---

## 5. Spot-Check: 3 Key Equations

### Eq (19-01.2): omega_6^2 = (-1)^{6*5/2} = (-1)^{15} = -1

Verified: omega_6^2 + I_{32} has max element error = 0. PASS.

### Eq (19-01.8): omega_6 = -i * (-1)^N

Verified: max element error = 3.7e-16 (machine epsilon). PASS.

### Eq (19-02.3): Q = J3L + Y/2, Y = (B-L) + 2*J3R, B-L = 1 - (2/3)*N

Verified for all 16 states: Gell-Mann-Nishijima max error = 0. Y formula max error = 0. PASS.

---

## Summary

| Check | Count | Pass | Fail | Warning |
|-------|-------|------|------|---------|
| Convention compliance | 7 | 7 | 0 | 0 |
| Provides/requires pairs | 3 | 3 | 0 | 0 |
| Plan 01/02 internal consistency | 8 | 7 | 0 | 1 |
| Spot-check equations | 3 | 3 | 0 | 0 |
| Approximation validity | 0 | -- | -- | -- |
| **Total** | **21** | **20** | **0** | **1** |

### Issues Found

1. **WARNING -- omega_6 eigenvalue text error in derivation:** Steps 4 and 9 of derivations/12-cl6-chirality.md claim P selects the omega_6 = -i eigenspace. Algebra and code show P selects omega_6 = +i. Impact: LOW (text only; code and results correct). Fix: edit two sentences in the derivation.

2. **NOTE -- Conventions ledger not updated:** CONVENTIONS.md and STATE.md convention_lock still have gamma matrices, creation/annihilation ordering, etc. as "N/A" despite Phase 19 introducing these. Should be updated before Phase 20.

3. **NOTE -- S_{10}^+ clarification:** Phase 19 SUMMARY ref-phase18 text "The 16-dim Weyl spinor from Phase 18 is the space on which Cl(6) acts" is imprecise. Cl(6) acts on the 32-dim Dirac spinor; the P-projected 16-dim subspace differs from S_{10}^+ (overlap = 8 dimensions, not 16). No physics impact.

---

_Consistency check by: gpd-consistency-checker (rapid mode)_
_Checked: 2026-03-23_
