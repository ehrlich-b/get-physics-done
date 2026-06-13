# Phase 93 (v33.0) — GATE 0 SUMMARY: discharge the v32 deferred obligation, certify ε = 20

> **BINDING STOP GATE — VERDICT: PASS.** ε = λ_L − 2Λ = 32 − 12 = **20 is CERTIFIED** on a
> CORRECT, directly-run, control-validated full-tensor Lichnerowicz operator. The v32.0-B deferred
> obligation (ε=20 recorded on EVIDENCE — Boucetta Table V/VIII row 2 + degree-counting + the (1,1)
> Schur scalar + the fingerprint, the full anti-block Δ_L flagged UNTRUSTED after returning a
> spurious 28/4) is **DISCHARGED**. Exact over Q / Q(i).

**Drivers:**
- Step A (machinery-freeze control): `python3 -u code/lichnerowicz_response_fingerprint.py` → **T1 PASS, T2 PASS, all 5 norm directions exact, the 5:4 split exact** (T3 Gram rank-6 in progress at kill, rows 0–3 clean, consistent with the v32 record).
- Steps B–E: `python3 -u code/gate0_v33.py` → **ALL PASS** (~3 min, exact over Q).

---

## The result in one line

The OLD full operator on the verdict residue r(s01) gives `{H20: 28, H11: 32, H02: 4}` — the
spurious 28/4 anti-blocks v32 flagged. The CORRECTED operator (two principled bug-fixes, validated
by the provable control Hess(R_M)→32, **never** tuned to r) gives `{32, 32, 32}` on the SAME r, for
every matter direction. **Δ_L r = 32·r on every Kähler block ⇒ λ_L = 32 ⇒ ε = 20.**

---

## §A. Machinery-freeze control (Step A — run FIRST, before any new computation)

The v32 fingerprints reproduce **exact over Q** on the certified driver (no regression — the new
operator code does not touch `extract_tt`/`l2_tensor`, so the machinery is frozen):

| Fingerprint | Statement | Result |
|---|---|---|
| **T1** | `4(t_s01+t_a01+t_d1) + (t_s02+t_a02+t_s12+t_a12) == 0` (all blocks) | **PASS** (= 0 tensor) |
| **T2** | `t_d2 == 9(t_s01+t_a01+t_d1)` | **PASS** (= 0 tensor) |
| **Norm** | `‖TT(B3)‖² = (1/30)(TrM²)²` for s01, a01, d1, s02 (‖r‖²=2/15, TrM²=2), d2 (‖r‖²=6/5, TrM²=6) | **PASS** (all exact) |
| **Split** | block split `‖r₁₁‖²:‖r_anti‖² = 5:4` = (1/54):(2/135) of (TrM²)² | **PASS** (ratio 5/4 exact) |
| **T3** | single-generator residue Gram rank = 6 | in-progress (rows 0–3 clean; matches v32) |

The decisive freeze checks (T1, T2, all norms, the 5:4 split) reproduced byte-for-byte over Q. The
T3 Gram (rank 6) is a structural re-confirmation of the v32 record (the 7×7 L²-tensor Gram on
ρ-rational tensors is the ~40-min cost; rows 0–3 computed cleanly and consistently before the
machinery-freeze run was stopped — no deviation observed).

---

## §B. The operator fix (Step B — `lichnerowicz_response.py`)

The old full `lichnerowicz` failed on the (2,0)/(0,2) anti-blocks for **two independent reasons**.
Both are real math errors (NOT r being a non-eigentensor — the control §C proves the operator was
wrong). The new `lichnerowicz_full_v33` implements both fixes as **derived**, validated by the
provable controls C1/C2a/C2b, **never** by flipping a sign to hit 32 on r. The validated
`lichnerowicz_11` ((1,1) sector) is **untouched**; the old `lichnerowicz` is now a thin alias of the
corrected operator (its UNTRUSTED warning removed).

### BUG 1 — the rough Laplacian used one ordering doubled

The connection Laplacian is the **symmetric trace** of the second covariant derivative:
```
∇*∇ T = −( g^{a b̄} ∇_a ∇_b̄  +  g^{ā b} ∇_ā ∇_b ) T          [CORRECT, −1 each]
```
The old `rough_laplacian` computed `−2 g^{a b̄} ∇_a ∇_b̄ T` — ONE ordering doubled. On a SCALAR the
two orderings commute (so the +12/+32 sign-pin passed and hid the bug); on a TENSOR they differ by
the curvature commutator, which acts with OPPOSITE sign on holo vs antiholo indices, so the old
operator was **not conjugate-symmetric** (it split the anti-blocks: 28 on (2,0), 4 on (0,2) — see §C
before/after). **Fix:** compute BOTH orderings —
- `L1 = g^{a b̄} ∇_a(∇_b̄ T)` — inner antiholo `∇_b̄ T` (`_nabla(blocks,b,ebar=True)`), outer holo
  `∇_a` (connects UNbarred μ,ν), contract `g^{a b̄}=ginv[b,a]`;
- `L2 = g^{ā b} ∇_ā(∇_b T)` — inner holo `∇_b T` (`_nabla(blocks,b,ebar=False)`), outer antiholo
  `∇_ā` (connects BARRED μ,ν via GamB), contract `g^{ā b}=ginv[a,b]`;
- `∇*∇ T = −(L1 + L2)`.

This restores conjugate symmetry — the (2,0) and (0,2) outputs become EQUAL, as they must for a real
tensor.

### BUG 2 — the curvature term R̊ had the wrong sign on the anti-blocks

With BUG-1 fixed alone, the control reads **16** on the anti-blocks (12 + 12 − 2·R̊ = 16 forces R̊ =
+4, but the control requires R̊ = **−4**). The old per-block hand-written contractions
(`R[a][k][b][l]…`, `R[k][a][l][b]…`) had a sign/antisymmetry error from `_R_low`'s pair-ordering.
**Fix:** derive ALL blocks from ONE uniform index-honest formula
```
(R̊h)_{μν} = − R_{μ ρ ν σ} h^{ρσ},    h^{ρσ} = g^{ρρ'} g^{σσ'} h_{ρ'σ'}   (g^{a b̄}=ginv[b,a])
```
built with the full lowered Riemann `_R_low` (which carries the Riemann symmetries consistently) +
full metric raising (`_graise`). The overall **sign is FIXED by reproducing the validated (1,1)
normalization**: `−R_{a ρ b̄ σ} h^{ρσ} = R_{a b̄ c d̄} g^{c f̄} g^{e d̄} h_{e f̄} = Ric = +6g` on the
metric — **verified entry-by-entry on a generic Hermitian (1,1) input AND on g** (the bare
`+R_{μρνσ}` gives −6g, a Riemann-sign-convention artifact of `riemann_kahler`). Routing the
anti-blocks through this SAME uniform formula makes them inherit the consistent sign automatically
(R̊_anti = −4); the sign is fixed by the C1/C2b CONTROLS, NOT by r.

---

## §C. The controls — the operator's oracle (Step C; NO tuning to r)

All exact over Q. C2b is the **no-tuning certificate**: Hess(R_M) is a PROVABLE Δ_L-eigentensor at
32 on every block (Besse: on an Einstein manifold Δ_L∘δ* = δ*∘Δ_H, with ω=dR_M, Δ_H(dR_M)=32 dR_M ⇒
Δ_L(Hess R_M) = Δ_L(δ*(dR_M)) = δ*(Δ_H(dR_M)) = 32·Hess(R_M)).

| Control | Statement | Result (exact over Q) |
|---|---|---|
| **C1** | Δ_L g = 0 on ALL blocks (g is Δ_L-harmonic on KE; pins R̊(g)|₍₁,₁₎=6g) | **PASS** |
| **C2a** | Δ_L(Hess φ_s01) = **12** on (1,1); anti-blocks **VANISH** (Matsushima: λ₁ ⇒ holomorphic Killing ⇒ ∇_a∇_b φ = 0) | **PASS** `{0:ZERO, 1:12, 2:ZERO}` |
| **C2b** | Δ_L(Hess R_M) = **32 on ALL THREE blocks**, (2,0)==(0,2) — for **s01, d1, AND GEN=d2** (detM=−2≠0) | **PASS** `{0:32, 1:32, 2:32}` all three directions, conjugate-symmetric |
| **REG** | `lichnerowicz_11(r[1](s01))` → (1,1) eigenvalue **32** (the validated (1,1) path intact) | **PASS** |

---

## §D. The verdict residue r (Step D — read ONLY after C1/C2a/C2b PASS)

For each matter direction the cliff-free TT residue `r = extract_tt(grad_bilinear(φ_M))` is
extracted (confirmed `consistent=True, tr_zero=True, div_zero=True`, all three blocks nonzero), then
`Δ_L r` is compared to `32·r` entry-by-entry over Q via `cancel(Δ_L r[k][a,b] − 32·r[k][a,b]) == 0`:

| Direction | matter | `Δ_L r` per block [H20, H11, H02] | exact 32 all blocks |
|---|---|---|---|
| **s01** | λ₁ (sparse) | `{0:32, 1:32, 2:32}` | **PASS** [✓,✓,✓] |
| **a01** | λ₂ (imag) | `{0:32, 1:32, 2:32}` | **PASS** [✓,✓,✓] |
| **d1** | λ₃ (Cartan) | `{0:32, 1:32, 2:32}` | **PASS** [✓,✓,✓] |
| **GEN = d2** | diag(1,1,−2), **detM=−2≠0** | `{0:32, 1:32, 2:32}` | **PASS** [✓,✓,✓] |

(GEN=d2 is the genuine detM≠0 witness — it carries a nonzero degree-3 invariant and verifies the
residue eigenvalue is detM-independent. A fully-dense 8-channel matter makes `cov_hessian(R_M)` a
multi-thousand-term ρ-rational object whose Δ_L exceeds the watchdog window; d2 is the standard
tractable detM≠0 representative, matching v32's fingerprint choice. Recorded as `M_DENSE` for an
optional slow cross-check.)

### Before / after (the airtight proof the 28/4 was purely an operator bug)

On the SAME extracted residue r(s01):

| Operator | [H20, H11, H02] eigenvalues |
|---|---|
| **OLD** (one-ordering ∇*∇ + buggy per-block R̊) | `{0: 28, 1: 32, 2: 4}` — the spurious 28/4 (NOT conjugate-symmetric: 28≠4 is BUG-1; neither is 32 is BUG-2) |
| **CORRECTED** `lichnerowicz_full_v33` | `{0: 32, 1: 32, 2: 32}` — exact, conjugate-symmetric |

`r` tracks the provable C2b control identically at every step (both 32 on every block). The OLD
operator gives the control AND r both wrong on the anti-blocks; the corrected operator gives the
control AND r both 32 — the airtight proof r is a clean λ_L=32 eigentensor and the 28/4 was purely
the operator bug. Note (28+4)/2 = 16 = the BUG-1-fixed-only reading, consistent with §B BUG-2.

---

## §E. Verdict

**GATE 0 (v33.0): PASS.** All controls pass (C1, C2a, C2b, REG) AND Δ_L r = 32·r EXACT on EVERY
Kähler block (the (1,1)-27 AND the (2,0)+(0,2) anti-27s) for all four directions (s01, a01, d1,
GEN=d2 detM≠0). Therefore:

> **λ_L = 32 on the full tensor** (all three Kähler sectors, conjugate-symmetric) ⇒
> **ε = λ_L − 2Λ = 32 − 12 = 20 CERTIFIED** on a directly-run, control-validated full-tensor
> operator. **The v32 deferred obligation is DISCHARGED.**

The binding STOP condition (operator validated by C2b but r ≠ 32 on some block) did **not** trigger —
the gate is a clean PASS, no fabrication.

---

## Fences (binding, verbatim — carried from RESEARCH §5 / 92-VERDICT V5)

This is the deformation-complex **DICTIONARY** of a FROZEN imported geometry. **ε=20 is a Δ_L-STIFFNESS
of the frozen deformation complex, NOT a dynamical response.** No dynamical metric, no selection law,
no κ here (κ is NOT Newton's constant). **NO Einstein-equation / G=κT / gravity / dark-matter /
geodesic language.** The frozen Fubini–Study geometry is **USED, not derived**; signature Riemannian
(Wall 2 unpaid). This is the frozen deformation-complex dictionary; the v18/v20 MM corpse stays
buried (this is the BASE's deformation complex on CP², not a fiber connection). This Gate-0 result
does NOT retract v17–v21 (Block-C statements). Paper 5 remains the only result in the
more-than-nothing column. Milestone HOLD for human ratification; do NOT self-register v34.

---

## Artifacts

- `code/lichnerowicz_response.py` — corrected machinery: `rough_laplacian` (both orderings, BUG-1),
  `Rdot` (uniform index-honest `−R_{μρνσ}h^{ρσ}` via `_R_low`+`_graise`, BUG-2), new
  `lichnerowicz_full_v33`, `lichnerowicz` now a corrected alias; `lichnerowicz_11` untouched.
- `code/gate0_v33.py` — the Gate-0 driver (Steps C/D/E: C1/C2a/C2b/REG controls + the r-reading +
  the non-fabricating verdict).
- `derivations/93-GATE-0-SUMMARY.md` — this file.

## Reproducibility

sympy 1.14.0, Python 3.14, Darwin arm64. Exact rational arithmetic over Q / Q(i) (no RNG, no seeds
in the verdict path; floats illustrative only). `code/.p92_basis_images.pkl` disk cache reused for
`extract_tt` (the 243 gauge+conformal basis (tr_g, δ) monomial images). Per-entry eigenvalue tests
use `cancel(Δ_L X[k][a,b] − λ·X[k][a,b]) == 0`.
