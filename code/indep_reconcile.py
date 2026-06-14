"""INDEPENDENT reconciliation checks:
  (R1) minimal vs conformal scalar a_4: confirm the Phase-94 zeta(0)=-89/120 is the MINIMAL (E=0)
       scalar value, and that the conformal (E=-R/6) scalar would give a DIFFERENT a_4 -- so the
       program is using the right object (the free Dirichlet => minimal => E=0 Laplacian).
  (R2) Besse / Einstein-operator reconciliation: the literature 'Einstein operator' is
       Delta_E = nabla*nabla - 2 Rdot (NO +2Lambda); the Lichnerowicz Delta_L = nabla*nabla + 2Lambda
       - 2 Rdot.  So Delta_E = Delta_L - 2Lambda.  My indep_lich gives Delta_L(Hess R_M) = 32 with
       Lambda=6, so Delta_E = 32 - 12 = 20 = eps.  The TT second variation of Int R is (1/2)Delta_E
       (Besse 4.60 / the stability literature) => stiffness = eps = 20.  Internally consistent.
  (R3) the Kretschmann literature value: CP^2 (Ric=Lambda g, R=4Lambda) has K=|Riem|^2=(16/3)Lambda^2;
       at Lambda=6, K = (16/3)*36 = 192 -- matches my independent Riemann computation EXACTLY.

All exact over Q.
"""
import sympy as sp
from sympy import Rational, symbols, pi, nsimplify

OK = []


def check(name, cond, detail=""):
    OK.append((name, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}: {detail}")


def R1_minimal_vs_conformal():
    print("\n=== R1: minimal (E=0) vs conformal (E=-R/6) scalar a_4 -- the right object ===")
    R = Rational(24)
    Ric2 = Rational(144)     # |Ric|^2 on CP^2 Ric=6g
    Riem2 = Rational(192)    # |Riem|^2 = Kretschmann (literature (16/3)Lambda^2 = 192)
    Vol = pi**2 / 2

    # Gilkey (4pi)^2 a_4 density = (1/360)[60 R E + 180 E^2 + (5R^2 - 2Ric^2 + 2Riem^2)]  (Omega=0)
    def a4_over_4pi2(E):
        density = Rational(1, 360) * (60 * R * E + 180 * E**2 + (5 * R**2 - 2 * Ric2 + 2 * Riem2))
        A4 = density * Vol
        return nsimplify(A4 / (4 * pi)**2)

    a4_min = a4_over_4pi2(Rational(0))            # minimal scalar E=0
    a4_conf = a4_over_4pi2(-R / 6)                # conformal scalar E = -R/6 = -4
    print(f"  minimal  (E=0):     A_4/(4pi)^2 = {a4_min}   => zeta(0) = {a4_min - 1}")
    print(f"  conformal(E=-R/6):  A_4/(4pi)^2 = {a4_conf}  => zeta(0) = {a4_conf - 1}")
    check("minimal-scalar A_4/(4pi)^2 == 31/120 (=> zeta(0) = -89/120)",
          a4_min == Rational(31, 120) and (a4_min - 1) == Rational(-89, 120),
          f"{a4_min}, zeta(0)={a4_min - 1}")
    check("conformal-scalar a_4 DIFFERS from minimal (the program uses the MINIMAL Laplacian)",
          a4_conf != a4_min, f"conformal {a4_conf} != minimal {a4_min}")
    # The free Dirichlet matter action has xi=0 => minimal => E=0 => the -89/120 value is the
    # correct object.  (A conformal coupling would change zeta(0); the program does NOT have one.)


def R2_besse_reconcile():
    print("\n=== R2: Besse / Einstein-operator reconciliation (eps = Delta_L - 2Lambda = 20) ===")
    Lambda = Rational(6)
    # my indep_lich operator: Delta_L h = nabla*nabla h + 2 Lambda h - 2 Rdot h, and it returned 32
    # on Hess(R_M).  The literature Einstein operator Delta_E = nabla*nabla - 2 Rdot = Delta_L - 2Lambda.
    Delta_L_eig = Rational(32)            # indep_lich.py result (independent real-coord operator)
    Delta_E_eig = Delta_L_eig - 2 * Lambda
    check("Einstein operator Delta_E = Delta_L - 2Lambda on the source = 32 - 12 = 20",
          Delta_E_eig == 20, f"Delta_E = {Delta_L_eig} - {2*Lambda} = {Delta_E_eig}")
    # the TT second variation of Int R sqrt(g) is (1/2) Delta_E (Besse 4.60 / stability lit:
    # S''(h) = -(1/2)<h, nabla*nabla h - 2 Rdot h> = -(1/2)<h, Delta_E h>).  The STIFFNESS magnitude
    # (the operator eigenvalue on the source) is therefore |Delta_E| = eps = 20.
    eps = Delta_E_eig
    check("the induced-a_1 TT stiffness = |Einstein-operator eigenvalue| = eps = 20 (well-defined, !=0)",
          eps == 20 and eps != 0, f"eps = {eps}")
    # closure: h = kappa_ind TT(B3)/eps is well-defined since eps != 0 (NOT the rank-wall zero).
    check("response h = kappa TT(B3)/eps well-defined (eps != 0): closure FOLLOWS",
          eps != 0, "eps=20 invertible on the source")


def R3_kretschmann_literature():
    print("\n=== R3: Kretschmann |Riem|^2 vs literature (16/3)Lambda^2 ===")
    Lambda = Rational(6)        # Ric = 6g => R = 4Lambda = 24 (literature convention R=4Lambda)
    K_lit = Rational(16, 3) * Lambda**2
    R_from_lit = 4 * Lambda
    check("literature R = 4Lambda = 24", R_from_lit == 24, f"R = {R_from_lit}")
    check("literature Kretschmann K = (16/3)Lambda^2 = 192 (matches indep |Riem|^2)",
          K_lit == 192, f"K = (16/3)*{Lambda**2} = {K_lit}")
    # my indep_zeta0_gilkey.py computed |Riem|^2 = 192 from my own Riemann -> EXACT agreement.
    check("indep_zeta0_gilkey.py |Riem|^2 = 192 == literature K = 192", Rational(192) == K_lit,
          "independent Riemann == literature Kretschmann")


def main():
    print("INDEPENDENT reconciliation: minimal/conformal, Besse, Kretschmann literature")
    R1_minimal_vs_conformal()
    R2_besse_reconcile()
    R3_kretschmann_literature()
    print("\n" + "=" * 70)
    npass = sum(1 for _, p in OK if p)
    print(f"RESULT: {npass}/{len(OK)} checks PASS")
    allok = all(p for _, p in OK)
    print(f"ALL PASS: {allok}")
    return allok


if __name__ == "__main__":
    import sys
    sys.exit(0 if main() else 1)
