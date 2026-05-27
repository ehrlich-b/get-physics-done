"""
(REDUCIBILITY) cross-term decomposition — canned EXACT-Q correctness check  (REDU-01 / Phase 69-01)
====================================================================================================
Milestone: v16.0 The (RING) Lemma — the (REDUCIBILITY) statement-only dynamical bridge.
Deliverable: deliv-check (the one algebraic identity the statement of
derivations/69-reducibility-statement.md owes).

WHAT THIS CHECKS (and what it does NOT)
---------------------------------------
This is a POLYNOMIAL-IDENTITY BOOKKEEPING CHECK that the cross-term decomposition
stated in Object 3 of derivations/69-reducibility-statement.md is algebraically
correct in the FROZEN Phase-64 conventions, EXACT over Q. It is the
"correctness check on the statement" the backtracking rule calls for.

It is **NOT** a proof of irreducibility. It asserts NO verdict about the driven
stream. It uses NO chaos / Lyapunov / NKS argument. The decomposition's only
non-trivial content is power-associativity (Tr(X o X^2) = Tr(X^3)); everything
else is bilinearity + symmetry of Tr(A o B). There is NO rank computation here:
it is a pure polynomial identity, so `Matrix.rank()` is not used and NO float
appears on any path.

The five assertions (all must hold; residuals identically 0):
  (1) Tr(X o X^2) - Tr(X^3) = 0                                  [power-associativity bookkeeping]
  (2) Tr(X o Y) - [(1-eps) Tr(X^3) + eps Tr(X o S)] = 0          [THE decomposition, symbolic in eps,
                                                                   for the PRE-projection Y = (1-eps)X^2 + eps S]
  (3) c(X,X) - Tr(X o X) = 0                                     [convention-lock sanity: c(X,X)=Tr(X^2)]
  (4) Tr(X o S) - Tr(S o X) = 0                                  [symmetry of the overlap term]
  (5) Tr(X o (X o X)) - Tr((X o X) o X) = 0                      [power-associativity, BOTH associations]

ENGINE
------
Imports the warm, FROZEN EXACT-SymPy-over-Q engine code/ring_lemma_verification.py
(jordan = (1/2)(AB+BA), Tr, det, c = Tr(X o Y), generic_rational_X, h3o_from_coords,
oct, octmat_add, octmat_scal). Arithmetic is exact over Q (rational entries + a
symbolic eps); `simplify` reduces each residual to 0.

BACKTRACKING RULE: if ANY residual is nonzero, the STATEMENT's decomposition
(Object 3) is WRONG -> fix the statement (this is a correctness check, not a proof
attempt) and re-run until clean. Do NOT record a passing certificate over a
failing check.

Reproducibility: SymPy 1.14.0, Python 3.14.2, macOS Darwin 24.6.0. Deterministic
(no random seeds; X and S are hardcoded exact-rational h_3(O) elements). The 2nd
point S is the generic octonionic stand-in used as the exogenous-input element in
the polynomial identity (the identity is symbolic in eps and holds for any S; this
is a structural identity check, not a sampling argument).

Run:  /Users/ehrlich/.gpd/venv/bin/python code/reducibility_decomposition_check.py
Exits 0 iff all 5 assertions pass; nonzero on any failure.
"""

import sys
sys.path.insert(0, 'code')

from ring_lemma_verification import (jordan, Tr, c, generic_rational_X,
    h3o_from_coords, oct, octmat_add, octmat_scal)
from sympy import Rational, symbols, simplify

eps = symbols('eps')
X = generic_rational_X()
# A second generic rational octonionic point: the exogenous S_k stand-in for the
# polynomial-identity check (the decomposition is symbolic in eps and structural in S).
S = h3o_from_coords(Rational(1), Rational(-2), Rational(4),
        oct([0, 1, -1, 2, 0, 1, 0, -1]),
        oct([0, 2, 0, -1, 1, 0, 1, 1]),
        oct([0, -1, 1, 0, 2, -1, 1, 0]))

X2 = jordan(X, X)            # X o X
X3 = jordan(X, X2)           # X o (X o X)
Y = octmat_add(octmat_scal((1 - eps), X2), octmat_scal(eps, S))   # pre-projection Y_k = (1-eps)X^2 + eps S

a1 = simplify(Tr(jordan(X, X2)) - Tr(X3))                                  # Tr(X o X^2) == Tr(X^3)
a2 = simplify(Tr(jordan(X, Y)) - ((1 - eps) * Tr(X3) + eps * Tr(jordan(X, S))))  # the decomposition (symbolic in eps)
a3 = simplify(c(X, X) - Tr(jordan(X, X)))                                  # c(X,X) == Tr(X^2)  (convention lock)
a4 = simplify(Tr(jordan(X, S)) - Tr(jordan(S, X)))                         # Tr(X o S) == Tr(S o X)
a5 = simplify(Tr(X3) - Tr(jordan(X2, X)))                                  # X o (X o X) == (X o X) o X (power-assoc.)

print('(1) Tr(XoX^2)-Tr(X^3)        =', a1, '| Tr(XoX^2) =', simplify(Tr(jordan(X, X2))))
print('(2) decomposition residual   =', a2)
print('(3) c(X,X)-Tr(XoX)           =', a3)
print('(4) Tr(XoS)-Tr(SoX)          =', a4)
print('(5) assoc Tr(Xo(XoX)-(XoX)oX) =', a5)
assert all(v == 0 for v in (a1, a2, a3, a4, a5)), 'DECOMPOSITION CHECK FAILED'
print('ALL 5 ASSERTIONS PASS (exact over Q).')
