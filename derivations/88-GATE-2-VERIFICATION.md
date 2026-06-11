# 88 — GATE-2 VERIFICATION (independent): E1 (identification), E2 (zeros = eigenframe), and the Gate-0 v22 dictionary

**Phase 88 / v28.0 (J5-on-the-variety, step 4). Independent verifier. Exact over Q / Q(t).
Three code paths agree: executor `variety_spinor_moment.py` (14/14), eigenprojector
`variety_spinor_moment_verify.py` (9/9), and a FROM-SCRATCH check `/tmp/v28_indep_check.py`
(18/18) importing NEITHER driver (its own octonion table, h₃(O) matmul, Jordan product, and
Peirce-½ projector).**

The object: `s_X(p) := π_{1/2}^{(p)}(X) ∈ J_{1/2}(p) = T_p(variety)`, the Peirce-1/2 projection
of state X at a rank-1 idempotent p. `⟨A,B⟩ = Tr(A∘B)`, `X# = X×X` the Freudenthal adjoint.

---

## Method (independence)

I rebuilt the arena from scratch:
- **My own octonion product** `omul` from a Fano table I reconstructed empirically from the
  engine's `oct_mul` (so it is provably the SAME algebra: `e_i²=−1` all i, `e_i e_j=−e_j e_i`
  i≠j — both confirmed). My `omul`, `jordan`, `Tr`, `inner` are independent code.
- **Reconciliation**: MY Jordan product == the engine Jordan product entrywise on a rational +
  octonionic battery — so any cross-path agreement is meaningful, not a different algebra.
- **THREE independent Peirce-½ constructions** that must agree at E₁₁ for symbolic X:
  (A) entry-extraction (off-diagonal (i,·) block); (B) the Jordan eigenprojector
  `P_{1/2}=4L_p(I−L_p)`; (C) the complement `P_{1/2}=I−P_1−P_0`,
  `P_1=2L_p²−L_p`, `P_0=2L_p²−3L_p+I`. **All three agree** (symbolic X). This defeats the risk
  that the executor (entry-extraction) and verifier (eigenprojector) share a single hidden bug.
- **Product-order trap (guard #5):** independently, `Re((x₂x₁)x₃)=−1 ≠ Re((x₁x₂)x₃)=+1` for
  x₂=e₁, x₁=e₂, x₃=e₄ — genuine non-associativity; my `omul` reproduces the trap. The det₃ SSOT
  uses `(x₂x₁)x₃`; my independent `det₃` matches.

---

## E1 — the identification: s_X = dφ_X. **CONFIRMED (HIGH).**

**Re-derived (one-line Peirce proof).** For a tangent v ∈ J_{1/2}(p) (= T_p of the variety),
`⟨X,v⟩ = ⟨π_1 X + π_{1/2} X + π_0 X, v⟩ = ⟨π_{1/2} X, v⟩` by Peirce orthogonality (v has only a
½-part). Hence the gradient of φ_X(p)=⟨X,p⟩ in the trace metric IS π_{1/2}^{(p)}(X) = s_X. □

**Independently verified (my from-scratch path):**
- `d/dt ⟨X, p(t)⟩|_0 == ⟨s_X(E₁₁), p′(0)⟩` along ALL 16 of MY families (I built my own rank-1
  idempotent families `p(t)=vv*`, including a genuinely octonionic e₃-direction family, each
  certified `p∘p=p`, `Tr p=1` exact/Q(t)), symbolic X — **PASS**.
- **Norm formula** `‖s_X‖²_tr == TrX² − a² − (TrX−a)² + 2c` (a=⟨X,p⟩, c=⟨X#,p⟩) on a 3-state
  rational, **non-traceless** battery (MY computation, MY `sharp`) — **PASS** (3/3). Both other
  paths also confirm it for fully symbolic X.
- **Direction NOT scalar-determined:** I exhibited two states X₁ (x₃=e₀) and X₂ (x₃=e₁) with
  **equal** (a, c, TrX², det₃X) at E₁₁ but **different** s_X direction — **PASS**. The scalars
  miss the direction; this is the genuine v24 direction-resolution content.

## E2 — zeros = the eigenframe. **CONFIRMED (HIGH).**

**Re-derived.** `s_X(p)=0 ⟺ π_{1/2}^{(p)}(X)=0 ⟺ X ∈ J_1(p)⊕J_0(p) ⟺ [L_X,L_p]=0` (X and p
share an eigenframe). For distinct spectrum the only compatible rank-1 idempotents are the three
spectral projectors {p₁,p₂,p₃} — exactly three isolated zeros.

**Independently verified — and F₄-covariance made EXPLICIT (the load-bearing part):**
- Diagonal control: `s_X(E_ii)=0`, i=0,1,2 — **PASS**.
- **GENUINELY OCTONIONIC ROTATED FRAME (the decisive check).** I built a Jordan frame
  {p₁,p₂,p₃} from rational unit kets with an **e₃** component:
  v₁=(3/5, (4/5)e₃, 0), v₂=(−4/5, (3/5)e₃, 0), v₃=(0,0,1). I certified independently that
  {p₁,p₂,p₃} is a genuine Jordan frame (each idempotent, Tr=1, pairwise Jordan-orthogonal,
  Σ=I), and that **p₁ is genuinely octonionic** (nonzero e₃ off-diagonal entry, ≠ any E_ii).
  Then X_rot = 7p₁+5p₂+3p₃ (distinct spectrum). Result:
  `s_{X_rot}(p_i)=0 EXACTLY at the rotated points`, while `s_{X_rot}(E₁₁) ≠ 0` — **the zero
  FOLLOWS the rotated frame**, not the standard frame. The operator characterization tracks:
  `[X_rot, p_i]=0` at the rotated points and `≠0` at E₁₁. **PASS.** Covariance is exhibited,
  not assumed.
- Permutation-rotated frame (both other paths): zero follows g.E_ii — **PASS**.
- **Degenerate strata recorded & excluded** (guard #1): X=I/3 ⟹ s≡0 identically (vacuum control);
  diag(5,5,3) ⟹ E₃₃ an isolated zero AND a positive-dimensional zero locus in the x₁=x₂
  eigenspace (I exhibited a non-E_ii rank-1 idempotent in that block that is also a zero) — no
  index claim there. **PASS.**

---

## Gate 0 — the v22 dictionary (the ONE genuinely-open identification). **HOLDS (HIGH).**

**Claim.** The v22-unforced gluing U(1) circle (slot 82: joint pair-stabilizer Spin(8), slice
action one compact SO(2) = the C_u phase) acts on the J_{1/2}(E₁₁)∩h₃(C_u) tangent as a NONZERO
multiple of the C_u complex structure: generator `D=[dU,·]`, `dU=diag(0, −e₇/2, e₇/2)`; slice
weight +1, tangent weight −1/2.

**Independently re-derived and verified (MY computation + slot-82 cross-checks):**
- `D=[dU,·]` acts on the V₀ slice (the x₁=(2,1) entry) as `+1·J_Cu` and on the J_{1/2} tangent
  (x₂=(0,2) and x₃=(1,0) entries) as `−½·J_Cu`, where `J_Cu` is e₇-multiplication
  (a+be₇ ↦ −b+ae₇) — **PASS** (MY matmul, symbolic C_u state).
- **D is genuinely the slot-82 surviving circle.** Building D's 27×27 engine matrix and running
  the slot-82 tests directly: D **fixes both E₁₁ and E₂₂** (it is in the joint pair-stabilizer
  r₁₂), and it **passes all four defining conditions** — cond1 u-alignment `[D_slice,J]=0`,
  cond2 det₂-isometry (so(3,1)-valued slice block), cond3 Peirce-block preservation, cond4
  interface-intertwining (D is a derivation of the Peirce quadratic map). These are exactly the
  conditions v22/slot-82 used to ISOLATE the surviving SO(2). **PASS.**
- **D's slice block exactly equals the recorded `KK._Cu_complex_structure_slice`** (the v22 J),
  and is nonzero (`is_zero_on_slice = False`): the nontrivial surviving circle, not the dead one.
- **D is a genuine Jordan derivation in f₄** (`D(A∘B)=D(A)∘B+A∘D(B)` on a battery) — so the
  circle `exp(θD)` is an exact one-parameter subgroup of F₄=Aut(h₃(O)).
- **The spectrum settles the weights and circle-closure.** `D` (27×27) has eigenvalues
  **{0 : 9, +i : 1, −i : 1, +i/2 : 8, −i/2 : 8}**. The ±i pair (mult 1 each = 1 complex
  direction) is the slice C_u rotation (weight +1); the ±i/2 pair (mult 8 each = 16 = the full
  V_{1/2}(E₁₁) tangent) is the tangent rotation (weight −1/2). The magnitude ratio is exactly 2,
  so `exp(θD)` **closes into a genuine U(1)** (the tangent rotates at half the slice rate). The
  −1/2 tangent weight is therefore real algebra, not an artifact. 1+16+9 = 26 nonzero+zero
  matches dim f₄ acting; the count is consistent.

**Assessment.** Nonzero action on the tangent, by the SAME circle v22 isolated, with the C_u
complex structure as the action — the dictionary is sound. The framing ("v28's object is the
v22-U(1)'s action on the variety's own tangent") is established, not assumed. **Gate 0 holds.**

---

## Fence / honesty

- All E1/E2/Gate-0 verdicts are exact over Q / Q(t); no float enters the verdict path.
- Classical-vs-program (guard #4): the spectral theorem in h₃(O) is used (recorded); the program
  content here is the identification (s_X = landscape gradient; zeros = eigenframe; the v22
  dictionary). No imported result is presented as derived.
- Language fence respected: this is BASE tangent kinematics. No Einstein, Newton constant, G=κT,
  dark matter, geodesic, or "gravity = connection". "matter-pinned" = topological class only
  (developed in 88-GATE-3-VERIFICATION.md).

**E1: CONFIRMED (HIGH). E2: CONFIRMED (HIGH). Gate-0 dictionary: HOLDS (HIGH).**
