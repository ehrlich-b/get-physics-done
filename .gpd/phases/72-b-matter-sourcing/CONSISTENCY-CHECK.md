# Cross-Phase Consistency Check — Phase 72 (B — Matter-Sourcing, matter-on-flat)

**Mode:** rapid (post-phase)
**Checked:** 2026-06-01
**Scope:** Phase 72 (plans 72-01, 72-02) vs full conventions ledger + Phases 70.1, 71
**Verdict:** **CONSISTENT** (status: completed) with **2 non-blocking WARNINGS** (known notation-coordinator follow-up — stale prose in CONVENTIONS.md §6 / ROADMAP VALD-04, NOT a blocker)

---

## Summary

Phase 72's decisive results are internally consistent and consistent with the full
conventions ledger and with the human-ratified Phase-70.1 reframe. **Every load-bearing
cross-phase test value was independently reproduced exact-over-Q by re-running the engine
(`code/bulk_geometry_verification.py`).** The two findings are both the SAME pre-known
non-blocking issue: stale "center is Einstein, Λ<0" prose in CONVENTIONS.md §6 and
ROADMAP VALD-04/CALC-05 that was falsified by Phase 70.1. The machine-readable
`state.json` convention_lock is clean; Phase 72's own artifacts explicitly reject the
falsified framing (`fp-lambda-as-sourcing`).

---

## Test-Value Verification (re-ran the engine — all exact over Q)

| # | Claim (from SUMMARY) | Reproduced value | Match |
|---|---|---|---|
| 1 | `bulk det_3` == `ring_lemma` SSOT (certified F_4-invariant) | det_3 identical on e_4-content octonions | ✅ |
| 2 | cross-term order `2Re((x2 x1)x3)` is load-bearing (≠ buggy `(x1 x2)x3`) | 2Re difference = 4 ≠ 0 | ✅ |
| 3 | cone-Hessian SOURCE anchor R(center) = −3 (Phase-71 regression) | R = −3 exactly | ✅ |
| 4a | M=0 spacetime baseline FLAT (B1 h≡0 ⇒ R[g]=0), DERIVED | h = 0₄ₓ₄, R = 0 | ✅ |
| 4b | eta_bg = [[0,½,0,0],[½,0,0,0],[0,0,−1,0],[0,0,0,−1]], sig (1,3) | eigval signs {+,−,−,−} | ✅ |
| 4c | g(M=0) = eta_bg exactly (construction-(ii) bridge gate) | g−eta = 0₄ₓ₄ | ✅ |
| 5 | H³ benchmark: round K=−1 target; cone-Hessian slice K=−½ | h3_constant_curvature → (R=−6, K=−1) | ✅ |
| 6 | DECISIVE off-switch: R_full ~ 4007.98, R_off ~ 246.66, ~93.8% drop | R_full=4007.981, R_off=246.66, 1−ratio=0.93846 | ✅ |
| 6 | both g_full and g_off signature (1,3) | (1,3,0) and (1,3,0) | ✅ |
| 7 | ‖M‖→0 limit: R ~ a_4 t⁴, a_4 = 395268903/24010000 ~ 16.46 | R/t⁴ → 16.46 (20.0,18.1,17.1↓); R/t²→0; R/t⁵↑ | ✅ |
| 8 | h⁽¹⁾ = 0 (⇒ Phase 73 is a quadratic-response test) | dh/dt\|₀ = 0₄ₓ₄ | ✅ |

**All 11 spot-checks PASS exact over Q.** The headline 72-02 numbers (R_full/R_off,
93.8%, signatures) and the Phase-73 handoff (h⁽¹⁾=0, k=4 leading power) reproduce on a
fresh run.

---

## 1. Convention Compliance (current phase vs FULL ledger)

| Convention (state.json / CONVENTIONS.md) | Relevant? | Compliant in Ph72? | Evidence |
|---|---|---|---|
| **metric_signature** mostly-minus (−,+,+,+) on slice | Yes | ✅ | eta_bg eigenvalue signs {+,−,−,−} = sig (1,3); both SUMMARYs state "mostly-minus"; g_full/g_off sig (1,3) reproduced. Timelike x₀=β+γ (the +½ eigenvector of the null-aligned (β,γ) block). |
| **det_3 cross-term** `2Re((x2 x1)x3)` (Phase-64.1 fix; octonion_algebra.py BANNED) | Yes (CORE) | ✅ | TEST1: bulk det_3 == ring_lemma SSOT. TEST2: order is load-bearing. det_block off-switch drops exactly the triple (self-norms retained). SSOT guard green per SUMMARY. |
| **potential −log det₃** / cone metric Hess(−log det) | Yes | ✅ | spacetime_curvature_of_g uses the same norm in source Hessian, B1 reference, AND difference cubic C (changes exactly one thing in ON/OFF). |
| **Totaro curvature** R_ijkl = −¼ g^{pq}(C_jlp C_ikq − C_ilp C_jkq), indices raised g⁻¹=(eta+h)⁻¹ | Yes | ✅ | 72-01 cross-checked Totaro vs hand-rolled Levi-Civita exact over Q on R_0202/R_2323/R_0101; index-raising non-vacuity (g⁻¹ ≠ H_bg⁻¹) asserted. |
| **Riemann/Ricci sign** pinned negative; H³ K=−1 (round), cone-Hessian K=−½ | Yes | ✅ | TEST5: h3_constant_curvature → K=−1; R(center)=−3 (TEST3). 72-01 documents the hand-rolled global sign flip reconciled to the engine's pinned Totaro convention (uniform −1 on 9 components = single global convention flip, not a bug). |
| **natural units** ħ=c=k_B=1; **EXACT over Q** | Yes | ✅ | Both SUMMARYs; all reproduced quantities exact rationals; signatures via real_roots(charpoly), no float on decisive path. |
| **construction-(ii) bridge** g=eta+h, enforce g(center,M=0)=eta EXACTLY | Yes (CORE) | ✅ | TEST4c: g(M=0)=eta_bg exactly. B1 h≡0 at M=0. |
| Jordan product, octonion Fano e1e2=e4, u=e7, Peirce V_1/V_{1/2}/V_0 | Yes | ✅ | Engine inherits SSOT layout; V_{1/2}={11..26} matter channel, V_0 x1 partner, consistent with CONVENTIONS §3. |
| Fourier / gauge / regularization / renormalization / time-ordering / creation-annihilation | No | N/A | Pure differential geometry on the cone — no field theory, no second quantization (state.json marks these "N/A"). |

**18 canonical types:** the 8 field-theory types are correctly N/A (pure algebra/geometry).
The geometry-relevant types (metric_signature, coordinate_system, index_positioning) and
the custom det₃/Jordan/octonion conventions are all compliant.

---

## 2. Provides/Consumes Verification (semantic)

### 72-01 → 72-02 (intra-phase)
- **`spacetime_curvature_of_g` engine (B1, validated):** 72-02 reuses it for the ON/OFF
  off-switch + ‖M‖→0 series. Same B1 h, same index-raising g⁻¹=(eta+h)⁻¹. ✅ Consistent
  (reproduced R_full/R_off on this engine).
- **Flat M=0 baseline (R=S=Weyl=0):** consumed verbatim as the matter-on-flat reference. ✅

### 70.1 → 72 (the load-bearing reframe)
- **"g=eta+h is the physical metric; M=0 flat DERIVED from KKT det₂; cone-Hessian=SOURCE":**
  72-01/72-02 implement this verbatim. **Semantic check:** R(center)=−3 / {0,−1,−1,−1} /
  R_time×H³ is consistently labeled the **cone-Hessian SOURCE field's geometry**, NEVER the
  spacetime curvature, in both SUMMARYs, the .tex, AND the engine docstrings. ✅ This is the
  precise distinction the task flagged to watch — it is maintained correctly throughout.
- **No Λ tripwire:** the M=0 limit is the trivial flat point (h≡0), explicitly NOT a Λ/R=−3
  subtraction. `fp-lambda-as-sourcing` rejected in both plans. ✅

### 71 → 72
- **Totaro engine + SOURCE regression anchors (R(center)=−3):** reproduced exact over Q
  (TEST3). 72-01 also reproduces R{4:1/3}=−73041507/21967969 etc. per SUMMARY. ✅

### 72 → 73 (downstream handoff — highest cascade risk)
- **h⁽¹⁾=0, h⁽²⁾ (4×4 exact), a_4=395268903/24010000:** h⁽¹⁾=0 reproduced (TEST8); a_4 limit
  reproduced (TEST7). The handoff correctly determines Phase 73 must be a **quadratic-response**
  (h⁽²⁾) linearized-Einstein test, not linear. ✅ Consistent and well-specified.

---

## 3. Cross-Phase Error-Pattern Scan

| Pattern | Found? | Note |
|---|---|---|
| Sign absorbed into redefinition | No | Hand-rolled Riemann sign flip diagnosed (uniform −1 = global convention) and reconciled to engine's pinned Totaro form BEFORE the cross-check; not silently absorbed. |
| Normalization change | No | det₃ SSOT byte-identical across engines; polarization d=6·det untouched. |
| Implicit assumption violated | No | Small-‖M‖ Lorentzian regime declared in the plan's `approximations`; large-M signature flip to (0,4) recorded as the documented perturbative boundary, not used on the verdict. |
| Coupling/factor mismatch | No | Cross-term factor `2Re((x2 x1)x3)` consistent; off-switch drops exactly that triple. |
| Index-raising error (g⁻¹ vs H_bg⁻¹) | No | Non-vacuity asserted (g⁻¹-raised R ≠ H_bg⁻¹-raised R); the latent docstring bug at offcenter_slice_metric is fully annotated SUPERSEDED/FALSIFIED and is NOT on the decisive path. |

---

## 4. Findings (both NON-BLOCKING — pre-known notation-coordinator follow-up)

### WARNING-1 (non-blocking): CONVENTIONS.md §6 stale falsified text
- **Location:** `.gpd/CONVENTIONS.md` line 112:
  > "`Lambda ≠ 0`: the center is Einstein with **negative** Ricci (Cartan), so `Lambda < 0`
  > (background Einstein-negative)."
- **Why falsified:** Phase 70.1 proved the cone-Hessian center is NOT Einstein (Ricci-endo
  eigenvalues {0,−1,−1,−1}, not all −3/4), AND the cone-Hessian is not the spacetime metric.
  Phase 72 uses a flat-DERIVED M=0 baseline (h≡0 ⇒ R=0), no Λ.
- **Why non-blocking:** Exactly the follow-up already recorded in STATE.md / ROADMAP / project
  memory. The machine-readable `state.json` convention_lock is CLEAN (no "center is Einstein"
  assertion). Phase 72's artifacts explicitly reject this (`fp-lambda-as-sourcing` rejected in
  both 72-01 and 72-02). Per task instruction: treat as WARNING, not INCONSISTENT.
- **Fix (notation-coordinator):** rewrite §6 row to "the cone-Hessian SOURCE center is
  non-Einstein {0,−1,−1,−1}; the spacetime M=0 vacuum is flat η (DERIVED from KKT det₂), no Λ.
  κ/Λ to be re-examined at Phase 73 as a genuine can-fail test."

### WARNING-2 (non-blocking): ROADMAP VALD-04 criterion #2 / CALC-05 stale text
- **Location:** `.gpd/ROADMAP.md` line 166 ("the irreducible symmetric space is Einstein with
  NEGATIVE Lambda (Cartan)") and line 192 (CALC-05: "`Lambda` is fitted NONZERO ... do NOT set
  Lambda = 0").
- **Same root cause** as WARNING-1; same non-blocking status. (ROADMAP line 66 already carries
  the 70.1 SUPERSEDES note, so the document is self-aware of the contradiction.)
- **Fix:** align VALD-04 #2 / CALC-05 with the flat-DERIVED-η baseline; Λ is no longer asserted
  nonzero a priori.

### INFO (not a defect): ROADMAP "off-switch kills it" vs ratified "changes decisively"
- ROADMAP line 177 phrases the SURVIVES criterion as "off-switch **kills** it"; 72-02
  human-ratified the weaker "changes decisively (~93.8% reduction, not a total kill)" reading,
  with the ~6% V_{1/2} self-norm residual recorded at true strength. This is a documented,
  human-ratified `competing_explanations` entry in the 72-02 SUMMARY — a transparent reading
  choice, not a hidden inconsistency. No action required (optionally tighten ROADMAP wording).

---

## Conclusion

**CONSISTENT.** Phase 72 faithfully implements the Phase-70.1 reframe (g=eta+h physical
metric; cone-Hessian = SOURCE; M=0 flat DERIVED, no Λ tripwire), preserves the det₃ SSOT
cross-term order `2Re((x2 x1)x3)`, maintains mostly-minus signature (1,3) throughout, and
pins the Riemann/Ricci sign consistently with Phase 71's H³ benchmark. All decisive numbers
reproduce exact over Q. The only issues are two instances of one pre-known stale-prose item
(CONVENTIONS §6 / ROADMAP VALD-04) already on the notation-coordinator's queue — non-blocking
WARNINGS, not consistency violations. Phase 73 greenlight is sound; the h⁽¹⁾=0 / quadratic-
response handoff is correctly specified.

_Checker: gpd-consistency-checker (rapid mode)_
