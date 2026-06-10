# Derivation 82 — GATE 2 SUMMARY (one screen)

**Milestone:** v22.0 (η-reading test). **Gate 2 — the DECISIVE three-point holonomy.**
**Exact over Q**, det SSOT, no `numpy` on the decisive path, no `octonion_algebra`
(source-guarded), no `κ`/`Λ`/physical constants.

Driver: `PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py gate2` → **exit 0,
ALL_PASS**. Independent verification (different code path, from scratch):
`derivations/82-GATE-2-VERIFICATION.md` — **HIGH**, none of (a)(b)(c) failed.

## VERDICT: `LIVE-A` — INDEPENDENCE PROVED

The algebra does **NOT** force a canonical flat gluing between distinct observers' KKT
slices. The inter-observer three-point holonomy is an **unforced** choice (flat at the
canonical u-aligned base, nontrivial under the residual `C_u` phase).

## The decisive chain (exact over Q)

| Step | Result |
|---|---|
| **Bug-guard FIRED** | bare transpositions `τ` FLIP `u=e_7` (`L_τ·J = −J·L_τ`, antiholomorphic) ⟹ **INADMISSIBLE** (fail Gate-1 u-alignment); their loop `diag(1,1,−1,−1)` was the **predicted spurious LIVE-B** — DISCARDED |
| **Admissible base** | u-aligned 3-cycle `ρ` (`E_11→E_22→E_33→E_11`, preserves `u`, `L_ρ·J = +J·L_ρ`), **`ρ³ = I`** ⟹ base loop **FLAT** (`h_slice = I`) |
| **Structural reduction** | residual `⊂ Der` fixes both endpoints ⟹ intertwines ALL algebraic data ⟹ Gate-1 conds 1–4 can't cut it ⟹ **LIVE ⟺ joint-stab acts nontrivially on the slice** |
| **Joint-stab slice action** | `r_12 = so(8)` (dim 28); slice action = **nontrivial compact `SO(2)`** (dim 1, the `C_u` phase) ⟹ **LIVE** |
| **Holonomy `h(φ)`** | VARIES; `h(0)=I` (identity REACHABLE, flat) AND single residual phase ⟹ `h≠I` (nontrivial REACHABLE); `det_2`-isometry ∀φ |
| **so(3) add-on** | reachable group = a single **`SO(2)` = `U(1)`** (the `C_u` plane; conjugated phase-generators span **rank 1**), **NOT** full `SO(3)` |

> **DEAD / LIVE-A / LIVE-B ladder (non-hardwired, self-tested):** base flat + varies +
> identity reachable ⟹ **LIVE-A**.

## What it establishes / leaves open (binding caveats)

- **Establishes:** independence ONLY — the axioms do not force a canonical flat
  identification (the independence half of the implementation-dictionary route), exact.
- **Leaves open:** the freedom is **one internal `u`-phase = a gauge-flavored spatial
  `SO(2)/U(1)`** (Berry/MM-shaped, **NOT metric-shaped**); it is **NOT** a tetrad /
  frame-gluing field (boosts are never algebra-internal, Phase 48). The **No-Absolute-
  Objects "bridge"** clamp is untouched (argued separately, `substrate-dictionary-gravity.md`
  §9.2).
- **No promotion past independence:** no metric law, no `G = κT`, no dynamics; the v17–v21
  six-kind metric-selection menu stays exhausted; v12/v13 Einstein untouched.

**Deliverables:** `code/kkt_gluing_holonomy.py` (gate2 driver), `derivations/82-kkt-gluing-RESEARCH.md`
§G2, `derivations/82-GATE-2-VERIFICATION.md`. Milestone verdict paragraph: RESEARCH.md tail.
