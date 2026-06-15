# Phase 95 / v35.0 — AREA-PER-BIT KILL-TEST — INDEPENDENT VERIFICATION

> Independent verifier (gpd-verifier), 2026-06-14. Charge: verify the load-bearing identities behind
> the **DEAD-FISHER / fork A** verdict. Built from the prompt's definitions, NOT from the existing
> `code/area_per_bit.py` driver (no driver code was read into the verification path). Exact over ℚ / ℚ(i)
> by point evaluation at ≥3–5 rational + Gaussian-rational chart points per direction. NO generic-M
> symbolic `cancel`/`simplify` over a multiparameter matrix (the forbidden stall). Three independent code
> paths for the load-bearing identity. No state edits, no commits.
>
> Verifier scripts: `/tmp/verify95_engine.py` (engine + §9 anchor), `/tmp/verify95_charges34.py`
> (charges 3,4), `/tmp/verify95_charge1_final.py` (charge 1), `/tmp/verify95_charge2_final.py` (charge 2),
> `/tmp/verify95_qgt_xcheck.py` (independent operator-form QGT cross-check).

---

## VERDICT OF THE VERIFICATION: ALL FIVE CHARGES PASS. CONFIDENCE: **HIGH** (math); MEDIUM (the one interpretive leap, inherited).

The three symbolic identities that carry the DEAD-FISHER verdict are **independently confirmed** —
re-derived from the prompt definitions in a clean engine, on a wider point set than §9, and (for the
load-bearing A_ii ≡ Var) by a second, chart-free operator-theoretic code path. The literature anchor
(Provost–Vallée 1980: FS = Re(QGT) = quantum Fisher metric on pure states) is verified against the
primary citation. Off-faithfulness clears the v23-death concern decisively.

---

## CHARGE-BY-CHARGE

### Charge 1 — A_ii ≡ Var  (FS metric-trace area = quantum variance): **PASS** (INDEPENDENTLY CONFIRMED)

**Object computed.** A_M^(ii)(p) = g^{j̄i} ∂_i φ_M ∂_{j̄} φ_M = |∇φ_M|²_g, with the potential-normalized
Fubini–Study metric g_{ij̄} = ∂_i∂_{j̄} log ρ, ρ = 1+|z₁|²+|z₂|², φ_M = (v†Mv)/(v†v), v=(1,z₁,z₂)ᵀ.

**Analytic argument (one line, Provost–Vallée Fisher fact).** On CPⁿ with normalized state |ψ⟩, the QGT
is Q_{ij̄} = ⟨∂_iψ|(1−P)|∂_jψ⟩; its real part is the FS metric g, and the contraction
g^{j̄i} ∂_i⟨M⟩ ∂_{j̄}⟨M⟩ = ⟨ψ|M(1−P)M|ψ⟩ = ⟨M²⟩ − ⟨M⟩² = Var. So A_ii ≡ Var identically.

**Numerical confirmation.** Exact over ℚ at **5 points × 4 directions = 20/20** (s01, a01, d1, gen at
z=(1+2i,−1+i), (−1,2−3i), (½,⅓), (2,−½), (1+i,½−i) — 3 complex + 2 real per direction).
Examples: d1@(1+2i,−1+i): A_ii=1/2=Var; gen@(1+2i,−1+i): A_ii=27/16=Var; s01@(½,⅓): A_ii=909/2401=Var.

**Skeptic's note (a real pitfall caught and resolved).** My *first* attempt used the contraction
`g^{ij̄}` with the naive transpose `ginv[i,j]` and FAILED at every complex point (passed only at real z,
where the inverse metric is symmetric). This is exactly the conjugation/index hazard the prompt's
flag #2 warns about. Isolating it (`/tmp/verify95_charge1_diag.py`) showed the correct Hermitian
contraction is `g^{j̄i} = ginv[j,i]` (≡ conj(ginv[i,j])), pairing the holomorphic index with the
antiholomorphic index; the diagnostic also verified ∂_{j̄}φ = conj(∂_jφ) on the real slice (required for
Hermitian M). With the correct contraction the identity holds at ALL points. **The "failure" was a
verifier convention bug, not a flaw in the identity** — and its resolution independently confirms the
prompt's claim that the i↔−i / index handling is the delicate piece.

### Charge 2 — A_iii ≡ Var  (KKS symplectic gradient-norm = variance): **PASS** (INDEPENDENTLY CONFIRMED)

**Object computed.** |X_{φ_M}|²_ω with the Hamiltonian/symplectic gradient X_φ = J∇φ. In holomorphic
coords J acts as +i on (1,0) and −i on (0,1); raised gradient Y^i = g^{j̄i}∂_{j̄}φ (convention B,
pinned below), X^i = +iY^i, and the g-norm Re(g_{ij̄}X^i conj(X^j)).

**Analytic argument (the Kähler isometry — the collapse that makes the canonical area the Fisher metric).**
On a Kähler manifold ω(·,·)=g(J·,·) and J is a g-isometry: |J∇φ|²_g = g(J∇φ,J∇φ) = g(∇φ,∇φ) = |∇φ|²_g.
Concretely the J factors multiply as (+i)·conj(+i) = (+i)(−i) = +1, so the symplectic norm is
IDENTICAL to the metric-gradient norm ⇒ A_iii ≡ A_ii ≡ Var. The symplectic "area" collapses onto the
same Fisher/QGT-real metric.

**Numerical confirmation.** Exact over ℚ at **20/20** points: at each point |X_φ|² = |∇φ|² = Var.
Examples: d1@(1+2i,−1+i): |X|²=1/2; gen@(1+i,½−i): |X|²=540/289=Var; a01@(−1,2−3i): |X|²=2/15=Var.

**Skeptic's note (second pitfall caught and resolved).** Same complex-point failure recurred from a
raised-index convention error in the (0,1) gradient. Diagnosing (`/tmp/verify95_charge2_diag.py`) showed
the correct raising is Y^i = ginv[j,i]·∂_{j̄}φ (convention B), giving |∇φ|²_g (as 2·Re of the
g_{ij̄}Y^iconj(Y^j) pairing) = 1, half = 1/2 = Var at the test point. With convention B the symplectic
construction with explicit J factors matches Var at all points. **Again a verifier convention bug, not
an identity flaw.** This corroborates the driver's flag #2: the i→−i flip on the genuine imaginary unit
(matter Hermitian off-diagonals + the J-factor) is required and legitimate; it is NOT sympy
`conjugate()` on the independent Wirtinger symbols.

### Charge 3 — G_M = Var + ¾⟨M⟩² − ½Tr(M²)  (entropy-response decomposition): **PASS** (INDEPENDENTLY CONFIRMED)

Point-checked exact over ℚ at **5 points × 4 directions = 20/20**, residual G_M − (Var+¾⟨M⟩²−½TrM²) ≡ 0
at every point. Confirmed G_M is **NOT ∝ Var**: G_M/Var = {−5/8, −1513/5904, −19/92} for d1 across
P0/Pa/Pb (and {−3/4, −45/16, −5} for gen) — genuinely non-constant. So R = Var/|Var+¾⟨M⟩²−½TrM²| does
shear, and the shear is exactly the relative-entropy correction (¾⟨M⟩²−½TrM², a state-space quantity).

### Charge 4 — OFF-FAITHFULNESS (∇S_face ≠ 0; G_M genuinely varies with p): **PASS** (INDEPENDENTLY CONFIRMED)

G_M(p) takes **5 distinct values across 5 points for all 4 directions** (e.g. d1: −5/16, −13/15,
−1513/9604, −19/147, −89/289). The face-purity r = q/m² for the structured state X = I/3 + εM (ε=1/10)
likewise varies in p (d1: {451/1849, 198646/808201, 301/1216}). I additionally confirmed the *numerator*
Var(p) also varies (4 distinct values/direction), so BOTH sides of R are genuinely p-dependent.

**Disposition of the v23 concern (my specific charge).** The v23 death occurred AT the maximally-mixed
faithful point (the I/3-type fiber center) where ∇S = 0 by symmetry — a point-specific vacuity. On the
CP² variety (pure states) here, Var(p) and G_M(p) are genuinely non-constant rational functions of p.
Therefore the Fisher collapse A_M ≡ Var is **NOT** the constant-by-symmetry value, and the test is **NOT
vacuous**. **The v23-death concern is CLEARED**: the DEAD-FISHER verdict arises from a *live, varying*
test that nonetheless reduces the canonical area to a state-space (Fisher) object — a strictly sharper
and more defensible closure than the v23 ∇S=0 vacuity.

### Charge 5 — §9 ground-truth spot check: **PASS** (INDEPENDENTLY CONFIRMED)

All **6/6** §9 rows reproduced exactly over ℚ with the independent engine:

| M | point | ⟨M,p⟩ | Var=A_M | G_M | R=A/|G| | match |
|---|---|---|---|---|---|---|
| d1 | P0 | −1/2 | 1/2 | −5/16 | 8/5 | ✓ |
| d1 | P2 | 0 | 2/15 | −13/15 | 2/13 | ✓ |
| s01 | P0 | 1/4 | 11/16 | −17/64 | 44/17 | ✓ |
| a01 | P0 | 1/2 | 1/2 | −5/16 | 8/5 | ✓ |
| gen | P0 | 1/4 | 27/16 | −81/64 | 4/3 | ✓ |
| gen | P2 | −8/5 | 26/25 | −1/25 | 26 | ✓ |

R is verifiably NOT constant (8/5, 2/13, 44/17, 4/3, 26 …), so the literal DEAD-CONSTANT reading fails;
the shear is Var/|G_M| = Fisher/(relative-entropy), state-space. The gen@P2 R=26 is the near-zero-G_M
artifact (denominator approaching its zero locus), correctly flagged as a non-shear.

---

## INDEPENDENT CROSS-CHECK (strengthens charge 1/2 beyond the chart)

The load-bearing identity A_ii ≡ Var was re-derived a THIRD way via the operator form of the QGT/Fisher
fact, **with no Kähler chart and no Wirtinger derivatives** (pure 3×3 linear algebra over ℚ(i)):
⟨ψ|M(1−P)M|ψ⟩ = Var. PASS at all 20/20 points. So:

**A_ii (chart metric-trace) = ⟨ψ|M(1−P)M|ψ⟩ (operator QGT) = Var — triple agreement.**

This rules out the possibility that A_ii ≡ Var is an artifact of my chart/convention choices: the equality
is the genuine, chart-independent Provost–Vallée Fisher identity.

---

## LITERATURE ANCHOR (verified)

**J. P. Provost and G. Vallée, Commun. Math. Phys. 76, 289 (1980).** Verified via web search: Provost and
Vallée first derived the complex quantum (geometric) metric, showing its **real part is the gauge-invariant
Riemannian Fubini–Study metric** and its **imaginary part is the symplectic (Berry) structure**. This is
exactly the decomposition the verdict rests on: every FS-canonical local area is a contraction of Re(QGT) =
the quantum Fisher metric. Both A_ii (the metric-trace) and A_iii (the symplectic norm, collapsed by the
Kähler isometry) reduce to the same Fisher object Var = the quantum Fisher information of φ_M — a
STATE-SPACE quantity, the v17-corpse family. Source:
https://link.springer.com/article/10.1007/BF02193559 (Commun. Math. Phys. 76, 289).

---

## DOES OFF-FAITHFULNESS CLEAR THE v23-DEATH CONCERN?

**YES, decisively.** The v23 death was a point-specific vacuity (∇S = 0 at the maximally-mixed faithful
center, where everything is constant by F₄-symmetry). Here, on the CP² pure-state variety:
- G_M(p) varies (5 distinct values / direction across the test points), so the bits side has genuine gradient;
- Var(p) = A_M(p) also varies (4 distinct values / direction), so the area side has genuine gradient;
- the face-purity r=q/m² of the structured state X=I/3+εM varies in p.

So the test is run on genuinely *off-faithful, structured* states with a live gradient — Bug-guard 4 is
cleared, and the DEAD-FISHER verdict is NOT the v23 death sneaking back in. The verdict is sharper than
v23: the area is a *varying* object that is nevertheless *identically the Fisher metric*, so its shear
cannot certify a geometric rate.

---

## SKEPTIC'S RESIDUAL CONCERNS (and why they do not move the verdict)

1. **The two convention bugs I hit** were in MY verification scaffolding, not the claimed identities; once
   the Hermitian metric contraction (g^{j̄i}, charge 1) and the (1,0)-gradient raising (convention B,
   charge 2) are fixed, both identities hold at every complex point, and the chart-free operator
   cross-check confirms A_ii≡Var independently. The identities are robust. (They also independently
   reproduce the driver's flag-#2 warning about the i→−i piece — a point in the driver's favor.)

2. **The one interpretive leap is genuinely interpretive, not computational.** "A Fisher-object area
   certifies that R's shear is NOT a geometric rate" is a *reading* of the exact math, resting on the
   Provost–Vallée FS=Re(QGT) identification + the program's pre-registered Fence 3 / Bug-guard 3. The math
   (A_M ≡ Fisher; G_M = Fisher + non-proportional correction; R shears state-space-only) is exact and
   HIGH-confidence. The leap is the de-risked, pre-registered expected landing; I concur with the driver's
   self-assessed **MEDIUM** on this single step (it is sound and well-anchored, but it is an interpretation
   of "no native geometric area independent of the state-space information geometry," not a theorem that
   no such area *could* be imported — importing one is precisely fork A).

3. **LIVE-TENSOR structural preclusion confirmed in spirit.** A_M^(ii) is literally the metric *trace* of
   the v31 metric-mode dφ_M⊗dφ_M, so by construction it carries the scalar/trace part, never the TT part.
   I did not need to reach G2; the Fisher gate fires first. (I did not independently re-verify the v31/v32
   TT-norm anchors — out of scope for the four load-bearing identities, and not on the decisive path.)

4. **Fences honored.** Nothing in the verified math derives gravity, Einstein's equation, or Newton's G;
   FS is used not derived; signature is Riemannian (Wall 2 unpaid). The verification is consistent with the
   fences. (These are scope statements, not computations; I confirm the verdict text does not overclaim.)

---

## CONFIDENCE: **HIGH** on the mathematics; **MEDIUM** on the single interpretive step (inherited, concurred)

- **HIGH** that the three symbolic identities hold (A_ii≡Var, A_iii≡Var, G_M=Var+¾⟨M⟩²−½TrM²): exact over
  ℚ/ℚ(i) at 20 points/identity across 4 directions including complex points, plus an independent chart-free
  operator-form confirmation of the load-bearing one, plus clean one-line analytic arguments for each.
- **HIGH** that R shears and is not literally constant (§9 reproduced 6/6), and that the shear is
  Fisher/(relative-entropy), i.e. state-space.
- **HIGH** that off-faithfulness clears the v23-death concern (numerator AND denominator genuinely
  vary in p on the pure-state variety).
- **MEDIUM** only on the interpretive conclusion that a Fisher-object area ⇒ no native geometric rate ⇒
  fork A — exactly the driver's own self-assessment (flag #5), which I independently reach and endorse.

**Overall: the DEAD-FISHER / fork A verdict is mathematically sound and well-anchored. I find no error
that moves the verdict.** The independent reproduction (different engine, wider points, third operator-form
path, verified literature anchor) raises confidence in the load-bearing identities to HIGH.

Verification report: `/Users/ehrlich/scratch/get-physics-done/derivations/95-VERIFICATION.md`
