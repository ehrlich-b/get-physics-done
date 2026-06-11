# 87 — GATE-3 VERIFICATION (independent): THE FORK — Q_M tuple-determinacy, the certificate hunt, the law

**v27.0 Phase 87 — independent verifier. A GENUINE FORK resolved to LIVE. Exact over
Q / Q(t). I tried HARD to break LIVE and could not. CONFIDENCE: HIGH.**

The fork: on the parallel locus (off trivial strata), is `λ` a state-universal function
of the frozen tuple `(a, c, c_R, TrM², detM)`? By the (verified, Gate-2) reduction
`λ² = Q_M/(2c_R(1−c_R))`, this reduces to: **is `Q_M := |π_{1/2}(M#−½aM)|²`
tuple-determined?** LIVE ⇔ yes (state the law P); DEAD ⇔ a certificate pair (two
on-locus configs, same tuple, different λ, i.e. different Q_M).

---

## D3 — Q_M IS tuple-determined (the law), proven symbolically through Tier C

Verified independently of BOTH drivers (`/tmp/v87_scratch.py` STEP 4 with the
executor's `sharp`; `/tmp/v87_hard.py` STEP B with the literal-adjugate `sharp_adj`):
the full-26-param symbolic `Q_M` admits the degree-4 tuple ansatz
`A(TrM²)² + B c² + C·a·detM + D a²TrM² + E a⁴ + F a²c + G c·TrM²` with an **identically
zero** residual and the unique coefficients

> **{A:0, B:−2, C:0, D:1/4, E:−1/2, F:5/2, G:−1}**

identical on Tier A (cut, 8 params), Tier B (one octonion block, 10 params), Tier C
(full 26 params), and identical across all THREE independent sharp constructions. The
fit factors exactly:

> **`2 Q_M = (½TrM² − a² + c)(a² − 4c)`**, equivalently
> **`4 c_R(1−c_R) λ² = (½TrM² − a² + c)(a² − 4c)`**,
> i.e. **`c_R(1−c_R) λ² = −|π_{1/2}M|² · G_M(p)`** with `G_M = c − a²/4 ≤ 0` (eigengap
> form) so `λ² ≥ 0`.

Confirmed pieces (`/tmp/v87_final.py` STEP 1): `G_M(E₁₁) = c − a²/4` exactly; and
`2Q_M = −4·(½TrM²−a²+c)·(c−a²/4)` exactly. **`detM` has coefficient C = 0 — the
multiplier is cubic-norm-blind** (the octonion-direction data that v24 proved the
landscape resolves does NOT leak into λ beyond the quadratic tuple).

**Anchor specialization** (`/tmp/v87_final.py` STEP 4): the law at `(1,0,4,1)` gives
`(½·4 − 1 + 0)(1 − 0) = 1`, matching `4c_R(1−c_R)λ² = 2Q_M0 = 1`. The closed-form P is
thus verified to specialize to the hand anchor, as the prompt requires.

---

## The certificate hunt (the DEAD test) — EMPTY after a real effort

A single matched-tuple pair with different Q_M would flip the verdict to DEAD. I hunted
hard, by four independent strategies, importing neither driver:

| strategy | construction | matched-tuple pairs | certificates |
|---|---|---|---|
| A (random sparse) | 4000 traceless M, sparse octonions, bucket by tuple | 461 | **0** |
| A′ (random DENSE) | 20000 traceless M, all-8-comp octonions | 0 collisions* | **0** |
| B (targeted on anchor tuple) | x₃=e_k (k=0..7), x₂=e_k, x₃=(3/5,4/5) | all share tuple (1,0,4,1) | **0** (all Q_M = 1/2) |
| C (J₀-support trap) | off-diag placed in x₁ (the J₀ block) | tuple → (1,−1,4,−1) ≠ anchor | n/a (correctly excluded) |
| D (constructed same-tuple, diff direction) | swap x₂↔x₃, sign-flip x₃ direction | 7 genuine | **0** |
| E (perm-direction matched) | 8000 with permuted octonion units | 8000 | **0** |
| F (e₁-line vs e₂-line, nonzero cross-term) | shared-unit triples on different associative lines | matched | **0** (Q_M equal) |

(*dense random points essentially never collide on a 5-dim tuple — itself consistent
with LIVE: the generic tuple-fiber is the stabilizer orbit, dimension exactly marginal.)

The most decisive constructed pair (`/tmp/v87_final.py` STEP 3): `M_D` (all off-diag
along the e₁ line) and `M_E` (all along the e₂ line) — **same tuple
`(1/3, −19/48, 2369/1800, −491/3600)`, same `Q_M = 1037/8100`**. These are genuinely
non-stabilizer-related (different associative octonion lines), exactly the kind of pair
the prompt asked for, and Q_M is identical.

The J₀-support trap (Strategy C) was the most promising DEAD candidate — putting the
off-diagonal in x₁ (the J₀ Peirce block, which π_{1/2} kills) gives `dG = 0`. But those
matrices land on tuple `(1,−1,4,−1)`, **not** the anchor `(1,0,4,1)`: the tuple records
`c = β·γ − |x₁|²`, which moves when x₁ carries the entry. So the trap closes — there is
no same-tuple, π-killed certificate.

The executor's verdict that "no certificate pair can exist" is therefore not merely an
absence-of-evidence claim: it follows from the **exact symbolic identity** for Q_M
(same tuple ⇒ same a,c,TrM² ⇒ same `(½TrM²−a²+c)(a²−4c)` ⇒ same Q_M), and the empty
hunt independently corroborates it on genuinely diverse octonion directions.

---

## Adversarial: is the LIVE mechanism a genuine identity or an over-rich fit?

Three independent guards confirm the fit is a true identity, not noise-fitting:

1. **Residual identically zero, not least-squares** (`/tmp/v87_scratch.py` STEP 4,
   `/tmp/v87_hard.py` STEP B): `sp.solve` of the coefficient system + a final
   `expand(residual.subs(sol)) == 0` over all 26 symbols.

2. **Every used monomial is necessary** (`/tmp/v87_scratch.py` STEP 6,
   `/tmp/v87_hard.py` STEP F): dropping any of B, D, E, F, G makes the fit FAIL. So the
   7-monomial ansatz is not redundantly over-rich — it is exactly the needed span (with
   A and C genuinely zero, not fitted-away).

3. **The hidden alignment invariant is itself tuple-forced — and not masked**
   (`/tmp/v87_hard.py` STEP F). The prompt's central worry: does Q_M secretly depend on
   a mixed-alignment invariant `J := ⟨π_{1/2}M, π_{1/2}M#⟩` that is NOT in the tuple? I
   computed J symbolically and found **J = −2·a·c + 2·detM** — itself tuple-determined,
   with both monomials necessary (dropping either fails). So the alignment data the fork
   could have hidden is *forced by the tuple on the whole space*; Q_M's clean 7-monomial
   fit is a real identity, with nothing swept under an over-rich basis. **This is the
   single deepest confirmation of LIVE**: the very invariant that would have produced a
   certificate is itself a function of the tuple.

---

## Independent batteries (direct Q_M vs the law)

- This verifier, my own dense-octonion builder (`/tmp/v87_battery.py`): **120/120**
  rational traceless M satisfy `Q_M(direct) == Q_law(tuple)` exactly, with `detM` passed
  but unused (cubic-norm-blindness reproduced).
- Executor `_instance_battery`: **44/44** (re-run). This is a genuine independent check
  (direct `normsq(dG(M))` vs the tuple-polynomial), not a tautology.
- Verifier-driver matched-tuple hunt: 5/5 PASS (its 5 pairs all share Q_M).

---

## verdict() non-hardwiredness

`verdict()` is a deterministic ladder, not a literal (`/tmp/v87_final.py` STEP 5,
matching the executor's `_verdict_selftest`):
`verdict(T,T,False)=LIVE`, `verdict(T,T,True)=DEAD`, `verdict(T,False,False)=OPEN-per-tier`.
DEAD is reachable; LIVE is produced only by (Tier-C-exact ∧ no-certificate). Had any of
my batteries or hunts produced a certificate, the same code would have returned DEAD.

---

## Language fence (guard #7)

Clean. The only "Einstein"/"geodesic"/"Newton" tokens in the executor, verifier,
RESEARCH, and VERDICT are the fence declarations and the Jacobson citation marked
"STRUCTURAL analogy only." λ is consistently called a multiplier, NOT a coupling; the
canonical geometry (λ₁=48/12, λ₂) is FROZEN spectral data; no `G=κT`, no dark-matter,
no force/geodesic language. Signature left OPEN.

---

## GATE-3 RESULT: **LIVE — CONFIRMED** (HIGH confidence)

`Q_M` is tuple-determined by an exact symbolic identity through Tier C (full 26-param M
on OP²), verified on three independent `sharp` constructions and three independent
`π_{1/2}` constructions; the certificate hunt is EMPTY after a genuine effort across
sparse, dense, constructed, permuted, and associative-line-matched non-stabilizer pairs;
the fit is necessary (not over-rich) and the worrisome alignment invariant `J` is itself
tuple-forced (`J = −2ac + 2detM`); the reduction is metric-free and the denominator
tuple-determined (Gate 2). The exact law

> **`4 c_R(1−c_R) λ² = (½TrM² − a² + c)(a² − 4c) = −4|π_{1/2}M|²·G_M`**

stands, with `detM` absent (cubic-norm-blind). **We are in the LIVE world: the scalar
sector closes into a local balance law.**

**No certificate found. The LIVE verdict is confirmed.**

Single caveat (cosmetic, non-blocking): the `|π_{1/2}M|²` symbol in the factored prose
denotes the half-norm `|x₂|²+|x₃|²` (= ½ of the trace-form `Tr((πM)∘(πM))`); the
reduction itself uses one consistent norm top-and-bottom, so the verdict is unaffected.
Worth one clarifying sentence in the write-up.
