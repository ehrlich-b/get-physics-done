# Consistency Check: Phase 35 (BW Theorem and Local Equilibrium)

**Mode:** rapid
**Phase:** 35-bw-theorem-and-local-equilibrium (Plans 01-02)
**Checked against:** Full conventions ledger + phases 33-34 + convention_lock in state.json
**Date:** 2026-03-30

---

## 1. Convention Compliance Matrix

### Convention Lock (state.json) vs Phase 35

| Convention | Lock Value | Relevant to Phase 35? | Phase 35 Usage | Compliant? | Notes |
|---|---|---|---|---|---|
| metric_signature | (+,+,...,+) Riemannian Fisher | YES (emergent Lorentzian) | (-,+,...,+) emergent Lorentzian | N/A -- different object | See Finding 2 |
| fourier_convention | N/A (lattice spin chain) | No | N/A | N/A | -- |
| natural_units | hbar=1, k_B=1, a=1 | YES | hbar=1, k_B=1, a=1 | YES | Consistent |
| gauge_choice | N/A | No | N/A | N/A | -- |
| regularization_scheme | N/A | No | N/A | N/A | -- |
| renormalization_scheme | N/A | No | N/A | N/A | -- |
| coordinate_system | N/A | Partially (Rindler coords) | Rindler + Minkowski | YES | Appropriate for BW |
| spin_basis | standard S^z eigenbasis | No (not used in Phase 35) | N/A | N/A | -- |
| state_normalization | density matrices trace 1 | YES (rho_A) | rho_A = e^{-K_A}/Z, Tr=1 | YES | Consistent |
| coupling_convention | J > 0 AFM | YES (h_x = J S_x . S_{x+1}) | J > 0 AFM | YES | Consistent |
| index_positioning | N/A | Partially (GR tensors) | Standard | YES | -- |
| time_ordering | N/A | No | N/A | N/A | -- |
| commutation_convention | N/A | No | N/A | N/A | -- |
| levi_civita_sign | N/A | No | N/A | N/A | -- |
| generator_normalization | N/A | No | N/A | N/A | -- |
| covariant_derivative_sign | N/A | No | N/A | N/A | -- |
| gamma_matrix_convention | N/A | No | N/A | N/A | -- |
| creation_annihilation_order | N/A | No | N/A | N/A | -- |

### Custom Conventions

| Convention | Lock Value | Phase 35 Usage | Compliant? |
|---|---|---|---|
| Jordan product | a o b = (1/2)(ab + ba) | Not used in Phase 35 | N/A |
| Peirce eigenvalues | {0, 1/2, 1} | Not used in Phase 35 | N/A |
| Clifford signature | Cl(9,0) | Not used in Phase 35 | N/A |

### Phase 35 Internal Conventions (ASSERT_CONVENTION)

Both derivation files assert consistent convention lines:
- `natural_units=natural (hbar=1 k_B=1 a=1)`
- `metric_signature=mostly_minus (-,+,...,+) for emergent Lorentzian spacetime`
- `modular_hamiltonian=K_A=-ln(rho_A)`
- `kms_temperature=beta=2pi for Rindler`
- `coupling_convention=J>0 AFM`

**Uniformity across Phase 35 files:** 2/2 files consistent -- PASS

---

## 2. Findings

### Finding 1 (WARNING): Equation number collision -- Eq. (35.3) used for two different quantities

**Severity:** Minor (notation collision, not physics error)

In `derivations/35-bw-axioms-and-lattice-bw.md` (Plan 01), Eq. (35.3) is:
$$K_A^{\text{exact}} = H_{\text{ent}}^{\text{BW}} + O(a^2/L^2)$$

In `derivations/35-kms-equilibrium-and-modular-hamiltonian.md` (Plan 02), Eq. (35.3) is:
$$T_U = a/(2\pi)$$

These are different equations sharing the same label. The 35-01-SUMMARY correctly lists Eq. (35.3) as the lattice-BW accuracy statement. The 35-02-SUMMARY lists "T_U = a/(2pi) (Eq. 35.3)" as the Unruh temperature. Both are internally consistent with their respective derivation files, but the shared label creates ambiguity for any downstream consumer (Phase 36) that references "Eq. (35.3)".

**Impact:** Low. Phase 36 consumers reference J1 (K_A = 2pi K_boost), J2 (theta=sigma=0), and J3 (T_U = a/(2pi)) by name rather than equation number, so the collision is unlikely to cause confusion. The SUMMARYs explicitly write out the equation content alongside the number.

**Suggested fix:** Renumber one instance. Since Plan 02 uses numbers 35.7-35.21, the Unruh temperature could be renumbered to Eq. (35.6) (currently unused), and the lattice accuracy could remain Eq. (35.3).

### Finding 2 (INFO): "mostly_minus" label for (-,+,+,+) -- known pre-existing issue

**Severity:** Informational -- known from Phase 12 CONSISTENCY-CHECK Finding 1

Phase 35 ASSERT_CONVENTION headers use `metric_signature=mostly_minus` to label the (-,+,+,+) signature. The standard convention in the HEP/GR community is that (-,+,+,+) is called "mostly plus" (three spatial plus signs) while (+,-,-,-) is called "mostly minus." This labeling error was first flagged in the Phase 12 consistency check and has propagated through Phases 33-35 without correction.

**Impact:** None on physics. The actual metric used (ds^2 = -c_s^2 dt^2 + dx^2) is unambiguous and correct. Both derivation files write out the explicit signature (-,+,...,+) in parentheses after the label, so no reader would be confused. The mislabel only matters for automated convention checkers.

**Suggested fix:** Same as Phase 12 recommendation: change `mostly_minus` to `mostly_plus` globally. This is cosmetic.

### Finding 3 (INFO): Convention lock in state.json is stale (v8.0 scope, not v9.0)

**Severity:** Informational -- not an error in Phase 35

The `state.json` position block still reads `current_phase: "31"` and `current_focus: "v8.0 Gap C Algebraic Closure via C*-Measurement Maps"`. The convention_lock describes the metric as "(+,+,...,+) Riemannian Fisher metric" which was correct for the v8.0 algebraic work but does not reflect the v9.0 continuum-limit physics (emergent Lorentzian spacetime). STATE.md has been updated to reflect Phase 35 but state.json has not been synced.

**Impact:** Low for Phase 35 itself (STATE.md is the primary human-readable state). Could cause confusion for any automation reading state.json.

**Suggested fix:** Sync state.json position and convention_lock to reflect v9.0 state.

---

## 3. Provides/Consumes Verification

### Phase 34 -> Phase 35 (Plan 01): Lorentz invariance and c_s

| Quantity | Producer (Phase 34) | Consumer (Phase 35, Plan 01) | Meaning Match | Units Match | Test Value | Status |
|---|---|---|---|---|---|---|
| Emergent metric | ds^2 = -c_s^2 dt^2 + dx^2 (Eq. 34.30) | Cited as Eq. (34.30), used for W2 assessment and lattice-BW | YES | YES (natural units) | -- | OK |
| Spin-wave velocity | c_s = 1.659 Ja (Phase 33 Eq. 33.14, Phase 34) | c_s = 1.659 Ja in Eq. (35.1) denominator | YES | YES | beta_eff(1) = 2pi/1.659 = 3.787/J (verified in Python) | OK |
| DLS reflection positivity | OS-RP established in Phase 34 Step 11 | Cited in Plan 01 Step 5 as input | YES | N/A (theorem) | -- | OK |

### Phase 35 Plan 01 -> Plan 02: BW identification

| Quantity | Producer (Plan 01) | Consumer (Plan 02) | Meaning Match | Units Match | Test Value | Status |
|---|---|---|---|---|---|---|
| K_A = 2pi K_boost (Eq. 35.0a) | BW theorem statement, Step 1 | Used in Steps 2, 4 to derive modular flow | YES | YES (both dimensionless) | 2pi factor traced through 6-step table in Plan 02 Step 5 | OK |
| Lattice-BW H_ent (Eq. 35.1) | Step 6 | Cited in Plan 02 Step 7 for lattice cross-check | YES | YES (dimensionless) | -- | OK |
| SRF = 0.9993 | Step 9 | Cited in Plan 02 Steps 7, 14 | YES | YES (dimensionless fraction) | -- | OK |
| W1-W6 assessment | Step 2 table | Cited in Plan 02 Step 1 as input | YES | N/A | -- | OK |

### Phase 35 -> Phase 36: Jacobson inputs J1-J3

| Quantity | Producer (Phase 35) | Consumer (Phase 36, expected) | Meaning Match | Units Match | Convention Match | Status |
|---|---|---|---|---|---|---|
| J1: K_A = 2pi K_boost | Plan 01 Eq. (35.0a) | Modular Hamiltonian for entanglement first law | YES | YES | YES | OK |
| J2: theta=sigma=0 | Plan 02 Eqs. (35.19, 35.21) | Local equilibrium at bifurcation surface | YES | YES | YES | OK |
| J3: T_U = a/(2pi) | Plan 02 Eq. (35.3) / Step 5 | Unruh temperature for thermal entropy | YES | YES | YES | OK |

---

## 4. Sign and Factor Spot-Checks

### Check 1: The 2pi factor chain (load-bearing, downstream-referenced)

The factor 2pi appears in K_A = 2pi K_boost and propagates to T_U = a/(2pi). Plan 02 Step 5 traces this end-to-end in a 6-row table:

1. K_A = 2pi K_boost (BW) -- 2pi introduced
2. sigma_t = boost by 2pi*t -- 2pi carried
3. beta_mod = 1 (Tomita-Takesaki) -- modular inverse temperature
4. t = a*tau/(2pi) -- modular-to-proper time
5. beta_phys = 2pi/a -- physical inverse temperature
6. T_U = a/(2pi) -- standard Unruh result

**Verification:** T_U = a/(2pi) is the textbook Unruh temperature (Unruh 1976, PRD 14, 870). For a=1: T_U = 1/(2pi) ~ 0.1592. This matches the standard result. No factor of 2pi doubled or dropped.

**Status:** PASS

### Check 2: Dimensional analysis of H_ent^BW (Eq. 35.1)

H_ent = (2pi/c_s) * sum x_perp * h_x

- [2pi] = dimensionless
- [c_s] = [J] (since a=1, c_s = 1.659 J*a = 1.659 J)
- [x_perp] = dimensionless (lattice site integer)
- [h_x] = [J] (h_x = J S_x . S_{x+1}, spin operators dimensionless)

[H_ent] = [1/J] * [1] * [J] = dimensionless

K_A = -ln(rho_A) is dimensionless (exponent of density matrix). CONSISTENT.

**Status:** PASS

### Check 3: Rindler observer normalization

Plan 02 Eq. (35.10): x^0 = (1/a)sinh(a*tau), x^1 = (1/a)cosh(a*tau)

u^mu = dx^mu/d(tau) = (cosh(a*tau), sinh(a*tau))

u^mu u_mu = g_mu_nu u^mu u^nu with g = diag(-c_s^2, 1, ...):
= -c_s^2 * cosh^2(a*tau) + sinh^2(a*tau)

Wait -- the derivation file states u^mu u_mu = -1 using (-,+,...,+) metric. But the emergent metric is ds^2 = -c_s^2 dt^2 + dx^2, so g_00 = -c_s^2, g_11 = 1. Then:

u^0 = d(x^0)/d(tau) = cosh(a*tau), u^1 = d(x^1)/d(tau) = sinh(a*tau)

u_mu u^mu = g_00 (u^0)^2 + g_11 (u^1)^2 = -c_s^2 cosh^2(a*tau) + sinh^2(a*tau)

For this to equal -1, we need c_s = 1 in the Rindler coordinates. The derivation file implicitly works in the continuum with c_s = 1 (or equivalently, uses rescaled coordinates where the metric is ds^2 = -dt^2 + dx^2). This is stated in the self-critique checkpoint at Step 5: "Using hbar=1, k_B=1, c_s=1 (natural units for the emergent spacetime)."

This is consistent: the Rindler analysis is performed in the continuum limit with c_s absorbed into the time coordinate (the rescaled coordinates tau' = c_s*tau from Phase 34 Eq. 34.16). The lattice-BW formula Eq. (35.1) retains the explicit c_s factor because it works in lattice coordinates where c_s != 1.

**Status:** PASS (with note: two coordinate systems coexist -- lattice coords where c_s appears explicitly, and continuum rescaled coords where c_s = 1. Both are used correctly.)

---

## 5. Approximation Validity

### Active approximations in Phase 35

| Approximation | Validity Condition | Current Parameter Values | Satisfied? |
|---|---|---|---|
| Lattice-BW ansatz | a/L << 1, Lorentz-invariant low-energy theory | L >> 1 (thermodynamic limit assumed) | YES (conditional) |
| Half-space bipartition | R/L_curv << 1 (flat spacetime) | Flat emergent spacetime assumed | YES |
| Neel-ordered ground state | d >= 2 for true LRO | d >= 2 stated throughout | YES |

No approximation validity ranges from prior phases are violated.

---

## 6. Summary

### Semantic Verification Summary

**Provides/Consumes pairs verified:** 10 total
- Meaning match: 10/10
- Units match: 10/10
- Test-value pass: 2/2 (those with numerical test values)
- Convention match: 10/10
- Failed transfers: 0

### Convention Compliance (All Phases)

**Active conventions checked:** 18 canonical + 3 custom
- Compliant: 4 relevant conventions all compliant
- Not applicable: 14 canonical + 3 custom (correct: Phase 35 is lattice QFT / emergent GR, not full QFT)
- Violations: 0

### Cross-Phase Error Patterns

| Error Pattern | Instances | Severity |
|---|---|---|
| Equation number collision (35.3) | 1 | Minor |
| "mostly_minus" mislabel (pre-existing) | 1 | Informational |
| state.json stale (pre-existing) | 1 | Informational |
| Sign absorbed into definition | 0 | -- |
| Normalization factor change | 0 | -- |
| Implicit assumption violated | 0 | -- |
| Coupling convention mismatch | 0 | -- |
| Factor of 2pi error | 0 | -- |

### Narrative Coherence

**Logical chain:** Phase 34 (Lorentz) -> Plan 01 (BW) -> Plan 02 (KMS + equilibrium) -> Phase 36 (Jacobson)
- No circularity detected
- Each step uses only previously established results
- The derivation chain is explicitly stated in Plan 02 Step 1

---

_Phase: 35-bw-theorem-and-local-equilibrium_
_Checked: 2026-03-30_
