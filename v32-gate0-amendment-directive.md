# v32.0 GATE-0 AMENDMENT DIRECTIVE (v32.0-A) — multiplet-ID flag, paste before Gate 3

**Status: machinery amendment at Gate 0, BEFORE the evidential gates run. This is not a
new physics claim and not a STOP — it is the registered repair of an unsound mid-run
criterion rewrite, plus the discriminating test that settles the multiplet ID.**

## The flag (from the blog-side audit, independently computed)

Commit e295f0ce rewrote the Gate-0 gram criterion from `rank == 8` to
`rank == 6 AND N-rank == 8`, justified as "single generators probe a rank-6 d-symbol
slice." That justification is **false**: the d-symbol image of single generators
{N(λ_a) = d_aac λ_c} lies in the Cartan span{λ₃, λ₈} — rank **2**, not 6. Your own
75d6639d docstring said exactly this ("spans only rank 2"), and the blog side verified
it numerically. So the observed single-generator residue Gram rank 6 has NO explanation
under the registered direction hypothesis c(M) ∝ N(M): a pure d-channel residue map
predicts Gram rank 2 on single generators. Rank 6 is a 4-dimensional excess. Rewriting
the gate to bless the observed number without a correct theory of it is the
designed-in-verdict bug class (trap #17/#18 territory; STOP rule 3 polices exactly this).

## The candidate explanation (fits every number; independently computed blog-side)

The residue map M ↦ TT(B3[M])^{(1,1)} is quadratic in M and SU(3)-equivariant, so its
target decomposes through Sym²(8) = 1 ⊕ 8 ⊕ 27, each multiplicity ONE. The d-channel
(8) is what v31 assumed. The **27-channel** was never excluded — and the numbers match it
in a three-point signature:

| probe set | 27-channel predicted Gram rank | d-channel predicted | observed |
|---|---|---|---|
| 8 single Gell-Mann | **6** | 2 | **6** (your gate) |
| 8 dense generic (m1..m8) | 8 | 8 | (both predict 8 — non-discriminating) |
| 11 probes (below) | **9** | caps at 8 | **← the test** |

Independent blog-side computation: rank{P27(λ_a ⊗ λ_a)} = 6 exactly (P27 = Sym² minus
the trace part minus the (3/5)·d-projector part; d_abe d_cbe = (5/3)δ_ac verified).

Supporting consistency: (i) **Koiso rigidity** (Besse 12.98) forbids ANY TT mode at
2Λ = 12 on CP², so the v31 "λ=12 dim-8 Boucetta" reading was paradoxical on its face —
plausibly the (1,1) TT spectrum has NO dim-8 multiplet at the bilinear level and the
d-channel has nowhere to land; (ii) each t_a is an exact Δ_L^{(1,1)} eigentensor at
λ_L = 32 (your 0.dL/Schur), which gauge contamination would not produce — the residues
are clean single-eigenvalue multiplet content; (iii) Sym²(8) ⊃ 27 with multiplicity one,
so the v31 rep-theory deficit-1 lock transfers verbatim to the 27-channel — **the v31
LIVE verdict is untouched either way**; only the multiplet NAME would amend
(dim-8 → dim-27 at λ_L=32).

**Channel-robustness of the verdict center (blog-side, hand-checked):** for traceless
3×3 M every degree-4 invariant collapses to (TrM²)² (Cayley–Hamilton: TrM⁴ = ½(TrM²)²,
detM·TrM = 0), and |P27(M⊗M)|² is degree-4, so ‖TT(B3)‖² = κ·(TrM²)² is the forced form
in EITHER channel. v32's verdict center survives the swap unchanged.

## Why this must be settled before Gate 3

The frozen basis {t_a} (8 single-generator residues) spans only a 6-dim slice. If the
multiplet is the 27, the symbolic-M residue sweeps dimensions outside that slice, Gate 3a
comes out INCONSISTENT, and verdict() mislabels it STOP-"contradicts-v31" — a spurious
halt with a false post-mortem. Gates 1 and 2 are channel-agnostic (Schur and
ε = λ_L − 12 = 20 are about the eigenvalue, not the dim) and may stand as run.

## THE DISCRIMINATOR (run now; one rank, total discrimination)

Extract the TT residues for THREE more sparse probes (fast CRT, ≤4 nonzero entries each):

    M9  = λ1 + λ2,    M10 = λ1 + λ3,    M11 = λ1 + λ4

Build the 11×11 L² Gram of {t_1..t_8, t_9, t_10, t_11} ((1,1) blocks, same l2_tensor
path) and take its rank, exact over Q.

- **rank ≥ 9** ⇒ the multiplet is BIGGER than dim-8: dim-8 ID dead unconditionally.
  Predicted value under the 27-channel: exactly **9** (blog-side: rank{P27 of these 11
  probe-squares} = 9). A match on the exact value is the signature.
- **rank ≤ 8** ⇒ the 27 story is refuted too; then the rank-6 needs a third explanation —
  first suspect: divergence contamination of the (1,1) truncation (check div(t_a) = 0
  directly on the truncated blocks, which the current flags do NOT certify — they certify
  the FULL r pre-truncation). Report and HOLD for a blog-side decision.

Also run (cheap, confirms cleanliness): Schur on t_9..t_11 — all should give the same
λ_L = 32.

## IF THE 27 CONFIRMS (rank = 9): the registered repair

1. **Amend Gate 0 (explicitly, as v32.0-A; no silent rewrites):** the verdict-object (i)
   direction hypothesis becomes c(M) ∝ P27(M⊗M) (the 27-channel; multiplicity-one forced,
   same rigidity). The multiplet ID becomes "the λ_L=32 (1,1)-Hermitian dim-27 multiplet."
   The gram criterion becomes the three-point signature: singles rank 6 = rank{P27
   singles}, 11-probe rank 9, AND the polarized basis below reaching rank 27.
2. **Gate-3 basis repair:** the residue map is an exact quadratic form in M (B3 bilinear
   in dφ_M; extraction linear), so polarize: r_ab := (r(λ_a+λ_b) − r(λ_a) − r(λ_b))/2 for
   a<b. The 8 diagonals + 28 polarized pairs span the full multiplet (the P27 images of
   {λ_a ⊙ λ_b} span all 27 dims). All sparse extractions. Freeze THAT as the Gate-3 basis
   (or any rank-27 subset), then run 3a/3b/3c as registered. The closed-form target:
   TT(B3[M]) = c · T[P27(M⊗M)] with T the polarization-built equivariant map and c ONE
   forced constant; norm identity ‖TT(B3)‖² = κ(TrM²)² unchanged.
3. **Literature re-map (Gate 2 documentation):** locate the (1,1) dim-27 TT multiplet at
   λ=32 in Boucetta's tables; identify what his λ=12 dim-8 row actually is (gauge sector /
   non-TT / different convention) and resolve the Koiso paradox of the v31 reading
   explicitly in RESEARCH. In-rep numbers remain authoritative (trap #18).
4. **v31 amendment note (for the close-out, not now):** v31's verdict objects stand
   (TT residue exists, nonzero, (1,1), deficit-1); the multiplet attribution amends
   dim-8 → dim-27 at λ_L=32. The deferred-exhibit obligation is discharged by the
   explicit t_a's either way.

## Fences (unchanged)

Same scope fence as registered: deformation-complex dictionary of a frozen imported
geometry; no dynamical metric, no selection law, no κ, no Einstein-equation language.
The 8-vs-27 question is a machinery/ID question inside Block B. Exact arithmetic over Q
throughout. If anything here conflicts with what the run has already committed past
Gate 2, HOLD and report rather than reconcile silently.
