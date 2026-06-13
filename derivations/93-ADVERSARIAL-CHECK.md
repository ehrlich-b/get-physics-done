# Phase 93 (v33.0) — ADVERSARIAL THIRD-PATH CHECK: the Block-C gravity tripwire

**Mandate:** try to REFUTE the negative verdict (FORCES-NOTHING natively). Default to "the negative
is wrong" and attack the four load-bearing steps. If after a real effort no crack survives, the
negative is sealed triple-path.

## NET VERDICT: FORCES-NOTHING (natively) is SEALED. No attack cracked it. Confidence HIGH.

All four attacks were mounted with genuine intent to find a positive reading (FORCES-EINSTEIN-FORM or
a genuine FORCES-OTHER). Each either confirmed the negative or, where it found a real true fact
(Attack 4's invariant-class uniqueness), that fact turned out to be **vacuous as a selection law** or
**not decision-relevant** (does not touch A4 / the matter-coupling). Two of the attacks produced
*independent positive confirmations* of the verdict's own claims (Attack 1 reproduced A4's no-force
Tr(V)=0; the split-universality runs reproduced the v32 forced 5:4 across all matter incl. two dense
witnesses). This is a genuine third path: it shares no code with the orchestrator's verdict logic
(it attacks rather than re-runs), and it independently confirmed the SU(3) rep theory, the rank-6
residue span, and the no-force condition.

All computations exact over Q; short foreground/background runs; the slow 8×8 L²-tensor Gram sweep was
deliberately avoided (cheap single `l2_tensor` calls + rep theory + pointwise rank instead).

---

## ATTACK 1 — the Schur-tautology dismissal (A4 §4.1). Is the proportionality CONSTANT q meaningful?

**Counter-attack:** the verdict calls `Q_A r ∝ (Δ_L−2Λ)r` content-free because r is one irrep. But is
the constant q (the λ₁-Hessian / second-variation scalar on the matter-27) a *forced number*? If
q = ε = 20, that would be a non-trivial match (like v25's λ₁=12). Compute q, compare to 20.

**OUTCOME: CONFIRMS the negative (and STRENGTHENS the dismissal). q is not even well-posed.**

The decisive obstruction: **λ₁ = 12 is 8-fold degenerate (the SU(3) adjoint), and the matter mode
h = r lifts that degeneracy to FIRST order.** I computed the 8 first-order eigenvalue shifts
δλ_a = ⟨r, dφ_a⊗dφ_a⟩ / ⟨φ_a,φ_a⟩ for h = r(d1) (`code/adv_q_split.py`, exact/Q):

```
δλ = { d1: 8/5,  d2: 8/45,  s01: -104/135,  s02/s12/a02/a12: -8/135,  a01: -104/135 }
   = four DISTINCT values {8/5, 8/45, -104/135, -8/135}  ⇒  the 8-fold λ₁ SPLITS.
```

Because λ₁ splits under the matter perturbation, there is **no single eigenvalue whose Hessian is one
scalar q** — "the λ₁-Hessian eigenvalue on the matter-27" is set-valued (8 different directional
shifts), so "`Q_A r ∝ (Δ_L−2Λ)r` with a forced constant q=20" is not even a well-posed statement to
match. Steelmanning every natural scalar one could extract (`code/adv_q_split.py`):

```
sum of shifts (trace) = 0     self-shift δ_{d1} = 8/5     mean = 0     max = 8/5     spread = 64/27
NONE equals 20, nor 12, 32, 6 (the framework eigenvalues).
```

So even granting a "q", it is not 20 and not any framework number — no v25-style forced match. And
the deeper point is that the degeneracy-lift kills the premise. **The Schur dismissal holds; the
"content-free" judgement is correct and if anything too generous to the positive case.**

**Bonus independent confirmation of A4:** the *weighted* numerator sum
`Σ_a w_a⟨r, dφ_a⊗dφ_a⟩ = Tr(V) = ⟨4g,r⟩ = 0` reproduced exactly (`code/adv_q_split_xcheck.py`) — an
independent re-derivation of the verdict's "no first-order force" (δA = 0). The shift-sum = 0 is the
matching trace condition. Both confirm extremality.

---

## ATTACK 2 — the rank-deficiency argument (A4 §4.2, the flagged softest step).

**Counter-attack:** (a) is Sym²(8) ⊃ 27 really multiplicity 1? (b) does the straddle carry 27 at
mult 3, or could the blocks be ONE irrep of a larger group? (c) do ALL matter modes share the same
5:4 split (only one straddle combination reachable)? If the straddle is effectively 1 irrep or the
matter reaches >1 combination, the rank argument breaks → could be FORCES-OTHER/EINSTEIN.

**OUTCOME: CONFIRMS the negative on all three sub-attacks.**

**(a) Sym²(8) ⊃ 27 multiplicity — CONFIRMED = 1, independently.** Built SU(3) weight multiplicities
from Gelfand–Tsetlin patterns from scratch (`code/adv_su3_mult.py`, integer arithmetic; GT counts
match all irrep dims 1,3,8,10,27). Result, exact:
```
8 ⊗ 8:  27=(2,2) multiplicity 1     Sym²(8):  27 multiplicity 1     Λ²(8):  27 multiplicity 0
Sym²(8) dominant-weight spectrum: (0,0):6, (1,1):3, (2,2):1, (3,0):1, (0,3):1  ⇒ Sym²(8)=1⊕8⊕27 (36=1+8+27).
```
The verdict's 27-once claim is exactly right; 27 lives in the SYMMETRIC square (not Λ²).

**(b) is the multiplicity-3 straddle secretly 1 irrep of a bigger group? — NO.** The matter modes r
genuinely occupy three Kähler blocks: I confirmed pointwise-nonzero (2,0) and (0,2) blocks, with the
pure (2,0)·(2,0) and (0,2)·(0,2) L²-norms = 0 but the (2,0)×(0,2) **cross term nonzero** = 4/135, so
the anti-block norm 8/135 is real (`code/adv_block_norms.py`). The (1,1) and anti copies are distinct
SU(3)-equivariant tensor sectors on the Kähler 4-manifold — there is no larger simple group acting on
CP² beyond the isometry SU(3) (Attack 4 confirms the isometry/holonomy structure), so the three
copies are not artificially split pieces of one irrep. The straddle multiplicity is genuinely > 1.

**(c) do all matter modes share the SAME 5:4 split? — CONFIRMED, universal.** I computed the
(1,1):anti block-norm ratio for **all 8 single Gell-Mann generators** (s01, a01, d1, s02, a02, s12,
a12 + d2) AND **two independent DENSE witnesses** d2=diag(1,1,−2) (detM=−2) and d3=diag(2,−1,−1)
(detM=2) (`code/adv_block_norms.py`, `code/adv_split_universality.py`, exact/Q):
```
EVERY direction: ratio 11:anti = 5/4, normalized split (5/9, 4/9). Including detM≠0 dense matters.
```
So all matter modes realize exactly ONE combination of the three 27-copies (the forced 5:4 `e_grad`).
The matter-reachable subspace of the straddle multiplicity is **rank-1**. Independently, the 8
single-generator residues span a **rank-6** space (verified by a cheap *pointwise* rank, no L²
sweep — `code/adv_q_split.py`-style stack at 3 on-slice points → rank 6 of 7), matching the v32 T3
Gram rank-6 from a completely different method.

**Why the rank argument holds.** On the matter-27, the Einstein operator (Δ_L−2Λ) acts as the clean
scalar 20 (Gate 0: Δ_L r = 32 r on all three blocks ⇒ (Δ_L−2Λ)r = 20r), preserving the 5:4 split.
Q_A (image ⊆ Sym²(8), 27-once) reaches only the single `e_grad` combination of the multiplicity-3
straddle, whereas the Einstein operator is uniform across all three copies. A rank-1-on-multiplicity
operator cannot equal a rank-3-uniform one ⇒ Q_A ≠ (Δ_L−2Λ) as global operators. **CONFIRMED.**
(And even the restricted agreement-on-the-matter-sector is content-free by Attack 1's Schur point.)

---

## ATTACK 3 — Track B completeness. Is there a native Einstein-producer the menu MISSED?

**Counter-attack:** name a NATIVE functional (combination of λ_k's, a metric-dependent moment-map
functional, a spectral zeta/determinant) whose selection traces to algebra/framework data and that
yields (Δ_L−2Λ) WITHOUT being the a₁=∫R√g import. If found → FORCES-EINSTEIN/OTHER.

**OUTCOME: CONFIRMS the negative. Every candidate I could name fails (`code/adv_trackB_menu.py`).**

The clean structural dichotomy that closes the menu: **the Einstein operator (Δ_L−2Λ) is
matter-INDEPENDENT** (acts as 20 on every block, every irrep, regardless of M). Every native spectral
functional produces a stress that is one of:

| Candidate | Selection-traceable? | Produces Einstein? | Verdict |
|---|---|---|---|
| `f(λ₁,…,λ_k)` eigenvalue combo | YES (native λ-tower) | NO — `δλ_n[h] = −⟨dφ_n⊗dφ_n, h⟩` is a gradient-product stress (Berger/ESI); any `f` is a combo of these ⇒ image ⊆ Sym²(8), 27-once, Schur-locked = **Track A in disguise** | not new |
| `∫\|∇φ_M\|⁴`, `∫\|F_moment\|²` (YM-type) | PARTIAL (power/contraction is a free model choice = import-like) | NO — stress is matter-direction-dependent, higher-rank `(Sym²8)^{⊗2}`, not the universal Δ_L | not Einstein |
| `ζ'(0) = −log det Δ` (zeta-determinant) | NO (needs regularization machinery = v21 base-Sakharov import) | At 2-deriv order = the same `∫R√g` (Polyakov/Gilkey) ⇒ **IS a₁** | the import |
| "spectral-costume scalar curvature" | NO (a₁ coefficient universal; no datum picks a₁ over a₀/a₂) | YES but = a₁ | the import |
| a₂ (R², \|Ric\|², \|Riem\|²) | NO | NO — 4-derivative (Bach), not the 2-derivative Einstein operator | out of scope |

Every named functional reduces to (a) Track A (gradient-product, Schur-locked, not Einstein), (b) the
a₁ import in disguise (zeta-det, costume curvature — the dead GST/v21 move), or (c) a
matter-dependent / higher-rank / higher-derivative object that is not the universal Δ_L−2Λ. There is
no gap between these classes. **The menu is complete; no native Einstein-producer exists.**

---

## ATTACK 4 — A1(b) the other way. Is there a STRONGER uniqueness that upgrades Track A to a law?

**Counter-attack:** the verdict says FS is non-unique (class-selection) so λ₁-extremality is not a
law. But is FS the unique metric in a *natural restricted class* — e.g. SU(3)-INVARIANT metrics —
making λ₁-extremality select FS uniquely and upgrading Track A to a genuine law?

**OUTCOME: finds a TRUE fact, but it is VACUOUS as a selection law — CONFIRMS the negative.**

The true fact (`code/adv_su3_invariant_metrics.py`, exact via isotropy irreducibility): **SU(3)-
invariant metrics on CP² = SU(3)/U(2) form a 1-parameter (homothety) family — all homothetic to FS.**
The isotropy rep of U(2) on T_o CP² (real dim 4 = the standard ℂ², complex type) is R-irreducible, so
the invariant symmetric bilinear form is unique up to scale (computed: the space of U(2)-invariant
symmetric 4×4 forms is exactly 1-dimensional). So among SU(3)-invariant metrics, FS IS unique up to
scale. This is the steelman's foothold.

**Why it does NOT crack the verdict (`code/adv_su3_invariant_analysis.py`):**

1. **The uniqueness is vacuous as a selection.** The functional is `λ₁·Vol^{2/n}`, which is
   **scale-invariant**, hence **constant on the homothety class** {c·g_FS}. So *every* invariant
   metric is trivially λ₁-critical within the class — λ₁-extremality selects NOTHING there. What picks
   FS is "assume SU(3)-invariance" + "pick a scale," not the variational principle. Assuming the
   symmetry group of the answer and then noting the answer is extremal is precisely the
   extremality-as-property move (Trap #20): a CONSISTENCY CONDITION, not a derivation.

2. **A genuine law must select FS without assuming the answer's symmetry** — i.e. among ALL metrics.
   There, Kähler-rigidity FAILS (the verdict's A1(b), El Soufi–Ilias / Montiel–Ros / AJK): FS is
   λ₁-extremal but not uniquely pinned. The SU(3)-invariant restriction does not rescue this; it
   pre-selects the answer. **A1(b)'s "class-selection" grading is correct.**

3. **Even if one insisted on the "law" label, it would only fix the BACKGROUND FS metric** and say
   nothing about the matter-coupling operator Q_A, which A4 independently shows is not Einstein. The
   gravity verdict rests on A4 + Track B (Attacks 1–3), which Attack 4 does not touch.

---

## SUMMARY TABLE

| Attack | Target | Strongest finding | Cracks the negative? |
|---|---|---|---|
| 1 | Schur-tautology dismissal (A4) | λ₁=12 SPLITS under the matter mode (shifts {8/5,8/45,−104/135,−8/135}); no single q; none = 20 | **NO — confirms + strengthens** |
| 2 | rank-deficiency (softest step) | Sym²(8)⊃27 once (GT); all 8 gens + 2 dense witnesses give the SAME forced 5:4; residue span rank-6 | **NO — confirms all 3 sub-attacks** |
| 3 | Track B completeness | clean dichotomy: every native functional = Track A (gradient-product) or a₁ import or higher-rank/deriv | **NO — menu complete** |
| 4 | A1(b) other way (uniqueness) | SU(3)-invariant metrics = 1-param homothety (FS unique in-class) — but λ₁·Vol^{2/n} is CONSTANT there ⇒ vacuous selection | **NO — true but vacuous/non-decisive** |

## NET

**FORCES-NOTHING (natively) is SEALED triple-path.** No live positive reading survives a genuine
refutation effort. The single true fact a hostile reading turns up (Attack 4's invariant-class
uniqueness) is vacuous as a selection law (the scale-invariant functional is constant on the class)
and in any case orthogonal to the decision-relevant core (the matter-coupling operator A4). The
Schur-tautology dismissal is not just defensible but *strengthened* (λ₁ degeneracy lifts, so the "q"
the positive case would need is ill-posed). The rank argument — the verdict's flagged softest step —
is robust: the forced 5:4 split is universal across all single generators and both dense witnesses,
so the matter is genuinely rank-1 on the multiplicity-3 straddle while Einstein is rank-3-uniform.
Track B is complete by a gap-free dichotomy. **Gravity is separate; the route parks at fork A.**

The OTHER-vs-NOTHING label is unaffected: both labels agree NOT Einstein, and Attack 1 makes
FORCES-OTHER (calling Q_A "the framework's gravity-shaped law") *less* defensible, not more — the
λ₁-Hessian isn't even a clean operator on the matter sector. I concur with the orchestrator and
verifier: **FORCES-NOTHING** is the honest primary label.

**Confidence: HIGH** on the decision-relevant core (NOT Einstein gravity; no native Einstein-producer).
All four attacks resolved by exact-over-Q computation or airtight analytic argument; two produced
independent positive confirmations of the verdict's own load-bearing claims (Tr(V)=0; forced 5:4).

## Fences (carried, binding)
This adversarial check changes nothing in the physics: NO Einstein / G=κT / dark-matter / geodesic;
κ is not Newton; FS is USED not derived; signature Riemannian (Wall 2 unpaid); does NOT retract
v17–v21; Paper 5 remains the only more-than-nothing result; milestone HOLD for ratification; no v34
self-register.

## Artifacts (exact over Q)
- `code/adv_q_split.py` — Attack 1: the 8 first-order λ₁-shifts (degeneracy lift) + steelman scalars.
- `code/adv_q_split_xcheck.py` — Attack 1 cross-check: weighted Tr(V)=0, shift-sum=0, shifts unequal.
- `code/adv_su3_mult.py` — Attack 2(a): SU(3) GT weight multiplicities; 27 in Sym²(8) = 1, Λ² = 0.
- `code/adv_block_norms.py` — Attack 2(b): (2,0)×(0,2) cross-term structure; 5:4 split per generator.
- `code/adv_split_universality.py` — Attack 2(c): 5:4 universal across all 8 gens + 2 dense witnesses.
- `code/adv_trackB_menu.py` — Attack 3: native-functional candidate analysis (dichotomy closes menu).
- `code/adv_su3_invariant_metrics.py` — Attack 4: SU(3)-invariant metrics = 1-param homothety family.
- `code/adv_su3_invariant_analysis.py` — Attack 4: the uniqueness is vacuous (functional constant on class).
