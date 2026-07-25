# v32.0 MILESTONE RATIFICATION DIRECTIVE — paste into the GPD session
# Bryan has RATIFIED v32.0-B LIVE (human ratification, 2026-06-12). The blog-side
# six-location propagation is DONE. This directive authorizes the GPD-side milestone
# bookkeeping. This is BOOKKEEPING, not a new research run — the verdict is already
# computed, reconciled, and committed (e8fcbcf2). Do NOT re-derive; record.

## 0. Authorization + what NOT to touch

Bryan ratifies **v32.0 (The Tensor Dictionary) COMPLETE — VERDICT LIVE (v32.0-B,
reconciled across three paths).** Record it BY HAND across the four milestone files,
mirroring the v31.0 entries exactly:
- `.gpd/state.json` (`current_phase_name`, `current_plan`, `status`, `last_activity_desc`)
- `.gpd/MILESTONES.md` (a new `## v32.0 …` entry after the v31.0 entry at line 807)
- `.gpd/PROJECT.md` (the milestone rollup, mirroring how v31.0 was logged)
- `.gpd/STATE.md` (GPD's own state)

**TRANSITION BY HAND.** Do NOT run `gpd phase complete`, `state advance`, or
`/gpd:complete-milestone` — they are buggy (see [[feedback_gpd_phase_complete_gotcha]];
v31.0 and v17.0 both transitioned by hand). Edit the files directly.

**STOP RULE (binding):** the reconciled numbers below are the committed `92-VERDICT.md`.
Before writing, open `92-VERDICT.md` and confirm κ_full=1/30, ε=20, the triple-27
straddle, T₂₇[P27(M⊗M)], c₈=c₁=0. If ANY committed number disagrees with this
directive, HALT and report — do not paper over a mismatch.

## 1. The verdict to record (RECONCILED — use these, NOT the first pass)

**VERDICT: LIVE — the tensor sector's SOURCE DATA closes in canonical form (a
dictionary fact, strictly stronger than v31's existence).** On the frozen cut
CP²=h₃(C_u) (Fubini–Study, Kähler–Einstein, Ric=6g, Λ=6, λ₁=12, λ₂=32):

- **‖TT(B3)‖² = (1/30)·(TrM²)²** — single FORCED rational κ=1/30, **detM ABSENT**
  (the only degree-4 SU(3)-invariant of a traceless 3×3 is (TrM²)², Cayley–Hamilton).
  Confirmed exact over Q on s01/a01/d1 (‖r‖²=2/15), d2 (detM=−2), and a generic
  detM≠0 matter.
- **ε = λ_L − 2Λ = 32 − 12 = 20** — λ_L=32 is the eigenvalue of the WHOLE TT mode;
  non-marginal.
- **Direction = T₂₇[P27(M⊗M)]** — the 27-channel of Sym²(8)=27⊕8⊕1, **c₈=c₁=0**
  structural. The first-pass d-symbol-square hypothesis c∝N(M) FAILED (N(M) is the
  8-channel; N(s01)=N(d1) yet the residues differ). Fingerprints T1/T2/T3 exact/Q.
- **The mode = a SINGLE λ_L=32 Lichnerowicz eigentensor STRADDLING the triple-27:**
  the (1,1)-dim-27 (Boucetta Table V/VIII **row 2**, m=0: 4(m+2)(m+4)=32, dim 27,
  φ∘δ*_h∘δ̄*_h(T^{0,0}_{2,2})) ⊕ the (2,0)+(0,2)-dim-27s (Tables VI/VII row 1). All
  three blocks nonzero; forced norm split ‖TT⁽¹¹⁾‖²:‖TT_anti‖² = 5:4 = (1/54):(2/135),
  one overall κ_full=1/30. There is NO TT mode at λ=12 (the two dim-8s there are
  non-transverse/trace) ⇒ Koiso rigidity intact, the trap-#16 tension dissolves.

**Forced closed form:** TT(B3[M]) = T₂₇[P27(M⊗M)], T₂₇ the fixed straddling
equivariant map, ONE forced constant. This is the deferred v31 positive-exhibit
certificate PLUS the strictly higher v32 bar (the geometry tells matter how much TT
it gets, no fitted constant).

## 2. The three-path reconciliation (record it — the protocol is the achievement)

- Executor: right on λ_L=32/ε=20; WRONG on the κ-object (reported 1/54 = the
  (1,1)-block share, not the full mode) and the multiplet name ("λ=12 dim-8 adjoint").
- Independent verifier (`c5d66e25`, `92-VERIFICATION.md`): right on κ_full=1/30 and the
  refutation of v31's "jointly gauge" localization; WRONG on ε (read Boucetta row 1 → ε=0).
- Blog-side: caught the multiplet ID (the residue map factors through Sym²(8), pure
  27-channel; T1/T2/T3 exact/Q on this driver) and fetched Boucetta arXiv:0712.2830 as
  the arbiter (row 2 = the (1,1)-27 at 32). No single path had the full picture.

## 3. Fences (VERBATIM from 92-VERDICT.md §V5 — binding, carry into every file)

LIVE is a DICTIONARY fact of a FROZEN imported geometry. **No dynamical metric, no
selection law, no κ (Newton).** NO Einstein-equation / G=κT / dark-matter / geodesic
language. The frozen Fubini–Study geometry is USED, not derived. The v18/v20
MM-connection corpse stays buried (the BASE's deformation complex on CP², not a
fiber-built spacetime connection). The v18 Ph77 / v21 16-vs-6 rank wall, the
constructed-vs-extremized gap, the Riemannian signature, and the base/format clamp are
untouched. v32 does NOT retract v17–v21 (Block-C statements; v32 is the strictly weaker
upstream dictionary). Paper 5 remains the only result in the more-than-nothing column.

## 4. Honest evidence level + the DEFERRED OBLIGATION (mirror v31's deferred exhibit)

Record verbatim in the milestone's scope section:
> **ε=20 for the full mode is NOT yet on a directly-run full-block operator.** It rests
> on Boucetta Table V/VIII row 2 + the degree-counting argument (the anti content has
> bidegree (2,2), reachable only in T^{0,2}_{2,0} at 32) + the (1,1)-block Schur scalar
> (both independent (1,1)-operators gave 32 on r[1]) + the fingerprint single-rep
> certificate. The executor's full-tensor `lichnerowicz` anti path is FLAGGED UNTRUSTED
> (returned a spurious 28/4; duplicate def removed). **DEFERRED to v33 Gate-0 as a
> BINDING obligation:** build a correct full-tensor Δ_L and confirm Δ_L r = 32·r on
> EVERY block of r (control: a fixed full Δ_L must return 32 on each block). Failure to
> exhibit there = STOP + revisit the ε=20 grade. (This mirrors v31's deferred
> positive-exhibit obligation, which v32 Gate-0 discharged.)

## 5. The v31 amendment (carry as a STANDING amendment — do NOT rewrite the v31 record)

The ratified v31.0 records stay INTACT. Append a one-line amendment pointer to:
- the v31.0 `MILESTONES.md` entry (after the through-line, before the `---`), and
- the v31 `status`/`last_activity_desc` once they are superseded by v32.0:

> **AMENDMENT (v32.0-B, see `derivations/91-AMENDMENT-v32.md`):** v31's EXISTENCE verdict
> STANDS (re-confirmed three ways). v31's isotypic localization — "(2,0)+(0,2) jointly
> gauge ⇒ the λ=12 (1,1) dim-8 adjoint" — is RETRACTED: the residue is a single λ_L=32
> eigentensor straddling the triple-27 (Boucetta row 2 (1,1)-27 ⊕ rows VI/VII anti-27s),
> all blocks nonzero. The "deficit 1 forced by Sym²(8)⊃adjoint once" count is right but
> the CHANNEL is the 27 (Sym²(8)⊃27 once), not the 8.

The `status`/`last_activity_desc`/`current_phase_name` fields are OVERWRITTEN with the
v32.0 content (§1–§3); the v31 stale "λ=12 dim-8" language survives only in the
historical MILESTONES.md entry, now amendment-flagged.

## 6. Artifacts to cite (all committed)

- `e8fcbcf2` — the v32.0-B reconciliation close-out (10 files).
- `derivations/92-VERDICT.md` (reconciled), `derivations/92-tensor-dictionary-RESEARCH.md`
  §§7–9, `derivations/91-AMENDMENT-v32.md`, `92-GATE-{0..5}-SUMMARY.md` (banner-corrected).
- `code/lichnerowicz_response.py` (executor; anti path flagged untrusted, duplicate def
  removed), `code/lichnerowicz_response_verify.py` (`c5d66e25`; caught κ=1/30 + the v31
  regression), `code/lichnerowicz_response_fingerprint.py` (`8bfb73c9`; T1/T2 + κ_full=1/30
  + the 5:4 split, exact/Q on the driver).
- The reconciliation reasoning: `v32-reconciliation-directive.md` (blog-side).

## 7. Through-line (for the milestone entry, mirror v31's)

v24 field → v25 closed form + forced operator → v26 source + MaxEnt (λ₂=104) → v27 local
balance law (LIVE) → v28 topological skeleton → v29 global-time closed → v30 form-selection
fork closed → v31 the tensor wall OPENS (LIVE, EXISTENCE) → **v32 the tensor DICTIONARY
closes: the matter-sourced TT mode is a single λ_L=32 eigentensor straddling the triple-27,
its norm the FORCED ‖TT(B3)‖²=(1/30)(TrM²)² (detM absent), its direction T₂₇[P27(M⊗M)], its
Δ_L-stiffness ε=20 — the program's first forced tensor-response coefficient (LIVE); the
selection law (Block C) still open.**

## 8. NEXT (record, then STOP)

**NEXT = HOLD.** The v33 ledger (Gate-5, priced only): the lapse/00 assembly, the OP² lift
(Spin(9), not Kähler — price, do not assume), the full-block Δ_L verification (§4, binding),
and the fenced Fredholm/response reading of ε (Block-C-shaped, named, NOT run). **The v33
prompt comes from blog-side — do NOT self-register a v33.** The GOVERNANCE TRIPWIRE binds
after v32 + the lapse/00 assembly: the NEXT registered run must BE the Block-C confrontation
(what, if anything, FORCES the metric response).

Human-ratified (Bryan), exact over Q. Record, transition by hand, report the commit.
