# Prior Work: Cartan / MacDowell-Mansouri / Berry-Curvature Gravity on h_3(O)

**Surveyed:** 2026-06-01
**Domain:** Mathematical physics / quantum foundations / information geometry — specifically: MacDowell-Mansouri (MM) / Cartan-geometric formulations of gravity; the quantum geometric tensor (QGT) and its imaginary part (Berry curvature); exceptional Jordan algebra h_3(O), the Cayley plane OP^2 = F_4/Spin(9), and exceptional/octonionic approaches to gravity.
**Milestone:** v18.0 — "Gravity as the curvature of the Peirce-frame (Cartan/MacDowell-Mansouri) connection on h_3(O)" (fresh physics-side route; explicitly NOT lattice/Fisher, NOT det/GST/Weinberg supergravity Lagrangian, NOT v17.0 cone-Hessian symmetric-sector metric).
**Research type:** Literature survey — PRIOR WORK & explicit NOVELTY assessment.
**Confidence:** HIGH on the established-math-to-cite (MM/Cartan, QGT real/imag split, OP^2 = F_4/Spin(9), Peirce tangent identity, all anchored to canonical references with verified bibliographic data); HIGH on the central novelty flags (the located literature does NOT preempt the idempotent-coframe / Berry-curvature-of-OP^2 / MM-from-cubic-norm sub-claims); MEDIUM on completeness of the exceptional-gravity-attempt census (Singh and Castro programs located and characterized decisively; a long tail of vixra/preprint octonion-gravity notes was not exhaustively read).

> **Scope discipline (per prompt).** This file surveys ONLY what bears on the four sub-questions:
> (1) Berry curvature / Im(QGT) of the primitive-idempotent (rank-1 projector) family on OP^2 = F_4/Spin(9) or on exceptional/Jordan projective spaces; (2) MM/Cartan gravity DERIVED FROM h_3(O) / its cubic norm (vs posited as an action); (3) dE of an idempotent/projector field as a soldering form / tetrad, or T_E OP^2 = V_{1/2} identified with a gravitational coframe; (4) Berry curvature / QGT over F_4/Spin(9), OP^2, or rank-1 symmetric spaces, and "emergent gravity from Berry/QGT geometry" programs.
> The two dead in-program routes (det/GST/Weinberg supergravity *Lagrangian*; lattice/Fisher) and the v17.0 cone-Hessian *real-part-QGT* route are NOT cited as load-bearing. The established chain (OP^2=F_4/Spin(9); QGT real=Fubini-Study, imag=Berry; MM=curvature of a broken Cartan connection; h_2(C_u)=R^{3,1}) is taken as **cite-only** standard math.

---

## TL;DR for the roadmapper (read this first)

1. **The "established math to cite" is solid and all references are bibliographically confirmed.**
   OP^2 = F_4/Spin(9) (16-dim, rank-1 symmetric space; Borel); T_E OP^2 = V_{1/2}(E) (Peirce
   half-eigenspace; McCrimmon / Baez); QGT real part = Fubini-Study metric, imaginary part = Berry
   curvature (**Provost & Vallee, Comm. Math. Phys. 76, 289-301 (1980), DOI 10.1007/BF02193559** —
   confirmed exact citation, and they treat exactly the **group-orbit / generalized-coherent-state**
   case relevant here); MM gravity = curvature of a broken de Sitter/Lorentz Cartan connection,
   ∫ε F∧F = Einstein-Hilbert + Λ + topological term (**MacDowell & Mansouri, PRL 38, 739 (1977)**;
   **D. K. Wise, gr-qc/0611154 = Class. Quantum Grav. 27, 155010 (2010)** — confirmed). These are
   cite-not-rederive; the milestone spec already designates them so.

2. **CRITICAL GEOMETRIC SUBTLETY (Phase A / A.5 — verified, load-bearing):** OP^2 = F_4/Spin(9)
   **has NO invariant almost-complex structure, is NOT Hermitian symmetric, and carries NO invariant
   symplectic 2-form** — it is rank-1 and *isotropy-irreducible*, and Spin(9) preserves an invariant
   **8-form** (the analog of the Kähler form), not a 2-form. CONSEQUENCE: the standard machinery
   "Berry curvature of a generalized-coherent-state orbit = the Kirillov-Kostant-Souriau symplectic
   form" (Provost-Vallee for Kähler orbits; Berry-phase-on-homogeneous-Kähler-manifolds literature)
   **does NOT directly apply** to the un-broken primitive-idempotent family on OP^2. A nonzero
   2-form Berry curvature on the 4d slice must come from the **C_u / Spin(9)→Lorentz symmetry
   breaking**, NOT from an invariant structure on OP^2. This *supports* the route's premise that the
   C_u reduction does essential work, but it is also a live failure mode: if the broken structure
   does not produce a well-defined invertible coframe + nonzero Im(QGT), Phase A/A.5 KILLs. **The
   roadmap MUST treat "is Im(QGT) even a nonzero 2-form here, pre/post C_u-breaking?" as an explicit
   Phase-A.5 question, not an assumption.**

3. **The idempotent-coframe sub-claim (dE = V_{1/2}-valued soldering form; T_E OP^2 = V_{1/2} as a
   gravitational coframe) appears GENUINELY NEW.** The tangent identity T_E OP^2 = V_{1/2}(E) is
   standard Jordan-algebra math (cite). "dE of a projector field is a tetrad/soldering form" exists
   as a *generic idea* in emergent-gravity programs (tetrad-as-soldering-form is textbook; tetrad as
   a fermion bilinear / composite is a known emergent-gravity motif), but **no located work builds
   the coframe from dE of a primitive idempotent of h_3(O), nor reduces V_{1/2}(16) via a complex
   structure to a 4d Lorentzian coframe.** This is the novelty core and the Phase-A deliverable.

4. **MM/Cartan gravity has NEVER (in the located literature) been DERIVED FROM the h_3(O) cubic
   norm without positing an action.** Every exceptional/octonionic-gravity program located posits a
   Lagrangian: Singh (trace dynamics — a posited Planck-scale trace Lagrangian, gravity emergent,
   "Lorentz boson"); Castro (a posited E_6(-26)-invariant cubic-form membrane/matrix action); the
   v12/v13 in-program det/GST/Weinberg route (posited N=2 MESGT Lagrangian — the "GST sin"). The MM
   action itself is *always* posited as an SO(4,1)/SO(3,2) Yang-Mills-type action that breaks to
   SO(3,1). **Deriving the MM ε-contraction from the h_3(O) trace-form/cubic-norm (Phase C STRONG
   WIN) is unattested — but so is success; the most likely real outcome is fp-imported-action.**

5. **The closest prior art to "Berry curvature → Lorentz connection of an emergent geometry" is
   Viennot (arXiv:2106.01913):** in BFSS matrix theory, the operator-valued generator of the
   geometric phase of adiabatic transport of a quasi-coherent state IS the (torsionful) Lorentz
   connection of the emergent geometry. This is the *spirit* of the v18.0 route — but in a
   matrix-theory/D-brane setting, with no h_3(O) idempotent, no MM ε-contraction, and no Einstein-
   structure claim. It is a precedent for the mechanism, NOT a preemption of the result.

**Bottom line for novelty:** three of the four sub-claims (idempotent-coframe; Berry-curvature/Im-QGT
of the OP^2 idempotent family; MM-from-cubic-norm) are **candidate-novel** — the located literature
contains the ingredients as standard math but not the assembly. The fourth (emergent-gravity-from-
Berry/QGT as a *program*) is an active, crowded field, so the route is **not** novel as a *philosophy*;
its novelty is the *specific algebraic source* (h_3(O) primitive idempotents + C_u) and the *MM-Einstein*
target. Report at true strength; do not overclaim originality of the QGT-gravity idea itself.

---

## Sub-claim → Source → Novelty map (the table the requirements author asked for)

| Sub-claim (v18.0) | Status | Nearest prior art | Verdict |
| ----------------- | ------ | ----------------- | ------- |
| OP^2 = F_4/Spin(9), 16-dim, rank-1 sym. space | **Standard math — CITE** | Borel 1950; Baez 2002 §3.4 | Not novel (foundation). |
| T_E OP^2 = V_{1/2}(E) (Peirce half-eigenspace); E∘δ=½δ | **Standard math — CITE** | McCrimmon *A Taste of Jordan Algebras*; Baez 2002 | Not novel (foundation). |
| QGT real part = Fubini-Study, imag part = Berry curvature | **Standard math — CITE** | Provost-Vallee 1980 (CMP 76, 289) | Not novel (foundation). |
| MM gravity = curvature of broken Cartan connection; ε F∧F = EH+Λ | **Standard math — CITE** | MacDowell-Mansouri 1977; Wise 2010 | Not novel (foundation). |
| h_2(C_u) ≅ R^{3,1} Lorentzian; so(4,2) conformal | **Internal GPD prior — REUSE** | GPD `52-kkt-spacetime`, `52-observer-uniqueness` | Not novel (established internally). |
| **e := dE of a primitive-idempotent field = V_{1/2}-valued soldering form** | **CANDIDATE-NOVEL** | tetrad-as-soldering-form (textbook); tetrad-as-bilinear/composite (Volovik, Sarfatti, others) — generic, NOT from h_3(O) idempotents | **New in this route** (assembly unattested). |
| **C_u reduction V_{1/2}(16) → 4d Lorentzian coframe carrying SO(3,1), forced by (E_11,u)** | **CANDIDATE-NOVEL** | no located precedent; Spin(9) preserves an 8-form not a 2-form (so the reduction is non-trivial) | **New in this route** — Phase A KILL gate. |
| **Berry curvature / Im(QGT) of the OP^2 = F_4/Spin(9) primitive-idempotent family** | **CANDIDATE-NOVEL (with a sharp caveat)** | Provost-Vallee + KKS symplectic form for *Kähler* coherent-state orbits — but OP^2 is **not Kähler / not symplectic**, so the standard result does NOT cover it | **New + subtle**: must be computed via the C_u-broken structure; not an off-the-shelf KKS form. |
| **MM ε-contraction (Einstein term) FORCED by the h_3(O) trace-form/cubic-norm (no posited action)** | **CANDIDATE-NOVEL / likely-fails** | every located exceptional-gravity program posits an action (Singh, Castro, GST) | **New target**; the most likely real outcome is fp-imported-action (B yes, C no). |
| "Emergent gravity from Berry curvature / QGT geometry" as a *program* | **NOT novel as a philosophy** | Viennot 2106.01913 (Berry→Lorentz connection, BFSS); QGT-curved-space program (2209.07728, 2403.09804); QGT sub-bundle (2503.17163); "kinematic space from modular QGT" (2110.08703) | **Crowded field** — novelty is the *source* (h_3(O)) and the *MM-Einstein* target, not the idea. |

---

## Key Results (with conditions, references, confidence)

| # | Result | Statement / Expression | Conditions | Source | Year | Conf. |
| - | ------ | ---------------------- | ---------- | ------ | ---- | ----- |
| S1 | **OP^2 = F_4/Spin(9)** | The space of rank-1 (primitive) idempotents of h_3(O) is the Cayley plane = F_4/Spin(9); dim = 52 − 36 = 16. Compact rank-1 symmetric space, isotropy-irreducible. | h_3(O) the exceptional (Albert) Jordan algebra; F_4 = Aut(h_3(O)). | Borel 1950; Baez, "The Octonions," Bull. AMS 39 (2002) 145, §3.4 (arXiv math/0105155). | 1950/2002 | HIGH |
| S2 | **T_E OP^2 = V_{1/2}(E)** | At a primitive idempotent E, the tangent space to the idempotent variety is exactly the Peirce ½-eigenspace V_{1/2}(E) (16-dim), where E∘δ=½δ for δ tangent. | Peirce decomposition J = V_1(E) ⊕ V_{1/2}(E) ⊕ V_0(E) at idempotent E. | McCrimmon, *A Taste of Jordan Algebras* (2004), Peirce ch.; Baez 2002 §3.4. | 2004 | HIGH |
| S3 | **QGT split: real=Fubini-Study, imag=Berry** | For a state family \|ψ(x)⟩, Q_{μν} = ⟨∂_μψ\|(1−P)\|∂_νψ⟩ with P=\|ψ⟩⟨ψ\|; Re Q = quantum (Fubini-Study) metric g_{μν}, Im Q = −½ F_{μν} (Berry curvature). The v17.0 cone-Hessian was Re Q; this route mines Im Q. | Pure-state ray family; P rank-1 projector. | Provost & Vallee, Comm. Math. Phys. **76, 289-301 (1980)**, DOI 10.1007/BF02193559. | 1980 | HIGH |
| S4 | **Provost-Vallee treat the group-orbit / coherent-state case explicitly** | They derive the metric and an explicit scalar curvature for submanifolds generated by a Lie-group action on a fixed state (generalized coherent states). | Manifold = G·\|ψ_0⟩ (coherent-state orbit). | Provost-Vallee 1980 (as above). | 1980 | HIGH |
| S5 | **MM gravity = curvature of a broken Cartan connection** | A=ω⊕e valued in so(3,2)/so(4,1)/iso(3,1); F=dA+A∧A: Lorentz block = R(ω)+Λ e∧e (Riemann + cosmological), translation block = de+ω∧e (torsion). The MM action ∫ε_{ABCD} F^{AB}∧F^{CD} = Einstein-Hilbert + Λ + a topological (Euler/Gauss-Bonnet) term after the SO(4,1)→SO(3,1) (or SO(3,2)→SO(3,1)) symmetry breaking. | An SO(4,1)/SO(3,2) Yang-Mills-type **action is posited**; symmetry breaking SO(4,1)→SO(3,1) via so(4,1)≅so(3,1)⊕R^{3,1}. | MacDowell & Mansouri, Phys. Rev. Lett. **38, 739 (1977)**; Wise, gr-qc/0611154 = Class. Quantum Grav. **27, 155010 (2010)**. | 1977/2010 | HIGH |
| S6 | **MM is a *posited* gauge-theory action; the contraction is the input** | "MM model is a Yang-Mills-type gauge theory with gauge group SO(4,1); after SO(4,1)→SO(3,1) the action is classically equivalent to the Palatini action of GR, differing only by a topological term." The Einstein term appears *because* of the specific ε-contraction of the *posited* action. | Vacuum (A)dS; the ε-tensor / broken generators are an external MM choice. | Wise 2010; (formulation reviews) e.g. arXiv:1703.09755, arXiv:2304.05606. | 2010 | HIGH |
| S7 | **MM gauge algebra fixed by conformal structure (relevant to Phase C)** | The MM gauge algebras are uniquely determined by the *conformal* structure for vacuum Lorentzian/Euclidean spacetimes (Wise's conformal-holonomy result). | Vacuum, fixed conformal class. | Wise, "Conformal holonomy in MM gravity"; Wise 2010. | 2010 | MEDIUM |
| S8 | **OP^2 = F_4/Spin(9) is NOT Hermitian symmetric / NOT Kähler / NO invariant 2-form** | The tangent bundle of the Cayley projective plane admits **no almost-complex structure**; OP^2 is rank-1, isotropy-irreducible; Spin(9) preserves an invariant **8-form** (Kähler-form analog), not a 2-form. | Compact real Cayley plane F_4/Spin(9). | Wikipedia "Cayley plane" + the Spin(9)-octonionic-geometry literature (e.g. "The rôle of Spin(9) in Octonionic Geometry," preprints.org 201809.0430); standard symmetric-space classification (Helgason). | — | HIGH |
| S9 | **Berry curvature of *Kähler* coherent-state orbits = KKS symplectic form** | For coherent states over a homogeneous **Kähler** manifold = coadjoint orbit with linear (in generators) Hamiltonian, the geometric phase / Berry curvature is the Kirillov-Kostant-Souriau symplectic 2-form; closed-form expressions exist. **Does NOT cover OP^2 (S8).** | Orbit must be Kähler/symplectic (coadjoint orbit). | Berry-phase-on-homogeneous-Kähler-manifolds (arXiv math-ph/0111022); KKS form (orbit-method literature). | — | HIGH |

---

## Foundational Work (the "cite, do not re-derive" set)

### MacDowell & Mansouri (1977) — gravity as a broken gauge theory
**Key contribution:** Reformulated GR + Λ as a gauge theory of a de Sitter/anti-de Sitter (or Poincaré) connection A=ω⊕e, with the Einstein-Hilbert + cosmological action arising from ∫ε F∧F after breaking SO(4,1)/SO(3,2) → SO(3,1).
**Method:** Posit an SO(4,1)/SO(3,2) Yang-Mills-type action; the ε_{ABCD}-contraction selects the Lorentz block; symmetry breaking yields Palatini GR + Λ + Gauss-Bonnet.
**Limitations / what is *assumed*:** The action and the ε-contraction are **posited**, not derived from a deeper structure. This is exactly the input that Phase C audits (`fp-imported-action`).
**Relevance:** Defines the target object F=dA+A∧A and the contraction whose *origin* the route must justify from h_3(O) to claim a STRONG WIN.

### D. K. Wise (2006/2010) — MacDowell-Mansouri gravity and Cartan geometry **[THE reference for this route]**
**Key contribution:** Gave the clean Cartan-geometric statement: MM gravity = a Cartan connection modeling spacetime on a homogeneous model (de Sitter / anti-de Sitter / Minkowski), "rolling" the model along physical spacetime; unifies ω and e into one connection. Showed the MM gauge algebra is fixed by the conformal structure.
**Method:** Cartan geometry (Sharpe's framework); reductive split g = h ⊕ (g/h) with h = Lorentz, g/h = translations = the soldering form's home.
**Limitations:** Still *posits* the model geometry and the action; does not derive the connection from an algebra of states.
**Relevance:** Supplies the precise definitions Phase B needs (soldering form = the g/h part; curvature blocks; torsion). The reductive split g/h ↔ V_{1/2} is the structural bridge the route asserts.

### Provost & Vallee (1980) — Riemannian structure on manifolds of quantum states
**Key contribution:** Defined the gauge-invariant metric on any submanifold of quantum states from the Hilbert-space inner product (the QGT). Treated the **generalized-coherent-state** case (Lie-group orbit on a fixed state) and gave an explicit scalar curvature.
**Method:** Pull back the Fubini-Study structure; the real part is the metric, the imaginary part (skew) is the Berry curvature.
**Limitations:** Their explicit-curvature results lean on Kähler/orbit structure; the bare framework is general, but a *symplectic* Berry curvature presupposes structure that OP^2 lacks (see S8/S9).
**Relevance:** Defines Im(QGT) = Berry curvature, the half of the QGT the v18.0 route mines (v17.0 used Re(QGT)). The "NONE does not bind it" claim rests on this being a genuinely different tensor — which Provost-Vallee establishes.

### Baez (2002) — "The Octonions"; McCrimmon — *A Taste of Jordan Algebras*
**Key contribution:** Baez §3.4: OP^2 = F_4/Spin(9), T_E OP^2 = V_{1/2}; F_4 = Aut(h_3(O)); E_6(-26) = norm-preserving (collineation) group. McCrimmon: Peirce decomposition, primitive idempotents, the E∘δ=½δ tangent identity.
**Relevance:** The Phase-0 tangent identity (E_11∘δ=½δ; T_{E_11}OP^2 = V_{1/2}(16)) is verbatim from these; cite, do not re-derive.

### Sharpe (1997) — *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program*
**Key contribution:** The rigorous definition of a Cartan connection and soldering form on a principal bundle with a reductive (or parabolic) model G/H.
**Relevance:** Provides the precise meaning of "e=dE is a soldering form" (it must be a bundle isomorphism g/h ≅ TM — i.e. the coframe must be **invertible/non-degenerate**, the Phase B(a) check) and of the structure-group reduction (Phase A(c)).

---

## Prior exceptional/octonionic-gravity attempts (the "already attempted, with what outcome" set)

### Tejinder P. Singh and collaborators — trace dynamics / "spontaneous quantum gravity" / aikyon (2019–2023)
**What was shown:** A unification program on h_3(O) / octonions in which gravitation, Yang-Mills, and fermions arise from a **posited Lagrangian in trace dynamics** at the Planck scale (L = trace of a matrix polynomial of Grassmann-valued "aikyon" matrices). G_2 automorphisms replace diffeomorphisms + internal gauge; three fermion generations from three G_2 ⊂ F_4. Gravity is an **emergent classical phenomenon**; at the Planck scale a quantized Lorentz symmetry is "mediated by a Lorentz boson." Claims a new U(1) gravitational interaction (→ MOND). Key papers: arXiv:2006.16274 (octonions/trace-dynamics/NCG), 2009.05574 (trace dynamics & division algebras), 2104.14344 (ground state), 2304.01213 (EJA & gravitation/weak force), 2308.16216 (gravitation & QT as emergent).
**Conditions / what is *assumed*:** A specific trace-dynamics **action is posited ab initio** ("We have recently proposed a Lagrangian in trace dynamics… for unification of gravitation, Yang-Mills fields, and fermions" — confirmed from the 2009.05574 abstract). Gravity emerges *from that action*, statistically/thermodynamically, below the Planck scale.
**EXACTLY how it differs from this route:** (i) Singh **posits an action**; v18.0 forbids that and audits exactly it in Phase C — Singh's route is, in v18.0's terms, structurally `fp-imported-action`. (ii) Singh uses **G_2** (octonion automorphisms) as the replacement for diffeos; v18.0 uses the **F_4/Spin(9) idempotent geometry** and a **Spin(9,1)→SO(3,1) Cartan/MM** structure. (iii) No located Singh paper builds a **soldering form e=dE from a primitive idempotent field**, nor uses the **Berry curvature / imaginary QGT**; the spacetime/Lorentz content comes from the posited Lagrangian + a "Lorentz boson," not from Im(QGT) of the idempotent family. (iv) Singh's gravity is *emergent/thermodynamic* in flavor — v18.0 explicitly **rejects thermodynamic/ensemble routes** (standing constraint). **Verdict: related program on the same algebra, but a different (posited-action, emergent/thermal) mechanism. Does NOT preempt any v18.0 sub-claim; is itself an instance of the GST sin the route avoids.**
**Caveat:** The 2304.01213 PDF could not be machine-read (compression corruption); characterization is from the confirmed 2009.05574 abstract + multiple search summaries of the program. Confidence HIGH on "posits an action / no idempotent-coframe / no Berry curvature"; the roadmap may wish a human eyeball on 2304.01213 if Phase C needs to cite Singh as contrast.

### Carlos Castro (Perelman) — exceptional Jordan strings/membranes, octonionic gravity/p-branes, EJA matrix models (2000s–2021)
**What was shown:** A membrane moving in a background with an **octonionic-valued metric** has an action invariant under rigid **E_6(-26)** transformations preserving the cubic (volume) form — *replacing* diffeomorphisms. Cubic matrix-Chern-Simons-type actions from the F_4, E_6 Jordan matrix models; large-N limits → Chern-Simons membrane Lagrangians for M-theory in D=27. Key works: "Exceptional Jordan Strings/Membranes and Octonionic Gravity/p-branes"; "Exceptional Jordan Matrix Models, octonionic p-branes and star-product deformations" (J. Geom. Phys. 2021, S0393044021001145).
**Conditions / what is *assumed*:** A **membrane / matrix action is posited**; "gravity" = invariance of that action under E_6(-26) cubic-form transformations.
**EXACTLY how it differs:** Castro **posits a cubic-form-invariant action** (E_6(-26)), exactly the GST-adjacent move v18.0 forbids; no idempotent soldering form; no Berry curvature / QGT; no MM/Cartan ω⊕e connection; no Einstein-structure derivation. The cubic form enters as an *invariance of a posited action*, not as the *source of a connection curvature*. **Verdict: uses the same h_3(O)/E_6(-26) cubic-norm ingredient but in a posited-action membrane setting; does NOT preempt the connection-curvature/Berry-curvature sub-claims. This is the same category the v17.0 PRIOR-WORK already flagged as a different (rejected) route.**

### In-program det/GST/Weinberg N=2 MESGT route (v12/v13; GPD phases 47–50, 53) — DEAD/circular
**What was shown (internal):** h_3(O) → Peirce V_0 → π_u → R^{3,1} → det(X) prepotential → N=2 MESGT (GST classification) → Weinberg 1964 forces −R/2.
**Why excluded:** Circular — the −R/2 Einstein term is the assumed N=2 multiplet's own output (`fp-imported-action`). Gunaydin-Sierra-Townsend (1983-84) geometry (E_6(-26)/F_4) is citable for orientation **only**; their Lagrangian is the dead route.
**Relevance:** This is the canonical example of the failure mode Phase C must avoid; v18.0's whole point is to get the Einstein term WITHOUT positing such an action.

### v17.0 cone-Hessian intrinsic-bulk-geometry route — CLOSED, verdict NONE
**What was shown (internal):** g = η+h on the h_2(C_u) slice (cone-Hessian = matter source, not metric); position-dependent (homogeneity SURVIVES), ~94% matter-sourced, but the full nonlinear G[g] is NOT of Einstein form for any global (κ,Λ) — **NONE: curved but not Einstein-structured**.
**Relevance:** This computed **Re(QGT)** (Fubini-Study / cone-Hessian). v18.0 computes **Im(QGT)** (Berry curvature) — a *different tensor* (S3), so the NONE verdict does not bind it. BUT Phase A.5 must explicitly check the **same-wall** failure: does the matter-sourced Im(QGT) inherit the cone-Hessian's mismatch (support disjoint from T[M]; ~10^3 magnitude/shape mismatch; no M-power match)? The v17.0 result is the consistency anchor (Re(QGT) must reproduce Hess(−log det)) AND the cautionary precedent.

---

## Berry-curvature / QGT "emergent gravity" programs (sub-question 4 — the crowded field)

### Viennot (2021) — "Emergent gravity and D-brane adiabatic dynamics: emergent Lorentz connection" (arXiv:2106.01913) **[closest mechanism precedent]**
**What was shown:** In BFSS matrix theory, adiabatic transport of a quasi-coherent state of a fermionic string yields an **emergent Lorentz connection** = the operator-valued generator of the geometric (Berry) phase; the shift vector of the spacetime foliation is the Berry-phase generator; the connection is **not torsion-free** at the microscopic scale (Berry curvature ↔ pseudo-magnetic field / torsion).
**Conditions:** BFSS/matrix-theory background; quasi-coherent states; weak adiabatic transport.
**EXACTLY how it differs:** Same *idea* (geometric-phase generator = Lorentz connection of an emergent geometry) but (i) source is **matrix theory / D-branes**, not h_3(O) primitive idempotents; (ii) no MM ε-contraction, no Einstein-structure claim, no cubic-norm; (iii) torsionful by construction. **Verdict: the strongest precedent for "Berry → Lorentz connection," so v18.0 is NOT philosophically novel here; the novelty is the algebraic source (h_3(O)) and the MM-Einstein target. CITE as precedent + intellectual honesty.**

### QGT-in-curved-parameter-space program (Gonzalez, et al.) — arXiv:2209.07728 (Symmetry 2022), arXiv:2403.09804
**What was shown:** A QGT defined on a curved parameter space with a parameter-dependent metric; the symmetric part = quantum metric, antisymmetric part = Berry curvature, with corrections proportional to derivatives of the metric determinant. "The quantum metric resembles gravity — it determines how space bends around electrons."
**Differs:** Generic parameter-space framework; no exceptional algebra, no idempotent field, no MM. Relevant for *how* to define Im(QGT) when the base carries its own (Lorentzian) metric — useful Phase A.5/B methodology.

### QGT from sub-bundle geometry — Lim/Hughes et al., arXiv:2503.17163 = Quantum 8, ... (q-2026-01-14-1965)
**What was shown:** General connection on a Hermitian vector bundle + a sub-bundle projector; **shape operators** fully determine the QGT, with a geometric decomposition QGT = quantum metric + Berry curvature + **bundle curvature** (generalized Gauss-Codazzi-Mainardi). Worked example: Dirac fermions on a hyperbolic plane.
**Differs:** General framework; worked example is a hyperbolic plane, NOT OP^2/F_4 or any exceptional/symmetric coset; no octonions/Jordan algebra. **Relevant as the cleanest modern *machinery* for computing Im(QGT) of a projector sub-bundle with an extrinsic (shape-operator / Gauss-Codazzi) contribution — which is exactly the structure of a V_0-sub-slice inside OP^2.** Recommend the roadmap consider this framework for Phase A.5/B.
**Note (Gauss-Codazzi parallel):** The v17.0 PRIOR-WORK already flagged that the V_0 slice is plausibly *non-totally-geodesic* inside E_6/F_4 (Kollross–Rodríguez-Vázquez classification). The sub-bundle shape-operator decomposition (2503.17163) is the QGT-side analog: the slice's Im(QGT) will pick up a bundle/shape-operator term. This is a methodological gift, not a result.

### "Kinematic space from quantum modular geometric tensor" — arXiv:2110.08703
**What was shown:** A modular (Tomita-Takesaki) version of the QGT whose geometry reproduces a kinematic/auxiliary "spacetime."
**Differs + EXCLUDE as load-bearing:** This is a **modular/thermal** construction — squarely inside the rejected Connes-Rovelli/thermal-time class (standing constraint: no entropy/KMS/modular/thermal-time arguments). **Do NOT cite as load-bearing; note only as a contrast that the v18.0 route deliberately avoids the modular flavor.**

---

## Novelty Assessment (per sub-claim — the load-bearing section for the requirements author)

### Sub-claim N1: e := dE of a primitive-idempotent field of h_3(O) is a V_{1/2}-valued soldering form / coframe
- **Standard-math content (cite):** T_E OP^2 = V_{1/2}(E), E∘δ=½δ (S2; McCrimmon, Baez); "tetrad = soldering form" (Sharpe; textbook); "tetrad as a composite/bilinear field" is a known emergent-gravity motif (Volovik-style effective gravity; tetrad-from-fermion-bilinear; tetrad-spin-connection gauge gravity).
- **Genuinely new:** Building the soldering form as **dE of a primitive idempotent of the exceptional Jordan algebra**, with the coframe valued in the Peirce V_{1/2}(E). No located work does this. The generic "dProjector is a frame" idea exists in spirit, but not from h_3(O) idempotents, and not tied to V_{1/2}.
- **VERDICT: CANDIDATE-NOVEL.** Absence of prior art (after targeted searches on "tetrad from projector/idempotent field," "Peirce V_{1/2} as coframe," "Cayley plane tangent as gravitational coframe") = candidate novelty. Phase A(a) deliverable. **Failure mode to watch:** the coframe must be **non-degenerate/invertible** (Sharpe's soldering-form condition; Phase B(a)) — a "soldering form" that is not a bundle isomorphism is not a tetrad.

### Sub-claim N2: C_u reduction of V_{1/2}(16) → a 4d Lorentzian coframe carrying SO(3,1), forced by (E_11,u)
- **Standard-math content (cite/reuse):** The Phase-46 π_u C_u bottleneck sending V_0 = h_2(O) → h_2(C_u) ≅ R^{3,1} (internal GPD `52-kkt-spacetime`). The *parallel* reduction on V_{1/2} is the new step.
- **Genuinely new:** No located precedent reduces the 16-dim Peirce ½-space to a 4d Lorentzian coframe via a complex structure u=e_7.
- **Sharp caveat (S8):** OP^2 carries **no invariant 2-form/complex structure** — so the 4d Lorentzian + SO(3,1) structure cannot be inherited from an invariant structure on OP^2; it must be *forced by the broken pair (E_11,u)*. This is consistent with the route's logic but is precisely where `fp-arbitrary-reduction` lurks: if the 4d slice or its Lorentzian signature requires a choice beyond (E_11,u), the Phase-A KILL fires.
- **VERDICT: CANDIDATE-NOVEL; the Phase-A KILL gate.** Expected (by analogy to V_0): image dim 4, signature (1,3), forced. Must be computed exact-over-Q, not assumed.

### Sub-claim N3: Berry curvature / Im(QGT) of the OP^2 = F_4/Spin(9) primitive-idempotent (rank-1 projector) family
- **Standard-math content (cite):** Im(QGT) = Berry curvature (S3); for **Kähler** coherent-state orbits, Im(QGT) = the KKS symplectic form (S9; Provost-Vallee, Berry-on-Kähler-manifolds literature).
- **Genuinely new + subtle:** **OP^2 is not Kähler / not symplectic (S8)** — so the off-the-shelf KKS result does NOT give the Berry curvature of the un-broken idempotent family (an invariant 2-form does not exist; Spin(9) preserves an 8-form). No located work computes the Berry curvature / Im(QGT) of the primitive-idempotent family on OP^2 = F_4/Spin(9) or on any exceptional Jordan projective space. (Searches on "QGT/Berry curvature OP^2 / F_4/Spin(9) / Cayley plane / exceptional Jordan coherent states" returned only the *ingredients*, never the computation.)
- **VERDICT: CANDIDATE-NOVEL, with a genuine well-definedness question.** The roadmap must NOT assume Im(QGT) is a nonzero 2-form on OP^2; the nonzero 2-form on the 4d slice must arise from the C_u/Spin(9)→Lorentz breaking. Phase A.5 should *first* establish that Im(QGT) (post-breaking) is a well-defined, generically-nonzero 2-form, *then* test its Einstein-vs-EM shape. **Consistency anchor (mandatory):** Re(QGT) must reproduce the v17.0 Hess(−log det) (the cone-Hessian) — if it does not, the QGT construction is wrong and Phase A.5 STOPs.

### Sub-claim N4: MM ε-contraction (the Einstein term) FORCED by the h_3(O) trace-form / cubic-norm, with NO posited action
- **Standard-math content (cite):** MM/Cartan curvature F=dA+A∧A; ∫ε F∧F = EH+Λ (S5/S6; MM 1977, Wise 2010). The MM gauge algebra is fixed by the conformal structure (S7).
- **Genuinely new target — and unattested in either direction:** No located work derives the MM ε-contraction from a Jordan-algebra trace form / cubic norm. Every located exceptional-gravity program (Singh, Castro, in-program GST) **posits an action**. So a Phase-C STRONG WIN (forced contraction) would be genuinely new; but the more likely outcome — the Einstein term only appearing via a posited MM action — is `fp-imported-action`, an honest partial, NOT a win.
- **VERDICT: CANDIDATE-NOVEL TARGET / most-likely-fails.** This is the highest-risk, highest-reward sub-claim. The trace form on h_3(O) (Tr(X∘Y), the v16.0 ring-lemma object) and the cubic norm det_3 are the only candidate intrinsic sources for the ε-contraction; whether they *force* the SO(3,1)-projecting ε-tensor is the Phase-C question. Reward-hacking guard: the contraction must be FORCED by the trace form, not chosen to make EH appear.

### Sub-claim N5 (meta): "Emergent gravity from Berry curvature / QGT geometry" as a research program
- **NOT novel as a philosophy.** Active, crowded field: Viennot 2106.01913 (Berry → Lorentz connection, the closest precedent); QGT-curved-space program (2209.07728, 2403.09804); QGT-sub-bundle (2503.17163); modular-QGT kinematic space (2110.08703, but rejected as modular/thermal). 
- **VERDICT: the *idea* is prior art; the *specific source* (h_3(O) primitive idempotents + C_u reduction) and the *MM-Einstein-structure target* are the novel contribution.** Report honestly: v18.0 is a *specific algebraic instantiation* of an existing program, distinguished by (a) the exceptional-Jordan source, (b) the exact-over-Q decidability, and (c) the MM/Cartan Einstein-structure test.

---

## Open Questions / Novelty (consolidated)

1. **Is Im(QGT) of the idempotent family a well-defined nonzero 2-form on the 4d slice?** OP^2 has no invariant 2-form (S8); the route's Berry curvature must be born from the C_u breaking. *Unaddressed in the literature → candidate novelty, but also a live well-definedness risk.* (Phase A.5)
2. **Does C_u reduce V_{1/2}(16) to exactly 4 Lorentzian dimensions, forced by (E_11,u)?** No precedent; expected by analogy to V_0 → h_2(C_u). (Phase A KILL)
3. **Does the matter-sourced Berry curvature inherit the v17.0 cone-Hessian "same-wall" mismatch?** The matter couples through the same algebra; the symmetric sector (Re QGT) gave NONE. *Must be tested at matched M-power/structure/support.* (Phase A.5 SOFT KILL)
4. **Is the MM ε-contraction forced by the h_3(O) trace-form/cubic-norm, or only by a posited action?** Unattested either way; every prior exceptional-gravity program posits an action. (Phase C — fp-imported-action is the most likely real outcome.)
5. **Census completeness:** Singh and Castro are the two substantial exceptional-Jordan-gravity programs located. A long tail of octonion-gravity preprints (vixra, conference notes) was not exhaustively read; none surfaced as a soldering-form-from-idempotent or Berry-curvature-of-OP^2 construction in the targeted searches. *Residual risk LOW but nonzero.*

---

## Alternatives Considered (what NOT to adopt, and why)

| Category | Recommended (v18.0) | Alternative (prior art) | Why not |
| -------- | ------------------- | ----------------------- | ------- |
| Source of gravity | Berry curvature = Im(QGT) of the idempotent field (antisymmetric/Lie sector) | Cone-Hessian = Re(QGT) (v17.0) | v17.0 verdict NONE; symmetric sector is not Einstein. Different tensor — but check same-wall (Phase A.5). |
| How the Einstein term arises | FORCED by trace-form/cubic-norm (target) | Posited MM/EH action (MM 1977, Wise 2010); posited trace-dynamics action (Singh); posited cubic-form membrane action (Castro); posited N=2 MESGT (GST/v12-13) | All posited → `fp-imported-action` (the GST sin). The route only WINS if the contraction is forced. |
| Replacement for diffeomorphisms | Spin(9,1)→SO(3,1) Cartan/MM connection from idempotent geometry | G_2 octonion automorphisms (Singh); E_6(-26) cubic-form invariance (Castro) | Those are posited-action frameworks; v18.0's gravity is the *connection curvature*, not an action invariance. |
| Emergent-geometry mechanism | Berry/geometric-phase generator → Lorentz connection | BFSS quasi-coherent-state adiabatic transport (Viennot) | Viennot is the precedent (cite for honesty), but matrix-theory source, torsionful, no MM-Einstein, no h_3(O). |
| QGT computational machinery | Sub-bundle / shape-operator / Gauss-Codazzi decomposition | Naive parameter-space QGT | The V_0 slice is a sub-bundle inside OP^2 (non-totally-geodesic, v17.0); use 2503.17163-style shape-operator decomposition. |
| Thermal/modular constructions | NONE (rejected) | Modular-QGT kinematic space (2110.08703); Jacobson/Connes-Rovelli | Standing constraint: no entropy/KMS/modular/thermal-time. Exclude as load-bearing. |

---

## Notation Conventions in the Literature (reconcile before computing)

| Quantity | Common symbol(s) | Variations / pitfalls | This route's choice |
| -------- | ---------------- | --------------------- | ------------------- |
| QGT | Q_{μν}, T_{μν}, χ_{μν} | Some define Q = ⟨∂ψ\|∂ψ⟩−⟨∂ψ\|ψ⟩⟨ψ\|∂ψ⟩ (projector form); sign/factor of the imaginary part varies | Im Q = −½ F (Berry); fix sign against a known example before reading verdicts. |
| Berry curvature | F_{μν}, Ω_{μν}, B | Factor of 2 vs Im(QGT); curvature of the *Berry connection* A_μ = i⟨ψ\|∂_μψ⟩ | F = dA, A = i⟨ψ\|dψ⟩; the antisymmetric part of Q. |
| MM connection | A = ω ⊕ e | so(3,2) (Λ<0/AdS) vs so(4,1) (Λ>0/dS) vs iso(3,1) (Λ=0); CONVENTIONS §6 says Λ=0, flat vacuum | A in so(3,2)/so(4,1)/iso(3,1); **do NOT reintroduce Λ<0** (corrected §6). |
| MM action | ∫ε_{ABCD}F^{AB}∧F^{CD} | Yields EH + Λ + Gauss-Bonnet; the Gauss-Bonnet/Euler term is topological | The ε-contraction is what Phase C audits (forced vs posited). |
| Cayley-plane coset | F_4/Spin(9) | Real OP^2 (compact, F_4/Spin(9)) vs hyperbolic OP^2 (F_4(-20)/Spin(9)) vs complexified; the non-compact real form for the route lives in Stab_{E_6}(E_11), Levi ~ Spin(9,1) | Compact OP^2 for the idempotent variety; the non-compact Spin(9,1) is the *ambient* group (NOT the 4d gravity connection). |
| Invariant form on OP^2 | (8-form, not 2-form) | Spin(9) preserves an invariant 8-form (Kähler-analog); **no invariant 2-form** | The Berry 2-form must come from C_u breaking, not an OP^2 invariant. |

---

## Sources (with confidence)

**Established math — CITE, do not re-derive (HIGH):**
- MacDowell & Mansouri, Phys. Rev. Lett. **38, 739 (1977)** — gravity as a broken de Sitter/Lorentz gauge theory. [bibliographic data confirmed]
- D. K. Wise, **gr-qc/0611154** = Class. Quantum Grav. **27, 155010 (2010)** — MM gravity & Cartan geometry (THE reference; "rolling" interpretation; gauge algebra fixed by conformal structure). [confirmed]
- Provost & Vallee, Comm. Math. Phys. **76, 289-301 (1980)**, DOI 10.1007/BF02193559 — QGT: real=Fubini-Study, imaginary=Berry; treats group-orbit/coherent-state case with explicit curvature. [confirmed]
- R. W. Sharpe, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (Springer GTM 166, 1997) — Cartan connections, soldering forms, reductive split.
- J. C. Baez, "The Octonions," Bull. AMS **39, 145 (2002)**, arXiv math/0105155 — OP^2 = F_4/Spin(9), T_E OP^2 = V_{1/2}, E_6(-26) collineations.
- K. McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004) — Peirce decomposition, primitive idempotents, E∘δ=½δ.
- (S8) OP^2 not Hermitian-symmetric / no almost-complex structure / Spin(9)-invariant 8-form: standard symmetric-space classification (Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*) + the Spin(9)-octonionic-geometry literature ("The rôle of Spin(9) in Octonionic Geometry," preprints.org 201809.0430). [HIGH — multiply confirmed]

**Prior exceptional/octonionic-gravity attempts — CONTRAST, do not adopt (HIGH on characterization):**
- T. P. Singh et al.: arXiv:2006.16274, **2009.05574** (abstract confirms "we proposed a Lagrangian in trace dynamics"), 2104.14344, 2304.01213 (PDF unreadable — abstract/summaries only), 2308.16216 — posited trace-dynamics action; gravity emergent; G_2 not idempotent-coframe; no Berry/QGT. **= fp-imported-action category.**
- C. Castro: "Exceptional Jordan Strings/Membranes and Octonionic Gravity/p-branes"; "Exceptional Jordan Matrix Models, octonionic p-branes and star-product deformations," J. Geom. Phys. (2021) S0393044021001145 — posited E_6(-26) cubic-form membrane/matrix action; no connection-curvature/Berry construction.
- Gunaydin-Sierra-Townsend (1983-84) — E_6(-26)/F_4 magic-supergravity **geometry only** (citable for orientation); their Lagrangian = the dead in-program det/GST route.

**Berry/QGT emergent-gravity programs — CITE for precedent/method, NOT load-bearing for the result:**
- D. Viennot, **arXiv:2106.01913** — Berry/geometric-phase generator = emergent (torsionful) Lorentz connection in BFSS matrix theory. [closest mechanism precedent]
- QGT-in-curved-space: arXiv:2209.07728 (Symmetry 2022), arXiv:2403.09804. [Phase A.5/B methodology]
- QGT from sub-bundle geometry: arXiv:2503.17163 = Quantum (q-2026-01-14-1965) — shape-operator/Gauss-Codazzi decomposition of the QGT into metric + Berry + bundle curvature. [Phase A.5/B machinery]
- Berry phase on homogeneous Kähler manifolds: arXiv math-ph/0111022 — KKS-symplectic Berry curvature (the result that does NOT cover non-Kähler OP^2).

**EXCLUDE as load-bearing (rejected by standing constraint):**
- Modular-QGT kinematic space: arXiv:2110.08703 — modular/thermal flavor (Tomita-Takesaki); the v18.0 route deliberately avoids this. Note as contrast only.
- Jacobson 1995; Connes-Rovelli thermal time — rejected (thermodynamic/modular).

**Internal GPD prior — REUSE (not re-derived):**
- `derivations/52-kkt-spacetime.tex`, `52-observer-uniqueness.tex` — h_2(C_u) ≅ R^{3,1} (1,3), the Phase-46 π_u C_u bottleneck (REUSE for V_{1/2}).
- `code/ring_lemma_verification.py` (det_3 SSOT, trace form Tr(X∘Y)); `code/orbit_dimension_gate.py` (stabilizer calibration); `code/peirce_coupling.py` (Peirce under E_11); `code/bulk_geometry_verification.py` (Totaro/Levi-Civita harness + cone-Hessian = Re(QGT) consistency anchor).

---

## External-tool note (per protocol)

- arXiv:2304.01213 (Singh, EJA & gravitation/weak force) PDF could not be machine-read (PDF-stream compression corruption on both `/pdf/` and `/abs/` fetches). Singh's program is characterized from the **confirmed abstract of arXiv:2009.05574** ("we have recently proposed a Lagrangian in trace dynamics… for unification of gravitation, Yang-Mills fields, and fermions") plus multiple search-summary cross-checks. Confidence HIGH that Singh **posits an action** and does **not** use an idempotent-coframe or Berry curvature; if Phase C wishes to cite Singh as the canonical contrast, a human read of 2304.01213 is advised (non-blocking).
- All other key references (Provost-Vallee, Wise, MM 1977, the OP^2-not-Kähler fact) were confirmed via independent searches with bibliographic data.
