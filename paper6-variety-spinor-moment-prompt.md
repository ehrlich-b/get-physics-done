# GPD Prompt — The Spinor Moment: the Tangent-Valued Matter Field and its Topology (J5-on-the-variety, step 4)

**Slot 88 / v28.0-candidate. STATUS: RATIFIED-BY-STANDING-DIRECTIVE
(Bryan, 2026-06-11). Ready to run.**

_Context: v27.0 COMPLETE (commit 199614c6) — the scalar sector CLOSES
into the local balance law c_R(1−c_R)λ² = −|π_{1/2}M|²·G_M. Certified
assets this run consumes: the moment doublet and field equations
(v25), the response field G_M and the sourced equation (v26), the
balance law and the gradient calculus dφ_Y ↦ π_{1/2}^{(p)}(Y) (v27),
the tangent identification T_p = J_{1/2}(p) (16-dim; cut 4-dim), the
16 recorded families, and the v22.0 result (slot 82: the gluing
holonomy between observers' slices is an UNFORCED U(1) — the joint
pair-stabilizer is Spin(8), the slice action one compact SO(2), the
C_u phase). This run builds the object both Gate-5 ledgers point at:
the SPINOR MOMENT — the tangent-valued matter field — and extracts
its exact zero/index/winding structure. Per v27-LIVE this object is
the natural next step, NOT forced; declared accordingly._

_FENCE (standing, important): this is NOT the dead v18/v20
Cartan/MM-connection route. That route built a spacetime connection
from FIBER data and is closed. Here the variety is the candidate
BASE, and the question is the kinematics of its own tangent gluing
vs matter. No gravity claims, no metric law, no selection law in
this run; the connection-SELECTION question is routed to the v29
ledger._

_Discipline: v21–v27 pattern — executor + independent verifier
(separate code path), exact over Q / Q(t), fail-fast gates, controls
with known answers. No Einstein, no Newton constant, no G = κT, no
dark-matter, no geodesic-motion language._

## Pre-read: milestone type (pre-registered)

**Verification-and-extraction** (v25/v26 class), declared up front:
the central facts below come with derivation sketches and hand-checked
anchors, and the topology is classical mathematics ONCE the
identifications are made — ⟨X,p⟩ restricted to the cut is a
moment-map-type Morse function (for diagonal X it IS the torus moment
map on CP²; Atiyah / Guillemin–Sternberg — cite, do not claim). The
program-specific content: (i) the spinor moment IS the gradient field
of the certified v24 landscape, (ii) its zeros are exactly the matter
EIGENFRAME events, (iii) the index/winding data is matter-pinned
gluing data for the v22-unforced U(1) at the level of the TOPOLOGICAL
CLASS, on both the cut and the mother space. The one genuinely open
identification = Gate 0 (the v22 dictionary); if it fails, STOP and
report (more informative than proceeding). Expected outcome: PASS
with the winding numbers as the extracted new numbers.

## The setup (verify every step; hand-checked anchors)

**The object.** For a state X and event p (rank-1 idempotent), the
spinor moment is the Peirce-1/2 projection

> **s_X(p) := π_{1/2}^{(p)}(X) ∈ J_{1/2}(p) = T_p(variety).**

By the v27 gradient calculus, **s_X = dφ_X, the gradient field of
φ_X(p) = ⟨X,p⟩** (equivalently −dm): the tangent-valued matter field
is not a new construction — it is the v24 landscape's own gradient.
Its norm is scalar-local: in the trace form,
‖s_X‖²_tr = TrX² − a_X² − (TrX − a_X)² + 2c_X with a_X = ⟨X,p⟩,
c_X = ⟨X#,p⟩ (Peirce orthogonality + Tr C_pX = TrX − a_X,
det₂C_pX = c_X; for traceless M this is the v27
2(½TrM² − a² + c)). Its DIRECTION is the data the scalars miss (v24
direction-resolution).

**Zeros = the eigenframe.** s_X(p) = 0 ⟺ X ∈ J_1(p) ⊕ J_0(p) ⟺ p
is compatible with the spectral frame of X. For X with DISTINCT
eigenvalues (spectral theorem in h₃(O), recorded): exactly the three
eigenframe idempotents {p₁, p₂, p₃} — three isolated zeros, on the
cut (when X ∈ h₃(C_u)) and on OP² alike. Degenerate spectra give
positive-dimensional zero sets — recorded STRATA, excluded from index
claims (the #9 discipline; the vacuum X = I/3 has s ≡ 0 identically:
the vacuum singles out NO events, consistent with v24 homogeneity —
this is a Gate-1 control, not a defect).

**Indices and the Euler closure (hand-checked).** Wlog X =
diag(x₁ > x₂ > x₃) (F₄ spectral + covariance). φ_X is Morse off the
degenerate strata with critical points E_11, E_22, E_33 and critical
values x₁, x₂, x₃. Tangent directions at E_ii split by which other
diagonal they move toward: at E_22, the (1,2)-block directions raise
φ toward x₁, the (2,3)-block directions lower it toward x₃ ⇒ Morse
index (as a MAXIMUM-counting index of φ): cut (4, 2, 0) at
(E_11, E_22, E_33); OP² (16, 8, 0). Poincaré–Hopf for the gradient
s_X: index(p_i) = (−1)^{Morse index} = +1 at each (all even) ⇒

> **Σ indices = 3 = χ(CP²) = χ(OP²)** — the Euler closure must come
> out EXACTLY on both spaces (χ(OP²) = 3, b₀ = b₈ = b₁₆ = 1, Borel —
> recorded math; cite).

Quantitative anchor (hand-checked, t-parametrization of the recorded
families, NOT geodesic-normalized — flag the bookkeeping): along the
(1,2)-family from E_11, φ_X(t) = x₁ + (x₂ − x₁)s² with
s = 2t/(1+t²), so **φ''(0) = 8(x₂ − x₁)**; the four cut directions
give Δφ(E_11) = ¼[2·8(x₂−x₁) + 2·8(x₃−x₁)] = 4(x₂ + x₃ − 2x₁), which
must equal the v25 field equation −λ₁(φ − φ̄) = −12(x₁ − TrX/3) —
they agree identically (hand-checked). This cross-check is a Gate-1
control wiring v28 to the certified v25 machinery.

**The U(1)/winding refinement (the v22 contact).** On the cut, the
tangent J_{1/2}(E_11) ∩ h₃(C_u) is two C_u-lines ((1,2) and (1,3)
entries); multiplication by the C_u phase is one compact SO(2) on
this tangent. Gate 0 must establish the DICTIONARY: this SO(2) is
the same one-parameter compact group v22.0 isolated as the slice
action / unforced gluing U(1) (slot-82 artifacts; joint
pair-stabilizer Spin(8), one SO(2) = the C_u phase). Pre-registered
expectation: YES (both are "the C_u phase acting on off-diagonal
data"); if the identification FAILS, STOP — the run's framing is
wrong and that is the finding. Given the dictionary: around each
isolated zero, s_X has an integer index (degree on a small sphere),
and on the cut its C_u-phase decomposition carries WINDING data —
the matter field's zeros and windings are X-determined, i.e. **the
first matter-pinned gluing data for the v22-unforced U(1), at the
level of the topological class.** The extracted new numbers = the
per-zero winding decomposition (cut: degree on S³ refined by the two
C_u-lines; report exactly what is computed, with conventions stated).

## Claims

**E1 — the identification (the unification).** s_X = dφ_X exactly
(one-line Peirce proof, verified symbolically at E_11 + along all 16
families); the norm formula ‖s_X‖²_tr above verified for general
(non-traceless) X; the direction data is NOT scalar-determined
(exhibit: two X with equal (a_X, c_X, TrX², detX) at a p and
different s_X direction — the v27 negative-anchor pair M₀/M_{e₁}
shifted by I works if it still does after the TrX ≠ 0 generalization;
otherwise construct one).

**E2 — zeros = the eigenframe.** For distinct spectrum: the zero set
of s_X is exactly {p₁, p₂, p₃} on OP², intersecting the cut exactly
when X ∈ h₃(C_u) (then all three are cut points). Verified
symbolically for diagonal X and for at least one NON-diagonal
u-complex X (rotated frame) and one genuinely octonionic X (rotated
into an e_k direction — the zero set follows the frame; F₄-covariance
made explicit, not assumed). Degenerate-spectrum strata recorded
(X = I/3 ⇒ s ≡ 0; two equal eigenvalues ⇒ a CP¹/S⁸-type zero
locus — identify it exactly and record, no index claims there).

**E3 — the topology (the extraction).** For diagonal X with
x₁ > x₂ > x₃: Morse indices (4,2,0) on the cut and (16,8,0) on OP²
(computed from exact Hessians along the recorded families, the
φ''(0) = 8(x₂−x₁) anchor reproduced); Poincaré–Hopf indices +1 each;
**Σ = 3 = χ on BOTH spaces** (the Euler closure exact). The
C_u-winding decomposition at each zero on the cut computed exactly
and reported with stated conventions (the new numbers). The v25
cross-check Δφ(E_11) = 4(x₂+x₃−2x₁) = −12(φ−φ̄)(E_11) exact.

**E4 — the reading (fenced).** The v22-unforced U(1) now has
matter-pinned TOPOLOGICAL data: the zeros (where), the indices
(how much), both X-determined; what remains unforced is the LOCAL
FORM of the gluing — that question (is there a canonical
matter-aligned connection, and what selects it) is the v29 fork,
NOT claimed here. No gravity language: this is connection-KINEMATICS
on the candidate base. The vacuum pins nothing (s ≡ 0) — matter is
what creates the topological skeleton; state this as the one-sentence
reading.

## Gates

- **Gate 0 — the v22 dictionary (fail-fast).** Load the slot-82
  construction; verify the slice SO(2) = C_u-phase multiplication on
  J_{1/2}(E_11) ∩ h₃(C_u) (explicit generator match, exact). Expected
  YES; on NO: STOP and report the mismatch.
- **Gate 1 — controls (known answers, zero weight).** (i) X = I/3 ⇒
  s_X ≡ 0 at E_11 and along all 16 families; (ii) diagonal X ⇒
  s_X(E_ii) = 0 exactly; (iii) the φ''(0) = 8(x₂−x₁) anchor; (iv) the
  v25 cross-check Δφ = −λ₁(φ−φ̄) at E_11 from the family Hessians;
  (v) ‖s_X‖²_tr formula vs direct computation on a rational battery.
- **Gate 2 — E1 + E2** (symbolic; the non-diagonal and octonionic
  frame-following checks are the load-bearing part — no
  diagonal-only shortcut).
- **Gate 3 — E3 on the cut** (indices + Euler closure + the
  C_u-winding decomposition with conventions stated).
- **Gate 4 — E3 on OP² + E4** (the 16-dim index computation may use
  the family Hessians + Peirce block structure; the Euler closure
  Σ = 3 must be exact).
- **Gate 5 — the v29 ledger (exploratory, non-blocking, NO claims).**
  Price: (i) the form-selection fork — given the matter-pinned class,
  is there a canonical matter-aligned connection on the cut tangent
  (existence/uniqueness as an exact question; what functional would
  select it — flag any import); (ii) the claim-2 contact
  (K_face(m,q) consumption note, standing); (iii) whether the v27
  balance law has a covariant statement along the matter field's
  flow lines (a derivative-of-the-law question, priced only).
- **STOP rule:** any broken setup step (the s_X = dφ_X identity, the
  anchor values, the Gate-0 dictionary) = a design hole = report and
  STOP.

## Guards (pre-registered)

1. **Strata discipline.** Index/winding claims ONLY for distinct
   spectrum; degenerate strata recorded, excluded (the vacuum s ≡ 0
   is a control, not a defect).
2. **Exactness.** All verdict-path computations over Q/Q(t); winding
   integers from exact algebra (resultants/degree counts), not
   numeric integration.
3. **Normalization bookkeeping.** The t-parametrization is NOT
   geodesic-normalized — the 8's and ¼'s must be tracked once,
   stated once (the v25 λ₁ convention is the reference); no silent
   renormalization between gates.
4. **Classical-vs-program honesty.** χ = 3, the Morse structure, and
   torus moment maps on CP² are classical (cite Borel; Atiyah/GS);
   the program-content is the identification (spinor moment =
   landscape gradient; zeros = eigenframe; v22 dictionary). Do not
   present imported topology as a derived result; do not let the
   import disguise the genuinely new numbers (the winding
   decomposition).
5. **The octonion product-order trap (standing).** conj(x₃x₂)-type
   entries; independent implementations must agree on an octonionic
   battery before any verdict computation.
6. **Language fence.** No Einstein, no Newton constant, no G = κT,
   no dark matter, no geodesic-motion/force language, no "gravity =
   connection" (the v18/v20 corpse stays buried — this is base
   tangent kinematics); "matter-pinned" refers to the topological
   class only.

## Deliverables

`derivations/88-VERDICT.md` (E1–E4, scope stated);
`derivations/88-GATE-N-SUMMARY.md` per gate;
`derivations/88-spinor-moment-RESEARCH.md` (the identification, the
zero/index/winding structure, the v22 dictionary, the E4 reading,
the v29 ledger); `code/variety_spinor_moment.py` (executor) +
`code/variety_spinor_moment_verify.py` (independent path; an
`_indep_check.py` third path welcome, v26/v27-parity). Commit; HOLD
the v28.0 milestone bookkeeping for ratification, mirroring v25–v27.
