# Phase 86 — GATE 2 Independent Verification (B1 MaxEnt + B2 the response field)

**Verifier:** independent (separate code path + from-scratch re-derivation)
**Date:** 2026-06-11
**Milestone:** v26.0 Phase 86 — "The Sourced Field Equation," J5-on-the-variety step 2
**Setup:** vacuum perturbation `X = I/3 + eps*M`, `M` traceless (26 params), exact in `Q[eps]/(eps^3)`, `Q(t)` along families. `<A,B>=Tr(A o B)`, `X# = X x X` (Freudenthal adjoint), `C_p` = Peirce-0 compression.

**Verdict: B1 CONFIRMED, B2 CONFIRMED. Confidence HIGH.**

---

## What was run

1. **Executor** `code/variety_sourced_field_equation.py` re-run via `python3 -u` → **19/19 PASS** (all gates 0–5), 22.8 s. Gate 0 (machinery), Gate 1 (controls), Gate 2 (B1+B2) all PASS.
2. **Independent verifier** `code/variety_sourced_field_equation_verify.py` (eigenprojector-q + gradient-of-N M#, a *different* compression and a *different* sharp) → **10/10 PASS**. Reproduces m, q, dr=0, d²r=(9/4)G_M, and the positivity identity along a code path sharing none of the executor's sharp/compression machinery.
3. **My own from-scratch check** `/tmp/v86_scratch.py`, importing **neither** `variety_sourced_field_equation*.py` **nor** `variety_moment_doublet*.py`. I built independently: (i) my **own octonion product** by Cayley–Dickson doubling of the quaternions (verified unital, alternative, norm-multiplicative — a genuine composition algebra), (ii) the h₃(O) layout + Jordan product + trace form, (iii) **M# via the Hermitian adjugate / cofactor matrix** (distinct from both the executor's `MoM − Tr(M)M + σ₂(M)I` and the verifier's gradient-of-N), (iv) the compression and the Laplacian assembler. I ran the **entire pipeline twice** — once with RL's Fano-table product, once with my Cayley–Dickson product — and both reproduce every headline rational. **27/27 PASS.**

The adjugate octonion factor-order was **not** read off the repo: I tested both orders ("A" = `conj(x_{i+1} x_{i+2})`, "B" = reversed) and kept only the one satisfying the defining identities `(M#)# = N(M)·M` and `Tr(M#)=σ₂(M)`. Both my product and RL's selected order "B" uniquely. M# is then forced, not chosen.

---

## B1 — MaxEnt derived (`dq = dm/3`, `dr = 0` identically)

### Equations re-derived (from scratch, symbolic traceless M, exact in Q[eps])

```
m = Tr(X) - <X,E11>      = 2/3 - eps<M,E11>
q = <X#, E11>            = 1/9 - (eps/3)<M,E11> + eps^2 <M#,E11>
X# = I/9 - (eps/3) M + eps^2 M#          (verified entry-by-entry, all 27 components)
```

The `eps^1` coefficient `-(1/3)M` of `X#` is exactly the **sharp identity `I x M = -M/2` for traceless M** (polarization of #): `(I/3 + eps M)# = (I/3)# + eps (I/3 x M)·2 + eps^2 M#`, and `I x M = -M/2` gives the `-(eps/3)M` term. My from-scratch adjugate M# reproduces this `X#` expansion exactly — i.e. I confirmed `I x M = -M/2` independently as the consequence that makes the linear sharp coefficient `-(1/3)M`.

**`dq = dm/3` at first order:** `dq^(1) = -(1/3)<M,E11>`, `dm^(1) = -<M,E11>`. ✓ One field at first order, not two.

### `dr = 0` is an IDENTITY in Q[eps], not numeric (guard 1)

`r = q/m²` expanded to O(eps³); the `eps^1` coefficient is a **polynomial in the 26 M-params** that is **identically zero** (its total degree as a polynomial in the symbols is 0, value 0). This was checked:
- at `E11` for symbolic M (from scratch, both octonion products);
- **along all 16 families over Q(t)** — the `eps^1` coefficient of `r(p_i(t))` vanishes for every family, i.e. the landscape is flat at first order **at every event p**, not just at E11.

This is the vacuum MaxEnt property, derived. **INDEPENDENTLY CONFIRMED.**

---

## B2 — the response field (`d²S = (9/2)G_M`, positivity, relative entropy)

### `d²r = (9/4) G_M` with `G_M(p) = <M#,p> - (1/4)<M,p>²`

The `eps²` coefficient of `r` equals `(9/4)·G_M` exactly, with `G_M = c - a²/4`, `a=<M,E11>`, `c=<M#,E11>`. Re-derived from scratch (both octonion products), symbolic traceless M. **INDEPENDENTLY CONFIRMED.**

Provenance of the `c - a²/4` structure: `r = q/m² = (1/9 - (eps/3)a + eps²c)/(2/3 - eps a)²`; expanding `1/m²` and collecting `eps²` gives `(9/4)(c - a²/4)`. Hand-checked.

### Branch smoothness `S = f(r)` at `r = 1/4` (guard 2)

Face density eigenvalues `lam_± = 1/2 ± (1/2)√(1-4r)`. With `u = 1-4r`:
```
S(u) = -lam_+ log(lam_+) - lam_- log(lam_-)
     = log2 - u/2 - u²/12 - u³/30 - u⁴/56 - ...     (NO sqrt(u) terms)
```
The ±√u branches **cancel** → `S` is analytic in `u` (hence in `r` at `r=1/4`). I confirmed the series has **no half-integer powers of u** to order u⁴. Then `f'(1/4) = -4·dS/du|_0 = -4·(-1/2) = 2`. So `d²S = f'(1/4)·d²r = 2·(9/4)G_M = (9/2)G_M`. **INDEPENDENTLY CONFIRMED.** (Note: the executor's `_entropy_branch` printed a `smooth` flag against a wrong reference series `log2 - u/2`; the executor nonetheless gates only on `f'(1/4)=2` and "no sqrt" — both correct. My from-scratch series gives the exact analytic expansion above. **Convention/cosmetic only — the decisive facts are right.**)

### Positivity `G_M ≤ 0` (structural)

`G_M(p) = det₂(C_pM) - (1/4)(Tr C_pM)² = -(1/4)(eigengap of C_pM)²`. Both identities verified from scratch:
- `det₂(C_pM) == <M#,p>` (the v25 doublet identity, on a generic off-u family);
- `G_M == det₂ - (1/4)(Tr)²` symbolically.

Since `(Tr)² - 4det₂ = (λ₊-λ₋)²` for the 2×2 face, `G_M = -(1/4)(eigengap)² ≤ 0` for **all** traceless M and **all** p. A 10-instance rational battery (M = diag and octonion-supported, p = E11/E22/E33/off-u families) gives `G_M ≤ 0` in every case. **INDEPENDENTLY CONFIRMED.**

### Relative-entropy identity

`S(rho_face || rho_vac) = log2 - S(rho_face)` exactly, with `rho_vac = I₂/2` maximally mixed on the 2-face. Verified symbolically (`Σ λ log λ + log2 == log2 - S`). The response field IS the second-order relative-entropy density. **INDEPENDENTLY CONFIRMED.**

---

## Anchors (Gate 1 controls reproduced)

| anchor | claimed | from-scratch (both products) | status |
|---|---|---|---|
| `M=diag(2,-1,-1)`, `G(E11)` | 0 | 0 | ✓ (face sees only the ∝I₂ block) |
| `M=diag(2,-1,-1)`, `G(E22)` | -9/4 | -9/4 | ✓ |
| `<M#,E22>` for that M | -2 | -2 | ✓ |
| `M=0` | all vanish | all vanish | ✓ |

The design sketch wrote `G(E22) = -2 - 1/4`; the correct value is `<M#,E22> - (1/4)<M,E22>²= -2 - 1/4 = -9/4`. The sketch's `-2-1/4` and the code's `-9/4` are the **same number** — sketch bookkeeping, substance correct.

---

## Discrepancies

- **None of substance.** Two cosmetic items, both non-blocking: (1) the executor's `_entropy_branch` `smooth` reference series is wrong but the gate rests only on the correct facts (no √u, f'(1/4)=2); (2) the sketch's `-2-1/4` = code's `-9/4`. Neither affects any verdict.

## Confidence

**HIGH.** Three independent code paths (executor; verifier with eigenprojector+grad-N; my from-scratch with adjugate M# on two independent octonion algebras) agree on every B1/B2 quantity. `dr=0` is established as a polynomial identity in Q[eps] (guard 1 satisfied), the branch is genuinely analytic with f'(1/4)=2 (guard 2 satisfied), and positivity is structural (`-(1/4)eigengap²`), not just sampled.

**B1 CONFIRMED. B2 CONFIRMED.**
