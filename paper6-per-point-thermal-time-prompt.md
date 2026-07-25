# GPD Prompt — Per-Point Thermal Time: the Referent-Free Consistency Test (Claim 2 / J4)

**Slot 89 / v29.0-candidate. STATUS: RATIFIED-BY-STANDING-DIRECTIVE
(Bryan, 2026-06-11). Queued behind slot 88; run when 88 completes.**

_Context: this is CLAIM 2 — the J4 thermal-time question pinned since
slot 83, now run with the variety machinery it was waiting for.
Certified assets consumed: the moment doublet (m, q) and r = q/m²
(v25); the perturbation machinery X = I/3 + εM and the level
decomposition (constants ⊕ level-1 ⊕ level-2, the R_M object) (v26);
K_face = −log ρ_face explicit in (m,q) (face eigenvalues
½ ± ½√(1−4r)); the 16 recorded families; the harmonic/eigenvalue
toolkit λ₁ = 12/48, λ₂ = 32/104. The question (referent-free form,
recorded 2026-06-10): do the per-face modular generators of ONE
structured state cohere into ONE global generator up to compression —
i.e., is there an emergent global state-time — or is thermal time
irreducibly face-relative? LIVE upgrades Jacobson joint J4 from
IMPORT to PROGRAM-SUPPLIED (originality budget {J5} → {J4, J5});
DEAD retypes time as face-local and the obstruction field becomes
connection-shaped data. BOTH branches are consumed downstream (the
Block-A unfreezing design). Connes–Rovelli thermal time is the
literature frame (cite); no thermodynamic postulate enters any
verdict path — everything is exact state algebra._

_Discipline: v21–v28 pattern — executor + independent verifier
(separate code path), exact verdicts only, fail-fast gates, controls
with known answers. No proper-time/metric/Einstein claims; the
lapse/twist outputs are CANDIDATES for the Block-A design, not metric
components. No Newton constant, no G = κT, no dark matter._

## Pre-read: milestone type (pre-registered)

**GENUINE FORK** (v27 class): no expected verdict, both branches
informative and both payloads downstream-consumed. Honest prior,
pre-registered: leaning DEAD at the deciding order (the level-count
argument below — the v26 precedent says level-2 content is
generically present), with LIVE requiring a δr = 0-class miraculous
cancellation — which this program has produced before, so the test
is genuinely open, not theater. The DESIGN PASS CAUGHT THREE VACUITY
TRAPS (#5–#7 below, instances 10–12 of the recorded bug class); the
claims are structured so none of them can produce the verdict.

## The setup (verify every step; the trap inventory is load-bearing)

**Objects.** Structured state X = I/3 + εM (Tr M = 0, M symbolic),
positive definite (det X ≠ 0 — the observer condition). At each event
p (rank-1 idempotent), the face state ρ_face(p) = C_pX / Tr(C_pX) on
the complementary 2-face, and the per-face modular generator
K_face(p) = −log ρ_face(p). The consistency question: does there
exist ONE global Hermitian H with

> traceless( C_pH ) = β · traceless( K_face(p) )  for ALL p,

with ONE global constant β (a single time unit) and per-face
I-shifts quotiented (modular flow is unchanged by adding multiples
of the face identity)?

**TRAP #5 (caught at the desk): direction-only is VACUOUS.** For a
2×2 face, ANY function f(ρ) has traceless part PARALLEL to the
traceless part of ρ (ρ = c₀I + r·n̂σ ⇒ f(ρ) = aI + b·n̂σ). So
"common generating DIRECTION" alone is trivially LIVE with H = X
itself (C_pX ∥ ρ_face ∥ K_face at every face, automatically). The
content is NOT the direction — it is whether the per-face RATES
(b(p) = −½ log(λ₊/λ₋), transcendental in the gap) are jointly
realizable by one linear object with one global β. Verify the 2×2
parallelism fact symbolically (it doubles as the reduction lemma),
then NEVER use direction-match as evidence.

**TRAP #6 (caught at the desk): single-rotation faces are
structurally consistent.** For X diagonal and p on a standard
(1,2)-family (v = (c, sω, 0)), the complement face contains e₃ as a
common eigenvector and C_pX, C_p(log X) CO-DIAGONALIZE — consistency
is automatic, carrying ZERO evidence. The same holds for all 16
standard families from E_11 against frame-aligned X, and at the
eigenframe faces themselves (C_{E_ii}X diagonal). A run testing only
the standard families would return FAKE-LIVE. Verdict faces must be
FULLY GENERIC: p = vv* with all three eigencomponents of v nonzero.
Rational anchor face (hand-picked): **v = (1, 2, 2)/3** (exactly
unit: (1+4+4)/9 = 1), with **X = diag(1, 2, 3)/6** (positive, Tr = 1,
distinct). Verify the co-diagonalization claim on the families as a
Gate-1 control, then exclude those faces from all evidence.

**TRAP #7 (caught at the desk): first order is structurally LIVE.**
Expanding ρ_face = I₂/2 + ε·(δρ) + O(ε²): −log(I/2 + εδρ) =
log2·I − 2ε·δρ + O(ε²) — the ε¹ part of K_face is LINEAR in the
compression δρ, so a global H^(1) ∝ M always realizes it. A
first-order-only test would fake-LIVE. Pre-register ε⁰ (vacuum:
K ∝ I, trivial) and ε¹ (always coherent) as zero-weight controls.
**The verdict lives at ε².**

**The deciding structure (the level-count argument — verify, then
use).** The ε² coefficient of K_face(p) contains products of
first-order terms ((δρ)², ⟨M,p⟩·δρ cross-terms), so as a field over
events it carries p-dependence at LEVEL 2 (the ⟨M,p⟩²-type sector —
the v26 R_M story). But the compression of any FIXED global H is
LINEAR in p — level ≤ 1 — for every Peirce component. Therefore:

> **A global H exists at order ε² ⟺ the level-2 part of the
> second-order modular field vanishes identically.**

This reduces claim 2 to a finite, exact harmonic computation in the
certified v25/v26 toolkit. The v26 precedent (R_M ≢ 0 — the level-2
part of ⟨M,p⟩² is a genuine λ₂-eigenfunction) is why the prior leans
DEAD; the open question is whether the SPECIFIC combination appearing
in the log expansion cancels (the δr = 0 precedent shows such
cancellations happen when the algebra wants them).

**Exactness scheme for finite-ε corroboration (no floats).** log X =
Σᵢ (log xᵢ) Pᵢ (spectral), so C_p(log X) = Σᵢ ℓᵢ · C_p(Pᵢ) with
FORMAL symbols ℓᵢ = log xᵢ and rational matrices C_p(Pᵢ). All
verdict-path checks are per-symbol polynomial identities over Q
(note Σᵢ C_p(Pᵢ) = I_face, so only n−1 symbol-coefficients are
independent; the I-shift gauge absorbs the normalization constant).
Watch multiplicative relations among the xᵢ when choosing instances
(diag(1,2,3)/6 has logs affine in the two symbols {log 2, log 3} —
acceptable and recorded; avoid e.g. diag(1,2,4) where ℓ₃ = 2ℓ₂
silently collapses a condition).

## Claims

**T1 — the reduction (lemma grade).** (i) The 2×2 parallelism fact
(any f(ρ) is I-plus-parallel), hence the H = X direction-vacuity —
verified symbolically; the sharp non-vacuous statement formulated as
above (one global β, I-shifts quotiented). (ii) The ε-grading:
ε⁰ trivial, ε¹ always coherent (exhibit H^(1) explicitly), the
question begins at ε². (iii) The level-count lemma: compressions of
fixed H are level ≤ 1 in p, per Peirce block, verified against the
v25 machinery.

**T2 — strata and controls (zero evidential weight, all must
behave).** Vacuum (K ∝ I); eigenframe faces (co-diagonal);
single-rotation/standard-family faces (co-diagonal — the trap-#6
catch verified); first order (coherent, the trap-#7 catch verified);
the generic rational anchor face v = (1,2,2)/3 is NOT in any trivial
stratum (verify: no common eigenvector, faces genuinely mix all
three eigendirections).

**T3 — THE VERDICT (at ε², exact).** Compute the second-order
modular field: the ε² coefficient of traceless K_face(p) as an exact
function over the variety (symbolic M at E_11 + families + the
generic-face machinery; u-complex sector first, then full). Decompose
by harmonic level (the certified toolkit). Then:
**LIVE ⟺ the level-2 part ≡ 0** (then construct the global H up to
ε², extract the per-face rate field α(p) exactly, and express it in
the certified moments (m, q) — the lapse candidate, the
position-dependent-ticks field); **DEAD ⟺ the level-2 part ≢ 0**
(then extract it exactly in the harmonic basis — the modular-anomaly
/ clock-twist field, an R_M-cousin: state its precise relation to
the v26 R_M object). Either payload stated exactly; OPEN only if a
computation is genuinely infeasible (record which and why).

**T4 — corroboration and extensions (non-blocking).** (i) Finite-ε
check on the rational anchor (X = diag(1,2,3)/6, p from
v = (1,2,2)/3) via the formal-log scheme — must agree with the ε²
verdict's sign (a finite-ε LIVE with an ε²-DEAD or vice versa = a
design hole, STOP and report). (ii) The bottleneck contrast: one
genuinely octonionic instance — h₂(O) faces are spin factors, the
parallelism fact still holds (9-sphere instead of Bloch sphere) —
does the cut-vs-mother distinction change the verdict pattern?
(iii) The KKT comparison as the recorded non-blocking interpretation
gate only.

## Gates

- **Gate 0 — machinery regression (fail-fast).** v25 doublet + v26
  perturbation identities re-verified; the spectral-compression
  identity C_p(log X) = Σ ℓᵢ C_p(Pᵢ) on the anchor; the 2×2
  parallelism lemma symbolic.
- **Gate 1 — controls (the trap inventory, zero weight).** All of T2;
  every trivial stratum must come out consistent (they are controls
  that the machinery behaves, not evidence).
- **Gate 2 — T1** (the reduction + the level-count lemma).
- **Gate 3 — T3 in the u-complex sector** (the verdict computation,
  symbolic M).
- **Gate 4 — T3 full + T4** (the global verdict; the payload field
  extracted exactly; the finite-ε cross-check).
- **Gate 5 — the consumption ledger (exploratory, NO claims).**
  (i) Block-A consumption: LIVE → emergent global time + lapse
  α(m,q) feeds the 5d/appended-time design; DEAD → time is
  face-local and the twist field is the connection-shaped object
  (the parallel-transport-of-clocks datum) — state which world and
  what the next design consumes. (ii) J4 bookkeeping: LIVE =
  IMPORT → PROGRAM-SUPPLIED ({J5} → {J4,J5}); DEAD = J4 stays
  imported, recorded. (iii) v30 candidates priced, no verdicts.
- **STOP rule:** any broken reduction step, or a T4(i) sign
  disagreement = design hole; report and STOP.

## Guards (pre-registered)

1. **No direction-only evidence** (trap #5): every LIVE-relevant
   check must constrain rates/magnitudes, not rays.
2. **Strata discipline** (trap #6): standard-family and eigenframe
   faces are excluded from evidence; verdict faces generic (all
   three eigencomponents nonzero).
3. **Order discipline** (trap #7): ε⁰/ε¹ are controls; only ε²
   carries the verdict.
4. **Exactness:** formal-log symbols over Q; per-symbol polynomial
   identities; no floats in any verdict path; multiplicative
   relations among eigenvalues recorded per instance.
5. **Gauge quotients stated once:** per-face I-shifts and the ONE
   global β are the only freedoms; any per-face rescaling sneaking
   into a LIVE claim is the H = X vacuity returning.
6. **The octonion product-order trap (standing):** conj(x₃x₂)-type
   entries; independent implementations agree on an octonionic
   battery before verdicts.
7. **Language fence:** thermal time = state flow (Connes–Rovelli,
   cite); no proper-time/metric/Einstein/dark-matter language; the
   lapse and twist fields are design INPUTS for Block A, not
   physics claims.

## Deliverables

`derivations/89-VERDICT.md` (T1–T4, the verdict rule applied, scope
stated); `derivations/89-GATE-N-SUMMARY.md` per gate;
`derivations/89-thermal-time-RESEARCH.md` (the reduction, the trap
inventory, the level computation, the payload field, the Gate-5
ledger); `code/thermal_time_consistency.py` (executor) +
`code/thermal_time_consistency_verify.py` (independent path; an
`_indep_check.py` third path welcome, v26–v28 parity). Commit; HOLD
the v29.0 milestone bookkeeping for ratification, mirroring v25–v28.
