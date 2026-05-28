# Research Digest: v16.0 The (RING) Lemma

Generated: 2026-05-27
Milestone: v16.0
Phases: 64–69 (6 primary + 2 corrective decimals: 64.1, 65.1)

## Narrative Arc

The Radical Relativity program's consciousness-side spine asks the math half of the Chalmers / Mary
gap: does the complete third-person record of a Stream — *all* single-state F_4-invariants of the
density object ρ — determine the experiential functional Φ? Φ integrates an inter-frame cross-term
c(X,Y) = Tr(X∘Y). If c is a function of the single-state invariant ring R[Tr, Tr², det], the third-person
record fixes Φ and the (Φ-inaccessibility) mechanism collapses; if c is provably independent, the
record does not determine Φ. v16.0 settles this as a question of exact computational invariant theory
over Q on the warm v15.0 octonion engine.

The work proceeds: (64) port the exact-SymPy h_3(O) engine, freeze the pointwise subring R_pt, confirm
the single-state ring R[h_3(O)]^{F_4} = R[Tr, Tr², det]; (64.1, corrective) repair the cubic norm det₃
to the genuine F_4-invariant (factor-order fix, certified by 324/324 inner-derivation annihilation);
(65) build the 52-generator f_4 = Der(h_3(O)) action and compute the generic pair orbit dimension of
F_4 on 27⊕27 — the GATE. The GATE **fired by design**: the orbit dimension is 44, so the transcendence
degree is 54−44 = **10, not the naive-anchor 7** (the anchor was exactly the forbidden Spin(8)-triality
back-of-envelope; the true generic stabilizer descends Spin(8)→Spin(7)→G₂→SU(3), dim 8). The
"six pointwise + c" picture undercounts by 3 joint invariants. (65.1, corrective) pins those three down
as the natural mixed trace monomials Tr(X²∘Y), Tr(X∘Y²), Tr(X²∘Y²), confirming the 10-candidate set has
field-level Jacobian rank 10 by a second route. With the corrected target in hand, the three RING
sub-claims close: (66) **the SPINE** — c is functionally independent of the six pointwise generators
(exact 7×54 Jacobian rank 7, two routes agreeing); (67) c is the **unique** degree-2 coupling generator
(bidegree-(1,1) trivial part 2-dimensional = span{Tr(X)Tr(Y), c}, quotient 1); (68) the 10-candidate set
is a **complete and minimal** generating set to total degree ≤6, certified by an exact-over-Q bigraded
Hilbert/Molien match (polarization was NOT assumed to generate — the Hilbert match is the certificate).
Finally (69) states — without proving — the (REDUCIBILITY) dynamical bridge for the next milestone,
with its one owed algebraic identity (the cross-term decomposition) verified exact over Q.

The verdict is a clean POSITIVE: **c = Tr(X∘Y) is a genuine, minimal, functionally-independent,
unique-degree-2 generator of R[27⊕27]^{F_4}.** The third-person single-frame record provably does not
determine the inter-frame content Φ integrates. The decisive subtlety — that the GATE refuted the naive
anchor 7 and forced trdeg 10 — strengthened rather than weakened the result: c is the first of four
genuinely-joint invariants, so its independence is robust, not a knife-edge saturation.

## Key Results

| Phase | Result | Equation / Value | Validity | Confidence |
| ----- | ------ | ---------------- | -------- | ---------- |
| 64 | Exact engine + single-state ring confirmed | R[h_3(O)]^{F_4} = R[Tr, Tr², det]; locks `d(X,X,X)=6·det X`, `c(X,X)=Tr(X²)`, `det(diag)=abc` | exact over Q | HIGH (5 locks) |
| 64.1 | det₃ repaired to genuine F_4 cubic norm | cross-term `2·Re((x₂x₁)x₃)`; annihilated by 324/324 inner derivations [L_a,L_b] | exact over Q | HIGH (27/27) |
| 65 | Pair orbit-dimension GATE (fired) | orbit dim **44** → trdeg = 54−44 = **10 ≠ 7**; generic Stab Spin(8)→Spin(7)→G₂→SU(3), dim 8 | exact QQ rank | HIGH (triple-confirmed) |
| 65.1 | trdeg-10 generating set pinned | 10-candidate Jacobian rank **10** (MAX over 4 generic pairs); +3 mixed Tr(X²∘Y),Tr(X∘Y²),Tr(X²∘Y²) | exact over Q | HIGH (22/22) |
| 66 | **THE SPINE**: c functionally independent | 7×54 Jacobian rank **7** (baseline 6, X=Y control 6) + orbit-derivative separating ξ | exact over Q | HIGH (4/4) |
| 67 | c the unique degree-2 coupling generator | (1,1) trivial mult = **2** = span{Tr(X)Tr(Y), c}; quotient **1**; Schur 1²+1²=2 == nullspace 729−727=2 | exact over Q | HIGH (7/7) |
| 68 | Generating set CERTIFIED COMPLETE | d_candidate==d_true at **all 28 bidegrees** a+b≤6; (2,2) a GENERATOR (8→9); FREE through deg6; Krull=10; CT_w=\|W(F_4)\|=1152 | exact over Q | HIGH (9/9) |
| 69 | (REDUCIBILITY) bridge STATED (not proved) | `Tr(X_k∘X_{k+1}) = (1−ε)Tr(X_k³) + ε·c(X_k,S_k)`; `Tr(X∘X²)=2885361604861/14428814400`; 5/5 residuals 0 | exact over Q | HIGH (25/25; statement only) |

Cross-phase coherence (one inequality chain): **trdeg 10 (65/65.1) ≥ SPINE rank 7 (66) ≥ quotient 1 (67)**; Krull dim 10 (68); bidegree-(1,1) coefficient 2 (67 == 68).

## Methods Employed

- **Phase 64:** Exact-SymPy octonion arithmetic over Q (byte-faithful COPY of the v15.0 warm engine), Jordan product X∘Y=½(XY+YX), cubic norm det₃, polarize_d; convention locks established exactly; exact-only source guard (regex, comment-stripped) against `numpy.linalg.matrix_rank` on the decisive path.
- **Phase 64.1:** Generic-norm-consistency repair — det₃ cross-term factor order corrected to `2·Re((x₂x₁)x₃)`; a permanent lock certifying det₃ equals the Cayley-Hamilton generic norm of the Jordan product AND is annihilated by all 324 inner derivations (the five original locks were necessary-but-insufficient; the verification *process* was the defect).
- **Phase 65:** f_4 = span{[L_a,L_b]} as 52 independent 27×27 rational matrices; exact orbit dimension = rank over Q of the (52-basis × 54) infinitesimal-action matrix at a generic integer pair (point substituted BEFORE the rank); `DomainMatrix.convert_to(QQ).rank()` for width-54 (plain `Matrix.rank()` does not return at 54 symbolic columns); pre-registered anchor assertion fails loudly on disconfirmation; independent from-scratch reconstruction (full 324-row stack, two exact domains) before trusting the negative.
- **Phase 65.1:** Candidate-Jacobian rank as the exact dual of the certified orbit-tangent rank (two-route trdeg cross-check, Derksen-Kemper char-0); F_4-invariance gate (D_M f=0, all 52 generators) BEFORE any rank; deterministic fallback ladder (a recorded no-op — the three natural monomials sufficed).
- **Phase 66:** Two computationally-independent mandatory routes — Route 1 exact 7×54 sub-Jacobian rank over Q (MAX over 5 generic pairs); Route 2 orbit-derivative separating-direction test (a separating f_4 direction ξ with D_ξ c ≠ 0 while all 6 pointwise derivatives vanish) — with a diagonal-only adjudicator as the reward-hacking guard (off-diagonal ⇒ NO VERDICT + STOP); the NEGATIVE branch fully wired and probe-tested even though the positive fired.
- **Phase 67:** Leibniz lift ρ(M)=M⊗I+I⊗M realized as the (1,1) Sylvester condition MᵀC + CM = 0 (guard: the wrong M⊗M lift annihilates c for 0/52 generators vs the correct 52/52); invariant dim = 729 − exact_qq_rank(stacked operator); named-basis identification (in-kernel AND linearly independent via witness Tr(I)Tr(I)=9 ≠ c(I,I)=3) defeats dimension-match-only; Route A Schur dim End_{F_4}(1⊕26)=1²+1²=2 as the literature cross-check.
- **Phase 68:** Bigraded Molien series H(s,t) via a pure-SymPy Molien-Weyl iterated symbolic residue (no Sage, no float grid; CT_w=1152); calibration gates G1 (single-copy specialization [1,1,2,3,4,5,7]) + G2 (d_(1,1)=2); completeness by candidate-product dimension saturation (exact_qq_rank, generic octonionic pairs); minimality by the in-span-of-lower-products exact test (distinguishes a minimal generating set from a Reynolds spanning set); two-route tripwire Molien == exact-over-Q f_4-kernel at every feasible bidegree; plethystic-log generator/relation separation.
- **Phase 69:** Statement-only typing of five frozen-notation objects + exactly two grounding checks (Breuer citation + the EXACT-Q cross-term decomposition as a polynomial-identity bookkeeping check, NOT a proof); target reduction routed to a STRUCTURAL finite-capacity (Breuer) argument, explicitly forbidding any chaos/NKS/Lyapunov route; modulo-P_psd projection-correction named, not dropped.

## Convention Evolution

| Phase | Convention | Description | Status |
| ----- | ---------- | ----------- | ------ |
| 64 | Group | F_4 = Aut(h_3(O)) (compact, 52-dim; fixes Tr, trace form, det) — NOT E_6 = Stab(det). c is F_4- but not E_6-invariant. | Active |
| 64 | Representation | 27 = 1 (trivial/Tr direction) ⊕ 26 (trace-free irreducible, self-dual) | Active |
| 64 | Jordan product | X∘Y = ½(XY+YX); Tr(X∘Y) = Re Tr(XY) for Hermitian X,Y | Active |
| 64 | Coupling generator | c = Tr(X∘Y), bidegree (1,1); c(X,X) = Tr(X²) (NOT (Tr X)²) | Active |
| 64 | Cubic norm / polarization | det X = N(X); LOCKED d(X,X,X) = 6·det X | Active |
| 64 | Pointwise subring | R_pt = R-subalgebra gen by {Tr X, Tr X², det X, Tr Y, Tr Y², det Y} = R[..X]⊗R[..Y]; FROZEN. Tr(X)Tr(Y) ∈ R_pt; claim (b) is c ∉ R_pt. | Active |
| 64 | Arithmetic field | EXACT over Q; ranks via `sympy.Matrix.rank()` / `DomainMatrix`-over-QQ, NEVER `numpy.linalg.matrix_rank`. Warm engine = `code/ring_lemma_verification.py` (ported from `embedding_under_E_verification.py`); float64 `octonion_algebra.py` is a formula reference only. | Active |
| 64 | Citation correction | Single-state ring R[Tr, Tr², det] is Faraut-Korányi Ch. II–IV, NOT Ch. V (Ch. V is the classification). | Active |
| **64.1** | **det₃ cross-term** | **CORRECTED to `2·Re((x₂x₁)x₃)`** (octonion factor order: Re(x₁x₂x₃) ≠ Re(x₂x₁x₃)). The original `2·Re((x₁x₂)x₃)` satisfied all 5 base locks but was annihilated by only 30/324 inner derivations. New permanent generic-norm lock added. | **Superseded the Phase-64 det₃** |
| 65 | Krull / transcendence degree | trdeg R[27⊕27]^{F_4} = 54 − orbit_dim = **10** (NOT the naive Spin(8)-triality value 7) | Active (the "7" is FORBIDDEN downstream) |

## Figures and Data Registry

(Pure algebra — no plots/figures this milestone. Deliverables are self-contained exact-over-Q assert-harnesses, each exits 0.)

| File | Phase | Description | Paper-ready? |
| ---- | ----- | ----------- | ------------ |
| `code/ring_lemma_verification.py` | 64 (+64.1) | Frozen exact-SymPy engine: octonion arithmetic, Jordan product, det₃ (64.1-corrected), polarize_d, Tr/Tr²/c, 54-symbol pair layout, R_pt frozen block, 5 convention locks + generic-norm lock | Yes (the binding engine) |
| `code/orbit_dimension_gate.py` | 65 | f_4 builder (52 gens), single-copy GATE (orbit 24/Spin(8)/trdeg 3), pair orbit dim 44 → trdeg 10, exact_qq_rank machinery | Yes |
| `code/ring_generating_set.py` | 65.1 | 10-candidate trdeg-10 generating set + bidegree table; two-route rank-10 confirmation; tier ladder (6,7,8,9,10) | Yes |
| `code/spine_independence.py` | 66 | THE SPINE: 7×54 Jacobian rank 7 + orbit-derivative route + two-route adjudicator + wired NEGATIVE branch | Yes (decisive) |
| `code/degree2_uniqueness.py` | 67 | (1,1)=2 by Schur + exact f_4-kernel nullspace; named basis spans; quotient 1; full deg-2 dim 6 | Yes |
| `code/molien_bigraded.py` | 68 | Bigraded Molien-Weyl iterated residue H(s,t) to deg 6; CT_w=1152; gates G1/G2; Krull=10; two-route tripwire | Yes |
| `code/generating_set_certificate.py` | 68 | Completeness (d_candidate==d_true all 28 bidegrees) + minimality (in-span test) + (2,2) generator decision + plethystic log (free through deg6) | Yes (decisive) |
| `code/reducibility_decomposition_check.py` | 69 | EXACT-Q cross-term decomposition check (5/5 residuals 0; Tr(X∘X²)=2885361604861/14428814400) | Supporting (bookkeeping, not a proof) |
| `derivations/69-reducibility-statement.md` | 69 | The durable (REDUCIBILITY) statement (five typed objects in frozen notation) the next milestone opens | Yes (next-milestone seed) |

## Open Questions

(Both are explicitly BEYOND v16.0 scope — they motivate the next milestone, not gaps in this one.)

1. **Global freeness of R[27⊕27]^{F_4}.** Is the ring GLOBALLY free (a polynomial ring on the 10 generators), or non-free with its first relation at total degree ≥7? The certificate establishes freeness through degree 6 (10 generators == Krull dim 10 is consistent with a polynomial ring); the Blind E_6 contrast suggested ultimate non-freeness. Settling this needs the Hilbert series past degree 6, where the f_4-kernel cross-check is infeasible — outside sub-claim (a) scope.
2. **(REDUCIBILITY) irreducibility verdict.** Is the driven gauge-overlap ε·Tr(X_k∘S_k) = ε·c(X_k,S_k) genuinely NOT reconstructible from the bounded diachronic self-model M (dim M < dim B), i.e. irreducible? Honest residual: the program-doc Sec 9.6.1 concedes it "is not automatic" (an integrable flow would make it reducible). Route: a STRUCTURAL Breuer / finite-capacity argument (NOT chaos/NKS). The modulo-P_psd projection correction Tr(X_k∘(X_{k+1}−Y_k)) must be handled in closed form. This is the NEXT milestone's burden — v16.0 only STATES the target.

## Dependency Graph

    Phase 64 "Setup + Exact Engine" (BASE-01)
      provides: frozen engine, R_pt, single-state ring, 54-symbol layout, 7 base invariants
      requires: (v16.0 literature survey + roadmap)
    → Phase 64.1 "det₃ norm-consistency fix" (corrective)
      provides: genuine F_4 cubic norm (324/324 annihilation)
    → Phase 65 "f_4 + Orbit-Dimension GATE" (BASE-02)
      provides: f_4 builder (52 gens), pair orbit dim 44, trdeg 10, single-copy sanity 24/Spin(8)/3
      requires: 64
    → Phase 65.1 "trdeg-10 generating-set count correction" (corrective)
      provides: 10-candidate set + bidegree table, two-route rank-10
      requires: 64, 65
    → Phase 66 "(b) Independence of c — THE SPINE" (RING-02)
      provides: c functionally independent (rank 7), two-route agreement
      requires: 64, 65, 65.1
    → Phase 67 "(c) Degree-2 Uniqueness" (RING-03)
      provides: (1,1)=2, quotient 1, named basis spans
      requires: 64, 65, 65.1, 66
    → Phase 68 "(a) Generating-Set Completeness Certificate" (RING-01)
      provides: CERTIFIED COMPLETE to deg≤6, (2,2) a generator, free through deg6, Krull 10
      requires: 65, 65.1, 66, 67, 68-Plan01
    → Phase 69 "(REDUCIBILITY) Statement" (REDU-01)
      provides: frozen-notation bridge statement + EXACT-Q cross-term certificate
      requires: 64, 66, 68

    Critical path: 64 → 65 (GATE) → 66 (SPINE). Parallelizable: 67 ∥ 66; 69 any time after 64.

## Mapping to Original Objectives

| Requirement | Status | Fulfilled by | Key Result |
| ----------- | ------ | ------------ | ---------- |
| BASE-01 (single-state ring + exact engine) | Complete | Phase 64 (+64.1) | R[h_3(O)]^{F_4} = R[Tr,Tr²,det]; exact engine ported, R_pt frozen, locks pass exactly over Q |
| BASE-02 GATE (orbit dim → trdeg; anchor) | Complete (anchor refuted as designed) | Phase 65 | orbit dim 44 → trdeg **10 ≠ 7**; the naive anchor 7 was the forbidden triality value; honest computed value is the deliverable (NEGATIVE-RESULT-IS-SUCCESS) |
| RING-01 (a) generating set | Complete | Phase 68 | 10-candidate set CERTIFIED COMPLETE + MINIMAL to total degree ≤6 (d_candidate==d_true all 28 bidegrees); polarization NOT assumed — Hilbert match is the certificate |
| RING-02 (b) functional independence [SPINE] | Complete | Phase 66 | c INDEPENDENT: exact 7×54 Jacobian rank 7 + orbit-derivative separating direction (two routes agree) |
| RING-03 (c) degree-2 uniqueness | Complete | Phase 67 | c the UNIQUE degree-2 coupling generator; (1,1) trivial part 2-dim = span{Tr(X)Tr(Y), c}, quotient 1 |
| REDU-01 (STATE, do NOT prove) | Complete (statement only) | Phase 69 | (REDUCIBILITY) bridge STATED as five typed objects; cross-term decomposition verified EXACT over Q; NO irreducibility verdict, NO chaos/NKS |

**Consequence (the Chalmers-gap math half):** "Observable-about-a-single-frame" = exactly the pointwise
ring R_pt; the inter-frame content Φ integrates (the cross-term c) is provably NOT a function of the
single-frame Observable data. The complete third-person record of ρ does not determine Φ.

---

_For current project status, see `.gpd/ROADMAP.md` and `.gpd/PROJECT.md`. Full phase detail:
`.gpd/milestones/v16.0-ROADMAP.md`. Requirements as shipped: `.gpd/milestones/v16.0-REQUIREMENTS.md`._
