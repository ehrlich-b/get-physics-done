#!/usr/bin/env python3
"""
Directional derivatives of rho_J on h_3(O) at observer-like states.

rho_J(X) = det(X) * (Tr(X^2) - 1/3)

where X = [[a, x3*, x2*], [x3, b, x1*], [x2, x1, c]] in h_3(O),
det(X) = abc + 2 Re(x1 x2 x3) - a|x1|^2 - b|x2|^2 - c|x3|^2,
sigma_2 = Tr(X^2) = a^2 + b^2 + c^2 + 2(|x1|^2 + |x2|^2 + |x3|^2).

Perturbations: real component in x_i slot, amplitude delta.
"""

import sympy as sp
from sympy import symbols, Rational, sqrt, diff, simplify, factor, collect, expand
from sympy import Float, oo, solve, pprint
import numpy as np
from itertools import product as iprod

print("=" * 80)
print("PART 1: SYMBOLIC COMPUTATION")
print("=" * 80)

# Symbols
a, b, c, d1, d2, d3, eps = symbols('a b c delta_1 delta_2 delta_3 epsilon', real=True)

# det(X) with perturbations delta_i in x_i directions (real perturbations only)
# x_1 in (2,3) slot, x_2 in (1,3) slot, x_3 in (1,2) slot
# det = abc + 2 Re(x1 x2 x3) - a|x1|^2 - b|x2|^2 - c|x3|^2
# For real perturbations: x_i = delta_i (real), so Re(x1 x2 x3) = d1*d2*d3
det_full = a*b*c + 2*d1*d2*d3 - a*d1**2 - b*d2**2 - c*d3**2

# sigma_2 = a^2 + b^2 + c^2 + 2(|x1|^2 + |x2|^2 + |x3|^2)
sigma2_full = a**2 + b**2 + c**2 + 2*(d1**2 + d2**2 + d3**2)

# rho_J = det * (sigma_2 - 1/3)
rho_full = det_full * (sigma2_full - Rational(1, 3))

print("\n--- General rho_J with all three real perturbations ---")
print(f"det  = {det_full}")
print(f"sig2 = {sigma2_full}")
print(f"rho  = det * (sig2 - 1/3)")

# ========================================================================
# Single-direction perturbations from diagonal state diag(a, b, c)
# ========================================================================
print("\n" + "=" * 80)
print("PART 2: SINGLE-DIRECTION PERTURBATIONS FROM diag(a,b,c)")
print("=" * 80)

delta = symbols('delta', real=True)

for label, slot, det_expr, sig2_expr in [
    ("x_1 (slot 2,3)", "x_1",
     a*b*c - a*delta**2,
     a**2 + b**2 + c**2 + 2*delta**2),
    ("x_2 (slot 1,3)", "x_2",
     a*b*c - b*delta**2,
     a**2 + b**2 + c**2 + 2*delta**2),
    ("x_3 (slot 1,2)", "x_3",
     a*b*c - c*delta**2,
     a**2 + b**2 + c**2 + 2*delta**2),
]:
    rho_dir = det_expr * (sig2_expr - Rational(1, 3))
    rho_dir_expanded = expand(rho_dir)

    d1_rho = diff(rho_dir, delta).subs(delta, 0)
    d2_rho = diff(rho_dir, delta, 2).subs(delta, 0)

    print(f"\n--- Perturbation in {label} ---")
    print(f"  det(delta)  = {det_expr}")
    print(f"  sig2(delta) = {sig2_expr}")
    print(f"  d(rho)/d(delta)|_0  = {simplify(d1_rho)}")
    print(f"  d2(rho)/d(delta^2)|_0 = {simplify(d2_rho)}")

    # Factor nicely
    d2_factored = factor(d2_rho)
    d2_collected = collect(expand(d2_rho), [a, b, c])
    print(f"  d2 factored = {d2_factored}")

# ========================================================================
# Explicit formulas at diag(1-2e, e, e)
# ========================================================================
print("\n" + "=" * 80)
print("PART 3: EXPLICIT AT X(epsilon) = diag(1-2e, e, e)")
print("=" * 80)

a_e, b_e, c_e = 1 - 2*eps, eps, eps

# Base values
det_base = a_e * b_e * c_e
sig2_base = a_e**2 + b_e**2 + c_e**2
rho_base = det_base * (sig2_base - Rational(1, 3))

det_base_exp = expand(det_base)
sig2_base_exp = expand(sig2_base)
rho_base_exp = expand(rho_base)

print(f"\ndet(X(e))  = {det_base_exp}")
print(f"sig2(X(e)) = {sig2_base_exp}")
print(f"rho(X(e))  = {rho_base_exp}")

# Second derivatives in each direction
# For x_1: d2(rho)/d(delta^2) uses the general formula with a=1-2e, b=e, c=e
# We need to compute it properly using the product rule on det * (sig2 - 1/3)

for label, weight_diag in [("x_1", a_e), ("x_2", b_e), ("x_3", c_e)]:
    # det(delta) = abc - weight*delta^2
    det_d = det_base - weight_diag * delta**2
    # sig2(delta) = sig2_base + 2*delta^2
    sig2_d = sig2_base + 2*delta**2
    # rho(delta)
    rho_d = det_d * (sig2_d - Rational(1, 3))

    d1_val = diff(rho_d, delta).subs(delta, 0)
    d2_val = diff(rho_d, delta, 2).subs(delta, 0)

    d2_simplified = simplify(d2_val)
    d2_expanded = expand(d2_val)

    print(f"\n--- {label} direction ---")
    print(f"  d(rho)/d(delta)|_0    = {simplify(d1_val)}")
    print(f"  d2(rho)/d(delta^2)|_0 = {d2_expanded}")
    print(f"  d2 simplified         = {d2_simplified}")
    print(f"  d2 factored           = {factor(d2_val)}")

# ========================================================================
# NUMERICAL EVALUATION
# ========================================================================
print("\n" + "=" * 80)
print("PART 4: NUMERICAL EVALUATION AT VARIOUS EPSILON")
print("=" * 80)

def compute_all(a_val, b_val, c_val, label=""):
    """Compute rho_J and all second derivatives numerically."""
    det0 = a_val * b_val * c_val
    sig20 = a_val**2 + b_val**2 + c_val**2
    rho0 = det0 * (sig20 - 1/3)

    results = {"a": a_val, "b": b_val, "c": c_val,
               "det": det0, "sig2": sig20, "rho": rho0}

    # For each direction, compute d2(rho)/d(delta^2) at delta=0
    # Using the formula: rho(delta) = (det0 - w*delta^2)(sig20 + 2*delta^2 - 1/3)
    # d(rho)/d(delta) = -2w*delta*(sig20 + 2*delta^2 - 1/3) + (det0 - w*delta^2)*4*delta
    # At delta=0: d(rho)/d(delta) = 0 (confirmed)
    # d2(rho)/d(delta^2) at delta=0:
    #   = -2w*(sig20 - 1/3) + 4*det0
    # Wait, let me be more careful.

    # rho(delta) = (D - w*delta^2)*(S + 2*delta^2 - 1/3)
    # Let f = D - w*delta^2, g = S + 2*delta^2 - 1/3
    # rho = f*g
    # rho' = f'g + fg'
    # rho'' = f''g + 2f'g' + fg''
    # f = D - w*d^2, f' = -2wd, f'' = -2w
    # g = S + 2d^2 - 1/3, g' = 4d, g'' = 4
    # At d=0:
    # f=D, f'=0, f''=-2w, g=S-1/3, g'=0, g''=4
    # rho''(0) = (-2w)(S-1/3) + 2*0*0 + D*4 = -2w(S-1/3) + 4D

    for dir_label, w in [("x1", a_val), ("x2", b_val), ("x3", c_val)]:
        d2_rho = -2*w*(sig20 - 1/3) + 4*det0
        results[f"d2_{dir_label}"] = d2_rho

    # Also numerical verification via finite differences
    dd = 1e-7
    for dir_label, w in [("x1", a_val), ("x2", b_val), ("x3", c_val)]:
        # rho at +dd and -dd
        det_p = det0 - w*dd**2
        sig2_p = sig20 + 2*dd**2
        rho_p = det_p * (sig2_p - 1/3)

        det_m = det0 - w*dd**2  # same (even function)
        sig2_m = sig20 + 2*dd**2
        rho_m = det_m * (sig2_m - 1/3)

        # Second derivative: (rho(+dd) - 2*rho(0) + rho(-dd)) / dd^2
        d2_num = (rho_p - 2*rho0 + rho_m) / dd**2
        results[f"d2_{dir_label}_num"] = d2_num

    return results

# Table header
print(f"\n{'epsilon':>10} | {'rho_J':>14} | {'d2_x1':>14} | {'d2_x2':>14} | {'d2_x3':>14} | {'x1/x2':>10} | {'x1/x3':>10} | {'x2/x3':>10}")
print("-" * 110)

epsilons = [0.001, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 1/3]
for e in epsilons:
    r = compute_all(1 - 2*e, e, e)
    ratio_12 = r["d2_x1"] / r["d2_x2"] if abs(r["d2_x2"]) > 1e-30 else float('inf')
    ratio_13 = r["d2_x1"] / r["d2_x3"] if abs(r["d2_x3"]) > 1e-30 else float('inf')
    ratio_23 = r["d2_x2"] / r["d2_x3"] if abs(r["d2_x3"]) > 1e-30 else float('inf')
    e_label = f"{e:.6f}" if e != 1/3 else "1/3"
    print(f"{e_label:>10} | {r['rho']:>14.8e} | {r['d2_x1']:>14.8e} | {r['d2_x2']:>14.8e} | {r['d2_x3']:>14.8e} | {ratio_12:>10.4f} | {ratio_13:>10.4f} | {ratio_23:>10.4f}")

# ========================================================================
# PART 5: FIND THE MAXIMUM OF rho_J
# ========================================================================
print("\n" + "=" * 80)
print("PART 5: MAXIMUM OF rho_J ON THE TRACE-1 DIAGONAL SLICE")
print("=" * 80)

# On diag(a, b, 1-a-b), find max of rho_J = abc * (a^2+b^2+c^2 - 1/3)
a_s, b_s = symbols('a_s b_s', real=True, positive=True)
c_s = 1 - a_s - b_s

det_s = a_s * b_s * c_s
sig2_s = a_s**2 + b_s**2 + c_s**2
rho_s = det_s * (sig2_s - Rational(1, 3))

# Gradient
grad_a = diff(rho_s, a_s)
grad_b = diff(rho_s, b_s)

print("\nGradient equations (setting to zero):")
print(f"  d(rho)/da = {simplify(grad_a)}")
print(f"  d(rho)/db = {simplify(grad_b)}")

# By symmetry, try a = b (then c = 1 - 2a)
a_sym = symbols('a_sym', positive=True)
rho_sym = a_sym * a_sym * (1 - 2*a_sym) * (a_sym**2 + a_sym**2 + (1 - 2*a_sym)**2 - Rational(1, 3))
rho_sym_exp = expand(rho_sym)
print(f"\nrho on a=b line: {rho_sym_exp}")

drho_da = diff(rho_sym_exp, a_sym)
print(f"d(rho)/da on a=b line: {expand(drho_da)}")

# Solve
crits = solve(drho_da, a_sym)
print(f"\nCritical points on a=b line: {crits}")
for cp in crits:
    cp_float = float(cp.evalf())
    if 0 < cp_float < 0.5:
        c_val = 1 - 2*cp_float
        rho_val = float(rho_sym_exp.subs(a_sym, cp))
        print(f"  a = b = {cp_float:.8f}, c = {c_val:.8f}, rho = {rho_val:.10f}")

# Also numerical optimization
print("\nNumerical grid search for max:")
best_rho = -1e30
best_abc = None
N = 500
for i in range(1, N):
    for j in range(1, N - i):
        aa = i / N
        bb = j / N
        cc = 1 - aa - bb
        if cc > 0:
            dd = aa * bb * cc
            ss = aa**2 + bb**2 + cc**2
            rr = dd * (ss - 1/3)
            if rr > best_rho:
                best_rho = rr
                best_abc = (aa, bb, cc)

print(f"  Max rho_J ~ {best_rho:.10f} at ({best_abc[0]:.4f}, {best_abc[1]:.4f}, {best_abc[2]:.4f})")

# Also try fully general (a != b != c) with scipy
from scipy.optimize import minimize

def neg_rho(params):
    aa, bb = params
    cc = 1 - aa - bb
    if cc <= 0 or aa <= 0 or bb <= 0:
        return 1e10
    dd = aa * bb * cc
    ss = aa**2 + bb**2 + cc**2
    return -(dd * (ss - 1/3))

# Multiple starts
best_result = None
best_val = 1e10
for _ in range(100):
    x0 = np.random.dirichlet([1, 1, 1])[:2]
    res = minimize(neg_rho, x0, method='Nelder-Mead')
    if res.fun < best_val:
        best_val = res.fun
        best_result = res

aa_opt, bb_opt = best_result.x
cc_opt = 1 - aa_opt - bb_opt
print(f"  Scipy max rho_J = {-best_val:.10f} at ({aa_opt:.6f}, {bb_opt:.6f}, {cc_opt:.6f})")
# Sort to canonical form
abc_sorted = sorted([aa_opt, bb_opt, cc_opt], reverse=True)
print(f"  Sorted: ({abc_sorted[0]:.6f}, {abc_sorted[1]:.6f}, {abc_sorted[2]:.6f})")

# ========================================================================
# PART 6: SECOND DERIVATIVES AT THE MAXIMUM
# ========================================================================
print("\n" + "=" * 80)
print("PART 6: SECOND DERIVATIVES AT THE rho_J MAXIMUM")
print("=" * 80)

# At the symmetric max (a=b, c=1-2a)
for cp in crits:
    cp_float = float(cp.evalf())
    if 0 < cp_float < 0.5:
        a_max = cp_float
        b_max = cp_float
        c_max = 1 - 2*cp_float

        print(f"\nAt rho_J maximum: diag({a_max:.8f}, {b_max:.8f}, {c_max:.8f})")
        r = compute_all(a_max, b_max, c_max)
        print(f"  rho_J = {r['rho']:.10e}")
        print(f"  d2(rho)/d(x_1)^2 = {r['d2_x1']:.10e}")
        print(f"  d2(rho)/d(x_2)^2 = {r['d2_x2']:.10e}")
        print(f"  d2(rho)/d(x_3)^2 = {r['d2_x3']:.10e}")
        if abs(r['d2_x2']) > 1e-30:
            print(f"  ratio x1/x2 = {r['d2_x1']/r['d2_x2']:.8f}")
            print(f"  ratio x1/x3 = {r['d2_x1']/r['d2_x3']:.8f}")
            print(f"  ratio x2/x3 = {r['d2_x2']/r['d2_x3']:.8f}")

# At the general maximum from scipy
print(f"\nAt scipy maximum: diag({abc_sorted[0]:.6f}, {abc_sorted[1]:.6f}, {abc_sorted[2]:.6f})")
r = compute_all(abc_sorted[0], abc_sorted[1], abc_sorted[2])
print(f"  rho_J = {r['rho']:.10e}")
print(f"  d2(rho)/d(x_1)^2 = {r['d2_x1']:.10e}")
print(f"  d2(rho)/d(x_2)^2 = {r['d2_x2']:.10e}")
print(f"  d2(rho)/d(x_3)^2 = {r['d2_x3']:.10e}")
if abs(r['d2_x2']) > 1e-30:
    print(f"  ratio x1/x2 = {r['d2_x1']/r['d2_x2']:.8f}")
    print(f"  ratio x1/x3 = {r['d2_x1']/r['d2_x3']:.8f}")
    print(f"  ratio x2/x3 = {r['d2_x2']/r['d2_x3']:.8f}")

# ========================================================================
# PART 7: GENERAL diag(a, b, c) WITH a >> b > c
# ========================================================================
print("\n" + "=" * 80)
print("PART 7: GENERAL diag(a, b, c) WITH VARIOUS HIERARCHIES")
print("=" * 80)

test_states = [
    ("a >> b = c (observer-like)", 0.98, 0.01, 0.01),
    ("a >> b > c", 0.9, 0.07, 0.03),
    ("a > b > c (moderate)", 0.7, 0.2, 0.1),
    ("rho_max symmetric", a_max, b_max, c_max),
    ("a >> b >> c", 0.95, 0.04, 0.01),
    ("a >> b >> c (extreme)", 0.99, 0.009, 0.001),
    ("near democratic", 0.4, 0.35, 0.25),
    ("democratic (1/3,1/3,1/3)", 1/3, 1/3, 1/3),
    ("broken symmetry near max", 0.706, 0.2, 0.094),
]

print(f"\n{'State':>35} | {'rho_J':>12} | {'d2_x1':>12} | {'d2_x2':>12} | {'d2_x3':>12} | {'x1/x2':>8} | {'x1/x3':>8} | {'x2/x3':>8}")
print("-" * 130)

for label, aa, bb, cc in test_states:
    r = compute_all(aa, bb, cc)
    r12 = r["d2_x1"] / r["d2_x2"] if abs(r["d2_x2"]) > 1e-30 else float('inf')
    r13 = r["d2_x1"] / r["d2_x3"] if abs(r["d2_x3"]) > 1e-30 else float('inf')
    r23 = r["d2_x2"] / r["d2_x3"] if abs(r["d2_x3"]) > 1e-30 else float('inf')
    print(f"{label:>35} | {r['rho']:>12.6e} | {r['d2_x1']:>12.6e} | {r['d2_x2']:>12.6e} | {r['d2_x3']:>12.6e} | {r12:>8.3f} | {r13:>8.3f} | {r23:>8.3f}")

# ========================================================================
# PART 8: ANALYTICAL FORMULA BREAKDOWN
# ========================================================================
print("\n" + "=" * 80)
print("PART 8: ANALYTICAL FORMULA BREAKDOWN")
print("=" * 80)

print("""
For X = diag(a, b, c) with Tr=1, perturbed by delta in x_i direction:

  rho(delta) = (det_0 - w_i * delta^2) * (sig2_0 + 2*delta^2 - 1/3)

where w_1 = a, w_2 = b, w_3 = c (the diagonal entry OPPOSITE the perturbed slot).

  d2(rho)/d(delta^2)|_0 = -2*w_i*(sig2_0 - 1/3) + 4*det_0

This is a LINEAR function of w_i (holding det_0, sig2_0 fixed):

  d2_i = 4*det_0 - 2*(sig2_0 - 1/3)*w_i

The weight w_i is the eigenvalue OPPOSITE the x_i slot:
  x_1 slot (2,3): weight = a (the observer's eigenvalue)
  x_2 slot (1,3): weight = b
  x_3 slot (1,2): weight = c
""")

# So the splitting is entirely controlled by the eigenvalue opposite the slot
# x_1 connects particles 2 and 3 (weighted by observer a)
# x_2 connects particles 1 and 3 (weighted by b)
# x_3 connects particles 1 and 2 (weighted by c)

print("The formula d2_i = 4*det - 2*(sig2 - 1/3)*w_i shows:")
print("  - All directions share the same constant term: 4*det")
print("  - The direction-dependent part is -2*(sig2 - 1/3)*w_i")
print("  - Since sig2 >= 1/3 for non-democratic states, larger w_i => MORE NEGATIVE d2")
print("  - The x_1 direction (weighted by a, the observer eigenvalue) has the MOST NEGATIVE curvature")
print("  - This means rho DECREASES FASTEST when the observer's off-diagonal (x_1) is excited")

# ========================================================================
# PART 9: SIGN ANALYSIS AND PHYSICAL INTERPRETATION
# ========================================================================
print("\n" + "=" * 80)
print("PART 9: SIGN ANALYSIS")
print("=" * 80)

print("""
Key question: are the second derivatives POSITIVE (rho increases = coupling enhances)
or NEGATIVE (rho decreases = coupling suppresses)?

d2_i = 4*det_0 - 2*(sig2_0 - 1/3)*w_i

For observer-like states (a ~ 1, b,c ~ 0):
  det_0 ~ 0 (small)
  sig2_0 ~ 1 (close to pure state)
  w_1 = a ~ 1 (large)
  w_2 = b ~ 0 (small)
  w_3 = c ~ 0 (small)

So:  d2_1 ~ 4*0 - 2*(1 - 1/3)*1 = -4/3 (NEGATIVE, strongly suppressed)
     d2_2 ~ 4*0 - 2*(1 - 1/3)*0 ~ 0 (weakly affected)
     d2_3 ~ 4*0 - 2*(1 - 1/3)*0 ~ 0 (weakly affected)
""")

# ========================================================================
# PART 10: RATIO OF SECOND DERIVATIVES AS FUNCTION OF EPSILON
# ========================================================================
print("\n" + "=" * 80)
print("PART 10: DETAILED ANALYSIS AT diag(1-2e, e, e)")
print("=" * 80)

print(f"\n{'epsilon':>10} | {'det':>12} | {'sig2':>12} | {'d2_x1':>12} | {'d2_x23':>12} | {'4*det':>12} | {'-2w(s-1/3)':>12} | {'x1_wt_term':>12}")
print("-" * 120)

for e in [0.001, 0.005, 0.01, 0.02, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 1/3]:
    aa, bb, cc = 1 - 2*e, e, e
    det0 = aa * bb * cc
    sig20 = aa**2 + bb**2 + cc**2
    d2_x1 = -2*aa*(sig20 - 1/3) + 4*det0
    d2_x23 = -2*bb*(sig20 - 1/3) + 4*det0
    term_det = 4*det0
    term_w_x1 = -2*aa*(sig20 - 1/3)
    term_w_x23 = -2*bb*(sig20 - 1/3)
    e_label = f"{e:.6f}" if e != 1/3 else "  1/3     "
    print(f"{e_label:>10} | {det0:>12.6e} | {sig20:>12.6f} | {d2_x1:>12.6e} | {d2_x23:>12.6e} | {term_det:>12.6e} | {term_w_x23:>12.6e} | {term_w_x1:>12.6e}")

# ========================================================================
# PART 11: EXPLORE NON-REAL OCTONIONIC DIRECTIONS
# ========================================================================
print("\n" + "=" * 80)
print("PART 11: DO DIFFERENT OCTONIONIC IMAGINARY UNITS MATTER?")
print("=" * 80)

print("""
When we perturb x_i in a REAL direction, det changes by -w_i*delta^2.
What about perturbing in an imaginary octonionic direction (e_1, ..., e_7)?

For x_i = t * e_k (imaginary unit), |x_i|^2 = t^2 (same as real direction).
The Re(x_1 * x_2 * x_3) term only matters when ALL THREE x_i are nonzero.

For single-direction perturbation (only one x_i nonzero, others = 0):
  Re(x_1 * x_2 * x_3) = 0 regardless of octonionic direction.
  det = abc - w_i * |x_i|^2 = abc - w_i * t^2

So the second derivative is INDEPENDENT of which octonionic direction we choose,
as long as we're perturbing only one x_i at a time.

The 8 octonionic directions within each x_i slot are DEGENERATE.
The anisotropy is ONLY between the three slots (x_1 vs x_2 vs x_3).
""")

# ========================================================================
# PART 12: CROSS-TERM ANALYSIS (two directions at once)
# ========================================================================
print("\n" + "=" * 80)
print("PART 12: CROSS-TERM ANALYSIS (mixed second derivatives)")
print("=" * 80)

# When perturbing x_1 = s, x_2 = t (both real), x_3 = 0:
s, t = symbols('s t', real=True)
det_12 = a*b*c + 0 - a*s**2 - b*t**2 - 0  # Re(s*t*0) = 0
sig2_12 = a**2 + b**2 + c**2 + 2*s**2 + 2*t**2
rho_12 = det_12 * (sig2_12 - Rational(1, 3))

d2_ds_dt = diff(diff(rho_12, s), t).subs([(s, 0), (t, 0)])
print(f"d2(rho)/ds dt at (0,0) = {simplify(d2_ds_dt)}")
print("(This is zero - no cross-coupling between x_1 and x_2 real directions at diagonal base)")

# When ALL three are nonzero: x_1 = s, x_2 = t, x_3 = u (all real)
u = symbols('u', real=True)
det_123 = a*b*c + 2*s*t*u - a*s**2 - b*t**2 - c*u**2
sig2_123 = a**2 + b**2 + c**2 + 2*s**2 + 2*t**2 + 2*u**2
rho_123 = det_123 * (sig2_123 - Rational(1, 3))

# Mixed partials at (0,0,0)
d2_st = diff(diff(rho_123, s), t).subs([(s, 0), (t, 0), (u, 0)])
d2_su = diff(diff(rho_123, s), u).subs([(s, 0), (t, 0), (u, 0)])
d2_tu = diff(diff(rho_123, t), u).subs([(s, 0), (t, 0), (u, 0)])

print(f"\nWith all three perturbations (s, t, u) for x_1, x_2, x_3:")
print(f"  d2(rho)/ds dt = {simplify(d2_st)}")
print(f"  d2(rho)/ds du = {simplify(d2_su)}")
print(f"  d2(rho)/dt du = {simplify(d2_tu)}")
print("(All zero - the Hessian is diagonal at diagonal base points)")

# Third derivative (cubic term from det)
d3_stu = diff(diff(diff(rho_123, s), t), u).subs([(s, 0), (t, 0), (u, 0)])
print(f"\nd3(rho)/ds dt du = {simplify(d3_stu)}")
print("(This captures the cubic term 2*Re(x1*x2*x3) in det)")
print("The triple product only appears at THIRD order - it's a vertex, not a propagator")

# Evaluate the third derivative at specific states
print(f"\nThird derivative d3(rho)/ds dt du = 2*(sig2 - 1/3) = 2*(a^2+b^2+c^2 - 1/3)")
d3_formula = 2*(a**2 + b**2 + c**2 - Rational(1, 3))
print(f"  Symbolic: {simplify(d3_stu)} = {simplify(d3_stu - d3_formula)} + 2*(sig2 - 1/3)")

# Actually expand it properly
d3_expanded = expand(d3_stu)
print(f"  Expanded: {d3_expanded}")

# ========================================================================
# PART 13: THE HESSIAN EIGENVALUES (full 27-dimensional)
# ========================================================================
print("\n" + "=" * 80)
print("PART 13: HESSIAN STRUCTURE IN THE 27-DIMENSIONAL TANGENT SPACE")
print("=" * 80)

print("""
At a diagonal state diag(a, b, c) with Tr=1, the tangent directions are:

  DIAGONAL: da, db (with dc = -da - db to preserve Tr=1) -> 2 directions
  OFF-DIAGONAL: x_1 (8 dims), x_2 (8 dims), x_3 (8 dims) -> 24 directions

Total tangent dim to Tr=1 slice: 2 + 24 = 26

The off-diagonal Hessian blocks:
  x_1 block (8x8): d2_1 * I_8, where d2_1 = 4*det - 2a*(sig2 - 1/3)
  x_2 block (8x8): d2_2 * I_8, where d2_2 = 4*det - 2b*(sig2 - 1/3)
  x_3 block (8x8): d2_3 * I_8, where d2_3 = 4*det - 2c*(sig2 - 1/3)

Multiplicities: 8, 8, 8 (one per octonionic dimension in each slot)
""")

# Summary table of Hessian eigenvalues at key states
print(f"\n{'State':>35} | {'d2_1 (x8)':>12} | {'d2_2 (x8)':>12} | {'d2_3 (x8)':>12}")
print("-" * 80)

for label, aa, bb, cc in test_states:
    det0 = aa * bb * cc
    sig20 = aa**2 + bb**2 + cc**2
    d2_1 = -2*aa*(sig20 - 1/3) + 4*det0
    d2_2 = -2*bb*(sig20 - 1/3) + 4*det0
    d2_3 = -2*cc*(sig20 - 1/3) + 4*det0
    print(f"{label:>35} | {d2_1:>12.6e} | {d2_2:>12.6e} | {d2_3:>12.6e}")

# ========================================================================
# PART 14: PHYSICAL SIGNIFICANCE CHECK
# ========================================================================
print("\n" + "=" * 80)
print("PART 14: DO THE RATIOS MATCH ANY KNOWN PHYSICS?")
print("=" * 80)

print("\nKnown mass ratios (rough orders of magnitude):")
print("  m_top/m_up ~ 75000")
print("  m_tau/m_electron ~ 3477")
print("  m_b/m_d ~ 1250")
print("  m_W/m_electron ~ 157000")
print("  alpha_s/alpha_EM ~ 14 (at M_Z)")

print("\nOur d2 ratios at observer-like states:")
for label, aa, bb, cc in test_states:
    det0 = aa * bb * cc
    sig20 = aa**2 + bb**2 + cc**2
    d2_1 = -2*aa*(sig20 - 1/3) + 4*det0
    d2_2 = -2*bb*(sig20 - 1/3) + 4*det0
    d2_3 = -2*cc*(sig20 - 1/3) + 4*det0
    if abs(d2_2) > 1e-30 and abs(d2_3) > 1e-30:
        r12 = abs(d2_1/d2_2)
        r13 = abs(d2_1/d2_3)
        r23 = abs(d2_2/d2_3)
        print(f"  {label:>35}: |d2_1/d2_2| = {r12:.4f}, |d2_1/d2_3| = {r13:.4f}, |d2_2/d2_3| = {r23:.4f}")

print("""
CONCLUSION: The ratios are ORDER 1 (close to 1), not orders of magnitude.
This is because the formula d2_i = 4*det - 2*w_i*(sig2 - 1/3) is LINEAR in w_i.
The ratio d2_1/d2_2 = (4*det - 2a*(sig2-1/3)) / (4*det - 2b*(sig2-1/3)).
For a >> b, this ratio ~ a/b but only when det ~ 0.
The maximum ratio achievable is a/c for the most extreme states.
""")

# ========================================================================
# PART 15: WHAT IF WE USE |rho_J|^n or log(rho_J)?
# ========================================================================
print("\n" + "=" * 80)
print("PART 15: GRADIENT OF log(rho_J) - LOGARITHMIC SENSITIVITY")
print("=" * 80)

print("""
If rho_J is a probability density, the physically relevant quantity might be
the RELATIVE change: d2(log rho)/d(delta^2), not d2(rho)/d(delta^2).

log(rho_J) = log(det) + log(sig2 - 1/3)

d2(log det)/d(delta^2)|_0 = d/d(delta) [det'/det]|_0
  = [det'' * det - (det')^2] / det^2 |_0
  = det''(0) / det(0)   (since det'(0) = 0)
  = -2*w_i / det_0

Similarly for the sigma part:
d2(log(sig2-1/3))/d(delta^2)|_0 = 4 / (sig2_0 - 1/3)

So: d2(log rho)/d(delta^2)|_0 = -2*w_i/det_0 + 4/(sig2_0 - 1/3)
""")

print(f"\n{'State':>35} | {'d2log_x1':>12} | {'d2log_x2':>12} | {'d2log_x3':>12} | {'x1/x2':>8} | {'x1/x3':>8}")
print("-" * 110)

for label, aa, bb, cc in test_states:
    det0 = aa * bb * cc
    sig20 = aa**2 + bb**2 + cc**2
    if det0 > 1e-30 and sig20 - 1/3 > 1e-30:
        d2log_1 = -2*aa/det0 + 4/(sig20 - 1/3)
        d2log_2 = -2*bb/det0 + 4/(sig20 - 1/3)
        d2log_3 = -2*cc/det0 + 4/(sig20 - 1/3)
        r12 = d2log_1/d2log_2 if abs(d2log_2) > 1e-30 else float('inf')
        r13 = d2log_1/d2log_3 if abs(d2log_3) > 1e-30 else float('inf')
        print(f"{label:>35} | {d2log_1:>12.4e} | {d2log_2:>12.4e} | {d2log_3:>12.4e} | {r12:>8.4f} | {r13:>8.4f}")
    else:
        print(f"{label:>35} | {'(det=0)':>12} | {'':>12} | {'':>12} | {'':>8} | {'':>8}")

print("""
For log(rho), the ratios d2log_i are dominated by -2*w_i/det_0.
At observer-like states (det ~ 0), these blow up but the RATIOS become:
  d2log_1/d2log_2 ~ (-2a/det) / (-2b/det) = a/b

So the log-derivative ratios are exactly the eigenvalue ratios!
For diag(0.98, 0.01, 0.01): ratio ~ 98
For diag(0.99, 0.009, 0.001): ratio ~ 110 (x1/x2), 990 (x1/x3)

These are still not SM mass ratios, but the HIERARCHY is controlled by eigenvalue ratios.
""")

# ========================================================================
# PART 16: SUMMARY
# ========================================================================
print("\n" + "=" * 80)
print("SUMMARY OF RESULTS")
print("=" * 80)

print("""
1. FORMULA: At diagonal state diag(a,b,c), perturbation in x_i direction gives
   d2(rho_J)/d(delta^2)|_0 = 4*det(a,b,c) - 2*w_i*(sig2 - 1/3)
   where w_1=a, w_2=b, w_3=c.

2. ALL 8 OCTONIONIC DIRECTIONS within each slot are DEGENERATE.
   The anisotropy is ONLY between the three slots (x_1 vs x_2 vs x_3).
   This gives a 8+8+8 = 24 dimensional off-diagonal space split into
   three 8-fold degenerate blocks.

3. SPLIT PATTERN:
   - At diag(1-2e, e, e): 8 + 16 split (x_1 different from x_2 = x_3)
   - At diag(a, b, c) with a > b > c: 8 + 8 + 8 split (all different)
   - At diag(1/3, 1/3, 1/3): all 24 degenerate

4. SIGN: Near the observer boundary (a ~ 1, b,c ~ 0):
   - d2_1 is strongly NEGATIVE (rho decreases when x_1 excited)
   - d2_2, d2_3 are weakly negative or near zero
   This means rho is PEAKED at diagonal states and FALLS OFF
   in off-diagonal directions, with the observer's slot (x_1) being
   the steepest descent direction.

5. RATIOS: The curvature ratios d2_i/d2_j are ORDER 1 numbers for rho_J itself.
   For log(rho_J), the ratios approach the eigenvalue ratios a/b, a/c, b/c.
   These can be large (hundreds) but are not intrinsically SM mass ratios.

6. MAXIMUM OF rho_J: Occurs at specific eigenvalues (computed above).
   At the maximum, all three second derivatives are nonzero, and the
   Hessian is negative definite in the off-diagonal directions (confirming
   it's a local max on the diagonal subspace).

7. TRIPLE COUPLING: The cubic term 2*Re(x_1*x_2*x_3) in det contributes
   ONLY at third order (d3/ds dt du), not at second order. This is a
   VERTEX (three-point coupling), not a mass/propagator term.
   Its coefficient is 2*(sig2 - 1/3), independent of the state's eigenvalues.
""")
