# Paper 7: Chirality from h_3(O) via Cl(6)

## Research Question

Does the observer's complexification of h_3(O) automatically produce the
correct chiral (left-handed) SM representation? Specifically: starting from
the Peirce decomposition of h_3(O), does the observer's C*-algebra nature
force complexification that (a) upgrades Spin(9) to Spin(10), and (b) induces
a Cl(6) structure whose volume form selects the chiral embedding?

If yes: chirality is not a separate problem. It falls out of the SAME complex
structure choice that gives the SM gauge group in Gap B. One choice, two
consequences.

## Context

### What we have (proved/theorem)

1. Self-modeling forces Jordan algebra (Paper 5, van de Wetering)
2. Universe's algebra contains h_3(O) (non-composability argument, Gap A closed)
3. Aut(h_3(O)) = F_4 (Chevalley-Schafer 1950)
4. F_4 has maximal subgroups Spin(9) and [SU(3)xSU(3)]/Z_3 (Borel-de Siebenthal)
5. Their intersection = (U(1)xSU(2)xSU(3))/Z_6 = SM gauge group (Todorov-Drenska)
6. Observer is a C*-algebra system (Paper 5, local tomography)

### The chirality problem (Baez-Sawin)

Sawin proved: two conjugacy classes of SU(2)xSU(3) in Spin(10):
- LEFT embedding G_l: chiral (correct). Left-handed doublets, right-handed
  singlets. Does NOT fit inside Spin(9).
- DIAGONAL embedding G_delta: parity-symmetric (wrong). Both particles and
  antiparticles are doublets. DOES fit inside Spin(9).

For odd n, all irreps of Spin(n) are self-dual, so the left embedding
(which requires non-self-dual reps) cannot sit inside Spin(9). The F_4/Spin(9)
construction gives the diagonal embedding.

### The resolution path

The observer is a COMPLEX system (C*-algebra). This forces complexification
of h_3(O) to h_3^C(O), upgrading:
- F_4 -> E_6 (structure group)
- Spin(9) -> Spin(10) (stabilizer subgroup)

At Spin(10), BOTH embeddings exist. Chirality is intrinsic to Spin(2n) -
the volume element of Cl(10) splits the Dirac spinor into 16_L + 16_R
automatically.

The SAME octonion splitting O = C + C^3 that gives [SU(3)xSU(3)]/Z_3
also induces Cl(6) inside Cl(10). Todorov (arXiv:2206.06912) showed the
Cl(6) volume form omega_6 defines a particle projector whose stabilizer
in Spin(10) is the Pati-Salam group. The SM gauge group with the LEFT
(chiral) embedding is obtained by further breaking Pati-Salam.

Furey (arXiv:1806.00612) showed SU(2)_L acts on only left-handed states
AUTOMATICALLY in the Cl(6) Witt decomposition. No ad hoc projectors needed.

## The Two-Part Computation

### Part A: Complexification is forced

**Claim:** The observer's C*-algebra nature (complex type, from Paper 5 local
tomography) forces complexification of the Peirce V_1 space from a real
Spin(9) spinor to a complex Spin(10) Weyl spinor.

**Starting point:** h_3(O) with Peirce decomposition relative to rank-1
idempotent E_1:
- V_2(E_1) = R (1-dimensional)
- V_1(E_1) = O^2 (16-dimensional, real Spin(9) spinor S_9)
- V_0(E_1) = h_2(O) = V_9 (10-dimensional, spin factor = JSpin_9)

The observer lives in V_2 (their "position" in h_3(O)). They interact with
V_1 (the off-diagonal octonionic entries). V_0 is the "rest of the universe."

**What to show:**
1. The observer's algebra is M_n(C)^sa (Paper 5). They process information
   using complex-linear operations.
2. When the observer probes V_1 = O^2 using complex-linear operations, they
   must extend scalars from R to C. This turns V_1 into V_1^C = (C tensor O)^2,
   a 16-dimensional complex space.
3. The symmetry group of V_0 = h_2(O) upgrades from Spin(9) (automorphisms
   of h_2(O) as a real Jordan algebra) to Spin(10) (automorphisms of the
   complexified structure). Specifically: Spin(9) acts on V_1 = O^2 as the
   real spinor representation. After complexification, the 16-dim complex
   space carries a Weyl representation of Spin(10).
4. At the h_3(O) level, F_4 upgrades to E_6 (the structure group of h_3^C(O)).
   Spin(9) subset F_4 upgrades to Spin(10) subset E_6.

**Key references:**
- Boyle arXiv:2006.16265, Section 2: h_3^C(O) and E_6
- Baez, "The Octonions," Section 4.3: Spin(9) acting on O^2
- Todorov arXiv:2206.06912: Cl(10) from left multiplication on O

### Part B: Cl(6) gives chirality

**Claim:** The octonion splitting O = C + C^3 (the same splitting used in
Gap B step 2 to break F_4 to [SU(3)xSU(3)]/Z_3) induces a Cl(6) subalgebra
inside Cl(10) whose volume form selects the chiral (left) embedding of the
SM gauge group.

**Starting point:** The observer has chosen:
1. A rank-1 idempotent E_1 in h_3(O) (Gap B step 1, breaks F_4 to Spin(9))
2. A unit imaginary octonion u in Im(O) (Gap B step 2, gives O = C + C^3,
   breaks F_4 to [SU(3)xSU(3)]/Z_3)
3. Complexification (Part A, forced by C*-nature, upgrades to Spin(10))

**What to show:**
1. The splitting O = C + C^3 (from choice of u) gives 6 "internal" real
   directions (the imaginary part of C^3, orthogonal to u). These 6
   directions generate a Cl(6) subalgebra inside Cl(10).
   (Todorov arXiv:2206.06912 constructs this explicitly.)

2. The Cl(6) volume form omega_6 = gamma_1...gamma_6 (product of the 6
   internal gamma matrices) acts on the 32-dim Dirac spinor of Spin(10).
   omega_6 commutes with Spin(6) and Spin(4) (which together give
   Spin(6) x Spin(4) / Z_2 = Pati-Salam).

3. The projector P = (1/2)(1 - i*omega_6) selects a 16-dimensional subspace
   (the "particle" space). This is one Weyl representation of Spin(10).
   (Todorov arXiv:2206.06912, Section 3.)

4. The Pati-Salam group Spin(6) x Spin(4) / Z_2 = SU(4) x SU(2)_L x SU(2)_R
   preserves this projector. Under the further breaking SU(4) -> SU(3) x U(1)
   (from the same complex structure), the SM gauge group is obtained with
   the LEFT embedding: SU(2)_L acts on left-handed fermions only.

5. Furey's result (arXiv:1806.00612): the Witt decomposition of Cl(6) into
   creation/annihilation operators a_i = (1/2)(-e_{i+4} + i*e_i) naturally
   channels SU(2) to act on a single chirality. This is AUTOMATIC - no
   projector is imposed by hand.

6. Connect back to the Todorov-Drenska intersection: the SM gauge group
   obtained via the Cl(6)/Pati-Salam route (with chirality) is the SAME
   group as the F_4 subgroup intersection (without chirality), but now
   carrying the correct (chiral) representation.

**Key references:**
- Todorov arXiv:2206.06912, Sections 2-3: Cl(6) inside Cl(10), omega_6 projector
- Furey arXiv:1806.00612: automatic parity violation from Cl(6) Witt decomposition
- Furey arXiv:1611.09182, Chapter 5: ladder operators and chirality
- Krasnov arXiv:2504.16465: pure spinor characterization, complex structures on O^2
- Baez n-Category Cafe Part 13 (Dec 2025): Sawin's theorem, left vs diagonal
- Boyle arXiv:2006.16265: 27 -> 1 + 10 + 16 decomposition under Spin(10)

## Success Criteria

**Part A succeeds if:** We can state and prove: "A C*-algebra observer
performing measurements on the Peirce V_1 = O^2 component of h_3(O) necessarily
complexifies V_1 to a Spin(10) Weyl spinor."

**Part B succeeds if:** We can state and prove: "The octonion splitting
O = C + C^3 (from the observer's complex structure choice) induces Cl(6)
inside Cl(10) on the complexified V_1, and the Cl(6) volume form together
with the Pati-Salam breaking gives the SM gauge group with the left (chiral)
embedding."

**Full success:** The observer's SINGLE ACT - choosing a complex structure
on O (embedding C in O) - simultaneously:
1. Breaks F_4 to [SU(3)xSU(3)]/Z_3 (Gap B step 2)
2. Forces complexification to E_6/Spin(10) (Part A)
3. Induces Cl(6) whose volume form selects the chiral embedding (Part B)

One choice -> gauge group + chirality. The SM is fully determined by the
observer being a complex system in an octonionic universe.

## What failure looks like

- Part A fails if complexification requires more structure than just "being
  a C*-algebra observer" (e.g., if it needs a specific embedding or additional
  data beyond the complex structure choice)
- Part B fails if the Cl(6) volume form does not cleanly select the LEFT
  embedding (e.g., if additional discrete choices are needed to break the
  L/R symmetry)
- Partial success: if the Cl(6) construction works but requires an additional
  orientation choice beyond the complex structure, this is still valuable
  (it reduces chirality to a single discrete choice rather than leaving it
  completely open)

## Connection to existing GPD work

This prompt extends the Paper 7 program. Previous prompts:
- paper7-spectral-triple-prompt.md: DEAD (single-algebra route impossible)
- paper7-chirality-prompt.md: SUPERSEDED (was based on temporal asymmetry
  -> gamma grading on M_n(C); now replaced by h_3(O) route)

This prompt is the FIRST to start from h_3(O) (now DERIVED, not assumed)
and work toward chirality through the Peirce decomposition + Cl(6) route.
