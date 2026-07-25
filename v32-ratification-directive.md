# v32.0 RATIFICATION DIRECTIVE (conditional) + the zero-cost multiplet-ID tests
# Paste into the GPD session. Supersedes v32-gate0-amendment-directive.md's discriminator
# section (the 11-probe Gram is now OPTIONAL — the tests below use ONLY existing tensors).

## 1. RATIFIED AS DELIVERED (the verdict center held)

- **(3c) ‖TT(B3)‖² = (1/54)(TrM²)², κ forced, detM ABSENT** (5 probes incl. detM=−2,−7).
  Blog-side checked the arithmetic (2/27, 2/3, 128/27 vs (TrM²)² — all 1/54) and the
  degree-4 collapse (Cayley–Hamilton). This is the registered excitement threshold and it
  CLOSED. Ratified.
- **(Gate 2) ε = λ_L − 2Λ = 20, λ_L = 32** — convention pinned by the full battery
  (∇*∇ sign regressions through the same code path, Δ_L(g)=0 pinning R̊, gauge-image
  preservation, Schur on 3 directions). Ratified. Koiso-CONSISTENT (no TT at 12).
- **(3d) York dictionary closes exact over Q**; the v31 deferred positive-exhibit
  obligation is DISCHARGED by the explicit residues (tr_g=0, δ=0, ≠0). Ratified.
- **(3b) the direction-hypothesis failure caught honestly** (N(s01)=N(d1) ⇒ r differs).
  Ratified as a finding — and RESOLVED by §3 below.
- Controls 6/6 + 6/6, fences held, no Einstein-language leaks. Ratified.

## 2. NOT RATIFIED AS WRITTEN — doc corrections required (no new computation)

These stay OUT of any milestone text until corrected:

a. **"single-generator Gram rank-6 = the d-symbol image" is FALSE.** The d-symbol image
   of single generators {N(λ_a) = d_aac λ_c} lies in span{λ₃, λ₈}: rank **2** (your own
   75d6639d docstring; blog-side verified numerically). Rank 6 is NOT the d-image and the
   Gate-0 criterion rewrite (e295f0ce) was wrong-reasoned even though the observation was
   real. The TRUE explanation is §3.
b. **The "λ=12 multiplet" label is incoherent** with the measured λ_L=32 and must be
   retired (the doc currently uses "λ=12" as a carrier-level label and "32" as the
   eigenvalue of the same object).
c. **The "dim-8 su(3)-adjoint" ID is unverified** and contradicted by your own rank-6
   (a dim-8 adjoint probed by single generators through the d-channel gives rank 2).
d. **3a-as-run ≠ 3a-as-registered.** Registered: the extended solve B3 = Σc_a t_a + δ*ω
   + f·g consistent for SYMBOLIC M over the FROZEN basis. Run: per-matter extraction
   consistency (which never probes the basis span). The Scope line "the closed form
   TT(B3)=Σc_a t_a exists" is UNVERIFIED — and false over the frozen 8-element basis if
   §3 confirms (the basis spans a 6-dim slice of a 27-dim multiplet). Object (i) is
   currently STRUCTURE-UNKNOWN, not delivered. §3 completes it.

## 3. THE ZERO-COST FINGERPRINT TESTS (existing tensors only; minutes)

**The candidate truth (blog-side, every number independently computed):** the residue map
M ↦ TT(B3[M])^{(1,1)} is quadratic and SU(3)-equivariant, so it factors through
Sym²(8) = 1 ⊕ 8 ⊕ 27 (each multiplicity ONE). The 8-channel (d-square) is KILLED by an
already-proved v31 result: the level-1 component of φ_M² is itself a moment
(φ_M² = c₀TrM² + c₁φ_{N(M)} + level-2), and v31's B1 control proved moment-Hessians have
ZERO TT residue. So the residue is pure **27-channel**: TT(B3[M]) = T₂₇[P27(M⊗M)] with
T₂₇ equivariant — by Schur a scalar multiple of an isometry. That forces the ENTIRE Gram
of your already-extracted {t_a} up to one overall constant, plus two exact linear
identities. It also explains 3b exactly: P27 separates s01 from d1 while N cannot.

With your probe normalization (s01,a01,d1,s02,a02,s12,a12 = unit-entry λ₁..λ₇;
d2 = diag(1,1,−2) = √3·λ₈, so t_d2 = 3·t_λ8 by quadraticity):

**T1 (linear identity):** 4·(t_s01 + t_a01 + t_d1) + (t_s02 + t_a02 + t_s12 + t_a12) = 0
   — exact, block-for-block, as tensors.
**T2 (linear identity):** t_d2 = 9·(t_s01 + t_a01 + t_d1) — exact.
**T3 (the 28-entry Gram fingerprint):** the full predicted Gram, exact over Q
   (overall scale fixed by your own ‖t_s01‖² = 2/27):

   | pair type | predicted ⟨t_i, t_j⟩ |
   |---|---|
   | single diagonal (s01,a01,d1,s02,a02,s12,a12) | 2/27 |
   | d2 diagonal | 2/3 (✓ already matches your 3c table) |
   | within the su(2) triple {s01,a01,d1} | −26/729 |
   | conjugate quartet pairs (s02,a02) and (s12,a12) | −26/729 |
   | all other triple↔quartet and cross-quartet pairs | −2/729 |
   | triple ↔ d2 | +2/81 |
   | quartet ↔ d2 | −2/27 |

   Compare against the Gate-0 logged Gram (you already computed these integrals).
**T4 (the mechanism, one Δ_L application):** build u := traceless((i∂∂̄ R_M)^{(1,1)})
   from the level-2 scalar R_M (λ₂=32, already in the code). Check Δ_L^{(1,1)} u = 32·u.
   Mechanism: on Kähler–Einstein, Δ_L∘i∂∂̄ = i∂∂̄∘Δ, so the multiplet is the i∂∂̄-image
   of the level-2 (2,2) scalars — **dim 27, at exactly λ_L = λ₂ = 32** (which is WHY the
   two numbers coincide; the verdict's "λ₁ + Weitzenböck shift" gloss should be replaced
   by this). Optionally check ⟨u, t_a⟩ ≠ 0 (the residues live in that image).

## 4. ON CONFIRMATION (T1+T2 pass, T3 matches): the v32.0-A amendment

1. **Multiplet ID:** the λ_L=32 (1,1)-Hermitian **dim-27** multiplet (the SU(3) (2,2)),
   = i∂∂̄(level-2 scalars). Replaces "λ=12 dim-8 su(3)-adjoint" EVERYWHERE in 92-*.
   Gate-0's gram criterion documents the verified structure: singles-rank-6 = the rank of
   {P27(λ_a⊙λ_a)} (blog-verified), N-rank-8 retired as scaffolding (wrong channel).
2. **Object (i) COMPLETES:** TT(B3[M]) = T₂₇[P27(M⊗M)], ONE forced constant by Schur +
   multiplicity-one — the same rigidity class as the failed N-hypothesis, one level up.
   3b's "richer than N(M)" RESOLVES into this exact direction. The norm identity (3c) is
   its squared-norm shadow: |P27(M⊗M)|² ∝ (TrM²)² (degree-4 collapse), κ = 1/54 the one
   constant. The polarized constructive basis (r_ab := ½[r(λ_a+λ_b)−r(λ_a)−r(λ_b)],
   28 sparse extractions, spans all 27 — blog-verified) is PRICED for v33, not required
   for v32.0-A: the structural form + fingerprint is the deliverable.
3. **c₈ = 0 recorded as a THEOREM-from-parts:** level decomposition of φ_M² + v31's
   B1-control (moment-Hessian TT ≡ 0) + multiplicity-one. The d-channel had nothing to
   land in. (This also retires the "is there a TT 8 at all?" question for this level.)
4. **v31 amendment note (one line, verdict UNTOUCHED):** the residue's multiplet
   attribution amends dim-8 → dim-27 at λ_L=32; the deficit-1 rep-theory lock transfers
   verbatim (Sym²(8) ⊃ 27 exactly once); existence/nonzeroness/(1,1)/deficit-1 unchanged.
5. **Literature re-map (documentation):** locate the (1,1) 27 at λ=32 in Boucetta
   Table VIII n=2; identify what the v31 "λ=12 dim-8" row actually is (likely the gauge
   sector or a different operator convention); state the Koiso paradox of the OLD reading
   and its resolution explicitly in RESEARCH.
6. THEN: VERDICT = LIVE stands (the center never moved), milestone text uses the amended
   IDs, HOLD for human ratification as usual.

## 5. IF T1 OR T2 FAILS

The 27 story is wrong too. HOLD, commit the failure pattern (which identity, the residual
tensor's nonzero blocks), do NOT improvise a third ID. The blog side re-derives.

## 6. Drift note (record, no penalty to the center)

Two drift instances this run, both trap-#17-family (criterion adjusted to match an
observation without a correct theory): the Gate-0 rank rewrite (e295f0ce) and the 3a
redefinition. Neither touched the norm/ε/York legs (channel-robust). Record both in
RESEARCH §"what the run changed mid-flight" so the milestone support chain is honest.
Fences unchanged throughout; exact arithmetic over Q.

## 7. BLOG-SIDE RESULT (added after §3 was run locally): T1/T2/T3 ALL PASS — the 27 is FACT

The fingerprint tests were run blog-side on YOUR OWN driver (same `build_basis`, same
`l2_tensor`, exact over Q; 8 extractions + 36 integrals, ~5 min): both linear identities
hold block-for-block (`t_d2 = 9(t_d1+t_s01+t_a01)`; `4t_d2 + 9(t_s02+t_s12+t_a02+t_a12) = 0`)
and the full 36-entry observed Gram is EXACTLY proportional to the predicted P27 Gram
(diag 2/27; d2 2/3; in-triple and conjugate-pair −26/729; cross −2/729; triple↔d2 2/81;
quartet↔d2 −2/27). Log: /tmp/fingerprint_check.log (blog machine).

**Rigor upgrade (cite in the amendment):** the channel Grams G₁, G₈, G₂₇ are linearly
independent PSD matrices, so exact proportionality to G₂₇ forces c₈ = c₁ = 0 IDENTICALLY
(not merely on the probe span). The trivial channel is empty anyway (no SU(3)-invariant
TT (1,1) tensor exists — the unique invariant is g, not traceless). And since the
equivariant image of an irrep is zero or a full copy, the residue span over all M IS a
full dim-27 multiplet — the ID is rigorous WITHOUT the polarized basis (polarization
stays priced for v33 only if explicit 27-basis tensors are wanted).

Your remaining work, in order:
1. Re-run T1/T2/T3 executor-side and COMMIT (the protocol wants the certificate in-repo;
   adapt §3 or request the blog-side script).
2. The §2 doc corrections + §4 amendments (multiplet ID, 3a/object-(i) honest status →
   completes as TT(B3[M]) = T₂₇[P27(M⊗M)], the c₈=0 theorem-from-parts, v31 one-line
   amendment, drift note §6).
3. T4 (the i∂∂̄/level-2 mechanism check) — recommended, one Δ_L application, makes the
   λ_L = λ₂ = 32 coincidence mechanical in RESEARCH.
4. The Boucetta Table VIII re-map note.
Then VERDICT = LIVE stands as v32.0-A and the milestone HOLD proceeds as usual.
