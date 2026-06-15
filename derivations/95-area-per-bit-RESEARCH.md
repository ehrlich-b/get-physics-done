# Phase 95 / v35.0-candidate — THE AREA-PER-BIT KILL-TEST — RESEARCH (executor grounding bible)

> Source prompt: `paper6-area-per-bit-prompt.md` (slot 95, registered by Bryan 2026-06-14, paste-after-v34).
> The native-holography diagnostic / entanglement-route Limb A.
> **You (the executor) have NO web/arxiv tools. This file is your complete grounding.** Everything here was
> de-risked by the orchestrator exact over ℚ before you were spawned; the load-bearing numbers are in §9.
> Exact over ℚ on every decisive line (sympy.Rational / cancel; NEVER float in a verdict). Fail-fast gates.
> Non-hardwired verdict() ladder with self-tests. Milestone HOLD for human ratification — do NOT self-register
> the next slot, do NOT run `gpd phase complete`/`state advance`.

---

## 0. BOTTOM LINE (what this run decides, and the honest expected landing)

**The question.** Does the variety (CP², the C\*-cut of OP², where v23's faithful-point fiber kill does not reach)
natively set the **bits↔geometric-area exchange rate** as a UNIVERSAL CONSTANT (→ a background scale; gravity is a
contingent import; **fork A**) or as a SHEARING field (→ a candidate gravitational field)? This is the
off-faithful / on-variety form of the entanglement route's sharp-claim-1: slot 83 ran that claim AT the faithful
point I/3 (= v23) and DIED (∇S = 0, point-specific). This run runs it on STRUCTURED (off-faithful) states with the
area pairing. It is built entirely from CERTIFIED objects (v25 moment doublet + v26 G_M + v31/v32 TT mode), so it
is CHEAP.

**It is NOT a claim that FS-area derives gravity.** The FS metric is IMPORTED (Fence 2 + Bug-guard 2). This is a
DIAGNOSTIC of whether native area↔entropy variation exists at all on the variety.

**THE ORCHESTRATOR DE-RISK ALREADY CRACKED THE STRUCTURE (exact over ℚ, you must reproduce it — see §2/§9):**

1. The FS metric **is** the real part of the quantum geometric tensor (Provost–Vallée 1980: Fubini–Study = the
   quantum Fisher metric on pure states). Therefore **every FS-canonical local area density is a contraction of the
   QGT-real / Fisher metric.** Concretely:
   - **Candidate (ii)** — the FS metric-trace of the v31 metric-mode dφ_M⊗dφ_M, i.e. |∇φ_M|²_g — is **identically**
     the quantum variance **Var_p(M) = ⟨M²⟩_p − ⟨M⟩²_p** (verified as a symbolic identity, A_ii − Var ≡ 0).
   - **Candidate (iii)** — the KKS symplectic gradient-norm |X_{φ_M}|²_ω with X_φ = J∇φ — equals candidate (ii) by
     the Kähler identity (J is a g-isometry ⇒ |J∇φ|²_g = |∇φ|²_g). So **(iii) = (ii) = Var** as well.
   - Var_p(M) = the quantum Fisher information of the moment field φ_M = a **STATE-SPACE** object.
2. The v26 entropy response decomposes **exactly** as **G_M(p) = Var_p(M) + ¾⟨M⟩²_p − ½Tr(M²)** (symbolic identity,
   G_M − (Var + ¾⟨M⟩² − ½TrM²) ≡ 0). This is the relative-entropy Hessian = the Fisher information PLUS a
   non-proportional correction. So **G_M is NOT ∝ Var.**
3. Consequently **R(p,M) = A_M/|G_M| SHEARS** strongly in p and across M (it is NOT a pure constant). BUT the
   numerator is the Fisher information and the denominator is the relative-entropy Hessian — **both state-space
   information measures.** This shear is the (well-known, state-space) disagreement between two information metrics,
   **NOT a geometric bits↔area exchange rate.**

**THE HONEST EXPECTED VERDICT: DEAD / fork A, via the FISHER-CORPSE mechanism (Bug-guard 3).** The variety's only
FS-canonical "area" is identically the QGT/Fisher metric (v17's corpse — a positive-semidefinite object on STATES,
not a spacetime metric). There is no native geometric area independent of the state-space information geometry to
pair with the bits. Hence the variety does NOT natively set a geometric bits↔area rate; the rate (Ryu–Takayanagi's
G) is a contingent import → **fork A**, the honest-scope TOE. **This is a REAL result:** it closes the entanglement
route and confirms the bits↔area rate is a contingent import — the same conclusion family as v33 FORCES-NOTHING and
the v23 ∇S = 0 death, reached here through a sharper, more defensible identity (the canonical area IS the bit-counter
metric).

**Your job is to REACH this rigorously, not to assume it.** Run G0 (pin the area canonically, Bug-guards 1/3/4),
G1 (the kill-test, exact R, the homogeneity + denominator-zero handling), and classify with a non-hardwired ladder.
If the exact math contradicts the expected landing, REPORT THE TRUTH (a genuine geometric shear would be the
surprise → G2). Do not glaze; do not force "constant" when R shears; do not promote the Fisher-corpse shear to LIVE.

### Verdict taxonomy (as in the prompt, with the Fisher-corpse refinement made explicit)
- **DEAD-CONSTANT** — R is p- and M-independent up to one overall scale ⇒ universal background rate, no native
  gravity; contingent import (κ, Λ company); **fork A**. *[Literal-constant reading. The de-risk shows R is NOT
  literally constant — see DEAD-FISHER below for the actual mechanism.]*
- **DEAD-FISHER (the de-risked expected landing; same fork-A conclusion)** — the unique FS-canonical local area =
  Var = the QGT/Fisher metric (the v17 corpse), so R's shear is Fisher-info vs relative-entropy, a state-space fact,
  NOT a geometric rate ⇒ the variety sets no native geometric bits↔area rate ⇒ contingent import ⇒ **fork A**.
- **LIVE-SCALAR** — R shears via a GENUINELY geometric area (NOT the Fisher corpse) but trace-only ⇒ Nordström
  ceiling (empirically dead gravity; no light bending); partial, NOT Einstein.
- **LIVE-TENSOR** — R shears via a genuinely geometric area carrying the v31 TT tensor structure ⇒ the variety
  natively sets a SHEARING tensor exchange rate; the surprise; upstream-but-pointing-at the clamp (does NOT by
  itself = Einstein — see anti-overclaim).
- **INCONCLUSIVE** — the verdict FLIPS between two FS-canonical area definitions (Bug-guard 1) ⇒ artifact; report,
  do NOT pick the favorable one.

---

## 1. THE CERTIFIED OBJECTS (all exact over ℚ; the engine API)

**Work entirely in h₃(ℂ) = the C_u cut = CP².** The matter directions are already 3×3 complex Hermitian (the
Gell-Mann/SU(3) basis), points are rank-1 complex projectors, and ⟨X,p⟩ = Tr(XP), X# = adj(X). The octonion engine
is NOT needed and must NOT be on the decisive path (octonion_algebra.py is BANNED; the cut is associative-clean).

### 1.1 Engine (reuse the certified helpers; or re-implement in h₃(ℂ) and assert agreement at Gate 0)
- Trace form / inner product: **⟨X,p⟩ = Tr(X·P)** (for Hermitian X, P this equals Tr(jordan(X,P))). Source:
  `code/variety_moment_doublet.py` `inner(A,B)=Tr(jordan(A,B))`; `code/ring_lemma_verification.py` `jordan`, `Tr`.
- Freudenthal sharp: **X# = adj(X) = X² − Tr(X)·X + ½((TrX)² − Tr(X²))·I** (the matrix of cofactors). Source:
  `code/variety_moment_doublet.py` `sharp(X)`. For TRACELESS M this reduces to **M# = M² − ½Tr(M²)·I.**
- Rank-1 CP² point: **P(z) = v v† / (v† v), v = (1, z₁, z₂)ᵀ.** Source: `code/tensor_probe.py` `P_chart()`.
  Idempotent (P²=P), Tr P = 1. The vertex/north-pole is z→0 ⇒ P → diag(1,0,0) = E_11.
- FS metric (Kähler potential K = log ρ, ρ = 1 + |z₁|² + |z₂|²): **g_{i j̄} = ∂_i∂_{j̄}K = (ρ δ_{ij} − z̄_i z_j)/ρ².**
  Physical normalization `MET_SCALE = 1/2` gives Ric = 6g, R = 24, Vol = π²/2 (`code/tensor_probe.py` `fs_metric`).
  **The overall metric scale is IRRELEVANT to the constancy test** — it is the "single overall scale" G1 allows to
  be normalized away. Keep it explicit and report it, but do not let it decide the verdict.

### 1.2 The moment / entropy / area objects
- Moment field (the "potential"): **φ_M(p) = ⟨M,p⟩ = Tr(M·P(z)) = (v† M v)/(v† v).** Linear in M, linear in P.
- v25 moment doublet at address p: **m(p) = Tr(X) − ⟨X,p⟩, q(p) = ⟨X#,p⟩,** face-purity **r = q/m²,** S_face = f(r).
  Source `code/variety_moment_doublet.py` (`m_moment`, `q_moment`). The structured state is **X = I/3 + εM.**
- v26 entropy response (THE BITS SIDE): **δ²S = (9/2)·G_M(p)·ε²,** with
  **G_M(p) = ⟨M#,p⟩ − ¼⟨M,p⟩² = Tr(M#·P) − ¼ Tr(M·P)².** G_M ≤ 0 (= minus the second-order relative entropy).
  Source `code/variety_sourced_field_equation.py` `G_M(M,p)`.
- Quantum variance (the QGT-real / Fisher object): **Var_p(M) = ⟨M²,p⟩ − ⟨M,p⟩² = Tr(M²P) − Tr(MP)².** ≥ 0.
- v31/v32 (for G2 only): the matter-sourced metric mode is the gradient bilinear **dφ_M⊗dφ_M** (`tensor_probe.py`
  `grad_bilinear`); the certified TT norm **‖TT(B3)‖² = (1/30)(Tr M²)²**; the Lichnerowicz stiffness
  **ε = λ_L − 2Λ = 32 − 12 = 20** (`gate0_v33.py`, `lichnerowicz_response.py`). York TT split: `york_tt_residue`.

### 1.3 The matter directions (v24 families; traceless Hermitian; reproduce ≥3 + one generic)
- **s01** = [[0,1,0],[1,0,0],[0,0,0]] (symmetric real off-diagonal, λ₁ Gell-Mann). Tr=0, rank 2.
- **a01** = [[0,−i,0],[i,0,0],[0,0,0]] (Hermitian "antisymmetric", λ₂). Tr=0, rank 2.
- **d1**  = [[1,0,0],[0,−1,0],[0,0,0]] (diagonal traceless, λ₃). Tr=0, rank 2, det₃ = 0.
- **gen** = [[1,0,0],[0,1,0],[0,0,−2]] ("d2", generic with **det M = −2 ≠ 0**, full rank). Tr=0.
Source `code/gate0_v33.py` `GM = {...}`, `M_GEN`. NOTE (de-risked): for the three rank-2 directions M# = diag(0,0,−1)
(= −E₃₃) because each acts in the (1,2) block with eigenvalues {+1,−1,0} ⇒ M² = the (1,2)-block projector,
M# = M² − I = −E₃₃. For gen, M# = diag(−2,−2,1).

---

## 2. G0 — SETUP + PIN THE AREA OBJECT (the load-bearing definitional gate; do this carefully)

This gate decides the run, because (de-risked) the verdict turns entirely on **what counts as a canonical
matter-induced area on the variety.** Do all of the following exactly over ℚ.

**G0.1 — reproduce the certified objects on s01, a01, d1, gen.** Build P(z), φ_M, M#, G_M, Var on each direction.
Confirm G_M ≤ 0 (sample several ℚ-points) and Tr M = 0.

**G0.2 — confirm OFF I/3 (Bug-guard 4: not vacuous like v23).** The structured states must have ∇S_face ≠ 0, i.e.
G_M(p) must genuinely VARY with p (not be the constant-by-F₄-symmetry value of the faithful point). The de-risk
confirms G_M(p) is a non-constant rational function of p for every direction — so the test is NOT vacuous. Verify by
exhibiting ≥2 ℚ-points with different G_M for at least one direction.

**G0.3 — PIN A_M(p) CANONICALLY (state the definition explicitly; justify FS-canonicity + matter-functoriality).**
The three prompt candidates and the de-risked facts:
- **(ii) FS metric-trace of the v31 metric-mode dφ_M⊗dφ_M:** A_M^(ii)(p) = g^{i j̄} ∂_iφ_M ∂_{j̄}φ_M = |∇φ_M|²_g.
  **DE-RISKED IDENTITY: A_M^(ii) ≡ Var_p(M)** (the quantum variance / Fisher information). You MUST reproduce this
  as a symbolic identity (A_ii − Var = 0), not just at points. This is the standard Kähler fact that the squared
  gradient of an expectation function equals the variance.
- **(iii) KKS (Kirillov–Kostant–Souriau) symplectic area of the perturbation:** the moment-map component is φ_M, its
  Hamiltonian vector field is X_{φ_M} = J∇φ_M, and the symplectic gradient norm |X_{φ_M}|²_ω. **DE-RISKED: ≡ A_M^(ii)
  ≡ Var,** because J is a g-isometry on the Kähler manifold (|J∇φ|²_g = |∇φ|²_g). Verify cleanly (use b̄ = conj(z)
  with real arithmetic at ℚ-points, OR a swap-based conjugation — do NOT mix independent Wirtinger symbols with
  sympy `conjugate()`, which silently breaks the identity; that was an orchestrator-side throwaway bug, the identity
  is true). Two canonical definitions AGREEING is the Bug-guard-1 pass (no flip).
- **(i) FS Riemannian measure of the perturbation's support:** this is a GLOBAL volume (one number per M, via
  `l2_scalar`), NOT a local field over p. Pairing a per-M constant against the p-varying G_M(p) gives a p-shear that
  is purely the variation of the DENOMINATOR — the homogeneity check (G1) rules this out as a non-shear of the RATE.
  Report it as the control that exhibits the homogeneity-artifact failure mode, not as a competing local area.

**G0.4 — THE FISHER-CORPSE DETERMINATION (Bug-guard 3, load-bearing).** Record explicitly: the FS metric = the real
part of the QGT (Provost–Vallée), so the canonical local area A_M = Var = the quantum Fisher information of φ_M — a
STATE-SPACE object, the same family as v17's dead real-QGT/cone-Hessian/Fisher metric. There is NO FS-canonical
local area that is not a QGT/Fisher contraction; the only way to obtain a geometric area independent of the
state-space information geometry is to IMPORT a different metric — which is precisely the contingent import (fork A).
**Decision rule:** if the canonical area is the Fisher object, then a shear of R does NOT certify a geometric rate
(it is Fisher vs relative-entropy) ⇒ route to DEAD-FISHER / fork A, do NOT proceed to G2 with a contaminated object.

---

## 3. G1 — THE KILL-TEST (cheap, decisive; exact over ℚ)

Compute **R(p, M) = A_M(p) / |G_M(p)|** exactly over ℚ along the structured families and across s01, a01, d1, gen,
using the pinned canonical A_M = A_M^(ii) = Var (and the cross-check A_M^(iii)).

**The verdict ladder (apply the bug guards BEFORE classifying):**
1. **Denominator-zero handling.** G_M(p) → 0 on a real locus — for the rank-2 directions this is the **EQUATOR**
   (e.g. z₁=±1, z₂=0, where the (1,2)-block face is maximally mixed), NOT the vertex; at the vertex z→0 it is instead
   the **numerator** Var that vanishes (G_M = −1/4 stays finite) — where R blows up (or → 0). These are ZEROS OF THE
   BIT-COUNTER (or of the area), not shears of the rate; exclude that locus (state it) or work with the reciprocal
   |G_M|/A_M, which is finite there. Do NOT report a blow-up as "R shears."
2. **Homogeneity check.** A ratio that "varies" only because A_M is homogeneous-constant while G_M varies is NOT a
   shear of the RATE. A real geometric shear needs A_M and G_M to have DIFFERENT M-structure AND a p-dependence not
   removable by one global normalization. Test: is R(p,M) a genuine non-constant function of p after fixing one
   global scale per the prompt? (De-risk: yes, R varies in p — but via the Fisher mechanism, step 3.)
3. **Fisher-corpse gate (Bug-guard 3, decisive).** The canonical A_M = Var = the QGT/Fisher metric. So R = Var/|G_M|
   = (Fisher information)/(relative-entropy Hessian) — a comparison of two STATE-SPACE information measures. This is
   NOT a geometric bits↔area exchange rate. ⇒ **DEAD-FISHER / fork A.** STOP (do not proceed to G2).
4. **Only if a GENUINELY GEOMETRIC, non-Fisher, FS-canonical, matter-functorial area gives a real p/M shear** (the
   surprise the de-risk did NOT find): proceed to G2.

**The decomposition that explains the shear (reproduce it exactly):**
G_M = Var + ¾⟨M⟩² − ½Tr(M²) ⇒ R = Var / |Var + ¾⟨M⟩² − ½Tr(M²)|. The shear is entirely the relative-entropy
correction ¾⟨M⟩² − ½Tr(M²) — a state-space quantity, not geometry.

**Preempting a spurious LIVE-TENSOR (adversarial-sharpened).** Do NOT claim the TT channel is "structurally
precluded" — it is PRESENT. Because the metric-mode dφ_M⊗dφ_M is rank-1 (s⊗s with |s|²_g = Var), EVERY FS-canonical
area invariant of it is a fixed power of the Fisher variance: the metric-trace A_ii = Var, the full norm
‖dφ_M⊗dφ_M‖²_g = 4·Var², and the transverse-traceless part A_TT = ‖traceless part‖²_g = 3·Var². So the TT channel
exists but is itself a Fisher monomial (a power of Var) — it supplies NO independent geometric shearing rate.
LIVE-TENSOR is killed not by TT-absence but by TT-being-Fisher. State this.

---

## 4. G2 — THE RANK WALL (only if a legitimate geometric shear survives G1's bug guards; NOT expected)

If and only if step 4 of G1 fires: decompose the shear's source against dφ_M⊗dφ_M and test whether it is the TRACE
of the v31 TT(B3) mode (→ LIVE-TENSOR; connect to v32 ‖TT(B3)‖² = (1/30)(Tr M²)², ε = 20) or pure trace (→
LIVE-SCALAR / Nordström). Reproduce the v31/v32 anchors (`tensor_probe.grad_bilinear`, `york_tt_residue`,
`lichnerowicz_response`, ε = 20) as the certified inputs. The de-risk expects this gate is NOT reached (the canonical
area is the Fisher trace; the shear is state-space). If you reach it, you have found the surprise — report it loudly
and route through the anti-overclaim (§8): LIVE is necessary-not-sufficient for gravity.

---

## 5. CONVENTIONS + CONTROLS + SELF-TESTS (non-negotiable)

- **Exact over ℚ throughout.** sympy.Rational / cancel / simplify; never a float in a verdict (Bug-guard 5).
- **Complex chart, h₃(ℂ).** P = vv†/(v†v); ⟨X,p⟩ = Tr(XP); X# = adj(X). No octonion engine on the decisive path.
- **The verdict() function MUST be non-hardwired** — a DERIVED ladder from the computed booleans, with self-tests:
  - a RIGGED-CONSTANT input (an area defined so A ∝ |G_M| by construction) → returns DEAD-CONSTANT.
  - a HAND-BUILT SHEARING input (an area with genuinely different M-structure, NOT the Fisher object) → returns LIVE
    (SCALAR or TENSOR per the trace test).
  - a verdict that FLIPS under area-redefinition (feed two non-agreeing canonical areas) → returns INCONCLUSIVE.
  - the Fisher-corpse path (A = Var) → returns DEAD-FISHER / fork A.
  Print all self-tests PASS before the real verdict line.
- **Commit after each gate** (G0, G1, [G2]) so a socket death loses at most one gate
  ([[feedback_executor_socket_timeout_long_agent]], [[feedback_executor_watchdog_stall_long_symbolic]]). These
  computations are CHEAP (3×3 matrices, rational functions in 4 chart symbols) — no V-matrix sweeps, no long
  symbolic stalls — so this should run in minutes.

---

## 6. FENCES (binding, verbatim — copy into SUMMARY/VERDICT)

NO Einstein-equation / G=κT / gravity / Newton / dark-matter / geodesic language as a DERIVED result; the bits↔area
rate is a framework ratio (a contingent import like κ, Λ unless G1 forces otherwise), **NOT Newton's G**; FS is USED,
not derived; signature **Riemannian** (Wall 2 unpaid — NOTHING is called gravity until signature is paid);
DEAD-CONSTANT / DEAD-FISHER and LIVE-\* are NOT derivations of gravity. This run does NOT retract v33 (extremize
FORCES-NOTHING), v34 (induce CLOSES-CONDITIONAL), v17–v21 (fiber kills), or v23 (I/3 death). **Paper 5 remains the
only result in the more-than-nothing column.**

---

## 7. ANTI-OVERCLAIM (Jaksland arXiv:2005.05055)

LIVE (either) = the variety sets a non-constant exchange rate — NECESSARY, not sufficient, for gravity; it is the
area-side diagnostic of the entanglement route, UPSTREAM of the clamp (state-fp ⟹ metric-fp). Even LIVE-TENSOR shows
native area↔entropy variation, NOT that the metric obeys a field equation. A generic Jacobson/RT recovery validates
nothing program-specific — the originality is whether the variety FORCES the rate, not that an area law exists.
DEAD (CONSTANT or FISHER) is the expected and honest outcome; it closes the entanglement route and is the green light
for fork A. Holography is theorem-blocked natively (h₃(O) is finite Type-I₃ by Zelmanov; the "Area/4G from an
algebra" result CPW arXiv:2302.01938 needs a Type III₁ factor the exceptional algebra cannot have). The program has
the Bekenstein BOUND (S ≤ Area, G-free) but NOT the RT EQUALITY (Area = 4G·S, G-valued); the G-valued equality is the
unpaid step = the clamp.

---

## 8. THROUGH-LINE

v24 entropy landscape (LIVE) → v25 moment doublet (X,X#) → v26 source field G_M + MaxEnt → v27 local balance →
v28 spinor moment → v29/v30 clock sector closes → v31 tensor wall OPENS → v32 tensor dictionary (κ=1/30, ε=20) →
v33 EXTREMIZE forces nothing → v34 INDUCE CLOSES-CONDITIONAL (gravity gap = the single state-fp⟹metric-fp clamp) →
**v35 AREA-PER-BIT: does the variety natively set a bits↔area rate?** Expected DEAD (fork A) — the canonical area is
the QGT/Fisher corpse, so there is no native geometric rate; closes the entanglement route, the SIXTH brainstorm
angle reducing to the one clamp. Every gravity angle now points at the same single unpaid step.

---

## 9. DE-RISKED GROUND TRUTH (orchestrator, exact over ℚ — use to self-check your engine at G0)

Chart point P0: z₁ = 1 + 2i, z₂ = −1 + i ⇒ ρ = 1 + 5 + 2 = 8. Point P2: z₁ = −1, z₂ = 2 − 3i ⇒ ρ = 1 + 1 + 13 = 15.

Symbolic identities (must hold for ALL p, all M) — reproduce as `simplify(expr) == 0`:
- **A_M^(ii)(p) − Var_p(M) = 0** (metric-trace area = quantum variance).
- **A_M^(iii)(p) − Var_p(M) = 0** (KKS symplectic = same, Kähler tie).
- **G_M(p) − (Var_p(M) + ¾⟨M⟩²_p − ½Tr(M²)) = 0** (entropy response decomposition).

Point values (A_M = A_M^(ii) = Var):

| M    | point | ⟨M,p⟩  | Var = A_M | G_M       | R = A/\|G\| |
|------|-------|--------|-----------|-----------|-------------|
| d1   | P0    | −1/2   | 1/2       | −5/16     | 8/5 = 1.600 |
| d1   | P2    | (see)  | 2/15      | −13/15    | 2/13 ≈ 0.154|
| s01  | P0    | (see)  | 11/16     | −17/64    | 44/17 ≈ 2.588|
| a01  | P0    | (see)  | 1/2       | −5/16     | 8/5 = 1.600 |
| gen  | P0    | (see)  | 27/16     | −81/64    | 4/3 ≈ 1.333 |
| gen  | P2    | (see)  | 26/25     | −1/25     | 26 (denominator near-zero — homogeneity/zero-locus artifact, NOT a rate shear)|

Worked anchor (d1 at P0): φ = (1−|z₁|²)/ρ = (1−5)/8 = −1/2; ⟨M²⟩ = (P₀₀+P₁₁) = 6/8 = 3/4; Var = 3/4 − 1/4 = 1/2;
M# = diag(0,0,−1), ⟨M#⟩ = −P₂₂ = −2/8 = −1/4; G_M = −1/4 − ¼·(1/4) = −5/16; decomposition check
Var + ¾⟨M⟩² − ½Tr(M²) = 1/2 + ¾·1/4 − ½·2 = 1/2 + 3/16 − 1 = −5/16 ✓.

**R is NOT constant** (8/5, 2/13, 44/17, 4/3, … vary by direction and point) ⇒ the literal DEAD-CONSTANT reading
FAILS. **The shear is Var/|G_M| = Fisher/(relative-entropy), state-space, not geometric** ⇒ the honest landing is
**DEAD-FISHER / fork A** (Bug-guard 3). Reproduce, classify with the non-hardwired ladder, and report the truth.
