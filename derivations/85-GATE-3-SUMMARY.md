# 85 — GATE 3 SUMMARY: C2 (field equation, λ₁) + C3 (frequency fingerprint)

**v25.0 Phase 85. Exact over Q / Q(t). VERDICT = C2 PASS (λ₁ = 48 OP² / 12 CP² cut),
C3 PASS.** Independently confirmed by `code/variety_moment_doublet_verify.py` (different
frame + λ from the `E_22` component) and the gpd-verifier (`85-GATE-3-VERIFICATION.md`).

## C2 — the forced canonical field equation

Every moment field `φ_Y(p) = ⟨Y,p⟩` obeys the canonical Helmholtz equation
`Δ(φ_Y − φ̄_Y) = −λ₁(φ_Y − φ̄_Y)`, mean `φ̄_Y = ⟨Y, I/3⟩` (the F₄-average of `p`,
exact — no integration). Sharpest form (all `Y` at once, at `E_11`): the
mean-curvature vector `ΔP := Σ_i ¼ p_i''(0)` satisfies the single h_3(O)-vector identity

> **`ΔP = −λ₁ (E_11 − I/3)`** — verified in **all 27 components**, both frames:

```
   OP² (16-frame):  ΔP = diag(−32, 16, 16) = −48 (E_11 − I/3)   ⇒  λ₁ = 48
   CP² cut (4-frame): ΔP = diag(−8,  4,  4) = −12 (E_11 − I/3)   ⇒  λ₁ = 12
```

- **λ₁ pre-registered values CONFIRMED.** `λ₁(CP²) = 12 = 4(n+1)|_{n=2}` matches the
  Fubini–Study spectrum `λ_j = 4j(j+n)` (Ikeda–Taniguchi 1978) — a free external
  cross-check. `λ₁(OP²) = 48` (Cayley plane `F_4/Spin(9)`, normalization in which the
  totally geodesic CP² cut gives 12). **Ratio `λ₁(OP²)/λ₁(CP²) = 4 = 16/4 = dim ratio.**
- **λ₁ is non-hardwired:** extracted as `−Δc11/(c11(E_11)−c̄) = −Δc11/(2/3)` from one
  component, then the **full-vector** identity `ΔP = −λ₁(E_11−I/3)` is an independent
  check (the independent path extracts λ from the `E_22` component instead and agrees).
- **Means + field equations (symbolic X):** `m̄ = (2/3)Tr X`, `q̄ = σ₂(X)/3 = Tr(X#)/3`.
  Final form (also checked directly for symbolic X in the independent path):
  > **`Δm = −λ₁(m − (2/3)Tr X)`, `Δq = −λ₁(q − σ₂(X)/3)`, λ₁ = 48 (OP²) / 12 (cut).**
  The state's second char-poly coefficient `σ₂(X)` is the `q`-field background level.
- **Symbolic-Y identity at `E_11`:** `⟨Y, ΔP⟩ == −48⟨Y, E_11 − I/3⟩` for all 27 Y-params.

**Frame-independence** (Gate-0.4 closure): `ΔP_cut` from the standard cut frame equals
`ΔP_cut` from a Pythagorean-rotated cut frame (`3/5,4/5` in the driver; `5/13,12/13`
in the independent path) — two genuinely different orthonormal frames; and the
entry-swap `Spin(9)` automorphism leaves `ΔP_full` invariant.

## C3 — the geodesic-frequency fingerprint

Every moment along every canonical geodesic is `a + b·cos2θ + c·sin2θ` (frequency ≤ 2;
`t = tan(θ/2)`), i.e. `moment·(1+t²)²` is a degree-≤4 polynomial in `t`. Verified for
`m, q` (symbolic X) on all cut + off-u families. Hand anchor: `diag(7,5,3)` on `(1,0)`
gives `m = 9 − cos2θ`, `q = 18 − 3cos2θ` exactly. Hence `r = q/m²` is a ratio of
frequency-2 trigs over a squared one — a **rational** function (infinite harmonic
content): trap-guard #5, no field equation for `r`. Discriminating control: `c11² =
cos⁴θ` (freq 4) fails the ≤2 test.

## Anti-overclaim

`λ₁` is a property of the FROZEN canonical (Borel) geometry, **not** a derived coupling;
no Newton constant here. Trap-guard #6: only the first-order single-eigenvalue
statement is a law (no polynomial-in-Δ annihilator). Signature stays OPEN. This is the
entropy side's forced operator, not a balance.

**Gate 3: C2 PASS (λ₁ = 48 / 12), C3 PASS.**
