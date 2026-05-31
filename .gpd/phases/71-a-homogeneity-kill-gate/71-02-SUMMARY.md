---
phase: 71-a-homogeneity-kill-gate
plan: 02
depth: full
one-liner: "Route-2 + CALC-02 two-route cross-check (FULL V_0, exact over Q): e_6=f_4+L(traceless) dim 78=52+26; dim Stab_E6(E_11)=ker{D->D.E_11}=61 (orbit of E_11=17=affine cone over the Cayley plane OP^2); the slice-preserving Stab_{V_0}=Spin(9,1) dim 45, NON-transitive on V_0 (orbit 9<10, the 1 modulus = det_2); but CALC-02 finds II(V_0)=0 (TOTALLY GEODESIC, sub-Jordan-algebra sub-cone) at >=2 positive-cone basepoints and II(h_2(C_u))=0 (=> the 71-01 H^3 K=-1/2 is constant), while II!=0 once a V_1/2 matter direction is added. The three measurements DISAGREE (CALC-02 II=0 KILL-signal vs Route-1 SURVIVES) => per test-two-route-agreement, NO Phase-71 verdict is emitted; STOP + LOCALIZE: matterless V_0 geometry is homogeneous (KILL signal), Route-1 SURVIVES is sourced ENTIRELY by V_1/2/V_1 MATTER (the Phase-72 question), NOT a Riemannian-vs-Lorentzian/Wick artifact"
subsystem: [derivation, validation, analysis]
tags: [jordan-algebra, h3o, e6, f4, koecher-tits, stabilizer, orbit-dimension, peirce, second-fundamental-form, totally-geodesic, gauss-equation, cayley-plane, spin-9-1, two-route-crosscheck, exact-over-Q, kill-gate, route-disagreement, no-verdict]

requires:
  - phase: 71-a-homogeneity-kill-gate
    provides: "Plan 71-01 Route-1 curvature verdict = SURVIVES (R,K differ across 4 generic rational basepoints on the dim-4 h_2(C_u) sub-slice, exact over Q); the Totaro curvature engine + off-center machinery + rho_J variable in the certified engine; H^3 cone-Hessian benchmark K=-1/2 (constant negative)"
  - phase: 70-a0-engine-reconciliation-signature-bridge
    provides: "certified SSOT det_3 (LOCK 0 byte-identity, LOCK 7a/7b F_4 certificate); cone metric g_X=Hess(-log det); Peirce index map under E_11; construction-(ii) signature bridge"
provides:
  - "e_6 = f_4 + L(h_3(O)_traceless) build (dim 78 = 52+26, exact span rank over Q) added to the certified engine"
  - "dim Stab_{E_6}(E_11) = ker{D -> D . E_11} = 61 exact over Q (orbit of E_11 = 17 = affine cone over the Cayley plane OP^2); two independent rank routes agree"
  - "dim Stab_{V_0} = 45 = dim Spin(9,1) (the V_0-slice-preserving subgroup; recovers the contract's structural Levi expectation); V_0 orbit 9 < family 10, trdeg-1 modulus = det_2"
  - "second fundamental form II of V_0 via the Hessian-metric algebraic shortcut II^n_{bc}=(1/2)f_{abc}n^a (no metric inverse, full V_0): II(V_0)=II(h_2(C_u))=0 (totally geodesic) at positive-cone basepoints; II!=0 with one V_1/2 matter direction"
  - "the FINAL two-route reconciliation: ROUTE DISAGREEMENT (CALC-02 II=0 KILL-signal vs Route-1 SURVIVES) => NO verdict, localization = matter-vs-geometry split (Phase-72), NOT a Wick/Phase-70 artifact"
affects: [72, 73]

methods:
  added:
    - "e_6 Koecher-Tits assembly from primitives: f_4 = span(inner_derivations()) (52) + L(h_3(O)_traceless) (26 multiplication operators, traceless basis {E_1-E_0,E_2-E_0} U {E_3..E_26})"
    - "dim Stab as exact kernel: 78 - rank[D.E_11] (exact_qq_rank DomainMatrix-over-QQ); Stab generators = nullspace lifted to 27x27 matrices"
    - "Stab_{V_0} = slice-preserving subgroup via the normal-projection linear constraint (D.e_b)_a=0 for a normal, b in V_0"
    - "second fundamental form of a Hessian metric via lowered Christoffel Gamma_{a,bc}=(1/2)f_{abc}: II^n_{bc}=(1/2)f_{abc}n^a, g-normal n; NO metric inverse, addresses the FULL tangent space"
    - "cached symbolic derivative tensor (_ii_d1/_ii_d2_col) so 4 II evaluations share one heavy build (watchdog-safe)"
  patterns:
    - "single-copy anchor reproduced via exact_qq_rank (DomainMatrix-over-QQ, ~0.01s) instead of dense Matrix.rank (~55s/pt) -- identical exact rational result, watchdog-safe, NOT a float proxy"
    - "II evaluated only at POSITIVE-cone basepoints (det_3>0, g nondegenerate, dim_normal=17); pure-V_0 (alpha=0) is the cone boundary (det_3=0, g singular) and is correctly excluded"
    - "ROUTE DISAGREEMENT handled per contract: NO verdict emitted, localization returned (do NOT relabel, do NOT force agreement)"

key-files:
  created: [derivations/71-homogeneity-stabilizer.tex, .gpd/phases/71-a-homogeneity-kill-gate/71-02-LOG.md, .gpd/phases/71-a-homogeneity-kill-gate/71-02-STATE-TRACKING.md]
  modified: [code/bulk_geometry_verification.py]

key-decisions:
  - "NO FINAL Phase-71 verdict emitted. The three decisive measurements DISAGREE: Route 1 (71-01) = SURVIVES (matter-loaded basepoints); CALC-02 II(V_0)=0 => totally geodesic => homogeneous => KILL signal; Route 2 (Stab_{V_0}=Spin(9,1) orbit 9<10) shows the 1 modulus is the radial det_2, the symmetric-space leaves homogeneous (consistent with II=0). Per the contract acceptance test test-two-route-agreement, agreement is PART OF THE PASS CONDITION; on disagreement the plan STOPS and localizes the error, emitting NO verdict. This is exactly the contract's named disconfirming_observation ('II=0 while Route 1 SURVIVES => contradiction via Gauss => localize')."
  - "LOCALIZATION: the mathematics is fully consistent; the routes probe DIFFERENT submanifolds. PURE GEOMETRY (matterless): V_0=h_2(O) and its h_2(C_u) spacetime sub-slice are TOTALLY GEODESIC (II=0), homogeneous symmetric-space slices (the 71-01 H^3 K=-1/2 is constant). Route-1's SURVIVES arises ENTIRELY from off-center-ness in the V_1/2/V_1 MATTER directions (II!=0 there), i.e. the PHASE-72 matter-sourcing question. The disagreement is curvature-vs-II (investigate the matter-vs-geometry split), NOT Riemannian-vs-Lorentzian (both pictures agree on matter-sources-curvature) => NOT a return to Phase 70."
  - "dim Stab_{E_6}(E_11) = 61 (decisive, exact over Q), NOT the ~45 structural guide. The orbit of E_11 = 17 = dim of the AFFINE CONE OVER THE CAYLEY PLANE OP^2 (E_11 a primitive idempotent on the rank-<=1 minimal-orbit locus) -- a textbook number, two independent rank routes agree. The contract's ~45 is the semisimple Levi Spin(9,1), which is RECOVERED as the slice-preserving subgroup dim Stab_{V_0}=45, NOT the full parabolic of the cone point (61). The contract explicitly flagged ~45 as a non-decisive sanity guide."
  - "CALC-02 OVERTURNS the Kollross-Rodriguez-Vazquez Table-7 inference (V_0 absent from the MAXIMAL totally-geodesic list => leans non-geodesic): the DIRECT II computation finds V_0 IS totally geodesic (a sub-Jordan-algebra sub-cone, Faraut-Koranyi). The research explicitly placed the decisive weight on the direct II computation, not the literature inference (its WebFetch returned only the abstract)."

patterns-established:
  - "Pattern: Route-2 group-theory gates ADDED to the 70/71-01-certified engine (Section 13); engine stays ALL_PASS exit 0 (41/41 PASS), deterministic (run1==run2), exact-only source guard PASS (0 octonion_algebra, 0 float-rank)."
  - "Pattern: a decisive two-route DISAGREEMENT is reported HONESTLY as no-verdict + localization, never massaged into a verdict (fp-relabel-homogeneous defeated in BOTH directions)."

conventions:
  - "natural units; decisive arithmetic EXACT over Q (sympy.Rational/Matrix, exact_qq_rank DomainMatrix-over-QQ); 0 numpy float-rank / octonion_algebra on the decisive path"
  - "F_4 = inner_derivations() (52); E_6 = Stab(det); e_6 = f_4 + L(h_3(O)_traceless), dim 78 = 52+26 (Koecher-Tits)"
  - "E_11 = diag(1,0,0); Peirce V_1[0](1) + V_0[1..10](10)=h_2(O) + V_{1/2}[11..26](16) (VERIFIED via L_E11 spectrum)"
  - "det_3 = engine SSOT (LOCK 0 byte-identity); cone metric g_X = Hess(-log det); II=0 <=> totally geodesic (Gauss)"
  - "dim Stab_{E_6}(E_11) = ker{D -> D . E_11} = 78 - dim(orbit of E_11)"

plan_contract_ref: ".gpd/phases/71-a-homogeneity-kill-gate/71-02-PLAN.md#/contract"
contract_results:
  claims:
    claim-homogeneity:
      status: partial
      summary: "Route 2 (stabilizer transitivity) + CALC-02 (II), both on the FULL V_0 family, computed EXACT over Q. dim Stab_{E_6}(E_11) = ker{D->D.E_11} = 61 (orbit of E_11 = 17 = affine cone over the Cayley plane OP^2); dim Stab_{V_0} = 45 = Spin(9,1); V_0 orbit 9 < family 10 (trdeg-1 modulus = det_2). CALC-02: II(V_0)=0 (totally geodesic) at >=2 positive-cone basepoints, II(h_2(C_u))=0, II!=0 with a V_1/2 matter direction. The FINAL reconciliation finds the three decisive measurements DISAGREE (CALC-02 II=0 KILL-signal vs Route-1 SURVIVES); per test-two-route-agreement, agreement is PART OF THE PASS CONDITION, so NO Phase-71 verdict is emitted -- the plan STOPS and LOCALIZES (matter-vs-geometry split, the Phase-72 question). status=partial because the claim's binary SURVIVES/DEAD verdict is intentionally NOT emitted on disagreement, per the contract."
      linked_ids: [deliv-phaseA, deliv-stabilizer-note, test-homogeneity, test-single-copy-anchor, test-e6-dim, test-two-route-agreement, ref-warm-engine, ref-baez-octonions, ref-kollross-rodriguez-vazquez, ref-faraut-koranyi, ref-52-kkt]
      evidence:
        - verifier: gpd-executor
          method: "exact-over-Q engine gates (python3 code/bulk_geometry_verification.py -> ALL_PASS exit 0, 41/41 PASS, deterministic run1==run2): single-copy anchor 24/Spin(8)28/trdeg3 (exact_qq_rank, 3 octonionic-int pts); dim e_6=78=52+26 (span rank over Q); dim Stab_E6(E_11)=ker{D->D.E_11}=61 (orbit of E_11=17 via Matrix.rank AND nullspace); dim Stab_{V_0}=45=Spin(9,1); V_0 orbit=9<10 (MAX over 2 generic octonionic-int V_0 pts); II(V_0)=0 & II(h_2(C_u))=0 at positive-cone basepoints (det_3>0, dim_normal=17), II(V_0+V_1/2 matter)!=0"
          confidence: high
          claim_id: claim-homogeneity
          deliverable_id: deliv-stabilizer-note
          acceptance_test_id: test-homogeneity
          reference_id: ref-warm-engine
          evidence_path: "code/bulk_geometry_verification.py (Section 13 + main() Phase-71-02 gates; commit 2b4fde36)"
  deliverables:
    deliv-phaseA:
      status: partial
      path: derivations/71-homogeneity-stabilizer.tex
      summary: "The SHARED Phase 70+71 deliverable. must_contain coverage: (1) dim Stab_{E_6}(E_11) and the (basepoint,slice)-family dim modulo it -- PRESENT exact over Q (Stab=61; Stab_{V_0}=45=Spin(9,1); V_0 orbit 9<10). (2) the FINAL reconciled two-route verdict + the totally-geodesic II shortcut -- PRESENT as a DISAGREEMENT -> no-verdict + localization (the honest computed outcome; agreement is part of the pass condition and does not hold). (3) explicit 'route dead. STOP.' if homogeneous -- N/A: the matterless-geometry KILL signal (II=0) is stated explicitly, but the BINARY verdict is withheld on disagreement (NOT relabeled). (4) Cayley-Hamilton + multiplicativity reaffirmation of the cubic-norm cross-term (LOCK 7a/7b) BEFORE the group build -- PRESENT (engine LOCK 7a/7b reaffirmed first). status=partial: the binary homogeneity verdict is deferred pending the matter-vs-geometry resolution (Phase 72), per the disagreement handling."
      linked_ids: [claim-homogeneity, test-homogeneity, test-two-route-agreement]
    deliv-stabilizer-note:
      status: passed
      path: derivations/71-homogeneity-stabilizer.tex
      summary: "Route-2 + CALC-02 write-up: the e_6=f_4+L(traceless) build (dim 78); the single-copy anchor (orbit 24/Spin(8)28/trdeg3); dim Stab_{E_6}(E_11)=ker{D->D.E_11}=61 and the (basepoint,slice)-family dim modulo it (Stab_{V_0}=45=Spin(9,1), V_0 orbit 9<10); the second fundamental form II of V_0 (II=0 totally geodesic, OVERTURNING the KRV Table-7 absence-inference via the DIRECT computation); and the final two-route reconciliation (DISAGREEMENT => no verdict + localization). All required literal tokens present: 'e_6 = f_4 + L(h_3(O)_traceless), dim 78 = 52 + 26', 'dim Stab_{E_6}(E_11) = ker{D -> D . E_11}', 'second fundamental form II', 'two-route agreement'. LaTeX balanced (braces 224/224, $ even 288, begin==end 3/3); fragment lint (no pdflatex in env, mirroring 52-kkt / 71-01)."
      linked_ids: [claim-homogeneity, test-single-copy-anchor, test-e6-dim, test-homogeneity, test-two-route-agreement, ref-warm-engine, ref-baez-octonions, ref-kollross-rodriguez-vazquez]
  acceptance_tests:
    test-single-copy-anchor:
      status: passed
      summary: "Single-copy F_4 calibration anchor REPRODUCED on this engine's f_4=inner_derivations(): orbit 24 / Spin(8) stabilizer 28 / trdeg 3, exact over Q, MAX over 3 generic octonionic-integer points (all =24; each validated by _is_genuinely_octonionic_integer). Computed via exact_qq_rank (DomainMatrix-over-QQ, watchdog-safe) on a 52-independent f_4 basis (exact rref). The orbit/stabilizer builder is CERTIFIED before the E_11 count."
      linked_ids: [claim-homogeneity, deliv-stabilizer-note, ref-warm-engine]
    test-e6-dim:
      status: passed
      summary: "dim e_6 = 78 = 52 + 26 VERIFIED as an exact span rank over Q (span_rank_over_QQ of the 52 f_4 generators + 26 L(traceless) acting on the 27). The assembled Lie algebra is genuine E_6 (Koecher-Tits). Traceless basis: {E_1-E_0,E_2-E_0} (2 traceless diagonal) U {E_3..E_26} (24 off-diagonal)."
      linked_ids: [claim-homogeneity, deliv-stabilizer-note, ref-baez-octonions]
    test-homogeneity:
      status: partial
      summary: "(a) dim Stab_{E_6}(E_11) = ker{D->D.E_11} = 78 - rank[D.E_11] = 61 EXACT over Q (orbit of E_11 = 17 = affine cone over OP^2; two routes -- Matrix.rank and nullspace -- agree; all 61 Stab gens annihilate E_11). (b) the (basepoint,slice)-family dim modulo the stabilizer: Stab_{V_0} (slice-preserving) = 45 = Spin(9,1); V_0 orbit = 9 < family 10 (MAX over 2 generic octonionic-int V_0 pts); trdeg-1 modulus = det_2 (the symmetric-space leaves are homogeneous, orbit 9 = leaf dim 9). (c) II of the FULL V_0: II(V_0)=0 (TOTALLY GEODESIC) at >=2 positive-cone basepoints AND II(h_2(C_u))=0; II!=0 once a V_1/2 matter direction is added (V_0-inside-larger-geodesic ruled out by the direct II + the sub-Jordan-algebra structure). DECISIVE Route-2+II results, exact over Q. BUT they do NOT AGREE with Plan 71-01's curvature verdict (II=0 KILL-signal vs Route-1 SURVIVES) => per test-two-route-agreement the pass condition (agreement) FAILS, so NO binary verdict is emitted; the plan STOPS and localizes. status=partial (decisive computations done; the binary KILL/SURVIVES verdict withheld on disagreement, as the contract requires)."
      linked_ids: [claim-homogeneity, deliv-phaseA, deliv-stabilizer-note, ref-warm-engine, ref-kollross-rodriguez-vazquez]
    test-two-route-agreement:
      status: failed
      summary: "AGREEMENT IS PART OF THE PASS CONDITION and DOES NOT HOLD. Route-1 (curvature, 71-01) = SURVIVES; CALC-02 II(V_0)=0 => totally geodesic => homogeneous => KILL signal; Route-2 stabilizer transitivity on V_0 (Stab_{V_0}=Spin(9,1), orbit 9<10) is consistent with II=0 (the 1 modulus is the radial det_2; the symmetric-space leaves are homogeneous). The three do NOT give the same KILL/SURVIVES verdict. Per the contract, on DISAGREEMENT the plan STOPS and LOCALIZES the error, emitting NO verdict. LOCALIZED: curvature-vs-II disagreement (NOT Riemannian-vs-Lorentzian) => the routes probe DIFFERENT submanifolds -- the matterless V_0/h_2(C_u) geometry is totally geodesic/homogeneous (KILL signal), while Route-1's SURVIVES is sourced ENTIRELY by V_1/2/V_1 MATTER off-center-ness (the Phase-72 matter-sourcing question), NOT pure-geometry inhomogeneity. status=failed denotes the agreement test did not pass (=> no verdict); this is the contract-specified handling, NOT an engine failure (the engine gates that DETECT and LOCALIZE the disagreement all PASS, ALL_PASS exit 0)."
      linked_ids: [claim-homogeneity, deliv-phaseA, deliv-stabilizer-note, test-homogeneity, test-single-copy-anchor]
  references:
    ref-warm-engine:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "code/orbit_dimension_gate.py machinery (single_copy_orbit_rank pattern, exact_qq_rank, span_rank_over_QQ, _is_genuinely_octonionic_integer, _select_independent_basis, SINGLE_COPY_POINTS) REUSED VERBATIM for the calibration anchor + all decisive ranks; code/bulk_geometry_verification.py (det_3 SSOT, jordan_L_matrix, inner_derivations, _standard_basis_27, _flat27, Peirce maps, the Totaro engine) EXTENDED (Section 13), not rebuilt. orbit_dimension_gate imports ring_lemma_verification (the SSOT this engine's det_3 is byte-identical to, LOCK 0), NOT octonion_algebra. Engine stays ALL_PASS exit 0; source guard PASS."
    ref-baez-octonions:
      status: completed
      completed_actions: [cite, use]
      missing_actions: []
      summary: "Baez, The Octonions (2002): e_6 = f_4 + L(h_3(O)_traceless), dim 78 (Koecher-Tits) -- the build verified dim 78=52+26 over Q. E_6 = Stab(det). SL(2,O) ~ Spin(9,1) -- the expected Levi of Stab_{E_6}(E_11), RECOVERED EXACTLY as the slice-preserving subgroup dim Stab_{V_0}=45=dim Spin(9,1). OP^2 = F_4/Spin(9) -- the Cayley plane, whose affine cone (dim 17) is the orbit of the primitive idempotent E_11."
    ref-kollross-rodriguez-vazquez:
      status: completed
      completed_actions: [cite, compare]
      missing_actions: []
      summary: "KRV Table 7 (maximal totally-geodesic submanifolds of E_{6(-26)}/F_4): V_0=h_2(O) slice ABSENT from the maximal list => the literature INFERENCE leans non-geodesic/GREENLIGHT. The DIRECT II computation (CALC-02) OVERTURNS this inference: II(V_0)=0 => V_0 IS totally geodesic (a sub-Jordan-algebra sub-cone, Faraut-Koranyi; absent from the MAXIMAL list because it is contained in a larger geodesic structure / is itself a sub-cone, not because it is non-geodesic). The research explicitly placed the decisive weight on the direct computation (its WebFetch returned only the abstract, not the table) -- so the overturn is by the intended decisive route. V_0-inside-larger-geodesic-submanifold is addressed: the direct II=0 (not the absence-inference) is what decides, and the sub-Jordan-algebra structure explains the geodesy."
    ref-faraut-koranyi:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Faraut-Koranyi, Analysis on Symmetric Cones: the det=1 hypersurface is the Riemannian symmetric space E_{6(-26)}/F_4 (homogeneous, parallel curvature) -- the AMBIENT whose constant curvature the totally-geodesic V_0 inherits (Gauss with II=0). Also the sub-Jordan-algebra => totally-geodesic sub-cone theorem that EXPLAINS II(V_0)=0 (V_0=h_2(O) is a sub-Euclidean-Jordan-algebra). Cited in deliv-stabilizer-note."
    ref-52-kkt:
      status: completed
      completed_actions: [read, use, cite]
      missing_actions: []
      summary: "52-kkt: the slice frame h_2(C_u) ~ R^{3,1}, index map {17,18,19,26}=={x1,x2,x3,x10} (engine V_0 indices [1,2,3,10]); the V_0=h_2(O) (10-dim) Peirce slice with E_11 fixed. Defines the (basepoint,slice) family Route 2 measures the transitivity of and the V_0 submanifold whose II is computed. Used + cited."
  forbidden_proxies:
    fp-relabel-homogeneous:
      status: rejected
      notes: "Defeated in BOTH directions. (a) The matterless II=0 (homogeneous V_0) KILL signal is reported HONESTLY and explicitly, NOT relabeled as 'approximately position-dependent'. (b) The Route-1 SURVIVES is NOT manufactured into a false KILL by gauging with a non-Stab element: the transitivity test uses ONLY the RESIDUAL Stab_{V_0} (the slice-preserving subgroup of Stab_{E_6}(E_11)), and fixing E_11 BREAKS transitivity to Stab_{V_0}=Spin(9,1) (orbit 9<10). (c) On the genuine DISAGREEMENT, NO verdict is forced -- the plan STOPS and localizes, exactly as the contract requires (no over-symmetrizing, no softening either way)."
    fp-coordinate-curvature:
      status: rejected
      notes: "Route 2 is purely group-theoretic (exact ranks of infinitesimal actions -- dim Stab, dim orbit -- NOT metric components), immune to the component/chart trap. CALC-02 rests on the Gauss equation via the INTRINSIC second fundamental form II^n_{bc}=(1/2)f_{abc}n^a (a g-normal contraction of the cubic structure tensor f, NOT raw metric components); the totally-geodesic question is the algebraic vanishing of II, not a reading of varying g components. The decisive arena is the Peirce structure (V_0 vs matter), expanded in the off-center/Peirce content, NOT the spacetime coordinate x."
    fp-float-decisive:
      status: rejected
      notes: "Every decisive rank EXACT over Q: dim e_6 (span_rank_over_QQ), dim Stab (exact_qq_rank DomainMatrix-over-QQ + nullspace), Stab_{V_0} (nullspace), V_0 orbit (exact_qq_rank), the single-copy anchor (exact_qq_rank). II is exact over Q (sympy Rational/cancel on the cubic tensor and the normal-space nullspace). The module-local exact-only source guard reports 0 octonion_algebra imports and 0 numpy.linalg.matrix_rank calls on the decisive path (PASS). Float appears nowhere on the decisive path."
  uncertainty_markers:
    weakest_anchors:
      - "The KRV Table-7 inference is OVERTURNED by the direct II computation (II(V_0)=0 => totally geodesic), as the research anticipated (decisive weight on the direct computation, not the abstract-only WebFetch). The geodesy is independently corroborated by the Faraut-Koranyi sub-Jordan-algebra theorem (h_2(O) is a sub-Euclidean-Jordan-algebra => its sub-cone is totally geodesic) AND by the 71-01 H^3 K=-1/2 being CONSTANT. Confidence HIGH that II(V_0)=0; the residual uncertainty is interpretive (matter-vs-geometry), resolved in Phase 72."
      - "dim Stab_{E_6}(E_11)=61 (not ~45): the ~45 guide is the Levi Spin(9,1), RECOVERED as Stab_{V_0}; 61 is the full parabolic of the cone point, corroborated by orbit of E_11 = 17 = dim affine cone over OP^2 (textbook). The build passed test-e6-dim (78) and the single-copy anchor (24/28/3), so the e_6 build and action are certified."
    disconfirming_observations:
      - "HIT and HONORED: 'II=0 (totally geodesic) while Route 1 reported SURVIVES => contradiction via Gauss => localize the error before any verdict.' NO Phase-71 verdict emitted; the localization (curvature-vs-II = matter-vs-geometry split) is returned. NOT a Riemannian-vs-Lorentzian disagreement (both pictures agree on matter-sources-curvature) => NOT a return-to-Phase-70."
      - "Did NOT fire: single-copy anchor != 24/28/3 (it reproduced exactly) -> builder OK."
      - "Did NOT fire: dim e_6 != 78 (it is 78) -> f_4+L(traceless) assembly OK."
      - "Did NOT fire: II of the pure spacetime sub-slice non-constant (h_2(C_u) is totally geodesic, II=0, consistent with the 71-01 H^3 constant K=-1/2)."
      - "g-degeneracy localized: pure-V_0 (alpha=0) basepoints give a SINGULAR g (det_3=0, cone boundary, dim_normal=26, nan); the FIX (positive-cone basepoints, det_3>0, dim_normal=17) is recorded and is the reason II is evaluated at I/3 and a positive V_0-perturbed point, NOT at pure-V_0 points."
    competing_explanations:
      - "Apparent paradox (II=0 'homogeneous' vs Stab_{V_0} orbit 9<10 'non-transitive') RESOLVED: V_0 as a 10-dim CONE is not Spin(9,1)-homogeneous (the radial det_2 is a modulus), but each det_2=const LEAF (9-dim symmetric space) IS homogeneous (orbit 9 = leaf dim 9); totally geodesic V_0 = cone over a homogeneous symmetric space. Fully consistent."

comparison_verdicts:
  - subject_id: test-two-route-agreement
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: cross_method
    metric: same_verdict_all_routes
    threshold: "Route-1 curvature, Route-2 stabilizer transitivity, and CALC-02 II ALL give the SAME KILL/SURVIVES verdict => emit the reconciled verdict; if they DISAGREE => STOP, localize, emit NO verdict"
    verdict: fail
    recommended_action: "STOP and return to the orchestrator with NO Phase-71 verdict. The disagreement is curvature-vs-II (CALC-02 II(V_0)=0 KILL-signal vs Route-1 SURVIVES), NOT Riemannian-vs-Lorentzian => investigate the matter-vs-geometry split (do NOT return to Phase 70). Resolution: determine in Phase 72 whether the inherited spacetime curvature is genuinely SOURCED by V_1/2/V_1 matter (Route-1's SURVIVES, II!=0 with matter) on top of the homogeneous matterless V_0 geometry (II=0). Do NOT auto-greenlight Phase 72 and do NOT declare the milestone KILL: the binary verdict is withheld pending this resolution."
    notes: "The agreement test did not pass (agreement is PART OF THE PASS CONDITION). The math is consistent; the routes probe different submanifolds. The engine gates that DETECT and LOCALIZE the disagreement all PASS (ALL_PASS exit 0); 'fail' here means the two-route AGREEMENT (and hence the binary verdict) is not established, exactly the contract-specified disagreement handling."
  - subject_id: test-homogeneity
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: other
    metric: exact_dimension_counts_over_Q
    threshold: "dim Stab_{E_6}(E_11), the (basepoint,slice)-family dim modulo it, and II(V_0) computed EXACT over Q; Route-2 verdict (orbit=family => KILL / orbit<family => SURVIVES) and II verdict (II=0 => KILL / II!=0 => SURVIVES) stated"
    verdict: pass
    recommended_action: "Carry the decisive exact-over-Q facts (Stab=61, Stab_{V_0}=45=Spin(9,1), V_0 orbit 9<10, II(V_0)=0, II!=0 with matter) into the Phase-72 matter-vs-geometry resolution. The Route-2 transitivity result and the II result are individually decisive and mutually consistent (totally-geodesic V_0 = cone over a homogeneous symmetric space); they only 'disagree' with Route-1 because Route-1 loaded matter into the basepoints."
    notes: "The decisive computations are DONE and exact over Q (this verdict=pass for the computation); the BINARY homogeneity verdict is withheld at test-two-route-agreement (disagreement). orbit of E_11 = 17 = dim affine cone over the Cayley plane OP^2 (two rank routes agree); Stab_{V_0}=45 recovers the Levi Spin(9,1)."
  - subject_id: test-single-copy-anchor
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-warm-engine
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "single-copy F_4 orbit dim == 24, Spin(8) stabilizer == 28, trdeg == 3 (exact over Q)"
    verdict: pass
    recommended_action: "The orbit/stabilizer builder is CERTIFIED -> the E_11 stabilizer count (and Stab_{V_0}, V_0 orbit) are trustworthy. No re-calibration (backtracking trigger did NOT fire)."
    notes: "orbit 24 / Spin(8) 28 / trdeg 3 reproduced via exact_qq_rank (DomainMatrix-over-QQ), MAX over 3 generic octonionic-integer points (each =24, all validated by _is_genuinely_octonionic_integer). Watchdog-safe (exact_qq_rank ~0.01s vs ~55s/pt dense Matrix.rank); identical exact rational result."
  - subject_id: test-e6-dim
    subject_kind: acceptance_test
    subject_role: decisive
    reference_id: ref-baez-octonions
    comparison_kind: benchmark
    metric: exact_equality_over_Q
    threshold: "dim e_6 == 78 == 52 + 26 (exact span rank over Q)"
    verdict: pass
    recommended_action: "The assembled e_6 is genuine E_6 -> the Stab_{E_6}(E_11) kernel computation rests on a correct algebra. No fix needed."
    notes: "span rank over Q of (52 f_4 = inner_derivations + 26 L(traceless)) acting on the 27 == 78. Traceless basis {E_1-E_0,E_2-E_0} U {E_3..E_26}."
  - subject_id: ref-kollross-rodriguez-vazquez
    subject_kind: reference
    subject_role: decisive
    reference_id: ref-kollross-rodriguez-vazquez
    comparison_kind: prior_work
    metric: totally_geodesic_yes_no
    threshold: "KRV Table 7 (maximal totally-geodesic submanifolds of E_{6(-26)}/F_4): V_0=h_2(O) ABSENT => the INFERENCE leans non-geodesic. The DIRECT II computation (CALC-02) is decisive: II(V_0)=0 (exact over Q, >=2 positive-cone basepoints) => V_0 IS totally geodesic"
    verdict: fail
    recommended_action: "Do NOT rely on the KRV Table-7 absence-inference for the geodesy verdict: the DIRECT II computation OVERTURNS it (V_0 IS totally geodesic, a sub-Jordan-algebra sub-cone per Faraut-Koranyi). The research explicitly placed the decisive weight on the direct computation (its WebFetch returned only the abstract, not the table); use the direct II=0 result. The absence from the MAXIMAL list is consistent with V_0 being a sub-cone contained in a larger geodesic structure, not non-geodesic."
    notes: "verdict=fail denotes the literature INFERENCE (V_0 absent => non-geodesic) is CONTRADICTED by the direct exact-over-Q computation (II(V_0)=0 => totally geodesic). This is the intended decisive route (the research flagged the Table-7 read as MEDIUM-HIGH, abstract-only). Corroborated by Faraut-Koranyi (sub-Jordan-algebra => totally geodesic) and by the 71-01 H^3 K=-1/2 being CONSTANT. This overturn is part of the localization: the matterless V_0 geometry is totally geodesic/homogeneous (KILL signal)."

duration: 41min
completed: 2026-05-30
---

# Phase 71 (A) Plan 02: Route-2 Stabilizer Transitivity + CALC-02 II -- Two-Route Cross-Check Summary

**NO FINAL Phase-71 verdict is emitted: the two-route agreement that is part of the pass condition does NOT hold.** Route 2 (stabilizer transitivity) and CALC-02 (the totally-geodesic second fundamental form II), both on the FULL V_0 family and exact over Q, were computed independently of Plan 71-01's Route-1 SURVIVES. The decisive facts: e_6 = f_4 + L(h_3(O)_traceless), **dim 78 = 52 + 26**; **dim Stab_{E_6}(E_11) = ker{D -> D . E_11} = 61** (the orbit of the primitive idempotent E_11 is 17 = the dimension of the **affine cone over the Cayley plane OP^2**); the slice-preserving subgroup **Stab_{V_0} = 45 = dim Spin(9,1)** (recovering the contract's structural Levi expectation) is **NON-transitive on V_0** (orbit 9 < family 10, the single modulus being the Lorentzian norm det_2); and **II(V_0) = 0 (TOTALLY GEODESIC)** at >= 2 positive-cone basepoints, with **II(h_2(C_u)) = 0** (explaining why the 71-01 H^3 benchmark found CONSTANT K = -1/2), while **II != 0 the moment a V_1/2 matter direction is added**. CALC-02's II=0 OVERTURNS the Kollross-Rodriguez-Vazquez Table-7 absence-inference via the direct computation (V_0 = h_2(O) IS totally geodesic -- a sub-Jordan-algebra sub-cone, Faraut-Koranyi). **The three decisive measurements DISAGREE** (CALC-02 II=0 => KILL signal vs Route-1 SURVIVES); per the contract acceptance test `test-two-route-agreement`, agreement is PART OF THE PASS CONDITION, so the plan **STOPS and LOCALIZES** rather than reporting a verdict. **LOCALIZATION (the mathematics is fully consistent; the routes probe DIFFERENT submanifolds):** the matterless V_0 = h_2(O) geometry and its h_2(C_u) spacetime sub-slice are totally geodesic / homogeneous (a KILL signal), while Route-1's SURVIVES is sourced ENTIRELY by off-center-ness in the V_1/2 / V_1 MATTER directions (where II != 0) -- i.e. the **Phase-72 matter-sourcing question**, NOT a pure-geometry inhomogeneity, and NOT a Riemannian-vs-Lorentzian / Wick artifact (so NOT a return to Phase 70). The engine prints **ALL_PASS, exit 0, 41/41 PASS, deterministic**, with the exact-only source guard PASS (0 octonion_algebra, 0 float-rank); the gates that DETECT and LOCALIZE the disagreement all pass.

## Performance

- **Duration:** ~41 min (heaviest steps: the f_4 build (~0.5s), the e_6 rref basis (~2s), the Stab/orbit ranks (~5s total via exact_qq_rank), and the four II evaluations (~50s total with a shared cached symbolic derivative tensor). The first engine run was killed by the ~150s stream-watchdog mid single-copy anchor (dense Matrix.rank ~55s/pt x 3); FIXED by routing the anchor through exact_qq_rank (DomainMatrix-over-QQ, ~0.01s) and caching the II symbolic derivatives -- the full engine then runs well inside the watchdog, foreground `python3 -u`.)
- **Started:** 2026-05-30
- **Completed:** 2026-05-30
- **Tasks:** 3 (calibration gates; Stab + V_0 orbit + II; final reconciliation) -- all build the two deliverables (Section 13 of the certified engine + derivations/71-homogeneity-stabilizer.tex)
- **Files modified:** 1 extended (`code/bulk_geometry_verification.py`, Section 13), 1 created (`derivations/71-homogeneity-stabilizer.tex`)

## Key Results

- **e_6 = f_4 + L(h_3(O)_traceless), dim 78 = 52 + 26** (exact span rank over Q). f_4 = span(inner_derivations()) (52); L(traceless) = the 26 multiplication operators L_a with Tr a = 0 (basis {E_1-E_0, E_2-E_0} U {E_3..E_26}).
- **dim Stab_{E_6}(E_11) = ker{D -> D . E_11} = 61** EXACT over Q. The orbit of E_11 = rank[D.E_11] = **17 = dim of the affine cone over the Cayley plane OP^2** (E_11 a primitive idempotent on the rank-<=1 minimal-orbit locus); two independent rank routes (Matrix.rank, nullspace) agree; all 61 Stab generators annihilate E_11. [Structural note: the contract's ~45 is the Levi Spin(9,1), recovered below as Stab_{V_0}, NOT the full parabolic 61.]
- **Stab_{V_0} = 45 = dim Spin(9,1)** -- the V_0-slice-preserving subgroup of Stab_{E_6}(E_11); exactly recovers the structural Levi expectation. **V_0 orbit under Stab_{V_0} = 9 < family dim 10** (MAX over 2 generic octonionic-integer V_0 points); trdeg of Stab_{V_0}-invariants on V_0 = 1, the single modulus being det_2 (the radial cone direction Spin(9,1) preserves). The det_2 = const symmetric-space leaves are homogeneous (orbit 9 = leaf dim 9).
- **CALC-02 second fundamental form II of V_0 = 0 (TOTALLY GEODESIC):** via the Hessian-metric shortcut II^n_{bc} = (1/2) f_{abc} n^a (lowered Christoffel Gamma_{a,bc} = (1/2) f_{abc}; g-normal n; no metric inverse; FULL V_0). II(V_0) = 0 at the center I/3 (det_3 = 1/27 > 0, dim_normal = 17) and at a positive V_0-perturbed point (det_3 = 92006/99225 > 0); II(h_2(C_u)) = 0 (=> the 71-01 H^3 K = -1/2 is constant). V_0 = h_2(O) is a sub-Jordan-algebra sub-cone (Faraut-Koranyi). **II != 0** (#nonzero = 17) once a single V_1/2 matter direction is added to the tangent -- MATTER sources extrinsic curvature.
- **FINAL two-route reconciliation: ROUTE DISAGREEMENT => NO verdict.** Route-1 SURVIVES (matter-loaded basepoints) vs CALC-02 II = 0 (matterless V_0 totally geodesic => KILL signal); Route-2 (Stab_{V_0} orbit 9 < 10) is consistent with II = 0 (the 1 modulus is the radial det_2). Per `test-two-route-agreement`, agreement is part of the pass condition; on disagreement the plan STOPS and LOCALIZES. **The localization:** matterless V_0 / h_2(C_u) geometry is homogeneous (KILL signal); Route-1's SURVIVES is sourced ENTIRELY by V_1/2 / V_1 MATTER off-center-ness (Phase-72), NOT pure-geometry inhomogeneity; curvature-vs-II disagreement (NOT Riemannian-vs-Lorentzian) => investigate the matter-vs-geometry split, NOT a return to Phase 70.
- **Engine status:** `python3 code/bulk_geometry_verification.py` -> ALL_PASS, exit 0, **41/41 PASS**, 0 FAIL, deterministic (run1 == run2). Source guard PASS (0 octonion_algebra imports, 0 numpy float-rank on the decisive path); LOCK 0 / 7a / 7b reaffirmed.

## Task Commits

The Section-13 engine extension + derivation were developed and verified as ONE coherent unit (the three tasks' code is interdependent and lives in a single file + main() block), then committed as a single atomic compute commit (DEVIATION from strict per-task commits, organizational only -- see Deviations):

1. **Tasks 1-3 (calibration gates + Stab/orbit/II + reconciliation)** - `2b4fde36` (compute) - `code/bulk_geometry_verification.py` (Section 13: peirce_indices_under_E11, build_e6_generators/basis, e6_dimension, stab_E6_E11, stab_preserving_V0, v0_orbit_under, second_fundamental_form + cached derivative helpers; main() Phase-71-02 gate block) + `derivations/71-homogeneity-stabilizer.tex` (created)

**Plan metadata:** this SUMMARY + LOG + STATE-TRACKING (committed separately).

## Files Created/Modified

- `code/bulk_geometry_verification.py` (extended) - Section 13 (Phase-71-02 Route-2 + CALC-02 engine) ADDED on top of the 70/71-01-certified engine; an `orbit_dimension_gate` import (guarded) added after the sympy import; the Phase-71-02 gate block ADDED to main(). The 70/71-01-certified region is otherwise UNCHANGED (LOCK 0 byte-identity, 7a/7b, the source guard, the Route-1 verdict all still pass).
- `derivations/71-homogeneity-stabilizer.tex` (created) - Route-2 + CALC-02 write-up: the e_6 build (Sec.); the single-copy anchor; dim Stab_{E_6}(E_11) = ker{D->D.E_11} and Stab_{V_0} = Spin(9,1) with the V_0 orbit 9<10 (Sec.); the second fundamental form II (Sec.) with the KRV Table-7 overturn; the final reconciliation (Sec.) with the DISAGREEMENT => no-verdict + localization. All 4 required literal tokens present; LaTeX balanced (braces 224/224, $ even 288, begin==end 3/3). Fragment (no \documentclass), \input-included by the project master.

## Equations Derived

**Eq. (e6-build)** -- the Koecher-Tits Lie algebra (LOCKED token):
$$ \mathfrak{e}_6 = \mathfrak{f}_4 + L\bigl(h_3(\mathbb{O})_{\mathrm{traceless}}\bigr), \qquad \dim 78 = 52 + 26. $$

**Eq. (stab-kernel)** -- the residual symmetry dimension (LOCKED token):
$$ \dim\operatorname{Stab}_{E_6}(E_{11}) = \ker\{D \to D \cdot E_{11}\} = 78 - \operatorname{rank}\bigl[D\cdot E_{11}\bigr] = 78 - 17 = 61. $$

**Eq. (II)** -- the second fundamental form of the Hessian metric (LOCKED token):
$$ \mathrm{II}^n_{bc} = g(\nabla_b\partial_c, n) = \Gamma_{a,bc}\,n^a = \tfrac12\, f_{abc}\, n^a, \qquad b,c \in T,\ n \perp_g T, $$
with $f_{abc} = \partial_a\partial_b\partial_c(-\log\det_3)$. $\mathrm{II}=0 \iff$ totally geodesic $\iff R^{\mathrm{slice}} = R^{\mathrm{ambient}}|_{\mathrm{slice}}$ (Gauss). Computed: $\mathrm{II}(V_0) = \mathrm{II}(h_2(\mathbb{C}_u)) = 0$ at positive-cone basepoints; $\mathrm{II}(V_0 \oplus V_{1/2}) \neq 0$.

## Validations Completed

- **Single-copy anchor (test-single-copy-anchor):** orbit 24 / Spin(8) 28 / trdeg 3, exact over Q, MAX over 3 generic octonionic-integer points (each = 24, all validated by `_is_genuinely_octonionic_integer`), via exact_qq_rank on a 52-independent f_4 basis. PASS (builder CERTIFIED).
- **e_6 dimension (test-e6-dim):** span rank over Q of (52 f_4 + 26 L(traceless)) == 78. PASS.
- **Peirce decomposition:** L_{E_11} diagonal in the engine basis; V_1[0](1) + V_0[1..10](10) + V_{1/2}[11..26](16). Exact over Q. PASS.
- **dim Stab / orbit:** orbit of E_11 = 17 via TWO routes (Matrix.rank == nullspace dim); dim Stab = 61; all 61 Stab gens annihilate E_11. Exact over Q. PASS.
- **Stab_{V_0} / V_0 transitivity:** Stab_{V_0} = 45 = Spin(9,1); preserves V_0 (verified); V_0 orbit 9 < 10. Exact over Q. PASS.
- **II reliability:** evaluated at POSITIVE-cone basepoints (det_3 > 0, dim_normal = 17); pure-V_0 (alpha = 0) correctly excluded (cone boundary, det_3 = 0, g singular, dim_normal = 26, nan -- localized and avoided). PASS.
- **II verdict:** II(V_0) = II(h_2(C_u)) = 0 at >= 2 positive-cone basepoints; II != 0 with one V_1/2 matter direction. Exact over Q. PASS.
- **Reconciliation:** the DISAGREEMENT (II = 0 KILL-signal vs Route-1 SURVIVES) is detected; NO verdict emitted; localization returned. The contract's named disconfirming_observation is HIT and HONORED. PASS.
- **Engine regression:** all 70/71-01 LOCKs (0, 1-5, LAYOUT, 7a/7b, exact-only guard, signature-bridge gates, Route-1 verdict) still PASS; OVERALL ALL_PASS exit 0, deterministic.
- **Reproducibility:** SymPy 1.14.0, Python 3.x, NumPy 2.4.2, macOS Darwin 24.6.0; all points hardcoded exact rationals/integers, no random seeds; run1 == run2 byte-identical on the decisive lines.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
| --- | --- | --- | --- |
| II via the Hessian-metric shortcut II^n_{bc}=(1/2)f_{abc}n^a (no metric inverse) | always (g_ij = Hess Phi => Gamma_{a,bc}=(1/2)f_{abc} exactly) | 0 (exact algebraic identity) | never (it is an identity, not a truncation) |
| Evaluate II / orbit ranks at generic rational/octonionic-integer basepoints | always exact over Q; MAX over >=2 generic points (rank lower-semicontinuous) | 0 (exact points) | a non-generic basepoint UNDERESTIMATES; mitigated by MAX over >=2 generic points |
| II evaluated at POSITIVE-cone basepoints only (det_3>0) | the V_0 slice through the positive center I/3 | 0 (exact; g nondegenerate, dim_normal=17) | a pure-V_0 (alpha=0) point is the cone boundary (det_3=0, g singular) -- EXCLUDED (localized) |

No perturbative truncation: all basepoints are exact evaluation points; the orbit/Stab/II computations are exact algebra.

## Decisions Made

- **NO FINAL Phase-71 verdict (the binary KILL/SURVIVES is withheld on route disagreement)**, per the contract's `test-two-route-agreement` (agreement is part of the pass condition). The disagreement is reported HONESTLY with the localization, NOT massaged into a verdict (fp-relabel-homogeneous defeated in both directions).
- **Localization = matter-vs-geometry split (Phase-72), NOT a Phase-70 Wick artifact.** The matterless V_0 / h_2(C_u) geometry is totally geodesic / homogeneous (II=0); Route-1's SURVIVES is sourced by V_1/2/V_1 matter (II!=0 with matter). Both pictures (Riemannian restriction, Lorentzian bridge) agree on this, so it is NOT a coordinate/Wick artifact.
- **dim Stab_{E_6}(E_11) = 61 reported as decisive (NOT the ~45 guide).** orbit of E_11 = 17 = dim affine cone over OP^2 (corroborated); the Levi Spin(9,1) (~45) is recovered as Stab_{V_0}=45.
- **CALC-02 OVERTURNS the KRV Table-7 inference** via the direct II computation (the research's intended decisive route); V_0 IS totally geodesic (sub-Jordan-algebra sub-cone).
- **EXTEND the certified engine + reuse orbit_dimension_gate machinery; NEVER import octonion_algebra.py.** Source guard PASS.
- **exact_qq_rank for the single-copy anchor + cached II derivatives** (watchdog-safe; exact over Q, not float).

## Deviations from Plan

### Auto-fixed / documented

**1. [Rule 5 - Route disagreement / circuit breaker => NO verdict] The mandatory two-route agreement does NOT hold; the milestone's binary verdict is withheld.**

- **Found during:** Task 3 (final reconciliation).
- **Issue:** The plan/contract's pass condition requires Route-1 (curvature, SURVIVES), Route-2 (stabilizer transitivity), and CALC-02 (II) to AGREE on one KILL/SURVIVES verdict. CALC-02 finds II(V_0) = 0 (totally geodesic => homogeneous => KILL signal), which DISAGREES with Route-1 SURVIVES.
- **Handling (per the contract, NOT a free choice):** `test-two-route-agreement` is explicit -- on disagreement the plan STOPS and LOCALIZES, emitting NO verdict. This is exactly the contract's named `disconfirming_observation` ("II=0 while Route 1 SURVIVES => contradiction via Gauss => localize"). I did NOT emit a verdict; I returned the localization.
- **Localization (the math is consistent):** the routes probe DIFFERENT submanifolds. Matterless V_0/h_2(C_u) is totally geodesic/homogeneous (KILL signal); Route-1's SURVIVES is sourced entirely by V_1/2/V_1 MATTER off-center-ness (II!=0 with matter), the Phase-72 question. Curvature-vs-II disagreement => investigate matter-vs-geometry; NOT Riemannian-vs-Lorentzian => NOT return-to-Phase-70.
- **Surfaced for the orchestrator:** YES (this SUMMARY's one-liner, Key Results, Decisions, the test-two-route-agreement comparison verdict; the engine output prints the localization).

**2. [Rule 4 - Structural note, benign] dim Stab_{E_6}(E_11) = 61, not the ~45 structural guide.**

- **Found during:** Task 2 (Stab kernel).
- **Issue:** The contract's structural sanity guide is "~45 (parabolic, Levi ~ Spin(9,1))". The computed dim Stab_{E_6}(E_11) = 61 (orbit of E_11 = 17).
- **Root cause (verified, benign):** 17 = dim of the affine cone over the Cayley plane OP^2 (E_11 a primitive idempotent on the rank-<=1 minimal-orbit locus) -- a textbook number, confirmed by two independent rank routes. The ~45 is the semisimple Levi Spin(9,1), RECOVERED EXACTLY as the slice-preserving subgroup dim Stab_{V_0} = 45. The full parabolic stabilizer of the cone point is 61. The contract explicitly flagged ~45 as a non-decisive sanity guide.
- **Why not a STOP:** the disconfirming triggers for the e_6 build (test-e6-dim != 78) and the action (single-copy anchor != 24/28/3) did NOT fire (both passed), so the build and action are certified; 61 is the correct decisive value.
- **Committed in:** 2b4fde36.

**3. [Rule 1 - Code/perf fix, documented] First engine run killed by the ~150s stream-watchdog; FIXED.**

- **Found during:** Task 1 (single-copy anchor) -- the first full engine run died mid-anchor (dense Matrix.rank ~55s/pt x 3 points + the 4 II builds at ~62s each redoing the symbolic derivative tensor).
- **Fix:** (a) route the anchor through `exact_qq_rank` (DomainMatrix-over-QQ, ~0.01s; identical exact rational result, NOT a float proxy); (b) cache the symbolic 1st/2nd derivative tensor of -log det_3 module-level (`_ii_d1`/`_ii_d2_col`) so the four II evaluations share one heavy build and only do rational substitution per call; (c) restrict the II computation to the needed entries (tangent columns of g, f_{abc} for b,c in tangent). The full engine then runs well inside the watchdog (foreground `python3 -u`, progress prints between heavy steps).
- **Committed in:** 2b4fde36.

**4. [Process note] Single-file atomic commit instead of strict per-task commits.**

- The Section-13 engine code for all three tasks is interdependent (Task 2 needs Task 1's e_6 build; Task 3 reconciles Task 2's II with Route 1) and lives in one file + one main() block; it was developed and verified as a coherent unit, then committed once (2b4fde36). This is an organizational deviation from "each task committed individually" (Rule 4-style, no scope/correctness impact). Each task's deliverable is nonetheless distinct and fully documented (here, in the LOG, and in the engine gate block).

---

**Total deviations:** 4 documented (1 Rule-5 route-disagreement/no-verdict [the headline outcome]; 1 Rule-4 structural-note benign [Stab=61 vs ~45]; 1 Rule-1 perf/watchdog fix; 1 process note on commit granularity).
**Impact on plan:** the decisive Route-2 + II computations are COMPLETE and exact over Q; the binary milestone verdict is WITHHELD per the contract's disagreement handling, with the localization (matter-vs-geometry, Phase-72) returned. No scope change to the computation; the milestone's go/no-go is deferred pending the matter-vs-geometry resolution.

## Issues Encountered

- **No physics bugs.** The II=0 result was localized through two false starts (a non-V_0 basepoint gave II=0 coincidentally; pure-V_0 basepoints gave a singular g on the cone boundary) to the correct positive-cone evaluation, where II(V_0)=0 is robust, multi-basepoint, and matches the Faraut-Koranyi sub-Jordan-algebra theorem.
- **Tooling:** `pdflatex` not available in the executor environment, so the `.tex` fragment was validated by structural lint (braces 224/224, inline `$` even 288, environments begin==end 3/3), consistent with how the sibling fragments (52-kkt, 71-01) are handled (they are `\input`-included by the project master, compiled elsewhere).
- **Watchdog:** the first full run was killed (~150s silent-compute); fixed (Deviation 3). The fix keeps every decisive step well inside the watchdog.

## Open Questions (handed to Phase 72)

- **THE Phase-72 question (now sharply posed):** is the inherited spacetime curvature genuinely SOURCED by V_1/2/V_1 MATTER (Route-1's SURVIVES; II != 0 with matter) on top of the homogeneous matterless V_0 geometry (II = 0)? The matter-vs-geometry split IS the localization; Phase 72 (matter-sourcing) must resolve whether Route-1's position-dependence is a genuine matter-sourced effect (=> the gravity route lives, conditionally) or an artifact of loading matter into the basepoint comparison (=> the pure-geometry KILL signal dominates).
- Is V_0 = h_2(O) sitting inside a larger totally-geodesic structure (consistent with its absence from the KRV MAXIMAL list)? The direct II = 0 already decides it IS totally geodesic; the absence from the maximal list is then because it is a sub-cone / contained in a larger geodesic structure, not because it is non-geodesic.
- Does the Einstein structure G_mu_nu = kappa T_mu_nu + Lambda g_mu_nu hold once the matter source is identified (Phase 73)?

## Next Phase Readiness

**Phase 72 is NOT auto-greenlit, and the milestone is NOT declared KILL.** The binary Phase-71 verdict is WITHHELD pending the matter-vs-geometry resolution (the route disagreement is the honest computed outcome). The decisive, exact-over-Q facts established here -- dim e_6 = 78, dim Stab_{E_6}(E_11) = 61 (orbit 17 = cone over OP^2), dim Stab_{V_0} = 45 = Spin(9,1), V_0 orbit 9 < 10, II(V_0) = 0 (totally geodesic, matterless), II != 0 with V_1/2 matter -- are the handoff for Phase 72 to decide whether the inherited spacetime curvature is genuinely matter-sourced (route lives) or whether the matterless-geometry homogeneity (KILL signal) dominates. The orbit/stabilizer/II machinery is in the certified engine for reuse. **Recommended orchestrator action:** treat this as a Rule-5 physics redirect -- the milestone's KILL gate is unresolved (NOT passed, NOT failed) and requires the Phase-72 matter-sourcing computation to disambiguate the matter-vs-geometry split before the go/no-go can be called.

## Contract Coverage

- **Claim IDs advanced:** `claim-homogeneity` -> partial (Route-2 + II computed decisively and exact over Q; the binary verdict withheld on disagreement, per the contract).
- **Deliverable IDs produced:** `deliv-phaseA` -> partial (Stab dims + II + reconciliation advanced; binary verdict deferred); `deliv-stabilizer-note` -> derivations/71-homogeneity-stabilizer.tex (passed, all 4 must_contain tokens present).
- **Acceptance test IDs run:** `test-single-copy-anchor` -> passed (24/28/3); `test-e6-dim` -> passed (78=52+26); `test-homogeneity` -> partial (decisive dims + II done; binary verdict withheld at agreement); `test-two-route-agreement` -> failed (agreement does NOT hold => no verdict + localization, the contract-specified disagreement handling).
- **Reference IDs surfaced:** `ref-warm-engine` (read/use/cite); `ref-baez-octonions` (cite/use); `ref-kollross-rodriguez-vazquez` (cite/compare -- OVERTURNED via direct II); `ref-faraut-koranyi` (cite); `ref-52-kkt` (read/use/cite).
- **Forbidden proxies rejected:** `fp-relabel-homogeneous` (defeated both directions: matterless KILL-signal stated honestly, Route-1 SURVIVES not falsely KILLed, disagreement not forced to a verdict), `fp-coordinate-curvature` (group-theoretic ranks + intrinsic II, not components), `fp-float-decisive` (all exact over Q, guard 0/0) -> all rejected.
- **Decisive comparison verdicts:** `test-two-route-agreement` -> fail (decisive; disagreement => no verdict + localization); `test-homogeneity` -> pass (decisive computations done exact over Q); `test-single-copy-anchor` -> pass; `test-e6-dim` -> pass.

---

## Self-Check: PASSED

- All files exist on disk: `code/bulk_geometry_verification.py`, `derivations/71-homogeneity-stabilizer.tex`, `.gpd/phases/71-a-homogeneity-kill-gate/71-02-SUMMARY.md`, `71-02-LOG.md`, `71-02-STATE-TRACKING.md`. OK
- Task commit present in `git log`: `2b4fde36`. OK
- Key result reproduces: `python3 code/bulk_geometry_verification.py` -> `OVERALL: ALL_PASS`, exit 0, **41/41 PASS, 0 FAIL**, deterministic (run1 == run2 on the decisive lines). OK
- Decisive numbers present in engine output: dim e_6 = 78; orbit of E_11 = 17; dim Stab = 61; Stab_{V_0} = 45; V_0 orbit 9 < 10; II(V_0) = 0; II != 0 with matter; "ROUTES DISAGREE ... emit NO Phase-71 verdict". OK
- Convention consistency: one unit system (natural, exact over Q); det_3 SSOT (LOCK 0); Peirce split verified; decisive geometry/group on the SSOT (no octonion_algebra import; guard PASS, 0 float-rank). OK
- Contract coverage: every claim / deliverable / acceptance-test / reference / forbidden-proxy ID from the PLAN contract appears in contract_results; the 4 comparison verdicts (test-two-route-agreement [fail], test-homogeneity, test-single-copy-anchor, test-e6-dim) recorded; the route disagreement is surfaced as a no-verdict + localization, NOT relabeled. OK
- Required literal tokens in the .tex: all 4 present (e_6=f_4+L(...) dim 78=52+26; dim Stab_{E_6}(E_11)=ker{D->D.E_11}; second fundamental form II; two-route agreement). OK

## Validation: PASSED

- Algebraic grading / dimension counts (the "dimensional" check for this pure-algebra phase): dim e_6 = 78 = 52 + 26; orbit of E_11 = 17; dim Stab = 61; Stab_{V_0} = 45; V_0 family = 10, orbit = 9; II tangent/normal dims consistent (V_0: 10/17; h_2(C_u): 4/23). All exact over Q. OK
- Single-copy anchor exact over Q: orbit 24 / Spin(8) 28 / trdeg 3 (MAX over 3 octonionic-int pts). OK
- e_6 dim exact over Q: span rank 78. OK
- II exact over Q: II(V_0) = II(h_2(C_u)) = 0 at positive-cone basepoints; II != 0 with matter; positivity caveat localized (pure-V_0 = cone boundary excluded). OK
- Two-route reconciliation: disagreement DETECTED, NO verdict emitted, localization returned; the contract's disconfirming_observation honored. OK
- Forbidden proxies: fp-relabel-homogeneous (no-verdict + honest localization, both directions), fp-coordinate-curvature (ranks + intrinsic II), fp-float-decisive (exact over Q, guard 0/0) -- all rejected. OK

---

_Phase: 71-a-homogeneity-kill-gate_
_Completed: 2026-05-30_
