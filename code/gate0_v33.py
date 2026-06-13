#!/usr/bin/env python3
"""gate0_v33.py -- Phase 93 (v33.0) GATE 0 (BINDING STOP GATE): discharge the v32 deferred obligation.

Certify eps = lambda_L - 2 Lambda = 32 - 12 = 20 on a CORRECT, DIRECTLY-RUN full-tensor Lichnerowicz
operator (the v32 record had eps=20 on EVIDENCE -- Boucetta Table V/VIII row 2 + degree-counting +
the (1,1) Schur scalar + the fingerprint -- NOT on a directly-run full-block Delta_L; the old full
`lichnerowicz` returned a spurious 28/4 on the verdict residue's anti-blocks).

THE METHOD (RESEARCH s1, exact over Q, fail-fast):
  Step B (done in lichnerowicz_response.py): the corrected full operator `lichnerowicz_full_v33`
    fixes TWO independent bugs in the old anti-block path (both DERIVED, validated by the controls,
    NEVER tuned to r):
      BUG 1 -- rough_laplacian now uses BOTH orderings of the 2nd covariant derivative
               (nabla*nabla = -(g^{a bbar} nabla_a nabla_bbar + g^{abar b} nabla_abar nabla_b), -1
               each), restoring conjugate symmetry on the anti-blocks.
      BUG 2 -- Rdot now contracts ONE uniform index-honest formula -R_{mu rho nu sigma} h^{rho sigma}
               via _R_low + full raising, the sign FIXED to reproduce Rdot(g)|(1,1)=Ric=+6g; the
               anti-blocks inherit the consistent sign.
  Step C (here): validate the operator against the PROVABLE controls (the oracle; NO tuning to r):
      C1   Delta_L g = 0 on all blocks.
      C2a  Delta_L(Hess phi_M) = 12 Hess(phi_M) on (1,1) (anti vanish -- Matsushima).
      C2b  Delta_L(Hess R_M) = 32 Hess(R_M) EXACT on ALL THREE blocks, (2,0)==(0,2) (the no-tuning
           certificate: Hess(R_M) is a PROVABLE 32-eigentensor by Besse's Delta_L o delta* = delta* o
           Delta_H with Delta_H(dR_M)=32 dR_M).
      REG  lichnerowicz_11 still returns 32 on r[1] (the validated (1,1) path intact).
  Step D (here): read the verdict residue r = extract_tt(grad_bilinear(phi_M)) for >=3 matter
      directions (s01,a01,d1) AND one generic detM!=0 matter; confirm Delta_L r = 32 r EXACT on
      EVERY block (all three).
  Step E (here): PASS => eps=20 CERTIFIED on a directly-run control-validated operator (the v32
      deferred obligation discharged).  FAIL (operator validated by C2b but r != 32 on some block)
      => a genuine STOP -- report it, do NOT fabricate a pass.

SCOPE FENCE (binding, verbatim): this is the deformation-complex DICTIONARY of a FROZEN imported
geometry.  No dynamical metric, no selection law, no kappa (here kappa is NOT Newton's constant).
NO Einstein-equation / G=kT / gravity / dark-matter / geodesic language; the frozen FS geometry is
USED not derived; signature Riemannian.  This is the frozen deformation-complex dictionary.

Reproducibility: sympy 1.14.0, Python 3.14, exact rational arithmetic over Q / Q(i) (no RNG / no
seeds in the verdict path; floats illustrative only).  Darwin arm64.
Run: python3 -u code/gate0_v33.py
"""
import sys
import time

import sympy as sp
from sympy import Matrix, Rational, I, zeros, cancel

sys.path.insert(0, __file__.rsplit("/", 1)[0])
import tensor_probe as TP
from lichnerowicz_response import (lichnerowicz_full_v33, lichnerowicz_11, riemann_kahler,
                                   extract_tt)

_t0 = time.time()


def _log(m):
    print(f"[{time.time() - _t0:6.1f}s] {m}", flush=True)


# --- the eight Gell-Mann su(3) matter directions + a generic detM!=0 matter (frozen) ---
GM = {
    "s01": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),       # lambda_1
    "a01": Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),      # lambda_2
    "d1":  Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),      # lambda_3
}
# a generic detM != 0 matter: d2 = diag(1,1,-2) = sqrt(3)*lambda_8 (detM = -2 != 0; the v32
# fingerprint's detM != 0 witness).  This is the genuine "generic detM-nonzero" probe -- it carries
# a nonzero degree-3 invariant (detM) and verifies the residue eigenvalue is detM-independent (=32),
# while staying TRACTABLE (a fully-dense 8-channel M makes cov_hessian(R_M) a multi-thousand-term
# rho-rational object whose Delta_L exceeds the watchdog; d2 is the standard detM!=0 representative).
M_GEN = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]])      # detM = -2 != 0
# the fully-dense generic matter (recorded; used only in an OPTIONAL slow cross-check, not the gate)
M_DENSE = Matrix([[2, Rational(1, 2) + I / 3, Rational(1, 4) - I / 5],
                  [Rational(1, 2) - I / 3, -3, Rational(1, 6) + I / 7],
                  [Rational(1, 4) + I / 5, Rational(1, 6) - I / 7, 1]])


def eig_on_blocks(dL, X):
    """Per-block eigenvalue lam_k s.t. dL[k] == lam_k * X[k] (exact over Q), checked per entry by
    `cancel(dL[k][a,b] - lam*X[k][a,b]) == 0`.  Returns {k: lam | 'ZERO' | 'NOT-PROP'}."""
    res = {}
    for k in range(3):
        lam = None
        ok = True
        allzero = True
        for a in range(2):
            for b in range(2):
                xb = cancel(X[k][a, b])
                db = cancel(dL[k][a, b])
                if xb == 0:
                    if db != 0:
                        ok = False
                    continue
                allzero = False
                r = cancel(db / xb)
                if lam is None:
                    lam = r
                elif cancel(lam - r) != 0:
                    ok = False
        res[k] = ("ZERO" if allzero else (lam if ok else "NOT-PROP"))
    return res


def eig_exact_lambda(dL, X, lam):
    """Confirm dL[k] == lam * X[k] EXACTLY on EVERY block (all three), entrywise over Q.  Returns
    (ok_all, per_block_bool)."""
    perblock = []
    for k in range(3):
        bok = all(cancel(dL[k][a, b] - lam * X[k][a, b]) == 0 for a in range(2) for b in range(2))
        perblock.append(bok)
    return all(perblock), perblock


def main():
    print("=" * 78)
    print("GATE 0 (v33.0) : certify eps=20 on a CONTROL-VALIDATED, DIRECTLY-RUN full-tensor Delta_L")
    print("=" * 78)
    print("[SCOPE FENCE] deformation-complex DICTIONARY of a FROZEN imported geometry; no dynamical")
    print("metric, no selection law, no kappa (kappa NOT Newton); frozen FS geometry USED not derived;")
    print("NO Einstein/G=kT/gravity language; signature Riemannian.  Exact over Q/Q(i).")
    print("")

    g = TP.fs_metric()
    ginv = TP.fs_metric_inv(g)
    Gam = TP.christoffel_hol(g, ginv)
    GamB = TP._christoffel_antihol(g, ginv)
    R = riemann_kahler(g, ginv, Gam)
    _log("geometry built (FS Kahler-Einstein, Ric=6g, Lambda=6)")

    results = {}

    # ========================= Step C -- the PROVABLE controls (the oracle) ==================
    print("\n" + "-" * 78)
    print("Step C -- validate the operator against the PROVABLE controls (NO tuning to r)")
    print("-" * 78)

    # --- C1: Delta_L g = 0 on all blocks (g as a (1,1) tensor) ---
    gblocks = (zeros(2, 2), g, zeros(2, 2))
    dLg = lichnerowicz_full_v33(gblocks, g, ginv, Gam, GamB, R, Lambda=6)
    c1 = all(cancel(dLg[k][a, b]) == 0 for k in range(3) for a in range(2) for b in range(2))
    results["C1"] = c1
    _log(f"C1: Delta_L g == 0 on ALL blocks (g is Delta_L-harmonic on KE): {c1}")

    # --- C2a: Delta_L(Hess phi_M) = 12 on (1,1), anti-blocks VANISH (Matsushima) ---
    M = GM["s01"]
    phi = cancel(TP.phi_field(M))
    Hphi = TP.cov_hessian(phi, g, ginv, Gam, simp=cancel)
    anti0 = all(cancel(Hphi[0][a, b]) == 0 and cancel(Hphi[2][a, b]) == 0
                for a in range(2) for b in range(2))
    dLHphi = lichnerowicz_full_v33(Hphi, g, ginv, Gam, GamB, R, Lambda=6)
    eig_a = eig_on_blocks(dLHphi, Hphi)
    c2a = (eig_a.get(1) == 12 and eig_a.get(0) == "ZERO" and eig_a.get(2) == "ZERO" and anti0)
    results["C2a"] = c2a
    _log(f"C2a: Delta_L(Hess phi_s01) per block {eig_a} (Hess anti vanish={anti0}); "
         f"(1,1)->12 expected: {c2a}")

    # --- C2b (DECISIVE): Delta_L(Hess R_M) = 32 on ALL THREE blocks, (2,0)==(0,2) ---
    # Hess(R_M) is a PROVABLE 32-eigentensor (Besse Delta_L o delta* = delta* o Delta_H, Delta_H
    # dR_M = 32 dR_M).  Run >=2 sparse directions (fast) + the generic detM!=0 matter (incremental).
    c2b_dirs = {}
    for nm in ["s01", "d1", "GEN"]:
        Mc = M_GEN if nm == "GEN" else GM[nm]
        RM = TP.R_M_field(Mc)
        HRM = TP.cov_hessian(RM, g, ginv, Gam, simp=cancel)
        nz = [not all(cancel(HRM[k][a, b]) == 0 for a in range(2) for b in range(2)) for k in range(3)]
        _log(f"C2b[{nm}]: Hess(R_M) blocks nonzero [H20,H11,H02]={nz}; running Delta_L ...")
        dLHRM = lichnerowicz_full_v33(HRM, g, ginv, Gam, GamB, R, Lambda=6)
        eig_b = eig_on_blocks(dLHRM, HRM)
        ok32, _ = eig_exact_lambda(dLHRM, HRM, 32)
        conj_sym = (eig_b.get(0) == eig_b.get(2))      # (2,0)==(0,2) eigenvalues equal
        passed = (eig_b.get(0) == 32 and eig_b.get(1) == 32 and eig_b.get(2) == 32 and ok32 and all(nz))
        c2b_dirs[nm] = passed
        _log(f"C2b[{nm}]: eig per block [H20,H11,H02]={eig_b}  exact-32-all-blocks={ok32}  "
             f"(2,0)==(0,2)={conj_sym}  PASS={passed}")
    c2b = all(c2b_dirs.values())
    results["C2b"] = c2b
    _log(f"C2b (DECISIVE, the no-tuning certificate): {c2b_dirs}  ALL PASS={c2b}")

    # --- REG: lichnerowicz_11 still returns 32 on r[1] (the validated (1,1) path intact) ---
    # r[1] = the (1,1) block of the verdict residue for s01.
    B3_s01 = TP.grad_bilinear(cancel(TP.phi_field(GM["s01"])), simp=sp.together)
    _log("REG: extracting r(s01) for the lichnerowicz_11 regression ...")
    r_s01, _, _, _, info_s01 = extract_tt(B3_s01, g, ginv, Gam, verify=True)
    r11only = (zeros(2, 2), r_s01[1], zeros(2, 2))
    dL11 = lichnerowicz_11(r11only, g, ginv, Gam, GamB, R, Lambda=6)
    eig_reg = eig_on_blocks(dL11, r11only)
    reg_ok = (eig_reg.get(1) == 32)
    results["REG"] = reg_ok
    _log(f"REG: lichnerowicz_11(r[1](s01)) -> (1,1) eigenvalue {eig_reg.get(1)} (==32 expected): "
         f"{reg_ok} (r consistent={info_s01.get('consistent')}, tr0={info_s01.get('tr_zero')}, "
         f"div0={info_s01.get('div_zero')})")

    controls_ok = c1 and c2a and c2b and reg_ok
    print(f"\n  Step C CONTROLS: C1={c1} C2a={c2a} C2b={c2b} REG={reg_ok}  ALL={controls_ok}")
    if not controls_ok:
        print("\n  *** STEP C FAILED -- the operator is NOT validated by the provable controls.")
        print("  *** Per RESEARCH s1.3, fix the operator (the fix is principled, validated by C2b,")
        print("  *** NEVER by r); do NOT proceed to read r. ***")
        print(f"\n  GATE 0 (v33.0): FAIL -- operator not control-validated, STOP.")
        return False, results

    # ========================= Step D -- read the verdict residue r =========================
    print("\n" + "-" * 78)
    print("Step D -- read the verdict residue r (ONLY after C1/C2a/C2b PASS): Delta_L r = 32 r ?")
    print("-" * 78)
    r_dirs = {}
    r_cache = {"s01": (r_s01, info_s01)}
    for nm in ["s01", "a01", "d1", "GEN"]:
        Mc = M_GEN if nm == "GEN" else GM[nm]
        if nm in r_cache:
            r, info = r_cache[nm]
        else:
            B3 = TP.grad_bilinear(cancel(TP.phi_field(Mc)), simp=sp.together)
            _log(f"D[{nm}]: extracting verdict residue r = extract_tt(grad_bilinear(phi_M)) ...")
            r, _, _, _, info = extract_tt(B3, g, ginv, Gam, verify=True)
        tt_ok = (r is not None and info.get("consistent") and info.get("tr_zero")
                 and info.get("div_zero"))
        nz = [not all(cancel(r[k][a, b]) == 0 for a in range(2) for b in range(2)) for k in range(3)]
        _log(f"D[{nm}]: r consistent/tr0/div0={tt_ok}; blocks nonzero [H20,H11,H02]={nz}; "
             f"running Delta_L r ...")
        dLr = lichnerowicz_full_v33(r, g, ginv, Gam, GamB, R, Lambda=6)
        eig_r = eig_on_blocks(dLr, r)
        ok32, perblock = eig_exact_lambda(dLr, r, 32)
        passed = (tt_ok and all(nz) and ok32 and eig_r.get(0) == 32 and eig_r.get(1) == 32
                  and eig_r.get(2) == 32)
        r_dirs[nm] = passed
        _log(f"D[{nm}]: Delta_L r eig per block [H20,H11,H02]={eig_r}  "
             f"exact-32-all-blocks={ok32} {perblock}  PASS={passed}")
    r_all = all(r_dirs.values())
    results["r_dirs"] = r_dirs

    # ========================= Step E -- verdict =========================
    print("\n" + "=" * 78)
    print("Step E -- VERDICT")
    print("=" * 78)
    if controls_ok and r_all:
        eps = 32 - 12
        print(f"  ALL CONTROLS PASS (C1,C2a,C2b,REG) AND Delta_L r = 32 r EXACT on EVERY block for")
        print(f"  all {len(r_dirs)} directions {list(r_dirs.keys())} (s01,a01,d1 + GEN=d2 detM=-2!=0).")
        print(f"  => lambda_L = 32 on the full tensor (all three Kahler sectors, conjugate-symmetric)")
        print(f"  => eps = lambda_L - 2 Lambda = 32 - 12 = {eps}  CERTIFIED on a directly-run,")
        print(f"     control-validated full-tensor operator.  The v32 deferred obligation is")
        print(f"     DISCHARGED.  r tracks the provable C2b control identically (both 32 on every")
        print(f"     block) -- the airtight proof r is a clean lambda_L=32 eigentensor (the 28/4 was")
        print(f"     purely the old operator bug).")
        print(f"\n  [FENCE] eps={eps} is a Delta_L-STIFFNESS of the FROZEN deformation complex, NOT a")
        print(f"  dynamical response; kappa is NOT Newton's constant; no Einstein equation here.")
        print(f"\n  GATE 0 (v33.0): PASS -- eps=20 CERTIFIED.")
        return True, results
    else:
        print(f"  Operator control-validated (C1={c1},C2a={c2a},C2b={c2b},REG={reg_ok}) but")
        print(f"  Delta_L r = 32 r FAILED on some block: {r_dirs}.")
        print(f"  This is a GENUINE STOP (RESEARCH s1.1): the operator passes the provable controls")
        print(f"  yet r is NOT a clean 32-eigentensor -- the eps=20 grade must be revisited.  Do NOT")
        print(f"  fabricate a pass.")
        print(f"\n  GATE 0 (v33.0): FAIL -- STOP, revisit eps=20.")
        return False, results


if __name__ == "__main__":
    ok, _ = main()
    sys.exit(0 if ok else 1)
