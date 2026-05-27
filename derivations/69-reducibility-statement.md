# (REDUCIBILITY): the Dynamical Bridge — Statement for the Next Milestone

<!-- ASSERT_CONVENTION: arithmetic=exact-over-Q; jordan=(1/2)(AB+BA); trace=sum-of-real-diagonal; squared_trace=Tr(XoX); cubic_norm=det=N(X); coupling=c=Tr(XoY); algebra=h_3(O); group=F_4=Aut(h_3(O)); rep=27=1(+)26 -->

> **STATEMENT-ONLY.** This document **STATES** the (REDUCIBILITY) target for the next
> milestone; it asserts **NO irreducibility verdict** and uses **NO chaos / Lyapunov /
> NKS / sensitive-dependence argument**. The single executable check here is a
> polynomial-identity bookkeeping check (the cross-term decomposition, exact over Q),
> **not** a proof of irreducibility. This is the LAST deliverable of milestone v16.0
> (REDU-01): the dynamical bridge from the now-complete static (RING) result —
> `c = Tr(X o Y)` is a genuine, minimal, functionally-independent, unique-degree-2
> `F_4` coupling generator of `R[27 (+) 27]^{F_4}` (Phases 66/67/68) — to the next
> milestone's open-system irreducibility question. A future milestone should be able
> to open this file alone and find a precise, frozen-notation statement of what it must
> prove.

---

## 0. Frozen conventions (Phase-64, LOCKED — used verbatim throughout)

All equations in this document use the FROZEN Phase-64 notation. These are
**pure-algebra** conventions (the Albert algebra over Q); there are no physical units.

| Choice | Convention |
| ------ | ---------- |
| Jordan product | `X o Y = (1/2)(XY + YX)`; for Hermitian `X,Y`, `Tr(X o Y) = Re Tr(XY)` |
| Trace | `Tr(X) = alpha + beta + gamma` (sum of real diagonal entries); bidegree `(1,0)` |
| Squared trace | `Tr(X^2) := Tr(X o X)` — the **Jordan-square trace**, NOT `(Tr X)^2`; and `c(X,X) = Tr(X^2)` |
| Cubic norm / det | `det X = N(X)`; polarization LOCKED `d(X,X,X) = 6 det X`; cross-factor order `(x2 x1) x3` (Phase-64.1 fix) |
| Powers (power-associative) | `X^2 := X o X`; `X^3 := X o (X o X) = (X o X) o X` (well-defined: `h_3(O)` is power-associative) |
| Coupling generator | `c = Tr(X o Y)`, bidegree `(1,1)`; `F_4`-invariant, **NOT** `E_6`-invariant |
| Algebra | `h_3(O)` = `3x3` Hermitian octonionic (Albert) algebra, 27-dim real |
| Group | `F_4 = Aut(h_3(O))` (compact, 52-dim; fixes `Tr`, the trace form, and `det`); `27 = 1 (+) 26` |
| Arithmetic | **EXACT over Q**; ranks/identities via SymPy; **NEVER** float on a decisive path |

Warm exact engine: `code/ring_lemma_verification.py` (the frozen EXACT-SymPy-over-Q
engine for the whole (RING) milestone), exposing `jordan`, `Tr`, `det_3`, `c`,
`generic_rational_X`, `h3o_from_coords`, `oct`, `octmat_add`, `octmat_scal`.

**Notation reminder (anti-drift).** Throughout, `o` is the Jordan product, `Tr` the
trace, `det` the cubic norm, `c` the coupling. `X^2` always means `X o X` and `X^3`
means `X o (X o X)`. `Tr(X^2)` is the **Jordan-square trace** `Tr(X o X)` — never
`(Tr X)^2` (these are distinct degree-2 invariants).

---

## 1. Object 1 — Driven self-modeling dynamics

The self-modeling update (the `find_fp` / Jordan–Hopfield update; program doc
`phi-inaccessibility-program.md` Sec. 9.7, line 608) is the map

> **`X_{k+1} = P_psd((1-eps) X_k^2 + eps S_k)`,   with   `X_k^2 := X_k o X_k`.**
>
> (equivalently, with explicit spacing, `X_{k+1} = P_psd( (1 - eps) X_k^2 + eps S_k )`.)

Every symbol, typed:

- `X_k in h_3(O)` — the system's self-state at step `k` (a `27`-dim Hermitian
  octonionic Albert-algebra element).
- `X_k^2 := X_k o X_k` — the Jordan square of the self-state (the `(1/2)(X_k X_k + X_k X_k) = X_k X_k`
  Jordan product of `X_k` with itself; lands back in `h_3(O)`). This is the
  "self-iteration" term: the system applies its own state to itself.
- `S_k in h_3(O)` — the **exogenous driven input stream** at step `k` (the incoming
  "world").
- `eps in (0,1)` — the **self-world coupling rate** (the relative weight of
  self-iteration vs. input). `eps -> 0` is pure world-tracking; `eps -> 1` is pure
  self-iteration.
- `P_psd : h_3(O) -> h_3(O)` — the **projection onto the PSD (positive-semidefinite)
  cone** of `h_3(O)` (the nearest PSD element in the Jordan/trace-form metric). It
  keeps the self-state a valid (PSD) "density-like" object after each update.

**Implicit energy (the variational form the update relaxes).** The map descends the
energy

> `E(X) = || X - S ||_J^2  +  || X^2 - X ||_J^2`

(the **depart-from-input** term `|| X - S ||_J^2` + the **depart-from-idempotency**
term `|| X^2 - X ||_J^2`), where `|| . ||_J` is the Jordan/trace-form norm. The first
term pins the state to the incoming world `S`; the second pushes the state toward an
idempotent (a "definite" self-model, `X^2 = X`). The update above is the corresponding
relaxation step, projected back onto the PSD cone.

This object is the load-bearing dynamics. (Scope note: Sec. 9 of the program doc is
DEMOTED for its self-inaccessibility framing but RE-PROMOTED for exactly this
driven-dynamics content — see the Forbidden / Out-of-scope section. We carry the
dynamics, not the demoted verdict.)

---

## 2. Object 2 — Autonomous vs. driven (two distinct maps)

The map of Object 1 is run in **two physically distinct regimes**. They are
**different maps**, and the distinction is the binding subtlety of this whole bridge.

### 2a. AUTONOMOUS regime (`S_k` fixed)

`S_k = S` fixed (or `S_k =` a prior fixed point = the metacognitive tower feeding on
its own settled state). With the input held constant, the update

> `X_{k+1} = P_psd( (1 - eps) X_k^2 + eps S )`

is a **contraction to a fixed point**: geometric convergence, `|| X_{k+1} - X_k ||_J -> 0`.
The trajectory settles to `X_* = X_*(S, eps)`.

**This regime is REDUCIBLE in the capacity sense** (defined precisely in Object 4): the
entire trajectory `{X_k}` is **RECONSTRUCTIBLE** by re-running the law from `(S,` the
update rule`)` — no information is irretrievably lost, because the closed map plus its
fixed input determines everything. Re-running the rule with `S` and `eps` regenerates
the whole orbit on demand.

Consequence to record: **ALL existing `Phi` measurements are autonomous**, hence
reducible, hence **NOT a source of inaccessibility**. (Using the autonomous
`F_3`-contraction to settle the irreducibility question would "falsely kill the engine":
its limit is recomputable — see the trap below.)

### 2b. DRIVEN regime (`S_k` exogenous, time-varying — the lived Stream)

`S_k` is an **exogenous, time-varying input stream** — the lived Stream. The update is
**slaved to the input** and has **no fixed point**: each step is driven by a fresh,
externally supplied `S_k`. The orbit `{X_k}` now depends on the entire incoming history
`S_0, S_1, ..., S_k`.

### 2c. The autonomous-vs-driven trap (stated up front; re-flagged formally in Object 5)

**The autonomous map's reconstructibility must NOT be used to claim or deny
irreducibility of the driven Stream, and vice versa.** They are two different maps:

- The **autonomous** map is a **contraction** (re-runnable from `(S, law)`) ⇒ reducible.
- Any irreducibility of the **driven** Stream — *if there is any* — is **inherited from
  the unpredictability of the exogenous input `S_k`**, **NEVER manufactured by the
  algebra**. The algebra (the autonomous map) is a contraction, not a source of
  intrinsic unpredictability.

**Wolfram refinement (the licensed framing).** A closed, autonomous cellular automaton
is *runnable given the rule*: you can always reproduce its evolution from the rule and
initial data. The inaccessibility-relevant notion here is the **open-system** kind:
*you cannot run the Stream forward without the exogenous input you do not possess.*
This **refines** Wolfram's computational irreducibility (closed-CA, runnable-given-rule)
to the open-driven case (not runnable without the missing input) — it does **not**
invoke chaos, Lyapunov exponents, or sensitive dependence, and it does **not** assert a
verdict here.

*(No irreducibility verdict is asserted in this object. No chaos/NKS/Lyapunov argument
appears. The two regimes are kept as two maps.)*

---

## 3. Object 3 — The cross-term decomposition (the algebraic core)

Form the overlap of the current self-state with the next one, `Tr(X_k o X_{k+1})`. For
the **pre-projection object**

> `Y_k := (1-eps) X_k^2 + eps S_k`     (so that `X_{k+1} = P_psd(Y_k)`),

the overlap decomposes cleanly:

> **`Tr(X_k o X_{k+1}) = (1-eps) Tr(X_k^3) + eps Tr(X_k o S_k)`**   *(holds exactly when `X_{k+1} = Y_k`; see the modulo-`P_psd` caveat in §3c).*

### 3a. The two pieces and what they mean

- **First piece `(1-eps) Tr(X_k^3)` — a POINTWISE invariant ⇒ REDUCIBLE.**
  `Tr(X_k^3) = Tr(X_k o (X_k o X_k))` is a single-state `F_4` invariant of `X_k`
  alone. By the established single-state result `R[h_3(O)]^{F_4} = R[Tr, Tr^2, det]`
  (Phases 64–68; Springer 1962; Faraut–Korányi), `Tr(X_k^3)` lies in the pointwise
  invariant ring `R[Tr, Tr^2, det]`. It is computable from the cheap pointwise
  invariants of the *current state* — **reducible** in the capacity sense of Object 4.

- **Second piece `eps Tr(X_k o S_k)` — the self-world OVERLAP ⇒ "the irreducible
  candidate."** This is the overlap of the current self-state `X_k` with the incoming
  world `S_k`, in the gauge directions (the `26` trace-free directions where the
  coupling lives). We **NAME** it the **"self-world overlap / the irreducible
  candidate"** — and STOP. We do **NOT** assert it is irreducible (prerequisites are
  unmet; that is the next milestone's burden), and we do **NOT** bake in the
  relational-experience identity (program doc Sec. 9.7, line 656, tags it "do NOT bake
  in yet").

### 3b. Algebraic lineage (the only non-trivial step)

The decomposition is **bilinearity + symmetry of `Tr(A o B)` plus a single
power-associativity identity**:

- `Tr(X_k o Y_k) = Tr(X_k o ((1-eps) X_k^2 + eps S_k)) = (1-eps) Tr(X_k o X_k^2) + eps Tr(X_k o S_k)`
  — by bilinearity of the Jordan product and linearity of `Tr`.
- The **ONLY non-trivial step** is power-associativity:
  `X_k o X_k^2 = X_k^3`, i.e. `X_k o (X_k o X_k) = X_k^3` (well-defined because
  `h_3(O)` is power-associative, so `X_k o (X_k o X_k) = (X_k o X_k) o X_k`). Hence
  `Tr(X_k o X_k^2) = Tr(X_k^3)`. This is a cited Albert-algebra fact
  (Springer–Veldkamp), **not** re-proved here; it is the one identity the canned check
  of §4 confirms exact over Q.
- Symmetry: `Tr(X_k o S_k) = Tr(S_k o X_k)` (the Jordan product is commutative; the
  trace form is symmetric).

**Link to (RING).** The cross-term `Tr(X_k o X_{k+1})` is built from the coupling
generator `c = Tr(X o Y)` (Phases 66/67): `eps Tr(X_k o S_k) = eps * c(X_k, S_k)`. The
just-completed (RING) result — `c` is a genuine, functionally-independent,
unique-degree-2 `F_4` coupling generator that is **NOT** in the pointwise ring `R_pt`
(Phase 66, the SPINE) — is exactly **why the self-world overlap escapes the pointwise
invariant ring**: the first piece is pointwise (`Tr(X_k^3) in R[Tr,Tr^2,det]`), but the
second piece is the coupling `c`, which provably is not a pointwise invariant. (This is
the static-to-dynamical bridge: the static independence of `c` is what makes the
overlap piece a *candidate* for being irreducible. It is a candidate, not a verdict.)

### 3c. The "modulo P_psd" caveat (load-bearing — stated honestly, NOT dropped)

*(Caveat label, verbatim: the decomposition of §3 is the pre-projection identity, exact
**modulo P_psd** — i.e. exact for `Y_k`, with a projection correction otherwise.)*

The clean identity of §3 holds **exactly for the pre-projection object `Y_k`**. The
actual update applies the PSD-cone projection `X_{k+1} = P_psd(Y_k)`. There are two
cases:

- **On the PSD interior** (`Y_k` already PSD): the projection does nothing,
  `X_{k+1} = Y_k`, and the decomposition is **exact** as written.
- **When the projection bites** (`Y_k` not PSD): the identity acquires a **projection
  correction**

  > `Tr(X_k o X_{k+1}) = (1-eps) Tr(X_k^3) + eps Tr(X_k o S_k) + Tr(X_k o (X_{k+1} - Y_k))`,

  where `(X_{k+1} - Y_k)` is the PSD-projection displacement.

We carry this correction **modulo `P_psd`** explicitly; we do **NOT** silently write the
bare identity as if `X_{k+1} = Y_k` always. (The program doc Sec. 9.7, line 623, itself
writes "(modulo `P_psd`)" — we match that honesty.) Note: the correction term
`Tr(X_k o (X_{k+1} - Y_k))` is itself a diagonal-Observable-type quantity tied to the
PSD-boundary geometry; it is **NOT** part of the "irreducible candidate" — but we do not
over-claim its character either way (this is a STATEMENT, not an analysis of the
projection). The next milestone must handle the projection correction explicitly.

*(Frozen notation throughout. `Tr(X_k^2)` and `Tr(X_k^3)` are Jordan-power traces, never
`(Tr X_k)^2` or `(Tr X_k)^3`. No irreducibility verdict; no chaos/NKS.)*

---

## 4. Object 4 — Reducibility, defined via capacity / reconstructibility

This is the **finite face of computational irreducibility**, defined via **capacity /
reconstructibility** (program doc Sec. 9.7, lines 640–654; Sec. 9.1). It is **NOT** a
chaos notion and **NOT** a ring-membership shortcut.

> **A trajectory-functional `f` is REDUCIBLE for a system iff it is reconstructible
> from the bounded data the DIACHRONIC self-model `M` can hold (re-running the law if
> needed), WITHOUT the full body `B`. `f` is IRREDUCIBLE iff computing `f` requires `B`
> itself** — the full `26`-dim gauge and/or the exogenous input history `S_0, ..., S_k`.

The precise structure of the two objects:

- **`M` = the rank-compressing diachronic self-model** (the metacognitive tower,
  compressed toward rank-1 as it climbs). `M` holds only the **cheap pointwise
  invariants** of the self-state — `Tr`, `Tr^2`, `det` (just **3 numbers**) — plus the
  capacity to **re-run the update law**. `M` does **NOT** hold the `26`-dim gauge
  directions, and it does **NOT** hold the exogenous input history.
- **`B` = the full body** — the entire `27`-dim state (equivalently the `26`-dim gauge
  beyond the trivial direction), and the exogenous input stream the body is actually
  coupled to.
- **`dim M < dim B`** — the self-model is a **proper** subsystem, strictly smaller than
  the whole. This strict inequality is the hinge of the target reduction (Object 5).

Two distinctions that pin the definition (anti-drift, anti-reward-hack):

1. **`M` is the DIACHRONIC self-model, NOT the Paper-5 synchronic order-iso.** Paper 5's
   clause (ii) is a **synchronic, full-dimensional, lossless order-isomorphism** of the
   state. `M` here is the **diachronic** tower: **compressed** (`dim M < dim B`), and it
   accumulates over time by re-running the law. The synchronic/diachronic split (program
   doc Sec. 9.1) is exactly why they must not be conflated: Paper 5's order-iso loses
   nothing and is full-dim; `M` is lossy/compressed and lower-dim. Do not confuse the
   two.
2. **"Reducible" is the CAPACITY/reconstructibility notion, NOT two things it is often
   mistaken for.** It is **NOT** "`f` lies in `R[Tr, Tr^2, det]`" (a ring-membership
   shortcut would trivially predetermine whether the cross-term is in/out of the
   pointwise ring — a definitional reward-hack we explicitly avoid). It is **NOT**
   asymptotic Kolmogorov complexity / NKS algorithmic incompressibility (an asymptotic,
   rule-length notion). It is the **finite** reconstructibility-from-`M` notion:
   *can the bounded, compressed `M` regenerate `f` by holding its `3` invariants and
   re-running the law, or does `f` genuinely require the full `B`?*

"Self-modeling = projection onto the reducible sector" is therefore a statement to be
**EARNED, not asserted by fiat**: `M` can compute only what fits its capacity (the
pointwise invariant ring + re-running the law). Whether the driven gauge-overlap fits
that capacity is precisely the open question of Object 5.

---

## 5. Object 5 — The target reduction ("what the next milestone needs")

This object states **what the next milestone needs** to prove. It asserts **NO
verdict**; it routes the question to a structural argument.

### 5a. The target

From the decomposition (Object 3), the driven overlap splits into a pointwise piece
`(1-eps) Tr(X_k^3)` (reducible — in `R[Tr, Tr^2, det]`, computable by `M`) and the
**self-world overlap `eps Tr(X_k o S_k)`** (the irreducible candidate). The
target of the next milestone:

> **Show that the driven gauge-overlap `eps Tr(X_k o S_k)` is NOT reconstructible from
> `M`'s bounded held data** (the `3` pointwise invariants + re-running the law) — i.e.
> that computing it genuinely requires `B` (the full gauge and/or the exogenous input
> history).

This is **what the next milestone needs**; it is **not** established here. (Object 3's
EXACT-Q certificate confirms only that the *decomposition* is algebraically correct —
not that the overlap piece is irreducible.)

### 5b. The licensed route: a STRUCTURAL finite-capacity (Breuer) argument

The target routes to a **structural, finite-capacity** argument — **NOT** a dynamical /
chaos argument. The anchor is the self-measurement theorem:

> **Breuer 1995.** Thomas Breuer, "The Impossibility of Accurate State
> Self-Measurements," *Philosophy of Science* **62**(2) (June 1995), pp. 197–214
> (University of Chicago Press / Philosophy of Science Association).
>
> **Theorem (form used here):** A **proper subsystem cannot fully measure/model the
> whole that contains it**, because it has **strictly fewer degrees of freedom** than
> the whole; hence distinct global states with identical restrictions to the subsystem
> are **indistinguishable** to it. (Equivalently: an observer cannot distinguish all
> present states of a system in which the observer is properly contained — independent
> of classical vs. quantum, and independent of deterministic vs. stochastic dynamics.)
>
> **Hypotheses (the routing conditions):** (i) **proper containment** — the self-model
> is a proper subsystem of the whole (here `dim M < dim B`); (ii) the discriminating
> observable lives in the subsystem's algebra only.
>
> **Nature:** a **STRUCTURAL / finite-capacity** result (degrees-of-freedom counting +
> self-reference), **NOT** a dynamical/chaos result — which is exactly why it is the
> licensed route and why a chaos argument is forbidden.

The routing: with `dim M < dim B` (Object 4), `M` is a proper subsystem; the
discriminating quantity — the gauge-overlap `eps Tr(X_k o S_k)` — lives in the gauge
directions that `M` does not hold. Breuer's structural conclusion is then the candidate
mechanism by which `M` cannot reconstruct the overlap. **Companion structural routes**
(the structural family the next milestone may draw on; **mention only**, do not lean on
them here): the **Lawvere** fixed-point "no complete self-model" (already in program doc
Sec. 9.4), and Breuer's "Ignorance of the Own Past" (for the unbounded
input-history half). **Breuer 1995 is the primary, finite-capacity anchor.**

### 5c. The autonomous-vs-driven trap, re-flagged FORMALLY

Re-stated formally as a binding constraint on the next milestone's proof:

- The **autonomous** `F_3`-contraction is **REDUCIBLE**: it contracts to a fixed point
  and is re-runnable from `(S,` the law`)`. Its reconstructibility says **nothing** for
  or against the driven Stream.
- Any irreducibility of the **driven** Stream is **INHERITED from the exogenous stream
  `S_k`'s unpredictability** (the open-system "cannot run without the input you lack"),
  **NEVER** from chaos / Lyapunov exponents / NKS / sensitive dependence of the
  algebra. The algebra is a contraction.

So the target reduction must route through finite capacity (Breuer / `dim M < dim B`),
never through a dynamical-instability argument.

### 5d. Honest residual — this is a TARGET, not a fait accompli

This is stated honestly as a **weakest anchor**. The program doc Sec. 9.6.1 itself
concedes that the gauge/angle irreducibility **"is not automatic — an integrable flow
would make them reducible too."** In other words, the structural route is *plausible but
genuinely unproven*: it is conceivable that the driven gauge dynamics are integrable, in
which case the overlap would be reducible after all. **This is exactly why this
milestone only STATES the target and the next milestone must PROVE it.** The target
reduction is a *candidate route*, not a fait accompli, and the next milestone must
either close the finite-capacity argument (including handling the integrable-flow
escape) or report a negative result honestly.

*(No irreducibility verdict is asserted in this object. The reducibility definition is
the capacity/reconstructibility one. No chaos/NKS argument is used; the route is
explicitly structural/finite-capacity. The eps-term remains "the self-world overlap /
the irreducible candidate" — named, not adjudicated.)*
