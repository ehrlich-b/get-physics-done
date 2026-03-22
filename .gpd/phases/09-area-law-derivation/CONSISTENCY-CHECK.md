# Consistency Check: Phase 09 (Area-Law Derivation)

**Mode:** Rapid
**Date:** 2026-03-22
**Checker:** gpd-consistency-checker
**Scope:** Phase 09 (Plans 01-03) vs. full convention lock and Phase 08 results

---

## 1. Convention Compliance Matrix

Phase 09 derivation files all carry `ASSERT_CONVENTION` headers. Checked each against the convention lock in STATE.md.

| Convention (STATE.md) | Relevant to Phase 9? | Phase 9 Usage | Compliant? | Evidence |
|---|---|---|---|---|
| State normalization: Tr(rho) = 1 | Yes | All files use Tr(rho) = 1 | Yes | WVCH: Z = Tr(e^{-beta H}); channel capacity: rho_A = Tr_B(psi)(psi) |
| Coupling: H = sum h_xy (no 1/2) | Yes | All files | Yes | 09-wvch Eq.(09.3), 09-channel Part A, 09-synthesis Eq.(09-03.7a) |
| Commutation: [A,B] = AB - BA | Yes | Used in LR context | Yes | Standard commutator in Hastings/LR references |
| Entropy base: nats (ln) | Yes | All files | Yes | S = -Tr(rho ln rho) consistently; no log_2 anywhere |
| Sequential product: a & b | Marginally | Referenced in synthesis | Yes | Notation matches Phase 08 |
| Jordan product: a * b = (1/2)(a & b + b & a) | No | Not used in Phase 9 | N/A | Algebraic structure not needed |
| Composite product: product-form | Marginally | Referenced | Yes | (a tensor b) & (c tensor d) = (a & c) tensor (b & d) |
| Metric signature: N/A | Noted in ASSERT headers | See Issue #1 below | WARNING | Headers say mostly_minus; STATE.md says N/A |
| All other locked conventions | No | Not applicable | N/A | Phase 9 is lattice quantum info, not QFT |

### Issue #1 (Minor): ASSERT_CONVENTION header vs. STATE.md for metric_signature

All four Phase 9 derivation files include `metric_signature=mostly_minus` in their ASSERT_CONVENTION headers. However, STATE.md convention lock states `Metric signature: N/A (algebraic/categorical project)`.

**Assessment:** No actual metric signature is used anywhere in Phase 9 calculations. No Lorentzian inner products, no spacetime indices, no p^2 contractions. The ASSERT header is vestigial/aspirational (anticipating Phase 10 Jacobson bridge, where a metric will become relevant). No equations are affected.

**Severity:** Cosmetic. No physics impact.

---

## 2. Hamiltonian Convention: H = sum h_xy (no 1/2)

This is the most important convention for cross-phase consistency. In many textbooks, the Heisenberg Hamiltonian is written as H = (1/2) sum J sigma.sigma (with the 1/2 compensating double-counting of edges). This project uses H = sum_{<x,y>} h_xy with h_xy = JF, summing over ordered or unordered edges once, with NO factor of 1/2.

**Phase 8 (producer):**
- derivations/08-lattice-definition.md, Definition 6: H_Lambda = sum_{edges in Lambda} h_xy. No 1/2.
- derivations/08-hamiltonian-construction.md: h_xy = JF. For n=2: h_xy^int = (J/2)(sigma.sigma). The 1/2 here is from F = (1/2)(1 + sigma.sigma), NOT from edge double-counting.

**Phase 9 (consumer):**
- 09-wvch: H = sum h_xy with h_xy = JF. Consistent with Phase 8.
- 09-channel-capacity: H = sum h_xy. Consistent.
- 09-heisenberg-entanglement: FM/AFM analysis uses h_xy = JF with eigenvalues +J (symmetric) and -J (antisymmetric). This is correct for the SWAP operator F (not for the Heisenberg sigma.sigma, which would have different eigenvalue structure without the identity piece).
- 09-synthesis: Inherits from Plans 01-02. Consistent.

**Test value:** For n=2, two sites, one edge: H = JF. Eigenvalues of F are +1 (triplet, dim 3) and -1 (singlet, dim 1). So H has eigenvalues +J and -J. For J > 0 (AFM): ground state energy = -J (singlet), excitation energy = +J (triplet). Gap = 2J. This matches the standard Heisenberg result where H_Heis = (J/2)(sigma.sigma) + (J/2)1 has eigenvalues J (triplet) and -J (singlet). PASS.

**Verdict:** CONSISTENT across all Phase 8-9 files. No double-counting issue.

---

## 3. Entropy Convention: Nats vs. Bits

All Phase 9 files use von Neumann entropy S = -Tr(rho ln rho) in nats. No log_2 appears anywhere.

**Test value check:** 09-channel-capacity states I_max per bond = 2*log(n) nats, and for n=2 gives 2*ln(2) = 1.386 nats. This is correct: superdense coding gives 2 classical bits = 2*ln(2) nats. PASS.

**09-heisenberg-entanglement:** AFM S(L) = (1/3)*ln(L). The Calabrese-Cardy formula uses natural logarithm. PASS.

**Verdict:** CONSISTENT. All entropy quantities in nats throughout.

---

## 4. Cross-Phase Provides/Consumes Verification

### 4a. h_xy = JF (Phase 8 -> Phase 9)

| Check | Result |
|---|---|
| Physical meaning match | Yes -- SWAP operator interaction on M_n(C) tensor M_n(C), derived from diagonal U(n) covariance |
| Notation match | Yes -- JF in both phases |
| Eigenvalue structure | Phase 8: F eigenvalues +1 (sym) and -1 (anti). Phase 9 uses same. PASS |
| Operator norm | Phase 8: ||h_xy|| = |J| (since ||F|| = 1). Phase 9: ||h_xy|| = |J| (Eq. 09.2). MATCH |

### 4b. ||h_xy|| = |J| (Phase 8 -> Phase 9 WVCH)

Phase 8 (08-hamiltonian-construction.md): ||h_xy|| = |J| * ||F|| = |J| * 1 = |J|.
Phase 9 (09-wvch, Eq. 09.2): ||h_xy|| = |J|.
**MATCH.**

### 4c. v_LR = 8eJ/(e-1) (Phase 8 -> Phase 9)

Phase 8 (08-lr-self-modeling.md): v_LR(1) = 8eJ/(e-1) ~ 12.66J on Z^1.
Phase 9 (09-synthesis, line 303): v_LR = 8eJ/(e-1).
Phase 9 (09-03-SUMMARY.md, Key Quantities table): v_LR = 12.66J.

**Minor inconsistency:** The synthesis file uses both `8eJ/(e-1)` (line 303, Part F) and `8e|J|/(e-1)` (lines 233, 398). The LR velocity should use |J| since it is a speed bound that must be positive. Phase 8 computes it with J implicitly positive (the norm ||h_xy|| = |J| enters the NS formula). The correct expression is v_LR = 8e|J|/(e-1).

**Assessment:** Not a computational error -- v_LR is always used as a positive quantity in context. The omission of absolute value signs in Part F line 303 is a notational imprecision, not a sign error. No downstream result is affected because v_LR only enters through the statement that information propagates at bounded speed.

**Severity:** Cosmetic notational inconsistency. No physics impact.

### 4d. Lattice definition G = (V, E) (Phase 8 -> Phase 9)

Phase 8 (08-lattice-definition.md): G = (V, E), sites carry A_x = M_n(C), edges carry h_xy = JF.
Phase 9: All files reference this structure consistently.
Boundary definition: partial(A) = {edges crossing the cut}. Same in both phases.
**MATCH.**

### 4e. Locality mapping / Theorem 1 (Phase 8 -> Phase 9)

Phase 8: Theorem 1 proves self-modeling locality implies Hamiltonian locality.
Phase 9 (09-wvch, H4): "By the locality mapping (Theorem 1 of Phase 8)."
Phase 9 (09-channel-capacity, Part A): "Theorem 1 (Phase 8, derivations/08-lattice-definition.md)."
**Correctly cited and used.**

---

## 5. Sign Convention Consistency

The sign of J is a physical ambiguity identified in Phase 8 and carried through Phase 9. All Phase 9 results correctly handle both signs:

| Result | J dependence | Sign-safe? |
|---|---|---|
| WVCH bound I <= 2*beta*|boundary|*|J| | |J| | Yes |
| Channel capacity S <= log(n)*|boundary| | J-independent | Yes |
| ||h_xy|| = |J| | |J| | Yes |
| FM ground state analysis | J < 0 specific | Yes (explicitly conditional) |
| AFM ground state analysis | J > 0 specific | Yes (explicitly conditional) |
| delta S ~ |boundary| | |J| through v_LR | Yes |

**No sign errors found.** All expressions that should use |J| do so. The FM/AFM analyses correctly condition on the sign.

---

## 6. Spot-Check: Load-Bearing Equations

### 6a. WVCH bound (Eq. 09.3)

The WVCH theorem (Wolf et al. 2008) states:
I(A:B) <= 2*beta * sum_{X straddling cut} ||Phi(X)||

For self-modeling H with nearest-neighbor h_xy = JF:
- Only edges in boundary(A) straddle the cut
- Each contributes ||h_xy|| = |J|
- Sum = |boundary(A)| * |J|

Result: I(A:B) <= 2*beta*|boundary(A)|*|J|. **Correct application of the theorem.**

**Dimensional test:** [2*beta*|boundary|*|J|] = [energy^{-1}]*[count]*[energy] = [dimensionless]. Matches [I(A:B)] = [dimensionless]. PASS.

**Limiting case test:**
- beta -> 0 (T -> infinity): bound -> 0. Physical: maximally mixed state has I = 0. PASS.
- J -> 0: bound -> 0. Physical: decoupled sites have I = 0. PASS.
- |boundary| = 0: bound -> 0. Physical: disconnected regions. PASS.

### 6b. Channel capacity bound (Eq. 09-02.1)

Chain: I_max per bond = 2*log(n) (Holevo + superdense coding) -> I(A:B) <= 2*log(n)*|boundary| (DPI, sum over bonds) -> for pure state I = 2*S(A) -> S(A) <= log(n)*|boundary|.

**Test value (n=2, single bond):** S(A) <= ln(2) ~ 0.693 nats. Maximum entanglement of a Bell pair: S = ln(2). Bound is TIGHT for this case. PASS.

**Test value (n=1):** S(A) <= ln(1)*|boundary| = 0. Only trivial states exist. PASS.

### 6c. Entanglement first law (Eq. 09-03.3)

delta S(A) = delta <K_A>, K_A = -ln(rho_A).

Derivation check: S(rho + delta rho) = -Tr[(rho + delta rho)*ln(rho + delta rho)].
First order: delta S = -Tr[delta rho * ln rho] - Tr[delta rho] = -Tr[delta rho * ln rho] (since Tr(delta rho) = 0).
= Tr[delta rho * (-ln rho)] = Tr[delta rho * K_A] = delta <K_A>.

**Sign check:** K_A = -ln(rho_A). The minus sign in K and the minus sign in S = -Tr(rho ln rho) combine correctly: delta S = +Tr[delta rho_A * K_A]. PASS.

**Test value (thermal state):** rho_beta = e^{-beta H}/Z, so K_A -> beta*H_A (the modular Hamiltonian equals beta times the physical Hamiltonian for the Gibbs state of H_A). Then delta S = beta * delta <H_A>, which is the standard thermodynamic first law dS = dE/T. PASS.

---

## 7. CONVENTIONS.md Staleness

The project-level .gpd/CONVENTIONS.md was established during project initialization (2026-03-15) and reflects the v1.0/v2.0 milestone (information-theoretic / experiential measure conventions). It does NOT include the Phase 8-9 conventions:
- No entry for H = sum h_xy (no 1/2)
- No entry for the SWAP interaction h_xy = JF
- No entry for Tr(rho) = 1 in the QIS context
- The convention lock in STATE.md IS up to date

**Assessment:** The STATE.md convention lock is the authoritative source and is correct. CONVENTIONS.md has not been updated for the v3.0 milestone. This is a documentation gap, not a physics inconsistency.

**Severity:** Documentation debt. No physics impact. Should be updated at next milestone audit.

---

## 8. Approximation Validity Check

No approximation-validity ranges are registered in STATE.md ("Active Approximations: None yet."). Phase 9 introduces no approximations -- all results are either exact (WVCH bound, channel capacity bound, entanglement first law) or explicitly flagged as physical arguments (A3, modular Hamiltonian locality).

The Calabrese-Cardy formula S(L) = (1/3)*ln(L) applies in the regime L >> 1 (subsystem much smaller than total). This is correctly stated in 09-heisenberg-entanglement.md.

No approximation violations found.

---

## Summary

| Check Category | Items Checked | Issues Found | Severity |
|---|---|---|---|
| Convention compliance (STATE.md lock) | 10 conventions | 1 (metric_signature header) | Cosmetic |
| Hamiltonian convention H = sum h_xy | 6 files | 0 | -- |
| Entropy convention (nats) | 4 files | 0 | -- |
| Cross-phase provides/consumes | 5 quantities | 1 (v_LR |J| vs J notation) | Cosmetic |
| Sign convention consistency | 6 results | 0 | -- |
| Load-bearing equation spot-checks | 3 equations | 0 | -- |
| CONVENTIONS.md currency | 1 file | 1 (stale for v3.0) | Documentation debt |
| Approximation validity | 1 check | 0 | -- |

**Total issues: 3 (all cosmetic/documentation-level). No physics-impacting inconsistencies found.**

---

_Generated: 2026-03-22 by gpd-consistency-checker (rapid mode)_
