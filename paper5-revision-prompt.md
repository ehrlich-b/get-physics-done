# Paper 5 Revision: Close Load-Bearing Jigsaw-Piece Gaps

## Context

Paper 5 ("Quantum Mechanics from Self-Modeling") was submitted to the
Journal of Mathematical Physics on 2026-03-28 (JMP26-AR-00922) and
archived at Zenodo (DOI 10.5281/zenodo.19342703). It is currently 16+
days with the associate editor. No referee report yet.

While the paper is out, a jigsaw-piece-level review found six places
where the logical chain is sound to the eye but the author cannot
independently reconstruct the argument from primitives. One is
load-bearing; the rest are material. This milestone closes them before
the referee report lands, so revisions ship fast and survive reviewer
scrutiny.

The submitted version is frozen at git tag `paper5-jmp-submitted` and
copied to `landing/papers/qm-from-self-modeling/main-jmp-submitted.tex`
in the blog repo. Revisions will land in `main.tex`.

## Milestone goals

Close six jigsaw gaps in Paper 5, in this order:

1. **§3.3 Peirce preservation from OUS primitives** (this prompt; Phase 1)
2. **S4 facial structure lemma**: either precise Alfsen-Shultz citation or standalone proof
3. **Thm 5.8 upper bound**: W carries product-form sequential product (currently asserted)
4. **Phi inert-wrapper resolution**: stop equivocating across sections
5. **Lean axiom audit**: 16 axioms in the Lean formalization vs cited Alfsen-Shultz / van de Wetering statements
6. **Minimal composite assumption defense**: every adversarial reviewer flags this

Phase 1 is the only one scoped here. Subsequent phases will be spec'd as
Phase 1 closes.

## Phase 1 — §3.3 Peirce preservation

### The exact claim to prove or disprove

Paper 5 §3.3 (lines 508-528 of `main.tex`, subsection "The Corrected
Product via Peirce Feedback") argues that the sequential product
$a \circ b$ restricted to each Peirce subspace is an endomorphism of
that subspace. The key passage:

> "The Peirce decomposition with respect to the spectral projectors of
> $a$ decomposes $V$ into subspaces $V_2(p_i)$ and $V_1(p_i, p_j)$.
> Compressions project onto these subspaces (Alfsen-Shultz 2003), so
> linearity gives a block decomposition: $a \circ \cdot$ maps each
> Peirce subspace to itself."

**The claim to prove:**

> Let $V$ be a finite-dimensional spectral order unit space in the
> Alfsen-Shultz sense (order unit, compressions $c_p$ for every
> projective unit $p$, faithful normal states). Let $a = \sum_i
> \lambda_i p_i$ be a spectral decomposition of an effect $a \in V$,
> with the $p_i$ orthogonal projective units. Let
> $V = \bigoplus_i V_2(p_i) \oplus \bigoplus_{i<j} V_1(p_i, p_j)$ be
> the Peirce decomposition.
>
> Suppose $\mathord{\circ}: V \times V \to V$ satisfies the axioms
> S1 (additive in the second argument) and S3 (sharp constraint
> $a \circ b = c_a(b)$ when $a$ is a projective unit), and that
> $a \circ \cdot$ is a linear endomorphism of $V$.
>
> Then $a \circ V_2(p_i) \subseteq V_2(p_i)$ and
> $a \circ V_1(p_i, p_j) \subseteq V_1(p_i, p_j)$ for all $i, j$.

### What counts as success

Exactly one of the following:

**(A) Proof from OUS primitives only.** A complete proof using only:
- order-unit structure,
- compressions (with Alfsen-Shultz properties: idempotent, positive,
  $c_p + c_{p'} = \mathrm{id}$, Peirce decomposition),
- the axioms S1 and S3 as stated,
- linearity and finite-dimensionality.

The proof MUST NOT use:
- Jordan multiplication,
- Euclidean Jordan algebra structure,
- anything downstream of §3.3 (S4, S5, sequential product formula,
  $f(\lambda, \mu) = \sqrt{\lambda \mu}$, etc.),
- C\*-algebra structure,
- $h_n(\mathbb{C})$ or any specific EJA realization.

**(B) Precise citation to Alfsen-Shultz 2003.** Chapter, section, and
theorem/proposition number of a statement in *Geometry of State Spaces
of Operator Algebras* (Alfsen-Shultz, Birkhäuser 2003) that directly
proves the claim above. "Peirce decomposition exists" is NOT sufficient;
we need "the sequential product preserves Peirce subspaces" or an
equivalent statement that implies it from OUS primitives.

**(C) Counterexample or structural gap.** A construction showing the
claim does NOT follow from the stated primitives, OR an argument that
the proof requires Jordan structure one step earlier in the chain than
§3.3 currently allows. If (C), characterize the gap precisely: what
additional axiom or derivation step is required?

### Why this matters

If (A): §3.3 gets a one-paragraph lemma with a clean proof. Referee
cannot poke at it.

If (B): Add a precise citation. Two-line fix.

If (C): The paper has an ordering problem in its derivation chain.
§3.3 is leaning on a Jordan fact that only becomes available in §4 or
§5. This would require restructuring the logical spine of the paper -
either moving the Jordan-structure derivation earlier, or finding a
pre-Jordan argument for Peirce invariance, or accepting that §3.3
depends on a non-primitive assumption and stating that explicitly.

Outcome (C) is the kind of finding that absolutely must happen BEFORE
the referee does, not after.

### Failure modes to avoid

**Assuming the conclusion.** Saying "Peirce subspaces are preserved
because the sequential product is a Jordan-algebraic operation" uses
the very structure being derived. The whole point of Paper 5's strategy
is to get to Jordan algebras FROM sequential-product axioms, not the
other way around. If the proof has the form "since a∘b is a Jordan
product..." it has failed.

**Citing the Peirce decomposition theorem as if it proves Peirce
invariance of a∘(-).** The Peirce decomposition exists in any spectral
OUS (Alfsen-Shultz). That's a decomposition of the space, not a
statement about the sequential product's invariance properties.

**Confusing "compressions preserve Peirce subspaces" with
"a∘(-) preserves Peirce subspaces."** The first is an Alfsen-Shultz
result about individual compressions $c_{p_i}$. The second is a claim
about the composite map $b \mapsto a \circ b$, which is a different
object. One does not trivially imply the other.

**Rate-limiting on "it's obvious."** If the claim were obvious,
Paper 5 would not spend 20 lines asserting it. The paragraph at
lines 508-528 is doing real work; the question is whether it's
doing the work it claims to do, or whether it's waving.

### Deliverables

- `derivations/paper5-peirce-preservation/STATE.md` — working file
- `derivations/paper5-peirce-preservation/claim.md` — the claim restated
  in the derivation's own notation
- `derivations/paper5-peirce-preservation/attempt-NN.md` — one file per
  serious proof attempt (numbered, most recent last)
- `derivations/paper5-peirce-preservation/RESULT.md` — final outcome:
  (A), (B), or (C), with full proof / citation / gap characterization
- `derivations/paper5-peirce-preservation/alfsen-shultz-notes.md` —
  which specific Alfsen-Shultz theorems were consulted, with page
  numbers where accessible; what each does and does not establish

### Reference material

- Paper 5 source: `/Users/ehrlich/repos/blog/landing/papers/qm-from-self-modeling/main.tex`
  (frozen at git tag `paper5-jmp-submitted`; revision copy at
  `main-jmp-submitted.tex`)
- §3.3 content: lines 483-562 of `main.tex`
- Alfsen-Shultz axiom references cited: `\cite{AlfsenShultz2003}` throughout §2-3
- van de Wetering axioms S1-S7: referenced in §3.2, used throughout §3.3-3.5
- Paper 5 Lean formalization: `~/repos/research/lean/Paper5/` (0 sorry, 16 axioms)
- Previous GPD work on sequential product: `derivations/` entries from
  v2.0 (Sequential Product on OUS) — check whether that work already
  settled this or whether it assumed it

### Success criteria for Phase 1

- [ ] Claim stated precisely in derivation-native notation
- [ ] Serious attempt at proof from OUS primitives (allowed tools listed)
- [ ] If successful: proof verified, no prohibited structure used
- [ ] If citation found: exact theorem + page in Alfsen-Shultz 2003
- [ ] If structural gap: gap characterized, minimum additional structure
      identified, explicit statement of what ordering change Paper 5
      would need
- [ ] Adversarial review of the outcome (second agent, fresh eyes)
- [ ] RESULT.md with recommended revision text for §3.3

### What happens after Phase 1

Outcome (A) or (B): Phase 1 closes. Milestone proceeds to Phase 2
(S4 facial structure lemma). Paper 5 §3.3 receives the fix as part of
the revision response to referees.

Outcome (C): Phase 1 closes but flags a larger structural issue.
Milestone pauses for human decision on whether to restructure §3.3,
add an explicit assumption, or rip out the current argument and find
a different route. This decision is above GPD's pay grade.

## Milestone notes

- The program's author (Bryan Ehrlich) is an independent researcher,
  software engineer by trade, understands the math at "jigsaw piece"
  level. The whole point of this milestone is that the author cannot
  hold these pieces independently and needs them made solid before the
  JMP referee report arrives.
- No shortcut via "Bryan's intuition says X." The milestone exists
  because intuition is insufficient here; we need proofs or precise
  citations.
- Prior Paper 5 work happened in GPD v2.0 (Phases 4-6). If any of that
  work already established (A), promote it. If it assumed the claim,
  flag it.
- The author is blunt; GPD should be too. If the claim fails, say so.
