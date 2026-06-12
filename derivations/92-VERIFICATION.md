# Phase 92 (v32.0-candidate) — INDEPENDENT VERIFICATION (gpd-verifier)

**Verdict-vs-executor: INCONSISTENT (one load-bearing number REFUTED, one CORRECTED/RE-LABELED, one
CONFIRMED). Overall confidence: HIGH.** The verdict CENTER (ε) and the verdict's NORM identity both
rest on a single mis-step: the executor reads every (1,1)-sector quantity off `r[1]`, the (1,1) block
of the divergence-coupled York residue, which is **NOT** a transverse (1,1) tensor and **NOT** the
genuine Boucetta λ=12 (1,1) eigentensor. The independent re-derivation, the executor's own machinery
fed cleaner inputs, AND the Boucetta paper (fetched, same convention) all point the same way.

Verifier code: `code/lichnerowicz_response_verify.py` (independent geometry, general-ω York solve, own
Riemann + covariant calculus + Lichnerowicz, own FS L² integral). Exact over Q. sympy 1.14.0.

---

## TL;DR — the three load-bearing numbers

| # | Claim | Verdict | Independent value |
|---|---|---|---|
| **A/iii** | **ε = λ_L − 2Λ = 32 − 12 = 20** | **REFUTED** | **ε = 0** (Boucetta (1,1) TT λ_L = **12**; the executor's 32 is the **(2,0)/(0,2)** eigenvalue) |
| **A/ii** | **‖TT(B3)‖² = (1/54)(TrM²)²** | **CONFIRMED-BUT-MISLABELED → CORRECTED** | κ=1/54 is the **(1,1)-block** norm; the genuine **full TT mode** norm is **κ_full = 1/30** (also forced, detM-absent) |
| **A/ii** | **detM ABSENT** | **CONFIRMED** | detM absent in the (1,1) (1/54), anti (2/135), AND full (1/30) norm |

Plus the direction sub-claim and the integrity checks (all consistent with the executor): see below.

---

## What I reproduced (PRIORITY C — integrity, all PASS)

Byte-for-byte reproduction of the executor driver `code/lichnerowicz_response.py`:

- **Gate 0: 6/6 PASS** (Ric=6g Einstein, Kähler Riemann contracts to Ricci=6g, rough-Laplacian sign
  pin λ₁=12/λ₂=32, all 8 generator residues tr_g=0 ∧ div=0, single-generator Gram **rank 6**,
  generic-M {N(M)} **rank 8**, Δ_L^{(1,1)} eigentensor). Gram values reproduced
  (`Gram[s01,s01]=Gram[d1,d1]=2/27`, `Gram[d2,d2]=2/3`, …).
- **Gate 1: 6/6 PASS** (verdict() non-hardwired, vacuum M=0→0, sign-pin regression, Δ_L(g)=0,
  Δ_L^{(1,1)} preserves the gauge image, **SCHUR λ_L=32** for d1/d2/s01).
- **Gate 3: 5/5 PASS** (3a residue closes nonzero+TT, 3b c(M)∝N(M)=**False**, 3c κ=1/54 detM-absent,
  3c-identity symbolic, 3d dictionary `B3 = r + δ*ω + f·g` EXACT).
- **`verdict()` NON-HARDWIRED — CONFIRMED.** Fed 7 synthetic flag combinations: LIVE only when
  `closes_3a ∧ norm_forced ∧ needs_outside is None ∧ schur_ok ∧ ¬contradicts`; flipping any required
  flag changes the result (closes_3a→STOP, norm_forced→PARTIAL, contradicts→STOP). Deterministic.
- **Dead code — CONFIRMED (flagged):** two `def lichnerowicz` (lines 840, 897); the 2nd shadows the
  1st. Both bodies are byte-identical (full-tensor Δ_L), so the shadowing is harmless. The
  verdict-critical path uses `lichnerowicz_11` (lines 1125/1263/1283/1329); the full `lichnerowicz`
  is used only on `g` and the zero tensor (controls 1b/1c), where the anti-block is genuinely zero.
- **3a does NOT contradict v31 — CONFIRMED.** Independently (general-polynomial ω, NOT the
  {φ_A dφ_B} ansatz): `york_solve(B1)` consistent at D=3 while `york_solve(B3)` INCONSISTENT
  (B3 ∉ gauge⊕conformal) — the v31 existence obstruction reproduced. `B3 = r + δ*ω + f·g` holds
  exactly with r nonzero, tr_g=0, div=0.
- **Scope fences (binding) — present and correct.** The VERDICT/driver carry the no-dynamics fence
  verbatim (no Einstein-eq/κ/G=κT/dark-matter/geodesic; frozen FS USED-not-derived; v18/v20 corpse
  buried; OP² priced only; ε named+fenced, the Fredholm response equation NOT run). ε is a stiffness
  label, not run as a response equation. **These fences are intact** — the issues below are about the
  numbers, not the framing.

---

## PRIORITY A — the (1,1)-projection (the suspected bug): CONFIRMED BUG

### A.1 — `r[1]` is NOT a transverse (1,1) tensor (the divergence couples the J-blocks)

The York TT residue `r` of `B3 = dφ_M⊗dφ_M` is the UNIQUE transverse-traceless tensor (tr_g r=0 ∧
δr=0). I extracted the executor's `r` (via `extract_tt`, verified `tr_zero=True, div_zero=True`) and
decomposed it into its J-invariant (1,1) block and J-anti-invariant (2,0)+(0,2) blocks. **Exact over Q
(s01):**

| object | divergence-free? | ‖·‖² |
|---|---|---|
| `r[1]` ALONE = (0, r₁₁, 0) | **NO** | 2/27 |
| `r_anti` ALONE = (r₂₀, 0, r₀₂) | **NO** | 8/135 |
| **full r** | **YES** (TT) | 2/15 |
| div(r₁₁) + div(r_anti) | **= 0** (only the SUM is transverse) | — |
| ‖r₁₁‖² + ‖r_anti‖² | (L²-orthogonal) | = 2/15 = ‖r‖² ✓ |

So the genuine TT residue genuinely has BOTH a nonzero (1,1) part AND a nonzero (2,0)+(0,2) part whose
**divergences cancel against each other** — neither block is individually transverse. The executor's
docstrings admit `r` carries a "divergence-coupled (2,0)/(0,2) gauge remainder," but the (2,0)+(0,2)
part is **NOT gauge** (see A.2). The executor then reads κ, the direction, and the Schur scalar off
`r[1]` alone — an object that is neither transverse nor a clean (1,1) eigentensor.

### A.2 — the (2,0)+(0,2) part is NOT pure gauge — REFUTES v31's "jointly gauge"

Independent general-polynomial-ω test: is B3's (2,0)+(0,2) part expressible as δ*ω+f·g?

| degree D | B3 (2,0)+(0,2) pure gauge+conformal? |
|---|---|
| D=3, kw=2 | **False** |
| D=4, kw=3 | **False** |

The (2,0)+(0,2) sector of B3 carries genuine **transverse** content (the Boucetta λ=32 dim-27 modes,
Tables VI/VII). **This contradicts the ratified v31 claim** that "the (2,0)+(0,2) blocks are
individually/jointly pure gauge ⇒ the residue is purely (1,1)" (91-VERDICT §V3; 91-RESEARCH line 246).

> **NOTE on v31:** v31's HEADLINE (matter sources a NONZERO TT mode — LIVE/existence) is **NOT
> overturned**; it is independently re-confirmed (B3 ∉ gauge⊕conformal). What is wrong is v31's
> *isotypic localization* ("residue purely in the (1,1) λ=12 sector"). The genuine residue MIXES the
> (1,1) λ=12 dim-8 mode and the (2,0)/(0,2) λ=32 dim-27 modes. This is a regression in the v31
> characterization that propagates into v32's ε and norm.

### A.3 — there is NO standalone transverse-traceless (1,1) tensor at low degree

Solving directly for a purely-(1,1) tensor that is traceless AND transverse (general (1,1) ansatz,
no reference to B3): **0 nonzero solutions** at D=2/kp=2, D=3/kp=2,3, D=4/kp=3. Forcing the
(2,0)/(0,2) of B3 entirely into δ*ω+f·g with a purely-(1,1) transverse residue: **INCONSISTENT** at
D=3 and D=4. This is structural: transversality of a (1,1) tensor forces (2,0)/(0,2) coupling. So
"`r[1]` = the clean dim-8 (1,1) TT multiplet element" is **false** — the executor's basis {t_a}=r[1]
is the (1,1) block of a J-mixed object, not a (1,1) TT eigentensor.

### A.4 — the direction c(M) ∝ N(M) FAILS — REAL, not a contamination artifact

| test | result |
|---|---|
| N(s01) = N(d1) = diag(1,1,0)−⅔I | **True** |
| `r[1]`(s01) = `r[1]`(d1)? | **False** |
| **full** r(s01) = r(d1)? | **False** |

Both the (1,1) block AND the full residue differ between s01 and d1 while N is equal ⇒ **c(M)∝N(M)
genuinely fails** (the executor's FAIL is correct, NOT a contamination artifact). **Mechanism:** the
multiplicity-one pinning (Sym²(8)⊃8 once ⇒ the projection is the unique d-symbol) only forces
c(M)∝N(M) IF the residue is a single copy of the **8**. It is not — the residue spans the **8 ⊕ 27**
(the (1,1) λ=12 plus the (2,0)/(0,2) λ=32). With more than one irreducible present, multiplicity-one
does not pin the direction, so the FAIL is expected, not a paradox. (The executor's prose attributes
the FAIL to "the full dφ⊗dφ structure"; the sharper statement is "the residue is not a single copy of
the adjoint 8.")

### A.5 — κ on the clean object (CORRECTED value)

The norm closes with a FORCED detM-absent constant for EVERY block, exact over Q across matters
{s01, d1, d2(detM=−2), a01}:

| matter | ‖r₁₁‖² (executor) | k₁₁ | ‖r_anti‖² | k_anti | ‖full‖² | **k_full** | detM |
|---|---|---|---|---|---|---|---|
| s01 | 2/27 | 1/54 | 8/135 | 2/135 | 2/15 | **1/30** | 0 |
| d1 | 2/27 | 1/54 | 8/135 | 2/135 | 2/15 | **1/30** | 0 |
| d2 | 2/3 | 1/54 | 8/15 | 2/135 | 6/5 | **1/30** | −2 |
| a01 | 2/27 | 1/54 | 8/135 | 2/135 | 2/15 | **1/30** | 0 |

- **κ = 1/54 is reproduced** (independent l2_tensor) — but it is the norm of `r[1]` (the (1,1) BLOCK),
  NOT "the matter-sourced TT metric mode." It captures only **5/9** of the full TT mode's norm.
- **The genuine matter-sourced TT mode (the full unique TT residue) has κ_full = 1/30** (= 1/54 +
  2/135, the L²-orthogonal sum), also FORCED, also detM-absent.
- **detM ABSENT — CONFIRMED** for all three (the (TrM²)²-only degree-4 invariant-theory argument is
  correct; verified across detM∈{0,−2}).

---

## PRIORITY B — ε = 20 / λ_L = 32: REFUTED (genuine ε = 0)

### B.1 — Boucetta (arXiv:0712.2830), fetched and read — SAME convention as the executor

- **Lichnerowicz convention (p.5):** Δ_M(T) = D*D(T) + R(T) = ∇*∇ + Ric∘ + ∘Ric − 2R̊ — the **Besse
  convention, identical to the executor's frozen Δ_L.** No normalization shift.
- **Ricci (Lemma 2.1, p.8):** r(X) = 2(n+1)X ⇒ **Ric = 6g at n=2 — identical to the executor (Λ=6).**
- **Δ_M respects the Kähler bigraduation** (pp.5–6).

So Boucetta's eigenvalues are **directly comparable, no convention correction**.

### B.2 — the genuine (1,1) TT eigenvalue is 12, NOT 32 (Tables V, VIII + master formula)

- **Table VIII (S^{1,1}(P²(C)), n=2):** the (1,1) primitive TT mode φ(T^{1,1}_{0,0}) has eigenvalue
  **12**, complex dim **8**. (Table V general-n row 1: eigenvalue **4(n+1)** = 12 at n=2, dim
  n(n+2)=8.)
- **Tables VI/VII (S^{0,2}/S^{2,0}, n=2):** the LOWEST anti-invariant TT mode has eigenvalue **32**,
  dim **27** each. (Tables III/IV general-n row 1: eigenvalue **8(n+2)** = 32 at n=2,
  dim n(n+4)(n+1)²/4 = 27.)
- **Master formula (Lemma 3.4) cross-check at n=2:** (1,1) primitive → 12; (2,0)/(0,2) lowest → 32.

**Conclusion: the genuine Boucetta Lichnerowicz eigenvalue of the (1,1)-Hermitian dim-8 TT mode is
λ_L = 12 ⇒ ε = λ_L − 2Λ = 12 − 12 = 0 (Einstein-marginal). The value 32 is the eigenvalue of the
(2,0)/(0,2) dim-27 sector** — exactly the J-anti-invariant content that mixes into B3's TT residue.

### B.3 — why the executor got 32 (operator is CORRECT, input is WRONG)

- **Operator agreement — CONFIRMED.** My fully independent Δ_L^{(1,1)} (own Kähler Riemann — matches
  the executor's byte-for-byte; own covariant 2nd derivative; own Weitzenböck) gives **λ = 32 on
  r[1]**, EXACTLY matching the executor's `lichnerowicz_11`. The operator is not the bug.
- **Operator calibration — CONFIRMED.** Independent operator passes the same controls:
  R̊(g)=6g=Ric ✓, Δ_L(g)=0 ✓, ∇*∇(g)=0 ✓. So the 32-vs-12 gap is **entirely about the input
  object**: `r[1]` is NOT a transverse (1,1) tensor (A.1) and NOT the genuine λ=12 eigentensor (A.3).
  Feeding the (1,1)-block-only operator a non-transverse (1,1) block returns the (2,0)/(0,2)-flavored
  eigenvalue 32, not the genuine (1,1) λ=12.
- The full Δ_L on the **full** r is NOT proportional to r (block ratios 28/32/4) ⇒ the full residue is
  not a single eigentensor (it is the **8⊕27** superposition), consistent with B.2. (Side note: the
  executor's full `lichnerowicz` gives 28/4 on the (2,0)/(0,2) blocks, which match neither 12 nor 32 —
  the anti-block Weitzenböck/rough-Laplacian path looks mis-normalized; but this path is OFF the
  verdict-critical route, which only uses `lichnerowicz_11` on r[1].)

### B.4 — the Besse/Koiso "trap #16" resolved correctly, but the OPPOSITE way to the executor

- Besse 12.28: infinitesimal Einstein deformations = ker(Δ_L − 2Λ)|_TT. Besse 12.98: CP^n is
  Koiso-RIGID. Boucetta: the (1,1) TT dim-8 sits AT λ=12 = 2Λ.
- **The genuine resolution:** the (1,1) TT dim-8 mode IS at λ_L = 2Λ = 12 (ε=0, formally
  Einstein-marginal), and Koiso rigidity is **second-order/obstruction-theoretic** (the dim-8 (1,1)
  primitive is the lowest Lichnerowicz TT but is NOT an integrable Einstein deformation —
  91-RESEARCH line 116 says exactly this: "this dim-8 is the lowest Lichnerowicz TT, NOT an Einstein
  deformation"). This is the executor's RESEARCH §3 branch **(b)** (`ε=0`, second-order Koiso),
  which the executor itself pre-registered — and then did NOT take.
- The executor instead claimed branch **(a)** (ε=20≠0, "λ_L=32 = scalar 12 + Weitzenböck shift, NOT
  the same operator as Boucetta's"). This is **false**: Boucetta's operator IS the same operator
  (B.1), and Boucetta's (1,1) TT eigenvalue IS 12. The executor's "12 is the scalar carrier's
  threshold, not the Lichnerowicz eigenvalue" mis-reads Table VIII — 12 there IS the Lichnerowicz
  eigenvalue of the symmetric-2-tensor (1,1) TT mode, not a scalar eigenvalue.

---

## Per-claim ledger

| claim | verdict | evidence | confidence |
|---|---|---|---|
| κ = 1/54 (of `r[1]`) | **CONFIRMED** (independent l2_tensor: 2/27, 2/3 → 1/54) | A.5 | INDEPENDENTLY CONFIRMED |
| κ = 1/54 = "norm of the matter-sourced TT mode" | **MISLABELED → CORRECTED to κ_full = 1/30** | A.1, A.5 (full TT mode norm = 2/15 = (1/30)(TrM²)²) | INDEPENDENTLY CONFIRMED |
| detM ABSENT | **CONFIRMED** (all three blocks; detM∈{0,−2}) | A.5 | INDEPENDENTLY CONFIRMED |
| ε = 20 / λ_L = 32 (1,1) | **REFUTED → ε = 0, λ_L(1,1) = 12** | B.1–B.4 (Boucetta, same convention; operator agreement) | INDEPENDENTLY CONFIRMED |
| direction c(M) ∝ N(M) | **FAILS — CONFIRMED real** (full residues differ too) | A.4 | INDEPENDENTLY CONFIRMED |
| dictionary B3 = r + δ*ω + f·g closes | **CONFIRMED** exact over Q | C, A.2 | INDEPENDENTLY CONFIRMED |
| verdict() non-hardwired | **CONFIRMED** | C | INDEPENDENTLY CONFIRMED |
| scope fences (no dynamics/κ) intact | **CONFIRMED** | C | INDEPENDENTLY CONFIRMED |
| 3a consistent with v31 (nonzero TT exists) | **CONFIRMED** | C | INDEPENDENTLY CONFIRMED |
| v31 "(2,0)+(0,2) jointly gauge ⇒ residue purely (1,1)" | **REFUTED** (anti part nonzero + non-gauge) | A.1, A.2 | INDEPENDENTLY CONFIRMED |

---

## Bottom line for the verdict

The v32 verdict text — "**‖TT(B3)‖² = (1/54)(TrM²)²** ... the Lichnerowicz threshold **ε = 20**" — is
**not a correct statement about the matter-sourced TT metric mode**:

1. **ε = 20 is REFUTED.** The genuine Lichnerowicz eigenvalue of the (1,1) TT dim-8 mode is **12**, so
   **ε = 0** (Einstein-marginal; Koiso rigidity is second-order). The executor's 32 is the
   **(2,0)/(0,2)** sector eigenvalue, obtained by applying the (correct) operator to the **wrong**
   object (the non-transverse (1,1) block `r[1]`). This is the **verdict CENTER's sub-fork**, and it
   lands on the opposite branch.

2. **κ = 1/54 is the (1,1)-block norm, not the TT-mode norm.** The genuine matter-sourced TT metric
   mode (the full unique York TT residue) has **‖TT(B3)‖² = (1/30)(TrM²)²**. Both close with a forced
   constant and detM absent, so the v32 LIVE *shape* criterion (a forced κ(TrM²)², no free function)
   is met **for either object** — but the executor's stated κ=1/54 is attached to the wrong tensor.

3. The shape facts that DO survive intact: (i) a nonzero matter-sourced TT mode EXISTS (v31, ✓);
   (ii) its norm is a FORCED degree-4 invariant = κ(TrM²)² with **detM absent** (✓, the
   invariant-theory argument is correct); (iii) the dictionary B3 = TT + δ*ω + f·g closes (✓);
   (iv) c(M)∝N(M) fails (✓, and now mechanistically explained as 8⊕27, not a single 8).

**Recommended corrections (loud):**
- **ε: 20 → 0** (λ_L of the (1,1) TT mode is 12, not 32). The non-marginal/stiffness reading is gone;
  the mode is Einstein-marginal, Koiso-second-order — fence accordingly.
- **κ: re-label.** If the verdict object is the (1,1) BLOCK, κ=1/54 (state it as the (1,1)-block
  norm). If it is the genuine TT MODE, **κ = 1/30**. Either way, drop "‖TT(B3)‖²=1/54" as written.
- **v31 isotypic claim** ("residue purely (1,1)") needs a footnote: the residue is **8⊕27** (the (1,1)
  λ=12 plus the (2,0)/(0,2) λ=32), not purely (1,1). v31's existence verdict stands; its localization
  does not.

**This does NOT, by itself, sink a LIVE-class dictionary statement** — a forced, detM-absent
κ(TrM²)² norm closure genuinely holds (for the full mode, κ=1/30). But the verdict as written reports
the wrong κ-object and a refuted ε, so it must be corrected before ratification. **Overall:
INCONSISTENT with the executor on ε (refuted) and on the κ object (corrected), CONSISTENT on
detM-absence, the dictionary closure, the direction finding, and all integrity checks. Confidence
HIGH** (Boucetta read directly with matching convention; independent operator agrees with the
executor on the same input; norms reproduced exactly over Q; the structural impossibility of a
standalone (1,1) TT tensor confirmed at D≤4).

---

## Reproducibility

- `code/lichnerowicz_response_verify.py` — independent module; `python3 -u lichnerowicz_response_verify.py B`
  (Boucetta formula + operator agreement + calibration, ~45s) and `... A` (J-decomposition, norms, ~70s).
- Executor reproduction: `python3 -u lichnerowicz_response.py g0|g1|g3` (6/6, 6/6, 5/5 PASS).
- All numbers exact over Q. Boucetta arXiv:0712.2830 Tables III–VIII + Lemmas 2.1/3.4 (n=2).
