# 85 — GATE 2 SUMMARY: C1 — the moment-doublet identity + completeness (THE CORE)

**v25.0 Phase 85 (decisive). Exact over Q / Q(t). VERDICT = C1 PASS.**
Independently confirmed by `code/variety_moment_doublet_verify.py` (eigenprojector
compression + gradient-of-N sharp + literal block det₂, separate code path) and by the
from-scratch gpd-verifier (`85-GATE-2-VERIFICATION.md`).

## The identity

> **`m(p;X) := Tr(C_p X) = Tr(X) − ⟨X,p⟩`** and **`q(p;X) := det₂(C_p X) = ⟨X#,p⟩`**

for all `X ∈ h_3(O)` and all rank-1 idempotents `p`; `⟨A,B⟩ = Tr(A∘B)`, `C_p` the v24
Peirce-0 compression, `X# = X×X` the Freudenthal adjoint.

**Consequence (the doublet reading):** the rank-2 face has exactly two spectral
invariants, so `(m,q)` generate the entire v24 object — `r = q/m²`. **The whole v24
entropy landscape is the moment doublet of the linear pair `(X, X#)`: two linear
moment fields over the event-space, nothing else.**

## How verified (no step taken on faith)

| check | scope | result |
|---|---|---|
| C1 at `p = E_11` | symbolic `X` (27 params) | `m`, `q` ✓ |
| C1 along **all 16** families incl. off-u | symbolic `X` over `Q(t)`, **no covariance shortcut** | `m`, `q` ✓ |
| covariance `φ_Y(g·p) = φ_{g⁻¹Y}(p)` | `g∈{(01),(012)}`, `Y∈{X,X#}`, off-u samples | ✓ |

**Closure argument** (carries the "all `p`" load): every rank-1 `p = g·E_11`,
`g ∈ F_4` (Freudenthal–Borel transitivity); C1 is F₄-covariant
(`m(g·E_11;X) = m(E_11; g⁻¹X)`, same for `q`, since F₄ preserves `Tr, ∘, #`); hence C1
at `E_11` for symbolic `X` ⇒ C1 at all `p` for all `X`. The 16 along-family symbolic
checks are the independent confirmation that no convention/covariance bug hides.

## Completeness — all of v24 reproduced FROM the doublet

- **(a) vacuum DERIVED:** `(I/3)# = I/9` ⇒ `q ≡ 1/9`, `m ≡ 2/3`, `r ≡ 1/4`. The vacuum
  is homogeneous *because both moments of `(I/3,(I/3)#)` are constant*.
- **(b) diagonal direction-blindness DERIVED:** diagonal `X` ⇒ `X#` diagonal ⇒
  `⟨X#,p⟩` sees only `diag(p)` and `|offdiag|²`; the slot `e_k` enters only via
  `|s e_k|² = s²`, so the three `(0,1)` families are identical (`k = 0,1,7` checked
  equal). The octonion direction enters the moments only through the off-diagonal
  entries of `X`/`X#`.
- **(c) recorded generic-X tables:** off-u `r(2) = 2727493/12700800`, C_u-phase
  `r(3) = 503003/2252432` — exact match.
- **(d) eigenframe critical points:** transverse-real `(1,0)` `dr/dt=0` at `{−1,0,1}`
  (standard frame); off-u numerator degree 10 (eigenframe-tracking) — the v24 finding.
- **(e) flattening DERIVED:** `X_s=(1−s)I/3+sX_gen` ⇒ moments affine in `s` near the
  constant vacuum moments; gradient `dr/dτ|_0 = 0` at `s=0`, `=13879/1837500` at
  `s=1/4`, `=629/58800` at `s=1` (recorded table).

## Anti-overclaim

C1 PASS establishes EXACTLY: the v24 landscape is the moment doublet of `(X,X#)`, a
classical cubic-Jordan adjugate identity (cited, not claimed novel). It is not a metric,
not geometry-from-entanglement, not J5, not a balance. Trap-guard #5 (no field equation
for the rational `r`; the objects are `(m,q)`) held.

**Gate 2: C1 PASS.**
