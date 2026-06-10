# v24.0 Independent Verification — Gate 0 (tangent counts) + Gate 2 (the LIVE verdict)

**Verifier:** independent (gpd-verifier), spawned BEFORE human ratification.
**Driver under test:** `code/variety_entropy_landscape.py` (reported VERDICT = **LIVE**).
**Date:** 2026-06-10. **Field:** exact over Q (and Q(t) along families). No floats on any decisive path.

**Milestone claim:** over the primitive-idempotent variety OP² = {rank-1 idempotents of h₃(𝕆)} = F₄/Spin(9),
the face-entropy S_X(p) = S(ρ_face(p)), ρ_face(p) = C_p(X)/Tr(C_p(X)) on the rank-2 COMPLEMENT face
V₀(p) ≅ h₂(𝕆), is a NON-TRIVIAL landscape for generic structured full-rank X, while I/3 is HOMOGENEOUS.
The exact-over-Q verdict criterion is: S_X(p) constant ⟺ char-poly coeffs constant ⟺
r(p) := det₂(C_p X)/Tr(C_p X)² constant (entropies/logs are illustration only).

---

## Independence of the verifier's code path

The verifier did **not** import or reuse the driver's `compress0`, `face_coeffs`, `family`,
`herm_from_vec`, `cmul_k`, or `el_*` helpers. Only the warm det-SSOT primitives were reused
(`RL.jordan, RL.Tr, RL.det_3, RL.h3o_from_coords, RL.h3o_identity, RL._standard_basis_27,
RL.jordan_L_matrix, RL.X_from_symbols, RL._flat27, KK.E_ii`) — these are the project det-SSOT for
octonion/Jordan algebra. The compression and the rank-2 spectrum were re-derived two independent ways:

- **Compression (independent):** built the 27×27 spectral **projector matrix** P₀(p) by Lagrange
  interpolation on the L_p matrix (`P = ∏_{o∈{1/2,1}} (L_p − o·I)/(0 − o)`) and applied it to the
  flat coords of X. (The driver instead applies the **operator polynomial** `2 L_p² − 3 L_p + 1`
  element-wise via repeated `RL.jordan`.) The projector was built from scratch — **not** via
  `KK.peirce_proj`.
- **Spectrum Method A:** r = det₂(C)/Tr(C)² with det₂ = (Tr² − Tr(C∘C))/2 on the matrix-built C.
- **Spectrum Method B (no (Tr²−Tr2)/2 anywhere):** literal 2×2 spin-factor determinant
  `det₂ = d_axis·d_o − |w|²` on an **independently constructed orthonormal face frame**
  {q_axis = v′v′*, v′⊥v in the {0,j} plane; q_other = E_other}, with |w|² read as the surviving
  off-block octonion-norm-squared of C after removing the two diagonal poles.
- **Families (independent):** assembled p(t) = vv* directly into engine coords via `RL.h3o_from_coords`
  with my own associative-line product, **not** the driver's `herm_from_vec`.

Method A ≡ Method B as full rational functions over Q(t) for both decisive families, and both ≡ the
driver at every pre-registered sample AND at a fresh non-pre-registered point t = 7.

---

## GATE 0 — tangent counts (two independent methods) — **PASS**

| Item | Method (how it differs from the driver) | Result | Verdict |
|---|---|---|---|
| (a) FULL variety tangent at E₁₁ | dim of ½-eigenspace of L_{E₁₁} via **nullspace of (L − ½I)** + per-basis-vector eigenvalue scan | **16** = V_{1/2}(E₁₁) = coords {11..26} | PASS |
| (b) u-aligned locus tangent at E₁₁ | built the **9-dim h₃(C_u) subalgebra explicitly** (coords {0,1,2}+{e₀,e₇ slots of each off-diagonal block} = {0,1,2,3,10,11,18,19,26}), verified it is L_{E₁₁}-invariant, **restricted L_{E₁₁} to a 9×9 matrix**, counted its ½-eigenspace | **4** | PASS |

- (a) The driver derives 16 the same way (nullspace) but the verifier additionally confirms the
  ½-eigenvectors are **exactly** the standard basis {11..26} by scanning `L·e_k`.
- (b) The driver counts the {e₀,e₇} survivors **set-theoretically** (it never restricts/diagonalizes
  the operator). The verifier instead **restricts the operator** L_{E₁₁} to the h₃(C_u) subalgebra and
  reads the eigenvalue multiplicities: `L|_{h₃(C_u)}` has spectrum **{1:×1, 0:×4, ½:×4}** (1+4+4 = 9),
  the exact rank-1-idempotent Peirce pattern, whose ½-block = **4**. This is the pre-registered
  OP² → CP² = SU(3)/U(2) (4-dim, totally geodesic) bottleneck count. **CONFIRMED.**

---

## GATE 1 — vacuum calibration (must be constant) — **PASS**

For X = I/3, on ALL four families, the verifier's Method A gives **Tr = 2/3, r = 1/4 (constant)** ⟹
spectrum (1/2, 1/2), S = log 2.

| Family | Tr(C_p X) | r = det(ρ_face) | Verdict |
|---|---|---|---|
| u-aligned-Cu-phase(e7)  j=1,k=7 | 2/3 | 1/4 | PASS |
| transverse-real         j=1,k=0 | 2/3 | 1/4 | PASS |
| off-u(e1)               j=1,k=1 | 2/3 | 1/4 | PASS |
| u-aligned-E33-real      j=2,k=0 | 2/3 | 1/4 | PASS |

**Harness-bug note (verifier-side, NOT a driver discrepancy):** the verifier's first real-direction
(k=0) family build squared e₀ as if imaginary (e₀²=−1), giving a wrong p(t) and r=7/25 on the two
k=0 families. This was a bug in the verifier's own associative-line product, fixed by routing k=0
through ordinary real multiplication. After the fix, all four families calibrate to r=1/4. The two
**decisive** families (off-u e1, u-aligned e7; both k≠0) were never affected and matched the driver's
exact sample values throughout.

---

## GATE 2 — THE decisive verdict — **CONFIRM LIVE**

Generic state X_gen = h3o_from_coords(7, 5, 3, x1, x2, x3), x1=(e₄:1/5, e₆:1/7), x2=(e₂:1/4, e₅:1/6),
x3=(e₁:1/3, e₃:1/5, e₇:1/8). Verifier independently rebuilt it; **det₃(X_gen) = 696029/6720 > 0**
(full-rank, cone interior) — matches.

**Pre-registered sample match (verifier Method A, matrix-projector compression):**

| Family | t | verifier r(t) | expected | match |
|---|---|---|---|---|
| off-u(e1) | 2 | 2727493/12700800 | 2727493/12700800 | ✓ |
| off-u(e1) | 3 | 8878651/40043584 | 8878651/40043584 | ✓ |
| off-u(e1) | 5 | 83558976059/366799809600 | 83558976059/366799809600 | ✓ |
| u-aligned-Cu-phase(e7) | 2 | 5270711/24354225 | 5270711/24354225 | ✓ |
| u-aligned-Cu-phase(e7) | 3 | 503003/2252432 | 503003/2252432 | ✓ |

**r(2) ≠ r(3) on BOTH families ⟹ r is non-constant in the family parameter ⟹ the face-entropy
landscape VARIES ⟹ LIVE.**

**Triple-route fresh cross-check (t = 7, NOT pre-registered):**

| Family | Method A (matrix-projector + det₂ form) | Method B (literal 2×2 spin det, no (Tr²−Tr2)/2) | driver | agree |
|---|---|---|---|---|
| off-u(e1) | 1762338539/7661150784 | 1762338539/7661150784 | 1762338539/7661150784 | ✓ |
| u-aligned(e7) | 1721060939/7456667904 | 1721060939/7456667904 | 1721060939/7456667904 | ✓ |

Method A ≡ Method B as **full rational functions over Q(t)** (Tr, det₂, and r all identical) for both
families — the rank-2 face spectrum is confirmed by two genuinely different determinant computations.

**verdict() non-hardwired:** the driver's `verdict(False)=="DEAD"`, `verdict(True)=="LIVE"` self-test
holds; the boolean fed to it is derived from `cancel(r − r₀) != 0` on a guard-1-clean family.

---

## Item 4 — non-vacuity / bug-guard #1 (stabilizer) — **PASS**

**Direction-blind vs direction-resolving (the decisive non-vacuity contrast):**

- **X = diag(7,5,3):** r(t) is the **SAME** rational function across the three (0,1)-entry octonion
  directions e₁, e₂, e₇: r(t) = (15t⁸+84t⁶+138t⁴+84t²+15)/(64t⁸+384t⁶+704t⁴+384t²+64). Octonion-
  direction-BLIND (its large effective symmetry). Matches the driver exactly. **PASS.**
- **X = X_gen:** r(t) is **DIFFERENT** across e₁, e₂, e₇ (r(e1)≠r(e2) and r(e1)≠r(e7)). Direction-
  RESOLVING — genuine matter content, not a stabilizer-orbit artifact. **PASS.**

**Stabilizer dims (KK.stab_f4):** dim Stab_{F₄}(diag(7,5,3)) = **28**, dim Stab_{F₄}(X_gen) = **28**.
Both are Spin(8)-type (dim 28) stabilizers, but **distinct embeddings**: the diagonal stabilizer acts
blindly on the off-diagonal octonion directions of the family, X_gen's does not. Dimension equality
does NOT make X_gen blind — the resolving contrast above is the operative guard. (Note: the diagonal
r(t) itself varies with t, so a single-family check would false-LIVE on a special state; the
direction contrast is exactly the bug-guard that distinguishes generic matter.)

**Families move E₁₁:** p(t) ≠ E₁₁ for t ≠ 0 (verified), so the families are transverse to the
E₁₁-fixing part of any stabilizer ⟹ variation is non-vacuous. **PASS.**

---

## Item 5 — flattening (vacuum homogeneous) — **PASS**

Along X_t = (1−t)·I/3 + t·X_gen, leading sensitivity of r along the off-u(e1) probe family (param s):

| t | dr/ds|₀ | d²r/ds²|₀ |
|---|---|---|
| 0   | **0** | **0** |
| 1/4 | 13879/1837500 | −7328317/55125000 |
| 1/2 | 102021/10765300 | −47416301/279897800 |
| 3/4 | 2548557/248199700 | −3394563813/18366777800 |
| 1   | 629/58800 | −45463/235200 |

Both first- and second-order sensitivities **vanish identically at t = 0** (X₀ = I/3: the whole probe
family is flat, r ≡ 1/4) and **grow with t**. The vacuum is the homogeneous (flat) point; matter
content turns on the landscape. **PASS.**

---

## Item 6 — guard #5: numeric leakage — **PASS**

The decisive path (compress → Tr, det₂, r → verdict comparison) contains **zero Float atoms**: T, det₂,
r are all-rational; r(2)=2727493/12700800 and r(3)=8878651/40043584 are exact Rationals; the verdict
`r(2) ≠ r(3)` is decided over Q. The only `sqrt`/`log`/`float` in the driver are in
`face_spectrum`/`S_illustration`, explicitly labeled illustration-only and **never** fed to
`verdict()`. **PASS.**

---

## Summary table

| # | Item | Verdict | Independent method |
|---|---|---|---|
| 0a | FULL tangent = 16 = V_{1/2}{11..26} | PASS | nullspace(L−½I) + per-basis eigenvalue scan |
| 0b | u-aligned tangent = 4 | PASS | 9×9 restriction of L to h₃(C_u); spectrum {1,0×4,½×4} |
| 1 | I/3 calibration r=1/4, Tr=2/3 const | PASS | matrix-projector compression (post harness-bug fix) |
| 2 | r non-constant for X_gen (LIVE) | **CONFIRM LIVE** | Method A ≡ Method B over Q(t) ≡ driver; 5 samples + fresh t=7 |
| 4 | diag blind / X_gen resolving; families move E₁₁ | PASS | direction contrast + KK.stab_f4 (both dim 28) |
| 5 | flattening at t=0, grows with t | PASS | dr/ds, d²r/ds² along off-u probe over X_t |
| 6 | no numeric leakage on verdict path | PASS | Float-atom audit; logs only in illustration |

## VERDICT

**CONFIRM LIVE (HIGH).** The decisive Gate-2 verdict (r(p) non-constant for the generic structured
state X_gen ⟹ the face-entropy landscape is a non-trivial field over the idempotent variety, while
I/3 is homogeneous) is confirmed through a fully independent code path: a from-scratch 27×27 spectral-
projector compression and a literal 2×2 spin-factor determinant (no (Tr²−Tr2)/2), which agree with each
other as rational functions over Q(t) and with the driver at every pre-registered sample plus a fresh
point. Gate-0 tangent counts (16 and 4) are independently re-derived, the latter by an operator
restriction the driver never performs. No discrepancy with the driver. The only anomaly encountered was
a bug in the **verifier's own** real-direction (k=0) family construction during Gate-1 calibration,
which was diagnosed and fixed; it never touched the decisive k≠0 families. Numeric leakage is absent;
the verdict is exact over Q.
