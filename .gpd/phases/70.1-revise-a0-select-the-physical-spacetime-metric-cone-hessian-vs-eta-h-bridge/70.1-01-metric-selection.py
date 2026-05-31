#!/usr/bin/env python3
"""Phase 70.1-01 metric-selection inputs -- reproduce-and-headline (EXACT over Q).

PURPOSE (Phase 70.1, A0' revision): reproduce, EXACT over Q, every decisive input the
physical-metric SELECTION (cone-Hessian g_X=Hess(-log det_3) vs construction-(ii) bridge
g=eta+h) rests on. This script does NOT rebuild the engine and does NOT recompute the
Totaro Riemann from scratch beyond what the (already-certified) curvature_tensors_at
prototype does -- it IMPORTS the warm engine code/bulk_geometry_verification.py as a
module and reuses the verified 72-01 prototypes verbatim. It does NOT run the engine
main() (~183s harness); it finishes in seconds.

The HEADLINE (never papered over): the M=0 cone-Hessian vacuum is the non-Einstein
static product R_time x H^3 -- Ricci-endomorphism g^{-1}Ric eigenvalues {0,-1,-1,-1},
R=-3, traceless-Ricci S != 0. A GR Lambda-vacuum must be Einstein (Ric prop g); n=4,R=-3
=> the Einstein value is R/4=-3/4, and NO eigenvalue equals it => NOT a GR Lambda-vacuum.

ASSERT_CONVENTION: natural_units=natural; metric_signature=mostly-minus_slice(-,+,+,+)/
riemannian_bulk_positive_definite; arithmetic=EXACT-SymPy-over-Q (Rational/Matrix/
.eigenvals(); ranks via sympy.Matrix.rank(); NEVER numpy/float on a decisive verdict --
fp-float-decisive); jordan_product=(1/2)(AB+BA); octonion_fano=e1e2=e4; complex_structure
u=e7; cubic_norm det_3 cross-term=2Re((x2 x1)x3) [SSOT=bulk_geometry_verification.py det_3;
buggy (x1 x2)x3 / octonion_algebra.py FORBIDDEN -- fp-wrong-cross-term]; potential
Phi=-log det_3 (Faraut-Koranyi, FIXED); g_X=Hess(Phi); curvature_engine=Totaro 2004 Cor 2.3
closed form (ref-totaro, plan-local; ALREADY in the warm engine -- do NOT recompute);
riemann_ricci_sign=NEGATIVE & constant (cone-Hessian-slice K(p,q)=-1/2; round H^3 K=-1;
factor-of-2 BENIGN; load-bearing fact = negative SIGN, do NOT force -1 -- fp-assume-einstein).

DISCIPLINE: NO factor inserted to force Ric prop g or flatness (fp-assume-einstein); NO
H^3-leaf restriction / timelike-x_0 quotient (fp-relabel); octonion_algebra.py untouched
(fp-wrong-cross-term); every verdict sympy-exact over Q (fp-float-decisive).

NOTE ON STEP 7 (signature-independence) -- DEVIATION from the plan's literal recipe:
The plan's Task-1 step 7 said "multiply g by -1 and show RicEndo=ginv*Ric is UNCHANGED."
That literal recipe is mathematically FALSE: under an overall metric sign flip g->-g the
(0,2) Ricci tensor Ric_jl is UNCHANGED, but the (1,1) endomorphism g^{-1}Ric NEGATES
(eigenvalues {0,-1,-1,-1} -> {0,+1,+1,+1}). The CONTRACT's stated principle is what is
load-bearing: "the eigenvalues of the (1,1) Ricci endomorphism g^{-1}Ric are similarity/
signature invariants." We implement that CORRECTLY: a frame change (congruence) P acts as
g->P^T g P, Ric->P^T Ric P, so the endomorphism transforms by SIMILARITY
P^{-1}(g^{-1}Ric)P -- eigenvalues invariant. We ALSO show the naive g->-g sign flip
explicitly (eigenvalues negate) to expose precisely the contract disconfirming-observation
("a sign-dependent verdict means the (0,2) Ricci components were used without raising the
index"): the reported invariant is the (1,1) endomorphism spectrum (index raised), NOT the
raw (0,2) entries and NOT an overall scalar flip. Same physics claim; faithful, non-false
implementation.

Run: python3 -u .gpd/phases/70.1-.../70.1-01-metric-selection.py
Expect: every assert passes; final line METRIC_SELECTION_INPUTS_OK; exit 0.
Reproducibility: SymPy 1.14.0, Python 3.14.x, NumPy not on the decisive path. No seeds
(deterministic exact arithmetic). Engine HEAD: code/bulk_geometry_verification.py.
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..', 'code'))
from sympy import Rational, cancel, simplify, Matrix, log as _log, symbols

import bulk_geometry_verification as E

t0 = time.time()
n = 4


def tick(msg):
    print(f"[{time.time() - t0:6.1f}s] {msg}", flush=True)


def curvature_tensors_at(delta, slice_pt_vals, simp=cancel):
    """(R_tensor, Ric, Rs, g_at, ginv, detg) of the off-center cone-Hessian slice
    metric at X_bg=I/3+delta evaluated at the rational slice point. EXACT over Q.
    Reused VERBATIM from .gpd/phases/72-b-matter-sourcing/72-01-baseline-probe.py
    (already verified); mirrors the engine _curvature_invariants_at but exposes the
    tensors. The Totaro Riemann is the warm engine's (NOT a re-derivation)."""
    beta, gamma, p, q = symbols('beta gamma p q', real=True)
    coords = [beta, gamma, p, q]
    Phi = (-_log(E.inv_det_X)).subs(E._offcenter_subs(delta, slice_symbolic=True))
    g_sym = E.hessian_metric(Phi, coords)
    C_sym = E.cubic_form_C(Phi, coords)
    pt = {coords[i]: slice_pt_vals[i] for i in range(n)}
    g_at = g_sym.subs(pt).applyfunc(simp)
    C_at = [[[simp(C_sym[i][j][k].subs(pt)) for k in range(n)] for j in range(n)]
            for i in range(n)]
    detg = simp(g_at.det())
    ginv = g_at.inv().applyfunc(simp)
    Rt = E.totaro_riemann(ginv, C_at, n, simp=simp)
    Ric = Matrix(n, n, lambda j, l: simp(sum(
        ginv[i, k] * Rt[i][j][k][l] for i in range(n) for k in range(n))))
    Rs = simp(sum(ginv[j, l] * Ric[j, l] for j in range(n) for l in range(n)))
    return Rt, Ric, Rs, g_at, ginv, detg


def ricci_decomposition(Rt, g, ginv, n=4, simp=cancel):
    """n=4 GR Ricci decomposition: scalar + traceless-Ricci + Weyl, with the
    reconstruction residual. EXACT over Q. Reused VERBATIM from the 72-01 probe."""
    Ric = Matrix(n, n, lambda j, l: simp(sum(
        ginv[i, k] * Rt[i][j][k][l] for i in range(n) for k in range(n))))
    Rs = simp(sum(ginv[j, l] * Ric[j, l] for j in range(n) for l in range(n)))
    S = Matrix(n, n, lambda a, b: simp(Ric[a, b] - Rs / n * g[a, b]))
    trace_S = simp(sum(ginv[a, b] * S[a, b] for a in range(n) for b in range(n)))
    coef = Rs / (n * (n - 1))
    Scal = [[[[simp(coef * (g[i, l] * g[j, k] - g[i, k] * g[j, l]))
               for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    Epart = [[[[simp(Rational(1, n - 2) * (S[i, l] * g[j, k] - S[j, l] * g[i, k]
                                           - S[i, k] * g[j, l] + S[j, k] * g[i, l]))
                for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    Weyl = [[[[simp(Rt[i][j][k][l] - Scal[i][j][k][l] - Epart[i][j][k][l])
               for l in range(n)] for k in range(n)] for j in range(n)] for i in range(n)]
    resid_zero = all(
        simp(Rt[i][j][k][l] - (Scal[i][j][k][l] + Epart[i][j][k][l] + Weyl[i][j][k][l])) == 0
        for i in range(n) for j in range(n) for k in range(n) for l in range(n))
    return {"Ric": Ric, "Rs": Rs, "S": S, "trace_S": trace_S, "resid_zero": resid_zero}


CENTER = [Rational(1, 3), Rational(1, 3), Rational(0), Rational(0)]

print("=" * 78)
print("PHASE 70.1-01 metric-selection inputs -- reproduce-and-headline (EXACT over Q)")
print("=" * 78)
tick("engine imported (warm; main() NOT run, Totaro Riemann NOT recomputed from scratch)")

# Guard: the SSOT engine must be the geometry module, NOT octonion_algebra (fp-wrong-cross-term)
assert 'octonion_algebra' not in sys.modules, "fp-wrong-cross-term: octonion_algebra.py must not be imported"
tick("SSOT GUARD: octonion_algebra.py NOT imported (det_3 SSOT = bulk_geometry_verification.py)")

# === Step 2: M=0 cone-Hessian metric =========================================
Rt_c, Ric_c, Rs_c, g_c, ginv_c, detg_c = curvature_tensors_at({}, CENTER, simp=cancel)
assert g_c == Matrix.diag(9, 9, 18, 18), g_c
assert detg_c == 26244, detg_c
tick(f"METRIC: g(center,M=0) = diag(9,9,18,18), det_g = {detg_c} -- CONFIRMED exact over Q")
print(f"        Ric (0,2) = {Ric_c.tolist()}")

# === Step 3: Ricci endomorphism spectrum + scalar =============================
RicEndo = (ginv_c * Ric_c).applyfunc(cancel)
eig = RicEndo.eigenvals()
assert eig == {Rational(0): 1, Rational(-1): 3}, dict(eig)
assert Rs_c == -3, Rs_c
tick(f"HEADLINE SPECTRUM: g^-1 Ric eigenvalues = {dict(eig)} (mult 0:1, -1:3); R = {Rs_c}")

# RED-FLAG guard: g^{-1}Ric must NOT be proportional to identity (that would be Einstein)
assert not RicEndo.is_diagonal() or len(set(RicEndo.diagonal())) > 1 or eig != {RicEndo[0, 0]: n}, \
    "RED FLAG: g^-1 Ric proportional to identity => would be Einstein; re-check SSOT import"
# explicit: not all eigenvalues equal
assert len(eig) > 1, "RED FLAG: single eigenvalue => Einstein; re-check the slice/import"
tick("RED-FLAG GUARD: g^-1 Ric is NOT proportional to identity (would falsely read Einstein)")

# === Step 4: Ricci decomposition + Einstein-value contradiction ===============
dec_c = ricci_decomposition(Rt_c, g_c, ginv_c, n=4, simp=cancel)
S_is_zero = all(dec_c["S"][i, j] == 0 for i in range(n) for j in range(n))
assert dec_c["resid_zero"] is True, "reconstruction residual must be exactly 0"
assert dec_c["trace_S"] == 0, dec_c["trace_S"]
assert not S_is_zero, "S must be NON-zero (non-Einstein) -- the point of the verdict"
einstein_value = Rs_c / n            # R/4 = -3/4
assert einstein_value == Rational(-3, 4), einstein_value
assert einstein_value not in eig, "Einstein value -3/4 must NOT be among the eigenvalues"
tick(f"EINSTEIN TEST: reconstruction residual = 0; trace(S) = 0; S != 0 (NON-Einstein).")
tick(f"  Einstein value R/4 = {einstein_value}; NOT among eigenvalues {set(eig.keys())}"
     f" => NOT a GR Lambda-vacuum.")
print(f"        traceless Ricci S = {dec_c['S'].tolist()}")

# === Step 5: Sectional curvatures name the R_time x H^3 structure =============
K = {}
for (i, j) in [(0, 1), (2, 3)]:
    vi = [0] * n; vi[i] = 1
    vj = [0] * n; vj[j] = 1
    K[(i, j)], _ = E.sectional_curvature(Rt_c, g_c, vi, vj, n, simp=cancel)
assert K[(0, 1)] == 0, K[(0, 1)]
assert K[(2, 3)] == Rational(-1, 2), K[(2, 3)]
# cross-check the H^3 base value against the engine's certified benchmark
bench = E.h3_cone_hessian_benchmark()
assert bench["K_value"] == Rational(-1, 2), bench["K_value"]
assert all(k == Rational(-1, 2) for k in bench["K_sections"]), bench["K_sections"]
assert bench["sym_ok"] and bench["imag_free"]
tick(f"SECTIONAL STRUCTURE: K(e0,e1) = {K[(0, 1)]} (timelike/dilation plane FLAT), "
     f"K(p,q) = {K[(2, 3)]} (H^3 base; == h3_cone_hessian_benchmark K_value).")
tick(f"  => static product R_time x H^3 (flat factor = time x_0 ~ beta+gamma); "
     f"round-H^3 cross-check K_round = {bench['round_K']} = 2*(-1/2) (factor-of-2 BENIGN).")

# === Step 6: eta+h flatness cross-check (construction-(ii), Lambda=0 inserted) =
MG = E.offcenter_slice_metric({}, slice_vals=CENTER)
assert MG["h"] == Matrix.zeros(4, 4), MG["h"]
# g == eta_bg at center (h=0): the bridge reduces to exact Minkowski by construction
assert MG["g"] == MG["eta_bg"], (MG["g"], MG["eta_bg"])
mink = E.minkowski_reduction()
assert mink["residual"] == Matrix.zeros(4, 4), mink["residual"]
assert mink["h_center"] == Matrix.zeros(4, 4), mink["h_center"]
assert mink["sylvester_minors"] == [1, -1, 1, -1], mink["sylvester_minors"]
assert mink["g_center"] == mink["eta"], (mink["g_center"], mink["eta"])
tick(f"ETA+H CROSS-CHECK: h == 0 (4x4) at (M=0,center) => g = eta_bg, FLAT (R=0, Lambda=0).")
tick(f"  minkowski_reduction(): residual = 0, Sylvester minors {mink['sylvester_minors']} "
     f"=> signature {mink['signature']}. Lambda=0 is INSERTED by the centered subtraction "
     f"h:=Hess-Hess|center (TAUTOLOGICAL, not derived).")

# === Step 7: signature-independence (CORRECT congruence/similarity statement) ==
# The CONTRACT principle: eigenvalues of the (1,1) endomorphism g^{-1}Ric are
# similarity/signature invariants. Demonstrate via a frame change (congruence) P:
#   g -> P^T g P,  Ric -> P^T Ric P  =>  g^{-1}Ric -> P^{-1}(g^{-1}Ric)P  (similarity).
P = Matrix([[2, 1, 0, 0], [0, 1, 0, 0], [1, 0, 3, 0], [0, 0, 1, 2]])  # generic invertible rational
assert P.det() != 0
gP = (P.T * g_c * P).applyfunc(cancel)
RicP = (P.T * Ric_c * P).applyfunc(cancel)
RicEndoP = (gP.inv() * RicP).applyfunc(cancel)
assert RicEndoP.eigenvals() == eig, dict(RicEndoP.eigenvals())
tick(f"SIGNATURE-INDEPENDENCE (congruence P, det {cancel(P.det())}): g^-1 Ric eigenvalues "
     f"= {dict(RicEndoP.eigenvals())} -- INVARIANT (similarity on the (1,1) endomorphism).")

# Expose the contract disconfirming-observation explicitly: a naive OVERALL metric
# sign flip g->-g leaves the (0,2) Ric UNCHANGED but NEGATES the (1,1) endomorphism.
# This is WHY the reported invariant must be the (1,1) endo spectrum (index raised),
# not the raw (0,2) entries / an overall scalar flip. (The plan's literal step-7
# recipe asserted 'unchanged under g->-g' -- that is false; see module docstring.)
beta, gamma, p, q = symbols('beta gamma p q', real=True)
coords = [beta, gamma, p, q]
Phi = (-_log(E.inv_det_X)).subs(E._offcenter_subs({}, slice_symbolic=True))
C_sym = E.cubic_form_C(Phi, coords)
pt = {coords[i]: CENTER[i] for i in range(n)}
C_at = [[[cancel(C_sym[i][j][k].subs(pt)) for k in range(n)] for j in range(n)]
        for i in range(n)]
g_neg = (-g_c)
ginv_neg = g_neg.inv().applyfunc(cancel)
Rt_neg = E.totaro_riemann(ginv_neg, C_at, n, simp=cancel)
Ric_neg = Matrix(n, n, lambda j, l: cancel(sum(
    ginv_neg[i, k] * Rt_neg[i][j][k][l] for i in range(n) for k in range(n))))
RicEndo_neg = (ginv_neg * Ric_neg).applyfunc(cancel)
assert Ric_neg == Ric_c, "(0,2) Ric should be unchanged under g->-g"
assert RicEndo_neg.eigenvals() == {Rational(0): 1, Rational(1): 3}, dict(RicEndo_neg.eigenvals())
tick(f"  CONTRAST (raise-index point): under g->-g, (0,2) Ric UNCHANGED but g^-1 Ric "
     f"eigenvalues = {dict(RicEndo_neg.eigenvals())} (negated). The reported invariant is "
     f"the (1,1) endomorphism spectrum -- NOT the (0,2) entries. No verdict uses (0,2) Ric raw.")

# === Step 8: cross-term SSOT confirmation (corrected association; fp-wrong-cross-term excluded)
Xs = E.X_from_symbols(E.xs)
a, b, gsym, x1, x2, x3 = E._coord_from_octmat(Xs)
n1, n2, n3 = E._oct_normsq(x1), E._oct_normsq(x2), E._oct_normsq(x3)
cross = E.oct_mul(E.oct_mul(x2, x1), x3)            # 2Re((x2 x1) x3) = 2*cross[0]
det_block_expr = a * b * gsym - a * n1 - b * n2 - gsym * n3
assert simplify(E.det_3(Xs) - det_block_expr - 2 * cross[0]) == 0
assert not (cross[0].free_symbols & {E.xs[0], E.xs[1], E.xs[2]})   # alpha,beta,gamma absent
tick("CROSS-TERM SSOT: det_3 - diag-norm == 2Re((x2 x1)x3); alpha,beta,gamma absent from "
     "the triple (corrected association; buggy (x1 x2)x3 / octonion_algebra.py EXCLUDED).")

print("-" * 78)
print("METRIC_SELECTION_INPUTS_OK -- headline {0,-1,-1,-1} (R=-3, NON-Einstein, "
      "R_time x H^3, flat dir = timelike x_0, K(p,q)=-1/2), eta+h h==0-at-center (flat, "
      "Lambda=0 inserted), signature-independence (similarity-invariant (1,1) spectrum), "
      "and the corrected cross-term -- ALL reproduced EXACT over Q from the warm engine.")
