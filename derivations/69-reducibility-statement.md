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
