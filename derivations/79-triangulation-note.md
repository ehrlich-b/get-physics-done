# v19.0 Triangulation Note — "the i belongs to internal gauge, not gravity"

**Status:** closing synthesis for milestone v19.0 (Gate-A quick negative,
`fp-no-intrinsic-orientation`). Companion to `derivations/79-orientation-gate.tex`.
Verifier-hardened (HIGH), human-ratified. Reported at true strength.

## The one structural fact, seen three ways

Three intrinsic routes to gravity from `h_3(O)`, each on a **different tensor**, have now
each returned a decisive negative — and they are three faces of a single fact, not three
unrelated dead ends:

| Milestone | Route (tensor) | Sector | Verdict |
|-----------|----------------|--------|---------|
| v17.0 | cone-Hessian `Hess(−log det)` | **symmetric** / `V_0` / `Re(QGT)` (Fubini–Study) | **NONE** — curved, matter-sourced, but not Einstein-structured |
| v18.0 | Cartan/MM connection `F=dA+A∧A`, torsion-free | **Lie** / `V_0` | **fp-imported-action** — forced SO(3,1) coframe + genuine Riemann, but `G[g]≠κT+Λg` and the ε-contraction is not forced |
| v19.0 | complex-structure orientation from `u=e_7` | **antisymmetric** / `u` | **fp-no-intrinsic-orientation** — `u` does not orient the (1,3) slice |

**The fact:** the program's complex / antisymmetric "i" — the complex structure `u = e_7`
and the antisymmetric (Berry / imaginary-QGT) sector — is **internal-gauge-natured**, and
**Lorentzian spacetime structurally rejects it.**

## Why v19.0 is the sharpest face

The Gate-A kill rests on a construction-**independent** theorem, not on "u happened to fail":

> A pseudo-Riemannian 4-metric of signature **(1,3)** admits **no** compatible
> almost-complex structure (`J²=−1`, η-orthogonal). A compatible `J` pairs the axes into
> J-invariant 2-planes on each of which η is conformal `diag(a,a)`, forcing **even** counts
> of both signs; (1,3) has `n₊=1, n₋=3`, **both odd** → obstruction.

So **no** complex-structure orientation source — `u=e_7` or any other — can supply the
orientation ε that the MacDowell–Mansouri contraction `ε_{abcd} R^{ab}∧e^c∧e^d` needs.
Phase-78 clause C2 stands for a structural reason, now fully general.

The `u`-specific computation is one clean instance: `u` complexifies only the off-diagonal
**spatial** C_u-plane (slice `J` is rank 2, `J²=diag(0,−1,−1,0)`; the timelike `{x0,x3}`
plane is frozen because `u·(real diagonal)=e_7` leaves h_3(O)), so the Kähler form is
degenerate (`Pf=0`) and `ω_K∧ω_K=0`.

## Where the i *does* live (the convergence)

`u` is not inert — it orients the **Euclidean (4,0)** `V_{1/2}` C_u² coframe foil **cleanly**
(`J²=−I₄`, `Pf=4≠0`). That is the **internal** OP²=F₄/Spin(9) space, not spacetime. This
converges with **Phase 76**: the Berry curvature `Im(QGT)` is the internal `so(6)=SU(4)`
gauge curvature, not gravity. Same message from two directions: the holomorphic/complex
structure is at home in the **Euclidean / self-dual "internal" half** and **walls off at full
Lorentzian dynamics** — the **Penrose/twistor shape**.

## The publishable closure

The result is **not** "another route failed." It is: *the exceptional algebra's complex
structure belongs to the internal gauge sector — which is exactly why every intrinsic-gravity
route from `h_3(O)` falls short, and why gravity is separate* (the Penrose / 't Hooft
reading). v19.0 closes the **last unexploited data class** (the forced antisymmetric `u`),
completing the triangulation that grounds "gravity is separate."

## Residual thread (OPEN — do not chase)

The theorem forecloses **continuous** complex-structure orientation sources. It does **not**
formally foreclose a **discrete** parity datum: the chiral `V_{1/2}` 8+8 split (Phase 50,
`C_{i,i,18}=∓1/6`, `e_7`-linked). A discrete chirality could fix a sign where a continuous
`J` cannot. Expected disease one level up: is the 8↔8 labeling **forced**, or swappable by an
`F_4/Spin` automorphism (gauge)? If gauge, it orients nothing intrinsically. **Logged as an
open question only — no gate, no phase.**
