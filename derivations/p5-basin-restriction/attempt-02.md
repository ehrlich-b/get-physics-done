<!-- ASSERT_CONVENTION: metric_signature=riemannian_fisher, fourier_convention=na, natural_units=natural, gauge_choice=na, renormalization_scheme=na -->
<!-- Phase-60 attempt log (DERV-00-01 slice). Plan 60-02. Provenance: LIVE papers only. -->

# Attempt 02 — `rem:converse` grounded against BGW

**Plan:** 60-02 (Phase 60, milestone v15.0) — DERV-00-01 slice
**Date:** 2026-05-23
**Goal:** Confirm Paper 7's `rem:converse` against the BGW literature (not by re-asserting
the prompt): every `M_n(C)^sa` admits a faithful self-model with composite `M_{n^2}(C)^sa`,
and "minimal = maximal composite for `M_n(C)^sa`" so clause (iii) is auto-satisfied. Locate
the EXACT BGW statement; flag `rem:converse` as not-yet-in-live-paper.

---

## Inputs used

| Input | Source (LIVE / staged) | Used for |
|---|---|---|
| `rem:converse` (prompt-inline authoritative) | `~/scratch/get-physics-done/p5-basin-restriction-prompt.md` + spawn prompt | the claim to confirm/correct (NOT used as published) |
| Paper 5 Def 1 clauses (i)–(iv) verbatim | `~/repos/blog/landing/papers/qm-from-self-modeling/main.tex` lines 342–356 | clause (ii)/(iii) requirements, checked AS WRITTEN |
| `lem:bottleneck` + remark inventory | `~/repos/blog/landing/papers/sm-from-self-modeling/sections/complexification.tex` | provenance flag (grep: `rem:converse` absent; `lem:bottleneck` line 409) |
| **BGW 2020** (arXiv:1606.09331v3 = Quantum 4, 359) | staged PDF `/tmp/bgw-2020-1606.09331.pdf`, read pp. 1–4, 17–21, 24–29, 33–35, 39–41 | the EXACT composite statements (the load-bearing grounding) |
| Hanche-Olsen (universal tensor product) | via BGW [30], pp. 18, 20–21 | corroboration: `M_n(C)^sa` special ⇒ `⊠̃` exists; `h_3(O)` exceptional ⇒ `C^*=0` |
| 60-01 outputs (read-only) | `claim.md`, `two-composites.md`, `STATE.md` | distinction to preserve; clause (iii) integrity guard |

**Provenance grep (executed):** `grep -n "rem:converse" complexification.tex` → **0 matches
(exit 1)**; `lem:bottleneck` `\label` at **line 409**; other labeled remarks present
(`rem:basin-scope`, `rem:observer-universe`, `rem:sel-vs-force`, `rem:minkowski`,
`rem:complexification-scope`, …) but **no `rem:converse`**. PDF text-extraction module
(pypdf/PyPDF2) unavailable in the venv; BGW was read directly via the Read tool's native PDF
support, so provenance confidence is **full** (verbatim quotes captured), not reduced.

---

## Argument / grounding made

1. **Faithful self-model of `M_n(C)^sa`.** `V_M = V_B = M_n(C)^sa`, `phi = id` (order
   isomorphism ⇒ clause (ii) `sms:faithful`), internal composite `M_n(C)^sa ⊗ M_n(C)^sa ≅
   M_{n^2}(C)^sa`. OUS dimension bookkeeping `dim = n^4 = n^2·n^2` ✓ (local tomography holds
   for the *minimal* composite). For the slice `n = 3`: `M_3(C)^sa` (dim 9) → `M_9(C)^sa`
   (dim 81).

2. **EXACT BGW statement located.** The decisive passage is **BGW Corollary 4.16 + its
   discussion (p.29)**: for `A = B = C_n = M_n(C)^sa`, the universal tensor product is
   `A ⊠̃ B = M_{n^2}(C)_sa ⊕ M_{n^2}(C)_sa` (TWO copies), with the *"usual quantum-mechanical
   composite `M_{n^2}(C)_sa`"* a **separate** candidate — a direct summand by **Theorem 4.15**
   (p.29). Corroborated by **Table 2** (`C_n ⊠̃ C_k = C_{nk} ⊕ C_{nk}`, p.21), **Table 1(a)**
   (`C^*(C_n) = M_n(C) ⊕ M_n(C)`, p.19), and the **extra-classical-bit** statements
   (abstract p.1; Ex. 6.3 p.35; §6.3 p.39). Hanche-Olsen corroboration: `A` exceptional iff
   `C^*(A) = {0}` (p.18) ⇒ `M_n(C)^sa` special admits `⊠̃`; `h_3(O)` does not.

3. **Clause (iii) auto-satisfaction, AS WRITTEN.** The minimal/standard composite
   `M_{n^2}(C)^sa` carries all four data verbatim (product states, product effects,
   non-signaling, product-form sequential product) and is **simple** ⇒ minimal. The
   universal/maximal composite is NOT minimal (the extra classical bit is exactly the
   "hidden structure" minimality forbids). So clause (iii)'s **minimality selects the
   standard summand** `M_{n^2}(C)^sa`. Auto-satisfaction holds **not** because minimal =
   maximal, but because the minimal composite exists as a direct summand of the maximal one.

4. **Provenance flag + distinction preservation.** `rem:converse` flagged prompt-inline /
   not-in-live-paper (FUTR-01 insertion after `lem:bottleneck`, with a wording constraint:
   no "coincide"). The existence result SUPPORTS 60-01: `V_BM` (observer's self-composite,
   body⊗model) is never identified with BGW `⊠̃` on the whole `h_3(O)`
   (`fp-conflate-composites` rejected).

---

## Outcome

**`rem:converse`: CONFIRMED-WITH-CAVEAT.**

- **CONFIRMED:** existence of the faithful self-model of `M_n(C)^sa` with composite
  `M_{n^2}(C)^sa`; **clause (iii) satisfied as written** via the minimal composite. The
  **existence side of the two-composites distinction STANDS**, grounded in the literature
  (BGW + Hanche-Olsen), not the prompt.
- **CAVEAT:** the verbatim phrasing **"minimal and maximal composites COINCIDE for
  `M_n(C)^sa`" is FALSE.** BGW's maximal (universal) composite is strictly larger
  (`M_{n^2}(C)^sa ⊕ M_{n^2}(C)^sa`, extra classical bit); the standard composite is a
  *direct summand* (Thm 4.15 / Cor. 4.16). The correction is recorded in
  `rem-converse-bgw.md` §3 and carried into `STATE.md` as the FUTR-01 wording constraint.

**No collapse, no PAUSE.** PAUSE condition 1 (two-composites collapse) NOT triggered: the
existence direction uses the standard composite of `M_n(C)^sa` *with itself* (a special-EJA
composite, BGW Ex. 6.3), a different object from `⊠̃` evaluated on `h_3(O)`. The two
composite notions remain type-distinct.

---

## Failure mode / what remains open

- **No failure to locate the BGW statement.** The exact statement (Cor. 4.16 discussion) was
  found and quoted verbatim with page/theorem numbers. Provenance confidence full.
- **Minor numbering ambiguity (recorded, not blocking):** v3/published labels the
  no-exceptional-composite result **Proposition 4.14**, while the abstract/intro result-map
  calls it **Corollary 4.14**. Same content; flagged for the verifier.
- **Deferred to Phase 61 (not a failure of this plan):** explicit operational/matrix
  verification that the self-modeling sequential product `a & b = sqrt(a) b sqrt(a)`
  factorizes on the standard composite was *asserted* from the Lüders form here (adequate for
  literature grounding), not re-derived. Phase 61's SymPy/matrix check of the slice should
  confirm it. Clauses (i) [spectral, ≥2 orthogonal projective units] and (iv) [simple] for
  `M_3(C)^sa` are also Phase 61.
- **The CAVEAT is a finding, not an obstruction.** It corrects `rem:converse`'s wording but
  does **not** weaken the existence side or the distinction; it does not trigger any PAUSE.

---

## Deliverables this attempt

- `rem-converse-bgw.md` (DERV-60-03) — created, committed `a6709a38`.
- `STATE.md` — appended (Step 1 COMPLETE; verdict status; EXACT BGW citation baseline for
  Phase 61; provenance flag; [60-02] open question RESOLVED).
- `attempt-02.md` — this file.
- **NOT modified:** `claim.md`, `two-composites.md` (owned by 60-01). ✓
