# GPD Directive: Ratify and Record v36.0 — Faithfulness Clamp DEAD-POINTWISE / fork A proven

**RATIFIED on the blog side after independent verification. Record v36.0 BY HAND**
(the `gpd phase complete` / `state advance` path is buggy — do NOT use it). Mirror the
v35 recording exactly.

## Verification done before ratifying (blog side)

- Read `96-VERDICT.md`, `96-VERIFICATION.md` (fresh-from-scratch CP² engine, not a re-run),
  `96-ADVERSARIAL-CHECK.md`.
- Re-ran, exit 0, exact over ℚ: `faithfulness_clamp.py` (**24/24**), `adv_kernel_96.py`
  (**20/20**), `adv_circularity_96.py` (**12/12**).
- Confirmed the decisive facts directly, not via PASS counts:
  - the ensemble-mean multiplier `m_proj = {0:1, 12:0, 32:0}` (rank-1 constant-mode
    projector) ≠ the Laplacian `m_Δ = {0:0, 12:12, 32:32}` — the φ-map's only non-locality
    is provably NOT a derivative;
  - `β = 0` over-determined on the λ=12 and λ=32 carriers (the local-Δ_FS coefficient is
    identically 0);
  - even an imported kernel gives the scalar `□φ_M = −12 φ_M`, never the ε=20 Lichnerowicz
    tensor;
  - the adversarial caught and fixed its OWN vacuous-QGT trap (`Tr(P∂P∂P) ≡ 0` for rank-1)
    before relying on it ⇒ the Berry-channel kill is real.

**Verdict: DEAD-POINTWISE / fork A PROVEN, CONFIDENCE HIGH. Ratify.**

## Record by hand (mirror v35)

- `state.json`: advance to v36.0, verdict `DEAD-POINTWISE`.
- `MILESTONES`: v36.0 entry.
- `PROJECT` / `STATE`: the state-fp⟹metric-fp clamp is refuted; the variety menu and the
  clamp are exhausted; fork A proven (with the scope-guard below).
- memory: mirror the v35 memory write.

## Scope-guard — bind into the record, do NOT overclaim

Record as: **"the state-fp⟹metric-fp clamp is REFUTED; fork A proven ON THE MENU /
for geometry-respecting (U(3)-invariant) self-modeling."**

- **NOT** "gravity proven impossible." Fork B (off-menu — a homogeneity-breaking or
  scale-importing self-modeling map not in the corpus) is NOT excluded. But inserting one
  is the program's standing **fp-import fence**, and even then it gives the WRONG TYPE
  (scalar `□φ_M`, not the ε=20 tensor).
- Residual = the standing import fence, **not a fresh assumption** (weaker than v35's
  interpretive step). Math HIGH.

## Fences (verbatim, carry into the record)

NO Einstein / `G=κT` / gravity / Newton / dark-matter / geodesic as a DERIVED result; the
bits↔area / induced-`G` rate is a framework ratio, NOT Newton's G; FS is USED, not derived;
signature Riemannian (**Wall 2 UNPAID** — nothing is called gravity until signature is paid).
Does NOT retract v33 (extremize), v34 (induce), v35 (DEAD-FISHER), v17–v21 (fiber kills),
v23 (I/3 death). Paper 5 remains the only result in the more-than-nothing column.

## After recording

**Do NOT self-register the next slot.** Hold. The next direction is decided on the blog
side (Bryan + the open-ended research repo).
