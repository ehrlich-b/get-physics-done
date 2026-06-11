# 89 — RESEARCH: Per-Point Thermal Time — the Referent-Free Consistency Test (Claim 2 / J4)

**v29.0 Phase 89. A GENUINE FORK.
Drivers: `code/thermal_time_consistency.py` (executor, 12/12 PASS),
`code/thermal_time_consistency_verify.py` (independent path, 5/5 PASS). Exact over Q/Q(t).
VERDICT: DEAD — per-point thermal time is irreducibly face-local.**

This is CLAIM 2 — the J4 thermal-time question pinned since slot 83, run with the variety
machinery it was waiting for. The question (referent-free): do the per-face modular
generators of ONE structured state cohere into ONE global generator up to compression — an
emergent global state-time — or is thermal time irreducibly face-relative? Thermal time =
Connes–Rovelli state flow (cited); NO thermodynamic postulate enters any verdict path —
everything is exact state algebra. No proper-time/metric/Einstein/dark-matter language; the
lapse/twist outputs are CANDIDATES for the Block-A design, not metric components.

---

## 0. Setup and the consistency question

Structured state `X = I/3 + εM` (`Tr M = 0`, `M` symbolic, positive definite — the observer
condition). At each event `p` (rank-1 idempotent), the face state
`ρ_face(p) = C_pX/Tr(C_pX)` on the complementary 2-face, and the per-face modular generator
`K_face(p) = −log ρ_face(p)`. The consistency question:
> does there exist ONE global Hermitian `H` with **`traceless(C_pH) = β·traceless(K_face(p))`
> for ALL `p`**, with ONE global constant `β` and per-face `I`-shifts quotiented (modular
> flow is unchanged by adding multiples of the face identity)?

LIVE upgrades the Jacobson joint J4 from IMPORT to PROGRAM-SUPPLIED ({J5} → {J4, J5}); DEAD
retypes time as face-local and the obstruction becomes connection-shaped data. Both branches
are consumed downstream (the Block-A unfreezing design).

---

## 1. The trap inventory (load-bearing — the fences that keep the verdict honest)

- **Trap #5 — direction-only is VACUOUS.** On a 2-face (rank-2 spin factor), Cayley–Hamilton
  gives `ρ² = Tr(ρ)ρ − det₂(ρ)(1−p)`, so any analytic `f(ρ) ∈ span{1−p, ρ}` and
  `traceless(f(ρ)) ∥ traceless(ρ)`. Hence `traceless(K_face) ∥ traceless(ρ_face) ∥
  traceless(C_pX)` AUTOMATICALLY — "common generating direction" is trivially LIVE with
  `H = X`. **The content is NOT the direction — it is the RATES** `b(p) = −½log(λ₊/λ₋)`
  (transcendental in the gap), jointly realizable by one linear object with one `β`. Verified
  symbolically; never used as evidence.
- **Trap #6 — single-rotation / eigenframe faces are co-diagonal** (`C_{E_ii}X` diagonal,
  standard-family faces share an eigenvector): consistency automatic, ZERO evidence. **Verdict
  faces must be FULLY GENERIC** (`p = vv*`, all three eigencomponents of `v` nonzero). Rational
  anchor: `v = (1,2,2)/3` (unit), `X = diag(1,2,3)/6` (positive, `Tr = 1`, distinct, logs affine
  in `{log2, log3}`). Verified the anchor face mixes all three eigendirections (`[X,p] ≠ 0`).
- **Trap #7 — first order is structurally LIVE.** `−log(½I + εδρ) = log2·I − 2εδρ + O(ε²)`:
  the `ε¹` part is LINEAR in `δρ`, so `H⁽¹⁾ ∝ M` always realizes it
  (`traceless(K)⁽¹⁾ = −3·traceless(C_pM)`, a single compression). `ε⁰` (vacuum, `K ∝ I`) and
  `ε¹` (always coherent) are zero-weight controls. **The verdict lives at `ε²`.**

---

## 2. The reduction (T1) — the verdict is a finite harmonic computation

Expanding `ρ_face = ½I + εδρ⁽¹⁾ + ε²δρ⁽²⁾`, the spin-factor rate `b(s)/s → −2` at `O(ε⁰)`
gives `traceless(K_face)⁽²⁾ = −2·δρ⁽²⁾`; and `δρ⁽²⁾ = (9/4)·⟨M,p⟩·traceless(C_pM)` (from
`ρ_face = C_pX/m`, `m = 2/3 − ε⟨M,p⟩`). Hence
> **`K_face⁽²⁾(p) = −(9/2)·⟨M,p⟩·traceless(C_pM)`** (verified symbolic `M` at `E_11`).

**The level-count lemma:** `traceless(C_pH)` of a FIXED global `H` is a single compression =
LEVEL ≤ 1 in `p`, per Peirce block; but `K⁽²⁾ = ⟨M,p⟩(level-1)·traceless(C_pM)` is LEVEL-2
capable (the `⟨M,p⟩²`-type sector — the v26 `R_M` story). Therefore:
> **A global `H` exists at order `ε²` ⟺ `K⁽²⁾` is compression-realizable ⟺ its level-2 part
> vanishes identically.** The v26 precedent (`R_M ≢ 0`) is why the prior leans DEAD; the open
> question is whether the specific log-expansion combination cancels (the `δr = 0` precedent
> shows such cancellations happen when the algebra wants them).

This reduces Claim 2 to a finite, exact harmonic computation in the certified v25/v26 toolkit.

---

## 3. T3 — the verdict (at ε², exact): DEAD

The decisive test: does a global `H` (27 unknowns) satisfy `traceless(C_pH) = ⟨M,p⟩·
traceless(C_pM)` (symbolic `M`) over `E_11` + families? Result (`linsolve`, and an independent
explicit certificate):

| sector | `E_11`-alone | `E_11` + families | verdict |
|---|---|---|---|
| u-complex (cut), 8-param `M` | **solvable** | `E_11` + 2 cut families → **EmptySet** | DEAD |
| full OP², 26-param `M` | **solvable** | `E_11` + (off-u, real) → **EmptySet** | DEAD |

`E_11`-alone is solvable (`H`'s lower block `= ⟨M,p⟩·M`'s lower block + `I`-shift — no
over-determination at a single face), so the machinery is sound; the inconsistency comes from
even ONE additional generic face. **Explicit certificate (independent path):** fix `H` on the
`E_11` face, leaving the `E_11`-row (`x2, x3`) and the `I`-shift free; substitute into the
off-u `(1,1)` family — the residual field CANNOT be killed by any choice of the 17 free
parameters (`linsolve = EmptySet`). The per-face `I`-shift gauge `H → H + c·1` is quotiented
(it leaves `traceless(C_pH)` invariant), so the DEAD is not a gauge artifact.

> **VERDICT = DEAD: there is NO global modular generator; per-point thermal time is
> irreducibly FACE-LOCAL.**

**The payload (the obstruction, extracted).** The level-2 part of `K⁽²⁾` is the
**clock-twist / modular-anomaly field** — a tangent-valued `R_M`-cousin: its scalar
`|K⁽²⁾|²` carries the `⟨M,p⟩²` level-2 sector (the v26 `R_M = ⟨M,p⟩² − α⟨M#,p⟩ − βTrM²`
story). It is the connection-shaped datum: the parallel-transport-of-clocks twist, now
matter-pinned (the v28 gluing-`U(1)` carries a matter-pinned RATE twist, not just a class).

**T4 finite-ε cross-check (corroboration, no design hole).** At the anchor `X = diag(1,2,3)/6`,
`p` from `v = (1,2,2)/3` (formal logs `ℓ_i = log x_i`): the per-face rate of `traceless(K_face)`
vs `traceless(C_p log X)` is NOT a single global ratio across faces (the rate `b(s)` is a
DIFFERENT transcendental than the `ℓ_i`), so the finite-ε check is also DEAD — **agreeing in
sign with the ε² verdict (no design-hole STOP triggered).**

---

## 4. Scope and the consumption ledger (Gate 5; no claims)

**Anti-overclaim.** DEAD is a SCOPE THEOREM (the v23 fork discipline): per-point thermal time
does not cohere into a global state-time at the deciding order; time is face-relative. No
proper-time/metric/Einstein language; the lapse (LIVE payload, NOT realized) and the twist
(the DEAD payload, the obstruction field) are design INPUTS for Block A, not physics claims.
**J4 bookkeeping:** DEAD ⟹ J4 (Jacobson joint thermal time) STAYS IMPORTED; the originality
budget remains `{J5}` (not promoted to `{J4, J5}`). **Block-A consumption:** time is
face-local; the next design consumes the clock-twist field as connection data (the
parallel-transport-of-clocks datum), not an emergent global time + lapse `α(m,q)`.

**Through-line:** v24 found the field; v25 its closed form + forced operator; v26 its source +
the MaxEnt theorem; v27 the local balance law; v28 the topological skeleton + the gluing-`U(1)`
class; **v29 closes the global-time question: thermal time is face-local, and the obstruction
is the matter-pinned clock-twist — connection-shaped data for Block A.**

---

## 5. Citations

- A. Connes & C. Rovelli, "Von Neumann algebra automorphisms and time–thermodynamics relation in generally covariant quantum theories," Class. Quantum Grav. **11** (1994) 2899 — thermal time = the modular flow of a state (the literature frame; used as a structural analogy, no thermodynamic postulate enters the verdict).
- A. Connes, *Noncommutative Geometry*, Academic Press (1994); M. Takesaki, Tomita–Takesaki modular theory — the modular generator `K = −log ρ`.
- T. Jacobson, "Entanglement Equilibrium and the Einstein Equation," Phys. Rev. Lett. **116** (2016) 201101 — the joint (J4/J5) structure; here J4 is the per-point thermal-time consistency, tested and found IMPORT-grade (DEAD).
- (Internal) v26 `R_M` (the level-2 `λ₂`-eigenfunction, `derivations/86-*`) — the obstruction is its tangent-valued cousin.
