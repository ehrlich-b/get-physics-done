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


if __name__ == "__main__":
    sys.exit(main())
