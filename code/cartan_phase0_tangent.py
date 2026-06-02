#!/usr/bin/env python3
# ASSERT_CONVENTION: natural_units=natural, metric_signature=mostly_minus, fourier_convention=NA, coupling_convention=NA, renormalization_scheme=NA, gauge_choice=NA
# ============================================================================
# Phase 74 (v18.0 Cartan/MacDowell-Mansouri) -- Plan 01
# Phase 0: ENGINE RECOVERY + EXACT TANGENT IDENTITY + CALIBRATION
# ============================================================================
#
# Re-certification + calibration driver. EXACT over Q on every decisive path
# (sympy.Matrix.rank/.nullspace only; NEVER numpy/float -- fp-float-decisive).
#
#   DERV-01  re-certify the det SSOT (ring_lemma_verification.py): CH generic
#            norm (LOCK 7a) + 324/324 inner-derivation annihilation = dim f_4 = 52
#            (LOCK 7b); source guard confirms octonion_algebra.py is ABSENT on the
#            decisive path (0 outside-fence imports, 0 float-rank calls).
#   DERV-02  the load-bearing soldering-form fact, NEW code, exact over Q:
#            (a) E_11 o delta = (1/2)delta for a V_{1/2}(E_11) basis (Peirce
#                half-eigenspace);
#            (b) the Zariski tangent of the primitive-idempotent variety {X o X = X}
#                at E_11 (kernel of the 27x27 Jacobian of F(X)=X o X - X) EQUALS
#                V_{1/2}(E_11), dim 16 (Jacobian rank 11; kernel == span{11..26};
#                16 = 17-1 cross-check vs orbit(E_11)=17).
#            Cites Baez 2002 Sec 3.4 (OP^2=F_4/Spin(9), T_E OP^2=V_{1/2}) and
#            McCrimmon (E o delta=(1/2)delta) -- these standard facts are NOT
#            re-derived; the deliverable is the EXACT-over-Q machine verification.
#   VALD-01  reproduce the v17.0 calibration anchors across THREE engines (the
#            anchors are SPLIT across engines, not in one):
#              orbit_dimension_gate.py    -> single-copy 24 / Spin(8)=28 / trdeg 3
#              bulk_geometry_verification -> e_6=78=52+26; orbit(E_11)=17;
#                                            Stab_{E_6}(E_11)=61; Stab_{V_0}=45=Spin(9,1);
#                                            K=-1/2 cone-Hessian sign benchmark (round_K=-1).
#
# CONVENTION LOCK (v18.0, inherited from v17.0; see CONVENTIONS.md / state.json):
#   * EXACT over Q (sympy QQ); NO float on any decisive path.
#   * octonion multiplication: Fano e1 e2 = e4.       complex structure: u = e7.
#   * primitive idempotent: E_11 = diag(1,0,0).       Peirce eigenvalues {0,1/2,1}.
#   * det SSOT = ring_lemma_verification.py det_3 (F_4-invariant cubic norm); the
#     cyclic 2Re((x1 x2)x3) variant is the documented BUG (off by 16; annihilated by
#     only 30/324 inner derivations) and is REJECTED. octonion_algebra.py is BANNED
#     on every decisive path.
#   * metric signature mostly-minus (-,+,+,+) on the h_2(C_u) det_2 Lorentzian slice;
#     bulk cone Riemannian (positive-definite). natural units hbar=k_B=1.
#   * engine 27-coord layout: V_1={0} (alpha); V_0={1..10}; V_{1/2}={11..26}
#     (V_HALF_IDX = list(range(11,27))).
#
# Reuses the warm exact-Q engine primitives from bulk_geometry_verification.py
# (peirce_indices_under_E11, _standard_basis_27, _flat27, jordan, octmat_*,
# h3o_from_coords, oct_zero) -- imported, NOT rebuilt. The det_3/jordan/octonion
# product are inherited verbatim; this file adds ONLY the new Jacobian-kernel
# tangent check and a thin three-engine re-pass/assert driver.
#
# Reproducibility: Python 3.14.2, SymPy 1.14.0 (deterministic, exact over Q; no RNG
# on any decisive path -- generic-point sampling inside the engines uses fixed
# integer points).
#
# Runnable directly:  python3 -u code/cartan_phase0_tangent.py
# Exits 0 iff DERV-01, DERV-02, and VALD-01 all PASS; nonzero on any failure.
# ============================================================================

import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CODE_DIR = os.path.join(REPO_ROOT, "code")
if CODE_DIR not in sys.path:
    sys.path.insert(0, CODE_DIR)

from sympy import Matrix, Rational  # noqa: E402

import bulk_geometry_verification as BG  # noqa: E402  (warm SSOT-consistent engine primitives)

# Engine-native Peirce layout (v17.0 lock).
V_HALF_IDX = list(range(11, 27))   # V_{1/2}(E_11) engine indices (16 elements)
V0_IDX = list(range(1, 11))        # V_0 (10 elements)
V1_IDX = [0]                       # V_1 (alpha direction)

# Track overall pass/fail; the script must exit nonzero on any failure.
ALL_PASS = True


def _report(label, ok):
    """Print a PASS/FAIL line; latch ALL_PASS to False on any failure."""
    global ALL_PASS
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {label}")
    if not ok:
        ALL_PASS = False
    return ok


def _run_engine(rel_path):
    """Run an engine UNBUFFERED (python -u), return (exit_code, stdout_text).

    Pitfall 3: exact-QQ runs buffer stdout when not a TTY; `-u` keeps progress
    visible so a watchdog does not mistake buffered silence for a stall. We run
    in the foreground and capture the full stdout for the anchor greps. The
    engines are deterministic and byte-identical to the v17.0 anchors -- this is
    run-and-assert, not assume.
    """
    proc = subprocess.run(
        [sys.executable, "-u", os.path.join(REPO_ROOT, rel_path)],
        cwd=REPO_ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    return proc.returncode, proc.stdout


# ============================================================================
# DERV-01 : re-certify the det SSOT engine + the source guard
# ============================================================================
def derv01():
    """Re-pass ring_lemma_verification.py and assert the four load-bearing facts:
    exit 0 + ALL_PASS; LOCK 7a (det_3 == CH generic norm); LOCK 7b (324/324
    inner-derivation annihilation = dim f_4 = 52); source guard (0 outside-fence
    octonion_algebra imports, 0 float-rank calls)."""
    print("=" * 78)
    print("DERV-01 : det SSOT re-certification (ring_lemma_verification.py)")
    print("  det_3 = F_4-invariant cubic norm; CH (LOCK 7a) + 324/324 (LOCK 7b);")
    print("  source guard => octonion_algebra.py ABSENT on the decisive path.")
    print("=" * 78)

    rc, out = _run_engine("code/ring_lemma_verification.py")
    print(f"      ring_lemma_verification.py exit code = {rc} (expect 0)")

    exit0 = (rc == 0)
    all_pass = ("ALL_PASS" in out) and ("FAILURES PRESENT" not in out)
    # LOCK 7a: det_3 == Cayley-Hamilton generic norm (3 octonionic points).
    lock7a = ("[PASS] LOCK 7a det_3 == Cayley-Hamilton generic norm" in out)
    # LOCK 7b: 324/324 inner-derivation annihilation = dim f_4 = 52. RED FLAG if
    # the count comes back < 324 (e.g. 30 = the buggy (x1 x2)x3 association).
    lock7b = ("[PASS] LOCK 7b" in out) and ("324/324" in out) and ("dim f_4=52" in out)
    # Source guard: the LOAD-BEARING assertion is "0 outside" + "float-rank calls: 0".
    # The single in-fence import is the sanctioned oracle (a float reference
    # cross-check, NOT on the decisive path).
    guard_line_ok = (
        "exact-only guard" in out
        and "0 outside (expect 0)" in out
        and "float-rank calls: 0 (expect 0)" in out
    )

    _report("ring_lemma_verification.py exit 0 AND OVERALL: ALL_PASS "
            "(no FAILURES PRESENT)", exit0 and all_pass)
    _report("LOCK 7a -- det_3 == Cayley-Hamilton generic norm of jordan "
            "[3 octonionic points, exact over Q]", lock7a)
    _report("LOCK 7b -- det_3 annihilated by ALL 324 inner derivations [L_a,L_b] "
            "(324/324 = dim f_4 = 52), NOT 30; det_3 is F_4-invariant [exact Q]",
            lock7b)
    _report("SOURCE GUARD -- octonion_algebra.py ABSENT on the decisive path: "
            "0 outside-fence imports, 0 float-rank calls (1 in-fence = sanctioned "
            "oracle) [fp-octonion-algebra + fp-float-decisive REJECTED]",
            guard_line_ok)

    ok = exit0 and all_pass and lock7a and lock7b and guard_line_ok
    if ok:
        print("      DERV-01 PASS: ring_lemma exit 0 + ALL_PASS; LOCK 7a (CH norm); "
              "LOCK 7b (324/324 = dim f_4 = 52); guard (0 outside-fence, 0 float-rank).")
    else:
        print("      DERV-01 FAIL: ENGINE DRIFT from the v17.0 SSOT -- STOP, diff "
              "against the warm commit; do NOT patch the cross-term or import "
              "octonion_algebra.py.")
    return ok


# ============================================================================
# DERV-02 : exact tangent identity  E_11 o delta = (1/2)delta  and
#           T_{E_11}OP^2 = V_{1/2}(E_11) = 16   (the ONE new computation)
# ============================================================================
def derv02():
    """(a) Peirce half-eigenspace: E_11 o delta = (1/2)delta for the V_{1/2} basis.
    (b) Zariski tangent of {X o X = X} at E_11 (kernel of the 27x27 Jacobian of
    F(X)=X o X - X) EQUALS V_{1/2}(E_11), dim 16 (rank 11; kernel == span{11..26};
    16 = 17-1). Baez 2002 / McCrimmon CITED, not re-derived. EXACT over Q
    throughout (sympy QQ; fp-float-decisive rejected)."""
    print("=" * 78)
    print("DERV-02 : soldering form is V_{1/2}-valued -- T_{E_11}OP^2 = V_{1/2}(16)")
    print("  (a) E_11 o delta = (1/2)delta (Peirce; McCrimmon)")
    print("  (b) Zariski tangent of {X o X = X} at E_11 == V_{1/2} (Baez 2002 Sec 3.4)")
    print("=" * 78)

    E11 = BG.h3o_from_coords(1, 0, 0, BG.oct_zero(), BG.oct_zero(), BG.oct_zero())
    basis = BG._standard_basis_27()

    # ---- Clause (a): the half-eigenvalue split (Peirce), read off L_{E_11} ----
    groups, diagonal = BG.peirce_indices_under_E11()
    V1 = sorted(groups.get(Rational(1), []))
    V0 = sorted(groups.get(Rational(0), []))
    Vh = sorted(groups.get(Rational(1, 2), []))
    print(f"      Peirce under E_11 (L_E11 diagonal={diagonal}): "
          f"V_1={V1}, V_0={V0} (|{len(V0)}|), V_1/2={Vh} (|{len(Vh)}|)")
    _report("PEIRCE under E_11=diag(1,0,0): V_1=[0] (+) V_0=[1..10] (+) "
            "V_1/2=[11..26](16); L_E11 diagonal in engine basis [exact Q]",
            diagonal and V1 == V1_IDX and V0 == V0_IDX and Vh == V_HALF_IDX)

    # E_11 o delta = (1/2) delta for each delta in the V_{1/2} basis (exact over Q).
    half_ok = 0
    for k in V_HALF_IDX:
        lhs = BG.jordan(E11, basis[k])                       # E_11 o delta_k
        rhs = BG.octmat_scal(Rational(1, 2), basis[k])       # (1/2) delta_k
        if BG.octmat_equal(BG.octmat_simplify(lhs), BG.octmat_simplify(rhs)):
            half_ok += 1
    print(f"      E_11 o delta == (1/2)delta verified for {half_ok}/16 V_1/2 basis "
          f"elements (component-wise octonion equality, exact over Q)")
    _report("CLAUSE (a): E_11 o delta = (1/2)delta EXACTLY over Q for ALL 16 "
            "V_{1/2}(E_11) basis elements (the Peirce half-eigenspace identity; "
            "McCrimmon) [exact Q, not 'approximately']", half_ok == 16)

    # ---- Clause (b): the Zariski tangent of the primitive-idempotent variety ----
    # F(X) = X o X - X (the trace-1 idempotent / OP^2 equation; rank-1 locus = the
    # affine cone over OP^2 cut by X^2 = Tr(X)X with the trace-1 normalization).
    # Linearize at E_11: DF(b_k) = 2*jordan(E_11, b_k) - b_k  (jordan is symmetric).
    # Jacobian column k = _flat27(DF(b_k)) over the standard basis.
    cols = [
        BG._flat27(BG.octmat_sub(BG.octmat_scal(Rational(2), BG.jordan(E11, basis[k])),
                                 basis[k]))
        for k in range(27)
    ]
    J = Matrix(27, 27, lambda r, c: cols[c][r])

    rank_J = J.rank()                  # EXACT over Q
    ker = J.nullspace()                # Zariski tangent space, EXACT over Q
    dim_ker = len(ker)
    print(f"      Jacobian J of F(X)=X o X - X at E_11: J.rank() = {rank_J} "
          f"(expect 11 = 27-16); dim ker = {dim_ker} (expect 16 = dim T_E11 OP^2)")
    _report("CLAUSE (b) DIM: J.rank() == 11 (= 27-16) AND dim ker == 16 "
            "(= dim T_{E_11}OP^2 = the Cayley-plane dimension) [exact Q]",
            rank_J == 11 and dim_ker == 16)

    # IDENTITY with V_{1/2} (Pitfall 2: NOT merely dimension). Khalf = 27x16 unit
    # columns at indices 11..26; rank[ker | Khalf] == 16 iff ker == span(V_HALF_IDX).
    Khalf = Matrix.hstack(*[Matrix([1 if i == j else 0 for i in range(27)])
                            for j in V_HALF_IDX])
    rank_combined = Matrix.hstack(*ker, Khalf).rank()
    # Defensive cross-check: every kernel vector is ZERO on V_0{1..10} and V_1{0}.
    nonhalf = V1_IDX + V0_IDX
    leak = any(v[i] != 0 for v in ker for i in nonhalf)
    print(f"      rank[ker | V_HALF_IDX] = {rank_combined} (expect 16 => "
          f"ker == span{{11..26}}); any ker leak into V_0/V_1? {leak} (expect False)")
    _report("CLAUSE (b) IDENTITY: rank[ker | V_HALF_IDX] == 16 -- the kernel "
            "EQUALS V_{1/2}(E_11) = span(engine indices {11..26}), NOT merely a "
            "16-dim subspace; no component in V_0{1..10} or V_1{0} [exact Q]",
            rank_combined == 16 and (leak is False))

    # Cross-check 16 = 17 - 1 against orbit(E_11) = 17 (reproduced in VALD-01).
    print("      CROSS-CHECK: dim T_{E_11}OP^2 = 16 == 17 - 1 = orbit(E_11) - 1 "
          "(affine cone over OP^2 minus the scale direction; orbit(E_11)=17 "
          "reproduced by bulk_geometry_verification.py in VALD-01)")
    _report("CROSS-CHECK: 16 == 17 - 1 (projective OP^2 tangent = affine-cone "
            "orbit(E_11)=17 minus the 1 scale direction) [exact integer]",
            dim_ker == 17 - 1)

    ok = ALL_PASS  # latched by the _report calls above for this section
    if rank_J == 11 and dim_ker == 16 and rank_combined == 16 and not leak and half_ok == 16:
        print("      DERV-02 PASS: E_11 o delta = (1/2)delta (16/16); Zariski tangent "
              "of {X o X = X} at E_11 == V_{1/2} = {11..26}, dim 16 = 17-1. EXACT over Q.")
    return ok


# ============================================================================
# VALD-01 : reproduce the calibration anchors + the K=-1/2 sign benchmark
#           (anchors SPLIT across orbit_dimension_gate.py + bulk_geometry_verification.py)
# ============================================================================
def vald01():
    """Re-run the two slow calibration engines UNBUFFERED and assert each anchor:
      orbit_dimension_gate.py    -> single-copy 24 / Spin(8)=28 / trdeg 3
      bulk_geometry_verification -> e_6=78=52+26; orbit(E_11)=17; Stab_{E_6}(E_11)=61;
                                    Stab_{V_0}=45=Spin(9,1); K=-1/2 (round_K=-1).
    These are deterministic and byte-identical to the v17.0 anchors -- run-and-assert."""
    print("=" * 78)
    print("VALD-01 : calibration anchors + K=-1/2 sign benchmark (3 engines, exact Q)")
    print("=" * 78)

    # --- single-copy anchor: orbit_dimension_gate.py ---
    # IMPORTANT (driver correctness, not a VALD-01 anchor failure): this engine is
    # the v16.0 RING gate. By DESIGN it exits NONZERO -- its `test-anchor-7`
    # (pair-orbit trdeg == 7) is a milestone go/no-go assertion that FAILS because
    # the COMPUTED pair trdeg is 10 (orbit 44), the documented v16.0 result
    # (triple-confirmed; see MEMORY project_v16_ring_lemma). That nonzero exit is
    # UNRELATED to the VALD-01 single-copy anchor, which PASSES cleanly inside it.
    # The decisive VALD-01 condition is therefore the explicit single-copy PASS
    # lines (test-single-copy-24 / test-stabilizer-28 / test-trdeg-3) + the source
    # guard, NOT the overall exit code. We assert those lines directly and verify
    # the only FAILs present are the expected v16.0 pair-anchor lines.
    print("  orbit_dimension_gate.py (single-copy 24 / Spin(8)=28 / trdeg 3) ...")
    rc_g, out_g = _run_engine("code/orbit_dimension_gate.py")
    print(f"      orbit_dimension_gate.py exit code = {rc_g} (DESIGNED nonzero: the "
          f"v16.0 RING pair-anchor test-anchor-7 fails by design; the single-copy "
          f"anchor below is what VALD-01 needs and it PASSES)")
    # The three single-copy anchor PASS lines (each an engine `_report` hard check).
    sc_24 = "[PASS]" in out_g and "single-copy orbit rank over QQ == 24" in out_g
    sc_multi = "[PASS]" in out_g and "MAX single-copy orbit rank over QQ == 24" in out_g
    sc_orbit = ("[PASS] orbit_dim == 24 (single-copy generic orbit" in out_g)
    sc_spin8 = ("[PASS] stabilizer dim = 52 - 24 == 28 == dim Spin(8)" in out_g)
    sc_trdeg = ("[PASS] single-state trdeg = 27 - 24 == 3" in out_g)
    sc_certified = ("Garibaldi-Guralnick / Lawther single-copy anchor (orbit 24 "
                    "/ Spin(8) 28 / trdeg 3) REPRODUCED in-engine" in out_g)
    # Source guard inside this engine: 0 octonion_algebra, 0 float-rank.
    g_guard = ("[PASS] exact-only guard: no float-rank / no octonion_algebra on "
               "decisive path" in out_g) and ("float-rank calls: 0 (expect 0)" in out_g)
    # Confirm the ONLY FAILs are the expected, designed v16.0 pair-anchor lines
    # (test-anchor-7 / pair-stabilizer == 5). Any OTHER FAIL would be true drift.
    fail_lines = [ln for ln in out_g.splitlines() if "[FAIL]" in ln]
    expected_fail_markers = ("test-anchor-7", "pair-stabilizer dim == 5")
    only_expected_fails = all(any(m in ln for m in expected_fail_markers)
                              for ln in fail_lines)
    single_copy_ok = (sc_24 and sc_multi and sc_orbit and sc_spin8 and sc_trdeg
                      and sc_certified and g_guard and only_expected_fails)
    _report("SINGLE-COPY anchor (orbit_dimension_gate.py): generic orbit dim == 24 "
            "(MAX over 3 generic integer points), stabilizer == 52-24 == 28 == dim "
            "Spin(8), trdeg == 27-24 == 3 (= R[Tr, Tr^2, det]); 0 octonion_algebra, "
            "0 float-rank -- COMPUTED in-engine, not looked up [exact Q]",
            sc_24 and sc_multi and sc_orbit and sc_spin8 and sc_trdeg and sc_certified
            and g_guard)
    _report("orbit_dimension_gate.py nonzero exit is the DESIGNED v16.0 RING "
            "pair-anchor gate-stop (test-anchor-7: pair trdeg 10 != 7), NOT engine "
            "drift: the only FAILs are the expected pair-anchor lines; the VALD-01 "
            "single-copy anchor is unaffected", only_expected_fails)
    gate_pass = single_copy_ok

    # --- e_6 / orbit(E_11) / stabilizers / K: bulk_geometry_verification.py ---
    print("  bulk_geometry_verification.py (e_6=78; orbit(E_11)=17; Stab=61; "
          "Stab_{V_0}=45; K=-1/2) ... [SLOW: several minutes; running unbuffered]")
    rc_b, out_b = _run_engine("code/bulk_geometry_verification.py")
    print(f"      bulk_geometry_verification.py exit code = {rc_b} (expect 0)")
    bulk_pass = (rc_b == 0) and ("ALL_PASS" in out_b) and ("FAILURES PRESENT" not in out_b)

    e6_ok = ("dim 78 = 52 + 26" in out_b) or ("dim 78 = 52+26" in out_b) \
        or ("[PASS] e_6 = f_4 + L(h_3(O)_traceless), dim 78 = 52 + 26" in out_b)
    # orbit(E_11)=17 and Stab_{E_6}(E_11)=61.
    orbit17_stab61 = ("orbit of E_11 = 17" in out_b) and ("dim Stab = 61" in out_b)
    # Stab_{V_0} = 45 = Spin(9,1).
    stabV0_45 = ("== 45 == dim Spin(9,1)" in out_b)
    # K = -1/2 with round_K = -1 (factor-2 cross-check). RED FLAG if +1/2 or -1.
    K_half = ("K == -1/2" in out_b) and ("round-metric reinforcement K == -1" in out_b) \
        and ("exact factor-of-2" in out_b)

    _report("bulk_geometry_verification.py exit 0 + ALL_PASS [exact over Q]",
            bulk_pass)
    _report("e_6 = f_4 (+) L(h_3(O)_traceless), dim 78 = 52 + 26 (exact span rank "
            "over Q) [test-e6-dim]", e6_ok)
    _report("orbit(E_11) = 17 (affine cone over OP^2) AND Stab_{E_6}(E_11) = 61 "
            "= 78-17 (exact kernel over Q); 17 is the DERV-02 16=17-1 cross-check "
            "[test-homogeneity]", orbit17_stab61)
    _report("Stab_{V_0} = 45 = dim Spin(9,1) (the slice-preserving Levi; exact "
            "kernel over Q)", stabV0_45)
    _report("K = -1/2 cone-Hessian sign benchmark (NEGATIVE-constant sign is "
            "load-bearing) WITH round_K = -1 factor-2 cross-check (g_slice|_apex "
            "= 2*g_round); NOT +1/2, NOT -1 [exact rationals over Q]", K_half)

    ok = (single_copy_ok
          and bulk_pass and e6_ok and orbit17_stab61 and stabV0_45 and K_half)
    if ok:
        print("      VALD-01 PASS: single-copy 24/Spin(8)=28/trdeg 3; e_6=78=52+26; "
              "orbit(E_11)=17; Stab_E6(E_11)=61; Stab_{V_0}=45=Spin(9,1); "
              "K=-1/2 (round_K=-1). All exact integers/rationals.")
    else:
        print("      VALD-01 FAIL: a v17.0 anchor did not reproduce -- STOP and diff "
              "against the warm commit (sign/normalization slip or e_6/stabilizer "
              "regression). Do NOT re-derive; re-read the engine normalization note.")
    return ok


def main():
    print("#" * 78)
    print("# Phase 74-01 : Phase 0 -- engine recovery, tangent identity, calibration")
    print("#   EXACT over Q on every decisive path (fp-float-decisive REJECTED).")
    print("#" * 78)

    ok1 = derv01()
    ok2 = derv02()
    ok3 = vald01()

    print("=" * 78)
    print(f"DERV-01 (det SSOT) ............ {'PASS' if ok1 else 'FAIL'}")
    print(f"DERV-02 (tangent identity) .... {'PASS' if ok2 else 'FAIL'}")
    print(f"VALD-01 (calibration) ......... {'PASS' if ok3 else 'FAIL'}")
    print(f"OVERALL: {'ALL_PASS' if ALL_PASS else 'FAILURES PRESENT'}")
    print("=" * 78)
    return 0 if ALL_PASS else 1


if __name__ == "__main__":
    sys.exit(main())
