# GPD Prompt — The Two-Term Balance Question (Jacobson J5, fiber side)

**Slot 83 / v23.0-candidate. STATUS: RATIFIED by Bryan 2026-06-10 — READY
TO RUN. (Claim 1 of the revised menu, `entanglement-route.md` §10.5. The
appendix claim-2 draft remains UNRATIFIED — its design blocker stands.)**

_Context (blog repo): `research/gr-from-h3o/entanglement-route.md` (the
kind-7 unban, demon test 2.0, the Jacobson-2015 joint table §8.4, the
vacuity catch §8.1, the two-term deflation §8.2, the R^(2Δ) critique §8.5a,
Bryan's synthesis §10). Discipline: v21/v22 pattern — executor + independent
verifier, exact over Q wherever possible, fail-fast gates, pre-registered
failure modes. One sharp claim. No κ, no Λ, no G = κT anywhere in this run._

## The claim (sharp, falsifiable)

> In h_3(O), with faces given by Peirce compressions, there EXISTS a
> program-native scalar functional A (the "geometric/volume" term) and a
> native constraint such that the faithful point X = I/3 is a critical
> point of the COMBINED functional S + λA with **λ ≠ 0 forced and the
> balance non-degenerate** — i.e., the fiber carries a genuine TWO-TERM
> Jacobson-shaped equilibrium, not the one-term entropy-max tautology.

DEAD and LIVE are both informative:
- **DEAD** (no native A at low degree gives a forced non-degenerate λ ≠ 0):
  the vacuum-identification flip is decoration; the second/geometric term
  provably does not live on the fiber; the route is FULLY gated on the
  base/format object. (This would be a clean, publishable scope theorem —
  the fiber-side analog of "Molien has no κ-slot.")
- **LIVE** (exhibit A, constraint, λ ≠ 0, non-degenerate): the fiber
  carries a Jacobson-shaped balance; report the winning A, its degree/grade,
  and proceed to Gate 3 (support structure).

## Setup

- Algebra: h_3(O) over Q (octonion structure constants as in v17-v22;
  u = e_7 conventions as recorded).
- Faces: for a primitive idempotent p (start p = E_11) and the rank-2
  complement, the Peirce compression C_p; the face-reduced state of a
  configuration X is the compressed, normalized positive element
  ρ_face(X) = C_p(X)/Tr(C_p(X)) (define carefully; record the choice).
- Entropy: S_face(X) = von Neumann entropy of ρ_face(X) (eigenvalues exact
  over Q or algebraic extensions for the pre-registered configs; symbolic
  where needed).
- The faithful point: X = I/3 (recorded: ρ_J = 0, the TrX² = 1/3 branch,
  max-entropy/thermal-death state — `lie-sector-gravity.md` 2026-06-06).

## Gates

### Gate 0 — the invariant candidate space (derive, don't guess)

Compute the LOW-DEGREE (≤ 3) generators of the Stab_{F_4}(p)-invariant
polynomial ring on h_3(O) (Stab(E_11) = Spin(9); the Peirce blocks
decompose as Spin(9)-modules — derive the decomposition exactly; expected
shape: the two diagonal traces, the spinor-block norm (the 16), the
vector-block norm, det-type cubics — but DERIVE it, the list is the
deliverable). This is the EXHAUSTIVE candidate space for A at low degree:
every native face-functional is a polynomial in these generators.
**Fail-fast:** if the ring computation doesn't close cleanly at degree 3,
stop and report.

### Gate 1 — calibration (the pre-registered tautology; MUST pass, carries zero evidence)

Confirm X = I/3 is the unconstrained fixed-trace maximum of S_face (both
face choices). This is the §8.1 degeneracy (K ∝ I, first variations vanish).
If this FAILS something is wrong with the setup — abort. Passing it proves
NOTHING (pre-registered: the one-term extremum is the tautology this run
exists to go beyond).

### Gate 2 — THE TEST: the candidate sweep for a forced two-term balance

For each generator-monomial candidate A from Gate 0 (exhaustive through
degree 3), and for each native constraint choice from the pre-registered
constraint set {fixed Tr, fixed Tr_face, no constraint, fixed det — record
any other natural ones found in Gate 0}:

1. Solve the criticality condition δ(S_face + λA) = 0 at X = I/3 over the
   FULL tangent space (all Peirce blocks), exactly.
2. Record whether criticality FORCES λ ≠ 0 (forced = required by the
   equations, not chosen; λ = 0 allowed ⇒ that candidate is the tautology
   again).
3. For any λ ≠ 0 solution: compute the SECOND variation and check
   non-degeneracy + the saddle/competition structure (the A-term and S-term
   must genuinely compete — opposite-sign contributions on a shared block,
   the Jacobson shape — not reinforce).

**Branch verdicts:** all-candidates-fail ⇒ **DEAD at degree ≤ 3** (state
the scope honestly: higher degree remains, with a naturalness penalty —
report the obstruction pattern, e.g. "every invariant's gradient at I/3 is
∝ the identity ⇒ no competition possible," if that is the mechanism).
Any candidate passes ⇒ **LIVE**; report (A, constraint, λ, second-variation
signature) and its Molien/ring status (is A a function of Tr/Tr²/det alone,
or does it need the face structure? — the latter is expected and
informative: face-dependence = the fiber's shadow of geometry).

### Gate 3 — ONLY IF LIVE: the support preview (claim-3 rider)

For the winning balance, compute the second-order response per Peirce block
(V_1 vs V_{1/2} vs diagonal) for matter-type perturbations (v18-type
structured directions). Compare the support pattern against the recorded
16-vs-6 wall (`selection-law-ledger.md` §5). This is a PREVIEW of the
predicted death-spot, not a G = κT test — no geometric matching claims.

## Pre-registered failure modes (the bug guards)

1. **First-law vacuity** (§8.1): any check that reduces to δS = δ⟨K⟩ alone
   is an IDENTITY and proves nothing — if a gate collapses to it, the gate
   is void; abort and redesign. (This bug already fired once, in the
   original §6.1 design.)
2. **λ-glaze:** "λ ≠ 0 exists" is NOT the claim; "λ ≠ 0 FORCED +
   non-degenerate competition" is. A free λ that the equations don't fix =
   DEAD for that candidate.
3. **Constraint-smuggling:** the Tr X² = 1/3 shell IS the faithful branch
   (recorded); imposing it as a constraint trivializes the test — banned
   from the constraint set.
4. **Normalization traps** in ρ_face (the compression-then-normalize order
   matters at second order — fix the convention in Gate 0 and verify it
   doesn't manufacture spurious criticality).
5. **u-alignment** (the v22.0 lesson): any map used between faces must be
   u-aligned; bare transpositions carry the antiholomorphic octonion
   conjugation.

## Anti-overclaim (binding scope)

- LIVE ≠ Einstein, ≠ gravity, ≠ J5 won. It is the FIBER SHADOW of J5: the
  statement "a Jacobson-shaped two-term equilibrium exists at the faithful
  point." The geometric/base matching (real J5 + J1) remains gated on the
  base/format object. Jaksland governs: only program-native joints count.
- DEAD at degree ≤ 3 ≠ absolute DEAD — but say so once, without inflating
  higher-degree hope.
- The J5 target is the MODIFIED Jacobson conjecture (the CGM/Speranza
  R^(2Δ) repair, §8.5a), not the naive 2015 form — note any contact.

## Deliverables

- derivations/83-* (the Spin(9) decomposition; the invariant generators;
  the criticality systems; the verdict per candidate × constraint).
- code/entanglement_two_term.py (exact/Q; executor), independent verifier
  re-derivation (different code path, the v21/v22 pattern).
- One-paragraph verdict: DEAD-at-low-degree / LIVE(A, λ, signature), with
  the §8.5a and Gate-3 notes.

---

## APPENDIX — claim 2, PINNED (J4 thermal time; design blocker RESOLVED 2026-06-10; awaiting Bryan's ratification as a separate run)

**The pinning analysis (in-repo, resolves the referent question by
elimination):**

1. The Stone/JLB referent is a CLASS, not an element — TARGET-1 proves
   "time evolution exists" (nonzero bracket ⇒ some one-parameter
   automorphism group); WHICH generator is recorded as contingent. Using it
   as the referent makes the claim unfalsifiable.
2. **The finite-dim vacuity trap (4th instance of the bug class,
   pre-registered here):** in Type I, EVERY state's modular flow is inner —
   K = −log ρ is always an algebra element — so "the modular flow is
   generated by the Lie sector" is TRIVIALLY TRUE. The naive Connes-Rovelli
   check carries zero content in finite dimension.
3. The KKT so(4,2) referent is interpretation-flagged (OD3: "J⁺ =
   world-translations was interpretation, not computation"), so pinning to
   it makes any DEAD ambiguous (wrong referent vs wrong hypothesis).

**Therefore the sharp claim is the REFERENT-FREE CONSISTENCY version
(forced by elimination, not chosen):**

> For a structured (matter-bearing, v18-type) config X — NOT the faithful
> point (its modular flow is trivial, K ∝ I) — compute the modular
> generators K_face for SEVERAL faces (E_11, E_22, E_33, and rank-2
> complements; all u-aligned). **Sharp question: does a single algebra
> direction generate all of them simultaneously (up to each face's
> compression)?** LIVE = the per-face thermal times are mutually consistent
> with ONE global time direction (an emergent state-defined time exists
> across faces); DEAD = the face flows are mutually inconsistent (thermal
> time is face-relative; no global emergent time from the state). Both
> branches informative; non-vacuous (consistency can genuinely fail);
> exact over Q on pre-registered configs.

Final non-blocking gate IF LIVE: compare the common direction against the
KKT so(4,2) candidates — labeled as an INTERPRETATION check (OD3 flag
inherited), not part of the verdict. Scope: LIVE upgrades J4 IMPORT →
PROGRAM-SUPPLIED-candidate (`entanglement-route.md` §10.4); it does not
give dynamics, and the run must not mention κ/Λ/G = κT.
