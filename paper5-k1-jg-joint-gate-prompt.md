# Paper 5 — JG: bounded-rank GLOBAL joint coherence at the actual K (the K1 decider)

## TASK TYPE
Settle ONE claim (**CLAIM JG**, §0) under a PINNED pre-registration:
`~/repos/blog/research/qm-genericity-review/K1-JOINT-GATE-PREREG.md` — read it
FIRST. It is CLOSED; only its ledger may be appended. The original prereg
`K1-BRANCH-B-PREREG.md` remains binding for bars and doctrine (V1, A1–A5).
Anti-glaze; grades ([PROVED]/[CERTIFIED]/[COMPUTED]/[ARGUED]) on every claim;
exact arithmetic where decisive. Fired 2026-07-03 on Bryan's explicit go.

## 0. The one claim to settle

> **CLAIM JG.** At the actual extracted kernel K (the packed witness battery),
> there exists a BOUNDED-RANK globally coherent level-2 assignment: ONE
> continuous choice of (label branch, R_ν) over the whole cell continuum —
> all atom pairs on all generated faces, all pencils through shared atoms,
> for the tested frame pairs — satisfying simultaneously (i) per-cell duality
> + positivity (exact convex LP SWEPT OVER ALL FOUR LABEL BRANCHES), (ii)
> cross-disk / pencil coherence (shared-atom norming consistency;
> cross-transitions matching ambient), at a hidden rank that stays bounded as
> the sampled cell set densifies.

Methodology: the joint minimal rank curve r*(N) as the sampled cell/pencil
count N grows — SATURATION vs GROWTH, the level-1 pattern that survived
review. Verdict semantics are the JG prereg's own (BUILD / FAIL / UNRESOLVED);
do not restate them, follow them.

## 1. Pinned run parameters (J2 — declared in the JG ledger BEFORE this file)

- **Rank ceiling r_max = 16** — mirror of G2's m' ≤ m+3 = 13+3. A joint
  witness needing rank > 16 cannot feed G2 and does NOT count as BUILD. No
  post-hoc raising to chase a build; no lowering to fake growth. Report
  r*(N) against this ceiling.
- **Densification:** ≥ 4x growth of the sampled cell set from a documented
  base set. Document the base set in the ledger before the first actual-K
  read (J4).
- **K battery (A2, ≥ 2 independent ancestries):** `witness_n40_m13.npz` +
  `landing_n40_m13_w24-j0.02.npz` (designated fat-interior source) MANDATORY;
  `landing_n40_m13_w32-j0.05.npz` third where budget allows. A one-basin
  verdict is not a result.
- **Joint-rank definition:** formalize explicitly (e.g. dimension of the
  joint span of all face carriers H_ν in the ambient, or the minimal common
  hidden dimension supporting all face-data simultaneously — your call, made
  once), then FREEZE it as a ledger append BEFORE any actual-K cell is read.

## 2. What is new relative to G1 (read `k1_g1_VERDICT.md` §0-A first)

G1 settled the PER-CELL question: no local lever at the actual K — every
tested cell is feasible once the LP is swept over the four gauge-distinct
label branches (the G1 lesson: labels are existentially-quantified face DOF;
a fixed-label certificate is void). What G1 did NOT test: whether the
per-cell solutions PATCH — one continuous (branch, R_ν) field over all cells
and pencils at once, at bounded joint rank. Per-cell existence is pointwise;
JG is the sheaf question. The load grows superlinearly (witness-active set
96→620 while cells grow linearly), which is exactly where growth could hide
after local saturation.

Constructive ansatz (pre-registered in the JG doc): the reviewer-observed
continuous branch structure — θ_r ≈ 0, θ_u sweeping smoothly across α-bands.
Start there: attempt the explicit continuous field first, then stress it.

Joint coherence constraints to encode (formalize precisely, freeze pre-read):
1. Per-cell: ω⁰-eliminated convex LP feasibility (duality collapsed to the
   one linear eq via ⟨sig_p−sig_q, p−q⟩ = 2−α−β; positivity exact via
   max_w⟨s, ½R+Hw⟩ = ½⟨s,R⟩ + ‖Hᵀs‖₄), min over ALL FOUR branches (C4).
2. Pencil/shared-atom: cells sharing an atom use ONE consistent norming and
   face-datum restriction on the shared atom.
3. Cross-disk: transition data match the ambient α, β from the clamped K
   (reply_009/reply_010 arena formulas).
4. Continuity: one continuous (branch, R_ν) assignment — branch switching
   only where branches actually coincide/cross, never as a free per-cell
   re-choice.
5. Bounded rank: all face carriers jointly within r ≤ r_max = 16.

## 3. Controls (GATE the run — no actual-K cell is read before C1–C3 pass)

- C1 p=2 rebit joint: MUST BUILD (composes at dim 10; a joint encoding that
  kills the rebit is mis-normalized — fix before reading ℓ⁴).
- C2 K=0 joint: must reproduce T-COH's exact-zero 2-disk joint at bounded
  rank.
- C3 Coincidence limit: joint assignment collapses to the own-disk solution
  as the frame pair degenerates.
- C4 Branch sweep everywhere (any one-branch claim is void).
- C5 Iteration/rank-scaling discriminator + nit discipline on every boundary
  cell; SCALE=1e12 ftol lesson; true ℓ^{4/3}→ℓ^{4/3} norms only, no spectral
  proxy; first-touch vs cap-shrink ladder for margins.

## 4. Verdict discipline (J1/J5 — read before running anything)

- J1: the WANTED outcome (Bryan's fork call) is FAIL/lever — therefore attack
  FAIL hardest. A false global lever is the worst possible outcome. Note the
  instrument asymmetry: cells whose tightest legal cap is within 10x of the
  1e-6 bar cannot certify INFEAS (n=40 asymmetry) — a numeric GROWTH claim
  needs the full packing-sweep discipline (V1-INFEAS per cell, ≥2 ancestries,
  starvation battery per A2, branch sweep per C4), and a clean FAIL likely
  needs an EXACT certificate (rank obstruction / semialgebraic / SDP dual
  with stated tolerances) rather than a numeric curve.
- Every r*(N) BUILD point: brute-gated per V1 (< 1e-6, eq < 1e-7, 10x
  cross-check).
- **J5 STOP RULE: you do NOT bank a decisive verdict.** Write
  `k1_jg_VERDICT.md` with the verdict marked **PENDING COLD REVIEW**, append
  the ledger run-line marked the same, and REPORT BACK. The driver spawns the
  isolated cold review. Only after that review does anything get banked.

## 5. Data and artifacts (in place; do not re-derive banked items)

- K battery: `kernel_kblocks_close_pairs.npz` + `kernel_kblocks_log.txt`
  (K 2x2 blocks, both directions, all sign combos, pairs (1|R):(0.00,0.09)
  and (0.18,0.09), THREE witnesses); kernel reports `kernel_report_n*.npz`;
  witnesses `witness_n{12..40}_m13.npz`; landings `landing_n40_m13_*.npz`.
  Box `/mnt/c/Users/ehrli/qm/` and repo review dir.
- Corrected per-cell tooling: `k1_g1_convex.py` (ω⁰-eliminated LP; correct
  once branch-swept) + the reviewer's branch-sweep scripts
  `k1_g1cr_{labels,density,reconstruct,othersectors}.py` — REUSE this core;
  it is the validated instrument.
- Coherence encoding to extend: `k1_tcoh_01..05_*.py` (labels → witness →
  positivity → consolidate → joint at K=0); `k1_tower_level1.py` (frames,
  duality-eliminated parametrization, golden-refined ℓ^{4/3} norms).
- Arena formulas: reply_009 / reply_010 in `~/.codex-channels/k1-composability/`
  (α, β at general K; T4 flip condition for the later G2).
- Story + lessons: `HANDOFF-K1-OPUS.md` §0; `k1_g1_VERDICT.md`;
  `k1_tcoh_VERDICT.md`.

## 6. Box ops (ALL compute there — Mac on battery, NO local compute)

`ssh -i ~/.ssh/id_ed25519 -o IdentitiesOnly=yes ehrli@192.168.4.108 'wsl bash
-lc "..."'`, dir `/mnt/c/Users/ehrli/qm/`; scp to `ehrli@…:qm/`. Long runs:
wrap the local ssh in `caffeinate -i`, keepalives 30x40, run_in_background,
tee to a box-side log, PERSIST PARTIAL RESULTS INCREMENTALLY (landing-file
pattern — a pipe death must not vaporize results). WSL kills EVERYTHING
(setsid/nohup/tmux/the VM) when the last ssh session closes. pkill self-match
gotcha (verify with follow-up ps). NO schtasks (permission-denied; Bryan-only).
Simple remote commands only (nested quoting fails). `~/.ssh/config` /
`known_hosts` reads are permission-DENIED — do not attempt.

## 7. Output

- Verdict on CLAIM JG: **BUILD / FAIL / UNRESOLVED**, marked PENDING COLD
  REVIEW; the r*(N) table with per-point brute gates; controls results
  explicitly, either way; grades per claim.
- Scripts `k1_jg_*.py` in the review dir; verdict file `k1_jg_VERDICT.md`;
  JG ledger appends (instrument+controls line; frozen joint-rank definition;
  run line PENDING COLD REVIEW). NO other prereg edits. NO SSOT flip; no git
  commits.
- **Progress cadence (Bryan requires visible progress):** report back at
  (a) instrument built + controls C1–C3 passed, (b) first r*(N) points,
  (c) verdict written. If blocked > ~1h wall-clock on infrastructure, report
  that too.
