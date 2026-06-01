# Known Pitfalls Research — Gravity as the Curvature of the Peirce-Frame (Cartan / MacDowell-Mansouri) Connection on h_3(O)

**Domain:** Cartan geometry of gravity (MacDowell-Mansouri / broken (A)dS connection), the quantum geometric tensor and its imaginary part (Berry curvature, abelian and non-abelian / Wilczek-Zee), the Cayley plane OP^2 = F_4/Spin(9) and its tangent Peirce half-eigenspace V_{1/2}, octonionic Jordan algebra h_3(O), soldering forms / coframes, and the distinction between a Lie-sector connection field strength (a 2-form F) and a symmetric-sector metric Hessian (the dead v17.0 cone-Hessian tensor).
**Researched:** 2026-06-01
**Confidence:** HIGH on the route's central risk (fp-imported-action — the MM-action circularity) and on the four KILL-gate traps the milestone names (arbitrary reduction, sector confusion, Berry gauge ambiguity, the EM-shaped same-wall relabel); each is backed by published mathematics (Wise gr-qc/0611154; Provost-Vallée 1980; Wilczek-Zee non-abelian Berry; the EM stress tensor characterization) AND by this project's own v17.0 NONE post-mortem. HIGH on the arithmetic-hygiene traps (octonion association, float-decisive, watchdog stalls) — each is a documented failure already realized in this repo. MEDIUM on the exact form the Phase-B/C false-positive will take (depends which clause of Phase A/A.5 survives).

> **Milestone shape (read first).** v18.0 is a **KILL-gated** test on the ANTISYMMETRIC/Lie-sector curvature F = dA + A∧A of the assembled (A)dS Cartan connection A = ω⊕e on h_3(O) — the Berry curvature / imaginary part of the self-model QGT. The dead v17.0 route was the REAL part (the cone-Hessian / Fubini-Study metric), so its NONE does **not** bind this tensor. Phase A (coframe reduction) and Phase A.5 (Berry-curvature same-wall) are cheap KILL/SOFT-KILL gates that decide survival before the expensive Phase B/C machinery. **The single dominant failure mode of the whole milestone is fp-imported-action: declaring "Einstein structure" that only appears because a MacDowell-Mansouri / Einstein-Hilbert action (the ε F∧F contraction) was POSITED by hand.** That is the same circularity (the "GST sin") that killed the det/GST/Weinberg route, where −R/2 is the assumed N=2 multiplet's own output. Every pitfall below is tagged with the Phase (0 / A / A.5 / B / C) that must guard it. Pitfall 1 (fp-imported-action) and Pitfall 2 (fp-arbitrary-reduction) are the two that decide whether this milestone produces a trustworthy verdict; Pitfalls 3 (sector confusion) and 4 (the EM-shaped same-wall relabel) are where a near-miss gets dishonestly inflated.

> **NEGATIVE-RESULT-IS-SUCCESS.** A clean Phase A KILL (no forced 4d Lorentzian coframe), a Phase A.5 same-wall SOFT KILL, or a Phase C fp-imported-action verdict are each full, publishable closures. The deadliest pitfall is not a negative result — it is a **dishonestly positive** one. Report at true strength; never relabel "approximately 4d" or "approximately Einstein."

---

## Critical Pitfalls

### Pitfall 1: fp-imported-action — declaring "Einstein structure" that only appears because an MM / Einstein-Hilbert action was POSITED (Phase C critical; the input ban must be declared at Phase 0/A and enforced throughout)

**What goes wrong:**
The MacDowell-Mansouri construction does NOT give Einstein gravity from the raw curvature F = dA + A∧A. It gives Einstein-Hilbert + Λ **only after** a specific contraction is imposed by hand: the action S = ∫ ε_{abcd} F^{ab} ∧ F^{cd} (equivalently the BF form with B^{ab} = ε^{abcd} e_c ∧ e_d, the Hodge dual of the vielbein). It is **that ε-tensor contraction onto the broken Lorentz block** — not the connection, not the curvature 2-form — that selects the −(1/2)R Einstein-Hilbert term, the cosmological term Λ e∧e, and a topological Gauss-Bonnet/Euler term [Wise, gr-qc/0611154; the B^{ab}=ε e∧e auxiliary-field/Plebański structure]. So a researcher who has assembled A = ω⊕e and computed F can ALWAYS "find Einstein gravity" by reaching for the standard MM ε-contraction — and will have proven nothing, because the Einstein term was carried in by the posited action, exactly as −R/2 was carried in by the assumed N=2 SUSY closure in the dead det/GST/Weinberg route.

This is **the same sin as the GST graveyard** (`47-*`..`50-*`, `53-*`): in 5D N=2 MESGT the −(1/2)R coefficient is fixed by the supersymmetry structure, and the same C_IJK tensor that defines the special-real geometry also fixes the gravitational term — so reading off Einstein gravity from the matching geometry is circular. The MM route shares the danger in a new costume: the (A)dS gauge structure makes the ε F∧F action look "natural" and "forced by the symmetry," when in fact the choice of ε-contraction (which group breaks to which subgroup, which Levi-Civita tensor on which broken generators, and the overall normalization that becomes 1/16πG) is **external input**, not output of h_3(O).

**Why it happens:**
The (A)dS Cartan/MM literature is action-shaped: every reference writes down ∫ ε F∧F as "the" MM action and reads off EH+Λ. Confirmation bias ("Einstein is the hoped-for answer") plus a literature that hands you the ε-contraction for free makes the circular step feel like legitimate textbook physics. The deadliest version is subtle: not citing the MM action explicitly, but silently using its ε-contraction or its −R/2 dictionary "because that is how you get gravity from F."

**Consequences:**
A reported "STRONG WIN" (gravity from h_3(O), non-circular) that is actually an fp-imported-action honest-partial at best — the third circular-Einstein false alarm in this program, and a retraction-grade error if it ships as a derivation.

**How to detect it / what would count as the ε-contraction being FORCED:**
1. **The forced-vs-posited test (this IS Phase C).** Ask the precise question: *Is the ε-contraction — the Spin(9,1)→SO(3,1) symmetry breaking pattern AND the Levi-Civita tensor / pairing on the broken generators AND its normalization — FIXED by the h_3(O) trace form ⟨X,Y⟩ = Tr(X∘Y) or the cubic norm det_3, or is it an external MM choice?* It is FORCED only if the trace-form/cubic-norm pairing on the relevant Peirce blocks **uniquely** produces the ε_{abcd}-shaped invariant quadratic-in-F contraction with no freedom to choose a different invariant. Demonstrate: (i) the space of trace-form-invariant quadratic contractions of F is **one-dimensional** (compute it — Schur/invariant-theory count over the residual structure group), and (ii) that unique invariant **equals** the ε-contraction up to the normalization the cubic norm fixes. If the invariant space is >1-dimensional, or the ε-contraction is only one choice among several, or the normalization has to be put in by hand → POSITED → fp-imported-action.
2. **Independence audit (checklist for every Phase B/C equation).** For each equation, ask: "Could I have written this down WITHOUT already knowing the answer is Einstein gravity?" Any step that requires the MM action, the −1/2 coefficient, the 1/16πG normalization, a SUSY multiplet assignment, Weinberg's soft-graviton theorem, or the equivalence principle as a *premise* is circular — flag and remove.
3. **Hard input ban (declare in the Phase 0/A plan).** Phase B/C may use ONLY: the trace form Tr(X∘Y) and cubic norm det_3 (SSOT, correct association), the Peirce decomposition under E_11, the C_u/π_u reduction, the soldering form e = π_u(dE), the spin connection ω forced by metric-compatibility/torsion, and standard differential geometry (d, ∧, F = dA+A∧A, the curvature/torsion split). **Forbidden:** any MM/EH/supergravity action, the ε F∧F contraction as an *assumed* action, the −1/2 coefficient, SUSY, Weinberg, the equivalence principle as premise. Wise/MM may be cited **for the Cartan-geometry statement (what F's blocks mean)** — never for the action that selects Einstein.

**Warning signs:**
- Any appearance of "∫ ε F∧F", "−1/2", "16πG", "MM action", or "SUSY" in the Phase B/C derivation chain used as load-bearing input.
- A "STRONG WIN" whose final step is "and contracting MM-style gives Einstein-Hilbert" — that is the posited action, not a derivation.
- The ε-contraction's normalization (→ Newton's constant) put in by hand rather than read off the cubic norm.
- Citing Wise/MM for the action rather than for the geometric meaning of the curvature blocks.

**Phase to address:** **Phase C** is where it is fatal and where the forced-vs-posited verdict is rendered; the **input ban is declared at Phase 0/A planning** and enforced through B. The honest and most-likely real outcome is **forced-coframe-but-imported-action (B yes, C no)** → report as fp-imported-action, NOT a win.

**References:** Wise, "MacDowell-Mansouri gravity and Cartan geometry," gr-qc/0611154 (the ε F∧F → EH+Λ+Euler structure; the B^{ab}=ε e∧e auxiliary field); MacDowell & Mansouri, PRL 38 (1977) 739; the project's own dead GST route (`47-*`..`50-*`,`53-*`) and the v17.0 Phase 73 circularity audit (VALD-05: no GST/SUSY/−R/2/Weinberg import).

---

### Pitfall 2: fp-arbitrary-reduction — a 4-dim Lorentzian coframe obtained by a CHOICE not forced by (E_11, u) (Phase A, the KILL gate itself)

**What goes wrong:**
The route needs the 16-dim V_{1/2}(E_11) soldering form e = dE to reduce, via the C_u/π_u bottleneck, to **exactly a 4-dim Lorentzian coframe carrying SO(3,1)** — and that reduction must be **forced by (E_11, u) alone**, not smuggled in by an extra choice. Three ways the gate is failed dishonestly:
- **Wrong dimension dressed as 4.** π_u(V_{1/2}(16)) lands on some image; if its exact dimension is not 4 (e.g. 6, 8, or 16), but a 4-dim sub-piece is then selected "for the physical part," the 4 was chosen, not derived. (Contrast: V_0's h_2(O)→h_2(C_u) gave R^{3,1} = 4d because the C_u bottleneck acted on the 10-dim V_0 and the det_2 Minkowski form is intrinsic — the analogous computation on V_{1/2} must be done and its image dimension reported exactly, expecting 4 only if it genuinely parallels V_0.)
- **Non-Lorentzian pairing relabeled Lorentzian.** The induced coframe pairing (the Gram matrix of e under the trace form) must have exact signature (1,3) / mostly-minus over Q. A Euclidean (4,0) or split (2,2) Gram reported as "Lorentzian after a Wick rotation" is a choice — the rotation is the extra structure.
- **Structure group put in by hand.** SO(3,1) must be FORCED as (or inside) the residual structure group the reduction leaves on the 4-dim coframe; choosing an SO(3,1) frame on a space that does not intrinsically carry it is fp-arbitrary-reduction.

**Why it happens:**
"4-dim Lorentzian spacetime" is the hoped-for answer, and there are many ways to project 16→4 or to declare a frame. The C_u bottleneck genuinely worked for V_0 (Phase 46), which tempts the assumption that "the same bottleneck obviously gives 4d Lorentzian on V_{1/2}" without computing it. The Cayley-plane fact T_E OP^2 = V_{1/2}(16) (Borel; Freudenthal-Jordan construction of OP^2 = F_4/Spin(9) as trace-1 idempotents) is 16-dimensional — getting to 4 is a real reduction that must be earned, not assumed.

**Consequences:**
A "SURVIVES" verdict that is really a hand-built coframe — the entire route then rests on a smuggled spacetime, and Phases B/C compute the curvature of a fiction.

**How to avoid (the clean KILL gate):**
1. **Compute the exact image dimension of π_u(V_{1/2}(16)) over Q** (sympy rank of the reduction map on the Peirce basis), and report it. KILL if ≠ 4.
2. **Compute the exact Gram-eigenvalue signature** of the coframe pairing under the trace form Tr(X∘Y), over Q (sympy eigenvalues, count signs). KILL if not (1,3) / mostly-minus. Do NOT rescue a non-Lorentzian Gram with a coordinate Wick rotation (that is fp-arbitrary-reduction and, per the v17.0 signature post-mortem, manufactures spurious structure).
3. **Verify the residual structure group ⊇ SO(3,1) is FORCED by (E_11, u).** The reduction must be determined by E_11 (the idempotent) and u = e_7 (the complex structure) ALONE. Log every structural input; if any step needs a choice beyond (E_11, u) — a basis selection, a projection direction, an extra idempotent — it is fp-arbitrary-reduction → KILL.
4. **Reuse, do not reinvent, the Phase-46 π_u mechanism.** The C_u bottleneck that sent h_2(O)→h_2(C_u)=R^{3,1} (`derivations/52-kkt-spacetime`, `52-observer-uniqueness`) is the SAME map to apply to V_{1/2}; using a different, ad hoc reduction is a red flag for a smuggled choice.

**Warning signs:**
- Image dimension ≠ 4 with a 4-dim sub-piece then selected.
- A Wick rotation invoked to make the Gram Lorentzian.
- The reduction needs any input beyond (E_11, u).
- "Approximately 4-dim" or "effectively Lorentzian" language — a reduction is exactly 4d and exactly Lorentzian over Q, or it is a KILL.

**Phase to address:** **Phase A** — this pitfall IS the KILL gate. Get it right or the milestone is worthless.

**References:** the prompt's Phase A KILL condition and `fp-arbitrary-reduction` forbidden proxy; Baez, "The Octonions" (2002) and the Cayley-plane construction (OP^2 = F_4/Spin(9) = trace-1 idempotents, T_E OP^2 = V_{1/2}); McCrimmon, *A Taste of Jordan Algebras* (Peirce decomposition, E∘δ=(1/2)δ); `derivations/52-kkt-spacetime` (the V_0 precedent).

---

### Pitfall 3: SECTOR CONFUSION — mistaking the antisymmetric/Lie curvature (this route) for the symmetric-sector cone-Hessian (the dead v17.0 tensor), or reusing the dead Riemann as load-bearing (Phase 0 calibration; Phase A.5 and B critical)

**What goes wrong:**
The entire justification for re-attacking gravity after the v17.0 NONE is that this route computes a **different tensor**: the antisymmetric/Lie-sector connection field strength F = dA+A∧A (the Berry curvature = imaginary part of the QGT), NOT the symmetric/Jordan-sector metric Hessian g_X = Hess(−log det) (the Fubini-Study/real part of the QGT, verdict NONE). Two failure modes collapse this distinction and silently re-bind the route to the dead verdict:
- **Reusing the dead cone-Hessian Riemann as load-bearing.** Importing the v17.0 `bulk_geometry_verification.py` Riemann tensor, or its Ricci/Weyl decomposition, as the gravitational object — that is the symmetric-sector tensor that already returned NONE. The cone-Hessian appears in this route ONLY as a consistency check (the REAL part of the QGT must reproduce Hess(−log det); see Pitfall 5), never as the curvature being tested.
- **Computing a symmetric object and calling it the connection curvature.** If the "curvature" computed in Phase B is secretly the Levi-Civita Riemann of the induced metric (a symmetric-sector object) rather than the Lie-algebra-valued field strength of the assembled Cartan connection A=ω⊕e, the route has quietly reverted to v17.0 and the NONE verdict DOES bind it. The Lorentz block of F **does** contain a Riemann tensor R(ω) — but it is the curvature of the spin connection ω forced by the soldering form, an antisymmetric-sector object; conflating it with the cone-Hessian Riemann is the error.

**Why it happens:**
Both routes live on the same OP^2 = F_4/Spin(9) geometry, both involve "curvature," both are halves of the same QGT, and the v17.0 harness is sitting in the repo ready to import. The QGT's real and imaginary parts are genuinely different tensors (Provost-Vallée 1980: real = Fubini-Study metric, imaginary = Berry curvature), but "curvature of the idempotent family" is ambiguous between them, and the warm v17.0 code makes the wrong import frictionless.

**Consequences:**
The whole milestone's premise ("NONE does not bind this tensor") is voided — a curved-but-not-Einstein verdict that is just the v17.0 result re-run under a new name.

**How to avoid:**
1. **Calibrate the QGT split at Phase 0/A.5.** Compute the QGT of the idempotent state family |ψ(x)⟩ at E(x); verify EXACTLY that its REAL part reproduces the dead Hess(−log det) (consistency check — if it does not, STOP and re-examine the QGT before trusting the imaginary part, per the prompt's stop condition). The load-bearing object is the IMAGINARY part F_B (Phase A.5) and the assembled-connection F (Phase B) — keep them typed-distinct from the real part in code and notation.
2. **Type-guard the curvature.** The Phase-B gravitational object is the Lie-algebra-valued 2-form F = dA+A∧A with A=ω⊕e (a so(3,2)/so(4,1)/iso(3,1)-valued connection), whose Lorentz block is R(ω) and whose translation block is torsion de+ω∧e. It is NOT g_X = Hess(−log det). Forbid any import of the v17.0 cone-Hessian Riemann into the decisive path; the v17.0 harness is allowed only for (a) the real-part consistency check and (b) the Totaro/Levi-Civita cross-check of R(ω) on ≥5 components.
3. **State the sector in every artifact.** Each derivation/code file declares whether it computes a symmetric-sector (metric/real-part) or antisymmetric-sector (connection/imaginary-part) quantity; a decisive verdict resting on a symmetric-sector object is a regression to v17.0.

**Warning signs:**
- An `import` of the v17.0 cone-Hessian Riemann (not just the cross-check harness) on a decisive path.
- The Phase-B "curvature" is symmetric in its index structure like a metric Hessian rather than antisymmetric like a field strength.
- The real part of the QGT is assumed to equal Hess(−log det) without an exact check.
- The verdict language echoes v17.0 ("curved but not Einstein") without a demonstration that the tensor tested is the imaginary-part/connection object, not the real-part/metric one.

**Phase to address:** **Phase 0/A.5** (QGT real-part consistency check + type calibration), **Phase B** (the connection curvature, not the metric Hessian, is load-bearing).

**References:** Provost & Vallée, Comm. Math. Phys. 76 (1980) 289 (QGT real=Fubini-Study, imaginary=Berry curvature; the imaginary part is symplectic/antisymmetric); the prompt's "Stay distinct from `paper6-bulk-geometry-prompt.md`" and "do NOT reuse the cone-Hessian Riemann as load-bearing"; v17.0 Phase 73 NONE verdict.

---

### Pitfall 4: fp-relabel / THE SAME-WALL TRAP — relabeling a generic EM-shaped U(1) field strength "Einstein" without an independent stress-energy T[M] matched in MAGNITUDE, TENSOR STRUCTURE, and M-POWER (Phase A.5 SOFT KILL; Phase B/C critical)

**What goes wrong:**
The curvature 2-form F is, structurally, a gauge field strength — a generic non-abelian F_{μν}. The deadly relabel is: "F_{μν} ≠ 0 and satisfies a 2-form equation, therefore gravity / Einstein." A field strength satisfying a 2-form equation is a *Maxwell-type* (EM-shaped) object, NOT an Einstein structure. The v17.0 Phase 73 lesson is exact and binding here: **a tensor appearing ≠ Einstein structure.** v17.0 found genuine curvature (S≠0, Weyl≠0) that was nonetheless NOT of Einstein form — no global (κ,Λ) gave G_μν = κT_μν + Λg_μν against an independently-frozen T, with κT ~10³ smaller than G and support mismatched. The Lie sector can inherit precisely this failure: the matter-sourced part of the Berry/MM curvature can be a generic U(1)/Yang-Mills-shaped field strength whose effective stress content is **EM-shaped** — i.e. **quadratic in the field strength (T ~ F², hence quadratic in M-derivatives), traceless, and conformally invariant** [EM stress tensor characterization: T^μ_μ = 0, T_{μν} ~ F_{μα}F_ν^α − (1/4)η_{μν}F²] — which is the SOURCE side of Einstein's equation, not the curvature side, and does not match a metric stress-energy in M-power or tensor structure.

**Why it happens:**
After surviving the Phase A coframe gate, "the curvature is nonzero and matter turns it on" feels like success. The distinction between (i) a 2-form field strength (EM-shaped, lives on the source side) and (ii) the Einstein tensor G_μν[g] of the induced metric (the geometric response) is easy to blur because both are "curvature." Confirmation bias supplies the relabel.

**Consequences:**
A "SURVIVES / Einstein-shaped" verdict that is really the Lie-sector version of the v17.0 same-wall mismatch — an EM-shaped field strength dressed as gravity (fp-relabel), the route's most likely premature false positive.

**How to avoid (the same-wall discriminants — these ARE Phase A.5(b,c)):**
1. **Match M-POWER.** Determine the leading M-power of the matter-sourced F_B (and of G[g] in Phase B) and of the independently-built V_{1/2} stress-energy T[M]. An EM-shaped object scales as T ~ F² ~ (∂M)² (quadratic in field strength); a genuine matter source for Einstein must match the M-power of G[g] at the SAME order. (v17.0 found h^(1)=0, matter entering g at O(‖M‖²), curvature at O(‖M‖⁴) — the order-counting is decisive and must be reproduced, not assumed.) A mismatch in M-power = EM-shaped, not Einstein → SOFT KILL.
2. **Match TENSOR STRUCTURE.** An EM stress tensor is **traceless** (T^μ_μ = 0). Test whether the candidate source has the trace structure a metric source needs; a traceless ∝-to-F² object sourcing a non-traceless G[g] cannot be Einstein. Decompose F_B's effective stress into trace (Λ-like), traceless-Ricci-shaped, and Weyl-shaped parts and check it tracks a metric T[M], not a Maxwell T~F².
3. **Match SUPPORT and MAGNITUDE (the explicit same-wall check, A.5(c)).** Does the matter-source of F_B come out **non-proportional to T[M] the way the cone-Hessian's did** — support where T vanishes, ~10³ magnitude/shape mismatch? Build T[M] from V_{1/2} cross-term data ONLY (independent of the curvature; freeze κ from the cubic norm BEFORE computing F_B), then test proportionality. If the cone-Hessian mismatch recurs → SOFT KILL, the Lie sector inherits the symmetric-sector failure.
4. **The ε-contraction order-match (A.5(b)).** Check whether the ε-contraction of F_B∧F_B onto the Lorentz block yields a tensor whose M-scaling and structure CAN match a V_{1/2} T[M] at the SAME order — "some tensor appears" is not enough (v17.0 Ph73). (Note: this is the *diagnostic* ε-contraction; whether the ε-contraction is FORCED is Pitfall 1 / Phase C — keep the two questions separate.)

**Warning signs:**
- "F satisfies a 2-form / Bianchi equation, therefore Einstein." (Pure fp-relabel.)
- A matter-source quadratic in field strength (T~F²) or traceless, declared a metric stress-energy.
- T[M] or κ whose definition references F_B or G[g]. (Circular — must be frozen first.)
- Support of the curvature-source disjoint from the support of T[M], or a ~10³ magnitude gap (the v17.0 signature).
- M-power of the source ≠ M-power of G[g] at the matched order.

**Phase to address:** **Phase A.5** is the cheap version (SOFT KILL on the canonical Berry curvature F_B before building the full connection). **Phase B/C** must re-apply the M-power/structure/support match to the full F. SOFT KILL if A.5(c) reproduces the cone-Hessian mismatch — recommend STOP before Phase B.

**References:** v17.0 Phase 73 NONE post-mortem ("a tensor appearing ≠ Einstein"; κT ~10³ < G; per-point Λ unequal); the prompt's `fp-relabel` proxy and Phase A.5 same-wall gate; electromagnetic stress-energy tensor (traceless, ~F², conformal) [Wikipedia, "Electromagnetic stress-energy tensor"; arXiv:1101.2505 "A characterization of the electromagnetic stress-energy tensor"]; Provost-Vallée 1980 (the imaginary-part Berry curvature IS a symplectic 2-form / field strength, not a priori a metric source).

---

### Pitfall 5: BERRY-CURVATURE / QGT GAUGE & NORMALIZATION AMBIGUITY — deciding a verdict on a gauge-COVARIANT (frame-dependent) quantity, or on the gauge-dependent connection, instead of a gauge-INVARIANT scalar (Phase A.5; Phase B)

**What goes wrong:**
The QGT and its imaginary part (Berry curvature) carry gauge structure, and the soldering-form / degenerate-subspace setting here is **non-abelian** (the V_{1/2} eigenbundle and the Spin(9,1)-valued connection are multi-dimensional / matrix-valued). Three traps:
- **Berry CONNECTION is gauge-dependent.** The Berry connection A_B = ⟨ψ|∂ψ⟩ is gauge-dependent (depends on the phase/frame choice of |ψ(x)⟩); only its curvature is physical [Provost-Vallée; standard QGT]. A verdict resting on the connection (e.g. ω before checking its curvature) can be pure gauge.
- **Non-abelian Berry curvature is gauge-COVARIANT, not invariant.** For a degenerate subspace (the Wilczek-Zee setting), the non-abelian Berry curvature F_B transforms **covariantly** under U(r) frame rotations — F_B → U F_B U^{-1} — it is NOT gauge-invariant. Its individual components/eigen-structure are frame-dependent; only gauge-invariant combinations (traces tr F_B, tr F_B², Wilson LOOPS) are physical. The Wilson LINE (open path) is gauge-dependent at both endpoints [Wilczek-Zee; "Wilson loop and Wilczek-Zee phase," arXiv:1910.13991; "non-abelian Berry curvatures in lattice QCD," arXiv:1712.02218]. Reading "Einstein-shaped" off a frame-dependent component of F_B is meaningless.
- **Sign and normalization conventions.** The QGT imaginary part has a sign/factor-of-2 convention (Berry curvature = −2 Im⟨∂ψ|(1−P)|∂ψ⟩ in one common normalization); the H^3 cone-Hessian benchmark already carries a factor-2 (K=−1/2 vs round −1). A sign/normalization slip can flip a vacuum verdict (flat vs pure-Λ) or a curvature sign.

**Why it happens:**
"Berry curvature is gauge-invariant" is a true slogan for the **abelian** (single-band) case and is reflexively over-extended to the non-abelian/degenerate case where it is only gauge-COVARIANT. The frame freedom in the V_{1/2} eigenbundle is exactly a U(r) Wilczek-Zee freedom.

**Consequences:**
A verdict (vacuum level, Einstein-shape) that is an artifact of a frame/phase choice — not a property of the geometry. A factor-2/sign slip mis-reports the vacuum or the curvature sign.

**How to avoid:**
1. **Decide verdicts on gauge-INVARIANT scalars only.** Use trace invariants (tr F_B, tr(F_B∧F_B), curvature scalars of R(ω)) and Wilson LOOPS, never raw connection components or frame-dependent F_B components. Exact over Q (Pitfall 6).
2. **Treat F_B as gauge-covariant in the non-abelian sector.** When the eigenbundle is degenerate / the connection is matrix-valued, expect F_B → U F_B U^{-1}; verify any claimed property is invariant under a U(r) frame rotation (apply a generic frame rotation and confirm the verdict scalar is unchanged over Q).
3. **Fix sign/normalization at Phase 0/A.5 against the H^3 K=−1/2 benchmark.** Pin the QGT-imaginary-part normalization and sign convention, and the relation between F_B's normalization and the cone-Hessian's, BEFORE reading any vacuum or curvature verdict. Cross-check the real part reproduces Hess(−log det) with the SAME normalization (Pitfall 3).
4. **Distinguish Wilson loop from Wilson line.** Any holonomy diagnostic must be a closed loop (gauge-invariant), not an open line (gauge-dependent at endpoints).

**Warning signs:**
- A verdict that changes under a frame/phase rotation of |ψ(x)⟩ or a U(r) rotation of the eigenbundle. (Gauge artifact.)
- A decisive quantity that is a connection component, an open Wilson line, or a single off-diagonal F_B component.
- A vacuum flat-vs-Λ flip traceable to a sign/factor-2 choice.
- "Berry curvature is gauge-invariant" invoked in the degenerate/non-abelian setting without the covariance caveat.

**Phase to address:** **Phase A.5** (gauge-invariant F_B verdict + normalization/sign calibration), **Phase B** (gauge-invariant curvature scalars of R(ω); the spin connection ω itself is gauge-dependent).

**References:** Provost & Vallée 1980 (QGT, real=metric/imaginary=Berry, gauge structure); Wilczek-Zee non-abelian Berry phase; "Wilson loop and Wilczek-Zee phase from a non-Abelian gauge field," npj Quantum Information / arXiv:1910.13991 (Wilson loop gauge-invariant, Wilson line not; F covariant under U(r)); "Abelian and non-Abelian Berry curvatures in lattice QCD," arXiv:1712.02218; the H^3 K=−1/2 benchmark (`riemann_ricci_sign`, CONVENTIONS §6).

---

### Pitfall 6: fp-float-decisive — float ranks / Gram signatures / curvatures on a decisive verdict (ALL phases; Phase A image-dim & signature, Phase B/C curvature critical)

**What goes wrong:**
Every decisive number in this route is a rank, a signature, or a curvature built from differences of derivatives — all catastrophic-cancellation factories. A float "image dimension" can miscount (a true rank-4 read as 5 from 1e-12 noise, or rank-6 collapsed to 4 by a sloppy tolerance) → a false Phase A KILL or GREENLIGHT. A float Gram eigenvalue near zero can flip a signature (1,3)↔(2,2) or (4,0). A float curvature "1e-12" (really exactly 0 → a clean verdict) read as "small but nonzero" is a false positive — exactly the failure the project has flagged repeatedly.

**Why it happens:**
numpy/float is the default reflex; SymPy exact-over-Q is slower and the temptation under time pressure is to "just check numerically." The route's verdicts are all of the type where float noise is indistinguishable from a true small/zero value.

**How to avoid:**
- **Exact over Q on every decisive verdict.** Restrict octonionic data to rational components; use `sympy.Matrix.rank()` (never numpy rank), exact eigenvalues for signatures, exact rationals/symbols for curvature. An image dimension, Gram signature, structure-group dimension, or curvature scalar that is decisive MUST be exact. A curvature exactly 0 over Q is a clean KILL; a nonzero rational is a clean survive — never decide on a float magnitude.
- Use float finite-differences ONLY as a sanity cross-check against the exact result, never as the verdict; watch for eps-dependence (if the answer changes with eps, it is noise).
- Cross-check any Riemann R(ω) against a hand-rolled Levi-Civita on ≥5 components (the v17.0 Ph72/73 harness), exact over Q.

**Phase to address:** **All phases.** Especially Phase A (image dimension, Gram signature — both decisive and both rank/eigenvalue computations) and Phase B/C (curvature, Einstein-test residuals).

**References:** the prompt's `fp-float-decisive` proxy and "EXACT over Q (sympy.Matrix.rank, never numpy/float)"; v17.0 Pitfall 8 (catastrophic cancellation in curvature); the project's standing exact-over-Q discipline.

---

### Pitfall 7: OCTONION NON-ASSOCIATIVITY corrupting the soldering form / det — and the BANNED octonion_algebra.py (Phase 0 prerequisite to everything; Phase A/B critical)

**What goes wrong:**
Octonion multiplication is non-associative: (x₁x₂)x₃ ≠ x₁(x₂x₃), and Re((x₁x₂)x₃) ≠ Re(x₁(x₂x₃)) in general. The soldering form e = dE, the differential of the idempotent field, and the cubic-norm cross-term that couples V_{1/2} matter, are both association-sensitive. A wrong association does not throw — it returns a plausible number, and every downstream curvature is silently wrong, amplified (not averaged) by the derivative structure. **`octonion_algebra.py` is BANNED in this project** for exactly this reason: it has a buggy `(x₁x₂)x₃` order, is float, and has a documented 0.67 associator gap. (Note: this contradicts the v17.0 PITFALLS, which named `octonion_algebra.py`'s `det_3` as the SSOT — that guidance is SUPERSEDED. The current SSOT is `ring_lemma_verification.py`'s `det_3`, cross-term `2Re(x₂* x₀* x₁)`, CH + 324/324 verified.)

**Why it happens:**
Multiple inconsistent cubic-norm/association conventions coexist in the repo, all correct for diagonal/real data but differing for genuine octonionic off-diagonal data. The differential dE introduces octonionic components (e_4..e_7) that leave the associative subalgebras where the bugs hide.

**How to avoid (a hard gate at Phase 0):**
1. **Single source of truth: `ring_lemma_verification.py` `det_3`** for all cubic-norm/trace-form evaluations on octonionic data. Confirm `octonion_algebra.py` is NOT imported anywhere on a decisive path (Phase 0 explicitly checks this).
2. **Re-pass the SSOT's Cayley-Hamilton + 324/324 checks at Phase 0** before trusting any new geometry (the prompt requires this).
3. **Association-invariance pre-flight on genuinely non-associative inputs** (off-diagonal octonions with nonzero e_4..e_7, NOT just e_0..e_3 which sit in an associative subalgebra): document that Re((x₁x₂)x₃) − Re(x₁(x₂x₃)) is NONZERO on the test triple (if zero, the test inputs are accidentally associative and the test is vacuous).
4. **Conjugation/order audit for the soldering form and the (V_{1/2},V_{1/2},·) coupling.** The order and conjugation (`x₂* x₀* x₁` vs `x₀x₁x₂`) changes the coupling tensor; re-derive on the Peirce basis (`peirce_coupling.py`) and confirm it matches the SSOT convention before Phase B.

**Warning signs:**
- Any `import octonion_algebra` on a decisive path. (Hard stop.)
- A curvature/coupling that changes when you swap (x₁x₂)x₃ ↔ x₁(x₂x₃) — association is load-bearing and must be the SSOT one.
- A cross-term "verified" only on diagonal/e_0..e_3 (quaternionic) data — vacuous.

**Phase to address:** **Phase 0** (SSOT reload, CH + 324/324, octonion_algebra.py absent, association pre-flight) gates everything. **Phase A/B** is where the soldering form e=dE and the V_{1/2} coupling are genuinely octonionic and the association most bites.

**References:** the prompt's Det SSOT convention (`ring_lemma_verification.py` `det_3`, `2Re(x₂* x₀* x₁)`, CH + 324/324) and `octonion_algebra.py` BANNED; v17.0 Pitfall 2 (octonion non-associativity, with the SSOT designation now corrected); `code/peirce_coupling.py`.

---

## Moderate Pitfalls

### Pitfall 8: TORSION vs CURVATURE confusion — reading the translation block as gravity, or expecting torsion to vanish (Phase B)

**What goes wrong:**
The curvature of the assembled Cartan connection A = ω⊕e splits into two blocks with distinct physical meaning: the **Lorentz block** R(ω) + Λ e∧e (Riemann + cosmological — the gravitational content) and the **translation block** de + ω∧e (the **torsion** — the field strength of the translation/transvection generators) [Wise gr-qc/0611154; Cartan geometry: torsion = field strength of translations, curvature = field strength of rotations; Hehl, "Élie Cartan's torsion," arXiv:0711.1535]. Two errors: (i) reading the torsion (translation) block as the gravitational curvature — wrong block; the 4d Riemann is in the Lorentz block. (ii) Assuming torsion vanishes "because GR is torsion-free" — in this route torsion-freeness is NOT an assumption to import; whether de+ω∧e = 0 (torsion-free), or is matter-sourced, is a COMPUTED output. A nonzero torsion is a real feature (the V_{1/2} soldering form need not be torsion-free a priori), not a bug to be set to zero.

**How to avoid:**
- Explicitly separate the Lorentz block (→ R(ω), the gravity claim) from the translation block (→ torsion). Identify the 4d Riemann tensor with R(ω) only, cross-checked against Totaro/Levi-Civita on ≥5 components.
- Compute the torsion de+ω∧e and report whether it vanishes or is matter-sourced — do NOT impose torsion-freeness as an input (that would be an unstated assumption, a cousin of fp-imported-action).
- The spin connection ω is FORCED by metric-compatibility with e (or the canonical f_4/e_6 reductive split); if ω is chosen to make torsion vanish, that choice is an input — log it.

**Phase to address:** **Phase B** (the block decomposition of F).

**References:** Wise gr-qc/0611154 (Lorentz block = R+Λe∧e, translation block = torsion); Hehl, arXiv:0711.1535 (torsion = translational field strength); the prompt's new-objects block (Lorentz block = R(ω)+Λe∧e; translation block = de+ω∧e = torsion).

---

### Pitfall 9: AMBIENT 45-dim Spin(9,1) curvature mistaken for the 4d gravity connection (Phase B)

**What goes wrong:**
Spin(9,1) (45-dim) is the AMBIENT structure group; it is NOT the 4d gravity connection. The gravitational content is the **10-dim** assembled (A)dS/Poincaré connection A = ω⊕e (ω = the so(3,1) Lorentz block, 6-dim; e = the 4 translation/transvection generators), built from the Spin(3,1) Lorentz sub-block of Spin(9,1) plus the V_{1/2}-coset coframe. Computing the raw 45-dim Spin(9,1) curvature and reading gravity off it is a category error — it mixes the internal Spin(6)=SU(4) directions and the rest of so(9,1) into the "gravitational" object.

**How to avoid:**
- PROJECT to the Spin(3,1) Lorentz block. Extract ω as the so(3,1) part of the ambient connection (the prompt: "Do NOT use the raw 45-dim Spin(9,1) curvature — project to the Spin(3,1) Lorentz block").
- Confirm the assembled A is 10-dim (6 Lorentz + 4 translation), matching so(3,2)/so(4,1)/iso(3,1); the internal Spin(6)=SU(4) part is matter/gauge, not gravity (matching the Phase-48 so(3)×so(6) split).
- A gravitational verdict resting on a 45-dim or otherwise >10-dim object has the wrong connection.

**Phase to address:** **Phase B** (extracting ω and assembling A).

**References:** the prompt's NOTE ("Spin(9,1) is the AMBIENT structure group (45-dim); it is NOT itself the 4d gravity connection... gravity content is the 10-dim A=ω⊕e"); calibration anchors `Stab_{V_0}=45=Spin(9,1)`, `e_6=78`.

---

### Pitfall 10: VACUUM (M=0) STRUCTURE mis-read — reintroducing the dead R×H³ / Λ<0, or mis-calling flat vs pure-Λ (Phase A.5, Phase B vacuum)

**What goes wrong:**
The M=0 vacuum structure of F_B / F must be MEASURED, but the corrected CONVENTIONS §6 (2026-06-01) is authoritative: Λ=0, the M=0 spacetime vacuum is **flat KKT η** (structurally derived from the det_2 Minkowski form), NOT the dead Einstein-negative R×H³ ({0,−1,−1,−1}). That R×H³ / Λ<0 geometry was the v17.0 cone-Hessian SOURCE field, FALSIFIED as the spacetime metric (Phase 70.1). Two errors: (i) reintroducing Λ<0 / R×H³ as the expected vacuum (it is the dead symmetric-sector object, Pitfall 3); (ii) mis-calling a maximally-symmetric F_B (∝ e∧e, constant) as "matter curvature" when it is pure-Λ — the v17.0 Pitfall 6 trap, now on the 2-form: a nonzero F_B ∝ e∧e with constant coefficient is a cosmological term, not matter-sourcing.

**How to avoid:**
- Expect flat / pure-Λ at M=0 (per corrected §6); report Λ's value/sign as MEASURED, but do NOT reintroduce Λ<0 / R×H³.
- Decompose the M=0 F_B / R(ω) into trace (Λ), traceless-Ricci, Weyl; a pure ∝-e∧e (or ∝-g) constant is Λ, not matter. Genuine matter-sourcing must vanish as M→0 and show structure beyond ∝ e∧e.
- Use the H^3 K=−1/2 sign benchmark to fix conventions before reading the vacuum verdict (Pitfall 5).

**Phase to address:** **Phase A.5** (F_B at M=0), **Phase B(d)** (vacuum Einstein/(A)dS).

**References:** CONVENTIONS §6 corrected 2026-06-01 (Λ=0, flat M=0 vacuum, R×H³ falsified); v17.0 Phase 70.1 (η+h bridge, cone-Hessian-IS-metric falsified) and Pitfall 6 (pure-Λ false positive); the prompt's "do NOT reintroduce Λ<0."

---

### Pitfall 11: SINGLE-POINT / SINGLE-M sampling cannot detect position-dependence or Einstein structure (Phase B/C)

**What goes wrong:**
Computing F / R(ω) at one basepoint x or one matter configuration M and concluding "position-dependent" (it might be constant) or "Einstein" (one tuned point always fits). Position-dependence is a statement about a *function* of x; Einstein structure is a statement that ONE global (κ,Λ) works across a FAMILY. v17.0 Phase 73 made the verdict decisive precisely by testing a 12-point (M,x) family and finding per-point Λ all unequal — a single point would have given a false "Einstein."

**How to avoid:**
- Evaluate curvature invariants as symbolic functions of x (exact, preferred) or on a grid of ≥3 generic basepoints; test ∂_x(invariant) ≢ 0 over Q. A nonzero-but-constant curvature is homogeneous, not position-dependent.
- Test the Einstein relation over a FAMILY of (M,x): the SAME (κ,Λ) must work for all. A κ re-tuned per configuration is a fit, not a constant (fp-relabel / Pitfall 1+4). Predefine κ,Λ from intrinsic data BEFORE the test.
- State the honest order (exact / leading-order / none); check the next M-order before any "exact" claim.

**Phase to address:** **Phase B** (position-dependence of R(ω)), **Phase C** (Einstein structure across the family).

**References:** v17.0 Phase 73 (12-point (M,x) family, per-point Λ unequal) and Pitfalls 7/11; the prompt's family-not-point discipline.

---

## Minor Pitfalls

### Pitfall 12: SOLDERING-FORM NON-INVERTIBILITY — e = π_u(dE) degenerate as a tetrad (Phase B)

**What goes wrong:** A genuine coframe/tetrad must be invertible (det(e^a_μ) ≠ 0); a non-invertible soldering form is a degenerate/collapsed frame, not a spacetime coframe. Phase A establishes the 4-dim Lorentzian image; Phase B must additionally confirm e is non-degenerate as a soldering form.
**Prevention:** Compute det(e^a_μ) over Q at generic and special points; confirm ≠ 0. A degenerate e invalidates the spin-connection extraction and the F computation. (Wise: a Cartan connection requires the soldering form to be a linear iso at each point.)
**Phase to address:** Phase B(a).

### Pitfall 13: CONVENTION DRIFT across phases — changing the bridge, normalization, or association mid-stream (all phases)

**What goes wrong:** Changing the C_u reduction, the QGT sign/normalization, the metric signature convention, or the det association between phases silently invalidates cross-phase comparisons (e.g. the A.5 vacuum vs the B vacuum). v17.0 emitted a non-blocking notation follow-up (metric_signature label/glyph reconcile, K=−1/2) for exactly this.
**Prevention:** Freeze all conventions at Phase 0 (det SSOT, u=e_7, E_11=diag(1,0,0), Peirce indices {17,18,19,26}, mostly-minus via det_2, K=−1/2, QGT normalization) and inherit them unchanged; log any change and re-run dependent checks.
**Phase to address:** Phase 0 (freeze), all phases (inherit).

---

## Numerical / Computational Traps

| Trap | Symptom | Prevention | When It Breaks |
|------|---------|------------|----------------|
| Long-symbolic-run watchdog stall | gpd-executor killed at ~600s with 0-token return on a no-output symbolic curvature run | Run foreground with `python -u` (unbuffered); commit task-by-task so work survives a kill; orchestrator can commit+SUMMARY on stall (recover via git log, NOT re-run) | Large symbolic F=dA+A∧A / Riemann over Q (Phase B); the curvature engine on 16→4 reduced data |
| Float rank/signature miscount | image dim or Gram signature flips with tolerance; 1e-12 read as nonzero | sympy.Matrix.rank() + exact eigenvalues over Q; never numpy on a decisive verdict | Phase A image dim (decisive); Phase A Gram signature (decisive) |
| Catastrophic cancellation in curvature | curvature scalar = noise; changes with finite-difference eps | Exact over Q; finite-difference only as sanity cross-check | Phase B/C Riemann, Einstein-test residuals |
| Wrong octonion association | curvature/coupling changes under (x₁x₂)x₃↔x₁(x₂x₃); plausible-but-wrong number, no error thrown | SSOT `ring_lemma_verification.py` det_3; association pre-flight on e_4..e_7 data | Phase A/B soldering form & V_{1/2} coupling (genuinely octonionic) |
| Inverse / det cost cliff | symbolic matrix inverse or det >200s on full octonionic data | Restrict to rational data; exploit Peirce block structure; pre-reduce before inverting | Phase B (assembling A, computing F on full data) |
| Gauge-frame-dependent verdict | F_B / curvature property changes under U(r) frame rotation | Decide on gauge-invariant scalars (tr F, Wilson loops) only; test invariance under a generic frame rotation over Q | Phase A.5 (non-abelian F_B), Phase B (ω gauge-dependent) |

---

## Convention / Notation Traps

| Convention Issue | Common Mistake | Correct Approach |
|------------------|----------------|------------------|
| det / cubic-norm SSOT | Using `octonion_algebra.py` det_3 (the v17.0 PITFALLS named it SSOT — now SUPERSEDED) | SSOT = `ring_lemma_verification.py` det_3, cross-term `2Re(x₂* x₀* x₁)`, CH + 324/324; octonion_algebra.py BANNED |
| Metric signature | Sign-flip between mostly-plus/mostly-minus; double-counting the Minkowski background | mostly-minus via det_2 (`metric_on_h2Cu=mostly_minus_via_det2`, `52-kkt-spacetime`); state explicitly; reduce to exact η at (M=0, center) |
| H^3 curvature normalization | round-sphere K=−1 used where the cone-Hessian gives K=−1/2 (factor-2) | Fix sign/scale against K=−1/2 BEFORE any curvature verdict (riemann_ricci_sign) |
| QGT imaginary-part sign/factor | Berry curvature sign/factor-2 convention slips; flips flat-vs-Λ | Pin the QGT-imag normalization at Phase 0; cross-check real part = Hess(−log det) with SAME normalization |
| Berry curvature "gauge-invariant" | over-extending the abelian slogan to the non-abelian/degenerate case | Non-abelian F_B is gauge-COVARIANT (U(r)); decide on invariant traces / Wilson loops only |
| Λ sign / vacuum | reintroducing Λ<0 / R×H³ as the expected vacuum (the dead v17.0 cone-Hessian object) | CONVENTIONS §6 (corrected): Λ=0, flat M=0 vacuum; R×H³ falsified; measure Λ, do not assume Λ<0 |
| ε-contraction normalization | the Newton's-constant normalization put in by hand and called "forced" | The normalization must be read off the cubic norm; if hand-set → fp-imported-action (Pitfall 1) |

---

## "Looks Correct But Is Not" Checklist

- [ ] **Phase A reduction:** image dimension computed EXACTLY over Q and = 4 (not "a 4-dim sub-piece selected from a larger image") — verify `sympy` rank, not a chosen projection.
- [ ] **Phase A signature:** Gram signature = (1,3) over Q WITHOUT a Wick rotation rescuing it — verify exact eigenvalue signs.
- [ ] **Phase A forced-ness:** the reduction uses (E_11, u) ONLY — verify no extra basis/projection/idempotent choice was logged.
- [ ] **Phase A.5 sector:** the REAL part of the QGT reproduces Hess(−log det) exactly — verify before trusting the imaginary part F_B.
- [ ] **Phase A.5 same-wall:** the matter-source of F_B is matched to an independently-frozen T[M] in M-power AND trace structure AND support — verify it is not a traceless ∝F² (EM-shaped) object relabeled Einstein.
- [ ] **Phase A.5 gauge:** the F_B verdict is a gauge-invariant scalar, unchanged under a U(r) frame rotation — verify, do not read a frame-dependent component.
- [ ] **Phase B block:** the 4d Riemann is the LORENTZ block R(ω), not the translation/torsion block, and not the raw 45-dim Spin(9,1) curvature — verify the connection is the 10-dim A=ω⊕e.
- [ ] **Phase B tetrad:** e=π_u(dE) is invertible (det(e^a_μ)≠0 over Q) — verify non-degeneracy, not just 4-dimensionality.
- [ ] **Phase B vacuum:** M=0 is flat / pure-Λ (per §6), NOT R×H³ — verify Λ measured, not assumed; pure-∝e∧e is Λ, not matter.
- [ ] **Phase C ε-contraction:** the space of trace-form-invariant quadratic-in-F contractions is 1-dimensional AND equals the ε-contraction with the cubic-norm-fixed normalization — verify FORCED, else fp-imported-action.
- [ ] **Phase C independence:** every Phase B/C equation passes "could I write this without knowing the answer is Einstein?" — verify no MM action / −1/2 / SUSY / Weinberg import.
- [ ] **Einstein test:** holds across a ≥3-point (M,x) family with ONE predefined (κ,Λ) — verify not a single tuned point.
- [ ] **All decisive numbers:** exact over Q (ranks via sympy, never numpy) — verify no float decided a KILL/SURVIVE/Einstein verdict.

---

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
|---------|---------------|----------------|
| fp-imported-action discovered late (Phase C) | LOW (it is the honest verdict) | Report fp-imported-action as the outcome (B yes, C no) — the most likely real result, a publishable honest-partial; do NOT relabel a win |
| Phase A reduction not 4d/not Lorentzian/not forced | LOW (clean KILL) | Report the KILL flat ("Phase A: coframe reduction fails [clause]"); stop; a clean KILL is a full publishable pass |
| Phase A.5 same-wall mismatch | LOW (clean SOFT KILL) | Report "Lie sector inherits the symmetric-sector mismatch"; recommend STOP before B; the cheap version of the whole test |
| octonion_algebra.py used on a decisive path | MEDIUM | Re-run with `ring_lemma_verification.py` det_3; re-pass CH + 324/324; re-derive the affected coupling/curvature |
| Float decided a verdict | MEDIUM | Re-run exact over Q on rational data; if the exact result flips the verdict, the float verdict was wrong |
| Sector confusion (cone-Hessian reused) | HIGH | Excise the symmetric-sector import; recompute the imaginary-part F_B / connection F; re-verify the real-part consistency check separately |
| Watchdog stall on long symbolic run | LOW-MEDIUM | Recover committed work via git log (task-by-task commits); orchestrator commits+writes SUMMARY on stall; do NOT blind-re-run |

---

## Pitfall-to-Phase Mapping (the register)

| # | Pitfall | Guarding Phase | Verdict if triggered | Verification |
|---|---------|----------------|---------------------|--------------|
| 1 | **fp-imported-action** (MM/EH action posited; the GST sin) | C (ban declared 0/A) | fp-imported-action (honest partial) | 1-dim invariant-contraction space + normalization from cubic norm; independence audit |
| 2 | **fp-arbitrary-reduction** (4d coframe by a choice) | A (the KILL gate) | KILL | exact image dim=4, Gram (1,3), forced by (E_11,u) only |
| 3 | **Sector confusion** (cone-Hessian reused / symmetric object) | 0, A.5, B | regression to v17.0 NONE | real part = Hess(−log det); F is the imaginary-part/connection 2-form |
| 4 | **fp-relabel / same-wall** (EM-shaped F called Einstein) | A.5 (SOFT KILL), B/C | SOFT KILL / fp-relabel | M-power + trace structure + support matched to frozen T[M] |
| 5 | **Berry/QGT gauge & normalization** (covariant not invariant) | A.5, B | gauge artifact | verdict invariant under U(r); invariant scalars / Wilson loops; K=−1/2 calibration |
| 6 | **fp-float-decisive** | all (A, B, C) | false KILL/survive | exact over Q, sympy rank, never numpy |
| 7 | **Octonion non-associativity / banned lib** | 0 (gate), A, B | silent corruption | SSOT det_3; CH+324/324; association pre-flight on e_4..e_7 |
| 8 | Torsion vs curvature block | B | wrong block / unstated torsion-free assumption | Lorentz block = R(ω); torsion computed, not imposed |
| 9 | 45-dim ambient vs 10-dim gravity connection | B | wrong connection | A=ω⊕e is 10-dim; project to Spin(3,1) |
| 10 | Vacuum mis-read (Λ<0 / R×H³ / pure-Λ as matter) | A.5, B(d) | false positive / dead-object revival | flat per §6; decompose trace/traceless/Weyl; K=−1/2 |
| 11 | Single-point sampling | B, C | false position-dep / false Einstein | ≥3-point (M,x) family; one predefined (κ,Λ); ∂_x(inv)≢0 |
| 12 | Non-invertible soldering form | B(a) | degenerate tetrad | det(e^a_μ)≠0 over Q |
| 13 | Convention drift | 0 (freeze), all | invalid cross-phase comparison | freeze at 0; log & re-run on any change |

---

## Sources

- **Wise, D. K.**, "MacDowell-Mansouri gravity and Cartan geometry," gr-qc/0611154 (CQG 27 (2010) 155010) — THE reference: ε F∧F → Einstein-Hilbert + Λ + Euler; the auxiliary field B^{ab}=ε e∧e; Lorentz block = curvature, translation block = torsion; the ε-contraction is what selects Einstein (the heart of Pitfall 1). [https://arxiv.org/abs/gr-qc/0611154]
- **MacDowell, S. W. & Mansouri, F.**, Phys. Rev. Lett. 38 (1977) 739 — gravity as a broken (A)dS gauge theory; SO(3,2)/SO(4,1) → SO(3,1).
- **Provost, J. P. & Vallée, G.**, Comm. Math. Phys. 76 (1980) 289 — quantum geometric tensor: real part = Fubini-Study metric, imaginary part = Berry curvature (symplectic); the real/imaginary split underlying Pitfalls 3 and 5.
- **Wilczek, F. & Zee, A.**, non-abelian Berry phase / "Wilson loop and Wilczek-Zee phase from a non-Abelian gauge field," npj Quantum Information (arXiv:1910.13991); "Abelian and non-Abelian Berry curvatures in lattice QCD," arXiv:1712.02218 — non-abelian Berry curvature is gauge-COVARIANT (U(r)), Wilson loop invariant / line not (Pitfall 5).
- **Hehl, F. W. & Obukhov, Y. N.**, "Élie Cartan's torsion in geometry and in field theory, an essay," arXiv:0711.1535 — torsion = field strength of translations, curvature = field strength of rotations (Pitfall 8).
- **Electromagnetic stress-energy tensor** — Wikipedia "Electromagnetic stress-energy tensor"; "A characterization of the electromagnetic stress-energy tensor," arXiv:1101.2505 — T^μ_μ=0 (traceless), T~F² (quadratic in field strength), conformal; the EM-shaped discriminants for the same-wall trap (Pitfall 4).
- **Baez, J. C.**, "The Octonions," Bull. AMS 39 (2002) 145 — OP^2 = F_4/Spin(9) (16-dim), T_E OP^2 = V_{1/2}, h_3(O), F_4 (Pitfall 2). Cayley plane = trace-1 idempotents (Freudenthal-Jordan).
- **McCrimmon, K.**, *A Taste of Jordan Algebras* (2004) — Peirce decomposition, primitive idempotents, the E∘δ=(1/2)δ tangent identity (Phase 0, Pitfall 2).
- **Sharpe, R. W.**, *Differential Geometry: Cartan's Generalization of Klein's Erlangen Program* (1997) — Cartan connections, soldering forms, the non-degeneracy requirement (Pitfall 12).
- **Project-internal:** v17.0 `.gpd/research/archive-v17/PITFALLS.md` (the prior route's GST-sin, same-wall, single-point, octonion-association, and float-decisive post-mortem — inherited and adapted; NOTE the octonion_algebra.py SSOT designation there is SUPERSEDED by `ring_lemma_verification.py`); v17.0 Phase 73 NONE verdict ("a tensor appearing ≠ Einstein"; κT~10³<G; 12-point family); Phase 70.1 (η+h bridge, R×H³ falsified); CONVENTIONS §6 corrected 2026-06-01 (Λ=0, flat vacuum); `paper6-cartan-tetrad-prompt.md` (authoritative spec: Forbidden proxies, Pass/Fail summary, KILL/SOFT-KILL conditions, the det SSOT + octonion_algebra.py ban).

---

_Known pitfalls research for: Cartan/MacDowell-Mansouri/Berry-curvature gravity route on h_3(O) (v18.0)_
_Researched: 2026-06-01_
