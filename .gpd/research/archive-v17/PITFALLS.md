# Known Pitfalls Research — Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry

**Domain:** Riemannian geometry of symmetric cones (Faraut–Koranyi / Vinberg–Koszul), Hessian-of-cubic ("special real") geometry, octonionic Jordan algebra h_3(O), Peirce decomposition under a primitive idempotent, Riemannian→Lorentzian signature bridges, and the distinction between intrinsic bulk curvature and inherited/extrinsic slice curvature.
**Researched:** 2026-05-30
**Confidence:** HIGH on the four headline pitfalls named in the milestone prompt (homogeneity trap, octonionic cross-term association, signature/Wick bridge, GST/Weinberg circularity) — each is backed by published mathematics and by the corrected code already in this repo. MEDIUM on the exact form the false-positive will take in Phases B/C (depends on which signature bridge survives Phase A). The reward-hacking signatures are HIGH (each is a named risk in the prompt with a runnable disconfirming check below).

> **Milestone shape (read first).** v17.0 is a **KILL test**. Phase A asks the single decisive question: *after fixing E_11, is the inherited slice metric genuinely position-dependent, or homogeneous?* Phases B (matter-sourcing) and C (Einstein structure) run **only if A greenlights**. The dominant failure mode of this entire milestone is **fooling ourselves at the Phase A gate** — either a false KILL (gauging away real curvature, or mistaking the symmetric-cone's homogeneity for a slice property) or a false GREENLIGHT (reading a coordinate/Wick artifact as physical curvature). Every pitfall below is tagged with the phase that must guard it. The homogeneity trap (Pitfall 1) and the circularity guards (Pitfall 4) are the two that decide whether this milestone produces a trustworthy verdict.

---

## Critical Pitfalls

### Pitfall 1: THE HOMOGENEITY TRAP — confusing the bulk's homogeneity with a verdict on the slice (Phase A, DECISIVE)

**What goes wrong:**
The det=1 cone of h_3(O) is the Riemannian symmetric space E_{6(-26)}/F_4 (26-dim). **Every Riemannian symmetric space is homogeneous, geodesically complete, has constant scalar curvature, and has a covariantly constant (parallel) Riemann tensor: ∇R = 0** [Symmetric space, Wikipedia; Helgason; Eschenburg lecture notes]. So the *bulk* curvature scalars are literally the **same number at every point** of the cone, and E_{6(-26)} maps any point to any other isometrically. Two opposite errors both kill the project dishonestly:

- **False KILL (over-symmetrizing).** Reasoning "the cone is homogeneous, so the metric looks identical everywhere, so the slice metric is x-independent — route dead." This is wrong because the relevant object is not the bulk metric at a point; it is the metric induced on a *fixed* slice V_0 (with E_11 fixed) as the basepoint moves. Fixing E_11 **breaks** E_{6(-26)} down to Stab_{E_6}(E_11), and the question is whether that smaller group still acts transitively on (basepoint, slice) pairs. Homogeneity of the *full* cone does not imply homogeneity of the *slice-with-fixed-frame* family.
- **False KILL (gauging away real variation).** Using the residual symmetry Stab_{E_6}(E_11) to transform h_μν(x) to a constant form and declaring it homogeneous — when the transformation needed actually moves E_11 or the slice (i.e. is not in the residual stabilizer). A symmetry you are not allowed to use cannot be used to gauge away the field.
- **False GREENLIGHT (coordinate artifact).** Computing h_μν(x) in some coordinates, seeing the *components* vary with x, and concluding "position-dependent curvature." Metric components vary under any non-affine coordinate change even on flat space. Component variation is **not** curvature.

**Why it happens:**
"Symmetric space" and "homogeneous" are strong, seductive words that tempt a one-line dismissal. Conversely, h_μν component-watching tempts a one-line confirmation. Both skip the only invariant that matters.

**How to avoid (the clean invariant test — this IS the KILL gate):**
1. **Decide via curvature SCALARS / curvature TENSOR, never via metric components.** The honest question is: *does the intrinsic curvature of the inherited slice metric depend on the basepoint x?* Compute coordinate-invariant curvature quantities of g_μν(x): the Ricci scalar R(x), the Kretschmann scalar R_{abcd}R^{abcd}(x), and (decisively) check whether ∇R = 0. If all curvature invariants are **x-independent constants**, the slice carries a fixed homogeneous geometry → **KILL**. If a curvature invariant genuinely varies with x (after the stabilizer check below), the route survives.
2. **Do the honest stabilizer dimension count.** dim E_6 = 78, dim F_4 = 52, dim(E_{6(-26)}/F_4) = 26. The primitive idempotents form OP^2 = F_4/Spin(9), dim 16 (dim Spin(9)=36). Fixing E_11 picks a basepoint of OP^2-type data; compute dim Stab_{E_6}(E_11) and compare to the dimension of the basepoint family (the V_0 directions, ≤10, with the 4-dim h_2(C_u) sub-slice the physical part). If dim(basepoint family) > dim(orbit of Stab_{E_6}(E_11) through a basepoint), there exist **inequivalent** (basepoint, slice) pairs → genuine position dependence is *possible*. If the stabilizer orbit covers the whole family, all pairs are isometric → homogeneous → KILL. Report both dimensions explicitly; do not assert transitivity, compute it.
3. **Only the residual group may be used to simplify.** Any isometry invoked to put h_μν in normal form must lie in Stab_{E_6}(E_11) AND preserve the slice V_0. Log the group element used and verify it fixes E_11 and maps V_0→V_0 before trusting any "it's just a gauge artifact" claim.
4. **Use the Totaro / cubic-form curvature invariant as a cross-check.** For a Hessian metric of a cubic form, the full curvature tensor is fixed by the Hessian determinant and the **S-invariant of the cubic** [Totaro, "The curvature of a Hessian metric", math/0401381; "A curvature formula for the complexified index cone of a cubic form", arXiv:1007.2737]. Evaluating these invariants on the slice gives a coordinate-free flat-vs-curved verdict independent of any chart.

**Warning signs:**
- A homogeneity conclusion reached from the *words* "symmetric space" without computing a single curvature scalar. (Red flag.)
- A "position-dependent" claim supported only by varying metric *components*, with no curvature scalar shown to vary. (Red flag.)
- A "gauge artifact" dismissal that invokes an E_6 element not verified to be in Stab_{E_6}(E_11). (Red flag.)
- R(x) and R_{abcd}R^{abcd}(x) computed but only at ONE basepoint x (you cannot detect x-dependence from one point — see Pitfall 11).

**Phase to address:** **Phase A (the KILL gate itself).** This pitfall *is* Phase A. Get it right or the whole milestone is worthless.

---

### Pitfall 2: OCTONION NON-ASSOCIATIVITY in the cubic-norm cross-term — wrong association silently corrupts every downstream geometry (Phase A prerequisite to everything; Phase B critical)

**What goes wrong:**
The cubic norm cross-term `2 Re(triple)` is **association-sensitive** because octonions are non-associative: `(x1·x2)·x3 ≠ x1·(x2·x3)` and `Re((x1 x2) x3) ≠ Re(x1 (x2 x3))` in general. A prior bug in this very project (`trip_tracking.py`) coded `2 Re(x0(x1 x2))` where the milestone states the correct term is `2 Re(x2* x0* x1)`. A wrong association does not throw an error — it returns a plausible number, and **every** Hessian, every curvature, and every cross-term coupling V_0↔V_1/V_{1/2} built on it is silently wrong. Because the geometry is extracted from *derivatives* of det (the Hessian and its derivatives), the error is amplified, not averaged out.

**Why it happens:**
- Multiple inconsistent-looking conventions coexist in the live repo, all of which are correct for diagonal/real data but differ for genuine octonionic off-diagonal data:
  - `code/octonion_algebra.py` (lines 2143–2181): `N(X) = αβγ − α|x1|² − β|x2|² − γ|x3|² + 2 Re((x1·x2)·x3)`, with an explicit comment "**LEFT-to-right association (x1·x2)·x3, matching the Sarrus expansion … Do NOT use x1·(x2·x3)**." This is the corrected, gated implementation (ASSERT_CONVENTION `det_3_association=left_to_right_Re((x1*x2)*x3)`).
  - `rho_directional_derivatives.py` (header): writes `det = abc + 2 Re(x1 x2 x3) − …`, association unparenthesized — *safe only because that module perturbs in REAL directions* (`Re(real·real·real)` is association-free). It must NOT be reused for genuinely octonionic M.
  - The milestone prompt CAUTION names the correct term as `2 Re(x2* x0* x1)` and the bug as `2 Re(x0(x1 x2))` — a **third labeling** (conjugated, with a different index/slot naming `x0,x1,x2` vs `x1,x2,x3`).
  These are (intended to be) the SAME physical invariant written in different notations; the danger is treating them as interchangeable code, or "fixing" one to match another and silently changing the physics.

**How to avoid (verify the cross-term BEFORE any geometry — this is a hard gate):**
1. **Single source of truth.** Use `det_3` from the corrected `code/octonion_algebra.py` for all cubic-norm evaluations on octonionic data. Do not re-derive the cross-term inline; do not import the real-only form from `rho_directional_derivatives.py` for octonionic perturbations.
2. **Run the association-invariance pre-flight** on genuinely non-associative inputs (off-diagonal octonions with nonzero e_4..e_7 components, NOT just e_0..e_3 which sit in an associative subalgebra): confirm the implemented `det_3` equals the matrix/Sarrus determinant convention and document by how much `Re((x1·x2)·x3)` differs from `Re(x1·(x2·x3))` on a random non-associative triple (it should be NONZERO — if it is zero, your test inputs are accidentally associative and the test is vacuous).
3. **Multiplicativity check on commuting/associative subsets ONLY.** N(XY)=N(X)N(Y) holds for the cubic norm only when X,Y lie in an associative subalgebra (e.g. a common h_3(C_u) or diagonal). Verify N(XY)=N(X)N(Y) there; do NOT expect it to hold for generic octonionic X,Y and do NOT use a failure on generic inputs as evidence of a bug (that would be a false alarm masking the real convention question).
4. **Cayley–Hamilton / characteristic-polynomial check.** Verify X satisfies its cubic X³ − Tr(X)X² + S(X)X − N(X)I = 0 (Jordan-algebra Cayley–Hamilton) with the implemented N; this ties N, the trace, and the quadratic invariant S together and catches an inconsistent cross-term.
5. **Conjugation/order audit for the (V_{1/2},V_{1/2},V_0) block.** The matter coupling lives in the polarized cross-term; when M ∈ V_{1/2} is genuinely octonionic, the *order and conjugation* (`x2* x0* x1` vs `x0 x1 x2`) changes the V_0↔V_{1/2} coupling tensor. Re-derive the polarized d(·,·,·) on the Peirce basis (the `d_ijk_tensor` machinery exists) and confirm the (V_{1/2},V_{1/2},V_0) block matches between the prompt's convention and the code's convention; if they disagree, STOP and reconcile before Phase B.

**Warning signs:**
- A curvature or coupling result that changes when you swap `(x1·x2)·x3 ↔ x1·(x2·x3)` — means an association choice is load-bearing and must be the documented one (good that you caught it; bad if you didn't test).
- Any new inline reimplementation of the cubic norm anywhere in Phase A/B code.
- A "verification" of the cross-term done only on diagonal or e_0..e_3 (quaternionic) data — vacuous, because those subalgebras are associative.

**Phase to address:** **Phase A** must pass the cross-term gate before computing any Hessian (the homogeneity verdict depends on a correct det). **Phase B** is where the association most bites, because M ∈ V_1+V_{1/2} is genuinely octonionic and the cross-terms are the claimed source of curvature.

---

### Pitfall 3: SIGNATURE / WICK-ROTATION — spurious curvature, double-counted Minkowski, and a bridge that does not reduce to flat space (Phase A sub-task A0, then load-bearing through C)

**What goes wrong:**
The bulk metric g_X = Hess(−log det) is **Riemannian (positive-definite)**; physical spacetime is **Lorentzian**. The map between them (sub-task A0) is where false verdicts are manufactured:
- **Spurious curvature from a naive coordinate Wick rotation.** Substituting t→−it on a generic/curved metric is **coordinate-dependent and can yield complex or unintended-signature metrics**; the *same* space in different slicings gives *different* rotated metrics, and causal structure can silently vanish [Visser, "How to Wick rotate generic curved spacetime", arXiv:1702.05572]. A rotation done this way can generate curvature that is an artifact of the chart, not of the geometry — a direct false GREENLIGHT.
- **Double-counting the Minkowski background.** Construction (i) [restrict g_X to V_0 and Wick-rotate via u=e_7] and construction (ii) [take η from h_2(C_u)'s own det, let the cone-Hessian supply only h_μν] both have a Minkowski piece. Mixing them — e.g. taking η from h_2(C_u) AND keeping the η-like part of the restricted cone-Hessian — double-counts the flat background and fabricates an h_μν that is really just the background appearing twice.
- **A bridge that does not reduce to exact Minkowski at (M=0, center).** If the chosen bridge gives g_μν ≠ η_μν exactly when M=0 and x is at the center I/3, then the "perturbation" h_μν is contaminated by a constant offset that will masquerade as either a cosmological constant (Phase B false positive) or position dependence (Phase A false positive).

**Why it happens:**
Wick rotation is folklore-simple in flat space (t→−it) and physicists apply the folklore reflexively to curved/Hessian metrics where it is ill-defined. The two candidate constructions look interchangeable but are not, and the "reduces to Minkowski" check is easy to skip.

**How to avoid (keep the bridge honest):**
1. **Pick ONE bridge and state it precisely in A0; do not mix.** Per the prompt, select the construction that reduces to exact Minkowski at (M=0, center) and report which. Recommended default: **rotate the metric, not the coordinate**, using the algebra's own complex structure u=e_7 as the distinguished timelike direction (Visser's metric-rotation g_E = g_L + iε (V⊗V)/g_L(V,V) with V the u-direction). This is coordinate-independent and is the natural realization of the C*-bottleneck / Phase 46 mechanism. Construction (ii) (η from det of h_2(C_u), perturbation from the cone-Hessian) is the **cleaner default for keeping the background exact** and is recommended unless A0 shows it fails to capture the V_0↔matter coupling.
2. **Mandatory reduction test (gate).** Verify symbolically/exactly that at M=0, x=center: g_μν = η_μν with NO residual h_μν (machine-zero / exact-Q zero). If h_μν(center, M=0) ≠ 0, the bridge is contaminated — fix the bridge before drawing ANY conclusion. State eta's signature convention explicitly (this project: mostly-minus via det_2, per `metric_on_h2Cu=mostly_minus_via_det2`, `52-kkt-spacetime`).
3. **Curvature invariants must be computed in the LORENTZIAN metric, consistently.** Do not compute curvature in the Riemannian cone metric and then "rotate the answer" — rotate first (fix the bridge), then compute curvature scalars of the Lorentzian g_μν(x). Mixing Riemannian-curvature with Lorentzian-interpretation is a category error.
4. **Cross-check signature independence of the verdict.** The KILL/greenlight verdict (Pitfall 1) is about whether curvature *varies with x*; that question should be answerable in the Riemannian slice metric too (variation of curvature scalars is signature-robust). If the Riemannian restriction is homogeneous but the Lorentzian one looks curved, the curvature came from the rotation → artifact. Compute curvature-scalar x-dependence in BOTH the Riemannian restriction and the Lorentzian bridge; they must agree on *whether* curvature varies. Disagreement localizes the artifact to the bridge.

**Warning signs:**
- A nonzero h_μν at (M=0, center). (Bridge contaminated — hard stop.)
- Curvature that appears only after the Wick rotation and not in the Riemannian restriction. (Rotation artifact.)
- The verdict (homogeneous vs curved) changes depending on which coordinate chart the rotation is done in. (Ill-defined rotation — Visser's exact warning.)
- Complex-valued metric components after rotation. (Naive coordinate rotation — switch to metric rotation.)

**Phase to address:** **Phase A sub-task A0** must fix and validate the bridge (including the reduction-to-Minkowski gate) before Theorem A. The bridge then propagates as a fixed, documented choice through **B and C**; changing it mid-stream invalidates comparisons.

---

### Pitfall 4: CIRCULARITY / QUESTION-BEGGING — smuggling the answer (Einstein form) in via GST/supergravity/Weinberg inputs (Phase C critical; guards needed from Phase A)

**What goes wrong:**
The entire point of this route is to obtain gravity **intrinsically** from the cubic norm, NOT from a posited supergravity action. The dead route (`47-*`,`48-*`,`49-*`,`50-*`,`53-*`) posited the GST / N=2 Maxwell–Einstein supergravity Lagrangian with det as prepotential and *read off* the Einstein term — circular, because in 5D N=2 MESGT the **−½R Einstein–Hilbert coefficient is fixed by the supersymmetry structure**, and the *same* C_IJK tensor that defines the scalar (very special) geometry also fixes the vector couplings and the gravitational term [GST 1984, Nucl. Phys. B242 244; de Wit–Van Proeyen; 5D MESGT Lagrangian reviews]. The deadly subtlety: **the new route shares the SAME geometry** as GST — special-real / Hessian-of-cubic scalar manifolds ARE the 5D N=2 vector-multiplet scalar manifolds [special real geometry ↔ N=2 D=5, multiple refs]. So it is extremely natural to reach for a GST formula "because the geometry matches" and thereby silently re-import the assumed Einstein structure. Concrete circularity modes:
- **Lagrangian smuggling:** using any GST/supergravity bosonic Lagrangian, its −½R term, or its C_IJK→Einstein dictionary as an input.
- **Multiplet-data smuggling:** assuming the V_1/V_{1/2} sectors are a SUSY multiplet with prescribed couplings to the metric (the SUSY closure is exactly what fixes −R/2).
- **Soft-graviton / Weinberg smuggling:** invoking Weinberg's soft-graviton theorem or equivalence-principle universality to *argue* the coupling must be Einsteinian — that assumes the graviton and thus the answer.
- **Fitting to the target:** defining T_μν and κ, then *tuning* them so G_μν = κT_μν holds, and reporting "Einstein structure confirmed." This is curve-fitting, not derivation.

**Why it happens:**
The geometry genuinely coincides with GST's, the literature is GST-shaped, and "Einstein" is the hoped-for answer. Confirmation bias plus a matching reference set makes the circular step feel like legitimate cross-referencing.

**How to avoid (keep T_μν and the Einstein test independent of the conclusion):**
1. **Hard input ban (declare it in the plan).** Phase B/C may use ONLY: the cubic norm det (corrected association), its Hessian/derivatives, the Peirce decomposition under E_11, and the chosen signature bridge. **Forbidden inputs:** any supergravity/GST Lagrangian, the −½R coefficient, any SUSY transformation or multiplet assignment, Weinberg's soft theorem, the equivalence principle as a *premise*. GST may be cited **for the geometry of the manifold only** (it is the same E_{6(-26)}/F_4), never for the action or the gravitational coupling. Reference-set restriction: Faraut–Koranyi, Vinberg, Koszul, McCrimmon, Baez, Totaro — the *geometry/Jordan-algebra* literature, not the supergravity-action literature.
2. **Define T_μν purely from cross-term content, BEFORE computing G_μν.** Build the candidate stress-energy from the V_1/V_{1/2} cross-term data of M (the (V_{1/2},V_{1/2},V_0) coupling tensor) using only algebraic data — fix its normalization κ from something intrinsic (e.g. the cubic-norm normalization), NOT from matching G_μν. Freeze T_μν and κ, THEN test G_μν = κT_μν + Λg_μν. The test must be falsifiable: there must be a possible numeric outcome that says "NO."
3. **Report the honest level (a/b/c) without forcing.** Per the prompt: exact Einstein, linear-order Einstein, or not-at-all are all acceptable. "**Curved but not Einstein-structured**" is the *most likely real outcome* and is a legitimate, publishable result. Do NOT relabel a near-miss as a win.
4. **Independence audit (a checklist item):** for every equation used in Phase C, ask "could I have written this down without already knowing the answer is Einstein gravity?" If any step requires the supergravity dictionary, it is circular — flag and remove.

**Warning signs:**
- Any appearance of "−½", "16πG", a supergravity action, or "SUSY" in the Phase B/C derivation chain.
- κ or T_μν whose definition references G_μν. (Circular by construction.)
- A perfect G_μν = κT_μν that only holds at one tuned point or after a free constant was adjusted. (Fitting — see Pitfall 7/11.)
- Citing GST for anything other than "the manifold is E_{6(-26)}/F_4."

**Phase to address:** **Phase C** is where circularity is fatal, but the **input ban must be declared at Phase A planning** and enforced throughout. Phase B must define T_μν-precursors from cross-terms only.

---

### Pitfall 5: SLICE vs BULK CONFUSION — attributing bulk (constant) curvature to the slice, or mistaking extrinsic curvature for intrinsic gravity (Phase A and B)

**What goes wrong:**
g_μν(x) is the metric *induced on the V_0 slice* by the bulk cone geometry. The slice's **intrinsic** Riemann tensor is NOT simply the bulk Riemann tensor restricted to V_0 directions. By the **Gauss equation**, R^{slice}_{abcd} = (R^{bulk}_{abcd} restricted) + (second-fundamental-form / extrinsic-curvature terms) [Gauss–Codazzi, Wikipedia; do Carmo]. Two failure modes:
- **Attributing bulk curvature to the slice.** The bulk cone is a symmetric space with *constant* curvature scalars (Pitfall 1). If the slice is **totally geodesic** (second fundamental form II = 0), then R^{slice} = R^{bulk}|_slice = a CONSTANT — i.e. a totally-geodesic slice automatically inherits a homogeneous, x-independent curvature → KILL, and any "position dependence" seen would be an artifact. Whether the V_0 / h_2(C_u) slice is totally geodesic in the cone is a concrete computable question that **directly feeds the Phase A verdict** and must be checked.
- **Mistaking extrinsic curvature for intrinsic gravity.** If the slice is NOT totally geodesic, the extrinsic-curvature (II) terms contribute to R^{slice}. Reporting those II-driven terms as "matter-sourced gravity" conflates how the slice bends *inside* h_3(O) (embedding data) with intrinsic spacetime curvature (the gravitational claim). The gravitational claim requires the *intrinsic* curvature to vary with x and be sourced by M — not merely that the embedding bends.

**Why it happens:**
"Induced metric" invites the shortcut "restrict the bulk metric and read off the bulk curvature." The Gauss-equation correction is invisible unless you explicitly compute the second fundamental form.

**How to avoid:**
1. **Compute the second fundamental form of the V_0 (and h_2(C_u)) slice in the cone.** Decide explicitly whether the slice is totally geodesic. If II = 0: the slice curvature equals the bulk's *constant* curvature → expect homogeneity → KILL (and any apparent x-dependence is artifact — recheck Pitfalls 1 and 3). If II ≠ 0: proceed, but track the II contribution separately.
2. **Decompose R^{slice} via Gauss explicitly:** R^{slice} = R^{bulk}|_slice + (II∧II terms). Attribute any claimed "gravity" to the part that genuinely varies with x AND is sourced by M, not to the ambient-constant part and not to embedding-only II terms that survive at M=0.
3. **Intrinsic test only.** The gravitational verdict must rest on *intrinsic* curvature invariants of g_μν(x) (Ricci scalar, Kretschmann), which are computed from g_μν alone and are blind to the embedding. Use the bulk/extrinsic decomposition for *diagnosis*, the intrinsic invariants for the *verdict*.

**Warning signs:**
- A curvature computed by "restricting the bulk Riemann tensor" with no Gauss-equation / II term anywhere.
- "Position-dependent curvature" that persists at M=0 (likely extrinsic/embedding, not matter-sourced — see Pitfalls 6 and 10).
- The totally-geodesic question never asked.

**Phase to address:** **Phase A** (totally-geodesic check feeds the homogeneity verdict directly). **Phase B** (separate II/embedding curvature from M-sourced intrinsic curvature).

---

### Pitfall 6: FALSE-POSITIVE "curvature appears" that is actually pure cosmological constant (Phase B)

**What goes wrong:**
Turning on M, you observe nonzero Riemann tensor and conclude "matter sources curvature." But a nonzero curvature that is **maximally symmetric** (R_{abcd} ∝ (g_{ac}g_{bd} − g_{ad}g_{bc}), i.e. R_{ab} ∝ g_{ab}, constant R) is a **cosmological constant Λ**, not matter-sourcing. The prompt explicitly anticipates this: Phase B (a) must distinguish "flat (R=0)" from "pure Λ (R=const)" from genuine M-sourced inhomogeneous curvature. Declaring Λ-type curvature as "gravity sourced by matter" is a false positive.

**Why it happens:**
"Nonzero Riemann tensor" feels like success after a KILL-risk Phase A. The maximally-symmetric structure is easy to miss if you only look at "is R_{abcd} ≠ 0."

**How to avoid:**
1. **Decompose curvature into Ricci scalar (Λ part), traceless Ricci, and Weyl.** Genuine matter-sourcing must show structure beyond R_{ab} ∝ g_{ab} — a non-constant Ricci scalar, a nonzero traceless Ricci tracking M's distribution, and/or nonzero Weyl. A purely ∝ g_{ab} result with constant coefficient = Λ only.
2. **The cross-term off-switch test (the prompt's own (b)).** Replace det by the block-diagonal product det(V_1)·det(V_0) (kill the V_0↔V_1/V_{1/2} cross-terms). If the curvature *survives* this off-switch, it is NOT cross-term/matter-sourced — it is intrinsic to the cone (Λ-like) and the matter-sourcing claim fails. Genuine M-sourcing must VANISH when the cross-terms are switched off.
3. **Scaling test (the prompt's (c)).** Relate the curvature scale to ‖M‖ and ρ_J(X_bg). A true matter source scales with ‖M‖ (vanishes as M→0); a Λ does not. Curvature that persists at M=0 is Λ/intrinsic, not matter.

**Warning signs:**
- R_{abcd} ∝ (g g − g g) with a constant coefficient. (Pure Λ.)
- Curvature unchanged by the cross-term off-switch.
- Curvature that does not vanish as ‖M‖→0.

**Phase to address:** **Phase B** (this is precisely Theorem B parts a–c).

---

### Pitfall 7: FALSE-POSITIVE Einstein structure from a single tuned point or linearization sleight (Phase C)

**What goes wrong:**
Declaring G_μν = κT_μν + Λg_μν "holds" when it was checked at a single basepoint, with a single M, or after κ/Λ were tuned to fit. Or: claiming exact Einstein structure when only the *linear-in-M* relation holds (which is far weaker and often automatic once the right tensor structures are present). Both overstate the result.

**Why it happens:**
One clean data point is psychologically convincing, and the linear order is the easiest to satisfy. The hoped-for answer (Einstein) biases toward over-claiming.

**How to avoid:**
1. **Test over a FAMILY, not a point.** Vary M (direction and magnitude within V_1+V_{1/2}) and the basepoint x; the SAME κ, Λ must work for all. A κ that must be re-tuned per configuration is not a physical constant — it is a fit.
2. **State the honest order explicitly (a/b/c per prompt).** Exact, linear-only, or none. Linear-order agreement must be reported AS linear-order, not as "Einstein structure." Check at least the next order (M²) before any "exact" claim.
3. **Predefine κ and Λ.** Fix them from intrinsic data before the test (Pitfall 4.2). If the test then passes across the family with the predefined constants, it is real; if you had to solve for κ to make it pass, it is fitting.
4. **Falsifiability:** demonstrate a configuration that *could* have failed the Einstein test and report whether it did.

**Warning signs:**
- κ or Λ different for different M or different x.
- "Einstein structure" claimed from one (M, x) pair.
- "Exact" claimed with only first-order-in-M evidence.

**Phase to address:** **Phase C** (Theorem C honesty).

---

## Moderate Pitfalls

### Pitfall 8: Numerical curvature from catastrophic cancellation — float ranks/curvatures are unreliable here

**What goes wrong:**
Curvature is built from *differences of derivatives* of det (Christoffels ~ ∂g, Riemann ~ ∂Γ + ΓΓ). These are textbook catastrophic-cancellation factories: large nearly-equal terms subtract, and float64 returns noise. The project already flags float ranks/curvatures as unreliable for exactly this reason and works EXACT over Q. The danger: a float curvature scalar that is "1e-12" (really zero → would correctly KILL) read as "small but nonzero" (false greenlight), or a genuine small curvature drowned in 1e-10 float noise (false KILL).

**How to avoid:**
- **Work EXACT over Q (SymPy / rationals) for all curvature-deciding quantities.** Restrict octonionic data to rational components so det, Hessian, Christoffels, Riemann are exact. A curvature scalar that is *exactly* 0 over Q is a clean KILL; a curvature scalar that is a nonzero rational is a clean survive. Never decide KILL vs survive on a float magnitude.
- Use finite-difference float (as in `det3_quadratic_expansion_50`, which uses eps=1e-4 central differences) ONLY as a sanity cross-check against the exact result, never as the verdict. Note the existing `det3_quadratic_expansion_50` already shows the O(eps²) V_0 term = det_2 Gram (Minkowski, massless) — that is the *leading-order* homogeneity signal; Phase A must go to the order where x-dependence could first appear and do it exactly.
- Watch for eps-dependence: if the finite-difference curvature changes with eps, it is noise-dominated.

**Phase to address:** All phases; especially the Phase A verdict and the Phase C order-counting.

---

### Pitfall 9: rho_J expansion misused — real-direction perturbations hide the octonionic cross-term

**What goes wrong:**
`rho_directional_derivatives.py` expands around I/3 using **real** perturbations in the x_i slots (so `Re(x1 x2 x3) = δ1δ2δ3`, association-free). Reusing this module to characterize M ∈ V_1+V_{1/2} when M is genuinely octonionic (components along e_4..e_7) will silently use the wrong (real-only) cross-term and miss exactly the non-associative coupling that is the claimed source of curvature.

**How to avoid:**
- Use `rho_directional_derivatives.py` for the *scalar* off-center expansion (ρ_J around I/3) as intended, but recompute any *cross-term/coupling* quantity with the full octonionic `det_3` from `octonion_algebra.py` (Pitfall 2). Confirm M has nonzero e_4..e_7 components when testing the non-associative coupling, else the test is in an associative subalgebra and vacuous.

**Phase to address:** **Phase B** (off-center expansion and ‖M‖, ρ_J scaling).

---

### Pitfall 10: "Position-dependence" that is really off-center-ness (ρ_J) of the background, not a field on spacetime

**What goes wrong:**
The background X_bg = I/3 + M is off-center (ρ_J > 0). Moving the basepoint and seeing the metric change could reflect (i) genuine x-dependence of the inherited slice metric (the gravitational claim), or (ii) merely that you evaluated at different off-center points where the homogeneous metric *looks* different in your fixed chart. Conflating the background's off-center-ness with a propagating spacetime field h_μν(x) is a subtle false greenlight feeding Pitfall 1.

**How to avoid:**
- Separate the roles cleanly: ρ_J(X_bg) parametrizes the *basepoint* (one number characterizing off-center-ness); h_μν(x) is supposed to be a *field over the spacetime coordinate x ∈ V_0*. Test x-dependence at FIXED background off-center-ness, and test curvature-invariant variation (Pitfall 1), not component variation.
- Use the stabilizer argument (Pitfall 1.2): if Stab_{E_6}(E_11) relates two basepoints, the apparent difference is gauge, not field.

**Phase to address:** **Phase A** (distinguishing field from frame), **Phase B** (ρ_J scaling).

---

### Pitfall 11: Single-point sampling cannot detect x-dependence

**What goes wrong:**
Computing curvature scalars at one basepoint and concluding "homogeneous" (because you have nothing to compare) or "curved" (because the number is nonzero — but a constant nonzero curvature is still homogeneous!). x-dependence is a statement about a *function* of x; one sample determines nothing about variation.

**How to avoid:**
- Evaluate curvature invariants symbolically as functions of x (exact, preferred), or at a *grid* of ≥3 generic basepoints, and test whether they actually vary. A nonzero-but-constant curvature scalar across all samples = homogeneous (KILL), not survive. Explicitly compute ∂_x(curvature invariant) and check it is not identically zero over Q.

**Phase to address:** **Phase A.**

---

## Minor Pitfalls

### Pitfall 12: Convention drift in the Peirce/spacetime index assignment

**What goes wrong:** The spacetime V_0 indices are a specific subset (`spacetime_V0_indices={17,18,19,26}`, `internal_V0_indices={20..25}` per `octonion_algebra.py` ASSERT_CONVENTION), and the h_2(C_u) sub-slice uses u=e_7. Picking the wrong 4 of the 10 V_0 directions, or a different complex structure, gives a metric that is not the Minkowski slice and breaks the reduction test.

**How to avoid:** Pin the spacetime sub-slice to the documented `{17,18,19,26}` / h_2(C_u) with u=e_7; verify the restricted det_2 on this sub-slice equals the Minkowski quadratic form (per `52-kkt-spacetime`) before building g_μν.

**Phase to address:** Phase A (A0).

### Pitfall 13: Mostly-plus vs mostly-minus signature sign errors in curvature

**What goes wrong:** This project uses mostly-minus via det_2. Curvature-tensor and Einstein-tensor sign conventions (and the sign of Λ) depend on signature and on the Riemann sign convention; a mismatch flips the sign of "the curvature" and can flip a Λ sign.

**How to avoid:** State the Riemann/Ricci sign convention alongside the mostly-minus signature; verify on a known case (e.g. the H^3 = SL(2,C)/SU(2) hyperboloid sub-slice has known constant negative curvature — use it as a signed benchmark).

**Phase to address:** Phase A/B.

---

## Approximation Shortcuts

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
| --- | --- | --- | --- |
| Float64 finite-difference curvature | Fast, easy | Catastrophic cancellation → unreliable KILL/survive verdict | ONLY as a cross-check of an exact-Q result; NEVER for the verdict |
| Real-only perturbations (rho module) for M | Association-free, simple | Misses the non-associative V_0↔V_{1/2} coupling = the claimed source | For the scalar ρ_J expansion only; never for octonionic cross-term coupling |
| Linearize in M | Tractable Einstein test | Linear agreement is weak/often automatic; not "exact Einstein" | Acceptable as Phase C level (b) IF reported as linear-only, not as a win |
| Diagonal/quaternionic (e_0..e_3) test data | Easy hand-checks | Lives in an associative subalgebra → association bugs invisible | Sanity checks only; the real test needs e_4..e_7 components |
| Restrict bulk metric, read bulk curvature | Skips Gauss equation | Ignores second-fundamental-form term; conflates extrinsic/intrinsic | Only if the slice is PROVEN totally geodesic (then verify it gives constant curvature) |
| Cite GST for the geometry | Legit (same manifold) | One step from citing GST for the action (circular) | Geometry/manifold facts ONLY; never the Lagrangian or −½R |

## Convention Traps

| Convention Issue | Common Mistake | Correct Approach |
| --- | --- | --- |
| Cubic-norm cross-term association | Treating `2Re((x1·x2)·x3)`, `2Re(x1·(x2·x3))`, and the prompt's `2Re(x2* x0* x1)` as interchangeable code | Use corrected `det_3` (`octonion_algebra.py`, left-to-right `(x1·x2)·x3`); verify the prompt's conjugated form equals it on non-associative data before trusting either |
| Real-perturbation det vs octonionic det | Importing `rho_directional_derivatives.py`'s unparenthesized `2Re(x1 x2 x3)` for octonionic M | That form is real-only-safe; for octonionic M use full `det_3` |
| Metric signature | Mixing mostly-plus and mostly-minus across the Riemannian cone, the det_2 Minkowski form, and curvature conventions | Project standard: mostly-minus via det_2; state Riemann/Ricci sign convention explicitly; benchmark on H^3 |
| Riemannian vs Lorentzian curvature | Computing curvature in g_X (Riemannian) then "rotating the result" | Fix the signature bridge FIRST, compute curvature in the final Lorentzian g_μν |
| d(X,X,X) normalization | Forgetting d(X,X,X)=6·N(X) (this project's convention) | Use the gated normalization; C_IJK=(1/6)d_IJK per `octonion_algebra.py` |
| GST geometry vs GST action | "The manifold is E_{6(-26)}/F_4, so use the GST Lagrangian/−½R" | Manifold identification is fine; the action and gravitational coupling are the forbidden circular input |
| Wick rotation: coordinate vs metric | t→−it on the curved/Hessian metric | Rotate the metric via the u=e_7 direction (Visser); coordinate rotation is ill-defined here |

## Numerical Traps

| Trap | Symptoms | Prevention | When It Breaks |
| --- | --- | --- | --- |
| Catastrophic cancellation in Christoffel/Riemann | Curvature scalar ~1e-10..1e-12, eps-dependent | Exact-Q (rational) arithmetic; SymPy | Whenever curvature is decided from float differences of det-derivatives |
| Float "rank"/"curvature" near a degenerate point | Apparent rank jumps; tiny eigenvalues | Exact-Q rank/curvature; the project already flags floats unreliable | Near the center I/3 and near det→0 (cone boundary) |
| Vacuous association test (associative inputs) | "Cross-term verified" but on diagonal/e_0..e_3 data | Use e_4..e_7 components so `Re((x1x2)x3)≠Re(x1(x2x3))` | Any test confined to an associative subalgebra |
| eps-sensitivity of finite-difference Hessian | Mass matrix / curvature changes with eps | Compare to exact polarized result (`_polarized_sharp`) | Higher-derivative (curvature) order, where existing eps=1e-4 may be too coarse |
| Degenerate metric in Wick rotation | Metric singular/complex at ε=+i | Avoid ε=+i; use Visser's safe continuation | Naive rotation through the degenerate point |

## Interpretation Mistakes

| Mistake | Risk | Prevention |
| --- | --- | --- |
| "Symmetric space ⇒ slice metric is x-independent" | False KILL of a live route | The slice-with-fixed-E_11 family is a DIFFERENT question; decide by curvature invariants + stabilizer count, not by the word "symmetric" |
| "Metric components vary with x ⇒ curvature" | False GREENLIGHT | Components vary under coordinate changes even on flat space; use curvature scalars |
| "Nonzero Riemann ⇒ matter-sourced gravity" | False positive (could be Λ) | Off-switch the cross-terms; check ‖M‖→0 vanishing; decompose Ricci/Weyl |
| "Restricted bulk metric's curvature = slice gravity" | Conflates extrinsic/intrinsic | Gauss equation: separate II terms; verdict on intrinsic invariants only |
| "Linear-in-M Einstein relation ⇒ Einstein gravity" | Overclaim | Report the honest order (a/b/c); test M² before "exact" |
| "Curvature after Wick rotation ⇒ physical" | Rotation artifact | Confirm same curvature-variation verdict in the Riemannian restriction |
| Softening a homogeneous KILL to "approximately position-dependent" | Dishonest reporting; the prompt explicitly forbids this | A homogeneous result is a clean, valuable KILL — report it as such and STOP |

## "Looks Correct But Is Not" Checklist

- [ ] **Homogeneity verdict:** Often missing the curvature-scalar x-dependence test and the Stab_{E_6}(E_11) dimension count — verify R(x), Kretschmann(x), ∂_x of each, AND dim(stabilizer orbit) vs dim(basepoint family).
- [ ] **Cubic norm:** Often missing the non-associative test input — verify `Re((x1x2)x3) ≠ Re(x1(x2x3))` on e_4..e_7 data and that `det_3` matches the prompt's conjugated convention.
- [ ] **Signature bridge:** Often missing the reduction gate — verify g_μν(center, M=0) = η_μν EXACTLY with zero residual h_μν.
- [ ] **Slice curvature:** Often missing the second fundamental form — verify whether the slice is totally geodesic and decompose R^{slice} via Gauss.
- [ ] **Matter-sourcing (B):** Often missing the cross-term off-switch — verify curvature VANISHES when det→det(V_1)·det(V_0) and as ‖M‖→0.
- [ ] **Einstein test (C):** Often missing family-robustness — verify the SAME predefined κ, Λ work across multiple (M, x), not one tuned point.
- [ ] **Circularity (C):** Often missing the input audit — verify no −½R, no SUSY, no GST action, no Weinberg soft theorem entered the derivation.
- [ ] **Exactness:** Often missing exact arithmetic — verify the KILL/survive verdict rests on exact-Q zero/nonzero, not a float magnitude.

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
| --- | --- | --- |
| Wrong cross-term association used | HIGH | Recompute det_3 with corrected association; redo ALL Hessians/curvatures downstream (nothing built on the wrong norm survives) |
| Contaminated signature bridge (h_μν≠0 at M=0,center) | MEDIUM | Re-fix the bridge (switch to construction (ii) or Visser metric-rotation), re-run reduction gate, recompute h_μν |
| Float-based KILL/survive verdict | MEDIUM | Redo the deciding curvature in exact-Q; the qualitative verdict may flip |
| Λ mistaken for matter-sourcing | LOW | Apply cross-term off-switch + ‖M‖→0 test; relabel honestly |
| Single-point homogeneity claim | LOW | Recompute curvature invariants symbolically in x or over a basepoint grid |
| Circular Einstein "confirmation" | HIGH | Audit inputs; remove any supergravity/SUSY/Weinberg step; redefine κ,T_μν intrinsically; re-test (may downgrade verdict to "curved not Einstein") |
| Extrinsic curvature reported as gravity | MEDIUM | Compute II; decompose via Gauss; restate verdict on intrinsic invariants |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
| --- | --- | --- |
| 1. Homogeneity trap (false KILL / false greenlight) | **Phase A (gate)** | Curvature scalars as functions of x are constant ⇒ KILL; vary ⇒ survive; stabilizer-orbit dim vs basepoint-family dim computed and reported |
| 2. Octonion cross-term association | **Phase A (pre-flight), Phase B** | `det_3` matches matrix-determinant on non-associative data; prompt's conjugated form reconciled; Cayley–Hamilton holds |
| 3. Signature/Wick bridge | **Phase A sub-task A0** | One bridge fixed; g_μν(center,M=0)=η exactly; curvature-variation verdict agrees between Riemannian and Lorentzian |
| 4. GST/Weinberg circularity | **Phase C (fatal), declared at Phase A** | Input audit shows no −½R/SUSY/GST-action/Weinberg; κ,T_μν defined before G_μν computed |
| 5. Slice vs bulk / extrinsic curvature | **Phase A, Phase B** | Second fundamental form computed; totally-geodesic question answered; R^{slice} Gauss-decomposed |
| 6. Λ mistaken for matter-sourcing | **Phase B** | Cross-term off-switch removes curvature; curvature ∝ ‖M‖ and vanishes at M=0 |
| 7. Tuned-point / linear-order Einstein overclaim | **Phase C** | Same κ,Λ across (M,x) family; honest a/b/c level reported |
| 8. Float curvature cancellation | **All phases** | Verdict from exact-Q zero/nonzero; float used only as cross-check |
| 9. rho_J real-perturbation misuse | **Phase B** | Octonionic M (e_4..e_7) uses full det_3, not the real-only form |
| 10. Off-center-ness vs field | **Phase A, B** | x-dependence at fixed ρ_J; gauge-vs-field separated via stabilizer |
| 11. Single-point sampling | **Phase A** | Curvature invariants symbolic in x or sampled at ≥3 basepoints |
| 12. Peirce/spacetime index drift | **Phase A (A0)** | Sub-slice = {17,18,19,26}/h_2(C_u), u=e_7; det_2 restriction = Minkowski form |
| 13. Signature/Riemann sign | **Phase A/B** | Sign convention stated; benchmarked on H^3 constant negative curvature |

## Sources

- **Faraut & Koranyi, *Analysis on Symmetric Cones* (1994)** — cone metric g_X = Hess(−log det), symmetric-space structure of the det=1 hypersurface. HIGH (standard reference).
- **Symmetric space (Wikipedia); Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*; Eschenburg, "Lecture Notes on Symmetric Spaces"** — every Riemannian symmetric space is homogeneous, geodesically complete, constant scalar curvature, ∇R = 0. HIGH. (https://en.wikipedia.org/wiki/Symmetric_space)
- **B. Totaro, "The curvature of a Hessian metric," math/0401381** — full Riemann tensor of a Hessian-of-cubic metric determined by the Hessian determinant and the S-invariant of the cubic; flat/symmetric criteria. HIGH (the coordinate-free curvature test for the homogeneity gate). PDF was not text-extractable via automated fetch; cited from the published abstract/title and corroborating search results — confirm the explicit formula against the journal version (Math. Ann.) when implementing. (https://arxiv.org/pdf/math/0401381)
- **"A curvature formula for the complexified index cone of a cubic form," arXiv:1007.2737** — explicit curvature of the cubic-form Hessian metric. MEDIUM–HIGH.
- **M. Visser, "How to Wick rotate generic curved spacetime," arXiv:1702.05572** — naive coordinate Wick rotation is coordinate-dependent and yields complex/unphysical metrics; rotate the metric via a chosen timelike vector field; reduce to flat-space results. HIGH for the signature-bridge pitfall. (https://ar5iv.labs.arxiv.org/html/1702.05572)
- **Gunaydin, Sierra, Townsend, "The Geometry of N=2 Maxwell–Einstein Supergravity and Jordan Algebras," Nucl. Phys. B242 (1984) 244** — the GST scalar manifold E_{6(-26)}/F_4; the −½R Einstein term and vector couplings are fixed by the SAME C_IJK / SUSY closure (the circular input to avoid). Cite for GEOMETRY ONLY. HIGH. 5D MESGT Lagrangian structure corroborated by hep-th/0304109, hep-th/9912027.
- **de Wit & Van Proeyen, "Special geometry, cubic polynomials and homogeneous quaternionic spaces," hep-th/9112027 (Commun. Math. Phys. 149 (1992) 307)** — classification of homogeneous special-real manifolds; symmetric (magic, incl. E_{6(-26)}/F_4) vs non-symmetric L(q,P); special-real ↔ N=2 D=5 scalar manifolds. HIGH.
- **Gauss–Codazzi equations (Wikipedia); do Carmo, *Riemannian Geometry*** — intrinsic submanifold curvature = restricted ambient curvature + second-fundamental-form terms; totally geodesic ⇒ II=0 ⇒ R^{slice}=R^{ambient}|_slice. HIGH. (https://en.wikipedia.org/wiki/Gauss%E2%80%93Codazzi_equations)
- **Baez, "The Octonions," math/0105155 (2002)** — h_3(O), F_4=Aut, OP^2=F_4/Spin(9) (dim 16), cubic norm det formula and association convention. HIGH.
- **McCrimmon, *A Taste of Jordan Algebras*** — Peirce decomposition, cubic norm, Cayley–Hamilton, quadratic representation. HIGH.
- **In-repo (HIGH, local):** `code/octonion_algebra.py` lines 2143–2181 (corrected `det_3`, left-to-right association, ASSERT_CONVENTION block) and `det3_quadratic_expansion_50` (V_0 O(eps²) term = det_2 Gram = massless/homogeneous at leading order — the leading homogeneity signal Phase A must push past); `rho_directional_derivatives.py` (real-perturbation ρ_J expansion — real-only-safe); `peirce_coupling.py` (Peirce decomposition under E_11); phase work `52-kkt-spacetime`, `52-observer-uniqueness` (h_2(C_u)≅R^{3,1}, mostly-minus from det_2, so(4,2)). Prior bug of record: `trip_tracking.py` `2Re(x0(x1 x2))` vs correct `2Re(x2* x0* x1)`.

---

_Known pitfalls research for: gravity as intrinsic curvature of the h_3(O) symmetric-cone bulk geometry inherited by a Peirce spacetime slice (milestone v17.0)._
_Researched: 2026-05-30_
