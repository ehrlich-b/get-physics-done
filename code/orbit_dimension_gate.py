"""
(RING) Lemma — f_4 Construction + Orbit-Dimension GATE  --  Phase 65, Plan 01
=============================================================================
Phase: 65-f-4-construction-orbit-dimension-gate, Plan: 01  (BASE-02 GATE)
Milestone: v16.0 The (RING) Lemma (math half of the Chalmers gap).

This is the BUILDER half of the chain-critical orbit-dimension GATE. It builds
f_4 = Der(h_3(O)) explicitly as the 52-dimensional span of the inner derivations
{[L_a, L_b]} (27x27 rational matrices), COMPUTES dim f_4 = 52 over Q (it is NOT
assumed from the literature -- the famous number 52 is a CONFIRMATION here, not a
premise; see forbidden proxy fp-assume-dim52), verifies the span is closed under
the Lie bracket, and certifies that every generator infinitesimally annihilates
the three single-copy invariants {Tr, Tr^2, det_3} EXACTLY over Q at genuinely
octonionic points.

WHY THIS IS THE GATE: the 52 f_4 generators and the infinitesimal-invariance
certificate are the prerequisite for the single-copy sanity GATE (Plan 02,
orbit 24) and the pair orbit-dimension value (Plan 03). A wrong builder silently
corrupts the entire downstream milestone, so dim 52 and the F_4-invariance of
det_3 are COMPUTED here, not assumed. Per the Derksen-Kemper char-0 criterion an
invariant is annihilated by the infinitesimal action of the Lie algebra; the
D_M f = 0 certificate below is the CONTINUOUS-group F_4-invariance statement that
finite-group sampling cannot establish.

PROVENANCE  (the DECISIVE reuse -- not an oracle)
-------------------------------------------------
This module PATH-IMPORTS the FROZEN Phase 64 + 64.1 exact-SymPy engine
code/ring_lemma_verification.py VERBATIM (the two files live together in code/).
The frozen engine ports/pins the exact octonion arithmetic (Fano e1e2=e4), the
3x3 octonion matmul, the Jordan product jordan=(1/2)(AB+BA), the Phase-64.1
CORRECTED generic norm det_3 (cross term (x2 x1) x3 -- NOT octonion_algebra.py's
buggy (x1 x2) x3), Tr / Tr2, the engine-native 27-per-copy coordinate layout
(X_from_symbols / _flat27 / _standard_basis_27), jordan_L_matrix (L_A as a 27x27
matrix), inner_derivations() (the 324 nonzero brackets whose span is f_4), and
octonionic_points(). We do NOT re-derive octonion arithmetic and we do NOT
re-freeze det_3. The frozen engine's permanent LOCK 7a/7b guards det_3.

CONVENTION (carry verbatim from the frozen engine):
# ASSERT_CONVENTION: jordan=(1/2)(AB+BA); fano e1e2=e4; det3 cross=2Re((x2x1)x3) [generic norm; Phase64.1 factor-order fix]; det3_normalization d(X,X,X)=6*det_3; coupling c=Tr(X o Y); f4=span{[L_a,L_b]} dim 52; arithmetic=exact-SymPy-over-Q; ranks=sympy.Matrix.rank() over QQ; NEVER float64 / numpy.linalg.matrix_rank on the decisive path
# REP-DECOMP: 27 = 1 (trivial/Tr direction) (+) 26 (trace-free irreducible)

Assert-based harness (NO pytest -- the executor venv has sympy/numpy only).
Runnable directly:  python3 code/orbit_dimension_gate.py
Exits 0 iff ALL_PASS (every Plan-01 check passes); nonzero on any failure.

Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0. Deterministic
(no random seeds; all test elements are the frozen engine's hardcoded exact
rational points). NumPy 2.4.2 is present but FORBIDDEN on the decisive/rank path.

References:
  Schafer, R.D. -- An Introduction to Nonassociative Algebras (1966): inner
    derivations [L_a,L_b] span Der(J); Der(h_3(O)) = f_4; each preserves the
    generic norm. Justifies the inner-derivation builder.
  Jacobson, N. -- Structure and Representations of Jordan Algebras (1968):
    [L_a,L_b] in Der(J); derivations of the simple Albert algebra are all inner,
    dim 52. Justifies span{[L_a,L_b]} IS the full f_4 and is bracket-closed.
  Derksen, H.; Kemper, G. -- Computational Invariant Theory, Sec 4: char-0
    criterion -- an invariant is annihilated by the infinitesimal action of the
    Lie algebra; orbit dim = rank of infinitesimal action at a generic point.
    Justifies the D_M f = 0 invariance certificate (here) and the orbit-rank GATE
    (Plans 02/03).
  Garibaldi, S.; Guralnick, R. -- arXiv:2308.08214 (F_4 on 26 -> generic
    stabilizer Spin(8) dim 28, orbit 24, trdeg 3): the single-copy anchor,
    reproduced in-engine in Plan 02. Cited here because builder correctness is
    what makes the single-copy 24 meaningful.
  code/ring_lemma_verification.py (VALD-64-01) -- the FROZEN exact-SymPy engine.
"""

import os
import re
import sys

# Path-import the FROZEN engine (sibling file in code/). Mirror the engine's own
# sibling-touch pattern; here it is the DECISIVE reuse, not an oracle.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ring_lemma_verification as E  # noqa: E402  (path insert must precede import)

from sympy import Matrix, diff, simplify, Rational  # noqa: E402

# Track overall pass/fail; the script must exit nonzero on any check failure.
ALL_PASS = True


def _report(label, ok):
    """Print a PASS/FAIL line and fold into the global pass flag (engine pattern)."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok:
        ALL_PASS = False
    return ok


# ============================================================================
# Helpers (built ON TOP of the frozen engine; no re-derivation of algebra)
# ============================================================================

def _flatten_729(M):
    """Row-major flatten of a 27x27 SymPy matrix to a length-729 list.

    Consistent row-major order (r outer, col inner) is used EVERYWHERE a 27x27
    derivation matrix is turned into a span vector, so the stacked rank is the
    honest dimension of the span of the matrices."""
    return [M[r, col] for r in range(27) for col in range(27)]


def cached_L_matrices():
    """The 27 cached Jordan left-multiplication matrices L_k = jordan_L_matrix(E_k)
    on the standard basis E_k = _standard_basis_27()[k]. Each is a 27x27 rational
    matrix L_k(Z) = jordan(E_k, Z). Caching avoids rebuilding inside the
    bracket-closure check. (inner_derivations() rebuilds its own L internally; we
    keep an independent cache here for the double-bracket spot check so we never
    re-derive the algebra.)"""
    basis = E._standard_basis_27()
    return [E.jordan_L_matrix(basis[k], basis) for k in range(27)]


def span_rank_over_QQ(matrices, extra=None):
    """Exact span rank over QQ of a list of 27x27 matrices (each row-major
    flattened to 729), optionally with extra 27x27 matrices appended.

    EXACT-ONLY: uses sympy.Matrix(...).rank() over QQ exclusively. numpy rank is
    FORBIDDEN on this decisive path (rank is discontinuous; an SVD tolerance would
    fabricate the dim-52 verdict -- forbidden proxy fp-float-rank)."""
    rows = [_flatten_729(M) for M in matrices]
    if extra:
        rows += [_flatten_729(M) for M in extra]
    return Matrix(rows).rank()


def infinitesimal_action(grad_at, M, v):
    """D_M f at a point: sum_i (df/dx_i)|_v * (M . v)_i, where M acts on the
    coordinate vector v by matrix*vector. grad_at must already be evaluated at v
    (substitute the point FIRST so this sum is over rationals, not symbols)."""
    Mv = M * v
    return sum(grad_at[i] * Mv[i] for i in range(27))


# ============================================================================
# TASK 1 CHECKS — build f_4, dim 52 over Q, derivation identity, bracket closure
# ============================================================================

def check_roundtrip_guard():
    """Defensive round-trip: _flat27(X_from_symbols(v)) == v for a sample integer
    27-vector (NO change-of-basis; the layout is the frozen 27-per-copy layout)."""
    v = [Rational(k + 1) for k in range(27)]
    rt = E._flat27(E.X_from_symbols(v))
    return _report("round-trip guard _flat27(X_from_symbols(v)) == v (no change-of-basis)",
                   rt == v)


def check_dim_f4(derivs):
    """test-dim-52: 324 nonzero inner derivations; span rank over QQ == 52 EXACTLY
    (dim f_4 COMPUTED, not assumed). The count 324 is NOT the dimension."""
    n_ok = _report("inner_derivations() returns 324 nonzero brackets",
                   len(derivs) == 324)
    rk = span_rank_over_QQ(derivs)
    rk_ok = _report(f"span rank over QQ of the 324 brackets == 52 EXACTLY "
                    f"(dim f_4 COMPUTED; rank={rk})",
                    rk == 52)
    return n_ok and rk_ok, rk


def check_derivation_identity(derivs):
    """test-derivation-identity: each sampled generator M is a genuine Jordan
    derivation -- D_M(jordan(X,Y)) == jordan(D_M X, Y) + jordan(X, D_M Y) as an
    exact equality of 27-vectors over Q at >=3 genuinely octonionic points.

    D_M acts by matrix*vector on _flat27 coordinates; reconstruct via
    X_from_symbols to apply jordan. (Leibniz on the Jordan product is the
    DEFINING property of a derivation; if it fails the L-matrix build or the
    jordan reuse is wrong -- STOP, do NOT tune.)"""
    pts = E.octonionic_points()
    # Sample generators including some with large index (well-mixed coverage).
    sample_idx = [0, 7, 50, 123, 200, 323]
    sample = [derivs[i] for i in sample_idx]
    all_ok = True
    for P in pts:
        vP = Matrix(E._flat27(P))   # X = P
        # Use a SECOND fixed octonionic point as Y (independent of X) so the
        # Leibniz cross terms are non-trivial.
        Q = pts[(pts.index(P) + 1) % len(pts)]
        vQ = Matrix(E._flat27(Q))
        for M in sample:
            # D_M X and D_M Y as coordinate vectors, then rebuild matrices.
            DMX = E.X_from_symbols(list(M * vP))
            DMY = E.X_from_symbols(list(M * vQ))
            Xm = E.X_from_symbols(list(vP))
            Ym = E.X_from_symbols(list(vQ))
            # LHS: D_M(jordan(X,Y)) = M . flat(jordan(X,Y))
            lhs = M * Matrix(E._flat27(E.jordan(Xm, Ym)))
            # RHS: jordan(D_M X, Y) + jordan(X, D_M Y)
            rhs_mat = E.octmat_add(E.jordan(DMX, Ym), E.jordan(Xm, DMY))
            rhs = Matrix(E._flat27(rhs_mat))
            diff_vec = simplify(lhs - rhs)
            if not all(diff_vec[i] == 0 for i in range(27)):
                all_ok = False
    return _report(f"derivation (Leibniz) identity exact over Q "
                   f"[{len(sample)} generators x {len(pts)} octonionic points]",
                   all_ok)


def check_bracket_closure(L, derivs):
    """test-bracket-closure: span{[L_a,L_b]} is closed under the Lie bracket -- a
    sample of double brackets [[L_a,L_b],[L_c,L_d]] lies in the span (the span
    rank stays 52 when each is appended). Confirms the spanning set is a Lie
    subalgebra = f_4 (Jacobson)."""
    quads = [
        (0, 1, 2, 3),
        (1, 4, 7, 10),
        (3, 9, 12, 18),
        (5, 11, 19, 26),
        (2, 8, 14, 20),
        (6, 13, 21, 25),
    ]
    all_ok = True
    for (a, b, cc, d) in quads:
        Bab = L[a] * L[b] - L[b] * L[a]
        Bcd = L[cc] * L[d] - L[d] * L[cc]
        DD = Bab * Bcd - Bcd * Bab            # [[L_a,L_b],[L_c,L_d]]
        rk = span_rank_over_QQ(derivs, extra=[DD])
        if rk != 52:
            all_ok = False
    return _report(f"Lie-bracket closure: appending {len(quads)} double brackets "
                   f"leaves span rank at 52 over QQ (subalgebra = f_4)",
                   all_ok)


# ============================================================================
# TASK 2 CHECKS — infinitesimal F_4-invariance: D_M f = 0 over Q for all 324
# ============================================================================

def _gradients_in_X():
    """Gradients of the three single-copy invariants in the 27 X-symbols E.xs.
    det_3's gradient is heavy but only in the 27 X-symbols (Y not involved);
    we substitute the point BEFORE further use to control swell."""
    f_Tr = E.Tr(E.Xsym)
    f_Tr2 = E.Tr2(E.Xsym)
    f_det = E.det_3(E.Xsym)
    grad_Tr = [diff(f_Tr, E.xs[i]) for i in range(27)]
    grad_Tr2 = [diff(f_Tr2, E.xs[i]) for i in range(27)]
    grad_det = [diff(f_det, E.xs[i]) for i in range(27)]
    return {"Tr": grad_Tr, "Tr^2": grad_Tr2, "det_3": grad_det}


def check_invariance(derivs):
    """test-invariance-det3 + test-invariance-tr-tr2: every generator M (all 324
    brackets, hence all of f_4 = span) annihilates each of {Tr, Tr^2, det_3}:
    D_M f := (grad f).(M.v) == 0 EXACTLY over Q, at >=3 genuinely octonionic
    rational points. This re-establishes the engine LOCK 7b on det_3 IN THIS
    MODULE and EXTENDS it to the full certificate (Tr, Tr^2 too).

    PERF: substitute the rational point into the gradient components FIRST so the
    D_M f sum is over rationals; tangents M.v are matrix*vector. Forbidden proxy
    fp-single-point-invariance rejected: >=3 genuinely octonionic points (non-real
    off-diagonals), NOT a single point and NOT the commutative real subalgebra."""
    grads = _gradients_in_X()
    pts = E.octonionic_points()
    n = len(derivs)
    results = {}   # name -> (min_killed_over_points, total)
    for name, grad in grads.items():
        worst_killed = n
        for P in pts:
            v = Matrix(E._flat27(P))
            subs_pt = {E.xs[k]: v[k] for k in range(27)}
            grad_at = [g.subs(subs_pt) for g in grad]
            killed = sum(
                1 for M in derivs
                if simplify(infinitesimal_action(grad_at, M, v)) == 0
            )
            worst_killed = min(worst_killed, killed)
        results[name] = (worst_killed, n)

    # Report det_3 first (re-establishes engine LOCK 7b), then Tr and Tr^2.
    det_killed, det_tot = results["det_3"]
    det_ok = _report(f"D_M det_3 == 0 over Q for ALL generators at >=3 octonionic "
                     f"points ({det_killed}/{det_tot} annihilate the corrected "
                     f"generic norm)  [test-invariance-det3; re-establishes LOCK 7b]",
                     det_killed == det_tot and det_tot == 324)
    tr_killed, tr_tot = results["Tr"]
    tr_ok = _report(f"D_M Tr == 0 over Q for ALL generators at >=3 octonionic "
                    f"points ({tr_killed}/{tr_tot})  [test-invariance-tr-tr2]",
                    tr_killed == tr_tot and tr_tot == 324)
    tr2_killed, tr2_tot = results["Tr^2"]
    tr2_ok = _report(f"D_M Tr^2 == 0 over Q for ALL generators at >=3 octonionic "
                     f"points ({tr2_killed}/{tr2_tot})  [test-invariance-tr-tr2]",
                     tr2_killed == tr2_tot and tr2_tot == 324)
    return det_ok and tr_ok and tr2_ok, results


# ============================================================================
# EXACT-ONLY source guard  (forbidden proxy fp-float-rank + fp-norm-bug)
# ============================================================================
# RANK-ROUTING CONVENTION (carried forward to Plans 02/03): ALL ranks MUST go
# through sympy.Matrix(...).rank() over QQ. numpy.linalg.matrix_rank /
# np.linalg.matrix_rank are FORBIDDEN on any rank-bearing path (rank is
# discontinuous; an SVD tolerance fabricates the dim-52 / annihilation verdict).
# octonion_algebra.py is FORBIDDEN entirely (it carries the buggy det_3 cross
# term (x1 x2) x3 -- forbidden proxy fp-norm-bug). This module touches NEITHER.
RANK_ROUTING_CONVENTION = (
    "All ranks via sympy.Matrix(...).rank() over QQ; "
    "numpy.linalg.matrix_rank / np.linalg.matrix_rank FORBIDDEN on the decisive path; "
    "octonion_algebra.py FORBIDDEN entirely (buggy det_3)."
)


def exact_only_guard():
    """Scan THIS module's source for forbidden decisive-path tokens (mirrors the
    frozen engine's regex approach). Asserts:
      (a) NO `import octonion_algebra` / `from octonion_algebra import ...`
          anywhere (this module reuses the FROZEN engine's corrected det_3 via E.
          -- it must never touch the float64 buggy file);
      (b) NO live np.linalg / numpy.linalg float-rank CALL (the trailing '('
          in the regex distinguishes a live call from this prose mention);
      (c) does NOT trip on provenance PROSE (comments/docstrings naming the
          tokens as text, e.g. the forbidden-proxy citations above).
    Returns (ok, detail)."""
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


def main():
    print("=" * 76)
    print("Phase 65 Plan 01 : f_4 = Der(h_3(O)) builder + infinitesimal F_4-invariance GATE")
    print("=" * 76)

    # ------------------------------------------------------------------------
    # TASK 1: build f_4 = span{[L_a,L_b]}, dim 52 over Q, derivation identity,
    # Lie-bracket closure.
    #
    # BACKTRACKING (disconfirming_observations): span rank != 52 -> builder or
    # layout bug; derivation identity fails -> L-matrix / jordan reuse wrong. In
    # either case STOP and reconcile against the engine; do NOT tune.
    # ------------------------------------------------------------------------
    print("Task 1 — build f_4 (52 generators, dim 52 over Q, bracket-closed):")

    # Round-trip guard (defensive; no change-of-basis).
    check_roundtrip_guard()

    # Cache the 27 L-matrices (independent cache for the double-bracket spot check)
    # and build the 324 inner derivations via the FROZEN builder.
    L = cached_L_matrices()
    _report("cached 27 Jordan left-multiplication matrices L_k (27x27 over Q)",
            len(L) == 27 and all(Lk.shape == (27, 27) for Lk in L))
    derivs = E.inner_derivations()

    # dim f_4 = 52 COMPUTED over Q (test-dim-52).
    _dim_ok, _rk = check_dim_f4(derivs)

    # Every generator is a genuine Jordan derivation (test-derivation-identity).
    check_derivation_identity(derivs)

    # Lie-bracket closure (test-bracket-closure).
    check_bracket_closure(L, derivs)

    # ------------------------------------------------------------------------
    # TASK 2: infinitesimal F_4-invariance certificate -- D_M f = 0 over Q for
    # {Tr, Tr^2, det_3}, ALL 324 generators, >=3 genuinely octonionic points.
    #
    # BACKTRACKING: any generator with D_M det_3 != 0 (corrected norm, octonionic
    # point) -> that generator is NOT in f_4 OR det_3 regressed (engine LOCK 7b
    # should have caught a regression). STOP.
    # ------------------------------------------------------------------------
    print("Task 2 — infinitesimal F_4-invariance certificate (Derksen-Kemper char-0):")
    check_invariance(derivs)

    # exact-only guard self-check (forbidden proxies fp-float-rank, fp-norm-bug).
    print("Exact-only guard (decisive-path source scan):")
    _guard_ok, _guard_detail = exact_only_guard()
    _report(f"exact-only guard: no float-rank / no octonion_algebra on decisive "
            f"path [{_guard_detail}]", _guard_ok)

    print("-" * 76)
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}")
    print("=" * 76)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
