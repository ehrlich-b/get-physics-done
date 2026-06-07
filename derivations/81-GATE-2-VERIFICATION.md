---
phase: 81-sakharov-gate2
gate: "Gate 2 (SUPPORT MISMATCH) — milestone-decisive"
milestone: v21.0 (Sakharov Induced Gravity from V_{1/2} on h_3(O))
verified: 2026-06-06T00:00:00Z
verifier: gpd-verifier (adversarial, independent recompute, web access)
status: DEAD-confirmed
confidence: HIGH
verdict: "Gate 2 is genuinely DEAD — the induced scalar kappa = 6*pi^2/Lambda_f^2 cannot repair the v18 16-vs-6 tensor-support mismatch. The Sakharov route dies exactly where v18 died. DEAD verdict UPHELD."
independence: "G recomputed via the hand-rolled Christoffel Levi-Civita route (bulk_geometry_verification.hand_rolled_riemann_of_g), a code path DIFFERENT from the driver's Totaro closed-form (curvature_at -> spacetime_curvature_of_g); off-T Lambda ratios and all three single-global solves reassembled by the verifier's own linsolve."
---

# Phase 81 (v21.0 Sakharov) — Gate 2 (SUPPORT MISMATCH): INDEPENDENT VERIFICATION

**Decisive question.** Does the Sakharov-induced **scalar** Newton coupling
`kappa = 6*pi^2/Lambda_f^2` (from Gate 1's `c_1 = 1/(6*pi^2)`, `kappa^-1 = c_1*Lambda_f^2`)
repair the v18 Phase-77 tensor-support mismatch — `G[g]` supported on 16 entries vs `kappa*T`
on 6 — and close `G[g] = kappa*T + Lambda*g` for one global `(kappa, Lambda)` on
matter-bearing profiles? The executor returned **DEAD**, with the load-bearing kill argument
**self-corrected mid-execution** (naive support-coverage -> off-T over-determination). A
milestone-decisive verdict resting on a self-corrected argument demands fully independent
recomputation. I performed it.

**Bottom line: DEAD-confirmed at HIGH confidence.** Every decisive number reproduces by an
independent code path, exact over Q. The corrected argument (off-T over-determination) is
**correct**; the discarded naive argument was correctly discarded. The verdict does NOT depend
on the cutoff scale `Lambda_f`. One **scope caveat** (Einstein vs higher-derivative) is flagged
below — it tempers the ledger-consequence wording but does NOT change the DEAD verdict.

---

## 1. The decisive thing, verified independently

I rebuilt `G[g] = Ric - (1/2) g R` from the **hand-rolled Christoffel Levi-Civita Riemann**
(`hand_rolled_riemann_of_g`: `Gamma^a_bc`, `R^a_bcd`, lower the index — the full 16-component
lower-index Riemann), then assembled `Ric_jl = g^{ik} R_ijkl`, `R = g^{jl} Ric_jl`, and `G`
**by my own code**. This is a genuinely different path from the driver's Totaro closed form
`R_ijkl = -(1/4) g^{pq}(C_jlp C_ikq - C_ilp C_jkq)` (`curvature_at -> spacetime_curvature_of_g`).
`T[psi]` is independent of curvature by construction (AST-guarded, no Ric/R/G).

### 1.1 Support counts (independent hand-rolled route, matter-bearing anchor)

| Quantity | Verifier (hand-rolled route) | Driver (Totaro route) | Match |
|---|---|---|---|
| `R[g=e.e]` at M_0 | `14187524733311967018208791837/634906109300195099205387025 != 0` | same | EXACT ✓ |
| `psi` | `11*p/50 - 7*q/50` (real) | same | ✓ |
| **n_G** | **16** (full 4x4) | 16 | ✓ |
| `support(G)` | `{00,01,02,03,10,11,12,13,20,21,22,23,30,31,32,33}` | same | ✓ |
| **n_T** | **6** | 6 | ✓ |
| `support(T[psi])` | `{01,10,22,23,32,33}` | same | ✓ |
| `support(g)` | all 16 (g dense) | same | ✓ |
| v18 16-vs-6 reproduced | **True** | True | ✓ |

The verifier-hardened v18 Phase-77 headline (n_G=16, n_T=6, T_support={01,10,22,23,32,33}) is
reproduced **exactly over Q by an independent curvature route**. The "16/6" definition (count of
nonzero entries of the 4x4 lower-index array — NOT "10 symmetric slots") is the v18 definition and
is used consistently.

### 1.2 The off-T over-determination (THE load-bearing fact) — independently recomputed

`off-T = support(G) \ support(T)` = the entries where `G != 0` but `T = 0`. There
`G = kappa*T + Lambda*g` collapses to `G = Lambda*g` (kappa multiplies 0 and **drops out**), so a
single scalar `Lambda` must equal `G_{mu nu}/g_{mu nu}` on every off-T entry simultaneously.

**Independent result (hand-rolled G, my own ratios):** off-T has **exactly 10 entries**
`{00,02,03,11,12,13,20,21,30,31}`, and the required `Lambda = G/g` takes **4 DISTINCT values**:

| off-T entries | required Lambda (exact over Q) |
|---|---|
| (0,0) | `-9978961924797449174836874709459039 / 319202855887328887296103559140900` |
| (0,2),(0,3),(2,0),(3,0) | `-317916618161805844627443852087 / 3286572801083362866474944600` |
| (1,1) | `2522589903237169689329195542703061 / 11215489439566086388443320719220` |
| (1,2),(1,3),(2,1),(3,1) | `57364678715409746689086420509187 / 1046325268126721523490477817200` |

**4 distinct values are required where exactly 1 is allowed.** No single scalar `Lambda` works,
and `kappa` is absent (T=0 there). The driver printed the first three of these
(`(0,0), (0,2), (0,3)`) and they match my values **byte-for-byte**. This is the precise,
verifier-defensible mechanism: a scalar coupling cannot repair a tensor-rank mismatch because the
matter stress vanishes on the off-T block while `G` does not, and there the cosmological term is
over-determined. **The corrected argument is correct.**

**Structural, not a single-point accident:** the same `n_G=16, n_T=6, off-T=10, 4-distinct-Lambda`
pattern recurs on **two further matter directions** (D2, D3) at the same slice point — independently
confirmed:

| direction | R!=0 | n_G | n_T | off-T | distinct off-T Lambda |
|---|---|---|---|---|---|
| D1 (anchor) | yes | 16 | 6 | 10 | **4** |
| D2 | yes | 16 | 6 | 10 | **4** |
| D3 | yes | 16 | 6 | 10 | **4** |

### 1.3 The three single-global solves — independently reassembled

Cross-validation first: I confirmed **hand-rolled `G` == Totaro `G` exactly over Q at 3
representative family points** (anchor D1/X0/t1, off-center D2/XA/t2, off-center D3/XB/t1), `g`
matching too. This licenses using the (now twice-validated) `G` in the solve step, which I then
reassembled with **my own `linsolve`** over the full 18-point matter-bearing family:

| Solve | Verifier (own linsolve) | Driver | Meaning |
|---|---|---|---|
| both `(kappa,Lambda)` free (180 eqs) | **EmptySet** | EmptySet | no linear-in-T Einstein closure at all |
| induced `kappa=6*pi^2/Lambda_f^2`, `Lambda_f` SYMBOLIC | **EmptySet** | EmptySet | induced scalar does not close |
| v18 frozen rational `kappa_psi` | **EmptySet** | EmptySet | reproduces v18 Phase-77 negative |
| **generic symbolic `(kappa,Lambda)`** (verifier-added) | **EmptySet** | — | NO scalar `(kappa,Lambda)` closes |

The v18 frozen `kappa_psi` I rebuilt independently (`a4 / [t^4 * tr_eta T]`) is a genuine rational
(numerator/denominator ~1500 digits) and its solve is EmptySet — reproducing the verifier-hardened
v18 result.

### 1.4 kappa-independence => Lambda_f-independence

Two independent confirmations that the kill does not depend on the (un-pinned) cutoff `Lambda_f`:

1. **induced-kappa solve with `Lambda_f` carried SYMBOLIC -> EmptySet.** If the kill depended on a
   particular `Lambda_f`, a symbolic solve could have produced a constraint surface; it produces the
   empty set instead.
2. **generic symbolic `(kappa, Lambda)` 2-unknown solve -> EmptySet.** Here `kappa` is a free symbol;
   the induced `6*pi^2/Lambda_f^2` is merely one value of it. Since NO value of a free scalar `kappa`
   (paired with any `Lambda`) closes the system, the conclusion is manifestly `kappa`-independent and
   hence `Lambda_f`-independent. This is the strongest form of the claim.

The off-T argument (Sec 1.2) makes this transparent: on the off-T block `kappa` literally drops out
(T=0), so the 4-distinct-`Lambda` obstruction is `kappa`-free by construction.

---

## 2. The self-correction is sound (both deviations checked)

The executor logged two deviations. Both are sound and the final code is self-consistent:

- **Deviation 1 (NameError fix):** `scalar_invariance_of_support` referenced `G` without pulling it
  from the `rep` dict; fixed by `G = rep["G"]`. Cosmetic; the re-run is clean (exit 0, byte-identical).
- **Deviation 2 (naive -> off-T correction, load-bearing):** The first check naively asserted
  `support(kappa*T + Lambda*g)` fails to *cover* `support(G)`. This was a **false FAIL**: `g = e.e` is
  **dense** (16/16 nonzero — I confirmed), so `support(kappa*T + Lambda*g) = support(T) ∪ support(g)`
  IS the full 16. Naive coverage is trivially satisfied and is NOT the obstruction. The corrected
  argument — the **off-T over-determination** (Sec 1.2) — is the physically correct mechanism and is
  exactly what the v18 EmptySet solve encodes. I independently verified the corrected argument from
  scratch (4 distinct off-T Lambda values, hand-rolled G). **The verdict (DEAD) is unchanged; the
  supporting argument is now sound.** The discarded naive argument was correctly discarded.

**Note on the verdict() ladder.** `verdict()` is passed the *matter* support (6) as `support_kT`, so
its `support_G_covered_by_kappaT` clause is False (16 ⊄ 6). As the driver's own docstring states, this
clause is NOT load-bearing (dense `g` makes coverage trivial once `Lambda*g` is added). The
**load-bearing clause is `single_global_solve_consistent = False`** (the off-T EmptySet). DEAD fires if
EITHER clause is False, and the decisive clause is independently False — so DEAD is robust even if one
entirely discounts the loose support-coverage framing. Good.

---

## 3. Non-hardwired verdict (v20 hardcoded-boolean bug ABSENT)

I exercised `verdict()` directly with adversarial inputs:

| Input | Output | Correct? |
|---|---|---|
| synthetic matching supports (n_G<=n_T) + consistent solve | **SURVIVES** | ✓ |
| `support(G) ⊆ support(kT)` + consistent solve (true surprise branch) | **SURVIVES** | ✓ |
| real (16 vs 6) + inconsistent solve | **DEAD** | ✓ |
| matching supports + INconsistent solve | **DEAD** (solve clause) | ✓ |

And I confirmed the **off-T logic itself flips**: a synthetic `G = 2g` (uniform off-T ratio) yields
**1** distinct off-T value -> a single Lambda WOULD work -> the kill would not fire. So the DEAD verdict
genuinely depends on the computed 4-distinct-ratios fact, not a constant. The verdict is data-driven; the
v20 hardcoded-decisive-boolean bug is absent.

---

## 4. Matter-bearing, not deflated

Confirmed the test is on `rho > 0`, differentiated profiles (`R[g] != 0`, `G != 0`, `T != 0`) across
D1/D2/D3 (Sec 1.2). The `M=0` case — which the prompt explicitly warns is "deflated" — has
`R = 0` and `G == 0` (independently confirmed) and is **NOT** the configuration tested. The kill is on
genuinely matter-curved backgrounds.

---

## 5. Scope note: Einstein vs higher-derivative (FLAG — tempers wording, not the verdict)

Gate 2, as posed, tests whether the **leading induced Einstein term** — the scalar
`kappa ∝ Lambda_f^2` from the Seeley-DeWitt `a_1` coefficient — repairs the support. It is correctly
scoped to that object: the induced coupling really is a scalar (standard Sakharov form; literature
below), and a scalar genuinely cannot change tensor rank. The DEAD verdict for **induced Einstein
gravity** is correct.

However, the Sakharov / Seeley-DeWitt expansion also produces:
- `a_0 -> Lambda` (cosmological constant, `∝ Lambda_f^4`), and
- `a_2 -> higher-derivative` curvature (`R^2`, `C^2`, Gauss-Bonnet; `∝ Lambda_f^0`).

The `a_2` terms are genuine **4-derivative** tensors, NOT `scalar × T`, and are **out of scope** for
Gate 2's rank argument. Therefore:

> **"DEAD" means "induced *Einstein* gravity does not close" — NOT "no induced-action gravity of any
> kind".** Induced *higher-derivative* gravity is a distinct, weaker, less physically desirable, and
> untested claim.

The SUMMARY/tex wording **"Route C / kind-4 (induced action) gravity is DEAD for h_3(O)"** and "the
six-kind selection-law menu is now EXHAUSTED" (SUMMARY lines 92, 98; tex line 235 "nor (now) by an
induced one-loop effective action") slightly **overclaims** by not carving out the higher-derivative
escape hatch. This is a **non-blocking wording caveat** for the orchestrator/ledger, NOT a reason to
overturn: the milestone-decisive Gate-2 question (can the induced **Einstein** scalar repair 16-vs-6?)
is answered correctly and at true strength. Recommended ledger phrasing: "induced **Einstein** gravity
is DEAD; induced higher-derivative gravity is out of scope / a separate question."

---

## 6. Driver hygiene

| Check | Result |
|---|---|
| Driver exit code | **0** |
| ALL_PASS | **True** |
| Byte-identical decisive output across 2 runs (timing stripped) | **True** (verified by diff) |
| Floats on decisive path | **None** (only `float(` token is in the guard's banned-list + the injection test) |
| Source guard FIRES on injected `numpy.linalg`/`float(` | **True** (not a no-op; hit on `reproduce_support_counts`) |
| `octonion_algebra` imported at runtime | **False** (not in `sys.modules`) — the operative guard holds |
| `octonion_algebra.py` on disk | **Present** (207 KB) — the SUMMARY's "absent" is loose wording; the convention_lock explicitly sanctions the file as "a formula reference ONLY, never on the decisive path", and the guard correctly tests non-import, not file-absence. NON-BLOCKING wording nit. |
| det SSOT exact-Q | `ring_lemma_verification.det_3(diag(2,3,5)) == 30`, not float, module-correct ✓ |
| Convention consistency | mostly-minus (+,-,-,-), `g=e.e` (1,3), gravity = `R[omega]`, exact over Q — matches `state.json` convention_lock and the Gate-0/1 drivers ✓ |

---

## 7. Literature cross-check (Sakharov setup is standard)

[Visser, "Sakharov's induced gravity: a modern perspective" (gr-qc/0204062)] confirms the standard
structure: `1/(16*pi*G) = c_1 * Lambda^2` from the Seeley-DeWitt `a_1` coefficient with a supertrace
`STr` over species, cutoff `Lambda ~ M_Planck`. This matches the Gate-0/1 inputs Gate 2 imports
(`STr = +8/3`, `c_1 = 1/(6*pi^2)`, `kappa^-1 = c_1*Lambda_f^2`). The literature also confirms the full
induced effective action carries `a_0` (cosmological) and `a_2` (higher-derivative `R^2`) terms beyond
the leading `a_1` Einstein term — corroborating the scope note (Sec 5). The induced coupling being a
**scalar `∝ Lambda_f^2`** is exactly the textbook Sakharov form, so the "a scalar cannot change tensor
rank" argument applies on solid ground. No literature value contradicts the Gate-2 result.

---

## 8. Computational verification summary

| Check | Method | Confidence | Result |
|---|---|---|---|
| 5.2 numerical spot-check (G,T at anchor) | independent hand-rolled route, exact Q | INDEPENDENTLY CONFIRMED | n_G=16, n_T=6, R[g] exact match |
| 5.8 math consistency (G assembly) | hand-rolled Christoffel vs Totaro at 3 pts | INDEPENDENTLY CONFIRMED | G_hand == G_totaro exactly over Q |
| off-T over-determination | own ratios, hand-rolled G, 3 matter dirs | INDEPENDENTLY CONFIRMED | 4 distinct Lambda (need 1) -> DEAD |
| single-global solves (x3 + generic) | own `linsolve`, 18-pt family | INDEPENDENTLY CONFIRMED | all EmptySet |
| kappa/Lambda_f-independence | symbolic Lambda_f + generic kappa solve | INDEPENDENTLY CONFIRMED | EmptySet (kappa-free) |
| matter-bearing not deflated | D1/D2/D3 R!=0; M=0 R=0/G=0 | INDEPENDENTLY CONFIRMED | confirmed |
| non-hardwired verdict | adversarial verdict() inputs | INDEPENDENTLY CONFIRMED | flips correctly |
| driver hygiene | re-run, diff, guard injection | INDEPENDENTLY CONFIRMED | clean, byte-identical |
| 5.10 literature | web_search (Visser gr-qc/0204062) | CONFIRMED | standard Sakharov form |

**Computational oracle:** Section 1 contains executed, exact-over-Q recomputation by an independent
curvature route with actual numeric output (the 4 distinct off-T Lambda values, the EmptySet solves).

---

## 9. Verdict

**Gate 2 is genuinely DEAD.** The induced scalar `kappa = 6*pi^2/Lambda_f^2` does NOT repair the v18
16-vs-6 tensor-support mismatch. Independently, exact over Q, via a curvature route different from the
driver's: `n_G = 16`, `n_T = 6`; the 10 off-T entries force a single `Lambda` to take **4 distinct
values** (`kappa`-free), so `G = kappa*T + Lambda*g` has **no scalar solution**; all three (plus a
generic-`kappa`) single-global solves are **EmptySet**; the kill is **`Lambda_f`-independent**. The
self-corrected off-T argument is sound; the discarded naive coverage argument was correctly discarded.
The Sakharov route dies **exactly where v18 died**.

**Confidence: HIGH.** Three genuinely independent confirmations (hand-rolled curvature route, own
off-T ratios, own linsolve), a structural (not single-point) failure across three matter directions, a
non-hardwired verdict, clean reproducible driver hygiene, and literature-consistent setup. The only
caveat is a wording one (Sec 5): DEAD applies to induced **Einstein** gravity; induced
higher-derivative gravity is out of scope and the "menu exhausted / induced-action DEAD" framing should
be tempered to "induced **Einstein** gravity DEAD". This does not affect the milestone-decisive verdict.

### ONE-LINE VERDICT

**DEAD-confirmed: the induced scalar kappa cannot repair the 16-vs-6 tensor-support mismatch (4 distinct off-T Lambda values, all single-global solves EmptySet, Lambda_f-independent) — the executor did NOT err; the route dies exactly where v18 died.**

---

## Sources

- [Sakharov's induced gravity: a modern perspective (Visser, gr-qc/0204062)](https://arxiv.org/pdf/gr-qc/0204062)
