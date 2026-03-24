# Consistency Check: Phase 20 -- Synthesis: One Choice, Two Consequences

**Mode:** Rapid (post-phase)
**Checked:** 2026-03-24
**Scope:** Phase 20 (Plans 01 and 02) against Phases 18-19 and full conventions ledger

---

## 1. Convention Compliance

### ASSERT_CONVENTION Alignment Across Phases 18-20

| Convention | Phase 18 (11-peirce) | Phase 19 (12-cl6) | Phase 20 (13-synthesis) | Match? |
|---|---|---|---|---|
| natural_units | dimensionless | dimensionless | dimensionless | YES |
| jordan_product | (1/2)(ab+ba) | (1/2)(ab+ba) | (1/2)(ab+ba) | YES |
| peirce_decomposition | under_E11 | under_E11 | under_E11 | YES |
| clifford_convention | (not in Phase 18) | euclidean_positive | euclidean_positive | YES |
| octonion_basis | (not in Phase 18) | fano_e1e2=e4 | fano_e1e2=e4 | YES |
| complex_structure | (not in Phase 18, but u=e_7 used) | u_equals_e7 | u_equals_e7 | YES |
| spin_representation | (not in Phase 18 assert, but S10+ used) | S10plus_boyle | S10plus_boyle | YES |

**Finding:** Phase 18 (derivation 11-peirce-complexification.md) has a narrower ASSERT_CONVENTION header (`natural_units=dimensionless, jordan_product=(1/2)(ab+ba), peirce_decomposition=under_E11, octonion_notation=O_8dim`) because it precedes the Clifford algebra construction. The Clifford and octonion basis conventions are introduced in Phase 19 and correctly inherited by Phase 20. No drift detected.

**Phase 18 implicit conventions check:** Phase 18 Step 8 adopts S_{10}^+ (Boyle convention) and explicitly notes "We denote the complexified spinor as S_{10}^+ following the convention of Boyle 2020." Phase 19 and 20 consume this as S_{10}^+ consistently.

### Full Conventions Ledger Compliance

The project-level CONVENTIONS.md marks all QFT-standard conventions as N/A (this is an algebraic/categorical project). The v5.0 work introduces physics-specific conventions not in the original ledger:

| Convention (v5.0 specific) | Defined in | Used in Phase 20 | Compliant? |
|---|---|---|---|
| Clifford: {gamma_i, gamma_j} = 2*delta_ij (Euclidean, positive) | Phase 19 | Phase 20 Step 5 (Route B table) | YES |
| Octonion basis: Fano, e_1*e_2 = e_4 | Phase 19 | Phase 20 Steps 2, 5-7 | YES |
| Complex structure: u = e_7 | Phase 19 | Phase 20 Steps 1-12 | YES |
| S_{10}^+ = positive-chirality Weyl (Boyle) | Phase 18 | Phase 20 Step 10 | YES |
| Pati-Salam: SU(4) x SU(2)_L x SU(2)_R | Phase 19 | Phase 20 Steps 8, 10-11 | YES |
| omega_6^2 = -1 | Phase 19 | Phase 20 Step 5 Route B table | YES |
| P = (1/2)(1 - i*omega_6) | Phase 19 | Phase 20 (implicit, via "selects chiral") | YES |
| LEFT embedding: (4,2,1) + (4bar,1,2) | Phase 19 | Phase 20 Steps 10-11 | YES |
| Witt: a_j = (1/2)(gamma_{2j-1} + i*gamma_{2j}) | Phase 19 | Phase 20 Step 7 (reference to Witt pairing) | YES |

**Note on convention ledger gap:** The project CONVENTIONS.md was established during v1.0 (information-theoretic phase) and has not been updated to include v5.0 Clifford/octonion conventions. This is a minor infrastructure issue -- the conventions ARE consistently applied across Phases 18-20, they are just not recorded in the top-level ledger. The per-derivation ASSERT_CONVENTION headers serve as the de facto convention ledger for v5.0.

---

## 2. Provides/Requires Chain Verification

### Phase 18 -> Phase 20 (Plan 01)

| Quantity | Phase 18 provides | Phase 20 consumes | Meaning match | Value match |
|---|---|---|---|---|
| Peirce decomposition | 27 = 1 + 16 + 10 under E_11 | Step 1: "Peirce decomposition (Phase 18, Step 2)" | YES | YES (1+16+10=27) |
| Stab_{F_4}(E_11) = Spin(9) | dim(Spin(9)) = 36 | Step 1: "dim(Spin(9)) = 36" | YES | YES (36 = 9*8/2) |
| Spin(9) -> Spin(10) upgrade | S_9 tensor C = S_{10}^+ | Step 1: "upgrades to Spin(10)" | YES | YES |
| F_4 -> E_6 | Phase 18 Plan 02 | Step 1: "F_4 -> E_6" | YES | YES |
| 27 -> 1 + 10 + 16 under Spin(10) | Phase 18 Plan 02 | Step 1: "27 -> 1 + 10 + 16" | YES | YES |

### Phase 19 -> Phase 20 (Plan 01)

| Quantity | Phase 19 provides | Phase 20 consumes | Meaning match | Value match |
|---|---|---|---|---|
| O = C + C^3 splitting | W = span{e_1,...,e_6}, u = e_7 | Step 5 Route B: "same Im(O) = span{u} + W" | YES | YES (W identical) |
| Cl(6) from W | gamma_1,...,gamma_6 from W | Step 5 Route B: "W provides 6 real directions" | YES | YES |
| omega_6 | omega_6 = gamma_1...gamma_6, omega_6^2 = -1 | Step 5 Route B: "omega_6, omega_6^2 = -1" | YES | YES |
| Pati-Salam stabilizer | Stab_{Spin(10)}(omega_6) = [SU(4) x SU(2)_L x SU(2)_R]/Z_2, dim 21 | Step 5 Route B: "SU(4) x SU(2)_L x SU(2)_R, dim 21" | YES | YES (15+6=21) |
| LEFT embedding | 16 -> (4,2,1) + (4bar,1,2) | Step 10(b), Step 11 table | YES | YES (8+8=16) |
| SU(4) -> SU(3) x U(1) | From same u breaking SU(4) | Step 5 Route B: "SU(3)_C x U(1)_{B-L}" | YES | YES |

### Phase 20 Plan 01 -> Plan 02

| Quantity | Plan 01 provides | Plan 02 consumes | Meaning match | Value match |
|---|---|---|---|---|
| F_4 intersection route | SM = SU(3) x SU(2) x U(1), dim 12 | L8 in chain table | YES | YES |
| Single-input theorem | Both routes use same u, same W | L9, Step 18 | YES | YES |
| Chiral upgrade | F_4 = no chirality, Cl(6) = LEFT | Synthesis theorem part (iii) | YES | YES |
| Gap statement | E_11, u, generations, spectral action | Gap register Step 19 | YES | YES (5 gaps) |

**All provides/requires pairs verified.** No mismatches.

---

## 3. Sign and Factor Spot-Checks

### Check 1: Dimension of [SU(3) x SU(3)]/Z_3

Phase 20 Step 3: dim([SU(3) x SU(3)]/Z_3) = 8 + 8 = 16.

The Z_3 quotient is a finite group (acts by discrete identification), so it does not reduce the Lie algebra dimension. dim(SU(3)) = 3^2 - 1 = 8. Total = 16. **CORRECT.**

### Check 2: SM gauge group dimension from intersection

Phase 20 Step 4: dim(SU(3)_C x SU(2) x U(1)) = 8 + 3 + 1 = 12.

Cross-check: Phase 19 Step 7 also gives dim = 8 + 3 + 1 = 12 for the SM group from the Pati-Salam chain. **MATCH.**

### Check 3: Codimension check in F_4

Phase 20 Step 3: codim = dim(F_4) - dim([SU(3)xSU(3)]/Z_3) = 52 - 16 = 36.

Note that 36 = dim(Spin(9)), which is consistent with the orbit F_4/Spin(9) being 16-dimensional (= dim(OP^2)), and the codimension of the u-preserving subgroup being equal to dim(Spin(9)). This is not numerically coincidental but reflects the complementary breaking patterns. **CONSISTENT.**

### Check 4: W = span{e_1,...,e_6} identity across routes

Phase 19 Step 1: "W = span_R{e_1, e_2, e_3, e_4, e_5, e_6}" with u = e_7.
Phase 20 Step 5: Route A "Im(O) = span{u} + W", Route B "same Im(O) = span{u} + W", both with W = span{e_1,...,e_6}.

The 6-dimensional subspace is defined identically: e_7^perp intersect Im(O). Since Im(O) = span{e_1,...,e_7} and u = e_7, W = span{e_1,...,e_6} in both routes. **MATCH.**

### Check 5: Stabilizer dimensions through the breaking chain

Phase 19 Step 5: Spin(10) has dim 45 = C(10,2). Stabilizer of omega_6 has dim 15 (internal-internal) + 6 (external-external) = 21. Complement = 24 (mixed). 21 + 24 = 45. **CORRECT.**

Phase 20 Step 4: Spin(9) cap [SU(3)xSU(3)]/Z_3 = SU(3)_C x U(2). dim(U(2)) = 4 = 3 + 1 (SU(2) x U(1)/Z_2). Total: 8 + 4 = 12. But this should give SU(3) x SU(2) x U(1) with dim 12 = 8 + 3 + 1, consistent.

The intermediate U(2) = SU(2) x U(1)/Z_2 has dim 4 (Lie algebra level), which decomposes as SU(2) (dim 3) + U(1) (dim 1). **CORRECT.**

---

## 4. Approximation Validity

Phase 20 is entirely algebraic/group-theoretic. No approximations, no perturbative expansions, no truncations. All results are exact. No validity range issues.

---

## 5. Cross-Phase Consistency of Key Identifications

### SU(3)_C identification

- Phase 18: Not explicitly named SU(3)_C, but the G_2 = Aut(O) and its subgroup structure are part of the mathematical setup.
- Phase 19 Step 1: SU(3)_C = Stab_{G_2}(u) (dim 8), preserves J: W -> W.
- Phase 19 Step 7: SU(3)_C from SU(4) -> SU(3) x U(1) breaking.
- Phase 20 Step 2: SU(3)_C := Stab_{G_2}(u) = Stab_{G_2}(e_7), dim 8.
- Phase 20 Step 7: Identification across routes -- both are "the group of transformations of W ~ C^3 that preserve J."

**Consistent across all phases.** The SU(3)_C is always identified as the stabilizer of u in G_2, acting on W ~ C^3 via the fundamental representation.

### Pati-Salam group identification

- Phase 19 Step 5: Stab_{Spin(10)}(omega_6) = [SU(4) x SU(2)_L x SU(2)_R]/Z_2, dim 21 = 15 + 6.
- Phase 20 Step 5 Route B: Same identification.
- Phase 20 Step 8: SU(2) from "external Spin(4) directions" in both routes.

**Consistent.** The Spin(4) ~ SU(2)_L x SU(2)_R from external generators (7-10) is the same in Phase 19 and Phase 20.

### omega_6 eigenspace convention

- Phase 19 Step 3-4: P = (1/2)(1 - i*omega_6) selects omega_6 = -i eigenspace (16-dim, "particle" per Todorov).
- Phase 19 SUMMARY: "P selects omega_6 = +i eigenspace = odd N" (from Plan 02).
- STATE.md: "P selects omega_6 = +i eigenspace = odd N (N=1 quarks + N=3 leptons)"

**Minor notation point:** Phase 19 Step 4 says "P selects the eigenspace with eigenvalue -i (called the 'particle' eigenspace)." The STATE.md entry says "+i eigenspace." Let me verify: P = (1/2)(1 - i*omega_6). If omega_6 v = lambda v, then P v = (1/2)(1 - i*lambda) v. For P v = v (selected), need i*lambda = -1, so lambda = +i. For P v = 0 (rejected), need i*lambda = 1, so lambda = -i.

Wait -- re-reading Phase 19 Step 4 carefully: "The projector P = (1/2)(1 - i*omega_6) selects the eigenspace with eigenvalue -i."

Let me check: If omega_6 v = -i v, then P v = (1/2)(1 - i*(-i)) v = (1/2)(1 - (-1))v = (1/2)(2)v = v. So P selects the omega_6 = -i eigenspace. But the STATE.md decision says "+i eigenspace."

This needs investigation. Reading the Phase 19 Plan 02 SUMMARY decision: "P selects omega_6 = +i eigenspace = odd N (N=1 quarks + N=3 leptons)."

The resolution: In the Furey Witt basis, omega_6 = -i*(-1)^N (Phase 19 Step 8 result). For odd N: omega_6 = -i*(-1) = +i. For even N: omega_6 = -i*(+1) = -i. So P = (1/2)(1 - i*omega_6) selects states where i*omega_6 = -1, i.e., omega_6 = +i (odd N) gives i*omega_6 = i*(+i) = -1, so P v = (1/2)(1-(-1))v = v. This means P selects the omega_6 = +i eigenspace, which is the odd-N sector.

But Phase 19 Step 4 says "eigenvalue -i." This appears to be an error in Step 4's phrasing. The correct statement is:

- P = (1/2)(1 - i*omega_6) selects omega_6 = +i eigenspace (since i*(+i) = -1, giving P = 1).

Phase 19 Step 4 says "selects the eigenspace with eigenvalue -i" but the algebra shows it selects +i. However, Phase 19 Plan 02 and STATE.md correctly record "+i eigenspace." The Phase 20 derivation does not re-derive this eigenvalue -- it references the chirality as "LEFT embedding" without specifying the omega_6 eigenvalue. So the Phase 19 Step 4 statement is an internal Phase 19 issue (within-phase), not a cross-phase inconsistency.

**Cross-phase status:** Phase 20 does not directly consume the omega_6 eigenvalue sign. It references "chirality" and "LEFT embedding" which are the physically meaningful outputs. The eigenvalue sign discrepancy in Phase 19 Step 4 is a within-phase issue for the verifier, not a cross-phase consistency problem for Phase 20.

---

## 6. STATE.md Consistency

Key Phase 20 results recorded in STATE.md:

| STATE.md Entry | Phase 20 Derivation | Match? |
|---|---|---|
| F_4 breaking by u: [SU(3)_C x SU(3)_J]/Z_3 (dim 16) | Step 3 | YES |
| SM from F_4 intersection: dim 12 | Step 4 | YES |
| Single-input theorem: same u, same W | Step 6 | YES |
| Chiral upgrade: F_4 = no chirality, Cl(6) = LEFT | Steps 10-11 | YES |
| Factor matching: SU(3)_C, SU(2), U(1) | Steps 7-9 | YES |
| 9-link chain L1-L9 | Step 13 | YES |
| Synthesis theorem conditional on A, B1, B2 | Step 17 | YES |
| Gap register: B1, B2, A, Gen, SA | Step 19 | YES |
| v5.0 milestone statement | Step 20 | YES |

**All STATE.md entries consistent with Phase 20 derivation.**

---

## Summary

### Checks Performed: 6 categories

1. Convention assertion alignment (Phases 18-19-20): **PASS**
2. Provides/requires chain (14 cross-phase transfers): **PASS**
3. Sign and factor spot-checks (5 checks): **PASS**
4. Approximation validity: **N/A** (all exact)
5. Cross-phase identification consistency (SU(3)_C, Pati-Salam, omega_6): **PASS** (with one within-phase note)
6. STATE.md consistency (9 entries): **PASS**

### Issues Found: 1 (minor, within-phase)

1. **Phase 19 Step 4 eigenvalue phrasing** (MINOR, within-phase): Step 4 says "P selects omega_6 = -i eigenspace" but the algebra gives omega_6 = +i (confirmed by Phase 19 Plan 02 and STATE.md). This is a within-phase phrasing issue in the derivation file, not a cross-phase inconsistency. Phase 20 does not consume this eigenvalue directly.

### Issues Found Affecting Phase 20: 0

### Convention Ledger Note

The project CONVENTIONS.md has not been updated to include v5.0 conventions (Clifford algebra, octonion basis, complex structure, Pati-Salam). The per-derivation ASSERT_CONVENTION headers serve as the effective convention record. This is an infrastructure hygiene item, not a consistency failure.

---

_Consistency check completed: 2026-03-24_
_Phase: 20-synthesis-one-choice-two-consequences_
_Mode: rapid_
