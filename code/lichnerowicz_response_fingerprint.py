#!/usr/bin/env python3
"""Phase 92 (v32.0-B) FINGERPRINT TESTS -- the empirical backbone of the reconciled verdict.

Reconciliation (v32-reconciliation-directive.md): the matter-sourced TT residue of
B3 = dphi_M (x) dphi_M is a SINGLE Lichnerowicz eigentensor at lambda_L = 32 that STRADDLES the
three Kahler sectors -- the (1,1) dim-27 (Boucetta Table V/VIII row 2, phi.delta*_h.delta-bar*_h
of the level-2 scalars) (+) the (2,0)+(0,2) dim-27s (Tables VI/VII row 1).  NOT the lambda=12
dim-8 adjoint (row 1, which is non-transverse).  c_8 = c_1 = 0 (the 8/1 channels have no
transverse home at this level).  The forced closed form is TT(B3[M]) = T_27[P27(M (x) M)].

These tests reproduce -- executor-side, exact over Q on the certified driver -- the blog-side
fingerprints (T1/T2/T3) + the full-mode norm kappa=1/30 + the forced 5:4 (1,1):anti block split.
Run: python3 -u code/lichnerowicz_response_fingerprint.py
"""
import sys, time
import sympy as sp
from sympy import Matrix, Rational, I, zeros, cancel, together

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from tensor_probe import (fs_metric, fs_metric_inv, christoffel_hol, phi_field, grad_bilinear,
                          l2_tensor, TrM2_cx)
from lichnerowicz_response import extract_tt

_t0 = time.time()
def _log(m): print(f"[{time.time()-_t0:6.1f}s] {m}", flush=True)

g = fs_metric(); ginv = fs_metric_inv(g); Gam = christoffel_hol(g, ginv)

# The Gell-Mann su(3) matter directions (3x3-complex Hermitian, traceless) + the d2 Cartan probe.
GM = {
    "s01": Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),       # lambda_1
    "a01": Matrix([[0, -I, 0], [I, 0, 0], [0, 0, 0]]),      # lambda_2
    "d1":  Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]),      # lambda_3
    "s02": Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),       # lambda_4
    "a02": Matrix([[0, 0, -I], [0, 0, 0], [I, 0, 0]]),      # lambda_5
    "s12": Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),       # lambda_6
    "a12": Matrix([[0, 0, 0], [0, 0, -I], [0, I, 0]]),      # lambda_7
    "d2":  Matrix([[1, 0, 0], [0, 1, 0], [0, 0, -2]]),      # = sqrt(3) lambda_8
}


def residue(M):
    B3 = grad_bilinear(cancel(phi_field(M)), simp=together)
    r, wh, wa, f, info = extract_tt(B3, g, ginv, Gam, verify=True)
    return r, info


def tadd(*triples_with_coeffs):
    """Sum of (coeff, block-triple): returns a block-triple."""
    out = [zeros(2, 2), zeros(2, 2), zeros(2, 2)]
    for coeff, t in triples_with_coeffs:
        for k in range(3):
            for a in range(2):
                for b in range(2):
                    out[k][a, b] += coeff * t[k][a, b]
    return (out[0], out[1], out[2])


def is_zero(t):
    return all(cancel(t[k][a, b]) == 0 for k in range(3) for a in range(2) for b in range(2))


def main():
    t = {}
    for nm, M in GM.items():
        r, info = residue(M)
        t[nm] = r
        anti_nz = not (is_zero((r[0], zeros(2, 2), zeros(2, 2))) and is_zero((zeros(2, 2), zeros(2, 2), r[2])))
        _log(f"residue[{nm}]: consistent={info.get('consistent')} tr0={info.get('tr_zero')} "
             f"div0={info.get('div_zero')} | (2,0)/(0,2) blocks NONZERO={anti_nz}")

    print("\n" + "=" * 78)
    print("T1: 4(t_s01+t_a01+t_d1) + (t_s02+t_a02+t_s12+t_a12) == 0  (a single-rep relation)")
    print("=" * 78)
    S1 = tadd((4, t["s01"]), (4, t["a01"]), (4, t["d1"]),
              (1, t["s02"]), (1, t["a02"]), (1, t["s12"]), (1, t["a12"]))
    T1 = is_zero(S1)
    _log(f"T1 holds (sum == 0 tensor, all blocks): {T1}")

    print("\n" + "=" * 78)
    print("T2: t_d2 == 9(t_s01+t_a01+t_d1)")
    print("=" * 78)
    S2 = tadd((1, t["d2"]), (-9, t["s01"]), (-9, t["a01"]), (-9, t["d1"]))
    T2 = is_zero(S2)
    _log(f"T2 holds (t_d2 - 9(...) == 0 tensor): {T2}")

    print("\n" + "=" * 78)
    print("NORM: full-mode ||TT(B3)||^2 = l2_tensor(r,r) =? (1/30)(TrM^2)^2 ; block split 5:4")
    print("=" * 78)
    norm_ok = True
    split_ok = True
    for nm in ["s01", "a01", "d1", "s02", "d2"]:
        r = t[nm]; M = GM[nm]
        tr2 = cancel(TrM2_cx(M))
        full = cancel(l2_tensor(r, r, ginv))
        b11 = cancel(l2_tensor((zeros(2, 2), r[1], zeros(2, 2)), (zeros(2, 2), r[1], zeros(2, 2)), ginv))
        bant = cancel(l2_tensor((r[0], zeros(2, 2), r[2]), (r[0], zeros(2, 2), r[2]), ginv))
        pred_full = cancel(Rational(1, 30) * tr2 ** 2)
        pred_11 = cancel(Rational(1, 54) * tr2 ** 2)
        pred_ant = cancel(Rational(2, 135) * tr2 ** 2)
        ok_f = (cancel(full - pred_full) == 0)
        ok_s = (cancel(b11 - pred_11) == 0) and (cancel(bant - pred_ant) == 0)
        norm_ok &= ok_f; split_ok &= ok_s
        ratio = cancel(b11 / bant) if bant != 0 else None
        _log(f"  {nm}: TrM2={tr2}  ||r||^2={full} (=(1/30)TrM2^2? {ok_f})  "
             f"||r11||^2={b11} ||r_anti||^2={bant} ratio={ratio} (5:4 & 1/54,2/135? {ok_s})")

    print("\n" + "=" * 78)
    print("T3: the Gram of the single-generator residues -- rank (expect 6 = P27 single-gen image)")
    print("=" * 78)
    gens = ["s01", "a01", "d1", "s02", "a02", "s12", "a12"]
    n = len(gens)
    G = zeros(n, n)
    for i in range(n):
        for j in range(i, n):
            v = cancel(l2_tensor(t[gens[i]], t[gens[j]], ginv))
            G[i, j] = v; G[j, i] = v
        _log(f"  T3 Gram row {i} done")
    rk = G.rank()
    _log(f"T3 Gram rank over Q = {rk} (expect 6)")

    print("\n" + "=" * 78)
    print(f"FINGERPRINT SUMMARY: T1={T1}  T2={T2}  T3_rank={rk}(==6:{rk==6})  "
          f"norm_full=(1/30)TrM2^2:{norm_ok}  split_5:4:{split_ok}")
    print("=" * 78)
    allok = T1 and T2 and (rk == 6) and norm_ok and split_ok
    print(f"ALL_FINGERPRINTS_PASS = {allok}")
    return allok


if __name__ == "__main__":
    ok = main()
    sys.exit(0 if ok else 1)
