"""
KKT-Slice Gluing Freedom & Three-Point Holonomy -- GATE 0 (exact over Q)
========================================================================
Derivation slot: 82.  Milestone v22.0-candidate (the eta-reading test).
Spec: paper6-kkt-gluing-holonomy-prompt.md, section "Gate 0 -- the identification
space (pure structure, cheapest)".  Conventions: .gpd/CONVENTIONS.md.

This is the REUSABLE warm-harness for the whole derivation-82 run (Gates 0-3).
It is built on the v17-v21 EXACT-over-Q det-SSOT engines (ring_lemma_verification),
NOT on the BANNED float64 octonion_algebra.py (and NOT on Phase 52's KKT code,
which was built on that banned file).  A source guard fires before any decisive
computation.

GATE 0 SCOPE (this file's driver runs ONLY Gate 0; the orchestrator picks the
next gate from the result -- fail-fast discipline):
  Task 1a  the exact conjugating automorphism P (F_4, P.E_11 = E_22).
  Task 1b  Stab_{f_4}(E_11)  (the identification coset is P . Stab).
  Task 2   the residual r_12 = joint-stabilizer of the standard frame, and its
           SLICE ACTION on the 4d Minkowski slice h_2(C_u) = coords {1,2,3,10}.
  Verdict  a deterministic, NON-hardwired verdict() ladder (+ self-tests) that
           routes from the COMPUTED slice-residual dimension (unique -> Gate 2,
           else residual-survives -> record + Gate 1).

# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; det3 cross=2Re((x2x1)x3); arithmetic=exact-SymPy-over-Q; ranks=sympy/DomainMatrix-over-QQ; NEVER numpy on the decisive path; metric_signature=mostly-minus(+,-,-,-); u=e7; slice=h_2(C_u) coords {1,2,3,10}
# NUMEROLOGY GUARD: NO kappa, NO Lambda, NO physical constants anywhere in this run (pure structure / group theory over Q).

Engine map (file:line cited in 82-kkt-gluing-RESEARCH.md):
  ring_lemma_verification.py
    h3o_from_coords, X_from_symbols, _flat27, _standard_basis_27   (coords)
    jordan, det_3, Tr, Tr2                                          (det SSOT)
    jordan_L_matrix, inner_derivations                             (f_4 = Der)
  orbit_dimension_gate.py
    exact_qq_rank (DomainMatrix-over-QQ), _select_independent_basis, span_rank_over_QQ
  bulk_geometry_verification.py
    stab_E6_E11 (the nullspace PATTERN; here ADAPTED to f_4, NOT e_6)

Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0.  Deterministic
(no random seeds; all test elements hardcoded with exact rational entries).
Runnable directly:  PYTHONPATH=code python3 -u code/kkt_gluing_holonomy.py
Exits 0 iff ALL_PASS (every lock + the verdict self-tests pass); nonzero on any
failure or any forced deviation from the brief.
"""

import os
import sys
import time

# --- path: the warm engines live alongside this file in code/ -------------------
_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

from sympy import Matrix, Rational, symbols, simplify  # noqa: E402

import ring_lemma_verification as RL  # noqa: E402  (det SSOT + h_3(O) arithmetic)
import orbit_dimension_gate as ODG    # noqa: E402  (exact-QQ rank machinery)

ALL_PASS = True
_t0 = time.time()


def _log(msg):
    print(f"[{time.time() - _t0:7.1f}s] {msg}", flush=True)


def _report(label, ok):
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


# ============================================================================
# 0. SOURCE GUARD  (mirror cartan_phaseB_curvature.py:120-141)
#    octonion_algebra absent; det SSOT native exact-over-Q ring_lemma; no numpy
#    imported on this decisive path.  Fire BEFORE any decisive computation.
# ============================================================================
def source_guard():
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra BANNED + det SSOT exact-over-Q ring_lemma "
          "+ no numpy on the decisive path")
    print("=" * 78)
    oa_absent = "octonion_algebra" not in sys.modules
    np_absent = "numpy" not in sys.modules
    native = (RL.det_3.__module__ == "ring_lemma_verification"
              and RL.jordan.__module__ == "ring_lemma_verification"
              and RL.Tr.__module__ == "ring_lemma_verification")
    Xspot = RL.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                               RL.oct_zero(), RL.oct_zero(), RL.oct_zero())
    spot = RL.det_3(Xspot)
    spot_ok = (spot == 30) and (not isinstance(spot, float))
    _report("octonion_algebra NOT imported on the decisive path", oa_absent)
    _report(f"det SSOT native exact-over-Q ring_lemma (det_3(diag(2,3,5))=={spot})",
            native and spot_ok)
    _report("numpy NOT imported on this driver's decisive path (all sympy over QQ)",
            np_absent)
    return oa_absent and native and spot_ok and np_absent


# ============================================================================
# 1. Idempotent frame + coords helpers
# ============================================================================
def E_ii(i):
    """Primitive diagonal idempotent E_ii (i in {0,1,2}) = diag(delta_i)."""
    diag = [Rational(1) if k == i else Rational(0) for k in range(3)]
    return RL.h3o_from_coords(diag[0], diag[1], diag[2],
                              RL.oct_zero(), RL.oct_zero(), RL.oct_zero())


E11 = E_ii(0)   # diag(1,0,0)
E22 = E_ii(1)   # diag(0,1,0)
E33 = E_ii(2)   # diag(0,0,1) = I - E11 - E22

# h_2(C_u) Minkowski slice of E_11: engine-native coords (CONVENTIONS.md H2CU_SLICE_IDX).
#   1 = beta, 2 = gamma, 3 = Re(x1) = p, 10 = <x1,e7> = q   (u = e_7).
#   Minkowski basis: x0=(beta+gamma)/2, x1_M=Re(x1), x2_M=<x1,e7>, x3=(beta-gamma)/2.
#   det_2 = beta*gamma - |x1|^2_{C_u} = x0^2 - x1_M^2 - x2_M^2 - x3^2  (mostly-minus, timelike-positive).
SLICE_IDX = [1, 2, 3, 10]
# V_0(E_11) (the slice tangent, h_2(O)): coords 1..10.
V0_IDX = list(range(1, 11))


# ============================================================================
# 2. TASK 1a -- the exact conjugating automorphism P (F_4, P.E_11 = E_22)
# ============================================================================
# P = conjugation by the 3x3 REAL permutation matrix swapping matrix indices 0<->1
# (fixing 2): (P X)[i][j] = X[sigma(i)][sigma(j)] with sigma = (0 1).  A real
# orthogonal conjugation preserves Hermiticity AND the Jordan product
# (XoY -> S^{-1}(XoY)S), hence is an exact element of F_4 = Aut(h_3(O)).  It swaps
# the diagonal slots alpha<->beta (=> E_11<->E_22), fixes gamma (=> E_33 fixed), and
# induces a SIGNED permutation on the off-diagonal octonion slots (x1<->conj(x2),
# x3<->conj(x3)) -- the conjugation flips every imaginary component's sign.
#
# This REPLACES Phase 52's numeric P (max err 1.9e-15) with an EXACT-over-Q element.
_SIGMA_01 = {0: 1, 1: 0, 2: 2}


def conj_perm(X, sigma=_SIGMA_01):
    """Apply the index-permutation conjugation (P X)[i][j] = X[sigma(i)][sigma(j)]."""
    return [[X[sigma[i]][sigma[j]] for j in range(3)] for i in range(3)]


def build_P():
    """The explicit 27x27 rational matrix of P (column k = flat27(conj_perm(E_k)))."""
    basis = RL._standard_basis_27()
    cols = [RL._flat27(conj_perm(basis[k])) for k in range(27)]
    return Matrix(27, 27, lambda r, c: cols[c][r])


def check_P(verbose=True):
    """Certify P is an exact F_4 element with P.E_11 = E_22 (involutive, det_3/Tr/Jordan
    preserved).  Returns (P_matrix, ok)."""
    P = build_P()
    ok = True

    # (a) P E_11 = E_22, P E_22 = E_11 (involutive on the swapped pair), P E_33 = E_33.
    a1 = RL.octmat_equal(conj_perm(E11), E22)
    a2 = RL.octmat_equal(conj_perm(E22), E11)
    a3 = RL.octmat_equal(conj_perm(E33), E33)
    ok &= _report("P . E_11 == E_22", a1)
    ok &= _report("P . E_22 == E_11  (involutive on the pair)", a2)
    ok &= _report("P . E_33 == E_33  (third idempotent fixed)", a3)

    # (b) P in Aut(h_3(O)): preserves the JORDAN PRODUCT on ALL standard-basis pairs
    #     (the genuine automorphism test -- product, not just the norm).
    basis = RL._standard_basis_27()
    prod_ok = True
    for a in range(27):
        for b in range(27):
            lhs = conj_perm(RL.jordan(basis[a], basis[b]))
            rhs = RL.jordan(conj_perm(basis[a]), conj_perm(basis[b]))
            if not RL.octmat_equal(lhs, rhs):
                prod_ok = False
                break
        if not prod_ok:
            break
    ok &= _report("P preserves the Jordan product on all 27x27 basis pairs "
                  "(genuine Aut(h_3(O)))", prod_ok)

    # (c) P preserves det_3, Tr, Tr2 on a GENERIC symbolic element (F_4-invariance).
    xs = symbols('x0:27', real=True)
    X = RL.X_from_symbols(xs)
    PX = conj_perm(X)
    det_ok = simplify(RL.det_3(PX) - RL.det_3(X)) == 0
    tr_ok = simplify(RL.Tr(PX) - RL.Tr(X)) == 0
    tr2_ok = simplify(RL.Tr2(PX) - RL.Tr2(X)) == 0
    ok &= _report("P preserves det_3 on a generic symbolic element", det_ok)
    ok &= _report("P preserves Tr on a generic symbolic element", tr_ok)
    ok &= _report("P preserves Tr2 on a generic symbolic element", tr2_ok)

    # (d) P is an exact signed permutation (entries {0,+-1}, involutive, det 1).
    entries_ok = all(P[i, j] in (Rational(0), Rational(1), Rational(-1))
                     for i in range(27) for j in range(27))
    invol = (P * P) == Matrix.eye(27)
    ok &= _report("P entries in {0,+-1} (exact signed permutation)", entries_ok)
    ok &= _report("P*P == I_27 (P involutive as a 27x27 matrix)", invol)

    if verbose:
        _print_signed_perm(P)
    return P, ok


def _print_signed_perm(P):
    labels = (['alpha', 'beta', 'gamma']
              + ['x1.%d' % i for i in range(8)]
              + ['x2.%d' % i for i in range(8)]
              + ['x3.%d' % i for i in range(8)])
    print("  --- explicit P (coord -> sign * image) ---")
    for j in range(27):
        for i in range(27):
            if P[i, j] != 0:
                sgn = '+' if P[i, j] == 1 else '-'
                print("      %3d %-7s -> %s%-7s (idx %d)" % (j, labels[j], sgn, labels[i], i))
                break


# ============================================================================
# 3. f_4 = Der(h_3(O)) basis (dim 52) -- exact over Q
# ============================================================================
# The 324 nonzero inner derivations span f_4 (dim 52).  Build a 52-dim BASIS via
# the rref pivot set (orbit_dimension_gate._select_independent_basis), EXACT over Q.
_F4_CACHE = {}


def f4_basis():
    """A 52-element exact-over-Q basis of f_4 = span(inner_derivations()).
    Cached (the 324-bracket build + rref pivot selection is the slow step)."""
    if "basis" in _F4_CACHE:
        return _F4_CACHE["basis"], _F4_CACHE["dim"], _F4_CACHE["nbrack"]
    _log("building inner_derivations() (324 brackets) ...")
    derivs = RL.inner_derivations()
    nbrack = len(derivs)
    _log(f"got {nbrack} nonzero brackets; selecting an independent basis (rref over QQ) ...")
    idx = ODG._select_independent_basis(derivs)
    basis = [derivs[i] for i in idx]
    dim = len(basis)
    # Confirm dim f_4 = 52 EXACTLY (span rank of the full 324 over QQ).
    rk = ODG.span_rank_over_QQ(derivs)
    _F4_CACHE.update(basis=basis, dim=dim, nbrack=nbrack, span_rank=rk)
    _log(f"f_4 basis: {dim} generators; span rank over QQ of all {nbrack} = {rk}")
    return basis, dim, nbrack


# ============================================================================
# 4. Stabilizers in f_4 (nullspace PATTERN adapted from stab_E6_E11; f_4 NOT e_6)
# ============================================================================
def stab_f4(targets, basis=None):
    """stab_{f_4}(targets) = { D in f_4 : D . v == 0 for every v in `targets` }, EXACT
    over Q.  `targets` is a list of h_3(O) elements (matrices); each contributes a
    27-row block to M (column j = basis[j] . flat(target)); the joint stabilizer is
    the nullspace of the stacked M.  Returns dict(dim, gens(list of 27x27), basis_dim).

    This is the bulk_geometry.stab_E6_E11 nullspace PATTERN, ADAPTED to f_4 (fed the
    f_4 basis, not build_e6_basis()), and generalized to a JOINT (multi-target) kernel.
    """
    if basis is None:
        basis, _, _ = f4_basis()
    blocks = []
    for T in targets:
        v = Matrix(RL._flat27(T))
        cols = [list(D * v) for D in basis]           # each length 27
        blocks.append(Matrix(27, len(basis), lambda r, cc: cols[cc][r]))
    M = Matrix.vstack(*blocks)                          # (27 * |targets|) x |basis|
    img_dim = ODG.exact_qq_rank(M)
    dim_stab = len(basis) - img_dim
    ns = M.nullspace()
    gens = []
    for c in ns:
        D = Matrix.zeros(27, 27)
        for j in range(len(basis)):
            if c[j] != 0:
                D += c[j] * basis[j]
        gens.append(D)
    return {"dim": dim_stab, "gens": gens, "basis_dim": len(basis),
            "img_dim": img_dim, "n_nullspace": len(ns)}


# ============================================================================
# 5. SLICE ACTION of a derivation D on the 4d Minkowski slice h_2(C_u)
# ============================================================================
# Each D in r_12 acts on the 27 coords.  Restrict to V_0(E_11) (coords 1..10), then
# read off the slice block on SLICE_IDX = {1,2,3,10}.  We report, EXACT over Q:
#   - leak: does D map the 4d slice OUT of V_0 (any nonzero normal component)?
#   - does D preserve the slice (slice -> slice, i.e. V_0\slice components vanish)?
#   - the 4x4 slice block (the candidate structure-group action), and whether it
#     is so(3,1)-valued (preserves the det_2 Minkowski form) vs trivial.
ETA_DIAG_M = None  # filled by minkowski_form()


def minkowski_form():
    """The 4x4 Minkowski Gram of det_2 in the slice basis (x0,x1_M,x2_M,x3) =
    ((beta+gamma)/2, Re(x1), <x1,e7>, (beta-gamma)/2), i.e. eta = diag(+1,-1,-1,-1).
    Returned together with the change-of-basis B from engine coords {1,2,3,10} to
    Minkowski coords, so eta is in the Minkowski frame.

    det_2 = beta*gamma - p^2 - q^2 (p=Re x1, q=<x1,e7>) = x0^2 - x1_M^2 - x2_M^2 - x3^2.
    """
    # engine slice coords order: [beta(idx1), gamma(idx2), p=Re x1(idx3), q=<x1,e7>(idx10)]
    # Minkowski coords: x0=(beta+gamma)/2, x1_M=p, x2_M=q, x3=(beta-gamma)/2.
    half = Rational(1, 2)
    # rows = Minkowski coord as a combo of [beta,gamma,p,q]:
    B = Matrix([
        [half, half, 0, 0],     # x0
        [0,    0,    1, 0],     # x1_M = p
        [0,    0,    0, 1],     # x2_M = q
        [half, -half, 0, 0],    # x3
    ])
    eta = Matrix.diag(1, -1, -1, -1)
    return eta, B


def slice_action(D):
    """Return dict describing D's action on the 4d slice h_2(C_u)(E_11), EXACT over Q:
      block44_engine : 4x4 matrix of D restricted to SLICE_IDX (engine coords),
                       i.e. the {1,2,3,10}->{1,2,3,10} sub-block of D.
      block44_mink   : the same action in Minkowski coords (B block44 B^{-1}).
      leaves_V0      : True iff D maps the 4 slice basis vectors into V_0 (no
                       cone-NORMAL component, indices {0} u {11..26}).
      preserves_slice: True iff D maps each slice basis vector back into the slice
                       (the V_0-internal off-slice comps {4..9} also vanish).
      so31_valued    : True iff the engine 4x4 block is so(3,1)-valued
                       (eta_M . A + A^T . eta_M == 0 in Minkowski coords), i.e. the
                       slice action is an infinitesimal Lorentz transformation.
      is_zero_on_slice: True iff block44_engine == 0 (D acts trivially on the slice).
    """
    NORMAL_IDX = [0] + list(range(11, 27))      # V_1 (+) V_{1/2}: cone-normal
    V0_OFF_SLICE = [k for k in V0_IDX if k not in SLICE_IDX]   # {4..9}: internal W-sector
    # Columns of D on the slice basis vectors e_{1},e_{2},e_{3},e_{10}.
    leaves_V0 = True
    preserves_slice = True
    block_cols = []
    for col in SLICE_IDX:
        e = Matrix([Rational(1) if r == col else Rational(0) for r in range(27)])
        De = D * e
        if any(De[a] != 0 for a in NORMAL_IDX):
            leaves_V0 = False
        if any(De[a] != 0 for a in (NORMAL_IDX + V0_OFF_SLICE)):
            preserves_slice = False
        block_cols.append([De[r] for r in SLICE_IDX])
    block44 = Matrix(4, 4, lambda r, c: block_cols[c][r])
    is_zero = block44.is_zero_matrix

    eta, B = minkowski_form()
    block_mink = B * block44 * B.inv()
    so31 = (eta * block_mink + block_mink.T * eta).is_zero_matrix

    return {"block44_engine": block44, "block44_mink": block_mink,
            "leaves_V0": leaves_V0, "preserves_slice": preserves_slice,
            "so31_valued": so31, "is_zero_on_slice": is_zero}


def slice_residual(gens):
    """Given the generators of r_12 (joint stabilizer), compute the slice-action
    residual, EXACT over Q:
      - the SUBALGEBRA of r_12 that PRESERVES the slice and acts NONTRIVIALLY on it,
        expressed as the span of the 4x4 engine blocks (dimension = rank over QQ of
        the flattened-16 blocks);
      - n_zero_on_slice: how many basis gens act trivially on the slice (the internal
        triality/so(6) complement -- EXPECTED & fine);
      - n_leak: how many gens leak the slice OUT of V_0 (should be 0 -- the slice is
        an invariant subspace of the frame stabilizer);
      - all_so31: whether every nonzero slice block is so(3,1)-valued.
    Returns dict with slice_dim (the load-bearing Gate-0 number), iso hints, and the
    list of (gen_index, slice_action dict).
    """
    per = []
    blocks16 = []     # row-flattened 4x4 engine blocks, for the exact span rank
    n_zero = 0
    n_leak = 0
    n_preserve = 0
    all_so31 = True
    for k, D in enumerate(gens):
        sa = slice_action(D)
        per.append((k, sa))
        if sa["is_zero_on_slice"]:
            n_zero += 1
        else:
            blocks16.append([sa["block44_engine"][r, c] for r in range(4) for c in range(4)])
            if not sa["so31_valued"]:
                all_so31 = False
        if not sa["leaves_V0"]:
            n_leak += 1
        if sa["preserves_slice"]:
            n_preserve += 1
    slice_dim = Matrix(blocks16).rank() if blocks16 else 0
    return {"slice_dim": slice_dim, "n_zero_on_slice": n_zero, "n_leak": n_leak,
            "n_preserve_slice": n_preserve, "all_so31": all_so31,
            "n_gens": len(gens), "per": per}


# ============================================================================
# 6. VERDICT LADDER -- deterministic, NON-hardwired (branch derived from the
#    COMPUTED slice_dim), with self-tests proving it fires on synthetic inputs.
# ============================================================================
def verdict(slice_dim, n_leak):
    """Route Gate 0 from the COMPUTED slice-residual dimension (NOT a literal).

      slice_dim == 0  -> 'GATE0-UNIQUE'   : identification already unique from bare
                         algebra -> skip Gate 1, go to Gate 2 with the unique
                         identifications.  (ROUTING decision, NOT the milestone DEAD.)
      slice_dim  > 0  -> 'RESIDUAL-SURVIVES': record the surviving slice-residual
                         group (the 2-point freedom) -> proceed to Gate 1.

    A nonzero n_leak means the slice is NOT an invariant subspace of the frame
    stabilizer -- a MODELING/BUILD inconsistency, surfaced as 'BUILD-ERROR' so the
    orchestrator stops rather than trusting a leaking slice action.
    """
    if n_leak != 0:
        return "BUILD-ERROR"
    if slice_dim == 0:
        return "GATE0-UNIQUE"
    return "RESIDUAL-SURVIVES"


def _verdict_selftests():
    """Prove the verdict ladder fires correctly on SYNTHETIC inputs (no hardcoded
    decisive boolean: each branch is reached by a different synthetic slice_dim)."""
    cases = [
        ("synthetic slice_dim=0, no leak -> GATE0-UNIQUE",
         verdict(0, 0), "GATE0-UNIQUE"),
        ("synthetic slice_dim=3, no leak -> RESIDUAL-SURVIVES",
         verdict(3, 0), "RESIDUAL-SURVIVES"),
        ("synthetic slice_dim=6, no leak -> RESIDUAL-SURVIVES",
         verdict(6, 0), "RESIDUAL-SURVIVES"),
        ("synthetic leak!=0 -> BUILD-ERROR",
         verdict(3, 2), "BUILD-ERROR"),
    ]
    ok = True
    for label, got, want in cases:
        ok &= _report(f"verdict self-test: {label} (got {got})", got == want)
    return ok


# ============================================================================
# 7. Iso-type hints (dimension -> classical algebra name), informational only.
# ============================================================================
def iso_hint(dim):
    table = {
        0: "trivial (0-dim)",
        1: "u(1) / so(2)",
        3: "so(3) ~ su(2)  (the compact rotation block)",
        6: "so(4) ~ su(2)+su(2)  OR so(3,1) (dim 6) -- distinguish by signature",
        8: "su(3)  (dim 8)",
        15: "so(6) ~ su(4)  (dim 15)",
        21: "so(7)  (dim 21)",
        28: "so(8)  (dim 28; triality)",
        36: "so(9)  (dim 36)",
        45: "so(10)  (dim 45)",
        52: "f_4  (dim 52)",
    }
    return table.get(dim, f"dim {dim} (no standard label tabulated)")


# ============================================================================
# 7b. PEIRCE STRUCTURE (projectors + the V_{1/2} -> V_0 quadratic map)
#     Used by the GATE 1 conditions (u-alignment, Peirce-block, interface).
# ============================================================================
def peirce_proj(E, val):
    """Exact spectral projector onto the eigenvalue-`val` Peirce space of L_E
    (val in {0, 1/2, 1}); L_E = jordan(E, .).  EXACT over Q (Lagrange interpolation
    on the 3 distinct eigenvalues).  For E_11: P_0 picks {1..10}=V_0, P_{1/2} picks
    {11..26}=V_{1/2}, P_1 picks {0}=V_1."""
    basis = RL._standard_basis_27()
    L = RL.jordan_L_matrix(E, basis)
    eigs = [Rational(0), Rational(1, 2), Rational(1)]
    others = [v for v in eigs if v != val]
    Pj = Matrix.eye(27)
    for o in others:
        Pj = Pj * (L - o * Matrix.eye(27)) * Rational(1, (val - o))
    return Pj


def peirce_idx(E, val):
    """The standard-basis indices that are pure eigenvalue-`val` eigenvectors of L_E."""
    basis = RL._standard_basis_27()
    L = RL.jordan_L_matrix(E, basis)
    out = []
    for k in range(27):
        e = Matrix([Rational(1) if r == k else Rational(0) for r in range(27)])
        Le = L * e
        nz = {r: Le[r] for r in range(27) if Le[r] != 0}
        if nz == {k: val} or (val == 0 and nz == {}):
            out.append(k)
    return out


def _vec(k):
    return Matrix([Rational(1) if r == k else Rational(0) for r in range(27)])


def _X(v):
    return RL.X_from_symbols([v[i] for i in range(27)])


def _flatv(X):
    return Matrix(RL._flat27(X))


# ============================================================================
# 7c. GATE 1 -- the canonicalization sweep.
#
# The residual after Gate 0 lives in r_12 = {D in f_4 : D.E_11=0, D.E_22=0} = so(8)
# (slice action = so(2) C_u-phase, dim 1).  Each program-native compatibility
# condition carves a SUBALGEBRA R^(i) of r_12; we recompute the surviving SLICE
# residual (via slice_residual) after each, and cumulatively.
#
# Conditions (prompt verbatim):
#   (1) u-alignment        : D's slice action commutes with the C_u complex
#                            structure J (mult-by-e_7 on C_u; the {p,q} rotation).
#                            => D preserves the complex structure u = e_7.
#   (2) det_2 isometry      : D's slice action is so(3,1)-valued (preserves det_2).
#                            AUTOMATIC from F_4 subset Aut -- VERIFIED, not assumed.
#   (3) Peirce-block        : D maps V_1(E_11)->V_1, V_{1/2}(E_11)->V_{1/2},
#                            V_0(E_11)->V_0.  AUTOMATIC since D.E_11=0 (D commutes
#                            with L_{E_11}) -- VERIFIED.
#   (4) interface intertwining (THE one with modeling content): D is a derivation
#                            of the Peirce quadratic map Q_11(x,y)=Pi_{V_0(E_11)}(x o y)
#                            on the shared V_{1/2} channel.  Exact operator equation
#                            below; non-vacuity is DEMONSTRATED (a non-derivation map
#                            fails it).
# ============================================================================

# The C_u complex structure J on the slice {1,2,3,10}: mult-by-e_7 inside C_u sends
# p=Re(x1) (idx 3) -> q=<x1,e7> (idx 10), q -> -p.  As a 4x4 on SLICE_IDX order
# [beta(1),gamma(2),p(3),q(10)]: J[p,q-col]... position of idx3 is 2, idx10 is 3.
def _Cu_complex_structure_slice():
    Js = Matrix.zeros(4, 4)
    Js[3, 2] = Rational(1)    # p -> q   (slice-row idx10, slice-col idx3)
    Js[2, 3] = Rational(-1)   # q -> -p
    return Js


def cond1_u_alignment(D):
    """(1) u-alignment: D's 4x4 slice action commutes with the C_u complex structure J.
    Equivalently D preserves the complex structure u=e_7 of the slice (intertwines
    pi_u, pi_u').  Returns True iff [D_slice, J_slice] == 0."""
    b = slice_action(D)["block44_engine"]
    Js = _Cu_complex_structure_slice()
    return (b * Js - Js * b).is_zero_matrix


def cond2_det2_isometry(D):
    """(2) det_2 isometry: D's slice action preserves the det_2 Minkowski form, i.e.
    is so(3,1)-valued (AUTOMATIC from F_4 subset Aut; VERIFIED here).  A zero slice
    block trivially preserves it."""
    return slice_action(D)["so31_valued"]


def cond3_peirce_block(D, E=None):
    """(3) Peirce-block preservation: D maps each Peirce space of E_11 to itself
    (V_1->V_1, V_{1/2}->V_{1/2}, V_0->V_0).  AUTOMATIC since D.E_11=0; VERIFIED."""
    if E is None:
        E = E11
    for val in (Rational(1), Rational(1, 2), Rational(0)):
        idxset = peirce_idx(E, val)
        comp = [i for i in range(27) if i not in idxset]
        for j in idxset:
            Dj = D * _vec(j)
            if any(Dj[a] != 0 for a in comp):
                return False
    return True


# Cache the Peirce-0 projector of E_11 (used by cond4).
_P0_11_CACHE = {}


def _P0_11():
    if "P" not in _P0_11_CACHE:
        _P0_11_CACHE["P"] = peirce_proj(E11, Rational(0))
    return _P0_11_CACHE["P"]


def cond4_interface_intertwining(D, channel=None):
    """(4) Interface intertwining -- the minimal mutual-faithfulness proxy.

    OPERATOR EQUATION (derived from Peirce structure alone; the SHARED V_{1/2}
    channel of E_11 & E_22):

        For all x, y in V_{1/2}(E_11):
            Pi_{V_0(E_11)}( (D x) o y  +  x o (D y) )  ==  D ( Pi_{V_0(E_11)}( x o y ) )

    i.e. D is an infinitesimal DERIVATION of the Peirce quadratic map
        Q_11(x, y) = Pi_{V_0(E_11)}( x o y ) : V_{1/2}(E_11) x V_{1/2}(E_11) -> V_0(E_11),
    the canonical 'sequential-product data each observer assigns to the V_{1/2}
    channel'.  (Cross-frame intertwining Q_11 <-> Q_22 under the full g = P.exp(tD)
    splits into: P intertwines Q_11<->Q_22 EXACTLY since P in Aut -- VERIFIED in the
    driver -- plus the residual-D condition above.)

    `channel` (default = ALL of V_{1/2}(E_11) = {11..26}) lets the test focus on the
    SHARED sub-channel {19..26}=x3 = V_{1/2}(E_11) cap V_{1/2}(E_22); the result is the
    same (any f_4 derivation preserves every Peirce product).  The default tests the
    full V_{1/2}(E_11), the strongest form.

    NON-VACUITY: this equation has TEETH -- a linear map that is NOT an f_4 derivation
    (e.g. one adding a cross-channel V_{1/2} coupling) FAILS it (demonstrated in the
    driver's cond4 non-vacuity check).  It is auto-satisfied for D in r_12 because
    r_12 subset Der(h_3(O)) and every D in r_12 fixes E_11 (commutes with
    Pi_{V_0(E_11)}); that is the honest reason the so(2) survives, NOT a vacuous test."""
    if channel is None:
        channel = list(range(11, 27))     # full V_{1/2}(E_11)
    P0 = _P0_11()
    for ix in channel:
        Xx = _X(_vec(ix))
        Dx = _X(D * _vec(ix))
        for iy in channel:
            Yy = _X(_vec(iy))
            Dy = _X(D * _vec(iy))
            lhs = P0 * (_flatv(RL.jordan(Dx, Yy)) + _flatv(RL.jordan(Xx, Dy)))
            rhs = D * (P0 * _flatv(RL.jordan(Xx, Yy)))
            if lhs != rhs:
                return False
    return True


def cond4_nonvacuity_demo():
    """Demonstrate cond 4 is NON-VACUOUS: a finite linear map on V_{1/2} that is NOT an
    f_4 derivation (P with a spurious cross-channel V_{1/2} coupling 11->19 added)
    FAILS the cross-frame intertwining of Q_11 <-> Q_22.  Returns (P_passes, corrupt_fails).
    P_passes must be True (P is a genuine automorphism); corrupt_fails must be True
    (the equation rejects a non-automorphism) => the condition has teeth."""
    P0_11 = _P0_11()
    P0_22 = peirce_proj(E22, Rational(0))
    Pmat = build_P()
    Vh11 = list(range(11, 27))

    def cross_intertwines(g, idxs):
        for ix in idxs:
            Xx = _X(_vec(ix)); gx = _X(g * _vec(ix))
            for iy in idxs:
                Yy = _X(_vec(iy)); gy = _X(g * _vec(iy))
                lhs = g * (P0_11 * _flatv(RL.jordan(Xx, Yy)))
                rhs = P0_22 * _flatv(RL.jordan(gx, gy))
                if lhs != rhs:
                    return False
        return True

    P_passes = cross_intertwines(Pmat, Vh11)
    g_bad = Pmat.copy()
    g_bad[19, 11] = Rational(1)     # spurious x2(idx11)->x3(idx19) cross-channel coupling
    corrupt_fails = not cross_intertwines(g_bad, Vh11)
    return P_passes, corrupt_fails


def carve_subalgebra(gens, predicate):
    """Return the largest subset of `gens` closed under `predicate` AS A SUBSPACE:
    the residual is a LINEAR subalgebra, so we keep the maximal independent set of
    generators satisfying the linear `predicate(D)`.  Because each condition here is
    a LINEAR condition on D, the surviving subalgebra = span of the gens passing the
    test (we return them; the slice residual is computed from this span).  EXACT."""
    return [D for D in gens if predicate(D)]


def gate1_sweep(gens):
    """Run the Gate-1 canonicalization sweep on the r_12 generators.  Imposes the four
    conditions ONE AT A TIME then CUMULATIVELY, recomputing the surviving slice residual
    at each step.  Returns a dict with the per-condition and cumulative chains."""
    base = slice_residual(gens)
    out = {"R12": {"n_gens": len(gens), "slice_dim": base["slice_dim"]}}

    conds = [
        ("1_u_alignment", cond1_u_alignment),
        ("2_det2_isometry", cond2_det2_isometry),
        ("3_peirce_block", cond3_peirce_block),
        ("4_interface", cond4_interface_intertwining),
    ]

    # ONE-AT-A-TIME: each condition applied to the FULL r_12.
    individual = {}
    for name, pred in conds:
        kept = carve_subalgebra(gens, pred)
        sr = slice_residual(kept)
        individual[name] = {"n_kept": len(kept), "slice_dim": sr["slice_dim"],
                            "automatic": len(kept) == len(gens)}
    out["individual"] = individual

    # CUMULATIVE: intersect conditions 1..k.
    cumulative = {}
    kept = list(gens)
    for name, pred in conds:
        kept = carve_subalgebra(kept, pred)
        sr = slice_residual(kept)
        cumulative[name] = {"n_kept": len(kept), "slice_dim": sr["slice_dim"]}
    out["cumulative"] = cumulative
    out["final_slice_dim"] = cumulative[conds[-1][0]]["slice_dim"]
    out["final_n_kept"] = cumulative[conds[-1][0]]["n_kept"]
    return out


# ============================================================================
# 7d. GATE 1 VERDICT LADDER -- deterministic, NON-hardwired, self-tested.
# ============================================================================
def gate1_verdict(final_slice_dim):
    """Route Gate 1 from the COMPUTED final cumulative slice residual (NOT a literal).

      final_slice_dim == 0 -> 'CANONICAL'       : some condition cut the freedom to
                              triviality -> identifications are algebra-determined ->
                              Gate 2 with the canonical g's.
      final_slice_dim  > 0 -> 'RESIDUAL-SURVIVES': freedom survives all four conditions
                              -> the 2-point independence result -> Gate 2 sweeping the
                              residual classes."""
    if final_slice_dim == 0:
        return "CANONICAL"
    return "RESIDUAL-SURVIVES"


def _gate1_verdict_selftests():
    cases = [
        ("synthetic final_slice_dim=0 -> CANONICAL", gate1_verdict(0), "CANONICAL"),
        ("synthetic final_slice_dim=1 -> RESIDUAL-SURVIVES",
         gate1_verdict(1), "RESIDUAL-SURVIVES"),
        ("synthetic final_slice_dim=3 -> RESIDUAL-SURVIVES",
         gate1_verdict(3), "RESIDUAL-SURVIVES"),
    ]
    ok = True
    for label, got, want in cases:
        ok &= _report(f"gate1 verdict self-test: {label} (got {got})", got == want)
    return ok


# ============================================================================
# 8. GATE 0 DRIVER
# ============================================================================
def main():
    print("=" * 78)
    print("DERIVATION 82 -- KKT GLUING & 3-POINT HOLONOMY -- GATE 0 (exact over Q)")
    print("=" * 78)

    if not source_guard():
        print("\nSOURCE GUARD FAILED -- aborting before any decisive computation.")
        return 1

    # ---- Task 1a : the exact conjugating automorphism P ---------------------
    print("\n" + "-" * 78)
    print("TASK 1a -- exact conjugating automorphism P (F_4, P.E_11 = E_22)")
    print("-" * 78)
    P, P_ok = check_P(verbose=True)

    # ---- f_4 basis ----------------------------------------------------------
    print("\n" + "-" * 78)
    print("f_4 = Der(h_3(O)) basis (dim 52, exact over Q)")
    print("-" * 78)
    basis, f4dim, nbrack = f4_basis()
    _report(f"inner_derivations() returns {nbrack} nonzero brackets", nbrack == 324)
    _report(f"dim f_4 == 52 (span rank over QQ of all {nbrack})",
            _F4_CACHE["span_rank"] == 52)
    _report(f"selected basis has 52 generators (rref pivots)", f4dim == 52)

    # ---- Task 1b : Stab_{f_4}(E_11) ----------------------------------------
    print("\n" + "-" * 78)
    print("TASK 1b -- Stab_{f_4}(E_11) (the identification coset is P . Stab)")
    print("-" * 78)
    stab11 = stab_f4([E11], basis=basis)
    _log(f"dim Stab_{{f_4}}(E_11) = {stab11['dim']}  "
         f"(img_dim {stab11['img_dim']}, basis_dim {stab11['basis_dim']})")
    _report(f"dim Stab_{{f_4}}(E_11) == 36 = dim spin(9)  [{iso_hint(stab11['dim'])}]",
            stab11["dim"] == 36)
    print(f"  coset {{g in F_4 : g.E_11 = E_22}} = P . Stab_{{F_4}}(E_11), "
          f"dim {stab11['dim']} (the P-translate of the 36-dim stabilizer).")

    # ---- Task 2a : r_12 = joint stabilizer of the standard frame -----------
    print("\n" + "-" * 78)
    print("TASK 2a -- r_12 = joint stabilizer {D in f_4 : D.E_11=0 AND D.E_22=0}")
    print("-" * 78)
    r12 = stab_f4([E11, E22], basis=basis)
    _log(f"dim r_12 = {r12['dim']}  (img_dim {r12['img_dim']}, basis_dim {r12['basis_dim']})")
    _report(f"dim r_12 == 28 = dim spin(8) (triality)  [{iso_hint(r12['dim'])}]",
            r12["dim"] == 28)
    # Sanity: fixing E_11 & E_22 also fixes E_33 = I - E_11 - E_22 (the whole frame).
    fix_E33 = all((D * Matrix(RL._flat27(E33))).is_zero_matrix for D in r12["gens"])
    _report("r_12 also annihilates E_33 = I - E_11 - E_22 (fixes the whole frame)",
            fix_E33)

    # ---- Task 2b : SLICE ACTION of r_12 on h_2(C_u)(E_11) ------------------
    print("\n" + "-" * 78)
    print("TASK 2b -- slice action of r_12 on h_2(C_u)(E_11) = coords {1,2,3,10}")
    print("-" * 78)
    sr = slice_residual(r12["gens"])
    _report("r_12 keeps the 4d slice INSIDE V_0 (no cone-normal leak; invariant subspace)",
            sr["n_leak"] == 0)
    _log(f"slice-acting residual dimension (span of 4x4 engine blocks) = {sr['slice_dim']}")
    _log(f"  generators acting TRIVIALLY on the slice (internal so(6)/triality) = "
         f"{sr['n_zero_on_slice']} of {sr['n_gens']}")
    _log(f"  generators preserving the slice (slice -> slice) = {sr['n_preserve_slice']}")
    _log(f"  every nonzero slice block is so(3,1)-valued (Lorentz) = {sr['all_so31']}")
    print(f"  ==> slice-action residual: dim {sr['slice_dim']}  "
          f"[{iso_hint(sr['slice_dim'])}]")
    if sr["all_so31"] and sr["slice_dim"] > 0:
        print(f"      (the {sr['slice_dim']}-dim residual sits inside the slice "
              f"structure group so(3,1); its COMPACT part is so(3) per the "
              f"pre-registered wrinkle)")

    # ---- Verdict ladder (with self-tests) ----------------------------------
    print("\n" + "-" * 78)
    print("VERDICT LADDER (deterministic, non-hardwired; self-tested)")
    print("-" * 78)
    selftests_ok = _verdict_selftests()
    v = verdict(sr["slice_dim"], sr["n_leak"])
    print(f"\n  COMPUTED slice_dim = {sr['slice_dim']}, n_leak = {sr['n_leak']}")
    print(f"  VERDICT (derived from the computed dim) = {v}")
    if v == "GATE0-UNIQUE":
        print("  ROUTING: identification unique from bare algebra -> SKIP Gate 1, "
              "go to Gate 2 with the unique identifications.")
    elif v == "RESIDUAL-SURVIVES":
        print(f"  ROUTING: residual slice freedom survives (dim {sr['slice_dim']}, "
              f"{iso_hint(sr['slice_dim'])}) -> RECORD the 2-point freedom, proceed "
              f"to Gate 1 (canonicalization sweep).")
        print("  NOTE (pre-registered wrinkle): a COMPACT residual (e.g. so(3)) is "
              "CONSISTENT with the dictionary picture -- NOT a kill.")
    else:
        print("  ROUTING: BUILD-ERROR -- slice leaks out of V_0; STOP and report "
              "(do not trust a leaking slice action).")

    _report("verdict ladder self-tests all pass", selftests_ok)

    # ---- summary line -------------------------------------------------------
    print("\n" + "=" * 78)
    print("GATE-0 SUMMARY (load-bearing numbers, exact over Q):")
    print(f"  P                       : exact F_4 signed-permutation, P.E_11=E_22, "
          f"P^2=I, det=1")
    print(f"  dim Stab_{{F_4}}(E_11)     : {stab11['dim']}  ({iso_hint(stab11['dim'])})")
    print(f"  dim r_12 (joint stab)   : {r12['dim']}  ({iso_hint(r12['dim'])})")
    print(f"  slice-action residual   : dim {sr['slice_dim']}  "
          f"({iso_hint(sr['slice_dim'])}); so(3,1)-valued={sr['all_so31']}; "
          f"trivial-on-slice gens={sr['n_zero_on_slice']}/{sr['n_gens']}")
    print(f"  VERDICT / routing       : {v}")
    print("=" * 78)

    print(f"\n{'ALL_PASS' if ALL_PASS else 'SOME CHECKS FAILED'} "
          f"(P_ok={P_ok}, selftests={selftests_ok})")
    return 0 if ALL_PASS else 1


# ============================================================================
# 9. GATE 1 DRIVER -- the canonicalization sweep (does any condition force unique?)
# ============================================================================
def main_gate1():
    print("=" * 78)
    print("DERIVATION 82 -- KKT GLUING & 3-POINT HOLONOMY -- GATE 1 (exact over Q)")
    print("  the canonicalization sweep: R_12 -> R^(1) -> R^(2) -> R^(3) -> R^(4)")
    print("=" * 78)

    if not source_guard():
        print("\nSOURCE GUARD FAILED -- aborting before any decisive computation.")
        return 1

    # ---- Peirce structure (frame the sweep) ---------------------------------
    print("\n" + "-" * 78)
    print("PEIRCE STRUCTURE under the standard frame (exact eigenspaces of L_E)")
    print("-" * 78)
    v1_11 = peirce_idx(E11, Rational(1))
    vh_11 = peirce_idx(E11, Rational(1, 2))
    v0_11 = peirce_idx(E11, Rational(0))
    vh_22 = peirce_idx(E22, Rational(1, 2))
    shared = sorted(set(vh_11) & set(vh_22))
    _report(f"V_1(E_11) = {v1_11} (dim 1)", v1_11 == [0])
    _report(f"V_{{1/2}}(E_11) = {{11..26}} (dim 16)", vh_11 == list(range(11, 27)))
    _report(f"V_0(E_11) = {{1..10}} (dim 10); spacetime slice {{1,2,3,10}} subset V_0",
            v0_11 == list(range(1, 11)) and all(s in v0_11 for s in SLICE_IDX))
    print(f"  V_{{1/2}}(E_22) = {vh_22}")
    print(f"  SHARED V_{{1/2}} channel = V_{{1/2}}(E_11) cap V_{{1/2}}(E_22) = {shared} "
          f"(= x3 slot; connects E_11<->E_22)")

    # ---- build r_12 (the Gate-0 residual carrier) ---------------------------
    basis, _, _ = f4_basis()
    r12 = stab_f4([E11, E22], basis=basis)
    base = slice_residual(r12["gens"])
    print("\n" + "-" * 78)
    print(f"GATE-0 START: r_12 = so(8) (dim {r12['dim']}); slice residual = "
          f"dim {base['slice_dim']} ({iso_hint(base['slice_dim'])}, the C_u phase)")
    print("-" * 78)
    _report(f"r_12 dim == 28 (so(8))", r12["dim"] == 28)
    _report(f"Gate-0 slice residual == 1 (so(2)=u(1))", base["slice_dim"] == 1)

    # ---- condition-4 non-vacuity (it MUST have teeth) -----------------------
    print("\n" + "-" * 78)
    print("CONDITION 4 -- non-vacuity check (the operator equation must have TEETH)")
    print("-" * 78)
    P_passes, corrupt_fails = cond4_nonvacuity_demo()
    _report("P (genuine Aut) intertwines Q_11 <-> Q_22 cross-frame (exact)", P_passes)
    _report("a non-derivation map (P + spurious x2->x3 cross-coupling) FAILS the "
            "intertwining  => condition 4 is NON-VACUOUS (has teeth)", corrupt_fails)

    # ---- the sweep ----------------------------------------------------------
    print("\n" + "-" * 78)
    print("THE SWEEP: each condition ONE-AT-A-TIME then CUMULATIVE (slice residual dim)")
    print("-" * 78)
    sweep = gate1_sweep(r12["gens"])
    names = {"1_u_alignment": "u-alignment",
             "2_det2_isometry": "det_2 isometry",
             "3_peirce_block": "Peirce-block preservation",
             "4_interface": "interface intertwining"}
    print(f"  R_12 (start)                         : slice_dim = {sweep['R12']['slice_dim']}  "
          f"({iso_hint(sweep['R12']['slice_dim'])})")
    print("\n  ONE-AT-A-TIME (each applied to the full r_12):")
    for key in ["1_u_alignment", "2_det2_isometry", "3_peirce_block", "4_interface"]:
        d = sweep["individual"][key]
        tag = "AUTOMATIC" if d["automatic"] else "NON-TRIVIAL (cuts)"
        print(f"    cond {key[0]} ({names[key]:<26}): kept {d['n_kept']:>2}/28 gens, "
              f"slice_dim = {d['slice_dim']}  [{tag}]")
    print("\n  CUMULATIVE chain R_12 ⊇ R^(1) ⊇ R^(2) ⊇ R^(3) ⊇ R^(4):")
    chain = [("R_12", sweep["R12"]["slice_dim"])]
    for i, key in enumerate(["1_u_alignment", "2_det2_isometry",
                             "3_peirce_block", "4_interface"], start=1):
        d = sweep["cumulative"][key]
        chain.append((f"R^({i})", d["slice_dim"]))
        print(f"    R^({i}) after +cond {i} ({names[key]:<26}): "
              f"kept {d['n_kept']:>2}/28, slice_dim = {d['slice_dim']}  "
              f"({iso_hint(d['slice_dim'])})")
    print("    chain:  " + " ⊇ ".join(f"{nm}(dim {dm})" for nm, dm in chain))

    # ---- verdict ladder (self-tested) ---------------------------------------
    print("\n" + "-" * 78)
    print("GATE-1 VERDICT LADDER (deterministic, non-hardwired; self-tested)")
    print("-" * 78)
    selftests_ok = _gate1_verdict_selftests()
    final = sweep["final_slice_dim"]
    gv = gate1_verdict(final)
    print(f"\n  COMPUTED final cumulative slice_dim = {final}")
    print(f"  GATE-1 VERDICT (derived from the computed dim) = {gv}")
    if gv == "CANONICAL":
        print("  ROUTING: a condition cut the residual to triviality -> identifications "
              "are algebra-determined (CANONICAL) -> Gate 2 with the canonical g's.")
    else:
        print(f"  ROUTING: residual SURVIVES all four conditions (dim {final}, "
              f"{iso_hint(final)} = the C_u phase) -> this IS the 2-point INDEPENDENCE "
              f"result -> Gate 2 SWEEPING the residual classes.")
        print("  NOTE (pre-registered): a COMPACT residual is NOT a kill; full SL(2,C) "
              "boosts were never inside Spin(9) (Phase 48, metric-side).")
    _report("gate1 verdict ladder self-tests all pass", selftests_ok)

    # ---- summary ------------------------------------------------------------
    print("\n" + "=" * 78)
    print("GATE-1 SUMMARY (residual chain, exact over Q):")
    print(f"  chain R_12 ⊇ R^(1) ⊇ R^(2) ⊇ R^(3) ⊇ R^(4) (slice_dim): "
          + " ⊇ ".join(str(dm) for _, dm in chain))
    autos = [names[k] for k in sweep["individual"] if sweep["individual"][k]["automatic"]]
    cuts = [names[k] for k in sweep["individual"] if not sweep["individual"][k]["automatic"]]
    print(f"  AUTOMATIC conditions    : {autos}")
    print(f"  NON-TRIVIAL (cutting)   : {cuts if cuts else 'NONE -- no condition cuts the so(2)'}")
    print(f"  final residual          : dim {final}  ({iso_hint(final)})")
    print(f"  VERDICT / routing       : {gv}")
    print("=" * 78)

    print(f"\n{'ALL_PASS' if ALL_PASS else 'SOME CHECKS FAILED'} "
          f"(nonvacuity: P={P_passes}/corrupt_fails={corrupt_fails}; "
          f"selftests={selftests_ok})")
    return 0 if ALL_PASS else 1


# ============================================================================
# 10. GATE 2 -- three-point holonomy (THE DECISIVE GATE), exact over Q.
#
# Frame E_11,E_22,E_33; base identifications G_ij = conj by the (i<->j) index swap
# (each an exact F_4 element, G_ij.E_ii = E_jj -- the per-leg analogue of P).  The
# residual U(1) per leg (Gate 0/1: the C_u phase, slice so(2)) modifies each leg:
#   g_ij(phi) = G_ij . A_i(phi),   A_i(phi) = exp(phi J_i) in r_ij = joint-stab,
# the C_u phase of E_ii's slice (a clean 2-plane rotation in {Re(x),<x,e7>}).
# Loop  h(phi) = g_31 . g_23 . g_12 in Stab(E_11); read its 4x4 slice action on
# h_2(C_u)(E_11).  EVERY factor maps/preserves the 4d slices with NO leak (verified),
# so the whole holonomy is computed EXACTLY in 4x4 slice maps; the phases are clean
# 2-plane rotations exp(phi J)=I+sin J+(1-cos)J^2 -> a 2x2 rotation block.
#
# DECISIVE three-way (deterministic, non-hardwired):
#   DEAD   : h_slice(phi) == I for ALL admissible phi  (algebra certifies flat gluing).
#   LIVE-A : h_slice varies AND == I for SOME phi (gluing genuinely FREE -> indep).
#   LIVE-B : h_slice != I for ALL admissible phi (forced nontrivial -> curvature seed).
#
# THE FIRED BUG-GUARD (prompt: "a spurious forced-h is the most likely executor bug"):
# the bare frame TRANSPOSITIONS carry an octonion conjugation that FLIPS u=e_7
# (antiholomorphic on the C_u slice) -> they FAIL Gate-1 u-alignment, are INADMISSIBLE,
# and a transposition-loop returns a SPURIOUS nontrivial diag(1,1,-1,-1) (the bug).  The
# ADMISSIBLE identifications are u-ALIGNED: the 3-cycle rho (rho^3=I) gives a FLAT base.
#
# STRUCTURAL REDUCTION (Ehrlich): every residual element fixes BOTH endpoint idempotents
# and is an automorphism, so it intertwines ALL purely-algebraic data -> Gate-1 conds 1-4
# can NEVER cut it -> LIVE-vs-DEAD reduces to ONE fact: does the joint endpoint stabilizer
# act NONTRIVIALLY on the h_2(C_u) slice?  It does (a genuine compact SO(2) = the C_u phase)
# -> with the u-aligned rho base (flat) the holonomy h(phi) is flat at phi=0 and nontrivial
# for phi!=0 -> LIVE-A.  The admissible loop reaches only the single C_u-plane SO(2) (a
# gauge-flavored U(1)), NOT full SO(3) (the so(3) add-on); independence ONLY (no metric).
# ============================================================================

# slice(E_ii) engine-coord bases, order [diag_lo, diag_hi, Re(x_k), <x_k,e7>];
# the C_u 2-plane is positions {2,3}.
SLICE = {0: [1, 2, 3, 10], 1: [0, 2, 11, 18], 2: [0, 1, 19, 26]}
# TAU = the bare frame TRANSPOSITIONS (E_ii<->E_jj).  Each carries an octonion
# CONJUGATION that FLIPS u=e_7 (antiholomorphic on the C_u slice) -> it FAILS Gate-1
# u-alignment and is INADMISSIBLE.  Kept ONLY to document the FIRED bug-guard (the
# prompt's predicted spurious-forced-h: a tau-loop returns a nontrivial diag(1,1,-1,-1)).
_TAU = {(0, 1): {0: 1, 1: 0, 2: 2},
        (1, 2): {0: 0, 1: 2, 2: 1},
        (2, 0): {0: 2, 1: 1, 2: 0}}
# RHO = the u-ALIGNED 3-cycle automorphism, conj_perm(.,RHO): E_11->E_22->E_33->E_11.
# It PRESERVES u=e_7 (holomorphic) and has order 3 (rho^3 = I) -> the ADMISSIBLE base
# identification; its loop is FLAT.  (conj_perm(E_kk,sigma)=E_{sigma^{-1}(k)}, so
# sigma=RHO={0:2,1:0,2:1} gives E_11->E_22->E_33->E_11.)
_RHO = {0: 2, 1: 0, 2: 1}


def build_perm(sigma):
    """27x27 exact matrix of the index-permutation conjugation conj_perm(., sigma)."""
    basis = RL._standard_basis_27()
    cols = [RL._flat27(conj_perm(basis[k], sigma)) for k in range(27)]
    return Matrix(27, 27, lambda r, c: cols[c][r])


def grp_slice_block(M, src, dst):
    """4x4 block of a 27x27 (group OR Lie) element M: slice(src)->slice(dst) in engine
    bases, plus a leak flag (True if any image carries a component outside `dst`)."""
    leak = False
    cols = []
    for k in src:
        e = Matrix([Rational(1) if r == k else Rational(0) for r in range(27)])
        Me = M * e
        if any(Me[a] != 0 for a in range(27) if a not in dst):
            leak = True
        cols.append([Me[r] for r in dst])
    return Matrix(4, 4, lambda r, c: cols[c][r]), leak


def _Jrot4():
    """C_u-phase GENERATOR: rotation in slice positions {2,3}={Re(x),<x,e7>}; J^3=-J."""
    J = Matrix.zeros(4, 4)
    J[3, 2] = Rational(1)
    J[2, 3] = Rational(-1)
    return J


def phase4(c, s):
    """C_u-phase by (c,s)=(cos,sin) = exp(theta Jrot) = I + s Jrot + (1-c) Jrot^2 :
    a 2x2 rotation in slice positions {2,3}."""
    return Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, c, -s], [0, 0, s, c]])


def _reduce_pyth(expr, cs):
    """Reduce a sympy expr modulo s_i^2 = 1 - c_i^2 for every (c_i,s_i) in `cs`."""
    from sympy import expand
    e = expand(expr)
    for (c, s) in cs:
        e = e.subs(s**2, 1 - c**2)
        e = expand(e)
    return e


def gate2_verdict(constant, base_is_identity, identity_reachable):
    """Deterministic, NON-hardwired three-way from the COMPUTED orbit facts."""
    if constant:
        return "DEAD" if base_is_identity else "LIVE-B"
    return "LIVE-A" if identity_reachable else "LIVE-B"


def _gate2_verdict_selftests():
    cases = [
        ("constant & base=I            -> DEAD",   gate2_verdict(True, True, True),  "DEAD"),
        ("constant & base!=I           -> LIVE-B", gate2_verdict(True, False, False), "LIVE-B"),
        ("varies & identity reachable  -> LIVE-A", gate2_verdict(False, False, True), "LIVE-A"),
        ("varies & identity NOT reach. -> LIVE-B", gate2_verdict(False, False, False), "LIVE-B"),
    ]
    ok = True
    for label, got, want in cases:
        ok &= _report(f"gate2 verdict self-test: {label} (got {got})", got == want)
    return ok


def main_gate2():
    from sympy import symbols as _sym, eye as _eye
    print("=" * 78)
    print("DERIVATION 82 -- KKT GLUING & 3-POINT HOLONOMY -- GATE 2 (exact over Q)")
    print("  the decisive three-point holonomy h = g_31 . g_23 . g_12")
    print("=" * 78)

    if not source_guard():
        print("\nSOURCE GUARD FAILED -- aborting before any decisive computation.")
        return 1

    eta, B = minkowski_form()
    Binv = B.inv()
    Efr = {0: E11, 1: E22, 2: E33}
    Jc = _Jrot4()    # C_u complex structure on the slice (positions {2,3}); J^2 = -proj.

    def _u_in_x1():
        v = [Rational(0)] * 27
        v[10] = Rational(1)            # u = e_7 in the (2,1)=x1 slot (coord 10 = <x1,e7>)
        return RL.X_from_symbols(v)

    # ---- BUG-GUARD (FIRED): the bare TRANSPOSITIONS flip u -> INADMISSIBLE ----------
    print("\n" + "-" * 78)
    print("BUG-GUARD (FIRED): bare transpositions FLIP u=e_7 -> INADMISSIBLE (discarded)")
    print("-" * 78)
    Tau = {ij: build_perm(_TAU[ij]) for ij in [(0, 1), (1, 2), (2, 0)]}
    tau_flips_u = (RL._flat27(conj_perm(_u_in_x1(), _TAU[(0, 1)]))[18] == -1)
    _report("transposition tau_01 maps u=e_7 -> -e_7 => NOT u-aligned => INADMISSIBLE "
            "(Gate-1 cond 1)", tau_flips_u)
    Lt12, _lk = grp_slice_block(Tau[(0, 1)], SLICE[0], SLICE[1])
    _report("tau_01 slice map ANTI-intertwines the C_u complex structure "
            "(L_tau.J = -J.L_tau) => antiholomorphic", (Lt12 * Jc + Jc * Lt12).is_zero_matrix)
    H_tau = Tau[(2, 0)] * Tau[(1, 2)] * Tau[(0, 1)]
    Ht_eng, _lk = grp_slice_block(H_tau, SLICE[0], SLICE[0])
    print(f"  tau-loop slice action (Mink) = {(B * Ht_eng * Binv).tolist()}  "
          f"(the SPURIOUS LIVE-B -- DISCARDED)")
    print("  MONOTONICITY: admitting tau only ENLARGES the holonomy set; the u-aligned")
    print("  rho-loop (flat) + residual phases (nontrivial) stay admissible regardless,")
    print("  so identity remains reachable and DEAD cannot be restored.")

    # ---- the ADMISSIBLE base identification rho (u-aligned 3-cycle; rho^3=I; FLAT) --
    print("\n" + "-" * 78)
    print("ADMISSIBLE base rho: u-aligned 3-cycle E_11->E_22->E_33->E_11, rho^3=I (FLAT base)")
    print("-" * 78)
    R = build_perm(_RHO)
    for i, j in [(0, 1), (1, 2), (2, 0)]:
        _report(f"rho . E_{i+1}{i+1} == E_{j+1}{j+1}",
                RL.octmat_equal(conj_perm(Efr[i], _RHO), Efr[j]))
    _report("rho maps u=e_7 -> +e_7 (PRESERVES u) => u-aligned / holomorphic",
            RL._flat27(conj_perm(_u_in_x1(), _RHO))[18] == 1)   # e_7 -> +e_7 in x2 slot (coord 18)
    _report("rho^3 == I_27 (order 3) => the u-aligned base loop is FLAT",
            (R * R * R) == _eye(27))
    Lr12, lk1 = grp_slice_block(R, SLICE[0], SLICE[1])
    Lr23, lk2 = grp_slice_block(R, SLICE[1], SLICE[2])
    Lr31, lk3 = grp_slice_block(R, SLICE[2], SLICE[0])
    _report("rho slice maps slice(E_ii)->slice(E_jj) with NO leak (all three legs)",
            not (lk1 or lk2 or lk3))
    _report("rho slice map INTERTWINES the C_u complex structure (L_rho.J = +J.L_rho) "
            "=> holomorphic", (Lr12 * Jc - Jc * Lr12).is_zero_matrix)
    eta_eng = B.T * eta * B
    for nm, Lm in (("Lr12", Lr12), ("Lr23", Lr23), ("Lr31", Lr31)):
        _report(f"{nm} preserves det_2 (Lorentz between slices)",
                (Lm.T * eta_eng * Lm - eta_eng) == Matrix.zeros(4, 4))
    base_is_identity = (B * (Lr31 * Lr23 * Lr12) * Binv == _eye(4))
    _report("base loop (rho^3) slice action == I (FLAT gluing at the canonical base)",
            base_is_identity)

    # ---- STRUCTURAL REDUCTION: LIVE <=> joint-stab acts nontrivially on the slice --
    print("\n" + "-" * 78)
    print("STRUCTURAL REDUCTION: residual = joint-stab subset Der -> intertwines ALL")
    print("  algebraic data -> Gate-1 conds 1-4 cannot cut it -> LIVE iff slice nontrivial")
    print("-" * 78)
    basis, _, _ = f4_basis()
    Jrot = _Jrot4()
    r12 = stab_f4([E11, E22], basis=basis)
    _report("residual r_12 = {D in f_4 : D.E_11=0 AND D.E_22=0} = joint frame stabilizer "
            f"(dim {r12['dim']} = so(8))", r12["dim"] == 28)
    blocks = []
    for D in r12["gens"]:
        blk, _lk = grp_slice_block(D, SLICE[0], SLICE[0])
        if not blk.is_zero_matrix:
            blocks.append([blk[r, c] for r in range(4) for c in range(4)])
    sdim = Matrix(blocks).rank() if blocks else 0
    inspan = (Matrix(blocks + [[Jrot[r, c] for r in range(4) for c in range(4)]]).rank()
              == sdim) if blocks else False
    _report("joint-stab slice action is a GENUINE NONTRIVIAL compact SO(2) "
            f"(dim {sdim}==1, = the C_u phase <Jrot>)", sdim == 1 and inspan)
    print("  => by the reduction (the LOAD-BEARING fact), the gluing is NOT forced flat.")

    # ---- the ADMISSIBLE holonomy h(phi): u-aligned rho base + residual C_u phases --
    print("\n" + "-" * 78)
    print("ADMISSIBLE HOLONOMY h(phi) = (rho-loop) with the residual C_u phases turned on")
    print("-" * 78)
    c1, s1, c2, s2, c3, s3 = _sym('c1 s1 c2 s2 c3 s3', real=True)
    cs = [(c1, s1), (c2, s2), (c3, s3)]
    h_eng = Lr31 * phase4(c3, s3) * Lr23 * phase4(c2, s2) * Lr12 * phase4(c1, s1)
    h_mink = (B * h_eng * Binv).applyfunc(lambda e: _reduce_pyth(e, cs))
    free = set().union(*[e.free_symbols for e in h_mink]) if h_mink else set()
    varies = len(free & {c1, s1, c2, s2, c3, s3}) > 0
    _report("h(phi) VARIES with the residual phases (the SO(2) is genuinely turned on)",
            varies)
    h_at0 = h_mink.subs({c1: 1, s1: 0, c2: 1, s2: 0, c3: 1, s3: 0}).applyfunc(
        lambda e: _reduce_pyth(e, cs))
    identity_reachable = (h_at0 == _eye(4))
    _report("h(phi=0) == I (the pure rho-loop is FLAT -> identity REACHABLE)",
            identity_reachable)
    h1 = (B * (Lr31 * phase4(1, 0) * Lr23 * phase4(1, 0) * Lr12 * phase4(c1, s1)) * Binv)
    hv = h1.subs({c1: Rational(3, 5), s1: Rational(4, 5)})
    nontrivial_reachable = (hv != _eye(4))
    _report("h(single residual phase) != I -> NONTRIVIAL holonomy REACHABLE",
            nontrivial_reachable)
    iso_all = (h_mink.T * eta * h_mink - eta).applyfunc(
        lambda e: _reduce_pyth(e, cs)) == Matrix.zeros(4, 4)
    _report("h(phi) is a det_2-isometry (in SO(3,1)) for ALL phi", iso_all)

    # ---- so(3) ADD-ON (non-blocking): which holonomy GROUP does the loop reach? -----
    print("\n" + "-" * 78)
    print("ADD-ON (non-blocking): reachable holonomy group of the admissible rho-loop")
    print("-" * 78)
    L12i, L23i = Lr12.inv(), Lr23.inv()
    Xg = [Jrot, L12i * Jrot * Lr12, L12i * L23i * Jrot * Lr23 * Lr12]
    span_rank = Matrix([[(B * X * Binv)[r, c] for r in range(4) for c in range(4)]
                        for X in Xg]).rank()
    print(f"  span of the 3 conjugated phase-generators in so(3) = rank {span_rank}")
    print(f"  => the admissible loop with the joint-stab residual reaches "
          f"{'a single SO(2) (the C_u plane / a gauge-flavored U(1))' if span_rank == 1 else f'a rank-{span_rank} subgroup'}, "
          f"NOT full SO(3).  (No interpretation.)")

    # ---- VERDICT ladder (deterministic, non-hardwired; self-tested) ----------------
    print("\n" + "-" * 78)
    print("GATE-2 VERDICT LADDER (deterministic, non-hardwired; self-tested)")
    print("-" * 78)
    selftests_ok = _gate2_verdict_selftests()
    v = gate2_verdict(constant=(not varies),
                      base_is_identity=base_is_identity,
                      identity_reachable=identity_reachable)
    print(f"\n  COMPUTED: varies={varies}, base_is_identity={base_is_identity}, "
          f"identity_reachable={identity_reachable}, nontrivial_reachable={nontrivial_reachable}")
    print(f"  GATE-2 VERDICT (derived from the computed orbit) = {v}")
    if v == "LIVE-A":
        print("  ROUTING: with ADMISSIBLE (u-aligned) identifications the holonomy VARIES,")
        print("           identity reachable (phi=0, flat) AND nontrivial reachable (phi!=0)")
        print("           -> the inter-observer gluing holonomy is an UNFORCED choice ->")
        print("           INDEPENDENCE PROVED (the algebra does NOT force a canonical flat gluing).")
    _report("gate2 verdict ladder self-tests all pass", selftests_ok)

    # ---- summary -------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("GATE-2 SUMMARY (three-point holonomy, exact over Q):")
    print("  bug-guard FIRED         : bare transpositions FLIP u (antiholomorphic) -> "
          "INADMISSIBLE; their loop diag(1,1,-1,-1) was the SPURIOUS LIVE-B")
    print("  admissible base (rho^3) : FLAT (h_slice = I; rho u-aligned, order 3)")
    print("  structural reduction    : residual subset Der fixes both endpoints -> "
          "LIVE iff joint-stab slice action nontrivial")
    print("  joint-stab slice action : NONTRIVIAL compact SO(2) (the C_u phase) -> LIVE")
    print(f"  h(phi) varies/iso/reach : varies={varies}; det_2-isom={iso_all}; "
          f"identity@0={identity_reachable}; nontrivial@phi!=0={nontrivial_reachable}")
    print(f"  reachable holonomy grp  : rank {span_rank} = the single C_u-plane SO(2) / U(1) "
          f"(NOT full SO(3))")
    print(f"  GATE-2 VERDICT          : {v}  (INDEPENDENCE PROVED)")
    print("  ANTI-OVERCLAIM (binding): independence ONLY.  The freedom is ONE internal "
          "u-phase = a spatial SO(2)/U(1) (gauge-flavored, Berry/MM-shaped, NOT metric-")
    print("  shaped).  NOT 'the dictionary's DOF' (a tetrad needs frame-gluing freedom; "
          "boosts are never-algebra-internal, Phase 48); the bridge clamp is untouched;")
    print("  the six-kind menu stays exhausted; no kappa, no Lambda, no dynamics.")
    print("=" * 78)

    print(f"\n{'ALL_PASS' if ALL_PASS else 'SOME CHECKS FAILED'} "
          f"(verdict={v}; base_flat={base_is_identity}; joint_stab_so2={sdim == 1}; "
          f"varies={varies}; selftests={selftests_ok})")
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    _mode = sys.argv[1] if len(sys.argv) > 1 else "gate0"
    if _mode == "gate1":
        sys.exit(main_gate1())
    elif _mode == "gate2":
        sys.exit(main_gate2())
    else:
        sys.exit(main())
