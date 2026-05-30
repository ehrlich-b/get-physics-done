# Phase 70 (A0) Rapid Consistency Check

**Date:** 2026-05-30
**Mode:** rapid (per-phase, post-execution)
**Scope:** Phase 70-01 + 70-02 vs the full conventions ledger (CONVENTIONS.md + state.json
`convention_lock`, locked commit 0d10eeea)
**Verdict:** CONSISTENT

The live ledger exists in two mirrored places (`.gpd/CONVENTIONS.md` human-readable +
`state.json.convention_lock` machine-readable). They agree with each other and with both
Phase-70 SUMMARYs. 33 convention entries (18 canonical + 15 custom); all checks below run
against this authoritative ledger.

## Specific checks

### 1. Cross-term label wrinkle — ADJUDICATED BENIGN (NOT a real inconsistency)

- The ledger (CONVENTIONS.md sec 0/3 + `custom_conventions.cubic_norm_det`) states the
  Freudenthal cross-term as `2Re(x2* x0* x1)`; the engine + both plans + 70-01 SUMMARY use
  `2Re((x2 x1) x3)`. These are the SAME determinant in two index-naming conventions, not a
  conflict.
- **Mechanism (verified by me, independently of Wave 1):** the ledger names the three
  off-diagonal octonions `x0,x1,x2`; the engine names them `x1,x2,x3`. Under that relabel
  (x0:=x3), the literal conjugated form `2*Re(conj(x2)*conj(x0)*x1)` equals the engine's
  `2*Re((x2*x1)*x3)` EXACTLY. Independent Cayley-Dickson octonion multiply over Q:
  **200/200 random rational triples match exactly** (mismatches = 0). This is the standard
  Freudenthal conjugated cross-term; the engine's docstring + `ref-h3o-tower` reconciliation
  row already document it as the same det (both = +4 = Cayley-Hamilton norm at the test point).
- Only the BUGGY unconjugated `(x1 x2) x3` order differs, by exactly N_SSOT - N_buggy = 16 at
  octonionic_points()[1] (reproduced: full associator nonzero, order discriminator = 8). That
  is the banned `octonion_algebra.py` order; it is annihilated by only 30/324 inner derivations
  vs the SSOT's 324/324. The engine imports 0 of octonion_algebra (fence-free guard PASS).
- Note: cyclic symmetry of the UNconjugated real triple product is a red herring (it happens
  to hold for unconjugated inputs but is not the operative identity); the correct identity is
  the conjugation+relabel one above. Verdict unchanged: BENIGN.

### 2. Metric signature — CONSISTENT

Lorentzian mostly-minus (−,+,+,+) on the `h_2(C_u)` slice via `det_2`; Riemannian
positive-definite on the ambient `h_3(O)` cone (`g_X = Hess(−log det)`). Identical across
CONVENTIONS.md sec 0/1, state.json `metric_signature`, 70-02 `convention[0]` + `eta =
diag(+1,−1,−1,−1)` signature (1,3) (Sylvester minors [1,−1,1,−1]). 70-01 correctly treats it
as N/A (pure-algebra cubic-norm sub-phase). Consistent.

### 3. Potential `−log det` + SSOT engine + octonion_algebra ban — HONORED

`potential = −log det` (NOT bare det) in ledger sec 4 and 70-02 (`convention[1]`, Eq. 70.1,
`cone_hessian_at_center` computes Hess of `−log(det_3)`). SSOT = `ring_lemma_verification.det_3`
in ledger; 70-01 certifies a byte-identical verbatim copy (`bulk_geometry_verification.py`,
sha256 e43d6a3f..., LOCK 0) and 70-02 builds the geometry only on it. `octonion_algebra.py`
BANNED in ledger sec 7; both plans confirm 0 imports (guard PASS, 0 float-rank). Consistent.

### 4. Construction (ii) signature bridge + exact-over-Q — CONSISTENT

Construction (ii) [eta from `h_2(C_u)`'s own `det_2`; cone-Hessian supplies only `h_mu_nu`]
USED; construction (i) [Wick-rotate via u=e_7] REJECTED — matches ledger `signature_bridge`
verbatim, with the same two reasons (unproven C*-bottleneck conjecture + Visser
arXiv:1702.05572 spurious-curvature). 70-02 honestly flags the Minkowski residual=0 as
tautological-by-construction (Note B) and routes decisive content to the Hessian benchmark
`diag(9,9,18,18)`/det 26244 + index-map slice form `beta*gamma/3 − p^2/3 − q^2/3` — both
matching the ledger `milestone` test values exactly. Exact-over-Q discipline honored
throughout (sympy.Rational/Matrix; float only as labeled non-decisive eigenvalue triage).
Consistent.

### 5. Other drift — NONE on the decisive path

- **provides/requires chain clean:** everything 70-02 `requires` from 70-01 (the certified
  SSOT det_3) is exactly what 70-01 `provides`; 70-02 also correctly consumes 52-kkt's
  `det_2`/eta. Index map `{17,18,19,26} == engine-native {x1,x2,x3,x10}` is asserted (not
  trusted) via the slice det form. H^3 = SL(2,C)/SU(2) target curvature −1 (Totaro −d^2/4,
  d=2) stated, full computation correctly deferred to Phase 71 — matches ledger
  `riemann_ricci_sign`.
- **Natural units** (ħ=c=k_B=1) consistent; the verdicts are dimensionless geometry, so no
  unit-conversion boundary to mishandle.

## STATE.md staleness (housekeeping, NON-blocking — does not affect Phase 70 correctness)

`.gpd/STATE.md` lines ~142-171 still carry the v16.0 "Convention Lock" block, which lists
several RETIRED v16.0 values that contradict the live v17.0 ledger:
- line ~153 "Coupling convention: J > 0 antiferromagnetic" — RETIRED per ledger
  `coupling_convention` (now cubic-norm cross-terms C_{(V_0)(V_1)(V_{1/2})}).
- the block predates the v17.0 cone-geometry conventions generally.
state.json `convention_lock` and CONVENTIONS.md are the authoritative, mutually-consistent
v17.0 sources and both SUMMARYs follow them. STATE.md is a stale human-readable mirror only;
recommend the orchestrator refresh its Convention Lock section to mirror the v17.0 ledger
(matches the existing MEMORY note about STATE/state.json reconciliation). This is a
documentation lag, not a physics inconsistency in Phase 70.

## Recommendation (non-blocking)

Optionally align CONVENTIONS.md's cross-term wording to the engine-native
`2Re((x2 x1) x3)` form (or annotate that `2Re(x2* x0* x1)` is the identical Freudenthal
conjugated form under the x0=x3 relabel) to remove future confusion. Refresh STATE.md's
Convention Lock block to the v17.0 ledger. Neither affects any Phase-70 verdict.
