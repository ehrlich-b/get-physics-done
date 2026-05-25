# Methods Research: Paper 5 Revision (v14.0 — Internal-Exposition Gap Closure)

**Project:** Paper 5 ("Quantum Mechanics from Self-Modeling") post-submission revision
**Physics Domain:** Operational quantum theory / Order unit spaces / Sequential effect algebras / Euclidean Jordan algebras / Axiomatic reconstructions / Lean 4 formalization
**Researched:** 2026-04-16
**Confidence:** HIGH (OUS toolkit, sequential-product axiomatizations, Lean 4 print_axioms workflow), MEDIUM (Phi-wrapper defense patterns, minimal-composite adversarial responses — these are judgment calls, not theorems)

---

## Scope Boundary

METHODS.md here covers the **proof techniques, formalization strategies, and referee-response patterns** needed to close the six internal-exposition gaps identified at jigsaw-piece review for Paper 5 (submitted JMP26-AR-00922, 2026-03-28). It does NOT cover:

- The Paper 5 derivation chain itself (already in the paper and in Lean)
- Alfsen-Shultz background (assumed — primary reference already cited)
- vdW S1-S7 axiom statements (already cited in §3.2-3.5)
- New physics or new theorems beyond what is needed to patch the 6 gaps

Each method entry below is tagged by which revision phase (Phase 54-59) consumes it, so the planner can dispatch methods to phases without re-deriving the map.

---

## Problem Statement: The Six Gaps

| Phase | Gap | One-line Description |
|-------|-----|---------------------|
| 54 | §3.3 Peirce preservation | Prove `a o_s b in P_e^{0,1}` when `a, b in P_e^{0,1}` from OUS/compression primitives |
| 55 | S4 facial structure | Either cite a standalone facial-orthogonality lemma or supply a self-contained proof |
| 56 | Thm 5.8 upper bound | Show sequential product on W is forced to product-form `a o_s b = (a o b) + delta` |
| 57 | Phi inert-wrapper | Resolve whether `Phi(a) = a` (identity) or Phi is a non-trivial labeling across sections |
| 58 | Lean axiom audit | Audit 16 axioms in RadicalRelativity Paper5 module against cited literature |
| 59 | Minimal composite defense | Adversarial defense of the "at least one qubit subsystem" assumption |

---

## Recommended Methods

### Primary Proof-Technique Methods

| Method | Phase | Purpose | Applicability | Limitations |
|--------|-------|---------|---------------|-------------|
| **Spectral-OUS preservation argument** (Alfsen-Shultz 2003, Ch. 7-8) | 54 | Prove Peirce-range invariance of `o_s` from compression axiom C1-C5 | OUS with smooth compressions and functional calculus | Requires compressions already established; does not apply if only S1+S3 available |
| **S1+linearity collapse argument** (Gudder-Greechie 2002, Thm 3.2) | 54 | Show `a o_s b` lies in P_e^{0,1} when a does, using only sequential-product distributivity (S1) + homogeneity (S3) | Works when base theory has positive cone and idempotent e | Requires `b perp e' - e` available as witness; does not handle non-sharp effects without extra axiom |
| **vdW three-characterizations trick** (van de Wetering 2018, arXiv:1803.08453) | 54, 56 | Reduce abstract `o_s` to Lueders form `sqrt(a) b sqrt(a)` via continuity + homogeneity + self-duality | When ambient OUS is homogeneous self-dual (Koecher-Vinberg) | Only gives Lueders on JB-algebras, not on the Peirce subspace unless subspace is itself a Jordan subalgebra |
| **Hanche-Olsen facial symmetry** (Hanche-Olsen-Stormer 1984, Ch. 2) | 55 | Derive S4 (`a \perp b iff b \perp a`) from support-projection symmetry in JB-algebras | Applies once JB-structure is available or OUS has orthogonal decomposition | Not available for arbitrary effect algebras without JB-structure |
| **Foulis-Holland theorem** (orthomodular lattice theory, standard) | 55 | Obtain symmetric orthogonality from commutativity of any two of {a,b,a'} | Orthomodular lattices / orthomodular posets | Requires lattice (not just effect algebra) structure |
| **Westerbaan-Westerbaan-vdW spectral theorem** (arXiv:2004.12749) | 54, 55, 56 | For normal SEAs, decompose into Boolean + convex + purely-almost-convex, then use Jordan spectral calculus on the convex part | Normal SEA (sigma-complete, countable suprema) | Requires normality (Paper 5 has this via L4 and vdW S5); does not apply to non-normal toy models |
| **Product-form closure via KV homogeneity** (Koecher-Vinberg theorem, vdW 2019 JMP Thm 1) | 56 | Show W closed under `o_s` + homogeneity + self-duality => W is Jordan subalgebra => o_s is product-form | W is a face of a homogeneous self-dual cone | If W is not a face (arbitrary subspace), this fails — must first show face structure |
| **Hardy-style ancilla elimination** (Hardy 2001 §5; Masanes-Muller 2011 §IV) | 57, 59 | Show wrapper Phi drops out of physical predictions via ancilla discard | Axiomatic frameworks where tensor product is defined and Phi respects it | Must check Phi commutes with partial trace; fails if Phi introduces state-dependent labeling |
| **Chiribella-D'Ariano-Perinotti purification** (CDP 2011 arXiv:1011.6451) | 57, 59 | Replace Phi wrapper with a canonical purification + discard; well-defined up to isomorphism | Purification postulate satisfied (CDP Axiom 6) | Paper 5 does not assume purification — may need to show derivable, or drop the pattern |
| **Barnum-Wilce qubit-anchor argument** (Barnum-Wilce 2014 FoP) | 59 | Local tomography + one qubit subsystem => full quantum theory (Hanche-Olsen classification) | Finite-dim Jordan + local tomography + one 2-level subsystem | Only works after Jordan structure; cannot be invoked earlier in the chain |

### Primary Formalization Methods (Lean 4)

| Method | Phase | Purpose | Cost | Limitations |
|--------|-------|---------|------|-------------|
| **`#print axioms` single-theorem trace** | 58 | Surface all axioms transitively used by a single theorem (e.g., `Paper5.main`) | Instant per invocation; parsing 30-60 min per axiom to match to citation | Only shows *used* axioms, not *declared*; unused declared axioms hide from this tool |
| **Axiom dependency grep** (`grep -c '^axiom '` over tree) | 58 | Enumerate declared axioms per file | Instant | Misses axioms declared via `opaque` or `constant` (Lean 4); also misses axioms inherited from transitive imports |
| **`Lean.Elab.Print.printAxioms` API walk** | 58 | Programmatic axiom extraction for all theorems, build citation table | 1-2 days to write audit script | Requires `import Lean` and meta-code; not trivially composable with mathlib tooling |
| **Axiom-to-citation bridge docstrings** (`/-- @axiom_source Alfsen-Shultz 2003 Prop 2.11 -/`) | 58 | Attach literature citation to each `axiom` declaration, then lint | 5-10 min per axiom once discipline is adopted; retroactive pass 30-60 min/axiom | Not enforced by Lean compiler; drift possible if reviewer edits without updating |
| **`sorry`-scan + axiom-scan combined** | 58 | Verify both: no sorries AND every axiom has provenance | Fast; 15 min for full Paper5 tree | Does not catch *semantic* mismatches (axiom stated correctly but referring to wrong theorem in source) |

### Referee-Response / Exposition Methods

| Method | Phase | Purpose | Known Limitations |
|--------|-------|---------|------------------|
| **Adversarial "minimal-composite" stress test** (Hardy 2001, Masanes-Muller 2011 §II critiques, Kent 2024 arXiv:2405.17733 critique pattern) | 59 | Draft the reviewer's likely objection to "minimal composite" assumption; defend pre-emptively | Cannot pre-empt arbitrary referees; goal is to block *standard* objections |
| **Dakic-Brukner subspace-axiom echo** (Dakic-Brukner 2009 arXiv:0911.0695 Axiom 2) | 59 | Frame "minimal composite" as analogous to their "elementary system equivalence"; leverages existing community acceptance | Only persuasive if audience accepts Dakic-Brukner framing; some JMP referees reject axiomatic reconstruction entirely |
| **Operational redundancy argument** (Masanes-Galley-Muller 2019 Nat Comm) | 59 | Argue composite assumption is redundant given prior axioms; if not, state precisely what it adds | Requires showing genuine non-redundancy OR full redundancy — no middle ground survives peer review |
| **Phi-inert notation pass** (Paper 5 exposition) | 57 | Uniform notation across §3-§6: declare Phi = id once, then drop OR commit to non-trivial Phi and audit all uses | Purely editorial but mistakes introduce logical gaps; takes 4-6 hours for a paper of Paper 5's size |

### Supporting Tools

| Tool | Phase | Purpose | When to Use |
|------|-------|---------|-------------|
| Lean 4 (v4.x compatible with RadicalRelativity toolchain) | 58 | Run `#print axioms`, rebuild Paper5 module to verify audit | Phase 58 start |
| `leanblueprint` (if installed) | 58 | Cross-link informal LaTeX claims to Lean statements | Optional; only if time allows integration |
| grep/ripgrep | 57, 58 | Phi-uses enumeration, axiom enumeration | Phase 57 and 58 both |
| Zotero/BibTeX | 58 | Map each axiom to a paper + page/theorem number | Throughout audit |
| Git blame on RadicalRelativity/*.lean | 58 | Identify *when* each axiom was added — hints at which paper-era derivation relies on it | Phase 58 if axiom origin is unclear |

---

## Method Details

### Method 1: Spectral-OUS Preservation Argument (Phase 54 primary)

**What:** Prove that `a, b in P_e^{0,1}` implies `a o_s b in P_e^{0,1}` using the compression machinery developed in Alfsen-Shultz 2003 Chapter 7 (Compressions) and Chapter 8 (Spectral theory).

**Mathematical basis:** Let `P_e^{0,1}` denote the Peirce range of idempotent `e` (equivalently, the compressed subspace `P_e(A) = {a : a o e = a}`). Alfsen-Shultz Prop 8.4 shows that compression `P_e` commutes with bounded functional calculus. The sequential product `o_s` on a spectral OUS is definable in terms of functional calculus (vdW 2018 Thm 1), so `P_e(a o_s b) = P_e(a) o_s P_e(b)`. When `a, b` are already in `P_e^{0,1}`, their compression is the identity, giving closure.

**Proof skeleton (~4-6 pages):**
1. Recall that `o_s` on a spectral OUS satisfies `a o_s b = f(a) b f(a)` where `f = sqrt` (vdW 2018).
2. Note that `P_e` is a positive projection (Alfsen-Shultz 7.2.3).
3. Apply Alfsen-Shultz 8.4.5 (compression commutes with functional calculus on the compressed subspace).
4. Conclude: if `a, b` are in range of `P_e`, so is `sqrt(a) b sqrt(a) = a o_s b`.
5. Verify zero and top elements preserved via linearity.

**Known failure modes:**
- Fails if OUS is not spectral (vdW S7 not holding). Paper 5 has S7 via spectral convex effect algebra machinery — VERIFY before invoking.
- Fails if `e` is not a *sharp* idempotent in the compression sense (Alfsen-Shultz 7.1). Paper 5's `e` arises from L4 and is sharp.

**Benchmark:** Standard in JB-algebra literature. Analogous preservation for the Jordan product is Alfsen-Shultz Lemma 2.5.2; for `o_s`, vdW 2018 Thm 2 gives the same structure.

**References:**
- Alfsen-Shultz, *Geometry of State Spaces of Operator Algebras*, Birkhauser 2003, Ch 7-8
- van de Wetering, "Three characterisations of the sequential product", JMP 59, 082202 (2018), arXiv:1803.08453

---

### Method 2: S1+Linearity Collapse (Phase 54 fallback)

**What:** If the full spectral OUS toolkit is unavailable, use a weaker argument from only S1 (sequential-product distributivity) + S3 (one-sided homogeneity) + linearity.

**Mathematical basis:** Gudder-Greechie "Sequential products on effect algebras" (RMP 49, 2002) Theorem 3.2: if the sequential-product effect algebra admits a linear extension to a real vector space and S1 holds, then `o_s` preserves any subspace closed under (+, 0, e).

**Proof skeleton (~2-3 pages):**
1. Start with `a in P_e^{0,1}`. Expand `a = a o_s e` using idempotency.
2. Apply S1: `(a + a') o_s b = a o_s b + a' o_s b` whenever `a perp a'`.
3. Use the Peirce relation `a + (e - a) = e` to decompose b relative to e.
4. Sum terms; the only surviving piece lies in P_e^{0,1}.

**Known failure modes:**
- Requires `o_s` to respect effect-algebra sum on the left argument *and* right argument. vdW S1 only guarantees right-linearity; you may need to assume or derive left-linearity separately.
- Does NOT give the full product-form `a o_s b = a o b`; only gives preservation. If Phase 54 also needs the product-form identity, must invoke Method 1 or 3.

**When to use:** Only if the paper cannot or does not want to invoke the full Alfsen-Shultz spectral machinery in §3.3 for exposition reasons.

**References:**
- Gudder, Greechie, "Sequential products on effect algebras", Reports on Mathematical Physics 49, 87-111 (2002)
- Gudder, Greechie, "Uniqueness and order in sequential effect algebras", IJTP 44, 755-770 (2005), DOI: 10.1007/s10773-005-7054-y

---

### Method 3: Hanche-Olsen Facial Symmetry (Phase 55 primary)

**What:** Derive S4 (orthogonality-is-symmetric) from the Hanche-Olsen-Stormer facial structure theorem: orthogonal faces have orthogonal support projections, which are symmetric operators.

**Mathematical basis:** In a JB-algebra, every norm-closed face F corresponds to a unique projection p with `F = p^perp` (Hanche-Olsen-Stormer, *Jordan Operator Algebras*, Pitman 1984, Prop 2.1.3). The orthogonal complement operation on projections is an involution (p -> e - p), so `a perp b iff b perp a`.

**Proof skeleton (~1-2 pages):**
1. Given `a, b in P_e^{0,1}` with `a perp b` (meaning `a o_s b = 0`).
2. Show a and b have disjoint support projections (Hanche-Olsen 2.1.3).
3. Disjoint support is manifestly symmetric in a JB-algebra.
4. Therefore `b o_s a = 0`.

**Known failure modes:**
- Requires JB-algebra structure. At the §3.3-§3.4 stage of Paper 5, the JB structure is DERIVED (not assumed) — may be circular if invoked too early. CHECK phase ordering.
- Alfsen-Shultz 2003 Prop 2.5.6 gives a cleaner version using order-theoretic faces without invoking Jordan product; prefer this formulation if §3.3 is pre-Jordan.

**When to use:** If the paper is willing to cite a standalone lemma. If not, use Method 4.

**References:**
- Hanche-Olsen, Stormer, *Jordan Operator Algebras*, Pitman 1984, §2.1
- Alfsen-Shultz 2003, Ch. 2, §2.5 (order-theoretic faces)

---

### Method 4: Foulis-Holland Symmetric Orthogonality (Phase 55 fallback)

**What:** Pure order-theoretic / orthomodular-lattice proof of S4 that does not invoke Jordan structure.

**Mathematical basis:** Foulis-Holland theorem for orthomodular posets: if any two of `{a, b, a'}` commute, then the sublattice they generate is distributive, and orthogonality relations are symmetric.

**Proof skeleton (~1 page):**
1. In the projection lattice of a spectral OUS, `a perp b` means `a <= b'` (order-theoretic).
2. Apply orthomodular law: `a <= b' iff b <= a'`.
3. By definition `b <= a' iff b perp a`.

**Known failure modes:**
- Requires effect algebra to embed into an orthomodular lattice via sharp elements. Paper 5's `P_e^{0,1}` consists of sharp effects by construction (they are in the idempotent-compressed subspace), so this is automatic.
- If `a, b` are not sharp, the Foulis-Holland argument does not directly apply. Paper 5 gap is stated for sharp-effect subspace, so no issue here.

**When to use:** Preferred for §3.3-3.4 exposition if the paper wants to minimize forward references to Jordan structure.

**References:**
- Kalmbach, *Orthomodular Lattices*, Academic Press 1983, Ch. 2
- Beran, *Orthomodular Lattices*, Reidel 1985 (alternative treatment)

---

### Method 5: Product-Form Closure via Koecher-Vinberg (Phase 56 primary)

**What:** Show that the sequential product on a subspace W is forced to product-form (i.e., `a o_s b = sqrt(a) b sqrt(a)`), not just preserved in W.

**Mathematical basis:** van de Wetering 2019 JMP "Sequential product spaces are Jordan algebras" (arXiv:1803.11139) Theorem 1: A finite-dimensional order unit space with a continuous sequential product is homogeneous and self-dual, hence by Koecher-Vinberg is a Euclidean Jordan algebra. The sequential product is then uniquely `sqrt(a) b sqrt(a)`.

**Proof skeleton for Thm 5.8 upper bound (~3-5 pages):**
1. W is a subspace of the OUS A, equipped with restricted `o_s`.
2. Verify W inherits S1-S7 from A (direct check).
3. Apply vdW 2019 Thm 1: W is a Euclidean Jordan algebra.
4. Apply vdW 2018 Thm 2: `o_s|_W = sqrt(a) b sqrt(a)`.
5. Therefore `a o_s b = a o b + delta` where `a o b` is the Jordan product and delta is the symmetric-square correction (explicit formula in vdW 2019).

**Known failure modes:**
- Requires W to be a *face* of A, not an arbitrary subspace. Paper 5's W is constructed as the Peirce range of a specific idempotent, which IS a face — verify this claim explicitly.
- Finite-dimensional hypothesis is essential. vdW 2019 Thm 1 is infinite-dim only in restricted settings.

**Benchmark:** This is the standard argument used in the operational-QM reconstruction literature (Barnum-Wilce 2014, CDP 2011 all invoke analogous KV-style closures).

**References:**
- van de Wetering, "Sequential product spaces are Jordan algebras", JMP 60, 062201 (2019), arXiv:1803.11139
- Faraut, Koranyi, *Analysis on Symmetric Cones*, OUP 1994, Ch. III (KV theorem)

---

### Method 6: Hardy-Style Ancilla Elimination (Phase 57 primary)

**What:** Resolve the Phi inert-wrapper ambiguity by showing Phi either (a) drops out of all observational predictions (inert) or (b) is genuinely needed and affects predictions in a specified way.

**Mathematical basis:** Hardy 2001 §5.4 (and Masanes-Muller 2011 §IV) shows that any transformation Phi acting on a system S "labeled" by auxiliary data can be eliminated from predictions iff:
- Phi commutes with all allowed measurements on S (i.e., `M(Phi(rho)) = M(rho)` for all measurements M), OR
- Phi is a relabeling of fiducial outcomes that does not affect probability structure.

**Proof skeleton (4-6 hour editorial pass):**
1. Enumerate all uses of Phi in Paper 5 (Phase 57 preliminary task: `grep -n 'Phi' paper5.tex`).
2. For each use, classify: (a) Phi in a measurement prediction (`P(outcome | Phi(rho))`), (b) Phi in a state-preparation step, (c) Phi in a notational wrapper for exposition.
3. If (a): verify Phi commutes with the measurement — if so, Phi drops out.
4. If (b): verify Phi does not change the equivalence class of the state — if so, Phi is inert.
5. If (c): either replace with explicit identity or commit to non-trivial Phi with explicit justification for each occurrence.

**Known failure modes:**
- Danger of "Phi = id sometimes, not others" in prose — this is exactly the gap. Must be globally consistent.
- If Phi is a self-modeling projection (plausible given Paper 5's setup), it is NOT trivially the identity on the full state space, only on a sub-state-space. Must state which one.

**When to use:** Phase 57 central method.

**References:**
- Hardy, "Quantum Theory From Five Reasonable Axioms", quant-ph/0101012 (2001), §5
- Masanes, Muller, "A derivation of quantum theory from physical requirements", NJP 13, 063001 (2011), arXiv:1004.1483

---

### Method 7: Lean 4 Axiom Audit Workflow (Phase 58 primary)

**What:** Systematic audit of the 16 axioms in RadicalRelativity/Paper5 module against cited Alfsen-Shultz and van de Wetering sources.

**Mathematical basis:** Lean 4 tracks axiom dependencies transitively. `#print axioms <theorem>` lists all axioms actually used in the proof term. Standard mathlib axioms (`Classical.choice`, `propext`, `Quot.sound`) are expected and accepted; any other axiom must have a literature citation.

**Audit procedure (estimated 30-60 min per axiom, so 8-16 hours total):**

```
Step 1 (15 min): Identify Paper5 entry theorem(s).
  cd ~/repos/research/lean/
  # Find theorems tagged as Paper 5 top-level results.
  grep -n '^theorem\|^lemma' RadicalRelativity/*.lean | grep -i 'paper5\|main\|quantum'

Step 2 (5 min per theorem): Extract axiom list.
  In Lean: `#print axioms Paper5.main`
  Record output.

Step 3 (30-60 min per axiom): Match to literature.
  For each axiom listed:
  - Read its docstring (if any) in the .lean file.
  - Find its declaration site: `grep -rn '^axiom <name>' RadicalRelativity/`
  - Look up the cited source; verify the axiom matches the statement in the paper/book.
  - If no docstring exists, trace back through git blame to find the derivation context.

Step 4 (15 min): Categorize.
  - STANDARD: Classical.choice, propext, Quot.sound — OK, no citation needed.
  - CITED: axiom has literature citation that matches its content — OK.
  - UNCITED-DERIVABLE: axiom could be proved in Lean but was axiomatized for speed — flag for Phase 58 follow-up.
  - UNCITED-UNJUSTIFIED: axiom has no citation and no clear derivation — BLOCKER for referee response.

Step 5 (30 min): Write audit report.
  Table: axiom name | statement | citation | category | action.
```

**Known failure modes:**
- `#print axioms` only shows axioms *reached* by the proof term; axioms declared in a file but not used by the top-level theorem are invisible. Cross-check with `grep '^axiom '` on the tree.
- Lean 4's `opaque` and `constant` declarations behave like axioms but print differently. Verify: `grep -rn '^opaque\|^constant' RadicalRelativity/Paper5*`.
- Axioms in transitively imported files (e.g., deep in mathlib or in Octonions.lean) count. The 16 number may be Paper5-direct; full transitive count is larger.

**Tooling:**
```bash
# Paper5 axiom enumeration (run at Lean project root):
lake build
# Then in a Lean file add:
# #print axioms Paper5.main_theorem
# #print axioms Paper5.quantum_emergence

# Fast declared-axiom count:
grep -c '^axiom ' RadicalRelativity/*.lean | grep -v ':0'
```

**References:**
- Lean 4 manual, "Axioms and Computation" chapter, https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/
- Mathlib4 axiom-hygiene docs (community conventions)
- Reference axiom-audit from a recent Lean physics formalization: "A Formalization of the Generalized Quantum Stein's Lemma in Lean", arXiv:2510.08672 (October 2025) — good template for Paper 5 audit style

---

### Method 8: Adversarial Minimal-Composite Defense (Phase 59 primary)

**What:** Pre-empt the standard referee objection that "you need a subsystem of dimension >= 2 somewhere; why is this not sneaking in quantum structure?".

**Mathematical basis:** Three axiomatic frameworks handle this:

1. **Hardy 2001**: posits an "N-level system" for each N, with N=2 as the smallest non-trivial case. Defense: all physical theories need SOME non-trivial system; N=2 is minimal. No circularity because the N=2 system is characterized by operational axioms, not by quantum structure.

2. **Dakic-Brukner 2009**: uses the "subspace axiom" — all elementary systems of the same information capacity are equivalent. Defense: this is an *equivalence* assumption, not an existence assumption; existence comes from operationally asking "can we prepare any state?".

3. **Masanes-Muller 2011 + Masanes-Galley-Muller 2019**: uses "continuous reversibility" applied to all systems uniformly. Defense: minimal composite is derivable from non-signaling + information capacity.

4. **Barnum-Wilce 2014**: requires "at least one qubit subsystem" as a hypothesis in their classification theorem. They defend it as: "this is not an additional physical assumption beyond local tomography + Jordan structure — it is the smallest system for which the classification is non-trivial".

**Defense pattern for Paper 5 (~2-3 pages of prose):**
1. State the minimal-composite assumption precisely.
2. Compare to Hardy 2001 N=2 / Dakic-Brukner subspace / Masanes-Muller continuous-reversibility / Barnum-Wilce qubit-subsystem — note that all extant operational reconstructions require something analogous.
3. Show that the Paper 5 assumption is the WEAKEST of these (or equivalent to the weakest), with citation.
4. Address the Kent-style objection (Kent 2024 arXiv:2405.17733): does the assumption sneak in "quantumness"? Answer must be "no, because it is characterized by [operational property X] which is satisfied by classical theories too".
5. Optional: show that assumption is *necessary* by exhibiting a theory where it fails.

**Known failure modes:**
- Weakness: if reviewer rejects axiomatic reconstruction as a genre, this defense cannot persuade.
- Must avoid claiming the assumption is "obvious" — every published reconstruction has had to defend it, and "obvious" is a red flag.

**References:**
- Hardy, quant-ph/0101012 (2001), §3-4
- Dakic, Brukner, "Quantum Theory and Beyond: Is Entanglement Special?", arXiv:0911.0695 (2009)
- Masanes, Muller, NJP 13, 063001 (2011), arXiv:1004.1483
- Masanes, Galley, Muller, "The measurement postulates of quantum mechanics are operationally redundant", Nat Comm 10, 1361 (2019)
- Barnum, Wilce, "Local Tomography and the Jordan Structure of Quantum Theory", FoP 44, 192-212 (2014), arXiv:1202.4513
- Kent, "Contradictions or Curiosities? On Kent's Critique of the Masanes-Galley-Muller Derivation", arXiv:2405.17733 (2024) — critique template; Paper 5 must anticipate similar objections
- *Defending the quantum reconstruction program*, European J. Philosophy of Science (2024), https://link.springer.com/article/10.1007/s13194-024-00608-2

---

## Alternatives Considered

| Category | Recommended | Alternative | Why Not |
|----------|-------------|-------------|---------|
| Peirce preservation proof (Phase 54) | Alfsen-Shultz spectral compression (Method 1) | Direct Jordan-algebra computation | Would require pulling Jordan structure forward in the derivation chain; AS method stays in OUS/compression primitives, preserving the ordering of the derivation |
| S4 proof (Phase 55) | Foulis-Holland (Method 4) | Hanche-Olsen facial (Method 3) | HO requires JB-structure which is downstream in Paper 5's derivation chain; FH is pre-Jordan |
| Thm 5.8 upper bound (Phase 56) | vdW 2019 KV closure (Method 5) | Direct verification on W | Direct verification would require knowing the explicit form of `o_s` on W, which is what 5.8 is trying to establish — circular |
| Phi wrapper (Phase 57) | Hardy-style elimination (Method 6) | Commit to non-trivial Phi throughout | Commits to more structure than needed; elimination is cleaner if it succeeds |
| Lean audit (Phase 58) | `#print axioms` + grep + citation docstrings (Method 7) | Rewrite proofs to eliminate axioms | Out of scope for a revision window before referee report; keep axioms, document them |
| Composite defense (Phase 59) | Comparative defense (Method 8) | Silence / hope reviewer doesn't notice | Standard review practice; reviewers WILL notice this assumption |

---

## Installation / Setup

```bash
# Lean 4 audit tooling (Phase 58). Paper 5 Lean project already exists.
cd ~/repos/research/lean
lake build  # rebuilds RadicalRelativity module; confirms no sorries

# Quick axiom enumeration
grep -c '^axiom ' RadicalRelativity/*.lean | grep -v ':0' | sort -t: -k2 -nr

# Full Paper 5 axiom trace (run in a Lean file, e.g., Paper5Audit.lean):
# import RadicalRelativity.Paper5
# #print axioms Paper5.main

# Literature management (optional but recommended for Phase 58 citation work)
# Zotero + Better BibTeX export to the paper's bibliography file
```

No new Python/scientific-computing dependencies required — revision work is proof, exposition, and Lean-level auditing.

---

## Validation Strategy

| Check | Phase | Expected Result | How to Verify |
|-------|-------|----------------|---------------|
| Peirce preservation holds in Paper 5's L4 model | 54 | `P_e^{0,1}` closed under `o_s` | Write the proof out; cross-check against vdW 2018 Thm 2 / AS Prop 8.4.5 |
| S4 holds for P_e^{0,1} from Paper 5 axioms | 55 | `a perp b iff b perp a` | Foulis-Holland argument completes without invoking Jordan structure |
| W is a face of A | 56 | Yes (needed for Method 5) | Explicit check that `a in W, 0 <= b <= a => b in W` |
| vdW KV closure applies to W | 56 | W is Euclidean Jordan algebra | Verify S1-S7 inherited from A |
| Phi = id on all measurement-relevant states | 57 | Every use of Phi classified as inert OR justified | Exhaustive enumeration via grep + manual classification |
| All 16 axioms cited | 58 | Every axiom maps to Alfsen-Shultz / vdW / etc. location | Audit table complete, no UNCITED-UNJUSTIFIED rows |
| No sorries in Paper5 Lean tree | 58 | 0 sorries | `grep -c 'sorry' RadicalRelativity/*.lean` returns all zeros |
| Composite-assumption defense addresses Hardy/DB/MM/BW/Kent objections | 59 | All five objection patterns addressed | Self-review against the five patterns; external read-through |

---

## Cost Estimates

| Phase | Primary method | Estimated effort | Notes |
|-------|---------------|------------------|-------|
| 54 | Method 1 (AS spectral compression) | 1-2 days (4-6 page proof + editorial) | Straightforward once the AS citation is located |
| 55 | Method 4 (Foulis-Holland) OR citation of AS 2.5 | 0.5-1 day | If citation suffices, a single paragraph; if full proof, 1-2 pages |
| 56 | Method 5 (vdW 2019 KV) | 1-2 days (3-5 page proof + face-check) | Main cost is verifying W is a face; proof itself is short once that's established |
| 57 | Method 6 (Hardy-style Phi audit) | 0.5-1 day (4-6 hour editorial pass + careful rewrite) | Pure exposition; no new proofs |
| 58 | Method 7 (Lean axiom audit) | 2-3 days (8-16 hours of axiom-to-citation matching) | Bottleneck is matching axioms to specific theorem numbers in sources |
| 59 | Method 8 (adversarial defense) | 1-2 days (2-3 page defense + integration into §9 or new appendix) | Editorial; re-reads several referenced papers |

**Total:** ~6-11 working days across 6 phases. If run sequentially in a revision window before referee report (typically 6-8 weeks at JMP), this is comfortable.

---

## Sources

| Reference | arXiv/DOI | Type | Relevance |
|-----------|-----------|------|-----------|
| Alfsen, Shultz, *Geometry of State Spaces of Operator Algebras* (2003) | ISBN 978-0-8176-4319-8 | Textbook | Primary source for OUS / compression / facial / spectral — Phase 54, 55 |
| Alfsen, Shultz, *State Spaces of Operator Algebras* (2001) | DOI 10.1007/978-1-4612-0147-2 | Textbook | Companion volume; useful for basic-theory citations |
| Hanche-Olsen, Stormer, *Jordan Operator Algebras*, Pitman (1984) | — | Textbook | JB-algebra facial structure — Phase 55 (alternative) |
| van de Wetering, "Three characterisations of the sequential product" | arXiv:1803.08453, JMP 59, 082202 (2018) | Paper | Spectral `o_s` on JB-algebras — Phase 54, 56 |
| van de Wetering, "Sequential product spaces are Jordan algebras" | arXiv:1803.11139, JMP 60, 062201 (2019) | Paper | KV closure theorem — Phase 56 |
| Westerbaan, Westerbaan, van de Wetering, "Three types of normal SEAs" | arXiv:2004.12749, Quantum 4, 378 (2020) | Paper | Normal SEA spectral theorem — Phase 54, 55, 56 |
| Gudder, Greechie, "Sequential products on effect algebras" | RMP 49, 87 (2002) | Paper | S1+linearity arguments — Phase 54 (fallback) |
| Gudder, Greechie, "Uniqueness and order in sequential effect algebras" | DOI 10.1007/s10773-005-7054-y, IJTP 44, 755 (2005) | Paper | Uniqueness results — Phase 54, 56 |
| Hardy, "Quantum Theory From Five Reasonable Axioms" | quant-ph/0101012 | Preprint | Ancilla / composite defense — Phase 57, 59 |
| Dakic, Brukner, "Quantum Theory and Beyond: Is Entanglement Special?" | arXiv:0911.0695 | Preprint | Subspace axiom comparison — Phase 59 |
| Masanes, Muller, "A derivation of quantum theory from physical requirements" | arXiv:1004.1483, NJP 13, 063001 (2011) | Paper | Composite-system postulate defense — Phase 57, 59 |
| Masanes, Galley, Muller, "The measurement postulates are operationally redundant" | Nat Comm 10, 1361 (2019) | Paper | Redundancy-style arguments — Phase 59 |
| Chiribella, D'Ariano, Perinotti, "Informational derivation of quantum theory" | arXiv:1011.6451, PRA 84, 012311 (2011) | Paper | Purification-based wrapper handling — Phase 57, 59 |
| Barnum, Wilce, "Local Tomography and the Jordan Structure of Quantum Theory" | arXiv:1202.4513, FoP 44, 192 (2014) | Paper | Qubit-subsystem argument — Phase 59 |
| Kent critique template | arXiv:2405.17733 (2024) | Preprint | Adversarial-review pattern — Phase 59 (anticipate) |
| Stein's Lemma Lean formalization | arXiv:2510.08672 (2025) | Preprint | Template for Lean 4 physics audit — Phase 58 |
| Lean 4 manual, "Axioms and Computation" | https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/ | Docs | `#print axioms` workflow — Phase 58 |
| Mathlib4 repository | https://github.com/leanprover-community/mathlib4 | Code | Axiom-hygiene conventions — Phase 58 |

---

## Confidence Notes

- **HIGH confidence** on Methods 1, 2, 3, 4, 5, 7: these are textbook or well-cited published results with explicit theorem numbers.
- **MEDIUM confidence** on Method 6 (Phi-wrapper): requires manual classification pass; success depends on whether Phi can actually be eliminated everywhere.
- **MEDIUM confidence** on Method 8 (composite defense): this is judgment and exposition, not theorem; a determined referee can reject the defense. Best practice is to address multiple objection patterns preemptively.
- **Aggregate confidence: HIGH** that these methods close the 6 gaps in the revision window, assuming Paper 5's existing derivation chain is correct (which is assumed by the revision scope, not challenged).
