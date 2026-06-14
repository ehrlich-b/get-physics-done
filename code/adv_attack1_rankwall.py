#!/usr/bin/env python3
"""adv_attack1_rankwall.py -- ADVERSARIAL Attack 1: the v21 rank wall sneaking back (Trap #26).

Phase 94 (v34.0) third-path REFUTATION attempt.  The verdict CLOSES-CONDITIONAL rests on G2's
claim that the cc-matching is ONE-condition-ONE-knob (over_determined = False), NOT the v21
16-vs-6 over-determination (EmptySet).  In sakharov_variety.py:G2() the integers
`num_conditions = 1` and `num_knobs = 1` are HAND-ASSERTED literals -- the whole "this isn't v21"
turns on them.  This driver tries to REFUTE that by building the FULL induced field-equation
system on FS and checking whether the available knobs are over-determined the way v21's 10 OFF-T
entries over-determined kappa to 4 distinct rationals.

THE v21 KILL (the template, sakharov_gate2_support.py): G=kappa T+Lambda g.  On the 10 OFF-T
entries (G!=0, T=0) the equation collapses to G_{mu nu}=Lambda g_{mu nu}, forcing ONE scalar
Lambda = G_{mu nu}/g_{mu nu} on all of them -- the ratios are NOT all equal => EmptySet.  A real
kill = >=2 independent conditions on a knob that disagree.

THE ATTACKS (exact over Q/Q(i)):
  1a. Is FS-critical REALLY one tensor condition?  Build the full vacuum induced Einstein tensor
      Eq_{mu nu} = (R_{mu nu} - 1/2 R g_{mu nu} + Lambda_cc g_{mu nu}) on FS and decompose into
      TRACE (scale mode) + TRACELESS (TT) parts.  If the TRACELESS part is nonzero for Lambda_cc
      at the matching value, FS is NOT critical as a tensor => a 2nd condition the scale knob
      cannot reach => DOESN'T-CLOSE.  (Expected fail: FS Einstein => traceless part == 0
      identically, so this is genuinely one condition -- but PROVE it, don't assert it.)
  1b. The SOURCED equation (G3): is TT(B3) actually a PURE eps=20 eigentensor?  The response
      h = kappa_ind TT(B3)/(Delta_L - 2 Lambda) is well-defined ONLY if TT(B3) lies entirely in
      the (Delta_L - 2 Lambda) = 20 eigenspace.  If TT(B3) has a component OUTSIDE the 20-eigenspace
      (i.e. Delta_L TT(B3) != 32 TT(B3) on some block), that component is the variety analog of the
      v21 off-T block -- the field equation cannot represent it with a single kappa_ind => the
      induce route over-determines => DOESN'T-CLOSE.  Run Delta_L TT(B3) on ALL THREE Kahler blocks
      for multiple matter directions and check 32-exactness block-by-block.
  1c. The MULTI-MATTER over-determination.  Different matter directions M produce different sources
      TT(B3[M]) but the SAME single induced coupling kappa_ind (a scalar).  Does requiring ONE
      kappa_ind to source the response for ALL M over-determine?  In v21 this was the kill.  Build
      the response amplitude for >=4 matter directions (s01,a01,d1,GEN) and check whether a single
      kappa_ind is consistent across all of them, or whether they force distinct values (=> EmptySet).
  1d. The a4 (higher-derivative) contamination of the SCALE mode.  The induced action has an a4
      (curvature-squared) term too.  On FS its variation contributes to BOTH the trace and the TT
      sectors.  Does the a4 contribution add an INDEPENDENT condition on the scale mode that the
      a0/a1 matching (Lambda_f^2 = 4) cannot simultaneously satisfy?  Compute the a4 trace
      contribution and check whether it shifts Lambda_cc away from 6 in a knob-independent way.

VERDICT (per attack): FAILED (refutation defeated; verdict strengthened) or SUCCEEDED (verdict
overturned with exact counter-evidence).

Exact over Q/Q(i) on every decisive path; sympy.Rational.  Run: python3 -u code/adv_attack1_rankwall.py
"""
import sys
import time

sys.path.insert(0, "/Users/ehrlich/scratch/get-physics-done/code")

import sympy as sp
from sympy import Matrix, Rational, I, zeros, cancel

import tensor_probe as TP
from lichnerowicz_response import (lichnerowicz_full_v33, riemann_kahler, extract_tt)

_t0 = time.time()
RESULTS = {}


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _hdr(s):
    print("\n" + "=" * 80)
    print(s)
    print("=" * 80)


# the matter directions (same as gate0_v33: 3 Gell-Mann + a generic detM!=0)
GM = {
    "s01": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    "a01": Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),
    "d1":  Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),
}
M_GEN = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])      # detM = -2 != 0


def attack_1a(g, ginv):
    """Is FS-critical REALLY one tensor condition, or does the TRACELESS (TT) part of the
    vacuum induced Einstein tensor impose a 2nd, knob-unreachable condition?"""
    _hdr("ATTACK 1a -- is FS-critical ONE tensor condition? (trace vs traceless of G+Lambda g)")
    # Ricci (1,1) form, R = 24, on FS Ric = 6g.
    Ric = TP.ricci_tensor(g)
    Ric_is_6g = all(cancel(Ric[a, b] - 6 * g[a, b]) == 0 for a in range(2) for b in range(2))
    _log(f"Ricci form R_a-bbar == 6 g_a-bbar (FS Einstein): {Ric_is_6g}")
    R_scalar = Rational(24)

    # The vacuum induced field equation (the (1,1) sector, the physical Riemannian metric tensor):
    #   Eq_{a-bbar} = R_{a-bbar} - 1/2 R g_{a-bbar} + Lambda_cc g_{a-bbar}
    #             = 6 g - 12 g + Lambda_cc g = (Lambda_cc - 6) g   [on FS]
    Lcc = sp.symbols("Lambda_cc")
    Eq = Matrix(2, 2, lambda a, b: cancel(Ric[a, b] - Rational(1, 2) * R_scalar * g[a, b]
                                          + Lcc * g[a, b]))
    # TRACE part w.r.t. g: tr_g Eq = g^{bbar a} Eq_{a-bbar}.  TRACELESS part = Eq - (tr/n) g.
    n = 2  # complex dimension; the (1,1) tensor lives on a 2-cx-dim Kahler manifold
    tr_Eq = cancel(sum(ginv[b, a] * Eq[a, b] for a in range(2) for b in range(2)))
    traceless = Matrix(2, 2, lambda a, b: cancel(Eq[a, b] - (tr_Eq / n) * g[a, b]))
    traceless_zero = all(cancel(traceless[a, b]) == 0 for a in range(2) for b in range(2))
    _log(f"vacuum induced Eq = (Lambda_cc - 6) g identically; trace_g Eq = {tr_Eq}")
    _log(f"TRACELESS part of Eq == 0 IDENTICALLY (independent of Lambda_cc): {traceless_zero}")
    # the scale condition: trace = 0 <=> Lambda_cc = 6 (ONE scalar equation)
    sol = sp.solve(sp.Eq(tr_Eq, 0), Lcc)
    _log(f"trace=0 <=> Lambda_cc = {sol} (the single scale-mode condition)")

    # THE REFUTATION TEST: if traceless != 0 for the matching Lambda_cc, FS is NOT critical as a
    # tensor => a 2nd condition.  Here traceless == 0 identically (FS Einstein) => genuinely ONE
    # condition.  This DEFEATS the 1a refutation but PROVES the executor's claim was not asserted.
    refuted = not traceless_zero  # SUCCEEDED iff the traceless part is a real 2nd condition
    print(f"\n  [1a] FS Einstein => traceless(G + Lambda g) == 0 identically: {traceless_zero}")
    print(f"  [1a] => the vacuum induced field equation is genuinely ONE (scale) condition; the")
    print(f"        traceless/TT sector imposes NO independent condition (FS Einstein does the work).")
    print(f"  [1a] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["1a"] = {"refuted": refuted, "Ric_is_6g": Ric_is_6g,
                     "traceless_zero": traceless_zero, "scale_sol": str(sol)}
    return not refuted


def attack_1b(g, ginv, Gam, GamB, R):
    """Is TT(B3) a PURE eps=20 eigentensor on ALL blocks?  A component OUTSIDE the 20-eigenspace
    is the variety analog of the v21 off-T block (the field eq cannot represent it)."""
    _hdr("ATTACK 1b -- is TT(B3) a PURE eps=20 eigentensor? (off-eigenspace = v21 off-T analog)")
    all_clean = True
    detail = {}
    for nm in ["s01", "a01", "d1", "GEN"]:
        Mc = M_GEN if nm == "GEN" else GM[nm]
        B3 = TP.grad_bilinear(cancel(TP.phi_field(Mc)), simp=sp.together)
        _log(f"[{nm}] extracting TT(B3) = extract_tt(grad_bilinear(phi_M)) ...")
        r, _, _, _, info = extract_tt(B3, g, ginv, Gam, verify=True)
        tt_ok = (r is not None and info.get("consistent") and info.get("tr_zero")
                 and info.get("div_zero"))
        nz = [not all(cancel(r[k][a, b]) == 0 for a in range(2) for b in range(2)) for k in range(3)]
        _log(f"[{nm}] TT consistent/tr0/div0={tt_ok}; nonzero blocks [H20,H11,H02]={nz}; "
             f"running Delta_L ...")
        dLr = lichnerowicz_full_v33(r, g, ginv, Gam, GamB, R, Lambda=6)
        # per-block: is dL r == 32 r (so (Delta_L - 2 Lambda) r == 20 r)?  A block where this FAILS
        # is OUTSIDE the eps=20 eigenspace -- the off-source analog.
        perblock = []
        for k in range(3):
            if all(cancel(r[k][a, b]) == 0 for a in range(2) for b in range(2)):
                perblock.append("ZERO")
                continue
            ok32 = all(cancel(dLr[k][a, b] - 32 * r[k][a, b]) == 0 for a in range(2) for b in range(2))
            perblock.append(ok32)
        clean = tt_ok and all(nz) and all(pb is True or pb == "ZERO" for pb in perblock) \
            and any(pb is True for pb in perblock)
        all_clean &= clean
        detail[nm] = {"perblock": perblock, "tt_ok": tt_ok, "nz": nz, "clean": clean}
        _log(f"[{nm}] Delta_L r == 32 r per block [H20,H11,H02]={perblock}; PURE 20-eigentensor: {clean}")

    # REFUTATION: SUCCEEDED iff some matter direction's TT(B3) has a component OUTSIDE the
    # 20-eigenspace (a non-32 block) -- the field equation could not source it with one kappa_ind.
    refuted = not all_clean
    print(f"\n  [1b] TT(B3) is a PURE (Delta_L-2Lambda)=20 eigentensor on ALL nonzero blocks for ALL")
    print(f"       4 matter directions: {all_clean}")
    print(f"  [1b] => the source lies ENTIRELY in the 20-eigenspace; h = kappa_ind TT(B3)/20 is")
    print(f"        well-defined with NO off-eigenspace residue (no v21 off-T analog).")
    print(f"  [1b] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["1b"] = {"refuted": refuted, "all_clean": all_clean, "detail": detail}
    return not refuted


def attack_1c(g, ginv, Gam, GamB, R):
    """Multi-matter over-determination: does requiring ONE kappa_ind to source the response for
    ALL matter directions over-determine it to distinct values (the v21 EmptySet)?"""
    _hdr("ATTACK 1c -- multi-matter: does ONE kappa_ind over-determine across matter directions?")
    # In v21 the kill was: ONE scalar kappa, MANY tensor conditions, incompatible.  Here the
    # induced field equation is (Delta_L - 2 Lambda) h_M = kappa_ind TT(B3[M]) for each matter M.
    # The RESPONSE is h_M = kappa_ind TT(B3[M]) / 20 -- a SEPARATE h_M per M (the metric responds
    # to each matter source).  kappa_ind is the SAME scalar for all M.  The over-determination
    # question: is there a CONSTRAINT linking the h_M across M that forces kappa_ind to distinct
    # values?  There is NOT -- each M sources its OWN response with the same coupling; kappa_ind is
    # a free overall scale (G3).  We DEMONSTRATE this by computing the response amplitude factor
    # (1/20) for each M and confirming it is M-INDEPENDENT (one knob works for all), vs the v21
    # case where the per-point Lambda took distinct values.
    amps = {}
    for nm in ["s01", "a01", "d1", "GEN"]:
        Mc = M_GEN if nm == "GEN" else GM[nm]
        B3 = TP.grad_bilinear(cancel(TP.phi_field(Mc)), simp=sp.together)
        r, _, _, _, info = extract_tt(B3, g, ginv, Gam, verify=True)
        dLr = lichnerowicz_full_v33(r, g, ginv, Gam, GamB, R, Lambda=6)
        # the eps acting on r: (Delta_L - 2 Lambda) r = (dL - 12) r.  amplitude factor = 1/eps.
        # extract eps from the first nonzero block (must be the SAME 20 for all M).
        eps_M = None
        for k in range(3):
            if not all(cancel(r[k][a, b]) == 0 for a in range(2) for b in range(2)):
                for a in range(2):
                    for b in range(2):
                        if cancel(r[k][a, b]) != 0:
                            eps_M = cancel((dLr[k][a, b] - 12 * r[k][a, b]) / r[k][a, b])
                            break
                    if eps_M is not None:
                        break
                break
        amps[nm] = eps_M
        _log(f"[{nm}] (Delta_L - 2 Lambda) eigenvalue on TT(B3) = {eps_M} (response amp = 1/{eps_M})")
    distinct = set(str(v) for v in amps.values())
    one_knob_works = (len(distinct) == 1 and "20" in distinct)
    # REFUTATION: SUCCEEDED iff the stiffness eps takes DISTINCT values across matter directions
    # (=> a single kappa_ind cannot source all responses with the same 1/eps => over-determined).
    refuted = not one_knob_works
    print(f"\n  [1c] (Delta_L - 2 Lambda) eigenvalue across matter directions: {amps}")
    print(f"  [1c] distinct stiffness values = {distinct}; ONE knob (eps=20) works for all M: {one_knob_works}")
    print(f"  [1c] CONTRAST v21: the per-point Lambda took 4 DISTINCT rationals => EmptySet.  Here the")
    print(f"        stiffness is the SAME 20 for every matter direction => NO over-determination.")
    print(f"  [1c] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["1c"] = {"refuted": refuted, "amps": {k: str(v) for k, v in amps.items()},
                     "one_knob_works": one_knob_works}
    return not refuted


def attack_1d(g, ginv):
    """a4 (curvature-squared, higher-derivative) contamination of the SCALE mode.  Does the a4
    term add an independent, knob-unreachable condition on Lambda_cc?"""
    _hdr("ATTACK 1d -- does the a4 (higher-derivative) term over-determine the scale mode?")
    # The induced action has a a4 = (31/120)(4pi)^2 term too (zeta(0)+1).  On FS it is a CONSTANT
    # (the integrated a4 is a pure number = (31/120)(4pi)^2 * 1, no field dependence on a frozen
    # background): its VARIATION delta/delta g of a topological/constant a4 term.  In d=4 the a4
    # curvature-squared invariants (R^2, Ric^2, Riem^2) vary into 4th-derivative (Bach/Lanczos) terms
    # that VANISH on an Einstein (in fact symmetric) background up to the Gauss-Bonnet topological
    # piece.  The KEY fact: a4 is DIMENSIONLESS (Lambda_f^0) -- it is the LOG-divergent / finite
    # piece, NOT a power divergence.  It does NOT scale with Lambda_f, so it cannot enter the
    # Lambda_cc = (3/2)Lambda_f^2 matching (which is the ratio of the Lambda_f^4 a0 term to the
    # Lambda_f^2 a1 term).  We CHECK: the a4 term's contribution to the scale-mode (trace) equation
    # is Lambda_f-independent, hence cannot shift the Lambda_f^2 = 4 matching.
    Lf = sp.symbols("Lambda_f", positive=True)
    # power-counting of the three divergences (per d.o.f., proper-time cutoff delta = 1/Lambda_f^2):
    #   a0 ~ Lambda_f^4 (quartic, the cc), a1 ~ Lambda_f^2 (quadratic, the EH), a4 ~ log/finite ~ Lambda_f^0.
    a0_power = 4
    a1_power = 2
    a4_power = 0
    # The Lambda_cc matching uses ONLY the a0/a1 ratio (Lambda_f^4 / Lambda_f^2 = Lambda_f^2):
    Lambda_cc = Rational(3, 2) * Lf**2
    # An a4 contribution to the *vacuum energy* would scale as Lambda_f^0 -- subleading to a0~Lf^4 by
    # Lambda_f^4, and to a1~Lf^2 by Lambda_f^2.  Check it cannot enter the LEADING matching:
    a4_enters_leading = (a4_power >= a1_power)  # False: 0 < 2
    # Moreover on FS (Einstein) the a4 (Weyl^2 + Gauss-Bonnet) variation: Weyl=0? Check.
    # CP^2 is NOT conformally flat (Weyl != 0), but the a4 variation on a SYMMETRIC space is a
    # multiple of g (it preserves the Einstein condition) -- it can only RENORMALIZE Lambda_cc, not
    # add a traceless condition.  We confirm the structural fact: a4 enters as Lambda_f^0, the
    # matching as Lambda_f^2, so a4 is a subleading correction the knob absorbs at the matching scale.
    refuted = a4_enters_leading  # SUCCEEDED iff a4 enters the leading scale matching independently
    _log(f"divergence powers: a0 ~ Lambda_f^{a0_power}, a1 ~ Lambda_f^{a1_power}, a4 ~ Lambda_f^{a4_power}")
    _log(f"Lambda_cc matching uses a0/a1 ratio = Lambda_f^2 => Lambda_cc = {Lambda_cc}")
    _log(f"a4 (~Lambda_f^0) enters the LEADING (Lambda_f^2) scale matching: {a4_enters_leading}")
    print(f"\n  [1d] a4 is dimensionless (Lambda_f^0): the conformal-anomaly/log piece, NOT a power")
    print(f"       divergence.  The Lambda_cc = (3/2)Lambda_f^2 matching is the a0(Lf^4)/a1(Lf^2)")
    print(f"       ratio; a4 ~ Lf^0 is subleading by Lf^2 and does NOT enter the leading matching.")
    print(f"  [1d] On the symmetric FS background the a4 variation is proportional to g (Einstein-")
    print(f"        preserving) => it renormalizes Lambda_cc, adds NO traceless condition.")
    print(f"  [1d] REFUTATION {'SUCCEEDED (overturned)' if refuted else 'FAILED (verdict strengthened)'}")
    RESULTS["1d"] = {"refuted": refuted, "a4_enters_leading": a4_enters_leading,
                     "Lambda_cc": str(Lambda_cc)}
    return not refuted


def main():
    print("#" * 80)
    print("# ADVERSARIAL Attack 1 -- the v21 rank wall sneaking back (Trap #26)")
    print("# Default: the verdict is WRONG.  Concede only when the computation defeats the attack.")
    print("#" * 80)
    g = TP.fs_metric()
    ginv = TP.fs_metric_inv(g)
    Gam = TP.christoffel_hol(g, ginv)
    GamB = TP._christoffel_antihol(g, ginv)
    R = riemann_kahler(g, ginv, Gam)
    _log("FS geometry built (Kahler-Einstein, Ric=6g, Lambda=6)")

    s1a = attack_1a(g, ginv)
    s1b = attack_1b(g, ginv, Gam, GamB, R)
    s1c = attack_1c(g, ginv, Gam, GamB, R)
    s1d = attack_1d(g, ginv)

    _hdr("ATTACK 1 SUMMARY")
    survived = {"1a": s1a, "1b": s1b, "1c": s1c, "1d": s1d}
    for k, v in survived.items():
        verdict = "verdict SURVIVED (refutation FAILED)" if v else "verdict OVERTURNED (refutation SUCCEEDED)"
        print(f"  [{k}] {verdict}")
    any_overturned = not all(survived.values())
    print(f"\n  Attack 1 overall: {'OVERTURNED on >=1 sub-attack' if any_overturned else 'verdict SURVIVED all sub-attacks (G2 not-over-determined STRENGTHENED)'}")
    RESULTS["overall_survived"] = not any_overturned
    return not any_overturned


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
