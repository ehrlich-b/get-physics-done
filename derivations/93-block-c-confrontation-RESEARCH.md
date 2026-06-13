# Phase 93 (v33.0) — RESEARCH: The Block-C Confrontation
### "What, if anything, forces the metric response?"  (the governance tripwire run)

> **No-web executor's grounding bible.** All literature the executor needs is staged verbatim
> below (the executor has no web/arxiv tools). Discipline (v21–v32): exact over Q/Q(t); fail-fast
> gates; controls with known answers; non-hardwired `verdict()`; reuse `tensor_probe.py` +
> `lichnerowicz_response.py` (do NOT rebuild); matched-monomial; commit after each gate.
>
> **THE QUESTION (Bryan's tripwire):** does any framework-NATIVE functional `A[g]` of the metric,
> built from the program's own resources, whose coupled extremization with the matter energy `E`
> forces a sourced metric response `(Δ_L − 2Λ)h = κ·TT(B3)` — or does the variety force NOTHING and
> the route parks at fork A (honest incomplete-TOE)? **Gravity or genuinely-don't-know, never
> math-for-math.** CANNOT-FORMULATE / FORCES-NOTHING is a RESOLUTION, not a failure.

---

## §0. Where we stand, and the verdict objects

The program owns the MATTER side of a variational pair, as theorems on the frozen cut
**CP² = h₃(C_u)** (Fubini–Study, Kähler–Einstein, **Ric = 6g, Λ = 6, λ₁ = 12 (mult 8), λ₂ = 32**):

- `E[φ_M, g] = ∫(|dφ_M|²_g − λ₁ φ_M²) dvol_g` is framework-native (v25's field equation is its
  Euler–Lagrange identity); `δE/δg` is the B3-shaped stress whose unique transverse part is the
  certified v31/v32 mode:
  - **TT(B3) = the λ_L = 32 triple-27 straddle**, **‖TT(B3)‖² = (1/30)(TrM²)²** (detM absent),
    direction **T₂₇[P27(M⊗M)]** (c₈ = c₁ = 0), stiffness **ε = λ_L − 2Λ = 32 − 12 = 20**.
- The v26 sourced equation and v27 balance law are exact identities on FROZEN g (v27 is metric-free
  by construction; demanding its persistence under g→g+h forces NOTHING — **excluded from the gates**).

**What the framework has NEVER produced is the GEOMETRY side:** a functional `A[g]` built from its
OWN resources (NO imported ∫R√g, NO GST prepotential — that chain died circular) whose coupled
extremization with E forces a response, or that NAMES what replaces it. **The five fiber kills
(v17–v21) do NOT transfer:** Molien forbids derivative functionals on the *algebra*, but the variety
is a *manifold* and spectral functionals of g exist there. Wall 1 (the selection law) has never been
asked on the variety. This run asks it, and only it.

**Verdict taxonomy (frozen at Gate 0; STOP rules binding):**
- **FORCES-EINSTEIN-FORM** — A4 lands Einstein-form with forced constants AND A3a couples to all three
  blocks. (The program's first selection law — Wall 2 unpaid, NOT called gravity.)
- **FORCES-OTHER** — A4 lands a different named operator (still a sourced metric response). Do NOT
  relabel to fit.
- **FORCES-OTHER-PARTIAL** — A3a couples to the (1,1)-27 only ⇒ partial (5/9) response; honest
  intermediate, not Einstein.
- **FORCES-NOTHING** — A3a blindness, or A4 degenerate, AND Track B exhausted with no native
  Einstein-producer ⇒ park at fork A. A RESOLUTION — write it that way.
- **CANNOT-FORMULATE** — Gate A1 cannot pin the principle sharply ⇒ same as FORCES-NOTHING per the
  tripwire.

---

## §1. GATE 0 (BINDING STOP GATE) — discharge the v32 deferred obligation: certify ε = 20

**Status as of this RESEARCH: DE-RISKED → PASS, exact over Q (orchestrator prototype).** The executor
FORMALIZES this into the committed driver and re-certifies; the verifier independently re-derives.

### §1.1 The obligation
v32.0-B recorded ε = 20 on EVIDENCE (Boucetta Table V/VIII row 2 + degree-counting + the (1,1)-block
Schur scalar + the single-rep fingerprint), **NOT on a directly-run full-tensor operator**. The
driver's full `lichnerowicz` def returned a spurious **28 on (2,0), 4 on (0,2)** (not 32) on the
verdict residue r — flagged UNTRUSTED, duplicate def removed. Gate 0 must build a CORRECT full-tensor
Δ_L and confirm **Δ_L r = 32·r on EVERY block** (the (1,1)-27 AND the (2,0)+(0,2) anti-27s), exact
over Q, with a control that a fixed Δ_L returns 32 on each block independently (no per-block tuning).
PASS ⇒ ε=20 CERTIFIED, proceed. FAIL ⇒ **STOP the entire run, revisit the ε=20 grade.**

### §1.2 The operator (frozen convention, RESEARCH §3 of v32)
On the Einstein background Ric = Λg (Λ=6):
> **Δ_L h = ∇*∇h + 2Λ h − 2 R̊h = ∇*∇h + 12h − 2R̊h**,   (R̊h)_{μν} = R_{μρνσ} h^{ρσ}
with ∇*∇ = −g^{μν}∇_μ∇_ν the POSITIVE (geometer's) connection Laplacian. Sign pin (mandatory):
∇*∇ gives **+12 on a λ₁ scalar, +32 on a λ₂ scalar** (the engine `laplacian` is the analyst +div grad,
negative-semidefinite; ∇*∇ = −Δ_analyst). Work in the Kähler complex frame; a symmetric 2-tensor is
the block-triple (H20, H11, H02) = (T_{ab}, T_{ab̄}, T_{āb̄}).

### §1.3 THE TWO BUGS IN THE OLD ANTI-BLOCK PATH, AND THE PRINCIPLED FIX
The old full `lichnerowicz` failed on the anti-blocks for two independent reasons. Both are real math
errors (not r being a non-eigentensor — see §1.4 the control proof). **The executor must implement
the fix as DERIVED below, not by flipping a sign to hit 32.**

**BUG 1 — the rough Laplacian used one ordering doubled.** The connection Laplacian is the symmetric
trace of the second covariant derivative:
```
∇*∇ T = − g^{μν} ∇_μ ∇_ν T = − ( g^{a b̄} ∇_a ∇_b̄  +  g^{ā b} ∇_ā ∇_b ) T          [CORRECT]
```
(In the complex frame the nonzero inverse-metric components are g^{a b̄} and its conjugate g^{ā b};
both contractions appear.) The old `rough_laplacian` computed `−2 g^{a b̄} ∇_a ∇_b̄ T` — ONE ordering
doubled. On a SCALAR the two orderings commute (∂_a∂_b̄ = ∂_b̄∂_a), so −2 g^{ab̄}∂_a∂_b̄ = the correct
Laplacian — which is why the +12/+32 scalar sign-pin passed and hid the bug. On a TENSOR the orderings
differ by the curvature commutator g^{ab̄}[∇_a,∇_b̄], which acts with OPPOSITE sign on holomorphic vs
antiholomorphic indices ⇒ the old operator was not conjugate-symmetric: it gave ∇*∇ = 24 on (2,0) but
0 on (0,2) for the control. **FIX:** compute BOTH orderings —
- L1 = g^{a b̄} ∇_a(∇_b̄ T):  inner antiholo `∇_b̄ T` (= `_nabla(blocks, b, ebar=True)`), then outer
  holo `∇_a` (connects UNbarred μ,ν with Γ^λ_{a·}), contract g^{a b̄} = `ginv[b,a]`.
- L2 = g^{ā b} ∇_ā(∇_b T):  inner holo `∇_b T` (= `_nabla(blocks, b, ebar=False)`), then outer antiholo
  `∇_ā` (connects BARRED μ,ν with GamB^λ_{ā·}), contract g^{ā b} = `ginv[a,b]`.
- `∇*∇ T = −(L1 + L2)`.

This is exactly the existing `rough_laplacian` machinery run a second time with holo/antiholo swapped,
summed (coefficient −1 each, NOT −2 on one). It restores conjugate symmetry (the (2,0) and (0,2)
outputs become equal, as they must for a real tensor).

**BUG 2 — the curvature term R̊ has the wrong sign on the anti-blocks.** With BUG 1 fixed, the control
read 16 on the anti-blocks (still not 32). Decomposition: with the correct ∇*∇ = 12 on the anti-blocks
of the control, Δ_L = 12 + 12 − 2R̊ = 16 forces R̊_anti = +4 in the old code, but the control requires
R̊_anti = **−4**. The curvature operator R̊ on the *holomorphic* (2,0)/(0,2) tensors of positively-
curved CP² carries the **opposite sign** to the (1,1) Hermitian block (where R̊(g)=Ric=+6g is the
validated normalization). The old `Rdot` anti-block contractions (the `R[a][k][b][l]…` and
`R[k][a][l][b]…` lines) have a sign/antisymmetry error from `_R_low`'s pair-ordering. **FIX:** derive
the anti-blocks index-honestly as (R̊h)_{μν}=R_{μρνσ}h^{ρσ} with the SAME `_R_low` + full raising used
for the (1,1) block (which is correct: R̊(g)|₍₁,₁₎=+6g), so the anti-blocks inherit the consistent
sign automatically; do NOT hand-write separate per-block formulas. Validate via the control below
(which fixes the sign without reference to r). Empirically the corrected R̊_anti = −4.

### §1.4 THE CONTROL (the operator's oracle — validates ALL blocks at λ=32, NO tuning to r)
The independent control eigentensor is **Hess(R_M)** for R_M a λ₂=32 scalar eigenfunction
(`TP.R_M_field(M)`, already certified: `∇∇R_M == δ*(dR_M)`, λ₂=32). It is a PROVABLE Δ_L
eigentensor at 32 on EVERY block, by the Einstein identity (Besse 1.143 corollary; standard
deformation theory):
> On an Einstein manifold, **Δ_L ∘ δ* = δ* ∘ Δ_H** (δ* the symmetrized covariant derivative on
> 1-forms, Δ_H the Hodge–de Rham Laplacian). With ω = dR_M: Δ_H(dR_M) = d(Δ_0 R_M) = 32·dR_M, and
> δ*(dR_M) = Hess(R_M). Hence **Δ_L(Hess R_M) = 32·Hess(R_M)** identically — independent of the
> operator's implementation. Hess(R_M) has nonzero (2,0), (1,1), (0,2) blocks.

**Controls the executor MUST pass before reading r (all exact over Q):**
- **C0 (sign pin):** ∇*∇ = +12 on a λ₁ scalar, +32 on a λ₂ scalar (already a Gate-1 control).
- **C1:** Δ_L g = 0 on all blocks (g is Δ_L-harmonic on KE; pins R̊(g)|₍₁,₁₎=6g).
- **C2a:** Δ_L(Hess φ_M) = 12·Hess(φ_M) on the (1,1) block (the λ₁ Hessian; its anti-blocks VANISH
  because λ₁ eigenfunctions generate holomorphic Killing fields ⇒ Matsushima: ∇_a∇_b φ = 0).
- **C2b (the decisive control):** Δ_L(Hess R_M) = **32·Hess(R_M) EXACT on ALL THREE blocks**, and
  the (2,0) and (0,2) eigenvalues are EQUAL (conjugate symmetry). This is the no-tuning certificate.
If C2b passes only after a sign choice, that sign is FIXED by the control (a provable 32-eigentensor),
NOT by r — so it is not tuning to the answer.

### §1.5 THE CERTIFIED RESULT (orchestrator de-risk, to be reproduced)
With BUG-1 + BUG-2 fixed: **C1 PASS (g→0), C2a PASS (Hess φ→12 on (1,1)), C2b PASS (Hess R_M→EXACT
32 on all three blocks, conjugate-symmetric), and r → EXACT 32 on every block** (the d1 direction
shown; the executor runs ≥3 directions s01/a01/d1 and a generic-detM matter). The wrong (old) operator
gives the control AND r both 16 on the anti-blocks; the right operator gives the control AND r both 32
— **r tracks the provable control identically at every step**, the airtight proof that r is a clean
λ_L=32 eigentensor and the 28/4 was purely an operator bug. **⇒ Δ_L r = 32·r on every block ⇒ ε =
λ_L − 2Λ = 32 − 12 = 20 CERTIFIED on a directly-run, control-validated full-tensor operator.** The v32
deferred obligation is discharged.

### §1.6 Machinery-freeze control (run BEFORE any new computation)
Re-run the v32 fingerprints **T1/T2/T3 exact over Q** (`lichnerowicz_response_fingerprint.py`):
T1: `4(t_s01+t_a01+t_d1) + (t_s02+t_a02+t_s12+t_a12) = 0`; T2: `t_d2 = 9(t_s01+t_a01+t_d1)`; T3:
single-generator residue Gram rank 6. Deviation = a regression ⇒ halt and diagnose.

---

## §2. TRACK A (the positive candidate) — the λ₁-extremal selection principle

The one geometry-side functional the framework arguably FORCES: the variety's defining embedding is
**by λ₁-eigenfunctions** — the moments φ_a (a=1..8 = the SU(3) adjoint = the λ₁=12 eigenspace; v25's
moment construction is algebraic, not chosen). The candidate functional is **A[g] = λ₁[g]·Vol[g]^{1/2}**
(n=4 ⇒ the scale-invariant combination λ₁·Vol^{2/n} = λ₁·Vol^{1/2}).

### §2.1 The two theorems (VERBATIM — staged for the no-web executor)

**Takahashi (1966), "Minimal immersions of Riemannian manifolds", J. Math. Soc. Japan 18, 380–385.**
> If an isometric immersion f: M → ℝ^{N+1}, f=(f¹,…,f^{N+1}), is defined by eigenfunctions f^i of the
> Laplace–Beltrami operator with a COMMON eigenvalue λ (Δf^i = λf^i), then (i) f(M) lies on a sphere
> S^N_R centered at the origin with **λ = dim(M)/R²**, and (ii) f: M → S^N_R is MINIMAL. Conversely,
> a minimal isometric immersion into S^N_R has coordinate functions that are λ-eigenfunctions with
> λ = dim(M)/R².

**El Soufi–Ilias (Pacific J. Math 195 (2000) 91–99; and "Immersions minimales, première valeur propre
du Laplacien et volume conforme", Math. Ann. 275 (1986) 257–267).**
> A metric g is **λ₁-CRITICAL** (a critical point of g ↦ λ₁(g)·Vol(g)^{2/n} over all metrics, or a
> conformal class) **iff** there is a finite family of first eigenfunctions giving an **isometric
> minimal immersion of (M,g) into a sphere** ("λ₁-minimal immersion"). Subharmonicity gives the
> variational characterization: g is λ₁-extremal ⟺ ∃ first eigenfunctions u_1,…,u_k with
> Σ du_i ⊗ du_i = g (the immersion is isometric) and Σ u_i² = const (lands on a sphere).
> **Uniqueness:** for a given CONFORMAL class there is **at most one** λ₁-minimal metric (Montiel–Ros
> 1986; El Soufi–Ilias). **Caveat (Kähler):** rigidity FAILS in the Kähler setting — every
> Kähler–Einstein Fano manifold with a nontrivial holomorphic vector field has λ₁ equal to its
> Matsushima/Bourguignon–Li–Yau lower bound (CP^n included); FS SATURATES the bound but is not pinned
> as the unique metric by criticality alone. Toric refinement (Biliotti–Ghigi; Apostolov–Jakobson–
> Kokarev arXiv:1411.7725 "An extremal eigenvalue problem in Kähler geometry"): FS is the unique TORIC
> Kähler metric saturating the BLY bound, but general λ_k-extremal Kähler metrics in a fixed Kähler
> class are NOT unique.

### §2.2 The gates (each falsifiable; exact over Q where in-rep)

**A1 (literature + scope pin + the joint test).** Verify the moment embedding CP² → ℝ⁸ (the SU(3)
adjoint, by the 8 φ_a) satisfies the Takahashi/El Soufi–Ilias hypotheses: isometric (up to the v25
normalization — STATE the normalization), minimal, into the trace-form sphere Σ φ_a² = const (the
Jordan trace-form sphere; check it). Deliverable = a PROPERTY-vs-PRINCIPLE verdict on TWO joints:
- **(a) Is λ₁-extremality FORCED by the algebraic embedding, or merely TRUE of FS?** If the embedding
  is the moment map BY CONSTRUCTION (the φ_a are the algebraic moments, and Σdφ_a⊗dφ_a ∝ g, Σφ_a²=const
  hold by the Jordan identities), then by El Soufi–Ilias extremality is a CONSEQUENCE → **FIT** (the
  principle is forced). If it must be checked and merely happens to hold → **CLAMP**. Apply the joint
  test honestly; if CLAMP, grade Track A accordingly — do NOT relabel "conditional" and proceed
  (Trap #20).
- **(b) Is FS the UNIQUE λ₁-extremal metric in its Kähler class (a genuine SELECTION), or one of many
  (a property selecting a CLASS, not FS)?** Per §2.1: criticality alone does NOT pin FS (rigidity fails
  in Kähler); uniqueness holds only in a CONFORMAL class (Montiel–Ros) or for TORIC metrics at BLY
  saturation. **A selection LAW needs uniqueness.** Report which: if non-unique, A[g] selects a CLASS,
  not FS ⇒ Track A weakens to a CONSISTENCY CONDITION, not a law. This is a load-bearing finding.

**A2 (in-rep minimality).** Minimality of the moment embedding (mean curvature vanishes): by Takahashi
this is AUTOMATIC for an immersion by λ-eigenfunctions of a normalized metric — verify which direction
is theorem (auto, given the eigenfunction property) and which needs computing (the normalization
Σdφ_a⊗dφ_a ∝ g), from the v25/v31 machinery (`phi_field`, `grad_bilinear`, `trace_g`).

**A3a (the BLINDNESS check — RUN BEFORE A3; this can decide the verdict).** The second variation of
λ₁ couples h through the overlaps **⟨dφ_a ⊗_sym dφ_b, h⟩**. The products dφ_a ⊗_sym dφ_b are real
symmetric 2-tensors; Sym²(8) ⊃ 27 once, so they CAN reach the straddle's 27-channel — but the straddle
is THREE blocks ((1,1)-27 ⊕ (2,0)-27 ⊕ (0,2)-27). **Test the L² overlap ⟨dφ_a ⊗_sym dφ_b, r_block⟩
with EACH block of the certified r separately** (use `l2_tensor` block-restricted, the 8×8×(3 blocks)
overlaps, exact over Q):
- zero on all three ⇒ Track A is BLIND to the certified mode ⇒ A4 degenerate ⇒ **FORCES-NOTHING** for
  this candidate (record, move to Track B).
- nonzero on the (1,1)-27 ONLY ⇒ Track A sources just 5/9 of the mode (the (1,1) share); the anti-parts
  get no response ⇒ a PARTIAL, non-Einstein response ⇒ **FORCES-OTHER-PARTIAL**, NOT FORCES-EINSTEIN
  (Trap #23). NOTE: the gradients dφ_a have nonzero (1,0) parts, so dφ_a⊗dφ_b HAS a (2,0) component —
  the anti-overlap is NOT obviously zero; compute it, do not assume.
- nonzero on all three ⇒ Track A can source the full mode ⇒ proceed to A3/A4.

**A3 (the second variation).** Compute δ²(λ₁·Vol^{1/2}) at FS on the TT sector, in-rep on the v32
multiplet. λ₁ is degenerate (mult 8) ⇒ the variation is the eigenvalue-of-a-matrix (degenerate
perturbation theory) on the 8×8 Gram G_{ab} = ⟨dφ_a ⊗ dφ_b, h⟩. Deliverable = the quadratic form
**Q_A[h]** on the 27-multiplet, exact, **SU(3)-equivariant (Schur block-diagonal — deviation = bug)**.
Standard second-variation formula (Berger; El Soufi–Ilias): for a degenerate λ₁ with eigenspace {φ_a},
δ²λ₁[h] is the extremal eigenvalue of the matrix
`−∫(2 h(∇φ_a,∇φ_b) + (div h − ½∇tr h)·… )` restricted to the eigenspace; on the TT sector (div h=0,
tr h=0) this collapses to `δ²λ₁[h]_{ab} = −2∫ h(∇φ_a,∇φ_b) dvol = −2⟨dφ_a⊗dφ_b, h⟩` (the overlaps of
A3a). Build it exactly; verify Schur structure.

**A4 (the coupled equation).** Extremize `A[g] + μ·E[φ_M, g]` over h at fixed M (μ a Lagrange
multiplier enforcing the matter constraint, **NOT a coupling** — fence, Trap #21). The stationarity
δ/δh = 0 gives a sourced LINEAR equation for h. Deliverable = that equation, exact. **STATE which:**
- **(i) Einstein-form:** `(Δ_L − 2Λ)h ∝ TT(B3)` on the TT sector (i.e. the variation of A reproduces
  the linearized-Einstein operator (Δ_L−2Λ) — this is the program's first selection law);
- **(ii) a DIFFERENT named operator** (still a sourced metric response — NAME it: e.g. the λ₁-Hessian
  operator H_{φφ}, a projector onto the (1,1)-27, …; do NOT relabel to fit);
- **(iii) degenerate** (no TT response — A3a blindness).

**A5 (the number).** If (i) or a clean (ii): read off **κ as the spectral ratio it is** (e.g. the ratio
of the A-second-variation eigenvalue to ε=20, both framework numbers). **FENCE:** κ is a ratio of
framework numbers, NOT Newton's constant; signature is still Riemannian (Wall 2 unpaid). NO outcome
here is called "gravity."

---

## §3. TRACK B (the exhaustion negative) — the native-functional menu

Enumerate ALL framework-native functionals of g on the base. The menu is short and auditable; the test
for each is **selection-traceability**, not mere existence: a functional is NATIVE iff its SELECTION
(why THIS functional) traces to algebra/framework data; it is an IMPORT iff it is just the known
gravity action written down.
- **(i) ∫G_M dvol (the entropy field):** integrand is metric-blind ⇒ at most a trace/conformal
  response. PROVE the one-line lemma (δ/δh of a metric-independent integrand × dvol = ½ G_M g^{μν} ⇒
  pure-trace, kills nothing on the TT sector) and retire it.
- **(ii) spectral functionals:** the λ₁ tower (= Track A — selection traces to the moment embedding,
  NATIVE), λ₂, the heat invariants a_k. **CRITICAL (Trap #22):** a_1 = ∫R√g is a heat-kernel invariant
  — admissible to NAME on the menu, but it IS the fenced Einstein–Hilbert import (NO framework-side
  reason selects it over any other functional of g; that is exactly the dead GST move). **If the ONLY
  Einstein-producing menu item is a_1, the honest verdict is FORCES-NOTHING *natively*** — a_1 wearing
  a spectral-invariant costume is still the import.
- **(iii) Vol[g]:** cosmological-constant only (δVol/δh ∝ g, pure trace).
- **(iv) anything from the moment map beyond (i)–(iii):** sweep and name, same selection-traceability
  test (e.g. ∫|∇φ_M|², ∫φ_M², the v26 λ₂-field functional — check each is trace-only or λ₁-equivalent).

**Deliverable:** either Track A is the UNIQUE selection-traceable candidate (the menu argument closes),
or the missed candidates are named and priced. If Track A fails AND the menu is exhausted with no
native Einstein-producer ⇒ **FORCES-NOTHING, park at fork A** — the tripwire ACCEPTS this as the
RESOLUTION of don't-know; what it forbids is wandering. **Log any silent cap** (a functional skipped, a
sweep bounded) explicitly — silent truncation reads as "exhausted" when it isn't.

---

## §4. FENCED / PRICED ONLY — NOT run, NOT the verdict

- **lapse/00 — DEFERRED, not run here (ordering call; Bryan can override).** Block-C (does any native
  A[g] force a response) is formulable on the SPATIAL TT sector the program already owns; the lapse/00
  (time-time) assembly acquires a referent only IF Block-C lands positive. Running lapse/00 first would
  be math-for-math. Block-C now; lapse/00 becomes the immediate follow-up iff FORCES-EINSTEIN-FORM or
  FORCES-OTHER.
- **OP² lift** (Spin(9), not Kähler): priced, off-menu this run (the (1,1) split does not transfer).
- **Base-Sakharov** (one-loop det of the 8 moment scalars on CP²; a_1 ∝ ∫R√g): an IMPORT (the
  functional-integral machinery + extremize-the-effective-action are not native). The v21 kind-4 kill
  was the FIBER version (16-vs-6 rank wall); the base version stays PRICED-ONLY — if Track A/B both
  land negative, it is the NAMED off-menu option for a later Bryan decision, not a silent fallback.
- **Thermo scope:** cite the 2026-06-09 unban memo's exact boundary before ANY entropy-extremization
  language beyond v26's proved vacuum-MaxEnt (a theorem of the doublet, not a thermodynamic postulate).

---

## §5. Traps / controls / discipline (carry into every artifact)

- **Trap #20** — extremality-as-property smuggled as principle: A1's joint test (a) is the guard.
- **Trap #21** — the multiplier μ relabeled a coupling: it is not.
- **Trap #22** — a degenerate A4 "fixed" by adding imported terms: adding ∫R√g at any gate (INCLUDING
  via the heat-kernel a_1 relabeled a "native spectral functional") = STOP.
- **Trap #23** — a partial (1,1)-only response relabeled "Einstein on the relevant sector": the relevant
  sector is the FULL straddle; partial is FORCES-OTHER-PARTIAL.
- **Controls:** v32 fingerprints reproduce before any new computation (machinery freeze); Gate-0
  controls C0/C1/C2a/C2b; A3's quadratic form SU(3)-equivariant (Schur block-diagonal); exact over Q.
- **`verdict()` NON-HARDWIRED** — deterministic ladder driven by the computed booleans (A3a block
  overlaps, A4 operator identity, Track-B traceability), with a synthetic-flag self-test.
- **FENCES (binding, verbatim):** NO Einstein-equation / G=κT / dark-matter / geodesic language; κ is a
  framework ratio, NOT Newton's constant; the frozen FS geometry is USED, not derived; signature
  Riemannian (Wall 2 unpaid). v33 does NOT retract v17–v21 (Block-C statements). Paper 5 remains the
  only result in the more-than-nothing column. Three-path verification standing; milestone HOLD for
  human ratification; do NOT self-register v34.

---

## §6. Conventions (frozen; mirror v31/v32)
- Cut CP² = h₃(C_u), FS Kähler–Einstein, Ric = 6g, Λ = λ₁/2 = 6, λ₁ = 12 (mult 8 = su(3) adjoint),
  λ₂ = 32. Metric `MET_SCALE·g_pot` (the λ₁=12 bridge). Complex frame; symmetric 2-tensor = block-triple
  (H20, H11, H02). ∇*∇ POSITIVE (geometer's): +12 on λ₁, +32 on λ₂ scalars. Riemann sign pinned by
  R̊(g)|₍₁,₁₎ = Ric = +6g. Exact over Q/Q(t); floats illustrative only. sympy 1.14.0, Python 3.14.
- Reuse `tensor_probe.py` (fs_metric, christoffel_hol/_antihol, cov_hessian, R_M_field, phi_field,
  grad_bilinear, delta_star, divergence, trace_g, l2_tensor/l2_scalar) and `lichnerowicz_response.py`
  (extract_tt, riemann_kahler, _nabla, rough_laplacian [to be corrected], Rdot [anti to be corrected],
  lichnerowicz_11 [validated (1,1)]). Do NOT rebuild certified machinery.

---

## §7. Through-line (for the milestone, mirror v32's)
v31 the tensor wall OPENS (existence) → v32 the tensor DICTIONARY closes (forced source data: κ=1/30,
ε=20, the triple-27 straddle) → **v33 asks the SELECTION LAW: is there a native A[g] whose coupled
extremization with the matter E forces a sourced metric response, or does the variety force nothing and
the route park at fork A (honest incomplete-TOE)?** The tripwire: gravity or genuinely-don't-know.

## §8. References (staged)
- Takahashi, J. Math. Soc. Japan 18 (1966) 380. — minimal immersion by eigenfunctions.
- Montiel–Ros, Invent. Math. 83 (1986) 153; El Soufi–Ilias, Math. Ann. 275 (1986) 257 & Pacific J.
  Math 195 (2000) 91. — λ₁-extremal ⟺ minimal immersion by first eigenfunctions; conformal uniqueness.
- Apostolov–Jakobson–Kokarev, arXiv:1411.7725 — λ_k-extremal Kähler metrics (non-uniqueness in class).
- Boucetta, arXiv:0712.2830 — CP^n Lichnerowicz spectrum (Tables V–VIII; row 2 = (1,1)-27 at 32).
- Besse, "Einstein Manifolds" §1.143 (Δ_L), and the Einstein identity Δ_L∘δ* = δ*∘Δ_H.
- Koiso (rigidity of CP^n); Matsushima (λ₁ eigenfunctions ↔ holomorphic Killing fields).
