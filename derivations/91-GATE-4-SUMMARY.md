# Phase 91 (v31.0-candidate) — GATE 4 SUMMARY: V3 (the fork) + V4 (the fenced reading)

**Driver:** `python3 -u code/tensor_probe.py g4` → **1/1 PASS** (~20s).

## V3 — THE FORK (assembled, exact)

The non-hardwired `verdict()` reads the per-member TT-residues:

| member | object | TT-residue | source |
|---|---|---|---|
| B2 | ∇∇G_M | 0 (gauge) | Gate 2 (Hessian) |
| B4 | ∇∇χ | 0 (gauge) | Gate 2 (Hessian) |
| B5 | ∇∇R_M | 0 (gauge) | Gate 2 (Hessian) |
| **B3** | dφ_M⊗dφ_M | **≠ 0 (TT present)** | Gate 3 (york_solve inconsistent) |
| **B6** | π_{1/2}M tangent stress = dφ_M⊗dφ_M | **≠ 0 (= B3)** | Gate 3 (pin: tr = v27 \|π_{1/2}M\|²) |

```
verdict({B2:0, B4:0, B5:0, B3:1, B6:1})  ->  ('LIVE', ['B3', 'B6'])
```

**VERDICT = LIVE.** Deciding member(s): **B3 (= B6)**. The TT-part lives in the J-invariant
(1,1)-Hermitian isotypic sector = the Boucetta **λ=12 dim-8** target (the λ₁-threshold where the
v25 moment fields sit). Dimension audit: TT-residue dim = 1 per su(3)-generator direction,
≤ the dim-8 multiplicity (no under-spanning).

## V4 — THE READING (FENCED — binding)

**The variety route's certified matter data DOES source a genuine transverse-traceless metric
mode** — the first matter-forced TENSOR structure in the program. The two-scalar (Nordström-class)
gravity ceiling of v27–v30 is broken: matter (via the spinor moment s_M = dφ_M, equivalently the
v25 moment field's gradient bilinear) forces a rank-2, non-scalar, non-gauge mode on the compact
cut CP² = h₃(C_u).

**FENCE (binding, verbatim from the prompt):**

- **LIVE = "a matter-sourced tensor MODE exists"** — the prerequisite for Einstein-FORM —
  **NOT "Einstein gravity derived".**
- **Block C is NOT claimed**: the selection law (WHY the Einstein equation, the value of the
  coupling κ) is untouched. No Einstein-equation, no Newton constant, no G = κT, no dark matter,
  no geodesic-motion language.
- The frozen Fubini–Study geometry is **USED, not derived** (the same fence as v24–v30).
- The v18/v20 MM-connection corpse stays buried: this is the **BASE's deformation complex**
  (symmetric 2-tensors on the cut CP²), not a fiber-built spacetime connection.
- The 16-vs-6 rank wall (v18 Ph77 / v21 Gate 2) was a statement about whether the FULL nonlinear
  G[g] = κT + Λg holds with a single global (κ,Λ); LIVE here is the strictly weaker, upstream
  statement that a TT mode EXISTS. The two are not in tension — the wall lives in Block C.

## One sentence (which world)

> On the compact Kähler–Einstein cut, the certified matter bilinear B3 = dφ_M⊗dφ_M (= the pinned
> π_{1/2}M tangent stress B6) carries a nonzero transverse-traceless residue in the λ=12 (1,1)
> Hermitian sector — **matter sources a genuine metric tensor mode (LIVE)**; the Einstein
> selection law (Block C) remains open and is not claimed.
