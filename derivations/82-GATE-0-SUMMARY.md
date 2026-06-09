# Derivation 82 — GATE 0 SUMMARY (one screen)

**Milestone:** v22.0-candidate (η-reading test). **Gate 0 ONLY** (Gates 1/2/3 not
run — orchestrator routes next). **Exact over Q**, det SSOT, no `numpy` on the
decisive path, no `octonion_algebra` (source-guarded), no `κ`/`Λ`/physical constants.

Driver: `PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py` → **exit 0, ALL_PASS**.

## Load-bearing numbers (all exact over Q)

| Quantity | Result | Iso type | Expected | Status |
|---|---|---|---|---|
| `P` (conjugating automorphism, `P·E_11=E_22`) | exact `F_4` **signed permutation**, `P²=I`, `det=1` | — | replaces Phase 52 numeric `P` (1.9e-15) | ✓ exact |
| `dim Stab_{F_4}(E_11)` | **36** | `spin(9)` | 36 | ✓ |
| `dim r_12` (joint frame stabilizer) | **28** | `spin(8)` (triality) | 28 | ✓ |
| **slice-action residual on `h_2(C_u){1,2,3,10}`** | **dim 1** | **`so(2) ≅ u(1)`** | "e.g. so(3)" (illustrative) | ✓ (smaller, see note) |

## Explicit P

Conjugation by the real `3×3` swap `(0↔1)`: `α↔β`, `γ` fixed (the `E_11↔E_22` swap,
`E_33` fixed); off-diagonal `x1 ↔ x̄2`, `x3 ↔ x̄3` (octonion conjugation ⟹ sign-flip
on all imaginary comps). Preserves the Jordan product on all `27×27` basis pairs and
`det_3/Tr/Tr2` on a generic symbolic element. Identification coset
`{g : g·E_11=E_22} = P · Stab_{F_4}(E_11)` (dim-36 `P`-translate).

## Slice residual detail

`r_12 = spin(8)` acts faithfully on `V_0 = h_2(O)` (rank 28, **no leak** out of
`V_0`). Slice-preserving subalgebra = **dim 16**; 12 of 28 gens mix the slice with
the internal W-sector `{4..9}`. The surviving **dim-1** generator is the **`SO(2)`
rotation in the `{p,q}` plane** (`p=Re x1`, `q=⟨x1,e_7⟩`) = the **phase of the
complex line `C_u=span{1,e_7}`**; `so(3,1)`-valued (antisym under `η=diag(+,−,−,−)`),
`block² = −1` on `{p,q}` (genuine compact rotation). Confirmed by **3 independent
routes** (slice sub-block / `so(3,1)`-projection / full `gl(4)`), all = **1**.

## VERDICT / ROUTING

> **`RESIDUAL-SURVIVES`** (deterministic ladder, derived from computed `slice_dim=1`,
> self-tests pass). The 2-point identification keeps a residual **`so(2)≅u(1)`** slice
> freedom (the `C_u` phase). **Per the pre-registered wrinkle a compact residual is
> NOT a kill.**
>
> **→ RECORD the dim-1 residual; PROCEED TO GATE 1** (the canonicalization sweep —
> does `u`-alignment / `det_2`-isometry / Peirce-block / interface-intertwining cut
> this `so(2)` to triviality?).

## Note (deviation from brief, flagged)

Brief illustrated the residual as "e.g. `so(3)`" (dim 3); the exact result is
**`so(2)=u(1)` (dim 1)** — smaller because `r_12` fixes the diagonal `(β,γ)` ⟹ cannot
rotate `x3=(β−γ)/2` against `{p,q}`; only the intra-`C_u` `{p,q}` phase survives.
Same routing verdict, same wrinkle (compact, not a kill). Reported, not silently
adopted.

## Anti-overclaim

Structure-only identification space. Does NOT prove independence (Gate 2 holonomy),
NO metric law / `G=κT` / dynamics, does NOT touch the exhausted v17–v21/Sakharov
six-kind menu.

## Artifacts

- `code/kkt_gluing_holonomy.py` — reusable Gate-0 harness (source-guarded, exact-Q,
  self-tested verdict ladder).
- `derivations/82-kkt-gluing-RESEARCH.md` — full setup, exact definitions, engine
  map (file:line), results, modeling choices.
