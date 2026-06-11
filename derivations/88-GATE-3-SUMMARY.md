# 88 — GATE 3 SUMMARY: E3 on the cut — indices, Euler closure, C_u-winding

**v28.0 Phase 88. Exact over Q. VERDICT = E3 (cut) PASS — Euler closure Σ = 3 = χ(CP²).**
Independently confirmed (`88-GATE-3-VERIFICATION.md`).

Diagonal X = diag(7,5,3), x_1>x_2>x_3. The Hessian along the (i→j) family is ∝ (x_j − x_i)
(anchor φ''(0) = 8(x_2−x_1)). Counting descending directions (cut, 2 real dirs per C_u-line):

| | E_11 | E_22 | E_33 |
|---|---|---|---|
| Morse index | 4 | 2 | 0 |
| Poincaré–Hopf (−1)^{ind} | +1 | +1 | +1 |

**Euler closure: Σ = 3 = χ(CP²)** (computed from real Hessian signs; χ = 3 cited, Borel /
Atiyah–GS torus moment map — not claimed).

**C_u-winding decomposition (the extracted new numbers, conventions stated):** each cut
C_u-line is oriented by the C_u complex structure J (e_7-mult); s_X|line = (x_j−x_i)·z, a
real-scalar map ⟹ C_u-phase winding +1 per line, total S³ degree +1 = Poincaré–Hopf. The
matter-pinned datum is the weight sign sign(x_j−x_i): **E_11:(−,−), E_22:(+,−), E_33:(+,+)**
(+ toward the larger eigenvalue) — the moment-polytope vertex data, X-determined.

**Gate 3: E3 (cut) PASS.**
