# Derivation 82 — GATE 1 SUMMARY (one screen)

**Milestone:** v22.0-candidate (η-reading test). **Gate 1 ONLY** (the canonicalization
sweep). **Gate 2 NOT run** — orchestrator routes next. **Exact over Q**, det SSOT, no
`numpy` on the decisive path, no `octonion_algebra` (source-guarded), no
`κ`/`Λ`/physical constants.

Driver: `PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py gate1` → **exit 0,
ALL_PASS**.

## The residual chain (exact over Q) — the headline

| Step | Condition added | kept | slice residual | iso |
|---|---|---|---|---|
| `R_12` | (Gate-0 start) | 28/28 | **dim 1** | `so(2)≅u(1)` |
| `R^(1)` | + u-alignment | 28/28 | **dim 1** | `so(2)` |
| `R^(2)` | + det_2 isometry | 28/28 | **dim 1** | `so(2)` |
| `R^(3)` | + Peirce-block | 28/28 | **dim 1** | `so(2)` |
| `R^(4)` | + interface intertwining | 28/28 | **dim 1** | `so(2)` |

> **`R_12 ⊇ R^(1) ⊇ R^(2) ⊇ R^(3) ⊇ R^(4)` = `1 ⊇ 1 ⊇ 1 ⊇ 1 ⊇ 1`.**
> **ALL FOUR conditions AUTOMATIC; NONE cuts the `so(2)=u(1)` C_u-phase residual.**

Confirmed by **two independent routes**: (a) generator-filtering (`gate1_sweep`); (b)
joint-linear-nullspace on `D(t)=Σ t_k gens_k` — the cond1+cond2 slice-constraint
matrix has **rank 0**, cond3+cond4 add **no rows** ⟹ surviving slice residual dim 1.

## Per-condition status (AUTOMATIC / NON-TRIVIAL)

| # | Condition | Status | Why |
|---|---|---|---|
| 1 | u-alignment | **AUTOMATIC** | the residual IS the C_u phase (`e_3↦−e_10`, `e_10↦e_3`, nothing else) ⟹ commutes with the C_u complex structure `J` |
| 2 | det_2 isometry | **AUTOMATIC** (verified) | the slice block is `so(3,1)`-valued (`F_4⊂Aut`) |
| 3 | Peirce-block preservation | **AUTOMATIC** (verified) | `D·E_11=0 ⟹ [D,L_{E_11}]=0 ⟹` preserves V_1,V_{1/2},V_0 |
| 4 | interface intertwining | **AUTOMATIC, NON-VACUOUS** | `r_12 ⊂ Der(h_3(O))` preserves every Peirce product & fixes the frame |

## Condition 4 — the exact operator equation + flagged choices

**Equation (Peirce-canonical, derived from Peirce structure alone):** for all
`x,y ∈ V_{1/2}(E_11)`,
```
Π_{V_0(E_11)}( (Dx)∘y + x∘(Dy) )  ==  D( Π_{V_0(E_11)}( x∘y ) )
```
i.e. **D is an infinitesimal derivation of the Peirce quadratic map**
`Q_11(x,y) = Π_{V_0(E_11)}(x∘y) : V_{1/2}×V_{1/2} → V_0` (the "sequential-product data
on the shared channel"). Cross-frame form `g(Q_11)=Q_22(g·,g·)` splits into: **P
intertwines Q_11↔Q_22 exactly** (P∈Aut, verified on all 16×16 pairs over Q) + the
residual-D equation above.

**Shared V_{1/2} channel** `= V_{1/2}(E_11)∩V_{1/2}(E_22) = {19..26}` = the **x3 slot**
(connects E_11↔E_22).

**Flagged choices:** (1) `Q = Π_{V_0}(x∘y)` (the Peirce-0 component) is *the* canonical
quadratic map (McCrimmon Peirce rules), not hand-picked — the V_0-component is the
genuinely inter-frame channel (lands in the slice arena). (2) Default channel = full
`V_{1/2}(E_11)`; the shared sub-channel gives the same. (3) Infinitesimal (Lie)
reading of "intertwines."

**NON-VACUITY (teeth, demonstrated):** P **passes** the cross-frame intertwining; a
**non-derivation** map (P + spurious `x2→x3` cross-channel coupling) **FAILS** it. So
condition 4 could have obstructed; it doesn't, because the residual lives in the
frame-fixing derivation algebra.

## VERDICT / ROUTING

> **`RESIDUAL-SURVIVES`** (deterministic ladder from computed `final_slice_dim=1`,
> self-tests pass). No program-native compatibility condition cuts the `so(2)≅u(1)`
> C_u-phase residual ⟹ the identification `E_11→E_22` is **NOT canonically unique** —
> this **IS the two-point independence result** at the canonicalization level.
>
> **→ RECORD the surviving `so(2)`; PROCEED TO GATE 2** (three-point holonomy:
> `h = g_31∘g_23∘g_12` — forced identity = route DEAD / global-flat vindicated;
> choice-dependent = independence proved; forced-nontrivial = curvature seed). Sweep
> the residual classes (the `U(1)` freedom).

## Anti-overclaim

Two-point independence ONLY (the four conditions don't force a canonical flat
identification). Does NOT prove loop independence (Gate 2), NO metric law / `G=κT` /
dynamics, does NOT establish the No-Absolute-Objects "bridge" (argued separately,
§9.2), does NOT touch the exhausted v17–v21/Sakharov menu. Compact `so(2)` = the
Phase-48 fact (boosts metric-side), not evidence about boosts.

## Artifacts

- `code/kkt_gluing_holonomy.py` — Gate-0 + Gate-1 harness (source-guarded, exact-Q,
  self-tested ladders); Gate-1 driver: `... gate1`.
- `derivations/82-kkt-gluing-RESEARCH.md` — full Gate 0 + Gate 1 (the operator
  equation, flagged choices, residual chain, cross-checks).
