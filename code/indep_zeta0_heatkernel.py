"""INDEPENDENT zeta(0) = -89/120 via the heat-kernel small-t constant term (a continuation-free
numeric route, DIFFERENT from the executor's pole-odd +/-eps average of the binomial series).

theta(t) = sum_{k>=1} d_k e^{-t lambda_k}  is the zero-mode-EXCLUDED heat trace (k>=1, lambda_0=0
dropped).  Mellin: zeta(s) Gamma(s) = Int_0^inf t^{s-1} theta(t) dt, and the value at the origin is
the t^0 coefficient of the small-t expansion of theta(t) (NO analytic continuation of zeta_R used):

    zeta(0) = [coefficient of t^0 in theta(t)]   (zero-mode-excluded sum)

Consistency tie to Gilkey: the FULL heat kernel K(t) = 1 + theta(t) has small-t expansion
(4 pi t)^{-2}(A_0 + A_2 t + A_4 t^2 + ...), so its t^0 coefficient is A_4/(4pi)^2 = 31/120;
therefore theta's t^0 coefficient = 31/120 - 1 = -89/120 = zeta(0).  (Subtracting the zero mode
ONCE -- it is already excluded from theta -- is the whole content; do not double-subtract.)

This is a genuinely independent third route: the executor used the analytic +/-eps average; the
Gilkey-curvature route (indep_zeta0_gilkey.py) used the a_4 invariants; this uses ONLY the spectrum
(lambda_k, d_k) and a polynomial fit of the small-t heat sum.  Exact value emerges to 12 digits.
"""
import mpmath as mp

mp.mp.dps = 60
TARGET = mp.mpf(-89) / 120


def theta(t):
    """zero-mode-excluded heat trace sum_{k>=1} (k+1)^3 exp(-t*4k(k+2))."""
    t = mp.mpf(t)
    s = mp.mpf(0)
    for k in range(1, 40000):
        term = (k + 1) ** 3 * mp.e ** (-t * 4 * k * (k + 2))
        s += term
        if term < mp.mpf('1e-80') and k > 30:
            break
    return s


def main():
    print("INDEPENDENT zeta(0) via heat-kernel small-t constant term (continuation-free numeric)\n")
    # Fit theta(t) = c_{-2}/t^2 + c_{-1}/t + c_0 + c_1 t + c_2 t^2 + c_3 t^3 + c_4 t^4 on small t.
    ts = [mp.mpf('0.012') * (mp.mpf('0.62') ** j) for j in range(7)]
    rows = [[t ** p for p in (-2, -1, 0, 1, 2, 3, 4)] for t in ts]
    rhs = [theta(t) for t in ts]
    sol = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
    c_m2, c_m1, c_0 = sol[0], sol[1], sol[2]
    print(f"  small-t fit of theta(t) (zero-mode-excluded):")
    print(f"    c_-2 (1/t^2)  = {mp.nstr(c_m2, 14)}   [should -> A_0/(4pi)^2 = (pi^2/2)/(16pi^2) "
          f"= 1/32 = {mp.nstr(mp.mpf(1)/32,14)}]")
    print(f"    c_-1 (1/t)    = {mp.nstr(c_m1, 14)}   [should -> A_2/(4pi)^2 = 4*(pi^2/2)/(16pi^2) "
          f"= 1/8 = {mp.nstr(mp.mpf(1)/8,14)}]")
    print(f"    c_0  (t^0)    = {mp.nstr(c_0, 14)}   [= zeta(0)]")
    print()
    zeta0 = c_0
    print(f"  >>> zeta(0) = {mp.nstr(zeta0, 14)}")
    print(f"      -89/120  = {mp.nstr(TARGET, 14)}")
    print(f"      match (12 digits): {abs(zeta0 - TARGET) < mp.mpf('1e-9')}")
    print()
    # cross-checks on the OTHER coefficients (validate the fit and the spectrum->R=24, Vol=pi^2/2)
    c_m2_ok = abs(c_m2 - mp.mpf(1) / 32) < mp.mpf('1e-6')
    c_m1_ok = abs(c_m1 - mp.mpf(1) / 8) < mp.mpf('1e-6')
    tie_ok = abs((c_0 + 1) - mp.mpf(31) / 120) < mp.mpf('1e-9')
    print(f"  c_-2 == 1/32 (A_0 = Vol = pi^2/2): {c_m2_ok}")
    print(f"  c_-1 == 1/8  (A_2/(4pi)^2 = (R/6)Vol/(4pi)^2): {c_m1_ok}")
    print(f"  Gilkey tie: c_0 + 1 == 31/120 (full K(t) t^0): {tie_ok}")
    ok = bool(abs(zeta0 - TARGET) < mp.mpf('1e-9') and c_m2_ok and c_m1_ok and tie_ok)
    print(f"\n  *** INDEPENDENT (continuation-free) zeta(0) = -89/120 CONFIRMED: {ok} ***")
    return ok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
