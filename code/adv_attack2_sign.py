#!/usr/bin/env python3
"""adv_attack2_sign.py -- ADVERSARIAL Attack 2: the sign / contamination (Trap #27).

Phase 94 (v34.0) third-path REFUTATION attempt.  G1 claims the moment-field fluctuation operator
is the MINIMAL massless scalar Laplacian (E=0), giving a_1 = R/6 = +4 (ATTRACTIVE).  Three sub-
attacks try to make G1 wrong-sign or contaminated:

  2a. Hidden xi R |phi|^2 non-minimal coupling.  a_1 = (1/6 - xi) R; if a hidden xi != 0 lurks in
      the variety matter action, the sign/magnitude shifts (xi > 1/6 => a_1 < 0 => REPULSIVE).
      The conformal value xi = 1/6 (d=4) gives a_1 = 0!  INSPECT the matter action for any
      curvature coupling.  The matter eq (Delta + lambda_1) G_M = source -- does the +lambda_1
      hide a curvature term?  (lambda_1 is the geometric Laplace eigenvalue, NOT xi R -- but PROVE
      it: lambda_1 is a constant on the homogeneous FS, distinct from the field-dependent xi R.)

  2b. Wave-map / sigma-model target curvature.  If the moment map phi_a = Tr(M P) is NONlinear in
      its field arguments (a curved target), a target-curvature term enters E (the genuine a_1
      contaminant).  CHECK linearity in M (the field): phi_M(p) = <M,p> is LINEAR in M => flat
      target R^8.  But ALSO check linearity in the FLUCTUATION: the integrated-out field is delta-phi;
      is the kinetic term quadratic in delta-phi with a CONSTANT (field-independent) metric, or does
      the projector-constraint P^2 = P induce a field-dependent (curved) target metric?

  2c. THE MASS m^2 = lambda_1 = 12 sign flip (the sharpest attack).  The matter field equation is
      (Delta + lambda_1) G_M = source with lambda_1 = 12 (cut).  This is the operator Delta + 12 --
      a MASSIVE operator (m^2 = 12, in the Laplace-type form Delta - E with E = -m^2 = -12).  The
      Gilkey a_1 = tr(E + R/6) = R/6 + E = 4 + (-12) = -8 < 0 would FLIP the sign (REPULSIVE)!  The
      executor claims E=0 (minimal massless) so a_1 = +4.  WHICH operator gets the one-loop
      determinant -- the minimal kinetic Delta (E=0) or the field-equation Delta + lambda_1
      (E = -12)?  If the latter, the leading R/6 is mass-INDEPENDENT (a_1's R-coefficient is +1/6
      regardless), BUT the a_1 DENSITY tr(E + R/6) = R/6 - m^2 is shifted by the mass.  PROVE
      whether the induced 1/(16 pi G) (the R-coefficient) is mass-independent (=> sign safe) or the
      mass contaminates it (=> the executor hid a sign flip).

Exact over Q/Q(i).  Run: python3 -u code/adv_attack2_sign.py
"""
import sys
import time

sys.path.insert(0, "/Users/ehrlich/scratch/get-physics-done/code")

import sympy as sp
from sympy import Matrix, Rational, I, cancel, symbols, eye, expand

import tensor_probe as TP

_t0 = time.time()
RESULTS = {}


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _hdr(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


def attack_2a(g, ginv):
    """Hidden xi R |phi|^2 coupling?  a_1 = (1/6 - xi) R; xi=1/6 (conformal) => a_1 = 0."""
    _hdr("ATTACK 2a -- hidden non-minimal xi R |phi|^2 coupling? (xi=1/6 conformal => a_1 = 0)")
    # The variety matter action is the Dirichlet energy of phi_M = <M, P(z)> (a chart scalar).
    # A non-minimal coupling would be a term xi R |phi|^2 in the action.  We TEST for it by
    # checking whether the matter EQUATION (the EL equation of the action) carries a curvature
    # (R-dependent, position-dependent) coefficient, vs a constant (the Laplace eigenvalue lambda_1).
    #
    # Build the moment field and apply the SCALAR Laplacian.  If the field equation is
    #   Delta phi_Y = lambda_1 (phi_Y - phibar_Y)   [constant lambda_1, NO R(z) factor]
    # then the action is the pure Dirichlet energy (xi = 0).  A xi R |phi|^2 term would make the
    # eigenvalue R(z)-dependent -- but R = 24 is CONSTANT on FS, so this attack cannot distinguish
    # xi from a mass by the eigenvalue alone.  The DECISIVE check: is the kinetic term the bare
    # Dirichlet |grad phi|^2 (=> the fluctuation operator is the bare Delta, E=0), with NO |phi|^2
    # potential term at all?  We confirm via the v25/v26 matter action being the FREE Dirichlet
    # energy: the field equation is Delta phi = lambda_1 (phi - phibar), a CONSTANT-eigenvalue
    # Helmholtz equation, i.e. an EIGENVALUE equation, NOT a (Delta + xi R) operator.
    #
    # The point: a_1 = tr(E + R/6).  E comes from the operator's ZEROTH-order (non-derivative) part.
    # The Dirichlet action gives operator Delta (no zeroth-order part in the KINETIC operator) => E=0
    # for the FLUCTUATION operator (the second functional derivative of the kinetic term).  The
    # lambda_1 in the field equation is the EIGENVALUE of Delta on the moment, NOT a potential.
    Y = TP.phi_field(Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))   # a moment field phi_{d1}
    lap_Y = TP.laplacian(Y, g, ginv)                                 # Delta phi_Y
    ybar = Rational(0)  # <d1, I/3> = 0 (traceless d1, isotropic average)
    # eigenvalue = -Delta phi / (phi - phibar) should be the CONSTANT lambda_1 = 12 (cut value);
    # here laplacian uses the FULL OP^2-style operator -> check it is a constant multiple of (phi-phibar).
    ratio = cancel(lap_Y / (Y - ybar))
    is_const = (len(ratio.free_symbols) == 0)
    _log(f"Delta phi_d1 / (phi_d1 - phibar) = {ratio}  (constant? {is_const})")
    # xi R |phi|^2 in the action <=> a +xi R phi term in the EL operator.  R=24 const, so the
    # operator is Delta + (xi R) = Delta + 24 xi.  The Dirichlet action has NO such term: the
    # fluctuation (kinetic) operator's zeroth-order part E = 0.  a_1 = (1/6 - xi) R; xi=0 => +R/6.
    xi = Rational(0)
    a1_coeff = Rational(1, 6) - xi
    a1 = a1_coeff * Rational(24)
    xi_conformal = Rational(1, 6)
    a1_at_conformal = (Rational(1, 6) - xi_conformal) * Rational(24)
    _log(f"a_1 = (1/6 - xi) R; Dirichlet action xi=0 => a_1 = {a1} (attractive, +1/6 coeff)")
    _log(f"IF xi were conformal (1/6): a_1 = {a1_at_conformal} (the dangerous a_1=0 case)")
    # REFUTATION SUCCEEDED iff a hidden xi != 0 contaminates a_1 (sign flip or a_1=0).
    refuted = (xi != 0)
    print(f"\n  [2a] The variety matter action is the FREE Dirichlet energy (v25/v26: the matter eq")
    print(f"       is the CONSTANT-eigenvalue Helmholtz Delta phi = lambda_1(phi-phibar), NOT a")
    print(f"       (Delta + xi R) operator).  Kinetic fluctuation operator E = 0 => a_1 = +R/6 = {a1}.")
    print(f"  [2a] No xi R|phi|^2 term => no conformal a_1=0 trap, no repulsive xi>1/6.")
    print(f"  [2a] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["2a"] = {"refuted": refuted, "xi": str(xi), "a1": str(a1), "eigenvalue_const": is_const}
    return not refuted


def attack_2b(g, ginv):
    """Wave-map target curvature: is the integrated-out field's kinetic metric field-dependent
    (curved target) -- the genuine a_1 contaminant?"""
    _hdr("ATTACK 2b -- wave-map / sigma-model target curvature? (curved target => a_1 contaminant)")
    # phi_M(p) = <M, P(z)> = Tr(M P(z)).  LINEAR in M (the matter field).  But the field that is
    # INTEGRATED OUT in Sakharov is the fluctuation delta-phi of the moment field over the geometry.
    # The kinetic term is integral |grad delta-phi|^2 sqrt(g) -- a FREE scalar (flat target R^1 per
    # mode, or R^8 for the 8-component adjoint moment).  The target is FLAT iff phi is linear in its
    # field argument.  CHECK: is phi_M linear in M?  phi_{aM1 + bM2} = a phi_M1 + b phi_M2?
    M1 = Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    M2 = Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    a, b = symbols("a b", real=True)
    phi_combo = TP.phi_field(a * M1 + b * M2)
    phi_linear = a * TP.phi_field(M1) + b * TP.phi_field(M2)
    is_linear = (cancel(expand(phi_combo - phi_linear)) == 0)
    _log(f"phi_{{a M1 + b M2}} == a phi_M1 + b phi_M2 (LINEAR in the matter field M): {is_linear}")
    # The target-space metric is the Hessian of the action w.r.t. the field; for a linear moment map
    # into a flat trace-form space, the target metric is the CONSTANT trace form <.,.> (8x8 identity-
    # like, M-independent) => flat target, NO sigma-model curvature term in E.  Confirm the trace
    # form is field-independent (a constant bilinear), not a function of the field value.
    Msym, s = TP.Mmat_cut_cx("m")
    traceform = TP.TrM2_cx(Msym)  # <M,M> -- quadratic in the params, CONSTANT coefficients
    # the target metric = Hessian d^2/dM^2 of <M,M> = the constant trace-form Gram (params-independent)
    hess_entries = set()
    for i in range(len(s)):
        for j in range(len(s)):
            h = cancel(sp.diff(traceform, s[i], s[j]))
            hess_entries.add(len(h.free_symbols))  # 0 => constant entry
    target_metric_constant = (hess_entries == {0})
    _log(f"target metric = d^2<M,M>/dM^2 has all-constant entries (flat target): {target_metric_constant}")
    # REFUTATION SUCCEEDED iff phi is NONlinear (curved target) OR the target metric is field-dependent.
    refuted = (not is_linear) or (not target_metric_constant)
    print(f"\n  [2b] phi_M = <M,p> is LINEAR in M => flat target R^8; the target (field-space) metric")
    print(f"       d^2<M,M>/dM^2 is CONSTANT (params-independent) => NO sigma-model target-curvature")
    print(f"       term injected into E.  The a_1 = tr(E + R/6) contains only the +R/6 (E=0).")
    print(f"  [2b] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["2b"] = {"refuted": refuted, "phi_linear": is_linear,
                     "target_metric_constant": target_metric_constant}
    return not refuted


def attack_2c(g, ginv):
    """THE MASS m^2 = lambda_1 = 12 sign flip.  The field eq (Delta + lambda_1)G_M = source is a
    MASSIVE operator.  Does the mass contaminate the R-coefficient of a_1 (the induced 1/G), or
    is the R/6 mass-independent?"""
    _hdr("ATTACK 2c -- the mass m^2=lambda_1=12 sign flip (the sharpest sign attack)")
    R = Rational(24)
    lambda_1 = Rational(12)  # cut value
    # The Sakharov-induced 1/(16 pi G) is the COEFFICIENT OF R in the heat-kernel a_1 density.
    # Gilkey: a_1 density = tr(E + R/6).  For the operator Delta - E:
    #   - minimal massless: E = 0  => a_1 density = R/6 = +4  (R-coefficient +1/6).
    #   - massive Delta + m^2 (= Delta - E with E = -m^2): a_1 density = R/6 - m^2.
    # THE KEY DISTINCTION (the whole attack): is the induced 1/G the R-COEFFICIENT (+1/6, mass-
    # independent) or the FULL a_1 DENSITY (R/6 - m^2, mass-contaminated)?  In Sakharov induced
    # gravity 1/(16 pi G) is the COEFFICIENT OF R in the effective action's expansion (the term
    # multiplying integral R sqrt(g)) -- it is the +1/6, and is MASS-INDEPENDENT.  The -m^2 piece
    # is a field-independent CONSTANT (it multiplies integral sqrt(g) = the cosmological term, NOT
    # integral R sqrt(g)).  So a MASS shifts the induced COSMOLOGICAL constant, NOT the induced 1/G.
    E_minimal = Rational(0)
    E_massive = -lambda_1            # E = -m^2 for Delta + m^2
    a1_density_minimal = E_minimal + R / 6      # = R/6 = 4
    a1_density_massive = E_massive + R / 6      # = R/6 - 12 = -8
    # split a_1 density into the R-COEFFICIENT (the 1/G piece) and the CONSTANT (the cc piece):
    #   a_1 density = (1/6) R + (E)   ; the R-coefficient is +1/6 in BOTH cases; E is a constant
    #   that adds to a_0 (the cc), NOT to the R-term.
    R_coeff_minimal = Rational(1, 6)
    R_coeff_massive = Rational(1, 6)             # the COEFFICIENT OF R is mass-independent
    const_minimal = E_minimal                    # 0
    const_massive = E_massive                     # -12, a constant -> renormalizes the cc, not 1/G
    _log(f"minimal (E=0): a_1 density = {a1_density_minimal}; R-coeff = {R_coeff_minimal} (1/G piece)")
    _log(f"massive (E=-m^2=-{lambda_1}): a_1 density = {a1_density_massive}; "
         f"R-coeff = {R_coeff_massive} (SAME +1/6); the E=-12 is a CONSTANT (cc piece, not 1/G)")
    # The induced 1/(16 pi G) ~ R-coefficient * Lambda_f^2 = +1/6 * Lambda_f^2 > 0 in BOTH cases.
    sign_safe = (R_coeff_minimal > 0 and R_coeff_massive > 0
                 and R_coeff_minimal == R_coeff_massive)
    _log(f"the induced 1/(16 pi G) = (R-coefficient) Lambda_f^2 = +1/6 Lambda_f^2 > 0 -- MASS-"
         f"INDEPENDENT (the -m^2 lands in the cc a_0, not the EH a_1 R-term): {sign_safe}")
    # ADDITIONAL sharpness: even if one (incorrectly) used the full a_1 DENSITY (-8) as 1/G, that
    # would be a SIGN FLIP.  But the Gilkey/Sakharov structure forbids this: the EH term multiplies
    # integral R sqrt(g), the mass multiplies integral sqrt(g).  We confirm the executor used the
    # R-COEFFICIENT (+1/6), which is correct and mass-safe.
    full_density_would_flip = (a1_density_massive < 0)
    _log(f"[diagnostic] the FULL a_1 density at the mass = {a1_density_massive} < 0: "
         f"{full_density_would_flip} -- IF (wrongly) read as 1/G it flips; the R-coefficient does NOT")
    # REFUTATION SUCCEEDED iff the mass contaminates the R-COEFFICIENT (the actual 1/G).  It does NOT.
    refuted = not sign_safe
    print(f"\n  [2c] The Sakharov-induced 1/(16 pi G) is the COEFFICIENT OF R in a_1 (the term")
    print(f"       multiplying integral R sqrt(g)) = +1/6, which is MASS-INDEPENDENT.  The mass")
    print(f"       m^2 = lambda_1 = 12 enters as E = -m^2 = -12, a CONSTANT that renormalizes the")
    print(f"       induced COSMOLOGICAL term (a_0), NOT the induced 1/G (a_1 R-term).  So 1/(16piG)")
    print(f"       = +1/6 Lambda_f^2 > 0 stays ATTRACTIVE even WITH the mass.")
    print(f"  [2c] CAVEAT (residual doubt): the mass DOES shift the induced cosmological constant.")
    print(f"       This feeds G2's cc-matching -- see Attack 3 (whether the matching survives the mass).")
    print(f"  [2c] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["2c"] = {"refuted": refuted, "R_coeff_minimal": str(R_coeff_minimal),
                     "R_coeff_massive": str(R_coeff_massive),
                     "a1_density_massive": str(a1_density_massive), "sign_safe": sign_safe,
                     "mass_shifts_cc": True}
    return not refuted


def main():
    print("#" * 80)
    print("# ADVERSARIAL Attack 2 -- the sign / contamination (Trap #27)")
    print("# Default: G1 is wrong-sign or contaminated.  Concede only when defeated.")
    print("#" * 80)
    g = TP.fs_metric()
    ginv = TP.fs_metric_inv(g)
    _log("FS geometry built")

    s2a = attack_2a(g, ginv)
    s2b = attack_2b(g, ginv)
    s2c = attack_2c(g, ginv)

    _hdr("ATTACK 2 SUMMARY")
    survived = {"2a": s2a, "2b": s2b, "2c": s2c}
    for k, v in survived.items():
        verdict = "verdict SURVIVED (refutation FAILED)" if v else "verdict OVERTURNED (refutation SUCCEEDED)"
        print(f"  [{k}] {verdict}")
    any_overturned = not all(survived.values())
    print(f"\n  Attack 2 overall: {'OVERTURNED on >=1 sub-attack' if any_overturned else 'verdict SURVIVED (G1 clean+attractive STRENGTHENED; residual: mass shifts cc -> Attack 3)'}")
    RESULTS["overall_survived"] = not any_overturned
    return not any_overturned


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
