# 89 — GATE 3 SUMMARY: T3 (u-complex sector) — the verdict computation

**v29.0 Phase 89. Exact over Q/Q(t). VERDICT (sector) = DEAD.** Independently confirmed
(`89-GATE-3-VERIFICATION.md`, explicit constructive certificate).

The decisive test: does a global `H` satisfy `traceless(C_pH) = ⟨M,p⟩·traceless(C_pM)`
(symbolic `M`)? In the u-complex (cut) sector (8-param `M`):
- **`E_11`-alone: SOLVABLE** (`H`'s lower block `= ⟨M,p⟩·M`'s lower block + `I`-shift; no
  over-determination at a single face — the machinery is sound).
- **`E_11` + 2 cut families: `linsolve = EmptySet`** ⟹ NO global `H`.

So the level-2 part of `K⁽²⁾` is NONZERO ⟹ **sector verdict = DEAD**. The per-face `I`-shift
gauge (`H → H + c·1`) is quotiented (it leaves `traceless(C_pH)` invariant), so the DEAD is
not a gauge artifact; it survives on FULLY GENERIC faces (not a trap #6 artifact).

**Gate 3: T3 (u-complex) = DEAD.**
