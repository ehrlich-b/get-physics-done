# Phase 91 (v31.0-candidate) — GATE 3 SUMMARY: The Bilinear Sector (B3, B6) — THE VERDICT CENTER

**Driver:** `python3 -u code/tensor_probe.py g3` → **7/7 PASS** (~540s, exact over Q).

This is the verdict center. B3 and B6 are NOT Hessians; whether they carry a transverse-traceless
(TT) residue against the complete gauge+conformal span decides the fork.

| # | Check | Result |
|---|---|---|
| 3.link | reduction δ*(φ dφ) == dφ⊗dφ + φ∇∇φ ⇒ TT(B3) = −TT(φ∇∇φ) | PASS |
| 3.ctrl | **TRAP #14:** york_solve(B1=∇∇φ) consistent=True + symbolic reconstruction δ*ω+f·g == B1 | PASS |
| 3.B3 | **VERDICT:** york_solve(B3) consistent=**False** ⇒ B3 HAS a TT residue | PASS |
| 3.B6 | **PIN:** tr_g(B3) == 2|π_{1/2}M|² (the v27 trace) ⇒ B6 = s_M⊗s_M = dφ_M⊗dφ_M COINCIDES with B3 | PASS |
| 3.type | (2,0)+(0,2) jointly gauge while full B3 inconsistent ⇒ TT in the J-invariant (1,1) sector = λ=12 dim-8 | PASS |
| 3.audit | **DIMENSION AUDIT (Trap #15):** dim(gauge+conf)=181, B1-control deficit=0, B3 deficit=1 (two primes), 1 ≤ dim-8 | PASS |
| 3.generic | **GUARD 4:** dense generic M — B1 consistent, B3 inconsistent (direction-independent verdict) | PASS |

## The verdict object and the york_solve engine

For each member h we ask: does there exist a SINGLE 1-form ω and conformal scalar f with
**h = δ*ω + f·g** (the gauge+conformal part of the Berger–Ebin/York split)? `york_solve` answers
exactly, over Q, by the **matched-monomial route**: build δ*ω + f·g over the complete certified
gauge+conformal span, bring h − δ*ω − f·g over a common ρ-power, and require every polynomial
coefficient (in z₁,z₂,z̄₁,z̄₂) to vanish — a linear system over Q. CONSISTENT ⇒ DEAD (h is
gauge+conformal, certificate exhibited and symbolically reconstructed). INCONSISTENT ⇒ h has a
TT residue (LIVE).

**The complete gauge+conformal span.** By LINEARITY of δ*, the gauge image is spanned by δ* of
the complete 1-form basis {φ_A dφ_B (holo-only), φ_A d̄φ_B (antiholo-only)} over the certified
potentials φ_A (A = the 8 traceless Hermitian su(3) generators + identity; φ_id = Tr(p) = 1, so
bare dφ_B AND the Killing/co-exact forms i(dφ − d̄φ) are BOTH in the span — holo and antiholo
coefficients INDEPENDENT). Conformal f = Σ d_AB φ_A φ_B (the complete degree-2 scalar span). The
B1 round-trip certifies this span is complete for the gauge image (it captures all Hessians).

## The result: B3 (= B6) carries a TT residue → LIVE

- **B1 control consistent + reconstructed exactly** (Trap #14): the same solver finds the known
  gauge tensor and rebuilds it symbolically. No solver asymmetry between control and verdict.
- **B3 = dφ_M⊗dφ_M INCONSISTENT**: no (ω,f) reproduces it. The obstruction is a genuine TT mode.
- **B6 coincides with B3.** Pin (stated, frozen): the canonical π_{1/2}M tangent stress whose
  trace is the v27 |π_{1/2}M|² is s_M⊗s_M with s_M = π_{1/2}^{(p)}M = dφ_M (v28). The trace check
  tr_g(dφ⊗dφ) = 2g^{ab̄}∂_aφ∂_b̄φ = 2|∇φ|² = 2|π_{1/2}M|² (verified, ratio exactly 2) certifies the
  pin. B6 IS B3 — reported transparently; same verdict object, same LIVE result.

## Isotypic type and the dimension audit (Trap #15, MANDATORY for LIVE)

- **Type:** the (2,0) and (0,2) blocks of B3 are INDIVIDUALLY pure gauge (δ* of holomorphic
  1-forms — verified jointly consistent). The full B3 is inconsistent only when the THREE blocks
  must share a SINGLE ω. So the residue is the **J-invariant (1,1)-Hermitian** sector — the
  Boucetta **λ=12 dim-8** TT target (RESEARCH §4). NOT the anti-invariant λ=32 (2,0)/(0,2) TT.
- **Audit:** exact rank deficit of B3 against the complete gauge+conformal image, via
  off-reality-slice modular point-sampling (two primes, cross-checked). dim(gauge+conf) = **181**;
  **B1-control deficit = 0** (a Hessian is gauge — the control fires correctly); **B3 deficit = 1**
  (two primes agree). The TT residue is 1-dimensional for a single su(3)-generator direction —
  ≤ the Boucetta multiplicity dim-8, NOT exceeding it ⇒ **no under-spanning** (the fake-LIVE
  failure mode is excluded).

## A diagnosed-and-rejected pitfall (recorded for the verifier)

An intermediate dimension audit using **reality-slice** sample points (z = z̄) FALSELY reported
B3 in-span (deficit 0). Reason: the reality slice is 2-real-dimensional and does NOT separate the
4 independent Wirtinger monomials z₁,z₂,z̄₁,z̄₂ — it ALIASES the coefficient structure. The fix is
**off-slice** points (z, z̄ independent generic rationals). The B1 control catches it: off-slice,
B1 correctly gives deficit 0; reality-slice gave spurious B1 deficits for some directions. All
reported audit numbers use off-slice points with the B1 control passing. The exact-Q rank (no
sampling) independently confirmed dim(gauge+conf)=118 (s01), deficit=1 — same conclusion.

## Generic-M robustness (Guard 4)

The verdict is direction-independent: on the sparse single-generator s01, on a dense generic M
(all 8 params nonzero, off the diagonal stratum), and on a second dense M, york_solve(B1) is
consistent and york_solve(B3) is inconsistent — LIVE in every case. Co-diagonalization strata and
the v24 diagonal reference carry zero weight (the matters used are off-diagonal/generic).
