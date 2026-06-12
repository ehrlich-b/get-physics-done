# Phase 92 (v32.0-candidate) — GATE 2 SUMMARY: The Threshold Number ε

**Driver:** `python3 -u code/lichnerowicz_response.py g2` → **PASS** (exact over Q).

Gate 2 computes the genuine factual sub-fork: the Lichnerowicz eigenvalue `λ_L` of the λ=12
(1,1)-Hermitian multiplet, and `ε = λ_L − 2Λ = λ_L − 12`. **Both branches were a priori informative;
no prior was registered. The value was COMPUTED exactly over Q, NOT adjudicated from the literature.**

## The result

| quantity | value | meaning |
|---|---|---|
| **λ_L** (Schur scalar) | **32** | the Δ_L^{(1,1)} eigenvalue on the multiplet — the SAME constant for all nonzero single-generator t_a (Schur; the multiplet is irreducible) |
| **2Λ** | 12 | the Einstein-marginal threshold (Λ = λ₁/2 = 6) |
| **ε = λ_L − 2Λ** | **20** | the multiplet is NON-marginal; ε ≠ 0 is canonical response-stiffness data |

`Δ_L^{(1,1)} t_a = 32 t_a` for every nonzero single-generator residue (the Schur check; the constant
agrees across directions because the (1,1)-Hermitian λ=12 multiplet is an irreducible su(3) adjoint).
**ε = 32 − 12 = 20 ≠ 0.**

## The ε reading — mechanical (trap #16/#18, NO convention-picking)

**ε = 20 ≠ 0 ⇒ the λ=12 (1,1) multiplet is NON-marginal under our certified convention.** The
trap-#16 tension among
- Besse 12.28: infinitesimal Einstein deformations = `ker(Δ_L − 2Λ)|_TT`,
- Besse 12.98: CP^n is Koiso-RIGID (no infinitesimal Einstein deformations),
- Boucetta's table placing the (1,1) TT multiplet "at" λ=12 = 2Λ,

is resolved FACTUALLY and mechanically. Under OUR certified convention — `Δ_L h = ∇*∇h + 12h − 2R̊h`
with `∇*∇ = −Δ_analyst` pinned at Gate 0/1e (+12 on λ₁, +32 on λ₂), and the full Kähler Weitzenböck
`R̊` cross-checked by `R̊(g) = Ric = 6g` and `Δ_L(g) = 0` — the Lichnerowicz eigenvalue on the (1,1)
multiplet is **λ_L = 32, NOT 12**. So the multiplet is **NOT Einstein-marginal**; it lies a finite
gap `ε = 20` above the 2Λ threshold. This is fully CONSISTENT with Koiso rigidity of CP^n (Besse
12.98): CP² has NO infinitesimal Einstein deformations, exactly because `ker(Δ_L − 2Λ)|_TT = ∅` here
(λ_L = 32 ≠ 12 = 2Λ). The apparent "λ=12" of Boucetta's (1,1) TT mode is the SCALAR Laplacian
eigenvalue of the carrier (the moment fields' threshold), NOT the Lichnerowicz eigenvalue — the two
differ by the curvature/Weitzenböck term. **NAMED mechanically: λ_L (Lichnerowicz) = λ₁(scalar) + the
Weitzenböck shift; they are NOT the same operator.** ε = 20 stands as computed; no convention was
chosen to force a marginal answer.

(If ε had been 0, the Fredholm/response reading would have been fenced as a second-order
obstruction-theoretic statement per trap #19. Since ε ≠ 0, the multiplet is non-marginal and ε is
genuine response-stiffness data — but the Fredholm/sourced-response EQUATION is STILL not run here
(trap #19): "response" is priced only, in the Gate-5 ledger.)

## Scope fence (binding, verbatim)

This is the deformation-complex DICTIONARY of a FROZEN imported geometry. No dynamical metric, no
selection law, no κ. LIVE = "the tensor sector's source data closes in canonical form" — a DICTIONARY
fact, not a dynamics fact. No Einstein-equation / Newton-constant / G=κT / dark-matter / geodesic
language; frozen FS geometry USED not derived; the v18/v20 MM corpse stays buried; OP² priced only.
Does NOT retract v17–v21 (Block-C statements; v32 is the strictly weaker upstream dictionary). ε = 20
is a Δ_L-stiffness number of the frozen geometry's deformation complex, NOT a dynamical response.
