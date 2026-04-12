# Paper 6: Close the Gaps or Identify the Wall

## Philosophy

We don't want a "defensible" paper that hedges everything. We want to
either CLOSE each gap or CLEANLY IDENTIFY it as the wall. The paper
title is "Einstein's Equations from Self-Modeling." Either we earn that
title or we know exactly why we can't.

## The Gaps (5 remaining)

### Gap 1: Diagonal covariance is not derived from self-modeling

**The problem:** The SWAP Hamiltonian follows from diagonal U(n)
covariance via Schur-Weyl. But diagonal covariance is assumed, not
derived. A local lattice theory normally allows independent onsite
basis changes (full U(n) x U(n) gauge redundancy). The restriction
to diagonal U(n) excludes anisotropic couplings and needs justification.

**Attack:** Self-modeling means B contains M as a subsystem, and M
is isomorphic to B (Paper 5). At a boundary between sites x and y,
the self-model probes both sites through the SAME measurement apparatus
(itself). The model doesn't have two independent reference frames for
x and y - it has ONE frame (its own). Therefore rotations must act
identically on both sites as seen by the model.

Formalize: the sequential product a . b = sqrt(a) b sqrt(a) treats
both arguments in the SAME algebra. When the self-model applies a
sequential product across the boundary, it uses one algebra element
(from its own state space) to probe both sites. The covariance is
diagonal because the probe is one object, not two independent objects.

**Task:** Write this as a lemma with proof. If it works, diagonal
covariance is derived from self-modeling. If it doesn't, it's an
input - state it as such and move on.

### Gap 2: The pure-state area law bound (Eq 14) is wrong as stated

**The problem:** The paper claims S(A) <= log(n) |dA| for pure ground
states from "channel capacity" / locality alone. This is FALSE. Generic
pure states on local lattices can have volume-law entanglement. You
need either:
(a) Hastings' area law theorem (2007): gapped ground states of local
    Hamiltonians satisfy area-law entanglement in 1D. Extended to
    higher d under additional assumptions.
(b) The spectral gap of the specific Hamiltonian.

**Attack:** The self-modeling Hamiltonian H = sum J F_xy is a
Heisenberg model. Its spectral gap properties are KNOWN:
- 1D, n=2 (spin-1/2 Heisenberg): gapless, but entanglement has
  logarithmic corrections to area law (Calabrese-Cardy)
- 1D, n>=3 (higher spin Heisenberg): Haldane gap (gapped for integer
  spin). Area law follows from Hastings.
- 2D and higher: believed gapped (Neel order), area law expected
  but not rigorously proved for all n.

**Task:** Replace the channel-capacity argument with the correct one:
1. For gapped phases: invoke Hastings (2007) directly. The Heisenberg
   Hamiltonian is local and bounded. If the spectral gap is nonzero,
   area law follows.
2. For gapless phases (1D critical): cite Calabrese-Cardy (2004) for
   the logarithmic correction S ~ (c/3) log(L). This is still
   "area-law-like" (sub-volume) and sufficient for Jacobson's argument
   (which needs sub-volume scaling, not strict area law).
3. For 2D+: cite the numerical evidence (our own ED results + extensive
   condensed matter literature) and flag that rigorous proof in d>=2
   requires assumptions beyond what we prove.

The key point: the SELF-MODELING Hamiltonian produces area-law-like
entanglement not because of a generic locality argument, but because
it's a SPECIFIC Hamiltonian (Heisenberg) whose entanglement properties
are well-studied. We're not proving a new area law theorem. We're
observing that the Hamiltonian self-modeling forces happens to be one
whose entanglement properties are known.

### Gap 3: MVEH is a hypothesis

**The problem:** "Structural identification" is still a hypothesis.
The reviewer correctly says: "the only available identification" does
not imply "the vacuum extremizes entanglement."

**Attack:** This might actually be closeable. The argument:

1. In a pre-geometric framework, "vacuum" has no prior meaning. We
   DEFINE the vacuum as the state whose modular flow generates smooth
   geometry (Connes-Rovelli thermal time).

2. Among all states, the one whose modular flow is most geometric
   (smoothest, most symmetric) is the one with MAXIMAL entanglement
   at fixed energy. Why? Because:
   - More entanglement = more correlations across regions = smoother
     interpolation between regions = smoother geometry
   - A state with less entanglement has "gaps" in its correlations,
     producing a less smooth geometry (or no geometry at all)
   - The state that maximizes entanglement at fixed <T_ab> is the
     one whose geometry is smoothest, which is the vacuum by definition

3. This connects to Van Raamsdonk (2010): reducing entanglement
   between two regions increases the "distance" between them. In the
   limit of zero entanglement, the geometry disconnects. The maximally
   entangled state (at fixed energy) is the one with the most connected,
   smoothest geometry - i.e., the vacuum.

**Task:** Formalize this argument. If it works, MVEH follows from
"vacuum = smoothest geometry" + "entanglement = geometric connectivity."
If it doesn't, identify exactly what additional assumption is needed
and state it as such. The Van Raamsdonk connection is the key - it's
published, well-cited, and provides the entanglement-geometry link.

### Gap 4: The d>=2 infrared behavior

**The problem:** In d>=2, the Heisenberg AFM likely has Neel order,
not conformal symmetry. Route A needs conformal symmetry for the
CHM formula. Route B avoids this but needs the tensoriality assumption.

**This gap may not be closeable with current mathematics.** The
infrared behavior of the d>=2 Heisenberg model is an open problem
in condensed matter physics. We can't solve it here.

**Task:** State this as the PRINCIPAL OPEN PROBLEM clearly and
without hedging. The paper's result in d>=2 is conditional on the
continuum limit producing a local, tensorial effective theory. This
is the wall. Name it. Don't pretend it's solved.

BUT: also note that this is the SAME wall everyone hits. Jacobson's
original argument has this gap too. The entire "gravity from entanglement"
program (Van Raamsdonk, Maldacena-Susskind, Swingle, Cao-Carroll)
has this gap. We're not worse off than the field. We're exactly where
the field is, but with a UV completion nobody else has.

### Gap 5: Route B tensoriality

**The problem:** Assuming the entanglement-geometry relation is a
symmetric second-order tensor equation is "smuggling in GR structure."

**Attack:** The tensoriality assumption is actually WEAKER than it
looks:
1. Symmetry: follows from metric symmetry (g_ab = g_ba). Any equation
   involving the metric inherits this.
2. Second-order: follows from the entanglement first law being
   FIRST-ORDER in perturbations. First-order perturbation theory on
   a second-order object (the metric) gives at most second derivatives.
   This is not a GR assumption - it's a perturbation theory statement.
3. Tensor character: follows from general covariance of the emergent
   geometry. If the long-wavelength theory has no preferred frame
   (which the Wilsonian continuum limit should ensure for a rotationally
   invariant lattice), equations must be covariant = tensorial.

**Task:** Write out this justification carefully. If it holds up,
tensoriality is derived from: metric symmetry + first-order perturbation
theory + general covariance. If it doesn't, identify which sub-step
fails and state it as an assumption.

## Execution order

1. Gap 2 first (factual error, must fix regardless)
2. Gap 1 (diagonal covariance lemma - attempt the proof)
3. Gap 3 (MVEH from Van Raamsdonk - attempt the argument)
4. Gap 5 (tensoriality justification)
5. Gap 4 (state the wall honestly)

After each gap: either close it (add the proof/argument to the paper)
or identify it as an irreducible input/open problem and state it in
the discussion.

## What the paper looks like when done

Best case (all gaps close): "Einstein's equations from self-modeling"
is literally true. The chain has no gaps. The only inputs are
self-modeling + lattice topology + J>0 + NEC.

Realistic case (gaps 1-3 close, 4-5 remain): The chain is:
self-modeling → QM → SWAP Hamiltonian → area law → MVEH →
entanglement equilibrium → Einstein (in conformal regime) / Einstein
uniqueness (in d>=2, conditional on tensorial continuum limit).
Two stated open problems. Still a strong paper.

Worst case (multiple gaps don't close): The paper becomes "self-modeling
selects a SWAP Hamiltonian whose entanglement structure provides UV
inputs for Jacobson-type gravity arguments." Narrower but honest.

## Key references to add if not already present

- Hastings (2007) "An area law for one-dimensional quantum systems"
  J. Stat. Mech. P08024
- Calabrese, Cardy (2004) "Entanglement entropy and quantum field
  theory" J. Stat. Mech. P06002
- Van Raamsdonk (2010) "Building up spacetime with quantum
  entanglement" Gen. Rel. Grav. 42, 2323
- Eisert, Cramer, Plenio (2010) "Area laws for the entanglement
  entropy" Rev. Mod. Phys. 82, 277
