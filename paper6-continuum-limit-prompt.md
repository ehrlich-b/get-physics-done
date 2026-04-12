# GPD Prompt: Continuum Limit from Finite-Dimensional Observer

## The Claim

The continuum limit of the self-modeling lattice (Paper 6) is not a property
of the lattice that needs to be proved constructively. It is a CONSEQUENCE of
the observer being finite-dimensional (Paper 5). A finite-dimensional
C*-observer necessarily sees a smooth effective geometry because:

1. The observer's algebra M_n(C)^sa has finite dimension n^2.
2. Lattice correlations decay exponentially outside the Lieb-Robinson cone.
3. The observer cannot resolve sub-correlation-length structure.
4. The effective state (partial trace over unresolved DOF) varies smoothly
   with the observer's position on the lattice.
5. The space of effective states is a smooth manifold with the Fisher
   information metric.

This collapses all four Paper 6 gaps into one claim: "the SWAP Hamiltonian's
ground state has exponentially decaying correlations in d=3."

## What To Prove

### Phase A: Fisher Geometry of Reduced States

**Theorem target:** Let H = sum J*SWAP on a d-dimensional lattice with local
algebra M_n(C) at each site. Let |psi> be the ground state. Let rho_Lambda(x)
be the reduced density matrix of |psi> on a ball of radius R centered at
lattice site x. Then:

(a) rho_Lambda(x) is a smooth function of x (in the sense that matrix
    elements vary smoothly with x) whenever the ground state has exponential
    decay of correlations.

(b) The Fisher information metric g_ij(x) = Tr(rho d_i(log rho) d_j(log rho))
    on the manifold of reduced states {rho_Lambda(x) : x in lattice} is
    positive-definite and smooth.

(c) The Fisher metric recovers the lattice distance at leading order:
    d_Fisher(x, y) ~ d_lattice(x, y) for |x-y| >> correlation length.

**Key references:**
- Braunstein-Caves 1994 (Fisher information metric on quantum states)
- Zanardi et al. 2007 (information geometry of quantum phase transitions)
- Provost-Vallee 1980 (Fubini-Study metric from state manifolds)

### Phase B: Exponential Decay for SWAP Hamiltonian

**Theorem target:** The ground state of H = sum J*SWAP (J > 0) on a
d-dimensional regular lattice with local algebra M_n(C) has:

(a) A spectral gap above the ground state (for d >= 2, above Neel order).

(b) Exponential decay of connected correlations:
    |<A_x B_y> - <A_x><B_y>| <= C * exp(-|x-y|/xi)
    where xi is the correlation length.

For n=2, d=3: the Heisenberg AFM has Neel order with magnon gap. This is
well-established (spin-wave theory, Monte Carlo) but does it have a proof?

For general n: the SU(n) Heisenberg model. Large-n limit may be tractable
via saddle-point / 1/n expansion.

**Key references:**
- Hastings 2004 (spectral gap implies exponential decay, general theorem)
- Hastings 2007 (area law in 1D from spectral gap)
- Nachtergaele-Sims 2006 (Lieb-Robinson bounds)
- Affleck et al. (AKLT model: exact gap proof for specific Hamiltonians)
- Dyson-Lieb-Simon 1978 (phase transitions in quantum Heisenberg)

### Phase C: Emergent Lorentz Invariance from Fisher Geometry

**Theorem target:** If the Fisher metric on the manifold of reduced states is:
(a) positive-definite (from Phase A),
(b) isotropic at long wavelengths (from lattice symmetry of SWAP Hamiltonian),
(c) compatible with the Lieb-Robinson causal structure,

then the effective low-energy theory has emergent Lorentz invariance with
the LR velocity as the speed of light.

**Argument:** Isotropy + finite maximum speed + smoothness = Lorentz. The
lattice symmetry group (hypercubic in d dimensions) contains enough
rotational symmetry that the Fisher metric is isotropic at long wavelengths
(lattice anisotropy enters only at O(a^2/L^2)). The LR bound gives the
maximum speed. Smoothness comes from Phase A. These three ingredients
uniquely determine the Lorentz group as the symmetry of the effective metric
(this is essentially the content of von Ignatowsky's 1911 theorem: isotropy
+ maximum finite speed = Lorentz transformations, no need to postulate
light).

**Key references:**
- von Ignatowsky 1911 (Lorentz group from isotropy + finite speed)
- Nachtergaele-Sims 2006 (LR bounds for lattice systems)
- Hamma et al. 2009 (Lieb-Robinson and Lorentz invariance on lattices)

### Phase D: BW and Equilibrium (Downstream)

**Theorem target:** Given Phases A-C (smooth Lorentz-invariant effective
geometry), show:

(a) The modular Hamiltonian of the ground state restricted to a half-space
    approximates a local Lorentz boost (Bisognano-Wichmann) in the effective
    theory. This follows from BW theorem applied to the effective QFT (which
    satisfies Wightman axioms by Phase C).

(b) The ground state satisfies theta = sigma = 0 at the bifurcation surface
    (local equilibrium). This follows from KMS property of the ground state
    restricted to a half-space.

These are downstream of Phases A-C and should follow from standard results
once the effective theory is established.

### Phase E: Assembly

Write a derivation document assembling Phases A-D into a single chain:

Finite-dim observer (Paper 5) + SWAP lattice (Paper 6 L2) + exponential
decay (Phase B) -> smooth Fisher manifold (Phase A) -> emergent Lorentz
(Phase C) -> BW + equilibrium (Phase D) -> Jacobson 1995 -> Einstein
equations.

This closes all four Paper 6 gaps simultaneously via one mechanism: the
observer's finite-dimensional C*-algebra acting as a natural UV cutoff.

## Verification

1. Phase A: Check Fisher metric smoothness numerically on small lattices
   (N=8-20). Compute rho_Lambda(x) for different x, compute Fisher metric,
   verify smoothness and positive-definiteness. Compare d_Fisher with
   d_lattice.

2. Phase B: Verify exponential decay of correlations numerically for
   SWAP Hamiltonian on small lattices. Compute correlation length xi.
   For n=2,3,4 and d=1,2 (d=3 too large for ED).

3. Phase C: Verify isotropy of Fisher metric at long wavelengths numerically.
   Check that anisotropy scales as O(a^2/L^2).

4. Phase D: Verify modular Hamiltonian locality (SRF) converges to 1 as
   system size increases (Paper 6 already has SRF=0.9993 at N=16).

## What This Does NOT Claim

- Does NOT give a constructive proof of the continuum limit in the
  mathematical sense (convergence of lattice correlation functions to
  continuum QFT). That remains an open problem.
- DOES show that any finite-dimensional observer necessarily sees smooth
  effective geometry, which is the physically relevant claim.
- The shift: from "does the limit exist?" (math) to "what does the observer
  see?" (physics). The observer's finite capacity IS the UV cutoff.

## Connection to Papers 5 and 7

The C*-bottleneck (Paper 5) that gives QM and that gives SM (Paper 7 via
F_4 -> SM through the bottleneck) ALSO gives smooth geometry (Paper 6 via
Fisher metric on reduced states). One mechanism, three consequences:

| Paper | What the C*-bottleneck gives |
|-------|----------------------------|
| 5 | QM (sequential product -> Jordan -> C*) |
| 6 | Smooth geometry (finite-dim -> Fisher manifold) |
| 7 | SM gauge group (C*-observer probes h_3(O) -> F_4 intersection) |

## Files

- Paper 6 source: ~/repos/blog/landing/papers/spacetime-from-self-modeling/
- Paper 6 deployed: ehrlich.dev/papers/spacetime-from-self-modeling-2026.pdf
- Paper 5 (reference): ~/repos/blog/landing/papers/qm-from-self-modeling/
- Derivations target: ~/scratch/get-physics-done/derivations/
- Tests target: ~/scratch/get-physics-done/tests/
