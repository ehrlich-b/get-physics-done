# Research Roadmap: Experiential Measure on Structure Space

Deriving the fundamental laws of physics from the algebraic structure of self-modeling composite processes. See `.gpd/PROJECT.md` for the full program narrative and `.gpd/MILESTONES.md` for shipped-milestone records.

## Milestones

- **v1.0–v13.0** — Phases 1–53 (archived under `.gpd/milestones/`)
- **v14.0 Paper 5 Revision** — Phases 54–59 (PAUSED 2026-04-17, pending JMP referee report; see `.gpd/V14-CLOSEOUT.md`)
- **v15.0 The P5 ↔ Basin Restriction Lemma** — Phases 60–63 (completed 2026-05-24 — CHARACTERIZED OBSTRUCTION / coexistence-as-island; through-line survives)
- **v16.0 The (RING) Lemma** — Phases 64–69 (completed 2026-05-27 — (RING) (a)+(b)+(c) PROVED)
- **v17.0 Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry** — Phases 70–73 (completed 2026-06-01 — **NONE: curved but not Einstein-structured**; the REAL part / cone-Hessian / Jordan sector)
- **Active: v18.0 Gravity as the Curvature of the Peirce-Frame (Cartan/MacDowell-Mansouri) Connection on h_3(O)** — Phases 74–78 (physics-side; the ANTISYMMETRIC/Lie sector = Berry curvature = imaginary part of the QGT)

---

## Active Milestone: v18.0 — Gravity as the Curvature of the Peirce-Frame (Cartan/MM) Connection on h_3(O)

### Overview

This milestone computes the **antisymmetric/Lie-sector** gravitational object every prior route in the program ignored: the curvature 2-form `F = dA + A∧A` of the Peirce-frame Cartan/MacDowell-Mansouri connection `A = ω⊕e` on h_3(O), equivalently the **Berry curvature = imaginary part of the quantum geometric tensor (QGT)** of the rank-1 primitive-idempotent state family. The dead v17.0 cone-Hessian route computed the QGT's **real part** (Fubini-Study metric) and returned NONE; Provost-Vallée (1980) is the load-bearing justification that NONE binds only `Re(Q)`, leaving the imaginary part — a genuinely different tensor — untouched. The question is decided by two **cheap KILL gates first**: Phase A (does the `C_u` bottleneck reduce the 16-dim `V_{1/2}` soldering form `e=dE` to a 4-dim Lorentzian coframe carrying SO(3,1), *forced* by `(E_11,u)`?) and Phase A.5 (is the canonical Berry curvature Einstein-shaped, or does it inherit the v17.0 cone-Hessian same-wall mismatch?), which gate the expensive full Cartan assembly (Phase B) and the forced-vs-posited circularity audit (Phase C). Everything decisive is **exact over Q** (the Berry sector over Q(i), Re/Im split); the det SSOT is `code/ring_lemma_verification.py` det_3; `octonion_algebra.py` is BANNED.

> **Scope = GR (the Lorentz Spin(3,1) block).** This milestone tests whether the connection yields 4d **Einstein gravity** — not the Standard Model. The same ambient Spin(9,1) connection also carries a Spin(6)=SU(4) internal block (Pati-Salam, Phase 48); IF the GR test passes, the gauge-connection / SM-unification angle is a flagged **BONUS for a later milestone, NOT a v18.0 deliverable**. Paper 7 already HOUSES the SM rep (derive→house discipline); this milestone does not attempt to derive it.

> **NEGATIVE-RESULT-IS-SUCCESS (binding reporting discipline).** A clean Phase A KILL (no forced 4d Lorentzian coframe) or a Phase A.5 same-wall SOFT KILL is a **full, publishable closure** — report it flat, never relabel "approximately 4d" or "approximately Einstein". The **most likely real outcome** is a forced coframe but an imported action (B yes, C no): report that as `fp-imported-action`, an honest partial, NOT a win. The point is to find out whether gravity is the Lie-sector connection curvature of h_3(O), not to confirm it. Authoritative spec: `~/scratch/get-physics-done/paper6-cartan-tetrad-prompt.md`.

### Verdict Ladder (decidable conditions)

| Stage | Decidable condition | Verdict |
| ----- | ------------------- | ------- |
| Phase A (75) | `dim π_u(V_{1/2}(16)) ≠ 4`, OR Gram signature not Lorentzian (1,3), OR 4d reduction needs an arbitrary choice | **KILL** — route dead, STOP |
| Phase A.5 (76) | matter-sourced `F_B` EM-shaped (traceless `~F²`) / support disjoint from `T[M]` / no M-power match — reproduces the cone-Hessian same-wall mismatch | **SOFT KILL** — recommend STOP before B |
| Phase B (77) | A & A.5 survive; `F=dA+A∧A` Lorentz block = 4d Riemann (Totaro/Levi-Civita-cross-checked ≥5 components), V_{1/2}-sourced | **SURVIVES** — connection-curvature gravity, distinct from the dead metric route |
| Phase C (78) | trace-form-invariant quadratic-in-F contraction space is 1-dim AND equals the ε-contraction with a cubic-norm-fixed normalization | **STRONG WIN** — gravity from h_3(O) Lie-sector geometry, non-circular |
| Phase C (78) | Einstein term appears only because an MM/EH action was posited by hand | **`fp-imported-action`** — honest partial, NOT a derivation |

### Contract Overview

Machine-readable contract: `.gpd/state.json` field `project_contract` (schema v1, set 2026-06-01). 4 claims, 5 deliverables, 12 acceptance tests, 15 references, 8 forbidden proxies.

| Contract Item | Advanced By Phase(s) | Status |
| ------------- | -------------------- | ------ |
| **claim-coframe-reduction** (THE KILL GATE) | Phase 74 (anchors ✓), Phase 75 (decisive ✓) | ✓ **SURVIVES** (2026-06-02): (E_11,u) forces a 4d Lorentzian (1,3) coframe carrying SO(3,1); 3/3 clauses exact over Q; verified HIGH; human-ratified |
| **claim-berry-same-wall** (SOFT KILL) | Phase 76 | Planned |
| **claim-cartan-gravity** | Phase 77 | Planned |
| **claim-forced-einstein** | Phase 78 | Planned |
| deliv-phase0 | Phase 74 | ✓ Done (2026-06-02) |
| deliv-phaseA | Phase 75 | ✓ Done (2026-06-02) |
| deliv-phaseA5 | Phase 76 | Planned |
| deliv-phaseB | Phase 77 | Planned |
| deliv-phaseC | Phase 78 | Planned |
| test-tangent-identity, test-calibration | Phase 74 | ✓ Done (2026-06-02) |
| test-coframe-dim, test-coframe-signature, test-coframe-forced | Phase 75 | ✓ Done (2026-06-02) |
| test-berry-real-part, test-berry-vacuum, test-berry-shape | Phase 76 | Planned |
| test-coframe-invertible, test-cartan-curvature, test-vacuum-einstein | Phase 77 | Planned |
| test-forced-vs-posited | Phase 78 | Planned |

### Phase Dependencies

| Phase | Depends On | Enables | Gate | Critical Path? |
| ----- | ---------- | ------- | ---- | :-: |
| 74 — Phase 0: Engine, Tangent Identity & Calibration | — | 75, 76 | — | Yes |
| 75 — Phase A: Coframe-Reduction Dealbreaker | 74 | 77 (greenlight) | **KILL gate** | Yes |
| 76 — Phase A.5: Berry-Curvature Same-Wall | 74 | 77 (greenlight) | **SOFT KILL gate** | Yes |
| 77 — Phase B: Full Cartan Curvature = 4d Gravity | 74, **75 survives**, **76 survives** | 78 | — | Yes |
| 78 — Phase C: Circularity Audit (forced vs posited) | 77 | — | — | Yes |

**Critical path:** 74 → {75, 76} → 77 → 78. The gates are *conjunctive*: BOTH Phase 75 (A) and Phase 76 (A.5) must SURVIVE to greenlight Phase 77 (B); a KILL at 75 or a SOFT KILL at 76 ends the milestone as a complete, publishable closure (later phases are NOT mandatory).
**Parallelizable:** Phases 75 (A) and 76 (A.5) have **no inter-dependency** — both depend only on Phase 74, both are cheap (linear algebra over Q / canonical curvature needing no metric-compatibility equation), and may be planned and executed in parallel. The `Re(QGT)=cone-Hessian` consistency anchor (Phase 76) is the single check that licenses the whole "imaginary part" framing — front-load it.

### Phases

**Phase Numbering:** Integer phases (74–78) are planned research work (continuing across milestones from v17.0's Phase 73 — numbering never restarts). Decimal phases (e.g. 75.1) are urgent insertions, marked INSERTED.

- [x] **Phase 74: Phase 0 — Engine Recovery, Tangent Identity & Calibration** *(completed 2026-06-02)* — reload the det SSOT, verify `E_11∘δ=(1/2)δ` and `T_{E_11}OP^2=V_{1/2}(16)`, reproduce the calibration anchors + K=−1/2 benchmark. **VERDICT: foundation certified** — det SSOT re-passes (324/324 = dim f_4 52, octonion_algebra.py absent); soldering form dE confirmed V_{1/2}-valued (kernel == span{11..26}); all anchors + K=−1/2 reproduced byte-for-byte; verified 9/9 HIGH.
- [x] **Phase 75: Phase A — Coframe-Reduction Dealbreaker (THE KILL GATE, do first; cheap)** *(completed 2026-06-02)* — exact image dim of `π_u(V_{1/2}(16))`, exact Gram signature, forced-vs-arbitrary structure group. **VERDICT: SURVIVES** — (E_11,u) forces a 4d Lorentzian (1,3) coframe carrying SO(3,1): dim π_u(V_{1/2})=4 (survivors {11,18,19,26}=C_u²); soldering-form metric (1,3) + B rank 4 (bare trace-form diag(2,2,2,2)=(4,0) reported as the Euclidean OP² FS foil, NOT the verdict); residual 21=so(3,1)[6]⊕so(6)[15], so(3,1) FORCED (the so(6) a trivial-on-spacetime ideal, res/so(6)=so(3,1)). Human-ratified + orchestrator-reproduced; verified HIGH. Greenlight Phase 77 (conjunctive with Phase 76).
- [ ] **Phase 76: Phase A.5 — Berry-Curvature Same-Wall Gate (SOFT KILL)** — Im(QGT) well-definedness after C_u breaking, `Re(QGT)=Hess(−log det)` anchor, M=0 vacuum, Einstein-vs-EM shape.
- [ ] **Phase 77: Phase B — Full Cartan Curvature = 4d Gravity (only if A and A.5 survive)** — invertible coframe, Spin(3,1) connection ω, `F=dA+A∧A` Lorentz block = 4d Riemann, vacuum + matter-sourced.
- [ ] **Phase 78: Phase C — Circularity Audit (forced vs posited)** — is the MM ε-contraction FORCED by the h_3(O) trace-form/cubic-norm, or `fp-imported-action`?

## Phase Details

### Phase 74: Phase 0 — Engine Recovery, Tangent Identity & Calibration

**Goal:** The computational foundation is re-certified and the load-bearing geometric fact — that the soldering form `dE` is `V_{1/2}`-valued — is established exactly, BEFORE any geometry is built on it.
**Depends on:** Nothing (entry point; inherits the v17.0 engine).
**Requirements:** DERV-01, DERV-02, VALD-01
**Contract Coverage:**
- Advances: `claim-coframe-reduction` (supplies its two consistency anchors `test-tangent-identity`, `test-calibration`).
- Deliverable: `deliv-phase0` (derivation + supporting exact-SymPy code) — det SSOT re-passing CH + 324/324; exact `E_11∘δ=(1/2)δ` and `dim T_{E_11}OP^2 = 16`; reproduced calibration anchors.
- Anchors / benchmarks: det SSOT `code/ring_lemma_verification.py` det_3 (324/324 inner-derivation annihilation = dim f_4 52); `code/orbit_dimension_gate.py` calibration anchors (single-copy 24 / Spin(8)=28 / trdeg 3; e_6=78=52+26; orbit(E_11)=17; Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1)); H^3 cone-Hessian sign benchmark K=−1/2. Refs: Baez 2002 (OP^2=F_4/Spin(9), T_E OP^2=V_{1/2}), McCrimmon (`E∘δ=(1/2)δ`).
- Prior outputs reused: `code/bulk_geometry_verification.py:peirce_indices_under_E11` and `code/embedding_under_E_verification.py` for Peirce-under-E_11 (NOTE: `code/peirce_coupling.py` cited in the prompt does NOT exist — use these instead or build Peirce-under-E_11 fresh).
- Forbidden proxies to avoid: `fp-octonion-algebra` (octonion_algebra.py BANNED on any decisive path); `fp-float-decisive` (sympy.Matrix.rank only, never numpy).
**Success Criteria** (what must be TRUE):

1. The det SSOT `ring_lemma_verification.py` det_3 re-passes Cayley-Hamilton + 324/324 inner-derivation annihilation (= dim f_4 = 52), engine ALL_PASS (exit 0); a source guard confirms `octonion_algebra.py` is NOT imported on the decisive path.
2. `E_11∘δ = (1/2)δ` holds exactly over Q for a full basis of `δ ∈ V_{1/2}(E_11)`, and the tangent space to the primitive-idempotent variety at `E_11` is exactly `V_{1/2}(E_11)`, of dimension 16.
3. The calibration anchors are reproduced exactly via `orbit_dimension_gate.py` (single-copy dim 24 / Spin(8)=28 / trdeg 3; e_6=78=52+26; orbit(E_11)=17; Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1)).
4. The H^3 cone-Hessian sign benchmark K=−1/2 is re-passed (sign conventions pinned BEFORE any curvature verdict downstream).

**Plans:** 1 plan (1 wave)

Plans:

- [x] 74-01-PLAN.md — DERV-01 (det SSOT re-pass: CH + 324/324 + source guard) + DERV-02 (exact E_11∘δ=(1/2)δ and Zariski tangent T_{E_11}OP²=V_{1/2}(16), kernel==span(V_HALF_IDX)) + VALD-01 (calibration anchors 24/28/3, 78, 17, 61, 45 + K=−1/2 across the three engines) — ✓ COMPLETE 2026-06-02 (verified 9/9 HIGH; exact over Q)

### Phase 75: Phase A — Coframe-Reduction Dealbreaker (THE KILL GATE)

**Goal:** It is decided, exactly over Q, whether `(E_11,u)` ALONE reduces the 16-dim `V_{1/2}` soldering form to a 4-dim Lorentzian coframe carrying SO(3,1) — a decisive greenlight or a flat KILL of the whole route.
**Depends on:** Phase 74 (the verified `V_{1/2}`-valued soldering form and the det SSOT).
**Requirements:** CALC-01, CALC-02, VALD-02
**Contract Coverage:**
- Advances: `claim-coframe-reduction` (THE KILL GATE) — decisively.
- Deliverable: `deliv-phaseA` — exact image dimension of `π_u(V_{1/2}(16))`, exact Gram-eigenvalue signature, forced-vs-arbitrary residual-structure-group analysis, with a DECISIVE 4d-Lorentzian-and-forced verdict OR a flat KILL.
- Acceptance tests: `test-coframe-dim` (image dim — exactly 4 or KILL), `test-coframe-signature` (Lorentzian (1,3) or KILL), `test-coframe-forced` (SO(3,1) forced by `(E_11,u)` or KILL = `fp-arbitrary-reduction`).
- Anchors / benchmarks: the validated `V_0 = h_2(O) → h_2(C_u) ≅ R^{3,1}` reduction (Minkowski (1,3)) from `derivations/52-kkt-spacetime.tex` + `52-observer-uniqueness.tex` — the same Phase-46 `π_u` `C_u` bottleneck REUSED for `V_{1/2}`. Refs: Baez 2002, McCrimmon, Sharpe 1997 (soldering forms).
- Forbidden proxies to avoid: **`fp-arbitrary-reduction`** (a 4d coframe obtained by ANY choice not forced by `(E_11,u)` — "4" must be EARNED, not assumed by analogy to V_0); `fp-relabel-approx-4d` (never relabel a non-4d/non-Lorentzian reduction "approximately 4d"); `fp-float-decisive` (rank/signature involve cancellations — sympy.Matrix.rank only).
**Success Criteria** (what must be TRUE):

1. The exact image dimension over Q of `π_u(V_{1/2}(16))` under the `C_u`/Phase-46 bottleneck is computed and reported as a decidable integer — **exactly 4 (greenlight) or ≠ 4 (KILL)**, with the reduction made explicit (no softening).
2. The induced coframe Gram pairing has its exact eigenvalues over Q computed and its signature read off — **Lorentzian (1,3) / mostly-minus (greenlight) or non-Lorentzian (KILL)**.
3. The residual structure group preserving the reduced coframe is determined over Q, and it is decided whether it contains SO(3,1) **FORCED by `(E_11,u)` alone (greenlight)** or whether the 4d reduction requires an arbitrary extra choice (**KILL = `fp-arbitrary-reduction`**).
4. If any clause fails (not 4-dim / not Lorentzian / not forced): an explicit "Phase A: coframe reduction fails [clause]" KILL is reported flat and the route STOPS (a clean, publishable closure).

**Plans:** 1 plan (1 wave)

Plans:

- [x] 75-01-PLAN.md -- C_u reduction of V_{1/2}: CALC-01 exact image dim (KILL if !=4) + image(B)==pi_u(V_0) identity; CALC-02 soldering-form-metric signature (1,3) on the R^{3,1} target + Euclidean trace-form foil diag(2,2,2,2) (KILL if not Lorentzian / B not rank 4); VALD-02 forced-vs-arbitrary SO(3,1) residual group over QQ (KILL = fp-arbitrary-reduction); verdict synthesis -> deliv-phaseA (interactive: human ratification of the KILL/greenlight) — ✓ COMPLETE 2026-06-02 (VERDICT: SURVIVES; all 3 clauses exact over Q; verified 1/1 claim + 3/3 tests HIGH; human-ratified + orchestrator-reproduced)

### Phase 76: Phase A.5 — Berry-Curvature Same-Wall Gate (SOFT KILL)

**Goal:** It is decided, cheaply and before any expensive connection machinery, whether the canonical Berry curvature `F_B = Im(QGT)` has Einstein-shaped matter content — or whether the Lie sector inherits the v17.0 cone-Hessian same-wall mismatch (a SOFT KILL).
**Depends on:** Phase 74. (Independent of Phase 75 — may be planned/run in parallel; canonical/tautological Berry curvature needs no metric-compatibility equation.)
**Requirements:** CALC-03, VALD-03, CALC-04, VALD-04
**Contract Coverage:**
- Advances: `claim-berry-same-wall` (the SOFT KILL gate).
- Deliverable: `deliv-phaseA5` — `F_B` as Im(QGT); the real-part consistency check; the M=0 vacuum level; the matter-sourced tensor shape (Einstein-vs-EM); the same-wall comparison to the v17.0 cone-Hessian mismatch.
- Acceptance tests: `test-berry-real-part` (Re(QGT) is a real symmetric metric of the same non-Einstein character as the cone-Hessian — SOFT sanity check, NOT a hard stop; FS pullback vs cone-Hessian restriction, discrepancy informative), `test-berry-vacuum` (M=0 vacuum level: flat / pure-Λ / other), `test-berry-shape` (Einstein-shaped → SURVIVES to B, or EM-shaped reproducing the cone-Hessian mismatch → SOFT KILL).
- Survey-added checkpoints (fold in): **(VALD-03) well-definedness FIRST** — establish that `Im(QGT)=F_B` is a well-defined, generically-NONZERO 2-form on the 4d slice AFTER the C_u breaking, since OP^2=F_4/Spin(9) is isotropy-irreducible / not Hermitian-symmetric and carries NO invariant 2-form (a nonzero Berry 2-form must be *born from the breaking*), BEFORE testing its shape; **(CALC-03) the `Re(QGT)` ≈ cone-Hessian consistency anchor is a SOFT sanity check** — `Re(QGT)` is the Fubini-Study pullback along `E(x)` (a different construction than the v17.0 cone-Hessian restriction), so it should be of the same non-Einstein CHARACTER but a discrepancy is INFORMATIVE (diagnose), NOT a KILL/HALT on this anchor alone.
- Anchors / benchmarks: Provost-Vallée 1980 (QGT real=Fubini-Study / imaginary=Berry); the `Re(QGT)=cone-Hessian` consistency anchor against the v17.0 `code/bulk_geometry_verification.py`; the v17.0 Ph73 same-wall lesson (a tensor appearing ≠ Einstein; `κT~10³ < G`; support must match). Refs: Provost-Vallée, Wise gr-qc/0611154, Faraut-Koranyi (cone-Hessian, for the real-part check only).
- Forbidden proxies to avoid: **`fp-relabel`** (an EM-shaped `~F²`/traceless/conformal field strength relabeled "Einstein" without an independently-frozen `T[M]` matched in magnitude, tensor structure, AND M-power); the non-abelian-gauge mistake (the degenerate `V_{1/2}` eigenbundle is Wilczek-Zee non-abelian Berry — gauge-COVARIANT not invariant; decisive verdicts must rest on gauge-invariant scalars / traces / Wilson loops, tested under a frame rotation); `fp-reuse-cone-hessian` (the cone-Hessian is the real-part consistency check ONLY, never load-bearing for the imaginary-part verdict).
**Success Criteria** (what must be TRUE):

1. The QGT of the idempotent state family `|ψ(x)⟩` at `E(x)` is computed in gauge-invariant projector form `Q = Tr(P ∂P ∂P)` over Q(i), and its **real part is a sensible real symmetric metric of the SAME non-Einstein CHARACTER as the v17.0 cone-Hessian** — a **SOFT sanity check** (`Re(QGT)` is the Fubini-Study pullback along `E(x)`, a DIFFERENT construction than the cone-Hessian restriction on the V_0 slice, so a discrepancy is INFORMATIVE; diagnose why before proceeding). **Do NOT KILL or HALT on this anchor alone.**
2. `Im(QGT)=F_B` is established to be a well-defined, generically-nonzero 2-form on the 4d slice *after* the C_u breaking (the OP^2-not-Kähler well-definedness checkpoint) — confirmed before any shape test.
3. `F_B` at `M=0` is classified exactly: zero/flat, pure-Λ (`F_B ~ e∧e`), or other (vacuum level reported; expected flat/pure-Λ per CONVENTIONS §6; **Λ<0 is NOT reintroduced**).
4. With `M ∈ V_{1/2}` turned on, the matter-sourced `F_B` (and the ε-contraction of `F_B∧F_B` onto the Lorentz block) is decided to be **transverse/Einstein-shaped — order, tensor structure, and support matchable to an independently-frozen `V_{1/2}` stress-energy `T[M]` (SURVIVES to B)** — or **EM-shaped (traceless `T^μ_μ=0`, `~F²`) reproducing the v17.0 cone-Hessian mismatch (support disjoint from `T[M]`, no M-power match → SOFT KILL, recommend STOP before B)**, using gauge-invariant scalars.

**Plans:** TBD

Plans:

- [ ] 76-01: TBD (QGT real-part anchor + Im(QGT) well-definedness + vacuum + Einstein-vs-EM same-wall)

### Phase 77: Phase B — Full Cartan Curvature = 4d Gravity

**Goal:** The assembled (A)dS Cartan connection `A=ω⊕e` and its curvature `F=dA+A∧A` are computed, and the Lorentz block is identified — with an independent cross-check — as the 4d Riemann tensor, with its vacuum and matter-sourced structure characterized.
**Depends on:** Phase 74; **conditional on Phase 75 (A) SURVIVING and Phase 76 (A.5) SURVIVING.** (If either gate KILLs/SOFT-KILLs, this phase does not run.)
**Requirements:** DERV-03, DERV-04, CALC-05, VALD-05
**Contract Coverage:**
- Advances: `claim-cartan-gravity`.
- Deliverable: `deliv-phaseB` — invertible coframe; Spin(3,1) connection ω; `F=dA+A∧A` with Lorentz block = 4d Riemann (Totaro/Levi-Civita cross-check); torsion block; M=0 Einstein/(A)dS level; matter-sourced Riemann.
- Acceptance tests: `test-coframe-invertible` (`det(e^a_μ)≠0`), `test-cartan-curvature` (Lorentz block matches independent Totaro/Levi-Civita Riemann on ≥5 components exact over Q; torsion reported), `test-vacuum-einstein` (M=0 Einstein/(A)dS level + Λ sign MEASURED, sign-pinned by K=−1/2).
- Anchors / benchmarks: **H^3 sign benchmark K=−1/2** (fix conventions before any curvature verdict); the **in-repo Ph72/73 Totaro + hand-rolled Levi-Civita cross-check harness `code/bulk_geometry_verification.py`** (`totaro_riemann`, `hand_rolled_riemann_of_g`, `ricci_decomposition_n4`, `eig_signature_count`) for the ≥5-component Riemann cross-check; the expected vacuum is flat/pure-Λ per CONVENTIONS §6 (NOT the dead R×H³). Refs: MacDowell-Mansouri 1977, Wise gr-qc/0611154 (`A=ω+(1/ℓ)e`, `F=R[ω]−(Λ/3)e∧e+d_ω e`), Sharpe 1997.
- Forbidden proxies to avoid: **`fp-reuse-cone-hessian`** (do NOT reuse the v17.0 symmetric-sector / real-part Riemann as load-bearing — this is the antisymmetric/Lie sector, a different tensor; the cone-Hessian is for the real-part consistency check only); the raw-45-dim-Spin(9,1)-curvature mistake (Spin(9,1) is the AMBIENT group; gravity = the 10-dim `A=ω⊕e`, extract the Spin(3,1) Lorentz block — never the raw 45-dim curvature); `fp-float-decisive`.
**Success Criteria** (what must be TRUE):

1. `e = π_u(dE)` is confirmed a non-degenerate soldering form on the 4d slice: `det(e^a_μ) ≠ 0` exact over Q (a genuine invertible tetrad).
2. `ω` is extracted as the Lorentz Spin(3,1) part of the ambient Spin(9,1) connection compatible with `e` (metric/torsion condition or the canonical f_4/e_6 reductive split `g=h⊕m`) — NOT the raw 45-dim Spin(9,1) curvature.
3. `F = dA + A∧A` is computed symbolically; its Lorentz block `R(ω)+Λe∧e` is identified with the 4d Riemann tensor and **cross-checked against an independent Totaro/Levi-Civita computation on ≥5 components, agreeing exactly over Q**; the translation/torsion block `de+ω∧e` is reported (vanishing or matter-sourced).
4. At M=0 the Lorentz block's Einstein/(A)dS level is read against the K=−1/2 benchmark and Λ's sign/value is reported as MEASURED (expected flat/pure-Λ, NOT the dead R×H³); then with `M ∈ V_{1/2}` on, the matter-sourced Riemann is characterized.

**Plans:** TBD

Plans:

- [ ] 77-01: TBD (coframe invertibility + ω extraction)
- [ ] 77-02: TBD (F=dA+A∧A + Riemann cross-check + vacuum + matter-sourced)

### Phase 78: Phase C — Circularity Audit (forced vs posited)

**Goal:** The decisive non-circularity question is settled: is the MM ε-contraction (hence the Einstein term) FORCED by the intrinsic h_3(O) trace-form/cubic-norm, or does it only appear because an MM/EH action was posited by hand?
**Depends on:** Phase 77 (B) — the assembled connection and its `F∧F` structure.
**Requirements:** VALD-06
**Contract Coverage:**
- Advances: `claim-forced-einstein`.
- Deliverable: `deliv-phaseC` — an explicit determination of whether the Spin(9,1)→SO(3,1) breaking and the ε-tensor are fixed by the h_3(O) trace form / cubic norm; the honest final verdict at true strength.
- Acceptance test: `test-forced-vs-posited` (FORCED by the trace-form/cubic-norm → STRONG WIN, or only via a posited MM action → `fp-imported-action`, honest partial; reported at true strength, not relabeled a win).
- Survey-added concreteness (fold in): the forced-vs-posited test is **concrete** — the space of **trace-form-invariant quadratic-in-F contractions must be 1-DIMENSIONAL AND equal the ε-contraction with a cubic-norm-fixed normalization** (STRONG WIN), else `fp-imported-action`. Do NOT structure the phase to "confirm Einstein"; frame Singh / Castro / GST (which all posit an action) as the explicit contrast class.
- Anchors / refs: MacDowell-Mansouri 1977 and Wise gr-qc/0611154 (the ε-contraction `B^{ab}=ε^{abcd}e_c∧e_d` breaks SO(4,1)→SO(3,1) BY HAND — the precise circularity locus); GST 1983-84 geometry as the in-program contrast (the `fp-imported-action` precedent — "the −R/2 is the assumed N=2 multiplet's own output").
- Forbidden proxies to avoid: **`fp-imported-action`** (declaring Einstein structure that only appears because an MM/EH action was posited — the GST sin in new clothes — is the central risk and the most likely real outcome; do NOT cite the MM action as the source); `fp-reuse-cone-hessian`; `fp-float-decisive`.
**Success Criteria** (what must be TRUE):

1. It is explicitly determined whether the Spin(9,1)→SO(3,1) symmetry breaking and the ε-tensor that turn `F∧F` into Einstein-Hilbert+Λ are FIXED by the h_3(O) trace form / cubic-norm pairing, or are an external MM choice imported by hand.
2. The concrete test is run: the dimension of the trace-form-invariant quadratic-in-F contraction space is computed (== 1 AND == the ε-contraction with a cubic-norm-fixed normalization ⇒ **FORCED / STRONG WIN**; otherwise **POSITED**).
3. If the Einstein term only appears via a posited MM action, it is reported as **`fp-imported-action`** (honest partial, NOT a derivation); Singh/Castro/GST are framed as the contrast class.
4. The honest final milestone verdict (KILL / SOFT KILL / SURVIVES / STRONG WIN / `fp-imported-action`) is stated at true strength — neither inflated to a win nor softened.

**Plans:** TBD

Plans:

- [ ] 78-01: TBD (forced-vs-posited: trace-form quadratic-in-F contraction dimension vs ε-contraction)

## Backtracking Triggers

Research backtracking is expected; these are the explicit conditions for revisiting earlier work, and the STOP conditions that end the milestone as a publishable closure (NEGATIVE-RESULT-IS-SUCCESS).

- **Phase 75 (A) — KILL / STOP:** the `C_u` reduction does NOT land on a 4-dim space, OR the coframe is NOT Lorentzian, OR the 4d reduction is NOT forced by `(E_11,u)` (requires an arbitrary extra choice). → Report "Phase A: coframe reduction fails [clause]" and STOP. Do NOT relabel "approximately 4d". Phases 76–78 do not become mandatory.
- **Phase 76 (A.5) — SOFT KILL / STOP:** the canonical Berry curvature `F_B` reproduces the cone-Hessian same-wall mismatch (curvature support disjoint from the `V_{1/2}` stress-energy support; no order-matching possible). → Report "Phase A.5: Lie sector inherits the symmetric-sector mismatch" and recommend STOP before Phase B.
- **Phase 76 (A.5) — SOFT sanity check (NOT a stop):** if the real part of the QGT differs from the v17.0 `Hess(−log det)`, that is INFORMATIVE, not a bug — `Re(QGT)` is the Fubini-Study pullback along `E(x)`, a DIFFERENT construction than the cone-Hessian restriction on the V_0 slice; diagnose the geometric difference before proceeding. Do NOT KILL or HALT on this anchor alone. (The genuine A.5 SOFT KILL is the matter-sourced same-wall mismatch vs `T[M]`, below.)
- **Any phase — arithmetic-hygiene STOP:** `octonion_algebra.py` detected on a decisive path, OR a float rank/curvature on a decisive verdict → STOP and switch to the det SSOT `ring_lemma_verification.py` det_3 / exact-over-Q (`fp-octonion-algebra`, `fp-float-decisive`).
- **Phase 78 (C) — honest-partial, not a win:** the Einstein term appears ONLY because an MM/EH action was posited by hand → report `fp-imported-action` (the GST sin in new clothes); do NOT relabel it a win. This (B yes, C no) is the most likely real outcome.
- **Roadmap-level:** if Phase 75 or 76 KILLs, the milestone is COMPLETE at that gate (a clean publishable negative). Do not pad with speculative later phases. If a decisive computation proves infeasible, return DESIGN BLOCKED to the executor orchestrator (which may re-invoke the roadmapper).

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
| ----- | -------- | :-: | :-: | ---------- |
| 74 | Peirce-under-E_11 machinery (`peirce_coupling.py`) absent | RESOLVED | LOW | Reuse `bulk_geometry_verification.py:peirce_indices_under_E11` / `embedding_under_E_verification.py`, or build fresh; contract reference corrected |
| 75 | `(E_11,u)` does NOT force a 4d Lorentzian reduction — "4" smuggled by analogy to V_0 | MEDIUM | HIGH | The KILL gate itself: exact image dim + Gram signature + forced-vs-arbitrary, decided over Q; KILL flat if not forced (`fp-arbitrary-reduction`) |
| 76 | OP^2 carries no invariant 2-form ⇒ `Im(QGT)` ill-defined | MEDIUM | HIGH | Well-definedness checkpoint (VALD-03) FIRST: confirm `F_B` born from the C_u breaking is a nonzero 2-form before any shape test |
| 76 | Lie sector inherits the symmetric-sector same-wall mismatch | MEDIUM-HIGH | HIGH | SOFT KILL gate: matter-sourced `F_B` vs independently-frozen `T[M]` at matched M-power/structure/support; gauge-invariant scalars (Wilczek-Zee covariance) |
| 77 | Reusing the dead cone-Hessian Riemann; mistaking raw 45-dim Spin(9,1) curvature for 4d gravity | MEDIUM | HIGH | Independent Totaro/Levi-Civita cross-check on ≥5 components; extract the Spin(3,1) block only; `fp-reuse-cone-hessian` flagged |
| 78 | `fp-imported-action` — Einstein only via a posited MM action (the GST sin) | HIGH | HIGH (decisive) | Concrete forced-vs-posited test (1-dim trace-form contraction space == ε-contraction?); report at true strength; the most likely real outcome, reported honestly |

## Progress

**Execution Order:** Phases execute in numeric order with the conjunctive gate: 74 → {75, 76 in parallel} → [STOP if KILL/SOFT-KILL] → 77 → 78.

| Phase | Milestone | Plans Complete | Status | Completed |
| ----- | --------- | -------------- | ------ | --------- |
| 74. Phase 0 — Engine, Tangent Identity & Calibration | v18.0 | 1/1 | ✓ Complete | 2026-06-02 |
| 75. Phase A — Coframe-Reduction Dealbreaker (KILL) | v18.0 | 1/1 | ✓ Complete (SURVIVES) | 2026-06-02 |
| 76. Phase A.5 — Berry-Curvature Same-Wall (SOFT KILL) | v18.0 | 0/TBD | Not started | - |
| 77. Phase B — Full Cartan Curvature = 4d Gravity | v18.0 | 0/TBD | Not started | - |
| 78. Phase C — Circularity Audit (forced vs posited) | v18.0 | 0/TBD | Not started | - |

**Coverage:** 15/15 objectives mapped (DERV ×4, CALC ×5, VALD ×6) — no orphans, no duplicates. All 4 contract claims, 5 deliverables, and 12 acceptance tests surfaced. All 8 forbidden proxies visible at the phases where they bite.

---

_v18.0 roadmap created 2026-06-01 (gpd-roadmapper). Physics-side; INDEPENDENT of the consciousness-side (RING/REDUCIBILITY) line — do not entangle. Prior milestone roadmaps and requirements live under `.gpd/milestones/`. Phase numbering continues across milestones (never restarts). Machine-readable contract: `.gpd/state.json` field `project_contract`._
