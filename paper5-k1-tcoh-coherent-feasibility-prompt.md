# Paper 5 — T-COH: coherent K=0 feasibility (does the UNENCODED cross-pair coherence force a local lever, or does the vanishing trick survive full-strength heredity?)

## TASK TYPE
Settle ONE specific claim (**CLAIM COH**, §0), prove-or-disprove, with a decision tree. This is
**Gate 2** of the K1 reopened route (Gate 1 = T-NS, landed and cold-checked BANK-WITH-DOWNGRADES —
deep note §19.23: the ¼I identity, curve strictness, and p=2 control verified exact by independent
re-derivation, BUT its STRICT no-sharing is heredity + ENCODING-conditional — established only in
the ½-centered/mutually-unbiased truncated regime; the tilted/biased regime is UNDETERMINED, and
there sharing no longer requires P = 2). It is the analytic successor of CLAIM XD-GROWTH
(`paper5-k1-crossdisk-rank-growth-prompt.md`, verdict BLOCKED in
`~/repos/blog/research/qm-genericity-review/XDGROWTH-VERDICT.md`): Track A there refuted the
PER-PAIR local lever (K = 0 feasible everywhere when each atom pair gets FRESH face variables), but
the cold audit (`COLDPASS-AUDIT-1920.md`) proved that verdict is scoped to the per-pair TRUNCATION —
the constraints that make heredity actually bite were never imposed. THIS task imposes them.

Anti-glaze. Exact arithmetic (ℚ/sympy) wherever decisive. Ground every claim or tag it.

---

## 0. The one claim to settle

> **CLAIM COH.** Fix one pair of distinct close legal Bell frames τ ≠ σ of the Niestegge ℓ⁴ qubit
> (+ their D₄ images as needed) and set ALL cross-frame kernels K = 0 (the vanishing trick). Then
> the **coherent** hereditary level-2 system — defined by (i) ONE face-datum (R_ν, H_ν, G_ν) per
> generated face ν, valid across ν's ENTIRE atom-pair continuum, not fresh variables per pair;
> (ii) consistency across each PENCIL of generated faces through a shared atom; (iii) internal
> ℓ⁴-disk transition values matching ambient transitions for ALL atom pairs on every generated
> face, with the transition/cap forms for tilted/biased units DERIVED from positivity, not assumed
> ¼-centered — is **INFEASIBLE at every finite hidden rank m**.

Prove it or disprove it.

- **PROOF (INFEASIBLE) = a LOCAL LEVER EXISTS.** The vanishing trick dies under full-strength
  heredity: some cross-kernel is FORCED nonzero between close frames — the coherent resurrection of
  XD-GROWTH. Then also extract the quantitative version (a lower bound ‖K‖ ≥ f(τ,σ) > 0, even
  crude) — that is the input to Gate 3 (the growth theorem: forced-nonzero couplings + the T-NS
  no-sharing + caps ⟹ rank growth ⟹ no finite hereditary tower ⟹ hereditary-K1 FALSE ⟹
  **forced selection**, the campaign's wanted outcome). Do NOT claim Gate 3 from Gate 2 — deliver
  the lever and the precise statement of what Gate 3 still owes.
- **DISPROOF (FEASIBLE) = no local lever anywhere.** Exhibit the bounded-rank coherent witness
  ({R_ν, H_ν, G_ν} as functions over the atom-pair continuum, its rank m). Then run the recursion
  test (Codex T4): do the generated faces' OWN cross-disk demands reproduce the same kernel without
  new rank? If YES ⟹ a genuine hereditary ℓ⁴ tower exists ⟹ hereditary-K1 TRUE ⟹ **the §19
  genericity route is DEAD — report as death, plainly, no softening** (pre-registered kill,
  binding). If the witness does NOT recurse ⟹ the decision honestly collapses to the global
  packing bound (park final; report that plainly too).
- **BLOCKED** only with the precise missing lemma + the cheapest computation that would settle it.

---

## 1. Context (read once — why this is the decisive probe)

The genericity route (deep note §19: axiom B as a 1/|Aut| histories-measure; ℂ the unique
B-critical type) has one gate: K1 — can the ℓ⁴ qubit build hereditary (ℓ⁴ all the way down)
record-towers? Banked: below dim 13 impossible [PROVED/CERTIFIED]; the rebit control composes at
dim 10 exactly-on-threshold; level-1 rank prefix m* = 8, 11, 12 climbing but decelerating
(numerically undecidable); per-pair local lever REFUTED (XDGROWTH-VERDICT); K = 0 is rank-MAXIMAL
(m ≥ 4n — the vanishing trick is the most expensive option, NOT a tower). Gate 1 (T-NS) just
established: the ¼I no-sharing algebra transfers verbatim to generated disks; strictness holds at
the effective-frame level (design-sup = original m=2 sup, cells < 4, adversarial clean); STRICT ⟺
heredity; p=2 correctly escapes (isotropy E = I + one global YY hidden coordinate). What Gate 1
could NOT reach: the tilted/biased-unit regime — exactly the coherence this task encodes. The cold
check sharpened this: in the tilted regime the ¼ ± P/8 cap form FAILS, so block-sharing between
distinct generated faces no longer requires P = 2 — a NON-STRICT sharing witness could live there,
and finding one would be a tower-favorable (route-dead-leaning) signal in its own right. The whole
TRUE/FALSE decision for K1 now funnels through CLAIM COH.

## 2. The objects (self-contained; verify in the artifacts, do not re-derive banked items)

**Read first:** `~/repos/blog/research/qm-genericity-review/XDGROWTH-VERDICT.md` (the per-pair
encoding + its scope annotations), `COLDPASS-AUDIT-1920.md` (the audit specifying this probe),
deep note `~/repos/blog/research/paper5-virtuous-loop-three-joints.md` §19.20–§19.23, Codex
`~/.codex-channels/k1-composability/reply_009.md`/`reply_010.md` (level-1/2 encoding), scripts
`~/repos/blog/research/qm-genericity-review/k1_frame_manifold.py`, `k1_xdgrowth_01_range.py`,
`k1_xdgrowth_02_local.py`, `k1_tns_01_identity.py`–`k1_tns_04_adversary.py` (reuse the frame
parametrization T_s, the duality map J(y)_i = sign(y_i)|y_i|^{1/3}, and the effective-frame
machinery (E_ν, T_ν) — T-NS's P_{νν′} = tr(E_ν T_{ν′}) is the transition datum one level down).

Arena (from reply_009/010, as annotated): frames τ carry flat units P_{τ,s} with disk atoms
a_{τ,s,y} = ½P_{τ,s} + H_{τ,s}y (‖y‖_{4/3} = 1), carriers ω_{τ,s,x} = ω⁰_{τ,s} + G_{τ,s}x
(‖x‖₄ = 1), forced duality G_{τ,s}ᵀH_{τ,s} = ½I₂, G_{τ,s}ᵀH_{τ,−s} = 0; cross-frame kernels
K_{τσ}^{st} = G_{τ,s}ᵀH_{σ,t} — SET TO ZERO throughout this task. Cross-disk spectrality: for
atoms p = a_{τ,s,y}, q = a_{σ,t,z}, heredity forces a generated ℓ⁴ disk ν(p,q): ½R_ν + H_νr = p,
½R_ν + H_νu = q, G_νᵀH_ν = ½I, internal transitions (1 + J(r)·u)/2 = α, (1 + J(u)·r)/2 = β
matching ambient (at K = 0: α, β pinned by product-sector data A alone).

**The COHERENCE constraints (the new content — what the per-pair encoding omitted):**
1. **One datum per face.** A generated face ν is a FACE, not a pair-artifact: every atom pair
   (p′, q′) lying ON ν must be interpolated by the SAME (R_ν, H_ν, G_ν) with internal parameters
   (r′, u′) and matching ambient transitions. The per-pair design freedom (the free column w′,
   XDGROWTH-VERDICT's [PROVED] item) must survive being shared across the whole continuum of pairs
   on ν — or fail.
2. **Pencils.** For a fixed atom p on frame τ's disk, the family ν(p, q_z) as q_z sweeps frame σ's
   disk is a continuum of generated faces all CONTAINING p. Each pencil member's carrier data must
   norm p consistently: the transition ω(p-normer of ν)(anything) is face-independent (A-S
   compressions preserve transitions — cold-audit finding #5: matching is an identity once ν is a
   real face; the FORCE must come from ν's embedding, never from assuming ν composes).
3. **Biased/tilted units DERIVED.** Generated units R_ν are generically NOT ½-centered
   product-aligned flat units (T-NS: generated faces occupy distinct TILTED blocks; their base
   transitions drift off ¼). Derive the positivity boxes/caps for tilted units from
   0 ≤ effect ≤ 1 against all states directly — do NOT import the ¼ ± P/8 cap form (T-NS proved it
   only in the ¼-centered regime; assuming it here would be the starvation-artifact analogue).
4. **Recursion boundary (flag, don't silently truncate):** atoms of ν differenced against original
   atoms or other generated atoms trigger level-3 faces. This task is LEVEL-2-COHERENT: impose
   1–3 fully; STATE what level-3 demands are deferred (if your FEASIBLE witness only survives by
   pushing violations into deferred levels, say so — that is not feasibility).

## 3. The decider — run analytics first, encode second

**Step 1 (analytic core, exact):** for close frames σ = τ + δ, work out the coherent system on ONE
pencil at K = 0. Count: unknowns per face-datum (shared, not per-pair) vs matching equations over
the pair-continuum + pencil consistency. The per-pair result (free w′ ⟹ always solvable) used one
fresh w′ PER PAIR; coherence forces one w′ per FACE and pencil-consistency across faces. Determine
whether the overdetermination is real (rank/Jacobian at the coincidence anchor: at σ = τ the
generated face IS the frame's own disk, K_ττ = ½I forced — the coherent system must reproduce this
limit exactly; a formulation failing the coincidence control is discarded).
**Step 2 (exact feasibility encoding):** extend the level-2 encoding with shared face-data
variables (per face, not per pair), pencil constraints, and derived tilted-unit boxes; test
bounded-rank feasibility at K = 0 for one close pair, sampled atom pairs + pencil members, then
push boundary cells to exact/sympy.
**Step 3 (whichever way Step 2 points):** INFEASIBLE ⟹ extract which constraint family delivers
the contradiction (pencil? shared-datum? tilted boxes?) and the quantitative lever ‖K‖ ≥ f > 0
(re-run with K free and small to find the feasibility threshold). FEASIBLE ⟹ exhibit the witness
explicitly and run the T4 recursion test on it.

**Controls (pre-register; a run failing its control is discarded wholesale):**
- Coincidence: σ → τ must reproduce the frame's own disk with K_ττ = ½I and identical transitions.
- **p=2 control (MANDATORY):** the rebit's coherent system at its own K = 0 analogue must be
  FEASIBLE (it composes at dim 10; one global YY hidden coordinate serves every face; pencils close
  through it — exhibit or verify). If your coherent constraints kill the rebit too, the encoding is
  MIS-NORMALIZED — fix it before reading any ℓ⁴ verdict.
- Iteration-scaling discriminator on every boundary cell (4× warm-started budget: collapsing
  residual = slow-feasible; flat plateau nit→0 = infeasible). This campaign was burned twice.
- True ℓ^{4/3}→ℓ^{4/3} norms only where operator norms arise; no spectral proxy.

## 4. Guards (anti-glaze — binding)
- **The wanted outcome is INFEASIBLE** (it re-lights the forced-selection route) — therefore attack
  FEASIBLE hardest. A false INFEASIBLE poisons the mainline worse than an honest park.
- Do not conflate "optimizer found no witness" with infeasibility — grade
  [PROVED/CERTIFIED/COMPUTED/ARGUED] per claim; infeasibility claims need an exact certificate
  (rank obstruction, sign contradiction, semialgebraic infeasibility) or the iteration-scaling
  discriminator at minimum.
- Do not assume ν composes to prove ν composes (cold-audit #5); force comes from embedding demands.
- Do not import the ¼-centered cap form into the tilted regime (T-NS scope boundary).
- DEFLATION vs SURRENDER: "FEASIBLE with recursion ⟹ route dead" is a real result — deliver it as
  death, no hedging to "conditional." "FEASIBLE without recursion ⟹ decision = global packing" is
  also real — the park then hardens honestly. Neither is failure; only a fake verdict is.

## 5. Output
- Verdict on **CLAIM COH: INFEASIBLE / FEASIBLE / BLOCKED**, with grades per claim.
- If INFEASIBLE: the contradicting constraint family + the coincidence-control check + the
  quantitative lever f (or the statement it resists quantification) + what Gate 3 still owes
  (growth theorem: forced-K + T-NS no-sharing + caps ⟹ unbounded rank — do not claim it).
- If FEASIBLE: the explicit bounded-rank coherent witness + the T4 recursion test result + the
  plain-language consequence (recursing ⟹ genericity route DEAD; non-recursing ⟹ park final at
  the packing wall).
- p=2 control result, stated explicitly either way.
- **The tilted-regime sharing readout (mandatory, separate from the feasibility verdict):** under
  your DERIVED tilted caps, can two DISTINCT generated faces occupy the SAME hidden 2-block (a
  NON-STRICT witness, sharing at P < 2)? YES-with-witness / NO-with-certificate / UNDETERMINED.
  A YES is tower-favorable and retro-downgrades T-NS's relevance — report it prominently, do not
  bury it inside a feasibility answer.
- File back into the deep note (new subsection under §19), update
  `~/repos/blog/research/qm-genericity-review/HANDOFF-K1-OPUS.md` §4, scripts as
  `~/repos/blog/research/qm-genericity-review/k1_tcoh_*.py`. **NO SSOT flip without Bryan** (P5
  stays CONDITIONAL-SYNTHESIS regardless; this decides the genericity upgrade's gate, not the
  floor). No git commits.
