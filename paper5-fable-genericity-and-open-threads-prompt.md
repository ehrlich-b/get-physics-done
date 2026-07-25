# Fable brief — the open threads after the Conservation No-Go (2026-06-30 → run 2026-07-01)

You are Fable (the highest-capability model), coming in fresh on a hard foundations problem. A
Claude↔Codex correspondence + 4 adversarial reviewers converged yesterday; your job is the threads
they did NOT close. Read `research/paper5-virtuous-loop-three-joints.md` §18 first (the full context),
then this. Anti-glaze is the house rule. Ground every claim (published result / formal statement /
explicit witness / honest [PHILOSOPHICAL]/[STRUCTURAL-CORRESPONDENCE] tag).

## The program in one paragraph
Two axioms: **(A) self-modeling** — a system contains a structure-preserving representation of its own
operationally accessible state+effect structure; **(B) relativity of isomorphism** — physical counting
is over isomorphism classes, weight `1/|Aut(x)|`. Dream: derive complex QM from A+B. Status: a
two-import labeled synthesis — self-duality → Jordan, central-i/local-tomography → complex — both
imports proven irreducible by explicit exact-arithmetic witnesses (Vinberg cone, Niestegge ℓ⁴ qubit,
rebit `M_n(ℝ)`, quaternionic).

## What is CLOSED — do NOT re-litigate
**Can self-modeling force the Jordan step (self-duality, `K≅K*`)?** NO, exhaustively: static,
dynamical (Candidate C has a continuous reversible `T²` flow yet is non-self-dual), recursive
(Conservation No-Go: intrinsic self-modeling operations re-encode conserved invariant fibers but never
erase them while faithful — `Fix(F)=⋃_s Fix(F_s)`; a conserved self-label is idempotent under
re-representation, so no Lawvere/Gödel diagonal bites), purification (self-models admit ontic classical
mixedness), and *every* known GPT reconstruction lever (all reduce on homogeneous cones to
pure-state-transitivity → BUvdW → self-dual). The gap between self-modeling and QM is exactly the
state↔effect symmetry, which is exactly radical relativity, which is exactly the universal selector of
the whole reconstruction program. Self-modeling is CONSERVATIVE. This is settled; don't reopen it.

## Your targets, in priority order

### ★ THREAD 1 — GENERICITY / measure-dominance (the game-changer; could win WITHOUT forcing)
Every "kill" above shows non-quantum self-models EXIST. But **axiom B is a counting measure** (`1/|Aut|`),
and it has only ever been deployed as "symmetry-completion" (correctly killed: quotienting ≠ completion).
It has NEVER been deployed as what it literally is: a **measure on the space of self-models / presentations**.
**The question:** under B's `1/|Aut|` weighting (groupoid cardinality) over the space of finite-dim
self-models (or over presentations of a given self-model, or over histories), is **complex QM generic /
measure-dominant, and are the non-quantum witnesses (Vinberg, rebit, Niestegge, ontic-mixedness)
measure-zero or non-generic?** If yes, the dream is rescued in a DIFFERENT currency — QM is not *forced*
but is *what you almost surely are* — and the witnesses become measure-zero curiosities, exactly the
"exotic self-modeler" bracket the paper already wants.
- Read `research/qm-genericity-review/state_of_research.md` FIRST — the program has a genericity file;
  find what was tried, what's alive, what's dead. Do not re-report dead routes as live.
- Sharpen the measure: over WHAT ensemble? (a) all simple EJAs / all order-unit spaces of dim ≤ N;
  (b) presentations of one self-model weighted `1/|Aut|`; (c) self-model *histories* (τ-towers) weighted
  by groupoid cardinality. Which ensemble makes the question well-posed AND non-circular?
- The honest trap to pre-empt: `1/|Aut|` *disfavors* high symmetry (more automorphisms → less weight),
  and QM's state space is highly symmetric — so naively B pushes AWAY from QM. Resolve this head-on: is
  there a formulation where the weighting nonetheless concentrates on the complex/Jordan locus (e.g.
  because non-quantum homogeneous cones are non-generic among homogeneous cones; or because the
  *history*-measure penalizes the self-opaque `r(k)→0` families)? Or does the tension kill genericity too?
- Deliverable: is genericity (i) a live rescue with a concrete well-posed measure + a computable test
  case, (ii) dead for a stated reason, or (iii) needs one specific computation to decide (specify it,
  exact-arithmetic if possible)?

### THREAD 2 — the COMPLEX constitutive door (recursion → observable generator)
Distinct from the (closed) Jordan door. The recursive fixed point `ρ*=R(M(ρ*))` must fold in the
generator `i[ρ,H]` of your own becoming; `i[ρ,H]∈V ⟺ complex`; the rebit "caps at level 2" (faithful
SO(n) becoming, generator ∉ V). Catalogue `:46-68`, graded [STRUCTURAL-CORRESPONDENCE]. **Does full
recursive self-consistency (a self-model that models its own modeling-*dynamics*, not just its states)
FORCE the generator observable?** Or does the rebit survive it too (as it survives every static
strengthening)? Be precise about what "model your own dynamics recursively" adds beyond "keep faithful
SO(n) records" (which the rebit already does). If it collapses to the rebit again, say so and show it.

### THREAD 3 — the Jordan constitutive door (philosophy, last resort)
"Self-modeling *means* no-preferred-state" as a constitutive principle (like accepting Einstein's
relativity principle rather than deriving it). All *operational* versions died (the preferred-state
label is intrinsic reachability data, readable from inside, no external chart needed). What survives is
a philosophy-of-physics argument. Make the STRONGEST honest case that the no-preferred-state symmetry is
constitutive of self-modeling under radical relativity — or conclude cleanly that it's an irreducible
postulate (which vindicates the two-axiom framing honestly). Tag [PHILOSOPHICAL] where grounding runs out.

### THREAD 4 (only if time) — joint axiom coupling
The self-model represents its own `Aut(B)` (part of B's structure), and B weights by `1/|Aut(B)|`. Is
there a self-consistency condition from coupling the measure to the self-modeled automorphism structure?
Likely related to Thread 1; note any connection.

## Output
For each thread: LIVE (with the concrete next computation/argument) / DEAD (with the reason + witness) /
NEEDS-ONE-COMPUTATION (specify it). Rank by breakthrough potential. If Thread 1 (genericity) is live,
that is the headline — it's the only route that wins without forcing. Cite `file:line` for repo claims
and arXiv ids for external results.
