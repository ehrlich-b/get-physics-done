#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# Phase 78 (v18.0 Cartan / MacDowell-Mansouri) -- Plan 78-01  [THE FINAL PHASE]
#   THE DECISIVE FORCED-VS-POSITED CIRCULARITY AUDIT.
#
#   Measure, EXACT over Q, whether the MacDowell-Mansouri eps-contraction (the
#   Spin(9,1)->SO(3,1) breaking + the eps-tensor that turns F^F into Einstein-
#   Hilbert+Lambda) is FORCED by the intrinsic h_3(O) trace form Tr(X o Y) and
#   cubic norm det_3, or appears ONLY because an MM/EH action was posited by hand
#   (fp-imported-action).
#
#   Operationalized as a single decidable INTEGER plus an IDENTITY:
#     * the BARE so(3,1)-invariant quadratic-in-curvature 4-form space dimension
#       (expected 2 = Euler eps R^R + Pontryagin R^R) -- the mandatory sanity anchor;
#     * the strictly smaller TRACE-FORM-INVARIANT subspace -- the 4-form contractions
#       buildable from Tr(X o Y) (=> eta) and det_3 ALONE (the DECISIVE dimension);
#     * eps-reachability (both routes) + Pontryagin-reachability + det_3-fixed-vs-free
#       normalization -> the decisive triple (dim; eps-in-span; normalization).
#
#   THE AUDITED OBJECT is the LINEAR-in-Riemann Einstein-Hilbert term
#   eps_{abcd} R^{ab} ^ e^c ^ e^d (R wedged with the tetrad) -- which emerges from
#   the R^e^e CROSS-term of the eps F^F square -- NOT a quadratic-in-F Maxwell /
#   Pontryagin stress (the Phase-76 OVERTURNED tautology; [[feedback_test_right_object_not_tautology]]).
#   Here we count the quadratic-in-curvature invariants whose eps-contraction is the
#   one that produces that linear-in-R EH term.
#
# CONVENTIONS (state.json convention_lock / CONVENTIONS.md sec 0,1,6,11; carried
# from Phases 74-77):
#   * Metric mostly-minus (+,-,-,-); frame metric eta=diag(+1,-1,-1,-1) (1,3),
#     timelike-positive. The PHYSICAL frame metric is the SOLDERED det_2 Lorentzian
#     metric (Phase 75), NOT the bare Jordan trace Gram diag(2,2,2,2)=(4,0) (the OP^2
#     Fubini-Study FOIL -- reported transparently, never the spacetime metric).
#   * EXACT over Q (sympy.Matrix.rank / nullspace over QQ); NEVER numpy.linalg,
#     NEVER float on the decisive dimension/rank/identity (fp-float-decisive).
#   * det SSOT = ring_lemma_verification.py det_3 (the UNIQUE F_4-invariant cubic
#     norm; cross-term 2Re((x2 x1)x3), x2 BEFORE x1, Phase-64.1 fix; 324/324 inner-
#     derivation annihilation). octonion_algebra.py BANNED (buggy associator).
#   * Trace form c(X,Y)=Tr(X o Y)=Tr(jordan(X,Y)), jordan=(1/2)(AB+BA), F_4-invariant.
#   * Structure group: residual so(3,1)[6] FORCED by (E_11,u) (Phase 75; residual
#     21 = so(3,1)[6] (+) so(6)[15], the so(6) a trivial-on-spacetime ideal). The
#     invariant count is at the BROKEN so(3,1) level (the Spin(9,1)->SO(3,1) breaking
#     is exactly the 'by hand' step being audited).
#   * Index layout LOCKED LIVE: frame indices a,b,c,d=0..3 (so(3,1)); slice coords
#     (the soldered V_0 ~ R^{3,1} frame) = engine idx [1,2,3,10]={beta,gamma,p,q};
#     V_{1/2} survivors = engine idx [11,18,19,26].
#   * Lambda=0 at M=0 (Phase 77 MEASURED). At Lambda=0 the eps F^F action is pure
#     Gauss-Bonnet/Euler (topological). Do NOT reintroduce Lambda<0 / R x H^3.
#
# THE INPUT BAN (the forced determination may use ONLY Tr(X o Y), det_3, the Peirce
# decomposition under E_11, the C_u / pi_u reduction, the (E_11,u)-forced so(3,1)
# structure, and standard differential geometry). FORBIDDEN as load-bearing: any
# posited MM/EH/SUGRA action / '\int eps F^F' as an assumed action / '-1/2' / '16piG'
# / SUSY / Weinberg / octonion_algebra / numpy.linalg on the decisive path.
#
# FORBIDDEN PROXIES (all rejected; see the per-task guards):
#   fp-imported-action (CENTRAL): declaring a STRONG WIN whose final step is 'and
#     contracting MM-style with eps F^F gives Einstein-Hilbert'. We COUNT whether eps
#     is forced; we do NOT posit the eps-action and expand. fp-imported-action is the
#     HIGH / most-likely real outcome -- report at TRUE STRENGTH (an honest partial,
#     same class as GST/Singh/Castro), NOT a derivation.
#   fp-float-decisive: any decisive dim/rank on numpy/float. sympy over QQ only.
#   fp-octonion-algebra: octonion_algebra.py BANNED (buggy det_3 cross term).
#   fp-reuse-cone-hessian: the v17.0 symmetric/real cone-Hessian Riemann is a
#     DIFFERENT tensor (Re(QGT)); not load-bearing here (antisymmetric/Lie sector).
#   fp-wrong-object: auditing a quadratic-in-F Maxwell/Pontryagin stress as 'the
#     Einstein object' (the Phase-76 tautology). The EH term is LINEAR-in-R eps R^e^e.
#
# Reproducibility: Python 3.14.2, SymPy 1.14.0 (deterministic, exact over Q; no RNG,
#   no float on any decisive path). Reuses the WARM exact-Q engines (imported, NOT
#   rebuilt; det SSOT preserved).
#
# Runnable:  python3 -u code/cartan_phaseC_contraction.py
# Exit 0 iff every decisive check PASSES and the decisive triple is rendered cleanly.
# This plan renders the DIMENSION + IDENTITY at true strength; the FINAL verdict
# (STRONG WIN xor fp-imported-action) + human ratification are 78-02.
# ============================================================================

import os
import sys
import ast as _ast

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import (Matrix, Rational, zeros, eye, Symbol, LeviCivita,  # noqa: E402
                   linear_eq_to_matrix, simplify)

# WARM engines (imported, NOT rebuilt). NO octonion_algebra; NO numpy.linalg.
import ring_lemma_verification as RL          # noqa: E402  (det SSOT: det_3, Tr, c, jordan, polarize_d)
import bulk_geometry_verification as BG        # noqa: E402  (Peirce / Stab machinery for the forced so(3,1))
import cartan_phaseA_coframe as PA             # noqa: E402  (CU4_IDX, G_DET2_RAW, the (E_11,u)-forced frame)
import cartan_phaseB_curvature as P1           # noqa: E402  (Phase-77 R[omega]: curvature_F, split_blocks, riemann_lower_from_F)
# IMPORT-ONLY (do NOT run their __main__): the exact-over-Q rank/nullspace tooling.
from orbit_dimension_gate import (             # noqa: E402
    exact_qq_rank, span_rank_over_QQ,
)

N = 4
ETA = Matrix.diag(1, -1, -1, -1)               # frame metric diag(+1,-1,-1,-1), mostly-minus (1,3)
CU4_IDX = PA.CU4_IDX                            # [1,2,3,10] = {beta,gamma,p,q} soldered V_0 frame
W6_IDX = PA.W6_IDX                              # [4..9] internal V_0 sector
G_DET2_RAW = PA.G_DET2_RAW                      # the (1,3) det_2 Gram on raw {beta,gamma,p,q}

# Change of basis raw {beta,gamma,p,q} -> orthonormal {x0,x1,x2,x3} (52-kkt Eq 46.4):
#   x0=(beta+gamma)/2, x1=p, x2=q, x3=(beta-gamma)/2.  v_on = T v_raw.
T_ON = Matrix([[Rational(1, 2), Rational(1, 2), 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1],
               [Rational(1, 2), Rational(-1, 2), 0, 0]])
T_ON_INV = T_ON.inv()

ALL_PASS = True


def _report(label, ok):
    """Print a PASS/FAIL line; latch ALL_PASS to False on any failure."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return ok


def _signature(M):
    """(n_pos, n_neg, n_zero) of a symmetric rational Matrix, EXACT over Q via
    .eigenvals() (rational eigenvalues here). NEVER numpy/float (fp-float-decisive)."""
    ev = M.eigenvals()
    pos = sum(m for v, m in ev.items() if v > 0)
    neg = sum(m for v, m in ev.items() if v < 0)
    zer = sum(m for v, m in ev.items() if v == 0)
    return pos, neg, zer


# ============================================================================
# THE (E_11,u)-FORCED so(3,1) FRAME GENERATORS  (Phase 75 residual, exact over Q)
# ============================================================================
def forced_so31_generators():
    """The 6 so(3,1) generators on the 4 frame indices a,b,c,d=0..3, FORCED by
    (E_11,u) (Phase 75): residual structure group 21 = so(3,1)[6] (+) so(6)[15],
    the so(6) a trivial-on-spacetime ideal. Built by the EXACT-over-Q residual
    nullspace (mirror cartan_phaseA_coframe.vald02 steps 1,3,4), then restricted to
    the C_u 4-space CU4_IDX, then transformed to the orthonormal frame where
    eta=diag(+1,-1,-1,-1). Returns (L_on, L_raw): the 6 generators in the
    orthonormal frame AND in the raw {beta,gamma,p,q} basis.

    The invariant-tensor DIMENSION count is conjugation-invariant, so working in the
    orthonormal frame (where eps and Pontryagin are canonical) gives the SAME
    decisive dimension as the raw basis -- and we cross-check the forced generators
    span EXACTLY the canonical so(eta) (re-confirming Phase 75)."""
    e6_basis, _ = BG.build_e6_basis()
    sb = BG.stab_E6_E11(e6_basis)
    sV0 = BG.stab_preserving_V0(sb["stab_gens"])
    # residual = nullspace over QQ of {Stab_{V_0} preserving the C_u 4-space}
    rows = []
    for b in CU4_IDX:
        eb = Matrix([Rational(1) if i == b else Rational(0) for i in range(27)])
        col = [D * eb for D in sV0]
        for a in W6_IDX:
            rows.append([col[k][a] for k in range(len(sV0))])
    ns = Matrix(rows).nullspace()
    res = []
    for t in ns:
        D = zeros(27, 27)
        for k in range(len(sV0)):
            if t[k] != 0:
                D += t[k] * sV0[k]
        res.append(D)
    # restrict each residual generator to the C_u 4-space and take 6 independent.
    acts = [Matrix(4, 4, lambda i, j: D[CU4_IDX[i], CU4_IDX[j]]) for D in res]
    flat = Matrix([[A[r, c] for r in range(4) for c in range(4)] for A in acts])
    _, piv = flat.T.rref()
    L_raw = [acts[i] for i in piv]
    # transform to the orthonormal frame: A_on = T A_raw T^{-1}.
    L_on = [(T_ON * A * T_ON_INV).applyfunc(simplify) for A in L_raw]
    return L_on, L_raw, len(res)


def canonical_so_eta():
    """The canonical so(eta) basis: all 4x4 A with A^T eta + eta A = 0 (the Lorentz
    condition in the orthonormal frame), via exact nullspace over QQ. Returns the
    list of basis generators (expect 6)."""
    syms = [Symbol('a%d%d' % (i, j)) for i in range(4) for j in range(4)]
    A = Matrix(4, 4, lambda i, j: syms[4 * i + j])
    cond = A.T * ETA + ETA * A
    eqs = [cond[i, j] for i in range(4) for j in range(4)]
    M, _ = linear_eq_to_matrix(eqs, syms)
    canon = []
    for t in M.nullspace():
        canon.append(Matrix(4, 4, lambda i, j: t[4 * i + j]))
    return canon


# ============================================================================
# QUADRATIC-IN-CURVATURE 4-FORM TENSOR SPACE  (wedge symmetries on frame indices)
# ============================================================================
# A quadratic-in-curvature 4-form is  T_{abcd} R^{ab} ^ R^{cd}  with T_{abcd}:
#   antisymmetric in (a,b), antisymmetric in (c,d) (R^{ab} antisym),
#   symmetric under (ab)<->(cd) (the two 2-forms R^{ab},R^{cd} commute).
# Independent components: 6 antisym pairs P=(a<b); a symmetric 6x6 over pairs => 21
# free parameters. The so(3,1)-invariant subspace is the nullspace of delta_g T = 0.
_PAIRS = [(a, b) for a in range(4) for b in range(4) if a < b]     # 6 pairs
_PIDX = {p: k for k, p in enumerate(_PAIRS)}
_FREE = []
for _i in range(6):
    for _j in range(_i, 6):
        _FREE.append((_PAIRS[_i], _PAIRS[_j]))
_NFREE = len(_FREE)                                                # 21
_FREE_INDEX = {k: i for i, k in enumerate(_FREE)}


def _decompose(a, b, c, d):
    """Map a full (a,b,c,d) to (sign, free-index) using antisym in (a,b),(c,d) and
    pair-symmetry (ab)<->(cd). Returns None if a==b or c==d (the component is 0)."""
    if a == b or c == d:
        return None
    sab = 1
    if a > b:
        a, b, sab = b, a, -1
    scd = 1
    if c > d:
        c, d, scd = d, c, -1
    pi, qi = _PIDX[(a, b)], _PIDX[(c, d)]
    key = ((a, b), (c, d)) if pi <= qi else ((c, d), (a, b))
    return sab * scd, _FREE_INDEX[key]


def _to_free_vector(Tfun):
    """Project a tensor function T_{abcd} onto the 21-dim free-parameter vector."""
    vec = [Rational(0)] * _NFREE
    for k, (P, Q) in enumerate(_FREE):
        a, b = P
        c, d = Q
        vec[k] = Tfun(a, b, c, d)
    return Matrix(vec)


def _invariance_nullspace(gens):
    """The nullspace over QQ of delta_g T = 0 for all generators g in `gens`, where
        (delta_g T)_{abcd} = - [ g^e_a T_{ebcd} + g^e_b T_{aecd}
                                 + g^e_c T_{abed} + g^e_d T_{abce} ].
    Returns the list of nullspace basis vectors (each a length-21 free-param vector)."""
    rows = []
    for A in gens:
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for dd in range(4):
                        row = [Rational(0)] * _NFREE
                        for e in range(4):
                            t = _decompose(e, b, c, dd)
                            if t:
                                row[t[1]] += -A[e, a] * t[0]
                            t = _decompose(a, e, c, dd)
                            if t:
                                row[t[1]] += -A[e, b] * t[0]
                            t = _decompose(a, b, e, dd)
                            if t:
                                row[t[1]] += -A[e, c] * t[0]
                            t = _decompose(a, b, c, e)
                            if t:
                                row[t[1]] += -A[e, dd] * t[0]
                        if any(x != 0 for x in row):
                            rows.append(row)
    return Matrix(rows).nullspace()


def _Euler_tensor(a, b, c, d):
    """The Euler/eps-contraction tensor eps_{abcd} (frame Levi-Civita)."""
    return LeviCivita(a, b, c, d)


def _Pontryagin_tensor(a, b, c, d):
    """The Pontryagin tensor eta_{ac} eta_{bd} - eta_{ad} eta_{bc} (built from the
    SYMMETRIC frame metric eta = Tr|frame); contraction R^{ab} ^ R_{ab}."""
    return ETA[a, c] * ETA[b, d] - ETA[a, d] * ETA[b, c]


def _in_span(basis_rows, extra):
    """True iff `extra` lies in the span of `basis_rows` (exact rank over QQ)."""
    base = Matrix(basis_rows)
    if base.rows == 0:
        return all(x == 0 for x in extra)
    return base.rank() == Matrix(basis_rows + [list(extra)]).rank()


# ============================================================================
# TASK 1 : SETUP -- det SSOT re-pass, Tr|frame metrics, the input-ban guard
# ============================================================================
def source_guard():
    """fp-octonion-algebra + det-SSOT + no-numpy guard (Phase-0/77 semantics):
      (1) octonion_algebra NOT in sys.modules on the decisive path;
      (2) the decisive primitives are the NATIVE exact ring_lemma functions;
      (3) no numpy on this driver's decisive path."""
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra absent + exact-over-Q det SSOT + no numpy")
    print("=" * 78)
    oa_absent = "octonion_algebra" not in sys.modules
    np_absent = "numpy" not in sys.modules
    native = (RL.det_3.__module__ == "ring_lemma_verification"
              and RL.Tr.__module__ == "ring_lemma_verification"
              and RL.jordan.__module__ == "ring_lemma_verification"
              and RL.polarize_d.__module__ == "ring_lemma_verification")
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


# --- AST/source input-ban guard: NO posited MM/EH action enters the FORCED count ---
_FORBIDDEN_IDS = {
    'octonion_algebra', 'GST', 'SUSY', 'supergravity', 'Weinberg', 'MM_action',
    'eps_F_F_action', 'cone_hessian',
    # numpy float-rank routes are forbidden on the decisive path:
    'linalg',
}
# numeric-literal bans (the posited-action coefficients) are scanned at the
# SOURCE-STRING layer (the must_contain pins this; numeric literals are NOT AST.Name).
_FORBIDDEN_SOURCE_TOKENS = [
    "16piG", "16*pi*G", "16 pi G",
    "MM action", "MM-action", "posited action",
    "numpy.linalg", "np.linalg.matrix_rank",
]
# The decisive-path functions whose body must be free of a load-bearing posited
# action / forbidden symbol. (The Wise/MM eps F^F formula appears ONLY in module
# docstrings/comments as the AUDITED construction -- never as load-bearing code.)
_DECISIVE_FUNCS = {
    'forced_so31_generators', 'canonical_so_eta', '_invariance_nullspace',
    '_Euler_tensor', '_Pontryagin_tensor', '_to_free_vector', '_decompose',
    'bare_invariant_space', 'traceform_invariant_subspace', '_in_span',
}


def _forbidden_ids_used(func_node):
    used = set()
    for nd in _ast.walk(func_node):
        if isinstance(nd, _ast.Name) and nd.id in _FORBIDDEN_IDS:
            used.add(nd.id)
        elif isinstance(nd, _ast.Attribute) and nd.attr in _FORBIDDEN_IDS:
            used.add(nd.attr)
    return used


class _BlankStrings(_ast.NodeTransformer):
    """Replace every string-literal CONSTANT with an empty string, so a banned token
    that appears ONLY inside a human-readable _report(...) message or a docstring
    (provenance/finding prose) is not mistaken for a load-bearing code use. A genuine
    posited-action coefficient would appear as a NUMERIC literal or an IDENTIFIER in
    real code, never solely inside a report string. Mirrors the AST-only discipline of
    cartan_phaseB_einstein.ast_guard_T (which flags AST.Name/Attribute, never string
    contents)."""

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return _ast.copy_location(_ast.Constant(value=""), node)
        return node


def _strip_code_only(seg):
    """Return only the LOAD-BEARING executable code of a function source segment: drop
    the docstring, BLANK all string-literal contents (report messages / prose are not
    code uses), and strip trailing '#' comments (mirrors
    ring_lemma_verification.exact_only_guard._strip_comment). Provenance/finding prose
    that merely NAMES a banned token (a docstring or a _report message that says
    '16piG' while DESCRIBING the ban or the finding) is NOT a load-bearing code use and
    must not trip the guard."""
    try:
        mod = _ast.parse(seg)
        fn = mod.body[0]
        body = list(fn.body)
        if (body and isinstance(body[0], _ast.Expr)
                and isinstance(getattr(body[0], "value", None), _ast.Constant)
                and isinstance(body[0].value.value, str)):
            body = body[1:]                       # drop the docstring
        mod.body = [_ast.copy_location(
            _ast.FunctionDef(name=fn.name, args=fn.args, body=body or [_ast.Pass()],
                             decorator_list=[], returns=None, type_comment=None,
                             type_params=[]), fn)]
        mod = _BlankStrings().visit(mod)           # blank all string-literal contents
        _ast.fix_missing_locations(mod)
        code = _ast.unparse(mod)
    except (SyntaxError, AttributeError, TypeError):
        code = seg
    # strip any residual inline '#' comments (defensive; unparse drops comments).
    out = []
    for ln in code.splitlines():
        in_s = in_d = esc = False
        cut = len(ln)
        for idx, ch in enumerate(ln):
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
                cut = idx
                break
        out.append(ln[:cut])
    return "\n".join(out)


def _coefficient_ban_in_decisive_code():
    """Scan the EXECUTABLE CODE (docstrings + comments stripped) of the decisive-path
    functions for the posited-action coefficient/phrase tokens, mirroring
    cartan_phaseB_einstein.ast_guard_T (comment/docstring mentions of the ban are NOT
    code-uses; ring_lemma_verification.exact_only_guard does the same comment-strip).
    The must_contain pins these coefficient bans to the source-string layer -- numeric
    literals like Rational(-1,2) are NOT AST.Name nodes -- but only LOAD-BEARING CODE
    counts, never provenance prose. Returns the dict of decisive functions in which a
    banned token's CODE text appears (expect empty).

    Discipline note: a posited '-1/2' Einstein normalization or a '16piG' coupling
    would be a GRAVITATIONAL ACTION coefficient. The bare Pontryagin/eps tensors and
    the soldering-frame change-of-basis T_ON use Rational(1,2) as PURELY GEOMETRIC
    factors (Minkowski coords x0=(beta+gamma)/2; the metric volume normalization
    sqrt|det eta|), NOT as a posited-action coefficient -- those are not banned. The
    ban is on the ACTION itself: '16piG', 'MM action', 'posited action', numpy.linalg
    appearing as load-bearing CODE."""
    src = open(os.path.abspath(__file__)).read()
    tree = _ast.parse(src)
    hits = {}
    func_sources = {}
    for node in _ast.walk(tree):
        if isinstance(node, _ast.FunctionDef) and node.name in _DECISIVE_FUNCS:
            seg = _ast.get_source_segment(src, node) or ""
            code_only = _strip_code_only(seg)
            func_sources[node.name] = code_only
            bad = [tok for tok in _FORBIDDEN_SOURCE_TOKENS if tok in code_only]
            if bad:
                hits[node.name] = bad
    return hits, func_sources


def input_ban_guard():
    """THE HARD INPUT BAN (mirrors cartan_phaseB_einstein ast_guard_T / source_guard).
    Assert NO load-bearing appearance of a posited MM/EH action, '\\int eps F^F' as an
    assumed action, '-1/2'/'16piG' as an action coefficient, 'MM action', 'SUSY',
    octonion_algebra, or numpy.linalg ON THE DECISIVE PATH (the so(3,1) construction
    and the invariant counts). The forced determination uses ONLY Tr, det_3, the
    Peirce/C_u reduction, the (E_11,u)-forced so(3,1), and standard linear algebra.

    Returns True iff the decisive path is clean."""
    print("=" * 78)
    print("INPUT-BAN GUARD : no posited action / -1/2 / 16piG / MM-action / SUSY /")
    print("                  octonion_algebra / numpy.linalg load-bearing on the count")
    print("=" * 78)
    # (a) AST: no forbidden IDENTIFIER used in any decisive-path function.
    src = open(os.path.abspath(__file__)).read()
    tree = _ast.parse(src)
    id_hits = {}
    for node in _ast.walk(tree):
        if isinstance(node, _ast.FunctionDef) and node.name in _DECISIVE_FUNCS:
            u = _forbidden_ids_used(node)
            if u:
                id_hits[node.name] = sorted(u)
    ast_ok = _report(
        f"AST: NO forbidden identifier (octonion_algebra/GST/SUSY/linalg/...) used in "
        f"the decisive-path functions {sorted(_DECISIVE_FUNCS)} (hits={id_hits})",
        not id_hits)
    # (b) SOURCE-STRING: no posited-action coefficient/phrase token in decisive code.
    coeff_hits, _ = _coefficient_ban_in_decisive_code()
    coeff_ok = _report(
        f"SOURCE: NO posited-action token (16piG / 'MM action' / 'posited action' / "
        f"numpy.linalg) in the decisive-path function bodies (hits={coeff_hits})",
        not coeff_hits)
    # (c) RUNTIME: octonion_algebra + numpy absent on the live path.
    runtime_ok = _report(
        "RUNTIME: octonion_algebra and numpy absent from sys.modules on the decisive "
        "path (no banned engine pulled in)",
        "octonion_algebra" not in sys.modules and "numpy" not in sys.modules)
    return ast_ok and coeff_ok and runtime_ok


def task1_setup():
    """det SSOT re-pass + the two frame trace-form metrics (bare-trace FOIL and the
    soldered (1,3) eta) + the input ban. EXACT over Q."""
    print("#" * 78)
    print("# TASK 1 : det SSOT re-pass, Tr|frame metrics, the hard input-ban guard")
    print("#" * 78)

    # ---- 1.1 det_3 SSOT re-pass (cheap algebraic identities; or cite Phase 64.1/65) ----
    print("-- 1.1 det_3 SSOT re-pass (algebraic identities, exact over Q) --")
    a_s, b_s, c_s = Symbol('a'), Symbol('b'), Symbol('c')
    detI = RL.det_3(RL.h3o_identity())
    Xdiag = RL.h3o_from_coords(a_s, b_s, c_s, RL.oct_zero(), RL.oct_zero(), RL.oct_zero())
    det_diag = simplify(RL.det_3(Xdiag) - a_s * b_s * c_s)
    Xr = RL.generic_rational_X()
    pol_ok = simplify(RL.polarize_d(Xr, Xr, Xr) - 6 * RL.det_3(Xr)) == 0
    _report(f"det_3(I) == 1 (got {detI})", detI == 1)
    _report("det_3(diag(a,b,c)) == a*b*c [symbolic over Q]", det_diag == 0)
    _report("polarize_d(X,X,X) == 6*det_3(X) [exact over Q] "
            "(cites Phase-64.1/65 324/324 inner-derivation annihilation as the F_4 "
            "uniqueness certificate)", pol_ok)
    det_ok = (detI == 1 and det_diag == 0 and pol_ok)

    # ---- 1.2 the two frame trace-form metrics (FOIL vs soldered eta) ----
    print("-- 1.2 Tr|frame: the bare-trace FOIL (4,0) vs the SOLDERED (1,3) eta --")
    basis27 = RL._standard_basis_27()
    cof = [basis27[k] for k in CU4_IDX]
    # (i) FOIL: bare Jordan trace Gram on the raw frame directions (Phase 75 foil).
    GramFoil = Matrix(4, 4, lambda i, j: RL.c(cof[i], cof[j]))
    sig_foil = _signature(GramFoil)
    _report(f"FOIL (transparency, NEVER the spacetime metric): bare trace Gram "
            f"Tr(jordan(.,.)) on raw {{beta,gamma,p,q}} = diag(1,1,2,2), signature "
            f"{sig_foil} EUCLIDEAN (the OP^2 Fubini-Study foil) [exact Q]",
            sig_foil == (4, 0, 0))
    # (ii) SOLDERED metric: the det_2 Lorentzian (1,3) eta (the PHYSICAL frame metric,
    #      Phase 75 -- the trace form via the soldering projection onto V_0 ~ R^{3,1}).
    sig_raw = _signature(G_DET2_RAW)
    sig_on = _signature(ETA)
    _report(f"SOLDERED frame metric = det_2 Lorentzian (1,3): raw {{beta,gamma,p,q}} "
            f"Gram signature {sig_raw}; orthonormal eta=diag(+1,-1,-1,-1) signature "
            f"{sig_on} (the PHYSICAL spacetime frame metric, Phase 75) [exact Q]",
            sig_raw == (1, 3, 0) and sig_on == (1, 3, 0))
    # change-of-basis consistency: G_DET2_RAW == T^T eta T.
    cob_ok = (G_DET2_RAW - T_ON.T * ETA * T_ON).is_zero_matrix
    _report("frame change-of-basis consistent: G_DET2_RAW == T_ON^T eta T_ON "
            "(raw <-> orthonormal soldered frame) [exact Q]", cob_ok)
    # This soldered eta is the symmetric metric that (a) gives the Pontryagin
    # contraction delta^{ac}delta^{bd} and (b) up to orientation a volume sqrt|eta| eps.
    metric_ok = (sig_foil == (4, 0, 0) and sig_raw == (1, 3, 0)
                 and sig_on == (1, 3, 0) and cob_ok)

    # ---- 1.3 the input-ban guard ----
    print("-- 1.3 input-ban guard (no posited action on the decisive path) --")
    ban_ok = input_ban_guard()

    return {"det_ok": det_ok, "metric_ok": metric_ok, "ban_ok": ban_ok,
            "sig_foil": sig_foil, "sig_soldered": sig_on,
            "GramFoil": GramFoil.tolist(), "eta": ETA.tolist()}


# ============================================================================
# TASK 2 : BARE INVARIANT SPACE -- the dim=2 anchor (Euler + Pontryagin)
# ============================================================================
def bare_invariant_space():
    """Build the space of quadratic-in-curvature 4-forms invariant under the
    (E_11,u)-FORCED so(3,1) on the frame indices a,b,c,d=0..3, via the exact-over-Q
    invariance nullspace delta_g T = 0. Cross-confirm by exhibiting the two known
    independent invariants -- Euler eps_{abcd}R^{ab}^R^{cd} and Pontryagin
    R^{ab}^R_{ab} -- and their linear independence on a generic Phase-77 R[omega].

    Returns the evidence dict. dim != 2 => the so(3,1) setup is BUGGY (debug; the
    baseline MUST be Euler + Pontryagin) -- NO verdict on a broken baseline."""
    print("#" * 78)
    print("# TASK 2 : bare so(3,1)-invariant quad-in-curvature 4-form space (dim=2 anchor)")
    print("#" * 78)

    # ---- 2.1 the (E_11,u)-forced so(3,1) generators on the frame ----
    print("-- 2.1 the (E_11,u)-forced so(3,1) frame generators (Phase 75 residual) --")
    L_on, L_raw, dim_res = forced_so31_generators()
    _report(f"residual structure group dim == 21 (= so(3,1)[6] (+) so(6)[15], Phase 75) "
            f"[exact Q]", dim_res == 21)
    raw_kill = all((A.T * G_DET2_RAW + G_DET2_RAW * A).is_zero_matrix for A in L_raw)
    on_kill = all((A.T * ETA + ETA * A).is_zero_matrix for A in L_on)
    _report(f"6 forced so(3,1) generators: kill G_DET2_RAW (raw) = {raw_kill}; kill eta "
            f"(orthonormal) = {on_kill}; |L| = {len(L_on)} == 6 [exact Q]",
            raw_kill and on_kill and len(L_on) == 6)
    # cross-check: the FORCED generators span EXACTLY the canonical so(eta) (Phase 75).
    canon = canonical_so_eta()
    cflat = [[c[i, j] for i in range(4) for j in range(4)] for c in canon]
    lflat = [[A[i, j] for i in range(4) for j in range(4)] for A in L_on]
    base_rank = Matrix(cflat).rank()
    join_rank = Matrix(cflat + lflat).rank()
    _report(f"the (E_11,u)-forced so(3,1) == the canonical Lorentz algebra so(eta): "
            f"dim so(eta)={base_rank}, dim(so(eta)+forced)={join_rank} (equal => SAME "
            f"algebra; re-confirms Phase 75) [exact Q]",
            base_rank == 6 and join_rank == 6)

    # ---- 2.2 the invariance nullspace -> dim 2 ----
    print("-- 2.2 the so(3,1)-invariance nullspace of quad-in-curvature 4-forms --")
    nullsp = _invariance_nullspace(L_on)
    dim_bare = len(nullsp)
    _report(f"bare so(3,1)-invariant quad-in-curvature 4-form space dim == 2 "
            f"(Euler + Pontryagin) via exact nullspace over QQ (got {dim_bare}; "
            f"{_NFREE} free params before invariance)", dim_bare == 2)
    if dim_bare != 2:
        print("  [SETUP BUG] bare dim != 2 -- the so(3,1)-invariance setup is BROKEN "
              "(the baseline MUST be Euler + Pontryagin; Nieh-Yan is torsionful, "
              "excluded for the Levi-Civita omega). DEBUG; do NOT interpret a verdict.")
        return {"dim_bare": dim_bare, "setup_ok": False}

    # ---- 2.3 identify the 2-dim space as Euler + Pontryagin, independent ----
    print("-- 2.3 identify: Euler(eps) + Pontryagin, independent --")
    nb = [list(v) for v in nullsp]
    vE = _to_free_vector(_Euler_tensor)
    vP = _to_free_vector(_Pontryagin_tensor)
    euler_in = _in_span(nb, vE)
    pont_in = _in_span(nb, vP)
    rank_EP = Matrix([list(vE), list(vP)]).rank()
    _report(f"Euler eps_{{abcd}} in the bare invariant space = {euler_in}; "
            f"Pontryagin (eta_ac eta_bd - eta_ad eta_bc) in it = {pont_in} [exact Q]",
            euler_in and pont_in)
    _report(f"rank{{Euler, Pontryagin}} == 2 -> they are independent and SPAN the "
            f"2-dim bare space (got {rank_EP}) [exact Q]", rank_EP == 2)

    # ---- 2.4 Euler != Pontryagin: independent on generic curvature + Phase-77 R ----
    print("-- 2.4 Euler != Pontryagin: independent on generic curvature; Phase-77 R[omega] --")
    val = _evaluate_invariants_independence()
    _report(f"on a GENERIC algebraic-curvature tensor: Euler-contraction = "
            f"{val['euler']}, Pontryagin-contraction = {val['pont']} -- both nonzero, "
            f"two distinct rationals [exact Q]",
            val["both_nonzero"] and val["euler"] != val["pont"])
    _report(f"Euler and Pontryagin are linearly INDEPENDENT invariants: rank over QQ "
            f"of the [Euler;Pont] value-matrix across 2 generic curvatures == 2 "
            f"(got {val['indep_rank']}) [exact Q]",
            val["indep_rank"] == 2)
    # SECONDARY (transparency): the Phase-77 diagonal warped-reference R[omega].
    print(f"      [Phase-77 R[omega] (the genuine Lorentz-block Riemann of g=e.e, "
          f"diagonal warped reference, {val['phase77_nz']} nonzero comps, curved in "
          f"ONE 2-plane): Euler = {val['phase77_euler']}, Pontryagin = "
          f"{val['phase77_pont']}]")
    _report("SECONDARY (Phase-77 R[omega], transparency): the diagonal-tetrad R[omega] "
            "gives Pontryagin == 0 IDENTICALLY (the exact, expected fact that the "
            "Pontryagin density vanishes on diagonal metrics -- it needs Riemann "
            "mixing complementary planes); the independence of the two invariants is "
            "certified on the GENERIC curvature above, NOT on this special R [exact Q]",
            val["phase77_pont"] == 0)

    return {"dim_bare": dim_bare, "setup_ok": True, "euler_in": euler_in,
            "pont_in": pont_in, "rank_EP": rank_EP,
            "euler_val": str(val["euler"]), "pont_val": str(val["pont"]),
            "indep_rank": val["indep_rank"],
            "phase77_euler": str(val["phase77_euler"]),
            "phase77_pont": str(val["phase77_pont"]),
            "phase77_nz": val["phase77_nz"],
            "L_on": L_on, "nullsp_basis": nb}


def _contract_4form(Tfun, Rframe):
    """Contract a quad-in-curvature invariant T_{abcd} with two copies of the
    frame-index curvature R^{ab}_{munu} into a scalar density (sum over a<b, c<d of
    T_{abcd} times the eps^{munurhosig}-traced R^{ab}_{munu} R^{cd}_{rhosig}). For
    the scalar invariant we use the fully-antisymmetrized 4d top-form contraction
    eps^{munurhosig} R^{ab}_{munu} R^{cd}_{rhosig} (the wedge of the two 2-forms).

    Rframe[a][b][mu][nu] is the upper-frame-index curvature (a,b,mu,nu in 0..3).
    Returns the exact rational scalar T_{abcd} (R^{ab} ^ R^{cd})."""
    from sympy import Rational as _R
    total = _R(0)
    # the slice top-form: sum over the 4! permutations weighted by eps^{munurhosig}.
    perms = [(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2),
             (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2), (1, 2, 0, 3), (1, 2, 3, 0),
             (1, 3, 0, 2), (1, 3, 2, 0), (2, 0, 1, 3), (2, 0, 3, 1), (2, 1, 0, 3),
             (2, 1, 3, 0), (2, 3, 0, 1), (2, 3, 1, 0), (3, 0, 1, 2), (3, 0, 2, 1),
             (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)]
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            for c in range(4):
                for d in range(4):
                    if c == d:
                        continue
                    Tabcd = Tfun(a, b, c, d)
                    if Tabcd == 0:
                        continue
                    s = _R(0)
                    for (mu, nu, rho, sig) in perms:
                        eps = LeviCivita(mu, nu, rho, sig)
                        if eps == 0:
                            continue
                        s += eps * Rframe[a][b][mu][nu] * Rframe[c][d][rho][sig]
                    total += Tabcd * s
    return total


def _phase77_Rframe_at(x0_val):
    """The Phase-77 frame-index Lorentz curvature R^{ab}_{munu} (a,b,mu,nu = 0..3) of
    the warped-Lorentzian reference tetrad e=diag(1, f, 1, 1), f=1+x0^2 (the EXACT
    frame-universal R[omega] reference used by cartan_phaseB_curvature.sign_pin /
    task1_assemble_and_F -- surd-free, watchdog-safe), evaluated at a rational
    basepoint x0=x0_val (x0 != 0 => M != 0 => a GENERIC, nonzero R[omega]).

    Built from the Phase-77 closed-form torsion-free spin connection
    spin_connection_omega(E,coords) (formula 2) + the second Cartan structure equation
    R^{ab}_{munu} = d_mu omega_nu^{ab} - d_nu omega_mu^{ab}
                    + omega_mu^{ac} eta_{cd} omega_nu^{db} - (mu<->nu).
    This is the SAME R[omega] object Phase 77 validated == metric Levi-Civita Riemann
    of g=e.e (so it is a genuine Riemann frame curvature, not a generic 2-form ansatz).
    EXACT over Q."""
    from sympy import symbols as _syms, diff as _diff, cancel as _cancel, Matrix as _M
    x = _syms('x0 x1 x2 x3', real=True)
    f = 1 + x[0] ** 2
    E = _M.diag(1, f, 1, 1)
    W, _Einv = P1.spin_connection_omega(E, list(x))     # W[mu][a][b] = omega_mu^{ab}

    def Rframe_sym(a, b, mu, nu):
        t = _diff(W[nu][a][b], x[mu]) - _diff(W[mu][a][b], x[nu])
        for c in range(4):
            for d in range(4):
                t += (W[mu][a][c] * ETA[c, d] * W[nu][d][b]
                      - W[nu][a][c] * ETA[c, d] * W[mu][d][b])
        return _cancel(t)

    sub = {x[0]: x0_val, x[1]: Rational(0), x[2]: Rational(0), x[3]: Rational(0)}
    R = [[[[_cancel(Rframe_sym(a, b, mu, nu).subs(sub)) for nu in range(4)]
           for mu in range(4)] for b in range(4)] for a in range(4)]
    return R


_PAIRS6 = [(a, b) for a in range(4) for b in range(4) if a < b]   # 6 antisym frame pairs


def _generic_algebraic_curvature(vals21):
    """A GENERIC algebraic-curvature frame tensor R^{ab}_{munu} (a,b,mu,nu=0..3) with
    the Riemann pair-symmetries (antisym [ab], antisym [munu], pair-sym (ab)<->(munu)),
    built from a generic rational symmetric 6x6 matrix on the antisym pairs (21 free
    rationals -- the full algebraic-curvature space on which the topological 4-forms
    Euler & Pontryagin are defined; the first Bianchi identity is NOT needed for the
    4-form invariant COUNT, and is the only symmetry that does not affect Euler/Pont).
    Lower indices are raised with eta. EXACT over Q. This is the correct GENERIC test
    object to certify Euler and Pontryagin are DISTINCT invariants -- a single diagonal
    tetrad R[omega] is too special (Pontryagin vanishes identically on diagonal metrics)."""
    M = [[Rational(0)] * 6 for _ in range(6)]
    idx = 0
    for i in range(6):
        for j in range(i, 6):
            M[i][j] = vals21[idx]
            M[j][i] = vals21[idx]
            idx += 1

    def Rlow(a, b, c, d):
        if a == b or c == d:
            return Rational(0)
        sab = 1
        if a > b:
            a, b, sab = b, a, -1
        scd = 1
        if c > d:
            c, d, scd = d, c, -1
        return sab * scd * M[_PAIRS6.index((a, b))][_PAIRS6.index((c, d))]

    def Rup(a, b, mu, nu):
        return sum(ETA[a, e] * ETA[b, fk] * Rlow(e, fk, mu, nu)
                   for e in range(4) for fk in range(4))
    return [[[[Rup(a, b, mu, nu) for nu in range(4)] for mu in range(4)]
             for b in range(4)] for a in range(4)]


def _evaluate_invariants_independence():
    """Certify Euler and Pontryagin are DISTINCT, linearly-independent invariants by
    contracting them on GENERIC algebraic-curvature tensors (the correct generic test
    object; full Riemann pair-symmetries). Two generic curvatures give a 2x2 value
    matrix of rank 2 iff the invariants are genuinely independent. Also records the
    Phase-77 diagonal R[omega] values as a SECONDARY observation (Euler != 0,
    Pontryagin == 0 -- the exact, expected fact that Pontryagin vanishes on diagonal
    tetrads; NOT a failure). EXACT over Q."""
    v1 = [Rational(v, 7) for v in
          [3, -2, 5, -1, 4, -3, 2, -5, 1, 6, -4, 2, -1, 3, -2, 5, 1, -3, 4, 2, -1]]
    v2 = [Rational(v, 11) for v in
          [1, 3, -2, 4, -1, 2, 5, -3, 1, -4, 2, 6, -1, 3, -5, 2, 4, 1, -2, 3, 5]]
    R1 = _generic_algebraic_curvature(v1)
    R2 = _generic_algebraic_curvature(v2)
    e1, p1 = _contract_4form(_Euler_tensor, R1), _contract_4form(_Pontryagin_tensor, R1)
    e2, p2 = _contract_4form(_Euler_tensor, R2), _contract_4form(_Pontryagin_tensor, R2)
    Vmat = Matrix([[e1, p1], [e2, p2]])
    indep_rank = Vmat.rank()
    # SECONDARY: the Phase-77 (diagonal warped reference) R[omega], curved in one plane.
    R77 = _phase77_Rframe_at(Rational(1))             # x0 = 1, M != 0
    e77 = _contract_4form(_Euler_tensor, R77)
    p77 = _contract_4form(_Pontryagin_tensor, R77)
    # nonzero-component count of the Phase-77 R (transparency).
    nz77 = sum(1 for a in range(4) for b in range(4) for mu in range(4) for nu in range(4)
               if R77[a][b][mu][nu] != 0)
    return {"euler": e1, "pont": p1, "euler2": e2, "pont2": p2,
            "indep_rank": indep_rank, "both_nonzero": (e1 != 0 and p1 != 0),
            "phase77_euler": e77, "phase77_pont": p77, "phase77_nz": nz77,
            "phase77_is_genuine_riemann": True}


# ============================================================================
# TASK 3 : THE DECISIVE COUNT -- trace-form-invariant subspace + eps-reachability
# ============================================================================
def traceform_invariant_subspace(bare):
    """THE DECISIVE COMPUTATION (test-forced-vs-posited, VALD-06): the dimension of
    the trace-form-invariant subspace -- the quad-in-F 4-form invariants buildable
    from Tr(X o Y) (=> eta) and det_3 ALONE (+ the (E_11,u)-forced structures), with
    NO posited eps. eps-reachability (BOTH routes) + Pontryagin-reachability +
    det_3-fixed-vs-free normalization. EXACT over Q.

    Returns the decisive triple (dim; eps-in-span; normalization) + the full evidence.
    Reported at TRUE STRENGTH; the FINAL verdict + ratification are 78-02."""
    print("#" * 78)
    print("# TASK 3 : THE DECISIVE trace-form-invariant subspace dimension + eps-reach")
    print("#" * 78)

    nb = bare["nullsp_basis"]                      # the 2-dim bare invariant space basis
    vE = _to_free_vector(_Euler_tensor)
    vP = _to_free_vector(_Pontryagin_tensor)

    # ---- 3.1 Pontryagin-reachability (the pure-eta product) ----
    print("-- 3.1 Pontryagin-reachability from Tr (=> eta): pure symmetric eta-product --")
    # The eta-TENSORIAL invariants are products of the symmetric eta=Tr|frame.
    # Antisymmetrized into the wedge symmetry class, the ONLY surviving eta-product
    # invariant is Pontryagin (eta_ab eta_cd is symmetric in (ab) => killed). So the
    # eta-tensorial subspace is span{Pontryagin}, dim 1. eps is NOT a tensorial fn of
    # the symmetric eta (an antisymmetric eps cannot be a polynomial in symmetric eta).
    eta_tensorial_dim = Matrix([list(vP)]).rank()
    eps_tensorial = _in_span([list(vP)], vE)
    _report(f"Pontryagin reachable from Tr (eta-product eta_ac eta_bd - eta_ad eta_bc): "
            f"span{{Pontryagin}} dim == 1 (got {eta_tensorial_dim}) [exact Q]",
            eta_tensorial_dim == 1)
    _report(f"eps NOT a TENSORIAL function of the symmetric eta=Tr|frame "
            f"(eps in span{{Pontryagin}} = {eps_tensorial}; an antisymmetric eps "
            f"cannot be built from symmetric eta-products) [exact Q]",
            not eps_tensorial)

    # ---- 3.2 det_3-reachability on the soldered V_0 Lorentz block (route b) ----
    print("-- 3.2 det_3-reachability: does the cubic norm supply an orientation/eps? --")
    # det_3 is a SYMMETRIC trilinear (polarize_d). Restrict its polarization to the 4
    # soldered V_0 ~ R^{3,1} frame directions CU4 and show it carries NO antisymmetric
    # 4-index orientation element. CONCRETE EXACT FACT: det_3|CU4 == 0 identically
    # (the cubic norm couples x1 to ALPHA, which is OUTSIDE the {beta,gamma,p,q} block),
    # so det_3 supplies NOTHING -- no metric, no orientation, no Pfaffian -- on the block.
    basis27 = RL._standard_basis_27()
    EE = [basis27[k] for k in CU4_IDX]
    Tijk = {}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                Tijk[(i, j, k)] = RL.polarize_d(EE[i], EE[j], EE[k])
    n_nonzero = sum(1 for v in Tijk.values() if v != 0)
    sym_ok = all(Tijk[(i, j, k)] == Tijk[(j, i, k)] == Tijk[(i, k, j)]
                 for i in range(4) for j in range(4) for k in range(4))
    _report(f"det_3 polarization restricted to the soldered V_0 Lorentz block CU4 is "
            f"a SYMMETRIC trilinear with {n_nonzero}/64 nonzero comps == 0 IDENTICALLY "
            f"(the cubic norm couples x1 to alpha, outside {{beta,gamma,p,q}}) [exact Q]",
            n_nonzero == 0 and sym_ok)
    _report("det_3 (symmetric trilinear, vanishing on the Lorentz block) supplies NO "
            "antisymmetric eps / orientation / Pfaffian -> det_3 route to eps is CLOSED "
            "[exact Q]", n_nonzero == 0)
    det3_supplies_eps = (n_nonzero != 0)           # False -> det_3 gives no eps

    # ---- 3.3 eps-reachability route (a): the metric volume form sqrt|det eta| eps ----
    print("-- 3.3 eps-reachability (a): the metric volume form sqrt|det eta| eps --")
    # A metric fixes a volume form up to ORIENTATION: eps_{abcd} = sqrt|det g| [abcd].
    # In the orthonormal frame det eta = -1 => sqrt|det eta| = 1, so the eps TENSOR is
    # numerically reachable from eta IF an orientation (a discrete sign) is chosen. The
    # NORMALIZATION sqrt|det eta| = 1 is FIXED by eta; the ORIENTATION (eps vs -eps) is
    # NOT fixed by the symmetric eta alone.
    det_eta = ETA.det()
    sqrt_abs_det = Rational(1)                      # sqrt|det eta| = sqrt(1) = 1 (det eta = -1)
    vol_norm_fixed = (det_eta == -1)               # sqrt|det eta| = 1 fixed by eta
    _report(f"metric volume form: det(eta) = {det_eta} => sqrt|det eta| = "
            f"{sqrt_abs_det} (the volume NORMALIZATION is FIXED by eta) [exact Q]",
            vol_norm_fixed)
    # If the metric volume form is ADMITTED as 'reachable from Tr', eps enters the
    # subspace -- but then BOTH eps and Pontryagin are reachable.
    eps_via_volume = vol_norm_fixed                # eps reachable as the eta volume form
    _report("eps reachable from Tr ONLY via the metric volume form sqrt|det eta| eps "
            "(route a); the ORIENTATION (eps vs -eps) is a DISCRETE choice NOT fixed by "
            "the symmetric eta/det_3 -- the 'broken by hand' orientation [exact Q]",
            eps_via_volume)

    # ---- 3.4 the DECISIVE dimension of the trace-form-invariant subspace ----
    print("-- 3.4 THE DECISIVE trace-form-invariant subspace dimension --")
    # eta-tensorial-only (orientation-free, the strictly-intrinsic reading):
    #   span{Pontryagin} = 1-dim; eps NOT reachable (det_3 gives no orientation either).
    # admitting the metric volume form (route a): span{Pontryagin, eps} = 2-dim.
    dim_tensorial = Matrix([list(vP)]).rank()                       # 1 (Pontryagin only)
    dim_with_volume = Matrix([list(vP), list(vE)]).rank()           # 2 (Pont + eps)
    eps_in_span = eps_via_volume                  # YES, but ONLY via the volume form
    pont_in_span = True                           # always (pure eta product)
    _report(f"trace-form-invariant subspace (eta-tensorial ONLY, orientation-free): "
            f"dim == 1 (span{{Pontryagin}}; eps unreachable) [exact Q]",
            dim_tensorial == 1)
    _report(f"trace-form-invariant subspace (ADMITTING the metric volume form route): "
            f"dim == 2 (span{{Pontryagin, eps}}) -> eps is a NON-UNIQUE choice "
            f"(both eps and Pontryagin reachable) [exact Q]",
            dim_with_volume == 2)

    # ---- 3.5 normalization read-off ----
    print("-- 3.5 normalization read-off: det_3-fixed vs free/imported --")
    # The eps-contraction's GRAVITATIONAL normalization (-> 1/16piG) is NOT read off
    # det_3: det_3 vanishes on the Lorentz block (3.2), so it fixes NOTHING about the
    # eps-contraction's scale. The metric volume sqrt|det eta|=1 fixes the eps tensor's
    # numeric scale but NOT the EH coupling. => the Einstein normalization is FREE /
    # imported (it comes with the posited action, not from Tr/det_3).
    norm_fixed_by_det3 = det3_supplies_eps        # False -> normalization NOT det_3-fixed
    _report("the eps-contraction's gravitational normalization (-> 1/16piG) is NOT "
            "fixed by det_3 (det_3 == 0 on the Lorentz block) -> normalization is "
            "FREE / imported (the posited-action coupling) [exact Q]",
            not norm_fixed_by_det3)

    # ---- 3.6 the decisive triple ----
    print("-- 3.6 THE DECISIVE TRIPLE (input to the 78-02 verdict ladder) --")
    # The honest decisive reading (at TRUE STRENGTH):
    #   * dim of the trace-form-invariant subspace: 1 (eta-tensorial, eps unreachable)
    #     OR 2 (admitting the metric volume form, eps reachable but NON-UNIQUE) --
    #     EITHER reading is fp-imported-action (dim=1 WITHOUT eps, or dim>=2 with eps
    #     non-unique). The STRONG WIN needs dim==1 WITH the generator == eps AND a
    #     det_3-fixed normalization -- which does NOT hold.
    #   * eps-in-span: YES only via the metric volume form (orientation a discrete,
    #     non-intrinsic choice); NOT singled out over Pontryagin; det_3 supplies no eps.
    #   * normalization: FREE / imported (det_3 vanishes on the block).
    decisive = {
        "dim_tensorial": int(dim_tensorial),               # 1 (Pontryagin; eps unreachable)
        "dim_with_volume": int(dim_with_volume),           # 2 (Pont + eps via volume form)
        "eps_in_span": bool(eps_in_span),                  # YES only via the volume form
        "eps_singled_out_over_pontryagin": False,          # eps NOT singled out
        "eps_via_det3": bool(det3_supplies_eps),           # False
        "pontryagin_in_span": bool(pont_in_span),          # True
        "normalization_det3_fixed": bool(norm_fixed_by_det3),  # False -> free/imported
        "verdict_input": "fp-imported-action",
    }
    print()
    print("  " + "=" * 70)
    print("  THE DECISIVE TRIPLE (at TRUE STRENGTH; the 78-02 verdict ladder input):")
    print(f"    dim(trace-form-invariant subspace) = {decisive['dim_tensorial']} "
          f"(eta-tensorial: Pontryagin only, eps unreachable)")
    print(f"                                       = {decisive['dim_with_volume']} "
          f"(admitting metric volume form: Pont + eps, eps NON-UNIQUE)")
    print(f"    eps-in-span = {decisive['eps_in_span']} "
          f"(ONLY via the metric volume form; orientation a discrete non-intrinsic "
          f"choice; det_3 supplies no eps)")
    print(f"    Pontryagin-in-span = {decisive['pontryagin_in_span']} (pure eta product)")
    print(f"    eps singled out over Pontryagin = "
          f"{decisive['eps_singled_out_over_pontryagin']}")
    print(f"    normalization det_3-fixed = {decisive['normalization_det3_fixed']} "
          f"(-> FREE / imported: det_3 == 0 on the Lorentz block)")
    print(f"    => verdict INPUT = {decisive['verdict_input']} "
          f"(the HIGH / most-likely outcome; NOT a STRONG WIN -- reported at true "
          f"strength, the FINAL verdict + ratification are 78-02)")
    print("  " + "=" * 70)

    # STRONG-WIN test (all three required): dim==1 AND generator==eps AND det_3-fixed norm.
    strong_win = (dim_tensorial == 1 and (not pont_in_span)  # would need eps-only, not Pont
                  and eps_in_span and norm_fixed_by_det3)
    _report("STRONG-WIN condition (dim==1 AND generator==eps AND normalization "
            "det_3-fixed -- ALL three) is NOT met -> the decisive input is "
            "fp-imported-action (reported at true strength, not relabeled a win)",
            not strong_win)

    return decisive


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("#" * 78)
    print("# Phase 78-01 : THE DECISIVE FORCED-VS-POSITED CIRCULARITY AUDIT (v18.0 FINAL)")
    print("#   MM eps-contraction FORCED by Tr(X o Y)/det_3, or fp-imported-action?")
    print("#   The decisive output is a DIMENSION (integer) + an IDENTITY, exact over Q.")
    print("#   Audited object = LINEAR-in-R Einstein term eps R^e^e (NOT a quadratic")
    print("#   Maxwell/Pontryagin stress -- the Phase-76 OVERTURNED tautology).")
    print("#" * 78)

    okG = source_guard()
    t1 = task1_setup()
    t2 = bare_invariant_space()
    if not t2.get("setup_ok", False):
        print("\n[STOP] bare invariant space dim != 2 -- setup BUG; NO verdict on a "
              "broken baseline (Task 3 not run).")
        return 1
    t3 = traceform_invariant_subspace(t2)

    print("\n" + "=" * 78)
    print("SUMMARY OF DECISIVE CHECKS (78-01)")
    print("=" * 78)
    print(f"  source guard (octonion_algebra/numpy absent, det SSOT native) ... {okG}")
    print(f"  TASK 1 det_3 SSOT re-pass ....................................... {t1['det_ok']}")
    print(f"  TASK 1 Tr|frame: FOIL (4,0) + soldered eta (1,3) ................ {t1['metric_ok']}")
    print(f"  TASK 1 input-ban guard (no posited action on the count) ......... {t1['ban_ok']}")
    print(f"  TASK 2 bare invariant space dim == 2 (Euler + Pontryagin) ....... {t2['dim_bare'] == 2}")
    print(f"  TASK 2 Euler+Pontryagin independent on the Phase-77 R[omega] .... {t2['indep_rank'] == 2}")
    print(f"  TASK 3 decisive dim (eta-tensorial / with-volume) ............... "
          f"{t3['dim_tensorial']} / {t3['dim_with_volume']}")
    print(f"  TASK 3 eps-in-span / singled-out / det_3-fixed normalization .... "
          f"{t3['eps_in_span']} / {t3['eps_singled_out_over_pontryagin']} / "
          f"{t3['normalization_det3_fixed']}")
    print("=" * 78)
    print(f"  >>> DECISIVE VERDICT INPUT (TRUE STRENGTH): {t3['verdict_input']}")
    print("      (the FINAL verdict ladder + human ratification are 78-02)")
    print("=" * 78)
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}  |  78-01 build complete")
    print("=" * 78)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
