# Phase 73 (C — Einstein Structure) — Cross-Phase Consistency Check (RAPID)

**Mode:** rapid (post-phase, single-phase vs full accumulated conventions ledger)
**Phase checked:** 73-c-einstein-structure (plans 73-01 BUILD + 73-02 TEST) — the FINAL phase of milestone v17.0
**Verdict under check:** NONE (curved but not Einstein-structured), human-ratified 2026-06-01
**Date:** 2026-06-01
**Consistency status: CONSISTENT** (1 pre-existing non-blocking notation WARNING, carried — not introduced here)

---

## Scope

Semantic cross-phase consistency of Phase 73 against the full convention ledger (`gpd convention list`, 32 entries / 18 canonical) and the accumulated state (STATE.md, state.json, Phase 70.1/71/72 SUMMARYs + circularity audit). Within-phase correctness (the G[g] computation, the n=4 decomposition, the linsolve) is the verifier's job; this report checks that Phase 73's consumed/produced quantities and conventions are coherent with what the producing phases established.

---

## 1. Convention Compliance (Phase 73 vs FULL ledger)

| Convention (ledger) | Relevant to Ph73? | Compliant? | Evidence |
|---|---|---|---|
| metric_signature (mostly-minus, (1,3) Lorentzian slice) | YES | YES (operationally) — see WARNING-1 on the string | `eta_bg=J^T diag(+1,-1,-1,-1)J`, eigen-signs {+1,-1,-1,-1} = (1,3); every decisive number from `eta_bg` |
| natural_units (hbar=k_B=1, a=1) | YES | YES | "natural units (hbar=c=k_B=1)" in both SUMMARYs + audit |
| arithmetic_field (EXACT over Q; sympy ranks, never numpy) | YES | YES | all decisive quantities rational; `fp-float-decisive` rejected; `eig_signature_count` via sympy real_roots |
| cubic_norm / det_3 cross-term 2Re((x2 x1)x3); SSOT = bulk_geometry_verification.py; octonion_algebra.py BANNED | YES | YES | `fp-wrong-cross-term` rejected; det_3 SSOT byte-identical to ring_lemma_verification; engine ALL_PASS exit 0 |
| jordan_product / Tr(X∘Y) | YES (psi via det_3 cross-term, Jordan-derived) | YES | psi = 2Re((x2 x1)x3) via oct_mul (Fano e1 e2=e4) |
| octonion_convention (Fano e1 e2=e4) | YES | YES | engine oct_mul, audit T3.a |
| complex_structure (u=e_7), clifford_signature Cl(9,0), group F_4, rep 27=1+26 | inherited (slice algebra) | YES | unchanged; engine carries them; no redefinition |
| coupling_convention (J>0 AFM) | NO | N/A | no spin Hamiltonian in Ph73 (gravity/geometry phase) |
| fourier, gauge_choice, regularization, renormalization, coordinate_system, index_positioning (canonical "N/A pure algebra"), time_ordering, covariant_derivative_sign, creation_annihilation_order | NO | N/A | pure differential geometry of a fixed background; no field-theoretic machinery |
| levi_civita_sign (ledger: "N/A") | borderline | OK | Ph73 uses Levi-Civita *connection* (Christoffels) for the hand-rolled Riemann cross-check, but no epsilon-tensor / dual; ledger "N/A" refers to the epsilon symbol, which is genuinely unused. No conflict. |
| spin_basis, state_normalization, generator_normalization, gamma_matrix_convention, commutation_convention | NO (or inherited, untouched) | N/A / YES | not exercised by the curvature computation |

**Compliance result:** 8 relevant conventions checked, all compliant; ~10 correctly N/A with reason. No silent skips.

### Newly-introduced Phase-73 conventions (checked for consistency with ledger)
- `eta_bg` constant null-aligned KKT pullback `[[0,1/2,0,0],[1/2,0,0,0],[0,0,-1,0],[0,0,0,-1]]`, inverse `[[0,2,0,0],[2,0,0,0],[0,0,-1,0],[0,0,0,-1]]`. **Verified exact:** `eta_bg · eta_bg^{-1} = I_4`; signature (1,3). Consistent with the 70.1/71/72 "det_2 Lorentzian slice, timelike x_0 = beta+gamma".
- box = `eta_bg^{ab} ∂_a ∂_b = 4 ∂_β∂_γ − ∂_p² − ∂_q²`. **Verified:** coefficients read from `eta_bg^{-1}` (β-γ cross = 2+2 = 4; p,q = −1). Engine pins the null-aligned inverse with an internal assertion (NOT a hard-coded diag) — confirmed in `code/bulk_geometry_verification.py:2488-2504`.
- `G_munu[g] = Ric − (1/2) g R`, indices raised by `g^{-1}=(eta+h)^{-1}`; T raised by `eta_bg` (flat background). Consistent split (matter stress on the flat background; curvature on the full metric) — coherent with the 70.1 "g=eta+h is the spacetime metric, cone-Hessian = source" frame.

---

## 2. Provides/Consumes Verification (test-value, exact over Q)

| Quantity | Producer | Consumer | Meaning | Test value | Status |
|---|---|---|---|---|---|
| a_4 (t^4 R-scale) | 72-02 | 73-01 (kappa R-scale) | leading coeff of R[g(tM_0)] ~ a_4 t^4 | a_4 = 395268903/24010000 (carried verbatim) | OK |
| kappa_psi | 73-01 | 73-02 (frozen RHS coupling) | a_4 / (T[psi] t^4 scale) | a_4/(121/39690000) = 32016781143/5929 ✓ exact | OK |
| kappa_sigma | 73-01 | 73-02 | a_4 / (T_sigma t^2 scale) | a_4/(53/9800) = 395268903/129850 ✓ exact | OK |
| kappa ≠ −R/2 (fp-assume-einstein guard) | 73-01 | 73-02 | coupling not the GST/SUSY −R/2 | −a_4/2 = −395268903/48020000 ≠ both kappa ✓ | OK |
| h^(2) center matrix | 72-02 | 73-01 (h2_field regression anchor) | leading (quadratic) metric response at center | h2_field(MATTER_L,BG_HALF)|center == handoff matrix (regression, per SUMMARY) | OK |
| h^(1) = 0 identically | 72-02 | 73-01/02 (test-order rationale) | linear response vanishes ⇒ linear test degenerate | G^(1)[h^(2)]=0, R^(1)=0 reproduced exact over Q | OK |
| decisive M_0 (MATTER_L + BG_HALF, triple −13/63000) | 72-02 | 73-01/02 (family anchor) | non-vacuous cross-term direction | psi(M_0)|center = −13/63000 (== Phase-72 non-vacuity triple) | OK |
| R_full ~ 4008 (R[g] at M_0,center) | 72-02 | 73-02 (regression) | full-metric Ricci scalar at the anchor | Rscalar(M_0,center) ~ 4007.98 == Phase-72 R_full exact over Q (per 73-02 + ref-72-handoff) | OK |
| g=eta+h physical metric; cone-Hessian=source; Lambda=0 DERIVED | 70.1 | 72, 73 | spacetime metric selection + vacuum framing | T,kappa on flat eta_bg; G on g; Lambda offered as free fit (no value works) | OK |
| validated curvature engine (Totaro==hand-rolled), ricci_decomposition_n4, eig_signature_count, det_3 SSOT, eta_bg | 72-01 | 73-01/02 | reused engine routines | engine extended in place (Sections 13→14), ALL_PASS exit 0 preserved | OK |

**All 9 cross-phase transfers verified** — meaning, units (all dimensionless, natural units), test value (exact over Q), and convention (eta_bg / det_3 SSOT) all match. No factor-of-2/pi/sign drift; the three frozen rationals reproduce exactly from the Phase-72 a_4 and the 73-01 T-scales.

---

## 3. Focus-Item Findings (as requested)

### 3a. Metric signature / eta_bg null-aligned form (vs 70.1/71/72) — CONSISTENT (with WARNING-1)
The operational object `eta_bg` is congruent to Minkowski diag(+1,-1,-1,-1) via the 52-kkt frame Jacobian, giving genuine signature (1,3) (verified eigen-signs {+1,-1,-1,-1}). The engine uses the *null-aligned inverse* for every trace/box (assertion-pinned, `bulk_geometry_verification.py:2504`), NOT a diag. Identical eta_bg to 71/72. The box `4∂_β∂_γ−∂_p²−∂_q²` is correctly the eta_bg^{-1} contraction. **CONSISTENT.** See WARNING-1 for the (label/glyph) string aliasing.

### 3b. det_3 SSOT + cross-term 2Re((x2 x1)x3) (vs 70/71/72) — CONSISTENT
det_3 SSOT = `code/bulk_geometry_verification.py`, byte-identical to ring_lemma_verification; `octonion_algebra.py` BANNED on the decisive path; `fp-wrong-cross-term` rejected in both plans. psi and the sigma multiplet both route through the engine oct_mul (Fano e1 e2=e4). Identical cross-term channel as Phases 70/71/72. **CONSISTENT.**

### 3c. Lambda=0 framing (DERIVED, not inserted; struck wording not reintroduced) — CONSISTENT
Every Phase-73 reference to "center is Einstein / Lambda<0 / inserted-Lambda" is explicitly tagged FALSIFIED, SUPERSEDED, REJECTED, or "does NOT fire" — never reasserted as an active claim (grep-confirmed across 73-01/02 SUMMARY, .tex, RESEARCH, audit). The circularity audit's STALE-ROADMAP reconciliation table certifies both stale items: (a) the box-hbar linear test is gauge-degenerate ⇒ full nonlinear G[g] is decisive; (b) Lambda=0 is DERIVED from the KKT det_2 (B1 difference potential ≡ 0 at M=0 ⇒ C≡0 ⇒ R≡0), the inserted-Lambda tripwire does NOT fire. Lambda was offered as a free global fit constant (expected 0); no value yields Einstein structure because the obstruction is structural (S≠0, Weyl≠0). True-strength framing preserved in both directions (not inflated to "leading-order Einstein", not deflated to "inserted-Lambda circularity"). **CONSISTENT** — and this phase actively *repairs* the stale ROADMAP/CONVENTIONS §6 text via the audit note.

### 3d. h^(2) handoff (a_4, R_full) between Phase 72 and 73 — CONSISTENT (exact)
a_4 = 395268903/24010000 carried verbatim; R_full ~ 4007.98 reproduced as a Phase-72 regression; h^(2) center matrix reproduced by h2_field at the center. h^(1)=0 correctly drives the re-scope to the quadratic-response / full-nonlinear test. **CONSISTENT.**

### 3e. Exact-over-Q discipline on the decisive verdict — CONSISTENT
`fp-float-decisive` rejected in both plans; the family G[g], the per-point + 120-eq global Lambda solve (sympy linsolve over Q), the residual matrices, the n=4 S/Weyl reconstruction (residual ==0), and the signature gate (sympy real_roots) are all exact over Q. Floats appear only in human-readable prints. **CONSISTENT.**

### 3f. Verdict coherence: NONE vs Phase 71 (SURVIVES) + Phase 72 (SURVIVES-qualified) — CONSISTENT (NOT a contradiction)
The three verdicts answer three *different* questions and compose coherently:
- **Phase 71 (SURVIVES):** the slice metric is genuinely position-dependent (curved, not homogeneous) — R(x) varies exact over Q. ⇒ spacetime is curved.
- **Phase 72 (SURVIVES-qualified):** matter (V_{1/2} cross-term) dominantly sources that curvature — off-switch removes ~94%; R~a_4||M||^4; S≠0, Weyl≠0. ⇒ the curvature is matter-sourced.
- **Phase 73 (NONE):** that curved, matter-sourced geometry does NOT satisfy G = kappa T + Lambda g for any single global (kappa,Lambda). ⇒ the matter-curvature relation is not *Einstein-structured*.

"Curved" (71) + "matter-sourced" (72) + "but the field equation is not Einstein" (73) is a single coherent narrative, NOT a contradiction. The S≠0/Weyl≠0 found in Phase 72 is precisely the structural obstruction Phase 73 confirms (the honest prior, stated in 72-02 and 73-01, was "curved but not Einstein-structured"). The R_full~4008 anchor is shared across 72 and 73 (regression). **CONSISTENT** — Phase 73's NONE is the predicted, internally-coherent terminus of the 71→72→73 chain.

---

## 4. Cross-Phase Error-Pattern Sweep (rapid)

| Pattern | Found? | Note |
|---|---|---|
| Sign absorbed into definition | NO | sign conventions (Riemann global sign) reconciled at the 72-01 boundary (Totaro==hand-rolled); 73 reuses the same engine, no re-absorption |
| Normalization factor change | NO | T raised by eta_bg, G by g^{-1} — both explicit and consistent; no implicit renorm |
| Implicit assumption violated | NO | "all sig (1,3)" enforced per-point (6/18 out-of-splice points DROPPED, not forced); ||M||→0 anchor holds; kappa frozen BEFORE G (DERV-03), not re-fit |
| Coupling convention mismatch | NO | kappa frozen as a single global rational; reproduces exactly from a_4 and T-scales |
| Factor of 2pi | N/A | no momentum-space/Fourier content |
| Wick rotation sign | NO | no Euclidean↔Minkowski rotation in Ph73; eta_bg Lorentzian throughout (Wick-via-u=e7 stays rejected per 70.1) |
| Boundary condition / symmetry factor | NO | single off-center point family; no image-charge/identical-particle factors |

---

## 5. WARNINGS (non-blocking)

### WARNING-1 (pre-existing, carried — NOT introduced by Phase 73): metric-signature label/glyph aliasing
- **state.json** `convention_lock.metric_signature` = `"mostly-minus (-,+,+,+ via h_2(C_u) det_2 Lorentzian slice)"` — the LABEL "mostly-minus" is paired with the GLYPH `(-,+,+,+)` (which conventionally denotes *mostly-plus*). This string is internally label/glyph-inconsistent.
- **Phases 70.1, 71, 72** all write `mostly-minus (-,+,+,+)` — i.e. they carry the SAME label/glyph pairing consistently.
- **Phase 73** plan frontmatter / 72-handoff write the glyph `(+,-,-,-)` (true mostly-minus), while the 73 SUMMARYs faithfully *flag* the state.json `(-,+,+,+)` aliasing.
- **Impact on results: NONE.** Every decisive quantity in Phases 70.1/71/72/73 is computed directly from the fixed operational object `eta_bg` (frame-derived, genuine (1,3)), never from the signature string. Verified: eta_bg has eigen-signs {+1,-1,-1,-1}, eta_bg·eta_bg^{-1}=I, box reads correctly off eta_bg^{-1}. The +/- string does not enter any number.
- **Why WARNING not INCONSISTENT:** the inconsistency is purely in the human-readable convention *string* (a label/glyph confusion present since milestone v17.0 init), carried uniformly, and operationally inert. It is correctly self-flagged in all three Phase-73 artifacts for the notation-coordinator.
- **Recommended fix (non-blocking, notation-coordinator):** reconcile the state.json / STATE.md / CONVENTIONS string to a single unambiguous form — e.g. `"signature (1,3) Lorentzian (one +, three −); operational object = eta_bg null-aligned KKT det_2 pullback"` — and pick ONE glyph convention. This is the same item flagged (and deferred) at Phases 71 and 72; Phase 73 did not regress it.

### WARNING-2 (informational): no standalone 73-VERIFICATION.md
Phases 70.1/71/72 each have a `*-VERIFICATION.md`; Phase 73 has none on disk. The 73-02 SUMMARY records that the orchestrator independently re-ran the driver and reproduced every decisive number exact over Q (and lists an "optional gpd-verifier pass" as a next action). This is a process/artifact-coverage note, not a consistency defect — the cross-phase numbers all check out here. Non-blocking; flag for the milestone-closure orchestrator if a formal verifier artifact is desired before archival.

---

## 6. Self-Test (Step 0): ledger internal consistency
- metric_signature (1,3 Lorentzian) ⇄ no propagator/Fourier convention to conflict with (field-theory entries are "N/A pure algebra") — compatible.
- natural_units (hbar=k_B=1) ⇄ all quantities dimensionless rationals — compatible.
- det_3 cross-term + Jordan product + octonion (Fano e1 e2=e4) + Cl(9,0) — mutually consistent algebra stack, unchanged since v16.0.
- **Self-test: PASS** (no contradictory test-value pairs in the active ledger).

---

## Conclusion

**consistency_status: CONSISTENT**

All Phase-73 cross-phase handoffs (a_4, kappa_psi, kappa_sigma, h^(2), h^(1)=0, M_0, R_full, the engine routines, the g=eta+h / Lambda=0 frame) verify exactly over Q against their producers (70.1, 72-01, 72-02, 73-01). The metric signature / eta_bg null-aligned form, the det_3 SSOT cross-term, the Lambda=0-DERIVED framing (with the struck "center is Einstein / inserted-Lambda" wording properly superseded and NOT reintroduced — indeed actively reconciled in the audit), the exact-over-Q discipline on the decisive verdict, and the verdict coherence (NONE is the internally-consistent terminus of curved[71] + matter-sourced[72]) all hold.

One pre-existing, non-blocking notation WARNING (metric-signature label/glyph string aliasing in state.json, carried uniformly from v17.0 init through 70.1/71/72, operationally inert, correctly self-flagged) and one informational note (no standalone 73-VERIFICATION.md). Neither blocks milestone v17.0 closure on the human-ratified NONE verdict.

_Checks performed: ~24 (8 convention-compliance, 9 provides/consumes test-value, 6 focus items, ~7 error-pattern, ledger self-test). Issues found: 2 (both non-blocking warnings)._
