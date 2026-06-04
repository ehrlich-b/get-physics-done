# v19.0 GATE A — Independent Ratification Verification

**Verdict under audit:** `fp-no-intrinsic-orientation` (GATE A KILL)
**Driver under audit:** `code/cartan_gateA_orientation.py`
**Independent verifier:** `code/cartan_gateA_verify_independent.py`
**Date:** 2026-06-03
**Mode:** Blocking ratification gate (gpd-verifier). The verdict is recorded ONLY if the kill is reproduced by a from-scratch, construction-independent re-derivation. Reported at true strength.

---

## TL;DR

**KILL `fp-no-intrinsic-orientation` is INDEPENDENTLY REPRODUCED — confidence HIGH.**

The forced complex structure `u = e_7` does **NOT** supply a sign-definite orientation on the `(1,3)` Lorentzian spacetime slice `h_2(C_u)`. The induced endomorphism `J` is **rank 2** with `J^2 = diag(0,-1,-1,0)` in Minkowski coordinates (NOT `-I_4`), so it is not an almost-complex structure on the slice; the Kähler 2-form `omega_K = eta(J·,·)` is **degenerate** (rank 2, **Pfaffian = 0**), so `omega_K ^ omega_K = 0` gives no volume form. Phase-78 clause C2 (orientation `eps` is a by-hand sign) **SURVIVES**. The reason is **construction-independent**: a `(1,3)` metric admits no `eta`-compatible `J` at all (odd time parity). `u` only orients the **Euclidean `(4,0)`** `V_{1/2}` `C_u^2` foil — the wrong space.

`code/cartan_gateA_verify_independent.py` exits **0** (kill reproduced). All decisive numbers exact over **Q** (SymPy `QQ`); no numpy / no float; `octonion_algebra.py` absent; `det` SSOT exact.

---

## Independence of the re-derivation (why this is cross-validation, not a re-run)

The audited driver builds `J` by **left-multiplying every octonion entry of the 3×3 `h_3(O)` matrix by `u = e_7`** (`_Lu_entrywise`, entrywise `oct_mul`) and reading slice coordinates, then argues the parity obstruction in **prose** (even/odd eigenvalue counting).

This verifier uses **different code paths**:

| Sub-claim | Driver method | Independent method used here |
|---|---|---|
| (a) no `eta`-compatible `J` | prose: even-# of `+` eigenvalues from `{v,Jv}` planes | **solve the polynomial system**: general `so(3,1)` `J` (6 unknowns), impose `J^2 = -I_4`, `solve` → empty over **R**; PLUS an airtight SOS witness `J^2[0,0] = a^2+b^2+c^2` forced to `-1` |
| (b) `u`-induced `J` on the slice | entrywise octonion `oct_mul(u, X[i][j])` | **`M_2(C_u) ~ M_2(C)` representation**: `e_7 -> i`, act by `i·I_2` on the 2×2 complex matrix, project back; triangulated by a `M_2(C)`-right variant and a from-scratch octonion route |
| (c) foil orientation | `oct_mul` on the two `C_u` lines | **complex-line `i`-multiplication** on each `C_u` line |

**Cross-validation confirmed:** the `M_2(C)` route (using SymPy `I`) and a from-scratch octonion route (using the Fano `oct_mul`) produce the **literally identical** `J` matrix. A separate from-scratch rebuild of the driver's full-3×3 entrywise mechanism (without importing the driver) also gives the same `J`. Agreement across the complex-scalar algebra and the non-associative octonion algebra is genuine cross-validation.

---

## (a) Construction-independent fact — a `(1,3)` metric admits NO `eta`-compatible `J`

**Claim:** No `J` with `J^2 = -I_4` AND `J in so(3,1)` (`J^T eta + eta J = 0`) exists for `eta = diag(+1,-1,-1,-1)`.

**Independent method (polynomial system, NOT the parity prose).** Parametrize `J = eta·A` with `A` a general antisymmetric 4×4 (6 rational unknowns `a..f`); this is the general element of `so(3,1)` (verified `eta`-skew exactly). Then

```
J^2 diagonal = [ a^2+b^2+c^2 ,  a^2-d^2-e^2 ,  b^2-d^2-f^2 ,  c^2-e^2-f^2 ]
```

- **SymPy `solve`** of the 16 equations `J^2 = -I_4` over real-declared symbols returns **0 solution branches** (empty over **R**).
- **Airtight solver-independent witness:** `J^2[0,0] = a^2 + b^2 + c^2` is a sum of three real squares (`>= 0`), and `J^2 = -I_4` forces `J^2[0,0] = -1`. **A sum of real squares can never equal `-1`.** This single equation proves the impossibility, with no reliance on `solve` completeness. The timelike `+1` entry of `eta` (row 0) is precisely what makes this diagonal entry positive-semidefinite.
- **Parity restatement:** `J^2[1,1] - J^2[0,0] = -(b^2+c^2+d^2+e^2) <= 0`, forced to `0` by `J^2=-I`, forces `b=c=d=e=0`, whence `J^2[0,0]=a^2=-1` — impossible. This exhibits the timelike(+)/spacelike(−) sign clash explicitly.

**Discriminating positive control (method is not vacuous):**

| Signature | `eta`-compatible `J^2=-I` exists? | Evidence |
|---|---|---|
| `(1,3)` Lorentzian | **NO** | real-solution-count = 0; `J^2[0,0]=a^2+b^2+c^2` SOS witness |
| `(3,1)` | NO | real-solution-count = 0 |
| `(4,0)` Euclidean | **YES** | explicit `J=[[0,-1,..],[1,0,..],..]` satisfies `J^2=-I_4` AND `eta`-skew |

The framework correctly returns "exists" for Euclidean `(4,0)` (explicit witness) and "none" for Lorentzian `(1,3)` — so the empty result is a real signature obstruction, not a vacuous failure.

> Note: over **C** the system is solvable (the complexified `so(3,1)` does contain such `J`); the obstruction is specifically **over R**, which is the physical content (a real Lorentzian metric). The `real=True` `solve` and the SOS witness both target real solvability correctly.

**Status: INDEPENDENTLY CONFIRMED (HIGH).** The result is construction-independent — it holds for ANY `J` built from `u` or otherwise.

---

## (b) `u`-specific construction (M_2(C) route) — `J^2 != -I`, Kähler form degenerate

**Claim:** `J` induced by `u = e_7` on the `(1,3)` slice is rank 2 with `J^2 = diag(0,-1,-1,0)` (Minkowski); `omega_K` is degenerate (Pf = 0); C2 not repaired.

**Independent construction (M_2(C_u)).** The slice `h_2(C_u)` is `[[beta, conj(x1)],[x1, gamma]]` with `x1 = p + q e_7`. Mapping `e_7 -> i` gives a 2×2 Hermitian complex matrix `[[beta, p-qi],[p+qi, gamma]]`. Acting by the `C_u` imaginary unit (`i·I_2`) and projecting back onto the (real-diagonal, `C_u`-off-diagonal) slice:

- **Diagonal leak (exact):** `i·beta` and `i·gamma` are pure-imaginary diagonal entries — they have **no real-diagonal coordinate**, so they read `0`. `i*(beta diagonal)` reads slice-coords `[0,0,0,0]`. The timelike/diagonal `{x0,x3}` plane has **no `u`-action** (frozen). This is forced, not a discretionary projection.
- **Off-diagonal:** `x1 -> i·x1` rotates `(p,q) -> (-q,p)`.

**Decisive results (exact over Q):**

| Quantity | Value | Meaning |
|---|---|---|
| `J` (raw `{beta,gamma,p,q}`) | `[[0,0,0,0],[0,0,0,0],[0,0,0,-1],[0,0,1,0]]` | acts only on `(p,q)`; diagonal frozen |
| `J^2` (Minkowski `{x0,x1,x2,x3}`) | `diag(0,-1,-1,0)` | `!= -I_4` |
| `rank(J)` | **2** | only the spatial off-diagonal plane complexified |
| `omega_K = antisym(eta·J)` (Mink) | `[[0,0,0,0],[0,0,1,0],[0,-1,0,0],[0,0,0,0]]` | rank 2 |
| `rank(omega_K)` | **2** | degenerate |
| **`Pf(omega_K)`** | **0** | `omega_K ^ omega_K = 2 Pf · vol = 0` ⇒ **no volume form** |

**Structure:** `u` complexifies ONLY the `{x1,x2}` purely-spatial off-diagonal plane (`eta = (-,-)`); the `{x0,x3}` plane containing the timelike `x0` is `u`-frozen. Complexifying it would rotate time into space, which a spatial octonion unit `e_7` cannot do.

**Triangulation (three `u`-faithful routes agree, exact over Q):**

| Route | `J^2` (Minkowski) | Note |
|---|---|---|
| `M_2(C)`-left (`i·I_2 · M`) | `diag(0,-1,-1,0)` | primary |
| `M_2(C)`-right (`M · i·I_2`) | `diag(0,-1,-1,0)` | sign of `(p,q)` rotation flips; square identical |
| from-scratch octonion left-mult | `diag(0,-1,-1,0)` | raw `J` **identical** to `M_2(C)`-left |
| driver-mechanism rebuilt from scratch (full 3×3 entrywise `oct_mul`, NOT imported) | `diag(0,-1,-1,0)` | raw `J` identical to `M_2(C)`-left |

**`fp-imported-orientation` guard.** The only way to reach `J^2 = -I` on the slice is to ADD a diagonal pairing that is **not** `u`'s action. The "keep-diagonal" contrast operator (leaves the real diagonal as identity instead of leaking it) is tested: it gives `J^2(Mink) = diag(1,-1,-1,1) != -I_4` AND retains the diagonal (contradicting the leak). So there is **no `u`-intrinsic repair** — any repair would be an imported pairing, exactly the v19.0 tripwire.

**Status: INDEPENDENTLY CONFIRMED (HIGH).** `J^2 != -I_4`, `Pf(omega_K) = 0` ⇒ C2 NOT repaired.

---

## (c) Triangulation — `u` DOES orient the Euclidean `(4,0)` `V_{1/2}` foil (the wrong space)

**Claim:** On the `V_{1/2}` `C_u^2` foil `{11,18,19,26}`, `u` gives a genuine `J^2 = -I_4` with a non-degenerate Kähler form (Pf != 0), confirming `u` orients the internal/Euclidean `OP^2` foil — not the spacetime slice.

**Construction.** Two `C_u` lines (`x2`'s `{Re,e7} = {11,18}` and `x3`'s `{Re,e7} = {19,26}`); `u = i` acts as the standard `[[0,-1],[1,0]]` on each line.

**Results (exact over Q):**

| Quantity | Value |
|---|---|
| `J` on foil | `[[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]]` |
| `J^2 == -I_4` | **True** (genuine complex structure) |
| foil bare-trace Gram `Tr(jordan(·,·))` | `diag(2,2,2,2)` |
| foil signature `(n+,n-,n0)` | **`(4,0,0)`** Euclidean |
| `Pf(omega_K)` on foil | **4** (non-degenerate ⇒ orientation FORCED) |

So `u` cleanly orients the **Euclidean `(4,0)`** `V_{1/2}` coframe-value foil — but `eps_{abcd} R^{ab} e^c e^d` lives on the `(1,3)` spacetime slice, where `u` fails. The triangulation isolates the failure precisely: `u` is a perfectly good complex structure on the Euclidean factor and a non-starter on the Lorentzian factor.

**Status: INDEPENDENTLY CONFIRMED (HIGH).**

---

## (d) Source guard — exactness and provenance

| Check | Result |
|---|---|
| `octonion_algebra` in `sys.modules` | **False** (banned engine absent) |
| `numpy` in `sys.modules` (after EMB+RL+BG imports) | **False** (no numpy on the decisive path) |
| `det` SSOT exact: `RL.det_3(diag(2,3,5))` | **30** (exact `int`, not float) |
| `u·u` via Fano `oct_mul` | `-1` (exact) |
| `u·1` via Fano `oct_mul` | `u` (exact) |
| All ranks / eigenvalues / signatures | SymPy `.rank()`, `.eigenvals()` over `QQ` — no `numpy.linalg`, no float |

**Status: INDEPENDENTLY CONFIRMED (HIGH).**

---

## Physics consistency checks (verifier registry)

| Check | Status | Confidence | Notes |
|---|---|---|---|
| Dimensional analysis | N/A | — | Pure dimensionless differential geometry over Q |
| Limiting cases | VERIFIED | INDEPENDENTLY CONFIRMED | `V_0`-limit / Euclidean-foil limit triangulated; (4,0) positive control vs (1,3) |
| Symmetry (`so(3,1)` compatibility) | VERIFIED | INDEPENDENTLY CONFIRMED | constructed `J` is `eta`-skew (an `so(2)` in `so(3,1)`) but not ACS; (1,3) admits no `eta`-compatible ACS |
| Mathematical consistency | VERIFIED | INDEPENDENTLY CONFIRMED | `J^2`, Pfaffian, ranks recomputed exactly over Q; two algebras agree |
| Cross-check (independent method) | VERIFIED | INDEPENDENTLY CONFIRMED | `M_2(C)` (SymPy `i`) ≡ octonion (`oct_mul`) ≡ rebuilt driver-mechanism `J` |
| Positivity / structure | VERIFIED | INDEPENDENTLY CONFIRMED | foil Gram `(4,0)` positive-definite; SOS witness `J^2[0,0]=a^2+b^2+c^2>=0` |
| Numerical exactness / source guard | VERIFIED | INDEPENDENTLY CONFIRMED | no float / no numpy / no banned engine; `det` SSOT exact |

**Catastrophic cancellation (Gate A):** N/A — all results are exact rationals/integers (no floating subtraction).
**Integration measure (Gate C):** N/A — no coordinate integral; the `RAW_TO_MINK` change of basis is exact and invertible (used consistently).

---

## Convention audit

- **Decisive-path conventions all consistent with the lock:** `eta = diag(+1,-1,-1,-1)` mostly-minus timelike-positive; Fano `e_1 e_2 = e_4`; `u = e_7`; `det` SSOT = `ring_lemma_verification.det_3` (cross-term `(x2 x1) x3`); EXACT over Q; ranks via SymPy. `octonion_algebra.py` banned and absent.
- **Documentation-vs-engine index discrepancy (non-blocking, flagged):** `CONVENTIONS.md` §3 labels the spacetime slice `{17,18,19,26}` (v17.0 Peirce naming), while the LIVE engine-native layout (`bulk_geometry_verification.py` Section 4) and BOTH the driver and the task spec use `{1,2,3,10} = {beta, gamma, p=Re(x1), q=<x1,e7>}`. These refer to the SAME 4 directions under different `x1/x2/x3` octonion-slot assignments; the engine-native set `{1,2,3,10}` is unambiguous from the layout and is what the decisive computation uses. **This is a documentation lag, not a convention violation on the decisive path.** Recommend the notation-coordinator reconcile the CONVENTIONS.md §3 / §1 index label to the engine-native `{1,2,3,10}` (this is the same ledger-lag noted for v18.0 Phase 77/78 — `{17,18,19,26}`→`[1,2,3,10]`).

---

## Discrepancies

**None on the verdict.** The independent re-derivation reproduces every decisive number of the driver: `J^2 = diag(0,-1,-1,0)`, `rank(J) = 2`, `Pf(omega_K) = 0` on the slice; `J^2 = -I_4`, Gram `(4,0)`, `Pf = 4` on the foil; `(1,3)` admits no `eta`-compatible `J`. The only discrepancy is the documentation index label noted above (non-blocking).

A self-inflicted harness bug during verification (an initial "offdiag" triangulation route that modeled "leave diagonal as identity" rather than "`u` kills the diagonal") was caught and corrected; it is NOT a physics issue — it is precisely the `fp-imported-orientation` contrast operator and now serves as the explicit guard in (b). The three `u`-faithful routes were always in exact agreement.

---

## Final verdict

**KILL `fp-no-intrinsic-orientation` is REPRODUCED. Confidence: HIGH.**

`u = e_7` supplies nothing the symmetric `(Tr, det_3)` data did not. On the `(1,3)` spacetime slice it induces only a rank-2, `J^2 = diag(0,-1,-1,0)` endomorphism whose Kähler form is degenerate (`Pf = 0`), giving no volume form; and `(1,3)`'s odd time parity forbids ANY `eta`-compatible complex structure (`J^2[0,0] = a^2+b^2+c^2` cannot equal `-1`) — a construction-independent obstruction. `u` orients only the Euclidean `(4,0)` `V_{1/2}` foil, the wrong space. **Phase-78 clause C2 SURVIVES.** The forced-antisymmetric-data route is dead at Gate A.

**Recommendation: RATIFY the GATE A KILL and STOP** (no Gates B/C/D; negative-result-is-success).

**Independent script:** `code/cartan_gateA_verify_independent.py` — exits 0 (kill reproduced); all sub-claims (a)/(b)/(c)/(d) PASS, exact over Q.
