# Phase 68: (a) Generating-Set Completeness Certificate - Research

**Researched:** 2026-05-27
**Domain:** Computational invariant theory of the exceptional group F_4 = Aut(h_3(O)); bigraded Hilbert/Molien series of the diagonal two-copy ring R[27 ⊕ 27]^{F_4}; plethystic-log generator extraction; minimality testing over Q.
**Confidence:** HIGH on the method structure, weight ingredients, and feasibility budget; MEDIUM on the exact Molien-Weyl normalization tuning (the executor must pass a calibration gate, validated structurally here); HIGH on the frozen-engine cross-check route.

## Summary

This is a **certification** phase, not a derivation phase. Phase 65 fixed the Krull dimension target (10), Phase 65.1 proved field-level (trdeg) completeness of the 10-candidate set, and Phase 67 fixed the bidegree-(1,1) Hilbert coefficient (= 2). Phase 68 must produce the **ring-generation completeness certificate** that 65.1 explicitly deferred: compute the bigraded Hilbert series H(s,t) = Σ dim R[27⊕27]^{F_4}_{(a,b)} sᵃtᵇ for all total degrees a+b ≤ 6, compare it bidegree-by-bidegree against the dimension reachable by products of the candidate generators, and report either "certified complete to degree ≤ 6" or the specific bidegree with a missing generator.

The decisive method question is **how to compute H(s,t) without Sage**. I evaluated three routes and recommend a **two-route certificate**: (PRIMARY) the **Molien-Weyl torus integral evaluated by iterated symbolic residue/constant-term extraction in pure SymPy**, using the F_4 27-weight multiset {zero weight with multiplicity 3, plus the 24 short roots}; and (CORROBORATION, exact-over-Q) the **frozen-f_4-kernel-dimension route** generalizing Phase 67's Route B to every bidegree where it is computationally feasible. The frozen-f_4 route is the *exact-over-Q* anchor (no float on the decisive path) but does NOT scale past roughly a+b ≤ 4 (the (3,3) monomial space is 13.35M-dimensional); the Molien-Weyl route reaches all of a+b ≤ 6 cheaply because its cost depends only on rank 4 and the 24 weights, not on the bidegree-space size. They overlap and cross-check in the low-bidegree window (≤ 4), which is where the genuinely new generators live.

I validated the core structurally: the Weyl-measure constant term CT_z[∏_{48 roots}(1 − z^α)] computes to exactly 1152 = |W(F_4)| (confirming the integrand form and the all-48-roots numerator), and the candidate-free-algebra Hilbert series ∏ 1/(1 − sᵃtᵇ) over the 10 candidate bidegrees reproduces (1,1)-coefficient = 2 (matches Phase 67) and t=0 specialization = 1/((1−s)(1−s²)(1−s³)) exactly (matches the single-copy anchor). The subtle heart of the phase is **distinguishing a missing generator from a syzygy** (the ring is NOT free — that is the E_6 case, Blind 2011, which is the CONTRAST anchor): the plethystic logarithm of H(s,t) gives (generators − relations + ...) per bidegree, so a bidegree where the true dimension exceeds the candidate-product dimension is a missing generator, while a bidegree where products of candidates OVER-shoot signals a relation, not a generator.

**Primary recommendation:** Implement the pure-SymPy **Molien-Weyl iterated-residue** computation of H(s,t) (rank-4 torus, 27-weights = zero³ + 24 short roots, Weyl-measure numerator ∏_{48 roots}(1−z^α), 1/|W| with |W|=1152) as a truncated bivariate power series to total degree 6; CROSS-CHECK every feasible low bidegree (a+b ≤ 4, at minimum (1,1),(2,0),(2,1),(2,2)) against the **exact-over-Q frozen-f_4-kernel dimension** (Phase-67 Route B generalized). Do NOT stage a Sage fixture as the primary — keep the certificate self-contained and exact-corroborated; reserve a one-off Sage `WeylCharacterRing('F4')` multiplicity table only as an optional third independent witness if Molien and f_4-kernel disagree.

## User Constraints

No CONTEXT.md exists for this phase (no `/gpd:discuss-phase` was run). The roadmap Phase-68 entry is the effective contract and carries full scope. There is no formal `project_contract` in state.json for milestone v16.0 — the roadmap phase entry is authoritative (established project pattern). The locked constraints that bound this research:

- **Certification, not derivation.** Polarization is used only to PRODUCE candidate generators; the Hilbert-series match supplies the completeness certificate polarization cannot. Do NOT assume polarization generates the pair ring (this is THE headline forbidden proxy — see Pitfall 1).
- **Exact-over-Q on any decisive path.** No float64, no `numpy.linalg.matrix_rank`, no SVD tolerance on the decisive path. Float is acceptable ONLY for a non-decisive scaffolding/exploration check that is then confirmed exactly.
- **No SageMath / GAP / Singular / Macaulay2 in the executor environment.** SymPy 1.14 + NumPy 2.4 only. Any external data (e.g. a Sage multiplicity table) must be STAGED as a repo fixture by the plan, not fetched at execution time (the executor has no web/arxiv tools).
- **Krull dimension target = 10** (Phase 65: orbit_dim 44, 54 − 44 = 10). The older "54 − orbit = 7" anchor scattered through SUMMARY.md/METHODS.md is SUPERSEDED — it predates the Phase-65 orbit computation and was the Spin(8)-triality TRAP value. Use 10.
- **NEGATIVE-RESULT-IS-SUCCESS.** If a bidegree shows d_true > d_candidate, report the missing generator honestly; do NOT paper over the gap by assuming polarization closes it.
- **Scope decision is the planner's to make explicit IN-PLAN** (not deferred to the executor): pure-SymPy Molien-Weyl residue vs Sage fixture vs frozen-f_4-kernel route. This research recommends the Molien-Weyl + frozen-f_4 two-route combination.

## Active Anchor References

| Anchor / Artifact | Type | Why It Matters Here | Required Action | Where It Must Reappear |
| ----------------- | ---- | ------------------- | --------------- | ---------------------- |
| **Phase 65 orbit_dim = 44 ⇒ Krull dim = 10** | prior artifact (decisive) | The Hilbert series H(s,t) must have a pole structure of order 10 (Krull dim read from the series = 54 − 44 = 10) | USE as the target; read Krull dim from H(s,t) and assert == 10 | plan, execution, verification |
| **Phase 65.1 ten-candidate set, trdeg=10, exact over Q (22/22)** | prior artifact (decisive) | The starting candidate generating set with bidegrees: 6 pointwise + c(1,1) + (2,1)+(1,2)+(2,2). Field-level complete; ring-generation is THIS phase. | USE verbatim as the candidate list; `ring_generating_set.py` builds it | plan, execution |
| **Phase 67 bidegree-(1,1) trivial mult = 2, exact over Q (7/7)** | prior artifact (decisive) | The (1,1) Hilbert coefficient MUST equal 2 = span{Tr(X)Tr(Y), c}. The single most important cross-check of the Hilbert computation. | USE as a mandatory consistency gate on H(s,t); reuse `degree2_uniqueness.py` Route B as the generalizable engine | plan, execution, verification |
| **Single-copy series 1/((1−s)(1−s²)(1−s³))** (Garibaldi-Guralnick / Springer 1962 / Faraut-Korányi) | benchmark | t=0 (and s=0) specialization of H(s,t) MUST reduce to this. THE calibration gate for the Molien-Weyl code. | USE as the Molien-Weyl calibration check BEFORE trusting any two-copy coefficient | execution, verification |
| **Blind 2011 (arXiv:0906.5525): C[27⊕27]^{E_6} is FREE on 4 det-polarizations** | benchmark / CONTRAST (NOT the target) | E_6 = Stab(det); F_4 = Aut also fixes the trace form, so the F_4 pair ring is strictly LARGER (contains c, which is F_4- but not E_6-invariant). The F_4 ring is NOT free. | CITE as the contrast / lower bound; do NOT import the E_6 free-algebra answer | plan (scope), verification |
| **Iltyakov 1998 (J. Algebra 207): F_4 several-copy invariants = trace polynomials + Laplace invariants** | method anchor | Licenses that the F_4 pair generators ARE trace monomials (c, Tr(X²∘Y), etc.) — the candidate set is the right FORM | CITE as the authority that the candidate generators are trace polynomials | plan |
| **Schwarz math/0609078 ("When Polarizations Generate"): 2-polarization fails generically in char 0** | method anchor (THE guard) | The headline forbidden-proxy guard for (a): polarizing single-copy generators need NOT generate the pair ring even in char 0. The Hilbert match is the actual certificate. | CITE as the reason the Hilbert certificate is mandatory; flag in every "completeness" claim | plan, verification |
| **Derksen-Kemper, Computational Invariant Theory (2nd ed. 2015)** | method anchor (canonical) | Molien/Hilbert series for reductive G, the Weyl-integration/CT form, plethystic log, Reynolds redundancy, Jacobian criterion | USE the Molien-Weyl formula (Thm ~4.6.5) and the plethystic-log generator-extraction; CITE as canonical | plan, execution |
| **Hanany et al. "Standard Model Plethystics" arXiv:1902.10550 / "Highest Weight Generating Functions" arXiv:1408.4690** | method anchor (analogue) | The Molien-Weyl + plethystic-log workflow for gauge-rep invariant rings is the exact computational analogue; PE / plog formulas | USE as the plethystic-exponential / plog reference and the practical residue-evaluation recipe | execution |
| **`polarize_d` (frozen engine): d(X,X,X) = 6·det_3** | prior artifact | Produces the polarized mixed-cubic CANDIDATES f(X,X,Y), f(X,Y,Y); these are candidate-producers only (Schwarz guard) | USE to build the polarized-cubic candidates if/when needed at bidegrees (2,1),(1,2) | execution |
| **Frozen engine: `degree2_uniqueness.py` Route B (f_4-kernel nullspace over QQ)** | prior artifact (the exact corroboration engine) | The EXACT-over-Q dimension of invariants at a bidegree = nullspace dim of the stacked f_4-derivation operators. Generalizes from (1,1) to all (a,b). | REUSE and generalize as the exact cross-check engine for low bidegrees | execution, verification |

**Missing or weak anchors:** (i) No source packages the *minimal* F_4 two-copy generating set with a proven completeness certificate — this phase produces it; treat as NOVEL TERRITORY (see below). (ii) The exact normalization of the Molien-Weyl integral (|Δ| vs |Δ|², all-roots vs positive-roots, 1/|W| placement) has competing conventions in the literature; I validated the all-48-roots + 1/|W| form structurally (CT[∏(1−z^α)] = 1152), but the executor MUST pass the single-copy calibration gate before trusting two-copy coefficients. (iii) No literature value exists for the explicit two-copy bigraded dimensions at a+b = 4,5,6 — these are computed here for the first time; the f_4-kernel route (where feasible) and the Molien route must agree, and that agreement IS the validation.

## Conventions

| Choice | Convention | Alternatives | Source |
| ------ | ---------- | ------------ | ------ |
| Group | Compact F_4 = Aut(h_3(O)); complexification F_4(ℂ) reductive | — | Springer-Veldkamp; project frozen |
| Jordan product | jordan(A,B) = (1/2)(AB+BA) | — | frozen engine ASSERT_CONVENTION |
| Coupling | c = Tr(X∘Y) = Tr(jordan(X,Y)); c(X,X) = Tr(X²) (NOT (Tr X)²) | — | `degree2_uniqueness.py` |
| 27 decomposition | 27 = 1 ⊕ 26 (trivial Tr-direction ⊕ trace-free irreducible 26) | — | Phase 67 REP-DECOMP |
| **27 weight multiset (torus)** | **zero weight with multiplicity 3, plus the 24 short roots of F_4** | — | derived here (26 = 24 short roots + zero mult 2; 27 adds one more zero) |
| F_4 short roots (the 26's nonzero weights) | the 24 vectors = all permutations of (±1,±1,0,0), norm² = 2 | the dual 24-cell (±eᵢ, (±½)⁴) are the LONG roots, norm²=1 | Wikipedia F_4; Bourbaki normalization |
| Weyl group order | \|W(F_4)\| = 1152 | — | Wikipedia (symmetry group of the 24-cell); VALIDATED here (CT[∏ roots] = 1152) |
| Krull dim target | 10 (= 54 − orbit_dim 44) | the SUPERSEDED 7 (Spin(8)-triality trap) | Phase 65 |
| Arithmetic | exact SymPy over Q; ranks/nullspaces via `exact_qq_rank` = DomainMatrix-over-QQ | float64 / numpy rank FORBIDDEN on decisive path | frozen engine |
| Generating-function variables | s = X-copy degree marker, t = Y-copy degree marker; H(s,t) bigraded | — | METHODS.md |

**CRITICAL: The 27-weight multiset is the crux ingredient.** det(1 − s·ρ(g)) on one copy = ∏_{weights μ}(1 − s·z^μ) = (1−s)³ · ∏_{μ ∈ 24 short roots}(1 − s·z^μ). The (1−s)³ comes from the zero weight of multiplicity 3 (the trivial 1 contributes one zero weight; the 26 contributes the zero weight with multiplicity 2). The short roots (norm² = 2, perms of (±1,±1,0,0)) are the 26's nonzero weights. Converting from a source that uses the opposite short/long convention requires swapping the 24-root set — but the 26's weights are unambiguously the perms-of-(±1,±1,0,0) set in the rep-theory normalization; VERIFY by the calibration gate.

Convention loading: see agent-infrastructure.md Convention Loading Protocol.

## Mathematical Framework

### Key Equations and Starting Points

| Equation | Name/Description | Source | Role in This Phase |
| -------- | ---------------- | ------ | ------------------ |
| H(s,t) = (1/\|W\|) · CT_z [ ∏_{α∈roots}(1 − z^α) / (D_X(s,z)·D_Y(t,z)) ] | Bigraded Molien-Weyl formula for F_4 on 27_s ⊕ 27_t | Derksen-Kemper ~Thm 4.6.5; Procesi FFT chapter | THE primary computation of H(s,t) |
| D(u,z) = (1−u)³ · ∏_{μ∈24 short roots}(1 − u·z^μ) | One-copy characteristic factor (u = s or t) | derived here from the 27-weight multiset | the integrand denominators D_X(s,z), D_Y(t,z) |
| ∏_{α∈48 roots}(1 − z^α) = \|Δ(z)\|² on the torus | Weyl measure (Vandermonde) numerator | standard | numerator of the Molien-Weyl integrand; CT = 1152 (validated) |
| dim R[27⊕27]^{F_4}_{(a,b)} = dim Sym^a(27)⊗Sym^b(27) − rank(stacked f_4-derivation operators) | f_4-kernel dimension (Route B generalized) | Phase 67 `degree2_uniqueness.py` | EXACT-over-Q cross-check at feasible bidegrees |
| plog H(s,t) = Σ_{k≥1} (μ(k)/k)·log H(sᵏ,tᵏ) | Plethystic logarithm | Hanany et al. 1902.10550; 1408.4690 | reads off (generators − relations) per bidegree from H(s,t) |
| H_free(s,t) = ∏_{gens (a,b)} 1/(1 − sᵃtᵇ) | Free-algebra (no-relations) candidate series | METHODS.md | candidate baseline; differs from true H above the first relation |
| in-span test: value-vector of G_d ∈ span{value-vectors of products of lower gens} over Q | Minimality / SFT-free generator test | PITFALLS Pitfall 8 | proves each generator is genuinely new (not reducible) |

### Required Techniques

| Technique | What It Does | Where Applied | Standard Reference |
| --------- | ------------ | ------------- | ------------------ |
| Molien-Weyl / Weyl integration | Hilbert series of a reductive-group invariant ring as a torus integral | primary H(s,t) computation | Derksen-Kemper §4.6; Procesi |
| Iterated residue / constant-term extraction | Evaluate the rank-4 torus integral as nested 1-variable residues (symbolic) | H(s,t) evaluation in SymPy | Hanany et al.; standard CT methods |
| Plethystic exponential / logarithm | Convert between generators+relations and the Hilbert series | generator/relation extraction | 1902.10550; 1408.4690 |
| f_4-infinitesimal-kernel nullspace (Route B) | Exact dim of invariants at a bidegree = ker dim of derivation operators | exact cross-check (low bidegree) | `degree2_uniqueness.py` (Phase 67) |
| Generic-rational-point value matrices + exact_qq_rank | Minimality (in-span-of-lower-products) and spanning tests over Q | minimality certificate | `ring_generating_set.py` (Phase 65.1) |
| Truncated bivariate power series | Hold H(s,t) to total degree ≤ 6 | every series step | SymPy `series` / `Poly` |

### Approximation Schemes

| Approximation | Small Parameter | Regime of Validity | Error Estimate | Alternatives if Invalid |
| ------------- | --------------- | ------------------ | -------------- | ----------------------- |
| Truncate H(s,t) to total degree ≤ 6 | total degree | sufficient for the contract (degree ≤ 6) | exact within the truncation; NO error inside degree 6 | extend truncation if a generator-degree bound > 6 is suspected (it is not — single-copy gens are degree ≤ 3, mixed ≤ 4) |
| (NONE on the decisive path) | — | the certificate is exact-integer arithmetic | — | — |

**There are no controlled approximations on the decisive path** — every Hilbert coefficient and every rank is an exact integer. The only "truncation" is the harmless degree-≤-6 series cutoff, which is the contract scope.

## Standard Approaches

### Approach 1: Molien-Weyl iterated residue (pure SymPy) + frozen-f_4-kernel cross-check (RECOMMENDED — TWO-ROUTE)

**What:** Compute H(s,t) for all a+b ≤ 6 by evaluating the bigraded Molien-Weyl torus integral symbolically (iterated residue / constant-term over the 4 torus variables), using the F_4 27-weight multiset. Independently confirm the low-bidegree coefficients (where feasible) by the exact-over-Q f_4-kernel-dimension route generalized from Phase 67.

**Why standard:** Molien-Weyl is THE canonical method for Hilbert series of reductive-group invariant rings (Derksen-Kemper); the plethystic workflow is industry-standard in the physics invariant-ring literature (Hanany et al.). The f_4-kernel route is the project's own certified exact engine (Phase 67 passed 7/7 with it).

**Track record:** The single-copy specialization is a known closed form (validated structurally here); the (1,1) coefficient is independently pinned at 2 by Phase 67. The two routes provide the reward-hacking-resistant independent confirmation the project demands.

**Key steps:**

1. **Build the F_4 ingredients (data, exact):** the 48 roots (24 short = perms of (±1,±1,0,0); 24 long = ±eᵢ and (±½)⁴), |W| = 1152, and the 27-weight multiset = {zero × 3} ∪ {24 short roots}. These are exact rational vectors — no algebra engine needed.
2. **Assemble the integrand:** numerator N(z) = ∏_{α∈48 roots}(1 − z^α); denominator D_X(s,z)·D_Y(t,z) with D(u,z) = (1−u)³·∏_{μ∈24 short}(1 − u·z^μ). Clear the half-integer powers (from the (±½)⁴ long roots) by substituting z_i = w_i² so all exponents are integers.
3. **Extract the constant term by iterated residue:** for each torus variable in turn, expand 1/D as a power series in (s,t) to total degree 6, then take the z_i⁰ Laurent coefficient via SymPy `Poly` coefficient extraction (or `residue`/`apart` per variable). Result: H(s,t) as a truncated bivariate polynomial Σ d_{a,b} sᵃtᵇ, a+b ≤ 6.
4. **CALIBRATION GATE (mandatory, before trusting two-copy):** set t = 0 and confirm H(s,0) = 1/((1−s)(1−s²)(1−s³)) coefficient-by-coefficient = [1,1,2,3,4,5,6,...] through s⁶. Set s = 0 symmetrically. If this fails, the weight set or normalization is wrong — fix before proceeding (do NOT report any two-copy number until this passes).
5. **(1,1) GATE:** confirm d_{1,1} = 2 (matches Phase 67). If not, the integrand is wrong.
6. **Exact cross-check (Route B generalized):** for each bidegree with a+b ≤ 4 (at minimum (1,1),(2,0),(0,2),(2,1),(1,2),(2,2),(3,0)): build the f_4-derivation operators on Sym^a(27)⊗Sym^b(27) (Leibniz lift ρ(M) acting on the symmetric-power monomial basis), and compute d_{a,b} = dim(space) − exact_qq_rank(stacked operators) over QQ. This MUST equal the Molien coefficient. This is the exact-over-Q decisive anchor.
7. **Krull-dim read-off:** the order of the pole of H(s,t) at s=t=1 (equivalently the degree of the denominator after writing H as a rational function) = Krull dim; assert == 10 (Phase 65). Equivalently confirm the leading growth of d_{a,b} matches a dimension-10 ring.
8. **Candidate-match + plethystic log:** compute H_free(s,t) = ∏ 1/(1 − sᵃtᵇ) over the candidate bidegrees; compute plog H(s,t) = Σ_k (μ(k)/k) log H(sᵏ,tᵏ); read off the generator count (positive plog coefficients at low degree) and the first relation (first negative plog coefficient). At each bidegree compare d_true (Molien) against d_candidate (dimension reachable by products of candidate generators — computed exactly via the value-matrix rank, step 9). d_true > d_candidate ⇒ missing generator at that bidegree.
9. **Minimality (in-span-of-lower-products):** for each candidate generator G at bidegree (a,b), evaluate G and ALL products of strictly-lower-degree candidates landing at (a,b) at ≥ (enough) generic rational octonionic points (reuse `PAIR_POINTS`); build the value matrix; check via exact_qq_rank that G's value-vector is NOT in the span of the lower-product value-vectors. Genuinely-new ⇒ minimal.
10. **Verdict:** state honestly — certified complete to total degree ≤ 6 (with explicit note polarization was NOT assumed; the Hilbert match is the certificate), OR the specific bidegree with a missing generator (add the lowest-degree trace monomial there, re-match — backtracking per roadmap).

**Known difficulties at each step:**

- Step 3: **dense numerical torus-grid CT extraction is INFEASIBLE in pure Python** (validated: even order-2 single-copy at a sufficient grid n=13 times out; the (3,3) space is irrelevant to Molien but the grid must cover the full Laurent support of ∏ over 48 roots, demanding n > ~13, i.e. > 28k grid points × heavy products). MUST use SYMBOLIC iterated residue (partial fractions / `Poly` coefficient extraction per variable), which is exact and grid-free. A numeric grid would also be a forbidden float path on the decisive route.
- Step 3: the half-integer exponents (from (±½)⁴ roots) require the z_i = w_i² doubling substitution, or working over a cyclotomic field; handle before any coefficient extraction.
- Step 6: the f_4-kernel route does NOT scale — dim Sym^a(27)⊗Sym^b(27) reaches 13.35M at (3,3) and 142,884 at (2,2). Feasible cleanly to about a+b ≤ 3, strained at (2,2) (142,884-dim space × 52 operators). Use it as the exact anchor where it fits; do NOT attempt it at a+b ≥ 5.
- Step 8: **distinguishing missing-generator from syzygy is the subtle heart** (Pitfall 8). The ring is NOT free, so H_free ≠ H_true above the first relation. The plog disentangles them: positive coefficient = generator, negative = relation. d_true > d_candidate is a missing generator; d_candidate-products > d_true is a relation (the candidates satisfy a syzygy, NOT a missing generator).

### Approach 2: Stage a one-off Sage `WeylCharacterRing('F4')` multiplicity fixture (FALLBACK / OPTIONAL THIRD WITNESS)

**What:** On a machine with Sage, compute the bigraded multiplicity of the trivial rep in Sym^a(27) ⊗ Sym^b(27) for all a+b ≤ 6, and stage the resulting integer table as a repo data fixture.

```python
# One-off Sage script (NOT run by the executor; produces a static fixture table):
from sage.all import WeylCharacterRing
F4 = WeylCharacterRing("F4", style="coroots")
# 27 = trivial(1) + 26(fundamental, highest weight (0,0,0,1) in coroots):
rep27 = F4(0,0,0,0) + F4(0,0,0,1)        # 1 + 26 = 27
def sym_power(chi, n):
    # symmetric power character via Adams/Newton or built-in symmetric_power
    return chi.symmetric_power(n)
table = {}
for a in range(7):
    for b in range(7-a):
        prod = sym_power(rep27, a) * sym_power(rep27, b)
        table[(a,b)] = prod.multiplicity(F4(0,0,0,0))   # dim of invariants
# write table to JSON fixture; commit to repo
```

**When to switch:** Use ONLY as an optional independent third witness (if Molien and the f_4-kernel route disagree and the disagreement cannot be localized). Do NOT make it the primary — it breaks self-containment (requires staging) and is not exact-over-Q in the project's sense (it is exact-integer rep theory, fine, but it is an external import, not an in-environment proof). If staged, the plan MUST keep the in-environment Molien + f_4-kernel checks as the actual certificate.

**Tradeoffs:** Gains: trivially correct rep-theory multiplicities, cheap in Sage. Loses: self-containment (executor can't reproduce it), and it is a third route only — the contract wants an in-environment certificate.

### Anti-Patterns to Avoid

- **Assuming polarization generates the pair ring** (THE headline forbidden proxy): "we polarized the cubic norm, so we have all generators." FALSE in char 0 (Schwarz: 2-polarization fails generically). The Hilbert match is the certificate; polarization only PRODUCES candidates.
  - _Example:_ stopping after building f(X,X,Y), f(X,Y,Y) and declaring completeness without the Molien match.
- **Importing the E_6 free-algebra answer for F_4** (Blind 2011 is the CONTRAST, not the target): the F_4 ring is strictly larger (contains c) and is NOT free.
  - _Example:_ assuming H(s,t) has a clean product denominator ∏ 1/(1−sᵃtᵇ) — that is the free-algebra form, wrong for the non-free F_4 ring.
- **Conflating spanning with minimal generating** (Pitfall 8): a Reynolds-projection spanning set is redundant by design; "minimal generating" requires the in-span-of-lower-products test.
  - _Example:_ listing Tr(X²∘Y²) as a generator at (2,2) without checking it isn't a product (c², c·Tr(X)Tr(Y), Tr(X²)Tr(Y²), (2,1)·(0,1), (1,2)·(1,0), ...).
- **Using float64 / numpy rank on the decisive path:** fabricates the dimension verdict. Exact-over-Q only.
- **Using the SUPERSEDED Krull-dim target 7:** the orbit-derived target is 10 (Phase 65). The 7 was the Spin(8)-triality trap.
- **Dense numerical torus grid for the CT:** infeasible AND float. Symbolic iterated residue only.

## Existing Results to Leverage

### Established Results (DO NOT RE-DERIVE)

| Result | Exact Form | Source | How to Use |
| ------ | ---------- | ------ | ---------- |
| Single-copy F_4 invariant ring is free on degrees 1,2,3 | R[27]^{F_4} = R[Tr, Tr², det]; Hilbert series 1/((1−s)(1−s²)(1−s³)) | Springer 1962; Faraut-Korányi Ch.V; Garibaldi-Guralnick | t=0 specialization gate; do NOT re-derive single-copy generation |
| F_4 root system | 48 roots: 24 short = perms(±1,±1,0,0); 24 long = ±eᵢ, (±½)⁴; \|W\| = 1152 | Bourbaki; Wikipedia F_4; VALIDATED here | build the Molien integrand directly from these |
| 27-weight multiset | {0 with mult 3} ∪ {24 short roots} | derived here (26 = 24 short + 0·mult2; 27 = +1 more 0) | THE crux ingredient for D(u,z) |
| dim f_4 = 52, the 52-generator basis, exact over Q | `inner_derivations()` span rank 52 | `orbit_dimension_gate.py` (Phase 65) | reuse for the f_4-kernel route; do NOT rebuild f_4 |
| Krull dim of the pair ring = 10 | 54 − orbit_dim(44) = 10 | Phase 65 (computed, triple-confirmed) | the target the Hilbert-series pole order must match |
| trdeg-10 candidate set, exact Jacobian rank 10 over Q | {Tr X, Tr X², det X, Tr Y, Tr Y², det Y, c, Tr(X²∘Y), Tr(X∘Y²), Tr(X²∘Y²)} | Phase 65.1 `ring_generating_set.py` | the candidate generating list (with bidegrees) — verbatim |
| bidegree-(1,1) trivial mult = 2, exact over Q | span{Tr(X)Tr(Y), c}; quotient mod products = 1 | Phase 67 `degree2_uniqueness.py` | mandatory (1,1) Hilbert-coefficient gate |
| Molien-Weyl Weyl-measure CT = \|W\| | CT_z[∏_{48 roots}(1−z^α)] = 1152 | VALIDATED here (n=13 grid) | confirms the integrand numerator + 1/\|W\| normalization |

**Key insight:** The dangerous re-derivation here is the **integrand normalization** of the Molien-Weyl formula — there are competing conventions (|Δ| vs |Δ|², positive-roots vs all-roots, where 1/|W| sits). Do NOT trust a hand-derived integrand; pin it by the single-copy calibration gate (t=0 ⇒ 1/((1−s)(1−s²)(1−s³))) and the (1,1)=2 gate BEFORE reporting any new coefficient. The all-48-roots numerator + 1/1152 form is validated structurally here (CT = 1152).

### Useful Intermediate Results

| Result | What It Gives You | Source | Conditions |
| ------ | ----------------- | ------ | ---------- |
| Candidate-free-algebra series ∏ 1/(1−sᵃtᵇ) | Baseline H_free; (1,1)=2, t=0 → single-copy series (both VALIDATED here) | computed here | the candidate set is NOT free, so H_free over-counts above the first relation |
| (2,2) free-algebra coefficient = 9 | The key diagnostic bidegree for the "(2,2) generator or product?" question | computed here | compare against d_true(2,2) from Molien/f_4-kernel |
| Sym^a(27) dimensions = C(26+a, a) | The f_4-kernel route space sizes (budget) | computed here | (0,0,1,378,3654,27405,...) → (3,3) product = 13.35M |
| polarize_d: d(X,X,X) = 6·det_3 | Polarized mixed-cubic candidate producer | frozen engine | produces (2,1),(1,2) candidates; candidate-only (Schwarz guard) |

### Relevant Prior Work

| Paper/Result | Authors | Year | Relevance | What to Extract |
| ------------ | ------- | ---- | --------- | --------------- |
| C[27⊕27]^{E_6} free on 4 det-polarizations | Blind | 2011 | CONTRAST (NOT target); F_4 ring is larger | the free-algebra structure E_6 has but F_4 lacks; lower bound |
| F_4 several-copy invariants = trace polys + Laplace | Iltyakov | 1998 | the candidate generators ARE trace monomials | licenses the candidate FORM (c, Tr(X²∘Y), ...) |
| "When Polarizations Generate" | Schwarz | 2006/07 | 2-polarization fails generically in char 0 | THE guard: Hilbert match is mandatory, polarization is not enough |
| Computational Invariant Theory (2nd ed.) | Derksen-Kemper | 2015 | Molien-Weyl formula, plog, Reynolds redundancy | the canonical formula and the generator-extraction method |
| Standard Model Plethystics / Highest Weight Generating Functions | Hanany et al. | 2014/19 | the Molien-Weyl + plog workflow analogue | practical residue evaluation, PE/plog formulas |

## Computational Tools

### Core Tools

| Tool | Version/Module | Purpose | Why Standard |
| ---- | -------------- | ------- | ------------ |
| SymPy | 1.14 — `Poly`, `series`, `apart`, `residue`, `Rational`, `binomial`, `mobius` | Molien-Weyl symbolic residue, plog, all exact series | the only symbolic CAS in-environment; exact over Q |
| SymPy | `sympy.polys.matrices.DomainMatrix` over `QQ` | `exact_qq_rank` — exact nullspace/rank for the f_4-kernel route and minimality | exact integer ranks; the project's certified rank tool |
| Frozen engine | `embedding_under_E_verification.py` | jordan, Tr, Tr2, c, det_3, polarize_d, 54 symbols, octonionic points | THE exact base; never re-derive |
| Frozen engine | `orbit_dimension_gate.py` | `inner_derivations()` (52-gen f_4 basis), `exact_qq_rank` | f_4 for the kernel route; never rebuild |
| Frozen engine | `degree2_uniqueness.py` | Route B Leibniz-lift kernel machinery (the (1,1) engine to generalize) | the exact-over-Q cross-check engine |
| Frozen engine | `ring_generating_set.py` | the 10-candidate list, bidegrees, PAIR_POINTS, value-matrix rank | candidate generators + minimality scaffolding |

### Supporting Tools

| Tool | Purpose | When to Use |
| ---- | ------- | ----------- |
| SymPy `mobius` (number theory) | Möbius μ(k) for the plethystic log Σ (μ(k)/k) log H(sᵏ,tᵏ) | the plog generator/relation extraction |
| NumPy / mpmath | float exploration ONLY (e.g. quick grid sanity) | NEVER on the decisive path; scratch only, then confirm exactly |

### Alternatives Considered

| Instead of | Could Use | Tradeoff |
| ---------- | --------- | -------- |
| Pure-SymPy Molien residue | Sage `WeylCharacterRing('F4').symmetric_power` | Sage trivially correct but breaks self-containment (must stage fixture); keep as optional 3rd witness only |
| f_4-kernel exact route at all bidegrees | f_4-kernel only at a+b ≤ 4 | the route does not scale ((3,3) = 13.35M-dim); Molien covers 5,6 |
| Symbolic iterated residue | Dense numerical torus grid | grid is INFEASIBLE in pure Python (validated timeout) AND a forbidden float path |

### Computational Feasibility

| Computation | Estimated Cost | Bottleneck | Mitigation |
| ----------- | -------------- | ---------- | ---------- |
| Molien-Weyl symbolic residue, H(s,t) to deg 6 | minutes (rank-4 torus, 48-root numerator, 24-weight denominators) | the 4-fold iterated residue × bivariate series truncation | truncate to total deg 6 first; iterate residues one torus var at a time; cost is INDEPENDENT of bidegree-space size |
| f_4-kernel dim at (1,1) | seconds (729-dim, done in Phase 67) | — | reuse Phase 67 verbatim |
| f_4-kernel dim at (2,1),(1,2) | minutes (10,206-dim space × 52 ops) | building the Leibniz lift on the symmetric-power basis | feasible; chunk output (`python -u`) |
| f_4-kernel dim at (2,2) | HEAVY (142,884-dim × 52 ops, exact QQ rank) | exact_qq_rank on a ~7.4M-row stacked matrix | feasible only with sparse/structured rank; consider deferring (2,2) to Molien + Sage witness, or exploit irrep block structure |
| f_4-kernel dim at a+b ≥ 5 | INFEASIBLE | dim Sym ≥ 170k–13.35M | do NOT attempt; Molien covers these |
| Minimality value-matrix ranks | seconds-minutes per bidegree | building all lower-degree products | reuse PAIR_POINTS; exact_qq_rank |

**Budget table (dim Sym^a(27)·Sym^b(27), the f_4-kernel space size per bidegree):**

```
(a+b)  bidegrees (dim)
  0    (0,0):1
  1    (0,1)/(1,0):27
  2    (0,2)/(2,0):378    (1,1):729
  3    (0,3)/(3,0):3,654  (1,2)/(2,1):10,206
  4    (0,4)/(4,0):27,405 (1,3)/(3,1):98,658  (2,2):142,884
  5    (0,5)/(5,0):169,911 (1,4)/(4,1):739,935 (2,3)/(3,2):1,381,212
  6    (0,6)/(6,0):906,192 (1,5)/(5,1):4,587,597 (2,4)/(4,2):10,359,090 (3,3):13,351,716
```

f_4-kernel route: clean to a+b ≤ 3; (2,2) is the boundary (heavy but maybe feasible with structure); a+b ≥ 5 infeasible — Molien only.

**Installation / Setup:**
```bash
# Nothing to install in the executor environment — SymPy 1.14 + the frozen engine suffice.
# Optional THIRD-witness fixture (run ONCE on a Sage machine, NOT the executor):
#   sage -python produce_f4_multiplicity_table.py  # writes a JSON fixture to the repo
```

## Validation Strategies

### Internal Consistency Checks

| Check | What It Validates | How to Perform | Expected Result |
| ----- | ----------------- | -------------- | --------------- |
| t=0 (and s=0) specialization | the Molien-Weyl integrand normalization + weight set | set t=0 in H(s,t) | 1/((1−s)(1−s²)(1−s³)) = [1,1,2,3,4,5,6] through s⁶ |
| Weyl-measure CT | the numerator + 1/\|W\| | CT_z[∏_{48 roots}(1−z^α)] | exactly 1152 (VALIDATED here) |
| (1,1) coefficient | the whole bigraded machinery against Phase 67 | read d_{1,1} from H(s,t) | exactly 2 |
| Molien vs f_4-kernel (a+b ≤ 4) | the two independent routes agree | compare d_{a,b} | identical integers at every cross-checked bidegree |
| Krull dim from pole order | against Phase 65 | order of pole of H(s,t) at s=t=1 | exactly 10 |
| symmetry H(s,t) = H(t,s) | the X↔Y swap symmetry of the diagonal action | inspect coefficients | d_{a,b} = d_{b,a} for all a,b |

### Known Limits and Benchmarks

| Limit | Parameter Regime | Known Result | Source |
| ----- | ---------------- | ------------ | ------ |
| Single copy (Y absent) | t = 0 | 1/((1−s)(1−s²)(1−s³)) | Springer 1962 / Faraut-Korányi |
| Single copy (X absent) | s = 0 | 1/((1−t)(1−t²)(1−t³)) | same (by symmetry) |
| Degree-2 sector | (a,b) ∈ {(2,0),(1,1),(0,2)} | dims 2, 2, 2 (total 6) | Phase 67 / METHODS (c) |
| Krull dimension | growth of d_{a,b} | dimension-10 ring | Phase 65 |
| E_6 contrast (NOT a match) | — | E_6 pair ring free on 4 dets | Blind 2011 — F_4 must DIFFER (larger) |

### Numerical Validation

| Test | Method | Tolerance | Reference Value |
| ---- | ------ | --------- | --------------- |
| All Hilbert coefficients | exact integer (SymPy Rational / Poly) | EXACT — no tolerance | integers; any non-integer = bug |
| All ranks/nullspaces | exact_qq_rank over QQ | EXACT | integers |
| (Float grid scratch only) | mpmath, non-decisive | n/a | discard; confirm exactly |

### Red Flags During Computation

- Any non-integer Hilbert coefficient → the residue extraction or normalization is wrong.
- t=0 specialization ≠ 1/((1−s)(1−s²)(1−s³)) → wrong weight set or normalization; STOP and fix (do not report two-copy numbers).
- d_{1,1} ≠ 2 → contradicts Phase 67; integrand is wrong.
- Molien and f_4-kernel disagree at any cross-checked bidegree → at least one route is wrong; localize before proceeding (this is the reward-hacking tripwire).
- H(s,t) ≠ H(t,s) → the X↔Y symmetry is broken; bug in the integrand.
- Pole order ≠ 10 at s=t=1 → wrong Krull dim; contradicts Phase 65.
- A "generator" at a bidegree whose dimension is already fully accounted for by products of lower generators → it is a product, not a generator (Pitfall 8).
- plog has a POSITIVE coefficient at a bidegree NOT in the candidate set → a genuinely missing generator there (the NEGATIVE-result-is-success outcome — report it).

## Common Pitfalls

### Pitfall 1: Assuming polarization generates the pair ring (THE headline forbidden proxy)

**What goes wrong:** Treating "we polarized the cubic norm to get f(X,X,Y), f(X,Y,Y)" as proof of a complete generating set.
**Why it happens:** METHODS.md's executive line leans toward "polarization generates in char 0" — but that is Weyl's theorem, which needs dim-V = 27 COPIES, not the single-copy "2-polarization property." The 2-polarization property fails generically even in char 0 (Schwarz math/0609078; PITFALLS Pitfall 1).
**How to avoid:** The bigraded Hilbert-series match IS the certificate. Polarization only PRODUCES candidates. State explicitly in the verdict that polarization was NOT assumed to generate.
**Warning signs:** any "completeness" claim that does not cite the degree-by-degree Hilbert match.
**Recovery:** run the Molien match; at the first d_true > d_candidate, find and add the missing generator.

### Pitfall 2: Conflating spanning with minimal generating; ignoring syzygies (Pitfall 8)

**What goes wrong:** Listing a redundant generator (a product of lower ones) as "new," or missing a generator hidden behind a relation. The ring is NOT free, so H_free(s,t) ≠ H_true(s,t) above the first relation.
**Why it happens:** Reynolds projection gives a redundant spanning set; "minimal generating" requires knowing the relations (SFT). H_free over-counts.
**How to avoid:** plethystic log of H_true gives (generators − relations) per bidegree. d_true > d_candidate-products = missing generator; candidate-products over-shoot d_true = relation. Run the in-span-of-lower-products minimality test for each generator.
**Warning signs:** assuming a clean product denominator ∏ 1/(1−sᵃtᵇ) for H_true (that is the free/E_6 form).
**Recovery:** use plog to separate generators from relations; never claim "minimal" without the in-span test.

### Pitfall 3: Wrong Krull-dimension target (the superseded 7)

**What goes wrong:** Targeting Krull dim 7 (the Spin(8)-triality back-of-envelope = naive "6 pointwise + c" count).
**Why it happens:** SUMMARY.md/METHODS.md were written before Phase 65 computed orbit_dim = 44; they carry the stale "54 − orbit = 7" anchor throughout.
**How to avoid:** Krull dim = 54 − 44 = 10 (Phase 65, triple-confirmed). The Hilbert-series pole order must be 10.
**Warning signs:** a Hilbert series whose pole order at s=t=1 is 7 — that would mean the orbit/stabilizer is wrong.
**Recovery:** re-read Phase 65 GATE; the target is 10.

### Pitfall 4: Importing the E_6 free-algebra answer for F_4

**What goes wrong:** Assuming H(s,t) has a free-algebra (clean product) form because Blind 2011 says the E_6 pair ring is free on 4 dets.
**Why it happens:** E_6 = Stab(det) and F_4 = Aut are both relevant to h_3(O); easy to conflate.
**How to avoid:** F_4 also fixes the trace form, so the F_4 pair ring is strictly LARGER (contains c, which is F_4- but not E_6-invariant) and is NOT free. Blind is the CONTRAST anchor.
**Warning signs:** expecting exactly 4 generators or a free Hilbert series.
**Recovery:** the F_4 ring has c plus mixed trace monomials; expect relations (non-free).

### Pitfall 5: Dense numerical torus grid for the constant term (float + infeasible)

**What goes wrong:** Evaluating the Molien-Weyl CT by averaging the integrand over a product grid of roots of unity.
**Why it happens:** It is the "obvious" way to extract a constant term and looks simple.
**How to avoid:** It is INFEASIBLE in pure Python (validated: even order-2 single-copy at the required grid n≥13 times out — the ∏ over 48 roots has Laurent support up to degree ~48 in the doubled lattice, forcing a fine grid). And it is a FLOAT path — forbidden on the decisive route. Use SYMBOLIC iterated residue (`Poly` coefficient extraction / `apart` per torus variable) — exact and grid-free.
**Warning signs:** importing mpmath/numpy on the H(s,t) path; runtimes blowing up.
**Recovery:** rewrite as symbolic iterated residue over Q.

### Pitfall 6: Float64 / numpy rank on the decisive path

**What goes wrong:** Using `numpy.linalg.matrix_rank` or SVD tolerance for the f_4-kernel nullspace or the minimality value-matrix rank.
**Why it happens:** numpy rank is fast and tempting.
**How to avoid:** exact_qq_rank (DomainMatrix over QQ) only. Float rank fabricates dimension verdicts (this is the GLOBAL forbidden proxy).
**Warning signs:** any tolerance parameter on a decisive rank.
**Recovery:** switch to exact_qq_rank; re-run.

## Level of Rigor

**Required for this phase:** Exact-arithmetic computational certificate (the project's standard) — every decisive Hilbert coefficient and every rank/nullspace is an exact integer over Q, cross-confirmed by two independent routes in the bidegree window where both are feasible.

**Justification:** This is the capstone proof phase of the (RING) lemma's sub-claim (a). The reward-hacking guard demands independent confirmation and forbids float on decisive paths. The contract is finite (degree ≤ 6) and the arithmetic is exact-integer, so a genuine certificate (not "numerical evidence") is achievable and required.

**What this means concretely:**
- The Molien-Weyl series must pass BOTH calibration gates (single-copy specialization AND (1,1)=2) before any new coefficient is reported.
- Every cross-checkable bidegree (a+b ≤ 4) must show Molien = f_4-kernel as identical exact integers.
- Minimality is proven by the in-span-of-lower-products exact_qq_rank test for each generator (not asserted).
- The completeness verdict is stated honestly per the NEGATIVE-result-is-success rule — a missing generator at a bidegree is a valid, must-report outcome.
- The Krull-dim read-off must equal 10 (Phase 65) and the (1,1) coefficient must equal 2 (Phase 67) — these are non-negotiable consistency anchors.

## State of the Art

| Old Approach | Current Approach | When Changed | Impact |
| ------------ | ---------------- | ------------ | ------ |
| "Polarization generates in char 0" (METHODS.md executive line) | Hilbert-series certificate; 2-polarization fails generically (Schwarz) | resolved in PITFALLS Pitfall 1 / SUMMARY Reconciliation 1 | (a) is a certification obligation, not a polarization hand-wave |
| Krull-dim target = 7 (Spin(8)-triality) | Krull-dim = 10 (Phase 65 orbit_dim 44) | Phase 65 | the candidate set needs the 3 mixed joint invariants beyond {6 pointwise + c} |
| Field-level (trdeg) completeness (Phase 65.1) | Ring-generation completeness via Hilbert series (THIS phase) | Phase 68 | trdeg 10 does NOT imply ring generation; the Hilbert match is the upgrade |

**Superseded approaches to avoid:**
- The "54 − orbit = 7" anchor (pre-Phase-65): now 10. Appears throughout SUMMARY.md/METHODS.md — do not use.
- "Polarization suffices in char 0" as a completeness argument: superseded by the Schwarz guard and the Hilbert certificate.

## Open Questions

1. **Exact Molien-Weyl normalization (|Δ| vs |Δ|², 1/|W| placement)**
   - What we know: the all-48-roots numerator ∏(1−z^α) with 1/|W| gives CT = 1152 = |W| (validated); this is the Derksen-Kemper / standard form.
   - What's unclear: whether the iterated-residue implementation reproduces the single-copy series exactly without a residual normalization factor (competing conventions exist).
   - Impact on this phase: medium — it is fully resolved by the mandatory calibration gate (t=0 ⇒ single-copy series). The executor must pass the gate before trusting two-copy numbers.
   - Recommendation: implement, then GATE on t=0 and (1,1)=2; if the gate fails, adjust normalization (most likely a |Δ| vs |Δ|² or a per-variable residue-sign issue) and re-gate.

2. **Feasibility of the f_4-kernel cross-check at (2,2)**
   - What we know: the (2,2) space is 142,884-dimensional; exact_qq_rank on a ~7.4M-row stacked matrix is heavy.
   - What's unclear: whether it completes within the executor's runtime/watchdog (~600s) limits.
   - Impact: (2,2) is the key "(2,2) generator or product?" diagnostic bidegree; losing the exact cross-check there weakens the certificate at that bidegree.
   - Recommendation: attempt (2,2) with structured/sparse rank or irrep-block reduction; if infeasible, rely on Molien there with the optional Sage witness, and lean on the exact f_4-kernel at (1,1),(2,0),(2,1),(1,2) for the reward-hacking anchor. Chunk output / `python -u` to avoid the stream-watchdog stall.

3. **Whether Tr(X²∘Y²) at (2,2) is a generator or a product**
   - What we know: it is in the Phase-65.1 trdeg-10 set (needed for FIELD completeness), but field-completeness ≠ ring generation.
   - What's unclear: whether at the RING level it is expressible via products {c², c·Tr(X)Tr(Y), Tr(X²)Tr(Y²), (2,1)·(0,1), (1,2)·(1,0), ...}.
   - Impact: decides the minimal generating set at (2,2).
   - Recommendation: the d_true(2,2) vs candidate-product-dimension comparison + the in-span minimality test decides it. Report the outcome honestly either way.

## Alternative Approaches if Primary Fails

| If This Fails | Because Of | Switch To | Cost of Switching |
| ------------- | ---------- | --------- | ----------------- |
| Molien-Weyl symbolic residue | normalization can't be pinned / SymPy residue too slow | Sage `WeylCharacterRing('F4')` fixture (staged) + f_4-kernel for ≤ 4 | low (one-off Sage run); breaks self-containment — keep f_4-kernel as the in-environment anchor |
| f_4-kernel at (2,2) | space too large for exact_qq_rank | Molien coefficient at (2,2) + Sage witness | low; lose one exact cross-check bidegree |
| Both Molien AND f_4-kernel at high bidegree | infeasibility | restrict the EXACT certificate to a+b ≤ 4 (where both agree) + Molien (corroborated by Sage) for 5,6 | low; the genuinely-new generators all live at degree ≤ 4 (single-copy ≤ 3, mixed ≤ 4), so degree 5,6 only checks for surprise generators |

**Decision criteria:** If the single-copy calibration gate cannot be passed after reasonable normalization adjustment, abandon the pure-SymPy Molien residue and stage the Sage fixture (with the f_4-kernel as the in-environment exact anchor for a+b ≤ 4). If the f_4-kernel route exceeds runtime at a bidegree, cap it there and use Molien (+ optional Sage) for that bidegree, keeping the exact cross-check at every bidegree where it fits.

## Caveats and Alternatives (Pre-Submission Self-Critique)

1. **What assumption might be wrong?** That the 27's nonzero weights are the norm²=2 (perms of (±1,±1,0,0)) short-root set. Sources disagree on the short/long label (Wikipedia vs Grokipedia swap them). I mitigated this by validating CT[∏ roots] = |W| (convention-independent) and by making the single-copy calibration gate mandatory — if the weight set is wrong, the gate fails loudly. The weight MULTISET (24 + zero³), not the label, is what matters.
2. **What did I dismiss too quickly?** The dense numerical torus grid — but I validated it is infeasible (timeout) AND float-forbidden, so dismissal is justified. I also did not fully nail the iterated-residue normalization (left to the executor behind the gate); a deeper dive could pin it, but the gate makes that safe.
3. **What limitation am I understating?** The f_4-kernel cross-check at (2,2) may not complete in the executor's runtime — I flag this as Open Question 2. If it fails, the exact two-route anchor is restricted to a+b ≤ ~3, and (2,2) leans on Molien + the optional Sage witness, which is weaker (Sage breaks self-containment).
4. **Simpler method overlooked?** The Sage fixture IS simpler — but it breaks self-containment and is not an in-environment proof. The roadmap explicitly wants the scope decision made in-plan and prefers self-containment; the f_4-kernel route is the project's own certified style. I recommend Molien (self-contained, all degrees) + f_4-kernel (exact anchor, low degrees), with Sage as optional 3rd witness.
5. **Would a specialist disagree?** An invariant theorist might say "just use the Molien-Weyl formula, it's textbook." True — but the *implementation* in pure SymPy without Sage's `WeylCharacterRing` is the real work, and the normalization conventions are a genuine trap. A specialist would endorse the calibration-gate discipline. They might also push for the plethystic log as the primary generator-extraction tool (rather than the d_true-vs-d_candidate comparison) — I include both; the plog is cleaner for separating generators from relations and should lead.

## Sources

### Primary (HIGH confidence)
- **Derksen, H.; Kemper, G.** *Computational Invariant Theory*, 2nd ed., Springer (2015). — Molien-Weyl formula for reductive G (Weyl-integration/CT form, ~Thm 4.6.5), plethystic log, Reynolds redundancy, Jacobian criterion. [canonical]
- **Springer, T. A.** "Characterization of a class of cubic forms," Indag. Math. 24 (1962). — single-copy F_4 invariant ring = R[Tr, Tr², det]; the t=0 series anchor.
- **Faraut, J.; Korányi, A.** *Analysis on Symmetric Cones*, Oxford 1994, Ch. V. — Jordan trace/norm; single-state ring.
- **Schwarz, G. W.** "When Polarizations Generate," arXiv:math/0609078; Transform. Groups 12 (2007). — 2-polarization fails generically in char 0. THE guard for (a). [text extracted in PITFALLS]
- **Frozen engine modules** (project, certified): `embedding_under_E_verification.py`, `orbit_dimension_gate.py` (Phase 65, dim f_4 = 52, orbit 44), `ring_generating_set.py` (Phase 65.1, trdeg 10), `degree2_uniqueness.py` (Phase 67, (1,1) = 2). [verified by inspection + prior verification 22/22, 7/7]
- **Project research** `.gpd/research/{SUMMARY,METHODS,PITFALLS,PRIOR-WORK,COMPUTATIONAL}.md`. — Reconciliation 1 (do not assume polarization generates), Pitfall 1 (Weyl-vs-k-polarization), Pitfall 8 (spanning vs minimal generating). [project canon]
- **In-session validations** (this research): CT_z[∏_{48 F_4 roots}(1−z^α)] = 1152 = |W| (n=13 grid); candidate-free-algebra series ∏ 1/(1−sᵃtᵇ) gives (1,1)=2 and t=0 → 1/((1−s)(1−s²)(1−s³)) exactly; dense torus-grid CT infeasible in pure Python (timeout). [computed here, exact/reproducible]

### Secondary (MEDIUM confidence)
- **Blind, B.** "Algèbres de Jordan et théorie des invariants," J. Lie Theory 21 (2011), arXiv:0906.5525. — C[27⊕27]^{E_6} free on 4 det-polarizations. CONTRAST anchor. [verified in PRIOR-WORK]
- **Iltyakov, A. V.** J. Algebra 207 (1998). — F_4 several-copy invariants = trace polynomials + Laplace invariants. [via PRIOR-WORK]
- **Hanany et al.** "Standard Model Plethystics" arXiv:1902.10550; "Highest Weight Generating Functions for Hilbert Series" arXiv:1408.4690. — Molien-Weyl + plog workflow analogue, PE/plog formulas. [search summary; PDF binary not extractable in-session]
- **Wikipedia, "F4 (mathematics)"** and **Bourbaki root-system data**. — |W| = 1152; 48 roots (24 short = perms(±1,±1,0,0), 24 long = ±eᵢ,(±½)⁴); 26 = trace-free part of the Albert action. [verified vs computation]

### Tertiary (LOW confidence)
- **Grokipedia "F4"** — 26 weight structure (24 weights mult 1 + zero mult 2); uses the OPPOSITE short/long label from Wikipedia. [single source; reconciled via the calibration gate, not relied upon for the label]

## Metadata

**Confidence breakdown:**
- Mathematical framework (Molien-Weyl form, 27-weights, plog): HIGH — formula is canonical, weight multiset derived and structurally validated (CT = |W|), but exact normalization is gated not proven in-session (MEDIUM on the final normalization).
- Standard approaches (two-route certificate): HIGH — both routes are project-certified or canonical; the cross-check window (a+b ≤ 4) is well-defined.
- Computational tools (SymPy + frozen engine): HIGH — tools verified present and exercised; feasibility budget computed exactly (the (2,2) and a+b ≥ 5 limits are quantified).
- Validation strategies (calibration gates, two-route agreement, Krull/(1,1) anchors): HIGH — multiple independent, exact consistency checks pinned to prior phases.

**Research date:** 2026-05-27
**Valid until:** Indefinite for the mathematics (root systems, Molien-Weyl, prior-phase results are stable). Tool-version-sensitive only via SymPy 1.14 API for `apart`/`residue`/`Poly` (stable). The (2,2) feasibility caveat depends on the executor runtime/watchdog and may need re-assessment at plan time.
