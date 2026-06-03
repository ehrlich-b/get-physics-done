# Research Roadmap: Experiential Measure on Structure Space

Deriving the fundamental laws of physics from the algebraic structure of self-modeling composite processes. See `.gpd/PROJECT.md` for the full program narrative and `.gpd/MILESTONES.md` for shipped-milestone records.

## Milestones

- **v1.0–v13.0** — Phases 1–53 (archived under `.gpd/milestones/`)
- **v14.0 Paper 5 Revision** — Phases 54–59 (PAUSED 2026-04-17, pending JMP referee report; see `.gpd/V14-CLOSEOUT.md`)
- **v15.0 The P5 ↔ Basin Restriction Lemma** — Phases 60–63 (completed 2026-05-24 — CHARACTERIZED OBSTRUCTION / coexistence-as-island; through-line survives)
- **v16.0 The (RING) Lemma** — Phases 64–69 (completed 2026-05-27 — (RING) (a)+(b)+(c) PROVED)
- **v17.0 Gravity as Intrinsic Curvature of the h_3(O) Bulk Geometry** — Phases 70–73 (completed 2026-06-01 — **NONE: curved but not Einstein-structured**; the REAL part / cone-Hessian / Jordan sector)
- **v18.0 Gravity as the Curvature of the Peirce-Frame (Cartan/MacDowell-Mansouri) Connection on h_3(O)** — Phases 74–78 (**COMPLETE 2026-06-02 — `fp-imported-action`: a curved, matter-sourced, position-dependent Lorentzian slice carrying a forced SO(3,1) coframe, but NOT Einstein gravity without a posited action**; the antisymmetric/Lie **connection** sector. Gravity = the soldering-form Riemann `R[ω]` = the Lorentz block of `F=dA+A∧A`. NOTE 2026-06-02: the Berry curvature `Im(QGT)` is a *distinct internal gauge* object, NOT gravity — Phase 76 reframed; see the disposition note below. NEXT = `/gpd:complete-milestone`.)

---

## Active Milestone: v18.0 — Gravity as the Curvature of the Peirce-Frame (Cartan/MM) Connection on h_3(O)

### Overview

This milestone computes the **antisymmetric/Lie-sector** gravitational object every prior route in the program ignored: the curvature 2-form `F = dA + A∧A` of the Peirce-frame Cartan/MacDowell-Mansouri connection `A = ω⊕e` on h_3(O), equivalently the **Berry curvature = imaginary part of the quantum geometric tensor (QGT)** of the rank-1 primitive-idempotent state family. The dead v17.0 cone-Hessian route computed the QGT's **real part** (Fubini-Study metric) and returned NONE; Provost-Vallée (1980) is the load-bearing justification that NONE binds only `Re(Q)`, leaving the imaginary part — a genuinely different tensor — untouched. The question is decided by two **cheap KILL gates first**: Phase A (does the `C_u` bottleneck reduce the 16-dim `V_{1/2}` soldering form `e=dE` to a 4-dim Lorentzian coframe carrying SO(3,1), *forced* by `(E_11,u)`?) and Phase A.5 (is the canonical Berry curvature Einstein-shaped, or does it inherit the v17.0 cone-Hessian same-wall mismatch?), which gate the expensive full Cartan assembly (Phase B) and the forced-vs-posited circularity audit (Phase C). Everything decisive is **exact over Q** (the Berry sector over Q(i), Re/Im split); the det SSOT is `code/ring_lemma_verification.py` det_3; `octonion_algebra.py` is BANNED.

> **Scope = GR (the Lorentz Spin(3,1) block).** This milestone tests whether the connection yields 4d **Einstein gravity** — not the Standard Model. The same ambient Spin(9,1) connection also carries a Spin(6)=SU(4) internal block (Pati-Salam, Phase 48); IF the GR test passes, the gauge-connection / SM-unification angle is a flagged **BONUS for a later milestone, NOT a v18.0 deliverable**. Paper 7 already HOUSES the SM rep (derive→house discipline); this milestone does not attempt to derive it.

> **NEGATIVE-RESULT-IS-SUCCESS (binding reporting discipline).** A clean Phase A KILL (no forced 4d Lorentzian coframe) or a Phase A.5 same-wall SOFT KILL is a **full, publishable closure** — report it flat, never relabel "approximately 4d" or "approximately Einstein". The **most likely real outcome** is a forced coframe but an imported action (B yes, C no): report that as `fp-imported-action`, an honest partial, NOT a win. The point is to find out whether gravity is the Lie-sector connection curvature of h_3(O), not to confirm it. Authoritative spec: `~/scratch/get-physics-done/paper6-cartan-tetrad-prompt.md`.

> **⚠ DISPOSITION UPDATE (2026-06-02) — Phase 76 (A.5) verdict OVERTURNED; milestone re-scoped.** Phase 76 computed the Berry curvature `F_B = Im(QGT)` and proposed a SOFT KILL; Bryan OVERTURNED it — **A.5 tested the wrong object.** The Maxwell stress and the Pontryagin `F_B∧F_B` are *quadratic* in `F_B`; the Einstein–Hilbert object is `ε_{abcd} R^{ab}∧e^c∧e^d`, **linear** in the Riemann `R[ω]` and wedged with the tetrad. "A 2-form's Maxwell stress is traceless in 4d" is a universal tautology that also kills *real* GR ⟹ the discriminant is invalid for gravity. **Corrected framing:** the Berry curvature is the **internal `U(k)` / `so(6)=SU(4)` gauge** sector (a deferred SM-unification bonus, NOT a v18.0 deliverable); **gravity is the soldering-form Riemann `R[ω]`** = the Lorentz block of `F = dA + A∧A`, built from `e = π_u(dE)` (Phase 75). **Consequences:**
> 1. The A.5 result does NOT gate gravity — **Phase 75 (SURVIVES) alone greenlights Phase B.** The "75 ∧ 76 conjunctive" gate is **RETIRED**.
> 2. Cheap pre-check DONE (`76-precheck`, exact over Q): `g = e·e` is `(1,3)` Lorentzian = the v17.0 η baseline, **DIFFERENT** from the `(4,0)` cone-Hessian. Base-metric coincidence ≠ Riemann redundancy (different curvature mechanism: soldering/Cartan `ω(e)` vs cone-Hessian cross-terms) ⟹ **Phase B is a genuine, non-redundant test.**
> 3. **Phase 77 (B) now OPENS with a flatness gate** (the v18.0 analog of the v17.0 homogeneity dealbreaker): build `g = e·e` for a sample `M ≠ 0`, compute `R[ω(e)]`, confirm it is **NONZERO** BEFORE any `G = κT[M]` comparison. The `M=0` vacuum `g=e·e=η` is correctly flat; if `R[ω] = 0` for `M ≠ 0` (rigid / integrable soldering, pure-gauge), the route yields no gravity — **honest trivial death, STOP there.** Only if `R[ω] ≠ 0` proceed to `ω(e) → R[ω] → G` vs the independently-frozen `T[M]` with the v17.0-Ph73 power-counting discipline.

### Verdict Ladder (decidable conditions)

| Stage | Decidable condition | Verdict |
| ----- | ------------------- | ------- |
| Phase A (75) | `dim π_u(V_{1/2}(16)) ≠ 4`, OR Gram signature not Lorentzian (1,3), OR 4d reduction needs an arbitrary choice | **KILL** — route dead, STOP |
| Phase A.5 (76) | ~~matter-sourced `F_B` EM-shaped → SOFT KILL~~ **RETIRED AS A GATE (overturned 2026-06-02, see disposition above): A.5 tested the wrong object — `F_B` is the internal `so(6)=SU(4)` gauge curvature, not gravity; the traceless-`~F²` discriminant is a tautology that also kills real GR** | **does NOT gate B** |
| Phase B (77) — flatness sub-gate | build `g=e·e` for `M≠0`; `R[ω(e)] = 0` (rigid/integrable soldering) | **trivial death** — no gravity, STOP |
| Phase B (77) | Phase 75 survives; flatness sub-gate passes (`R[ω]≠0` for `M≠0`); `F=dA+A∧A` Lorentz block = 4d Riemann (Totaro/Levi-Civita-cross-checked ≥5 components), V_{1/2}-sourced | **SURVIVES** — connection-curvature gravity, distinct from the dead metric route |
| Phase C (78) | trace-form-invariant quadratic-in-F contraction space is 1-dim AND equals the ε-contraction with a cubic-norm-fixed normalization | **STRONG WIN** — gravity from h_3(O) Lie-sector geometry, non-circular |
| Phase C (78) | Einstein term appears only because an MM/EH action was posited by hand | **`fp-imported-action`** — honest partial, NOT a derivation |

### Contract Overview

Machine-readable contract: `.gpd/state.json` field `project_contract` (schema v1, set 2026-06-01). 4 claims, 5 deliverables, 12 acceptance tests, 15 references, 8 forbidden proxies.

| Contract Item | Advanced By Phase(s) | Status |
| ------------- | -------------------- | ------ |
| **claim-coframe-reduction** (THE KILL GATE) | Phase 74 (anchors ✓), Phase 75 (decisive ✓) | ✓ **SURVIVES** (2026-06-02): (E_11,u) forces a 4d Lorentzian (1,3) coframe carrying SO(3,1); 3/3 clauses exact over Q; verified HIGH; human-ratified |
| **claim-berry-same-wall** (~~SOFT KILL gate~~ RETIRED) | Phase 76 | ⚠ **Reinterpreted 2026-06-02** — A.5 tested the wrong object (`F_B` = internal `so(6)=SU(4)` gauge curvature, not gravity). SOFT KILL overturned; does NOT gate Phase B. |
| **claim-cartan-gravity** | Phase 77 | ⚠ **Phase B partial / NEGATIVE** (2026-06-02): `R[ω]` of `g=e·e` is a genuine matter-sourced 4d curvature (6/6-component independent Levi-Civita cross-check exact over Q, torsion=0); M=0 vacuum flat (Λ=0 measured); but `G[g]` is **NOT** Einstein-form `κT+Λg` for any single global `(κ,Λ)` vs an AST-guarded order-matched `T[M]` (per-point Λ varies; 180-eq solve inconsistent; support 16 vs 6; both T candidates; t⁴ order-match satisfied) → **`fp-imported-action` partial**. Human-ratified; verified passed 4/4, HIGH |
| **claim-forced-einstein** | Phase 78 | ✓ **Resolved — `fp-imported-action`** (2026-06-02, human-ratified): the MM ε-contraction is **NOT forced** by the h_3(O) trace form `Tr(X∘Y)` / cubic norm `det_3`. Decisive triple (exact over Q): bare so(3,1)-invariant quad-curvature 4-form space already dim=2 (Euler+Pontryagin, triple-route); ε reachable only via the orientation-ambiguous metric volume form `√|det η| ε`; `det_3 ≡ 0` identically on the soldered Lorentz block [1,2,3,10] ⇒ normalization free/imported. STRONG-WIN fails all three clauses; Λ=0 ⇒ εF∧F is topological Gauss-Bonnet (a 2nd independent argument). Verified HIGH; consistency CONSISTENT |
| deliv-phase0 | Phase 74 | ✓ Done (2026-06-02) |
| deliv-phaseA | Phase 75 | ✓ Done (2026-06-02) |
| deliv-phaseA5 | Phase 76 | Executed (retired as a gate) |
| deliv-phaseB | Phase 77 | ✓ Done (2026-06-02) |
| deliv-phaseC | Phase 78 | ✓ Done (2026-06-02) |
| test-tangent-identity, test-calibration | Phase 74 | ✓ Done (2026-06-02) |
| test-coframe-dim, test-coframe-signature, test-coframe-forced | Phase 75 | ✓ Done (2026-06-02) |
| test-berry-real-part, test-berry-vacuum, test-berry-shape | Phase 76 | Executed (gate retired) |
| test-flatness-gate, test-coframe-invertible, test-cartan-curvature, test-vacuum-einstein | Phase 77 | ✓ Done (2026-06-02) |
| test-forced-vs-posited | Phase 78 | ✓ Done (2026-06-02) — decisively determined forced-vs-posited = **POSITED** (passing ≠ STRONG WIN) |

### Phase Dependencies

| Phase | Depends On | Enables | Gate | Critical Path? |
| ----- | ---------- | ------- | ---- | :-: |
| 74 — Phase 0: Engine, Tangent Identity & Calibration | — | 75, 76 | — | Yes |
| 75 — Phase A: Coframe-Reduction Dealbreaker | 74 | 77 (greenlight) | **KILL gate** | Yes |
| 76 — Phase A.5: Berry-Curvature Same-Wall | 74 | 77 (greenlight) | **SOFT KILL gate** | Yes |
| 77 — Phase B: Full Cartan Curvature = 4d Gravity | 74, **75 survives** (76 RETIRED as a gate, 2026-06-02) | 78 | **flatness sub-gate** (opens Phase B) | Yes |
| 78 — Phase C: Circularity Audit (forced vs posited) | 77 | — | — | Yes |

**Critical path (updated 2026-06-02):** 74 → 75 → 77 → 78. The "75 ∧ 76 conjunctive gate" is **RETIRED**: Phase 76 (A.5) was overturned as a gravity gate (it tested the Berry / internal-gauge sector, not the tetrad Riemann). **Phase 75 (A, SURVIVES) alone greenlights Phase B (77).** Phase 77 opens with its own **flatness sub-gate** (`R[ω]≠0` for `M≠0`); failure there is an honest trivial death (the v18.0 analog of the v17.0 homogeneity dealbreaker). A KILL at 75 (it survived) or the flatness sub-gate ends the milestone as a publishable closure.
**Historical note:** Phases 75 (A) and 76 (A.5) were originally planned as parallel cheap gates with no inter-dependency. Phase 76's premise (Berry curvature = the gravity object) proved wrong; its computation is preserved as an internal-gauge-sector observation (deferred SM bonus).

### Phases

**Phase Numbering:** Integer phases (74–78) are planned research work (continuing across milestones from v17.0's Phase 73 — numbering never restarts). Decimal phases (e.g. 75.1) are urgent insertions, marked INSERTED.

- [x] **Phase 74: Phase 0 — Engine Recovery, Tangent Identity & Calibration** *(completed 2026-06-02)* — reload the det SSOT, verify `E_11∘δ=(1/2)δ` and `T_{E_11}OP^2=V_{1/2}(16)`, reproduce the calibration anchors + K=−1/2 benchmark. **VERDICT: foundation certified** — det SSOT re-passes (324/324 = dim f_4 52, octonion_algebra.py absent); soldering form dE confirmed V_{1/2}-valued (kernel == span{11..26}); all anchors + K=−1/2 reproduced byte-for-byte; verified 9/9 HIGH.
- [x] **Phase 75: Phase A — Coframe-Reduction Dealbreaker (THE KILL GATE, do first; cheap)** *(completed 2026-06-02)* — exact image dim of `π_u(V_{1/2}(16))`, exact Gram signature, forced-vs-arbitrary structure group. **VERDICT: SURVIVES** — (E_11,u) forces a 4d Lorentzian (1,3) coframe carrying SO(3,1): dim π_u(V_{1/2})=4 (survivors {11,18,19,26}=C_u²); soldering-form metric (1,3) + B rank 4 (bare trace-form diag(2,2,2,2)=(4,0) reported as the Euclidean OP² FS foil, NOT the verdict); residual 21=so(3,1)[6]⊕so(6)[15], so(3,1) FORCED (the so(6) a trivial-on-spacetime ideal, res/so(6)=so(3,1)). Human-ratified + orchestrator-reproduced; verified HIGH. Greenlight Phase 77 (conjunctive with Phase 76).
- [x] **Phase 76: Phase A.5 — Berry-Curvature (RETIRED as a gravity gate)** *(executed 2026-06-02; SOFT-KILL verdict OVERTURNED)* — computed `F_B=Im(QGT)` (well-definedness born-from-breaking, M=0 pure-Λ/Kähler vacuum `F_B=−2ω_K`, matter-on EM-shape). The SOFT KILL was overturned: A.5 tested the **wrong object**. `F_B` is the **internal `so(6)=SU(4)` gauge curvature**, not the tetrad Riemann; it does NOT gate gravity (preserved as a deferred SM bonus). See the disposition note above.
- [x] **Phase 77: Phase B — Full Cartan Curvature = 4d Gravity** *(completed 2026-06-02)* — flatness sub-gate PROCEED (`R[ω]≠0` for `M≠0`, 136/256 nonzero exact/Q; M=0 baseline flat); invertible coframe `det(e)≠0` sig (1,3); closed-form torsion-free `ω(e)`; `F=dA+A∧A` Lorentz block = 4d Riemann (6/6-component independent Levi-Civita cross-check exact/Q); M=0 vacuum flat, Λ=0 measured. **VERDICT: NEGATIVE / `fp-imported-action` partial** — `G[g]` is NOT Einstein-form `κT+Λg` for any single global `(κ,Λ)` vs an AST-guarded order-matched `T[M]` (two-axis failure: global-Λ inconsistency + tensor support 16-vs-6; both T candidates; t⁴ order-match satisfied → structural, not a near-miss). A curved, matter-sourced, position-dependent Lorentzian slice that is NOT Einstein-structured without a posited action. Mirrors v17.0 Ph73 NONE on a DIFFERENT tensor (antisymmetric/Lie `R[ω]` vs symmetric/real cone-Hessian) ⇒ an INDEPENDENT negative; v17.0 NONE does not bind it. Human-ratified; verified passed 4/4 HIGH; consistency CONSISTENT.
- [x] **Phase 78: Phase C — Circularity Audit (forced vs posited)** *(completed 2026-06-02)* — **VERDICT: `fp-imported-action`** (human-ratified by Bryan). The MM ε-contraction (hence the Einstein term) is **NOT forced** by the intrinsic h_3(O) trace form `Tr(X∘Y)` / cubic norm `det_3`. Decisive computation exact over Q: (T1) det_3 SSOT re-passes + `Tr(X∘Y)|frame == η=diag(+1,−1,−1,−1)` (the bare Jordan trace Gram diag(1,1,2,2)=(4,0) is the OP² Fubini–Study FOIL) + AST/source input-ban guard passes (and catches an injected violation, not a no-op); (T2) bare so(3,1)-invariant quad-curvature 4-form space = **dim 2** (Euler + Pontryagin), triple-route confirmed; (T3) the decisive triple — dim(trace-form-invariant subspace) = 1 (η-tensorial, Pontryagin) / 2 (with volume form, +ε); ε reachable **only** via the orientation-ambiguous metric volume form `√|det η| ε` (not singled out); `det_3 ≡ 0` **identically** on the soldered Lorentz block [1,2,3,10] (couples x₁ to α, outside the block) ⇒ normalization **free/imported**. The deterministic, non-hardwired `verdict()` maps this to `fp-imported-action` (STRONG-WIN fails all three clauses). **Λ=0 corollary** (2nd independent argument): at the Phase-77-MEASURED Λ=0 vacuum, εF∧F → εR∧R = pure Gauss-Bonnet/Euler (topological, no EOM, no GR). GST/Singh/Castro framed as the imported-action contrast class (each imports its action; the h_3(O) exceptional-structure escape hatch is CLOSED). Verified passed 1/1 + 9/9 physics checks INDEPENDENTLY confirmed, HIGH (verifier re-derived det_3≡0-on-block via a different code path + rebuilt dim=2 with its own generators + proved verdict() non-hardwired + driver re-ran 3× byte-identical); consistency CONSISTENT. **Combined v18.0 verdict (Phase 77 dynamical NEGATIVE + Phase 78 tensor/action NEGATIVE):** a curved, matter-sourced, position-dependent Lorentzian slice with a forced SO(3,1) coframe, but NOT Einstein gravity without a posited action. Closes claim-forced-einstein and milestone v18.0.

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

### Phase 76: Phase A.5 — Berry-Curvature (RETIRED as a gravity gate)

> **DISPOSITION (2026-06-02):** Executed (76-01 vacuum + 76-02 matter, both committed, driver 43/43 PASS exact over Q(i), orchestrator-reproduced). The proposed SOFT KILL was **OVERTURNED** by Bryan: A.5 tested the **wrong object** — the Maxwell stress and Pontryagin `F_B∧F_B` are *quadratic* in `F_B`, whereas the Einstein–Hilbert object `ε_{abcd}R^{ab}∧e^c∧e^d` is *linear* in `R[ω]` wedged with the tetrad; and "a 2-form's Maxwell stress is traceless in 4d" is a universal tautology that also kills real GR. **`F_B = Im(QGT)` is the internal `so(6)=SU(4)` gauge curvature, NOT gravity** (preserved as a deferred SM-unification bonus). A.5 does NOT gate Phase B; **Phase 75 (SURVIVES) alone greenlights Phase B**, which now opens with a flatness sub-gate. The original SOFT-KILL goal and success criteria below are retained for the record but are **SUPERSEDED**.

**Goal (SUPERSEDED — see disposition):** It is decided, cheaply and before any expensive connection machinery, whether the canonical Berry curvature `F_B = Im(QGT)` has Einstein-shaped matter content — or whether the Lie sector inherits the v17.0 cone-Hessian same-wall mismatch (a SOFT KILL).
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

**Plans:** 2 plans (2 waves)

Plans:

- [ ] 76-01-PLAN.md — PART 1 (cheap/vacuum, non-interactive): QGT recipe + CP¹ convention pin; VALD-03 (Im(QGT)=F_B well-defined + generically nonzero, born-from-breaking) FIRST; CALC-03 (SOFT Re(QGT)=FS-metric same-character anchor vs cone-Hessian — informative, NOT a KILL); CALC-04 (M=0 vacuum: flat / pure-Λ-Kähler / other). Fixes the vacuum baseline.
- [ ] 76-02-PLAN.md — PART 2 (decisive/matter, **interactive**, depends_on 76-01): the matter-on E(x;M) over C_u (rank-1 + C_u-faithful + M→0 limit — the biggest modeling gap, its own verified task); VALD-04 decisive same-wall (matter F_B M-series + F_B∧F_B Lorentz-block ε-contraction vs an INDEPENDENTLY-FROZEN T[M], on gauge-invariant scalars, frame-rotation tested) → SURVIVES or SOFT KILL; blocking human-ratification of the milestone-gating verdict (conjunctive with Phase 75 ✓ for the Phase-77 greenlight).

### Phase 77: Phase B — Full Cartan Curvature = 4d Gravity

**Goal:** The assembled (A)dS Cartan connection `A=ω⊕e` and its curvature `F=dA+A∧A` are computed, and the Lorentz block is identified — with an independent cross-check — as the 4d Riemann tensor, with its vacuum and matter-sourced structure characterized. **Phase B OPENS with a flatness sub-gate (added 2026-06-02, the v18.0 analog of the v17.0 homogeneity dealbreaker):** build `g=e·e` for a sample `M≠0`, compute `R[ω(e)]`, and confirm it is NONZERO before any `G=κT[M]` comparison. The `M=0` vacuum `g=e·e=η` is correctly flat (76-precheck); if `R[ω]=0` for `M≠0` (rigid / integrable soldering, pure-gauge), the route yields no gravity — honest trivial death, STOP. Only if `R[ω]≠0` proceed.
**Depends on:** Phase 74 and **Phase 75 (A) SURVIVING** (which it does). *(Updated 2026-06-02: the Phase 76 / A.5 SURVIVING condition is REMOVED — A.5 was retired as a gravity gate, see the disposition note above. Phase 75 alone greenlights this phase.)*
**Requirements:** DERV-03, DERV-04, CALC-05, VALD-05
**Contract Coverage:**
- Advances: `claim-cartan-gravity`.
- Deliverable: `deliv-phaseB` — invertible coframe; Spin(3,1) connection ω; `F=dA+A∧A` with Lorentz block = 4d Riemann (Totaro/Levi-Civita cross-check); torsion block; M=0 Einstein/(A)dS level; matter-sourced Riemann.
- Acceptance tests: `test-coframe-invertible` (`det(e^a_μ)≠0`), `test-cartan-curvature` (Lorentz block matches independent Totaro/Levi-Civita Riemann on ≥5 components exact over Q; torsion reported), `test-vacuum-einstein` (M=0 Einstein/(A)dS level + Λ sign MEASURED, sign-pinned by K=−1/2).
- Anchors / benchmarks: **H^3 sign benchmark K=−1/2** (fix conventions before any curvature verdict); the **in-repo Ph72/73 Totaro + hand-rolled Levi-Civita cross-check harness `code/bulk_geometry_verification.py`** (`totaro_riemann`, `hand_rolled_riemann_of_g`, `ricci_decomposition_n4`, `eig_signature_count`) for the ≥5-component Riemann cross-check; the expected vacuum is flat/pure-Λ per CONVENTIONS §6 (NOT the dead R×H³). Refs: MacDowell-Mansouri 1977, Wise gr-qc/0611154 (`A=ω+(1/ℓ)e`, `F=R[ω]−(Λ/3)e∧e+d_ω e`), Sharpe 1997.
- Forbidden proxies to avoid: **`fp-reuse-cone-hessian`** (do NOT reuse the v17.0 symmetric-sector / real-part Riemann as load-bearing — this is the antisymmetric/Lie sector, a different tensor; the cone-Hessian is for the real-part consistency check only); the raw-45-dim-Spin(9,1)-curvature mistake (Spin(9,1) is the AMBIENT group; gravity = the 10-dim `A=ω⊕e`, extract the Spin(3,1) Lorentz block — never the raw 45-dim curvature); `fp-float-decisive`.
**Success Criteria** (what must be TRUE):

0. **(Flatness sub-gate — opens Phase B; added 2026-06-02; the v18.0 analog of the v17.0 homogeneity dealbreaker.)** `g=e·e` is built for a sample `M≠0` and `R[ω(e)] ≠ 0` is confirmed exact over Q BEFORE any `G=κT` comparison. (`M=0` ⟹ `g=e·e=η` flat, expected; `R[ω]=0` for `M≠0` ⟹ rigid/integrable soldering ⟹ no gravity ⟹ honest trivial death, STOP.)
1. `e = π_u(dE)` is confirmed a non-degenerate soldering form on the 4d slice: `det(e^a_μ) ≠ 0` exact over Q (a genuine invertible tetrad).
2. `ω` is extracted as the Lorentz Spin(3,1) part of the ambient Spin(9,1) connection compatible with `e` (metric/torsion condition or the canonical f_4/e_6 reductive split `g=h⊕m`) — NOT the raw 45-dim Spin(9,1) curvature.
3. `F = dA + A∧A` is computed symbolically; its Lorentz block `R(ω)+Λe∧e` is identified with the 4d Riemann tensor and **cross-checked against an independent Totaro/Levi-Civita computation on ≥5 components, agreeing exactly over Q**; the translation/torsion block `de+ω∧e` is reported (vanishing or matter-sourced).
4. At M=0 the Lorentz block's Einstein/(A)dS level is read against the K=−1/2 benchmark and Λ's sign/value is reported as MEASURED (expected flat/pure-Λ, NOT the dead R×H³); then with `M ∈ V_{1/2}` on, the matter-sourced Riemann is characterized.

**Plans:** 2 plans (2 waves)

Plans:

- [x] 77-01-PLAN.md (wave 1) — FLATNESS SUB-GATE + B(a) coframe non-degeneracy + B(b) closed-form Levi-Civita ω(e) — ✓ COMPLETE 2026-06-02 (**PROCEED**: R[ω]≠0 for M≠0, 136/256 nonzero exact/Q, Ricci scalar ≠0; M=0 baseline flat; det(e)=1/2 sig (1,3); ω(e) torsion-free antisymmetric sign-pinned K=−1/2; R[ω]==metric Levi-Civita Riemann identity verified. Tetrad via the contract-sanctioned Lagrange-congruence fallback over Q — π_u(dE) symbolic route hit the watchdog cliff; frame-invariant so verdict unaffected).
- [x] 77-02-PLAN.md (wave 2, depends_on 77-01, interactive) — B(c) F=dA+A∧A Lorentz/torsion split + ≥5-component independent Levi-Civita Riemann cross-check; B(d) M=0 vacuum + matter-sourcing Einstein test — ✓ COMPLETE 2026-06-02 (**VERDICT: NEGATIVE / `fp-imported-action` partial**, human-ratified; F=dA+A∧A torsion=0, Lorentz block == Levi-Civita Riemann of g=e·e on 6/6 components exact/Q; M=0 flat Λ=0 measured; G[g] NOT Einstein-form for any single global (κ,Λ) vs AST-guarded T[M] — two-axis failure, both T, t⁴ order-match satisfied; 18 sig-(1,3) family points, 0 dropped).

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

**Plans:** 2 plans (2 waves)

Plans:

- [x] 78-01-PLAN.md — the decisive forced-vs-posited computation (wave 1, non-interactive): det SSOT re-pass + Tr|frame==η + AST/source input-ban guard; the bare so(3,1)-invariant quadratic-in-curvature 4-form space dim=2 anchor (Euler + Pontryagin) exact over Q; THE decisive trace-form-invariant subspace dimension + ε-reachability + det_3-fixed-normalization read-off — ✓ COMPLETE 2026-06-02 (decisive triple: dim 1/2; ε-in-span YES only via the metric volume form; normalization free; det_3≡0 on the Lorentz block ⇒ input = fp-imported-action at true strength; driver 32/32 PASS exact over Q; commits 495303e0 + cf606563)
- [x] 78-02-PLAN.md — verdict synthesis + contrast + ratification (wave 2, depends_on 78-01, INTERACTIVE): map the decisive triple to the verdict ladder (STRONG WIN xor `fp-imported-action`) + Λ=0 corollary; GST/Singh/Castro imported-action contrast; the milestone-closing v18.0 derivation; **BLOCKING** human ratification of the milestone-headline verdict — ✓ COMPLETE 2026-06-02 (**VERDICT: `fp-imported-action`**, human-ratified by Bryan; deterministic non-hardwired verdict() ladder; Λ=0 Gauss-Bonnet corollary; GST/Singh/Castro contrast; v18.0 through-line; driver ALL_PASS/exit 0 reproduced; commits e51cc23e + 2bc1e322 + db3617bb)

## Backtracking Triggers

Research backtracking is expected; these are the explicit conditions for revisiting earlier work, and the STOP conditions that end the milestone as a publishable closure (NEGATIVE-RESULT-IS-SUCCESS).

- **Phase 75 (A) — KILL / STOP:** the `C_u` reduction does NOT land on a 4-dim space, OR the coframe is NOT Lorentzian, OR the 4d reduction is NOT forced by `(E_11,u)` (requires an arbitrary extra choice). → Report "Phase A: coframe reduction fails [clause]" and STOP. Do NOT relabel "approximately 4d". Phases 76–78 do not become mandatory.
- **Phase 76 (A.5) — RETIRED as a gate (2026-06-02):** the original SOFT-KILL trigger (matter `F_B` EM-shaped / support-disjoint from `T[M]`) is **VOID** — A.5 tested the wrong object (`F_B` = internal `so(6)=SU(4)` gauge curvature, not gravity; the traceless-Maxwell-stress discriminant is a tautology that also kills real GR). A.5 does NOT stop the route.
- **Phase 77 (B) — flatness sub-gate / trivial-death STOP (replaces the retired A.5 gate as the cheap pre-B kill):** if `R[ω(e)] = 0` for `M ≠ 0` (rigid / integrable soldering, pure-gauge), the soldering route yields no gravity → honest trivial death, STOP before the `G=κT[M]` comparison.
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

**Execution Order (updated 2026-06-02):** 74 ✓ → 75 ✓ (SURVIVES) → 77 ✓ (flatness sub-gate PROCEED `R[ω]≠0`; **verdict NEGATIVE / `fp-imported-action` partial** — curved + matter-sourced but not Einstein-without-an-action) → **78 ✓ (`fp-imported-action`, the final phase, COMPLETE)**. The 75∧76 conjunctive gate is RETIRED — Phase 75 (SURVIVES) alone greenlit 77; Phase 76 (A.5) was reinterpreted (Berry = internal gauge sector, not a gravity gate). Phase 78 (C — forced-vs-posited) decisively determined the ε-contraction is **POSITED, not forced**: combined with the Phase 77 dynamical NEGATIVE, **milestone v18.0 closes `fp-imported-action`** — a curved, matter-sourced, forced-SO(3,1)-coframe Lorentzian slice that is NOT Einstein gravity without a posited action. **All 5 phases complete → NEXT = `/gpd:complete-milestone`.**

| Phase | Milestone | Plans Complete | Status | Completed |
| ----- | --------- | -------------- | ------ | --------- |
| 74. Phase 0 — Engine, Tangent Identity & Calibration | v18.0 | 1/1 | ✓ Complete | 2026-06-02 |
| 75. Phase A — Coframe-Reduction Dealbreaker (KILL) | v18.0 | 1/1 | ✓ Complete (SURVIVES) | 2026-06-02 |
| 76. Phase A.5 — Berry-Curvature (RETIRED as a gravity gate) | v18.0 | 2/2 | ⚠ Reinterpreted (SOFT KILL overturned 2026-06-02) | 2026-06-02 |
| 77. Phase B — Full Cartan Curvature = 4d Gravity | v18.0 | 2/2 | ✓ Complete (**NEGATIVE / `fp-imported-action` partial**) | 2026-06-02 |
| 78. Phase C — Circularity Audit (forced vs posited) | v18.0 | 2/2 | ✓ Complete (**`fp-imported-action`**) | 2026-06-02 |

**Coverage:** 15/15 objectives mapped (DERV ×4, CALC ×5, VALD ×6) — no orphans, no duplicates. All 4 contract claims, 5 deliverables, and 12 acceptance tests surfaced. All 8 forbidden proxies visible at the phases where they bite.

---

_v18.0 roadmap created 2026-06-01 (gpd-roadmapper). Physics-side; INDEPENDENT of the consciousness-side (RING/REDUCIBILITY) line — do not entangle. Prior milestone roadmaps and requirements live under `.gpd/milestones/`. Phase numbering continues across milestones (never restarts). Machine-readable contract: `.gpd/state.json` field `project_contract`._
