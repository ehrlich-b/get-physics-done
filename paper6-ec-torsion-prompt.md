# GPD Prompt: Does Einstein-Cartan torsion sourced by the chiral V_{1/2} spin close the v18 Einstein gap? (the last un-run gravity computation)

## State recovery (read first - this is the one route the triangulation did NOT execute)

**The program.** Self-modeling -> QM (Paper 5, the firewall, at JMP, the only solid
theorem) -> h_3(O) basin + SM gauge data (Paper 7) -> GR (the endpoint). This task
runs the single gravity computation that was set to zero in v18 and never executed.

**The gravity graveyard (do NOT reanimate):**
- det/GST/Weinberg-1964 (`47-*`..`50-*`,`53-*`): -R/2 forced via an assumed
  minimal-coupling / N=2 SUSY closure = circular. (Note: Weinberg-**1964** "given a
  massless spin-2, force -R/2" is a DIFFERENT theorem from Weinberg-**Witten 1980**;
  do not conflate.)
- cone-Hessian / symmetric / V_0 (v17.0, Ph 70-73): **NONE** - not an Einstein object.
- Cartan-MM / Lie / V_0, **TORSION-FREE** (v18.0, Ph 74-78): **fp-imported-action** -
  Ph77 used the torsion-free Levi-Civita `omega(e)`, verified `d_omega e = 0` exactly,
  computed `R[omega]` = the metric Riemann of `g = e.e`, and found `G[g]` is NOT
  `kappa T + Lambda g` for any single global `(kappa,Lambda)` (tensor-support mismatch:
  `G` on 16 components, `kappa T` on 6; per-point `Lambda` varies). Ph78: the MM
  epsilon-contraction is not forced.
- antisymmetric / u-orientation (v19.0, Ph 79): **fp-no-intrinsic-orientation** -
  (1,3) admits no compatible almost-complex structure.
- ensemble/thermodynamic (Jacobson/Verlinde/Vanchurin): REJECTED. No entropy, KMS,
  modular/thermal time, "many observers."

**The precise un-run gap.** v18 Ph77 set **torsion to zero by hand** (it used the
torsion-free `omega`). The Einstein-Cartan (EC) version - where the chiral `V_{1/2}`
spin **sources torsion** (`d_omega e = T[V_{1/2}] != 0`) - was NEVER computed; v19
demoted the torsion sub-question to "diagnostic only, does not gate the verdict." So
**no phase has ever computed `G = kappa T` with torsion ON.** The v18 NEGATIVE is a
statement about the **torsion-free** Einstein tensor and does not bind the torsionful
one: EC splits the field content into the symmetric Einstein equation PLUS an
independent algebraic spin-torsion equation, and the v18 tensor-support mismatch is
exactly the kind of defect a spin-current contribution (Belinfante-Rosenfeld, on the
antisymmetric components) could fill. The source is demonstrably in the algebra: the
96-entry `C_{(V_{1/2})(V_{1/2})(V_0)}` block with its chirality structure
(`C_{i,i,18} = -1/6` for i=1..8, `+1/6` for i=9..16; the `a=26` off-diagonal pairing
is `e_7`-linked).

**Claim to prove or disprove (one sentence).** The chiral `V_{1/2}` spin current,
sourcing torsion via the algebra's OWN intrinsic coupling (the `C` block, NOT a posited
EC/Palatini action), makes the torsionful Einstein tensor `G_EC = kappa(T_canonical +
T_spin) + Lambda g` close with a SINGLE GLOBAL `(kappa,Lambda)` against the same
AST-guarded independent stress-energy v18 used (**STRONG WIN: Einstein-Cartan gravity
derivable from h_3(O)**); OR it does not, and the triangulation is sealed to four
corners with the exact reason named (expected: torsion is algebraic/non-propagating, so
the vacuum-order mismatch survives).

## Fail-fast gate ladder (cheap kill FIRST)

**GATE 0 - the cheap kill (~minutes, exact over Q; run BEFORE any ceremony).**
Compute the spacetime torsion `T[V_{1/2}]` as the `V_{1/2}` spin current contracted
through the intrinsic `C_{(V_{1/2})(V_{1/2})(V_0)}` block (the algebra's own coupling).
Decide, exact over Q:
- (G0a) `T[V_{1/2}]` is NONZERO (the algebra actually sources torsion);
- (G0b) it is **chirality-tracking**: flip the 8<->8 `V_{1/2}` labeling, the torsion
  flips sign;
- (G0c) **THE non-circularity gate**: the spin-torsion coupling coefficient is FIXED by
  the intrinsic `C` block (read from the algebra), NOT a free constant that must be
  posited. If the coefficient is free / must be put in by hand, that is the SAME import
  v18 Ph78 audited.
**KILL/VERDICT CONDITIONS:** if `T=0` (G0a fails) OR torsion is parity-blind (G0b
fails), EC adds nothing -> **STOP, the torsion-free v18 verdict is robust, triangulation
complete.** If the coupling must be posited (G0c fails) -> **STOP, `fp-imported-action`
(consistent with Ph78), the algebra does not intrinsically fix the torsion dynamics.**
No requirements/roadmap, no Gate 1, in either stop case.

**GATE 1 - the decisive test (only if Gate 0 fully survives).** Assemble the EC
connection `omega_EC = omega_LC(e) + K(T)` (contorsion `K` from the algebra-sourced
torsion `T`), recompute the curvature and the **full nonlinear** Einstein tensor
`G_EC = Ric(omega_EC) - (1/2) g R(omega_EC)`, and test, exact over Q, over the same
12-point `(M,x)` family v18 Ph73/77 used: does
`G_EC = kappa(T_canonical + T_spin) + Lambda g` hold for a SINGLE GLOBAL `(kappa,Lambda)`
against the AST-guarded independent `T[M]` (PRIMARY `T[psi=2Re((x2 x1) x3)]` + ALT
sigma-model `T[V_{1/2}]`), with `kappa` frozen from the intrinsic `V_{1/2}` cross-terms
BEFORE `G` is touched?
- **CLOSES** (single global `(kappa,Lambda)`, both `T`): **STRONG WIN** - Einstein-Cartan
  gravity is derivable from h_3(O). Re-verify independently before any celebration.
- **FAILS** (no global `(kappa,Lambda)`; per-point `Lambda` still varies; or the `M=0`
  vacuum mismatch persists because algebraic torsion vanishes there): the v18 negative is
  **robust to torsion** -> the gravity triangulation is COMPLETE. Record the EXACT reason
  (expected: torsion is algebraic / non-propagating, so it cannot repair vacuum-order
  curvature, and the tensor-support mismatch survives at `M=0`-adjacent orders).

## Hard input ban (inherit v18.0/v19.0 + the EC-specific guard)

Inherit ALL locks: det SSOT `code/ring_lemma_verification.py det_3` (cross-term
`2Re(x2* x0* x1)`); **`code/octonion_algebra.py` BANNED**; **EXACT over Q**, ranks via
`sympy.Matrix.rank()`, **never numpy**; signature mostly-minus `(+,-,-,-)`,
`eta=diag(+1,-1,-1,-1)`; `E_11=diag(1,0,0)`; Peirce `{0,1/2,1}`; spacetime block engine
indices `[1,2,3,10]`, `V_{1/2}={11..26}`, `u=e_7`; gravity = the curvature of
`A = omega (+) e`, `e = pi_u(dE)`.

**EC-specific non-circularity guard (the load-bearing one):** the torsion `T` and its
spin-torsion coupling must be **READ from the intrinsic `C_{(V_{1/2})(V_{1/2})(V_0)}`
block and the Peirce products** - NOT from a posited Einstein-Hilbert-Palatini / EC
action, NOT from an assumed `kappa_torsion`. If the construction requires positing the
EC action or a free torsion coupling, that is `fp-imported-action` and Gate 0 (G0c)
must catch it. `kappa` for the Einstein equation is frozen from the `V_{1/2}`
cross-terms BEFORE computing `G` (reuse the Ph73/77 AST-guard / `source_guard` so no
`Ric`/`R`/`G` leaks into the `kappa`/`T` definition). No thermal, no SUSY, no GST
Lagrangian, no `-1/2`/`16piG` by hand.

## Reuse the warm engines (do NOT rebuild)
`code/ring_lemma_verification.py` (det SSOT); `code/cartan_phaseA_coframe.py` (the forced
`SO(3,1)` coframe + `pi_u`); `code/cartan_phaseB_curvature.py` (Riemann from a connection
- extend it to accept a contorsion `K(T)` so `omega_EC = omega_LC + K`);
`code/cartan_phaseB_einstein.py` (the `G = kappa T + Lambda g` global-fit test + its
AST-guard - reuse the single-global-`(kappa,Lambda)` fitter and the independent `T[M]`);
`code/cartan_phaseC_contraction.py` (the invariant/`verdict()` machinery). Gate 0 adds
only the `T[V_{1/2}]` spin-current contraction through the `C` block; Gate 1 adds the
contorsion `K(T)` into the existing curvature + Einstein-fit pipeline.

## Verdict ladder (negative-result-is-success, at true strength)
Three outcomes, reported at true strength, non-hardwired:
1. **STRONG WIN** - Gate 1 closes with a single global `(kappa,Lambda)` against both `T`.
   Einstein-Cartan gravity derived. (Independent re-verification mandatory.)
2. **Triangulation complete (NEGATIVE)** - Gate 1 fails; record the exact tensor-support
   / vacuum-order reason. v18's Lie-sector verdict is now robust to torsion; "gravity is
   separate" is a genuine four-corner closure, not three-with-a-hole.
3. **`fp-imported-action`** - Gate 0 (G0c) fails; the algebra does not intrinsically fix
   the spin-torsion coupling. Same equivalence class as v18 Ph78.

## Honest scope (carry into the verdict)
Most likely: outcome 2 (NEGATIVE, triangulation sealed) - EC torsion is **algebraic /
non-propagating** (it vanishes outside matter), so it cannot supply free radiative DOF or
repair the `M=0`-adjacent vacuum mismatch that killed v18. But the v18 mismatch was a
tensor-SUPPORT defect (G on 16, kappaT on 6), and the spin current lives on exactly the
antisymmetric components torsion feeds, so a positive surprise (outcome 1) is structurally
possible and is the last place in the gravity program it could hide - which is why this
cheap computation is owed before the closure is written. Do NOT let "torsion is algebraic
so it won't close" substitute for the exact-over-Q computation; run it.
