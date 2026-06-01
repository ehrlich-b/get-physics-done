# Research Summary

**Project:** v18.0 — Gravity as the Curvature of the Peirce-Frame (Cartan/MacDowell-Mansouri) Connection on h_3(O)
**Domain:** Mathematical physics — Cartan/MM gauge gravity; quantum geometric tensor (Berry curvature, abelian + non-abelian Wilczek-Zee); exceptional Jordan algebra h_3(O); the Cayley plane OP^2 = F_4/Spin(9); exact-over-Q symbolic computation
**Researched:** 2026-06-01
**Confidence:** HIGH on established-math-to-cite, the four load-bearing methods, and the central risk; MEDIUM on the two genuinely-open outcomes the milestone must MEASURE (Phase A reduction dimension/signature; Phase C forced-vs-posited)

## Executive Summary

This milestone computes the **antisymmetric/Lie-sector** object that every prior gravity route in the program ignored: the curvature 2-form `F = dA + A∧A` of the Peirce-frame Cartan/MacDowell-Mansouri connection `A = ω⊕e` on h_3(O), equivalently the **Berry curvature** = imaginary part of the quantum geometric tensor (QGT) of the rank-1 idempotent state family. The (failed) v17.0 cone-Hessian route computed the **real part** (Fubini-Study metric); Provost-Vallée (1980) is the load-bearing justification that the v17.0 NONE verdict binds only `Re(Q)`, leaving the imaginary part — a genuinely different tensor — untouched. The survey confirms the route is **computationally feasible exact-over-Q with existing tooling** (no new heavy CAS), and that **three of the four sub-claims are candidate-novel** (coframe `e=dE` from an h_3(O) idempotent; Berry curvature of the OP^2=F_4/Spin(9) idempotent family; MM ε-contraction forced by the trace-form/cubic-norm).

The recommended approach mirrors the prompt's hard-gated structure and the survey sharpens it: **Phase 0** (re-pass the det SSOT + the tangent identity `E∘δ=(1/2)δ` + calibration), then the two cheap KILL gates **Phase A** (does the C_u bottleneck reduce `V_{1/2}(16)` to a 4-dim Lorentzian coframe carrying SO(3,1), *forced* by `(E_11,u)`? — pure linear algebra over Q) and **Phase A.5** (canonical Berry curvature, no metric-compatibility equation needed; SOFT-KILL diagnostic), gating the expensive **Phase B** (full Cartan assembly + Riemann cross-check) and **Phase C** (the forced-vs-posited circularity audit).

The single biggest risk is **`fp-imported-action`** and it is also the **most likely real outcome** (forced coframe but imported action: B yes, C no). Every prior exceptional/octonionic-gravity program (Singh, Castro, the in-program GST/Weinberg route) *posits* an action; Wise (gr-qc/0611154) is explicit that MM yields Einstein-Hilbert+Λ **only** via the posited ε-contraction `B^{ab}=ε^{abcd}e_c∧e_d` that breaks SO(4,1)→SO(3,1) **by hand**. A second load-bearing subtlety: OP^2=F_4/Spin(9) is rank-1, isotropy-irreducible, **not Hermitian symmetric — it carries no invariant almost-complex structure and no invariant 2-form**, so a nonzero Berry 2-form *cannot* be inherited from the unbroken idempotent family; it must be **born from the C_u / Spin(9)→Lorentz breaking**. This both supports the route's premise and is a Phase-A.5 well-definedness risk to test, not assume.

## Key Findings

### Computational Approaches

The route is feasible **exact-over-Q** with the project's existing engines; new code is small (~150–300 lines in a fresh `code/cartan_curvature_verification.py` that verbatim-copies the SSOT engine, matching the v17.0 precedent). `sympy.diffgeom` stays exact for scalar rational forms but has **no native matrix-valued connection wedge**; use a hand-rolled component-matrix curvature `F_{μν} = ∂_μA_ν − ∂_νA_μ + [A_μ,A_ν]` (the commutator = the `A∧A` term). The eigenprojector QGT `F_B = −i·Tr(P[∂_μP,∂_νP])` is exact over **Q(i)** (Gaussian rationals), not Q — a real exactness caveat: split Re/Im before any real-root signature call.

**Core approach:**

- **Hand-rolled matrix curvature `F=dA+A∧A`** over a coordinate chart — exact over Q; `sympy.diffgeom` insufficient for matrix-valued forms.
- **Eigenprojector QGT** `Q = Tr(P ∂P ∂P)`, `Re→`metric, `Im→`Berry curvature — gauge-invariant projector form preferred over the state form (which smuggles a gauge phase); exact over Q(i).
- **Reuse `code/bulk_geometry_verification.py`** — confirmed to already contain `totaro_riemann`, `hand_rolled_riemann_of_g` (independent Levi-Civita cross-check), `ricci_decomposition_n4`, `eig_signature_count` (exact Lorentzian-(1,3) gate via `real_roots`), `peirce_indices_under_E11`, `stab_E6_E11`, `stab_preserving_V0`, `h3_cone_hessian_benchmark` (K=−1/2 sign anchor). Env: Python 3.14.2 / SymPy 1.14.0 / NumPy 2.4.2 — no new packages on the decisive path.
- **`code/ring_lemma_verification.py` det SSOT** (det_3, 324/324 inner-derivation annihilation); `code/orbit_dimension_gate.py` for exact orbit/stabilizer counts.

### Prior Work Landscape

**Must reproduce / cite (established math — do NOT re-derive):**

- OP^2 = F_4/Spin(9) (Borel 1950); `T_E OP^2 = V_{1/2}(E)` from `E∘δ=(1/2)δ` (McCrimmon; Baez 2002).
- QGT real=Fubini-Study / imaginary=Berry curvature — Provost & Vallée, CMP 76 (1980) 289, DOI 10.1007/BF02193559.
- MM gravity = curvature of a broken Cartan/de Sitter connection, `∫ε F∧F = EH + Λ` — MacDowell-Mansouri, PRL 38 (1977) 739; D.K. Wise, gr-qc/0611154 = CQG 27 (2010) 155010 (the clean Cartan statement; `A=ω+(1/ℓ)e`, `F=R[ω]−(Λ/3)e∧e+d_ω e`).
- Cartan connections & soldering forms — Sharpe 1997. `h_2(C_u) ≅ R^{3,1}` Lorentzian — internal GPD `52-kkt-spacetime`.

**Novel contributions (candidate-novel — the milestone's frontier):**

- **Coframe `e=dE` from a primitive idempotent** of h_3(O) (soldering form = V_{1/2}-valued differential). Unattested.
- **Berry curvature / Im(QGT) of the OP^2 = F_4/Spin(9) idempotent family.** Unattested (and subtle — see well-definedness below).
- **MM ε-contraction *forced* by the h_3(O) trace-form / cubic-norm** (vs posited). Unattested in either direction; this is the STRONG-WIN target and the highest-risk sub-claim.

**Not novel as a philosophy (report at true strength):** "emergent gravity from Berry/QGT geometry" — Viennot (arXiv:2106.01913) already derives a Lorentz connection from the geometric-phase generator in BFSS matrix theory. v18.0's novelty is the **algebraic source** (h_3(O) idempotents + C_u) and the **MM-Einstein target**, not the QGT→gravity concept. Cite Viennot as the mechanism precedent for honesty.

**Defer:** quantizing gravity; dynamics/field equations of the matter M; cosmology.

### Methods and Tools

Five phase-mapped methods, each with explicit formulas (METHODS.md):

1. **QGT/Berry (projector form)** — Phase A.5; gauge-invariant; `Re(Q)` must reproduce the cone-Hessian (consistency anchor).
2. **MM/Cartan assembly + ε-contraction** — Phase B/C; `A=ω⊕e` in so(3,2)/so(4,1)/iso(3,1); split `F` into Lorentz block `R[ω]+Λe∧e` and torsion block `d_ω e`; the ε-contraction is exactly the Phase-C circularity locus.
3. **Reductive coset / canonical connection on F_4/Spin(9)** — Phase B; extract the Lorentz Spin(3,1) sub-block of the ambient Spin(9,1) connection compatible with the soldering form (reductive split `g=h⊕m`); the non-compact `so(3,1)⊂so(9,1)` extraction transports the compact F_4/Spin(9) connection to the `e_{6(-26)}` real form (a Phase-B detail).
4. **Complex-structure (C_u, u=e_7) reduction** of `V_{1/2}(16)` to a 4-dim Lorentzian coframe — Phase A; the open KILL question; parallels the validated `h_2(O)→h_2(C_u)≅R^{3,1}` reduction.
5. **Exact orbit/stabilizer rank** — Phase 0/A; `orbit_dimension_gate.py` for the calibration anchors and the forced-vs-arbitrary structure-group decision.

### Critical Pitfalls

1. **`fp-imported-action` (CENTRAL RISK, most-likely outcome).** Declaring "Einstein structure" that only appears because the MM/EH ε-contraction was posited by hand (the GST sin). The concrete forced-vs-posited test (Phase C): the space of trace-form-invariant quadratic-in-F contractions must be **1-dimensional AND equal the ε-contraction with a cubic-norm-fixed normalization**, else POSITED. Do NOT structure Phase C to "confirm Einstein."
2. **OP^2-not-Kähler well-definedness (Phase A.5 first checkpoint).** OP^2=F_4/Spin(9) carries no invariant 2-form; the Berry 2-form must be born from the C_u breaking. Establish `Im(QGT)` is a well-defined, generically-nonzero 2-form on the 4d slice *after* breaking, BEFORE testing its shape.
3. **`fp-arbitrary-reduction` (Phase A).** A 4-dim coframe obtained by any choice NOT forced by `(E_11,u)` — `4` must be earned, not assumed by analogy to V_0.
4. **Same-wall / `fp-relabel` (Phase A.5/B).** An EM-shaped stress content is **traceless (`T^μ_μ=0`), `~F²`, conformal** — the SOURCE side, not the curvature side. Test the matter-sourced Berry curvature at matched M-power + tensor-structure + support against an independently-frozen `T[M]` (the v17.0 Ph73 lesson: a tensor appearing ≠ Einstein; `κT~10³ < G`). The degenerate `V_{1/2}` eigenbundle is **non-abelian Berry (Wilczek-Zee): gauge-COVARIANT, not invariant** — decisive verdicts must rest on gauge-invariant scalars (traces/Wilson loops), tested under a frame rotation.
5. **Sector / dimension confusion.** Do not reuse the dead cone-Hessian (symmetric-sector, real-part) Riemann as load-bearing; do not mistake the raw 45-dim Spin(9,1) curvature for the 4d gravity connection (gravity = the 10-dim `A=ω⊕e`); torsion lives in the translation block, curvature in the Lorentz block.
6. **Arithmetic hygiene.** `octonion_algebra.py` is BANNED (buggy associator); det SSOT = `ring_lemma_verification.py` det_3. No float ranks/curvature on decisive verdicts (sympy.Matrix.rank only); Berry verdicts over Q(i) with Re/Im split. Watch the long-symbolic-run watchdog (diff-symbolic → substitute-rational-point → invert; `python -u`; commit task-by-task).

> **CORRECTION (flag for the roadmapper):** `code/peirce_coupling.py` cited in the prompt's "Build on" list **does NOT exist** in the repo. The Peirce-under-E_11 machinery lives in `code/bulk_geometry_verification.py` (`peirce_indices_under_E11`: verifies `{V_1:1, V_{1/2}:16 at engine indices 11..26, V_0:10}`) and `code/embedding_under_E_verification.py` — reuse these or build Peirce-under-E_11 fresh in Phase 0. (The machine-readable contract reference has been corrected accordingly.)

## Implications for Research Plan

The prompt's Phase 0 / A / A.5 / B / C map to roadmap **Phases 74–78**. The survey strongly endorses the ordering (cheap KILL gates first) and adds specific checkpoints.

### Phase 74 — Phase 0: Engine Recovery, Tangent Identity & Calibration

**Rationale:** every decisive verdict rests on the det SSOT + the soldering form being `V_{1/2}`-valued; pin both before any geometry.
**Delivers:** det SSOT re-passes CH + 324/324 (octonion_algebra.py absent); EXACT `E_11∘δ=(1/2)δ` for a V_{1/2} basis and `T_{E_11}OP^2 = V_{1/2}(16)`; calibration anchors reproduced (single-copy 24/Spin(8)28/trdeg3; e_6=78; orbit(E_11)=17; Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1)); K=−1/2 sign benchmark re-passed.
**Avoids:** stale-SSOT / banned-engine / wrong-association traps; resolves the `peirce_coupling.py` gap.

### Phase 75 — Phase A: Coframe-Reduction Dealbreaker (KILL GATE, do first)

**Rationale:** cheapest possible (pure linear algebra over Q); kills or greenlights the whole route.
**Delivers:** exact image dim of `π_u(V_{1/2}(16))` (expect 4); exact Gram-eigenvalue signature (expect Lorentzian (1,3)); forced-vs-arbitrary structure-group analysis (SO(3,1) forced by `(E_11,u)`?).
**Validates:** the V_0→h_2(C_u)≅R^{3,1} reduction as the precedent. **Avoids:** `fp-arbitrary-reduction`, `fp-float-decisive`.

### Phase 76 — Phase A.5: Berry-Curvature Same-Wall Gate (SOFT KILL)

**Rationale:** canonical/tautological Berry curvature needs no metric-compatibility equation → cheap diagnostic before the expensive assembly; no dependency on Phase B.
**Delivers:** **well-definedness checkpoint** (is `Im(QGT)` a nonzero 2-form on the 4d slice after C_u breaking?); the mandatory **`Re(QGT)=Hess(−log det)` consistency anchor (hard STOP if it fails)**; M=0 vacuum level; matter-sourced shape Einstein vs EM-shaped (M-power + structure + support vs `T[M]`).
**Avoids:** same-wall `fp-relabel`; non-abelian-gauge mistakes (use gauge-invariant scalars).

### Phase 77 — Phase B: Full Cartan Curvature = 4d Gravity (only if A, A.5 survive)

**Rationale:** the load-bearing dynamical object; expensive, so gated.
**Delivers:** invertible coframe `det(e^a_μ)≠0`; `ω` = Spin(3,1) projection of the ambient Spin(9,1) connection; `F=dA+A∧A` with Lorentz block = 4d Riemann (cross-checked against `hand_rolled_riemann_of_g`/Totaro on ≥5 components) + torsion block; M=0 Einstein/(A)dS level via K=−1/2; matter-sourced Riemann.
**Uses:** MM/Cartan assembly (M2) + reductive Lorentz extraction (M3); the in-repo Levi-Civita harness.

### Phase 78 — Phase C: Circularity Audit (forced vs posited)

**Rationale:** the decisive non-circularity check — the whole "win" hinges on it.
**Delivers:** whether the trace-form-invariant quadratic-in-F contraction space is **1-dimensional and equals the ε-contraction with cubic-norm-fixed normalization** (STRONG WIN) or the Einstein term is only posited (`fp-imported-action`, honest partial). Frame Singh/Castro/GST as the explicit contrast class.
**Avoids:** `fp-imported-action` — do NOT cite the MM action as the source.

### Phase Ordering Rationale

- Cost-driven: A and A.5 are seconds-to-minutes (linear algebra / canonical curvature); B and C are the expensive dynamical work. Gate B/C behind both cheap gates surviving.
- A and A.5 have **no inter-dependency** and may be planned/run in parallel.
- The `Re(QGT)=cone-Hessian` anchor (Phase A.5) is the single check that licenses the whole "imaginary part" framing — front-load it.

### Phases Requiring Deep Investigation

- **Phase 76 (A.5):** novel — Berry curvature of OP^2=F_4/Spin(9) idempotents has no literature precedent, and the OP^2-not-Kähler subtlety makes well-definedness genuinely open.
- **Phase 78 (C):** the milestone's real frontier — whether the h_3(O) trace form *uniquely forces* the ε-contraction is unattested invariant theory; likely warrants a phase-researcher dig.
- **Phase 75 (A):** the reduction outcome (image dim, signature, forced-ness) is the open KILL question — established machinery, open answer.

Phases with established methodology: **Phase 74 (0)** (re-run existing engines), **Phase 77 (B)** assembly mechanics (Wise's formulas are explicit; the in-repo Riemann cross-check exists).

## Confidence Assessment

| Area                     | Confidence | Notes                                                                                 |
| ------------------------ | ---------- | ------------------------------------------------------------------------------------- |
| Computational Approaches | HIGH       | All four new objects prototyped exact-over-Q this session; both engines import/run clean |
| Prior Work               | HIGH / MEDIUM | Must-cite refs confirmed with exact bib; exceptional-gravity-attempt census MEDIUM completeness |
| Methods                  | HIGH       | Wise MM formulas read from primary source; Provost-Vallée real/imag split confirmed     |
| Pitfalls                 | HIGH       | fp-imported-action mechanism sourced from Wise; same-wall trap = direct v17.0 Ph73 precedent |

**Overall confidence:** HIGH on the route's structure, methods, and risks; the two genuinely-open *outcomes* (Phase A reduction; Phase C forced-vs-posited) are what the milestone exists to MEASURE.

### Gaps to Address

- **Is `Im(QGT)` a nonzero 2-form on the 4d slice after C_u breaking?** (OP^2 has no invariant 2-form) — first Phase-A.5 question.
- **Does `(E_11,u)` force the 4d Lorentzian reduction?** — the Phase-A KILL question; `4` must be earned.
- **Does the h_3(O) trace form uniquely force the ε-contraction?** — the Phase-C frontier; deeper invariant theory.
- **`peirce_coupling.py` absent** — resolved in Phase 0 by reusing the engine's `peirce_indices_under_E11` (contract reference corrected).
- **Non-compact `so(3,1)⊂so(9,1)` sub-block extraction** — a Phase-B construction detail (compact F_4/Spin(9) → `e_{6(-26)}` real form).

## Sources

### Primary (HIGH)

- MacDowell & Mansouri, PRL 38 (1977) 739 — gravity as a broken de Sitter/Lorentz gauge theory.
- D.K. Wise, gr-qc/0611154 (CQG 27, 155010, 2010) — MM gravity & Cartan geometry; the ε-contraction breaks SO(4,1)→SO(3,1) by hand (the Phase-C circularity locus).
- Provost & Vallée, CMP 76 (1980) 289 — QGT: real=Fubini-Study, imaginary=Berry curvature.
- Baez 2002 (h_3(O), F_4, OP^2=F_4/Spin(9)); McCrimmon, *A Taste of Jordan Algebras* (Peirce, `E∘δ=(1/2)δ`); Sharpe 1997 (Cartan connections, soldering).

### Secondary (MEDIUM)

- Viennot, arXiv:2106.01913 — Lorentz connection from the geometric-phase generator in BFSS (the QGT→gravity mechanism precedent).
- arXiv:2503.17163 (Quantum 2026) — sub-bundle / shape-operator / Gauss-Codazzi QGT decomposition (natural machinery for the V_0-sub-slice Im(QGT)).
- arXiv:2102.09899 — eigenprojector approach to Berry curvature & quantum metric in N-band systems (the projector formula).

### Tertiary (LOW)

- Singh (arXiv:2009.05574, 2304.01213) and Castro (E_6(-26) cubic-form action) — exceptional/octonionic-gravity programs that POSIT an action; the `fp-imported-action` contrast class. (Singh 2304.01213 PDF unreadable this session; characterized from the confirmed 2009.05574 abstract — human eyeball advised only if Phase C cites Singh as the canonical contrast.)

---

_Research analysis completed: 2026-06-01 (synthesized in main context after the synthesizer agent hit a transient API error; the four scout artifacts are complete and on disk)_
_Ready for research plan: yes_
