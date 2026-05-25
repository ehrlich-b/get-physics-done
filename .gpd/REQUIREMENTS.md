# Requirements: v16.0 The (RING) Lemma

**Defined:** 2026-05-24
**Core Research Question (this milestone):** Does the complete third-person record — all single-state F_4-invariants of a Stream — determine Phi, or is the inter-frame cross-term c(X,Y) = Tr(X o Y) that Phi integrates provably independent of the single-state invariant ring R[Tr, Tr^2, det]? (The math half of the Chalmers gap; consciousness-side spine, independent of v15.0.)

## Primary Requirements

### Foundational Baseline

- [x] **BASE-01**: Confirm the single-state ("Observable") ring R[h_3(O)]^{F_4} = R[Tr, Tr^2, det] (Faraut-Korányi Thm IV.2.5 / Springer; the milestone prompt's "Ch. V" attribution is imprecise — the invariant-ring fact lives in Ch. II-IV). Port and re-verify the EXACT-SymPy h_3(O) engine (octonion arithmetic over Q, Jordan product a o b = (1/2)(ab+ba), `det_3` = cubic norm with d(X,X,X) = 6·det X, Peirce projectors) from `code/embedding_under_E_verification.py`. The float64 `code/octonion_algebra.py` must NOT be used on any decisive path.

- [ ] **BASE-02 (GATE)**: Compute the exact generic ORBIT DIMENSION of F_4 acting diagonally on h_3(O) ⊕ h_3(O): build the 52-generator f_4 action (g_2 derivations + inner derivations [L_A, L_B], closed under commutator, dim = 52 asserted) and compute the rank over Q of the 52×54 infinitesimal-action matrix at a generic rational point. Derive transcendence degree = 54 − orbit_dim and verify the consistency anchor **54 − orbit_dim = 7** (six pointwise + c). Compute it; do NOT look it up (the Spin(8)-triality back-of-envelope is a trap). This gates RING-01/02/03.

### The (RING) Lemma

- [ ] **RING-01 (a) — generating set**: Establish the generating set of R[h_3(O) ⊕ h_3(O)]^{F_4} (diagonal F_4). Assemble candidate generators — the six pointwise {Tr X, Tr X^2, det X, Tr Y, Tr Y^2, det Y}, the coupling c = Tr(X o Y), the polarized mixed cubics f(X,X,Y), f(X,Y,Y), and any needed higher trace monomials (Tr(X^2 o Y), Tr(X o Y^2), Tr(X^2 o Y^2)) — and CERTIFY completeness via the bigraded Hilbert/Molien series degree-by-degree to total degree ≤ 6. Do NOT assume polarization generates (Schwarz: the 2-polarization property can fail in char 0; completeness needs the Hilbert-series certificate).

- [ ] **RING-02 (b) — functional independence [THE SPINE]**: Prove c = Tr(X o Y) is FUNCTIONALLY INDEPENDENT of the six pointwise generators. Two proofs, both demanded by the reward-hacking guard: (i) exact 7×54 Jacobian rank over Q at ≥3 independent generic rational points (rank 7 = independent); (ii) the infinitesimal orbit-derivative argument (the pointwise invariants are constant on the F_4-orbit of X while c varies, because the trace form is F_4-equivariant and non-degenerate and dim O_X > 0). A rank-6 result for the full set is the decisive NEGATIVE — a full pass — and must be reported with the explicit polynomial expressing c in the pointwise generators.

- [ ] **RING-03 (c) — degree-2 uniqueness**: Prove c is the UNIQUE degree-2 coupling generator (mod scale, products, and pointwise terms). Decompose Sym^2(27 ⊕ 27) into F_4-irreps; show the bidegree-(1,1) trivial part is 2-dimensional = span{Tr(X)Tr(Y), Tr(X o Y)}, so the only NEW (irreducible, non-product) degree-2 coupling invariant is c. State the "mod products" precisely (Tr(X)Tr(Y) is reducible).

### Dynamical Bridge (statement only)

- [ ] **REDU-01 (STATE, do NOT prove)**: Write the precise statement of the (REDUCIBILITY) dynamical bridge for the next milestone. Specify the driven self-modeling dynamics X_{k+1} = P_psd((1−eps) X_k^2 + eps S_k); fix the reducibility definition (capacity / reconstructibility — f reducible if reconstructible from the bounded data the diachronic self-model M can hold, dim M < dim B, re-running the law if needed); write the cross-term decomposition Tr(X_k o X_{k+1}) = (1−eps) Tr(X_k^3) [pointwise, reducible] + eps Tr(X_k o S_k) [self-world overlap, the irreducible candidate]; flag the AUTONOMOUS-vs-DRIVEN trap (the autonomous F_3-contraction is reducible; irreducibility is inherited from the exogenous input's unpredictability); state the target reduction (driven gauge-overlap not reconstructible from M's bounded held data → routes to a STRUCTURAL Breuer / finite-capacity argument). Output as "what the next milestone needs." No chaos/NKS; assert NO irreducibility verdict.

## Out of Scope

| Topic | Reason |
| ----- | ------ |
| The (REDUCIBILITY) irreducibility VERDICT | Prerequisites unmet; this milestone STATES it, does not prove it. Needs a structural finite-capacity (Breuer) argument — separate milestone. |
| ID-MOVE "irreducible residue = experience" | Axiom-B / identification move; separate track, never "proved" here. |
| The frame-quotient half (why a third party gets only the invariants) | QRF / no-broadcasting; framework-level identification, separate from this invariant-theory half. |
| Wolfram-as-authority / NKS framing | Ground in invariant theory + (eventually) algorithmic incompressibility, never NKS. |
| Whether Phi is phenomenology; whether rho is "off a brain" | Open encoding question (§17.8); out of scope. |
| The basin-restriction question (v15.0) | Physics-side spine; separate, does NOT bear on this invariant-theory claim. |
| Full Second Fundamental Theorem (complete syzygy/relation ideal) | (RING) needs generation + degree-2 minimality only; the full relation ideal is not required. |

## Accuracy and Validation Criteria

| Requirement | Accuracy Target | Validation Method |
| ----------- | --------------- | ----------------- |
| BASE-01 | Exact (symbolic over Q) | d(X,X,X) = 6·det X and det(diag(a,b,c)) = abc reproduced exactly; engine = `embedding_under_E_verification.py` (exact, not float64) |
| BASE-02 | Exact integer rank | rank over Q of the 52×54 infinitesimal-action matrix; consistency 54 − orbit_dim = 7; re-checked at ≥2 generic rational points |
| RING-01 | Exact, degree-by-degree | bigraded Hilbert/Molien series matches the candidate generating set for all total degrees ≤ 6 (Krull dimension = 54 − orbit_dim) |
| RING-02 | Exact integer rank | 7×54 Jacobian rank = 7 over Q at ≥3 generic rational points; pointwise-only Jacobian = rank 6; rank-6-for-full ⇒ decisive NEGATIVE reported with explicit expression for c |
| RING-03 | Exact irrep multiplicities | Sym^2(27 ⊕ 27) trivial-summand count; bidegree-(1,1) part dim = 2; F_4 irrep dims verified (Sym^2(27) = 378, Sym^2(26) = 351) |
| REDU-01 | N/A (statement only) | cross-term decomposition algebraically correct; autonomous-vs-driven trap explicitly flagged; no irreducibility asserted |

## Contract Coverage

| Requirement | Decisive Output / Deliverable | Anchor / Benchmark / Reference | Prior Inputs / Baselines | False Progress To Reject |
| ----------- | ----------------------------- | ------------------------------ | ------------------------ | ------------------------ |
| RING-02 | exact Jacobian-rank verdict (7 = independent; 6 = decisive negative) | orbit/Jacobian on the actual h_3(O); Derksen-Kemper Jacobian criterion (char 0: trdeg = generic rank) | exact engine `embedding_under_E_verification.py` | asserting independence without the orbit/Jacobian computation; float rank; non-generic evaluation point |
| RING-01 | generating set + Hilbert-series completeness certificate | Blind 2011 (E_6, 4 gens, contrast); Iltyakov 1998 (F_4 trace polys) | `polarize_d` (d(X,X,X)=6 det) | assuming polarization generates (Schwarz: 2-polarization property can fail in char 0) |
| RING-03 | Sym^2(27⊕27) branching: c is the unique NEW degree-2 coupling | F_4 irrep dims; Schur's lemma (dim End_{F_4}(1⊕26)=2) | METHODS Sym^2 arithmetic | forgetting Tr(X)Tr(Y) is a reducible degree-2 invariant |
| BASE-02 | exact orbit dim → transcendence degree; anchor 54 − orbit_dim = 7 | Garibaldi-Guralnick (single 27: generic stabilizer Spin(8), orbit 24) | f_4 action builder | the naive Spin(8)-triality back-of-envelope (must be COMPUTED) |
| REDU-01 | precise statement of the next-milestone target | `phi-inaccessibility-program.md` §9 | cross-term decomposition | asserting irreducibility (chaos / autonomous-vs-driven conflation) |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
| ----------- | --------------------------------------------- | ------ |
| BASE-01 | Phase 64 — Setup, Conventions, and Exact Engine | Verified (passed 2026-05-25) |
| BASE-02 (GATE) | Phase 65 — f_4 Construction + Orbit-Dimension GATE | Pending |
| RING-02 (b) [SPINE] | Phase 66 — (b) Functional Independence of c | Pending |
| RING-03 (c) | Phase 67 — (c) Degree-2 Uniqueness | Pending |
| RING-01 (a) | Phase 68 — (a) Generating-Set Completeness Certificate | Pending |
| REDU-01 (STATE only) | Phase 69 — (REDUCIBILITY) State the Dynamical Bridge | Pending |

**Coverage:**

- Primary requirements: 6 total (BASE-01, BASE-02, RING-01, RING-02, RING-03, REDU-01)
- Mapped to phases: 6/6 (100%) — every requirement maps to exactly one primary phase
- Unmapped: 0 (no orphans, no duplicates)
- Chain-critical items: BASE-02 (the orbit-dimension GATE, Phase 65) and RING-02 (the (b) SPINE, Phase 66)
- Phase numbering: 64-69 (continuing from v15.0's Phase 63)

**Phase ordering note:** the gated ordering (per SUMMARY.md, all four scouts converged) is preserved — Setup (64) → orbit-dim GATE (65, gates the RING phases) → the (b) SPINE (66) and (c) (67) in parallel → (a) generating-set completeness (68, last of the proof phases) → (REDUCIBILITY) statement (69). The traceability table above is ordered by phase number; note RING-02/03/01 map to phases 66/67/68 in that gated order, NOT in REQ-ID numeric order.

---

_Requirements defined: 2026-05-24_
_Last updated: 2026-05-24 — traceability mapped to Phases 64-69 during v16.0 roadmap creation_
