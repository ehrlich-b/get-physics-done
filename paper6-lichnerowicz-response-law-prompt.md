# Slot 92 / v32.0-candidate — The Tensor Dictionary: Does the TT Sector Close in Canonical Form?

**RATIFIED-BY-STANDING-DIRECTIVE. Run AFTER the v31.0 ratification and
close-out are pasted and committed — this prompt CONSUMES the close-out's
TEST-2 artifacts (the explicit λ=12 (1,1) TT multiplet basis).**

**Milestone type (declared honestly at registration): EXTRACTION-leaning
(v25/v26 class), with ONE genuine factual sub-fork (Gate 2's threshold
number) and one dictionary-closure question (Gate 3/4) whose LIVE bar is
pre-registered below. This is NOT a v27/v31-class genuine fork — do not
present it as one.**

**Calibration (binding, from the 2026-06-12 steelman — the prompt embeds it
so the run cannot re-inflate):** v31 established EXISTENCE of the TT residue,
which was the less-informative branch (generic-position DOF counting
predicted it). v32's bar for LIVE is strictly higher: a FORCED closed form —
the geometry telling matter exactly how much TT it gets, in the certified
dictionary, with no free function and no fitted constant. Anything short of
that is more kinematics and must be reported as such. "First selection-shaped
tensor statement" language is permitted ONLY if Gate 4's LIVE criteria are
met verbatim. Paper 5 remains the only result in the more-than-nothing
column.

---

## 1. The question

v31 proved (ratified): on the cut CP² = h₃(C_u), the matter stress bilinear
B3 = dφ_M⊗dφ_M (= B6) has a nonzero TT residue, dim 1 per matter direction,
in the λ=12 (1,1)-Hermitian Boucetta dim-8 multiplet, with the count forced
by Sym²(8) = 27⊕8⊕1 ⊃ 8 (multiplicity one).

Multiplicity one means the equivariant map M ↦ TT(B3) factors through the
UNIQUE symmetric equivariant projection Sym²(8) → 8 — the d-symbol. So the
TT mode's closed form is rep-theoretically PINNED up to one scalar function
of the invariants. v32 extracts the whole dictionary exactly:

- **(i) The TT closed form.** TT(B3) = Σᵢ cᵢ(M)·tᵢ over the explicit dim-8
  TT basis {tᵢ}, with the NAMED HYPOTHESIS (verify, do not assume): the
  coefficient vector points along N(M) = the traceless adjoint square of M
  (the d-symbol square; in Jordan language the traceless(M∘M)-direction).
- **(ii) The norm identity — the v27-sequel candidate and the verdict
  center.** ‖TT(B3)‖² as a closed form in the FROZEN v27 tuple
  (a, c, c_R, TrM², detM) with constants forced by the geometry. v27's law
  was c_R(1−c_R)λ² = −|π_{1/2}M|²·G_M; the question is whether the tensor
  sector closes the same way.
- **(iii) The threshold number (the genuine sub-fork).** ε = λ_L − 2Λ
  measured IN-REP on the multiplet, where λ_L is the actual Lichnerowicz
  eigenvalue under the frozen convention and Λ = 6 (Ric = 6g, certified).
  This resolves the standing trap-#16 tension factually: Boucetta's table
  puts the multiplet AT eigenvalue 12 = 2Λ, while infinitesimal Einstein
  deformations are ker(Δ_L − 2Λ)|_TT (Besse 12.28) and CP^n is Koiso-RIGID
  (Besse 12.98) — so either the table's normalization differs from the
  Besse convention as realized by OUR certified connection, or the
  multiplet is formally marginal and rigidity lives at second order.
  COMPUTE it; do not adjudicate from the literature. NO prior is registered
  on ε — both outcomes are informative and both are consumed by the
  lapse/00 assembly later.
- **(iv) The full York dictionary.** The gauge potential ω and conformal f
  of B3 in certified closed form (the reduction B3 = ½∇∇(φ²) − φ∇∇φ makes
  ½d(φ²) the natural seed for ω — verify and complete it), so that
  B3 = TT + δ*ω + f·g is exhibited entirely in closed form.

## 2. Setup (all certified, reuse — do not rebuild)

- The v31 machinery: `code/tensor_probe.py` (FS chart, exact metric/inverse,
  certified Christoffels, cov_hessian, δ*, conformal block, york_solve,
  the dimension-audit tooling) and `code/tensor_probe_indep_check.py`
  (independent geometry + general_york_solve at D with kw/kf powers).
- The v31 close-out's TEST-2 artifacts: the explicit (1,1) TT basis {tᵢ}
  with committed in-rep verification δtᵢ = 0, tr tᵢ = 0. If the close-out
  delivered only a single tᵢ for the sparse direction, construct the full
  dim-8 basis at Gate 0 by su(3) rotation of that element (equivariance) and
  re-verify each.
- Certified fields: φ_M = ⟨M,p⟩ (v25), G_M (v26), R_M with cut
  (α,β,λ₂) = (2/5, 3/20, 32), χ (v30, rational realization per 91-GATE-2),
  s_M = dφ_M (v28), the v27 tuple and law.
- Spectral anchors (cross-checks only, never inputs): λ₁ = 12, λ₂ = 32,
  Λ = 6, κ₀ = 9/4 on the cut; Boucetta Tables VI–VIII at n=2 as staged in
  `derivations/91-tensor-probe-RESEARCH.md` §4.

**The frozen Δ_L convention (state at Gate 0 and never vary):**
Δ_L h = ∇*∇h + Ric∘h + h∘Ric − 2R̊h, with ∇*∇ the rough Laplacian from the
certified connection and (R̊h)_{ab} = R_{acbd}h^{cd} from the certified
curvature. Every operator is BUILT in-rep; external eigenvalues are
cross-checks.

## 3. Gates

**Gate 0 — machinery + freeze.** Load/construct the dim-8 basis; re-verify
δtᵢ = 0, tr tᵢ = 0 in-rep (symbolically or at off-slice rational points).
Build Δ_L per the frozen convention. FREEZE the four verdict objects
(i)–(iv) and the LIVE criteria of Gate 4. No post-hoc verdict objects — any
addition after Gate 0 is a new run.

**Gate 1 — controls (zero evidential weight).** (a) verdict() non-hardwired
self-test. (b) Vacuum M = 0: every object ≡ 0. (c) Δ_L on f·g for a λ₁
eigenfunction f: known answer through the certified scalar Δ (report the
identity used). (d) Δ_L on the gauge tensor δ*(dφ_Y): known answer via the
commutation of Δ_L with δ* (Δ_L δ*ω = δ*Δ_H ω on an Einstein background —
verify the identity IN-REP on the certified objects before using it; if it
fails, the convention bookkeeping is wrong — STOP). (e) Scalar regressions:
λ₁ = 12, λ₂ = 32 reproduced through the tensor-machinery code path.
(f) **The Schur check (mandatory):** equivariance + multiplicity-one force
Δ_L to act as a SCALAR on the dim-8 multiplet — compute Δ_L tᵢ for at least
two independent basis elements and verify proportionality to tᵢ with the
SAME constant. Deviation = engine bug, STOP (do not reinterpret as physics).

**Gate 2 — the threshold number (the genuine sub-fork; report, both
branches informative).** λ_L = the Schur scalar from Gate 1(f), computed
exactly over Q. Report ε = λ_L − 2Λ = λ_L − 12. If ε = 0: the multiplet is
formally Einstein-marginal under the frozen convention; record the
Koiso-rigidity reconciliation as SECOND-ORDER (obstruction-theoretic) and
fence any Fredholm/response reading per trap #19. If ε ≠ 0: the multiplet
is non-marginal; ε is canonical response-stiffness data for the lapse/00
assembly. Either way: ONE exact rational number, with the
Boucetta-table-vs-Besse-convention discrepancy (if any) explained
mechanically (which term, which sign, which normalization).

**Gate 3 — the closed form (the verdict center).** All in the fast
matched-monomial representation; control-gated at degrees where the B1
control passes (D = 3 for dense/symbolic matter — the v31 close-out
lesson).
- (3a) Extended solve B3 = Σ cᵢ tᵢ + δ*ω + f·g over (cᵢ, ω, f): sparse s01,
  both dense matters, then SYMBOLIC 8-parameter M. Consistency with some
  cᵢ ≠ 0 is forced by ratified v31 — if the extended solve is inconsistent
  or all-zero for generic M, that CONTRADICTS the ratified result: STOP and
  report (do not paper over).
- (3b) The direction hypothesis: verify c(M) ∝ the N(M) = adjoint-square
  direction (compute N(M) explicitly from the su(3) d-symbol or the Jordan
  product; compare the 8-vectors exactly). Report PASS/FAIL — a FAIL is a
  finding, not a failure (the unique-projection argument then needs
  re-examination: check the (1,1)-projection step).
- (3c) The norm identity: ‖TT(B3)‖² = ‖Σ cᵢ tᵢ‖² as a polynomial in the
  frozen tuple — fit over the certified invariant basis with EXACT
  coefficients, verify symbolically with residual ≡ 0 through the full
  symbolic M (the v27 standard: no locus constraint, identical constants in
  all sectors). detM kept in the ansatz (v27 found it absent — finding
  either way).
- (3d) The ω and f closed forms: complete the dictionary; verify the
  reconstruction B3 − Σ cᵢtᵢ − δ*ω − f·g ≡ 0 symbolically.

**Gate 4 — verdict (frozen criteria).**
- **LIVE ⟺ (3a) consistent for symbolic M AND (3c) closes with FORCED exact
  constants over the frozen tuple (residual ≡ 0, no fitted/free function).**
  Then and only then the sentence "the tensor sector closes in the canonical
  dictionary — the program's first forced tensor-response coefficient" is
  licensed, with the fences of §5 verbatim.
- **PARTIAL (informative): (3a) closes but (3c) requires invariants OUTSIDE
  the frozen tuple.** Report WHICH new invariant the closure demands — the
  dictionary's first incompleteness is a finding (it names the next object),
  not a failure. No LIVE language.
- **DEAD-equivalent here = contradiction with v31 (see Gate 3a STOP) or a
  Schur/identity failure — machinery, not physics; STOP rather than verdict.**

**Gate 5 — v33 ledger (priced only, NO claims, NO computation).**
(a) The lapse/00 assembly: consumes ε (Gate 2), c(M) (Gate 3), and the
scalar sector (v26/v27) into candidate 00/ij blocks — requires the 4d-slice
embedding question to be confronted; price it. (b) The OP² lift: Spin(9)
isotypic bookkeeping, no Kähler split, the (1,1) story does not transfer —
price, do not assume. (c) The Fredholm/response READING of ε (the
"(Δ_L − 2Λ)h = source" equation): this is a Block-C-shaped IMPORT — name it,
fence it, do not run it.

## 4. Traps (pre-registered; instances 17–19 of the designed-in-verdict bug
class)

- **#17 — eigen-tautology.** (Δ_L − λ_L)tᵢ ≡ 0 within the multiplet is
  KINEMATICS (Schur). Any "law" that reduces to it is vacuous. The verdict
  objects are the COEFFICIENTS (c, the norm identity, ε) — never the
  eigen-identity. The Gate-1 Schur check is a control, not a result.
- **#18 — convention skew.** Boucetta vs Besse vs the certified machinery
  can differ in Δ_L normalization, curvature-sign, and Λ bookkeeping. Every
  operator in this run is built from the certified connection; the
  literature numbers are cross-checks. The 12-vs-2Λ tension is resolved by
  Gate 2's computation, with the discrepancy mechanism named — never by
  picking the convenient convention.
- **#19 — the Einstein-import smuggle.** Writing a sourced response
  EQUATION ((Δ_L − 2Λ)h = κ·T_TT) imports the linearized Einstein form —
  that is Block C, where five routes died. v32 reports canonical identities
  and spectral data. The word "response" appears only in Gate-5 pricing,
  fenced.
- Standing guards: octonion product-order trap (re-verify any hand-derived
  d-symbol/Jordan-square against BOTH recorded product tables); generic
  matter only for verdicts (diagonal/co-diagonalization strata zero
  weight); control-gating (results cited only at degrees where B1 passes);
  exact arithmetic over Q throughout (no floats, no numerics); the v31
  language fences verbatim (no Einstein-equation / Newton-constant /
  G-equals-kappa-T / dark-matter / geodesic language; frozen FS geometry
  USED not derived; the MM corpse stays buried; OP² priced only).

## 5. Scope fence (binding, verbatim in every summary)

Whatever Gate 4 returns: this is the deformation-complex dictionary of a
FROZEN imported geometry. No dynamical metric. No selection law. No κ. The
constructed-vs-extremized gap, the 16-vs-6 rank wall, the Riemannian
signature, and the base/format clamp are untouched by construction. LIVE
means "the tensor sector's source data closes in canonical form" — a
dictionary fact, not a dynamics fact.

## 6. STOP rules

(1) Gate-1 identity or Schur failure → engine/convention bug — fix or halt;
never reinterpret. (2) Gate-3a inconsistency or all-zero c for generic M →
contradicts ratified v31 — halt, report, do not self-amend the v31 record.
(3) Any verdict object not frozen at Gate 0 → not a verdict (new run).
(4) Engine disagreement (executor vs independent check) → halt at the
disagreeing check.

## 7. Deliverables

`derivations/92-tensor-dictionary-RESEARCH.md` (grounding §1–6, results
§7–9 incl. the v33 ledger); `derivations/92-GATE-{0..4}-SUMMARY.md`;
`derivations/92-VERDICT.md`; `code/lichnerowicz_response.py` (executor);
`code/lichnerowicz_response_verify.py` (independent path — at minimum the
Schur scalar and the norm identity through a separate code path);
third-path adversarial check per v30/v31 parity. List in the VERDICT only
what actually ran (the v30/v31 lesson — nothing "expected").

## NEXT

HOLD the v32.0 milestone bookkeeping for ratification (mirroring v25–v31).
The v33 prompt (whichever Gate-5 item is elevated) comes from blog-side —
do not self-register.
