# v22.0-candidate: KKT-Slice Gluing Freedom and Three-Point Holonomy (the η-reading test)

_Registered 2026-06-09 from `blog/research/gr-from-h3o/substrate-dictionary-gravity.md`
§9 (steelmanned twice before registration; the vacuous first form of this test was
caught and replaced — see §9.3 there). Derivation slot: **82**. Pattern: executor +
independent verifier through different code paths, exact over Q where possible,
fail-fast gates cheapest-first (the v21/Sakharov discipline)._

---

## Context (one paragraph, no more needed)

The six-kind metric-selection menu is exhausted for Einstein gravity (v17-v21;
`selection-law-ledger.md`). The live question moved one level down: Phase 46/52
proved the observer's Peirce slice V_0 ⊃ h_2(C_u) ≅ R^{3,1} with KKT = so(4,2)
(OD1-OD7), worded as "V_0 IS spacetime" — the GLOBAL reading. But the global
reading forbids curvature a priori (a curved manifold is only locally R^{3,1}),
and an OD1-OD7 re-sort (substrate-dictionary §9.1) found all seven criteria pin
MODEL-LEVEL structure only (so(4,2) is the model algebra of conformal Cartan
geometry; OD5 gives per-observer F_4-CONJUGATE copies — "same spacetime *up to*
F_4"). The open question: **does anything in the algebra force a canonical FLAT
identification (gluing) between distinct observers' local models, or is the
gluing genuinely free?** Free gluing = the independence half of the
"implementation dictionary" route (gravity = the unforced inter-observer gluing
field). Forced-flat gluing = that route DEAD and the global reading vindicated.

## The claim to prove or disprove

**CLAIM (independence):** In h_3(O), after imposing every program-native
compatibility condition, the identification between the KKT slices of two
distinct primitive idempotents retains residual freedom (is NOT canonically
unique), and the three-point loop composition of pairwise identifications is
NOT forced to the identity.

Disproof (= canonical unique identifications with forced-trivial loop) is the
DEALBREAKER for the dictionary route and is equally valuable: it would be the
first theorem-grade certification of the global flat reading, strengthening
fork A. **Both branches are informative; there is no wasted outcome.**

## Setup (all ingredients already exist)

- Standard frame E_11, E_22, E_33 in h_3(O); F_4 transitive on primitive
  idempotents; Stab(E) ≅ Spin(9) (classical, used in Phases 48/52).
- Phase 52's explicit conjugating automorphism P = (1,0,2) (max err 1.9e-15
  numerically; redo exact or to verifier-grade precision).
- Phase 46/48 machinery: π_u, h_2(C_u) slice, det_2 Gram, Stab(u) ∩ Spin(9) =
  so(3) ⊕ so(6), pi_u equivariance under all 18 stabilizer generators.
- Warm h_3(O) arithmetic engines from the v17-v21 harness
  (`code/cartan_phaseB_curvature.py` lineage; det SSOT).

Definitions for this run:
- An **identification** E_i → E_j is g ∈ F_4 with g·E_ii = E_jj (hence g maps
  the Peirce decomposition of E_ii to that of E_jj, and V_0(E_ii) → V_0(E_jj)).
- Its **slice action** is the induced map h_2(C_u)(E_ii) → h_2(C_u')(E_jj)
  (note: g need not respect the complex structures u, u' — that is one of the
  Gate-1 conditions, not an assumption).
- The **residual group** R_ij = the set of slice actions of
  {g : g·E_ii = E_ii, g·E_jj = E_jj}-composable redefinitions, i.e. the
  ambiguity left after endpoints are fixed. Compute it as a group, exactly.

## Gates (cheapest first; STOP at first decisive kill)

### Gate 0 — the identification space (pure structure, cheapest)

Compute exactly:
1. The coset {g ∈ F_4 : g·E_11 = E_22} (= P · Stab(E_11); confirm exact).
2. The residual group R_12 acting on the h_2(C_u) slice after fixing both
   endpoint idempotents. Express it as a Lie subgroup/subalgebra (dimension,
   isomorphism type) of the slice's structure group.

**Expected wrinkle (NOT a failure — pre-registered):** F_4 is compact, so R_12
is compact; the slice's full isometry group SL(2,C) is non-compact and was
NEVER inside Spin(9) (Phase 48: boosts come from det_2, not internal symmetry).
Compact-only residual freedom (e.g. containing the so(3) rotation block) is
CONSISTENT with the dictionary picture (algebraic freedom = compact part;
boost freedom = metric-side). Do not misreport compactness as a kill.

**Kill condition at this gate:** R_12 trivial (identification already unique
from bare algebra) → skip Gate 1, go straight to Gate 2 (holonomy of the
unique identifications).

### Gate 1 — the canonicalization sweep (does anything force uniqueness?)

Impose, ONE AT A TIME and then cumulatively, each program-native compatibility
condition on g, recomputing the surviving freedom R_12 ⊇ R^{(1)} ⊇ R^{(2)} ⊇ …
exactly at each step:

1. **u-alignment:** g maps the complex structure u of E_11's slice to u' of
   E_22's slice (equivalently g intertwines π_u and π_u').
2. **det_2 isometry:** the slice action preserves the det_2 Minkowski form
   (should be automatic from F_4 ⊂ Aut; verify, don't assume).
3. **Peirce-block preservation:** g maps V_{1/2}(E_11) → V_{1/2}(E_22) and
   V_1 → V_1 (automatic given g·E_11 = E_22; verify exactly).
4. **Interface intertwining (minimal mutual-faithfulness proxy):** g
   intertwines the sequential-product data each observer assigns to the SHARED
   V_{1/2} channel — concretely, for the basis V_{1/2}-elements x: the Peirce
   quadratic maps / V_{1/2}∘V_{1/2} → V_0 products computed in E_11's frame,
   pushed through g, equal those computed in E_22's frame. (This is the only
   condition with modeling content; state the exact operator equation used and
   flag any choice made in formulating it — the verifier must be able to
   re-derive the equation from Peirce structure alone.)

**Output:** the chain of residual groups, exact. **Kill condition:** some
condition (state which) cuts the freedom to triviality = identifications are
CANONICAL → the gluing is algebra-determined → proceed to Gate 2 with the
canonical g's; if instead freedom survives all four, record the surviving
group (this is already the independence result at the two-point level).

### Gate 2 — three-point holonomy (THE decisive gate)

With the standard frame E_11, E_22, E_33 and pairwise identifications g_12,
g_23, g_31 (canonical ones if Gate 1 forced uniqueness; otherwise sweep
representatives of the residual classes):

Compute the loop composition h = g_31 ∘ g_23 ∘ g_12 ∈ Stab(E_11), and its
slice action on h_2(C_u)(E_11).

Three exhaustive outcomes:
- **(DEAD branch)** h's slice action is forced to the IDENTITY for ALL
  admissible choices → the algebra certifies flat gluing around the loop →
  **the dictionary route is DEAD; the global flat reading is vindicated as a
  theorem; record as fork-A-strengthened.** (This is the predicted-death
  analogue of v21 Gate 2 — a clean negative is a success.)
- **(LIVE branch A)** the slice action of h is choice-dependent (sweeps a
  nontrivial set as the residual classes vary) → gluing genuinely FREE →
  **independence PROVED in exact arithmetic** (the axioms do not force global
  flatness; the freedom is the candidate dictionary degrees of freedom).
- **(LIVE branch B, strongest)** h is forced NONTRIVIAL for all admissible
  choices → the algebra OBSTRUCTS flat gluing → independence proved AND a
  canonical curvature seed exists. (Treat with suspicion; verify the
  identifications were not mis-normalized — a spurious forced-h is the most
  likely executor bug.)

### Gate 3 — associator contact (exploratory; run ONLY if Gate 2 lands LIVE-B)

If a forced nontrivial h exists, test whether it is expressible through the
associator/triality structure (Baez: the associator determines the curvature of
the cone metric — Piece 10). EXPLORATORY: no kill condition, no claim beyond
"contact found / not found." Do not let this gate's outcome color the Gate 2
report.

## Scope and anti-overclaim (binding on the writeup)

- A LIVE outcome proves **INDEPENDENCE ONLY**: the axioms do not force a
  canonical flat gluing. It does NOT prove the No-Absolute-Objects Lemma (the
  "bridge" — that the model's law may contain only forced/certified structure —
  remains an ARGUED clamp, attacked separately in-repo), does NOT produce a
  metric law, G = κT, or any dynamics, and does NOT touch the v17-v21 /
  Sakharov verdicts (the six-kind menu stays exhausted; this is not a
  metric-selection law).
- A DEAD outcome kills the implementation-dictionary route specifically and
  certifies the global flat reading of Phase 52; it does NOT retroactively
  validate any dead route.
- The compactness of all F_4-side freedom is expected and is not evidence
  either way about boosts (Phase 48).
- Numerology guard: no physical constants, no κ, no Λ anywhere in this run.

## Deliverables

1. `derivations/82-kkt-gluing-RESEARCH.md` — setup, exact definitions used
   (especially Gate 1 condition 4's operator equation), gate-by-gate results.
2. `derivations/82-GATE-{0,1,2}-VERIFICATION.md` — independent verifier,
   different code path, exact recomputation of each residual group and of h.
3. `code/kkt_gluing_holonomy.py` (+ verifier twin) — warm-harness based,
   exact-Q core, det SSOT.
4. One-paragraph verdict in the v21 format: which branch fired, what it kills,
   what it leaves open (the bridge clamp), no promotion past independence.

## Source-of-truth pointers (blog repo)

- `research/gr-from-h3o/substrate-dictionary-gravity.md` §8-§9 (the route, the
  two audits, this test's registration and its vacuity fix)
- `research/gr-from-h3o/selection-law-ledger.md` (the exhausted menu this does
  NOT reopen)
- `research/gr-from-h3o/gap-analysis.md` Phases 46/48/52 (OD1-OD7, stabilizers,
  the P=(1,0,2) automorphism)
