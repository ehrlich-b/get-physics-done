# GPD Patch: O(9)/S^8 Quantitative Verification

## Context

v10.0 assembled a 12-link derivation chain from self-modeling on h_3(O) to Einstein's equations. Adversarial review found that links (i)-(l) carry forward Heisenberg S=1/2 numbers (c_s = 1.659 Ja, rho_s = 0.181 J, v_LR/c_s = 7.63, SRF = 0.9993) from v9.0 Phases 32-35. The v10.0 model is O(9)/S^8 with rho_s = J/8 = 0.125 J. The structural arguments carry over by universality class reasoning, but the specific numbers need recomputation.

This is a single-phase patch, not a full milestone. Quantum SSB conditionality is documented honestly and stays as-is (open problem in rigorous stat mech, not a framework gap).

## Goal

One phase: recompute all model-specific numbers for O(9)/S^8 and update links (i)-(l) in the derivation chain. Remove all Heisenberg-specific numbers.

## Target Results

- Spin-wave velocity c_s for O(9)/S^8 sigma model on Z^3 (analytical: c_s = sqrt(rho_s / chi_perp) with rho_s = J/8 and chi_perp for 8 Type-A Goldstones)
- Lieb-Robinson velocity v_LR for H_eff on Z^3 (Hastings-Koma bound with ||H_ij|| from 2-site spectrum)
- v_LR / c_s ratio
- Fisher metric statement for O(9): CORR-03 applied with 8 Goldstone modes, algebraic decay C(r) ~ r^{-(d-2)} from massless propagator
- Lattice-BW entanglement Hamiltonian: H_ent = (2pi/c_s) sum x_perp h_x with O(9)-specific c_s and h_x = J sum_a T_a T_a
- SRF argument for O(9) (lattice-BW is structurally model-independent modulo c_s; state this explicitly with the O(9) c_s value)
- Emergent metric: ds^2 = -c_s^2 dt^2 + g_ij dx^i dx^j with O(9)-specific c_s
- Updated links (i)-(l) in a patch document (not a full chain reassembly)

## Acceptance

- All Heisenberg-specific numbers (c_s = 1.659, rho_s = 0.181, v_LR/c_s = 7.63) replaced with O(9)/S^8 values
- Carry-forward caveat in 40-derivation-chain.md can be marked RESOLVED
- No new conditionalities introduced

## Key Files

- v10.0 chain: derivations/40-derivation-chain.md (carry-forward caveat at links (i)-(l))
- Sigma model: derivations/39-sigma-model.md (rho_s = J/8, g^2 = 8T/J)
- Goldstone modes: derivations/39-goldstone-modes.md (8 Type-A, rho_ab = 0)
- 2-site spectrum: derivations/38-lattice-and-symmetry.md (E/J = {-7/4, -3/4, 1/4, 5/4, 9/4})
- Fisher geometry (Heisenberg, for structure reference): derivations/32-fisher-geometry-theorems.md
- Emergent Lorentz (Heisenberg, for structure reference): derivations/34-emergent-lorentz-invariance.md
- BW/KMS (Heisenberg, for structure reference): derivations/35-bw-axioms-and-lattice-bw.md

## Constraints

- No QMC data exists for O(9). Analytical spin-wave approximation only.
- Convention lock: Cl(9,0), {T_a,T_b} = (1/2) delta I_16, J > 0.

## False Progress to Reject

- Using Heisenberg numbers and relabeling them as O(9) results
- Claiming lattice-BW SRF "must be" similar without stating the structural argument
- Computing c_s for O(3) and calling it O(9)
