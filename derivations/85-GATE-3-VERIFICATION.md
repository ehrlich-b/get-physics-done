# Phase 85 — GATE 3 Independent Verification (C2 + C3: field equation, eigenvalues, fingerprint)

**Verifier:** independent GPD verifier (separate, from-scratch code path)
**Date:** 2026-06-10
**Claims under test:**
- **C2** — the mean-curvature vector `ΔP := Σ_i (1/4) p_i''(0)` over an orthonormal canonical-geodesic frame satisfies `ΔP == −λ₁ (E_11 − I/3)`, with **λ₁ = 48** on OP² (16-frame) and **12** on the CP² cut (4-frame); equivalently every moment field obeys `Δ(φ_Y − ⟨Y,I/3⟩) = −λ₁(φ_Y − ⟨Y,I/3⟩)`. Field equations: `Δm = −λ₁(m − (2/3)Tr X)`, `Δq = −λ₁(q − σ₂(X)/3)`.
- **C3** — every moment along every canonical geodesic is `a + b·cos2θ + c·sin2θ` (frequency ≤ 2; level ≤ 1).

**VERDICT: C2 CONFIRMED with λ₁ = 48 (OP²) and 12 (CP² cut). C3 CONFIRMED. Confidence HIGH (INDEPENDENTLY CONFIRMED, exact over Q / Q(t)).**

---

## Independent assembly of ΔP and λ₁ (my own families, my own Laplacian)

In `/tmp/vm_indep_check.py` I built the `vv*` families, the second-derivative-at-0 operator, and the mean-curvature sum from scratch (no import of the phase-85 drivers or V24 geometry). Results:

```
DeltaP_full (16-frame) = diag(−32, 16, 16)
DeltaP_cut  ( 4-frame) = diag(−8,  4,  4)

[PASS] OP^2 16-frame: λ₁ = 48, full-vector ΔP == −λ(E_11 − I/3)  (all 27 comps)
[PASS] CP^2  4-frame: λ₁ = 12, full-vector ΔP == −λ(E_11 − I/3)  (all 27 comps)
[PASS] ratio = 4  ( = dim ratio 16/4)
[PASS] λ from E_22 component: full=48, cut=12  (agrees with E_00 extraction)
```

λ₁ is extracted as `−ΔP_00 / (E_11 − I/3)_00 = −(−32)/(2/3) = 48` and `−(−8)/(2/3) = 12`. **Two independent extractions** (the E_00 and the E_22 diagonal components) give the same λ, and the full 27-component vector proportionality `ΔP = −λ(E_11 − I/3)` holds exactly — this is a genuine eigenvector statement, not a single-component coincidence.

## The arithmetic is transparent (and the test has teeth)

```
[PASS] c11 (cos²θ, freq 2) passes freq≤2:  True
[PASS] c11² (cos⁴θ, freq 4) passes freq≤2: False   ← the discriminating control: the test CAN say no
[PASS] (1/4)·c11''_t(0) = −2   (per-direction second-θ-derivative of cos²θ)
```

Chain rule: `dt/dθ = (1+t²)/2 → 1/2` at t=0, so `f''_θ(0) = (1/2)²·f''_t(0) = (1/4)·f''_t(0)`. Each canonical-geodesic direction contributes `−2` to `Δφ_{E11}`. Then:
- 16 directions ⇒ `ΔP_00 = 16·(−2) = −32` ⇒ `λ₁ = (32)/(2/3) = 48`.
- 4 directions ⇒ `ΔP_00 = 4·(−2) = −8` ⇒ `λ₁ = 12`.

## λ₁ is NOT hardwired (adversarial audit)

`extract_lambda(DP)` in the executor computes `−⟨E_11,ΔP⟩ / (⟨E_11,E_11⟩ − ⟨E_11,I/3⟩)` — both numerator (the actual Laplacian of `c11`, assembled from the families' second derivatives) and denominator (`1 − 1/3 = 2/3`) are *derived*. The literals `48`/`12` appear only as post-hoc `== 48` / `== 12` assertions gating the PASS against the pre-registered values; they never feed the computation. My from-scratch script reproduces 48 and 12 without referencing them until the final equality check. **Non-hardwired confirmed.** The repo verifier independently extracts λ from the *E_22* component on a *different* (5/13-12/13) rotated frame and also gets 48/12.

## Frame-independence is genuine (not a relabel)

```
[PASS] std (1,0) tangent  ≠  rotated-real-+ tangent   (genuinely different frame)
       e_std supports only the x3-slot (E_22 entry);
       e_rot mixes the E_22 and E_33 entries (3/5-4/5 Pythagorean rotation).
```

Both the standard cut frame and the 3/5-4/5 rotated cut frame give `ΔP_cut = diag(−8,4,4)`; the entry-swap Spin(9) automorphism leaves `ΔP_full` invariant. The repo verifier additionally uses a 5/13-12/13 rotation and agrees. These are three genuinely distinct orthonormal frames, all yielding the same mean-curvature vector — a real frame-independence test, not a coordinate relabeling.

## The c11 unit-speed certificate

The certificate `c11(t) = ((1−t²)/(1+t²))² = cos²θ` is checked for all 16 families in Gate 0; a failure fail-fast-stops the run. (Note: `mean_curv` sums over the static family list rather than a filtered survivor list, so the cert acts as a *global precondition* on the run, not a per-family filter — benign because all 16 families pass. I independently confirmed the (1,1) family passes the cert.) This certificate is what *fixes the normalization*: λ₁ is reported in the normalization where the `vv*` families are unit-speed canonical geodesics.

## The field equation is on the UNNORMALIZED doublet (trap guard #5 respected)

I re-derived the means and the field equation symbolically:

```
[PASS] ⟨X,I/3⟩ == (1/3)Tr X                          ⇒ m̄ = TrX − ⟨X,I/3⟩ == (2/3)Tr X
[PASS] ⟨X#,I/3⟩ == σ₂(X)/3 == Tr(X#)/3                ⇒ q̄ = σ₂(X)/3
[PASS] Δq == −48(q − σ₂(X)/3)   [symbolic X, my own 16-frame assembly]
[PASS] q·(1+t²)² is a polynomial of degree 4 in t      (level-1, NOT rational r)
```

The means use the F_4-average idempotent `p̄ = I/3` (exact, no integration). The equation is on the **polynomial** `q` (degree ≤ 4 after clearing `(1+t²)²` ⇒ frequency ≤ 2 ⇒ Laplace level 1), **not** the banned rational `r = q/m²`. Trap guards #5 (no field equation for `r`) and #6 (only the first-order Helmholtz statement) are respected.

## External literature cross-check on the eigenvalues

- **CP² cut (= 12):** Ikeda–Taniguchi (Osaka J. Math. 15, 1978) give the Laplacian spectrum on **functions** on `CP^n` as `λ_k = 4k(k+n)` in the Fubini-Study normalization (holomorphic sectional curvature 4). At `k=1, n=2`: `λ₁ = 4(n+1) = 12`. **The run's CP² value matches exactly.**
- **Ratio (= 4):** `λ₁(OP²)/λ₁(CP²) = 48/12 = 4` equals the real-dimension ratio `16/4`. For these rank-1 two-point-homogeneous spaces sharing the same canonical-geodesic structure, this is the expected relationship and is the internally-forced consequence of the (16 vs 4)-direction assembly.
- **OP² (= 48):** whether 48 is the canonical/Borel-normalized first eigenvalue of `OP² = F₄/Spin(9)` in the Cahn–Wolf (1976) / Besse tables is **normalization-dependent** and the prompt correctly marks this cross-check **non-blocking**.

**Normalization note (important, non-blocking):** the run does *not* import a metric and rescale to hit the literature numbers. It fixes its normalization *intrinsically* via the unit-speed `c11 = cos²θ` certificate, and the value 12 then *coincides* with `4(n+1)|_{n=2}`. The decisive, normalization-independent facts that *can* be pinned — (a) CP² = 12 = `4(n+1)`, (b) the ratio = 4 = the dimension ratio — both hold. So the eigenvalues are internally consistent and consistent with the one external value that is normalization-pinned.

## C3 fingerprint — independently confirmed

Every moment (`m` and `q`), symbolic `X`, on all four cut families and the off-u (1,1) family, satisfies `moment·(1+t²)²` = degree-≤4 polynomial (verified directly). The hand anchor `diag(7,5,3)` on (1,0): `m = 9 − cos2θ`, `q = 18 − 3cos2θ` reproduces (executor PASS; consistent with my `q*(1+t²)²` degree-4 result).

## Confidence

**HIGH.** C2's eigenvector identity `ΔP = −λ₁(E_11 − I/3)` is verified exactly over all 27 components by an independent family/Laplacian assembly; λ₁ = 48 and 12 are derived (not hardwired), confirmed from two different components and three different orthonormal frames; the field equation on the unnormalized doublet is re-derived symbolically; the means use the exact F_4-average. The single externally-pinnable eigenvalue (CP² = 12) matches Ikeda–Taniguchi `4(n+1)`, and the ratio is exactly the dimension ratio 4. The OP² = 48 absolute value is normalization-dependent (non-blocking, as designed). No substance-level discrepancy found.
