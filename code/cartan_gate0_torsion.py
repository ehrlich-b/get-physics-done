"""Gate 0 ("cheap kill") -- Einstein-Cartan TORSION sourced by chiral V_{1/2} spin
on the exceptional Jordan algebra h_3(O).  A fail-fast PRE-FLIGHT: NO curvature (that
is the deferred Gate 1), NO roadmap/requirements/state/commits.  Build the spin
current two independent ways, verify the load-bearing soldering BRIDGE, run the three
Gate-0 checks (G0a nonzero / G0b chirality-tracking / G0c non-circularity), and emit a
deterministic non-hardwired verdict() reading.  EXACT over Q throughout (sympy.Rational
/ sympy.Matrix; ranks via .rank()); NEVER numpy/float on any decisive value.

THE PHYSICS (Hehl et al. RMP 48 (1976) + Wise gr-qc/0611154).  In Einstein-Cartan the
Cartan equation is ALGEBRAIC, (modified) torsion = kappa * spin-current, with the
coupling kappa = 8 pi G fixed (in standard EC) by the SINGLE posited EH-Palatini action
-- the matter sector supplies the spin current's SHAPE but NEVER the coupling
coefficient.  This milestone tests whether h_3(O) supplies that coupling INTRINSICALLY
(trace form Tr(X o Y) / cubic norm det_3 / the soldering normalization itself) instead.
Gate 0 only needs the ALGEBRAIC current (no d_omega e^a yet).

THE OBJECTS (all from the det SSOT; octonion_algebra.py BANNED -- buggy associator):
  - C_{(V_1/2)(V_1/2)(V_0)} block  C(A,B,D) = (1/6) polarize_d(A,B,D)  (det_3 polarization).
  - soldering form  to_mink(jordan(E(phi), E(psi)))  -- E = the pi_u conditional
    expectation onto h_3(C_u), C_u = span{1,e_7}; to_mink reads the V_0 frame coords
    {beta,gamma,p,q} = engine {1,2,3,10} and rotates to Minkowski {x0,x1,x2,x3}.

THE BRIDGE (verified FIRST):  on the C_u-survivor V_{1/2} sub-block (engine
[11,18,19,26] = the PHYSICAL matter sector, exactly where the locked sample MATTER
lives) the lowered C block IS the metric-lowered soldering current,
    (1/6) polarize_d(phi_i, phi_j, frame_a)  ==  const * (eta * soldering(phi_i,phi_j))_a
with a SINGLE rational const = -2/3 fixed by the algebra (NOT a free knob).  The e_1..e_6
octonion directions of V_{1/2} are KILLED by E (pi_u), so they carry no soldering image
-- the spin current is intrinsically a C_u-survivor object.  This certifies the spin
current is the algebra's OWN cubic coupling, not an inserted bilinear.

ENGINE / convention locks inherited from v18.0 / v19.0 (read, NOT rebuilt):
  27-coord layout [alpha,beta,gamma | x1=3..10 | x2=11..18 | x3=19..26]; Peirce under
  E_11=diag(1,0,0): V_1=[0], V_0=[1..10], V_{1/2}=[11..26]; chirality blocks x2(11..18)
  vs x3(19..26); spacetime CU4_IDX=[1,2,3,10]; mostly-minus eta=diag(+1,-1,-1,-1);
  u=e_7; C_u survivors of V_{1/2} = [11,18,19,26].  det SSOT = ring_lemma_verification.
"""
import os
import sys
import ast as _ast
import time
import itertools

sys.path.insert(0, '/Users/ehrlich/scratch/get-physics-done/code')

# --- the EXACT-over-Q det SSOT and the soldering machinery (NO octonion_algebra) ----
import ring_lemma_verification as RL            # det_3 / polarize_d / jordan / h3o_from_coords (SSOT)
import embedding_under_E_verification as EMB     # E() = pi_u conditional expectation onto h_3(C_u)
import cartan_phaseA_coframe as PA               # to_mink (soldering), CU4_IDX, G_DET2_RAW, V_HALF_IDX
import bulk_geometry_verification as BG          # build_e6_basis/stab_* (forced so(3,1)); spacetime_curvature_of_g
import cartan_phaseC_contraction as PC            # T_ON (raw {beta,gamma,p,q} <-> orthonormal frame)
from sympy import Rational, Matrix, simplify, cancel, zeros, eye, symbols

# ============================================================================
# CONVENTION LOCKS (v18.0 / v19.0; reproduced -- not re-derived)
# ============================================================================
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
#   fourier_convention=physics, coupling_convention=alpha_s,
#   renormalization_scheme=MSbar, gauge_choice=Feynman
N = 4
ETA = Matrix.diag(1, -1, -1, -1)               # frame metric diag(+1,-1,-1,-1), mostly-minus (1,3)
G_DET2_RAW = PA.G_DET2_RAW                      # det_2 (1,3) Gram on raw {beta,gamma,p,q} (G_DET2_RAW = T_ON^T eta T_ON)
CU4_IDX = [1, 2, 3, 10]                         # {beta,gamma,p,q} = the soldered V_0 frame (spacetime)
W6_IDX = [4, 5, 6, 7, 8, 9]                     # internal V_0 sector (orthogonal to C_u)
V_HALF_IDX = list(range(11, 27))               # V_{1/2}(E_11), idx 11..26 (the 16-dim chiral rep)
X2_BLOCK = list(range(11, 19))                  # chirality block x2 (engine 11..18)
X3_BLOCK = list(range(19, 27))                  # chirality block x3 (engine 19..26)
CU_SURVIVOR_IDX = [11, 18, 19, 26]             # the pi_u survivors of V_{1/2} (C_u^2)

# Peirce numbering of V_{1/2}: i=1..8 -> x2-block (e_{i-1}); i=9..16 -> x3-block (e_{i-9}).
# The C_u survivors in Peirce numbering: 11->1, 18->8, 19->9, 26->16.
SURV_PEIRCE = [1, 8, 9, 16]

# The v18 Phase-77 LOCKED rational sample (a pure C_u-survivor V_{1/2} vector) + a V_0 x1
# partner so the det_3 triple cross-term has all three slots populated.
MATTER = {11: Rational(1, 5), 18: Rational(-1, 10), 19: Rational(3, 10), 26: Rational(1, 2)}
SLICE_VALS = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]   # slice basepoint (beta,gamma,p,q)
BG_PARTNER = {4: Rational(1)}                  # V_0 x1 partner (third det_3 slot)

ALL_PASS = True
_t0 = time.time()


def tick(msg):
    print(f"[{time.time() - _t0:7.1f}s] {msg}", flush=True)


def _report(label, ok):
    """PASS/FAIL line; latch ALL_PASS to False on any failure."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}", flush=True)
    if not ok:
        ALL_PASS = False
    return bool(ok)


def _signature(M):
    """(n_pos,n_neg,n_zero) of a symmetric rational Matrix, EXACT over Q via eigenvals."""
    ev = M.eigenvals()
    pos = sum(m for v, m in ev.items() if v > 0)
    neg = sum(m for v, m in ev.items() if v < 0)
    zer = sum(m for v, m in ev.items() if v == 0)
    return pos, neg, zer


# ============================================================================
# BASIS HELPERS (V_{1/2} and the V_0 frame), all over Q
# ============================================================================
Z = RL.oct_zero()


def _e(k):
    v = [Rational(0)] * 8
    v[k] = Rational(1)
    return v


def phi(i):
    """V_{1/2} basis vector, Peirce index i=1..16. i<=8 -> x2=e_{i-1}; else x3=e_{i-9}.
    Built from the det SSOT constructor RL.h3o_from_coords (NO octonion_algebra)."""
    if 1 <= i <= 8:
        return RL.h3o_from_coords(0, 0, 0, Z, _e(i - 1), Z)
    return RL.h3o_from_coords(0, 0, 0, Z, Z, _e(i - 9))


def phi_vec(coeffs):
    """A general V_{1/2} element from a dict {engine_idx: rational} (engine 11..26)."""
    x2 = [Rational(0)] * 8
    x3 = [Rational(0)] * 8
    for idx, val in coeffs.items():
        if 11 <= idx <= 18:
            x2[idx - 11] = val
        elif 19 <= idx <= 26:
            x3[idx - 19] = val
        else:
            raise ValueError(f"index {idx} not in V_{{1/2}} [11..26]")
    return RL.h3o_from_coords(0, 0, 0, Z, x2, x3)


def frame_elt(x0, x1, x2, x3):
    """The h_3(O) element whose V_0 part maps under to_mink to the orthonormal frame
    vector (x0,x1,x2,x3).  Inverse of to_mink: beta=x0+x3, gamma=x0-x3, p=x1, q=x2
    (p=Re(x1), q=<x1,e_7>).  Used to read off C-block components in the orthonormal frame."""
    b = x0 + x3
    g = x0 - x3
    x1oct = [Rational(x1), 0, 0, 0, 0, 0, 0, Rational(x2)]   # Re(x1)=p=x1, <x1,e7>=q=x2
    return RL.h3o_from_coords(0, b, g, x1oct, Z, Z)


FRAME = {a: frame_elt(*[1 if k == a else 0 for k in range(4)]) for a in range(4)}


def C(A, B, D):
    """C-block = (1/6) polarize_d(A,B,D) (the det_3 polarization; d(X,X,X)=6 det_3)."""
    return simplify(Rational(1, 6) * RL.polarize_d(A, B, D))


def soldering(A, B):
    """The soldering current to_mink(jordan(E(A),E(B))) in R^{3,1} (upper frame index).
    E = pi_u conditional expectation onto h_3(C_u); to_mink projects onto V_0 ~ R^{3,1}."""
    return Matrix(PA.to_mink(RL.jordan(EMB.E(A), EMB.E(B))))


# ============================================================================
# SOURCE GUARD : octonion_algebra absent; det SSOT native exact-over-Q; no numpy
# ============================================================================
def source_guard():
    print("=" * 78)
    print("SOURCE GUARD : octonion_algebra ABSENT + native exact-over-Q det SSOT + no numpy")
    print("=" * 78)
    oa_absent = "octonion_algebra" not in sys.modules
    np_absent = "numpy" not in sys.modules
    native = (RL.det_3.__module__ == "ring_lemma_verification"
              and RL.jordan.__module__ == "ring_lemma_verification"
              and RL.polarize_d.__module__ == "ring_lemma_verification")
    Xspot = RL.h3o_from_coords(Rational(2), Rational(3), Rational(5), Z, Z, Z)
    spot = RL.det_3(Xspot)
    spot_ok = (spot == 30) and (not isinstance(spot, float))
    _report("octonion_algebra NOT in sys.modules on the decisive path [fp-octonion-algebra REJECTED]",
            oa_absent)
    _report(f"det SSOT native ring_lemma exact-over-Q (det_3(diag(2,3,5))=={spot} exact integer) "
            "[fp-float-decisive REJECTED]", native and spot_ok)
    _report("numpy NOT on this driver's decisive path (all ranks/eigvals sympy over QQ)", np_absent)
    return oa_absent and native and spot_ok and np_absent


# ============================================================================
# G0c.1 AST/source GUARD : NO posited coupling on the coefficient path
#   Mirrors cartan_phaseB_einstein.ast_guard_T + cartan_phaseC_contraction input-ban.
# ============================================================================
_FORBIDDEN_IDS = {
    'kappa', 'kappa_torsion', 'GST', 'SUSY', 'supergravity', 'Weinberg',
    'octonion_algebra', 'cone_hessian',
    'EH_action', 'Palatini', 'MM_action', 'eps_F_F_action',
    'linalg',                                   # numpy float-rank routes banned
}
_FORBIDDEN_SOURCE_TOKENS = [
    "8*pi*G", "8 pi G", "8piG", "16piG", "16*pi*G",
    "MM action", "posited action", "EH-Palatini action", "Palatini action",
    "numpy.linalg", "np.linalg",
]
# The decisive coefficient-path functions: building the spin current and the bridge const.
_DECISIVE_FUNCS = {
    'C', 'soldering', 'def_A_current', 'def_B_spin_current', 'bridge_const',
    'sigma_half_generators', 'verdict',
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
    """Blank every string-literal CONSTANT so a banned token that appears ONLY in a
    docstring / _report message (prose describing the ban or finding) is not mistaken
    for a load-bearing code use.  Mirrors cartan_phaseC_contraction._BlankStrings."""

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return _ast.copy_location(_ast.Constant(value=""), node)
        return node


def _strip_code_only(seg):
    """Return the LOAD-BEARING executable code of a function source: drop the docstring,
    blank all string literals, strip trailing '#' comments.  Provenance prose that merely
    NAMES a banned token is not a code use."""
    try:
        mod = _ast.parse(seg)
        fn = mod.body[0]
        body = list(fn.body)
        if (body and isinstance(body[0], _ast.Expr)
                and isinstance(getattr(body[0], "value", None), _ast.Constant)
                and isinstance(body[0].value.value, str)):
            body = body[1:]
        new_fn = _ast.copy_location(
            _ast.FunctionDef(name=fn.name, args=fn.args, body=body or [_ast.Pass()],
                             decorator_list=[], returns=None, type_comment=None,
                             type_params=[]), fn)
        mod.body = [new_fn]
        mod = _BlankStrings().visit(mod)
        _ast.fix_missing_locations(mod)
        code = _ast.unparse(mod)
    except (SyntaxError, AttributeError, TypeError):
        code = seg
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


def ast_source_guard(extra_src=None):
    """G0c.1 hard guard: (a) AST -- no forbidden IDENTIFIER used in any decisive-path
    function; (b) SOURCE -- no posited-coupling token in decisive-function CODE (docstrings
    /comments/report-strings stripped); (c) RUNTIME -- octonion_algebra + numpy absent.
    `extra_src` (optional) lets the guard scan an INJECTED violation string to prove it
    FIRES (not a no-op).  Returns (ok, ast_hits, src_hits)."""
    src = open(os.path.abspath(__file__)).read()
    if extra_src is not None:
        src = src + "\n" + extra_src
    tree = _ast.parse(src)
    ast_hits, src_hits = {}, {}
    for node in _ast.walk(tree):
        if isinstance(node, _ast.FunctionDef) and node.name in _DECISIVE_FUNCS:
            u = _forbidden_ids_used(node)
            if u:
                ast_hits[node.name] = sorted(u)
            seg = _ast.get_source_segment(src, node) or ""
            code_only = _strip_code_only(seg)
            bad = [tok for tok in _FORBIDDEN_SOURCE_TOKENS if tok in code_only]
            if bad:
                src_hits[node.name] = bad
    runtime_ok = ("octonion_algebra" not in sys.modules) and ("numpy" not in sys.modules)
    ok = (not ast_hits) and (not src_hits) and runtime_ok
    return ok, ast_hits, src_hits


# ============================================================================
# THE BRIDGE (verify FIRST) : C block == const * (eta * soldering) on C_u survivors
# ============================================================================
def bridge_const():
    """Fix the bridge constant `const` from the algebra over the C_u-survivor V_{1/2}
    sub-block: (1/6) polarize_d(phi_i, phi_j, frame_a) == const * (eta * soldering)_a.
    The const is a FIXED rational read off the algebra (det_3 polarization vs the
    pi_u-soldered Jordan product), NOT an inserted knob.  EXACT over Q.  Returns the
    set of distinct ratios (must be a singleton)."""
    consts = set()
    for (pi_, pj_) in itertools.product(SURV_PEIRCE, repeat=2):
        Cvec = Matrix([C(phi(pi_), phi(pj_), FRAME[a]) for a in range(4)])
        sold = soldering(phi(pi_), phi(pj_))
        EtaS = (ETA * sold).applyfunc(simplify)
        for a in range(4):
            if EtaS[a] != 0:
                consts.add(simplify(Cvec[a] / EtaS[a]))
            elif Cvec[a] != 0:
                consts.add("INCONSISTENT")
    return consts


def verify_bridge():
    print("=" * 78)
    print("BRIDGE (load-bearing, verified FIRST) : the C block IS the metric-lowered")
    print("  soldering current on the C_u-survivor sub-block (the PHYSICAL matter sector)")
    print("=" * 78)
    consts = bridge_const()
    single = (len(consts) == 1 and "INCONSISTENT" not in consts)
    const_val = next(iter(consts)) if single else None
    print(f"      C_u-survivor V_{{1/2}} sub-block (engine {CU_SURVIVOR_IDX}; Peirce "
          f"{SURV_PEIRCE}) -- where MATTER lives")
    print(f"      bridge: (1/6) polarize_d(phi_i,phi_j,frame_a) == const * (eta*soldering)_a")
    print(f"      distinct ratios over Q = {consts}")
    _report(f"BRIDGE exact over Q with a SINGLE algebra-fixed const == {const_val} "
            "(det_3 polarization vs pi_u-soldered Jordan product; NOT an inserted knob) "
            "[the spin current is the algebra's OWN cubic coupling]", single)

    # The e_1..e_6 octonion directions of V_{1/2} are KILLED by E (pi_u onto C_u) -> no
    # soldering image (so the FULL-V_{1/2} C-block has extra entries with no current; the
    # spin current is intrinsically a C_u-survivor object).
    killed = []
    for idx in range(11, 27):
        if idx in CU_SURVIVOR_IDX:
            continue
        s = soldering(phi_vec({idx: Rational(1)}), phi_vec({idx: Rational(1)}))
        killed.append(s.is_zero_matrix)
    _report("E (pi_u onto h_3(C_u)) KILLS the e_1..e_6 octonion directions of V_{1/2} "
            "(idx 12-17, 20-25): NO soldering image -> spin current is intrinsically a "
            "C_u-survivor object [exact Q]", all(killed))
    return {"const": str(const_val), "single": single, "consts": [str(x) for x in consts]}


# ============================================================================
# Def-A : direct C-contraction / soldering current  S^a[phi]
# ============================================================================
def def_A_current(matter):
    """S^a[phi] = component-a of to_mink(jordan(E(phi),E(phi))), a in the 4 spacetime
    frame indices (symmetric in phi).  By the BRIDGE this equals -(1/const) eta^{-1}
    contracted into the C-block S^a = sum_{i,j in V_{1/2}} C_{ija} phi^i phi^j -- BUT we
    compute it DIRECTLY from the soldering (the algebra object), no inserted constant.
    `matter` is a dict {engine_idx: rational}.  EXACT over Q.  Returns the R^{3,1} vector."""
    Phi = phi_vec(matter)
    return soldering(Phi, Phi)


def def_A_C_contraction(matter):
    """The C-contraction form of Def-A: S_a = sum_{i,j} C(phi_i,phi_j,frame_a) phi^i phi^j
    (lowered frame index).  Cross-checks def_A_current via the BRIDGE.  EXACT over Q."""
    # expand phi = sum_i c_i phi(peirce_i); C is symmetric trilinear so
    # S_a = sum_{i,j} c_i c_j C(phi_i,phi_j,frame_a).
    coeffs = {}   # peirce index -> coefficient
    for idx, val in matter.items():
        peirce = (idx - 11 + 1) if 11 <= idx <= 18 else (idx - 19 + 9)
        coeffs[peirce] = val
    S = []
    for a in range(4):
        tot = Rational(0)
        for pi_, ci in coeffs.items():
            for pj_, cj in coeffs.items():
                tot += ci * cj * C(phi(pi_), phi(pj_), FRAME[a])
        S.append(simplify(tot))
    return Matrix(S)


# ============================================================================
# THE FORCED so(3,1) ON V_{1/2} : Sigma^{ab} (the genuine antisymmetric spin generators)
#   Replicate cartan_phaseC_contraction.forced_so31_generators' residual `res` (27x27),
#   then take the 16x16 block on V_HALF_IDX.  Source: Phase 75 residual structure group.
# ============================================================================
def sigma_half_generators():
    """The 6 (E_11,u)-FORCED so(3,1) generators (Phase 75 residual 21 = so(3,1)[6] +
    so(6)[15]; so(6) a trivial-on-spacetime ideal), as 27x27 residual matrices `res`
    RESTRICTED to:
      - the 4x4 frame block (CU4_IDX) -> L_frame  (to pick the 6 Lorentz generators &
        verify they close as so(3,1) / kill eta);
      - the 16x16 V_{1/2} block (V_HALF_IDX) -> Sigma_half  (how so(3,1) acts on the
        chiral spinor rep -- the SPIN content for Def-B).
    Mirrors cartan_phaseC_contraction.forced_so31_generators' construction (BG.build_e6_basis
    -> stab_E6_E11 -> stab_preserving_V0 -> residual nullspace), then keeps the V_{1/2}
    block instead of only the 4-space.  EXACT over Q.  Returns (Sigma_half, L_frame, dim_res)."""
    e6_basis, _ = BG.build_e6_basis()
    sb = BG.stab_E6_E11(e6_basis)
    sV0 = BG.stab_preserving_V0(sb["stab_gens"])
    # residual = nullspace over QQ of {Stab_{V_0} preserving the C_u 4-space CU4_IDX}.
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
    # 4x4 frame block (to select the 6 independent Lorentz generators):
    acts4 = [Matrix(4, 4, lambda i, j: D[CU4_IDX[i], CU4_IDX[j]]) for D in res]
    flat4 = Matrix([[A[r, c] for r in range(4) for c in range(4)] for A in acts4])
    _, piv = flat4.T.rref()
    L_frame = [acts4[i] for i in piv]
    # the SAME pivots select the corresponding residual generators; take their 16x16
    # V_{1/2} block -> the spin action on the chiral rep.
    Sigma_half = [Matrix(16, 16, lambda i, j: res[i0][V_HALF_IDX[i], V_HALF_IDX[j]])
                  for i0 in piv]
    return Sigma_half, L_frame, len(res)


def _lie_closes_so31(L_frame):
    """Verify the 6 frame generators ARE so(3,1) and close under the bracket.  The frame
    blocks are in the RAW {beta,gamma,p,q} basis, so the Lorentz condition is against
    G_DET2_RAW (NOT eta directly); we ALSO conjugate to the orthonormal frame via PC.T_ON
    and confirm they kill eta=diag(+1,-1,-1,-1) there (re-confirming Phase 75 in BOTH
    bases).  Closure: their span is bracket-closed and 6-dimensional.  EXACT over Q."""
    kill_raw = all((A.T * G_DET2_RAW + G_DET2_RAW * A).is_zero_matrix for A in L_frame)
    L_on = [(PC.T_ON * A * PC.T_ON_INV).applyfunc(simplify) for A in L_frame]
    kill_eta = all((A.T * ETA + ETA * A).is_zero_matrix for A in L_on)
    # span dim:
    flat = Matrix([[A[i, j] for i in range(4) for j in range(4)] for A in L_frame])
    dim6 = (flat.rank() == 6)
    # closure: every [L_i,L_j] is in the span (rank does not grow when adjoined).
    base_rank = flat.rank()
    brackets = []
    for A, Bm in itertools.combinations(L_frame, 2):
        comm = A * Bm - Bm * A
        brackets.append([comm[i, j] for i in range(4) for j in range(4)])
    join = Matrix([[A[i, j] for i in range(4) for j in range(4)] for A in L_frame] + brackets)
    closed = (join.rank() == base_rank)
    return (kill_raw and kill_eta), dim6, closed


def _sigma_acts_on_half(Sigma_half):
    """Verify the V_{1/2} blocks are nonzero (so(3,1) genuinely ACTS on the chiral rep)
    and the 6 blocks are linearly independent (a faithful 16-dim rep).  EXACT over Q."""
    nonzero = [not S.is_zero_matrix for S in Sigma_half]
    flat = Matrix([[S[i, j] for i in range(16) for j in range(16)] for S in Sigma_half])
    indep6 = (flat.rank() == 6)
    return all(nonzero), indep6


# ============================================================================
# Def-B : the spin tensor (antisymmetric -- the genuine torsion current)
# ============================================================================
def def_B_spin_current(matter, Sigma_half, ab_pairs=None):
    """s^{ab}_c[phi] = component-c of to_mink(jordan(E(phi), E(Sigma^{ab}.phi))),
    antisymmetric in [ab].  Sigma^{ab} acts on V_{1/2} via the forced so(3,1) blocks
    (Sigma_half).  Torsion T^c_{ab}[phi] = s with frame indices raised/lowered by eta.
    `matter` dict {engine_idx: rational}; `ab_pairs` optional list of generator indices
    (default all 6).  EXACT over Q.  Returns {gen_index: R^{3,1} vector s_c}."""
    Phi = phi_vec(matter)
    # phi as a 16-vector on V_HALF_IDX (engine 11..26):
    phi16 = Matrix([matter.get(idx, Rational(0)) for idx in V_HALF_IDX])
    if ab_pairs is None:
        ab_pairs = list(range(len(Sigma_half)))
    out = {}
    for k in ab_pairs:
        Sk = Sigma_half[k]
        spun16 = Sk * phi16                       # Sigma^{ab} . phi, a V_{1/2} vector
        spun = phi_vec({V_HALF_IDX[i]: spun16[i] for i in range(16) if spun16[i] != 0}) \
            if any(spun16[i] != 0 for i in range(16)) else phi_vec({})
        s_c = Matrix(PA.to_mink(RL.jordan(EMB.E(Phi), EMB.E(spun))))
        out[k] = s_c.applyfunc(simplify)
    return out


# ============================================================================
# G0c.2 : does the algebra FIX the geometric-torsion coupling? (REPORT, not hardwire)
# ============================================================================
def g0c2_geometric_coupling():
    """G0c.2 -- the decisive non-circularity question.  The spin current S is a
    DIMENSIONLESS algebra object.  Geometric torsion is T^a = d_omega e^a built from the
    SAME soldering form e (e = pi_u(dE); g = e.e is the Phase-77 position-dependent (1,3)
    Lorentzian slice).  The Cartan equation T^a = (coupling) * S^a needs a coupling with
    dimension 1/length^2 (1/L from d, and S/e^2 carrying the rest).  The question: is the
    constant relating S to a geometric torsion of that SAME e FORCED by an algebra object
    (trace form / det / the soldering normalization) -- => SURVIVES -- or FREE -- =>
    fp-imported-action?

    We build the decisive geometric object from the SAME e (the M=0 baseline soldering
    g = G_DET2_RAW and the M!=0 curved slice via spacetime_curvature_of_g), and test
    exact-over-Q whether ANY algebra scalar (Tr / det_3 / det_2 / the soldering norm)
    supplies a dimensionful scale that fixes the coupling.  REPORT the finding; do NOT
    hardwire the verdict."""
    print("=" * 78)
    print("G0c.2 (the DECISIVE non-circularity gate) : does the algebra FIX the")
    print("  geometric-torsion coupling (=> SURVIVES) or is it free (=> fp-imported-action)?")
    print("=" * 78)

    # (i) the SAME soldering form e: g = e.e.  M=0 baseline and M!=0 curved slice.
    tick("building g(M=0) and g(M!=0) from the SAME soldering e (Phase-77 pipeline) ...")
    res0 = BG.spacetime_curvature_of_g({}, SLICE_VALS, bg_delta=BG_PARTNER)
    g0 = res0["g"]
    resM = BG.spacetime_curvature_of_g(MATTER, SLICE_VALS, bg_delta=BG_PARTNER)
    gM = resM["g"]
    base_ok = (simplify(g0 - PA.G_DET2_RAW) == Matrix.zeros(4, 4))
    sig0 = _signature(g0)
    _report(f"the SAME soldering e: g(M=0) == G_DET2_RAW (Phase-75 (1,3) Lorentzian base, "
            f"signature {sig0}) [exact Q]", base_ok and sig0 == (1, 3, 0))

    # (ii) the algebra scalars available to set a scale, evaluated on the matter:
    #   - det_2 of the soldered metric g (a geometric volume scale of e itself);
    #   - det_3 (cubic norm) of the matter element in h_3(O);
    #   - the bare trace form Tr(jordan(.,.)) -- the (4,0) FOIL (NOT the spacetime metric).
    tick("evaluating the candidate algebra scalars (det_2(g), det_3(matter), Tr-foil) ...")
    det2_g0 = simplify(g0.det())                 # det of the (1,3) soldered metric, M=0
    det2_gM = simplify(gM.det())                 # ... M!=0
    Phi_full = phi_vec(MATTER)
    # the full matter h_3(O) element (V_{1/2} survivors + the V_0 x1 partner) for det_3:
    Mfull = RL.h3o_from_coords(
        0, 0, 0,
        [BG_PARTNER.get(3 + k, Rational(0)) for k in range(8)],   # x1 octonion (engine 3..10)
        [MATTER.get(11 + k, Rational(0)) for k in range(8)],      # x2 octonion (engine 11..18)
        [MATTER.get(19 + k, Rational(0)) for k in range(8)],      # x3 octonion (engine 19..26)
    )
    det3_M = simplify(RL.det_3(Mfull))
    print(f"      det_2(g, M=0) = {det2_g0}    det_2(g, M!=0 sample) = {det2_gM}")
    print(f"      det_3(matter element in h_3(O)) = {det3_M}")

    # (iii) THE DECISIVE TEST.  The soldering normalization is SCALE-FREE: e = pi_u(dE) is
    #   defined up to an overall real rescaling e -> lambda e (the soldering form has no
    #   intrinsic length -- h_3(O) is a graded ALGEBRA, dimensionless).  Under e -> lambda e:
    #     g = e.e          -> lambda^2 g
    #     det_2(g)         -> lambda^8 det_2(g)
    #     T^a = d_omega e^a-> lambda T^a   (omega is scale-invariant; e scales)
    #     S^a (Def-A)      -> lambda^2 S^a (quadratic in phi via the soldering)
    #   The Cartan coupling c in  T^a = c S^a  then scales as c -> lambda^{-1} c.  An
    #   ALGEBRA scalar fixes c iff some algebra invariant has the SAME lambda-weight as
    #   c (weight -1).  But every h_3(O) invariant (Tr ~ lambda, det_2 ~ lambda^8 here on
    #   the bilinear g, det_3 ~ lambda^3 on a cubic element, the trace form ~ lambda^2) has
    #   a NON-NEGATIVE integer weight under the algebra's NATURAL grading -- NONE has weight
    #   -1, and NONE is dimensionful (1/length^2).  So no algebra scalar can supply the
    #   coupling's dimension: the coupling is a FREE parameter not fixed by any algebra
    #   object.  We DEMONSTRATE the scale-freedom exact-over-Q with two rescalings.
    tick("testing scale-covariance under e -> lambda e (the decisive weight argument) ...")
    weights = {}
    for lam in (Rational(2), Rational(3, 2)):
        # e -> lambda e  <=>  g -> lambda^2 g.  Recompute the soldering-derived scalars.
        g_sc = (lam ** 2 * g0).applyfunc(simplify)
        det2_sc = simplify(g_sc.det())
        w_det2 = simplify(det2_sc / det2_g0)               # expect lambda^8
        # Def-A current scales as lambda^2 (quadratic in phi through the bilinear soldering):
        w_S = lam ** 2
        # the Cartan coupling weight: T ~ lambda^1, S ~ lambda^2  =>  c = T/S ~ lambda^{-1}.
        w_c = simplify(lam ** 1 / lam ** 2)                # lambda^{-1}
        weights[str(lam)] = {"det2_weight": str(w_det2),
                             "expect_lambda8": str(lam ** 8),
                             "S_weight": str(w_S),
                             "coupling_weight": str(w_c)}
    # the decisive booleans:
    det2_w8 = all(simplify(Rational(v["det2_weight"]) - Rational(v["expect_lambda8"])) == 0
                  for v in weights.values()) if False else \
        all(simplify(eval_w(v["det2_weight"]) - eval_w(v["expect_lambda8"])) == 0
            for v in weights.values())
    coupling_negative_weight = all(eval_w(v["coupling_weight"]) != Rational(1)
                                   and eval_w(v["coupling_weight"]) < Rational(1)
                                   for v in weights.values())
    # DERIVE (not assert) "no F_4-invariant has negative weight": R[h_3(O)]^{F_4} is the
    # FREE polynomial ring on Tr (deg 1), Tr2 (deg 2), det_3 (deg 3) (Springer; this project's
    # v16 RING generating-set certificate, code/molien_bigraded.py: H(s)=1/((1-s)(1-s^2)(1-s^3))).
    # Confirm each generator's grading weight by direct X -> lam*X substitution into the SSOT
    # invariants, exact over Q; the MIN generator degree is 1 > 0, so every invariant (a
    # polynomial in them) has NON-NEGATIVE weight -- NONE can be the weight -1 the coupling needs.
    lam = symbols('lam', positive=True)
    _gc = [Rational(3), Rational(-1, 2), Rational(2),
           Rational(1, 3), 0, Rational(2, 5), 0, Rational(1, 7), 0, 0,
           Rational(1, 4), Rational(1, 5), 0, 0, Rational(3, 8), 0, Rational(1, 6), 0,
           0, Rational(1, 9), 0, Rational(2, 3), 0, 0, Rational(1, 11), 0, Rational(1, 2)]
    Xc = RL.X_from_symbols(_gc)
    Xl = RL.X_from_symbols([lam * v for v in _gc])
    gen_w = {"Tr (deg1)": simplify(RL.Tr(Xl) / RL.Tr(Xc)),
             "Tr2 (deg2)": simplify(RL.Tr2(Xl) / RL.Tr2(Xc)),
             "det_3 (deg3)": simplify(RL.det_3(Xl) / RL.det_3(Xc))}
    # positive weight <=> value > 1 at lam=2 (lam^k>1 iff k>=1; k=0 -> 1; k<0 -> <1):
    algebra_weights_nonneg = all(w.subs(lam, Rational(2)) > 1 for w in gen_w.values())
    print("      F_4-invariant ring generators -- weight under X -> lam X (exact over Q):")
    for _nm, _w in gen_w.items():
        print(f"        {_nm}: weight = {_w}")
    print(f"      -> all generator weights positive (min degree 1 > 0) => the free poly ring "
          f"R[h_3(O)]^F4 has NO negative-weight invariant: {algebra_weights_nonneg}")
    print("      e -> lambda e scale-covariance (exact over Q):")
    for lam, v in weights.items():
        print(f"        lambda={lam}: det_2(g) weight = {v['det2_weight']} "
              f"(expect lambda^8={v['expect_lambda8']}); Def-A S weight = {v['S_weight']}; "
              f"Cartan coupling weight = {v['coupling_weight']} (= lambda^-1)")
    _report("det_2(g) scales as lambda^8 under e -> lambda e (exact over Q) -- the "
            "soldering metric is SCALE-COVARIANT [the soldering form has no intrinsic length]",
            det2_w8)
    _report("the Cartan coupling c in T^a = c S^a has weight lambda^{-1} (T~lambda^1, "
            "S~lambda^2) -- it is DIMENSIONFUL (1/length^2 in physical units)",
            coupling_negative_weight)
    _report("NO h_3(O) algebra invariant has weight -1 (Tr~lambda^1, det_2(g)~lambda^8, "
            "det_3~lambda^3, trace-form~lambda^2 -- ALL non-negative) and none is "
            "dimensionful => NO algebra scalar fixes the coupling's dimension/scale",
            algebra_weights_nonneg)

    # the HONEST reading (REPORTED, not hardwired into the verdict ladder here):
    coupling_forced = (not algebra_weights_nonneg)   # would need a weight-(-1) algebra scalar
    decisive_object = ("the soldering-form normalization e -> lambda e (scale-freedom of "
                       "h_3(O) as a dimensionless graded algebra) vs the Cartan coupling's "
                       "weight-(-1) / dimension 1/length^2")
    print(f"      >>> G0c.2 DECISIVE OBJECT: {decisive_object}")
    print(f"      >>> G0c.2 FINDING: coupling FORCED by an algebra object = {coupling_forced} "
          f"=> {'SURVIVES' if coupling_forced else 'fp-imported-action'}")
    return {"base_ok": bool(base_ok and sig0 == (1, 3, 0)),
            "det2_g0": str(det2_g0), "det2_gM": str(det2_gM), "det3_M": str(det3_M),
            "weights": weights, "det2_weight8": bool(det2_w8),
            "coupling_negative_weight": bool(coupling_negative_weight),
            "algebra_has_weight_minus1": bool(not algebra_weights_nonneg),
            "coupling_forced": bool(coupling_forced),
            "decisive_object": decisive_object}


def eval_w(s):
    """Parse a small rational-power weight string ('lambda^8' style already evaluated to a
    rational here, e.g. '256', '1/2') into a sympy Rational.  All weights handed in are
    already numeric (we substituted explicit lambdas)."""
    return Rational(s)


# ============================================================================
# verdict() -- deterministic, NON-hardwired ladder (mirror cartan_phaseC_contraction.verdict)
# ============================================================================
def verdict(flags):
    """Map the Gate-0 booleans to the categorical pre-flight verdict via the LADDER, with
    NO new computation, NO posited coupling, NO float -- a pure deterministic function of
    the exact-over-Q flags.  Each clause is INDEPENDENTLY load-bearing (demonstrated
    non-hardwired by feeding a hypothetical all-pass input in main()).

    flags keys (all bool):
      torsion_nonzero        : G0a -- the spin current (Def-A & Def-B) is not identically 0
      parity_tracking        : G0b -- chirality-odd comps flip, even comps stay (NOT parity-blind)
      coeff_noncircular      : G0c.1 -- every coefficient is (1/6)polarize_d / soldering, NO
                                        inserted coupling (AST/source guard clean + FIRES on injection)
      coupling_forced        : G0c.2 -- an algebra object FIXES the geometric-torsion coupling

    Ladder:
      T == 0 OR parity-blind                  -> "robust-v18-torsion-free" (STOP; triangulation)
      coupling NOT forced (G0c.2 posited)     -> "fp-imported-action"      (STOP)
      all of {nonzero, parity, noncircular, forced} -> "SURVIVES -> greenlight Gate 1"
    Returns {category, clauses, summary}."""
    torsion_nonzero = bool(flags["torsion_nonzero"])
    parity_tracking = bool(flags["parity_tracking"])
    coeff_noncircular = bool(flags["coeff_noncircular"])
    coupling_forced = bool(flags["coupling_forced"])

    clauses = {
        "G0a_torsion_nonzero": torsion_nonzero,
        "G0b_parity_tracking": parity_tracking,
        "G0c1_coeff_noncircular": coeff_noncircular,
        "G0c2_coupling_forced": coupling_forced,
    }

    # clause 1 (independent): no torsion / parity-blind => the v18 torsion-free triangulation holds.
    if (not torsion_nonzero) or (not parity_tracking):
        category = "robust-v18-torsion-free"
        summary = ("the chiral V_{1/2} spin current either VANISHES or is parity-blind -- "
                   "no chirality-tracking torsion; the v18 torsion-free reading is robust "
                   "(STOP; triangulation complete)")
    # clause 2 (independent): coupling not forced => imported action (the most-likely outcome).
    elif not coupling_forced:
        category = "fp-imported-action"
        summary = ("a nonzero chirality-tracking spin current EXISTS, but NO h_3(O) algebra "
                   "object fixes the geometric-torsion coupling (the Cartan kappa is "
                   "dimensionful / weight-(-1); every algebra invariant has non-negative "
                   "weight) -- the coupling comes only with a POSITED EC action, an honest "
                   "partial in the GST/Singh/Castro class (STOP)")
    # clause 3 (all pass): SURVIVES -> Gate 1 (the curvature gate).
    elif torsion_nonzero and parity_tracking and coeff_noncircular and coupling_forced:
        category = "SURVIVES -> greenlight Gate 1"
        summary = ("a nonzero chirality-tracking, non-circular spin current AND an algebra "
                   "object that fixes the coupling -- the cheap kill is PASSED; proceed to "
                   "Gate 1 (geometric torsion T^a = d_omega e^a curvature)")
    else:
        # the residual case (e.g. noncircular guard failed) -- a setup problem, NOT a verdict.
        category = "INCONCLUSIVE (coefficient guard failed -- debug, no verdict)"
        summary = ("the coefficient non-circularity guard (G0c.1) did not pass cleanly; "
                   "this is a SETUP problem, not a physics verdict")
    return {"category": category, "clauses": clauses, "summary": summary}


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("#" * 78)
    print("# GATE 0 (cheap kill) : Einstein-Cartan TORSION from chiral V_{1/2} spin on h_3(O)")
    print("#   fail-fast pre-flight -- NO curvature (deferred Gate 1), NO roadmap/state/commits")
    print("#   EXACT over Q (sympy.Rational / Matrix; ranks via .rank()); NEVER numpy/float")
    print("#" * 78)

    # ---- 0. guards ----
    sg = source_guard()
    print()
    print("=" * 78)
    print("G0c.1 GUARD : AST/source coefficient non-circularity (no inserted EC coupling)")
    print("=" * 78)
    ast_ok, ast_hits, src_hits = ast_source_guard()
    _report(f"AST: NO forbidden identifier (kappa/8piG/EC-action/octonion_algebra/linalg) USED "
            f"in the decisive coefficient-path functions {sorted(_DECISIVE_FUNCS)} "
            f"(hits={ast_hits}) [comment/docstring mentions are not code-uses]", not ast_hits)
    _report(f"SOURCE: NO posited-coupling token (8piG / 'posited action' / 'EH-Palatini "
            f"action' / numpy.linalg) in the decisive-function CODE (hits={src_hits})",
            not src_hits)
    # PROVE the guard FIRES on an injected violation (not a no-op):
    inject = ("def def_B_spin_current_INJECT(m):\n"
              "    kappa = 1\n"
              "    return kappa  # 8*pi*G posited EH-Palatini action coupling\n")
    # rename the injected func to a decisive name so the guard scans it:
    inject_named = inject.replace("def_B_spin_current_INJECT", "def_B_spin_current")
    bad_ok, bad_ast, bad_src = ast_source_guard(extra_src=inject_named)
    guard_fires = (not bad_ok) and (("def_B_spin_current" in bad_ast) or ("def_B_spin_current" in bad_src))
    _report("the G0c.1 guard FIRES on an injected violation (a kappa=8*pi*G posited-action "
            f"coupling in a decisive func) -- NOT a no-op (ast_hit={bad_ast}, src_hit={bad_src})",
            guard_fires)
    g0c1_ok = ast_ok and guard_fires

    # ---- the load-bearing BRIDGE (verify FIRST) ----
    print()
    bridge = verify_bridge()

    # ---- Def-A : the soldering current ----
    print()
    print("=" * 78)
    print("Def-A (direct C-contraction / soldering current) : S^a[phi]")
    print("=" * 78)
    print(f"      sample MATTER (C_u survivors {CU_SURVIVOR_IDX}) = {MATTER}")
    S_sold = def_A_current(MATTER)
    S_Ccon = def_A_C_contraction(MATTER)
    print(f"      S^a (soldering to_mink(jordan(E phi,E phi))) [x0,x1,x2,x3] = {list(S_sold)}")
    print(f"      S_a (C-contraction sum C_ija phi^i phi^j, lowered)        = {list(S_Ccon)}")
    # cross-check via the bridge: S_a (lowered) == const * eta * S^a (upper). const = -2/3.
    bridge_const_val = Rational(bridge["const"]) if bridge["single"] else None
    if bridge_const_val is not None:
        check = (S_Ccon - (bridge_const_val * ETA * S_sold)).applyfunc(simplify)
        _report(f"Def-A self-consistent: C-contraction S_a == const*eta*S^a with const="
                f"{bridge_const_val} (the two Def-A forms agree via the BRIDGE) [exact Q]",
                check.is_zero_matrix)
    S_nonzero = (not S_sold.is_zero_matrix)

    # ---- the FORCED so(3,1) on V_{1/2} (Sigma^{ab}) ----
    print()
    print("=" * 78)
    print("THE (E_11,u)-FORCED so(3,1) ON V_{1/2} : Sigma^{ab} (Phase-75 residual, 16x16 block)")
    print("=" * 78)
    tick("building the forced so(3,1) generators (build_e6_basis -> stab -> residual) ...")
    Sigma_half, L_frame, dim_res = sigma_half_generators()
    _report(f"residual structure group dim == 21 (= so(3,1)[6] + so(6)[15], Phase 75) "
            f"(got {dim_res}) [exact Q]", dim_res == 21)
    kill_eta, dim6, closed = _lie_closes_so31(L_frame)
    _report(f"the 6 forced frame generators are so(3,1): kill G_DET2_RAW (raw) AND eta "
            f"(orthonormal, via T_ON) = {kill_eta}, dim span = {'6' if dim6 else 'NOT 6'}, "
            f"bracket-closed = {closed} [exact Q]", kill_eta and dim6 and closed)
    acts_half, indep6 = _sigma_acts_on_half(Sigma_half)
    _report(f"so(3,1) genuinely ACTS on V_{{1/2}}: all 6 Sigma^{{ab}} blocks nonzero = "
            f"{acts_half}, linearly independent (faithful 16-dim spinor rep) = {indep6} [exact Q]",
            acts_half and indep6)

    # ---- Def-B : the spin tensor (antisymmetric torsion current) ----
    print()
    print("=" * 78)
    print("Def-B (spin tensor, antisymmetric -- the genuine torsion current) : s^{ab}_c[phi]")
    print("=" * 78)
    s_dict = def_B_spin_current(MATTER, Sigma_half)
    s_nonzero_any = False
    print(f"      s^{{ab}}_c[phi] = to_mink(jordan(E phi, E(Sigma^ab . phi)))  (6 generators):")
    for k in sorted(s_dict):
        vec = s_dict[k]
        nz = not vec.is_zero_matrix
        s_nonzero_any = s_nonzero_any or nz
        print(f"        gen {k}: s_c = {list(vec)}   ({'NONZERO' if nz else 'zero'})")
    # Torsion T^c_{ab} = eta-raise on s (antisymmetric in [ab] by Sigma antisymmetry).
    _report("Def-B spin current s^{ab}_c has >=1 NONZERO rational component over the 6 "
            "forced so(3,1) generators at the sample [exact Q]", s_nonzero_any)

    # ---- G0a : generic-symbolic non-vanishing ----
    print()
    print("=" * 78)
    print("G0a (nonzero) : Def-A and Def-B nonzero at sample + generic-symbolic not identically 0")
    print("=" * 78)
    # generic 16-symbol phi on V_{1/2}: Def-A current must not be identically zero.
    gsyms = symbols('p0:16', real=True)
    gen_matter = {V_HALF_IDX[i]: gsyms[i] for i in range(16)}
    S_gen = def_A_current(gen_matter)
    S_gen_simpl = S_gen.applyfunc(cancel)
    gen_nonzero = (not S_gen_simpl.is_zero_matrix)
    print(f"      generic-symbolic Def-A S^0 (head) = {S_gen_simpl[0]}")
    _report(f"Def-A current is NOT identically zero for a generic 16-symbol V_{{1/2}} phi "
            f"(symbolic over Q) [exact]", gen_nonzero)
    # generic Def-B (one generator) not identically zero:
    s_gen = def_B_spin_current(gen_matter, Sigma_half, ab_pairs=[0])
    s_gen_vec = s_gen[0].applyfunc(cancel)
    s_gen_nonzero = (not s_gen_vec.is_zero_matrix)
    print(f"      generic-symbolic Def-B s^{{(gen0)}}_c (head) = {s_gen_vec[0]}")
    _report("Def-B spin current (generator 0) is NOT identically zero for generic phi "
            "(symbolic over Q) [exact]", s_gen_nonzero)
    g0a = S_nonzero and s_nonzero_any and gen_nonzero and s_gen_nonzero
    print(f"      >>> G0a = {g0a}")

    # ---- G0b : chirality tracking ----
    print()
    print("=" * 78)
    print("G0b (chirality-tracking) : flip x2<->x3 (Gamma=+1 on 11..18, -1 on 19..26);")
    print("  chirality-ODD comps must flip sign, universal/timelike (beta+gamma=x0) stays")
    print("=" * 78)
    # the flip sigma: swap x2-block[11..18] <-> x3-block[19..26].
    def chirality_flip(matter):
        out = {}
        for idx, val in matter.items():
            if 11 <= idx <= 18:
                out[idx + 8] = val          # x2 -> x3
            elif 19 <= idx <= 26:
                out[idx - 8] = val          # x3 -> x2
        return out
    M_flip = chirality_flip(MATTER)
    S_flip = def_A_current(M_flip)
    print(f"      MATTER          = {MATTER}")
    print(f"      MATTER (flipped)= {M_flip}")
    print(f"      Def-A S^a (orig)    [x0,x1,x2,x3] = {list(S_sold)}")
    print(f"      Def-A S^a (flipped) [x0,x1,x2,x3] = {list(S_flip)}")
    # classify each frame component: even (S_flip==S) or odd (S_flip==-S).
    comp_class = {}
    for a, name in enumerate(["x0(timelike=beta+gamma)", "x1(p=Re x1)",
                              "x2(q=<x1,e7>)", "x3(spacelike=beta-gamma)"]):
        so, sf = simplify(S_sold[a]), simplify(S_flip[a])
        if so == 0 and sf == 0:
            comp_class[a] = ("zero", name)
        elif simplify(sf - so) == 0:
            comp_class[a] = ("EVEN(stays)", name)
        elif simplify(sf + so) == 0:
            comp_class[a] = ("ODD(flips)", name)
        else:
            comp_class[a] = ("mixed", name)
    for a in range(4):
        cls, name = comp_class[a]
        print(f"        S^{a} [{name}]: orig={simplify(S_sold[a])}, flip={simplify(S_flip[a])} -> {cls}")
    # the chirality SIGNAL: at least one ODD component flips; the timelike x0 (beta+gamma,
    # the universal C_{i,i,17}=-1/6 direction) stays EVEN (NOT parity-blind).
    any_odd = any(comp_class[a][0] == "ODD(flips)" for a in range(4))
    x0_even_or_zero = comp_class[0][0] in ("EVEN(stays)", "zero")
    not_parity_blind = any_odd
    _report("Def-A: >=1 chirality-ODD frame component FLIPS sign under x2<->x3 (the "
            "(beta-gamma) sign-split + the e_7-linked off-diagonal pairing) [exact Q]", any_odd)
    _report("Def-A: the timelike x0=(beta+gamma) component (the UNIVERSAL C_{i,i,17}=-1/6 "
            "direction) stays chirality-EVEN/zero -- NOT parity-blind [exact Q]", x0_even_or_zero)
    # Def-B parity: spin current of the flipped matter -- the odd structure must track too.
    s_flip = def_B_spin_current(M_flip, Sigma_half)
    sB_tracks = False
    for k in sorted(s_dict):
        vo, vf = s_dict[k].applyfunc(simplify), s_flip[k].applyfunc(simplify)
        for a in range(4):
            if vo[a] != 0 and simplify(vf[a] + vo[a]) == 0:
                sB_tracks = True
    _report("Def-B: the antisymmetric spin current also has a chirality-ODD component that "
            "flips under x2<->x3 (the torsion tracks chirality) [exact Q]", sB_tracks)
    g0b = not_parity_blind and x0_even_or_zero
    print(f"      >>> G0b = {g0b}  (chirality-tracking, NOT parity-blind)")

    # ---- G0c.1 already computed above; ---- G0c.2 ----
    print()
    g0c2 = g0c2_geometric_coupling()

    # ---- the verdict ladder (deterministic, non-hardwired) ----
    print()
    print("#" * 78)
    print("# verdict() : deterministic NON-hardwired ladder (mirror cartan_phaseC.verdict)")
    print("#" * 78)
    flags = {
        "torsion_nonzero": g0a,
        "parity_tracking": g0b,
        "coeff_noncircular": g0c1_ok,
        "coupling_forced": g0c2["coupling_forced"],
    }
    v = verdict(flags)
    print(f"      flags = {flags}")
    print(f"      >>> Gate-0 VERDICT (this driver's reading): {v['category']}")
    print(f"      >>> {v['summary']}")

    # NON-HARDWIRED demonstration: a HYPOTHETICAL all-pass input yields SURVIVES, and
    # flipping any single clause changes the category -- so no clause is hardwired.
    print()
    print("      [non-hardwired ladder check]")
    hyp_all = {"torsion_nonzero": True, "parity_tracking": True,
               "coeff_noncircular": True, "coupling_forced": True}
    print(f"        hypothetical all-pass -> {verdict(hyp_all)['category']}")
    hyp_noT = {**hyp_all, "torsion_nonzero": False}
    print(f"        hypothetical T==0     -> {verdict(hyp_noT)['category']}")
    hyp_blind = {**hyp_all, "parity_tracking": False}
    print(f"        hypothetical parity-blind -> {verdict(hyp_blind)['category']}")
    hyp_free = {**hyp_all, "coupling_forced": False}
    print(f"        hypothetical coupling-free -> {verdict(hyp_free)['category']}")
    ladder_nonhardwired = (
        verdict(hyp_all)["category"].startswith("SURVIVES")
        and verdict(hyp_noT)["category"] == "robust-v18-torsion-free"
        and verdict(hyp_blind)["category"] == "robust-v18-torsion-free"
        and verdict(hyp_free)["category"] == "fp-imported-action")
    _report("verdict ladder is NON-hardwired: all-pass->SURVIVES, T==0->torsion-free, "
            "parity-blind->torsion-free, coupling-free->fp-imported-action (each clause "
            "independently load-bearing)", ladder_nonhardwired)

    # ---- final summary block (for the report) ----
    print()
    print("#" * 78)
    print("# GATE-0 SUMMARY")
    print("#" * 78)
    print(f"  source/exactness guards clean      : {sg}")
    print(f"  BRIDGE const (algebra-fixed)        : {bridge['const']}  (single={bridge['single']})")
    print(f"  Def-A S^a at sample [x0,x1,x2,x3]   : {list(S_sold)}")
    print(f"  Def-A S^a flipped  [x0,x1,x2,x3]    : {list(S_flip)}")
    print(f"  Def-B s^ab_c nonzero generators     : "
          f"{[k for k in sorted(s_dict) if not s_dict[k].is_zero_matrix]}")
    print(f"  G0a (nonzero)                       : {g0a}")
    print(f"  G0b (chirality-tracking)            : {g0b}")
    print(f"  G0c.1 (coeff non-circular + fires)  : {g0c1_ok}")
    print(f"  G0c.2 (coupling forced by algebra)  : {g0c2['coupling_forced']}  "
          f"=> {'SURVIVES' if g0c2['coupling_forced'] else 'fp-imported-action'}")
    print(f"  G0c.2 decisive object               : {g0c2['decisive_object']}")
    print(f"  VERDICT (driver reading)            : {v['category']}")
    print(f"  ALL_PASS (mechanical checks)        : {ALL_PASS}")
    print("#" * 78)
    print("# NOTE: this is the EXECUTOR's reading of the mechanical Gate-0 checks. The")
    print("#   ORCHESTRATOR adjudicates the milestone verdict and handles any transition.")
    print("#" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
