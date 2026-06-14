"""INDEPENDENT verification of zeta(0) = -89/120 for the CP^2 scalar Laplacian, via the
Gilkey a_4 heat-kernel coefficient computed from the CURVATURE INVARIANTS (a DIFFERENT method
than the executor's binomial/Hurwitz analytic continuation of the spectral zeta).

The chain (all standard, all cross-checked against the literature in 94-VERIFICATION.md):
  - For a minimal scalar (E=0, Omega=0) in d=4, the integrated Gilkey a_4 coefficient is
        A_4 = (1/360) Int (5 R^2 - 2 Ric^2 + 2 Riem^2) sqrt(g)        [Gilkey; box-R total deriv=0]
    (sign convention 5R^2 - 2|Ric|^2 + 2|Riem|^2; Vassilevich hep-th/0306138 eq 4.34).
  - The spectral zeta(s) = sum_{lambda>0} d_lambda lambda^{-s} of the (zero-mode-excluded) Laplacian
    relates to the heat kernel by Mellin transform; the value at the origin is
        zeta(0) = A_4 / (4pi)^2 - dim ker(Delta)                       [d=4; the t^2 coefficient]
    with dim ker = 1 (the constant zero mode).  So A_4/(4pi)^2 = zeta(0) + 1.
  - The RESEARCH claims A_4/(4pi)^2 = 31/120, hence zeta(0) = 31/120 - 1 = -89/120.

THIS SCRIPT: compute (5R^2 - 2Ric^2 + 2Riem^2) and Vol INDEPENDENTLY from my own from-scratch
real-coordinate Riemann tensor (the v33 indep_curv/indep_lich pipeline, ZERO shared code with the
executor's spectral-zeta path), form A_4/(4pi)^2, and check it equals 31/120 (=> zeta(0) = -89/120).

Reuses /tmp/indep_gam.pkl (my own real Christoffels from indep_curv.py).  Exact over Q.
"""
import sympy as sp, pickle
from sympy import cancel, zeros, symbols, Rational, diff, Matrix, pi, nsimplify, sqrt, Integer

x1, y1, x2, y2 = symbols('x1 y1 x2 y2', real=True)
RC = [x1, y1, x2, y2]
n = 4

D = pickle.load(open('/tmp/indep_gam.pkl', 'rb'))
G = D['G']; Ginv = D['Ginv']; Gam = D['Gam']   # my own real metric / inverse / Christoffels


def d(f, i):
    return diff(f, RC[i])


# ---- full Riemann (all lower) R_{abcd} at a rational point, from MY Christoffels ----
def riemann_lower_pt(pt):
    """R^a_{bcd} = d_c Gam^a_{db} - d_d Gam^a_{cb} + Gam^a_{cm}Gam^m_{db} - Gam^a_{dm}Gam^m_{cb};
    lower the first index with G."""
    Gam_pt = [[[cancel(Gam[a][b][c].subs(pt)) for c in range(n)] for b in range(n)] for a in range(n)]
    Gp = G.subs(pt).applyfunc(cancel)
    Rup = [[[[Integer(0)] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    t = cancel(d(Gam[a][dd][b], cc).subs(pt)) - cancel(d(Gam[a][cc][b], dd).subs(pt))
                    for m in range(n):
                        t += Gam_pt[a][cc][m] * Gam_pt[m][dd][b] - Gam_pt[a][dd][m] * Gam_pt[m][cc][b]
                    Rup[a][b][cc][dd] = cancel(t)
    Rl = [[[[Integer(0)] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    s = Integer(0)
                    for e in range(n):
                        s += Gp[a, e] * Rup[e][b][cc][dd]
                    Rl[a][b][cc][dd] = cancel(s)
    return Rl, Gp


def invariants_at(pt):
    Rl, Gp = riemann_lower_pt(pt)
    Ginv_pt = Ginv.subs(pt).applyfunc(cancel)

    # Ricci R_{bd} = g^{ac} R_{abcd}
    Ric = zeros(n, n)
    for b in range(n):
        for dd in range(n):
            s = Integer(0)
            for a in range(n):
                for cc in range(n):
                    g_ac = Ginv_pt[a, cc]
                    if g_ac == 0:
                        continue
                    s += g_ac * Rl[a][b][cc][dd]
            Ric[b, dd] = cancel(s)

    # scalar R = g^{bd} R_{bd}
    Rscal = Integer(0)
    for b in range(n):
        for dd in range(n):
            g_bd = Ginv_pt[b, dd]
            if g_bd == 0:
                continue
            Rscal += g_bd * Ric[b, dd]
    Rscal = cancel(Rscal)

    # |Ric|^2 = R_{ab} R^{ab} = g^{ac} g^{bd} R_{ab} R_{cd}
    Ric2 = Integer(0)
    for a in range(n):
        for b in range(n):
            for cc in range(n):
                for dd in range(n):
                    ga = Ginv_pt[a, cc]; gb = Ginv_pt[b, dd]
                    if ga == 0 or gb == 0:
                        continue
                    Ric2 += ga * gb * Ric[a, b] * Ric[cc, dd]
    Ric2 = cancel(Ric2)

    # |Riem|^2 = R_{abcd} R^{abcd}.  Raise all four indices with Ginv.
    # Build R^{abcd} = g^{ap} g^{bq} g^{cr} g^{ds} R_{pqrs}, then contract with R_{abcd}.
    # Do it as: sum over all indices of R_{abcd} * Rup_{abcd} where Rup raised.
    # For tractability raise progressively.
    # Step 1: Ru1[a][q][r][s] = g^{? } ... we just brute force the full contraction with 4 inverses.
    Riem2 = Integer(0)
    # precompute a list of nonzero Ginv entries to prune
    gpairs = [(i, j, Ginv_pt[i, j]) for i in range(n) for j in range(n) if Ginv_pt[i, j] != 0]
    for (a, p, gap) in gpairs:
        for (b, q, gbq) in gpairs:
            for (c, r, gcr) in gpairs:
                for (e, s, ges) in gpairs:
                    rl = Rl[a][b][c][e]
                    if rl == 0:
                        continue
                    Riem2 += gap * gbq * gcr * ges * rl * Rl[p][q][r][s]
    Riem2 = cancel(Riem2)

    return Rscal, Ric2, Riem2, Ric, Gp


# ---- volume: Vol(CP^2) = Int sqrt(det G) over the chart; but easier to use the closed form ----
# The FS metric here is normalized to Ric = 6g (R = 24).  Literature (search-confirmed):
#   CP^n with Fubini-Study has R = 4n(n+1) and Vol = pi^n / n!.  For n=2: R=24, Vol = pi^2/2.
# We CONFIRM R = 24 from our own Riemann (below); the Vol = pi^2/2 is the matched normalization
# (also cross-checked by the executor's small-t heat kernel A_0 -> pi^2/2).  Since the a_4 INTEGRAND
# (5R^2 - 2Ric^2 + 2Riem^2) is CONSTANT on the homogeneous space CP^2, A_4 = (integrand)/360 * Vol.

def main():
    print("INDEPENDENT zeta(0) via Gilkey a_4 from curvature invariants (different method)\n")
    pts = [
        {x1: Rational(1, 3), y1: Rational(1, 5), x2: Rational(-1, 4), y2: Rational(1, 7)},
        {x1: Rational(2, 5), y1: Rational(-1, 3), x2: Rational(1, 6), y2: Rational(1, 4)},
    ]
    results = []
    for ip, pt in enumerate(pts):
        print(f"=== curvature invariants at test point {ip+1} ===")
        Rscal, Ric2, Riem2, Ric, Gp = invariants_at(pt)
        # confirm Einstein Ric = 6g at this point (independent re-confirmation of Lambda=6)
        einstein_ok = all(cancel(Ric[i, j] - 6 * Gp[i, j]) == 0 for i in range(n) for j in range(n))
        print(f"  R (scalar)      = {Rscal}     (expect 24)")
        print(f"  |Ric|^2         = {Ric2}     (expect 6^2 * 4 = 144 for Ric=6g in d=4)")
        print(f"  |Riem|^2        = {Riem2}")
        print(f"  Ric == 6g (Einstein, Lambda=6): {einstein_ok}")
        integrand = cancel(5 * Rscal**2 - 2 * Ric2 + 2 * Riem2)
        print(f"  5R^2 - 2|Ric|^2 + 2|Riem|^2 = {integrand}")
        results.append((Rscal, Ric2, Riem2, integrand, einstein_ok))
        print()

    # the integrand must be CONSTANT (homogeneous space) -> same at both points
    same = all(cancel(results[0][3] - r[3]) == 0 for r in results)
    print(f"integrand constant across test points (homogeneous): {same}")
    Rscal, Ric2, Riem2, integrand, einstein_ok = results[0]

    # sanity: Ric=6g, d=4 => |Ric|^2 = sum g^{ac}g^{bd} (6 g_ab)(6 g_cd) = 36 * g^{ac}g^{bd}g_ab g_cd
    #        = 36 * delta^c_c ... = 36 * g^{ac} g_ac = 36 * tr(I_4) = 36*4 = 144. And R = g^{ab}6g_ab = 6*4 = 24.
    ric2_expected = Rational(144)
    R_expected = Rational(24)
    print(f"  cross-check |Ric|^2 = 144: {Ric2 == ric2_expected};  R = 24: {Rscal == R_expected}")

    Vol = pi**2 / 2          # matched normalization (Ric=6g): literature Vol = pi^n/n! = pi^2/2
    A4 = Rational(1, 360) * integrand * Vol
    A4_over_4pi2 = nsimplify(A4 / (4 * pi)**2)
    print(f"\n  Vol(CP^2, Ric=6g) = pi^2/2  (literature pi^n/n!; xcheck heat-kernel A_0)")
    print(f"  A_4 = (1/360)(5R^2-2Ric^2+2Riem^2) * Vol = (1/360)({integrand})(pi^2/2) = {nsimplify(A4)}")
    print(f"  A_4/(4pi)^2 = {A4_over_4pi2}   (expect 31/120)")
    tie_ok = (A4_over_4pi2 == Rational(31, 120))
    print(f"  A_4/(4pi)^2 == 31/120: {tie_ok}")

    zeta0 = A4_over_4pi2 - 1     # zeta(0) = A_4/(4pi)^2 - dim ker(=1)
    print(f"\n  zeta(0) = A_4/(4pi)^2 - dim ker(=1) = {A4_over_4pi2} - 1 = {zeta0}   (expect -89/120)")
    zeta0_ok = (zeta0 == Rational(-89, 120))
    print(f"\n  *** INDEPENDENT zeta(0) = {zeta0}  [== -89/120: {zeta0_ok}] ***")
    print(f"  *** via Gilkey a_4 / curvature invariants (DIFFERENT method from spectral-zeta) ***")

    allok = bool(same and tie_ok and zeta0_ok and einstein_ok
                 and Ric2 == 144 and Rscal == 24)
    print(f"\n  ALL CHECKS PASS: {allok}")
    return allok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
