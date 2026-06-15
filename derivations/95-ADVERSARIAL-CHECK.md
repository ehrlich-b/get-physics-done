# Phase 95 / v35.0 — AREA-PER-BIT KILL-TEST — ADVERSARIAL CHECK (bug-guard #1, AREA-RIG)

> Adversarial path. Driver: `code/adv_area_rig_95.py` (point-first, exact over ℚ; reuses the
> certified `tensor_probe.py` + `lichnerowicz_response.py` engines). All values exact rational at
> 5 ℚ-points {P0(ρ=8), P2(ρ=15), P3(ρ=49/36), P4(ρ=126/25), P5(ρ=4)} × {s01, a01, d1, gen}.
> NO brute symbolic `simplify`/`cancel` over a generic multi-parameter M (resource rule honored —
> point evaluation only). No commits, no state edits.

## VERDICT OF THE ADVERSARIAL CHECK: **DEAD-FISHER ROBUST — fork A green-lit. HIGH confidence.**

I attacked the verdict at its single soft point: the executor took candidate (ii) to be the metric
**TRACE** of `dφ_M⊗dφ_M` (trivially `= Var → Fisher → DEAD`) and asserted (Fence/VERDICT line 62–64)
that the TT part "is structurally precluded" because the trace channel carries the scalar part only.
The prompt's mandate was to test the **non-trace** readings the executor skipped — the TT-projected
mode contracted into an area, and the genuinely symplectic area — as FS-canonical, matter-functorial
areas. **All of them collapse to functions of the Fisher variance `Var`.** The attack did not flip the
verdict; it tightened it. The decisive new fact:

> **The traceless ("TT") area density of the v31 metric mode is `A_TT = 3·Var²` — exactly, at every
> chart point, every matter direction.** It is a pure monomial in the quantum Fisher variance. There
> is no independent geometric structure hiding in the traceless part. `R_TT = A_TT/|G_M| = 3Var²/|G_M|`
> shears, but the shear is again Fisher-vs-relative-entropy (state-space), NOT a geometric rate.

This is a *stronger* DEAD-FISHER closure than the verdict's: the verdict argued the TT channel is
"precluded by construction"; the adversarial computation shows the TT channel is *present but is
itself a power of the Fisher object*. The Fisher corpse is even more inescapable than claimed.

---

## CANDIDATE (ii)-TT — the transverse-traceless metric-mode area

**Object.** `A_TT(p,M) = ‖h₀‖²_g`, where `h₀ = (dφ_M⊗dφ_M) − ¼ tr_g(dφ_M⊗dφ_M)·g` is the LOCAL,
FS-canonical, matter-functorial traceless part of the v31 metric mode `B3 = dφ_M⊗dφ_M`. This is the
**local** analogue of v31's GLOBAL `‖TT(B3)‖²_{L²} = (1/30)(TrM²)²`. It is a genuine non-Fisher
candidate: it is built from the **traceless** part, NOT the metric trace `= Var`.

**Exact algebraic structure (the kill), universal over all 12 (dir × point) samples, g_pot/Fisher norm:**

| channel | closed form (exact, all points/dirs) | reduces to |
|---|---|---|
| `A_ii = g^{ab̄}∂_aφ ∂_b̄φ` (executor's candidate ii) | **`= Var`** | Fisher (verdict ✓) |
| `tr_g(dφ⊗dφ) = 2 g^{ab̄}∂φ∂φ` (real trace) | **`= 2·Var`** | Fisher |
| `A_full = ‖dφ⊗dφ‖²_g` (full tensor norm) | **`= 4·Var²`** | Fisher² |
| `A_TT = ‖traceless part‖²_g` | **`= 3·Var²`** | **Fisher²** |

These four ratios (`A_ii/Var = 1`, `tr/Var = 2`, `A_full/Var² = 4`, `A_TT/Var² = 3`) are **constant to
the last digit at every one of the 12 samples** (see driver Probe 1). The relation is the rank-1
identity: `dφ⊗dφ` is `s⊗s` for the gradient `s` with `|s|²_g = Var`, so `‖s⊗s‖² = (|s|²)² = Var²` per
holomorphic pairing (giving `A_full = 4Var²` with the real (1,1)+(2,0)+(0,2) bookkeeping), real trace
`= 2Var`, and `A_TT = A_full − (tr²)/(2·n) = 4Var² − (2Var)²/4 = 3Var²` (n=4 real dims). **Pure Fisher.**

**Sample R_TT values (g_pot), showing it SHEARS but only via the Fisher/rel-entropy split:**

| M | pt | A_TT = 3Var² | G_M | R_TT = A_TT/\|G_M\| |
|---|----|------|-----|---------|
| s01 | P0 | 363/256 | −17/64 | 363/68 |
| s01 | P5 | 3/4 | −1/2 | 3/2 |
| d1 | P0 | 3/4 | −5/16 | 12/5 |
| d1 | P5 | 3/4 | −1/2 | 3/2 |
| gen | P0 | 2187/256 | −81/64 | 27/4 |
| gen | P5 | 243/16 | −9/16 | 27 |

R_TT has 17 distinct values across the 17 finite samples (in BOTH g_pot and g_phys=½g_pot norms —
the shear is **scale-independent**, as G1 requires). But `R_TT = 3Var²/|Var + ¾⟨M⟩² − ½TrM²|` — the
numerator is the **Fisher information squared**, the denominator is the **relative-entropy Hessian**.
The shear is the *same* state-space disagreement that drives the verdict's `R = Var/|G_M|`, now squared
in the numerator. It is **not** a geometric bits↔area exchange rate.

**Disposition: A_TT COLLAPSES to Fisher (= 3·Var²). It is NOT independent geometric structure.**
Probe 3 reports `A_TT/G_M` varies — but that is the trivial non-proportionality of `Var²` to
`Var + ¾⟨M⟩² − ½TrM²`, i.e. the *same* Fisher-vs-rel-entropy fact, not an independent geometric area.
**Does NOT carry an independent v31 TT(B3) structure** in the rate sense: `A_TT = 3Var²` is a function
of the *scalar* `Var`, so it cannot encode the rank-2 `(TrM²)²` direction-content as an *independent*
area — the local norm of the TT part is forced to be `3Var²` pointwise. (Consistency note: v31's GLOBAL
`‖TT(B3)‖²_{L²} = (1/30)(TrM²)²` is the L²-integral of a *different* object — the **L²-orthogonal** York
TT residue `r`, which is nonlocal — not the integral of the pointwise `A_TT = 3Var²`. Both are real; they
are different projections. Neither yields a geometric rate: the global one is a fixed number per M, the
local one is `3Var²`.)

**Relation to v31's LIVE record (does NOT flip the verdict, clarified for the verifier).** `extract_tt(B3)`
produces a **nonzero TT residue** `r` for s01, d1, gen (its (1,1) block `r11 ≠ 0`, confirmed in the driver
STEP 0) — this is exactly v31's ratified LIVE object. (`info['consistent']` is the CRT-solvability flag of
the York *particular solution*, not a "B3 is pure gauge" verdict; the LIVE content is the nonzero TT residue
`r` with `tr_r = 0`, `div_r = 0`.) The point of THIS adversarial check is orthogonal: the v31 LIVE object is
the certified **L²-orthogonal residue norm** `‖TT(B3)‖²_{L²} = (1/30)(TrM²)²` — a single number per M, a
GLOBAL object. The *area-per-bit* question instead needs a **local area density** `A_TT(p,M)`, and the
FS-canonical local traceless norm is `‖h₀‖²_g = 3·Var²` pointwise — a power of the Fisher variance. Both are
correct and BOTH are DEAD for a geometric rate: the global one is a fixed `(TrM²)²` per M (no p-rate), the
local one is `3Var²` (Fisher). v31 LIVE (a tensor MODE *exists*) and v35 DEAD-FISHER (the canonical *area*
is the Fisher object) are consistent — the anti-overclaim already says a mode existing is necessary-not-
sufficient. No contradiction with v31.

---

## CANDIDATE (iii) — the genuinely SYMPLECTIC (Kähler 2-form / moment-map) area

**(iii-a) gradient-norm symplectic area `|grad φ_M|²_g`.** Collapses: `= Var` exactly (ratio **1** in
g_pot at all 9 samples). This is the Kähler tie the verdict already covers — `J` is a g-isometry so the
Hamiltonian-field norm equals the gradient norm = Var. CONFIRMED COLLAPSE.

**(iii-b) Poisson bracket `{φ_M, φ_a01} = i g^{ab̄}(∂_aφ_M ∂_b̄φ_{a01} − ∂_aφ_{a01} ∂_b̄φ_M)`.** A genuine
symplectic pairing of two moment-map components. Exact values: s01@P0 = 1, s01@P3 = −54/49, d1@P0 = 1/2,
d1@P3 = 72/49, gen@P0 = gen@P3 = **0**. This is the **structure-constant / Lie-bracket pairing of two
su(3) moments** (a state-space, representation-theoretic object), not an independent geometric area; it
vanishes identically for `gen` (which commutes with a01 in the relevant block). State-space, not geometry.

**(iii-c) orbit 2-form magnitude `|dφ_M ∧ dφ_a01|²_g`.** As literally built (`g^{ca̅}g^{bd̄} W_{ab̄}
conj(W)_{cd̄}` with `W` the (1,1) commutator block) this is NOT a clean FS-canonical 2-form norm — it
mixes index pairings and is NOT a multiple of the natural Gram determinant `Var(M)Var(a01) − |⟨grad M,
grad a01⟩|²` (the wedge/Gram ratio varies: 74/5, 473/16, 2, 4, 802/9, 2, 0). **I do not count (iii-c) as
a flip:** its variation is an artifact of an ill-defined 2-form contraction, not a genuine independent
geometric area. The two well-defined symplectic readings — (iii-a) gradient norm and (iii-b) Poisson
bracket — are both state-space; there is no third independent FS-canonical symplectic-area reading
(the Kähler symplectic form on a single moment IS the gradient norm = Var; on two moments IS the
Poisson bracket). SYMPLECTIC ROUTE: no independent geometric rate. DEAD.

---

## OTHER AREA-RIG ANGLES MOUNTED

- **Full tensor norm `‖dφ⊗dφ‖²_g = 4Var²`** — Fisher² (above). DEAD.
- **Metric-mode determinant / rank-1 structure** — `dφ⊗dφ` is rank-1 (`s⊗s`), so all its symmetric-
  tensor invariants (norm, traceless norm, trace) are powers of the single scalar `|s|²_g = Var`. There
  is structurally no second independent invariant at this order. The only deg-4 SU(3) invariant for
  traceless 3×3 is `(TrM²)²` (Cayley–Hamilton; v31/RESEARCH §1) — and the *global* norm lands exactly
  there `(1/30)(TrM²)²`, a fixed number per M, not a p-varying rate.

---

## THE VERDICT FORK (reported honestly per the prompt's three-way rule)

- ☑ **All collapse to Fisher / R-shear-is-state-space → DEAD-FISHER ROBUST → HIGH seal, fork A green-lit.**
- ☐ LIVE-TENSOR flip — **NOT triggered.** The TT-projected area is `3Var²`, a Fisher monomial, not an
  independent shearing tensor rate. The genuinely symplectic areas are gradient-norm (= Var) or
  Poisson-bracket (state-space structure constants). No FS-canonical, matter-functorial AREA stays
  independent of `G_M` *as a geometric object* — every one is a power/pairing of the QGT/Fisher metric.
- ☐ INCONCLUSIVE (verdict flips between defs) — **NOT triggered.** All FS-canonical area definitions
  (trace, full norm, TT norm, gradient symplectic norm) reduce to `{Var, Var², 2Var, 3Var², 4Var²}` —
  all the *same* Fisher object up to a numerical constant. No flip.

**I did NOT find a flip. The DEAD-FISHER / fork-A verdict survives the AREA-RIG attack, and is in fact
strengthened:** the variety's canonical area is not merely *equal to* the Fisher metric in the trace
channel — *every* FS-canonical area invariant of the matter-induced metric mode (trace, traceless, full,
symplectic) is a fixed power of the quantum Fisher variance `Var`. There is no native geometric area on
the variety independent of the state-space information geometry. The bits↔area rate is a contingent
import. **Fork A.**

### Confidence: HIGH (computational), HIGH (interpretive for this attack).
The `A_TT = 3Var²`, `A_full = 4Var²`, `A_ii = Var`, `tr = 2Var` identities are exact over ℚ, reproduced
at 12 (dir × point) samples in two metric normalizations, and follow from the rank-1 `s⊗s` structure with
`|s|²_g = Var`. The single interpretive step ("a Fisher-power area cannot be a geometric rate") is the
verdict's own pre-registered Fence 3 / Bug-guard 3, now satisfied through the *strongest* reading
(traceless channel) rather than the trace channel — which removes precisely the loophole the prompt
worried about. The §9 ground truth (8/5, 2/13, 44/17, 4/3) reproduced exactly.

### Note for the orchestrator / verifier
- The local pointwise `A_TT = 3Var²` (this check) and the global `‖TT(B3)‖²_{L²} = (1/30)(TrM²)²` (v31,
  ratified) are *different projections* of `dφ⊗dφ` and are BOTH correct — do not read them as a
  contradiction. The area-per-bit question is about a *local area density*, which is the `3Var²` (Fisher)
  reading; that is the one that decides this milestone, and it is DEAD-FISHER.
- `extract_tt(B3)` yields a NONZERO TT residue `r` (r11 ≠ 0) for s01/d1/gen — v31's LIVE object is intact
  and NOT contradicted. (`info['consistent']` is the CRT-solvability flag of the particular solution, not a
  pure-gauge verdict.) The adversarial result is about the *local area density* `‖h₀‖²_g = 3Var²`, a
  different (pointwise) projection than v31's GLOBAL residue *norm identity* `(1/30)(TrM²)²`. Both DEAD for
  a geometric rate; mutually consistent.
