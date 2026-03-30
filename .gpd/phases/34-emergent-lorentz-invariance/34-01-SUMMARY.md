---
phase: 34-emergent-lorentz-invariance
plan: 01
depth: full
one-liner: "Derived emergent Lorentz invariance from O(3) sigma model: isotropy via RG irrelevance (rho~2), O(d+1) rescaling + DLS reflection positivity, von Ignatowsky supporting route"
subsystem: [derivation]
tags: [lorentz-invariance, sigma-model, isotropy, wick-rotation, von-ignatowsky, reflection-positivity, emergent-spacetime]

requires:
  - phase: 33-correlation-structure-and-effective-theory
    plan: 01
    provides: "O(3) NL sigma model action Eq. (33.11) with c_s = 1.659 Ja, rho_s = 0.181 J, g = 9.18"

provides:
  - "LRNZ-01: Emergent isotropy -- lattice anisotropy corrections scale as O(a^2/L^2), RG irrelevant with exponent rho ~ 2"
  - "LRNZ-02 (primary): Lorentz invariance from sigma model rescaling -- O(d+1) symmetric action, Wick rotation justified by DLS reflection positivity"
  - "LRNZ-02 (secondary): Von Ignatowsky supporting route -- P1-P4 mapped to emergent theory properties"
  - "Emergent Lorentzian metric: ds^2 = -c_s^2 dt^2 + delta_ij dx^i dx^j with c_s = 1.659 Ja"
  - "Relativistic propagator: G_M^{-1} = k^2 - omega^2/c_s^2, poles at omega = +/- c_s |k|"

affects: [35-bisognano-wichmann, 36-assembly]

methods:
  added: [lattice-dispersion-expansion, euclidean-time-rescaling, wick-rotation, von-ignatowsky-theorem]
  patterns: [anisotropy-as-irrelevant-operator, sigma-model-lorentz-derivation]

key-files:
  created:
    - derivations/34-emergent-lorentz-invariance.md

key-decisions:
  - "Isotropy: used RG irrelevance (Hasenbusch rho~2) plus Davoudi-Savage O(a^2) scaling, not numerical simulation"
  - "Wick rotation justified by DLS 1978 reflection positivity on bipartite lattices"
  - "Fisher metric explicitly distinguished from Lorentzian metric (forbidden proxy fp-fisher-is-lorentzian respected)"

patterns-established:
  - "sigma-model-lorentz: rescale tau' = c_s * tau to get O(d+1) action, then Wick rotate"
  - "anisotropy-irrelevance: lattice anisotropy operators have scaling dim d_E + rho with rho > 0"

conventions:
  - "natural_units=natural, hbar=1, k_B=1, a=1"
  - "metric_signature=Riemannian_Fisher (spatial Fisher metric); Lorentzian ds^2 = -c_s^2 dt^2 + dx^2 (emergent spacetime)"
  - "coupling_convention=J>0 AFM"
  - "sigma_model_field=O(3) n-field, n^2=1"
  - "wick_rotation=tau'=-it (standard Euclidean to Minkowski)"
  - "fourier_convention=e^{-ikx} forward"

plan_contract_ref: ".gpd/phases/34-emergent-lorentz-invariance/34-01-PLAN.md#/contract"

contract_results:
  claims:
    claim-isotropy:
      status: passed
      summary: "Emergent isotropy established: lattice magnon dispersion expanded to O((qa)^2), anisotropy coefficient alpha_4 = -1/96 ~ 1% at lattice scale, cubic anisotropy classified as RG irrelevant with exponent rho ~ 2 (Hasenbusch 2021), corrections O(a^2/L^2) (Davoudi-Savage 2012)."
      linked_ids: [deliv-derivation-34-01, test-anisotropy-scaling, test-isotropy-rg, ref-davoudi-savage2012, ref-hasenbusch2021]
    claim-lorentz:
      status: passed
      summary: "Emergent Lorentz invariance derived: rescaled sigma model has O(d+1) Euclidean symmetry Eq. (34.16), Wick rotation gives Lorentzian metric ds^2 = -c_s^2 dt^2 + dx^2 Eq. (34.30), propagator poles at omega = +/- c_s|k| Eq. (34.27), reflection positivity from DLS 1978."
      linked_ids: [deliv-derivation-34-01, test-o-d1-symmetry, test-wick-rotation, test-propagator-poles, ref-chn1989, ref-sachdev-textbook, ref-dls1978]
    claim-von-ignatowsky:
      status: passed
      summary: "Von Ignatowsky route verified: all four premises (P1-P4) mapped to sigma model properties, finite c_s selects Lorentz over Galileo, logical independence from primary route confirmed."
      linked_ids: [deliv-derivation-34-01, test-von-ignatowsky-premises, ref-vonignatowsky1911, ref-baccetti-tate-visser2012]
  deliverables:
    deliv-derivation-34-01:
      status: passed
      path: "derivations/34-emergent-lorentz-invariance.md"
      summary: "Complete derivation document with three parts: (I) isotropy restoration via dispersion expansion + RG, (II) Lorentz invariance from sigma model rescaling + Wick rotation + DLS, (III) von Ignatowsky supporting argument."
      linked_ids: [claim-isotropy, claim-lorentz, claim-von-ignatowsky, test-anisotropy-scaling, test-isotropy-rg, test-o-d1-symmetry, test-wick-rotation, test-propagator-poles, test-von-ignatowsky-premises]
  acceptance_tests:
    test-anisotropy-scaling:
      status: passed
      summary: "Lattice magnon dispersion expanded at small q around Q=(pi,pi). Leading anisotropy: alpha_4 * (qa)^2 * cos(4*phi_q) with alpha_4 = -1/96. Vanishes as q->0. Numerical verification at qa=0.1 shows anisotropy fraction < 0.1% (Python Level 5 check)."
      linked_ids: [claim-isotropy, deliv-derivation-34-01, ref-davoudi-savage2012]
    test-isotropy-rg:
      status: passed
      summary: "Cubic anisotropy operator classified as irrelevant: scaling dimension d_E + rho with rho ~ 2.0 for O(3) (Hasenbusch 2021, Calabrese-Pelissetto-Vicari 2003). Cited Davoudi-Savage (2012) for O(a^2/L^2) lattice QCD discretization artifacts as supporting evidence."
      linked_ids: [claim-isotropy, deliv-derivation-34-01, ref-hasenbusch2021]
    test-o-d1-symmetry:
      status: passed
      summary: "After rescaling tau' = c_s * tau, the sigma model action becomes (1/(2g*c_s)) int d^{d+1}x_E (nabla' n)^2 (Eq. 34.16). The integrand is (d_{tau'} n)^2 + (nabla n)^2, manifestly O(d+1) symmetric with no term distinguishing tau' from x^i."
      linked_ids: [claim-lorentz, deliv-derivation-34-01, ref-phase33-sigma-model]
    test-wick-rotation:
      status: passed
      summary: "Wick rotation tau' = -it yields Minkowski action with (d_t n)^2 - (nabla n)^2 structure (Eq. 34.22). Emergent metric ds^2 = -c_s^2 dt^2 + dx^2 (Eq. 34.30). Sign structure verified by self-critique checkpoint. DLS 1978 reflection positivity cited: applies to bipartite lattice Heisenberg AFM. SWAP lattice on Z^d is bipartite."
      linked_ids: [claim-lorentz, deliv-derivation-34-01, ref-dls1978]
    test-propagator-poles:
      status: passed
      summary: "Euclidean propagator G_E^{-1} = omega_E^2/c_s^2 + k^2 (Eq. 34.25). Wick rotation gives G_M^{-1} = k^2 - omega^2/c_s^2 (Eq. 34.26). Poles at omega = +/- c_s|k| (Eq. 34.27): relativistic dispersion with invariant speed c_s."
      linked_ids: [claim-lorentz, deliv-derivation-34-01]
    test-von-ignatowsky-premises:
      status: passed
      summary: "P1 (relativity principle): universality class determines effective theory, not lattice position. P2 (homogeneity): translation invariance of Heisenberg H, continuous in continuum limit. P3 (isotropy): LRNZ-01 from Part I. P4 (group structure): standard for symmetry transformations. Finite c_s selects Lorentz over Galileo. All four premises mapped with explicit justification."
      linked_ids: [claim-von-ignatowsky, deliv-derivation-34-01, ref-vonignatowsky1911, ref-baccetti-tate-visser2012]
  references:
    ref-davoudi-savage2012:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for O(a^2) rotational symmetry restoration on cubic lattices (lattice QCD context). Applied to isotropy argument."
    ref-hasenbusch2021:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for cubic anisotropy scaling exponent rho ~ 2.0 in O(3) model. Confirms irrelevance of lattice anisotropy."
    ref-chn1989:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as standard reference for 2D quantum Heisenberg NL sigma model. Source of sigma model framework used throughout."
    ref-sachdev-textbook:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for textbook derivation of relativistic sigma model structure and Lorentz invariance."
    ref-dls1978:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for reflection positivity of Heisenberg AFM on bipartite lattices. Key mathematical justification for Wick rotation via Osterwalder-Schrader reconstruction."
    ref-vonignatowsky1911:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited as originator of the theorem deriving Lorentz from isotropy + homogeneity + finite speed without assuming light."
    ref-baccetti-tate-visser2012:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Cited for precise modern statement of von Ignatowsky premises and evasions. Used as framework for mapping premises to emergent theory."
    ref-phase33-sigma-model:
      status: completed
      completed_actions: [cite]
      missing_actions: []
      summary: "Phase 33 NL sigma model action Eq. (33.11) with c_s = 1.659 Ja used as starting point. Not re-derived."
  forbidden_proxies:
    fp-lorentz-by-fiat:
      status: rejected
      notes: "Lorentz invariance explicitly derived from sigma model structure (Part II) and independently from von Ignatowsky premises (Part III). Not assumed."
    fp-vonignatowsky-without-isotropy:
      status: rejected
      notes: "Isotropy independently established in Part I (LRNZ-01) via dispersion expansion + RG irrelevance before applying von Ignatowsky in Part III."
    fp-fisher-is-lorentzian:
      status: rejected
      notes: "Step 17 item 4 explicitly states: 'Fisher metric g_ij^F is Riemannian (positive-definite). Lorentzian structure arises from sigma model dynamics, not from the Fisher metric.'"
  uncertainty_markers:
    weakest_anchors:
      - "No single paper derives emergent Lorentz specifically for the Heisenberg/SWAP lattice -- argument assembled from standard components"
      - "S=1/2 d=2 Neel order is QMC-established, not rigorously proved (inherited from Phase 33)"
    unvalidated_assumptions: []
    competing_explanations: []
    disconfirming_observations:
      - "If the rescaled sigma model action had O(d+1)-breaking terms at leading order (not just O((ka)^2) corrections), the Lorentz derivation would fail"
      - "If reflection positivity failed for the SWAP lattice Hamiltonian, the Wick rotation would not be justified"

duration: 6min
completed: 2026-03-30
---

# Phase 34, Plan 01: Emergent Lorentz Invariance

**Derived emergent Lorentz invariance from O(3) sigma model: isotropy via RG irrelevance (rho~2), O(d+1) rescaling + DLS reflection positivity, von Ignatowsky supporting route**

## Performance

- **Duration:** 6 min
- **Started:** 2026-03-30T03:59:22Z
- **Completed:** 2026-03-30T04:05:06Z
- **Tasks:** 2
- **Files modified:** 1

## Key Results

- **LRNZ-01 (Emergent isotropy):** Lattice anisotropy correction $\alpha_4 (qa)^2 \cos 4\phi_q$ with $\alpha_4 = -1/96 \approx -1\%$ at lattice scale. Cubic anisotropy is RG irrelevant with exponent $\rho \approx 2.0$ (Hasenbusch 2021). Corrections $O(a^2/L^2) \to 0$ in the continuum limit. [CONFIDENCE: HIGH -- standard RG result, cited quantitative exponent]
- **LRNZ-02 (Lorentz invariance):** Rescaling $\tau' = c_s\tau$ converts sigma model to O($d+1$)-symmetric form Eq. (34.16). Wick rotation $\tau' = -it$ yields Lorentzian metric $ds^2 = -c_s^2 dt^2 + \delta_{ij}dx^i dx^j$ with invariant speed $c_s = 1.659\,Ja$. Justified by DLS 1978 reflection positivity. [CONFIDENCE: HIGH -- standard textbook argument with rigorous mathematical foundation]
- **Von Ignatowsky (supporting):** All four premises (relativity principle, homogeneity, isotropy, group structure) mapped to emergent sigma model properties. Finite $c_s$ selects Lorentz over Galileo. Logically independent of the sigma model route. [CONFIDENCE: HIGH -- theorem is exact; mapping of premises is clear]

## Task Commits

1. **Task 1+2: Isotropy restoration + Lorentz derivation + von Ignatowsky** - `a020cd3` (derive)

**Plan metadata:** (pending)

## Files Created/Modified

- `derivations/34-emergent-lorentz-invariance.md` - Complete derivation: Part I (isotropy), Part II (Lorentz from sigma model), Part III (von Ignatowsky)

## Next Phase Readiness

- Emergent Lorentzian metric $ds^2 = -c_s^2 dt^2 + dx^2$ ready for Phase 35 (Bisognano-Wichmann theorem)
- Lorentz-invariant QFT established, satisfying prerequisites for the modular Hamiltonian $\to$ Rindler wedge argument
- Invariant speed $c_s = 1.659\,Ja$ available as the "speed of light" for the emergent spacetime
- Reflection positivity (DLS 1978) confirms unitarity of the Wick-rotated theory

## Contract Coverage

- claim-isotropy -> passed (RG irrelevance with $\rho \approx 2$, $O(a^2/L^2)$ corrections)
- claim-lorentz -> passed (O($d+1$) rescaling + Wick rotation + DLS reflection positivity)
- claim-von-ignatowsky -> passed (all four premises mapped, finite $c_s$ selects Lorentz)
- deliv-derivation-34-01 -> passed (derivations/34-emergent-lorentz-invariance.md)
- test-anisotropy-scaling -> passed ($\alpha_4 = -1/96$, numerical verification)
- test-isotropy-rg -> passed (scaling dimension $d_E + \rho$, $\rho \approx 2.0$)
- test-o-d1-symmetry -> passed (action manifestly O($d+1$) after rescaling)
- test-wick-rotation -> passed (correct sign structure, DLS cited)
- test-propagator-poles -> passed ($\omega = \pm c_s|\mathbf{k}|$)
- test-von-ignatowsky-premises -> passed (P1-P4 mapped)
- ref-davoudi-savage2012 -> completed (cited)
- ref-hasenbusch2021 -> completed (cited)
- ref-chn1989 -> completed (cited)
- ref-sachdev-textbook -> completed (cited)
- ref-dls1978 -> completed (cited)
- ref-vonignatowsky1911 -> completed (cited)
- ref-baccetti-tate-visser2012 -> completed (cited)
- ref-phase33-sigma-model -> completed (cited, not re-derived)
- fp-lorentz-by-fiat -> rejected (derived, not assumed)
- fp-vonignatowsky-without-isotropy -> rejected (isotropy established independently in Part I)
- fp-fisher-is-lorentzian -> rejected (explicitly distinguished in Step 17)

## Equations Derived

**Eq. (34.7): Anisotropic dispersion**

$$
\omega_\mathbf{q} = c_s^{\text{cl}}|\mathbf{q}|\left[1 - (qa)^2\left(\frac{3}{32} + \frac{\cos 4\phi_\mathbf{q}}{96}\right) + O((qa)^4)\right]
$$

**Eq. (34.16): O($d+1$)-symmetric sigma model**

$$
S_{\text{eff}} = \frac{1}{2gc_s}\int d^{d+1}x_E\;(\boldsymbol{\nabla}'\mathbf{n})^2, \quad \mathbf{n}^2 = 1
$$

**Eq. (34.30): Emergent Lorentzian metric**

$$
ds^2 = -c_s^2\,dt^2 + \delta_{ij}\,dx^i\,dx^j
$$

## Validations Completed

- Dispersion expansion: full LSWT dispersion vs approximation matches to 7 significant figures at $qa = 0.1$ (Python Level 5)
- Trig identity $\cos^4\phi + \sin^4\phi = 3/4 + (1/4)\cos 4\phi$: verified at 5 test points
- Prefactor consistency: $1/(2gc_s)$ vs $\rho_s/(dc_s^2)$ agree to 0.03%
- Sign structure: Wick rotation $\tau' = -it$ produces correct $(\partial_t\mathbf{n})^2 - (\nabla\mathbf{n})^2$ (self-critique checkpoint at Steps 7 and 9)
- Dimensional analysis: $[\tau'] = [x^i]$ after rescaling (necessary for O($d+1$) symmetry)
- Propagator poles: $\omega = \pm c_s|\mathbf{k}|$ from $G_M^{-1} = k^2 - \omega^2/c_s^2 = 0$

## Decisions & Deviations

### Decisions

- Combined Tasks 1 and 2 into a single derivation file write (Parts I-III in one document) for coherence
- Used RG irrelevance argument (Hasenbusch exponent) rather than direct numerical simulation for isotropy
- Distinguished Fisher metric (Riemannian) from emergent Lorentzian metric (Step 17)

### Deviations from Plan

None -- plan executed as specified. Tasks 1 and 2 merged into a single write for the derivation file, but all content from both tasks is present.

## Approximations Used

| Approximation | Valid When | Error Estimate | Breaks Down At |
|---------------|-----------|----------------|----------------|
| NL sigma model continuum limit | $ka \ll 1$ | $O((ka)^2)$ | $k \sim \pi/a$ |
| Cubic anisotropy irrelevant | $L \gg a$ | $O(a^2/L^2)$ | $L \sim a$ |
| Gaussian propagator (free field) | weak coupling | $O(g)$ corrections | strong coupling |

## Open Questions

- How does the velocity hierarchy ($c_s < v_{\text{LR}}$) affect the emergent causal structure at intermediate length scales?
- Is the connection between the emergent $c_s$ and the physical speed of light made in Paper 8 or Phase 36?
- Does the topological sector (skyrmions) in $d = 2$ modify the Lorentz structure at any level?

## Self-Check: PASSED

- [x] derivations/34-emergent-lorentz-invariance.md exists
- [x] Commit a020cd3 exists
- [x] All contract IDs covered (3 claims, 1 deliverable, 6 acceptance tests, 8 references, 3 forbidden proxies)
- [x] No forbidden proxies violated
- [x] Numerical verification via Python (Level 5)
- [x] Convention assertion line present in derivation file
- [x] All 7 references cited

---

_Phase: 34-emergent-lorentz-invariance_
_Plan: 01_
_Completed: 2026-03-30_
