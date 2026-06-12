# Phase 91 (v31.0-candidate) — The Tensor Probe: Does Matter Source a Genuine Metric Mode?

**Slot 91 / Block B (the Einstein make-or-break). GENUINE FORK (v27/v29/v30 class).
Source: `paper6-lichnerowicz-tensor-probe-prompt.md` (RATIFIED-BY-STANDING-DIRECTIVE).**
Exact over Q / Q(t); octonion engine + 3×3-complex cut rep (guard-locked); u = e₇; cut = CP² = h₃(C_u).

> **STATUS OF THIS FILE.** Sections 1–6 are the orchestrator-staged grounding (the
> machinery, the dimension audit, the battery, the controls, the strategy) — the literature
> the no-web executor cannot fetch, verified by the orchestrator. Sections 7–9 (per-member
> results, payload/certificates, v32 ledger) are filled by the executor/verifier from the
> exact computation. NOTHING here prejudges LIVE vs DEAD; §6 fixes only the *targets* and the
> *method*.

---

## 1. The question, stated as exact linear algebra

The route's gravity ceiling so far is **two scalars** (clock-rate/lapse-class K-data + the
conformal/landscape-class r, G_M data) = Nordström-class, empirically dead as gravity.
**Einstein-FORM needs a rank-2, non-scalar, non-gauge metric mode sourced by matter.** The
16-vs-6 rank wall (v18 Ph77 / v21 Gate 2) relocated to the variety route lives HERE.

On the compact cut (CP², Fubini–Study, Kähler–Einstein), symmetric 2-tensor fields decompose
**L²-orthogonally** (Berger–Ebin 1969 / York):

> **h = h_TT ⊕ δ*ω ⊕ f·g**

- **TT** = divergence-free AND traceless (`δh=0`, `tr_g h = 0`);
- **δ*ω** = the longitudinal/gauge part, `(δ*ω)_{ab} = ½(∇_a ω_b + ∇_b ω_a)`, ω a 1-form;
- **f·g** = conformal (f a function).

The three blocks are mutually L²-orthogonal (Besse, *Einstein Manifolds* 4.57; the conformal
Killing overlap is handled by taking δ*ω trace-free-projected and absorbing its trace into
f·g — the executor's split solver must realize the *orthogonal* version, §5).

**LIVE ⟺ at least one certified rank-2 battery member has TT-residue ≢ 0 at generic M.**
**DEAD ⟺ every member = δ*ω + f·g exactly, with (ω,f) exhibited per member (constructive).**

Over the finite polynomial sectors the split is **exact rational linear algebra per
SU(3)-isotypic block**. No elliptic inversion, no numerics. p = vv† (rank-1 projector);
functions and tensors are low-degree polynomials in v, v̄.

---

## 2. Gate-0 threshold facts (verify in-rep; do NOT import blind)

**(i) The cut metric is Einstein, Λ = λ₁/2 = 6.** Boucetta (arXiv:0712.2830) Lemma 2.1: for
P^n(C) with the FS metric quotient of the unit S^{2n+1}, Ric = 2(n+1) g. For **n=2: Ric = 6g**,
so Λ=6 = λ₁/2 (λ₁=12). Verify Ric = Λg via the recorded curvature/holonomy machinery
(KK, the v17/v22 curvature engine; K = −1/2 sign convention is the cone-Hessian, distinct —
do not conflate). **This normalization matches the codebase exactly**: `variety_moment_doublet`
certifies λ₁(cut)=12, λ₂(cut)=32 = Boucetta's scalar spectrum 4k(n+k)|_{n=2} = 12, 32. So the
Boucetta dimension tables (§4) apply *verbatim* to the certified cut.

**(ii) The v25 moment fields ARE λ₁-eigenfunctions** (recorded; regression). φ_Y(p) = ⟨Y,p⟩
obeys Δ(φ_Y − φ̄_Y) = −λ₁(φ_Y − φ̄_Y), φ̄_Y = ⟨Y,I/3⟩, λ₁=12 (cut). Re-run the
`variety_moment_doublet.mean_curv(cut_families())` regression at Gate 0.

**(iii) Matsushima made concrete (THE WALL, the B1 control with known answer).** On a
Kähler–Einstein manifold, for a λ₁-threshold eigenfunction φ:
- grad φ + iJ grad φ is a **holomorphic** vector field; J grad φ is **Killing**
  (Matsushima; Lichnerowicz–Obata bound λ₁ ≥ 2·(Einstein const) saturated on CP²);
- the **Hessian is pure gauge**: **∇∇φ = ½ L_{grad φ} g = δ*(dφ)**.

Note `L_X g = 2 δ*(X♭)`, so `∇∇φ = ½·2·δ*(dφ) = δ*(dφ)` — and this holds for **any** scalar φ,
not only eigenfunctions (∇∇φ symmetric ⇒ `δ*(dφ)_{ab} = ∇_a∇_b φ`). Matsushima additionally
pins ω = dφ as a *special* (holomorphic-gradient) potential. Consequence used in §6.

---

## 3. The reduction that focuses the verdict (load-bearing)

**Every Hessian is pure gauge by construction.** `∇∇φ = δ*(dφ)` lands in the image of δ*,
hence its TT-residue is **identically zero**, with the explicit constructive certificate

> **ω = dφ,  f = (1/n)·tr_g(∇∇φ) = (1/n)·Δφ**   (n = real dim = 4 on the cut).

Therefore **B1, B2, B4, B5 (all Hessians: ∇∇φ_Y, ∇∇G_M, ∇∇χ, ∇∇R_M) are constructively DEAD
trivially.** This is why the prompt says "Gate 2 (B2,B4,B5) may be all-trivial without deciding
the fork" and "Hessians are longitudinal-by-nature." Boucetta confirms structurally: ∇∇(scalar
level m+2) lands in the **δ*δ* longitudinal block** `φ∘δ*_h∘δ*_h(T^{0,0}_{m+2,m+2})`
(Table VIII, λ=4(m+2)(m+4)) — pure gauge, trace split into conformal.

**The verdict rests ENTIRELY on the bilinear sector (Gate 3): B3 and B6**, which are NOT
Hessians:
- **B3 = s_X⊗s_X = dφ⊗dφ** (traceless part). Identity (verify it):
  `dφ⊗dφ = ½∇∇(φ²) − φ∇∇φ`. The first term is a Hessian (pure gauge); so
  **TT(dφ⊗dφ) = −TT(φ·∇∇φ)** — and `φ·∇∇φ` (a function times a Hessian) is NOT a Hessian and
  CAN carry TT. This is the genuine, non-prejudged question.
- **B6 = T_M(v,w)**, the π_{1/2}M tangent bilinear (the stress-shaped member; v27 |π_{1/2}M|²
  is its trace). The most stress-energy-like object; pin its canonical form at Gate 0 from the
  Jordan structure and FREEZE it.

---

## 4. The dimension audit — the TT targets (Trap #15 anchor)

**External anchor: Boucetta, "Spectra and symmetric eigentensors of the Lichnerowicz Laplacian
on P^n(C)", arXiv:0712.2830, Tables VI–VIII at n=2** (which recover Warner, Proc. R. Soc. Lond.
A 383 (1982) 217, and build on Ikeda–Taniguchi, Osaka J. Math. 15 (1978) 515). Real symmetric
2-tensors on CP² split by the Kähler bigraduation into J-invariant (Hermitian, type (1,1)) and
J-anti-invariant (type (2,0)⊕(0,2)). Eigenvalues below are of the Lichnerowicz Laplacian Δ_L;
they coincide with the scalar 4k(n+k) where indicated.

**Hermitian (1,1) sector — Table VIII (n=2):**

| block | space | eigenvalue | complex dim |
|---|---|---|---|
| **TT** | φ(T^{1,1}_{0,0}) | **12** | **8** |
| conformal f·g | φ(⟨,⟩⊙T^{0,0}_{m,m}) | 4m(m+2) | (m+1)³ : 1,8,27,… |
| longitudinal δ*ω | φ∘δ*_h(T^{1,0}_{m+1,m+2}∩ker i_W) | 4(m+2)(m+3) | (m+1)(m+3)(2m+5) |
| longitudinal δ*δ*(scalar) | φ∘δ*_h∘δ*_h(T^{0,0}_{m+2,m+2}) | 4(m+2)(m+4) | (m+3)³ : 27,… |

> **The ONLY Hermitian-(1,1) TT mode on all of CP² is the single dim-8 multiplet at λ=12**
> (the (1,1)-primitive = the adjoint su(3)). Every higher (1,1) mode is conformal or
> longitudinal. (Consistent with CP² Einstein-rigidity / Koiso — but see Trap #16: this dim-8
> is the lowest Lichnerowicz TT, NOT an Einstein deformation. Do not conflate.)

**Anti-invariant (2,0) and (0,2) sectors — Tables VII, VI (n=2):**

| block | space | eigenvalue | complex dim |
|---|---|---|---|
| **TT (lowest)** | φ(T^{2,0}_{0,2}∩ker δ*_h) | **32** | **27** |
| **TT (lowest, conj.)** | φ(T^{0,2}_{2,0}∩ker δ*_h) | **32** | **27** |
| TT | φ(T^{2,0}_{1,3}∩ker δ*_h) | 48 | 56 |
| TT tower | φ(T^{2,0}_{m+2,m+4}∩ker i_W) | 4(m²+8m+18) | (m+1)(m+7)(m+4) |
| longitudinal | φ∘δ*_h(…), φ∘(δ*_h)²(T^{0,0}_{m+4,m+4}) | … | … |

**The low-level TT targets (where a degree-≤2-in-M battery member can have a residue):**
- **λ=12 : dim-8** real (1,1)-Hermitian primitive TT;
- **λ=32 : dim-27 (2,0) ⊕ dim-27 (0,2)** anti-invariant TT (real 54-dim together).

**The audit (V1/V2(v), MANDATORY before any verdict):** at each battery degree, the executor's
explicitly-spanned gauge image δ*(Ω¹) + conformal {f·g} must have dimension **equal to** the
Boucetta non-TT multiplicity in that isotypic block (total − TT). Under-spanning the gauge or
conformal space is the **fake-LIVE failure mode** (Trap #15): a missed longitudinal generator
masquerades as a TT residue. A TT-residue claim WITHOUT the per-block dimension match is no
claim. The scalar spectrum (12, 32 = Ikeda–Taniguchi 4k(k+2)) and these tensor dims are the
cross-check.

---

## 5. The split solver (V1, lemma grade) + L²-orthogonality

The verdict object for member h is its TT-residue: `h − Proj_{δ*ω⊕fg}(h)`, by exact
orthogonality in the finite sector.

**Two independent realizations (executor uses one as primary; verifier uses the other —
this is the path independence, guard 1/Trap #14 + guard 6):**

**Approach A (direct chart, reuse codebase exact-rational machinery).** Base point E₁₁
(v=(1,0,0)); affine chart v=(1,z₁,z₂); FS metric/Christoffels/covariant Hessian as exact
rational functions of (z,z̄). Build each field f(p(z,z̄)) from the certified formulas; form its
covariant Hessian / the gradient bilinear as a symmetric 2-tensor field over the chart. Span the
gauge image δ*(Ω¹) by {δ*(dχ_a)} for a basis {χ_a} of the relevant scalar-harmonic degrees AND
δ* of the non-exact harmonic 1-forms; span conformal by {χ_a·g}. The TT-residue is the
L²-orthogonal complement. L² inner products = exact FS integrals of monomials in
(z,z̄)/(1+|z|²)^k — exact rationals (Fubini–Study volume / beta-integrals). This reuses the
`family`/`mean_curv` Σᵢ¼ d²/dt² Laplacian idiom and stays guard-locked to the octonion engine
(guard 6 battery, mirror `clock_connection._guard6_battery`).

**Approach B (rep-theoretic, Boucetta-anchored — the independent verifier).** Lift to circle-
invariant symmetric tensors on C³ with harmonic-polynomial coefficients (Ikeda–Taniguchi /
Boucetta §3); apply δ*_h, i_W and read off which Boucetta space (TT vs longitudinal vs
conformal, §4) each isotypic component lands in. The dimension audit is automatic here. A
member is DEAD iff it has zero component in every TT space of §4.

**The frame and the complex structure (from the codebase).** The 4 cut tangent directions at
E₁₁ are the families (2,0)→slot 11, (2,7)→slot 18, (1,0)→slot 19, (1,7)→slot 26
(`variety_moment_doublet.cut_families`, Gram = const·I, orthogonal frame). The Kähler J (e₇↔i)
pairs the real↔e₇ directions: J : (slot 19)↔(slot 26), (slot 11)↔(slot 18). The (1,1) vs
(2,0)+(0,2) split of any symmetric 2-tensor at E₁₁ is the J-invariant vs J-anti-invariant split
in this frame.

---

## 6. THE BATTERY (frozen at Gate 0) + certified-field pointers

All symmetric rank-2 tangent forms of degree ≤ 2 in M buildable from certified objects + the
Jordan product + the C_p/π projections. **Enumerate exhaustively at Gate 0, declare any member
beyond B1–B6 there or never, then FREEZE.** Exact coded formulas (executor: re-read & verify
against the cited file:line — the orchestrator's transcription is a pointer, not gospel):

- **B1 (control, known answer: pure gauge).** ∇∇φ_Y, Y traceless. φ_Y(p)=⟨Y,p⟩ =
  `variety_moment_doublet.inner(Y,p)` (vMD:82). deg 1. The Matsushima wall; (ω,f) = (dφ_Y,
  ¼Δφ_Y) exhibited and re-verified by BOTH paths BEFORE any B2–B6 (Gate 1, Trap #14).
- **B2.** ∇∇G_M. G_M(p)=⟨M#,p⟩ − ¼⟨M,p⟩² (`variety_sourced_field_equation`:~131). deg 2.
- **B3.** s_X⊗s_X = dφ⊗dφ, traceless part. s_X(p)=π_{1/2}^{(p)}(X) = ∇φ_X
  (`variety_spinor_moment`:~92, certified s_X=∇φ_X). deg 2. **Verify the link**
  dφ⊗dφ = ½∇∇(φ²) − φ∇∇φ in-rep ⇒ TT(B3) = −TT(φ∇∇φ).
- **B4.** ∇∇χ. χ(p)=⟨𝒦,D_p⟩ = −(9/2)⟨M,p⟩⟨M,D_p⟩ (`clock_connection`, v30 χ). deg 2.
- **B5.** ∇∇R_M. R_M(p)=⟨M,p⟩² − α⟨M#,p⟩ − β·Tr(M²), (α,β,λ₂) the cut solve
  (`variety_sourced_field_equation`:~369; READ the exact cut α,β,λ₂=32). deg 2.
- **B6 (the stress-shaped member).** T_M(v,w) = the π_{1/2}M tangent bilinear; trace = v27
  |π_{1/2}M|². Pin the canonical symmetric form at Gate 0 from the Jordan structure
  (candidate: T_M(v,w) = ⟨π_{1/2}^{(p)}M ∘ v, w⟩_sym or the Peirce (½)-block bilinear; state
  explicitly, freeze). deg 2.

**Verdict object per member:** exact TT-residue at generic M (symbolic where feasible;
rational-instance battery with exact per-instance verdicts otherwise; co-diagonalization strata
and the v24 diagonal reference carry ZERO weight).

**Expected structure (NOT a prejudgment, for sanity only):** B1,B2,B4,B5 → 0 TT (Hessians, §3).
The fork is decided by **B3 and B6**: do they have a component in the λ=12 dim-8 (1,1)-TT or
the λ=32 dim-27 (2,0)/(0,2)-TT (§4)? For φ_Y with holomorphic gradient (Matsushima), B3's
(2,0) part is ∂φ_Y⊗∂φ_Y (a candidate λ=32 (2,0)-TT) and its (1,1)-traceless part a candidate
λ=12 (1,1)-TT — both finite, exact, decidable. Nothing here forces the sign of the verdict.

---

## 7. Per-member results  *(from the exact computation, executor)*

**Method (the York split solver, V1).** For each member h: solve `h = δ*ω + f·g` over Q by the
**matched-monomial route** (`york_solve`) — build δ*ω + f·g over the COMPLETE certified
gauge+conformal span, bring h − δ*ω − f·g over a common ρ-power, require every (z,z̄)-monomial
coefficient to vanish (a linear system over Q). The complete gauge image is spanned (by linearity
of δ*) by δ* of {φ_A dφ_B (holo-only), φ_A d̄φ_B (antiholo-only)}, φ_A over the 8 su(3) generators
+ identity (φ_id = Tr(p) = 1 ⇒ bare dφ_B and the Killing forms i(dφ−d̄φ) included; holo/antiholo
coefficients INDEPENDENT); conformal = {φ_A φ_B · g}. CONSISTENT ⇒ DEAD; INCONSISTENT ⇒ TT present.

| member | object | deg | TT-residue | certificate / note |
|---|---|---|---|---|
| **B1** (control) | ∇∇φ_Y | 1 | **0 (pure gauge)** | (ω,f) = (dφ_Y, ¼Δφ_Y); york_solve consistent + symbolic reconstruction EXACT (Trap #14) |
| **B2** | ∇∇G_M | 2 | **0 (pure gauge)** | (ω,f) = (dG_M, ¼ΔG_M); universal identity ∇∇f=δ*(df) + 3 exact chart pts |
| **B4** | ∇∇χ | 2 | **0 (pure gauge)** | (ω,f) = (dχ, ¼Δχ); χ=−(9/2)⟨M,p⟩⟨M,D_p⟩ (v30); same universal identity |
| **B5** | ∇∇R_M | 2 | **0 (pure gauge)** | (ω,f) = (dR_M, ¼ΔR_M); R_M cut (α,β,λ₂)=(2/5,3/20,32); same identity |
| **B3** | dφ_M⊗dφ_M | 2 | **≠ 0 (TT present)** | york_solve INCONSISTENT; reduction δ*(φ dφ)=dφ⊗dφ+φ∇∇φ ⇒ TT(B3)=−TT(φ∇∇φ) |
| **B6** | π_{1/2}M tangent stress | 2 | **≠ 0 (= B3)** | PIN: s_M=π_{1/2}^{(p)}M=dφ_M (v28) ⇒ B6=s_M⊗s_M=dφ_M⊗dφ_M; tr_g(B3)=2\|π_{1/2}M\|² (v27) |

**The B6 pin (stated and frozen at Gate 3).** The π_{1/2}M tangent bilinear whose trace is the v27
|π_{1/2}M|² is, using the v28 certification s_M = π_{1/2}^{(p)}M = dφ_M (the moment gradient), the
gradient bilinear s_M⊗s_M = dφ_M⊗dφ_M. The trace identity tr_g(dφ⊗dφ) = 2g^{ab̄}∂_aφ∂_b̄φ = 2|∇φ|²
= 2|π_{1/2}M|² (verified exact, ratio = 2) certifies it. **B6 COINCIDES with B3** — reported
transparently; the same verdict object and the same LIVE result.

### The dimension audit (Trap #15, MANDATORY for LIVE)

Exact rank deficit of B3 against the COMPLETE gauge+conformal image (off-reality-slice modular
point-sampling, two primes cross-checked; independently confirmed by exact-Q rank, no sampling):

| quantity | value | meaning |
|---|---|---|
| dim(gauge+conf image) | **181** (two primes agree) | the complete longitudinal+conformal span |
| **B1-control deficit** | **0** | a Hessian IS in the gauge image (the control fires correctly) |
| **B3 deficit** | **1** (two primes agree) | B3 sticks out by 1 dim ⇒ TT-residue dim = 1 (this M-direction) |
| isotypic type | **λ=12 (1,1)-Hermitian** | (2,0)+(0,2) jointly gauge ⇒ residue in the J-invariant sector |

**TT dim = 1 ≤ Boucetta multiplicity dim-8** (the λ=12 (1,1) primitive, Table VIII) ⇒ the deficit
does NOT exceed the genuine TT multiplicity ⇒ **no under-spanning** (the fake-LIVE failure mode is
excluded). A single su(3)-generator matter direction projects onto a 1-dimensional slice of the
dim-8 multiplet.

**A diagnosed-and-rejected pitfall.** An intermediate audit using **reality-slice** points (z=z̄)
FALSELY reported B3 in-span — the 2-real-dim slice does not separate the 4 independent Wirtinger
monomials (aliasing). The B1 control caught it (spurious nonzero B1 deficits off s01). Fix:
**off-slice** points (z,z̄ independent). All reported numbers use off-slice sampling with the B1
control passing; the exact-Q rank (no sampling) independently gives dim=118 (s01), deficit=1.

**Generic-M robustness (Guard 4).** LIVE on the sparse single-generator s01, on a dense generic M
(all 8 params nonzero, off the diagonal stratum), and on a second dense M — york_solve(B1)
consistent and york_solve(B3) inconsistent in every case. Direction-independent; co-diagonalization
strata and the v24 diagonal reference carry zero weight.

## 8. Verdict, payload, scope

**VERDICT = LIVE.** `verdict({B2:0, B4:0, B5:0, B3:1, B6:1}) = ('LIVE', ['B3','B6'])`.

**Payload.** Matter forces a rank-2 transverse-traceless deformation of the cut metric — the
**λ=12 (1,1) Hermitian primitive** sourced by the bilinear of the matter's tangent moment
s_M = dφ_M. The v27–v30 two-scalar (Nordström-class) gravity ceiling is broken at the
λ₁-threshold: the program's first matter-forced TENSOR structure. The TT residue lives exactly at
the moment fields' own threshold (λ₁=12), in the unique low-level (1,1) TT mode on CP².

**One sentence (which world).** On the compact Kähler–Einstein cut, the certified matter bilinear
B3 = dφ_M⊗dφ_M (= the pinned π_{1/2}M tangent stress B6) carries a nonzero transverse-traceless
residue in the λ=12 (1,1) Hermitian sector — **matter sources a genuine metric tensor mode
(LIVE)**; the Einstein selection law (Block C) remains open and is not claimed.

**Scope / fence (binding).** LIVE = "a matter-sourced tensor MODE exists" — NOT "Einstein gravity
derived". Block C (the selection law, the κ value) NOT claimed. No Einstein-equation / Newton-
constant / G=κT / dark-matter / geodesic language. Frozen FS geometry USED, not derived. The
v18/v20 MM corpse stays buried (BASE deformation complex, not a fiber spacetime connection). The
v18 Ph77 / v21 16-vs-6 rank wall is a Block-C statement (full nonlinear G[g]=κT+Λg with one global
(κ,Λ)); LIVE is the strictly weaker upstream existence of a TT mode — not in tension.

## 9. v32 ledger (Gate 5, exploratory, NO claims — priced only)

IF LIVE (this branch):
- **The sourced Lichnerowicz response law.** Does the λ=12 (1,1) TT-part satisfy a Δ_L-type
  equation (Δ_L h_TT = source) with the v26 source content (TrM², R_M)? The λ=12 eigenvalue of
  the Lichnerowicz Laplacian on the (1,1) primitive is the natural left-hand side. PRICE: this is
  a NEW computation (the Δ_L action on the extracted TT mode vs the v26 source); not done here.
- **The lapse/00 assembly.** Einstein-FORM needs the scalar (lapse/conformal) + the new tensor
  pieces assembled into the 00 and ij blocks of a 4d G_{μν}. PRICE: requires the cut → 4d-slice
  embedding (the v17/v18 soldering), NOT the CP² deformation complex alone.
- **The OP² extension.** OP² = h₃(O) is the full base; it is **NOT Kähler** (Spin(9) holonomy, no
  global complex structure — cf. v19 no-intrinsic-orientation). The Matsushima/λ₁-threshold
  mechanism is Kähler-specific; the OP² tensor-harmonic content (Spin(9) isotypic) differs.
  PRICE: a separate Spin(9) bookkeeping; do NOT assume the CP² LIVE lifts to OP².
- **The κ / selection law (Block C).** Untouched. Whether a single global κ closes the full
  nonlinear Einstein equation is exactly the v18 Ph77 / v21 wall — relocated upstream of, not
  resolved by, the TT-existence result.

---

### References (orchestrator-verified, for the no-web executor)
- M. Boucetta, *Spectra and symmetric eigentensors of the Lichnerowicz Laplacian on P^n(C)*,
  arXiv:0712.2830 (Tables VI–VIII at n=2 = CP²). **The dimension-audit anchor.**
- A. Ikeda, Y. Taniguchi, *Spectra and eigenforms of the Laplacian on S^n and P^n(C)*, Osaka J.
  Math. 15 (1978) 515. (Scalar spectrum 4k(n+k); 1-form eigenforms as SU(n+1)-modules.)
- N. P. Warner, *The spectra of operators on CP^n*, Proc. R. Soc. Lond. A 383 (1982) 217.
- M. Berger, D. Ebin, *Some decompositions of the space of symmetric tensors on a Riemannian
  manifold*, J. Diff. Geom. 3 (1969) 379. (The TT ⊕ δ*ω split.)
- Y. Matsushima (holomorphic gradients of λ₁-eigenfunctions on KE manifolds); A. Besse,
  *Einstein Manifolds* §4.57 (the orthogonal York split), §12.98ff (Koiso rigidity, Trap #16).
