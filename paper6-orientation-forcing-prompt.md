# GPD Prompt: Is the MacDowell-Mansouri ε-contraction forced by the FORCED ANTISYMMETRIC data (u=e_7 complex structure + V_{1/2} chiral sector) that Phase 78 did not exploit?

## State recovery (read first - this milestone attacks the EXACT shortfall v18 closed on)

**The program.** Self-modeling -> QM (Paper 5, the firewall, at JMP, the only solid
theorem) -> h_3(O) basin + SM gauge data (Paper 7) -> GR (the open endpoint). This
task attacks the endpoint, surgically.

**The GR graveyard (do NOT reanimate):**
- det/GST/Weinberg-1964 (`47-*`..`50-*`,`53-*`): the massless spin-2 IS found (Phase
  50: det_2 perturbation, 10=9+1 under SO(3,1), no Fierz-Pauli mass, universal V_{1/2}
  coupling) but `-R/2` is then forced via an **assumed minimal-coupling / N=2 SUSY
  closure** = circular. The spin-2 existence is NOT the open question.
- cone-Hessian bulk geometry (v17.0, Ph 70-73): **NONE** - the symmetric (Jordan / real
  part of QGT) metric is not an Einstein object.
- Cartan/MM torsion-free connection (v18.0, Ph 74-78): **`fp-imported-action`** -
  `F=dA+A∧A` has Lorentz block == the genuine Levi-Civita Riemann of `g=e·e` (6/6 exact,
  torsion=0), curved + matter-sourced + a FORCED SO(3,1) coframe, but **(Ph77 dynamical)**
  `G[g]` is not `κT+Λg` for any global `(κ,Λ)`, and **(Ph78 action)** the MM ε-contraction
  that would give Einstein-Hilbert is **not forced** by the trace form / cubic norm.
- ensemble/thermodynamic (Jacobson/Verlinde/Vanchurin): REJECTED as woo. No entropy, KMS,
  modular/thermal time, or "many observers" arguments anywhere.

**The precise Phase-78 shortfall this milestone targets.** Phase 78's `fp-imported-action`
rested on a deterministic 3-clause verdict ladder, ALL THREE of which failed, and they all
failed for ONE structural reason: **the audited intrinsic data (`Tr(X∘Y)` and `det_3`) is
SYMMETRIC, and a symmetric tensor cannot build the antisymmetric orientation ε.** Concretely
(78-circularity-audit.tex, exact over Q):
- **(C1)** the bare so(3,1)-invariant quad-in-curvature 4-form space is **2-dim** (Euler ε +
  Pontryagin); the η-tensorial intrinsic subspace is **1-dim = Pontryagin only**, NOT ε.
- **(C2)** ε is reachable only as the metric volume form `√|det η| ε`; its **orientation
  (sign) is a by-hand discrete choice**, not fixed by the symmetric `Tr/det_3`.
- **(C3)** the EH normalization is free: **`det_3 ≡ 0` identically on the soldered Lorentz
  block `[1,2,3,10]`** (the cubic norm couples `x_1` to `α`, which is OUTSIDE the block), so
  `det_3` pins no scale there.

**The hypothesis (genuinely new - the one forced data class Phase 78 left on the table).**
Phase 78 audited the SYMMETRIC data on the V_0 Lorentz block. Two pieces of **forced,
ANTISYMMETRIC / chiral** structure were never used as orientation/normalization sources:

1. **`u = e_7`, the complex structure** (`J^2 = -1`). `u` is already admitted intrinsic data
   (it DEFINES the slice `h_2(C_u) ≅ R^{3,1}` via `π_u`; Phase 46/75). A complex structure
   **canonically orients** a manifold (a complex manifold has a preferred orientation; the
   Kähler 2-form `ω_K(·,·)=g(J·,·)` gives `vol = ±(1/2)ω_K∧ω_K` with a FORCED sign). So `u`
   is exactly an **antisymmetric** object that can fix the orientation **sign** that the
   symmetric `η` (C2) could not. This is not new data - it is exploiting `u` as an orientation,
   which Phase 78 did not do.
2. **The `V_{1/2}` chiral sector**, where `det_3 ≠ 0`. The cross-term coupling
   `C_{(V_{1/2})(V_{1/2})(V_0)}` is the **96-entry nonzero block** (Phase 49/50) with a clean
   chirality structure (`C_{i,i,18} = -1/6` for i=1..8, `+1/6` for i=9..16; the a=26 off-diag
   pairing is `e_7`-linked). Unlike the Lorentz block where `det_3 ≡ 0`, the cubic norm is
   **alive** when `V_{1/2}` is involved - so `V_{1/2}` is the natural place to look for the
   normalization (C3) the Lorentz block couldn't supply. In Einstein-Cartan, the chiral
   `V_{1/2}` spin **sources torsion** (`d_ω e = T[V_{1/2}] ≠ 0`), which v18 set to zero - so
   the torsionful connection is genuinely untested.

**Claim to prove or disprove (one sentence).** The forced antisymmetric data - the complex
structure `u=e_7` and the chiral `V_{1/2}` torsion source - supplies the orientation (repairs
C2) and/or the normalization (repairs C3) that the symmetric `Tr/det_3` could not, **forcing
the MM ε-contraction** (STRONG WIN: flips v18's `fp-imported-action` to a derivation of
Einstein-Hilbert); OR it does not, and the milestone returns a **named, triangulated negative**
identifying which Phase-78 clause survives even with the antisymmetric data.

## Fail-fast gate ladder (cheap kill FIRST - do not enter full ceremony unless Gate A survives)

**GATE A - the cheap kill (~minutes, exact over Q; run BEFORE any plan/requirements ceremony).**
Construct the endomorphism `J` on the 4d slice tangent space induced by `u=e_7` (same `π_u`
mechanism that reduced `V_0→h_2(C_u)` and `V_{1/2}`). Decide, exact over Q:
- (A1) `J^2 = -1` on the 4d slice (genuine almost-complex structure), and `J` is compatible
  with the soldered `(1,3)` `η` (i.e. `J ∈ so(3,1)` or the appropriate compatibility);
- (A2) the induced orientation is **forced / sign-definite**: `ω_K∧ω_K = c·vol` with the sign
  of `c` fixed by `u` (not a free choice).
**KILL CONDITION:** if `J^2 ≠ -1`, OR `J` is incompatible with `η`, OR the orientation sign is
NOT fixed by `u` (still ambiguous) - then `u` supplies nothing the symmetric data didn't, the
antisymmetric-data route is dead, **STOP and report `fp-no-intrinsic-orientation`**. No
requirements doc, no further phases.

**GATE B - does u repair Phase-78 (C2)?** If Gate A survives: is the `u`-forced orientation
ε **equal (up to positive scale)** to the metric volume form ε appearing in the EH term
`ε_{abcd} R^{ab}∧e^c∧e^d`? I.e., is the orientation now **intrinsic** (from `u`) rather than
by-hand? Report C2 = REPAIRED or C2 = SURVIVES (with reason).

**GATE C - does V_{1/2} repair Phase-78 (C3)?** Compute whether the chiral `V_{1/2}` sector
(where `det_3 ≠ 0`; the 96-entry `C_{(V_{1/2})(V_{1/2})(V_0)}` block, optionally sourcing
torsion `T[V_{1/2}]`) supplies a **fixed normalization** for the ε-contraction (the `→1/16πG`
scale). Report C3 = REPAIRED or C3 = SURVIVES.

**GATE D - the verdict (reuse Phase 78's deterministic ladder).** Re-run the Phase-78
`verdict(triple)` map with the C2/C3 statuses from B/C and a re-examined C1 (does forcing ε
via `u` make the trace-form-invariant subspace effectively 1-dim-generated-by-ε, or does
Pontryagin still coexist?). Output:
- **STRONG WIN** iff C1 ∧ C2 ∧ C3 all now pass = the ε-contraction (hence `-R/2`) is FORCED by
  the intrinsic `(Tr, det_3, u, V_{1/2})` data = Einstein-Hilbert derived, v18 flipped.
- **`fp-imported-action` (refined)** otherwise, naming exactly which clause survives (the most
  likely outcome: C2 repaired by `u`, C1/C3 survive = "orientation now forced, coupling still
  imported").

**Woven diagnostic (the googly / chirality - cheap, run alongside Gate C).** Phase 78 found
Pontryagin `≡ 0` on the DIAGONAL Phase-77 metric (non-chiral). Recompute the Pontryagin density
(= the self-dual/anti-self-dual imbalance `|W+|^2 - |W-|^2`) for a **GENERAL (non-diagonal)**
`M ∈ V_{1/2}`, with torsion sourced by the chiral `V_{1/2}`: is it nonzero, and does it
**track V_{1/2}'s 8+8 chirality** (flip the chirality, flip the sign)? Chiral = the googly is
real and the missing half is named (the opposite-chirality completion). Non-chiral = drop it.
This is diagnostic only; it does not gate the verdict.

## Hard input ban (inherit v18.0 + one addition)

Inherit ALL v18.0 / CONVENTIONS.md locks verbatim:
- **det SSOT = `code/ring_lemma_verification.py det_3`** (cross-term `2Re(x2* x0* x1)`,
  F_4-invariant via 324/324). **`code/octonion_algebra.py` BANNED** on every decisive path.
- **EXACT over Q** on all verdicts; ranks via `sympy.Matrix.rank()`, **never `numpy.linalg`**;
  the `i` of `u` carried symbolically over `Q(i)` (Re/Im split), never float.
- signature mostly-minus `(+,-,-,-)`, `η = diag(+1,-1,-1,-1)`; `E_11 = diag(1,0,0)`;
  Peirce `{0,1/2,1}`; spacetime block engine indices `[1,2,3,10]`, `V_{1/2} = {11..26}`,
  `u = e_7`.
- gravity = the Lorentz block `R[ω]` of `F = dA + A∧A`, `A = ω ⊕ (1/ℓ)e`, `e = π_u(dE)`.
- **NO posited MM/EH action**, no `∫ ε F∧F` as an assumed action, no `-1/2`/`16πG` coupling
  put in by hand, no SUSY/GST Lagrangian, no Jacobson/thermal. The forced determination may
  use ONLY `Tr(X∘Y)`, `det_3`, the Peirce decomposition under `E_11`, the `C_u/π_u` reduction,
  **`u=e_7` as a complex structure**, the `(E_11,u)`-forced `so(3,1)`, the `V_{1/2}` couplings,
  and standard differential geometry. Reuse the Phase-78 `input_ban_guard()` (AST + source
  string strip + `sys.modules`).
- **ADDITION (the new fp tripwire):** `fp-imported-orientation` - the orientation ε must come
  from `u` intrinsically; if it is asserted, tuned, or sign-picked by hand, that is the import
  under audit, exactly as the action was in Phase 78. The Gate-A/B computation must SHOW `u`
  fixes the sign, not assume it.

**Non-circularity note (state it explicitly in the derivation).** `u` is not new data: it is
the same forced complex structure that defines the slice (`h_2(C_u)`, Phase 46) and was already
admitted by Phase 78's input ban. This milestone uses `u` as an **orientation source**, a use
Phase 78 did not make. That is a legitimate exploitation of already-forced structure, not an
import - and Gate A is precisely the test that `u`'s orientation is forced (sign-definite), not
chosen.

## Reuse the warm engines (do NOT rebuild)
`code/ring_lemma_verification.py` (det SSOT), `code/cartan_phaseA_coframe.py` (the forced
`so(3,1)` coframe + `π_u`), `code/cartan_phaseB_curvature.py` (the `R[ω]` Riemann), and
`code/cartan_phaseC_contraction.py` (the Phase-78 invariant-count engine + `verdict()` ladder +
`input_ban_guard`). Gate A adds only the `J = π_u`-induced complex structure and its Kähler
form; Gates B/C/D extend the existing `cartan_phaseC` invariant count with `u` (orientation) and
the `V_{1/2}` block (normalization).

## Verdict reporting (negative-result-is-success, at true strength)
Report at true strength - neither inflate a partial into a win nor deflate a genuine win.
The verdict() map must remain non-hardwired: a genuinely forced triple (C1 ∧ C2 ∧ C3 all pass
with `u`/`V_{1/2}` supplying orientation+normalization) returns STRONG WIN; any surviving
shortfall returns refined `fp-imported-action` with the clause named. Either outcome is a
publishable closure: a WIN derives Einstein-Hilbert; a refined negative completes the
triangulation (symmetric-V_0 NONE / Lie-V_0 fp-imported / antisymmetric-u+V_{1/2} fp-X) that
grounds the "gravity is separate" (Penrose/'t Hooft) conclusion by closing the last unexploited
data class.

## Honest scope (carry into the verdict)
Most likely outcome: **C2 repaired by `u` (orientation now forced), C1/C3 survive** = a refined
negative, a real advance on v18 but not a derivation. Quick kill possible at Gate A (`u` may not
descend to a sign-definite orientation on the `(1,3)` slice). STRONG WIN (Einstein forced) is the
low-probability tail. The deepest residual risk even if C2/C3 pass: forcing ε as an *invariant
tensor* is not yet forcing `∫εF∧F` as *the action* (the variational principle) - flag this in
Gate D as the boundary between "ε forced" and "action forced," and do not let "ε is now a forced
invariant" silently inflate into "the EH action is derived."
