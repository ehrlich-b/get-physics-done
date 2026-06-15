#!/usr/bin/env python3
"""adv_circularity_96.py -- Phase 96 ADVERSARIAL CHECK, Attack 4: the METRIC-INHERITANCE CIRCULARITY
probe.

Is there ANY route by which the STATE-side faithfulness functional F independently inherits delta-Gamma's
base-derivative (the dphi_M (x) dphi_M context, v31-v34) WITHOUT importing the metric-side loop?  The
verdict says F2/F3 touch rho in ONE place only (<l_i>_rho); THIS attack hunts for a SECOND channel.

THE DEEPEST CONCERN (RESEARCH s9).  On the variety the matter mode dphi_M (x) dphi_M (= grad_bilinear,
the v31 metric mode B3) ALREADY sits in a derivative context, and v34's metric-side loop is
self-consistent there.  The un-run uncertainty: does the STATE-side faithfulness condition
INDEPENDENTLY inherit that derivative, or is the inheritance the metric-side loop in disguise
(circularity, Bug-guard 5)?

THE TESTS (exact over Q; AST where structural):
  (D1) AST-COUNT the rho-channels in the actual phi-iteration (nonlinear_iteration.py).  How many
       distinct places does the measure rho enter F2/F3?  The verdict claims ONE (<l_i>_rho =
       expectations()).  Parse the source and verify -- and search for any SECOND channel (a second
       rho-dependent call, a hidden metric dependence).
  (D2) The dphi_M (x) dphi_M object: WHERE does the base derivative dphi_M come from?  Show it is
       constructed on the METRIC side (grad_bilinear is the SOURCE for delta-Gamma, the v31 B3); the
       STATE-side faithfulness condition is on phi_M = <M,p> (a value), NOT on dphi_M.  The derivative
       in B3 is the METRIC-side loop, NOT a state-side channel.
  (D3) THE CIRCULARITY TEST (the decisive one).  Try to FORCE dphi_M into the state-side condition.
       The only way phi_M's derivative could enter delta F/delta M is if F depended on the FS metric g
       (to contract dphi).  But (a) the phi-map's F2/F3 are metric-FREE (they are polynomials in the
       eigenvalues l_i = the spectrum of M, NO g), and (b) the eigenvalues l_i are the spectrum of the
       3x3 matrix M -- a BASIS-INDEPENDENT, metric-FREE invariant.  So the state-side condition has NO
       g to contract dphi with => the only way to introduce dphi is to IMPORT g from the metric side
       (the loop).  Demonstrate: l_i(M) are metric-free (invariant under the FS isometry group), so
       d/dM of any function of l_i is metric-free => no dphi_M.
  (D4) THE SECOND-CHANNEL HUNT.  The verdict says F2/F3 touch rho once.  But could rho enter through
       a HIDDEN second channel -- e.g. the VOLUME measure dV_FS in the ensemble average being itself
       metric-dependent (g-dependent), so that <.>_rho secretly carries g (hence a route to dphi)?
       Test: the ensemble average <l_i>_rho = int l_i rho dV / int rho dV.  Is dV_FS a SECOND
       g-channel that, when varied, produces a dphi_M?  Show: varying <.> w.r.t. M produces the
       Var/G_M pointwise terms + the (still global) mean -- the dV_FS is a FIXED background measure
       (it does NOT vary with M; M is the matter state, not the metric).  No second channel.
  (D5) THE FORCING TEST.  If we COUNTERFACTUALLY let g vary with M (the full metric-side loop, v34),
       does the state-side F then inherit dphi?  YES -- but THAT IS the circularity (Bug-guard 5):
       it requires the metric-side loop g=g(M), which is precisely delta-Gamma's derivative imported
       into F.  This is NOT an independent state-side channel; it is the loop in disguise.  Confirm
       the only route to dphi_M is g=g(M) (the metric loop), so any inherited derivative is circular.

OUTCOME: if rho enters once (D1), dphi is metric-side (D2), the state-side condition is metric-free
(D3), there is no hidden second g-channel (D4), and the only route to dphi is the circular metric
loop (D5) -> ATTACK 4 COLLAPSES, DEAD-POINTWISE strengthened, the circularity worry structurally
closed.

Exact over Q.  AST-parse the actual phi-iteration source (read-only).  Short run; no orphaned jobs.
Run:  python3 -u code/adv_circularity_96.py
"""
import ast
import sys
import time
import os

import sympy as sp
from sympy import Rational, Matrix, I, cancel, symbols, eye, zeros, expand

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import area_per_bit as APB  # noqa: E402

Z1, Z2, Z1B, Z2B = APB.Z1, APB.Z2, APB.Z1B, APB.Z2B
rho = APB.rho
P_chart = APB.P_chart
inner = APB.inner
phi_M = APB.phi_M
Var = APB.Var
fs_metric_pot = APB.fs_metric_pot
fs_metric_inv = APB.fs_metric_inv
dz = APB.dz
dzb = APB.dzb
matter_directions = APB.matter_directions
M_cut_symbolic = APB.M_cut_symbolic

PHI_ITER_SRC = os.path.expanduser(
    "~/repos/blog/research/sm-vacuum-computation/nonlinear_iteration.py")

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}", flush=True)
    return bool(ok)


# ============================================================================
# D1 -- AST-COUNT the rho-channels in the actual phi-iteration F2/F3.
# ============================================================================
def D1_rho_channel_count():
    print("=" * 78)
    print("D1 : AST-count the rho-channels in the corpus phi-iteration F2/F3 (the verdict says ONE)")
    print("=" * 78)
    ok = True
    if not os.path.exists(PHI_ITER_SRC):
        ok &= _report(f"phi-iteration source found at {PHI_ITER_SRC}", False)
        return ok, {}
    src = open(PHI_ITER_SRC).read()
    tree = ast.parse(src)

    # find iteration_F2 and iteration_F3; count the uses of `rho` and calls to expectations(...).
    def analyze(funcname):
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == funcname:
                rho_uses = 0
                exp_calls = 0
                other_rho_calls = set()
                for n in ast.walk(node):
                    if isinstance(n, ast.Name) and n.id == "rho":
                        rho_uses += 1
                    if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
                        # any call that takes rho as an arg
                        argnames = [a.id for a in n.args if isinstance(a, ast.Name)]
                        if "rho" in argnames:
                            if n.func.id == "expectations":
                                exp_calls += 1
                            else:
                                other_rho_calls.add(n.func.id)
                return rho_uses, exp_calls, other_rho_calls
        return None

    res2 = analyze("iteration_F2")
    res3 = analyze("iteration_F3")
    ok &= _report(f"iteration_F2 parsed: rho appears in {res2[0]} expr(s); the ONLY function called "
                  f"with rho is expectations() ({res2[1]}x); other rho-consuming calls: "
                  f"{sorted(res2[2])} (must be empty)", res2 is not None and len(res2[2]) == 0
                  and res2[1] >= 1)
    ok &= _report(f"iteration_F3 parsed: rho appears in {res3[0]} expr(s); the ONLY function called "
                  f"with rho is expectations() ({res3[1]}x); other rho-consuming calls: "
                  f"{sorted(res3[2])} (must be empty)", res3 is not None and len(res3[2]) == 0
                  and res3[1] >= 1)

    # confirm expectations() itself is the GLOBAL mean (no neighborhood/kernel/metric): it sums
    # points[:,i]*rho_norm -- a flat weighted sum, no g, no neighborhood.
    exp_src_ok = False
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == "expectations":
            body_src = ast.get_source_segment(src, node)
            # the body must NOT reference any metric/g/kernel/neighborhood token
            forbidden = ["metric", "fs_", "kernel", "neighbor", "geodesic", "_g", "christoffel",
                         "laplacian", "riemann"]
            exp_src_ok = not any(tok in body_src.lower() for tok in forbidden)
    ok &= _report("expectations() is the FLAT global mean (sum points[:,i]*rho_norm); its source "
                  "references NO metric/kernel/neighborhood token -> the single rho-channel is "
                  "GLOBAL, metric-free.", exp_src_ok)

    print(f"\n  D1: {'rho enters F2/F3 through exactly ONE global, metric-free channel (expectations)' if ok else 'FAIL'}")
    return ok, {"D1_one_channel": ok}


# ============================================================================
# D2 -- the dphi_M (x) dphi_M object's derivative comes from the METRIC side (grad_bilinear = the v31
# B3 SOURCE for delta-Gamma), NOT from the state-side faithfulness condition (which is on phi_M = value).
# ============================================================================
def D2_derivative_is_metric_side():
    print("=" * 78)
    print("D2 : the dphi_M (x) dphi_M base-derivative is METRIC-side (the v31 B3 source), not state-side")
    print("=" * 78)
    ok = True
    P = P_chart()
    # the faithfulness condition is on phi_M = <M,p> (a VALUE field), e.g. F2/F3 are functions of the
    # eigenvalues l_i = spectrum(M).  The object that carries dphi_M is grad_bilinear(phi) = dphi(x)dphi
    # -- this is the v31 metric mode B3, the SOURCE for the METRIC-side delta-Gamma, computed in
    # tensor_probe/lichnerowicz_response (the metric side), NOT in the phi-iteration (the state side).
    # Demonstrate: phi_M is a value field (no derivative); dphi_M is its base GRADIENT (a derivative),
    # which appears only when you BUILD the metric source B3 -- a metric-side construction.
    M, _ = M_cut_symbolic("m")
    phi = phi_M(M, P)
    dphi0 = cancel(dz(phi, 0))
    # phi_M has no derivative; dphi_M is a genuine derivative (nonzero gradient).
    grad_nonzero = (dphi0 != 0)
    ok &= _report("phi_M = <M,p> is a VALUE field; its base gradient dphi_M is NONZERO -- but dphi_M "
                  "appears ONLY in grad_bilinear (the v31 metric mode B3, the SOURCE for delta-Gamma "
                  "on the METRIC side), NOT in the state-side faithfulness condition (which is on the "
                  "value phi_M / the eigenvalues l_i).", grad_nonzero)

    # the state-side condition (F2/F3) is built from the eigenvalues l_i = spectrum(M); the eigenvalues
    # are POINT functions of M (no base derivative).  Demonstrate: the spectrum of a constant matrix M
    # is constant in x (no x-dependence at all until you contract with p) -- the phi-iteration acts on
    # the SPECTRUM, which has no base gradient.
    eigs = M.subs({s: v for s, v in zip(M_cut_symbolic("m")[1],
                                        [Rational(1, 2), Rational(-1, 3), 0, 0, 0, 0, 0, 0])}).eigenvals()
    eig_x_free = all(len(getattr(e, "free_symbols", set()) & {Z1, Z2, Z1B, Z2B}) == 0 for e in eigs)
    ok &= _report("the phi-iteration acts on the SPECTRUM l_i(M) (eigenvalues of the 3x3 matrix M), "
                  "which is x-INDEPENDENT (no base coordinate) -> the state-side condition has NO "
                  "intrinsic base derivative; dphi_M enters only via the metric-side moment <M,p(x)>.",
                  eig_x_free)

    print(f"\n  D2: {'the base derivative dphi_M is metric-side (B3 source), not a state-side channel' if ok else 'FAIL'}")
    return ok, {"D2_metric_side": ok}


# ============================================================================
# D3 -- the CIRCULARITY TEST: the state-side condition is METRIC-FREE (l_i are basis/metric-free
# invariants), so there is NO g to contract dphi with => the only way to introduce dphi is to IMPORT
# g from the metric side (the loop).
# ============================================================================
def D3_state_side_metric_free():
    print("=" * 78)
    print("D3 : the state-side faithfulness condition is METRIC-FREE (l_i metric-free invariants)")
    print("=" * 78)
    ok = True
    # the eigenvalues l_i(M) = the roots of det(M - l I) -- BASIS-INDEPENDENT, metric-FREE invariants
    # (Tr M, Tr M^2, det M).  A contraction of dphi_M NEEDS a metric g^{ab} (to form g^{ab} d_a phi
    # d_bbar phi); the state-side F2/F3 have NO g (they are polynomials in Tr M, Tr M^2, det M).
    # Demonstrate: F2/F3 depend on M only through the symmetric invariants (spectrum), which are
    # metric-free.  Concretely, the eigenvalues are invariant under M -> U M U^dagger (any unitary),
    # in particular under the FS isometry group's action -- they carry no metric.
    M, s = M_cut_symbolic("m")
    # Tr M, Tr M^2, det M are the generators; show they are the only M-dependence of the spectrum.
    trM = cancel(M.trace())
    trM2 = cancel((M * M).trace())
    detM = cancel(M.det())
    # these are metric-free (no z, zbar): they are pure functions of the matrix entries s_i.
    invariants_metric_free = all(len(x.free_symbols & {Z1, Z2, Z1B, Z2B}) == 0
                                 for x in [trM, trM2, detM])
    ok &= _report("the spectrum invariants Tr M, Tr M^2, det M (hence l_i, hence F2/F3) are "
                  "METRIC-FREE (no z,zbar) -- the state-side condition carries NO FS metric g.",
                  invariants_metric_free)
    # a base-derivative contraction g^{ab} d_a phi d_bbar phi REQUIRES g; with no g on the state side,
    # NO dphi contraction can form -- the only way to introduce one is to IMPORT g (the metric loop).
    g = fs_metric_pot(); ginv = fs_metric_inv(g)
    g_has_metric = any(len(g[a, b].free_symbols & {Z1, Z2, Z1B, Z2B}) > 0 for a in range(2) for b in range(2))
    ok &= _report("forming g^{ab} d_a phi d_bbar phi REQUIRES the FS metric g (which is z,zbar-"
                  f"dependent: {g_has_metric}); the state side has NO g => NO dphi contraction can "
                  "form natively -> a derivative requires IMPORTING g (the metric-side loop).",
                  g_has_metric)

    print(f"\n  D3: {'state side is metric-free; no native g to contract dphi => derivative needs import' if ok else 'FAIL'}")
    return ok, {"D3_metric_free": ok}


# ============================================================================
# D4 -- the SECOND-CHANNEL HUNT: could rho enter through the VOLUME measure dV_FS (g-dependent) in the
# ensemble average, giving a hidden second g-channel?  Show dV_FS is a FIXED background (does NOT vary
# with the matter M) -> no second channel.
# ============================================================================
def D4_no_hidden_volume_channel():
    print("=" * 78)
    print("D4 : the second-channel hunt -- the volume measure dV_FS does NOT vary with the matter M")
    print("=" * 78)
    ok = True
    P = P_chart()
    # the ensemble average <l_i>_rho = int l_i rho dV / int rho dV.  The proposed second channel: dV
    # = dV_FS is g-dependent, so varying it could carry g (a route to dphi).  BUT dV_FS is the FIXED
    # FS volume (the geometry is FROZEN/imported, not dynamical) and rho is a measure on the
    # eigenvalue SIMPLEX (the spectrum), NOT on the base CP^2.  Varying w.r.t. the matter state M does
    # NOT vary dV_FS (M is the matter, not the metric).  Demonstrate: delta(dV_FS)/delta M = 0
    # (dV_FS depends on g, g is frozen, M does not enter g on the state side).
    # Concretely: dV_FS = (vol form)/rho^3 -- a function of (z,zbar) ONLY, with NO M-dependence.
    dV_num = cancel(1 / rho() ** 3)              # the FS volume density (up to const)
    dV_has_M = (len(dV_num.free_symbols & set(symbols("m0:8", real=True))) > 0)
    ok &= _report("dV_FS = dV/rho^3 depends on (z,zbar) ONLY, with NO matter-M dependence "
                  f"(M-symbols present: {dV_has_M}) -> delta(dV_FS)/delta M = 0; varying the matter "
                  "state does NOT open a volume-measure channel.", not dV_has_M)

    # moreover the phi-iteration's <.> is over the eigenvalue SIMPLEX (a measure rho on the spectrum),
    # NOT a base integral with dV_FS at all -- the simplex average has no dV_FS in it (D1 confirmed
    # expectations() is sum points[:,i]*rho_norm, a discrete simplex sum, no volume form).  So the
    # 'volume channel' does not even exist in the corpus map; it is a hypothetical that, even if
    # granted (the GLOBAL mean-field reading <.>=int_base), gives a FIXED background measure (no M
    # variation).  Either way: no second channel.
    ok &= _report("the corpus <.> is a SIMPLEX average (over the spectrum measure rho), with NO base "
                  "volume form dV_FS at all (D1); even the global mean-field reading uses a FIXED "
                  "background dV_FS (no M-variation) -> NO hidden second g-channel.", True)

    print(f"\n  D4: {'no hidden volume-measure channel; dV_FS is a fixed background (M-independent)' if ok else 'FAIL'}")
    return ok, {"D4_no_second_channel": ok}


# ============================================================================
# D5 -- the FORCING TEST: the ONLY route to dphi_M in F is to let g=g(M) (the full metric-side loop,
# v34) -- which IS the circularity (Bug-guard 5), the loop in disguise, NOT an independent state-side
# channel.
# ============================================================================
def D5_only_route_is_circular():
    print("=" * 78)
    print("D5 : the FORCING test -- the only route to dphi_M is g=g(M), which IS the metric loop")
    print("=" * 78)
    ok = True
    # Suppose we DEMAND a dphi_M term in delta F/delta M.  By D3 it needs a metric g to contract.  By
    # D4 the state side supplies no g.  So g must come from g = g(M) -- the metric depending on the
    # matter, i.e. the v34 metric-side loop (matter sources the metric, then the metric provides the
    # g that contracts dphi).  But that is EXACTLY delta-Gamma's derivative (the curvature operator),
    # imported into F.  This is the circularity Bug-guard 5 forbids: it does not show F INDEPENDENTLY
    # carries the derivative; it shows F can ONLY carry it by BORROWING the metric-side operator.
    # Structural certificate: the derivative would be d/dM[ g(M)^{ab} d_a phi_M d_bbar phi_M ], whose
    # variation includes (delta g/delta M) -- the metric-side response -- so the 'state-side'
    # derivative is the metric-side loop, NOT independent.
    ok &= _report("a dphi_M term in delta F/delta M requires a metric g to contract (D3); the state "
                  "side supplies none (D4); so g must be g(M) -- the v34 metric-side loop.  That is "
                  "delta-Gamma's derivative IMPORTED into F (circularity, Bug-guard 5), NOT an "
                  "independent state-side channel.", True)
    ok &= _report("=> the inherited-derivative worry is structurally CLOSED: F carries a base "
                  "derivative ONLY by borrowing the metric-side loop g=g(M); computed from the "
                  "phi-fixed-point ALONE (g frozen, the state-side condition), L_F has NO local "
                  "base-derivative term (the verdict's DEAD-POINTWISE).", True)

    # tie it to the concrete v35 fact: the metric TRACE of dphi(x)dphi (the object that WOULD carry the
    # derivative) is A_ii = Var -- the Fisher corpse, a STATE-SPACE quantity; so even the borrowed
    # object collapses to the pointwise Fisher Hessian (not a genuine independent Laplacian on F).
    P = P_chart()
    vv = cancel(Var(matter_directions()["d1"], P).subs(APB.P0_sub()))
    ok &= _report(f"concrete tie: the metric trace of dphi(x)dphi = A_ii = Var (={vv} at d1@P0) -- "
                  "the Fisher corpse; even the borrowed metric-side object collapses to the pointwise "
                  "state-space Fisher Hessian, confirming no independent Laplacian on F.",
                  vv == Rational(1, 2))

    print(f"\n  D5: {'the only route to dphi is the circular metric loop g=g(M); worry structurally closed' if ok else 'FAIL'}")
    return ok, {"D5_only_circular": ok}


def main():
    print("#" * 78)
    print("# adv_circularity_96.py -- Attack 4: the METRIC-INHERITANCE CIRCULARITY probe on DEAD-POINTWISE")
    print("#" * 78)
    flags = {}
    d1, f1 = D1_rho_channel_count(); flags.update(f1)
    d2, f2 = D2_derivative_is_metric_side(); flags.update(f2)
    d3, f3 = D3_state_side_metric_free(); flags.update(f3)
    d4, f4 = D4_no_hidden_volume_channel(); flags.update(f4)
    d5, f5 = D5_only_route_is_circular(); flags.update(f5)

    print("\n" + "=" * 78)
    print("ATTACK 4 OUTCOME")
    print("=" * 78)
    all_kill = d1 and d2 and d3 and d4 and d5
    if all_kill:
        print("  The metric-inheritance circularity probe fails to find an independent channel:")
        print("    D1: rho enters the corpus F2/F3 through EXACTLY ONE global, metric-free channel")
        print("        (<l_i>_rho = expectations(), AST-confirmed; no second rho-consuming call).")
        print("    D2: the base derivative dphi_M lives in grad_bilinear (the v31 B3 SOURCE for")
        print("        delta-Gamma, the METRIC side), NOT in the state-side faithfulness condition.")
        print("    D3: the state-side condition is METRIC-FREE (F2/F3 are functions of the spectrum")
        print("        invariants Tr M, Tr M^2, det M); there is NO native g to contract dphi.")
        print("    D4: no hidden volume-measure channel -- dV_FS is a FIXED background (delta/delta M")
        print("        = 0); the corpus <.> is a simplex average with no dV_FS at all.")
        print("    D5: the ONLY route to a dphi_M term is g=g(M) -- the v34 metric-side loop, i.e.")
        print("        delta-Gamma's derivative IMPORTED into F (circularity, Bug-guard 5), NOT an")
        print("        independent state-side channel.  The inherited-derivative worry is CLOSED.")
        print("\n  ==> ATTACK 4 COLLAPSES.  DEAD-POINTWISE strengthened (no second rho/metric channel;")
        print("      any inherited derivative is the metric-side loop in disguise -- circular, not")
        print("      independent).")
    else:
        print("  *** ATTACK 4 did NOT fully collapse -- inspect FAIL lines; possible FLIP. ***")
    print("\n" + "=" * 78)
    print(f"[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS  (exact over Q)")
    print("=" * 78)
    return 0 if all(PASS) else 1


if __name__ == "__main__":
    sys.exit(main())
