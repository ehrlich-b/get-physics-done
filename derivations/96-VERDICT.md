# Phase 96 / v36.0-candidate — VERDICT: the FIELD-FAITHFULNESS CLAMP gate

**Primary verdict: `DEAD-POINTWISE` at Gate 0 (the decisive gate). The clamp is FALSE; fork A is PROVEN.**

Driver: `code/faithfulness_clamp.py` (24/24 PASS, exit 0, exact over ℚ, no float in any verdict).
Commits: `8aadfe14` (scaffold + verdict ladder + anchors), `f5d6ee7d` (Gate 0 decisive),
`09202541` (Gate 0 circularity hardening). Reproduce: `python3 -u code/faithfulness_clamp.py`.

---

## §1 — Which taxonomy entry (the primary verdict)

**`DEAD-POINTWISE` (Gate 0; the skeptical prior, CONFIRMED concretely exact over ℚ on CP² —
NOT merely adopted).**

Field faithfulness `M(x) = φ[M](x)` on the curved variety carries **NO genuine local
base-derivative term**. The faithfulness operator `L_F = δ(faithfulness)/δM` is the pointwise
algebraic `−Tr(h²)`-type (state-space / Fisher–Bures) Hessian, plus at most a **nonlocal
rank-1 global-mean correction** — the decisive coefficient of any local Laplacian (`Δ_FS`)
term is **identically 0**. Therefore field faithfulness is structurally a **different TYPE**
from the curvature operator `δΓ` (the v33 `ε = λ_L − 2Λ = 20` Lichnerowicz tensor operator),
the clamp `δF/δM = 0 ⟺ δΓ/δM = 0` is **FALSE** (faithful ≠ Einstein-extremal), **fork A is
PROVEN**, and the 2026-06-07 "self-modeling is fiber-local" brainstorm is upgraded to a
**theorem** (self-modeling provably cannot reach the base metric).

Gates 1, 2, 3 are **NOT reached** — Gate 0 is decisive DEAD (the gates are run in order, STOP at
the first DEAD).

---

## §2 — The obstruction operator (exact)

Promote the matter state to a field `M(x)` on CP² = h₃(ℂ_u); linearize at a **structured
off-faithful** background `M̄ = s01` (Bug-guard 3 — the faithful I/3 point is matter-free,
doubly degenerate `0=0`), `M(x) = M̄ + ε h(x)`. The faithfulness operator is

```
L_F[h](x)  =  (pointwise algebraic Fisher/Bures Hessian)·h(x)   −   c · ⟨h⟩_ρ ,
              \__________ −Tr(h²)-type, the v35 corpse _________/      \__ nonlocal rank-1 __/

      with the LOCAL base-derivative (Lichnerowicz/Laplacian) coefficient  ≡ 0 .
```

- **Pointwise core** (the algebraic Fisher/Bures Hessian): from the F3 covariance differentiation
  `δ(⟨M²,p⟩ − ⟨M,p⟩²)`, equals `⟨{M̄,h},p⟩ − 2⟨M̄,p⟩⟨h,p⟩` — a matrix-algebraic field times `h(x)`,
  the **v35 DEAD-FISHER object** (`A_ii ≡ Var`, the quantum Fisher / QGT-real metric on states).
- **Nonlocal correction** `c·⟨h⟩_ρ`: the φ-map's only non-locality is the ensemble expectation
  `⟨·⟩_ρ`, which on a field is the global base integral `⟨h⟩ = ∫_{CP²} h dV_FS / Vol` — a **number**,
  a rank-1 projector onto the **constant mode**. Exact over ℚ: `⟨Y_λ⟩_FS = 0` for every nonconstant
  harmonic (the ensemble mean couples to the constant mode ONLY), and `Δ_FS(⟨h⟩) = 0` (a constant has
  no base derivative).

Neither piece carries the eigenvalue of a mode-carrier `Y(x)`: building `L_F` on the mode
`h(x) = h_dir·Y(x)` for `Y` a genuine `λ₂ = 32` harmonic and a `λ₁ = 12` harmonic gives the **same**
algebraic core (λ-INDEPENDENT) — the discriminant `L_F[h] ≠ (core)·Δ_FS Y` holds on **both** modes,
so the eigenvalue (−32 / −12) that a local Laplacian would inject is **absent**. Decisive coefficient
`= 0` (exact over ℚ).

---

## §3 — Bug-guard dispositions (all checked before the DEAD call)

| # | Bug-guard | Disposition |
|---|-----------|-------------|
| 1 | **DIRICHLET-TRAP** (a base-derivative that is the harmonic-map scalar `□φ_M`, the WRONG TYPE) | **N/A but pre-empted.** No local derivative exists natively; an IMPORTED kernel would give the scalar `□φ_M` (verified `□φ_M = −12 φ_M`, a scalar eigenvalue equation), NOT the `ε=20` Lichnerowicz TENSOR operator — so even the import route routes to DEAD-WRONG-DERIVATIVE, never ALIVE. |
| 2 | **IMPORTED-KERNEL** (a derivative appearing only after an inserted smoothing kernel) | **FIRES (the kill route).** A local `Δ_FS` term appears only with an inserted kernel of second moment `σ²`, coefficient `½σ²`; the φ-iteration's native `⟨·⟩` is the FLAT global average `K = 1/Vol` (localized second moment 0), so `σ² → 0` and the coefficient `→ 0`. Any nonzero local derivative is **smuggled, not forced** ⟹ collapse. |
| 3 | **FAITHFUL-POINT-MATTER-FREE** (the faithful I/3 point is matter-free; naive linearization gives `0=0`) | **SATISFIED.** Linearized at a structured off-faithful `M̄ = s01 ≠ I/3`; the algebraic core is non-vacuous (nonzero); `G_M`/`Var` genuinely vary over the s9 ground points. Not the v23 death. |
| 4 | **WOO / DEMON-TEST 2.0** (no thermodynamics / horizons / coarse-graining / ensemble entropy) | **PASSED (AST-guarded).** The Gate-0 code contains no thermo/horizon/ensemble-entropy token; the φ-map's `⟨·⟩` is a SELF-CONSISTENCY mean over the state's own distribution, not a thermal ensemble. The source guard FIRES on an injected violation (proven not a no-op). |
| 5 | **NO-CIRCULARITY** (compute `L_F` from the φ-fixed-point ALONE; no `R`/`Ric`/`G`/`Δ_L`) | **PASSED (AST-guarded).** The Gate-0 decisive functions contain no `R`/`Ricci`/`Riemann`/`Einstein`/`Lichnerowicz`/`tensor_probe` token in their code; `L_F` is built from `φ_M = ⟨M,p⟩` and the F2/F3 variance/covariance structure alone. The metric-action comparison is deferred to Gate 2 (not reached). Guard FIRES on injection. |

**Plus the deepest concern (RESEARCH §9 "honest reading") — closed.** AST-parsing the actual
φ-iteration reference confirms the faithful-`ρ_J` branches F2/F3 reference the measure `ρ` in
**exactly one place** — `expectations(points, ρ) = ⟨l_i⟩_ρ` — with every other term pointwise in
the current state. So the state-side condition has **no independent base-derivative channel**: the
inherited-derivative worry (that this is the metric-side loop in disguise) is structurally refuted.

---

## §4 — FENCES (binding, verbatim from RESEARCH §6)

NO Einstein / `G=κT` / gravity / Newton / dark-matter / geodesic language as a DERIVED result; the
bits↔area / induced-`G` rate is a framework ratio, NOT Newton's G; FS is USED, not derived;
signature Riemannian (**Wall 2 unpaid** — NOTHING is called gravity until signature is paid);
DEAD-\* and ALIVE-\* are NOT derivations of gravity. ALIVE is **necessary-not-sufficient** for
gravity (Jaksland arXiv:2005.05055) — it sits UPSTREAM of the state-fp⟹metric-fp clamp, which
itself sits upstream of Wall 2. Does NOT retract v33 (extremize), v34 (induce), v17–v21 (fiber
kills), v23 (I/3 death), v35 (DEAD-FISHER). Paper 5 remains the only result in the
more-than-nothing column.

---

## §5 — Anti-overclaim

- `DEAD-POINTWISE` is the **expected, honest** outcome (the skeptical prior); it is **theorem-grade
  and governance-compliant either way**. It **closes** the faithfulness-clamp route and is the
  **green light for fork A**.
- This is a **no-go on the CLAMP**, not a claim about gravity. It says: the self-modeling-faithful
  profile is **not** forced to extremize the gravitational action its fluctuations induce, because
  the state-side faithfulness condition lacks the base-derivative structure that the curvature-side
  `δΓ` has. It does **not** assert anything about whether gravity exists, only that *this bridge*
  (state-fp ⟹ metric-fp) is **false on the variety**.
- The decisive object is the **coefficient of the local base-derivative term in `L_F`**, computed
  from the φ-fixed-point ALONE; it is `≡ 0` exact over ℚ on CP². This is a structural/at-points
  determination, not a heavy symbolic claim.
- We did **not** re-derive any of the three dead handles (entropy/MaxEnt-as-F; fixed-point-scale
  `κ_ind`; static/pointwise `ρ_J`). `L_F` is the **geometry-respecting** field extension, the
  non-trivial object — and it still collapses.
- The collapse mechanism is **specific and exact**: `⟨Y_λ⟩_FS = 0` (the ensemble mean is a global
  integral that annihilates every nonconstant harmonic), so the only non-locality is a rank-1
  constant-mode projector with zero base-derivative — there is no native local Laplacian to match
  the `ε=20` Lichnerowicz mode.

---

## §6 — The Deliverable items (one sentence each)

- **Gate it died at / the decisive number (the form of `L_F`):** Gate 0 — `DEAD-POINTWISE`;
  `L_F = (pointwise −Tr(h²)/Fisher–Bures Hessian) − c·⟨h⟩_ρ`, with the local base-derivative
  (Lichnerowicz/`Δ_FS`) coefficient **identically 0** exact over ℚ on CP².
- **The explicit `F` (Gate 1):** not written — Gate 0 is decisive DEAD, so Gates 1–3 are not reached.
- **`δF=0` vs `δΓ=0` (Gate 2):** not run — but the reason is recorded: `L_F` is a state-space
  algebraic/nonlocal operator (wrong TYPE) while `δΓ` is a local 2nd-order Lichnerowicz operator
  (the `ε=20` tensor mode), so their critical points cannot generically coincide.
- **`κ_ind` status (Gate 3):** not run — `κ_ind` remains FREE (v34's framework ratio), unpinned;
  the clamp that could have pinned it is refuted upstream.
- **The clamp:** `state-fp ⟹ metric-fp` is **FALSE** on the variety — the faithful profile does not
  carry the base-derivative structure required to extremize the induced gravitational action, so
  it is not forced to be Einstein-extremal.
- **The selection-law ledger:** every metric-selection kind is now closed
  (v17 NONE / v18 fp-imported-action / v19 fp-no-intrinsic-orientation / v20 fp-imported-action /
  v21 DEAD induced-Einstein / **v36 DEAD-POINTWISE faithfulness clamp**), so the §6 ledger fork is
  forced — "gravity is separate" (incomplete-TOE), not a failed program.
- **The 06-06↔06-07 tension:** 2026-06-06 killed the pointwise/scale/`ρ_J` handles **on the fiber**
  (the uninteresting collapse), and 2026-06-07's "self-modeling is fiber-local" brainstorm bet the
  same on the **variety** but argued only structurally — Gate 0 resolves the tension by computing
  exact over ℚ that the variety's geometry-respecting field extension **also** collapses (the
  `⟨·⟩_ρ` is an intrinsically global state-space mean, never a local FS-neighborhood average), so
  06-07 is upgraded from intuition to **theorem**.

---

## §7 — Through-line consequence

v24 → v25 → v26 → v27 → v28 → v29/v30 → v31 (tensor wall OPENS) → v32 (dictionary κ=1/30, ε=20) →
v33 EXTREMIZE forces nothing → v34 INDUCE CLOSES-CONDITIONAL (gravity gap = the single
state-fp⟹metric-fp clamp) → v35 AREA-PER-BIT DEAD-FISHER → **v36 FAITHFULNESS CLAMP DEAD-POINTWISE:
the STATE-side `F` carries NO base-derivative the clamp needs.** Every gravity angle pointed at this
one operator `L_F`; it is the pointwise Fisher Hessian plus a nonlocal global-mean, never the
`ε=20` Lichnerowicz operator. The clamp is **refuted** — fork A is proven; Paper 6 v2 ships as a
genuine no-go (self-modeling provably forces QM but not gravity).
