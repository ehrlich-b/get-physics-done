# Methods Research — (RING) Lemma: Joint F_4-Invariants of 27 ⊕ 27

**Domain:** Mathematical physics / invariant theory of exceptional groups (F_4 = Aut(h_3(O)) acting diagonally on the Albert algebra 27 = h_3(O))
**Researched:** 2026-05-24
**Confidence:** HIGH (methods); MEDIUM-HIGH (the literature already containing an explicit pair-ring presentation — see Open Question OQ-1)
**Milestone:** v16.0, the (RING) lemma. The single-state ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] (3 algebraically independent generators), F_4 = compact 52-dim exceptional, and the warm exact-SymPy h_3(O) harness (`code/octonion_algebra.py`: `jordan_product`, `det_3`, `peirce_V1/Vhalf/V0`) are ESTABLISHED. Do NOT re-derive. This file is methodology ONLY — survey/scout, not the proof.

### Scope Boundary

This file covers the analytical and numerical METHODS for proving (RING) sub-claims (a) generating set, (b) functional independence of c = Tr(X∘Y), (c) degree-2 uniqueness. Software/tooling specifics (SymPy version, which harness functions, the f_4 Lie-algebra corroboration stack) live in COMPUTATIONAL.md. The theoretical framework (Albert algebra, cubic norm, F_4 rep theory) lives in PRIOR-WORK.md. Convention conflicts and traps live in PITFALLS.md.

---

## Executive Recommendation (opinionated)

| Sub-claim | THE direct rigorous method | Theorem that licenses it | Cost | Hardest caveat |
|---|---|---|---|---|
| **(a) Generating set** | Weyl polarization (char 0) of the single-copy generators {Tr, Tr², det} + the cubic-norm polarizations, with **Molien/Hilbert-series completeness check** degree-by-degree | Weyl FFT for polarization in char 0 (Weyl, *Classical Groups*; Procesi §; Kraft–Procesi Primer); finite generation by Hilbert–Nagata for reductive G | Hilbert series to degree ≤ 6: minutes in SymPy; full Derksen algorithm: heavier (Gröbner over a 106-dim+ ideal) | Polarization bounds the **degree** but does NOT say single-copy generators *alone* suffice — you MUST adjoin the genuine mixed (cross-frame) polarizations. The "fails for exceptional groups" worry is a **positive-characteristic** phenomenon, irrelevant over R. |
| **(b) Functional independence of c** | **Jacobian-rank / orbit-dimension** demonstration on the actual algebra: show the 7×N differential matrix d(Tr X, Tr X², det X, Tr Y, Tr Y², det Y, c) has rank 7 at a generic point | Jacobian criterion: in char 0, trdeg = generic rank of the Jacobian (Derksen–Kemper Thm; Ehrenborg–Rota / standard) | One symbolic gradient + rank at a random rational point: seconds in exact SymPy | Must be a **demonstrated** rank-7 fact on h_3(O), not asserted (reward-hacking guard). The clean orbit argument (fix generic Y, vary X over its F_4-orbit) is the *conceptual* proof; the Jacobian rank is the *machine-checkable* proof. Do BOTH. |
| **(c) Degree-2 uniqueness** | Decompose Sym²(27 ⊕ 27) into F_4-irreps; **count trivial summands** (a character/branching computation), then identify the genuine coupling generator | Complete reducibility (F_4 compact ⇒ all reps real & completely reducible); multiplicity of trivial = dim of degree-2 invariants | Character integral / weight-multiplicity sum: minutes (LiE/Weyl character formula or harness Reynolds projection) | Must distinguish the **product** invariant Tr(X)Tr(Y) (reducible) from the **genuine** coupling Tr(X∘Y). Both are bidegree-(1,1) F_4-invariants; the claim is that mod products + single-state terms exactly one remains. |

**One-line verdict on the central question (a):** In characteristic zero Weyl's polarization theorem is **valid for every linearly reductive group, exceptional groups included** — so polarizing a single-copy generating set DOES yield a generating set for any number of copies, and the single-copy degree bound transfers. The genuine content of (a) is therefore *not* "does polarization generate?" (yes, by Weyl) but "*which* polarized objects are the new generators, and is the resulting list minimal/complete?" — answered by polarizing det (the cubic norm) and checking the bigraded Hilbert series.

---

## Recommended Methods

### Analytical Methods

| Method | Purpose | Why Recommended |
|---|---|---|
| **Weyl polarization + restitution (char 0)** | (a) Produce a generating set of R[V⊕V]^{F_4} from R[V]^{F_4} | The single theorem that licenses building pair-invariants from single-copy ones; in char 0 it holds for ALL reductive groups (no exceptional-group obstruction). Gives the degree bound β(R[V⊕V]^G) ≤ β(R[V]^G). |
| **Polarization of the cubic norm det(X)** | (a) Generate the mixed coupling invariants explicitly | det is degree 3; its full polarization gives the mixed terms det(X,X,Y)→Tr(X#X · Y)-type and det(X,Y,Y); the degree-2 trace form polarizes from Tr(X²) to give c = Tr(X∘Y). These ARE the cross-frame generators. |
| **Molien / Hilbert–Poincaré series (bigraded)** | (a) Completeness check: verify a candidate generating set degree-by-degree | The Hilbert series H(s,t) = Σ dim R[V⊕V]^{F_4}_{(i,j)} sⁱtʲ is computable from the F_4 character (Molien/Weyl integration). A candidate generator list is COMPLETE iff its free/quotient Hilbert series matches H term-by-term. This is the gold-standard completeness certificate. |
| **Jacobian criterion (char 0)** | (b) Functional/algebraic independence of c from the six pointwise generators | trdeg of {generators} = generic rank of their Jacobian matrix. c independent ⇔ rank jumps from 6 to 7 ⇔ d(c) ∉ span{d(pointwise)} on a dense open set. Exactly the machine-checkable form of the claim. |
| **Orbit-dimension argument (F_4-orbit of X, generic Y fixed)** | (b) The conceptual, coordinate-free proof of independence | All single-state invariants of X are constant on the F_4-orbit of X; if Tr(X∘Y) varies as X ranges over that orbit (for fixed generic Y), then c cannot be a function of the pointwise subring. Made rigorous by orbit dim = dim F_4 − dim Stab(X) and F_4-equivariance of the trace pairing ⟨X,Y⟩ = Tr(X∘Y). |
| **Sym² branching / trivial-summand count** | (c) Degree-2 uniqueness | The space of degree-2 diagonal invariants = (Sym²(27⊕27))^{F_4}; its dimension = multiplicity of the trivial rep in Sym²(27⊕27). A character/branching computation. |
| **Reynolds-operator averaging (projection to invariants)** | (a,c) Independent corroboration: project a monomial basis onto the invariant subspace | For compact F_4, the Reynolds operator R(f) = ∫_{F_4} g·f dg projects onto invariants; its image in each bidegree gives the invariant space directly. Harness-friendly (numerical Haar average or symbolic via characters). |

### Numerical / Symbolic Methods

| Method | Purpose | When to Use |
|---|---|---|
| **Exact-SymPy symbolic gradient + rank-at-rational-point** | (b) The decisive Jacobian-rank computation | PRIMARY for (b). Build the 7 invariants symbolically on a 27-dim parametrized X,Y; form the 7×54 Jacobian; evaluate at a random rational point; check rank = 7. Exact arithmetic ⇒ no false rank from rounding. Reuse the warm `code/octonion_algebra.py` `jordan_product`/`det_3`. |
| **Numerical Haar-average Reynolds projection** | (a,c) Cross-check the invariant dimension in low bidegree | Generate random F_4 group elements (exp of random f_4 Lie-algebra elements), average a monomial; the rank of the averaged-monomial span = dim of invariants. Fast sanity check before symbolic confirmation. |
| **Weyl character formula / weight-multiplicity sum** | (c) Branching of Sym²(27) and Sym²(27⊕27) | Compute Sym² character then decompose against F_4 irreducible characters (or use LiE/SageMath `WeylCharacterRing`). Gives exact multiplicities. |
| **Bigraded Molien series via residue/Weyl integration** | (a) Completeness certificate to degree ≤ 6 | Integrate det(I − s·ρ(g))⁻¹ det(I − t·ρ(g))⁻¹ over F_4; extract coefficients. Heavier; only needed if minimality/completeness of the full generator list is in scope. |

---

## Method Details

### (a) GENERATING SET of R[V ⊕ V]^{F_4}, V = 27

**The licensing theorem (Weyl polarization, characteristic zero).**
Let G be linearly reductive over a field of characteristic 0 (compact F_4 qualifies; its complexification F_4(C) is reductive). Then for any G-module W and any m, the invariant ring R[W^m]^G is generated by **polarizations** of a generating set of R[W^n]^G where n = dim W. Procesi's FFT phrasing: *"simultaneous invariants of a large number of copies of a given representation can all be obtained from n copies by polarization."* Crucial degree corollary: if R[W]^G is generated in degree ≤ d, then so is R[W^m]^G for every m (Weyl). [Weyl, *The Classical Groups*; Procesi, *Lie Groups* Ch. on FFT; Kraft–Procesi *Classical Invariant Theory: A Primer*.]

**Why "fails for exceptional groups" is a non-issue here (address explicitly).**
The literature counterexamples to Weyl polarization are **positive-characteristic** phenomena: in char p there exist explicit failures, and the theorem is recovered only in sufficiently large characteristic for good G-modules (Domokos–Kemper, arXiv:1803.03602, *Weyl's polarization theorem in positive characteristic*). A second, separate subtlety is **separating vs generating**: a characteristic-free analogue holds for *separating* invariants (Draisma–Kemper–Wehlau, "Polarization of Separating Invariants", Canad. J. Math.) but not automatically for *generating* sets. **Over R (char 0), the full generating-set version of Weyl polarization holds for F_4 with no exceptional-group caveat.** The downstream planner should NOT treat exceptional-group status as an obstacle to (a); it is an obstacle only to *minimality* claims and to positive-characteristic variants we never enter.

**What polarization actually produces (the real work of (a)).**
Single-copy generators: Tr(X) (deg 1), Tr(X²) = trace form (deg 2), det(X) = cubic norm N(X) (deg 3). Polarizing each in the diagonal V⊕V action:
- Tr is linear → polarization gives Tr(X), Tr(Y) (no new mixed term).
- Tr(X²) (the quadratic trace form Q(X)=Tr(X²)) polarizes to the **symmetric bilinear trace form** T(X,Y) = Tr(X∘Y) — i.e. **c = Tr(X∘Y) is exactly the (1,1)-polarization of the single-copy degree-2 generator.** This is the lowest-degree genuine coupling generator.
- det(X) (cubic) polarizes to mixed cubics: the (2,1) term ~ Tr(X# ∘ Y) (where X# is the Freudenthal sharp/adjoint, det's gradient) and the (1,2) term ~ Tr(X ∘ Y#). These are the higher coupling generators.

**FFT/SFT framing.** First Fundamental Theorem (FFT): the listed polarized invariants generate. Second Fundamental Theorem (SFT): the *relations* among them (e.g. how products of low-degree couplings re-express higher ones; the syzygies of the cubic-norm polarizations). For (RING) only the FFT (generation) and a degree-2 *minimality* statement are needed; the full SFT (complete syzygy ideal) is OUT OF SCOPE unless the planner wants the entire ring presentation.

**Completeness certificate (the Hilbert-series check — recommended, decisive).**
Compute the bigraded Hilbert series H(s,t) = Σ_{i,j} dim (R[V⊕V]^{F_4})_{(i,j)} sⁱ tʲ by Molien/Weyl integration over F_4. For a candidate generator list with assigned bidegrees, the generated subring has a predictable (rational) Hilbert series; **the list is complete iff the two series agree coefficient-by-coefficient up to the Noether degree bound.** This converts "did we find all generators?" into a finite, verifiable arithmetic check. The single-state series is already known: R[Tr,Tr²,det] ⇒ 1/((1−s)(1−s²)(1−s³)). The planner should target verifying H(s,t) through total degree ≤ 6 (enough to confirm the degree-2 coupling c and the degree-3 mixed cubics, and that no surprise generator hides at degrees 4–6).

**Computational invariant theory (Derksen–Kemper) — the algorithmic fallback.**
If a from-scratch generating set is wanted (rather than verifying the polarization candidate), **Derksen's algorithm** computes a generating set for R[W]^G for linearly reductive G via the *Derksen ideal* (the ideal of the graph of the action), eliminate-and-Reynolds. Practical for F_4 only in low degree; the Molien-series + Reynolds-operator route is simpler but yields **redundant** generators (Derksen–Kemper, *Computational Invariant Theory*, Springer; Kemper ISSAC 2010 tutorial). RECOMMENDATION: do NOT run the full Derksen algorithm; use polarization-to-produce + Hilbert-series-to-verify. Cite Derksen–Kemper as the authority that the problem is algorithmically decidable and that the redundancy of the Reynolds route is expected.

**SymPy + f_4 corroboration path for (a).** (i) Symbolically build the candidate generators (Tr, Tr², det, c=Tr(X∘Y), the two mixed cubics) using `jordan_product`/`det_3`. (ii) Verify each is F_4-invariant by checking its derivative annihilates under all 52 f_4 generators (infinitesimal invariance: D_ξ f = 0 for ξ ∈ f_4 — much cheaper than finite group elements). (iii) Compute the bigraded invariant dimension in each low bidegree by Reynolds projection (numerical Haar average or character integral) and match against the candidate list.

### (b) FUNCTIONAL INDEPENDENCE of c(X,Y) = Tr(X∘Y) from the six pointwise generators

**The precise notion.** "Functional independence" here = **algebraic independence over R is not the claim**; the claim is the weaker, exactly-right statement: *c is not a polynomial (equivalently, by Schwarz/Luna, not a smooth function) in the six pointwise generators.* The clean formalization: the six pointwise invariants g_1,…,g_6 generate a subring R_pt ⊂ R[V⊕V]^{F_4}; c ∉ R_pt. The transcendence-degree / Jacobian formulation makes this checkable.

**Jacobian criterion (the machine-checkable proof — char 0).**
THEOREM (Jacobian criterion, char 0): for polynomials f_1,…,f_k on an affine space, trdeg_R R(f_1,…,f_k) = max rank of the Jacobian matrix [∂f_i/∂x_j] over the variety; equivalently = rank at a generic (dense-open) point. [Standard; Derksen–Kemper *Computational Invariant Theory* §; Ehrenborg–Rota; in char 0 the "large enough characteristic" caveat is vacuous.]

Application: let the seven functions be (g_1,…,g_6, c) on R^{54} (coordinates of X,Y ∈ h_3(O), each 27-dim). Form the 7×54 Jacobian J. Then **c is not a function of g_1,…,g_6 iff rank J = 7 generically** (the gradient d(c) escapes the 6-dim span of d(g_1),…,d(g_6) on a dense set). Since the six pointwise generators already have trdeg 6 (R[Tr,Tr²,det] each ⇒ 3+3, algebraically independent across the two blocks), rank-7 of the full Jacobian is exactly "c adds a new functionally independent direction."

**The exact recipe (hand this verbatim to the executor):**
1. Parametrize X = Σ x_a B_a, Y = Σ y_b B_b in the 27-dim basis {B_a} of h_3(O) (3 real diagonal + 3 octonionic off-diagonal = 3 + 3·8 = 27). 54 symbolic variables.
2. Build symbolically (exact SymPy): g_1=Tr(X), g_2=Tr(X²)=Tr(X∘X), g_3=det_3(X)=N(X), g_4=Tr(Y), g_5=Tr(Y²), g_6=det_3(Y), and c=Tr(X∘Y). (Tr(X∘Y) = the trace bilinear form T(X,Y) = T(XY); for Hermitian X,Y, Tr(X∘Y) = Re Tr(XY).)
3. Jacobian J = Matrix([[diff(f, v) for v in vars] for f in [g1,…,g6,c]]) — 7×54.
4. Pick a random **rational** point (x_a,y_b) ∈ Q^{54} avoiding the discriminant locus; substitute; `J.subs(...).rank()` in exact arithmetic.
5. Assert rank = 7. (If rank = 6 at a generic rational point, c IS in the pointwise subring → the decisive NEGATIVE; report honestly.)

**The clean orbit argument (the conceptual proof — do this TOO, it explains *why*).**
Fix a generic Y. Let X range over its F_4-orbit O_X = {ρ(g)X : g ∈ F_4}. Every single-state invariant of X is, by definition of invariant, **constant** on O_X: Tr(gX)=Tr(X), Tr((gX)²)=Tr(X²), det(gX)=det(X). The single-state invariants of Y are fixed (Y fixed). So if c were a function of the six pointwise generators, c would be CONSTANT on O_X (for fixed Y). But c(gX, Y) = Tr((gX)∘Y) = ⟨ρ(g)X, Y⟩_T where ⟨·,·⟩_T is the F_4-**equivariant** trace pairing; equivalently c(gX,Y) = ⟨X, ρ(g)⁻¹Y⟩_T, which varies as g moves Y′=ρ(g)⁻¹Y around its orbit and pairs against X. **It is not constant** for generic X,Y because the orbit O_X is positive-dimensional (dim O_X = dim F_4 − dim Stab(X) = 52 − dim Stab(X) > 0 for non-fixed X) and the trace form is non-degenerate. Contradiction ⇒ c ∉ R_pt. ∎(sketch)

**What makes the orbit argument rigorous (the load-bearing facts to verify, not assert):**
- **Orbit dimension.** dim O_X = 52 − dim Stab_{F_4}(X). For a *generic* X (regular semisimple-type element of the Jordan algebra), Stab is the small subgroup fixing X; the orbit is positive-dimensional. Verify by computing the rank of the infinitesimal action map ξ ↦ ξ·X (ξ ∈ f_4, 52-dim) at a generic X — its rank = dim O_X. Harness check: build the 27×52 matrix [B_a-components of ξ_k · X], compute its rank at a random rational X.
- **Trace-form equivariance & non-degeneracy.** T(gX, gY) = T(X,Y) for g ∈ F_4 (F_4 preserves the trace form — this is part of F_4 = automorphisms preserving N and T), and T is non-degenerate on h_3(O) (the 27 is real/self-dual for F_4; T is THE invariant pairing). Both are standard (Springer–Veldkamp; Faraut–Koranyi Ch. V) and harness-verifiable.
- **Constancy-on-orbit of pointwise invariants** is definitional (invariance), no computation needed.

**SymPy + f_4 corroboration path for (b).** Two independent confirmations, BOTH required by the reward-hacking guard:
1. *Jacobian route* (algebraic): rank-7 of the 7×54 Jacobian at a random rational point (above). Decisive and self-contained.
2. *Orbit route* (geometric): (i) rank of the infinitesimal-action matrix ξ·X = dim O_X > 0 at generic X; (ii) symbolically/numerically evaluate c(exp(tξ)X, Y) and show d/dt|_0 ≠ 0 for some ξ ∈ f_4 — i.e. c genuinely varies along the orbit while the six pointwise invariants have zero derivative along the same ξ. The pair (nonzero orbit-derivative of c, zero orbit-derivative of every pointwise generator) IS the independence, demonstrated on the actual algebra.

### (c) DEGREE-2 UNIQUENESS — span{Tr(X²), Tr(Y²), Tr(X∘Y)}

**The method: decompose Sym²(27 ⊕ 27) and count trivial summands.**
Degree-2 polynomial functions on 27⊕27 = Sym²((27⊕27)*) ≅ Sym²(27⊕27) (self-dual over F_4). The F_4-invariant degree-2 functions = the trivial-rep isotypic component. Its dimension = multiplicity of **1** in Sym²(27⊕27).

**The branching arithmetic (dimension-checked here; the executor confirms with characters):**
- 27 = **1 ⊕ 26** as F_4-reps (the 27 of E_6 restricts to F_4 as trivial ⊕ 26; the 1 is the Tr direction, the 26 the trace-free part). [PRIOR-WORK.md.]
- Sym²(27) decomposes as **2·(1) ⊕ 2·(26) ⊕ 324**, dim 378 ✓ (since Sym²(26) = 1 ⊕ 26 ⊕ 324, dim 351 = 1+26+324 ✓, and Sym²(1⊕26)=Sym²(1)⊕(1⊗26)⊕Sym²(26)=1⊕26⊕(1⊕26⊕324)). **Trivial multiplicity in Sym²(27) = 2** → the two single-state degree-2 invariants Tr(X)² and Tr(X²). (324 is a genuine F_4-irrep; 1,26,52,273,324,1053,1274 are the small F_4 irreps — confirmed, Wikipedia F_4 / Slansky.)
- For the **diagonal pair**: Sym²(27⊕27) = Sym²(27)_{XX} ⊕ (27⊗27)_{XY} ⊕ Sym²(27)_{YY}. Trivial multiplicities: 2 (XX) + 2 (YY) + mult_1(27⊗27) (the pure cross / bidegree-(1,1) part). And **mult_1(27⊗27) = dim Hom_{F_4}(27,27) = dim End_{F_4}(1⊕26) = 1+1 = 2** (Schur: one scalar for the 1, one for the 26). So the bidegree-(1,1) invariants are **2-dimensional**: spanned by **Tr(X)Tr(Y)** (the reducible product) and **Tr(X∘Y) = c** (the genuine coupling).
- Total degree-2 diagonal invariants = 2 + 2 + 2 = **6**: {Tr(X)², Tr(X²), Tr(Y)², Tr(Y²), Tr(X)Tr(Y), Tr(X∘Y)}.

**The uniqueness statement, made precise.** Modulo products of degree-1 invariants (Tr(X)², Tr(Y)², Tr(X)Tr(Y)) and the single-state degree-2 invariants (Tr(X²), Tr(Y²)), the space of degree-2 invariants is **exactly 1-dimensional**, spanned by c = Tr(X∘Y). Equivalently: the bidegree-(1,1) genuine-coupling space (after removing the reducible product Tr(X)Tr(Y)) is span{Tr(X∘Y)}, dimension 1. THAT is "c is the unique degree-2 coupling generator (mod scale + pointwise terms)." [Matches PROJECT.md sub-claim (c).]

**SymPy + character corroboration path for (c).** (i) Compute the Sym²(27) and Sym²(27⊕27) characters via the Weyl character ring (SageMath `WeylCharacterRing('F4')`, or LiE) and read off the trivial multiplicity = 2 and 6 respectively — the authoritative branching. (ii) Independently, harness-side: enumerate the degree-2 monomial basis in the 54 variables, project with the Reynolds operator (numerical Haar average over F_4, or symbolic via the f_4 infinitesimal-invariance kernel: solve D_ξ f = 0 for all 52 ξ on the 1485-dim degree-2 monomial space), and confirm the invariant space is 6-dimensional with the explicit basis above. The infinitesimal-kernel route is exact and avoids group sampling.

---

## Software Stack

(Tool/version specifics → COMPUTATIONAL.md. Summary only.)

| Layer | Tool | Role in (RING) |
|---|---|---|
| Exact algebra | SymPy (warm harness `code/octonion_algebra.py`) | (b) Jacobian rank, (a) invariance checks, (c) infinitesimal-kernel — all exact rational |
| Lie-algebra structure | f_4 generators (52-dim derivation algebra of h_3(O); buildable from harness Peirce/automorphism data) | (b) orbit dimension via infinitesimal action; (a,c) infinitesimal invariance D_ξ f = 0 |
| Representation theory | SageMath `WeylCharacterRing('F4')` or LiE (cross-check only) | (c) Sym² branching, (a) Hilbert-series coefficients |
| Numerical cross-check | NumPy (random F_4 group elements via exp of random f_4) | Reynolds-projection sanity checks before exact confirmation |

---

## Alternatives Considered

| Recommended | Alternative | When to use the alternative |
|---|---|---|
| **(a)** Polarization + Hilbert-series completeness check | Full Derksen algorithm (Derksen ideal + Gröbner) | Only if a from-scratch generating set is demanded and the polarization candidate is in doubt. Heavier; F_4 in 54 vars strains Gröbner. |
| **(a)** Bigraded Molien via Weyl integration | Reynolds-operator monomial averaging | Reynolds gives the dimension fast but a *redundant* generating set; use it as a cross-check, not the certificate. |
| **(b)** Jacobian-rank at a rational point | Symbolic rank over the function field (generic rank, not at a point) | If worried the chosen rational point is non-generic (on the discriminant); compute the symbolic rank or test 2–3 random points. Costlier but removes the genericity assumption. |
| **(b)** Orbit argument via infinitesimal f_4 action | Finite-group orbit sampling (exp of large random ξ) | Numerical illustration only; the infinitesimal (derivative) version is exact and rigorous. |
| **(c)** Character/branching of Sym² | Direct Reynolds projection on degree-2 monomials | Use as the *independent* corroboration. The character count is the cleaner proof; the projection is the harness witness. |

## What NOT to Use

| Avoid | Why | Use instead |
|---|---|---|
| Asserting "polarization fails for exceptional groups, so (a) is hard/impossible" | The failures are **positive-characteristic** (arXiv:1803.03602) or *separating-vs-generating* subtleties; over R (char 0) Weyl polarization is fully valid for F_4 | State the char-0 theorem; the real content is *which* polarizations and minimality |
| Floating-point Jacobian rank for (b) | Rounding produces spurious rank drops/jumps; rank is discontinuous | Exact rational SymPy rank at a rational point |
| Asserting c's independence from the orbit picture alone, without computation | Reward-hacking guard (PROJECT.md): independence MUST be demonstrated on the actual algebra | Do the rank-7 Jacobian AND the nonzero orbit-derivative of c |
| Claiming algebraic independence of all 7 generators | False and not needed — det(X) and Tr(X²),Tr(X) already satisfy no relation but adding c gives 7 functions on a space where the *invariant ring* has Krull dim = dim(27⊕27) − dim(generic orbit) | Claim only the weaker, true statement: c ∉ R_pt (the pointwise subring), via trdeg jump 6→7 |
| Pursuing the full SFT (complete syzygy ideal of the pair-ring) | Out of scope; (RING) needs generation + degree-2 minimality only | FFT (generation) + Hilbert-series completeness to degree ≤ 6 |
| Re-deriving R[h_3(O)]^{F_4} = R[Tr,Tr²,det] | Established (Springer 1962 cubic-norm uniqueness; Faraut–Koranyi Ch. V) | Cite it; use only as the polarization seed |

## Method Selection by Sub-problem

**If proving (a) generating set:**
- Use polarization (char 0 Weyl FFT) to PRODUCE candidates {Tr, Tr², det of X,Y; c=Tr(X∘Y); mixed cubics Tr(X#∘Y), Tr(X∘Y#)}, then the bigraded Hilbert series (to total degree ≤ 6) to CERTIFY completeness.
- Because polarization is unconditionally valid in char 0, and the Hilbert-series match is a finite verifiable certificate.

**If proving (b) independence of c:**
- Use the exact-SymPy Jacobian rank (decisive, machine-checkable) PLUS the infinitesimal orbit-derivative argument (explanatory, demonstrated on h_3(O)).
- Because the reward-hacking guard demands a *demonstrated* orbit/Jacobian fact, and the two routes are independent confirmations.

**If proving (c) degree-2 uniqueness:**
- Use the Sym²(27⊕27) character/branching (trivial multiplicity = 6; bidegree-(1,1) part 2-dim = {Tr(X)Tr(Y), Tr(X∘Y)}) PLUS the harness infinitesimal-kernel projection on degree-2 monomials.
- Because the branching is the clean proof and the projection is the exact harness witness.

## Validation Strategy by Method

| Method | Validation Approach | Key Benchmarks |
|---|---|---|
| Polarization candidate list (a) | Bigraded Hilbert series match to degree ≤ 6 | Single-state series 1/((1−s)(1−s²)(1−s³)) must appear as the s-only and t-only specializations |
| Jacobian rank (b) | Recompute at 2–3 independent random rational points; confirm rank = 7 each | Pointwise-only Jacobian (6 functions) must give rank 6 |
| Orbit-derivative (b) | Verify every pointwise generator has ZERO derivative along the chosen ξ ∈ f_4 (invariance), while c has NONZERO derivative | dim O_X = rank(ξ·X map) > 0 at generic X (e.g. 52 − dim Stab) |
| Sym² branching (c) | Cross-check dimension sums: Sym²(27)=378, Sym²(26)=351=1+26+324; total degree-2 invariants = 6 | SageMath `WeylCharacterRing('F4')` symmetric_power vs harness Reynolds count must agree |
| Single-state baseline (sanity) | Confirm R[Tr,Tr²,det] is the FULL single-copy invariant ring (3 alg-indep gens) before polarizing | Springer 1962 / Faraut–Koranyi; harness generic-orbit separation |

## Sources

**Invariant-theory foundations:**
- H. Weyl, *The Classical Groups: Their Invariants and Representations*, Princeton 1939/1946 — original polarization theorem (char 0). [textbook]
- H. Derksen, G. Kemper, *Computational Invariant Theory*, Encyclopaedia of Mathematical Sciences 130, Springer (2002; 2nd enlarged ed. 2015) — Derksen's algorithm, Molien/Hilbert series, Jacobian criterion, finite-generation for reductive G. [canonical computational reference] PDF: math.cit.tum.de/.../kem.k.pdf
- C. Procesi, *Lie Groups: An Approach through Invariants and Representations*, Springer 2007 — FFT/SFT, polarization for classical and reductive groups. [textbook]
- H. Kraft, C. Procesi, *Classical Invariant Theory: A Primer* (lecture notes, U. Basel, free) — clean FFT/polarization exposition. dmi.unibas.ch/.../Classical_Invariant_Theory.pdf
- V. L. Popov, E. B. Vinberg, "Invariant Theory", in *Algebraic Geometry IV*, Encyclopaedia of Math. Sciences 55, Springer — reductive-group invariant theory, covariants, finite generation. [reference]
- G. Kemper, "Computational Invariant Theory", ISSAC 2010 tutorial (slides). issac-conference.org/2010/.../TutorialKemper.pdf

**Polarization caveats (the "exceptional group / characteristic" subtleties):**
- M. Domokos, G. Kemper (and related), "Weyl's polarization theorem in positive characteristic", arXiv:1803.03602; Transformation Groups (2020) — explicit char-p failures; recovered in large char for good modules. (Confirms char-0 validity for F_4.)
- J. Draisma, G. Kemper, D. Wehlau, "Polarization of Separating Invariants", Canad. J. Math. — characteristic-free analogue for *separating* (not generating) invariants. (Confirms the generating-set version needs char 0.)

**F_4 / Albert algebra / cubic norm (seed for polarization; cross-listed in PRIOR-WORK):**
- T. A. Springer, "Characterization of a class of cubic forms", Indag. Math. 24 (1962) 259–265 — uniqueness of the cubic norm as the F_4 cubic invariant. (Harness `det_3` cites this.)
- J. Faraut, A. Korányi, *Analysis on Symmetric Cones*, Oxford 1994, Ch. V — Jordan algebra trace/norm, single-state invariant ring. [must-use, PROJECT.md]
- H. P. Petersson, "Albert Algebras" (Fields Institute notes 2012) & "A Survey on Albert Algebras" — trace bilinear form T(x,y)=T(xy), cubic norm structure. fields.utoronto.ca/.../Alb.-alg.-Ottawa-2012.pdf
- M. Thakur, "Exceptional Groups" (ISI Bangalore notes) — F_4 = automorphisms of the Albert algebra preserving N and T. isibang.ac.in/~statmath/.../exceptional.pdf
- F_4 small-irrep dimensions {1,26,52,273,324,1053,1274}: en.wikipedia.org/wiki/F4_(mathematics) (cross-checked, dimension arithmetic above).

**Jacobian / functional independence:**
- Derksen–Kemper (above), Jacobian criterion section (char 0: trdeg = generic Jacobian rank).
- G. W. Schwarz / D. Luna: smooth invariants of a compact (reductive) group are smooth functions of the polynomial generators (relevant to "functional" independence). See arXiv:2510.19053 §1 (Hilbert–Weyl + Schwarz–Luna survey) and Schwarz, "Smooth functions invariant under the action of a compact Lie group", Topology 1975. [licenses upgrading "not a polynomial" to "not a smooth function" if needed]

---

_Methods research for: v16.0 (RING) lemma — joint F_4-invariants of 27 ⊕ 27._
_Researched: 2026-05-24. Confidence HIGH on methods; the one open literature question (an explicit published pair-ring presentation) is flagged in COMPUTATIONAL.md OQ-1._
