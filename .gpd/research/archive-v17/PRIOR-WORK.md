# Prior Work: Intrinsic Curvature of the h_3(O) Bulk and the V_0 Spacetime Slice

**Surveyed:** 2026-05-30
**Domain:** Riemannian/Hessian geometry of symmetric cones; exceptional Jordan algebra h_3(O); geometry (only) of cubic-norm scalar manifolds; emergent-gravity-from-Jordan attempts.
**Milestone:** v17.0 — "Gravity as intrinsic curvature of the h_3(O) bulk geometry" (fresh route; explicitly NOT lattice/Fisher, NOT det/GST/Weinberg supergravity Lagrangian).
**Confidence:** HIGH on the established cone/curvature math (Q1, Q2, Q5 mostly resolved by canonical references); HIGH on the novelty flag (Q3 slice-curvature question is unaddressed in the located literature).

> **Scope discipline (per prompt).** This file surveys ONLY what bears on whether the
> V_0 = h_2(O) Peirce slice inherits position-dependent, matter-sourced curvature from the
> h_3(O) cubic-norm cone geometry. The two dead routes — (i) lattice/Fisher continuum limit,
> (ii) det/GST/Weinberg N=2 supergravity *Lagrangian* — are NOT cited as load-bearing. Where a
> supergravity-adjacent reference is used (de Wit–Van Proeyen, Gunaydin–Sierra–Townsend), ONLY
> its differential-geometric content (metric, curvature, classification) is taken; their
> Lagrangian / SUSY content is explicitly excluded.

---

## TL;DR for the roadmapper (read this first)

1. **The bulk geometry is completely pinned down by a single classical theorem.** The cone metric
   `g_X = Hess(-log det X)` and the `{det=1}` symmetric space `E6(-26)/F4` are not conjectural —
   Totaro (2004) gives the *explicit curvature formula* for any Hessian metric and names the
   octonionic det case as yielding the Riemannian symmetric space `E6/F4` of noncompact type.
   The curvature depends ONLY on the **third derivative tensor** `C_ijk = ∂³(det)/∂x_i∂x_j∂x_k`
   (the cubic-norm coefficients). **This is the engine Phase B/C needs — and it already exists.**

2. **The homogeneity question (Phase A KILL gate) has a sharp literature anchor.** Whether the
   slice carries one fixed metric reduces to: *is the V_0 = h_2(O) slice a totally geodesic
   submanifold of `E6(-26)/F4`, and does the stabilizer of E_11 act transitively on basepoints?*
   The maximal totally geodesic submanifolds of `E6(-26)/F4` are **completely classified**
   (Kollross–Rodríguez-Vázquez 2022, Adv. Math., Table 7). The h_2(O) det=1 slice
   (`SO(9,1)/SO(9)`, dim 9) and its h_2(C_u) sub-slice (`H^3 = SL(2,C)/SU(2) = SO(3,1)/SO(3)`,
   dim 3) **do NOT appear in that list** (the listed rank-1 piece is the *octonionic* hyperbolic
   plane `F4(-20)/Spin(9)`, dim 16 — the idempotent direction, not the spacetime slice). This is
   strong evidence the V_0 slice is **NON-totally-geodesic** (nonzero second fundamental form) →
   Gauss–Codazzi gives it curvature *different from* the ambient → plausibly position-dependent.
   **This points toward "survives," not "homogeneous KILL" — but it MUST be computed, not assumed.**

3. **The exact slice-curvature question appears UNADDRESSED in the literature → this is the novelty.**
   Nobody located has computed the metric/curvature *induced on a Peirce V_0 sub-block* of a
   Jordan-algebra cone, nor asked whether matter content in V_1/V_{1/2} sources that curvature via
   the det cross-terms. See "Open Questions / Novelty" below.

4. **Prior emergent-gravity-from-octonions attempts exist but take a different (rejected) route.**
   Castro (octonionic gravity/p-branes) posits a *membrane action* invariant under E6(-26)
   cubic-form transformations — an action, not intrinsic cone curvature. Singh and
   Dubois-Violette–Todorov use h_2(O)=10D-Minkowski / h_3(O)-as-quantum-geometry but do not
   derive gravitational *curvature* from the cone. None preempts the V_0-slice-curvature claim.

---

## Key Results

| # | Result | Expression / Statement | Conditions | Source | Year | Confidence |
| - | ------ | ---------------------- | ---------- | ------ | ---- | ---------- |
| Q1 | **Explicit curvature of a Hessian metric** | For `g_ij = f_ij`: `R_ijkl = -(1/4) Σ_pq g^pq (f_jlp f_ikq − f_ilp f_jkq)`. Depends ONLY on 3rd derivatives `f_ijk`. With normalization `g_ij = −1/[d(d−1)] f_ij`: `R_ijkl = −1/[4d²(d−1)²] Σ_pq g^pq(f_jlp f_ikq − f_ilp f_jkq)`. | f homogeneous deg `d>1`, Hessian nondegenerate (index cone). | Totaro, *Curvature of a Hessian metric*, Int. J. Math. 15 (2004), the curvature-tensor formula (§2) and its cone-normalized form; arXiv math/0401381. | 2004 | HIGH |
| Q1 | **Cone Hessian `Hess(-log det)` ↔ `{det=1}` symmetric space** | `(R × M, dt² ⊕ g_M)` with `M={det=1}` and `g_M = restriction of −∂²(det)/∂x∂x` is **isometric** to `(U, −∂²(log det)/∂x∂x)`. So the −log det cone metric = warped/product of R and the det=1 hypersurface metric (Lemma 2.4, after Loftin Thm 1). | f=det, homogeneous; U = positive cone. | Totaro 2004, Lemma 2.4; Loftin (centroaffine metric). | 2004 | HIGH |
| Q1 | **h_3(O) det case = `E6(-26)/F4`** | For f = det on octonion-Hermitian 3×3 (n=3), the `{det=1}` hypersurface with the Hessian metric is the **Riemannian symmetric space of noncompact type `E6/F4`** (= `E6(-26)/F4`, dim 26). Parallel cases: `SL(n,R)/SO(n)`, `SL(n,C)/SU(n)`, `SL(n,H)/Sp(n)`. | Cone of positive-definite matrices; reference Vinberg for general homogeneous cones. | Totaro 2004, §2 "Example". | 2004 | HIGH |
| Q1 | **The bulk is a symmetric cone; canonical (characteristic) metric** | Every symmetric cone `Ω` = cone of squares of a Euclidean (formally real) Jordan algebra; canonical `G`-invariant Riemannian metric `g_X = Hess(−log det X)` (= `Hess(−log φ)`, φ the characteristic function ∝ det^{n/r}). Cone is a symmetric space `G/K` with `G=` connected component of the linear automorphism group (here `E6(-26)`), `K=` stabilizer of basepoint (here `F4`). | Symmetric (self-dual homogeneous) cone. | Faraut & Korányi, *Analysis on Symmetric Cones*, OUP 1994 (esp. Ch. I–III, characteristic function & Riemannian structure); Koszul; Vinberg (1963). | 1994 / 1963 | HIGH |
| Q2 | **Sectional curvature of `{f=1}` via Clebsch covariant (R³)** | On R³, deg-d homogeneous f: `K(2-plane tangent to M) = d²(d−1)² S(f) f / [4(d−2)² H(f)²]` and the *surface* `K_M = −d²/4 + d²(d−1)² S(f) f² /[4(d−2)² H(f)²]`, with `H(f)=` Hessian determinant, `S(f)=` Clebsch covariant of the cubic-form 3rd-derivative tensor. | R³, Hessian determinant ≠ 0, d>2. | Totaro 2004, **Theorem 3.1** (extends Wilson Thm 5.1); Clebsch covariant from Dolgachev–Kanev. | 2004 | HIGH |
| Q2 | **Constant negative curvature only for special cubics** | The whole cone metric `−1/[d(d−1)]f_ij` on the rank-1 (R³/Lorentzian-quadratic) and Fermat-type cases has constant curvature `−d²/4`; **higher-rank Jordan cones (incl. h_3(O)) are symmetric but NOT constant-curvature.** | — | Totaro 2004, Cor. 2.3 + Example; Wilson. | 2004 | HIGH |
| Q2 | **Very special real geometry: curvature from cubic coefficients** | A "very special real" manifold from a cubic norm `N(h)=d_{ijk}h^i h^j h^k` has metric `g_{ij} = −½ ∂_i∂_j ln N` (the same Hess(−log N)) and curvature built algebraically from `d_{ijk}`; the *symmetric* cases are classified, with `h_3(O)`'s det giving the rank-3 `E6(-26)/F4` (26-dim, the "magic" `J_3^O` entry). **Geometry only — Lagrangian NOT used.** | Cubic-norm scalar manifold; "symmetric" = isometry group transitive. | de Wit & Van Proeyen, *Special geometry, cubic polynomials and homogeneous quaternionic spaces*, CMP 149 (1992) 307; arXiv hep-th/9112027. Gunaydin–Sierra–Townsend (1983–84) for the `E6(-26)/F4` identification (GEOMETRY only). | 1992 / 1983-84 | HIGH |
| Q3 | **Maximal totally geodesic submanifolds of `E6(-26)/F4` — COMPLETE classification** | Table 7 lists them: `Sp(1,3)/Sp(1)×Sp(3)` (dim 12, reflective, Dynkin idx 1); **`F4(-20)/Spin(9)`** = octonionic hyperbolic plane OH² (dim 16, reflective, idx 1); `SL3(C)/SU3` (dim 8, idx 9); `G2(C)/G2` (dim 14, idx 3). | Riemannian symmetric space EIV = `E6(-26)/F4`, rank 3, dim 26. | Kollross & Rodríguez-Vázquez, *Totally geodesic submanifolds in exceptional symmetric spaces*, Adv. Math. (2022), Table 7; arXiv 2202.10775. | 2022 | HIGH |
| Q3 | **h_2(O) / h_2(C_u) det=1 slices are NOT in that list** | The V_0 = h_2(O) det=1 space `SO(9,1)/SO(9)` (dim 9) and the h_2(C_u)~R^{3,1} sub-slice `H^3=SL(2,C)/SU(2)=SO(3,1)/SO(3)` (dim 3) are absent from the maximal-tot-geod list of `E6(-26)/F4`. ⇒ V_0 slice is (almost certainly) **non-totally-geodesic** → nonzero 2nd fundamental form → Gauss–Codazzi curvature ≠ ambient. | Comparison of Table 7 list against the Peirce-slice candidates. | Inference from Kollross–Rodríguez-Vázquez 2022 Table 7; to be CONFIRMED by direct computation in Phase A. | 2022 | MEDIUM–HIGH (inference) |
| Q5 | **Stabilizer of a primitive idempotent in F4 = `Spin(9)`** | F4 acts transitively on primitive (rank-1, trace-1) idempotents = Cayley plane `OP² = F4/Spin(9)` (dim 16). `Stab_{F4}(E_11) = Spin(9)`. | h_3(O); F4 = Aut. | Baez, *The Octonions*, BAMS 39 (2002), §3.4 / §4.2 (`OP²=F4/Spin(9)`); standard. | 2002 | HIGH |
| Q5 | **`E6(-26)` transitive on `{det=1}` positives; stabilizer = F4** | `E6(-26)` (det-preserving group, = Str_0) acts transitively on the det=1 positive cone slice; point-stabilizer = `F4`. So `{det=1} = E6(-26)/F4`. | — | Baez 2002 §4.4; Faraut–Korányi 1994. | 2002 / 1994 | HIGH |
| Q5 | **Rank > 1 ⇒ sectional curvature NOT constant; flat 2-planes exist** | A noncompact symmetric space of rank `r>1` has sectional curvature `≤0` that **vanishes on certain 2-planes** (the flats of dim r) and is `<0` on others. `E6(-26)/F4` has rank 3. | Standard symmetric-space theory. | Helgason; Eberlein; confirmed in survey notes (Gorodski; Iozzi). | — | HIGH |

---

## Foundational Work

### Totaro, B. (2004) — *The Curvature of a Hessian Metric* (Int. J. Math. 15; arXiv math/0401381)

**Key contribution.** THE load-bearing reference for this milestone. Gives (a) the explicit
Riemann tensor of any Hessian metric `g_ij = ∂²f/∂x_i∂x_j` purely in terms of third derivatives
`f_ijk` (`R_ijkl = −¼ Σ g^pq(f_jlp f_ikq − f_ilp f_jkq)`); (b) Lemma 2.4 reducing
`Hess(−log f)` on the cone to a product `R × {f=1}` with the restricted `Hess(f)`-metric — i.e.
the cone Hessian and the det=1 hypersurface metric are the same geometry up to a flat R factor;
(c) the explicit Example identifying the octonionic-det `{det=1}` hypersurface as the symmetric
space `E6/F4` of noncompact type; (d) Theorem 3.1 expressing the sectional curvature of `{f=1}`
in R³ via the **Clebsch covariant** `S(f)` and Hessian determinant `H(f)` of the cubic.

**Method.** Classical pseudo-Riemannian curvature formula (Schouten / O'Neill) specialized to
Hessian metrics; GL-equivariance via `H(fA)=H(f)det(A)²`, `S(fA)=S(f)det(A)⁴`; warped-product
(O'Neill) relation between cone curvature and hypersurface curvature (Cor. 2.2).

**Limitations / what it does NOT do.** (i) Theorem 3.1's Clebsch-covariant closed form is
**only for R³** (n=3 variables) — directly usable for the 3-dim h_2(C_u) det=1 hyperboloid `H^3`,
but NOT for the full 10-dim V_0 = h_2(O) or 26-dim bulk (there one uses the general 3rd-derivative
formula). (ii) Totaro studies the *ambient* cone/hypersurface curvature; he does **NOT** compute
curvature *induced on a sub-block / Peirce slice*. (iii) No matter-sourcing notion.

**Relevance.** Supplies the exact curvature engine (depends only on `C_ijk` = cubic-norm 3rd
derivatives) for Phases B/C, AND certifies that the bulk is symmetric-but-not-constant-curvature
(so the slice can in principle inherit nontrivial, varying curvature). Phase B should use the
general formula; the H^3 sub-slice can be cross-checked with Theorem 3.1 + Clebsch covariant.

### Faraut, J. & Korányi, A. (1994) — *Analysis on Symmetric Cones* (Oxford Math. Monographs)

**Key contribution.** Canonical text. Symmetric cone `Ω` = cone of squares of a Euclidean
(formally real) Jordan algebra; characteristic function `φ(x) = ∫_Ω e^{−⟨x,y⟩} dy ∝ det(x)^{−n/r}`;
the `G`-invariant Riemannian metric `g_x = D²(−log φ)(x) ∝ Hess(−log det x)`; `Ω = G/K` a
Riemannian symmetric space; geodesics, the quadratic representation `P(x)`, and the
"associative" trace inner product. For h_3(O): `r=3`, `n=27`, `G = E6(-26)`, `K = F4`.

**Method.** Jordan-algebraic; builds analysis (spherical functions, Gindikin gamma) on the cone.

**Limitations.** A treatise on harmonic analysis — it establishes the symmetric-space/Hessian
structure and `G`-invariance but does not tabulate sectional curvature by 2-plane, and (like all
of this literature) does not treat induced metrics on Peirce sub-blocks.

**Relevance.** Authoritative citation for everything the milestone marks "already SOLID":
`g_X = Hess(−log det)`, det=1 = `E6(-26)/F4`, symmetric-cone status. Cite for the convention
`g_X(A,B) = −∂_s∂_t log det(X+sA+tB)|_0`.

### Kollross, A. & Rodríguez-Vázquez, A. (2022) — *Totally geodesic submanifolds in exceptional symmetric spaces* (Adv. Math.; arXiv 2202.10775)

**Key contribution.** Complete classification of **maximal** totally geodesic submanifolds of all
exceptional Riemannian symmetric spaces, **including `E6(-26)/F4` (EIV)** — see Table 7. For EIV
the maximal totally geodesic submanifolds are: `Sp(1,3)/Sp(1)×Sp(3)` (dim 12), the octonionic
hyperbolic plane `F4(-20)/Spin(9)` (dim 16), `SL3(C)/SU3` (dim 8), `G2(C)/G2` (dim 14). Introduces
a "Dynkin index" invariant and notes reflectivity.

**Method.** Lie-algebraic (subalgebra lattices `L(g)`, Dynkin index, reflective submanifolds);
builds on Chen–Nagano, Klein, Berndt–Olmos.

**Limitations.** Classifies *totally geodesic* (zero second fundamental form) submanifolds only.
A Peirce V_0 = h_2(O) sub-block is generically NOT one of these, so the paper's direct content is
the **negative** result: the spacetime slice is not totally geodesic. It does not compute the
second fundamental form / induced curvature of non-geodesic slices.

**Relevance.** This is the decisive reference for Phase A. Because neither `SO(9,1)/SO(9)` (the
h_2(O) det=1 space) nor `SO(3,1)/SO(3)=H^3` (the h_2(C_u) det=1 space) appears as a maximal
totally geodesic submanifold of `E6(-26)/F4`, the V_0 slice is almost certainly **non-geodesic**
→ has a position-dependent second fundamental form → the Gauss equation gives it intrinsic
curvature that differs from the ambient and varies with the basepoint. That is exactly the
"survives" branch the milestone hopes for — **but Phase A must confirm it by direct computation,
since absence-from-the-maximal-list is not a proof of non-geodesic (a non-maximal slice could
still be totally geodesic inside a larger geodesic submanifold; e.g. check whether the V_0 slice
sits inside the dim-16 `F4(-20)/Spin(9)` or dim-12 `Sp(1,3)/…` totally geodesic submanifold).**

### de Wit, B. & Van Proeyen, A. (1992) — *Special geometry, cubic polynomials and homogeneous quaternionic spaces* (CMP 149; arXiv hep-th/9112027) — GEOMETRY ONLY

**Key contribution.** Classifies cubic norms `N(h) = d_{ijk}h^i h^j h^k` whose invariance group
acts transitively on the real manifold (the "very special real" / homogeneous cases). The
Riemannian geometry of such a manifold is the Hessian geometry of `−log N`; curvature is built
from `d_{ijk}` and its contractions. The symmetric entries include the four "magic"
Jordan-algebra families `J_3^{R,C,H,O}`, with `J_3^O` (det of 3×3 octonionic Hermitian) giving
the rank-3, 26-dim space identified with `E6(-26)/F4`.

**Method.** Algebraic classification of cubic forms + r-map/c-map relations.

**Limitations / EXPLICIT EXCLUSION.** This paper sits inside the N=2 supergravity literature. We
take ONLY its differential-geometric statements (which cubic norms are homogeneous/symmetric,
the curvature-from-`d_{ijk}` structure, the `E6(-26)/F4` identification). We do **NOT** import the
supergravity Lagrangian, the prepotential-as-action, or any SUSY closure — that is the dead
det/GST/Weinberg route. Used here purely as independent corroboration that the cubic-norm
Hessian geometry of h_3(O) is `E6(-26)/F4` and that its curvature is fixed by `d_{ijk}=det`.

**Relevance.** Cross-checks Totaro's identification from a different (algebraic-classification)
direction; supplies the "curvature is algebraic in the cubic coefficients" framing for Phase B.

### Shima, H. (2007) — *The Geometry of Hessian Structures* (World Scientific); Shima–Yagi (1997)

**Key contribution.** Systematic theory of Hessian manifolds: Hessian metric `g = ∇dτ`, dual
flat connections, Hessian sectional curvature, Koszul forms, homogeneous Hessian manifolds. The
characteristic-function metric on a regular convex cone (incl. symmetric cones) is the motivating
example.

**Limitations.** General theory; the curvature *of a submanifold with induced Hessian metric*
(centroaffine/Gauss–Codazzi for slices) is not a focus.

**Relevance.** Vocabulary and general identities (dual connections, Hessian sectional curvature,
Codazzi/difference tensor `C_ijk`) for METHODS/PITFALLS; secondary to Totaro for the explicit
formula. Good source for the warning that "a canonical Hessian metric on a convex domain can have
positive curvature" (Duistermaat) — relevant if the slice curvature comes out positive somewhere.

---

## Prior Emergent-Gravity-from-Jordan/Octonion Attempts (Q4) — and how the new route differs

| Author(s) | Vehicle | What they got | Relation to THIS milestone |
| --------- | ------- | ------------- | -------------------------- |
| Castro (Perelman), C. — *Exceptional Jordan Strings/Membranes and Octonionic Gravity/p-branes* (IJGMMP, ~2008/2012) and *Exceptional Jordan matrix models, octonionic strings/branes* (J. Geom. Phys. 2021) | A **membrane/p-brane action** in an octonionic-valued spacetime background; large-N exceptional Jordan matrix models. | The membrane action is invariant not under worldvolume diffeos but under rigid `E6(-26)` transformations preserving the **cubic (volume) form** det. An octonionic metric `G_μν` packaging `g_μν` + Maxwell + SU(2). | **Different route — explicitly the kind we avoid.** Gravity enters via a posited action / octonionic metric put in by hand; he does NOT derive Einstein curvature *intrinsically* from the cone Hessian. Shares the cubic-form / `E6(-26)` ingredient, so cite as "prior attempt, action-based, distinct." NOT load-bearing. |
| Singh, T.P. and collaborators — octonionic / exceptional-Jordan unification (e.g. arXiv 2304.01213; EPJ Plus 2022) | "Trace dynamics" / pre-quantum aikyon program; `h_2(O)`-as-10D-Minkowski with det = Minkowski metric; gravity as emergent low-energy phenomenon. | Identifies spacetime sector with octonionic matrices; aims at SM flavor + emergent classical spacetime; computes coupling/mass ratios. | **Adjacent, not preempting.** Uses the det=Minkowski identification (which we also use for the background `eta` of the h_2(C_u) slice) but does NOT compute *curvature induced on a Peirce slice* nor source it from V_1/V_{1/2}. No conflict; cite for the det↔Minkowski dictionary. |
| Dubois-Violette, M. & Todorov, I. (2016–18) — *Exceptional quantum geometry and particle physics I, II* (arXiv 1604.01247 and sequel) | `h_3(O)` as the observable algebra of an "almost classical quantum spacetime"; SM gauge group as the subgroup preserving the C⊕(2×2 octonionic) splitting. | `h_2(O) ≅ 10D Minkowski`, pairs of octonions = MW spinors; SM gauge group `(SU(3)×SU(2)×U(1))/Z6`. | **Establishes the algebraic dictionary (Peirce structure, h_2(O)=Minkowski), NOT gravitational curvature.** Strongly supports the milestone's "already SOLID" h_2(O) facts; does not address slice curvature. Cite for the Peirce-decomposition / Minkowski-from-det facts. |
| Oliveira & Marques (cited via Castro); "Octonionic gravity" tradition | Octonionic generalization of GR's metric. | A metric-level octonionic gravity. | Older, metric-postulated; distinct from intrinsic cone curvature. Mention only as lineage. |

**Net (Q4): No prior work derives gravitational curvature from the *intrinsic Hessian geometry of
the h_3(O) cone restricted to the V_0 spacetime slice*.** Existing octonionic-gravity programs
either posit an action (Castro), or use h_2(O)=Minkowski as flat background without slice curvature
(Singh, Dubois-Violette–Todorov). The specific mechanism — matter in V_1/V_{1/2} sourcing V_0-slice
curvature through the det cross-terms — is not in the located literature.

---

## Known Limiting Cases (validation anchors for Phases A–C)

| Limit | Known Result | Source | Use in validation |
| ----- | ------------ | ------ | ------------------ |
| M=0, basepoint = center I/3, h_2(C_u) sub-slice | Background must be **exact Minkowski** `eta_μν` (`−det = t² − |a|² − z²` on 2×2 octonionic Hermitian; the complex sub-slice gives R^{3,1}). | Oregon State *Geometry of the Octonions* (`−det = |a|²+z²−t²`); Dubois-Violette–Todorov; existing GPD `52-kkt-spacetime`. | A0 signature bridge MUST reduce to `eta_μν` here. If not, the bridge construction is wrong. |
| det=1 hyperboloid of h_2(C_u) | `H^3 = SL(2,C)/SU(2) = SO(3,1)/SO(3)`, **constant negative curvature** `−d²/4` with d=2 ⇒ `K=−1` (rank-1). Computable via Totaro Thm 3.1 + Clebsch covariant. | Totaro 2004 Cor. 2.3 (quadratic-form / rank-1 case); existing GPD `52-*`. | Cross-check the H^3 sub-slice curvature; expect constant `<0` in the M=0 limit. |
| det=1 hyperboloid of h_2(O) | `SO(9,1)/SO(9)`, rank-1, constant negative curvature (Lorentzian-quadratic case, d=2). | Totaro 2004 Example (Lorentzian quadratic → hyperbolic space). | The full V_0=h_2(O) det=1 background (no matter, no embedding) is `H^9`-type, constant `<0`. Deviation from this when embedded in h_3(O) is the inherited (extrinsic) effect. |
| Full bulk `E6(-26)/F4`, M arbitrary | Rank-3 symmetric space: `K ≤ 0`, **vanishes on flat 2-planes**, NOT constant. | Helgason; Totaro 2004 (symmetric-but-not-constant). | Phase B: ambient curvature is fixed/homogeneous as a symmetric space; any *position dependence on the slice* must come from the slice's embedding (2nd fundamental form), not from the ambient symmetric-space curvature varying. |
| Cross-terms switched off (det → block-diagonal `det(V_1)·det(V_0)`) | Curvature should lose its M-sourced part (the V_0↔V_1/V_{1/2} coupling). | (Conjectural — Phase B test.) | Phase B(b) consistency check; if curvature persists with cross-terms off, the mechanism is misattributed. |

---

## Open Questions / NOVELTY (what the literature does NOT settle)

1. **[NOVELTY — central] Does restricting `g_X = Hess(−log det)` (or `Hess(det)` on `{det=1}`) to
   the Peirce V_0 = h_2(O) directions yield a *position-dependent* induced metric `h_μν(x)` once
   E_11 is fixed?** No located reference computes the induced metric/curvature on a Peirce
   sub-block of a Jordan-algebra cone. Totaro/Faraut–Korányi treat the ambient cone; Kollross–
   Rodríguez-Vázquez treat only totally-geodesic (curvature-preserving) submanifolds. **This is the
   Phase A KILL gate and the milestone's primary novelty.** Status: **UNADDRESSED.**

2. **[NOVELTY] Is the V_0 slice totally geodesic or not?** Strong indirect evidence (it is absent
   from the maximal-tot-geod list of `E6(-26)/F4`, Kollross–Rodríguez-Vázquez Table 7) says
   **non-geodesic** → nonzero second fundamental form → Gauss–Codazzi-inherited curvature ≠ ambient.
   But this is an *inference*, not a theorem (a non-maximal slice could be geodesic inside a larger
   geodesic submanifold — must rule out V_0 ⊂ {`F4(-20)/Spin(9)`, `Sp(1,3)/…`}). **Must be settled
   by direct computation of the 2nd fundamental form in Phase A.** Status: **partially constrained.**

3. **[NOVELTY] Is the curvature of `h_μν(x)` sourced specifically by the det cross-terms coupling
   V_0 to V_1/V_{1/2}?** The general Hessian curvature formula (Totaro) shows curvature = quadratic
   in `C_ijk = ∂³det`. Whether the *V_0-block* curvature is controlled by the *mixed* components
   `C_{(V_0)(V_1)(V_{1/2})}` (vs. the pure `C_{(V_0)(V_0)(V_0)}` block) is a structural question
   about the cubic norm's Peirce-graded components — **not computed anywhere located.** Status:
   **UNADDRESSED.**

4. **[NOVELTY — strong form] Does `G_μν[h(x)] ∝ T_μν` for any natural `T_μν` built from V_1/V_{1/2}?**
   Einstein structure of an induced Peirce-slice metric is entirely unstudied. The honest prior
   expectation (from rank-3 symmetric-space + Gauss–Codazzi heuristics) is "curved, possibly not
   Einstein." Status: **UNADDRESSED / open.**

5. **Homogeneity via the stabilizer (Phase A(b)).** `Stab_{E6(-26)}(E_11)` and the dimension of the
   basepoint family modulo it: standard inputs exist (`F4 = Stab` of the det=1 basepoint;
   `Spin(9) = Stab_{F4}` of the idempotent; idempotent space `OP² = F4/Spin(9)`, dim 16) but the
   precise non-compact stabilizer of a *primitive idempotent in E6(-26)* (expected: a parabolic-type
   subgroup with Levi containing `Spin(9,1)`, since `E6(-26) ⊃ Spin(9,1)` and the P1 maximal
   parabolic of complex/compact E6 has semisimple part `Spin(10)`) and whether it acts transitively
   on the *(basepoint, slice)* pairs is **not cleanly tabulated** in the located sources. Status:
   **needs phase-specific lookup / direct computation.**

---

## Notation & Convention Reconciliation Across the Literature

| Quantity | Symbols in literature | Variants / pitfalls | This project's choice | Reason |
| -------- | --------------------- | ------------------- | --------------------- | ------ |
| Cubic norm of h_3(O) | `N(X)`, `det(X)`, `n(x)` | "Freudenthal det" with **cross-term** `+2 Re(triple)`; octonion non-associativity makes `2Re(x0(x1 x2))` ≠ `2Re(x2* x0* x1)` (a real prior bug). | `det(X)` = Freudenthal cubic WITH the *verified* cross-term association (`h3o_tower.py`). | Springer: unique F4-invariant cubic; cross-term order is load-bearing. |
| Cone metric | `g_X`, characteristic/canonical metric, `Hess(−log det)`, `D²(−log φ)` | Normalization factors `−1` vs `−1/[d(d−1)]` (Totaro/Wilson) vs `−n/r` (Faraut–Korányi φ ∝ det^{n/r}). | `g_X(A,B) = −∂_s∂_t log det(X+sA+tB)|_0` (prompt convention). | Matches Faraut–Korányi up to normalization; fix once, track factors. |
| Curvature constant of rank-1 hyperbolic slices | `−d²/4` (Totaro), `−1` (with d=2), or `−4` (some hyperbolic normalizations) | The `−d²/4` is for the *cone* normalization `−1/[d(d−1)]f`; renormalizing rescales. | State normalization explicitly with every curvature number. | Avoid factor-of-4 errors when comparing H^3 curvature to GR. |
| Hessian 3rd-derivative tensor | `C_ijk`, `f_ijk`, `d_{ijk}`, "difference/Codazzi tensor", "cubic form" | Factor `½` (`Γ_ijk = f_ijk/2`); sign conventions in `R_ijkl`. | `C_ijk = ∂³det/∂x_i∂x_j∂x_k`; use Totaro's `R_ijkl = −¼ g^pq(f_jlp f_ikq − f_ilp f_jkq)`. | Single explicit formula prevents sign drift. |
| Bulk symmetric space | `E6(-26)/F4`, `EIV`, `E6/F4` (noncompact), `J_3^O` very-special-real | Compact-dual confusion (`E6/F4` of "outer type" is the *compact* dual); Cartan label EIV. | `E6(-26)/F4`, noncompact type, dim 26, rank 3. | Compact vs noncompact dual have opposite-sign curvature; the cone gives the NONcompact one. |
| V_0 spacetime sub-slices | `h_2(O)`, `h_2(C_u)`; det=1 spaces `SO(9,1)/SO(9)`, `H^3=SL(2,C)/SU(2)` | `SL(2,C)/SU(2)` ≅ `SO(3,1)/SO(3)` ≅ Riemannian `H^3` vs the Lorentzian `R^{3,1}` cone itself. | Distinguish the *Lorentzian slice* `R^{3,1}` (signature −+++) from the *Riemannian det=1 hyperboloid* `H^3`. | A0 signature bridge depends critically on which object carries the Lorentzian signature. |

---

## Sources

**Load-bearing (cite directly):**
- **Totaro, B., "The Curvature of a Hessian Metric," Int. J. Math. 15 (2004) 369–391; arXiv:math/0401381.** — Explicit Hessian curvature formula (3rd-derivatives only); Lemma 2.4 (cone ↔ det=1 hypersurface); Example (octonionic det = `E6/F4` noncompact); Theorem 3.1 (Clebsch-covariant sectional curvature on R³). PRIMARY engine for Phases B/C. [Read directly via local pdftotext — HIGH confidence on quoted formulas.]
- **Faraut, J. & Korányi, A., *Analysis on Symmetric Cones*, Oxford Math. Monographs, OUP 1994.** — Symmetric-cone = Jordan-cone-of-squares; characteristic function; canonical `G`-invariant metric `Hess(−log det)`; `Ω=G/K` symmetric space; `h_3(O)` ⇒ `E6(-26)/F4`. Authoritative for all "already SOLID" cone facts.
- **Kollross, A. & Rodríguez-Vázquez, A., "Totally geodesic submanifolds in exceptional symmetric spaces," Adv. Math. (2022); arXiv:2202.10775.** — Table 7: complete maximal-tot-geod classification for `E6(-26)/F4`. DECISIVE for Phase A homogeneity / non-geodesic-slice argument. [Read directly via local pdftotext — Table 7 E6(-26)/F4 row quoted verbatim, HIGH confidence.]
- **de Wit, B. & Van Proeyen, A., "Special geometry, cubic polynomials and homogeneous quaternionic spaces," Commun. Math. Phys. 149 (1992) 307–333; arXiv:hep-th/9112027.** — GEOMETRY ONLY: homogeneous cubic norms, curvature-from-`d_{ijk}`, `J_3^O` ⇒ `E6(-26)/F4`. (Lagrangian/SUSY content explicitly NOT used.)
- **Baez, J., "The Octonions," Bull. AMS 39 (2002) 145–205; arXiv:math/0105155.** — `F4 = Aut(h_3(O))`, `OP² = F4/Spin(9)`, `Stab_{F4}(idempotent)=Spin(9)`, `E6(-26)` det-preserving, `{det=1}=E6(-26)/F4`. Standard reference for Q5 group facts.

**Supporting / corroborating:**
- **Shima, H., *The Geometry of Hessian Structures*, World Scientific 2007; Shima–Yagi, "Geometry of Hessian manifolds," Diff. Geom. Appl. 7 (1997) 277.** — General Hessian-manifold theory; dual connections; Hessian sectional curvature; positive-curvature warning (Duistermaat).
- **Vinberg, E.B., "The theory of convex homogeneous cones," Trans. Moscow Math. Soc. 12 (1963) 340.** — Canonical metric on a homogeneous convex cone (cited by Totaro for the symmetric-cone Example).
- **Loftin, J. — centroaffine metric of `{f=1}` (cited in Totaro Lemma 2.4).** — Affine-differential-geometry framing of the hypersurface metric; relevant if Phase A uses centroaffine/Gauss–Codazzi machinery for the slice.
- **Dubois-Violette, M. & Todorov, I., "Exceptional quantum geometry and particle physics," Nucl. Phys. B 938 (2019); arXiv:1604.01247 (+ sequel arXiv:1806.09450).** — `h_2(O)=10D Minkowski`, Peirce decomposition, SM gauge group; det↔Minkowski dictionary (Q4 adjacent, not preempting).
- **Singh, T.P. et al., e.g. arXiv:2304.01213; EPJ Plus 137 (2022).** — Octonionic emergent-gravity program; det=Minkowski; does not compute slice curvature (Q4 adjacent).
- **Gunaydin, M., Sierra, G., Townsend, P.K. (1983–84).** — `E6(-26)/F4` as the `J_3^O` scalar manifold (GEOMETRY of the identification ONLY; their N=2 supergravity Lagrangian is the DEAD route and is NOT used).
- **Kollross & Rodríguez-Vázquez companion / Berndt–Olmos (submanifold geometry of symmetric spaces of noncompact type, arXiv:1901.04552); Gorodski (Riemannian symmetric spaces survey).** — Background on totally geodesic vs non-geodesic submanifolds, reflective submanifolds, flats and rank.

**Explicitly NOT load-bearing (dead routes, per prompt):**
- `paper6-continuum-limit-prompt.md` (lattice/Fisher) — abandoned, not cited.
- The det/GST/Weinberg N=2 **supergravity Lagrangian** (GPD derivations `47–50`, `53`) — circular, not cited as a derivation of `−R/2`.
- Castro's membrane *action* — cited only as a *distinct prior attempt* (action-based), not as a method to adopt.
- Jacobson 1995 (Einstein eqs. as equation of state) — thermodynamic/ensemble route explicitly rejected; not used.

---

### Status note for orchestrator

Per the spawn contract this run produced ONLY `PRIOR-WORK.md` (a focused literature survey for the
v17.0 bulk-geometry milestone), overwriting the prior v16.0 PRIOR-WORK.md. The other research files
(SUMMARY/METHODS/COMPUTATIONAL/PITFALLS) were NOT regenerated and still reflect v16.0 unless a
separate run refreshes them.

**Verification caveats:** Several arXiv PDFs returned as binary to WebFetch; the two load-bearing
ones (Totaro math/0401381; Kollross–Rodríguez-Vázquez 2202.10775) were converted locally via
`pdftotext` and read directly — quoted formulas/tables (Totaro curvature formula, Lemma 2.4,
Thm 3.1, Example; Kollross–Rodríguez-Vázquez Table 7 E6(-26)/F4 row) are from the actual paper
text, HIGH confidence. Faraut–Korányi, Baez, de Wit–Van Proeyen statements are from canonical
knowledge + search corroboration (HIGH for the cited facts). The "V_0 slice not totally geodesic"
claim is an **inference** from Table 7 (MEDIUM–HIGH) and is flagged for direct computation in Phase A.
ResearchGate copy of Castro's membrane paper was paywalled (HTTP 403); its framing is corroborated
via secondary search snippets (MEDIUM confidence on exact venue/year, HIGH on the action-based
nature).
