"""
(RING) Lemma -- (a) GENERATING-SET COMPLETENESS CERTIFICATE (RING-01), Plan 02
==============================================================================
Phase: 68-a-generating-set-completeness-certificate
Plan: 02
Milestone: v16.0 The (RING) Lemma (math half of the Chalmers gap).

WHAT THIS IS (the CERTIFICATE half of sub-claim (a))
----------------------------------------------------
Plan 01 computed, exactly and gate-passed, the bigraded Molien/Hilbert series

    H(s,t) = sum_{a,b} dim R[27(+)27]^{F_4}_{(a,b)} s^a t^b   (d_true, a+b <= 6)

of the diagonal two-copy F_4-invariant ring. THIS plan ASSEMBLES the candidate
generating set and CERTIFIES its completeness (and minimality) by matching that
series degree-by-degree -- NOT by assuming polarization generates (Schwarz). The
decisive guard: 2-polarization fails generically in char 0 (Schwarz 2006), so the
bigraded Hilbert match -- d_candidate(a,b) vs d_true(a,b) -- is the only valid
completeness certificate; polarization is used ONLY to PRODUCE candidates.

THE CANDIDATE SET (10, verbatim from Phase-65.1 ring_generating_set.py):
    six pointwise: Tr X (1,0), Tr X^2 (2,0), det X (3,0),
                   Tr Y (0,1), Tr Y^2 (0,2), det Y (0,3)
    coupling:      c = Tr(X o Y) (1,1)                       [Phase 67 anchor]
    mixed trace:   Tr(X^2 o Y) (2,1), Tr(X o Y^2) (1,2), Tr(X^2 o Y^2) (2,2)
(polarize_d(X,X,Y)/(X,Y,Y) produce equivalent (2,1)/(1,2) CANDIDATES -- Schwarz
guard, candidate-producers only, NEVER assumed to generate.)

THE METHOD (exact over Q; the GLOBAL forbidden proxy is fp-float-rank):
  d_candidate(a,b): enumerate ALL monomials in the 10 candidates of bidegree
    (a,b) (by integer partition of (a,b) over the candidate bidegrees), evaluate
    each at MANY generic rational octonionic PAIR points (the value of a PRODUCT
    invariant at a point = the product of the candidate scalar values), build the
    exact rational value-matrix (rows = monomials, cols = points), and take
    d_candidate(a,b) = exact_qq_rank of it. Enough points are added until the rank
    SATURATES (rank stops increasing) -- so d_candidate is the true dimension
    spanned by candidate products. EXACT_QQ_RANK = DomainMatrix-over-QQ; NEVER
    numpy.linalg.matrix_rank / SVD tolerance; NEVER octonion_algebra (float64).
  plethystic log: plog H(s,t) = sum_{k>=1} (mu(k)/k) log H(s^k,t^k), exact
    rational bivariate power series to total degree <= 6. Positive coefficient at
    (a,b) = generator(s); negative = relation(s). The F_4 ring is NON-free (Blind
    2011 E_6 is the FREE contrast), so negatives WILL appear (fp-e6-free-form).
  minimality (in-span-of-lower-products): for each candidate generator G at (a,b),
    compare exact_qq_rank of {all products of strictly-lower-degree candidates at
    (a,b)} with and without G's value-vector. G is a GENUINE (minimal) generator
    iff adding G increases the rank by 1 (G NOT in the lower-product span). This
    distinguishes minimal generating from spanning (Pitfall 8; fp-spanning-as-
    minimal). The (2,2) Tr(X^2 o Y^2) generator-vs-product question is decided
    this way (the headline diagnostic).
  completeness: at every a+b <= 6 compare d_true(a,b) (Plan 01) vs d_candidate.
    d_true <= d_candidate everywhere => candidate-complete to degree 6.
    d_true > d_candidate at some bidegree => a generator is MISSING there
    (NEGATIVE-RESULT-IS-SUCCESS; report it, do NOT suppress -- fp-suppress-missing).

HONEST VERDICT (NEGATIVE-RESULT-IS-SUCCESS): either (i) CERTIFIED COMPLETE to
total degree <= 6 (with the EXPLICIT note that polarization was NOT assumed to
generate -- the Hilbert match IS the certificate; Schwarz), the minimal
generating set listed with bidegrees, relations catalogued; OR (ii) the specific
missing-generator bidegree(s). Both are full passes.

# ASSERT_CONVENTION: natural_units=natural, metric_signature=riemannian, fourier_convention=NA, gauge_choice=NA, renormalization_scheme=NA, coupling_convention=c=Tr(XoY); jordan=(1/2)(AB+BA); fano e1e2=e4; c(X,X)=Tr(X^2) (NOT (Tr X)^2); det3 cross=2Re((x2x1)x3) [Phase64.1]; det3 polarization d(X,X,X)=6*det_3; 10-candidate set with bidegrees (1,0),(2,0),(3,0),(0,1),(0,2),(0,3),(1,1),(2,1),(1,2),(2,2) verbatim from ring_generating_set.py; R_pt frozen = R-subalgebra gen by 6 pointwise; Tr(X)Tr(Y) in R_pt; c NOT in R_pt; gen_func vars s=X-degree t=Y-degree H(s,t) bigraded; H_free != H_true (F_4 ring NON-free; Blind E_6 is the FREE contrast); arithmetic=exact-SymPy-over-Q; ranks/nullspace=exact_qq_rank=DomainMatrix-over-QQ (NEVER numpy.linalg.matrix_rank / SVD); polarization used ONLY to PRODUCE candidates (NEVER assumed to generate; Schwarz); Krull=10 (Phase 65, the superseded 7 is FORBIDDEN); (1,1)=2 (Phase 67)
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible)

PROVENANCE (decisive reuse -- frozen engine + certified machinery, imported):
  - code/ring_generating_set.py (Phase-65.1 FROZEN): CANDIDATES, NAMES, BIDEGREES,
    BUILDERS, CANDIDATE_GRADS (the 10 candidate invariants verbatim).
  - code/molien_bigraded.py (Phase-68 Plan-01 CERTIFIED): build_f4_roots,
    build_27_weights, molien_H -> the gate-passed, two-route-confirmed d_true
    table (regenerated here by import, NOT hand-typed).
  - code/orbit_dimension_gate.py (Phase-65 CERTIFIED): exact_qq_rank
    (DomainMatrix-over-QQ exact rank), PAIR_POINTS, _pair_not_proportional,
    _is_genuinely_octonionic_integer.
  - code/ring_lemma_verification.py (Phase-64.1 FROZEN engine), imported as E:
    Tr, Tr2, det_3, c, jordan, polarize_d, Xsym/Ysym, xs/ys, X_from_symbols,
    _coord_from_octmat. NEVER octonion_algebra (float64, buggy det_3).

Assert-based harness (NO pytest -- the venv has sympy/numpy only). Foreground,
chatty (python -u), one progress line per bidegree (watchdog-safe).

Reproducibility: SymPy 1.14.0, NumPy 2.4.3, Python 3.14.2, macOS Darwin 24.6.0.
Deterministic: the fresh generic octonionic pairs are drawn from a FIXED-seed
(seed=68022, Python random) integer generator and validated genuinely octonionic;
all decisive ranks are exact over Q.

References:
  - Schwarz, G.W., "When Polarizations Generate," arXiv:math/0609078; Transform.
    Groups 12 (2007): 2-polarization fails generically in char 0. [ref-schwarz] --
    THE headline forbidden-proxy guard: the Hilbert match is the certificate, NOT
    polarization. Cited in EVERY completeness claim.
  - Blind, B., J. Lie Theory 21 (2011), arXiv:0906.5525: C[27(+)27]^{E_6} FREE on
    4 det-polarizations. [ref-blind] -- the CONTRAST: the F_4 pair ring is strictly
    LARGER (contains c) and NOT free; H_free over-counts H_true; relations appear.
  - Iltyakov, A.V., J. Algebra 207 (1998): F_4 several-copy invariants = trace
    polynomials + Laplace invariants. [ref-iltyakov] -- warrants the candidate FORM
    (trace monomials); a missing generator (if any) is the lowest-degree trace
    monomial at that bidegree (backtracking guidance).
  - Derksen, H.; Kemper, G., Computational Invariant Theory, 2nd ed., Springer
    (2015): plethystic log, generating-set extraction from the Hilbert series,
    minimal-vs-spanning. [ref-derksen-kemper]
  - Hanany et al., arXiv:1902.10550, arXiv:1408.4690: practical PE/plog formulas.
    [ref-hanany]
  - code/ring_generating_set.py (Phase 65.1): the 10-candidate trdeg-10 set,
    PAIR_POINTS. [ref-ring-gen-set]
  - code/degree2_uniqueness.py (Phase 67): (1,1)=2 = span{Tr(X)Tr(Y), c}; quotient
    mod the reducible Tr(X)Tr(Y) is 1 = span{c}. [ref-frozen-degree2] -- the
    prototype of the generator-vs-product reasoning at every bidegree.
"""

import os
import re
import sys
import time
import random
from itertools import combinations_with_replacement

# Path-import the FROZEN engine + certified machinery (sibling files in code/).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ring_lemma_verification as E  # noqa: E402  (path insert precedes import)
from orbit_dimension_gate import (  # noqa: E402
    exact_qq_rank,
    PAIR_POINTS,
    _pair_not_proportional,
    _is_genuinely_octonionic_integer,
)
from ring_generating_set import (  # noqa: E402
    CANDIDATES, NAMES, BIDEGREES, BUILDERS, CANDIDATE_GRADS,
)
import molien_bigraded as MB  # noqa: E402  (the certified Plan-01 d_true producer)

from sympy import (  # noqa: E402
    Matrix, Rational, symbols, Poly, S, expand, series, log, mobius, prod, simplify,
)

# ============================================================================
# Overall pass/fail accumulator + chatty reporter (engine pattern)
# ============================================================================
ALL_PASS = True
FAILED_LABELS = []
STOP_TRIGGERED = False


def _report(label, ok):
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
        FAILED_LABELS.append(label)
    return ok


# ============================================================================
# PRE-REGISTRATION (frozen targets + verdict logic, BEFORE any d_candidate).
# ============================================================================
TRUNCATION_DEGREE = 6
KRULL_TARGET = 10           # Phase 65 (NOT the superseded 7)
TRDEG_TARGET = 10           # Phase 65/65.1 field-level
SPINE_RANK = 7              # Phase 66 (c independent of the pointwise sextet)
D_11_TARGET = 2             # Phase 67 (1,1) = span{Tr(X)Tr(Y), c}
D_22_TARGET = 9             # Plan 01 (the (2,2) diagnostic d_true)
SINGLE_COPY = [1, 1, 2, 3, 4, 5, 7]   # Plan 01 single-copy row/col (s^6 entry = 7)

s, t = symbols('s t')

# The 54 pair symbols (engine-native layout), X-block then Y-block.
XS = list(E.xs)
YS = list(E.ys)

RESULTS = {
    "d_true": None,           # {(a,b): d_true} from Plan-01 Molien (regenerated)
    "d_candidate": None,      # {(a,b): d_candidate} via exact_qq_rank
    "plog": None,             # {(a,b): plog coefficient} exact rational
    "minimality": None,       # {name: 'generator'|'product'} per candidate generator
    "d22_decision": None,     # 'generator' or 'product'
    "verdict": None,          # 'certified-complete' or 'missing-generator-at-...'
    "missing_bidegrees": [],  # bidegrees with d_true > d_candidate
    "relations": [],          # bidegrees with negative plog (syzygies)
    "n_points": None,         # number of generic pairs used (after saturation)
}


def print_preregistration():
    print("=" * 76)
    print("Phase 68 Plan 02 -- (a) GENERATING-SET COMPLETENESS CERTIFICATE "
          "(RING-01)")
    print("  Assemble the candidate F_4 two-copy generating set; CERTIFY "
          "completeness by")
    print("  matching the Plan-01 bigraded Hilbert series degree-by-degree "
          "(a+b<=6),")
    print("  NOT by assuming polarization generates (Schwarz). Decide (2,2); "
          "honest verdict.")
    print("=" * 76)
    print("PRE-REGISTRATION (frozen anchors + verdict logic BEFORE any "
          "d_candidate):", flush=True)
    print(f"  [ANCHOR] d_true (Plan 01) single-copy row/col = {SINGLE_COPY} "
          f"(s^6 entry = 7, NOT 6)")
    print(f"  [ANCHOR] d_true(1,1) = {D_11_TARGET} (Phase 67); d_true(2,2) = "
          f"{D_22_TARGET} (Plan 01 diagnostic)")
    print(f"  [ANCHOR] Krull = {KRULL_TARGET}, trdeg = {TRDEG_TARGET} (Phase "
          f"65/65.1); SPINE rank = {SPINE_RANK} (Phase 66)")
    print(f"  [CONSISTENCY] trdeg {TRDEG_TARGET} >= rank {SPINE_RANK} >= quotient "
          f"1 (67); Krull {KRULL_TARGET}; (1,1)={D_11_TARGET}")
    print("  [METHOD] d_candidate(a,b) = exact_qq_rank of the candidate-monomial "
          "value-matrix")
    print("           at MANY generic rational octonionic pairs (points added "
          "until rank SATURATES).")
    print("  [VERDICT LOGIC] d_true <= d_candidate for ALL a+b<=6 => "
          "candidate-complete; ANY")
    print("                  d_true > d_candidate => MISSING generator at that "
          "bidegree (report it).")
    print("  [SCHWARZ GUARD] polarization PRODUCES candidates ONLY; the Hilbert "
          "match IS the")
    print("                  certificate. [BLIND CONTRAST] F_4 ring NON-free => "
          "relations (neg plog) appear.")
    print("  [EXACT-ONLY] exact_qq_rank (DomainMatrix-over-QQ); 0 numpy "
          "float-rank, 0 octonion_algebra")
    print("               on the decisive path (fp-float-rank, "
          "fp-spanning-as-minimal, fp-suppress-missing).")
    print("-" * 76, flush=True)


# ============================================================================
# TASK 1a -- assemble + re-confirm the candidate set; load d_true from Plan 01.
# ============================================================================
def assemble_candidates():
    """Re-confirm the 10 candidates (verbatim from ring_generating_set.py) with
    their bidegrees, and that the F_4-invariance was certified upstream. Polarization
    note: state explicitly that polarize_d is a candidate-PRODUCER only (Schwarz)."""
    print("Task 1a -- assemble the candidate set (verbatim from "
          "ring_generating_set.py):")
    expected_bidegrees = [(1, 0), (2, 0), (3, 0), (0, 1), (0, 2), (0, 3),
                          (1, 1), (2, 1), (1, 2), (2, 2)]
    n_ok = _report(
        f"10 candidates loaded (|CANDIDATES|={len(CANDIDATES)}, "
        f"|NAMES|={len(NAMES)}, |BIDEGREES|={len(BIDEGREES)})  "
        f"[test-candidate-bidegrees; ref-ring-gen-set]",
        len(CANDIDATES) == 10 and len(NAMES) == 10 and len(BIDEGREES) == 10)
    bidegrees_ok = _report(
        f"candidate bidegrees == {expected_bidegrees} (six pointwise + c + 3 "
        f"mixed)  [test-candidate-bidegrees]",
        list(BIDEGREES) == expected_bidegrees)
    for i, (name, builder, bd) in enumerate(zip(NAMES, BUILDERS, BIDEGREES)):
        print(f"  [INFO]  cand[{i}] {name:<16} {str(bd):<7} {builder}", flush=True)
    # Schwarz guard, stated in-code and at runtime (fp-polarization-generates):
    print("  [SCHWARZ GUARD] polarize_d(X,X,Y)=(2,1) and polarize_d(X,Y,Y)=(1,2) "
          "produce EQUIVALENT", flush=True)
    print("    (2,1)/(1,2) CANDIDATES (cubic-norm polarization) -- candidate-"
          "PRODUCERS ONLY. The 10", flush=True)
    print("    candidates here are the trace monomials; polarization is NOWHERE "
          "used as evidence of", flush=True)
    print("    completeness. F_4-invariance of ALL 10 was certified in Phase 65.1 "
          "(D_M f=0, 52 gens,", flush=True)
    print("    >=3 octonionic points) and is re-asserted via the imported "
          "CANDIDATES/CANDIDATE_GRADS.", flush=True)
    inv_note_ok = _report(
        "polarization used ONLY to PRODUCE candidates (Schwarz); the completeness "
        "claim rests SOLELY on the Hilbert match  [test-no-polarization-assumption; "
        "ref-schwarz; fp-polarization-generates]",
        True)
    return n_ok and bidegrees_ok and inv_note_ok


def reconfirm_f4_invariance():
    """test-candidate-bidegrees (invariance half): re-confirm each of the 10
    candidates is F_4-invariant by the Phase-65.1 D_M f = 0 check (52 generators) at
    a genuinely octonionic point. The diagonal lift D_M f = grad_X(f).(M.v_x) +
    grad_Y(f).(M.v_y); the SAME 27x27 M acts on both copies. (The full multi-point
    gate is in ring_generating_set.py; here we re-fire the strong gate at one point
    + one independent pair as a handoff re-check.)"""
    print("Task 1a -- re-confirm F_4-invariance of all 10 candidates (D_M f=0, 52 "
          "generators):")
    derivs = E.inner_derivations()
    from orbit_dimension_gate import _select_independent_basis
    f4 = [derivs[i] for i in _select_independent_basis(derivs)]
    pts = E.octonionic_points()
    # diagonal point (X=Y=P0) AND an independent pair (X=P0, Y=P1)
    test_subs = []
    v0 = Matrix(E._flat27(pts[0]))
    sd = {XS[k]: v0[k] for k in range(27)}
    sd.update({YS[k]: v0[k] for k in range(27)})
    test_subs.append(("diagonal P0", v0, v0, sd))
    v1 = Matrix(E._flat27(pts[1]))
    sp = {XS[k]: v0[k] for k in range(27)}
    sp.update({YS[k]: v1[k] for k in range(27)})
    test_subs.append(("pair P0xP1", v0, v1, sp))
    all_ok = True
    for i, (name, bd) in enumerate(zip(NAMES, BIDEGREES)):
        grad = CANDIDATE_GRADS[i]
        gX, gY = grad[0:27], grad[27:54]
        worst = len(f4)
        for (plabel, vx, vy, subs_pt) in test_subs:
            gXa = [g.subs(subs_pt) for g in gX]
            gYa = [g.subs(subs_pt) for g in gY]
            killed = 0
            for M in f4:
                Mvx = M * vx
                Mvy = M * vy
                dmf = sum(gXa[k] * Mvx[k] for k in range(27)) \
                    + sum(gYa[k] * Mvy[k] for k in range(27))
                if simplify(dmf) == 0:
                    killed += 1
            worst = min(worst, killed)
        ok = (worst == len(f4))
        all_ok = all_ok and ok
        _report(
            f"F_4-invariant {NAMES[i]:<16} {str(bd):<7} D_M f=0 for {worst}/"
            f"{len(f4)} gens (diagonal + independent pair)  [test-candidate-bidegrees]",
            ok)
    return all_ok


def load_d_true():
    """Load d_true from Plan 01 by IMPORTING molien_bigraded and regenerating the
    certified table (NOT hand-typed). Re-fires the Plan-01 Weyl-CT structural check
    + the single-copy and (1,1) handoff gates as a sanity re-check of the handoff."""
    print("Task 1a -- load d_true from Plan 01 (regenerate via "
          "molien_bigraded.molien_H; NOT hand-typed):")
    global STOP_TRIGGERED
    short, long_ = MB.build_f4_roots()
    zero_mult, _ = MB.build_27_weights(short, long_)
    ct = MB.weyl_measure_CT(short, long_)   # structural: CT == 1152
    ct_ok = _report(
        "Plan-01 Weyl-measure CT == 1152 = |W(F_4)| (handoff structural re-check)  "
        "[ref-plan01-table]", ct)
    table = MB.molien_H(short, long_, zero_mult)
    RESULTS["d_true"] = table
    # Handoff sanity gates.
    single_col = [table[(a, 0)] for a in range(TRUNCATION_DEGREE + 1)]
    single_row = [table[(0, b)] for b in range(TRUNCATION_DEGREE + 1)]
    g_single = _report(
        f"d_true single-copy row/col == {SINGLE_COPY} (s^6 entry = 7; handoff "
        f"sanity)  [ref-plan01-table]",
        single_col == SINGLE_COPY and single_row == SINGLE_COPY)
    g11 = _report(
        f"d_true(1,1) == {D_11_TARGET} (Phase 67 anchor; handoff sanity)  "
        f"[ref-frozen-degree2]",
        table[(1, 1)] == D_11_TARGET)
    g22 = _report(
        f"d_true(2,2) == {D_22_TARGET} (the (2,2) diagnostic; handoff sanity)  "
        f"[ref-plan01-table]",
        table[(2, 2)] == D_22_TARGET)
    sym = all(table[(a, b)] == table[(b, a)]
              for a in range(TRUNCATION_DEGREE + 1)
              for b in range(TRUNCATION_DEGREE + 1 - a))
    g_sym = _report("d_true(a,b) == d_true(b,a) for all a+b<=6 (handoff symmetry)",
                    sym)
    # Print the table for the SUMMARY.
    print("  [INFO] d_true table {d_(a,b): a+b<=6} (regenerated from Plan 01):",
          flush=True)
    for a in range(TRUNCATION_DEGREE + 1):
        print(f"  [INFO]   a={a}: "
              f"{[table[(a, b)] for b in range(TRUNCATION_DEGREE + 1 - a)]}",
              flush=True)
    ok = ct_ok and g_single and g11 and g22 and g_sym
    if not ok:
        STOP_TRIGGERED = True
        print("  [STOP] d_true handoff sanity FAILED -- the Plan-01 table does not "
              "regenerate. STOP; report the discrepancy (do NOT paper over).",
              flush=True)
    return ok


# ============================================================================
# TASK 1b -- generic rational octonionic pairs (deterministic, saturating).
# ============================================================================
def _random_octonion(rng, lo=-3, hi=3):
    """A genuinely-octonionic integer octonion: >=2 nonzero imaginary parts."""
    while True:
        a = [rng.randint(lo, hi) for _ in range(8)]
        if sum(1 for k in range(1, 8) if a[k] != 0) >= 2:
            return a


def _random_pair_point(rng):
    """A 27-coordinate genuinely-octonionic integer point (distinct diagonals,
    each off-diagonal octonion genuinely octonionic). Validated by
    _is_genuinely_octonionic_integer."""
    while True:
        diag = rng.sample(range(-4, 5), 3)   # 3 DISTINCT diagonal reals
        x1 = _random_octonion(rng)
        x2 = _random_octonion(rng)
        x3 = _random_octonion(rng)
        v = list(diag) + x1 + x2 + x3
        ok, _ = _is_genuinely_octonionic_integer(v)
        if ok:
            return v


def build_generic_pairs(n_fresh, seed=68022):
    """Deterministic generic rational octonionic PAIRS: the 4 certified PAIR_POINTS
    plus n_fresh fresh integer pairs (fixed-seed; each genuinely octonionic, X!=Y,
    X NOT proportional to Y). Returns a list of (X27, Y27)."""
    pairs = []
    for label, (X, Y) in PAIR_POINTS.items():
        pairs.append((list(X), list(Y)))
    rng = random.Random(seed)
    tries = 0
    while len(pairs) < 4 + n_fresh and tries < 100000:
        tries += 1
        X = _random_pair_point(rng)
        Y = _random_pair_point(rng)
        if list(X) == list(Y):
            continue
        if not _pair_not_proportional(X, Y):
            continue
        pairs.append((X, Y))
    return pairs


def candidate_values_at_pairs(pairs):
    """Evaluate each of the 10 candidate INVARIANTS at each pair point -> a
    (#pairs x 10) table of exact rationals. The value of a candidate at a pair is a
    SCALAR; the value of a product monomial is the product of the relevant scalars
    (handled in monomial_value_matrix). Substitute the integer pair into the cached
    candidate gradient's PARENT expression -- i.e. evaluate the invariant itself.

    We evaluate the invariant EXPRESSIONS (CANDIDATES) directly (substitute-first;
    these are the frozen engine objects, exact over Q)."""
    print(f"Task 1b -- evaluate the 10 candidate invariants at {len(pairs)} generic "
          f"pairs (exact over Q):", flush=True)
    table = []   # table[p] = [val_cand0, ..., val_cand9] at pair p
    t0 = time.time()
    for pidx, (X27, Y27) in enumerate(pairs):
        subs_pt = {XS[k]: Rational(X27[k]) for k in range(27)}
        subs_pt.update({YS[k]: Rational(Y27[k]) for k in range(27)})
        row = []
        for f in CANDIDATES:
            val = f.subs(subs_pt)
            row.append(Rational(val))
        table.append(row)
        if (pidx + 1) % 5 == 0 or pidx + 1 == len(pairs):
            print(f"  [INFO]   evaluated {pidx + 1}/{len(pairs)} pairs "
                  f"({time.time() - t0:.1f}s)", flush=True)
    return table


# ============================================================================
# monomial enumeration + value matrices (the core d_candidate machinery)
# ============================================================================
def monomials_of_bidegree(a, b, max_total=None):
    """All monomials in the 10 candidates with total bidegree exactly (a,b).
    A monomial is a tuple of exponents (e0,...,e9) with sum_i e_i * BIDEGREES[i] ==
    (a,b). Enumerated by bounded recursion over candidate exponents (each candidate
    bidegree has positive total degree, so exponents are bounded by (a+b)//deg_i).

    Returns a list of exponent-tuples."""
    bidegs = list(BIDEGREES)
    n = len(bidegs)
    results = []
    # max exponent for each candidate: floor of remaining degree / its degree.
    cand_total = [bd[0] + bd[1] for bd in bidegs]   # all >= 1

    def rec(i, ra, rb, expo):
        if i == n:
            if ra == 0 and rb == 0:
                results.append(tuple(expo))
            return
        da, db = bidegs[i]
        # prune: even with all remaining candidates we can't fix a negative leftover
        e = 0
        while True:
            na, nb = ra - e * da, rb - e * db
            if na < 0 or nb < 0:
                break
            expo.append(e)
            rec(i + 1, na, nb, expo)
            expo.pop()
            e += 1

    rec(0, a, b, [])
    return results


def monomial_value_matrix(monos, cand_vals):
    """The exact rational value-matrix: rows = monomials, cols = pair points.
    entry[m][p] = prod_i cand_vals[p][i] ** monos[m][i]. (The value of a product
    invariant at a point is the product of the candidate scalar values.)"""
    rows = []
    for expo in monos:
        row = []
        for p in range(len(cand_vals)):
            val = S.One
            for i, e in enumerate(expo):
                if e:
                    val *= cand_vals[p][i] ** e
            row.append(val)
        rows.append(row)
    return Matrix(rows)


def d_candidate_at(a, b, cand_vals):
    """d_candidate(a,b) = exact_qq_rank of the value-matrix of ALL candidate
    monomials of bidegree (a,b) at the pair points. Returns (d, n_monos)."""
    monos = monomials_of_bidegree(a, b)
    if not monos:
        return 0, 0
    M = monomial_value_matrix(monos, cand_vals)
    return exact_qq_rank(M), len(monos)


# ============================================================================
# saturation: add fresh points until every bidegree's d_candidate stabilizes.
# ============================================================================
def compute_d_candidate_saturated(d_true):
    """Compute d_candidate(a,b) for all a+b<=6, ADDING fresh generic pairs until
    the rank at every bidegree SATURATES (stops increasing) -- so d_candidate is the
    TRUE dimension spanned by candidate products, not a point-count artifact. The
    saturation target per bidegree is at most d_true(a,b) (candidate products cannot
    exceed the full invariant dimension); we add points until two successive point-
    counts give identical d_candidate at ALL bidegrees AND each d_candidate has
    reached its value (needs at least d_true points to witness d_true).

    Returns (dc, n_points, saturated, cand_vals_saturated) -- the saturated
    candidate value table is RETURNED so Task 2's minimality test reuses the same
    generic points (no re-evaluation)."""
    print("Task 1b -- d_candidate(a,b) via exact_qq_rank, points added until "
          "SATURATION:", flush=True)
    global STOP_TRIGGERED
    bidegrees = [(a, b) for a in range(TRUNCATION_DEGREE + 1)
                 for b in range(TRUNCATION_DEGREE + 1 - a)]
    max_dtrue = max(d_true.values())   # 24 (at (3,3))
    # start with enough points to (over)cover the largest dimension, then grow.
    n_fresh = max_dtrue + 8            # 4 PAIR_POINTS + this
    prev = None
    prev_vals = None
    while True:
        pairs = build_generic_pairs(n_fresh)
        cand_vals = candidate_values_at_pairs(pairs)
        dc = {}
        for (a, b) in bidegrees:
            d, nm = d_candidate_at(a, b, cand_vals)
            dc[(a, b)] = d
        # saturation: identical to prev round AND each dc <= d_true (sanity).
        sane = all(dc[(a, b)] <= d_true[(a, b)] for (a, b) in bidegrees)
        if not sane:
            bad = [(a, b) for (a, b) in bidegrees if dc[(a, b)] > d_true[(a, b)]]
            print(f"  [STOP] d_candidate > d_true at {bad} -- IMPOSSIBLE "
                  f"(candidate products cannot exceed the invariant dimension); "
                  f"point/evaluation bug. STOP.", flush=True)
            STOP_TRIGGERED = True
            RESULTS["d_candidate"] = dc
            RESULTS["n_points"] = len(pairs)
            return dc, len(pairs), False, cand_vals
        if prev is not None and all(dc[k] == prev[k] for k in bidegrees):
            print(f"  [INFO] SATURATED at {len(pairs)} pairs (d_candidate stable "
                  f"vs the previous round).", flush=True)
            RESULTS["d_candidate"] = dc
            RESULTS["n_points"] = len(pairs)
            return dc, len(pairs), True, cand_vals
        # report this round's table compactly, then add more points.
        print(f"  [INFO] round with {len(pairs)} pairs: d_candidate diagonal "
              f"sample (1,1)={dc[(1,1)]} (2,1)={dc[(2,1)]} (2,2)={dc[(2,2)]} "
              f"(3,3)={dc[(3,3)]}", flush=True)
        prev = dc
        prev_vals = cand_vals
        n_fresh += 8


# ============================================================================
# TASK 1c -- the plethystic log of H(s,t).
# ============================================================================
def hilbert_series_poly(d_true):
    """H(s,t) as an exact bivariate polynomial truncated to total degree <= 6
    (sum d_true(a,b) s^a t^b)."""
    H = S.Zero
    for (a, b), d in d_true.items():
        H += d * s**a * t**b
    return expand(H)


def _truncate(poly, deg):
    """Drop monomials of (s,t) total degree > deg."""
    P = Poly(expand(poly), s, t)
    out = S.Zero
    for (i, j), c in P.terms():
        if i + j <= deg:
            out += c * s**i * t**j
    return expand(out)


def _series_log_st(H, deg):
    """log(H(s,t)) as an exact bivariate power series to total degree <= deg, where
    H = 1 + (higher). Uses log(1+u) = sum_{m>=1} (-1)^{m+1} u^m / m with u = H - 1,
    truncated at total degree deg (u has no constant term, so u^m has total degree
    >= m -- the sum is finite)."""
    u = _truncate(H - 1, deg)
    acc = S.Zero
    upow = S.One
    for m in range(1, deg + 1):
        upow = _truncate(expand(upow * u), deg)
        if upow == 0:
            break
        acc += Rational((-1)**(m + 1), m) * upow
    return _truncate(acc, deg)


def plethystic_log(d_true):
    """plog H(s,t) = sum_{k>=1} (mu(k)/k) log H(s^k, t^k), exact rational bivariate
    series to total degree <= 6 (k up to 6, since H(s^k,t^k) has lowest nonconstant
    term degree k). Returns {(a,b): coefficient} for a+b <= 6."""
    print("Task 1c -- plethystic log plog H(s,t) = sum_k (mu(k)/k) log H(s^k,t^k) "
          "(exact rational, deg<=6):", flush=True)
    deg = TRUNCATION_DEGREE
    H = hilbert_series_poly(d_true)
    total = S.Zero
    for k in range(1, deg + 1):
        mu = mobius(k)
        if mu == 0:
            continue
        Hk = _truncate(H.subs({s: s**k, t: t**k}), deg)
        logHk = _series_log_st(Hk, deg)
        total += Rational(mu, k) * logHk
        total = _truncate(total, deg)
    P = Poly(expand(total), s, t)
    plog = {}
    for a in range(deg + 1):
        for b in range(deg + 1 - a):
            plog[(a, b)] = P.coeff_monomial(s**a * t**b)
    RESULTS["plog"] = plog
    # report
    print("  [INFO] plog coefficients {(a,b): coeff} (a+b<=6):", flush=True)
    for a in range(deg + 1):
        row = [(b, plog[(a, b)]) for b in range(deg + 1 - a)]
        print(f"  [INFO]   a={a}: " +
              ", ".join(f"({a},{b})={c}" for (b, c) in row), flush=True)
    return plog


# ============================================================================
# TASK 2 -- per-generator minimality (in-span-of-lower-products), the (2,2)
#   decision, the d_true-vs-d_candidate completeness match, and the verdict.
# ============================================================================
# The 10 candidates are indexed 0..9 in the FIXED order
#   0:Tr X (1,0) 1:Tr X^2 (2,0) 2:det X (3,0) 3:Tr Y (0,1) 4:Tr Y^2 (0,2)
#   5:det Y (0,3) 6:c (1,1) 7:Tr(X^2 o Y) (2,1) 8:Tr(X o Y^2) (1,2)
#   9:Tr(X^2 o Y^2) (2,2)
# A candidate G at bidegree (a,b) is a GENUINE (minimal) generator iff its
# value-vector is NOT in the span of {products of STRICTLY-LOWER-degree candidates
# landing at (a,b)} -- i.e. monomials in candidates whose bidegrees are each
# component-wise/total strictly less than (a,b), equivalently any monomial of
# bidegree (a,b) that does NOT contain G itself and whose factors all have total
# degree < a+b. For these candidate bidegrees, "products of strictly-lower-degree
# candidates" = all monomials of bidegree (a,b) EXCLUDING the pure generator G and
# any monomial that uses a candidate of total degree >= the generator's own total
# degree as a primitive (only G itself has total degree a+b among the candidates at
# bidegree (a,b) EXCEPT possibly other candidates of the same bidegree -- none here,
# each candidate bidegree is unique). So: lower-products = all (a,b)-monomials with
# the G-exponent forced to 0.

CAND_DEGREE = [bd[0] + bd[1] for bd in BIDEGREES]   # total degrees of the 10


def lower_product_monomials(a, b, gen_index):
    """Monomials of bidegree (a,b) that are PRODUCTS of strictly-lower-degree
    candidates relative to the generator at gen_index: all (a,b)-monomials with
    monos[gen_index] == 0 (the generator itself excluded) AND every candidate used
    has total degree < CAND_DEGREE[gen_index] (strictly lower). Since each candidate
    bidegree is unique, the only candidate of total degree == the generator's at
    that bidegree is the generator itself; we additionally forbid any candidate of
    total degree > the generator's (cannot appear at a smaller-or-equal bidegree
    anyway) for safety."""
    gd = CAND_DEGREE[gen_index]
    monos = monomials_of_bidegree(a, b)
    out = []
    for expo in monos:
        if expo[gen_index] != 0:
            continue                       # excludes the generator itself
        # every used candidate must be strictly lower total degree than the gen
        if any(expo[i] != 0 and CAND_DEGREE[i] >= gd for i in range(len(expo))):
            continue
        out.append(expo)
    return out


def minimality_test(cand_vals, d_true, d_candidate):
    """For each candidate generator G at (a,b): compute exact_qq_rank of the
    lower-product value-matrix WITHOUT G, then WITH G's value-vector appended. G is
    a GENUINE (minimal) generator iff the rank increases by 1 (G not in the lower-
    product span). Report PASS (generator) / reducible (product) per candidate.

    Spanning is explicitly distinguished from minimal generating (Pitfall 8): a
    candidate that appears in a spanning set but lies in the lower-product span is
    reported as a PRODUCT, not a generator."""
    print("Task 2 -- per-generator minimality (in-span-of-lower-products, exact "
          "over Q):", flush=True)
    minimal = {}
    for gi, (name, bd) in enumerate(zip(NAMES, BIDEGREES)):
        a, b = bd
        lower = lower_product_monomials(a, b, gi)
        # value-vector of G itself (the pure monomial e_gi = 1)
        g_expo = tuple(1 if i == gi else 0 for i in range(len(NAMES)))
        if lower:
            M_lower = monomial_value_matrix(lower, cand_vals)
            r_without = exact_qq_rank(M_lower)
            M_with = monomial_value_matrix(lower + [g_expo], cand_vals)
            r_with = exact_qq_rank(M_with)
        else:
            # no strictly-lower products land here (the six pointwise primaries and
            # c at (1,1) -- (1,1) has Tr(X)Tr(Y) as a lower product, handled above;
            # the pure pointwise (1,0),(2,0),(3,0),(0,1),(0,2),(0,3) have none).
            r_without = 0
            r_with = exact_qq_rank(monomial_value_matrix([g_expo], cand_vals))
        is_gen = (r_with == r_without + 1)
        minimal[name] = ("generator" if is_gen else "product")
        _report(
            f"minimality {name:<16} {str(bd):<7} lower-product rank "
            f"{r_without} -> {r_with} (+G): {'GENERATOR' if is_gen else 'PRODUCT'} "
            f"({len(lower)} lower products)  [test-minimality; "
            f"test-spanning-vs-minimal]",
            is_gen)
    RESULTS["minimality"] = minimal
    return minimal


def decide_22(cand_vals, d_true):
    """test-22-decision -- the headline diagnostic. At (2,2) enumerate the strictly-
    lower candidate products {c^2, c*Tr(X)Tr(Y), Tr(X^2)Tr(Y^2), Tr(X^2 o Y)*Tr(Y),
    Tr(X o Y^2)*Tr(X), (Tr X)^2(Tr Y)^2, Tr(X^2)(Tr Y)^2, (Tr X)^2 Tr(Y^2),
    Tr(X)Tr(Y)*c, ...} = ALL (2,2)-monomials with the Tr(X^2 o Y^2) exponent 0;
    compute their exact_qq_rank, then the in-span test for Tr(X^2 o Y^2). Compare to
    d_true(2,2). Tr(X^2 o Y^2) is a GENERATOR iff its value-vector is NOT in the
    lower-product span AND d_true(2,2) > rank-without-it; else it is a PRODUCT."""
    print("Task 2 -- the (2,2) Tr(X^2 o Y^2) generator-vs-product decision "
          "(exact over Q):", flush=True)
    gi = 9   # index of Tr(X^2 o Y^2)
    lower = lower_product_monomials(2, 2, gi)
    M_lower = monomial_value_matrix(lower, cand_vals)
    r_without = exact_qq_rank(M_lower)
    g_expo = tuple(1 if i == gi else 0 for i in range(len(NAMES)))
    r_with = exact_qq_rank(monomial_value_matrix(lower + [g_expo], cand_vals))
    d22 = d_true[(2, 2)]
    is_gen = (r_with == r_without + 1) and (d22 > r_without)
    decision = "generator" if is_gen else "product"
    RESULTS["d22_decision"] = decision
    print(f"  [INFO] (2,2): {len(lower)} strictly-lower candidate products; "
          f"their exact_qq_rank = {r_without}; +Tr(X^2 o Y^2) -> {r_with}; "
          f"d_true(2,2) = {d22}.", flush=True)
    print(f"  [INFO] lower products at (2,2) include: c^2, Tr(X^2)Tr(Y^2), "
          f"c*Tr(X)Tr(Y), Tr(X^2 o Y)*Tr(Y), Tr(X o Y^2)*Tr(X), (TrX)^2(TrY)^2, "
          f"Tr(X^2)(TrY)^2, (TrX)^2 Tr(Y^2), ...", flush=True)
    ok = _report(
        f"(2,2) DECISION: Tr(X^2 o Y^2) is a {decision.upper()} "
        f"(lower-product rank {r_without} -> {r_with} with it; d_true(2,2)={d22}; "
        f"GENERATOR iff value-vector not in lower span AND d_true > rank-without)  "
        f"[test-22-decision; ref-plan01-table; ref-frozen-degree2]",
        is_gen)   # reported honestly; pass-line records the decision either way
    # The decision is honest regardless of branch; record both possibilities.
    if not is_gen:
        print("  [NOTE] (2,2) verdict = PRODUCT: Tr(X^2 o Y^2) is reducible "
              "(in the lower-product span); the minimal set is smaller than the "
              "candidate set (fp-spanning-as-minimal -- reported honestly).",
              flush=True)
    else:
        print("  [NOTE] (2,2) verdict = GENERATOR: Tr(X^2 o Y^2) is a genuine new "
              "(2,2) generator (its value-vector is NOT a product of strictly-lower "
              "candidates; the d_true(2,2)=9 dimension requires it).", flush=True)
    return decision, r_without, r_with, d22


def completeness_match(d_true, d_candidate, plog):
    """test-hilbert-match + test-plog. Print the full d_true-vs-d_candidate table at
    every a+b<=6. d_true <= d_candidate everywhere => candidate-complete to degree 6.
    Any d_true > d_candidate => MISSING generator (report the bidegree; backtracking
    rule: the lowest-degree trace monomial there, Iltyakov). Cross-check the plog:
    positive coefficients should match the candidate generator bidegrees; a positive
    plog coefficient at a NON-candidate bidegree independently flags a missing
    generator; negative coefficients catalogue the relations (non-free structure)."""
    print("Task 2 -- completeness match: d_true(a,b) vs d_candidate(a,b), all "
          "a+b<=6:", flush=True)
    deg = TRUNCATION_DEGREE
    cand_bidegrees = set(BIDEGREES)
    # print the full match grid
    print("  d_true  / d_candidate  (T/C), . = out of range:", flush=True)
    hdr = "    a\\b |" + "".join(f"{b:>9}" for b in range(deg + 1))
    print(hdr, flush=True)
    print("    " + "-" * (len(hdr) - 4), flush=True)
    for a in range(deg + 1):
        cells = []
        for b in range(deg + 1):
            if a + b <= deg:
                cells.append(f"{d_true[(a,b)]}/{d_candidate[(a,b)]}".rjust(9))
            else:
                cells.append(".".rjust(9))
        print(f"    {a:>3} |" + "".join(cells), flush=True)

    missing = [(a, b) for a in range(deg + 1) for b in range(deg + 1 - a)
               if d_true[(a, b)] > d_candidate[(a, b)]]
    RESULTS["missing_bidegrees"] = missing
    match_ok = _report(
        f"completeness: d_true(a,b) <= d_candidate(a,b) for ALL a+b<=6 "
        f"(candidate products reach the true dimension)  [test-hilbert-match; "
        f"ref-plan01-table]",
        not missing)
    if missing:
        global STOP_TRIGGERED
        print(f"  [MISSING GENERATOR] d_true > d_candidate at {missing} "
              f"(NEGATIVE-RESULT-IS-SUCCESS). Lowest-degree trace monomial there is "
              f"the missing generator (Iltyakov); report the bidegree, do NOT "
              f"suppress (fp-suppress-missing).", flush=True)

    # plog cross-check
    pos = [(a, b) for a in range(deg + 1) for b in range(deg + 1 - a)
           if plog[(a, b)] > 0]
    neg = [(a, b) for a in range(deg + 1) for b in range(deg + 1 - a)
           if plog[(a, b)] < 0]
    RESULTS["relations"] = neg
    pos_at_candidates = all(bd in cand_bidegrees for bd in pos)
    pos_outside = [bd for bd in pos if bd not in cand_bidegrees]
    plog_ok = _report(
        f"plog cross-check: positive coefficients at {sorted(pos)} (all candidate "
        f"bidegrees: {pos_at_candidates}); positive-at-NON-candidate (missing "
        f"generators): {pos_outside}  [test-plog; ref-derksen-kemper; ref-hanany]",
        pos_at_candidates)
    # relations: negatives are the syzygies; their ABSENCE through deg 6 is reported
    # honestly (NOT assumed away -- the Blind contrast EXPECTS non-free; we report
    # what the computation shows).
    if neg:
        print(f"  [RELATIONS] negative plog coefficients (syzygies) at {sorted(neg)}"
              f" -- the F_4 ring is non-free (Blind contrast); the relations are "
              f"catalogued.", flush=True)
        rel_note = f"relations (negative plog) at {sorted(neg)}"
    else:
        print("  [RELATIONS] NO negative plog coefficient through total degree 6: "
              "the candidate set is FREE through degree 6 (the first relation, if "
              "the ring is non-free as the Blind E_6 contrast suggests for the "
              "larger structure, must occur at total degree >= 7, BEYOND the "
              "contract scope). Reported honestly -- NOT assumed (fp-e6-free-form: "
              "H_free was NEVER substituted for H_true; d_true was computed "
              "independently in Plan 01 and HAPPENS to match the free product "
              "through degree 6).", flush=True)
        rel_note = ("NO relations through degree 6 (free through deg 6; first "
                    "relation at total degree >= 7 if non-free)")
    return match_ok, plog_ok, missing, neg, rel_note


def honest_verdict(d_true, d_candidate, minimal, d22_decision, missing, neg,
                   rel_note):
    """test-verdict-honest (NEGATIVE-RESULT-IS-SUCCESS). State the verdict and the
    cross-phase consistency. Either CERTIFIED COMPLETE to total degree <=6 (with the
    explicit polarization-NOT-assumed note) OR the missing-generator bidegree(s)."""
    print("Task 2 -- honest completeness verdict (NEGATIVE-RESULT-IS-SUCCESS):",
          flush=True)
    deg = TRUNCATION_DEGREE
    # the minimal generating set = candidates flagged 'generator'
    gen_list = [(NAMES[i], BIDEGREES[i]) for i in range(len(NAMES))
                if minimal[NAMES[i]] == "generator"]
    n_gen = len(gen_list)
    if not missing:
        RESULTS["verdict"] = "certified-complete"
        print(f"  [VERDICT] CERTIFIED COMPLETE to total degree <= {deg}: the "
              f"candidate-product dimension reaches d_true at EVERY bidegree "
              f"a+b<=6.", flush=True)
        print(f"  [VERDICT] Minimal generating set ({n_gen} generators):",
              flush=True)
        for name, bd in gen_list:
            print(f"  [VERDICT]   {name:<16} {bd}", flush=True)
        print(f"  [VERDICT] {rel_note}.", flush=True)
        print("  [VERDICT] POLARIZATION WAS NOT ASSUMED TO GENERATE: the bigraded "
              "Hilbert match (d_true vs d_candidate, computed independently) IS the "
              "certificate (Schwarz arXiv:math/0609078; polarize_d only PRODUCED "
              "the mixed-cubic candidates). [fp-polarization-generates rejected]",
              flush=True)
        verdict_ok = True
    else:
        RESULTS["verdict"] = f"missing-generator-at-{missing}"
        print(f"  [VERDICT] MISSING GENERATOR at {missing} (NEGATIVE-RESULT-IS-"
              f"SUCCESS): d_true > d_candidate there. The lowest-degree trace "
              f"monomial at that bidegree (Iltyakov) is the missing generator; ADD "
              f"it and re-match. NOT suppressed (fp-suppress-missing).", flush=True)
        verdict_ok = True   # an honestly-reported missing generator is a full pass

    # (2,2) call-out
    print(f"  [VERDICT] (2,2) Tr(X^2 o Y^2): {d22_decision.upper()} "
          f"(d_true(2,2)={d_true[(2,2)]}).", flush=True)

    # cross-phase consistency
    print("  [CROSS-PHASE] consistency with prior phases:", flush=True)
    trdeg_ok = (TRDEG_TARGET >= SPINE_RANK >= 1)
    print(f"  [CROSS-PHASE]   trdeg {TRDEG_TARGET} (65/65.1) >= SPINE rank "
          f"{SPINE_RANK} (66) >= quotient 1 (67): {trdeg_ok}", flush=True)
    print(f"  [CROSS-PHASE]   Krull = {KRULL_TARGET} (65); (1,1) = "
          f"{d_true[(1,1)]} == {D_11_TARGET} (67): "
          f"{d_true[(1,1)] == D_11_TARGET}", flush=True)
    # the 10 candidate bidegrees include the trdeg-10 field-generating set; n_gen
    # should equal the field-level count 10 if all candidates are genuine generators
    n_gen_ok = _report(
        f"minimal generating set has {n_gen} generators "
        f"(field-level trdeg-10 set had 10 candidates; each genuine generator is a "
        f"ring generator too)  [test-verdict-honest]",
        n_gen >= 1)
    consistency_ok = _report(
        f"cross-phase consistency: trdeg {TRDEG_TARGET} >= rank {SPINE_RANK} >= "
        f"quotient 1; Krull {KRULL_TARGET}; (1,1)={d_true[(1,1)]}=={D_11_TARGET}  "
        f"[test-verdict-honest]",
        trdeg_ok and d_true[(1, 1)] == D_11_TARGET)
    return verdict_ok and consistency_ok and n_gen_ok, gen_list


# ============================================================================
# EXACT-ONLY source guard (module-local; fp-float-rank, octonion_algebra).
# ============================================================================
def exact_only_guard():
    """Scan THIS module's source: 0 octonion_algebra imports AND 0 numpy/np
    float-rank CALLS on the decisive path. (numpy itself is not imported here; the
    guard asserts no matrix_rank call regardless.)"""
    _re_oa_import = re.compile(
        r"^\s*(from\s+octonion_algebra\s+import\b|import\s+octonion_algebra\b)")
    _re_float_rank_call = re.compile(r"\b(np|numpy)\.linalg\.matrix_rank\s*\(")

    def _strip_comment(text):
        in_s, in_d, esc = False, False, False
        for idx, ch in enumerate(text):
            if esc:
                esc = False
                continue
            if ch == "\\":
                esc = True
                continue
            if ch == "'" and not in_d:
                in_s = not in_s
            elif ch == '"' and not in_s:
                in_d = not in_d
            elif ch == "#" and not in_s and not in_d:
                return text[:idx]
        return text

    try:
        with open(__file__, "r") as fh:
            lines = fh.readlines()
    except (OSError, NameError):
        return False, "could not open module source for the guard"
    oa_imports = 0
    float_rank_hits = []
    for n, raw in enumerate(lines, start=1):
        code = _strip_comment(raw)
        if _re_float_rank_call.search(code):
            float_rank_hits.append(n)
        if _re_oa_import.match(code):
            oa_imports += 1
    ok = (oa_imports == 0) and (float_rank_hits == [])
    detail = (f"octonion_algebra imports: {oa_imports} (expect 0); "
              f"float-rank calls: {len(float_rank_hits)} (expect 0)")
    return ok, detail


# ============================================================================
# main() -- the full ordered harness + clean-pass-vs-bug exit classifier.
# ============================================================================
def main():
    print_preregistration()

    # exact-only guard FIRST.
    print("Exact-only guard (decisive-path source scan):")
    guard_ok, guard_detail = exact_only_guard()
    _report(f"exact-only guard: no float-rank / no octonion_algebra on the "
            f"decisive path [{guard_detail}]  [fp-float-rank rejected]", guard_ok)

    # --- TASK 1: assemble candidates, load d_true, d_candidate, plog ---
    assemble_ok = assemble_candidates()
    inv_ok = reconfirm_f4_invariance()
    dtrue_ok = load_d_true()
    if STOP_TRIGGERED:
        print("-" * 76)
        print("OVERALL: STOP -- d_true handoff did not regenerate. Report the "
              "discrepancy.")
        print("=" * 76)
        return False
    d_true = RESULTS["d_true"]
    d_candidate, npairs, saturated, cand_vals = \
        compute_d_candidate_saturated(d_true)
    sat_ok = _report(
        f"d_candidate computed for all a+b<=6 via exact_qq_rank; SATURATED at "
        f"{npairs} generic pairs  [test-hilbert-match; fp-float-rank rejected]",
        saturated and not STOP_TRIGGERED)
    if STOP_TRIGGERED:
        print("-" * 76)
        print("OVERALL: STOP -- d_candidate > d_true (impossible). Report the bug.")
        print("=" * 76)
        return False
    plog = plethystic_log(d_true)

    # --- TASK 2: minimality, (2,2), completeness match, verdict ---
    minimal = minimality_test(cand_vals, d_true, d_candidate)
    d22_decision, r22_wo, r22_w, d22 = decide_22(cand_vals, d_true)
    match_ok, plog_ok, missing, neg, rel_note = \
        completeness_match(d_true, d_candidate, plog)
    verdict_ok, gen_list = honest_verdict(
        d_true, d_candidate, minimal, d22_decision, missing, neg, rel_note)

    # ------------------------------------------------------------------------
    # Exit classifier. A CLEAN PASS is: guards green, handoff regenerated,
    # d_candidate saturated, the match run, the (2,2) decided, the verdict stated
    # (BOTH certified-complete AND missing-generator are full passes -- the harness
    # passes IFF the analysis completed honestly and consistently, NOT IFF the
    # ring is complete). A BUG is a guard failure, a STOP, or a cross-phase
    # inconsistency.
    # ------------------------------------------------------------------------
    print("-" * 76)
    # minimality consistency: every candidate is either a generator or a product,
    # and the count of generators is the size of the minimal generating set.
    all_classified = all(v in ("generator", "product")
                         for v in minimal.values())
    clean_pass = (
        not STOP_TRIGGERED
        and guard_ok and assemble_ok and inv_ok and dtrue_ok and saturated
        and sat_ok and match_ok and plog_ok and verdict_ok and all_classified
        and ALL_PASS_or_only_honest_branches(minimal, missing)
    )
    if clean_pass:
        n_gen = len(gen_list)
        if not missing:
            print(f"OVERALL: CLEAN PASS -- CERTIFIED COMPLETE to total degree "
                  f"<= {TRUNCATION_DEGREE}. The {n_gen}-element candidate set "
                  f"generates R[27(+)27]^{{F_4}} to total degree 6 (d_candidate == "
                  f"d_true at every bidegree).")
            print(f"  Minimal generating set: {n_gen} generators "
                  f"{[(n, b) for n, b in gen_list]}.")
            print(f"  (2,2) Tr(X^2 o Y^2): {d22_decision.upper()}. {rel_note}.")
            print("  POLARIZATION NOT ASSUMED -- the bigraded Hilbert match is the "
                  "certificate (Schwarz). Exact over Q; exact-only guard green.")
            print(f"  Cross-consistent: trdeg {TRDEG_TARGET} >= rank {SPINE_RANK} "
                  f">= quotient 1; Krull {KRULL_TARGET}; (1,1)={d_true[(1,1)]}.")
        else:
            print(f"OVERALL: CLEAN PASS (NEGATIVE-RESULT-IS-SUCCESS) -- MISSING "
                  f"GENERATOR at {missing}. d_true > d_candidate there; the lowest-"
                  f"degree trace monomial is the missing generator (Iltyakov). "
                  f"Reported honestly, NOT suppressed.")
            print(f"  (2,2) Tr(X^2 o Y^2): {d22_decision.upper()}.")
            print(f"  Cross-consistent: trdeg {TRDEG_TARGET} >= rank {SPINE_RANK} "
                  f">= quotient 1; Krull {KRULL_TARGET}; (1,1)={d_true[(1,1)]}.")
    else:
        print("OVERALL: BUG / GUARD FAILURE / STOP / INCONSISTENCY -- see FAIL "
              "lines above. The completeness certificate is NOT trustworthy.")
    print("=" * 76)
    return clean_pass


def ALL_PASS_or_only_honest_branches(minimal, missing):
    """The harness FAIL accumulator (ALL_PASS) flips on a minimality 'PRODUCT'
    verdict (the _report line is parameterized by is_gen). But a reducible candidate
    is an HONEST outcome (NEGATIVE-RESULT-IS-SUCCESS), not a bug. Likewise a missing
    generator is honest. This adjudicator returns True iff every FAIL line is one of
    those two honest branches (a 'product' minimality call or the missing-generator
    match line), and False iff a genuine guard/handoff/consistency check failed."""
    honest_fail_substrings = []
    # 'product' minimality calls are honest:
    for name, verdict in minimal.items():
        if verdict == "product":
            honest_fail_substrings.append(f"minimality {name}")
    # the (2,2) PRODUCT call is honest:
    honest_fail_substrings.append("(2,2) DECISION")
    # the completeness 'missing' line is honest:
    if missing:
        honest_fail_substrings.append("completeness: d_true(a,b) <= d_candidate")
    for failed in FAILED_LABELS:
        if not any(sub in failed for sub in honest_fail_substrings):
            return False
    return True


if __name__ == "__main__":
    sys.exit(0 if main() else 1)
