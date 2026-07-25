# GPD Prompt — The Sourced Field Equation: MaxEnt Derived and the Second-Order Vacuum Structure (J5-on-the-variety, step 2)

**Slot 86 / v26.0-candidate. STATUS: RATIFIED-BY-STANDING-DIRECTIVE
(Bryan, 2026-06-10/11). Ready to run.**

_Context: v25.0 COMPLETE (commits f1f95f37 + 2833cddb). Certified assets
this run consumes: the moment doublet m = TrX − ⟨X,p⟩,
q = det₂(C_p X) = ⟨X#,p⟩, r = q/m²; the canonical field equation
Δφ_Y = −λ₁(φ_Y − ⟨Y,I/3⟩) with λ₁ = 48 (OP²) / 12 (CP² cut); the
ΔP = −λ₁(E_11 − I/3) frame machinery; the freq-≤2 fingerprint; the
Gate-4 ledger. This run is the SECOND-ORDER chapter: expand the
landscape around the vacuum X = I/3 + εM (traceless M) and extract the
sourced field equation. Literature placement (cite): the second-order
entanglement-equilibrium level is where Jacobson's program meets
canonical energy / Fisher information (Lashkari–Van Raamsdonk; Faulkner
et al.); the v17 corpse (Hess(−log det) = Fisher–Bures) was the
right-object-wrong-side version of this object — explained, not
resurrected._

_Discipline: v21–v25 pattern — executor + independent verifier (separate
code path), exact over Q / Q(t) / Q[ε], fail-fast gates, controls with
known answers. No G = κT, no Newton constant, no SUGRA, no dark-matter
language anywhere._

## Pre-read: milestone type (pre-registered)

**Extraction milestone #2** (same type as v25, declared up front): the
central identities below come with derivation sketches and two were
hand-checked at design time. Expected outcome: PASS. The run's
new-information content: the exact constants (α, β, the level-2
eigenvalue λ₂ on OP² — a genuinely underived number; on the cut
λ₂ = 32 is pre-registered), the sourced-equation coefficients, the
hidden-sector statements verified, and the v27 fork ledger. ANY failure
= a hole in the design derivation = more informative than passing;
report the broken step and STOP. The genuine open FORKS of the route
(the constrained-balance equation-of-state question; the U(1)/connection
coupling) are NOT in this run — Gate 5 triages them for v27.

## The derivation sketch (verify every step; two hand-checked anchors)

Perturb the vacuum: X = I/3 + εM, Tr M = 0, symbolic M (26 params),
exact in Q[ε] (truncate at ε²; order-counting is load-bearing — guard 1).

1. **First order — the doublet collapses and MaxEnt derives.**
   m = 2/3 − ε⟨M,p⟩. Sharp identity: I × M = −M/2 for traceless M
   (polarize #; hand-checked), so X# = I/9 − (ε/3)M + ε²M#, giving
   q = 1/9 − (ε/3)⟨M,p⟩ + ε²⟨M#,p⟩. Hence **δq = δm/3**: at first
   order there is ONE field, ⟨M,p⟩, not two. Consequence (hand-checked):
   δr = (9/4)δq − (3/4)δm = 0 — **the purity/entropy landscape is
   flat at first order in the matter perturbation, at EVERY event p**
   = the MaxEnt property of the vacuum, now DERIVED on the variety
   (this is v24's flattening result and v23's zero-gradient fact,
   re-read: the first-order balance the fiber failed to host is
   structurally empty; the content lives at second order).

2. **Second order — the entropy-response field.**
   r = q/m² expanded exactly:
   > **δ²r = (9/4)·G_M(p)·ε², G_M(p) := ⟨M#,p⟩ − ¼⟨M,p⟩²**
   (hand-checked via the ε²-coefficient c − a²/4 with a = −⟨M,p⟩,
   c = ⟨M#,p⟩). Entropy conversion: on the 2-face, S = f(r) with
   f analytic at r = 1/4 (expand in u = 1 − 4r: the ±√u branches
   cancel — verify exactly, guard 2), f'(1/4) = 2, so
   **δ²S = (9/2)·G_M·ε²** (no (δr)² term since δr = 0).
   Exact relative entropy: the vacuum face state is maximally mixed,
   so S(ρ_face ‖ ρ_vac) = log 2 − S(ρ_face) EXACTLY (2-dim face) —
   the response field IS the relative-entropy density at second order.
   **Built-in positivity check (must hold; failure = bug):
   G_M(p) ≤ 0 for all traceless M and all p** (S ≤ log 2), with
   equality possible (anchor: M = diag(2,−1,−1), p = E_11 gives
   G = 1 − 1 = 0 — the face sees only the ∝I₂ block of M).

3. **The level split of the square.** Sym²(26) under F_4 = 1 ⊕ 26 ⊕ 324
   (multiplicity one each) and the only quadratic covariants of
   traceless M are M# and TrM²·1 (note M² = M# + ½TrM²·1 for traceless
   M — dependent, not a third covariant). Therefore
   > **⟨M,p⟩² = α·⟨M#,p⟩ + β·TrM² + R_M(p)**, with R_M exactly a
   > λ₂-eigenfunction (mean-zero level-2 part),
   for universal rationals (α, β) and the level-2 eigenvalue λ₂.
   **Operational determination (all pointwise at E_11, symbolic M):**
   compute Δ[⟨M,·⟩²](E_11) with the v25 frame machinery (second
   derivatives of products of the explicit rational t-functions), and
   solve
   Δ[⟨M,·⟩²](E_11) = −αλ₁(⟨M#,E_11⟩ + TrM²/6) − λ₂·R_M(E_11),
   R_M(E_11) = ⟨M,E_11⟩² − α⟨M#,E_11⟩ − β·TrM²
   (using ⟨M#, I/3⟩ = σ₂(M)/3 = −TrM²/6) as a polynomial identity in
   the 26 symbolic M-params: the system is OVERDETERMINED in
   (α, β, λ₂) — its consistency IS the level-split claim; covariance
   closes it to all p (the v25 closure pattern; spot-check with one
   exact rotation). **Pre-registered: λ₂ = 32 on the cut** (Fubini–Study
   λ_j = 4j(j+n): 4·2·4, consistent with λ₁ = 12 = 4·1·3 in the same
   normalization — external cross-check Ikeda–Taniguchi); **λ₂ on OP²
   is genuinely underived — derive it** (then cross-check non-blocking
   vs CROSS spectra, Cahn–Wolf 1976 / Besse ch. 3; report the ratio
   λ₂/λ₁ on both spaces).

4. **THE SOURCED FIELD EQUATION (the centerpiece).** Combining 2 and 3
   with the v25 free equation:
   > **(Δ + λ₁) G_M = −κ₀·TrM² + ((λ₂ − λ₁)/4)·R_M(p)**,
   with κ₀ = λ₁(1/6 + (α/4)·(0) + β/4)-type — DERIVE the exact constant
   from (α, β, λ₁) symbolically; do not trust this sketch's
   bookkeeping, only its shape. Reading (with fences, see
   anti-overclaim): the entropy-response field fails its free Helmholtz
   equation by an EXPLICIT source — a homogeneous term weighted by the
   matter's total quadratic invariant TrM² and an anisotropic term =
   the level-2 part of the squared matter moment — with both couplings
   fixed by canonical spectral data (λ₁, λ₂ − λ₁, α, β). This is the
   route's first SOURCED (Poisson-type) equation: free propagation
   (v25) + matter source (this run). Note the kernel honestly: (Δ+λ₁)
   annihilates level-1, so the identity does not DETERMINE G_M from
   the source — it is an exact identity, not a boundary-value problem.

5. **The hidden-sector statements (the 4-vs-16 gap materialized).** For
   M supported entirely off-u (all components in octonion directions
   e_1..e_6; the 12 V_{1/2} coords {12..17, 20..25} and the off-u parts
   of the (1,2) block):
   - **(invisibility)** ⟨M,p⟩ ≡ 0 for ALL p in the CP² cut (trace-form
     orthogonality to h_3(C_u) — verify symbolically), so the cut has
     NO first-order moment and NO direction data for M; yet
   - **(it still sources)** G_M|_cut = ⟨M#,p⟩|_cut ≠ 0 for M ≠ 0
     (the squares in M# land on the diagonal / in C_u — exhibit the
     exact form: which quadratic invariants of the hidden M the cut's
     field sees), and
   - **(the signature dichotomy)** hidden matter sources the cut PURELY
     at level ≤ 1 (the −¼⟨M,p⟩² term vanishes identically on the cut ⇒
     square-free, no level-2/anisotropic signature), while every
     u-aligned M' ≠ 0 is first-order VISIBLE on the cut (cut-moment
     injectivity, from v25's 9 = 1⊕8) and generically sources at
     level 2 as well. So on the cut: first-order-invisible ⟺
     off-u-supported ⟺ square-free source. All three statements exact;
     verify with symbolic off-u M and with explicit instances.

## The claims

- **B1 (MaxEnt derived):** δq = δm/3 and δr = 0 identically (symbolic
  M, all p via E_11 + covariance; along all 16 families over Q(t)).
- **B2 (the response field):** δ²S = (9/2)(⟨M#,p⟩ − ¼⟨M,p⟩²)·ε²; the
  exact relative-entropy identity on the face; the positivity check
  across symbolic/instance batteries.
- **B3 (the sourced equation):** the level split with (α, β, λ₂)
  determined by the overdetermined symbolic solve (consistency = PASS);
  λ₂(cut) = 32 confirmed, λ₂(OP²) derived; the sourced-equation
  constants assembled exactly.
- **B4 (hidden sector):** the three cut statements (invisibility /
  still-sources / square-free dichotomy), symbolic + instances.

## The exact verdict criterion

Everything symbolic: Q[ε]/(ε³) for the expansion (26 free M-params),
Q(t) along families, polynomial-identity solves for (α, β, λ₂).
Verdict per claim: PASS/FAIL stated separately. Floats illustrative
only; any gate resting on floats is void.

## Gates

- **Gate 0 (machinery, fail-fast):** the v25 frame machinery reloaded
  (both frames); Δ of PRODUCTS of moments along frames (second
  derivatives of products of rational t-functions — verify against the
  product rule symbolically); the ε-truncation ring; exactness checks.
- **Gate 1 (controls, zero evidential weight):** (i) the v25 free
  equation re-verified for one moment (regression control); (ii) the
  level-2 control: c11² − its (α,β)-fit must come out a λ₂-eigenfunction
  with the SAME λ₂ as the symbolic solve (independent λ₂ path);
  (iii) M = diag(2,−1,−1): the hand anchors G(E_11) = 0,
  G(E_22) = −2 − ¼ < 0... compute exactly (design-sketch values:
  ⟨M#,E_22⟩ = −2, ¼⟨M,E_22⟩² = ¼) — reproduce or correct with the
  triage rule (convention vs substance); (iv) I/3 (M = 0): everything
  vanishes identically.
- **Gate 2 (B1 + B2).**
- **Gate 3 (B3).** The overdetermined solve + covariance closure + the
  cut/OP² comparison table (λ₁, λ₂, gap, ratio on both spaces).
- **Gate 4 (B4).** Symbolic off-u M + at least two explicit hidden
  instances + one u-aligned contrast instance.
- **Gate 5 (the v27 fork ledger — exploratory, NON-BLOCKING, no
  claims):** (a) the constrained-balance fork at second order: with
  G_M and the canonical moment c11 both explicit, state precisely the
  equation-of-state question (on the locus ∇G_M ∥ ∇c11, is the
  multiplier a state-universal function of the LOCAL field values
  (m, q, c11) alone? note the invariant-counting fact that mixed
  U_X-type invariants of (X,p) exist beyond the moments — so
  state-dependence beyond local fields is POSSIBLE and the question is
  a genuine fork); assess computability (critical loci are algebraic —
  estimate degree/cost from one instance). (b) the U(1)/connection
  fork: confirm the scalar moments are gluing-invariant (the
  v22 U(1) cannot couple to (m,q) — one-line check), so a
  matter-forces-the-connection test needs the V_{1/2} spinor-valued
  data (which v24 proved the landscape resolves directionally) — list
  what object would have to be built. (c) claim-2 contact: the face
  modular generator K_face = −log ρ_face is now an explicit function
  of (m, q) — note what the per-point-time (J4) check would consume.
  File all three; no verdicts.

## Pre-registered failure modes (bug guards)

1. **Order-counting:** δr = 0 must be established as an identity in the
   truncation ring, not numerically; all second-order claims must
   exhibit their ε² coefficient symbolically.
2. **Branch smoothness:** S = f(r) at the degenerate point r = 1/4 —
   verify the √(1−4r) branches cancel to an analytic series (else the
   (9/2) conversion is wrong); the f'(1/4) = 2 factor verified exactly.
3. **Projector hygiene:** the level split comes ONLY from the
   overdetermined symbolic solve + the eigenfunction property — no
   numerically-diagonalized projectors; consistency of the system is
   itself the claim (if (α, β, λ₂) fail to exist, that is a FAIL of B3,
   not a fitting problem to paper over).
4. **Hidden-M bookkeeping:** off-u support defined by exact coordinate
   sets; the cut-vanishing of ⟨M,p⟩ shown by trace-form block
   orthogonality symbolically (not by sampling); octonion product
   conventions as v25 (the conj(x3·x2)-order trap is known — reuse the
   resolved convention).
5. **Trap-class #5/#6 (standing, with the exemption stated):** still no
   field equation for r or S themselves (rational objects); the SOURCED
   equation for G_M is exempt from #6 because the source is EXPLICIT
   and the claim is a specific exact identity with derived constants —
   NOT an existence claim for an annihilator. State this distinction in
   the write-up.
6. **Numeric leakage (standing).**

## Anti-overclaim (binding scope)

PASS ≠ Einstein, ≠ J5 complete, ≠ a balance with an independent
geometric variation — the background canonical geometry is STILL
FROZEN; λ₁, λ₂, α, β, κ₀ are spectral/structural data of that frozen
geometry (imports-as-math), NOT derived couplings; no Newton constant.
What this run certifies if PASS: the vacuum's MaxEnt property is a
THEOREM of the doublet (first order empty — the honest restatement of
v23's kill), the second-order entropy response is an explicit
relative-entropy field with a SOURCED Poisson-type equation whose
source is quadratic in matter, and first-order-invisible matter still
sources the cut's field (with a square-free signature). NO dark-matter
language — the hidden-sector statements are about THIS landscape's cut
restriction, nothing else. Signature stays OPEN. The genuine forks
(equation-of-state; connection coupling) are explicitly NOT tested
here — Gate 5 only prices them.

## Deliverables

- derivations/86-sourced-field-equation-RESEARCH.md (the sketch worked
  out with citations: Lashkari–Van Raamsdonk / Faulkner et al. for the
  second-order placement; Ikeda–Taniguchi / Cahn–Wolf / Besse for λ₂;
  the Jordan covariant facts with McCrimmon/Jacobson refs).
- derivations/86-GATE-N-SUMMARY.md per gate; independent verifier on
  B1/B2 (separate expansion path) and B3 (independent λ₂ via the c11²
  control + a different frame); 86-GATE-2/3-VERIFICATIONs; 86-VERDICT.md
  with B1–B4 stated separately from the Gate-5 ledger.
- code/variety_sourced_field_equation.py (executor, exact).
- Milestone bookkeeping per the v25 pattern (→ v26.0).
