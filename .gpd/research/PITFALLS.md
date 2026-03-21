# Known Pitfalls Research

**Domain:** Quantum foundations / algebraic quantum theory -- deriving C*-structure from sequential product axioms applied to self-modeling systems
**Researched:** 2026-03-20
**Confidence:** MEDIUM (pitfalls in the established literature are well-documented; pitfalls specific to the novel self-modeling construction are inferred from structural analogies and require validation)

## Critical Pitfalls

### Pitfall 1: Checking S1-S7 Against Quantum Sequential Products Instead of the Self-Modeling Construction

**What goes wrong:**
S1-S7 hold trivially for the standard quantum sequential product a & b = sqrt(a) b sqrt(a) on B(H). The entire point of this project is to check them for the *self-modeling* sequential product ("test a on B, update M, test b on B"), which is a different operation. It is extremely easy to slip into verifying axioms for the standard Luders-rule product and declaring victory. This is the false progress mode the user explicitly flagged.

**Why it happens:**
The quantum sequential product is the best-studied example. When formalizing "test-update-test," the natural move is to represent it in Hilbert space -- but then you have already assumed the conclusion. The self-modeling construction lives in an order unit space whose structure is *to be determined*; it does not yet have a Hilbert space representation.

**How to avoid:**
Work entirely within the abstract order unit space framework. Define the self-modeling sequential product using only the operational primitives (effects, states, the update map) without importing Hilbert space structure. Every axiom verification must reference properties of the *self-modeling update rule*, not properties of sqrt(a) b sqrt(a).

**Warning signs:**
- Any step that invokes "let H be the Hilbert space of the system"
- Any use of the spectral theorem before the Jordan algebra structure is established
- Proofs that work identically for any sequential product (they prove nothing specific to the self-modeling case)

**Phase to address:** Phase 1 (Sequential Product Formalization), from the very first task

---

### Pitfall 2: Wrong Effect Algebra Carrier -- Effects on B vs Effects on B x M

**What goes wrong:**
The sequential product must be defined on an effect algebra, but there are two natural candidates: E(B) (effects on the body alone) and E(B x M) (effects on the body-model composite). Choosing wrong invalidates the entire axiom verification. The two choices give different sequential products with potentially different properties.

**Why it happens:**
The self-modeling operation involves *both* B and M: you test on B, but the update modifies M. If you define the sequential product on E(B), you must explain how the M-update enters. If you define it on E(B x M), you must explain why the "test" operation acts only on the B-marginal. Neither framing is obviously correct, and the literature on sequential products (Gudder-Greechie 2002, van de Wetering 2018) works with effects on a single system.

**How to avoid:**
Explore both framings explicitly in Phase 1. For each framing:
1. Write out the sequential product formula in terms of the operational primitives
2. Check whether the formula is well-defined (closure, range in [0,1])
3. Check S1-S7 for that specific formula
4. If one framing makes S4 fail and the other makes it hold, that resolves the question

The correct framing is a *result* of Phase 1, not a premise. Do not commit to one framing prematurely.

**Warning signs:**
- Axiom proofs that never mention M (suggests effects-on-B framing was adopted without justification)
- Axiom proofs that treat B and M symmetrically (the self-model is asymmetric: B is tested, M is updated)
- A sequential product formula that does not reduce to the standard one when B is a quantum system and M is trivial

**Phase to address:** Phase 1, Task 1 (formalization of the sequential product)

---

### Pitfall 3: S4 (Symmetry of Orthogonality) Assumed Rather Than Proved

**What goes wrong:**
S4 states: if a & b = 0 then b & a = 0 (orthogonality is symmetric with respect to the sequential product). For the standard quantum product, this follows from sqrt(a) b sqrt(a) = 0 iff sqrt(b) a sqrt(b) = 0 (proven by spectral arguments). For the self-modeling product, S4 encodes the claim that "testing a then b yields zero" implies "testing b then a yields zero" -- but the M-update between tests breaks time-reversal symmetry. The self-modeling update after testing a may put M in a state where b's test behaves differently than it would on the original state.

**Why it happens:**
S4 is the subtlest axiom. S1-S3 and S5-S7 constrain algebraic structure (additivity, continuity, unit, compatibility). S4 constrains *information flow*: orthogonality cannot depend on testing order. In a self-model, testing order determines how M is updated, which determines what subsequent tests "see." The M-update channel introduces an asymmetry that the standard quantum product does not have.

**How to avoid:**
S4 is the make-or-break axiom. It must be either:
(a) Proved from explicit properties of the self-modeling update map (what *specific* property of the update ensures orthogonality symmetry?), or
(b) Disproved by constructing a concrete self-modeling system where a & b = 0 but b & a != 0

Do NOT argue S4 holds "because it's physically reasonable" or "because it holds in quantum mechanics." The entire point is to *derive* quantum structure, not assume it.

**Warning signs:**
- S4 proof is shorter than 1 page (it should be the hardest axiom to verify)
- S4 proof uses properties of the update map that have not been independently established
- S4 proof works for any update map (then it proves too much -- not all updates give quantum structure)

**Phase to address:** Phase 1, Task 2 (axiom verification), specifically S4

---

### Pitfall 4: Conflating Local Tomography with Independent Accessibility

**What goes wrong:**
Phase 2 must show that B-M compositionality implies local tomography. Local tomography means: the state rho_BM is determined by all product measurements {Tr((a_B tensor b_M) rho_BM)}. Independent accessibility means: the self-model can perform measurements on B alone and M alone. These are NOT the same thing. Independent accessibility says you *can* measure each subsystem; local tomography says product measurements *suffice* to determine the joint state. The gap is the entangled sector: product measurements may not resolve entangled states.

**Why it happens:**
In standard quantum mechanics over C, local tomography holds automatically (the tensor product of matrix algebras is a matrix algebra, and product effects span the dual). But local tomography FAILS for:
- Real quantum mechanics (R-QM): the tensor product of real matrix algebras has an entangled sector invisible to product measurements
- Quaternionic quantum mechanics (H-QM): dim(H_n tensor H_m) < dim(H_n) * dim(H_m) as vector spaces, so product effects cannot span
- Spin factors (V_n for n != 3): no locally tomographic composite exists for most spin factors

If the self-modeling construction produces a Jordan algebra that is not a complex matrix algebra (e.g., a spin factor or a real/quaternionic type), local tomography will fail even though independent accessibility holds.

**How to avoid:**
Do not assume the Jordan algebra from Phase 1 is a complex matrix algebra. The Jordan-von Neumann-Wigner classification gives five types of simple EJAs:
1. Self-adjoint real matrices (R_n)
2. Self-adjoint complex matrices (C_n) -- STANDARD QM
3. Self-adjoint quaternionic matrices (H_n)
4. Spin factors (V_n)
5. Exceptional Albert algebra (M_3(O), 27-dimensional)

Only type 2 supports local tomography in the standard sense. Phase 2 must either:
(a) Show the self-modeling construction forces type 2 specifically, or
(b) Identify an additional property of the self-model (beyond independent accessibility) that rules out types 1, 3, 4, 5

Key reference: Barnum and Wilce (2014), "Local tomography and the Jordan structure of quantum theory," arXiv:1202.4513. They show that local tomography + Jordan structure + a qubit-like system = complex QM.

**Warning signs:**
- Phase 2 proof never mentions the Jordan algebra type
- Proof of local tomography that would work equally well for R-QM or H-QM (both violate it)
- No discussion of the exceptional Jordan algebra or spin factors

**Phase to address:** Phase 2 (Local Tomography from B-M Compositionality)

---

### Pitfall 5: The Exceptional Jordan Algebra Obstruction

**What goes wrong:**
Even if S1-S7 hold and produce a Jordan algebra, the exceptional Albert algebra M_3(O) (3x3 self-adjoint octonion matrices, 27-dimensional) is a valid Euclidean Jordan algebra that admits NO composition with any non-trivial system. It cannot appear as a factor in a locally tomographic composite. If the self-modeling construction produces an Albert algebra factor, the entire Phase 2 program collapses -- not because local tomography fails to hold, but because the composite B x M cannot be formed within the Jordan framework.

**Why it happens:**
Octonions are not associative, so tensor products of octonionic matrix algebras are not well-defined as Jordan algebras. This is the Hanche-Olsen obstruction: the only Euclidean Jordan algebras admitting a well-behaved tensor product (forming a symmetric monoidal category) are the complex ones. The Albert algebra is an isolated exceptional point in the classification.

**How to avoid:**
The self-modeling construction inherently involves composition (B and M are subsystems of a composite). If the construction is well-defined, this composition requirement should automatically exclude the Albert algebra. But this needs to be checked explicitly: does the requirement that B and M form a composite with independently accessible subsystems force the Jordan algebra to be a complex matrix algebra?

This is actually where the self-modeling framework may contribute something novel: the existence of the B-M composite structure is a *built-in* compositionality constraint that other reconstruction programs must postulate separately.

Reference: Barnum, Mueller, Ududec (2014), "Higher-order interference and single-system postulates characterizing quantum theory," arXiv:1403.4147. Also: Barnum, Ududec, van de Wetering (2020), "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359.

**Warning signs:**
- Jordan algebra type not explicitly determined after Phase 1
- No argument excluding the Albert algebra before invoking local tomography
- Composition of B and M assumed without verifying it is well-defined in the Jordan framework

**Phase to address:** Phase 1 (establishing the Jordan type) and Phase 2 (compositionality)

---

### Pitfall 6: Circularity -- Smuggling Quantum Structure into the Update Map

**What goes wrong:**
The self-modeling sequential product depends on the update rule: "test a on B, update M according to result, test b on B." If the update rule is defined using Luders' rule (state -> sqrt(a) rho sqrt(a) / Tr(a rho)), quantum structure is assumed in the update map, and deriving it from S1-S7 is circular. More subtly, if the update rule is defined using *any* map that implicitly assumes an inner product, involution, or Hilbert space structure, the derivation is circular.

**Why it happens:**
This is the central pitfall of all QM reconstruction programs. D'Ariano (2006, quant-ph/0611094) explicitly notes that the involution corresponding to "complex conjugation" must be derived operationally, not assumed. In the self-modeling context, the update map must be defined using only:
- The effect algebra structure (partial order, orthocomplement, sequential composition)
- The self-modeling constraint (M must track B)
- Order unit space structure (states, effects, evaluation pairing)

Any additional structure in the update map is smuggled quantum mechanics.

**How to avoid:**
Define the update map axiomatically from the self-modeling requirement. Candidate: the update map is the *unique* map that keeps M's state consistent with the information gained by testing a on B. This is a Bayesian update in the generalized probabilistic theory (GPT) sense, not necessarily a Luders update. The key question is: what properties of this Bayesian update are forced by the self-modeling constraint?

Check: if you replace "self-modeling system" with "classical Bayesian agent," does the update map give a commutative sequential product? It should -- classical Bayesian updating gives commutative statistics. If it also gives a non-commutative sequential product for the general case, you have a genuine derivation.

**Warning signs:**
- Update map defined by formula involving sqrt, adjoint, or inner product
- Update map assumed to be a completely positive map (this assumes C*-structure)
- No explicit statement of what structure the update map is allowed to use

**Phase to address:** Phase 1, Task 1 (formalization)

---

### Pitfall 7: The Norm Completion Trap in Finite Dimensions

**What goes wrong:**
The v2-plan states "Norm: FREE (automatic in finite dims)." This is correct for C*-algebras (the C*-norm is unique on a finite-dimensional *-algebra), but it is NOT free in the order unit space setting. The order unit norm on an order unit space is ||a|| = inf{r > 0 : -r*1 <= a <= r*1}. This norm depends on the order structure, which depends on the cone of positive elements, which depends on the Jordan product. The claim that the norm is "free" hides the assumption that the order structure is already determined.

**Why it happens:**
In finite dimensions, all norms are equivalent, so people casually say "the norm doesn't matter." But the *specific* C*-norm satisfies ||a*a|| = ||a||^2, which is the C*-identity. This identity is what makes C*-algebras special (it connects the algebraic and topological structure). In the Jordan-to-C* promotion, the norm enters through the spectral radius and the GNS construction. Getting the wrong norm gives the wrong inner product on the GNS Hilbert space.

**How to avoid:**
Do not claim the norm is free until after the C*-identity has been established. In van de Wetering's framework, the norm is determined by the Jordan algebra structure (through spectral theory of EJAs), and the C*-identity follows from the local tomography step. Track this dependency explicitly.

**Warning signs:**
- Invoking the C*-identity before establishing the involution
- Claiming equivalence of norms to skip norm verification
- Using completeness arguments in a finite-dimensional context (vacuous but misleading)

**Phase to address:** Phase 2 (Jordan to C* promotion)

## Moderate Pitfalls

### Pitfall 8: Gudder's S4 vs Van de Wetering's S4 -- Axiom Version Mismatch

**What goes wrong:**
Gudder and Greechie (2002) defined sequential products on effect algebras with different axioms than van de Wetering (2018). The numbering "S1-S7" is from van de Wetering's paper, but earlier literature uses different axiom sets. In particular, Gudder's "symmetry" conditions concern commutativity of the sequential product (a & b = b & a when a and b are compatible), while van de Wetering's S4 concerns symmetry of *orthogonality* (a & b = 0 implies b & a = 0). These are logically distinct conditions.

**Why it happens:**
The sequential product literature evolved rapidly between 2002 and 2020. Gudder-Greechie, Gudder (2005 open problems), van de Wetering (2018, 2020), and Westerbaan-Westerbaan-van de Wetering (2020) each use slightly different axiom sets. Citing the wrong version or mixing axioms from different papers produces invalid arguments.

**How to avoid:**
Pin all axiom references to van de Wetering (2018), arXiv:1803.11139, Theorem 1. Use his exact formulations. When citing Gudder-Greechie for context, explicitly note where the axioms differ from van de Wetering's.

**Warning signs:**
- Axiom proofs that cite Gudder-Greechie for S4 (they use different formulations)
- Axiom numbering that does not match arXiv:1803.11139
- Conflation of "commutativity of compatible effects" with "symmetry of orthogonality"

**Phase to address:** Phase 1 (axiom verification)

---

### Pitfall 9: Associativity Implies Commutativity in Normal SEAs

**What goes wrong:**
Westerbaan, Westerbaan, and van de Wetering (2020, "The three types of normal sequential effect algebras," Quantum 4, 378) proved that associativity of the sequential product forces normal SEAs satisfying their axioms to be commutative. If the self-modeling sequential product turns out to be associative, the resulting algebra is necessarily commutative (classical), and the entire program fails -- no quantum structure emerges.

**Why it happens:**
The self-modeling operation "test a, update, test b, update, test c" might seem to be associative: (a & b) & c = a & (b & c) if the update rule composes. But associativity is too strong -- it kills non-commutativity. The standard quantum sequential product is NOT associative: sqrt(sqrt(a) b sqrt(a)) c sqrt(sqrt(a) b sqrt(a)) != sqrt(a) sqrt(b) c sqrt(b) sqrt(a) in general.

**How to avoid:**
Verify early in Phase 1 that the self-modeling sequential product is non-associative. If it is associative, STOP -- the program cannot produce quantum structure. Non-associativity of the sequential product is a *necessary* condition for the Jordan algebra to be non-commutative (and hence for the C*-algebra to be non-commutative).

**Warning signs:**
- Self-modeling sequential product that composes simply (a & b) & c = a & (b & c)
- No explicit check of non-associativity
- Update rule that factorizes: update(a then b) = update(a) followed by update(b)

**Phase to address:** Phase 1 (early structural check)

---

### Pitfall 10: D'Ariano Backup Route -- Faithful State Existence Is Non-Trivial

**What goes wrong:**
Phase 4 (D'Ariano backup) requires a "symmetric faithful state" on the algebra of observables. D'Ariano (2006, quant-ph/0611094) uses this to construct the involution. But the existence of a symmetric faithful state is a non-trivial assumption. For the self-modeling construction, the natural candidate is the B-M correlation state (the state describing how well M tracks B). This state may not be faithful (it might have a kernel -- observables that the self-model cannot distinguish), and it may not be symmetric under the exchange that defines the involution.

**Why it happens:**
D'Ariano's Postulate 5 (existence of a symmetric faithful state) is precisely the postulate that allows the involution to be constructed operationally. It is not automatic from the other postulates. In the self-modeling context, faithfulness requires that the B-M correlation resolves all observables, which is a strong claim about the quality of the self-model.

**How to avoid:**
If Phase 1 fails and the D'Ariano backup is triggered, the first task must be verifying that the B-M correlation state satisfies D'Ariano's Postulate 5 (symmetric and faithful). Do not assume it. Check:
- Faithfulness: rho(a*a) = 0 implies a = 0 (or in the Jordan setting: rho(a^2) = 0 implies a = 0)
- Symmetry: rho(a . b) = rho(b . a) where . is the Jordan product (this is automatic for a trace state, but the B-M state may not be a trace state)

**Warning signs:**
- Assuming the B-M correlation state is faithful without proof
- Not checking whether the correlation state has a kernel
- Confusing "the self-model tracks B" with "the self-model resolves all observables on B"

**Phase to address:** Phase 4 (D'Ariano backup, only if Phase 1 fails)

---

### Pitfall 11: Finite vs Infinite Dimension -- Scope Creep

**What goes wrong:**
All of the key theorems (van de Wetering's Theorem 1, Jordan-von Neumann-Wigner classification, Artin-Wedderburn) have finite-dimensional versions that are cleaner than their infinite-dimensional generalizations. The project is explicitly scoped to finite dimensions. But it is tempting to generalize: "this should also work in infinite dimensions." Infinite-dimensional generalizations introduce JB-algebras (instead of EJAs), von Neumann algebras (instead of matrix algebras), Type II and III factors, and the failure of nice classification theorems.

**Why it happens:**
Referees and self-review will ask "does this generalize?" The honest answer is "we do not know, and that is a separate paper." Attempting the generalization mid-project derails the core argument.

**How to avoid:**
State "all systems are finite-dimensional" as a standing assumption in every theorem statement. Defer infinite-dimensional generalization to future work. Note explicitly where the proofs use finite-dimensionality (e.g., spectral theorem for finite-dimensional Jordan algebras, automatic norm completeness).

**Warning signs:**
- Citing JB-algebra results instead of EJA results
- Using weak-* topology arguments (only needed in infinite dimensions)
- Attempting to handle the Type II_1 or Type III factor case

**Phase to address:** All phases (standing assumption)

## Approximation Shortcuts

| Shortcut | Immediate Benefit | Long-term Cost | When Acceptable |
| -------- | ----------------- | -------------- | --------------- |
| Assume the self-model is "ideal" (perfect tracking) | Simplifies update map | Real self-models have finite precision; results may not hold for approximate tracking | For the initial axiom verification (Phase 1), but must be revisited for robustness |
| Assume B and M have the same dimension | Simplifies composition structure | Self-models may need dim(M) > dim(B) to track complex behavior; equal dimension is a special case | Never -- keep dimensions independent from the start |
| Assume the Jordan algebra is simple (no direct sum decomposition) | Avoids superselection sector complications | Self-modeling systems may naturally have superselection sectors (classical labels + quantum observables) | For a first pass, but the full argument must handle direct sums |
| Skip the Albert algebra exclusion | Saves one argument step | Leaves a logical gap that referees will catch; the exceptional Jordan algebra is the canonical counterexample to naive Jordan-implies-C* claims | Never |

## Convention Traps

| Convention Issue | Common Mistake | Correct Approach |
| ---------------- | -------------- | ---------------- |
| Sequential product notation: a & b vs a . b vs a circ b | Confusing the sequential product (non-commutative) with the Jordan product (commutative) | Use a & b for sequential product, a . b for Jordan product; they are related (a . b = (a & b + b & a)/2 in the standard case) but distinct |
| Effect algebra ordering | Confusing the algebraic order (a <= b iff b - a is positive) with the informational order (a is more informative than b) | The algebraic order on effects is: a <= b iff b - a is an effect. This determines the cone structure. Always specify which order is meant. |
| Orthogonality: algebraic vs operational | a perp b in the effect algebra (a + b <= 1) vs a and b give mutually exclusive outcomes | These coincide in quantum mechanics but may diverge in general. Van de Wetering's S4 uses the sequential product to define orthogonality: a perp b iff a & b = 0 |
| Self-adjointness convention | Assuming observables are self-adjoint (a = a*) before the involution is established | Before Phase 2, there is no involution. "Observable" means "element of the order unit space." Self-adjointness is a consequence, not an assumption. |

## Numerical Traps

This project is primarily proof-work, not computational. However, if small verification calculations are used:

| Trap | Symptoms | Prevention | When It Breaks |
| ---- | -------- | ---------- | -------------- |
| Using numpy matrix operations to verify Jordan algebra identities | Floating point errors mask exact zero/non-zero distinctions | Use sympy (exact arithmetic) for all algebraic identity checks | Any dimension > 3, where floating point accumulation matters |
| Testing S4 on random effects | Random effects are generically in general position -- S4 might hold generically but fail on a measure-zero set that matters | Test S4 on corner cases: projectors, extreme effects, maximally non-commuting pairs | When the sequential product has symmetry that makes generic and special cases behave differently |
| Verifying local tomography by dimension counting | dim(A tensor B) = dim(A) * dim(B) holds for complex matrix algebras but fails for real/quaternionic types | Check local tomography by constructing the product effect span explicitly, not just by counting dimensions | Real quantum theory (dim(R_n tensor R_m) > dim(R_n) * dim(R_m) as state spaces) |

## Interpretation Mistakes

| Mistake | Risk | Prevention |
| ------- | ---- | ---------- |
| "S1-S7 hold, therefore quantum mechanics" | Skips the Jordan-to-C* promotion step (local tomography). S1-S7 give a Jordan algebra, which could be real, quaternionic, spin factor, or exceptional -- not necessarily quantum. | Phase 1 establishes Jordan structure. Phase 2 (local tomography) is required separately. |
| "Local tomography holds, therefore complex quantum mechanics" | Local tomography + Jordan = C*, but this requires compositionality of the Jordan algebra. If the composite B x M is not itself a Jordan algebra with the right properties, the promotion fails. | Verify compositionality explicitly using Barnum-Ududec-van de Wetering (2020) results. |
| "S4 fails, therefore the program fails" | S4 failure means the van de Wetering route fails, but the D'Ariano backup (Phase 4) is independent. Also, S4 failure for one effect algebra framing does not mean it fails for the other. | If S4 fails: (1) try the other framing, (2) characterize exactly how it fails, (3) try Phase 4. |
| "S4 holds for my specific example, therefore S4 holds generally" | A specific self-modeling system (e.g., qubit body + qubit model) may satisfy S4 due to dimension-specific accidents, not from general structural reasons. | Prove S4 for arbitrary finite dimension, or identify the precise condition on dim(B) and dim(M) that makes it hold. |

## Publication Pitfalls

| Pitfall | Impact | Better Approach |
| ------- | ------ | --------------- |
| Claiming "QM from one premise" without flagging L4 as metaphysics | Referees at Foundations of Physics will immediately reject; overclaiming is the #1 review failure mode | "QM from one operational premise (L4), given the algebraic genericity framework." Honest about the conditional. |
| Not citing the full chain of prior results (van de Wetering, Barnum-Wilce, Gudder-Greechie, D'Ariano) | Perceived as reinventing known results; damages credibility | The novel contribution is connecting self-modeling to sequential products. Everything else is established; cite it generously. |
| Presenting the conditional result (L4 + C*) as a failure | Both results (one-premise and two-premise) are publishable; the two-premise version is actually cleaner and more defensible | Frame the conditional result positively: "We reduce the C*-assumption to sequential product axioms S1-S7. If S4 holds for self-models, the C*-assumption is eliminated entirely." |

## "Looks Correct But Is Not" Checklist

- [ ] **S4 proof:** Often missing the case where a and b are not in general position -- verify on projectors and extreme effects, not just generic elements
- [ ] **Effect algebra closure:** Often missing that the sequential product must map effects to effects (0 <= a & b <= 1) -- verify the range, not just the algebraic formula
- [ ] **Update map well-definedness:** Often missing that the update map must preserve the state space (map states to states) -- verify positivity and normalization
- [ ] **Jordan product recovery:** Often missing the factor of 2 -- the Jordan product is a . b = (a & b + b & a)/2, not a & b + b & a
- [ ] **Local tomography dimension check:** Often missing that local tomography requires dim(state space of composite) = dim(state space of A) * dim(state space of B) -- verify this equality, not just inequality
- [ ] **Compositionality of the Jordan algebra:** Often assuming the tensor product of two EJAs is an EJA -- this fails for the Albert algebra, spin factors, and quaternionic systems (Barnum et al. 2020)

## Recovery Strategies

| Pitfall | Recovery Cost | Recovery Steps |
| ------- | ------------- | -------------- |
| Wrong effect algebra framing (Pitfall 2) | MEDIUM | Re-do Phase 1 axiom verification with the other framing. If both framings were explored in parallel from the start, cost is LOW. |
| S4 fails (Pitfall 3) | MEDIUM-HIGH | Characterize the failure precisely (which self-modeling systems, which effects). Try Phase 4 (D'Ariano backup). Ship conditional result if both fail. |
| Circularity in update map (Pitfall 6) | HIGH | Must re-derive the update map from scratch without quantum assumptions. May require rethinking the formalization entirely. |
| S1-S7 hold but Jordan algebra is non-quantum type (Pitfall 4/5) | MEDIUM | Phase 2 explicitly handles this. Need additional argument (local tomography) to select complex QM. If self-modeling construction inherently excludes non-complex types, this is actually a positive result. |
| Associativity kills non-commutativity (Pitfall 9) | HIGH | Fundamental obstruction. If the self-modeling sequential product is associative, the program cannot produce quantum structure. Must rethink the update map to break associativity. |

## Pitfall-to-Phase Mapping

| Pitfall | Prevention Phase | Verification |
| ------- | ---------------- | ------------ |
| P1: Checking standard QM instead of self-model | Phase 1, Task 1 | Review: does any step invoke Hilbert space structure? |
| P2: Wrong effect algebra carrier | Phase 1, Task 1 | Both framings explored; correct one identified |
| P3: S4 assumed not proved | Phase 1, Task 2 | S4 proof is the longest and most detailed axiom proof |
| P4: Local tomography conflated with accessibility | Phase 2 | Jordan algebra type explicitly identified; local tomography proven for that type |
| P5: Albert algebra obstruction | Phase 1 + Phase 2 | Explicit argument excluding exceptional Jordan algebra |
| P6: Circularity in update map | Phase 1, Task 1 | Update map uses only order unit space + self-modeling constraint |
| P7: Norm completion trap | Phase 2 | C*-identity established after involution, not before |
| P8: Axiom version mismatch | Phase 1 | All axioms pinned to arXiv:1803.11139 |
| P9: Associativity implies commutativity | Phase 1 (early check) | Non-associativity of self-modeling sequential product verified |
| P10: D'Ariano faithful state | Phase 4 (if triggered) | B-M correlation state faithfulness checked explicitly |
| P11: Finite dimension scope creep | All phases | Standing assumption stated in all theorem statements |

## Sources

- van de Wetering (2018), "Sequential product spaces are Jordan algebras," arXiv:1803.11139 -- axioms S1-S7, Theorems 1 and 3
- Gudder and Greechie (2002), "Sequential products on effect algebras," Reports on Mathematical Physics 49, 87-111 -- original sequential product formalism
- Gudder (2005), "Open problems for sequential effect algebras," International Journal of Theoretical Physics 44, 755-772 -- open problems including commutativity questions
- Westerbaan, Westerbaan, and van de Wetering (2020), "The three types of normal sequential effect algebras," Quantum 4, 378 -- associativity implies commutativity; three-type decomposition
- Barnum and Wilce (2014), "Local tomography and the Jordan structure of quantum theory," Foundations of Physics 44, 192-212, arXiv:1202.4513 -- local tomography selects complex QM from Jordan algebras
- Barnum, Ududec, and van de Wetering (2020), "Composites and categories of Euclidean Jordan algebras," Quantum 4, 359, arXiv:1606.09331 -- compositionality constraints, Albert algebra exclusion
- D'Ariano (2006), "Operational axioms for quantum mechanics," arXiv:quant-ph/0611094 -- faithful state construction of involution
- D'Ariano, Chiribella, Perinotti (2017), "Quantum theory from first principles," Cambridge University Press -- systematic reconstruction, circularity discussion
- Barnum, Mueller, Ududec (2014), "Higher-order interference and single-system postulates characterizing quantum theory," arXiv:1403.4147 -- ruling out non-quantum Jordan algebras
- Grinbaum (2007), "Reconstruction of quantum theory," British Journal for the Philosophy of Science 58, 387-408 -- general discussion of reconstruction pitfalls and circularity

---

_Known pitfalls research for: C*-structure from sequential product axioms applied to self-modeling systems_
_Researched: 2026-03-20_
