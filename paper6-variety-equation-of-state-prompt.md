# GPD Prompt — The Constrained Balance: the Equation-of-State Fork (J5-on-the-variety, step 3)

**Slot 87 / v27.0-candidate. STATUS: RATIFIED-BY-STANDING-DIRECTIVE
(Bryan, 2026-06-11). Ready to run.**

_Context: v26.0 COMPLETE (commit cd7f579b). Certified assets this run
consumes: the moment doublet m = TrX − ⟨X,p⟩, q = ⟨X#,p⟩; the response
field G_M(p) = ⟨M#,p⟩ − ¼⟨M,p⟩² with δ²S = (9/2)G_M ε² and
G_M = −¼(face eigengap of C_pM)² ≤ 0; the canonical field equation with
λ₁ = 48 (OP²) / 12 (cut), λ₂ = 104 / 32; the sourced equation; the
tangent identification T_p(variety) = J_{1/2}(p) (16-dim; cut: 4-dim,
coords {11,18,19,26} at E_11); v24 Gate 3 (the matter landscape and the
canonical geometry are genuinely distinct structures). This run executes
the v26 Gate-5(a) fork: does the two-structure competition close into a
LOCAL balance law? "Equation of state" is Jacobson's phrase used as a
STRUCTURAL analogy only — the question here is pure exact algebra
(multiplier-locality), with no thermodynamic import, no horizons, no
G = κT._

_Discipline: v21–v26 pattern — executor + independent verifier (separate
code path), exact over Q / Q(t), fail-fast gates, controls with known
answers. No Newton constant, no Einstein claims, no dark-matter
language, no geodesic-motion language anywhere._

## Pre-read: milestone type (pre-registered)

**GENUINE FORK — the first fork-type run since v23.** Unlike v24–v26
(verification/extraction, expected PASS), this run has NO expected
verdict. Pre-registered honesty about the prior: a naive dimension count
leans DEAD (on-locus tuple-fibers are positive-dimensional), but the
stabilizer action is tuple- and λ-preserving and in the Tier-A sector
the count is EXACTLY MARGINAL (generic tuple-fiber dimension = generic
stabilizer-orbit dimension = 4), so **LIVE ⟺ the tuple-fibers are
precisely the stabilizer orbits** — dimension counting is inconclusive
and the elimination decides. Both branches are informative and their
consequences are pre-stated (claim D4). v23's fork discipline is the
template: a DEAD branch is a scope theorem, not a failure.

## The setup (verify every step; one fully hand-checked anchor)

**Gradients on the variety.** At a rank-1 idempotent p, the tangent
space is the Peirce space J_{1/2}(p), trace-form-orthogonal to
J_1 ⊕ J_0. For any fixed Y, the differential of φ_Y(p) = ⟨Y,p⟩ in a
tangent direction v ∈ J_{1/2}(p) is ⟨Y,v⟩ = ⟨π_{1/2}(Y), v⟩, so the
covector dφ_Y is represented by the Peirce projection π_{1/2}^{(p)}(Y).
Hence, exactly:

- dG_M(p) = π_{1/2}( M# − ½⟨M,p⟩·M )
- dc_R(p) = π_{1/2}( R ),  where c_R(p) = ⟨R,p⟩ for a reference rank-1
  idempotent R (the canonical coordinate; v24 Gate 3's c11 with
  R = E_11 generalized to movable R).

**The balance condition.** Extremize the entropy response G_M on level
sets of the canonical coordinate c_R. Critical points satisfy the
PARALLEL condition

> **π_{1/2}( M# − ½⟨M,p⟩·M ) = λ · π_{1/2}(R)**   (at p, as covectors)

with λ = the Lagrange multiplier. The condition is METRIC-FREE
(proportionality of covectors needs no inner product), so λ has no
hidden normalization. Verify the formula by a second path: d/dt of
G_M(p(t)) along the 16 recorded families must equal ⟨dG_M, ṗ(t)⟩.

**THE FORK QUESTION (frozen).** On the parallel locus (off the trivial
strata), is λ a state-universal function of the FROZEN local tuple

> **(a, c, c_R, TrM², detM),  a := ⟨M,p⟩, c := ⟨M#,p⟩**

— the same function for all matter M and all reference R? Why the tuple
is exactly this: the quadratic Peirce data of M at p is
tuple-determined (|π_{1/2}M|² = ½TrM² − a² + c, Tr C_pM = −a,
det₂C_pM = c for traceless M), so the fork lives at CUBIC order — the
octonion direction data v24 proved the landscape resolves. The mixed
alignment invariants (⟨π_{1/2}M, π_{1/2}R⟩-type) are NOT in the tuple:
whether the locus FORCES them given the tuple IS the fork.

**Hand-checked anchor (reproduce exactly over Q(t) before anything
else).** M₀ = F_12(1) + E_11 − E_33 ∈ h₃(R) (rows
[[1,1,0],[1,0,0],[0,0,−1]]; F_12(ω) = the Hermitian unit with
(1,2)-entry ω). Then M₀# = [[0,1,0],[1,−1,0],[0,0,−1]] (two ways:
cofactors, and X² − (TrX)X + σ₂(X)I with σ₂ = −2). Take p = E_11 and
R(t) = the real (1,0)-family idempotent (entries R_11 = c², R_12 = cs,
R_22 = s², c = (1−t²)/(1+t²), s = 2t/(1+t²)). Then:

- tuple: a = 1, c = 0, c_R = c², TrM² = 4, detM = 1;
- dG(E_11) = π(M₀#) − ½·1·π(M₀) = F_12(1) − ½F_12(1) = **½·F_12(1) ≠ 0**;
- dc_R(E_11) = cs·F_12(1);
- so E_11 is ON the locus for every t ∉ {0, ±1}, with
  **λ = 1/(2cs) = (1+t²)²/(4t(1−t²))**, i.e. λ² = 1/(4·c_R(1−c_R)):
  for THIS configuration λ is a function of c_R alone — note λ is
  RATIONAL in t but only ALGEBRAIC in the tuple (λ², not λ, is
  rational). LIVE therefore accepts F as a finitely-sheeted algebraic
  function: a polynomial relation P(λ; tuple) = 0 with the sheet fixed
  by recorded sign data, stated exactly.
- NEGATIVE anchor (locus is direction-sensitive): M_{e₁} =
  F_12(e₁) + E_11 − E_33 has the SAME tuple (a = 1, c = 0, TrM² = 4,
  detM = 1) but dG(E_11) = ½F_12(e₁) ∦ cs·F_12(1) — OFF the locus at
  E_11 against the real family. (It re-enters against the e₁-family,
  Spin(9)-equivariantly, with the SAME λ — stabilizer pairs are never
  certificates.)

**Wlog.** F₄ is transitive on the variety (Spin(9) = Stab(E_11)); the
cut's SU(3) is transitive on CP² (U(2) = Stab). So fix p = E_11
throughout; M and R stay symbolic. The tuple and λ are
stabilizer-invariant; the locus is stabilizer-covariant.

## Claims

**D1 — well-posedness (locus bookkeeping).** The parallel locus is
non-empty off the trivial strata (the anchor is the existence
certificate; confirm on a battery). Strata EXCLUDED from all fork
evidence: dc_R = 0 (the c_R-critical set: p = R and the polar locus),
dG_M = 0 (G-critical points — for eigenframe-aligned/diagonal M these
include E_11, per v24's critical-point tracking), and λ = 0. Record the
strata; they carry no verdict weight (vacuity guard — catches #7/#9 of
the trap class, institutionalized at design time).

**D2 — the multiplier machinery.** Reproduce the hand anchor exactly
over Q(t) (both dG formula paths). Then the invariant-rank check
(catch #8): along the locus, compute the Jacobian rank of the tuple map
(a, c, c_R, TrM², detM) at the anchor and on a battery — if the locus
forces a relation among the tuple coordinates, RECORD it and restate
the fork over the reduced tuple before proceeding (a finding, not a
failure).

**D3 — THE FORK (the verdict).** Decide, tier by tier: on the locus, is
λ a function of the tuple?

- **Tier A (decisive sector, symbolic): the u-complex sector.**
  M ∈ h₃(C_u) traceless (8 params), R in the cut CP² (affine chart,
  4 params; R-symbolic preferred — fallback: ≥ 3 generic rational R's,
  recorded as slices), p = E_11. The parallel condition on the 4-dim
  cut tangent = rank ≤ 1 of the 2×4 covector stack = vanishing 2×2
  minors. Eliminate: does the ideal force a polynomial relation
  P(λ; a, c, c_R, TrM², detM) = 0 determining λ (finitely many sheets)?
  YES → LIVE-in-sector (state P exactly; verify P on the anchor:
  4c_R(1−c_R)λ² = 1 must be its specialization or consequence).
  NO (λ free over the tuple on a positive-dimensional fiber) →
  DEAD-in-sector + extract an exact certificate pair (two rational
  on-locus points, same tuple, different λ).
- **Tier B (one-octonion-block sector, symbolic):** M = diagonal + a
  single off-diagonal octonion entry (~10 params), R against matching
  families; same elimination question on the full 16-dim tangent.
- **Tier C (full 26-param M on OP²):** exact instance battery (≥ 40
  rational on-locus instances spread across octonion directions; record
  (λ; tuple) rows) + targeted certificate solves: fix a rational tuple
  target (start from the anchor's (1, 0, c_R(t₀), 4, 1) at rational
  t₀), solve {locus ∧ tuple = target} from different branches, compare
  λ exactly. If Tiers A/B produced a closed-form P: VERIFY P symbolically
  on full-26 (verification ≪ discovery).

  Verdict rules: ONE exact certificate pair anywhere = **DEAD**
  globally. P exhibited AND verified symbolically through Tier C =
  **LIVE** (state F/P exactly). Neither = **OPEN-per-tier** (record
  exactly which tier is undecided and why — no silent promotion in
  either direction).

**D4 — the reading (conditional, fenced).** IF LIVE: the route's first
selection-shaped LOCAL law — on the locus, the second-order entropy
response trades against the canonical coordinate at a rate fixed by
local field values alone; still NOT Einstein, NOT a metric law, the
geometry still frozen, λ a multiplier not a coupling, no Newton
constant. IF DEAD: the scalar sector provably does NOT close into a
local balance — the closure data is the J_{1/2} direction data, so the
spinor-moment object p ↦ π_{1/2}^{(p)}(X) (= the tangent-valued matter
field, v26 Gate-5(b)) is FORCED as v28's object, not optional; record
the certificate pair as the scope theorem. Either way, state which
world we are in, in one sentence.

## Gates

- **Gate 0 — machinery regression (fail-fast).** v25 doublet identity +
  v26 anchors re-verified (M = diag(2,−1,−1): G(E_11) = 0,
  G(E_22) = −9/4); π_{1/2}^{(E_11)} = the row-1 off-diagonal block,
  matching tangent coords {11..26} (cut: {11,18,19,26}); the two dG
  paths (Peirce projection vs d/dt along families) agree on a battery.
- **Gate 1 — controls (known answers, zero evidential weight).**
  (i) diagonal M ⇒ dG(E_11) = 0 (eigenframe-critical stratum, as
  designed); (ii) M = 0 ⇒ everything vanishes; (iii) the M_{e₁}
  rotation exits the locus at E_11 against the real family (hand-derived
  ∦) and re-enters against the e₁-family with the same λ;
  (iv) a Spin(9)/U(2)-rotated pair gives identical λ (equivariance,
  zero-weight); (v) the anchor λ at two rational t values by direct
  component ratio, no solver.
- **Gate 2 — D1 + D2** (anchor exact; strata recorded; tuple-rank
  check).
- **Gate 3 — D3 Tier A** (the sector verdict, symbolic).
- **Gate 4 — D3 Tiers B/C + the global verdict + D4.**
- **Gate 5 — the v28 ledger (exploratory, non-blocking, NO claims).**
  Price: (b-continuation) the spinor-moment map p ↦ π_{1/2}^{(p)}(X) —
  well-definedness, U(1)/gluing covariance (v22 contact), what
  "matter forces the connection" would mean as an exact claim;
  (c) the claim-2 contact: K_face = −log ρ_face explicit in (m,q)
  (face eigenvalues ½ ± ½√(1 − 4q/m²)) — consumption note only.
- **STOP rule:** any broken step in the setup formulas (the dG
  representation, the anchor values) = a design hole = more informative
  than proceeding; report and STOP.

## Guards (pre-registered)

1. **Metric-free verdicts.** The parallel condition is covector
   proportionality; no |∇·| norms, induced metrics, or normalization
   choices anywhere in the verdict path (commentary only).
2. **Strata discipline.** λ-verdicts only on the open stratum
   (dc_R ≠ 0, dG ≠ 0); λ = 0 and critical points are recorded but are
   NOT fork evidence (the vacuity bug class, instances #1–#6 on
   record).
3. **Exactness.** Certificate pairs and P-verification over Q/Q(t)
   only; no float matching in any verdict computation.
4. **The tuple is FROZEN:** (a, c, c_R, TrM², detM). Do NOT add mixed
   invariants to rescue LIVE (that is the fork resolving DEAD in
   disguise); do NOT drop detM (fakes DEAD). If D2's rank check forces
   a tuple change, restate the fork explicitly and proceed with the
   reduced tuple, flagged.
5. **Sector honesty.** Tier verdicts are SECTOR verdicts. A certificate
   pair globalizes DEAD; only full-26 symbolic verification globalizes
   LIVE. State the scope of whatever is obtained.
6. **The octonion product-order trap (standing).** The conj(x₃x₂)-type
   adjugate entries — the exact spot flagged in v25/v26; require the
   independent implementations to agree on an octonionic battery BEFORE
   any verdict computation.
7. **Language fence.** No Einstein, no Newton constant, no G = κT, no
   dark matter, no geodesic-motion or force language; "equation of
   state" = multiplier-locality, nothing else; the canonical geometry
   is FROZEN throughout (λ₁, λ₂ etc. are spectral data, not couplings).

## Deliverables

`derivations/87-VERDICT.md` (D1–D4, the verdict rule applied, scope
stated); `derivations/87-GATE-N-SUMMARY.md` per gate;
`derivations/87-equation-of-state-RESEARCH.md` (the locus geometry, the
elimination, the certificate or the law, the D4 reading);
`code/variety_equation_of_state.py` (executor) +
`code/variety_equation_of_state_verify.py` (independent path; an
`_indep_check.py` third path is welcome, v26-parity). Commit; HOLD the
v27.0 milestone bookkeeping for ratification, mirroring v25/v26.
