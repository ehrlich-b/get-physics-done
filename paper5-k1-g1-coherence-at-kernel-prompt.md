# Paper 5 — G1: coherent level-2 feasibility at the kernel's ACTUAL K (first promotion gate of the pre-registered K1 endgame)

## TASK TYPE
Settle ONE claim (**CLAIM G1**, §0), prove-or-disprove, decision tree, grades
([PROVED]/[CERTIFIED]/[COMPUTED]/[ARGUED]) on every claim. Anti-glaze. Exact
arithmetic where decisive. This gate runs under a PINNED pre-registration:
`~/repos/blog/research/qm-genericity-review/K1-BRANCH-B-PREREG.md` — read it
FIRST; its gates/bars/anti-goalpost clauses are CLOSED and may not be edited.

## 0. The one claim to settle

> **CLAIM G1.** Fix close legal Bell-frame pairs τ ≠ σ of the Niestegge ℓ⁴
> qubit with the cross-frame kernels CLAMPED to the actual extracted values of
> the banked saturated packing (battery in §2 — NOT the K = 0 idealization
> T-COH already settled). Then the coherent hereditary level-2 system — (i)
> one face-datum (R_ν, H_ν, G_ν) per generated face valid across its entire
> atom-pair continuum; (ii) pencil consistency through shared atoms; (iii)
> carrier-consistency (force from embedding); (iv) tilted-unit positivity
> DERIVED from 0 ≤ effect ≤ 1, never the imported ¼ ± P/8 form — is FEASIBLE
> at bounded hidden rank.

Prove (BUILD) or disprove (FAIL) per the prereg's V1 bars:
- **BUILD** = feasible, brute-gated (< 1e-6, eq < 1e-7, 10x cross-check).
  Consequence: half the kill; gate G2 (level-2 recursion at m' <= m+3) is next.
- **FAIL** = certified infeasible (> 1e-4 + flatline + hammer + the A2
  multi-ancestry battery). Consequence: BRANCH B — K1 undecided at this
  encoding, escalate to the level-2 encoding attack. NEVER "route survival."
- **UNRESOLVED** = anything between; escalate the instrument (exact
  arithmetic), never the claim.
There is NO wanted outcome at this gate: a false FEASIBLE glazes toward a fake
kill; a false INFEASIBLE fakes a branch-B rescue. Attack both directions.

## 1. What is new relative to T-COH (read its verdict first)

`~/repos/blog/research/qm-genericity-review/k1_tcoh_VERDICT.md`: at K = 0 the
coherent system is FEASIBLE (no local lever) — and its central mechanism, the
z-independent pinned D₄ label-orbit, is a K = 0 ARTIFACT: K = 0 makes ambient
transitions α, β constant per pair. At the ACTUAL kernel α, β VARY over the
atom-pair continuum, labels unfreeze and must TRACK the pair — the regime of
T-COH's coincidence control (K_ττ = ½I, labels track (r,u) = (y,z)), which
PASSED. So G1 probes between two passing endpoints (K = 0 and coincidence),
at the packing's real operating point.

**The extracted kernel's structure (kernel_kblocks_log.txt, [COMPUTED]):**
- Interior same-chamber neighbors (e.g. 1:s=0.18 x 1:s=0.09, R same): K^{++}
  and K^{--} ≈ (cap)·I₂ with cap = ¼ + P/8 ≈ 0.49987 — NEAR-COINCIDENCE,
  riding the box (slack down to 5e-9); cross-sign blocks ≈ 0 within their
  ~1e-4 caps. The packing saturates by CHAINING: neighbors nearly merge.
- Endpoint pairs (s=0.00 x s=0.09): structured non-aligned K (opn 0.32–0.50,
  slack up to 0.18), BASIN-DEPENDENT across witnesses.
So the analytic core of G1 is a PERTURBATION question: does the coincidence
solution deform smoothly to K = (½ − ε)·I, ε = (2 − P)/8 ~ 1e-4, under full
coherence (shared face-data + pencils + derived positivity)? Rank/Jacobian at
the coincidence anchor decides smooth deformability; then the numeric
encoding confirms at the actual clamped values.

## 2. Data and artifacts (all in place; do not re-derive banked items)

- K battery (box `/mnt/c/Users/ehrli/qm/` and repo review dir):
  `kernel_kblocks_close_pairs.npz` + `kernel_kblocks_log.txt` — K 2x2 blocks,
  both directions, all sign combos, pairs (1|R):(0.00,0.09) and (0.18,0.09),
  from THREE independent witnesses (witness_n40_m13, landing w24-j0.02 = the
  designated fat-interior source, landing w32-j0.05). Prereg A2: run the gate
  at >= 2 independent witnesses' K values; a FAIL claimed from one basin is
  not a result.
- Kernel reports `kernel_report_n*.npz` (opns/caps/eq/sv per witness);
  witnesses `witness_n{12..40}_m13.npz`, landings `landing_n40_m13_*.npz`.
- Encoding to rewire: `k1_tcoh_01_labels.py` … `k1_tcoh_05_joint.py` (labels →
  witness → positivity → consolidate → joint), `k1_tower_level1.py` (frames,
  duality-eliminated parametrization, ℓ^{4/3} norms — golden-refined; SCALE
  1e12 lesson), reply_009/reply_010 arena formulas in
  `~/.codex-channels/k1-composability/` (α, β at general K — the K-dependent
  ambient transition terms are THE rewiring).
- Level-1 story + instrument lessons: `HANDOFF-K1-OPUS.md` §0 (ftol floor,
  first-touch margins, nit discipline, starvation doctrine).

## 3. The decider — analytics first, encode second

1. **Coincidence-anchor perturbation (exact/sympy where possible):** write the
   coherent matching system at K = (½ − ε)I on one pencil; expand at ε = 0
   (the coincidence solution). Jacobian nondegenerate ⟹ smooth deformation
   exists for small ε [PROVED-local] — then the interior-neighbor clamps
   (ε ≈ 1.3e-4) are inside the tube, and BUILD for the chaining regime should
   follow numerically. Jacobian degenerate ⟹ the deformation may obstruct —
   locate the obstruction family (pencil? shared-datum? derived positivity?).
2. **Numeric gate at the clamped battery:** extend the T-COH encoding with
   K-dependent ambient transitions; clamp K per battery entry; solve for the
   coherent face-data over sampled pencil members; verdict per V1 bars.
   Include the STRUCTURED endpoint K's (not just the chaining ones) — that is
   where genuine novelty could hide.
3. **Whichever way it points:** BUILD ⟹ exhibit the witness (face-data over
   the continuum, rank) + state precisely what G2 still owes (recursion at
   m' <= m + 3, reply_010/T4). FAIL ⟹ the contradicting constraint family +
   exact certificate or the full V1-INFEAS discipline + the A2 battery.

**Controls (pre-registered; a run failing its control is discarded):**
- Coincidence limit ε → 0 reproduces the own-disk solution exactly.
- **p=2 rebit control (MANDATORY):** the rebit's coherent system clamped at
  ITS OWN packed-kernel analogue must BUILD (it composes at dim 10). An
  encoding that kills the rebit is mis-normalized — fix before reading ℓ⁴.
- Iteration-scaling discriminator on every boundary cell; nit printed always.
- True ℓ^{4/3}→ℓ^{4/3} norms only; no spectral proxy.

## 4. Box ops (compute THERE; Mac on battery)
`ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes ehrli@192.168.4.108 'wsl bash
-lc "..."'`, dir `/mnt/c/Users/ehrli/qm/`; scp to `ehrli@…:qm/`. Long runs:
wrap local ssh in `caffeinate -i`, keepalives 30x40, run_in_background, tee to
a box-side log, persist partial results incrementally (landing-file pattern).
WSL kills EVERYTHING (incl. tmux/VM) when the last ssh session closes; pkill
self-match gotcha; no schtasks (permission-denied). Simple remote commands
only (nested quoting fails).

## 5. Output
- Verdict on CLAIM G1: **BUILD / FAIL / UNRESOLVED** + grades per claim; the
  perturbation-analysis result at the coincidence anchor stated separately.
- p=2 control result, explicitly, either way.
- Scripts `k1_g1_*.py` in the review dir; verdict file `k1_g1_VERDICT.md`;
  fill the prereg ledger's G1 line (append-only, no other prereg edits);
  update `HANDOFF-K1-OPUS.md` §0 next-actions. NO SSOT flip; no git commits;
  report back the one-paragraph physical-register summary for Bryan.
