# Phase 95 / v35.0-candidate — THE AREA-PER-BIT KILL-TEST — SUMMARY

> Driver: `code/area_per_bit.py` (fresh, independent; built from `derivations/95-area-per-bit-RESEARCH.md`).
> Exact over ℚ on every decisive line; octonion engine NOT on the decisive path (h₃(ℂ) = the C_u cut = CP²).
> Run: `python3 -u code/area_per_bit.py` → **exit 0, 25/25 checks PASS, ~2.6 s**.
> **VERDICT: DEAD-FISHER / fork A** (the de-risked expected landing, reached rigorously not assumed).
> **MILESTONE HOLD for human ratification** — state.json / MILESTONES / PROJECT / STATE NOT touched; no `gpd phase complete`.

---

## 1. The question and the answer (one paragraph)

Does the variety (CP², the C\*-cut of OP² where v23's faithful-point fiber kill does not reach) natively set the
**bits ↔ geometric-area exchange rate** as a UNIVERSAL CONSTANT (→ a background scale; gravity a contingent import;
**fork A**) or as a SHEARING field (→ a candidate gravitational field)? **Answer: DEAD-FISHER / fork A.** The
variety's only FS-canonical local area is **identically the quantum Fisher / QGT-real metric** `Var_p(M)` (v17's
corpse — a positive-semidefinite object on STATES, not a spacetime metric). The ratio `R = A_M/|G_M|` shears
strongly in `p` and across `M`, but the shear is the (well-known, state-space) disagreement between the Fisher
information `Var` and the relative-entropy Hessian `G_M`, **NOT a geometric bits↔area exchange rate**. There is no
native geometric area independent of the state-space information geometry to pair with the bits ⇒ the variety sets
**no native geometric bits↔area rate** ⇒ the rate (Ryu–Takayanagi's `G`) is a contingent import ⇒ **fork A**. This
**closes the entanglement route** (the sixth brainstorm angle), reached through the sharper, more defensible identity
"the canonical area IS the bit-counter metric" — the same fork-A conclusion family as v33 FORCES-NOTHING and the v23
∇S = 0 death.

---

## 2. Gate-by-gate results table

| Gate | What it checks | Result | Key exact facts |
|------|----------------|--------|-----------------|
| **self-tests** | verdict() ladder is NON-HARDWIRED (flips under synthetic inputs) | **5/5 PASS** | rigged-constant→DEAD-CONSTANT; non-Fisher shear→LIVE-{TENSOR,SCALAR}; non-agreeing areas→INCONCLUSIVE; A=Var→DEAD-FISHER; 5 distinct outputs |
| **G0.1** | certified objects on s01,a01,d1,gen; Tr M = 0; G_M ≤ 0 | **3/3 PASS** | Tr M = 0 (all 4); G_M ≤ 0 on {P0,P2,Q}×4; M# = diag(0,0,−1) (rank-2), diag(−2,−2,1) (gen) |
| **G0.2** | Bug-guard 4 (OFF I/3, not vacuous): G_M(p) VARIES with p | **1/1 PASS** | G_M(P0)≠G_M(P2) all 4 dirs (e.g. d1: −5/16 vs −13/15) ⇒ ∇S_face ≠ 0 |
| **G0.3** | PIN A_M canonically — SYMBOLIC identities (ALL p, ALL M) | **7/7 PASS** | det(gN)=ρ; **A_ii−Var≡0**; **A_iii−Var≡0** (KKS); **A_ii≡A_iii** (no flip); **G_M−(Var+¾⟨M⟩²−½TrM²)≡0**; shear≡¾⟨M⟩²−½TrM²; numeric anchor d1@P0 all = 1/2 |
| **G0.4** | FISHER-CORPSE determination (Bug-guard 3) | **1/1 PASS** | A_M ≡ Var ≡ the quantum Fisher metric = a STATE-SPACE object (v17 corpse) ⇒ decision rule routes to DEAD-FISHER |
| **G0.3(i)** | CONTROL: candidate (i) is a per-M CONSTANT (homogeneity-artifact mode) | **1/1 PASS** | A_i_global = 1/12 (s01,a01,d1), 1/4 (gen) — p-INDEPENDENT ⇒ rejected as a competing local area |
| **G1 ground truth** | reproduce RESEARCH §9 (Var, G_M, R on 6 rows) | **2/2 PASS** | all 6 rows EXACT; A_iii (KKS) reproduces the SAME R (no flip) |
| **G1 guard (1)** | DENOMINATOR-ZERO handling | **1/1 PASS** | genuine G_M=0 locus = the EQUATOR (z1=±1, z2=0; corrected from §3 "vertex"); reciprocal |G|/A=0 finite; vertex = NUMERATOR-zero (Var=0, R=0) |
| **G1 guard (2)** | HOMOGENEITY: R non-constant + A_M, G_M different M-structure | **2/2 PASS** | R ∈ {2/13, 4/3, 8/5, 44/17} NOT literally constant; shear = ¾⟨M⟩²−½TrM² (state-space) |
| **G1 guard (3)** | FISHER-CORPSE gate (decisive) | **1/1 PASS** | A_M ≡ Var ⇒ R = Fisher/(rel-entropy) ⇒ DEAD-FISHER / fork A, STOP (G2 not reached) |
| **G1 preempt** | LIVE-TENSOR killed (TT present-but-Fisher; adversarial-sharpened) | **1/1 PASS** | rank-1 dφ⊗dφ ⇒ every FS-canonical area is a Var power: A_ii=Var, A_full=4Var², **A_TT=3Var²**; TT channel PRESENT but a Fisher monomial ⇒ no independent rate |
| **G2** | the rank wall | **NOT REACHED** | the Fisher-corpse gate fired in G1; no genuine geometric non-Fisher shear survived |
| **verdict()** | the real verdict from computed booleans | **DEAD-FISHER** | flags {areas_agree:T, A_is_fisher:T, R_constant:F, area_is_trace:T, shear_is_geometric:F} |

**Total: 25/25 checks PASS, exact over ℚ, no float in the verdict, exit 0.**

---

## 3. The symbolic identities (shown — `simplify == 0` for ALL p, ALL M)

Proven over a GENERIC 8-parameter traceless cut matter `M` (2 diagonal trace-free + 3 complex off-diagonal,
Hermitian) and ALL chart points `p` (z, z̄ independent Wirtinger symbols), each via exact **polynomial-numerator**
comparison over explicit ρ-powers (the enabling fact: det(gN) = ρ ⇒ the FS inverse `g_pot^{-1} = ρ·adj(gN)` is a
polynomial; this avoids the `cancel`-of-combined-fraction performance cliff — see §6 deviations):

| Identity | Statement | Status |
|----------|-----------|--------|
| (ii) metric-trace area | `A_ii := g_pot^{a b̄} ∂_a φ_M ∂_{b̄} φ_M = |∇φ_M|²_g  ≡  Var_p(M)` | **≡ 0 ✓** |
| (iii) KKS symplectic | `A_iii := g_{a b̄} X^a conj(X)^{b̄}`, `X = J∇φ` (i.e. `X^a = +i g^{a b̄}∂_{b̄}φ`) `≡ Var_p(M)` | **≡ 0 ✓** |
| Bug-guard 1 (no flip) | `A_ii ≡ A_iii` (the two canonical area defs agree) | **≡ 0 ✓** |
| decomposition | `G_M(p) − (Var_p(M) + ¾⟨M⟩²_p − ½Tr(M²)) ≡ 0` | **≡ 0 ✓** |
| shear | `(G_M − Var) − (¾⟨M⟩²_p − ½Tr(M²)) ≡ 0` | **≡ 0 ✓** |

**Conventions / objects (all exact over ℚ):**
- Chart: `v = (1, z₁, z₂)`, `P(z) = v v† / (v† v)`, `ρ = 1 + z₁z̄₁ + z₂z̄₂`; z, z̄ INDEPENDENT (Wirtinger).
- Conjugation = the **full** complex conjugation: z↔z̄ SWAP **AND** i→−i. (Never sympy `conjugate()` on the
  independent z symbols; but i→−i on the genuine imaginary unit IS required — see §6 deviation, this was a latent bug.)
- `⟨X,p⟩ = Tr(X·P)`; `X# = adj(X) = X² − Tr(X)X + ½((TrX)²−Tr(X²))I`; for traceless M: `M# = M² − ½Tr(M²)I`.
- `φ_M = ⟨M,p⟩`; `Var_p(M) = ⟨M²,p⟩ − ⟨M,p⟩²`; `G_M(p) = ⟨M#,p⟩ − ¼⟨M,p⟩²` (≤ 0).
- Canonical area uses the **potential / Fisher** metric `g_pot = ∂∂̄ log ρ = Re(QGT)` (Provost–Vallée), giving
  `A_ii ≡ Var`. The engine/Boucetta metric `g_phys = g_pot/2` gives `A_ii(phys) ≡ 2·Var` — the single overall scale
  G1 allows to normalize away (R = A/|G| rescales uniformly; it does NOT decide the verdict).

---

## 4. RESEARCH §9 de-risked ground truth — REPRODUCED EXACTLY

Chart points: P0 (z₁=1+2i, z₂=−1+i ⇒ ρ=8); P2 (z₁=−1, z₂=2−3i ⇒ ρ=15). A_M = A_ii = A_iii = Var.

| M | point | ⟨M,p⟩ | Var = A_M | G_M | R = A/\|G\| | §9 expected | match |
|------|-------|--------|-----------|-----------|-------------|-------------|:-----:|
| d1 | P0 | −1/2 | 1/2 | −5/16 | 8/5 | 8/5 | ✓ |
| d1 | P2 | 0 | 2/15 | −13/15 | 2/13 | 2/13 | ✓ |
| s01 | P0 | 1/4 | 11/16 | −17/64 | 44/17 | 44/17 | ✓ |
| a01 | P0 | 1/2 | 1/2 | −5/16 | 8/5 | 8/5 | ✓ |
| gen | P0 | 1/4 | 27/16 | −81/64 | 4/3 | 4/3 | ✓ |
| gen | P2 | −8/5 | 26/25 | −1/25 | 26 | 26 (denom near-zero artifact) | ✓ |

**Worked anchor (d1 @ P0):** φ = (1−|z₁|²)/ρ = (1−5)/8 = −1/2; ⟨M²⟩ = (P₀₀+P₁₁) = 6/8 = 3/4; Var = 3/4 − 1/4 = 1/2;
M# = diag(0,0,−1), ⟨M#⟩ = −P₂₂ = −2/8 = −1/4; G_M = −1/4 − ¼·(1/4) = −5/16; decomposition check
Var + ¾⟨M⟩² − ½Tr(M²) = 1/2 + ¾·1/4 − ½·2 = 1/2 + 3/16 − 1 = −5/16 ✓.

**R is NOT literally constant** (8/5, 2/13, 44/17, 4/3 vary by direction and point) ⇒ the literal DEAD-CONSTANT reading
FAILS. The shear is `Var/|G_M| = Fisher/(relative-entropy)`, state-space, not geometric ⇒ **DEAD-FISHER / fork A**.

**Independent cross-check (separate code path):** all 6 rows reproduced via a from-scratch numeric projector using
`sympy.conjugate` on the concrete complex chart points (NOT the Wirtinger symbols) — two independent implementations
agree exactly on every decisive R-value. [CONFIDENCE: HIGH]

---

## 5. The bug-guard dispositions (pre-registered, RESEARCH §3/§5)

| # | Bug guard | Disposition |
|---|-----------|-------------|
| 1 | **AREA-RIG** (FS-canonical + matter-functorial; re-run with ≥2 defs; flip ⇒ INCONCLUSIVE) | **CLEARED**: A_ii (metric-trace) and A_iii (KKS symplectic) are both FS-canonical and matter-functorial, and they AGREE identically (A_ii ≡ A_iii ≡ Var, symbolic). No flip ⇒ NOT INCONCLUSIVE. |
| 2 | **CIRCULARITY** (FS is imported; do NOT record G as derived) | **HONORED**: the FS metric is USED, not derived. This run DIAGNOSES whether native area↔entropy variation exists; it records NO derived G. The verdict (DEAD-FISHER) is the diagnosis that no native geometric rate exists. |
| 3 | **FISHER-CORPSE** (G_M is the state-space Fisher/Bures object; do NOT read R's shear as curvature) | **FIRES — DECISIVE**: the canonical AREA `A_M` is ALSO the Fisher object (A_M ≡ Var = the QGT-real metric). So R = Var/\|G_M\| is Fisher/(rel-entropy) — both state-space. The shear is NOT a geometric rate ⇒ DEAD-FISHER. |
| 4 | **CONSTANT-BY-SYMMETRY** (at I/3 everything is F₄-homogeneous, ∇S=0 = v23; confirm OFF I/3) | **CLEARED**: G_M(p) genuinely varies with p (G_M(P0)≠G_M(P2) all 4 dirs) ⇒ ∇S_face ≠ 0 ⇒ NOT vacuous (unlike v23). |
| 5 | **NUMERIC LEAKAGE** (exact over ℚ; no floats in the verdict) | **HONORED**: every decisive line is sympy.Rational / cancel / expand over ℚ (and ℚ(i) for the complex chart). No float anywhere in the verdict path. |

---

## 6. Deviations table (every number / framing vs RESEARCH)

| # | Item | RESEARCH says | Driver finds (exact) | Disposition |
|---|------|---------------|----------------------|-------------|
| 1 | A_ii ≡ Var | identity (§1.3, §9) | **≡ 0** symbolically (all p,M) | **CONFIRMED** |
| 2 | A_iii ≡ Var (KKS) | identity (§1.3, §9) | **≡ 0** symbolically (all p,M) | **CONFIRMED** |
| 3 | G_M = Var + ¾⟨M⟩² − ½TrM² | identity (§2, §9) | **≡ 0** symbolically (all p,M) | **CONFIRMED** |
| 4 | §9 point table (6 rows) | exact values | all 6 EXACT (Var, G_M, R) | **CONFIRMED** + independent path |
| 5 | M# for rank-2 dirs | diag(0,0,−1) (§1.3) | diag(0,0,−1) (s01,a01,d1) | **CONFIRMED** |
| 6 | M# for gen | diag(−2,−2,1) (§1.3) | diag(−2,−2,1) | **CONFIRMED** |
| 7 | **denominator-zero locus** | "G_M → 0 **near the vertex** E_11" (§3 guard 1) | **G_M=0 at the EQUATOR** z₁=±1,z₂=0 (the (1,2)-block maximally mixed); at the **vertex** it is the **NUMERATOR Var=0** (eigenstate) while G_M=−1/4 finite | **DEVIATION [Rule 4 — corrected locus]**: the §3 "vertex" framing is imprecise for these directions; the exact G_M=0 locus is the equator. Physics unchanged (both loci are non-shears; reciprocal \|G\|/A=0 finite at the equator, R=0 at the vertex). Driver tests the CORRECT facts. |
| 8 | **conjugation method** | "use a z↔z̄ swap (NEVER sympy conjugate)" (prompt) | the z↔z̄ swap ALONE gives A_iii ≠ Var; the **full** conjugation = swap **AND** i→−i gives A_iii ≡ Var | **DEVIATION [Rule 1 — latent bug fix]**: the swap is necessary but NOT sufficient — the genuine imaginary unit I (from the matter Hermitian off-diagonals and the J-factor i) must also flip i→−i. This is legitimate complex conjugation of a true constant (NOT applying sympy `conjugate()` to the independent Wirtinger z symbols, which remains banned). With both pieces the KKS identity holds exactly. |
| 9 | metric normalization for A_ii≡Var | not specified | the **potential/Fisher** metric g_pot=∂∂̄ log ρ (not the engine g_phys=g_pot/2) | **DEVIATION [Rule 4 — pinned normalization]**: A_ii≡Var requires the QGT-real/Fisher normalization (g_pot); the engine metric gives 2·Var. Both reported; the overall scale is the one G1 normalizes away and does not affect the verdict. |
| 10 | R literally constant? | expected NOT constant (de-risk, §9) | NOT constant ({2/13,4/3,8/5,44/17}) | **CONFIRMED** (literal DEAD-CONSTANT reading fails; DEAD-FISHER is the mechanism) |

No deviation rose to Rule 5/6 (no physics redirect, no scope change). Deviations 7–9 are correctness fixes (Rules 1/4)
that leave the verdict and all decisive numbers unchanged.

---

## 7. Confidence (per claim)

- **A_ii ≡ A_iii ≡ Var (symbolic, all p, all M)** — [CONFIDENCE: HIGH]: exact polynomial-numerator identity over the
  generic 8-param M; numeric anchor d1@P0 = 1/2 cross-checks; det(gN)=ρ certificate.
- **G_M = Var + ¾⟨M⟩² − ½TrM² (symbolic)** — [CONFIDENCE: HIGH]: exact numerator identity; matches §9 worked anchor.
- **§9 ground truth (6 rows)** — [CONFIDENCE: HIGH]: reproduced exactly by TWO independent code paths (the Wirtinger
  chart and a from-scratch concrete-point numeric projector).
- **FISHER-CORPSE ⇒ DEAD-FISHER / fork A** — [CONFIDENCE: HIGH for the math, MEDIUM for the interpretive leap]: the
  math (A_M ≡ the Fisher metric) is exact and decisive. The interpretive step "a Fisher-object area certifies no
  geometric rate" rests on the Provost–Vallée identification FS = Re(QGT) = the quantum Fisher metric (a standard,
  cited result) and the program's own Fence 3 / Bug-guard 3 pre-registration. Flagged MEDIUM only because it is an
  interpretive (not purely computational) determination; it is the de-risked, pre-registered expected landing.
- **verdict() non-hardwired** — [CONFIDENCE: HIGH]: the same function returns 5 distinct verdicts under synthetic
  inputs (self-tests), proving the branch is forced by the flags, not a constant.
- **G2 not reached / LIVE-TENSOR killed (TT-is-Fisher)** — [CONFIDENCE: HIGH]: the rank-1 metric-mode dφ⊗dφ has
  EVERY FS-canonical area a Var power (A_ii=Var, A_full=4Var², A_TT=‖traceless‖²=3Var²); the TT channel is PRESENT but
  a Fisher monomial (not "structurally precluded", per the adversarial path) ⇒ no independent geometric rate; the
  Fisher gate fires before G2.

---

## 8. FENCES (binding, verbatim — copied from RESEARCH §6)

> NO Einstein-equation / G=κT / gravity / Newton / dark-matter / geodesic language as a DERIVED result; the bits↔area
> rate is a framework ratio (a contingent import like κ, Λ unless G1 forces otherwise), **NOT Newton's G**; FS is
> USED, not derived; signature **Riemannian** (Wall 2 unpaid — NOTHING is called gravity until signature is paid);
> DEAD-CONSTANT / DEAD-FISHER and LIVE-\* are NOT derivations of gravity. This run does NOT retract v33 (extremize
> FORCES-NOTHING), v34 (induce CLOSES-CONDITIONAL), v17–v21 (fiber kills), or v23 (I/3 death). **Paper 5 remains the
> only result in the more-than-nothing column.**

## 9. ANTI-OVERCLAIM (verbatim — RESEARCH §7, Jaksland arXiv:2005.05055)

> LIVE (either) = the variety sets a non-constant exchange rate — NECESSARY, not sufficient, for gravity; it is the
> area-side diagnostic of the entanglement route, UPSTREAM of the clamp (state-fp ⟹ metric-fp). Even LIVE-TENSOR shows
> native area↔entropy variation, NOT that the metric obeys a field equation. A generic Jacobson/RT recovery validates
> nothing program-specific — the originality is whether the variety FORCES the rate, not that an area law exists.
> DEAD (CONSTANT or FISHER) is the expected and honest outcome; it closes the entanglement route and is the green light
> for fork A. Holography is theorem-blocked natively (h₃(O) is finite Type-I₃ by Zelmanov; the "Area/4G from an
> algebra" result CPW arXiv:2302.01938 needs a Type III₁ factor the exceptional algebra cannot have). The program has
> the Bekenstein BOUND (S ≤ Area, G-free) but NOT the RT EQUALITY (Area = 4G·S, G-valued); the G-valued equality is the
> unpaid step = the clamp.

---

## 10. Reproducibility

- `python3 -u code/area_per_bit.py` → exit 0, 25/25 PASS, ~2.6 s.
- sympy 1.14.0, Python 3.x (Homebrew /opt/homebrew/bin/python3), Darwin arm64. Exact rational arithmetic over ℚ / ℚ(i);
  no RNG, no seeds in the verdict path (floats illustrative only).
- Octonion engine (`octonion_algebra.py`) is BANNED and NOT on the decisive path; the cut h₃(ℂ) is associative-clean
  (3×3 complex Hermitian matrices, rank-1 projectors).
- Commit: driver `code/area_per_bit.py` at `3af1080b`.

## Self-Check: PASSED
- `code/area_per_bit.py` exists, runs to exit 0, 25/25 PASS, exact over ℚ, no float in the verdict.
- `derivations/95-SUMMARY.md` (this file) and `derivations/95-VERDICT.md` written.
- §9 ground truth reproduced exactly + independent numeric cross-check.
- All bug guards dispositioned; deviations documented (none above Rule 4); fences + anti-overclaim copied verbatim.
- verdict() non-hardwired (5 distinct outputs under self-tests).
- MILESTONE HELD: no state.json / MILESTONES / PROJECT / STATE edits; no `gpd phase complete`.
