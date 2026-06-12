# Phase 91 (v31.0-candidate) — GATE 1 SUMMARY: Controls (zero evidential weight)

**Driver:** `python3 -u code/tensor_probe.py g1` → **5/5 PASS** (~7s, exact over Q).

All of V2 (the controls with known answers). Zero evidential weight — these calibrate the
machinery and the verdict() rule BEFORE any verdict computation.

| # | Control | Result |
|---|---|---|
| 1.self | `verdict()` is NON-HARDWIRED: all-zero → DEAD; one-nonzero → LIVE (reads only the residues) | PASS |
| 1.iii | VACUUM M=0: φ_M = G_M = R_M = χ = 0 and B3 = dφ⊗dφ ≡ 0 (every member vanishes) | PASS |
| 1.i | **B1 (Matsushima wall):** cov_hessian(φ_Y) == δ*(dφ_Y) block-for-block — PURE GAUGE; certificate (ω,f) = (dφ_Y, ¼Δφ_Y) | PASS |
| 1.ii | Killing/kernel control: δ*(0) = 0 (parallel/Killing directions in ker δ*; su(3) isometry potentials → Killing J grad φ_Y) | PASS |
| 1.v | L²-orthogonality: the trace-free longitudinal tensor (δ*(dφ) − conformal trace) is g-traceless ⇒ ⊥ the conformal block f·g | PASS |

**Trap #14 honored at the gate level:** B1's gauge certificate is exhibited and re-verified by
the same δ* machinery BEFORE any B2–B6 computation. The known-gauge case succeeds first.

**verdict() self-test (V3 well-posedness):** the fork rule is a deterministic function of the
per-member TT-residues only — `LIVE ⟺ ∃ member with ‖h_TT‖² ≠ 0`. Not a baked constant; the
self-test confirms both branches fire correctly on synthetic residues.

**Frozen battery (Gate 0 freeze, recorded here):** {B1, B2, B3, B4, B5, B6}. R_M cut solve
(α, β, λ₂) = (2/5, 3/20, 32) [verified this run via `vSFE._level_split_solve`]; χ the v30 clock
potential −(9/2)⟨M,p⟩⟨M,D_p⟩; B6 the π_{1/2}M tangent stress (pinned at Gate 3). No member beyond
B1–B6 — the enumeration of degree-≤2 symmetric rank-2 tangent forms from the certified scalars
{φ_Y, G_M, R_M, χ} and the only certified tangent vector s_M = dφ_M is exhausted by B1–B6.
