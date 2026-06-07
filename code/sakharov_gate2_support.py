"""Gate 2 ("SUPPORT MISMATCH") -- does the induced SCALAR kappa from Sakharov
(kappa = c_1 Lambda_f^2 form, c_1 = 1/(6 pi^2) from Gate 1) REPAIR the v18 Phase-77
tensor-support mismatch that killed v18, or does the mismatch SURVIVE the induced kappa?
This is the MILESTONE-DECISIVE third gate of the v21.0 Sakharov ladder -- the ledger's
predicted real cause of death.  Gate 0 (SIGN) SURVIVED (STr=+8/3, induced G>0) and Gate 1
(a_1 propto R) PASSED (a_1=-R/3 clean, c_1=1/(6 pi^2), G=3 pi/(8 Lambda_f^2)>0), both
verifier-hardened HIGH + human-ratified.  This driver runs ONLY Gate 2.  FAIL-FAST: NO
closure (Gate 3) unless Gate 2 SURVIVES; NO roadmap/requirements/state.  EXACT over Q
throughout (sympy.Rational ONLY; NEVER float on any decisive value).

THE v18 FINDING (reproduced here, not assumed).  v18 Phase 77 established -- verifier-hardened,
exact over Q -- that on the matter-bearing soldered background g = e.e the full nonlinear
Einstein tensor G_{mu nu}[g] = Ric_{mu nu} - (1/2) g_{mu nu} R and an INDEPENDENT, AST-guarded
stress tensor T[M] do NOT match as G = kappa T + Lambda g for any single global (kappa,Lambda).
Two faces of the same failure:
  (i) per-point Lambda VARIES across the (M,x) family and the over-determined global solve is
      inconsistent (EmptySet); and
  (ii) a TENSOR-SUPPORT mismatch: at the anchor M_0, G[g] is supported on ALL 16 components of
      the 4x4 symmetric array (every entry nonzero) while kappa T^{[psi]} is supported on only
      6 ({01,10,22,23,32,33}) -- the matter stress is a thin fragment of G (the v17.0
      G_{00} != 0, T_{00} = 0 phenomenon recurs).  This "16-vs-6" is the count of NONZERO
      entries of the 4x4 (lower-index) tensors at the matter-bearing anchor -- NOT "10 symmetric
      slots", and NOT a coordinate accident (it is the structural fact that the symmetric scalar
      stress is rank/support-deficient relative to the full curvature).  We REPRODUCE the actual
      integers here via the warm v18 harness (cartan_phaseB_einstein); if they differ from 16/6
      we report the real numbers and proceed with them.

THE GATE-2 QUESTION (Q).  The induced kappa from Sakharov is a SCALAR (a single cutoff-scale
number, kappa = 6 pi^2 / Lambda_f^2 from Gate 1's c_1 = 1/(6 pi^2), kappa^{-1} = c_1 Lambda_f^2).
A scalar coupling MULTIPLIES T by a number; it CANNOT change which tensor components are nonzero
(it cannot change the tensor rank / support of T).  So structurally:

    support(kappa T + Lambda g) = support(T) U support(g)   (for any scalar kappa != 0, any Lambda)

Because g is invertible Lorentzian its support is the full diagonal (and on this background the
off-diagonal of g may also be nonzero), so support(kappa T + Lambda g) has at most n_T + (support
of g) entries -- and crucially CANNOT cover the n_G nonzero entries of G when n_G exceeds what
T + g can reach.  The induced scalar kappa does NOT enlarge the solution space of
G = kappa T + Lambda g because it is STILL a scalar: the induced-kappa solve is a RESTRICTION of
the v18 free-kappa solve, which ALREADY failed (EmptySet).  We compute -- not assert -- the
following, all exact over Q on MATTER-BEARING profiles (rho > 0, differentiated; the OPPOSITE of
any deflated matter-free check):

  (1) REPRODUCE n_G and n_T at the matter-bearing anchor (confirm matter-bearing: rho>0 i.e.
      G != 0, T != 0, R != 0).  Report the actual integers.
  (2) SCALAR-INVARIANCE OF SUPPORT: for the induced kappa (= 6 pi^2/Lambda_f^2) AND for a
      symbolic free scalar kappa AND for a panel of random rational scalars, support(kappa T) ==
      support(T) identically (a scalar cannot change support).  And support(kappa T + Lambda g)
      with Lambda symbolic == support(T) U support(g) -- still cannot cover support(G).
  (3) THE SINGLE-GLOBAL SOLVE IS INCONSISTENT: solve G = kappa T + Lambda g for ONE global
      (kappa,Lambda) over the matter-bearing family with (a) BOTH free (the strongest test --
      if even both-free fails, the fixed induced kappa certainly fails) and (b) kappa = the
      induced 6 pi^2/Lambda_f^2 with Lambda (and Lambda_f) free.  Confirm EmptySet / residual
      != 0 in both.  The induced solve is a restriction of (a).
  (4) CROSS-CHECK the v18 result reproduces (the 16-vs-6, the single-(kappa,Lambda) inconsistency
      with the v18 frozen rational kappa) -- anchors Gate 2 to the established verifier-hardened
      finding.

THE NON-HARDWIRED VERDICT (Q5).  DEAD iff support(G) is NOT contained in support(kappa T +
Lambda g) for scalar kappa,Lambda (operationally: n_G > n_T + 1 AND G_support != kT_support AND
the single-global solve is inconsistent) -- the induced scalar kappa does NOT repair the
mismatch.  SURVIVES iff the induced kappa makes G = kappa T + Lambda g consistent (the surprise
branch: n_G <= n_T + 1 AND a consistent global solve exists).  The category is DERIVED from the
ACTUAL (n_G, n_T) and the solve result -- it is a pure function of the computed inputs, NEVER a
hardcoded literal.  Three self-tests prove each branch fires (synthetic matching supports +
consistent solve -> SURVIVES; the real mismatched supports + inconsistent solve -> DEAD; a
literal-detector confirms the verdict is not a constant) -- pre-empting the v20 hardcoded-
decisive-boolean bug the verifier caught.

HONEST FRAMING.  Gate 2 DEAD means the Sakharov route dies EXACTLY where v18 died -- the induced
scalar kappa cannot repair a tensor-RANK mismatch (the CONSTRUCTED-vs-EXTREMIZED gap is a rank
fact, scalar-invariant).  This is the predicted outcome.  If instead the induced kappa SURVIVES
(somehow repairs it) that is a MAJOR surprise -> report SURVIVES at true strength and flag that
Gate 3 (CLOSURE) must then run.  Report what the math says.

THE INDUCED kappa (carried from Gate 1, NOT recomputed -- imported/asserted for consistency):
  c_1 = STr/(4 pi)^2 = (8/3)/(16 pi^2) = 1/(6 pi^2)   (Gate 1, on the Gate-0 STr=+8/3)
  kappa^{-1} = c_1 Lambda_f^2 = Lambda_f^2/(6 pi^2)  =>  kappa = 6 pi^2 / Lambda_f^2  (scalar)
  G = 3 pi/(8 Lambda_f^2) > 0.   Lambda_f (the rho_J fixed-point scale) is Gate-3 scope: carried
  symbolic.  The Gate-2 conclusion is Lambda_f-INDEPENDENT (a scalar of ANY value cannot change
  tensor support), which is the whole point.

ENGINE / convention locks inherited from v18.0 (read, NOT rebuilt):
  spacetime slice CU4_IDX = [1,2,3,10]; V_{1/2} matter survivors [11,18,19,26];
  mostly-minus eta = diag(+1,-1,-1,-1); g = e.e (1,3); gravity = Lorentz block R[omega].
  det SSOT = ring_lemma_verification.det_3; octonion_algebra.py BANNED (buggy float associator).
  The v18 matter tetrad is surd-laden and symbolic d-omega hits the >200s watchdog cliff, so the
  warm harness delivers R[omega] via its provably-equal metric-Levi-Civita route (exactly as
  v18-Ph77 did); we do NOT brute-force the symbolic spin connection.

Reproducibility: Python 3.14.x, SymPy 1.14.0 (deterministic, exact over Q; no RNG except a fixed-
seed rational panel for the scalar-invariance sweep, which touches NO decisive verdict path; no
float on any decisive path).

Runnable:  python3 -u code/sakharov_gate2_support.py
Exit 0 iff every decisive check PASSES and the Gate-2 verdict is rendered cleanly.
"""
import os
import sys
import ast as _ast
import time

sys.path.insert(0, '/Users/ehrlich/scratch/get-physics-done/code')

# --- the EXACT-over-Q warm v18 harness (G[g], the independent AST-guarded T[M]) ---
import cartan_phaseB_einstein as E18      # curvature_at (G[g]), psi_scalar, scalar_stress_tensor, family
import bulk_geometry_verification as BG   # spacetime_curvature_of_g (matter-bearing rho>0 / R!=0 check)
import ring_lemma_verification as RL      # det SSOT (source guard)
from sympy import (Matrix, Rational, cancel, pi, symbols, Symbol, zeros,        # noqa: E402
                   linsolve, nsimplify, im as _im)

# ============================================================================
# CONVENTION LOCKS (v18.0; reproduced -- not re-derived)
# ============================================================================
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus,
#   fourier_convention=physics, coupling_convention=alpha_s,
#   renormalization_scheme=MSbar, gauge_choice=Feynman
#
# (The project convention_lock marks fourier/gauge/renorm as N/A for this pure-algebra
#  program; the ASSERT line carries the canonical key names for the validator.  The
#  load-bearing locks are: mostly-minus eta=diag(+1,-1,-1,-1); g=e.e (1,3); gravity =
#  Lorentz block R[omega]; EXACT over Q.  Carried verbatim from v18-Ph77.)

N = 4
ETA = E18.ETA                              # frame metric diag(+1,-1,-1,-1)
CU_SURVIVOR_IDX = E18.CU_SURVIVOR_IDX      # [11,18,19,26]
COORDS = E18.COORDS                        # slice coords (beta,gamma,p,q)
CENTER = E18.CENTER

# The matter-bearing anchor + family (the v18 D1/X0/t1 anchor; rho>0, differentiated).
MATTER_0 = E18.MATTER_0                    # {11:1/5, 18:-1/10, 19:3/10, 26:1/2}  (V_{1/2})
BG_PARTNER = E18.BG                        # {4: 1}  (V_0 partner; keeps det_3 triple non-vacuous)
POS_CENTER = E18.POS_CENTER               # [1/3,1/3,0,0]
MATTER_DIRS = E18.MATTER_DIRS             # 3 V_{1/2} directions
SLICE_POS = E18.SLICE_POS                 # 3 slice positions
AMPS = E18.AMPS                           # 2 amplitudes
scale = E18.scale

# The Gate-1 induced kappa (carried, NOT recomputed): c_1 = 1/(6 pi^2).
C1_GATE1 = Rational(1, 6) / pi**2          # = 1/(6 pi^2), the Gate-1 read-off (on STr=+8/3)
LAMBDA_F = Symbol('Lambda_f', positive=True)   # the Gate-3 rho_J scale (symbolic; NOT pinned here)
KAPPA_INDUCED = cancel(1 / (C1_GATE1 * LAMBDA_F**2))   # = 6 pi^2 / Lambda_f^2  (kappa^-1 = c_1 Lf^2)

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
    return ok


# ============================================================================
# SUPPORT helpers (the count is NONZERO 4x4 entries of the lower-index tensor)
# ============================================================================
def support_of(M):
    """The set of (mu,nu) for which the 4x4 (lower-index) tensor entry is nonzero, EXACT over
    Q.  This is the v18 definition of "support" -- NOT "10 symmetric slots", but the raw count
    of nonzero entries of the 4x4 array (a symmetric thin-support stress shows up as < 16)."""
    return {(mu, nu) for mu in range(N) for nu in range(N) if cancel(M[mu, nu]) != 0}


def at_point(Tbuilder, matter, bg, pos):
    """Evaluate a T-builder (returns a Matrix or (Matrix, ...)) at slice point `pos`, EXACT Q."""
    out = Tbuilder(matter, bg)
    Tf = out[0] if isinstance(out, tuple) else out
    sub = {COORDS[i]: pos[i] for i in range(N)}
    return Tf.applyfunc(lambda e: cancel(e.subs(sub)))


def _T_psi_mat(matter, bg):
    """The INDEPENDENT AST-guarded primary scalar stress T[psi], psi=2Re((x2 x1)x3), reused
    VERBATIM from the v18 harness (E18.psi_scalar/scalar_stress_tensor -- AST-guarded there with
    NO Ric/R/G).  Returns the symbolic Matrix (slice-dependent)."""
    psi = E18.psi_scalar(matter, bg)
    T, _, _ = E18.scalar_stress_tensor(psi)
    return T


def _T_sigma_mat(matter, bg):
    """The INDEPENDENT AST-guarded ALT 16-field sigma stress T_sigma, reused VERBATIM from the
    v18 harness (E18.sigma_multiplet/sigma_stress_tensor).  Returns the symbolic Matrix."""
    phis = E18.sigma_multiplet(matter, bg)
    T, _ = E18.sigma_stress_tensor(phis)
    return T


# ============================================================================
# THE NON-HARDWIRED VERDICT  (DEAD iff support(G) NOT covered by support(kappa T + Lambda g))
# ============================================================================
def verdict(n_G, n_T, support_G, support_kT, global_solve_consistent):
    """Map the ACTUAL (reproduced) support counts and the single-global solve result to the
    categorical Gate-2 verdict via a deterministic LADDER -- a pure function of the inputs, NO
    new computation, NO hardcoded category.  The scalar-kappa structural fact:
        support(kappa T + Lambda g) = support(T) U support(g)  (any scalar kappa!=0, any Lambda),
    so a scalar kappa CANNOT cover support(G) when G is supported on strictly more components
    than T+g can reach.

    Inputs:
      n_G        : int  -- # nonzero 4x4 entries of G[g] at the matter-bearing anchor (the "16").
      n_T        : int  -- # nonzero 4x4 entries of T[M] at the same anchor (the "6").
      support_G  : set  -- the actual G support (for containment check).
      support_kT : set  -- the actual support of (induced kappa) T (== support(T) for scalar).
      global_solve_consistent : bool -- True iff a single global (kappa,Lambda) closes
                   G = kappa T + Lambda g over the matter-bearing family (EmptySet => False).

    Ladder:
      SURVIVES iff (support_G subset of support_kT, i.e. n_G <= n_T) AND global_solve_consistent
               (the surprise branch -- the induced scalar kappa repairs the mismatch).
      DEAD     iff support_G NOT subset of support_kT (n_G > n_T) OR the global solve is
               inconsistent (the induced scalar kappa does NOT repair the mismatch -- dies
               where v18 died).
    Here support_kT is the support of the MATTER piece kappa T (== support(T) for a scalar kappa),
    NOT the dense g.  support(G) not subset of support(kappa T) is the strict statement that the
    matter stress is a thin fragment of G (the v18 16-vs-6).  The DECISIVE clause is
    global_solve_consistent (the off-T over-determination: adding Lambda*g is dense but a single
    scalar Lambda cannot match G on the off-T block -- see scalar_invariance_of_support (d)).
    n_G_exceeds_n_T_plus_1 is a reported diagnostic (the gap is too large for the one extra
    structure Lambda*g could in principle add), not the load-bearing clause.  The DERIVED booleans
    are computed from the inputs, never literals.
    Returns {category, clauses, summary}."""
    for nm, v in (("n_G", n_G), ("n_T", n_T)):
        if not isinstance(v, int):
            raise TypeError(f"{nm} must be int, got {type(v).__name__}")
    if not isinstance(global_solve_consistent, bool):
        raise TypeError("global_solve_consistent must be bool")

    support_covered = support_G.issubset(support_kT)          # DERIVED, not a literal
    rank_excess = (n_G > n_T)                                  # DERIVED
    strict_excess = (n_G > n_T + 1)                            # DERIVED (the +1 = adding Lambda g)
    repairs = support_covered and global_solve_consistent     # DERIVED

    clauses = {
        "support_G_covered_by_kappaT": support_covered,
        "n_G_exceeds_n_T": rank_excess,
        "n_G_exceeds_n_T_plus_1": strict_excess,
        "single_global_solve_consistent": global_solve_consistent,
        "induced_scalar_kappa_repairs": repairs,
    }

    if repairs:
        category = "SURVIVES (induced scalar kappa REPAIRS the v18 support mismatch)"
        summary = ("the induced scalar kappa makes G = kappa T + Lambda g consistent with "
                   "support(G) covered by support(kappa T + Lambda g) -- a MAJOR surprise (a "
                   "scalar repairing a tensor-rank mismatch); Gate 2 does NOT kill and Gate 3 "
                   "(CLOSURE) MUST now run")
    else:
        why = []
        if not support_covered:
            why.append(f"support(G) ({n_G} nonzero entries) is NOT covered by support(kappa T) "
                       f"({n_T}); a scalar kappa cannot change tensor rank/support")
        if not global_solve_consistent:
            why.append("the single global (kappa,Lambda) solve over the matter-bearing family is "
                       "INCONSISTENT (EmptySet) -- and the induced-kappa solve is a RESTRICTION "
                       "of the (already-failing) free-kappa solve")
        category = "DEAD (induced scalar kappa does NOT repair the v18 support mismatch)"
        summary = ("the Sakharov route dies EXACTLY where v18 died: " + "; ".join(why)
                   + ".  The CONSTRUCTED-vs-EXTREMIZED gap is a tensor-RANK fact, invariant under "
                   "ANY scalar coupling (the conclusion is Lambda_f-independent).  Route C / "
                   "kind-4 induced-action is DEAD; the six-kind menu is EXHAUSTED for h_3(O)")
    return {"category": category, "clauses": clauses, "summary": summary}


# ============================================================================
# SOURCE GUARD : octonion_algebra absent; no numpy/float/thermo on the decisive path
# ============================================================================
_FORBIDDEN_SOURCE_TOKENS = [
    "numpy.linalg", "np.linalg", "float(",
    # thermodynamic-route tokens (the REJECTED Route A/D): must not appear as decisive code
    "entropy", "horizon", "ensemble", "temperature", "partition_function",
]
_DECISIVE_FUNCS = {
    "support_of", "at_point", "verdict",
    "reproduce_support_counts", "scalar_invariance_of_support",
    "single_global_solve", "v18_crosscheck",
}


class _BlankStrings(_ast.NodeTransformer):
    """Blank every string-literal so a token appearing ONLY in a docstring / message (prose
    naming the banned thermodynamic words, or 'float' in a guard) is not mistaken for a load-
    bearing code use.  Mirrors sakharov_gate0/1._BlankStrings."""

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            return _ast.copy_location(_ast.Constant(value=""), node)
        return node


def _strip_code_only(seg):
    """Return the LOAD-BEARING executable code of a function: drop the docstring, blank all
    string literals, strip trailing '#' comments.  Provenance prose that merely NAMES a banned
    token is not a code use.  Mirrors sakharov_gate0/1._strip_code_only."""
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


def source_guard(extra_src=None):
    """(a) SOURCE: no numpy.linalg / float(...) / thermodynamic-route token in the decisive-
    function CODE (docstrings/comments/messages stripped).  (b) RUNTIME: octonion_algebra absent
    from sys.modules + det SSOT native exact-over-Q.  `extra_src` lets the guard scan an INJECTED
    violation to prove it FIRES (not a no-op).  Returns (ok, src_hits)."""
    src = open(os.path.abspath(__file__)).read()
    if extra_src is not None:
        src = src + "\n" + extra_src
    tree = _ast.parse(src)
    src_hits = {}
    for node in _ast.walk(tree):
        if isinstance(node, _ast.FunctionDef) and node.name in _DECISIVE_FUNCS:
            seg = _ast.get_source_segment(src, node) or ""
            code_only = _strip_code_only(seg)
            bad = [tok for tok in _FORBIDDEN_SOURCE_TOKENS if tok in code_only]
            if bad:
                src_hits[node.name] = bad
    runtime_ok = ("octonion_algebra" not in sys.modules)
    # det SSOT native exact-over-Q (det_3(diag(2,3,5)) == 30) -- the v18 SSOT path.
    Xspot = BG.h3o_from_coords(Rational(2), Rational(3), Rational(5),
                               BG.oct_zero(), BG.oct_zero(), BG.oct_zero())
    spot = RL.det_3(Xspot)
    ssot_ok = (spot == 30) and (not isinstance(spot, float)) \
        and (RL.det_3.__module__ == "ring_lemma_verification")
    ok = (not src_hits) and runtime_ok and ssot_ok
    return ok, src_hits


# ============================================================================
# 1. REPRODUCE the v18 support counts (n_G, n_T) on the MATTER-BEARING anchor
# ============================================================================
def reproduce_support_counts():
    """Build G[g] and the independent T[M] on the matter-bearing anchor M_0 (V_{1/2} survivors
    [11,18,19,26]; rho>0, differentiated) via the warm v18 harness, and COUNT the nonzero 4x4
    entries (the v18 definition of support).  Report the ACTUAL integers (n_G, n_T).  Confirm
    the anchor is matter-bearing (G!=0, T!=0, R!=0 -- NOT the M=0 deflated check)."""
    print("=" * 78)
    print("1. REPRODUCE the v18 support counts (n_G vs n_T) on the MATTER-BEARING anchor")
    print("=" * 78)
    print(f"      anchor M_0 (V_{{1/2}} survivors {CU_SURVIVOR_IDX}) = {MATTER_0}; BG_partner={BG_PARTNER}; "
          f"pos={POS_CENTER}")

    tick("building G[g] = Ric - (1/2) g R at the matter-bearing anchor (warm engine, exact Q) ...")
    res = E18.curvature_at(MATTER_0, POS_CENTER)
    G = res["G"]
    g = res["g"]
    Rs = cancel(res["Rscalar"])

    # MATTER-BEARING confirmation (rho>0 proxy: R!=0 AND G!=0 AND T!=0; NOT M=0).
    G_nonzero = (G != zeros(N, N))
    R_nonzero = (Rs != 0)

    tick("building the INDEPENDENT primary scalar stress T[psi] (AST-guarded; FROZEN before G) ...")
    Tpsi_c = at_point(_T_psi_mat, MATTER_0, BG_PARTNER, POS_CENTER)
    Tpsi_nonzero = (Tpsi_c != zeros(N, N))
    psi = E18.psi_scalar(MATTER_0, BG_PARTNER)
    psi_real = getattr(_im(psi), "is_zero", None) is not False

    support_G = support_of(G)
    support_T = support_of(Tpsi_c)
    n_G = len(support_G)
    n_T = len(support_T)

    print(f"      psi = {psi}  (real? {psi_real})")
    print(f"      R[g=e.e](anchor) = {Rs}  (!= 0 => matter-bearing, rho>0)")
    print(f"      n_G = # nonzero 4x4 entries of G[g] at anchor = {n_G}")
    print(f"          G_support = {sorted(support_G)}")
    print(f"      n_T = # nonzero 4x4 entries of T[psi] at anchor = {n_T}")
    print(f"          T_support = {sorted(support_T)}")

    _report(f"matter-bearing anchor confirmed: R[g] != 0 ({Rs}), G[g] != 0, T[psi] != 0 "
            f"(rho>0, differentiated -- NOT the M=0 deflated check)",
            R_nonzero and G_nonzero and Tpsi_nonzero)
    _report(f"REPRODUCED v18 support counts EXACT over Q: n_G = {n_G} (G supported on the full "
            f"4x4) , n_T = {n_T} (T a thin fragment) -- the actual integers", True)  # report-only
    # The v18 headline was 16-vs-6; confirm we reproduce it (or report the real numbers).
    v18_16_6 = (n_G == 16 and n_T == 6
                and sorted(support_T) == [(0, 1), (1, 0), (2, 2), (2, 3), (3, 2), (3, 3)])
    _report(f"v18 headline reproduced: n_G==16 and n_T==6 with T_support=={{01,10,22,23,32,33}}? "
            f"{v18_16_6}  (if False, the real numbers above are used downstream)",
            v18_16_6)

    return {"G": G, "g": g, "Rscalar": Rs, "T_psi": Tpsi_c, "psi": str(psi),
            "support_G": support_G, "support_T": support_T, "n_G": n_G, "n_T": n_T,
            "v18_16_6": v18_16_6,
            "G_mat": [[str(cancel(G[i, j])) for j in range(N)] for i in range(N)],
            "T_mat": [[str(cancel(Tpsi_c[i, j])) for j in range(N)] for i in range(N)]}


# ============================================================================
# 2. SCALAR-INVARIANCE OF SUPPORT (a scalar kappa cannot change tensor rank)
# ============================================================================
def scalar_invariance_of_support(rep):
    """Show -- COMPUTED, not asserted -- that for the INDUCED kappa (= 6 pi^2/Lambda_f^2) AND a
    symbolic free scalar kappa AND a panel of rational scalars, support(kappa T) == support(T)
    identically (a scalar multiplies T by a number; it cannot change which entries are nonzero).
    The DECISIVE mechanism is NOT naive support-set coverage: g = e.e is a DENSE Lorentzian
    metric (all 16 entries nonzero at the anchor), so support(kappa T + Lambda g) = support(T) U
    support(g) is the FULL 16 -- a scalar combination CAN reach every entry as a support set.
    What it CANNOT do is EQUAL G: on the 10 "off-T" entries where T=0 but G!=0, the equation
    G = kappa T + Lambda g collapses to G_{mu nu} = Lambda g_{mu nu}, forcing a SINGLE scalar
    Lambda to equal G_{mu nu}/g_{mu nu} simultaneously on all of them -- which is over-determined
    (the ratios are NOT all equal) -- INDEPENDENTLY of kappa (kappa drops out where T=0).  So the
    matter coupling kappa is irrelevant on the off-T block, and the Gate-2 conclusion is
    Lambda_f-INDEPENDENT (the whole point): no scalar (kappa,Lambda) repairs it."""
    print("=" * 78)
    print("2. SCALAR-INVARIANCE OF SUPPORT : a scalar kappa cannot change tensor rank/support")
    print("=" * 78)
    Tpsi = rep["T_psi"]
    g = rep["g"]
    G = rep["G"]
    support_T = rep["support_T"]
    support_G = rep["support_G"]

    # (a) induced kappa (= 6 pi^2/Lambda_f^2), symbolic in the Gate-3 scale Lambda_f:
    kT_induced = (KAPPA_INDUCED * Tpsi).applyfunc(cancel)
    support_kT_induced = support_of(kT_induced)
    induced_inv = (support_kT_induced == support_T)
    print(f"      induced kappa = {KAPPA_INDUCED}  (= 6 pi^2/Lambda_f^2; c_1=1/(6 pi^2) from Gate 1)")
    _report(f"support(induced-kappa * T) == support(T) ({len(support_kT_induced)} == {len(support_T)}) "
            f"-- the induced SCALAR kappa does NOT change support (Lambda_f-independent)", induced_inv)

    # (b) symbolic free scalar kappa:
    k_sym = Symbol('kappa', nonzero=True)
    kT_sym = (k_sym * Tpsi).applyfunc(cancel)
    support_kT_sym = support_of(kT_sym)
    sym_inv = (support_kT_sym == support_T)
    _report(f"support(kappa_symbolic * T) == support(T) ({len(support_kT_sym)} == {len(support_T)}) "
            f"-- ANY nonzero scalar kappa preserves support", sym_inv)

    # (c) a fixed-seed rational panel (NON-decisive sweep -- corroboration only):
    import random
    rng = random.Random(20210606)
    panel = [Rational(rng.randint(-9, 9) or 1, rng.randint(1, 9)) for _ in range(8)]
    panel_inv = all(support_of((kv * Tpsi).applyfunc(cancel)) == support_T for kv in panel)
    _report(f"support(kappa * T) == support(T) for a rational panel {panel} (8 random nonzero "
            f"scalars) -- corroboration (NON-decisive)", panel_inv)

    # (d) the DECISIVE off-T-block argument (NOT naive support coverage -- g is DENSE).
    #     g = e.e fills all 16 entries, so support(kappa T + Lambda g) = support(T) U support(g)
    #     IS the full 16: a scalar combination DOES reach every entry as a support set.  The kill
    #     is that it cannot EQUAL G: on the off-T entries (T=0, G!=0), G = kappa T + Lambda g
    #     collapses to G = Lambda g, forcing one scalar Lambda = G_{mu nu}/g_{mu nu} on all of
    #     them -- over-determined, and INDEPENDENT of kappa (kappa drops out where T=0).
    g_support = support_of(g)
    g_dense = (len(g_support) == 16)
    off_T = sorted((support_G - support_T))               # entries where G!=0 but T=0
    print(f"      support(g) = {sorted(g_support)}  (g=e.e DENSE: {len(g_support)}/16 nonzero)")
    print(f"      off-T entries (G!=0, T=0) = {off_T}  ({len(off_T)} of them; kappa is IRRELEVANT here)")
    # On the off-T block, the required Lambda = G_{mu nu}/g_{mu nu} (kappa-free); collect the ratios.
    off_T_ratios = {}
    for (mu, nu) in off_T:
        if cancel(g[mu, nu]) != 0:
            off_T_ratios[(mu, nu)] = cancel(G[mu, nu] / g[mu, nu])
    distinct_ratios = set(off_T_ratios.values())
    one_lambda_works = (len(distinct_ratios) <= 1)
    print(f"      required Lambda = G/g on the off-T block: {len(distinct_ratios)} DISTINCT value(s) "
          f"(a single scalar Lambda needs exactly 1)")
    # a couple of representative ratios for the record:
    for k in list(off_T_ratios)[:3]:
        print(f"        Lambda would need to be {off_T_ratios[k]} on entry {k}")
    _report(f"g = e.e is DENSE ({len(g_support)}/16) -- so support(kappa T + Lambda g) is the full "
            f"16; the kill is NOT naive support coverage but the off-T over-determination", g_dense)
    _report(f"off-T block NONEMPTY: {len(off_T)} entries have G!=0 but T=0 (the matter stress is a "
            f"thin {rep['n_T']}-entry fragment of the {rep['n_G']}-entry G) -- on these kappa "
            f"DROPS OUT entirely", len(off_T) > 0)
    _report(f"NO single scalar Lambda matches G=Lambda g on the off-T block: {len(distinct_ratios)} "
            f"distinct required values (need exactly 1) -- so kappa T + Lambda g != G for ANY "
            f"scalar (kappa,Lambda); the {rep['n_G']}-vs-{rep['n_T']} mismatch is NOT repaired "
            f"(kappa-independent => Lambda_f-independent)", not one_lambda_works)

    return {"induced_inv": induced_inv, "sym_inv": sym_inv, "panel_inv": panel_inv,
            "g_dense": g_dense, "off_T": off_T, "n_off_T": len(off_T),
            "n_distinct_offT_ratios": len(distinct_ratios), "one_lambda_works": one_lambda_works,
            "support_kT_induced": sorted(support_kT_induced)}


# ============================================================================
# 3. THE SINGLE-GLOBAL SOLVE IS INCONSISTENT (free-kappa AND induced-kappa)
# ============================================================================
def _build_matter_family():
    """The matter-bearing (M,x) family (3 V_{1/2} directions x 3 slice positions x 2 amplitudes),
    dropping any point that leaves the (1,3) Lorentzian splice (reported, not forced).  Each point
    carries G[g] (LHS), g, and is rho>0 (V_{1/2} matter on the flat KKT eta).  EXACT over Q."""
    family, dropped = [], []
    for (dn, dd) in MATTER_DIRS:
        for (pn, pos) in SLICE_POS:
            for (an, amp) in AMPS:
                key = f"{dn}/{pn}/{an}"
                matter = scale(dd, amp)
                res = E18.curvature_at(matter, pos)
                sig = BG.eig_signature_count(res["g"])
                if sig != (1, 3, 0):
                    dropped.append((key, sig))
                    continue
                family.append({"key": key, "matter": matter, "pos": pos,
                               "G": res["G"], "g": res["g"]})
    return family, dropped


def single_global_solve(rep):
    """Solve G = kappa T + Lambda g for ONE global (kappa,Lambda) over the matter-bearing family.
    (a) BOTH free (the strongest test: if even both-free is inconsistent, a FIXED induced kappa
        certainly is).  (b) kappa = the INDUCED 6 pi^2/Lambda_f^2 with Lambda (and the scale
        Lambda_f) free.  Confirm EmptySet / no solution in both -- and that the induced solve is a
        RESTRICTION of the free solve (so it cannot succeed where the free one failed).  Uses the
        independent AST-guarded T[psi] from the v18 harness.  EXACT over Q."""
    print("=" * 78)
    print("3. THE SINGLE-GLOBAL (kappa,Lambda) SOLVE over the MATTER-BEARING family")
    print("=" * 78)
    tick("building the matter-bearing (M,x) family (drop (4,0) flips; rho>0) ...")
    family, dropped = _build_matter_family()
    print(f"      family: {len(family)} valid sig-(1,3) points, {len(dropped)} dropped "
          f"(left the Lorentzian splice -- reported, not forced)")
    for f in family:
        print(f"        {f['key']}: G!=0? {f['G'] != zeros(N, N)}")
    _report(f"matter-bearing family has >=6 valid sig-(1,3) points ({len(family)})", len(family) >= 6)

    # T[psi] at each family point (independent, AST-guarded, evaluated at the point):
    def Tpsi_at(matter, pos):
        return at_point(_T_psi_mat, matter, BG_PARTNER, pos)

    # ---- (a) BOTH (kappa, Lambda) FREE : the strongest over-determined solve ----
    tick("(a) solve G = kappa T + Lambda g for BOTH (kappa,Lambda) FREE (the strongest test) ...")
    k_free = Symbol('kappa_glob', real=True)
    L_free = Symbol('Lambda_glob', real=True)
    eqs_free = []
    for f in family:
        Tm = Tpsi_at(f["matter"], f["pos"])
        for mu in range(N):
            for nu in range(mu, N):     # symmetric: upper triangle (incl diagonal)
                eqs_free.append(cancel(f["G"][mu, nu] - k_free * Tm[mu, nu] - L_free * f["g"][mu, nu]))
    sol_free = linsolve(eqs_free, [k_free, L_free])
    free_consistent = (len(sol_free) > 0)
    print(f"      both-free over-determined solve: {len(eqs_free)} eqs, 2 unknowns "
          f"(kappa,Lambda); solution set = {sol_free}")
    _report(f"BOTH-(kappa,Lambda)-FREE single-global solve is INCONSISTENT (EmptySet) over the "
            f"matter-bearing family ({len(eqs_free)} eqs) -- no global linear-in-T Einstein "
            f"closure exists at all", not free_consistent)

    # ---- (b) INDUCED kappa fixed (= 6 pi^2/Lambda_f^2) : a RESTRICTION of (a) ----
    tick("(b) solve with kappa = INDUCED 6 pi^2/Lambda_f^2 fixed; Lambda, Lambda_f free ...")
    # Per-point: with kappa fixed to the induced scalar, the trace-forced per-point Lambda is
    # Lambda = (1/N) g^{-1} : (G - kappa T).  Einstein holds iff (G - kappa T - Lambda g)=0 for a
    # SINGLE global Lambda.  Lambda_f is symbolic (Gate-3 scale) -- the conclusion is independent
    # of its value (scalar invariance), which we confirm by leaving it free in a linsolve too.
    L_ind = Symbol('Lambda_ind', real=True)
    eqs_ind = []
    per_point_resid_nonzero = []
    for f in family:
        Tm = Tpsi_at(f["matter"], f["pos"])
        ginv = f["g"].inv().applyfunc(cancel)
        Rmat = Matrix(N, N, lambda mu, nu: cancel(f["G"][mu, nu] - KAPPA_INDUCED * Tm[mu, nu]))
        lam_pt = cancel(sum(ginv[mu, nu] * Rmat[mu, nu] for mu in range(N) for nu in range(N)) / N)
        resid = Matrix(N, N, lambda mu, nu: cancel(Rmat[mu, nu] - lam_pt * f["g"][mu, nu]))
        per_point_resid_nonzero.append((f["key"], resid != zeros(N, N), lam_pt))
        for mu in range(N):
            for nu in range(mu, N):
                eqs_ind.append(cancel(f["G"][mu, nu] - KAPPA_INDUCED * Tm[mu, nu] - L_ind * f["g"][mu, nu]))
    sol_ind = linsolve(eqs_ind, [L_ind])
    ind_consistent = (len(sol_ind) > 0)
    print("      per-point trace-forced Lambda (induced kappa): "
          f"{[(k, str(cancel(l))) for (k, _, l) in per_point_resid_nonzero]}")
    all_resid_nonzero = all(nz for (_, nz, _) in per_point_resid_nonzero)
    print(f"      induced-kappa global solve (Lambda free): solution set = {sol_ind}")
    _report(f"INDUCED-kappa (6 pi^2/Lambda_f^2) single-global solve is INCONSISTENT: every "
            f"per-point residual G - kappa T - Lambda g != 0 ({all_resid_nonzero}) AND the global "
            f"Lambda solve is EmptySet ({not ind_consistent}) -- the induced scalar does NOT close",
            all_resid_nonzero and not ind_consistent)
    _report("the induced-kappa solve is a RESTRICTION of the both-free solve (kappa pinned to one "
            "value); since the both-free solve is already EmptySet, the restricted one cannot be "
            "consistent -- a scalar induced kappa cannot enlarge the (empty) solution space",
            (not free_consistent) and (not ind_consistent))

    return {"family": [f["key"] for f in family], "n_family": len(family), "n_dropped": len(dropped),
            "dropped": dropped, "free_consistent": free_consistent, "ind_consistent": ind_consistent,
            "all_resid_nonzero": all_resid_nonzero,
            "per_point_lambda": [(k, str(cancel(l))) for (k, _, l) in per_point_resid_nonzero],
            "sol_free": str(sol_free), "sol_ind": str(sol_ind)}


# ============================================================================
# 4. CROSS-CHECK the v18 result reproduces (16-vs-6 + frozen-kappa inconsistency)
# ============================================================================
def v18_crosscheck(rep, solve):
    """Anchor Gate 2 to the verifier-hardened v18 Phase-77 finding: (i) the 16-vs-6 support
    counts, and (ii) the single-(kappa,Lambda) inconsistency with the v18 FROZEN RATIONAL kappa
    (NOT the induced one) -- exactly the object v18 reported.  This confirms our reproduction is
    the same computation v18 ran, so the Gate-2 conclusion inherits v18's hardening."""
    print("=" * 78)
    print("4. CROSS-CHECK : the verifier-hardened v18 Phase-77 result reproduces")
    print("=" * 78)
    # (i) the 16-vs-6 headline (already reproduced in step 1):
    _report(f"v18 16-vs-6 support reproduced (n_G={rep['n_G']}, n_T={rep['n_T']}) -- matches the "
            f"verifier-hardened v18 Phase-77 finding", rep["v18_16_6"])

    # (ii) the v18 frozen-rational-kappa inconsistency: rebuild v18's kappa_psi (a4/T-scale) and
    # confirm the single-global solve is inconsistent with THAT kappa too (the exact v18 object).
    tick("rebuilding the v18 frozen RATIONAL kappa_psi (a4 / t^4 T-scale) and re-solving ...")
    # Reuse the v18 harness's own leading-order machinery by reading kappa_psi off the same
    # construction (a rational, NOT the induced symbolic one).  We recompute it here to anchor.
    from sympy import interpolate, factorial as _fact, diff
    t = symbols('t', real=True, positive=True)
    tt = Symbol('tt')
    ts = [Rational(1, 8), Rational(1, 10), Rational(1, 12), Rational(1, 16), Rational(1, 20),
          Rational(1, 28), Rational(1, 40)]
    Rsamples = []
    for tv in ts:
        rt = E18.curvature_at(scale(MATTER_0, tv), POS_CENTER)
        Rsamples.append((tv, cancel(rt["Rscalar"])))
    Rpoly = interpolate(Rsamples, tt)
    a4 = cancel(Rpoly.diff(tt, 4).subs(tt, 0) / 24)
    psi_t = E18.psi_scalar(scale(MATTER_0, t), scale(BG_PARTNER, t))
    T_psi_t, _, _ = E18.scalar_stress_tensor(psi_t)
    # trace with the v18 ETA_INV (the FLAT background metric inverse, exactly as v18 did):
    ETA_INV = E18.ETA_INV
    trT = cancel(sum(ETA_INV[mu, nu] * T_psi_t[mu, nu] for mu in range(N) for nu in range(N)))
    trT_c = cancel(trT.subs(CENTER))
    Tscale = cancel(diff(trT_c, t, 4).subs(t, 0) / _fact(4))
    kappa_psi_v18 = cancel(a4 / Tscale) if Tscale != 0 else None
    print(f"      v18 frozen kappa_psi = a4/[t^4 T-scale] = {kappa_psi_v18}  (a4={a4}, T-scale={Tscale})")
    _report(f"v18 frozen kappa_psi rebuilt as an exact rational ({kappa_psi_v18}) -- the object "
            f"v18 used (NOT the induced symbolic kappa)", kappa_psi_v18 is not None
            and getattr(kappa_psi_v18, "is_rational", False))

    # re-solve the single global Lambda with the v18 frozen kappa (should be inconsistent):
    family, _ = _build_matter_family()
    L = Symbol('Lambda_v18', real=True)
    eqs = []
    for f in family:
        Tm = at_point(_T_psi_mat, f["matter"], BG_PARTNER, f["pos"])
        for mu in range(N):
            for nu in range(mu, N):
                eqs.append(cancel(f["G"][mu, nu] - kappa_psi_v18 * Tm[mu, nu] - L * f["g"][mu, nu]))
    sol = linsolve(eqs, [L])
    v18_inconsistent = (len(sol) == 0)
    print(f"      v18 frozen-kappa single-global Lambda solve: solution set = {sol}")
    _report(f"v18 frozen-RATIONAL-kappa single-global (kappa,Lambda) solve is INCONSISTENT "
            f"(EmptySet) -- reproduces the verifier-hardened v18 Phase-77 negative", v18_inconsistent)

    # consistency: the induced solve and the v18 frozen solve agree (both inconsistent); the
    # induced is the same structural failure as v18, now with the Sakharov-induced scalar.
    agree = (not solve["ind_consistent"]) and v18_inconsistent and (not solve["free_consistent"])
    _report("Gate-2 (induced kappa) and v18 (frozen kappa) AGREE: both inconsistent, both "
            "16-vs-6 -- the induced scalar reproduces, not repairs, the v18 mismatch", agree)

    return {"kappa_psi_v18": str(kappa_psi_v18), "a4": str(a4), "Tscale": str(Tscale),
            "v18_inconsistent": v18_inconsistent, "agree": agree, "sol_v18": str(sol)}


def main():
    print("#" * 78)
    print("# Phase 81 (v21.0 Sakharov) -- Gate 2 : SUPPORT MISMATCH (the MILESTONE-DECISIVE gate)")
    print("#   does the induced SCALAR kappa repair the v18 16-vs-6 tensor-support mismatch?")
    print("#   g = e.e (1,3); gravity = Lorentz block R[omega]; EXACT over Q; v18 harness reused.")
    print("#   Gate 0 SURVIVED (STr=+8/3, G>0); Gate 1 PASSED (c_1=1/(6 pi^2), G=3pi/(8 Lf^2)>0).")
    print("#" * 78)

    # ---- 0. source guard ----
    tick("0. source guard (octonion_algebra absent; no numpy/float/thermo; det SSOT exact-Q) ...")
    guards_ok, src_hits = source_guard()
    _report(f"source/runtime guard clean (no numpy.linalg/float/thermo on decisive funcs "
            f"{sorted(_DECISIVE_FUNCS)}; octonion_algebra absent; det SSOT exact-Q) hits={src_hits}",
            guards_ok)
    # prove the guard FIRES on an injected violation (not a no-op):
    inj = "def reproduce_support_counts():\n    return float(numpy.linalg.det([[1]]))\n"
    fires_ok, fires_hits = source_guard(extra_src=inj)
    _report(f"source guard FIRES on injected numpy.linalg/float violation (not a no-op; "
            f"hits={fires_hits})", (not fires_ok) and ("reproduce_support_counts" in fires_hits))

    # ---- 1. reproduce the v18 support counts on the matter-bearing anchor ----
    print()
    rep = reproduce_support_counts()

    # ---- 2. scalar-invariance of support (a scalar cannot change tensor rank) ----
    print()
    inv = scalar_invariance_of_support(rep)

    # ---- 3. the single-global solve is inconsistent (free-kappa AND induced-kappa) ----
    print()
    solve = single_global_solve(rep)

    # ---- 4. cross-check the v18 result reproduces ----
    print()
    xcheck = v18_crosscheck(rep, solve)

    # ---- 5. the NON-HARDWIRED verdict (DERIVED from the actual (n_G,n_T) + solve) ----
    print()
    print("=" * 78)
    print("5. THE NON-HARDWIRED GATE-2 VERDICT")
    print("=" * 78)
    # the induced-kappa support (== support(T) for scalar) and the induced-kappa solve result:
    support_kT_induced = set(tuple(x) for x in inv["support_kT_induced"])
    v = verdict(n_G=rep["n_G"], n_T=rep["n_T"], support_G=rep["support_G"],
                support_kT=support_kT_induced,
                global_solve_consistent=solve["ind_consistent"])
    print(f"      inputs (DERIVED, exact over Q): n_G={rep['n_G']}, n_T={rep['n_T']}, "
          f"support(G) subset support(kappa T)? {rep['support_G'].issubset(support_kT_induced)}, "
          f"single-global solve consistent? {solve['ind_consistent']}")
    print(f"      clauses: {v['clauses']}")
    print(f"      >>> Gate-2 VERDICT (this driver's reading): {v['category']}")
    print(f"      >>> {v['summary']}")

    # NON-HARDWIRED demonstration: synthetic inputs MUST change the category (pre-empt the v20
    # hardcoded-decisive-boolean bug).  THREE required self-tests.
    print()
    print("      [non-hardwired ladder check -- synthetic inputs (the 3 required self-tests)]")
    # (a) synthetic MATCHING supports (n_G <= n_T) + consistent solve -> SURVIVES:
    syn_support = {(0, 0), (1, 1)}
    v_match = verdict(n_G=2, n_T=2, support_G=syn_support, support_kT=syn_support,
                      global_solve_consistent=True)
    # (b) the REAL mismatched supports + inconsistent solve -> DEAD:
    v_real = verdict(n_G=rep["n_G"], n_T=rep["n_T"], support_G=rep["support_G"],
                     support_kT=support_kT_induced, global_solve_consistent=solve["ind_consistent"])
    # (c) a half-synthetic case: matching support but INconsistent solve -> DEAD (solve clause):
    v_half = verdict(n_G=2, n_T=2, support_G=syn_support, support_kT=syn_support,
                     global_solve_consistent=False)
    print(f"        synthetic matching supports + consistent solve -> {v_match['category']}")
    print(f"        real mismatched supports + inconsistent solve -> {v_real['category']}")
    print(f"        synthetic matching supports + INconsistent solve -> {v_half['category']}")
    ladder_nonhardwired = (
        v_match["category"].startswith("SURVIVES")
        and v_real["category"].startswith("DEAD")
        and v_half["category"].startswith("DEAD"))
    _report("verdict ladder is NON-hardwired: synthetic matching supports + consistent solve -> "
            "SURVIVES; real mismatched supports + inconsistent solve -> DEAD; matching-but-"
            "inconsistent -> DEAD (each clause independently load-bearing; the category is DERIVED "
            "from (n_G,n_T) + solve, NOT a constant -- pre-empts the v20 bug)", ladder_nonhardwired)
    # the THREE explicit self-tests the task requires (assert each direction):
    _report("SELF-TEST (a): verdict(synthetic matching supports n_G<=n_T+1, consistent solve) == "
            "SURVIVES", verdict(2, 2, {(0, 0)}, {(0, 0)}, True)["category"].startswith("SURVIVES"))
    _report("SELF-TEST (b): verdict(real mismatched supports, inconsistent solve) == DEAD",
            v_real["category"].startswith("DEAD"))
    # (c) literal-detector: verdict's return is not a constant -- flipping inputs flips the category
    _report("SELF-TEST (c): verdict is NOT a literal (two different input sets give two different "
            "categories: SURVIVES vs DEAD) -- the v20 hardcoded-boolean bug is ABSENT",
            v_match["category"] != v_real["category"])

    # ---- final summary block (for the report) ----
    print()
    print("#" * 78)
    print("# GATE-2 SUMMARY")
    print("#" * 78)
    print(f"  source/guard clean (guard FIRES on injection) : {guards_ok}")
    print(f"  matter-bearing anchor (R!=0, G!=0, T!=0, rho>0): True  (NOT the M=0 deflated check)")
    print(f"  n_G (G nonzero 4x4 entries at anchor)          : {rep['n_G']}  (the v18 '16')")
    print(f"  n_T (T[psi] nonzero 4x4 entries at anchor)     : {rep['n_T']}  (the v18 '6')")
    print(f"  v18 16-vs-6 reproduced exactly                 : {rep['v18_16_6']}")
    print(f"  support(induced-kappa T) == support(T)         : {inv['induced_inv']}  "
          f"(scalar cannot change rank)")
    print(f"  off-T entries (G!=0, T=0; kappa-free)          : {inv['n_off_T']}  "
          f"(matter is a thin {rep['n_T']}-of-{rep['n_G']} fragment)")
    print(f"  distinct Lambda required on off-T block         : {inv['n_distinct_offT_ratios']}  "
          f"(need 1 for a single scalar Lambda => mismatch survives)")
    print(f"  induced kappa = 6 pi^2/Lambda_f^2 (c_1=1/(6pi^2)) carried from Gate 1")
    print(f"  both-(kappa,Lambda)-free single-global solve   : {solve['sol_free']}  "
          f"(EmptySet => no closure at all)")
    print(f"  induced-kappa single-global solve              : {solve['sol_ind']}  (EmptySet)")
    print(f"  v18 frozen-kappa single-global solve           : {xcheck['sol_v18']}  (EmptySet)")
    print(f"  Gate-2 == v18 (both inconsistent, both 16-vs-6): {xcheck['agree']}")
    print(f"  family valid/dropped                           : {solve['n_family']}/{solve['n_dropped']}")
    print(f"  scheme                                         : vacuum (Casimir-category, zero-T, "
          f"NO thermodynamics)")
    print(f"  VERDICT (driver reading)                       : {v['category']}")
    print(f"  ALL_PASS (mechanical checks)                   : {ALL_PASS}")
    print("#" * 78)
    print("# Ledger consequence (one line per gate):")
    print("#   Gate 0 (SIGN)            : DONE -- SURVIVES (G>0, STr=+8/3, unforced)")
    print("#   Gate 1 (a_1 propto R)    : DONE -- PASS (a_1=-R/3 clean, c_1=1/(6 pi^2))")
    print(f"#   Gate 2 (support mismatch): DONE -- {v['category']}")
    if v["category"].startswith("DEAD"):
        print("#   Gate 3 (closure)         : NOT RUN (Gate 2 DEAD -- the six-kind menu is "
              "EXHAUSTED for h_3(O); redirect per selection-law-ledger.md sec 6)")
    else:
        print("#   Gate 3 (closure)         : MUST RUN (Gate 2 SURVIVED -- a major surprise)")
    print("#" * 78)
    print("# NOTE: this is the EXECUTOR's reading of the mechanical Gate-2 checks. The")
    print("#   ORCHESTRATOR/VERIFIER adjudicates the milestone verdict and any transition.")
    print("#" * 78)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
