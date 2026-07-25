# GPD Prompt: Gravity as the Curvature of the Peirce-Frame (Cartan/MacDowell-Mansouri) Connection on h_3(O)

## State recovery (read first - the prior route just died)

**The program.** Self-modeling -> QM (Paper 5, the firewall, at JMP, the only
solid theorem) -> h_3(O) basin + SM gauge data (Paper 7) -> GR (the open
endpoint). This task attacks the endpoint.

**The GR graveyard (do NOT reanimate any of these):**
- det/GST/Weinberg (`47-*`..`50-*`,`53-*`): DEAD, circular - the -R/2 Einstein
  term is the assumed N=2 multiplet's own output.
- lattice/Fisher (`paper6-continuum-limit-prompt.md`): abandoned (modeling choice).
- **cone-Hessian bulk geometry (`paper6-bulk-geometry-prompt.md`, v17.0 Ph 70-73):
  CLOSED 2026-05-31 = NONE.** Matter genuinely sources the slice curvature (~94%
  via the V_0<->V_{1/2} cross-term, Ph72) but `G[g]` is NOT proportional to any
  independently-motivated stress-energy (Ph73, exact over Q: `G_00~=6151` where
  `T_00=0`). The cubic-norm metric `g_X = Hess(-log det)` is just not an Einstein
  object - the THIRD confirmation (det/GST circular; M=0 slice = `R x H^3`;
  matter `eta+h` not `kappa T`).
- ensemble/thermodynamic (Jacobson/Verlinde/Vanchurin): REJECTED as woo
  (Bryan's standing constraint). Do not use entropy, KMS, modular/thermal time,
  or "many observers" arguments anywhere.

**Why this route is different (the diagnosis behind it).** Every dead route built
the spacetime metric from the **symmetric (Jordan) sector** - `Hess(-log det)` is
a symmetric metric. In the Jordan-Lie-Banach split of the observer's C*-algebra,
the symmetric product is the *static observables* and the **antisymmetric (Lie)
product (the commutator) is where time-evolution / dynamics live**. Gravity, if it
is in h_3(O), should be in the **antisymmetric/Lie sector**, and the curvature of
that sector is a **2-form / connection field strength** (a `F_{mu nu}`), NOT a
metric Hessian. That is exactly the **MacDowell-Mansouri / Cartan** formulation of
gravity (gravity = curvature of a broken connection). This route computes that
object. It is a genuinely different tensor than the cone-Hessian Riemann tensor,
so the NONE verdict above does NOT bind it.

## The mechanism (what to build)

The space of primitive idempotents of h_3(O) is the Cayley plane
`OP^2 = F_4/Spin(9)` (16-dim, Borel 1950). At a primitive idempotent `E`, the
tangent space to `OP^2` is exactly the Peirce half-eigenspace `V_{1/2}(E)` (from
`E o delta = (1/2) delta` for `delta` tangent). So an **idempotent field `E(x)`**
over a base has differential `dE` that is **`V_{1/2}`-valued = a soldering form /
coframe (tetrad)**. The natural connection on the `OP^2 = F_4/Spin(9)` frame
bundle (structure group the idempotent's stabilizer) has a **curvature 2-form**;
its `Spin(9)`-broken / Lorentz-subgroup part is the Cartan/MM gravitational
curvature. The non-compact real form lives in `Stab_{E_6}(E_11)` (Levi `~ Spin(9,1)`).

Equivalently and computationally: the curvature 2-form of the `E(x)` family is the
**Berry curvature** = the **imaginary part of the quantum geometric tensor (QGT)**
of the self-model state family (`|psi(x)> = ` the rank-1 state at `E(x)`). The dead
cone-Hessian was the **real part** (Fubini-Study/Fisher) of the same QGT. So this
route mines the half of the QGT we never touched.

**SOLID (standard math, cite, do not re-derive):**
- `OP^2 = F_4/Spin(9)`, 16-dim; `T_E OP^2 = V_{1/2}(E)` (Borel; McCrimmon Peirce).
- QGT: real part = Fubini-Study metric, imaginary part = Berry curvature
  (Provost-Vallee 1980).
- MM gravity = curvature of a Cartan connection broken to the Lorentz subgroup;
  `F ^ F` contraction gives Einstein-Hilbert + Lambda (MacDowell-Mansouri 1977;
  Wise gr-qc/0611154 for the clean Cartan-geometry statement).
- `h_2(C_u) ~= R^{3,1}` with Lorentzian `det`, `so(4,2)` conformal algebra
  (existing GPD `52-kkt-spacetime`, `52-observer-uniqueness`).

**CONJECTURAL (the thing to prove or disprove):** that the `Spin(9)`-broken
curvature of the Peirce-frame connection, after the `C_u` reduction of `V_{1/2}`
to a 4-dim Lorentzian coframe, is **gravitational and Einstein-structured** -
WITHOUT positing an MM action by hand.

## Conventions (inherit the v17.0 lock; new objects below)

- **Det SSOT:** the cubic norm is `ring_lemma_verification.py` `det_3`, cross-term
  `2Re(x2* x0* x1)` (F_4-invariant, Cayley-Hamilton + 324/324 verified).
  `octonion_algebra.py` is **BANNED** (buggy `(x1 x2) x3` order, float, 0.67
  associator gap). Octonion mul = Fano, `e1 e2 = e4`, complex structure `u = e7`.
- **Exact over Q on every decisive verdict.** `sympy.Matrix.rank()`, never numpy
  rank. Decisive numbers rational/symbolic, not float.
- **Curvature engine:** Totaro `R_ijkl = -(1/4) g^{pq}(f_jlp f_ikq - f_ilp f_jkq)`
  for the cone side; for the connection side use the standard Cartan structure
  equation `F = dA + A ^ A` (or `Omega = d omega + omega ^ omega`) computed
  symbolically. Cross-check any Riemann against a hand-rolled Levi-Civita on >=5
  components (as in Ph72).
- **H^3 sign benchmark:** the cone-Hessian on the `det=1` hyperboloid has `K=-1/2`
  (round-sphere convention `K=-1` differs by a factor of 2). Use it to fix sign
  conventions before reading any curvature verdict.
- `idempotent E_11 = diag(1,0,0)`; Peirce `V_1(1) = R E_11`, `V_{1/2}(16) = (1,2),(1,3)`
  octonions, `V_0(10) = h_2(O)`; spacetime sub-slice `h_2(C_u) ~= R^{3,1}` indices
  `{17,18,19,26}`. center `= I/3` (rho_J=0).
- **`CONVENTIONS.md` Section 6 is now AUTHORITATIVE** (corrected 2026-06-01 during
  the v17.0 run): `Lambda = 0`, the `M=0` spacetime vacuum is **flat KKT eta**
  (structurally derived, NOT Einstein-negative); the old "center is
  Einstein-negative Cartan, `Lambda < 0`" framing is FALSIFIED (that
  `{0,-1,-1,-1}` / `R x H^3` geometry is the cone-Hessian SOURCE field, not the
  spacetime metric). Inherit §6 as corrected. For THIS route the vacuum
  Einstein-structure level is to be MEASURED (Phase B(c)), but the expected vacuum
  is flat / pure-`Lambda`, not the dead `R x H^3` - do not reintroduce `Lambda<0`.

**New objects this route introduces:**
```
E(x)            : primitive-idempotent field over the 4d spacetime slice (the
                  KKT h_2(C_u) = R^{3,1} base); its variation IS the frame field
e := dE         : V_{1/2}-valued soldering form, C_u-reduced to a 4-dim coframe
                  (the tetrad). Must be invertible for a genuine soldering form.
omega           : the Lorentz Spin(3,1)-connection (spin connection) compatible
                  with e; sits in Spin(3,1) x Spin(6) subset Spin(9,1), the Levi
                  of the parabolic Stab_{E_6(-26)}(E_11). (Spin(3,1)=Lorentz,
                  Spin(6)=SU(4)=internal, matching Phase 48's so(3)xso(6) split.)
A := omega (+) e : the ASSEMBLED (A)dS/Poincare Cartan connection, valued in
                  so(3,2)/so(4,1)/iso(3,1) (10-dim): omega = the so(3,1) block,
                  e = the 4 translation/transvection generators.
F := dA + A ^ A : its curvature 2-form. Lorentz block = R(omega) + Lambda e^e
                  (Riemann + cosmological); translation block = de + omega^e
                  (torsion). F is also the Berry curvature of E(x) = imaginary
                  part of the self-model QGT (the cone-Hessian = its real part).
pi_u            : the C_u reduction V_{1/2}(16) -> 4-dim coframe (the SAME O->C
                  bottleneck that sent V_0's h_2(O) -> h_2(C_u) = R^{3,1}, Phase 46)
```

NOTE: Spin(9,1) is the AMBIENT structure group (45-dim); it is NOT itself the
4d gravity connection. It supplies the Lorentz Spin(3,1) sub-block (-> omega) and,
via its coset/V_{1/2} part, the coframe (-> e). The gravity content is the 10-dim
(A)dS connection A = omega (+) e assembled from those pieces, never the raw 45-dim
Spin(9,1) curvature.

## The claim

Fix `E_11` and the complex structure `u`. The Peirce-frame connection `omega` on
`OP^2 = F_4/Spin(9)`, reduced by `C_u` to the 4-dim Lorentzian coframe, has a
curvature `F` whose Lorentz-part, contracted MM-style, is the 4d gravitational
curvature - position-dependent, sourced by `V_{1/2}` matter, and (strong form)
Einstein-structured, with NO posited action.

## What to prove

### Phase 0: engine recovery + the tangent identity + calibration

- Reload the det SSOT (`ring_lemma_verification.py` `det_3`), re-pass its CH +
  324/324 checks. Confirm `octonion_algebra.py` is not imported anywhere.
- **Verify the load-bearing tangent fact exactly:** for `delta in V_{1/2}(E_11)`,
  `E_11 o delta = (1/2) delta`; and the primitive-idempotent variety's tangent
  space at `E_11` is exactly `V_{1/2}(E_11)` (16-dim). Exact over Q.
- Calibration anchor (reuse): single-copy `dim = 24`, `Spin(8) = 28`, `trdeg 3`;
  `e_6 = 78 = 52 + 26`; `orbit(E_11) = 17`, `Stab_{E_6}(E_11) = 61`,
  `Stab_{V_0} = 45 = Spin(9,1)`, `V_0` orbit `9 < 10`. Reproduce via
  `orbit_dimension_gate.py` before trusting any new stabilizer count.

### Phase A: the coframe-reduction dealbreaker (DO THIS FIRST - cheap, kills or greenlights)

**Theorem target A.** Does `(E_11, u)` ALONE reduce the 16-dim `V_{1/2}` soldering
form to a **4-dim Lorentzian coframe** carrying `SO(3,1)`?
  (a) Apply the `C_u` bottleneck (the Phase-46 `pi_u` mechanism that sent
      `h_2(O) -> h_2(C_u) = R^{3,1}`) to `V_{1/2}(16)`. Compute the image
      dimension (expect 4 if it parallels `V_0`) exactly.
  (b) Compute the signature of the induced coframe pairing (expect Lorentzian
      `(1,3)` / mostly-minus). Exact Gram eigenvalues over Q.
  (c) Confirm the residual structure group on the 4-dim coframe is (or contains)
      `SO(3,1)`, FORCED by `(E_11,u)`, not chosen by hand.

**KILL CONDITION:** if the reduction does not land on a **4-dim** space, or the
coframe is **not Lorentzian**, or the 4d reduction is **not forced** by `(E_11,u)`
(requires an arbitrary extra choice), the route is DEAD. Report
"Phase A: coframe reduction fails [which clause]" and STOP. This is the
`fp-arbitrary-reduction` gate: a 4d coframe smuggled in by hand is not a result.

### Phase A.5: the early MM-Einstein / same-wall gate (cheap; do BEFORE the full action)

The cone-Hessian died because its curvature was not proportional to any
stress-energy. The matter (`V_{1/2}`) couples through the same algebra here, so
test for the **same failure mode early**, on the curvature 2-form alone, before
investing in the full connection machinery.

**Theorem target A.5.** Compute the **canonical Berry curvature** `F_B` of the
idempotent field `E(x)` over the slice = imaginary part of the QGT (the cone-Hessian
was its real part - verify that the real part reproduces the dead `Hess(-log det)`
as a consistency check). `F_B` is the curvature of the CANONICAL (Grassmann/tautological)
connection on the eigenbundle - it needs no metric-compatibility equation, so it is
cheap and computable now, as a PROXY/diagnostic for whether the antisymmetric sector
has Einstein-shaped content at all. (The load-bearing object is Phase B's `F` from
the dynamical assembled connection `A=omega(+)e`; `F_B` and `F` need not be equal,
but if even the canonical `F_B` is hopelessly EM-shaped/mismatched, B will not save it.)
  (a) `F_B` at `M=0`: is it zero (flat), pure `Lambda` (`F_B ~ e ^ e`), or other?
      Report the vacuum structure level (expected flat/pure-`Lambda` per the
      corrected §6; do NOT reintroduce `Lambda<0`).
  (b) Turn on `M in V_{1/2}`. Is the matter-sourced part of `F_B` **transverse /
      Einstein-shaped**, or is it `EM-shaped` (a generic `U(1)`-type field
      strength with no relation to a metric stress-energy)? Specifically: does the
      `epsilon`-contraction of `F_B ^ F_B` onto the Lorentz sub-block yield a
      tensor whose `M`-scaling and tensor structure can match a `V_{1/2}`
      stress-energy `T[M]` at the SAME order in `M` (the lesson from v17.0 Ph73:
      power-counting and support must match, not just "some tensor appears")?
  (c) **Same-wall check:** does `F_B`'s matter-source come out non-proportional to
      `T[M]` the way the cone-Hessian's did (support where `T` vanishes,
      `~10^3` magnitude/shape mismatch)? If yes, the Lie sector inherits the
      symmetric sector's failure and the route is in serious trouble - report it
      plainly.

**SOFT KILL:** if A.5(c) reproduces the cone-Hessian mismatch (curvature support
disjoint from stress-energy support; no order-matching possible), report
"Phase A.5: Lie sector inherits the symmetric-sector mismatch" and recommend STOP
before Phase B. This is the cheap version of the whole test.

### Phase B: full Cartan curvature = 4d gravity

(Only if A and A.5 survive.)

**Theorem target B.** Assemble the (A)dS Cartan connection and read off 4d gravity.
  (a) Coframe: `e = pi_u(dE)` is a genuine invertible tetrad on the 4d slice
      (Phase A established it is 4-dim Lorentzian; here confirm non-degeneracy as
      a soldering form, i.e. `det(e^a_mu) != 0`).
  (b) Spin connection: extract `omega` = the Lorentz `Spin(3,1)` part of the
      ambient `Spin(9,1)` connection compatible with `e` (metric/torsion
      condition, or the canonical `f_4`/`e_6` reductive split). Do NOT use the
      raw 45-dim `Spin(9,1)` curvature - project to the `Spin(3,1)` Lorentz block.
  (c) Assemble `A = omega (+) e` (so(3,2)/so(4,1)/iso(3,1)) and compute
      `F = dA + A ^ A`. Its Lorentz block is `R(omega) + Lambda e^e`; its
      translation block is the torsion `de + omega^e` (check whether torsion
      vanishes / is matter-sourced). Identify `R(omega)` with the 4d Riemann
      tensor; cross-check against Totaro/Levi-Civita on >=5 components.
  (d) Vacuum (`M=0`): is the Lorentz block Einstein / `(A)dS`
      (`R_{mu nu} ~ Lambda g_{mu nu}`)? Use the `H^3` sign benchmark (`K=-1/2`)
      to fix conventions. Expected vacuum is flat / pure-`Lambda` (per the
      corrected §6), NOT the dead `R x H^3`; report `Lambda`'s value/sign as
      MEASURED. Then turn on `M in V_{1/2}` and check the matter-sourced Riemann.

### Phase C: the circularity audit (the GST sin, re-armed)

**Theorem target C.** Is the Einstein term **FORCED** by intrinsic h_3(O) data, or
**POSITED**? The MM action `integral epsilon F ^ F` gives Einstein-Hilbert + Lambda
ONLY because of the specific `epsilon`-contraction (which group, which broken
generators). Decide:
  (a) Is the contraction (the `Spin(9,1) -> SO(3,1)` symmetry breaking and the
      `epsilon`-tensor) FIXED by the trace form / cubic-norm pairing on h_3(O), or
      is it an external MM choice?
  (b) If the Einstein term only appears because an MM action was assumed, that is
      `fp-imported-action` = the GST sin in new clothes. Report it as such. The
      route only WINS if the Einstein structure falls out of the cubic-norm /
      trace-form geometry without importing the action.

## Pass/Fail summary

| Outcome | Verdict |
|---------|---------|
| Phase A: reduction not 4d / not Lorentzian / not forced | **KILL.** Route dead, stop. |
| Phase A.5: Lie sector inherits the cone-Hessian mismatch | **SOFT KILL.** Report, recommend stop. |
| A,A.5 survive; B gives 4d Riemann sourced by V_{1/2} | **SURVIVES:** connection-curvature gravity, distinct from the dead metric route. |
| C: Einstein term FORCED by trace-form/cubic-norm (not imported) | **STRONG WIN:** gravity from h_3(O) Lie-sector geometry, non-circular. |
| C: Einstein term only via posited MM action | **fp-imported-action** - honest partial, NOT a derivation. |

## Reporting discipline

Negative-result-is-success. A clean Phase A KILL (no forced 4d Lorentzian coframe)
or a Phase A.5 same-wall SOFT KILL is a valuable, publishable closure - report it
flat, do not relabel "approximately 4d" or "approximately Einstein". A
forced-coframe-but-imported-action outcome (B yes, C no) is the most likely real
result; report it as `fp-imported-action`, not as a win. The point is to find out
whether gravity is the Lie-sector connection curvature of h_3(O), not to confirm it.

## Forbidden proxies (auto-fail if used as load-bearing)

- `fp-imported-action`: declaring Einstein structure that only appears because an
  MM/EH action was posited by hand (the GST sin).
- `fp-arbitrary-reduction`: a 4-dim coframe obtained by a choice not forced by
  `(E_11, u)`.
- `fp-float-decisive`: any decisive verdict resting on floating-point rank or
  curvature (must be exact over Q).
- `fp-relabel`: "F satisfies some 2-form equation" relabeled as "F satisfies
  Einstein" without an independent stress-energy `T[M]` matched in magnitude,
  tensor structure, AND M-power.
- `octonion_algebra.py`: banned (buggy associator).

## Build on (do not rebuild)

- `ring_lemma_verification.py` (det SSOT), `orbit_dimension_gate.py` (stabilizer
  calibration), `peirce_coupling.py` (Peirce decomposition under E_11).
- `52-kkt-spacetime`, `52-observer-uniqueness` (`h_2(C_u) = R^{3,1}`, Phase-46
  `pi_u` bottleneck - REUSE the same `C_u` reduction for `V_{1/2}`).
- The Ph72/73 Totaro + Levi-Civita curvature cross-check harness.

## Stay distinct from (do not reuse as load-bearing)

- `paper6-bulk-geometry-prompt.md` (cone-Hessian = the dead SYMMETRIC sector;
  here we compute the ANTISYMMETRIC/connection curvature - a different tensor).
- `47-*`..`50-*`,`53-*` (det/GST/Weinberg - circular). We do NOT posit an action;
  Phase C audits exactly that.
- Any thermodynamic/modular/ensemble construction (rejected).

## Key references

- MacDowell & Mansouri, Phys. Rev. Lett. 38 (1977) 739 - gravity as a broken
  gauge theory of a de Sitter/Lorentz connection.
- D. K. Wise, gr-qc/0611154 - MacDowell-Mansouri gravity and Cartan geometry
  (the clean modern statement; THE reference for this route).
- Provost & Vallee, Comm. Math. Phys. 76 (1980) 289 - quantum geometric tensor;
  real part = Fubini-Study, imaginary part = Berry curvature.
- R. W. Sharpe, *Differential Geometry: Cartan's Generalization of Klein's
  Erlangen Program* (1997) - Cartan connections, soldering forms.
- Baez, "The Octonions" (2002) - h_3(O), F_4, `OP^2 = F_4/Spin(9)`,
  `T_E OP^2 = V_{1/2}`.
- McCrimmon, *A Taste of Jordan Algebras* - Peirce decomposition, primitive
  idempotents, the `E o delta = (1/2) delta` tangent identity.
- Faraut & Koranyi, *Analysis on Symmetric Cones* (1994) - for the cone-Hessian
  consistency cross-check (the real part of the QGT) only.
- Gunaydin-Sierra-Townsend (1983-84) - **geometry only** (`E_{6(-26)}/F_4`); we
  do NOT adopt their Lagrangian (the dead route).
- (Contrast only, do not use:) Jacobson 1995; Connes-Rovelli thermal time - the
  thermodynamic/modular route is explicitly rejected.
