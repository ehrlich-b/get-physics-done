# Phase 90 (v30.0) — GATE 2 INDEPENDENT VERIFICATION (U1 — the ε² pairing)

**gpd-verifier adversarial re-derivation. PASS (HIGH).**
The ε² clock-drift 1-form is a_X⁽²⁾(v) = ⟨∇_v 𝒦, D⟩ with 𝒦 = −(9/2)⟨M,p⟩·tl(C_pM), and the
constructive potential is **χ = ⟨𝒦,D⟩ = −(9/2)⟨M,p⟩⟨M,D_p⟩**. Re-derived independently
(symbolic cut M at E₁₁), exact over Q. Driver: `code/clock_connection_indep_check.py` (C1, C2,
C7) + targeted re-checks.

---

## The cast re-verified (D|_face)

The C_u-phase reference at E₁₁ is the coord-10 element D = e₇ in the x₁=(2,1) entry. Independently:

- **in-face** C_{E₁₁} D = D ✓
- **traceless** Tr D = 0 ✓
- **slice-rotation** with dU = diag(0, −e₇/2, e₇/2): D = [dU,·]|_face rotates D within the slice
  2-plane (C_{E₁₁}([dU,D]) = [dU,D] ≠ 0) ✓

So D|_face is the v28 ±i:1 slice-rotation phase element, exactly as cast.

---

## U1 facts re-derived (symbolic cut M, exact over Q)

| Fact | Statement | Independent result |
|---|---|---|
| **face Cayley–Hamilton** | tl((C_pM)²) = Tr(C_pM)·tl(C_pM) | TRUE |
| **moment of the compression** | Tr(C_pM) = Tr(M) − ⟨M,p⟩ = −⟨M,p⟩ (Tr M = 0) | TRUE (both equalities) |
| **I-drop** | ⟨face-identity, D⟩ = 0 (D traceless) ⇒ the −(9/8)a²·I part of K⁽²⁾ contributes nothing | TRUE |
| **pairing** | ⟨𝒦, D⟩ = (9/2)⟨(C_pM)², D⟩ ⇒ a_X⁽²⁾(v) = (9/2)⟨∇_v(C_pM)², D⟩ = ⟨∇_v 𝒦, D⟩ | TRUE |

Consequence: the two written forms of the clock agree —
(9/2)·tl((C_pM)²) = −(9/2)⟨M,p⟩·tl(C_pM) = 𝒦.

---

## The constructive potential (the payload of Gate 2)

Symbolic cut M at E₁₁:

> **χ = ⟨𝒦, D⟩ = −9·w₀·w₃**

where w₀ = ⟨M,E₁₁⟩ (the (1,1) diagonal entry of M) and w₃ = the e₇-coefficient of the x₁=(2,1)
entry, so ⟨M,D⟩ = 2·w₃. This is exactly

> **χ = −(9/2)⟨M,p⟩·⟨M,D_p⟩**     (verified: χ − [−(9/2)⟨M,p⟩⟨M,D⟩] = 0)

**Rational check** (M = diag(2,−1,−1) + cut off-diagonals): ⟨M,E₁₁⟩ = 2, ⟨M,D⟩ = 2/3,
χ = −(9/2)·2·(2/3) = **−6** — reproduced three ways (engine, formula, AND the opposite-orientation
e₇→−i 3×3-complex rep all give −6).

---

## Independent cross-checks (distinct from both drivers)

- **K_face⁽²⁾ via the 2×2 reduced-density block** (rows/cols {1,2}, e₇→i): the ε²-coefficient
  route reproduces tl(K⁽²⁾) = −(9/2)⟨M,p⟩·tl(C_pM) for symbolic cut M. Cross-checked against the
  **matrix-log clock** −2 log(2ρ_face): it differs from the cast clock by a **V₀ (face) term
  only**, so the pairing and the exactness are **robust to the clock definition**.
- **Opposite complex orientation e₇ → −i** (conjugate Fano sign): χ is unchanged (−6). χ is a real
  trace-form pairing, so it cannot depend on the choice of complex structure sign — confirmed.
- **Guard 5**: χ = ⟨𝒦,D⟩ is exhibited **constructively** from the matter data alone, with no
  appeal to v29's no-global-H. Exactness of the 1-form and over-determination of operator
  synchronization are independent statements.

---

## Confidence

**HIGH. GATE 2 PASS.** The ε² pairing a_X⁽²⁾(v) = ⟨∇_v 𝒦, D⟩ and the constructive potential
χ = −(9/2)⟨M,p⟩⟨M,D_p⟩ = −9 w₀ w₃ are reproduced independently (symbolic cut M, exact over Q),
robust to the clock definition (Taylor vs matrix-log differ only in V₀) and to the complex-structure
orientation (e₇ → ±i give the same real χ). These feed Gate 3, where the exactness a_X⁽²⁾ = dχ
(∇D=0 + Peirce orthogonality) closes the verdict DEAD.
