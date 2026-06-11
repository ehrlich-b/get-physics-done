# 87 — GATE 0 SUMMARY: machinery regression (fail-fast)

**v27.0 Phase 87. Exact over Q/Q(t). ALL PASS.** Driver `code/variety_equation_of_state.py`.

- **v25/v26 regression:** `M = diag(2,−1,−1)` gives `G(E_11) = 0`, `G(E_22) = −9/4` (the
  v26 response-field anchors intact).
- **The Peirce projection `π_{1/2}^{(E_11)}`** = the `(0,1)` and `(0,2)` octonion entries
  (tangent coords `{11..26}`; cut `{11,18,19,26}`); diagonal and the `(1,2)` entry killed.
- **The two `dG` paths agree:** the Peirce-projection covector formula
  `dG_M = π_{1/2}(M# − ½⟨M,p⟩M)` matches `d/dt G_M(p(t))|_0 == ⟨dG_M, ṗ(0)⟩` on 5 families
  (real, `e_1`, `e_7`, two cut) — the differential representation is certified.

**Gate 0: ALL PASS** — the v26 response field, the tangent Peirce projection, and the
gradient representation are certified before the fork.
