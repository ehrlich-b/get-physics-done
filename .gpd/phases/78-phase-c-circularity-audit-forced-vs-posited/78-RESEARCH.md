# Phase 78: Phase C — Circularity Audit (forced vs posited) — Research

**Researched:** 2026-06-02
**Domain:** Mathematical physics — invariant theory of the MacDowell–Mansouri ε-contraction over the residual structure group; exact-over-Q symbolic enumeration of the trace-form/cubic-norm-invariant quadratic-in-curvature 4-form space on h_3(O); the GST/Singh/Castro "imported-action" contrast class
**Confidence:** HIGH on the MM/Wise formulas, the invariant-theory facts (the bare SO(3,1)-invariant quadratic-curvature 4-form space is 2-dim: Euler + Pontryagin), the decisive-criterion mapping, the in-repo SSOT (det_3, Tr(X∘Y)), the contrast class, and the fp-imported-action discipline; MEDIUM only on the genuinely-open OUTCOME (whether the trace-form/cubic-norm uniquely forces ε with a cubic-norm-fixed normalization) — that is exactly what this phase MEASURES, and the contract + Phase 77 NEGATIVE make `fp-imported-action` the HIGH / most-likely real verdict.

## Summary

Phase 78 is the FINAL phase of v18.0 and the decisive non-circularity audit. Phase 77 (Phase B) established at true strength that the assembled (A)dS Cartan connection `A=ω⊕e` has a curvature `F=dA+A∧A` whose Lorentz block IS the genuine 4d Riemann tensor `R[ω]` of `g=e·e` (6/6-component independent Levi-Civita cross-check exact over Q, torsion=0), with a flat `M=0` vacuum (`Λ=0` MEASURED), but `G[g]` is **NOT** Einstein-form `κT+Λg` for any single global `(κ,Λ)` against an AST-guarded order-matched independent `T[M]`. So the Einstein term, **if recoverable at all, is recoverable only via a posited action**. Phase C audits whether the MacDowell–Mansouri ε-contraction — the `Spin(9,1)→SO(3,1)` symmetry breaking plus the ε-tensor that turns the curvature term `F∧F` into Einstein–Hilbert + Λ — is **FORCED** by the intrinsic h_3(O) trace form `⟨X,Y⟩=Tr(X∘Y)` and cubic norm `det_3`, or is an **external MM choice imported by hand** (`fp-imported-action` = the GST sin in new clothes).

The decisive question reduces to a single decidable integer plus an identity, both computable **exact over Q**: the dimension of the space of **trace-form-invariant quadratic-in-F contractions onto a Lagrangian 4-form scalar density** — where "trace-form-invariant" means the admissible invariant tensors used to build the contraction are restricted to those constructed ONLY from `Tr(X∘Y)`, `det_3`, and the structures forced by `(E_11,u)`, NOT from a hand-posited ε or a hand-posited action. **STRONG WIN** iff that space is exactly **1-dimensional AND its generator equals the ε-contraction with a cubic-norm-fixed normalization**; otherwise **`fp-imported-action`** (the space is >1-dim so ε is one choice among several requiring an external pick, OR ε / its normalization is not expressible via the intrinsic trace-form/cubic-norm and must be imported).

Two literature facts pre-load the likely answer and MUST anchor the plan. (1) **The bare SO(3,1)-invariant quadratic-in-curvature 4-form space in 4d is already 2-dimensional** — spanned by the Euler/Gauss-Bonnet form (the ε-contraction `ε_{abcd}R^{ab}∧R^{cd}`) and the Pontryagin form (`R^{ab}∧R_{ab}`). So among *quadratic-in-curvature* invariants the ε-contraction is **not** unique; forced-ness can only come from a *further* restriction that the intrinsic trace-form/cubic-norm structure singles out ε and fixes its normalization. (2) **At `Λ=0` (the Phase-77-MEASURED vacuum) the MM action `∫ε R∧R` is purely the Gauss–Bonnet/Euler topological term — it yields NO equations of motion and does NOT recover GR.** The Einstein–Hilbert term `ε_{abcd}R^{ab}∧e^c∧e^d` appears only from the cosmological/transvection `e∧e` block of the *full* SO(4,1)/SO(3,2) curvature `F^{ab}=R^{ab}-(1/ℓ²)e^a∧e^b`, governed by `1/ℓ²=Λ/3`. This is a second, independent reason the route lands on `fp-imported-action` at true strength: not only is the ε-contraction one of several invariants, but at the measured `Λ=0` even the posited ε-action gives a topological term, not Einstein gravity.

**Primary recommendation:** Compute, **exact over Q via `sympy.Matrix` rank/nullspace (NEVER numpy, NEVER float)**, the dimension of the space of `SO(3,1)`-invariant (equivalently `(E_11,u)`-residual-structure-group-invariant) quadratic-in-`F` 4-form contractions, then the strictly smaller subspace of those **reachable from `Tr(X∘Y)` and `det_3` alone** (the trace-form-invariant subspace), and test whether that subspace is 1-dim and equals the ε-contraction with the `det_3`-fixed normalization. Frame the result against the explicit prediction: the bare quadratic invariant space is 2-dim (Euler + Pontryagin), so the trace-form restriction must collapse it to exactly `{ε}` with a fixed normalization for a STRONG WIN — and report `fp-imported-action` at true strength if it does not, citing Singh / Castro / GST as the contrast class (all three POSIT an action). **Do NOT structure the phase to "confirm Einstein"; do NOT cite the MM action as the source of the Einstein term.**

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| --- | --- | --- | --- | --- |
| **`code/ring_lemma_verification.py`** (det SSOT: `det_3`, `Tr`, `Tr2`, `c`, `jordan`, `polarize_d`) | prior artifact / SSOT | THE source of the intrinsic invariant tensors. `det_3` = the UNIQUE F_4-invariant cubic norm (Cayley–Hamilton + annihilated by all 324 inner derivations); `c(X,Y)=Tr(X∘Y)` = the F_4-invariant trace form. The forced-vs-posited question is *whether ε is reachable from these two*. | USE verbatim; `det_3` and `Tr(X∘Y)` are the ONLY admissible invariant-tensor sources for the "trace-form-invariant" count | every plan, every driver header, verification |
| **`code/cartan_phaseB_curvature.py`** (`assemble_A`, `curvature_F`, `split_blocks`, `riemann_from_omega`, `riemann_lower_from_F`, `tetrad_at_point`) | prior artifact (Phase 77) | Produces the curvature `F` (5×5 iso(3,1)), the Lorentz block `R[ω]^{ab}_{μν}`, the mixed `e∧e` structure, and the tetrad `e`. **Phase C contracts these — it does NOT rebuild F.** | REUSE; the contraction acts on `F`'s Lorentz block (index range a,b=0..3 frame; μ,ν slice coords [1,2,3,10]) | plan, the decisive contraction-space computation |
| **`code/cartan_phaseB_einstein.py`** (`ast_guard_T`, `_forbidden_ids_used`, `source_guard`) | prior artifact (Phase 77) | The AST-guard + source-guard discipline (no `octonion_algebra`, no `numpy.linalg` on the decisive path; no `Ric/R/G` symbol leaks). Phase C needs the analogous **input ban guard**: no `∫ε F∧F`, no `−1/2`, no `16πG`, no posited action enters the FORCED determination. | REPLICATE the guard pattern for the Phase-C input ban (assert the ε-contraction is DERIVED from `det_3`/`Tr`, not imported) | the decisive plan, verification |
| **Wise, gr-qc/0611154** (verbatim formulas below; executor has NO web) | benchmark reference (THE reference) | `A=ω+(1/ℓ)e`; `F=(R−(Λ/3)e∧e)+d_ω e`; `S_MM=(−3/2GΛ)∫tr(F̂∧⋆F̂) = ∫ε_{abcd}F^{ab}∧F^{cd}` up to normalization; the ε-contraction breaks `SO(4,1)→SO(3,1)` **BY HAND** (Wise: "we have broken symmetry in the Lagrangian by hand") — the precise circularity locus. | CITE for what `F`'s blocks mean and what the ε-contraction IS; **NEVER cite the action as the source of the Einstein term** | the decisive plan, the verdict, the .tex |
| **MacDowell & Mansouri, PRL 38 (1977) 739** | benchmark reference | The original broken dS/Lorentz gauge mechanism; the `∫ε F∧F` action. | CITE as the source of the construction being audited | plan, .tex |
| **GST (Gunaydin–Sierra–Townsend 1983–84)** | contrast class (AVOID the Lagrangian) | Magic N=2 MESGT on `E_{6(-26)}/F_4`; the `−R/2` Einstein term is the assumed N=2 multiplet's own output (the C_IJK tensor that defines special-real geometry also fixes the gravitational term). THE in-program `fp-imported-action` precedent (the dead `47-*`..`50-*`,`53-*` route). | CITE for the geometry/contrast ONLY; **do NOT adopt their Lagrangian** (that posited Lagrangian is exactly the fp being audited) | the contrast-class framing, the verdict |
| **`code/orbit_dimension_gate.py`** (`exact_qq_rank`, `span_rank_over_QQ`, `infinitesimal_action`) | prior artifact | Exact-over-Q rank / nullspace / infinitesimal-action machinery — the natural tool for the invariant-tensor nullspace count (the dimension of the invariant contraction space). | REUSE `exact_qq_rank`/`span_rank_over_QQ` for the decisive dimension count | the decisive computation, verification |
| **Phase 77 SUMMARY / VERDICT (NEGATIVE / fp-imported-action partial)** | prior artifact (handoff) | Establishes that `G[g]` is NOT Einstein-form intrinsically ⇒ Einstein structure, if any, must come from a posited action ⇒ THIS phase is the decisive remaining question. Also: `Λ=0` MEASURED (so the ε-action is topological-only at the vacuum). | USE as the premise; the `Λ=0` measurement is load-bearing for the "ε∧R∧R is Gauss-Bonnet-only" argument | plan premise, verdict synthesis |

**Missing or weak anchors:** None blocking. NOTE two soft caveats: (i) the Wise PDF text-layer is not machine-extractable this session (it was read from a locally-saved PDF in Phase 77); the verbatim formulas below are carried from 77-RESEARCH.md + cross-confirmed by web search and are HIGH-confidence. (ii) `peirce_coupling.py` named in the original prompt does NOT exist (corrected in project SUMMARY.md); the Peirce-under-E_11 machinery is in `bulk_geometry_verification.py` (`peirce_indices_under_E11`) and `embedding_under_E_verification.py` — reuse those if a Peirce decomposition is needed.

## Conventions

| Choice | Convention | Source |
| --- | --- | --- |
| Metric signature (slice) | **mostly-minus (+,−,−,−)** timelike-positive Lorentzian (1,3); η=diag(+1,−1,−1,−1) | CONVENTIONS §1, §11; Phase 77 |
| Det / cubic norm SSOT | `ring_lemma_verification.py det_3`, cross-term `2Re((x2 x1)x3)` (x2 BEFORE x1; Phase-64.1 fix); the UNIQUE F_4-invariant cubic norm (CH + 324/324 inner-derivation annihilation). `octonion_algebra.py` BANNED. | CONVENTIONS §0; `det_3` docstring |
| Trace form | `c(X,Y)=Tr(X∘Y)=Tr(jordan(X,Y))`, F_4-invariant (NOT E_6-invariant); the Jordan `1/2` is load-bearing | `ring_lemma_verification.py` `c`, `jordan` |
| Exactness | EXACT over Q on every decisive verdict (the dimension/rank/identity); `sympy.Matrix.rank`/`nullspace`/`eigenvals` over QQ, **NEVER numpy.linalg, NEVER float** | CONVENTIONS §2; `fp-float-decisive` |
| Curvature object | gravity = Lorentz block `R[ω]` of `F=dA+A∧A`; `A=ω+(1/ℓ)e`; `F=(R−(Λ/3)e∧e)+d_ω e` (Wise) | CONVENTIONS §11; Phase 77 |
| Cosmological constant | `Λ=0` at `M=0` (flat KKT η, DERIVED & MEASURED in Phase 77). `Λ<0`/`R×H³` FALSIFIED — do NOT reintroduce | CONVENTIONS §6; Phase 77 |
| Index layout | slice coords (g base) = engine idx **[1,2,3,10]**=(β,γ,p,q); V_{1/2} survivors = engine idx **[11,18,19,26]**=C_u²; frame a,b=0..3 | Phase 77 LOCKED LIVE |

**CRITICAL: All equations below use these conventions. The decisive verdict (the dimension of the trace-form-invariant contraction space, and the ε-identity) is convention-independent as an integer/identity, but the normalization that the cubic norm must fix is read in these conventions — the `−Λ/3` coefficient sign is pinned to the K=−1/2 H³ benchmark, and at the MEASURED `Λ=0` the cosmological/EH terms degenerate (the Poincaré contraction `iso(3,1)` is the right model algebra, not `so(4,1)`).**

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Mathematical Framework

### Key Equations and Starting Points (VERBATIM — executor has NO web access)

**(1) Wise MM/Cartan connection, curvature, and the ε-contraction action** (gr-qc/0611154, carried from 77-RESEARCH.md + web-cross-confirmed):

```
  A = ω + (1/ℓ) e            [ℓ a constant with units of length; ℓ² = 3/Λ]

  F = dA + A∧A = ( R − (Λ/3) e ∧ e ) + d_ω e
        \_____________/       \_____/
         so(3,1) Lorentz       R^{3,1} translation
         block = F̂            block (TORSION)

  where  R^{ab} = dω^{ab} + ω^a_c ∧ ω^cb     [the Lorentz curvature = Riemann]

  THE MM ACTION (the object whose forced-vs-posited status is the verdict):

     S_MM  =  (−3 / 2 G Λ) ∫ tr( F̂ ∧ ⋆F̂ )
           ∝  ∫ ε_{abcd}  F^{ab} ∧ F^{cd}        [the ε-contraction onto the Lorentz block]

  with F̂ = the projection of F into the so(3,1) Lorentz block (the SO(4,1)→SO(3,1)
  symmetry breaking — done "by hand", Wise's words), and ⋆ = the internal Hodge star
  built from ε_{abcd} (the SO(3,1) 4d Levi-Civita ε on the frame indices a,b,c,d=0..3).
  Gauge group: SO(4,1) for Λ>0 (dS), SO(3,2) for Λ<0 (AdS), ISO(3,1) for Λ=0 (Poincaré).
```

**(2) The decomposition of the ε-contraction into EH + Λ + Gauss–Bonnet** (standard MM expansion; substitute `F^{ab}=R^{ab}−(Λ/3)e^a∧e^b` into `ε_{abcd}F^{ab}∧F^{cd}` and expand the square):

```
  ε_{abcd} F^{ab} ∧ F^{cd}
    = ε_{abcd} R^{ab} ∧ R^{cd}                         [GAUSS–BONNET / EULER — topological]
      − (2Λ/3) ε_{abcd} R^{ab} ∧ e^c ∧ e^d             [EINSTEIN–HILBERT]
      + (Λ²/9)  ε_{abcd} e^a ∧ e^b ∧ e^c ∧ e^d         [COSMOLOGICAL CONSTANT]

  ⇒  the EH term carries coefficient ∝ Λ, the Λ-term ∝ Λ², the GB term Λ-independent.
```

**Two load-bearing consequences (HIGH confidence, web-cross-confirmed):**
- **The EH (Einstein) term `ε_{abcd}R^{ab}∧e^c∧e^d` is LINEAR in the Riemann curvature `R[ω]` and requires the `e∧e` (transvection/cosmological) cross-term — it does NOT come from the quadratic-in-R piece.** This is the [[feedback_test_right_object_not_tautology]] lesson made precise: the Einstein object is the **linear-in-R** `ε R∧e∧e`, NOT a quadratic-in-F Maxwell/Pontryagin stress.
- **At `Λ=0` (the Phase-77-MEASURED vacuum), the EH and Λ terms VANISH and `S_MM → ε_{abcd}R^{ab}∧R^{cd}` is the pure Gauss–Bonnet/Euler topological term — no equations of motion, no GR.** (Confirmed by web search: "When the cosmological constant is zero, the MacDowell-Mansouri action reduces to the Gauss-Bonnet term … a purely topological term that yields no equations of motion and does not recover general relativity.")

**(3) The intrinsic invariant-tensor sources** (from `ring_lemma_verification.py`, verbatim):

```
  TRACE FORM (F_4-invariant, bidegree (1,1)):
     c(X,Y) = Tr(X∘Y) = Tr(jordan(X,Y)),   jordan(A,B) = (1/2)(AB+BA)
     Tr(X) = α + β + γ        (linear trace, bidegree (1,0))

  CUBIC NORM (the UNIQUE F_4-invariant cubic form, bidegree (3,0)):
     N(X) = det_3(X) = α β γ − α|x1|² − β|x2|² − γ|x3|² + 2 Re((x2 x1) x3)
     — uniquely fixed by Cayley–Hamilton X^∘3 − Tr(X) X^∘2 + S(X) X − N(X) I = 0,
       equivalently annihilated by ALL 324 inner derivations [L_a,L_b] (Phase 64.1/65).
     POLARIZATION: d(X,Y,Z) = N(X+Y+Z) − N(X+Y) − N(X+Z) − N(Y+Z) + N(X)+N(Y)+N(Z),
                   with d(X,X,X) = 6 N(X)  (the symmetric trilinear form T_{ijk}).
```

These are the ONLY admissible invariant-tensor sources for the "trace-form-invariant" count. The cubic-norm polarization `d(X,Y,Z)` is a symmetric trilinear form; the trace form `Tr(X∘Y)` is a symmetric bilinear form. **The decisive question is whether an ANTISYMMETRIC orientation/volume element (a candidate ε) and the EH normalization are reachable from these symmetric intrinsic data** — see the crux below.

### Required Techniques

| Technique | What It Does | Where Applied | In-Repo Anchor |
| --- | --- | --- | --- |
| Invariant-tensor nullspace over Q | enumerate the space of `G`-invariant bilinear contractions of `F` onto a 4-form by solving the invariance linear system `δ_g T = 0` for all generators g, exact over Q | the decisive dimension count | `exact_qq_rank`, `span_rank_over_QQ` (orbit_dimension_gate.py) |
| Residual-structure-group action | build the so(3,1) (and the so(6) ideal) generators on the frame indices from the Phase-75 residual analysis; act on the quadratic-in-F tensor space | constructing the invariance constraints | Phase 75 residual `21=so(3,1)⊕so(6)`; `cartan_phaseA_coframe.py` |
| Reachability from `Tr`/`det_3` | express the candidate invariant 4-forms in a basis and test which lie in the span generated by `Tr(X∘Y)`-contractions and `det_3`-polarization tensors | the trace-form-invariant subspace | `c`, `polarize_d`, `Tr` (ring_lemma) |
| ε vs Pontryagin discriminant | distinguish the ε-contraction `ε_{abcd}R^{ab}∧R^{cd}` (Euler) from `R^{ab}∧R_{ab}` (Pontryagin) — the two bare invariants — by their action on a generic `R[ω]` | confirming dim≥2 bare, and which survive | new code (small) |
| AST input-ban guard | assert no `∫ε F∧F`, `−1/2`, `16πG`, MM action, SUSY symbol enters the FORCED determination as load-bearing input | the whole decisive path | replicate `ast_guard_T`/`source_guard` (cartan_phaseB_einstein.py) |

### Approximation Schemes

**None.** This is exact symbolic representation theory / invariant theory over Q. There is no small parameter, no perturbation, no numerical sweep. The decisive output is an integer (a dimension/rank) plus an identity (generator == ε with cubic-norm-fixed normalization), both exact over Q. (This is why **no experiment-designer pass is needed** — see Plan-Shape.)

## Standard Approaches

### Approach 1: Invariant-contraction-space dimension count over Q (RECOMMENDED — the contract's decisive computation)

**What:** Compute, exact over Q, (a) the dimension of the space of `SO(3,1)`-invariant quadratic-in-`F` 4-form contractions [expect 2: Euler + Pontryagin]; then (b) the dimension of the strictly smaller **trace-form-invariant** subspace — those contractions buildable from `Tr(X∘Y)` and `det_3` alone (and `(E_11,u)`-forced structures), with NO posited ε; then (c) test whether that subspace is 1-dim AND its generator equals the ε-contraction with a `det_3`-fixed normalization.

**Why standard / why this IS the test:** This is the operational form of the forced-vs-posited question as stated in the contract, the ROADMAP, and PITFALLS.md Pitfall 1: "the space of trace-form-invariant quadratic contractions of F is **one-dimensional** (compute it — Schur/invariant-theory count over the residual structure group), and that unique invariant **equals** the ε-contraction up to the normalization the cubic norm fixes. If the invariant space is >1-dimensional, or the ε-contraction is only one choice among several, or the normalization has to be put in by hand → POSITED → fp-imported-action."

**Track record:** The exact-over-Q rank/nullspace machinery (`exact_qq_rank`, `span_rank_over_QQ`) is the same tooling that produced the Phase-75 residual `21=so(3,1)⊕so(6)` decomposition and the Phase-64.1/65 `324/324` inner-derivation annihilation that PINNED `det_3` as the unique F_4-invariant cubic norm. The invariant-theory facts (2-dim bare space) are textbook (Euler + Pontryagin are the two independent quadratic curvature 4-forms in 4d).

**Key steps:**
1. **Enumerate the bare invariant space.** Build the space of quadratic-in-`F` 4-forms invariant under the residual structure group on the frame indices (the `so(3,1)` forced by `(E_11,u)` from Phase 75). Expect **dim = 2**: the Euler/ε-contraction `ε_{abcd}R^{ab}∧R^{cd}` and the Pontryagin `R^{ab}∧R_{ab} = δ^{ac}δ^{bd}R_{ab}∧R_{cd}` (built from the trace form / Killing metric `η_{ab}`). Verify exactly over Q by solving the invariance linear system (nullspace) and/or by exhibiting the two independent invariants acting on a generic `R[ω]`.
2. **Restrict to the trace-form-invariant subspace (THE crux).** The Pontryagin form is built from the **symmetric** Killing/trace-form metric `η_{ab}` (which IS reachable from `Tr(X∘Y)` restricted to the frame); the Euler/ε form is built from the **antisymmetric** orientation tensor `ε_{abcd}`. The decisive question: **is `ε_{abcd}` (and the EH normalization) reachable from `Tr(X∘Y)` and `det_3`?** Compute the span of invariant 4-forms generated by the intrinsic data and read off its dimension and whether ε is in it.
3. **Decide.** `dim(trace-form-invariant subspace)==1 AND generator==ε with det_3-fixed normalization` ⇒ **STRONG WIN**. Otherwise (`dim>1`, i.e. both ε and Pontryagin reachable so ε is a non-unique choice; OR ε not reachable / normalization imported) ⇒ **`fp-imported-action`**.

**Known difficulties at each step:**
- Step 1: the "4-form" / `∧` bookkeeping is on the slice coordinate indices; the *invariant-tensor* count is on the **frame** indices (a,b,c,d=0..3) under so(3,1). Keep the two index sets distinct (frame a,b vs slice μ,ν). The invariant count is a finite-dimensional linear-algebra problem on the frame indices — the slice wedge is a fixed top-form.
- Step 2: "reachable from `Tr`/`det_3`" must be made operational. The trace form supplies the symmetric `η_{ab}` (hence Pontryagin AND the `δ^{ac}δ^{bd}` contraction); the cubic norm `det_3` is a SYMMETRIC trilinear form. **A symmetric bilinear + a symmetric trilinear do not obviously generate an antisymmetric `ε_{abcd}`** — this is precisely why the most-likely verdict is `fp-imported-action`. The phase must MEASURE whether some combination (e.g. a Pfaffian-like object, or a `det`/orientation induced by the cubic norm on the Peirce blocks) supplies ε; do not assume either way.
- Step 3: the normalization (→ Newton's constant `1/16πG`) must be READ OFF the cubic norm, not put in by hand. If the dimension is 1 but the normalization is free / imported, it is still `fp-imported-action`.

### Approach 2: Direct algebraic reachability of ε from `det_3` polarization (CROSS-CHECK / sharpening of Step 2)

**What:** Test concretely whether the totally-antisymmetric `ε_{abcd}` on the 4d frame arises as a derived object from the cubic-norm polarization `d(·,·,·)` restricted to the soldered `V_0≅R^{3,1}` block (the Phase-75 image), or from a Pfaffian of the trace-form Gram. If the cubic norm's restriction to the Lorentz block carries a natural volume/orientation element that equals ε up to the cubic-norm normalization, that is the FORCED witness; if it only ever produces symmetric contractions (η-traces, Pontryagin), ε is imported.

**When to use:** As the load-bearing sharpening of Approach-1 Step 2 (they are the same question from two angles). Recommended as a second leg so the verdict does not rest on a single counting.

**Tradeoffs:** More algebra (explicit polarization tensors on the Peirce blocks); but it is the most direct way to answer "does the cubic norm SUPPLY an ε" rather than inferring it from a dimension count alone.

### Anti-Patterns to Avoid

- **fp-imported-action (THE central risk):** declaring a STRONG WIN whose final step is "and contracting MM-style with `ε F∧F` gives Einstein–Hilbert." That is the posited action, not a derivation. The ε-contraction, the `SO(4,1)→SO(3,1)` breaking, and the `1/16πG` normalization are EXTERNAL input unless DERIVED from `Tr`/`det_3`.
  - _Example:_ computing `S_MM=∫ε F∧F`, expanding to EH+Λ+GB, and reporting "Einstein recovered" — WRONG; the ε was the input. The phase must instead COUNT whether ε is forced.
- **Confirming Einstein (structuring the phase to find a win):** PITFALLS.md is explicit — "Do NOT structure Phase C to 'confirm Einstein.'" The phase MEASURES a dimension; `fp-imported-action` is the HIGH / most-likely outcome and a full publishable closure.
- **Testing the wrong object (tautology trap, [[feedback_test_right_object_not_tautology]]):** auditing a quadratic-in-F Maxwell/Pontryagin stress instead of the **linear-in-R** Einstein object `ε_{abcd}R^{ab}∧e^c∧e^d`. The EH term is LINEAR in Riemann wedged with the tetrad. "A 2-form's Maxwell stress is traceless in 4d" is a tautology that also kills real GR. The contraction-space being audited is the one that yields the EH `ε R∧e∧e` term, NOT a generic `F²` Pontryagin/Maxwell stress.
- **fp-float-decisive:** any dimension/rank/contraction-space-dim verdict on `numpy`/float. The cancellations are exact; use `sympy.Matrix.rank`/`nullspace` over QQ only.
- **fp-octonion-algebra:** `octonion_algebra.py` is BANNED (buggy `(x1 x2)x3` associator order); det SSOT = `ring_lemma_verification.py det_3`.
- **fp-reuse-cone-hessian:** do NOT reuse the v17.0 symmetric/real cone-Hessian Riemann as load-bearing — this is the antisymmetric/Lie sector. (Allowed only as a soft Re(QGT) sanity if at all; not relevant to the contraction-space count.)
- **Any thermodynamic/modular/ensemble argument (Jacobson/Verlinde/Connes–Rovelli):** explicitly rejected (Bryan's standing constraint).

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| --- | --- | --- | --- |
| **Bare SO(3,1)-invariant quadratic-curvature 4-form space is 2-dim** | spanned by Euler `ε_{abcd}R^{ab}∧R^{cd}` and Pontryagin `R^{ab}∧R_{ab}` | standard 4d topology (web-confirmed; Nieh–Yan is torsionful, excluded for Levi-Civita ω) | the baseline dimension; ε is NOT unique among quadratic invariants ⇒ forced-ness needs the trace-form restriction to collapse 2→1 |
| **MM ε-action decomposition** | `ε F∧F = ε R∧R − (2Λ/3) ε R∧e∧e + (Λ²/9) ε e∧e∧e∧e` (GB + EH + Λ) | Wise gr-qc/0611154; MM 1977 | the EH term is LINEAR-in-R via `e∧e`; identify exactly which term is "Einstein" |
| **At Λ=0, ε F∧F = Gauss–Bonnet only (topological, no GR)** | `ε R∧R` = Euler density; no EOM | web-confirmed; MM/Wise | Phase 77 MEASURED Λ=0 ⇒ even the posited ε-action is topological at the vacuum (a second independent fp-imported-action argument) |
| **det_3 is the UNIQUE F_4-invariant cubic norm** | `N(X)=αβγ−α|x1|²−β|x2|²−γ|x3|²+2Re((x2 x1)x3)`; 324/324 inner-derivation annihilation; CH | `ring_lemma_verification.py`; Phase 64.1/65 | the cubic-norm invariant-tensor source; its uniqueness is what makes the normalization (if forced) canonical |
| **Tr(X∘Y) is the F_4-invariant trace form** | `c(X,Y)=Tr(jordan(X,Y))`, jordan=(1/2)(AB+BA) | `ring_lemma_verification.py` | the symmetric bilinear invariant-tensor source (supplies η_{ab}, hence Pontryagin) |
| **(E_11,u) forces so(3,1) (Phase 75 SURVIVES)** | residual `21=so(3,1)[6]⊕so(6)[15]`; so(6) a trivial-on-spacetime ideal; res/so(6)=so(3,1) | derivations/75; `cartan_phaseA_coframe.py` | the residual structure group whose invariants are counted; so(3,1) (not the full so(9,1)) is the forced symmetry of the contraction |
| **Phase 77: R[ω] genuine Riemann, G[g] NOT Einstein-form intrinsically; Λ=0** | 6/6 cross-check exact/Q, torsion=0; G≠κT+Λg for any global (κ,Λ); Λ=0 measured | 77-02-SUMMARY.md | the premise: Einstein, if any, only via a posited action ⇒ this phase is decisive |

**Key insight:** The whole phase reduces to a finite-dimensional invariant-theory question with a KNOWN baseline (2-dim bare space) and a KNOWN intrinsic toolkit (a symmetric bilinear `Tr(X∘Y)` and a symmetric trilinear `det_3`). The novel content is **whether those symmetric intrinsic data generate the antisymmetric ε (and its normalization)**. Re-deriving the 2-dim bare space, the MM decomposition, or the det_3 uniqueness wastes budget — cite them.

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| --- | --- | --- | --- |
| Phase-77 `F`, Lorentz block `R[ω]^{ab}_{μν}`, `e∧e` mixed form | the curvature the contraction acts on (no rebuild) | `cartan_phaseB_curvature.py` (`curvature_F`, `split_blocks`, `riemann_lower_from_F`) | at a rational basepoint; M≠0 for a generic R[ω] |
| `exact_qq_rank`, `span_rank_over_QQ` | exact-over-Q dimension/rank of the invariant space | `orbit_dimension_gate.py` | sympy over QQ |
| `polarize_d`, `c`, `Tr` | the intrinsic invariant tensors to test ε-reachability | `ring_lemma_verification.py` | the trace-form-invariant subspace generators |
| AST-guard / source-guard | the input-ban enforcement | `cartan_phaseB_einstein.py` (`ast_guard_T`, `source_guard`) | replicate for the ε-not-imported assertion |

### Relevant Prior Work (the contrast class — CITE for orientation, AVOID the Lagrangians)

| Program | Authors | Year | Where it imports the action (the `fp` they commit) | What to Extract |
| --- | --- | --- | --- | --- |
| **GST magic supergravity** | Gunaydin–Sierra–Townsend | 1983–84 | POSITS the N=2 Maxwell–Einstein SUGRA Lagrangian on `E_{6(-26)}/F_4`; the `−R/2` is the assumed N=2 multiplet's own output (the C_IJK that defines special-real geometry also fixes the gravitational term) | THE in-program precedent; the dead `47-*`..`50-*`,`53-*` route; cite as the canonical `fp-imported-action` example |
| **Singh trace dynamics / division algebras** | T. P. Singh et al. | 2020– (arXiv:2009.05574) | POSITS a Planck-scale trace-dynamics Lagrangian + the Connes spectral action principle; gravity is put in via the spectral/aikonic action, not derived from the algebra's invariant geometry | cite as a contemporary exceptional-Jordan-gravity program that imports its action (the spectral action) |
| **Castro–Perelman Clifford/exceptional gravity** | C. Castro Perelman | 2000s– | POSITS a "candidate action" for an E8 gauge theory of gravity in Clifford `Cl(16)` space (conformal-gravity/Yang–Mills GUT); the gravitational action is constructed/posited, not forced by a cubic-norm invariant count | cite as another posited-action exceptional program; contrast with our forced-vs-posited TEST |

**Why the contrast matters:** all three POSIT an action and read off Einstein gravity from the matching geometry. Our test is non-circular precisely because it does NOT posit `∫ε F∧F` — it asks whether the ε-contraction is forced by `Tr`/`det_3`. Pinning down WHERE each imports the action lets the verdict say precisely what "posited by hand" means and why `fp-imported-action` (if that is the outcome) is in the same equivalence class as GST/Singh/Castro — an honest partial, not a derivation.

## Computational Tools

### Core Tools

| Tool | Module | Purpose | Why Standard |
| --- | --- | --- | --- |
| SymPy 1.14.0 | `Matrix.rank`, `Matrix.nullspace`, `Rational`, `cancel`, `eye`, `zeros` | exact-over-Q invariant-tensor nullspace / dimension count | the project SSOT; exact, deterministic, no float |
| `ring_lemma_verification.py` | `det_3`, `Tr`, `c`, `jordan`, `polarize_d`, `X_from_symbols`, `h3o_from_coords` | the intrinsic trace-form/cubic-norm invariant tensors (the ONLY admissible sources) | certified F_4-invariant; `octonion_algebra.py` BANNED |
| `cartan_phaseB_curvature.py` | `assemble_A`, `curvature_F`, `split_blocks`, `riemann_from_omega`, `riemann_lower_from_F`, `tetrad_at_point` | the curvature `F`, Lorentz block `R[ω]`, `e∧e`, tetrad — the objects contracted | Phase-77 validated, exact over Q |
| `orbit_dimension_gate.py` | `exact_qq_rank`, `span_rank_over_QQ`, `infinitesimal_action` | exact-over-Q rank/nullspace for the invariant dimension; so(3,1) generator action | validated on Phase-75 residual + Phase-65 anchors |
| `cartan_phaseB_einstein.py` | `ast_guard_T`, `_forbidden_ids_used`, `source_guard` | the AST input-ban guard (no imported action, no octonion_algebra, no numpy) | the discipline that held Phase-77 honest |

### Supporting Tools

| Tool | Purpose | When to Use |
| --- | --- | --- |
| `derivations/75-coframe-reduction.tex`, `cartan_phaseA_coframe.py` | the so(3,1) residual generators (Phase-75) on the frame indices | building the invariance constraints |
| sympy `simplify`/`cancel` | per-entry exact simplification | every matrix op |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| --- | --- | --- |
| nullspace invariant count | character/Schur dimension formula by hand | the explicit nullspace over Q is auditable and matches the project's exact-over-Q discipline; a hand character count is harder to certify |
| reuse Phase-77 `F` | rebuild a generic curvature 2-form ansatz | reusing the validated `F`/`R[ω]` ties the count to the actual route object (no fp-relabel risk) |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| --- | --- | --- | --- |
| invariant-tensor nullspace on frame indices (a,b,c,d=0..3) | seconds | small linear system (the invariant space of quadratic-in-curvature 4-forms is low-dim) | the index space is tiny (4 frame indices); no watchdog risk |
| ε-reachability from `Tr`/`det_3` (polarization span) | seconds-to-minutes | symbolic polarization tensors on Peirce blocks | evaluate at a rational basepoint; the count is exact-over-Q linear algebra |
| (if any geometry leg) `R[ω]` at a rational basepoint | seconds | (already done in Phase 77) | reuse `cartan_phaseB_curvature` substitute-then-evaluate |

**No watchdog risk:** unlike Phase 77 (4×4 symbolic matrix inverses), Phase C is a finite-dimensional linear-algebra count on 4 frame indices plus the intrinsic-tensor span — small, fast, exact over Q.

**Installation / Setup:** No new packages. Python 3.14.x / SymPy 1.14.0 already present.

```bash
# No installation needed. Verify the warm engines import:
python3 -c "import sys; sys.path.insert(0,'code'); import ring_lemma_verification, cartan_phaseB_curvature, orbit_dimension_gate; print('OK')"
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| --- | --- | --- | --- |
| Bare invariant space dim == 2 | the baseline (Euler + Pontryagin) is reproduced | nullspace of the so(3,1)-invariance system on quadratic-in-curvature 4-forms, exact over Q | dim = 2 (sanity anchor: if not 2, the setup is wrong — debug, do not interpret) |
| ε and Pontryagin independent on a generic `R[ω]` | the two invariants are genuinely distinct | evaluate `ε_{abcd}R^{ab}∧R^{cd}` and `R^{ab}∧R_{ab}` on the Phase-77 `R[ω]` at a rational basepoint | two distinct rationals; linearly independent |
| `Tr(X∘Y)` restricts to the frame η_{ab} | the trace form supplies the symmetric metric (Pontryagin source) | restrict `c` to the soldered V_0≅R^{3,1} frame; compare to η=diag(+1,−1,−1,−1) | matches the (1,3) Killing/trace-form metric |
| det_3 SSOT re-pass | the cubic norm is the certified F_4-invariant | `det_3(I)=1`, `det_3(diag)=abc`, polarize_d=6N, 324/324 (or cite Phase 64.1/65) | all pass exact over Q |
| AST input-ban guard | no posited action enters the FORCED determination | assert no `ε F∧F`/`−1/2`/`16πG`/MM-action symbol is load-bearing in the forced count | guard passes |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| --- | --- | --- | --- |
| Λ=0 ε-action | the MEASURED vacuum | `ε F∧F → ε R∧R` = Gauss–Bonnet topological (no GR) | web-confirmed; MM/Wise |
| bare 4d quadratic invariants | Levi-Civita ω (torsion=0) | exactly 2 (Euler + Pontryagin; Nieh–Yan excluded) | standard topology |
| GST/Singh/Castro | exceptional-Jordan gravity | all POSIT an action ⇒ `fp-imported-action` class | the contrast references |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| --- | --- | --- | --- |
| all decisive numbers (the dimension, the identity) | sympy over QQ | EXACT (zero tolerance) | dim=1 (STRONG WIN) or dim>1 / ε-unreachable (fp-imported-action) |
| invariant independence | `sympy.Matrix.rank` over QQ | exact | rank = the invariant-space dimension |

### Red Flags During Computation

- **Bare invariant space dim ≠ 2** → the so(3,1)-invariance setup is buggy (the baseline MUST be Euler + Pontryagin); debug before interpreting.
- **"ε-contraction gives Einstein-Hilbert" appearing as the FINAL step** → the posited action smuggled in; that is the `fp-imported-action` the phase is auditing, NOT a derivation.
- **A float/`numpy.linalg` rank on the decisive dimension** → `fp-float-decisive`; switch to `sympy.Matrix.rank` over QQ.
- **The normalization (`1/16πG`) put in by hand** → even if dim=1, this is `fp-imported-action`; the normalization must be read off `det_3`.
- **Auditing a quadratic-in-F Maxwell/Pontryagin stress as "the Einstein object"** → wrong object (tautology trap); the Einstein term is the LINEAR-in-R `ε R∧e∧e`.

## Common Pitfalls

### Pitfall 1: fp-imported-action — declaring a STRONG WIN that only holds because the MM/EH action was posited (THE central risk, the GST sin in new clothes)

**What goes wrong:** assembling `F`, reaching for the standard MM ε-contraction `∫ε F∧F`, expanding to EH+Λ+GB, and reporting "gravity from h_3(O)" — when the ε-contraction, the `SO(4,1)→SO(3,1)` breaking, and the `1/16πG` normalization were carried in by the posited action, exactly as `−R/2` was carried in by the assumed N=2 SUSY closure in the dead GST route.
**Why it happens:** the (A)dS Cartan/MM literature is action-shaped — every reference writes `∫ε F∧F` as "the" MM action and reads off EH+Λ. Confirmation bias ("Einstein is the hoped-for answer") plus a literature that hands you the ε-contraction for free makes the circular step feel like textbook physics. The deadliest version is subtle: not citing the MM action explicitly, but silently using its ε-contraction or its `−R/2` dictionary "because that is how you get gravity from F."
**How to avoid:** the forced-vs-posited test IS the phase. Compute the dimension of the trace-form-invariant quadratic-in-F contraction space; require dim==1 AND generator==ε with `det_3`-fixed normalization for FORCED. Declare and enforce the **hard input ban** (Phase 0/A discipline, enforced here): Phase C may use ONLY `Tr(X∘Y)`, `det_3`, the Peirce decomposition under E_11, the `C_u`/π_u reduction, the soldering form `e=π_u(dE)`, the spin connection ω forced by metric-compatibility/torsion, and standard differential geometry. **Forbidden as load-bearing:** any MM/EH/SUGRA action, the `ε F∧F` contraction as an *assumed* action, the `−1/2` coefficient, `16πG`, SUSY, Weinberg, the equivalence principle as premise. Wise/MM may be cited for the Cartan-geometry statement (what F's blocks mean) — NEVER for the action that selects Einstein.
**Warning signs:** any appearance of "∫ε F∧F", "−1/2", "16πG", "MM action", or "SUSY" used as load-bearing input; a "STRONG WIN" whose final step is "and contracting MM-style gives Einstein-Hilbert"; the normalization put in by hand.
**Recovery:** report `fp-imported-action` at true strength (honest partial, NOT a derivation; the same equivalence class as GST/Singh/Castro). This is the HIGH / most-likely real outcome and a full publishable closure.

### Pitfall 2: Testing the wrong object — quadratic-in-F Maxwell/Pontryagin stress instead of the LINEAR-in-R Einstein term (the tautology trap, [[feedback_test_right_object_not_tautology]])

**What goes wrong:** auditing whether a quadratic-in-F stress (`F²`, Pontryagin `R∧R`, a Maxwell-type stress) is "Einstein-shaped" — but the Einstein–Hilbert object is `ε_{abcd}R^{ab}∧e^c∧e^d`, which is **LINEAR in the Riemann curvature** wedged with the tetrad. "A 2-form's Maxwell stress is traceless in 4d" is a TAUTOLOGY that also kills real GR (this exact error caused the Phase-76 SOFT KILL that Bryan OVERTURNED).
**Why it happens:** the MM action is quadratic in `F` (`ε F∧F`), so it is natural to think the audited object is quadratic-in-curvature; but the EH term emerges from the `R∧e∧e` *cross-term* of that square (linear in R), not from the `R∧R` piece (which is the topological Gauss–Bonnet term).
**How to avoid:** keep the audited object the EH term `ε R∧e∧e` (linear-in-R). The contraction-space count is over contractions that yield a Lagrangian 4-form; the FORCED criterion is about whether the ε that produces the linear-in-R EH term is intrinsic. Note explicitly: at Λ=0 the `R∧R` piece is ALL that survives (topological), so a quadratic-in-R audit at the measured vacuum would be auditing a topological invariant — manifestly not Einstein.
**Warning signs:** "the F² stress is traceless ⇒ not Einstein" (tautology); auditing Pontryagin/`R∧R` as "the gravity term."
**Recovery:** re-center on the linear-in-R `ε R∧e∧e` EH term and the ε that produces it.

### Pitfall 3: A symmetric→antisymmetric reachability error (assuming ε is or isn't forced without computing)

**What goes wrong:** asserting "the trace form gives a metric, so the volume element / ε is automatic" (over-claiming FORCED) OR "symmetric data can never give an antisymmetric ε, so it's imported" (over-claiming POSITED) without the exact computation.
**Why it happens:** `Tr(X∘Y)` is a symmetric bilinear and `det_3` a symmetric trilinear; whether their invariant-tensor algebra contains a totally-antisymmetric `ε_{abcd}` (e.g. via a Pfaffian, a determinant/orientation on the Peirce blocks, or the `(E_11,u)`-forced complex structure supplying an orientation) is a genuine computation, not a slogan.
**How to avoid:** MEASURE the span. A metric does fix a volume form up to orientation (`√|det g| ε`), so ε MAY be reachable as `√|η| ε` from the trace-form metric — BUT then BOTH ε (Euler) and `δδ` (Pontryagin) are reachable, so the invariant space is **2-dim, not 1-dim** ⇒ ε is a non-unique choice ⇒ still `fp-imported-action`. The STRONG WIN requires the intrinsic data to single out ε over Pontryagin AND fix the normalization — a strictly 1-dim trace-form-invariant subspace. Compute both reachabilities and the resulting dimension.
**Warning signs:** a verdict that rests on "obviously" rather than an exact dimension; claiming dim=1 while Pontryagin is also trace-form-reachable.
**Recovery:** report the exact dimension; if both ε and Pontryagin are reachable, dim≥2 ⇒ `fp-imported-action`.

## Level of Rigor

**Required for this phase:** controlled exact-over-Q invariant-theory computation with an explicit decidable criterion (physicist's proof backed by certified computation), plus human ratification of the milestone-closing verdict.

**Justification:** the project's standard; the decisive verdict is a dimension (an integer) plus an identity (generator==ε with cubic-norm-fixed normalization), both exact over Q with no floating point. As the FINAL phase of v18.0, the verdict is the milestone headline and must be human-ratified at true strength (neither inflated to a STRONG WIN nor softened).

**What this means concretely:**
- The dimension of the trace-form-invariant quadratic-in-F contraction space is computed by `sympy.Matrix.rank`/`nullspace` over QQ, zero tolerance.
- The bare-space sanity anchor (dim=2: Euler + Pontryagin) is reproduced exactly over Q before any verdict.
- The ε-identity and its `det_3`-fixed normalization are verified symbolically over Q (if FORCED) or the imported step is named explicitly (if POSITED).
- The input ban is AST/source-guarded: no posited action, `−1/2`, `16πG`, SUSY, or `octonion_algebra.py` on the decisive path.
- The verdict (STRONG WIN xor `fp-imported-action`) is reported at true strength; `fp-imported-action` is a full publishable closure, framed in the same class as GST/Singh/Castro.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| --- | --- | --- | --- |
| GST/det/Weinberg: posit N=2 SUGRA Lagrangian, read off −R/2 | the forced-vs-posited TEST: count the trace-form-invariant contraction space, do NOT posit an action | v18.0 (this phase) | the test is non-circular precisely because it refuses the posited action |
| "ε F∧F is the MM action, read off EH+Λ" | audit whether ε is FORCED by `Tr`/`det_3` (else it is imported) | v18.0 | reproducing EH from a posited ε-action is NOT a derivation |

**Superseded approaches to avoid:** the Phase-76 quadratic-in-F Maxwell-stress/Pontryagin discriminant (OVERTURNED — tautology that also kills real GR). Any route that reads Einstein off a posited `∫ε F∧F` (the GST sin). The cone-Hessian symmetric Riemann (different tensor, v17.0 NONE).

## Open Questions

1. **Is the totally-antisymmetric ε_{abcd} (and the EH normalization) reachable from `Tr(X∘Y)` and `det_3` alone?**
   - What we know: `Tr(X∘Y)` supplies the symmetric frame metric η_{ab} (hence Pontryagin AND, up to orientation, a volume form `√|η| ε`); `det_3` is the unique F_4-invariant symmetric cubic norm; the bare invariant space is 2-dim (Euler + Pontryagin).
   - What's unclear: whether the intrinsic data single out ε OVER Pontryagin (collapsing 2→1) AND fix the normalization — the STRONG WIN condition — or leave a ≥2-dim / normalization-free choice (the `fp-imported-action` condition).
   - Impact on this phase: this IS the verdict.
   - Recommendation: MEASURE the exact dimension of the trace-form-invariant subspace and the ε-identity/normalization. The contract + Phase-77 NEGATIVE + the symmetric-data structure make `fp-imported-action` the HIGH / most-likely outcome; report at true strength, do NOT inflate.

2. **Does the Λ=0 measurement (Phase 77) make even a forced ε topological-only?**
   - What we know: at Λ=0, `ε F∧F → ε R∧R` = Gauss–Bonnet (topological, no EOM, no GR); the EH term carries coefficient ∝ Λ.
   - What's unclear: whether the audit should be framed at finite Λ (where EH appears) and then note the vacuum is Λ=0, OR directly at Λ=0 (where the audited ε-contraction is topological).
   - Impact: framing of the verdict; it is a second independent argument for `fp-imported-action` (even the posited ε-action gives no GR at the measured vacuum).
   - Recommendation: count the invariant space at the structural level (Λ formal), report the dimension/ε-identity verdict, AND note the Λ=0 corollary (the EH term's coefficient vanishes at the measured vacuum) as a reinforcing observation. Do NOT reintroduce Λ<0.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| --- | --- | --- | --- |
| invariant nullspace count over Q | the so(3,1)-action setup is ambiguous on the frame indices | Approach 2 (direct ε-reachability from `det_3` polarization on the Peirce blocks) | low — same question, more explicit algebra |
| dimension count alone is ambiguous | borderline (e.g. ε reachable but normalization unclear) | add the explicit normalization read-off from `det_3` (is `1/16πG` fixed or free?) | low — a single symbolic check |
| both legs inconclusive | genuinely subtle invariant theory | report `fp-imported-action` (the conservative, contract-favored verdict) with the explicit gap named | none — the honest default |

**Decision criteria:** declare STRONG WIN ONLY if the trace-form-invariant subspace is exactly 1-dim AND its generator equals the ε-contraction AND the normalization is fixed by `det_3` — all three, exact over Q. Any shortfall (dim>1, ε one-of-several, normalization imported/free, ε not reachable) ⇒ `fp-imported-action` at true strength.

## Sources

### Primary (HIGH confidence)
- **D. K. Wise, gr-qc/0611154 (CQG 27 (2010) 155010), "MacDowell–Mansouri gravity and Cartan geometry"** — `A=ω+(1/ℓ)e`; `F=(R−(Λ/3)e∧e)+d_ω e`; `S_MM=(−3/2GΛ)∫tr(F̂∧⋆F̂) ∝ ∫ε F∧F`; the `SO(4,1)→SO(3,1)` breaking done "by hand"; the EH+Λ+GB decomposition. Carried verbatim from 77-RESEARCH.md (read from the locally-saved PDF in Phase 77; the web text-layer was not extractable this session) + web-cross-confirmed.
- **MacDowell & Mansouri, PRL 38 (1977) 739** — the original broken dS/Lorentz gauge mechanism; the `∫ε F∧F` action.
- **In-repo `ring_lemma_verification.py`** (read this session): `det_3` (the unique F_4-invariant cubic norm; 324/324 inner-derivation annihilation), `Tr`, `c=Tr(X∘Y)`, `jordan`, `polarize_d`. The intrinsic invariant-tensor SSOT.
- **In-repo `cartan_phaseB_curvature.py` / `cartan_phaseB_einstein.py`** (read this session): the curvature `F`, Lorentz block `R[ω]`, `e∧e`, tetrad, AST-guard/source-guard.
- **In-repo Phase 77 SUMMARY/PLAN** (read this session): the NEGATIVE / fp-imported-action partial verdict; Λ=0 measured; the contract-wiring template to mirror.
- **Web-confirmed standard facts:** (i) at Λ=0 the MM action reduces to the Gauss–Bonnet/Euler topological term (no EOM, no GR) [arxiv.org/abs/gr-qc/0611154; math.ucr.edu/home/baez/derek/]; (ii) the two independent SO(3,1)-invariant quadratic-curvature 4-forms in 4d are Euler and Pontryagin [arxiv.org/html/2512.22400; arxiv.org/pdf/1804.07440].

### Secondary (MEDIUM confidence)
- `.gpd/research/METHODS.md`, `PITFALLS.md`, `SUMMARY.md` (project-level v18.0 research, 2026-06-01) — Method 2 (Cartan/MM assembly + ε-contraction); Pitfall 1 (fp-imported-action, the operational forced-vs-posited test + the hard input ban); the forced-vs-posited concreteness.
- **GST: Gunaydin–Sierra–Townsend, "Exceptional supergravity theories and the magic square," Phys. Lett. B 133 (1983) 72** [sciencedirect.com/science/article/abs/pii/0370269383901089; ncatlab.org/nlab/show/magic+supergravity] — the in-program `fp-imported-action` precedent (geometry/contrast only).
- **Singh, arXiv:2009.05574, "Trace dynamics and division algebras"** [arxiv.org/abs/2009.05574] — contemporary exceptional-Jordan-gravity program that imports a trace-dynamics + spectral action (contrast).
- **Castro Perelman, "An Exceptional E8 Gauge Theory of Gravity in D=8, Clifford Spaces and Grand Unification"** [semanticscholar.org/.../918f28c9...; worldscientific.com/doi/abs/10.1142/S0219887809003588] — posited E8/Clifford gravity action (contrast).

### Tertiary (LOW confidence)
- None load-bearing.

## Caveats and Alternatives (pre-submission self-critique)

1. **Assumption that might be wrong:** that the trace-form-invariant contraction space is the right operationalization of "forced." If a reviewer argued the FORCED criterion should be about the *full* SO(4,1)/SO(3,2) (not the broken SO(3,1)) invariants, the count could differ — but the contract, ROADMAP, and PITFALLS.md all specify the SO(3,1)/residual-structure-group count, and the SO(4,1)→SO(3,1) breaking is exactly the "by hand" step being audited, so counting at the broken SO(3,1) level is correct. Flagged as the key modeling choice.
2. **Alternative dismissed quickly:** computing the audit at finite Λ (where EH appears) vs at the measured Λ=0 (where the ε-action is topological). I recommend the structural count (Λ formal) as primary with the Λ=0 corollary as reinforcement, because the dimension/ε-identity is the contract's decisive object and is Λ-independent as an invariant count; the Λ=0 topological observation is a second, reinforcing argument, not the primary verdict.
3. **Understated limitation:** the dimension count certifies whether ε is forced *as an invariant tensor*; it does not by itself prove the *dynamical* claim "gravity is the Lie-sector connection curvature." But Phase 77 already settled the dynamical side (NEGATIVE: G[g] not Einstein-form intrinsically), so Phase C's invariant count is exactly the remaining decidable piece — whether the action that WOULD supply Einstein is forced or imported. The two phases together give the full milestone verdict.
4. **Simpler method overlooked?** One could argue the phase is "already decided" by Phase 77 + the literature (Wise's explicit "broken by hand" + the 2-dim bare space + Λ=0-is-topological all point to `fp-imported-action`). That is true as a *physics expectation*, but the contract requires the **exact-over-Q dimension computation** to render the verdict at true strength (not as an argument from authority). The computation also leaves open the small chance the intrinsic `det_3` supplies a forced ε — which only an explicit count can confirm or exclude. So the computation is required, not optional.
5. **Would a specialist disagree?** A Cartan-gravity specialist might say "of course the MM action is posited — Wise says so explicitly; why compute?" The answer: the milestone's STRONG-WIN hypothesis is that h_3(O)'s *specific* cubic-norm/trace-form structure might force ε where generic MM does not (the exceptional-Jordan structure is richer than a generic SO(3,1) frame). The exact count is the only way to confirm or exclude that exceptional-structure escape hatch — and the negative-result-is-success discipline demands it be MEASURED, not assumed.

## Metadata

**Confidence breakdown:**
- Mathematical framework: HIGH — MM/Wise ε-contraction and EH+Λ+GB decomposition carried verbatim + web-cross-confirmed; the 2-dim bare invariant space (Euler+Pontryagin) and the Λ=0-is-topological fact are standard and web-confirmed; `det_3`/`Tr(X∘Y)` read from the SSOT this session.
- Standard approaches: HIGH — the invariant-contraction-space dimension count is the contract's stated decisive computation, with PITFALLS.md giving the operational recipe; the exact-over-Q rank/nullspace tooling is validated.
- Computational tools: HIGH — all reuse functions (`det_3`, `Tr`, `c`, `exact_qq_rank`, `curvature_F`, `split_blocks`, AST/source guards) read and confirmed; engine imports verified clean this session; no watchdog risk (small linear algebra).
- Validation strategies: HIGH — the dim=2 bare-space sanity anchor, the ε/Pontryagin independence check, the trace-form-metric restriction, and the det_3 SSOT re-pass all have in-repo precedent.
- The OUTCOME (FORCED vs POSITED): MEDIUM by design — that is what Phase C measures; `fp-imported-action` is the HIGH / most-likely real verdict per the contract, Phase 77, and the symmetric-intrinsic-data structure.

**Research date:** 2026-06-02
**Valid until:** stable (physics + conventions locked); re-check if CONVENTIONS §11 or the engine API changes.

## Recommended Plan Structure

**Two plans, mirroring the Phase-77 77-01/77-02 split**, with the decisive computation non-interactive and the milestone-closing verdict interactive (human ratifies). This is the FINAL v18.0 phase ⇒ the verdict checkpoint MUST be INTERACTIVE.

**Plan 78-01 — The decisive forced-vs-posited computation (wave 1, NON-interactive):**
- **Task 1 (setup + sanity anchors):** re-pass the det SSOT (`det_3(I)=1`, `det_3(diag)=abc`, polarize_d=6N; or cite Phase 64.1/65); load `Tr(X∘Y)` and confirm its restriction to the soldered V_0≅R^{3,1} frame == η=diag(+1,−1,−1,−1); declare and AST/source-guard the **hard input ban** (no `∫ε F∧F`/`−1/2`/`16πG`/MM-action/SUSY/`octonion_algebra`/`numpy.linalg` on the decisive path).
- **Task 2 (bare invariant space — the dim=2 anchor):** build the so(3,1)-invariant quadratic-in-curvature 4-form space on the frame indices (so(3,1) forced by (E_11,u) from Phase 75); confirm **dim=2** (Euler `ε R∧R` + Pontryagin `R∧R`) exact over Q; verify the two are independent on the Phase-77 `R[ω]` at a rational basepoint. (Sanity: if not 2, debug the setup.)
- **Task 3 (THE decisive count — trace-form-invariant subspace):** compute the dimension of the subspace of quadratic-in-F contractions buildable from `Tr(X∘Y)` and `det_3` alone (and (E_11,u)-forced structures), exact over Q via `sympy.Matrix.rank`/`nullspace`; test ε-reachability (is `ε_{abcd}` derivable, e.g. as `√|η| ε` from the trace-form metric, or from a `det_3` polarization/orientation?) and Pontryagin-reachability; read off whether the subspace is 1-dim and == ε with a `det_3`-fixed normalization.
- INTERACTIVE: no (computational, exact symbolic).

**Plan 78-02 — Verdict synthesis + contrast framing + ratification (wave 2, depends_on 78-01, INTERACTIVE):**
- **Task 1 (verdict synthesis):** map the 78-01 dimension/identity to the verdict ladder — STRONG WIN (dim==1 AND ==ε AND normalization det_3-fixed) xor `fp-imported-action` (dim>1 / ε one-of-several / ε unreachable / normalization imported); note the Λ=0 corollary (at the measured vacuum even the posited ε-action is topological Gauss–Bonnet).
- **Task 2 (contrast class):** frame GST / Singh / Castro as the explicit `fp-imported-action` contrast (where each imports its action); write `derivations/78-circularity-audit.tex` documenting the count, the ε-identity (or its failure), the verdict at true strength, and the milestone-closing summary.
- **Task 3 (checkpoint:human-verify, BLOCKING):** present the milestone-closing verdict for ratification — STRONG WIN xor `fp-imported-action` (the HIGH / most-likely outcome) — at true strength, neither inflated nor softened; resume signal `approved: STRONG WIN` or `approved: fp-imported-action` (with the honest characterization).
- INTERACTIVE: yes (the milestone-closing verdict; the FINAL v18.0 phase).

**Experiment-designer pass:** NOT needed — this is exact symbolic representation theory / invariant theory, no numerical sweep, no parameter scan. (Confirm in the plan header.)

**Contract wiring (mirror 77-02-PLAN):** claims `claim-forced-einstein`; deliverable `deliv-phaseC` (derivation) + a code deliverable (the contraction-space driver); acceptance test `test-forced-vs-posited` (FORCED→STRONG WIN xor posited→fp-imported-action, at true strength); references `ref-mm-1977` (read,cite), `ref-wise` (read,cite — for what F's blocks mean, NEVER for the action as source), `ref-gst` (cite,avoid — the Lagrangian); forbidden proxies `fp-imported-action` (central), `fp-float-decisive`, `fp-reuse-cone-hessian`, `fp-octonion-algebra`. All decisive numbers exact over Q; det SSOT = `ring_lemma_verification.py det_3`; the AST/source-guard input ban enforced throughout.
