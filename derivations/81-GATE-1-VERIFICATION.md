# Phase 81 (v21.0 Sakharov Gate 1: a_1 ∝ R) — INDEPENDENT VERIFICATION

**Verifier:** gpd-verifier (web-enabled)
**Verified:** 2026-06-06
**Profile / mode / autonomy:** deep-theory / balanced / balanced
**Driver under test:** `code/sakharov_gate1_a1R.py`
**Executor claim:** PASS — `a_1 = -R/3` per Dirac, clean ∝ R, zero non-R residual; `c_1 = 1/(6π²)`; `G = 3π/(8Λ_f²) > 0`.

## VERDICT: PASS-confirmed (a_1 is a clean ∫R). CONFIDENCE: HIGH.

The single most important check — an **independent explicit-Clifford re-derivation of `a_1 = -R/3`** (NOT reusing the driver's `tr(γ^{μν})=0` assertion) — reproduces the executor's result exactly over Q(i), in **two independent gamma representations**. The structural claim is confirmed against the **primary source** (Vassilevich hep-th/0306138, equations extracted directly from the PDF). The c_1 read-off and Gate-0 consistency hold exact over Q·π. The verdict is genuinely non-hardwired (the v20 bug is absent). One nuance on the torsion check (item 4) is documented below; it does **not** change the verdict.

---

## 1. Independent explicit-Clifford re-derivation of a_1 = -R/3 (THE decisive check) — INDEPENDENTLY CONFIRMED

I built explicit 4×4 Dirac gamma matrices in the **standard (Dirac) representation**, mostly-minus metric η=diag(+1,−1,−1,−1) (project lock), exact over Q(i), and verified the full Clifford algebra and the three sub-claims. I did **not** import the driver's `spinor_trace_identities()`; I constructed the matrices from Pauli blocks myself.

**Gamma matrices (Dirac rep):**
```
γ⁰ = [[I₂, 0],[0, −I₂]]      γ¹ = [[0, σ₁],[−σ₁, 0]]
γ² = [[0, σ₂],[−σ₂, 0]]      γ³ = [[0, σ₃],[−σ₃, 0]]
```
with σ₁=[[0,1],[1,0]], σ₂=[[0,−i],[i,0]], σ₃=[[1,0],[0,−1]].

**Results (exact over Q(i)):**

| Check | Result | Status |
|---|---|---|
| Clifford `{γ^μ,γ^ν}=2η^{μν}I₄` for all 16 (μ,ν) | holds exactly | ✓ |
| (i) `tr(I₄)` | `4` | ✓ |
| (ii) `tr(γ^{μν})` for **all** μ≠ν, γ^{μν}=½[γ^μ,γ^ν] | `0` (all 12 off-diagonal) | ✓ |
| γ^{01} ≠ 0 (so traceless is **nontrivial**, not a zero matrix) | nonzero | ✓ |
| (iii) `tr(E + R/6·I₄)` with E=−R/4·I₄ (Lichnerowicz) | `−R/3` | ✓ |
| `tr(E + R/6) == −R/3` exact | `4(−1/4 + 1/6)R = −R/3` | ✓ |

**Cross-check in a SECOND representation (chiral/Weyl basis, γ⁰=[[0,I₂],[I₂,0]]):** Clifford algebra holds, and `tr(γ^{μν})=0` for all μ≠ν. The traceless-ness of the antisymmetrized product is therefore representation-independent, as the textbook fact requires.

**Conclusion of item 1:** `tr(γ^{μν})=0` is **genuinely true** (not merely asserted), so the minimal-gauge F-term `−½γ^{μν}F_{μν}` in E traces to zero and the gauge field strength **drops out of a_1**. The bundle trace `tr(E+R/6) = -R/3` per Dirac is confirmed from first principles. **This is the load-bearing check and it passes at true strength.** Had `tr(γ^{μν})≠0` in my explicit rep, the F-term would survive and Gate 1 would be DEAD — it is zero, so Gate 1 is clean on this channel.

---

## 2. Structural / Gilkey citation — INDEPENDENTLY CONFIRMED against the primary source

The web tool could not parse the Vassilevich PDF (binary), as the research note predicted. I extracted the text directly via `pdftotext` and read the actual equations. **Source: D.V. Vassilevich, "Heat kernel expansion: user's manual," Phys. Rept. 388 (2003) 279, arXiv:hep-th/0306138.**

**Eq. (4.14):** `a₂(f,D) = (4π)^{−n/2} (1/6) ∫ √g tr_V{f(α₁E + α₂R)}`, with **α₁=6** fixed by eq. (4.16). Hence `a₂ = (4π)^{−n/2} ∫ √g tr_V{f(E + R/6)}` — **exactly the "E + R/6" coefficient.**

**Eq. (4.1) + the k=2 statement (line 2224–2227):** *"if k=2 only two independent invariants exist. These are E and R."* This is the precise structural fact the whole gate rests on: the curvature-linear coefficient contains **only E and R·I**, nothing else.

**Eq. (4.15):** `a₄(f,D)` contains `E_{;kk}, RE, E², R_{;kk}, R², R_{ij}R_{ij}, R_{ijkl}R_{ijkl}, Ω_{ij}Ω_{ij}`. So `R²`, `R_{μν}²`, `R_{μνρσ}²`, `□R`, and the bundle/gauge field-strength `Ω²` (= tr F²) **all live one order up, in a₄ — never in the a₂/(E+R/6) coefficient.** Confirmed exactly as claimed.

**Eq. (3.27) — the squared Dirac operator:** `E = −R/4 + (1/4)[γ^μ,γ^ν]F_{μν} + (axial/vector pieces)`. The **Lichnerowicz term is −R/4** (matches the driver). The field-strength term is `(1/4)[γ^μ,γ^ν]F_{μν}` (= ½γ^{μν}F_{μν} up to the sign convention) and traces away by item 1.

**Naming note (not an error):** the driver and tex call this coefficient **a_1**, while Gilkey/Vassilevich label it **a_2** (Vassilevich indexes by mass dimension; odd-index coefficients vanish on a closed manifold). The *object* — the curvature-linear E+R/6 coefficient, with R²/F² strictly one order higher — is identically the one the gate needs, and is correctly identified. The tex (`prop:a1-structure`, eq. 74) states the structure correctly. This is a labeling convention, not a physics discrepancy.

**Sign nuance (immaterial):** Vassilevich's E carries `+(1/4)[γ,γ]F` whereas the driver writes `−½γ^{μν}F`. Since the term traces to zero either way, the sign is irrelevant to a_1. The decisive `−R/4` Lichnerowicz piece matches.

---

## 3. Wave-map / target-curvature channel absent — STRUCTURALLY CONFIRMED

`V_{1/2} = 16` of Spin(10) is a **linear spinor representation** (one SM generation; Paper 7 / the Peirce half-eigenspace). A field valued in a linear rep is a section of a **vector bundle** with fiber V=C^16 and structure group Spin(10) acting linearly; the fiber metric is the constant Spin(10)-invariant bilinear, which is **flat** (a vector space has identically zero Riemann curvature). Therefore the target Riemann tensor `R^{target} ≡ 0` and the sigma-model endomorphism `E ⊃ −R^{target}_{abcd}(φ̄)∂_μφ̄^b∂^μφ̄^d` (Friedan; Alvarez-Gaumé–Freedman–Mukhi) is **identically absent**. This is a structural fact about linear reps, not a numerical computation. The contrast — a nonlinear sigma-model into a curved coset G/H — is the genuine risk, and it does not apply here because the **16** is linear, not a coset. The driver's synthetic-injection self-test (a hypothetical curved target gives `∂a_1/∂R^{target} = −4 ≠ 0`) correctly demonstrates the contaminant *would* be detected, so the absence is a genuine finding, not a blind spot. **Channel absent; confirmed.**

---

## 4. Torsion-free / Laplace-type check — CONFIRMED with an important nuance (does NOT change the verdict)

This is the one item the task flagged for scrutiny (toy tetrad vs. actual matter background). I inspected `cartan_phaseB_curvature.py` (`spin_connection_omega` l.148, `torsion_of` l.186) and ran independent tests.

**What the harness actually does.** `spin_connection_omega(E, coords)` computes the **closed-form Levi-Civita spin connection** (the unique torsion-free, metric-compatible connection of g=e·e, via the standard formula). Consequently `torsion_of(spin_connection_omega(e)) = 0` is **identically true for ANY invertible tetrad e** — it certifies that formula (2) correctly *implements* the torsion-free connection; it is **not** a discovery that the specific matter background "happens" to be torsion-free.

**The check is non-trivial (it would catch a wrong connection).** I confirmed `torsion_of` genuinely detects non-Levi-Civita connections:

| Connection fed to `torsion_of` (on E=diag(1,1+x0²,1,1)) | Torsion residual | Interpretation |
|---|---|---|
| `spin_connection_omega(E)` (toy tetrad) | `0` | reproduces executor |
| `ω = 0` (deliberately wrong) | `−2·x0 ≠ 0` | check is non-trivial |
| `ω` perturbed by +1/7 (antisymmetric, non-LC) | `(x0²+1)/7 ≠ 0` | catches non-LC |
| richer diagonal `diag(1,1+x0²,1+x1²,1+x0·x2)` | `0` | LC-by-construction |
| non-diagonal tetrad (off-diag x0/3) | `0` | LC-by-construction |

**Scrutiny: is the toy-tetrad check sufficient?** The executor's check is on the toy frame E(x)=diag(1,1+x0²,1,1), **not** on the actual soldered/matter tetrad e=π_u(dE). The SUMMARY (Deviation note) and the research note (Q3) acknowledge that the surd-laden matter tetrad hits the symbolic-d-omega watchdog (the same cliff v18-Ph77 hit), so Ph77 itself certified the **machinery** on a rational frame and delivered the matter verdict via the provably-equal metric-Riemann route.

**Assessment — torsion-free-by-construction makes this sufficient, with one caveat made explicit:**

- The physics question is whether the **matter Laplacian's connection** in `⟨DM,DM⟩` is metric-compatible Levi-Civita (so the operator is Laplace-type and a_1=tr(E+R/6) applies). The harness **defines** ω(e) to *be* the Levi-Civita connection of g=e·e. By construction it is torsion-free for any invertible e, including the matter tetrad — so torsion=0 holds on the matter background too, regardless of which tetrad you feed. The toy-tetrad run is a *machinery certification* (does the code correctly produce a torsion-free connection?), and that certification is valid and non-trivial.
- **The genuine, separate physics assumption** (which the research note Q3 correctly isolates as "the ONE thing to CHECK") is whether `D` in `⟨DM,DM⟩` *is* this Levi-Civita ∇ + gauge, i.e. that **no leftover octonionic associator term sneaks into D and makes the operator non-Laplace-type.** This is established upstream (v18-Ph77, exact over Q: R[ω]==metric Levi-Civita Riemann of g=e·e on every sampled component, the soldered background is an ordinary pseudo-Riemannian manifold once g=e·e is fixed). The Gate-1 driver does **not** re-establish this from scratch on the matter tetrad — it relies on the Ph77 result. Given Ph77 was verifier-hardened HIGH in v18, this reliance is sound.
- **Distinct from v20's torsion.** This Levi-Civita (matter-Laplacian) torsion is correctly distinguished from v20's *geometric* Einstein-Cartan torsion of e sourced by the spin current (a different connection). v20's torsion finding does not reintroduce a T² term in the matter heat kernel. Correctly stated.

**Conclusion of item 4:** torsion=0 / Laplace-type holds. The toy-tetrad check is a valid (non-trivial) certification of the torsion-free machinery; combined with the construction (ω *is* the Levi-Civita connection) and the upstream Ph77 result (soldered background is ordinary Riemannian, D is metric ∇), it is sufficient. A stronger direct run on the matter tetrad is **not needed** for the conclusion (and is blocked by the symbolic watchdog anyway). The one residual reliance — that D carries no associator term — is inherited from verifier-hardened v18-Ph77, not independently re-proven here. This is a reasonable scope boundary, not a gap. **Conclusion holds.**

---

## 5. c_1 consistency — INDEPENDENTLY CONFIRMED (exact over Q·π)

Computed independently (not via the driver's `read_off_c1`):

| Quantity | Value | Check |
|---|---|---|
| STr (Gate-0, ratified) | `8/3` | reproduced via Gate-0 primitives AND the per-Weyl chain |
| `c_1 = STr/(4π)²` | `1/(6π²)` | `= (8/3)/(16π²)` ✓ exact |
| `κ⁻¹ = c_1 Λ_f²` | `Λ_f²/(6π²)` | ✓ |
| `G = 1/(16π c_1 Λ_f²)` | `3π/(8Λ_f²)` | ✓ exact, **POSITIVE** (Λ_f>0) |

**Gate-0 cross-checks:** STr=+8/3 reproduced two independent ways — (a) the imported `supertrace_vhalf` primitive, and (b) reconstructing the chain `per-Dirac-component −1/12 → per-Weyl −1/6 → STr = 16·(−1)·(−1/6) = +8/3`. Dirac signed contribution = +1/3. The HK-vs-Frolov-Fursaev dual cross-check holds. The sign is consistent with G>0 (Gate 0). Λ_f kept symbolic (Gate-3 scope), correctly not pinned. **Consistent.**

---

## 6. Non-hardwired verdict — INDEPENDENTLY CONFIRMED (v20 bug absent)

I fed `verdict()` a **genuinely injected** contaminant by running a curved-target a_1 through the *full* `a1_curvature_decomposition` machinery (not merely synthetic booleans):

| Input | Path | verdict() output |
|---|---|---|
| contaminated a_1 (curved target injected, `coeff_R^target = −4`) → computed `has_nonR_residual=True` | full decomposition → verdict | **DEAD (a_1 NOT clean ∝ R)** ✓ |
| nonzero torsion flag | verdict | **DEAD (non-Laplace-type)** ✓ |
| clean inputs | verdict | **PASS** ✓ |

The category is derived from an if/elif ladder on the flags (≥4 distinct `category =` assignments), **not** a hardcoded literal. The v20 hardcoded-decisive-boolean bug is **absent**. The driver's three required self-tests all fire. **Non-hardwired confirmed.**

---

## 7. Driver re-run — INDEPENDENTLY CONFIRMED

| Check | Result |
|---|---|
| Exit code | `0` (both runs) |
| `ALL_PASS` | `True` |
| VERDICT | `PASS (a_1 clean propto R)` |
| Byte-identical across two runs | **YES** (`diff` empty) |
| Floats on decisive output | **none** (scan clean; only timing/citation/version numerals) |
| Source guard FIRES on injected violation | YES (`endomorphism_E: ['float(']`) |
| `octonion_algebra` on decisive path | **absent** (RUNTIME PASS; not in sys.modules) |
| R[g=e·e] anchor (M≠0) | `14187524733311967018208791837/634906109300195099205387025 ≠ 0` (exact Q) |
| R[g=e·e] (M=0 baseline) | `0` (flat vacuum) |

---

## Physics consistency summary (universal checks)

| Check | Status | Confidence | Notes |
|---|---|---|---|
| 5.1 Dimensional analysis | CONSISTENT | INDEPENDENTLY CONFIRMED | c_1 dimensionless × π^−2; κ⁻¹ ~ Λ_f² (mass²); a_1 ~ R (mass²); all consistent |
| 5.2 Numerical/symbolic spot-check | CONSISTENT | INDEPENDENTLY CONFIRMED | explicit gamma matrices, both reps, exact over Q(i) |
| 5.5 Intermediate spot-check | CONSISTENT | INDEPENDENTLY CONFIRMED | −1/12 per component → −1/6 per Weyl → +8/3 STr chain re-derived |
| 5.6 Symmetry (Lorentz/trace) | VERIFIED | INDEPENDENTLY CONFIRMED | ω antisymmetric (so(3,1)); γ^{μν} traceless rep-independent |
| 5.8 Math consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | Clifford algebra exact; residual a_1−coeff_R·R = 0 |
| 5.10 Literature agreement | AGREES | INDEPENDENTLY CONFIRMED | Vassilevich eqs (4.14)/(4.15)/(3.27)/(4.1) extracted from primary PDF |
| 5.11 Plausibility | PLAUSIBLE | INDEPENDENTLY CONFIRMED | G>0; a_1 ∝ R with the universal −1/12/component coefficient |
| Gate-0 consistency | CONSISTENT | INDEPENDENTLY CONFIRMED | STr=+8/3 two ways; dual cross-check holds |
| Convention lock (mostly-minus, tr1=4) | CONSISTENT | INDEPENDENTLY CONFIRMED | matches state.json convention_lock |
| Non-hardwired verdict | VERIFIED | INDEPENDENTLY CONFIRMED | genuine contaminant → DEAD; v20 bug absent |

---

## Discrepancies / caveats

1. **Naming (a_1 vs a_2):** the driver/tex call the curvature-linear coefficient "a_1"; Gilkey/Vassilevich call it "a_2". This is a labeling convention (Vassilevich indexes by mass dimension; odd coefficients vanish). The object is correctly identified. **Not a physics error; noted for the write-up so the paper uses a consistent, citable convention.**
2. **Torsion check is on a toy tetrad, not the matter tetrad** (item 4). Sufficient because ω is Levi-Civita *by construction* (torsion=0 for any invertible e) and the "D is Laplace-type / no associator" fact is inherited from verifier-hardened v18-Ph77. The Gate-1 driver does not independently re-prove the no-associator property on the matter background — a reasonable scope boundary (blocked by the symbolic watchdog), not a gap.
3. **F-term sign convention** differs from Vassilevich (+¼[γ,γ]F vs −½γ^{μν}F). Immaterial — traces to zero either way.

None of these affects the verdict.

---

## CONFIDENCE: HIGH

The decisive check (explicit-Clifford a_1=−R/3) is independently confirmed in two gamma reps exact over Q(i). The structural claim is confirmed against the **primary source** (Vassilevich PDF, equations read directly). c_1, Gate-0 consistency, and the non-hardwired verdict are independently reproduced. The one nuance (toy-tetrad torsion check) is documented and assessed as sufficient given the by-construction Levi-Civita connection plus the upstream v18-Ph77 result. Driver re-run is byte-identical, exit 0, no floats, octonion_algebra absent.

## VERDICT: **Gate 1 PASSES — a_1 is a clean ∫R (`a_1 = −R/3` per Dirac, `c_1 = 1/(6π²)`, `G = 3π/(8Λ_f²) > 0`); not contaminated.**
