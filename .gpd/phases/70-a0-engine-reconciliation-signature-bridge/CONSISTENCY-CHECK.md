# Phase 70 (A0) Rapid Consistency Check

**Date:** 2026-05-30
**Mode:** rapid (per-phase, post-execution)
**Scope:** Phase 70-01 + 70-02 vs the full conventions ledger (CONVENTIONS.md + state.json
`convention_lock`, locked commit 0d10eeea)
**Verdict:** CONSISTENT (with one ledger-wording cleanup recommended)

The live ledger exists in two mirrored places (`.gpd/CONVENTIONS.md` human-readable +
state.json `convention_lock` machine-readable). They agree with each other and with both
Phase-70 SUMMARYs. 33 convention entries (18 canonical + 15 custom); all checks below run
against this authoritative ledger.

## Specific checks

### 1. Cross-term label wrinkle — ADJUDICATED BENIGN (NOT a real inconsistency)

**Question:** the ledger writes the Freudenthal cross-term as `2Re(x2* x0* x1)`; the engine
+ both plans + 70-01 SUMMARY use `2Re((x2 x1) x3)`. Same operation, or a real conflict?

**What I verified against the engine's own `oct_mul` (ground truth), not a hand-rolled
multiply:**
- The engine SSOT `2Re((x2 x1) x3)` equals its cyclic rotations `2Re((x3 x2) x1)` and
  `2Re((x1 x3) x2)` EXACTLY (120/120 random rational triples), and DIFFERS from the buggy
  `2Re((x1 x2) x3)` (matches the engine docstring's stated identity exactly: cyclic
  rotations equivalent, `(x1 x2) x3` a different form).
- I could NOT reproduce the *literal string* `2Re(x2* x0* x1)` as equal to the engine SSOT:
  an exhaustive search over all 6 name-assignments {x0,x1,x2}->{x1,x2,x3}, both associations,
  and the marked conjugations gave 0 matches. So the ledger STRING, parsed literally, is
  ambiguous/under-specified — it is NOT a self-evidently-equal rewrite of the engine form.

**Why the wrinkle is nonetheless BENIGN (the equivalence-that-matters does not depend on
parsing that string):**
1. **Uniqueness certificate.** Wave 1 (70-01) certified the engine `det_3` IS the cubic
   generic norm: `det_3 == Cayley-Hamilton norm` at 3 octonionic points (LOCK 7a) AND
   annihilated by all 324 inner derivations (LOCK 7b, dim f_4 = 52). The F_4-invariant
   cubic norm on h_3(O) is UNIQUE up to scale; the engine form is pinned to it independent
   of any cross-term notation. The buggy `(x1 x2) x3` fails this (30/324) and is the banned
   `octonion_algebra.py` order — off-by-16 at octonionic_points()[1], reproduced here.
2. **Byte-identity.** The Phase-70 module is a byte-identical verbatim copy of the v16.0
   SSOT engine (sha256 e43d6a3f..., LOCK 0). The decisive det Phase 70 uses is provably the
   certified one, regardless of the prose label.
3. **Prior reconciliation.** 70-01's `ref-h3o-tower` row already reconciled the h3o_tower
   `2Re(x2* x0* x1)` labeling to the engine form numerically (both = +4 = CH norm at the
   test point).

**Verdict:** BENIGN. Phase 70 uses the certified, unique F_4-invariant engine form
throughout — there is NO inconsistency in the WORK. The only issue is that the ledger's
prose string `2Re(x2* x0* x1)` is an ambiguous way to write it and does not parse literally
to the engine form; it should be tightened (recommendation below).

### 2. Metric signature — CONSISTENT

Lorentzian mostly-minus (−,+,+,+) on the `h_2(C_u)` slice via `det_2`; Riemannian
positive-definite on the ambient `h_3(O)` cone (`g_X = Hess(−log det)`). Identical across
CONVENTIONS.md sec 0/1, state.json `metric_signature`, 70-02 `convention[0]` + `eta =
diag(+1,−1,−1,−1)` signature (1,3) (Sylvester minors [1,−1,1,−1]). 70-01 correctly treats it
as N/A (pure-algebra cubic-norm sub-phase). Consistent.

### 3. Potential `−log det` + SSOT engine + octonion_algebra ban — HONORED

`potential = −log det` (NOT bare det) in ledger sec 4 and 70-02 (`convention[1]`, Eq. 70.1;
`cone_hessian_at_center` differentiates `−log(det_3)` twice). SSOT =
`ring_lemma_verification.det_3` in ledger; 70-01 certifies a byte-identical verbatim copy
(`bulk_geometry_verification.py`, LOCK 0) and 70-02 builds the geometry only on it.
`octonion_algebra.py` BANNED in ledger sec 7; both plans confirm 0 imports (fence-free guard
PASS, 0 float-rank). Consistent.

### 4. Construction (ii) signature bridge + exact-over-Q — CONSISTENT

Construction (ii) [eta from `h_2(C_u)`'s own `det_2`; cone-Hessian supplies only `h_mu_nu`]
USED; construction (i) [Wick-rotate via u=e_7] REJECTED — matches ledger `signature_bridge`
verbatim, same two reasons (unproven C*-bottleneck conjecture + Visser arXiv:1702.05572
spurious curvature). 70-02 honestly flags the Minkowski residual=0 as
tautological-by-construction (Note B) and routes decisive content to the Hessian benchmark
`diag(9,9,18,18)`/det 26244 + index-map slice form `beta*gamma/3 − p^2/3 − q^2/3` — both
matching the ledger `milestone` test values exactly. Exact-over-Q discipline honored
throughout. Consistent.

### 5. Other drift — NONE on the decisive path

- **provides/requires chain clean:** everything 70-02 `requires` from 70-01 (the certified
  SSOT det_3) is exactly what 70-01 `provides`; 70-02 also correctly consumes 52-kkt's
  `det_2`/eta. Index map `{17,18,19,26} == engine-native {x1,x2,x3,x10}` is asserted (not
  trusted) via the slice det form. H^3 = SL(2,C)/SU(2) target curvature −1 (Totaro −d^2/4,
  d=2) stated, full computation correctly deferred to Phase 71 — matches ledger
  `riemann_ricci_sign`.
- **Natural units** (ħ=c=k_B=1) consistent; verdicts are dimensionless geometry, no
  unit-conversion boundary to mishandle.

## STATE.md staleness (housekeeping, NON-blocking)

`.gpd/STATE.md` lines ~142-171 still carry the v16.0 "Convention Lock" block with RETIRED
v16.0 values that contradict the live v17.0 ledger — e.g. line ~153
"Coupling convention: J > 0 antiferromagnetic" (RETIRED; ledger `coupling_convention` is now
the cubic-norm cross-terms C_{(V_0)(V_1)(V_{1/2})}). state.json `convention_lock` and
CONVENTIONS.md are the authoritative, mutually-consistent v17.0 sources and both SUMMARYs
follow them; STATE.md is a stale human-readable mirror only. Recommend refreshing STATE.md's
Convention Lock section to v17.0 (matches the existing MEMORY note on STATE/state.json
reconciliation). Documentation lag, not a physics inconsistency.

## Recommendations (both non-blocking; neither affects any Phase-70 verdict)

1. **Cross-term wording.** Replace the ambiguous ledger string `2Re(x2* x0* x1)` with the
   unambiguous engine-native `2Re((x2 x1) x3)` (the SSOT-certified, unique F_4-invariant
   form), and note that its cyclic rotations `(x3 x2) x1`, `(x1 x3) x2` are equal while
   `(x1 x2) x3` is the banned buggy form. The literal string does not parse to the engine
   form under any conjugation/association tried, so it invites future confusion despite the
   underlying det being correct and uniquely pinned.
2. **STATE.md refresh** to mirror the v17.0 ledger Convention Lock.
