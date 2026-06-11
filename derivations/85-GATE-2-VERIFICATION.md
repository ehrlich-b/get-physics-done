# Phase 85 — GATE 2 Independent Verification (C1: the moment-doublet identity)

**Verifier:** independent GPD verifier (separate, from-scratch code path)
**Date:** 2026-06-10
**Claim under test:** **C1** — for all `X ∈ h_3(O)` and all rank-1 idempotents `p`:
> `m(p;X) := Tr(C_p X) == Tr(X) − ⟨X,p⟩`
> `q(p;X) := det₂(C_p X) == ⟨X#, p⟩`   (THE novel content)
with `⟨A,B⟩ = Tr(A∘B)`, `C_p` = Peirce-0 compression, `X#` = Freudenthal adjoint.

**VERDICT: C1 CONFIRMED. Confidence HIGH (INDEPENDENTLY CONFIRMED, exact over Q / Q(t)).**

---

## What I did (three code paths, not one)

| Path | Compression `C_p X` | Sharp `X#` | det₂ |
|---|---|---|---|
| Executor (`variety_moment_doublet.py`) | nested `2L²−3L+1` via `RL.jordan` | `X∘X − Tr(X)X + σ₂I` | `(Tr²−Tr(Y∘Y))/2` |
| Repo verifier (`..._verify.py`) | 27×27 eigenprojector `P_0` matrix | grad-of-N via Gram dual | literal `βγ−|x1|²` block det |
| **My from-scratch** (`/tmp/vm_indep_check.py`) | `2L²−3L+1` rebuilt from my own octonions | **entrywise Hermitian adjugate** | literal `βγ−|x1|²` block det |

My script imports **neither** `variety_moment_doublet*.py` **nor** `variety_entropy_landscape` for the algebra: it builds the octonion product from its own Fano table, `h_3(O)`, `Tr`, the Jordan product, `det_3`, and the families from scratch. It uses `RL.oct_mul` only as a *cross-check oracle* (confirmed my table == `RL.oct_mul` on 6 random pairs), and reads two recorded states' coordinates for the anchor triage.

## Re-run of both supplied drivers (reproduced, exact)

- Executor `variety_moment_doublet.py`: **27/27 PASS** (21 s). `ΔP_full = diag(−32,16,16)`, `ΔP_cut = diag(−8,4,4)`.
- Repo verifier `variety_moment_doublet_verify.py`: **11/11 PASS**, exit 0.

These are *re-runs* (necessary but not sufficient). The substance is the from-scratch path below.

## The sharp convention — re-derived, not trusted (the one place this could break)

The prompt flagged the octonionic off-diagonals of `#` as the fracture point. **It was:** my first entrywise-adjugate guess `conj(x2·x3) − α·x1` FAILED `(X#)# = N·X`. I then derived the correct convention by matching the pinned algebraic sharp entry-by-entry on symbolic `X`:

```
(X#).x1 = conj(x3 · x2) − α·x1      (slot [2][1])
(X#).x2 = conj(x1 · x3) − β·x2      (slot [0][2])
(X#).x3 = conj(x2 · x1) − γ·x3      (slot [1][0])
(X#)_00 = βγ − |x1|² ,  (X#)_11 = αγ − |x2|² ,  (X#)_22 = αβ − |x3|²
```

The product **order is load-bearing** (octonions don't commute: `x3·x2 ≠ x2·x3`). With the corrected order my entrywise sharp is **pinned to the repo sharp** by four independent identities:

```
[PASS] entrywise-adjugate sharp == X∘X − Tr(X)X + σ₂I   (symbolic, 27 params)
[PASS] Tr(X#) == σ₂(X)                                  (symbolic)
[PASS] (X#)# == det₃(X)·X                                (3 random octonionic pts)
[PASS] d(X,X,X) == 6·det₃(X)                             (pins det₃ order (x2 x1)x3)
```

This is a genuine independent re-derivation: I found the convention by *matching*, and the discovered correction (a flipped product order) is itself diagnostic that the octonionic # is non-trivial.

## The novel identity — independently confirmed

```
[PASS] q := det₂(C_{E11} X) == ⟨X#, E_11⟩            (symbolic X, 27 params)
[PASS] m := Tr(C_{E11} X)   == Tr(X) − ⟨X, E_11⟩      (symbolic X)
[PASS] det₂(C_{E11} X) == (X#)_00 = βγ − |x1|² of X   (compression-free cofactor)
[PASS] off-u(1,1) over Q(t): det₂(C_p X) == ⟨X#,p⟩    (generic X, full family)
```

The third line is the cleanest structural fact: **the det₂ of the Peirce-0–compressed face equals, identically in the 27 symbolic parameters, the bare Freudenthal cofactor `(X#)_00 = βγ − |x1|²` of `X` itself** — the compression does no work on the determinant beyond exposing the cofactor. That is the geometric heart of C1, and it is the lower-2×2 block determinant in the engine layout `(x1 = X[2][1])`, matching the design-sketch step (ii).

## Anchors reproduced (convention triage)

```
[PASS] diag(7,5,3) @ E_11:  m=8, q=15, r=15/64        (recorded 84-GATE-2)
[PASS] generic off-u r(2) = 2727493/12700800          (recorded)
[PASS] (I/3)# == I/9  ⇒ q≡1/9, m≡2/3                  (vacuum homogeneity DERIVED)
```

The vacuum row is now *explained*: both moments of the pair `(I/3, (I/3)#=I/9)` are constant, so the v24 homogeneity at `I/3` is forced, not coincidental.

## Covariance closure — logically audited

C1 at `E_11` for symbolic `X` extends to all rank-1 `p` by F_4-covariance. The load-bearing requirement is **sharp-equivariance** `(g·X)# = g·(X#)`, which I verified directly for `g ∈ {(01),(012),swap23}`:

```
conj_perm (01)/(012)/swap23: Tr-preserved, trace-form-preserved <gX,gY>=<X,Y>,
                              sharp-equivariant (gX)#==g(X#)  — ALL True
conj_perm (012): det_3 invariant on a random octonionic point  — True
(01)·E_11 == E_22                                              — True
```

So `q(g·p; X) = ⟨X#, g·p⟩ = ⟨g⁻¹X#, p⟩ = ⟨(g⁻¹X)#, p⟩ = q(p; g⁻¹X)` is valid; the closure is sound **given** F_4-transitivity on rank-1 idempotents (imported Borel fact — this is where the family-sampled argument explicitly leans on imported group theory, correctly flagged in the prompt's anti-overclaim). The covariance *identity itself* is verified on the autos tested and on off-u sample points.

## Adversarial findings

- **No hidden floats on a decisive line for C1.** (The single `float()` in the executor is a *sort key* for the critical-point list in completeness (d); the equality verdict `roots==[-1,0,1]` is exact sympy.)
- **Diagonal direction-blindness is derived, not observed:** `X` diagonal ⇒ `X#` diagonal ⇒ `q=⟨X#,p⟩` sees only `diag(p)` and `|offdiag(p)|²`, hence is independent of the octonion direction `e_k` (k=0,1,7 give identical `q`). I confirmed `X#` diagonal for `diag(7,5,3)`.
- **Completeness is genuine:** `r = q/m²` is a function of the doublet alone; all of v24's recorded tables (vacuum, diagonal, generic `r(2)`, flattening `dr/dτ|_0` table, eigenframe critical points) reproduce from `(m,q)`.

## Confidence

**HIGH.** C1 is an exact polynomial identity over Q (27 free params) at `E_11` and over Q(t) along an off-u family, confirmed by a third code path with an independently-derived sharp. The only subtlety (octonionic # product order) was caught and resolved by direct matching. The identity is — as the prompt states — classical cubic-Jordan adjoint/cofactor theory (Jacobson/McCrimmon/Springer); novelty is in the *doublet reading*, not the identity. No substance-level discrepancy found.
