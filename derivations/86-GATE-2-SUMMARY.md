# 86 — GATE 2 SUMMARY: B1 (MaxEnt derived) + B2 (the response field)

**v26.0 Phase 86. Exact over Q[ε]/Q(t). VERDICT = B1 PASS, B2 PASS.** Independently
confirmed (`code/variety_sourced_field_equation_verify.py`, 10/10) and the gpd-verifier
(`86-GATE-2-VERIFICATION.md`).

## B1 — MaxEnt derived

`X = I/3 + εM` (traceless `M`). `I × M = −M/2` ⇒ `X# = I/9 − (ε/3)M + ε²M#`, so
`m = 2/3 − ε⟨M,p⟩`, `q = 1/9 − (ε/3)⟨M,p⟩ + ε²⟨M#,p⟩`. At first order **δq = δm/3** (ONE
field, `⟨M,p⟩`), hence
> **δr = (9/4)δq − (3/4)δm = 0 identically** — the purity/entropy landscape is flat at
> first order at EVERY event `p`.

Verified for symbolic `M` at `E_11` AND along all 16 families over `Q(t)`. This is the
vacuum **MaxEnt property DERIVED on the variety** — the honest restatement of v23's kill
and v24's flattening: the first-order balance the fiber couldn't host is structurally
empty; the content is second order.

## B2 — the response field

> **δ²r = (9/4)·G_M·ε²,  G_M(p) := ⟨M#,p⟩ − ¼⟨M,p⟩².**

Entropy: `S = f(r)` is analytic at the degenerate `r = 1/4` (the `±√(1−4r)` branches
cancel: `S = log2 − ½u + O(u²)`, `u = 1−4r`), `f'(1/4) = 2`, so (since `δr = 0`)
**δ²S = (9/2)·G_M·ε²**. Relative entropy: `S(ρ_face ‖ ρ_vac) = log2 − S(ρ_face)` exactly
(2-face vacuum maximally mixed) — the response field is minus the 2nd-order relative-
entropy density.

**Positivity `G_M ≤ 0`** (must hold): structurally `G_M = det₂(C_pM) − ¼(Tr C_pM)² =
−¼(face eigengap of C_pM)² ≤ 0`, equality iff `C_pM ∝ I₂`. Verified structurally + on an
exact `(M,p)` battery; anchors `G(E_11)=0`, `G(E_22)=−9/4` for `M=diag(2,−1,−1)`.

**Gate 2: B1 PASS, B2 PASS.**
