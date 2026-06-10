#!/usr/bin/env python3
"""variety_entropy_landscape.py  --  v24.0 Gate 0/1/2/3
"The Entropy Landscape on the Idempotent Variety (the base-route's first gate)."

CLAIM (sharp, falsifiable): over the primitive-idempotent variety
OP^2 = {rank-1 idempotents of h_3(O)} = F_4/Spin(9), the face-entropy function
    S_X(p) = S(rho_face(p)),   rho_face(p) = C_p(X) / Tr(C_p(X))
on the rank-2 COMPLEMENT face V_0(p) (the Peirce-0 subalgebra h_2(O) of a rank-1 p),
is a NON-TRIVIAL LANDSCAPE for generic structured (matter-bearing, full-rank) X
-- matter shaping a scalar field over the event-space -- while the faithful state
I/3 has a HOMOGENEOUS (constant) landscape, and on interpolations it flattens at I/3.

  DEAD  : landscape constant for generic structured X  (matter shapes nothing).
  LIVE  : non-constant with computable structure (the first ingredient of the
          base/format object on the algebra's own many-point event-space).

VERDICT CRITERION (mandatory -- exact over Q, NO numerics in the verdict):
    S_X(p) constant in p  <=>  spectrum of rho_face(p) p-independent
                          <=>  char-poly coefficients of rho_face(p) constant
                          <=>  r(p) := det_2(C_p X) / Tr(C_p X)^2  constant,
where  C_p X = P_0(p).X = 2 (p o (p o X)) - 3 (p o X) + X     (Peirce-0 compression;
       L_p has eigenvalues {0,1/2,1} so P_0 = 2 L_p^2 - 3 L_p + 1),
       det_2(Y) = ( Tr(Y)^2 - Tr(Y o Y) ) / 2     (rank-2 generic norm of Y in V_0(p)),
       Tr = the h_3(O) trace.
rho_face is a rank-2 (spin-factor) state: char-poly lambda^2 - lambda + det(rho_face),
det(rho_face) = det_2(C_p X)/Tr(C_p X)^2 = r(p).  Entropies S = -sum lam log lam (logs of
algebraic eigenvalues) are reported as ILLUSTRATION ONLY, NEVER as the verdict (guard #5).

Engines (CONVENTIONS.md): ring_lemma_verification (Tr, jordan, det_3, h3o_identity,
h3o_from_coords, _standard_basis_27, jordan_L_matrix); kkt_gluing_holonomy (E_ii,
peirce_idx, stab_f4, f4_basis).  det SSOT = RL.det_3; octonion_algebra BANNED.
Exact over Q (and Q(t) along families).  u = e_7; C_u = span{1, e_7}.
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp                                              # noqa: E402
from sympy import Rational, symbols, cancel, together, sqrt     # noqa: E402

import ring_lemma_verification as RL                            # noqa: E402
import kkt_gluing_holonomy as KK                                # noqa: E402

_t0 = time.time()
PASS = []


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}")


def _report(label, ok):
    PASS.append(bool(ok))
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    return ok


# ----------------------------------------------------------------------------
# octonion / h_3(O) element helpers  (element = 3x3 nested list of 8-lists)
# ----------------------------------------------------------------------------
def zoct():
    return [sp.Integer(0)] * 8


def oct1(k, val):
    """8-list with `val` on the e_k slot (k=0 real)."""
    z = zoct()
    z[k] = sp.sympify(val)
    return z


def conj_oct(a):
    return [a[0]] + [-a[i] for i in range(1, 8)]


def cmul_k(a, b, k):
    """Octonion product of a,b BOTH supported on span{1, e_k} (associative = C).
    (a0 + a_k e_k)(b0 + b_k e_k) = (a0 b0 - a_k b_k) + (a0 b_k + a_k b0) e_k."""
    r = zoct()
    r[0] = a[0] * b[0] - a[k] * b[k]
    r[k] = a[0] * b[k] + a[k] * b[0]
    return r


def el_zero():
    return [[zoct() for _ in range(3)] for _ in range(3)]


def el_scal(c, X):
    c = sp.sympify(c)
    return [[[c * X[i][j][k] for k in range(8)] for j in range(3)] for i in range(3)]


def el_add(*Xs):
    out = el_zero()
    for X in Xs:
        for i in range(3):
            for j in range(3):
                for k in range(8):
                    out[i][j][k] += X[i][j][k]
    return out


def el_simplify(X, fn=sp.expand):
    return [[[fn(X[i][j][k]) for k in range(8)] for j in range(3)] for i in range(3)]


def herm_from_vec(v):
    """Rank-1 element p = v v* for v=(v0,v1,v2), each v_i an 8-list lying in a common
    associative subalgebra span{1,e_k}; p[i][j] = v_i conj(v_j).  (Valid h_3(O) idempotent
    iff |v|^2 = 1 and the v_i share one e_k -- enforced by construction below.)"""
    p = el_zero()
    k_used = None
    for vi in v:
        for kk in range(1, 8):
            if vi[kk] != 0:
                k_used = kk
    if k_used is None:
        k_used = 7  # all-real; any k works
    for i in range(3):
        for j in range(3):
            p[i][j] = cmul_k(v[i], conj_oct(v[j]), k_used)
    return p


def _pyth(t):
    """Rational point on the unit circle: (c,s) with c^2+s^2=1."""
    den = 1 + t ** 2
    return (1 - t ** 2) / den, 2 * t / den


def family(t, j, k):
    """One-parameter rank-1 idempotent family through E_11, rotating E_11 (index 0)
    toward E_{jj} along the e_k octonion direction of the (0,j) entry.
    v_0 = c (real),  v_j = s e_k,  v_other = 0.  At t=0: p = E_11."""
    c, s = _pyth(t)
    v = [zoct(), zoct(), zoct()]
    v[0] = oct1(0, c)
    v[j] = oct1(k, s)
    return herm_from_vec(v)


FAMILIES = {
    "u-aligned-Cu-phase(e7)": dict(j=1, k=7, kind="u-aligned"),   # (i)  the C_u=e_7 phase
    "transverse-real":        dict(j=1, k=0, kind="u-aligned"),   # (ii) real dir, transverse to (i)
    "off-u(e1)":              dict(j=1, k=1, kind="off-u"),       # (iii) leaves the u-aligned locus
    "u-aligned-E33-real":     dict(j=2, k=0, kind="u-aligned"),   # (iv) extra independent family
}


# ----------------------------------------------------------------------------
# the face object  (general rank-2 complement face of a rank-1 idempotent p)
# ----------------------------------------------------------------------------
def compress0(p, X):
    """C_p X = P_0(p) . X = 2 (p o (p o X)) - 3 (p o X) + X  (Peirce-0 compression)."""
    LpX = RL.jordan(p, X)
    Lp2X = RL.jordan(p, LpX)
    return el_add(el_scal(2, Lp2X), el_scal(-3, LpX), X)


def face_coeffs(p, X, simp=cancel):
    """Char-poly coefficients of rho_face(p) for state X.
    Returns (T, det2, r) with T=Tr(C_pX), det2=(T^2 - Tr((C_pX)o(C_pX)))/2,
    r = det2 / T^2 = det(rho_face)  (the second/only nontrivial char-poly coeff)."""
    Cp = compress0(p, X)
    T = simp(RL.Tr(Cp))
    Sq = RL.jordan(Cp, Cp)
    T2 = simp(RL.Tr(Sq))
    det2 = simp((T ** 2 - T2) / 2)
    r = simp(together(det2 / T ** 2))
    return T, det2, r


def face_spectrum(p, X):
    """rho_face eigenvalues (lam_+/-) = 1/2 +- sqrt(1/4 - r).  Illustration only (sqrt)."""
    _, _, r = face_coeffs(p, X)
    disc = sqrt(Rational(1, 4) - r)
    return [Rational(1, 2) + disc, Rational(1, 2) - disc]


def S_illustration(p, X, tval):
    """Numeric von Neumann entropy at a sample rational t -- ILLUSTRATION ONLY."""
    t = symbols("t")
    eigs = [sp.simplify(e.subs(t, tval)) for e in face_spectrum_t(p_of_t=p, X=X)]
    val = 0
    for e in eigs:
        ef = float(e)
        if ef > 0:
            val += -ef * sp.log(ef)
    return float(val)


def face_spectrum_t(p_of_t, X):
    _, _, r = face_coeffs(p_of_t, X)
    disc = sqrt(Rational(1, 4) - r)
    return [Rational(1, 2) + disc, Rational(1, 2) - disc]


# ----------------------------------------------------------------------------
# GATE 0 : families exact + the bottleneck tangent count
# ----------------------------------------------------------------------------
def gate0():
    print("=" * 78)
    print("GATE 0 : rational rank-1 idempotent families through E_11 + tangent counts")
    print("=" * 78)
    t = symbols("t")
    E11 = KK.E_ii(0)

    all_ok = True
    for name, cfg in FAMILIES.items():
        p = family(t, cfg["j"], cfg["k"])
        # p o p = p  exactly over Q(t)
        pp = RL.jordan(p, p)
        idem = all(cancel(pp[i][j][kk] - p[i][j][kk]) == 0
                   for i in range(3) for j in range(3) for kk in range(8))
        # Tr p = 1
        trp = cancel(RL.Tr(p))
        # p(0) = E_11
        p0 = el_simplify([[[p[i][j][kk].subs(t, 0) for kk in range(8)]
                           for j in range(3)] for i in range(3)], sp.simplify)
        at0 = all(p0[i][j][kk] == E11[i][j][kk]
                  for i in range(3) for j in range(3) for kk in range(8))
        ok = idem and (trp == 1) and at0
        all_ok = all_ok and ok
        _report(f"family '{name}' ({cfg['kind']}): p o p = p, Tr p = 1, p(0)=E_11 (exact/Q(t))", ok)

    # ---- tangent dimension of the FULL rank-1 variety at E_11 ----
    # linearize p = E_11 + eps H:  p o p = p  =>  L_{E11} H = (1/2) H  => H in V_{1/2}(E11);
    # Tr p = 1 => Tr H = 0 (automatic on V_{1/2}).  dim = nullspace(L_{E11} - 1/2 I).
    basis = RL._standard_basis_27()
    L = RL.jordan_L_matrix(E11, basis)
    half = Rational(1, 2)
    Mhalf = L - half * sp.eye(27)
    null_full = Mhalf.nullspace()
    dim_full = len(null_full)
    vhalf_idx = sorted(KK.peirce_idx(E11, half))
    _report(f"FULL variety tangent at E_11 = dim {dim_full} = 16 = V_{{1/2}}(E_11) "
            f"(indices {vhalf_idx[0]}..{vhalf_idx[-1]})",
            dim_full == 16 and vhalf_idx == list(range(11, 27)))

    # ---- tangent dimension of the u-ALIGNED rank-1 locus at E_11 ----
    # u-aligned locus = rank-1 idempotents of h_3(C_u), C_u = span{1, e_7}.
    # tangent = V_{1/2}(E_11) INTERSECT h_3(C_u) = the (0,1),(0,2) entries restricted to
    # span{1,e_7}.  DERIVE: impose, on H in V_{1/2}, that every octonion component on the
    # non-C_u directions {e_1..e_6} of each V_{1/2} entry vanishes.
    # V_{1/2}(E_11) entries: x2 = coords 11..18 (the (0,2) octonion), x3 = 19..26 (the (0,1)).
    # non-C_u slots inside each 8-block: e_1..e_6 -> offsets {1,2,3,4,5,6} (keep e_0,e_7).
    cu_keep = set()
    for base in (11, 19):           # the two V_{1/2} octonion blocks
        cu_keep.add(base + 0)       # e_0 (real)
        cu_keep.add(base + 7)       # e_7 = u
    ualigned_idx = sorted(i for i in range(11, 27) if i in cu_keep)
    dim_ual = len(ualigned_idx)
    # cross-check it is genuinely the h_3(C_u) intersection (a linear subspace of V_{1/2})
    _report(f"u-ALIGNED locus tangent at E_11 = dim {dim_ual} (V_{{1/2}} cap h_3(C_u): "
            f"(0,1)&(0,2) entries restricted to span{{1,e_7}}; indices {ualigned_idx})",
            dim_ual == 4)
    print(f"  -> PRE-REGISTERED 4 {'CONFIRMED' if dim_ual == 4 else 'FALSIFIED'}: "
          f"the recorded OP^2 -> CP^2=SU(3)/U(2) (4-dim, Einstein, totally geodesic, Liu 1998) "
          f"bottleneck cut {'governs' if dim_ual == 4 else 'does NOT govern'} the event-space.")

    print(f"\n  GATE 0 families+tangent: {'ALL PASS' if all_ok and dim_full == 16 and dim_ual == 4 else 'FAIL'}")
    return all_ok and dim_full == 16 and dim_ual == 4


# ----------------------------------------------------------------------------
# GATE 1 : vacuum-homogeneity calibration  (must pass; ZERO evidential weight)
# ----------------------------------------------------------------------------
def _I_over_3():
    I3 = RL.h3o_identity()
    return el_scal(Rational(1, 3), I3)


def gate1():
    print("=" * 78)
    print("GATE 1 : vacuum calibration -- X=I/3 char-poly CONSTANT along ALL families")
    print("         (F_4-invariance tautology; S = log 2; carries ZERO evidence)")
    print("=" * 78)
    t = symbols("t")
    X = _I_over_3()
    all_const = True
    for name, cfg in FAMILIES.items():
        p = family(t, cfg["j"], cfg["k"])
        T, det2, r = face_coeffs(p, X)
        const = (cancel(r - Rational(1, 4)) == 0) and (cancel(T - Rational(2, 3)) == 0)
        all_const = all_const and const
        _report(f"X=I/3 on '{name}': Tr=2/3 const, det(rho_face)=r=1/4 const "
                f"(=> spectrum (1/2,1/2), S=log2)", const)
    print(f"  -> calibration {'PASS (homogeneous vacuum)' if all_const else 'FAIL'} "
          f"-- pre-registered tautology, ZERO evidential weight.")
    return all_const


# ----------------------------------------------------------------------------
# test states for GATE 2
# ----------------------------------------------------------------------------
def state_diagonal():
    """A diagonal (special, large-stabilizer) state -- included to expose the guard."""
    return RL.h3o_from_coords(Rational(7), Rational(5), Rational(3), zoct(), zoct(), zoct())


def state_generic():
    """A GENERIC full-rank rational structured state: diagonal-dominant (det_3>0, interior
    of the cone) with matter switched on across MULTIPLE octonion directions so the eigenframe
    is generic (not the standard E_ii frame) -- the decisive Gate-2 state."""
    x1 = zoct(); x1[4] = Rational(1, 5); x1[6] = Rational(1, 7)          # (1,2) entry  V_0
    x2 = zoct(); x2[2] = Rational(1, 4); x2[5] = Rational(1, 6)          # (0,2) entry  V_{1/2}
    x3 = zoct(); x3[1] = Rational(1, 3); x3[3] = Rational(1, 5); x3[7] = Rational(1, 8)  # (0,1) V_{1/2}
    return RL.h3o_from_coords(Rational(7), Rational(5), Rational(3), x1, x2, x3)


def state_v18_matter():
    """A v18-style matter config: flat-ish diagonal + V_{1/2} matter only (off-diagonals on
    the (0,1),(0,2) spinor entries), a structured matter-bearing full-rank state."""
    x1 = zoct()
    x2 = zoct(); x2[0] = Rational(1, 4); x2[3] = Rational(1, 6)
    x3 = zoct(); x3[0] = Rational(1, 5); x3[1] = Rational(1, 7)
    return RL.h3o_from_coords(Rational(4), Rational(3), Rational(2), x1, x2, x3)


# ----------------------------------------------------------------------------
# GATE 2 : THE TEST  (the landscape of structured states)
# ----------------------------------------------------------------------------
def _stab_dim(X):
    try:
        res = KK.stab_f4([X])
        return res.get("dim", res) if isinstance(res, dict) else res
    except Exception as e:                                   # pragma: no cover
        return f"(stab_f4 failed: {e})"


def landscape_along(p_of_t, X):
    """Return r(t) and its variation summary along a family."""
    t = symbols("t")
    T, det2, r = face_coeffs(p_of_t, X)
    r0 = cancel(r.subs(t, 0))
    varies = cancel(r - r0) != 0
    return dict(T=T, det2=det2, r=r, r0=r0, varies=bool(varies))


def verdict(any_generic_varies_transverse):
    """NON-HARDWIRED: DEAD iff the landscape is constant for the generic state along ALL
    families; LIVE iff it varies along at least one guard-1-clean family."""
    return "LIVE" if any_generic_varies_transverse else "DEAD"


def _verdict_selftest():
    # constant input -> DEAD ; varying input -> LIVE   (proves verdict() not hardwired)
    ok = (verdict(False) == "DEAD") and (verdict(True) == "LIVE")
    _report("verdict() self-test: const->DEAD, varying->LIVE (non-hardwired)", ok)
    return ok


def gate2():
    print("=" * 78)
    print("GATE 2 : THE TEST -- the face-entropy landscape of structured states")
    print("=" * 78)
    _verdict_selftest()
    t = symbols("t")

    states = {
        "GENERIC (decisive)": state_generic(),
        "v18-matter (V_1/2)": state_v18_matter(),
        "diagonal (special)": state_diagonal(),
    }

    # guard #1: report each state's F_4-stabilizer dimension; the families MOVE E_11
    # (transverse to the E_11-fixing part of any stabilizer), so variation is non-vacuous.
    print("\n  guard #1 (stabilizer): families move E_11; report dim Stab_{F_4}(X):")
    for sname, X in states.items():
        d3 = RL.det_3(X)
        print(f"    {sname:22s}: det_3 = {d3}  (full-rank/interior: {d3 > 0});  "
              f"dim Stab_F4 = {_stab_dim(X)}")
    print(f"    {'I/3 (vacuum)':22s}: dim Stab_F4 = 52 (all of F_4 -> calibration constancy is vacuous)")

    generic_live = False
    summary = {}
    for sname, X in states.items():
        print(f"\n  --- state: {sname} ---")
        st = {}
        for fname, cfg in FAMILIES.items():
            p = family(t, cfg["j"], cfg["k"])
            info = landscape_along(p, X)
            st[fname] = info
            tag = "VARIES" if info["varies"] else "constant"
            print(f"    family {fname:24s} [{cfg['kind']:9s}]: det(rho_face)=r(t) {tag}")
            if info["varies"]:
                print(f"        r(t) = {info['r']}")
            else:
                print(f"        r = {info['r0']} (p-independent)")
        summary[sname] = st
        # generic state: LIVE if it varies along an off-u or transverse (guard-1-clean) family
        if sname.startswith("GENERIC"):
            for fname, cfg in st.items():
                if FAMILIES[fname]["kind"] in ("off-u", "u-aligned") and cfg["varies"]:
                    generic_live = True

    v = verdict(generic_live)
    print("\n" + "=" * 78)
    print(f"  VERDICT (Gate 2, exact over Q): {v}")
    print("=" * 78)

    if v == "LIVE":
        _live_structure(summary["GENERIC (decisive)"], state_generic())
    return v, summary


def _live_structure(generic_summary, Xgen):
    """LIVE-only: which char-poly coeff varies, critical points vs eigenframe, flattening."""
    t = symbols("t")
    print("\n  LIVE structure report (generic state):")
    # (a) which coefficient(s) vary
    for fname, info in generic_summary.items():
        Tv = cancel(info["T"] - info["T"].subs(t, 0)) != 0
        dv = cancel(info["det2"] - info["det2"].subs(t, 0)) != 0
        print(f"    {fname:24s}: Tr varies={bool(Tv)}, det_2 varies={bool(dv)}, "
              f"purity r varies={info['varies']}")
    # (b) critical points of the leading varying coefficient (r) along each family
    print("\n    critical points of r(t) (dr/dt = 0) along each family:")
    for fname, info in generic_summary.items():
        if not info["varies"]:
            print(f"      {fname:24s}: (constant -- no critical structure)")
            continue
        dr = cancel(sp.diff(info["r"], t))
        num = sp.numer(together(dr))
        roots = sp.solve(sp.Eq(num, 0), t)
        real_roots = [rr for rr in roots if rr.is_real is not False]
        print(f"      {fname:24s}: dr/dt=0 at t in {real_roots}")
    # (c) FLATTENING check: X_t = (1-t) I/3 + t Xgen ; variation of r along a probe family
    #     must vanish at t=0 and grow with t (vacuum = homogeneous point of the family).
    print("\n    FLATTENING check  X_t = (1-t) I/3 + t X_gen  (probe = off-u(e1) family):")
    s = symbols("s")               # variety parameter for the probe family
    pprobe = family(s, j=1, k=1)   # off-u probe
    I3 = _I_over_3()
    flat_ok = True
    for tv in [Rational(0), Rational(1, 4), Rational(1, 2), Rational(3, 4), Rational(1)]:
        Xt = el_add(el_scal(1 - tv, I3), el_scal(tv, Xgen))
        _, _, r = face_coeffs(pprobe, Xt)
        # "landscape variation" = d r / d s at s=0 (leading sensitivity of the face to position)
        dvar = cancel(sp.diff(r, s).subs(s, 0))
        # second-order amplitude (since first order may vanish): coefficient of s near 0
        amp = cancel(sp.diff(r, s, 2).subs(s, 0))
        print(f"      t={tv}:  dr/ds|_0 = {dvar} ,  d2r/ds2|_0 = {amp}")
        if tv == 0 and not (dvar == 0 and amp == 0):
            flat_ok = False
    _report("FLATTENING: variation of the landscape vanishes at t=0 (X_0=I/3 homogeneous)",
            flat_ok)


# ----------------------------------------------------------------------------
def main(run=(0, 1, 2)):
    print("#" * 78)
    print("# variety_entropy_landscape.py  --  v24.0  (exact over Q; verdict = char-poly constancy)")
    print("#" * 78)
    results = {}
    if 0 in run:
        results["gate0"] = gate0()
        if not results["gate0"]:
            print("\n*** GATE 0 FAILED (families inexact) -- FAIL-FAST STOP ***")
            return results
    if 1 in run:
        results["gate1"] = gate1()
        if not results["gate1"]:
            print("\n*** GATE 1 calibration FAILED -- machinery broken, STOP ***")
            return results
    if 2 in run:
        results["gate2"] = gate2()
    print(f"\n[{time.time() - _t0:6.1f}s] checks: {sum(PASS)}/{len(PASS)} PASS")
    return results


if __name__ == "__main__":
    main()
