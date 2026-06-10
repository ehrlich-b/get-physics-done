# Slot 83 / v23.0 — GATE 2 VERIFICATION (independent)

**The Two-Term Balance Question (Jacobson J5, fiber side) — independent verification of
Gate 1 (calibration) + Gate 2 (THE TEST).** Performed BEFORE ratification, on a decisive
path built INDEPENDENTLY of `code/entanglement_two_term.py` (that driver was read only to
learn the claims; it was NOT imported as evidence).

- **VERDICT UNDER TEST:** Gate 2 = **DEAD at degree ≤ 3** (no program-native deg-≤3
  Spin(9)-invariant `A` forces a non-degenerate two-term balance `S_face + λA` at X=I/3).
- **OUTCOME: INDEPENDENTLY SUPPORTED. [CONFIDENCE: HIGH].**
- Exact over Q throughout (entropy/log symbolic). No κ, no Λ, no `G=κT`.
- Sandbox: Python 3.14 / sympy 1.14.0 (code executed; nothing fabricated).

---

## Independence of method (how this differs from the executor)

| object | executor's method | THIS verifier's INDEPENDENT method |
|--------|-------------------|-------------------------------------|
| linchpin `∇S_face(I/3)=0` | general 27-dim `H`, ε-series of vN entropy | **closed-form 2×2 corner eigenvalues** `μ_±=(1±r)/2`, `r²=((β−γ)²+4\|x1\|²)/(β+γ)²`, then symbolic `sympy.series` of `S=−Σμlogμ` |
| Fisher Hessian spectrum | ε² coefficient of general-H series | independent λ-scaled `series(…,lam,0,3)` of the closed-form S on the 10-dim face block; eigenvalues via `Matrix.eigenvals()` |
| candidate gradients | driver's `grad` at I/3 | I differentiate the **SSOT `det_3` polynomial** (`ring_lemma_verification.det_3(X_from_symbols)`) and the norms myself |
| forced-λ sweep | driver `gate2()` `linsolve` | my **own** `forced_lambda_nonzero(gradS,gradA,gradg)` routine, written from scratch, that takes `gradS` as a GENERAL argument |
| anti-vacuity | driver self-test | I feed my routine HAND-BUILT off-faithful gradients and confirm `forced=True` |

**Guards held on my decisive path:** `octonion_algebra` NOT in `sys.modules`; `numpy` NOT
in `sys.modules` at decisive time; `det_3`/`jordan`/`Tr` native to
`ring_lemma_verification`; `det_3(diag(2,3,5))==30` exact; coord layout confirmed
(`_flat27(X_from_symbols(c))==[c0…c26]`, identity flat = `[1,1,1,0×24]`,
0/1/2=α/β/γ, 3..10=x1, 11..18=x2, 19..26=x3). No numpy.linalg on decisive paths.

---

## 1. THE LINCHPIN — `∇S_face(I/3)=0` in all 27 directions + Fisher spectrum — **PASS**

Independent closed-form route (rank-2 face `q=E22+E33`, corner `[[β, x1],[x1*, γ]]`,
compress-then-normalize `ρ=corner/(β+γ)`, density eigenvalues `μ_±=(1±r)/2`):

| check | independent result | claim | status |
|-------|--------------------|----- |--------|
| `S_face(I/3)` | `log(2)` exact | log 2 | ✓ |
| diagonal (β−γ) direction, `β=1/3+s,γ=1/3−s` | `S = log2 − (9/2)s²` | ∇=0, Fisher −9/2 | ✓ |
| off-diagonal x1 direction, `\|x1\|²=u²` | `S = log2 − (9/2)u²` | ∇=0 | ✓ |
| scale (β+γ) direction, `β=γ=1/3+w` | `S ≡ log2` identically | ∇=0, flat | ✓ (scale-invariant) |
| non-face coords {0}∪{11..26} | S independent of them (closed form is a function of β,γ,\|x1\|² only) | ∇=0 trivially | ✓ |

⇒ **`∇S_face(I/3)=0` in ALL 27 tangent directions** (the closed form makes this
manifest: S depends only on the face block {1..10}; the order-ε¹ coefficient is `0`).

**Face Hessian spectrum (independent, on the 10-dim face block, standard basis
`h1=δβ,h2=δγ,h3..h10=x1`):** the λ-scaled series gives the Fisher form
`−(9/8)(h1−h2)² − (9/2)Σ_{i=3..10}h_i²`, with

```
   eigenvalues  =  { 0 (×1),  −9/2 (×1),  −9 (×8) }   — ALL ≤ 0  ⇒  I/3 is the MAX
```

byte-for-byte the Gate-1 claim. The single `0` = the (β+γ) scale direction; `−9/2` =
the (β−γ) traceless-diagonal; `−9` = each of the 8 x1-octonion directions.

**This is the degenerate-spectrum point** (`ρ_face(I/3)=½I₂`, both eigenvalues 1/2) where
a subtle error would hide. It does not: an entirely independent expansion method
(closed-form corner eigenvalues, not the executor's general-H ε-series) reproduces the
vanishing gradient AND the exact `{0,−9/2,−9×8}` Fisher spectrum.

> Note: a literal `d²S/ds²|₀` via `sympy.diff(...).subs(s,0)` returns `0` because the
> `sqrt(r²)` branch is non-smooth at the degenerate point; the correct object is the
> `series`/λ-scaled expansion, which cleanly yields `−9/2`. Flagged for transparency —
> it does NOT affect the verdict (the polynomial Fisher form is unambiguous).

---

## 2. THE EXHAUSTIVE SWEEP — no forced λ in any of 64 cells — **DEAD confirmed**

**Candidate gradients at I/3 (I differentiated the SSOT `det_3` and the norms myself):**

| generator | ∇ at I/3 (nonzero coords) | claim | ✓ |
|-----------|---------------------------|-------|---|
| α | `e_0` | e_0 | ✓ |
| T=β+γ | `e_1+e_2` | e_1+e_2 | ✓ |
| Q_v | `−⅓(e_1+e_2)` | `=−⅓∇T` | ✓ |
| **Q_s** | **`0`** | **∇Q_s=0** | ✓ |
| det_3 | `⅑(e_0+e_1+e_2)` | `=⅑∇Tr` | ✓ |
| Tr (constr) | `e_0+e_1+e_2` | — | ✓ |
| Tr_face (constr) | `e_1+e_2` | — | ✓ |

**Every candidate gradient lies in the diagonal `span{e_0,e_1,e_2}`** (coords 3..26
identically zero) — verified for all 16 candidates. This is **disjoint** from the
traceless Fisher block (β−γ, x1) where S_face curvature lives ⇒ no shared block ⇒ no
Jacobson saddle.

**Criticality sweep** (16 candidates × 4 constraints = 64 cells), solved with my own
routine `gradS + λ∇A − μ∇g = 0` and `gradS=0`:

```
   ANY cell forces λ≠0 ?  ->  False
   Forced cells: []
   INDEPENDENT VERDICT:  DEAD at degree ≤ 3
```

Because `∇S_face(I/3)=0`, `(λ,μ)=(0,0)` solves criticality in EVERY cell ⇒ `λ=0` always
allowed ⇒ `λ≠0` never forced. The three failure modes all confirmed by explicit
`linsolve` solsets (most-dangerous candidate `det_3` spot-checked):

- **tautology** `det_3 | none`: `{(0,)}` ⇒ λ=0 forced.
- **constraint-absorbed** `det_3 | fixed_Tr`: `{(9μ, μ)}` (incl. (0,0)); `det_3 | fixed_det`: `{(μ,μ)}`; `Q_v | fixed_Tr_face`: `{(−3μ,μ)}` — all include (0,0).
- **λ-glaze** `Q_s | none`: `{(λ,0)}`, λ FREE ⇒ DEAD (bug-guard #2 — a free λ is DEAD, not LIVE).

**Obstruction is FIRST-order, independently confirmed:** `det_3` Hessian on the β−γ
Fisher direction `= −2/3` (matches summary), i.e. second-order structure on the shared
block DOES exist — but it is never triggered because the entropy gradient vanishes, so no
equation forces λ off 0. The death is `∇S_face=0` at the max, not a 2nd-order near-miss.

---

## 3. NON-HARDWIRED / ANTI-VACUITY GUARD (bug-guard #1) — **SATISFIED**

The DEAD verdict is meaningful only if the forced-λ routine COULD return LIVE. My routine
takes `gradS` as a general argument (NOT specialized to 0). Independent inputs:

| input | gradS | A | constraint | `forced` | expected |
|-------|-------|---|-----------|----------|----------|
| LIVE #1 | `e_0` (≠0) | α (`e_0`) | none | **True** | True ✓ |
| LIVE #2 | `e_0` (≠0) | α (`e_0`) | fixed_Tr_face (`e_1+e_2`, non-absorbing) | **True** | True ✓ |
| FAITHFUL | `0` | α | fixed_Tr_face | **False** | False ✓ |
| ABSORBED | `e_0+e_1+e_2` ∥ ∇g | α | fixed_Tr (`∥`) | **False** | False ✓ |

⇒ the routine returns **forced=True for genuine off-faithful inputs** and **False at I/3**.
So LIVE is detectable in principle; the DEAD answer is a SUBSTANTIVE fact about I/3 being
the entropy maximum, NOT a rigged/vacuous pass. The gate does NOT collapse to the
first-law `δS=δ⟨K⟩` identity — it tests the SECOND term (the λA balance). **Non-vacuous.**

---

## 4. Gate 1 + remaining bug-guards

- **Gate 1 (PASS):** I/3 is the **fixed-trace** maximum of S_face. The single `0`
  Hessian eigenvalue is exactly the (β+γ) trace direction, removed by the fixed-Tr
  constraint ⇒ the restricted face Hessian is `{−9/2, −9×8}`, strictly negative ⇒ strict
  fixed-trace max. (Also confirmed: rank-1 face corner = scalar ⇒ `S≡0` at all orders ⇒
  the rank-2 face is the meaningful one.) PASS, carries zero evidence as pre-registered.
- **#2 λ-glaze (SATISFIED):** `∇Q_s=0` (independently) ⇒ `Q_s` family gives free λ ⇒
  recorded DEAD.
- **#3 TrX²=1/3 banned (SATISFIED):** independently `Tr2(I/3)=1/3` exact ⇒ imposing it
  pins precisely the faithful point and would trivialize the test; correctly absent from
  the constraint set. (∇Tr2 at I/3 `=⅔(e_0+e_1+e_2)`, also diagonal.)
- **#4 compress-then-normalize (SATISFIED):** I built both orders; the full-trace factor
  cancels under re-normalization (`r_B²−r_A²=0`, independent of α) ⇒ ordering does NOT
  manufacture spurious criticality. The pinned convention is sound.
- **#5 u-alignment:** N/A (single face, single point at I/3; no inter-face map).

---

## 5. PASS/FAIL SUMMARY

| item | status |
|------|--------|
| **Linchpin `∇S_face(I/3)=0` (all 27 dirs), independent method** | **PASS** |
| **Fisher spectrum `{0,−9/2,−9×8}`, independent** | **PASS** (exact match) |
| I/3 is the entropy MAX (Hessian ≤ 0) | PASS |
| **Exhaustive 16×4 no-forced-λ sweep → DEAD** | **PASS** (0/64 forced) |
| Obstruction first-order (det_3 Fisher curvature `−2/3` but never triggered) | PASS |
| **Non-hardwired / anti-vacuity guard (routine flags LIVE for genuine input)** | **PASS** (non-vacuous) |
| Gate 1 fixed-trace max + rank-1 triviality | PASS |
| Bug-guards #2 (λ-glaze), #3 (TrX²=1/3 banned), #4 (normalization order) | PASS |
| Source guards (no octonion_algebra, no numpy on decisive path, det_3 SSOT) | PASS |

**The DEAD-at-degree-≤3 verdict is INDEPENDENTLY SUPPORTED. [CONFIDENCE: HIGH].**

The verdict rests on three exact-over-Q facts, each reproduced here on an independent
path: (1) `∇S_face(I/3)=0` in all 27 directions (closed-form 2×2 corner expansion);
(2) all 16 candidate gradients are diagonal / `∇Q_s=0` (differentiated from the SSOT
`det_3`); (3) every one of the 64 criticality systems admits `(λ,μ)=(0,0)` (my own
forced-λ routine). The anti-vacuity guard confirms the routine would flag LIVE if the
geometry allowed it — so DEAD is substantive (I/3 is the entropy maximum, ∇S_face=0
necessarily), not a numerical near-miss or a rigged pass. No κ, no Λ, no `G=κT`.

**Scope (anti-overclaim, carried):** DEAD at degree ≤ 3 ≠ absolute DEAD (degree ≥ 4
invariants remain, with a naturalness penalty). The result is the fiber-side scope
theorem: the second/geometric Jacobson term provably does not live on the fiber at low
degree; the route stays gated on the base/format object.

**No discrepancy found. Verdict not overturned. Safe to ratify.**
