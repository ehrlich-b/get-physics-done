# Research Roadmap: v16.0 The (RING) Lemma (Experiential Measure on Structure Space)

## Milestones

- **v1.0 Experiential Measure Formalization** -- Phases 1-3 (completed 2026-03-16)
- **v2.0 QM from Algebraic Genericity** -- Phases 4-7 (completed 2026-03-21)
- **v3.0 GR Extension** -- Phases 8-12 (completed 2026-03-22)
- **v4.0 Spectral Triple from Self-Modeling** -- Phases 13-15 (closed 2026-03-23, medium success)
- **v5.0 Chirality from h_3(O) via Cl(6)** -- Phases 18-21 (completed 2026-03-24)
- **v6.0 Gap C -- Complexification from C*-Measurement Maps** -- Phase 22 (closed 2026-03-24, negative result)
- **v7.0 Arrow of Time, Complexification, and Evolutionary Selection** -- Phases 23-27 (completed 2026-03-24)
- **v8.0 Gap C Algebraic Closure via C*-Measurement Maps** -- Phases 28-31 (completed 2026-03-29)
- **v9.0 Continuum Limit from Finite-Dimensional Observer** -- Phases 32-36 (completed 2026-03-30)
- **v10.0 Universality Class of Self-Modeler Network and Full Gap Closure** -- Phases 37-41 (completed 2026-03-31)
- **v11.0 Gap C Complexification from Sequential Product** -- Phases 42-45 (completed 2026-04-05)
- **v12.0 GR from det(X) on h_3(O)** -- Phases 46-51 (completed 2026-04-12)
- **v13.0 Paper 6 Closure -- G4 + N=2 from Algebraic Structure** -- Phases 52-53 (completed 2026-04-13)
- **v14.0 Paper 5 Revision -- Close Load-Bearing Jigsaw-Piece Gaps** -- Phases 54-59 (PAUSED 2026-04-17, pending JMP referee report; see `.gpd/V14-CLOSEOUT.md`)
- **v15.0 The P5 <-> Basin Restriction Lemma** -- Phases 60-63 (completed 2026-05-24 -- CHARACTERIZED OBSTRUCTION / coexistence-as-island; through-line survives)
- **v16.0 The (RING) Lemma** -- Phases 64-69 (active -- math half of the Chalmers gap; consciousness-side spine, independent of v15.0)

## Overview

**v16.0 proves (or cleanly disproves) the (RING) lemma:** that the inter-frame coupling c(X,Y) = Tr(X o Y) driving the experiential functional Phi is FUNCTIONALLY INDEPENDENT of the single-state F_4-invariant ring R[Tr, Tr^2, det]. Concretely, characterize the diagonal-F_4-invariant ring R[h_3(O) (+) h_3(O)]^{F_4}, prove c is not a polynomial in the six pointwise generators, and show c is the unique degree-2 coupling generator. This is the math half of the Chalmers / Mary gap: the complete third-person record (all single-frame invariants of rho) provably does NOT determine Phi. The work is exact computational invariant theory over Q on the warm v15.0 octonion engine. A decisive NEGATIVE (c expressible in the pointwise ring -> kills the Phi mechanism) is an equally-full pass and must be reported honestly. This milestone is INDEPENDENT of the v15.0 physics-side basin-restriction result (do not entangle).

## Contract Overview

Authoritative contract: PROJECT.md "Scoping Contract Summary" + REQUIREMENTS.md "Contract Coverage" (state.json `project_contract` is null for this fresh milestone).

| Decisive Contract Item | Advanced By Phase(s) | Type |
| ---------------------- | -------------------- | ---- |
| Exact-SymPy h_3(O) engine ported + single-state ring R[Tr,Tr^2,det] confirmed (BASE-01) | 64 | Foundation |
| **GATE: exact generic orbit dimension of F_4 on 27(+)27; anchor 54 - orbit_dim = 7** (BASE-02) | 65 | Chain-critical gate |
| **(b) c = Tr(X o Y) functionally independent of the six pointwise generators [THE SPINE, reward-hacking-guarded]** (RING-02) | 66 | Chain-critical decisive output |
| (c) c is the UNIQUE degree-2 coupling generator mod products + pointwise (RING-03) | 67 | Decisive sub-claim |
| (a) generating set of R[27(+)27]^{F_4} + Hilbert-series completeness certificate (RING-01) | 68 | Decisive sub-claim |
| (REDUCIBILITY) dynamical bridge STATED (not proved) for next milestone (REDU-01) | 69 | Statement-only deliverable |

**Acceptance signal (both are full passes -- NEGATIVE-RESULT-IS-SUCCESS):** a clean (RING) characterization with c provably independent (explicit orbit/Jacobian demonstration on the actual algebra), OR a decisive NEGATIVE (c IS expressible in the pointwise generators). Report honestly; do not bury a negative.

**Active anchors (carry-forward across phases):** Faraut-Korányi (Ch. II-IV, NOT Ch. V -- citation correction); Springer/Springer-Veldkamp + Springer 1962 (cubic norm, polarization); Blind 2011 (E_6 pair-ring, 4 gens -- CONTRAST, not target); Iltyakov 1998 (F_4 trace polynomials); Garibaldi-Guralnick (single-27 generic stabilizer Spin(8), orbit 24); Schwarz math/0609078 (2-polarization fails generically in char 0); Derksen-Kemper (Jacobian criterion: char-0 trdeg = generic rank); `~/repos/blog/research/phi-inaccessibility-program.md`; RhoJ.lean / DS1; pathspace_invariants.py.

**Warm exact engine (binding):** `code/embedding_under_E_verification.py` -- exact-SymPy octonion arithmetic over Q (Jordan product, det_3, polarize_d, Peirce projectors). The float64 `code/octonion_algebra.py` is a FORMULA REFERENCE ONLY and must NOT run on any decisive path (float rank fabricates the 6-vs-7 verdict).

**Tooling:** SymPy 1.14 + NumPy 2.4 only -- no SageMath / GAP / Singular / Macaulay2 / Magma. SymPy carries the entire decisive computation. The (a) Molien/Hilbert step is the ONLY place wanting Sage; resolve via external one-off Sage fixture OR pure-SymPy Molien-Weyl residue (scope decision belongs to the Phase 68 planner).

**Global forbidden proxies (guarded across all phases):**
- Assuming polarization generates the pair ring without a Hilbert-series certificate (Schwarz: the single-copy 2-polarization property fails generically even in char 0).
- Asserting c independent without the exact orbit/Jacobian computation on the actual h_3(O).
- Float arithmetic (`numpy.linalg.matrix_rank`) on the decisive path -- ranks must be `sympy.Matrix.rank()` over Q.
- Non-generic evaluation points (X=Y, X proportional to Y, repeated spectra, discriminant locus) for the independence test.
- Forcing a positive over the honest NEGATIVE (rank 6 = full pass, reported with the constructed explicit pointwise expression for c).
- Looking up the pair orbit dimension / naive Spin(8)-triality back-of-envelope (must be COMPUTED in-harness).
- Proving the (REDUCIBILITY) verdict (STATE only this milestone); grounding irreducibility in "nonlinear, so chaotic"; conflating the autonomous F_3-contraction with the driven stream.
- Redefining "reducible"/"pointwise" so c trivially lands in/out of the ring.

## Phases

- [x] **Phase 64: Setup, Conventions, and Exact Engine** -- Port the exact-SymPy h_3(O) engine, build the 54-symbol pair layout + seven base invariants, freeze R_pt, verify convention locks, confirm single-state ring (BASE-01). Phases continue from 64 (v15.0 ended at 63).
- [ ] **Phase 65: f_4 Construction + Orbit-Dimension GATE** -- Build the 52-generator f_4 = Der(h_3(O)) action, compute the exact generic orbit dimension of F_4 on 27(+)27 via the 52x54 infinitesimal-action rank over Q; verify the consistency anchor 54 - orbit_dim = 7 (BASE-02). GATES Phases 66/67/68.
- [ ] **Phase 66: (b) Functional Independence of c -- THE SPINE** -- Demonstrate c not in R_pt via the exact 7x54 Jacobian rank over Q at >=3 generic rational points AND the infinitesimal orbit-derivative argument; wire the decisive-NEGATIVE branch (RING-02).
- [ ] **Phase 67: (c) Degree-2 Uniqueness** -- Show via Sym^2(27(+)27) branching that the bidegree-(1,1) trivial part is 2-dimensional = span{Tr(X)Tr(Y), Tr(X o Y)}, so c is the unique NEW degree-2 coupling generator mod products + pointwise (RING-03). Parallel with Phase 66.
- [ ] **Phase 68: (a) Generating-Set Completeness Certificate** -- Assemble the candidate generating set and CERTIFY completeness via the bigraded Hilbert/Molien series degree-by-degree to total degree <= 6; do NOT assume polarization generates (RING-01).
- [ ] **Phase 69: (REDUCIBILITY) -- State the Dynamical Bridge (do NOT prove)** -- Write the precise statement of the (REDUCIBILITY) target for the next milestone: driven dynamics, reducibility definition, cross-term decomposition, autonomous-vs-driven trap, target reduction (REDU-01). Statement only; assert NO irreducibility verdict.

## Phase Details

### Phase 64: Setup, Conventions, and Exact Engine

**Goal:** The frozen algebraic foundation is in place -- the exact-SymPy h_3(O) engine is ported and re-verified, the 54-symbol pair coordinatization and seven base invariants are constructed, the pointwise subring R_pt is frozen, all convention locks are checked exactly, and the single-state ("Observable") ring is confirmed to be R[Tr, Tr^2, det]. Everything downstream uses these objects identically.

**Depends on:** -- (entry point; reuses v15.0 warm engine)
**Requirements:** BASE-01
**Contract Coverage:**
- Advances: exact-SymPy engine port + single-state ring confirmation (the "Observable" ring = the pointwise subring of (a)).
- Deliverables: new `code/ring_lemma_verification.py` importing/porting the exact-SymPy octonion block from `embedding_under_E_verification.py`; the 54-symbol pair layout (x0..x26, y0..y26); the seven base invariants {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c=Tr(X o Y)} as SymPy expressions; FROZEN R_pt definition.
- Anchor coverage: Faraut-Korányi Ch. II-IV (single-state ring R[Tr, Tr^2, det]; NOT Ch. V -- record the citation correction); Springer 1962/1973 (cubic norm); warm engine `code/embedding_under_E_verification.py`.
- Required prior outputs: reuse the v15.0 exact octonion harness; do NOT re-derive octonion arithmetic from scratch.
- Forbidden proxies: using the float64 `code/octonion_algebra.py` on any decisive path; definitional drift in R_pt (Pitfall 7); convention traps (wrong det normalization, wrong Jordan product, sharp-vs-d confusion).

**Success Criteria** (what must be TRUE):

1. Convention locks pass exactly in-harness: `polarize_d(X,X,X) == 6*det_3(X)`, `c(X,X) == Tr(X^2)`, and the octonion table reproduces e1*e2 = e4 (Fano, matches Paper 7), `det_3(diag(a,b,c)) == a*b*c`, `det_3(I) == 1` -- all over Q (exact, no floats).
2. The pointwise subring R_pt is FROZEN and documented as the R-subalgebra generated by {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y} = R[..X] (x) R[..Y]; Tr(X)Tr(Y) is recorded as a member of R_pt; the claim (b) is stated as "c not in R_pt".
3. The single-state ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] is confirmed (trdeg 3, degrees 1/2/3), citing Faraut-Korányi Ch. II-IV (with the Ch. V citation correction recorded) -- the "Observable" ring of the Chalmers-gap framing equals exactly this pointwise single-copy subring.
4. The engine is exact-only on the decisive path: the new verification module imports the SymPy octonion block, and a guard/check confirms no `numpy.linalg.matrix_rank` (or float arithmetic) is reachable from the rank computations.

**Backtracking:** If any convention lock fails (e.g., `polarize_d(X,X,X) != 6*det_3(X)`), STOP and reconcile against the harness header before building anything -- a wrong normalization corrupts every downstream invariant. If the ported engine disagrees with the v15.0 harness benchmarks, treat as a port error, not a new result.

**Plans:** 1 plan

Plans:
- [x] 64-01-PLAN.md -- Port exact-SymPy h_3(O) engine, build 54-symbol pair layout + seven invariants, freeze R_pt, verify 5 convention locks exactly over Q, confirm single-state ring (one cohesive wave-1 plan, 6 tasks)

### Phase 64.1: det_3 generic-norm-consistency fix (CORRECTIVE)

**Status:** Complete (2026-05-25). Opened during `/gpd:plan-phase 65` when verification uncovered that the Phase-64 frozen `det_3` was **not** the F_4 = Aut(h_3(O))-invariant cubic norm: its cross term used `2*Re((x1*x2)*x3)` but the generic norm of the frozen Jordan product needs `2*Re((x2*x1)*x3)` (octonion factor order; `Re(x1 x2 x3) != Re(x2 x1 x3)`). The wrong form satisfies all five original locks yet is annihilated by only 30/324 inner derivations.

**Fix:** one-line cross-term correction in `code/ring_lemma_verification.py`, plus a **permanent generic-norm-consistency lock (Task 7)** that certifies, on genuinely octonionic points, that `det_3` (7a) equals the Cayley-Hamilton generic norm of `jordan` and (7b) is annihilated by ALL inner derivations `[L_a,L_b]` (324/324, dim f_4 = 52). The five original locks are necessary-but-insufficient; the verification *process* was the defect and is now closed. Harness: 27/27 ALL_PASS, exit 0. Builder verified correct (reproduces single-copy orbit 24 = Spin(8)). See `.gpd/phases/64.1-det3-norm-consistency-fix/64.1-SUMMARY.md`.

**Blast radius (separate audit):** the same bug is in `code/octonion_algebra.py:~2178` (used by prior phases/papers); triage via the `[L_a,L_b]`-kills-det_3 probe.

### Phase 65: f_4 Construction + Orbit-Dimension GATE

**Goal:** The 52-generator infinitesimal action of f_4 = Der(h_3(O)) is built (closed under commutator, dimension 52 verified) and the exact generic orbit dimension of F_4 acting diagonally on h_3(O) (+) h_3(O) is computed as the rank over Q of the 52x54 infinitesimal-action matrix at a generic rational point. This fixes the target transcendence degree (54 - orbit_dim) and therefore the expected Jacobian rank and Hilbert-series Krull dimension for every downstream phase. The consistency anchor 54 - orbit_dim = 7 is the early go/no-go for the whole milestone.

**Depends on:** Phase 64 (exact engine, pair layout, base invariants)
**Requirements:** BASE-02 (GATE)
**Contract Coverage:**
- Advances: the chain-critical GATE -- exact generic pair orbit dimension -> transcendence degree; gates RING-01/02/03.
- Deliverables: 52 f_4 generators as 27x27 rational matrices (g_2 derivations + inner [L_A, L_B], closed under commutator, dim asserted = 52); the 52x54 infinitesimal-action matrix and its exact rank over Q at a generic rational point; transcendence degree = 54 - orbit_dim; single-copy sanity (orbit 24, stabilizer Spin(8) dim 28, trdeg 3).
- Anchor coverage: Garibaldi-Guralnick (single-27 generic stabilizer Spin(8), orbit 24, trdeg 27-24=3); Schafer (derivation formula D_{a,b}, Der(h_3(O)) = f_4); Derksen-Kemper (Jacobian/orbit criterion in char 0).
- Required prior outputs: the Phase 64 exact engine and the seven base invariants (D_xi annihilation test reuses them).
- Forbidden proxies: looking up the pair orbit dimension; the naive Spin(8)-triality back-of-envelope (the three 8's are permuted -- a generic element of one is NOT trivially stabilized; the pair principal isotropy must be COMPUTED); float rank.

**Success Criteria** (what must be TRUE):

1. The 52 f_4 generators are built as 27x27 matrices over Q, verified closed under commutator, and the spanning set has rank exactly 52 over Q (the dimension of f_4 is confirmed, not assumed).
2. Infinitesimal invariance holds exactly: D_xi annihilates det_3, Tr, and Tr^2 for all 52 generators xi at a random rational point (D_xi f = 0 over Q) -- the continuous-group invariance test that finite-group sampling cannot establish.
3. The generic orbit dimension is computed as the exact rank over Q of the 52x54 infinitesimal-action matrix at a generic rational point (substitute the rational point BEFORE taking the rank, to avoid det_3 expression swell in 54 variables).
4. The consistency anchor is verified: **54 - orbit_dim = 7** (= six pointwise + c), i.e. transcendence degree of R[27(+)27]^{F_4} = 7, with orbit_dim <= 47 and pair-stabilizer dim >= 5.
5. Single-copy sanity reproduced: F_4 on one 27 gives generic orbit dimension 24, stabilizer Spin(8) (dim 28), trdeg 27 - 24 = 3 (cross-check of the f_4 builder against Garibaldi-Guralnick).

**GATE / Backtracking:** If 54 - orbit_dim != 7, the whole generating-set picture (six pointwise + c) is wrong -- STOP and reconsider before any RING phase; this is the milestone's early go/no-go (consider `/gpd:research-phase` only on this failure). If the single-copy sanity (orbit 24 / Spin(8)) does not reproduce, the f_4 builder is broken -- fix it before computing the pair value.

### Phase 66: (b) Functional Independence of c -- THE SPINE

**Goal:** It is DEMONSTRATED -- on the actual non-associative h_3(O), by exact computation over Q -- whether c = Tr(X o Y) is functionally independent of the six pointwise generators. This is the load-bearing result and the mathematical content of "the complete third-person (single-frame) record does not determine Phi." The verdict is either independence (Jacobian rank 7) or the decisive NEGATIVE (rank 6, c expressible in the pointwise ring), both full passes.

**Depends on:** Phase 65 (orbit-dimension gate fixes the target rank 7)
**Requirements:** RING-02 (the SPINE)
**Contract Coverage:**
- Advances: THE SPINE -- the decisive Jacobian-rank verdict (7 = independent; 6 = decisive negative). This is the single load-bearing contract item.
- Deliverables: (i) the exact 7x54 Jacobian rank over Q at >=3 independent generic rational points (rank 7 = independent); (ii) the infinitesimal orbit-derivative argument (pointwise invariants constant on the F_4-orbit of X while c varies, via the F_4-equivariant non-degenerate trace form and dim O_X > 0); (iii) on the NEGATIVE branch, the explicit polynomial expressing c in {Tr, Tr^2, det of X and Y}.
- Anchor coverage: Derksen-Kemper Jacobian criterion (char 0: trdeg = generic Jacobian rank); the orbit/Jacobian computation on the actual h_3(O); warm exact engine `embedding_under_E_verification.py`.
- Required prior outputs: Phase 65 orbit dimension (the target rank), the Phase 64 base invariants and f_4 action.
- Forbidden proxies: asserting independence without the orbit/Jacobian computation (Pitfall 2); float rank (Pitfall 3); non-generic evaluation point -- X=Y, X proportional to Y, repeated spectra (Pitfall 4); forcing a positive over the honest NEGATIVE (Pitfall 5).

**Success Criteria** (what must be TRUE):

1. The exact 7x54 Jacobian of {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y, c} has a definite rank over Q computed at **>=3 independent generic rational points** (all-nonzero, distinct diagonals, X not proportional to Y), with the same rank at every point (rank stable across points). **The verdict is exactly one of: rank 7 (c INDEPENDENT -- positive pass) OR rank 6 (c DEPENDENT -- decisive NEGATIVE, full pass).**
2. Baseline control: the pointwise-only 6x54 Jacobian {six pointwise generators} has rank exactly 6 over Q (the pointwise generators are themselves independent), and the degenerate point X=Y correctly gives rank <= 6 and is NOT used as an independence-test point.
3. The infinitesimal orbit-derivative argument is carried out independently of the Jacobian: there exists an f_4 direction along the F_4-orbit of X on which every pointwise generator has zero derivative while c has nonzero derivative (the trace form is F_4-equivariant and non-degenerate, dim O_X > 0) -- on the positive branch, this confirms rank 7 by a second route.
4. NEGATIVE branch wired: IF the rank is 6, an explicit polynomial P with c = P(Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y) is CONSTRUCTED and reported (this kills the Phi mechanism and is a full pass -- reported honestly, not buried).
5. Consistency with the gate: the verdict rank is <= 54 - orbit_dim = 7 (Phase 65), and a rank of 7 saturates the transcendence-degree bound (c is a genuinely new functionally-independent invariant).

**Backtracking:** If the Jacobian rank is unstable across generic points, suspect a non-generic point (re-pick all-nonzero, distinct-spectrum X, Y with X not proportional to Y) before doubting the engine. If the two routes disagree (Jacobian says 7 but the orbit-derivative finds no separating direction, or vice versa), do NOT report a verdict -- isolate the discrepancy (this is the reward-hacking guard: both routes are mandatory). Pre-register the exact test before evaluating, so a NEGATIVE cannot be quietly rerolled.

### Phase 67: (c) Degree-2 Uniqueness

**Goal:** It is established that c is the UNIQUE degree-2 coupling generator modulo scale, products, and pointwise terms. Concretely, the bidegree-(1,1) trivial part of the invariant ring is shown to be exactly 2-dimensional = span{Tr(X)Tr(Y), Tr(X o Y)}, of which Tr(X)Tr(Y) is reducible (a product of pointwise generators), leaving c as the single genuine (irreducible, non-product) degree-2 coupling invariant.

**Depends on:** Phase 65 (orbit-dimension gate); runs in PARALLEL with Phase 66 (both depend only on the gate)
**Requirements:** RING-03
**Contract Coverage:**
- Advances: the degree-2 uniqueness sub-claim -- c is the unique NEW degree-2 coupling generator.
- Deliverables: the Sym^2(27 (+) 27) decomposition into F_4-irreps with trivial-summand count; the bidegree-(1,1) part shown 2-dimensional = span{Tr(X)Tr(Y), Tr(X o Y)}; the genuine-coupling quotient (mod the reducible product) shown 1-dimensional; a precise statement of "mod products" (Tr(X)Tr(Y) is reducible).
- Anchor coverage: F_4 irrep dims (Sym^2(27) = 378, Sym^2(26) = 351 = 1 (+) 26 (+) 324; 27 = 1 (+) 26); Schur's lemma (dim End_{F_4}(1 (+) 26) = 2); cross-check via the exact f_4-kernel nullspace on degree-2 monomials.
- Required prior outputs: Phase 64 base invariants; Phase 65 f_4 action (for the nullspace cross-check).
- Forbidden proxies: conflating Sym^2(26) with Sym^2(27); forgetting the trivial summand; dropping the "mod products" qualifier (Tr(X)Tr(Y) is a reducible degree-2 invariant -- the 26-vs-27 confusion, Pitfall 6).

**Success Criteria** (what must be TRUE):

1. The F_4 branching is verified exactly: 27 = 1 (+) 26; Sym^2(27) has dimension 378; Sym^2(26) = 1 (+) 26 (+) 324 (dimension 351); the (27 (x) 27) trivial multiplicity is 2.
2. The bidegree-(1,1) trivial part of R[27 (+) 27]^{F_4} is exactly 2-dimensional, spanned by {Tr(X)Tr(Y), Tr(X o Y)} (= dim End_{F_4}(1 (+) 26) = 2 via Schur's lemma applied to the two copies of the "1" and the 26 (x) 26 -> 1 contraction).
3. Modulo the reducible product Tr(X)Tr(Y) (a product of pointwise generators) and pointwise terms, the genuine-coupling quotient is 1-dimensional -- c = Tr(X o Y) is the UNIQUE degree-2 coupling generator. The "mod products" qualifier is stated precisely.
4. Cross-check: the exact f_4-infinitesimal-kernel nullspace on degree-2 monomials of (X, Y) over Q matches the branching count (number of independent degree-2 invariants = 6 diagonal {Tr X^2, Tr Y^2, (Tr X)^2, (Tr Y)^2, Tr(X)Tr(Y), ...} consistent with the (1,1) part = 2), confirming the representation-theoretic count by direct computation.

**Backtracking:** If the bidegree-(1,1) trivial part comes out with dimension != 2, recheck the 27 = 1 (+) 26 split and whether Tr(X)Tr(Y) was double-counted or dropped (Pitfall 6). If the exact nullspace disagrees with the branching count, trust the exact nullspace and re-derive the irrep arithmetic.

### Phase 68: (a) Generating-Set Completeness Certificate

**Goal:** The generating set of R[h_3(O) (+) h_3(O)]^{F_4} is assembled from candidate generators and its completeness is CERTIFIED degree-by-degree via the bigraded Hilbert/Molien series to total degree <= 6. This is a certification phase, not a derivation phase: polarization is used only to PRODUCE candidates, and the Hilbert-series match supplies the completeness certificate that polarization cannot.

**Depends on:** Phase 65 (orbit-dimension gate -> Krull dimension), Phase 67 (degree-2 structure)
**Requirements:** RING-01
**Contract Coverage:**
- Advances: the generating-set sub-claim (a) -- the assembled minimal F_4 two-copy generating set + the completeness certificate.
- Deliverables: candidate generators {six pointwise; c = Tr(X o Y); polarized mixed cubics f(X,X,Y), f(X,Y,Y); and any needed higher trace monomials Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)}; the bigraded Hilbert/Molien series matched to the candidate set for all total degrees <= 6; minimality (each generator fails the in-span-of-lower-products test); Krull dimension from the series = 54 - orbit_dim.
- Anchor coverage: Blind 2011 (E_6 pair ring = free on 4 det-polarizations -- CONTRAST/lower bound, NOT the target; c is F_4- but not E_6-invariant, which is exactly why F_4 is the right group); Iltyakov 1998 (F_4 several-copy invariants = trace polynomials + Laplace invariants); Schwarz math/0609078 (2-polarization fails generically in char 0); Derksen-Kemper (Molien/Hilbert series, plethystic log); `polarize_d` (d(X,X,X) = 6 det).
- Required prior outputs: Phase 65 orbit dimension (Krull dim target); Phase 67 (1,1)-part result (the degree-(1,1) Hilbert coefficient must equal 2).
- Forbidden proxies: assuming polarization generates the pair ring (Schwarz: single-copy 2-polarization property fails generically even in char 0 -- this is the headline guard for (a)); confusing spanning with minimal generating (Pitfall 8); importing the E_6 free-algebra answer as if it were the F_4 ring.

**Scope decision (planner must make explicit):** the bigraded Molien step is the ONLY computation wanting a tool the environment lacks (Sage `WeylCharacterRing('F4')`). Resolve EITHER by staging an external one-off Sage bigraded-multiplicity table (d_X + d_Y <= 6) as a data fixture in the plan (keeping the executor self-contained), OR by implementing the Molien-Weyl residue in pure SymPy. This phase is LAST of the proof phases and does NOT gate (b)/(c).

**Success Criteria** (what must be TRUE):

1. The candidate generating set is assembled with explicit bidegrees: six pointwise (degrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3)), c at (1,1), the polarized mixed cubics f(X,X,Y) at (2,1) and f(X,Y,Y) at (1,2), plus any trace monomials the bidegree match demands.
2. The bigraded Hilbert/Molien series of R[27 (+) 27]^{F_4} is computed and matched, bidegree-by-bidegree, against the candidate generating set for all total degrees <= 6; the bidegree-(1,1) coefficient is 2 (consistent with Phase 67), and any bidegree where the true dimension exceeds the candidate count flags a genuinely-missing generator at that degree.
3. The Krull dimension read from the Hilbert series equals 54 - orbit_dim (Phase 65), and the s-only / t-only specialization reproduces the single-state series 1 / ((1 - s)(1 - s^2)(1 - s^3)) (degrees 1,2,3).
4. Minimality: each proposed generator fails the in-span-of-products-of-lower-degree-generators test (it is a genuine generator, not redundant) -- spanning is distinguished from minimal generating.
5. The completeness verdict is stated honestly: either the candidate set is certified complete to total degree <= 6 (with explicit note that polarization was NOT assumed to generate -- the Hilbert match is the certificate), OR a specific bidegree with a missing generator is reported.

**Backtracking:** If the Hilbert series shows d_true > d_candidate at some bidegree, a genuinely-new generator is missing there -- add the lowest-degree trace monomial at that bidegree and re-match; do NOT paper over the gap by assuming polarization closes it. If Sage is chosen for the fixture and is unavailable at plan time, fall back to the pure-SymPy Molien-Weyl residue (the scope decision must be resolved in-plan, not deferred to the executor who lacks Sage).

### Phase 69: (REDUCIBILITY) -- State the Dynamical Bridge (do NOT prove)

**Goal:** The precise statement of the (REDUCIBILITY) dynamical bridge is written for the next milestone -- specifying the driven self-modeling dynamics, the reducibility definition, the cross-term decomposition, the autonomous-vs-driven trap, and the target reduction. This is a STATEMENT-ONLY deliverable: the milestone asserts NO irreducibility verdict and uses NO chaos/NKS argument.

**Depends on:** Phase 64 (frozen conventions; can be written any time after setup)
**Requirements:** REDU-01 (STATE, do NOT prove)
**Contract Coverage:**
- Advances: the statement-only deliverable -- "what the next milestone needs" for the (REDUCIBILITY) verdict.
- Deliverables: the driven self-modeling dynamics X_{k+1} = P_psd((1-eps) X_k^2 + eps S_k); the reducibility definition (capacity / reconstructibility -- f reducible if reconstructible from the bounded data the diachronic self-model M can hold, dim M < dim B, re-running the law if needed); the cross-term decomposition Tr(X_k o X_{k+1}) = (1-eps) Tr(X_k^3) [pointwise, reducible] + eps Tr(X_k o S_k) [self-world overlap, the irreducible candidate]; the explicit autonomous-vs-driven trap flag; the target reduction (driven gauge-overlap not reconstructible from M's bounded held data -> routes to a STRUCTURAL Breuer / finite-capacity argument).
- Anchor coverage: `~/repos/blog/research/phi-inaccessibility-program.md` Sec.9 (the reframe this milestone serves); the cross-term decomposition.
- Required prior outputs: the Phase 64 conventions (Jordan product, Tr, det) so the cross-term decomposition is written in the frozen notation.
- Forbidden proxies: asserting any irreducibility verdict (prerequisites unmet -- this milestone STATES, the next proves); grounding irreducibility in "nonlinear, so chaotic" / NKS; conflating the autonomous F_3-contraction (reducible -- contracts to a fixed point) with the driven stream (irreducibility, if any, inherited from the exogenous input's unpredictability).

**Success Criteria** (what must be TRUE):

1. The driven dynamics X_{k+1} = P_psd((1-eps) X_k^2 + eps S_k) is written precisely (P_psd = projection to positive-semidefinite; S_k = exogenous driven stream; eps = self-world coupling), distinguished explicitly from the autonomous (S fixed) map.
2. The reducibility definition is fixed in capacity / reconstructibility terms: f is reducible if it is reconstructible from the bounded data the diachronic self-model M can hold (dim M < dim B), re-running the law if needed -- NOT a redefinition that makes c trivially land in or out of the invariant ring.
3. The cross-term decomposition is algebraically correct: Tr(X_k o X_{k+1}) = (1-eps) Tr(X_k^3) [pointwise, reducible] + eps Tr(X_k o S_k) [self-world overlap, the irreducible candidate], verified consistent with the Jordan-product and trace conventions from Phase 64.
4. The autonomous-vs-driven trap is explicitly flagged: the autonomous F_3-contraction is reducible (contracts to a fixed point -- a numerical canary may illustrate this); any irreducibility is INHERITED from the exogenous driven stream's unpredictability, never from chaos/NKS. The target reduction (driven gauge-overlap not reconstructible from M's bounded held data -> structural Breuer / finite-capacity argument) is stated as "what the next milestone needs."
5. NO irreducibility verdict is asserted anywhere in the deliverable (the write-up only STATES the target).

**Backtracking:** If the cross-term decomposition does not check out algebraically against the Phase 64 conventions, fix the statement (this is a correctness check on the statement, not a proof attempt). If the write-up drifts toward asserting irreducibility or invoking chaos, cut it -- the deliverable is strictly a statement of the next-milestone target.

## Phase Dependencies

| Phase | Depends On | Enables | Critical Path? |
|-------|-----------|---------|:-:|
| 64 - Setup + Exact Engine | -- | 65, 69 | Yes |
| 65 - f_4 + Orbit-Dimension GATE | 64 | 66, 67, 68 | Yes (the GATE) |
| 66 - (b) Independence of c [SPINE] | 65 | -- | Yes (the SPINE) |
| 67 - (c) Degree-2 Uniqueness | 65 | 68 | No (parallel with 66) |
| 68 - (a) Generating-Set Completeness | 65, 67 | -- | No (last proof phase) |
| 69 - (REDUCIBILITY) Statement | 64 | -- | No (independent, statement-only) |

**Critical path:** 64 -> 65 -> 66 (the gate then the spine; 3 phases minimum to the decisive result).
**Parallelizable:** Phase 67 (c) runs concurrently with Phase 66 (b) -- both depend only on the gate. Phase 69 (REDUCIBILITY statement) can be written any time after Phase 64. Phase 68 (a) is last of the proof phases (it certifies completeness; it does not gate (b)/(c)).

**Wave schedule (for `/gpd:execute-phase`):**
- Wave 1: Phase 64 (sole entry point)
- Wave 2: Phase 65 (the GATE -- must pass before any RING phase)
- Wave 3: Phase 66 (SPINE) || Phase 67 (c) || Phase 69 (REDUCIBILITY statement) -- parallel
- Wave 4: Phase 68 (a) -- needs the gate + the degree-2 structure from 67

## Risk Register

| Phase | Top Risk | Probability | Impact | Mitigation |
|-------|---------|:-:|:-:|-----------|
| 64 | Wrong convention / float engine on decisive path | LOW | HIGH | Convention locks (`polarize_d=6det`, `c(X,X)=Tr X^2`) verified before building; exact-only guard against `numpy.linalg.matrix_rank` |
| 65 | Consistency anchor 54 - orbit_dim != 7 (whole generating-set picture wrong) | LOW-MEDIUM | HIGH | GATE: STOP on failure; single-copy sanity (orbit 24 / Spin(8)) cross-checks the f_4 builder first; `/gpd:research-phase` only on this failure |
| 65 | Naive Spin(8)-triality back-of-envelope corrupts the orbit dimension | MEDIUM | HIGH | Forbidden proxy: COMPUTE the pair orbit dimension in-harness, never look it up; the three 8's are permuted |
| 66 | Asserting independence without the demonstration / forced positive over NEGATIVE | MEDIUM | HIGH | Reward-hacking guard: BOTH the exact Jacobian (>=3 generic points) AND the orbit-derivative are mandatory; pre-register the exact test; NEGATIVE (rank 6) is a full pass reported with the explicit c expression |
| 66 | Non-generic evaluation point fabricates the verdict | MEDIUM | HIGH | >=3 generic rational points (all-nonzero, distinct diagonals, X not proportional to Y); X=Y is NOT an independence-test point |
| 67 | 26-vs-27 confusion / dropping "mod products" | LOW | MEDIUM | Carry 27 = 1 (+) 26 explicitly; exact f_4-kernel nullspace cross-checks the branching count |
| 68 | Assuming polarization generates (Schwarz: 2-polarization fails in char 0) | MEDIUM | HIGH | (a) is a CERTIFICATION phase: Hilbert-series match degree-by-degree is the completeness certificate; mismatch at a bidegree => missing generator there |
| 68 | Sage unavailable for the Molien step | MEDIUM | LOW | Scope decision in-plan: external Sage fixture OR pure-SymPy Molien-Weyl residue; phase is last and non-gating |
| 69 | Drift into asserting irreducibility / chaos shortcut | LOW | MEDIUM | STATEMENT-ONLY; autonomous-vs-driven trap flagged; no irreducibility verdict; no NKS |

## Progress

**Execution Order:** 64 -> 65 (GATE) -> (66 SPINE || 67 || 69) -> 68

| Phase | Milestone | Plans Complete | Status | Completed |
| ----- | --------- | -------------- | ------ | --------- |
| 64. Setup, Conventions, Exact Engine | v16.0 | 1/1 | ✓ Complete | 2026-05-25 |
| 65. f_4 Construction + Orbit-Dimension GATE | v16.0 | 0/TBD | Pending | - |
| 66. (b) Functional Independence of c [SPINE] | v16.0 | 0/TBD | Pending | - |
| 67. (c) Degree-2 Uniqueness | v16.0 | 0/TBD | Pending | - |
| 68. (a) Generating-Set Completeness Certificate | v16.0 | 0/TBD | Pending | - |
| 69. (REDUCIBILITY) State the Dynamical Bridge | v16.0 | 0/TBD | Pending | - |

## Coverage

- v16.0 requirements: 6 total (BASE-01, BASE-02, RING-01, RING-02, RING-03, REDU-01)
- Mapped to phases: 6/6 (100%) -- no orphans, no duplicates
- Decisive contract items surfaced: 6/6 (engine+single-state ring, orbit-dim GATE, the (b) SPINE, (c) uniqueness, (a) generating set, (REDU) statement)
- Chain-critical items flagged: the orbit-dimension GATE (Phase 65) and the (b) SPINE (Phase 66)
- Anchors surfaced in contract coverage: Faraut-Korányi (Ch. II-IV correction), Springer/Springer-Veldkamp, Blind 2011 (contrast), Iltyakov 1998, Garibaldi-Guralnick, Schwarz, Derksen-Kemper, warm exact engine `embedding_under_E_verification.py`, phi-inaccessibility-program.md
- Forbidden proxies surfaced: polarization-without-Hilbert-certificate, assert-without-orbit/Jacobian, float-on-decisive-path, non-generic point, forced-positive-over-negative, look-up-orbit-dim, prove-REDUCIBILITY, chaos/autonomous-vs-driven, redefine-reducible

---

_v16.0 roadmap created 2026-05-24. Phases 64-69 derived from the 6 requirements (BASE-01/02, RING-01/02/03, REDU-01), the PROJECT.md scoping contract, and the SUMMARY.md gated ordering (all four scouts converged). Decisive deliverable: (RING) proved (or decisive NEGATIVE) with c provably independent. NEGATIVE-RESULT-IS-SUCCESS. Independent of v15.0._
